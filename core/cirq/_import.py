# Copyright 2019 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import inspect
from typing import Any, Callable, List, Optional, Sequence

from contextlib import contextmanager
import importlib
import sys

# Bug workaround: https://github.com/python/mypy/issues/1498
import typing

ModuleType = Any


class InstrumentedFinder(importlib.abc.MetaPathFinder):
    """A module finder used to hook the python import statement."""

    def __init__(
        self,
        finder: Any,
        module_name: str,
        wrap_module: Callable[[ModuleType], Optional[ModuleType]],
        after_exec: Callable[[ModuleType], None],
    ):
        """A module finder that uses an existing module finder to find a python
        module spec and intercept the execution of matching modules.

        Replace finders in `sys.meta_path` with instances of this class to
        instrument import statements.

        Args:
            finder: The original module finder to wrap.
            module_name: The fully qualified module name to instrument e.g.
                `'pkg.submodule'`.  Submodules of this are also instrumented.
            wrap_module: A callback function that takes a module object before
                it is run and either modifies or replaces it before it is run.
                The module returned by this function will be executed.  If None
                is returned the module is not executed and may be executed
                later.
            after_exec: A callback function that is called with the return value
                of `wrap_module` after that module was executed if `wrap_module`
                didn't return None.
        """

        self.finder = finder
        self.module_name = module_name
        self.match_components: List[str] = []
        if self.module_name:
            self.match_components = self.module_name.split('.')
        self.wrap_module = wrap_module
        self.after_exec = after_exec

    def find_spec(self, fullname: str, path: Any = None, target: Any = None) -> Any:
        components = fullname.split('.')
        spec = self.finder.find_spec(fullname, path=path, target=target)
        if spec is None:
            return None
        if components[: len(self.match_components)] == self.match_components:
            spec = self.wrap_spec(spec)
        return spec

    def wrap_spec(self, spec: Any) -> Any:
        spec.loader = InstrumentedLoader(spec.loader, self.wrap_module, self.after_exec)
        return spec


class InstrumentedLoader(importlib.abc.Loader):
    """A module loader used to hook the python import statement."""

    def __init__(
        self,
        loader: Any,
        wrap_module: Callable[[ModuleType], Optional[ModuleType]],
        after_exec: Callable[[ModuleType], None],
    ):
        """A module loader that uses an existing module loader and intercepts
        the execution of a module.

        Use `InstrumentedFinder` to instrument modules with instances of this
        class.

        Args:
            loader: The original module loader to wrap.
            module_name: The fully qualified module name to instrument e.g.
                `'pkg.submodule'`.  Submodules of this are also instrumented.
            wrap_module: A callback function that takes a module object before
                it is run and either modifies or replaces it before it is run.
                The module returned by this function will be executed.  If None
                is returned the module is not executed and may be executed
                later.
            after_exec: A callback function that is called with the return value
                of `wrap_module` after that module was executed if `wrap_module`
                didn't return None.
        """
        self.loader = loader
        self.wrap_module = wrap_module
        self.after_exec = after_exec

    def create_module(self, spec: ModuleType) -> ModuleType:
        return self.loader.create_module(spec)

    def exec_module(self, module: ModuleType) -> None:
        module = self.wrap_module(module)
        if module is not None:
            self.loader.exec_module(module)
            self.after_exec(module)


@contextmanager
def wrap_module_executions(
    module_name: str,
    wrap_func: Callable[[ModuleType], Optional[ModuleType]],
    after_exec: Callable[[ModuleType], None] = lambda m: None,
    assert_meta_path_unchanged: bool = True,
):
    """A context manager that hooks python's import machinery within the
    context.

    `wrap_func` is called before executing the module called `module_name` and
    any of its submodules.  The module returned by `wrap_func` will be executed.
    """

    def wrap(finder: Any) -> Any:
        if not hasattr(finder, 'find_spec'):
            return finder
        return InstrumentedFinder(finder, module_name, wrap_func, after_exec)

    new_meta_path = [wrap(finder) for finder in sys.meta_path]

    try:
        orig_meta_path, sys.meta_path = sys.meta_path, new_meta_path
        yield
    finally:
        if assert_meta_path_unchanged:
            assert sys.meta_path == new_meta_path
        sys.meta_path = orig_meta_path


@contextmanager
def delay_import(module_name: str):
    """A context manager that allows the module or submodule named `module_name`
    to be imported without the contents of the module executing until the
    context manager exits.
    """
    delay = True
    execute_list = []

    def wrap_func(module: ModuleType) -> Optional[ModuleType]:
        if delay:
            execute_list.append(module)
            return None  # Don't allow the module to be executed yet
        return module  # Now allow the module to be executed

    with wrap_module_executions(module_name, wrap_func):
        importlib.import_module(module_name)

    yield  # Run the body of the context

    delay = False
    for module in execute_list:
        module.__loader__.exec_module(module)  # Calls back into wrap_func


## Aliasing for cirq.google and others


class AliasingLoader(importlib.abc.Loader):
    """A module loader used to hook the python import statement."""

    def __init__(self, loader: Any, alias: str, real_name: str):
        """A module loader that uses an existing module loader and intercepts
        the execution of a module.

        Use `InstrumentedFinder` to instrument modules with instances of this
        class.

        Args:
            loader: The original module loader to wrap.
            module_name: The fully qualified module name to instrument e.g.
                `'pkg.submodule'`.  Submodules of this are also instrumented.
            wrap_module: A callback function that takes a module object before
                it is run and either modifies or replaces it before it is run.
                The module returned by this function will be executed.  If None
                is returned the module is not executed and may be executed
                later.
            after_exec: A callback function that is called with the return value
                of `wrap_module` after that module was executed if `wrap_module`
                didn't return None.
        """

        def wrap_exec_module(method: Any) -> Any:
            def exec_module(module: ModuleType) -> None:
                print(f"executing module: {module.__name__} {self.alias}->{self.real_name}")
                if not module.__name__.startswith(self.alias):
                    return method(module)
                unaliased_module_name = module.__name__.replace(self.alias, self.real_name)
                if unaliased_module_name not in sys.modules:
                    print("ADDING THE NEW STUFF!")
                    sys.modules[unaliased_module_name] = module
                try:
                    return method(module)
                except Exception as ex:
                    print(f"REMOVING THE NEW STUFF - {ex}")
                    del sys.modules[unaliased_module_name]
                    raise ex

            return exec_module

        def wrap_load_module(method: Any) -> Any:
            def load_module(fullname: str) -> ModuleType:
                print(f"loading module: {fullname}")
                if fullname == self.alias:
                    print(f"but instead with the {self.real_name}")
                    mod = method(self.real_name)
                    return mod
                return method(fullname)

            return load_module

        self.loader = loader
        if hasattr(loader, 'exec_module'):
            self.exec_module = wrap_exec_module(loader.exec_module)
        if hasattr(loader, 'load_module'):
            self.load_module = wrap_load_module(loader.load_module)
        self.alias = alias
        self.real_name = real_name

    def create_module(self, spec: ModuleType) -> ModuleType:
        print(f"creating module: {spec}")
        return self.loader.create_module(spec)

    def module_repr(self, module: ModuleType) -> str:
        return self.loader.module_repr(module)


class AliasingFinder(importlib.abc.MetaPathFinder):
    """A module finder used to hook the python import statement."""

    def __init__(
        self,
        finder: Any,
        module_name: str,
        alias: str,
    ):
        """An aliasing module finder that uses an existing module finder to find a python
        module spec and intercept the execution of matching modules.
        """
        self.finder = finder
        self.module_name = module_name
        self.alias = alias

    def find_spec(self, fullname: str, path: Any = None, target: Any = None) -> Any:
        spec = self.finder.find_spec(fullname, path=path, target=target)
        if spec is not None and fullname.startswith(self.alias):
            unaliased_module_name = fullname.replace(self.alias, self.module_name)
            spec.loader = AliasingLoader(spec.loader, fullname, unaliased_module_name)
        if spec is not None and fullname.startswith(self.module_name):
            unaliased_module_name = fullname.replace(self.module_name, self.alias)
            spec.loader = AliasingLoader(spec.loader, fullname, unaliased_module_name)

        return spec


def deep_alias(module_name: str, alias: str):
    """Creates an alias for a module and all of its submodules in the Python module cache.

    For `module_name` (e.g. google) creates an alias (e.g cirq.google) in Python's module cache. It also
    recursively checks for the already imported submodules (e.g. google.api) and creates the alias for them too
    (e.g. cirq.google.api). With this method it is possible to create an alias that really looks like a module, e.g you
    can do things like `from cirq.google import api` - which would be otherwise impossible.

    While it is not recommended, one could even use this to make this work:

    >>> import numpy as np
    >>> import cirq._import
    >>> cirq._import.deep_alias('numpy', 'np')
    >>> from np import linalg # which would otherwise fail!

    """

    def wrap(finder: Any) -> Any:
        if not hasattr(finder, 'find_spec'):
            return finder
        return AliasingFinder(finder, module_name, alias)

    sys.meta_path = [wrap(finder) for finder in sys.meta_path]

    def replace_descendants(mod):
        if mod not in sys.modules:
            # when a module imports a module as an alias it will also live on the module's namespace, even if it's not a
            # true submodule
            return
        aliased_key = mod.replace(module_name, alias)
        sys.modules[aliased_key] = sys.modules[mod]
        for child in inspect.getmembers(sys.modules[mod], inspect.ismodule):
            replace_descendants(mod + "." + child[0])

    replace_descendants(module_name)

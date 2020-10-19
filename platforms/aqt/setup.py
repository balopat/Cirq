# Copyright 2018 The Cirq Developers
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

import io
import os
from setuptools import find_packages, setup

# This reads the __version__ variable from cirq/_version.py
__version__ = ''
exec(open('_version.py').read())

name = 'cirq-aqt'

description = ('Cirq-aqt')

# README file as long_description.
long_description = "Cirq-aqt"

# Read in requirements
requirements = open('requirements.txt').readlines()
requirements = [r.strip() for r in requirements]

cirq_packages = ['cirq_aqt'] + [
    'cirq_aqt.' + package for package in find_packages(where='cirq_aqt')
]

# Sanity check
assert __version__, 'Version string cannot be empty'

setup(
    name=name,
    version=__version__,
    url='http://github.com/quantumlib/cirq',
    author='The Cirq Developers',
    author_email='cirq@googlegroups.com',
    python_requires=('>=3.6.0'),
    install_requires=requirements,
    license='Apache 2',
    description=description,
    long_description=long_description,
    packages=cirq_packages,
)
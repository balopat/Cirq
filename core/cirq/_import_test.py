

def test_metadata_resolution():
    from importlib import metadata
    assert metadata.version("jsonschema") is not None
    import cirq
    assert metadata.version("jsonschema") is not None
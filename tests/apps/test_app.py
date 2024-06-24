def test_importing_app():
    # this will raise an exception if pydantic model validation fails for th app
    from nomad_example_plugin_app.apps import myapp

    assert myapp.app.label == 'MyApp'


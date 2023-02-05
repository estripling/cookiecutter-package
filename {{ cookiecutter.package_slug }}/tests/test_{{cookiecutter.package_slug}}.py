from importlib import metadata

import {{ cookiecutter.package_slug }}


def test_version():
    assert {{ cookiecutter.package_slug }}.__version__ == metadata.version("{{ cookiecutter.package_slug }}")

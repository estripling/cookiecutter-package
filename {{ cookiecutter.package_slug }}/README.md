<h1 align="center">{{ cookiecutter.package_name }}</h1>

<p align="center">
<a href="https://pypi.org/project/{{ cookiecutter.package_slug }}"><img alt="pypi" src="https://img.shields.io/pypi/v/{{ cookiecutter.package_slug }}"></a>
<a href="https://readthedocs.org/projects/{{ cookiecutter.package_slug }}/?badge=latest"><img alt="docs" src="https://readthedocs.org/projects/{{ cookiecutter.package_slug }}/badge/?version=latest"></a>
<a href="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_slug }}/actions/workflows/ci.yml"><img alt="ci status" src="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_slug }}/actions/workflows/ci.yml/badge.svg?branch=main"></a>
<a href="https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.package_slug }}"><img alt="coverage" src="https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.package_slug }}/coverage.svg?branch=main"></a>
<a href="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_slug }}/blob/main/LICENSE"><img alt="license" src="https://img.shields.io/pypi/l/{{ cookiecutter.package_slug }}"></a>
</p>

## About

{{ cookiecutter.package_short_description }}:

- [Documentation](https://{{ cookiecutter.package_slug }}.readthedocs.io/en/stable/index.html)
- [Example usage](https://{{ cookiecutter.package_slug }}.readthedocs.io/en/stable/example.html)
- [API Reference](https://{{ cookiecutter.package_slug }}.readthedocs.io/en/stable/autoapi/{{ cookiecutter.package_slug }}/index.html)

## Installation

`{{ cookiecutter.package_slug }}` is available on [PyPI](https://pypi.org/project/{{ cookiecutter.package_slug }}/) for Python {{ cookiecutter.python_version }}+:

```console
pip install {{ cookiecutter.package_slug }}
```

## Examples

- TODO

## Contributing to {{ cookiecutter.package_name }}

Your contribution is greatly appreciated!
See the following links to help you get started:

- [Contributing Guide](https://{{ cookiecutter.package_slug }}.readthedocs.io/en/latest/contributing.html)
- [Developer Guide](https://{{ cookiecutter.package_slug }}.readthedocs.io/en/latest/developers.html)
- [Contributor Code of Conduct](https://{{ cookiecutter.package_slug }}.readthedocs.io/en/latest/conduct.html)

## License

`{{ cookiecutter.package_slug }}` was created by {{ cookiecutter.package_developers }}.
{% if cookiecutter.license != "None" -%} It is licensed under the terms of the {{ cookiecutter.license }} license.{% else %}{{ cookiecutter.package_developers }} retains all rights to the source and it may not be reproduced, distributed, or used to create derivative works.{% endif %}

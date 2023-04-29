from importlib import metadata

__version__ = metadata.version("{{ cookiecutter.package_slug }}")

from .core import *

del (
    metadata,
    core,
)

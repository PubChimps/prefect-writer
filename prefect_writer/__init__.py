from . import _version
from .credentials import WriterCredentials

__version__ = _version.get_versions()["version"]

__all__ = ["WriterCredentials"]

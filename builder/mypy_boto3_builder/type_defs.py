"""
Provides compatibility between `typing` and `typing_extensions`.
"""
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict, Literal  # pylint: disable=no-name-in-module
else:
    from typing_extensions import TypedDict, Literal


__all__ = (
    "TypedDict",
    "Literal",
)

"""
Provides compatibility between `typing` and `typing_extensions`.
"""
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict, Literal, overload
else:
    from typing_extensions import TypedDict, Literal, overload


__all__ = (
    "TypedDict",
    "Literal",
    "overload",
)

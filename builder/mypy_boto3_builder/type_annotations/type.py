"""
Predefined FakeAnnotation instances.
"""
from typing import Union, Optional, Any, Dict, List, Callable, IO

from mypy_boto3_builder.type_defs import overload
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_class import TypeClass


class Type:
    """
    Predefined FakeAnnotation instances.
    """

    Union = TypeAnnotation(Union)
    Any = TypeAnnotation(Any)
    Dict = TypeAnnotation(Dict)
    List = TypeAnnotation(List)
    Optional = TypeAnnotation(Optional)
    Callable = TypeAnnotation(Callable)
    IO = TypeAnnotation(IO)
    overload = TypeAnnotation(overload)
    none = TypeConstant(None)
    str = TypeClass(str)
    bool = TypeClass(bool)
    bytes = TypeClass(bytes)
    int = TypeClass(int)
    float = TypeClass(float)
    Ellipsis = TypeConstant(...)

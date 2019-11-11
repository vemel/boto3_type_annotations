import re
import inspect
from typing import List, Any, Pattern, Optional

from mypy_boto3_builder.structures import Argument
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_def import TypeDef
from mypy_boto3_builder.type_map import TYPE_MAP, NAMED_TYPE_MAP
from mypy_boto3_builder.logger import get_logger


class DocstringParser:
    RE_PARAM: Pattern = re.compile(r":param\s+(?P<name>\S+):")
    RE_TYPE: Pattern = re.compile(r":type\s+(?P<name>\S+):\s+(?P<type>.+)")
    RE_RTYPE: Pattern = re.compile(r":rtype:\s+(?P<type>.+)")
    NONE_ANNOTATION: FakeAnnotation = TypeAnnotation(None)

    DEFAULT_METHOD_ARGUMENTS = {
        "create_tags": [
            Argument("self",),
            Argument(
                "Resources", TypeSubscript(TypeAnnotation(List), [TypeAnnotation(Any)]),
            ),
            Argument("Tags", TypeSubscript(TypeAnnotation(List), [TypeDef("Tag")]),),
            Argument("DryRun", TypeAnnotation(bool), TypeAnnotation(False)),
        ]
    }

    def __init__(self) -> None:
        self.logger = get_logger()

    @classmethod
    def get_return_type(cls, docstring: str) -> FakeAnnotation:
        for line in docstring.splitlines():
            line = line.strip()
            if not line.startswith(":rtype:"):
                continue
            match = cls.RE_RTYPE.match(line)
            if not match:
                continue
            return cls.parse_type(match.groupdict()["type"])
        return TypeAnnotation(None)

    @staticmethod
    def _find_argument_or_append(
        argument_name: str, arguments: List[Argument]
    ) -> Argument:
        for argument in arguments:
            if argument.name == argument_name:
                return argument

        for index, argument in enumerate(arguments):
            if argument.prefix == "*":
                del arguments[index]
                break

        for index, argument in enumerate(arguments):
            if argument.prefix == "**":
                del arguments[index]
                break

        arguments.append(Argument(argument_name, default=TypeAnnotation(None)))
        return arguments[-1]

    def get_docless_method_arguments(
        self, method_name: str
    ) -> Optional[List[Argument]]:
        if method_name not in self.DEFAULT_METHOD_ARGUMENTS:
            self.logger.warning(f"Cannot annotate {method_name}")
            return None
        return self.DEFAULT_METHOD_ARGUMENTS[method_name]

    @classmethod
    def get_function_arguments(cls, func: Any) -> List[Argument]:
        argspec = inspect.getfullargspec(func)
        arguments: List[Argument] = []
        for argument_name in argspec.args:
            arguments.append(Argument(argument_name))
        if argspec.defaults:
            for index, default_value in enumerate(argspec.defaults):
                argument_index = len(arguments) - len(argspec.defaults) + index
                arguments[argument_index].default = TypeAnnotation(default_value)

        if argspec.varargs:
            arguments.append(
                Argument(argspec.varargs, prefix="*", type=TypeAnnotation(Any))
            )
        for argument_name in argspec.kwonlyargs:
            arguments.append(Argument(argument_name))
        if argspec.kwonlydefaults:
            for argument_name, default_value in argspec.kwonlydefaults:
                for argument in arguments:
                    if argument.name != argument_name:
                        continue
                    argument.default = TypeAnnotation(default_value)
                    break
        if argspec.varkw:
            arguments.append(
                Argument(argspec.varkw, prefix="**", type=TypeAnnotation(Any))
            )

        return arguments

    @classmethod
    def enrich_arguments(cls, docstring: str, arguments: List[Argument]) -> None:
        for line in docstring.splitlines():
            line = line.strip()
            if line.startswith(":param "):
                match = cls.RE_PARAM.match(line)
                if match:
                    argument_name = match.groupdict()["name"]
                    argument = cls._find_argument_or_append(argument_name, arguments)
                    if "**[REQUIRED]**" in line or "This **must** be set." in line:
                        argument.default = None
            if line.startswith(":type "):
                match = cls.RE_TYPE.match(line)
                if match:
                    argument_name = match.groupdict()["name"]
                    argument_type_str = match.groupdict()["type"]
                    argument = cls._find_argument_or_append(argument_name, arguments)
                    argument.type = cls.parse_type(argument_type_str, argument_name)

        arguments.sort(key=lambda x: x.default is not None)

    @staticmethod
    def parse_type(type_str: str, name: Optional[str] = None) -> FakeAnnotation:
        if name is not None:
            try:
                return NAMED_TYPE_MAP[f"{name}: {type_str}"]
            except KeyError:
                pass

        try:
            return TYPE_MAP[type_str]
        except KeyError:
            raise ValueError(f"Unknown type: {type_str}")

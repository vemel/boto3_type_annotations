import re
import inspect
from typing import List, Any

from mypy_boto3_builder.structures import Argument
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_map import TYPE_MAP


class DocstringParser:
    RE_PARAM = re.compile(r":param\s+(?P<name>\S+):")
    RE_TYPE = re.compile(r":type\s+(?P<name>\S+):\s+(?P<type>.+)")
    RE_RTYPE = re.compile(r":rtype:\s+(?P<type>.+)")

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
            arguments.append(Argument(argspec.varargs, prefix="*"))
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
            arguments.append(Argument(argspec.varkw, prefix="**"))

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
                        argument.required = True
                        argument.default = None
            if line.startswith(":type "):
                match = cls.RE_TYPE.match(line)
                if match:
                    argument_name = match.groupdict()["name"]
                    argument = cls._find_argument_or_append(argument_name, arguments)
                    argument.type = cls.parse_type(match.groupdict()["type"])

        arguments.sort(key=lambda x: x.default is not None)

    @staticmethod
    def parse_type(type_str: str) -> FakeAnnotation:
        try:
            return TYPE_MAP[type_str]
        except KeyError:
            raise ValueError(f"Unknown type: {type_str}")

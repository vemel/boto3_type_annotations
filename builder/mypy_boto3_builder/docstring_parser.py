import re
from typing import List, Dict

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

    @classmethod
    def get_arguments(cls, docstring: str) -> List[Argument]:
        argument_map: Dict[str, Argument] = {}
        for line in docstring.splitlines():
            line = line.strip()
            if line.startswith(":param "):
                match = cls.RE_PARAM.match(line)
                if match:
                    argument_name = match.groupdict()["name"]
                    if argument_name not in argument_map:
                        argument_map[argument_name] = Argument(argument_name)
                    argument = argument_map.get(argument_name, Argument(argument_name))
                    argument_map[argument_name] = argument
                    if "**[REQUIRED]**" in line:
                        argument.required = True
                    if "This **must** be set" in line:
                        argument.required = True
            if line.startswith(":type "):
                match = cls.RE_TYPE.match(line)
                if match:
                    argument_name = match.groupdict()["name"]
                    if argument_name not in argument_map:
                        argument_map[argument_name] = Argument(argument_name)
                    argument = argument_map.get(argument_name, Argument(argument_name))
                    argument_map[argument_name] = argument
                    argument.type = cls.parse_type(match.groupdict()["type"])

        result = list(argument_map.values())
        result.sort(key=lambda x: not x.required)
        return result

    @staticmethod
    def parse_type(type_str: str) -> FakeAnnotation:
        try:
            return TYPE_MAP[type_str]
        except KeyError:
            raise ValueError(f"Unknown type: {type_str}")

"""
Boto3 docstring parser for arguments and return type annotations.
"""
import re
import inspect
from typing import List, Pattern, Optional, Dict, Tuple
from types import FunctionType


from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.type_annotations.type_def import TypeDef
from mypy_boto3_builder.type_maps.type_map import TYPE_MAP
from mypy_boto3_builder.type_maps.named_type_map import NAMED_TYPE_MAP
from mypy_boto3_builder.type_maps.method_type_map import METHOD_TYPE_MAP
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.utils.indent_trimmer import IndentTrimmer


class DocstringParser:
    RE_PARAM: Pattern[str] = re.compile(r":param\s+(?P<name>\S+):")
    RE_TYPE: Pattern[str] = re.compile(r":type\s+(?P<name>\S+):\s+(?P<type>.+)")
    RE_RTYPE: Pattern[str] = re.compile(r":rtype:\s+(?P<type>.+)")

    RE_SYNTAX_DICT_KEY: Pattern[str] = re.compile(
        r"\- \*\*(?P<name>\S+)\*\* \*\((?P<type>.+)\) \-\-\*"
    )
    RE_SYNTAX_TYPE: Pattern[str] = re.compile(r"\- \*\((?P<type>.+)\) \-\-\*")

    DEFAULT_METHOD_ARGUMENTS = {
        "create_tags": [
            Argument("self", None),
            Argument("Resources", TypeSubscript(List, [TypeAnnotation.Any()]),),
            Argument("Tags", TypeSubscript(List, [TypeDef("EC2Tag")]),),
            Argument("DryRun", TypeClass(bool), TypeConstant(False)),
        ]
    }

    def __init__(self) -> None:
        self.logger = get_logger()

    def get_return_type(self, docstring: str, prefix: str) -> FakeAnnotation:
        lines = docstring.splitlines()
        return_type: FakeAnnotation = TypeConstant(None)
        for line in lines:
            line = line.strip()
            if not line.startswith(":rtype:"):
                continue
            match = self.RE_RTYPE.match(line)
            if not match:
                continue
            return_type = self.parse_type(match.groupdict()["type"])
            break
        type_syntax: List[str] = []
        response_syntax_found = False
        for doc_line in lines:
            doc_line = doc_line.rstrip()
            line = doc_line.strip()
            if "**Response Syntax**" in line:
                response_syntax_found = True
            if not response_syntax_found:
                continue
            type_syntax.append(doc_line)

        syntax_return_type = self.parse_any_syntax(
            name="Response", lines=type_syntax, prefix=prefix
        )
        if syntax_return_type is not TypeAnnotation.Any():
            return_type = syntax_return_type
        return return_type

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

        arguments.append(
            Argument(argument_name, TypeAnnotation.Any(), TypeConstant(None))
        )
        return arguments[-1]

    def get_docless_method_arguments(
        self, method_name: str
    ) -> Optional[List[Argument]]:
        if method_name not in self.DEFAULT_METHOD_ARGUMENTS:
            self.logger.warning(f"Cannot annotate {method_name}")
            return None
        return self.DEFAULT_METHOD_ARGUMENTS[method_name]

    @staticmethod
    def _get_arguments_from_argspec(func: FunctionType) -> List[Argument]:
        arguments: List[Argument] = []
        argspec = inspect.getfullargspec(func)
        for argument_name in argspec.args:
            if argument_name == "factory_self":
                argument_name = "self"
            type_annotation: Optional[TypeAnnotation] = TypeAnnotation.Any()
            if not arguments and argument_name in ("self", "cls"):
                type_annotation = None
            arguments.append(Argument(argument_name, type_annotation))
        if argspec.defaults:
            for index, default_value in enumerate(argspec.defaults):
                argument_index = len(arguments) - len(argspec.defaults) + index
                arguments[argument_index].default = TypeConstant(default_value)

        if argspec.varargs:
            arguments.append(
                Argument(argspec.varargs, TypeAnnotation.Any(), prefix="*")
            )
        for argument_name in argspec.kwonlyargs:
            arguments.append(Argument(argument_name, TypeAnnotation.Any()))
        if argspec.kwonlydefaults:
            for argument_name, default_value in argspec.kwonlydefaults:
                for argument in arguments:
                    if argument.name != argument_name:
                        continue
                    argument.default = TypeConstant(default_value)
                    break
        if argspec.varkw:
            arguments.append(Argument(argspec.varkw, TypeAnnotation.Any(), prefix="**"))
        return arguments

    def get_function_arguments(self, func: FunctionType) -> List[Argument]:
        func_name = func.__name__
        arguments = self._get_arguments_from_argspec(func)

        for argument in arguments:
            method_type = f"{func_name}: {argument.name}"
            if method_type in METHOD_TYPE_MAP:
                argument.type = METHOD_TYPE_MAP[method_type]

        return arguments

    def enrich_arguments(
        self, docstring: str, arguments: List[Argument], prefix: str
    ) -> None:
        type_syntax: Dict[str, List[str]] = {}
        argument: Optional[Argument] = None
        argument_line_indent = 0

        for doc_line in docstring.splitlines():
            doc_line = doc_line.rstrip()
            doc_line_indent = IndentTrimmer.get_line_indent(doc_line)
            line = doc_line.strip()
            if line.startswith(":param "):
                match = self.RE_PARAM.match(line)
                if match:
                    argument_line_indent = doc_line_indent
                    argument_name = match.groupdict()["name"]
                    argument = self._find_argument_or_append(argument_name, arguments)
                    if "**[REQUIRED]**" in line or "This **must** be set." in line:
                        argument.default = None
                continue
            if line.startswith(":type "):
                match = self.RE_TYPE.match(line)
                if match:
                    argument_line_indent = doc_line_indent
                    argument_name = match.groupdict()["name"]
                    argument_type_str = match.groupdict()["type"]
                    argument = self._find_argument_or_append(argument_name, arguments)
                    argument.type = self.parse_type(argument_type_str, argument_name)
                continue
            if line and doc_line_indent <= argument_line_indent:
                argument = None
                argument_line_indent = 0
            if argument:
                if argument.name not in type_syntax:
                    type_syntax[argument.name] = []
                type_syntax[argument.name].append(doc_line)

        arguments.sort(key=lambda x: x.default is not None)
        for argument_name, syntax_lines in type_syntax.items():
            argument = self._find_argument_or_append(argument_name, arguments)
            argument_type = self.parse_syntax(
                name=argument.name,
                parent_type=argument.type or TypeSubscript(TypeAnnotation(Dict)),
                lines=syntax_lines,
                prefix=prefix,
            )
            argument.type = argument_type

    @staticmethod
    def parse_type(type_str: str, name: Optional[str] = None) -> FakeAnnotation:
        if name is not None:
            try:
                return NAMED_TYPE_MAP[f"{name}: {type_str}"].copy()
            except KeyError:
                pass

        try:
            return TYPE_MAP[type_str].copy()
        except KeyError:
            raise ValueError(f"Unknown type: {type_str}")

    def parse_any_syntax(
        self, name: str, lines: List[str], prefix: str
    ) -> FakeAnnotation:
        lines = IndentTrimmer.trim_lines(IndentTrimmer.trim_empty_lines(lines))
        for index, line in enumerate(lines):
            match = self.RE_SYNTAX_DICT_KEY.match(line)
            if match:
                return self.parse_typed_dict_syntax(name, lines, prefix)

            match = self.RE_SYNTAX_TYPE.match(line)
            if match:
                type_str = match.groupdict()["type"]
                type_annotation = self.parse_type(type_str)
                sub_lines = lines[index + 1 :]
                if sub_lines:
                    type_annotation = self.parse_syntax(
                        name, type_annotation, sub_lines, prefix=prefix,
                    )
                return type_annotation

        return TypeAnnotation.Any()

    def parse_syntax(
        self, name: str, parent_type: FakeAnnotation, lines: List[str], prefix: str
    ) -> FakeAnnotation:
        if parent_type.is_dict():
            parent_type.remove_children()
            return self.parse_dict_syntax(name, parent_type, lines, prefix)

        child = self.parse_any_syntax(name, lines, prefix)
        if child is not TypeAnnotation.Any():
            if parent_type.is_list():
                parent_type.remove_children()
            parent_type.add_child(child)
        return parent_type

    def parse_dict_syntax(
        self, name: str, parent_type: FakeAnnotation, lines: List[str], prefix: str
    ) -> FakeAnnotation:
        lines = IndentTrimmer.trim_lines(IndentTrimmer.trim_empty_lines(lines))
        for index, line in enumerate(lines):
            match = self.RE_SYNTAX_DICT_KEY.match(line)
            if match:
                return self.parse_typed_dict_syntax(name, lines, prefix)

            match = self.RE_SYNTAX_TYPE.match(line)
            if match:
                type_str = match.groupdict()["type"]
                parent_type.add_child(self.parse_type(type_str))
                sub_lines = lines[index + 1 :]
                parent_type.add_child(self.parse_any_syntax(name, sub_lines, prefix))

        return parent_type

    def parse_typed_dict_syntax(
        self, name: str, lines: List[str], prefix: str
    ) -> TypeTypedDict:
        result = TypeTypedDict(f"{prefix}{name}TypeDef")
        lines = IndentTrimmer.trim_lines(IndentTrimmer.trim_empty_lines(lines))
        line_joined = "\n".join(lines)
        result.docstring = f"Type definition for `{prefix}` `{name}`\n\n{line_joined}"
        line_groups: List[Tuple[str, List[str]]] = []
        for line in lines:
            if line_groups and (line.startswith(" ") or not line.strip()):
                line_groups[-1][1].append(line)
            else:
                line_groups.append((line, []))

        for line, sub_lines in line_groups:
            match = self.RE_SYNTAX_DICT_KEY.match(line)
            if match:
                attr_name = match.groupdict()["name"]
                attr_type_str = match.groupdict()["type"]
                attr_required = "REQUIRED" in line or "**must**" in line
                attr_type = self.parse_type(attr_type_str)
                if sub_lines:
                    attr_type = self.parse_syntax(
                        attr_name, attr_type, sub_lines, prefix=f"{prefix}{name}",
                    )
                result.add_attribute(attr_name, attr_type, attr_required)
        return result


def main() -> None:
    result = DocstringParser().parse_syntax(
        "Test",
        TypeSubscript(TypeAnnotation(Dict)),
        """
          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 60

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60
""".split(
            "\n"
        ),
        prefix="My",
    )
    print(result)
    # print(result.render_class())
    # print(result.children[0].type_annotation.children[-1].render_class())


if __name__ == "__main__":
    main()

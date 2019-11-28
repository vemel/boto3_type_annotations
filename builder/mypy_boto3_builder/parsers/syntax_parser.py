"""
Botocore request syntax parser.
"""
from typing import Dict, Any, List

from pyparsing import (
    Word,
    alphanums,
    alphas,
    Combine,
    printables,
    ZeroOrMore,
    Group,
    Suppress,
    ParseException,
    OneOrMore,
    Optional,
    White,
    Forward,
)

from mypy_boto3_builder.type_maps.syntax_type_map import SYNTAX_TYPE_MAP
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.utils.strings import get_class_prefix


class SyntaxParser:
    """
    Botocore request syntax parser.
    """

    variable_name = Word(alphanums + "_")
    name_value = Word(alphanums + "_")
    string_value = Combine(
        Optional(Word(alphas, max=2))
        + "'"
        + ZeroOrMore(Optional(White()) + Word(printables, excludeChars="'"))
        + "'"
    )
    plain_value = string_value | name_value
    literal_value = Combine(plain_value) + OneOrMore("|" + Combine(plain_value))
    literal_items = Combine(plain_value) + OneOrMore(
        Suppress("|") + Combine(plain_value)
    )
    any_value = Forward()
    list_value = (
        "["
        + Combine(any_value)
        + ZeroOrMore("," + Combine(any_value))
        + Optional(",")
        + "]"
    )
    set_value = (
        "{"
        + Combine(any_value)
        + ZeroOrMore("," + Combine(any_value))
        + Optional(",")
        + "}"
    )
    list_items = (
        Suppress("[")
        + Combine(any_value)
        + ZeroOrMore(Suppress(",") + Combine(any_value))
        + Suppress(Optional(","))
        + Suppress("]")
    )
    dict_value = (
        "{"
        + Group(string_value + ":" + Combine(any_value))
        + ZeroOrMore("," + Group(string_value + ":" + Combine(any_value)))
        + Optional(",")
        + "}"
    )
    dict_items = (
        Suppress("{")
        + Group(string_value + Suppress(":") + Combine(any_value))
        + ZeroOrMore(
            Suppress(",") + Group(string_value + Suppress(":") + Combine(any_value))
        )
        + Suppress(Optional(","))
        + Suppress("}")
    )
    any_value <<= literal_value | list_value | dict_value | set_value | plain_value
    argument = Word(alphanums) + Suppress("=") + Combine(any_value)
    arguments = (
        Group(argument)
        + ZeroOrMore(Suppress(",") + Group(argument))
        + Suppress(Optional(","))
    )
    definition = (
        Suppress(
            variable_name + "=" + variable_name + ZeroOrMore("." + variable_name) + "("
        )
        + arguments
        + Suppress(")")
    )
    docstring = Suppress("**Request Syntax**" + White() + "::") + definition

    @classmethod
    def _parse_constant(cls, value: str) -> Any:
        if value.startswith("'"):
            return value.replace("'", "")

        if value.isdigit():
            return int(value)

        raise ValueError(f"Invalid constant: {value}")

    @classmethod
    def _parse_value(cls, value: str, typed_dict_name: str) -> FakeAnnotation:
        if value in SYNTAX_TYPE_MAP:
            return SYNTAX_TYPE_MAP[value]

        try:
            literal_items = cls.literal_items.parseString(value)
        except ParseException:
            pass
        else:
            literal_values = [cls._parse_constant(i) for i in literal_items]
            return TypeLiteral(*literal_values)

        try:
            list_items = cls.list_items.parseString(value)
        except ParseException:
            pass
        else:
            subscript = TypeSubscript(List)
            for item_index, list_item in enumerate(list_items):
                list_value = cls._parse_value(
                    list_item, f"{typed_dict_name}{item_index}"
                )
                subscript.add_child(list_value)
            return subscript

        try:
            dict_items = cls.dict_items.parseString(value)
        except ParseException:
            pass
        else:
            if dict_items[0][0] in SYNTAX_TYPE_MAP:
                subscript = TypeSubscript(Dict)
                for dict_item_key, dict_item_value in dict_items:
                    key_name = cls._parse_constant(dict_item_key)
                    subscript.add_child(SYNTAX_TYPE_MAP[dict_item_key])
                    subscript.add_child(
                        cls._parse_value(
                            dict_item_value,
                            typed_dict_name + get_class_prefix(key_name),
                        )
                    )
                return subscript
            typed_dict = TypeTypedDict(typed_dict_name)
            for dict_item_key, dict_item_value in dict_items:
                key_name = cls._parse_constant(dict_item_key)
                typed_dict.add_attribute(
                    key_name,
                    cls._parse_value(
                        dict_item_value, typed_dict_name + get_class_prefix(key_name)
                    ),
                    required=False,
                )
            return typed_dict

        return TypeAnnotation.Any()

    @classmethod
    def parse_docstring(
        cls, input_string: str, typed_dict_prefix: str
    ) -> Dict[str, FakeAnnotation]:
        """
        Parse type annotations for request arguments.

        Arguments:
            input_string -- Request syntax from dotocore docs.
            typed_dict_prefix -- Prefix for TypedDict classes.

        Returns:
            Mapping of argument name to its type annotation.
        """
        result: Dict[str, FakeAnnotation] = {}
        for argument_groups, _, _ in cls.docstring.scanString(
            input_string, maxMatches=1
        ):
            for argument_name, argument_value in argument_groups:
                try:
                    value = cls._parse_value(
                        argument_value,
                        get_class_prefix(typed_dict_prefix)
                        + get_class_prefix(argument_name),
                    )
                except ParseException as e:
                    raise ValueError(f"Could not parse {argument_value}: {e}")
                result[argument_name] = value
        return result

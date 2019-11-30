from pyparsing import (
    Word,
    alphanums,
    Group,
    alphas,
    SkipTo,
    Optional,
    delimitedList,
    Combine,
    Forward,
    Literal,
    White,
)


class SyntaxGrammar:
    """
    variable_name ::= alphanums + "_-."
    name_value ::= alphanums + "_-."
    string_value ::= alphas{0,2} "'"  [^"'"]+  "'"
    plain_value ::= string_value | name_value
    literal_value ::= plain_value ("|" plain_value)+
    any_value ::= literal_value | list_value | dict_value | set_value | union_value | func_call | plain_value
    list_value ::= "[" any_value ("," any_value)* [","] "]"
    set_value ::= "{" any_value ("," any_value)* [","] "}"
    func_call ::= name_value "(" plain_value ("," plain_value)* [","] ")"
    dict_value ::= "{" string_value ":" any_value ("," string_value ":" any_value)* [","] "}"
    union_item ::= literal_value | list_value | dict_value | set_value | plain_value
    union_value ::= union_item ("or" union_item)+
    """

    variable_name = Word(alphanums + "_-.")
    name_value = Word(alphanums + "_-.")
    string_value = Combine(Optional(Word(alphas, max=2)) + "'" + SkipTo("'") + "'")
    plain_value = (string_value | name_value).setResultsName("value")
    literal_value = (
        Group(plain_value).setResultsName("literal_first_item")
        + "|"
        + delimitedList(Group(plain_value), delim="|").setResultsName(
            "literal_rest_items"
        )
    )
    any_value = Forward()
    list_value = (
        "["
        + Group(delimitedList(Group(any_value))).setResultsName("list_items")
        + Optional(",")
        + "]"
    )
    set_value = (
        "{"
        + Group(delimitedList(Group(any_value))).setResultsName("set_items")
        + Optional(",")
        + "}"
    )
    func_call = Group(
        name_value.setResultsName("name")
        + "("
        + delimitedList(Group(plain_value)).setResultsName("args")
        + Optional(",")
        + ")"
    ).setResultsName("func_call")
    dict_value = (
        "{"
        + Optional(
            delimitedList(
                Group(
                    string_value.setResultsName("key")
                    + Literal(":").suppress()
                    + Combine(any_value).setResultsName("value")
                )
            ).setResultsName("dict_items")
        )
        + Optional(",")
        + "}"
    )
    union_item = literal_value | list_value | dict_value | set_value | plain_value
    union_value = (
        Group(union_item).setResultsName("union_first_item")
        + Literal("or").suppress()
        + delimitedList(Group(union_item), delim="or",).setResultsName(
            "union_rest_items"
        )
    )
    any_value <<= (
        literal_value
        | list_value
        | dict_value
        | set_value
        | union_value
        | func_call
        | plain_value
    )
    argument = (
        Word(alphanums).setResultsName("name")
        + "="
        + Group(any_value).setResultsName("value")
    )
    definition = (
        SkipTo("(")
        + "("
        + Optional(delimitedList(Group(argument))).setResultsName("arguments")
        + Optional(",")
        + ")"
    )
    request_syntax = "**Request Syntax**" + White() + "::" + definition
    response_syntax = "**Response Syntax**" + White() + "::" + definition

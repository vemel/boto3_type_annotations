# SyntaxGrammar

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.docstring_parser.syntax_grammar](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/syntax_grammar.py) module.

Pyparsing grammar for request and response syntax.

- [mypy-boto3](../../../../README.md#mypy_boto3) / [Modules](../../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../../index.md#mypy-boto3-builder) / [Parsers](../index.md#parsers) / [Docstring Parser](index.md#docstring-parser) / SyntaxGrammar
    - [SyntaxGrammar](#syntaxgrammar)

## SyntaxGrammar

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/syntax_grammar.py#L18)

```python
class SyntaxGrammar():
```

variable_name ::= alphanums + "_-."
name_value ::= alphanums + "_-."
string_value ::= alphas{0,2} "'"  [^']+  "'"
plain_value ::= string_value | name_value
literal_value ::= plain_value ("|" plain_value)+
any_value ::= literal_value | list_value | dict_value | set_value | union_value | func_call | plain_value
list_value ::= "[" any_value ("," any_value)* [","] "]"
set_value ::= "{" any_value ("," any_value)* [","] "}"
func_call ::= name_value "(" any_value ("," any_value)* [","] ")"
empty_dict_value ::= "{" [","] "}"
non_empty_dict_value ::= "{" string_value ":" any_value ("," string_value ":" any_value)* [","] "}"
dict_value ::= empty_dict_value | non_empty_dict_value
union_item ::= literal_value | list_value | dict_value | set_value | plain_value
union_value ::= union_item ("or" union_item)+
argument ::= alphanums "=" any_value
definition ::= [^']+ "(" argument ("," argument)* [","] ")"
request_syntax ::= "**Request Syntax**" "::" definition
response_syntax ::= "**Response Syntax**" "::" (list_value | dict_value)

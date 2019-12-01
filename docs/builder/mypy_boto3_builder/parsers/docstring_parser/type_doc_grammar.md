# TypeDocGrammar

> Auto-generated documentation for [builder.mypy_boto3_builder.parsers.docstring_parser.type_doc_grammar](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_doc_grammar.py) module.

Pyparsing grammar for argument type doc lines.

- [mypy-boto3](../../../../README.md#mypy_boto3) / [Modules](../../../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](../../index.md#mypy-boto3-builder) / [Parsers](../index.md#parsers) / [Docstring Parser](index.md#docstring-parser) / TypeDocGrammar
    - [TypeDocGrammar](#typedocgrammar)
        - [TypeDocGrammar.fail_action](#typedocgrammarfail_action)
        - [TypeDocGrammar.reset](#typedocgrammarreset)

## TypeDocGrammar

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_doc_grammar.py#L18)

```python
class TypeDocGrammar():
```

    EOL ::= [""] "
"
    SOL ::= LINE_START
    line ::= [^EOL]+ EOL
    word ::= alphanums + "_"
    indented_block ::= INDENT (line_indented | any_line)
    line_indented ::= any_line indented_block
    type_definition ::= ":type" [^:]+ ":" [^EOL]+
    rtype_definition ::= ":rtype:" [^EOL]+
    returns_definition ::= (":returns:" | ":return:") [^EOL]+
    param_definition ::= ":param" [^:]+ ":" [^EOL]+ EOL [indented_block]
    response_structure ::= "**Response Structure**" line [indented_block]
    typed_dict_key_line ::= "-" "**" word "**" "*(" word ")" "--*" [^EOL]+ + EOL
    type_line ::= "-" "*(" word ")" "--*" [^EOL]+ + EOL
    any_line ::= typed_dict_key_line | type_line | line

### TypeDocGrammar.fail_action

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_doc_grammar.py#L108)

```python
@classmethod
def fail_action(
    _input_string: str,
    _chr_index: int,
    _source: str,
    _error: str,
) -> None:
```

### TypeDocGrammar.reset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/parsers/docstring_parser/type_doc_grammar.py#L126)

```python
@classmethod
def reset() -> None:
```

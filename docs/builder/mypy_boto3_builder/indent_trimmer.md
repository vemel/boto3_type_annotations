# IndentTrimmer

> Auto-generated documentation for [builder.mypy_boto3_builder.indent_trimmer](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/indent_trimmer.py) module.

Utility for removing indentation for sections and lines.

- [mypy-boto3](../../README.md#mypy_boto3) / [Modules](../../MODULES.md#mypy-boto3-modules) / `Builder` / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / IndentTrimmer
    - [IndentTrimmer](#indenttrimmer)
        - [IndentTrimmer.get_line_indent](#indenttrimmerget_line_indent)
        - [IndentTrimmer.indent_line](#indenttrimmerindent_line)
        - [IndentTrimmer.trim_empty_lines](#indenttrimmertrim_empty_lines)
        - [IndentTrimmer.trim_line](#indenttrimmertrim_line)
        - [IndentTrimmer.trim_lines](#indenttrimmertrim_lines)
        - [IndentTrimmer.trim_text](#indenttrimmertrim_text)

## IndentTrimmer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/indent_trimmer.py#L11)

```python
class IndentTrimmer():
```

Utility for removing indentation for sections and lines.

### IndentTrimmer.get_line_indent

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/indent_trimmer.py#L129)

```python
@staticmethod
def get_line_indent(line: str) -> int:
```

Get indent length of the line.

#### Examples

```python
IndentTrimmer.get_line_indent('   test')
3

IndentTrimmer.get_line_indent('test')
0
```

#### Arguments

- `line` - Line of text.

#### Returns

A number of indentation characters in a beginning of the line.

### IndentTrimmer.indent_line

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/indent_trimmer.py#L150)

```python
@staticmethod
def indent_line(line: str, indent: int) -> str:
```

Indent line with givent length `indent`

#### Examples

```python
IndentTrimmer.indent_line('test', 2)
'  test'
```

#### Arguments

- `line` - Line to indent.
- `indent` - Length of indent in spaces.

#### Returns

An indented line.

### IndentTrimmer.trim_empty_lines

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/indent_trimmer.py#L16)

```python
@staticmethod
def trim_empty_lines(lines: List[str]) -> List[str]:
```

Trim empty lines in the begging and the end of the text.

#### Examples

```python
IndentTrimmer.trim_empty_lines([
    '',
    '  asd',
    ' asd',
    '   asd',
    '  ',
    '',
])
[
    '  asd',
    ' asd',
    '   asd',
]
```

#### Returns

Lines wih no empty lines at start and end.

### IndentTrimmer.trim_line

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/indent_trimmer.py#L102)

```python
@staticmethod
def trim_line(line: str, indent: int) -> str:
```

Trim indent from line if it is empty.

#### Examples

```python
IndentTrimmer.trim_line('     test', 2)
'   test'

IndentTrimmer.trim_line('     test', 6)
'test'

IndentTrimmer.trim_line('     test', 1)
'    test'
```

#### Arguments

- `line` - A line of text.

#### Returns

A line with removed indent.

### IndentTrimmer.trim_lines

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/indent_trimmer.py#L67)

```python
@classmethod
def trim_lines(lines: Iterable[str]) -> List[str]:
```

Trim minimum indent from each line of text.

#### Examples

```python
IndentTrimmer.trim_lines([
    '  asd',
    ' asd',
    '   asd',
])
[
    ' asd',
    'asd',
    '  asd',
]
```

#### Arguments

- `lines` - List of lines.

#### Returns

A list of lines with trimmed indent.

### IndentTrimmer.trim_text

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/builder/mypy_boto3_builder/indent_trimmer.py#L48)

```python
@classmethod
def trim_text(text: str) -> str:
```

Trim minimum indent from each line of text.

#### Examples

```python
IndentTrimmer.trim_text('  asd\n asd\n   asd\n')
' asd\nasd\n  asd\n'
```

#### Arguments

- `text` - Multiline text.

#### Returns

A text with trimmed indent.

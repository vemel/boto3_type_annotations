# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.polly.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Polly](index.md#polly) / Paginator
    - [DescribeVoices](#describevoices)
        - [DescribeVoices().paginate](#describevoicespaginate)
    - [ListLexicons](#listlexicons)
        - [ListLexicons().paginate](#listlexiconspaginate)
    - [ListSpeechSynthesisTasks](#listspeechsynthesistasks)
        - [ListSpeechSynthesisTasks().paginate](#listspeechsynthesistaskspaginate)

## DescribeVoices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/paginator.py#L9)

```python
class DescribeVoices(Paginator):
```

### DescribeVoices().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/paginator.py#L12)

```python
def paginate(
    Engine: str = None,
    LanguageCode: str = None,
    IncludeAdditionalLanguageCodes: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListLexicons

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/paginator.py#L22)

```python
class ListLexicons(Paginator):
```

### ListLexicons().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/paginator.py#L25)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListSpeechSynthesisTasks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/paginator.py#L29)

```python
class ListSpeechSynthesisTasks(Paginator):
```

### ListSpeechSynthesisTasks().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/polly/paginator.py#L32)

```python
def paginate(
    Status: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

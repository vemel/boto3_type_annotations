# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.lex_models.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Lex Models](index.md#lex-models) / Paginator
    - [GetBotAliases](#getbotaliases)
        - [GetBotAliases().paginate](#getbotaliasespaginate)
    - [GetBotChannelAssociations](#getbotchannelassociations)
        - [GetBotChannelAssociations().paginate](#getbotchannelassociationspaginate)
    - [GetBotVersions](#getbotversions)
        - [GetBotVersions().paginate](#getbotversionspaginate)
    - [GetBots](#getbots)
        - [GetBots().paginate](#getbotspaginate)
    - [GetBuiltinIntents](#getbuiltinintents)
        - [GetBuiltinIntents().paginate](#getbuiltinintentspaginate)
    - [GetBuiltinSlotTypes](#getbuiltinslottypes)
        - [GetBuiltinSlotTypes().paginate](#getbuiltinslottypespaginate)
    - [GetIntentVersions](#getintentversions)
        - [GetIntentVersions().paginate](#getintentversionspaginate)
    - [GetIntents](#getintents)
        - [GetIntents().paginate](#getintentspaginate)
    - [GetSlotTypeVersions](#getslottypeversions)
        - [GetSlotTypeVersions().paginate](#getslottypeversionspaginate)
    - [GetSlotTypes](#getslottypes)
        - [GetSlotTypes().paginate](#getslottypespaginate)

## GetBotAliases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L9)

```python
class GetBotAliases(Paginator):
```

### GetBotAliases().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L12)

```python
def paginate(
    botName: str,
    nameContains: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetBotChannelAssociations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L21)

```python
class GetBotChannelAssociations(Paginator):
```

### GetBotChannelAssociations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L24)

```python
def paginate(
    botName: str,
    botAlias: str,
    nameContains: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetBotVersions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L34)

```python
class GetBotVersions(Paginator):
```

### GetBotVersions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L37)

```python
def paginate(
    name: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetBots

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L43)

```python
class GetBots(Paginator):
```

### GetBots().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L46)

```python
def paginate(
    nameContains: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetBuiltinIntents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L52)

```python
class GetBuiltinIntents(Paginator):
```

### GetBuiltinIntents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L55)

```python
def paginate(
    locale: str = None,
    signatureContains: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetBuiltinSlotTypes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L64)

```python
class GetBuiltinSlotTypes(Paginator):
```

### GetBuiltinSlotTypes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L67)

```python
def paginate(
    locale: str = None,
    signatureContains: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetIntentVersions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L76)

```python
class GetIntentVersions(Paginator):
```

### GetIntentVersions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L79)

```python
def paginate(
    name: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetIntents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L85)

```python
class GetIntents(Paginator):
```

### GetIntents().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L88)

```python
def paginate(
    nameContains: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetSlotTypeVersions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L94)

```python
class GetSlotTypeVersions(Paginator):
```

### GetSlotTypeVersions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L97)

```python
def paginate(
    name: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetSlotTypes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L103)

```python
class GetSlotTypes(Paginator):
```

### GetSlotTypes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/lex_models/paginator.py#L106)

```python
def paginate(
    nameContains: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.appsync.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Appsync](index.md#appsync) / Paginator
    - [ListApiKeys](#listapikeys)
        - [ListApiKeys().paginate](#listapikeyspaginate)
    - [ListDataSources](#listdatasources)
        - [ListDataSources().paginate](#listdatasourcespaginate)
    - [ListFunctions](#listfunctions)
        - [ListFunctions().paginate](#listfunctionspaginate)
    - [ListGraphqlApis](#listgraphqlapis)
        - [ListGraphqlApis().paginate](#listgraphqlapispaginate)
    - [ListResolvers](#listresolvers)
        - [ListResolvers().paginate](#listresolverspaginate)
    - [ListResolversByFunction](#listresolversbyfunction)
        - [ListResolversByFunction().paginate](#listresolversbyfunctionpaginate)
    - [ListTypes](#listtypes)
        - [ListTypes().paginate](#listtypespaginate)

## ListApiKeys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/paginator.py#L9)

```python
class ListApiKeys(Paginator):
```

### ListApiKeys().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/paginator.py#L12)

```python
def paginate(
    apiId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListDataSources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/paginator.py#L18)

```python
class ListDataSources(Paginator):
```

### ListDataSources().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/paginator.py#L21)

```python
def paginate(
    apiId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListFunctions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/paginator.py#L27)

```python
class ListFunctions(Paginator):
```

### ListFunctions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/paginator.py#L30)

```python
def paginate(
    apiId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListGraphqlApis

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/paginator.py#L36)

```python
class ListGraphqlApis(Paginator):
```

### ListGraphqlApis().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/paginator.py#L39)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListResolvers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/paginator.py#L43)

```python
class ListResolvers(Paginator):
```

### ListResolvers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/paginator.py#L46)

```python
def paginate(
    apiId: str,
    typeName: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListResolversByFunction

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/paginator.py#L52)

```python
class ListResolversByFunction(Paginator):
```

### ListResolversByFunction().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/paginator.py#L55)

```python
def paginate(
    apiId: str,
    functionId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListTypes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/paginator.py#L61)

```python
class ListTypes(Paginator):
```

### ListTypes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/paginator.py#L64)

```python
def paginate(
    apiId: str,
    format: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

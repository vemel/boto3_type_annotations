# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.apigatewayv2.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Apigatewayv2](index.md#apigatewayv2) / Paginator
    - [GetApis](#getapis)
        - [GetApis().paginate](#getapispaginate)
    - [GetAuthorizers](#getauthorizers)
        - [GetAuthorizers().paginate](#getauthorizerspaginate)
    - [GetDeployments](#getdeployments)
        - [GetDeployments().paginate](#getdeploymentspaginate)
    - [GetDomainNames](#getdomainnames)
        - [GetDomainNames().paginate](#getdomainnamespaginate)
    - [GetIntegrationResponses](#getintegrationresponses)
        - [GetIntegrationResponses().paginate](#getintegrationresponsespaginate)
    - [GetIntegrations](#getintegrations)
        - [GetIntegrations().paginate](#getintegrationspaginate)
    - [GetModels](#getmodels)
        - [GetModels().paginate](#getmodelspaginate)
    - [GetRouteResponses](#getrouteresponses)
        - [GetRouteResponses().paginate](#getrouteresponsespaginate)
    - [GetRoutes](#getroutes)
        - [GetRoutes().paginate](#getroutespaginate)
    - [GetStages](#getstages)
        - [GetStages().paginate](#getstagespaginate)

## GetApis

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L9)

```python
class GetApis(Paginator):
```

### GetApis().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L12)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## GetAuthorizers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L16)

```python
class GetAuthorizers(Paginator):
```

### GetAuthorizers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L19)

```python
def paginate(
    ApiId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetDeployments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L25)

```python
class GetDeployments(Paginator):
```

### GetDeployments().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L28)

```python
def paginate(
    ApiId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetDomainNames

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L34)

```python
class GetDomainNames(Paginator):
```

### GetDomainNames().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L37)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## GetIntegrationResponses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L41)

```python
class GetIntegrationResponses(Paginator):
```

### GetIntegrationResponses().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L44)

```python
def paginate(
    ApiId: str,
    IntegrationId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetIntegrations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L50)

```python
class GetIntegrations(Paginator):
```

### GetIntegrations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L53)

```python
def paginate(
    ApiId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetModels

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L59)

```python
class GetModels(Paginator):
```

### GetModels().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L62)

```python
def paginate(
    ApiId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetRouteResponses

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L68)

```python
class GetRouteResponses(Paginator):
```

### GetRouteResponses().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L71)

```python
def paginate(
    ApiId: str,
    RouteId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetRoutes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L77)

```python
class GetRoutes(Paginator):
```

### GetRoutes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L80)

```python
def paginate(
    ApiId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetStages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L86)

```python
class GetStages(Paginator):
```

### GetStages().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/apigatewayv2/paginator.py#L89)

```python
def paginate(
    ApiId: str,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

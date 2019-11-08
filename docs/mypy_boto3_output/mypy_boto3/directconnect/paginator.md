# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.directconnect.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Directconnect](index.md#directconnect) / Paginator
    - [DescribeDirectConnectGatewayAssociations](#describedirectconnectgatewayassociations)
        - [DescribeDirectConnectGatewayAssociations().paginate](#describedirectconnectgatewayassociationspaginate)
    - [DescribeDirectConnectGatewayAttachments](#describedirectconnectgatewayattachments)
        - [DescribeDirectConnectGatewayAttachments().paginate](#describedirectconnectgatewayattachmentspaginate)
    - [DescribeDirectConnectGateways](#describedirectconnectgateways)
        - [DescribeDirectConnectGateways().paginate](#describedirectconnectgatewayspaginate)

## DescribeDirectConnectGatewayAssociations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/paginator.py#L9)

```python
class DescribeDirectConnectGatewayAssociations(Paginator):
```

### DescribeDirectConnectGatewayAssociations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/paginator.py#L12)

```python
def paginate(
    associationId: str = None,
    associatedGatewayId: str = None,
    directConnectGatewayId: str = None,
    virtualGatewayId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDirectConnectGatewayAttachments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/paginator.py#L23)

```python
class DescribeDirectConnectGatewayAttachments(Paginator):
```

### DescribeDirectConnectGatewayAttachments().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/paginator.py#L26)

```python
def paginate(
    directConnectGatewayId: str = None,
    virtualInterfaceId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeDirectConnectGateways

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/paginator.py#L35)

```python
class DescribeDirectConnectGateways(Paginator):
```

### DescribeDirectConnectGateways().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/directconnect/paginator.py#L38)

```python
def paginate(
    directConnectGatewayId: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

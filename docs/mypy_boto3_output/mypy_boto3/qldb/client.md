# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.qldb.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Qldb](index.md#qldb) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_ledger](#clientcreate_ledger)
        - [Client().delete_ledger](#clientdelete_ledger)
        - [Client().describe_journal_s3_export](#clientdescribe_journal_s3_export)
        - [Client().describe_ledger](#clientdescribe_ledger)
        - [Client().export_journal_to_s3](#clientexport_journal_to_s3)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_block](#clientget_block)
        - [Client().get_digest](#clientget_digest)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_revision](#clientget_revision)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_journal_s3_exports](#clientlist_journal_s3_exports)
        - [Client().list_journal_s3_exports_for_ledger](#clientlist_journal_s3_exports_for_ledger)
        - [Client().list_ledgers](#clientlist_ledgers)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_ledger](#clientupdate_ledger)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_ledger

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L20)

```python
def create_ledger(
    Name: str,
    PermissionsMode: str,
    Tags: Dict[str, Any] = None,
    DeletionProtection: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_ledger

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L30)

```python
def delete_ledger(Name: str) -> None:
```

### Client().describe_journal_s3_export

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L34)

```python
def describe_journal_s3_export(Name: str, ExportId: str) -> Dict[str, Any]:
```

### Client().describe_ledger

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L38)

```python
def describe_ledger(Name: str) -> Dict[str, Any]:
```

### Client().export_journal_to_s3

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L42)

```python
def export_journal_to_s3(
    Name: str,
    InclusiveStartTime: datetime,
    ExclusiveEndTime: datetime,
    S3ExportConfiguration: Dict[str, Any],
    RoleArn: str,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L53)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_block

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L63)

```python
def get_block(
    Name: str,
    BlockAddress: Dict[str, Any],
    DigestTipAddress: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().get_digest

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L72)

```python
def get_digest(Name: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L76)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_revision

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L80)

```python
def get_revision(
    Name: str,
    BlockAddress: Dict[str, Any],
    DocumentId: str,
    DigestTipAddress: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L90)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_journal_s3_exports

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L94)

```python
def list_journal_s3_exports(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_journal_s3_exports_for_ledger

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L100)

```python
def list_journal_s3_exports_for_ledger(
    Name: str,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_ledgers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L106)

```python
def list_ledgers(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L112)

```python
def list_tags_for_resource(ResourceArn: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L116)

```python
def tag_resource(ResourceArn: str, Tags: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L120)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_ledger

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/qldb/client.py#L124)

```python
def update_ledger(
    Name: str,
    DeletionProtection: bool = None,
) -> Dict[str, Any]:
```

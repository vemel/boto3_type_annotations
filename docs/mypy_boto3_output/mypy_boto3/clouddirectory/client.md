# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.clouddirectory.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Clouddirectory](index.md#clouddirectory) / Client
    - [Client](#client)
        - [Client().add_facet_to_object](#clientadd_facet_to_object)
        - [Client().apply_schema](#clientapply_schema)
        - [Client().attach_object](#clientattach_object)
        - [Client().attach_policy](#clientattach_policy)
        - [Client().attach_to_index](#clientattach_to_index)
        - [Client().attach_typed_link](#clientattach_typed_link)
        - [Client().batch_read](#clientbatch_read)
        - [Client().batch_write](#clientbatch_write)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_directory](#clientcreate_directory)
        - [Client().create_facet](#clientcreate_facet)
        - [Client().create_index](#clientcreate_index)
        - [Client().create_object](#clientcreate_object)
        - [Client().create_schema](#clientcreate_schema)
        - [Client().create_typed_link_facet](#clientcreate_typed_link_facet)
        - [Client().delete_directory](#clientdelete_directory)
        - [Client().delete_facet](#clientdelete_facet)
        - [Client().delete_object](#clientdelete_object)
        - [Client().delete_schema](#clientdelete_schema)
        - [Client().delete_typed_link_facet](#clientdelete_typed_link_facet)
        - [Client().detach_from_index](#clientdetach_from_index)
        - [Client().detach_object](#clientdetach_object)
        - [Client().detach_policy](#clientdetach_policy)
        - [Client().detach_typed_link](#clientdetach_typed_link)
        - [Client().disable_directory](#clientdisable_directory)
        - [Client().enable_directory](#clientenable_directory)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_applied_schema_version](#clientget_applied_schema_version)
        - [Client().get_directory](#clientget_directory)
        - [Client().get_facet](#clientget_facet)
        - [Client().get_link_attributes](#clientget_link_attributes)
        - [Client().get_object_attributes](#clientget_object_attributes)
        - [Client().get_object_information](#clientget_object_information)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_schema_as_json](#clientget_schema_as_json)
        - [Client().get_typed_link_facet_information](#clientget_typed_link_facet_information)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_applied_schema_arns](#clientlist_applied_schema_arns)
        - [Client().list_attached_indices](#clientlist_attached_indices)
        - [Client().list_development_schema_arns](#clientlist_development_schema_arns)
        - [Client().list_directories](#clientlist_directories)
        - [Client().list_facet_attributes](#clientlist_facet_attributes)
        - [Client().list_facet_names](#clientlist_facet_names)
        - [Client().list_incoming_typed_links](#clientlist_incoming_typed_links)
        - [Client().list_index](#clientlist_index)
        - [Client().list_managed_schema_arns](#clientlist_managed_schema_arns)
        - [Client().list_object_attributes](#clientlist_object_attributes)
        - [Client().list_object_children](#clientlist_object_children)
        - [Client().list_object_parent_paths](#clientlist_object_parent_paths)
        - [Client().list_object_parents](#clientlist_object_parents)
        - [Client().list_object_policies](#clientlist_object_policies)
        - [Client().list_outgoing_typed_links](#clientlist_outgoing_typed_links)
        - [Client().list_policy_attachments](#clientlist_policy_attachments)
        - [Client().list_published_schema_arns](#clientlist_published_schema_arns)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_typed_link_facet_attributes](#clientlist_typed_link_facet_attributes)
        - [Client().list_typed_link_facet_names](#clientlist_typed_link_facet_names)
        - [Client().lookup_policy](#clientlookup_policy)
        - [Client().publish_schema](#clientpublish_schema)
        - [Client().put_schema_from_json](#clientput_schema_from_json)
        - [Client().remove_facet_from_object](#clientremove_facet_from_object)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_facet](#clientupdate_facet)
        - [Client().update_link_attributes](#clientupdate_link_attributes)
        - [Client().update_object_attributes](#clientupdate_object_attributes)
        - [Client().update_schema](#clientupdate_schema)
        - [Client().update_typed_link_facet](#clientupdate_typed_link_facet)
        - [Client().upgrade_applied_schema](#clientupgrade_applied_schema)
        - [Client().upgrade_published_schema](#clientupgrade_published_schema)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L12)

```python
class Client(BaseClient):
```

### Client().add_facet_to_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L15)

```python
def add_facet_to_object(
    DirectoryArn: str,
    SchemaFacet: Dict[str, Any],
    ObjectReference: Dict[str, Any],
    ObjectAttributeList: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().apply_schema

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L25)

```python
def apply_schema(
    PublishedSchemaArn: str,
    DirectoryArn: str,
) -> Dict[str, Any]:
```

### Client().attach_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L31)

```python
def attach_object(
    DirectoryArn: str,
    ParentReference: Dict[str, Any],
    ChildReference: Dict[str, Any],
    LinkName: str,
) -> Dict[str, Any]:
```

### Client().attach_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L41)

```python
def attach_policy(
    DirectoryArn: str,
    PolicyReference: Dict[str, Any],
    ObjectReference: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().attach_to_index

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L50)

```python
def attach_to_index(
    DirectoryArn: str,
    IndexReference: Dict[str, Any],
    TargetReference: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().attach_typed_link

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L59)

```python
def attach_typed_link(
    DirectoryArn: str,
    SourceObjectReference: Dict[str, Any],
    TargetObjectReference: Dict[str, Any],
    TypedLinkFacet: Dict[str, Any],
    Attributes: List[Any],
) -> Dict[str, Any]:
```

### Client().batch_read

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L70)

```python
def batch_read(
    DirectoryArn: str,
    Operations: List[Any],
    ConsistencyLevel: str = None,
) -> Dict[str, Any]:
```

### Client().batch_write

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L76)

```python
def batch_write(DirectoryArn: str, Operations: List[Any]) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L80)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_directory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L84)

```python
def create_directory(Name: str, SchemaArn: str) -> Dict[str, Any]:
```

### Client().create_facet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L88)

```python
def create_facet(
    SchemaArn: str,
    Name: str,
    Attributes: List[Any] = None,
    ObjectType: str = None,
    FacetStyle: str = None,
) -> Dict[str, Any]:
```

### Client().create_index

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L99)

```python
def create_index(
    DirectoryArn: str,
    OrderedIndexedAttributeList: List[Any],
    IsUnique: bool,
    ParentReference: Dict[str, Any] = None,
    LinkName: str = None,
) -> Dict[str, Any]:
```

### Client().create_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L110)

```python
def create_object(
    DirectoryArn: str,
    SchemaFacets: List[Any],
    ObjectAttributeList: List[Any] = None,
    ParentReference: Dict[str, Any] = None,
    LinkName: str = None,
) -> Dict[str, Any]:
```

### Client().create_schema

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L121)

```python
def create_schema(Name: str) -> Dict[str, Any]:
```

### Client().create_typed_link_facet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L125)

```python
def create_typed_link_facet(
    SchemaArn: str,
    Facet: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().delete_directory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L131)

```python
def delete_directory(DirectoryArn: str) -> Dict[str, Any]:
```

### Client().delete_facet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L135)

```python
def delete_facet(SchemaArn: str, Name: str) -> Dict[str, Any]:
```

### Client().delete_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L139)

```python
def delete_object(
    DirectoryArn: str,
    ObjectReference: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().delete_schema

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L145)

```python
def delete_schema(SchemaArn: str) -> Dict[str, Any]:
```

### Client().delete_typed_link_facet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L149)

```python
def delete_typed_link_facet(SchemaArn: str, Name: str) -> Dict[str, Any]:
```

### Client().detach_from_index

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L153)

```python
def detach_from_index(
    DirectoryArn: str,
    IndexReference: Dict[str, Any],
    TargetReference: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().detach_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L162)

```python
def detach_object(
    DirectoryArn: str,
    ParentReference: Dict[str, Any],
    LinkName: str,
) -> Dict[str, Any]:
```

### Client().detach_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L168)

```python
def detach_policy(
    DirectoryArn: str,
    PolicyReference: Dict[str, Any],
    ObjectReference: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().detach_typed_link

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L177)

```python
def detach_typed_link(
    DirectoryArn: str,
    TypedLinkSpecifier: Dict[str, Any],
) -> None:
```

### Client().disable_directory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L183)

```python
def disable_directory(DirectoryArn: str) -> Dict[str, Any]:
```

### Client().enable_directory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L187)

```python
def enable_directory(DirectoryArn: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L191)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_applied_schema_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L201)

```python
def get_applied_schema_version(SchemaArn: str) -> Dict[str, Any]:
```

### Client().get_directory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L205)

```python
def get_directory(DirectoryArn: str) -> Dict[str, Any]:
```

### Client().get_facet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L209)

```python
def get_facet(SchemaArn: str, Name: str) -> Dict[str, Any]:
```

### Client().get_link_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L213)

```python
def get_link_attributes(
    DirectoryArn: str,
    TypedLinkSpecifier: Dict[str, Any],
    AttributeNames: List[Any],
    ConsistencyLevel: str = None,
) -> Dict[str, Any]:
```

### Client().get_object_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L223)

```python
def get_object_attributes(
    DirectoryArn: str,
    ObjectReference: Dict[str, Any],
    SchemaFacet: Dict[str, Any],
    AttributeNames: List[Any],
    ConsistencyLevel: str = None,
) -> Dict[str, Any]:
```

### Client().get_object_information

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L234)

```python
def get_object_information(
    DirectoryArn: str,
    ObjectReference: Dict[str, Any],
    ConsistencyLevel: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L243)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_schema_as_json

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L247)

```python
def get_schema_as_json(SchemaArn: str) -> Dict[str, Any]:
```

### Client().get_typed_link_facet_information

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L251)

```python
def get_typed_link_facet_information(
    SchemaArn: str,
    Name: str,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L257)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_applied_schema_arns

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L261)

```python
def list_applied_schema_arns(
    DirectoryArn: str,
    SchemaArn: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_attached_indices

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L271)

```python
def list_attached_indices(
    DirectoryArn: str,
    TargetReference: Dict[str, Any],
    NextToken: str = None,
    MaxResults: int = None,
    ConsistencyLevel: str = None,
) -> Dict[str, Any]:
```

### Client().list_development_schema_arns

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L282)

```python
def list_development_schema_arns(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_directories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L288)

```python
def list_directories(
    NextToken: str = None,
    MaxResults: int = None,
    state: str = None,
) -> Dict[str, Any]:
```

### Client().list_facet_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L294)

```python
def list_facet_attributes(
    SchemaArn: str,
    Name: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_facet_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L300)

```python
def list_facet_names(
    SchemaArn: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_incoming_typed_links

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L306)

```python
def list_incoming_typed_links(
    DirectoryArn: str,
    ObjectReference: Dict[str, Any],
    FilterAttributeRanges: List[Any] = None,
    FilterTypedLink: Dict[str, Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
    ConsistencyLevel: str = None,
) -> Dict[str, Any]:
```

### Client().list_index

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L319)

```python
def list_index(
    DirectoryArn: str,
    IndexReference: Dict[str, Any],
    RangesOnIndexedValues: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
    ConsistencyLevel: str = None,
) -> Dict[str, Any]:
```

### Client().list_managed_schema_arns

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L331)

```python
def list_managed_schema_arns(
    SchemaArn: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_object_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L337)

```python
def list_object_attributes(
    DirectoryArn: str,
    ObjectReference: Dict[str, Any],
    NextToken: str = None,
    MaxResults: int = None,
    ConsistencyLevel: str = None,
    FacetFilter: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().list_object_children

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L349)

```python
def list_object_children(
    DirectoryArn: str,
    ObjectReference: Dict[str, Any],
    NextToken: str = None,
    MaxResults: int = None,
    ConsistencyLevel: str = None,
) -> Dict[str, Any]:
```

### Client().list_object_parent_paths

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L360)

```python
def list_object_parent_paths(
    DirectoryArn: str,
    ObjectReference: Dict[str, Any],
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_object_parents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L370)

```python
def list_object_parents(
    DirectoryArn: str,
    ObjectReference: Dict[str, Any],
    NextToken: str = None,
    MaxResults: int = None,
    ConsistencyLevel: str = None,
    IncludeAllLinksToEachParent: bool = None,
) -> Dict[str, Any]:
```

### Client().list_object_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L382)

```python
def list_object_policies(
    DirectoryArn: str,
    ObjectReference: Dict[str, Any],
    NextToken: str = None,
    MaxResults: int = None,
    ConsistencyLevel: str = None,
) -> Dict[str, Any]:
```

### Client().list_outgoing_typed_links

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L393)

```python
def list_outgoing_typed_links(
    DirectoryArn: str,
    ObjectReference: Dict[str, Any],
    FilterAttributeRanges: List[Any] = None,
    FilterTypedLink: Dict[str, Any] = None,
    NextToken: str = None,
    MaxResults: int = None,
    ConsistencyLevel: str = None,
) -> Dict[str, Any]:
```

### Client().list_policy_attachments

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L406)

```python
def list_policy_attachments(
    DirectoryArn: str,
    PolicyReference: Dict[str, Any],
    NextToken: str = None,
    MaxResults: int = None,
    ConsistencyLevel: str = None,
) -> Dict[str, Any]:
```

### Client().list_published_schema_arns

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L417)

```python
def list_published_schema_arns(
    SchemaArn: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L423)

```python
def list_tags_for_resource(
    ResourceArn: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_typed_link_facet_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L429)

```python
def list_typed_link_facet_attributes(
    SchemaArn: str,
    Name: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_typed_link_facet_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L435)

```python
def list_typed_link_facet_names(
    SchemaArn: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().lookup_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L441)

```python
def lookup_policy(
    DirectoryArn: str,
    ObjectReference: Dict[str, Any],
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().publish_schema

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L451)

```python
def publish_schema(
    DevelopmentSchemaArn: str,
    Version: str,
    MinorVersion: str = None,
    Name: str = None,
) -> Dict[str, Any]:
```

### Client().put_schema_from_json

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L461)

```python
def put_schema_from_json(SchemaArn: str, Document: str) -> Dict[str, Any]:
```

### Client().remove_facet_from_object

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L465)

```python
def remove_facet_from_object(
    DirectoryArn: str,
    SchemaFacet: Dict[str, Any],
    ObjectReference: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L474)

```python
def tag_resource(ResourceArn: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L478)

```python
def untag_resource(ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_facet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L482)

```python
def update_facet(
    SchemaArn: str,
    Name: str,
    AttributeUpdates: List[Any] = None,
    ObjectType: str = None,
) -> Dict[str, Any]:
```

### Client().update_link_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L492)

```python
def update_link_attributes(
    DirectoryArn: str,
    TypedLinkSpecifier: Dict[str, Any],
    AttributeUpdates: List[Any],
) -> Dict[str, Any]:
```

### Client().update_object_attributes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L501)

```python
def update_object_attributes(
    DirectoryArn: str,
    ObjectReference: Dict[str, Any],
    AttributeUpdates: List[Any],
) -> Dict[str, Any]:
```

### Client().update_schema

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L510)

```python
def update_schema(SchemaArn: str, Name: str) -> Dict[str, Any]:
```

### Client().update_typed_link_facet

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L514)

```python
def update_typed_link_facet(
    SchemaArn: str,
    Name: str,
    AttributeUpdates: List[Any],
    IdentityAttributeOrder: List[Any],
) -> Dict[str, Any]:
```

### Client().upgrade_applied_schema

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L524)

```python
def upgrade_applied_schema(
    PublishedSchemaArn: str,
    DirectoryArn: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

### Client().upgrade_published_schema

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/clouddirectory/client.py#L530)

```python
def upgrade_published_schema(
    DevelopmentSchemaArn: str,
    PublishedSchemaArn: str,
    MinorVersion: str,
    DryRun: bool = None,
) -> Dict[str, Any]:
```

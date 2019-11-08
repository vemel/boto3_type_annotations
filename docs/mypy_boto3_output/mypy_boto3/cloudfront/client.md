# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloudfront.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloudfront](index.md#cloudfront) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_cloud_front_origin_access_identity](#clientcreate_cloud_front_origin_access_identity)
        - [Client().create_distribution](#clientcreate_distribution)
        - [Client().create_distribution_with_tags](#clientcreate_distribution_with_tags)
        - [Client().create_field_level_encryption_config](#clientcreate_field_level_encryption_config)
        - [Client().create_field_level_encryption_profile](#clientcreate_field_level_encryption_profile)
        - [Client().create_invalidation](#clientcreate_invalidation)
        - [Client().create_public_key](#clientcreate_public_key)
        - [Client().create_streaming_distribution](#clientcreate_streaming_distribution)
        - [Client().create_streaming_distribution_with_tags](#clientcreate_streaming_distribution_with_tags)
        - [Client().delete_cloud_front_origin_access_identity](#clientdelete_cloud_front_origin_access_identity)
        - [Client().delete_distribution](#clientdelete_distribution)
        - [Client().delete_field_level_encryption_config](#clientdelete_field_level_encryption_config)
        - [Client().delete_field_level_encryption_profile](#clientdelete_field_level_encryption_profile)
        - [Client().delete_public_key](#clientdelete_public_key)
        - [Client().delete_streaming_distribution](#clientdelete_streaming_distribution)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_cloud_front_origin_access_identity](#clientget_cloud_front_origin_access_identity)
        - [Client().get_cloud_front_origin_access_identity_config](#clientget_cloud_front_origin_access_identity_config)
        - [Client().get_distribution](#clientget_distribution)
        - [Client().get_distribution_config](#clientget_distribution_config)
        - [Client().get_field_level_encryption](#clientget_field_level_encryption)
        - [Client().get_field_level_encryption_config](#clientget_field_level_encryption_config)
        - [Client().get_field_level_encryption_profile](#clientget_field_level_encryption_profile)
        - [Client().get_field_level_encryption_profile_config](#clientget_field_level_encryption_profile_config)
        - [Client().get_invalidation](#clientget_invalidation)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_public_key](#clientget_public_key)
        - [Client().get_public_key_config](#clientget_public_key_config)
        - [Client().get_streaming_distribution](#clientget_streaming_distribution)
        - [Client().get_streaming_distribution_config](#clientget_streaming_distribution_config)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_cloud_front_origin_access_identities](#clientlist_cloud_front_origin_access_identities)
        - [Client().list_distributions](#clientlist_distributions)
        - [Client().list_distributions_by_web_acl_id](#clientlist_distributions_by_web_acl_id)
        - [Client().list_field_level_encryption_configs](#clientlist_field_level_encryption_configs)
        - [Client().list_field_level_encryption_profiles](#clientlist_field_level_encryption_profiles)
        - [Client().list_invalidations](#clientlist_invalidations)
        - [Client().list_public_keys](#clientlist_public_keys)
        - [Client().list_streaming_distributions](#clientlist_streaming_distributions)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_cloud_front_origin_access_identity](#clientupdate_cloud_front_origin_access_identity)
        - [Client().update_distribution](#clientupdate_distribution)
        - [Client().update_field_level_encryption_config](#clientupdate_field_level_encryption_config)
        - [Client().update_field_level_encryption_profile](#clientupdate_field_level_encryption_profile)
        - [Client().update_public_key](#clientupdate_public_key)
        - [Client().update_streaming_distribution](#clientupdate_streaming_distribution)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L11)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L14)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_cloud_front_origin_access_identity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L18)

```python
def create_cloud_front_origin_access_identity(
    CloudFrontOriginAccessIdentityConfig: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_distribution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L24)

```python
def create_distribution(DistributionConfig: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().create_distribution_with_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L28)

```python
def create_distribution_with_tags(
    DistributionConfigWithTags: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_field_level_encryption_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L34)

```python
def create_field_level_encryption_config(
    FieldLevelEncryptionConfig: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_field_level_encryption_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L40)

```python
def create_field_level_encryption_profile(
    FieldLevelEncryptionProfileConfig: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_invalidation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L46)

```python
def create_invalidation(
    DistributionId: str,
    InvalidationBatch: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_public_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L52)

```python
def create_public_key(PublicKeyConfig: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().create_streaming_distribution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L56)

```python
def create_streaming_distribution(
    StreamingDistributionConfig: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_streaming_distribution_with_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L62)

```python
def create_streaming_distribution_with_tags(
    StreamingDistributionConfigWithTags: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().delete_cloud_front_origin_access_identity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L68)

```python
def delete_cloud_front_origin_access_identity(
    Id: str,
    IfMatch: str = None,
) -> None:
```

### Client().delete_distribution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L74)

```python
def delete_distribution(Id: str, IfMatch: str = None) -> None:
```

### Client().delete_field_level_encryption_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L78)

```python
def delete_field_level_encryption_config(
    Id: str,
    IfMatch: str = None,
) -> None:
```

### Client().delete_field_level_encryption_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L84)

```python
def delete_field_level_encryption_profile(
    Id: str,
    IfMatch: str = None,
) -> None:
```

### Client().delete_public_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L90)

```python
def delete_public_key(Id: str, IfMatch: str = None) -> None:
```

### Client().delete_streaming_distribution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L94)

```python
def delete_streaming_distribution(Id: str, IfMatch: str = None) -> None:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L98)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_cloud_front_origin_access_identity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L108)

```python
def get_cloud_front_origin_access_identity(Id: str) -> Dict[str, Any]:
```

### Client().get_cloud_front_origin_access_identity_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L112)

```python
def get_cloud_front_origin_access_identity_config(Id: str) -> Dict[str, Any]:
```

### Client().get_distribution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L116)

```python
def get_distribution(Id: str) -> Dict[str, Any]:
```

### Client().get_distribution_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L120)

```python
def get_distribution_config(Id: str) -> Dict[str, Any]:
```

### Client().get_field_level_encryption

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L124)

```python
def get_field_level_encryption(Id: str) -> Dict[str, Any]:
```

### Client().get_field_level_encryption_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L128)

```python
def get_field_level_encryption_config(Id: str) -> Dict[str, Any]:
```

### Client().get_field_level_encryption_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L132)

```python
def get_field_level_encryption_profile(Id: str) -> Dict[str, Any]:
```

### Client().get_field_level_encryption_profile_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L136)

```python
def get_field_level_encryption_profile_config(Id: str) -> Dict[str, Any]:
```

### Client().get_invalidation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L140)

```python
def get_invalidation(DistributionId: str, Id: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L144)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_public_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L148)

```python
def get_public_key(Id: str) -> Dict[str, Any]:
```

### Client().get_public_key_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L152)

```python
def get_public_key_config(Id: str) -> Dict[str, Any]:
```

### Client().get_streaming_distribution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L156)

```python
def get_streaming_distribution(Id: str) -> Dict[str, Any]:
```

### Client().get_streaming_distribution_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L160)

```python
def get_streaming_distribution_config(Id: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L164)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_cloud_front_origin_access_identities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L168)

```python
def list_cloud_front_origin_access_identities(
    Marker: str = None,
    MaxItems: str = None,
) -> Dict[str, Any]:
```

### Client().list_distributions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L174)

```python
def list_distributions(
    Marker: str = None,
    MaxItems: str = None,
) -> Dict[str, Any]:
```

### Client().list_distributions_by_web_acl_id

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L180)

```python
def list_distributions_by_web_acl_id(
    WebACLId: str,
    Marker: str = None,
    MaxItems: str = None,
) -> Dict[str, Any]:
```

### Client().list_field_level_encryption_configs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L186)

```python
def list_field_level_encryption_configs(
    Marker: str = None,
    MaxItems: str = None,
) -> Dict[str, Any]:
```

### Client().list_field_level_encryption_profiles

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L192)

```python
def list_field_level_encryption_profiles(
    Marker: str = None,
    MaxItems: str = None,
) -> Dict[str, Any]:
```

### Client().list_invalidations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L198)

```python
def list_invalidations(
    DistributionId: str,
    Marker: str = None,
    MaxItems: str = None,
) -> Dict[str, Any]:
```

### Client().list_public_keys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L204)

```python
def list_public_keys(
    Marker: str = None,
    MaxItems: str = None,
) -> Dict[str, Any]:
```

### Client().list_streaming_distributions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L210)

```python
def list_streaming_distributions(
    Marker: str = None,
    MaxItems: str = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L216)

```python
def list_tags_for_resource(Resource: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L220)

```python
def tag_resource(Resource: str, Tags: Dict[str, Any]) -> None:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L224)

```python
def untag_resource(Resource: str, TagKeys: Dict[str, Any]) -> None:
```

### Client().update_cloud_front_origin_access_identity

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L228)

```python
def update_cloud_front_origin_access_identity(
    CloudFrontOriginAccessIdentityConfig: Dict[str, Any],
    Id: str,
    IfMatch: str = None,
) -> Dict[str, Any]:
```

### Client().update_distribution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L237)

```python
def update_distribution(
    DistributionConfig: Dict[str, Any],
    Id: str,
    IfMatch: str = None,
) -> Dict[str, Any]:
```

### Client().update_field_level_encryption_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L243)

```python
def update_field_level_encryption_config(
    FieldLevelEncryptionConfig: Dict[str, Any],
    Id: str,
    IfMatch: str = None,
) -> Dict[str, Any]:
```

### Client().update_field_level_encryption_profile

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L249)

```python
def update_field_level_encryption_profile(
    FieldLevelEncryptionProfileConfig: Dict[str, Any],
    Id: str,
    IfMatch: str = None,
) -> Dict[str, Any]:
```

### Client().update_public_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L258)

```python
def update_public_key(
    PublicKeyConfig: Dict[str, Any],
    Id: str,
    IfMatch: str = None,
) -> Dict[str, Any]:
```

### Client().update_streaming_distribution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudfront/client.py#L264)

```python
def update_streaming_distribution(
    StreamingDistributionConfig: Dict[str, Any],
    Id: str,
    IfMatch: str = None,
) -> Dict[str, Any]:
```

# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.ecr.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Ecr](index.md#ecr) / Client
    - [Client](#client)
        - [Client().batch_check_layer_availability](#clientbatch_check_layer_availability)
        - [Client().batch_delete_image](#clientbatch_delete_image)
        - [Client().batch_get_image](#clientbatch_get_image)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().complete_layer_upload](#clientcomplete_layer_upload)
        - [Client().create_repository](#clientcreate_repository)
        - [Client().delete_lifecycle_policy](#clientdelete_lifecycle_policy)
        - [Client().delete_repository](#clientdelete_repository)
        - [Client().delete_repository_policy](#clientdelete_repository_policy)
        - [Client().describe_image_scan_findings](#clientdescribe_image_scan_findings)
        - [Client().describe_images](#clientdescribe_images)
        - [Client().describe_repositories](#clientdescribe_repositories)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_authorization_token](#clientget_authorization_token)
        - [Client().get_download_url_for_layer](#clientget_download_url_for_layer)
        - [Client().get_lifecycle_policy](#clientget_lifecycle_policy)
        - [Client().get_lifecycle_policy_preview](#clientget_lifecycle_policy_preview)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_repository_policy](#clientget_repository_policy)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().initiate_layer_upload](#clientinitiate_layer_upload)
        - [Client().list_images](#clientlist_images)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().put_image](#clientput_image)
        - [Client().put_image_scanning_configuration](#clientput_image_scanning_configuration)
        - [Client().put_image_tag_mutability](#clientput_image_tag_mutability)
        - [Client().put_lifecycle_policy](#clientput_lifecycle_policy)
        - [Client().set_repository_policy](#clientset_repository_policy)
        - [Client().start_image_scan](#clientstart_image_scan)
        - [Client().start_lifecycle_policy_preview](#clientstart_lifecycle_policy_preview)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().upload_layer_part](#clientupload_layer_part)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L12)

```python
class Client(BaseClient):
```

### Client().batch_check_layer_availability

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L15)

```python
def batch_check_layer_availability(
    repositoryName: str,
    layerDigests: List[Any],
    registryId: str = None,
) -> Dict[str, Any]:
```

### Client().batch_delete_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L21)

```python
def batch_delete_image(
    repositoryName: str,
    imageIds: List[Any],
    registryId: str = None,
) -> Dict[str, Any]:
```

### Client().batch_get_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L27)

```python
def batch_get_image(
    repositoryName: str,
    imageIds: List[Any],
    registryId: str = None,
    acceptedMediaTypes: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L37)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().complete_layer_upload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L41)

```python
def complete_layer_upload(
    repositoryName: str,
    uploadId: str,
    layerDigests: List[Any],
    registryId: str = None,
) -> Dict[str, Any]:
```

### Client().create_repository

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L51)

```python
def create_repository(
    repositoryName: str,
    tags: List[Any] = None,
    imageTagMutability: str = None,
    imageScanningConfiguration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_lifecycle_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L61)

```python
def delete_lifecycle_policy(
    repositoryName: str,
    registryId: str = None,
) -> Dict[str, Any]:
```

### Client().delete_repository

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L67)

```python
def delete_repository(
    repositoryName: str,
    registryId: str = None,
    force: bool = None,
) -> Dict[str, Any]:
```

### Client().delete_repository_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L73)

```python
def delete_repository_policy(
    repositoryName: str,
    registryId: str = None,
) -> Dict[str, Any]:
```

### Client().describe_image_scan_findings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L79)

```python
def describe_image_scan_findings(
    repositoryName: str,
    imageId: Dict[str, Any],
    registryId: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().describe_images

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L90)

```python
def describe_images(
    repositoryName: str,
    registryId: str = None,
    imageIds: List[Any] = None,
    nextToken: str = None,
    maxResults: int = None,
    filter: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().describe_repositories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L102)

```python
def describe_repositories(
    registryId: str = None,
    repositoryNames: List[Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L112)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_authorization_token

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L122)

```python
def get_authorization_token(registryIds: List[Any] = None) -> Dict[str, Any]:
```

### Client().get_download_url_for_layer

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L126)

```python
def get_download_url_for_layer(
    repositoryName: str,
    layerDigest: str,
    registryId: str = None,
) -> Dict[str, Any]:
```

### Client().get_lifecycle_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L132)

```python
def get_lifecycle_policy(
    repositoryName: str,
    registryId: str = None,
) -> Dict[str, Any]:
```

### Client().get_lifecycle_policy_preview

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L138)

```python
def get_lifecycle_policy_preview(
    repositoryName: str,
    registryId: str = None,
    imageIds: List[Any] = None,
    nextToken: str = None,
    maxResults: int = None,
    filter: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L150)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_repository_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L154)

```python
def get_repository_policy(
    repositoryName: str,
    registryId: str = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L160)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().initiate_layer_upload

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L164)

```python
def initiate_layer_upload(
    repositoryName: str,
    registryId: str = None,
) -> Dict[str, Any]:
```

### Client().list_images

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L170)

```python
def list_images(
    repositoryName: str,
    registryId: str = None,
    nextToken: str = None,
    maxResults: int = None,
    filter: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L181)

```python
def list_tags_for_resource(resourceArn: str) -> Dict[str, Any]:
```

### Client().put_image

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L185)

```python
def put_image(
    repositoryName: str,
    imageManifest: str,
    registryId: str = None,
    imageTag: str = None,
) -> Dict[str, Any]:
```

### Client().put_image_scanning_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L195)

```python
def put_image_scanning_configuration(
    repositoryName: str,
    imageScanningConfiguration: Dict[str, Any],
    registryId: str = None,
) -> Dict[str, Any]:
```

### Client().put_image_tag_mutability

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L204)

```python
def put_image_tag_mutability(
    repositoryName: str,
    imageTagMutability: str,
    registryId: str = None,
) -> Dict[str, Any]:
```

### Client().put_lifecycle_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L210)

```python
def put_lifecycle_policy(
    repositoryName: str,
    lifecyclePolicyText: str,
    registryId: str = None,
) -> Dict[str, Any]:
```

### Client().set_repository_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L216)

```python
def set_repository_policy(
    repositoryName: str,
    policyText: str,
    registryId: str = None,
    force: bool = None,
) -> Dict[str, Any]:
```

### Client().start_image_scan

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L226)

```python
def start_image_scan(
    repositoryName: str,
    imageId: Dict[str, Any],
    registryId: str = None,
) -> Dict[str, Any]:
```

### Client().start_lifecycle_policy_preview

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L232)

```python
def start_lifecycle_policy_preview(
    repositoryName: str,
    registryId: str = None,
    lifecyclePolicyText: str = None,
) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L241)

```python
def tag_resource(resourceArn: str, tags: List[Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L245)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().upload_layer_part

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/ecr/client.py#L249)

```python
def upload_layer_part(
    repositoryName: str,
    uploadId: str,
    partFirstByte: int,
    partLastByte: int,
    layerPartBlob: bytes,
    registryId: str = None,
) -> Dict[str, Any]:
```

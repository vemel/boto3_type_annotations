# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.codebuild.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Codebuild](index.md#codebuild) / Client
    - [Client](#client)
        - [Client().batch_delete_builds](#clientbatch_delete_builds)
        - [Client().batch_get_builds](#clientbatch_get_builds)
        - [Client().batch_get_projects](#clientbatch_get_projects)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_project](#clientcreate_project)
        - [Client().create_webhook](#clientcreate_webhook)
        - [Client().delete_project](#clientdelete_project)
        - [Client().delete_source_credentials](#clientdelete_source_credentials)
        - [Client().delete_webhook](#clientdelete_webhook)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().import_source_credentials](#clientimport_source_credentials)
        - [Client().invalidate_project_cache](#clientinvalidate_project_cache)
        - [Client().list_builds](#clientlist_builds)
        - [Client().list_builds_for_project](#clientlist_builds_for_project)
        - [Client().list_curated_environment_images](#clientlist_curated_environment_images)
        - [Client().list_projects](#clientlist_projects)
        - [Client().list_source_credentials](#clientlist_source_credentials)
        - [Client().start_build](#clientstart_build)
        - [Client().stop_build](#clientstop_build)
        - [Client().update_project](#clientupdate_project)
        - [Client().update_webhook](#clientupdate_webhook)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L12)

```python
class Client(BaseClient):
```

### Client().batch_delete_builds

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L15)

```python
def batch_delete_builds(ids: List[Any]) -> Dict[str, Any]:
```

### Client().batch_get_builds

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L19)

```python
def batch_get_builds(ids: List[Any]) -> Dict[str, Any]:
```

### Client().batch_get_projects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L23)

```python
def batch_get_projects(names: List[Any]) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L27)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L31)

```python
def create_project(
    name: str,
    source: Dict[str, Any],
    artifacts: Dict[str, Any],
    environment: Dict[str, Any],
    serviceRole: str,
    description: str = None,
    secondarySources: List[Any] = None,
    sourceVersion: str = None,
    secondarySourceVersions: List[Any] = None,
    secondaryArtifacts: List[Any] = None,
    cache: Dict[str, Any] = None,
    timeoutInMinutes: int = None,
    queuedTimeoutInMinutes: int = None,
    encryptionKey: str = None,
    tags: List[Any] = None,
    vpcConfig: Dict[str, Any] = None,
    badgeEnabled: bool = None,
    logsConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_webhook

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L55)

```python
def create_webhook(
    projectName: str,
    branchFilter: str = None,
    filterGroups: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L61)

```python
def delete_project(name: str) -> Dict[str, Any]:
```

### Client().delete_source_credentials

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L65)

```python
def delete_source_credentials(arn: str) -> Dict[str, Any]:
```

### Client().delete_webhook

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L69)

```python
def delete_webhook(projectName: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L73)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L83)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L87)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().import_source_credentials

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L91)

```python
def import_source_credentials(
    token: str,
    serverType: str,
    authType: str,
    username: str = None,
    shouldOverwrite: bool = None,
) -> Dict[str, Any]:
```

### Client().invalidate_project_cache

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L102)

```python
def invalidate_project_cache(projectName: str) -> Dict[str, Any]:
```

### Client().list_builds

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L106)

```python
def list_builds(
    sortOrder: str = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_builds_for_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L112)

```python
def list_builds_for_project(
    projectName: str,
    sortOrder: str = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_curated_environment_images

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L118)

```python
def list_curated_environment_images() -> Dict[str, Any]:
```

### Client().list_projects

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L122)

```python
def list_projects(
    sortBy: str = None,
    sortOrder: str = None,
    nextToken: str = None,
) -> Dict[str, Any]:
```

### Client().list_source_credentials

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L128)

```python
def list_source_credentials() -> Dict[str, Any]:
```

### Client().start_build

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L132)

```python
def start_build(
    projectName: str,
    secondarySourcesOverride: List[Any] = None,
    secondarySourcesVersionOverride: List[Any] = None,
    sourceVersion: str = None,
    artifactsOverride: Dict[str, Any] = None,
    secondaryArtifactsOverride: List[Any] = None,
    environmentVariablesOverride: List[Any] = None,
    sourceTypeOverride: str = None,
    sourceLocationOverride: str = None,
    sourceAuthOverride: Dict[str, Any] = None,
    gitCloneDepthOverride: int = None,
    gitSubmodulesConfigOverride: Dict[str, Any] = None,
    buildspecOverride: str = None,
    insecureSslOverride: bool = None,
    reportBuildStatusOverride: bool = None,
    environmentTypeOverride: str = None,
    imageOverride: str = None,
    computeTypeOverride: str = None,
    certificateOverride: str = None,
    cacheOverride: Dict[str, Any] = None,
    serviceRoleOverride: str = None,
    privilegedModeOverride: bool = None,
    timeoutInMinutesOverride: int = None,
    queuedTimeoutInMinutesOverride: int = None,
    idempotencyToken: str = None,
    logsConfigOverride: Dict[str, Any] = None,
    registryCredentialOverride: Dict[str, Any] = None,
    imagePullCredentialsTypeOverride: str = None,
) -> Dict[str, Any]:
```

### Client().stop_build

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L166)

```python
def stop_build(id: str) -> Dict[str, Any]:
```

### Client().update_project

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L170)

```python
def update_project(
    name: str,
    description: str = None,
    source: Dict[str, Any] = None,
    secondarySources: List[Any] = None,
    sourceVersion: str = None,
    secondarySourceVersions: List[Any] = None,
    artifacts: Dict[str, Any] = None,
    secondaryArtifacts: List[Any] = None,
    cache: Dict[str, Any] = None,
    environment: Dict[str, Any] = None,
    serviceRole: str = None,
    timeoutInMinutes: int = None,
    queuedTimeoutInMinutes: int = None,
    encryptionKey: str = None,
    tags: List[Any] = None,
    vpcConfig: Dict[str, Any] = None,
    badgeEnabled: bool = None,
    logsConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_webhook

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/codebuild/client.py#L194)

```python
def update_webhook(
    projectName: str,
    branchFilter: str = None,
    rotateSecret: bool = None,
    filterGroups: List[Any] = None,
) -> Dict[str, Any]:
```

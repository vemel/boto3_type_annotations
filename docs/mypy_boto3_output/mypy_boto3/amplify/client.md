# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.amplify.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Amplify](index.md#amplify) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_app](#clientcreate_app)
        - [Client().create_branch](#clientcreate_branch)
        - [Client().create_deployment](#clientcreate_deployment)
        - [Client().create_domain_association](#clientcreate_domain_association)
        - [Client().create_webhook](#clientcreate_webhook)
        - [Client().delete_app](#clientdelete_app)
        - [Client().delete_branch](#clientdelete_branch)
        - [Client().delete_domain_association](#clientdelete_domain_association)
        - [Client().delete_job](#clientdelete_job)
        - [Client().delete_webhook](#clientdelete_webhook)
        - [Client().generate_access_logs](#clientgenerate_access_logs)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_app](#clientget_app)
        - [Client().get_artifact_url](#clientget_artifact_url)
        - [Client().get_branch](#clientget_branch)
        - [Client().get_domain_association](#clientget_domain_association)
        - [Client().get_job](#clientget_job)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().get_webhook](#clientget_webhook)
        - [Client().list_apps](#clientlist_apps)
        - [Client().list_artifacts](#clientlist_artifacts)
        - [Client().list_branches](#clientlist_branches)
        - [Client().list_domain_associations](#clientlist_domain_associations)
        - [Client().list_jobs](#clientlist_jobs)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_webhooks](#clientlist_webhooks)
        - [Client().start_deployment](#clientstart_deployment)
        - [Client().start_job](#clientstart_job)
        - [Client().stop_job](#clientstop_job)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_app](#clientupdate_app)
        - [Client().update_branch](#clientupdate_branch)
        - [Client().update_domain_association](#clientupdate_domain_association)
        - [Client().update_webhook](#clientupdate_webhook)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L13)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L16)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_app

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L20)

```python
def create_app(
    name: str,
    description: str = None,
    repository: str = None,
    platform: str = None,
    iamServiceRoleArn: str = None,
    oauthToken: str = None,
    accessToken: str = None,
    environmentVariables: Dict[str, Any] = None,
    enableBranchAutoBuild: bool = None,
    enableBasicAuth: bool = None,
    basicAuthCredentials: str = None,
    customRules: List[Any] = None,
    tags: Dict[str, Any] = None,
    buildSpec: str = None,
    enableAutoBranchCreation: bool = None,
    autoBranchCreationPatterns: List[Any] = None,
    autoBranchCreationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_branch

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L43)

```python
def create_branch(
    appId: str,
    branchName: str,
    description: str = None,
    stage: str = None,
    framework: str = None,
    enableNotification: bool = None,
    enableAutoBuild: bool = None,
    environmentVariables: Dict[str, Any] = None,
    basicAuthCredentials: str = None,
    enableBasicAuth: bool = None,
    tags: Dict[str, Any] = None,
    buildSpec: str = None,
    ttl: str = None,
    displayName: str = None,
    enablePullRequestPreview: bool = None,
    pullRequestEnvironmentName: str = None,
    backendEnvironmentArn: str = None,
) -> Dict[str, Any]:
```

### Client().create_deployment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L66)

```python
def create_deployment(
    appId: str,
    branchName: str,
    fileMap: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_domain_association

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L72)

```python
def create_domain_association(
    appId: str,
    domainName: str,
    subDomainSettings: List[Any],
    enableAutoSubDomain: bool = None,
) -> Dict[str, Any]:
```

### Client().create_webhook

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L82)

```python
def create_webhook(
    appId: str,
    branchName: str,
    description: str = None,
) -> Dict[str, Any]:
```

### Client().delete_app

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L88)

```python
def delete_app(appId: str) -> Dict[str, Any]:
```

### Client().delete_branch

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L92)

```python
def delete_branch(appId: str, branchName: str) -> Dict[str, Any]:
```

### Client().delete_domain_association

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L96)

```python
def delete_domain_association(appId: str, domainName: str) -> Dict[str, Any]:
```

### Client().delete_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L100)

```python
def delete_job(appId: str, branchName: str, jobId: str) -> Dict[str, Any]:
```

### Client().delete_webhook

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L104)

```python
def delete_webhook(webhookId: str) -> Dict[str, Any]:
```

### Client().generate_access_logs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L108)

```python
def generate_access_logs(
    domainName: str,
    appId: str,
    startTime: datetime = None,
    endTime: datetime = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L118)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_app

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L128)

```python
def get_app(appId: str) -> Dict[str, Any]:
```

### Client().get_artifact_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L132)

```python
def get_artifact_url(artifactId: str) -> Dict[str, Any]:
```

### Client().get_branch

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L136)

```python
def get_branch(appId: str, branchName: str) -> Dict[str, Any]:
```

### Client().get_domain_association

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L140)

```python
def get_domain_association(appId: str, domainName: str) -> Dict[str, Any]:
```

### Client().get_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L144)

```python
def get_job(appId: str, branchName: str, jobId: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L148)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L152)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().get_webhook

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L156)

```python
def get_webhook(webhookId: str) -> Dict[str, Any]:
```

### Client().list_apps

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L160)

```python
def list_apps(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_artifacts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L166)

```python
def list_artifacts(
    appId: str,
    branchName: str,
    jobId: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_branches

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L177)

```python
def list_branches(
    appId: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_domain_associations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L183)

```python
def list_domain_associations(
    appId: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L189)

```python
def list_jobs(
    appId: str,
    branchName: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L195)

```python
def list_tags_for_resource(resourceArn: str) -> Dict[str, Any]:
```

### Client().list_webhooks

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L199)

```python
def list_webhooks(
    appId: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().start_deployment

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L205)

```python
def start_deployment(
    appId: str,
    branchName: str,
    jobId: str = None,
    sourceUrl: str = None,
) -> Dict[str, Any]:
```

### Client().start_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L211)

```python
def start_job(
    appId: str,
    branchName: str,
    jobType: str,
    jobId: str = None,
    jobReason: str = None,
    commitId: str = None,
    commitMessage: str = None,
    commitTime: datetime = None,
) -> Dict[str, Any]:
```

### Client().stop_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L225)

```python
def stop_job(appId: str, branchName: str, jobId: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L229)

```python
def tag_resource(resourceArn: str, tags: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L233)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_app

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L237)

```python
def update_app(
    appId: str,
    name: str = None,
    description: str = None,
    platform: str = None,
    iamServiceRoleArn: str = None,
    environmentVariables: Dict[str, Any] = None,
    enableBranchAutoBuild: bool = None,
    enableBasicAuth: bool = None,
    basicAuthCredentials: str = None,
    customRules: List[Any] = None,
    buildSpec: str = None,
    enableAutoBranchCreation: bool = None,
    autoBranchCreationPatterns: List[Any] = None,
    autoBranchCreationConfig: Dict[str, Any] = None,
    repository: str = None,
    oauthToken: str = None,
    accessToken: str = None,
) -> Dict[str, Any]:
```

### Client().update_branch

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L260)

```python
def update_branch(
    appId: str,
    branchName: str,
    description: str = None,
    framework: str = None,
    stage: str = None,
    enableNotification: bool = None,
    enableAutoBuild: bool = None,
    environmentVariables: Dict[str, Any] = None,
    basicAuthCredentials: str = None,
    enableBasicAuth: bool = None,
    buildSpec: str = None,
    ttl: str = None,
    displayName: str = None,
    enablePullRequestPreview: bool = None,
    pullRequestEnvironmentName: str = None,
    backendEnvironmentArn: str = None,
) -> Dict[str, Any]:
```

### Client().update_domain_association

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L282)

```python
def update_domain_association(
    appId: str,
    domainName: str,
    subDomainSettings: List[Any],
    enableAutoSubDomain: bool = None,
) -> Dict[str, Any]:
```

### Client().update_webhook

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/amplify/client.py#L292)

```python
def update_webhook(
    webhookId: str,
    branchName: str = None,
    description: str = None,
) -> Dict[str, Any]:
```

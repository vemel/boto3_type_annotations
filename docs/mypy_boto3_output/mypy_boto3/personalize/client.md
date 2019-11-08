# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.personalize.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Personalize](index.md#personalize) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_campaign](#clientcreate_campaign)
        - [Client().create_dataset](#clientcreate_dataset)
        - [Client().create_dataset_group](#clientcreate_dataset_group)
        - [Client().create_dataset_import_job](#clientcreate_dataset_import_job)
        - [Client().create_event_tracker](#clientcreate_event_tracker)
        - [Client().create_schema](#clientcreate_schema)
        - [Client().create_solution](#clientcreate_solution)
        - [Client().create_solution_version](#clientcreate_solution_version)
        - [Client().delete_campaign](#clientdelete_campaign)
        - [Client().delete_dataset](#clientdelete_dataset)
        - [Client().delete_dataset_group](#clientdelete_dataset_group)
        - [Client().delete_event_tracker](#clientdelete_event_tracker)
        - [Client().delete_schema](#clientdelete_schema)
        - [Client().delete_solution](#clientdelete_solution)
        - [Client().describe_algorithm](#clientdescribe_algorithm)
        - [Client().describe_campaign](#clientdescribe_campaign)
        - [Client().describe_dataset](#clientdescribe_dataset)
        - [Client().describe_dataset_group](#clientdescribe_dataset_group)
        - [Client().describe_dataset_import_job](#clientdescribe_dataset_import_job)
        - [Client().describe_event_tracker](#clientdescribe_event_tracker)
        - [Client().describe_feature_transformation](#clientdescribe_feature_transformation)
        - [Client().describe_recipe](#clientdescribe_recipe)
        - [Client().describe_schema](#clientdescribe_schema)
        - [Client().describe_solution](#clientdescribe_solution)
        - [Client().describe_solution_version](#clientdescribe_solution_version)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_solution_metrics](#clientget_solution_metrics)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_campaigns](#clientlist_campaigns)
        - [Client().list_dataset_groups](#clientlist_dataset_groups)
        - [Client().list_dataset_import_jobs](#clientlist_dataset_import_jobs)
        - [Client().list_datasets](#clientlist_datasets)
        - [Client().list_event_trackers](#clientlist_event_trackers)
        - [Client().list_recipes](#clientlist_recipes)
        - [Client().list_schemas](#clientlist_schemas)
        - [Client().list_solution_versions](#clientlist_solution_versions)
        - [Client().list_solutions](#clientlist_solutions)
        - [Client().update_campaign](#clientupdate_campaign)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L11)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L14)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_campaign

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L18)

```python
def create_campaign(
    name: str,
    solutionVersionArn: str,
    minProvisionedTPS: int,
) -> Dict[str, Any]:
```

### Client().create_dataset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L24)

```python
def create_dataset(
    name: str,
    schemaArn: str,
    datasetGroupArn: str,
    datasetType: str,
) -> Dict[str, Any]:
```

### Client().create_dataset_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L30)

```python
def create_dataset_group(
    name: str,
    roleArn: str = None,
    kmsKeyArn: str = None,
) -> Dict[str, Any]:
```

### Client().create_dataset_import_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L36)

```python
def create_dataset_import_job(
    jobName: str,
    datasetArn: str,
    dataSource: Dict[str, Any],
    roleArn: str,
) -> Dict[str, Any]:
```

### Client().create_event_tracker

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L42)

```python
def create_event_tracker(name: str, datasetGroupArn: str) -> Dict[str, Any]:
```

### Client().create_schema

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L46)

```python
def create_schema(name: str, schema: str) -> Dict[str, Any]:
```

### Client().create_solution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L50)

```python
def create_solution(
    name: str,
    datasetGroupArn: str,
    performHPO: bool = None,
    performAutoML: bool = None,
    recipeArn: str = None,
    eventType: str = None,
    solutionConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_solution_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L63)

```python
def create_solution_version(
    solutionArn: str,
    trainingMode: str = None,
) -> Dict[str, Any]:
```

### Client().delete_campaign

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L69)

```python
def delete_campaign(campaignArn: str) -> None:
```

### Client().delete_dataset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L73)

```python
def delete_dataset(datasetArn: str) -> None:
```

### Client().delete_dataset_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L77)

```python
def delete_dataset_group(datasetGroupArn: str) -> None:
```

### Client().delete_event_tracker

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L81)

```python
def delete_event_tracker(eventTrackerArn: str) -> None:
```

### Client().delete_schema

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L85)

```python
def delete_schema(schemaArn: str) -> None:
```

### Client().delete_solution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L89)

```python
def delete_solution(solutionArn: str) -> None:
```

### Client().describe_algorithm

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L93)

```python
def describe_algorithm(algorithmArn: str) -> Dict[str, Any]:
```

### Client().describe_campaign

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L97)

```python
def describe_campaign(campaignArn: str) -> Dict[str, Any]:
```

### Client().describe_dataset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L101)

```python
def describe_dataset(datasetArn: str) -> Dict[str, Any]:
```

### Client().describe_dataset_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L105)

```python
def describe_dataset_group(datasetGroupArn: str) -> Dict[str, Any]:
```

### Client().describe_dataset_import_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L109)

```python
def describe_dataset_import_job(datasetImportJobArn: str) -> Dict[str, Any]:
```

### Client().describe_event_tracker

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L113)

```python
def describe_event_tracker(eventTrackerArn: str) -> Dict[str, Any]:
```

### Client().describe_feature_transformation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L117)

```python
def describe_feature_transformation(
    featureTransformationArn: str,
) -> Dict[str, Any]:
```

### Client().describe_recipe

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L123)

```python
def describe_recipe(recipeArn: str) -> Dict[str, Any]:
```

### Client().describe_schema

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L127)

```python
def describe_schema(schemaArn: str) -> Dict[str, Any]:
```

### Client().describe_solution

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L131)

```python
def describe_solution(solutionArn: str) -> Dict[str, Any]:
```

### Client().describe_solution_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L135)

```python
def describe_solution_version(solutionVersionArn: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L139)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L149)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_solution_metrics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L153)

```python
def get_solution_metrics(solutionVersionArn: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L157)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_campaigns

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L161)

```python
def list_campaigns(
    solutionArn: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_dataset_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L167)

```python
def list_dataset_groups(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_dataset_import_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L173)

```python
def list_dataset_import_jobs(
    datasetArn: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_datasets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L179)

```python
def list_datasets(
    datasetGroupArn: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_event_trackers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L185)

```python
def list_event_trackers(
    datasetGroupArn: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_recipes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L191)

```python
def list_recipes(
    recipeProvider: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_schemas

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L197)

```python
def list_schemas(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_solution_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L203)

```python
def list_solution_versions(
    solutionArn: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_solutions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L209)

```python
def list_solutions(
    datasetGroupArn: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().update_campaign

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/client.py#L215)

```python
def update_campaign(
    campaignArn: str,
    solutionVersionArn: str = None,
    minProvisionedTPS: int = None,
) -> Dict[str, Any]:
```

# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.machinelearning.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Machinelearning](index.md#machinelearning) / Client
    - [Client](#client)
        - [Client().add_tags](#clientadd_tags)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_batch_prediction](#clientcreate_batch_prediction)
        - [Client().create_data_source_from_rds](#clientcreate_data_source_from_rds)
        - [Client().create_data_source_from_redshift](#clientcreate_data_source_from_redshift)
        - [Client().create_data_source_from_s3](#clientcreate_data_source_from_s3)
        - [Client().create_evaluation](#clientcreate_evaluation)
        - [Client().create_ml_model](#clientcreate_ml_model)
        - [Client().create_realtime_endpoint](#clientcreate_realtime_endpoint)
        - [Client().delete_batch_prediction](#clientdelete_batch_prediction)
        - [Client().delete_data_source](#clientdelete_data_source)
        - [Client().delete_evaluation](#clientdelete_evaluation)
        - [Client().delete_ml_model](#clientdelete_ml_model)
        - [Client().delete_realtime_endpoint](#clientdelete_realtime_endpoint)
        - [Client().delete_tags](#clientdelete_tags)
        - [Client().describe_batch_predictions](#clientdescribe_batch_predictions)
        - [Client().describe_data_sources](#clientdescribe_data_sources)
        - [Client().describe_evaluations](#clientdescribe_evaluations)
        - [Client().describe_ml_models](#clientdescribe_ml_models)
        - [Client().describe_tags](#clientdescribe_tags)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_batch_prediction](#clientget_batch_prediction)
        - [Client().get_data_source](#clientget_data_source)
        - [Client().get_evaluation](#clientget_evaluation)
        - [Client().get_ml_model](#clientget_ml_model)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().predict](#clientpredict)
        - [Client().update_batch_prediction](#clientupdate_batch_prediction)
        - [Client().update_data_source](#clientupdate_data_source)
        - [Client().update_evaluation](#clientupdate_evaluation)
        - [Client().update_ml_model](#clientupdate_ml_model)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L12)

```python
class Client(BaseClient):
```

### Client().add_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L15)

```python
def add_tags(
    Tags: List[Any],
    ResourceId: str,
    ResourceType: str,
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L21)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_batch_prediction

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L25)

```python
def create_batch_prediction(
    BatchPredictionId: str,
    MLModelId: str,
    BatchPredictionDataSourceId: str,
    OutputUri: str,
    BatchPredictionName: str = None,
) -> Dict[str, Any]:
```

### Client().create_data_source_from_rds

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L36)

```python
def create_data_source_from_rds(
    DataSourceId: str,
    RDSData: Dict[str, Any],
    RoleARN: str,
    DataSourceName: str = None,
    ComputeStatistics: bool = None,
) -> Dict[str, Any]:
```

### Client().create_data_source_from_redshift

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L47)

```python
def create_data_source_from_redshift(
    DataSourceId: str,
    DataSpec: Dict[str, Any],
    RoleARN: str,
    DataSourceName: str = None,
    ComputeStatistics: bool = None,
) -> Dict[str, Any]:
```

### Client().create_data_source_from_s3

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L58)

```python
def create_data_source_from_s3(
    DataSourceId: str,
    DataSpec: Dict[str, Any],
    DataSourceName: str = None,
    ComputeStatistics: bool = None,
) -> Dict[str, Any]:
```

### Client().create_evaluation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L68)

```python
def create_evaluation(
    EvaluationId: str,
    MLModelId: str,
    EvaluationDataSourceId: str,
    EvaluationName: str = None,
) -> Dict[str, Any]:
```

### Client().create_ml_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L78)

```python
def create_ml_model(
    MLModelId: str,
    MLModelType: str,
    TrainingDataSourceId: str,
    MLModelName: str = None,
    Parameters: Dict[str, Any] = None,
    Recipe: str = None,
    RecipeUri: str = None,
) -> Dict[str, Any]:
```

### Client().create_realtime_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L91)

```python
def create_realtime_endpoint(MLModelId: str) -> Dict[str, Any]:
```

### Client().delete_batch_prediction

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L95)

```python
def delete_batch_prediction(BatchPredictionId: str) -> Dict[str, Any]:
```

### Client().delete_data_source

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L99)

```python
def delete_data_source(DataSourceId: str) -> Dict[str, Any]:
```

### Client().delete_evaluation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L103)

```python
def delete_evaluation(EvaluationId: str) -> Dict[str, Any]:
```

### Client().delete_ml_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L107)

```python
def delete_ml_model(MLModelId: str) -> Dict[str, Any]:
```

### Client().delete_realtime_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L111)

```python
def delete_realtime_endpoint(MLModelId: str) -> Dict[str, Any]:
```

### Client().delete_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L115)

```python
def delete_tags(
    TagKeys: List[Any],
    ResourceId: str,
    ResourceType: str,
) -> Dict[str, Any]:
```

### Client().describe_batch_predictions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L121)

```python
def describe_batch_predictions(
    FilterVariable: str = None,
    EQ: str = None,
    GT: str = None,
    LT: str = None,
    GE: str = None,
    LE: str = None,
    NE: str = None,
    Prefix: str = None,
    SortOrder: str = None,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_data_sources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L138)

```python
def describe_data_sources(
    FilterVariable: str = None,
    EQ: str = None,
    GT: str = None,
    LT: str = None,
    GE: str = None,
    LE: str = None,
    NE: str = None,
    Prefix: str = None,
    SortOrder: str = None,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_evaluations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L155)

```python
def describe_evaluations(
    FilterVariable: str = None,
    EQ: str = None,
    GT: str = None,
    LT: str = None,
    GE: str = None,
    LE: str = None,
    NE: str = None,
    Prefix: str = None,
    SortOrder: str = None,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_ml_models

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L172)

```python
def describe_ml_models(
    FilterVariable: str = None,
    EQ: str = None,
    GT: str = None,
    LT: str = None,
    GE: str = None,
    LE: str = None,
    NE: str = None,
    Prefix: str = None,
    SortOrder: str = None,
    NextToken: str = None,
    Limit: int = None,
) -> Dict[str, Any]:
```

### Client().describe_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L189)

```python
def describe_tags(ResourceId: str, ResourceType: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L193)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_batch_prediction

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L203)

```python
def get_batch_prediction(BatchPredictionId: str) -> Dict[str, Any]:
```

### Client().get_data_source

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L207)

```python
def get_data_source(
    DataSourceId: str,
    Verbose: bool = None,
) -> Dict[str, Any]:
```

### Client().get_evaluation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L213)

```python
def get_evaluation(EvaluationId: str) -> Dict[str, Any]:
```

### Client().get_ml_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L217)

```python
def get_ml_model(MLModelId: str, Verbose: bool = None) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L221)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L225)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().predict

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L229)

```python
def predict(
    MLModelId: str,
    Record: Dict[str, Any],
    PredictEndpoint: str,
) -> Dict[str, Any]:
```

### Client().update_batch_prediction

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L235)

```python
def update_batch_prediction(
    BatchPredictionId: str,
    BatchPredictionName: str,
) -> Dict[str, Any]:
```

### Client().update_data_source

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L241)

```python
def update_data_source(
    DataSourceId: str,
    DataSourceName: str,
) -> Dict[str, Any]:
```

### Client().update_evaluation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L247)

```python
def update_evaluation(
    EvaluationId: str,
    EvaluationName: str,
) -> Dict[str, Any]:
```

### Client().update_ml_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/machinelearning/client.py#L253)

```python
def update_ml_model(
    MLModelId: str,
    MLModelName: str = None,
    ScoreThreshold: float = None,
) -> Dict[str, Any]:
```

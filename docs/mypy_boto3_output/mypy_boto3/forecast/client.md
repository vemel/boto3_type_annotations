# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.forecast.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Forecast](index.md#forecast) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_dataset](#clientcreate_dataset)
        - [Client().create_dataset_group](#clientcreate_dataset_group)
        - [Client().create_dataset_import_job](#clientcreate_dataset_import_job)
        - [Client().create_forecast](#clientcreate_forecast)
        - [Client().create_forecast_export_job](#clientcreate_forecast_export_job)
        - [Client().create_predictor](#clientcreate_predictor)
        - [Client().delete_dataset](#clientdelete_dataset)
        - [Client().delete_dataset_group](#clientdelete_dataset_group)
        - [Client().delete_dataset_import_job](#clientdelete_dataset_import_job)
        - [Client().delete_forecast](#clientdelete_forecast)
        - [Client().delete_forecast_export_job](#clientdelete_forecast_export_job)
        - [Client().delete_predictor](#clientdelete_predictor)
        - [Client().describe_dataset](#clientdescribe_dataset)
        - [Client().describe_dataset_group](#clientdescribe_dataset_group)
        - [Client().describe_dataset_import_job](#clientdescribe_dataset_import_job)
        - [Client().describe_forecast](#clientdescribe_forecast)
        - [Client().describe_forecast_export_job](#clientdescribe_forecast_export_job)
        - [Client().describe_predictor](#clientdescribe_predictor)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_accuracy_metrics](#clientget_accuracy_metrics)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_dataset_groups](#clientlist_dataset_groups)
        - [Client().list_dataset_import_jobs](#clientlist_dataset_import_jobs)
        - [Client().list_datasets](#clientlist_datasets)
        - [Client().list_forecast_export_jobs](#clientlist_forecast_export_jobs)
        - [Client().list_forecasts](#clientlist_forecasts)
        - [Client().list_predictors](#clientlist_predictors)
        - [Client().update_dataset_group](#clientupdate_dataset_group)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_dataset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L19)

```python
def create_dataset(
    DatasetName: str,
    Domain: str,
    DatasetType: str,
    Schema: Dict[str, Any],
    DataFrequency: str = None,
    EncryptionConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_dataset_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L31)

```python
def create_dataset_group(
    DatasetGroupName: str,
    Domain: str,
    DatasetArns: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_dataset_import_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L37)

```python
def create_dataset_import_job(
    DatasetImportJobName: str,
    DatasetArn: str,
    DataSource: Dict[str, Any],
    TimestampFormat: str = None,
) -> Dict[str, Any]:
```

### Client().create_forecast

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L47)

```python
def create_forecast(ForecastName: str, PredictorArn: str) -> Dict[str, Any]:
```

### Client().create_forecast_export_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L51)

```python
def create_forecast_export_job(
    ForecastExportJobName: str,
    ForecastArn: str,
    Destination: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_predictor

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L57)

```python
def create_predictor(
    PredictorName: str,
    ForecastHorizon: int,
    InputDataConfig: Dict[str, Any],
    FeaturizationConfig: Dict[str, Any],
    AlgorithmArn: str = None,
    PerformAutoML: bool = None,
    PerformHPO: bool = None,
    TrainingParameters: Dict[str, Any] = None,
    EvaluationParameters: Dict[str, Any] = None,
    HPOConfig: Dict[str, Any] = None,
    EncryptionConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_dataset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L74)

```python
def delete_dataset(DatasetArn: str) -> None:
```

### Client().delete_dataset_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L78)

```python
def delete_dataset_group(DatasetGroupArn: str) -> None:
```

### Client().delete_dataset_import_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L82)

```python
def delete_dataset_import_job(DatasetImportJobArn: str) -> None:
```

### Client().delete_forecast

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L86)

```python
def delete_forecast(ForecastArn: str) -> None:
```

### Client().delete_forecast_export_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L90)

```python
def delete_forecast_export_job(ForecastExportJobArn: str) -> None:
```

### Client().delete_predictor

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L94)

```python
def delete_predictor(PredictorArn: str) -> None:
```

### Client().describe_dataset

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L98)

```python
def describe_dataset(DatasetArn: str) -> Dict[str, Any]:
```

### Client().describe_dataset_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L102)

```python
def describe_dataset_group(DatasetGroupArn: str) -> Dict[str, Any]:
```

### Client().describe_dataset_import_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L106)

```python
def describe_dataset_import_job(DatasetImportJobArn: str) -> Dict[str, Any]:
```

### Client().describe_forecast

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L110)

```python
def describe_forecast(ForecastArn: str) -> Dict[str, Any]:
```

### Client().describe_forecast_export_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L114)

```python
def describe_forecast_export_job(ForecastExportJobArn: str) -> Dict[str, Any]:
```

### Client().describe_predictor

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L118)

```python
def describe_predictor(PredictorArn: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L122)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_accuracy_metrics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L132)

```python
def get_accuracy_metrics(PredictorArn: str) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L136)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L140)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_dataset_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L144)

```python
def list_dataset_groups(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_dataset_import_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L150)

```python
def list_dataset_import_jobs(
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_datasets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L156)

```python
def list_datasets(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_forecast_export_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L162)

```python
def list_forecast_export_jobs(
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_forecasts

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L168)

```python
def list_forecasts(
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().list_predictors

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L174)

```python
def list_predictors(
    NextToken: str = None,
    MaxResults: int = None,
    Filters: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_dataset_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/forecast/client.py#L180)

```python
def update_dataset_group(
    DatasetGroupArn: str,
    DatasetArns: List[Any],
) -> Dict[str, Any]:
```

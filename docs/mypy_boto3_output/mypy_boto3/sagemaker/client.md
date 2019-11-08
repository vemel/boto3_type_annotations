# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.sagemaker.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Sagemaker](index.md#sagemaker) / Client
    - [Client](#client)
        - [Client().add_tags](#clientadd_tags)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_algorithm](#clientcreate_algorithm)
        - [Client().create_code_repository](#clientcreate_code_repository)
        - [Client().create_compilation_job](#clientcreate_compilation_job)
        - [Client().create_endpoint](#clientcreate_endpoint)
        - [Client().create_endpoint_config](#clientcreate_endpoint_config)
        - [Client().create_hyper_parameter_tuning_job](#clientcreate_hyper_parameter_tuning_job)
        - [Client().create_labeling_job](#clientcreate_labeling_job)
        - [Client().create_model](#clientcreate_model)
        - [Client().create_model_package](#clientcreate_model_package)
        - [Client().create_notebook_instance](#clientcreate_notebook_instance)
        - [Client().create_notebook_instance_lifecycle_config](#clientcreate_notebook_instance_lifecycle_config)
        - [Client().create_presigned_notebook_instance_url](#clientcreate_presigned_notebook_instance_url)
        - [Client().create_training_job](#clientcreate_training_job)
        - [Client().create_transform_job](#clientcreate_transform_job)
        - [Client().create_workteam](#clientcreate_workteam)
        - [Client().delete_algorithm](#clientdelete_algorithm)
        - [Client().delete_code_repository](#clientdelete_code_repository)
        - [Client().delete_endpoint](#clientdelete_endpoint)
        - [Client().delete_endpoint_config](#clientdelete_endpoint_config)
        - [Client().delete_model](#clientdelete_model)
        - [Client().delete_model_package](#clientdelete_model_package)
        - [Client().delete_notebook_instance](#clientdelete_notebook_instance)
        - [Client().delete_notebook_instance_lifecycle_config](#clientdelete_notebook_instance_lifecycle_config)
        - [Client().delete_tags](#clientdelete_tags)
        - [Client().delete_workteam](#clientdelete_workteam)
        - [Client().describe_algorithm](#clientdescribe_algorithm)
        - [Client().describe_code_repository](#clientdescribe_code_repository)
        - [Client().describe_compilation_job](#clientdescribe_compilation_job)
        - [Client().describe_endpoint](#clientdescribe_endpoint)
        - [Client().describe_endpoint_config](#clientdescribe_endpoint_config)
        - [Client().describe_hyper_parameter_tuning_job](#clientdescribe_hyper_parameter_tuning_job)
        - [Client().describe_labeling_job](#clientdescribe_labeling_job)
        - [Client().describe_model](#clientdescribe_model)
        - [Client().describe_model_package](#clientdescribe_model_package)
        - [Client().describe_notebook_instance](#clientdescribe_notebook_instance)
        - [Client().describe_notebook_instance_lifecycle_config](#clientdescribe_notebook_instance_lifecycle_config)
        - [Client().describe_subscribed_workteam](#clientdescribe_subscribed_workteam)
        - [Client().describe_training_job](#clientdescribe_training_job)
        - [Client().describe_transform_job](#clientdescribe_transform_job)
        - [Client().describe_workteam](#clientdescribe_workteam)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_search_suggestions](#clientget_search_suggestions)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_algorithms](#clientlist_algorithms)
        - [Client().list_code_repositories](#clientlist_code_repositories)
        - [Client().list_compilation_jobs](#clientlist_compilation_jobs)
        - [Client().list_endpoint_configs](#clientlist_endpoint_configs)
        - [Client().list_endpoints](#clientlist_endpoints)
        - [Client().list_hyper_parameter_tuning_jobs](#clientlist_hyper_parameter_tuning_jobs)
        - [Client().list_labeling_jobs](#clientlist_labeling_jobs)
        - [Client().list_labeling_jobs_for_workteam](#clientlist_labeling_jobs_for_workteam)
        - [Client().list_model_packages](#clientlist_model_packages)
        - [Client().list_models](#clientlist_models)
        - [Client().list_notebook_instance_lifecycle_configs](#clientlist_notebook_instance_lifecycle_configs)
        - [Client().list_notebook_instances](#clientlist_notebook_instances)
        - [Client().list_subscribed_workteams](#clientlist_subscribed_workteams)
        - [Client().list_tags](#clientlist_tags)
        - [Client().list_training_jobs](#clientlist_training_jobs)
        - [Client().list_training_jobs_for_hyper_parameter_tuning_job](#clientlist_training_jobs_for_hyper_parameter_tuning_job)
        - [Client().list_transform_jobs](#clientlist_transform_jobs)
        - [Client().list_workteams](#clientlist_workteams)
        - [Client().render_ui_template](#clientrender_ui_template)
        - [Client().search](#clientsearch)
        - [Client().start_notebook_instance](#clientstart_notebook_instance)
        - [Client().stop_compilation_job](#clientstop_compilation_job)
        - [Client().stop_hyper_parameter_tuning_job](#clientstop_hyper_parameter_tuning_job)
        - [Client().stop_labeling_job](#clientstop_labeling_job)
        - [Client().stop_notebook_instance](#clientstop_notebook_instance)
        - [Client().stop_training_job](#clientstop_training_job)
        - [Client().stop_transform_job](#clientstop_transform_job)
        - [Client().update_code_repository](#clientupdate_code_repository)
        - [Client().update_endpoint](#clientupdate_endpoint)
        - [Client().update_endpoint_weights_and_capacities](#clientupdate_endpoint_weights_and_capacities)
        - [Client().update_notebook_instance](#clientupdate_notebook_instance)
        - [Client().update_notebook_instance_lifecycle_config](#clientupdate_notebook_instance_lifecycle_config)
        - [Client().update_workteam](#clientupdate_workteam)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L13)

```python
class Client(BaseClient):
```

### Client().add_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L16)

```python
def add_tags(ResourceArn: str, Tags: List[Any]) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L20)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_algorithm

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L24)

```python
def create_algorithm(
    AlgorithmName: str,
    TrainingSpecification: Dict[str, Any],
    AlgorithmDescription: str = None,
    InferenceSpecification: Dict[str, Any] = None,
    ValidationSpecification: Dict[str, Any] = None,
    CertifyForMarketplace: bool = None,
) -> Dict[str, Any]:
```

### Client().create_code_repository

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L36)

```python
def create_code_repository(
    CodeRepositoryName: str,
    GitConfig: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_compilation_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L42)

```python
def create_compilation_job(
    CompilationJobName: str,
    RoleArn: str,
    InputConfig: Dict[str, Any],
    OutputConfig: Dict[str, Any],
    StoppingCondition: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L53)

```python
def create_endpoint(
    EndpointName: str,
    EndpointConfigName: str,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_endpoint_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L59)

```python
def create_endpoint_config(
    EndpointConfigName: str,
    ProductionVariants: List[Any],
    Tags: List[Any] = None,
    KmsKeyId: str = None,
) -> Dict[str, Any]:
```

### Client().create_hyper_parameter_tuning_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L69)

```python
def create_hyper_parameter_tuning_job(
    HyperParameterTuningJobName: str,
    HyperParameterTuningJobConfig: Dict[str, Any],
    TrainingJobDefinition: Dict[str, Any] = None,
    WarmStartConfig: Dict[str, Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_labeling_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L80)

```python
def create_labeling_job(
    LabelingJobName: str,
    LabelAttributeName: str,
    InputConfig: Dict[str, Any],
    OutputConfig: Dict[str, Any],
    RoleArn: str,
    HumanTaskConfig: Dict[str, Any],
    LabelCategoryConfigS3Uri: str = None,
    StoppingConditions: Dict[str, Any] = None,
    LabelingJobAlgorithmsConfig: Dict[str, Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L96)

```python
def create_model(
    ModelName: str,
    ExecutionRoleArn: str,
    PrimaryContainer: Dict[str, Any] = None,
    Containers: List[Any] = None,
    Tags: List[Any] = None,
    VpcConfig: Dict[str, Any] = None,
    EnableNetworkIsolation: bool = None,
) -> Dict[str, Any]:
```

### Client().create_model_package

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L109)

```python
def create_model_package(
    ModelPackageName: str,
    ModelPackageDescription: str = None,
    InferenceSpecification: Dict[str, Any] = None,
    ValidationSpecification: Dict[str, Any] = None,
    SourceAlgorithmSpecification: Dict[str, Any] = None,
    CertifyForMarketplace: bool = None,
) -> Dict[str, Any]:
```

### Client().create_notebook_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L121)

```python
def create_notebook_instance(
    NotebookInstanceName: str,
    InstanceType: str,
    RoleArn: str,
    SubnetId: str = None,
    SecurityGroupIds: List[Any] = None,
    KmsKeyId: str = None,
    Tags: List[Any] = None,
    LifecycleConfigName: str = None,
    DirectInternetAccess: str = None,
    VolumeSizeInGB: int = None,
    AcceleratorTypes: List[Any] = None,
    DefaultCodeRepository: str = None,
    AdditionalCodeRepositories: List[Any] = None,
    RootAccess: str = None,
) -> Dict[str, Any]:
```

### Client().create_notebook_instance_lifecycle_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L141)

```python
def create_notebook_instance_lifecycle_config(
    NotebookInstanceLifecycleConfigName: str,
    OnCreate: List[Any] = None,
    OnStart: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_presigned_notebook_instance_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L150)

```python
def create_presigned_notebook_instance_url(
    NotebookInstanceName: str,
    SessionExpirationDurationInSeconds: int = None,
) -> Dict[str, Any]:
```

### Client().create_training_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L156)

```python
def create_training_job(
    TrainingJobName: str,
    AlgorithmSpecification: Dict[str, Any],
    RoleArn: str,
    OutputDataConfig: Dict[str, Any],
    ResourceConfig: Dict[str, Any],
    StoppingCondition: Dict[str, Any],
    HyperParameters: Dict[str, Any] = None,
    InputDataConfig: List[Any] = None,
    VpcConfig: Dict[str, Any] = None,
    Tags: List[Any] = None,
    EnableNetworkIsolation: bool = None,
    EnableInterContainerTrafficEncryption: bool = None,
    EnableManagedSpotTraining: bool = None,
    CheckpointConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_transform_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L176)

```python
def create_transform_job(
    TransformJobName: str,
    ModelName: str,
    TransformInput: Dict[str, Any],
    TransformOutput: Dict[str, Any],
    TransformResources: Dict[str, Any],
    MaxConcurrentTransforms: int = None,
    MaxPayloadInMB: int = None,
    BatchStrategy: str = None,
    Environment: Dict[str, Any] = None,
    DataProcessing: Dict[str, Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_workteam

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L193)

```python
def create_workteam(
    WorkteamName: str,
    MemberDefinitions: List[Any],
    Description: str,
    NotificationConfiguration: Dict[str, Any] = None,
    Tags: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_algorithm

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L204)

```python
def delete_algorithm(AlgorithmName: str) -> None:
```

### Client().delete_code_repository

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L208)

```python
def delete_code_repository(CodeRepositoryName: str) -> None:
```

### Client().delete_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L212)

```python
def delete_endpoint(EndpointName: str) -> None:
```

### Client().delete_endpoint_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L216)

```python
def delete_endpoint_config(EndpointConfigName: str) -> None:
```

### Client().delete_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L220)

```python
def delete_model(ModelName: str) -> None:
```

### Client().delete_model_package

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L224)

```python
def delete_model_package(ModelPackageName: str) -> None:
```

### Client().delete_notebook_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L228)

```python
def delete_notebook_instance(NotebookInstanceName: str) -> None:
```

### Client().delete_notebook_instance_lifecycle_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L232)

```python
def delete_notebook_instance_lifecycle_config(
    NotebookInstanceLifecycleConfigName: str,
) -> None:
```

### Client().delete_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L238)

```python
def delete_tags(ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().delete_workteam

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L242)

```python
def delete_workteam(WorkteamName: str) -> Dict[str, Any]:
```

### Client().describe_algorithm

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L246)

```python
def describe_algorithm(AlgorithmName: str) -> Dict[str, Any]:
```

### Client().describe_code_repository

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L250)

```python
def describe_code_repository(CodeRepositoryName: str) -> Dict[str, Any]:
```

### Client().describe_compilation_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L254)

```python
def describe_compilation_job(CompilationJobName: str) -> Dict[str, Any]:
```

### Client().describe_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L258)

```python
def describe_endpoint(EndpointName: str) -> Dict[str, Any]:
```

### Client().describe_endpoint_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L262)

```python
def describe_endpoint_config(EndpointConfigName: str) -> Dict[str, Any]:
```

### Client().describe_hyper_parameter_tuning_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L266)

```python
def describe_hyper_parameter_tuning_job(
    HyperParameterTuningJobName: str,
) -> Dict[str, Any]:
```

### Client().describe_labeling_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L272)

```python
def describe_labeling_job(LabelingJobName: str) -> Dict[str, Any]:
```

### Client().describe_model

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L276)

```python
def describe_model(ModelName: str) -> Dict[str, Any]:
```

### Client().describe_model_package

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L280)

```python
def describe_model_package(ModelPackageName: str) -> Dict[str, Any]:
```

### Client().describe_notebook_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L284)

```python
def describe_notebook_instance(NotebookInstanceName: str) -> Dict[str, Any]:
```

### Client().describe_notebook_instance_lifecycle_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L288)

```python
def describe_notebook_instance_lifecycle_config(
    NotebookInstanceLifecycleConfigName: str,
) -> Dict[str, Any]:
```

### Client().describe_subscribed_workteam

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L294)

```python
def describe_subscribed_workteam(WorkteamArn: str) -> Dict[str, Any]:
```

### Client().describe_training_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L298)

```python
def describe_training_job(TrainingJobName: str) -> Dict[str, Any]:
```

### Client().describe_transform_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L302)

```python
def describe_transform_job(TransformJobName: str) -> Dict[str, Any]:
```

### Client().describe_workteam

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L306)

```python
def describe_workteam(WorkteamName: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L310)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L320)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_search_suggestions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L324)

```python
def get_search_suggestions(
    Resource: str,
    SuggestionQuery: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L330)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_algorithms

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L334)

```python
def list_algorithms(
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    MaxResults: int = None,
    NameContains: str = None,
    NextToken: str = None,
    SortBy: str = None,
    SortOrder: str = None,
) -> Dict[str, Any]:
```

### Client().list_code_repositories

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L347)

```python
def list_code_repositories(
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    MaxResults: int = None,
    NameContains: str = None,
    NextToken: str = None,
    SortBy: str = None,
    SortOrder: str = None,
) -> Dict[str, Any]:
```

### Client().list_compilation_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L362)

```python
def list_compilation_jobs(
    NextToken: str = None,
    MaxResults: int = None,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    NameContains: str = None,
    StatusEquals: str = None,
    SortBy: str = None,
    SortOrder: str = None,
) -> Dict[str, Any]:
```

### Client().list_endpoint_configs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L378)

```python
def list_endpoint_configs(
    SortBy: str = None,
    SortOrder: str = None,
    NextToken: str = None,
    MaxResults: int = None,
    NameContains: str = None,
    CreationTimeBefore: datetime = None,
    CreationTimeAfter: datetime = None,
) -> Dict[str, Any]:
```

### Client().list_endpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L391)

```python
def list_endpoints(
    SortBy: str = None,
    SortOrder: str = None,
    NextToken: str = None,
    MaxResults: int = None,
    NameContains: str = None,
    CreationTimeBefore: datetime = None,
    CreationTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    StatusEquals: str = None,
) -> Dict[str, Any]:
```

### Client().list_hyper_parameter_tuning_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L407)

```python
def list_hyper_parameter_tuning_jobs(
    NextToken: str = None,
    MaxResults: int = None,
    SortBy: str = None,
    SortOrder: str = None,
    NameContains: str = None,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    StatusEquals: str = None,
) -> Dict[str, Any]:
```

### Client().list_labeling_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L423)

```python
def list_labeling_jobs(
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    MaxResults: int = None,
    NextToken: str = None,
    NameContains: str = None,
    SortBy: str = None,
    SortOrder: str = None,
    StatusEquals: str = None,
) -> Dict[str, Any]:
```

### Client().list_labeling_jobs_for_workteam

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L439)

```python
def list_labeling_jobs_for_workteam(
    WorkteamArn: str,
    MaxResults: int = None,
    NextToken: str = None,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    JobReferenceCodeContains: str = None,
    SortBy: str = None,
    SortOrder: str = None,
) -> Dict[str, Any]:
```

### Client().list_model_packages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L453)

```python
def list_model_packages(
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    MaxResults: int = None,
    NameContains: str = None,
    NextToken: str = None,
    SortBy: str = None,
    SortOrder: str = None,
) -> Dict[str, Any]:
```

### Client().list_models

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L466)

```python
def list_models(
    SortBy: str = None,
    SortOrder: str = None,
    NextToken: str = None,
    MaxResults: int = None,
    NameContains: str = None,
    CreationTimeBefore: datetime = None,
    CreationTimeAfter: datetime = None,
) -> Dict[str, Any]:
```

### Client().list_notebook_instance_lifecycle_configs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L479)

```python
def list_notebook_instance_lifecycle_configs(
    NextToken: str = None,
    MaxResults: int = None,
    SortBy: str = None,
    SortOrder: str = None,
    NameContains: str = None,
    CreationTimeBefore: datetime = None,
    CreationTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
) -> Dict[str, Any]:
```

### Client().list_notebook_instances

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L494)

```python
def list_notebook_instances(
    NextToken: str = None,
    MaxResults: int = None,
    SortBy: str = None,
    SortOrder: str = None,
    NameContains: str = None,
    CreationTimeBefore: datetime = None,
    CreationTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    StatusEquals: str = None,
    NotebookInstanceLifecycleConfigNameContains: str = None,
    DefaultCodeRepositoryContains: str = None,
    AdditionalCodeRepositoryEquals: str = None,
) -> Dict[str, Any]:
```

### Client().list_subscribed_workteams

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L513)

```python
def list_subscribed_workteams(
    NameContains: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L519)

```python
def list_tags(
    ResourceArn: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_training_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L525)

```python
def list_training_jobs(
    NextToken: str = None,
    MaxResults: int = None,
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    NameContains: str = None,
    StatusEquals: str = None,
    SortBy: str = None,
    SortOrder: str = None,
) -> Dict[str, Any]:
```

### Client().list_training_jobs_for_hyper_parameter_tuning_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L541)

```python
def list_training_jobs_for_hyper_parameter_tuning_job(
    HyperParameterTuningJobName: str,
    NextToken: str = None,
    MaxResults: int = None,
    StatusEquals: str = None,
    SortBy: str = None,
    SortOrder: str = None,
) -> Dict[str, Any]:
```

### Client().list_transform_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L553)

```python
def list_transform_jobs(
    CreationTimeAfter: datetime = None,
    CreationTimeBefore: datetime = None,
    LastModifiedTimeAfter: datetime = None,
    LastModifiedTimeBefore: datetime = None,
    NameContains: str = None,
    StatusEquals: str = None,
    SortBy: str = None,
    SortOrder: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_workteams

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L569)

```python
def list_workteams(
    SortBy: str = None,
    SortOrder: str = None,
    NameContains: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().render_ui_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L580)

```python
def render_ui_template(
    UiTemplate: Dict[str, Any],
    Task: Dict[str, Any],
    RoleArn: str,
) -> Dict[str, Any]:
```

### Client().search

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L586)

```python
def search(
    Resource: str,
    SearchExpression: Dict[str, Any] = None,
    SortBy: str = None,
    SortOrder: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().start_notebook_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L598)

```python
def start_notebook_instance(NotebookInstanceName: str) -> None:
```

### Client().stop_compilation_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L602)

```python
def stop_compilation_job(CompilationJobName: str) -> None:
```

### Client().stop_hyper_parameter_tuning_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L606)

```python
def stop_hyper_parameter_tuning_job(HyperParameterTuningJobName: str) -> None:
```

### Client().stop_labeling_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L610)

```python
def stop_labeling_job(LabelingJobName: str) -> None:
```

### Client().stop_notebook_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L614)

```python
def stop_notebook_instance(NotebookInstanceName: str) -> None:
```

### Client().stop_training_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L618)

```python
def stop_training_job(TrainingJobName: str) -> None:
```

### Client().stop_transform_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L622)

```python
def stop_transform_job(TransformJobName: str) -> None:
```

### Client().update_code_repository

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L626)

```python
def update_code_repository(
    CodeRepositoryName: str,
    GitConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L632)

```python
def update_endpoint(
    EndpointName: str,
    EndpointConfigName: str,
) -> Dict[str, Any]:
```

### Client().update_endpoint_weights_and_capacities

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L638)

```python
def update_endpoint_weights_and_capacities(
    EndpointName: str,
    DesiredWeightsAndCapacities: List[Any],
) -> Dict[str, Any]:
```

### Client().update_notebook_instance

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L644)

```python
def update_notebook_instance(
    NotebookInstanceName: str,
    InstanceType: str = None,
    RoleArn: str = None,
    LifecycleConfigName: str = None,
    DisassociateLifecycleConfig: bool = None,
    VolumeSizeInGB: int = None,
    DefaultCodeRepository: str = None,
    AdditionalCodeRepositories: List[Any] = None,
    AcceleratorTypes: List[Any] = None,
    DisassociateAcceleratorTypes: bool = None,
    DisassociateDefaultCodeRepository: bool = None,
    DisassociateAdditionalCodeRepositories: bool = None,
    RootAccess: str = None,
) -> Dict[str, Any]:
```

### Client().update_notebook_instance_lifecycle_config

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L663)

```python
def update_notebook_instance_lifecycle_config(
    NotebookInstanceLifecycleConfigName: str,
    OnCreate: List[Any] = None,
    OnStart: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_workteam

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/sagemaker/client.py#L672)

```python
def update_workteam(
    WorkteamName: str,
    MemberDefinitions: List[Any] = None,
    Description: str = None,
    NotificationConfiguration: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

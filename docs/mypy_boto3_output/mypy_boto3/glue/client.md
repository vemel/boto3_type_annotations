# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.glue.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Glue](index.md#glue) / Client
    - [Client](#client)
        - [Client().batch_create_partition](#clientbatch_create_partition)
        - [Client().batch_delete_connection](#clientbatch_delete_connection)
        - [Client().batch_delete_partition](#clientbatch_delete_partition)
        - [Client().batch_delete_table](#clientbatch_delete_table)
        - [Client().batch_delete_table_version](#clientbatch_delete_table_version)
        - [Client().batch_get_crawlers](#clientbatch_get_crawlers)
        - [Client().batch_get_dev_endpoints](#clientbatch_get_dev_endpoints)
        - [Client().batch_get_jobs](#clientbatch_get_jobs)
        - [Client().batch_get_partition](#clientbatch_get_partition)
        - [Client().batch_get_triggers](#clientbatch_get_triggers)
        - [Client().batch_get_workflows](#clientbatch_get_workflows)
        - [Client().batch_stop_job_run](#clientbatch_stop_job_run)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().cancel_ml_task_run](#clientcancel_ml_task_run)
        - [Client().create_classifier](#clientcreate_classifier)
        - [Client().create_connection](#clientcreate_connection)
        - [Client().create_crawler](#clientcreate_crawler)
        - [Client().create_database](#clientcreate_database)
        - [Client().create_dev_endpoint](#clientcreate_dev_endpoint)
        - [Client().create_job](#clientcreate_job)
        - [Client().create_ml_transform](#clientcreate_ml_transform)
        - [Client().create_partition](#clientcreate_partition)
        - [Client().create_script](#clientcreate_script)
        - [Client().create_security_configuration](#clientcreate_security_configuration)
        - [Client().create_table](#clientcreate_table)
        - [Client().create_trigger](#clientcreate_trigger)
        - [Client().create_user_defined_function](#clientcreate_user_defined_function)
        - [Client().create_workflow](#clientcreate_workflow)
        - [Client().delete_classifier](#clientdelete_classifier)
        - [Client().delete_connection](#clientdelete_connection)
        - [Client().delete_crawler](#clientdelete_crawler)
        - [Client().delete_database](#clientdelete_database)
        - [Client().delete_dev_endpoint](#clientdelete_dev_endpoint)
        - [Client().delete_job](#clientdelete_job)
        - [Client().delete_ml_transform](#clientdelete_ml_transform)
        - [Client().delete_partition](#clientdelete_partition)
        - [Client().delete_resource_policy](#clientdelete_resource_policy)
        - [Client().delete_security_configuration](#clientdelete_security_configuration)
        - [Client().delete_table](#clientdelete_table)
        - [Client().delete_table_version](#clientdelete_table_version)
        - [Client().delete_trigger](#clientdelete_trigger)
        - [Client().delete_user_defined_function](#clientdelete_user_defined_function)
        - [Client().delete_workflow](#clientdelete_workflow)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_catalog_import_status](#clientget_catalog_import_status)
        - [Client().get_classifier](#clientget_classifier)
        - [Client().get_classifiers](#clientget_classifiers)
        - [Client().get_connection](#clientget_connection)
        - [Client().get_connections](#clientget_connections)
        - [Client().get_crawler](#clientget_crawler)
        - [Client().get_crawler_metrics](#clientget_crawler_metrics)
        - [Client().get_crawlers](#clientget_crawlers)
        - [Client().get_data_catalog_encryption_settings](#clientget_data_catalog_encryption_settings)
        - [Client().get_database](#clientget_database)
        - [Client().get_databases](#clientget_databases)
        - [Client().get_dataflow_graph](#clientget_dataflow_graph)
        - [Client().get_dev_endpoint](#clientget_dev_endpoint)
        - [Client().get_dev_endpoints](#clientget_dev_endpoints)
        - [Client().get_job](#clientget_job)
        - [Client().get_job_bookmark](#clientget_job_bookmark)
        - [Client().get_job_run](#clientget_job_run)
        - [Client().get_job_runs](#clientget_job_runs)
        - [Client().get_jobs](#clientget_jobs)
        - [Client().get_mapping](#clientget_mapping)
        - [Client().get_ml_task_run](#clientget_ml_task_run)
        - [Client().get_ml_task_runs](#clientget_ml_task_runs)
        - [Client().get_ml_transform](#clientget_ml_transform)
        - [Client().get_ml_transforms](#clientget_ml_transforms)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_partition](#clientget_partition)
        - [Client().get_partitions](#clientget_partitions)
        - [Client().get_plan](#clientget_plan)
        - [Client().get_resource_policy](#clientget_resource_policy)
        - [Client().get_security_configuration](#clientget_security_configuration)
        - [Client().get_security_configurations](#clientget_security_configurations)
        - [Client().get_table](#clientget_table)
        - [Client().get_table_version](#clientget_table_version)
        - [Client().get_table_versions](#clientget_table_versions)
        - [Client().get_tables](#clientget_tables)
        - [Client().get_tags](#clientget_tags)
        - [Client().get_trigger](#clientget_trigger)
        - [Client().get_triggers](#clientget_triggers)
        - [Client().get_user_defined_function](#clientget_user_defined_function)
        - [Client().get_user_defined_functions](#clientget_user_defined_functions)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().get_workflow](#clientget_workflow)
        - [Client().get_workflow_run](#clientget_workflow_run)
        - [Client().get_workflow_run_properties](#clientget_workflow_run_properties)
        - [Client().get_workflow_runs](#clientget_workflow_runs)
        - [Client().import_catalog_to_glue](#clientimport_catalog_to_glue)
        - [Client().list_crawlers](#clientlist_crawlers)
        - [Client().list_dev_endpoints](#clientlist_dev_endpoints)
        - [Client().list_jobs](#clientlist_jobs)
        - [Client().list_triggers](#clientlist_triggers)
        - [Client().list_workflows](#clientlist_workflows)
        - [Client().put_data_catalog_encryption_settings](#clientput_data_catalog_encryption_settings)
        - [Client().put_resource_policy](#clientput_resource_policy)
        - [Client().put_workflow_run_properties](#clientput_workflow_run_properties)
        - [Client().reset_job_bookmark](#clientreset_job_bookmark)
        - [Client().search_tables](#clientsearch_tables)
        - [Client().start_crawler](#clientstart_crawler)
        - [Client().start_crawler_schedule](#clientstart_crawler_schedule)
        - [Client().start_export_labels_task_run](#clientstart_export_labels_task_run)
        - [Client().start_import_labels_task_run](#clientstart_import_labels_task_run)
        - [Client().start_job_run](#clientstart_job_run)
        - [Client().start_ml_evaluation_task_run](#clientstart_ml_evaluation_task_run)
        - [Client().start_ml_labeling_set_generation_task_run](#clientstart_ml_labeling_set_generation_task_run)
        - [Client().start_trigger](#clientstart_trigger)
        - [Client().start_workflow_run](#clientstart_workflow_run)
        - [Client().stop_crawler](#clientstop_crawler)
        - [Client().stop_crawler_schedule](#clientstop_crawler_schedule)
        - [Client().stop_trigger](#clientstop_trigger)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_classifier](#clientupdate_classifier)
        - [Client().update_connection](#clientupdate_connection)
        - [Client().update_crawler](#clientupdate_crawler)
        - [Client().update_crawler_schedule](#clientupdate_crawler_schedule)
        - [Client().update_database](#clientupdate_database)
        - [Client().update_dev_endpoint](#clientupdate_dev_endpoint)
        - [Client().update_job](#clientupdate_job)
        - [Client().update_ml_transform](#clientupdate_ml_transform)
        - [Client().update_partition](#clientupdate_partition)
        - [Client().update_table](#clientupdate_table)
        - [Client().update_trigger](#clientupdate_trigger)
        - [Client().update_user_defined_function](#clientupdate_user_defined_function)
        - [Client().update_workflow](#clientupdate_workflow)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L12)

```python
class Client(BaseClient):
```

### Client().batch_create_partition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L15)

```python
def batch_create_partition(
    DatabaseName: str,
    TableName: str,
    PartitionInputList: List[Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().batch_delete_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L25)

```python
def batch_delete_connection(
    ConnectionNameList: List[Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().batch_delete_partition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L31)

```python
def batch_delete_partition(
    DatabaseName: str,
    TableName: str,
    PartitionsToDelete: List[Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().batch_delete_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L41)

```python
def batch_delete_table(
    DatabaseName: str,
    TablesToDelete: List[Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().batch_delete_table_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L47)

```python
def batch_delete_table_version(
    DatabaseName: str,
    TableName: str,
    VersionIds: List[Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().batch_get_crawlers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L57)

```python
def batch_get_crawlers(CrawlerNames: List[Any]) -> Dict[str, Any]:
```

### Client().batch_get_dev_endpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L61)

```python
def batch_get_dev_endpoints(DevEndpointNames: List[Any]) -> Dict[str, Any]:
```

### Client().batch_get_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L65)

```python
def batch_get_jobs(JobNames: List[Any]) -> Dict[str, Any]:
```

### Client().batch_get_partition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L69)

```python
def batch_get_partition(
    DatabaseName: str,
    TableName: str,
    PartitionsToGet: List[Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().batch_get_triggers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L79)

```python
def batch_get_triggers(TriggerNames: List[Any]) -> Dict[str, Any]:
```

### Client().batch_get_workflows

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L83)

```python
def batch_get_workflows(
    Names: List[Any],
    IncludeGraph: bool = None,
) -> Dict[str, Any]:
```

### Client().batch_stop_job_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L89)

```python
def batch_stop_job_run(JobName: str, JobRunIds: List[Any]) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L93)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().cancel_ml_task_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L97)

```python
def cancel_ml_task_run(TransformId: str, TaskRunId: str) -> Dict[str, Any]:
```

### Client().create_classifier

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L101)

```python
def create_classifier(
    GrokClassifier: Dict[str, Any] = None,
    XMLClassifier: Dict[str, Any] = None,
    JsonClassifier: Dict[str, Any] = None,
    CsvClassifier: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L111)

```python
def create_connection(
    ConnectionInput: Dict[str, Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().create_crawler

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L117)

```python
def create_crawler(
    Name: str,
    Role: str,
    Targets: Dict[str, Any],
    DatabaseName: str = None,
    Description: str = None,
    Schedule: str = None,
    Classifiers: List[Any] = None,
    TablePrefix: str = None,
    SchemaChangePolicy: Dict[str, Any] = None,
    Configuration: str = None,
    CrawlerSecurityConfiguration: str = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_database

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L135)

```python
def create_database(
    DatabaseInput: Dict[str, Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().create_dev_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L141)

```python
def create_dev_endpoint(
    EndpointName: str,
    RoleArn: str,
    SecurityGroupIds: List[Any] = None,
    SubnetId: str = None,
    PublicKey: str = None,
    PublicKeys: List[Any] = None,
    NumberOfNodes: int = None,
    WorkerType: str = None,
    GlueVersion: str = None,
    NumberOfWorkers: int = None,
    ExtraPythonLibsS3Path: str = None,
    ExtraJarsS3Path: str = None,
    SecurityConfiguration: str = None,
    Tags: Dict[str, Any] = None,
    Arguments: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L162)

```python
def create_job(
    Name: str,
    Role: str,
    Command: Dict[str, Any],
    Description: str = None,
    LogUri: str = None,
    ExecutionProperty: Dict[str, Any] = None,
    DefaultArguments: Dict[str, Any] = None,
    Connections: Dict[str, Any] = None,
    MaxRetries: int = None,
    AllocatedCapacity: int = None,
    Timeout: int = None,
    MaxCapacity: float = None,
    SecurityConfiguration: str = None,
    Tags: Dict[str, Any] = None,
    NotificationProperty: Dict[str, Any] = None,
    GlueVersion: str = None,
    NumberOfWorkers: int = None,
    WorkerType: str = None,
) -> Dict[str, Any]:
```

### Client().create_ml_transform

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L186)

```python
def create_ml_transform(
    Name: str,
    InputRecordTables: List[Any],
    Parameters: Dict[str, Any],
    Role: str,
    Description: str = None,
    MaxCapacity: float = None,
    WorkerType: str = None,
    NumberOfWorkers: int = None,
    Timeout: int = None,
    MaxRetries: int = None,
) -> Dict[str, Any]:
```

### Client().create_partition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L202)

```python
def create_partition(
    DatabaseName: str,
    TableName: str,
    PartitionInput: Dict[str, Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().create_script

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L212)

```python
def create_script(
    DagNodes: List[Any] = None,
    DagEdges: List[Any] = None,
    Language: str = None,
) -> Dict[str, Any]:
```

### Client().create_security_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L221)

```python
def create_security_configuration(
    Name: str,
    EncryptionConfiguration: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().create_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L227)

```python
def create_table(
    DatabaseName: str,
    TableInput: Dict[str, Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().create_trigger

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L233)

```python
def create_trigger(
    Name: str,
    Type: str,
    Actions: List[Any],
    WorkflowName: str = None,
    Schedule: str = None,
    Predicate: Dict[str, Any] = None,
    Description: str = None,
    StartOnCreation: bool = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_user_defined_function

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L248)

```python
def create_user_defined_function(
    DatabaseName: str,
    FunctionInput: Dict[str, Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().create_workflow

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L254)

```python
def create_workflow(
    Name: str,
    Description: str = None,
    DefaultRunProperties: Dict[str, Any] = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().delete_classifier

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L264)

```python
def delete_classifier(Name: str) -> Dict[str, Any]:
```

### Client().delete_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L268)

```python
def delete_connection(
    ConnectionName: str,
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().delete_crawler

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L274)

```python
def delete_crawler(Name: str) -> Dict[str, Any]:
```

### Client().delete_database

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L278)

```python
def delete_database(Name: str, CatalogId: str = None) -> Dict[str, Any]:
```

### Client().delete_dev_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L282)

```python
def delete_dev_endpoint(EndpointName: str) -> Dict[str, Any]:
```

### Client().delete_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L286)

```python
def delete_job(JobName: str) -> Dict[str, Any]:
```

### Client().delete_ml_transform

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L290)

```python
def delete_ml_transform(TransformId: str) -> Dict[str, Any]:
```

### Client().delete_partition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L294)

```python
def delete_partition(
    DatabaseName: str,
    TableName: str,
    PartitionValues: List[Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().delete_resource_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L304)

```python
def delete_resource_policy(PolicyHashCondition: str = None) -> Dict[str, Any]:
```

### Client().delete_security_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L308)

```python
def delete_security_configuration(Name: str) -> Dict[str, Any]:
```

### Client().delete_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L312)

```python
def delete_table(
    DatabaseName: str,
    Name: str,
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().delete_table_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L318)

```python
def delete_table_version(
    DatabaseName: str,
    TableName: str,
    VersionId: str,
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().delete_trigger

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L324)

```python
def delete_trigger(Name: str) -> Dict[str, Any]:
```

### Client().delete_user_defined_function

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L328)

```python
def delete_user_defined_function(
    DatabaseName: str,
    FunctionName: str,
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().delete_workflow

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L334)

```python
def delete_workflow(Name: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L338)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_catalog_import_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L348)

```python
def get_catalog_import_status(CatalogId: str = None) -> Dict[str, Any]:
```

### Client().get_classifier

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L352)

```python
def get_classifier(Name: str) -> Dict[str, Any]:
```

### Client().get_classifiers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L356)

```python
def get_classifiers(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L362)

```python
def get_connection(
    Name: str,
    CatalogId: str = None,
    HidePassword: bool = None,
) -> Dict[str, Any]:
```

### Client().get_connections

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L368)

```python
def get_connections(
    CatalogId: str = None,
    Filter: Dict[str, Any] = None,
    HidePassword: bool = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_crawler

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L379)

```python
def get_crawler(Name: str) -> Dict[str, Any]:
```

### Client().get_crawler_metrics

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L383)

```python
def get_crawler_metrics(
    CrawlerNameList: List[Any] = None,
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_crawlers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L392)

```python
def get_crawlers(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_data_catalog_encryption_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L398)

```python
def get_data_catalog_encryption_settings(
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().get_database

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L404)

```python
def get_database(Name: str, CatalogId: str = None) -> Dict[str, Any]:
```

### Client().get_databases

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L408)

```python
def get_databases(
    CatalogId: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_dataflow_graph

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L414)

```python
def get_dataflow_graph(PythonScript: str = None) -> Dict[str, Any]:
```

### Client().get_dev_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L418)

```python
def get_dev_endpoint(EndpointName: str) -> Dict[str, Any]:
```

### Client().get_dev_endpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L422)

```python
def get_dev_endpoints(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L428)

```python
def get_job(JobName: str) -> Dict[str, Any]:
```

### Client().get_job_bookmark

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L432)

```python
def get_job_bookmark(JobName: str, RunId: str = None) -> Dict[str, Any]:
```

### Client().get_job_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L436)

```python
def get_job_run(
    JobName: str,
    RunId: str,
    PredecessorsIncluded: bool = None,
) -> Dict[str, Any]:
```

### Client().get_job_runs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L442)

```python
def get_job_runs(
    JobName: str,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L448)

```python
def get_jobs(NextToken: str = None, MaxResults: int = None) -> Dict[str, Any]:
```

### Client().get_mapping

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L452)

```python
def get_mapping(
    Source: Dict[str, Any],
    Sinks: List[Any] = None,
    Location: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().get_ml_task_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L461)

```python
def get_ml_task_run(TransformId: str, TaskRunId: str) -> Dict[str, Any]:
```

### Client().get_ml_task_runs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L465)

```python
def get_ml_task_runs(
    TransformId: str,
    NextToken: str = None,
    MaxResults: int = None,
    Filter: Dict[str, Any] = None,
    Sort: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().get_ml_transform

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L476)

```python
def get_ml_transform(TransformId: str) -> Dict[str, Any]:
```

### Client().get_ml_transforms

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L480)

```python
def get_ml_transforms(
    NextToken: str = None,
    MaxResults: int = None,
    Filter: Dict[str, Any] = None,
    Sort: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L490)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_partition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L494)

```python
def get_partition(
    DatabaseName: str,
    TableName: str,
    PartitionValues: List[Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().get_partitions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L504)

```python
def get_partitions(
    DatabaseName: str,
    TableName: str,
    CatalogId: str = None,
    Expression: str = None,
    NextToken: str = None,
    Segment: Dict[str, Any] = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_plan

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L517)

```python
def get_plan(
    Mapping: List[Any],
    Source: Dict[str, Any],
    Sinks: List[Any] = None,
    Location: Dict[str, Any] = None,
    Language: str = None,
) -> Dict[str, Any]:
```

### Client().get_resource_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L528)

```python
def get_resource_policy() -> Dict[str, Any]:
```

### Client().get_security_configuration

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L532)

```python
def get_security_configuration(Name: str) -> Dict[str, Any]:
```

### Client().get_security_configurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L536)

```python
def get_security_configurations(
    MaxResults: int = None,
    NextToken: str = None,
) -> Dict[str, Any]:
```

### Client().get_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L542)

```python
def get_table(
    DatabaseName: str,
    Name: str,
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().get_table_version

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L548)

```python
def get_table_version(
    DatabaseName: str,
    TableName: str,
    CatalogId: str = None,
    VersionId: str = None,
) -> Dict[str, Any]:
```

### Client().get_table_versions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L558)

```python
def get_table_versions(
    DatabaseName: str,
    TableName: str,
    CatalogId: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_tables

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L569)

```python
def get_tables(
    DatabaseName: str,
    CatalogId: str = None,
    Expression: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_tags

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L580)

```python
def get_tags(ResourceArn: str) -> Dict[str, Any]:
```

### Client().get_trigger

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L584)

```python
def get_trigger(Name: str) -> Dict[str, Any]:
```

### Client().get_triggers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L588)

```python
def get_triggers(
    NextToken: str = None,
    DependentJobName: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_user_defined_function

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L597)

```python
def get_user_defined_function(
    DatabaseName: str,
    FunctionName: str,
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().get_user_defined_functions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L603)

```python
def get_user_defined_functions(
    DatabaseName: str,
    Pattern: str,
    CatalogId: str = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L614)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().get_workflow

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L618)

```python
def get_workflow(Name: str, IncludeGraph: bool = None) -> Dict[str, Any]:
```

### Client().get_workflow_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L622)

```python
def get_workflow_run(
    Name: str,
    RunId: str,
    IncludeGraph: bool = None,
) -> Dict[str, Any]:
```

### Client().get_workflow_run_properties

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L628)

```python
def get_workflow_run_properties(Name: str, RunId: str) -> Dict[str, Any]:
```

### Client().get_workflow_runs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L632)

```python
def get_workflow_runs(
    Name: str,
    IncludeGraph: bool = None,
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().import_catalog_to_glue

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L642)

```python
def import_catalog_to_glue(CatalogId: str = None) -> Dict[str, Any]:
```

### Client().list_crawlers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L646)

```python
def list_crawlers(
    MaxResults: int = None,
    NextToken: str = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().list_dev_endpoints

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L652)

```python
def list_dev_endpoints(
    NextToken: str = None,
    MaxResults: int = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().list_jobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L658)

```python
def list_jobs(
    NextToken: str = None,
    MaxResults: int = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().list_triggers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L664)

```python
def list_triggers(
    NextToken: str = None,
    DependentJobName: str = None,
    MaxResults: int = None,
    Tags: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().list_workflows

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L674)

```python
def list_workflows(
    NextToken: str = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().put_data_catalog_encryption_settings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L680)

```python
def put_data_catalog_encryption_settings(
    DataCatalogEncryptionSettings: Dict[str, Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().put_resource_policy

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L686)

```python
def put_resource_policy(
    PolicyInJson: str,
    PolicyHashCondition: str = None,
    PolicyExistsCondition: str = None,
) -> Dict[str, Any]:
```

### Client().put_workflow_run_properties

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L695)

```python
def put_workflow_run_properties(
    Name: str,
    RunId: str,
    RunProperties: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().reset_job_bookmark

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L701)

```python
def reset_job_bookmark(JobName: str, RunId: str = None) -> Dict[str, Any]:
```

### Client().search_tables

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L705)

```python
def search_tables(
    CatalogId: str = None,
    NextToken: str = None,
    Filters: List[Any] = None,
    SearchText: str = None,
    SortCriteria: List[Any] = None,
    MaxResults: int = None,
) -> Dict[str, Any]:
```

### Client().start_crawler

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L717)

```python
def start_crawler(Name: str) -> Dict[str, Any]:
```

### Client().start_crawler_schedule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L721)

```python
def start_crawler_schedule(CrawlerName: str) -> Dict[str, Any]:
```

### Client().start_export_labels_task_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L725)

```python
def start_export_labels_task_run(
    TransformId: str,
    OutputS3Path: str,
) -> Dict[str, Any]:
```

### Client().start_import_labels_task_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L731)

```python
def start_import_labels_task_run(
    TransformId: str,
    InputS3Path: str,
    ReplaceAllLabels: bool = None,
) -> Dict[str, Any]:
```

### Client().start_job_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L737)

```python
def start_job_run(
    JobName: str,
    JobRunId: str = None,
    Arguments: Dict[str, Any] = None,
    AllocatedCapacity: int = None,
    Timeout: int = None,
    MaxCapacity: float = None,
    SecurityConfiguration: str = None,
    NotificationProperty: Dict[str, Any] = None,
    WorkerType: str = None,
    NumberOfWorkers: int = None,
) -> Dict[str, Any]:
```

### Client().start_ml_evaluation_task_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L753)

```python
def start_ml_evaluation_task_run(TransformId: str) -> Dict[str, Any]:
```

### Client().start_ml_labeling_set_generation_task_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L757)

```python
def start_ml_labeling_set_generation_task_run(
    TransformId: str,
    OutputS3Path: str,
) -> Dict[str, Any]:
```

### Client().start_trigger

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L763)

```python
def start_trigger(Name: str) -> Dict[str, Any]:
```

### Client().start_workflow_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L767)

```python
def start_workflow_run(Name: str) -> Dict[str, Any]:
```

### Client().stop_crawler

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L771)

```python
def stop_crawler(Name: str) -> Dict[str, Any]:
```

### Client().stop_crawler_schedule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L775)

```python
def stop_crawler_schedule(CrawlerName: str) -> Dict[str, Any]:
```

### Client().stop_trigger

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L779)

```python
def stop_trigger(Name: str) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L783)

```python
def tag_resource(
    ResourceArn: str,
    TagsToAdd: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L789)

```python
def untag_resource(
    ResourceArn: str,
    TagsToRemove: List[Any],
) -> Dict[str, Any]:
```

### Client().update_classifier

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L795)

```python
def update_classifier(
    GrokClassifier: Dict[str, Any] = None,
    XMLClassifier: Dict[str, Any] = None,
    JsonClassifier: Dict[str, Any] = None,
    CsvClassifier: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_connection

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L805)

```python
def update_connection(
    Name: str,
    ConnectionInput: Dict[str, Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().update_crawler

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L811)

```python
def update_crawler(
    Name: str,
    Role: str = None,
    DatabaseName: str = None,
    Description: str = None,
    Targets: Dict[str, Any] = None,
    Schedule: str = None,
    Classifiers: List[Any] = None,
    TablePrefix: str = None,
    SchemaChangePolicy: Dict[str, Any] = None,
    Configuration: str = None,
    CrawlerSecurityConfiguration: str = None,
) -> Dict[str, Any]:
```

### Client().update_crawler_schedule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L828)

```python
def update_crawler_schedule(
    CrawlerName: str,
    Schedule: str = None,
) -> Dict[str, Any]:
```

### Client().update_database

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L834)

```python
def update_database(
    Name: str,
    DatabaseInput: Dict[str, Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().update_dev_endpoint

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L840)

```python
def update_dev_endpoint(
    EndpointName: str,
    PublicKey: str = None,
    AddPublicKeys: List[Any] = None,
    DeletePublicKeys: List[Any] = None,
    CustomLibraries: Dict[str, Any] = None,
    UpdateEtlLibraries: bool = None,
    DeleteArguments: List[Any] = None,
    AddArguments: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_job

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L854)

```python
def update_job(JobName: str, JobUpdate: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().update_ml_transform

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L858)

```python
def update_ml_transform(
    TransformId: str,
    Name: str = None,
    Description: str = None,
    Parameters: Dict[str, Any] = None,
    Role: str = None,
    MaxCapacity: float = None,
    WorkerType: str = None,
    NumberOfWorkers: int = None,
    Timeout: int = None,
    MaxRetries: int = None,
) -> Dict[str, Any]:
```

### Client().update_partition

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L874)

```python
def update_partition(
    DatabaseName: str,
    TableName: str,
    PartitionValueList: List[Any],
    PartitionInput: Dict[str, Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().update_table

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L885)

```python
def update_table(
    DatabaseName: str,
    TableInput: Dict[str, Any],
    CatalogId: str = None,
    SkipArchive: bool = None,
) -> Dict[str, Any]:
```

### Client().update_trigger

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L895)

```python
def update_trigger(
    Name: str,
    TriggerUpdate: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_user_defined_function

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L901)

```python
def update_user_defined_function(
    DatabaseName: str,
    FunctionName: str,
    FunctionInput: Dict[str, Any],
    CatalogId: str = None,
) -> Dict[str, Any]:
```

### Client().update_workflow

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/glue/client.py#L911)

```python
def update_workflow(
    Name: str,
    Description: str = None,
    DefaultRunProperties: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

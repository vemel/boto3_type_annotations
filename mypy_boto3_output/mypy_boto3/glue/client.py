from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def batch_create_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionInputList: List[Any],
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_delete_connection(
        self, ConnectionNameList: List[Any], CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_delete_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionsToDelete: List[Any],
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_delete_table(
        self, DatabaseName: str, TablesToDelete: List[Any], CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_delete_table_version(
        self,
        DatabaseName: str,
        TableName: str,
        VersionIds: List[Any],
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_get_crawlers(self, CrawlerNames: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_get_dev_endpoints(self, DevEndpointNames: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_get_jobs(self, JobNames: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_get_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionsToGet: List[Any],
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_get_triggers(self, TriggerNames: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_get_workflows(
        self, Names: List[Any], IncludeGraph: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_stop_job_run(self, JobName: str, JobRunIds: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def cancel_ml_task_run(self, TransformId: str, TaskRunId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_classifier(
        self,
        GrokClassifier: Dict[str, Any] = None,
        XMLClassifier: Dict[str, Any] = None,
        JsonClassifier: Dict[str, Any] = None,
        CsvClassifier: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_connection(
        self, ConnectionInput: Dict[str, Any], CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_crawler(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_database(
        self, DatabaseInput: Dict[str, Any], CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_dev_endpoint(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_job(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_ml_transform(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionInput: Dict[str, Any],
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_script(
        self,
        DagNodes: List[Any] = None,
        DagEdges: List[Any] = None,
        Language: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_security_configuration(
        self, Name: str, EncryptionConfiguration: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_table(
        self, DatabaseName: str, TableInput: Dict[str, Any], CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_trigger(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_user_defined_function(
        self, DatabaseName: str, FunctionInput: Dict[str, Any], CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_workflow(
        self,
        Name: str,
        Description: str = None,
        DefaultRunProperties: Dict[str, Any] = None,
        Tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_classifier(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_connection(
        self, ConnectionName: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_crawler(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_database(self, Name: str, CatalogId: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_dev_endpoint(self, EndpointName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_job(self, JobName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_ml_transform(self, TransformId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionValues: List[Any],
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_resource_policy(self, PolicyHashCondition: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_security_configuration(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_table(
        self, DatabaseName: str, Name: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_table_version(
        self, DatabaseName: str, TableName: str, VersionId: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_trigger(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_user_defined_function(
        self, DatabaseName: str, FunctionName: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_workflow(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_catalog_import_status(self, CatalogId: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_classifier(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_classifiers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_connection(
        self, Name: str, CatalogId: str = None, HidePassword: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_connections(
        self,
        CatalogId: str = None,
        Filter: Dict[str, Any] = None,
        HidePassword: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_crawler(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_crawler_metrics(
        self,
        CrawlerNameList: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_crawlers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_data_catalog_encryption_settings(
        self, CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_database(self, Name: str, CatalogId: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_databases(
        self, CatalogId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_dataflow_graph(self, PythonScript: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_dev_endpoint(self, EndpointName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_dev_endpoints(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_job(self, JobName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_job_bookmark(self, JobName: str, RunId: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_job_run(
        self, JobName: str, RunId: str, PredecessorsIncluded: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_job_runs(
        self, JobName: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_jobs(self, NextToken: str = None, MaxResults: int = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_mapping(
        self,
        Source: Dict[str, Any],
        Sinks: List[Any] = None,
        Location: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_ml_task_run(self, TransformId: str, TaskRunId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_ml_task_runs(
        self,
        TransformId: str,
        NextToken: str = None,
        MaxResults: int = None,
        Filter: Dict[str, Any] = None,
        Sort: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_ml_transform(self, TransformId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_ml_transforms(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Filter: Dict[str, Any] = None,
        Sort: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionValues: List[Any],
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_partitions(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        Expression: str = None,
        NextToken: str = None,
        Segment: Dict[str, Any] = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_plan(
        self,
        Mapping: List[Any],
        Source: Dict[str, Any],
        Sinks: List[Any] = None,
        Location: Dict[str, Any] = None,
        Language: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_resource_policy(self) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_security_configuration(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_security_configurations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_table(
        self, DatabaseName: str, Name: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_table_version(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        VersionId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_table_versions(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_tables(
        self,
        DatabaseName: str,
        CatalogId: str = None,
        Expression: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_tags(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_trigger(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_triggers(
        self,
        NextToken: str = None,
        DependentJobName: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_user_defined_function(
        self, DatabaseName: str, FunctionName: str, CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_user_defined_functions(
        self,
        DatabaseName: str,
        Pattern: str,
        CatalogId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def get_workflow(self, Name: str, IncludeGraph: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_workflow_run(
        self, Name: str, RunId: str, IncludeGraph: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_workflow_run_properties(self, Name: str, RunId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_workflow_runs(
        self,
        Name: str,
        IncludeGraph: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def import_catalog_to_glue(self, CatalogId: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_crawlers(
        self, MaxResults: int = None, NextToken: str = None, Tags: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_dev_endpoints(
        self, NextToken: str = None, MaxResults: int = None, Tags: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_jobs(
        self, NextToken: str = None, MaxResults: int = None, Tags: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_triggers(
        self,
        NextToken: str = None,
        DependentJobName: str = None,
        MaxResults: int = None,
        Tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_workflows(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_data_catalog_encryption_settings(
        self, DataCatalogEncryptionSettings: Dict[str, Any], CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_resource_policy(
        self,
        PolicyInJson: str,
        PolicyHashCondition: str = None,
        PolicyExistsCondition: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_workflow_run_properties(
        self, Name: str, RunId: str, RunProperties: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def reset_job_bookmark(self, JobName: str, RunId: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def search_tables(
        self,
        CatalogId: str = None,
        NextToken: str = None,
        Filters: List[Any] = None,
        SearchText: str = None,
        SortCriteria: List[Any] = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_crawler(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_crawler_schedule(self, CrawlerName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_export_labels_task_run(
        self, TransformId: str, OutputS3Path: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_import_labels_task_run(
        self, TransformId: str, InputS3Path: str, ReplaceAllLabels: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_job_run(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def start_ml_evaluation_task_run(self, TransformId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_ml_labeling_set_generation_task_run(
        self, TransformId: str, OutputS3Path: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_trigger(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_workflow_run(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_crawler(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_crawler_schedule(self, CrawlerName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_trigger(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(
        self, ResourceArn: str, TagsToAdd: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(
        self, ResourceArn: str, TagsToRemove: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_classifier(
        self,
        GrokClassifier: Dict[str, Any] = None,
        XMLClassifier: Dict[str, Any] = None,
        JsonClassifier: Dict[str, Any] = None,
        CsvClassifier: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_connection(
        self, Name: str, ConnectionInput: Dict[str, Any], CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_crawler(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def update_crawler_schedule(
        self, CrawlerName: str, Schedule: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_database(
        self, Name: str, DatabaseInput: Dict[str, Any], CatalogId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_dev_endpoint(
        self,
        EndpointName: str,
        PublicKey: str = None,
        AddPublicKeys: List[Any] = None,
        DeletePublicKeys: List[Any] = None,
        CustomLibraries: Dict[str, Any] = None,
        UpdateEtlLibraries: bool = None,
        DeleteArguments: List[Any] = None,
        AddArguments: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_job(self, JobName: str, JobUpdate: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_ml_transform(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def update_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionValueList: List[Any],
        PartitionInput: Dict[str, Any],
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_table(
        self,
        DatabaseName: str,
        TableInput: Dict[str, Any],
        CatalogId: str = None,
        SkipArchive: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_trigger(
        self, Name: str, TriggerUpdate: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_user_defined_function(
        self,
        DatabaseName: str,
        FunctionName: str,
        FunctionInput: Dict[str, Any],
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_workflow(
        self,
        Name: str,
        Description: str = None,
        DefaultRunProperties: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

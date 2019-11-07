from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def batch_create_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionInputList: List,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def batch_delete_connection(
        self,
        ConnectionNameList: List,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def batch_delete_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionsToDelete: List,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def batch_delete_table(
        self,
        DatabaseName: str,
        TablesToDelete: List,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def batch_delete_table_version(
        self,
        DatabaseName: str,
        TableName: str,
        VersionIds: List,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def batch_get_crawlers(
        self,
        CrawlerNames: List,
    ) -> Dict:
        pass


    def batch_get_dev_endpoints(
        self,
        DevEndpointNames: List,
    ) -> Dict:
        pass


    def batch_get_jobs(
        self,
        JobNames: List,
    ) -> Dict:
        pass


    def batch_get_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionsToGet: List,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def batch_get_triggers(
        self,
        TriggerNames: List,
    ) -> Dict:
        pass


    def batch_get_workflows(
        self,
        Names: List,
        IncludeGraph: Optional[bool] = None,
    ) -> Dict:
        pass


    def batch_stop_job_run(
        self,
        JobName: str,
        JobRunIds: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def cancel_ml_task_run(
        self,
        TransformId: str,
        TaskRunId: str,
    ) -> Dict:
        pass


    def create_classifier(
        self,
        GrokClassifier: Optional[Dict] = None,
        XMLClassifier: Optional[Dict] = None,
        JsonClassifier: Optional[Dict] = None,
        CsvClassifier: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_connection(
        self,
        ConnectionInput: Dict,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_crawler(
        self,
        Name: str,
        Role: str,
        Targets: Dict,
        DatabaseName: Optional[str] = None,
        Description: Optional[str] = None,
        Schedule: Optional[str] = None,
        Classifiers: Optional[List] = None,
        TablePrefix: Optional[str] = None,
        SchemaChangePolicy: Optional[Dict] = None,
        Configuration: Optional[str] = None,
        CrawlerSecurityConfiguration: Optional[str] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_database(
        self,
        DatabaseInput: Dict,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_dev_endpoint(
        self,
        EndpointName: str,
        RoleArn: str,
        SecurityGroupIds: Optional[List] = None,
        SubnetId: Optional[str] = None,
        PublicKey: Optional[str] = None,
        PublicKeys: Optional[List] = None,
        NumberOfNodes: Optional[int] = None,
        WorkerType: Optional[str] = None,
        GlueVersion: Optional[str] = None,
        NumberOfWorkers: Optional[int] = None,
        ExtraPythonLibsS3Path: Optional[str] = None,
        ExtraJarsS3Path: Optional[str] = None,
        SecurityConfiguration: Optional[str] = None,
        Tags: Optional[Dict] = None,
        Arguments: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_job(
        self,
        Name: str,
        Role: str,
        Command: Dict,
        Description: Optional[str] = None,
        LogUri: Optional[str] = None,
        ExecutionProperty: Optional[Dict] = None,
        DefaultArguments: Optional[Dict] = None,
        Connections: Optional[Dict] = None,
        MaxRetries: Optional[int] = None,
        AllocatedCapacity: Optional[int] = None,
        Timeout: Optional[int] = None,
        MaxCapacity: Optional[float] = None,
        SecurityConfiguration: Optional[str] = None,
        Tags: Optional[Dict] = None,
        NotificationProperty: Optional[Dict] = None,
        GlueVersion: Optional[str] = None,
        NumberOfWorkers: Optional[int] = None,
        WorkerType: Optional[str] = None,
    ) -> Dict:
        pass


    def create_ml_transform(
        self,
        Name: str,
        InputRecordTables: List,
        Parameters: Dict,
        Role: str,
        Description: Optional[str] = None,
        MaxCapacity: Optional[float] = None,
        WorkerType: Optional[str] = None,
        NumberOfWorkers: Optional[int] = None,
        Timeout: Optional[int] = None,
        MaxRetries: Optional[int] = None,
    ) -> Dict:
        pass


    def create_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionInput: Dict,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_script(
        self,
        DagNodes: Optional[List] = None,
        DagEdges: Optional[List] = None,
        Language: Optional[str] = None,
    ) -> Dict:
        pass


    def create_security_configuration(
        self,
        Name: str,
        EncryptionConfiguration: Dict,
    ) -> Dict:
        pass


    def create_table(
        self,
        DatabaseName: str,
        TableInput: Dict,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_trigger(
        self,
        Name: str,
        Type: str,
        Actions: List,
        WorkflowName: Optional[str] = None,
        Schedule: Optional[str] = None,
        Predicate: Optional[Dict] = None,
        Description: Optional[str] = None,
        StartOnCreation: Optional[bool] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_user_defined_function(
        self,
        DatabaseName: str,
        FunctionInput: Dict,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_workflow(
        self,
        Name: str,
        Description: Optional[str] = None,
        DefaultRunProperties: Optional[Dict] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_classifier(
        self,
        Name: str,
    ) -> Dict:
        pass


    def delete_connection(
        self,
        ConnectionName: str,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_crawler(
        self,
        Name: str,
    ) -> Dict:
        pass


    def delete_database(
        self,
        Name: str,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_dev_endpoint(
        self,
        EndpointName: str,
    ) -> Dict:
        pass


    def delete_job(
        self,
        JobName: str,
    ) -> Dict:
        pass


    def delete_ml_transform(
        self,
        TransformId: str,
    ) -> Dict:
        pass


    def delete_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionValues: List,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_resource_policy(
        self,
        PolicyHashCondition: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_security_configuration(
        self,
        Name: str,
    ) -> Dict:
        pass


    def delete_table(
        self,
        DatabaseName: str,
        Name: str,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_table_version(
        self,
        DatabaseName: str,
        TableName: str,
        VersionId: str,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_trigger(
        self,
        Name: str,
    ) -> Dict:
        pass


    def delete_user_defined_function(
        self,
        DatabaseName: str,
        FunctionName: str,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_workflow(
        self,
        Name: str,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_catalog_import_status(
        self,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_classifier(
        self,
        Name: str,
    ) -> Dict:
        pass


    def get_classifiers(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_connection(
        self,
        Name: str,
        CatalogId: Optional[str] = None,
        HidePassword: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_connections(
        self,
        CatalogId: Optional[str] = None,
        Filter: Optional[Dict] = None,
        HidePassword: Optional[bool] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_crawler(
        self,
        Name: str,
    ) -> Dict:
        pass


    def get_crawler_metrics(
        self,
        CrawlerNameList: Optional[List] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_crawlers(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_data_catalog_encryption_settings(
        self,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_database(
        self,
        Name: str,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_databases(
        self,
        CatalogId: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_dataflow_graph(
        self,
        PythonScript: Optional[str] = None,
    ) -> Dict:
        pass


    def get_dev_endpoint(
        self,
        EndpointName: str,
    ) -> Dict:
        pass


    def get_dev_endpoints(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_job(
        self,
        JobName: str,
    ) -> Dict:
        pass


    def get_job_bookmark(
        self,
        JobName: str,
        RunId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_job_run(
        self,
        JobName: str,
        RunId: str,
        PredecessorsIncluded: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_job_runs(
        self,
        JobName: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_jobs(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_mapping(
        self,
        Source: Dict,
        Sinks: Optional[List] = None,
        Location: Optional[Dict] = None,
    ) -> Dict:
        pass


    def get_ml_task_run(
        self,
        TransformId: str,
        TaskRunId: str,
    ) -> Dict:
        pass


    def get_ml_task_runs(
        self,
        TransformId: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Filter: Optional[Dict] = None,
        Sort: Optional[Dict] = None,
    ) -> Dict:
        pass


    def get_ml_transform(
        self,
        TransformId: str,
    ) -> Dict:
        pass


    def get_ml_transforms(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Filter: Optional[Dict] = None,
        Sort: Optional[Dict] = None,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionValues: List,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_partitions(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: Optional[str] = None,
        Expression: Optional[str] = None,
        NextToken: Optional[str] = None,
        Segment: Optional[Dict] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_plan(
        self,
        Mapping: List,
        Source: Dict,
        Sinks: Optional[List] = None,
        Location: Optional[Dict] = None,
        Language: Optional[str] = None,
    ) -> Dict:
        pass


    def get_resource_policy(
        self,
    ) -> Dict:
        pass


    def get_security_configuration(
        self,
        Name: str,
    ) -> Dict:
        pass


    def get_security_configurations(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def get_table(
        self,
        DatabaseName: str,
        Name: str,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_table_version(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: Optional[str] = None,
        VersionId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_table_versions(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_tables(
        self,
        DatabaseName: str,
        CatalogId: Optional[str] = None,
        Expression: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_tags(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def get_trigger(
        self,
        Name: str,
    ) -> Dict:
        pass


    def get_triggers(
        self,
        NextToken: Optional[str] = None,
        DependentJobName: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_user_defined_function(
        self,
        DatabaseName: str,
        FunctionName: str,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_user_defined_functions(
        self,
        DatabaseName: str,
        Pattern: str,
        CatalogId: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def get_workflow(
        self,
        Name: str,
        IncludeGraph: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_workflow_run(
        self,
        Name: str,
        RunId: str,
        IncludeGraph: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_workflow_run_properties(
        self,
        Name: str,
        RunId: str,
    ) -> Dict:
        pass


    def get_workflow_runs(
        self,
        Name: str,
        IncludeGraph: Optional[bool] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def import_catalog_to_glue(
        self,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def list_crawlers(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def list_dev_endpoints(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def list_jobs(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def list_triggers(
        self,
        NextToken: Optional[str] = None,
        DependentJobName: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def list_workflows(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def put_data_catalog_encryption_settings(
        self,
        DataCatalogEncryptionSettings: Dict,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def put_resource_policy(
        self,
        PolicyInJson: str,
        PolicyHashCondition: Optional[str] = None,
        PolicyExistsCondition: Optional[str] = None,
    ) -> Dict:
        pass


    def put_workflow_run_properties(
        self,
        Name: str,
        RunId: str,
        RunProperties: Dict,
    ) -> Dict:
        pass


    def reset_job_bookmark(
        self,
        JobName: str,
        RunId: Optional[str] = None,
    ) -> Dict:
        pass


    def search_tables(
        self,
        CatalogId: Optional[str] = None,
        NextToken: Optional[str] = None,
        Filters: Optional[List] = None,
        SearchText: Optional[str] = None,
        SortCriteria: Optional[List] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def start_crawler(
        self,
        Name: str,
    ) -> Dict:
        pass


    def start_crawler_schedule(
        self,
        CrawlerName: str,
    ) -> Dict:
        pass


    def start_export_labels_task_run(
        self,
        TransformId: str,
        OutputS3Path: str,
    ) -> Dict:
        pass


    def start_import_labels_task_run(
        self,
        TransformId: str,
        InputS3Path: str,
        ReplaceAllLabels: Optional[bool] = None,
    ) -> Dict:
        pass


    def start_job_run(
        self,
        JobName: str,
        JobRunId: Optional[str] = None,
        Arguments: Optional[Dict] = None,
        AllocatedCapacity: Optional[int] = None,
        Timeout: Optional[int] = None,
        MaxCapacity: Optional[float] = None,
        SecurityConfiguration: Optional[str] = None,
        NotificationProperty: Optional[Dict] = None,
        WorkerType: Optional[str] = None,
        NumberOfWorkers: Optional[int] = None,
    ) -> Dict:
        pass


    def start_ml_evaluation_task_run(
        self,
        TransformId: str,
    ) -> Dict:
        pass


    def start_ml_labeling_set_generation_task_run(
        self,
        TransformId: str,
        OutputS3Path: str,
    ) -> Dict:
        pass


    def start_trigger(
        self,
        Name: str,
    ) -> Dict:
        pass


    def start_workflow_run(
        self,
        Name: str,
    ) -> Dict:
        pass


    def stop_crawler(
        self,
        Name: str,
    ) -> Dict:
        pass


    def stop_crawler_schedule(
        self,
        CrawlerName: str,
    ) -> Dict:
        pass


    def stop_trigger(
        self,
        Name: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        TagsToAdd: Dict,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagsToRemove: List,
    ) -> Dict:
        pass


    def update_classifier(
        self,
        GrokClassifier: Optional[Dict] = None,
        XMLClassifier: Optional[Dict] = None,
        JsonClassifier: Optional[Dict] = None,
        CsvClassifier: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_connection(
        self,
        Name: str,
        ConnectionInput: Dict,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def update_crawler(
        self,
        Name: str,
        Role: Optional[str] = None,
        DatabaseName: Optional[str] = None,
        Description: Optional[str] = None,
        Targets: Optional[Dict] = None,
        Schedule: Optional[str] = None,
        Classifiers: Optional[List] = None,
        TablePrefix: Optional[str] = None,
        SchemaChangePolicy: Optional[Dict] = None,
        Configuration: Optional[str] = None,
        CrawlerSecurityConfiguration: Optional[str] = None,
    ) -> Dict:
        pass


    def update_crawler_schedule(
        self,
        CrawlerName: str,
        Schedule: Optional[str] = None,
    ) -> Dict:
        pass


    def update_database(
        self,
        Name: str,
        DatabaseInput: Dict,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def update_dev_endpoint(
        self,
        EndpointName: str,
        PublicKey: Optional[str] = None,
        AddPublicKeys: Optional[List] = None,
        DeletePublicKeys: Optional[List] = None,
        CustomLibraries: Optional[Dict] = None,
        UpdateEtlLibraries: Optional[bool] = None,
        DeleteArguments: Optional[List] = None,
        AddArguments: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_job(
        self,
        JobName: str,
        JobUpdate: Dict,
    ) -> Dict:
        pass


    def update_ml_transform(
        self,
        TransformId: str,
        Name: Optional[str] = None,
        Description: Optional[str] = None,
        Parameters: Optional[Dict] = None,
        Role: Optional[str] = None,
        MaxCapacity: Optional[float] = None,
        WorkerType: Optional[str] = None,
        NumberOfWorkers: Optional[int] = None,
        Timeout: Optional[int] = None,
        MaxRetries: Optional[int] = None,
    ) -> Dict:
        pass


    def update_partition(
        self,
        DatabaseName: str,
        TableName: str,
        PartitionValueList: List,
        PartitionInput: Dict,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def update_table(
        self,
        DatabaseName: str,
        TableInput: Dict,
        CatalogId: Optional[str] = None,
        SkipArchive: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_trigger(
        self,
        Name: str,
        TriggerUpdate: Dict,
    ) -> Dict:
        pass


    def update_user_defined_function(
        self,
        DatabaseName: str,
        FunctionName: str,
        FunctionInput: Dict,
        CatalogId: Optional[str] = None,
    ) -> Dict:
        pass


    def update_workflow(
        self,
        Name: str,
        Description: Optional[str] = None,
        DefaultRunProperties: Optional[Dict] = None,
    ) -> Dict:
        pass


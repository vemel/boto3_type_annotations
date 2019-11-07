from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_tags(
        self,
        ResourceArn: str,
        Tags: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_algorithm(
        self,
        AlgorithmName: str,
        TrainingSpecification: Dict,
        AlgorithmDescription: Optional[str] = None,
        InferenceSpecification: Optional[Dict] = None,
        ValidationSpecification: Optional[Dict] = None,
        CertifyForMarketplace: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_code_repository(
        self,
        CodeRepositoryName: str,
        GitConfig: Dict,
    ) -> Dict:
        pass


    def create_compilation_job(
        self,
        CompilationJobName: str,
        RoleArn: str,
        InputConfig: Dict,
        OutputConfig: Dict,
        StoppingCondition: Dict,
    ) -> Dict:
        pass


    def create_endpoint(
        self,
        EndpointName: str,
        EndpointConfigName: str,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_endpoint_config(
        self,
        EndpointConfigName: str,
        ProductionVariants: List,
        Tags: Optional[List] = None,
        KmsKeyId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_hyper_parameter_tuning_job(
        self,
        HyperParameterTuningJobName: str,
        HyperParameterTuningJobConfig: Dict,
        TrainingJobDefinition: Optional[Dict] = None,
        WarmStartConfig: Optional[Dict] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_labeling_job(
        self,
        LabelingJobName: str,
        LabelAttributeName: str,
        InputConfig: Dict,
        OutputConfig: Dict,
        RoleArn: str,
        HumanTaskConfig: Dict,
        LabelCategoryConfigS3Uri: Optional[str] = None,
        StoppingConditions: Optional[Dict] = None,
        LabelingJobAlgorithmsConfig: Optional[Dict] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_model(
        self,
        ModelName: str,
        ExecutionRoleArn: str,
        PrimaryContainer: Optional[Dict] = None,
        Containers: Optional[List] = None,
        Tags: Optional[List] = None,
        VpcConfig: Optional[Dict] = None,
        EnableNetworkIsolation: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_model_package(
        self,
        ModelPackageName: str,
        ModelPackageDescription: Optional[str] = None,
        InferenceSpecification: Optional[Dict] = None,
        ValidationSpecification: Optional[Dict] = None,
        SourceAlgorithmSpecification: Optional[Dict] = None,
        CertifyForMarketplace: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_notebook_instance(
        self,
        NotebookInstanceName: str,
        InstanceType: str,
        RoleArn: str,
        SubnetId: Optional[str] = None,
        SecurityGroupIds: Optional[List] = None,
        KmsKeyId: Optional[str] = None,
        Tags: Optional[List] = None,
        LifecycleConfigName: Optional[str] = None,
        DirectInternetAccess: Optional[str] = None,
        VolumeSizeInGB: Optional[int] = None,
        AcceleratorTypes: Optional[List] = None,
        DefaultCodeRepository: Optional[str] = None,
        AdditionalCodeRepositories: Optional[List] = None,
        RootAccess: Optional[str] = None,
    ) -> Dict:
        pass


    def create_notebook_instance_lifecycle_config(
        self,
        NotebookInstanceLifecycleConfigName: str,
        OnCreate: Optional[List] = None,
        OnStart: Optional[List] = None,
    ) -> Dict:
        pass


    def create_presigned_notebook_instance_url(
        self,
        NotebookInstanceName: str,
        SessionExpirationDurationInSeconds: Optional[int] = None,
    ) -> Dict:
        pass


    def create_training_job(
        self,
        TrainingJobName: str,
        AlgorithmSpecification: Dict,
        RoleArn: str,
        OutputDataConfig: Dict,
        ResourceConfig: Dict,
        StoppingCondition: Dict,
        HyperParameters: Optional[Dict] = None,
        InputDataConfig: Optional[List] = None,
        VpcConfig: Optional[Dict] = None,
        Tags: Optional[List] = None,
        EnableNetworkIsolation: Optional[bool] = None,
        EnableInterContainerTrafficEncryption: Optional[bool] = None,
        EnableManagedSpotTraining: Optional[bool] = None,
        CheckpointConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_transform_job(
        self,
        TransformJobName: str,
        ModelName: str,
        TransformInput: Dict,
        TransformOutput: Dict,
        TransformResources: Dict,
        MaxConcurrentTransforms: Optional[int] = None,
        MaxPayloadInMB: Optional[int] = None,
        BatchStrategy: Optional[str] = None,
        Environment: Optional[Dict] = None,
        DataProcessing: Optional[Dict] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_workteam(
        self,
        WorkteamName: str,
        MemberDefinitions: List,
        Description: str,
        NotificationConfiguration: Optional[Dict] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_algorithm(
        self,
        AlgorithmName: str,
    ):
        pass


    def delete_code_repository(
        self,
        CodeRepositoryName: str,
    ):
        pass


    def delete_endpoint(
        self,
        EndpointName: str,
    ):
        pass


    def delete_endpoint_config(
        self,
        EndpointConfigName: str,
    ):
        pass


    def delete_model(
        self,
        ModelName: str,
    ):
        pass


    def delete_model_package(
        self,
        ModelPackageName: str,
    ):
        pass


    def delete_notebook_instance(
        self,
        NotebookInstanceName: str,
    ):
        pass


    def delete_notebook_instance_lifecycle_config(
        self,
        NotebookInstanceLifecycleConfigName: str,
    ):
        pass


    def delete_tags(
        self,
        ResourceArn: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def delete_workteam(
        self,
        WorkteamName: str,
    ) -> Dict:
        pass


    def describe_algorithm(
        self,
        AlgorithmName: str,
    ) -> Dict:
        pass


    def describe_code_repository(
        self,
        CodeRepositoryName: str,
    ) -> Dict:
        pass


    def describe_compilation_job(
        self,
        CompilationJobName: str,
    ) -> Dict:
        pass


    def describe_endpoint(
        self,
        EndpointName: str,
    ) -> Dict:
        pass


    def describe_endpoint_config(
        self,
        EndpointConfigName: str,
    ) -> Dict:
        pass


    def describe_hyper_parameter_tuning_job(
        self,
        HyperParameterTuningJobName: str,
    ) -> Dict:
        pass


    def describe_labeling_job(
        self,
        LabelingJobName: str,
    ) -> Dict:
        pass


    def describe_model(
        self,
        ModelName: str,
    ) -> Dict:
        pass


    def describe_model_package(
        self,
        ModelPackageName: str,
    ) -> Dict:
        pass


    def describe_notebook_instance(
        self,
        NotebookInstanceName: str,
    ) -> Dict:
        pass


    def describe_notebook_instance_lifecycle_config(
        self,
        NotebookInstanceLifecycleConfigName: str,
    ) -> Dict:
        pass


    def describe_subscribed_workteam(
        self,
        WorkteamArn: str,
    ) -> Dict:
        pass


    def describe_training_job(
        self,
        TrainingJobName: str,
    ) -> Dict:
        pass


    def describe_transform_job(
        self,
        TransformJobName: str,
    ) -> Dict:
        pass


    def describe_workteam(
        self,
        WorkteamName: str,
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


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_search_suggestions(
        self,
        Resource: str,
        SuggestionQuery: Optional[Dict] = None,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_algorithms(
        self,
        CreationTimeAfter: Optional[datetime] = None,
        CreationTimeBefore: Optional[datetime] = None,
        MaxResults: Optional[int] = None,
        NameContains: Optional[str] = None,
        NextToken: Optional[str] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
    ) -> Dict:
        pass


    def list_code_repositories(
        self,
        CreationTimeAfter: Optional[datetime] = None,
        CreationTimeBefore: Optional[datetime] = None,
        LastModifiedTimeAfter: Optional[datetime] = None,
        LastModifiedTimeBefore: Optional[datetime] = None,
        MaxResults: Optional[int] = None,
        NameContains: Optional[str] = None,
        NextToken: Optional[str] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
    ) -> Dict:
        pass


    def list_compilation_jobs(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        CreationTimeAfter: Optional[datetime] = None,
        CreationTimeBefore: Optional[datetime] = None,
        LastModifiedTimeAfter: Optional[datetime] = None,
        LastModifiedTimeBefore: Optional[datetime] = None,
        NameContains: Optional[str] = None,
        StatusEquals: Optional[str] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
    ) -> Dict:
        pass


    def list_endpoint_configs(
        self,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NameContains: Optional[str] = None,
        CreationTimeBefore: Optional[datetime] = None,
        CreationTimeAfter: Optional[datetime] = None,
    ) -> Dict:
        pass


    def list_endpoints(
        self,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NameContains: Optional[str] = None,
        CreationTimeBefore: Optional[datetime] = None,
        CreationTimeAfter: Optional[datetime] = None,
        LastModifiedTimeBefore: Optional[datetime] = None,
        LastModifiedTimeAfter: Optional[datetime] = None,
        StatusEquals: Optional[str] = None,
    ) -> Dict:
        pass


    def list_hyper_parameter_tuning_jobs(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NameContains: Optional[str] = None,
        CreationTimeAfter: Optional[datetime] = None,
        CreationTimeBefore: Optional[datetime] = None,
        LastModifiedTimeAfter: Optional[datetime] = None,
        LastModifiedTimeBefore: Optional[datetime] = None,
        StatusEquals: Optional[str] = None,
    ) -> Dict:
        pass


    def list_labeling_jobs(
        self,
        CreationTimeAfter: Optional[datetime] = None,
        CreationTimeBefore: Optional[datetime] = None,
        LastModifiedTimeAfter: Optional[datetime] = None,
        LastModifiedTimeBefore: Optional[datetime] = None,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        NameContains: Optional[str] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        StatusEquals: Optional[str] = None,
    ) -> Dict:
        pass


    def list_labeling_jobs_for_workteam(
        self,
        WorkteamArn: str,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        CreationTimeAfter: Optional[datetime] = None,
        CreationTimeBefore: Optional[datetime] = None,
        JobReferenceCodeContains: Optional[str] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
    ) -> Dict:
        pass


    def list_model_packages(
        self,
        CreationTimeAfter: Optional[datetime] = None,
        CreationTimeBefore: Optional[datetime] = None,
        MaxResults: Optional[int] = None,
        NameContains: Optional[str] = None,
        NextToken: Optional[str] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
    ) -> Dict:
        pass


    def list_models(
        self,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        NameContains: Optional[str] = None,
        CreationTimeBefore: Optional[datetime] = None,
        CreationTimeAfter: Optional[datetime] = None,
    ) -> Dict:
        pass


    def list_notebook_instance_lifecycle_configs(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NameContains: Optional[str] = None,
        CreationTimeBefore: Optional[datetime] = None,
        CreationTimeAfter: Optional[datetime] = None,
        LastModifiedTimeBefore: Optional[datetime] = None,
        LastModifiedTimeAfter: Optional[datetime] = None,
    ) -> Dict:
        pass


    def list_notebook_instances(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NameContains: Optional[str] = None,
        CreationTimeBefore: Optional[datetime] = None,
        CreationTimeAfter: Optional[datetime] = None,
        LastModifiedTimeBefore: Optional[datetime] = None,
        LastModifiedTimeAfter: Optional[datetime] = None,
        StatusEquals: Optional[str] = None,
        NotebookInstanceLifecycleConfigNameContains: Optional[str] = None,
        DefaultCodeRepositoryContains: Optional[str] = None,
        AdditionalCodeRepositoryEquals: Optional[str] = None,
    ) -> Dict:
        pass


    def list_subscribed_workteams(
        self,
        NameContains: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags(
        self,
        ResourceArn: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_training_jobs(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        CreationTimeAfter: Optional[datetime] = None,
        CreationTimeBefore: Optional[datetime] = None,
        LastModifiedTimeAfter: Optional[datetime] = None,
        LastModifiedTimeBefore: Optional[datetime] = None,
        NameContains: Optional[str] = None,
        StatusEquals: Optional[str] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
    ) -> Dict:
        pass


    def list_training_jobs_for_hyper_parameter_tuning_job(
        self,
        HyperParameterTuningJobName: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        StatusEquals: Optional[str] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
    ) -> Dict:
        pass


    def list_transform_jobs(
        self,
        CreationTimeAfter: Optional[datetime] = None,
        CreationTimeBefore: Optional[datetime] = None,
        LastModifiedTimeAfter: Optional[datetime] = None,
        LastModifiedTimeBefore: Optional[datetime] = None,
        NameContains: Optional[str] = None,
        StatusEquals: Optional[str] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_workteams(
        self,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NameContains: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def render_ui_template(
        self,
        UiTemplate: Dict,
        Task: Dict,
        RoleArn: str,
    ) -> Dict:
        pass


    def search(
        self,
        Resource: str,
        SearchExpression: Optional[Dict] = None,
        SortBy: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def start_notebook_instance(
        self,
        NotebookInstanceName: str,
    ):
        pass


    def stop_compilation_job(
        self,
        CompilationJobName: str,
    ):
        pass


    def stop_hyper_parameter_tuning_job(
        self,
        HyperParameterTuningJobName: str,
    ):
        pass


    def stop_labeling_job(
        self,
        LabelingJobName: str,
    ):
        pass


    def stop_notebook_instance(
        self,
        NotebookInstanceName: str,
    ):
        pass


    def stop_training_job(
        self,
        TrainingJobName: str,
    ):
        pass


    def stop_transform_job(
        self,
        TransformJobName: str,
    ):
        pass


    def update_code_repository(
        self,
        CodeRepositoryName: str,
        GitConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_endpoint(
        self,
        EndpointName: str,
        EndpointConfigName: str,
    ) -> Dict:
        pass


    def update_endpoint_weights_and_capacities(
        self,
        EndpointName: str,
        DesiredWeightsAndCapacities: List,
    ) -> Dict:
        pass


    def update_notebook_instance(
        self,
        NotebookInstanceName: str,
        InstanceType: Optional[str] = None,
        RoleArn: Optional[str] = None,
        LifecycleConfigName: Optional[str] = None,
        DisassociateLifecycleConfig: Optional[bool] = None,
        VolumeSizeInGB: Optional[int] = None,
        DefaultCodeRepository: Optional[str] = None,
        AdditionalCodeRepositories: Optional[List] = None,
        AcceleratorTypes: Optional[List] = None,
        DisassociateAcceleratorTypes: Optional[bool] = None,
        DisassociateDefaultCodeRepository: Optional[bool] = None,
        DisassociateAdditionalCodeRepositories: Optional[bool] = None,
        RootAccess: Optional[str] = None,
    ) -> Dict:
        pass


    def update_notebook_instance_lifecycle_config(
        self,
        NotebookInstanceLifecycleConfigName: str,
        OnCreate: Optional[List] = None,
        OnStart: Optional[List] = None,
    ) -> Dict:
        pass


    def update_workteam(
        self,
        WorkteamName: str,
        MemberDefinitions: Optional[List] = None,
        Description: Optional[str] = None,
        NotificationConfiguration: Optional[Dict] = None,
    ) -> Dict:
        pass


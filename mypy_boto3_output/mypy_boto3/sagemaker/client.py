from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def add_tags(self, ResourceArn: str, Tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_algorithm(
        self,
        AlgorithmName: str,
        TrainingSpecification: Dict[str, Any],
        AlgorithmDescription: str = None,
        InferenceSpecification: Dict[str, Any] = None,
        ValidationSpecification: Dict[str, Any] = None,
        CertifyForMarketplace: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_code_repository(
        self, CodeRepositoryName: str, GitConfig: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_compilation_job(
        self,
        CompilationJobName: str,
        RoleArn: str,
        InputConfig: Dict[str, Any],
        OutputConfig: Dict[str, Any],
        StoppingCondition: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_endpoint(
        self, EndpointName: str, EndpointConfigName: str, Tags: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_endpoint_config(
        self,
        EndpointConfigName: str,
        ProductionVariants: List[Any],
        Tags: List[Any] = None,
        KmsKeyId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_hyper_parameter_tuning_job(
        self,
        HyperParameterTuningJobName: str,
        HyperParameterTuningJobConfig: Dict[str, Any],
        TrainingJobDefinition: Dict[str, Any] = None,
        WarmStartConfig: Dict[str, Any] = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_labeling_job(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_model(
        self,
        ModelName: str,
        ExecutionRoleArn: str,
        PrimaryContainer: Dict[str, Any] = None,
        Containers: List[Any] = None,
        Tags: List[Any] = None,
        VpcConfig: Dict[str, Any] = None,
        EnableNetworkIsolation: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_model_package(
        self,
        ModelPackageName: str,
        ModelPackageDescription: str = None,
        InferenceSpecification: Dict[str, Any] = None,
        ValidationSpecification: Dict[str, Any] = None,
        SourceAlgorithmSpecification: Dict[str, Any] = None,
        CertifyForMarketplace: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_notebook_instance(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_notebook_instance_lifecycle_config(
        self,
        NotebookInstanceLifecycleConfigName: str,
        OnCreate: List[Any] = None,
        OnStart: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_presigned_notebook_instance_url(
        self, NotebookInstanceName: str, SessionExpirationDurationInSeconds: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_training_job(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_transform_job(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def create_workteam(
        self,
        WorkteamName: str,
        MemberDefinitions: List[Any],
        Description: str,
        NotificationConfiguration: Dict[str, Any] = None,
        Tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_algorithm(self, AlgorithmName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_code_repository(self, CodeRepositoryName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_endpoint(self, EndpointName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_endpoint_config(self, EndpointConfigName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_model(self, ModelName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_model_package(self, ModelPackageName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_notebook_instance(self, NotebookInstanceName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_notebook_instance_lifecycle_config(
        self, NotebookInstanceLifecycleConfigName: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_tags(self, ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_workteam(self, WorkteamName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_algorithm(self, AlgorithmName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_code_repository(self, CodeRepositoryName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_compilation_job(self, CompilationJobName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_endpoint(self, EndpointName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_endpoint_config(self, EndpointConfigName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_hyper_parameter_tuning_job(
        self, HyperParameterTuningJobName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_labeling_job(self, LabelingJobName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_model(self, ModelName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_model_package(self, ModelPackageName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_notebook_instance(self, NotebookInstanceName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_notebook_instance_lifecycle_config(
        self, NotebookInstanceLifecycleConfigName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_subscribed_workteam(self, WorkteamArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_training_job(self, TrainingJobName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_transform_job(self, TransformJobName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_workteam(self, WorkteamName: str) -> Dict[str, Any]:
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
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_search_suggestions(
        self, Resource: str, SuggestionQuery: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_algorithms(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: str = None,
        SortOrder: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_code_repositories(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def list_compilation_jobs(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def list_endpoint_configs(
        self,
        SortBy: str = None,
        SortOrder: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_endpoints(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def list_hyper_parameter_tuning_jobs(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def list_labeling_jobs(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def list_labeling_jobs_for_workteam(
        self,
        WorkteamArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        JobReferenceCodeContains: str = None,
        SortBy: str = None,
        SortOrder: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_model_packages(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: str = None,
        SortOrder: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_models(
        self,
        SortBy: str = None,
        SortOrder: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_notebook_instance_lifecycle_configs(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def list_notebook_instances(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def list_subscribed_workteams(
        self, NameContains: str = None, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags(
        self, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_training_jobs(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def list_training_jobs_for_hyper_parameter_tuning_job(
        self,
        HyperParameterTuningJobName: str,
        NextToken: str = None,
        MaxResults: int = None,
        StatusEquals: str = None,
        SortBy: str = None,
        SortOrder: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_transform_jobs(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def list_workteams(
        self,
        SortBy: str = None,
        SortOrder: str = None,
        NameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def render_ui_template(
        self, UiTemplate: Dict[str, Any], Task: Dict[str, Any], RoleArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def search(
        self,
        Resource: str,
        SearchExpression: Dict[str, Any] = None,
        SortBy: str = None,
        SortOrder: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_notebook_instance(self, NotebookInstanceName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def stop_compilation_job(self, CompilationJobName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def stop_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def stop_labeling_job(self, LabelingJobName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def stop_notebook_instance(self, NotebookInstanceName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def stop_training_job(self, TrainingJobName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def stop_transform_job(self, TransformJobName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_code_repository(
        self, CodeRepositoryName: str, GitConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_endpoint(
        self, EndpointName: str, EndpointConfigName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_endpoint_weights_and_capacities(
        self, EndpointName: str, DesiredWeightsAndCapacities: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_notebook_instance(
        self,
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
        pass

    # pylint: disable=arguments-differ
    def update_notebook_instance_lifecycle_config(
        self,
        NotebookInstanceLifecycleConfigName: str,
        OnCreate: List[Any] = None,
        OnStart: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_workteam(
        self,
        WorkteamName: str,
        MemberDefinitions: List[Any] = None,
        Description: str = None,
        NotificationConfiguration: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_tags_to_on_premises_instances(
        self,
        tags: List,
        instanceNames: List,
    ):
        pass


    def batch_get_application_revisions(
        self,
        applicationName: str,
        revisions: List,
    ) -> Dict:
        pass


    def batch_get_applications(
        self,
        applicationNames: List,
    ) -> Dict:
        pass


    def batch_get_deployment_groups(
        self,
        applicationName: str,
        deploymentGroupNames: List,
    ) -> Dict:
        pass


    def batch_get_deployment_instances(
        self,
        deploymentId: str,
        instanceIds: List,
    ) -> Dict:
        pass


    def batch_get_deployment_targets(
        self,
        deploymentId: Optional[str] = None,
        targetIds: Optional[List] = None,
    ) -> Dict:
        pass


    def batch_get_deployments(
        self,
        deploymentIds: List,
    ) -> Dict:
        pass


    def batch_get_on_premises_instances(
        self,
        instanceNames: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def continue_deployment(
        self,
        deploymentId: Optional[str] = None,
        deploymentWaitType: Optional[str] = None,
    ):
        pass


    def create_application(
        self,
        applicationName: str,
        computePlatform: Optional[str] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_deployment(
        self,
        applicationName: str,
        deploymentGroupName: Optional[str] = None,
        revision: Optional[Dict] = None,
        deploymentConfigName: Optional[str] = None,
        description: Optional[str] = None,
        ignoreApplicationStopFailures: Optional[bool] = None,
        targetInstances: Optional[Dict] = None,
        autoRollbackConfiguration: Optional[Dict] = None,
        updateOutdatedInstancesOnly: Optional[bool] = None,
        fileExistsBehavior: Optional[str] = None,
    ) -> Dict:
        pass


    def create_deployment_config(
        self,
        deploymentConfigName: str,
        minimumHealthyHosts: Optional[Dict] = None,
        trafficRoutingConfig: Optional[Dict] = None,
        computePlatform: Optional[str] = None,
    ) -> Dict:
        pass


    def create_deployment_group(
        self,
        applicationName: str,
        deploymentGroupName: str,
        serviceRoleArn: str,
        deploymentConfigName: Optional[str] = None,
        ec2TagFilters: Optional[List] = None,
        onPremisesInstanceTagFilters: Optional[List] = None,
        autoScalingGroups: Optional[List] = None,
        triggerConfigurations: Optional[List] = None,
        alarmConfiguration: Optional[Dict] = None,
        autoRollbackConfiguration: Optional[Dict] = None,
        deploymentStyle: Optional[Dict] = None,
        blueGreenDeploymentConfiguration: Optional[Dict] = None,
        loadBalancerInfo: Optional[Dict] = None,
        ec2TagSet: Optional[Dict] = None,
        ecsServices: Optional[List] = None,
        onPremisesTagSet: Optional[Dict] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def delete_application(
        self,
        applicationName: str,
    ):
        pass


    def delete_deployment_config(
        self,
        deploymentConfigName: str,
    ):
        pass


    def delete_deployment_group(
        self,
        applicationName: str,
        deploymentGroupName: str,
    ) -> Dict:
        pass


    def delete_git_hub_account_token(
        self,
        tokenName: Optional[str] = None,
    ) -> Dict:
        pass


    def deregister_on_premises_instance(
        self,
        instanceName: str,
    ):
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_application(
        self,
        applicationName: str,
    ) -> Dict:
        pass


    def get_application_revision(
        self,
        applicationName: str,
        revision: Dict,
    ) -> Dict:
        pass


    def get_deployment(
        self,
        deploymentId: str,
    ) -> Dict:
        pass


    def get_deployment_config(
        self,
        deploymentConfigName: str,
    ) -> Dict:
        pass


    def get_deployment_group(
        self,
        applicationName: str,
        deploymentGroupName: str,
    ) -> Dict:
        pass


    def get_deployment_instance(
        self,
        deploymentId: str,
        instanceId: str,
    ) -> Dict:
        pass


    def get_deployment_target(
        self,
        deploymentId: Optional[str] = None,
        targetId: Optional[str] = None,
    ) -> Dict:
        pass


    def get_on_premises_instance(
        self,
        instanceName: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_application_revisions(
        self,
        applicationName: str,
        sortBy: Optional[str] = None,
        sortOrder: Optional[str] = None,
        s3Bucket: Optional[str] = None,
        s3KeyPrefix: Optional[str] = None,
        deployed: Optional[str] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_applications(
        self,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_deployment_configs(
        self,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_deployment_groups(
        self,
        applicationName: str,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_deployment_instances(
        self,
        deploymentId: str,
        nextToken: Optional[str] = None,
        instanceStatusFilter: Optional[List] = None,
        instanceTypeFilter: Optional[List] = None,
    ) -> Dict:
        pass


    def list_deployment_targets(
        self,
        deploymentId: Optional[str] = None,
        nextToken: Optional[str] = None,
        targetFilters: Optional[Dict] = None,
    ) -> Dict:
        pass


    def list_deployments(
        self,
        applicationName: Optional[str] = None,
        deploymentGroupName: Optional[str] = None,
        includeOnlyStatuses: Optional[List] = None,
        createTimeRange: Optional[Dict] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_git_hub_account_token_names(
        self,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_on_premises_instances(
        self,
        registrationStatus: Optional[str] = None,
        tagFilters: Optional[List] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def put_lifecycle_event_hook_execution_status(
        self,
        deploymentId: Optional[str] = None,
        lifecycleEventHookExecutionId: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Dict:
        pass


    def register_application_revision(
        self,
        applicationName: str,
        revision: Dict,
        description: Optional[str] = None,
    ):
        pass


    def register_on_premises_instance(
        self,
        instanceName: str,
        iamSessionArn: Optional[str] = None,
        iamUserArn: Optional[str] = None,
    ):
        pass


    def remove_tags_from_on_premises_instances(
        self,
        tags: List,
        instanceNames: List,
    ):
        pass


    def skip_wait_time_for_instance_termination(
        self,
        deploymentId: Optional[str] = None,
    ):
        pass


    def stop_deployment(
        self,
        deploymentId: str,
        autoRollbackEnabled: Optional[bool] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        Tags: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeys: List,
    ) -> Dict:
        pass


    def update_application(
        self,
        applicationName: Optional[str] = None,
        newApplicationName: Optional[str] = None,
    ):
        pass


    def update_deployment_group(
        self,
        applicationName: str,
        currentDeploymentGroupName: str,
        newDeploymentGroupName: Optional[str] = None,
        deploymentConfigName: Optional[str] = None,
        ec2TagFilters: Optional[List] = None,
        onPremisesInstanceTagFilters: Optional[List] = None,
        autoScalingGroups: Optional[List] = None,
        serviceRoleArn: Optional[str] = None,
        triggerConfigurations: Optional[List] = None,
        alarmConfiguration: Optional[Dict] = None,
        autoRollbackConfiguration: Optional[Dict] = None,
        deploymentStyle: Optional[Dict] = None,
        blueGreenDeploymentConfiguration: Optional[Dict] = None,
        loadBalancerInfo: Optional[Dict] = None,
        ec2TagSet: Optional[Dict] = None,
        ecsServices: Optional[List] = None,
        onPremisesTagSet: Optional[Dict] = None,
    ) -> Dict:
        pass


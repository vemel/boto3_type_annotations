from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_cluster(
        self,
        clusterName: Optional[str] = None,
        tags: Optional[List] = None,
        settings: Optional[List] = None,
    ) -> Dict:
        pass


    def create_service(
        self,
        serviceName: str,
        cluster: Optional[str] = None,
        taskDefinition: Optional[str] = None,
        loadBalancers: Optional[List] = None,
        serviceRegistries: Optional[List] = None,
        desiredCount: Optional[int] = None,
        clientToken: Optional[str] = None,
        launchType: Optional[str] = None,
        platformVersion: Optional[str] = None,
        role: Optional[str] = None,
        deploymentConfiguration: Optional[Dict] = None,
        placementConstraints: Optional[List] = None,
        placementStrategy: Optional[List] = None,
        networkConfiguration: Optional[Dict] = None,
        healthCheckGracePeriodSeconds: Optional[int] = None,
        schedulingStrategy: Optional[str] = None,
        deploymentController: Optional[Dict] = None,
        tags: Optional[List] = None,
        enableECSManagedTags: Optional[bool] = None,
        propagateTags: Optional[str] = None,
    ) -> Dict:
        pass


    def create_task_set(
        self,
        service: str,
        cluster: str,
        taskDefinition: str,
        externalId: Optional[str] = None,
        networkConfiguration: Optional[Dict] = None,
        loadBalancers: Optional[List] = None,
        serviceRegistries: Optional[List] = None,
        launchType: Optional[str] = None,
        platformVersion: Optional[str] = None,
        scale: Optional[Dict] = None,
        clientToken: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_account_setting(
        self,
        name: str,
        principalArn: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_attributes(
        self,
        attributes: List,
        cluster: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_cluster(
        self,
        cluster: str,
    ) -> Dict:
        pass


    def delete_service(
        self,
        service: str,
        cluster: Optional[str] = None,
        force: Optional[bool] = None,
    ) -> Dict:
        pass


    def delete_task_set(
        self,
        cluster: str,
        service: str,
        taskSet: str,
        force: Optional[bool] = None,
    ) -> Dict:
        pass


    def deregister_container_instance(
        self,
        containerInstance: str,
        cluster: Optional[str] = None,
        force: Optional[bool] = None,
    ) -> Dict:
        pass


    def deregister_task_definition(
        self,
        taskDefinition: str,
    ) -> Dict:
        pass


    def describe_clusters(
        self,
        clusters: Optional[List] = None,
        include: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_container_instances(
        self,
        containerInstances: List,
        cluster: Optional[str] = None,
        include: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_services(
        self,
        services: List,
        cluster: Optional[str] = None,
        include: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_task_definition(
        self,
        taskDefinition: str,
        include: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_task_sets(
        self,
        cluster: str,
        service: str,
        taskSets: Optional[List] = None,
    ) -> Dict:
        pass


    def describe_tasks(
        self,
        tasks: List,
        cluster: Optional[str] = None,
        include: Optional[List] = None,
    ) -> Dict:
        pass


    def discover_poll_endpoint(
        self,
        containerInstance: Optional[str] = None,
        cluster: Optional[str] = None,
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


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_account_settings(
        self,
        name: Optional[str] = None,
        value: Optional[str] = None,
        principalArn: Optional[str] = None,
        effectiveSettings: Optional[bool] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_attributes(
        self,
        targetType: str,
        cluster: Optional[str] = None,
        attributeName: Optional[str] = None,
        attributeValue: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_clusters(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_container_instances(
        self,
        cluster: Optional[str] = None,
        filter: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        status: Optional[str] = None,
    ) -> Dict:
        pass


    def list_services(
        self,
        cluster: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        launchType: Optional[str] = None,
        schedulingStrategy: Optional[str] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        resourceArn: str,
    ) -> Dict:
        pass


    def list_task_definition_families(
        self,
        familyPrefix: Optional[str] = None,
        status: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_task_definitions(
        self,
        familyPrefix: Optional[str] = None,
        status: Optional[str] = None,
        sort: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tasks(
        self,
        cluster: Optional[str] = None,
        containerInstance: Optional[str] = None,
        family: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        startedBy: Optional[str] = None,
        serviceName: Optional[str] = None,
        desiredStatus: Optional[str] = None,
        launchType: Optional[str] = None,
    ) -> Dict:
        pass


    def put_account_setting(
        self,
        name: str,
        value: str,
        principalArn: Optional[str] = None,
    ) -> Dict:
        pass


    def put_account_setting_default(
        self,
        name: str,
        value: str,
    ) -> Dict:
        pass


    def put_attributes(
        self,
        attributes: List,
        cluster: Optional[str] = None,
    ) -> Dict:
        pass


    def register_container_instance(
        self,
        cluster: Optional[str] = None,
        instanceIdentityDocument: Optional[str] = None,
        instanceIdentityDocumentSignature: Optional[str] = None,
        totalResources: Optional[List] = None,
        versionInfo: Optional[Dict] = None,
        containerInstanceArn: Optional[str] = None,
        attributes: Optional[List] = None,
        platformDevices: Optional[List] = None,
        tags: Optional[List] = None,
    ) -> Dict:
        pass


    def register_task_definition(
        self,
        family: str,
        containerDefinitions: List,
        taskRoleArn: Optional[str] = None,
        executionRoleArn: Optional[str] = None,
        networkMode: Optional[str] = None,
        volumes: Optional[List] = None,
        placementConstraints: Optional[List] = None,
        requiresCompatibilities: Optional[List] = None,
        cpu: Optional[str] = None,
        memory: Optional[str] = None,
        tags: Optional[List] = None,
        pidMode: Optional[str] = None,
        ipcMode: Optional[str] = None,
        proxyConfiguration: Optional[Dict] = None,
        inferenceAccelerators: Optional[List] = None,
    ) -> Dict:
        pass


    def run_task(
        self,
        taskDefinition: str,
        cluster: Optional[str] = None,
        overrides: Optional[Dict] = None,
        count: Optional[int] = None,
        startedBy: Optional[str] = None,
        group: Optional[str] = None,
        placementConstraints: Optional[List] = None,
        placementStrategy: Optional[List] = None,
        launchType: Optional[str] = None,
        platformVersion: Optional[str] = None,
        networkConfiguration: Optional[Dict] = None,
        tags: Optional[List] = None,
        enableECSManagedTags: Optional[bool] = None,
        propagateTags: Optional[str] = None,
    ) -> Dict:
        pass


    def start_task(
        self,
        taskDefinition: str,
        containerInstances: List,
        cluster: Optional[str] = None,
        overrides: Optional[Dict] = None,
        startedBy: Optional[str] = None,
        group: Optional[str] = None,
        networkConfiguration: Optional[Dict] = None,
        tags: Optional[List] = None,
        enableECSManagedTags: Optional[bool] = None,
        propagateTags: Optional[str] = None,
    ) -> Dict:
        pass


    def stop_task(
        self,
        task: str,
        cluster: Optional[str] = None,
        reason: Optional[str] = None,
    ) -> Dict:
        pass


    def submit_attachment_state_changes(
        self,
        attachments: List,
        cluster: Optional[str] = None,
    ) -> Dict:
        pass


    def submit_container_state_change(
        self,
        cluster: Optional[str] = None,
        task: Optional[str] = None,
        containerName: Optional[str] = None,
        runtimeId: Optional[str] = None,
        status: Optional[str] = None,
        exitCode: Optional[int] = None,
        reason: Optional[str] = None,
        networkBindings: Optional[List] = None,
    ) -> Dict:
        pass


    def submit_task_state_change(
        self,
        cluster: Optional[str] = None,
        task: Optional[str] = None,
        status: Optional[str] = None,
        reason: Optional[str] = None,
        containers: Optional[List] = None,
        attachments: Optional[List] = None,
        pullStartedAt: Optional[datetime] = None,
        pullStoppedAt: Optional[datetime] = None,
        executionStoppedAt: Optional[datetime] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        resourceArn: str,
        tags: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        resourceArn: str,
        tagKeys: List,
    ) -> Dict:
        pass


    def update_cluster_settings(
        self,
        cluster: str,
        settings: List,
    ) -> Dict:
        pass


    def update_container_agent(
        self,
        containerInstance: str,
        cluster: Optional[str] = None,
    ) -> Dict:
        pass


    def update_container_instances_state(
        self,
        containerInstances: List,
        status: str,
        cluster: Optional[str] = None,
    ) -> Dict:
        pass


    def update_service(
        self,
        service: str,
        cluster: Optional[str] = None,
        desiredCount: Optional[int] = None,
        taskDefinition: Optional[str] = None,
        deploymentConfiguration: Optional[Dict] = None,
        networkConfiguration: Optional[Dict] = None,
        platformVersion: Optional[str] = None,
        forceNewDeployment: Optional[bool] = None,
        healthCheckGracePeriodSeconds: Optional[int] = None,
    ) -> Dict:
        pass


    def update_service_primary_task_set(
        self,
        cluster: str,
        service: str,
        primaryTaskSet: str,
    ) -> Dict:
        pass


    def update_task_set(
        self,
        cluster: str,
        service: str,
        taskSet: str,
        scale: Dict,
    ) -> Dict:
        pass


from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def batch_describe_simulation_job(
        self,
        jobs: List,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def cancel_deployment_job(
        self,
        job: str,
    ) -> Dict:
        pass


    def cancel_simulation_job(
        self,
        job: str,
    ) -> Dict:
        pass


    def create_deployment_job(
        self,
        clientRequestToken: str,
        fleet: str,
        deploymentApplicationConfigs: List,
        deploymentConfig: Optional[Dict] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_fleet(
        self,
        name: str,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_robot(
        self,
        name: str,
        architecture: str,
        greengrassGroupId: str,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_robot_application(
        self,
        name: str,
        sources: List,
        robotSoftwareSuite: Dict,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_robot_application_version(
        self,
        application: str,
        currentRevisionId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_simulation_application(
        self,
        name: str,
        sources: List,
        simulationSoftwareSuite: Dict,
        robotSoftwareSuite: Dict,
        renderingEngine: Optional[Dict] = None,
        tags: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_simulation_application_version(
        self,
        application: str,
        currentRevisionId: Optional[str] = None,
    ) -> Dict:
        pass


    def create_simulation_job(
        self,
        maxJobDurationInSeconds: int,
        iamRole: str,
        clientRequestToken: Optional[str] = None,
        outputLocation: Optional[Dict] = None,
        loggingConfig: Optional[Dict] = None,
        failureBehavior: Optional[str] = None,
        robotApplications: Optional[List] = None,
        simulationApplications: Optional[List] = None,
        dataSources: Optional[List] = None,
        tags: Optional[Dict] = None,
        vpcConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_fleet(
        self,
        fleet: str,
    ) -> Dict:
        pass


    def delete_robot(
        self,
        robot: str,
    ) -> Dict:
        pass


    def delete_robot_application(
        self,
        application: str,
        applicationVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_simulation_application(
        self,
        application: str,
        applicationVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def deregister_robot(
        self,
        fleet: str,
        robot: str,
    ) -> Dict:
        pass


    def describe_deployment_job(
        self,
        job: str,
    ) -> Dict:
        pass


    def describe_fleet(
        self,
        fleet: str,
    ) -> Dict:
        pass


    def describe_robot(
        self,
        robot: str,
    ) -> Dict:
        pass


    def describe_robot_application(
        self,
        application: str,
        applicationVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_simulation_application(
        self,
        application: str,
        applicationVersion: Optional[str] = None,
    ) -> Dict:
        pass


    def describe_simulation_job(
        self,
        job: str,
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


    def list_deployment_jobs(
        self,
        filters: Optional[List] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_fleets(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        filters: Optional[List] = None,
    ) -> Dict:
        pass


    def list_robot_applications(
        self,
        versionQualifier: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        filters: Optional[List] = None,
    ) -> Dict:
        pass


    def list_robots(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        filters: Optional[List] = None,
    ) -> Dict:
        pass


    def list_simulation_applications(
        self,
        versionQualifier: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        filters: Optional[List] = None,
    ) -> Dict:
        pass


    def list_simulation_jobs(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        filters: Optional[List] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        resourceArn: str,
    ) -> Dict:
        pass


    def register_robot(
        self,
        fleet: str,
        robot: str,
    ) -> Dict:
        pass


    def restart_simulation_job(
        self,
        job: str,
    ) -> Dict:
        pass


    def sync_deployment_job(
        self,
        clientRequestToken: str,
        fleet: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        resourceArn: str,
        tags: Dict,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        resourceArn: str,
        tagKeys: List,
    ) -> Dict:
        pass


    def update_robot_application(
        self,
        application: str,
        sources: List,
        robotSoftwareSuite: Dict,
        currentRevisionId: Optional[str] = None,
    ) -> Dict:
        pass


    def update_simulation_application(
        self,
        application: str,
        sources: List,
        simulationSoftwareSuite: Dict,
        robotSoftwareSuite: Dict,
        renderingEngine: Optional[Dict] = None,
        currentRevisionId: Optional[str] = None,
    ) -> Dict:
        pass


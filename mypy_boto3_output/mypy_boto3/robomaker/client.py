from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def batch_describe_simulation_job(self, jobs: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def cancel_deployment_job(self, job: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def cancel_simulation_job(self, job: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_deployment_job(
        self,
        clientRequestToken: str,
        fleet: str,
        deploymentApplicationConfigs: List[Any],
        deploymentConfig: Dict[str, Any] = None,
        tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_fleet(self, name: str, tags: Dict[str, Any] = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_robot(
        self,
        name: str,
        architecture: str,
        greengrassGroupId: str,
        tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_robot_application(
        self,
        name: str,
        sources: List[Any],
        robotSoftwareSuite: Dict[str, Any],
        tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_robot_application_version(
        self, application: str, currentRevisionId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_simulation_application(
        self,
        name: str,
        sources: List[Any],
        simulationSoftwareSuite: Dict[str, Any],
        robotSoftwareSuite: Dict[str, Any],
        renderingEngine: Dict[str, Any] = None,
        tags: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_simulation_application_version(
        self, application: str, currentRevisionId: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_simulation_job(
        self,
        maxJobDurationInSeconds: int,
        iamRole: str,
        clientRequestToken: str = None,
        outputLocation: Dict[str, Any] = None,
        loggingConfig: Dict[str, Any] = None,
        failureBehavior: str = None,
        robotApplications: List[Any] = None,
        simulationApplications: List[Any] = None,
        dataSources: List[Any] = None,
        tags: Dict[str, Any] = None,
        vpcConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_fleet(self, fleet: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_robot(self, robot: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_robot_application(
        self, application: str, applicationVersion: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_simulation_application(
        self, application: str, applicationVersion: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def deregister_robot(self, fleet: str, robot: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_deployment_job(self, job: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_fleet(self, fleet: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_robot(self, robot: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_robot_application(
        self, application: str, applicationVersion: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_simulation_application(
        self, application: str, applicationVersion: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_simulation_job(self, job: str) -> Dict[str, Any]:
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
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_deployment_jobs(
        self, filters: List[Any] = None, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_fleets(
        self, nextToken: str = None, maxResults: int = None, filters: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_robot_applications(
        self,
        versionQualifier: str = None,
        nextToken: str = None,
        maxResults: int = None,
        filters: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_robots(
        self, nextToken: str = None, maxResults: int = None, filters: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_simulation_applications(
        self,
        versionQualifier: str = None,
        nextToken: str = None,
        maxResults: int = None,
        filters: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_simulation_jobs(
        self, nextToken: str = None, maxResults: int = None, filters: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, resourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_robot(self, fleet: str, robot: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def restart_simulation_job(self, job: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def sync_deployment_job(
        self, clientRequestToken: str, fleet: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, resourceArn: str, tags: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_robot_application(
        self,
        application: str,
        sources: List[Any],
        robotSoftwareSuite: Dict[str, Any],
        currentRevisionId: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_simulation_application(
        self,
        application: str,
        sources: List[Any],
        simulationSoftwareSuite: Dict[str, Any],
        robotSoftwareSuite: Dict[str, Any],
        renderingEngine: Dict[str, Any] = None,
        currentRevisionId: str = None,
    ) -> Dict[str, Any]:
        pass

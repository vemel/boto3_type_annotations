from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_campaign(
        self, name: str, solutionVersionArn: str, minProvisionedTPS: int
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_dataset(
        self, name: str, schemaArn: str, datasetGroupArn: str, datasetType: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_dataset_group(
        self, name: str, roleArn: str = None, kmsKeyArn: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_dataset_import_job(
        self, jobName: str, datasetArn: str, dataSource: Dict[str, Any], roleArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_event_tracker(self, name: str, datasetGroupArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_schema(self, name: str, schema: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_solution(
        self,
        name: str,
        datasetGroupArn: str,
        performHPO: bool = None,
        performAutoML: bool = None,
        recipeArn: str = None,
        eventType: str = None,
        solutionConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_solution_version(
        self, solutionArn: str, trainingMode: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_campaign(self, campaignArn: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_dataset(self, datasetArn: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_dataset_group(self, datasetGroupArn: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_event_tracker(self, eventTrackerArn: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_schema(self, schemaArn: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_solution(self, solutionArn: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_algorithm(self, algorithmArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_campaign(self, campaignArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_dataset(self, datasetArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_dataset_group(self, datasetGroupArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_dataset_import_job(self, datasetImportJobArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_event_tracker(self, eventTrackerArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_feature_transformation(
        self, featureTransformationArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_recipe(self, recipeArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_schema(self, schemaArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_solution(self, solutionArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_solution_version(self, solutionVersionArn: str) -> Dict[str, Any]:
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
    def get_solution_metrics(self, solutionVersionArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_campaigns(
        self, solutionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_dataset_groups(
        self, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_dataset_import_jobs(
        self, datasetArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_datasets(
        self, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_event_trackers(
        self, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_recipes(
        self, recipeProvider: str = None, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_schemas(
        self, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_solution_versions(
        self, solutionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_solutions(
        self, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_campaign(
        self,
        campaignArn: str,
        solutionVersionArn: str = None,
        minProvisionedTPS: int = None,
    ) -> Dict[str, Any]:
        pass

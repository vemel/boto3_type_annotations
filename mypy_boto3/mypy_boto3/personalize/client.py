from typing import Dict
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_campaign(
        self,
        name: str,
        solutionVersionArn: str,
        minProvisionedTPS: int,
    ) -> Dict:
        pass


    def create_dataset(
        self,
        name: str,
        schemaArn: str,
        datasetGroupArn: str,
        datasetType: str,
    ) -> Dict:
        pass


    def create_dataset_group(
        self,
        name: str,
        roleArn: Optional[str] = None,
        kmsKeyArn: Optional[str] = None,
    ) -> Dict:
        pass


    def create_dataset_import_job(
        self,
        jobName: str,
        datasetArn: str,
        dataSource: Dict,
        roleArn: str,
    ) -> Dict:
        pass


    def create_event_tracker(
        self,
        name: str,
        datasetGroupArn: str,
    ) -> Dict:
        pass


    def create_schema(
        self,
        name: str,
        schema: str,
    ) -> Dict:
        pass


    def create_solution(
        self,
        name: str,
        datasetGroupArn: str,
        performHPO: Optional[bool] = None,
        performAutoML: Optional[bool] = None,
        recipeArn: Optional[str] = None,
        eventType: Optional[str] = None,
        solutionConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_solution_version(
        self,
        solutionArn: str,
        trainingMode: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_campaign(
        self,
        campaignArn: str,
    ):
        pass


    def delete_dataset(
        self,
        datasetArn: str,
    ):
        pass


    def delete_dataset_group(
        self,
        datasetGroupArn: str,
    ):
        pass


    def delete_event_tracker(
        self,
        eventTrackerArn: str,
    ):
        pass


    def delete_schema(
        self,
        schemaArn: str,
    ):
        pass


    def delete_solution(
        self,
        solutionArn: str,
    ):
        pass


    def describe_algorithm(
        self,
        algorithmArn: str,
    ) -> Dict:
        pass


    def describe_campaign(
        self,
        campaignArn: str,
    ) -> Dict:
        pass


    def describe_dataset(
        self,
        datasetArn: str,
    ) -> Dict:
        pass


    def describe_dataset_group(
        self,
        datasetGroupArn: str,
    ) -> Dict:
        pass


    def describe_dataset_import_job(
        self,
        datasetImportJobArn: str,
    ) -> Dict:
        pass


    def describe_event_tracker(
        self,
        eventTrackerArn: str,
    ) -> Dict:
        pass


    def describe_feature_transformation(
        self,
        featureTransformationArn: str,
    ) -> Dict:
        pass


    def describe_recipe(
        self,
        recipeArn: str,
    ) -> Dict:
        pass


    def describe_schema(
        self,
        schemaArn: str,
    ) -> Dict:
        pass


    def describe_solution(
        self,
        solutionArn: str,
    ) -> Dict:
        pass


    def describe_solution_version(
        self,
        solutionVersionArn: str,
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


    def get_solution_metrics(
        self,
        solutionVersionArn: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_campaigns(
        self,
        solutionArn: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_dataset_groups(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_dataset_import_jobs(
        self,
        datasetArn: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_datasets(
        self,
        datasetGroupArn: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_event_trackers(
        self,
        datasetGroupArn: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_recipes(
        self,
        recipeProvider: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_schemas(
        self,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_solution_versions(
        self,
        solutionArn: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_solutions(
        self,
        datasetGroupArn: Optional[str] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def update_campaign(
        self,
        campaignArn: str,
        solutionVersionArn: Optional[str] = None,
        minProvisionedTPS: Optional[int] = None,
    ) -> Dict:
        pass


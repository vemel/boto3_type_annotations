from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_tags(
        self,
        Tags: List,
        ResourceId: str,
        ResourceType: str,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_batch_prediction(
        self,
        BatchPredictionId: str,
        MLModelId: str,
        BatchPredictionDataSourceId: str,
        OutputUri: str,
        BatchPredictionName: Optional[str] = None,
    ) -> Dict:
        pass


    def create_data_source_from_rds(
        self,
        DataSourceId: str,
        RDSData: Dict,
        RoleARN: str,
        DataSourceName: Optional[str] = None,
        ComputeStatistics: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_data_source_from_redshift(
        self,
        DataSourceId: str,
        DataSpec: Dict,
        RoleARN: str,
        DataSourceName: Optional[str] = None,
        ComputeStatistics: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_data_source_from_s3(
        self,
        DataSourceId: str,
        DataSpec: Dict,
        DataSourceName: Optional[str] = None,
        ComputeStatistics: Optional[bool] = None,
    ) -> Dict:
        pass


    def create_evaluation(
        self,
        EvaluationId: str,
        MLModelId: str,
        EvaluationDataSourceId: str,
        EvaluationName: Optional[str] = None,
    ) -> Dict:
        pass


    def create_ml_model(
        self,
        MLModelId: str,
        MLModelType: str,
        TrainingDataSourceId: str,
        MLModelName: Optional[str] = None,
        Parameters: Optional[Dict] = None,
        Recipe: Optional[str] = None,
        RecipeUri: Optional[str] = None,
    ) -> Dict:
        pass


    def create_realtime_endpoint(
        self,
        MLModelId: str,
    ) -> Dict:
        pass


    def delete_batch_prediction(
        self,
        BatchPredictionId: str,
    ) -> Dict:
        pass


    def delete_data_source(
        self,
        DataSourceId: str,
    ) -> Dict:
        pass


    def delete_evaluation(
        self,
        EvaluationId: str,
    ) -> Dict:
        pass


    def delete_ml_model(
        self,
        MLModelId: str,
    ) -> Dict:
        pass


    def delete_realtime_endpoint(
        self,
        MLModelId: str,
    ) -> Dict:
        pass


    def delete_tags(
        self,
        TagKeys: List,
        ResourceId: str,
        ResourceType: str,
    ) -> Dict:
        pass


    def describe_batch_predictions(
        self,
        FilterVariable: Optional[str] = None,
        EQ: Optional[str] = None,
        GT: Optional[str] = None,
        LT: Optional[str] = None,
        GE: Optional[str] = None,
        LE: Optional[str] = None,
        NE: Optional[str] = None,
        Prefix: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_data_sources(
        self,
        FilterVariable: Optional[str] = None,
        EQ: Optional[str] = None,
        GT: Optional[str] = None,
        LT: Optional[str] = None,
        GE: Optional[str] = None,
        LE: Optional[str] = None,
        NE: Optional[str] = None,
        Prefix: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_evaluations(
        self,
        FilterVariable: Optional[str] = None,
        EQ: Optional[str] = None,
        GT: Optional[str] = None,
        LT: Optional[str] = None,
        GE: Optional[str] = None,
        LE: Optional[str] = None,
        NE: Optional[str] = None,
        Prefix: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_ml_models(
        self,
        FilterVariable: Optional[str] = None,
        EQ: Optional[str] = None,
        GT: Optional[str] = None,
        LT: Optional[str] = None,
        GE: Optional[str] = None,
        LE: Optional[str] = None,
        NE: Optional[str] = None,
        Prefix: Optional[str] = None,
        SortOrder: Optional[str] = None,
        NextToken: Optional[str] = None,
        Limit: Optional[int] = None,
    ) -> Dict:
        pass


    def describe_tags(
        self,
        ResourceId: str,
        ResourceType: str,
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


    def get_batch_prediction(
        self,
        BatchPredictionId: str,
    ) -> Dict:
        pass


    def get_data_source(
        self,
        DataSourceId: str,
        Verbose: Optional[bool] = None,
    ) -> Dict:
        pass


    def get_evaluation(
        self,
        EvaluationId: str,
    ) -> Dict:
        pass


    def get_ml_model(
        self,
        MLModelId: str,
        Verbose: Optional[bool] = None,
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


    def predict(
        self,
        MLModelId: str,
        Record: Dict,
        PredictEndpoint: str,
    ) -> Dict:
        pass


    def update_batch_prediction(
        self,
        BatchPredictionId: str,
        BatchPredictionName: str,
    ) -> Dict:
        pass


    def update_data_source(
        self,
        DataSourceId: str,
        DataSourceName: str,
    ) -> Dict:
        pass


    def update_evaluation(
        self,
        EvaluationId: str,
        EvaluationName: str,
    ) -> Dict:
        pass


    def update_ml_model(
        self,
        MLModelId: str,
        MLModelName: Optional[str] = None,
        ScoreThreshold: Optional[float] = None,
    ) -> Dict:
        pass


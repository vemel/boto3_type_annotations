from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def add_tags(
        self, Tags: List[Any], ResourceId: str, ResourceType: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_batch_prediction(
        self,
        BatchPredictionId: str,
        MLModelId: str,
        BatchPredictionDataSourceId: str,
        OutputUri: str,
        BatchPredictionName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_data_source_from_rds(
        self,
        DataSourceId: str,
        RDSData: Dict[str, Any],
        RoleARN: str,
        DataSourceName: str = None,
        ComputeStatistics: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_data_source_from_redshift(
        self,
        DataSourceId: str,
        DataSpec: Dict[str, Any],
        RoleARN: str,
        DataSourceName: str = None,
        ComputeStatistics: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_data_source_from_s3(
        self,
        DataSourceId: str,
        DataSpec: Dict[str, Any],
        DataSourceName: str = None,
        ComputeStatistics: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_evaluation(
        self,
        EvaluationId: str,
        MLModelId: str,
        EvaluationDataSourceId: str,
        EvaluationName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_ml_model(
        self,
        MLModelId: str,
        MLModelType: str,
        TrainingDataSourceId: str,
        MLModelName: str = None,
        Parameters: Dict[str, Any] = None,
        Recipe: str = None,
        RecipeUri: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_realtime_endpoint(self, MLModelId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_batch_prediction(self, BatchPredictionId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_data_source(self, DataSourceId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_evaluation(self, EvaluationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_ml_model(self, MLModelId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_realtime_endpoint(self, MLModelId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_tags(
        self, TagKeys: List[Any], ResourceId: str, ResourceType: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_batch_predictions(
        self,
        FilterVariable: str = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: str = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_data_sources(
        self,
        FilterVariable: str = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: str = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_evaluations(
        self,
        FilterVariable: str = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: str = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_ml_models(
        self,
        FilterVariable: str = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: str = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_tags(self, ResourceId: str, ResourceType: str) -> Dict[str, Any]:
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
    def get_batch_prediction(self, BatchPredictionId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_data_source(
        self, DataSourceId: str, Verbose: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_evaluation(self, EvaluationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_ml_model(self, MLModelId: str, Verbose: bool = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def predict(
        self, MLModelId: str, Record: Dict[str, Any], PredictEndpoint: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_batch_prediction(
        self, BatchPredictionId: str, BatchPredictionName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_data_source(
        self, DataSourceId: str, DataSourceName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_evaluation(
        self, EvaluationId: str, EvaluationName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_ml_model(
        self, MLModelId: str, MLModelName: str = None, ScoreThreshold: float = None
    ) -> Dict[str, Any]:
        pass

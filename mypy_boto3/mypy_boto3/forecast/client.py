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


    def create_dataset(
        self,
        DatasetName: str,
        Domain: str,
        DatasetType: str,
        Schema: Dict,
        DataFrequency: Optional[str] = None,
        EncryptionConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_dataset_group(
        self,
        DatasetGroupName: str,
        Domain: str,
        DatasetArns: Optional[List] = None,
    ) -> Dict:
        pass


    def create_dataset_import_job(
        self,
        DatasetImportJobName: str,
        DatasetArn: str,
        DataSource: Dict,
        TimestampFormat: Optional[str] = None,
    ) -> Dict:
        pass


    def create_forecast(
        self,
        ForecastName: str,
        PredictorArn: str,
    ) -> Dict:
        pass


    def create_forecast_export_job(
        self,
        ForecastExportJobName: str,
        ForecastArn: str,
        Destination: Dict,
    ) -> Dict:
        pass


    def create_predictor(
        self,
        PredictorName: str,
        ForecastHorizon: int,
        InputDataConfig: Dict,
        FeaturizationConfig: Dict,
        AlgorithmArn: Optional[str] = None,
        PerformAutoML: Optional[bool] = None,
        PerformHPO: Optional[bool] = None,
        TrainingParameters: Optional[Dict] = None,
        EvaluationParameters: Optional[Dict] = None,
        HPOConfig: Optional[Dict] = None,
        EncryptionConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_dataset(
        self,
        DatasetArn: str,
    ):
        pass


    def delete_dataset_group(
        self,
        DatasetGroupArn: str,
    ):
        pass


    def delete_dataset_import_job(
        self,
        DatasetImportJobArn: str,
    ):
        pass


    def delete_forecast(
        self,
        ForecastArn: str,
    ):
        pass


    def delete_forecast_export_job(
        self,
        ForecastExportJobArn: str,
    ):
        pass


    def delete_predictor(
        self,
        PredictorArn: str,
    ):
        pass


    def describe_dataset(
        self,
        DatasetArn: str,
    ) -> Dict:
        pass


    def describe_dataset_group(
        self,
        DatasetGroupArn: str,
    ) -> Dict:
        pass


    def describe_dataset_import_job(
        self,
        DatasetImportJobArn: str,
    ) -> Dict:
        pass


    def describe_forecast(
        self,
        ForecastArn: str,
    ) -> Dict:
        pass


    def describe_forecast_export_job(
        self,
        ForecastExportJobArn: str,
    ) -> Dict:
        pass


    def describe_predictor(
        self,
        PredictorArn: str,
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


    def get_accuracy_metrics(
        self,
        PredictorArn: str,
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


    def list_dataset_groups(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_dataset_import_jobs(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Filters: Optional[List] = None,
    ) -> Dict:
        pass


    def list_datasets(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_forecast_export_jobs(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Filters: Optional[List] = None,
    ) -> Dict:
        pass


    def list_forecasts(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Filters: Optional[List] = None,
    ) -> Dict:
        pass


    def list_predictors(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        Filters: Optional[List] = None,
    ) -> Dict:
        pass


    def update_dataset_group(
        self,
        DatasetGroupArn: str,
        DatasetArns: List,
    ) -> Dict:
        pass


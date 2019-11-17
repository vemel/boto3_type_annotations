"Helper functions for machinelearning service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_machinelearning.client import Client
from mypy_boto3_machinelearning.paginator import (
    DescribeBatchPredictionsPaginator,
    DescribeDataSourcesPaginator,
    DescribeEvaluationsPaginator,
    DescribeMLModelsPaginator,
)
from mypy_boto3_machinelearning.waiter import (
    BatchPredictionAvailableWaiter,
    DataSourceAvailableWaiter,
    EvaluationAvailableWaiter,
    MLModelAvailableWaiter,
)

# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def boto3_client(
    session: Session = None,
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> Client:
    """
    Equivalent of `boto3.client('machinelearning')`, returns a correct type.
    """
    kwargs: Dict[str, Any] = {}
    if region_name is not None:
        kwargs["region_name"] = region_name
    if api_version is not None:
        kwargs["api_version"] = api_version
    if use_ssl is not None:
        kwargs["use_ssl"] = use_ssl
    if verify is not None:
        kwargs["verify"] = verify
    if endpoint_url is not None:
        kwargs["endpoint_url"] = endpoint_url
    if aws_access_key_id is not None:
        kwargs["aws_access_key_id"] = aws_access_key_id
    if aws_secret_access_key is not None:
        kwargs["aws_secret_access_key"] = aws_secret_access_key
    if aws_session_token is not None:
        kwargs["aws_session_token"] = aws_session_token
    if config is not None:
        kwargs["config"] = config
    if session is not None:
        return session.client("machinelearning", **kwargs)
    return boto3.client("machinelearning", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_batch_predictions_paginator(
    client: Client,
) -> DescribeBatchPredictionsPaginator:
    """
    Equivalent of `client.get_paginator('describe_batch_predictions')`, returns a correct type.
    """
    return client.get_paginator("describe_batch_predictions")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_data_sources_paginator(client: Client) -> DescribeDataSourcesPaginator:
    """
    Equivalent of `client.get_paginator('describe_data_sources')`, returns a correct type.
    """
    return client.get_paginator("describe_data_sources")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_evaluations_paginator(client: Client) -> DescribeEvaluationsPaginator:
    """
    Equivalent of `client.get_paginator('describe_evaluations')`, returns a correct type.
    """
    return client.get_paginator("describe_evaluations")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_ml_models_paginator(client: Client) -> DescribeMLModelsPaginator:
    """
    Equivalent of `client.get_paginator('describe_ml_models')`, returns a correct type.
    """
    return client.get_paginator("describe_ml_models")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_batch_prediction_available_waiter(
    client: Client,
) -> BatchPredictionAvailableWaiter:
    """
    Equivalent of `client.get_waiter('batch_prediction_available')`, returns a correct type.
    """
    return client.get_waiter("batch_prediction_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_data_source_available_waiter(client: Client) -> DataSourceAvailableWaiter:
    """
    Equivalent of `client.get_waiter('data_source_available')`, returns a correct type.
    """
    return client.get_waiter("data_source_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_evaluation_available_waiter(client: Client) -> EvaluationAvailableWaiter:
    """
    Equivalent of `client.get_waiter('evaluation_available')`, returns a correct type.
    """
    return client.get_waiter("evaluation_available")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_ml_model_available_waiter(client: Client) -> MLModelAvailableWaiter:
    """
    Equivalent of `client.get_waiter('ml_model_available')`, returns a correct type.
    """
    return client.get_waiter("ml_model_available")

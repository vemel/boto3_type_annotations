"Helper functions for comprehend service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_comprehend.client import Client
from mypy_boto3_comprehend.paginator import (
    ListDocumentClassificationJobsPaginator,
    ListDocumentClassifiersPaginator,
    ListDominantLanguageDetectionJobsPaginator,
    ListEntitiesDetectionJobsPaginator,
    ListEntityRecognizersPaginator,
    ListKeyPhrasesDetectionJobsPaginator,
    ListSentimentDetectionJobsPaginator,
    ListTopicsDetectionJobsPaginator,
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
    Equivalent of `boto3.client('comprehend')`, returns a correct type.
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
        return session.client("comprehend", **kwargs)
    return boto3.client("comprehend", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_document_classification_jobs_paginator(
    client: Client,
) -> ListDocumentClassificationJobsPaginator:
    """
    Equivalent of `client.get_paginator('list_document_classification_jobs')`, returns a correct type.
    """
    return client.get_paginator("list_document_classification_jobs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_document_classifiers_paginator(
    client: Client,
) -> ListDocumentClassifiersPaginator:
    """
    Equivalent of `client.get_paginator('list_document_classifiers')`, returns a correct type.
    """
    return client.get_paginator("list_document_classifiers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_dominant_language_detection_jobs_paginator(
    client: Client,
) -> ListDominantLanguageDetectionJobsPaginator:
    """
    Equivalent of `client.get_paginator('list_dominant_language_detection_jobs')`, returns a correct type.
    """
    return client.get_paginator("list_dominant_language_detection_jobs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_entities_detection_jobs_paginator(
    client: Client,
) -> ListEntitiesDetectionJobsPaginator:
    """
    Equivalent of `client.get_paginator('list_entities_detection_jobs')`, returns a correct type.
    """
    return client.get_paginator("list_entities_detection_jobs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_entity_recognizers_paginator(
    client: Client,
) -> ListEntityRecognizersPaginator:
    """
    Equivalent of `client.get_paginator('list_entity_recognizers')`, returns a correct type.
    """
    return client.get_paginator("list_entity_recognizers")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_key_phrases_detection_jobs_paginator(
    client: Client,
) -> ListKeyPhrasesDetectionJobsPaginator:
    """
    Equivalent of `client.get_paginator('list_key_phrases_detection_jobs')`, returns a correct type.
    """
    return client.get_paginator("list_key_phrases_detection_jobs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_sentiment_detection_jobs_paginator(
    client: Client,
) -> ListSentimentDetectionJobsPaginator:
    """
    Equivalent of `client.get_paginator('list_sentiment_detection_jobs')`, returns a correct type.
    """
    return client.get_paginator("list_sentiment_detection_jobs")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_topics_detection_jobs_paginator(
    client: Client,
) -> ListTopicsDetectionJobsPaginator:
    """
    Equivalent of `client.get_paginator('list_topics_detection_jobs')`, returns a correct type.
    """
    return client.get_paginator("list_topics_detection_jobs")

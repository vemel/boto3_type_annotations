from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def batch_detect_dominant_language(self, TextList: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_detect_entities(
        self, TextList: List[Any], LanguageCode: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_detect_key_phrases(
        self, TextList: List[Any], LanguageCode: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_detect_sentiment(
        self, TextList: List[Any], LanguageCode: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_detect_syntax(
        self, TextList: List[Any], LanguageCode: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_document_classifier(
        self,
        DocumentClassifierName: str,
        DataAccessRoleArn: str,
        InputDataConfig: Dict[str, Any],
        LanguageCode: str,
        Tags: List[Any] = None,
        OutputDataConfig: Dict[str, Any] = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_entity_recognizer(
        self,
        RecognizerName: str,
        DataAccessRoleArn: str,
        InputDataConfig: Dict[str, Any],
        LanguageCode: str,
        Tags: List[Any] = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_document_classifier(self, DocumentClassifierArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_entity_recognizer(self, EntityRecognizerArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_document_classification_job(self, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_document_classifier(
        self, DocumentClassifierArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_dominant_language_detection_job(self, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_entities_detection_job(self, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_entity_recognizer(self, EntityRecognizerArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_key_phrases_detection_job(self, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_sentiment_detection_job(self, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_topics_detection_job(self, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detect_dominant_language(self, Text: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detect_entities(self, Text: str, LanguageCode: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detect_key_phrases(self, Text: str, LanguageCode: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detect_sentiment(self, Text: str, LanguageCode: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detect_syntax(self, Text: str, LanguageCode: str) -> Dict[str, Any]:
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
    def list_document_classification_jobs(
        self,
        Filter: Dict[str, Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_document_classifiers(
        self,
        Filter: Dict[str, Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_dominant_language_detection_jobs(
        self,
        Filter: Dict[str, Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_entities_detection_jobs(
        self,
        Filter: Dict[str, Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_entity_recognizers(
        self,
        Filter: Dict[str, Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_key_phrases_detection_jobs(
        self,
        Filter: Dict[str, Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_sentiment_detection_jobs(
        self,
        Filter: Dict[str, Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, ResourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_topics_detection_jobs(
        self,
        Filter: Dict[str, Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_document_classification_job(
        self,
        DocumentClassifierArn: str,
        InputDataConfig: Dict[str, Any],
        OutputDataConfig: Dict[str, Any],
        DataAccessRoleArn: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_dominant_language_detection_job(
        self,
        InputDataConfig: Dict[str, Any],
        OutputDataConfig: Dict[str, Any],
        DataAccessRoleArn: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_entities_detection_job(
        self,
        InputDataConfig: Dict[str, Any],
        OutputDataConfig: Dict[str, Any],
        DataAccessRoleArn: str,
        LanguageCode: str,
        JobName: str = None,
        EntityRecognizerArn: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_key_phrases_detection_job(
        self,
        InputDataConfig: Dict[str, Any],
        OutputDataConfig: Dict[str, Any],
        DataAccessRoleArn: str,
        LanguageCode: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_sentiment_detection_job(
        self,
        InputDataConfig: Dict[str, Any],
        OutputDataConfig: Dict[str, Any],
        DataAccessRoleArn: str,
        LanguageCode: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_topics_detection_job(
        self,
        InputDataConfig: Dict[str, Any],
        OutputDataConfig: Dict[str, Any],
        DataAccessRoleArn: str,
        JobName: str = None,
        NumberOfTopics: int = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_dominant_language_detection_job(self, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_entities_detection_job(self, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_key_phrases_detection_job(self, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_sentiment_detection_job(self, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_training_document_classifier(
        self, DocumentClassifierArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_training_entity_recognizer(
        self, EntityRecognizerArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceArn: str, Tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
        pass

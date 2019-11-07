from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def batch_detect_dominant_language(
        self,
        TextList: List,
    ) -> Dict:
        pass


    def batch_detect_entities(
        self,
        TextList: List,
        LanguageCode: str,
    ) -> Dict:
        pass


    def batch_detect_key_phrases(
        self,
        TextList: List,
        LanguageCode: str,
    ) -> Dict:
        pass


    def batch_detect_sentiment(
        self,
        TextList: List,
        LanguageCode: str,
    ) -> Dict:
        pass


    def batch_detect_syntax(
        self,
        TextList: List,
        LanguageCode: str,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_document_classifier(
        self,
        DocumentClassifierName: str,
        DataAccessRoleArn: str,
        InputDataConfig: Dict,
        LanguageCode: str,
        Tags: Optional[List] = None,
        OutputDataConfig: Optional[Dict] = None,
        ClientRequestToken: Optional[str] = None,
        VolumeKmsKeyId: Optional[str] = None,
        VpcConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def create_entity_recognizer(
        self,
        RecognizerName: str,
        DataAccessRoleArn: str,
        InputDataConfig: Dict,
        LanguageCode: str,
        Tags: Optional[List] = None,
        ClientRequestToken: Optional[str] = None,
        VolumeKmsKeyId: Optional[str] = None,
        VpcConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def delete_document_classifier(
        self,
        DocumentClassifierArn: str,
    ) -> Dict:
        pass


    def delete_entity_recognizer(
        self,
        EntityRecognizerArn: str,
    ) -> Dict:
        pass


    def describe_document_classification_job(
        self,
        JobId: str,
    ) -> Dict:
        pass


    def describe_document_classifier(
        self,
        DocumentClassifierArn: str,
    ) -> Dict:
        pass


    def describe_dominant_language_detection_job(
        self,
        JobId: str,
    ) -> Dict:
        pass


    def describe_entities_detection_job(
        self,
        JobId: str,
    ) -> Dict:
        pass


    def describe_entity_recognizer(
        self,
        EntityRecognizerArn: str,
    ) -> Dict:
        pass


    def describe_key_phrases_detection_job(
        self,
        JobId: str,
    ) -> Dict:
        pass


    def describe_sentiment_detection_job(
        self,
        JobId: str,
    ) -> Dict:
        pass


    def describe_topics_detection_job(
        self,
        JobId: str,
    ) -> Dict:
        pass


    def detect_dominant_language(
        self,
        Text: str,
    ) -> Dict:
        pass


    def detect_entities(
        self,
        Text: str,
        LanguageCode: str,
    ) -> Dict:
        pass


    def detect_key_phrases(
        self,
        Text: str,
        LanguageCode: str,
    ) -> Dict:
        pass


    def detect_sentiment(
        self,
        Text: str,
        LanguageCode: str,
    ) -> Dict:
        pass


    def detect_syntax(
        self,
        Text: str,
        LanguageCode: str,
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


    def list_document_classification_jobs(
        self,
        Filter: Optional[Dict] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_document_classifiers(
        self,
        Filter: Optional[Dict] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_dominant_language_detection_jobs(
        self,
        Filter: Optional[Dict] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_entities_detection_jobs(
        self,
        Filter: Optional[Dict] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_entity_recognizers(
        self,
        Filter: Optional[Dict] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_key_phrases_detection_jobs(
        self,
        Filter: Optional[Dict] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_sentiment_detection_jobs(
        self,
        Filter: Optional[Dict] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        ResourceArn: str,
    ) -> Dict:
        pass


    def list_topics_detection_jobs(
        self,
        Filter: Optional[Dict] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def start_document_classification_job(
        self,
        DocumentClassifierArn: str,
        InputDataConfig: Dict,
        OutputDataConfig: Dict,
        DataAccessRoleArn: str,
        JobName: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
        VolumeKmsKeyId: Optional[str] = None,
        VpcConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def start_dominant_language_detection_job(
        self,
        InputDataConfig: Dict,
        OutputDataConfig: Dict,
        DataAccessRoleArn: str,
        JobName: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
        VolumeKmsKeyId: Optional[str] = None,
        VpcConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def start_entities_detection_job(
        self,
        InputDataConfig: Dict,
        OutputDataConfig: Dict,
        DataAccessRoleArn: str,
        LanguageCode: str,
        JobName: Optional[str] = None,
        EntityRecognizerArn: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
        VolumeKmsKeyId: Optional[str] = None,
        VpcConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def start_key_phrases_detection_job(
        self,
        InputDataConfig: Dict,
        OutputDataConfig: Dict,
        DataAccessRoleArn: str,
        LanguageCode: str,
        JobName: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
        VolumeKmsKeyId: Optional[str] = None,
        VpcConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def start_sentiment_detection_job(
        self,
        InputDataConfig: Dict,
        OutputDataConfig: Dict,
        DataAccessRoleArn: str,
        LanguageCode: str,
        JobName: Optional[str] = None,
        ClientRequestToken: Optional[str] = None,
        VolumeKmsKeyId: Optional[str] = None,
        VpcConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def start_topics_detection_job(
        self,
        InputDataConfig: Dict,
        OutputDataConfig: Dict,
        DataAccessRoleArn: str,
        JobName: Optional[str] = None,
        NumberOfTopics: Optional[int] = None,
        ClientRequestToken: Optional[str] = None,
        VolumeKmsKeyId: Optional[str] = None,
        VpcConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


    def stop_dominant_language_detection_job(
        self,
        JobId: str,
    ) -> Dict:
        pass


    def stop_entities_detection_job(
        self,
        JobId: str,
    ) -> Dict:
        pass


    def stop_key_phrases_detection_job(
        self,
        JobId: str,
    ) -> Dict:
        pass


    def stop_sentiment_detection_job(
        self,
        JobId: str,
    ) -> Dict:
        pass


    def stop_training_document_classifier(
        self,
        DocumentClassifierArn: str,
    ) -> Dict:
        pass


    def stop_training_entity_recognizer(
        self,
        EntityRecognizerArn: str,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        ResourceArn: str,
        Tags: List,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        ResourceArn: str,
        TagKeys: List,
    ) -> Dict:
        pass


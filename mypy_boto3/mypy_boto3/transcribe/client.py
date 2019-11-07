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


    def create_vocabulary(
        self,
        VocabularyName: str,
        LanguageCode: str,
        Phrases: Optional[List] = None,
        VocabularyFileUri: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_transcription_job(
        self,
        TranscriptionJobName: str,
    ):
        pass


    def delete_vocabulary(
        self,
        VocabularyName: str,
    ):
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


    def get_transcription_job(
        self,
        TranscriptionJobName: str,
    ) -> Dict:
        pass


    def get_vocabulary(
        self,
        VocabularyName: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_transcription_jobs(
        self,
        Status: Optional[str] = None,
        JobNameContains: Optional[str] = None,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_vocabularies(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
        StateEquals: Optional[str] = None,
        NameContains: Optional[str] = None,
    ) -> Dict:
        pass


    def start_transcription_job(
        self,
        TranscriptionJobName: str,
        LanguageCode: str,
        Media: Dict,
        MediaSampleRateHertz: Optional[int] = None,
        MediaFormat: Optional[str] = None,
        OutputBucketName: Optional[str] = None,
        OutputEncryptionKMSKeyId: Optional[str] = None,
        Settings: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_vocabulary(
        self,
        VocabularyName: str,
        LanguageCode: str,
        Phrases: Optional[List] = None,
        VocabularyFileUri: Optional[str] = None,
    ) -> Dict:
        pass


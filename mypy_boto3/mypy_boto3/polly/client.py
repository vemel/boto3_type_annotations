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


    def delete_lexicon(
        self,
        Name: str,
    ) -> Dict:
        pass


    def describe_voices(
        self,
        Engine: Optional[str] = None,
        LanguageCode: Optional[str] = None,
        IncludeAdditionalLanguageCodes: Optional[bool] = None,
        NextToken: Optional[str] = None,
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


    def get_lexicon(
        self,
        Name: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_speech_synthesis_task(
        self,
        TaskId: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_lexicons(
        self,
        NextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_speech_synthesis_tasks(
        self,
        MaxResults: Optional[int] = None,
        NextToken: Optional[str] = None,
        Status: Optional[str] = None,
    ) -> Dict:
        pass


    def put_lexicon(
        self,
        Name: str,
        Content: str,
    ) -> Dict:
        pass


    def start_speech_synthesis_task(
        self,
        OutputFormat: str,
        OutputS3BucketName: str,
        Text: str,
        VoiceId: str,
        Engine: Optional[str] = None,
        LanguageCode: Optional[str] = None,
        LexiconNames: Optional[List] = None,
        OutputS3KeyPrefix: Optional[str] = None,
        SampleRate: Optional[str] = None,
        SnsTopicArn: Optional[str] = None,
        SpeechMarkTypes: Optional[List] = None,
        TextType: Optional[str] = None,
    ) -> Dict:
        pass


    def synthesize_speech(
        self,
        OutputFormat: str,
        Text: str,
        VoiceId: str,
        Engine: Optional[str] = None,
        LanguageCode: Optional[str] = None,
        LexiconNames: Optional[List] = None,
        SampleRate: Optional[str] = None,
        SpeechMarkTypes: Optional[List] = None,
        TextType: Optional[str] = None,
    ) -> Dict:
        pass


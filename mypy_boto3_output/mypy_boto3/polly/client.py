from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_lexicon(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_voices(
        self,
        Engine: str = None,
        LanguageCode: str = None,
        IncludeAdditionalLanguageCodes: bool = None,
        NextToken: str = None,
    ) -> Dict[str, Any]:
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
    def get_lexicon(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_speech_synthesis_task(self, TaskId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_lexicons(self, NextToken: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_speech_synthesis_tasks(
        self, MaxResults: int = None, NextToken: str = None, Status: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_lexicon(self, Name: str, Content: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_speech_synthesis_task(
        self,
        OutputFormat: str,
        OutputS3BucketName: str,
        Text: str,
        VoiceId: str,
        Engine: str = None,
        LanguageCode: str = None,
        LexiconNames: List[Any] = None,
        OutputS3KeyPrefix: str = None,
        SampleRate: str = None,
        SnsTopicArn: str = None,
        SpeechMarkTypes: List[Any] = None,
        TextType: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def synthesize_speech(
        self,
        OutputFormat: str,
        Text: str,
        VoiceId: str,
        Engine: str = None,
        LanguageCode: str = None,
        LexiconNames: List[Any] = None,
        SampleRate: str = None,
        SpeechMarkTypes: List[Any] = None,
        TextType: str = None,
    ) -> Dict[str, Any]:
        pass

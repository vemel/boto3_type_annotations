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
    def create_vocabulary(
        self,
        VocabularyName: str,
        LanguageCode: str,
        Phrases: List[Any] = None,
        VocabularyFileUri: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_transcription_job(self, TranscriptionJobName: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_vocabulary(self, VocabularyName: str) -> None:
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
    def get_transcription_job(self, TranscriptionJobName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_vocabulary(self, VocabularyName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_transcription_jobs(
        self,
        Status: str = None,
        JobNameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_vocabularies(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        StateEquals: str = None,
        NameContains: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_transcription_job(
        self,
        TranscriptionJobName: str,
        LanguageCode: str,
        Media: Dict[str, Any],
        MediaSampleRateHertz: int = None,
        MediaFormat: str = None,
        OutputBucketName: str = None,
        OutputEncryptionKMSKeyId: str = None,
        Settings: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_vocabulary(
        self,
        VocabularyName: str,
        LanguageCode: str,
        Phrases: List[Any] = None,
        VocabularyFileUri: str = None,
    ) -> Dict[str, Any]:
        pass

from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_entities_detection_v2_job(self, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_phi_detection_job(self, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detect_entities(self, Text: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detect_entities_v2(self, Text: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detect_phi(self, Text: str) -> Dict[str, Any]:
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
    def list_entities_detection_v2_jobs(
        self,
        Filter: Dict[str, Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_phi_detection_jobs(
        self,
        Filter: Dict[str, Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_entities_detection_v2_job(
        self,
        InputDataConfig: Dict[str, Any],
        OutputDataConfig: Dict[str, Any],
        DataAccessRoleArn: str,
        LanguageCode: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        KMSKey: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def start_phi_detection_job(
        self,
        InputDataConfig: Dict[str, Any],
        OutputDataConfig: Dict[str, Any],
        DataAccessRoleArn: str,
        LanguageCode: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        KMSKey: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_entities_detection_v2_job(self, JobId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def stop_phi_detection_job(self, JobId: str) -> Dict[str, Any]:
        pass

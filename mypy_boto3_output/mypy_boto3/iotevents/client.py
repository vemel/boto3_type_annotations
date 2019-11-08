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
    def create_detector_model(
        self,
        detectorModelName: str,
        detectorModelDefinition: Dict[str, Any],
        roleArn: str,
        detectorModelDescription: str = None,
        key: str = None,
        tags: List[Any] = None,
        evaluationMethod: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_input(
        self,
        inputName: str,
        inputDefinition: Dict[str, Any],
        inputDescription: str = None,
        tags: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_detector_model(self, detectorModelName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_input(self, inputName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_detector_model(
        self, detectorModelName: str, detectorModelVersion: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_input(self, inputName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def describe_logging_options(self) -> Dict[str, Any]:
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
    def list_detector_model_versions(
        self, detectorModelName: str, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_detector_models(
        self, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_inputs(
        self, nextToken: str = None, maxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, resourceArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_logging_options(self, loggingOptions: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, resourceArn: str, tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_detector_model(
        self,
        detectorModelName: str,
        detectorModelDefinition: Dict[str, Any],
        roleArn: str,
        detectorModelDescription: str = None,
        evaluationMethod: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_input(
        self,
        inputName: str,
        inputDefinition: Dict[str, Any],
        inputDescription: str = None,
    ) -> Dict[str, Any]:
        pass

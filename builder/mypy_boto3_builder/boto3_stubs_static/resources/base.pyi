# pylint: disable=unused-argument,multiple-statements,super-init-not-called,unused-import,no-self-use
from __future__ import annotations

import logging
from typing import List, Dict, Any, Optional

import boto3
from boto3.resources.model import ResourceModel
from botocore.client import BaseClient

logger: logging.Logger

class ResourceMeta:
    def __init__(
        self,
        service_name: str,
        identifiers: List[str] = None,
        client: BaseClient = None,
        data: Dict = None,
        resource_model: ResourceModel = None,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def copy(self) -> ResourceMeta: ...

class ServiceResource:
    meta: ResourceMeta
    def __init__(self, client: Optional[BaseClient] = None) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

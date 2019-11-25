# pylint: disable=unused-argument,multiple-statements,super-init-not-called,no-self-use,unused-import
import logging
from functools import partial
from typing import Dict, Type, Any

from botocore.hooks import HierarchicalEmitter

from boto3.resources.action import ServiceAction
from boto3.resources.action import WaiterAction
from boto3.resources.base import ResourceMeta, ServiceResource
from boto3.resources.collection import CollectionFactory
from boto3.resources.model import ResourceModel
from boto3.resources.response import build_identifiers, ResourceHandler
from boto3.exceptions import ResourceLoadException
from boto3.utils import ServiceContext
from boto3.docs import docstring

logger: logging.Logger

class ResourceFactory:
    def __init__(self, emitter: HierarchicalEmitter) -> None: ...
    def load_from_definition(
        self,
        resource_name: str,
        single_resource_json_definition: Dict,
        service_context: ServiceContext,
    ) -> Type[ServiceResource]: ...

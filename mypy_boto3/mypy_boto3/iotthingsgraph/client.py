from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def associate_entity_to_thing(
        self,
        thingName: str,
        entityId: str,
        namespaceVersion: Optional[int] = None,
    ) -> Dict:
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def create_flow_template(
        self,
        definition: Dict,
        compatibleNamespaceVersion: Optional[int] = None,
    ) -> Dict:
        pass


    def create_system_instance(
        self,
        definition: Dict,
        target: str,
        tags: Optional[List] = None,
        greengrassGroupName: Optional[str] = None,
        s3BucketName: Optional[str] = None,
        metricsConfiguration: Optional[Dict] = None,
        flowActionsRoleArn: Optional[str] = None,
    ) -> Dict:
        pass


    def create_system_template(
        self,
        definition: Dict,
        compatibleNamespaceVersion: Optional[int] = None,
    ) -> Dict:
        pass


    def delete_flow_template(
        self,
        id: str,
    ) -> Dict:
        pass


    def delete_namespace(
        self,
    ) -> Dict:
        pass


    def delete_system_instance(
        self,
        id: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_system_template(
        self,
        id: str,
    ) -> Dict:
        pass


    def deploy_system_instance(
        self,
        id: Optional[str] = None,
    ) -> Dict:
        pass


    def deprecate_flow_template(
        self,
        id: str,
    ) -> Dict:
        pass


    def deprecate_system_template(
        self,
        id: str,
    ) -> Dict:
        pass


    def describe_namespace(
        self,
        namespaceName: Optional[str] = None,
    ) -> Dict:
        pass


    def dissociate_entity_from_thing(
        self,
        thingName: str,
        entityType: str,
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


    def get_entities(
        self,
        ids: List,
        namespaceVersion: Optional[int] = None,
    ) -> Dict:
        pass


    def get_flow_template(
        self,
        id: str,
        revisionNumber: Optional[int] = None,
    ) -> Dict:
        pass


    def get_flow_template_revisions(
        self,
        id: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_namespace_deletion_status(
        self,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_system_instance(
        self,
        id: str,
    ) -> Dict:
        pass


    def get_system_template(
        self,
        id: str,
        revisionNumber: Optional[int] = None,
    ) -> Dict:
        pass


    def get_system_template_revisions(
        self,
        id: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def get_upload_status(
        self,
        uploadId: str,
    ) -> Dict:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_flow_execution_messages(
        self,
        flowExecutionId: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags_for_resource(
        self,
        resourceArn: str,
        maxResults: Optional[int] = None,
        nextToken: Optional[str] = None,
    ) -> Dict:
        pass


    def search_entities(
        self,
        entityTypes: List,
        filters: Optional[List] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        namespaceVersion: Optional[int] = None,
    ) -> Dict:
        pass


    def search_flow_executions(
        self,
        systemInstanceId: str,
        flowExecutionId: Optional[str] = None,
        startTime: Optional[datetime] = None,
        endTime: Optional[datetime] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def search_flow_templates(
        self,
        filters: Optional[List] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def search_system_instances(
        self,
        filters: Optional[List] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def search_system_templates(
        self,
        filters: Optional[List] = None,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def search_things(
        self,
        entityId: str,
        nextToken: Optional[str] = None,
        maxResults: Optional[int] = None,
        namespaceVersion: Optional[int] = None,
    ) -> Dict:
        pass


    def tag_resource(
        self,
        resourceArn: str,
        tags: List,
    ) -> Dict:
        pass


    def undeploy_system_instance(
        self,
        id: Optional[str] = None,
    ) -> Dict:
        pass


    def untag_resource(
        self,
        resourceArn: str,
        tagKeys: List,
    ) -> Dict:
        pass


    def update_flow_template(
        self,
        id: str,
        definition: Dict,
        compatibleNamespaceVersion: Optional[int] = None,
    ) -> Dict:
        pass


    def update_system_template(
        self,
        id: str,
        definition: Dict,
        compatibleNamespaceVersion: Optional[int] = None,
    ) -> Dict:
        pass


    def upload_entity_definitions(
        self,
        document: Optional[Dict] = None,
        syncWithPublicNamespace: Optional[bool] = None,
        deprecateExistingEntities: Optional[bool] = None,
    ) -> Dict:
        pass


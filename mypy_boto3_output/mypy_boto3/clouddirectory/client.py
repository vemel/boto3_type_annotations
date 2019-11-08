from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def add_facet_to_object(
        self,
        DirectoryArn: str,
        SchemaFacet: Dict[str, Any],
        ObjectReference: Dict[str, Any],
        ObjectAttributeList: List[Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def apply_schema(
        self, PublishedSchemaArn: str, DirectoryArn: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def attach_object(
        self,
        DirectoryArn: str,
        ParentReference: Dict[str, Any],
        ChildReference: Dict[str, Any],
        LinkName: str,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def attach_policy(
        self,
        DirectoryArn: str,
        PolicyReference: Dict[str, Any],
        ObjectReference: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def attach_to_index(
        self,
        DirectoryArn: str,
        IndexReference: Dict[str, Any],
        TargetReference: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def attach_typed_link(
        self,
        DirectoryArn: str,
        SourceObjectReference: Dict[str, Any],
        TargetObjectReference: Dict[str, Any],
        TypedLinkFacet: Dict[str, Any],
        Attributes: List[Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_read(
        self, DirectoryArn: str, Operations: List[Any], ConsistencyLevel: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def batch_write(self, DirectoryArn: str, Operations: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_directory(self, Name: str, SchemaArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_facet(
        self,
        SchemaArn: str,
        Name: str,
        Attributes: List[Any] = None,
        ObjectType: str = None,
        FacetStyle: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_index(
        self,
        DirectoryArn: str,
        OrderedIndexedAttributeList: List[Any],
        IsUnique: bool,
        ParentReference: Dict[str, Any] = None,
        LinkName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_object(
        self,
        DirectoryArn: str,
        SchemaFacets: List[Any],
        ObjectAttributeList: List[Any] = None,
        ParentReference: Dict[str, Any] = None,
        LinkName: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_schema(self, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_typed_link_facet(
        self, SchemaArn: str, Facet: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_directory(self, DirectoryArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_facet(self, SchemaArn: str, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_object(
        self, DirectoryArn: str, ObjectReference: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_schema(self, SchemaArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_typed_link_facet(self, SchemaArn: str, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach_from_index(
        self,
        DirectoryArn: str,
        IndexReference: Dict[str, Any],
        TargetReference: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach_object(
        self, DirectoryArn: str, ParentReference: Dict[str, Any], LinkName: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach_policy(
        self,
        DirectoryArn: str,
        PolicyReference: Dict[str, Any],
        ObjectReference: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def detach_typed_link(
        self, DirectoryArn: str, TypedLinkSpecifier: Dict[str, Any]
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def disable_directory(self, DirectoryArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_directory(self, DirectoryArn: str) -> Dict[str, Any]:
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
    def get_applied_schema_version(self, SchemaArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_directory(self, DirectoryArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_facet(self, SchemaArn: str, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_link_attributes(
        self,
        DirectoryArn: str,
        TypedLinkSpecifier: Dict[str, Any],
        AttributeNames: List[Any],
        ConsistencyLevel: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_object_attributes(
        self,
        DirectoryArn: str,
        ObjectReference: Dict[str, Any],
        SchemaFacet: Dict[str, Any],
        AttributeNames: List[Any],
        ConsistencyLevel: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_object_information(
        self,
        DirectoryArn: str,
        ObjectReference: Dict[str, Any],
        ConsistencyLevel: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_schema_as_json(self, SchemaArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_typed_link_facet_information(
        self, SchemaArn: str, Name: str
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_applied_schema_arns(
        self,
        DirectoryArn: str,
        SchemaArn: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_attached_indices(
        self,
        DirectoryArn: str,
        TargetReference: Dict[str, Any],
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_development_schema_arns(
        self, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_directories(
        self, NextToken: str = None, MaxResults: int = None, state: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_facet_attributes(
        self, SchemaArn: str, Name: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_facet_names(
        self, SchemaArn: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_incoming_typed_links(
        self,
        DirectoryArn: str,
        ObjectReference: Dict[str, Any],
        FilterAttributeRanges: List[Any] = None,
        FilterTypedLink: Dict[str, Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_index(
        self,
        DirectoryArn: str,
        IndexReference: Dict[str, Any],
        RangesOnIndexedValues: List[Any] = None,
        MaxResults: int = None,
        NextToken: str = None,
        ConsistencyLevel: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_managed_schema_arns(
        self, SchemaArn: str = None, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_object_attributes(
        self,
        DirectoryArn: str,
        ObjectReference: Dict[str, Any],
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: str = None,
        FacetFilter: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_object_children(
        self,
        DirectoryArn: str,
        ObjectReference: Dict[str, Any],
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_object_parent_paths(
        self,
        DirectoryArn: str,
        ObjectReference: Dict[str, Any],
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_object_parents(
        self,
        DirectoryArn: str,
        ObjectReference: Dict[str, Any],
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: str = None,
        IncludeAllLinksToEachParent: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_object_policies(
        self,
        DirectoryArn: str,
        ObjectReference: Dict[str, Any],
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_outgoing_typed_links(
        self,
        DirectoryArn: str,
        ObjectReference: Dict[str, Any],
        FilterAttributeRanges: List[Any] = None,
        FilterTypedLink: Dict[str, Any] = None,
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_policy_attachments(
        self,
        DirectoryArn: str,
        PolicyReference: Dict[str, Any],
        NextToken: str = None,
        MaxResults: int = None,
        ConsistencyLevel: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_published_schema_arns(
        self, SchemaArn: str = None, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(
        self, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_typed_link_facet_attributes(
        self, SchemaArn: str, Name: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_typed_link_facet_names(
        self, SchemaArn: str, NextToken: str = None, MaxResults: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def lookup_policy(
        self,
        DirectoryArn: str,
        ObjectReference: Dict[str, Any],
        NextToken: str = None,
        MaxResults: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def publish_schema(
        self,
        DevelopmentSchemaArn: str,
        Version: str,
        MinorVersion: str = None,
        Name: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def put_schema_from_json(self, SchemaArn: str, Document: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_facet_from_object(
        self,
        DirectoryArn: str,
        SchemaFacet: Dict[str, Any],
        ObjectReference: Dict[str, Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, ResourceArn: str, Tags: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, ResourceArn: str, TagKeys: List[Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_facet(
        self,
        SchemaArn: str,
        Name: str,
        AttributeUpdates: List[Any] = None,
        ObjectType: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_link_attributes(
        self,
        DirectoryArn: str,
        TypedLinkSpecifier: Dict[str, Any],
        AttributeUpdates: List[Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_object_attributes(
        self,
        DirectoryArn: str,
        ObjectReference: Dict[str, Any],
        AttributeUpdates: List[Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_schema(self, SchemaArn: str, Name: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_typed_link_facet(
        self,
        SchemaArn: str,
        Name: str,
        AttributeUpdates: List[Any],
        IdentityAttributeOrder: List[Any],
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def upgrade_applied_schema(
        self, PublishedSchemaArn: str, DirectoryArn: str, DryRun: bool = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def upgrade_published_schema(
        self,
        DevelopmentSchemaArn: str,
        PublishedSchemaArn: str,
        MinorVersion: str,
        DryRun: bool = None,
    ) -> Dict[str, Any]:
        pass

from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.paginate import Paginator


class ListAppliedSchemaArns(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DirectoryArn: str,
        SchemaArn: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListAttachedIndices(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DirectoryArn: str,
        TargetReference: Dict[str, Any],
        ConsistencyLevel: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListDevelopmentSchemaArns(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListDirectories(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, state: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListFacetAttributes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, SchemaArn: str, Name: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListFacetNames(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, SchemaArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListIncomingTypedLinks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: Dict[str, Any],
        FilterAttributeRanges: List[Any] = None,
        FilterTypedLink: Dict[str, Any] = None,
        ConsistencyLevel: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListIndex(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DirectoryArn: str,
        IndexReference: Dict[str, Any],
        RangesOnIndexedValues: List[Any] = None,
        ConsistencyLevel: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListManagedSchemaArns(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, SchemaArn: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListObjectAttributes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: Dict[str, Any],
        ConsistencyLevel: str = None,
        FacetFilter: Dict[str, Any] = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListObjectParentPaths(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: Dict[str, Any],
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListObjectPolicies(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: Dict[str, Any],
        ConsistencyLevel: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListOutgoingTypedLinks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: Dict[str, Any],
        FilterAttributeRanges: List[Any] = None,
        FilterTypedLink: Dict[str, Any] = None,
        ConsistencyLevel: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListPolicyAttachments(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DirectoryArn: str,
        PolicyReference: Dict[str, Any],
        ConsistencyLevel: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListPublishedSchemaArns(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, SchemaArn: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTagsForResource(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, ResourceArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTypedLinkFacetAttributes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, SchemaArn: str, Name: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class ListTypedLinkFacetNames(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, SchemaArn: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class LookupPolicy(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: Dict[str, Any],
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

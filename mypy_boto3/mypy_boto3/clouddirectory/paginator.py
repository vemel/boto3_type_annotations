from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class ListAppliedSchemaArns(Paginator):
    def paginate(
        self,
        DirectoryArn: str,
        SchemaArn: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAttachedIndices(Paginator):
    def paginate(
        self,
        DirectoryArn: str,
        TargetReference: Dict,
        ConsistencyLevel: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDevelopmentSchemaArns(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDirectories(Paginator):
    def paginate(
        self,
        state: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListFacetAttributes(Paginator):
    def paginate(
        self,
        SchemaArn: str,
        Name: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListFacetNames(Paginator):
    def paginate(
        self,
        SchemaArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListIncomingTypedLinks(Paginator):
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: Dict,
        FilterAttributeRanges: Optional[List] = None,
        FilterTypedLink: Optional[Dict] = None,
        ConsistencyLevel: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListIndex(Paginator):
    def paginate(
        self,
        DirectoryArn: str,
        IndexReference: Dict,
        RangesOnIndexedValues: Optional[List] = None,
        ConsistencyLevel: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListManagedSchemaArns(Paginator):
    def paginate(
        self,
        SchemaArn: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListObjectAttributes(Paginator):
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: Dict,
        ConsistencyLevel: Optional[str] = None,
        FacetFilter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListObjectParentPaths(Paginator):
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: Dict,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListObjectPolicies(Paginator):
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: Dict,
        ConsistencyLevel: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListOutgoingTypedLinks(Paginator):
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: Dict,
        FilterAttributeRanges: Optional[List] = None,
        FilterTypedLink: Optional[Dict] = None,
        ConsistencyLevel: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPolicyAttachments(Paginator):
    def paginate(
        self,
        DirectoryArn: str,
        PolicyReference: Dict,
        ConsistencyLevel: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPublishedSchemaArns(Paginator):
    def paginate(
        self,
        SchemaArn: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTagsForResource(Paginator):
    def paginate(
        self,
        ResourceArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTypedLinkFacetAttributes(Paginator):
    def paginate(
        self,
        SchemaArn: str,
        Name: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTypedLinkFacetNames(Paginator):
    def paginate(
        self,
        SchemaArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class LookupPolicy(Paginator):
    def paginate(
        self,
        DirectoryArn: str,
        ObjectReference: Dict,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


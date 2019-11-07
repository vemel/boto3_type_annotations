from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class DescribeImageScanFindings(Paginator):
    def paginate(
        self,
        repositoryName: str,
        imageId: Dict,
        registryId: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeImages(Paginator):
    def paginate(
        self,
        repositoryName: str,
        registryId: Optional[str] = None,
        imageIds: Optional[List] = None,
        filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class DescribeRepositories(Paginator):
    def paginate(
        self,
        registryId: Optional[str] = None,
        repositoryNames: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetLifecyclePolicyPreview(Paginator):
    def paginate(
        self,
        repositoryName: str,
        registryId: Optional[str] = None,
        imageIds: Optional[List] = None,
        filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListImages(Paginator):
    def paginate(
        self,
        repositoryName: str,
        registryId: Optional[str] = None,
        filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListAliases(Paginator):
    def paginate(
        self,
        FunctionName: str,
        FunctionVersion: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListEventSourceMappings(Paginator):
    def paginate(
        self,
        EventSourceArn: Optional[str] = None,
        FunctionName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListFunctions(Paginator):
    def paginate(
        self,
        MasterRegion: Optional[str] = None,
        FunctionVersion: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListLayerVersions(Paginator):
    def paginate(
        self,
        LayerName: str,
        CompatibleRuntime: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListLayers(Paginator):
    def paginate(
        self,
        CompatibleRuntime: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListVersionsByFunction(Paginator):
    def paginate(
        self,
        FunctionName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


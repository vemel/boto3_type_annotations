from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListCollections(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListFaces(Paginator):
    def paginate(
        self,
        CollectionId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListStreamProcessors(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


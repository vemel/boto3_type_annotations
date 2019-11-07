from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListCreatedArtifacts(Paginator):
    def paginate(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDiscoveredResources(Paginator):
    def paginate(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListMigrationTasks(Paginator):
    def paginate(
        self,
        ResourceName: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListProgressUpdateStreams(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


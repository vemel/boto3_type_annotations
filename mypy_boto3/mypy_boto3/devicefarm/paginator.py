from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class GetOfferingStatus(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListArtifacts(Paginator):
    def paginate(
        self,
        arn: str,
        type: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDeviceInstances(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDevicePools(Paginator):
    def paginate(
        self,
        arn: str,
        type: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDevices(Paginator):
    def paginate(
        self,
        arn: Optional[str] = None,
        filters: Optional[List] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListInstanceProfiles(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListJobs(Paginator):
    def paginate(
        self,
        arn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListNetworkProfiles(Paginator):
    def paginate(
        self,
        arn: str,
        type: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListOfferingPromotions(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListOfferingTransactions(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListOfferings(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListProjects(Paginator):
    def paginate(
        self,
        arn: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListRemoteAccessSessions(Paginator):
    def paginate(
        self,
        arn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListRuns(Paginator):
    def paginate(
        self,
        arn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSamples(Paginator):
    def paginate(
        self,
        arn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSuites(Paginator):
    def paginate(
        self,
        arn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTests(Paginator):
    def paginate(
        self,
        arn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListUniqueProblems(Paginator):
    def paginate(
        self,
        arn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListUploads(Paginator):
    def paginate(
        self,
        arn: str,
        type: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListVPCEConfigurations(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


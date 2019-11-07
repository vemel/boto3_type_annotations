from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class DescribeSchedule(Paginator):
    def paginate(
        self,
        ChannelId: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListChannels(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListInputSecurityGroups(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListInputs(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListOfferings(Paginator):
    def paginate(
        self,
        ChannelClass: Optional[str] = None,
        ChannelConfiguration: Optional[str] = None,
        Codec: Optional[str] = None,
        MaximumBitrate: Optional[str] = None,
        MaximumFramerate: Optional[str] = None,
        Resolution: Optional[str] = None,
        ResourceType: Optional[str] = None,
        SpecialFeature: Optional[str] = None,
        VideoQuality: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListReservations(Paginator):
    def paginate(
        self,
        ChannelClass: Optional[str] = None,
        Codec: Optional[str] = None,
        MaximumBitrate: Optional[str] = None,
        MaximumFramerate: Optional[str] = None,
        Resolution: Optional[str] = None,
        ResourceType: Optional[str] = None,
        SpecialFeature: Optional[str] = None,
        VideoQuality: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


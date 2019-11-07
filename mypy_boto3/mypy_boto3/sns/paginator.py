from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListEndpointsByPlatformApplication(Paginator):
    def paginate(
        self,
        PlatformApplicationArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPhoneNumbersOptedOut(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListPlatformApplications(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSubscriptions(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSubscriptionsByTopic(Paginator):
    def paginate(
        self,
        TopicArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTopics(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


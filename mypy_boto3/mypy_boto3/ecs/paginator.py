from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListAccountSettings(Paginator):
    def paginate(
        self,
        name: Optional[str] = None,
        value: Optional[str] = None,
        principalArn: Optional[str] = None,
        effectiveSettings: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAttributes(Paginator):
    def paginate(
        self,
        targetType: str,
        cluster: Optional[str] = None,
        attributeName: Optional[str] = None,
        attributeValue: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListClusters(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListContainerInstances(Paginator):
    def paginate(
        self,
        cluster: Optional[str] = None,
        filter: Optional[str] = None,
        status: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListServices(Paginator):
    def paginate(
        self,
        cluster: Optional[str] = None,
        launchType: Optional[str] = None,
        schedulingStrategy: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTaskDefinitionFamilies(Paginator):
    def paginate(
        self,
        familyPrefix: Optional[str] = None,
        status: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTaskDefinitions(Paginator):
    def paginate(
        self,
        familyPrefix: Optional[str] = None,
        status: Optional[str] = None,
        sort: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTasks(Paginator):
    def paginate(
        self,
        cluster: Optional[str] = None,
        containerInstance: Optional[str] = None,
        family: Optional[str] = None,
        startedBy: Optional[str] = None,
        serviceName: Optional[str] = None,
        desiredStatus: Optional[str] = None,
        launchType: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


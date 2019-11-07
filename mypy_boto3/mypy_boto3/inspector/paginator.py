from typing import Dict
from typing import List
from typing import Optional

from botocore.paginate import Paginator


class ListAssessmentRunAgents(Paginator):
    def paginate(
        self,
        assessmentRunArn: str,
        filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAssessmentRuns(Paginator):
    def paginate(
        self,
        assessmentTemplateArns: Optional[List] = None,
        filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAssessmentTargets(Paginator):
    def paginate(
        self,
        filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListAssessmentTemplates(Paginator):
    def paginate(
        self,
        assessmentTargetArns: Optional[List] = None,
        filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListEventSubscriptions(Paginator):
    def paginate(
        self,
        resourceArn: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListExclusions(Paginator):
    def paginate(
        self,
        assessmentRunArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListFindings(Paginator):
    def paginate(
        self,
        assessmentRunArns: Optional[List] = None,
        filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListRulesPackages(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class PreviewAgents(Paginator):
    def paginate(
        self,
        previewAgentsArn: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class ListDocumentClassificationJobs(Paginator):
    def paginate(
        self,
        Filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDocumentClassifiers(Paginator):
    def paginate(
        self,
        Filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListDominantLanguageDetectionJobs(Paginator):
    def paginate(
        self,
        Filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListEntitiesDetectionJobs(Paginator):
    def paginate(
        self,
        Filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListEntityRecognizers(Paginator):
    def paginate(
        self,
        Filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListKeyPhrasesDetectionJobs(Paginator):
    def paginate(
        self,
        Filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSentimentDetectionJobs(Paginator):
    def paginate(
        self,
        Filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListTopicsDetectionJobs(Paginator):
    def paginate(
        self,
        Filter: Optional[Dict] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


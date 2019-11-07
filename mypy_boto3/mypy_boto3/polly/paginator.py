from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class DescribeVoices(Paginator):
    def paginate(
        self,
        Engine: Optional[str] = None,
        LanguageCode: Optional[str] = None,
        IncludeAdditionalLanguageCodes: Optional[bool] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListLexicons(Paginator):
    def paginate(
        self,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class ListSpeechSynthesisTasks(Paginator):
    def paginate(
        self,
        Status: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


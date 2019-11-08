from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class DescribeVoices(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        Engine: str = None,
        LanguageCode: str = None,
        IncludeAdditionalLanguageCodes: bool = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class ListLexicons(Paginator):

    # pylint: disable=arguments-differ
    def paginate(self, PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
        pass


class ListSpeechSynthesisTasks(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, Status: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

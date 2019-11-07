from typing import Dict
from typing import Optional

from botocore.paginate import Paginator


class GetBotAliases(Paginator):
    def paginate(
        self,
        botName: str,
        nameContains: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetBotChannelAssociations(Paginator):
    def paginate(
        self,
        botName: str,
        botAlias: str,
        nameContains: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetBotVersions(Paginator):
    def paginate(
        self,
        name: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetBots(Paginator):
    def paginate(
        self,
        nameContains: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetBuiltinIntents(Paginator):
    def paginate(
        self,
        locale: Optional[str] = None,
        signatureContains: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetBuiltinSlotTypes(Paginator):
    def paginate(
        self,
        locale: Optional[str] = None,
        signatureContains: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetIntentVersions(Paginator):
    def paginate(
        self,
        name: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetIntents(Paginator):
    def paginate(
        self,
        nameContains: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetSlotTypeVersions(Paginator):
    def paginate(
        self,
        name: str,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass



class GetSlotTypes(Paginator):
    def paginate(
        self,
        nameContains: Optional[str] = None,
        PaginationConfig: Optional[Dict] = None,
    ) -> Dict:
        pass


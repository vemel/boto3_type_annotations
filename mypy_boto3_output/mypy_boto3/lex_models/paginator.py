from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.paginate import Paginator


class GetBotAliases(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        botName: str,
        nameContains: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetBotChannelAssociations(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        botName: str,
        botAlias: str,
        nameContains: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetBotVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, name: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetBots(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, nameContains: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetBuiltinIntents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        locale: str = None,
        signatureContains: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetBuiltinSlotTypes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self,
        locale: str = None,
        signatureContains: str = None,
        PaginationConfig: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass


class GetIntentVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, name: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetIntents(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, nameContains: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetSlotTypeVersions(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, name: str, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass


class GetSlotTypes(Paginator):

    # pylint: disable=arguments-differ
    def paginate(
        self, nameContains: str = None, PaginationConfig: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        pass

from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def check_domain_availability(
        self, DomainName: str, IdnLangCode: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def check_domain_transferability(
        self, DomainName: str, AuthCode: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_tags_for_domain(
        self, DomainName: str, TagsToDelete: List[Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disable_domain_auto_renew(self, DomainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def disable_domain_transfer_lock(self, DomainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_domain_auto_renew(self, DomainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def enable_domain_transfer_lock(self, DomainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def generate_presigned_url(
        self,
        ClientMethod: str = None,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = None,
        HttpMethod: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def get_contact_reachability_status(self, domainName: str = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_domain_detail(self, DomainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_domain_suggestions(
        self, DomainName: str, SuggestionCount: int, OnlyAvailable: bool
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_operation_detail(self, OperationId: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_domains(self, Marker: str = None, MaxItems: int = None) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_operations(
        self, SubmittedSince: datetime = None, Marker: str = None, MaxItems: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_domain(self, DomainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def register_domain(
        self,
        DomainName: str,
        DurationInYears: int,
        AdminContact: Dict[str, Any],
        RegistrantContact: Dict[str, Any],
        TechContact: Dict[str, Any],
        IdnLangCode: str = None,
        AutoRenew: bool = None,
        PrivacyProtectAdminContact: bool = None,
        PrivacyProtectRegistrantContact: bool = None,
        PrivacyProtectTechContact: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def renew_domain(
        self, DomainName: str, CurrentExpiryYear: int, DurationInYears: int = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def resend_contact_reachability_email(
        self, domainName: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def retrieve_domain_auth_code(self, DomainName: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def transfer_domain(
        self,
        DomainName: str,
        DurationInYears: int,
        AdminContact: Dict[str, Any],
        RegistrantContact: Dict[str, Any],
        TechContact: Dict[str, Any],
        IdnLangCode: str = None,
        Nameservers: List[Any] = None,
        AuthCode: str = None,
        AutoRenew: bool = None,
        PrivacyProtectAdminContact: bool = None,
        PrivacyProtectRegistrantContact: bool = None,
        PrivacyProtectTechContact: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_domain_contact(
        self,
        DomainName: str,
        AdminContact: Dict[str, Any] = None,
        RegistrantContact: Dict[str, Any] = None,
        TechContact: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_domain_contact_privacy(
        self,
        DomainName: str,
        AdminPrivacy: bool = None,
        RegistrantPrivacy: bool = None,
        TechPrivacy: bool = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_domain_nameservers(
        self, DomainName: str, Nameservers: List[Any], FIAuthKey: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_tags_for_domain(
        self, DomainName: str, TagsToUpdate: List[Any] = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def view_billing(
        self,
        Start: datetime = None,
        End: datetime = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> Dict[str, Any]:
        pass

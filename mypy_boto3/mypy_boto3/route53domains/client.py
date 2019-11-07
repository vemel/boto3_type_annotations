from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def check_domain_availability(
        self,
        DomainName: str,
        IdnLangCode: Optional[str] = None,
    ) -> Dict:
        pass


    def check_domain_transferability(
        self,
        DomainName: str,
        AuthCode: Optional[str] = None,
    ) -> Dict:
        pass


    def delete_tags_for_domain(
        self,
        DomainName: str,
        TagsToDelete: List,
    ) -> Dict:
        pass


    def disable_domain_auto_renew(
        self,
        DomainName: str,
    ) -> Dict:
        pass


    def disable_domain_transfer_lock(
        self,
        DomainName: str,
    ) -> Dict:
        pass


    def enable_domain_auto_renew(
        self,
        DomainName: str,
    ) -> Dict:
        pass


    def enable_domain_transfer_lock(
        self,
        DomainName: str,
    ) -> Dict:
        pass


    def generate_presigned_url(
        self,
        ClientMethod: Optional[str] = None,
        Params: Optional[Dict] = None,
        ExpiresIn: Optional[int] = None,
        HttpMethod: Optional[str] = None,
    ):
        pass


    def get_contact_reachability_status(
        self,
        domainName: Optional[str] = None,
    ) -> Dict:
        pass


    def get_domain_detail(
        self,
        DomainName: str,
    ) -> Dict:
        pass


    def get_domain_suggestions(
        self,
        DomainName: str,
        SuggestionCount: int,
        OnlyAvailable: bool,
    ) -> Dict:
        pass


    def get_operation_detail(
        self,
        OperationId: str,
    ) -> Dict:
        pass


    def get_paginator(
        self,
        operation_name: Optional[str] = None,
    ) -> Paginator:
        pass


    def get_waiter(
        self,
        waiter_name: Optional[str] = None,
    ) -> Waiter:
        pass


    def list_domains(
        self,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_operations(
        self,
        SubmittedSince: Optional[datetime] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags_for_domain(
        self,
        DomainName: str,
    ) -> Dict:
        pass


    def register_domain(
        self,
        DomainName: str,
        DurationInYears: int,
        AdminContact: Dict,
        RegistrantContact: Dict,
        TechContact: Dict,
        IdnLangCode: Optional[str] = None,
        AutoRenew: Optional[bool] = None,
        PrivacyProtectAdminContact: Optional[bool] = None,
        PrivacyProtectRegistrantContact: Optional[bool] = None,
        PrivacyProtectTechContact: Optional[bool] = None,
    ) -> Dict:
        pass


    def renew_domain(
        self,
        DomainName: str,
        CurrentExpiryYear: int,
        DurationInYears: Optional[int] = None,
    ) -> Dict:
        pass


    def resend_contact_reachability_email(
        self,
        domainName: Optional[str] = None,
    ) -> Dict:
        pass


    def retrieve_domain_auth_code(
        self,
        DomainName: str,
    ) -> Dict:
        pass


    def transfer_domain(
        self,
        DomainName: str,
        DurationInYears: int,
        AdminContact: Dict,
        RegistrantContact: Dict,
        TechContact: Dict,
        IdnLangCode: Optional[str] = None,
        Nameservers: Optional[List] = None,
        AuthCode: Optional[str] = None,
        AutoRenew: Optional[bool] = None,
        PrivacyProtectAdminContact: Optional[bool] = None,
        PrivacyProtectRegistrantContact: Optional[bool] = None,
        PrivacyProtectTechContact: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_domain_contact(
        self,
        DomainName: str,
        AdminContact: Optional[Dict] = None,
        RegistrantContact: Optional[Dict] = None,
        TechContact: Optional[Dict] = None,
    ) -> Dict:
        pass


    def update_domain_contact_privacy(
        self,
        DomainName: str,
        AdminPrivacy: Optional[bool] = None,
        RegistrantPrivacy: Optional[bool] = None,
        TechPrivacy: Optional[bool] = None,
    ) -> Dict:
        pass


    def update_domain_nameservers(
        self,
        DomainName: str,
        Nameservers: List,
        FIAuthKey: Optional[str] = None,
    ) -> Dict:
        pass


    def update_tags_for_domain(
        self,
        DomainName: str,
        TagsToUpdate: Optional[List] = None,
    ) -> Dict:
        pass


    def view_billing(
        self,
        Start: Optional[datetime] = None,
        End: Optional[datetime] = None,
        Marker: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from botocore.client import BaseClient



class Client(BaseClient):
    def add_tags_to_certificate(
        self,
        CertificateArn: str,
        Tags: List,
    ):
        pass


    def can_paginate(
        self,
        operation_name: Optional[str] = None,
    ):
        pass


    def delete_certificate(
        self,
        CertificateArn: str,
    ):
        pass


    def describe_certificate(
        self,
        CertificateArn: str,
    ) -> Dict:
        pass


    def export_certificate(
        self,
        CertificateArn: str,
        Passphrase: bytes,
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


    def get_certificate(
        self,
        CertificateArn: str,
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


    def import_certificate(
        self,
        Certificate: bytes,
        PrivateKey: bytes,
        CertificateArn: Optional[str] = None,
        CertificateChain: Optional[bytes] = None,
    ) -> Dict:
        pass


    def list_certificates(
        self,
        CertificateStatuses: Optional[List] = None,
        Includes: Optional[Dict] = None,
        NextToken: Optional[str] = None,
        MaxItems: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags_for_certificate(
        self,
        CertificateArn: str,
    ) -> Dict:
        pass


    def remove_tags_from_certificate(
        self,
        CertificateArn: str,
        Tags: List,
    ):
        pass


    def renew_certificate(
        self,
        CertificateArn: str,
    ):
        pass


    def request_certificate(
        self,
        DomainName: str,
        ValidationMethod: Optional[str] = None,
        SubjectAlternativeNames: Optional[List] = None,
        IdempotencyToken: Optional[str] = None,
        DomainValidationOptions: Optional[List] = None,
        Options: Optional[Dict] = None,
        CertificateAuthorityArn: Optional[str] = None,
    ) -> Dict:
        pass


    def resend_validation_email(
        self,
        CertificateArn: str,
        Domain: str,
        ValidationDomain: str,
    ):
        pass


    def update_certificate_options(
        self,
        CertificateArn: str,
        Options: Dict,
    ):
        pass


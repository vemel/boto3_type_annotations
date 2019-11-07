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


    def create_certificate_authority(
        self,
        CertificateAuthorityConfiguration: Dict,
        CertificateAuthorityType: str,
        RevocationConfiguration: Optional[Dict] = None,
        IdempotencyToken: Optional[str] = None,
        Tags: Optional[List] = None,
    ) -> Dict:
        pass


    def create_certificate_authority_audit_report(
        self,
        CertificateAuthorityArn: str,
        S3BucketName: str,
        AuditReportResponseFormat: str,
    ) -> Dict:
        pass


    def create_permission(
        self,
        CertificateAuthorityArn: str,
        Principal: str,
        Actions: List,
        SourceAccount: Optional[str] = None,
    ):
        pass


    def delete_certificate_authority(
        self,
        CertificateAuthorityArn: str,
        PermanentDeletionTimeInDays: Optional[int] = None,
    ):
        pass


    def delete_permission(
        self,
        CertificateAuthorityArn: str,
        Principal: str,
        SourceAccount: Optional[str] = None,
    ):
        pass


    def describe_certificate_authority(
        self,
        CertificateAuthorityArn: str,
    ) -> Dict:
        pass


    def describe_certificate_authority_audit_report(
        self,
        CertificateAuthorityArn: str,
        AuditReportId: str,
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
        CertificateAuthorityArn: str,
        CertificateArn: str,
    ) -> Dict:
        pass


    def get_certificate_authority_certificate(
        self,
        CertificateAuthorityArn: str,
    ) -> Dict:
        pass


    def get_certificate_authority_csr(
        self,
        CertificateAuthorityArn: str,
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


    def import_certificate_authority_certificate(
        self,
        CertificateAuthorityArn: str,
        Certificate: bytes,
        CertificateChain: Optional[bytes] = None,
    ):
        pass


    def issue_certificate(
        self,
        CertificateAuthorityArn: str,
        Csr: bytes,
        SigningAlgorithm: str,
        Validity: Dict,
        TemplateArn: Optional[str] = None,
        IdempotencyToken: Optional[str] = None,
    ) -> Dict:
        pass


    def list_certificate_authorities(
        self,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_permissions(
        self,
        CertificateAuthorityArn: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def list_tags(
        self,
        CertificateAuthorityArn: str,
        NextToken: Optional[str] = None,
        MaxResults: Optional[int] = None,
    ) -> Dict:
        pass


    def restore_certificate_authority(
        self,
        CertificateAuthorityArn: str,
    ):
        pass


    def revoke_certificate(
        self,
        CertificateAuthorityArn: str,
        CertificateSerial: str,
        RevocationReason: str,
    ):
        pass


    def tag_certificate_authority(
        self,
        CertificateAuthorityArn: str,
        Tags: List,
    ):
        pass


    def untag_certificate_authority(
        self,
        CertificateAuthorityArn: str,
        Tags: List,
    ):
        pass


    def update_certificate_authority(
        self,
        CertificateAuthorityArn: str,
        RevocationConfiguration: Optional[Dict] = None,
        Status: Optional[str] = None,
    ):
        pass


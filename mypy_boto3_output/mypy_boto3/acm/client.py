from __future__ import annotations

from typing import Any
from typing import Dict
from typing import List

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def add_tags_to_certificate(self, CertificateArn: str, Tags: List[Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_certificate(self, CertificateArn: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def describe_certificate(self, CertificateArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def export_certificate(
        self, CertificateArn: str, Passphrase: bytes
    ) -> Dict[str, Any]:
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
    def get_certificate(self, CertificateArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def import_certificate(
        self,
        Certificate: bytes,
        PrivateKey: bytes,
        CertificateArn: str = None,
        CertificateChain: bytes = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_certificates(
        self,
        CertificateStatuses: List[Any] = None,
        Includes: Dict[str, Any] = None,
        NextToken: str = None,
        MaxItems: int = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_certificate(self, CertificateArn: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def remove_tags_from_certificate(
        self, CertificateArn: str, Tags: List[Any]
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def renew_certificate(self, CertificateArn: str) -> None:
        pass

    # pylint: disable=arguments-differ
    def request_certificate(
        self,
        DomainName: str,
        ValidationMethod: str = None,
        SubjectAlternativeNames: List[Any] = None,
        IdempotencyToken: str = None,
        DomainValidationOptions: List[Any] = None,
        Options: Dict[str, Any] = None,
        CertificateAuthorityArn: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def resend_validation_email(
        self, CertificateArn: str, Domain: str, ValidationDomain: str
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_certificate_options(
        self, CertificateArn: str, Options: Dict[str, Any]
    ) -> None:
        pass

from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.client import BaseClient
from botocore.paginate import Paginator
from botocore.waiter import Waiter


class Client(BaseClient):

    # pylint: disable=arguments-differ
    def can_paginate(self, operation_name: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def create_cloud_front_origin_access_identity(
        self, CloudFrontOriginAccessIdentityConfig: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_distribution(self, DistributionConfig: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_distribution_with_tags(
        self, DistributionConfigWithTags: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_field_level_encryption_config(
        self, FieldLevelEncryptionConfig: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_field_level_encryption_profile(
        self, FieldLevelEncryptionProfileConfig: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_invalidation(
        self, DistributionId: str, InvalidationBatch: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_public_key(self, PublicKeyConfig: Dict[str, Any]) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_streaming_distribution(
        self, StreamingDistributionConfig: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def create_streaming_distribution_with_tags(
        self, StreamingDistributionConfigWithTags: Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def delete_cloud_front_origin_access_identity(
        self, Id: str, IfMatch: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_distribution(self, Id: str, IfMatch: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_field_level_encryption_config(
        self, Id: str, IfMatch: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_field_level_encryption_profile(
        self, Id: str, IfMatch: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_public_key(self, Id: str, IfMatch: str = None) -> None:
        pass

    # pylint: disable=arguments-differ
    def delete_streaming_distribution(self, Id: str, IfMatch: str = None) -> None:
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
    def get_cloud_front_origin_access_identity(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_cloud_front_origin_access_identity_config(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_distribution(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_distribution_config(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_field_level_encryption(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_field_level_encryption_config(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_field_level_encryption_profile(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_field_level_encryption_profile_config(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_invalidation(self, DistributionId: str, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    # pylint: disable=arguments-differ
    def get_public_key(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_public_key_config(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_streaming_distribution(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_streaming_distribution_config(self, Id: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    # pylint: disable=arguments-differ
    def list_cloud_front_origin_access_identities(
        self, Marker: str = None, MaxItems: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_distributions(
        self, Marker: str = None, MaxItems: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_distributions_by_web_acl_id(
        self, WebACLId: str, Marker: str = None, MaxItems: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_field_level_encryption_configs(
        self, Marker: str = None, MaxItems: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_field_level_encryption_profiles(
        self, Marker: str = None, MaxItems: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_invalidations(
        self, DistributionId: str, Marker: str = None, MaxItems: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_public_keys(
        self, Marker: str = None, MaxItems: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_streaming_distributions(
        self, Marker: str = None, MaxItems: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def list_tags_for_resource(self, Resource: str) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def tag_resource(self, Resource: str, Tags: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def untag_resource(self, Resource: str, TagKeys: Dict[str, Any]) -> None:
        pass

    # pylint: disable=arguments-differ
    def update_cloud_front_origin_access_identity(
        self,
        CloudFrontOriginAccessIdentityConfig: Dict[str, Any],
        Id: str,
        IfMatch: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_distribution(
        self, DistributionConfig: Dict[str, Any], Id: str, IfMatch: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_field_level_encryption_config(
        self, FieldLevelEncryptionConfig: Dict[str, Any], Id: str, IfMatch: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_field_level_encryption_profile(
        self,
        FieldLevelEncryptionProfileConfig: Dict[str, Any],
        Id: str,
        IfMatch: str = None,
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_public_key(
        self, PublicKeyConfig: Dict[str, Any], Id: str, IfMatch: str = None
    ) -> Dict[str, Any]:
        pass

    # pylint: disable=arguments-differ
    def update_streaming_distribution(
        self, StreamingDistributionConfig: Dict[str, Any], Id: str, IfMatch: str = None
    ) -> Dict[str, Any]:
        pass

"Main interface for cloudfront type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef",
    "ClientCreateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef",
    "ClientCreateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityTypeDef",
    "ClientCreateCloudFrontOriginAccessIdentityResponseTypeDef",
    "ClientCreateDistributionDistributionConfigAliasesTypeDef",
    "ClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef",
    "ClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef",
    "ClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeadersTypeDef",
    "ClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef",
    "ClientCreateDistributionDistributionConfigDefaultCacheBehaviorTypeDef",
    "ClientCreateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaStatusCodesTypeDef",
    "ClientCreateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaTypeDef",
    "ClientCreateDistributionDistributionConfigOriginGroupsItemsMembersItemsTypeDef",
    "ClientCreateDistributionDistributionConfigOriginGroupsItemsMembersTypeDef",
    "ClientCreateDistributionDistributionConfigOriginGroupsItemsTypeDef",
    "ClientCreateDistributionDistributionConfigOriginGroupsTypeDef",
    "ClientCreateDistributionDistributionConfigOriginsItemsCustomHeadersItemsTypeDef",
    "ClientCreateDistributionDistributionConfigOriginsItemsCustomHeadersTypeDef",
    "ClientCreateDistributionDistributionConfigOriginsItemsCustomOriginConfigOriginSslProtocolsTypeDef",
    "ClientCreateDistributionDistributionConfigOriginsItemsCustomOriginConfigTypeDef",
    "ClientCreateDistributionDistributionConfigOriginsItemsS3OriginConfigTypeDef",
    "ClientCreateDistributionDistributionConfigOriginsItemsTypeDef",
    "ClientCreateDistributionDistributionConfigOriginsTypeDef",
    "ClientCreateDistributionDistributionConfigTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigAliasesTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesHeadersTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsFailoverCriteriaStatusCodesTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsFailoverCriteriaTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsMembersItemsTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsMembersTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomHeadersItemsTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomHeadersTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomOriginConfigOriginSslProtocolsTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomOriginConfigTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsS3OriginConfigTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigTypeDef",
    "ClientCreateDistributionWithTagsDistributionConfigWithTagsTypeDef",
    "ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef",
    "ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef",
    "ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef",
    "ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef",
    "ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef",
    "ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef",
    "ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigTypeDef",
    "ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef",
    "ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef",
    "ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef",
    "ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef",
    "ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef",
    "ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef",
    "ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigTypeDef",
    "ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionTypeDef",
    "ClientCreateFieldLevelEncryptionConfigResponseTypeDef",
    "ClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef",
    "ClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef",
    "ClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef",
    "ClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef",
    "ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef",
    "ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef",
    "ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef",
    "ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef",
    "ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileTypeDef",
    "ClientCreateFieldLevelEncryptionProfileResponseTypeDef",
    "ClientCreateInvalidationInvalidationBatchPathsTypeDef",
    "ClientCreateInvalidationInvalidationBatchTypeDef",
    "ClientCreateInvalidationResponseInvalidationInvalidationBatchPathsTypeDef",
    "ClientCreateInvalidationResponseInvalidationInvalidationBatchTypeDef",
    "ClientCreateInvalidationResponseInvalidationTypeDef",
    "ClientCreateInvalidationResponseTypeDef",
    "ClientCreatePublicKeyPublicKeyConfigTypeDef",
    "ClientCreatePublicKeyResponsePublicKeyPublicKeyConfigTypeDef",
    "ClientCreatePublicKeyResponsePublicKeyTypeDef",
    "ClientCreatePublicKeyResponseTypeDef",
    "ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef",
    "ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsTypeDef",
    "ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersTypeDef",
    "ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef",
    "ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef",
    "ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef",
    "ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef",
    "ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTypeDef",
    "ClientCreateStreamingDistributionResponseStreamingDistributionTypeDef",
    "ClientCreateStreamingDistributionResponseTypeDef",
    "ClientCreateStreamingDistributionStreamingDistributionConfigAliasesTypeDef",
    "ClientCreateStreamingDistributionStreamingDistributionConfigLoggingTypeDef",
    "ClientCreateStreamingDistributionStreamingDistributionConfigS3OriginTypeDef",
    "ClientCreateStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef",
    "ClientCreateStreamingDistributionStreamingDistributionConfigTypeDef",
    "ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef",
    "ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersItemsTypeDef",
    "ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersTypeDef",
    "ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef",
    "ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef",
    "ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef",
    "ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef",
    "ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigTypeDef",
    "ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionTypeDef",
    "ClientCreateStreamingDistributionWithTagsResponseTypeDef",
    "ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigAliasesTypeDef",
    "ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigLoggingTypeDef",
    "ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigS3OriginTypeDef",
    "ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigTrustedSignersTypeDef",
    "ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigTypeDef",
    "ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTagsItemsTypeDef",
    "ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTagsTypeDef",
    "ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTypeDef",
    "ClientGetCloudFrontOriginAccessIdentityConfigResponseCloudFrontOriginAccessIdentityConfigTypeDef",
    "ClientGetCloudFrontOriginAccessIdentityConfigResponseTypeDef",
    "ClientGetCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef",
    "ClientGetCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityTypeDef",
    "ClientGetCloudFrontOriginAccessIdentityResponseTypeDef",
    "ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef",
    "ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef",
    "ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef",
    "ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef",
    "ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef",
    "ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef",
    "ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigTypeDef",
    "ClientGetFieldLevelEncryptionConfigResponseTypeDef",
    "ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef",
    "ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef",
    "ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef",
    "ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigTypeDef",
    "ClientGetFieldLevelEncryptionProfileConfigResponseTypeDef",
    "ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef",
    "ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef",
    "ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef",
    "ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef",
    "ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileTypeDef",
    "ClientGetFieldLevelEncryptionProfileResponseTypeDef",
    "ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef",
    "ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef",
    "ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef",
    "ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef",
    "ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef",
    "ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef",
    "ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigTypeDef",
    "ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionTypeDef",
    "ClientGetFieldLevelEncryptionResponseTypeDef",
    "ClientGetInvalidationResponseInvalidationInvalidationBatchPathsTypeDef",
    "ClientGetInvalidationResponseInvalidationInvalidationBatchTypeDef",
    "ClientGetInvalidationResponseInvalidationTypeDef",
    "ClientGetInvalidationResponseTypeDef",
    "ClientGetPublicKeyConfigResponsePublicKeyConfigTypeDef",
    "ClientGetPublicKeyConfigResponseTypeDef",
    "ClientGetPublicKeyResponsePublicKeyPublicKeyConfigTypeDef",
    "ClientGetPublicKeyResponsePublicKeyTypeDef",
    "ClientGetPublicKeyResponseTypeDef",
    "ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigAliasesTypeDef",
    "ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigLoggingTypeDef",
    "ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigS3OriginTypeDef",
    "ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigTrustedSignersTypeDef",
    "ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigTypeDef",
    "ClientGetStreamingDistributionConfigResponseTypeDef",
    "ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef",
    "ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsTypeDef",
    "ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersTypeDef",
    "ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef",
    "ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef",
    "ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef",
    "ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef",
    "ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTypeDef",
    "ClientGetStreamingDistributionResponseStreamingDistributionTypeDef",
    "ClientGetStreamingDistributionResponseTypeDef",
    "ClientListCloudFrontOriginAccessIdentitiesResponseCloudFrontOriginAccessIdentityListItemsTypeDef",
    "ClientListCloudFrontOriginAccessIdentitiesResponseCloudFrontOriginAccessIdentityListTypeDef",
    "ClientListCloudFrontOriginAccessIdentitiesResponseTypeDef",
    "ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigContentTypeProfilesItemsTypeDef",
    "ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigContentTypeProfilesTypeDef",
    "ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigTypeDef",
    "ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigQueryArgProfilesItemsTypeDef",
    "ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigQueryArgProfilesTypeDef",
    "ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigTypeDef",
    "ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsTypeDef",
    "ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListTypeDef",
    "ClientListFieldLevelEncryptionConfigsResponseTypeDef",
    "ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesItemsFieldPatternsTypeDef",
    "ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesItemsTypeDef",
    "ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesTypeDef",
    "ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsTypeDef",
    "ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListTypeDef",
    "ClientListFieldLevelEncryptionProfilesResponseTypeDef",
    "ClientListInvalidationsResponseInvalidationListItemsTypeDef",
    "ClientListInvalidationsResponseInvalidationListTypeDef",
    "ClientListInvalidationsResponseTypeDef",
    "ClientListPublicKeysResponsePublicKeyListItemsTypeDef",
    "ClientListPublicKeysResponsePublicKeyListTypeDef",
    "ClientListPublicKeysResponseTypeDef",
    "ClientListStreamingDistributionsResponseStreamingDistributionListItemsAliasesTypeDef",
    "ClientListStreamingDistributionsResponseStreamingDistributionListItemsS3OriginTypeDef",
    "ClientListStreamingDistributionsResponseStreamingDistributionListItemsTrustedSignersTypeDef",
    "ClientListStreamingDistributionsResponseStreamingDistributionListItemsTypeDef",
    "ClientListStreamingDistributionsResponseStreamingDistributionListTypeDef",
    "ClientListStreamingDistributionsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsItemsTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientTagResourceTagsItemsTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUntagResourceTagKeysTypeDef",
    "ClientUpdateCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef",
    "ClientUpdateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef",
    "ClientUpdateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityTypeDef",
    "ClientUpdateCloudFrontOriginAccessIdentityResponseTypeDef",
    "ClientUpdateDistributionDistributionConfigAliasesTypeDef",
    "ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef",
    "ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef",
    "ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeadersTypeDef",
    "ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef",
    "ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorTypeDef",
    "ClientUpdateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaStatusCodesTypeDef",
    "ClientUpdateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaTypeDef",
    "ClientUpdateDistributionDistributionConfigOriginGroupsItemsMembersItemsTypeDef",
    "ClientUpdateDistributionDistributionConfigOriginGroupsItemsMembersTypeDef",
    "ClientUpdateDistributionDistributionConfigOriginGroupsItemsTypeDef",
    "ClientUpdateDistributionDistributionConfigOriginGroupsTypeDef",
    "ClientUpdateDistributionDistributionConfigOriginsItemsCustomHeadersItemsTypeDef",
    "ClientUpdateDistributionDistributionConfigOriginsItemsCustomHeadersTypeDef",
    "ClientUpdateDistributionDistributionConfigOriginsItemsCustomOriginConfigOriginSslProtocolsTypeDef",
    "ClientUpdateDistributionDistributionConfigOriginsItemsCustomOriginConfigTypeDef",
    "ClientUpdateDistributionDistributionConfigOriginsItemsS3OriginConfigTypeDef",
    "ClientUpdateDistributionDistributionConfigOriginsItemsTypeDef",
    "ClientUpdateDistributionDistributionConfigOriginsTypeDef",
    "ClientUpdateDistributionDistributionConfigTypeDef",
    "ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef",
    "ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef",
    "ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef",
    "ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef",
    "ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef",
    "ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef",
    "ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigTypeDef",
    "ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef",
    "ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef",
    "ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef",
    "ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef",
    "ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef",
    "ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef",
    "ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigTypeDef",
    "ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionTypeDef",
    "ClientUpdateFieldLevelEncryptionConfigResponseTypeDef",
    "ClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef",
    "ClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef",
    "ClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef",
    "ClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef",
    "ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef",
    "ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef",
    "ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef",
    "ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef",
    "ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileTypeDef",
    "ClientUpdateFieldLevelEncryptionProfileResponseTypeDef",
    "ClientUpdatePublicKeyPublicKeyConfigTypeDef",
    "ClientUpdatePublicKeyResponsePublicKeyPublicKeyConfigTypeDef",
    "ClientUpdatePublicKeyResponsePublicKeyTypeDef",
    "ClientUpdatePublicKeyResponseTypeDef",
    "ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef",
    "ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsTypeDef",
    "ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersTypeDef",
    "ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef",
    "ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef",
    "ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef",
    "ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef",
    "ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTypeDef",
    "ClientUpdateStreamingDistributionResponseStreamingDistributionTypeDef",
    "ClientUpdateStreamingDistributionResponseTypeDef",
    "ClientUpdateStreamingDistributionStreamingDistributionConfigAliasesTypeDef",
    "ClientUpdateStreamingDistributionStreamingDistributionConfigLoggingTypeDef",
    "ClientUpdateStreamingDistributionStreamingDistributionConfigS3OriginTypeDef",
    "ClientUpdateStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef",
    "ClientUpdateStreamingDistributionStreamingDistributionConfigTypeDef",
    "DistributionDeployedWaitWaiterConfigTypeDef",
    "InvalidationCompletedWaitWaiterConfigTypeDef",
    "ListCloudFrontOriginAccessIdentitiesPaginatePaginationConfigTypeDef",
    "ListCloudFrontOriginAccessIdentitiesPaginateResponseCloudFrontOriginAccessIdentityListItemsTypeDef",
    "ListCloudFrontOriginAccessIdentitiesPaginateResponseCloudFrontOriginAccessIdentityListTypeDef",
    "ListCloudFrontOriginAccessIdentitiesPaginateResponseTypeDef",
    "ListDistributionsPaginatePaginationConfigTypeDef",
    "ListInvalidationsPaginatePaginationConfigTypeDef",
    "ListInvalidationsPaginateResponseInvalidationListItemsTypeDef",
    "ListInvalidationsPaginateResponseInvalidationListTypeDef",
    "ListInvalidationsPaginateResponseTypeDef",
    "ListStreamingDistributionsPaginatePaginationConfigTypeDef",
    "ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsAliasesTypeDef",
    "ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsS3OriginTypeDef",
    "ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsTrustedSignersTypeDef",
    "ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsTypeDef",
    "ListStreamingDistributionsPaginateResponseStreamingDistributionListTypeDef",
    "ListStreamingDistributionsPaginateResponseTypeDef",
    "StreamingDistributionDeployedWaitWaiterConfigTypeDef",
)


_ClientCreateCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef = TypedDict(
    "_ClientCreateCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef",
    {"CallerReference": str, "Comment": str},
)


class ClientCreateCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef(
    _ClientCreateCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef
):
    """
    Type definition for `ClientCreateCloudFrontOriginAccessIdentity` `CloudFrontOriginAccessIdentityConfig`

    The current configuration information for the identity.

    - **CallerReference** *(string) --* **[REQUIRED]**

      A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.

      If the value of ``CallerReference`` is new (regardless of the content of the
      ``CloudFrontOriginAccessIdentityConfig`` object), a new origin access identity is created.

      If the ``CallerReference`` is a value already sent in a previous identity request, and the
      content of the ``CloudFrontOriginAccessIdentityConfig`` is identical to the original request
      (ignoring white space), the response includes the same information returned to the original
      request.

      If the ``CallerReference`` is a value you already sent in a previous request to create an
      identity, but the content of the ``CloudFrontOriginAccessIdentityConfig`` is different from the
      original request, CloudFront returns a ``CloudFrontOriginAccessIdentityAlreadyExists`` error.

    - **Comment** *(string) --* **[REQUIRED]**

      Any comments you want to include about the origin access identity.
    """


_ClientCreateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef = TypedDict(
    "_ClientCreateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef",
    {"CallerReference": str, "Comment": str},
    total=False,
)


class ClientCreateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef(
    _ClientCreateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef
):
    """
    Type definition for `ClientCreateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentity` `CloudFrontOriginAccessIdentityConfig`

    The current configuration information for the identity.

    - **CallerReference** *(string) --*

      A unique value (for example, a date-time stamp) that ensures that the request can't be
      replayed.

      If the value of ``CallerReference`` is new (regardless of the content of the
      ``CloudFrontOriginAccessIdentityConfig`` object), a new origin access identity is created.

      If the ``CallerReference`` is a value already sent in a previous identity request, and
      the content of the ``CloudFrontOriginAccessIdentityConfig`` is identical to the original
      request (ignoring white space), the response includes the same information returned to
      the original request.

      If the ``CallerReference`` is a value you already sent in a previous request to create an
      identity, but the content of the ``CloudFrontOriginAccessIdentityConfig`` is different
      from the original request, CloudFront returns a
      ``CloudFrontOriginAccessIdentityAlreadyExists`` error.

    - **Comment** *(string) --*

      Any comments you want to include about the origin access identity.
    """


_ClientCreateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityTypeDef = TypedDict(
    "_ClientCreateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityTypeDef",
    {
        "Id": str,
        "S3CanonicalUserId": str,
        "CloudFrontOriginAccessIdentityConfig": ClientCreateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef,
    },
    total=False,
)


class ClientCreateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityTypeDef(
    _ClientCreateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityTypeDef
):
    """
    Type definition for `ClientCreateCloudFrontOriginAccessIdentityResponse` `CloudFrontOriginAccessIdentity`

    The origin access identity's information.

    - **Id** *(string) --*

      The ID for the origin access identity, for example, ``E74FTE3AJFJ256A`` .

    - **S3CanonicalUserId** *(string) --*

      The Amazon S3 canonical user ID for the origin access identity, used when giving the origin
      access identity read permission to an object in Amazon S3.

    - **CloudFrontOriginAccessIdentityConfig** *(dict) --*

      The current configuration information for the identity.

      - **CallerReference** *(string) --*

        A unique value (for example, a date-time stamp) that ensures that the request can't be
        replayed.

        If the value of ``CallerReference`` is new (regardless of the content of the
        ``CloudFrontOriginAccessIdentityConfig`` object), a new origin access identity is created.

        If the ``CallerReference`` is a value already sent in a previous identity request, and
        the content of the ``CloudFrontOriginAccessIdentityConfig`` is identical to the original
        request (ignoring white space), the response includes the same information returned to
        the original request.

        If the ``CallerReference`` is a value you already sent in a previous request to create an
        identity, but the content of the ``CloudFrontOriginAccessIdentityConfig`` is different
        from the original request, CloudFront returns a
        ``CloudFrontOriginAccessIdentityAlreadyExists`` error.

      - **Comment** *(string) --*

        Any comments you want to include about the origin access identity.
    """


_ClientCreateCloudFrontOriginAccessIdentityResponseTypeDef = TypedDict(
    "_ClientCreateCloudFrontOriginAccessIdentityResponseTypeDef",
    {
        "CloudFrontOriginAccessIdentity": ClientCreateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityTypeDef,
        "Location": str,
        "ETag": str,
    },
    total=False,
)


class ClientCreateCloudFrontOriginAccessIdentityResponseTypeDef(
    _ClientCreateCloudFrontOriginAccessIdentityResponseTypeDef
):
    """
    Type definition for `ClientCreateCloudFrontOriginAccessIdentity` `Response`

    The returned result of the corresponding request.

    - **CloudFrontOriginAccessIdentity** *(dict) --*

      The origin access identity's information.

      - **Id** *(string) --*

        The ID for the origin access identity, for example, ``E74FTE3AJFJ256A`` .

      - **S3CanonicalUserId** *(string) --*

        The Amazon S3 canonical user ID for the origin access identity, used when giving the origin
        access identity read permission to an object in Amazon S3.

      - **CloudFrontOriginAccessIdentityConfig** *(dict) --*

        The current configuration information for the identity.

        - **CallerReference** *(string) --*

          A unique value (for example, a date-time stamp) that ensures that the request can't be
          replayed.

          If the value of ``CallerReference`` is new (regardless of the content of the
          ``CloudFrontOriginAccessIdentityConfig`` object), a new origin access identity is created.

          If the ``CallerReference`` is a value already sent in a previous identity request, and
          the content of the ``CloudFrontOriginAccessIdentityConfig`` is identical to the original
          request (ignoring white space), the response includes the same information returned to
          the original request.

          If the ``CallerReference`` is a value you already sent in a previous request to create an
          identity, but the content of the ``CloudFrontOriginAccessIdentityConfig`` is different
          from the original request, CloudFront returns a
          ``CloudFrontOriginAccessIdentityAlreadyExists`` error.

        - **Comment** *(string) --*

          Any comments you want to include about the origin access identity.

    - **Location** *(string) --*

      The fully qualified URI of the new origin access identity just created. For example:
      ``https://cloudfront.amazonaws.com/2010-11-01/origin-access-identity/cloudfront/E74FTE3AJFJ256A``
      .

    - **ETag** *(string) --*

      The current version of the origin access identity created.
    """


_RequiredClientCreateDistributionDistributionConfigAliasesTypeDef = TypedDict(
    "_RequiredClientCreateDistributionDistributionConfigAliasesTypeDef",
    {"Quantity": int},
)
_OptionalClientCreateDistributionDistributionConfigAliasesTypeDef = TypedDict(
    "_OptionalClientCreateDistributionDistributionConfigAliasesTypeDef",
    {"Items": List[str]},
    total=False,
)


class ClientCreateDistributionDistributionConfigAliasesTypeDef(
    _RequiredClientCreateDistributionDistributionConfigAliasesTypeDef,
    _OptionalClientCreateDistributionDistributionConfigAliasesTypeDef,
):
    """
    Type definition for `ClientCreateDistributionDistributionConfig` `Aliases`

    A complex type that contains information about CNAMEs (alternate domain names), if any, for
    this distribution.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of CNAME aliases, if any, that you want to associate with this distribution.

    - **Items** *(list) --*

      A complex type that contains the CNAME aliases, if any, that you want to associate with this
      distribution.

      - *(string) --*
    """


_RequiredClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef = TypedDict(
    "_RequiredClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef",
    {"Quantity": int},
)
_OptionalClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef = TypedDict(
    "_OptionalClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef",
    {"Items": List[str]},
    total=False,
)


class ClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef(
    _RequiredClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef,
    _OptionalClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef,
):
    """
    Type definition for `ClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies` `WhitelistedNames`

    Required if you specify ``whitelist`` for the value of ``Forward:`` . A complex type that
    specifies how many different cookies you want CloudFront to forward to the origin for
    this cache behavior and, if you want to forward selected cookies, the names of those
    cookies.

    If you specify ``all`` or none for the value of ``Forward`` , omit ``WhitelistedNames`` .
    If you change the value of ``Forward`` from ``whitelist`` to all or none and you don't
    delete the ``WhitelistedNames`` element and its child elements, CloudFront deletes them
    automatically.

    For the current limit on the number of cookie names that you can whitelist for each cache
    behavior, see `CloudFront Limits
    <https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront>`__
    in the *AWS General Reference* .

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of different cookies that you want CloudFront to forward to the origin for
      this cache behavior.

    - **Items** *(list) --*

      A complex type that contains one ``Name`` element for each cookie that you want
      CloudFront to forward to the origin for this cache behavior.

      - *(string) --*
    """


_RequiredClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef = TypedDict(
    "_RequiredClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef",
    {"Forward": str},
)
_OptionalClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef = TypedDict(
    "_OptionalClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef",
    {
        "WhitelistedNames": ClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef
    },
    total=False,
)


class ClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef(
    _RequiredClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef,
    _OptionalClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef,
):
    """
    Type definition for `ClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValues` `Cookies`

    A complex type that specifies whether you want CloudFront to forward cookies to the origin
    and, if so, which ones. For more information about forwarding cookies to the origin, see
    `How CloudFront Forwards, Caches, and Logs Cookies
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html>`__ in the
    *Amazon CloudFront Developer Guide* .

    - **Forward** *(string) --* **[REQUIRED]**

      Specifies which cookies to forward to the origin for this cache behavior: all, none, or
      the list of cookies specified in the ``WhitelistedNames`` complex type.

      Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an
      Amazon S3 origin, specify none for the ``Forward`` element.

    - **WhitelistedNames** *(dict) --*

      Required if you specify ``whitelist`` for the value of ``Forward:`` . A complex type that
      specifies how many different cookies you want CloudFront to forward to the origin for
      this cache behavior and, if you want to forward selected cookies, the names of those
      cookies.

      If you specify ``all`` or none for the value of ``Forward`` , omit ``WhitelistedNames`` .
      If you change the value of ``Forward`` from ``whitelist`` to all or none and you don't
      delete the ``WhitelistedNames`` element and its child elements, CloudFront deletes them
      automatically.

      For the current limit on the number of cookie names that you can whitelist for each cache
      behavior, see `CloudFront Limits
      <https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront>`__
      in the *AWS General Reference* .

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of different cookies that you want CloudFront to forward to the origin for
        this cache behavior.

      - **Items** *(list) --*

        A complex type that contains one ``Name`` element for each cookie that you want
        CloudFront to forward to the origin for this cache behavior.

        - *(string) --*
    """


_ClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeadersTypeDef = TypedDict(
    "_ClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeadersTypeDef",
    {"Quantity": int},
)


class ClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeadersTypeDef(
    _ClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeadersTypeDef
):
    """
    Type definition for `ClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValues` `Headers`

    A complex type that specifies the ``Headers`` , if any, that you want CloudFront to forward
    to the origin for this cache behavior (whitelisted headers). For the headers that you
    specify, CloudFront also caches separate versions of a specified object that is based on
    the header values in viewer requests.

    For more information, see `Caching Content Based on Request Headers
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html>`__
    in the *Amazon CloudFront Developer Guide* .

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of different headers that you want CloudFront to base caching on for this
      cache behavior. You can configure each cache behavior in a web distribution to do one of
      the following:

      * **Forward all headers to your origin** : Specify ``1`` for ``Quantity`` and ``*`` for
      ``Name`` .

      .. warning::

         CloudFront doesn't cache the objects that are associated with this cache behavior.
         Instead, CloudFront sends every request to the origin.

      * **Forward a whitelist of headers you specify** : Specify the number of headers that you
      want CloudFront to base caching on. Then specify the header names in ``Name`` elements.
      CloudFront caches your objects based on the values in the specified headers.

      * **Forward only the default headers** : Specify ``0`` for ``Quantity`` and omit
      ``Items`` . In this configuration, CloudFront doesn't cache based on the values in the
      request headers.

      Regardless of which option you choose, CloudFront forwards headers to your origin based
      on whether the origin is an S3 bucket or a custom origin. See the following documentation:

      * **S3 bucket** : See `HTTP Request Headers That CloudFront Removes or Updates
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorS3Origin.html#request-s3-removed-headers>`__
    """


_RequiredClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef = TypedDict(
    "_RequiredClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef",
    {
        "QueryString": bool,
        "Cookies": ClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef,
    },
)
_OptionalClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef = TypedDict(
    "_OptionalClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef",
    {
        "Headers": ClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeadersTypeDef
    },
    total=False,
)


class ClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef(
    _RequiredClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef,
    _OptionalClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef,
):
    """
    Type definition for `ClientCreateDistributionDistributionConfigDefaultCacheBehavior` `ForwardedValues`

    A complex type that specifies how CloudFront handles query strings and cookies.

    - **QueryString** *(boolean) --* **[REQUIRED]**

      Indicates whether you want CloudFront to forward query strings to the origin that is
      associated with this cache behavior and cache based on the query string parameters.
      CloudFront behavior depends on the value of ``QueryString`` and on the values that you
      specify for ``QueryStringCacheKeys`` , if any:

      If you specify true for ``QueryString`` and you don't specify any values for
      ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin
      and caches based on all query string parameters. Depending on how many query string
      parameters and values you have, this can adversely affect performance because CloudFront
      must forward more requests to the origin.

      If you specify true for ``QueryString`` and you specify one or more values for
      ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin,
      but it only caches based on the query string parameters that you specify.

      If you specify false for ``QueryString`` , CloudFront doesn't forward any query string
      parameters to the origin, and doesn't cache based on query string parameters.

      For more information, see `Configuring CloudFront to Cache Based on Query String Parameters
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html>`__
      in the *Amazon CloudFront Developer Guide* .

    - **Cookies** *(dict) --* **[REQUIRED]**

      A complex type that specifies whether you want CloudFront to forward cookies to the origin
      and, if so, which ones. For more information about forwarding cookies to the origin, see
      `How CloudFront Forwards, Caches, and Logs Cookies
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html>`__ in the
      *Amazon CloudFront Developer Guide* .

      - **Forward** *(string) --* **[REQUIRED]**

        Specifies which cookies to forward to the origin for this cache behavior: all, none, or
        the list of cookies specified in the ``WhitelistedNames`` complex type.

        Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an
        Amazon S3 origin, specify none for the ``Forward`` element.

      - **WhitelistedNames** *(dict) --*

        Required if you specify ``whitelist`` for the value of ``Forward:`` . A complex type that
        specifies how many different cookies you want CloudFront to forward to the origin for
        this cache behavior and, if you want to forward selected cookies, the names of those
        cookies.

        If you specify ``all`` or none for the value of ``Forward`` , omit ``WhitelistedNames`` .
        If you change the value of ``Forward`` from ``whitelist`` to all or none and you don't
        delete the ``WhitelistedNames`` element and its child elements, CloudFront deletes them
        automatically.

        For the current limit on the number of cookie names that you can whitelist for each cache
        behavior, see `CloudFront Limits
        <https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront>`__
        in the *AWS General Reference* .

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of different cookies that you want CloudFront to forward to the origin for
          this cache behavior.

        - **Items** *(list) --*

          A complex type that contains one ``Name`` element for each cookie that you want
          CloudFront to forward to the origin for this cache behavior.

          - *(string) --*

    - **Headers** *(dict) --*

      A complex type that specifies the ``Headers`` , if any, that you want CloudFront to forward
      to the origin for this cache behavior (whitelisted headers). For the headers that you
      specify, CloudFront also caches separate versions of a specified object that is based on
      the header values in viewer requests.

      For more information, see `Caching Content Based on Request Headers
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html>`__
      in the *Amazon CloudFront Developer Guide* .

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of different headers that you want CloudFront to base caching on for this
        cache behavior. You can configure each cache behavior in a web distribution to do one of
        the following:

        * **Forward all headers to your origin** : Specify ``1`` for ``Quantity`` and ``*`` for
        ``Name`` .

        .. warning::

           CloudFront doesn't cache the objects that are associated with this cache behavior.
           Instead, CloudFront sends every request to the origin.

        * **Forward a whitelist of headers you specify** : Specify the number of headers that you
        want CloudFront to base caching on. Then specify the header names in ``Name`` elements.
        CloudFront caches your objects based on the values in the specified headers.

        * **Forward only the default headers** : Specify ``0`` for ``Quantity`` and omit
        ``Items`` . In this configuration, CloudFront doesn't cache based on the values in the
        request headers.

        Regardless of which option you choose, CloudFront forwards headers to your origin based
        on whether the origin is an S3 bucket or a custom origin. See the following documentation:

        * **S3 bucket** : See `HTTP Request Headers That CloudFront Removes or Updates
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorS3Origin.html#request-s3-removed-headers>`__
    """


_ClientCreateDistributionDistributionConfigDefaultCacheBehaviorTypeDef = TypedDict(
    "_ClientCreateDistributionDistributionConfigDefaultCacheBehaviorTypeDef",
    {
        "TargetOriginId": str,
        "ForwardedValues": ClientCreateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef,
    },
)


class ClientCreateDistributionDistributionConfigDefaultCacheBehaviorTypeDef(
    _ClientCreateDistributionDistributionConfigDefaultCacheBehaviorTypeDef
):
    """
    Type definition for `ClientCreateDistributionDistributionConfig` `DefaultCacheBehavior`

    A complex type that describes the default cache behavior if you don't specify a
    ``CacheBehavior`` element or if files don't match any of the values of ``PathPattern`` in
    ``CacheBehavior`` elements. You must create exactly one default cache behavior.

    - **TargetOriginId** *(string) --* **[REQUIRED]**

      The value of ``ID`` for the origin that you want CloudFront to route requests to when a
      request matches the path pattern either for a cache behavior or for the default cache
      behavior in your distribution.

    - **ForwardedValues** *(dict) --* **[REQUIRED]**

      A complex type that specifies how CloudFront handles query strings and cookies.

      - **QueryString** *(boolean) --* **[REQUIRED]**

        Indicates whether you want CloudFront to forward query strings to the origin that is
        associated with this cache behavior and cache based on the query string parameters.
        CloudFront behavior depends on the value of ``QueryString`` and on the values that you
        specify for ``QueryStringCacheKeys`` , if any:

        If you specify true for ``QueryString`` and you don't specify any values for
        ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin
        and caches based on all query string parameters. Depending on how many query string
        parameters and values you have, this can adversely affect performance because CloudFront
        must forward more requests to the origin.

        If you specify true for ``QueryString`` and you specify one or more values for
        ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin,
        but it only caches based on the query string parameters that you specify.

        If you specify false for ``QueryString`` , CloudFront doesn't forward any query string
        parameters to the origin, and doesn't cache based on query string parameters.

        For more information, see `Configuring CloudFront to Cache Based on Query String Parameters
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html>`__
        in the *Amazon CloudFront Developer Guide* .

      - **Cookies** *(dict) --* **[REQUIRED]**

        A complex type that specifies whether you want CloudFront to forward cookies to the origin
        and, if so, which ones. For more information about forwarding cookies to the origin, see
        `How CloudFront Forwards, Caches, and Logs Cookies
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html>`__ in the
        *Amazon CloudFront Developer Guide* .

        - **Forward** *(string) --* **[REQUIRED]**

          Specifies which cookies to forward to the origin for this cache behavior: all, none, or
          the list of cookies specified in the ``WhitelistedNames`` complex type.

          Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an
          Amazon S3 origin, specify none for the ``Forward`` element.

        - **WhitelistedNames** *(dict) --*

          Required if you specify ``whitelist`` for the value of ``Forward:`` . A complex type that
          specifies how many different cookies you want CloudFront to forward to the origin for
          this cache behavior and, if you want to forward selected cookies, the names of those
          cookies.

          If you specify ``all`` or none for the value of ``Forward`` , omit ``WhitelistedNames`` .
          If you change the value of ``Forward`` from ``whitelist`` to all or none and you don't
          delete the ``WhitelistedNames`` element and its child elements, CloudFront deletes them
          automatically.

          For the current limit on the number of cookie names that you can whitelist for each cache
          behavior, see `CloudFront Limits
          <https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront>`__
          in the *AWS General Reference* .

          - **Quantity** *(integer) --* **[REQUIRED]**

            The number of different cookies that you want CloudFront to forward to the origin for
            this cache behavior.

          - **Items** *(list) --*

            A complex type that contains one ``Name`` element for each cookie that you want
            CloudFront to forward to the origin for this cache behavior.

            - *(string) --*

      - **Headers** *(dict) --*

        A complex type that specifies the ``Headers`` , if any, that you want CloudFront to forward
        to the origin for this cache behavior (whitelisted headers). For the headers that you
        specify, CloudFront also caches separate versions of a specified object that is based on
        the header values in viewer requests.

        For more information, see `Caching Content Based on Request Headers
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html>`__
        in the *Amazon CloudFront Developer Guide* .

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of different headers that you want CloudFront to base caching on for this
          cache behavior. You can configure each cache behavior in a web distribution to do one of
          the following:

          * **Forward all headers to your origin** : Specify ``1`` for ``Quantity`` and ``*`` for
          ``Name`` .

          .. warning::

             CloudFront doesn't cache the objects that are associated with this cache behavior.
             Instead, CloudFront sends every request to the origin.

          * **Forward a whitelist of headers you specify** : Specify the number of headers that you
          want CloudFront to base caching on. Then specify the header names in ``Name`` elements.
          CloudFront caches your objects based on the values in the specified headers.

          * **Forward only the default headers** : Specify ``0`` for ``Quantity`` and omit
          ``Items`` . In this configuration, CloudFront doesn't cache based on the values in the
          request headers.

          Regardless of which option you choose, CloudFront forwards headers to your origin based
          on whether the origin is an S3 bucket or a custom origin. See the following documentation:

          * **S3 bucket** : See `HTTP Request Headers That CloudFront Removes or Updates
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorS3Origin.html#request-s3-removed-headers>`__
    """


_ClientCreateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaStatusCodesTypeDef = TypedDict(
    "_ClientCreateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaStatusCodesTypeDef",
    {"Quantity": int, "Items": List[int]},
)


class ClientCreateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaStatusCodesTypeDef(
    _ClientCreateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaStatusCodesTypeDef
):
    """
    Type definition for `ClientCreateDistributionDistributionConfigOriginGroupsItemsFailoverCriteria` `StatusCodes`

    The status codes that, when returned from the primary origin, will trigger CloudFront
    to failover to the second origin.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of status codes.

    - **Items** *(list) --* **[REQUIRED]**

      The items (status codes) for an origin group.

      - *(integer) --*
    """


_ClientCreateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaTypeDef = TypedDict(
    "_ClientCreateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaTypeDef",
    {
        "StatusCodes": ClientCreateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaStatusCodesTypeDef
    },
)


class ClientCreateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaTypeDef(
    _ClientCreateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaTypeDef
):
    """
    Type definition for `ClientCreateDistributionDistributionConfigOriginGroupsItems` `FailoverCriteria`

    A complex type that contains information about the failover criteria for an origin group.

    - **StatusCodes** *(dict) --* **[REQUIRED]**

      The status codes that, when returned from the primary origin, will trigger CloudFront
      to failover to the second origin.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of status codes.

      - **Items** *(list) --* **[REQUIRED]**

        The items (status codes) for an origin group.

        - *(integer) --*
    """


_ClientCreateDistributionDistributionConfigOriginGroupsItemsMembersItemsTypeDef = TypedDict(
    "_ClientCreateDistributionDistributionConfigOriginGroupsItemsMembersItemsTypeDef",
    {"OriginId": str},
)


class ClientCreateDistributionDistributionConfigOriginGroupsItemsMembersItemsTypeDef(
    _ClientCreateDistributionDistributionConfigOriginGroupsItemsMembersItemsTypeDef
):
    """
    Type definition for `ClientCreateDistributionDistributionConfigOriginGroupsItemsMembers` `Items`

    An origin in an origin group.

    - **OriginId** *(string) --* **[REQUIRED]**

      The ID for an origin in an origin group.
    """


_ClientCreateDistributionDistributionConfigOriginGroupsItemsMembersTypeDef = TypedDict(
    "_ClientCreateDistributionDistributionConfigOriginGroupsItemsMembersTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientCreateDistributionDistributionConfigOriginGroupsItemsMembersItemsTypeDef
        ],
    },
)


class ClientCreateDistributionDistributionConfigOriginGroupsItemsMembersTypeDef(
    _ClientCreateDistributionDistributionConfigOriginGroupsItemsMembersTypeDef
):
    """
    Type definition for `ClientCreateDistributionDistributionConfigOriginGroupsItems` `Members`

    A complex type that contains information about the origins in an origin group.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of origins in an origin group.

    - **Items** *(list) --* **[REQUIRED]**

      Items (origins) in an origin group.

      - *(dict) --*

        An origin in an origin group.

        - **OriginId** *(string) --* **[REQUIRED]**

          The ID for an origin in an origin group.
    """


_ClientCreateDistributionDistributionConfigOriginGroupsItemsTypeDef = TypedDict(
    "_ClientCreateDistributionDistributionConfigOriginGroupsItemsTypeDef",
    {
        "Id": str,
        "FailoverCriteria": ClientCreateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaTypeDef,
        "Members": ClientCreateDistributionDistributionConfigOriginGroupsItemsMembersTypeDef,
    },
)


class ClientCreateDistributionDistributionConfigOriginGroupsItemsTypeDef(
    _ClientCreateDistributionDistributionConfigOriginGroupsItemsTypeDef
):
    """
    Type definition for `ClientCreateDistributionDistributionConfigOriginGroups` `Items`

    An origin group includes two origins (a primary origin and a second origin to failover to)
    and a failover criteria that you specify. You create an origin group to support origin
    failover in CloudFront. When you create or update a distribution, you can specifiy the
    origin group instead of a single origin, and CloudFront will failover from the primary
    origin to the second origin under the failover conditions that you've chosen.

    - **Id** *(string) --* **[REQUIRED]**

      The origin group's ID.

    - **FailoverCriteria** *(dict) --* **[REQUIRED]**

      A complex type that contains information about the failover criteria for an origin group.

      - **StatusCodes** *(dict) --* **[REQUIRED]**

        The status codes that, when returned from the primary origin, will trigger CloudFront
        to failover to the second origin.

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of status codes.

        - **Items** *(list) --* **[REQUIRED]**

          The items (status codes) for an origin group.

          - *(integer) --*

    - **Members** *(dict) --* **[REQUIRED]**

      A complex type that contains information about the origins in an origin group.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of origins in an origin group.

      - **Items** *(list) --* **[REQUIRED]**

        Items (origins) in an origin group.

        - *(dict) --*

          An origin in an origin group.

          - **OriginId** *(string) --* **[REQUIRED]**

            The ID for an origin in an origin group.
    """


_RequiredClientCreateDistributionDistributionConfigOriginGroupsTypeDef = TypedDict(
    "_RequiredClientCreateDistributionDistributionConfigOriginGroupsTypeDef",
    {"Quantity": int},
)
_OptionalClientCreateDistributionDistributionConfigOriginGroupsTypeDef = TypedDict(
    "_OptionalClientCreateDistributionDistributionConfigOriginGroupsTypeDef",
    {"Items": List[ClientCreateDistributionDistributionConfigOriginGroupsItemsTypeDef]},
    total=False,
)


class ClientCreateDistributionDistributionConfigOriginGroupsTypeDef(
    _RequiredClientCreateDistributionDistributionConfigOriginGroupsTypeDef,
    _OptionalClientCreateDistributionDistributionConfigOriginGroupsTypeDef,
):
    """
    Type definition for `ClientCreateDistributionDistributionConfig` `OriginGroups`

    A complex type that contains information about origin groups for this distribution.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of origin groups.

    - **Items** *(list) --*

      The items (origin groups) in a distribution.

      - *(dict) --*

        An origin group includes two origins (a primary origin and a second origin to failover to)
        and a failover criteria that you specify. You create an origin group to support origin
        failover in CloudFront. When you create or update a distribution, you can specifiy the
        origin group instead of a single origin, and CloudFront will failover from the primary
        origin to the second origin under the failover conditions that you've chosen.

        - **Id** *(string) --* **[REQUIRED]**

          The origin group's ID.

        - **FailoverCriteria** *(dict) --* **[REQUIRED]**

          A complex type that contains information about the failover criteria for an origin group.

          - **StatusCodes** *(dict) --* **[REQUIRED]**

            The status codes that, when returned from the primary origin, will trigger CloudFront
            to failover to the second origin.

            - **Quantity** *(integer) --* **[REQUIRED]**

              The number of status codes.

            - **Items** *(list) --* **[REQUIRED]**

              The items (status codes) for an origin group.

              - *(integer) --*

        - **Members** *(dict) --* **[REQUIRED]**

          A complex type that contains information about the origins in an origin group.

          - **Quantity** *(integer) --* **[REQUIRED]**

            The number of origins in an origin group.

          - **Items** *(list) --* **[REQUIRED]**

            Items (origins) in an origin group.

            - *(dict) --*

              An origin in an origin group.

              - **OriginId** *(string) --* **[REQUIRED]**

                The ID for an origin in an origin group.
    """


_ClientCreateDistributionDistributionConfigOriginsItemsCustomHeadersItemsTypeDef = TypedDict(
    "_ClientCreateDistributionDistributionConfigOriginsItemsCustomHeadersItemsTypeDef",
    {"HeaderName": str, "HeaderValue": str},
)


class ClientCreateDistributionDistributionConfigOriginsItemsCustomHeadersItemsTypeDef(
    _ClientCreateDistributionDistributionConfigOriginsItemsCustomHeadersItemsTypeDef
):
    """
    Type definition for `ClientCreateDistributionDistributionConfigOriginsItemsCustomHeaders` `Items`

    A complex type that contains ``HeaderName`` and ``HeaderValue`` elements, if any, for
    this distribution.

    - **HeaderName** *(string) --* **[REQUIRED]**

      The name of a header that you want CloudFront to forward to your origin. For more
      information, see `Forwarding Custom Headers to Your Origin (Web Distributions Only)
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html>`__
      in the *Amazon CloudFront Developer Guide* .

    - **HeaderValue** *(string) --* **[REQUIRED]**

      The value for the header that you specified in the ``HeaderName`` field.
    """


_RequiredClientCreateDistributionDistributionConfigOriginsItemsCustomHeadersTypeDef = TypedDict(
    "_RequiredClientCreateDistributionDistributionConfigOriginsItemsCustomHeadersTypeDef",
    {"Quantity": int},
)
_OptionalClientCreateDistributionDistributionConfigOriginsItemsCustomHeadersTypeDef = TypedDict(
    "_OptionalClientCreateDistributionDistributionConfigOriginsItemsCustomHeadersTypeDef",
    {
        "Items": List[
            ClientCreateDistributionDistributionConfigOriginsItemsCustomHeadersItemsTypeDef
        ]
    },
    total=False,
)


class ClientCreateDistributionDistributionConfigOriginsItemsCustomHeadersTypeDef(
    _RequiredClientCreateDistributionDistributionConfigOriginsItemsCustomHeadersTypeDef,
    _OptionalClientCreateDistributionDistributionConfigOriginsItemsCustomHeadersTypeDef,
):
    """
    Type definition for `ClientCreateDistributionDistributionConfigOriginsItems` `CustomHeaders`

    A complex type that contains names and values for the custom headers that you want.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of custom headers, if any, for this distribution.

    - **Items** *(list) --*

       **Optional** : A list that contains one ``OriginCustomHeader`` element for each custom
       header that you want CloudFront to forward to the origin. If Quantity is ``0`` , omit
       ``Items`` .

      - *(dict) --*

        A complex type that contains ``HeaderName`` and ``HeaderValue`` elements, if any, for
        this distribution.

        - **HeaderName** *(string) --* **[REQUIRED]**

          The name of a header that you want CloudFront to forward to your origin. For more
          information, see `Forwarding Custom Headers to Your Origin (Web Distributions Only)
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html>`__
          in the *Amazon CloudFront Developer Guide* .

        - **HeaderValue** *(string) --* **[REQUIRED]**

          The value for the header that you specified in the ``HeaderName`` field.
    """


_ClientCreateDistributionDistributionConfigOriginsItemsCustomOriginConfigOriginSslProtocolsTypeDef = TypedDict(
    "_ClientCreateDistributionDistributionConfigOriginsItemsCustomOriginConfigOriginSslProtocolsTypeDef",
    {"Quantity": int, "Items": List[str]},
)


class ClientCreateDistributionDistributionConfigOriginsItemsCustomOriginConfigOriginSslProtocolsTypeDef(
    _ClientCreateDistributionDistributionConfigOriginsItemsCustomOriginConfigOriginSslProtocolsTypeDef
):
    """
    Type definition for `ClientCreateDistributionDistributionConfigOriginsItemsCustomOriginConfig` `OriginSslProtocols`

    The SSL/TLS protocols that you want CloudFront to use when communicating with your
    origin over HTTPS.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of SSL/TLS protocols that you want to allow CloudFront to use when
      establishing an HTTPS connection with this origin.

    - **Items** *(list) --* **[REQUIRED]**

      A list that contains allowed SSL/TLS protocols for this distribution.

      - *(string) --*
    """


_RequiredClientCreateDistributionDistributionConfigOriginsItemsCustomOriginConfigTypeDef = TypedDict(
    "_RequiredClientCreateDistributionDistributionConfigOriginsItemsCustomOriginConfigTypeDef",
    {"HTTPPort": int, "HTTPSPort": int, "OriginProtocolPolicy": str},
)
_OptionalClientCreateDistributionDistributionConfigOriginsItemsCustomOriginConfigTypeDef = TypedDict(
    "_OptionalClientCreateDistributionDistributionConfigOriginsItemsCustomOriginConfigTypeDef",
    {
        "OriginSslProtocols": ClientCreateDistributionDistributionConfigOriginsItemsCustomOriginConfigOriginSslProtocolsTypeDef,
        "OriginReadTimeout": int,
        "OriginKeepaliveTimeout": int,
    },
    total=False,
)


class ClientCreateDistributionDistributionConfigOriginsItemsCustomOriginConfigTypeDef(
    _RequiredClientCreateDistributionDistributionConfigOriginsItemsCustomOriginConfigTypeDef,
    _OptionalClientCreateDistributionDistributionConfigOriginsItemsCustomOriginConfigTypeDef,
):
    """
    Type definition for `ClientCreateDistributionDistributionConfigOriginsItems` `CustomOriginConfig`

    A complex type that contains information about a custom origin. If the origin is an
    Amazon S3 bucket, use the ``S3OriginConfig`` element instead.

    - **HTTPPort** *(integer) --* **[REQUIRED]**

      The HTTP port the custom origin listens on.

    - **HTTPSPort** *(integer) --* **[REQUIRED]**

      The HTTPS port the custom origin listens on.

    - **OriginProtocolPolicy** *(string) --* **[REQUIRED]**

      The origin protocol policy to apply to your origin.

    - **OriginSslProtocols** *(dict) --*

      The SSL/TLS protocols that you want CloudFront to use when communicating with your
      origin over HTTPS.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of SSL/TLS protocols that you want to allow CloudFront to use when
        establishing an HTTPS connection with this origin.

      - **Items** *(list) --* **[REQUIRED]**

        A list that contains allowed SSL/TLS protocols for this distribution.

        - *(string) --*

    - **OriginReadTimeout** *(integer) --*

      You can create a custom origin read timeout. All timeout units are in seconds. The
      default origin read timeout is 30 seconds, but you can configure custom timeout lengths
      using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60
      seconds.

      If you need to increase the maximum time limit, contact the `AWS Support Center
      <https://console.aws.amazon.com/support/home#/>`__ .

    - **OriginKeepaliveTimeout** *(integer) --*

      You can create a custom keep-alive timeout. All timeout units are in seconds. The
      default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths
      using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60
      seconds.

      If you need to increase the maximum time limit, contact the `AWS Support Center
      <https://console.aws.amazon.com/support/home#/>`__ .
    """


_ClientCreateDistributionDistributionConfigOriginsItemsS3OriginConfigTypeDef = TypedDict(
    "_ClientCreateDistributionDistributionConfigOriginsItemsS3OriginConfigTypeDef",
    {"OriginAccessIdentity": str},
)


class ClientCreateDistributionDistributionConfigOriginsItemsS3OriginConfigTypeDef(
    _ClientCreateDistributionDistributionConfigOriginsItemsS3OriginConfigTypeDef
):
    """
    Type definition for `ClientCreateDistributionDistributionConfigOriginsItems` `S3OriginConfig`

    A complex type that contains information about the Amazon S3 origin. If the origin is a
    custom origin, use the ``CustomOriginConfig`` element instead.

    - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

      The CloudFront origin access identity to associate with the origin. Use an origin
      access identity to configure the origin so that viewers can *only* access objects in an
      Amazon S3 bucket through CloudFront. The format of the value is:

      origin-access-identity/cloudfront/*ID-of-origin-access-identity*

      where `` *ID-of-origin-access-identity* `` is the value that CloudFront returned in the
      ``ID`` element when you created the origin access identity.

      If you want viewers to be able to access objects using either the CloudFront URL or the
      Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

      To delete the origin access identity from an existing distribution, update the
      distribution configuration and include an empty ``OriginAccessIdentity`` element.

      To replace the origin access identity, update the distribution configuration and
      specify the new origin access identity.

      For more information about the origin access identity, see `Serving Private Content
      through CloudFront
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
      in the *Amazon CloudFront Developer Guide* .
    """


_RequiredClientCreateDistributionDistributionConfigOriginsItemsTypeDef = TypedDict(
    "_RequiredClientCreateDistributionDistributionConfigOriginsItemsTypeDef",
    {"Id": str, "DomainName": str},
)
_OptionalClientCreateDistributionDistributionConfigOriginsItemsTypeDef = TypedDict(
    "_OptionalClientCreateDistributionDistributionConfigOriginsItemsTypeDef",
    {
        "OriginPath": str,
        "CustomHeaders": ClientCreateDistributionDistributionConfigOriginsItemsCustomHeadersTypeDef,
        "S3OriginConfig": ClientCreateDistributionDistributionConfigOriginsItemsS3OriginConfigTypeDef,
        "CustomOriginConfig": ClientCreateDistributionDistributionConfigOriginsItemsCustomOriginConfigTypeDef,
    },
    total=False,
)


class ClientCreateDistributionDistributionConfigOriginsItemsTypeDef(
    _RequiredClientCreateDistributionDistributionConfigOriginsItemsTypeDef,
    _OptionalClientCreateDistributionDistributionConfigOriginsItemsTypeDef,
):
    """
    Type definition for `ClientCreateDistributionDistributionConfigOrigins` `Items`

    A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web
    server), Amazon MediaStore, or other server from which CloudFront gets your files. This can
    also be an origin group, if you've created an origin group. You must specify at least one
    origin or origin group.

    For the current limit on the number of origins or origin groups that you can specify for a
    distribution, see `Amazon CloudFront Limits
    <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront>`__
    in the *AWS General Reference* .

    - **Id** *(string) --* **[REQUIRED]**

      A unique identifier for the origin or origin group. The value of ``Id`` must be unique
      within the distribution.

      When you specify the value of ``TargetOriginId`` for the default cache behavior or for
      another cache behavior, you indicate the origin to which you want the cache behavior to
      route requests by specifying the value of the ``Id`` element for that origin. When a
      request matches the path pattern for that cache behavior, CloudFront routes the request
      to the specified origin. For more information, see `Cache Behavior Settings
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior>`__
      in the *Amazon CloudFront Developer Guide* .

    - **DomainName** *(string) --* **[REQUIRED]**

       **Amazon S3 origins** : The DNS name of the Amazon S3 bucket from which you want
       CloudFront to get objects for this origin, for example, ``myawsbucket.s3.amazonaws.com``
       . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3
       static website hosting endpoint for the bucket.

      For more information about specifying this value for different types of origins, see
      `Origin Domain Name
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesDomainName>`__
      in the *Amazon CloudFront Developer Guide* .

      Constraints for Amazon S3 origins:

      * If you configured Amazon S3 Transfer Acceleration for your bucket, don't specify the
      ``s3-accelerate`` endpoint for ``DomainName`` .

      * The bucket name must be between 3 and 63 characters long (inclusive).

      * The bucket name must contain only lowercase characters, numbers, periods, underscores,
      and dashes.

      * The bucket name must not contain adjacent periods.

       **Custom Origins** : The DNS domain name for the HTTP server from which you want
       CloudFront to get objects for this origin, for example, ``www.example.com`` .

      Constraints for custom origins:

      * ``DomainName`` must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.),
      hyphen (-), or underscore (_) characters.

      * The name cannot exceed 128 characters.

    - **OriginPath** *(string) --*

      An optional element that causes CloudFront to request your content from a directory in
      your Amazon S3 bucket or your custom origin. When you include the ``OriginPath`` element,
      specify the directory name, beginning with a ``/`` . CloudFront appends the directory
      name to the value of ``DomainName`` , for example, ``example.com/production`` . Do not
      include a ``/`` at the end of the directory name.

      For example, suppose you've specified the following values for your distribution:

      * ``DomainName`` : An Amazon S3 bucket named ``myawsbucket`` .

      * ``OriginPath`` : ``/production``

      * ``CNAME`` : ``example.com``

      When a user enters ``example.com/index.html`` in a browser, CloudFront sends a request to
      Amazon S3 for ``myawsbucket/production/index.html`` .

      When a user enters ``example.com/acme/index.html`` in a browser, CloudFront sends a
      request to Amazon S3 for ``myawsbucket/production/acme/index.html`` .

    - **CustomHeaders** *(dict) --*

      A complex type that contains names and values for the custom headers that you want.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of custom headers, if any, for this distribution.

      - **Items** *(list) --*

         **Optional** : A list that contains one ``OriginCustomHeader`` element for each custom
         header that you want CloudFront to forward to the origin. If Quantity is ``0`` , omit
         ``Items`` .

        - *(dict) --*

          A complex type that contains ``HeaderName`` and ``HeaderValue`` elements, if any, for
          this distribution.

          - **HeaderName** *(string) --* **[REQUIRED]**

            The name of a header that you want CloudFront to forward to your origin. For more
            information, see `Forwarding Custom Headers to Your Origin (Web Distributions Only)
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html>`__
            in the *Amazon CloudFront Developer Guide* .

          - **HeaderValue** *(string) --* **[REQUIRED]**

            The value for the header that you specified in the ``HeaderName`` field.

    - **S3OriginConfig** *(dict) --*

      A complex type that contains information about the Amazon S3 origin. If the origin is a
      custom origin, use the ``CustomOriginConfig`` element instead.

      - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

        The CloudFront origin access identity to associate with the origin. Use an origin
        access identity to configure the origin so that viewers can *only* access objects in an
        Amazon S3 bucket through CloudFront. The format of the value is:

        origin-access-identity/cloudfront/*ID-of-origin-access-identity*

        where `` *ID-of-origin-access-identity* `` is the value that CloudFront returned in the
        ``ID`` element when you created the origin access identity.

        If you want viewers to be able to access objects using either the CloudFront URL or the
        Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

        To delete the origin access identity from an existing distribution, update the
        distribution configuration and include an empty ``OriginAccessIdentity`` element.

        To replace the origin access identity, update the distribution configuration and
        specify the new origin access identity.

        For more information about the origin access identity, see `Serving Private Content
        through CloudFront
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
        in the *Amazon CloudFront Developer Guide* .

    - **CustomOriginConfig** *(dict) --*

      A complex type that contains information about a custom origin. If the origin is an
      Amazon S3 bucket, use the ``S3OriginConfig`` element instead.

      - **HTTPPort** *(integer) --* **[REQUIRED]**

        The HTTP port the custom origin listens on.

      - **HTTPSPort** *(integer) --* **[REQUIRED]**

        The HTTPS port the custom origin listens on.

      - **OriginProtocolPolicy** *(string) --* **[REQUIRED]**

        The origin protocol policy to apply to your origin.

      - **OriginSslProtocols** *(dict) --*

        The SSL/TLS protocols that you want CloudFront to use when communicating with your
        origin over HTTPS.

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of SSL/TLS protocols that you want to allow CloudFront to use when
          establishing an HTTPS connection with this origin.

        - **Items** *(list) --* **[REQUIRED]**

          A list that contains allowed SSL/TLS protocols for this distribution.

          - *(string) --*

      - **OriginReadTimeout** *(integer) --*

        You can create a custom origin read timeout. All timeout units are in seconds. The
        default origin read timeout is 30 seconds, but you can configure custom timeout lengths
        using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60
        seconds.

        If you need to increase the maximum time limit, contact the `AWS Support Center
        <https://console.aws.amazon.com/support/home#/>`__ .

      - **OriginKeepaliveTimeout** *(integer) --*

        You can create a custom keep-alive timeout. All timeout units are in seconds. The
        default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths
        using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60
        seconds.

        If you need to increase the maximum time limit, contact the `AWS Support Center
        <https://console.aws.amazon.com/support/home#/>`__ .
    """


_ClientCreateDistributionDistributionConfigOriginsTypeDef = TypedDict(
    "_ClientCreateDistributionDistributionConfigOriginsTypeDef",
    {
        "Quantity": int,
        "Items": List[ClientCreateDistributionDistributionConfigOriginsItemsTypeDef],
    },
)


class ClientCreateDistributionDistributionConfigOriginsTypeDef(
    _ClientCreateDistributionDistributionConfigOriginsTypeDef
):
    """
    Type definition for `ClientCreateDistributionDistributionConfig` `Origins`

    A complex type that contains information about origins for this distribution.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of origins or origin groups for this distribution.

    - **Items** *(list) --* **[REQUIRED]**

      A complex type that contains origins or origin groups for this distribution.

      - *(dict) --*

        A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web
        server), Amazon MediaStore, or other server from which CloudFront gets your files. This can
        also be an origin group, if you've created an origin group. You must specify at least one
        origin or origin group.

        For the current limit on the number of origins or origin groups that you can specify for a
        distribution, see `Amazon CloudFront Limits
        <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront>`__
        in the *AWS General Reference* .

        - **Id** *(string) --* **[REQUIRED]**

          A unique identifier for the origin or origin group. The value of ``Id`` must be unique
          within the distribution.

          When you specify the value of ``TargetOriginId`` for the default cache behavior or for
          another cache behavior, you indicate the origin to which you want the cache behavior to
          route requests by specifying the value of the ``Id`` element for that origin. When a
          request matches the path pattern for that cache behavior, CloudFront routes the request
          to the specified origin. For more information, see `Cache Behavior Settings
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior>`__
          in the *Amazon CloudFront Developer Guide* .

        - **DomainName** *(string) --* **[REQUIRED]**

           **Amazon S3 origins** : The DNS name of the Amazon S3 bucket from which you want
           CloudFront to get objects for this origin, for example, ``myawsbucket.s3.amazonaws.com``
           . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3
           static website hosting endpoint for the bucket.

          For more information about specifying this value for different types of origins, see
          `Origin Domain Name
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesDomainName>`__
          in the *Amazon CloudFront Developer Guide* .

          Constraints for Amazon S3 origins:

          * If you configured Amazon S3 Transfer Acceleration for your bucket, don't specify the
          ``s3-accelerate`` endpoint for ``DomainName`` .

          * The bucket name must be between 3 and 63 characters long (inclusive).

          * The bucket name must contain only lowercase characters, numbers, periods, underscores,
          and dashes.

          * The bucket name must not contain adjacent periods.

           **Custom Origins** : The DNS domain name for the HTTP server from which you want
           CloudFront to get objects for this origin, for example, ``www.example.com`` .

          Constraints for custom origins:

          * ``DomainName`` must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.),
          hyphen (-), or underscore (_) characters.

          * The name cannot exceed 128 characters.

        - **OriginPath** *(string) --*

          An optional element that causes CloudFront to request your content from a directory in
          your Amazon S3 bucket or your custom origin. When you include the ``OriginPath`` element,
          specify the directory name, beginning with a ``/`` . CloudFront appends the directory
          name to the value of ``DomainName`` , for example, ``example.com/production`` . Do not
          include a ``/`` at the end of the directory name.

          For example, suppose you've specified the following values for your distribution:

          * ``DomainName`` : An Amazon S3 bucket named ``myawsbucket`` .

          * ``OriginPath`` : ``/production``

          * ``CNAME`` : ``example.com``

          When a user enters ``example.com/index.html`` in a browser, CloudFront sends a request to
          Amazon S3 for ``myawsbucket/production/index.html`` .

          When a user enters ``example.com/acme/index.html`` in a browser, CloudFront sends a
          request to Amazon S3 for ``myawsbucket/production/acme/index.html`` .

        - **CustomHeaders** *(dict) --*

          A complex type that contains names and values for the custom headers that you want.

          - **Quantity** *(integer) --* **[REQUIRED]**

            The number of custom headers, if any, for this distribution.

          - **Items** *(list) --*

             **Optional** : A list that contains one ``OriginCustomHeader`` element for each custom
             header that you want CloudFront to forward to the origin. If Quantity is ``0`` , omit
             ``Items`` .

            - *(dict) --*

              A complex type that contains ``HeaderName`` and ``HeaderValue`` elements, if any, for
              this distribution.

              - **HeaderName** *(string) --* **[REQUIRED]**

                The name of a header that you want CloudFront to forward to your origin. For more
                information, see `Forwarding Custom Headers to Your Origin (Web Distributions Only)
                <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html>`__
                in the *Amazon CloudFront Developer Guide* .

              - **HeaderValue** *(string) --* **[REQUIRED]**

                The value for the header that you specified in the ``HeaderName`` field.

        - **S3OriginConfig** *(dict) --*

          A complex type that contains information about the Amazon S3 origin. If the origin is a
          custom origin, use the ``CustomOriginConfig`` element instead.

          - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

            The CloudFront origin access identity to associate with the origin. Use an origin
            access identity to configure the origin so that viewers can *only* access objects in an
            Amazon S3 bucket through CloudFront. The format of the value is:

            origin-access-identity/cloudfront/*ID-of-origin-access-identity*

            where `` *ID-of-origin-access-identity* `` is the value that CloudFront returned in the
            ``ID`` element when you created the origin access identity.

            If you want viewers to be able to access objects using either the CloudFront URL or the
            Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

            To delete the origin access identity from an existing distribution, update the
            distribution configuration and include an empty ``OriginAccessIdentity`` element.

            To replace the origin access identity, update the distribution configuration and
            specify the new origin access identity.

            For more information about the origin access identity, see `Serving Private Content
            through CloudFront
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
            in the *Amazon CloudFront Developer Guide* .

        - **CustomOriginConfig** *(dict) --*

          A complex type that contains information about a custom origin. If the origin is an
          Amazon S3 bucket, use the ``S3OriginConfig`` element instead.

          - **HTTPPort** *(integer) --* **[REQUIRED]**

            The HTTP port the custom origin listens on.

          - **HTTPSPort** *(integer) --* **[REQUIRED]**

            The HTTPS port the custom origin listens on.

          - **OriginProtocolPolicy** *(string) --* **[REQUIRED]**

            The origin protocol policy to apply to your origin.

          - **OriginSslProtocols** *(dict) --*

            The SSL/TLS protocols that you want CloudFront to use when communicating with your
            origin over HTTPS.

            - **Quantity** *(integer) --* **[REQUIRED]**

              The number of SSL/TLS protocols that you want to allow CloudFront to use when
              establishing an HTTPS connection with this origin.

            - **Items** *(list) --* **[REQUIRED]**

              A list that contains allowed SSL/TLS protocols for this distribution.

              - *(string) --*

          - **OriginReadTimeout** *(integer) --*

            You can create a custom origin read timeout. All timeout units are in seconds. The
            default origin read timeout is 30 seconds, but you can configure custom timeout lengths
            using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60
            seconds.

            If you need to increase the maximum time limit, contact the `AWS Support Center
            <https://console.aws.amazon.com/support/home#/>`__ .

          - **OriginKeepaliveTimeout** *(integer) --*

            You can create a custom keep-alive timeout. All timeout units are in seconds. The
            default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths
            using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60
            seconds.

            If you need to increase the maximum time limit, contact the `AWS Support Center
            <https://console.aws.amazon.com/support/home#/>`__ .
    """


_RequiredClientCreateDistributionDistributionConfigTypeDef = TypedDict(
    "_RequiredClientCreateDistributionDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "Origins": ClientCreateDistributionDistributionConfigOriginsTypeDef,
        "DefaultCacheBehavior": ClientCreateDistributionDistributionConfigDefaultCacheBehaviorTypeDef,
    },
)
_OptionalClientCreateDistributionDistributionConfigTypeDef = TypedDict(
    "_OptionalClientCreateDistributionDistributionConfigTypeDef",
    {
        "Aliases": ClientCreateDistributionDistributionConfigAliasesTypeDef,
        "DefaultRootObject": str,
        "OriginGroups": ClientCreateDistributionDistributionConfigOriginGroupsTypeDef,
    },
    total=False,
)


class ClientCreateDistributionDistributionConfigTypeDef(
    _RequiredClientCreateDistributionDistributionConfigTypeDef,
    _OptionalClientCreateDistributionDistributionConfigTypeDef,
):
    """
    Type definition for `ClientCreateDistribution` `DistributionConfig`

    The distribution's configuration information.

    - **CallerReference** *(string) --* **[REQUIRED]**

      A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.

      If the value of ``CallerReference`` is new (regardless of the content of the
      ``DistributionConfig`` object), CloudFront creates a new distribution.

      If ``CallerReference`` is a value that you already sent in a previous request to create a
      distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

    - **Aliases** *(dict) --*

      A complex type that contains information about CNAMEs (alternate domain names), if any, for
      this distribution.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of CNAME aliases, if any, that you want to associate with this distribution.

      - **Items** *(list) --*

        A complex type that contains the CNAME aliases, if any, that you want to associate with this
        distribution.

        - *(string) --*

    - **DefaultRootObject** *(string) --*

      The object that you want CloudFront to request from your origin (for example, ``index.html`` )
      when a viewer requests the root URL for your distribution (``http://www.example.com`` ) instead
      of an object in your distribution (``http://www.example.com/product-description.html`` ).
      Specifying a default root object avoids exposing the contents of your distribution.

      Specify only the object name, for example, ``index.html`` . Don't add a ``/`` before the object
      name.

      If you don't want to specify a default root object when you create a distribution, include an
      empty ``DefaultRootObject`` element.

      To delete the default root object from an existing distribution, update the distribution
      configuration and include an empty ``DefaultRootObject`` element.

      To replace the default root object, update the distribution configuration and specify the new
      object.

      For more information about the default root object, see `Creating a Default Root Object
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html>`__
      in the *Amazon CloudFront Developer Guide* .

    - **Origins** *(dict) --* **[REQUIRED]**

      A complex type that contains information about origins for this distribution.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of origins or origin groups for this distribution.

      - **Items** *(list) --* **[REQUIRED]**

        A complex type that contains origins or origin groups for this distribution.

        - *(dict) --*

          A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web
          server), Amazon MediaStore, or other server from which CloudFront gets your files. This can
          also be an origin group, if you've created an origin group. You must specify at least one
          origin or origin group.

          For the current limit on the number of origins or origin groups that you can specify for a
          distribution, see `Amazon CloudFront Limits
          <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront>`__
          in the *AWS General Reference* .

          - **Id** *(string) --* **[REQUIRED]**

            A unique identifier for the origin or origin group. The value of ``Id`` must be unique
            within the distribution.

            When you specify the value of ``TargetOriginId`` for the default cache behavior or for
            another cache behavior, you indicate the origin to which you want the cache behavior to
            route requests by specifying the value of the ``Id`` element for that origin. When a
            request matches the path pattern for that cache behavior, CloudFront routes the request
            to the specified origin. For more information, see `Cache Behavior Settings
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior>`__
            in the *Amazon CloudFront Developer Guide* .

          - **DomainName** *(string) --* **[REQUIRED]**

             **Amazon S3 origins** : The DNS name of the Amazon S3 bucket from which you want
             CloudFront to get objects for this origin, for example, ``myawsbucket.s3.amazonaws.com``
             . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3
             static website hosting endpoint for the bucket.

            For more information about specifying this value for different types of origins, see
            `Origin Domain Name
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesDomainName>`__
            in the *Amazon CloudFront Developer Guide* .

            Constraints for Amazon S3 origins:

            * If you configured Amazon S3 Transfer Acceleration for your bucket, don't specify the
            ``s3-accelerate`` endpoint for ``DomainName`` .

            * The bucket name must be between 3 and 63 characters long (inclusive).

            * The bucket name must contain only lowercase characters, numbers, periods, underscores,
            and dashes.

            * The bucket name must not contain adjacent periods.

             **Custom Origins** : The DNS domain name for the HTTP server from which you want
             CloudFront to get objects for this origin, for example, ``www.example.com`` .

            Constraints for custom origins:

            * ``DomainName`` must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.),
            hyphen (-), or underscore (_) characters.

            * The name cannot exceed 128 characters.

          - **OriginPath** *(string) --*

            An optional element that causes CloudFront to request your content from a directory in
            your Amazon S3 bucket or your custom origin. When you include the ``OriginPath`` element,
            specify the directory name, beginning with a ``/`` . CloudFront appends the directory
            name to the value of ``DomainName`` , for example, ``example.com/production`` . Do not
            include a ``/`` at the end of the directory name.

            For example, suppose you've specified the following values for your distribution:

            * ``DomainName`` : An Amazon S3 bucket named ``myawsbucket`` .

            * ``OriginPath`` : ``/production``

            * ``CNAME`` : ``example.com``

            When a user enters ``example.com/index.html`` in a browser, CloudFront sends a request to
            Amazon S3 for ``myawsbucket/production/index.html`` .

            When a user enters ``example.com/acme/index.html`` in a browser, CloudFront sends a
            request to Amazon S3 for ``myawsbucket/production/acme/index.html`` .

          - **CustomHeaders** *(dict) --*

            A complex type that contains names and values for the custom headers that you want.

            - **Quantity** *(integer) --* **[REQUIRED]**

              The number of custom headers, if any, for this distribution.

            - **Items** *(list) --*

               **Optional** : A list that contains one ``OriginCustomHeader`` element for each custom
               header that you want CloudFront to forward to the origin. If Quantity is ``0`` , omit
               ``Items`` .

              - *(dict) --*

                A complex type that contains ``HeaderName`` and ``HeaderValue`` elements, if any, for
                this distribution.

                - **HeaderName** *(string) --* **[REQUIRED]**

                  The name of a header that you want CloudFront to forward to your origin. For more
                  information, see `Forwarding Custom Headers to Your Origin (Web Distributions Only)
                  <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html>`__
                  in the *Amazon CloudFront Developer Guide* .

                - **HeaderValue** *(string) --* **[REQUIRED]**

                  The value for the header that you specified in the ``HeaderName`` field.

          - **S3OriginConfig** *(dict) --*

            A complex type that contains information about the Amazon S3 origin. If the origin is a
            custom origin, use the ``CustomOriginConfig`` element instead.

            - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

              The CloudFront origin access identity to associate with the origin. Use an origin
              access identity to configure the origin so that viewers can *only* access objects in an
              Amazon S3 bucket through CloudFront. The format of the value is:

              origin-access-identity/cloudfront/*ID-of-origin-access-identity*

              where `` *ID-of-origin-access-identity* `` is the value that CloudFront returned in the
              ``ID`` element when you created the origin access identity.

              If you want viewers to be able to access objects using either the CloudFront URL or the
              Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

              To delete the origin access identity from an existing distribution, update the
              distribution configuration and include an empty ``OriginAccessIdentity`` element.

              To replace the origin access identity, update the distribution configuration and
              specify the new origin access identity.

              For more information about the origin access identity, see `Serving Private Content
              through CloudFront
              <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
              in the *Amazon CloudFront Developer Guide* .

          - **CustomOriginConfig** *(dict) --*

            A complex type that contains information about a custom origin. If the origin is an
            Amazon S3 bucket, use the ``S3OriginConfig`` element instead.

            - **HTTPPort** *(integer) --* **[REQUIRED]**

              The HTTP port the custom origin listens on.

            - **HTTPSPort** *(integer) --* **[REQUIRED]**

              The HTTPS port the custom origin listens on.

            - **OriginProtocolPolicy** *(string) --* **[REQUIRED]**

              The origin protocol policy to apply to your origin.

            - **OriginSslProtocols** *(dict) --*

              The SSL/TLS protocols that you want CloudFront to use when communicating with your
              origin over HTTPS.

              - **Quantity** *(integer) --* **[REQUIRED]**

                The number of SSL/TLS protocols that you want to allow CloudFront to use when
                establishing an HTTPS connection with this origin.

              - **Items** *(list) --* **[REQUIRED]**

                A list that contains allowed SSL/TLS protocols for this distribution.

                - *(string) --*

            - **OriginReadTimeout** *(integer) --*

              You can create a custom origin read timeout. All timeout units are in seconds. The
              default origin read timeout is 30 seconds, but you can configure custom timeout lengths
              using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60
              seconds.

              If you need to increase the maximum time limit, contact the `AWS Support Center
              <https://console.aws.amazon.com/support/home#/>`__ .

            - **OriginKeepaliveTimeout** *(integer) --*

              You can create a custom keep-alive timeout. All timeout units are in seconds. The
              default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths
              using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60
              seconds.

              If you need to increase the maximum time limit, contact the `AWS Support Center
              <https://console.aws.amazon.com/support/home#/>`__ .

    - **OriginGroups** *(dict) --*

      A complex type that contains information about origin groups for this distribution.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of origin groups.

      - **Items** *(list) --*

        The items (origin groups) in a distribution.

        - *(dict) --*

          An origin group includes two origins (a primary origin and a second origin to failover to)
          and a failover criteria that you specify. You create an origin group to support origin
          failover in CloudFront. When you create or update a distribution, you can specifiy the
          origin group instead of a single origin, and CloudFront will failover from the primary
          origin to the second origin under the failover conditions that you've chosen.

          - **Id** *(string) --* **[REQUIRED]**

            The origin group's ID.

          - **FailoverCriteria** *(dict) --* **[REQUIRED]**

            A complex type that contains information about the failover criteria for an origin group.

            - **StatusCodes** *(dict) --* **[REQUIRED]**

              The status codes that, when returned from the primary origin, will trigger CloudFront
              to failover to the second origin.

              - **Quantity** *(integer) --* **[REQUIRED]**

                The number of status codes.

              - **Items** *(list) --* **[REQUIRED]**

                The items (status codes) for an origin group.

                - *(integer) --*

          - **Members** *(dict) --* **[REQUIRED]**

            A complex type that contains information about the origins in an origin group.

            - **Quantity** *(integer) --* **[REQUIRED]**

              The number of origins in an origin group.

            - **Items** *(list) --* **[REQUIRED]**

              Items (origins) in an origin group.

              - *(dict) --*

                An origin in an origin group.

                - **OriginId** *(string) --* **[REQUIRED]**

                  The ID for an origin in an origin group.

    - **DefaultCacheBehavior** *(dict) --* **[REQUIRED]**

      A complex type that describes the default cache behavior if you don't specify a
      ``CacheBehavior`` element or if files don't match any of the values of ``PathPattern`` in
      ``CacheBehavior`` elements. You must create exactly one default cache behavior.

      - **TargetOriginId** *(string) --* **[REQUIRED]**

        The value of ``ID`` for the origin that you want CloudFront to route requests to when a
        request matches the path pattern either for a cache behavior or for the default cache
        behavior in your distribution.

      - **ForwardedValues** *(dict) --* **[REQUIRED]**

        A complex type that specifies how CloudFront handles query strings and cookies.

        - **QueryString** *(boolean) --* **[REQUIRED]**

          Indicates whether you want CloudFront to forward query strings to the origin that is
          associated with this cache behavior and cache based on the query string parameters.
          CloudFront behavior depends on the value of ``QueryString`` and on the values that you
          specify for ``QueryStringCacheKeys`` , if any:

          If you specify true for ``QueryString`` and you don't specify any values for
          ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin
          and caches based on all query string parameters. Depending on how many query string
          parameters and values you have, this can adversely affect performance because CloudFront
          must forward more requests to the origin.

          If you specify true for ``QueryString`` and you specify one or more values for
          ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin,
          but it only caches based on the query string parameters that you specify.

          If you specify false for ``QueryString`` , CloudFront doesn't forward any query string
          parameters to the origin, and doesn't cache based on query string parameters.

          For more information, see `Configuring CloudFront to Cache Based on Query String Parameters
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html>`__
          in the *Amazon CloudFront Developer Guide* .

        - **Cookies** *(dict) --* **[REQUIRED]**

          A complex type that specifies whether you want CloudFront to forward cookies to the origin
          and, if so, which ones. For more information about forwarding cookies to the origin, see
          `How CloudFront Forwards, Caches, and Logs Cookies
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html>`__ in the
          *Amazon CloudFront Developer Guide* .

          - **Forward** *(string) --* **[REQUIRED]**

            Specifies which cookies to forward to the origin for this cache behavior: all, none, or
            the list of cookies specified in the ``WhitelistedNames`` complex type.

            Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an
            Amazon S3 origin, specify none for the ``Forward`` element.

          - **WhitelistedNames** *(dict) --*

            Required if you specify ``whitelist`` for the value of ``Forward:`` . A complex type that
            specifies how many different cookies you want CloudFront to forward to the origin for
            this cache behavior and, if you want to forward selected cookies, the names of those
            cookies.

            If you specify ``all`` or none for the value of ``Forward`` , omit ``WhitelistedNames`` .
            If you change the value of ``Forward`` from ``whitelist`` to all or none and you don't
            delete the ``WhitelistedNames`` element and its child elements, CloudFront deletes them
            automatically.

            For the current limit on the number of cookie names that you can whitelist for each cache
            behavior, see `CloudFront Limits
            <https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront>`__
            in the *AWS General Reference* .

            - **Quantity** *(integer) --* **[REQUIRED]**

              The number of different cookies that you want CloudFront to forward to the origin for
              this cache behavior.

            - **Items** *(list) --*

              A complex type that contains one ``Name`` element for each cookie that you want
              CloudFront to forward to the origin for this cache behavior.

              - *(string) --*

        - **Headers** *(dict) --*

          A complex type that specifies the ``Headers`` , if any, that you want CloudFront to forward
          to the origin for this cache behavior (whitelisted headers). For the headers that you
          specify, CloudFront also caches separate versions of a specified object that is based on
          the header values in viewer requests.

          For more information, see `Caching Content Based on Request Headers
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html>`__
          in the *Amazon CloudFront Developer Guide* .

          - **Quantity** *(integer) --* **[REQUIRED]**

            The number of different headers that you want CloudFront to base caching on for this
            cache behavior. You can configure each cache behavior in a web distribution to do one of
            the following:

            * **Forward all headers to your origin** : Specify ``1`` for ``Quantity`` and ``*`` for
            ``Name`` .

            .. warning::

               CloudFront doesn't cache the objects that are associated with this cache behavior.
               Instead, CloudFront sends every request to the origin.

            * **Forward a whitelist of headers you specify** : Specify the number of headers that you
            want CloudFront to base caching on. Then specify the header names in ``Name`` elements.
            CloudFront caches your objects based on the values in the specified headers.

            * **Forward only the default headers** : Specify ``0`` for ``Quantity`` and omit
            ``Items`` . In this configuration, CloudFront doesn't cache based on the values in the
            request headers.

            Regardless of which option you choose, CloudFront forwards headers to your origin based
            on whether the origin is an S3 bucket or a custom origin. See the following documentation:

            * **S3 bucket** : See `HTTP Request Headers That CloudFront Removes or Updates
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorS3Origin.html#request-s3-removed-headers>`__
    """


_RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigAliasesTypeDef = TypedDict(
    "_RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigAliasesTypeDef",
    {"Quantity": int},
)
_OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigAliasesTypeDef = TypedDict(
    "_OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigAliasesTypeDef",
    {"Items": List[str]},
    total=False,
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigAliasesTypeDef(
    _RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigAliasesTypeDef,
    _OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigAliasesTypeDef,
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfig` `Aliases`

    A complex type that contains information about CNAMEs (alternate domain names), if any, for
    this distribution.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of CNAME aliases, if any, that you want to associate with this distribution.

    - **Items** *(list) --*

      A complex type that contains the CNAME aliases, if any, that you want to associate with
      this distribution.

      - *(string) --*
    """


_RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef = TypedDict(
    "_RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef",
    {"Quantity": int},
)
_OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef = TypedDict(
    "_OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef",
    {"Items": List[str]},
    total=False,
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef(
    _RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef,
    _OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef,
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookies` `WhitelistedNames`

    Required if you specify ``whitelist`` for the value of ``Forward:`` . A complex type
    that specifies how many different cookies you want CloudFront to forward to the origin
    for this cache behavior and, if you want to forward selected cookies, the names of
    those cookies.

    If you specify ``all`` or none for the value of ``Forward`` , omit ``WhitelistedNames``
    . If you change the value of ``Forward`` from ``whitelist`` to all or none and you
    don't delete the ``WhitelistedNames`` element and its child elements, CloudFront
    deletes them automatically.

    For the current limit on the number of cookie names that you can whitelist for each
    cache behavior, see `CloudFront Limits
    <https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront>`__
    in the *AWS General Reference* .

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of different cookies that you want CloudFront to forward to the origin for
      this cache behavior.

    - **Items** *(list) --*

      A complex type that contains one ``Name`` element for each cookie that you want
      CloudFront to forward to the origin for this cache behavior.

      - *(string) --*
    """


_RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef = TypedDict(
    "_RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef",
    {"Forward": str},
)
_OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef = TypedDict(
    "_OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef",
    {
        "WhitelistedNames": ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef
    },
    total=False,
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef(
    _RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef,
    _OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef,
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValues` `Cookies`

    A complex type that specifies whether you want CloudFront to forward cookies to the
    origin and, if so, which ones. For more information about forwarding cookies to the
    origin, see `How CloudFront Forwards, Caches, and Logs Cookies
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html>`__ in
    the *Amazon CloudFront Developer Guide* .

    - **Forward** *(string) --* **[REQUIRED]**

      Specifies which cookies to forward to the origin for this cache behavior: all, none, or
      the list of cookies specified in the ``WhitelistedNames`` complex type.

      Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an
      Amazon S3 origin, specify none for the ``Forward`` element.

    - **WhitelistedNames** *(dict) --*

      Required if you specify ``whitelist`` for the value of ``Forward:`` . A complex type
      that specifies how many different cookies you want CloudFront to forward to the origin
      for this cache behavior and, if you want to forward selected cookies, the names of
      those cookies.

      If you specify ``all`` or none for the value of ``Forward`` , omit ``WhitelistedNames``
      . If you change the value of ``Forward`` from ``whitelist`` to all or none and you
      don't delete the ``WhitelistedNames`` element and its child elements, CloudFront
      deletes them automatically.

      For the current limit on the number of cookie names that you can whitelist for each
      cache behavior, see `CloudFront Limits
      <https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront>`__
      in the *AWS General Reference* .

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of different cookies that you want CloudFront to forward to the origin for
        this cache behavior.

      - **Items** *(list) --*

        A complex type that contains one ``Name`` element for each cookie that you want
        CloudFront to forward to the origin for this cache behavior.

        - *(string) --*
    """


_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesHeadersTypeDef = TypedDict(
    "_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesHeadersTypeDef",
    {"Quantity": int},
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesHeadersTypeDef(
    _ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesHeadersTypeDef
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValues` `Headers`

    A complex type that specifies the ``Headers`` , if any, that you want CloudFront to
    forward to the origin for this cache behavior (whitelisted headers). For the headers that
    you specify, CloudFront also caches separate versions of a specified object that is based
    on the header values in viewer requests.

    For more information, see `Caching Content Based on Request Headers
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html>`__
    in the *Amazon CloudFront Developer Guide* .

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of different headers that you want CloudFront to base caching on for this
      cache behavior. You can configure each cache behavior in a web distribution to do one
      of the following:

      * **Forward all headers to your origin** : Specify ``1`` for ``Quantity`` and ``*`` for
      ``Name`` .

      .. warning::

         CloudFront doesn't cache the objects that are associated with this cache behavior.
         Instead, CloudFront sends every request to the origin.

      * **Forward a whitelist of headers you specify** : Specify the number of headers that
      you want CloudFront to base caching on. Then specify the header names in ``Name``
      elements. CloudFront caches your objects based on the values in the specified headers.

      * **Forward only the default headers** : Specify ``0`` for ``Quantity`` and omit
      ``Items`` . In this configuration, CloudFront doesn't cache based on the values in the
      request headers.

      Regardless of which option you choose, CloudFront forwards headers to your origin based
      on whether the origin is an S3 bucket or a custom origin. See the following
      documentation:

      * **S3 bucket** : See `HTTP Request Headers That CloudFront Removes or Updates
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorS3Origin.html#request-s3-removed-headers>`__
    """


_RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef = TypedDict(
    "_RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef",
    {
        "QueryString": bool,
        "Cookies": ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef,
    },
)
_OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef = TypedDict(
    "_OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef",
    {
        "Headers": ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesHeadersTypeDef
    },
    total=False,
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef(
    _RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef,
    _OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef,
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehavior` `ForwardedValues`

    A complex type that specifies how CloudFront handles query strings and cookies.

    - **QueryString** *(boolean) --* **[REQUIRED]**

      Indicates whether you want CloudFront to forward query strings to the origin that is
      associated with this cache behavior and cache based on the query string parameters.
      CloudFront behavior depends on the value of ``QueryString`` and on the values that you
      specify for ``QueryStringCacheKeys`` , if any:

      If you specify true for ``QueryString`` and you don't specify any values for
      ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin
      and caches based on all query string parameters. Depending on how many query string
      parameters and values you have, this can adversely affect performance because CloudFront
      must forward more requests to the origin.

      If you specify true for ``QueryString`` and you specify one or more values for
      ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin,
      but it only caches based on the query string parameters that you specify.

      If you specify false for ``QueryString`` , CloudFront doesn't forward any query string
      parameters to the origin, and doesn't cache based on query string parameters.

      For more information, see `Configuring CloudFront to Cache Based on Query String
      Parameters
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html>`__
      in the *Amazon CloudFront Developer Guide* .

    - **Cookies** *(dict) --* **[REQUIRED]**

      A complex type that specifies whether you want CloudFront to forward cookies to the
      origin and, if so, which ones. For more information about forwarding cookies to the
      origin, see `How CloudFront Forwards, Caches, and Logs Cookies
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html>`__ in
      the *Amazon CloudFront Developer Guide* .

      - **Forward** *(string) --* **[REQUIRED]**

        Specifies which cookies to forward to the origin for this cache behavior: all, none, or
        the list of cookies specified in the ``WhitelistedNames`` complex type.

        Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an
        Amazon S3 origin, specify none for the ``Forward`` element.

      - **WhitelistedNames** *(dict) --*

        Required if you specify ``whitelist`` for the value of ``Forward:`` . A complex type
        that specifies how many different cookies you want CloudFront to forward to the origin
        for this cache behavior and, if you want to forward selected cookies, the names of
        those cookies.

        If you specify ``all`` or none for the value of ``Forward`` , omit ``WhitelistedNames``
        . If you change the value of ``Forward`` from ``whitelist`` to all or none and you
        don't delete the ``WhitelistedNames`` element and its child elements, CloudFront
        deletes them automatically.

        For the current limit on the number of cookie names that you can whitelist for each
        cache behavior, see `CloudFront Limits
        <https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront>`__
        in the *AWS General Reference* .

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of different cookies that you want CloudFront to forward to the origin for
          this cache behavior.

        - **Items** *(list) --*

          A complex type that contains one ``Name`` element for each cookie that you want
          CloudFront to forward to the origin for this cache behavior.

          - *(string) --*

    - **Headers** *(dict) --*

      A complex type that specifies the ``Headers`` , if any, that you want CloudFront to
      forward to the origin for this cache behavior (whitelisted headers). For the headers that
      you specify, CloudFront also caches separate versions of a specified object that is based
      on the header values in viewer requests.

      For more information, see `Caching Content Based on Request Headers
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html>`__
      in the *Amazon CloudFront Developer Guide* .

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of different headers that you want CloudFront to base caching on for this
        cache behavior. You can configure each cache behavior in a web distribution to do one
        of the following:

        * **Forward all headers to your origin** : Specify ``1`` for ``Quantity`` and ``*`` for
        ``Name`` .

        .. warning::

           CloudFront doesn't cache the objects that are associated with this cache behavior.
           Instead, CloudFront sends every request to the origin.

        * **Forward a whitelist of headers you specify** : Specify the number of headers that
        you want CloudFront to base caching on. Then specify the header names in ``Name``
        elements. CloudFront caches your objects based on the values in the specified headers.

        * **Forward only the default headers** : Specify ``0`` for ``Quantity`` and omit
        ``Items`` . In this configuration, CloudFront doesn't cache based on the values in the
        request headers.

        Regardless of which option you choose, CloudFront forwards headers to your origin based
        on whether the origin is an S3 bucket or a custom origin. See the following
        documentation:

        * **S3 bucket** : See `HTTP Request Headers That CloudFront Removes or Updates
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorS3Origin.html#request-s3-removed-headers>`__
    """


_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorTypeDef = TypedDict(
    "_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorTypeDef",
    {
        "TargetOriginId": str,
        "ForwardedValues": ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef,
    },
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorTypeDef(
    _ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorTypeDef
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfig` `DefaultCacheBehavior`

    A complex type that describes the default cache behavior if you don't specify a
    ``CacheBehavior`` element or if files don't match any of the values of ``PathPattern`` in
    ``CacheBehavior`` elements. You must create exactly one default cache behavior.

    - **TargetOriginId** *(string) --* **[REQUIRED]**

      The value of ``ID`` for the origin that you want CloudFront to route requests to when a
      request matches the path pattern either for a cache behavior or for the default cache
      behavior in your distribution.

    - **ForwardedValues** *(dict) --* **[REQUIRED]**

      A complex type that specifies how CloudFront handles query strings and cookies.

      - **QueryString** *(boolean) --* **[REQUIRED]**

        Indicates whether you want CloudFront to forward query strings to the origin that is
        associated with this cache behavior and cache based on the query string parameters.
        CloudFront behavior depends on the value of ``QueryString`` and on the values that you
        specify for ``QueryStringCacheKeys`` , if any:

        If you specify true for ``QueryString`` and you don't specify any values for
        ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin
        and caches based on all query string parameters. Depending on how many query string
        parameters and values you have, this can adversely affect performance because CloudFront
        must forward more requests to the origin.

        If you specify true for ``QueryString`` and you specify one or more values for
        ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin,
        but it only caches based on the query string parameters that you specify.

        If you specify false for ``QueryString`` , CloudFront doesn't forward any query string
        parameters to the origin, and doesn't cache based on query string parameters.

        For more information, see `Configuring CloudFront to Cache Based on Query String
        Parameters
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html>`__
        in the *Amazon CloudFront Developer Guide* .

      - **Cookies** *(dict) --* **[REQUIRED]**

        A complex type that specifies whether you want CloudFront to forward cookies to the
        origin and, if so, which ones. For more information about forwarding cookies to the
        origin, see `How CloudFront Forwards, Caches, and Logs Cookies
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html>`__ in
        the *Amazon CloudFront Developer Guide* .

        - **Forward** *(string) --* **[REQUIRED]**

          Specifies which cookies to forward to the origin for this cache behavior: all, none, or
          the list of cookies specified in the ``WhitelistedNames`` complex type.

          Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an
          Amazon S3 origin, specify none for the ``Forward`` element.

        - **WhitelistedNames** *(dict) --*

          Required if you specify ``whitelist`` for the value of ``Forward:`` . A complex type
          that specifies how many different cookies you want CloudFront to forward to the origin
          for this cache behavior and, if you want to forward selected cookies, the names of
          those cookies.

          If you specify ``all`` or none for the value of ``Forward`` , omit ``WhitelistedNames``
          . If you change the value of ``Forward`` from ``whitelist`` to all or none and you
          don't delete the ``WhitelistedNames`` element and its child elements, CloudFront
          deletes them automatically.

          For the current limit on the number of cookie names that you can whitelist for each
          cache behavior, see `CloudFront Limits
          <https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront>`__
          in the *AWS General Reference* .

          - **Quantity** *(integer) --* **[REQUIRED]**

            The number of different cookies that you want CloudFront to forward to the origin for
            this cache behavior.

          - **Items** *(list) --*

            A complex type that contains one ``Name`` element for each cookie that you want
            CloudFront to forward to the origin for this cache behavior.

            - *(string) --*

      - **Headers** *(dict) --*

        A complex type that specifies the ``Headers`` , if any, that you want CloudFront to
        forward to the origin for this cache behavior (whitelisted headers). For the headers that
        you specify, CloudFront also caches separate versions of a specified object that is based
        on the header values in viewer requests.

        For more information, see `Caching Content Based on Request Headers
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html>`__
        in the *Amazon CloudFront Developer Guide* .

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of different headers that you want CloudFront to base caching on for this
          cache behavior. You can configure each cache behavior in a web distribution to do one
          of the following:

          * **Forward all headers to your origin** : Specify ``1`` for ``Quantity`` and ``*`` for
          ``Name`` .

          .. warning::

             CloudFront doesn't cache the objects that are associated with this cache behavior.
             Instead, CloudFront sends every request to the origin.

          * **Forward a whitelist of headers you specify** : Specify the number of headers that
          you want CloudFront to base caching on. Then specify the header names in ``Name``
          elements. CloudFront caches your objects based on the values in the specified headers.

          * **Forward only the default headers** : Specify ``0`` for ``Quantity`` and omit
          ``Items`` . In this configuration, CloudFront doesn't cache based on the values in the
          request headers.

          Regardless of which option you choose, CloudFront forwards headers to your origin based
          on whether the origin is an S3 bucket or a custom origin. See the following
          documentation:

          * **S3 bucket** : See `HTTP Request Headers That CloudFront Removes or Updates
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorS3Origin.html#request-s3-removed-headers>`__
    """


_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsFailoverCriteriaStatusCodesTypeDef = TypedDict(
    "_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsFailoverCriteriaStatusCodesTypeDef",
    {"Quantity": int, "Items": List[int]},
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsFailoverCriteriaStatusCodesTypeDef(
    _ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsFailoverCriteriaStatusCodesTypeDef
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsFailoverCriteria` `StatusCodes`

    The status codes that, when returned from the primary origin, will trigger CloudFront
    to failover to the second origin.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of status codes.

    - **Items** *(list) --* **[REQUIRED]**

      The items (status codes) for an origin group.

      - *(integer) --*
    """


_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsFailoverCriteriaTypeDef = TypedDict(
    "_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsFailoverCriteriaTypeDef",
    {
        "StatusCodes": ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsFailoverCriteriaStatusCodesTypeDef
    },
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsFailoverCriteriaTypeDef(
    _ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsFailoverCriteriaTypeDef
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItems` `FailoverCriteria`

    A complex type that contains information about the failover criteria for an origin
    group.

    - **StatusCodes** *(dict) --* **[REQUIRED]**

      The status codes that, when returned from the primary origin, will trigger CloudFront
      to failover to the second origin.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of status codes.

      - **Items** *(list) --* **[REQUIRED]**

        The items (status codes) for an origin group.

        - *(integer) --*
    """


_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsMembersItemsTypeDef = TypedDict(
    "_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsMembersItemsTypeDef",
    {"OriginId": str},
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsMembersItemsTypeDef(
    _ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsMembersItemsTypeDef
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsMembers` `Items`

    An origin in an origin group.

    - **OriginId** *(string) --* **[REQUIRED]**

      The ID for an origin in an origin group.
    """


_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsMembersTypeDef = TypedDict(
    "_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsMembersTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsMembersItemsTypeDef
        ],
    },
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsMembersTypeDef(
    _ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsMembersTypeDef
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItems` `Members`

    A complex type that contains information about the origins in an origin group.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of origins in an origin group.

    - **Items** *(list) --* **[REQUIRED]**

      Items (origins) in an origin group.

      - *(dict) --*

        An origin in an origin group.

        - **OriginId** *(string) --* **[REQUIRED]**

          The ID for an origin in an origin group.
    """


_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsTypeDef = TypedDict(
    "_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsTypeDef",
    {
        "Id": str,
        "FailoverCriteria": ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsFailoverCriteriaTypeDef,
        "Members": ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsMembersTypeDef,
    },
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsTypeDef(
    _ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsTypeDef
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroups` `Items`

    An origin group includes two origins (a primary origin and a second origin to failover
    to) and a failover criteria that you specify. You create an origin group to support
    origin failover in CloudFront. When you create or update a distribution, you can specifiy
    the origin group instead of a single origin, and CloudFront will failover from the
    primary origin to the second origin under the failover conditions that you've chosen.

    - **Id** *(string) --* **[REQUIRED]**

      The origin group's ID.

    - **FailoverCriteria** *(dict) --* **[REQUIRED]**

      A complex type that contains information about the failover criteria for an origin
      group.

      - **StatusCodes** *(dict) --* **[REQUIRED]**

        The status codes that, when returned from the primary origin, will trigger CloudFront
        to failover to the second origin.

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of status codes.

        - **Items** *(list) --* **[REQUIRED]**

          The items (status codes) for an origin group.

          - *(integer) --*

    - **Members** *(dict) --* **[REQUIRED]**

      A complex type that contains information about the origins in an origin group.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of origins in an origin group.

      - **Items** *(list) --* **[REQUIRED]**

        Items (origins) in an origin group.

        - *(dict) --*

          An origin in an origin group.

          - **OriginId** *(string) --* **[REQUIRED]**

            The ID for an origin in an origin group.
    """


_RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsTypeDef = TypedDict(
    "_RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsTypeDef",
    {"Quantity": int},
)
_OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsTypeDef = TypedDict(
    "_OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsTypeDef",
    {
        "Items": List[
            ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsItemsTypeDef
        ]
    },
    total=False,
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsTypeDef(
    _RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsTypeDef,
    _OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsTypeDef,
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfig` `OriginGroups`

    A complex type that contains information about origin groups for this distribution.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of origin groups.

    - **Items** *(list) --*

      The items (origin groups) in a distribution.

      - *(dict) --*

        An origin group includes two origins (a primary origin and a second origin to failover
        to) and a failover criteria that you specify. You create an origin group to support
        origin failover in CloudFront. When you create or update a distribution, you can specifiy
        the origin group instead of a single origin, and CloudFront will failover from the
        primary origin to the second origin under the failover conditions that you've chosen.

        - **Id** *(string) --* **[REQUIRED]**

          The origin group's ID.

        - **FailoverCriteria** *(dict) --* **[REQUIRED]**

          A complex type that contains information about the failover criteria for an origin
          group.

          - **StatusCodes** *(dict) --* **[REQUIRED]**

            The status codes that, when returned from the primary origin, will trigger CloudFront
            to failover to the second origin.

            - **Quantity** *(integer) --* **[REQUIRED]**

              The number of status codes.

            - **Items** *(list) --* **[REQUIRED]**

              The items (status codes) for an origin group.

              - *(integer) --*

        - **Members** *(dict) --* **[REQUIRED]**

          A complex type that contains information about the origins in an origin group.

          - **Quantity** *(integer) --* **[REQUIRED]**

            The number of origins in an origin group.

          - **Items** *(list) --* **[REQUIRED]**

            Items (origins) in an origin group.

            - *(dict) --*

              An origin in an origin group.

              - **OriginId** *(string) --* **[REQUIRED]**

                The ID for an origin in an origin group.
    """


_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomHeadersItemsTypeDef = TypedDict(
    "_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomHeadersItemsTypeDef",
    {"HeaderName": str, "HeaderValue": str},
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomHeadersItemsTypeDef(
    _ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomHeadersItemsTypeDef
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomHeaders` `Items`

    A complex type that contains ``HeaderName`` and ``HeaderValue`` elements, if any,
    for this distribution.

    - **HeaderName** *(string) --* **[REQUIRED]**

      The name of a header that you want CloudFront to forward to your origin. For more
      information, see `Forwarding Custom Headers to Your Origin (Web Distributions
      Only)
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html>`__
      in the *Amazon CloudFront Developer Guide* .

    - **HeaderValue** *(string) --* **[REQUIRED]**

      The value for the header that you specified in the ``HeaderName`` field.
    """


_RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomHeadersTypeDef = TypedDict(
    "_RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomHeadersTypeDef",
    {"Quantity": int},
)
_OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomHeadersTypeDef = TypedDict(
    "_OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomHeadersTypeDef",
    {
        "Items": List[
            ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomHeadersItemsTypeDef
        ]
    },
    total=False,
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomHeadersTypeDef(
    _RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomHeadersTypeDef,
    _OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomHeadersTypeDef,
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItems` `CustomHeaders`

    A complex type that contains names and values for the custom headers that you want.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of custom headers, if any, for this distribution.

    - **Items** *(list) --*

       **Optional** : A list that contains one ``OriginCustomHeader`` element for each
       custom header that you want CloudFront to forward to the origin. If Quantity is
       ``0`` , omit ``Items`` .

      - *(dict) --*

        A complex type that contains ``HeaderName`` and ``HeaderValue`` elements, if any,
        for this distribution.

        - **HeaderName** *(string) --* **[REQUIRED]**

          The name of a header that you want CloudFront to forward to your origin. For more
          information, see `Forwarding Custom Headers to Your Origin (Web Distributions
          Only)
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html>`__
          in the *Amazon CloudFront Developer Guide* .

        - **HeaderValue** *(string) --* **[REQUIRED]**

          The value for the header that you specified in the ``HeaderName`` field.
    """


_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomOriginConfigOriginSslProtocolsTypeDef = TypedDict(
    "_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomOriginConfigOriginSslProtocolsTypeDef",
    {"Quantity": int, "Items": List[str]},
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomOriginConfigOriginSslProtocolsTypeDef(
    _ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomOriginConfigOriginSslProtocolsTypeDef
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomOriginConfig` `OriginSslProtocols`

    The SSL/TLS protocols that you want CloudFront to use when communicating with your
    origin over HTTPS.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of SSL/TLS protocols that you want to allow CloudFront to use when
      establishing an HTTPS connection with this origin.

    - **Items** *(list) --* **[REQUIRED]**

      A list that contains allowed SSL/TLS protocols for this distribution.

      - *(string) --*
    """


_RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomOriginConfigTypeDef = TypedDict(
    "_RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomOriginConfigTypeDef",
    {"HTTPPort": int, "HTTPSPort": int, "OriginProtocolPolicy": str},
)
_OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomOriginConfigTypeDef = TypedDict(
    "_OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomOriginConfigTypeDef",
    {
        "OriginSslProtocols": ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomOriginConfigOriginSslProtocolsTypeDef,
        "OriginReadTimeout": int,
        "OriginKeepaliveTimeout": int,
    },
    total=False,
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomOriginConfigTypeDef(
    _RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomOriginConfigTypeDef,
    _OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomOriginConfigTypeDef,
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItems` `CustomOriginConfig`

    A complex type that contains information about a custom origin. If the origin is an
    Amazon S3 bucket, use the ``S3OriginConfig`` element instead.

    - **HTTPPort** *(integer) --* **[REQUIRED]**

      The HTTP port the custom origin listens on.

    - **HTTPSPort** *(integer) --* **[REQUIRED]**

      The HTTPS port the custom origin listens on.

    - **OriginProtocolPolicy** *(string) --* **[REQUIRED]**

      The origin protocol policy to apply to your origin.

    - **OriginSslProtocols** *(dict) --*

      The SSL/TLS protocols that you want CloudFront to use when communicating with your
      origin over HTTPS.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of SSL/TLS protocols that you want to allow CloudFront to use when
        establishing an HTTPS connection with this origin.

      - **Items** *(list) --* **[REQUIRED]**

        A list that contains allowed SSL/TLS protocols for this distribution.

        - *(string) --*

    - **OriginReadTimeout** *(integer) --*

      You can create a custom origin read timeout. All timeout units are in seconds. The
      default origin read timeout is 30 seconds, but you can configure custom timeout
      lengths using the CloudFront API. The minimum timeout length is 4 seconds; the
      maximum is 60 seconds.

      If you need to increase the maximum time limit, contact the `AWS Support Center
      <https://console.aws.amazon.com/support/home#/>`__ .

    - **OriginKeepaliveTimeout** *(integer) --*

      You can create a custom keep-alive timeout. All timeout units are in seconds. The
      default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths
      using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60
      seconds.

      If you need to increase the maximum time limit, contact the `AWS Support Center
      <https://console.aws.amazon.com/support/home#/>`__ .
    """


_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsS3OriginConfigTypeDef = TypedDict(
    "_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsS3OriginConfigTypeDef",
    {"OriginAccessIdentity": str},
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsS3OriginConfigTypeDef(
    _ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsS3OriginConfigTypeDef
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItems` `S3OriginConfig`

    A complex type that contains information about the Amazon S3 origin. If the origin is a
    custom origin, use the ``CustomOriginConfig`` element instead.

    - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

      The CloudFront origin access identity to associate with the origin. Use an origin
      access identity to configure the origin so that viewers can *only* access objects in
      an Amazon S3 bucket through CloudFront. The format of the value is:

      origin-access-identity/cloudfront/*ID-of-origin-access-identity*

      where `` *ID-of-origin-access-identity* `` is the value that CloudFront returned in
      the ``ID`` element when you created the origin access identity.

      If you want viewers to be able to access objects using either the CloudFront URL or
      the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

      To delete the origin access identity from an existing distribution, update the
      distribution configuration and include an empty ``OriginAccessIdentity`` element.

      To replace the origin access identity, update the distribution configuration and
      specify the new origin access identity.

      For more information about the origin access identity, see `Serving Private Content
      through CloudFront
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
      in the *Amazon CloudFront Developer Guide* .
    """


_RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsTypeDef = TypedDict(
    "_RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsTypeDef",
    {"Id": str, "DomainName": str},
)
_OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsTypeDef = TypedDict(
    "_OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsTypeDef",
    {
        "OriginPath": str,
        "CustomHeaders": ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomHeadersTypeDef,
        "S3OriginConfig": ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsS3OriginConfigTypeDef,
        "CustomOriginConfig": ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsCustomOriginConfigTypeDef,
    },
    total=False,
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsTypeDef(
    _RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsTypeDef,
    _OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsTypeDef,
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOrigins` `Items`

    A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web
    server), Amazon MediaStore, or other server from which CloudFront gets your files. This
    can also be an origin group, if you've created an origin group. You must specify at least
    one origin or origin group.

    For the current limit on the number of origins or origin groups that you can specify for
    a distribution, see `Amazon CloudFront Limits
    <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront>`__
    in the *AWS General Reference* .

    - **Id** *(string) --* **[REQUIRED]**

      A unique identifier for the origin or origin group. The value of ``Id`` must be unique
      within the distribution.

      When you specify the value of ``TargetOriginId`` for the default cache behavior or for
      another cache behavior, you indicate the origin to which you want the cache behavior to
      route requests by specifying the value of the ``Id`` element for that origin. When a
      request matches the path pattern for that cache behavior, CloudFront routes the request
      to the specified origin. For more information, see `Cache Behavior Settings
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior>`__
      in the *Amazon CloudFront Developer Guide* .

    - **DomainName** *(string) --* **[REQUIRED]**

       **Amazon S3 origins** : The DNS name of the Amazon S3 bucket from which you want
       CloudFront to get objects for this origin, for example,
       ``myawsbucket.s3.amazonaws.com`` . If you set up your bucket to be configured as a
       website endpoint, enter the Amazon S3 static website hosting endpoint for the bucket.

      For more information about specifying this value for different types of origins, see
      `Origin Domain Name
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesDomainName>`__
      in the *Amazon CloudFront Developer Guide* .

      Constraints for Amazon S3 origins:

      * If you configured Amazon S3 Transfer Acceleration for your bucket, don't specify the
      ``s3-accelerate`` endpoint for ``DomainName`` .

      * The bucket name must be between 3 and 63 characters long (inclusive).

      * The bucket name must contain only lowercase characters, numbers, periods,
      underscores, and dashes.

      * The bucket name must not contain adjacent periods.

       **Custom Origins** : The DNS domain name for the HTTP server from which you want
       CloudFront to get objects for this origin, for example, ``www.example.com`` .

      Constraints for custom origins:

      * ``DomainName`` must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.),
      hyphen (-), or underscore (_) characters.

      * The name cannot exceed 128 characters.

    - **OriginPath** *(string) --*

      An optional element that causes CloudFront to request your content from a directory in
      your Amazon S3 bucket or your custom origin. When you include the ``OriginPath``
      element, specify the directory name, beginning with a ``/`` . CloudFront appends the
      directory name to the value of ``DomainName`` , for example, ``example.com/production``
      . Do not include a ``/`` at the end of the directory name.

      For example, suppose you've specified the following values for your distribution:

      * ``DomainName`` : An Amazon S3 bucket named ``myawsbucket`` .

      * ``OriginPath`` : ``/production``

      * ``CNAME`` : ``example.com``

      When a user enters ``example.com/index.html`` in a browser, CloudFront sends a request
      to Amazon S3 for ``myawsbucket/production/index.html`` .

      When a user enters ``example.com/acme/index.html`` in a browser, CloudFront sends a
      request to Amazon S3 for ``myawsbucket/production/acme/index.html`` .

    - **CustomHeaders** *(dict) --*

      A complex type that contains names and values for the custom headers that you want.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of custom headers, if any, for this distribution.

      - **Items** *(list) --*

         **Optional** : A list that contains one ``OriginCustomHeader`` element for each
         custom header that you want CloudFront to forward to the origin. If Quantity is
         ``0`` , omit ``Items`` .

        - *(dict) --*

          A complex type that contains ``HeaderName`` and ``HeaderValue`` elements, if any,
          for this distribution.

          - **HeaderName** *(string) --* **[REQUIRED]**

            The name of a header that you want CloudFront to forward to your origin. For more
            information, see `Forwarding Custom Headers to Your Origin (Web Distributions
            Only)
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html>`__
            in the *Amazon CloudFront Developer Guide* .

          - **HeaderValue** *(string) --* **[REQUIRED]**

            The value for the header that you specified in the ``HeaderName`` field.

    - **S3OriginConfig** *(dict) --*

      A complex type that contains information about the Amazon S3 origin. If the origin is a
      custom origin, use the ``CustomOriginConfig`` element instead.

      - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

        The CloudFront origin access identity to associate with the origin. Use an origin
        access identity to configure the origin so that viewers can *only* access objects in
        an Amazon S3 bucket through CloudFront. The format of the value is:

        origin-access-identity/cloudfront/*ID-of-origin-access-identity*

        where `` *ID-of-origin-access-identity* `` is the value that CloudFront returned in
        the ``ID`` element when you created the origin access identity.

        If you want viewers to be able to access objects using either the CloudFront URL or
        the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

        To delete the origin access identity from an existing distribution, update the
        distribution configuration and include an empty ``OriginAccessIdentity`` element.

        To replace the origin access identity, update the distribution configuration and
        specify the new origin access identity.

        For more information about the origin access identity, see `Serving Private Content
        through CloudFront
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
        in the *Amazon CloudFront Developer Guide* .

    - **CustomOriginConfig** *(dict) --*

      A complex type that contains information about a custom origin. If the origin is an
      Amazon S3 bucket, use the ``S3OriginConfig`` element instead.

      - **HTTPPort** *(integer) --* **[REQUIRED]**

        The HTTP port the custom origin listens on.

      - **HTTPSPort** *(integer) --* **[REQUIRED]**

        The HTTPS port the custom origin listens on.

      - **OriginProtocolPolicy** *(string) --* **[REQUIRED]**

        The origin protocol policy to apply to your origin.

      - **OriginSslProtocols** *(dict) --*

        The SSL/TLS protocols that you want CloudFront to use when communicating with your
        origin over HTTPS.

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of SSL/TLS protocols that you want to allow CloudFront to use when
          establishing an HTTPS connection with this origin.

        - **Items** *(list) --* **[REQUIRED]**

          A list that contains allowed SSL/TLS protocols for this distribution.

          - *(string) --*

      - **OriginReadTimeout** *(integer) --*

        You can create a custom origin read timeout. All timeout units are in seconds. The
        default origin read timeout is 30 seconds, but you can configure custom timeout
        lengths using the CloudFront API. The minimum timeout length is 4 seconds; the
        maximum is 60 seconds.

        If you need to increase the maximum time limit, contact the `AWS Support Center
        <https://console.aws.amazon.com/support/home#/>`__ .

      - **OriginKeepaliveTimeout** *(integer) --*

        You can create a custom keep-alive timeout. All timeout units are in seconds. The
        default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths
        using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60
        seconds.

        If you need to increase the maximum time limit, contact the `AWS Support Center
        <https://console.aws.amazon.com/support/home#/>`__ .
    """


_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsTypeDef = TypedDict(
    "_ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsItemsTypeDef
        ],
    },
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsTypeDef(
    _ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsTypeDef
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfig` `Origins`

    A complex type that contains information about origins for this distribution.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of origins or origin groups for this distribution.

    - **Items** *(list) --* **[REQUIRED]**

      A complex type that contains origins or origin groups for this distribution.

      - *(dict) --*

        A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web
        server), Amazon MediaStore, or other server from which CloudFront gets your files. This
        can also be an origin group, if you've created an origin group. You must specify at least
        one origin or origin group.

        For the current limit on the number of origins or origin groups that you can specify for
        a distribution, see `Amazon CloudFront Limits
        <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront>`__
        in the *AWS General Reference* .

        - **Id** *(string) --* **[REQUIRED]**

          A unique identifier for the origin or origin group. The value of ``Id`` must be unique
          within the distribution.

          When you specify the value of ``TargetOriginId`` for the default cache behavior or for
          another cache behavior, you indicate the origin to which you want the cache behavior to
          route requests by specifying the value of the ``Id`` element for that origin. When a
          request matches the path pattern for that cache behavior, CloudFront routes the request
          to the specified origin. For more information, see `Cache Behavior Settings
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior>`__
          in the *Amazon CloudFront Developer Guide* .

        - **DomainName** *(string) --* **[REQUIRED]**

           **Amazon S3 origins** : The DNS name of the Amazon S3 bucket from which you want
           CloudFront to get objects for this origin, for example,
           ``myawsbucket.s3.amazonaws.com`` . If you set up your bucket to be configured as a
           website endpoint, enter the Amazon S3 static website hosting endpoint for the bucket.

          For more information about specifying this value for different types of origins, see
          `Origin Domain Name
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesDomainName>`__
          in the *Amazon CloudFront Developer Guide* .

          Constraints for Amazon S3 origins:

          * If you configured Amazon S3 Transfer Acceleration for your bucket, don't specify the
          ``s3-accelerate`` endpoint for ``DomainName`` .

          * The bucket name must be between 3 and 63 characters long (inclusive).

          * The bucket name must contain only lowercase characters, numbers, periods,
          underscores, and dashes.

          * The bucket name must not contain adjacent periods.

           **Custom Origins** : The DNS domain name for the HTTP server from which you want
           CloudFront to get objects for this origin, for example, ``www.example.com`` .

          Constraints for custom origins:

          * ``DomainName`` must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.),
          hyphen (-), or underscore (_) characters.

          * The name cannot exceed 128 characters.

        - **OriginPath** *(string) --*

          An optional element that causes CloudFront to request your content from a directory in
          your Amazon S3 bucket or your custom origin. When you include the ``OriginPath``
          element, specify the directory name, beginning with a ``/`` . CloudFront appends the
          directory name to the value of ``DomainName`` , for example, ``example.com/production``
          . Do not include a ``/`` at the end of the directory name.

          For example, suppose you've specified the following values for your distribution:

          * ``DomainName`` : An Amazon S3 bucket named ``myawsbucket`` .

          * ``OriginPath`` : ``/production``

          * ``CNAME`` : ``example.com``

          When a user enters ``example.com/index.html`` in a browser, CloudFront sends a request
          to Amazon S3 for ``myawsbucket/production/index.html`` .

          When a user enters ``example.com/acme/index.html`` in a browser, CloudFront sends a
          request to Amazon S3 for ``myawsbucket/production/acme/index.html`` .

        - **CustomHeaders** *(dict) --*

          A complex type that contains names and values for the custom headers that you want.

          - **Quantity** *(integer) --* **[REQUIRED]**

            The number of custom headers, if any, for this distribution.

          - **Items** *(list) --*

             **Optional** : A list that contains one ``OriginCustomHeader`` element for each
             custom header that you want CloudFront to forward to the origin. If Quantity is
             ``0`` , omit ``Items`` .

            - *(dict) --*

              A complex type that contains ``HeaderName`` and ``HeaderValue`` elements, if any,
              for this distribution.

              - **HeaderName** *(string) --* **[REQUIRED]**

                The name of a header that you want CloudFront to forward to your origin. For more
                information, see `Forwarding Custom Headers to Your Origin (Web Distributions
                Only)
                <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html>`__
                in the *Amazon CloudFront Developer Guide* .

              - **HeaderValue** *(string) --* **[REQUIRED]**

                The value for the header that you specified in the ``HeaderName`` field.

        - **S3OriginConfig** *(dict) --*

          A complex type that contains information about the Amazon S3 origin. If the origin is a
          custom origin, use the ``CustomOriginConfig`` element instead.

          - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

            The CloudFront origin access identity to associate with the origin. Use an origin
            access identity to configure the origin so that viewers can *only* access objects in
            an Amazon S3 bucket through CloudFront. The format of the value is:

            origin-access-identity/cloudfront/*ID-of-origin-access-identity*

            where `` *ID-of-origin-access-identity* `` is the value that CloudFront returned in
            the ``ID`` element when you created the origin access identity.

            If you want viewers to be able to access objects using either the CloudFront URL or
            the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

            To delete the origin access identity from an existing distribution, update the
            distribution configuration and include an empty ``OriginAccessIdentity`` element.

            To replace the origin access identity, update the distribution configuration and
            specify the new origin access identity.

            For more information about the origin access identity, see `Serving Private Content
            through CloudFront
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
            in the *Amazon CloudFront Developer Guide* .

        - **CustomOriginConfig** *(dict) --*

          A complex type that contains information about a custom origin. If the origin is an
          Amazon S3 bucket, use the ``S3OriginConfig`` element instead.

          - **HTTPPort** *(integer) --* **[REQUIRED]**

            The HTTP port the custom origin listens on.

          - **HTTPSPort** *(integer) --* **[REQUIRED]**

            The HTTPS port the custom origin listens on.

          - **OriginProtocolPolicy** *(string) --* **[REQUIRED]**

            The origin protocol policy to apply to your origin.

          - **OriginSslProtocols** *(dict) --*

            The SSL/TLS protocols that you want CloudFront to use when communicating with your
            origin over HTTPS.

            - **Quantity** *(integer) --* **[REQUIRED]**

              The number of SSL/TLS protocols that you want to allow CloudFront to use when
              establishing an HTTPS connection with this origin.

            - **Items** *(list) --* **[REQUIRED]**

              A list that contains allowed SSL/TLS protocols for this distribution.

              - *(string) --*

          - **OriginReadTimeout** *(integer) --*

            You can create a custom origin read timeout. All timeout units are in seconds. The
            default origin read timeout is 30 seconds, but you can configure custom timeout
            lengths using the CloudFront API. The minimum timeout length is 4 seconds; the
            maximum is 60 seconds.

            If you need to increase the maximum time limit, contact the `AWS Support Center
            <https://console.aws.amazon.com/support/home#/>`__ .

          - **OriginKeepaliveTimeout** *(integer) --*

            You can create a custom keep-alive timeout. All timeout units are in seconds. The
            default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths
            using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60
            seconds.

            If you need to increase the maximum time limit, contact the `AWS Support Center
            <https://console.aws.amazon.com/support/home#/>`__ .
    """


_RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigTypeDef = TypedDict(
    "_RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "Origins": ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginsTypeDef,
        "DefaultCacheBehavior": ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigDefaultCacheBehaviorTypeDef,
    },
)
_OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigTypeDef = TypedDict(
    "_OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigTypeDef",
    {
        "Aliases": ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigAliasesTypeDef,
        "DefaultRootObject": str,
        "OriginGroups": ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigOriginGroupsTypeDef,
    },
    total=False,
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigTypeDef(
    _RequiredClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigTypeDef,
    _OptionalClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigTypeDef,
):
    """
    Type definition for `ClientCreateDistributionWithTagsDistributionConfigWithTags` `DistributionConfig`

    A distribution configuration.

    - **CallerReference** *(string) --* **[REQUIRED]**

      A unique value (for example, a date-time stamp) that ensures that the request can't be
      replayed.

      If the value of ``CallerReference`` is new (regardless of the content of the
      ``DistributionConfig`` object), CloudFront creates a new distribution.

      If ``CallerReference`` is a value that you already sent in a previous request to create a
      distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

    - **Aliases** *(dict) --*

      A complex type that contains information about CNAMEs (alternate domain names), if any, for
      this distribution.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of CNAME aliases, if any, that you want to associate with this distribution.

      - **Items** *(list) --*

        A complex type that contains the CNAME aliases, if any, that you want to associate with
        this distribution.

        - *(string) --*

    - **DefaultRootObject** *(string) --*

      The object that you want CloudFront to request from your origin (for example, ``index.html``
      ) when a viewer requests the root URL for your distribution (``http://www.example.com`` )
      instead of an object in your distribution
      (``http://www.example.com/product-description.html`` ). Specifying a default root object
      avoids exposing the contents of your distribution.

      Specify only the object name, for example, ``index.html`` . Don't add a ``/`` before the
      object name.

      If you don't want to specify a default root object when you create a distribution, include an
      empty ``DefaultRootObject`` element.

      To delete the default root object from an existing distribution, update the distribution
      configuration and include an empty ``DefaultRootObject`` element.

      To replace the default root object, update the distribution configuration and specify the new
      object.

      For more information about the default root object, see `Creating a Default Root Object
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html>`__
      in the *Amazon CloudFront Developer Guide* .

    - **Origins** *(dict) --* **[REQUIRED]**

      A complex type that contains information about origins for this distribution.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of origins or origin groups for this distribution.

      - **Items** *(list) --* **[REQUIRED]**

        A complex type that contains origins or origin groups for this distribution.

        - *(dict) --*

          A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web
          server), Amazon MediaStore, or other server from which CloudFront gets your files. This
          can also be an origin group, if you've created an origin group. You must specify at least
          one origin or origin group.

          For the current limit on the number of origins or origin groups that you can specify for
          a distribution, see `Amazon CloudFront Limits
          <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront>`__
          in the *AWS General Reference* .

          - **Id** *(string) --* **[REQUIRED]**

            A unique identifier for the origin or origin group. The value of ``Id`` must be unique
            within the distribution.

            When you specify the value of ``TargetOriginId`` for the default cache behavior or for
            another cache behavior, you indicate the origin to which you want the cache behavior to
            route requests by specifying the value of the ``Id`` element for that origin. When a
            request matches the path pattern for that cache behavior, CloudFront routes the request
            to the specified origin. For more information, see `Cache Behavior Settings
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior>`__
            in the *Amazon CloudFront Developer Guide* .

          - **DomainName** *(string) --* **[REQUIRED]**

             **Amazon S3 origins** : The DNS name of the Amazon S3 bucket from which you want
             CloudFront to get objects for this origin, for example,
             ``myawsbucket.s3.amazonaws.com`` . If you set up your bucket to be configured as a
             website endpoint, enter the Amazon S3 static website hosting endpoint for the bucket.

            For more information about specifying this value for different types of origins, see
            `Origin Domain Name
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesDomainName>`__
            in the *Amazon CloudFront Developer Guide* .

            Constraints for Amazon S3 origins:

            * If you configured Amazon S3 Transfer Acceleration for your bucket, don't specify the
            ``s3-accelerate`` endpoint for ``DomainName`` .

            * The bucket name must be between 3 and 63 characters long (inclusive).

            * The bucket name must contain only lowercase characters, numbers, periods,
            underscores, and dashes.

            * The bucket name must not contain adjacent periods.

             **Custom Origins** : The DNS domain name for the HTTP server from which you want
             CloudFront to get objects for this origin, for example, ``www.example.com`` .

            Constraints for custom origins:

            * ``DomainName`` must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.),
            hyphen (-), or underscore (_) characters.

            * The name cannot exceed 128 characters.

          - **OriginPath** *(string) --*

            An optional element that causes CloudFront to request your content from a directory in
            your Amazon S3 bucket or your custom origin. When you include the ``OriginPath``
            element, specify the directory name, beginning with a ``/`` . CloudFront appends the
            directory name to the value of ``DomainName`` , for example, ``example.com/production``
            . Do not include a ``/`` at the end of the directory name.

            For example, suppose you've specified the following values for your distribution:

            * ``DomainName`` : An Amazon S3 bucket named ``myawsbucket`` .

            * ``OriginPath`` : ``/production``

            * ``CNAME`` : ``example.com``

            When a user enters ``example.com/index.html`` in a browser, CloudFront sends a request
            to Amazon S3 for ``myawsbucket/production/index.html`` .

            When a user enters ``example.com/acme/index.html`` in a browser, CloudFront sends a
            request to Amazon S3 for ``myawsbucket/production/acme/index.html`` .

          - **CustomHeaders** *(dict) --*

            A complex type that contains names and values for the custom headers that you want.

            - **Quantity** *(integer) --* **[REQUIRED]**

              The number of custom headers, if any, for this distribution.

            - **Items** *(list) --*

               **Optional** : A list that contains one ``OriginCustomHeader`` element for each
               custom header that you want CloudFront to forward to the origin. If Quantity is
               ``0`` , omit ``Items`` .

              - *(dict) --*

                A complex type that contains ``HeaderName`` and ``HeaderValue`` elements, if any,
                for this distribution.

                - **HeaderName** *(string) --* **[REQUIRED]**

                  The name of a header that you want CloudFront to forward to your origin. For more
                  information, see `Forwarding Custom Headers to Your Origin (Web Distributions
                  Only)
                  <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html>`__
                  in the *Amazon CloudFront Developer Guide* .

                - **HeaderValue** *(string) --* **[REQUIRED]**

                  The value for the header that you specified in the ``HeaderName`` field.

          - **S3OriginConfig** *(dict) --*

            A complex type that contains information about the Amazon S3 origin. If the origin is a
            custom origin, use the ``CustomOriginConfig`` element instead.

            - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

              The CloudFront origin access identity to associate with the origin. Use an origin
              access identity to configure the origin so that viewers can *only* access objects in
              an Amazon S3 bucket through CloudFront. The format of the value is:

              origin-access-identity/cloudfront/*ID-of-origin-access-identity*

              where `` *ID-of-origin-access-identity* `` is the value that CloudFront returned in
              the ``ID`` element when you created the origin access identity.

              If you want viewers to be able to access objects using either the CloudFront URL or
              the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

              To delete the origin access identity from an existing distribution, update the
              distribution configuration and include an empty ``OriginAccessIdentity`` element.

              To replace the origin access identity, update the distribution configuration and
              specify the new origin access identity.

              For more information about the origin access identity, see `Serving Private Content
              through CloudFront
              <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
              in the *Amazon CloudFront Developer Guide* .

          - **CustomOriginConfig** *(dict) --*

            A complex type that contains information about a custom origin. If the origin is an
            Amazon S3 bucket, use the ``S3OriginConfig`` element instead.

            - **HTTPPort** *(integer) --* **[REQUIRED]**

              The HTTP port the custom origin listens on.

            - **HTTPSPort** *(integer) --* **[REQUIRED]**

              The HTTPS port the custom origin listens on.

            - **OriginProtocolPolicy** *(string) --* **[REQUIRED]**

              The origin protocol policy to apply to your origin.

            - **OriginSslProtocols** *(dict) --*

              The SSL/TLS protocols that you want CloudFront to use when communicating with your
              origin over HTTPS.

              - **Quantity** *(integer) --* **[REQUIRED]**

                The number of SSL/TLS protocols that you want to allow CloudFront to use when
                establishing an HTTPS connection with this origin.

              - **Items** *(list) --* **[REQUIRED]**

                A list that contains allowed SSL/TLS protocols for this distribution.

                - *(string) --*

            - **OriginReadTimeout** *(integer) --*

              You can create a custom origin read timeout. All timeout units are in seconds. The
              default origin read timeout is 30 seconds, but you can configure custom timeout
              lengths using the CloudFront API. The minimum timeout length is 4 seconds; the
              maximum is 60 seconds.

              If you need to increase the maximum time limit, contact the `AWS Support Center
              <https://console.aws.amazon.com/support/home#/>`__ .

            - **OriginKeepaliveTimeout** *(integer) --*

              You can create a custom keep-alive timeout. All timeout units are in seconds. The
              default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths
              using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60
              seconds.

              If you need to increase the maximum time limit, contact the `AWS Support Center
              <https://console.aws.amazon.com/support/home#/>`__ .

    - **OriginGroups** *(dict) --*

      A complex type that contains information about origin groups for this distribution.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of origin groups.

      - **Items** *(list) --*

        The items (origin groups) in a distribution.

        - *(dict) --*

          An origin group includes two origins (a primary origin and a second origin to failover
          to) and a failover criteria that you specify. You create an origin group to support
          origin failover in CloudFront. When you create or update a distribution, you can specifiy
          the origin group instead of a single origin, and CloudFront will failover from the
          primary origin to the second origin under the failover conditions that you've chosen.

          - **Id** *(string) --* **[REQUIRED]**

            The origin group's ID.

          - **FailoverCriteria** *(dict) --* **[REQUIRED]**

            A complex type that contains information about the failover criteria for an origin
            group.

            - **StatusCodes** *(dict) --* **[REQUIRED]**

              The status codes that, when returned from the primary origin, will trigger CloudFront
              to failover to the second origin.

              - **Quantity** *(integer) --* **[REQUIRED]**

                The number of status codes.

              - **Items** *(list) --* **[REQUIRED]**

                The items (status codes) for an origin group.

                - *(integer) --*

          - **Members** *(dict) --* **[REQUIRED]**

            A complex type that contains information about the origins in an origin group.

            - **Quantity** *(integer) --* **[REQUIRED]**

              The number of origins in an origin group.

            - **Items** *(list) --* **[REQUIRED]**

              Items (origins) in an origin group.

              - *(dict) --*

                An origin in an origin group.

                - **OriginId** *(string) --* **[REQUIRED]**

                  The ID for an origin in an origin group.

    - **DefaultCacheBehavior** *(dict) --* **[REQUIRED]**

      A complex type that describes the default cache behavior if you don't specify a
      ``CacheBehavior`` element or if files don't match any of the values of ``PathPattern`` in
      ``CacheBehavior`` elements. You must create exactly one default cache behavior.

      - **TargetOriginId** *(string) --* **[REQUIRED]**

        The value of ``ID`` for the origin that you want CloudFront to route requests to when a
        request matches the path pattern either for a cache behavior or for the default cache
        behavior in your distribution.

      - **ForwardedValues** *(dict) --* **[REQUIRED]**

        A complex type that specifies how CloudFront handles query strings and cookies.

        - **QueryString** *(boolean) --* **[REQUIRED]**

          Indicates whether you want CloudFront to forward query strings to the origin that is
          associated with this cache behavior and cache based on the query string parameters.
          CloudFront behavior depends on the value of ``QueryString`` and on the values that you
          specify for ``QueryStringCacheKeys`` , if any:

          If you specify true for ``QueryString`` and you don't specify any values for
          ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin
          and caches based on all query string parameters. Depending on how many query string
          parameters and values you have, this can adversely affect performance because CloudFront
          must forward more requests to the origin.

          If you specify true for ``QueryString`` and you specify one or more values for
          ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin,
          but it only caches based on the query string parameters that you specify.

          If you specify false for ``QueryString`` , CloudFront doesn't forward any query string
          parameters to the origin, and doesn't cache based on query string parameters.

          For more information, see `Configuring CloudFront to Cache Based on Query String
          Parameters
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html>`__
          in the *Amazon CloudFront Developer Guide* .

        - **Cookies** *(dict) --* **[REQUIRED]**

          A complex type that specifies whether you want CloudFront to forward cookies to the
          origin and, if so, which ones. For more information about forwarding cookies to the
          origin, see `How CloudFront Forwards, Caches, and Logs Cookies
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html>`__ in
          the *Amazon CloudFront Developer Guide* .

          - **Forward** *(string) --* **[REQUIRED]**

            Specifies which cookies to forward to the origin for this cache behavior: all, none, or
            the list of cookies specified in the ``WhitelistedNames`` complex type.

            Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an
            Amazon S3 origin, specify none for the ``Forward`` element.

          - **WhitelistedNames** *(dict) --*

            Required if you specify ``whitelist`` for the value of ``Forward:`` . A complex type
            that specifies how many different cookies you want CloudFront to forward to the origin
            for this cache behavior and, if you want to forward selected cookies, the names of
            those cookies.

            If you specify ``all`` or none for the value of ``Forward`` , omit ``WhitelistedNames``
            . If you change the value of ``Forward`` from ``whitelist`` to all or none and you
            don't delete the ``WhitelistedNames`` element and its child elements, CloudFront
            deletes them automatically.

            For the current limit on the number of cookie names that you can whitelist for each
            cache behavior, see `CloudFront Limits
            <https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront>`__
            in the *AWS General Reference* .

            - **Quantity** *(integer) --* **[REQUIRED]**

              The number of different cookies that you want CloudFront to forward to the origin for
              this cache behavior.

            - **Items** *(list) --*

              A complex type that contains one ``Name`` element for each cookie that you want
              CloudFront to forward to the origin for this cache behavior.

              - *(string) --*

        - **Headers** *(dict) --*

          A complex type that specifies the ``Headers`` , if any, that you want CloudFront to
          forward to the origin for this cache behavior (whitelisted headers). For the headers that
          you specify, CloudFront also caches separate versions of a specified object that is based
          on the header values in viewer requests.

          For more information, see `Caching Content Based on Request Headers
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html>`__
          in the *Amazon CloudFront Developer Guide* .

          - **Quantity** *(integer) --* **[REQUIRED]**

            The number of different headers that you want CloudFront to base caching on for this
            cache behavior. You can configure each cache behavior in a web distribution to do one
            of the following:

            * **Forward all headers to your origin** : Specify ``1`` for ``Quantity`` and ``*`` for
            ``Name`` .

            .. warning::

               CloudFront doesn't cache the objects that are associated with this cache behavior.
               Instead, CloudFront sends every request to the origin.

            * **Forward a whitelist of headers you specify** : Specify the number of headers that
            you want CloudFront to base caching on. Then specify the header names in ``Name``
            elements. CloudFront caches your objects based on the values in the specified headers.

            * **Forward only the default headers** : Specify ``0`` for ``Quantity`` and omit
            ``Items`` . In this configuration, CloudFront doesn't cache based on the values in the
            request headers.

            Regardless of which option you choose, CloudFront forwards headers to your origin based
            on whether the origin is an S3 bucket or a custom origin. See the following
            documentation:

            * **S3 bucket** : See `HTTP Request Headers That CloudFront Removes or Updates
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorS3Origin.html#request-s3-removed-headers>`__
    """


_ClientCreateDistributionWithTagsDistributionConfigWithTagsTypeDef = TypedDict(
    "_ClientCreateDistributionWithTagsDistributionConfigWithTagsTypeDef",
    {
        "DistributionConfig": ClientCreateDistributionWithTagsDistributionConfigWithTagsDistributionConfigTypeDef
    },
)


class ClientCreateDistributionWithTagsDistributionConfigWithTagsTypeDef(
    _ClientCreateDistributionWithTagsDistributionConfigWithTagsTypeDef
):
    """
    Type definition for `ClientCreateDistributionWithTags` `DistributionConfigWithTags`

    The distribution's configuration information.

    - **DistributionConfig** *(dict) --* **[REQUIRED]**

      A distribution configuration.

      - **CallerReference** *(string) --* **[REQUIRED]**

        A unique value (for example, a date-time stamp) that ensures that the request can't be
        replayed.

        If the value of ``CallerReference`` is new (regardless of the content of the
        ``DistributionConfig`` object), CloudFront creates a new distribution.

        If ``CallerReference`` is a value that you already sent in a previous request to create a
        distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

      - **Aliases** *(dict) --*

        A complex type that contains information about CNAMEs (alternate domain names), if any, for
        this distribution.

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of CNAME aliases, if any, that you want to associate with this distribution.

        - **Items** *(list) --*

          A complex type that contains the CNAME aliases, if any, that you want to associate with
          this distribution.

          - *(string) --*

      - **DefaultRootObject** *(string) --*

        The object that you want CloudFront to request from your origin (for example, ``index.html``
        ) when a viewer requests the root URL for your distribution (``http://www.example.com`` )
        instead of an object in your distribution
        (``http://www.example.com/product-description.html`` ). Specifying a default root object
        avoids exposing the contents of your distribution.

        Specify only the object name, for example, ``index.html`` . Don't add a ``/`` before the
        object name.

        If you don't want to specify a default root object when you create a distribution, include an
        empty ``DefaultRootObject`` element.

        To delete the default root object from an existing distribution, update the distribution
        configuration and include an empty ``DefaultRootObject`` element.

        To replace the default root object, update the distribution configuration and specify the new
        object.

        For more information about the default root object, see `Creating a Default Root Object
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html>`__
        in the *Amazon CloudFront Developer Guide* .

      - **Origins** *(dict) --* **[REQUIRED]**

        A complex type that contains information about origins for this distribution.

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of origins or origin groups for this distribution.

        - **Items** *(list) --* **[REQUIRED]**

          A complex type that contains origins or origin groups for this distribution.

          - *(dict) --*

            A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web
            server), Amazon MediaStore, or other server from which CloudFront gets your files. This
            can also be an origin group, if you've created an origin group. You must specify at least
            one origin or origin group.

            For the current limit on the number of origins or origin groups that you can specify for
            a distribution, see `Amazon CloudFront Limits
            <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront>`__
            in the *AWS General Reference* .

            - **Id** *(string) --* **[REQUIRED]**

              A unique identifier for the origin or origin group. The value of ``Id`` must be unique
              within the distribution.

              When you specify the value of ``TargetOriginId`` for the default cache behavior or for
              another cache behavior, you indicate the origin to which you want the cache behavior to
              route requests by specifying the value of the ``Id`` element for that origin. When a
              request matches the path pattern for that cache behavior, CloudFront routes the request
              to the specified origin. For more information, see `Cache Behavior Settings
              <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior>`__
              in the *Amazon CloudFront Developer Guide* .

            - **DomainName** *(string) --* **[REQUIRED]**

               **Amazon S3 origins** : The DNS name of the Amazon S3 bucket from which you want
               CloudFront to get objects for this origin, for example,
               ``myawsbucket.s3.amazonaws.com`` . If you set up your bucket to be configured as a
               website endpoint, enter the Amazon S3 static website hosting endpoint for the bucket.

              For more information about specifying this value for different types of origins, see
              `Origin Domain Name
              <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesDomainName>`__
              in the *Amazon CloudFront Developer Guide* .

              Constraints for Amazon S3 origins:

              * If you configured Amazon S3 Transfer Acceleration for your bucket, don't specify the
              ``s3-accelerate`` endpoint for ``DomainName`` .

              * The bucket name must be between 3 and 63 characters long (inclusive).

              * The bucket name must contain only lowercase characters, numbers, periods,
              underscores, and dashes.

              * The bucket name must not contain adjacent periods.

               **Custom Origins** : The DNS domain name for the HTTP server from which you want
               CloudFront to get objects for this origin, for example, ``www.example.com`` .

              Constraints for custom origins:

              * ``DomainName`` must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.),
              hyphen (-), or underscore (_) characters.

              * The name cannot exceed 128 characters.

            - **OriginPath** *(string) --*

              An optional element that causes CloudFront to request your content from a directory in
              your Amazon S3 bucket or your custom origin. When you include the ``OriginPath``
              element, specify the directory name, beginning with a ``/`` . CloudFront appends the
              directory name to the value of ``DomainName`` , for example, ``example.com/production``
              . Do not include a ``/`` at the end of the directory name.

              For example, suppose you've specified the following values for your distribution:

              * ``DomainName`` : An Amazon S3 bucket named ``myawsbucket`` .

              * ``OriginPath`` : ``/production``

              * ``CNAME`` : ``example.com``

              When a user enters ``example.com/index.html`` in a browser, CloudFront sends a request
              to Amazon S3 for ``myawsbucket/production/index.html`` .

              When a user enters ``example.com/acme/index.html`` in a browser, CloudFront sends a
              request to Amazon S3 for ``myawsbucket/production/acme/index.html`` .

            - **CustomHeaders** *(dict) --*

              A complex type that contains names and values for the custom headers that you want.

              - **Quantity** *(integer) --* **[REQUIRED]**

                The number of custom headers, if any, for this distribution.

              - **Items** *(list) --*

                 **Optional** : A list that contains one ``OriginCustomHeader`` element for each
                 custom header that you want CloudFront to forward to the origin. If Quantity is
                 ``0`` , omit ``Items`` .

                - *(dict) --*

                  A complex type that contains ``HeaderName`` and ``HeaderValue`` elements, if any,
                  for this distribution.

                  - **HeaderName** *(string) --* **[REQUIRED]**

                    The name of a header that you want CloudFront to forward to your origin. For more
                    information, see `Forwarding Custom Headers to Your Origin (Web Distributions
                    Only)
                    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html>`__
                    in the *Amazon CloudFront Developer Guide* .

                  - **HeaderValue** *(string) --* **[REQUIRED]**

                    The value for the header that you specified in the ``HeaderName`` field.

            - **S3OriginConfig** *(dict) --*

              A complex type that contains information about the Amazon S3 origin. If the origin is a
              custom origin, use the ``CustomOriginConfig`` element instead.

              - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

                The CloudFront origin access identity to associate with the origin. Use an origin
                access identity to configure the origin so that viewers can *only* access objects in
                an Amazon S3 bucket through CloudFront. The format of the value is:

                origin-access-identity/cloudfront/*ID-of-origin-access-identity*

                where `` *ID-of-origin-access-identity* `` is the value that CloudFront returned in
                the ``ID`` element when you created the origin access identity.

                If you want viewers to be able to access objects using either the CloudFront URL or
                the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

                To delete the origin access identity from an existing distribution, update the
                distribution configuration and include an empty ``OriginAccessIdentity`` element.

                To replace the origin access identity, update the distribution configuration and
                specify the new origin access identity.

                For more information about the origin access identity, see `Serving Private Content
                through CloudFront
                <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
                in the *Amazon CloudFront Developer Guide* .

            - **CustomOriginConfig** *(dict) --*

              A complex type that contains information about a custom origin. If the origin is an
              Amazon S3 bucket, use the ``S3OriginConfig`` element instead.

              - **HTTPPort** *(integer) --* **[REQUIRED]**

                The HTTP port the custom origin listens on.

              - **HTTPSPort** *(integer) --* **[REQUIRED]**

                The HTTPS port the custom origin listens on.

              - **OriginProtocolPolicy** *(string) --* **[REQUIRED]**

                The origin protocol policy to apply to your origin.

              - **OriginSslProtocols** *(dict) --*

                The SSL/TLS protocols that you want CloudFront to use when communicating with your
                origin over HTTPS.

                - **Quantity** *(integer) --* **[REQUIRED]**

                  The number of SSL/TLS protocols that you want to allow CloudFront to use when
                  establishing an HTTPS connection with this origin.

                - **Items** *(list) --* **[REQUIRED]**

                  A list that contains allowed SSL/TLS protocols for this distribution.

                  - *(string) --*

              - **OriginReadTimeout** *(integer) --*

                You can create a custom origin read timeout. All timeout units are in seconds. The
                default origin read timeout is 30 seconds, but you can configure custom timeout
                lengths using the CloudFront API. The minimum timeout length is 4 seconds; the
                maximum is 60 seconds.

                If you need to increase the maximum time limit, contact the `AWS Support Center
                <https://console.aws.amazon.com/support/home#/>`__ .

              - **OriginKeepaliveTimeout** *(integer) --*

                You can create a custom keep-alive timeout. All timeout units are in seconds. The
                default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths
                using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60
                seconds.

                If you need to increase the maximum time limit, contact the `AWS Support Center
                <https://console.aws.amazon.com/support/home#/>`__ .

      - **OriginGroups** *(dict) --*

        A complex type that contains information about origin groups for this distribution.

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of origin groups.

        - **Items** *(list) --*

          The items (origin groups) in a distribution.

          - *(dict) --*

            An origin group includes two origins (a primary origin and a second origin to failover
            to) and a failover criteria that you specify. You create an origin group to support
            origin failover in CloudFront. When you create or update a distribution, you can specifiy
            the origin group instead of a single origin, and CloudFront will failover from the
            primary origin to the second origin under the failover conditions that you've chosen.

            - **Id** *(string) --* **[REQUIRED]**

              The origin group's ID.

            - **FailoverCriteria** *(dict) --* **[REQUIRED]**

              A complex type that contains information about the failover criteria for an origin
              group.

              - **StatusCodes** *(dict) --* **[REQUIRED]**

                The status codes that, when returned from the primary origin, will trigger CloudFront
                to failover to the second origin.

                - **Quantity** *(integer) --* **[REQUIRED]**

                  The number of status codes.

                - **Items** *(list) --* **[REQUIRED]**

                  The items (status codes) for an origin group.

                  - *(integer) --*

            - **Members** *(dict) --* **[REQUIRED]**

              A complex type that contains information about the origins in an origin group.

              - **Quantity** *(integer) --* **[REQUIRED]**

                The number of origins in an origin group.

              - **Items** *(list) --* **[REQUIRED]**

                Items (origins) in an origin group.

                - *(dict) --*

                  An origin in an origin group.

                  - **OriginId** *(string) --* **[REQUIRED]**

                    The ID for an origin in an origin group.

      - **DefaultCacheBehavior** *(dict) --* **[REQUIRED]**

        A complex type that describes the default cache behavior if you don't specify a
        ``CacheBehavior`` element or if files don't match any of the values of ``PathPattern`` in
        ``CacheBehavior`` elements. You must create exactly one default cache behavior.

        - **TargetOriginId** *(string) --* **[REQUIRED]**

          The value of ``ID`` for the origin that you want CloudFront to route requests to when a
          request matches the path pattern either for a cache behavior or for the default cache
          behavior in your distribution.

        - **ForwardedValues** *(dict) --* **[REQUIRED]**

          A complex type that specifies how CloudFront handles query strings and cookies.

          - **QueryString** *(boolean) --* **[REQUIRED]**

            Indicates whether you want CloudFront to forward query strings to the origin that is
            associated with this cache behavior and cache based on the query string parameters.
            CloudFront behavior depends on the value of ``QueryString`` and on the values that you
            specify for ``QueryStringCacheKeys`` , if any:

            If you specify true for ``QueryString`` and you don't specify any values for
            ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin
            and caches based on all query string parameters. Depending on how many query string
            parameters and values you have, this can adversely affect performance because CloudFront
            must forward more requests to the origin.

            If you specify true for ``QueryString`` and you specify one or more values for
            ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin,
            but it only caches based on the query string parameters that you specify.

            If you specify false for ``QueryString`` , CloudFront doesn't forward any query string
            parameters to the origin, and doesn't cache based on query string parameters.

            For more information, see `Configuring CloudFront to Cache Based on Query String
            Parameters
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html>`__
            in the *Amazon CloudFront Developer Guide* .

          - **Cookies** *(dict) --* **[REQUIRED]**

            A complex type that specifies whether you want CloudFront to forward cookies to the
            origin and, if so, which ones. For more information about forwarding cookies to the
            origin, see `How CloudFront Forwards, Caches, and Logs Cookies
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html>`__ in
            the *Amazon CloudFront Developer Guide* .

            - **Forward** *(string) --* **[REQUIRED]**

              Specifies which cookies to forward to the origin for this cache behavior: all, none, or
              the list of cookies specified in the ``WhitelistedNames`` complex type.

              Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an
              Amazon S3 origin, specify none for the ``Forward`` element.

            - **WhitelistedNames** *(dict) --*

              Required if you specify ``whitelist`` for the value of ``Forward:`` . A complex type
              that specifies how many different cookies you want CloudFront to forward to the origin
              for this cache behavior and, if you want to forward selected cookies, the names of
              those cookies.

              If you specify ``all`` or none for the value of ``Forward`` , omit ``WhitelistedNames``
              . If you change the value of ``Forward`` from ``whitelist`` to all or none and you
              don't delete the ``WhitelistedNames`` element and its child elements, CloudFront
              deletes them automatically.

              For the current limit on the number of cookie names that you can whitelist for each
              cache behavior, see `CloudFront Limits
              <https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront>`__
              in the *AWS General Reference* .

              - **Quantity** *(integer) --* **[REQUIRED]**

                The number of different cookies that you want CloudFront to forward to the origin for
                this cache behavior.

              - **Items** *(list) --*

                A complex type that contains one ``Name`` element for each cookie that you want
                CloudFront to forward to the origin for this cache behavior.

                - *(string) --*

          - **Headers** *(dict) --*

            A complex type that specifies the ``Headers`` , if any, that you want CloudFront to
            forward to the origin for this cache behavior (whitelisted headers). For the headers that
            you specify, CloudFront also caches separate versions of a specified object that is based
            on the header values in viewer requests.

            For more information, see `Caching Content Based on Request Headers
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html>`__
            in the *Amazon CloudFront Developer Guide* .

            - **Quantity** *(integer) --* **[REQUIRED]**

              The number of different headers that you want CloudFront to base caching on for this
              cache behavior. You can configure each cache behavior in a web distribution to do one
              of the following:

              * **Forward all headers to your origin** : Specify ``1`` for ``Quantity`` and ``*`` for
              ``Name`` .

              .. warning::

                 CloudFront doesn't cache the objects that are associated with this cache behavior.
                 Instead, CloudFront sends every request to the origin.

              * **Forward a whitelist of headers you specify** : Specify the number of headers that
              you want CloudFront to base caching on. Then specify the header names in ``Name``
              elements. CloudFront caches your objects based on the values in the specified headers.

              * **Forward only the default headers** : Specify ``0`` for ``Quantity`` and omit
              ``Items`` . In this configuration, CloudFront doesn't cache based on the values in the
              request headers.

              Regardless of which option you choose, CloudFront forwards headers to your origin based
              on whether the origin is an S3 bucket or a custom origin. See the following
              documentation:

              * **S3 bucket** : See `HTTP Request Headers That CloudFront Removes or Updates
              <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorS3Origin.html#request-s3-removed-headers>`__
    """


_RequiredClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef = TypedDict(
    "_RequiredClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef",
    {"Format": str, "ContentType": str},
)
_OptionalClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef = TypedDict(
    "_OptionalClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef",
    {"ProfileId": str},
    total=False,
)


class ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef(
    _RequiredClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef,
    _OptionalClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef,
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles` `Items`

    A field-level encryption content type profile.

    - **Format** *(string) --* **[REQUIRED]**

      The format for a field-level encryption content type-profile mapping.

    - **ProfileId** *(string) --*

      The profile ID for a field-level encryption content type-profile mapping.

    - **ContentType** *(string) --* **[REQUIRED]**

      The content type for a field-level encryption content type-profile mapping.
    """


_RequiredClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef = TypedDict(
    "_RequiredClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef",
    {"Quantity": int},
)
_OptionalClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef = TypedDict(
    "_OptionalClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef",
    {
        "Items": List[
            ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef
        ]
    },
    total=False,
)


class ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef(
    _RequiredClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef,
    _OptionalClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef,
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfig` `ContentTypeProfiles`

    The configuration for a field-level encryption content type-profile.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of field-level encryption content type-profile mappings.

    - **Items** *(list) --*

      Items in a field-level encryption content type-profile mapping.

      - *(dict) --*

        A field-level encryption content type profile.

        - **Format** *(string) --* **[REQUIRED]**

          The format for a field-level encryption content type-profile mapping.

        - **ProfileId** *(string) --*

          The profile ID for a field-level encryption content type-profile mapping.

        - **ContentType** *(string) --* **[REQUIRED]**

          The content type for a field-level encryption content type-profile mapping.
    """


_RequiredClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef = TypedDict(
    "_RequiredClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef",
    {"ForwardWhenContentTypeIsUnknown": bool},
)
_OptionalClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef = TypedDict(
    "_OptionalClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef",
    {
        "ContentTypeProfiles": ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef
    },
    total=False,
)


class ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef(
    _RequiredClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef,
    _OptionalClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef,
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfig` `ContentTypeProfileConfig`

    A complex data type that specifies when to forward content if a content type isn't recognized
    and profiles to use as by default in a request if a query argument doesn't specify a profile to
    use.

    - **ForwardWhenContentTypeIsUnknown** *(boolean) --* **[REQUIRED]**

      The setting in a field-level encryption content type-profile mapping that specifies what to
      do when an unknown content type is provided for the profile. If true, content is forwarded
      without being encrypted when the content type is unknown. If false (the default), an error is
      returned when the content type is unknown.

    - **ContentTypeProfiles** *(dict) --*

      The configuration for a field-level encryption content type-profile.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of field-level encryption content type-profile mappings.

      - **Items** *(list) --*

        Items in a field-level encryption content type-profile mapping.

        - *(dict) --*

          A field-level encryption content type profile.

          - **Format** *(string) --* **[REQUIRED]**

            The format for a field-level encryption content type-profile mapping.

          - **ProfileId** *(string) --*

            The profile ID for a field-level encryption content type-profile mapping.

          - **ContentType** *(string) --* **[REQUIRED]**

            The content type for a field-level encryption content type-profile mapping.
    """


_ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef = TypedDict(
    "_ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef",
    {"QueryArg": str, "ProfileId": str},
)


class ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef(
    _ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles` `Items`

    Query argument-profile mapping for field-level encryption.

    - **QueryArg** *(string) --* **[REQUIRED]**

      Query argument for field-level encryption query argument-profile mapping.

    - **ProfileId** *(string) --* **[REQUIRED]**

      ID of profile to use for field-level encryption query argument-profile mapping
    """


_RequiredClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef = TypedDict(
    "_RequiredClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef",
    {"Quantity": int},
)
_OptionalClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef = TypedDict(
    "_OptionalClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef",
    {
        "Items": List[
            ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef
        ]
    },
    total=False,
)


class ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef(
    _RequiredClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef,
    _OptionalClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef,
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfig` `QueryArgProfiles`

    Profiles specified for query argument-profile mapping for field-level encryption.

    - **Quantity** *(integer) --* **[REQUIRED]**

      Number of profiles for query argument-profile mapping for field-level encryption.

    - **Items** *(list) --*

      Number of items for query argument-profile mapping for field-level encryption.

      - *(dict) --*

        Query argument-profile mapping for field-level encryption.

        - **QueryArg** *(string) --* **[REQUIRED]**

          Query argument for field-level encryption query argument-profile mapping.

        - **ProfileId** *(string) --* **[REQUIRED]**

          ID of profile to use for field-level encryption query argument-profile mapping
    """


_RequiredClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef = TypedDict(
    "_RequiredClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef",
    {"ForwardWhenQueryArgProfileIsUnknown": bool},
)
_OptionalClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef = TypedDict(
    "_OptionalClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef",
    {
        "QueryArgProfiles": ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef
    },
    total=False,
)


class ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef(
    _RequiredClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef,
    _OptionalClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef,
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfig` `QueryArgProfileConfig`

    A complex data type that specifies when to forward content if a profile isn't found and the
    profile that can be provided as a query argument in a request.

    - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --* **[REQUIRED]**

      Flag to set if you want a request to be forwarded to the origin even if the profile specified
      by the field-level encryption query argument, fle-profile, is unknown.

    - **QueryArgProfiles** *(dict) --*

      Profiles specified for query argument-profile mapping for field-level encryption.

      - **Quantity** *(integer) --* **[REQUIRED]**

        Number of profiles for query argument-profile mapping for field-level encryption.

      - **Items** *(list) --*

        Number of items for query argument-profile mapping for field-level encryption.

        - *(dict) --*

          Query argument-profile mapping for field-level encryption.

          - **QueryArg** *(string) --* **[REQUIRED]**

            Query argument for field-level encryption query argument-profile mapping.

          - **ProfileId** *(string) --* **[REQUIRED]**

            ID of profile to use for field-level encryption query argument-profile mapping
    """


_RequiredClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigTypeDef = TypedDict(
    "_RequiredClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigTypeDef",
    {"CallerReference": str},
)
_OptionalClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigTypeDef = TypedDict(
    "_OptionalClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigTypeDef",
    {
        "Comment": str,
        "QueryArgProfileConfig": ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef,
        "ContentTypeProfileConfig": ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef,
    },
    total=False,
)


class ClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigTypeDef(
    _RequiredClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigTypeDef,
    _OptionalClientCreateFieldLevelEncryptionConfigFieldLevelEncryptionConfigTypeDef,
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionConfig` `FieldLevelEncryptionConfig`

    The request to create a new field-level encryption configuration.

    - **CallerReference** *(string) --* **[REQUIRED]**

      A unique number that ensures the request can't be replayed.

    - **Comment** *(string) --*

      An optional comment about the configuration.

    - **QueryArgProfileConfig** *(dict) --*

      A complex data type that specifies when to forward content if a profile isn't found and the
      profile that can be provided as a query argument in a request.

      - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --* **[REQUIRED]**

        Flag to set if you want a request to be forwarded to the origin even if the profile specified
        by the field-level encryption query argument, fle-profile, is unknown.

      - **QueryArgProfiles** *(dict) --*

        Profiles specified for query argument-profile mapping for field-level encryption.

        - **Quantity** *(integer) --* **[REQUIRED]**

          Number of profiles for query argument-profile mapping for field-level encryption.

        - **Items** *(list) --*

          Number of items for query argument-profile mapping for field-level encryption.

          - *(dict) --*

            Query argument-profile mapping for field-level encryption.

            - **QueryArg** *(string) --* **[REQUIRED]**

              Query argument for field-level encryption query argument-profile mapping.

            - **ProfileId** *(string) --* **[REQUIRED]**

              ID of profile to use for field-level encryption query argument-profile mapping

    - **ContentTypeProfileConfig** *(dict) --*

      A complex data type that specifies when to forward content if a content type isn't recognized
      and profiles to use as by default in a request if a query argument doesn't specify a profile to
      use.

      - **ForwardWhenContentTypeIsUnknown** *(boolean) --* **[REQUIRED]**

        The setting in a field-level encryption content type-profile mapping that specifies what to
        do when an unknown content type is provided for the profile. If true, content is forwarded
        without being encrypted when the content type is unknown. If false (the default), an error is
        returned when the content type is unknown.

      - **ContentTypeProfiles** *(dict) --*

        The configuration for a field-level encryption content type-profile.

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of field-level encryption content type-profile mappings.

        - **Items** *(list) --*

          Items in a field-level encryption content type-profile mapping.

          - *(dict) --*

            A field-level encryption content type profile.

            - **Format** *(string) --* **[REQUIRED]**

              The format for a field-level encryption content type-profile mapping.

            - **ProfileId** *(string) --*

              The profile ID for a field-level encryption content type-profile mapping.

            - **ContentType** *(string) --* **[REQUIRED]**

              The content type for a field-level encryption content type-profile mapping.
    """


_ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef = TypedDict(
    "_ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef",
    {"Format": str, "ProfileId": str, "ContentType": str},
    total=False,
)


class ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef(
    _ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles` `Items`

    A field-level encryption content type profile.

    - **Format** *(string) --*

      The format for a field-level encryption content type-profile mapping.

    - **ProfileId** *(string) --*

      The profile ID for a field-level encryption content type-profile mapping.

    - **ContentType** *(string) --*

      The content type for a field-level encryption content type-profile mapping.
    """


_ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef = TypedDict(
    "_ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef
        ],
    },
    total=False,
)


class ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef(
    _ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfig` `ContentTypeProfiles`

    The configuration for a field-level encryption content type-profile.

    - **Quantity** *(integer) --*

      The number of field-level encryption content type-profile mappings.

    - **Items** *(list) --*

      Items in a field-level encryption content type-profile mapping.

      - *(dict) --*

        A field-level encryption content type profile.

        - **Format** *(string) --*

          The format for a field-level encryption content type-profile mapping.

        - **ProfileId** *(string) --*

          The profile ID for a field-level encryption content type-profile mapping.

        - **ContentType** *(string) --*

          The content type for a field-level encryption content type-profile mapping.
    """


_ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef = TypedDict(
    "_ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef",
    {
        "ForwardWhenContentTypeIsUnknown": bool,
        "ContentTypeProfiles": ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef,
    },
    total=False,
)


class ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef(
    _ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfig` `ContentTypeProfileConfig`

    A complex data type that specifies when to forward content if a content type isn't
    recognized and profiles to use as by default in a request if a query argument doesn't
    specify a profile to use.

    - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

      The setting in a field-level encryption content type-profile mapping that specifies
      what to do when an unknown content type is provided for the profile. If true, content
      is forwarded without being encrypted when the content type is unknown. If false (the
      default), an error is returned when the content type is unknown.

    - **ContentTypeProfiles** *(dict) --*

      The configuration for a field-level encryption content type-profile.

      - **Quantity** *(integer) --*

        The number of field-level encryption content type-profile mappings.

      - **Items** *(list) --*

        Items in a field-level encryption content type-profile mapping.

        - *(dict) --*

          A field-level encryption content type profile.

          - **Format** *(string) --*

            The format for a field-level encryption content type-profile mapping.

          - **ProfileId** *(string) --*

            The profile ID for a field-level encryption content type-profile mapping.

          - **ContentType** *(string) --*

            The content type for a field-level encryption content type-profile mapping.
    """


_ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef = TypedDict(
    "_ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef",
    {"QueryArg": str, "ProfileId": str},
    total=False,
)


class ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef(
    _ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles` `Items`

    Query argument-profile mapping for field-level encryption.

    - **QueryArg** *(string) --*

      Query argument for field-level encryption query argument-profile mapping.

    - **ProfileId** *(string) --*

      ID of profile to use for field-level encryption query argument-profile mapping
    """


_ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef = TypedDict(
    "_ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef
        ],
    },
    total=False,
)


class ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef(
    _ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfig` `QueryArgProfiles`

    Profiles specified for query argument-profile mapping for field-level encryption.

    - **Quantity** *(integer) --*

      Number of profiles for query argument-profile mapping for field-level encryption.

    - **Items** *(list) --*

      Number of items for query argument-profile mapping for field-level encryption.

      - *(dict) --*

        Query argument-profile mapping for field-level encryption.

        - **QueryArg** *(string) --*

          Query argument for field-level encryption query argument-profile mapping.

        - **ProfileId** *(string) --*

          ID of profile to use for field-level encryption query argument-profile mapping
    """


_ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef = TypedDict(
    "_ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef",
    {
        "ForwardWhenQueryArgProfileIsUnknown": bool,
        "QueryArgProfiles": ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef,
    },
    total=False,
)


class ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef(
    _ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfig` `QueryArgProfileConfig`

    A complex data type that specifies when to forward content if a profile isn't found and
    the profile that can be provided as a query argument in a request.

    - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

      Flag to set if you want a request to be forwarded to the origin even if the profile
      specified by the field-level encryption query argument, fle-profile, is unknown.

    - **QueryArgProfiles** *(dict) --*

      Profiles specified for query argument-profile mapping for field-level encryption.

      - **Quantity** *(integer) --*

        Number of profiles for query argument-profile mapping for field-level encryption.

      - **Items** *(list) --*

        Number of items for query argument-profile mapping for field-level encryption.

        - *(dict) --*

          Query argument-profile mapping for field-level encryption.

          - **QueryArg** *(string) --*

            Query argument for field-level encryption query argument-profile mapping.

          - **ProfileId** *(string) --*

            ID of profile to use for field-level encryption query argument-profile mapping
    """


_ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigTypeDef = TypedDict(
    "_ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigTypeDef",
    {
        "CallerReference": str,
        "Comment": str,
        "QueryArgProfileConfig": ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef,
        "ContentTypeProfileConfig": ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef,
    },
    total=False,
)


class ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigTypeDef(
    _ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigTypeDef
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryption` `FieldLevelEncryptionConfig`

    A complex data type that includes the profile configurations specified for field-level
    encryption.

    - **CallerReference** *(string) --*

      A unique number that ensures the request can't be replayed.

    - **Comment** *(string) --*

      An optional comment about the configuration.

    - **QueryArgProfileConfig** *(dict) --*

      A complex data type that specifies when to forward content if a profile isn't found and
      the profile that can be provided as a query argument in a request.

      - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

        Flag to set if you want a request to be forwarded to the origin even if the profile
        specified by the field-level encryption query argument, fle-profile, is unknown.

      - **QueryArgProfiles** *(dict) --*

        Profiles specified for query argument-profile mapping for field-level encryption.

        - **Quantity** *(integer) --*

          Number of profiles for query argument-profile mapping for field-level encryption.

        - **Items** *(list) --*

          Number of items for query argument-profile mapping for field-level encryption.

          - *(dict) --*

            Query argument-profile mapping for field-level encryption.

            - **QueryArg** *(string) --*

              Query argument for field-level encryption query argument-profile mapping.

            - **ProfileId** *(string) --*

              ID of profile to use for field-level encryption query argument-profile mapping

    - **ContentTypeProfileConfig** *(dict) --*

      A complex data type that specifies when to forward content if a content type isn't
      recognized and profiles to use as by default in a request if a query argument doesn't
      specify a profile to use.

      - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

        The setting in a field-level encryption content type-profile mapping that specifies
        what to do when an unknown content type is provided for the profile. If true, content
        is forwarded without being encrypted when the content type is unknown. If false (the
        default), an error is returned when the content type is unknown.

      - **ContentTypeProfiles** *(dict) --*

        The configuration for a field-level encryption content type-profile.

        - **Quantity** *(integer) --*

          The number of field-level encryption content type-profile mappings.

        - **Items** *(list) --*

          Items in a field-level encryption content type-profile mapping.

          - *(dict) --*

            A field-level encryption content type profile.

            - **Format** *(string) --*

              The format for a field-level encryption content type-profile mapping.

            - **ProfileId** *(string) --*

              The profile ID for a field-level encryption content type-profile mapping.

            - **ContentType** *(string) --*

              The content type for a field-level encryption content type-profile mapping.
    """


_ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionTypeDef = TypedDict(
    "_ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "FieldLevelEncryptionConfig": ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionTypeDef(
    _ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionTypeDef
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionConfigResponse` `FieldLevelEncryption`

    Returned when you create a new field-level encryption configuration.

    - **Id** *(string) --*

      The configuration ID for a field-level encryption configuration which includes a set of
      profiles that specify certain selected data fields to be encrypted by specific public keys.

    - **LastModifiedTime** *(datetime) --*

      The last time the field-level encryption configuration was changed.

    - **FieldLevelEncryptionConfig** *(dict) --*

      A complex data type that includes the profile configurations specified for field-level
      encryption.

      - **CallerReference** *(string) --*

        A unique number that ensures the request can't be replayed.

      - **Comment** *(string) --*

        An optional comment about the configuration.

      - **QueryArgProfileConfig** *(dict) --*

        A complex data type that specifies when to forward content if a profile isn't found and
        the profile that can be provided as a query argument in a request.

        - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

          Flag to set if you want a request to be forwarded to the origin even if the profile
          specified by the field-level encryption query argument, fle-profile, is unknown.

        - **QueryArgProfiles** *(dict) --*

          Profiles specified for query argument-profile mapping for field-level encryption.

          - **Quantity** *(integer) --*

            Number of profiles for query argument-profile mapping for field-level encryption.

          - **Items** *(list) --*

            Number of items for query argument-profile mapping for field-level encryption.

            - *(dict) --*

              Query argument-profile mapping for field-level encryption.

              - **QueryArg** *(string) --*

                Query argument for field-level encryption query argument-profile mapping.

              - **ProfileId** *(string) --*

                ID of profile to use for field-level encryption query argument-profile mapping

      - **ContentTypeProfileConfig** *(dict) --*

        A complex data type that specifies when to forward content if a content type isn't
        recognized and profiles to use as by default in a request if a query argument doesn't
        specify a profile to use.

        - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

          The setting in a field-level encryption content type-profile mapping that specifies
          what to do when an unknown content type is provided for the profile. If true, content
          is forwarded without being encrypted when the content type is unknown. If false (the
          default), an error is returned when the content type is unknown.

        - **ContentTypeProfiles** *(dict) --*

          The configuration for a field-level encryption content type-profile.

          - **Quantity** *(integer) --*

            The number of field-level encryption content type-profile mappings.

          - **Items** *(list) --*

            Items in a field-level encryption content type-profile mapping.

            - *(dict) --*

              A field-level encryption content type profile.

              - **Format** *(string) --*

                The format for a field-level encryption content type-profile mapping.

              - **ProfileId** *(string) --*

                The profile ID for a field-level encryption content type-profile mapping.

              - **ContentType** *(string) --*

                The content type for a field-level encryption content type-profile mapping.
    """


_ClientCreateFieldLevelEncryptionConfigResponseTypeDef = TypedDict(
    "_ClientCreateFieldLevelEncryptionConfigResponseTypeDef",
    {
        "FieldLevelEncryption": ClientCreateFieldLevelEncryptionConfigResponseFieldLevelEncryptionTypeDef,
        "Location": str,
        "ETag": str,
    },
    total=False,
)


class ClientCreateFieldLevelEncryptionConfigResponseTypeDef(
    _ClientCreateFieldLevelEncryptionConfigResponseTypeDef
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionConfig` `Response`

    - **FieldLevelEncryption** *(dict) --*

      Returned when you create a new field-level encryption configuration.

      - **Id** *(string) --*

        The configuration ID for a field-level encryption configuration which includes a set of
        profiles that specify certain selected data fields to be encrypted by specific public keys.

      - **LastModifiedTime** *(datetime) --*

        The last time the field-level encryption configuration was changed.

      - **FieldLevelEncryptionConfig** *(dict) --*

        A complex data type that includes the profile configurations specified for field-level
        encryption.

        - **CallerReference** *(string) --*

          A unique number that ensures the request can't be replayed.

        - **Comment** *(string) --*

          An optional comment about the configuration.

        - **QueryArgProfileConfig** *(dict) --*

          A complex data type that specifies when to forward content if a profile isn't found and
          the profile that can be provided as a query argument in a request.

          - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

            Flag to set if you want a request to be forwarded to the origin even if the profile
            specified by the field-level encryption query argument, fle-profile, is unknown.

          - **QueryArgProfiles** *(dict) --*

            Profiles specified for query argument-profile mapping for field-level encryption.

            - **Quantity** *(integer) --*

              Number of profiles for query argument-profile mapping for field-level encryption.

            - **Items** *(list) --*

              Number of items for query argument-profile mapping for field-level encryption.

              - *(dict) --*

                Query argument-profile mapping for field-level encryption.

                - **QueryArg** *(string) --*

                  Query argument for field-level encryption query argument-profile mapping.

                - **ProfileId** *(string) --*

                  ID of profile to use for field-level encryption query argument-profile mapping

        - **ContentTypeProfileConfig** *(dict) --*

          A complex data type that specifies when to forward content if a content type isn't
          recognized and profiles to use as by default in a request if a query argument doesn't
          specify a profile to use.

          - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

            The setting in a field-level encryption content type-profile mapping that specifies
            what to do when an unknown content type is provided for the profile. If true, content
            is forwarded without being encrypted when the content type is unknown. If false (the
            default), an error is returned when the content type is unknown.

          - **ContentTypeProfiles** *(dict) --*

            The configuration for a field-level encryption content type-profile.

            - **Quantity** *(integer) --*

              The number of field-level encryption content type-profile mappings.

            - **Items** *(list) --*

              Items in a field-level encryption content type-profile mapping.

              - *(dict) --*

                A field-level encryption content type profile.

                - **Format** *(string) --*

                  The format for a field-level encryption content type-profile mapping.

                - **ProfileId** *(string) --*

                  The profile ID for a field-level encryption content type-profile mapping.

                - **ContentType** *(string) --*

                  The content type for a field-level encryption content type-profile mapping.

    - **Location** *(string) --*

      The fully qualified URI of the new configuration resource just created. For example:
      ``https://cloudfront.amazonaws.com/2010-11-01/field-level-encryption-config/EDFDVBD632BHDS5``
      .

    - **ETag** *(string) --*

      The current version of the field level encryption configuration. For example:
      ``E2QWRUHAPOMQZL`` .
    """


_RequiredClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef = TypedDict(
    "_RequiredClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef",
    {"Quantity": int},
)
_OptionalClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef = TypedDict(
    "_OptionalClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef",
    {"Items": List[str]},
    total=False,
)


class ClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef(
    _RequiredClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef,
    _OptionalClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef,
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItems` `FieldPatterns`

    Field patterns in a field-level encryption content type profile specify the fields that
    you want to be encrypted. You can provide the full field name, or any beginning
    characters followed by a wildcard (*). You can't overlap field patterns. For example, you
    can't have both ABC* and AB*. Note that field patterns are case-sensitive.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of field-level encryption field patterns.

    - **Items** *(list) --*

      An array of the field-level encryption field patterns.

      - *(string) --*
    """


_ClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef = TypedDict(
    "_ClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef",
    {
        "PublicKeyId": str,
        "ProviderId": str,
        "FieldPatterns": ClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef,
    },
)


class ClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef(
    _ClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntities` `Items`

    Complex data type for field-level encryption profiles that includes the encryption key and
    field pattern specifications.

    - **PublicKeyId** *(string) --* **[REQUIRED]**

      The public key associated with a set of field-level encryption patterns, to be used when
      encrypting the fields that match the patterns.

    - **ProviderId** *(string) --* **[REQUIRED]**

      The provider associated with the public key being used for encryption. This value must
      also be provided with the private key for applications to be able to decrypt data.

    - **FieldPatterns** *(dict) --* **[REQUIRED]**

      Field patterns in a field-level encryption content type profile specify the fields that
      you want to be encrypted. You can provide the full field name, or any beginning
      characters followed by a wildcard (*). You can't overlap field patterns. For example, you
      can't have both ABC* and AB*. Note that field patterns are case-sensitive.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of field-level encryption field patterns.

      - **Items** *(list) --*

        An array of the field-level encryption field patterns.

        - *(string) --*
    """


_RequiredClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef = TypedDict(
    "_RequiredClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef",
    {"Quantity": int},
)
_OptionalClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef = TypedDict(
    "_OptionalClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef",
    {
        "Items": List[
            ClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef
        ]
    },
    total=False,
)


class ClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef(
    _RequiredClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef,
    _OptionalClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef,
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfig` `EncryptionEntities`

    A complex data type of encryption entities for the field-level encryption profile that include
    the public key ID, provider, and field patterns for specifying which fields to encrypt with
    this key.

    - **Quantity** *(integer) --* **[REQUIRED]**

      Number of field pattern items in a field-level encryption content type-profile mapping.

    - **Items** *(list) --*

      An array of field patterns in a field-level encryption content type-profile mapping.

      - *(dict) --*

        Complex data type for field-level encryption profiles that includes the encryption key and
        field pattern specifications.

        - **PublicKeyId** *(string) --* **[REQUIRED]**

          The public key associated with a set of field-level encryption patterns, to be used when
          encrypting the fields that match the patterns.

        - **ProviderId** *(string) --* **[REQUIRED]**

          The provider associated with the public key being used for encryption. This value must
          also be provided with the private key for applications to be able to decrypt data.

        - **FieldPatterns** *(dict) --* **[REQUIRED]**

          Field patterns in a field-level encryption content type profile specify the fields that
          you want to be encrypted. You can provide the full field name, or any beginning
          characters followed by a wildcard (*). You can't overlap field patterns. For example, you
          can't have both ABC* and AB*. Note that field patterns are case-sensitive.

          - **Quantity** *(integer) --* **[REQUIRED]**

            The number of field-level encryption field patterns.

          - **Items** *(list) --*

            An array of the field-level encryption field patterns.

            - *(string) --*
    """


_RequiredClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef = TypedDict(
    "_RequiredClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef",
    {
        "Name": str,
        "CallerReference": str,
        "EncryptionEntities": ClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef,
    },
)
_OptionalClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef = TypedDict(
    "_OptionalClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef",
    {"Comment": str},
    total=False,
)


class ClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef(
    _RequiredClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef,
    _OptionalClientCreateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef,
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionProfile` `FieldLevelEncryptionProfileConfig`

    The request to create a field-level encryption profile.

    - **Name** *(string) --* **[REQUIRED]**

      Profile name for the field-level encryption profile.

    - **CallerReference** *(string) --* **[REQUIRED]**

      A unique number that ensures that the request can't be replayed.

    - **Comment** *(string) --*

      An optional comment for the field-level encryption profile.

    - **EncryptionEntities** *(dict) --* **[REQUIRED]**

      A complex data type of encryption entities for the field-level encryption profile that include
      the public key ID, provider, and field patterns for specifying which fields to encrypt with
      this key.

      - **Quantity** *(integer) --* **[REQUIRED]**

        Number of field pattern items in a field-level encryption content type-profile mapping.

      - **Items** *(list) --*

        An array of field patterns in a field-level encryption content type-profile mapping.

        - *(dict) --*

          Complex data type for field-level encryption profiles that includes the encryption key and
          field pattern specifications.

          - **PublicKeyId** *(string) --* **[REQUIRED]**

            The public key associated with a set of field-level encryption patterns, to be used when
            encrypting the fields that match the patterns.

          - **ProviderId** *(string) --* **[REQUIRED]**

            The provider associated with the public key being used for encryption. This value must
            also be provided with the private key for applications to be able to decrypt data.

          - **FieldPatterns** *(dict) --* **[REQUIRED]**

            Field patterns in a field-level encryption content type profile specify the fields that
            you want to be encrypted. You can provide the full field name, or any beginning
            characters followed by a wildcard (*). You can't overlap field patterns. For example, you
            can't have both ABC* and AB*. Note that field patterns are case-sensitive.

            - **Quantity** *(integer) --* **[REQUIRED]**

              The number of field-level encryption field patterns.

            - **Items** *(list) --*

              An array of the field-level encryption field patterns.

              - *(string) --*
    """


_ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef = TypedDict(
    "_ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef",
    {"Quantity": int, "Items": List[str]},
    total=False,
)


class ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef(
    _ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItems` `FieldPatterns`

    Field patterns in a field-level encryption content type profile specify the fields
    that you want to be encrypted. You can provide the full field name, or any
    beginning characters followed by a wildcard (*). You can't overlap field patterns.
    For example, you can't have both ABC* and AB*. Note that field patterns are
    case-sensitive.

    - **Quantity** *(integer) --*

      The number of field-level encryption field patterns.

    - **Items** *(list) --*

      An array of the field-level encryption field patterns.

      - *(string) --*
    """


_ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef = TypedDict(
    "_ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef",
    {
        "PublicKeyId": str,
        "ProviderId": str,
        "FieldPatterns": ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef,
    },
    total=False,
)


class ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef(
    _ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntities` `Items`

    Complex data type for field-level encryption profiles that includes the encryption
    key and field pattern specifications.

    - **PublicKeyId** *(string) --*

      The public key associated with a set of field-level encryption patterns, to be used
      when encrypting the fields that match the patterns.

    - **ProviderId** *(string) --*

      The provider associated with the public key being used for encryption. This value
      must also be provided with the private key for applications to be able to decrypt
      data.

    - **FieldPatterns** *(dict) --*

      Field patterns in a field-level encryption content type profile specify the fields
      that you want to be encrypted. You can provide the full field name, or any
      beginning characters followed by a wildcard (*). You can't overlap field patterns.
      For example, you can't have both ABC* and AB*. Note that field patterns are
      case-sensitive.

      - **Quantity** *(integer) --*

        The number of field-level encryption field patterns.

      - **Items** *(list) --*

        An array of the field-level encryption field patterns.

        - *(string) --*
    """


_ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef = TypedDict(
    "_ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef
        ],
    },
    total=False,
)


class ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef(
    _ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfig` `EncryptionEntities`

    A complex data type of encryption entities for the field-level encryption profile that
    include the public key ID, provider, and field patterns for specifying which fields to
    encrypt with this key.

    - **Quantity** *(integer) --*

      Number of field pattern items in a field-level encryption content type-profile mapping.

    - **Items** *(list) --*

      An array of field patterns in a field-level encryption content type-profile mapping.

      - *(dict) --*

        Complex data type for field-level encryption profiles that includes the encryption
        key and field pattern specifications.

        - **PublicKeyId** *(string) --*

          The public key associated with a set of field-level encryption patterns, to be used
          when encrypting the fields that match the patterns.

        - **ProviderId** *(string) --*

          The provider associated with the public key being used for encryption. This value
          must also be provided with the private key for applications to be able to decrypt
          data.

        - **FieldPatterns** *(dict) --*

          Field patterns in a field-level encryption content type profile specify the fields
          that you want to be encrypted. You can provide the full field name, or any
          beginning characters followed by a wildcard (*). You can't overlap field patterns.
          For example, you can't have both ABC* and AB*. Note that field patterns are
          case-sensitive.

          - **Quantity** *(integer) --*

            The number of field-level encryption field patterns.

          - **Items** *(list) --*

            An array of the field-level encryption field patterns.

            - *(string) --*
    """


_ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef = TypedDict(
    "_ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef",
    {
        "Name": str,
        "CallerReference": str,
        "Comment": str,
        "EncryptionEntities": ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef,
    },
    total=False,
)


class ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef(
    _ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfile` `FieldLevelEncryptionProfileConfig`

    A complex data type that includes the profile name and the encryption entities for the
    field-level encryption profile.

    - **Name** *(string) --*

      Profile name for the field-level encryption profile.

    - **CallerReference** *(string) --*

      A unique number that ensures that the request can't be replayed.

    - **Comment** *(string) --*

      An optional comment for the field-level encryption profile.

    - **EncryptionEntities** *(dict) --*

      A complex data type of encryption entities for the field-level encryption profile that
      include the public key ID, provider, and field patterns for specifying which fields to
      encrypt with this key.

      - **Quantity** *(integer) --*

        Number of field pattern items in a field-level encryption content type-profile mapping.

      - **Items** *(list) --*

        An array of field patterns in a field-level encryption content type-profile mapping.

        - *(dict) --*

          Complex data type for field-level encryption profiles that includes the encryption
          key and field pattern specifications.

          - **PublicKeyId** *(string) --*

            The public key associated with a set of field-level encryption patterns, to be used
            when encrypting the fields that match the patterns.

          - **ProviderId** *(string) --*

            The provider associated with the public key being used for encryption. This value
            must also be provided with the private key for applications to be able to decrypt
            data.

          - **FieldPatterns** *(dict) --*

            Field patterns in a field-level encryption content type profile specify the fields
            that you want to be encrypted. You can provide the full field name, or any
            beginning characters followed by a wildcard (*). You can't overlap field patterns.
            For example, you can't have both ABC* and AB*. Note that field patterns are
            case-sensitive.

            - **Quantity** *(integer) --*

              The number of field-level encryption field patterns.

            - **Items** *(list) --*

              An array of the field-level encryption field patterns.

              - *(string) --*
    """


_ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileTypeDef = TypedDict(
    "_ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "FieldLevelEncryptionProfileConfig": ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef,
    },
    total=False,
)


class ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileTypeDef(
    _ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileTypeDef
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionProfileResponse` `FieldLevelEncryptionProfile`

    Returned when you create a new field-level encryption profile.

    - **Id** *(string) --*

      The ID for a field-level encryption profile configuration which includes a set of profiles
      that specify certain selected data fields to be encrypted by specific public keys.

    - **LastModifiedTime** *(datetime) --*

      The last time the field-level encryption profile was updated.

    - **FieldLevelEncryptionProfileConfig** *(dict) --*

      A complex data type that includes the profile name and the encryption entities for the
      field-level encryption profile.

      - **Name** *(string) --*

        Profile name for the field-level encryption profile.

      - **CallerReference** *(string) --*

        A unique number that ensures that the request can't be replayed.

      - **Comment** *(string) --*

        An optional comment for the field-level encryption profile.

      - **EncryptionEntities** *(dict) --*

        A complex data type of encryption entities for the field-level encryption profile that
        include the public key ID, provider, and field patterns for specifying which fields to
        encrypt with this key.

        - **Quantity** *(integer) --*

          Number of field pattern items in a field-level encryption content type-profile mapping.

        - **Items** *(list) --*

          An array of field patterns in a field-level encryption content type-profile mapping.

          - *(dict) --*

            Complex data type for field-level encryption profiles that includes the encryption
            key and field pattern specifications.

            - **PublicKeyId** *(string) --*

              The public key associated with a set of field-level encryption patterns, to be used
              when encrypting the fields that match the patterns.

            - **ProviderId** *(string) --*

              The provider associated with the public key being used for encryption. This value
              must also be provided with the private key for applications to be able to decrypt
              data.

            - **FieldPatterns** *(dict) --*

              Field patterns in a field-level encryption content type profile specify the fields
              that you want to be encrypted. You can provide the full field name, or any
              beginning characters followed by a wildcard (*). You can't overlap field patterns.
              For example, you can't have both ABC* and AB*. Note that field patterns are
              case-sensitive.

              - **Quantity** *(integer) --*

                The number of field-level encryption field patterns.

              - **Items** *(list) --*

                An array of the field-level encryption field patterns.

                - *(string) --*
    """


_ClientCreateFieldLevelEncryptionProfileResponseTypeDef = TypedDict(
    "_ClientCreateFieldLevelEncryptionProfileResponseTypeDef",
    {
        "FieldLevelEncryptionProfile": ClientCreateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileTypeDef,
        "Location": str,
        "ETag": str,
    },
    total=False,
)


class ClientCreateFieldLevelEncryptionProfileResponseTypeDef(
    _ClientCreateFieldLevelEncryptionProfileResponseTypeDef
):
    """
    Type definition for `ClientCreateFieldLevelEncryptionProfile` `Response`

    - **FieldLevelEncryptionProfile** *(dict) --*

      Returned when you create a new field-level encryption profile.

      - **Id** *(string) --*

        The ID for a field-level encryption profile configuration which includes a set of profiles
        that specify certain selected data fields to be encrypted by specific public keys.

      - **LastModifiedTime** *(datetime) --*

        The last time the field-level encryption profile was updated.

      - **FieldLevelEncryptionProfileConfig** *(dict) --*

        A complex data type that includes the profile name and the encryption entities for the
        field-level encryption profile.

        - **Name** *(string) --*

          Profile name for the field-level encryption profile.

        - **CallerReference** *(string) --*

          A unique number that ensures that the request can't be replayed.

        - **Comment** *(string) --*

          An optional comment for the field-level encryption profile.

        - **EncryptionEntities** *(dict) --*

          A complex data type of encryption entities for the field-level encryption profile that
          include the public key ID, provider, and field patterns for specifying which fields to
          encrypt with this key.

          - **Quantity** *(integer) --*

            Number of field pattern items in a field-level encryption content type-profile mapping.

          - **Items** *(list) --*

            An array of field patterns in a field-level encryption content type-profile mapping.

            - *(dict) --*

              Complex data type for field-level encryption profiles that includes the encryption
              key and field pattern specifications.

              - **PublicKeyId** *(string) --*

                The public key associated with a set of field-level encryption patterns, to be used
                when encrypting the fields that match the patterns.

              - **ProviderId** *(string) --*

                The provider associated with the public key being used for encryption. This value
                must also be provided with the private key for applications to be able to decrypt
                data.

              - **FieldPatterns** *(dict) --*

                Field patterns in a field-level encryption content type profile specify the fields
                that you want to be encrypted. You can provide the full field name, or any
                beginning characters followed by a wildcard (*). You can't overlap field patterns.
                For example, you can't have both ABC* and AB*. Note that field patterns are
                case-sensitive.

                - **Quantity** *(integer) --*

                  The number of field-level encryption field patterns.

                - **Items** *(list) --*

                  An array of the field-level encryption field patterns.

                  - *(string) --*

    - **Location** *(string) --*

      The fully qualified URI of the new profile resource just created. For example:
      ``https://cloudfront.amazonaws.com/2010-11-01/field-level-encryption-profile/EDFDVBD632BHDS5``
      .

    - **ETag** *(string) --*

      The current version of the field level encryption profile. For example: ``E2QWRUHAPOMQZL`` .
    """


_RequiredClientCreateInvalidationInvalidationBatchPathsTypeDef = TypedDict(
    "_RequiredClientCreateInvalidationInvalidationBatchPathsTypeDef", {"Quantity": int}
)
_OptionalClientCreateInvalidationInvalidationBatchPathsTypeDef = TypedDict(
    "_OptionalClientCreateInvalidationInvalidationBatchPathsTypeDef",
    {"Items": List[str]},
    total=False,
)


class ClientCreateInvalidationInvalidationBatchPathsTypeDef(
    _RequiredClientCreateInvalidationInvalidationBatchPathsTypeDef,
    _OptionalClientCreateInvalidationInvalidationBatchPathsTypeDef,
):
    """
    Type definition for `ClientCreateInvalidationInvalidationBatch` `Paths`

    A complex type that contains information about the objects that you want to invalidate. For
    more information, see `Specifying the Objects to Invalidate
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-specifying-objects>`__
    in the *Amazon CloudFront Developer Guide* .

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of invalidation paths specified for the objects that you want to invalidate.

    - **Items** *(list) --*

      A complex type that contains a list of the paths that you want to invalidate.

      - *(string) --*
    """


_ClientCreateInvalidationInvalidationBatchTypeDef = TypedDict(
    "_ClientCreateInvalidationInvalidationBatchTypeDef",
    {
        "Paths": ClientCreateInvalidationInvalidationBatchPathsTypeDef,
        "CallerReference": str,
    },
)


class ClientCreateInvalidationInvalidationBatchTypeDef(
    _ClientCreateInvalidationInvalidationBatchTypeDef
):
    """
    Type definition for `ClientCreateInvalidation` `InvalidationBatch`

    The batch information for the invalidation.

    - **Paths** *(dict) --* **[REQUIRED]**

      A complex type that contains information about the objects that you want to invalidate. For
      more information, see `Specifying the Objects to Invalidate
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-specifying-objects>`__
      in the *Amazon CloudFront Developer Guide* .

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of invalidation paths specified for the objects that you want to invalidate.

      - **Items** *(list) --*

        A complex type that contains a list of the paths that you want to invalidate.

        - *(string) --*

    - **CallerReference** *(string) --* **[REQUIRED]**

      A value that you specify to uniquely identify an invalidation request. CloudFront uses the
      value to prevent you from accidentally resubmitting an identical request. Whenever you create a
      new invalidation request, you must specify a new value for ``CallerReference`` and change other
      values in the request as applicable. One way to ensure that the value of ``CallerReference`` is
      unique is to use a ``timestamp`` , for example, ``20120301090000`` .

      If you make a second invalidation request with the same value for ``CallerReference`` , and if
      the rest of the request is the same, CloudFront doesn't create a new invalidation request.
      Instead, CloudFront returns information about the invalidation request that you previously
      created with the same ``CallerReference`` .

      If ``CallerReference`` is a value you already sent in a previous invalidation batch request but
      the content of any ``Path`` is different from the original request, CloudFront returns an
      ``InvalidationBatchAlreadyExists`` error.
    """


_ClientCreateInvalidationResponseInvalidationInvalidationBatchPathsTypeDef = TypedDict(
    "_ClientCreateInvalidationResponseInvalidationInvalidationBatchPathsTypeDef",
    {"Quantity": int, "Items": List[str]},
    total=False,
)


class ClientCreateInvalidationResponseInvalidationInvalidationBatchPathsTypeDef(
    _ClientCreateInvalidationResponseInvalidationInvalidationBatchPathsTypeDef
):
    """
    Type definition for `ClientCreateInvalidationResponseInvalidationInvalidationBatch` `Paths`

    A complex type that contains information about the objects that you want to invalidate.
    For more information, see `Specifying the Objects to Invalidate
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-specifying-objects>`__
    in the *Amazon CloudFront Developer Guide* .

    - **Quantity** *(integer) --*

      The number of invalidation paths specified for the objects that you want to invalidate.

    - **Items** *(list) --*

      A complex type that contains a list of the paths that you want to invalidate.

      - *(string) --*
    """


_ClientCreateInvalidationResponseInvalidationInvalidationBatchTypeDef = TypedDict(
    "_ClientCreateInvalidationResponseInvalidationInvalidationBatchTypeDef",
    {
        "Paths": ClientCreateInvalidationResponseInvalidationInvalidationBatchPathsTypeDef,
        "CallerReference": str,
    },
    total=False,
)


class ClientCreateInvalidationResponseInvalidationInvalidationBatchTypeDef(
    _ClientCreateInvalidationResponseInvalidationInvalidationBatchTypeDef
):
    """
    Type definition for `ClientCreateInvalidationResponseInvalidation` `InvalidationBatch`

    The current invalidation information for the batch request.

    - **Paths** *(dict) --*

      A complex type that contains information about the objects that you want to invalidate.
      For more information, see `Specifying the Objects to Invalidate
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-specifying-objects>`__
      in the *Amazon CloudFront Developer Guide* .

      - **Quantity** *(integer) --*

        The number of invalidation paths specified for the objects that you want to invalidate.

      - **Items** *(list) --*

        A complex type that contains a list of the paths that you want to invalidate.

        - *(string) --*

    - **CallerReference** *(string) --*

      A value that you specify to uniquely identify an invalidation request. CloudFront uses
      the value to prevent you from accidentally resubmitting an identical request. Whenever
      you create a new invalidation request, you must specify a new value for
      ``CallerReference`` and change other values in the request as applicable. One way to
      ensure that the value of ``CallerReference`` is unique is to use a ``timestamp`` , for
      example, ``20120301090000`` .

      If you make a second invalidation request with the same value for ``CallerReference`` ,
      and if the rest of the request is the same, CloudFront doesn't create a new invalidation
      request. Instead, CloudFront returns information about the invalidation request that you
      previously created with the same ``CallerReference`` .

      If ``CallerReference`` is a value you already sent in a previous invalidation batch
      request but the content of any ``Path`` is different from the original request,
      CloudFront returns an ``InvalidationBatchAlreadyExists`` error.
    """


_ClientCreateInvalidationResponseInvalidationTypeDef = TypedDict(
    "_ClientCreateInvalidationResponseInvalidationTypeDef",
    {
        "Id": str,
        "Status": str,
        "CreateTime": datetime,
        "InvalidationBatch": ClientCreateInvalidationResponseInvalidationInvalidationBatchTypeDef,
    },
    total=False,
)


class ClientCreateInvalidationResponseInvalidationTypeDef(
    _ClientCreateInvalidationResponseInvalidationTypeDef
):
    """
    Type definition for `ClientCreateInvalidationResponse` `Invalidation`

    The invalidation's information.

    - **Id** *(string) --*

      The identifier for the invalidation request. For example: ``IDFDVBD632BHDS5`` .

    - **Status** *(string) --*

      The status of the invalidation request. When the invalidation batch is finished, the status
      is ``Completed`` .

    - **CreateTime** *(datetime) --*

      The date and time the invalidation request was first made.

    - **InvalidationBatch** *(dict) --*

      The current invalidation information for the batch request.

      - **Paths** *(dict) --*

        A complex type that contains information about the objects that you want to invalidate.
        For more information, see `Specifying the Objects to Invalidate
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-specifying-objects>`__
        in the *Amazon CloudFront Developer Guide* .

        - **Quantity** *(integer) --*

          The number of invalidation paths specified for the objects that you want to invalidate.

        - **Items** *(list) --*

          A complex type that contains a list of the paths that you want to invalidate.

          - *(string) --*

      - **CallerReference** *(string) --*

        A value that you specify to uniquely identify an invalidation request. CloudFront uses
        the value to prevent you from accidentally resubmitting an identical request. Whenever
        you create a new invalidation request, you must specify a new value for
        ``CallerReference`` and change other values in the request as applicable. One way to
        ensure that the value of ``CallerReference`` is unique is to use a ``timestamp`` , for
        example, ``20120301090000`` .

        If you make a second invalidation request with the same value for ``CallerReference`` ,
        and if the rest of the request is the same, CloudFront doesn't create a new invalidation
        request. Instead, CloudFront returns information about the invalidation request that you
        previously created with the same ``CallerReference`` .

        If ``CallerReference`` is a value you already sent in a previous invalidation batch
        request but the content of any ``Path`` is different from the original request,
        CloudFront returns an ``InvalidationBatchAlreadyExists`` error.
    """


_ClientCreateInvalidationResponseTypeDef = TypedDict(
    "_ClientCreateInvalidationResponseTypeDef",
    {
        "Location": str,
        "Invalidation": ClientCreateInvalidationResponseInvalidationTypeDef,
    },
    total=False,
)


class ClientCreateInvalidationResponseTypeDef(_ClientCreateInvalidationResponseTypeDef):
    """
    Type definition for `ClientCreateInvalidation` `Response`

    The returned result of the corresponding request.

    - **Location** *(string) --*

      The fully qualified URI of the distribution and invalidation batch request, including the
      ``Invalidation ID`` .

    - **Invalidation** *(dict) --*

      The invalidation's information.

      - **Id** *(string) --*

        The identifier for the invalidation request. For example: ``IDFDVBD632BHDS5`` .

      - **Status** *(string) --*

        The status of the invalidation request. When the invalidation batch is finished, the status
        is ``Completed`` .

      - **CreateTime** *(datetime) --*

        The date and time the invalidation request was first made.

      - **InvalidationBatch** *(dict) --*

        The current invalidation information for the batch request.

        - **Paths** *(dict) --*

          A complex type that contains information about the objects that you want to invalidate.
          For more information, see `Specifying the Objects to Invalidate
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-specifying-objects>`__
          in the *Amazon CloudFront Developer Guide* .

          - **Quantity** *(integer) --*

            The number of invalidation paths specified for the objects that you want to invalidate.

          - **Items** *(list) --*

            A complex type that contains a list of the paths that you want to invalidate.

            - *(string) --*

        - **CallerReference** *(string) --*

          A value that you specify to uniquely identify an invalidation request. CloudFront uses
          the value to prevent you from accidentally resubmitting an identical request. Whenever
          you create a new invalidation request, you must specify a new value for
          ``CallerReference`` and change other values in the request as applicable. One way to
          ensure that the value of ``CallerReference`` is unique is to use a ``timestamp`` , for
          example, ``20120301090000`` .

          If you make a second invalidation request with the same value for ``CallerReference`` ,
          and if the rest of the request is the same, CloudFront doesn't create a new invalidation
          request. Instead, CloudFront returns information about the invalidation request that you
          previously created with the same ``CallerReference`` .

          If ``CallerReference`` is a value you already sent in a previous invalidation batch
          request but the content of any ``Path`` is different from the original request,
          CloudFront returns an ``InvalidationBatchAlreadyExists`` error.
    """


_RequiredClientCreatePublicKeyPublicKeyConfigTypeDef = TypedDict(
    "_RequiredClientCreatePublicKeyPublicKeyConfigTypeDef",
    {"CallerReference": str, "Name": str, "EncodedKey": str},
)
_OptionalClientCreatePublicKeyPublicKeyConfigTypeDef = TypedDict(
    "_OptionalClientCreatePublicKeyPublicKeyConfigTypeDef",
    {"Comment": str},
    total=False,
)


class ClientCreatePublicKeyPublicKeyConfigTypeDef(
    _RequiredClientCreatePublicKeyPublicKeyConfigTypeDef,
    _OptionalClientCreatePublicKeyPublicKeyConfigTypeDef,
):
    """
    Type definition for `ClientCreatePublicKey` `PublicKeyConfig`

    The request to add a public key to CloudFront.

    - **CallerReference** *(string) --* **[REQUIRED]**

      A unique number that ensures that the request can't be replayed.

    - **Name** *(string) --* **[REQUIRED]**

      The name for a public key you add to CloudFront to use with features like field-level
      encryption.

    - **EncodedKey** *(string) --* **[REQUIRED]**

      The encoded public key that you want to add to CloudFront to use with features like field-level
      encryption.

    - **Comment** *(string) --*

      An optional comment about a public key.
    """


_ClientCreatePublicKeyResponsePublicKeyPublicKeyConfigTypeDef = TypedDict(
    "_ClientCreatePublicKeyResponsePublicKeyPublicKeyConfigTypeDef",
    {"CallerReference": str, "Name": str, "EncodedKey": str, "Comment": str},
    total=False,
)


class ClientCreatePublicKeyResponsePublicKeyPublicKeyConfigTypeDef(
    _ClientCreatePublicKeyResponsePublicKeyPublicKeyConfigTypeDef
):
    """
    Type definition for `ClientCreatePublicKeyResponsePublicKey` `PublicKeyConfig`

    A complex data type for a public key you add to CloudFront to use with features like
    field-level encryption.

    - **CallerReference** *(string) --*

      A unique number that ensures that the request can't be replayed.

    - **Name** *(string) --*

      The name for a public key you add to CloudFront to use with features like field-level
      encryption.

    - **EncodedKey** *(string) --*

      The encoded public key that you want to add to CloudFront to use with features like
      field-level encryption.

    - **Comment** *(string) --*

      An optional comment about a public key.
    """


_ClientCreatePublicKeyResponsePublicKeyTypeDef = TypedDict(
    "_ClientCreatePublicKeyResponsePublicKeyTypeDef",
    {
        "Id": str,
        "CreatedTime": datetime,
        "PublicKeyConfig": ClientCreatePublicKeyResponsePublicKeyPublicKeyConfigTypeDef,
    },
    total=False,
)


class ClientCreatePublicKeyResponsePublicKeyTypeDef(
    _ClientCreatePublicKeyResponsePublicKeyTypeDef
):
    """
    Type definition for `ClientCreatePublicKeyResponse` `PublicKey`

    Returned when you add a public key.

    - **Id** *(string) --*

      A unique ID assigned to a public key you've added to CloudFront.

    - **CreatedTime** *(datetime) --*

      A time you added a public key to CloudFront.

    - **PublicKeyConfig** *(dict) --*

      A complex data type for a public key you add to CloudFront to use with features like
      field-level encryption.

      - **CallerReference** *(string) --*

        A unique number that ensures that the request can't be replayed.

      - **Name** *(string) --*

        The name for a public key you add to CloudFront to use with features like field-level
        encryption.

      - **EncodedKey** *(string) --*

        The encoded public key that you want to add to CloudFront to use with features like
        field-level encryption.

      - **Comment** *(string) --*

        An optional comment about a public key.
    """


_ClientCreatePublicKeyResponseTypeDef = TypedDict(
    "_ClientCreatePublicKeyResponseTypeDef",
    {
        "PublicKey": ClientCreatePublicKeyResponsePublicKeyTypeDef,
        "Location": str,
        "ETag": str,
    },
    total=False,
)


class ClientCreatePublicKeyResponseTypeDef(_ClientCreatePublicKeyResponseTypeDef):
    """
    Type definition for `ClientCreatePublicKey` `Response`

    - **PublicKey** *(dict) --*

      Returned when you add a public key.

      - **Id** *(string) --*

        A unique ID assigned to a public key you've added to CloudFront.

      - **CreatedTime** *(datetime) --*

        A time you added a public key to CloudFront.

      - **PublicKeyConfig** *(dict) --*

        A complex data type for a public key you add to CloudFront to use with features like
        field-level encryption.

        - **CallerReference** *(string) --*

          A unique number that ensures that the request can't be replayed.

        - **Name** *(string) --*

          The name for a public key you add to CloudFront to use with features like field-level
          encryption.

        - **EncodedKey** *(string) --*

          The encoded public key that you want to add to CloudFront to use with features like
          field-level encryption.

        - **Comment** *(string) --*

          An optional comment about a public key.

    - **Location** *(string) --*

      The fully qualified URI of the new public key resource just created. For example:
      ``https://cloudfront.amazonaws.com/2010-11-01/cloudfront-public-key/EDFDVBD632BHDS5`` .

    - **ETag** *(string) --*

      The current version of the public key. For example: ``E2QWRUHAPOMQZL`` .
    """


_ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef",
    {"Quantity": int, "Items": List[str]},
    total=False,
)


class ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef(
    _ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItems` `KeyPairIds`

    A complex type that lists the active CloudFront key pairs, if any, that are
    associated with ``AwsAccountNumber`` .

    - **Quantity** *(integer) --*

      The number of active CloudFront key pairs for ``AwsAccountNumber`` .

      For more information, see `ActiveTrustedSigners
      <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
      .

    - **Items** *(list) --*

      A complex type that lists the active CloudFront key pairs, if any, that are
      associated with ``AwsAccountNumber`` .

      For more information, see `ActiveTrustedSigners
      <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
      .

      - *(string) --*
    """


_ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsTypeDef",
    {
        "AwsAccountNumber": str,
        "KeyPairIds": ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef,
    },
    total=False,
)


class ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsTypeDef(
    _ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSigners` `Items`

    A complex type that lists the AWS accounts that were included in the ``TrustedSigners``
    complex type, as well as their active CloudFront key pair IDs, if any.

    - **AwsAccountNumber** *(string) --*

      An AWS account that is included in the ``TrustedSigners`` complex type for this
      distribution. Valid values include:

      * ``self`` , which is the AWS account used to create the distribution.

      * An AWS account number.

    - **KeyPairIds** *(dict) --*

      A complex type that lists the active CloudFront key pairs, if any, that are
      associated with ``AwsAccountNumber`` .

      - **Quantity** *(integer) --*

        The number of active CloudFront key pairs for ``AwsAccountNumber`` .

        For more information, see `ActiveTrustedSigners
        <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
        .

      - **Items** *(list) --*

        A complex type that lists the active CloudFront key pairs, if any, that are
        associated with ``AwsAccountNumber`` .

        For more information, see `ActiveTrustedSigners
        <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
        .

        - *(string) --*
    """


_ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
        "Items": List[
            ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsTypeDef
        ],
    },
    total=False,
)


class ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersTypeDef(
    _ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionResponseStreamingDistribution` `ActiveTrustedSigners`

    A complex type that lists the AWS accounts, if any, that you included in the
    ``TrustedSigners`` complex type for this distribution. These are the accounts that you want
    to allow to create signed URLs for private content.

    The ``Signer`` complex type lists the AWS account number of the trusted signer or ``self``
    if the signer is the AWS account that created the distribution. The ``Signer`` element also
    includes the IDs of any active CloudFront key pairs that are associated with the trusted
    signer's AWS account. If no ``KeyPairId`` element appears for a ``Signer`` , that signer
    can't create signed URLs.

    For more information, see `Serving Private Content through CloudFront
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
    in the *Amazon CloudFront Developer Guide* .

    - **Enabled** *(boolean) --*

      Enabled is ``true`` if any of the AWS accounts listed in the ``TrustedSigners`` complex
      type for this distribution have active CloudFront key pairs. If not, ``Enabled`` is
      ``false`` .

    - **Quantity** *(integer) --*

      The number of trusted signers specified in the ``TrustedSigners`` complex type.

    - **Items** *(list) --*

      A complex type that contains one ``Signer`` complex type for each trusted signer that is
      specified in the ``TrustedSigners`` complex type.

      - *(dict) --*

        A complex type that lists the AWS accounts that were included in the ``TrustedSigners``
        complex type, as well as their active CloudFront key pair IDs, if any.

        - **AwsAccountNumber** *(string) --*

          An AWS account that is included in the ``TrustedSigners`` complex type for this
          distribution. Valid values include:

          * ``self`` , which is the AWS account used to create the distribution.

          * An AWS account number.

        - **KeyPairIds** *(dict) --*

          A complex type that lists the active CloudFront key pairs, if any, that are
          associated with ``AwsAccountNumber`` .

          - **Quantity** *(integer) --*

            The number of active CloudFront key pairs for ``AwsAccountNumber`` .

            For more information, see `ActiveTrustedSigners
            <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
            .

          - **Items** *(list) --*

            A complex type that lists the active CloudFront key pairs, if any, that are
            associated with ``AwsAccountNumber`` .

            For more information, see `ActiveTrustedSigners
            <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
            .

            - *(string) --*
    """


_ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef",
    {"Quantity": int, "Items": List[str]},
    total=False,
)


class ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef(
    _ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfig` `Aliases`

    A complex type that contains information about CNAMEs (alternate domain names), if any,
    for this streaming distribution.

    - **Quantity** *(integer) --*

      The number of CNAME aliases, if any, that you want to associate with this distribution.

    - **Items** *(list) --*

      A complex type that contains the CNAME aliases, if any, that you want to associate with
      this distribution.

      - *(string) --*
    """


_ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef",
    {"Enabled": bool, "Bucket": str, "Prefix": str},
    total=False,
)


class ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef(
    _ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfig` `Logging`

    A complex type that controls whether access logs are written for the streaming
    distribution.

    - **Enabled** *(boolean) --*

      Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If
      you don't want to enable logging when you create a streaming distribution or if you
      want to disable logging for an existing streaming distribution, specify ``false`` for
      ``Enabled`` , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify
      ``false`` for ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the
      values are automatically deleted.

    - **Bucket** *(string) --*

      The Amazon S3 bucket to store the access logs in, for example,
      ``myawslogbucket.s3.amazonaws.com`` .

    - **Prefix** *(string) --*

      An optional string that you want CloudFront to prefix to the access log filenames for
      this streaming distribution, for example, ``myprefix/`` . If you want to enable
      logging, but you don't want to specify a prefix, you still must include an empty
      ``Prefix`` element in the ``Logging`` element.
    """


_ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef",
    {"DomainName": str, "OriginAccessIdentity": str},
    total=False,
)


class ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef(
    _ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfig` `S3Origin`

    A complex type that contains information about the Amazon S3 bucket from which you want
    CloudFront to get your media files for distribution.

    - **DomainName** *(string) --*

      The DNS name of the Amazon S3 origin.

    - **OriginAccessIdentity** *(string) --*

      The CloudFront origin access identity to associate with the distribution. Use an origin
      access identity to configure the distribution so that end users can only access objects
      in an Amazon S3 bucket through CloudFront.

      If you want end users to be able to access objects using either the CloudFront URL or
      the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

      To delete the origin access identity from an existing distribution, update the
      distribution configuration and include an empty ``OriginAccessIdentity`` element.

      To replace the origin access identity, update the distribution configuration and
      specify the new origin access identity.

      For more information, see `Using an Origin Access Identity to Restrict Access to Your
      Amazon S3 Content
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
      in the *Amazon CloudFront Developer Guide* .
    """


_ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef",
    {"Enabled": bool, "Quantity": int, "Items": List[str]},
    total=False,
)


class ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef(
    _ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfig` `TrustedSigners`

    A complex type that specifies any AWS accounts that you want to permit to create signed
    URLs for private content. If you want the distribution to use signed URLs, include this
    element; if you want the distribution to use public URLs, remove this element. For more
    information, see `Serving Private Content through CloudFront
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
    in the *Amazon CloudFront Developer Guide* .

    - **Enabled** *(boolean) --*

      Specifies whether you want to require viewers to use signed URLs to access the files
      specified by ``PathPattern`` and ``TargetOriginId`` .

    - **Quantity** *(integer) --*

      The number of trusted signers for this cache behavior.

    - **Items** *(list) --*

       **Optional** : A complex type that contains trusted signers for this cache behavior.
       If ``Quantity`` is ``0`` , you can omit ``Items`` .

      - *(string) --*
    """


_ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "S3Origin": ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef,
        "Aliases": ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef,
        "Comment": str,
        "Logging": ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef,
        "TrustedSigners": ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef,
        "PriceClass": str,
        "Enabled": bool,
    },
    total=False,
)


class ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTypeDef(
    _ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionResponseStreamingDistribution` `StreamingDistributionConfig`

    The current configuration information for the RTMP distribution.

    - **CallerReference** *(string) --*

      A unique value (for example, a date-time stamp) that ensures that the request can't be
      replayed.

      If the value of ``CallerReference`` is new (regardless of the content of the
      ``StreamingDistributionConfig`` object), CloudFront creates a new distribution.

      If ``CallerReference`` is a value that you already sent in a previous request to create a
      distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

    - **S3Origin** *(dict) --*

      A complex type that contains information about the Amazon S3 bucket from which you want
      CloudFront to get your media files for distribution.

      - **DomainName** *(string) --*

        The DNS name of the Amazon S3 origin.

      - **OriginAccessIdentity** *(string) --*

        The CloudFront origin access identity to associate with the distribution. Use an origin
        access identity to configure the distribution so that end users can only access objects
        in an Amazon S3 bucket through CloudFront.

        If you want end users to be able to access objects using either the CloudFront URL or
        the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

        To delete the origin access identity from an existing distribution, update the
        distribution configuration and include an empty ``OriginAccessIdentity`` element.

        To replace the origin access identity, update the distribution configuration and
        specify the new origin access identity.

        For more information, see `Using an Origin Access Identity to Restrict Access to Your
        Amazon S3 Content
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
        in the *Amazon CloudFront Developer Guide* .

    - **Aliases** *(dict) --*

      A complex type that contains information about CNAMEs (alternate domain names), if any,
      for this streaming distribution.

      - **Quantity** *(integer) --*

        The number of CNAME aliases, if any, that you want to associate with this distribution.

      - **Items** *(list) --*

        A complex type that contains the CNAME aliases, if any, that you want to associate with
        this distribution.

        - *(string) --*

    - **Comment** *(string) --*

      Any comments you want to include about the streaming distribution.

    - **Logging** *(dict) --*

      A complex type that controls whether access logs are written for the streaming
      distribution.

      - **Enabled** *(boolean) --*

        Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If
        you don't want to enable logging when you create a streaming distribution or if you
        want to disable logging for an existing streaming distribution, specify ``false`` for
        ``Enabled`` , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify
        ``false`` for ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the
        values are automatically deleted.

      - **Bucket** *(string) --*

        The Amazon S3 bucket to store the access logs in, for example,
        ``myawslogbucket.s3.amazonaws.com`` .

      - **Prefix** *(string) --*

        An optional string that you want CloudFront to prefix to the access log filenames for
        this streaming distribution, for example, ``myprefix/`` . If you want to enable
        logging, but you don't want to specify a prefix, you still must include an empty
        ``Prefix`` element in the ``Logging`` element.

    - **TrustedSigners** *(dict) --*

      A complex type that specifies any AWS accounts that you want to permit to create signed
      URLs for private content. If you want the distribution to use signed URLs, include this
      element; if you want the distribution to use public URLs, remove this element. For more
      information, see `Serving Private Content through CloudFront
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
      in the *Amazon CloudFront Developer Guide* .

      - **Enabled** *(boolean) --*

        Specifies whether you want to require viewers to use signed URLs to access the files
        specified by ``PathPattern`` and ``TargetOriginId`` .

      - **Quantity** *(integer) --*

        The number of trusted signers for this cache behavior.

      - **Items** *(list) --*

         **Optional** : A complex type that contains trusted signers for this cache behavior.
         If ``Quantity`` is ``0`` , you can omit ``Items`` .

        - *(string) --*

    - **PriceClass** *(string) --*

      A complex type that contains information about price class for this streaming
      distribution.

    - **Enabled** *(boolean) --*

      Whether the streaming distribution is enabled to accept user requests for content.
    """


_ClientCreateStreamingDistributionResponseStreamingDistributionTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionResponseStreamingDistributionTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "DomainName": str,
        "ActiveTrustedSigners": ClientCreateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersTypeDef,
        "StreamingDistributionConfig": ClientCreateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTypeDef,
    },
    total=False,
)


class ClientCreateStreamingDistributionResponseStreamingDistributionTypeDef(
    _ClientCreateStreamingDistributionResponseStreamingDistributionTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionResponse` `StreamingDistribution`

    The streaming distribution's information.

    - **Id** *(string) --*

      The identifier for the RTMP distribution. For example: ``EGTXBD79EXAMPLE`` .

    - **ARN** *(string) --*

      The ARN (Amazon Resource Name) for the distribution. For example:
      ``arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`` , where ``123456789012``
      is your AWS account ID.

    - **Status** *(string) --*

      The current status of the RTMP distribution. When the status is ``Deployed`` , the
      distribution's information is propagated to all CloudFront edge locations.

    - **LastModifiedTime** *(datetime) --*

      The date and time that the distribution was last modified.

    - **DomainName** *(string) --*

      The domain name that corresponds to the streaming distribution, for example,
      ``s5c39gqb8ow64r.cloudfront.net`` .

    - **ActiveTrustedSigners** *(dict) --*

      A complex type that lists the AWS accounts, if any, that you included in the
      ``TrustedSigners`` complex type for this distribution. These are the accounts that you want
      to allow to create signed URLs for private content.

      The ``Signer`` complex type lists the AWS account number of the trusted signer or ``self``
      if the signer is the AWS account that created the distribution. The ``Signer`` element also
      includes the IDs of any active CloudFront key pairs that are associated with the trusted
      signer's AWS account. If no ``KeyPairId`` element appears for a ``Signer`` , that signer
      can't create signed URLs.

      For more information, see `Serving Private Content through CloudFront
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
      in the *Amazon CloudFront Developer Guide* .

      - **Enabled** *(boolean) --*

        Enabled is ``true`` if any of the AWS accounts listed in the ``TrustedSigners`` complex
        type for this distribution have active CloudFront key pairs. If not, ``Enabled`` is
        ``false`` .

      - **Quantity** *(integer) --*

        The number of trusted signers specified in the ``TrustedSigners`` complex type.

      - **Items** *(list) --*

        A complex type that contains one ``Signer`` complex type for each trusted signer that is
        specified in the ``TrustedSigners`` complex type.

        - *(dict) --*

          A complex type that lists the AWS accounts that were included in the ``TrustedSigners``
          complex type, as well as their active CloudFront key pair IDs, if any.

          - **AwsAccountNumber** *(string) --*

            An AWS account that is included in the ``TrustedSigners`` complex type for this
            distribution. Valid values include:

            * ``self`` , which is the AWS account used to create the distribution.

            * An AWS account number.

          - **KeyPairIds** *(dict) --*

            A complex type that lists the active CloudFront key pairs, if any, that are
            associated with ``AwsAccountNumber`` .

            - **Quantity** *(integer) --*

              The number of active CloudFront key pairs for ``AwsAccountNumber`` .

              For more information, see `ActiveTrustedSigners
              <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
              .

            - **Items** *(list) --*

              A complex type that lists the active CloudFront key pairs, if any, that are
              associated with ``AwsAccountNumber`` .

              For more information, see `ActiveTrustedSigners
              <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
              .

              - *(string) --*

    - **StreamingDistributionConfig** *(dict) --*

      The current configuration information for the RTMP distribution.

      - **CallerReference** *(string) --*

        A unique value (for example, a date-time stamp) that ensures that the request can't be
        replayed.

        If the value of ``CallerReference`` is new (regardless of the content of the
        ``StreamingDistributionConfig`` object), CloudFront creates a new distribution.

        If ``CallerReference`` is a value that you already sent in a previous request to create a
        distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

      - **S3Origin** *(dict) --*

        A complex type that contains information about the Amazon S3 bucket from which you want
        CloudFront to get your media files for distribution.

        - **DomainName** *(string) --*

          The DNS name of the Amazon S3 origin.

        - **OriginAccessIdentity** *(string) --*

          The CloudFront origin access identity to associate with the distribution. Use an origin
          access identity to configure the distribution so that end users can only access objects
          in an Amazon S3 bucket through CloudFront.

          If you want end users to be able to access objects using either the CloudFront URL or
          the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

          To delete the origin access identity from an existing distribution, update the
          distribution configuration and include an empty ``OriginAccessIdentity`` element.

          To replace the origin access identity, update the distribution configuration and
          specify the new origin access identity.

          For more information, see `Using an Origin Access Identity to Restrict Access to Your
          Amazon S3 Content
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
          in the *Amazon CloudFront Developer Guide* .

      - **Aliases** *(dict) --*

        A complex type that contains information about CNAMEs (alternate domain names), if any,
        for this streaming distribution.

        - **Quantity** *(integer) --*

          The number of CNAME aliases, if any, that you want to associate with this distribution.

        - **Items** *(list) --*

          A complex type that contains the CNAME aliases, if any, that you want to associate with
          this distribution.

          - *(string) --*

      - **Comment** *(string) --*

        Any comments you want to include about the streaming distribution.

      - **Logging** *(dict) --*

        A complex type that controls whether access logs are written for the streaming
        distribution.

        - **Enabled** *(boolean) --*

          Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If
          you don't want to enable logging when you create a streaming distribution or if you
          want to disable logging for an existing streaming distribution, specify ``false`` for
          ``Enabled`` , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify
          ``false`` for ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the
          values are automatically deleted.

        - **Bucket** *(string) --*

          The Amazon S3 bucket to store the access logs in, for example,
          ``myawslogbucket.s3.amazonaws.com`` .

        - **Prefix** *(string) --*

          An optional string that you want CloudFront to prefix to the access log filenames for
          this streaming distribution, for example, ``myprefix/`` . If you want to enable
          logging, but you don't want to specify a prefix, you still must include an empty
          ``Prefix`` element in the ``Logging`` element.

      - **TrustedSigners** *(dict) --*

        A complex type that specifies any AWS accounts that you want to permit to create signed
        URLs for private content. If you want the distribution to use signed URLs, include this
        element; if you want the distribution to use public URLs, remove this element. For more
        information, see `Serving Private Content through CloudFront
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
        in the *Amazon CloudFront Developer Guide* .

        - **Enabled** *(boolean) --*

          Specifies whether you want to require viewers to use signed URLs to access the files
          specified by ``PathPattern`` and ``TargetOriginId`` .

        - **Quantity** *(integer) --*

          The number of trusted signers for this cache behavior.

        - **Items** *(list) --*

           **Optional** : A complex type that contains trusted signers for this cache behavior.
           If ``Quantity`` is ``0`` , you can omit ``Items`` .

          - *(string) --*

      - **PriceClass** *(string) --*

        A complex type that contains information about price class for this streaming
        distribution.

      - **Enabled** *(boolean) --*

        Whether the streaming distribution is enabled to accept user requests for content.
    """


_ClientCreateStreamingDistributionResponseTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionResponseTypeDef",
    {
        "StreamingDistribution": ClientCreateStreamingDistributionResponseStreamingDistributionTypeDef,
        "Location": str,
        "ETag": str,
    },
    total=False,
)


class ClientCreateStreamingDistributionResponseTypeDef(
    _ClientCreateStreamingDistributionResponseTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistribution` `Response`

    The returned result of the corresponding request.

    - **StreamingDistribution** *(dict) --*

      The streaming distribution's information.

      - **Id** *(string) --*

        The identifier for the RTMP distribution. For example: ``EGTXBD79EXAMPLE`` .

      - **ARN** *(string) --*

        The ARN (Amazon Resource Name) for the distribution. For example:
        ``arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`` , where ``123456789012``
        is your AWS account ID.

      - **Status** *(string) --*

        The current status of the RTMP distribution. When the status is ``Deployed`` , the
        distribution's information is propagated to all CloudFront edge locations.

      - **LastModifiedTime** *(datetime) --*

        The date and time that the distribution was last modified.

      - **DomainName** *(string) --*

        The domain name that corresponds to the streaming distribution, for example,
        ``s5c39gqb8ow64r.cloudfront.net`` .

      - **ActiveTrustedSigners** *(dict) --*

        A complex type that lists the AWS accounts, if any, that you included in the
        ``TrustedSigners`` complex type for this distribution. These are the accounts that you want
        to allow to create signed URLs for private content.

        The ``Signer`` complex type lists the AWS account number of the trusted signer or ``self``
        if the signer is the AWS account that created the distribution. The ``Signer`` element also
        includes the IDs of any active CloudFront key pairs that are associated with the trusted
        signer's AWS account. If no ``KeyPairId`` element appears for a ``Signer`` , that signer
        can't create signed URLs.

        For more information, see `Serving Private Content through CloudFront
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
        in the *Amazon CloudFront Developer Guide* .

        - **Enabled** *(boolean) --*

          Enabled is ``true`` if any of the AWS accounts listed in the ``TrustedSigners`` complex
          type for this distribution have active CloudFront key pairs. If not, ``Enabled`` is
          ``false`` .

        - **Quantity** *(integer) --*

          The number of trusted signers specified in the ``TrustedSigners`` complex type.

        - **Items** *(list) --*

          A complex type that contains one ``Signer`` complex type for each trusted signer that is
          specified in the ``TrustedSigners`` complex type.

          - *(dict) --*

            A complex type that lists the AWS accounts that were included in the ``TrustedSigners``
            complex type, as well as their active CloudFront key pair IDs, if any.

            - **AwsAccountNumber** *(string) --*

              An AWS account that is included in the ``TrustedSigners`` complex type for this
              distribution. Valid values include:

              * ``self`` , which is the AWS account used to create the distribution.

              * An AWS account number.

            - **KeyPairIds** *(dict) --*

              A complex type that lists the active CloudFront key pairs, if any, that are
              associated with ``AwsAccountNumber`` .

              - **Quantity** *(integer) --*

                The number of active CloudFront key pairs for ``AwsAccountNumber`` .

                For more information, see `ActiveTrustedSigners
                <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
                .

              - **Items** *(list) --*

                A complex type that lists the active CloudFront key pairs, if any, that are
                associated with ``AwsAccountNumber`` .

                For more information, see `ActiveTrustedSigners
                <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
                .

                - *(string) --*

      - **StreamingDistributionConfig** *(dict) --*

        The current configuration information for the RTMP distribution.

        - **CallerReference** *(string) --*

          A unique value (for example, a date-time stamp) that ensures that the request can't be
          replayed.

          If the value of ``CallerReference`` is new (regardless of the content of the
          ``StreamingDistributionConfig`` object), CloudFront creates a new distribution.

          If ``CallerReference`` is a value that you already sent in a previous request to create a
          distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

        - **S3Origin** *(dict) --*

          A complex type that contains information about the Amazon S3 bucket from which you want
          CloudFront to get your media files for distribution.

          - **DomainName** *(string) --*

            The DNS name of the Amazon S3 origin.

          - **OriginAccessIdentity** *(string) --*

            The CloudFront origin access identity to associate with the distribution. Use an origin
            access identity to configure the distribution so that end users can only access objects
            in an Amazon S3 bucket through CloudFront.

            If you want end users to be able to access objects using either the CloudFront URL or
            the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

            To delete the origin access identity from an existing distribution, update the
            distribution configuration and include an empty ``OriginAccessIdentity`` element.

            To replace the origin access identity, update the distribution configuration and
            specify the new origin access identity.

            For more information, see `Using an Origin Access Identity to Restrict Access to Your
            Amazon S3 Content
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
            in the *Amazon CloudFront Developer Guide* .

        - **Aliases** *(dict) --*

          A complex type that contains information about CNAMEs (alternate domain names), if any,
          for this streaming distribution.

          - **Quantity** *(integer) --*

            The number of CNAME aliases, if any, that you want to associate with this distribution.

          - **Items** *(list) --*

            A complex type that contains the CNAME aliases, if any, that you want to associate with
            this distribution.

            - *(string) --*

        - **Comment** *(string) --*

          Any comments you want to include about the streaming distribution.

        - **Logging** *(dict) --*

          A complex type that controls whether access logs are written for the streaming
          distribution.

          - **Enabled** *(boolean) --*

            Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If
            you don't want to enable logging when you create a streaming distribution or if you
            want to disable logging for an existing streaming distribution, specify ``false`` for
            ``Enabled`` , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify
            ``false`` for ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the
            values are automatically deleted.

          - **Bucket** *(string) --*

            The Amazon S3 bucket to store the access logs in, for example,
            ``myawslogbucket.s3.amazonaws.com`` .

          - **Prefix** *(string) --*

            An optional string that you want CloudFront to prefix to the access log filenames for
            this streaming distribution, for example, ``myprefix/`` . If you want to enable
            logging, but you don't want to specify a prefix, you still must include an empty
            ``Prefix`` element in the ``Logging`` element.

        - **TrustedSigners** *(dict) --*

          A complex type that specifies any AWS accounts that you want to permit to create signed
          URLs for private content. If you want the distribution to use signed URLs, include this
          element; if you want the distribution to use public URLs, remove this element. For more
          information, see `Serving Private Content through CloudFront
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
          in the *Amazon CloudFront Developer Guide* .

          - **Enabled** *(boolean) --*

            Specifies whether you want to require viewers to use signed URLs to access the files
            specified by ``PathPattern`` and ``TargetOriginId`` .

          - **Quantity** *(integer) --*

            The number of trusted signers for this cache behavior.

          - **Items** *(list) --*

             **Optional** : A complex type that contains trusted signers for this cache behavior.
             If ``Quantity`` is ``0`` , you can omit ``Items`` .

            - *(string) --*

        - **PriceClass** *(string) --*

          A complex type that contains information about price class for this streaming
          distribution.

        - **Enabled** *(boolean) --*

          Whether the streaming distribution is enabled to accept user requests for content.

    - **Location** *(string) --*

      The fully qualified URI of the new streaming distribution resource just created. For example:
      ``https://cloudfront.amazonaws.com/2010-11-01/streaming-distribution/EGTXBD79H29TRA8`` .

    - **ETag** *(string) --*

      The current version of the streaming distribution created.
    """


_RequiredClientCreateStreamingDistributionStreamingDistributionConfigAliasesTypeDef = TypedDict(
    "_RequiredClientCreateStreamingDistributionStreamingDistributionConfigAliasesTypeDef",
    {"Quantity": int},
)
_OptionalClientCreateStreamingDistributionStreamingDistributionConfigAliasesTypeDef = TypedDict(
    "_OptionalClientCreateStreamingDistributionStreamingDistributionConfigAliasesTypeDef",
    {"Items": List[str]},
    total=False,
)


class ClientCreateStreamingDistributionStreamingDistributionConfigAliasesTypeDef(
    _RequiredClientCreateStreamingDistributionStreamingDistributionConfigAliasesTypeDef,
    _OptionalClientCreateStreamingDistributionStreamingDistributionConfigAliasesTypeDef,
):
    """
    Type definition for `ClientCreateStreamingDistributionStreamingDistributionConfig` `Aliases`

    A complex type that contains information about CNAMEs (alternate domain names), if any, for
    this streaming distribution.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of CNAME aliases, if any, that you want to associate with this distribution.

    - **Items** *(list) --*

      A complex type that contains the CNAME aliases, if any, that you want to associate with this
      distribution.

      - *(string) --*
    """


_ClientCreateStreamingDistributionStreamingDistributionConfigLoggingTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionStreamingDistributionConfigLoggingTypeDef",
    {"Enabled": bool, "Bucket": str, "Prefix": str},
)


class ClientCreateStreamingDistributionStreamingDistributionConfigLoggingTypeDef(
    _ClientCreateStreamingDistributionStreamingDistributionConfigLoggingTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionStreamingDistributionConfig` `Logging`

    A complex type that controls whether access logs are written for the streaming distribution.

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you
      don't want to enable logging when you create a streaming distribution or if you want to
      disable logging for an existing streaming distribution, specify ``false`` for ``Enabled`` ,
      and specify ``empty Bucket`` and ``Prefix`` elements. If you specify ``false`` for
      ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the values are
      automatically deleted.

    - **Bucket** *(string) --* **[REQUIRED]**

      The Amazon S3 bucket to store the access logs in, for example,
      ``myawslogbucket.s3.amazonaws.com`` .

    - **Prefix** *(string) --* **[REQUIRED]**

      An optional string that you want CloudFront to prefix to the access log filenames for this
      streaming distribution, for example, ``myprefix/`` . If you want to enable logging, but you
      don't want to specify a prefix, you still must include an empty ``Prefix`` element in the
      ``Logging`` element.
    """


_ClientCreateStreamingDistributionStreamingDistributionConfigS3OriginTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionStreamingDistributionConfigS3OriginTypeDef",
    {"DomainName": str, "OriginAccessIdentity": str},
)


class ClientCreateStreamingDistributionStreamingDistributionConfigS3OriginTypeDef(
    _ClientCreateStreamingDistributionStreamingDistributionConfigS3OriginTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionStreamingDistributionConfig` `S3Origin`

    A complex type that contains information about the Amazon S3 bucket from which you want
    CloudFront to get your media files for distribution.

    - **DomainName** *(string) --* **[REQUIRED]**

      The DNS name of the Amazon S3 origin.

    - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

      The CloudFront origin access identity to associate with the distribution. Use an origin
      access identity to configure the distribution so that end users can only access objects in an
      Amazon S3 bucket through CloudFront.

      If you want end users to be able to access objects using either the CloudFront URL or the
      Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

      To delete the origin access identity from an existing distribution, update the distribution
      configuration and include an empty ``OriginAccessIdentity`` element.

      To replace the origin access identity, update the distribution configuration and specify the
      new origin access identity.

      For more information, see `Using an Origin Access Identity to Restrict Access to Your Amazon
      S3 Content
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
      in the *Amazon CloudFront Developer Guide* .
    """


_RequiredClientCreateStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef = TypedDict(
    "_RequiredClientCreateStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef",
    {"Enabled": bool, "Quantity": int},
)
_OptionalClientCreateStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef = TypedDict(
    "_OptionalClientCreateStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef",
    {"Items": List[str]},
    total=False,
)


class ClientCreateStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef(
    _RequiredClientCreateStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef,
    _OptionalClientCreateStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef,
):
    """
    Type definition for `ClientCreateStreamingDistributionStreamingDistributionConfig` `TrustedSigners`

    A complex type that specifies any AWS accounts that you want to permit to create signed URLs
    for private content. If you want the distribution to use signed URLs, include this element; if
    you want the distribution to use public URLs, remove this element. For more information, see
    `Serving Private Content through CloudFront
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__ in
    the *Amazon CloudFront Developer Guide* .

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Specifies whether you want to require viewers to use signed URLs to access the files
      specified by ``PathPattern`` and ``TargetOriginId`` .

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of trusted signers for this cache behavior.

    - **Items** *(list) --*

       **Optional** : A complex type that contains trusted signers for this cache behavior. If
       ``Quantity`` is ``0`` , you can omit ``Items`` .

      - *(string) --*
    """


_RequiredClientCreateStreamingDistributionStreamingDistributionConfigTypeDef = TypedDict(
    "_RequiredClientCreateStreamingDistributionStreamingDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "S3Origin": ClientCreateStreamingDistributionStreamingDistributionConfigS3OriginTypeDef,
        "Comment": str,
        "TrustedSigners": ClientCreateStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef,
        "Enabled": bool,
    },
)
_OptionalClientCreateStreamingDistributionStreamingDistributionConfigTypeDef = TypedDict(
    "_OptionalClientCreateStreamingDistributionStreamingDistributionConfigTypeDef",
    {
        "Aliases": ClientCreateStreamingDistributionStreamingDistributionConfigAliasesTypeDef,
        "Logging": ClientCreateStreamingDistributionStreamingDistributionConfigLoggingTypeDef,
        "PriceClass": str,
    },
    total=False,
)


class ClientCreateStreamingDistributionStreamingDistributionConfigTypeDef(
    _RequiredClientCreateStreamingDistributionStreamingDistributionConfigTypeDef,
    _OptionalClientCreateStreamingDistributionStreamingDistributionConfigTypeDef,
):
    """
    Type definition for `ClientCreateStreamingDistribution` `StreamingDistributionConfig`

    The streaming distribution's configuration information.

    - **CallerReference** *(string) --* **[REQUIRED]**

      A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.

      If the value of ``CallerReference`` is new (regardless of the content of the
      ``StreamingDistributionConfig`` object), CloudFront creates a new distribution.

      If ``CallerReference`` is a value that you already sent in a previous request to create a
      distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

    - **S3Origin** *(dict) --* **[REQUIRED]**

      A complex type that contains information about the Amazon S3 bucket from which you want
      CloudFront to get your media files for distribution.

      - **DomainName** *(string) --* **[REQUIRED]**

        The DNS name of the Amazon S3 origin.

      - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

        The CloudFront origin access identity to associate with the distribution. Use an origin
        access identity to configure the distribution so that end users can only access objects in an
        Amazon S3 bucket through CloudFront.

        If you want end users to be able to access objects using either the CloudFront URL or the
        Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

        To delete the origin access identity from an existing distribution, update the distribution
        configuration and include an empty ``OriginAccessIdentity`` element.

        To replace the origin access identity, update the distribution configuration and specify the
        new origin access identity.

        For more information, see `Using an Origin Access Identity to Restrict Access to Your Amazon
        S3 Content
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
        in the *Amazon CloudFront Developer Guide* .

    - **Aliases** *(dict) --*

      A complex type that contains information about CNAMEs (alternate domain names), if any, for
      this streaming distribution.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of CNAME aliases, if any, that you want to associate with this distribution.

      - **Items** *(list) --*

        A complex type that contains the CNAME aliases, if any, that you want to associate with this
        distribution.

        - *(string) --*

    - **Comment** *(string) --* **[REQUIRED]**

      Any comments you want to include about the streaming distribution.

    - **Logging** *(dict) --*

      A complex type that controls whether access logs are written for the streaming distribution.

      - **Enabled** *(boolean) --* **[REQUIRED]**

        Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you
        don't want to enable logging when you create a streaming distribution or if you want to
        disable logging for an existing streaming distribution, specify ``false`` for ``Enabled`` ,
        and specify ``empty Bucket`` and ``Prefix`` elements. If you specify ``false`` for
        ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the values are
        automatically deleted.

      - **Bucket** *(string) --* **[REQUIRED]**

        The Amazon S3 bucket to store the access logs in, for example,
        ``myawslogbucket.s3.amazonaws.com`` .

      - **Prefix** *(string) --* **[REQUIRED]**

        An optional string that you want CloudFront to prefix to the access log filenames for this
        streaming distribution, for example, ``myprefix/`` . If you want to enable logging, but you
        don't want to specify a prefix, you still must include an empty ``Prefix`` element in the
        ``Logging`` element.

    - **TrustedSigners** *(dict) --* **[REQUIRED]**

      A complex type that specifies any AWS accounts that you want to permit to create signed URLs
      for private content. If you want the distribution to use signed URLs, include this element; if
      you want the distribution to use public URLs, remove this element. For more information, see
      `Serving Private Content through CloudFront
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__ in
      the *Amazon CloudFront Developer Guide* .

      - **Enabled** *(boolean) --* **[REQUIRED]**

        Specifies whether you want to require viewers to use signed URLs to access the files
        specified by ``PathPattern`` and ``TargetOriginId`` .

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of trusted signers for this cache behavior.

      - **Items** *(list) --*

         **Optional** : A complex type that contains trusted signers for this cache behavior. If
         ``Quantity`` is ``0`` , you can omit ``Items`` .

        - *(string) --*

    - **PriceClass** *(string) --*

      A complex type that contains information about price class for this streaming distribution.

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Whether the streaming distribution is enabled to accept user requests for content.
    """


_ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef",
    {"Quantity": int, "Items": List[str]},
    total=False,
)


class ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef(
    _ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersItems` `KeyPairIds`

    A complex type that lists the active CloudFront key pairs, if any, that are
    associated with ``AwsAccountNumber`` .

    - **Quantity** *(integer) --*

      The number of active CloudFront key pairs for ``AwsAccountNumber`` .

      For more information, see `ActiveTrustedSigners
      <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
      .

    - **Items** *(list) --*

      A complex type that lists the active CloudFront key pairs, if any, that are
      associated with ``AwsAccountNumber`` .

      For more information, see `ActiveTrustedSigners
      <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
      .

      - *(string) --*
    """


_ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersItemsTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersItemsTypeDef",
    {
        "AwsAccountNumber": str,
        "KeyPairIds": ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef,
    },
    total=False,
)


class ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersItemsTypeDef(
    _ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersItemsTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSigners` `Items`

    A complex type that lists the AWS accounts that were included in the ``TrustedSigners``
    complex type, as well as their active CloudFront key pair IDs, if any.

    - **AwsAccountNumber** *(string) --*

      An AWS account that is included in the ``TrustedSigners`` complex type for this
      distribution. Valid values include:

      * ``self`` , which is the AWS account used to create the distribution.

      * An AWS account number.

    - **KeyPairIds** *(dict) --*

      A complex type that lists the active CloudFront key pairs, if any, that are
      associated with ``AwsAccountNumber`` .

      - **Quantity** *(integer) --*

        The number of active CloudFront key pairs for ``AwsAccountNumber`` .

        For more information, see `ActiveTrustedSigners
        <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
        .

      - **Items** *(list) --*

        A complex type that lists the active CloudFront key pairs, if any, that are
        associated with ``AwsAccountNumber`` .

        For more information, see `ActiveTrustedSigners
        <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
        .

        - *(string) --*
    """


_ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
        "Items": List[
            ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersItemsTypeDef
        ],
    },
    total=False,
)


class ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersTypeDef(
    _ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionWithTagsResponseStreamingDistribution` `ActiveTrustedSigners`

    A complex type that lists the AWS accounts, if any, that you included in the
    ``TrustedSigners`` complex type for this distribution. These are the accounts that you want
    to allow to create signed URLs for private content.

    The ``Signer`` complex type lists the AWS account number of the trusted signer or ``self``
    if the signer is the AWS account that created the distribution. The ``Signer`` element also
    includes the IDs of any active CloudFront key pairs that are associated with the trusted
    signer's AWS account. If no ``KeyPairId`` element appears for a ``Signer`` , that signer
    can't create signed URLs.

    For more information, see `Serving Private Content through CloudFront
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
    in the *Amazon CloudFront Developer Guide* .

    - **Enabled** *(boolean) --*

      Enabled is ``true`` if any of the AWS accounts listed in the ``TrustedSigners`` complex
      type for this distribution have active CloudFront key pairs. If not, ``Enabled`` is
      ``false`` .

    - **Quantity** *(integer) --*

      The number of trusted signers specified in the ``TrustedSigners`` complex type.

    - **Items** *(list) --*

      A complex type that contains one ``Signer`` complex type for each trusted signer that is
      specified in the ``TrustedSigners`` complex type.

      - *(dict) --*

        A complex type that lists the AWS accounts that were included in the ``TrustedSigners``
        complex type, as well as their active CloudFront key pair IDs, if any.

        - **AwsAccountNumber** *(string) --*

          An AWS account that is included in the ``TrustedSigners`` complex type for this
          distribution. Valid values include:

          * ``self`` , which is the AWS account used to create the distribution.

          * An AWS account number.

        - **KeyPairIds** *(dict) --*

          A complex type that lists the active CloudFront key pairs, if any, that are
          associated with ``AwsAccountNumber`` .

          - **Quantity** *(integer) --*

            The number of active CloudFront key pairs for ``AwsAccountNumber`` .

            For more information, see `ActiveTrustedSigners
            <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
            .

          - **Items** *(list) --*

            A complex type that lists the active CloudFront key pairs, if any, that are
            associated with ``AwsAccountNumber`` .

            For more information, see `ActiveTrustedSigners
            <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
            .

            - *(string) --*
    """


_ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef",
    {"Quantity": int, "Items": List[str]},
    total=False,
)


class ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef(
    _ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfig` `Aliases`

    A complex type that contains information about CNAMEs (alternate domain names), if any,
    for this streaming distribution.

    - **Quantity** *(integer) --*

      The number of CNAME aliases, if any, that you want to associate with this distribution.

    - **Items** *(list) --*

      A complex type that contains the CNAME aliases, if any, that you want to associate with
      this distribution.

      - *(string) --*
    """


_ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef",
    {"Enabled": bool, "Bucket": str, "Prefix": str},
    total=False,
)


class ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef(
    _ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfig` `Logging`

    A complex type that controls whether access logs are written for the streaming
    distribution.

    - **Enabled** *(boolean) --*

      Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If
      you don't want to enable logging when you create a streaming distribution or if you
      want to disable logging for an existing streaming distribution, specify ``false`` for
      ``Enabled`` , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify
      ``false`` for ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the
      values are automatically deleted.

    - **Bucket** *(string) --*

      The Amazon S3 bucket to store the access logs in, for example,
      ``myawslogbucket.s3.amazonaws.com`` .

    - **Prefix** *(string) --*

      An optional string that you want CloudFront to prefix to the access log filenames for
      this streaming distribution, for example, ``myprefix/`` . If you want to enable
      logging, but you don't want to specify a prefix, you still must include an empty
      ``Prefix`` element in the ``Logging`` element.
    """


_ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef",
    {"DomainName": str, "OriginAccessIdentity": str},
    total=False,
)


class ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef(
    _ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfig` `S3Origin`

    A complex type that contains information about the Amazon S3 bucket from which you want
    CloudFront to get your media files for distribution.

    - **DomainName** *(string) --*

      The DNS name of the Amazon S3 origin.

    - **OriginAccessIdentity** *(string) --*

      The CloudFront origin access identity to associate with the distribution. Use an origin
      access identity to configure the distribution so that end users can only access objects
      in an Amazon S3 bucket through CloudFront.

      If you want end users to be able to access objects using either the CloudFront URL or
      the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

      To delete the origin access identity from an existing distribution, update the
      distribution configuration and include an empty ``OriginAccessIdentity`` element.

      To replace the origin access identity, update the distribution configuration and
      specify the new origin access identity.

      For more information, see `Using an Origin Access Identity to Restrict Access to Your
      Amazon S3 Content
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
      in the *Amazon CloudFront Developer Guide* .
    """


_ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef",
    {"Enabled": bool, "Quantity": int, "Items": List[str]},
    total=False,
)


class ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef(
    _ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfig` `TrustedSigners`

    A complex type that specifies any AWS accounts that you want to permit to create signed
    URLs for private content. If you want the distribution to use signed URLs, include this
    element; if you want the distribution to use public URLs, remove this element. For more
    information, see `Serving Private Content through CloudFront
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
    in the *Amazon CloudFront Developer Guide* .

    - **Enabled** *(boolean) --*

      Specifies whether you want to require viewers to use signed URLs to access the files
      specified by ``PathPattern`` and ``TargetOriginId`` .

    - **Quantity** *(integer) --*

      The number of trusted signers for this cache behavior.

    - **Items** *(list) --*

       **Optional** : A complex type that contains trusted signers for this cache behavior.
       If ``Quantity`` is ``0`` , you can omit ``Items`` .

      - *(string) --*
    """


_ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "S3Origin": ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef,
        "Aliases": ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef,
        "Comment": str,
        "Logging": ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef,
        "TrustedSigners": ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef,
        "PriceClass": str,
        "Enabled": bool,
    },
    total=False,
)


class ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigTypeDef(
    _ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionWithTagsResponseStreamingDistribution` `StreamingDistributionConfig`

    The current configuration information for the RTMP distribution.

    - **CallerReference** *(string) --*

      A unique value (for example, a date-time stamp) that ensures that the request can't be
      replayed.

      If the value of ``CallerReference`` is new (regardless of the content of the
      ``StreamingDistributionConfig`` object), CloudFront creates a new distribution.

      If ``CallerReference`` is a value that you already sent in a previous request to create a
      distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

    - **S3Origin** *(dict) --*

      A complex type that contains information about the Amazon S3 bucket from which you want
      CloudFront to get your media files for distribution.

      - **DomainName** *(string) --*

        The DNS name of the Amazon S3 origin.

      - **OriginAccessIdentity** *(string) --*

        The CloudFront origin access identity to associate with the distribution. Use an origin
        access identity to configure the distribution so that end users can only access objects
        in an Amazon S3 bucket through CloudFront.

        If you want end users to be able to access objects using either the CloudFront URL or
        the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

        To delete the origin access identity from an existing distribution, update the
        distribution configuration and include an empty ``OriginAccessIdentity`` element.

        To replace the origin access identity, update the distribution configuration and
        specify the new origin access identity.

        For more information, see `Using an Origin Access Identity to Restrict Access to Your
        Amazon S3 Content
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
        in the *Amazon CloudFront Developer Guide* .

    - **Aliases** *(dict) --*

      A complex type that contains information about CNAMEs (alternate domain names), if any,
      for this streaming distribution.

      - **Quantity** *(integer) --*

        The number of CNAME aliases, if any, that you want to associate with this distribution.

      - **Items** *(list) --*

        A complex type that contains the CNAME aliases, if any, that you want to associate with
        this distribution.

        - *(string) --*

    - **Comment** *(string) --*

      Any comments you want to include about the streaming distribution.

    - **Logging** *(dict) --*

      A complex type that controls whether access logs are written for the streaming
      distribution.

      - **Enabled** *(boolean) --*

        Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If
        you don't want to enable logging when you create a streaming distribution or if you
        want to disable logging for an existing streaming distribution, specify ``false`` for
        ``Enabled`` , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify
        ``false`` for ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the
        values are automatically deleted.

      - **Bucket** *(string) --*

        The Amazon S3 bucket to store the access logs in, for example,
        ``myawslogbucket.s3.amazonaws.com`` .

      - **Prefix** *(string) --*

        An optional string that you want CloudFront to prefix to the access log filenames for
        this streaming distribution, for example, ``myprefix/`` . If you want to enable
        logging, but you don't want to specify a prefix, you still must include an empty
        ``Prefix`` element in the ``Logging`` element.

    - **TrustedSigners** *(dict) --*

      A complex type that specifies any AWS accounts that you want to permit to create signed
      URLs for private content. If you want the distribution to use signed URLs, include this
      element; if you want the distribution to use public URLs, remove this element. For more
      information, see `Serving Private Content through CloudFront
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
      in the *Amazon CloudFront Developer Guide* .

      - **Enabled** *(boolean) --*

        Specifies whether you want to require viewers to use signed URLs to access the files
        specified by ``PathPattern`` and ``TargetOriginId`` .

      - **Quantity** *(integer) --*

        The number of trusted signers for this cache behavior.

      - **Items** *(list) --*

         **Optional** : A complex type that contains trusted signers for this cache behavior.
         If ``Quantity`` is ``0`` , you can omit ``Items`` .

        - *(string) --*

    - **PriceClass** *(string) --*

      A complex type that contains information about price class for this streaming
      distribution.

    - **Enabled** *(boolean) --*

      Whether the streaming distribution is enabled to accept user requests for content.
    """


_ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "DomainName": str,
        "ActiveTrustedSigners": ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionActiveTrustedSignersTypeDef,
        "StreamingDistributionConfig": ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionStreamingDistributionConfigTypeDef,
    },
    total=False,
)


class ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionTypeDef(
    _ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionWithTagsResponse` `StreamingDistribution`

    The streaming distribution's information.

    - **Id** *(string) --*

      The identifier for the RTMP distribution. For example: ``EGTXBD79EXAMPLE`` .

    - **ARN** *(string) --*

      The ARN (Amazon Resource Name) for the distribution. For example:
      ``arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`` , where ``123456789012``
      is your AWS account ID.

    - **Status** *(string) --*

      The current status of the RTMP distribution. When the status is ``Deployed`` , the
      distribution's information is propagated to all CloudFront edge locations.

    - **LastModifiedTime** *(datetime) --*

      The date and time that the distribution was last modified.

    - **DomainName** *(string) --*

      The domain name that corresponds to the streaming distribution, for example,
      ``s5c39gqb8ow64r.cloudfront.net`` .

    - **ActiveTrustedSigners** *(dict) --*

      A complex type that lists the AWS accounts, if any, that you included in the
      ``TrustedSigners`` complex type for this distribution. These are the accounts that you want
      to allow to create signed URLs for private content.

      The ``Signer`` complex type lists the AWS account number of the trusted signer or ``self``
      if the signer is the AWS account that created the distribution. The ``Signer`` element also
      includes the IDs of any active CloudFront key pairs that are associated with the trusted
      signer's AWS account. If no ``KeyPairId`` element appears for a ``Signer`` , that signer
      can't create signed URLs.

      For more information, see `Serving Private Content through CloudFront
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
      in the *Amazon CloudFront Developer Guide* .

      - **Enabled** *(boolean) --*

        Enabled is ``true`` if any of the AWS accounts listed in the ``TrustedSigners`` complex
        type for this distribution have active CloudFront key pairs. If not, ``Enabled`` is
        ``false`` .

      - **Quantity** *(integer) --*

        The number of trusted signers specified in the ``TrustedSigners`` complex type.

      - **Items** *(list) --*

        A complex type that contains one ``Signer`` complex type for each trusted signer that is
        specified in the ``TrustedSigners`` complex type.

        - *(dict) --*

          A complex type that lists the AWS accounts that were included in the ``TrustedSigners``
          complex type, as well as their active CloudFront key pair IDs, if any.

          - **AwsAccountNumber** *(string) --*

            An AWS account that is included in the ``TrustedSigners`` complex type for this
            distribution. Valid values include:

            * ``self`` , which is the AWS account used to create the distribution.

            * An AWS account number.

          - **KeyPairIds** *(dict) --*

            A complex type that lists the active CloudFront key pairs, if any, that are
            associated with ``AwsAccountNumber`` .

            - **Quantity** *(integer) --*

              The number of active CloudFront key pairs for ``AwsAccountNumber`` .

              For more information, see `ActiveTrustedSigners
              <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
              .

            - **Items** *(list) --*

              A complex type that lists the active CloudFront key pairs, if any, that are
              associated with ``AwsAccountNumber`` .

              For more information, see `ActiveTrustedSigners
              <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
              .

              - *(string) --*

    - **StreamingDistributionConfig** *(dict) --*

      The current configuration information for the RTMP distribution.

      - **CallerReference** *(string) --*

        A unique value (for example, a date-time stamp) that ensures that the request can't be
        replayed.

        If the value of ``CallerReference`` is new (regardless of the content of the
        ``StreamingDistributionConfig`` object), CloudFront creates a new distribution.

        If ``CallerReference`` is a value that you already sent in a previous request to create a
        distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

      - **S3Origin** *(dict) --*

        A complex type that contains information about the Amazon S3 bucket from which you want
        CloudFront to get your media files for distribution.

        - **DomainName** *(string) --*

          The DNS name of the Amazon S3 origin.

        - **OriginAccessIdentity** *(string) --*

          The CloudFront origin access identity to associate with the distribution. Use an origin
          access identity to configure the distribution so that end users can only access objects
          in an Amazon S3 bucket through CloudFront.

          If you want end users to be able to access objects using either the CloudFront URL or
          the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

          To delete the origin access identity from an existing distribution, update the
          distribution configuration and include an empty ``OriginAccessIdentity`` element.

          To replace the origin access identity, update the distribution configuration and
          specify the new origin access identity.

          For more information, see `Using an Origin Access Identity to Restrict Access to Your
          Amazon S3 Content
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
          in the *Amazon CloudFront Developer Guide* .

      - **Aliases** *(dict) --*

        A complex type that contains information about CNAMEs (alternate domain names), if any,
        for this streaming distribution.

        - **Quantity** *(integer) --*

          The number of CNAME aliases, if any, that you want to associate with this distribution.

        - **Items** *(list) --*

          A complex type that contains the CNAME aliases, if any, that you want to associate with
          this distribution.

          - *(string) --*

      - **Comment** *(string) --*

        Any comments you want to include about the streaming distribution.

      - **Logging** *(dict) --*

        A complex type that controls whether access logs are written for the streaming
        distribution.

        - **Enabled** *(boolean) --*

          Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If
          you don't want to enable logging when you create a streaming distribution or if you
          want to disable logging for an existing streaming distribution, specify ``false`` for
          ``Enabled`` , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify
          ``false`` for ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the
          values are automatically deleted.

        - **Bucket** *(string) --*

          The Amazon S3 bucket to store the access logs in, for example,
          ``myawslogbucket.s3.amazonaws.com`` .

        - **Prefix** *(string) --*

          An optional string that you want CloudFront to prefix to the access log filenames for
          this streaming distribution, for example, ``myprefix/`` . If you want to enable
          logging, but you don't want to specify a prefix, you still must include an empty
          ``Prefix`` element in the ``Logging`` element.

      - **TrustedSigners** *(dict) --*

        A complex type that specifies any AWS accounts that you want to permit to create signed
        URLs for private content. If you want the distribution to use signed URLs, include this
        element; if you want the distribution to use public URLs, remove this element. For more
        information, see `Serving Private Content through CloudFront
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
        in the *Amazon CloudFront Developer Guide* .

        - **Enabled** *(boolean) --*

          Specifies whether you want to require viewers to use signed URLs to access the files
          specified by ``PathPattern`` and ``TargetOriginId`` .

        - **Quantity** *(integer) --*

          The number of trusted signers for this cache behavior.

        - **Items** *(list) --*

           **Optional** : A complex type that contains trusted signers for this cache behavior.
           If ``Quantity`` is ``0`` , you can omit ``Items`` .

          - *(string) --*

      - **PriceClass** *(string) --*

        A complex type that contains information about price class for this streaming
        distribution.

      - **Enabled** *(boolean) --*

        Whether the streaming distribution is enabled to accept user requests for content.
    """


_ClientCreateStreamingDistributionWithTagsResponseTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionWithTagsResponseTypeDef",
    {
        "StreamingDistribution": ClientCreateStreamingDistributionWithTagsResponseStreamingDistributionTypeDef,
        "Location": str,
        "ETag": str,
    },
    total=False,
)


class ClientCreateStreamingDistributionWithTagsResponseTypeDef(
    _ClientCreateStreamingDistributionWithTagsResponseTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionWithTags` `Response`

    The returned result of the corresponding request.

    - **StreamingDistribution** *(dict) --*

      The streaming distribution's information.

      - **Id** *(string) --*

        The identifier for the RTMP distribution. For example: ``EGTXBD79EXAMPLE`` .

      - **ARN** *(string) --*

        The ARN (Amazon Resource Name) for the distribution. For example:
        ``arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`` , where ``123456789012``
        is your AWS account ID.

      - **Status** *(string) --*

        The current status of the RTMP distribution. When the status is ``Deployed`` , the
        distribution's information is propagated to all CloudFront edge locations.

      - **LastModifiedTime** *(datetime) --*

        The date and time that the distribution was last modified.

      - **DomainName** *(string) --*

        The domain name that corresponds to the streaming distribution, for example,
        ``s5c39gqb8ow64r.cloudfront.net`` .

      - **ActiveTrustedSigners** *(dict) --*

        A complex type that lists the AWS accounts, if any, that you included in the
        ``TrustedSigners`` complex type for this distribution. These are the accounts that you want
        to allow to create signed URLs for private content.

        The ``Signer`` complex type lists the AWS account number of the trusted signer or ``self``
        if the signer is the AWS account that created the distribution. The ``Signer`` element also
        includes the IDs of any active CloudFront key pairs that are associated with the trusted
        signer's AWS account. If no ``KeyPairId`` element appears for a ``Signer`` , that signer
        can't create signed URLs.

        For more information, see `Serving Private Content through CloudFront
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
        in the *Amazon CloudFront Developer Guide* .

        - **Enabled** *(boolean) --*

          Enabled is ``true`` if any of the AWS accounts listed in the ``TrustedSigners`` complex
          type for this distribution have active CloudFront key pairs. If not, ``Enabled`` is
          ``false`` .

        - **Quantity** *(integer) --*

          The number of trusted signers specified in the ``TrustedSigners`` complex type.

        - **Items** *(list) --*

          A complex type that contains one ``Signer`` complex type for each trusted signer that is
          specified in the ``TrustedSigners`` complex type.

          - *(dict) --*

            A complex type that lists the AWS accounts that were included in the ``TrustedSigners``
            complex type, as well as their active CloudFront key pair IDs, if any.

            - **AwsAccountNumber** *(string) --*

              An AWS account that is included in the ``TrustedSigners`` complex type for this
              distribution. Valid values include:

              * ``self`` , which is the AWS account used to create the distribution.

              * An AWS account number.

            - **KeyPairIds** *(dict) --*

              A complex type that lists the active CloudFront key pairs, if any, that are
              associated with ``AwsAccountNumber`` .

              - **Quantity** *(integer) --*

                The number of active CloudFront key pairs for ``AwsAccountNumber`` .

                For more information, see `ActiveTrustedSigners
                <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
                .

              - **Items** *(list) --*

                A complex type that lists the active CloudFront key pairs, if any, that are
                associated with ``AwsAccountNumber`` .

                For more information, see `ActiveTrustedSigners
                <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
                .

                - *(string) --*

      - **StreamingDistributionConfig** *(dict) --*

        The current configuration information for the RTMP distribution.

        - **CallerReference** *(string) --*

          A unique value (for example, a date-time stamp) that ensures that the request can't be
          replayed.

          If the value of ``CallerReference`` is new (regardless of the content of the
          ``StreamingDistributionConfig`` object), CloudFront creates a new distribution.

          If ``CallerReference`` is a value that you already sent in a previous request to create a
          distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

        - **S3Origin** *(dict) --*

          A complex type that contains information about the Amazon S3 bucket from which you want
          CloudFront to get your media files for distribution.

          - **DomainName** *(string) --*

            The DNS name of the Amazon S3 origin.

          - **OriginAccessIdentity** *(string) --*

            The CloudFront origin access identity to associate with the distribution. Use an origin
            access identity to configure the distribution so that end users can only access objects
            in an Amazon S3 bucket through CloudFront.

            If you want end users to be able to access objects using either the CloudFront URL or
            the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

            To delete the origin access identity from an existing distribution, update the
            distribution configuration and include an empty ``OriginAccessIdentity`` element.

            To replace the origin access identity, update the distribution configuration and
            specify the new origin access identity.

            For more information, see `Using an Origin Access Identity to Restrict Access to Your
            Amazon S3 Content
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
            in the *Amazon CloudFront Developer Guide* .

        - **Aliases** *(dict) --*

          A complex type that contains information about CNAMEs (alternate domain names), if any,
          for this streaming distribution.

          - **Quantity** *(integer) --*

            The number of CNAME aliases, if any, that you want to associate with this distribution.

          - **Items** *(list) --*

            A complex type that contains the CNAME aliases, if any, that you want to associate with
            this distribution.

            - *(string) --*

        - **Comment** *(string) --*

          Any comments you want to include about the streaming distribution.

        - **Logging** *(dict) --*

          A complex type that controls whether access logs are written for the streaming
          distribution.

          - **Enabled** *(boolean) --*

            Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If
            you don't want to enable logging when you create a streaming distribution or if you
            want to disable logging for an existing streaming distribution, specify ``false`` for
            ``Enabled`` , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify
            ``false`` for ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the
            values are automatically deleted.

          - **Bucket** *(string) --*

            The Amazon S3 bucket to store the access logs in, for example,
            ``myawslogbucket.s3.amazonaws.com`` .

          - **Prefix** *(string) --*

            An optional string that you want CloudFront to prefix to the access log filenames for
            this streaming distribution, for example, ``myprefix/`` . If you want to enable
            logging, but you don't want to specify a prefix, you still must include an empty
            ``Prefix`` element in the ``Logging`` element.

        - **TrustedSigners** *(dict) --*

          A complex type that specifies any AWS accounts that you want to permit to create signed
          URLs for private content. If you want the distribution to use signed URLs, include this
          element; if you want the distribution to use public URLs, remove this element. For more
          information, see `Serving Private Content through CloudFront
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
          in the *Amazon CloudFront Developer Guide* .

          - **Enabled** *(boolean) --*

            Specifies whether you want to require viewers to use signed URLs to access the files
            specified by ``PathPattern`` and ``TargetOriginId`` .

          - **Quantity** *(integer) --*

            The number of trusted signers for this cache behavior.

          - **Items** *(list) --*

             **Optional** : A complex type that contains trusted signers for this cache behavior.
             If ``Quantity`` is ``0`` , you can omit ``Items`` .

            - *(string) --*

        - **PriceClass** *(string) --*

          A complex type that contains information about price class for this streaming
          distribution.

        - **Enabled** *(boolean) --*

          Whether the streaming distribution is enabled to accept user requests for content.

    - **Location** *(string) --*

      The fully qualified URI of the new streaming distribution resource just created. For
      example:``https://cloudfront.amazonaws.com/2010-11-01/streaming-distribution/EGTXBD79H29TRA8``
      .

    - **ETag** *(string) --*

      The current version of the distribution created.
    """


_RequiredClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigAliasesTypeDef = TypedDict(
    "_RequiredClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigAliasesTypeDef",
    {"Quantity": int},
)
_OptionalClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigAliasesTypeDef = TypedDict(
    "_OptionalClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigAliasesTypeDef",
    {"Items": List[str]},
    total=False,
)


class ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigAliasesTypeDef(
    _RequiredClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigAliasesTypeDef,
    _OptionalClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigAliasesTypeDef,
):
    """
    Type definition for `ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfig` `Aliases`

    A complex type that contains information about CNAMEs (alternate domain names), if any, for
    this streaming distribution.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of CNAME aliases, if any, that you want to associate with this distribution.

    - **Items** *(list) --*

      A complex type that contains the CNAME aliases, if any, that you want to associate with
      this distribution.

      - *(string) --*
    """


_ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigLoggingTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigLoggingTypeDef",
    {"Enabled": bool, "Bucket": str, "Prefix": str},
)


class ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigLoggingTypeDef(
    _ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigLoggingTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfig` `Logging`

    A complex type that controls whether access logs are written for the streaming distribution.

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you
      don't want to enable logging when you create a streaming distribution or if you want to
      disable logging for an existing streaming distribution, specify ``false`` for ``Enabled`` ,
      and specify ``empty Bucket`` and ``Prefix`` elements. If you specify ``false`` for
      ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the values are
      automatically deleted.

    - **Bucket** *(string) --* **[REQUIRED]**

      The Amazon S3 bucket to store the access logs in, for example,
      ``myawslogbucket.s3.amazonaws.com`` .

    - **Prefix** *(string) --* **[REQUIRED]**

      An optional string that you want CloudFront to prefix to the access log filenames for this
      streaming distribution, for example, ``myprefix/`` . If you want to enable logging, but you
      don't want to specify a prefix, you still must include an empty ``Prefix`` element in the
      ``Logging`` element.
    """


_ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigS3OriginTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigS3OriginTypeDef",
    {"DomainName": str, "OriginAccessIdentity": str},
)


class ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigS3OriginTypeDef(
    _ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigS3OriginTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfig` `S3Origin`

    A complex type that contains information about the Amazon S3 bucket from which you want
    CloudFront to get your media files for distribution.

    - **DomainName** *(string) --* **[REQUIRED]**

      The DNS name of the Amazon S3 origin.

    - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

      The CloudFront origin access identity to associate with the distribution. Use an origin
      access identity to configure the distribution so that end users can only access objects in
      an Amazon S3 bucket through CloudFront.

      If you want end users to be able to access objects using either the CloudFront URL or the
      Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

      To delete the origin access identity from an existing distribution, update the distribution
      configuration and include an empty ``OriginAccessIdentity`` element.

      To replace the origin access identity, update the distribution configuration and specify
      the new origin access identity.

      For more information, see `Using an Origin Access Identity to Restrict Access to Your
      Amazon S3 Content
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
      in the *Amazon CloudFront Developer Guide* .
    """


_RequiredClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigTrustedSignersTypeDef = TypedDict(
    "_RequiredClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigTrustedSignersTypeDef",
    {"Enabled": bool, "Quantity": int},
)
_OptionalClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigTrustedSignersTypeDef = TypedDict(
    "_OptionalClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigTrustedSignersTypeDef",
    {"Items": List[str]},
    total=False,
)


class ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigTrustedSignersTypeDef(
    _RequiredClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigTrustedSignersTypeDef,
    _OptionalClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigTrustedSignersTypeDef,
):
    """
    Type definition for `ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfig` `TrustedSigners`

    A complex type that specifies any AWS accounts that you want to permit to create signed URLs
    for private content. If you want the distribution to use signed URLs, include this element;
    if you want the distribution to use public URLs, remove this element. For more information,
    see `Serving Private Content through CloudFront
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
    in the *Amazon CloudFront Developer Guide* .

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Specifies whether you want to require viewers to use signed URLs to access the files
      specified by ``PathPattern`` and ``TargetOriginId`` .

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of trusted signers for this cache behavior.

    - **Items** *(list) --*

       **Optional** : A complex type that contains trusted signers for this cache behavior. If
       ``Quantity`` is ``0`` , you can omit ``Items`` .

      - *(string) --*
    """


_RequiredClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigTypeDef = TypedDict(
    "_RequiredClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "S3Origin": ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigS3OriginTypeDef,
        "Comment": str,
        "TrustedSigners": ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigTrustedSignersTypeDef,
        "Enabled": bool,
    },
)
_OptionalClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigTypeDef = TypedDict(
    "_OptionalClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigTypeDef",
    {
        "Aliases": ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigAliasesTypeDef,
        "Logging": ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigLoggingTypeDef,
        "PriceClass": str,
    },
    total=False,
)


class ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigTypeDef(
    _RequiredClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigTypeDef,
    _OptionalClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigTypeDef,
):
    """
    Type definition for `ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTags` `StreamingDistributionConfig`

    A streaming distribution Configuration.

    - **CallerReference** *(string) --* **[REQUIRED]**

      A unique value (for example, a date-time stamp) that ensures that the request can't be
      replayed.

      If the value of ``CallerReference`` is new (regardless of the content of the
      ``StreamingDistributionConfig`` object), CloudFront creates a new distribution.

      If ``CallerReference`` is a value that you already sent in a previous request to create a
      distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

    - **S3Origin** *(dict) --* **[REQUIRED]**

      A complex type that contains information about the Amazon S3 bucket from which you want
      CloudFront to get your media files for distribution.

      - **DomainName** *(string) --* **[REQUIRED]**

        The DNS name of the Amazon S3 origin.

      - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

        The CloudFront origin access identity to associate with the distribution. Use an origin
        access identity to configure the distribution so that end users can only access objects in
        an Amazon S3 bucket through CloudFront.

        If you want end users to be able to access objects using either the CloudFront URL or the
        Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

        To delete the origin access identity from an existing distribution, update the distribution
        configuration and include an empty ``OriginAccessIdentity`` element.

        To replace the origin access identity, update the distribution configuration and specify
        the new origin access identity.

        For more information, see `Using an Origin Access Identity to Restrict Access to Your
        Amazon S3 Content
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
        in the *Amazon CloudFront Developer Guide* .

    - **Aliases** *(dict) --*

      A complex type that contains information about CNAMEs (alternate domain names), if any, for
      this streaming distribution.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of CNAME aliases, if any, that you want to associate with this distribution.

      - **Items** *(list) --*

        A complex type that contains the CNAME aliases, if any, that you want to associate with
        this distribution.

        - *(string) --*

    - **Comment** *(string) --* **[REQUIRED]**

      Any comments you want to include about the streaming distribution.

    - **Logging** *(dict) --*

      A complex type that controls whether access logs are written for the streaming distribution.

      - **Enabled** *(boolean) --* **[REQUIRED]**

        Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you
        don't want to enable logging when you create a streaming distribution or if you want to
        disable logging for an existing streaming distribution, specify ``false`` for ``Enabled`` ,
        and specify ``empty Bucket`` and ``Prefix`` elements. If you specify ``false`` for
        ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the values are
        automatically deleted.

      - **Bucket** *(string) --* **[REQUIRED]**

        The Amazon S3 bucket to store the access logs in, for example,
        ``myawslogbucket.s3.amazonaws.com`` .

      - **Prefix** *(string) --* **[REQUIRED]**

        An optional string that you want CloudFront to prefix to the access log filenames for this
        streaming distribution, for example, ``myprefix/`` . If you want to enable logging, but you
        don't want to specify a prefix, you still must include an empty ``Prefix`` element in the
        ``Logging`` element.

    - **TrustedSigners** *(dict) --* **[REQUIRED]**

      A complex type that specifies any AWS accounts that you want to permit to create signed URLs
      for private content. If you want the distribution to use signed URLs, include this element;
      if you want the distribution to use public URLs, remove this element. For more information,
      see `Serving Private Content through CloudFront
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
      in the *Amazon CloudFront Developer Guide* .

      - **Enabled** *(boolean) --* **[REQUIRED]**

        Specifies whether you want to require viewers to use signed URLs to access the files
        specified by ``PathPattern`` and ``TargetOriginId`` .

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of trusted signers for this cache behavior.

      - **Items** *(list) --*

         **Optional** : A complex type that contains trusted signers for this cache behavior. If
         ``Quantity`` is ``0`` , you can omit ``Items`` .

        - *(string) --*

    - **PriceClass** *(string) --*

      A complex type that contains information about price class for this streaming distribution.

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Whether the streaming distribution is enabled to accept user requests for content.
    """


_RequiredClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTagsItemsTypeDef = TypedDict(
    "_RequiredClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTagsItemsTypeDef",
    {"Key": str},
)
_OptionalClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTagsItemsTypeDef = TypedDict(
    "_OptionalClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTagsItemsTypeDef",
    {"Value": str},
    total=False,
)


class ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTagsItemsTypeDef(
    _RequiredClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTagsItemsTypeDef,
    _OptionalClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTagsItemsTypeDef,
):
    """
    Type definition for `ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTags` `Items`

    A complex type that contains ``Tag`` key and ``Tag`` value.

    - **Key** *(string) --* **[REQUIRED]**

      A string that contains ``Tag`` key.

      The string length should be between 1 and 128 characters. Valid characters include
      ``a-z`` , ``A-Z`` , ``0-9`` , space, and the special characters ``_ - . : / = + @`` .

    - **Value** *(string) --*

      A string that contains an optional ``Tag`` value.

      The string length should be between 0 and 256 characters. Valid characters include
      ``a-z`` , ``A-Z`` , ``0-9`` , space, and the special characters ``_ - . : / = + @`` .
    """


_ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTagsTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTagsTypeDef",
    {
        "Items": List[
            ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTagsItemsTypeDef
        ]
    },
    total=False,
)


class ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTagsTypeDef(
    _ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTagsTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTags` `Tags`

    A complex type that contains zero or more ``Tag`` elements.

    - **Items** *(list) --*

      A complex type that contains ``Tag`` elements.

      - *(dict) --*

        A complex type that contains ``Tag`` key and ``Tag`` value.

        - **Key** *(string) --* **[REQUIRED]**

          A string that contains ``Tag`` key.

          The string length should be between 1 and 128 characters. Valid characters include
          ``a-z`` , ``A-Z`` , ``0-9`` , space, and the special characters ``_ - . : / = + @`` .

        - **Value** *(string) --*

          A string that contains an optional ``Tag`` value.

          The string length should be between 0 and 256 characters. Valid characters include
          ``a-z`` , ``A-Z`` , ``0-9`` , space, and the special characters ``_ - . : / = + @`` .
    """


_ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTypeDef = TypedDict(
    "_ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTypeDef",
    {
        "StreamingDistributionConfig": ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsStreamingDistributionConfigTypeDef,
        "Tags": ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTagsTypeDef,
    },
)


class ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTypeDef(
    _ClientCreateStreamingDistributionWithTagsStreamingDistributionConfigWithTagsTypeDef
):
    """
    Type definition for `ClientCreateStreamingDistributionWithTags` `StreamingDistributionConfigWithTags`

    The streaming distribution's configuration information.

    - **StreamingDistributionConfig** *(dict) --* **[REQUIRED]**

      A streaming distribution Configuration.

      - **CallerReference** *(string) --* **[REQUIRED]**

        A unique value (for example, a date-time stamp) that ensures that the request can't be
        replayed.

        If the value of ``CallerReference`` is new (regardless of the content of the
        ``StreamingDistributionConfig`` object), CloudFront creates a new distribution.

        If ``CallerReference`` is a value that you already sent in a previous request to create a
        distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

      - **S3Origin** *(dict) --* **[REQUIRED]**

        A complex type that contains information about the Amazon S3 bucket from which you want
        CloudFront to get your media files for distribution.

        - **DomainName** *(string) --* **[REQUIRED]**

          The DNS name of the Amazon S3 origin.

        - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

          The CloudFront origin access identity to associate with the distribution. Use an origin
          access identity to configure the distribution so that end users can only access objects in
          an Amazon S3 bucket through CloudFront.

          If you want end users to be able to access objects using either the CloudFront URL or the
          Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

          To delete the origin access identity from an existing distribution, update the distribution
          configuration and include an empty ``OriginAccessIdentity`` element.

          To replace the origin access identity, update the distribution configuration and specify
          the new origin access identity.

          For more information, see `Using an Origin Access Identity to Restrict Access to Your
          Amazon S3 Content
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
          in the *Amazon CloudFront Developer Guide* .

      - **Aliases** *(dict) --*

        A complex type that contains information about CNAMEs (alternate domain names), if any, for
        this streaming distribution.

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of CNAME aliases, if any, that you want to associate with this distribution.

        - **Items** *(list) --*

          A complex type that contains the CNAME aliases, if any, that you want to associate with
          this distribution.

          - *(string) --*

      - **Comment** *(string) --* **[REQUIRED]**

        Any comments you want to include about the streaming distribution.

      - **Logging** *(dict) --*

        A complex type that controls whether access logs are written for the streaming distribution.

        - **Enabled** *(boolean) --* **[REQUIRED]**

          Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you
          don't want to enable logging when you create a streaming distribution or if you want to
          disable logging for an existing streaming distribution, specify ``false`` for ``Enabled`` ,
          and specify ``empty Bucket`` and ``Prefix`` elements. If you specify ``false`` for
          ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the values are
          automatically deleted.

        - **Bucket** *(string) --* **[REQUIRED]**

          The Amazon S3 bucket to store the access logs in, for example,
          ``myawslogbucket.s3.amazonaws.com`` .

        - **Prefix** *(string) --* **[REQUIRED]**

          An optional string that you want CloudFront to prefix to the access log filenames for this
          streaming distribution, for example, ``myprefix/`` . If you want to enable logging, but you
          don't want to specify a prefix, you still must include an empty ``Prefix`` element in the
          ``Logging`` element.

      - **TrustedSigners** *(dict) --* **[REQUIRED]**

        A complex type that specifies any AWS accounts that you want to permit to create signed URLs
        for private content. If you want the distribution to use signed URLs, include this element;
        if you want the distribution to use public URLs, remove this element. For more information,
        see `Serving Private Content through CloudFront
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
        in the *Amazon CloudFront Developer Guide* .

        - **Enabled** *(boolean) --* **[REQUIRED]**

          Specifies whether you want to require viewers to use signed URLs to access the files
          specified by ``PathPattern`` and ``TargetOriginId`` .

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of trusted signers for this cache behavior.

        - **Items** *(list) --*

           **Optional** : A complex type that contains trusted signers for this cache behavior. If
           ``Quantity`` is ``0`` , you can omit ``Items`` .

          - *(string) --*

      - **PriceClass** *(string) --*

        A complex type that contains information about price class for this streaming distribution.

      - **Enabled** *(boolean) --* **[REQUIRED]**

        Whether the streaming distribution is enabled to accept user requests for content.

    - **Tags** *(dict) --* **[REQUIRED]**

      A complex type that contains zero or more ``Tag`` elements.

      - **Items** *(list) --*

        A complex type that contains ``Tag`` elements.

        - *(dict) --*

          A complex type that contains ``Tag`` key and ``Tag`` value.

          - **Key** *(string) --* **[REQUIRED]**

            A string that contains ``Tag`` key.

            The string length should be between 1 and 128 characters. Valid characters include
            ``a-z`` , ``A-Z`` , ``0-9`` , space, and the special characters ``_ - . : / = + @`` .

          - **Value** *(string) --*

            A string that contains an optional ``Tag`` value.

            The string length should be between 0 and 256 characters. Valid characters include
            ``a-z`` , ``A-Z`` , ``0-9`` , space, and the special characters ``_ - . : / = + @`` .
    """


_ClientGetCloudFrontOriginAccessIdentityConfigResponseCloudFrontOriginAccessIdentityConfigTypeDef = TypedDict(
    "_ClientGetCloudFrontOriginAccessIdentityConfigResponseCloudFrontOriginAccessIdentityConfigTypeDef",
    {"CallerReference": str, "Comment": str},
    total=False,
)


class ClientGetCloudFrontOriginAccessIdentityConfigResponseCloudFrontOriginAccessIdentityConfigTypeDef(
    _ClientGetCloudFrontOriginAccessIdentityConfigResponseCloudFrontOriginAccessIdentityConfigTypeDef
):
    """
    Type definition for `ClientGetCloudFrontOriginAccessIdentityConfigResponse` `CloudFrontOriginAccessIdentityConfig`

    The origin access identity's configuration information.

    - **CallerReference** *(string) --*

      A unique value (for example, a date-time stamp) that ensures that the request can't be
      replayed.

      If the value of ``CallerReference`` is new (regardless of the content of the
      ``CloudFrontOriginAccessIdentityConfig`` object), a new origin access identity is created.

      If the ``CallerReference`` is a value already sent in a previous identity request, and the
      content of the ``CloudFrontOriginAccessIdentityConfig`` is identical to the original
      request (ignoring white space), the response includes the same information returned to the
      original request.

      If the ``CallerReference`` is a value you already sent in a previous request to create an
      identity, but the content of the ``CloudFrontOriginAccessIdentityConfig`` is different from
      the original request, CloudFront returns a ``CloudFrontOriginAccessIdentityAlreadyExists``
      error.

    - **Comment** *(string) --*

      Any comments you want to include about the origin access identity.
    """


_ClientGetCloudFrontOriginAccessIdentityConfigResponseTypeDef = TypedDict(
    "_ClientGetCloudFrontOriginAccessIdentityConfigResponseTypeDef",
    {
        "CloudFrontOriginAccessIdentityConfig": ClientGetCloudFrontOriginAccessIdentityConfigResponseCloudFrontOriginAccessIdentityConfigTypeDef,
        "ETag": str,
    },
    total=False,
)


class ClientGetCloudFrontOriginAccessIdentityConfigResponseTypeDef(
    _ClientGetCloudFrontOriginAccessIdentityConfigResponseTypeDef
):
    """
    Type definition for `ClientGetCloudFrontOriginAccessIdentityConfig` `Response`

    The returned result of the corresponding request.

    - **CloudFrontOriginAccessIdentityConfig** *(dict) --*

      The origin access identity's configuration information.

      - **CallerReference** *(string) --*

        A unique value (for example, a date-time stamp) that ensures that the request can't be
        replayed.

        If the value of ``CallerReference`` is new (regardless of the content of the
        ``CloudFrontOriginAccessIdentityConfig`` object), a new origin access identity is created.

        If the ``CallerReference`` is a value already sent in a previous identity request, and the
        content of the ``CloudFrontOriginAccessIdentityConfig`` is identical to the original
        request (ignoring white space), the response includes the same information returned to the
        original request.

        If the ``CallerReference`` is a value you already sent in a previous request to create an
        identity, but the content of the ``CloudFrontOriginAccessIdentityConfig`` is different from
        the original request, CloudFront returns a ``CloudFrontOriginAccessIdentityAlreadyExists``
        error.

      - **Comment** *(string) --*

        Any comments you want to include about the origin access identity.

    - **ETag** *(string) --*

      The current version of the configuration. For example: ``E2QWRUHAPOMQZL`` .
    """


_ClientGetCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef = TypedDict(
    "_ClientGetCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef",
    {"CallerReference": str, "Comment": str},
    total=False,
)


class ClientGetCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef(
    _ClientGetCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef
):
    """
    Type definition for `ClientGetCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentity` `CloudFrontOriginAccessIdentityConfig`

    The current configuration information for the identity.

    - **CallerReference** *(string) --*

      A unique value (for example, a date-time stamp) that ensures that the request can't be
      replayed.

      If the value of ``CallerReference`` is new (regardless of the content of the
      ``CloudFrontOriginAccessIdentityConfig`` object), a new origin access identity is created.

      If the ``CallerReference`` is a value already sent in a previous identity request, and
      the content of the ``CloudFrontOriginAccessIdentityConfig`` is identical to the original
      request (ignoring white space), the response includes the same information returned to
      the original request.

      If the ``CallerReference`` is a value you already sent in a previous request to create an
      identity, but the content of the ``CloudFrontOriginAccessIdentityConfig`` is different
      from the original request, CloudFront returns a
      ``CloudFrontOriginAccessIdentityAlreadyExists`` error.

    - **Comment** *(string) --*

      Any comments you want to include about the origin access identity.
    """


_ClientGetCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityTypeDef = TypedDict(
    "_ClientGetCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityTypeDef",
    {
        "Id": str,
        "S3CanonicalUserId": str,
        "CloudFrontOriginAccessIdentityConfig": ClientGetCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef,
    },
    total=False,
)


class ClientGetCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityTypeDef(
    _ClientGetCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityTypeDef
):
    """
    Type definition for `ClientGetCloudFrontOriginAccessIdentityResponse` `CloudFrontOriginAccessIdentity`

    The origin access identity's information.

    - **Id** *(string) --*

      The ID for the origin access identity, for example, ``E74FTE3AJFJ256A`` .

    - **S3CanonicalUserId** *(string) --*

      The Amazon S3 canonical user ID for the origin access identity, used when giving the origin
      access identity read permission to an object in Amazon S3.

    - **CloudFrontOriginAccessIdentityConfig** *(dict) --*

      The current configuration information for the identity.

      - **CallerReference** *(string) --*

        A unique value (for example, a date-time stamp) that ensures that the request can't be
        replayed.

        If the value of ``CallerReference`` is new (regardless of the content of the
        ``CloudFrontOriginAccessIdentityConfig`` object), a new origin access identity is created.

        If the ``CallerReference`` is a value already sent in a previous identity request, and
        the content of the ``CloudFrontOriginAccessIdentityConfig`` is identical to the original
        request (ignoring white space), the response includes the same information returned to
        the original request.

        If the ``CallerReference`` is a value you already sent in a previous request to create an
        identity, but the content of the ``CloudFrontOriginAccessIdentityConfig`` is different
        from the original request, CloudFront returns a
        ``CloudFrontOriginAccessIdentityAlreadyExists`` error.

      - **Comment** *(string) --*

        Any comments you want to include about the origin access identity.
    """


_ClientGetCloudFrontOriginAccessIdentityResponseTypeDef = TypedDict(
    "_ClientGetCloudFrontOriginAccessIdentityResponseTypeDef",
    {
        "CloudFrontOriginAccessIdentity": ClientGetCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityTypeDef,
        "ETag": str,
    },
    total=False,
)


class ClientGetCloudFrontOriginAccessIdentityResponseTypeDef(
    _ClientGetCloudFrontOriginAccessIdentityResponseTypeDef
):
    """
    Type definition for `ClientGetCloudFrontOriginAccessIdentity` `Response`

    The returned result of the corresponding request.

    - **CloudFrontOriginAccessIdentity** *(dict) --*

      The origin access identity's information.

      - **Id** *(string) --*

        The ID for the origin access identity, for example, ``E74FTE3AJFJ256A`` .

      - **S3CanonicalUserId** *(string) --*

        The Amazon S3 canonical user ID for the origin access identity, used when giving the origin
        access identity read permission to an object in Amazon S3.

      - **CloudFrontOriginAccessIdentityConfig** *(dict) --*

        The current configuration information for the identity.

        - **CallerReference** *(string) --*

          A unique value (for example, a date-time stamp) that ensures that the request can't be
          replayed.

          If the value of ``CallerReference`` is new (regardless of the content of the
          ``CloudFrontOriginAccessIdentityConfig`` object), a new origin access identity is created.

          If the ``CallerReference`` is a value already sent in a previous identity request, and
          the content of the ``CloudFrontOriginAccessIdentityConfig`` is identical to the original
          request (ignoring white space), the response includes the same information returned to
          the original request.

          If the ``CallerReference`` is a value you already sent in a previous request to create an
          identity, but the content of the ``CloudFrontOriginAccessIdentityConfig`` is different
          from the original request, CloudFront returns a
          ``CloudFrontOriginAccessIdentityAlreadyExists`` error.

        - **Comment** *(string) --*

          Any comments you want to include about the origin access identity.

    - **ETag** *(string) --*

      The current version of the origin access identity's information. For example:
      ``E2QWRUHAPOMQZL`` .
    """


_ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef",
    {"Format": str, "ProfileId": str, "ContentType": str},
    total=False,
)


class ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef(
    _ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles` `Items`

    A field-level encryption content type profile.

    - **Format** *(string) --*

      The format for a field-level encryption content type-profile mapping.

    - **ProfileId** *(string) --*

      The profile ID for a field-level encryption content type-profile mapping.

    - **ContentType** *(string) --*

      The content type for a field-level encryption content type-profile mapping.
    """


_ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef
        ],
    },
    total=False,
)


class ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef(
    _ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfig` `ContentTypeProfiles`

    The configuration for a field-level encryption content type-profile.

    - **Quantity** *(integer) --*

      The number of field-level encryption content type-profile mappings.

    - **Items** *(list) --*

      Items in a field-level encryption content type-profile mapping.

      - *(dict) --*

        A field-level encryption content type profile.

        - **Format** *(string) --*

          The format for a field-level encryption content type-profile mapping.

        - **ProfileId** *(string) --*

          The profile ID for a field-level encryption content type-profile mapping.

        - **ContentType** *(string) --*

          The content type for a field-level encryption content type-profile mapping.
    """


_ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef",
    {
        "ForwardWhenContentTypeIsUnknown": bool,
        "ContentTypeProfiles": ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef,
    },
    total=False,
)


class ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef(
    _ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfig` `ContentTypeProfileConfig`

    A complex data type that specifies when to forward content if a content type isn't
    recognized and profiles to use as by default in a request if a query argument doesn't
    specify a profile to use.

    - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

      The setting in a field-level encryption content type-profile mapping that specifies what
      to do when an unknown content type is provided for the profile. If true, content is
      forwarded without being encrypted when the content type is unknown. If false (the
      default), an error is returned when the content type is unknown.

    - **ContentTypeProfiles** *(dict) --*

      The configuration for a field-level encryption content type-profile.

      - **Quantity** *(integer) --*

        The number of field-level encryption content type-profile mappings.

      - **Items** *(list) --*

        Items in a field-level encryption content type-profile mapping.

        - *(dict) --*

          A field-level encryption content type profile.

          - **Format** *(string) --*

            The format for a field-level encryption content type-profile mapping.

          - **ProfileId** *(string) --*

            The profile ID for a field-level encryption content type-profile mapping.

          - **ContentType** *(string) --*

            The content type for a field-level encryption content type-profile mapping.
    """


_ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef",
    {"QueryArg": str, "ProfileId": str},
    total=False,
)


class ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef(
    _ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles` `Items`

    Query argument-profile mapping for field-level encryption.

    - **QueryArg** *(string) --*

      Query argument for field-level encryption query argument-profile mapping.

    - **ProfileId** *(string) --*

      ID of profile to use for field-level encryption query argument-profile mapping
    """


_ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef
        ],
    },
    total=False,
)


class ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef(
    _ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfig` `QueryArgProfiles`

    Profiles specified for query argument-profile mapping for field-level encryption.

    - **Quantity** *(integer) --*

      Number of profiles for query argument-profile mapping for field-level encryption.

    - **Items** *(list) --*

      Number of items for query argument-profile mapping for field-level encryption.

      - *(dict) --*

        Query argument-profile mapping for field-level encryption.

        - **QueryArg** *(string) --*

          Query argument for field-level encryption query argument-profile mapping.

        - **ProfileId** *(string) --*

          ID of profile to use for field-level encryption query argument-profile mapping
    """


_ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef",
    {
        "ForwardWhenQueryArgProfileIsUnknown": bool,
        "QueryArgProfiles": ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef,
    },
    total=False,
)


class ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef(
    _ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfig` `QueryArgProfileConfig`

    A complex data type that specifies when to forward content if a profile isn't found and the
    profile that can be provided as a query argument in a request.

    - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

      Flag to set if you want a request to be forwarded to the origin even if the profile
      specified by the field-level encryption query argument, fle-profile, is unknown.

    - **QueryArgProfiles** *(dict) --*

      Profiles specified for query argument-profile mapping for field-level encryption.

      - **Quantity** *(integer) --*

        Number of profiles for query argument-profile mapping for field-level encryption.

      - **Items** *(list) --*

        Number of items for query argument-profile mapping for field-level encryption.

        - *(dict) --*

          Query argument-profile mapping for field-level encryption.

          - **QueryArg** *(string) --*

            Query argument for field-level encryption query argument-profile mapping.

          - **ProfileId** *(string) --*

            ID of profile to use for field-level encryption query argument-profile mapping
    """


_ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigTypeDef",
    {
        "CallerReference": str,
        "Comment": str,
        "QueryArgProfileConfig": ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef,
        "ContentTypeProfileConfig": ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef,
    },
    total=False,
)


class ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigTypeDef(
    _ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionConfigResponse` `FieldLevelEncryptionConfig`

    Return the field-level encryption configuration information.

    - **CallerReference** *(string) --*

      A unique number that ensures the request can't be replayed.

    - **Comment** *(string) --*

      An optional comment about the configuration.

    - **QueryArgProfileConfig** *(dict) --*

      A complex data type that specifies when to forward content if a profile isn't found and the
      profile that can be provided as a query argument in a request.

      - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

        Flag to set if you want a request to be forwarded to the origin even if the profile
        specified by the field-level encryption query argument, fle-profile, is unknown.

      - **QueryArgProfiles** *(dict) --*

        Profiles specified for query argument-profile mapping for field-level encryption.

        - **Quantity** *(integer) --*

          Number of profiles for query argument-profile mapping for field-level encryption.

        - **Items** *(list) --*

          Number of items for query argument-profile mapping for field-level encryption.

          - *(dict) --*

            Query argument-profile mapping for field-level encryption.

            - **QueryArg** *(string) --*

              Query argument for field-level encryption query argument-profile mapping.

            - **ProfileId** *(string) --*

              ID of profile to use for field-level encryption query argument-profile mapping

    - **ContentTypeProfileConfig** *(dict) --*

      A complex data type that specifies when to forward content if a content type isn't
      recognized and profiles to use as by default in a request if a query argument doesn't
      specify a profile to use.

      - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

        The setting in a field-level encryption content type-profile mapping that specifies what
        to do when an unknown content type is provided for the profile. If true, content is
        forwarded without being encrypted when the content type is unknown. If false (the
        default), an error is returned when the content type is unknown.

      - **ContentTypeProfiles** *(dict) --*

        The configuration for a field-level encryption content type-profile.

        - **Quantity** *(integer) --*

          The number of field-level encryption content type-profile mappings.

        - **Items** *(list) --*

          Items in a field-level encryption content type-profile mapping.

          - *(dict) --*

            A field-level encryption content type profile.

            - **Format** *(string) --*

              The format for a field-level encryption content type-profile mapping.

            - **ProfileId** *(string) --*

              The profile ID for a field-level encryption content type-profile mapping.

            - **ContentType** *(string) --*

              The content type for a field-level encryption content type-profile mapping.
    """


_ClientGetFieldLevelEncryptionConfigResponseTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionConfigResponseTypeDef",
    {
        "FieldLevelEncryptionConfig": ClientGetFieldLevelEncryptionConfigResponseFieldLevelEncryptionConfigTypeDef,
        "ETag": str,
    },
    total=False,
)


class ClientGetFieldLevelEncryptionConfigResponseTypeDef(
    _ClientGetFieldLevelEncryptionConfigResponseTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionConfig` `Response`

    - **FieldLevelEncryptionConfig** *(dict) --*

      Return the field-level encryption configuration information.

      - **CallerReference** *(string) --*

        A unique number that ensures the request can't be replayed.

      - **Comment** *(string) --*

        An optional comment about the configuration.

      - **QueryArgProfileConfig** *(dict) --*

        A complex data type that specifies when to forward content if a profile isn't found and the
        profile that can be provided as a query argument in a request.

        - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

          Flag to set if you want a request to be forwarded to the origin even if the profile
          specified by the field-level encryption query argument, fle-profile, is unknown.

        - **QueryArgProfiles** *(dict) --*

          Profiles specified for query argument-profile mapping for field-level encryption.

          - **Quantity** *(integer) --*

            Number of profiles for query argument-profile mapping for field-level encryption.

          - **Items** *(list) --*

            Number of items for query argument-profile mapping for field-level encryption.

            - *(dict) --*

              Query argument-profile mapping for field-level encryption.

              - **QueryArg** *(string) --*

                Query argument for field-level encryption query argument-profile mapping.

              - **ProfileId** *(string) --*

                ID of profile to use for field-level encryption query argument-profile mapping

      - **ContentTypeProfileConfig** *(dict) --*

        A complex data type that specifies when to forward content if a content type isn't
        recognized and profiles to use as by default in a request if a query argument doesn't
        specify a profile to use.

        - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

          The setting in a field-level encryption content type-profile mapping that specifies what
          to do when an unknown content type is provided for the profile. If true, content is
          forwarded without being encrypted when the content type is unknown. If false (the
          default), an error is returned when the content type is unknown.

        - **ContentTypeProfiles** *(dict) --*

          The configuration for a field-level encryption content type-profile.

          - **Quantity** *(integer) --*

            The number of field-level encryption content type-profile mappings.

          - **Items** *(list) --*

            Items in a field-level encryption content type-profile mapping.

            - *(dict) --*

              A field-level encryption content type profile.

              - **Format** *(string) --*

                The format for a field-level encryption content type-profile mapping.

              - **ProfileId** *(string) --*

                The profile ID for a field-level encryption content type-profile mapping.

              - **ContentType** *(string) --*

                The content type for a field-level encryption content type-profile mapping.

    - **ETag** *(string) --*

      The current version of the field level encryption configuration. For example:
      ``E2QWRUHAPOMQZL`` .
    """


_ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef",
    {"Quantity": int, "Items": List[str]},
    total=False,
)


class ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef(
    _ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesItems` `FieldPatterns`

    Field patterns in a field-level encryption content type profile specify the fields
    that you want to be encrypted. You can provide the full field name, or any beginning
    characters followed by a wildcard (*). You can't overlap field patterns. For example,
    you can't have both ABC* and AB*. Note that field patterns are case-sensitive.

    - **Quantity** *(integer) --*

      The number of field-level encryption field patterns.

    - **Items** *(list) --*

      An array of the field-level encryption field patterns.

      - *(string) --*
    """


_ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef",
    {
        "PublicKeyId": str,
        "ProviderId": str,
        "FieldPatterns": ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef,
    },
    total=False,
)


class ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef(
    _ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntities` `Items`

    Complex data type for field-level encryption profiles that includes the encryption key
    and field pattern specifications.

    - **PublicKeyId** *(string) --*

      The public key associated with a set of field-level encryption patterns, to be used
      when encrypting the fields that match the patterns.

    - **ProviderId** *(string) --*

      The provider associated with the public key being used for encryption. This value
      must also be provided with the private key for applications to be able to decrypt
      data.

    - **FieldPatterns** *(dict) --*

      Field patterns in a field-level encryption content type profile specify the fields
      that you want to be encrypted. You can provide the full field name, or any beginning
      characters followed by a wildcard (*). You can't overlap field patterns. For example,
      you can't have both ABC* and AB*. Note that field patterns are case-sensitive.

      - **Quantity** *(integer) --*

        The number of field-level encryption field patterns.

      - **Items** *(list) --*

        An array of the field-level encryption field patterns.

        - *(string) --*
    """


_ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef
        ],
    },
    total=False,
)


class ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef(
    _ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfig` `EncryptionEntities`

    A complex data type of encryption entities for the field-level encryption profile that
    include the public key ID, provider, and field patterns for specifying which fields to
    encrypt with this key.

    - **Quantity** *(integer) --*

      Number of field pattern items in a field-level encryption content type-profile mapping.

    - **Items** *(list) --*

      An array of field patterns in a field-level encryption content type-profile mapping.

      - *(dict) --*

        Complex data type for field-level encryption profiles that includes the encryption key
        and field pattern specifications.

        - **PublicKeyId** *(string) --*

          The public key associated with a set of field-level encryption patterns, to be used
          when encrypting the fields that match the patterns.

        - **ProviderId** *(string) --*

          The provider associated with the public key being used for encryption. This value
          must also be provided with the private key for applications to be able to decrypt
          data.

        - **FieldPatterns** *(dict) --*

          Field patterns in a field-level encryption content type profile specify the fields
          that you want to be encrypted. You can provide the full field name, or any beginning
          characters followed by a wildcard (*). You can't overlap field patterns. For example,
          you can't have both ABC* and AB*. Note that field patterns are case-sensitive.

          - **Quantity** *(integer) --*

            The number of field-level encryption field patterns.

          - **Items** *(list) --*

            An array of the field-level encryption field patterns.

            - *(string) --*
    """


_ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigTypeDef",
    {
        "Name": str,
        "CallerReference": str,
        "Comment": str,
        "EncryptionEntities": ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef,
    },
    total=False,
)


class ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigTypeDef(
    _ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionProfileConfigResponse` `FieldLevelEncryptionProfileConfig`

    Return the field-level encryption profile configuration information.

    - **Name** *(string) --*

      Profile name for the field-level encryption profile.

    - **CallerReference** *(string) --*

      A unique number that ensures that the request can't be replayed.

    - **Comment** *(string) --*

      An optional comment for the field-level encryption profile.

    - **EncryptionEntities** *(dict) --*

      A complex data type of encryption entities for the field-level encryption profile that
      include the public key ID, provider, and field patterns for specifying which fields to
      encrypt with this key.

      - **Quantity** *(integer) --*

        Number of field pattern items in a field-level encryption content type-profile mapping.

      - **Items** *(list) --*

        An array of field patterns in a field-level encryption content type-profile mapping.

        - *(dict) --*

          Complex data type for field-level encryption profiles that includes the encryption key
          and field pattern specifications.

          - **PublicKeyId** *(string) --*

            The public key associated with a set of field-level encryption patterns, to be used
            when encrypting the fields that match the patterns.

          - **ProviderId** *(string) --*

            The provider associated with the public key being used for encryption. This value
            must also be provided with the private key for applications to be able to decrypt
            data.

          - **FieldPatterns** *(dict) --*

            Field patterns in a field-level encryption content type profile specify the fields
            that you want to be encrypted. You can provide the full field name, or any beginning
            characters followed by a wildcard (*). You can't overlap field patterns. For example,
            you can't have both ABC* and AB*. Note that field patterns are case-sensitive.

            - **Quantity** *(integer) --*

              The number of field-level encryption field patterns.

            - **Items** *(list) --*

              An array of the field-level encryption field patterns.

              - *(string) --*
    """


_ClientGetFieldLevelEncryptionProfileConfigResponseTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionProfileConfigResponseTypeDef",
    {
        "FieldLevelEncryptionProfileConfig": ClientGetFieldLevelEncryptionProfileConfigResponseFieldLevelEncryptionProfileConfigTypeDef,
        "ETag": str,
    },
    total=False,
)


class ClientGetFieldLevelEncryptionProfileConfigResponseTypeDef(
    _ClientGetFieldLevelEncryptionProfileConfigResponseTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionProfileConfig` `Response`

    - **FieldLevelEncryptionProfileConfig** *(dict) --*

      Return the field-level encryption profile configuration information.

      - **Name** *(string) --*

        Profile name for the field-level encryption profile.

      - **CallerReference** *(string) --*

        A unique number that ensures that the request can't be replayed.

      - **Comment** *(string) --*

        An optional comment for the field-level encryption profile.

      - **EncryptionEntities** *(dict) --*

        A complex data type of encryption entities for the field-level encryption profile that
        include the public key ID, provider, and field patterns for specifying which fields to
        encrypt with this key.

        - **Quantity** *(integer) --*

          Number of field pattern items in a field-level encryption content type-profile mapping.

        - **Items** *(list) --*

          An array of field patterns in a field-level encryption content type-profile mapping.

          - *(dict) --*

            Complex data type for field-level encryption profiles that includes the encryption key
            and field pattern specifications.

            - **PublicKeyId** *(string) --*

              The public key associated with a set of field-level encryption patterns, to be used
              when encrypting the fields that match the patterns.

            - **ProviderId** *(string) --*

              The provider associated with the public key being used for encryption. This value
              must also be provided with the private key for applications to be able to decrypt
              data.

            - **FieldPatterns** *(dict) --*

              Field patterns in a field-level encryption content type profile specify the fields
              that you want to be encrypted. You can provide the full field name, or any beginning
              characters followed by a wildcard (*). You can't overlap field patterns. For example,
              you can't have both ABC* and AB*. Note that field patterns are case-sensitive.

              - **Quantity** *(integer) --*

                The number of field-level encryption field patterns.

              - **Items** *(list) --*

                An array of the field-level encryption field patterns.

                - *(string) --*

    - **ETag** *(string) --*

      The current version of the field-level encryption profile configuration result. For example:
      ``E2QWRUHAPOMQZL`` .
    """


_ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef",
    {"Quantity": int, "Items": List[str]},
    total=False,
)


class ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef(
    _ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItems` `FieldPatterns`

    Field patterns in a field-level encryption content type profile specify the fields
    that you want to be encrypted. You can provide the full field name, or any
    beginning characters followed by a wildcard (*). You can't overlap field patterns.
    For example, you can't have both ABC* and AB*. Note that field patterns are
    case-sensitive.

    - **Quantity** *(integer) --*

      The number of field-level encryption field patterns.

    - **Items** *(list) --*

      An array of the field-level encryption field patterns.

      - *(string) --*
    """


_ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef",
    {
        "PublicKeyId": str,
        "ProviderId": str,
        "FieldPatterns": ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef,
    },
    total=False,
)


class ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef(
    _ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntities` `Items`

    Complex data type for field-level encryption profiles that includes the encryption
    key and field pattern specifications.

    - **PublicKeyId** *(string) --*

      The public key associated with a set of field-level encryption patterns, to be used
      when encrypting the fields that match the patterns.

    - **ProviderId** *(string) --*

      The provider associated with the public key being used for encryption. This value
      must also be provided with the private key for applications to be able to decrypt
      data.

    - **FieldPatterns** *(dict) --*

      Field patterns in a field-level encryption content type profile specify the fields
      that you want to be encrypted. You can provide the full field name, or any
      beginning characters followed by a wildcard (*). You can't overlap field patterns.
      For example, you can't have both ABC* and AB*. Note that field patterns are
      case-sensitive.

      - **Quantity** *(integer) --*

        The number of field-level encryption field patterns.

      - **Items** *(list) --*

        An array of the field-level encryption field patterns.

        - *(string) --*
    """


_ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef
        ],
    },
    total=False,
)


class ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef(
    _ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfig` `EncryptionEntities`

    A complex data type of encryption entities for the field-level encryption profile that
    include the public key ID, provider, and field patterns for specifying which fields to
    encrypt with this key.

    - **Quantity** *(integer) --*

      Number of field pattern items in a field-level encryption content type-profile mapping.

    - **Items** *(list) --*

      An array of field patterns in a field-level encryption content type-profile mapping.

      - *(dict) --*

        Complex data type for field-level encryption profiles that includes the encryption
        key and field pattern specifications.

        - **PublicKeyId** *(string) --*

          The public key associated with a set of field-level encryption patterns, to be used
          when encrypting the fields that match the patterns.

        - **ProviderId** *(string) --*

          The provider associated with the public key being used for encryption. This value
          must also be provided with the private key for applications to be able to decrypt
          data.

        - **FieldPatterns** *(dict) --*

          Field patterns in a field-level encryption content type profile specify the fields
          that you want to be encrypted. You can provide the full field name, or any
          beginning characters followed by a wildcard (*). You can't overlap field patterns.
          For example, you can't have both ABC* and AB*. Note that field patterns are
          case-sensitive.

          - **Quantity** *(integer) --*

            The number of field-level encryption field patterns.

          - **Items** *(list) --*

            An array of the field-level encryption field patterns.

            - *(string) --*
    """


_ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef",
    {
        "Name": str,
        "CallerReference": str,
        "Comment": str,
        "EncryptionEntities": ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef,
    },
    total=False,
)


class ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef(
    _ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfile` `FieldLevelEncryptionProfileConfig`

    A complex data type that includes the profile name and the encryption entities for the
    field-level encryption profile.

    - **Name** *(string) --*

      Profile name for the field-level encryption profile.

    - **CallerReference** *(string) --*

      A unique number that ensures that the request can't be replayed.

    - **Comment** *(string) --*

      An optional comment for the field-level encryption profile.

    - **EncryptionEntities** *(dict) --*

      A complex data type of encryption entities for the field-level encryption profile that
      include the public key ID, provider, and field patterns for specifying which fields to
      encrypt with this key.

      - **Quantity** *(integer) --*

        Number of field pattern items in a field-level encryption content type-profile mapping.

      - **Items** *(list) --*

        An array of field patterns in a field-level encryption content type-profile mapping.

        - *(dict) --*

          Complex data type for field-level encryption profiles that includes the encryption
          key and field pattern specifications.

          - **PublicKeyId** *(string) --*

            The public key associated with a set of field-level encryption patterns, to be used
            when encrypting the fields that match the patterns.

          - **ProviderId** *(string) --*

            The provider associated with the public key being used for encryption. This value
            must also be provided with the private key for applications to be able to decrypt
            data.

          - **FieldPatterns** *(dict) --*

            Field patterns in a field-level encryption content type profile specify the fields
            that you want to be encrypted. You can provide the full field name, or any
            beginning characters followed by a wildcard (*). You can't overlap field patterns.
            For example, you can't have both ABC* and AB*. Note that field patterns are
            case-sensitive.

            - **Quantity** *(integer) --*

              The number of field-level encryption field patterns.

            - **Items** *(list) --*

              An array of the field-level encryption field patterns.

              - *(string) --*
    """


_ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "FieldLevelEncryptionProfileConfig": ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef,
    },
    total=False,
)


class ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileTypeDef(
    _ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionProfileResponse` `FieldLevelEncryptionProfile`

    Return the field-level encryption profile information.

    - **Id** *(string) --*

      The ID for a field-level encryption profile configuration which includes a set of profiles
      that specify certain selected data fields to be encrypted by specific public keys.

    - **LastModifiedTime** *(datetime) --*

      The last time the field-level encryption profile was updated.

    - **FieldLevelEncryptionProfileConfig** *(dict) --*

      A complex data type that includes the profile name and the encryption entities for the
      field-level encryption profile.

      - **Name** *(string) --*

        Profile name for the field-level encryption profile.

      - **CallerReference** *(string) --*

        A unique number that ensures that the request can't be replayed.

      - **Comment** *(string) --*

        An optional comment for the field-level encryption profile.

      - **EncryptionEntities** *(dict) --*

        A complex data type of encryption entities for the field-level encryption profile that
        include the public key ID, provider, and field patterns for specifying which fields to
        encrypt with this key.

        - **Quantity** *(integer) --*

          Number of field pattern items in a field-level encryption content type-profile mapping.

        - **Items** *(list) --*

          An array of field patterns in a field-level encryption content type-profile mapping.

          - *(dict) --*

            Complex data type for field-level encryption profiles that includes the encryption
            key and field pattern specifications.

            - **PublicKeyId** *(string) --*

              The public key associated with a set of field-level encryption patterns, to be used
              when encrypting the fields that match the patterns.

            - **ProviderId** *(string) --*

              The provider associated with the public key being used for encryption. This value
              must also be provided with the private key for applications to be able to decrypt
              data.

            - **FieldPatterns** *(dict) --*

              Field patterns in a field-level encryption content type profile specify the fields
              that you want to be encrypted. You can provide the full field name, or any
              beginning characters followed by a wildcard (*). You can't overlap field patterns.
              For example, you can't have both ABC* and AB*. Note that field patterns are
              case-sensitive.

              - **Quantity** *(integer) --*

                The number of field-level encryption field patterns.

              - **Items** *(list) --*

                An array of the field-level encryption field patterns.

                - *(string) --*
    """


_ClientGetFieldLevelEncryptionProfileResponseTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionProfileResponseTypeDef",
    {
        "FieldLevelEncryptionProfile": ClientGetFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileTypeDef,
        "ETag": str,
    },
    total=False,
)


class ClientGetFieldLevelEncryptionProfileResponseTypeDef(
    _ClientGetFieldLevelEncryptionProfileResponseTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionProfile` `Response`

    - **FieldLevelEncryptionProfile** *(dict) --*

      Return the field-level encryption profile information.

      - **Id** *(string) --*

        The ID for a field-level encryption profile configuration which includes a set of profiles
        that specify certain selected data fields to be encrypted by specific public keys.

      - **LastModifiedTime** *(datetime) --*

        The last time the field-level encryption profile was updated.

      - **FieldLevelEncryptionProfileConfig** *(dict) --*

        A complex data type that includes the profile name and the encryption entities for the
        field-level encryption profile.

        - **Name** *(string) --*

          Profile name for the field-level encryption profile.

        - **CallerReference** *(string) --*

          A unique number that ensures that the request can't be replayed.

        - **Comment** *(string) --*

          An optional comment for the field-level encryption profile.

        - **EncryptionEntities** *(dict) --*

          A complex data type of encryption entities for the field-level encryption profile that
          include the public key ID, provider, and field patterns for specifying which fields to
          encrypt with this key.

          - **Quantity** *(integer) --*

            Number of field pattern items in a field-level encryption content type-profile mapping.

          - **Items** *(list) --*

            An array of field patterns in a field-level encryption content type-profile mapping.

            - *(dict) --*

              Complex data type for field-level encryption profiles that includes the encryption
              key and field pattern specifications.

              - **PublicKeyId** *(string) --*

                The public key associated with a set of field-level encryption patterns, to be used
                when encrypting the fields that match the patterns.

              - **ProviderId** *(string) --*

                The provider associated with the public key being used for encryption. This value
                must also be provided with the private key for applications to be able to decrypt
                data.

              - **FieldPatterns** *(dict) --*

                Field patterns in a field-level encryption content type profile specify the fields
                that you want to be encrypted. You can provide the full field name, or any
                beginning characters followed by a wildcard (*). You can't overlap field patterns.
                For example, you can't have both ABC* and AB*. Note that field patterns are
                case-sensitive.

                - **Quantity** *(integer) --*

                  The number of field-level encryption field patterns.

                - **Items** *(list) --*

                  An array of the field-level encryption field patterns.

                  - *(string) --*

    - **ETag** *(string) --*

      The current version of the field level encryption profile. For example: ``E2QWRUHAPOMQZL`` .
    """


_ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef",
    {"Format": str, "ProfileId": str, "ContentType": str},
    total=False,
)


class ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef(
    _ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles` `Items`

    A field-level encryption content type profile.

    - **Format** *(string) --*

      The format for a field-level encryption content type-profile mapping.

    - **ProfileId** *(string) --*

      The profile ID for a field-level encryption content type-profile mapping.

    - **ContentType** *(string) --*

      The content type for a field-level encryption content type-profile mapping.
    """


_ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef
        ],
    },
    total=False,
)


class ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef(
    _ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfig` `ContentTypeProfiles`

    The configuration for a field-level encryption content type-profile.

    - **Quantity** *(integer) --*

      The number of field-level encryption content type-profile mappings.

    - **Items** *(list) --*

      Items in a field-level encryption content type-profile mapping.

      - *(dict) --*

        A field-level encryption content type profile.

        - **Format** *(string) --*

          The format for a field-level encryption content type-profile mapping.

        - **ProfileId** *(string) --*

          The profile ID for a field-level encryption content type-profile mapping.

        - **ContentType** *(string) --*

          The content type for a field-level encryption content type-profile mapping.
    """


_ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef",
    {
        "ForwardWhenContentTypeIsUnknown": bool,
        "ContentTypeProfiles": ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef,
    },
    total=False,
)


class ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef(
    _ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfig` `ContentTypeProfileConfig`

    A complex data type that specifies when to forward content if a content type isn't
    recognized and profiles to use as by default in a request if a query argument doesn't
    specify a profile to use.

    - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

      The setting in a field-level encryption content type-profile mapping that specifies
      what to do when an unknown content type is provided for the profile. If true, content
      is forwarded without being encrypted when the content type is unknown. If false (the
      default), an error is returned when the content type is unknown.

    - **ContentTypeProfiles** *(dict) --*

      The configuration for a field-level encryption content type-profile.

      - **Quantity** *(integer) --*

        The number of field-level encryption content type-profile mappings.

      - **Items** *(list) --*

        Items in a field-level encryption content type-profile mapping.

        - *(dict) --*

          A field-level encryption content type profile.

          - **Format** *(string) --*

            The format for a field-level encryption content type-profile mapping.

          - **ProfileId** *(string) --*

            The profile ID for a field-level encryption content type-profile mapping.

          - **ContentType** *(string) --*

            The content type for a field-level encryption content type-profile mapping.
    """


_ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef",
    {"QueryArg": str, "ProfileId": str},
    total=False,
)


class ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef(
    _ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles` `Items`

    Query argument-profile mapping for field-level encryption.

    - **QueryArg** *(string) --*

      Query argument for field-level encryption query argument-profile mapping.

    - **ProfileId** *(string) --*

      ID of profile to use for field-level encryption query argument-profile mapping
    """


_ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef
        ],
    },
    total=False,
)


class ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef(
    _ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfig` `QueryArgProfiles`

    Profiles specified for query argument-profile mapping for field-level encryption.

    - **Quantity** *(integer) --*

      Number of profiles for query argument-profile mapping for field-level encryption.

    - **Items** *(list) --*

      Number of items for query argument-profile mapping for field-level encryption.

      - *(dict) --*

        Query argument-profile mapping for field-level encryption.

        - **QueryArg** *(string) --*

          Query argument for field-level encryption query argument-profile mapping.

        - **ProfileId** *(string) --*

          ID of profile to use for field-level encryption query argument-profile mapping
    """


_ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef",
    {
        "ForwardWhenQueryArgProfileIsUnknown": bool,
        "QueryArgProfiles": ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef,
    },
    total=False,
)


class ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef(
    _ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfig` `QueryArgProfileConfig`

    A complex data type that specifies when to forward content if a profile isn't found and
    the profile that can be provided as a query argument in a request.

    - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

      Flag to set if you want a request to be forwarded to the origin even if the profile
      specified by the field-level encryption query argument, fle-profile, is unknown.

    - **QueryArgProfiles** *(dict) --*

      Profiles specified for query argument-profile mapping for field-level encryption.

      - **Quantity** *(integer) --*

        Number of profiles for query argument-profile mapping for field-level encryption.

      - **Items** *(list) --*

        Number of items for query argument-profile mapping for field-level encryption.

        - *(dict) --*

          Query argument-profile mapping for field-level encryption.

          - **QueryArg** *(string) --*

            Query argument for field-level encryption query argument-profile mapping.

          - **ProfileId** *(string) --*

            ID of profile to use for field-level encryption query argument-profile mapping
    """


_ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigTypeDef",
    {
        "CallerReference": str,
        "Comment": str,
        "QueryArgProfileConfig": ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef,
        "ContentTypeProfileConfig": ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef,
    },
    total=False,
)


class ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigTypeDef(
    _ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionResponseFieldLevelEncryption` `FieldLevelEncryptionConfig`

    A complex data type that includes the profile configurations specified for field-level
    encryption.

    - **CallerReference** *(string) --*

      A unique number that ensures the request can't be replayed.

    - **Comment** *(string) --*

      An optional comment about the configuration.

    - **QueryArgProfileConfig** *(dict) --*

      A complex data type that specifies when to forward content if a profile isn't found and
      the profile that can be provided as a query argument in a request.

      - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

        Flag to set if you want a request to be forwarded to the origin even if the profile
        specified by the field-level encryption query argument, fle-profile, is unknown.

      - **QueryArgProfiles** *(dict) --*

        Profiles specified for query argument-profile mapping for field-level encryption.

        - **Quantity** *(integer) --*

          Number of profiles for query argument-profile mapping for field-level encryption.

        - **Items** *(list) --*

          Number of items for query argument-profile mapping for field-level encryption.

          - *(dict) --*

            Query argument-profile mapping for field-level encryption.

            - **QueryArg** *(string) --*

              Query argument for field-level encryption query argument-profile mapping.

            - **ProfileId** *(string) --*

              ID of profile to use for field-level encryption query argument-profile mapping

    - **ContentTypeProfileConfig** *(dict) --*

      A complex data type that specifies when to forward content if a content type isn't
      recognized and profiles to use as by default in a request if a query argument doesn't
      specify a profile to use.

      - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

        The setting in a field-level encryption content type-profile mapping that specifies
        what to do when an unknown content type is provided for the profile. If true, content
        is forwarded without being encrypted when the content type is unknown. If false (the
        default), an error is returned when the content type is unknown.

      - **ContentTypeProfiles** *(dict) --*

        The configuration for a field-level encryption content type-profile.

        - **Quantity** *(integer) --*

          The number of field-level encryption content type-profile mappings.

        - **Items** *(list) --*

          Items in a field-level encryption content type-profile mapping.

          - *(dict) --*

            A field-level encryption content type profile.

            - **Format** *(string) --*

              The format for a field-level encryption content type-profile mapping.

            - **ProfileId** *(string) --*

              The profile ID for a field-level encryption content type-profile mapping.

            - **ContentType** *(string) --*

              The content type for a field-level encryption content type-profile mapping.
    """


_ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "FieldLevelEncryptionConfig": ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionFieldLevelEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionTypeDef(
    _ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryptionResponse` `FieldLevelEncryption`

    Return the field-level encryption configuration information.

    - **Id** *(string) --*

      The configuration ID for a field-level encryption configuration which includes a set of
      profiles that specify certain selected data fields to be encrypted by specific public keys.

    - **LastModifiedTime** *(datetime) --*

      The last time the field-level encryption configuration was changed.

    - **FieldLevelEncryptionConfig** *(dict) --*

      A complex data type that includes the profile configurations specified for field-level
      encryption.

      - **CallerReference** *(string) --*

        A unique number that ensures the request can't be replayed.

      - **Comment** *(string) --*

        An optional comment about the configuration.

      - **QueryArgProfileConfig** *(dict) --*

        A complex data type that specifies when to forward content if a profile isn't found and
        the profile that can be provided as a query argument in a request.

        - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

          Flag to set if you want a request to be forwarded to the origin even if the profile
          specified by the field-level encryption query argument, fle-profile, is unknown.

        - **QueryArgProfiles** *(dict) --*

          Profiles specified for query argument-profile mapping for field-level encryption.

          - **Quantity** *(integer) --*

            Number of profiles for query argument-profile mapping for field-level encryption.

          - **Items** *(list) --*

            Number of items for query argument-profile mapping for field-level encryption.

            - *(dict) --*

              Query argument-profile mapping for field-level encryption.

              - **QueryArg** *(string) --*

                Query argument for field-level encryption query argument-profile mapping.

              - **ProfileId** *(string) --*

                ID of profile to use for field-level encryption query argument-profile mapping

      - **ContentTypeProfileConfig** *(dict) --*

        A complex data type that specifies when to forward content if a content type isn't
        recognized and profiles to use as by default in a request if a query argument doesn't
        specify a profile to use.

        - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

          The setting in a field-level encryption content type-profile mapping that specifies
          what to do when an unknown content type is provided for the profile. If true, content
          is forwarded without being encrypted when the content type is unknown. If false (the
          default), an error is returned when the content type is unknown.

        - **ContentTypeProfiles** *(dict) --*

          The configuration for a field-level encryption content type-profile.

          - **Quantity** *(integer) --*

            The number of field-level encryption content type-profile mappings.

          - **Items** *(list) --*

            Items in a field-level encryption content type-profile mapping.

            - *(dict) --*

              A field-level encryption content type profile.

              - **Format** *(string) --*

                The format for a field-level encryption content type-profile mapping.

              - **ProfileId** *(string) --*

                The profile ID for a field-level encryption content type-profile mapping.

              - **ContentType** *(string) --*

                The content type for a field-level encryption content type-profile mapping.
    """


_ClientGetFieldLevelEncryptionResponseTypeDef = TypedDict(
    "_ClientGetFieldLevelEncryptionResponseTypeDef",
    {
        "FieldLevelEncryption": ClientGetFieldLevelEncryptionResponseFieldLevelEncryptionTypeDef,
        "ETag": str,
    },
    total=False,
)


class ClientGetFieldLevelEncryptionResponseTypeDef(
    _ClientGetFieldLevelEncryptionResponseTypeDef
):
    """
    Type definition for `ClientGetFieldLevelEncryption` `Response`

    - **FieldLevelEncryption** *(dict) --*

      Return the field-level encryption configuration information.

      - **Id** *(string) --*

        The configuration ID for a field-level encryption configuration which includes a set of
        profiles that specify certain selected data fields to be encrypted by specific public keys.

      - **LastModifiedTime** *(datetime) --*

        The last time the field-level encryption configuration was changed.

      - **FieldLevelEncryptionConfig** *(dict) --*

        A complex data type that includes the profile configurations specified for field-level
        encryption.

        - **CallerReference** *(string) --*

          A unique number that ensures the request can't be replayed.

        - **Comment** *(string) --*

          An optional comment about the configuration.

        - **QueryArgProfileConfig** *(dict) --*

          A complex data type that specifies when to forward content if a profile isn't found and
          the profile that can be provided as a query argument in a request.

          - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

            Flag to set if you want a request to be forwarded to the origin even if the profile
            specified by the field-level encryption query argument, fle-profile, is unknown.

          - **QueryArgProfiles** *(dict) --*

            Profiles specified for query argument-profile mapping for field-level encryption.

            - **Quantity** *(integer) --*

              Number of profiles for query argument-profile mapping for field-level encryption.

            - **Items** *(list) --*

              Number of items for query argument-profile mapping for field-level encryption.

              - *(dict) --*

                Query argument-profile mapping for field-level encryption.

                - **QueryArg** *(string) --*

                  Query argument for field-level encryption query argument-profile mapping.

                - **ProfileId** *(string) --*

                  ID of profile to use for field-level encryption query argument-profile mapping

        - **ContentTypeProfileConfig** *(dict) --*

          A complex data type that specifies when to forward content if a content type isn't
          recognized and profiles to use as by default in a request if a query argument doesn't
          specify a profile to use.

          - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

            The setting in a field-level encryption content type-profile mapping that specifies
            what to do when an unknown content type is provided for the profile. If true, content
            is forwarded without being encrypted when the content type is unknown. If false (the
            default), an error is returned when the content type is unknown.

          - **ContentTypeProfiles** *(dict) --*

            The configuration for a field-level encryption content type-profile.

            - **Quantity** *(integer) --*

              The number of field-level encryption content type-profile mappings.

            - **Items** *(list) --*

              Items in a field-level encryption content type-profile mapping.

              - *(dict) --*

                A field-level encryption content type profile.

                - **Format** *(string) --*

                  The format for a field-level encryption content type-profile mapping.

                - **ProfileId** *(string) --*

                  The profile ID for a field-level encryption content type-profile mapping.

                - **ContentType** *(string) --*

                  The content type for a field-level encryption content type-profile mapping.

    - **ETag** *(string) --*

      The current version of the field level encryption configuration. For example:
      ``E2QWRUHAPOMQZL`` .
    """


_ClientGetInvalidationResponseInvalidationInvalidationBatchPathsTypeDef = TypedDict(
    "_ClientGetInvalidationResponseInvalidationInvalidationBatchPathsTypeDef",
    {"Quantity": int, "Items": List[str]},
    total=False,
)


class ClientGetInvalidationResponseInvalidationInvalidationBatchPathsTypeDef(
    _ClientGetInvalidationResponseInvalidationInvalidationBatchPathsTypeDef
):
    """
    Type definition for `ClientGetInvalidationResponseInvalidationInvalidationBatch` `Paths`

    A complex type that contains information about the objects that you want to invalidate.
    For more information, see `Specifying the Objects to Invalidate
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-specifying-objects>`__
    in the *Amazon CloudFront Developer Guide* .

    - **Quantity** *(integer) --*

      The number of invalidation paths specified for the objects that you want to invalidate.

    - **Items** *(list) --*

      A complex type that contains a list of the paths that you want to invalidate.

      - *(string) --*
    """


_ClientGetInvalidationResponseInvalidationInvalidationBatchTypeDef = TypedDict(
    "_ClientGetInvalidationResponseInvalidationInvalidationBatchTypeDef",
    {
        "Paths": ClientGetInvalidationResponseInvalidationInvalidationBatchPathsTypeDef,
        "CallerReference": str,
    },
    total=False,
)


class ClientGetInvalidationResponseInvalidationInvalidationBatchTypeDef(
    _ClientGetInvalidationResponseInvalidationInvalidationBatchTypeDef
):
    """
    Type definition for `ClientGetInvalidationResponseInvalidation` `InvalidationBatch`

    The current invalidation information for the batch request.

    - **Paths** *(dict) --*

      A complex type that contains information about the objects that you want to invalidate.
      For more information, see `Specifying the Objects to Invalidate
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-specifying-objects>`__
      in the *Amazon CloudFront Developer Guide* .

      - **Quantity** *(integer) --*

        The number of invalidation paths specified for the objects that you want to invalidate.

      - **Items** *(list) --*

        A complex type that contains a list of the paths that you want to invalidate.

        - *(string) --*

    - **CallerReference** *(string) --*

      A value that you specify to uniquely identify an invalidation request. CloudFront uses
      the value to prevent you from accidentally resubmitting an identical request. Whenever
      you create a new invalidation request, you must specify a new value for
      ``CallerReference`` and change other values in the request as applicable. One way to
      ensure that the value of ``CallerReference`` is unique is to use a ``timestamp`` , for
      example, ``20120301090000`` .

      If you make a second invalidation request with the same value for ``CallerReference`` ,
      and if the rest of the request is the same, CloudFront doesn't create a new invalidation
      request. Instead, CloudFront returns information about the invalidation request that you
      previously created with the same ``CallerReference`` .

      If ``CallerReference`` is a value you already sent in a previous invalidation batch
      request but the content of any ``Path`` is different from the original request,
      CloudFront returns an ``InvalidationBatchAlreadyExists`` error.
    """


_ClientGetInvalidationResponseInvalidationTypeDef = TypedDict(
    "_ClientGetInvalidationResponseInvalidationTypeDef",
    {
        "Id": str,
        "Status": str,
        "CreateTime": datetime,
        "InvalidationBatch": ClientGetInvalidationResponseInvalidationInvalidationBatchTypeDef,
    },
    total=False,
)


class ClientGetInvalidationResponseInvalidationTypeDef(
    _ClientGetInvalidationResponseInvalidationTypeDef
):
    """
    Type definition for `ClientGetInvalidationResponse` `Invalidation`

    The invalidation's information. For more information, see `Invalidation Complex Type
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/InvalidationDatatype.html>`__
    .

    - **Id** *(string) --*

      The identifier for the invalidation request. For example: ``IDFDVBD632BHDS5`` .

    - **Status** *(string) --*

      The status of the invalidation request. When the invalidation batch is finished, the status
      is ``Completed`` .

    - **CreateTime** *(datetime) --*

      The date and time the invalidation request was first made.

    - **InvalidationBatch** *(dict) --*

      The current invalidation information for the batch request.

      - **Paths** *(dict) --*

        A complex type that contains information about the objects that you want to invalidate.
        For more information, see `Specifying the Objects to Invalidate
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-specifying-objects>`__
        in the *Amazon CloudFront Developer Guide* .

        - **Quantity** *(integer) --*

          The number of invalidation paths specified for the objects that you want to invalidate.

        - **Items** *(list) --*

          A complex type that contains a list of the paths that you want to invalidate.

          - *(string) --*

      - **CallerReference** *(string) --*

        A value that you specify to uniquely identify an invalidation request. CloudFront uses
        the value to prevent you from accidentally resubmitting an identical request. Whenever
        you create a new invalidation request, you must specify a new value for
        ``CallerReference`` and change other values in the request as applicable. One way to
        ensure that the value of ``CallerReference`` is unique is to use a ``timestamp`` , for
        example, ``20120301090000`` .

        If you make a second invalidation request with the same value for ``CallerReference`` ,
        and if the rest of the request is the same, CloudFront doesn't create a new invalidation
        request. Instead, CloudFront returns information about the invalidation request that you
        previously created with the same ``CallerReference`` .

        If ``CallerReference`` is a value you already sent in a previous invalidation batch
        request but the content of any ``Path`` is different from the original request,
        CloudFront returns an ``InvalidationBatchAlreadyExists`` error.
    """


_ClientGetInvalidationResponseTypeDef = TypedDict(
    "_ClientGetInvalidationResponseTypeDef",
    {"Invalidation": ClientGetInvalidationResponseInvalidationTypeDef},
    total=False,
)


class ClientGetInvalidationResponseTypeDef(_ClientGetInvalidationResponseTypeDef):
    """
    Type definition for `ClientGetInvalidation` `Response`

    The returned result of the corresponding request.

    - **Invalidation** *(dict) --*

      The invalidation's information. For more information, see `Invalidation Complex Type
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/InvalidationDatatype.html>`__
      .

      - **Id** *(string) --*

        The identifier for the invalidation request. For example: ``IDFDVBD632BHDS5`` .

      - **Status** *(string) --*

        The status of the invalidation request. When the invalidation batch is finished, the status
        is ``Completed`` .

      - **CreateTime** *(datetime) --*

        The date and time the invalidation request was first made.

      - **InvalidationBatch** *(dict) --*

        The current invalidation information for the batch request.

        - **Paths** *(dict) --*

          A complex type that contains information about the objects that you want to invalidate.
          For more information, see `Specifying the Objects to Invalidate
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-specifying-objects>`__
          in the *Amazon CloudFront Developer Guide* .

          - **Quantity** *(integer) --*

            The number of invalidation paths specified for the objects that you want to invalidate.

          - **Items** *(list) --*

            A complex type that contains a list of the paths that you want to invalidate.

            - *(string) --*

        - **CallerReference** *(string) --*

          A value that you specify to uniquely identify an invalidation request. CloudFront uses
          the value to prevent you from accidentally resubmitting an identical request. Whenever
          you create a new invalidation request, you must specify a new value for
          ``CallerReference`` and change other values in the request as applicable. One way to
          ensure that the value of ``CallerReference`` is unique is to use a ``timestamp`` , for
          example, ``20120301090000`` .

          If you make a second invalidation request with the same value for ``CallerReference`` ,
          and if the rest of the request is the same, CloudFront doesn't create a new invalidation
          request. Instead, CloudFront returns information about the invalidation request that you
          previously created with the same ``CallerReference`` .

          If ``CallerReference`` is a value you already sent in a previous invalidation batch
          request but the content of any ``Path`` is different from the original request,
          CloudFront returns an ``InvalidationBatchAlreadyExists`` error.
    """


_ClientGetPublicKeyConfigResponsePublicKeyConfigTypeDef = TypedDict(
    "_ClientGetPublicKeyConfigResponsePublicKeyConfigTypeDef",
    {"CallerReference": str, "Name": str, "EncodedKey": str, "Comment": str},
    total=False,
)


class ClientGetPublicKeyConfigResponsePublicKeyConfigTypeDef(
    _ClientGetPublicKeyConfigResponsePublicKeyConfigTypeDef
):
    """
    Type definition for `ClientGetPublicKeyConfigResponse` `PublicKeyConfig`

    Return the result for the public key configuration.

    - **CallerReference** *(string) --*

      A unique number that ensures that the request can't be replayed.

    - **Name** *(string) --*

      The name for a public key you add to CloudFront to use with features like field-level
      encryption.

    - **EncodedKey** *(string) --*

      The encoded public key that you want to add to CloudFront to use with features like
      field-level encryption.

    - **Comment** *(string) --*

      An optional comment about a public key.
    """


_ClientGetPublicKeyConfigResponseTypeDef = TypedDict(
    "_ClientGetPublicKeyConfigResponseTypeDef",
    {
        "PublicKeyConfig": ClientGetPublicKeyConfigResponsePublicKeyConfigTypeDef,
        "ETag": str,
    },
    total=False,
)


class ClientGetPublicKeyConfigResponseTypeDef(_ClientGetPublicKeyConfigResponseTypeDef):
    """
    Type definition for `ClientGetPublicKeyConfig` `Response`

    - **PublicKeyConfig** *(dict) --*

      Return the result for the public key configuration.

      - **CallerReference** *(string) --*

        A unique number that ensures that the request can't be replayed.

      - **Name** *(string) --*

        The name for a public key you add to CloudFront to use with features like field-level
        encryption.

      - **EncodedKey** *(string) --*

        The encoded public key that you want to add to CloudFront to use with features like
        field-level encryption.

      - **Comment** *(string) --*

        An optional comment about a public key.

    - **ETag** *(string) --*

      The current version of the public key configuration. For example: ``E2QWRUHAPOMQZL`` .
    """


_ClientGetPublicKeyResponsePublicKeyPublicKeyConfigTypeDef = TypedDict(
    "_ClientGetPublicKeyResponsePublicKeyPublicKeyConfigTypeDef",
    {"CallerReference": str, "Name": str, "EncodedKey": str, "Comment": str},
    total=False,
)


class ClientGetPublicKeyResponsePublicKeyPublicKeyConfigTypeDef(
    _ClientGetPublicKeyResponsePublicKeyPublicKeyConfigTypeDef
):
    """
    Type definition for `ClientGetPublicKeyResponsePublicKey` `PublicKeyConfig`

    A complex data type for a public key you add to CloudFront to use with features like
    field-level encryption.

    - **CallerReference** *(string) --*

      A unique number that ensures that the request can't be replayed.

    - **Name** *(string) --*

      The name for a public key you add to CloudFront to use with features like field-level
      encryption.

    - **EncodedKey** *(string) --*

      The encoded public key that you want to add to CloudFront to use with features like
      field-level encryption.

    - **Comment** *(string) --*

      An optional comment about a public key.
    """


_ClientGetPublicKeyResponsePublicKeyTypeDef = TypedDict(
    "_ClientGetPublicKeyResponsePublicKeyTypeDef",
    {
        "Id": str,
        "CreatedTime": datetime,
        "PublicKeyConfig": ClientGetPublicKeyResponsePublicKeyPublicKeyConfigTypeDef,
    },
    total=False,
)


class ClientGetPublicKeyResponsePublicKeyTypeDef(
    _ClientGetPublicKeyResponsePublicKeyTypeDef
):
    """
    Type definition for `ClientGetPublicKeyResponse` `PublicKey`

    Return the public key.

    - **Id** *(string) --*

      A unique ID assigned to a public key you've added to CloudFront.

    - **CreatedTime** *(datetime) --*

      A time you added a public key to CloudFront.

    - **PublicKeyConfig** *(dict) --*

      A complex data type for a public key you add to CloudFront to use with features like
      field-level encryption.

      - **CallerReference** *(string) --*

        A unique number that ensures that the request can't be replayed.

      - **Name** *(string) --*

        The name for a public key you add to CloudFront to use with features like field-level
        encryption.

      - **EncodedKey** *(string) --*

        The encoded public key that you want to add to CloudFront to use with features like
        field-level encryption.

      - **Comment** *(string) --*

        An optional comment about a public key.
    """


_ClientGetPublicKeyResponseTypeDef = TypedDict(
    "_ClientGetPublicKeyResponseTypeDef",
    {"PublicKey": ClientGetPublicKeyResponsePublicKeyTypeDef, "ETag": str},
    total=False,
)


class ClientGetPublicKeyResponseTypeDef(_ClientGetPublicKeyResponseTypeDef):
    """
    Type definition for `ClientGetPublicKey` `Response`

    - **PublicKey** *(dict) --*

      Return the public key.

      - **Id** *(string) --*

        A unique ID assigned to a public key you've added to CloudFront.

      - **CreatedTime** *(datetime) --*

        A time you added a public key to CloudFront.

      - **PublicKeyConfig** *(dict) --*

        A complex data type for a public key you add to CloudFront to use with features like
        field-level encryption.

        - **CallerReference** *(string) --*

          A unique number that ensures that the request can't be replayed.

        - **Name** *(string) --*

          The name for a public key you add to CloudFront to use with features like field-level
          encryption.

        - **EncodedKey** *(string) --*

          The encoded public key that you want to add to CloudFront to use with features like
          field-level encryption.

        - **Comment** *(string) --*

          An optional comment about a public key.

    - **ETag** *(string) --*

      The current version of the public key. For example: ``E2QWRUHAPOMQZL`` .
    """


_ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigAliasesTypeDef = TypedDict(
    "_ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigAliasesTypeDef",
    {"Quantity": int, "Items": List[str]},
    total=False,
)


class ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigAliasesTypeDef(
    _ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigAliasesTypeDef
):
    """
    Type definition for `ClientGetStreamingDistributionConfigResponseStreamingDistributionConfig` `Aliases`

    A complex type that contains information about CNAMEs (alternate domain names), if any, for
    this streaming distribution.

    - **Quantity** *(integer) --*

      The number of CNAME aliases, if any, that you want to associate with this distribution.

    - **Items** *(list) --*

      A complex type that contains the CNAME aliases, if any, that you want to associate with
      this distribution.

      - *(string) --*
    """


_ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigLoggingTypeDef = TypedDict(
    "_ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigLoggingTypeDef",
    {"Enabled": bool, "Bucket": str, "Prefix": str},
    total=False,
)


class ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigLoggingTypeDef(
    _ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigLoggingTypeDef
):
    """
    Type definition for `ClientGetStreamingDistributionConfigResponseStreamingDistributionConfig` `Logging`

    A complex type that controls whether access logs are written for the streaming distribution.

    - **Enabled** *(boolean) --*

      Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you
      don't want to enable logging when you create a streaming distribution or if you want to
      disable logging for an existing streaming distribution, specify ``false`` for ``Enabled``
      , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify ``false`` for
      ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the values are
      automatically deleted.

    - **Bucket** *(string) --*

      The Amazon S3 bucket to store the access logs in, for example,
      ``myawslogbucket.s3.amazonaws.com`` .

    - **Prefix** *(string) --*

      An optional string that you want CloudFront to prefix to the access log filenames for
      this streaming distribution, for example, ``myprefix/`` . If you want to enable logging,
      but you don't want to specify a prefix, you still must include an empty ``Prefix``
      element in the ``Logging`` element.
    """


_ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigS3OriginTypeDef = TypedDict(
    "_ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigS3OriginTypeDef",
    {"DomainName": str, "OriginAccessIdentity": str},
    total=False,
)


class ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigS3OriginTypeDef(
    _ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigS3OriginTypeDef
):
    """
    Type definition for `ClientGetStreamingDistributionConfigResponseStreamingDistributionConfig` `S3Origin`

    A complex type that contains information about the Amazon S3 bucket from which you want
    CloudFront to get your media files for distribution.

    - **DomainName** *(string) --*

      The DNS name of the Amazon S3 origin.

    - **OriginAccessIdentity** *(string) --*

      The CloudFront origin access identity to associate with the distribution. Use an origin
      access identity to configure the distribution so that end users can only access objects
      in an Amazon S3 bucket through CloudFront.

      If you want end users to be able to access objects using either the CloudFront URL or the
      Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

      To delete the origin access identity from an existing distribution, update the
      distribution configuration and include an empty ``OriginAccessIdentity`` element.

      To replace the origin access identity, update the distribution configuration and specify
      the new origin access identity.

      For more information, see `Using an Origin Access Identity to Restrict Access to Your
      Amazon S3 Content
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
      in the *Amazon CloudFront Developer Guide* .
    """


_ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigTrustedSignersTypeDef = TypedDict(
    "_ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigTrustedSignersTypeDef",
    {"Enabled": bool, "Quantity": int, "Items": List[str]},
    total=False,
)


class ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigTrustedSignersTypeDef(
    _ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigTrustedSignersTypeDef
):
    """
    Type definition for `ClientGetStreamingDistributionConfigResponseStreamingDistributionConfig` `TrustedSigners`

    A complex type that specifies any AWS accounts that you want to permit to create signed
    URLs for private content. If you want the distribution to use signed URLs, include this
    element; if you want the distribution to use public URLs, remove this element. For more
    information, see `Serving Private Content through CloudFront
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
    in the *Amazon CloudFront Developer Guide* .

    - **Enabled** *(boolean) --*

      Specifies whether you want to require viewers to use signed URLs to access the files
      specified by ``PathPattern`` and ``TargetOriginId`` .

    - **Quantity** *(integer) --*

      The number of trusted signers for this cache behavior.

    - **Items** *(list) --*

       **Optional** : A complex type that contains trusted signers for this cache behavior. If
       ``Quantity`` is ``0`` , you can omit ``Items`` .

      - *(string) --*
    """


_ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigTypeDef = TypedDict(
    "_ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "S3Origin": ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigS3OriginTypeDef,
        "Aliases": ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigAliasesTypeDef,
        "Comment": str,
        "Logging": ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigLoggingTypeDef,
        "TrustedSigners": ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigTrustedSignersTypeDef,
        "PriceClass": str,
        "Enabled": bool,
    },
    total=False,
)


class ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigTypeDef(
    _ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigTypeDef
):
    """
    Type definition for `ClientGetStreamingDistributionConfigResponse` `StreamingDistributionConfig`

    The streaming distribution's configuration information.

    - **CallerReference** *(string) --*

      A unique value (for example, a date-time stamp) that ensures that the request can't be
      replayed.

      If the value of ``CallerReference`` is new (regardless of the content of the
      ``StreamingDistributionConfig`` object), CloudFront creates a new distribution.

      If ``CallerReference`` is a value that you already sent in a previous request to create a
      distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

    - **S3Origin** *(dict) --*

      A complex type that contains information about the Amazon S3 bucket from which you want
      CloudFront to get your media files for distribution.

      - **DomainName** *(string) --*

        The DNS name of the Amazon S3 origin.

      - **OriginAccessIdentity** *(string) --*

        The CloudFront origin access identity to associate with the distribution. Use an origin
        access identity to configure the distribution so that end users can only access objects
        in an Amazon S3 bucket through CloudFront.

        If you want end users to be able to access objects using either the CloudFront URL or the
        Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

        To delete the origin access identity from an existing distribution, update the
        distribution configuration and include an empty ``OriginAccessIdentity`` element.

        To replace the origin access identity, update the distribution configuration and specify
        the new origin access identity.

        For more information, see `Using an Origin Access Identity to Restrict Access to Your
        Amazon S3 Content
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
        in the *Amazon CloudFront Developer Guide* .

    - **Aliases** *(dict) --*

      A complex type that contains information about CNAMEs (alternate domain names), if any, for
      this streaming distribution.

      - **Quantity** *(integer) --*

        The number of CNAME aliases, if any, that you want to associate with this distribution.

      - **Items** *(list) --*

        A complex type that contains the CNAME aliases, if any, that you want to associate with
        this distribution.

        - *(string) --*

    - **Comment** *(string) --*

      Any comments you want to include about the streaming distribution.

    - **Logging** *(dict) --*

      A complex type that controls whether access logs are written for the streaming distribution.

      - **Enabled** *(boolean) --*

        Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you
        don't want to enable logging when you create a streaming distribution or if you want to
        disable logging for an existing streaming distribution, specify ``false`` for ``Enabled``
        , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify ``false`` for
        ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the values are
        automatically deleted.

      - **Bucket** *(string) --*

        The Amazon S3 bucket to store the access logs in, for example,
        ``myawslogbucket.s3.amazonaws.com`` .

      - **Prefix** *(string) --*

        An optional string that you want CloudFront to prefix to the access log filenames for
        this streaming distribution, for example, ``myprefix/`` . If you want to enable logging,
        but you don't want to specify a prefix, you still must include an empty ``Prefix``
        element in the ``Logging`` element.

    - **TrustedSigners** *(dict) --*

      A complex type that specifies any AWS accounts that you want to permit to create signed
      URLs for private content. If you want the distribution to use signed URLs, include this
      element; if you want the distribution to use public URLs, remove this element. For more
      information, see `Serving Private Content through CloudFront
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
      in the *Amazon CloudFront Developer Guide* .

      - **Enabled** *(boolean) --*

        Specifies whether you want to require viewers to use signed URLs to access the files
        specified by ``PathPattern`` and ``TargetOriginId`` .

      - **Quantity** *(integer) --*

        The number of trusted signers for this cache behavior.

      - **Items** *(list) --*

         **Optional** : A complex type that contains trusted signers for this cache behavior. If
         ``Quantity`` is ``0`` , you can omit ``Items`` .

        - *(string) --*

    - **PriceClass** *(string) --*

      A complex type that contains information about price class for this streaming distribution.

    - **Enabled** *(boolean) --*

      Whether the streaming distribution is enabled to accept user requests for content.
    """


_ClientGetStreamingDistributionConfigResponseTypeDef = TypedDict(
    "_ClientGetStreamingDistributionConfigResponseTypeDef",
    {
        "StreamingDistributionConfig": ClientGetStreamingDistributionConfigResponseStreamingDistributionConfigTypeDef,
        "ETag": str,
    },
    total=False,
)


class ClientGetStreamingDistributionConfigResponseTypeDef(
    _ClientGetStreamingDistributionConfigResponseTypeDef
):
    """
    Type definition for `ClientGetStreamingDistributionConfig` `Response`

    The returned result of the corresponding request.

    - **StreamingDistributionConfig** *(dict) --*

      The streaming distribution's configuration information.

      - **CallerReference** *(string) --*

        A unique value (for example, a date-time stamp) that ensures that the request can't be
        replayed.

        If the value of ``CallerReference`` is new (regardless of the content of the
        ``StreamingDistributionConfig`` object), CloudFront creates a new distribution.

        If ``CallerReference`` is a value that you already sent in a previous request to create a
        distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

      - **S3Origin** *(dict) --*

        A complex type that contains information about the Amazon S3 bucket from which you want
        CloudFront to get your media files for distribution.

        - **DomainName** *(string) --*

          The DNS name of the Amazon S3 origin.

        - **OriginAccessIdentity** *(string) --*

          The CloudFront origin access identity to associate with the distribution. Use an origin
          access identity to configure the distribution so that end users can only access objects
          in an Amazon S3 bucket through CloudFront.

          If you want end users to be able to access objects using either the CloudFront URL or the
          Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

          To delete the origin access identity from an existing distribution, update the
          distribution configuration and include an empty ``OriginAccessIdentity`` element.

          To replace the origin access identity, update the distribution configuration and specify
          the new origin access identity.

          For more information, see `Using an Origin Access Identity to Restrict Access to Your
          Amazon S3 Content
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
          in the *Amazon CloudFront Developer Guide* .

      - **Aliases** *(dict) --*

        A complex type that contains information about CNAMEs (alternate domain names), if any, for
        this streaming distribution.

        - **Quantity** *(integer) --*

          The number of CNAME aliases, if any, that you want to associate with this distribution.

        - **Items** *(list) --*

          A complex type that contains the CNAME aliases, if any, that you want to associate with
          this distribution.

          - *(string) --*

      - **Comment** *(string) --*

        Any comments you want to include about the streaming distribution.

      - **Logging** *(dict) --*

        A complex type that controls whether access logs are written for the streaming distribution.

        - **Enabled** *(boolean) --*

          Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you
          don't want to enable logging when you create a streaming distribution or if you want to
          disable logging for an existing streaming distribution, specify ``false`` for ``Enabled``
          , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify ``false`` for
          ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the values are
          automatically deleted.

        - **Bucket** *(string) --*

          The Amazon S3 bucket to store the access logs in, for example,
          ``myawslogbucket.s3.amazonaws.com`` .

        - **Prefix** *(string) --*

          An optional string that you want CloudFront to prefix to the access log filenames for
          this streaming distribution, for example, ``myprefix/`` . If you want to enable logging,
          but you don't want to specify a prefix, you still must include an empty ``Prefix``
          element in the ``Logging`` element.

      - **TrustedSigners** *(dict) --*

        A complex type that specifies any AWS accounts that you want to permit to create signed
        URLs for private content. If you want the distribution to use signed URLs, include this
        element; if you want the distribution to use public URLs, remove this element. For more
        information, see `Serving Private Content through CloudFront
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
        in the *Amazon CloudFront Developer Guide* .

        - **Enabled** *(boolean) --*

          Specifies whether you want to require viewers to use signed URLs to access the files
          specified by ``PathPattern`` and ``TargetOriginId`` .

        - **Quantity** *(integer) --*

          The number of trusted signers for this cache behavior.

        - **Items** *(list) --*

           **Optional** : A complex type that contains trusted signers for this cache behavior. If
           ``Quantity`` is ``0`` , you can omit ``Items`` .

          - *(string) --*

      - **PriceClass** *(string) --*

        A complex type that contains information about price class for this streaming distribution.

      - **Enabled** *(boolean) --*

        Whether the streaming distribution is enabled to accept user requests for content.

    - **ETag** *(string) --*

      The current version of the configuration. For example: ``E2QWRUHAPOMQZL`` .
    """


_ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef = TypedDict(
    "_ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef",
    {"Quantity": int, "Items": List[str]},
    total=False,
)


class ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef(
    _ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef
):
    """
    Type definition for `ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItems` `KeyPairIds`

    A complex type that lists the active CloudFront key pairs, if any, that are
    associated with ``AwsAccountNumber`` .

    - **Quantity** *(integer) --*

      The number of active CloudFront key pairs for ``AwsAccountNumber`` .

      For more information, see `ActiveTrustedSigners
      <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
      .

    - **Items** *(list) --*

      A complex type that lists the active CloudFront key pairs, if any, that are
      associated with ``AwsAccountNumber`` .

      For more information, see `ActiveTrustedSigners
      <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
      .

      - *(string) --*
    """


_ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsTypeDef = TypedDict(
    "_ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsTypeDef",
    {
        "AwsAccountNumber": str,
        "KeyPairIds": ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef,
    },
    total=False,
)


class ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsTypeDef(
    _ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsTypeDef
):
    """
    Type definition for `ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSigners` `Items`

    A complex type that lists the AWS accounts that were included in the ``TrustedSigners``
    complex type, as well as their active CloudFront key pair IDs, if any.

    - **AwsAccountNumber** *(string) --*

      An AWS account that is included in the ``TrustedSigners`` complex type for this
      distribution. Valid values include:

      * ``self`` , which is the AWS account used to create the distribution.

      * An AWS account number.

    - **KeyPairIds** *(dict) --*

      A complex type that lists the active CloudFront key pairs, if any, that are
      associated with ``AwsAccountNumber`` .

      - **Quantity** *(integer) --*

        The number of active CloudFront key pairs for ``AwsAccountNumber`` .

        For more information, see `ActiveTrustedSigners
        <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
        .

      - **Items** *(list) --*

        A complex type that lists the active CloudFront key pairs, if any, that are
        associated with ``AwsAccountNumber`` .

        For more information, see `ActiveTrustedSigners
        <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
        .

        - *(string) --*
    """


_ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersTypeDef = TypedDict(
    "_ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
        "Items": List[
            ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsTypeDef
        ],
    },
    total=False,
)


class ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersTypeDef(
    _ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersTypeDef
):
    """
    Type definition for `ClientGetStreamingDistributionResponseStreamingDistribution` `ActiveTrustedSigners`

    A complex type that lists the AWS accounts, if any, that you included in the
    ``TrustedSigners`` complex type for this distribution. These are the accounts that you want
    to allow to create signed URLs for private content.

    The ``Signer`` complex type lists the AWS account number of the trusted signer or ``self``
    if the signer is the AWS account that created the distribution. The ``Signer`` element also
    includes the IDs of any active CloudFront key pairs that are associated with the trusted
    signer's AWS account. If no ``KeyPairId`` element appears for a ``Signer`` , that signer
    can't create signed URLs.

    For more information, see `Serving Private Content through CloudFront
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
    in the *Amazon CloudFront Developer Guide* .

    - **Enabled** *(boolean) --*

      Enabled is ``true`` if any of the AWS accounts listed in the ``TrustedSigners`` complex
      type for this distribution have active CloudFront key pairs. If not, ``Enabled`` is
      ``false`` .

    - **Quantity** *(integer) --*

      The number of trusted signers specified in the ``TrustedSigners`` complex type.

    - **Items** *(list) --*

      A complex type that contains one ``Signer`` complex type for each trusted signer that is
      specified in the ``TrustedSigners`` complex type.

      - *(dict) --*

        A complex type that lists the AWS accounts that were included in the ``TrustedSigners``
        complex type, as well as their active CloudFront key pair IDs, if any.

        - **AwsAccountNumber** *(string) --*

          An AWS account that is included in the ``TrustedSigners`` complex type for this
          distribution. Valid values include:

          * ``self`` , which is the AWS account used to create the distribution.

          * An AWS account number.

        - **KeyPairIds** *(dict) --*

          A complex type that lists the active CloudFront key pairs, if any, that are
          associated with ``AwsAccountNumber`` .

          - **Quantity** *(integer) --*

            The number of active CloudFront key pairs for ``AwsAccountNumber`` .

            For more information, see `ActiveTrustedSigners
            <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
            .

          - **Items** *(list) --*

            A complex type that lists the active CloudFront key pairs, if any, that are
            associated with ``AwsAccountNumber`` .

            For more information, see `ActiveTrustedSigners
            <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
            .

            - *(string) --*
    """


_ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef = TypedDict(
    "_ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef",
    {"Quantity": int, "Items": List[str]},
    total=False,
)


class ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef(
    _ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef
):
    """
    Type definition for `ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfig` `Aliases`

    A complex type that contains information about CNAMEs (alternate domain names), if any,
    for this streaming distribution.

    - **Quantity** *(integer) --*

      The number of CNAME aliases, if any, that you want to associate with this distribution.

    - **Items** *(list) --*

      A complex type that contains the CNAME aliases, if any, that you want to associate with
      this distribution.

      - *(string) --*
    """


_ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef = TypedDict(
    "_ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef",
    {"Enabled": bool, "Bucket": str, "Prefix": str},
    total=False,
)


class ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef(
    _ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef
):
    """
    Type definition for `ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfig` `Logging`

    A complex type that controls whether access logs are written for the streaming
    distribution.

    - **Enabled** *(boolean) --*

      Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If
      you don't want to enable logging when you create a streaming distribution or if you
      want to disable logging for an existing streaming distribution, specify ``false`` for
      ``Enabled`` , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify
      ``false`` for ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the
      values are automatically deleted.

    - **Bucket** *(string) --*

      The Amazon S3 bucket to store the access logs in, for example,
      ``myawslogbucket.s3.amazonaws.com`` .

    - **Prefix** *(string) --*

      An optional string that you want CloudFront to prefix to the access log filenames for
      this streaming distribution, for example, ``myprefix/`` . If you want to enable
      logging, but you don't want to specify a prefix, you still must include an empty
      ``Prefix`` element in the ``Logging`` element.
    """


_ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef = TypedDict(
    "_ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef",
    {"DomainName": str, "OriginAccessIdentity": str},
    total=False,
)


class ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef(
    _ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef
):
    """
    Type definition for `ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfig` `S3Origin`

    A complex type that contains information about the Amazon S3 bucket from which you want
    CloudFront to get your media files for distribution.

    - **DomainName** *(string) --*

      The DNS name of the Amazon S3 origin.

    - **OriginAccessIdentity** *(string) --*

      The CloudFront origin access identity to associate with the distribution. Use an origin
      access identity to configure the distribution so that end users can only access objects
      in an Amazon S3 bucket through CloudFront.

      If you want end users to be able to access objects using either the CloudFront URL or
      the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

      To delete the origin access identity from an existing distribution, update the
      distribution configuration and include an empty ``OriginAccessIdentity`` element.

      To replace the origin access identity, update the distribution configuration and
      specify the new origin access identity.

      For more information, see `Using an Origin Access Identity to Restrict Access to Your
      Amazon S3 Content
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
      in the *Amazon CloudFront Developer Guide* .
    """


_ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef = TypedDict(
    "_ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef",
    {"Enabled": bool, "Quantity": int, "Items": List[str]},
    total=False,
)


class ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef(
    _ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef
):
    """
    Type definition for `ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfig` `TrustedSigners`

    A complex type that specifies any AWS accounts that you want to permit to create signed
    URLs for private content. If you want the distribution to use signed URLs, include this
    element; if you want the distribution to use public URLs, remove this element. For more
    information, see `Serving Private Content through CloudFront
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
    in the *Amazon CloudFront Developer Guide* .

    - **Enabled** *(boolean) --*

      Specifies whether you want to require viewers to use signed URLs to access the files
      specified by ``PathPattern`` and ``TargetOriginId`` .

    - **Quantity** *(integer) --*

      The number of trusted signers for this cache behavior.

    - **Items** *(list) --*

       **Optional** : A complex type that contains trusted signers for this cache behavior.
       If ``Quantity`` is ``0`` , you can omit ``Items`` .

      - *(string) --*
    """


_ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTypeDef = TypedDict(
    "_ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "S3Origin": ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef,
        "Aliases": ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef,
        "Comment": str,
        "Logging": ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef,
        "TrustedSigners": ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef,
        "PriceClass": str,
        "Enabled": bool,
    },
    total=False,
)


class ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTypeDef(
    _ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTypeDef
):
    """
    Type definition for `ClientGetStreamingDistributionResponseStreamingDistribution` `StreamingDistributionConfig`

    The current configuration information for the RTMP distribution.

    - **CallerReference** *(string) --*

      A unique value (for example, a date-time stamp) that ensures that the request can't be
      replayed.

      If the value of ``CallerReference`` is new (regardless of the content of the
      ``StreamingDistributionConfig`` object), CloudFront creates a new distribution.

      If ``CallerReference`` is a value that you already sent in a previous request to create a
      distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

    - **S3Origin** *(dict) --*

      A complex type that contains information about the Amazon S3 bucket from which you want
      CloudFront to get your media files for distribution.

      - **DomainName** *(string) --*

        The DNS name of the Amazon S3 origin.

      - **OriginAccessIdentity** *(string) --*

        The CloudFront origin access identity to associate with the distribution. Use an origin
        access identity to configure the distribution so that end users can only access objects
        in an Amazon S3 bucket through CloudFront.

        If you want end users to be able to access objects using either the CloudFront URL or
        the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

        To delete the origin access identity from an existing distribution, update the
        distribution configuration and include an empty ``OriginAccessIdentity`` element.

        To replace the origin access identity, update the distribution configuration and
        specify the new origin access identity.

        For more information, see `Using an Origin Access Identity to Restrict Access to Your
        Amazon S3 Content
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
        in the *Amazon CloudFront Developer Guide* .

    - **Aliases** *(dict) --*

      A complex type that contains information about CNAMEs (alternate domain names), if any,
      for this streaming distribution.

      - **Quantity** *(integer) --*

        The number of CNAME aliases, if any, that you want to associate with this distribution.

      - **Items** *(list) --*

        A complex type that contains the CNAME aliases, if any, that you want to associate with
        this distribution.

        - *(string) --*

    - **Comment** *(string) --*

      Any comments you want to include about the streaming distribution.

    - **Logging** *(dict) --*

      A complex type that controls whether access logs are written for the streaming
      distribution.

      - **Enabled** *(boolean) --*

        Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If
        you don't want to enable logging when you create a streaming distribution or if you
        want to disable logging for an existing streaming distribution, specify ``false`` for
        ``Enabled`` , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify
        ``false`` for ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the
        values are automatically deleted.

      - **Bucket** *(string) --*

        The Amazon S3 bucket to store the access logs in, for example,
        ``myawslogbucket.s3.amazonaws.com`` .

      - **Prefix** *(string) --*

        An optional string that you want CloudFront to prefix to the access log filenames for
        this streaming distribution, for example, ``myprefix/`` . If you want to enable
        logging, but you don't want to specify a prefix, you still must include an empty
        ``Prefix`` element in the ``Logging`` element.

    - **TrustedSigners** *(dict) --*

      A complex type that specifies any AWS accounts that you want to permit to create signed
      URLs for private content. If you want the distribution to use signed URLs, include this
      element; if you want the distribution to use public URLs, remove this element. For more
      information, see `Serving Private Content through CloudFront
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
      in the *Amazon CloudFront Developer Guide* .

      - **Enabled** *(boolean) --*

        Specifies whether you want to require viewers to use signed URLs to access the files
        specified by ``PathPattern`` and ``TargetOriginId`` .

      - **Quantity** *(integer) --*

        The number of trusted signers for this cache behavior.

      - **Items** *(list) --*

         **Optional** : A complex type that contains trusted signers for this cache behavior.
         If ``Quantity`` is ``0`` , you can omit ``Items`` .

        - *(string) --*

    - **PriceClass** *(string) --*

      A complex type that contains information about price class for this streaming
      distribution.

    - **Enabled** *(boolean) --*

      Whether the streaming distribution is enabled to accept user requests for content.
    """


_ClientGetStreamingDistributionResponseStreamingDistributionTypeDef = TypedDict(
    "_ClientGetStreamingDistributionResponseStreamingDistributionTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "DomainName": str,
        "ActiveTrustedSigners": ClientGetStreamingDistributionResponseStreamingDistributionActiveTrustedSignersTypeDef,
        "StreamingDistributionConfig": ClientGetStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTypeDef,
    },
    total=False,
)


class ClientGetStreamingDistributionResponseStreamingDistributionTypeDef(
    _ClientGetStreamingDistributionResponseStreamingDistributionTypeDef
):
    """
    Type definition for `ClientGetStreamingDistributionResponse` `StreamingDistribution`

    The streaming distribution's information.

    - **Id** *(string) --*

      The identifier for the RTMP distribution. For example: ``EGTXBD79EXAMPLE`` .

    - **ARN** *(string) --*

      The ARN (Amazon Resource Name) for the distribution. For example:
      ``arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`` , where ``123456789012``
      is your AWS account ID.

    - **Status** *(string) --*

      The current status of the RTMP distribution. When the status is ``Deployed`` , the
      distribution's information is propagated to all CloudFront edge locations.

    - **LastModifiedTime** *(datetime) --*

      The date and time that the distribution was last modified.

    - **DomainName** *(string) --*

      The domain name that corresponds to the streaming distribution, for example,
      ``s5c39gqb8ow64r.cloudfront.net`` .

    - **ActiveTrustedSigners** *(dict) --*

      A complex type that lists the AWS accounts, if any, that you included in the
      ``TrustedSigners`` complex type for this distribution. These are the accounts that you want
      to allow to create signed URLs for private content.

      The ``Signer`` complex type lists the AWS account number of the trusted signer or ``self``
      if the signer is the AWS account that created the distribution. The ``Signer`` element also
      includes the IDs of any active CloudFront key pairs that are associated with the trusted
      signer's AWS account. If no ``KeyPairId`` element appears for a ``Signer`` , that signer
      can't create signed URLs.

      For more information, see `Serving Private Content through CloudFront
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
      in the *Amazon CloudFront Developer Guide* .

      - **Enabled** *(boolean) --*

        Enabled is ``true`` if any of the AWS accounts listed in the ``TrustedSigners`` complex
        type for this distribution have active CloudFront key pairs. If not, ``Enabled`` is
        ``false`` .

      - **Quantity** *(integer) --*

        The number of trusted signers specified in the ``TrustedSigners`` complex type.

      - **Items** *(list) --*

        A complex type that contains one ``Signer`` complex type for each trusted signer that is
        specified in the ``TrustedSigners`` complex type.

        - *(dict) --*

          A complex type that lists the AWS accounts that were included in the ``TrustedSigners``
          complex type, as well as their active CloudFront key pair IDs, if any.

          - **AwsAccountNumber** *(string) --*

            An AWS account that is included in the ``TrustedSigners`` complex type for this
            distribution. Valid values include:

            * ``self`` , which is the AWS account used to create the distribution.

            * An AWS account number.

          - **KeyPairIds** *(dict) --*

            A complex type that lists the active CloudFront key pairs, if any, that are
            associated with ``AwsAccountNumber`` .

            - **Quantity** *(integer) --*

              The number of active CloudFront key pairs for ``AwsAccountNumber`` .

              For more information, see `ActiveTrustedSigners
              <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
              .

            - **Items** *(list) --*

              A complex type that lists the active CloudFront key pairs, if any, that are
              associated with ``AwsAccountNumber`` .

              For more information, see `ActiveTrustedSigners
              <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
              .

              - *(string) --*

    - **StreamingDistributionConfig** *(dict) --*

      The current configuration information for the RTMP distribution.

      - **CallerReference** *(string) --*

        A unique value (for example, a date-time stamp) that ensures that the request can't be
        replayed.

        If the value of ``CallerReference`` is new (regardless of the content of the
        ``StreamingDistributionConfig`` object), CloudFront creates a new distribution.

        If ``CallerReference`` is a value that you already sent in a previous request to create a
        distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

      - **S3Origin** *(dict) --*

        A complex type that contains information about the Amazon S3 bucket from which you want
        CloudFront to get your media files for distribution.

        - **DomainName** *(string) --*

          The DNS name of the Amazon S3 origin.

        - **OriginAccessIdentity** *(string) --*

          The CloudFront origin access identity to associate with the distribution. Use an origin
          access identity to configure the distribution so that end users can only access objects
          in an Amazon S3 bucket through CloudFront.

          If you want end users to be able to access objects using either the CloudFront URL or
          the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

          To delete the origin access identity from an existing distribution, update the
          distribution configuration and include an empty ``OriginAccessIdentity`` element.

          To replace the origin access identity, update the distribution configuration and
          specify the new origin access identity.

          For more information, see `Using an Origin Access Identity to Restrict Access to Your
          Amazon S3 Content
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
          in the *Amazon CloudFront Developer Guide* .

      - **Aliases** *(dict) --*

        A complex type that contains information about CNAMEs (alternate domain names), if any,
        for this streaming distribution.

        - **Quantity** *(integer) --*

          The number of CNAME aliases, if any, that you want to associate with this distribution.

        - **Items** *(list) --*

          A complex type that contains the CNAME aliases, if any, that you want to associate with
          this distribution.

          - *(string) --*

      - **Comment** *(string) --*

        Any comments you want to include about the streaming distribution.

      - **Logging** *(dict) --*

        A complex type that controls whether access logs are written for the streaming
        distribution.

        - **Enabled** *(boolean) --*

          Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If
          you don't want to enable logging when you create a streaming distribution or if you
          want to disable logging for an existing streaming distribution, specify ``false`` for
          ``Enabled`` , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify
          ``false`` for ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the
          values are automatically deleted.

        - **Bucket** *(string) --*

          The Amazon S3 bucket to store the access logs in, for example,
          ``myawslogbucket.s3.amazonaws.com`` .

        - **Prefix** *(string) --*

          An optional string that you want CloudFront to prefix to the access log filenames for
          this streaming distribution, for example, ``myprefix/`` . If you want to enable
          logging, but you don't want to specify a prefix, you still must include an empty
          ``Prefix`` element in the ``Logging`` element.

      - **TrustedSigners** *(dict) --*

        A complex type that specifies any AWS accounts that you want to permit to create signed
        URLs for private content. If you want the distribution to use signed URLs, include this
        element; if you want the distribution to use public URLs, remove this element. For more
        information, see `Serving Private Content through CloudFront
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
        in the *Amazon CloudFront Developer Guide* .

        - **Enabled** *(boolean) --*

          Specifies whether you want to require viewers to use signed URLs to access the files
          specified by ``PathPattern`` and ``TargetOriginId`` .

        - **Quantity** *(integer) --*

          The number of trusted signers for this cache behavior.

        - **Items** *(list) --*

           **Optional** : A complex type that contains trusted signers for this cache behavior.
           If ``Quantity`` is ``0`` , you can omit ``Items`` .

          - *(string) --*

      - **PriceClass** *(string) --*

        A complex type that contains information about price class for this streaming
        distribution.

      - **Enabled** *(boolean) --*

        Whether the streaming distribution is enabled to accept user requests for content.
    """


_ClientGetStreamingDistributionResponseTypeDef = TypedDict(
    "_ClientGetStreamingDistributionResponseTypeDef",
    {
        "StreamingDistribution": ClientGetStreamingDistributionResponseStreamingDistributionTypeDef,
        "ETag": str,
    },
    total=False,
)


class ClientGetStreamingDistributionResponseTypeDef(
    _ClientGetStreamingDistributionResponseTypeDef
):
    """
    Type definition for `ClientGetStreamingDistribution` `Response`

    The returned result of the corresponding request.

    - **StreamingDistribution** *(dict) --*

      The streaming distribution's information.

      - **Id** *(string) --*

        The identifier for the RTMP distribution. For example: ``EGTXBD79EXAMPLE`` .

      - **ARN** *(string) --*

        The ARN (Amazon Resource Name) for the distribution. For example:
        ``arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`` , where ``123456789012``
        is your AWS account ID.

      - **Status** *(string) --*

        The current status of the RTMP distribution. When the status is ``Deployed`` , the
        distribution's information is propagated to all CloudFront edge locations.

      - **LastModifiedTime** *(datetime) --*

        The date and time that the distribution was last modified.

      - **DomainName** *(string) --*

        The domain name that corresponds to the streaming distribution, for example,
        ``s5c39gqb8ow64r.cloudfront.net`` .

      - **ActiveTrustedSigners** *(dict) --*

        A complex type that lists the AWS accounts, if any, that you included in the
        ``TrustedSigners`` complex type for this distribution. These are the accounts that you want
        to allow to create signed URLs for private content.

        The ``Signer`` complex type lists the AWS account number of the trusted signer or ``self``
        if the signer is the AWS account that created the distribution. The ``Signer`` element also
        includes the IDs of any active CloudFront key pairs that are associated with the trusted
        signer's AWS account. If no ``KeyPairId`` element appears for a ``Signer`` , that signer
        can't create signed URLs.

        For more information, see `Serving Private Content through CloudFront
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
        in the *Amazon CloudFront Developer Guide* .

        - **Enabled** *(boolean) --*

          Enabled is ``true`` if any of the AWS accounts listed in the ``TrustedSigners`` complex
          type for this distribution have active CloudFront key pairs. If not, ``Enabled`` is
          ``false`` .

        - **Quantity** *(integer) --*

          The number of trusted signers specified in the ``TrustedSigners`` complex type.

        - **Items** *(list) --*

          A complex type that contains one ``Signer`` complex type for each trusted signer that is
          specified in the ``TrustedSigners`` complex type.

          - *(dict) --*

            A complex type that lists the AWS accounts that were included in the ``TrustedSigners``
            complex type, as well as their active CloudFront key pair IDs, if any.

            - **AwsAccountNumber** *(string) --*

              An AWS account that is included in the ``TrustedSigners`` complex type for this
              distribution. Valid values include:

              * ``self`` , which is the AWS account used to create the distribution.

              * An AWS account number.

            - **KeyPairIds** *(dict) --*

              A complex type that lists the active CloudFront key pairs, if any, that are
              associated with ``AwsAccountNumber`` .

              - **Quantity** *(integer) --*

                The number of active CloudFront key pairs for ``AwsAccountNumber`` .

                For more information, see `ActiveTrustedSigners
                <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
                .

              - **Items** *(list) --*

                A complex type that lists the active CloudFront key pairs, if any, that are
                associated with ``AwsAccountNumber`` .

                For more information, see `ActiveTrustedSigners
                <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
                .

                - *(string) --*

      - **StreamingDistributionConfig** *(dict) --*

        The current configuration information for the RTMP distribution.

        - **CallerReference** *(string) --*

          A unique value (for example, a date-time stamp) that ensures that the request can't be
          replayed.

          If the value of ``CallerReference`` is new (regardless of the content of the
          ``StreamingDistributionConfig`` object), CloudFront creates a new distribution.

          If ``CallerReference`` is a value that you already sent in a previous request to create a
          distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

        - **S3Origin** *(dict) --*

          A complex type that contains information about the Amazon S3 bucket from which you want
          CloudFront to get your media files for distribution.

          - **DomainName** *(string) --*

            The DNS name of the Amazon S3 origin.

          - **OriginAccessIdentity** *(string) --*

            The CloudFront origin access identity to associate with the distribution. Use an origin
            access identity to configure the distribution so that end users can only access objects
            in an Amazon S3 bucket through CloudFront.

            If you want end users to be able to access objects using either the CloudFront URL or
            the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

            To delete the origin access identity from an existing distribution, update the
            distribution configuration and include an empty ``OriginAccessIdentity`` element.

            To replace the origin access identity, update the distribution configuration and
            specify the new origin access identity.

            For more information, see `Using an Origin Access Identity to Restrict Access to Your
            Amazon S3 Content
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
            in the *Amazon CloudFront Developer Guide* .

        - **Aliases** *(dict) --*

          A complex type that contains information about CNAMEs (alternate domain names), if any,
          for this streaming distribution.

          - **Quantity** *(integer) --*

            The number of CNAME aliases, if any, that you want to associate with this distribution.

          - **Items** *(list) --*

            A complex type that contains the CNAME aliases, if any, that you want to associate with
            this distribution.

            - *(string) --*

        - **Comment** *(string) --*

          Any comments you want to include about the streaming distribution.

        - **Logging** *(dict) --*

          A complex type that controls whether access logs are written for the streaming
          distribution.

          - **Enabled** *(boolean) --*

            Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If
            you don't want to enable logging when you create a streaming distribution or if you
            want to disable logging for an existing streaming distribution, specify ``false`` for
            ``Enabled`` , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify
            ``false`` for ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the
            values are automatically deleted.

          - **Bucket** *(string) --*

            The Amazon S3 bucket to store the access logs in, for example,
            ``myawslogbucket.s3.amazonaws.com`` .

          - **Prefix** *(string) --*

            An optional string that you want CloudFront to prefix to the access log filenames for
            this streaming distribution, for example, ``myprefix/`` . If you want to enable
            logging, but you don't want to specify a prefix, you still must include an empty
            ``Prefix`` element in the ``Logging`` element.

        - **TrustedSigners** *(dict) --*

          A complex type that specifies any AWS accounts that you want to permit to create signed
          URLs for private content. If you want the distribution to use signed URLs, include this
          element; if you want the distribution to use public URLs, remove this element. For more
          information, see `Serving Private Content through CloudFront
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
          in the *Amazon CloudFront Developer Guide* .

          - **Enabled** *(boolean) --*

            Specifies whether you want to require viewers to use signed URLs to access the files
            specified by ``PathPattern`` and ``TargetOriginId`` .

          - **Quantity** *(integer) --*

            The number of trusted signers for this cache behavior.

          - **Items** *(list) --*

             **Optional** : A complex type that contains trusted signers for this cache behavior.
             If ``Quantity`` is ``0`` , you can omit ``Items`` .

            - *(string) --*

        - **PriceClass** *(string) --*

          A complex type that contains information about price class for this streaming
          distribution.

        - **Enabled** *(boolean) --*

          Whether the streaming distribution is enabled to accept user requests for content.

    - **ETag** *(string) --*

      The current version of the streaming distribution's information. For example:
      ``E2QWRUHAPOMQZL`` .
    """


_ClientListCloudFrontOriginAccessIdentitiesResponseCloudFrontOriginAccessIdentityListItemsTypeDef = TypedDict(
    "_ClientListCloudFrontOriginAccessIdentitiesResponseCloudFrontOriginAccessIdentityListItemsTypeDef",
    {"Id": str, "S3CanonicalUserId": str, "Comment": str},
    total=False,
)


class ClientListCloudFrontOriginAccessIdentitiesResponseCloudFrontOriginAccessIdentityListItemsTypeDef(
    _ClientListCloudFrontOriginAccessIdentitiesResponseCloudFrontOriginAccessIdentityListItemsTypeDef
):
    """
    Type definition for `ClientListCloudFrontOriginAccessIdentitiesResponseCloudFrontOriginAccessIdentityList` `Items`

    Summary of the information about a CloudFront origin access identity.

    - **Id** *(string) --*

      The ID for the origin access identity. For example: ``E74FTE3AJFJ256A`` .

    - **S3CanonicalUserId** *(string) --*

      The Amazon S3 canonical user ID for the origin access identity, which you use when
      giving the origin access identity read permission to an object in Amazon S3.

    - **Comment** *(string) --*

      The comment for this origin access identity, as originally specified when created.
    """


_ClientListCloudFrontOriginAccessIdentitiesResponseCloudFrontOriginAccessIdentityListTypeDef = TypedDict(
    "_ClientListCloudFrontOriginAccessIdentitiesResponseCloudFrontOriginAccessIdentityListTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
        "Items": List[
            ClientListCloudFrontOriginAccessIdentitiesResponseCloudFrontOriginAccessIdentityListItemsTypeDef
        ],
    },
    total=False,
)


class ClientListCloudFrontOriginAccessIdentitiesResponseCloudFrontOriginAccessIdentityListTypeDef(
    _ClientListCloudFrontOriginAccessIdentitiesResponseCloudFrontOriginAccessIdentityListTypeDef
):
    """
    Type definition for `ClientListCloudFrontOriginAccessIdentitiesResponse` `CloudFrontOriginAccessIdentityList`

    The ``CloudFrontOriginAccessIdentityList`` type.

    - **Marker** *(string) --*

      Use this when paginating results to indicate where to begin in your list of origin access
      identities. The results include identities in the list that occur after the marker. To get
      the next page of results, set the ``Marker`` to the value of the ``NextMarker`` from the
      current page's response (which is also the ID of the last identity on that page).

    - **NextMarker** *(string) --*

      If ``IsTruncated`` is ``true`` , this element is present and contains the value you can use
      for the ``Marker`` request parameter to continue listing your origin access identities
      where they left off.

    - **MaxItems** *(integer) --*

      The maximum number of origin access identities you want in the response body.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether more origin access identities remain to be listed. If your
      results were truncated, you can make a follow-up pagination request using the ``Marker``
      request parameter to retrieve more items in the list.

    - **Quantity** *(integer) --*

      The number of CloudFront origin access identities that were created by the current AWS
      account.

    - **Items** *(list) --*

      A complex type that contains one ``CloudFrontOriginAccessIdentitySummary`` element for each
      origin access identity that was created by the current AWS account.

      - *(dict) --*

        Summary of the information about a CloudFront origin access identity.

        - **Id** *(string) --*

          The ID for the origin access identity. For example: ``E74FTE3AJFJ256A`` .

        - **S3CanonicalUserId** *(string) --*

          The Amazon S3 canonical user ID for the origin access identity, which you use when
          giving the origin access identity read permission to an object in Amazon S3.

        - **Comment** *(string) --*

          The comment for this origin access identity, as originally specified when created.
    """


_ClientListCloudFrontOriginAccessIdentitiesResponseTypeDef = TypedDict(
    "_ClientListCloudFrontOriginAccessIdentitiesResponseTypeDef",
    {
        "CloudFrontOriginAccessIdentityList": ClientListCloudFrontOriginAccessIdentitiesResponseCloudFrontOriginAccessIdentityListTypeDef
    },
    total=False,
)


class ClientListCloudFrontOriginAccessIdentitiesResponseTypeDef(
    _ClientListCloudFrontOriginAccessIdentitiesResponseTypeDef
):
    """
    Type definition for `ClientListCloudFrontOriginAccessIdentities` `Response`

    The returned result of the corresponding request.

    - **CloudFrontOriginAccessIdentityList** *(dict) --*

      The ``CloudFrontOriginAccessIdentityList`` type.

      - **Marker** *(string) --*

        Use this when paginating results to indicate where to begin in your list of origin access
        identities. The results include identities in the list that occur after the marker. To get
        the next page of results, set the ``Marker`` to the value of the ``NextMarker`` from the
        current page's response (which is also the ID of the last identity on that page).

      - **NextMarker** *(string) --*

        If ``IsTruncated`` is ``true`` , this element is present and contains the value you can use
        for the ``Marker`` request parameter to continue listing your origin access identities
        where they left off.

      - **MaxItems** *(integer) --*

        The maximum number of origin access identities you want in the response body.

      - **IsTruncated** *(boolean) --*

        A flag that indicates whether more origin access identities remain to be listed. If your
        results were truncated, you can make a follow-up pagination request using the ``Marker``
        request parameter to retrieve more items in the list.

      - **Quantity** *(integer) --*

        The number of CloudFront origin access identities that were created by the current AWS
        account.

      - **Items** *(list) --*

        A complex type that contains one ``CloudFrontOriginAccessIdentitySummary`` element for each
        origin access identity that was created by the current AWS account.

        - *(dict) --*

          Summary of the information about a CloudFront origin access identity.

          - **Id** *(string) --*

            The ID for the origin access identity. For example: ``E74FTE3AJFJ256A`` .

          - **S3CanonicalUserId** *(string) --*

            The Amazon S3 canonical user ID for the origin access identity, which you use when
            giving the origin access identity read permission to an object in Amazon S3.

          - **Comment** *(string) --*

            The comment for this origin access identity, as originally specified when created.
    """


_ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigContentTypeProfilesItemsTypeDef = TypedDict(
    "_ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigContentTypeProfilesItemsTypeDef",
    {"Format": str, "ProfileId": str, "ContentType": str},
    total=False,
)


class ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigContentTypeProfilesItemsTypeDef(
    _ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigContentTypeProfilesItemsTypeDef
):
    """
    Type definition for `ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigContentTypeProfiles` `Items`

    A field-level encryption content type profile.

    - **Format** *(string) --*

      The format for a field-level encryption content type-profile mapping.

    - **ProfileId** *(string) --*

      The profile ID for a field-level encryption content type-profile mapping.

    - **ContentType** *(string) --*

      The content type for a field-level encryption content type-profile mapping.
    """


_ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigContentTypeProfilesTypeDef = TypedDict(
    "_ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigContentTypeProfilesTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigContentTypeProfilesItemsTypeDef
        ],
    },
    total=False,
)


class ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigContentTypeProfilesTypeDef(
    _ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigContentTypeProfilesTypeDef
):
    """
    Type definition for `ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfig` `ContentTypeProfiles`

    The configuration for a field-level encryption content type-profile.

    - **Quantity** *(integer) --*

      The number of field-level encryption content type-profile mappings.

    - **Items** *(list) --*

      Items in a field-level encryption content type-profile mapping.

      - *(dict) --*

        A field-level encryption content type profile.

        - **Format** *(string) --*

          The format for a field-level encryption content type-profile mapping.

        - **ProfileId** *(string) --*

          The profile ID for a field-level encryption content type-profile mapping.

        - **ContentType** *(string) --*

          The content type for a field-level encryption content type-profile mapping.
    """


_ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigTypeDef = TypedDict(
    "_ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigTypeDef",
    {
        "ForwardWhenContentTypeIsUnknown": bool,
        "ContentTypeProfiles": ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigContentTypeProfilesTypeDef,
    },
    total=False,
)


class ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigTypeDef(
    _ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigTypeDef
):
    """
    Type definition for `ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItems` `ContentTypeProfileConfig`

    A summary of a content type-profile mapping.

    - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

      The setting in a field-level encryption content type-profile mapping that specifies
      what to do when an unknown content type is provided for the profile. If true, content
      is forwarded without being encrypted when the content type is unknown. If false (the
      default), an error is returned when the content type is unknown.

    - **ContentTypeProfiles** *(dict) --*

      The configuration for a field-level encryption content type-profile.

      - **Quantity** *(integer) --*

        The number of field-level encryption content type-profile mappings.

      - **Items** *(list) --*

        Items in a field-level encryption content type-profile mapping.

        - *(dict) --*

          A field-level encryption content type profile.

          - **Format** *(string) --*

            The format for a field-level encryption content type-profile mapping.

          - **ProfileId** *(string) --*

            The profile ID for a field-level encryption content type-profile mapping.

          - **ContentType** *(string) --*

            The content type for a field-level encryption content type-profile mapping.
    """


_ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigQueryArgProfilesItemsTypeDef = TypedDict(
    "_ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigQueryArgProfilesItemsTypeDef",
    {"QueryArg": str, "ProfileId": str},
    total=False,
)


class ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigQueryArgProfilesItemsTypeDef(
    _ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigQueryArgProfilesItemsTypeDef
):
    """
    Type definition for `ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigQueryArgProfiles` `Items`

    Query argument-profile mapping for field-level encryption.

    - **QueryArg** *(string) --*

      Query argument for field-level encryption query argument-profile mapping.

    - **ProfileId** *(string) --*

      ID of profile to use for field-level encryption query argument-profile mapping
    """


_ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigQueryArgProfilesTypeDef = TypedDict(
    "_ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigQueryArgProfilesTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigQueryArgProfilesItemsTypeDef
        ],
    },
    total=False,
)


class ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigQueryArgProfilesTypeDef(
    _ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigQueryArgProfilesTypeDef
):
    """
    Type definition for `ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfig` `QueryArgProfiles`

    Profiles specified for query argument-profile mapping for field-level encryption.

    - **Quantity** *(integer) --*

      Number of profiles for query argument-profile mapping for field-level encryption.

    - **Items** *(list) --*

      Number of items for query argument-profile mapping for field-level encryption.

      - *(dict) --*

        Query argument-profile mapping for field-level encryption.

        - **QueryArg** *(string) --*

          Query argument for field-level encryption query argument-profile mapping.

        - **ProfileId** *(string) --*

          ID of profile to use for field-level encryption query argument-profile mapping
    """


_ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigTypeDef = TypedDict(
    "_ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigTypeDef",
    {
        "ForwardWhenQueryArgProfileIsUnknown": bool,
        "QueryArgProfiles": ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigQueryArgProfilesTypeDef,
    },
    total=False,
)


class ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigTypeDef(
    _ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigTypeDef
):
    """
    Type definition for `ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItems` `QueryArgProfileConfig`

    A summary of a query argument-profile mapping.

    - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

      Flag to set if you want a request to be forwarded to the origin even if the profile
      specified by the field-level encryption query argument, fle-profile, is unknown.

    - **QueryArgProfiles** *(dict) --*

      Profiles specified for query argument-profile mapping for field-level encryption.

      - **Quantity** *(integer) --*

        Number of profiles for query argument-profile mapping for field-level encryption.

      - **Items** *(list) --*

        Number of items for query argument-profile mapping for field-level encryption.

        - *(dict) --*

          Query argument-profile mapping for field-level encryption.

          - **QueryArg** *(string) --*

            Query argument for field-level encryption query argument-profile mapping.

          - **ProfileId** *(string) --*

            ID of profile to use for field-level encryption query argument-profile mapping
    """


_ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsTypeDef = TypedDict(
    "_ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "Comment": str,
        "QueryArgProfileConfig": ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsQueryArgProfileConfigTypeDef,
        "ContentTypeProfileConfig": ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsContentTypeProfileConfigTypeDef,
    },
    total=False,
)


class ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsTypeDef(
    _ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsTypeDef
):
    """
    Type definition for `ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionList` `Items`

    A summary of a field-level encryption item.

    - **Id** *(string) --*

      The unique ID of a field-level encryption item.

    - **LastModifiedTime** *(datetime) --*

      The last time that the summary of field-level encryption items was modified.

    - **Comment** *(string) --*

      An optional comment about the field-level encryption item.

    - **QueryArgProfileConfig** *(dict) --*

      A summary of a query argument-profile mapping.

      - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

        Flag to set if you want a request to be forwarded to the origin even if the profile
        specified by the field-level encryption query argument, fle-profile, is unknown.

      - **QueryArgProfiles** *(dict) --*

        Profiles specified for query argument-profile mapping for field-level encryption.

        - **Quantity** *(integer) --*

          Number of profiles for query argument-profile mapping for field-level encryption.

        - **Items** *(list) --*

          Number of items for query argument-profile mapping for field-level encryption.

          - *(dict) --*

            Query argument-profile mapping for field-level encryption.

            - **QueryArg** *(string) --*

              Query argument for field-level encryption query argument-profile mapping.

            - **ProfileId** *(string) --*

              ID of profile to use for field-level encryption query argument-profile mapping

    - **ContentTypeProfileConfig** *(dict) --*

      A summary of a content type-profile mapping.

      - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

        The setting in a field-level encryption content type-profile mapping that specifies
        what to do when an unknown content type is provided for the profile. If true, content
        is forwarded without being encrypted when the content type is unknown. If false (the
        default), an error is returned when the content type is unknown.

      - **ContentTypeProfiles** *(dict) --*

        The configuration for a field-level encryption content type-profile.

        - **Quantity** *(integer) --*

          The number of field-level encryption content type-profile mappings.

        - **Items** *(list) --*

          Items in a field-level encryption content type-profile mapping.

          - *(dict) --*

            A field-level encryption content type profile.

            - **Format** *(string) --*

              The format for a field-level encryption content type-profile mapping.

            - **ProfileId** *(string) --*

              The profile ID for a field-level encryption content type-profile mapping.

            - **ContentType** *(string) --*

              The content type for a field-level encryption content type-profile mapping.
    """


_ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListTypeDef = TypedDict(
    "_ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListTypeDef",
    {
        "NextMarker": str,
        "MaxItems": int,
        "Quantity": int,
        "Items": List[
            ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListItemsTypeDef
        ],
    },
    total=False,
)


class ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListTypeDef(
    _ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListTypeDef
):
    """
    Type definition for `ClientListFieldLevelEncryptionConfigsResponse` `FieldLevelEncryptionList`

    Returns a list of all field-level encryption configurations that have been created in
    CloudFront for this account.

    - **NextMarker** *(string) --*

      If there are more elements to be listed, this element is present and contains the value
      that you can use for the ``Marker`` request parameter to continue listing your
      configurations where you left off.

    - **MaxItems** *(integer) --*

      The maximum number of elements you want in the response body.

    - **Quantity** *(integer) --*

      The number of field-level encryption items.

    - **Items** *(list) --*

      An array of field-level encryption items.

      - *(dict) --*

        A summary of a field-level encryption item.

        - **Id** *(string) --*

          The unique ID of a field-level encryption item.

        - **LastModifiedTime** *(datetime) --*

          The last time that the summary of field-level encryption items was modified.

        - **Comment** *(string) --*

          An optional comment about the field-level encryption item.

        - **QueryArgProfileConfig** *(dict) --*

          A summary of a query argument-profile mapping.

          - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

            Flag to set if you want a request to be forwarded to the origin even if the profile
            specified by the field-level encryption query argument, fle-profile, is unknown.

          - **QueryArgProfiles** *(dict) --*

            Profiles specified for query argument-profile mapping for field-level encryption.

            - **Quantity** *(integer) --*

              Number of profiles for query argument-profile mapping for field-level encryption.

            - **Items** *(list) --*

              Number of items for query argument-profile mapping for field-level encryption.

              - *(dict) --*

                Query argument-profile mapping for field-level encryption.

                - **QueryArg** *(string) --*

                  Query argument for field-level encryption query argument-profile mapping.

                - **ProfileId** *(string) --*

                  ID of profile to use for field-level encryption query argument-profile mapping

        - **ContentTypeProfileConfig** *(dict) --*

          A summary of a content type-profile mapping.

          - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

            The setting in a field-level encryption content type-profile mapping that specifies
            what to do when an unknown content type is provided for the profile. If true, content
            is forwarded without being encrypted when the content type is unknown. If false (the
            default), an error is returned when the content type is unknown.

          - **ContentTypeProfiles** *(dict) --*

            The configuration for a field-level encryption content type-profile.

            - **Quantity** *(integer) --*

              The number of field-level encryption content type-profile mappings.

            - **Items** *(list) --*

              Items in a field-level encryption content type-profile mapping.

              - *(dict) --*

                A field-level encryption content type profile.

                - **Format** *(string) --*

                  The format for a field-level encryption content type-profile mapping.

                - **ProfileId** *(string) --*

                  The profile ID for a field-level encryption content type-profile mapping.

                - **ContentType** *(string) --*

                  The content type for a field-level encryption content type-profile mapping.
    """


_ClientListFieldLevelEncryptionConfigsResponseTypeDef = TypedDict(
    "_ClientListFieldLevelEncryptionConfigsResponseTypeDef",
    {
        "FieldLevelEncryptionList": ClientListFieldLevelEncryptionConfigsResponseFieldLevelEncryptionListTypeDef
    },
    total=False,
)


class ClientListFieldLevelEncryptionConfigsResponseTypeDef(
    _ClientListFieldLevelEncryptionConfigsResponseTypeDef
):
    """
    Type definition for `ClientListFieldLevelEncryptionConfigs` `Response`

    - **FieldLevelEncryptionList** *(dict) --*

      Returns a list of all field-level encryption configurations that have been created in
      CloudFront for this account.

      - **NextMarker** *(string) --*

        If there are more elements to be listed, this element is present and contains the value
        that you can use for the ``Marker`` request parameter to continue listing your
        configurations where you left off.

      - **MaxItems** *(integer) --*

        The maximum number of elements you want in the response body.

      - **Quantity** *(integer) --*

        The number of field-level encryption items.

      - **Items** *(list) --*

        An array of field-level encryption items.

        - *(dict) --*

          A summary of a field-level encryption item.

          - **Id** *(string) --*

            The unique ID of a field-level encryption item.

          - **LastModifiedTime** *(datetime) --*

            The last time that the summary of field-level encryption items was modified.

          - **Comment** *(string) --*

            An optional comment about the field-level encryption item.

          - **QueryArgProfileConfig** *(dict) --*

            A summary of a query argument-profile mapping.

            - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

              Flag to set if you want a request to be forwarded to the origin even if the profile
              specified by the field-level encryption query argument, fle-profile, is unknown.

            - **QueryArgProfiles** *(dict) --*

              Profiles specified for query argument-profile mapping for field-level encryption.

              - **Quantity** *(integer) --*

                Number of profiles for query argument-profile mapping for field-level encryption.

              - **Items** *(list) --*

                Number of items for query argument-profile mapping for field-level encryption.

                - *(dict) --*

                  Query argument-profile mapping for field-level encryption.

                  - **QueryArg** *(string) --*

                    Query argument for field-level encryption query argument-profile mapping.

                  - **ProfileId** *(string) --*

                    ID of profile to use for field-level encryption query argument-profile mapping

          - **ContentTypeProfileConfig** *(dict) --*

            A summary of a content type-profile mapping.

            - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

              The setting in a field-level encryption content type-profile mapping that specifies
              what to do when an unknown content type is provided for the profile. If true, content
              is forwarded without being encrypted when the content type is unknown. If false (the
              default), an error is returned when the content type is unknown.

            - **ContentTypeProfiles** *(dict) --*

              The configuration for a field-level encryption content type-profile.

              - **Quantity** *(integer) --*

                The number of field-level encryption content type-profile mappings.

              - **Items** *(list) --*

                Items in a field-level encryption content type-profile mapping.

                - *(dict) --*

                  A field-level encryption content type profile.

                  - **Format** *(string) --*

                    The format for a field-level encryption content type-profile mapping.

                  - **ProfileId** *(string) --*

                    The profile ID for a field-level encryption content type-profile mapping.

                  - **ContentType** *(string) --*

                    The content type for a field-level encryption content type-profile mapping.
    """


_ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesItemsFieldPatternsTypeDef = TypedDict(
    "_ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesItemsFieldPatternsTypeDef",
    {"Quantity": int, "Items": List[str]},
    total=False,
)


class ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesItemsFieldPatternsTypeDef(
    _ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesItemsFieldPatternsTypeDef
):
    """
    Type definition for `ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesItems` `FieldPatterns`

    Field patterns in a field-level encryption content type profile specify the
    fields that you want to be encrypted. You can provide the full field name, or any
    beginning characters followed by a wildcard (*). You can't overlap field
    patterns. For example, you can't have both ABC* and AB*. Note that field patterns
    are case-sensitive.

    - **Quantity** *(integer) --*

      The number of field-level encryption field patterns.

    - **Items** *(list) --*

      An array of the field-level encryption field patterns.

      - *(string) --*
    """


_ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesItemsTypeDef = TypedDict(
    "_ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesItemsTypeDef",
    {
        "PublicKeyId": str,
        "ProviderId": str,
        "FieldPatterns": ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesItemsFieldPatternsTypeDef,
    },
    total=False,
)


class ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesItemsTypeDef(
    _ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesItemsTypeDef
):
    """
    Type definition for `ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntities` `Items`

    Complex data type for field-level encryption profiles that includes the encryption
    key and field pattern specifications.

    - **PublicKeyId** *(string) --*

      The public key associated with a set of field-level encryption patterns, to be
      used when encrypting the fields that match the patterns.

    - **ProviderId** *(string) --*

      The provider associated with the public key being used for encryption. This value
      must also be provided with the private key for applications to be able to decrypt
      data.

    - **FieldPatterns** *(dict) --*

      Field patterns in a field-level encryption content type profile specify the
      fields that you want to be encrypted. You can provide the full field name, or any
      beginning characters followed by a wildcard (*). You can't overlap field
      patterns. For example, you can't have both ABC* and AB*. Note that field patterns
      are case-sensitive.

      - **Quantity** *(integer) --*

        The number of field-level encryption field patterns.

      - **Items** *(list) --*

        An array of the field-level encryption field patterns.

        - *(string) --*
    """


_ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesTypeDef = TypedDict(
    "_ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesItemsTypeDef
        ],
    },
    total=False,
)


class ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesTypeDef(
    _ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesTypeDef
):
    """
    Type definition for `ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItems` `EncryptionEntities`

    A complex data type of encryption entities for the field-level encryption profile that
    include the public key ID, provider, and field patterns for specifying which fields to
    encrypt with this key.

    - **Quantity** *(integer) --*

      Number of field pattern items in a field-level encryption content type-profile
      mapping.

    - **Items** *(list) --*

      An array of field patterns in a field-level encryption content type-profile mapping.

      - *(dict) --*

        Complex data type for field-level encryption profiles that includes the encryption
        key and field pattern specifications.

        - **PublicKeyId** *(string) --*

          The public key associated with a set of field-level encryption patterns, to be
          used when encrypting the fields that match the patterns.

        - **ProviderId** *(string) --*

          The provider associated with the public key being used for encryption. This value
          must also be provided with the private key for applications to be able to decrypt
          data.

        - **FieldPatterns** *(dict) --*

          Field patterns in a field-level encryption content type profile specify the
          fields that you want to be encrypted. You can provide the full field name, or any
          beginning characters followed by a wildcard (*). You can't overlap field
          patterns. For example, you can't have both ABC* and AB*. Note that field patterns
          are case-sensitive.

          - **Quantity** *(integer) --*

            The number of field-level encryption field patterns.

          - **Items** *(list) --*

            An array of the field-level encryption field patterns.

            - *(string) --*
    """


_ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsTypeDef = TypedDict(
    "_ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "Name": str,
        "EncryptionEntities": ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsEncryptionEntitiesTypeDef,
        "Comment": str,
    },
    total=False,
)


class ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsTypeDef(
    _ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsTypeDef
):
    """
    Type definition for `ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileList` `Items`

    The field-level encryption profile summary.

    - **Id** *(string) --*

      ID for the field-level encryption profile summary.

    - **LastModifiedTime** *(datetime) --*

      The time when the the field-level encryption profile summary was last updated.

    - **Name** *(string) --*

      Name for the field-level encryption profile summary.

    - **EncryptionEntities** *(dict) --*

      A complex data type of encryption entities for the field-level encryption profile that
      include the public key ID, provider, and field patterns for specifying which fields to
      encrypt with this key.

      - **Quantity** *(integer) --*

        Number of field pattern items in a field-level encryption content type-profile
        mapping.

      - **Items** *(list) --*

        An array of field patterns in a field-level encryption content type-profile mapping.

        - *(dict) --*

          Complex data type for field-level encryption profiles that includes the encryption
          key and field pattern specifications.

          - **PublicKeyId** *(string) --*

            The public key associated with a set of field-level encryption patterns, to be
            used when encrypting the fields that match the patterns.

          - **ProviderId** *(string) --*

            The provider associated with the public key being used for encryption. This value
            must also be provided with the private key for applications to be able to decrypt
            data.

          - **FieldPatterns** *(dict) --*

            Field patterns in a field-level encryption content type profile specify the
            fields that you want to be encrypted. You can provide the full field name, or any
            beginning characters followed by a wildcard (*). You can't overlap field
            patterns. For example, you can't have both ABC* and AB*. Note that field patterns
            are case-sensitive.

            - **Quantity** *(integer) --*

              The number of field-level encryption field patterns.

            - **Items** *(list) --*

              An array of the field-level encryption field patterns.

              - *(string) --*

    - **Comment** *(string) --*

      An optional comment for the field-level encryption profile summary.
    """


_ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListTypeDef = TypedDict(
    "_ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListTypeDef",
    {
        "NextMarker": str,
        "MaxItems": int,
        "Quantity": int,
        "Items": List[
            ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListItemsTypeDef
        ],
    },
    total=False,
)


class ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListTypeDef(
    _ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListTypeDef
):
    """
    Type definition for `ClientListFieldLevelEncryptionProfilesResponse` `FieldLevelEncryptionProfileList`

    Returns a list of the field-level encryption profiles that have been created in CloudFront
    for this account.

    - **NextMarker** *(string) --*

      If there are more elements to be listed, this element is present and contains the value
      that you can use for the ``Marker`` request parameter to continue listing your profiles
      where you left off.

    - **MaxItems** *(integer) --*

      The maximum number of field-level encryption profiles you want in the response body.

    - **Quantity** *(integer) --*

      The number of field-level encryption profiles.

    - **Items** *(list) --*

      The field-level encryption profile items.

      - *(dict) --*

        The field-level encryption profile summary.

        - **Id** *(string) --*

          ID for the field-level encryption profile summary.

        - **LastModifiedTime** *(datetime) --*

          The time when the the field-level encryption profile summary was last updated.

        - **Name** *(string) --*

          Name for the field-level encryption profile summary.

        - **EncryptionEntities** *(dict) --*

          A complex data type of encryption entities for the field-level encryption profile that
          include the public key ID, provider, and field patterns for specifying which fields to
          encrypt with this key.

          - **Quantity** *(integer) --*

            Number of field pattern items in a field-level encryption content type-profile
            mapping.

          - **Items** *(list) --*

            An array of field patterns in a field-level encryption content type-profile mapping.

            - *(dict) --*

              Complex data type for field-level encryption profiles that includes the encryption
              key and field pattern specifications.

              - **PublicKeyId** *(string) --*

                The public key associated with a set of field-level encryption patterns, to be
                used when encrypting the fields that match the patterns.

              - **ProviderId** *(string) --*

                The provider associated with the public key being used for encryption. This value
                must also be provided with the private key for applications to be able to decrypt
                data.

              - **FieldPatterns** *(dict) --*

                Field patterns in a field-level encryption content type profile specify the
                fields that you want to be encrypted. You can provide the full field name, or any
                beginning characters followed by a wildcard (*). You can't overlap field
                patterns. For example, you can't have both ABC* and AB*. Note that field patterns
                are case-sensitive.

                - **Quantity** *(integer) --*

                  The number of field-level encryption field patterns.

                - **Items** *(list) --*

                  An array of the field-level encryption field patterns.

                  - *(string) --*

        - **Comment** *(string) --*

          An optional comment for the field-level encryption profile summary.
    """


_ClientListFieldLevelEncryptionProfilesResponseTypeDef = TypedDict(
    "_ClientListFieldLevelEncryptionProfilesResponseTypeDef",
    {
        "FieldLevelEncryptionProfileList": ClientListFieldLevelEncryptionProfilesResponseFieldLevelEncryptionProfileListTypeDef
    },
    total=False,
)


class ClientListFieldLevelEncryptionProfilesResponseTypeDef(
    _ClientListFieldLevelEncryptionProfilesResponseTypeDef
):
    """
    Type definition for `ClientListFieldLevelEncryptionProfiles` `Response`

    - **FieldLevelEncryptionProfileList** *(dict) --*

      Returns a list of the field-level encryption profiles that have been created in CloudFront
      for this account.

      - **NextMarker** *(string) --*

        If there are more elements to be listed, this element is present and contains the value
        that you can use for the ``Marker`` request parameter to continue listing your profiles
        where you left off.

      - **MaxItems** *(integer) --*

        The maximum number of field-level encryption profiles you want in the response body.

      - **Quantity** *(integer) --*

        The number of field-level encryption profiles.

      - **Items** *(list) --*

        The field-level encryption profile items.

        - *(dict) --*

          The field-level encryption profile summary.

          - **Id** *(string) --*

            ID for the field-level encryption profile summary.

          - **LastModifiedTime** *(datetime) --*

            The time when the the field-level encryption profile summary was last updated.

          - **Name** *(string) --*

            Name for the field-level encryption profile summary.

          - **EncryptionEntities** *(dict) --*

            A complex data type of encryption entities for the field-level encryption profile that
            include the public key ID, provider, and field patterns for specifying which fields to
            encrypt with this key.

            - **Quantity** *(integer) --*

              Number of field pattern items in a field-level encryption content type-profile
              mapping.

            - **Items** *(list) --*

              An array of field patterns in a field-level encryption content type-profile mapping.

              - *(dict) --*

                Complex data type for field-level encryption profiles that includes the encryption
                key and field pattern specifications.

                - **PublicKeyId** *(string) --*

                  The public key associated with a set of field-level encryption patterns, to be
                  used when encrypting the fields that match the patterns.

                - **ProviderId** *(string) --*

                  The provider associated with the public key being used for encryption. This value
                  must also be provided with the private key for applications to be able to decrypt
                  data.

                - **FieldPatterns** *(dict) --*

                  Field patterns in a field-level encryption content type profile specify the
                  fields that you want to be encrypted. You can provide the full field name, or any
                  beginning characters followed by a wildcard (*). You can't overlap field
                  patterns. For example, you can't have both ABC* and AB*. Note that field patterns
                  are case-sensitive.

                  - **Quantity** *(integer) --*

                    The number of field-level encryption field patterns.

                  - **Items** *(list) --*

                    An array of the field-level encryption field patterns.

                    - *(string) --*

          - **Comment** *(string) --*

            An optional comment for the field-level encryption profile summary.
    """


_ClientListInvalidationsResponseInvalidationListItemsTypeDef = TypedDict(
    "_ClientListInvalidationsResponseInvalidationListItemsTypeDef",
    {"Id": str, "CreateTime": datetime, "Status": str},
    total=False,
)


class ClientListInvalidationsResponseInvalidationListItemsTypeDef(
    _ClientListInvalidationsResponseInvalidationListItemsTypeDef
):
    """
    Type definition for `ClientListInvalidationsResponseInvalidationList` `Items`

    A summary of an invalidation request.

    - **Id** *(string) --*

      The unique ID for an invalidation request.

    - **CreateTime** *(datetime) --*

      The time that an invalidation request was created.

    - **Status** *(string) --*

      The status of an invalidation request.
    """


_ClientListInvalidationsResponseInvalidationListTypeDef = TypedDict(
    "_ClientListInvalidationsResponseInvalidationListTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
        "Items": List[ClientListInvalidationsResponseInvalidationListItemsTypeDef],
    },
    total=False,
)


class ClientListInvalidationsResponseInvalidationListTypeDef(
    _ClientListInvalidationsResponseInvalidationListTypeDef
):
    """
    Type definition for `ClientListInvalidationsResponse` `InvalidationList`

    Information about invalidation batches.

    - **Marker** *(string) --*

      The value that you provided for the ``Marker`` request parameter.

    - **NextMarker** *(string) --*

      If ``IsTruncated`` is ``true`` , this element is present and contains the value that you
      can use for the ``Marker`` request parameter to continue listing your invalidation batches
      where they left off.

    - **MaxItems** *(integer) --*

      The value that you provided for the ``MaxItems`` request parameter.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether more invalidation batch requests remain to be listed. If your
      results were truncated, you can make a follow-up pagination request using the ``Marker``
      request parameter to retrieve more invalidation batches in the list.

    - **Quantity** *(integer) --*

      The number of invalidation batches that were created by the current AWS account.

    - **Items** *(list) --*

      A complex type that contains one ``InvalidationSummary`` element for each invalidation
      batch created by the current AWS account.

      - *(dict) --*

        A summary of an invalidation request.

        - **Id** *(string) --*

          The unique ID for an invalidation request.

        - **CreateTime** *(datetime) --*

          The time that an invalidation request was created.

        - **Status** *(string) --*

          The status of an invalidation request.
    """


_ClientListInvalidationsResponseTypeDef = TypedDict(
    "_ClientListInvalidationsResponseTypeDef",
    {"InvalidationList": ClientListInvalidationsResponseInvalidationListTypeDef},
    total=False,
)


class ClientListInvalidationsResponseTypeDef(_ClientListInvalidationsResponseTypeDef):
    """
    Type definition for `ClientListInvalidations` `Response`

    The returned result of the corresponding request.

    - **InvalidationList** *(dict) --*

      Information about invalidation batches.

      - **Marker** *(string) --*

        The value that you provided for the ``Marker`` request parameter.

      - **NextMarker** *(string) --*

        If ``IsTruncated`` is ``true`` , this element is present and contains the value that you
        can use for the ``Marker`` request parameter to continue listing your invalidation batches
        where they left off.

      - **MaxItems** *(integer) --*

        The value that you provided for the ``MaxItems`` request parameter.

      - **IsTruncated** *(boolean) --*

        A flag that indicates whether more invalidation batch requests remain to be listed. If your
        results were truncated, you can make a follow-up pagination request using the ``Marker``
        request parameter to retrieve more invalidation batches in the list.

      - **Quantity** *(integer) --*

        The number of invalidation batches that were created by the current AWS account.

      - **Items** *(list) --*

        A complex type that contains one ``InvalidationSummary`` element for each invalidation
        batch created by the current AWS account.

        - *(dict) --*

          A summary of an invalidation request.

          - **Id** *(string) --*

            The unique ID for an invalidation request.

          - **CreateTime** *(datetime) --*

            The time that an invalidation request was created.

          - **Status** *(string) --*

            The status of an invalidation request.
    """


_ClientListPublicKeysResponsePublicKeyListItemsTypeDef = TypedDict(
    "_ClientListPublicKeysResponsePublicKeyListItemsTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatedTime": datetime,
        "EncodedKey": str,
        "Comment": str,
    },
    total=False,
)


class ClientListPublicKeysResponsePublicKeyListItemsTypeDef(
    _ClientListPublicKeysResponsePublicKeyListItemsTypeDef
):
    """
    Type definition for `ClientListPublicKeysResponsePublicKeyList` `Items`

    A complex data type for public key information.

    - **Id** *(string) --*

      ID for public key information summary.

    - **Name** *(string) --*

      Name for public key information summary.

    - **CreatedTime** *(datetime) --*

      Creation time for public key information summary.

    - **EncodedKey** *(string) --*

      Encoded key for public key information summary.

    - **Comment** *(string) --*

      Comment for public key information summary.
    """


_ClientListPublicKeysResponsePublicKeyListTypeDef = TypedDict(
    "_ClientListPublicKeysResponsePublicKeyListTypeDef",
    {
        "NextMarker": str,
        "MaxItems": int,
        "Quantity": int,
        "Items": List[ClientListPublicKeysResponsePublicKeyListItemsTypeDef],
    },
    total=False,
)


class ClientListPublicKeysResponsePublicKeyListTypeDef(
    _ClientListPublicKeysResponsePublicKeyListTypeDef
):
    """
    Type definition for `ClientListPublicKeysResponse` `PublicKeyList`

    Returns a list of all public keys that have been added to CloudFront for this account.

    - **NextMarker** *(string) --*

      If there are more elements to be listed, this element is present and contains the value
      that you can use for the ``Marker`` request parameter to continue listing your public keys
      where you left off.

    - **MaxItems** *(integer) --*

      The maximum number of public keys you want in the response body.

    - **Quantity** *(integer) --*

      The number of public keys you added to CloudFront to use with features like field-level
      encryption.

    - **Items** *(list) --*

      An array of information about a public key you add to CloudFront to use with features like
      field-level encryption.

      - *(dict) --*

        A complex data type for public key information.

        - **Id** *(string) --*

          ID for public key information summary.

        - **Name** *(string) --*

          Name for public key information summary.

        - **CreatedTime** *(datetime) --*

          Creation time for public key information summary.

        - **EncodedKey** *(string) --*

          Encoded key for public key information summary.

        - **Comment** *(string) --*

          Comment for public key information summary.
    """


_ClientListPublicKeysResponseTypeDef = TypedDict(
    "_ClientListPublicKeysResponseTypeDef",
    {"PublicKeyList": ClientListPublicKeysResponsePublicKeyListTypeDef},
    total=False,
)


class ClientListPublicKeysResponseTypeDef(_ClientListPublicKeysResponseTypeDef):
    """
    Type definition for `ClientListPublicKeys` `Response`

    - **PublicKeyList** *(dict) --*

      Returns a list of all public keys that have been added to CloudFront for this account.

      - **NextMarker** *(string) --*

        If there are more elements to be listed, this element is present and contains the value
        that you can use for the ``Marker`` request parameter to continue listing your public keys
        where you left off.

      - **MaxItems** *(integer) --*

        The maximum number of public keys you want in the response body.

      - **Quantity** *(integer) --*

        The number of public keys you added to CloudFront to use with features like field-level
        encryption.

      - **Items** *(list) --*

        An array of information about a public key you add to CloudFront to use with features like
        field-level encryption.

        - *(dict) --*

          A complex data type for public key information.

          - **Id** *(string) --*

            ID for public key information summary.

          - **Name** *(string) --*

            Name for public key information summary.

          - **CreatedTime** *(datetime) --*

            Creation time for public key information summary.

          - **EncodedKey** *(string) --*

            Encoded key for public key information summary.

          - **Comment** *(string) --*

            Comment for public key information summary.
    """


_ClientListStreamingDistributionsResponseStreamingDistributionListItemsAliasesTypeDef = TypedDict(
    "_ClientListStreamingDistributionsResponseStreamingDistributionListItemsAliasesTypeDef",
    {"Quantity": int, "Items": List[str]},
    total=False,
)


class ClientListStreamingDistributionsResponseStreamingDistributionListItemsAliasesTypeDef(
    _ClientListStreamingDistributionsResponseStreamingDistributionListItemsAliasesTypeDef
):
    """
    Type definition for `ClientListStreamingDistributionsResponseStreamingDistributionListItems` `Aliases`

    A complex type that contains information about CNAMEs (alternate domain names), if any,
    for this streaming distribution.

    - **Quantity** *(integer) --*

      The number of CNAME aliases, if any, that you want to associate with this
      distribution.

    - **Items** *(list) --*

      A complex type that contains the CNAME aliases, if any, that you want to associate
      with this distribution.

      - *(string) --*
    """


_ClientListStreamingDistributionsResponseStreamingDistributionListItemsS3OriginTypeDef = TypedDict(
    "_ClientListStreamingDistributionsResponseStreamingDistributionListItemsS3OriginTypeDef",
    {"DomainName": str, "OriginAccessIdentity": str},
    total=False,
)


class ClientListStreamingDistributionsResponseStreamingDistributionListItemsS3OriginTypeDef(
    _ClientListStreamingDistributionsResponseStreamingDistributionListItemsS3OriginTypeDef
):
    """
    Type definition for `ClientListStreamingDistributionsResponseStreamingDistributionListItems` `S3Origin`

    A complex type that contains information about the Amazon S3 bucket from which you want
    CloudFront to get your media files for distribution.

    - **DomainName** *(string) --*

      The DNS name of the Amazon S3 origin.

    - **OriginAccessIdentity** *(string) --*

      The CloudFront origin access identity to associate with the distribution. Use an
      origin access identity to configure the distribution so that end users can only
      access objects in an Amazon S3 bucket through CloudFront.

      If you want end users to be able to access objects using either the CloudFront URL or
      the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

      To delete the origin access identity from an existing distribution, update the
      distribution configuration and include an empty ``OriginAccessIdentity`` element.

      To replace the origin access identity, update the distribution configuration and
      specify the new origin access identity.

      For more information, see `Using an Origin Access Identity to Restrict Access to Your
      Amazon S3 Content
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
      in the *Amazon CloudFront Developer Guide* .
    """


_ClientListStreamingDistributionsResponseStreamingDistributionListItemsTrustedSignersTypeDef = TypedDict(
    "_ClientListStreamingDistributionsResponseStreamingDistributionListItemsTrustedSignersTypeDef",
    {"Enabled": bool, "Quantity": int, "Items": List[str]},
    total=False,
)


class ClientListStreamingDistributionsResponseStreamingDistributionListItemsTrustedSignersTypeDef(
    _ClientListStreamingDistributionsResponseStreamingDistributionListItemsTrustedSignersTypeDef
):
    """
    Type definition for `ClientListStreamingDistributionsResponseStreamingDistributionListItems` `TrustedSigners`

    A complex type that specifies the AWS accounts, if any, that you want to allow to
    create signed URLs for private content. If you want to require signed URLs in requests
    for objects in the target origin that match the ``PathPattern`` for this cache
    behavior, specify ``true`` for ``Enabled`` , and specify the applicable values for
    ``Quantity`` and ``Items`` .If you don't want to require signed URLs in requests for
    objects that match ``PathPattern`` , specify ``false`` for ``Enabled`` and ``0`` for
    ``Quantity`` . Omit ``Items`` . To add, change, or remove one or more trusted signers,
    change ``Enabled`` to ``true`` (if it's currently ``false`` ), change ``Quantity`` as
    applicable, and specify all of the trusted signers that you want to include in the
    updated distribution.

    For more information, see `Serving Private Content through CloudFront
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
    in the *Amazon CloudFront Developer Guide* .

    - **Enabled** *(boolean) --*

      Specifies whether you want to require viewers to use signed URLs to access the files
      specified by ``PathPattern`` and ``TargetOriginId`` .

    - **Quantity** *(integer) --*

      The number of trusted signers for this cache behavior.

    - **Items** *(list) --*

       **Optional** : A complex type that contains trusted signers for this cache behavior.
       If ``Quantity`` is ``0`` , you can omit ``Items`` .

      - *(string) --*
    """


_ClientListStreamingDistributionsResponseStreamingDistributionListItemsTypeDef = TypedDict(
    "_ClientListStreamingDistributionsResponseStreamingDistributionListItemsTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "DomainName": str,
        "S3Origin": ClientListStreamingDistributionsResponseStreamingDistributionListItemsS3OriginTypeDef,
        "Aliases": ClientListStreamingDistributionsResponseStreamingDistributionListItemsAliasesTypeDef,
        "TrustedSigners": ClientListStreamingDistributionsResponseStreamingDistributionListItemsTrustedSignersTypeDef,
        "Comment": str,
        "PriceClass": str,
        "Enabled": bool,
    },
    total=False,
)


class ClientListStreamingDistributionsResponseStreamingDistributionListItemsTypeDef(
    _ClientListStreamingDistributionsResponseStreamingDistributionListItemsTypeDef
):
    """
    Type definition for `ClientListStreamingDistributionsResponseStreamingDistributionList` `Items`

    A summary of the information for a CloudFront streaming distribution.

    - **Id** *(string) --*

      The identifier for the distribution, for example, ``EDFDVBD632BHDS5`` .

    - **ARN** *(string) --*

      The ARN (Amazon Resource Name) for the streaming distribution. For example:
      ``arn:aws:cloudfront::123456789012:streaming-distribution/EDFDVBD632BHDS5`` , where
      ``123456789012`` is your AWS account ID.

    - **Status** *(string) --*

      Indicates the current status of the distribution. When the status is ``Deployed`` , the
      distribution's information is fully propagated throughout the Amazon CloudFront system.

    - **LastModifiedTime** *(datetime) --*

      The date and time the distribution was last modified.

    - **DomainName** *(string) --*

      The domain name corresponding to the distribution, for example,
      ``d111111abcdef8.cloudfront.net`` .

    - **S3Origin** *(dict) --*

      A complex type that contains information about the Amazon S3 bucket from which you want
      CloudFront to get your media files for distribution.

      - **DomainName** *(string) --*

        The DNS name of the Amazon S3 origin.

      - **OriginAccessIdentity** *(string) --*

        The CloudFront origin access identity to associate with the distribution. Use an
        origin access identity to configure the distribution so that end users can only
        access objects in an Amazon S3 bucket through CloudFront.

        If you want end users to be able to access objects using either the CloudFront URL or
        the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

        To delete the origin access identity from an existing distribution, update the
        distribution configuration and include an empty ``OriginAccessIdentity`` element.

        To replace the origin access identity, update the distribution configuration and
        specify the new origin access identity.

        For more information, see `Using an Origin Access Identity to Restrict Access to Your
        Amazon S3 Content
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
        in the *Amazon CloudFront Developer Guide* .

    - **Aliases** *(dict) --*

      A complex type that contains information about CNAMEs (alternate domain names), if any,
      for this streaming distribution.

      - **Quantity** *(integer) --*

        The number of CNAME aliases, if any, that you want to associate with this
        distribution.

      - **Items** *(list) --*

        A complex type that contains the CNAME aliases, if any, that you want to associate
        with this distribution.

        - *(string) --*

    - **TrustedSigners** *(dict) --*

      A complex type that specifies the AWS accounts, if any, that you want to allow to
      create signed URLs for private content. If you want to require signed URLs in requests
      for objects in the target origin that match the ``PathPattern`` for this cache
      behavior, specify ``true`` for ``Enabled`` , and specify the applicable values for
      ``Quantity`` and ``Items`` .If you don't want to require signed URLs in requests for
      objects that match ``PathPattern`` , specify ``false`` for ``Enabled`` and ``0`` for
      ``Quantity`` . Omit ``Items`` . To add, change, or remove one or more trusted signers,
      change ``Enabled`` to ``true`` (if it's currently ``false`` ), change ``Quantity`` as
      applicable, and specify all of the trusted signers that you want to include in the
      updated distribution.

      For more information, see `Serving Private Content through CloudFront
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
      in the *Amazon CloudFront Developer Guide* .

      - **Enabled** *(boolean) --*

        Specifies whether you want to require viewers to use signed URLs to access the files
        specified by ``PathPattern`` and ``TargetOriginId`` .

      - **Quantity** *(integer) --*

        The number of trusted signers for this cache behavior.

      - **Items** *(list) --*

         **Optional** : A complex type that contains trusted signers for this cache behavior.
         If ``Quantity`` is ``0`` , you can omit ``Items`` .

        - *(string) --*

    - **Comment** *(string) --*

      The comment originally specified when this distribution was created.

    - **PriceClass** *(string) --*

      A complex type that contains information about price class for this streaming
      distribution.

    - **Enabled** *(boolean) --*

      Whether the distribution is enabled to accept end user requests for content.
    """


_ClientListStreamingDistributionsResponseStreamingDistributionListTypeDef = TypedDict(
    "_ClientListStreamingDistributionsResponseStreamingDistributionListTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
        "Items": List[
            ClientListStreamingDistributionsResponseStreamingDistributionListItemsTypeDef
        ],
    },
    total=False,
)


class ClientListStreamingDistributionsResponseStreamingDistributionListTypeDef(
    _ClientListStreamingDistributionsResponseStreamingDistributionListTypeDef
):
    """
    Type definition for `ClientListStreamingDistributionsResponse` `StreamingDistributionList`

    The ``StreamingDistributionList`` type.

    - **Marker** *(string) --*

      The value you provided for the ``Marker`` request parameter.

    - **NextMarker** *(string) --*

      If ``IsTruncated`` is ``true`` , this element is present and contains the value you can use
      for the ``Marker`` request parameter to continue listing your RTMP distributions where they
      left off.

    - **MaxItems** *(integer) --*

      The value you provided for the ``MaxItems`` request parameter.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether more streaming distributions remain to be listed. If your
      results were truncated, you can make a follow-up pagination request using the ``Marker``
      request parameter to retrieve more distributions in the list.

    - **Quantity** *(integer) --*

      The number of streaming distributions that were created by the current AWS account.

    - **Items** *(list) --*

      A complex type that contains one ``StreamingDistributionSummary`` element for each
      distribution that was created by the current AWS account.

      - *(dict) --*

        A summary of the information for a CloudFront streaming distribution.

        - **Id** *(string) --*

          The identifier for the distribution, for example, ``EDFDVBD632BHDS5`` .

        - **ARN** *(string) --*

          The ARN (Amazon Resource Name) for the streaming distribution. For example:
          ``arn:aws:cloudfront::123456789012:streaming-distribution/EDFDVBD632BHDS5`` , where
          ``123456789012`` is your AWS account ID.

        - **Status** *(string) --*

          Indicates the current status of the distribution. When the status is ``Deployed`` , the
          distribution's information is fully propagated throughout the Amazon CloudFront system.

        - **LastModifiedTime** *(datetime) --*

          The date and time the distribution was last modified.

        - **DomainName** *(string) --*

          The domain name corresponding to the distribution, for example,
          ``d111111abcdef8.cloudfront.net`` .

        - **S3Origin** *(dict) --*

          A complex type that contains information about the Amazon S3 bucket from which you want
          CloudFront to get your media files for distribution.

          - **DomainName** *(string) --*

            The DNS name of the Amazon S3 origin.

          - **OriginAccessIdentity** *(string) --*

            The CloudFront origin access identity to associate with the distribution. Use an
            origin access identity to configure the distribution so that end users can only
            access objects in an Amazon S3 bucket through CloudFront.

            If you want end users to be able to access objects using either the CloudFront URL or
            the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

            To delete the origin access identity from an existing distribution, update the
            distribution configuration and include an empty ``OriginAccessIdentity`` element.

            To replace the origin access identity, update the distribution configuration and
            specify the new origin access identity.

            For more information, see `Using an Origin Access Identity to Restrict Access to Your
            Amazon S3 Content
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
            in the *Amazon CloudFront Developer Guide* .

        - **Aliases** *(dict) --*

          A complex type that contains information about CNAMEs (alternate domain names), if any,
          for this streaming distribution.

          - **Quantity** *(integer) --*

            The number of CNAME aliases, if any, that you want to associate with this
            distribution.

          - **Items** *(list) --*

            A complex type that contains the CNAME aliases, if any, that you want to associate
            with this distribution.

            - *(string) --*

        - **TrustedSigners** *(dict) --*

          A complex type that specifies the AWS accounts, if any, that you want to allow to
          create signed URLs for private content. If you want to require signed URLs in requests
          for objects in the target origin that match the ``PathPattern`` for this cache
          behavior, specify ``true`` for ``Enabled`` , and specify the applicable values for
          ``Quantity`` and ``Items`` .If you don't want to require signed URLs in requests for
          objects that match ``PathPattern`` , specify ``false`` for ``Enabled`` and ``0`` for
          ``Quantity`` . Omit ``Items`` . To add, change, or remove one or more trusted signers,
          change ``Enabled`` to ``true`` (if it's currently ``false`` ), change ``Quantity`` as
          applicable, and specify all of the trusted signers that you want to include in the
          updated distribution.

          For more information, see `Serving Private Content through CloudFront
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
          in the *Amazon CloudFront Developer Guide* .

          - **Enabled** *(boolean) --*

            Specifies whether you want to require viewers to use signed URLs to access the files
            specified by ``PathPattern`` and ``TargetOriginId`` .

          - **Quantity** *(integer) --*

            The number of trusted signers for this cache behavior.

          - **Items** *(list) --*

             **Optional** : A complex type that contains trusted signers for this cache behavior.
             If ``Quantity`` is ``0`` , you can omit ``Items`` .

            - *(string) --*

        - **Comment** *(string) --*

          The comment originally specified when this distribution was created.

        - **PriceClass** *(string) --*

          A complex type that contains information about price class for this streaming
          distribution.

        - **Enabled** *(boolean) --*

          Whether the distribution is enabled to accept end user requests for content.
    """


_ClientListStreamingDistributionsResponseTypeDef = TypedDict(
    "_ClientListStreamingDistributionsResponseTypeDef",
    {
        "StreamingDistributionList": ClientListStreamingDistributionsResponseStreamingDistributionListTypeDef
    },
    total=False,
)


class ClientListStreamingDistributionsResponseTypeDef(
    _ClientListStreamingDistributionsResponseTypeDef
):
    """
    Type definition for `ClientListStreamingDistributions` `Response`

    The returned result of the corresponding request.

    - **StreamingDistributionList** *(dict) --*

      The ``StreamingDistributionList`` type.

      - **Marker** *(string) --*

        The value you provided for the ``Marker`` request parameter.

      - **NextMarker** *(string) --*

        If ``IsTruncated`` is ``true`` , this element is present and contains the value you can use
        for the ``Marker`` request parameter to continue listing your RTMP distributions where they
        left off.

      - **MaxItems** *(integer) --*

        The value you provided for the ``MaxItems`` request parameter.

      - **IsTruncated** *(boolean) --*

        A flag that indicates whether more streaming distributions remain to be listed. If your
        results were truncated, you can make a follow-up pagination request using the ``Marker``
        request parameter to retrieve more distributions in the list.

      - **Quantity** *(integer) --*

        The number of streaming distributions that were created by the current AWS account.

      - **Items** *(list) --*

        A complex type that contains one ``StreamingDistributionSummary`` element for each
        distribution that was created by the current AWS account.

        - *(dict) --*

          A summary of the information for a CloudFront streaming distribution.

          - **Id** *(string) --*

            The identifier for the distribution, for example, ``EDFDVBD632BHDS5`` .

          - **ARN** *(string) --*

            The ARN (Amazon Resource Name) for the streaming distribution. For example:
            ``arn:aws:cloudfront::123456789012:streaming-distribution/EDFDVBD632BHDS5`` , where
            ``123456789012`` is your AWS account ID.

          - **Status** *(string) --*

            Indicates the current status of the distribution. When the status is ``Deployed`` , the
            distribution's information is fully propagated throughout the Amazon CloudFront system.

          - **LastModifiedTime** *(datetime) --*

            The date and time the distribution was last modified.

          - **DomainName** *(string) --*

            The domain name corresponding to the distribution, for example,
            ``d111111abcdef8.cloudfront.net`` .

          - **S3Origin** *(dict) --*

            A complex type that contains information about the Amazon S3 bucket from which you want
            CloudFront to get your media files for distribution.

            - **DomainName** *(string) --*

              The DNS name of the Amazon S3 origin.

            - **OriginAccessIdentity** *(string) --*

              The CloudFront origin access identity to associate with the distribution. Use an
              origin access identity to configure the distribution so that end users can only
              access objects in an Amazon S3 bucket through CloudFront.

              If you want end users to be able to access objects using either the CloudFront URL or
              the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

              To delete the origin access identity from an existing distribution, update the
              distribution configuration and include an empty ``OriginAccessIdentity`` element.

              To replace the origin access identity, update the distribution configuration and
              specify the new origin access identity.

              For more information, see `Using an Origin Access Identity to Restrict Access to Your
              Amazon S3 Content
              <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
              in the *Amazon CloudFront Developer Guide* .

          - **Aliases** *(dict) --*

            A complex type that contains information about CNAMEs (alternate domain names), if any,
            for this streaming distribution.

            - **Quantity** *(integer) --*

              The number of CNAME aliases, if any, that you want to associate with this
              distribution.

            - **Items** *(list) --*

              A complex type that contains the CNAME aliases, if any, that you want to associate
              with this distribution.

              - *(string) --*

          - **TrustedSigners** *(dict) --*

            A complex type that specifies the AWS accounts, if any, that you want to allow to
            create signed URLs for private content. If you want to require signed URLs in requests
            for objects in the target origin that match the ``PathPattern`` for this cache
            behavior, specify ``true`` for ``Enabled`` , and specify the applicable values for
            ``Quantity`` and ``Items`` .If you don't want to require signed URLs in requests for
            objects that match ``PathPattern`` , specify ``false`` for ``Enabled`` and ``0`` for
            ``Quantity`` . Omit ``Items`` . To add, change, or remove one or more trusted signers,
            change ``Enabled`` to ``true`` (if it's currently ``false`` ), change ``Quantity`` as
            applicable, and specify all of the trusted signers that you want to include in the
            updated distribution.

            For more information, see `Serving Private Content through CloudFront
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
            in the *Amazon CloudFront Developer Guide* .

            - **Enabled** *(boolean) --*

              Specifies whether you want to require viewers to use signed URLs to access the files
              specified by ``PathPattern`` and ``TargetOriginId`` .

            - **Quantity** *(integer) --*

              The number of trusted signers for this cache behavior.

            - **Items** *(list) --*

               **Optional** : A complex type that contains trusted signers for this cache behavior.
               If ``Quantity`` is ``0`` , you can omit ``Items`` .

              - *(string) --*

          - **Comment** *(string) --*

            The comment originally specified when this distribution was created.

          - **PriceClass** *(string) --*

            A complex type that contains information about price class for this streaming
            distribution.

          - **Enabled** *(boolean) --*

            Whether the distribution is enabled to accept end user requests for content.
    """


_ClientListTagsForResourceResponseTagsItemsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsItemsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseTagsItemsTypeDef(
    _ClientListTagsForResourceResponseTagsItemsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponseTags` `Items`

    A complex type that contains ``Tag`` key and ``Tag`` value.

    - **Key** *(string) --*

      A string that contains ``Tag`` key.

      The string length should be between 1 and 128 characters. Valid characters include
      ``a-z`` , ``A-Z`` , ``0-9`` , space, and the special characters ``_ - . : / = + @`` .

    - **Value** *(string) --*

      A string that contains an optional ``Tag`` value.

      The string length should be between 0 and 256 characters. Valid characters include
      ``a-z`` , ``A-Z`` , ``0-9`` , space, and the special characters ``_ - . : / = + @`` .
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef",
    {"Items": List[ClientListTagsForResourceResponseTagsItemsTypeDef]},
    total=False,
)


class ClientListTagsForResourceResponseTagsTypeDef(
    _ClientListTagsForResourceResponseTagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `Tags`

    A complex type that contains zero or more ``Tag`` elements.

    - **Items** *(list) --*

      A complex type that contains ``Tag`` elements.

      - *(dict) --*

        A complex type that contains ``Tag`` key and ``Tag`` value.

        - **Key** *(string) --*

          A string that contains ``Tag`` key.

          The string length should be between 1 and 128 characters. Valid characters include
          ``a-z`` , ``A-Z`` , ``0-9`` , space, and the special characters ``_ - . : / = + @`` .

        - **Value** *(string) --*

          A string that contains an optional ``Tag`` value.

          The string length should be between 0 and 256 characters. Valid characters include
          ``a-z`` , ``A-Z`` , ``0-9`` , space, and the special characters ``_ - . : / = + @`` .
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": ClientListTagsForResourceResponseTagsTypeDef},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    The returned result of the corresponding request.

    - **Tags** *(dict) --*

      A complex type that contains zero or more ``Tag`` elements.

      - **Items** *(list) --*

        A complex type that contains ``Tag`` elements.

        - *(dict) --*

          A complex type that contains ``Tag`` key and ``Tag`` value.

          - **Key** *(string) --*

            A string that contains ``Tag`` key.

            The string length should be between 1 and 128 characters. Valid characters include
            ``a-z`` , ``A-Z`` , ``0-9`` , space, and the special characters ``_ - . : / = + @`` .

          - **Value** *(string) --*

            A string that contains an optional ``Tag`` value.

            The string length should be between 0 and 256 characters. Valid characters include
            ``a-z`` , ``A-Z`` , ``0-9`` , space, and the special characters ``_ - . : / = + @`` .
    """


_RequiredClientTagResourceTagsItemsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsItemsTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagsItemsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsItemsTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagsItemsTypeDef(
    _RequiredClientTagResourceTagsItemsTypeDef,
    _OptionalClientTagResourceTagsItemsTypeDef,
):
    """
    Type definition for `ClientTagResourceTags` `Items`

    A complex type that contains ``Tag`` key and ``Tag`` value.

    - **Key** *(string) --* **[REQUIRED]**

      A string that contains ``Tag`` key.

      The string length should be between 1 and 128 characters. Valid characters include ``a-z``
      , ``A-Z`` , ``0-9`` , space, and the special characters ``_ - . : / = + @`` .

    - **Value** *(string) --*

      A string that contains an optional ``Tag`` value.

      The string length should be between 0 and 256 characters. Valid characters include ``a-z``
      , ``A-Z`` , ``0-9`` , space, and the special characters ``_ - . : / = + @`` .
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef",
    {"Items": List[ClientTagResourceTagsItemsTypeDef]},
    total=False,
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    A complex type that contains zero or more ``Tag`` elements.

    - **Items** *(list) --*

      A complex type that contains ``Tag`` elements.

      - *(dict) --*

        A complex type that contains ``Tag`` key and ``Tag`` value.

        - **Key** *(string) --* **[REQUIRED]**

          A string that contains ``Tag`` key.

          The string length should be between 1 and 128 characters. Valid characters include ``a-z``
          , ``A-Z`` , ``0-9`` , space, and the special characters ``_ - . : / = + @`` .

        - **Value** *(string) --*

          A string that contains an optional ``Tag`` value.

          The string length should be between 0 and 256 characters. Valid characters include ``a-z``
          , ``A-Z`` , ``0-9`` , space, and the special characters ``_ - . : / = + @`` .
    """


_ClientUntagResourceTagKeysTypeDef = TypedDict(
    "_ClientUntagResourceTagKeysTypeDef", {"Items": List[str]}, total=False
)


class ClientUntagResourceTagKeysTypeDef(_ClientUntagResourceTagKeysTypeDef):
    """
    Type definition for `ClientUntagResource` `TagKeys`

    A complex type that contains zero or more ``Tag`` key elements.

    - **Items** *(list) --*

      A complex type that contains ``Tag`` key elements.

      - *(string) --*

        A string that contains ``Tag`` key.

        The string length should be between 1 and 128 characters. Valid characters include ``a-z`` ,
        ``A-Z`` , ``0-9`` , space, and the special characters ``_ - . : / = + @`` .
    """


_ClientUpdateCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef = TypedDict(
    "_ClientUpdateCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef",
    {"CallerReference": str, "Comment": str},
)


class ClientUpdateCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef(
    _ClientUpdateCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef
):
    """
    Type definition for `ClientUpdateCloudFrontOriginAccessIdentity` `CloudFrontOriginAccessIdentityConfig`

    The identity's configuration information.

    - **CallerReference** *(string) --* **[REQUIRED]**

      A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.

      If the value of ``CallerReference`` is new (regardless of the content of the
      ``CloudFrontOriginAccessIdentityConfig`` object), a new origin access identity is created.

      If the ``CallerReference`` is a value already sent in a previous identity request, and the
      content of the ``CloudFrontOriginAccessIdentityConfig`` is identical to the original request
      (ignoring white space), the response includes the same information returned to the original
      request.

      If the ``CallerReference`` is a value you already sent in a previous request to create an
      identity, but the content of the ``CloudFrontOriginAccessIdentityConfig`` is different from the
      original request, CloudFront returns a ``CloudFrontOriginAccessIdentityAlreadyExists`` error.

    - **Comment** *(string) --* **[REQUIRED]**

      Any comments you want to include about the origin access identity.
    """


_ClientUpdateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef = TypedDict(
    "_ClientUpdateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef",
    {"CallerReference": str, "Comment": str},
    total=False,
)


class ClientUpdateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef(
    _ClientUpdateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef
):
    """
    Type definition for `ClientUpdateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentity` `CloudFrontOriginAccessIdentityConfig`

    The current configuration information for the identity.

    - **CallerReference** *(string) --*

      A unique value (for example, a date-time stamp) that ensures that the request can't be
      replayed.

      If the value of ``CallerReference`` is new (regardless of the content of the
      ``CloudFrontOriginAccessIdentityConfig`` object), a new origin access identity is created.

      If the ``CallerReference`` is a value already sent in a previous identity request, and
      the content of the ``CloudFrontOriginAccessIdentityConfig`` is identical to the original
      request (ignoring white space), the response includes the same information returned to
      the original request.

      If the ``CallerReference`` is a value you already sent in a previous request to create an
      identity, but the content of the ``CloudFrontOriginAccessIdentityConfig`` is different
      from the original request, CloudFront returns a
      ``CloudFrontOriginAccessIdentityAlreadyExists`` error.

    - **Comment** *(string) --*

      Any comments you want to include about the origin access identity.
    """


_ClientUpdateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityTypeDef = TypedDict(
    "_ClientUpdateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityTypeDef",
    {
        "Id": str,
        "S3CanonicalUserId": str,
        "CloudFrontOriginAccessIdentityConfig": ClientUpdateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfigTypeDef,
    },
    total=False,
)


class ClientUpdateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityTypeDef(
    _ClientUpdateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityTypeDef
):
    """
    Type definition for `ClientUpdateCloudFrontOriginAccessIdentityResponse` `CloudFrontOriginAccessIdentity`

    The origin access identity's information.

    - **Id** *(string) --*

      The ID for the origin access identity, for example, ``E74FTE3AJFJ256A`` .

    - **S3CanonicalUserId** *(string) --*

      The Amazon S3 canonical user ID for the origin access identity, used when giving the origin
      access identity read permission to an object in Amazon S3.

    - **CloudFrontOriginAccessIdentityConfig** *(dict) --*

      The current configuration information for the identity.

      - **CallerReference** *(string) --*

        A unique value (for example, a date-time stamp) that ensures that the request can't be
        replayed.

        If the value of ``CallerReference`` is new (regardless of the content of the
        ``CloudFrontOriginAccessIdentityConfig`` object), a new origin access identity is created.

        If the ``CallerReference`` is a value already sent in a previous identity request, and
        the content of the ``CloudFrontOriginAccessIdentityConfig`` is identical to the original
        request (ignoring white space), the response includes the same information returned to
        the original request.

        If the ``CallerReference`` is a value you already sent in a previous request to create an
        identity, but the content of the ``CloudFrontOriginAccessIdentityConfig`` is different
        from the original request, CloudFront returns a
        ``CloudFrontOriginAccessIdentityAlreadyExists`` error.

      - **Comment** *(string) --*

        Any comments you want to include about the origin access identity.
    """


_ClientUpdateCloudFrontOriginAccessIdentityResponseTypeDef = TypedDict(
    "_ClientUpdateCloudFrontOriginAccessIdentityResponseTypeDef",
    {
        "CloudFrontOriginAccessIdentity": ClientUpdateCloudFrontOriginAccessIdentityResponseCloudFrontOriginAccessIdentityTypeDef,
        "ETag": str,
    },
    total=False,
)


class ClientUpdateCloudFrontOriginAccessIdentityResponseTypeDef(
    _ClientUpdateCloudFrontOriginAccessIdentityResponseTypeDef
):
    """
    Type definition for `ClientUpdateCloudFrontOriginAccessIdentity` `Response`

    The returned result of the corresponding request.

    - **CloudFrontOriginAccessIdentity** *(dict) --*

      The origin access identity's information.

      - **Id** *(string) --*

        The ID for the origin access identity, for example, ``E74FTE3AJFJ256A`` .

      - **S3CanonicalUserId** *(string) --*

        The Amazon S3 canonical user ID for the origin access identity, used when giving the origin
        access identity read permission to an object in Amazon S3.

      - **CloudFrontOriginAccessIdentityConfig** *(dict) --*

        The current configuration information for the identity.

        - **CallerReference** *(string) --*

          A unique value (for example, a date-time stamp) that ensures that the request can't be
          replayed.

          If the value of ``CallerReference`` is new (regardless of the content of the
          ``CloudFrontOriginAccessIdentityConfig`` object), a new origin access identity is created.

          If the ``CallerReference`` is a value already sent in a previous identity request, and
          the content of the ``CloudFrontOriginAccessIdentityConfig`` is identical to the original
          request (ignoring white space), the response includes the same information returned to
          the original request.

          If the ``CallerReference`` is a value you already sent in a previous request to create an
          identity, but the content of the ``CloudFrontOriginAccessIdentityConfig`` is different
          from the original request, CloudFront returns a
          ``CloudFrontOriginAccessIdentityAlreadyExists`` error.

        - **Comment** *(string) --*

          Any comments you want to include about the origin access identity.

    - **ETag** *(string) --*

      The current version of the configuration. For example: ``E2QWRUHAPOMQZL`` .
    """


_RequiredClientUpdateDistributionDistributionConfigAliasesTypeDef = TypedDict(
    "_RequiredClientUpdateDistributionDistributionConfigAliasesTypeDef",
    {"Quantity": int},
)
_OptionalClientUpdateDistributionDistributionConfigAliasesTypeDef = TypedDict(
    "_OptionalClientUpdateDistributionDistributionConfigAliasesTypeDef",
    {"Items": List[str]},
    total=False,
)


class ClientUpdateDistributionDistributionConfigAliasesTypeDef(
    _RequiredClientUpdateDistributionDistributionConfigAliasesTypeDef,
    _OptionalClientUpdateDistributionDistributionConfigAliasesTypeDef,
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfig` `Aliases`

    A complex type that contains information about CNAMEs (alternate domain names), if any, for
    this distribution.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of CNAME aliases, if any, that you want to associate with this distribution.

    - **Items** *(list) --*

      A complex type that contains the CNAME aliases, if any, that you want to associate with this
      distribution.

      - *(string) --*
    """


_RequiredClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef = TypedDict(
    "_RequiredClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef",
    {"Quantity": int},
)
_OptionalClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef = TypedDict(
    "_OptionalClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef",
    {"Items": List[str]},
    total=False,
)


class ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef(
    _RequiredClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef,
    _OptionalClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef,
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies` `WhitelistedNames`

    Required if you specify ``whitelist`` for the value of ``Forward:`` . A complex type that
    specifies how many different cookies you want CloudFront to forward to the origin for
    this cache behavior and, if you want to forward selected cookies, the names of those
    cookies.

    If you specify ``all`` or none for the value of ``Forward`` , omit ``WhitelistedNames`` .
    If you change the value of ``Forward`` from ``whitelist`` to all or none and you don't
    delete the ``WhitelistedNames`` element and its child elements, CloudFront deletes them
    automatically.

    For the current limit on the number of cookie names that you can whitelist for each cache
    behavior, see `CloudFront Limits
    <https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront>`__
    in the *AWS General Reference* .

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of different cookies that you want CloudFront to forward to the origin for
      this cache behavior.

    - **Items** *(list) --*

      A complex type that contains one ``Name`` element for each cookie that you want
      CloudFront to forward to the origin for this cache behavior.

      - *(string) --*
    """


_RequiredClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef = TypedDict(
    "_RequiredClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef",
    {"Forward": str},
)
_OptionalClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef = TypedDict(
    "_OptionalClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef",
    {
        "WhitelistedNames": ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesWhitelistedNamesTypeDef
    },
    total=False,
)


class ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef(
    _RequiredClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef,
    _OptionalClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef,
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValues` `Cookies`

    A complex type that specifies whether you want CloudFront to forward cookies to the origin
    and, if so, which ones. For more information about forwarding cookies to the origin, see
    `How CloudFront Forwards, Caches, and Logs Cookies
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html>`__ in the
    *Amazon CloudFront Developer Guide* .

    - **Forward** *(string) --* **[REQUIRED]**

      Specifies which cookies to forward to the origin for this cache behavior: all, none, or
      the list of cookies specified in the ``WhitelistedNames`` complex type.

      Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an
      Amazon S3 origin, specify none for the ``Forward`` element.

    - **WhitelistedNames** *(dict) --*

      Required if you specify ``whitelist`` for the value of ``Forward:`` . A complex type that
      specifies how many different cookies you want CloudFront to forward to the origin for
      this cache behavior and, if you want to forward selected cookies, the names of those
      cookies.

      If you specify ``all`` or none for the value of ``Forward`` , omit ``WhitelistedNames`` .
      If you change the value of ``Forward`` from ``whitelist`` to all or none and you don't
      delete the ``WhitelistedNames`` element and its child elements, CloudFront deletes them
      automatically.

      For the current limit on the number of cookie names that you can whitelist for each cache
      behavior, see `CloudFront Limits
      <https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront>`__
      in the *AWS General Reference* .

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of different cookies that you want CloudFront to forward to the origin for
        this cache behavior.

      - **Items** *(list) --*

        A complex type that contains one ``Name`` element for each cookie that you want
        CloudFront to forward to the origin for this cache behavior.

        - *(string) --*
    """


_ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeadersTypeDef = TypedDict(
    "_ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeadersTypeDef",
    {"Quantity": int},
)


class ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeadersTypeDef(
    _ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeadersTypeDef
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValues` `Headers`

    A complex type that specifies the ``Headers`` , if any, that you want CloudFront to forward
    to the origin for this cache behavior (whitelisted headers). For the headers that you
    specify, CloudFront also caches separate versions of a specified object that is based on
    the header values in viewer requests.

    For more information, see `Caching Content Based on Request Headers
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html>`__
    in the *Amazon CloudFront Developer Guide* .

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of different headers that you want CloudFront to base caching on for this
      cache behavior. You can configure each cache behavior in a web distribution to do one of
      the following:

      * **Forward all headers to your origin** : Specify ``1`` for ``Quantity`` and ``*`` for
      ``Name`` .

      .. warning::

         CloudFront doesn't cache the objects that are associated with this cache behavior.
         Instead, CloudFront sends every request to the origin.

      * **Forward a whitelist of headers you specify** : Specify the number of headers that you
      want CloudFront to base caching on. Then specify the header names in ``Name`` elements.
      CloudFront caches your objects based on the values in the specified headers.

      * **Forward only the default headers** : Specify ``0`` for ``Quantity`` and omit
      ``Items`` . In this configuration, CloudFront doesn't cache based on the values in the
      request headers.

      Regardless of which option you choose, CloudFront forwards headers to your origin based
      on whether the origin is an S3 bucket or a custom origin. See the following documentation:

      * **S3 bucket** : See `HTTP Request Headers That CloudFront Removes or Updates
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorS3Origin.html#request-s3-removed-headers>`__
    """


_RequiredClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef = TypedDict(
    "_RequiredClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef",
    {
        "QueryString": bool,
        "Cookies": ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookiesTypeDef,
    },
)
_OptionalClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef = TypedDict(
    "_OptionalClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef",
    {
        "Headers": ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeadersTypeDef
    },
    total=False,
)


class ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef(
    _RequiredClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef,
    _OptionalClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef,
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfigDefaultCacheBehavior` `ForwardedValues`

    A complex type that specifies how CloudFront handles query strings and cookies.

    - **QueryString** *(boolean) --* **[REQUIRED]**

      Indicates whether you want CloudFront to forward query strings to the origin that is
      associated with this cache behavior and cache based on the query string parameters.
      CloudFront behavior depends on the value of ``QueryString`` and on the values that you
      specify for ``QueryStringCacheKeys`` , if any:

      If you specify true for ``QueryString`` and you don't specify any values for
      ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin
      and caches based on all query string parameters. Depending on how many query string
      parameters and values you have, this can adversely affect performance because CloudFront
      must forward more requests to the origin.

      If you specify true for ``QueryString`` and you specify one or more values for
      ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin,
      but it only caches based on the query string parameters that you specify.

      If you specify false for ``QueryString`` , CloudFront doesn't forward any query string
      parameters to the origin, and doesn't cache based on query string parameters.

      For more information, see `Configuring CloudFront to Cache Based on Query String Parameters
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html>`__
      in the *Amazon CloudFront Developer Guide* .

    - **Cookies** *(dict) --* **[REQUIRED]**

      A complex type that specifies whether you want CloudFront to forward cookies to the origin
      and, if so, which ones. For more information about forwarding cookies to the origin, see
      `How CloudFront Forwards, Caches, and Logs Cookies
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html>`__ in the
      *Amazon CloudFront Developer Guide* .

      - **Forward** *(string) --* **[REQUIRED]**

        Specifies which cookies to forward to the origin for this cache behavior: all, none, or
        the list of cookies specified in the ``WhitelistedNames`` complex type.

        Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an
        Amazon S3 origin, specify none for the ``Forward`` element.

      - **WhitelistedNames** *(dict) --*

        Required if you specify ``whitelist`` for the value of ``Forward:`` . A complex type that
        specifies how many different cookies you want CloudFront to forward to the origin for
        this cache behavior and, if you want to forward selected cookies, the names of those
        cookies.

        If you specify ``all`` or none for the value of ``Forward`` , omit ``WhitelistedNames`` .
        If you change the value of ``Forward`` from ``whitelist`` to all or none and you don't
        delete the ``WhitelistedNames`` element and its child elements, CloudFront deletes them
        automatically.

        For the current limit on the number of cookie names that you can whitelist for each cache
        behavior, see `CloudFront Limits
        <https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront>`__
        in the *AWS General Reference* .

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of different cookies that you want CloudFront to forward to the origin for
          this cache behavior.

        - **Items** *(list) --*

          A complex type that contains one ``Name`` element for each cookie that you want
          CloudFront to forward to the origin for this cache behavior.

          - *(string) --*

    - **Headers** *(dict) --*

      A complex type that specifies the ``Headers`` , if any, that you want CloudFront to forward
      to the origin for this cache behavior (whitelisted headers). For the headers that you
      specify, CloudFront also caches separate versions of a specified object that is based on
      the header values in viewer requests.

      For more information, see `Caching Content Based on Request Headers
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html>`__
      in the *Amazon CloudFront Developer Guide* .

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of different headers that you want CloudFront to base caching on for this
        cache behavior. You can configure each cache behavior in a web distribution to do one of
        the following:

        * **Forward all headers to your origin** : Specify ``1`` for ``Quantity`` and ``*`` for
        ``Name`` .

        .. warning::

           CloudFront doesn't cache the objects that are associated with this cache behavior.
           Instead, CloudFront sends every request to the origin.

        * **Forward a whitelist of headers you specify** : Specify the number of headers that you
        want CloudFront to base caching on. Then specify the header names in ``Name`` elements.
        CloudFront caches your objects based on the values in the specified headers.

        * **Forward only the default headers** : Specify ``0`` for ``Quantity`` and omit
        ``Items`` . In this configuration, CloudFront doesn't cache based on the values in the
        request headers.

        Regardless of which option you choose, CloudFront forwards headers to your origin based
        on whether the origin is an S3 bucket or a custom origin. See the following documentation:

        * **S3 bucket** : See `HTTP Request Headers That CloudFront Removes or Updates
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorS3Origin.html#request-s3-removed-headers>`__
    """


_ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorTypeDef = TypedDict(
    "_ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorTypeDef",
    {
        "TargetOriginId": str,
        "ForwardedValues": ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesTypeDef,
    },
)


class ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorTypeDef(
    _ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorTypeDef
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfig` `DefaultCacheBehavior`

    A complex type that describes the default cache behavior if you don't specify a
    ``CacheBehavior`` element or if files don't match any of the values of ``PathPattern`` in
    ``CacheBehavior`` elements. You must create exactly one default cache behavior.

    - **TargetOriginId** *(string) --* **[REQUIRED]**

      The value of ``ID`` for the origin that you want CloudFront to route requests to when a
      request matches the path pattern either for a cache behavior or for the default cache
      behavior in your distribution.

    - **ForwardedValues** *(dict) --* **[REQUIRED]**

      A complex type that specifies how CloudFront handles query strings and cookies.

      - **QueryString** *(boolean) --* **[REQUIRED]**

        Indicates whether you want CloudFront to forward query strings to the origin that is
        associated with this cache behavior and cache based on the query string parameters.
        CloudFront behavior depends on the value of ``QueryString`` and on the values that you
        specify for ``QueryStringCacheKeys`` , if any:

        If you specify true for ``QueryString`` and you don't specify any values for
        ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin
        and caches based on all query string parameters. Depending on how many query string
        parameters and values you have, this can adversely affect performance because CloudFront
        must forward more requests to the origin.

        If you specify true for ``QueryString`` and you specify one or more values for
        ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin,
        but it only caches based on the query string parameters that you specify.

        If you specify false for ``QueryString`` , CloudFront doesn't forward any query string
        parameters to the origin, and doesn't cache based on query string parameters.

        For more information, see `Configuring CloudFront to Cache Based on Query String Parameters
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html>`__
        in the *Amazon CloudFront Developer Guide* .

      - **Cookies** *(dict) --* **[REQUIRED]**

        A complex type that specifies whether you want CloudFront to forward cookies to the origin
        and, if so, which ones. For more information about forwarding cookies to the origin, see
        `How CloudFront Forwards, Caches, and Logs Cookies
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html>`__ in the
        *Amazon CloudFront Developer Guide* .

        - **Forward** *(string) --* **[REQUIRED]**

          Specifies which cookies to forward to the origin for this cache behavior: all, none, or
          the list of cookies specified in the ``WhitelistedNames`` complex type.

          Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an
          Amazon S3 origin, specify none for the ``Forward`` element.

        - **WhitelistedNames** *(dict) --*

          Required if you specify ``whitelist`` for the value of ``Forward:`` . A complex type that
          specifies how many different cookies you want CloudFront to forward to the origin for
          this cache behavior and, if you want to forward selected cookies, the names of those
          cookies.

          If you specify ``all`` or none for the value of ``Forward`` , omit ``WhitelistedNames`` .
          If you change the value of ``Forward`` from ``whitelist`` to all or none and you don't
          delete the ``WhitelistedNames`` element and its child elements, CloudFront deletes them
          automatically.

          For the current limit on the number of cookie names that you can whitelist for each cache
          behavior, see `CloudFront Limits
          <https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront>`__
          in the *AWS General Reference* .

          - **Quantity** *(integer) --* **[REQUIRED]**

            The number of different cookies that you want CloudFront to forward to the origin for
            this cache behavior.

          - **Items** *(list) --*

            A complex type that contains one ``Name`` element for each cookie that you want
            CloudFront to forward to the origin for this cache behavior.

            - *(string) --*

      - **Headers** *(dict) --*

        A complex type that specifies the ``Headers`` , if any, that you want CloudFront to forward
        to the origin for this cache behavior (whitelisted headers). For the headers that you
        specify, CloudFront also caches separate versions of a specified object that is based on
        the header values in viewer requests.

        For more information, see `Caching Content Based on Request Headers
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html>`__
        in the *Amazon CloudFront Developer Guide* .

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of different headers that you want CloudFront to base caching on for this
          cache behavior. You can configure each cache behavior in a web distribution to do one of
          the following:

          * **Forward all headers to your origin** : Specify ``1`` for ``Quantity`` and ``*`` for
          ``Name`` .

          .. warning::

             CloudFront doesn't cache the objects that are associated with this cache behavior.
             Instead, CloudFront sends every request to the origin.

          * **Forward a whitelist of headers you specify** : Specify the number of headers that you
          want CloudFront to base caching on. Then specify the header names in ``Name`` elements.
          CloudFront caches your objects based on the values in the specified headers.

          * **Forward only the default headers** : Specify ``0`` for ``Quantity`` and omit
          ``Items`` . In this configuration, CloudFront doesn't cache based on the values in the
          request headers.

          Regardless of which option you choose, CloudFront forwards headers to your origin based
          on whether the origin is an S3 bucket or a custom origin. See the following documentation:

          * **S3 bucket** : See `HTTP Request Headers That CloudFront Removes or Updates
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorS3Origin.html#request-s3-removed-headers>`__
    """


_ClientUpdateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaStatusCodesTypeDef = TypedDict(
    "_ClientUpdateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaStatusCodesTypeDef",
    {"Quantity": int, "Items": List[int]},
)


class ClientUpdateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaStatusCodesTypeDef(
    _ClientUpdateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaStatusCodesTypeDef
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfigOriginGroupsItemsFailoverCriteria` `StatusCodes`

    The status codes that, when returned from the primary origin, will trigger CloudFront
    to failover to the second origin.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of status codes.

    - **Items** *(list) --* **[REQUIRED]**

      The items (status codes) for an origin group.

      - *(integer) --*
    """


_ClientUpdateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaTypeDef = TypedDict(
    "_ClientUpdateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaTypeDef",
    {
        "StatusCodes": ClientUpdateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaStatusCodesTypeDef
    },
)


class ClientUpdateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaTypeDef(
    _ClientUpdateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaTypeDef
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfigOriginGroupsItems` `FailoverCriteria`

    A complex type that contains information about the failover criteria for an origin group.

    - **StatusCodes** *(dict) --* **[REQUIRED]**

      The status codes that, when returned from the primary origin, will trigger CloudFront
      to failover to the second origin.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of status codes.

      - **Items** *(list) --* **[REQUIRED]**

        The items (status codes) for an origin group.

        - *(integer) --*
    """


_ClientUpdateDistributionDistributionConfigOriginGroupsItemsMembersItemsTypeDef = TypedDict(
    "_ClientUpdateDistributionDistributionConfigOriginGroupsItemsMembersItemsTypeDef",
    {"OriginId": str},
)


class ClientUpdateDistributionDistributionConfigOriginGroupsItemsMembersItemsTypeDef(
    _ClientUpdateDistributionDistributionConfigOriginGroupsItemsMembersItemsTypeDef
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfigOriginGroupsItemsMembers` `Items`

    An origin in an origin group.

    - **OriginId** *(string) --* **[REQUIRED]**

      The ID for an origin in an origin group.
    """


_ClientUpdateDistributionDistributionConfigOriginGroupsItemsMembersTypeDef = TypedDict(
    "_ClientUpdateDistributionDistributionConfigOriginGroupsItemsMembersTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientUpdateDistributionDistributionConfigOriginGroupsItemsMembersItemsTypeDef
        ],
    },
)


class ClientUpdateDistributionDistributionConfigOriginGroupsItemsMembersTypeDef(
    _ClientUpdateDistributionDistributionConfigOriginGroupsItemsMembersTypeDef
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfigOriginGroupsItems` `Members`

    A complex type that contains information about the origins in an origin group.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of origins in an origin group.

    - **Items** *(list) --* **[REQUIRED]**

      Items (origins) in an origin group.

      - *(dict) --*

        An origin in an origin group.

        - **OriginId** *(string) --* **[REQUIRED]**

          The ID for an origin in an origin group.
    """


_ClientUpdateDistributionDistributionConfigOriginGroupsItemsTypeDef = TypedDict(
    "_ClientUpdateDistributionDistributionConfigOriginGroupsItemsTypeDef",
    {
        "Id": str,
        "FailoverCriteria": ClientUpdateDistributionDistributionConfigOriginGroupsItemsFailoverCriteriaTypeDef,
        "Members": ClientUpdateDistributionDistributionConfigOriginGroupsItemsMembersTypeDef,
    },
)


class ClientUpdateDistributionDistributionConfigOriginGroupsItemsTypeDef(
    _ClientUpdateDistributionDistributionConfigOriginGroupsItemsTypeDef
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfigOriginGroups` `Items`

    An origin group includes two origins (a primary origin and a second origin to failover to)
    and a failover criteria that you specify. You create an origin group to support origin
    failover in CloudFront. When you create or update a distribution, you can specifiy the
    origin group instead of a single origin, and CloudFront will failover from the primary
    origin to the second origin under the failover conditions that you've chosen.

    - **Id** *(string) --* **[REQUIRED]**

      The origin group's ID.

    - **FailoverCriteria** *(dict) --* **[REQUIRED]**

      A complex type that contains information about the failover criteria for an origin group.

      - **StatusCodes** *(dict) --* **[REQUIRED]**

        The status codes that, when returned from the primary origin, will trigger CloudFront
        to failover to the second origin.

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of status codes.

        - **Items** *(list) --* **[REQUIRED]**

          The items (status codes) for an origin group.

          - *(integer) --*

    - **Members** *(dict) --* **[REQUIRED]**

      A complex type that contains information about the origins in an origin group.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of origins in an origin group.

      - **Items** *(list) --* **[REQUIRED]**

        Items (origins) in an origin group.

        - *(dict) --*

          An origin in an origin group.

          - **OriginId** *(string) --* **[REQUIRED]**

            The ID for an origin in an origin group.
    """


_RequiredClientUpdateDistributionDistributionConfigOriginGroupsTypeDef = TypedDict(
    "_RequiredClientUpdateDistributionDistributionConfigOriginGroupsTypeDef",
    {"Quantity": int},
)
_OptionalClientUpdateDistributionDistributionConfigOriginGroupsTypeDef = TypedDict(
    "_OptionalClientUpdateDistributionDistributionConfigOriginGroupsTypeDef",
    {"Items": List[ClientUpdateDistributionDistributionConfigOriginGroupsItemsTypeDef]},
    total=False,
)


class ClientUpdateDistributionDistributionConfigOriginGroupsTypeDef(
    _RequiredClientUpdateDistributionDistributionConfigOriginGroupsTypeDef,
    _OptionalClientUpdateDistributionDistributionConfigOriginGroupsTypeDef,
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfig` `OriginGroups`

    A complex type that contains information about origin groups for this distribution.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of origin groups.

    - **Items** *(list) --*

      The items (origin groups) in a distribution.

      - *(dict) --*

        An origin group includes two origins (a primary origin and a second origin to failover to)
        and a failover criteria that you specify. You create an origin group to support origin
        failover in CloudFront. When you create or update a distribution, you can specifiy the
        origin group instead of a single origin, and CloudFront will failover from the primary
        origin to the second origin under the failover conditions that you've chosen.

        - **Id** *(string) --* **[REQUIRED]**

          The origin group's ID.

        - **FailoverCriteria** *(dict) --* **[REQUIRED]**

          A complex type that contains information about the failover criteria for an origin group.

          - **StatusCodes** *(dict) --* **[REQUIRED]**

            The status codes that, when returned from the primary origin, will trigger CloudFront
            to failover to the second origin.

            - **Quantity** *(integer) --* **[REQUIRED]**

              The number of status codes.

            - **Items** *(list) --* **[REQUIRED]**

              The items (status codes) for an origin group.

              - *(integer) --*

        - **Members** *(dict) --* **[REQUIRED]**

          A complex type that contains information about the origins in an origin group.

          - **Quantity** *(integer) --* **[REQUIRED]**

            The number of origins in an origin group.

          - **Items** *(list) --* **[REQUIRED]**

            Items (origins) in an origin group.

            - *(dict) --*

              An origin in an origin group.

              - **OriginId** *(string) --* **[REQUIRED]**

                The ID for an origin in an origin group.
    """


_ClientUpdateDistributionDistributionConfigOriginsItemsCustomHeadersItemsTypeDef = TypedDict(
    "_ClientUpdateDistributionDistributionConfigOriginsItemsCustomHeadersItemsTypeDef",
    {"HeaderName": str, "HeaderValue": str},
)


class ClientUpdateDistributionDistributionConfigOriginsItemsCustomHeadersItemsTypeDef(
    _ClientUpdateDistributionDistributionConfigOriginsItemsCustomHeadersItemsTypeDef
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfigOriginsItemsCustomHeaders` `Items`

    A complex type that contains ``HeaderName`` and ``HeaderValue`` elements, if any, for
    this distribution.

    - **HeaderName** *(string) --* **[REQUIRED]**

      The name of a header that you want CloudFront to forward to your origin. For more
      information, see `Forwarding Custom Headers to Your Origin (Web Distributions Only)
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html>`__
      in the *Amazon CloudFront Developer Guide* .

    - **HeaderValue** *(string) --* **[REQUIRED]**

      The value for the header that you specified in the ``HeaderName`` field.
    """


_RequiredClientUpdateDistributionDistributionConfigOriginsItemsCustomHeadersTypeDef = TypedDict(
    "_RequiredClientUpdateDistributionDistributionConfigOriginsItemsCustomHeadersTypeDef",
    {"Quantity": int},
)
_OptionalClientUpdateDistributionDistributionConfigOriginsItemsCustomHeadersTypeDef = TypedDict(
    "_OptionalClientUpdateDistributionDistributionConfigOriginsItemsCustomHeadersTypeDef",
    {
        "Items": List[
            ClientUpdateDistributionDistributionConfigOriginsItemsCustomHeadersItemsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateDistributionDistributionConfigOriginsItemsCustomHeadersTypeDef(
    _RequiredClientUpdateDistributionDistributionConfigOriginsItemsCustomHeadersTypeDef,
    _OptionalClientUpdateDistributionDistributionConfigOriginsItemsCustomHeadersTypeDef,
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfigOriginsItems` `CustomHeaders`

    A complex type that contains names and values for the custom headers that you want.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of custom headers, if any, for this distribution.

    - **Items** *(list) --*

       **Optional** : A list that contains one ``OriginCustomHeader`` element for each custom
       header that you want CloudFront to forward to the origin. If Quantity is ``0`` , omit
       ``Items`` .

      - *(dict) --*

        A complex type that contains ``HeaderName`` and ``HeaderValue`` elements, if any, for
        this distribution.

        - **HeaderName** *(string) --* **[REQUIRED]**

          The name of a header that you want CloudFront to forward to your origin. For more
          information, see `Forwarding Custom Headers to Your Origin (Web Distributions Only)
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html>`__
          in the *Amazon CloudFront Developer Guide* .

        - **HeaderValue** *(string) --* **[REQUIRED]**

          The value for the header that you specified in the ``HeaderName`` field.
    """


_ClientUpdateDistributionDistributionConfigOriginsItemsCustomOriginConfigOriginSslProtocolsTypeDef = TypedDict(
    "_ClientUpdateDistributionDistributionConfigOriginsItemsCustomOriginConfigOriginSslProtocolsTypeDef",
    {"Quantity": int, "Items": List[str]},
)


class ClientUpdateDistributionDistributionConfigOriginsItemsCustomOriginConfigOriginSslProtocolsTypeDef(
    _ClientUpdateDistributionDistributionConfigOriginsItemsCustomOriginConfigOriginSslProtocolsTypeDef
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfigOriginsItemsCustomOriginConfig` `OriginSslProtocols`

    The SSL/TLS protocols that you want CloudFront to use when communicating with your
    origin over HTTPS.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of SSL/TLS protocols that you want to allow CloudFront to use when
      establishing an HTTPS connection with this origin.

    - **Items** *(list) --* **[REQUIRED]**

      A list that contains allowed SSL/TLS protocols for this distribution.

      - *(string) --*
    """


_RequiredClientUpdateDistributionDistributionConfigOriginsItemsCustomOriginConfigTypeDef = TypedDict(
    "_RequiredClientUpdateDistributionDistributionConfigOriginsItemsCustomOriginConfigTypeDef",
    {"HTTPPort": int, "HTTPSPort": int, "OriginProtocolPolicy": str},
)
_OptionalClientUpdateDistributionDistributionConfigOriginsItemsCustomOriginConfigTypeDef = TypedDict(
    "_OptionalClientUpdateDistributionDistributionConfigOriginsItemsCustomOriginConfigTypeDef",
    {
        "OriginSslProtocols": ClientUpdateDistributionDistributionConfigOriginsItemsCustomOriginConfigOriginSslProtocolsTypeDef,
        "OriginReadTimeout": int,
        "OriginKeepaliveTimeout": int,
    },
    total=False,
)


class ClientUpdateDistributionDistributionConfigOriginsItemsCustomOriginConfigTypeDef(
    _RequiredClientUpdateDistributionDistributionConfigOriginsItemsCustomOriginConfigTypeDef,
    _OptionalClientUpdateDistributionDistributionConfigOriginsItemsCustomOriginConfigTypeDef,
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfigOriginsItems` `CustomOriginConfig`

    A complex type that contains information about a custom origin. If the origin is an
    Amazon S3 bucket, use the ``S3OriginConfig`` element instead.

    - **HTTPPort** *(integer) --* **[REQUIRED]**

      The HTTP port the custom origin listens on.

    - **HTTPSPort** *(integer) --* **[REQUIRED]**

      The HTTPS port the custom origin listens on.

    - **OriginProtocolPolicy** *(string) --* **[REQUIRED]**

      The origin protocol policy to apply to your origin.

    - **OriginSslProtocols** *(dict) --*

      The SSL/TLS protocols that you want CloudFront to use when communicating with your
      origin over HTTPS.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of SSL/TLS protocols that you want to allow CloudFront to use when
        establishing an HTTPS connection with this origin.

      - **Items** *(list) --* **[REQUIRED]**

        A list that contains allowed SSL/TLS protocols for this distribution.

        - *(string) --*

    - **OriginReadTimeout** *(integer) --*

      You can create a custom origin read timeout. All timeout units are in seconds. The
      default origin read timeout is 30 seconds, but you can configure custom timeout lengths
      using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60
      seconds.

      If you need to increase the maximum time limit, contact the `AWS Support Center
      <https://console.aws.amazon.com/support/home#/>`__ .

    - **OriginKeepaliveTimeout** *(integer) --*

      You can create a custom keep-alive timeout. All timeout units are in seconds. The
      default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths
      using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60
      seconds.

      If you need to increase the maximum time limit, contact the `AWS Support Center
      <https://console.aws.amazon.com/support/home#/>`__ .
    """


_ClientUpdateDistributionDistributionConfigOriginsItemsS3OriginConfigTypeDef = TypedDict(
    "_ClientUpdateDistributionDistributionConfigOriginsItemsS3OriginConfigTypeDef",
    {"OriginAccessIdentity": str},
)


class ClientUpdateDistributionDistributionConfigOriginsItemsS3OriginConfigTypeDef(
    _ClientUpdateDistributionDistributionConfigOriginsItemsS3OriginConfigTypeDef
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfigOriginsItems` `S3OriginConfig`

    A complex type that contains information about the Amazon S3 origin. If the origin is a
    custom origin, use the ``CustomOriginConfig`` element instead.

    - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

      The CloudFront origin access identity to associate with the origin. Use an origin
      access identity to configure the origin so that viewers can *only* access objects in an
      Amazon S3 bucket through CloudFront. The format of the value is:

      origin-access-identity/cloudfront/*ID-of-origin-access-identity*

      where `` *ID-of-origin-access-identity* `` is the value that CloudFront returned in the
      ``ID`` element when you created the origin access identity.

      If you want viewers to be able to access objects using either the CloudFront URL or the
      Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

      To delete the origin access identity from an existing distribution, update the
      distribution configuration and include an empty ``OriginAccessIdentity`` element.

      To replace the origin access identity, update the distribution configuration and
      specify the new origin access identity.

      For more information about the origin access identity, see `Serving Private Content
      through CloudFront
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
      in the *Amazon CloudFront Developer Guide* .
    """


_RequiredClientUpdateDistributionDistributionConfigOriginsItemsTypeDef = TypedDict(
    "_RequiredClientUpdateDistributionDistributionConfigOriginsItemsTypeDef",
    {"Id": str, "DomainName": str},
)
_OptionalClientUpdateDistributionDistributionConfigOriginsItemsTypeDef = TypedDict(
    "_OptionalClientUpdateDistributionDistributionConfigOriginsItemsTypeDef",
    {
        "OriginPath": str,
        "CustomHeaders": ClientUpdateDistributionDistributionConfigOriginsItemsCustomHeadersTypeDef,
        "S3OriginConfig": ClientUpdateDistributionDistributionConfigOriginsItemsS3OriginConfigTypeDef,
        "CustomOriginConfig": ClientUpdateDistributionDistributionConfigOriginsItemsCustomOriginConfigTypeDef,
    },
    total=False,
)


class ClientUpdateDistributionDistributionConfigOriginsItemsTypeDef(
    _RequiredClientUpdateDistributionDistributionConfigOriginsItemsTypeDef,
    _OptionalClientUpdateDistributionDistributionConfigOriginsItemsTypeDef,
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfigOrigins` `Items`

    A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web
    server), Amazon MediaStore, or other server from which CloudFront gets your files. This can
    also be an origin group, if you've created an origin group. You must specify at least one
    origin or origin group.

    For the current limit on the number of origins or origin groups that you can specify for a
    distribution, see `Amazon CloudFront Limits
    <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront>`__
    in the *AWS General Reference* .

    - **Id** *(string) --* **[REQUIRED]**

      A unique identifier for the origin or origin group. The value of ``Id`` must be unique
      within the distribution.

      When you specify the value of ``TargetOriginId`` for the default cache behavior or for
      another cache behavior, you indicate the origin to which you want the cache behavior to
      route requests by specifying the value of the ``Id`` element for that origin. When a
      request matches the path pattern for that cache behavior, CloudFront routes the request
      to the specified origin. For more information, see `Cache Behavior Settings
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior>`__
      in the *Amazon CloudFront Developer Guide* .

    - **DomainName** *(string) --* **[REQUIRED]**

       **Amazon S3 origins** : The DNS name of the Amazon S3 bucket from which you want
       CloudFront to get objects for this origin, for example, ``myawsbucket.s3.amazonaws.com``
       . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3
       static website hosting endpoint for the bucket.

      For more information about specifying this value for different types of origins, see
      `Origin Domain Name
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesDomainName>`__
      in the *Amazon CloudFront Developer Guide* .

      Constraints for Amazon S3 origins:

      * If you configured Amazon S3 Transfer Acceleration for your bucket, don't specify the
      ``s3-accelerate`` endpoint for ``DomainName`` .

      * The bucket name must be between 3 and 63 characters long (inclusive).

      * The bucket name must contain only lowercase characters, numbers, periods, underscores,
      and dashes.

      * The bucket name must not contain adjacent periods.

       **Custom Origins** : The DNS domain name for the HTTP server from which you want
       CloudFront to get objects for this origin, for example, ``www.example.com`` .

      Constraints for custom origins:

      * ``DomainName`` must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.),
      hyphen (-), or underscore (_) characters.

      * The name cannot exceed 128 characters.

    - **OriginPath** *(string) --*

      An optional element that causes CloudFront to request your content from a directory in
      your Amazon S3 bucket or your custom origin. When you include the ``OriginPath`` element,
      specify the directory name, beginning with a ``/`` . CloudFront appends the directory
      name to the value of ``DomainName`` , for example, ``example.com/production`` . Do not
      include a ``/`` at the end of the directory name.

      For example, suppose you've specified the following values for your distribution:

      * ``DomainName`` : An Amazon S3 bucket named ``myawsbucket`` .

      * ``OriginPath`` : ``/production``

      * ``CNAME`` : ``example.com``

      When a user enters ``example.com/index.html`` in a browser, CloudFront sends a request to
      Amazon S3 for ``myawsbucket/production/index.html`` .

      When a user enters ``example.com/acme/index.html`` in a browser, CloudFront sends a
      request to Amazon S3 for ``myawsbucket/production/acme/index.html`` .

    - **CustomHeaders** *(dict) --*

      A complex type that contains names and values for the custom headers that you want.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of custom headers, if any, for this distribution.

      - **Items** *(list) --*

         **Optional** : A list that contains one ``OriginCustomHeader`` element for each custom
         header that you want CloudFront to forward to the origin. If Quantity is ``0`` , omit
         ``Items`` .

        - *(dict) --*

          A complex type that contains ``HeaderName`` and ``HeaderValue`` elements, if any, for
          this distribution.

          - **HeaderName** *(string) --* **[REQUIRED]**

            The name of a header that you want CloudFront to forward to your origin. For more
            information, see `Forwarding Custom Headers to Your Origin (Web Distributions Only)
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html>`__
            in the *Amazon CloudFront Developer Guide* .

          - **HeaderValue** *(string) --* **[REQUIRED]**

            The value for the header that you specified in the ``HeaderName`` field.

    - **S3OriginConfig** *(dict) --*

      A complex type that contains information about the Amazon S3 origin. If the origin is a
      custom origin, use the ``CustomOriginConfig`` element instead.

      - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

        The CloudFront origin access identity to associate with the origin. Use an origin
        access identity to configure the origin so that viewers can *only* access objects in an
        Amazon S3 bucket through CloudFront. The format of the value is:

        origin-access-identity/cloudfront/*ID-of-origin-access-identity*

        where `` *ID-of-origin-access-identity* `` is the value that CloudFront returned in the
        ``ID`` element when you created the origin access identity.

        If you want viewers to be able to access objects using either the CloudFront URL or the
        Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

        To delete the origin access identity from an existing distribution, update the
        distribution configuration and include an empty ``OriginAccessIdentity`` element.

        To replace the origin access identity, update the distribution configuration and
        specify the new origin access identity.

        For more information about the origin access identity, see `Serving Private Content
        through CloudFront
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
        in the *Amazon CloudFront Developer Guide* .

    - **CustomOriginConfig** *(dict) --*

      A complex type that contains information about a custom origin. If the origin is an
      Amazon S3 bucket, use the ``S3OriginConfig`` element instead.

      - **HTTPPort** *(integer) --* **[REQUIRED]**

        The HTTP port the custom origin listens on.

      - **HTTPSPort** *(integer) --* **[REQUIRED]**

        The HTTPS port the custom origin listens on.

      - **OriginProtocolPolicy** *(string) --* **[REQUIRED]**

        The origin protocol policy to apply to your origin.

      - **OriginSslProtocols** *(dict) --*

        The SSL/TLS protocols that you want CloudFront to use when communicating with your
        origin over HTTPS.

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of SSL/TLS protocols that you want to allow CloudFront to use when
          establishing an HTTPS connection with this origin.

        - **Items** *(list) --* **[REQUIRED]**

          A list that contains allowed SSL/TLS protocols for this distribution.

          - *(string) --*

      - **OriginReadTimeout** *(integer) --*

        You can create a custom origin read timeout. All timeout units are in seconds. The
        default origin read timeout is 30 seconds, but you can configure custom timeout lengths
        using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60
        seconds.

        If you need to increase the maximum time limit, contact the `AWS Support Center
        <https://console.aws.amazon.com/support/home#/>`__ .

      - **OriginKeepaliveTimeout** *(integer) --*

        You can create a custom keep-alive timeout. All timeout units are in seconds. The
        default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths
        using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60
        seconds.

        If you need to increase the maximum time limit, contact the `AWS Support Center
        <https://console.aws.amazon.com/support/home#/>`__ .
    """


_ClientUpdateDistributionDistributionConfigOriginsTypeDef = TypedDict(
    "_ClientUpdateDistributionDistributionConfigOriginsTypeDef",
    {
        "Quantity": int,
        "Items": List[ClientUpdateDistributionDistributionConfigOriginsItemsTypeDef],
    },
)


class ClientUpdateDistributionDistributionConfigOriginsTypeDef(
    _ClientUpdateDistributionDistributionConfigOriginsTypeDef
):
    """
    Type definition for `ClientUpdateDistributionDistributionConfig` `Origins`

    A complex type that contains information about origins for this distribution.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of origins or origin groups for this distribution.

    - **Items** *(list) --* **[REQUIRED]**

      A complex type that contains origins or origin groups for this distribution.

      - *(dict) --*

        A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web
        server), Amazon MediaStore, or other server from which CloudFront gets your files. This can
        also be an origin group, if you've created an origin group. You must specify at least one
        origin or origin group.

        For the current limit on the number of origins or origin groups that you can specify for a
        distribution, see `Amazon CloudFront Limits
        <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront>`__
        in the *AWS General Reference* .

        - **Id** *(string) --* **[REQUIRED]**

          A unique identifier for the origin or origin group. The value of ``Id`` must be unique
          within the distribution.

          When you specify the value of ``TargetOriginId`` for the default cache behavior or for
          another cache behavior, you indicate the origin to which you want the cache behavior to
          route requests by specifying the value of the ``Id`` element for that origin. When a
          request matches the path pattern for that cache behavior, CloudFront routes the request
          to the specified origin. For more information, see `Cache Behavior Settings
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior>`__
          in the *Amazon CloudFront Developer Guide* .

        - **DomainName** *(string) --* **[REQUIRED]**

           **Amazon S3 origins** : The DNS name of the Amazon S3 bucket from which you want
           CloudFront to get objects for this origin, for example, ``myawsbucket.s3.amazonaws.com``
           . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3
           static website hosting endpoint for the bucket.

          For more information about specifying this value for different types of origins, see
          `Origin Domain Name
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesDomainName>`__
          in the *Amazon CloudFront Developer Guide* .

          Constraints for Amazon S3 origins:

          * If you configured Amazon S3 Transfer Acceleration for your bucket, don't specify the
          ``s3-accelerate`` endpoint for ``DomainName`` .

          * The bucket name must be between 3 and 63 characters long (inclusive).

          * The bucket name must contain only lowercase characters, numbers, periods, underscores,
          and dashes.

          * The bucket name must not contain adjacent periods.

           **Custom Origins** : The DNS domain name for the HTTP server from which you want
           CloudFront to get objects for this origin, for example, ``www.example.com`` .

          Constraints for custom origins:

          * ``DomainName`` must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.),
          hyphen (-), or underscore (_) characters.

          * The name cannot exceed 128 characters.

        - **OriginPath** *(string) --*

          An optional element that causes CloudFront to request your content from a directory in
          your Amazon S3 bucket or your custom origin. When you include the ``OriginPath`` element,
          specify the directory name, beginning with a ``/`` . CloudFront appends the directory
          name to the value of ``DomainName`` , for example, ``example.com/production`` . Do not
          include a ``/`` at the end of the directory name.

          For example, suppose you've specified the following values for your distribution:

          * ``DomainName`` : An Amazon S3 bucket named ``myawsbucket`` .

          * ``OriginPath`` : ``/production``

          * ``CNAME`` : ``example.com``

          When a user enters ``example.com/index.html`` in a browser, CloudFront sends a request to
          Amazon S3 for ``myawsbucket/production/index.html`` .

          When a user enters ``example.com/acme/index.html`` in a browser, CloudFront sends a
          request to Amazon S3 for ``myawsbucket/production/acme/index.html`` .

        - **CustomHeaders** *(dict) --*

          A complex type that contains names and values for the custom headers that you want.

          - **Quantity** *(integer) --* **[REQUIRED]**

            The number of custom headers, if any, for this distribution.

          - **Items** *(list) --*

             **Optional** : A list that contains one ``OriginCustomHeader`` element for each custom
             header that you want CloudFront to forward to the origin. If Quantity is ``0`` , omit
             ``Items`` .

            - *(dict) --*

              A complex type that contains ``HeaderName`` and ``HeaderValue`` elements, if any, for
              this distribution.

              - **HeaderName** *(string) --* **[REQUIRED]**

                The name of a header that you want CloudFront to forward to your origin. For more
                information, see `Forwarding Custom Headers to Your Origin (Web Distributions Only)
                <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html>`__
                in the *Amazon CloudFront Developer Guide* .

              - **HeaderValue** *(string) --* **[REQUIRED]**

                The value for the header that you specified in the ``HeaderName`` field.

        - **S3OriginConfig** *(dict) --*

          A complex type that contains information about the Amazon S3 origin. If the origin is a
          custom origin, use the ``CustomOriginConfig`` element instead.

          - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

            The CloudFront origin access identity to associate with the origin. Use an origin
            access identity to configure the origin so that viewers can *only* access objects in an
            Amazon S3 bucket through CloudFront. The format of the value is:

            origin-access-identity/cloudfront/*ID-of-origin-access-identity*

            where `` *ID-of-origin-access-identity* `` is the value that CloudFront returned in the
            ``ID`` element when you created the origin access identity.

            If you want viewers to be able to access objects using either the CloudFront URL or the
            Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

            To delete the origin access identity from an existing distribution, update the
            distribution configuration and include an empty ``OriginAccessIdentity`` element.

            To replace the origin access identity, update the distribution configuration and
            specify the new origin access identity.

            For more information about the origin access identity, see `Serving Private Content
            through CloudFront
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
            in the *Amazon CloudFront Developer Guide* .

        - **CustomOriginConfig** *(dict) --*

          A complex type that contains information about a custom origin. If the origin is an
          Amazon S3 bucket, use the ``S3OriginConfig`` element instead.

          - **HTTPPort** *(integer) --* **[REQUIRED]**

            The HTTP port the custom origin listens on.

          - **HTTPSPort** *(integer) --* **[REQUIRED]**

            The HTTPS port the custom origin listens on.

          - **OriginProtocolPolicy** *(string) --* **[REQUIRED]**

            The origin protocol policy to apply to your origin.

          - **OriginSslProtocols** *(dict) --*

            The SSL/TLS protocols that you want CloudFront to use when communicating with your
            origin over HTTPS.

            - **Quantity** *(integer) --* **[REQUIRED]**

              The number of SSL/TLS protocols that you want to allow CloudFront to use when
              establishing an HTTPS connection with this origin.

            - **Items** *(list) --* **[REQUIRED]**

              A list that contains allowed SSL/TLS protocols for this distribution.

              - *(string) --*

          - **OriginReadTimeout** *(integer) --*

            You can create a custom origin read timeout. All timeout units are in seconds. The
            default origin read timeout is 30 seconds, but you can configure custom timeout lengths
            using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60
            seconds.

            If you need to increase the maximum time limit, contact the `AWS Support Center
            <https://console.aws.amazon.com/support/home#/>`__ .

          - **OriginKeepaliveTimeout** *(integer) --*

            You can create a custom keep-alive timeout. All timeout units are in seconds. The
            default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths
            using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60
            seconds.

            If you need to increase the maximum time limit, contact the `AWS Support Center
            <https://console.aws.amazon.com/support/home#/>`__ .
    """


_RequiredClientUpdateDistributionDistributionConfigTypeDef = TypedDict(
    "_RequiredClientUpdateDistributionDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "Origins": ClientUpdateDistributionDistributionConfigOriginsTypeDef,
        "DefaultCacheBehavior": ClientUpdateDistributionDistributionConfigDefaultCacheBehaviorTypeDef,
    },
)
_OptionalClientUpdateDistributionDistributionConfigTypeDef = TypedDict(
    "_OptionalClientUpdateDistributionDistributionConfigTypeDef",
    {
        "Aliases": ClientUpdateDistributionDistributionConfigAliasesTypeDef,
        "DefaultRootObject": str,
        "OriginGroups": ClientUpdateDistributionDistributionConfigOriginGroupsTypeDef,
    },
    total=False,
)


class ClientUpdateDistributionDistributionConfigTypeDef(
    _RequiredClientUpdateDistributionDistributionConfigTypeDef,
    _OptionalClientUpdateDistributionDistributionConfigTypeDef,
):
    """
    Type definition for `ClientUpdateDistribution` `DistributionConfig`

    The distribution's configuration information.

    - **CallerReference** *(string) --* **[REQUIRED]**

      A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.

      If the value of ``CallerReference`` is new (regardless of the content of the
      ``DistributionConfig`` object), CloudFront creates a new distribution.

      If ``CallerReference`` is a value that you already sent in a previous request to create a
      distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

    - **Aliases** *(dict) --*

      A complex type that contains information about CNAMEs (alternate domain names), if any, for
      this distribution.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of CNAME aliases, if any, that you want to associate with this distribution.

      - **Items** *(list) --*

        A complex type that contains the CNAME aliases, if any, that you want to associate with this
        distribution.

        - *(string) --*

    - **DefaultRootObject** *(string) --*

      The object that you want CloudFront to request from your origin (for example, ``index.html`` )
      when a viewer requests the root URL for your distribution (``http://www.example.com`` ) instead
      of an object in your distribution (``http://www.example.com/product-description.html`` ).
      Specifying a default root object avoids exposing the contents of your distribution.

      Specify only the object name, for example, ``index.html`` . Don't add a ``/`` before the object
      name.

      If you don't want to specify a default root object when you create a distribution, include an
      empty ``DefaultRootObject`` element.

      To delete the default root object from an existing distribution, update the distribution
      configuration and include an empty ``DefaultRootObject`` element.

      To replace the default root object, update the distribution configuration and specify the new
      object.

      For more information about the default root object, see `Creating a Default Root Object
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html>`__
      in the *Amazon CloudFront Developer Guide* .

    - **Origins** *(dict) --* **[REQUIRED]**

      A complex type that contains information about origins for this distribution.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of origins or origin groups for this distribution.

      - **Items** *(list) --* **[REQUIRED]**

        A complex type that contains origins or origin groups for this distribution.

        - *(dict) --*

          A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web
          server), Amazon MediaStore, or other server from which CloudFront gets your files. This can
          also be an origin group, if you've created an origin group. You must specify at least one
          origin or origin group.

          For the current limit on the number of origins or origin groups that you can specify for a
          distribution, see `Amazon CloudFront Limits
          <https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront>`__
          in the *AWS General Reference* .

          - **Id** *(string) --* **[REQUIRED]**

            A unique identifier for the origin or origin group. The value of ``Id`` must be unique
            within the distribution.

            When you specify the value of ``TargetOriginId`` for the default cache behavior or for
            another cache behavior, you indicate the origin to which you want the cache behavior to
            route requests by specifying the value of the ``Id`` element for that origin. When a
            request matches the path pattern for that cache behavior, CloudFront routes the request
            to the specified origin. For more information, see `Cache Behavior Settings
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior>`__
            in the *Amazon CloudFront Developer Guide* .

          - **DomainName** *(string) --* **[REQUIRED]**

             **Amazon S3 origins** : The DNS name of the Amazon S3 bucket from which you want
             CloudFront to get objects for this origin, for example, ``myawsbucket.s3.amazonaws.com``
             . If you set up your bucket to be configured as a website endpoint, enter the Amazon S3
             static website hosting endpoint for the bucket.

            For more information about specifying this value for different types of origins, see
            `Origin Domain Name
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesDomainName>`__
            in the *Amazon CloudFront Developer Guide* .

            Constraints for Amazon S3 origins:

            * If you configured Amazon S3 Transfer Acceleration for your bucket, don't specify the
            ``s3-accelerate`` endpoint for ``DomainName`` .

            * The bucket name must be between 3 and 63 characters long (inclusive).

            * The bucket name must contain only lowercase characters, numbers, periods, underscores,
            and dashes.

            * The bucket name must not contain adjacent periods.

             **Custom Origins** : The DNS domain name for the HTTP server from which you want
             CloudFront to get objects for this origin, for example, ``www.example.com`` .

            Constraints for custom origins:

            * ``DomainName`` must be a valid DNS name that contains only a-z, A-Z, 0-9, dot (.),
            hyphen (-), or underscore (_) characters.

            * The name cannot exceed 128 characters.

          - **OriginPath** *(string) --*

            An optional element that causes CloudFront to request your content from a directory in
            your Amazon S3 bucket or your custom origin. When you include the ``OriginPath`` element,
            specify the directory name, beginning with a ``/`` . CloudFront appends the directory
            name to the value of ``DomainName`` , for example, ``example.com/production`` . Do not
            include a ``/`` at the end of the directory name.

            For example, suppose you've specified the following values for your distribution:

            * ``DomainName`` : An Amazon S3 bucket named ``myawsbucket`` .

            * ``OriginPath`` : ``/production``

            * ``CNAME`` : ``example.com``

            When a user enters ``example.com/index.html`` in a browser, CloudFront sends a request to
            Amazon S3 for ``myawsbucket/production/index.html`` .

            When a user enters ``example.com/acme/index.html`` in a browser, CloudFront sends a
            request to Amazon S3 for ``myawsbucket/production/acme/index.html`` .

          - **CustomHeaders** *(dict) --*

            A complex type that contains names and values for the custom headers that you want.

            - **Quantity** *(integer) --* **[REQUIRED]**

              The number of custom headers, if any, for this distribution.

            - **Items** *(list) --*

               **Optional** : A list that contains one ``OriginCustomHeader`` element for each custom
               header that you want CloudFront to forward to the origin. If Quantity is ``0`` , omit
               ``Items`` .

              - *(dict) --*

                A complex type that contains ``HeaderName`` and ``HeaderValue`` elements, if any, for
                this distribution.

                - **HeaderName** *(string) --* **[REQUIRED]**

                  The name of a header that you want CloudFront to forward to your origin. For more
                  information, see `Forwarding Custom Headers to Your Origin (Web Distributions Only)
                  <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html>`__
                  in the *Amazon CloudFront Developer Guide* .

                - **HeaderValue** *(string) --* **[REQUIRED]**

                  The value for the header that you specified in the ``HeaderName`` field.

          - **S3OriginConfig** *(dict) --*

            A complex type that contains information about the Amazon S3 origin. If the origin is a
            custom origin, use the ``CustomOriginConfig`` element instead.

            - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

              The CloudFront origin access identity to associate with the origin. Use an origin
              access identity to configure the origin so that viewers can *only* access objects in an
              Amazon S3 bucket through CloudFront. The format of the value is:

              origin-access-identity/cloudfront/*ID-of-origin-access-identity*

              where `` *ID-of-origin-access-identity* `` is the value that CloudFront returned in the
              ``ID`` element when you created the origin access identity.

              If you want viewers to be able to access objects using either the CloudFront URL or the
              Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

              To delete the origin access identity from an existing distribution, update the
              distribution configuration and include an empty ``OriginAccessIdentity`` element.

              To replace the origin access identity, update the distribution configuration and
              specify the new origin access identity.

              For more information about the origin access identity, see `Serving Private Content
              through CloudFront
              <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
              in the *Amazon CloudFront Developer Guide* .

          - **CustomOriginConfig** *(dict) --*

            A complex type that contains information about a custom origin. If the origin is an
            Amazon S3 bucket, use the ``S3OriginConfig`` element instead.

            - **HTTPPort** *(integer) --* **[REQUIRED]**

              The HTTP port the custom origin listens on.

            - **HTTPSPort** *(integer) --* **[REQUIRED]**

              The HTTPS port the custom origin listens on.

            - **OriginProtocolPolicy** *(string) --* **[REQUIRED]**

              The origin protocol policy to apply to your origin.

            - **OriginSslProtocols** *(dict) --*

              The SSL/TLS protocols that you want CloudFront to use when communicating with your
              origin over HTTPS.

              - **Quantity** *(integer) --* **[REQUIRED]**

                The number of SSL/TLS protocols that you want to allow CloudFront to use when
                establishing an HTTPS connection with this origin.

              - **Items** *(list) --* **[REQUIRED]**

                A list that contains allowed SSL/TLS protocols for this distribution.

                - *(string) --*

            - **OriginReadTimeout** *(integer) --*

              You can create a custom origin read timeout. All timeout units are in seconds. The
              default origin read timeout is 30 seconds, but you can configure custom timeout lengths
              using the CloudFront API. The minimum timeout length is 4 seconds; the maximum is 60
              seconds.

              If you need to increase the maximum time limit, contact the `AWS Support Center
              <https://console.aws.amazon.com/support/home#/>`__ .

            - **OriginKeepaliveTimeout** *(integer) --*

              You can create a custom keep-alive timeout. All timeout units are in seconds. The
              default keep-alive timeout is 5 seconds, but you can configure custom timeout lengths
              using the CloudFront API. The minimum timeout length is 1 second; the maximum is 60
              seconds.

              If you need to increase the maximum time limit, contact the `AWS Support Center
              <https://console.aws.amazon.com/support/home#/>`__ .

    - **OriginGroups** *(dict) --*

      A complex type that contains information about origin groups for this distribution.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of origin groups.

      - **Items** *(list) --*

        The items (origin groups) in a distribution.

        - *(dict) --*

          An origin group includes two origins (a primary origin and a second origin to failover to)
          and a failover criteria that you specify. You create an origin group to support origin
          failover in CloudFront. When you create or update a distribution, you can specifiy the
          origin group instead of a single origin, and CloudFront will failover from the primary
          origin to the second origin under the failover conditions that you've chosen.

          - **Id** *(string) --* **[REQUIRED]**

            The origin group's ID.

          - **FailoverCriteria** *(dict) --* **[REQUIRED]**

            A complex type that contains information about the failover criteria for an origin group.

            - **StatusCodes** *(dict) --* **[REQUIRED]**

              The status codes that, when returned from the primary origin, will trigger CloudFront
              to failover to the second origin.

              - **Quantity** *(integer) --* **[REQUIRED]**

                The number of status codes.

              - **Items** *(list) --* **[REQUIRED]**

                The items (status codes) for an origin group.

                - *(integer) --*

          - **Members** *(dict) --* **[REQUIRED]**

            A complex type that contains information about the origins in an origin group.

            - **Quantity** *(integer) --* **[REQUIRED]**

              The number of origins in an origin group.

            - **Items** *(list) --* **[REQUIRED]**

              Items (origins) in an origin group.

              - *(dict) --*

                An origin in an origin group.

                - **OriginId** *(string) --* **[REQUIRED]**

                  The ID for an origin in an origin group.

    - **DefaultCacheBehavior** *(dict) --* **[REQUIRED]**

      A complex type that describes the default cache behavior if you don't specify a
      ``CacheBehavior`` element or if files don't match any of the values of ``PathPattern`` in
      ``CacheBehavior`` elements. You must create exactly one default cache behavior.

      - **TargetOriginId** *(string) --* **[REQUIRED]**

        The value of ``ID`` for the origin that you want CloudFront to route requests to when a
        request matches the path pattern either for a cache behavior or for the default cache
        behavior in your distribution.

      - **ForwardedValues** *(dict) --* **[REQUIRED]**

        A complex type that specifies how CloudFront handles query strings and cookies.

        - **QueryString** *(boolean) --* **[REQUIRED]**

          Indicates whether you want CloudFront to forward query strings to the origin that is
          associated with this cache behavior and cache based on the query string parameters.
          CloudFront behavior depends on the value of ``QueryString`` and on the values that you
          specify for ``QueryStringCacheKeys`` , if any:

          If you specify true for ``QueryString`` and you don't specify any values for
          ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin
          and caches based on all query string parameters. Depending on how many query string
          parameters and values you have, this can adversely affect performance because CloudFront
          must forward more requests to the origin.

          If you specify true for ``QueryString`` and you specify one or more values for
          ``QueryStringCacheKeys`` , CloudFront forwards all query string parameters to the origin,
          but it only caches based on the query string parameters that you specify.

          If you specify false for ``QueryString`` , CloudFront doesn't forward any query string
          parameters to the origin, and doesn't cache based on query string parameters.

          For more information, see `Configuring CloudFront to Cache Based on Query String Parameters
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html>`__
          in the *Amazon CloudFront Developer Guide* .

        - **Cookies** *(dict) --* **[REQUIRED]**

          A complex type that specifies whether you want CloudFront to forward cookies to the origin
          and, if so, which ones. For more information about forwarding cookies to the origin, see
          `How CloudFront Forwards, Caches, and Logs Cookies
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html>`__ in the
          *Amazon CloudFront Developer Guide* .

          - **Forward** *(string) --* **[REQUIRED]**

            Specifies which cookies to forward to the origin for this cache behavior: all, none, or
            the list of cookies specified in the ``WhitelistedNames`` complex type.

            Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an
            Amazon S3 origin, specify none for the ``Forward`` element.

          - **WhitelistedNames** *(dict) --*

            Required if you specify ``whitelist`` for the value of ``Forward:`` . A complex type that
            specifies how many different cookies you want CloudFront to forward to the origin for
            this cache behavior and, if you want to forward selected cookies, the names of those
            cookies.

            If you specify ``all`` or none for the value of ``Forward`` , omit ``WhitelistedNames`` .
            If you change the value of ``Forward`` from ``whitelist`` to all or none and you don't
            delete the ``WhitelistedNames`` element and its child elements, CloudFront deletes them
            automatically.

            For the current limit on the number of cookie names that you can whitelist for each cache
            behavior, see `CloudFront Limits
            <https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront>`__
            in the *AWS General Reference* .

            - **Quantity** *(integer) --* **[REQUIRED]**

              The number of different cookies that you want CloudFront to forward to the origin for
              this cache behavior.

            - **Items** *(list) --*

              A complex type that contains one ``Name`` element for each cookie that you want
              CloudFront to forward to the origin for this cache behavior.

              - *(string) --*

        - **Headers** *(dict) --*

          A complex type that specifies the ``Headers`` , if any, that you want CloudFront to forward
          to the origin for this cache behavior (whitelisted headers). For the headers that you
          specify, CloudFront also caches separate versions of a specified object that is based on
          the header values in viewer requests.

          For more information, see `Caching Content Based on Request Headers
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html>`__
          in the *Amazon CloudFront Developer Guide* .

          - **Quantity** *(integer) --* **[REQUIRED]**

            The number of different headers that you want CloudFront to base caching on for this
            cache behavior. You can configure each cache behavior in a web distribution to do one of
            the following:

            * **Forward all headers to your origin** : Specify ``1`` for ``Quantity`` and ``*`` for
            ``Name`` .

            .. warning::

               CloudFront doesn't cache the objects that are associated with this cache behavior.
               Instead, CloudFront sends every request to the origin.

            * **Forward a whitelist of headers you specify** : Specify the number of headers that you
            want CloudFront to base caching on. Then specify the header names in ``Name`` elements.
            CloudFront caches your objects based on the values in the specified headers.

            * **Forward only the default headers** : Specify ``0`` for ``Quantity`` and omit
            ``Items`` . In this configuration, CloudFront doesn't cache based on the values in the
            request headers.

            Regardless of which option you choose, CloudFront forwards headers to your origin based
            on whether the origin is an S3 bucket or a custom origin. See the following documentation:

            * **S3 bucket** : See `HTTP Request Headers That CloudFront Removes or Updates
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorS3Origin.html#request-s3-removed-headers>`__
    """


_RequiredClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef = TypedDict(
    "_RequiredClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef",
    {"Format": str, "ContentType": str},
)
_OptionalClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef = TypedDict(
    "_OptionalClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef",
    {"ProfileId": str},
    total=False,
)


class ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef(
    _RequiredClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef,
    _OptionalClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef,
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles` `Items`

    A field-level encryption content type profile.

    - **Format** *(string) --* **[REQUIRED]**

      The format for a field-level encryption content type-profile mapping.

    - **ProfileId** *(string) --*

      The profile ID for a field-level encryption content type-profile mapping.

    - **ContentType** *(string) --* **[REQUIRED]**

      The content type for a field-level encryption content type-profile mapping.
    """


_RequiredClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef = TypedDict(
    "_RequiredClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef",
    {"Quantity": int},
)
_OptionalClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef = TypedDict(
    "_OptionalClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef",
    {
        "Items": List[
            ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef(
    _RequiredClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef,
    _OptionalClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef,
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfig` `ContentTypeProfiles`

    The configuration for a field-level encryption content type-profile.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of field-level encryption content type-profile mappings.

    - **Items** *(list) --*

      Items in a field-level encryption content type-profile mapping.

      - *(dict) --*

        A field-level encryption content type profile.

        - **Format** *(string) --* **[REQUIRED]**

          The format for a field-level encryption content type-profile mapping.

        - **ProfileId** *(string) --*

          The profile ID for a field-level encryption content type-profile mapping.

        - **ContentType** *(string) --* **[REQUIRED]**

          The content type for a field-level encryption content type-profile mapping.
    """


_RequiredClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef = TypedDict(
    "_RequiredClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef",
    {"ForwardWhenContentTypeIsUnknown": bool},
)
_OptionalClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef = TypedDict(
    "_OptionalClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef",
    {
        "ContentTypeProfiles": ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef
    },
    total=False,
)


class ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef(
    _RequiredClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef,
    _OptionalClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef,
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfig` `ContentTypeProfileConfig`

    A complex data type that specifies when to forward content if a content type isn't recognized
    and profiles to use as by default in a request if a query argument doesn't specify a profile to
    use.

    - **ForwardWhenContentTypeIsUnknown** *(boolean) --* **[REQUIRED]**

      The setting in a field-level encryption content type-profile mapping that specifies what to
      do when an unknown content type is provided for the profile. If true, content is forwarded
      without being encrypted when the content type is unknown. If false (the default), an error is
      returned when the content type is unknown.

    - **ContentTypeProfiles** *(dict) --*

      The configuration for a field-level encryption content type-profile.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of field-level encryption content type-profile mappings.

      - **Items** *(list) --*

        Items in a field-level encryption content type-profile mapping.

        - *(dict) --*

          A field-level encryption content type profile.

          - **Format** *(string) --* **[REQUIRED]**

            The format for a field-level encryption content type-profile mapping.

          - **ProfileId** *(string) --*

            The profile ID for a field-level encryption content type-profile mapping.

          - **ContentType** *(string) --* **[REQUIRED]**

            The content type for a field-level encryption content type-profile mapping.
    """


_ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef = TypedDict(
    "_ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef",
    {"QueryArg": str, "ProfileId": str},
)


class ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef(
    _ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles` `Items`

    Query argument-profile mapping for field-level encryption.

    - **QueryArg** *(string) --* **[REQUIRED]**

      Query argument for field-level encryption query argument-profile mapping.

    - **ProfileId** *(string) --* **[REQUIRED]**

      ID of profile to use for field-level encryption query argument-profile mapping
    """


_RequiredClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef = TypedDict(
    "_RequiredClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef",
    {"Quantity": int},
)
_OptionalClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef = TypedDict(
    "_OptionalClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef",
    {
        "Items": List[
            ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef(
    _RequiredClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef,
    _OptionalClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef,
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfig` `QueryArgProfiles`

    Profiles specified for query argument-profile mapping for field-level encryption.

    - **Quantity** *(integer) --* **[REQUIRED]**

      Number of profiles for query argument-profile mapping for field-level encryption.

    - **Items** *(list) --*

      Number of items for query argument-profile mapping for field-level encryption.

      - *(dict) --*

        Query argument-profile mapping for field-level encryption.

        - **QueryArg** *(string) --* **[REQUIRED]**

          Query argument for field-level encryption query argument-profile mapping.

        - **ProfileId** *(string) --* **[REQUIRED]**

          ID of profile to use for field-level encryption query argument-profile mapping
    """


_RequiredClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef = TypedDict(
    "_RequiredClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef",
    {"ForwardWhenQueryArgProfileIsUnknown": bool},
)
_OptionalClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef = TypedDict(
    "_OptionalClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef",
    {
        "QueryArgProfiles": ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef
    },
    total=False,
)


class ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef(
    _RequiredClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef,
    _OptionalClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef,
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfig` `QueryArgProfileConfig`

    A complex data type that specifies when to forward content if a profile isn't found and the
    profile that can be provided as a query argument in a request.

    - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --* **[REQUIRED]**

      Flag to set if you want a request to be forwarded to the origin even if the profile specified
      by the field-level encryption query argument, fle-profile, is unknown.

    - **QueryArgProfiles** *(dict) --*

      Profiles specified for query argument-profile mapping for field-level encryption.

      - **Quantity** *(integer) --* **[REQUIRED]**

        Number of profiles for query argument-profile mapping for field-level encryption.

      - **Items** *(list) --*

        Number of items for query argument-profile mapping for field-level encryption.

        - *(dict) --*

          Query argument-profile mapping for field-level encryption.

          - **QueryArg** *(string) --* **[REQUIRED]**

            Query argument for field-level encryption query argument-profile mapping.

          - **ProfileId** *(string) --* **[REQUIRED]**

            ID of profile to use for field-level encryption query argument-profile mapping
    """


_RequiredClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigTypeDef = TypedDict(
    "_RequiredClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigTypeDef",
    {"CallerReference": str},
)
_OptionalClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigTypeDef = TypedDict(
    "_OptionalClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigTypeDef",
    {
        "Comment": str,
        "QueryArgProfileConfig": ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef,
        "ContentTypeProfileConfig": ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef,
    },
    total=False,
)


class ClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigTypeDef(
    _RequiredClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigTypeDef,
    _OptionalClientUpdateFieldLevelEncryptionConfigFieldLevelEncryptionConfigTypeDef,
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionConfig` `FieldLevelEncryptionConfig`

    Request to update a field-level encryption configuration.

    - **CallerReference** *(string) --* **[REQUIRED]**

      A unique number that ensures the request can't be replayed.

    - **Comment** *(string) --*

      An optional comment about the configuration.

    - **QueryArgProfileConfig** *(dict) --*

      A complex data type that specifies when to forward content if a profile isn't found and the
      profile that can be provided as a query argument in a request.

      - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --* **[REQUIRED]**

        Flag to set if you want a request to be forwarded to the origin even if the profile specified
        by the field-level encryption query argument, fle-profile, is unknown.

      - **QueryArgProfiles** *(dict) --*

        Profiles specified for query argument-profile mapping for field-level encryption.

        - **Quantity** *(integer) --* **[REQUIRED]**

          Number of profiles for query argument-profile mapping for field-level encryption.

        - **Items** *(list) --*

          Number of items for query argument-profile mapping for field-level encryption.

          - *(dict) --*

            Query argument-profile mapping for field-level encryption.

            - **QueryArg** *(string) --* **[REQUIRED]**

              Query argument for field-level encryption query argument-profile mapping.

            - **ProfileId** *(string) --* **[REQUIRED]**

              ID of profile to use for field-level encryption query argument-profile mapping

    - **ContentTypeProfileConfig** *(dict) --*

      A complex data type that specifies when to forward content if a content type isn't recognized
      and profiles to use as by default in a request if a query argument doesn't specify a profile to
      use.

      - **ForwardWhenContentTypeIsUnknown** *(boolean) --* **[REQUIRED]**

        The setting in a field-level encryption content type-profile mapping that specifies what to
        do when an unknown content type is provided for the profile. If true, content is forwarded
        without being encrypted when the content type is unknown. If false (the default), an error is
        returned when the content type is unknown.

      - **ContentTypeProfiles** *(dict) --*

        The configuration for a field-level encryption content type-profile.

        - **Quantity** *(integer) --* **[REQUIRED]**

          The number of field-level encryption content type-profile mappings.

        - **Items** *(list) --*

          Items in a field-level encryption content type-profile mapping.

          - *(dict) --*

            A field-level encryption content type profile.

            - **Format** *(string) --* **[REQUIRED]**

              The format for a field-level encryption content type-profile mapping.

            - **ProfileId** *(string) --*

              The profile ID for a field-level encryption content type-profile mapping.

            - **ContentType** *(string) --* **[REQUIRED]**

              The content type for a field-level encryption content type-profile mapping.
    """


_ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef = TypedDict(
    "_ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef",
    {"Format": str, "ProfileId": str, "ContentType": str},
    total=False,
)


class ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef(
    _ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles` `Items`

    A field-level encryption content type profile.

    - **Format** *(string) --*

      The format for a field-level encryption content type-profile mapping.

    - **ProfileId** *(string) --*

      The profile ID for a field-level encryption content type-profile mapping.

    - **ContentType** *(string) --*

      The content type for a field-level encryption content type-profile mapping.
    """


_ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef = TypedDict(
    "_ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef(
    _ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfig` `ContentTypeProfiles`

    The configuration for a field-level encryption content type-profile.

    - **Quantity** *(integer) --*

      The number of field-level encryption content type-profile mappings.

    - **Items** *(list) --*

      Items in a field-level encryption content type-profile mapping.

      - *(dict) --*

        A field-level encryption content type profile.

        - **Format** *(string) --*

          The format for a field-level encryption content type-profile mapping.

        - **ProfileId** *(string) --*

          The profile ID for a field-level encryption content type-profile mapping.

        - **ContentType** *(string) --*

          The content type for a field-level encryption content type-profile mapping.
    """


_ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef = TypedDict(
    "_ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef",
    {
        "ForwardWhenContentTypeIsUnknown": bool,
        "ContentTypeProfiles": ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesTypeDef,
    },
    total=False,
)


class ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef(
    _ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfig` `ContentTypeProfileConfig`

    A complex data type that specifies when to forward content if a content type isn't
    recognized and profiles to use as by default in a request if a query argument doesn't
    specify a profile to use.

    - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

      The setting in a field-level encryption content type-profile mapping that specifies
      what to do when an unknown content type is provided for the profile. If true, content
      is forwarded without being encrypted when the content type is unknown. If false (the
      default), an error is returned when the content type is unknown.

    - **ContentTypeProfiles** *(dict) --*

      The configuration for a field-level encryption content type-profile.

      - **Quantity** *(integer) --*

        The number of field-level encryption content type-profile mappings.

      - **Items** *(list) --*

        Items in a field-level encryption content type-profile mapping.

        - *(dict) --*

          A field-level encryption content type profile.

          - **Format** *(string) --*

            The format for a field-level encryption content type-profile mapping.

          - **ProfileId** *(string) --*

            The profile ID for a field-level encryption content type-profile mapping.

          - **ContentType** *(string) --*

            The content type for a field-level encryption content type-profile mapping.
    """


_ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef = TypedDict(
    "_ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef",
    {"QueryArg": str, "ProfileId": str},
    total=False,
)


class ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef(
    _ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles` `Items`

    Query argument-profile mapping for field-level encryption.

    - **QueryArg** *(string) --*

      Query argument for field-level encryption query argument-profile mapping.

    - **ProfileId** *(string) --*

      ID of profile to use for field-level encryption query argument-profile mapping
    """


_ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef = TypedDict(
    "_ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef(
    _ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfig` `QueryArgProfiles`

    Profiles specified for query argument-profile mapping for field-level encryption.

    - **Quantity** *(integer) --*

      Number of profiles for query argument-profile mapping for field-level encryption.

    - **Items** *(list) --*

      Number of items for query argument-profile mapping for field-level encryption.

      - *(dict) --*

        Query argument-profile mapping for field-level encryption.

        - **QueryArg** *(string) --*

          Query argument for field-level encryption query argument-profile mapping.

        - **ProfileId** *(string) --*

          ID of profile to use for field-level encryption query argument-profile mapping
    """


_ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef = TypedDict(
    "_ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef",
    {
        "ForwardWhenQueryArgProfileIsUnknown": bool,
        "QueryArgProfiles": ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesTypeDef,
    },
    total=False,
)


class ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef(
    _ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfig` `QueryArgProfileConfig`

    A complex data type that specifies when to forward content if a profile isn't found and
    the profile that can be provided as a query argument in a request.

    - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

      Flag to set if you want a request to be forwarded to the origin even if the profile
      specified by the field-level encryption query argument, fle-profile, is unknown.

    - **QueryArgProfiles** *(dict) --*

      Profiles specified for query argument-profile mapping for field-level encryption.

      - **Quantity** *(integer) --*

        Number of profiles for query argument-profile mapping for field-level encryption.

      - **Items** *(list) --*

        Number of items for query argument-profile mapping for field-level encryption.

        - *(dict) --*

          Query argument-profile mapping for field-level encryption.

          - **QueryArg** *(string) --*

            Query argument for field-level encryption query argument-profile mapping.

          - **ProfileId** *(string) --*

            ID of profile to use for field-level encryption query argument-profile mapping
    """


_ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigTypeDef = TypedDict(
    "_ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigTypeDef",
    {
        "CallerReference": str,
        "Comment": str,
        "QueryArgProfileConfig": ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigQueryArgProfileConfigTypeDef,
        "ContentTypeProfileConfig": ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigContentTypeProfileConfigTypeDef,
    },
    total=False,
)


class ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigTypeDef(
    _ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigTypeDef
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryption` `FieldLevelEncryptionConfig`

    A complex data type that includes the profile configurations specified for field-level
    encryption.

    - **CallerReference** *(string) --*

      A unique number that ensures the request can't be replayed.

    - **Comment** *(string) --*

      An optional comment about the configuration.

    - **QueryArgProfileConfig** *(dict) --*

      A complex data type that specifies when to forward content if a profile isn't found and
      the profile that can be provided as a query argument in a request.

      - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

        Flag to set if you want a request to be forwarded to the origin even if the profile
        specified by the field-level encryption query argument, fle-profile, is unknown.

      - **QueryArgProfiles** *(dict) --*

        Profiles specified for query argument-profile mapping for field-level encryption.

        - **Quantity** *(integer) --*

          Number of profiles for query argument-profile mapping for field-level encryption.

        - **Items** *(list) --*

          Number of items for query argument-profile mapping for field-level encryption.

          - *(dict) --*

            Query argument-profile mapping for field-level encryption.

            - **QueryArg** *(string) --*

              Query argument for field-level encryption query argument-profile mapping.

            - **ProfileId** *(string) --*

              ID of profile to use for field-level encryption query argument-profile mapping

    - **ContentTypeProfileConfig** *(dict) --*

      A complex data type that specifies when to forward content if a content type isn't
      recognized and profiles to use as by default in a request if a query argument doesn't
      specify a profile to use.

      - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

        The setting in a field-level encryption content type-profile mapping that specifies
        what to do when an unknown content type is provided for the profile. If true, content
        is forwarded without being encrypted when the content type is unknown. If false (the
        default), an error is returned when the content type is unknown.

      - **ContentTypeProfiles** *(dict) --*

        The configuration for a field-level encryption content type-profile.

        - **Quantity** *(integer) --*

          The number of field-level encryption content type-profile mappings.

        - **Items** *(list) --*

          Items in a field-level encryption content type-profile mapping.

          - *(dict) --*

            A field-level encryption content type profile.

            - **Format** *(string) --*

              The format for a field-level encryption content type-profile mapping.

            - **ProfileId** *(string) --*

              The profile ID for a field-level encryption content type-profile mapping.

            - **ContentType** *(string) --*

              The content type for a field-level encryption content type-profile mapping.
    """


_ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionTypeDef = TypedDict(
    "_ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "FieldLevelEncryptionConfig": ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionFieldLevelEncryptionConfigTypeDef,
    },
    total=False,
)


class ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionTypeDef(
    _ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionTypeDef
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionConfigResponse` `FieldLevelEncryption`

    Return the results of updating the configuration.

    - **Id** *(string) --*

      The configuration ID for a field-level encryption configuration which includes a set of
      profiles that specify certain selected data fields to be encrypted by specific public keys.

    - **LastModifiedTime** *(datetime) --*

      The last time the field-level encryption configuration was changed.

    - **FieldLevelEncryptionConfig** *(dict) --*

      A complex data type that includes the profile configurations specified for field-level
      encryption.

      - **CallerReference** *(string) --*

        A unique number that ensures the request can't be replayed.

      - **Comment** *(string) --*

        An optional comment about the configuration.

      - **QueryArgProfileConfig** *(dict) --*

        A complex data type that specifies when to forward content if a profile isn't found and
        the profile that can be provided as a query argument in a request.

        - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

          Flag to set if you want a request to be forwarded to the origin even if the profile
          specified by the field-level encryption query argument, fle-profile, is unknown.

        - **QueryArgProfiles** *(dict) --*

          Profiles specified for query argument-profile mapping for field-level encryption.

          - **Quantity** *(integer) --*

            Number of profiles for query argument-profile mapping for field-level encryption.

          - **Items** *(list) --*

            Number of items for query argument-profile mapping for field-level encryption.

            - *(dict) --*

              Query argument-profile mapping for field-level encryption.

              - **QueryArg** *(string) --*

                Query argument for field-level encryption query argument-profile mapping.

              - **ProfileId** *(string) --*

                ID of profile to use for field-level encryption query argument-profile mapping

      - **ContentTypeProfileConfig** *(dict) --*

        A complex data type that specifies when to forward content if a content type isn't
        recognized and profiles to use as by default in a request if a query argument doesn't
        specify a profile to use.

        - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

          The setting in a field-level encryption content type-profile mapping that specifies
          what to do when an unknown content type is provided for the profile. If true, content
          is forwarded without being encrypted when the content type is unknown. If false (the
          default), an error is returned when the content type is unknown.

        - **ContentTypeProfiles** *(dict) --*

          The configuration for a field-level encryption content type-profile.

          - **Quantity** *(integer) --*

            The number of field-level encryption content type-profile mappings.

          - **Items** *(list) --*

            Items in a field-level encryption content type-profile mapping.

            - *(dict) --*

              A field-level encryption content type profile.

              - **Format** *(string) --*

                The format for a field-level encryption content type-profile mapping.

              - **ProfileId** *(string) --*

                The profile ID for a field-level encryption content type-profile mapping.

              - **ContentType** *(string) --*

                The content type for a field-level encryption content type-profile mapping.
    """


_ClientUpdateFieldLevelEncryptionConfigResponseTypeDef = TypedDict(
    "_ClientUpdateFieldLevelEncryptionConfigResponseTypeDef",
    {
        "FieldLevelEncryption": ClientUpdateFieldLevelEncryptionConfigResponseFieldLevelEncryptionTypeDef,
        "ETag": str,
    },
    total=False,
)


class ClientUpdateFieldLevelEncryptionConfigResponseTypeDef(
    _ClientUpdateFieldLevelEncryptionConfigResponseTypeDef
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionConfig` `Response`

    - **FieldLevelEncryption** *(dict) --*

      Return the results of updating the configuration.

      - **Id** *(string) --*

        The configuration ID for a field-level encryption configuration which includes a set of
        profiles that specify certain selected data fields to be encrypted by specific public keys.

      - **LastModifiedTime** *(datetime) --*

        The last time the field-level encryption configuration was changed.

      - **FieldLevelEncryptionConfig** *(dict) --*

        A complex data type that includes the profile configurations specified for field-level
        encryption.

        - **CallerReference** *(string) --*

          A unique number that ensures the request can't be replayed.

        - **Comment** *(string) --*

          An optional comment about the configuration.

        - **QueryArgProfileConfig** *(dict) --*

          A complex data type that specifies when to forward content if a profile isn't found and
          the profile that can be provided as a query argument in a request.

          - **ForwardWhenQueryArgProfileIsUnknown** *(boolean) --*

            Flag to set if you want a request to be forwarded to the origin even if the profile
            specified by the field-level encryption query argument, fle-profile, is unknown.

          - **QueryArgProfiles** *(dict) --*

            Profiles specified for query argument-profile mapping for field-level encryption.

            - **Quantity** *(integer) --*

              Number of profiles for query argument-profile mapping for field-level encryption.

            - **Items** *(list) --*

              Number of items for query argument-profile mapping for field-level encryption.

              - *(dict) --*

                Query argument-profile mapping for field-level encryption.

                - **QueryArg** *(string) --*

                  Query argument for field-level encryption query argument-profile mapping.

                - **ProfileId** *(string) --*

                  ID of profile to use for field-level encryption query argument-profile mapping

        - **ContentTypeProfileConfig** *(dict) --*

          A complex data type that specifies when to forward content if a content type isn't
          recognized and profiles to use as by default in a request if a query argument doesn't
          specify a profile to use.

          - **ForwardWhenContentTypeIsUnknown** *(boolean) --*

            The setting in a field-level encryption content type-profile mapping that specifies
            what to do when an unknown content type is provided for the profile. If true, content
            is forwarded without being encrypted when the content type is unknown. If false (the
            default), an error is returned when the content type is unknown.

          - **ContentTypeProfiles** *(dict) --*

            The configuration for a field-level encryption content type-profile.

            - **Quantity** *(integer) --*

              The number of field-level encryption content type-profile mappings.

            - **Items** *(list) --*

              Items in a field-level encryption content type-profile mapping.

              - *(dict) --*

                A field-level encryption content type profile.

                - **Format** *(string) --*

                  The format for a field-level encryption content type-profile mapping.

                - **ProfileId** *(string) --*

                  The profile ID for a field-level encryption content type-profile mapping.

                - **ContentType** *(string) --*

                  The content type for a field-level encryption content type-profile mapping.

    - **ETag** *(string) --*

      The value of the ``ETag`` header that you received when updating the configuration. For
      example: ``E2QWRUHAPOMQZL`` .
    """


_RequiredClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef = TypedDict(
    "_RequiredClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef",
    {"Quantity": int},
)
_OptionalClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef = TypedDict(
    "_OptionalClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef",
    {"Items": List[str]},
    total=False,
)


class ClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef(
    _RequiredClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef,
    _OptionalClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef,
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItems` `FieldPatterns`

    Field patterns in a field-level encryption content type profile specify the fields that
    you want to be encrypted. You can provide the full field name, or any beginning
    characters followed by a wildcard (*). You can't overlap field patterns. For example, you
    can't have both ABC* and AB*. Note that field patterns are case-sensitive.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of field-level encryption field patterns.

    - **Items** *(list) --*

      An array of the field-level encryption field patterns.

      - *(string) --*
    """


_ClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef = TypedDict(
    "_ClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef",
    {
        "PublicKeyId": str,
        "ProviderId": str,
        "FieldPatterns": ClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef,
    },
)


class ClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef(
    _ClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntities` `Items`

    Complex data type for field-level encryption profiles that includes the encryption key and
    field pattern specifications.

    - **PublicKeyId** *(string) --* **[REQUIRED]**

      The public key associated with a set of field-level encryption patterns, to be used when
      encrypting the fields that match the patterns.

    - **ProviderId** *(string) --* **[REQUIRED]**

      The provider associated with the public key being used for encryption. This value must
      also be provided with the private key for applications to be able to decrypt data.

    - **FieldPatterns** *(dict) --* **[REQUIRED]**

      Field patterns in a field-level encryption content type profile specify the fields that
      you want to be encrypted. You can provide the full field name, or any beginning
      characters followed by a wildcard (*). You can't overlap field patterns. For example, you
      can't have both ABC* and AB*. Note that field patterns are case-sensitive.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of field-level encryption field patterns.

      - **Items** *(list) --*

        An array of the field-level encryption field patterns.

        - *(string) --*
    """


_RequiredClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef = TypedDict(
    "_RequiredClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef",
    {"Quantity": int},
)
_OptionalClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef = TypedDict(
    "_OptionalClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef",
    {
        "Items": List[
            ClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef
        ]
    },
    total=False,
)


class ClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef(
    _RequiredClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef,
    _OptionalClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef,
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfig` `EncryptionEntities`

    A complex data type of encryption entities for the field-level encryption profile that include
    the public key ID, provider, and field patterns for specifying which fields to encrypt with
    this key.

    - **Quantity** *(integer) --* **[REQUIRED]**

      Number of field pattern items in a field-level encryption content type-profile mapping.

    - **Items** *(list) --*

      An array of field patterns in a field-level encryption content type-profile mapping.

      - *(dict) --*

        Complex data type for field-level encryption profiles that includes the encryption key and
        field pattern specifications.

        - **PublicKeyId** *(string) --* **[REQUIRED]**

          The public key associated with a set of field-level encryption patterns, to be used when
          encrypting the fields that match the patterns.

        - **ProviderId** *(string) --* **[REQUIRED]**

          The provider associated with the public key being used for encryption. This value must
          also be provided with the private key for applications to be able to decrypt data.

        - **FieldPatterns** *(dict) --* **[REQUIRED]**

          Field patterns in a field-level encryption content type profile specify the fields that
          you want to be encrypted. You can provide the full field name, or any beginning
          characters followed by a wildcard (*). You can't overlap field patterns. For example, you
          can't have both ABC* and AB*. Note that field patterns are case-sensitive.

          - **Quantity** *(integer) --* **[REQUIRED]**

            The number of field-level encryption field patterns.

          - **Items** *(list) --*

            An array of the field-level encryption field patterns.

            - *(string) --*
    """


_RequiredClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef = TypedDict(
    "_RequiredClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef",
    {
        "Name": str,
        "CallerReference": str,
        "EncryptionEntities": ClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef,
    },
)
_OptionalClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef = TypedDict(
    "_OptionalClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef",
    {"Comment": str},
    total=False,
)


class ClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef(
    _RequiredClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef,
    _OptionalClientUpdateFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef,
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionProfile` `FieldLevelEncryptionProfileConfig`

    Request to update a field-level encryption profile.

    - **Name** *(string) --* **[REQUIRED]**

      Profile name for the field-level encryption profile.

    - **CallerReference** *(string) --* **[REQUIRED]**

      A unique number that ensures that the request can't be replayed.

    - **Comment** *(string) --*

      An optional comment for the field-level encryption profile.

    - **EncryptionEntities** *(dict) --* **[REQUIRED]**

      A complex data type of encryption entities for the field-level encryption profile that include
      the public key ID, provider, and field patterns for specifying which fields to encrypt with
      this key.

      - **Quantity** *(integer) --* **[REQUIRED]**

        Number of field pattern items in a field-level encryption content type-profile mapping.

      - **Items** *(list) --*

        An array of field patterns in a field-level encryption content type-profile mapping.

        - *(dict) --*

          Complex data type for field-level encryption profiles that includes the encryption key and
          field pattern specifications.

          - **PublicKeyId** *(string) --* **[REQUIRED]**

            The public key associated with a set of field-level encryption patterns, to be used when
            encrypting the fields that match the patterns.

          - **ProviderId** *(string) --* **[REQUIRED]**

            The provider associated with the public key being used for encryption. This value must
            also be provided with the private key for applications to be able to decrypt data.

          - **FieldPatterns** *(dict) --* **[REQUIRED]**

            Field patterns in a field-level encryption content type profile specify the fields that
            you want to be encrypted. You can provide the full field name, or any beginning
            characters followed by a wildcard (*). You can't overlap field patterns. For example, you
            can't have both ABC* and AB*. Note that field patterns are case-sensitive.

            - **Quantity** *(integer) --* **[REQUIRED]**

              The number of field-level encryption field patterns.

            - **Items** *(list) --*

              An array of the field-level encryption field patterns.

              - *(string) --*
    """


_ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef = TypedDict(
    "_ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef",
    {"Quantity": int, "Items": List[str]},
    total=False,
)


class ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef(
    _ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItems` `FieldPatterns`

    Field patterns in a field-level encryption content type profile specify the fields
    that you want to be encrypted. You can provide the full field name, or any
    beginning characters followed by a wildcard (*). You can't overlap field patterns.
    For example, you can't have both ABC* and AB*. Note that field patterns are
    case-sensitive.

    - **Quantity** *(integer) --*

      The number of field-level encryption field patterns.

    - **Items** *(list) --*

      An array of the field-level encryption field patterns.

      - *(string) --*
    """


_ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef = TypedDict(
    "_ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef",
    {
        "PublicKeyId": str,
        "ProviderId": str,
        "FieldPatterns": ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsFieldPatternsTypeDef,
    },
    total=False,
)


class ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef(
    _ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntities` `Items`

    Complex data type for field-level encryption profiles that includes the encryption
    key and field pattern specifications.

    - **PublicKeyId** *(string) --*

      The public key associated with a set of field-level encryption patterns, to be used
      when encrypting the fields that match the patterns.

    - **ProviderId** *(string) --*

      The provider associated with the public key being used for encryption. This value
      must also be provided with the private key for applications to be able to decrypt
      data.

    - **FieldPatterns** *(dict) --*

      Field patterns in a field-level encryption content type profile specify the fields
      that you want to be encrypted. You can provide the full field name, or any
      beginning characters followed by a wildcard (*). You can't overlap field patterns.
      For example, you can't have both ABC* and AB*. Note that field patterns are
      case-sensitive.

      - **Quantity** *(integer) --*

        The number of field-level encryption field patterns.

      - **Items** *(list) --*

        An array of the field-level encryption field patterns.

        - *(string) --*
    """


_ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef = TypedDict(
    "_ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef",
    {
        "Quantity": int,
        "Items": List[
            ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesItemsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef(
    _ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfig` `EncryptionEntities`

    A complex data type of encryption entities for the field-level encryption profile that
    include the public key ID, provider, and field patterns for specifying which fields to
    encrypt with this key.

    - **Quantity** *(integer) --*

      Number of field pattern items in a field-level encryption content type-profile mapping.

    - **Items** *(list) --*

      An array of field patterns in a field-level encryption content type-profile mapping.

      - *(dict) --*

        Complex data type for field-level encryption profiles that includes the encryption
        key and field pattern specifications.

        - **PublicKeyId** *(string) --*

          The public key associated with a set of field-level encryption patterns, to be used
          when encrypting the fields that match the patterns.

        - **ProviderId** *(string) --*

          The provider associated with the public key being used for encryption. This value
          must also be provided with the private key for applications to be able to decrypt
          data.

        - **FieldPatterns** *(dict) --*

          Field patterns in a field-level encryption content type profile specify the fields
          that you want to be encrypted. You can provide the full field name, or any
          beginning characters followed by a wildcard (*). You can't overlap field patterns.
          For example, you can't have both ABC* and AB*. Note that field patterns are
          case-sensitive.

          - **Quantity** *(integer) --*

            The number of field-level encryption field patterns.

          - **Items** *(list) --*

            An array of the field-level encryption field patterns.

            - *(string) --*
    """


_ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef = TypedDict(
    "_ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef",
    {
        "Name": str,
        "CallerReference": str,
        "Comment": str,
        "EncryptionEntities": ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigEncryptionEntitiesTypeDef,
    },
    total=False,
)


class ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef(
    _ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfile` `FieldLevelEncryptionProfileConfig`

    A complex data type that includes the profile name and the encryption entities for the
    field-level encryption profile.

    - **Name** *(string) --*

      Profile name for the field-level encryption profile.

    - **CallerReference** *(string) --*

      A unique number that ensures that the request can't be replayed.

    - **Comment** *(string) --*

      An optional comment for the field-level encryption profile.

    - **EncryptionEntities** *(dict) --*

      A complex data type of encryption entities for the field-level encryption profile that
      include the public key ID, provider, and field patterns for specifying which fields to
      encrypt with this key.

      - **Quantity** *(integer) --*

        Number of field pattern items in a field-level encryption content type-profile mapping.

      - **Items** *(list) --*

        An array of field patterns in a field-level encryption content type-profile mapping.

        - *(dict) --*

          Complex data type for field-level encryption profiles that includes the encryption
          key and field pattern specifications.

          - **PublicKeyId** *(string) --*

            The public key associated with a set of field-level encryption patterns, to be used
            when encrypting the fields that match the patterns.

          - **ProviderId** *(string) --*

            The provider associated with the public key being used for encryption. This value
            must also be provided with the private key for applications to be able to decrypt
            data.

          - **FieldPatterns** *(dict) --*

            Field patterns in a field-level encryption content type profile specify the fields
            that you want to be encrypted. You can provide the full field name, or any
            beginning characters followed by a wildcard (*). You can't overlap field patterns.
            For example, you can't have both ABC* and AB*. Note that field patterns are
            case-sensitive.

            - **Quantity** *(integer) --*

              The number of field-level encryption field patterns.

            - **Items** *(list) --*

              An array of the field-level encryption field patterns.

              - *(string) --*
    """


_ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileTypeDef = TypedDict(
    "_ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileTypeDef",
    {
        "Id": str,
        "LastModifiedTime": datetime,
        "FieldLevelEncryptionProfileConfig": ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileFieldLevelEncryptionProfileConfigTypeDef,
    },
    total=False,
)


class ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileTypeDef(
    _ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileTypeDef
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionProfileResponse` `FieldLevelEncryptionProfile`

    Return the results of updating the profile.

    - **Id** *(string) --*

      The ID for a field-level encryption profile configuration which includes a set of profiles
      that specify certain selected data fields to be encrypted by specific public keys.

    - **LastModifiedTime** *(datetime) --*

      The last time the field-level encryption profile was updated.

    - **FieldLevelEncryptionProfileConfig** *(dict) --*

      A complex data type that includes the profile name and the encryption entities for the
      field-level encryption profile.

      - **Name** *(string) --*

        Profile name for the field-level encryption profile.

      - **CallerReference** *(string) --*

        A unique number that ensures that the request can't be replayed.

      - **Comment** *(string) --*

        An optional comment for the field-level encryption profile.

      - **EncryptionEntities** *(dict) --*

        A complex data type of encryption entities for the field-level encryption profile that
        include the public key ID, provider, and field patterns for specifying which fields to
        encrypt with this key.

        - **Quantity** *(integer) --*

          Number of field pattern items in a field-level encryption content type-profile mapping.

        - **Items** *(list) --*

          An array of field patterns in a field-level encryption content type-profile mapping.

          - *(dict) --*

            Complex data type for field-level encryption profiles that includes the encryption
            key and field pattern specifications.

            - **PublicKeyId** *(string) --*

              The public key associated with a set of field-level encryption patterns, to be used
              when encrypting the fields that match the patterns.

            - **ProviderId** *(string) --*

              The provider associated with the public key being used for encryption. This value
              must also be provided with the private key for applications to be able to decrypt
              data.

            - **FieldPatterns** *(dict) --*

              Field patterns in a field-level encryption content type profile specify the fields
              that you want to be encrypted. You can provide the full field name, or any
              beginning characters followed by a wildcard (*). You can't overlap field patterns.
              For example, you can't have both ABC* and AB*. Note that field patterns are
              case-sensitive.

              - **Quantity** *(integer) --*

                The number of field-level encryption field patterns.

              - **Items** *(list) --*

                An array of the field-level encryption field patterns.

                - *(string) --*
    """


_ClientUpdateFieldLevelEncryptionProfileResponseTypeDef = TypedDict(
    "_ClientUpdateFieldLevelEncryptionProfileResponseTypeDef",
    {
        "FieldLevelEncryptionProfile": ClientUpdateFieldLevelEncryptionProfileResponseFieldLevelEncryptionProfileTypeDef,
        "ETag": str,
    },
    total=False,
)


class ClientUpdateFieldLevelEncryptionProfileResponseTypeDef(
    _ClientUpdateFieldLevelEncryptionProfileResponseTypeDef
):
    """
    Type definition for `ClientUpdateFieldLevelEncryptionProfile` `Response`

    - **FieldLevelEncryptionProfile** *(dict) --*

      Return the results of updating the profile.

      - **Id** *(string) --*

        The ID for a field-level encryption profile configuration which includes a set of profiles
        that specify certain selected data fields to be encrypted by specific public keys.

      - **LastModifiedTime** *(datetime) --*

        The last time the field-level encryption profile was updated.

      - **FieldLevelEncryptionProfileConfig** *(dict) --*

        A complex data type that includes the profile name and the encryption entities for the
        field-level encryption profile.

        - **Name** *(string) --*

          Profile name for the field-level encryption profile.

        - **CallerReference** *(string) --*

          A unique number that ensures that the request can't be replayed.

        - **Comment** *(string) --*

          An optional comment for the field-level encryption profile.

        - **EncryptionEntities** *(dict) --*

          A complex data type of encryption entities for the field-level encryption profile that
          include the public key ID, provider, and field patterns for specifying which fields to
          encrypt with this key.

          - **Quantity** *(integer) --*

            Number of field pattern items in a field-level encryption content type-profile mapping.

          - **Items** *(list) --*

            An array of field patterns in a field-level encryption content type-profile mapping.

            - *(dict) --*

              Complex data type for field-level encryption profiles that includes the encryption
              key and field pattern specifications.

              - **PublicKeyId** *(string) --*

                The public key associated with a set of field-level encryption patterns, to be used
                when encrypting the fields that match the patterns.

              - **ProviderId** *(string) --*

                The provider associated with the public key being used for encryption. This value
                must also be provided with the private key for applications to be able to decrypt
                data.

              - **FieldPatterns** *(dict) --*

                Field patterns in a field-level encryption content type profile specify the fields
                that you want to be encrypted. You can provide the full field name, or any
                beginning characters followed by a wildcard (*). You can't overlap field patterns.
                For example, you can't have both ABC* and AB*. Note that field patterns are
                case-sensitive.

                - **Quantity** *(integer) --*

                  The number of field-level encryption field patterns.

                - **Items** *(list) --*

                  An array of the field-level encryption field patterns.

                  - *(string) --*

    - **ETag** *(string) --*

      The result of the field-level encryption profile request.
    """


_RequiredClientUpdatePublicKeyPublicKeyConfigTypeDef = TypedDict(
    "_RequiredClientUpdatePublicKeyPublicKeyConfigTypeDef",
    {"CallerReference": str, "Name": str, "EncodedKey": str},
)
_OptionalClientUpdatePublicKeyPublicKeyConfigTypeDef = TypedDict(
    "_OptionalClientUpdatePublicKeyPublicKeyConfigTypeDef",
    {"Comment": str},
    total=False,
)


class ClientUpdatePublicKeyPublicKeyConfigTypeDef(
    _RequiredClientUpdatePublicKeyPublicKeyConfigTypeDef,
    _OptionalClientUpdatePublicKeyPublicKeyConfigTypeDef,
):
    """
    Type definition for `ClientUpdatePublicKey` `PublicKeyConfig`

    Request to update public key information.

    - **CallerReference** *(string) --* **[REQUIRED]**

      A unique number that ensures that the request can't be replayed.

    - **Name** *(string) --* **[REQUIRED]**

      The name for a public key you add to CloudFront to use with features like field-level
      encryption.

    - **EncodedKey** *(string) --* **[REQUIRED]**

      The encoded public key that you want to add to CloudFront to use with features like field-level
      encryption.

    - **Comment** *(string) --*

      An optional comment about a public key.
    """


_ClientUpdatePublicKeyResponsePublicKeyPublicKeyConfigTypeDef = TypedDict(
    "_ClientUpdatePublicKeyResponsePublicKeyPublicKeyConfigTypeDef",
    {"CallerReference": str, "Name": str, "EncodedKey": str, "Comment": str},
    total=False,
)


class ClientUpdatePublicKeyResponsePublicKeyPublicKeyConfigTypeDef(
    _ClientUpdatePublicKeyResponsePublicKeyPublicKeyConfigTypeDef
):
    """
    Type definition for `ClientUpdatePublicKeyResponsePublicKey` `PublicKeyConfig`

    A complex data type for a public key you add to CloudFront to use with features like
    field-level encryption.

    - **CallerReference** *(string) --*

      A unique number that ensures that the request can't be replayed.

    - **Name** *(string) --*

      The name for a public key you add to CloudFront to use with features like field-level
      encryption.

    - **EncodedKey** *(string) --*

      The encoded public key that you want to add to CloudFront to use with features like
      field-level encryption.

    - **Comment** *(string) --*

      An optional comment about a public key.
    """


_ClientUpdatePublicKeyResponsePublicKeyTypeDef = TypedDict(
    "_ClientUpdatePublicKeyResponsePublicKeyTypeDef",
    {
        "Id": str,
        "CreatedTime": datetime,
        "PublicKeyConfig": ClientUpdatePublicKeyResponsePublicKeyPublicKeyConfigTypeDef,
    },
    total=False,
)


class ClientUpdatePublicKeyResponsePublicKeyTypeDef(
    _ClientUpdatePublicKeyResponsePublicKeyTypeDef
):
    """
    Type definition for `ClientUpdatePublicKeyResponse` `PublicKey`

    Return the results of updating the public key.

    - **Id** *(string) --*

      A unique ID assigned to a public key you've added to CloudFront.

    - **CreatedTime** *(datetime) --*

      A time you added a public key to CloudFront.

    - **PublicKeyConfig** *(dict) --*

      A complex data type for a public key you add to CloudFront to use with features like
      field-level encryption.

      - **CallerReference** *(string) --*

        A unique number that ensures that the request can't be replayed.

      - **Name** *(string) --*

        The name for a public key you add to CloudFront to use with features like field-level
        encryption.

      - **EncodedKey** *(string) --*

        The encoded public key that you want to add to CloudFront to use with features like
        field-level encryption.

      - **Comment** *(string) --*

        An optional comment about a public key.
    """


_ClientUpdatePublicKeyResponseTypeDef = TypedDict(
    "_ClientUpdatePublicKeyResponseTypeDef",
    {"PublicKey": ClientUpdatePublicKeyResponsePublicKeyTypeDef, "ETag": str},
    total=False,
)


class ClientUpdatePublicKeyResponseTypeDef(_ClientUpdatePublicKeyResponseTypeDef):
    """
    Type definition for `ClientUpdatePublicKey` `Response`

    - **PublicKey** *(dict) --*

      Return the results of updating the public key.

      - **Id** *(string) --*

        A unique ID assigned to a public key you've added to CloudFront.

      - **CreatedTime** *(datetime) --*

        A time you added a public key to CloudFront.

      - **PublicKeyConfig** *(dict) --*

        A complex data type for a public key you add to CloudFront to use with features like
        field-level encryption.

        - **CallerReference** *(string) --*

          A unique number that ensures that the request can't be replayed.

        - **Name** *(string) --*

          The name for a public key you add to CloudFront to use with features like field-level
          encryption.

        - **EncodedKey** *(string) --*

          The encoded public key that you want to add to CloudFront to use with features like
          field-level encryption.

        - **Comment** *(string) --*

          An optional comment about a public key.

    - **ETag** *(string) --*

      The current version of the update public key result. For example: ``E2QWRUHAPOMQZL`` .
    """


_ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef = TypedDict(
    "_ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef",
    {"Quantity": int, "Items": List[str]},
    total=False,
)


class ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef(
    _ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef
):
    """
    Type definition for `ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItems` `KeyPairIds`

    A complex type that lists the active CloudFront key pairs, if any, that are
    associated with ``AwsAccountNumber`` .

    - **Quantity** *(integer) --*

      The number of active CloudFront key pairs for ``AwsAccountNumber`` .

      For more information, see `ActiveTrustedSigners
      <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
      .

    - **Items** *(list) --*

      A complex type that lists the active CloudFront key pairs, if any, that are
      associated with ``AwsAccountNumber`` .

      For more information, see `ActiveTrustedSigners
      <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
      .

      - *(string) --*
    """


_ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsTypeDef = TypedDict(
    "_ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsTypeDef",
    {
        "AwsAccountNumber": str,
        "KeyPairIds": ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsKeyPairIdsTypeDef,
    },
    total=False,
)


class ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsTypeDef(
    _ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsTypeDef
):
    """
    Type definition for `ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSigners` `Items`

    A complex type that lists the AWS accounts that were included in the ``TrustedSigners``
    complex type, as well as their active CloudFront key pair IDs, if any.

    - **AwsAccountNumber** *(string) --*

      An AWS account that is included in the ``TrustedSigners`` complex type for this
      distribution. Valid values include:

      * ``self`` , which is the AWS account used to create the distribution.

      * An AWS account number.

    - **KeyPairIds** *(dict) --*

      A complex type that lists the active CloudFront key pairs, if any, that are
      associated with ``AwsAccountNumber`` .

      - **Quantity** *(integer) --*

        The number of active CloudFront key pairs for ``AwsAccountNumber`` .

        For more information, see `ActiveTrustedSigners
        <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
        .

      - **Items** *(list) --*

        A complex type that lists the active CloudFront key pairs, if any, that are
        associated with ``AwsAccountNumber`` .

        For more information, see `ActiveTrustedSigners
        <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
        .

        - *(string) --*
    """


_ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersTypeDef = TypedDict(
    "_ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersTypeDef",
    {
        "Enabled": bool,
        "Quantity": int,
        "Items": List[
            ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersItemsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersTypeDef(
    _ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersTypeDef
):
    """
    Type definition for `ClientUpdateStreamingDistributionResponseStreamingDistribution` `ActiveTrustedSigners`

    A complex type that lists the AWS accounts, if any, that you included in the
    ``TrustedSigners`` complex type for this distribution. These are the accounts that you want
    to allow to create signed URLs for private content.

    The ``Signer`` complex type lists the AWS account number of the trusted signer or ``self``
    if the signer is the AWS account that created the distribution. The ``Signer`` element also
    includes the IDs of any active CloudFront key pairs that are associated with the trusted
    signer's AWS account. If no ``KeyPairId`` element appears for a ``Signer`` , that signer
    can't create signed URLs.

    For more information, see `Serving Private Content through CloudFront
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
    in the *Amazon CloudFront Developer Guide* .

    - **Enabled** *(boolean) --*

      Enabled is ``true`` if any of the AWS accounts listed in the ``TrustedSigners`` complex
      type for this distribution have active CloudFront key pairs. If not, ``Enabled`` is
      ``false`` .

    - **Quantity** *(integer) --*

      The number of trusted signers specified in the ``TrustedSigners`` complex type.

    - **Items** *(list) --*

      A complex type that contains one ``Signer`` complex type for each trusted signer that is
      specified in the ``TrustedSigners`` complex type.

      - *(dict) --*

        A complex type that lists the AWS accounts that were included in the ``TrustedSigners``
        complex type, as well as their active CloudFront key pair IDs, if any.

        - **AwsAccountNumber** *(string) --*

          An AWS account that is included in the ``TrustedSigners`` complex type for this
          distribution. Valid values include:

          * ``self`` , which is the AWS account used to create the distribution.

          * An AWS account number.

        - **KeyPairIds** *(dict) --*

          A complex type that lists the active CloudFront key pairs, if any, that are
          associated with ``AwsAccountNumber`` .

          - **Quantity** *(integer) --*

            The number of active CloudFront key pairs for ``AwsAccountNumber`` .

            For more information, see `ActiveTrustedSigners
            <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
            .

          - **Items** *(list) --*

            A complex type that lists the active CloudFront key pairs, if any, that are
            associated with ``AwsAccountNumber`` .

            For more information, see `ActiveTrustedSigners
            <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
            .

            - *(string) --*
    """


_ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef = TypedDict(
    "_ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef",
    {"Quantity": int, "Items": List[str]},
    total=False,
)


class ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef(
    _ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef
):
    """
    Type definition for `ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfig` `Aliases`

    A complex type that contains information about CNAMEs (alternate domain names), if any,
    for this streaming distribution.

    - **Quantity** *(integer) --*

      The number of CNAME aliases, if any, that you want to associate with this distribution.

    - **Items** *(list) --*

      A complex type that contains the CNAME aliases, if any, that you want to associate with
      this distribution.

      - *(string) --*
    """


_ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef = TypedDict(
    "_ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef",
    {"Enabled": bool, "Bucket": str, "Prefix": str},
    total=False,
)


class ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef(
    _ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef
):
    """
    Type definition for `ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfig` `Logging`

    A complex type that controls whether access logs are written for the streaming
    distribution.

    - **Enabled** *(boolean) --*

      Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If
      you don't want to enable logging when you create a streaming distribution or if you
      want to disable logging for an existing streaming distribution, specify ``false`` for
      ``Enabled`` , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify
      ``false`` for ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the
      values are automatically deleted.

    - **Bucket** *(string) --*

      The Amazon S3 bucket to store the access logs in, for example,
      ``myawslogbucket.s3.amazonaws.com`` .

    - **Prefix** *(string) --*

      An optional string that you want CloudFront to prefix to the access log filenames for
      this streaming distribution, for example, ``myprefix/`` . If you want to enable
      logging, but you don't want to specify a prefix, you still must include an empty
      ``Prefix`` element in the ``Logging`` element.
    """


_ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef = TypedDict(
    "_ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef",
    {"DomainName": str, "OriginAccessIdentity": str},
    total=False,
)


class ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef(
    _ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef
):
    """
    Type definition for `ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfig` `S3Origin`

    A complex type that contains information about the Amazon S3 bucket from which you want
    CloudFront to get your media files for distribution.

    - **DomainName** *(string) --*

      The DNS name of the Amazon S3 origin.

    - **OriginAccessIdentity** *(string) --*

      The CloudFront origin access identity to associate with the distribution. Use an origin
      access identity to configure the distribution so that end users can only access objects
      in an Amazon S3 bucket through CloudFront.

      If you want end users to be able to access objects using either the CloudFront URL or
      the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

      To delete the origin access identity from an existing distribution, update the
      distribution configuration and include an empty ``OriginAccessIdentity`` element.

      To replace the origin access identity, update the distribution configuration and
      specify the new origin access identity.

      For more information, see `Using an Origin Access Identity to Restrict Access to Your
      Amazon S3 Content
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
      in the *Amazon CloudFront Developer Guide* .
    """


_ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef = TypedDict(
    "_ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef",
    {"Enabled": bool, "Quantity": int, "Items": List[str]},
    total=False,
)


class ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef(
    _ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef
):
    """
    Type definition for `ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfig` `TrustedSigners`

    A complex type that specifies any AWS accounts that you want to permit to create signed
    URLs for private content. If you want the distribution to use signed URLs, include this
    element; if you want the distribution to use public URLs, remove this element. For more
    information, see `Serving Private Content through CloudFront
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
    in the *Amazon CloudFront Developer Guide* .

    - **Enabled** *(boolean) --*

      Specifies whether you want to require viewers to use signed URLs to access the files
      specified by ``PathPattern`` and ``TargetOriginId`` .

    - **Quantity** *(integer) --*

      The number of trusted signers for this cache behavior.

    - **Items** *(list) --*

       **Optional** : A complex type that contains trusted signers for this cache behavior.
       If ``Quantity`` is ``0`` , you can omit ``Items`` .

      - *(string) --*
    """


_ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTypeDef = TypedDict(
    "_ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "S3Origin": ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigS3OriginTypeDef,
        "Aliases": ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigAliasesTypeDef,
        "Comment": str,
        "Logging": ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigLoggingTypeDef,
        "TrustedSigners": ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef,
        "PriceClass": str,
        "Enabled": bool,
    },
    total=False,
)


class ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTypeDef(
    _ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTypeDef
):
    """
    Type definition for `ClientUpdateStreamingDistributionResponseStreamingDistribution` `StreamingDistributionConfig`

    The current configuration information for the RTMP distribution.

    - **CallerReference** *(string) --*

      A unique value (for example, a date-time stamp) that ensures that the request can't be
      replayed.

      If the value of ``CallerReference`` is new (regardless of the content of the
      ``StreamingDistributionConfig`` object), CloudFront creates a new distribution.

      If ``CallerReference`` is a value that you already sent in a previous request to create a
      distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

    - **S3Origin** *(dict) --*

      A complex type that contains information about the Amazon S3 bucket from which you want
      CloudFront to get your media files for distribution.

      - **DomainName** *(string) --*

        The DNS name of the Amazon S3 origin.

      - **OriginAccessIdentity** *(string) --*

        The CloudFront origin access identity to associate with the distribution. Use an origin
        access identity to configure the distribution so that end users can only access objects
        in an Amazon S3 bucket through CloudFront.

        If you want end users to be able to access objects using either the CloudFront URL or
        the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

        To delete the origin access identity from an existing distribution, update the
        distribution configuration and include an empty ``OriginAccessIdentity`` element.

        To replace the origin access identity, update the distribution configuration and
        specify the new origin access identity.

        For more information, see `Using an Origin Access Identity to Restrict Access to Your
        Amazon S3 Content
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
        in the *Amazon CloudFront Developer Guide* .

    - **Aliases** *(dict) --*

      A complex type that contains information about CNAMEs (alternate domain names), if any,
      for this streaming distribution.

      - **Quantity** *(integer) --*

        The number of CNAME aliases, if any, that you want to associate with this distribution.

      - **Items** *(list) --*

        A complex type that contains the CNAME aliases, if any, that you want to associate with
        this distribution.

        - *(string) --*

    - **Comment** *(string) --*

      Any comments you want to include about the streaming distribution.

    - **Logging** *(dict) --*

      A complex type that controls whether access logs are written for the streaming
      distribution.

      - **Enabled** *(boolean) --*

        Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If
        you don't want to enable logging when you create a streaming distribution or if you
        want to disable logging for an existing streaming distribution, specify ``false`` for
        ``Enabled`` , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify
        ``false`` for ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the
        values are automatically deleted.

      - **Bucket** *(string) --*

        The Amazon S3 bucket to store the access logs in, for example,
        ``myawslogbucket.s3.amazonaws.com`` .

      - **Prefix** *(string) --*

        An optional string that you want CloudFront to prefix to the access log filenames for
        this streaming distribution, for example, ``myprefix/`` . If you want to enable
        logging, but you don't want to specify a prefix, you still must include an empty
        ``Prefix`` element in the ``Logging`` element.

    - **TrustedSigners** *(dict) --*

      A complex type that specifies any AWS accounts that you want to permit to create signed
      URLs for private content. If you want the distribution to use signed URLs, include this
      element; if you want the distribution to use public URLs, remove this element. For more
      information, see `Serving Private Content through CloudFront
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
      in the *Amazon CloudFront Developer Guide* .

      - **Enabled** *(boolean) --*

        Specifies whether you want to require viewers to use signed URLs to access the files
        specified by ``PathPattern`` and ``TargetOriginId`` .

      - **Quantity** *(integer) --*

        The number of trusted signers for this cache behavior.

      - **Items** *(list) --*

         **Optional** : A complex type that contains trusted signers for this cache behavior.
         If ``Quantity`` is ``0`` , you can omit ``Items`` .

        - *(string) --*

    - **PriceClass** *(string) --*

      A complex type that contains information about price class for this streaming
      distribution.

    - **Enabled** *(boolean) --*

      Whether the streaming distribution is enabled to accept user requests for content.
    """


_ClientUpdateStreamingDistributionResponseStreamingDistributionTypeDef = TypedDict(
    "_ClientUpdateStreamingDistributionResponseStreamingDistributionTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "DomainName": str,
        "ActiveTrustedSigners": ClientUpdateStreamingDistributionResponseStreamingDistributionActiveTrustedSignersTypeDef,
        "StreamingDistributionConfig": ClientUpdateStreamingDistributionResponseStreamingDistributionStreamingDistributionConfigTypeDef,
    },
    total=False,
)


class ClientUpdateStreamingDistributionResponseStreamingDistributionTypeDef(
    _ClientUpdateStreamingDistributionResponseStreamingDistributionTypeDef
):
    """
    Type definition for `ClientUpdateStreamingDistributionResponse` `StreamingDistribution`

    The streaming distribution's information.

    - **Id** *(string) --*

      The identifier for the RTMP distribution. For example: ``EGTXBD79EXAMPLE`` .

    - **ARN** *(string) --*

      The ARN (Amazon Resource Name) for the distribution. For example:
      ``arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`` , where ``123456789012``
      is your AWS account ID.

    - **Status** *(string) --*

      The current status of the RTMP distribution. When the status is ``Deployed`` , the
      distribution's information is propagated to all CloudFront edge locations.

    - **LastModifiedTime** *(datetime) --*

      The date and time that the distribution was last modified.

    - **DomainName** *(string) --*

      The domain name that corresponds to the streaming distribution, for example,
      ``s5c39gqb8ow64r.cloudfront.net`` .

    - **ActiveTrustedSigners** *(dict) --*

      A complex type that lists the AWS accounts, if any, that you included in the
      ``TrustedSigners`` complex type for this distribution. These are the accounts that you want
      to allow to create signed URLs for private content.

      The ``Signer`` complex type lists the AWS account number of the trusted signer or ``self``
      if the signer is the AWS account that created the distribution. The ``Signer`` element also
      includes the IDs of any active CloudFront key pairs that are associated with the trusted
      signer's AWS account. If no ``KeyPairId`` element appears for a ``Signer`` , that signer
      can't create signed URLs.

      For more information, see `Serving Private Content through CloudFront
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
      in the *Amazon CloudFront Developer Guide* .

      - **Enabled** *(boolean) --*

        Enabled is ``true`` if any of the AWS accounts listed in the ``TrustedSigners`` complex
        type for this distribution have active CloudFront key pairs. If not, ``Enabled`` is
        ``false`` .

      - **Quantity** *(integer) --*

        The number of trusted signers specified in the ``TrustedSigners`` complex type.

      - **Items** *(list) --*

        A complex type that contains one ``Signer`` complex type for each trusted signer that is
        specified in the ``TrustedSigners`` complex type.

        - *(dict) --*

          A complex type that lists the AWS accounts that were included in the ``TrustedSigners``
          complex type, as well as their active CloudFront key pair IDs, if any.

          - **AwsAccountNumber** *(string) --*

            An AWS account that is included in the ``TrustedSigners`` complex type for this
            distribution. Valid values include:

            * ``self`` , which is the AWS account used to create the distribution.

            * An AWS account number.

          - **KeyPairIds** *(dict) --*

            A complex type that lists the active CloudFront key pairs, if any, that are
            associated with ``AwsAccountNumber`` .

            - **Quantity** *(integer) --*

              The number of active CloudFront key pairs for ``AwsAccountNumber`` .

              For more information, see `ActiveTrustedSigners
              <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
              .

            - **Items** *(list) --*

              A complex type that lists the active CloudFront key pairs, if any, that are
              associated with ``AwsAccountNumber`` .

              For more information, see `ActiveTrustedSigners
              <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
              .

              - *(string) --*

    - **StreamingDistributionConfig** *(dict) --*

      The current configuration information for the RTMP distribution.

      - **CallerReference** *(string) --*

        A unique value (for example, a date-time stamp) that ensures that the request can't be
        replayed.

        If the value of ``CallerReference`` is new (regardless of the content of the
        ``StreamingDistributionConfig`` object), CloudFront creates a new distribution.

        If ``CallerReference`` is a value that you already sent in a previous request to create a
        distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

      - **S3Origin** *(dict) --*

        A complex type that contains information about the Amazon S3 bucket from which you want
        CloudFront to get your media files for distribution.

        - **DomainName** *(string) --*

          The DNS name of the Amazon S3 origin.

        - **OriginAccessIdentity** *(string) --*

          The CloudFront origin access identity to associate with the distribution. Use an origin
          access identity to configure the distribution so that end users can only access objects
          in an Amazon S3 bucket through CloudFront.

          If you want end users to be able to access objects using either the CloudFront URL or
          the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

          To delete the origin access identity from an existing distribution, update the
          distribution configuration and include an empty ``OriginAccessIdentity`` element.

          To replace the origin access identity, update the distribution configuration and
          specify the new origin access identity.

          For more information, see `Using an Origin Access Identity to Restrict Access to Your
          Amazon S3 Content
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
          in the *Amazon CloudFront Developer Guide* .

      - **Aliases** *(dict) --*

        A complex type that contains information about CNAMEs (alternate domain names), if any,
        for this streaming distribution.

        - **Quantity** *(integer) --*

          The number of CNAME aliases, if any, that you want to associate with this distribution.

        - **Items** *(list) --*

          A complex type that contains the CNAME aliases, if any, that you want to associate with
          this distribution.

          - *(string) --*

      - **Comment** *(string) --*

        Any comments you want to include about the streaming distribution.

      - **Logging** *(dict) --*

        A complex type that controls whether access logs are written for the streaming
        distribution.

        - **Enabled** *(boolean) --*

          Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If
          you don't want to enable logging when you create a streaming distribution or if you
          want to disable logging for an existing streaming distribution, specify ``false`` for
          ``Enabled`` , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify
          ``false`` for ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the
          values are automatically deleted.

        - **Bucket** *(string) --*

          The Amazon S3 bucket to store the access logs in, for example,
          ``myawslogbucket.s3.amazonaws.com`` .

        - **Prefix** *(string) --*

          An optional string that you want CloudFront to prefix to the access log filenames for
          this streaming distribution, for example, ``myprefix/`` . If you want to enable
          logging, but you don't want to specify a prefix, you still must include an empty
          ``Prefix`` element in the ``Logging`` element.

      - **TrustedSigners** *(dict) --*

        A complex type that specifies any AWS accounts that you want to permit to create signed
        URLs for private content. If you want the distribution to use signed URLs, include this
        element; if you want the distribution to use public URLs, remove this element. For more
        information, see `Serving Private Content through CloudFront
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
        in the *Amazon CloudFront Developer Guide* .

        - **Enabled** *(boolean) --*

          Specifies whether you want to require viewers to use signed URLs to access the files
          specified by ``PathPattern`` and ``TargetOriginId`` .

        - **Quantity** *(integer) --*

          The number of trusted signers for this cache behavior.

        - **Items** *(list) --*

           **Optional** : A complex type that contains trusted signers for this cache behavior.
           If ``Quantity`` is ``0`` , you can omit ``Items`` .

          - *(string) --*

      - **PriceClass** *(string) --*

        A complex type that contains information about price class for this streaming
        distribution.

      - **Enabled** *(boolean) --*

        Whether the streaming distribution is enabled to accept user requests for content.
    """


_ClientUpdateStreamingDistributionResponseTypeDef = TypedDict(
    "_ClientUpdateStreamingDistributionResponseTypeDef",
    {
        "StreamingDistribution": ClientUpdateStreamingDistributionResponseStreamingDistributionTypeDef,
        "ETag": str,
    },
    total=False,
)


class ClientUpdateStreamingDistributionResponseTypeDef(
    _ClientUpdateStreamingDistributionResponseTypeDef
):
    """
    Type definition for `ClientUpdateStreamingDistribution` `Response`

    The returned result of the corresponding request.

    - **StreamingDistribution** *(dict) --*

      The streaming distribution's information.

      - **Id** *(string) --*

        The identifier for the RTMP distribution. For example: ``EGTXBD79EXAMPLE`` .

      - **ARN** *(string) --*

        The ARN (Amazon Resource Name) for the distribution. For example:
        ``arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5`` , where ``123456789012``
        is your AWS account ID.

      - **Status** *(string) --*

        The current status of the RTMP distribution. When the status is ``Deployed`` , the
        distribution's information is propagated to all CloudFront edge locations.

      - **LastModifiedTime** *(datetime) --*

        The date and time that the distribution was last modified.

      - **DomainName** *(string) --*

        The domain name that corresponds to the streaming distribution, for example,
        ``s5c39gqb8ow64r.cloudfront.net`` .

      - **ActiveTrustedSigners** *(dict) --*

        A complex type that lists the AWS accounts, if any, that you included in the
        ``TrustedSigners`` complex type for this distribution. These are the accounts that you want
        to allow to create signed URLs for private content.

        The ``Signer`` complex type lists the AWS account number of the trusted signer or ``self``
        if the signer is the AWS account that created the distribution. The ``Signer`` element also
        includes the IDs of any active CloudFront key pairs that are associated with the trusted
        signer's AWS account. If no ``KeyPairId`` element appears for a ``Signer`` , that signer
        can't create signed URLs.

        For more information, see `Serving Private Content through CloudFront
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
        in the *Amazon CloudFront Developer Guide* .

        - **Enabled** *(boolean) --*

          Enabled is ``true`` if any of the AWS accounts listed in the ``TrustedSigners`` complex
          type for this distribution have active CloudFront key pairs. If not, ``Enabled`` is
          ``false`` .

        - **Quantity** *(integer) --*

          The number of trusted signers specified in the ``TrustedSigners`` complex type.

        - **Items** *(list) --*

          A complex type that contains one ``Signer`` complex type for each trusted signer that is
          specified in the ``TrustedSigners`` complex type.

          - *(dict) --*

            A complex type that lists the AWS accounts that were included in the ``TrustedSigners``
            complex type, as well as their active CloudFront key pair IDs, if any.

            - **AwsAccountNumber** *(string) --*

              An AWS account that is included in the ``TrustedSigners`` complex type for this
              distribution. Valid values include:

              * ``self`` , which is the AWS account used to create the distribution.

              * An AWS account number.

            - **KeyPairIds** *(dict) --*

              A complex type that lists the active CloudFront key pairs, if any, that are
              associated with ``AwsAccountNumber`` .

              - **Quantity** *(integer) --*

                The number of active CloudFront key pairs for ``AwsAccountNumber`` .

                For more information, see `ActiveTrustedSigners
                <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
                .

              - **Items** *(list) --*

                A complex type that lists the active CloudFront key pairs, if any, that are
                associated with ``AwsAccountNumber`` .

                For more information, see `ActiveTrustedSigners
                <https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ActiveTrustedSigners.html>`__
                .

                - *(string) --*

      - **StreamingDistributionConfig** *(dict) --*

        The current configuration information for the RTMP distribution.

        - **CallerReference** *(string) --*

          A unique value (for example, a date-time stamp) that ensures that the request can't be
          replayed.

          If the value of ``CallerReference`` is new (regardless of the content of the
          ``StreamingDistributionConfig`` object), CloudFront creates a new distribution.

          If ``CallerReference`` is a value that you already sent in a previous request to create a
          distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

        - **S3Origin** *(dict) --*

          A complex type that contains information about the Amazon S3 bucket from which you want
          CloudFront to get your media files for distribution.

          - **DomainName** *(string) --*

            The DNS name of the Amazon S3 origin.

          - **OriginAccessIdentity** *(string) --*

            The CloudFront origin access identity to associate with the distribution. Use an origin
            access identity to configure the distribution so that end users can only access objects
            in an Amazon S3 bucket through CloudFront.

            If you want end users to be able to access objects using either the CloudFront URL or
            the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

            To delete the origin access identity from an existing distribution, update the
            distribution configuration and include an empty ``OriginAccessIdentity`` element.

            To replace the origin access identity, update the distribution configuration and
            specify the new origin access identity.

            For more information, see `Using an Origin Access Identity to Restrict Access to Your
            Amazon S3 Content
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
            in the *Amazon CloudFront Developer Guide* .

        - **Aliases** *(dict) --*

          A complex type that contains information about CNAMEs (alternate domain names), if any,
          for this streaming distribution.

          - **Quantity** *(integer) --*

            The number of CNAME aliases, if any, that you want to associate with this distribution.

          - **Items** *(list) --*

            A complex type that contains the CNAME aliases, if any, that you want to associate with
            this distribution.

            - *(string) --*

        - **Comment** *(string) --*

          Any comments you want to include about the streaming distribution.

        - **Logging** *(dict) --*

          A complex type that controls whether access logs are written for the streaming
          distribution.

          - **Enabled** *(boolean) --*

            Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If
            you don't want to enable logging when you create a streaming distribution or if you
            want to disable logging for an existing streaming distribution, specify ``false`` for
            ``Enabled`` , and specify ``empty Bucket`` and ``Prefix`` elements. If you specify
            ``false`` for ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the
            values are automatically deleted.

          - **Bucket** *(string) --*

            The Amazon S3 bucket to store the access logs in, for example,
            ``myawslogbucket.s3.amazonaws.com`` .

          - **Prefix** *(string) --*

            An optional string that you want CloudFront to prefix to the access log filenames for
            this streaming distribution, for example, ``myprefix/`` . If you want to enable
            logging, but you don't want to specify a prefix, you still must include an empty
            ``Prefix`` element in the ``Logging`` element.

        - **TrustedSigners** *(dict) --*

          A complex type that specifies any AWS accounts that you want to permit to create signed
          URLs for private content. If you want the distribution to use signed URLs, include this
          element; if you want the distribution to use public URLs, remove this element. For more
          information, see `Serving Private Content through CloudFront
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
          in the *Amazon CloudFront Developer Guide* .

          - **Enabled** *(boolean) --*

            Specifies whether you want to require viewers to use signed URLs to access the files
            specified by ``PathPattern`` and ``TargetOriginId`` .

          - **Quantity** *(integer) --*

            The number of trusted signers for this cache behavior.

          - **Items** *(list) --*

             **Optional** : A complex type that contains trusted signers for this cache behavior.
             If ``Quantity`` is ``0`` , you can omit ``Items`` .

            - *(string) --*

        - **PriceClass** *(string) --*

          A complex type that contains information about price class for this streaming
          distribution.

        - **Enabled** *(boolean) --*

          Whether the streaming distribution is enabled to accept user requests for content.

    - **ETag** *(string) --*

      The current version of the configuration. For example: ``E2QWRUHAPOMQZL`` .
    """


_RequiredClientUpdateStreamingDistributionStreamingDistributionConfigAliasesTypeDef = TypedDict(
    "_RequiredClientUpdateStreamingDistributionStreamingDistributionConfigAliasesTypeDef",
    {"Quantity": int},
)
_OptionalClientUpdateStreamingDistributionStreamingDistributionConfigAliasesTypeDef = TypedDict(
    "_OptionalClientUpdateStreamingDistributionStreamingDistributionConfigAliasesTypeDef",
    {"Items": List[str]},
    total=False,
)


class ClientUpdateStreamingDistributionStreamingDistributionConfigAliasesTypeDef(
    _RequiredClientUpdateStreamingDistributionStreamingDistributionConfigAliasesTypeDef,
    _OptionalClientUpdateStreamingDistributionStreamingDistributionConfigAliasesTypeDef,
):
    """
    Type definition for `ClientUpdateStreamingDistributionStreamingDistributionConfig` `Aliases`

    A complex type that contains information about CNAMEs (alternate domain names), if any, for
    this streaming distribution.

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of CNAME aliases, if any, that you want to associate with this distribution.

    - **Items** *(list) --*

      A complex type that contains the CNAME aliases, if any, that you want to associate with this
      distribution.

      - *(string) --*
    """


_ClientUpdateStreamingDistributionStreamingDistributionConfigLoggingTypeDef = TypedDict(
    "_ClientUpdateStreamingDistributionStreamingDistributionConfigLoggingTypeDef",
    {"Enabled": bool, "Bucket": str, "Prefix": str},
)


class ClientUpdateStreamingDistributionStreamingDistributionConfigLoggingTypeDef(
    _ClientUpdateStreamingDistributionStreamingDistributionConfigLoggingTypeDef
):
    """
    Type definition for `ClientUpdateStreamingDistributionStreamingDistributionConfig` `Logging`

    A complex type that controls whether access logs are written for the streaming distribution.

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you
      don't want to enable logging when you create a streaming distribution or if you want to
      disable logging for an existing streaming distribution, specify ``false`` for ``Enabled`` ,
      and specify ``empty Bucket`` and ``Prefix`` elements. If you specify ``false`` for
      ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the values are
      automatically deleted.

    - **Bucket** *(string) --* **[REQUIRED]**

      The Amazon S3 bucket to store the access logs in, for example,
      ``myawslogbucket.s3.amazonaws.com`` .

    - **Prefix** *(string) --* **[REQUIRED]**

      An optional string that you want CloudFront to prefix to the access log filenames for this
      streaming distribution, for example, ``myprefix/`` . If you want to enable logging, but you
      don't want to specify a prefix, you still must include an empty ``Prefix`` element in the
      ``Logging`` element.
    """


_ClientUpdateStreamingDistributionStreamingDistributionConfigS3OriginTypeDef = TypedDict(
    "_ClientUpdateStreamingDistributionStreamingDistributionConfigS3OriginTypeDef",
    {"DomainName": str, "OriginAccessIdentity": str},
)


class ClientUpdateStreamingDistributionStreamingDistributionConfigS3OriginTypeDef(
    _ClientUpdateStreamingDistributionStreamingDistributionConfigS3OriginTypeDef
):
    """
    Type definition for `ClientUpdateStreamingDistributionStreamingDistributionConfig` `S3Origin`

    A complex type that contains information about the Amazon S3 bucket from which you want
    CloudFront to get your media files for distribution.

    - **DomainName** *(string) --* **[REQUIRED]**

      The DNS name of the Amazon S3 origin.

    - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

      The CloudFront origin access identity to associate with the distribution. Use an origin
      access identity to configure the distribution so that end users can only access objects in an
      Amazon S3 bucket through CloudFront.

      If you want end users to be able to access objects using either the CloudFront URL or the
      Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

      To delete the origin access identity from an existing distribution, update the distribution
      configuration and include an empty ``OriginAccessIdentity`` element.

      To replace the origin access identity, update the distribution configuration and specify the
      new origin access identity.

      For more information, see `Using an Origin Access Identity to Restrict Access to Your Amazon
      S3 Content
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
      in the *Amazon CloudFront Developer Guide* .
    """


_RequiredClientUpdateStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef = TypedDict(
    "_RequiredClientUpdateStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef",
    {"Enabled": bool, "Quantity": int},
)
_OptionalClientUpdateStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef = TypedDict(
    "_OptionalClientUpdateStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef",
    {"Items": List[str]},
    total=False,
)


class ClientUpdateStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef(
    _RequiredClientUpdateStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef,
    _OptionalClientUpdateStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef,
):
    """
    Type definition for `ClientUpdateStreamingDistributionStreamingDistributionConfig` `TrustedSigners`

    A complex type that specifies any AWS accounts that you want to permit to create signed URLs
    for private content. If you want the distribution to use signed URLs, include this element; if
    you want the distribution to use public URLs, remove this element. For more information, see
    `Serving Private Content through CloudFront
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__ in
    the *Amazon CloudFront Developer Guide* .

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Specifies whether you want to require viewers to use signed URLs to access the files
      specified by ``PathPattern`` and ``TargetOriginId`` .

    - **Quantity** *(integer) --* **[REQUIRED]**

      The number of trusted signers for this cache behavior.

    - **Items** *(list) --*

       **Optional** : A complex type that contains trusted signers for this cache behavior. If
       ``Quantity`` is ``0`` , you can omit ``Items`` .

      - *(string) --*
    """


_RequiredClientUpdateStreamingDistributionStreamingDistributionConfigTypeDef = TypedDict(
    "_RequiredClientUpdateStreamingDistributionStreamingDistributionConfigTypeDef",
    {
        "CallerReference": str,
        "S3Origin": ClientUpdateStreamingDistributionStreamingDistributionConfigS3OriginTypeDef,
        "Comment": str,
        "TrustedSigners": ClientUpdateStreamingDistributionStreamingDistributionConfigTrustedSignersTypeDef,
        "Enabled": bool,
    },
)
_OptionalClientUpdateStreamingDistributionStreamingDistributionConfigTypeDef = TypedDict(
    "_OptionalClientUpdateStreamingDistributionStreamingDistributionConfigTypeDef",
    {
        "Aliases": ClientUpdateStreamingDistributionStreamingDistributionConfigAliasesTypeDef,
        "Logging": ClientUpdateStreamingDistributionStreamingDistributionConfigLoggingTypeDef,
        "PriceClass": str,
    },
    total=False,
)


class ClientUpdateStreamingDistributionStreamingDistributionConfigTypeDef(
    _RequiredClientUpdateStreamingDistributionStreamingDistributionConfigTypeDef,
    _OptionalClientUpdateStreamingDistributionStreamingDistributionConfigTypeDef,
):
    """
    Type definition for `ClientUpdateStreamingDistribution` `StreamingDistributionConfig`

    The streaming distribution's configuration information.

    - **CallerReference** *(string) --* **[REQUIRED]**

      A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.

      If the value of ``CallerReference`` is new (regardless of the content of the
      ``StreamingDistributionConfig`` object), CloudFront creates a new distribution.

      If ``CallerReference`` is a value that you already sent in a previous request to create a
      distribution, CloudFront returns a ``DistributionAlreadyExists`` error.

    - **S3Origin** *(dict) --* **[REQUIRED]**

      A complex type that contains information about the Amazon S3 bucket from which you want
      CloudFront to get your media files for distribution.

      - **DomainName** *(string) --* **[REQUIRED]**

        The DNS name of the Amazon S3 origin.

      - **OriginAccessIdentity** *(string) --* **[REQUIRED]**

        The CloudFront origin access identity to associate with the distribution. Use an origin
        access identity to configure the distribution so that end users can only access objects in an
        Amazon S3 bucket through CloudFront.

        If you want end users to be able to access objects using either the CloudFront URL or the
        Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

        To delete the origin access identity from an existing distribution, update the distribution
        configuration and include an empty ``OriginAccessIdentity`` element.

        To replace the origin access identity, update the distribution configuration and specify the
        new origin access identity.

        For more information, see `Using an Origin Access Identity to Restrict Access to Your Amazon
        S3 Content
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
        in the *Amazon CloudFront Developer Guide* .

    - **Aliases** *(dict) --*

      A complex type that contains information about CNAMEs (alternate domain names), if any, for
      this streaming distribution.

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of CNAME aliases, if any, that you want to associate with this distribution.

      - **Items** *(list) --*

        A complex type that contains the CNAME aliases, if any, that you want to associate with this
        distribution.

        - *(string) --*

    - **Comment** *(string) --* **[REQUIRED]**

      Any comments you want to include about the streaming distribution.

    - **Logging** *(dict) --*

      A complex type that controls whether access logs are written for the streaming distribution.

      - **Enabled** *(boolean) --* **[REQUIRED]**

        Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you
        don't want to enable logging when you create a streaming distribution or if you want to
        disable logging for an existing streaming distribution, specify ``false`` for ``Enabled`` ,
        and specify ``empty Bucket`` and ``Prefix`` elements. If you specify ``false`` for
        ``Enabled`` but you specify values for ``Bucket`` and ``Prefix`` , the values are
        automatically deleted.

      - **Bucket** *(string) --* **[REQUIRED]**

        The Amazon S3 bucket to store the access logs in, for example,
        ``myawslogbucket.s3.amazonaws.com`` .

      - **Prefix** *(string) --* **[REQUIRED]**

        An optional string that you want CloudFront to prefix to the access log filenames for this
        streaming distribution, for example, ``myprefix/`` . If you want to enable logging, but you
        don't want to specify a prefix, you still must include an empty ``Prefix`` element in the
        ``Logging`` element.

    - **TrustedSigners** *(dict) --* **[REQUIRED]**

      A complex type that specifies any AWS accounts that you want to permit to create signed URLs
      for private content. If you want the distribution to use signed URLs, include this element; if
      you want the distribution to use public URLs, remove this element. For more information, see
      `Serving Private Content through CloudFront
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__ in
      the *Amazon CloudFront Developer Guide* .

      - **Enabled** *(boolean) --* **[REQUIRED]**

        Specifies whether you want to require viewers to use signed URLs to access the files
        specified by ``PathPattern`` and ``TargetOriginId`` .

      - **Quantity** *(integer) --* **[REQUIRED]**

        The number of trusted signers for this cache behavior.

      - **Items** *(list) --*

         **Optional** : A complex type that contains trusted signers for this cache behavior. If
         ``Quantity`` is ``0`` , you can omit ``Items`` .

        - *(string) --*

    - **PriceClass** *(string) --*

      A complex type that contains information about price class for this streaming distribution.

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Whether the streaming distribution is enabled to accept user requests for content.
    """


_DistributionDeployedWaitWaiterConfigTypeDef = TypedDict(
    "_DistributionDeployedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class DistributionDeployedWaitWaiterConfigTypeDef(
    _DistributionDeployedWaitWaiterConfigTypeDef
):
    """
    Type definition for `DistributionDeployedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 60

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 35
    """


_InvalidationCompletedWaitWaiterConfigTypeDef = TypedDict(
    "_InvalidationCompletedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class InvalidationCompletedWaitWaiterConfigTypeDef(
    _InvalidationCompletedWaitWaiterConfigTypeDef
):
    """
    Type definition for `InvalidationCompletedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 20

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 30
    """


_ListCloudFrontOriginAccessIdentitiesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCloudFrontOriginAccessIdentitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCloudFrontOriginAccessIdentitiesPaginatePaginationConfigTypeDef(
    _ListCloudFrontOriginAccessIdentitiesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListCloudFrontOriginAccessIdentitiesPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListCloudFrontOriginAccessIdentitiesPaginateResponseCloudFrontOriginAccessIdentityListItemsTypeDef = TypedDict(
    "_ListCloudFrontOriginAccessIdentitiesPaginateResponseCloudFrontOriginAccessIdentityListItemsTypeDef",
    {"Id": str, "S3CanonicalUserId": str, "Comment": str},
    total=False,
)


class ListCloudFrontOriginAccessIdentitiesPaginateResponseCloudFrontOriginAccessIdentityListItemsTypeDef(
    _ListCloudFrontOriginAccessIdentitiesPaginateResponseCloudFrontOriginAccessIdentityListItemsTypeDef
):
    """
    Type definition for `ListCloudFrontOriginAccessIdentitiesPaginateResponseCloudFrontOriginAccessIdentityList` `Items`

    Summary of the information about a CloudFront origin access identity.

    - **Id** *(string) --*

      The ID for the origin access identity. For example: ``E74FTE3AJFJ256A`` .

    - **S3CanonicalUserId** *(string) --*

      The Amazon S3 canonical user ID for the origin access identity, which you use when
      giving the origin access identity read permission to an object in Amazon S3.

    - **Comment** *(string) --*

      The comment for this origin access identity, as originally specified when created.
    """


_ListCloudFrontOriginAccessIdentitiesPaginateResponseCloudFrontOriginAccessIdentityListTypeDef = TypedDict(
    "_ListCloudFrontOriginAccessIdentitiesPaginateResponseCloudFrontOriginAccessIdentityListTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
        "Items": List[
            ListCloudFrontOriginAccessIdentitiesPaginateResponseCloudFrontOriginAccessIdentityListItemsTypeDef
        ],
    },
    total=False,
)


class ListCloudFrontOriginAccessIdentitiesPaginateResponseCloudFrontOriginAccessIdentityListTypeDef(
    _ListCloudFrontOriginAccessIdentitiesPaginateResponseCloudFrontOriginAccessIdentityListTypeDef
):
    """
    Type definition for `ListCloudFrontOriginAccessIdentitiesPaginateResponse` `CloudFrontOriginAccessIdentityList`

    The ``CloudFrontOriginAccessIdentityList`` type.

    - **Marker** *(string) --*

      Use this when paginating results to indicate where to begin in your list of origin access
      identities. The results include identities in the list that occur after the marker. To get
      the next page of results, set the ``Marker`` to the value of the ``NextMarker`` from the
      current page's response (which is also the ID of the last identity on that page).

    - **NextMarker** *(string) --*

      If ``IsTruncated`` is ``true`` , this element is present and contains the value you can use
      for the ``Marker`` request parameter to continue listing your origin access identities
      where they left off.

    - **MaxItems** *(integer) --*

      The maximum number of origin access identities you want in the response body.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether more origin access identities remain to be listed. If your
      results were truncated, you can make a follow-up pagination request using the ``Marker``
      request parameter to retrieve more items in the list.

    - **Quantity** *(integer) --*

      The number of CloudFront origin access identities that were created by the current AWS
      account.

    - **Items** *(list) --*

      A complex type that contains one ``CloudFrontOriginAccessIdentitySummary`` element for each
      origin access identity that was created by the current AWS account.

      - *(dict) --*

        Summary of the information about a CloudFront origin access identity.

        - **Id** *(string) --*

          The ID for the origin access identity. For example: ``E74FTE3AJFJ256A`` .

        - **S3CanonicalUserId** *(string) --*

          The Amazon S3 canonical user ID for the origin access identity, which you use when
          giving the origin access identity read permission to an object in Amazon S3.

        - **Comment** *(string) --*

          The comment for this origin access identity, as originally specified when created.
    """


_ListCloudFrontOriginAccessIdentitiesPaginateResponseTypeDef = TypedDict(
    "_ListCloudFrontOriginAccessIdentitiesPaginateResponseTypeDef",
    {
        "CloudFrontOriginAccessIdentityList": ListCloudFrontOriginAccessIdentitiesPaginateResponseCloudFrontOriginAccessIdentityListTypeDef,
        "NextToken": str,
    },
    total=False,
)


class ListCloudFrontOriginAccessIdentitiesPaginateResponseTypeDef(
    _ListCloudFrontOriginAccessIdentitiesPaginateResponseTypeDef
):
    """
    Type definition for `ListCloudFrontOriginAccessIdentitiesPaginate` `Response`

    The returned result of the corresponding request.

    - **CloudFrontOriginAccessIdentityList** *(dict) --*

      The ``CloudFrontOriginAccessIdentityList`` type.

      - **Marker** *(string) --*

        Use this when paginating results to indicate where to begin in your list of origin access
        identities. The results include identities in the list that occur after the marker. To get
        the next page of results, set the ``Marker`` to the value of the ``NextMarker`` from the
        current page's response (which is also the ID of the last identity on that page).

      - **NextMarker** *(string) --*

        If ``IsTruncated`` is ``true`` , this element is present and contains the value you can use
        for the ``Marker`` request parameter to continue listing your origin access identities
        where they left off.

      - **MaxItems** *(integer) --*

        The maximum number of origin access identities you want in the response body.

      - **IsTruncated** *(boolean) --*

        A flag that indicates whether more origin access identities remain to be listed. If your
        results were truncated, you can make a follow-up pagination request using the ``Marker``
        request parameter to retrieve more items in the list.

      - **Quantity** *(integer) --*

        The number of CloudFront origin access identities that were created by the current AWS
        account.

      - **Items** *(list) --*

        A complex type that contains one ``CloudFrontOriginAccessIdentitySummary`` element for each
        origin access identity that was created by the current AWS account.

        - *(dict) --*

          Summary of the information about a CloudFront origin access identity.

          - **Id** *(string) --*

            The ID for the origin access identity. For example: ``E74FTE3AJFJ256A`` .

          - **S3CanonicalUserId** *(string) --*

            The Amazon S3 canonical user ID for the origin access identity, which you use when
            giving the origin access identity read permission to an object in Amazon S3.

          - **Comment** *(string) --*

            The comment for this origin access identity, as originally specified when created.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListDistributionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDistributionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDistributionsPaginatePaginationConfigTypeDef(
    _ListDistributionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDistributionsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListInvalidationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListInvalidationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListInvalidationsPaginatePaginationConfigTypeDef(
    _ListInvalidationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListInvalidationsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListInvalidationsPaginateResponseInvalidationListItemsTypeDef = TypedDict(
    "_ListInvalidationsPaginateResponseInvalidationListItemsTypeDef",
    {"Id": str, "CreateTime": datetime, "Status": str},
    total=False,
)


class ListInvalidationsPaginateResponseInvalidationListItemsTypeDef(
    _ListInvalidationsPaginateResponseInvalidationListItemsTypeDef
):
    """
    Type definition for `ListInvalidationsPaginateResponseInvalidationList` `Items`

    A summary of an invalidation request.

    - **Id** *(string) --*

      The unique ID for an invalidation request.

    - **CreateTime** *(datetime) --*

      The time that an invalidation request was created.

    - **Status** *(string) --*

      The status of an invalidation request.
    """


_ListInvalidationsPaginateResponseInvalidationListTypeDef = TypedDict(
    "_ListInvalidationsPaginateResponseInvalidationListTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
        "Items": List[ListInvalidationsPaginateResponseInvalidationListItemsTypeDef],
    },
    total=False,
)


class ListInvalidationsPaginateResponseInvalidationListTypeDef(
    _ListInvalidationsPaginateResponseInvalidationListTypeDef
):
    """
    Type definition for `ListInvalidationsPaginateResponse` `InvalidationList`

    Information about invalidation batches.

    - **Marker** *(string) --*

      The value that you provided for the ``Marker`` request parameter.

    - **NextMarker** *(string) --*

      If ``IsTruncated`` is ``true`` , this element is present and contains the value that you
      can use for the ``Marker`` request parameter to continue listing your invalidation batches
      where they left off.

    - **MaxItems** *(integer) --*

      The value that you provided for the ``MaxItems`` request parameter.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether more invalidation batch requests remain to be listed. If your
      results were truncated, you can make a follow-up pagination request using the ``Marker``
      request parameter to retrieve more invalidation batches in the list.

    - **Quantity** *(integer) --*

      The number of invalidation batches that were created by the current AWS account.

    - **Items** *(list) --*

      A complex type that contains one ``InvalidationSummary`` element for each invalidation
      batch created by the current AWS account.

      - *(dict) --*

        A summary of an invalidation request.

        - **Id** *(string) --*

          The unique ID for an invalidation request.

        - **CreateTime** *(datetime) --*

          The time that an invalidation request was created.

        - **Status** *(string) --*

          The status of an invalidation request.
    """


_ListInvalidationsPaginateResponseTypeDef = TypedDict(
    "_ListInvalidationsPaginateResponseTypeDef",
    {
        "InvalidationList": ListInvalidationsPaginateResponseInvalidationListTypeDef,
        "NextToken": str,
    },
    total=False,
)


class ListInvalidationsPaginateResponseTypeDef(
    _ListInvalidationsPaginateResponseTypeDef
):
    """
    Type definition for `ListInvalidationsPaginate` `Response`

    The returned result of the corresponding request.

    - **InvalidationList** *(dict) --*

      Information about invalidation batches.

      - **Marker** *(string) --*

        The value that you provided for the ``Marker`` request parameter.

      - **NextMarker** *(string) --*

        If ``IsTruncated`` is ``true`` , this element is present and contains the value that you
        can use for the ``Marker`` request parameter to continue listing your invalidation batches
        where they left off.

      - **MaxItems** *(integer) --*

        The value that you provided for the ``MaxItems`` request parameter.

      - **IsTruncated** *(boolean) --*

        A flag that indicates whether more invalidation batch requests remain to be listed. If your
        results were truncated, you can make a follow-up pagination request using the ``Marker``
        request parameter to retrieve more invalidation batches in the list.

      - **Quantity** *(integer) --*

        The number of invalidation batches that were created by the current AWS account.

      - **Items** *(list) --*

        A complex type that contains one ``InvalidationSummary`` element for each invalidation
        batch created by the current AWS account.

        - *(dict) --*

          A summary of an invalidation request.

          - **Id** *(string) --*

            The unique ID for an invalidation request.

          - **CreateTime** *(datetime) --*

            The time that an invalidation request was created.

          - **Status** *(string) --*

            The status of an invalidation request.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListStreamingDistributionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStreamingDistributionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStreamingDistributionsPaginatePaginationConfigTypeDef(
    _ListStreamingDistributionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListStreamingDistributionsPaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **PageSize** *(integer) --*

      The size of each page.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsAliasesTypeDef = TypedDict(
    "_ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsAliasesTypeDef",
    {"Quantity": int, "Items": List[str]},
    total=False,
)


class ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsAliasesTypeDef(
    _ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsAliasesTypeDef
):
    """
    Type definition for `ListStreamingDistributionsPaginateResponseStreamingDistributionListItems` `Aliases`

    A complex type that contains information about CNAMEs (alternate domain names), if any,
    for this streaming distribution.

    - **Quantity** *(integer) --*

      The number of CNAME aliases, if any, that you want to associate with this
      distribution.

    - **Items** *(list) --*

      A complex type that contains the CNAME aliases, if any, that you want to associate
      with this distribution.

      - *(string) --*
    """


_ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsS3OriginTypeDef = TypedDict(
    "_ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsS3OriginTypeDef",
    {"DomainName": str, "OriginAccessIdentity": str},
    total=False,
)


class ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsS3OriginTypeDef(
    _ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsS3OriginTypeDef
):
    """
    Type definition for `ListStreamingDistributionsPaginateResponseStreamingDistributionListItems` `S3Origin`

    A complex type that contains information about the Amazon S3 bucket from which you want
    CloudFront to get your media files for distribution.

    - **DomainName** *(string) --*

      The DNS name of the Amazon S3 origin.

    - **OriginAccessIdentity** *(string) --*

      The CloudFront origin access identity to associate with the distribution. Use an
      origin access identity to configure the distribution so that end users can only
      access objects in an Amazon S3 bucket through CloudFront.

      If you want end users to be able to access objects using either the CloudFront URL or
      the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

      To delete the origin access identity from an existing distribution, update the
      distribution configuration and include an empty ``OriginAccessIdentity`` element.

      To replace the origin access identity, update the distribution configuration and
      specify the new origin access identity.

      For more information, see `Using an Origin Access Identity to Restrict Access to Your
      Amazon S3 Content
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
      in the *Amazon CloudFront Developer Guide* .
    """


_ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsTrustedSignersTypeDef = TypedDict(
    "_ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsTrustedSignersTypeDef",
    {"Enabled": bool, "Quantity": int, "Items": List[str]},
    total=False,
)


class ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsTrustedSignersTypeDef(
    _ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsTrustedSignersTypeDef
):
    """
    Type definition for `ListStreamingDistributionsPaginateResponseStreamingDistributionListItems` `TrustedSigners`

    A complex type that specifies the AWS accounts, if any, that you want to allow to
    create signed URLs for private content. If you want to require signed URLs in requests
    for objects in the target origin that match the ``PathPattern`` for this cache
    behavior, specify ``true`` for ``Enabled`` , and specify the applicable values for
    ``Quantity`` and ``Items`` .If you don't want to require signed URLs in requests for
    objects that match ``PathPattern`` , specify ``false`` for ``Enabled`` and ``0`` for
    ``Quantity`` . Omit ``Items`` . To add, change, or remove one or more trusted signers,
    change ``Enabled`` to ``true`` (if it's currently ``false`` ), change ``Quantity`` as
    applicable, and specify all of the trusted signers that you want to include in the
    updated distribution.

    For more information, see `Serving Private Content through CloudFront
    <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
    in the *Amazon CloudFront Developer Guide* .

    - **Enabled** *(boolean) --*

      Specifies whether you want to require viewers to use signed URLs to access the files
      specified by ``PathPattern`` and ``TargetOriginId`` .

    - **Quantity** *(integer) --*

      The number of trusted signers for this cache behavior.

    - **Items** *(list) --*

       **Optional** : A complex type that contains trusted signers for this cache behavior.
       If ``Quantity`` is ``0`` , you can omit ``Items`` .

      - *(string) --*
    """


_ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsTypeDef = TypedDict(
    "_ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsTypeDef",
    {
        "Id": str,
        "ARN": str,
        "Status": str,
        "LastModifiedTime": datetime,
        "DomainName": str,
        "S3Origin": ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsS3OriginTypeDef,
        "Aliases": ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsAliasesTypeDef,
        "TrustedSigners": ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsTrustedSignersTypeDef,
        "Comment": str,
        "PriceClass": str,
        "Enabled": bool,
    },
    total=False,
)


class ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsTypeDef(
    _ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsTypeDef
):
    """
    Type definition for `ListStreamingDistributionsPaginateResponseStreamingDistributionList` `Items`

    A summary of the information for a CloudFront streaming distribution.

    - **Id** *(string) --*

      The identifier for the distribution, for example, ``EDFDVBD632BHDS5`` .

    - **ARN** *(string) --*

      The ARN (Amazon Resource Name) for the streaming distribution. For example:
      ``arn:aws:cloudfront::123456789012:streaming-distribution/EDFDVBD632BHDS5`` , where
      ``123456789012`` is your AWS account ID.

    - **Status** *(string) --*

      Indicates the current status of the distribution. When the status is ``Deployed`` , the
      distribution's information is fully propagated throughout the Amazon CloudFront system.

    - **LastModifiedTime** *(datetime) --*

      The date and time the distribution was last modified.

    - **DomainName** *(string) --*

      The domain name corresponding to the distribution, for example,
      ``d111111abcdef8.cloudfront.net`` .

    - **S3Origin** *(dict) --*

      A complex type that contains information about the Amazon S3 bucket from which you want
      CloudFront to get your media files for distribution.

      - **DomainName** *(string) --*

        The DNS name of the Amazon S3 origin.

      - **OriginAccessIdentity** *(string) --*

        The CloudFront origin access identity to associate with the distribution. Use an
        origin access identity to configure the distribution so that end users can only
        access objects in an Amazon S3 bucket through CloudFront.

        If you want end users to be able to access objects using either the CloudFront URL or
        the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

        To delete the origin access identity from an existing distribution, update the
        distribution configuration and include an empty ``OriginAccessIdentity`` element.

        To replace the origin access identity, update the distribution configuration and
        specify the new origin access identity.

        For more information, see `Using an Origin Access Identity to Restrict Access to Your
        Amazon S3 Content
        <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
        in the *Amazon CloudFront Developer Guide* .

    - **Aliases** *(dict) --*

      A complex type that contains information about CNAMEs (alternate domain names), if any,
      for this streaming distribution.

      - **Quantity** *(integer) --*

        The number of CNAME aliases, if any, that you want to associate with this
        distribution.

      - **Items** *(list) --*

        A complex type that contains the CNAME aliases, if any, that you want to associate
        with this distribution.

        - *(string) --*

    - **TrustedSigners** *(dict) --*

      A complex type that specifies the AWS accounts, if any, that you want to allow to
      create signed URLs for private content. If you want to require signed URLs in requests
      for objects in the target origin that match the ``PathPattern`` for this cache
      behavior, specify ``true`` for ``Enabled`` , and specify the applicable values for
      ``Quantity`` and ``Items`` .If you don't want to require signed URLs in requests for
      objects that match ``PathPattern`` , specify ``false`` for ``Enabled`` and ``0`` for
      ``Quantity`` . Omit ``Items`` . To add, change, or remove one or more trusted signers,
      change ``Enabled`` to ``true`` (if it's currently ``false`` ), change ``Quantity`` as
      applicable, and specify all of the trusted signers that you want to include in the
      updated distribution.

      For more information, see `Serving Private Content through CloudFront
      <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
      in the *Amazon CloudFront Developer Guide* .

      - **Enabled** *(boolean) --*

        Specifies whether you want to require viewers to use signed URLs to access the files
        specified by ``PathPattern`` and ``TargetOriginId`` .

      - **Quantity** *(integer) --*

        The number of trusted signers for this cache behavior.

      - **Items** *(list) --*

         **Optional** : A complex type that contains trusted signers for this cache behavior.
         If ``Quantity`` is ``0`` , you can omit ``Items`` .

        - *(string) --*

    - **Comment** *(string) --*

      The comment originally specified when this distribution was created.

    - **PriceClass** *(string) --*

      A complex type that contains information about price class for this streaming
      distribution.

    - **Enabled** *(boolean) --*

      Whether the distribution is enabled to accept end user requests for content.
    """


_ListStreamingDistributionsPaginateResponseStreamingDistributionListTypeDef = TypedDict(
    "_ListStreamingDistributionsPaginateResponseStreamingDistributionListTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "MaxItems": int,
        "IsTruncated": bool,
        "Quantity": int,
        "Items": List[
            ListStreamingDistributionsPaginateResponseStreamingDistributionListItemsTypeDef
        ],
    },
    total=False,
)


class ListStreamingDistributionsPaginateResponseStreamingDistributionListTypeDef(
    _ListStreamingDistributionsPaginateResponseStreamingDistributionListTypeDef
):
    """
    Type definition for `ListStreamingDistributionsPaginateResponse` `StreamingDistributionList`

    The ``StreamingDistributionList`` type.

    - **Marker** *(string) --*

      The value you provided for the ``Marker`` request parameter.

    - **NextMarker** *(string) --*

      If ``IsTruncated`` is ``true`` , this element is present and contains the value you can use
      for the ``Marker`` request parameter to continue listing your RTMP distributions where they
      left off.

    - **MaxItems** *(integer) --*

      The value you provided for the ``MaxItems`` request parameter.

    - **IsTruncated** *(boolean) --*

      A flag that indicates whether more streaming distributions remain to be listed. If your
      results were truncated, you can make a follow-up pagination request using the ``Marker``
      request parameter to retrieve more distributions in the list.

    - **Quantity** *(integer) --*

      The number of streaming distributions that were created by the current AWS account.

    - **Items** *(list) --*

      A complex type that contains one ``StreamingDistributionSummary`` element for each
      distribution that was created by the current AWS account.

      - *(dict) --*

        A summary of the information for a CloudFront streaming distribution.

        - **Id** *(string) --*

          The identifier for the distribution, for example, ``EDFDVBD632BHDS5`` .

        - **ARN** *(string) --*

          The ARN (Amazon Resource Name) for the streaming distribution. For example:
          ``arn:aws:cloudfront::123456789012:streaming-distribution/EDFDVBD632BHDS5`` , where
          ``123456789012`` is your AWS account ID.

        - **Status** *(string) --*

          Indicates the current status of the distribution. When the status is ``Deployed`` , the
          distribution's information is fully propagated throughout the Amazon CloudFront system.

        - **LastModifiedTime** *(datetime) --*

          The date and time the distribution was last modified.

        - **DomainName** *(string) --*

          The domain name corresponding to the distribution, for example,
          ``d111111abcdef8.cloudfront.net`` .

        - **S3Origin** *(dict) --*

          A complex type that contains information about the Amazon S3 bucket from which you want
          CloudFront to get your media files for distribution.

          - **DomainName** *(string) --*

            The DNS name of the Amazon S3 origin.

          - **OriginAccessIdentity** *(string) --*

            The CloudFront origin access identity to associate with the distribution. Use an
            origin access identity to configure the distribution so that end users can only
            access objects in an Amazon S3 bucket through CloudFront.

            If you want end users to be able to access objects using either the CloudFront URL or
            the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

            To delete the origin access identity from an existing distribution, update the
            distribution configuration and include an empty ``OriginAccessIdentity`` element.

            To replace the origin access identity, update the distribution configuration and
            specify the new origin access identity.

            For more information, see `Using an Origin Access Identity to Restrict Access to Your
            Amazon S3 Content
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
            in the *Amazon CloudFront Developer Guide* .

        - **Aliases** *(dict) --*

          A complex type that contains information about CNAMEs (alternate domain names), if any,
          for this streaming distribution.

          - **Quantity** *(integer) --*

            The number of CNAME aliases, if any, that you want to associate with this
            distribution.

          - **Items** *(list) --*

            A complex type that contains the CNAME aliases, if any, that you want to associate
            with this distribution.

            - *(string) --*

        - **TrustedSigners** *(dict) --*

          A complex type that specifies the AWS accounts, if any, that you want to allow to
          create signed URLs for private content. If you want to require signed URLs in requests
          for objects in the target origin that match the ``PathPattern`` for this cache
          behavior, specify ``true`` for ``Enabled`` , and specify the applicable values for
          ``Quantity`` and ``Items`` .If you don't want to require signed URLs in requests for
          objects that match ``PathPattern`` , specify ``false`` for ``Enabled`` and ``0`` for
          ``Quantity`` . Omit ``Items`` . To add, change, or remove one or more trusted signers,
          change ``Enabled`` to ``true`` (if it's currently ``false`` ), change ``Quantity`` as
          applicable, and specify all of the trusted signers that you want to include in the
          updated distribution.

          For more information, see `Serving Private Content through CloudFront
          <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
          in the *Amazon CloudFront Developer Guide* .

          - **Enabled** *(boolean) --*

            Specifies whether you want to require viewers to use signed URLs to access the files
            specified by ``PathPattern`` and ``TargetOriginId`` .

          - **Quantity** *(integer) --*

            The number of trusted signers for this cache behavior.

          - **Items** *(list) --*

             **Optional** : A complex type that contains trusted signers for this cache behavior.
             If ``Quantity`` is ``0`` , you can omit ``Items`` .

            - *(string) --*

        - **Comment** *(string) --*

          The comment originally specified when this distribution was created.

        - **PriceClass** *(string) --*

          A complex type that contains information about price class for this streaming
          distribution.

        - **Enabled** *(boolean) --*

          Whether the distribution is enabled to accept end user requests for content.
    """


_ListStreamingDistributionsPaginateResponseTypeDef = TypedDict(
    "_ListStreamingDistributionsPaginateResponseTypeDef",
    {
        "StreamingDistributionList": ListStreamingDistributionsPaginateResponseStreamingDistributionListTypeDef,
        "NextToken": str,
    },
    total=False,
)


class ListStreamingDistributionsPaginateResponseTypeDef(
    _ListStreamingDistributionsPaginateResponseTypeDef
):
    """
    Type definition for `ListStreamingDistributionsPaginate` `Response`

    The returned result of the corresponding request.

    - **StreamingDistributionList** *(dict) --*

      The ``StreamingDistributionList`` type.

      - **Marker** *(string) --*

        The value you provided for the ``Marker`` request parameter.

      - **NextMarker** *(string) --*

        If ``IsTruncated`` is ``true`` , this element is present and contains the value you can use
        for the ``Marker`` request parameter to continue listing your RTMP distributions where they
        left off.

      - **MaxItems** *(integer) --*

        The value you provided for the ``MaxItems`` request parameter.

      - **IsTruncated** *(boolean) --*

        A flag that indicates whether more streaming distributions remain to be listed. If your
        results were truncated, you can make a follow-up pagination request using the ``Marker``
        request parameter to retrieve more distributions in the list.

      - **Quantity** *(integer) --*

        The number of streaming distributions that were created by the current AWS account.

      - **Items** *(list) --*

        A complex type that contains one ``StreamingDistributionSummary`` element for each
        distribution that was created by the current AWS account.

        - *(dict) --*

          A summary of the information for a CloudFront streaming distribution.

          - **Id** *(string) --*

            The identifier for the distribution, for example, ``EDFDVBD632BHDS5`` .

          - **ARN** *(string) --*

            The ARN (Amazon Resource Name) for the streaming distribution. For example:
            ``arn:aws:cloudfront::123456789012:streaming-distribution/EDFDVBD632BHDS5`` , where
            ``123456789012`` is your AWS account ID.

          - **Status** *(string) --*

            Indicates the current status of the distribution. When the status is ``Deployed`` , the
            distribution's information is fully propagated throughout the Amazon CloudFront system.

          - **LastModifiedTime** *(datetime) --*

            The date and time the distribution was last modified.

          - **DomainName** *(string) --*

            The domain name corresponding to the distribution, for example,
            ``d111111abcdef8.cloudfront.net`` .

          - **S3Origin** *(dict) --*

            A complex type that contains information about the Amazon S3 bucket from which you want
            CloudFront to get your media files for distribution.

            - **DomainName** *(string) --*

              The DNS name of the Amazon S3 origin.

            - **OriginAccessIdentity** *(string) --*

              The CloudFront origin access identity to associate with the distribution. Use an
              origin access identity to configure the distribution so that end users can only
              access objects in an Amazon S3 bucket through CloudFront.

              If you want end users to be able to access objects using either the CloudFront URL or
              the Amazon S3 URL, specify an empty ``OriginAccessIdentity`` element.

              To delete the origin access identity from an existing distribution, update the
              distribution configuration and include an empty ``OriginAccessIdentity`` element.

              To replace the origin access identity, update the distribution configuration and
              specify the new origin access identity.

              For more information, see `Using an Origin Access Identity to Restrict Access to Your
              Amazon S3 Content
              <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html>`__
              in the *Amazon CloudFront Developer Guide* .

          - **Aliases** *(dict) --*

            A complex type that contains information about CNAMEs (alternate domain names), if any,
            for this streaming distribution.

            - **Quantity** *(integer) --*

              The number of CNAME aliases, if any, that you want to associate with this
              distribution.

            - **Items** *(list) --*

              A complex type that contains the CNAME aliases, if any, that you want to associate
              with this distribution.

              - *(string) --*

          - **TrustedSigners** *(dict) --*

            A complex type that specifies the AWS accounts, if any, that you want to allow to
            create signed URLs for private content. If you want to require signed URLs in requests
            for objects in the target origin that match the ``PathPattern`` for this cache
            behavior, specify ``true`` for ``Enabled`` , and specify the applicable values for
            ``Quantity`` and ``Items`` .If you don't want to require signed URLs in requests for
            objects that match ``PathPattern`` , specify ``false`` for ``Enabled`` and ``0`` for
            ``Quantity`` . Omit ``Items`` . To add, change, or remove one or more trusted signers,
            change ``Enabled`` to ``true`` (if it's currently ``false`` ), change ``Quantity`` as
            applicable, and specify all of the trusted signers that you want to include in the
            updated distribution.

            For more information, see `Serving Private Content through CloudFront
            <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html>`__
            in the *Amazon CloudFront Developer Guide* .

            - **Enabled** *(boolean) --*

              Specifies whether you want to require viewers to use signed URLs to access the files
              specified by ``PathPattern`` and ``TargetOriginId`` .

            - **Quantity** *(integer) --*

              The number of trusted signers for this cache behavior.

            - **Items** *(list) --*

               **Optional** : A complex type that contains trusted signers for this cache behavior.
               If ``Quantity`` is ``0`` , you can omit ``Items`` .

              - *(string) --*

          - **Comment** *(string) --*

            The comment originally specified when this distribution was created.

          - **PriceClass** *(string) --*

            A complex type that contains information about price class for this streaming
            distribution.

          - **Enabled** *(boolean) --*

            Whether the distribution is enabled to accept end user requests for content.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_StreamingDistributionDeployedWaitWaiterConfigTypeDef = TypedDict(
    "_StreamingDistributionDeployedWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class StreamingDistributionDeployedWaitWaiterConfigTypeDef(
    _StreamingDistributionDeployedWaitWaiterConfigTypeDef
):
    """
    Type definition for `StreamingDistributionDeployedWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 60

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 25
    """

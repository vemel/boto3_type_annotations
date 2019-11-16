"Main interface for clouddirectory type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientAddFacetToObjectObjectAttributeListKeyTypeDef",
    "ClientAddFacetToObjectObjectAttributeListValueTypeDef",
    "ClientAddFacetToObjectObjectAttributeListTypeDef",
    "ClientAddFacetToObjectObjectReferenceTypeDef",
    "ClientAddFacetToObjectSchemaFacetTypeDef",
    "ClientApplySchemaResponseTypeDef",
    "ClientAttachObjectChildReferenceTypeDef",
    "ClientAttachObjectParentReferenceTypeDef",
    "ClientAttachObjectResponseTypeDef",
    "ClientAttachPolicyObjectReferenceTypeDef",
    "ClientAttachPolicyPolicyReferenceTypeDef",
    "ClientAttachToIndexIndexReferenceTypeDef",
    "ClientAttachToIndexResponseTypeDef",
    "ClientAttachToIndexTargetReferenceTypeDef",
    "ClientAttachTypedLinkAttributesValueTypeDef",
    "ClientAttachTypedLinkAttributesTypeDef",
    "ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientAttachTypedLinkResponseTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientAttachTypedLinkResponseTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientAttachTypedLinkResponseTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientAttachTypedLinkResponseTypedLinkSpecifierTypeDef",
    "ClientAttachTypedLinkResponseTypeDef",
    "ClientAttachTypedLinkSourceObjectReferenceTypeDef",
    "ClientAttachTypedLinkTargetObjectReferenceTypeDef",
    "ClientAttachTypedLinkTypedLinkFacetTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypeDef",
    "ClientBatchReadOperationsGetLinkAttributesTypeDef",
    "ClientBatchReadOperationsGetObjectAttributesObjectReferenceTypeDef",
    "ClientBatchReadOperationsGetObjectAttributesSchemaFacetTypeDef",
    "ClientBatchReadOperationsGetObjectAttributesTypeDef",
    "ClientBatchReadOperationsGetObjectInformationObjectReferenceTypeDef",
    "ClientBatchReadOperationsGetObjectInformationTypeDef",
    "ClientBatchReadOperationsListAttachedIndicesTargetReferenceTypeDef",
    "ClientBatchReadOperationsListAttachedIndicesTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksFilterTypedLinkTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksObjectReferenceTypeDef",
    "ClientBatchReadOperationsListIncomingTypedLinksTypeDef",
    "ClientBatchReadOperationsListIndexIndexReferenceTypeDef",
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesAttributeKeyTypeDef",
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeEndValueTypeDef",
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeStartValueTypeDef",
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef",
    "ClientBatchReadOperationsListIndexRangesOnIndexedValuesTypeDef",
    "ClientBatchReadOperationsListIndexTypeDef",
    "ClientBatchReadOperationsListObjectAttributesFacetFilterTypeDef",
    "ClientBatchReadOperationsListObjectAttributesObjectReferenceTypeDef",
    "ClientBatchReadOperationsListObjectAttributesTypeDef",
    "ClientBatchReadOperationsListObjectChildrenObjectReferenceTypeDef",
    "ClientBatchReadOperationsListObjectChildrenTypeDef",
    "ClientBatchReadOperationsListObjectParentPathsObjectReferenceTypeDef",
    "ClientBatchReadOperationsListObjectParentPathsTypeDef",
    "ClientBatchReadOperationsListObjectParentsObjectReferenceTypeDef",
    "ClientBatchReadOperationsListObjectParentsTypeDef",
    "ClientBatchReadOperationsListObjectPoliciesObjectReferenceTypeDef",
    "ClientBatchReadOperationsListObjectPoliciesTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksFilterTypedLinkTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksObjectReferenceTypeDef",
    "ClientBatchReadOperationsListOutgoingTypedLinksTypeDef",
    "ClientBatchReadOperationsListPolicyAttachmentsPolicyReferenceTypeDef",
    "ClientBatchReadOperationsListPolicyAttachmentsTypeDef",
    "ClientBatchReadOperationsLookupPolicyObjectReferenceTypeDef",
    "ClientBatchReadOperationsLookupPolicyTypeDef",
    "ClientBatchReadOperationsTypeDef",
    "ClientBatchReadResponseResponsesExceptionResponseTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesKeyTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesKeyTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationSchemaFacetsTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesKeyTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersSourceObjectReferenceTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTargetObjectReferenceTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypedLinkFacetTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesKeyTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListIndexTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesKeyTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectChildrenTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsPathToObjectIdentifiersListTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsParentLinksTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListObjectPoliciesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersSourceObjectReferenceTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTargetObjectReferenceTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypedLinkFacetTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseListPolicyAttachmentsTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListPoliciesTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyTypeDef",
    "ClientBatchReadResponseResponsesSuccessfulResponseTypeDef",
    "ClientBatchReadResponseResponsesTypeDef",
    "ClientBatchReadResponseTypeDef",
    "ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListKeyTypeDef",
    "ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListValueTypeDef",
    "ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListTypeDef",
    "ClientBatchWriteOperationsAddFacetToObjectObjectReferenceTypeDef",
    "ClientBatchWriteOperationsAddFacetToObjectSchemaFacetTypeDef",
    "ClientBatchWriteOperationsAddFacetToObjectTypeDef",
    "ClientBatchWriteOperationsAttachObjectChildReferenceTypeDef",
    "ClientBatchWriteOperationsAttachObjectParentReferenceTypeDef",
    "ClientBatchWriteOperationsAttachObjectTypeDef",
    "ClientBatchWriteOperationsAttachPolicyObjectReferenceTypeDef",
    "ClientBatchWriteOperationsAttachPolicyPolicyReferenceTypeDef",
    "ClientBatchWriteOperationsAttachPolicyTypeDef",
    "ClientBatchWriteOperationsAttachToIndexIndexReferenceTypeDef",
    "ClientBatchWriteOperationsAttachToIndexTargetReferenceTypeDef",
    "ClientBatchWriteOperationsAttachToIndexTypeDef",
    "ClientBatchWriteOperationsAttachTypedLinkAttributesValueTypeDef",
    "ClientBatchWriteOperationsAttachTypedLinkAttributesTypeDef",
    "ClientBatchWriteOperationsAttachTypedLinkSourceObjectReferenceTypeDef",
    "ClientBatchWriteOperationsAttachTypedLinkTargetObjectReferenceTypeDef",
    "ClientBatchWriteOperationsAttachTypedLinkTypedLinkFacetTypeDef",
    "ClientBatchWriteOperationsAttachTypedLinkTypeDef",
    "ClientBatchWriteOperationsCreateIndexOrderedIndexedAttributeListTypeDef",
    "ClientBatchWriteOperationsCreateIndexParentReferenceTypeDef",
    "ClientBatchWriteOperationsCreateIndexTypeDef",
    "ClientBatchWriteOperationsCreateObjectObjectAttributeListKeyTypeDef",
    "ClientBatchWriteOperationsCreateObjectObjectAttributeListValueTypeDef",
    "ClientBatchWriteOperationsCreateObjectObjectAttributeListTypeDef",
    "ClientBatchWriteOperationsCreateObjectParentReferenceTypeDef",
    "ClientBatchWriteOperationsCreateObjectSchemaFacetTypeDef",
    "ClientBatchWriteOperationsCreateObjectTypeDef",
    "ClientBatchWriteOperationsDeleteObjectObjectReferenceTypeDef",
    "ClientBatchWriteOperationsDeleteObjectTypeDef",
    "ClientBatchWriteOperationsDetachFromIndexIndexReferenceTypeDef",
    "ClientBatchWriteOperationsDetachFromIndexTargetReferenceTypeDef",
    "ClientBatchWriteOperationsDetachFromIndexTypeDef",
    "ClientBatchWriteOperationsDetachObjectParentReferenceTypeDef",
    "ClientBatchWriteOperationsDetachObjectTypeDef",
    "ClientBatchWriteOperationsDetachPolicyObjectReferenceTypeDef",
    "ClientBatchWriteOperationsDetachPolicyPolicyReferenceTypeDef",
    "ClientBatchWriteOperationsDetachPolicyTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypeDef",
    "ClientBatchWriteOperationsDetachTypedLinkTypeDef",
    "ClientBatchWriteOperationsRemoveFacetFromObjectObjectReferenceTypeDef",
    "ClientBatchWriteOperationsRemoveFacetFromObjectSchemaFacetTypeDef",
    "ClientBatchWriteOperationsRemoveFacetFromObjectTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypeDef",
    "ClientBatchWriteOperationsUpdateLinkAttributesTypeDef",
    "ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef",
    "ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef",
    "ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef",
    "ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesTypeDef",
    "ClientBatchWriteOperationsUpdateObjectAttributesObjectReferenceTypeDef",
    "ClientBatchWriteOperationsUpdateObjectAttributesTypeDef",
    "ClientBatchWriteOperationsTypeDef",
    "ClientBatchWriteResponseResponsesAttachObjectTypeDef",
    "ClientBatchWriteResponseResponsesAttachToIndexTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypeDef",
    "ClientBatchWriteResponseResponsesAttachTypedLinkTypeDef",
    "ClientBatchWriteResponseResponsesCreateIndexTypeDef",
    "ClientBatchWriteResponseResponsesCreateObjectTypeDef",
    "ClientBatchWriteResponseResponsesDetachFromIndexTypeDef",
    "ClientBatchWriteResponseResponsesDetachObjectTypeDef",
    "ClientBatchWriteResponseResponsesUpdateObjectAttributesTypeDef",
    "ClientBatchWriteResponseResponsesTypeDef",
    "ClientBatchWriteResponseTypeDef",
    "ClientCreateDirectoryResponseTypeDef",
    "ClientCreateFacetAttributesAttributeDefinitionDefaultValueTypeDef",
    "ClientCreateFacetAttributesAttributeDefinitionRulesTypeDef",
    "ClientCreateFacetAttributesAttributeDefinitionTypeDef",
    "ClientCreateFacetAttributesAttributeReferenceTypeDef",
    "ClientCreateFacetAttributesTypeDef",
    "ClientCreateIndexOrderedIndexedAttributeListTypeDef",
    "ClientCreateIndexParentReferenceTypeDef",
    "ClientCreateIndexResponseTypeDef",
    "ClientCreateObjectObjectAttributeListKeyTypeDef",
    "ClientCreateObjectObjectAttributeListValueTypeDef",
    "ClientCreateObjectObjectAttributeListTypeDef",
    "ClientCreateObjectParentReferenceTypeDef",
    "ClientCreateObjectResponseTypeDef",
    "ClientCreateObjectSchemaFacetsTypeDef",
    "ClientCreateSchemaResponseTypeDef",
    "ClientCreateTypedLinkFacetFacetAttributesDefaultValueTypeDef",
    "ClientCreateTypedLinkFacetFacetAttributesRulesTypeDef",
    "ClientCreateTypedLinkFacetFacetAttributesTypeDef",
    "ClientCreateTypedLinkFacetFacetTypeDef",
    "ClientDeleteDirectoryResponseTypeDef",
    "ClientDeleteObjectObjectReferenceTypeDef",
    "ClientDeleteSchemaResponseTypeDef",
    "ClientDetachFromIndexIndexReferenceTypeDef",
    "ClientDetachFromIndexResponseTypeDef",
    "ClientDetachFromIndexTargetReferenceTypeDef",
    "ClientDetachObjectParentReferenceTypeDef",
    "ClientDetachObjectResponseTypeDef",
    "ClientDetachPolicyObjectReferenceTypeDef",
    "ClientDetachPolicyPolicyReferenceTypeDef",
    "ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientDetachTypedLinkTypedLinkSpecifierTypeDef",
    "ClientDisableDirectoryResponseTypeDef",
    "ClientEnableDirectoryResponseTypeDef",
    "ClientGetAppliedSchemaVersionResponseTypeDef",
    "ClientGetDirectoryResponseDirectoryTypeDef",
    "ClientGetDirectoryResponseTypeDef",
    "ClientGetFacetResponseFacetTypeDef",
    "ClientGetFacetResponseTypeDef",
    "ClientGetLinkAttributesResponseAttributesKeyTypeDef",
    "ClientGetLinkAttributesResponseAttributesValueTypeDef",
    "ClientGetLinkAttributesResponseAttributesTypeDef",
    "ClientGetLinkAttributesResponseTypeDef",
    "ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientGetLinkAttributesTypedLinkSpecifierTypeDef",
    "ClientGetObjectAttributesObjectReferenceTypeDef",
    "ClientGetObjectAttributesResponseAttributesKeyTypeDef",
    "ClientGetObjectAttributesResponseAttributesValueTypeDef",
    "ClientGetObjectAttributesResponseAttributesTypeDef",
    "ClientGetObjectAttributesResponseTypeDef",
    "ClientGetObjectAttributesSchemaFacetTypeDef",
    "ClientGetObjectInformationObjectReferenceTypeDef",
    "ClientGetObjectInformationResponseSchemaFacetsTypeDef",
    "ClientGetObjectInformationResponseTypeDef",
    "ClientGetSchemaAsJsonResponseTypeDef",
    "ClientGetTypedLinkFacetInformationResponseTypeDef",
    "ClientListAppliedSchemaArnsResponseTypeDef",
    "ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    "ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    "ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesTypeDef",
    "ClientListAttachedIndicesResponseIndexAttachmentsTypeDef",
    "ClientListAttachedIndicesResponseTypeDef",
    "ClientListAttachedIndicesTargetReferenceTypeDef",
    "ClientListDevelopmentSchemaArnsResponseTypeDef",
    "ClientListDirectoriesResponseDirectoriesTypeDef",
    "ClientListDirectoriesResponseTypeDef",
    "ClientListFacetAttributesResponseAttributesAttributeDefinitionDefaultValueTypeDef",
    "ClientListFacetAttributesResponseAttributesAttributeDefinitionRulesTypeDef",
    "ClientListFacetAttributesResponseAttributesAttributeDefinitionTypeDef",
    "ClientListFacetAttributesResponseAttributesAttributeReferenceTypeDef",
    "ClientListFacetAttributesResponseAttributesTypeDef",
    "ClientListFacetAttributesResponseTypeDef",
    "ClientListFacetNamesResponseTypeDef",
    "ClientListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    "ClientListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    "ClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef",
    "ClientListIncomingTypedLinksFilterAttributeRangesTypeDef",
    "ClientListIncomingTypedLinksFilterTypedLinkTypeDef",
    "ClientListIncomingTypedLinksObjectReferenceTypeDef",
    "ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    "ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesTypeDef",
    "ClientListIncomingTypedLinksResponseLinkSpecifiersSourceObjectReferenceTypeDef",
    "ClientListIncomingTypedLinksResponseLinkSpecifiersTargetObjectReferenceTypeDef",
    "ClientListIncomingTypedLinksResponseLinkSpecifiersTypedLinkFacetTypeDef",
    "ClientListIncomingTypedLinksResponseLinkSpecifiersTypeDef",
    "ClientListIncomingTypedLinksResponseTypeDef",
    "ClientListIndexIndexReferenceTypeDef",
    "ClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef",
    "ClientListIndexRangesOnIndexedValuesRangeEndValueTypeDef",
    "ClientListIndexRangesOnIndexedValuesRangeStartValueTypeDef",
    "ClientListIndexRangesOnIndexedValuesRangeTypeDef",
    "ClientListIndexRangesOnIndexedValuesTypeDef",
    "ClientListIndexResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    "ClientListIndexResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    "ClientListIndexResponseIndexAttachmentsIndexedAttributesTypeDef",
    "ClientListIndexResponseIndexAttachmentsTypeDef",
    "ClientListIndexResponseTypeDef",
    "ClientListManagedSchemaArnsResponseTypeDef",
    "ClientListObjectAttributesFacetFilterTypeDef",
    "ClientListObjectAttributesObjectReferenceTypeDef",
    "ClientListObjectAttributesResponseAttributesKeyTypeDef",
    "ClientListObjectAttributesResponseAttributesValueTypeDef",
    "ClientListObjectAttributesResponseAttributesTypeDef",
    "ClientListObjectAttributesResponseTypeDef",
    "ClientListObjectChildrenObjectReferenceTypeDef",
    "ClientListObjectChildrenResponseTypeDef",
    "ClientListObjectParentPathsObjectReferenceTypeDef",
    "ClientListObjectParentPathsResponsePathToObjectIdentifiersListTypeDef",
    "ClientListObjectParentPathsResponseTypeDef",
    "ClientListObjectParentsObjectReferenceTypeDef",
    "ClientListObjectParentsResponseParentLinksTypeDef",
    "ClientListObjectParentsResponseTypeDef",
    "ClientListObjectPoliciesObjectReferenceTypeDef",
    "ClientListObjectPoliciesResponseTypeDef",
    "ClientListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    "ClientListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    "ClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef",
    "ClientListOutgoingTypedLinksFilterAttributeRangesTypeDef",
    "ClientListOutgoingTypedLinksFilterTypedLinkTypeDef",
    "ClientListOutgoingTypedLinksObjectReferenceTypeDef",
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef",
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef",
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef",
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypedLinkFacetTypeDef",
    "ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypeDef",
    "ClientListOutgoingTypedLinksResponseTypeDef",
    "ClientListPolicyAttachmentsPolicyReferenceTypeDef",
    "ClientListPolicyAttachmentsResponseTypeDef",
    "ClientListPublishedSchemaArnsResponseTypeDef",
    "ClientListTagsForResourceResponseTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListTypedLinkFacetAttributesResponseAttributesDefaultValueTypeDef",
    "ClientListTypedLinkFacetAttributesResponseAttributesRulesTypeDef",
    "ClientListTypedLinkFacetAttributesResponseAttributesTypeDef",
    "ClientListTypedLinkFacetAttributesResponseTypeDef",
    "ClientListTypedLinkFacetNamesResponseTypeDef",
    "ClientLookupPolicyObjectReferenceTypeDef",
    "ClientLookupPolicyResponsePolicyToPathListPoliciesTypeDef",
    "ClientLookupPolicyResponsePolicyToPathListTypeDef",
    "ClientLookupPolicyResponseTypeDef",
    "ClientPublishSchemaResponseTypeDef",
    "ClientPutSchemaFromJsonResponseTypeDef",
    "ClientRemoveFacetFromObjectObjectReferenceTypeDef",
    "ClientRemoveFacetFromObjectSchemaFacetTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionDefaultValueTypeDef",
    "ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionRulesTypeDef",
    "ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef",
    "ClientUpdateFacetAttributeUpdatesAttributeAttributeReferenceTypeDef",
    "ClientUpdateFacetAttributeUpdatesAttributeTypeDef",
    "ClientUpdateFacetAttributeUpdatesTypeDef",
    "ClientUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef",
    "ClientUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef",
    "ClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef",
    "ClientUpdateLinkAttributesAttributeUpdatesTypeDef",
    "ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    "ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    "ClientUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    "ClientUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    "ClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    "ClientUpdateLinkAttributesTypedLinkSpecifierTypeDef",
    "ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef",
    "ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef",
    "ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef",
    "ClientUpdateObjectAttributesAttributeUpdatesTypeDef",
    "ClientUpdateObjectAttributesObjectReferenceTypeDef",
    "ClientUpdateObjectAttributesResponseTypeDef",
    "ClientUpdateSchemaResponseTypeDef",
    "ClientUpdateTypedLinkFacetAttributeUpdatesAttributeDefaultValueTypeDef",
    "ClientUpdateTypedLinkFacetAttributeUpdatesAttributeRulesTypeDef",
    "ClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef",
    "ClientUpdateTypedLinkFacetAttributeUpdatesTypeDef",
    "ClientUpgradeAppliedSchemaResponseTypeDef",
    "ClientUpgradePublishedSchemaResponseTypeDef",
    "ListAppliedSchemaArnsPaginatePaginationConfigTypeDef",
    "ListAppliedSchemaArnsPaginateResponseTypeDef",
    "ListAttachedIndicesPaginatePaginationConfigTypeDef",
    "ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    "ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    "ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesTypeDef",
    "ListAttachedIndicesPaginateResponseIndexAttachmentsTypeDef",
    "ListAttachedIndicesPaginateResponseTypeDef",
    "ListAttachedIndicesPaginateTargetReferenceTypeDef",
    "ListDevelopmentSchemaArnsPaginatePaginationConfigTypeDef",
    "ListDevelopmentSchemaArnsPaginateResponseTypeDef",
    "ListDirectoriesPaginatePaginationConfigTypeDef",
    "ListDirectoriesPaginateResponseDirectoriesTypeDef",
    "ListDirectoriesPaginateResponseTypeDef",
    "ListFacetAttributesPaginatePaginationConfigTypeDef",
    "ListFacetAttributesPaginateResponseAttributesAttributeDefinitionDefaultValueTypeDef",
    "ListFacetAttributesPaginateResponseAttributesAttributeDefinitionRulesTypeDef",
    "ListFacetAttributesPaginateResponseAttributesAttributeDefinitionTypeDef",
    "ListFacetAttributesPaginateResponseAttributesAttributeReferenceTypeDef",
    "ListFacetAttributesPaginateResponseAttributesTypeDef",
    "ListFacetAttributesPaginateResponseTypeDef",
    "ListFacetNamesPaginatePaginationConfigTypeDef",
    "ListFacetNamesPaginateResponseTypeDef",
    "ListIncomingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef",
    "ListIncomingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef",
    "ListIncomingTypedLinksPaginateFilterAttributeRangesRangeTypeDef",
    "ListIncomingTypedLinksPaginateFilterAttributeRangesTypeDef",
    "ListIncomingTypedLinksPaginateFilterTypedLinkTypeDef",
    "ListIncomingTypedLinksPaginateObjectReferenceTypeDef",
    "ListIncomingTypedLinksPaginatePaginationConfigTypeDef",
    "ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    "ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesTypeDef",
    "ListIncomingTypedLinksPaginateResponseLinkSpecifiersSourceObjectReferenceTypeDef",
    "ListIncomingTypedLinksPaginateResponseLinkSpecifiersTargetObjectReferenceTypeDef",
    "ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypedLinkFacetTypeDef",
    "ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypeDef",
    "ListIncomingTypedLinksPaginateResponseTypeDef",
    "ListIndexPaginateIndexReferenceTypeDef",
    "ListIndexPaginatePaginationConfigTypeDef",
    "ListIndexPaginateRangesOnIndexedValuesAttributeKeyTypeDef",
    "ListIndexPaginateRangesOnIndexedValuesRangeEndValueTypeDef",
    "ListIndexPaginateRangesOnIndexedValuesRangeStartValueTypeDef",
    "ListIndexPaginateRangesOnIndexedValuesRangeTypeDef",
    "ListIndexPaginateRangesOnIndexedValuesTypeDef",
    "ListIndexPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    "ListIndexPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    "ListIndexPaginateResponseIndexAttachmentsIndexedAttributesTypeDef",
    "ListIndexPaginateResponseIndexAttachmentsTypeDef",
    "ListIndexPaginateResponseTypeDef",
    "ListManagedSchemaArnsPaginatePaginationConfigTypeDef",
    "ListManagedSchemaArnsPaginateResponseTypeDef",
    "ListObjectAttributesPaginateFacetFilterTypeDef",
    "ListObjectAttributesPaginateObjectReferenceTypeDef",
    "ListObjectAttributesPaginatePaginationConfigTypeDef",
    "ListObjectAttributesPaginateResponseAttributesKeyTypeDef",
    "ListObjectAttributesPaginateResponseAttributesValueTypeDef",
    "ListObjectAttributesPaginateResponseAttributesTypeDef",
    "ListObjectAttributesPaginateResponseTypeDef",
    "ListObjectParentPathsPaginateObjectReferenceTypeDef",
    "ListObjectParentPathsPaginatePaginationConfigTypeDef",
    "ListObjectParentPathsPaginateResponsePathToObjectIdentifiersListTypeDef",
    "ListObjectParentPathsPaginateResponseTypeDef",
    "ListObjectPoliciesPaginateObjectReferenceTypeDef",
    "ListObjectPoliciesPaginatePaginationConfigTypeDef",
    "ListObjectPoliciesPaginateResponseTypeDef",
    "ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef",
    "ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef",
    "ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeTypeDef",
    "ListOutgoingTypedLinksPaginateFilterAttributeRangesTypeDef",
    "ListOutgoingTypedLinksPaginateFilterTypedLinkTypeDef",
    "ListOutgoingTypedLinksPaginateObjectReferenceTypeDef",
    "ListOutgoingTypedLinksPaginatePaginationConfigTypeDef",
    "ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    "ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef",
    "ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef",
    "ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef",
    "ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypedLinkFacetTypeDef",
    "ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypeDef",
    "ListOutgoingTypedLinksPaginateResponseTypeDef",
    "ListPolicyAttachmentsPaginatePaginationConfigTypeDef",
    "ListPolicyAttachmentsPaginatePolicyReferenceTypeDef",
    "ListPolicyAttachmentsPaginateResponseTypeDef",
    "ListPublishedSchemaArnsPaginatePaginationConfigTypeDef",
    "ListPublishedSchemaArnsPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponseTagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
    "ListTypedLinkFacetAttributesPaginatePaginationConfigTypeDef",
    "ListTypedLinkFacetAttributesPaginateResponseAttributesDefaultValueTypeDef",
    "ListTypedLinkFacetAttributesPaginateResponseAttributesRulesTypeDef",
    "ListTypedLinkFacetAttributesPaginateResponseAttributesTypeDef",
    "ListTypedLinkFacetAttributesPaginateResponseTypeDef",
    "ListTypedLinkFacetNamesPaginatePaginationConfigTypeDef",
    "ListTypedLinkFacetNamesPaginateResponseTypeDef",
    "LookupPolicyPaginateObjectReferenceTypeDef",
    "LookupPolicyPaginatePaginationConfigTypeDef",
    "LookupPolicyPaginateResponsePolicyToPathListPoliciesTypeDef",
    "LookupPolicyPaginateResponsePolicyToPathListTypeDef",
    "LookupPolicyPaginateResponseTypeDef",
)


_ClientAddFacetToObjectObjectAttributeListKeyTypeDef = TypedDict(
    "_ClientAddFacetToObjectObjectAttributeListKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
)


class ClientAddFacetToObjectObjectAttributeListKeyTypeDef(
    _ClientAddFacetToObjectObjectAttributeListKeyTypeDef
):
    """
    Type definition for `ClientAddFacetToObjectObjectAttributeList` `Key`

    The key of the attribute.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --* **[REQUIRED]**

      The name of the facet that the attribute exists within.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.
    """


_ClientAddFacetToObjectObjectAttributeListValueTypeDef = TypedDict(
    "_ClientAddFacetToObjectObjectAttributeListValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientAddFacetToObjectObjectAttributeListValueTypeDef(
    _ClientAddFacetToObjectObjectAttributeListValueTypeDef
):
    """
    Type definition for `ClientAddFacetToObjectObjectAttributeList` `Value`

    The value of the attribute.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientAddFacetToObjectObjectAttributeListTypeDef = TypedDict(
    "_ClientAddFacetToObjectObjectAttributeListTypeDef",
    {
        "Key": ClientAddFacetToObjectObjectAttributeListKeyTypeDef,
        "Value": ClientAddFacetToObjectObjectAttributeListValueTypeDef,
    },
)


class ClientAddFacetToObjectObjectAttributeListTypeDef(
    _ClientAddFacetToObjectObjectAttributeListTypeDef
):
    """
    Type definition for `ClientAddFacetToObject` `ObjectAttributeList`

    The combination of an attribute key and an attribute value.

    - **Key** *(dict) --* **[REQUIRED]**

      The key of the attribute.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --* **[REQUIRED]**

        The name of the facet that the attribute exists within.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the attribute.

    - **Value** *(dict) --* **[REQUIRED]**

      The value of the attribute.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientAddFacetToObjectObjectReferenceTypeDef = TypedDict(
    "_ClientAddFacetToObjectObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientAddFacetToObjectObjectReferenceTypeDef(
    _ClientAddFacetToObjectObjectReferenceTypeDef
):
    """
    Type definition for `ClientAddFacetToObject` `ObjectReference`

    A reference to the object you are adding the specified facet to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAddFacetToObjectSchemaFacetTypeDef = TypedDict(
    "_ClientAddFacetToObjectSchemaFacetTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientAddFacetToObjectSchemaFacetTypeDef(
    _ClientAddFacetToObjectSchemaFacetTypeDef
):
    """
    Type definition for `ClientAddFacetToObject` `SchemaFacet`

    Identifiers for the facet that you are adding to the object. See  SchemaFacet for details.

    - **SchemaArn** *(string) --*

      The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place
      Schema Upgrade
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
      for a description of when to provide minor versions.

    - **FacetName** *(string) --*

      The name of the facet.
    """


_ClientApplySchemaResponseTypeDef = TypedDict(
    "_ClientApplySchemaResponseTypeDef",
    {"AppliedSchemaArn": str, "DirectoryArn": str},
    total=False,
)


class ClientApplySchemaResponseTypeDef(_ClientApplySchemaResponseTypeDef):
    """
    Type definition for `ClientApplySchema` `Response`

    - **AppliedSchemaArn** *(string) --*

      The applied schema ARN that is associated with the copied schema in the  Directory . You can
      use this ARN to describe the schema information applied on this directory. For more
      information, see  arns .

    - **DirectoryArn** *(string) --*

      The ARN that is associated with the  Directory . For more information, see  arns .
    """


_ClientAttachObjectChildReferenceTypeDef = TypedDict(
    "_ClientAttachObjectChildReferenceTypeDef", {"Selector": str}, total=False
)


class ClientAttachObjectChildReferenceTypeDef(_ClientAttachObjectChildReferenceTypeDef):
    """
    Type definition for `ClientAttachObject` `ChildReference`

    The child object reference to be attached to the object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAttachObjectParentReferenceTypeDef = TypedDict(
    "_ClientAttachObjectParentReferenceTypeDef", {"Selector": str}, total=False
)


class ClientAttachObjectParentReferenceTypeDef(
    _ClientAttachObjectParentReferenceTypeDef
):
    """
    Type definition for `ClientAttachObject` `ParentReference`

    The parent object reference.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAttachObjectResponseTypeDef = TypedDict(
    "_ClientAttachObjectResponseTypeDef", {"AttachedObjectIdentifier": str}, total=False
)


class ClientAttachObjectResponseTypeDef(_ClientAttachObjectResponseTypeDef):
    """
    Type definition for `ClientAttachObject` `Response`

    - **AttachedObjectIdentifier** *(string) --*

      The attached ``ObjectIdentifier`` , which is the child ``ObjectIdentifier`` .
    """


_ClientAttachPolicyObjectReferenceTypeDef = TypedDict(
    "_ClientAttachPolicyObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientAttachPolicyObjectReferenceTypeDef(
    _ClientAttachPolicyObjectReferenceTypeDef
):
    """
    Type definition for `ClientAttachPolicy` `ObjectReference`

    The reference that identifies the object to which the policy will be attached.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAttachPolicyPolicyReferenceTypeDef = TypedDict(
    "_ClientAttachPolicyPolicyReferenceTypeDef", {"Selector": str}, total=False
)


class ClientAttachPolicyPolicyReferenceTypeDef(
    _ClientAttachPolicyPolicyReferenceTypeDef
):
    """
    Type definition for `ClientAttachPolicy` `PolicyReference`

    The reference that is associated with the policy object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAttachToIndexIndexReferenceTypeDef = TypedDict(
    "_ClientAttachToIndexIndexReferenceTypeDef", {"Selector": str}, total=False
)


class ClientAttachToIndexIndexReferenceTypeDef(
    _ClientAttachToIndexIndexReferenceTypeDef
):
    """
    Type definition for `ClientAttachToIndex` `IndexReference`

    A reference to the index that you are attaching the object to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAttachToIndexResponseTypeDef = TypedDict(
    "_ClientAttachToIndexResponseTypeDef",
    {"AttachedObjectIdentifier": str},
    total=False,
)


class ClientAttachToIndexResponseTypeDef(_ClientAttachToIndexResponseTypeDef):
    """
    Type definition for `ClientAttachToIndex` `Response`

    - **AttachedObjectIdentifier** *(string) --*

      The ``ObjectIdentifier`` of the object that was attached to the index.
    """


_ClientAttachToIndexTargetReferenceTypeDef = TypedDict(
    "_ClientAttachToIndexTargetReferenceTypeDef", {"Selector": str}, total=False
)


class ClientAttachToIndexTargetReferenceTypeDef(
    _ClientAttachToIndexTargetReferenceTypeDef
):
    """
    Type definition for `ClientAttachToIndex` `TargetReference`

    A reference to the object that you are attaching to the index.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAttachTypedLinkAttributesValueTypeDef = TypedDict(
    "_ClientAttachTypedLinkAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientAttachTypedLinkAttributesValueTypeDef(
    _ClientAttachTypedLinkAttributesValueTypeDef
):
    """
    Type definition for `ClientAttachTypedLinkAttributes` `Value`

    The value for the typed link.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientAttachTypedLinkAttributesTypeDef = TypedDict(
    "_ClientAttachTypedLinkAttributesTypeDef",
    {"AttributeName": str, "Value": ClientAttachTypedLinkAttributesValueTypeDef},
)


class ClientAttachTypedLinkAttributesTypeDef(_ClientAttachTypedLinkAttributesTypeDef):
    """
    Type definition for `ClientAttachTypedLink` `Attributes`

    Identifies the attribute name and value for a typed link.

    - **AttributeName** *(string) --* **[REQUIRED]**

      The attribute name of the typed link.

    - **Value** *(dict) --* **[REQUIRED]**

      The value for the typed link.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesValueTypeDef(
    _ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesValueTypeDef
):
    """
    Type definition for `ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValues` `Value`

    The value for the typed link.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesTypeDef(
    _ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesTypeDef
):
    """
    Type definition for `ClientAttachTypedLinkResponseTypedLinkSpecifier` `IdentityAttributeValues`

    Identifies the attribute name and value for a typed link.

    - **AttributeName** *(string) --*

      The attribute name of the typed link.

    - **Value** *(dict) --*

      The value for the typed link.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientAttachTypedLinkResponseTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "_ClientAttachTypedLinkResponseTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientAttachTypedLinkResponseTypedLinkSpecifierSourceObjectReferenceTypeDef(
    _ClientAttachTypedLinkResponseTypedLinkSpecifierSourceObjectReferenceTypeDef
):
    """
    Type definition for `ClientAttachTypedLinkResponseTypedLinkSpecifier` `SourceObjectReference`

    Identifies the source object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAttachTypedLinkResponseTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "_ClientAttachTypedLinkResponseTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientAttachTypedLinkResponseTypedLinkSpecifierTargetObjectReferenceTypeDef(
    _ClientAttachTypedLinkResponseTypedLinkSpecifierTargetObjectReferenceTypeDef
):
    """
    Type definition for `ClientAttachTypedLinkResponseTypedLinkSpecifier` `TargetObjectReference`

    Identifies the target object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAttachTypedLinkResponseTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_ClientAttachTypedLinkResponseTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ClientAttachTypedLinkResponseTypedLinkSpecifierTypedLinkFacetTypeDef(
    _ClientAttachTypedLinkResponseTypedLinkSpecifierTypedLinkFacetTypeDef
):
    """
    Type definition for `ClientAttachTypedLinkResponseTypedLinkSpecifier` `TypedLinkFacet`

    Identifies the typed link facet that is associated with the typed link.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) that is associated with the schema. For more information,
      see  arns .

    - **TypedLinkName** *(string) --*

      The unique name of the typed link facet.
    """


_ClientAttachTypedLinkResponseTypedLinkSpecifierTypeDef = TypedDict(
    "_ClientAttachTypedLinkResponseTypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": ClientAttachTypedLinkResponseTypedLinkSpecifierTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientAttachTypedLinkResponseTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientAttachTypedLinkResponseTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientAttachTypedLinkResponseTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientAttachTypedLinkResponseTypedLinkSpecifierTypeDef(
    _ClientAttachTypedLinkResponseTypedLinkSpecifierTypeDef
):
    """
    Type definition for `ClientAttachTypedLinkResponse` `TypedLinkSpecifier`

    Returns a typed link specifier as output.

    - **TypedLinkFacet** *(dict) --*

      Identifies the typed link facet that is associated with the typed link.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) that is associated with the schema. For more information,
        see  arns .

      - **TypedLinkName** *(string) --*

        The unique name of the typed link facet.

    - **SourceObjectReference** *(dict) --*

      Identifies the source object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **TargetObjectReference** *(dict) --*

      Identifies the target object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **IdentityAttributeValues** *(list) --*

      Identifies the attribute value to update.

      - *(dict) --*

        Identifies the attribute name and value for a typed link.

        - **AttributeName** *(string) --*

          The attribute name of the typed link.

        - **Value** *(dict) --*

          The value for the typed link.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ClientAttachTypedLinkResponseTypeDef = TypedDict(
    "_ClientAttachTypedLinkResponseTypeDef",
    {"TypedLinkSpecifier": ClientAttachTypedLinkResponseTypedLinkSpecifierTypeDef},
    total=False,
)


class ClientAttachTypedLinkResponseTypeDef(_ClientAttachTypedLinkResponseTypeDef):
    """
    Type definition for `ClientAttachTypedLink` `Response`

    - **TypedLinkSpecifier** *(dict) --*

      Returns a typed link specifier as output.

      - **TypedLinkFacet** *(dict) --*

        Identifies the typed link facet that is associated with the typed link.

        - **SchemaArn** *(string) --*

          The Amazon Resource Name (ARN) that is associated with the schema. For more information,
          see  arns .

        - **TypedLinkName** *(string) --*

          The unique name of the typed link facet.

      - **SourceObjectReference** *(dict) --*

        Identifies the source object that the typed link will attach to.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **TargetObjectReference** *(dict) --*

        Identifies the target object that the typed link will attach to.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **IdentityAttributeValues** *(list) --*

        Identifies the attribute value to update.

        - *(dict) --*

          Identifies the attribute name and value for a typed link.

          - **AttributeName** *(string) --*

            The attribute name of the typed link.

          - **Value** *(dict) --*

            The value for the typed link.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.
    """


_ClientAttachTypedLinkSourceObjectReferenceTypeDef = TypedDict(
    "_ClientAttachTypedLinkSourceObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientAttachTypedLinkSourceObjectReferenceTypeDef(
    _ClientAttachTypedLinkSourceObjectReferenceTypeDef
):
    """
    Type definition for `ClientAttachTypedLink` `SourceObjectReference`

    Identifies the source object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAttachTypedLinkTargetObjectReferenceTypeDef = TypedDict(
    "_ClientAttachTypedLinkTargetObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientAttachTypedLinkTargetObjectReferenceTypeDef(
    _ClientAttachTypedLinkTargetObjectReferenceTypeDef
):
    """
    Type definition for `ClientAttachTypedLink` `TargetObjectReference`

    Identifies the target object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientAttachTypedLinkTypedLinkFacetTypeDef = TypedDict(
    "_ClientAttachTypedLinkTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
)


class ClientAttachTypedLinkTypedLinkFacetTypeDef(
    _ClientAttachTypedLinkTypedLinkFacetTypeDef
):
    """
    Type definition for `ClientAttachTypedLink` `TypedLinkFacet`

    Identifies the typed link facet that is associated with the typed link.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
      arns .

    - **TypedLinkName** *(string) --* **[REQUIRED]**

      The unique name of the typed link facet.
    """


_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef(
    _ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValues` `Value`

    The value for the typed link.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
)


class ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef(
    _ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifier` `IdentityAttributeValues`

    Identifies the attribute name and value for a typed link.

    - **AttributeName** *(string) --* **[REQUIRED]**

      The attribute name of the typed link.

    - **Value** *(dict) --* **[REQUIRED]**

      The value for the typed link.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef(
    _ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifier` `SourceObjectReference`

    Identifies the source object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading
      to it from the directory root. Use the link names from each parent/child link to
      construct the path. Path selectors start with a slash (/) and link names are separated
      by slashes. For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
      Cloud Directory. When creating objects, the system will provide you with the identifier
      of the created object. An object’s identifier is immutable and no two objects will ever
      share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef(
    _ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifier` `TargetObjectReference`

    Identifies the target object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading
      to it from the directory root. Use the link names from each parent/child link to
      construct the path. Path selectors start with a slash (/) and link names are separated
      by slashes. For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
      Cloud Directory. When creating objects, the system will provide you with the identifier
      of the created object. An object’s identifier is immutable and no two objects will ever
      share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
)


class ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef(
    _ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifier` `TypedLinkFacet`

    Identifies the typed link facet that is associated with the typed link.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more
      information, see  arns .

    - **TypedLinkName** *(string) --* **[REQUIRED]**

      The unique name of the typed link facet.
    """


_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
)


class ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypeDef(
    _ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsGetLinkAttributes` `TypedLinkSpecifier`

    Allows a typed link specifier to be accepted as input.

    - **TypedLinkFacet** *(dict) --* **[REQUIRED]**

      Identifies the typed link facet that is associated with the typed link.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) that is associated with the schema. For more
        information, see  arns .

      - **TypedLinkName** *(string) --* **[REQUIRED]**

        The unique name of the typed link facet.

    - **SourceObjectReference** *(dict) --* **[REQUIRED]**

      Identifies the source object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading
        to it from the directory root. Use the link names from each parent/child link to
        construct the path. Path selectors start with a slash (/) and link names are separated
        by slashes. For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
        Cloud Directory. When creating objects, the system will provide you with the identifier
        of the created object. An object’s identifier is immutable and no two objects will ever
        share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **TargetObjectReference** *(dict) --* **[REQUIRED]**

      Identifies the target object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading
        to it from the directory root. Use the link names from each parent/child link to
        construct the path. Path selectors start with a slash (/) and link names are separated
        by slashes. For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
        Cloud Directory. When creating objects, the system will provide you with the identifier
        of the created object. An object’s identifier is immutable and no two objects will ever
        share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **IdentityAttributeValues** *(list) --* **[REQUIRED]**

      Identifies the attribute value to update.

      - *(dict) --*

        Identifies the attribute name and value for a typed link.

        - **AttributeName** *(string) --* **[REQUIRED]**

          The attribute name of the typed link.

        - **Value** *(dict) --* **[REQUIRED]**

          The value for the typed link.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ClientBatchReadOperationsGetLinkAttributesTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": ClientBatchReadOperationsGetLinkAttributesTypedLinkSpecifierTypeDef,
        "AttributeNames": List[str],
    },
)


class ClientBatchReadOperationsGetLinkAttributesTypeDef(
    _ClientBatchReadOperationsGetLinkAttributesTypeDef
):
    """
    Type definition for `ClientBatchReadOperations` `GetLinkAttributes`

    Retrieves attributes that are associated with a typed link.

    - **TypedLinkSpecifier** *(dict) --* **[REQUIRED]**

      Allows a typed link specifier to be accepted as input.

      - **TypedLinkFacet** *(dict) --* **[REQUIRED]**

        Identifies the typed link facet that is associated with the typed link.

        - **SchemaArn** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) that is associated with the schema. For more
          information, see  arns .

        - **TypedLinkName** *(string) --* **[REQUIRED]**

          The unique name of the typed link facet.

      - **SourceObjectReference** *(dict) --* **[REQUIRED]**

        Identifies the source object that the typed link will attach to.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading
          to it from the directory root. Use the link names from each parent/child link to
          construct the path. Path selectors start with a slash (/) and link names are separated
          by slashes. For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
          Cloud Directory. When creating objects, the system will provide you with the identifier
          of the created object. An object’s identifier is immutable and no two objects will ever
          share the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **TargetObjectReference** *(dict) --* **[REQUIRED]**

        Identifies the target object that the typed link will attach to.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading
          to it from the directory root. Use the link names from each parent/child link to
          construct the path. Path selectors start with a slash (/) and link names are separated
          by slashes. For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
          Cloud Directory. When creating objects, the system will provide you with the identifier
          of the created object. An object’s identifier is immutable and no two objects will ever
          share the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **IdentityAttributeValues** *(list) --* **[REQUIRED]**

        Identifies the attribute value to update.

        - *(dict) --*

          Identifies the attribute name and value for a typed link.

          - **AttributeName** *(string) --* **[REQUIRED]**

            The attribute name of the typed link.

          - **Value** *(dict) --* **[REQUIRED]**

            The value for the typed link.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.

    - **AttributeNames** *(list) --* **[REQUIRED]**

      A list of attribute names whose values will be retrieved.

      - *(string) --*
    """


_ClientBatchReadOperationsGetObjectAttributesObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetObjectAttributesObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsGetObjectAttributesObjectReferenceTypeDef(
    _ClientBatchReadOperationsGetObjectAttributesObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsGetObjectAttributes` `ObjectReference`

    Reference that identifies the object whose attributes will be retrieved.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchReadOperationsGetObjectAttributesSchemaFacetTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetObjectAttributesSchemaFacetTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientBatchReadOperationsGetObjectAttributesSchemaFacetTypeDef(
    _ClientBatchReadOperationsGetObjectAttributesSchemaFacetTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsGetObjectAttributes` `SchemaFacet`

    Identifier for the facet whose attributes will be retrieved. See  SchemaFacet for details.

    - **SchemaArn** *(string) --*

      The ARN of the schema that contains the facet with no minor component. See  arns and
      `In-Place Schema Upgrade
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
      for a description of when to provide minor versions.

    - **FacetName** *(string) --*

      The name of the facet.
    """


_ClientBatchReadOperationsGetObjectAttributesTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetObjectAttributesTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsGetObjectAttributesObjectReferenceTypeDef,
        "SchemaFacet": ClientBatchReadOperationsGetObjectAttributesSchemaFacetTypeDef,
        "AttributeNames": List[str],
    },
)


class ClientBatchReadOperationsGetObjectAttributesTypeDef(
    _ClientBatchReadOperationsGetObjectAttributesTypeDef
):
    """
    Type definition for `ClientBatchReadOperations` `GetObjectAttributes`

    Retrieves attributes within a facet that are associated with an object.

    - **ObjectReference** *(dict) --* **[REQUIRED]**

      Reference that identifies the object whose attributes will be retrieved.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **SchemaFacet** *(dict) --* **[REQUIRED]**

      Identifier for the facet whose attributes will be retrieved. See  SchemaFacet for details.

      - **SchemaArn** *(string) --*

        The ARN of the schema that contains the facet with no minor component. See  arns and
        `In-Place Schema Upgrade
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
        for a description of when to provide minor versions.

      - **FacetName** *(string) --*

        The name of the facet.

    - **AttributeNames** *(list) --* **[REQUIRED]**

      List of attribute names whose values will be retrieved.

      - *(string) --*
    """


_ClientBatchReadOperationsGetObjectInformationObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetObjectInformationObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsGetObjectInformationObjectReferenceTypeDef(
    _ClientBatchReadOperationsGetObjectInformationObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsGetObjectInformation` `ObjectReference`

    A reference to the object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchReadOperationsGetObjectInformationTypeDef = TypedDict(
    "_ClientBatchReadOperationsGetObjectInformationTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsGetObjectInformationObjectReferenceTypeDef
    },
)


class ClientBatchReadOperationsGetObjectInformationTypeDef(
    _ClientBatchReadOperationsGetObjectInformationTypeDef
):
    """
    Type definition for `ClientBatchReadOperations` `GetObjectInformation`

    Retrieves metadata about an object.

    - **ObjectReference** *(dict) --* **[REQUIRED]**

      A reference to the object.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchReadOperationsListAttachedIndicesTargetReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListAttachedIndicesTargetReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListAttachedIndicesTargetReferenceTypeDef(
    _ClientBatchReadOperationsListAttachedIndicesTargetReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListAttachedIndices` `TargetReference`

    A reference to the object that has indices attached.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_RequiredClientBatchReadOperationsListAttachedIndicesTypeDef = TypedDict(
    "_RequiredClientBatchReadOperationsListAttachedIndicesTypeDef",
    {
        "TargetReference": ClientBatchReadOperationsListAttachedIndicesTargetReferenceTypeDef
    },
)
_OptionalClientBatchReadOperationsListAttachedIndicesTypeDef = TypedDict(
    "_OptionalClientBatchReadOperationsListAttachedIndicesTypeDef",
    {"NextToken": str, "MaxResults": int},
    total=False,
)


class ClientBatchReadOperationsListAttachedIndicesTypeDef(
    _RequiredClientBatchReadOperationsListAttachedIndicesTypeDef,
    _OptionalClientBatchReadOperationsListAttachedIndicesTypeDef,
):
    """
    Type definition for `ClientBatchReadOperations` `ListAttachedIndices`

    Lists indices attached to an object.

    - **TargetReference** *(dict) --* **[REQUIRED]**

      A reference to the object that has indices attached.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **NextToken** *(string) --*

      The pagination token.

    - **MaxResults** *(integer) --*

      The maximum number of results to retrieve.
    """


_ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef(
    _ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRange` `EndValue`

    The attribute value to terminate the range at.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef(
    _ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRange` `StartValue`

    The value to start the range at.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_RequiredClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef = TypedDict(
    "_RequiredClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef",
    {"StartMode": str, "EndMode": str},
)
_OptionalClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef = TypedDict(
    "_OptionalClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef",
    {
        "StartValue": ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef,
        "EndValue": ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef,
    },
    total=False,
)


class ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef(
    _RequiredClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef,
    _OptionalClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef,
):
    """
    Type definition for `ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRanges` `Range`

    The range of attribute values that are being selected.

    - **StartMode** *(string) --* **[REQUIRED]**

      The inclusive or exclusive range start.

    - **StartValue** *(dict) --*

      The value to start the range at.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.

    - **EndMode** *(string) --* **[REQUIRED]**

      The inclusive or exclusive range end.

    - **EndValue** *(dict) --*

      The attribute value to terminate the range at.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_RequiredClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef = TypedDict(
    "_RequiredClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef",
    {
        "Range": ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesRangeTypeDef
    },
)
_OptionalClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef = TypedDict(
    "_OptionalClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef",
    {"AttributeName": str},
    total=False,
)


class ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef(
    _RequiredClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef,
    _OptionalClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef,
):
    """
    Type definition for `ClientBatchReadOperationsListIncomingTypedLinks` `FilterAttributeRanges`

    Identifies the range of attributes that are used by a specified filter.

    - **AttributeName** *(string) --*

      The unique name of the typed link attribute.

    - **Range** *(dict) --* **[REQUIRED]**

      The range of attribute values that are being selected.

      - **StartMode** *(string) --* **[REQUIRED]**

        The inclusive or exclusive range start.

      - **StartValue** *(dict) --*

        The value to start the range at.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.

      - **EndMode** *(string) --* **[REQUIRED]**

        The inclusive or exclusive range end.

      - **EndValue** *(dict) --*

        The attribute value to terminate the range at.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.
    """


_ClientBatchReadOperationsListIncomingTypedLinksFilterTypedLinkTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIncomingTypedLinksFilterTypedLinkTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
)


class ClientBatchReadOperationsListIncomingTypedLinksFilterTypedLinkTypeDef(
    _ClientBatchReadOperationsListIncomingTypedLinksFilterTypedLinkTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListIncomingTypedLinks` `FilterTypedLink`

    Filters are interpreted in the order of the attributes on the typed link facet, not the
    order in which they are supplied to any API calls.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more information,
      see  arns .

    - **TypedLinkName** *(string) --* **[REQUIRED]**

      The unique name of the typed link facet.
    """


_ClientBatchReadOperationsListIncomingTypedLinksObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIncomingTypedLinksObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListIncomingTypedLinksObjectReferenceTypeDef(
    _ClientBatchReadOperationsListIncomingTypedLinksObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListIncomingTypedLinks` `ObjectReference`

    The reference that identifies the object whose attributes will be listed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_RequiredClientBatchReadOperationsListIncomingTypedLinksTypeDef = TypedDict(
    "_RequiredClientBatchReadOperationsListIncomingTypedLinksTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListIncomingTypedLinksObjectReferenceTypeDef
    },
)
_OptionalClientBatchReadOperationsListIncomingTypedLinksTypeDef = TypedDict(
    "_OptionalClientBatchReadOperationsListIncomingTypedLinksTypeDef",
    {
        "FilterAttributeRanges": List[
            ClientBatchReadOperationsListIncomingTypedLinksFilterAttributeRangesTypeDef
        ],
        "FilterTypedLink": ClientBatchReadOperationsListIncomingTypedLinksFilterTypedLinkTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ClientBatchReadOperationsListIncomingTypedLinksTypeDef(
    _RequiredClientBatchReadOperationsListIncomingTypedLinksTypeDef,
    _OptionalClientBatchReadOperationsListIncomingTypedLinksTypeDef,
):
    """
    Type definition for `ClientBatchReadOperations` `ListIncomingTypedLinks`

    Returns a paginated list of all the incoming  TypedLinkSpecifier information for an object.
    It also supports filtering by typed link facet and identity attributes. For more information,
    see `Typed Links
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
    .

    - **ObjectReference** *(dict) --* **[REQUIRED]**

      The reference that identifies the object whose attributes will be listed.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **FilterAttributeRanges** *(list) --*

      Provides range filters for multiple attributes. When providing ranges to typed link
      selection, any inexact ranges must be specified at the end. Any attributes that do not have
      a range specified are presumed to match the entire range.

      - *(dict) --*

        Identifies the range of attributes that are used by a specified filter.

        - **AttributeName** *(string) --*

          The unique name of the typed link attribute.

        - **Range** *(dict) --* **[REQUIRED]**

          The range of attribute values that are being selected.

          - **StartMode** *(string) --* **[REQUIRED]**

            The inclusive or exclusive range start.

          - **StartValue** *(dict) --*

            The value to start the range at.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.

          - **EndMode** *(string) --* **[REQUIRED]**

            The inclusive or exclusive range end.

          - **EndValue** *(dict) --*

            The attribute value to terminate the range at.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.

    - **FilterTypedLink** *(dict) --*

      Filters are interpreted in the order of the attributes on the typed link facet, not the
      order in which they are supplied to any API calls.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) that is associated with the schema. For more information,
        see  arns .

      - **TypedLinkName** *(string) --* **[REQUIRED]**

        The unique name of the typed link facet.

    - **NextToken** *(string) --*

      The pagination token.

    - **MaxResults** *(integer) --*

      The maximum number of results to retrieve.
    """


_ClientBatchReadOperationsListIndexIndexReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIndexIndexReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListIndexIndexReferenceTypeDef(
    _ClientBatchReadOperationsListIndexIndexReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListIndex` `IndexReference`

    The reference to the index to list.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchReadOperationsListIndexRangesOnIndexedValuesAttributeKeyTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIndexRangesOnIndexedValuesAttributeKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
)


class ClientBatchReadOperationsListIndexRangesOnIndexedValuesAttributeKeyTypeDef(
    _ClientBatchReadOperationsListIndexRangesOnIndexedValuesAttributeKeyTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListIndexRangesOnIndexedValues` `AttributeKey`

    The key of the attribute that the attribute range covers.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --* **[REQUIRED]**

      The name of the facet that the attribute exists within.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.
    """


_ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeEndValueTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeEndValueTypeDef(
    _ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeEndValueTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListIndexRangesOnIndexedValuesRange` `EndValue`

    The attribute value to terminate the range at.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeStartValueTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeStartValueTypeDef(
    _ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeStartValueTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListIndexRangesOnIndexedValuesRange` `StartValue`

    The value to start the range at.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_RequiredClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef = TypedDict(
    "_RequiredClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef",
    {"StartMode": str, "EndMode": str},
)
_OptionalClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef = TypedDict(
    "_OptionalClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef",
    {
        "StartValue": ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeStartValueTypeDef,
        "EndValue": ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeEndValueTypeDef,
    },
    total=False,
)


class ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef(
    _RequiredClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef,
    _OptionalClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef,
):
    """
    Type definition for `ClientBatchReadOperationsListIndexRangesOnIndexedValues` `Range`

    The range of attribute values being selected.

    - **StartMode** *(string) --* **[REQUIRED]**

      The inclusive or exclusive range start.

    - **StartValue** *(dict) --*

      The value to start the range at.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.

    - **EndMode** *(string) --* **[REQUIRED]**

      The inclusive or exclusive range end.

    - **EndValue** *(dict) --*

      The attribute value to terminate the range at.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientBatchReadOperationsListIndexRangesOnIndexedValuesTypeDef = TypedDict(
    "_ClientBatchReadOperationsListIndexRangesOnIndexedValuesTypeDef",
    {
        "AttributeKey": ClientBatchReadOperationsListIndexRangesOnIndexedValuesAttributeKeyTypeDef,
        "Range": ClientBatchReadOperationsListIndexRangesOnIndexedValuesRangeTypeDef,
    },
    total=False,
)


class ClientBatchReadOperationsListIndexRangesOnIndexedValuesTypeDef(
    _ClientBatchReadOperationsListIndexRangesOnIndexedValuesTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListIndex` `RangesOnIndexedValues`

    A range of attributes.

    - **AttributeKey** *(dict) --*

      The key of the attribute that the attribute range covers.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --* **[REQUIRED]**

        The name of the facet that the attribute exists within.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the attribute.

    - **Range** *(dict) --*

      The range of attribute values being selected.

      - **StartMode** *(string) --* **[REQUIRED]**

        The inclusive or exclusive range start.

      - **StartValue** *(dict) --*

        The value to start the range at.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.

      - **EndMode** *(string) --* **[REQUIRED]**

        The inclusive or exclusive range end.

      - **EndValue** *(dict) --*

        The attribute value to terminate the range at.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.
    """


_RequiredClientBatchReadOperationsListIndexTypeDef = TypedDict(
    "_RequiredClientBatchReadOperationsListIndexTypeDef",
    {"IndexReference": ClientBatchReadOperationsListIndexIndexReferenceTypeDef},
)
_OptionalClientBatchReadOperationsListIndexTypeDef = TypedDict(
    "_OptionalClientBatchReadOperationsListIndexTypeDef",
    {
        "RangesOnIndexedValues": List[
            ClientBatchReadOperationsListIndexRangesOnIndexedValuesTypeDef
        ],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)


class ClientBatchReadOperationsListIndexTypeDef(
    _RequiredClientBatchReadOperationsListIndexTypeDef,
    _OptionalClientBatchReadOperationsListIndexTypeDef,
):
    """
    Type definition for `ClientBatchReadOperations` `ListIndex`

    Lists objects attached to the specified index.

    - **RangesOnIndexedValues** *(list) --*

      Specifies the ranges of indexed values that you want to query.

      - *(dict) --*

        A range of attributes.

        - **AttributeKey** *(dict) --*

          The key of the attribute that the attribute range covers.

          - **SchemaArn** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

          - **FacetName** *(string) --* **[REQUIRED]**

            The name of the facet that the attribute exists within.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the attribute.

        - **Range** *(dict) --*

          The range of attribute values being selected.

          - **StartMode** *(string) --* **[REQUIRED]**

            The inclusive or exclusive range start.

          - **StartValue** *(dict) --*

            The value to start the range at.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.

          - **EndMode** *(string) --* **[REQUIRED]**

            The inclusive or exclusive range end.

          - **EndValue** *(dict) --*

            The attribute value to terminate the range at.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.

    - **IndexReference** *(dict) --* **[REQUIRED]**

      The reference to the index to list.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **MaxResults** *(integer) --*

      The maximum number of results to retrieve.

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientBatchReadOperationsListObjectAttributesFacetFilterTypeDef = TypedDict(
    "_ClientBatchReadOperationsListObjectAttributesFacetFilterTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientBatchReadOperationsListObjectAttributesFacetFilterTypeDef(
    _ClientBatchReadOperationsListObjectAttributesFacetFilterTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListObjectAttributes` `FacetFilter`

    Used to filter the list of object attributes that are associated with a certain facet.

    - **SchemaArn** *(string) --*

      The ARN of the schema that contains the facet with no minor component. See  arns and
      `In-Place Schema Upgrade
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
      for a description of when to provide minor versions.

    - **FacetName** *(string) --*

      The name of the facet.
    """


_ClientBatchReadOperationsListObjectAttributesObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListObjectAttributesObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListObjectAttributesObjectReferenceTypeDef(
    _ClientBatchReadOperationsListObjectAttributesObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListObjectAttributes` `ObjectReference`

    Reference of the object whose attributes need to be listed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_RequiredClientBatchReadOperationsListObjectAttributesTypeDef = TypedDict(
    "_RequiredClientBatchReadOperationsListObjectAttributesTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListObjectAttributesObjectReferenceTypeDef
    },
)
_OptionalClientBatchReadOperationsListObjectAttributesTypeDef = TypedDict(
    "_OptionalClientBatchReadOperationsListObjectAttributesTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "FacetFilter": ClientBatchReadOperationsListObjectAttributesFacetFilterTypeDef,
    },
    total=False,
)


class ClientBatchReadOperationsListObjectAttributesTypeDef(
    _RequiredClientBatchReadOperationsListObjectAttributesTypeDef,
    _OptionalClientBatchReadOperationsListObjectAttributesTypeDef,
):
    """
    Type definition for `ClientBatchReadOperations` `ListObjectAttributes`

    Lists all attributes that are associated with an object.

    - **ObjectReference** *(dict) --* **[REQUIRED]**

      Reference of the object whose attributes need to be listed.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **NextToken** *(string) --*

      The pagination token.

    - **MaxResults** *(integer) --*

      The maximum number of items to be retrieved in a single call. This is an approximate number.

    - **FacetFilter** *(dict) --*

      Used to filter the list of object attributes that are associated with a certain facet.

      - **SchemaArn** *(string) --*

        The ARN of the schema that contains the facet with no minor component. See  arns and
        `In-Place Schema Upgrade
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
        for a description of when to provide minor versions.

      - **FacetName** *(string) --*

        The name of the facet.
    """


_ClientBatchReadOperationsListObjectChildrenObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListObjectChildrenObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListObjectChildrenObjectReferenceTypeDef(
    _ClientBatchReadOperationsListObjectChildrenObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListObjectChildren` `ObjectReference`

    Reference of the object for which child objects are being listed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_RequiredClientBatchReadOperationsListObjectChildrenTypeDef = TypedDict(
    "_RequiredClientBatchReadOperationsListObjectChildrenTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListObjectChildrenObjectReferenceTypeDef
    },
)
_OptionalClientBatchReadOperationsListObjectChildrenTypeDef = TypedDict(
    "_OptionalClientBatchReadOperationsListObjectChildrenTypeDef",
    {"NextToken": str, "MaxResults": int},
    total=False,
)


class ClientBatchReadOperationsListObjectChildrenTypeDef(
    _RequiredClientBatchReadOperationsListObjectChildrenTypeDef,
    _OptionalClientBatchReadOperationsListObjectChildrenTypeDef,
):
    """
    Type definition for `ClientBatchReadOperations` `ListObjectChildren`

    Returns a paginated list of child objects that are associated with a given object.

    - **ObjectReference** *(dict) --* **[REQUIRED]**

      Reference of the object for which child objects are being listed.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **NextToken** *(string) --*

      The pagination token.

    - **MaxResults** *(integer) --*

      Maximum number of items to be retrieved in a single call. This is an approximate number.
    """


_ClientBatchReadOperationsListObjectParentPathsObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListObjectParentPathsObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListObjectParentPathsObjectReferenceTypeDef(
    _ClientBatchReadOperationsListObjectParentPathsObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListObjectParentPaths` `ObjectReference`

    The reference that identifies the object whose attributes will be listed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_RequiredClientBatchReadOperationsListObjectParentPathsTypeDef = TypedDict(
    "_RequiredClientBatchReadOperationsListObjectParentPathsTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListObjectParentPathsObjectReferenceTypeDef
    },
)
_OptionalClientBatchReadOperationsListObjectParentPathsTypeDef = TypedDict(
    "_OptionalClientBatchReadOperationsListObjectParentPathsTypeDef",
    {"NextToken": str, "MaxResults": int},
    total=False,
)


class ClientBatchReadOperationsListObjectParentPathsTypeDef(
    _RequiredClientBatchReadOperationsListObjectParentPathsTypeDef,
    _OptionalClientBatchReadOperationsListObjectParentPathsTypeDef,
):
    """
    Type definition for `ClientBatchReadOperations` `ListObjectParentPaths`

    Retrieves all available parent paths for any object type such as node, leaf node, policy
    node, and index node objects. For more information about objects, see `Directory Structure
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directorystructure.html>`__
    .

    - **ObjectReference** *(dict) --* **[REQUIRED]**

      The reference that identifies the object whose attributes will be listed.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **NextToken** *(string) --*

      The pagination token.

    - **MaxResults** *(integer) --*

      The maximum number of results to retrieve.
    """


_ClientBatchReadOperationsListObjectParentsObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListObjectParentsObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListObjectParentsObjectReferenceTypeDef(
    _ClientBatchReadOperationsListObjectParentsObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListObjectParents` `ObjectReference`

    The reference that identifies an object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_RequiredClientBatchReadOperationsListObjectParentsTypeDef = TypedDict(
    "_RequiredClientBatchReadOperationsListObjectParentsTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListObjectParentsObjectReferenceTypeDef
    },
)
_OptionalClientBatchReadOperationsListObjectParentsTypeDef = TypedDict(
    "_OptionalClientBatchReadOperationsListObjectParentsTypeDef",
    {"NextToken": str, "MaxResults": int},
    total=False,
)


class ClientBatchReadOperationsListObjectParentsTypeDef(
    _RequiredClientBatchReadOperationsListObjectParentsTypeDef,
    _OptionalClientBatchReadOperationsListObjectParentsTypeDef,
):
    """
    Type definition for `ClientBatchReadOperations` `ListObjectParents`

    - **ObjectReference** *(dict) --* **[REQUIRED]**

      The reference that identifies an object.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **NextToken** *(string) --*

    - **MaxResults** *(integer) --*
    """


_ClientBatchReadOperationsListObjectPoliciesObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListObjectPoliciesObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListObjectPoliciesObjectReferenceTypeDef(
    _ClientBatchReadOperationsListObjectPoliciesObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListObjectPolicies` `ObjectReference`

    The reference that identifies the object whose attributes will be listed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_RequiredClientBatchReadOperationsListObjectPoliciesTypeDef = TypedDict(
    "_RequiredClientBatchReadOperationsListObjectPoliciesTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListObjectPoliciesObjectReferenceTypeDef
    },
)
_OptionalClientBatchReadOperationsListObjectPoliciesTypeDef = TypedDict(
    "_OptionalClientBatchReadOperationsListObjectPoliciesTypeDef",
    {"NextToken": str, "MaxResults": int},
    total=False,
)


class ClientBatchReadOperationsListObjectPoliciesTypeDef(
    _RequiredClientBatchReadOperationsListObjectPoliciesTypeDef,
    _OptionalClientBatchReadOperationsListObjectPoliciesTypeDef,
):
    """
    Type definition for `ClientBatchReadOperations` `ListObjectPolicies`

    Returns policies attached to an object in pagination fashion.

    - **ObjectReference** *(dict) --* **[REQUIRED]**

      The reference that identifies the object whose attributes will be listed.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **NextToken** *(string) --*

      The pagination token.

    - **MaxResults** *(integer) --*

      The maximum number of results to retrieve.
    """


_ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef = TypedDict(
    "_ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef(
    _ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRange` `EndValue`

    The attribute value to terminate the range at.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef = TypedDict(
    "_ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef(
    _ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRange` `StartValue`

    The value to start the range at.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_RequiredClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef = TypedDict(
    "_RequiredClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef",
    {"StartMode": str, "EndMode": str},
)
_OptionalClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef = TypedDict(
    "_OptionalClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef",
    {
        "StartValue": ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef,
        "EndValue": ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef,
    },
    total=False,
)


class ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef(
    _RequiredClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef,
    _OptionalClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef,
):
    """
    Type definition for `ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRanges` `Range`

    The range of attribute values that are being selected.

    - **StartMode** *(string) --* **[REQUIRED]**

      The inclusive or exclusive range start.

    - **StartValue** *(dict) --*

      The value to start the range at.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.

    - **EndMode** *(string) --* **[REQUIRED]**

      The inclusive or exclusive range end.

    - **EndValue** *(dict) --*

      The attribute value to terminate the range at.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_RequiredClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef = TypedDict(
    "_RequiredClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef",
    {
        "Range": ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef
    },
)
_OptionalClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef = TypedDict(
    "_OptionalClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef",
    {"AttributeName": str},
    total=False,
)


class ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef(
    _RequiredClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef,
    _OptionalClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef,
):
    """
    Type definition for `ClientBatchReadOperationsListOutgoingTypedLinks` `FilterAttributeRanges`

    Identifies the range of attributes that are used by a specified filter.

    - **AttributeName** *(string) --*

      The unique name of the typed link attribute.

    - **Range** *(dict) --* **[REQUIRED]**

      The range of attribute values that are being selected.

      - **StartMode** *(string) --* **[REQUIRED]**

        The inclusive or exclusive range start.

      - **StartValue** *(dict) --*

        The value to start the range at.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.

      - **EndMode** *(string) --* **[REQUIRED]**

        The inclusive or exclusive range end.

      - **EndValue** *(dict) --*

        The attribute value to terminate the range at.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.
    """


_ClientBatchReadOperationsListOutgoingTypedLinksFilterTypedLinkTypeDef = TypedDict(
    "_ClientBatchReadOperationsListOutgoingTypedLinksFilterTypedLinkTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
)


class ClientBatchReadOperationsListOutgoingTypedLinksFilterTypedLinkTypeDef(
    _ClientBatchReadOperationsListOutgoingTypedLinksFilterTypedLinkTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListOutgoingTypedLinks` `FilterTypedLink`

    Filters are interpreted in the order of the attributes defined on the typed link facet, not
    the order they are supplied to any API calls.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more information,
      see  arns .

    - **TypedLinkName** *(string) --* **[REQUIRED]**

      The unique name of the typed link facet.
    """


_ClientBatchReadOperationsListOutgoingTypedLinksObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListOutgoingTypedLinksObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListOutgoingTypedLinksObjectReferenceTypeDef(
    _ClientBatchReadOperationsListOutgoingTypedLinksObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListOutgoingTypedLinks` `ObjectReference`

    The reference that identifies the object whose attributes will be listed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_RequiredClientBatchReadOperationsListOutgoingTypedLinksTypeDef = TypedDict(
    "_RequiredClientBatchReadOperationsListOutgoingTypedLinksTypeDef",
    {
        "ObjectReference": ClientBatchReadOperationsListOutgoingTypedLinksObjectReferenceTypeDef
    },
)
_OptionalClientBatchReadOperationsListOutgoingTypedLinksTypeDef = TypedDict(
    "_OptionalClientBatchReadOperationsListOutgoingTypedLinksTypeDef",
    {
        "FilterAttributeRanges": List[
            ClientBatchReadOperationsListOutgoingTypedLinksFilterAttributeRangesTypeDef
        ],
        "FilterTypedLink": ClientBatchReadOperationsListOutgoingTypedLinksFilterTypedLinkTypeDef,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)


class ClientBatchReadOperationsListOutgoingTypedLinksTypeDef(
    _RequiredClientBatchReadOperationsListOutgoingTypedLinksTypeDef,
    _OptionalClientBatchReadOperationsListOutgoingTypedLinksTypeDef,
):
    """
    Type definition for `ClientBatchReadOperations` `ListOutgoingTypedLinks`

    Returns a paginated list of all the outgoing  TypedLinkSpecifier information for an object.
    It also supports filtering by typed link facet and identity attributes. For more information,
    see `Typed Links
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
    .

    - **ObjectReference** *(dict) --* **[REQUIRED]**

      The reference that identifies the object whose attributes will be listed.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **FilterAttributeRanges** *(list) --*

      Provides range filters for multiple attributes. When providing ranges to typed link
      selection, any inexact ranges must be specified at the end. Any attributes that do not have
      a range specified are presumed to match the entire range.

      - *(dict) --*

        Identifies the range of attributes that are used by a specified filter.

        - **AttributeName** *(string) --*

          The unique name of the typed link attribute.

        - **Range** *(dict) --* **[REQUIRED]**

          The range of attribute values that are being selected.

          - **StartMode** *(string) --* **[REQUIRED]**

            The inclusive or exclusive range start.

          - **StartValue** *(dict) --*

            The value to start the range at.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.

          - **EndMode** *(string) --* **[REQUIRED]**

            The inclusive or exclusive range end.

          - **EndValue** *(dict) --*

            The attribute value to terminate the range at.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.

    - **FilterTypedLink** *(dict) --*

      Filters are interpreted in the order of the attributes defined on the typed link facet, not
      the order they are supplied to any API calls.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) that is associated with the schema. For more information,
        see  arns .

      - **TypedLinkName** *(string) --* **[REQUIRED]**

        The unique name of the typed link facet.

    - **NextToken** *(string) --*

      The pagination token.

    - **MaxResults** *(integer) --*

      The maximum number of results to retrieve.
    """


_ClientBatchReadOperationsListPolicyAttachmentsPolicyReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsListPolicyAttachmentsPolicyReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsListPolicyAttachmentsPolicyReferenceTypeDef(
    _ClientBatchReadOperationsListPolicyAttachmentsPolicyReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsListPolicyAttachments` `PolicyReference`

    The reference that identifies the policy object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_RequiredClientBatchReadOperationsListPolicyAttachmentsTypeDef = TypedDict(
    "_RequiredClientBatchReadOperationsListPolicyAttachmentsTypeDef",
    {
        "PolicyReference": ClientBatchReadOperationsListPolicyAttachmentsPolicyReferenceTypeDef
    },
)
_OptionalClientBatchReadOperationsListPolicyAttachmentsTypeDef = TypedDict(
    "_OptionalClientBatchReadOperationsListPolicyAttachmentsTypeDef",
    {"NextToken": str, "MaxResults": int},
    total=False,
)


class ClientBatchReadOperationsListPolicyAttachmentsTypeDef(
    _RequiredClientBatchReadOperationsListPolicyAttachmentsTypeDef,
    _OptionalClientBatchReadOperationsListPolicyAttachmentsTypeDef,
):
    """
    Type definition for `ClientBatchReadOperations` `ListPolicyAttachments`

    Returns all of the ``ObjectIdentifiers`` to which a given policy is attached.

    - **PolicyReference** *(dict) --* **[REQUIRED]**

      The reference that identifies the policy object.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **NextToken** *(string) --*

      The pagination token.

    - **MaxResults** *(integer) --*

      The maximum number of results to retrieve.
    """


_ClientBatchReadOperationsLookupPolicyObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadOperationsLookupPolicyObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadOperationsLookupPolicyObjectReferenceTypeDef(
    _ClientBatchReadOperationsLookupPolicyObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadOperationsLookupPolicy` `ObjectReference`

    Reference that identifies the object whose policies will be looked up.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_RequiredClientBatchReadOperationsLookupPolicyTypeDef = TypedDict(
    "_RequiredClientBatchReadOperationsLookupPolicyTypeDef",
    {"ObjectReference": ClientBatchReadOperationsLookupPolicyObjectReferenceTypeDef},
)
_OptionalClientBatchReadOperationsLookupPolicyTypeDef = TypedDict(
    "_OptionalClientBatchReadOperationsLookupPolicyTypeDef",
    {"NextToken": str, "MaxResults": int},
    total=False,
)


class ClientBatchReadOperationsLookupPolicyTypeDef(
    _RequiredClientBatchReadOperationsLookupPolicyTypeDef,
    _OptionalClientBatchReadOperationsLookupPolicyTypeDef,
):
    """
    Type definition for `ClientBatchReadOperations` `LookupPolicy`

    Lists all policies from the root of the  Directory to the object specified. If there are no
    policies present, an empty list is returned. If policies are present, and if some objects
    don't have the policies attached, it returns the ``ObjectIdentifier`` for such objects. If
    policies are present, it returns ``ObjectIdentifier`` , ``policyId`` , and ``policyType`` .
    Paths that don't lead to the root from the target object are ignored. For more information,
    see `Policies
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
    .

    - **ObjectReference** *(dict) --* **[REQUIRED]**

      Reference that identifies the object whose policies will be looked up.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **NextToken** *(string) --*

      The pagination token.

    - **MaxResults** *(integer) --*

      The maximum number of results to retrieve.
    """


_ClientBatchReadOperationsTypeDef = TypedDict(
    "_ClientBatchReadOperationsTypeDef",
    {
        "ListObjectAttributes": ClientBatchReadOperationsListObjectAttributesTypeDef,
        "ListObjectChildren": ClientBatchReadOperationsListObjectChildrenTypeDef,
        "ListAttachedIndices": ClientBatchReadOperationsListAttachedIndicesTypeDef,
        "ListObjectParentPaths": ClientBatchReadOperationsListObjectParentPathsTypeDef,
        "GetObjectInformation": ClientBatchReadOperationsGetObjectInformationTypeDef,
        "GetObjectAttributes": ClientBatchReadOperationsGetObjectAttributesTypeDef,
        "ListObjectParents": ClientBatchReadOperationsListObjectParentsTypeDef,
        "ListObjectPolicies": ClientBatchReadOperationsListObjectPoliciesTypeDef,
        "ListPolicyAttachments": ClientBatchReadOperationsListPolicyAttachmentsTypeDef,
        "LookupPolicy": ClientBatchReadOperationsLookupPolicyTypeDef,
        "ListIndex": ClientBatchReadOperationsListIndexTypeDef,
        "ListOutgoingTypedLinks": ClientBatchReadOperationsListOutgoingTypedLinksTypeDef,
        "ListIncomingTypedLinks": ClientBatchReadOperationsListIncomingTypedLinksTypeDef,
        "GetLinkAttributes": ClientBatchReadOperationsGetLinkAttributesTypeDef,
    },
    total=False,
)


class ClientBatchReadOperationsTypeDef(_ClientBatchReadOperationsTypeDef):
    """
    Type definition for `ClientBatchRead` `Operations`

    Represents the output of a ``BatchRead`` operation.

    - **ListObjectAttributes** *(dict) --*

      Lists all attributes that are associated with an object.

      - **ObjectReference** *(dict) --* **[REQUIRED]**

        Reference of the object whose attributes need to be listed.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **NextToken** *(string) --*

        The pagination token.

      - **MaxResults** *(integer) --*

        The maximum number of items to be retrieved in a single call. This is an approximate number.

      - **FacetFilter** *(dict) --*

        Used to filter the list of object attributes that are associated with a certain facet.

        - **SchemaArn** *(string) --*

          The ARN of the schema that contains the facet with no minor component. See  arns and
          `In-Place Schema Upgrade
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
          for a description of when to provide minor versions.

        - **FacetName** *(string) --*

          The name of the facet.

    - **ListObjectChildren** *(dict) --*

      Returns a paginated list of child objects that are associated with a given object.

      - **ObjectReference** *(dict) --* **[REQUIRED]**

        Reference of the object for which child objects are being listed.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **NextToken** *(string) --*

        The pagination token.

      - **MaxResults** *(integer) --*

        Maximum number of items to be retrieved in a single call. This is an approximate number.

    - **ListAttachedIndices** *(dict) --*

      Lists indices attached to an object.

      - **TargetReference** *(dict) --* **[REQUIRED]**

        A reference to the object that has indices attached.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **NextToken** *(string) --*

        The pagination token.

      - **MaxResults** *(integer) --*

        The maximum number of results to retrieve.

    - **ListObjectParentPaths** *(dict) --*

      Retrieves all available parent paths for any object type such as node, leaf node, policy
      node, and index node objects. For more information about objects, see `Directory Structure
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directorystructure.html>`__
      .

      - **ObjectReference** *(dict) --* **[REQUIRED]**

        The reference that identifies the object whose attributes will be listed.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **NextToken** *(string) --*

        The pagination token.

      - **MaxResults** *(integer) --*

        The maximum number of results to retrieve.

    - **GetObjectInformation** *(dict) --*

      Retrieves metadata about an object.

      - **ObjectReference** *(dict) --* **[REQUIRED]**

        A reference to the object.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

    - **GetObjectAttributes** *(dict) --*

      Retrieves attributes within a facet that are associated with an object.

      - **ObjectReference** *(dict) --* **[REQUIRED]**

        Reference that identifies the object whose attributes will be retrieved.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **SchemaFacet** *(dict) --* **[REQUIRED]**

        Identifier for the facet whose attributes will be retrieved. See  SchemaFacet for details.

        - **SchemaArn** *(string) --*

          The ARN of the schema that contains the facet with no minor component. See  arns and
          `In-Place Schema Upgrade
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
          for a description of when to provide minor versions.

        - **FacetName** *(string) --*

          The name of the facet.

      - **AttributeNames** *(list) --* **[REQUIRED]**

        List of attribute names whose values will be retrieved.

        - *(string) --*

    - **ListObjectParents** *(dict) --*

      - **ObjectReference** *(dict) --* **[REQUIRED]**

        The reference that identifies an object.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **NextToken** *(string) --*

      - **MaxResults** *(integer) --*

    - **ListObjectPolicies** *(dict) --*

      Returns policies attached to an object in pagination fashion.

      - **ObjectReference** *(dict) --* **[REQUIRED]**

        The reference that identifies the object whose attributes will be listed.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **NextToken** *(string) --*

        The pagination token.

      - **MaxResults** *(integer) --*

        The maximum number of results to retrieve.

    - **ListPolicyAttachments** *(dict) --*

      Returns all of the ``ObjectIdentifiers`` to which a given policy is attached.

      - **PolicyReference** *(dict) --* **[REQUIRED]**

        The reference that identifies the policy object.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **NextToken** *(string) --*

        The pagination token.

      - **MaxResults** *(integer) --*

        The maximum number of results to retrieve.

    - **LookupPolicy** *(dict) --*

      Lists all policies from the root of the  Directory to the object specified. If there are no
      policies present, an empty list is returned. If policies are present, and if some objects
      don't have the policies attached, it returns the ``ObjectIdentifier`` for such objects. If
      policies are present, it returns ``ObjectIdentifier`` , ``policyId`` , and ``policyType`` .
      Paths that don't lead to the root from the target object are ignored. For more information,
      see `Policies
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
      .

      - **ObjectReference** *(dict) --* **[REQUIRED]**

        Reference that identifies the object whose policies will be looked up.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **NextToken** *(string) --*

        The pagination token.

      - **MaxResults** *(integer) --*

        The maximum number of results to retrieve.

    - **ListIndex** *(dict) --*

      Lists objects attached to the specified index.

      - **RangesOnIndexedValues** *(list) --*

        Specifies the ranges of indexed values that you want to query.

        - *(dict) --*

          A range of attributes.

          - **AttributeKey** *(dict) --*

            The key of the attribute that the attribute range covers.

            - **SchemaArn** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

            - **FacetName** *(string) --* **[REQUIRED]**

              The name of the facet that the attribute exists within.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the attribute.

          - **Range** *(dict) --*

            The range of attribute values being selected.

            - **StartMode** *(string) --* **[REQUIRED]**

              The inclusive or exclusive range start.

            - **StartValue** *(dict) --*

              The value to start the range at.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

            - **EndMode** *(string) --* **[REQUIRED]**

              The inclusive or exclusive range end.

            - **EndValue** *(dict) --*

              The attribute value to terminate the range at.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

      - **IndexReference** *(dict) --* **[REQUIRED]**

        The reference to the index to list.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **MaxResults** *(integer) --*

        The maximum number of results to retrieve.

      - **NextToken** *(string) --*

        The pagination token.

    - **ListOutgoingTypedLinks** *(dict) --*

      Returns a paginated list of all the outgoing  TypedLinkSpecifier information for an object.
      It also supports filtering by typed link facet and identity attributes. For more information,
      see `Typed Links
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
      .

      - **ObjectReference** *(dict) --* **[REQUIRED]**

        The reference that identifies the object whose attributes will be listed.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **FilterAttributeRanges** *(list) --*

        Provides range filters for multiple attributes. When providing ranges to typed link
        selection, any inexact ranges must be specified at the end. Any attributes that do not have
        a range specified are presumed to match the entire range.

        - *(dict) --*

          Identifies the range of attributes that are used by a specified filter.

          - **AttributeName** *(string) --*

            The unique name of the typed link attribute.

          - **Range** *(dict) --* **[REQUIRED]**

            The range of attribute values that are being selected.

            - **StartMode** *(string) --* **[REQUIRED]**

              The inclusive or exclusive range start.

            - **StartValue** *(dict) --*

              The value to start the range at.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

            - **EndMode** *(string) --* **[REQUIRED]**

              The inclusive or exclusive range end.

            - **EndValue** *(dict) --*

              The attribute value to terminate the range at.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

      - **FilterTypedLink** *(dict) --*

        Filters are interpreted in the order of the attributes defined on the typed link facet, not
        the order they are supplied to any API calls.

        - **SchemaArn** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) that is associated with the schema. For more information,
          see  arns .

        - **TypedLinkName** *(string) --* **[REQUIRED]**

          The unique name of the typed link facet.

      - **NextToken** *(string) --*

        The pagination token.

      - **MaxResults** *(integer) --*

        The maximum number of results to retrieve.

    - **ListIncomingTypedLinks** *(dict) --*

      Returns a paginated list of all the incoming  TypedLinkSpecifier information for an object.
      It also supports filtering by typed link facet and identity attributes. For more information,
      see `Typed Links
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
      .

      - **ObjectReference** *(dict) --* **[REQUIRED]**

        The reference that identifies the object whose attributes will be listed.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **FilterAttributeRanges** *(list) --*

        Provides range filters for multiple attributes. When providing ranges to typed link
        selection, any inexact ranges must be specified at the end. Any attributes that do not have
        a range specified are presumed to match the entire range.

        - *(dict) --*

          Identifies the range of attributes that are used by a specified filter.

          - **AttributeName** *(string) --*

            The unique name of the typed link attribute.

          - **Range** *(dict) --* **[REQUIRED]**

            The range of attribute values that are being selected.

            - **StartMode** *(string) --* **[REQUIRED]**

              The inclusive or exclusive range start.

            - **StartValue** *(dict) --*

              The value to start the range at.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

            - **EndMode** *(string) --* **[REQUIRED]**

              The inclusive or exclusive range end.

            - **EndValue** *(dict) --*

              The attribute value to terminate the range at.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

      - **FilterTypedLink** *(dict) --*

        Filters are interpreted in the order of the attributes on the typed link facet, not the
        order in which they are supplied to any API calls.

        - **SchemaArn** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) that is associated with the schema. For more information,
          see  arns .

        - **TypedLinkName** *(string) --* **[REQUIRED]**

          The unique name of the typed link facet.

      - **NextToken** *(string) --*

        The pagination token.

      - **MaxResults** *(integer) --*

        The maximum number of results to retrieve.

    - **GetLinkAttributes** *(dict) --*

      Retrieves attributes that are associated with a typed link.

      - **TypedLinkSpecifier** *(dict) --* **[REQUIRED]**

        Allows a typed link specifier to be accepted as input.

        - **TypedLinkFacet** *(dict) --* **[REQUIRED]**

          Identifies the typed link facet that is associated with the typed link.

          - **SchemaArn** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) that is associated with the schema. For more
            information, see  arns .

          - **TypedLinkName** *(string) --* **[REQUIRED]**

            The unique name of the typed link facet.

        - **SourceObjectReference** *(dict) --* **[REQUIRED]**

          Identifies the source object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links leading
            to it from the directory root. Use the link names from each parent/child link to
            construct the path. Path selectors start with a slash (/) and link names are separated
            by slashes. For more information about paths, see `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
            Cloud Directory. When creating objects, the system will provide you with the identifier
            of the created object. An object’s identifier is immutable and no two objects will ever
            share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **TargetObjectReference** *(dict) --* **[REQUIRED]**

          Identifies the target object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links leading
            to it from the directory root. Use the link names from each parent/child link to
            construct the path. Path selectors start with a slash (/) and link names are separated
            by slashes. For more information about paths, see `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
            Cloud Directory. When creating objects, the system will provide you with the identifier
            of the created object. An object’s identifier is immutable and no two objects will ever
            share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **IdentityAttributeValues** *(list) --* **[REQUIRED]**

          Identifies the attribute value to update.

          - *(dict) --*

            Identifies the attribute name and value for a typed link.

            - **AttributeName** *(string) --* **[REQUIRED]**

              The attribute name of the typed link.

            - **Value** *(dict) --* **[REQUIRED]**

              The value for the typed link.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

      - **AttributeNames** *(list) --* **[REQUIRED]**

        A list of attribute names whose values will be retrieved.

        - *(string) --*
    """


_ClientBatchReadResponseResponsesExceptionResponseTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesExceptionResponseTypeDef",
    {"Type": str, "Message": str},
    total=False,
)


class ClientBatchReadResponseResponsesExceptionResponseTypeDef(
    _ClientBatchReadResponseResponsesExceptionResponseTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponses` `ExceptionResponse`

    Identifies which operation in a batch has failed.

    - **Type** *(string) --*

      A type of exception, such as ``InvalidArnException`` .

    - **Message** *(string) --*

      An exception message that is associated with the failure.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesKeyTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesKeyTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesKeyTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributes` `Key`

    The key of the attribute.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) of the schema that contains the facet and
      attribute.

    - **FacetName** *(string) --*

      The name of the facet that the attribute exists within.

    - **Name** *(string) --*

      The name of the attribute.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesValueTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesValueTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesValueTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributes` `Value`

    The value of the attribute.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesTypeDef",
    {
        "Key": ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesKeyTypeDef,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesValueTypeDef,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributes` `Attributes`

    The combination of an attribute key and an attribute value.

    - **Key** *(dict) --*

      The key of the attribute.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and
        attribute.

      - **FacetName** *(string) --*

        The name of the facet that the attribute exists within.

      - **Name** *(string) --*

        The name of the attribute.

    - **Value** *(dict) --*

      The value of the attribute.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesTypeDef",
    {
        "Attributes": List[
            ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesAttributesTypeDef
        ]
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponse` `GetLinkAttributes`

    The list of attributes to retrieve from the typed link.

    - **Attributes** *(list) --*

      The attributes that are associated with the typed link.

      - *(dict) --*

        The combination of an attribute key and an attribute value.

        - **Key** *(dict) --*

          The key of the attribute.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) of the schema that contains the facet and
            attribute.

          - **FacetName** *(string) --*

            The name of the facet that the attribute exists within.

          - **Name** *(string) --*

            The name of the attribute.

        - **Value** *(dict) --*

          The value of the attribute.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesKeyTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesKeyTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesKeyTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributes` `Key`

    The key of the attribute.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) of the schema that contains the facet and
      attribute.

    - **FacetName** *(string) --*

      The name of the facet that the attribute exists within.

    - **Name** *(string) --*

      The name of the attribute.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesValueTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesValueTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesValueTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributes` `Value`

    The value of the attribute.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesTypeDef",
    {
        "Key": ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesKeyTypeDef,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesValueTypeDef,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributes` `Attributes`

    The combination of an attribute key and an attribute value.

    - **Key** *(dict) --*

      The key of the attribute.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and
        attribute.

      - **FacetName** *(string) --*

        The name of the facet that the attribute exists within.

      - **Name** *(string) --*

        The name of the attribute.

    - **Value** *(dict) --*

      The value of the attribute.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesTypeDef",
    {
        "Attributes": List[
            ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesAttributesTypeDef
        ]
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponse` `GetObjectAttributes`

    Retrieves attributes within a facet that are associated with an object.

    - **Attributes** *(list) --*

      The attribute values that are associated with an object.

      - *(dict) --*

        The combination of an attribute key and an attribute value.

        - **Key** *(dict) --*

          The key of the attribute.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) of the schema that contains the facet and
            attribute.

          - **FacetName** *(string) --*

            The name of the facet that the attribute exists within.

          - **Name** *(string) --*

            The name of the attribute.

        - **Value** *(dict) --*

          The value of the attribute.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationSchemaFacetsTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationSchemaFacetsTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationSchemaFacetsTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationSchemaFacetsTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformation` `SchemaFacets`

    A facet.

    - **SchemaArn** *(string) --*

      The ARN of the schema that contains the facet with no minor component. See  arns
      and `In-Place Schema Upgrade
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
      for a description of when to provide minor versions.

    - **FacetName** *(string) --*

      The name of the facet.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationTypeDef",
    {
        "SchemaFacets": List[
            ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationSchemaFacetsTypeDef
        ],
        "ObjectIdentifier": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponse` `GetObjectInformation`

    Retrieves metadata about an object.

    - **SchemaFacets** *(list) --*

      The facets attached to the specified object.

      - *(dict) --*

        A facet.

        - **SchemaArn** *(string) --*

          The ARN of the schema that contains the facet with no minor component. See  arns
          and `In-Place Schema Upgrade
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
          for a description of when to provide minor versions.

        - **FacetName** *(string) --*

          The name of the facet.

    - **ObjectIdentifier** *(string) --*

      The ``ObjectIdentifier`` of the specified object.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesKeyTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesKeyTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesKeyTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributes` `Key`

    The key of the attribute.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) of the schema that contains the facet and
      attribute.

    - **FacetName** *(string) --*

      The name of the facet that the attribute exists within.

    - **Name** *(string) --*

      The name of the attribute.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesValueTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesValueTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesValueTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributes` `Value`

    The value of the attribute.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesTypeDef",
    {
        "Key": ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesKeyTypeDef,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesValueTypeDef,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachments` `IndexedAttributes`

    The combination of an attribute key and an attribute value.

    - **Key** *(dict) --*

      The key of the attribute.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and
        attribute.

      - **FacetName** *(string) --*

        The name of the facet that the attribute exists within.

      - **Name** *(string) --*

        The name of the attribute.

    - **Value** *(dict) --*

      The value of the attribute.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsTypeDef",
    {
        "IndexedAttributes": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsIndexedAttributesTypeDef
        ],
        "ObjectIdentifier": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndices` `IndexAttachments`

    Represents an index and an attached object.

    - **IndexedAttributes** *(list) --*

      The indexed attribute values.

      - *(dict) --*

        The combination of an attribute key and an attribute value.

        - **Key** *(dict) --*

          The key of the attribute.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) of the schema that contains the facet and
            attribute.

          - **FacetName** *(string) --*

            The name of the facet that the attribute exists within.

          - **Name** *(string) --*

            The name of the attribute.

        - **Value** *(dict) --*

          The value of the attribute.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.

    - **ObjectIdentifier** *(string) --*

      In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to
      the index. In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the
      index attached to the object. This field will always contain the
      ``ObjectIdentifier`` of the object on the opposite side of the attachment
      specified in the query.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesTypeDef",
    {
        "IndexAttachments": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesIndexAttachmentsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponse` `ListAttachedIndices`

    Lists indices attached to an object.

    - **IndexAttachments** *(list) --*

      The indices attached to the specified object.

      - *(dict) --*

        Represents an index and an attached object.

        - **IndexedAttributes** *(list) --*

          The indexed attribute values.

          - *(dict) --*

            The combination of an attribute key and an attribute value.

            - **Key** *(dict) --*

              The key of the attribute.

              - **SchemaArn** *(string) --*

                The Amazon Resource Name (ARN) of the schema that contains the facet and
                attribute.

              - **FacetName** *(string) --*

                The name of the facet that the attribute exists within.

              - **Name** *(string) --*

                The name of the attribute.

            - **Value** *(dict) --*

              The value of the attribute.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

        - **ObjectIdentifier** *(string) --*

          In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to
          the index. In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the
          index attached to the object. This field will always contain the
          ``ObjectIdentifier`` of the object on the opposite side of the attachment
          specified in the query.

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesValueTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesValueTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValues` `Value`

    The value for the typed link.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiers` `IdentityAttributeValues`

    Identifies the attribute name and value for a typed link.

    - **AttributeName** *(string) --*

      The attribute name of the typed link.

    - **Value** *(dict) --*

      The value for the typed link.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersSourceObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersSourceObjectReferenceTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersSourceObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiers` `SourceObjectReference`

    Identifies the source object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links
      leading to it from the directory root. Use the link names from each
      parent/child link to construct the path. Path selectors start with a slash (/)
      and link names are separated by slashes. For more information about paths, see
      `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by
      Amazon Cloud Directory. When creating objects, the system will provide you with
      the identifier of the created object. An object’s identifier is immutable and
      no two objects will ever share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTargetObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTargetObjectReferenceTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTargetObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiers` `TargetObjectReference`

    Identifies the target object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links
      leading to it from the directory root. Use the link names from each
      parent/child link to construct the path. Path selectors start with a slash (/)
      and link names are separated by slashes. For more information about paths, see
      `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by
      Amazon Cloud Directory. When creating objects, the system will provide you with
      the identifier of the created object. An object’s identifier is immutable and
      no two objects will ever share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypedLinkFacetTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypedLinkFacetTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypedLinkFacetTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiers` `TypedLinkFacet`

    Identifies the typed link facet that is associated with the typed link.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) that is associated with the schema. For more
      information, see  arns .

    - **TypedLinkName** *(string) --*

      The unique name of the typed link facet.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypeDef",
    {
        "TypedLinkFacet": ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinks` `LinkSpecifiers`

    Contains all the information that is used to uniquely identify a typed link. The
    parameters discussed in this topic are used to uniquely specify the typed link
    being operated on. The  AttachTypedLink API returns a typed link specifier while
    the  DetachTypedLink API accepts one as input. Similarly, the
    ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed
    link specifiers as output. You can also construct a typed link specifier from
    scratch.

    - **TypedLinkFacet** *(dict) --*

      Identifies the typed link facet that is associated with the typed link.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) that is associated with the schema. For more
        information, see  arns .

      - **TypedLinkName** *(string) --*

        The unique name of the typed link facet.

    - **SourceObjectReference** *(dict) --*

      Identifies the source object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links
        leading to it from the directory root. Use the link names from each
        parent/child link to construct the path. Path selectors start with a slash (/)
        and link names are separated by slashes. For more information about paths, see
        `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by
        Amazon Cloud Directory. When creating objects, the system will provide you with
        the identifier of the created object. An object’s identifier is immutable and
        no two objects will ever share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **TargetObjectReference** *(dict) --*

      Identifies the target object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links
        leading to it from the directory root. Use the link names from each
        parent/child link to construct the path. Path selectors start with a slash (/)
        and link names are separated by slashes. For more information about paths, see
        `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by
        Amazon Cloud Directory. When creating objects, the system will provide you with
        the identifier of the created object. An object’s identifier is immutable and
        no two objects will ever share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **IdentityAttributeValues** *(list) --*

      Identifies the attribute value to update.

      - *(dict) --*

        Identifies the attribute name and value for a typed link.

        - **AttributeName** *(string) --*

          The attribute name of the typed link.

        - **Value** *(dict) --*

          The value for the typed link.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksTypeDef",
    {
        "LinkSpecifiers": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksLinkSpecifiersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponse` `ListIncomingTypedLinks`

    Returns a paginated list of all the incoming  TypedLinkSpecifier information for an
    object. It also supports filtering by typed link facet and identity attributes. For
    more information, see `Typed Links
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
    .

    - **LinkSpecifiers** *(list) --*

      Returns one or more typed link specifiers as output.

      - *(dict) --*

        Contains all the information that is used to uniquely identify a typed link. The
        parameters discussed in this topic are used to uniquely specify the typed link
        being operated on. The  AttachTypedLink API returns a typed link specifier while
        the  DetachTypedLink API accepts one as input. Similarly, the
        ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed
        link specifiers as output. You can also construct a typed link specifier from
        scratch.

        - **TypedLinkFacet** *(dict) --*

          Identifies the typed link facet that is associated with the typed link.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) that is associated with the schema. For more
            information, see  arns .

          - **TypedLinkName** *(string) --*

            The unique name of the typed link facet.

        - **SourceObjectReference** *(dict) --*

          Identifies the source object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links
            leading to it from the directory root. Use the link names from each
            parent/child link to construct the path. Path selectors start with a slash (/)
            and link names are separated by slashes. For more information about paths, see
            `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by
            Amazon Cloud Directory. When creating objects, the system will provide you with
            the identifier of the created object. An object’s identifier is immutable and
            no two objects will ever share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **TargetObjectReference** *(dict) --*

          Identifies the target object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links
            leading to it from the directory root. Use the link names from each
            parent/child link to construct the path. Path selectors start with a slash (/)
            and link names are separated by slashes. For more information about paths, see
            `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by
            Amazon Cloud Directory. When creating objects, the system will provide you with
            the identifier of the created object. An object’s identifier is immutable and
            no two objects will ever share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **IdentityAttributeValues** *(list) --*

          Identifies the attribute value to update.

          - *(dict) --*

            Identifies the attribute name and value for a typed link.

            - **AttributeName** *(string) --*

              The attribute name of the typed link.

            - **Value** *(dict) --*

              The value for the typed link.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesKeyTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesKeyTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesKeyTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributes` `Key`

    The key of the attribute.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) of the schema that contains the facet and
      attribute.

    - **FacetName** *(string) --*

      The name of the facet that the attribute exists within.

    - **Name** *(string) --*

      The name of the attribute.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesValueTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesValueTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesValueTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributes` `Value`

    The value of the attribute.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesTypeDef",
    {
        "Key": ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesKeyTypeDef,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesValueTypeDef,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachments` `IndexedAttributes`

    The combination of an attribute key and an attribute value.

    - **Key** *(dict) --*

      The key of the attribute.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and
        attribute.

      - **FacetName** *(string) --*

        The name of the facet that the attribute exists within.

      - **Name** *(string) --*

        The name of the attribute.

    - **Value** *(dict) --*

      The value of the attribute.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsTypeDef",
    {
        "IndexedAttributes": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsIndexedAttributesTypeDef
        ],
        "ObjectIdentifier": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListIndex` `IndexAttachments`

    Represents an index and an attached object.

    - **IndexedAttributes** *(list) --*

      The indexed attribute values.

      - *(dict) --*

        The combination of an attribute key and an attribute value.

        - **Key** *(dict) --*

          The key of the attribute.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) of the schema that contains the facet and
            attribute.

          - **FacetName** *(string) --*

            The name of the facet that the attribute exists within.

          - **Name** *(string) --*

            The name of the attribute.

        - **Value** *(dict) --*

          The value of the attribute.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.

    - **ObjectIdentifier** *(string) --*

      In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to
      the index. In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the
      index attached to the object. This field will always contain the
      ``ObjectIdentifier`` of the object on the opposite side of the attachment
      specified in the query.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListIndexTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListIndexTypeDef",
    {
        "IndexAttachments": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListIndexIndexAttachmentsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListIndexTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListIndexTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponse` `ListIndex`

    Lists objects attached to the specified index.

    - **IndexAttachments** *(list) --*

      The objects and indexed values attached to the index.

      - *(dict) --*

        Represents an index and an attached object.

        - **IndexedAttributes** *(list) --*

          The indexed attribute values.

          - *(dict) --*

            The combination of an attribute key and an attribute value.

            - **Key** *(dict) --*

              The key of the attribute.

              - **SchemaArn** *(string) --*

                The Amazon Resource Name (ARN) of the schema that contains the facet and
                attribute.

              - **FacetName** *(string) --*

                The name of the facet that the attribute exists within.

              - **Name** *(string) --*

                The name of the attribute.

            - **Value** *(dict) --*

              The value of the attribute.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

        - **ObjectIdentifier** *(string) --*

          In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to
          the index. In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the
          index attached to the object. This field will always contain the
          ``ObjectIdentifier`` of the object on the opposite side of the attachment
          specified in the query.

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesKeyTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesKeyTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesKeyTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributes` `Key`

    The key of the attribute.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) of the schema that contains the facet and
      attribute.

    - **FacetName** *(string) --*

      The name of the facet that the attribute exists within.

    - **Name** *(string) --*

      The name of the attribute.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesValueTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesValueTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesValueTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributes` `Value`

    The value of the attribute.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesTypeDef",
    {
        "Key": ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesKeyTypeDef,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesValueTypeDef,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributes` `Attributes`

    The combination of an attribute key and an attribute value.

    - **Key** *(dict) --*

      The key of the attribute.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and
        attribute.

      - **FacetName** *(string) --*

        The name of the facet that the attribute exists within.

      - **Name** *(string) --*

        The name of the attribute.

    - **Value** *(dict) --*

      The value of the attribute.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesTypeDef",
    {
        "Attributes": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesAttributesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponse` `ListObjectAttributes`

    Lists all attributes that are associated with an object.

    - **Attributes** *(list) --*

      The attributes map that is associated with the object. ``AttributeArn`` is the key;
      attribute value is the value.

      - *(dict) --*

        The combination of an attribute key and an attribute value.

        - **Key** *(dict) --*

          The key of the attribute.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) of the schema that contains the facet and
            attribute.

          - **FacetName** *(string) --*

            The name of the facet that the attribute exists within.

          - **Name** *(string) --*

            The name of the attribute.

        - **Value** *(dict) --*

          The value of the attribute.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectChildrenTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectChildrenTypeDef",
    {"Children": Dict[str, str], "NextToken": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectChildrenTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectChildrenTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponse` `ListObjectChildren`

    Returns a paginated list of child objects that are associated with a given object.

    - **Children** *(dict) --*

      The children structure, which is a map with the key as the ``LinkName`` and
      ``ObjectIdentifier`` as the value.

      - *(string) --*

        - *(string) --*

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsPathToObjectIdentifiersListTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsPathToObjectIdentifiersListTypeDef",
    {"Path": str, "ObjectIdentifiers": List[str]},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsPathToObjectIdentifiersListTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsPathToObjectIdentifiersListTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPaths` `PathToObjectIdentifiersList`

    Returns the path to the ``ObjectIdentifiers`` that is associated with the directory.

    - **Path** *(string) --*

      The path that is used to identify the object starting from directory root.

    - **ObjectIdentifiers** *(list) --*

      Lists ``ObjectIdentifiers`` starting from directory root to the object in the
      request.

      - *(string) --*
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsTypeDef",
    {
        "PathToObjectIdentifiersList": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsPathToObjectIdentifiersListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponse` `ListObjectParentPaths`

    Retrieves all available parent paths for any object type such as node, leaf node,
    policy node, and index node objects. For more information about objects, see `Directory
    Structure
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directorystructure.html>`__
    .

    - **PathToObjectIdentifiersList** *(list) --*

      Returns the path to the ``ObjectIdentifiers`` that are associated with the directory.

      - *(dict) --*

        Returns the path to the ``ObjectIdentifiers`` that is associated with the directory.

        - **Path** *(string) --*

          The path that is used to identify the object starting from directory root.

        - **ObjectIdentifiers** *(list) --*

          Lists ``ObjectIdentifiers`` starting from directory root to the object in the
          request.

          - *(string) --*

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsParentLinksTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsParentLinksTypeDef",
    {"ObjectIdentifier": str, "LinkName": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsParentLinksTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsParentLinksTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListObjectParents` `ParentLinks`

    A pair of ObjectIdentifier and LinkName.

    - **ObjectIdentifier** *(string) --*

      The ID that is associated with the object.

    - **LinkName** *(string) --*

      The name of the link between the parent and the child object.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsTypeDef",
    {
        "ParentLinks": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsParentLinksTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponse` `ListObjectParents`

    - **ParentLinks** *(list) --*

      - *(dict) --*

        A pair of ObjectIdentifier and LinkName.

        - **ObjectIdentifier** *(string) --*

          The ID that is associated with the object.

        - **LinkName** *(string) --*

          The name of the link between the parent and the child object.

    - **NextToken** *(string) --*
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListObjectPoliciesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListObjectPoliciesTypeDef",
    {"AttachedPolicyIds": List[str], "NextToken": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListObjectPoliciesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListObjectPoliciesTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponse` `ListObjectPolicies`

    Returns policies attached to an object in pagination fashion.

    - **AttachedPolicyIds** *(list) --*

      A list of policy ``ObjectIdentifiers`` , that are attached to the object.

      - *(string) --*

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValues` `Value`

    The value for the typed link.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiers` `IdentityAttributeValues`

    Identifies the attribute name and value for a typed link.

    - **AttributeName** *(string) --*

      The attribute name of the typed link.

    - **Value** *(dict) --*

      The value for the typed link.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersSourceObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersSourceObjectReferenceTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersSourceObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiers` `SourceObjectReference`

    Identifies the source object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links
      leading to it from the directory root. Use the link names from each
      parent/child link to construct the path. Path selectors start with a slash (/)
      and link names are separated by slashes. For more information about paths, see
      `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by
      Amazon Cloud Directory. When creating objects, the system will provide you with
      the identifier of the created object. An object’s identifier is immutable and
      no two objects will ever share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTargetObjectReferenceTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTargetObjectReferenceTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTargetObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiers` `TargetObjectReference`

    Identifies the target object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links
      leading to it from the directory root. Use the link names from each
      parent/child link to construct the path. Path selectors start with a slash (/)
      and link names are separated by slashes. For more information about paths, see
      `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by
      Amazon Cloud Directory. When creating objects, the system will provide you with
      the identifier of the created object. An object’s identifier is immutable and
      no two objects will ever share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypedLinkFacetTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypedLinkFacetTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypedLinkFacetTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiers` `TypedLinkFacet`

    Identifies the typed link facet that is associated with the typed link.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) that is associated with the schema. For more
      information, see  arns .

    - **TypedLinkName** *(string) --*

      The unique name of the typed link facet.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypeDef",
    {
        "TypedLinkFacet": ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinks` `TypedLinkSpecifiers`

    Contains all the information that is used to uniquely identify a typed link. The
    parameters discussed in this topic are used to uniquely specify the typed link
    being operated on. The  AttachTypedLink API returns a typed link specifier while
    the  DetachTypedLink API accepts one as input. Similarly, the
    ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed
    link specifiers as output. You can also construct a typed link specifier from
    scratch.

    - **TypedLinkFacet** *(dict) --*

      Identifies the typed link facet that is associated with the typed link.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) that is associated with the schema. For more
        information, see  arns .

      - **TypedLinkName** *(string) --*

        The unique name of the typed link facet.

    - **SourceObjectReference** *(dict) --*

      Identifies the source object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links
        leading to it from the directory root. Use the link names from each
        parent/child link to construct the path. Path selectors start with a slash (/)
        and link names are separated by slashes. For more information about paths, see
        `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by
        Amazon Cloud Directory. When creating objects, the system will provide you with
        the identifier of the created object. An object’s identifier is immutable and
        no two objects will ever share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **TargetObjectReference** *(dict) --*

      Identifies the target object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links
        leading to it from the directory root. Use the link names from each
        parent/child link to construct the path. Path selectors start with a slash (/)
        and link names are separated by slashes. For more information about paths, see
        `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by
        Amazon Cloud Directory. When creating objects, the system will provide you with
        the identifier of the created object. An object’s identifier is immutable and
        no two objects will ever share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **IdentityAttributeValues** *(list) --*

      Identifies the attribute value to update.

      - *(dict) --*

        Identifies the attribute name and value for a typed link.

        - **AttributeName** *(string) --*

          The attribute name of the typed link.

        - **Value** *(dict) --*

          The value for the typed link.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypeDef",
    {
        "TypedLinkSpecifiers": List[
            ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypedLinkSpecifiersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponse` `ListOutgoingTypedLinks`

    Returns a paginated list of all the outgoing  TypedLinkSpecifier information for an
    object. It also supports filtering by typed link facet and identity attributes. For
    more information, see `Typed Links
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
    .

    - **TypedLinkSpecifiers** *(list) --*

      Returns a typed link specifier as output.

      - *(dict) --*

        Contains all the information that is used to uniquely identify a typed link. The
        parameters discussed in this topic are used to uniquely specify the typed link
        being operated on. The  AttachTypedLink API returns a typed link specifier while
        the  DetachTypedLink API accepts one as input. Similarly, the
        ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed
        link specifiers as output. You can also construct a typed link specifier from
        scratch.

        - **TypedLinkFacet** *(dict) --*

          Identifies the typed link facet that is associated with the typed link.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) that is associated with the schema. For more
            information, see  arns .

          - **TypedLinkName** *(string) --*

            The unique name of the typed link facet.

        - **SourceObjectReference** *(dict) --*

          Identifies the source object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links
            leading to it from the directory root. Use the link names from each
            parent/child link to construct the path. Path selectors start with a slash (/)
            and link names are separated by slashes. For more information about paths, see
            `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by
            Amazon Cloud Directory. When creating objects, the system will provide you with
            the identifier of the created object. An object’s identifier is immutable and
            no two objects will ever share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **TargetObjectReference** *(dict) --*

          Identifies the target object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links
            leading to it from the directory root. Use the link names from each
            parent/child link to construct the path. Path selectors start with a slash (/)
            and link names are separated by slashes. For more information about paths, see
            `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by
            Amazon Cloud Directory. When creating objects, the system will provide you with
            the identifier of the created object. An object’s identifier is immutable and
            no two objects will ever share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **IdentityAttributeValues** *(list) --*

          Identifies the attribute value to update.

          - *(dict) --*

            Identifies the attribute name and value for a typed link.

            - **AttributeName** *(string) --*

              The attribute name of the typed link.

            - **Value** *(dict) --*

              The value for the typed link.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseListPolicyAttachmentsTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseListPolicyAttachmentsTypeDef",
    {"ObjectIdentifiers": List[str], "NextToken": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseListPolicyAttachmentsTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseListPolicyAttachmentsTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponse` `ListPolicyAttachments`

    Returns all of the ``ObjectIdentifiers`` to which a given policy is attached.

    - **ObjectIdentifiers** *(list) --*

      A list of ``ObjectIdentifiers`` to which the policy is attached.

      - *(string) --*

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListPoliciesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListPoliciesTypeDef",
    {"PolicyId": str, "ObjectIdentifier": str, "PolicyType": str},
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListPoliciesTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListPoliciesTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathList` `Policies`

    Contains the ``PolicyType`` , ``PolicyId`` , and the ``ObjectIdentifier`` to
    which it is attached. For more information, see `Policies
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
    .

    - **PolicyId** *(string) --*

      The ID of ``PolicyAttachment`` .

    - **ObjectIdentifier** *(string) --*

      The ``ObjectIdentifier`` that is associated with ``PolicyAttachment`` .

    - **PolicyType** *(string) --*

      The type of policy that can be associated with ``PolicyAttachment`` .
    """


_ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListTypeDef",
    {
        "Path": str,
        "Policies": List[
            ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListPoliciesTypeDef
        ],
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicy` `PolicyToPathList`

    Used when a regular object exists in a  Directory and you want to find all of the
    policies that are associated with that object and the parent to that object.

    - **Path** *(string) --*

      The path that is referenced from the root.

    - **Policies** *(list) --*

      List of policy objects.

      - *(dict) --*

        Contains the ``PolicyType`` , ``PolicyId`` , and the ``ObjectIdentifier`` to
        which it is attached. For more information, see `Policies
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
        .

        - **PolicyId** *(string) --*

          The ID of ``PolicyAttachment`` .

        - **ObjectIdentifier** *(string) --*

          The ``ObjectIdentifier`` that is associated with ``PolicyAttachment`` .

        - **PolicyType** *(string) --*

          The type of policy that can be associated with ``PolicyAttachment`` .
    """


_ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyTypeDef",
    {
        "PolicyToPathList": List[
            ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyPolicyToPathListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponsesSuccessfulResponse` `LookupPolicy`

    Lists all policies from the root of the  Directory to the object specified. If there
    are no policies present, an empty list is returned. If policies are present, and if
    some objects don't have the policies attached, it returns the ``ObjectIdentifier`` for
    such objects. If policies are present, it returns ``ObjectIdentifier`` , ``policyId`` ,
    and ``policyType`` . Paths that don't lead to the root from the target object are
    ignored. For more information, see `Policies
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
    .

    - **PolicyToPathList** *(list) --*

      Provides list of path to policies. Policies contain ``PolicyId`` ,
      ``ObjectIdentifier`` , and ``PolicyType`` . For more information, see `Policies
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
      .

      - *(dict) --*

        Used when a regular object exists in a  Directory and you want to find all of the
        policies that are associated with that object and the parent to that object.

        - **Path** *(string) --*

          The path that is referenced from the root.

        - **Policies** *(list) --*

          List of policy objects.

          - *(dict) --*

            Contains the ``PolicyType`` , ``PolicyId`` , and the ``ObjectIdentifier`` to
            which it is attached. For more information, see `Policies
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
            .

            - **PolicyId** *(string) --*

              The ID of ``PolicyAttachment`` .

            - **ObjectIdentifier** *(string) --*

              The ``ObjectIdentifier`` that is associated with ``PolicyAttachment`` .

            - **PolicyType** *(string) --*

              The type of policy that can be associated with ``PolicyAttachment`` .

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientBatchReadResponseResponsesSuccessfulResponseTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesSuccessfulResponseTypeDef",
    {
        "ListObjectAttributes": ClientBatchReadResponseResponsesSuccessfulResponseListObjectAttributesTypeDef,
        "ListObjectChildren": ClientBatchReadResponseResponsesSuccessfulResponseListObjectChildrenTypeDef,
        "GetObjectInformation": ClientBatchReadResponseResponsesSuccessfulResponseGetObjectInformationTypeDef,
        "GetObjectAttributes": ClientBatchReadResponseResponsesSuccessfulResponseGetObjectAttributesTypeDef,
        "ListAttachedIndices": ClientBatchReadResponseResponsesSuccessfulResponseListAttachedIndicesTypeDef,
        "ListObjectParentPaths": ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentPathsTypeDef,
        "ListObjectPolicies": ClientBatchReadResponseResponsesSuccessfulResponseListObjectPoliciesTypeDef,
        "ListPolicyAttachments": ClientBatchReadResponseResponsesSuccessfulResponseListPolicyAttachmentsTypeDef,
        "LookupPolicy": ClientBatchReadResponseResponsesSuccessfulResponseLookupPolicyTypeDef,
        "ListIndex": ClientBatchReadResponseResponsesSuccessfulResponseListIndexTypeDef,
        "ListOutgoingTypedLinks": ClientBatchReadResponseResponsesSuccessfulResponseListOutgoingTypedLinksTypeDef,
        "ListIncomingTypedLinks": ClientBatchReadResponseResponsesSuccessfulResponseListIncomingTypedLinksTypeDef,
        "GetLinkAttributes": ClientBatchReadResponseResponsesSuccessfulResponseGetLinkAttributesTypeDef,
        "ListObjectParents": ClientBatchReadResponseResponsesSuccessfulResponseListObjectParentsTypeDef,
    },
    total=False,
)


class ClientBatchReadResponseResponsesSuccessfulResponseTypeDef(
    _ClientBatchReadResponseResponsesSuccessfulResponseTypeDef
):
    """
    Type definition for `ClientBatchReadResponseResponses` `SuccessfulResponse`

    Identifies which operation in a batch has succeeded.

    - **ListObjectAttributes** *(dict) --*

      Lists all attributes that are associated with an object.

      - **Attributes** *(list) --*

        The attributes map that is associated with the object. ``AttributeArn`` is the key;
        attribute value is the value.

        - *(dict) --*

          The combination of an attribute key and an attribute value.

          - **Key** *(dict) --*

            The key of the attribute.

            - **SchemaArn** *(string) --*

              The Amazon Resource Name (ARN) of the schema that contains the facet and
              attribute.

            - **FacetName** *(string) --*

              The name of the facet that the attribute exists within.

            - **Name** *(string) --*

              The name of the attribute.

          - **Value** *(dict) --*

            The value of the attribute.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.

      - **NextToken** *(string) --*

        The pagination token.

    - **ListObjectChildren** *(dict) --*

      Returns a paginated list of child objects that are associated with a given object.

      - **Children** *(dict) --*

        The children structure, which is a map with the key as the ``LinkName`` and
        ``ObjectIdentifier`` as the value.

        - *(string) --*

          - *(string) --*

      - **NextToken** *(string) --*

        The pagination token.

    - **GetObjectInformation** *(dict) --*

      Retrieves metadata about an object.

      - **SchemaFacets** *(list) --*

        The facets attached to the specified object.

        - *(dict) --*

          A facet.

          - **SchemaArn** *(string) --*

            The ARN of the schema that contains the facet with no minor component. See  arns
            and `In-Place Schema Upgrade
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
            for a description of when to provide minor versions.

          - **FacetName** *(string) --*

            The name of the facet.

      - **ObjectIdentifier** *(string) --*

        The ``ObjectIdentifier`` of the specified object.

    - **GetObjectAttributes** *(dict) --*

      Retrieves attributes within a facet that are associated with an object.

      - **Attributes** *(list) --*

        The attribute values that are associated with an object.

        - *(dict) --*

          The combination of an attribute key and an attribute value.

          - **Key** *(dict) --*

            The key of the attribute.

            - **SchemaArn** *(string) --*

              The Amazon Resource Name (ARN) of the schema that contains the facet and
              attribute.

            - **FacetName** *(string) --*

              The name of the facet that the attribute exists within.

            - **Name** *(string) --*

              The name of the attribute.

          - **Value** *(dict) --*

            The value of the attribute.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.

    - **ListAttachedIndices** *(dict) --*

      Lists indices attached to an object.

      - **IndexAttachments** *(list) --*

        The indices attached to the specified object.

        - *(dict) --*

          Represents an index and an attached object.

          - **IndexedAttributes** *(list) --*

            The indexed attribute values.

            - *(dict) --*

              The combination of an attribute key and an attribute value.

              - **Key** *(dict) --*

                The key of the attribute.

                - **SchemaArn** *(string) --*

                  The Amazon Resource Name (ARN) of the schema that contains the facet and
                  attribute.

                - **FacetName** *(string) --*

                  The name of the facet that the attribute exists within.

                - **Name** *(string) --*

                  The name of the attribute.

              - **Value** *(dict) --*

                The value of the attribute.

                - **StringValue** *(string) --*

                  A string data value.

                - **BinaryValue** *(bytes) --*

                  A binary data value.

                - **BooleanValue** *(boolean) --*

                  A Boolean data value.

                - **NumberValue** *(string) --*

                  A number data value.

                - **DatetimeValue** *(datetime) --*

                  A date and time value.

          - **ObjectIdentifier** *(string) --*

            In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to
            the index. In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the
            index attached to the object. This field will always contain the
            ``ObjectIdentifier`` of the object on the opposite side of the attachment
            specified in the query.

      - **NextToken** *(string) --*

        The pagination token.

    - **ListObjectParentPaths** *(dict) --*

      Retrieves all available parent paths for any object type such as node, leaf node,
      policy node, and index node objects. For more information about objects, see `Directory
      Structure
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directorystructure.html>`__
      .

      - **PathToObjectIdentifiersList** *(list) --*

        Returns the path to the ``ObjectIdentifiers`` that are associated with the directory.

        - *(dict) --*

          Returns the path to the ``ObjectIdentifiers`` that is associated with the directory.

          - **Path** *(string) --*

            The path that is used to identify the object starting from directory root.

          - **ObjectIdentifiers** *(list) --*

            Lists ``ObjectIdentifiers`` starting from directory root to the object in the
            request.

            - *(string) --*

      - **NextToken** *(string) --*

        The pagination token.

    - **ListObjectPolicies** *(dict) --*

      Returns policies attached to an object in pagination fashion.

      - **AttachedPolicyIds** *(list) --*

        A list of policy ``ObjectIdentifiers`` , that are attached to the object.

        - *(string) --*

      - **NextToken** *(string) --*

        The pagination token.

    - **ListPolicyAttachments** *(dict) --*

      Returns all of the ``ObjectIdentifiers`` to which a given policy is attached.

      - **ObjectIdentifiers** *(list) --*

        A list of ``ObjectIdentifiers`` to which the policy is attached.

        - *(string) --*

      - **NextToken** *(string) --*

        The pagination token.

    - **LookupPolicy** *(dict) --*

      Lists all policies from the root of the  Directory to the object specified. If there
      are no policies present, an empty list is returned. If policies are present, and if
      some objects don't have the policies attached, it returns the ``ObjectIdentifier`` for
      such objects. If policies are present, it returns ``ObjectIdentifier`` , ``policyId`` ,
      and ``policyType`` . Paths that don't lead to the root from the target object are
      ignored. For more information, see `Policies
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
      .

      - **PolicyToPathList** *(list) --*

        Provides list of path to policies. Policies contain ``PolicyId`` ,
        ``ObjectIdentifier`` , and ``PolicyType`` . For more information, see `Policies
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
        .

        - *(dict) --*

          Used when a regular object exists in a  Directory and you want to find all of the
          policies that are associated with that object and the parent to that object.

          - **Path** *(string) --*

            The path that is referenced from the root.

          - **Policies** *(list) --*

            List of policy objects.

            - *(dict) --*

              Contains the ``PolicyType`` , ``PolicyId`` , and the ``ObjectIdentifier`` to
              which it is attached. For more information, see `Policies
              <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
              .

              - **PolicyId** *(string) --*

                The ID of ``PolicyAttachment`` .

              - **ObjectIdentifier** *(string) --*

                The ``ObjectIdentifier`` that is associated with ``PolicyAttachment`` .

              - **PolicyType** *(string) --*

                The type of policy that can be associated with ``PolicyAttachment`` .

      - **NextToken** *(string) --*

        The pagination token.

    - **ListIndex** *(dict) --*

      Lists objects attached to the specified index.

      - **IndexAttachments** *(list) --*

        The objects and indexed values attached to the index.

        - *(dict) --*

          Represents an index and an attached object.

          - **IndexedAttributes** *(list) --*

            The indexed attribute values.

            - *(dict) --*

              The combination of an attribute key and an attribute value.

              - **Key** *(dict) --*

                The key of the attribute.

                - **SchemaArn** *(string) --*

                  The Amazon Resource Name (ARN) of the schema that contains the facet and
                  attribute.

                - **FacetName** *(string) --*

                  The name of the facet that the attribute exists within.

                - **Name** *(string) --*

                  The name of the attribute.

              - **Value** *(dict) --*

                The value of the attribute.

                - **StringValue** *(string) --*

                  A string data value.

                - **BinaryValue** *(bytes) --*

                  A binary data value.

                - **BooleanValue** *(boolean) --*

                  A Boolean data value.

                - **NumberValue** *(string) --*

                  A number data value.

                - **DatetimeValue** *(datetime) --*

                  A date and time value.

          - **ObjectIdentifier** *(string) --*

            In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to
            the index. In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the
            index attached to the object. This field will always contain the
            ``ObjectIdentifier`` of the object on the opposite side of the attachment
            specified in the query.

      - **NextToken** *(string) --*

        The pagination token.

    - **ListOutgoingTypedLinks** *(dict) --*

      Returns a paginated list of all the outgoing  TypedLinkSpecifier information for an
      object. It also supports filtering by typed link facet and identity attributes. For
      more information, see `Typed Links
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
      .

      - **TypedLinkSpecifiers** *(list) --*

        Returns a typed link specifier as output.

        - *(dict) --*

          Contains all the information that is used to uniquely identify a typed link. The
          parameters discussed in this topic are used to uniquely specify the typed link
          being operated on. The  AttachTypedLink API returns a typed link specifier while
          the  DetachTypedLink API accepts one as input. Similarly, the
          ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed
          link specifiers as output. You can also construct a typed link specifier from
          scratch.

          - **TypedLinkFacet** *(dict) --*

            Identifies the typed link facet that is associated with the typed link.

            - **SchemaArn** *(string) --*

              The Amazon Resource Name (ARN) that is associated with the schema. For more
              information, see  arns .

            - **TypedLinkName** *(string) --*

              The unique name of the typed link facet.

          - **SourceObjectReference** *(dict) --*

            Identifies the source object that the typed link will attach to.

            - **Selector** *(string) --*

              A path selector supports easy selection of an object by the parent/child links
              leading to it from the directory root. Use the link names from each
              parent/child link to construct the path. Path selectors start with a slash (/)
              and link names are separated by slashes. For more information about paths, see
              `Access Objects
              <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
              . You can identify an object in one of the following ways:

              * *$ObjectIdentifier* - An object identifier is an opaque string provided by
              Amazon Cloud Directory. When creating objects, the system will provide you with
              the identifier of the created object. An object’s identifier is immutable and
              no two objects will ever share the same object identifier

              * */some/path* - Identifies the object based on path

              * *#SomeBatchReference* - Identifies the object in a batch call

          - **TargetObjectReference** *(dict) --*

            Identifies the target object that the typed link will attach to.

            - **Selector** *(string) --*

              A path selector supports easy selection of an object by the parent/child links
              leading to it from the directory root. Use the link names from each
              parent/child link to construct the path. Path selectors start with a slash (/)
              and link names are separated by slashes. For more information about paths, see
              `Access Objects
              <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
              . You can identify an object in one of the following ways:

              * *$ObjectIdentifier* - An object identifier is an opaque string provided by
              Amazon Cloud Directory. When creating objects, the system will provide you with
              the identifier of the created object. An object’s identifier is immutable and
              no two objects will ever share the same object identifier

              * */some/path* - Identifies the object based on path

              * *#SomeBatchReference* - Identifies the object in a batch call

          - **IdentityAttributeValues** *(list) --*

            Identifies the attribute value to update.

            - *(dict) --*

              Identifies the attribute name and value for a typed link.

              - **AttributeName** *(string) --*

                The attribute name of the typed link.

              - **Value** *(dict) --*

                The value for the typed link.

                - **StringValue** *(string) --*

                  A string data value.

                - **BinaryValue** *(bytes) --*

                  A binary data value.

                - **BooleanValue** *(boolean) --*

                  A Boolean data value.

                - **NumberValue** *(string) --*

                  A number data value.

                - **DatetimeValue** *(datetime) --*

                  A date and time value.

      - **NextToken** *(string) --*

        The pagination token.

    - **ListIncomingTypedLinks** *(dict) --*

      Returns a paginated list of all the incoming  TypedLinkSpecifier information for an
      object. It also supports filtering by typed link facet and identity attributes. For
      more information, see `Typed Links
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
      .

      - **LinkSpecifiers** *(list) --*

        Returns one or more typed link specifiers as output.

        - *(dict) --*

          Contains all the information that is used to uniquely identify a typed link. The
          parameters discussed in this topic are used to uniquely specify the typed link
          being operated on. The  AttachTypedLink API returns a typed link specifier while
          the  DetachTypedLink API accepts one as input. Similarly, the
          ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed
          link specifiers as output. You can also construct a typed link specifier from
          scratch.

          - **TypedLinkFacet** *(dict) --*

            Identifies the typed link facet that is associated with the typed link.

            - **SchemaArn** *(string) --*

              The Amazon Resource Name (ARN) that is associated with the schema. For more
              information, see  arns .

            - **TypedLinkName** *(string) --*

              The unique name of the typed link facet.

          - **SourceObjectReference** *(dict) --*

            Identifies the source object that the typed link will attach to.

            - **Selector** *(string) --*

              A path selector supports easy selection of an object by the parent/child links
              leading to it from the directory root. Use the link names from each
              parent/child link to construct the path. Path selectors start with a slash (/)
              and link names are separated by slashes. For more information about paths, see
              `Access Objects
              <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
              . You can identify an object in one of the following ways:

              * *$ObjectIdentifier* - An object identifier is an opaque string provided by
              Amazon Cloud Directory. When creating objects, the system will provide you with
              the identifier of the created object. An object’s identifier is immutable and
              no two objects will ever share the same object identifier

              * */some/path* - Identifies the object based on path

              * *#SomeBatchReference* - Identifies the object in a batch call

          - **TargetObjectReference** *(dict) --*

            Identifies the target object that the typed link will attach to.

            - **Selector** *(string) --*

              A path selector supports easy selection of an object by the parent/child links
              leading to it from the directory root. Use the link names from each
              parent/child link to construct the path. Path selectors start with a slash (/)
              and link names are separated by slashes. For more information about paths, see
              `Access Objects
              <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
              . You can identify an object in one of the following ways:

              * *$ObjectIdentifier* - An object identifier is an opaque string provided by
              Amazon Cloud Directory. When creating objects, the system will provide you with
              the identifier of the created object. An object’s identifier is immutable and
              no two objects will ever share the same object identifier

              * */some/path* - Identifies the object based on path

              * *#SomeBatchReference* - Identifies the object in a batch call

          - **IdentityAttributeValues** *(list) --*

            Identifies the attribute value to update.

            - *(dict) --*

              Identifies the attribute name and value for a typed link.

              - **AttributeName** *(string) --*

                The attribute name of the typed link.

              - **Value** *(dict) --*

                The value for the typed link.

                - **StringValue** *(string) --*

                  A string data value.

                - **BinaryValue** *(bytes) --*

                  A binary data value.

                - **BooleanValue** *(boolean) --*

                  A Boolean data value.

                - **NumberValue** *(string) --*

                  A number data value.

                - **DatetimeValue** *(datetime) --*

                  A date and time value.

      - **NextToken** *(string) --*

        The pagination token.

    - **GetLinkAttributes** *(dict) --*

      The list of attributes to retrieve from the typed link.

      - **Attributes** *(list) --*

        The attributes that are associated with the typed link.

        - *(dict) --*

          The combination of an attribute key and an attribute value.

          - **Key** *(dict) --*

            The key of the attribute.

            - **SchemaArn** *(string) --*

              The Amazon Resource Name (ARN) of the schema that contains the facet and
              attribute.

            - **FacetName** *(string) --*

              The name of the facet that the attribute exists within.

            - **Name** *(string) --*

              The name of the attribute.

          - **Value** *(dict) --*

            The value of the attribute.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.

    - **ListObjectParents** *(dict) --*

      - **ParentLinks** *(list) --*

        - *(dict) --*

          A pair of ObjectIdentifier and LinkName.

          - **ObjectIdentifier** *(string) --*

            The ID that is associated with the object.

          - **LinkName** *(string) --*

            The name of the link between the parent and the child object.

      - **NextToken** *(string) --*
    """


_ClientBatchReadResponseResponsesTypeDef = TypedDict(
    "_ClientBatchReadResponseResponsesTypeDef",
    {
        "SuccessfulResponse": ClientBatchReadResponseResponsesSuccessfulResponseTypeDef,
        "ExceptionResponse": ClientBatchReadResponseResponsesExceptionResponseTypeDef,
    },
    total=False,
)


class ClientBatchReadResponseResponsesTypeDef(_ClientBatchReadResponseResponsesTypeDef):
    """
    Type definition for `ClientBatchReadResponse` `Responses`

    Represents the output of a ``BatchRead`` response operation.

    - **SuccessfulResponse** *(dict) --*

      Identifies which operation in a batch has succeeded.

      - **ListObjectAttributes** *(dict) --*

        Lists all attributes that are associated with an object.

        - **Attributes** *(list) --*

          The attributes map that is associated with the object. ``AttributeArn`` is the key;
          attribute value is the value.

          - *(dict) --*

            The combination of an attribute key and an attribute value.

            - **Key** *(dict) --*

              The key of the attribute.

              - **SchemaArn** *(string) --*

                The Amazon Resource Name (ARN) of the schema that contains the facet and
                attribute.

              - **FacetName** *(string) --*

                The name of the facet that the attribute exists within.

              - **Name** *(string) --*

                The name of the attribute.

            - **Value** *(dict) --*

              The value of the attribute.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

        - **NextToken** *(string) --*

          The pagination token.

      - **ListObjectChildren** *(dict) --*

        Returns a paginated list of child objects that are associated with a given object.

        - **Children** *(dict) --*

          The children structure, which is a map with the key as the ``LinkName`` and
          ``ObjectIdentifier`` as the value.

          - *(string) --*

            - *(string) --*

        - **NextToken** *(string) --*

          The pagination token.

      - **GetObjectInformation** *(dict) --*

        Retrieves metadata about an object.

        - **SchemaFacets** *(list) --*

          The facets attached to the specified object.

          - *(dict) --*

            A facet.

            - **SchemaArn** *(string) --*

              The ARN of the schema that contains the facet with no minor component. See  arns
              and `In-Place Schema Upgrade
              <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
              for a description of when to provide minor versions.

            - **FacetName** *(string) --*

              The name of the facet.

        - **ObjectIdentifier** *(string) --*

          The ``ObjectIdentifier`` of the specified object.

      - **GetObjectAttributes** *(dict) --*

        Retrieves attributes within a facet that are associated with an object.

        - **Attributes** *(list) --*

          The attribute values that are associated with an object.

          - *(dict) --*

            The combination of an attribute key and an attribute value.

            - **Key** *(dict) --*

              The key of the attribute.

              - **SchemaArn** *(string) --*

                The Amazon Resource Name (ARN) of the schema that contains the facet and
                attribute.

              - **FacetName** *(string) --*

                The name of the facet that the attribute exists within.

              - **Name** *(string) --*

                The name of the attribute.

            - **Value** *(dict) --*

              The value of the attribute.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

      - **ListAttachedIndices** *(dict) --*

        Lists indices attached to an object.

        - **IndexAttachments** *(list) --*

          The indices attached to the specified object.

          - *(dict) --*

            Represents an index and an attached object.

            - **IndexedAttributes** *(list) --*

              The indexed attribute values.

              - *(dict) --*

                The combination of an attribute key and an attribute value.

                - **Key** *(dict) --*

                  The key of the attribute.

                  - **SchemaArn** *(string) --*

                    The Amazon Resource Name (ARN) of the schema that contains the facet and
                    attribute.

                  - **FacetName** *(string) --*

                    The name of the facet that the attribute exists within.

                  - **Name** *(string) --*

                    The name of the attribute.

                - **Value** *(dict) --*

                  The value of the attribute.

                  - **StringValue** *(string) --*

                    A string data value.

                  - **BinaryValue** *(bytes) --*

                    A binary data value.

                  - **BooleanValue** *(boolean) --*

                    A Boolean data value.

                  - **NumberValue** *(string) --*

                    A number data value.

                  - **DatetimeValue** *(datetime) --*

                    A date and time value.

            - **ObjectIdentifier** *(string) --*

              In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to
              the index. In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the
              index attached to the object. This field will always contain the
              ``ObjectIdentifier`` of the object on the opposite side of the attachment
              specified in the query.

        - **NextToken** *(string) --*

          The pagination token.

      - **ListObjectParentPaths** *(dict) --*

        Retrieves all available parent paths for any object type such as node, leaf node,
        policy node, and index node objects. For more information about objects, see `Directory
        Structure
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directorystructure.html>`__
        .

        - **PathToObjectIdentifiersList** *(list) --*

          Returns the path to the ``ObjectIdentifiers`` that are associated with the directory.

          - *(dict) --*

            Returns the path to the ``ObjectIdentifiers`` that is associated with the directory.

            - **Path** *(string) --*

              The path that is used to identify the object starting from directory root.

            - **ObjectIdentifiers** *(list) --*

              Lists ``ObjectIdentifiers`` starting from directory root to the object in the
              request.

              - *(string) --*

        - **NextToken** *(string) --*

          The pagination token.

      - **ListObjectPolicies** *(dict) --*

        Returns policies attached to an object in pagination fashion.

        - **AttachedPolicyIds** *(list) --*

          A list of policy ``ObjectIdentifiers`` , that are attached to the object.

          - *(string) --*

        - **NextToken** *(string) --*

          The pagination token.

      - **ListPolicyAttachments** *(dict) --*

        Returns all of the ``ObjectIdentifiers`` to which a given policy is attached.

        - **ObjectIdentifiers** *(list) --*

          A list of ``ObjectIdentifiers`` to which the policy is attached.

          - *(string) --*

        - **NextToken** *(string) --*

          The pagination token.

      - **LookupPolicy** *(dict) --*

        Lists all policies from the root of the  Directory to the object specified. If there
        are no policies present, an empty list is returned. If policies are present, and if
        some objects don't have the policies attached, it returns the ``ObjectIdentifier`` for
        such objects. If policies are present, it returns ``ObjectIdentifier`` , ``policyId`` ,
        and ``policyType`` . Paths that don't lead to the root from the target object are
        ignored. For more information, see `Policies
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
        .

        - **PolicyToPathList** *(list) --*

          Provides list of path to policies. Policies contain ``PolicyId`` ,
          ``ObjectIdentifier`` , and ``PolicyType`` . For more information, see `Policies
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
          .

          - *(dict) --*

            Used when a regular object exists in a  Directory and you want to find all of the
            policies that are associated with that object and the parent to that object.

            - **Path** *(string) --*

              The path that is referenced from the root.

            - **Policies** *(list) --*

              List of policy objects.

              - *(dict) --*

                Contains the ``PolicyType`` , ``PolicyId`` , and the ``ObjectIdentifier`` to
                which it is attached. For more information, see `Policies
                <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
                .

                - **PolicyId** *(string) --*

                  The ID of ``PolicyAttachment`` .

                - **ObjectIdentifier** *(string) --*

                  The ``ObjectIdentifier`` that is associated with ``PolicyAttachment`` .

                - **PolicyType** *(string) --*

                  The type of policy that can be associated with ``PolicyAttachment`` .

        - **NextToken** *(string) --*

          The pagination token.

      - **ListIndex** *(dict) --*

        Lists objects attached to the specified index.

        - **IndexAttachments** *(list) --*

          The objects and indexed values attached to the index.

          - *(dict) --*

            Represents an index and an attached object.

            - **IndexedAttributes** *(list) --*

              The indexed attribute values.

              - *(dict) --*

                The combination of an attribute key and an attribute value.

                - **Key** *(dict) --*

                  The key of the attribute.

                  - **SchemaArn** *(string) --*

                    The Amazon Resource Name (ARN) of the schema that contains the facet and
                    attribute.

                  - **FacetName** *(string) --*

                    The name of the facet that the attribute exists within.

                  - **Name** *(string) --*

                    The name of the attribute.

                - **Value** *(dict) --*

                  The value of the attribute.

                  - **StringValue** *(string) --*

                    A string data value.

                  - **BinaryValue** *(bytes) --*

                    A binary data value.

                  - **BooleanValue** *(boolean) --*

                    A Boolean data value.

                  - **NumberValue** *(string) --*

                    A number data value.

                  - **DatetimeValue** *(datetime) --*

                    A date and time value.

            - **ObjectIdentifier** *(string) --*

              In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to
              the index. In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the
              index attached to the object. This field will always contain the
              ``ObjectIdentifier`` of the object on the opposite side of the attachment
              specified in the query.

        - **NextToken** *(string) --*

          The pagination token.

      - **ListOutgoingTypedLinks** *(dict) --*

        Returns a paginated list of all the outgoing  TypedLinkSpecifier information for an
        object. It also supports filtering by typed link facet and identity attributes. For
        more information, see `Typed Links
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
        .

        - **TypedLinkSpecifiers** *(list) --*

          Returns a typed link specifier as output.

          - *(dict) --*

            Contains all the information that is used to uniquely identify a typed link. The
            parameters discussed in this topic are used to uniquely specify the typed link
            being operated on. The  AttachTypedLink API returns a typed link specifier while
            the  DetachTypedLink API accepts one as input. Similarly, the
            ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed
            link specifiers as output. You can also construct a typed link specifier from
            scratch.

            - **TypedLinkFacet** *(dict) --*

              Identifies the typed link facet that is associated with the typed link.

              - **SchemaArn** *(string) --*

                The Amazon Resource Name (ARN) that is associated with the schema. For more
                information, see  arns .

              - **TypedLinkName** *(string) --*

                The unique name of the typed link facet.

            - **SourceObjectReference** *(dict) --*

              Identifies the source object that the typed link will attach to.

              - **Selector** *(string) --*

                A path selector supports easy selection of an object by the parent/child links
                leading to it from the directory root. Use the link names from each
                parent/child link to construct the path. Path selectors start with a slash (/)
                and link names are separated by slashes. For more information about paths, see
                `Access Objects
                <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
                . You can identify an object in one of the following ways:

                * *$ObjectIdentifier* - An object identifier is an opaque string provided by
                Amazon Cloud Directory. When creating objects, the system will provide you with
                the identifier of the created object. An object’s identifier is immutable and
                no two objects will ever share the same object identifier

                * */some/path* - Identifies the object based on path

                * *#SomeBatchReference* - Identifies the object in a batch call

            - **TargetObjectReference** *(dict) --*

              Identifies the target object that the typed link will attach to.

              - **Selector** *(string) --*

                A path selector supports easy selection of an object by the parent/child links
                leading to it from the directory root. Use the link names from each
                parent/child link to construct the path. Path selectors start with a slash (/)
                and link names are separated by slashes. For more information about paths, see
                `Access Objects
                <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
                . You can identify an object in one of the following ways:

                * *$ObjectIdentifier* - An object identifier is an opaque string provided by
                Amazon Cloud Directory. When creating objects, the system will provide you with
                the identifier of the created object. An object’s identifier is immutable and
                no two objects will ever share the same object identifier

                * */some/path* - Identifies the object based on path

                * *#SomeBatchReference* - Identifies the object in a batch call

            - **IdentityAttributeValues** *(list) --*

              Identifies the attribute value to update.

              - *(dict) --*

                Identifies the attribute name and value for a typed link.

                - **AttributeName** *(string) --*

                  The attribute name of the typed link.

                - **Value** *(dict) --*

                  The value for the typed link.

                  - **StringValue** *(string) --*

                    A string data value.

                  - **BinaryValue** *(bytes) --*

                    A binary data value.

                  - **BooleanValue** *(boolean) --*

                    A Boolean data value.

                  - **NumberValue** *(string) --*

                    A number data value.

                  - **DatetimeValue** *(datetime) --*

                    A date and time value.

        - **NextToken** *(string) --*

          The pagination token.

      - **ListIncomingTypedLinks** *(dict) --*

        Returns a paginated list of all the incoming  TypedLinkSpecifier information for an
        object. It also supports filtering by typed link facet and identity attributes. For
        more information, see `Typed Links
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
        .

        - **LinkSpecifiers** *(list) --*

          Returns one or more typed link specifiers as output.

          - *(dict) --*

            Contains all the information that is used to uniquely identify a typed link. The
            parameters discussed in this topic are used to uniquely specify the typed link
            being operated on. The  AttachTypedLink API returns a typed link specifier while
            the  DetachTypedLink API accepts one as input. Similarly, the
            ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed
            link specifiers as output. You can also construct a typed link specifier from
            scratch.

            - **TypedLinkFacet** *(dict) --*

              Identifies the typed link facet that is associated with the typed link.

              - **SchemaArn** *(string) --*

                The Amazon Resource Name (ARN) that is associated with the schema. For more
                information, see  arns .

              - **TypedLinkName** *(string) --*

                The unique name of the typed link facet.

            - **SourceObjectReference** *(dict) --*

              Identifies the source object that the typed link will attach to.

              - **Selector** *(string) --*

                A path selector supports easy selection of an object by the parent/child links
                leading to it from the directory root. Use the link names from each
                parent/child link to construct the path. Path selectors start with a slash (/)
                and link names are separated by slashes. For more information about paths, see
                `Access Objects
                <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
                . You can identify an object in one of the following ways:

                * *$ObjectIdentifier* - An object identifier is an opaque string provided by
                Amazon Cloud Directory. When creating objects, the system will provide you with
                the identifier of the created object. An object’s identifier is immutable and
                no two objects will ever share the same object identifier

                * */some/path* - Identifies the object based on path

                * *#SomeBatchReference* - Identifies the object in a batch call

            - **TargetObjectReference** *(dict) --*

              Identifies the target object that the typed link will attach to.

              - **Selector** *(string) --*

                A path selector supports easy selection of an object by the parent/child links
                leading to it from the directory root. Use the link names from each
                parent/child link to construct the path. Path selectors start with a slash (/)
                and link names are separated by slashes. For more information about paths, see
                `Access Objects
                <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
                . You can identify an object in one of the following ways:

                * *$ObjectIdentifier* - An object identifier is an opaque string provided by
                Amazon Cloud Directory. When creating objects, the system will provide you with
                the identifier of the created object. An object’s identifier is immutable and
                no two objects will ever share the same object identifier

                * */some/path* - Identifies the object based on path

                * *#SomeBatchReference* - Identifies the object in a batch call

            - **IdentityAttributeValues** *(list) --*

              Identifies the attribute value to update.

              - *(dict) --*

                Identifies the attribute name and value for a typed link.

                - **AttributeName** *(string) --*

                  The attribute name of the typed link.

                - **Value** *(dict) --*

                  The value for the typed link.

                  - **StringValue** *(string) --*

                    A string data value.

                  - **BinaryValue** *(bytes) --*

                    A binary data value.

                  - **BooleanValue** *(boolean) --*

                    A Boolean data value.

                  - **NumberValue** *(string) --*

                    A number data value.

                  - **DatetimeValue** *(datetime) --*

                    A date and time value.

        - **NextToken** *(string) --*

          The pagination token.

      - **GetLinkAttributes** *(dict) --*

        The list of attributes to retrieve from the typed link.

        - **Attributes** *(list) --*

          The attributes that are associated with the typed link.

          - *(dict) --*

            The combination of an attribute key and an attribute value.

            - **Key** *(dict) --*

              The key of the attribute.

              - **SchemaArn** *(string) --*

                The Amazon Resource Name (ARN) of the schema that contains the facet and
                attribute.

              - **FacetName** *(string) --*

                The name of the facet that the attribute exists within.

              - **Name** *(string) --*

                The name of the attribute.

            - **Value** *(dict) --*

              The value of the attribute.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

      - **ListObjectParents** *(dict) --*

        - **ParentLinks** *(list) --*

          - *(dict) --*

            A pair of ObjectIdentifier and LinkName.

            - **ObjectIdentifier** *(string) --*

              The ID that is associated with the object.

            - **LinkName** *(string) --*

              The name of the link between the parent and the child object.

        - **NextToken** *(string) --*

    - **ExceptionResponse** *(dict) --*

      Identifies which operation in a batch has failed.

      - **Type** *(string) --*

        A type of exception, such as ``InvalidArnException`` .

      - **Message** *(string) --*

        An exception message that is associated with the failure.
    """


_ClientBatchReadResponseTypeDef = TypedDict(
    "_ClientBatchReadResponseTypeDef",
    {"Responses": List[ClientBatchReadResponseResponsesTypeDef]},
    total=False,
)


class ClientBatchReadResponseTypeDef(_ClientBatchReadResponseTypeDef):
    """
    Type definition for `ClientBatchRead` `Response`

    - **Responses** *(list) --*

      A list of all the responses for each batch read.

      - *(dict) --*

        Represents the output of a ``BatchRead`` response operation.

        - **SuccessfulResponse** *(dict) --*

          Identifies which operation in a batch has succeeded.

          - **ListObjectAttributes** *(dict) --*

            Lists all attributes that are associated with an object.

            - **Attributes** *(list) --*

              The attributes map that is associated with the object. ``AttributeArn`` is the key;
              attribute value is the value.

              - *(dict) --*

                The combination of an attribute key and an attribute value.

                - **Key** *(dict) --*

                  The key of the attribute.

                  - **SchemaArn** *(string) --*

                    The Amazon Resource Name (ARN) of the schema that contains the facet and
                    attribute.

                  - **FacetName** *(string) --*

                    The name of the facet that the attribute exists within.

                  - **Name** *(string) --*

                    The name of the attribute.

                - **Value** *(dict) --*

                  The value of the attribute.

                  - **StringValue** *(string) --*

                    A string data value.

                  - **BinaryValue** *(bytes) --*

                    A binary data value.

                  - **BooleanValue** *(boolean) --*

                    A Boolean data value.

                  - **NumberValue** *(string) --*

                    A number data value.

                  - **DatetimeValue** *(datetime) --*

                    A date and time value.

            - **NextToken** *(string) --*

              The pagination token.

          - **ListObjectChildren** *(dict) --*

            Returns a paginated list of child objects that are associated with a given object.

            - **Children** *(dict) --*

              The children structure, which is a map with the key as the ``LinkName`` and
              ``ObjectIdentifier`` as the value.

              - *(string) --*

                - *(string) --*

            - **NextToken** *(string) --*

              The pagination token.

          - **GetObjectInformation** *(dict) --*

            Retrieves metadata about an object.

            - **SchemaFacets** *(list) --*

              The facets attached to the specified object.

              - *(dict) --*

                A facet.

                - **SchemaArn** *(string) --*

                  The ARN of the schema that contains the facet with no minor component. See  arns
                  and `In-Place Schema Upgrade
                  <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
                  for a description of when to provide minor versions.

                - **FacetName** *(string) --*

                  The name of the facet.

            - **ObjectIdentifier** *(string) --*

              The ``ObjectIdentifier`` of the specified object.

          - **GetObjectAttributes** *(dict) --*

            Retrieves attributes within a facet that are associated with an object.

            - **Attributes** *(list) --*

              The attribute values that are associated with an object.

              - *(dict) --*

                The combination of an attribute key and an attribute value.

                - **Key** *(dict) --*

                  The key of the attribute.

                  - **SchemaArn** *(string) --*

                    The Amazon Resource Name (ARN) of the schema that contains the facet and
                    attribute.

                  - **FacetName** *(string) --*

                    The name of the facet that the attribute exists within.

                  - **Name** *(string) --*

                    The name of the attribute.

                - **Value** *(dict) --*

                  The value of the attribute.

                  - **StringValue** *(string) --*

                    A string data value.

                  - **BinaryValue** *(bytes) --*

                    A binary data value.

                  - **BooleanValue** *(boolean) --*

                    A Boolean data value.

                  - **NumberValue** *(string) --*

                    A number data value.

                  - **DatetimeValue** *(datetime) --*

                    A date and time value.

          - **ListAttachedIndices** *(dict) --*

            Lists indices attached to an object.

            - **IndexAttachments** *(list) --*

              The indices attached to the specified object.

              - *(dict) --*

                Represents an index and an attached object.

                - **IndexedAttributes** *(list) --*

                  The indexed attribute values.

                  - *(dict) --*

                    The combination of an attribute key and an attribute value.

                    - **Key** *(dict) --*

                      The key of the attribute.

                      - **SchemaArn** *(string) --*

                        The Amazon Resource Name (ARN) of the schema that contains the facet and
                        attribute.

                      - **FacetName** *(string) --*

                        The name of the facet that the attribute exists within.

                      - **Name** *(string) --*

                        The name of the attribute.

                    - **Value** *(dict) --*

                      The value of the attribute.

                      - **StringValue** *(string) --*

                        A string data value.

                      - **BinaryValue** *(bytes) --*

                        A binary data value.

                      - **BooleanValue** *(boolean) --*

                        A Boolean data value.

                      - **NumberValue** *(string) --*

                        A number data value.

                      - **DatetimeValue** *(datetime) --*

                        A date and time value.

                - **ObjectIdentifier** *(string) --*

                  In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to
                  the index. In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the
                  index attached to the object. This field will always contain the
                  ``ObjectIdentifier`` of the object on the opposite side of the attachment
                  specified in the query.

            - **NextToken** *(string) --*

              The pagination token.

          - **ListObjectParentPaths** *(dict) --*

            Retrieves all available parent paths for any object type such as node, leaf node,
            policy node, and index node objects. For more information about objects, see `Directory
            Structure
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directorystructure.html>`__
            .

            - **PathToObjectIdentifiersList** *(list) --*

              Returns the path to the ``ObjectIdentifiers`` that are associated with the directory.

              - *(dict) --*

                Returns the path to the ``ObjectIdentifiers`` that is associated with the directory.

                - **Path** *(string) --*

                  The path that is used to identify the object starting from directory root.

                - **ObjectIdentifiers** *(list) --*

                  Lists ``ObjectIdentifiers`` starting from directory root to the object in the
                  request.

                  - *(string) --*

            - **NextToken** *(string) --*

              The pagination token.

          - **ListObjectPolicies** *(dict) --*

            Returns policies attached to an object in pagination fashion.

            - **AttachedPolicyIds** *(list) --*

              A list of policy ``ObjectIdentifiers`` , that are attached to the object.

              - *(string) --*

            - **NextToken** *(string) --*

              The pagination token.

          - **ListPolicyAttachments** *(dict) --*

            Returns all of the ``ObjectIdentifiers`` to which a given policy is attached.

            - **ObjectIdentifiers** *(list) --*

              A list of ``ObjectIdentifiers`` to which the policy is attached.

              - *(string) --*

            - **NextToken** *(string) --*

              The pagination token.

          - **LookupPolicy** *(dict) --*

            Lists all policies from the root of the  Directory to the object specified. If there
            are no policies present, an empty list is returned. If policies are present, and if
            some objects don't have the policies attached, it returns the ``ObjectIdentifier`` for
            such objects. If policies are present, it returns ``ObjectIdentifier`` , ``policyId`` ,
            and ``policyType`` . Paths that don't lead to the root from the target object are
            ignored. For more information, see `Policies
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
            .

            - **PolicyToPathList** *(list) --*

              Provides list of path to policies. Policies contain ``PolicyId`` ,
              ``ObjectIdentifier`` , and ``PolicyType`` . For more information, see `Policies
              <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
              .

              - *(dict) --*

                Used when a regular object exists in a  Directory and you want to find all of the
                policies that are associated with that object and the parent to that object.

                - **Path** *(string) --*

                  The path that is referenced from the root.

                - **Policies** *(list) --*

                  List of policy objects.

                  - *(dict) --*

                    Contains the ``PolicyType`` , ``PolicyId`` , and the ``ObjectIdentifier`` to
                    which it is attached. For more information, see `Policies
                    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
                    .

                    - **PolicyId** *(string) --*

                      The ID of ``PolicyAttachment`` .

                    - **ObjectIdentifier** *(string) --*

                      The ``ObjectIdentifier`` that is associated with ``PolicyAttachment`` .

                    - **PolicyType** *(string) --*

                      The type of policy that can be associated with ``PolicyAttachment`` .

            - **NextToken** *(string) --*

              The pagination token.

          - **ListIndex** *(dict) --*

            Lists objects attached to the specified index.

            - **IndexAttachments** *(list) --*

              The objects and indexed values attached to the index.

              - *(dict) --*

                Represents an index and an attached object.

                - **IndexedAttributes** *(list) --*

                  The indexed attribute values.

                  - *(dict) --*

                    The combination of an attribute key and an attribute value.

                    - **Key** *(dict) --*

                      The key of the attribute.

                      - **SchemaArn** *(string) --*

                        The Amazon Resource Name (ARN) of the schema that contains the facet and
                        attribute.

                      - **FacetName** *(string) --*

                        The name of the facet that the attribute exists within.

                      - **Name** *(string) --*

                        The name of the attribute.

                    - **Value** *(dict) --*

                      The value of the attribute.

                      - **StringValue** *(string) --*

                        A string data value.

                      - **BinaryValue** *(bytes) --*

                        A binary data value.

                      - **BooleanValue** *(boolean) --*

                        A Boolean data value.

                      - **NumberValue** *(string) --*

                        A number data value.

                      - **DatetimeValue** *(datetime) --*

                        A date and time value.

                - **ObjectIdentifier** *(string) --*

                  In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to
                  the index. In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the
                  index attached to the object. This field will always contain the
                  ``ObjectIdentifier`` of the object on the opposite side of the attachment
                  specified in the query.

            - **NextToken** *(string) --*

              The pagination token.

          - **ListOutgoingTypedLinks** *(dict) --*

            Returns a paginated list of all the outgoing  TypedLinkSpecifier information for an
            object. It also supports filtering by typed link facet and identity attributes. For
            more information, see `Typed Links
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
            .

            - **TypedLinkSpecifiers** *(list) --*

              Returns a typed link specifier as output.

              - *(dict) --*

                Contains all the information that is used to uniquely identify a typed link. The
                parameters discussed in this topic are used to uniquely specify the typed link
                being operated on. The  AttachTypedLink API returns a typed link specifier while
                the  DetachTypedLink API accepts one as input. Similarly, the
                ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed
                link specifiers as output. You can also construct a typed link specifier from
                scratch.

                - **TypedLinkFacet** *(dict) --*

                  Identifies the typed link facet that is associated with the typed link.

                  - **SchemaArn** *(string) --*

                    The Amazon Resource Name (ARN) that is associated with the schema. For more
                    information, see  arns .

                  - **TypedLinkName** *(string) --*

                    The unique name of the typed link facet.

                - **SourceObjectReference** *(dict) --*

                  Identifies the source object that the typed link will attach to.

                  - **Selector** *(string) --*

                    A path selector supports easy selection of an object by the parent/child links
                    leading to it from the directory root. Use the link names from each
                    parent/child link to construct the path. Path selectors start with a slash (/)
                    and link names are separated by slashes. For more information about paths, see
                    `Access Objects
                    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
                    . You can identify an object in one of the following ways:

                    * *$ObjectIdentifier* - An object identifier is an opaque string provided by
                    Amazon Cloud Directory. When creating objects, the system will provide you with
                    the identifier of the created object. An object’s identifier is immutable and
                    no two objects will ever share the same object identifier

                    * */some/path* - Identifies the object based on path

                    * *#SomeBatchReference* - Identifies the object in a batch call

                - **TargetObjectReference** *(dict) --*

                  Identifies the target object that the typed link will attach to.

                  - **Selector** *(string) --*

                    A path selector supports easy selection of an object by the parent/child links
                    leading to it from the directory root. Use the link names from each
                    parent/child link to construct the path. Path selectors start with a slash (/)
                    and link names are separated by slashes. For more information about paths, see
                    `Access Objects
                    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
                    . You can identify an object in one of the following ways:

                    * *$ObjectIdentifier* - An object identifier is an opaque string provided by
                    Amazon Cloud Directory. When creating objects, the system will provide you with
                    the identifier of the created object. An object’s identifier is immutable and
                    no two objects will ever share the same object identifier

                    * */some/path* - Identifies the object based on path

                    * *#SomeBatchReference* - Identifies the object in a batch call

                - **IdentityAttributeValues** *(list) --*

                  Identifies the attribute value to update.

                  - *(dict) --*

                    Identifies the attribute name and value for a typed link.

                    - **AttributeName** *(string) --*

                      The attribute name of the typed link.

                    - **Value** *(dict) --*

                      The value for the typed link.

                      - **StringValue** *(string) --*

                        A string data value.

                      - **BinaryValue** *(bytes) --*

                        A binary data value.

                      - **BooleanValue** *(boolean) --*

                        A Boolean data value.

                      - **NumberValue** *(string) --*

                        A number data value.

                      - **DatetimeValue** *(datetime) --*

                        A date and time value.

            - **NextToken** *(string) --*

              The pagination token.

          - **ListIncomingTypedLinks** *(dict) --*

            Returns a paginated list of all the incoming  TypedLinkSpecifier information for an
            object. It also supports filtering by typed link facet and identity attributes. For
            more information, see `Typed Links
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
            .

            - **LinkSpecifiers** *(list) --*

              Returns one or more typed link specifiers as output.

              - *(dict) --*

                Contains all the information that is used to uniquely identify a typed link. The
                parameters discussed in this topic are used to uniquely specify the typed link
                being operated on. The  AttachTypedLink API returns a typed link specifier while
                the  DetachTypedLink API accepts one as input. Similarly, the
                ListIncomingTypedLinks and  ListOutgoingTypedLinks API operations provide typed
                link specifiers as output. You can also construct a typed link specifier from
                scratch.

                - **TypedLinkFacet** *(dict) --*

                  Identifies the typed link facet that is associated with the typed link.

                  - **SchemaArn** *(string) --*

                    The Amazon Resource Name (ARN) that is associated with the schema. For more
                    information, see  arns .

                  - **TypedLinkName** *(string) --*

                    The unique name of the typed link facet.

                - **SourceObjectReference** *(dict) --*

                  Identifies the source object that the typed link will attach to.

                  - **Selector** *(string) --*

                    A path selector supports easy selection of an object by the parent/child links
                    leading to it from the directory root. Use the link names from each
                    parent/child link to construct the path. Path selectors start with a slash (/)
                    and link names are separated by slashes. For more information about paths, see
                    `Access Objects
                    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
                    . You can identify an object in one of the following ways:

                    * *$ObjectIdentifier* - An object identifier is an opaque string provided by
                    Amazon Cloud Directory. When creating objects, the system will provide you with
                    the identifier of the created object. An object’s identifier is immutable and
                    no two objects will ever share the same object identifier

                    * */some/path* - Identifies the object based on path

                    * *#SomeBatchReference* - Identifies the object in a batch call

                - **TargetObjectReference** *(dict) --*

                  Identifies the target object that the typed link will attach to.

                  - **Selector** *(string) --*

                    A path selector supports easy selection of an object by the parent/child links
                    leading to it from the directory root. Use the link names from each
                    parent/child link to construct the path. Path selectors start with a slash (/)
                    and link names are separated by slashes. For more information about paths, see
                    `Access Objects
                    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
                    . You can identify an object in one of the following ways:

                    * *$ObjectIdentifier* - An object identifier is an opaque string provided by
                    Amazon Cloud Directory. When creating objects, the system will provide you with
                    the identifier of the created object. An object’s identifier is immutable and
                    no two objects will ever share the same object identifier

                    * */some/path* - Identifies the object based on path

                    * *#SomeBatchReference* - Identifies the object in a batch call

                - **IdentityAttributeValues** *(list) --*

                  Identifies the attribute value to update.

                  - *(dict) --*

                    Identifies the attribute name and value for a typed link.

                    - **AttributeName** *(string) --*

                      The attribute name of the typed link.

                    - **Value** *(dict) --*

                      The value for the typed link.

                      - **StringValue** *(string) --*

                        A string data value.

                      - **BinaryValue** *(bytes) --*

                        A binary data value.

                      - **BooleanValue** *(boolean) --*

                        A Boolean data value.

                      - **NumberValue** *(string) --*

                        A number data value.

                      - **DatetimeValue** *(datetime) --*

                        A date and time value.

            - **NextToken** *(string) --*

              The pagination token.

          - **GetLinkAttributes** *(dict) --*

            The list of attributes to retrieve from the typed link.

            - **Attributes** *(list) --*

              The attributes that are associated with the typed link.

              - *(dict) --*

                The combination of an attribute key and an attribute value.

                - **Key** *(dict) --*

                  The key of the attribute.

                  - **SchemaArn** *(string) --*

                    The Amazon Resource Name (ARN) of the schema that contains the facet and
                    attribute.

                  - **FacetName** *(string) --*

                    The name of the facet that the attribute exists within.

                  - **Name** *(string) --*

                    The name of the attribute.

                - **Value** *(dict) --*

                  The value of the attribute.

                  - **StringValue** *(string) --*

                    A string data value.

                  - **BinaryValue** *(bytes) --*

                    A binary data value.

                  - **BooleanValue** *(boolean) --*

                    A Boolean data value.

                  - **NumberValue** *(string) --*

                    A number data value.

                  - **DatetimeValue** *(datetime) --*

                    A date and time value.

          - **ListObjectParents** *(dict) --*

            - **ParentLinks** *(list) --*

              - *(dict) --*

                A pair of ObjectIdentifier and LinkName.

                - **ObjectIdentifier** *(string) --*

                  The ID that is associated with the object.

                - **LinkName** *(string) --*

                  The name of the link between the parent and the child object.

            - **NextToken** *(string) --*

        - **ExceptionResponse** *(dict) --*

          Identifies which operation in a batch has failed.

          - **Type** *(string) --*

            A type of exception, such as ``InvalidArnException`` .

          - **Message** *(string) --*

            An exception message that is associated with the failure.
    """


_ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListKeyTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
)


class ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListKeyTypeDef(
    _ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListKeyTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsAddFacetToObjectObjectAttributeList` `Key`

    The key of the attribute.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --* **[REQUIRED]**

      The name of the facet that the attribute exists within.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.
    """


_ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListValueTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListValueTypeDef(
    _ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListValueTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsAddFacetToObjectObjectAttributeList` `Value`

    The value of the attribute.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListTypeDef",
    {
        "Key": ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListKeyTypeDef,
        "Value": ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListValueTypeDef,
    },
)


class ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListTypeDef(
    _ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsAddFacetToObject` `ObjectAttributeList`

    The combination of an attribute key and an attribute value.

    - **Key** *(dict) --* **[REQUIRED]**

      The key of the attribute.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --* **[REQUIRED]**

        The name of the facet that the attribute exists within.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the attribute.

    - **Value** *(dict) --* **[REQUIRED]**

      The value of the attribute.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientBatchWriteOperationsAddFacetToObjectObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAddFacetToObjectObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsAddFacetToObjectObjectReferenceTypeDef(
    _ClientBatchWriteOperationsAddFacetToObjectObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsAddFacetToObject` `ObjectReference`

    A reference to the object being mutated.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsAddFacetToObjectSchemaFacetTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAddFacetToObjectSchemaFacetTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientBatchWriteOperationsAddFacetToObjectSchemaFacetTypeDef(
    _ClientBatchWriteOperationsAddFacetToObjectSchemaFacetTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsAddFacetToObject` `SchemaFacet`

    Represents the facet being added to the object.

    - **SchemaArn** *(string) --*

      The ARN of the schema that contains the facet with no minor component. See  arns and
      `In-Place Schema Upgrade
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
      for a description of when to provide minor versions.

    - **FacetName** *(string) --*

      The name of the facet.
    """


_ClientBatchWriteOperationsAddFacetToObjectTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAddFacetToObjectTypeDef",
    {
        "SchemaFacet": ClientBatchWriteOperationsAddFacetToObjectSchemaFacetTypeDef,
        "ObjectAttributeList": List[
            ClientBatchWriteOperationsAddFacetToObjectObjectAttributeListTypeDef
        ],
        "ObjectReference": ClientBatchWriteOperationsAddFacetToObjectObjectReferenceTypeDef,
    },
)


class ClientBatchWriteOperationsAddFacetToObjectTypeDef(
    _ClientBatchWriteOperationsAddFacetToObjectTypeDef
):
    """
    Type definition for `ClientBatchWriteOperations` `AddFacetToObject`

    A batch operation that adds a facet to an object.

    - **SchemaFacet** *(dict) --* **[REQUIRED]**

      Represents the facet being added to the object.

      - **SchemaArn** *(string) --*

        The ARN of the schema that contains the facet with no minor component. See  arns and
        `In-Place Schema Upgrade
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
        for a description of when to provide minor versions.

      - **FacetName** *(string) --*

        The name of the facet.

    - **ObjectAttributeList** *(list) --* **[REQUIRED]**

      The attributes to set on the object.

      - *(dict) --*

        The combination of an attribute key and an attribute value.

        - **Key** *(dict) --* **[REQUIRED]**

          The key of the attribute.

          - **SchemaArn** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

          - **FacetName** *(string) --* **[REQUIRED]**

            The name of the facet that the attribute exists within.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the attribute.

        - **Value** *(dict) --* **[REQUIRED]**

          The value of the attribute.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.

    - **ObjectReference** *(dict) --* **[REQUIRED]**

      A reference to the object being mutated.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsAttachObjectChildReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachObjectChildReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsAttachObjectChildReferenceTypeDef(
    _ClientBatchWriteOperationsAttachObjectChildReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsAttachObject` `ChildReference`

    The child object reference that is to be attached to the object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsAttachObjectParentReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachObjectParentReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsAttachObjectParentReferenceTypeDef(
    _ClientBatchWriteOperationsAttachObjectParentReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsAttachObject` `ParentReference`

    The parent object reference.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsAttachObjectTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachObjectTypeDef",
    {
        "ParentReference": ClientBatchWriteOperationsAttachObjectParentReferenceTypeDef,
        "ChildReference": ClientBatchWriteOperationsAttachObjectChildReferenceTypeDef,
        "LinkName": str,
    },
)


class ClientBatchWriteOperationsAttachObjectTypeDef(
    _ClientBatchWriteOperationsAttachObjectTypeDef
):
    """
    Type definition for `ClientBatchWriteOperations` `AttachObject`

    Attaches an object to a  Directory .

    - **ParentReference** *(dict) --* **[REQUIRED]**

      The parent object reference.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **ChildReference** *(dict) --* **[REQUIRED]**

      The child object reference that is to be attached to the object.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **LinkName** *(string) --* **[REQUIRED]**

      The name of the link.
    """


_ClientBatchWriteOperationsAttachPolicyObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachPolicyObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsAttachPolicyObjectReferenceTypeDef(
    _ClientBatchWriteOperationsAttachPolicyObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsAttachPolicy` `ObjectReference`

    The reference that identifies the object to which the policy will be attached.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsAttachPolicyPolicyReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachPolicyPolicyReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsAttachPolicyPolicyReferenceTypeDef(
    _ClientBatchWriteOperationsAttachPolicyPolicyReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsAttachPolicy` `PolicyReference`

    The reference that is associated with the policy object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsAttachPolicyTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachPolicyTypeDef",
    {
        "PolicyReference": ClientBatchWriteOperationsAttachPolicyPolicyReferenceTypeDef,
        "ObjectReference": ClientBatchWriteOperationsAttachPolicyObjectReferenceTypeDef,
    },
)


class ClientBatchWriteOperationsAttachPolicyTypeDef(
    _ClientBatchWriteOperationsAttachPolicyTypeDef
):
    """
    Type definition for `ClientBatchWriteOperations` `AttachPolicy`

    Attaches a policy object to a regular object. An object can have a limited number of attached
    policies.

    - **PolicyReference** *(dict) --* **[REQUIRED]**

      The reference that is associated with the policy object.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **ObjectReference** *(dict) --* **[REQUIRED]**

      The reference that identifies the object to which the policy will be attached.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsAttachToIndexIndexReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachToIndexIndexReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsAttachToIndexIndexReferenceTypeDef(
    _ClientBatchWriteOperationsAttachToIndexIndexReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsAttachToIndex` `IndexReference`

    A reference to the index that you are attaching the object to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsAttachToIndexTargetReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachToIndexTargetReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsAttachToIndexTargetReferenceTypeDef(
    _ClientBatchWriteOperationsAttachToIndexTargetReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsAttachToIndex` `TargetReference`

    A reference to the object that you are attaching to the index.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsAttachToIndexTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachToIndexTypeDef",
    {
        "IndexReference": ClientBatchWriteOperationsAttachToIndexIndexReferenceTypeDef,
        "TargetReference": ClientBatchWriteOperationsAttachToIndexTargetReferenceTypeDef,
    },
)


class ClientBatchWriteOperationsAttachToIndexTypeDef(
    _ClientBatchWriteOperationsAttachToIndexTypeDef
):
    """
    Type definition for `ClientBatchWriteOperations` `AttachToIndex`

    Attaches the specified object to the specified index.

    - **IndexReference** *(dict) --* **[REQUIRED]**

      A reference to the index that you are attaching the object to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **TargetReference** *(dict) --* **[REQUIRED]**

      A reference to the object that you are attaching to the index.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsAttachTypedLinkAttributesValueTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachTypedLinkAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchWriteOperationsAttachTypedLinkAttributesValueTypeDef(
    _ClientBatchWriteOperationsAttachTypedLinkAttributesValueTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsAttachTypedLinkAttributes` `Value`

    The value for the typed link.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchWriteOperationsAttachTypedLinkAttributesTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachTypedLinkAttributesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchWriteOperationsAttachTypedLinkAttributesValueTypeDef,
    },
)


class ClientBatchWriteOperationsAttachTypedLinkAttributesTypeDef(
    _ClientBatchWriteOperationsAttachTypedLinkAttributesTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsAttachTypedLink` `Attributes`

    Identifies the attribute name and value for a typed link.

    - **AttributeName** *(string) --* **[REQUIRED]**

      The attribute name of the typed link.

    - **Value** *(dict) --* **[REQUIRED]**

      The value for the typed link.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientBatchWriteOperationsAttachTypedLinkSourceObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachTypedLinkSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsAttachTypedLinkSourceObjectReferenceTypeDef(
    _ClientBatchWriteOperationsAttachTypedLinkSourceObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsAttachTypedLink` `SourceObjectReference`

    Identifies the source object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsAttachTypedLinkTargetObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachTypedLinkTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsAttachTypedLinkTargetObjectReferenceTypeDef(
    _ClientBatchWriteOperationsAttachTypedLinkTargetObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsAttachTypedLink` `TargetObjectReference`

    Identifies the target object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsAttachTypedLinkTypedLinkFacetTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachTypedLinkTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
)


class ClientBatchWriteOperationsAttachTypedLinkTypedLinkFacetTypeDef(
    _ClientBatchWriteOperationsAttachTypedLinkTypedLinkFacetTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsAttachTypedLink` `TypedLinkFacet`

    Identifies the typed link facet that is associated with the typed link.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more information,
      see  arns .

    - **TypedLinkName** *(string) --* **[REQUIRED]**

      The unique name of the typed link facet.
    """


_ClientBatchWriteOperationsAttachTypedLinkTypeDef = TypedDict(
    "_ClientBatchWriteOperationsAttachTypedLinkTypeDef",
    {
        "SourceObjectReference": ClientBatchWriteOperationsAttachTypedLinkSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchWriteOperationsAttachTypedLinkTargetObjectReferenceTypeDef,
        "TypedLinkFacet": ClientBatchWriteOperationsAttachTypedLinkTypedLinkFacetTypeDef,
        "Attributes": List[ClientBatchWriteOperationsAttachTypedLinkAttributesTypeDef],
    },
)


class ClientBatchWriteOperationsAttachTypedLinkTypeDef(
    _ClientBatchWriteOperationsAttachTypedLinkTypeDef
):
    """
    Type definition for `ClientBatchWriteOperations` `AttachTypedLink`

    Attaches a typed link to a specified source and target object. For more information, see
    `Typed Links
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
    .

    - **SourceObjectReference** *(dict) --* **[REQUIRED]**

      Identifies the source object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **TargetObjectReference** *(dict) --* **[REQUIRED]**

      Identifies the target object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **TypedLinkFacet** *(dict) --* **[REQUIRED]**

      Identifies the typed link facet that is associated with the typed link.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) that is associated with the schema. For more information,
        see  arns .

      - **TypedLinkName** *(string) --* **[REQUIRED]**

        The unique name of the typed link facet.

    - **Attributes** *(list) --* **[REQUIRED]**

      A set of attributes that are associated with the typed link.

      - *(dict) --*

        Identifies the attribute name and value for a typed link.

        - **AttributeName** *(string) --* **[REQUIRED]**

          The attribute name of the typed link.

        - **Value** *(dict) --* **[REQUIRED]**

          The value for the typed link.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ClientBatchWriteOperationsCreateIndexOrderedIndexedAttributeListTypeDef = TypedDict(
    "_ClientBatchWriteOperationsCreateIndexOrderedIndexedAttributeListTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
)


class ClientBatchWriteOperationsCreateIndexOrderedIndexedAttributeListTypeDef(
    _ClientBatchWriteOperationsCreateIndexOrderedIndexedAttributeListTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsCreateIndex` `OrderedIndexedAttributeList`

    A unique identifier for an attribute.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --* **[REQUIRED]**

      The name of the facet that the attribute exists within.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.
    """


_ClientBatchWriteOperationsCreateIndexParentReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsCreateIndexParentReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsCreateIndexParentReferenceTypeDef(
    _ClientBatchWriteOperationsCreateIndexParentReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsCreateIndex` `ParentReference`

    A reference to the parent object that contains the index object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_RequiredClientBatchWriteOperationsCreateIndexTypeDef = TypedDict(
    "_RequiredClientBatchWriteOperationsCreateIndexTypeDef",
    {
        "OrderedIndexedAttributeList": List[
            ClientBatchWriteOperationsCreateIndexOrderedIndexedAttributeListTypeDef
        ],
        "IsUnique": bool,
    },
)
_OptionalClientBatchWriteOperationsCreateIndexTypeDef = TypedDict(
    "_OptionalClientBatchWriteOperationsCreateIndexTypeDef",
    {
        "ParentReference": ClientBatchWriteOperationsCreateIndexParentReferenceTypeDef,
        "LinkName": str,
        "BatchReferenceName": str,
    },
    total=False,
)


class ClientBatchWriteOperationsCreateIndexTypeDef(
    _RequiredClientBatchWriteOperationsCreateIndexTypeDef,
    _OptionalClientBatchWriteOperationsCreateIndexTypeDef,
):
    """
    Type definition for `ClientBatchWriteOperations` `CreateIndex`

    Creates an index object. See `Indexing and search
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search.htm>`__ for
    more information.

    - **OrderedIndexedAttributeList** *(list) --* **[REQUIRED]**

      Specifies the attributes that should be indexed on. Currently only a single attribute is
      supported.

      - *(dict) --*

        A unique identifier for an attribute.

        - **SchemaArn** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

        - **FacetName** *(string) --* **[REQUIRED]**

          The name of the facet that the attribute exists within.

        - **Name** *(string) --* **[REQUIRED]**

          The name of the attribute.

    - **IsUnique** *(boolean) --* **[REQUIRED]**

      Indicates whether the attribute that is being indexed has unique values or not.

    - **ParentReference** *(dict) --*

      A reference to the parent object that contains the index object.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **LinkName** *(string) --*

      The name of the link between the parent object and the index object.

    - **BatchReferenceName** *(string) --*

      The batch reference name. See `Transaction Support
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/transaction_support.html>`__
      for more information.
    """


_ClientBatchWriteOperationsCreateObjectObjectAttributeListKeyTypeDef = TypedDict(
    "_ClientBatchWriteOperationsCreateObjectObjectAttributeListKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
)


class ClientBatchWriteOperationsCreateObjectObjectAttributeListKeyTypeDef(
    _ClientBatchWriteOperationsCreateObjectObjectAttributeListKeyTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsCreateObjectObjectAttributeList` `Key`

    The key of the attribute.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --* **[REQUIRED]**

      The name of the facet that the attribute exists within.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.
    """


_ClientBatchWriteOperationsCreateObjectObjectAttributeListValueTypeDef = TypedDict(
    "_ClientBatchWriteOperationsCreateObjectObjectAttributeListValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchWriteOperationsCreateObjectObjectAttributeListValueTypeDef(
    _ClientBatchWriteOperationsCreateObjectObjectAttributeListValueTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsCreateObjectObjectAttributeList` `Value`

    The value of the attribute.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchWriteOperationsCreateObjectObjectAttributeListTypeDef = TypedDict(
    "_ClientBatchWriteOperationsCreateObjectObjectAttributeListTypeDef",
    {
        "Key": ClientBatchWriteOperationsCreateObjectObjectAttributeListKeyTypeDef,
        "Value": ClientBatchWriteOperationsCreateObjectObjectAttributeListValueTypeDef,
    },
)


class ClientBatchWriteOperationsCreateObjectObjectAttributeListTypeDef(
    _ClientBatchWriteOperationsCreateObjectObjectAttributeListTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsCreateObject` `ObjectAttributeList`

    The combination of an attribute key and an attribute value.

    - **Key** *(dict) --* **[REQUIRED]**

      The key of the attribute.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --* **[REQUIRED]**

        The name of the facet that the attribute exists within.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the attribute.

    - **Value** *(dict) --* **[REQUIRED]**

      The value of the attribute.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientBatchWriteOperationsCreateObjectParentReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsCreateObjectParentReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsCreateObjectParentReferenceTypeDef(
    _ClientBatchWriteOperationsCreateObjectParentReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsCreateObject` `ParentReference`

    If specified, the parent reference to which this object will be attached.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsCreateObjectSchemaFacetTypeDef = TypedDict(
    "_ClientBatchWriteOperationsCreateObjectSchemaFacetTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientBatchWriteOperationsCreateObjectSchemaFacetTypeDef(
    _ClientBatchWriteOperationsCreateObjectSchemaFacetTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsCreateObject` `SchemaFacet`

    A facet.

    - **SchemaArn** *(string) --*

      The ARN of the schema that contains the facet with no minor component. See  arns and
      `In-Place Schema Upgrade
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
      for a description of when to provide minor versions.

    - **FacetName** *(string) --*

      The name of the facet.
    """


_RequiredClientBatchWriteOperationsCreateObjectTypeDef = TypedDict(
    "_RequiredClientBatchWriteOperationsCreateObjectTypeDef",
    {
        "SchemaFacet": List[ClientBatchWriteOperationsCreateObjectSchemaFacetTypeDef],
        "ObjectAttributeList": List[
            ClientBatchWriteOperationsCreateObjectObjectAttributeListTypeDef
        ],
    },
)
_OptionalClientBatchWriteOperationsCreateObjectTypeDef = TypedDict(
    "_OptionalClientBatchWriteOperationsCreateObjectTypeDef",
    {
        "ParentReference": ClientBatchWriteOperationsCreateObjectParentReferenceTypeDef,
        "LinkName": str,
        "BatchReferenceName": str,
    },
    total=False,
)


class ClientBatchWriteOperationsCreateObjectTypeDef(
    _RequiredClientBatchWriteOperationsCreateObjectTypeDef,
    _OptionalClientBatchWriteOperationsCreateObjectTypeDef,
):
    """
    Type definition for `ClientBatchWriteOperations` `CreateObject`

    Creates an object.

    - **SchemaFacet** *(list) --* **[REQUIRED]**

      A list of ``FacetArns`` that will be associated with the object. For more information, see
      arns .

      - *(dict) --*

        A facet.

        - **SchemaArn** *(string) --*

          The ARN of the schema that contains the facet with no minor component. See  arns and
          `In-Place Schema Upgrade
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
          for a description of when to provide minor versions.

        - **FacetName** *(string) --*

          The name of the facet.

    - **ObjectAttributeList** *(list) --* **[REQUIRED]**

      An attribute map, which contains an attribute ARN as the key and attribute value as the map
      value.

      - *(dict) --*

        The combination of an attribute key and an attribute value.

        - **Key** *(dict) --* **[REQUIRED]**

          The key of the attribute.

          - **SchemaArn** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

          - **FacetName** *(string) --* **[REQUIRED]**

            The name of the facet that the attribute exists within.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the attribute.

        - **Value** *(dict) --* **[REQUIRED]**

          The value of the attribute.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.

    - **ParentReference** *(dict) --*

      If specified, the parent reference to which this object will be attached.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **LinkName** *(string) --*

      The name of the link.

    - **BatchReferenceName** *(string) --*

      The batch reference name. See `Transaction Support
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/transaction_support.html>`__
      for more information.
    """


_ClientBatchWriteOperationsDeleteObjectObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDeleteObjectObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsDeleteObjectObjectReferenceTypeDef(
    _ClientBatchWriteOperationsDeleteObjectObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsDeleteObject` `ObjectReference`

    The reference that identifies the object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsDeleteObjectTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDeleteObjectTypeDef",
    {"ObjectReference": ClientBatchWriteOperationsDeleteObjectObjectReferenceTypeDef},
)


class ClientBatchWriteOperationsDeleteObjectTypeDef(
    _ClientBatchWriteOperationsDeleteObjectTypeDef
):
    """
    Type definition for `ClientBatchWriteOperations` `DeleteObject`

    Deletes an object in a  Directory .

    - **ObjectReference** *(dict) --* **[REQUIRED]**

      The reference that identifies the object.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsDetachFromIndexIndexReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachFromIndexIndexReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsDetachFromIndexIndexReferenceTypeDef(
    _ClientBatchWriteOperationsDetachFromIndexIndexReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsDetachFromIndex` `IndexReference`

    A reference to the index object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsDetachFromIndexTargetReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachFromIndexTargetReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsDetachFromIndexTargetReferenceTypeDef(
    _ClientBatchWriteOperationsDetachFromIndexTargetReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsDetachFromIndex` `TargetReference`

    A reference to the object being detached from the index.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsDetachFromIndexTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachFromIndexTypeDef",
    {
        "IndexReference": ClientBatchWriteOperationsDetachFromIndexIndexReferenceTypeDef,
        "TargetReference": ClientBatchWriteOperationsDetachFromIndexTargetReferenceTypeDef,
    },
)


class ClientBatchWriteOperationsDetachFromIndexTypeDef(
    _ClientBatchWriteOperationsDetachFromIndexTypeDef
):
    """
    Type definition for `ClientBatchWriteOperations` `DetachFromIndex`

    Detaches the specified object from the specified index.

    - **IndexReference** *(dict) --* **[REQUIRED]**

      A reference to the index object.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **TargetReference** *(dict) --* **[REQUIRED]**

      A reference to the object being detached from the index.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsDetachObjectParentReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachObjectParentReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsDetachObjectParentReferenceTypeDef(
    _ClientBatchWriteOperationsDetachObjectParentReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsDetachObject` `ParentReference`

    Parent reference from which the object with the specified link name is detached.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_RequiredClientBatchWriteOperationsDetachObjectTypeDef = TypedDict(
    "_RequiredClientBatchWriteOperationsDetachObjectTypeDef",
    {
        "ParentReference": ClientBatchWriteOperationsDetachObjectParentReferenceTypeDef,
        "LinkName": str,
    },
)
_OptionalClientBatchWriteOperationsDetachObjectTypeDef = TypedDict(
    "_OptionalClientBatchWriteOperationsDetachObjectTypeDef",
    {"BatchReferenceName": str},
    total=False,
)


class ClientBatchWriteOperationsDetachObjectTypeDef(
    _RequiredClientBatchWriteOperationsDetachObjectTypeDef,
    _OptionalClientBatchWriteOperationsDetachObjectTypeDef,
):
    """
    Type definition for `ClientBatchWriteOperations` `DetachObject`

    Detaches an object from a  Directory .

    - **ParentReference** *(dict) --* **[REQUIRED]**

      Parent reference from which the object with the specified link name is detached.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **LinkName** *(string) --* **[REQUIRED]**

      The name of the link.

    - **BatchReferenceName** *(string) --*

      The batch reference name. See `Transaction Support
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/transaction_support.html>`__
      for more information.
    """


_ClientBatchWriteOperationsDetachPolicyObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachPolicyObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsDetachPolicyObjectReferenceTypeDef(
    _ClientBatchWriteOperationsDetachPolicyObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsDetachPolicy` `ObjectReference`

    Reference that identifies the object whose policy object will be detached.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsDetachPolicyPolicyReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachPolicyPolicyReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsDetachPolicyPolicyReferenceTypeDef(
    _ClientBatchWriteOperationsDetachPolicyPolicyReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsDetachPolicy` `PolicyReference`

    Reference that identifies the policy object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsDetachPolicyTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachPolicyTypeDef",
    {
        "PolicyReference": ClientBatchWriteOperationsDetachPolicyPolicyReferenceTypeDef,
        "ObjectReference": ClientBatchWriteOperationsDetachPolicyObjectReferenceTypeDef,
    },
)


class ClientBatchWriteOperationsDetachPolicyTypeDef(
    _ClientBatchWriteOperationsDetachPolicyTypeDef
):
    """
    Type definition for `ClientBatchWriteOperations` `DetachPolicy`

    Detaches a policy from a  Directory .

    - **PolicyReference** *(dict) --* **[REQUIRED]**

      Reference that identifies the policy object.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **ObjectReference** *(dict) --* **[REQUIRED]**

      Reference that identifies the object whose policy object will be detached.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef(
    _ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValues` `Value`

    The value for the typed link.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
)


class ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef(
    _ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifier` `IdentityAttributeValues`

    Identifies the attribute name and value for a typed link.

    - **AttributeName** *(string) --* **[REQUIRED]**

      The attribute name of the typed link.

    - **Value** *(dict) --* **[REQUIRED]**

      The value for the typed link.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef(
    _ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifier` `SourceObjectReference`

    Identifies the source object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading
      to it from the directory root. Use the link names from each parent/child link to
      construct the path. Path selectors start with a slash (/) and link names are separated
      by slashes. For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
      Cloud Directory. When creating objects, the system will provide you with the identifier
      of the created object. An object’s identifier is immutable and no two objects will ever
      share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef(
    _ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifier` `TargetObjectReference`

    Identifies the target object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading
      to it from the directory root. Use the link names from each parent/child link to
      construct the path. Path selectors start with a slash (/) and link names are separated
      by slashes. For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
      Cloud Directory. When creating objects, the system will provide you with the identifier
      of the created object. An object’s identifier is immutable and no two objects will ever
      share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
)


class ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef(
    _ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifier` `TypedLinkFacet`

    Identifies the typed link facet that is associated with the typed link.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more
      information, see  arns .

    - **TypedLinkName** *(string) --* **[REQUIRED]**

      The unique name of the typed link facet.
    """


_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
)


class ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypeDef(
    _ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsDetachTypedLink` `TypedLinkSpecifier`

    Used to accept a typed link specifier as input.

    - **TypedLinkFacet** *(dict) --* **[REQUIRED]**

      Identifies the typed link facet that is associated with the typed link.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) that is associated with the schema. For more
        information, see  arns .

      - **TypedLinkName** *(string) --* **[REQUIRED]**

        The unique name of the typed link facet.

    - **SourceObjectReference** *(dict) --* **[REQUIRED]**

      Identifies the source object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading
        to it from the directory root. Use the link names from each parent/child link to
        construct the path. Path selectors start with a slash (/) and link names are separated
        by slashes. For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
        Cloud Directory. When creating objects, the system will provide you with the identifier
        of the created object. An object’s identifier is immutable and no two objects will ever
        share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **TargetObjectReference** *(dict) --* **[REQUIRED]**

      Identifies the target object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading
        to it from the directory root. Use the link names from each parent/child link to
        construct the path. Path selectors start with a slash (/) and link names are separated
        by slashes. For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
        Cloud Directory. When creating objects, the system will provide you with the identifier
        of the created object. An object’s identifier is immutable and no two objects will ever
        share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **IdentityAttributeValues** *(list) --* **[REQUIRED]**

      Identifies the attribute value to update.

      - *(dict) --*

        Identifies the attribute name and value for a typed link.

        - **AttributeName** *(string) --* **[REQUIRED]**

          The attribute name of the typed link.

        - **Value** *(dict) --* **[REQUIRED]**

          The value for the typed link.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ClientBatchWriteOperationsDetachTypedLinkTypeDef = TypedDict(
    "_ClientBatchWriteOperationsDetachTypedLinkTypeDef",
    {
        "TypedLinkSpecifier": ClientBatchWriteOperationsDetachTypedLinkTypedLinkSpecifierTypeDef
    },
)


class ClientBatchWriteOperationsDetachTypedLinkTypeDef(
    _ClientBatchWriteOperationsDetachTypedLinkTypeDef
):
    """
    Type definition for `ClientBatchWriteOperations` `DetachTypedLink`

    Detaches a typed link from a specified source and target object. For more information, see
    `Typed Links
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
    .

    - **TypedLinkSpecifier** *(dict) --* **[REQUIRED]**

      Used to accept a typed link specifier as input.

      - **TypedLinkFacet** *(dict) --* **[REQUIRED]**

        Identifies the typed link facet that is associated with the typed link.

        - **SchemaArn** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) that is associated with the schema. For more
          information, see  arns .

        - **TypedLinkName** *(string) --* **[REQUIRED]**

          The unique name of the typed link facet.

      - **SourceObjectReference** *(dict) --* **[REQUIRED]**

        Identifies the source object that the typed link will attach to.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading
          to it from the directory root. Use the link names from each parent/child link to
          construct the path. Path selectors start with a slash (/) and link names are separated
          by slashes. For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
          Cloud Directory. When creating objects, the system will provide you with the identifier
          of the created object. An object’s identifier is immutable and no two objects will ever
          share the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **TargetObjectReference** *(dict) --* **[REQUIRED]**

        Identifies the target object that the typed link will attach to.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading
          to it from the directory root. Use the link names from each parent/child link to
          construct the path. Path selectors start with a slash (/) and link names are separated
          by slashes. For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
          Cloud Directory. When creating objects, the system will provide you with the identifier
          of the created object. An object’s identifier is immutable and no two objects will ever
          share the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **IdentityAttributeValues** *(list) --* **[REQUIRED]**

        Identifies the attribute value to update.

        - *(dict) --*

          Identifies the attribute name and value for a typed link.

          - **AttributeName** *(string) --* **[REQUIRED]**

            The attribute name of the typed link.

          - **Value** *(dict) --* **[REQUIRED]**

            The value for the typed link.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.
    """


_ClientBatchWriteOperationsRemoveFacetFromObjectObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsRemoveFacetFromObjectObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsRemoveFacetFromObjectObjectReferenceTypeDef(
    _ClientBatchWriteOperationsRemoveFacetFromObjectObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsRemoveFacetFromObject` `ObjectReference`

    A reference to the object whose facet will be removed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsRemoveFacetFromObjectSchemaFacetTypeDef = TypedDict(
    "_ClientBatchWriteOperationsRemoveFacetFromObjectSchemaFacetTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientBatchWriteOperationsRemoveFacetFromObjectSchemaFacetTypeDef(
    _ClientBatchWriteOperationsRemoveFacetFromObjectSchemaFacetTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsRemoveFacetFromObject` `SchemaFacet`

    The facet to remove from the object.

    - **SchemaArn** *(string) --*

      The ARN of the schema that contains the facet with no minor component. See  arns and
      `In-Place Schema Upgrade
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
      for a description of when to provide minor versions.

    - **FacetName** *(string) --*

      The name of the facet.
    """


_ClientBatchWriteOperationsRemoveFacetFromObjectTypeDef = TypedDict(
    "_ClientBatchWriteOperationsRemoveFacetFromObjectTypeDef",
    {
        "SchemaFacet": ClientBatchWriteOperationsRemoveFacetFromObjectSchemaFacetTypeDef,
        "ObjectReference": ClientBatchWriteOperationsRemoveFacetFromObjectObjectReferenceTypeDef,
    },
)


class ClientBatchWriteOperationsRemoveFacetFromObjectTypeDef(
    _ClientBatchWriteOperationsRemoveFacetFromObjectTypeDef
):
    """
    Type definition for `ClientBatchWriteOperations` `RemoveFacetFromObject`

    A batch operation that removes a facet from an object.

    - **SchemaFacet** *(dict) --* **[REQUIRED]**

      The facet to remove from the object.

      - **SchemaArn** *(string) --*

        The ARN of the schema that contains the facet with no minor component. See  arns and
        `In-Place Schema Upgrade
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
        for a description of when to provide minor versions.

      - **FacetName** *(string) --*

        The name of the facet.

    - **ObjectReference** *(dict) --* **[REQUIRED]**

      A reference to the object whose facet will be removed.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeAction` `AttributeUpdateValue`

    The value that you want to update to.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef",
    {
        "AttributeActionType": str,
        "AttributeUpdateValue": ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdates` `AttributeAction`

    The action to perform as part of the attribute update.

    - **AttributeActionType** *(string) --*

      A type that can be either ``UPDATE_OR_CREATE`` or ``DELETE`` .

    - **AttributeUpdateValue** *(dict) --*

      The value that you want to update to.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
)


class ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdates` `AttributeKey`

    The key of the attribute being updated.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --* **[REQUIRED]**

      The name of the facet that the attribute exists within.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.
    """


_ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesTypeDef",
    {
        "AttributeKey": ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef,
        "AttributeAction": ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsUpdateLinkAttributes` `AttributeUpdates`

    Structure that contains attribute update information.

    - **AttributeKey** *(dict) --*

      The key of the attribute being updated.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --* **[REQUIRED]**

        The name of the facet that the attribute exists within.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the attribute.

    - **AttributeAction** *(dict) --*

      The action to perform as part of the attribute update.

      - **AttributeActionType** *(string) --*

        A type that can be either ``UPDATE_OR_CREATE`` or ``DELETE`` .

      - **AttributeUpdateValue** *(dict) --*

        The value that you want to update to.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.
    """


_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValues` `Value`

    The value for the typed link.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
)


class ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifier` `IdentityAttributeValues`

    Identifies the attribute name and value for a typed link.

    - **AttributeName** *(string) --* **[REQUIRED]**

      The attribute name of the typed link.

    - **Value** *(dict) --* **[REQUIRED]**

      The value for the typed link.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifier` `SourceObjectReference`

    Identifies the source object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading
      to it from the directory root. Use the link names from each parent/child link to
      construct the path. Path selectors start with a slash (/) and link names are separated
      by slashes. For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
      Cloud Directory. When creating objects, the system will provide you with the identifier
      of the created object. An object’s identifier is immutable and no two objects will ever
      share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifier` `TargetObjectReference`

    Identifies the target object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading
      to it from the directory root. Use the link names from each parent/child link to
      construct the path. Path selectors start with a slash (/) and link names are separated
      by slashes. For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
      Cloud Directory. When creating objects, the system will provide you with the identifier
      of the created object. An object’s identifier is immutable and no two objects will ever
      share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
)


class ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifier` `TypedLinkFacet`

    Identifies the typed link facet that is associated with the typed link.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more
      information, see  arns .

    - **TypedLinkName** *(string) --* **[REQUIRED]**

      The unique name of the typed link facet.
    """


_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
)


class ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsUpdateLinkAttributes` `TypedLinkSpecifier`

    Allows a typed link specifier to be accepted as input.

    - **TypedLinkFacet** *(dict) --* **[REQUIRED]**

      Identifies the typed link facet that is associated with the typed link.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) that is associated with the schema. For more
        information, see  arns .

      - **TypedLinkName** *(string) --* **[REQUIRED]**

        The unique name of the typed link facet.

    - **SourceObjectReference** *(dict) --* **[REQUIRED]**

      Identifies the source object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading
        to it from the directory root. Use the link names from each parent/child link to
        construct the path. Path selectors start with a slash (/) and link names are separated
        by slashes. For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
        Cloud Directory. When creating objects, the system will provide you with the identifier
        of the created object. An object’s identifier is immutable and no two objects will ever
        share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **TargetObjectReference** *(dict) --* **[REQUIRED]**

      Identifies the target object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading
        to it from the directory root. Use the link names from each parent/child link to
        construct the path. Path selectors start with a slash (/) and link names are separated
        by slashes. For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
        Cloud Directory. When creating objects, the system will provide you with the identifier
        of the created object. An object’s identifier is immutable and no two objects will ever
        share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **IdentityAttributeValues** *(list) --* **[REQUIRED]**

      Identifies the attribute value to update.

      - *(dict) --*

        Identifies the attribute name and value for a typed link.

        - **AttributeName** *(string) --* **[REQUIRED]**

          The attribute name of the typed link.

        - **Value** *(dict) --* **[REQUIRED]**

          The value for the typed link.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ClientBatchWriteOperationsUpdateLinkAttributesTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateLinkAttributesTypeDef",
    {
        "TypedLinkSpecifier": ClientBatchWriteOperationsUpdateLinkAttributesTypedLinkSpecifierTypeDef,
        "AttributeUpdates": List[
            ClientBatchWriteOperationsUpdateLinkAttributesAttributeUpdatesTypeDef
        ],
    },
)


class ClientBatchWriteOperationsUpdateLinkAttributesTypeDef(
    _ClientBatchWriteOperationsUpdateLinkAttributesTypeDef
):
    """
    Type definition for `ClientBatchWriteOperations` `UpdateLinkAttributes`

    Updates a given object's attributes.

    - **TypedLinkSpecifier** *(dict) --* **[REQUIRED]**

      Allows a typed link specifier to be accepted as input.

      - **TypedLinkFacet** *(dict) --* **[REQUIRED]**

        Identifies the typed link facet that is associated with the typed link.

        - **SchemaArn** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) that is associated with the schema. For more
          information, see  arns .

        - **TypedLinkName** *(string) --* **[REQUIRED]**

          The unique name of the typed link facet.

      - **SourceObjectReference** *(dict) --* **[REQUIRED]**

        Identifies the source object that the typed link will attach to.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading
          to it from the directory root. Use the link names from each parent/child link to
          construct the path. Path selectors start with a slash (/) and link names are separated
          by slashes. For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
          Cloud Directory. When creating objects, the system will provide you with the identifier
          of the created object. An object’s identifier is immutable and no two objects will ever
          share the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **TargetObjectReference** *(dict) --* **[REQUIRED]**

        Identifies the target object that the typed link will attach to.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading
          to it from the directory root. Use the link names from each parent/child link to
          construct the path. Path selectors start with a slash (/) and link names are separated
          by slashes. For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
          Cloud Directory. When creating objects, the system will provide you with the identifier
          of the created object. An object’s identifier is immutable and no two objects will ever
          share the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **IdentityAttributeValues** *(list) --* **[REQUIRED]**

        Identifies the attribute value to update.

        - *(dict) --*

          Identifies the attribute name and value for a typed link.

          - **AttributeName** *(string) --* **[REQUIRED]**

            The attribute name of the typed link.

          - **Value** *(dict) --* **[REQUIRED]**

            The value for the typed link.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.

    - **AttributeUpdates** *(list) --* **[REQUIRED]**

      The attributes update structure.

      - *(dict) --*

        Structure that contains attribute update information.

        - **AttributeKey** *(dict) --*

          The key of the attribute being updated.

          - **SchemaArn** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

          - **FacetName** *(string) --* **[REQUIRED]**

            The name of the facet that the attribute exists within.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the attribute.

        - **AttributeAction** *(dict) --*

          The action to perform as part of the attribute update.

          - **AttributeActionType** *(string) --*

            A type that can be either ``UPDATE_OR_CREATE`` or ``DELETE`` .

          - **AttributeUpdateValue** *(dict) --*

            The value that you want to update to.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.
    """


_ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef(
    _ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeAction` `ObjectAttributeUpdateValue`

    The value that you want to update to.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef",
    {
        "ObjectAttributeActionType": str,
        "ObjectAttributeUpdateValue": ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef(
    _ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdates` `ObjectAttributeAction`

    The action to perform as part of the attribute update.

    - **ObjectAttributeActionType** *(string) --*

      A type that can be either ``Update`` or ``Delete`` .

    - **ObjectAttributeUpdateValue** *(dict) --*

      The value that you want to update to.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
)


class ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef(
    _ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdates` `ObjectAttributeKey`

    The key of the attribute being updated.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --* **[REQUIRED]**

      The name of the facet that the attribute exists within.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.
    """


_ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesTypeDef",
    {
        "ObjectAttributeKey": ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef,
        "ObjectAttributeAction": ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesTypeDef(
    _ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsUpdateObjectAttributes` `AttributeUpdates`

    Structure that contains attribute update information.

    - **ObjectAttributeKey** *(dict) --*

      The key of the attribute being updated.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --* **[REQUIRED]**

        The name of the facet that the attribute exists within.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the attribute.

    - **ObjectAttributeAction** *(dict) --*

      The action to perform as part of the attribute update.

      - **ObjectAttributeActionType** *(string) --*

        A type that can be either ``Update`` or ``Delete`` .

      - **ObjectAttributeUpdateValue** *(dict) --*

        The value that you want to update to.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.
    """


_ClientBatchWriteOperationsUpdateObjectAttributesObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateObjectAttributesObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteOperationsUpdateObjectAttributesObjectReferenceTypeDef(
    _ClientBatchWriteOperationsUpdateObjectAttributesObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteOperationsUpdateObjectAttributes` `ObjectReference`

    Reference that identifies the object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to
      it from the directory root. Use the link names from each parent/child link to construct
      the path. Path selectors start with a slash (/) and link names are separated by slashes.
      For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share
      the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteOperationsUpdateObjectAttributesTypeDef = TypedDict(
    "_ClientBatchWriteOperationsUpdateObjectAttributesTypeDef",
    {
        "ObjectReference": ClientBatchWriteOperationsUpdateObjectAttributesObjectReferenceTypeDef,
        "AttributeUpdates": List[
            ClientBatchWriteOperationsUpdateObjectAttributesAttributeUpdatesTypeDef
        ],
    },
)


class ClientBatchWriteOperationsUpdateObjectAttributesTypeDef(
    _ClientBatchWriteOperationsUpdateObjectAttributesTypeDef
):
    """
    Type definition for `ClientBatchWriteOperations` `UpdateObjectAttributes`

    Updates a given object's attributes.

    - **ObjectReference** *(dict) --* **[REQUIRED]**

      Reference that identifies the object.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to
        it from the directory root. Use the link names from each parent/child link to construct
        the path. Path selectors start with a slash (/) and link names are separated by slashes.
        For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share
        the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **AttributeUpdates** *(list) --* **[REQUIRED]**

      Attributes update structure.

      - *(dict) --*

        Structure that contains attribute update information.

        - **ObjectAttributeKey** *(dict) --*

          The key of the attribute being updated.

          - **SchemaArn** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

          - **FacetName** *(string) --* **[REQUIRED]**

            The name of the facet that the attribute exists within.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the attribute.

        - **ObjectAttributeAction** *(dict) --*

          The action to perform as part of the attribute update.

          - **ObjectAttributeActionType** *(string) --*

            A type that can be either ``Update`` or ``Delete`` .

          - **ObjectAttributeUpdateValue** *(dict) --*

            The value that you want to update to.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.
    """


_ClientBatchWriteOperationsTypeDef = TypedDict(
    "_ClientBatchWriteOperationsTypeDef",
    {
        "CreateObject": ClientBatchWriteOperationsCreateObjectTypeDef,
        "AttachObject": ClientBatchWriteOperationsAttachObjectTypeDef,
        "DetachObject": ClientBatchWriteOperationsDetachObjectTypeDef,
        "UpdateObjectAttributes": ClientBatchWriteOperationsUpdateObjectAttributesTypeDef,
        "DeleteObject": ClientBatchWriteOperationsDeleteObjectTypeDef,
        "AddFacetToObject": ClientBatchWriteOperationsAddFacetToObjectTypeDef,
        "RemoveFacetFromObject": ClientBatchWriteOperationsRemoveFacetFromObjectTypeDef,
        "AttachPolicy": ClientBatchWriteOperationsAttachPolicyTypeDef,
        "DetachPolicy": ClientBatchWriteOperationsDetachPolicyTypeDef,
        "CreateIndex": ClientBatchWriteOperationsCreateIndexTypeDef,
        "AttachToIndex": ClientBatchWriteOperationsAttachToIndexTypeDef,
        "DetachFromIndex": ClientBatchWriteOperationsDetachFromIndexTypeDef,
        "AttachTypedLink": ClientBatchWriteOperationsAttachTypedLinkTypeDef,
        "DetachTypedLink": ClientBatchWriteOperationsDetachTypedLinkTypeDef,
        "UpdateLinkAttributes": ClientBatchWriteOperationsUpdateLinkAttributesTypeDef,
    },
    total=False,
)


class ClientBatchWriteOperationsTypeDef(_ClientBatchWriteOperationsTypeDef):
    """
    Type definition for `ClientBatchWrite` `Operations`

    Represents the output of a ``BatchWrite`` operation.

    - **CreateObject** *(dict) --*

      Creates an object.

      - **SchemaFacet** *(list) --* **[REQUIRED]**

        A list of ``FacetArns`` that will be associated with the object. For more information, see
        arns .

        - *(dict) --*

          A facet.

          - **SchemaArn** *(string) --*

            The ARN of the schema that contains the facet with no minor component. See  arns and
            `In-Place Schema Upgrade
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
            for a description of when to provide minor versions.

          - **FacetName** *(string) --*

            The name of the facet.

      - **ObjectAttributeList** *(list) --* **[REQUIRED]**

        An attribute map, which contains an attribute ARN as the key and attribute value as the map
        value.

        - *(dict) --*

          The combination of an attribute key and an attribute value.

          - **Key** *(dict) --* **[REQUIRED]**

            The key of the attribute.

            - **SchemaArn** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

            - **FacetName** *(string) --* **[REQUIRED]**

              The name of the facet that the attribute exists within.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the attribute.

          - **Value** *(dict) --* **[REQUIRED]**

            The value of the attribute.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.

      - **ParentReference** *(dict) --*

        If specified, the parent reference to which this object will be attached.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **LinkName** *(string) --*

        The name of the link.

      - **BatchReferenceName** *(string) --*

        The batch reference name. See `Transaction Support
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/transaction_support.html>`__
        for more information.

    - **AttachObject** *(dict) --*

      Attaches an object to a  Directory .

      - **ParentReference** *(dict) --* **[REQUIRED]**

        The parent object reference.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **ChildReference** *(dict) --* **[REQUIRED]**

        The child object reference that is to be attached to the object.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **LinkName** *(string) --* **[REQUIRED]**

        The name of the link.

    - **DetachObject** *(dict) --*

      Detaches an object from a  Directory .

      - **ParentReference** *(dict) --* **[REQUIRED]**

        Parent reference from which the object with the specified link name is detached.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **LinkName** *(string) --* **[REQUIRED]**

        The name of the link.

      - **BatchReferenceName** *(string) --*

        The batch reference name. See `Transaction Support
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/transaction_support.html>`__
        for more information.

    - **UpdateObjectAttributes** *(dict) --*

      Updates a given object's attributes.

      - **ObjectReference** *(dict) --* **[REQUIRED]**

        Reference that identifies the object.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **AttributeUpdates** *(list) --* **[REQUIRED]**

        Attributes update structure.

        - *(dict) --*

          Structure that contains attribute update information.

          - **ObjectAttributeKey** *(dict) --*

            The key of the attribute being updated.

            - **SchemaArn** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

            - **FacetName** *(string) --* **[REQUIRED]**

              The name of the facet that the attribute exists within.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the attribute.

          - **ObjectAttributeAction** *(dict) --*

            The action to perform as part of the attribute update.

            - **ObjectAttributeActionType** *(string) --*

              A type that can be either ``Update`` or ``Delete`` .

            - **ObjectAttributeUpdateValue** *(dict) --*

              The value that you want to update to.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

    - **DeleteObject** *(dict) --*

      Deletes an object in a  Directory .

      - **ObjectReference** *(dict) --* **[REQUIRED]**

        The reference that identifies the object.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

    - **AddFacetToObject** *(dict) --*

      A batch operation that adds a facet to an object.

      - **SchemaFacet** *(dict) --* **[REQUIRED]**

        Represents the facet being added to the object.

        - **SchemaArn** *(string) --*

          The ARN of the schema that contains the facet with no minor component. See  arns and
          `In-Place Schema Upgrade
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
          for a description of when to provide minor versions.

        - **FacetName** *(string) --*

          The name of the facet.

      - **ObjectAttributeList** *(list) --* **[REQUIRED]**

        The attributes to set on the object.

        - *(dict) --*

          The combination of an attribute key and an attribute value.

          - **Key** *(dict) --* **[REQUIRED]**

            The key of the attribute.

            - **SchemaArn** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

            - **FacetName** *(string) --* **[REQUIRED]**

              The name of the facet that the attribute exists within.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the attribute.

          - **Value** *(dict) --* **[REQUIRED]**

            The value of the attribute.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.

      - **ObjectReference** *(dict) --* **[REQUIRED]**

        A reference to the object being mutated.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

    - **RemoveFacetFromObject** *(dict) --*

      A batch operation that removes a facet from an object.

      - **SchemaFacet** *(dict) --* **[REQUIRED]**

        The facet to remove from the object.

        - **SchemaArn** *(string) --*

          The ARN of the schema that contains the facet with no minor component. See  arns and
          `In-Place Schema Upgrade
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
          for a description of when to provide minor versions.

        - **FacetName** *(string) --*

          The name of the facet.

      - **ObjectReference** *(dict) --* **[REQUIRED]**

        A reference to the object whose facet will be removed.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

    - **AttachPolicy** *(dict) --*

      Attaches a policy object to a regular object. An object can have a limited number of attached
      policies.

      - **PolicyReference** *(dict) --* **[REQUIRED]**

        The reference that is associated with the policy object.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **ObjectReference** *(dict) --* **[REQUIRED]**

        The reference that identifies the object to which the policy will be attached.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

    - **DetachPolicy** *(dict) --*

      Detaches a policy from a  Directory .

      - **PolicyReference** *(dict) --* **[REQUIRED]**

        Reference that identifies the policy object.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **ObjectReference** *(dict) --* **[REQUIRED]**

        Reference that identifies the object whose policy object will be detached.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

    - **CreateIndex** *(dict) --*

      Creates an index object. See `Indexing and search
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search.htm>`__ for
      more information.

      - **OrderedIndexedAttributeList** *(list) --* **[REQUIRED]**

        Specifies the attributes that should be indexed on. Currently only a single attribute is
        supported.

        - *(dict) --*

          A unique identifier for an attribute.

          - **SchemaArn** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

          - **FacetName** *(string) --* **[REQUIRED]**

            The name of the facet that the attribute exists within.

          - **Name** *(string) --* **[REQUIRED]**

            The name of the attribute.

      - **IsUnique** *(boolean) --* **[REQUIRED]**

        Indicates whether the attribute that is being indexed has unique values or not.

      - **ParentReference** *(dict) --*

        A reference to the parent object that contains the index object.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **LinkName** *(string) --*

        The name of the link between the parent object and the index object.

      - **BatchReferenceName** *(string) --*

        The batch reference name. See `Transaction Support
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/transaction_support.html>`__
        for more information.

    - **AttachToIndex** *(dict) --*

      Attaches the specified object to the specified index.

      - **IndexReference** *(dict) --* **[REQUIRED]**

        A reference to the index that you are attaching the object to.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **TargetReference** *(dict) --* **[REQUIRED]**

        A reference to the object that you are attaching to the index.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

    - **DetachFromIndex** *(dict) --*

      Detaches the specified object from the specified index.

      - **IndexReference** *(dict) --* **[REQUIRED]**

        A reference to the index object.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **TargetReference** *(dict) --* **[REQUIRED]**

        A reference to the object being detached from the index.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

    - **AttachTypedLink** *(dict) --*

      Attaches a typed link to a specified source and target object. For more information, see
      `Typed Links
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
      .

      - **SourceObjectReference** *(dict) --* **[REQUIRED]**

        Identifies the source object that the typed link will attach to.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **TargetObjectReference** *(dict) --* **[REQUIRED]**

        Identifies the target object that the typed link will attach to.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links leading to
          it from the directory root. Use the link names from each parent/child link to construct
          the path. Path selectors start with a slash (/) and link names are separated by slashes.
          For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
          Directory. When creating objects, the system will provide you with the identifier of the
          created object. An object’s identifier is immutable and no two objects will ever share
          the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **TypedLinkFacet** *(dict) --* **[REQUIRED]**

        Identifies the typed link facet that is associated with the typed link.

        - **SchemaArn** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) that is associated with the schema. For more information,
          see  arns .

        - **TypedLinkName** *(string) --* **[REQUIRED]**

          The unique name of the typed link facet.

      - **Attributes** *(list) --* **[REQUIRED]**

        A set of attributes that are associated with the typed link.

        - *(dict) --*

          Identifies the attribute name and value for a typed link.

          - **AttributeName** *(string) --* **[REQUIRED]**

            The attribute name of the typed link.

          - **Value** *(dict) --* **[REQUIRED]**

            The value for the typed link.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.

    - **DetachTypedLink** *(dict) --*

      Detaches a typed link from a specified source and target object. For more information, see
      `Typed Links
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
      .

      - **TypedLinkSpecifier** *(dict) --* **[REQUIRED]**

        Used to accept a typed link specifier as input.

        - **TypedLinkFacet** *(dict) --* **[REQUIRED]**

          Identifies the typed link facet that is associated with the typed link.

          - **SchemaArn** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) that is associated with the schema. For more
            information, see  arns .

          - **TypedLinkName** *(string) --* **[REQUIRED]**

            The unique name of the typed link facet.

        - **SourceObjectReference** *(dict) --* **[REQUIRED]**

          Identifies the source object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links leading
            to it from the directory root. Use the link names from each parent/child link to
            construct the path. Path selectors start with a slash (/) and link names are separated
            by slashes. For more information about paths, see `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
            Cloud Directory. When creating objects, the system will provide you with the identifier
            of the created object. An object’s identifier is immutable and no two objects will ever
            share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **TargetObjectReference** *(dict) --* **[REQUIRED]**

          Identifies the target object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links leading
            to it from the directory root. Use the link names from each parent/child link to
            construct the path. Path selectors start with a slash (/) and link names are separated
            by slashes. For more information about paths, see `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
            Cloud Directory. When creating objects, the system will provide you with the identifier
            of the created object. An object’s identifier is immutable and no two objects will ever
            share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **IdentityAttributeValues** *(list) --* **[REQUIRED]**

          Identifies the attribute value to update.

          - *(dict) --*

            Identifies the attribute name and value for a typed link.

            - **AttributeName** *(string) --* **[REQUIRED]**

              The attribute name of the typed link.

            - **Value** *(dict) --* **[REQUIRED]**

              The value for the typed link.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

    - **UpdateLinkAttributes** *(dict) --*

      Updates a given object's attributes.

      - **TypedLinkSpecifier** *(dict) --* **[REQUIRED]**

        Allows a typed link specifier to be accepted as input.

        - **TypedLinkFacet** *(dict) --* **[REQUIRED]**

          Identifies the typed link facet that is associated with the typed link.

          - **SchemaArn** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) that is associated with the schema. For more
            information, see  arns .

          - **TypedLinkName** *(string) --* **[REQUIRED]**

            The unique name of the typed link facet.

        - **SourceObjectReference** *(dict) --* **[REQUIRED]**

          Identifies the source object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links leading
            to it from the directory root. Use the link names from each parent/child link to
            construct the path. Path selectors start with a slash (/) and link names are separated
            by slashes. For more information about paths, see `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
            Cloud Directory. When creating objects, the system will provide you with the identifier
            of the created object. An object’s identifier is immutable and no two objects will ever
            share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **TargetObjectReference** *(dict) --* **[REQUIRED]**

          Identifies the target object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links leading
            to it from the directory root. Use the link names from each parent/child link to
            construct the path. Path selectors start with a slash (/) and link names are separated
            by slashes. For more information about paths, see `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
            Cloud Directory. When creating objects, the system will provide you with the identifier
            of the created object. An object’s identifier is immutable and no two objects will ever
            share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **IdentityAttributeValues** *(list) --* **[REQUIRED]**

          Identifies the attribute value to update.

          - *(dict) --*

            Identifies the attribute name and value for a typed link.

            - **AttributeName** *(string) --* **[REQUIRED]**

              The attribute name of the typed link.

            - **Value** *(dict) --* **[REQUIRED]**

              The value for the typed link.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

      - **AttributeUpdates** *(list) --* **[REQUIRED]**

        The attributes update structure.

        - *(dict) --*

          Structure that contains attribute update information.

          - **AttributeKey** *(dict) --*

            The key of the attribute being updated.

            - **SchemaArn** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

            - **FacetName** *(string) --* **[REQUIRED]**

              The name of the facet that the attribute exists within.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the attribute.

          - **AttributeAction** *(dict) --*

            The action to perform as part of the attribute update.

            - **AttributeActionType** *(string) --*

              A type that can be either ``UPDATE_OR_CREATE`` or ``DELETE`` .

            - **AttributeUpdateValue** *(dict) --*

              The value that you want to update to.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.
    """


_ClientBatchWriteResponseResponsesAttachObjectTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesAttachObjectTypeDef",
    {"attachedObjectIdentifier": str},
    total=False,
)


class ClientBatchWriteResponseResponsesAttachObjectTypeDef(
    _ClientBatchWriteResponseResponsesAttachObjectTypeDef
):
    """
    Type definition for `ClientBatchWriteResponseResponses` `AttachObject`

    Attaches an object to a  Directory .

    - **attachedObjectIdentifier** *(string) --*

      The ``ObjectIdentifier`` of the object that has been attached.
    """


_ClientBatchWriteResponseResponsesAttachToIndexTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesAttachToIndexTypeDef",
    {"AttachedObjectIdentifier": str},
    total=False,
)


class ClientBatchWriteResponseResponsesAttachToIndexTypeDef(
    _ClientBatchWriteResponseResponsesAttachToIndexTypeDef
):
    """
    Type definition for `ClientBatchWriteResponseResponses` `AttachToIndex`

    Attaches the specified object to the specified index.

    - **AttachedObjectIdentifier** *(string) --*

      The ``ObjectIdentifier`` of the object that was attached to the index.
    """


_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef(
    _ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef
):
    """
    Type definition for `ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValues` `Value`

    The value for the typed link.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef(
    _ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef
):
    """
    Type definition for `ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifier` `IdentityAttributeValues`

    Identifies the attribute name and value for a typed link.

    - **AttributeName** *(string) --*

      The attribute name of the typed link.

    - **Value** *(dict) --*

      The value for the typed link.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef(
    _ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifier` `SourceObjectReference`

    Identifies the source object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links
      leading to it from the directory root. Use the link names from each parent/child
      link to construct the path. Path selectors start with a slash (/) and link names
      are separated by slashes. For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
      Cloud Directory. When creating objects, the system will provide you with the
      identifier of the created object. An object’s identifier is immutable and no two
      objects will ever share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef(
    _ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef
):
    """
    Type definition for `ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifier` `TargetObjectReference`

    Identifies the target object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links
      leading to it from the directory root. Use the link names from each parent/child
      link to construct the path. Path selectors start with a slash (/) and link names
      are separated by slashes. For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
      Cloud Directory. When creating objects, the system will provide you with the
      identifier of the created object. An object’s identifier is immutable and no two
      objects will ever share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef(
    _ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef
):
    """
    Type definition for `ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifier` `TypedLinkFacet`

    Identifies the typed link facet that is associated with the typed link.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) that is associated with the schema. For more
      information, see  arns .

    - **TypedLinkName** *(string) --*

      The unique name of the typed link facet.
    """


_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypeDef(
    _ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypeDef
):
    """
    Type definition for `ClientBatchWriteResponseResponsesAttachTypedLink` `TypedLinkSpecifier`

    Returns a typed link specifier as output.

    - **TypedLinkFacet** *(dict) --*

      Identifies the typed link facet that is associated with the typed link.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) that is associated with the schema. For more
        information, see  arns .

      - **TypedLinkName** *(string) --*

        The unique name of the typed link facet.

    - **SourceObjectReference** *(dict) --*

      Identifies the source object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links
        leading to it from the directory root. Use the link names from each parent/child
        link to construct the path. Path selectors start with a slash (/) and link names
        are separated by slashes. For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
        Cloud Directory. When creating objects, the system will provide you with the
        identifier of the created object. An object’s identifier is immutable and no two
        objects will ever share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **TargetObjectReference** *(dict) --*

      Identifies the target object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links
        leading to it from the directory root. Use the link names from each parent/child
        link to construct the path. Path selectors start with a slash (/) and link names
        are separated by slashes. For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
        Cloud Directory. When creating objects, the system will provide you with the
        identifier of the created object. An object’s identifier is immutable and no two
        objects will ever share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **IdentityAttributeValues** *(list) --*

      Identifies the attribute value to update.

      - *(dict) --*

        Identifies the attribute name and value for a typed link.

        - **AttributeName** *(string) --*

          The attribute name of the typed link.

        - **Value** *(dict) --*

          The value for the typed link.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ClientBatchWriteResponseResponsesAttachTypedLinkTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesAttachTypedLinkTypeDef",
    {
        "TypedLinkSpecifier": ClientBatchWriteResponseResponsesAttachTypedLinkTypedLinkSpecifierTypeDef
    },
    total=False,
)


class ClientBatchWriteResponseResponsesAttachTypedLinkTypeDef(
    _ClientBatchWriteResponseResponsesAttachTypedLinkTypeDef
):
    """
    Type definition for `ClientBatchWriteResponseResponses` `AttachTypedLink`

    Attaches a typed link to a specified source and target object. For more information, see
    `Typed Links
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
    .

    - **TypedLinkSpecifier** *(dict) --*

      Returns a typed link specifier as output.

      - **TypedLinkFacet** *(dict) --*

        Identifies the typed link facet that is associated with the typed link.

        - **SchemaArn** *(string) --*

          The Amazon Resource Name (ARN) that is associated with the schema. For more
          information, see  arns .

        - **TypedLinkName** *(string) --*

          The unique name of the typed link facet.

      - **SourceObjectReference** *(dict) --*

        Identifies the source object that the typed link will attach to.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links
          leading to it from the directory root. Use the link names from each parent/child
          link to construct the path. Path selectors start with a slash (/) and link names
          are separated by slashes. For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
          Cloud Directory. When creating objects, the system will provide you with the
          identifier of the created object. An object’s identifier is immutable and no two
          objects will ever share the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **TargetObjectReference** *(dict) --*

        Identifies the target object that the typed link will attach to.

        - **Selector** *(string) --*

          A path selector supports easy selection of an object by the parent/child links
          leading to it from the directory root. Use the link names from each parent/child
          link to construct the path. Path selectors start with a slash (/) and link names
          are separated by slashes. For more information about paths, see `Access Objects
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
          . You can identify an object in one of the following ways:

          * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
          Cloud Directory. When creating objects, the system will provide you with the
          identifier of the created object. An object’s identifier is immutable and no two
          objects will ever share the same object identifier

          * */some/path* - Identifies the object based on path

          * *#SomeBatchReference* - Identifies the object in a batch call

      - **IdentityAttributeValues** *(list) --*

        Identifies the attribute value to update.

        - *(dict) --*

          Identifies the attribute name and value for a typed link.

          - **AttributeName** *(string) --*

            The attribute name of the typed link.

          - **Value** *(dict) --*

            The value for the typed link.

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.
    """


_ClientBatchWriteResponseResponsesCreateIndexTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesCreateIndexTypeDef",
    {"ObjectIdentifier": str},
    total=False,
)


class ClientBatchWriteResponseResponsesCreateIndexTypeDef(
    _ClientBatchWriteResponseResponsesCreateIndexTypeDef
):
    """
    Type definition for `ClientBatchWriteResponseResponses` `CreateIndex`

    Creates an index object. See `Indexing and search
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search.htm>`__
    for more information.

    - **ObjectIdentifier** *(string) --*

      The ``ObjectIdentifier`` of the index created by this operation.
    """


_ClientBatchWriteResponseResponsesCreateObjectTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesCreateObjectTypeDef",
    {"ObjectIdentifier": str},
    total=False,
)


class ClientBatchWriteResponseResponsesCreateObjectTypeDef(
    _ClientBatchWriteResponseResponsesCreateObjectTypeDef
):
    """
    Type definition for `ClientBatchWriteResponseResponses` `CreateObject`

    Creates an object in a  Directory .

    - **ObjectIdentifier** *(string) --*

      The ID that is associated with the object.
    """


_ClientBatchWriteResponseResponsesDetachFromIndexTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesDetachFromIndexTypeDef",
    {"DetachedObjectIdentifier": str},
    total=False,
)


class ClientBatchWriteResponseResponsesDetachFromIndexTypeDef(
    _ClientBatchWriteResponseResponsesDetachFromIndexTypeDef
):
    """
    Type definition for `ClientBatchWriteResponseResponses` `DetachFromIndex`

    Detaches the specified object from the specified index.

    - **DetachedObjectIdentifier** *(string) --*

      The ``ObjectIdentifier`` of the object that was detached from the index.
    """


_ClientBatchWriteResponseResponsesDetachObjectTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesDetachObjectTypeDef",
    {"detachedObjectIdentifier": str},
    total=False,
)


class ClientBatchWriteResponseResponsesDetachObjectTypeDef(
    _ClientBatchWriteResponseResponsesDetachObjectTypeDef
):
    """
    Type definition for `ClientBatchWriteResponseResponses` `DetachObject`

    Detaches an object from a  Directory .

    - **detachedObjectIdentifier** *(string) --*

      The ``ObjectIdentifier`` of the detached object.
    """


_ClientBatchWriteResponseResponsesUpdateObjectAttributesTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesUpdateObjectAttributesTypeDef",
    {"ObjectIdentifier": str},
    total=False,
)


class ClientBatchWriteResponseResponsesUpdateObjectAttributesTypeDef(
    _ClientBatchWriteResponseResponsesUpdateObjectAttributesTypeDef
):
    """
    Type definition for `ClientBatchWriteResponseResponses` `UpdateObjectAttributes`

    Updates a given object’s attributes.

    - **ObjectIdentifier** *(string) --*

      ID that is associated with the object.
    """


_ClientBatchWriteResponseResponsesTypeDef = TypedDict(
    "_ClientBatchWriteResponseResponsesTypeDef",
    {
        "CreateObject": ClientBatchWriteResponseResponsesCreateObjectTypeDef,
        "AttachObject": ClientBatchWriteResponseResponsesAttachObjectTypeDef,
        "DetachObject": ClientBatchWriteResponseResponsesDetachObjectTypeDef,
        "UpdateObjectAttributes": ClientBatchWriteResponseResponsesUpdateObjectAttributesTypeDef,
        "DeleteObject": Dict,
        "AddFacetToObject": Dict,
        "RemoveFacetFromObject": Dict,
        "AttachPolicy": Dict,
        "DetachPolicy": Dict,
        "CreateIndex": ClientBatchWriteResponseResponsesCreateIndexTypeDef,
        "AttachToIndex": ClientBatchWriteResponseResponsesAttachToIndexTypeDef,
        "DetachFromIndex": ClientBatchWriteResponseResponsesDetachFromIndexTypeDef,
        "AttachTypedLink": ClientBatchWriteResponseResponsesAttachTypedLinkTypeDef,
        "DetachTypedLink": Dict,
        "UpdateLinkAttributes": Dict,
    },
    total=False,
)


class ClientBatchWriteResponseResponsesTypeDef(
    _ClientBatchWriteResponseResponsesTypeDef
):
    """
    Type definition for `ClientBatchWriteResponse` `Responses`

    Represents the output of a ``BatchWrite`` response operation.

    - **CreateObject** *(dict) --*

      Creates an object in a  Directory .

      - **ObjectIdentifier** *(string) --*

        The ID that is associated with the object.

    - **AttachObject** *(dict) --*

      Attaches an object to a  Directory .

      - **attachedObjectIdentifier** *(string) --*

        The ``ObjectIdentifier`` of the object that has been attached.

    - **DetachObject** *(dict) --*

      Detaches an object from a  Directory .

      - **detachedObjectIdentifier** *(string) --*

        The ``ObjectIdentifier`` of the detached object.

    - **UpdateObjectAttributes** *(dict) --*

      Updates a given object’s attributes.

      - **ObjectIdentifier** *(string) --*

        ID that is associated with the object.

    - **DeleteObject** *(dict) --*

      Deletes an object in a  Directory .

    - **AddFacetToObject** *(dict) --*

      The result of an add facet to object batch operation.

    - **RemoveFacetFromObject** *(dict) --*

      The result of a batch remove facet from object operation.

    - **AttachPolicy** *(dict) --*

      Attaches a policy object to a regular object. An object can have a limited number of
      attached policies.

    - **DetachPolicy** *(dict) --*

      Detaches a policy from a  Directory .

    - **CreateIndex** *(dict) --*

      Creates an index object. See `Indexing and search
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search.htm>`__
      for more information.

      - **ObjectIdentifier** *(string) --*

        The ``ObjectIdentifier`` of the index created by this operation.

    - **AttachToIndex** *(dict) --*

      Attaches the specified object to the specified index.

      - **AttachedObjectIdentifier** *(string) --*

        The ``ObjectIdentifier`` of the object that was attached to the index.

    - **DetachFromIndex** *(dict) --*

      Detaches the specified object from the specified index.

      - **DetachedObjectIdentifier** *(string) --*

        The ``ObjectIdentifier`` of the object that was detached from the index.

    - **AttachTypedLink** *(dict) --*

      Attaches a typed link to a specified source and target object. For more information, see
      `Typed Links
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
      .

      - **TypedLinkSpecifier** *(dict) --*

        Returns a typed link specifier as output.

        - **TypedLinkFacet** *(dict) --*

          Identifies the typed link facet that is associated with the typed link.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) that is associated with the schema. For more
            information, see  arns .

          - **TypedLinkName** *(string) --*

            The unique name of the typed link facet.

        - **SourceObjectReference** *(dict) --*

          Identifies the source object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links
            leading to it from the directory root. Use the link names from each parent/child
            link to construct the path. Path selectors start with a slash (/) and link names
            are separated by slashes. For more information about paths, see `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
            Cloud Directory. When creating objects, the system will provide you with the
            identifier of the created object. An object’s identifier is immutable and no two
            objects will ever share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **TargetObjectReference** *(dict) --*

          Identifies the target object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links
            leading to it from the directory root. Use the link names from each parent/child
            link to construct the path. Path selectors start with a slash (/) and link names
            are separated by slashes. For more information about paths, see `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
            Cloud Directory. When creating objects, the system will provide you with the
            identifier of the created object. An object’s identifier is immutable and no two
            objects will ever share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **IdentityAttributeValues** *(list) --*

          Identifies the attribute value to update.

          - *(dict) --*

            Identifies the attribute name and value for a typed link.

            - **AttributeName** *(string) --*

              The attribute name of the typed link.

            - **Value** *(dict) --*

              The value for the typed link.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

    - **DetachTypedLink** *(dict) --*

      Detaches a typed link from a specified source and target object. For more information,
      see `Typed Links
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
      .

    - **UpdateLinkAttributes** *(dict) --*

      Represents the output of a ``BatchWrite`` response operation.
    """


_ClientBatchWriteResponseTypeDef = TypedDict(
    "_ClientBatchWriteResponseTypeDef",
    {"Responses": List[ClientBatchWriteResponseResponsesTypeDef]},
    total=False,
)


class ClientBatchWriteResponseTypeDef(_ClientBatchWriteResponseTypeDef):
    """
    Type definition for `ClientBatchWrite` `Response`

    - **Responses** *(list) --*

      A list of all the responses for each batch write.

      - *(dict) --*

        Represents the output of a ``BatchWrite`` response operation.

        - **CreateObject** *(dict) --*

          Creates an object in a  Directory .

          - **ObjectIdentifier** *(string) --*

            The ID that is associated with the object.

        - **AttachObject** *(dict) --*

          Attaches an object to a  Directory .

          - **attachedObjectIdentifier** *(string) --*

            The ``ObjectIdentifier`` of the object that has been attached.

        - **DetachObject** *(dict) --*

          Detaches an object from a  Directory .

          - **detachedObjectIdentifier** *(string) --*

            The ``ObjectIdentifier`` of the detached object.

        - **UpdateObjectAttributes** *(dict) --*

          Updates a given object’s attributes.

          - **ObjectIdentifier** *(string) --*

            ID that is associated with the object.

        - **DeleteObject** *(dict) --*

          Deletes an object in a  Directory .

        - **AddFacetToObject** *(dict) --*

          The result of an add facet to object batch operation.

        - **RemoveFacetFromObject** *(dict) --*

          The result of a batch remove facet from object operation.

        - **AttachPolicy** *(dict) --*

          Attaches a policy object to a regular object. An object can have a limited number of
          attached policies.

        - **DetachPolicy** *(dict) --*

          Detaches a policy from a  Directory .

        - **CreateIndex** *(dict) --*

          Creates an index object. See `Indexing and search
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search.htm>`__
          for more information.

          - **ObjectIdentifier** *(string) --*

            The ``ObjectIdentifier`` of the index created by this operation.

        - **AttachToIndex** *(dict) --*

          Attaches the specified object to the specified index.

          - **AttachedObjectIdentifier** *(string) --*

            The ``ObjectIdentifier`` of the object that was attached to the index.

        - **DetachFromIndex** *(dict) --*

          Detaches the specified object from the specified index.

          - **DetachedObjectIdentifier** *(string) --*

            The ``ObjectIdentifier`` of the object that was detached from the index.

        - **AttachTypedLink** *(dict) --*

          Attaches a typed link to a specified source and target object. For more information, see
          `Typed Links
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
          .

          - **TypedLinkSpecifier** *(dict) --*

            Returns a typed link specifier as output.

            - **TypedLinkFacet** *(dict) --*

              Identifies the typed link facet that is associated with the typed link.

              - **SchemaArn** *(string) --*

                The Amazon Resource Name (ARN) that is associated with the schema. For more
                information, see  arns .

              - **TypedLinkName** *(string) --*

                The unique name of the typed link facet.

            - **SourceObjectReference** *(dict) --*

              Identifies the source object that the typed link will attach to.

              - **Selector** *(string) --*

                A path selector supports easy selection of an object by the parent/child links
                leading to it from the directory root. Use the link names from each parent/child
                link to construct the path. Path selectors start with a slash (/) and link names
                are separated by slashes. For more information about paths, see `Access Objects
                <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
                . You can identify an object in one of the following ways:

                * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
                Cloud Directory. When creating objects, the system will provide you with the
                identifier of the created object. An object’s identifier is immutable and no two
                objects will ever share the same object identifier

                * */some/path* - Identifies the object based on path

                * *#SomeBatchReference* - Identifies the object in a batch call

            - **TargetObjectReference** *(dict) --*

              Identifies the target object that the typed link will attach to.

              - **Selector** *(string) --*

                A path selector supports easy selection of an object by the parent/child links
                leading to it from the directory root. Use the link names from each parent/child
                link to construct the path. Path selectors start with a slash (/) and link names
                are separated by slashes. For more information about paths, see `Access Objects
                <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
                . You can identify an object in one of the following ways:

                * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
                Cloud Directory. When creating objects, the system will provide you with the
                identifier of the created object. An object’s identifier is immutable and no two
                objects will ever share the same object identifier

                * */some/path* - Identifies the object based on path

                * *#SomeBatchReference* - Identifies the object in a batch call

            - **IdentityAttributeValues** *(list) --*

              Identifies the attribute value to update.

              - *(dict) --*

                Identifies the attribute name and value for a typed link.

                - **AttributeName** *(string) --*

                  The attribute name of the typed link.

                - **Value** *(dict) --*

                  The value for the typed link.

                  - **StringValue** *(string) --*

                    A string data value.

                  - **BinaryValue** *(bytes) --*

                    A binary data value.

                  - **BooleanValue** *(boolean) --*

                    A Boolean data value.

                  - **NumberValue** *(string) --*

                    A number data value.

                  - **DatetimeValue** *(datetime) --*

                    A date and time value.

        - **DetachTypedLink** *(dict) --*

          Detaches a typed link from a specified source and target object. For more information,
          see `Typed Links
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
          .

        - **UpdateLinkAttributes** *(dict) --*

          Represents the output of a ``BatchWrite`` response operation.
    """


_ClientCreateDirectoryResponseTypeDef = TypedDict(
    "_ClientCreateDirectoryResponseTypeDef",
    {
        "DirectoryArn": str,
        "Name": str,
        "ObjectIdentifier": str,
        "AppliedSchemaArn": str,
    },
    total=False,
)


class ClientCreateDirectoryResponseTypeDef(_ClientCreateDirectoryResponseTypeDef):
    """
    Type definition for `ClientCreateDirectory` `Response`

    - **DirectoryArn** *(string) --*

      The ARN that is associated with the  Directory . For more information, see  arns .

    - **Name** *(string) --*

      The name of the  Directory .

    - **ObjectIdentifier** *(string) --*

      The root object node of the created directory.

    - **AppliedSchemaArn** *(string) --*

      The ARN of the published schema in the  Directory . Once a published schema is copied into
      the directory, it has its own ARN, which is referred to applied schema ARN. For more
      information, see  arns .
    """


_ClientCreateFacetAttributesAttributeDefinitionDefaultValueTypeDef = TypedDict(
    "_ClientCreateFacetAttributesAttributeDefinitionDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientCreateFacetAttributesAttributeDefinitionDefaultValueTypeDef(
    _ClientCreateFacetAttributesAttributeDefinitionDefaultValueTypeDef
):
    """
    Type definition for `ClientCreateFacetAttributesAttributeDefinition` `DefaultValue`

    The default value of the attribute (if configured).

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientCreateFacetAttributesAttributeDefinitionRulesTypeDef = TypedDict(
    "_ClientCreateFacetAttributesAttributeDefinitionRulesTypeDef",
    {"Type": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientCreateFacetAttributesAttributeDefinitionRulesTypeDef(
    _ClientCreateFacetAttributesAttributeDefinitionRulesTypeDef
):
    """
    Type definition for `ClientCreateFacetAttributesAttributeDefinition` `Rules`

    Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.

    - **Type** *(string) --*

      The type of attribute validation rule.

    - **Parameters** *(dict) --*

      The minimum and maximum parameters that are associated with the rule.

      - *(string) --*

        - *(string) --*
    """


_RequiredClientCreateFacetAttributesAttributeDefinitionTypeDef = TypedDict(
    "_RequiredClientCreateFacetAttributesAttributeDefinitionTypeDef", {"Type": str}
)
_OptionalClientCreateFacetAttributesAttributeDefinitionTypeDef = TypedDict(
    "_OptionalClientCreateFacetAttributesAttributeDefinitionTypeDef",
    {
        "DefaultValue": ClientCreateFacetAttributesAttributeDefinitionDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[str, ClientCreateFacetAttributesAttributeDefinitionRulesTypeDef],
    },
    total=False,
)


class ClientCreateFacetAttributesAttributeDefinitionTypeDef(
    _RequiredClientCreateFacetAttributesAttributeDefinitionTypeDef,
    _OptionalClientCreateFacetAttributesAttributeDefinitionTypeDef,
):
    """
    Type definition for `ClientCreateFacetAttributes` `AttributeDefinition`

    A facet attribute consists of either a definition or a reference. This structure contains the
    attribute definition. See `Attribute References
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
    for more information.

    - **Type** *(string) --* **[REQUIRED]**

      The type of the attribute.

    - **DefaultValue** *(dict) --*

      The default value of the attribute (if configured).

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.

    - **IsImmutable** *(boolean) --*

      Whether the attribute is mutable or not.

    - **Rules** *(dict) --*

      Validation rules attached to the attribute definition.

      - *(string) --*

        - *(dict) --*

          Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.

          - **Type** *(string) --*

            The type of attribute validation rule.

          - **Parameters** *(dict) --*

            The minimum and maximum parameters that are associated with the rule.

            - *(string) --*

              - *(string) --*
    """


_ClientCreateFacetAttributesAttributeReferenceTypeDef = TypedDict(
    "_ClientCreateFacetAttributesAttributeReferenceTypeDef",
    {"TargetFacetName": str, "TargetAttributeName": str},
)


class ClientCreateFacetAttributesAttributeReferenceTypeDef(
    _ClientCreateFacetAttributesAttributeReferenceTypeDef
):
    """
    Type definition for `ClientCreateFacetAttributes` `AttributeReference`

    An attribute reference that is associated with the attribute. See `Attribute References
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
    for more information.

    - **TargetFacetName** *(string) --* **[REQUIRED]**

      The target facet name that is associated with the facet reference. See `Attribute
      References
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
      for more information.

    - **TargetAttributeName** *(string) --* **[REQUIRED]**

      The target attribute name that is associated with the facet reference. See `Attribute
      References
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
      for more information.
    """


_RequiredClientCreateFacetAttributesTypeDef = TypedDict(
    "_RequiredClientCreateFacetAttributesTypeDef", {"Name": str}
)
_OptionalClientCreateFacetAttributesTypeDef = TypedDict(
    "_OptionalClientCreateFacetAttributesTypeDef",
    {
        "AttributeDefinition": ClientCreateFacetAttributesAttributeDefinitionTypeDef,
        "AttributeReference": ClientCreateFacetAttributesAttributeReferenceTypeDef,
        "RequiredBehavior": str,
    },
    total=False,
)


class ClientCreateFacetAttributesTypeDef(
    _RequiredClientCreateFacetAttributesTypeDef,
    _OptionalClientCreateFacetAttributesTypeDef,
):
    """
    Type definition for `ClientCreateFacet` `Attributes`

    An attribute that is associated with the  Facet .

    - **Name** *(string) --* **[REQUIRED]**

      The name of the facet attribute.

    - **AttributeDefinition** *(dict) --*

      A facet attribute consists of either a definition or a reference. This structure contains the
      attribute definition. See `Attribute References
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
      for more information.

      - **Type** *(string) --* **[REQUIRED]**

        The type of the attribute.

      - **DefaultValue** *(dict) --*

        The default value of the attribute (if configured).

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.

      - **IsImmutable** *(boolean) --*

        Whether the attribute is mutable or not.

      - **Rules** *(dict) --*

        Validation rules attached to the attribute definition.

        - *(string) --*

          - *(dict) --*

            Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.

            - **Type** *(string) --*

              The type of attribute validation rule.

            - **Parameters** *(dict) --*

              The minimum and maximum parameters that are associated with the rule.

              - *(string) --*

                - *(string) --*

    - **AttributeReference** *(dict) --*

      An attribute reference that is associated with the attribute. See `Attribute References
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
      for more information.

      - **TargetFacetName** *(string) --* **[REQUIRED]**

        The target facet name that is associated with the facet reference. See `Attribute
        References
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
        for more information.

      - **TargetAttributeName** *(string) --* **[REQUIRED]**

        The target attribute name that is associated with the facet reference. See `Attribute
        References
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
        for more information.

    - **RequiredBehavior** *(string) --*

      The required behavior of the ``FacetAttribute`` .
    """


_ClientCreateIndexOrderedIndexedAttributeListTypeDef = TypedDict(
    "_ClientCreateIndexOrderedIndexedAttributeListTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
)


class ClientCreateIndexOrderedIndexedAttributeListTypeDef(
    _ClientCreateIndexOrderedIndexedAttributeListTypeDef
):
    """
    Type definition for `ClientCreateIndex` `OrderedIndexedAttributeList`

    A unique identifier for an attribute.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --* **[REQUIRED]**

      The name of the facet that the attribute exists within.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.
    """


_ClientCreateIndexParentReferenceTypeDef = TypedDict(
    "_ClientCreateIndexParentReferenceTypeDef", {"Selector": str}, total=False
)


class ClientCreateIndexParentReferenceTypeDef(_ClientCreateIndexParentReferenceTypeDef):
    """
    Type definition for `ClientCreateIndex` `ParentReference`

    A reference to the parent object that contains the index object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientCreateIndexResponseTypeDef = TypedDict(
    "_ClientCreateIndexResponseTypeDef", {"ObjectIdentifier": str}, total=False
)


class ClientCreateIndexResponseTypeDef(_ClientCreateIndexResponseTypeDef):
    """
    Type definition for `ClientCreateIndex` `Response`

    - **ObjectIdentifier** *(string) --*

      The ``ObjectIdentifier`` of the index created by this operation.
    """


_ClientCreateObjectObjectAttributeListKeyTypeDef = TypedDict(
    "_ClientCreateObjectObjectAttributeListKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
)


class ClientCreateObjectObjectAttributeListKeyTypeDef(
    _ClientCreateObjectObjectAttributeListKeyTypeDef
):
    """
    Type definition for `ClientCreateObjectObjectAttributeList` `Key`

    The key of the attribute.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --* **[REQUIRED]**

      The name of the facet that the attribute exists within.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.
    """


_ClientCreateObjectObjectAttributeListValueTypeDef = TypedDict(
    "_ClientCreateObjectObjectAttributeListValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientCreateObjectObjectAttributeListValueTypeDef(
    _ClientCreateObjectObjectAttributeListValueTypeDef
):
    """
    Type definition for `ClientCreateObjectObjectAttributeList` `Value`

    The value of the attribute.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientCreateObjectObjectAttributeListTypeDef = TypedDict(
    "_ClientCreateObjectObjectAttributeListTypeDef",
    {
        "Key": ClientCreateObjectObjectAttributeListKeyTypeDef,
        "Value": ClientCreateObjectObjectAttributeListValueTypeDef,
    },
)


class ClientCreateObjectObjectAttributeListTypeDef(
    _ClientCreateObjectObjectAttributeListTypeDef
):
    """
    Type definition for `ClientCreateObject` `ObjectAttributeList`

    The combination of an attribute key and an attribute value.

    - **Key** *(dict) --* **[REQUIRED]**

      The key of the attribute.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --* **[REQUIRED]**

        The name of the facet that the attribute exists within.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the attribute.

    - **Value** *(dict) --* **[REQUIRED]**

      The value of the attribute.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientCreateObjectParentReferenceTypeDef = TypedDict(
    "_ClientCreateObjectParentReferenceTypeDef", {"Selector": str}, total=False
)


class ClientCreateObjectParentReferenceTypeDef(
    _ClientCreateObjectParentReferenceTypeDef
):
    """
    Type definition for `ClientCreateObject` `ParentReference`

    If specified, the parent reference to which this object will be attached.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientCreateObjectResponseTypeDef = TypedDict(
    "_ClientCreateObjectResponseTypeDef", {"ObjectIdentifier": str}, total=False
)


class ClientCreateObjectResponseTypeDef(_ClientCreateObjectResponseTypeDef):
    """
    Type definition for `ClientCreateObject` `Response`

    - **ObjectIdentifier** *(string) --*

      The identifier that is associated with the object.
    """


_ClientCreateObjectSchemaFacetsTypeDef = TypedDict(
    "_ClientCreateObjectSchemaFacetsTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientCreateObjectSchemaFacetsTypeDef(_ClientCreateObjectSchemaFacetsTypeDef):
    """
    Type definition for `ClientCreateObject` `SchemaFacets`

    A facet.

    - **SchemaArn** *(string) --*

      The ARN of the schema that contains the facet with no minor component. See  arns and
      `In-Place Schema Upgrade
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
      for a description of when to provide minor versions.

    - **FacetName** *(string) --*

      The name of the facet.
    """


_ClientCreateSchemaResponseTypeDef = TypedDict(
    "_ClientCreateSchemaResponseTypeDef", {"SchemaArn": str}, total=False
)


class ClientCreateSchemaResponseTypeDef(_ClientCreateSchemaResponseTypeDef):
    """
    Type definition for `ClientCreateSchema` `Response`

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
      arns .
    """


_ClientCreateTypedLinkFacetFacetAttributesDefaultValueTypeDef = TypedDict(
    "_ClientCreateTypedLinkFacetFacetAttributesDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientCreateTypedLinkFacetFacetAttributesDefaultValueTypeDef(
    _ClientCreateTypedLinkFacetFacetAttributesDefaultValueTypeDef
):
    """
    Type definition for `ClientCreateTypedLinkFacetFacetAttributes` `DefaultValue`

    The default value of the attribute (if configured).

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientCreateTypedLinkFacetFacetAttributesRulesTypeDef = TypedDict(
    "_ClientCreateTypedLinkFacetFacetAttributesRulesTypeDef",
    {"Type": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientCreateTypedLinkFacetFacetAttributesRulesTypeDef(
    _ClientCreateTypedLinkFacetFacetAttributesRulesTypeDef
):
    """
    Type definition for `ClientCreateTypedLinkFacetFacetAttributes` `Rules`

    Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.

    - **Type** *(string) --*

      The type of attribute validation rule.

    - **Parameters** *(dict) --*

      The minimum and maximum parameters that are associated with the rule.

      - *(string) --*

        - *(string) --*
    """


_RequiredClientCreateTypedLinkFacetFacetAttributesTypeDef = TypedDict(
    "_RequiredClientCreateTypedLinkFacetFacetAttributesTypeDef",
    {"Name": str, "Type": str, "RequiredBehavior": str},
)
_OptionalClientCreateTypedLinkFacetFacetAttributesTypeDef = TypedDict(
    "_OptionalClientCreateTypedLinkFacetFacetAttributesTypeDef",
    {
        "DefaultValue": ClientCreateTypedLinkFacetFacetAttributesDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[str, ClientCreateTypedLinkFacetFacetAttributesRulesTypeDef],
    },
    total=False,
)


class ClientCreateTypedLinkFacetFacetAttributesTypeDef(
    _RequiredClientCreateTypedLinkFacetFacetAttributesTypeDef,
    _OptionalClientCreateTypedLinkFacetFacetAttributesTypeDef,
):
    """
    Type definition for `ClientCreateTypedLinkFacetFacet` `Attributes`

    A typed link attribute definition.

    - **Name** *(string) --* **[REQUIRED]**

      The unique name of the typed link attribute.

    - **Type** *(string) --* **[REQUIRED]**

      The type of the attribute.

    - **DefaultValue** *(dict) --*

      The default value of the attribute (if configured).

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.

    - **IsImmutable** *(boolean) --*

      Whether the attribute is mutable or not.

    - **Rules** *(dict) --*

      Validation rules that are attached to the attribute definition.

      - *(string) --*

        - *(dict) --*

          Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.

          - **Type** *(string) --*

            The type of attribute validation rule.

          - **Parameters** *(dict) --*

            The minimum and maximum parameters that are associated with the rule.

            - *(string) --*

              - *(string) --*

    - **RequiredBehavior** *(string) --* **[REQUIRED]**

      The required behavior of the ``TypedLinkAttributeDefinition`` .
    """


_ClientCreateTypedLinkFacetFacetTypeDef = TypedDict(
    "_ClientCreateTypedLinkFacetFacetTypeDef",
    {
        "Name": str,
        "Attributes": List[ClientCreateTypedLinkFacetFacetAttributesTypeDef],
        "IdentityAttributeOrder": List[str],
    },
)


class ClientCreateTypedLinkFacetFacetTypeDef(_ClientCreateTypedLinkFacetFacetTypeDef):
    """
    Type definition for `ClientCreateTypedLinkFacet` `Facet`

      Facet structure that is associated with the typed link facet.

    - **Name** *(string) --* **[REQUIRED]**

      The unique name of the typed link facet.

    - **Attributes** *(list) --* **[REQUIRED]**

      A set of key-value pairs associated with the typed link. Typed link attributes are used when
      you have data values that are related to the link itself, and not to one of the two objects
      being linked. Identity attributes also serve to distinguish the link from others of the same
      type between the same objects.

      - *(dict) --*

        A typed link attribute definition.

        - **Name** *(string) --* **[REQUIRED]**

          The unique name of the typed link attribute.

        - **Type** *(string) --* **[REQUIRED]**

          The type of the attribute.

        - **DefaultValue** *(dict) --*

          The default value of the attribute (if configured).

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.

        - **IsImmutable** *(boolean) --*

          Whether the attribute is mutable or not.

        - **Rules** *(dict) --*

          Validation rules that are attached to the attribute definition.

          - *(string) --*

            - *(dict) --*

              Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.

              - **Type** *(string) --*

                The type of attribute validation rule.

              - **Parameters** *(dict) --*

                The minimum and maximum parameters that are associated with the rule.

                - *(string) --*

                  - *(string) --*

        - **RequiredBehavior** *(string) --* **[REQUIRED]**

          The required behavior of the ``TypedLinkAttributeDefinition`` .

    - **IdentityAttributeOrder** *(list) --* **[REQUIRED]**

      The set of attributes that distinguish links made from this facet from each other, in the order
      of significance. Listing typed links can filter on the values of these attributes. See
      ListOutgoingTypedLinks and  ListIncomingTypedLinks for details.

      - *(string) --*
    """


_ClientDeleteDirectoryResponseTypeDef = TypedDict(
    "_ClientDeleteDirectoryResponseTypeDef", {"DirectoryArn": str}, total=False
)


class ClientDeleteDirectoryResponseTypeDef(_ClientDeleteDirectoryResponseTypeDef):
    """
    Type definition for `ClientDeleteDirectory` `Response`

    - **DirectoryArn** *(string) --*

      The ARN of the deleted directory.
    """


_ClientDeleteObjectObjectReferenceTypeDef = TypedDict(
    "_ClientDeleteObjectObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientDeleteObjectObjectReferenceTypeDef(
    _ClientDeleteObjectObjectReferenceTypeDef
):
    """
    Type definition for `ClientDeleteObject` `ObjectReference`

    A reference that identifies the object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientDeleteSchemaResponseTypeDef = TypedDict(
    "_ClientDeleteSchemaResponseTypeDef", {"SchemaArn": str}, total=False
)


class ClientDeleteSchemaResponseTypeDef(_ClientDeleteSchemaResponseTypeDef):
    """
    Type definition for `ClientDeleteSchema` `Response`

    - **SchemaArn** *(string) --*

      The input ARN that is returned as part of the response. For more information, see  arns .
    """


_ClientDetachFromIndexIndexReferenceTypeDef = TypedDict(
    "_ClientDetachFromIndexIndexReferenceTypeDef", {"Selector": str}, total=False
)


class ClientDetachFromIndexIndexReferenceTypeDef(
    _ClientDetachFromIndexIndexReferenceTypeDef
):
    """
    Type definition for `ClientDetachFromIndex` `IndexReference`

    A reference to the index object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientDetachFromIndexResponseTypeDef = TypedDict(
    "_ClientDetachFromIndexResponseTypeDef",
    {"DetachedObjectIdentifier": str},
    total=False,
)


class ClientDetachFromIndexResponseTypeDef(_ClientDetachFromIndexResponseTypeDef):
    """
    Type definition for `ClientDetachFromIndex` `Response`

    - **DetachedObjectIdentifier** *(string) --*

      The ``ObjectIdentifier`` of the object that was detached from the index.
    """


_ClientDetachFromIndexTargetReferenceTypeDef = TypedDict(
    "_ClientDetachFromIndexTargetReferenceTypeDef", {"Selector": str}, total=False
)


class ClientDetachFromIndexTargetReferenceTypeDef(
    _ClientDetachFromIndexTargetReferenceTypeDef
):
    """
    Type definition for `ClientDetachFromIndex` `TargetReference`

    A reference to the object being detached from the index.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientDetachObjectParentReferenceTypeDef = TypedDict(
    "_ClientDetachObjectParentReferenceTypeDef", {"Selector": str}, total=False
)


class ClientDetachObjectParentReferenceTypeDef(
    _ClientDetachObjectParentReferenceTypeDef
):
    """
    Type definition for `ClientDetachObject` `ParentReference`

    The parent reference from which the object with the specified link name is detached.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientDetachObjectResponseTypeDef = TypedDict(
    "_ClientDetachObjectResponseTypeDef", {"DetachedObjectIdentifier": str}, total=False
)


class ClientDetachObjectResponseTypeDef(_ClientDetachObjectResponseTypeDef):
    """
    Type definition for `ClientDetachObject` `Response`

    - **DetachedObjectIdentifier** *(string) --*

      The ``ObjectIdentifier`` that was detached from the object.
    """


_ClientDetachPolicyObjectReferenceTypeDef = TypedDict(
    "_ClientDetachPolicyObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientDetachPolicyObjectReferenceTypeDef(
    _ClientDetachPolicyObjectReferenceTypeDef
):
    """
    Type definition for `ClientDetachPolicy` `ObjectReference`

    Reference that identifies the object whose policy object will be detached.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientDetachPolicyPolicyReferenceTypeDef = TypedDict(
    "_ClientDetachPolicyPolicyReferenceTypeDef", {"Selector": str}, total=False
)


class ClientDetachPolicyPolicyReferenceTypeDef(
    _ClientDetachPolicyPolicyReferenceTypeDef
):
    """
    Type definition for `ClientDetachPolicy` `PolicyReference`

    Reference that identifies the policy object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef(
    _ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef
):
    """
    Type definition for `ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValues` `Value`

    The value for the typed link.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
)


class ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef(
    _ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef
):
    """
    Type definition for `ClientDetachTypedLinkTypedLinkSpecifier` `IdentityAttributeValues`

    Identifies the attribute name and value for a typed link.

    - **AttributeName** *(string) --* **[REQUIRED]**

      The attribute name of the typed link.

    - **Value** *(dict) --* **[REQUIRED]**

      The value for the typed link.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "_ClientDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef(
    _ClientDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef
):
    """
    Type definition for `ClientDetachTypedLinkTypedLinkSpecifier` `SourceObjectReference`

    Identifies the source object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the
      path. Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "_ClientDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef(
    _ClientDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef
):
    """
    Type definition for `ClientDetachTypedLinkTypedLinkSpecifier` `TargetObjectReference`

    Identifies the target object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the
      path. Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_ClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
)


class ClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef(
    _ClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef
):
    """
    Type definition for `ClientDetachTypedLinkTypedLinkSpecifier` `TypedLinkFacet`

    Identifies the typed link facet that is associated with the typed link.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
      arns .

    - **TypedLinkName** *(string) --* **[REQUIRED]**

      The unique name of the typed link facet.
    """


_ClientDetachTypedLinkTypedLinkSpecifierTypeDef = TypedDict(
    "_ClientDetachTypedLinkTypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": ClientDetachTypedLinkTypedLinkSpecifierTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientDetachTypedLinkTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientDetachTypedLinkTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientDetachTypedLinkTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
)


class ClientDetachTypedLinkTypedLinkSpecifierTypeDef(
    _ClientDetachTypedLinkTypedLinkSpecifierTypeDef
):
    """
    Type definition for `ClientDetachTypedLink` `TypedLinkSpecifier`

    Used to accept a typed link specifier as input.

    - **TypedLinkFacet** *(dict) --* **[REQUIRED]**

      Identifies the typed link facet that is associated with the typed link.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
        arns .

      - **TypedLinkName** *(string) --* **[REQUIRED]**

        The unique name of the typed link facet.

    - **SourceObjectReference** *(dict) --* **[REQUIRED]**

      Identifies the source object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to it
        from the directory root. Use the link names from each parent/child link to construct the
        path. Path selectors start with a slash (/) and link names are separated by slashes. For more
        information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share the
        same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **TargetObjectReference** *(dict) --* **[REQUIRED]**

      Identifies the target object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to it
        from the directory root. Use the link names from each parent/child link to construct the
        path. Path selectors start with a slash (/) and link names are separated by slashes. For more
        information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share the
        same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **IdentityAttributeValues** *(list) --* **[REQUIRED]**

      Identifies the attribute value to update.

      - *(dict) --*

        Identifies the attribute name and value for a typed link.

        - **AttributeName** *(string) --* **[REQUIRED]**

          The attribute name of the typed link.

        - **Value** *(dict) --* **[REQUIRED]**

          The value for the typed link.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ClientDisableDirectoryResponseTypeDef = TypedDict(
    "_ClientDisableDirectoryResponseTypeDef", {"DirectoryArn": str}, total=False
)


class ClientDisableDirectoryResponseTypeDef(_ClientDisableDirectoryResponseTypeDef):
    """
    Type definition for `ClientDisableDirectory` `Response`

    - **DirectoryArn** *(string) --*

      The ARN of the directory that has been disabled.
    """


_ClientEnableDirectoryResponseTypeDef = TypedDict(
    "_ClientEnableDirectoryResponseTypeDef", {"DirectoryArn": str}, total=False
)


class ClientEnableDirectoryResponseTypeDef(_ClientEnableDirectoryResponseTypeDef):
    """
    Type definition for `ClientEnableDirectory` `Response`

    - **DirectoryArn** *(string) --*

      The ARN of the enabled directory.
    """


_ClientGetAppliedSchemaVersionResponseTypeDef = TypedDict(
    "_ClientGetAppliedSchemaVersionResponseTypeDef",
    {"AppliedSchemaArn": str},
    total=False,
)


class ClientGetAppliedSchemaVersionResponseTypeDef(
    _ClientGetAppliedSchemaVersionResponseTypeDef
):
    """
    Type definition for `ClientGetAppliedSchemaVersion` `Response`

    - **AppliedSchemaArn** *(string) --*

      Current applied schema ARN, including the minor version in use if one was provided.
    """


_ClientGetDirectoryResponseDirectoryTypeDef = TypedDict(
    "_ClientGetDirectoryResponseDirectoryTypeDef",
    {"Name": str, "DirectoryArn": str, "State": str, "CreationDateTime": datetime},
    total=False,
)


class ClientGetDirectoryResponseDirectoryTypeDef(
    _ClientGetDirectoryResponseDirectoryTypeDef
):
    """
    Type definition for `ClientGetDirectoryResponse` `Directory`

    Metadata about the directory.

    - **Name** *(string) --*

      The name of the directory.

    - **DirectoryArn** *(string) --*

      The Amazon Resource Name (ARN) that is associated with the directory. For more information,
      see  arns .

    - **State** *(string) --*

      The state of the directory. Can be either ``Enabled`` , ``Disabled`` , or ``Deleted`` .

    - **CreationDateTime** *(datetime) --*

      The date and time when the directory was created.
    """


_ClientGetDirectoryResponseTypeDef = TypedDict(
    "_ClientGetDirectoryResponseTypeDef",
    {"Directory": ClientGetDirectoryResponseDirectoryTypeDef},
    total=False,
)


class ClientGetDirectoryResponseTypeDef(_ClientGetDirectoryResponseTypeDef):
    """
    Type definition for `ClientGetDirectory` `Response`

    - **Directory** *(dict) --*

      Metadata about the directory.

      - **Name** *(string) --*

        The name of the directory.

      - **DirectoryArn** *(string) --*

        The Amazon Resource Name (ARN) that is associated with the directory. For more information,
        see  arns .

      - **State** *(string) --*

        The state of the directory. Can be either ``Enabled`` , ``Disabled`` , or ``Deleted`` .

      - **CreationDateTime** *(datetime) --*

        The date and time when the directory was created.
    """


_ClientGetFacetResponseFacetTypeDef = TypedDict(
    "_ClientGetFacetResponseFacetTypeDef",
    {"Name": str, "ObjectType": str, "FacetStyle": str},
    total=False,
)


class ClientGetFacetResponseFacetTypeDef(_ClientGetFacetResponseFacetTypeDef):
    """
    Type definition for `ClientGetFacetResponse` `Facet`

    The  Facet structure that is associated with the facet.

    - **Name** *(string) --*

      The name of the  Facet .

    - **ObjectType** *(string) --*

      The object type that is associated with the facet. See  CreateFacetRequest$ObjectType for
      more details.

    - **FacetStyle** *(string) --*

      There are two different styles that you can define on any given facet, ``Static`` and
      ``Dynamic`` . For static facets, all attributes must be defined in the schema. For dynamic
      facets, attributes can be defined during data plane operations.
    """


_ClientGetFacetResponseTypeDef = TypedDict(
    "_ClientGetFacetResponseTypeDef",
    {"Facet": ClientGetFacetResponseFacetTypeDef},
    total=False,
)


class ClientGetFacetResponseTypeDef(_ClientGetFacetResponseTypeDef):
    """
    Type definition for `ClientGetFacet` `Response`

    - **Facet** *(dict) --*

      The  Facet structure that is associated with the facet.

      - **Name** *(string) --*

        The name of the  Facet .

      - **ObjectType** *(string) --*

        The object type that is associated with the facet. See  CreateFacetRequest$ObjectType for
        more details.

      - **FacetStyle** *(string) --*

        There are two different styles that you can define on any given facet, ``Static`` and
        ``Dynamic`` . For static facets, all attributes must be defined in the schema. For dynamic
        facets, attributes can be defined during data plane operations.
    """


_ClientGetLinkAttributesResponseAttributesKeyTypeDef = TypedDict(
    "_ClientGetLinkAttributesResponseAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientGetLinkAttributesResponseAttributesKeyTypeDef(
    _ClientGetLinkAttributesResponseAttributesKeyTypeDef
):
    """
    Type definition for `ClientGetLinkAttributesResponseAttributes` `Key`

    The key of the attribute.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --*

      The name of the facet that the attribute exists within.

    - **Name** *(string) --*

      The name of the attribute.
    """


_ClientGetLinkAttributesResponseAttributesValueTypeDef = TypedDict(
    "_ClientGetLinkAttributesResponseAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientGetLinkAttributesResponseAttributesValueTypeDef(
    _ClientGetLinkAttributesResponseAttributesValueTypeDef
):
    """
    Type definition for `ClientGetLinkAttributesResponseAttributes` `Value`

    The value of the attribute.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientGetLinkAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientGetLinkAttributesResponseAttributesTypeDef",
    {
        "Key": ClientGetLinkAttributesResponseAttributesKeyTypeDef,
        "Value": ClientGetLinkAttributesResponseAttributesValueTypeDef,
    },
    total=False,
)


class ClientGetLinkAttributesResponseAttributesTypeDef(
    _ClientGetLinkAttributesResponseAttributesTypeDef
):
    """
    Type definition for `ClientGetLinkAttributesResponse` `Attributes`

    The combination of an attribute key and an attribute value.

    - **Key** *(dict) --*

      The key of the attribute.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --*

        The name of the facet that the attribute exists within.

      - **Name** *(string) --*

        The name of the attribute.

    - **Value** *(dict) --*

      The value of the attribute.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientGetLinkAttributesResponseTypeDef = TypedDict(
    "_ClientGetLinkAttributesResponseTypeDef",
    {"Attributes": List[ClientGetLinkAttributesResponseAttributesTypeDef]},
    total=False,
)


class ClientGetLinkAttributesResponseTypeDef(_ClientGetLinkAttributesResponseTypeDef):
    """
    Type definition for `ClientGetLinkAttributes` `Response`

    - **Attributes** *(list) --*

      The attributes that are associated with the typed link.

      - *(dict) --*

        The combination of an attribute key and an attribute value.

        - **Key** *(dict) --*

          The key of the attribute.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

          - **FacetName** *(string) --*

            The name of the facet that the attribute exists within.

          - **Name** *(string) --*

            The name of the attribute.

        - **Value** *(dict) --*

          The value of the attribute.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef(
    _ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef
):
    """
    Type definition for `ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValues` `Value`

    The value for the typed link.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
)


class ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef(
    _ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
):
    """
    Type definition for `ClientGetLinkAttributesTypedLinkSpecifier` `IdentityAttributeValues`

    Identifies the attribute name and value for a typed link.

    - **AttributeName** *(string) --* **[REQUIRED]**

      The attribute name of the typed link.

    - **Value** *(dict) --* **[REQUIRED]**

      The value for the typed link.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "_ClientGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef(
    _ClientGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef
):
    """
    Type definition for `ClientGetLinkAttributesTypedLinkSpecifier` `SourceObjectReference`

    Identifies the source object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the
      path. Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "_ClientGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef(
    _ClientGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef
):
    """
    Type definition for `ClientGetLinkAttributesTypedLinkSpecifier` `TargetObjectReference`

    Identifies the target object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the
      path. Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_ClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
)


class ClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef(
    _ClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef
):
    """
    Type definition for `ClientGetLinkAttributesTypedLinkSpecifier` `TypedLinkFacet`

    Identifies the typed link facet that is associated with the typed link.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
      arns .

    - **TypedLinkName** *(string) --* **[REQUIRED]**

      The unique name of the typed link facet.
    """


_ClientGetLinkAttributesTypedLinkSpecifierTypeDef = TypedDict(
    "_ClientGetLinkAttributesTypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": ClientGetLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientGetLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientGetLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientGetLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
)


class ClientGetLinkAttributesTypedLinkSpecifierTypeDef(
    _ClientGetLinkAttributesTypedLinkSpecifierTypeDef
):
    """
    Type definition for `ClientGetLinkAttributes` `TypedLinkSpecifier`

    Allows a typed link specifier to be accepted as input.

    - **TypedLinkFacet** *(dict) --* **[REQUIRED]**

      Identifies the typed link facet that is associated with the typed link.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
        arns .

      - **TypedLinkName** *(string) --* **[REQUIRED]**

        The unique name of the typed link facet.

    - **SourceObjectReference** *(dict) --* **[REQUIRED]**

      Identifies the source object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to it
        from the directory root. Use the link names from each parent/child link to construct the
        path. Path selectors start with a slash (/) and link names are separated by slashes. For more
        information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share the
        same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **TargetObjectReference** *(dict) --* **[REQUIRED]**

      Identifies the target object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to it
        from the directory root. Use the link names from each parent/child link to construct the
        path. Path selectors start with a slash (/) and link names are separated by slashes. For more
        information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share the
        same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **IdentityAttributeValues** *(list) --* **[REQUIRED]**

      Identifies the attribute value to update.

      - *(dict) --*

        Identifies the attribute name and value for a typed link.

        - **AttributeName** *(string) --* **[REQUIRED]**

          The attribute name of the typed link.

        - **Value** *(dict) --* **[REQUIRED]**

          The value for the typed link.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ClientGetObjectAttributesObjectReferenceTypeDef = TypedDict(
    "_ClientGetObjectAttributesObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientGetObjectAttributesObjectReferenceTypeDef(
    _ClientGetObjectAttributesObjectReferenceTypeDef
):
    """
    Type definition for `ClientGetObjectAttributes` `ObjectReference`

    Reference that identifies the object whose attributes will be retrieved.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientGetObjectAttributesResponseAttributesKeyTypeDef = TypedDict(
    "_ClientGetObjectAttributesResponseAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientGetObjectAttributesResponseAttributesKeyTypeDef(
    _ClientGetObjectAttributesResponseAttributesKeyTypeDef
):
    """
    Type definition for `ClientGetObjectAttributesResponseAttributes` `Key`

    The key of the attribute.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --*

      The name of the facet that the attribute exists within.

    - **Name** *(string) --*

      The name of the attribute.
    """


_ClientGetObjectAttributesResponseAttributesValueTypeDef = TypedDict(
    "_ClientGetObjectAttributesResponseAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientGetObjectAttributesResponseAttributesValueTypeDef(
    _ClientGetObjectAttributesResponseAttributesValueTypeDef
):
    """
    Type definition for `ClientGetObjectAttributesResponseAttributes` `Value`

    The value of the attribute.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientGetObjectAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientGetObjectAttributesResponseAttributesTypeDef",
    {
        "Key": ClientGetObjectAttributesResponseAttributesKeyTypeDef,
        "Value": ClientGetObjectAttributesResponseAttributesValueTypeDef,
    },
    total=False,
)


class ClientGetObjectAttributesResponseAttributesTypeDef(
    _ClientGetObjectAttributesResponseAttributesTypeDef
):
    """
    Type definition for `ClientGetObjectAttributesResponse` `Attributes`

    The combination of an attribute key and an attribute value.

    - **Key** *(dict) --*

      The key of the attribute.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --*

        The name of the facet that the attribute exists within.

      - **Name** *(string) --*

        The name of the attribute.

    - **Value** *(dict) --*

      The value of the attribute.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientGetObjectAttributesResponseTypeDef = TypedDict(
    "_ClientGetObjectAttributesResponseTypeDef",
    {"Attributes": List[ClientGetObjectAttributesResponseAttributesTypeDef]},
    total=False,
)


class ClientGetObjectAttributesResponseTypeDef(
    _ClientGetObjectAttributesResponseTypeDef
):
    """
    Type definition for `ClientGetObjectAttributes` `Response`

    - **Attributes** *(list) --*

      The attributes that are associated with the object.

      - *(dict) --*

        The combination of an attribute key and an attribute value.

        - **Key** *(dict) --*

          The key of the attribute.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

          - **FacetName** *(string) --*

            The name of the facet that the attribute exists within.

          - **Name** *(string) --*

            The name of the attribute.

        - **Value** *(dict) --*

          The value of the attribute.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ClientGetObjectAttributesSchemaFacetTypeDef = TypedDict(
    "_ClientGetObjectAttributesSchemaFacetTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientGetObjectAttributesSchemaFacetTypeDef(
    _ClientGetObjectAttributesSchemaFacetTypeDef
):
    """
    Type definition for `ClientGetObjectAttributes` `SchemaFacet`

    Identifier for the facet whose attributes will be retrieved. See  SchemaFacet for details.

    - **SchemaArn** *(string) --*

      The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place
      Schema Upgrade
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
      for a description of when to provide minor versions.

    - **FacetName** *(string) --*

      The name of the facet.
    """


_ClientGetObjectInformationObjectReferenceTypeDef = TypedDict(
    "_ClientGetObjectInformationObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientGetObjectInformationObjectReferenceTypeDef(
    _ClientGetObjectInformationObjectReferenceTypeDef
):
    """
    Type definition for `ClientGetObjectInformation` `ObjectReference`

    A reference to the object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientGetObjectInformationResponseSchemaFacetsTypeDef = TypedDict(
    "_ClientGetObjectInformationResponseSchemaFacetsTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientGetObjectInformationResponseSchemaFacetsTypeDef(
    _ClientGetObjectInformationResponseSchemaFacetsTypeDef
):
    """
    Type definition for `ClientGetObjectInformationResponse` `SchemaFacets`

    A facet.

    - **SchemaArn** *(string) --*

      The ARN of the schema that contains the facet with no minor component. See  arns and
      `In-Place Schema Upgrade
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
      for a description of when to provide minor versions.

    - **FacetName** *(string) --*

      The name of the facet.
    """


_ClientGetObjectInformationResponseTypeDef = TypedDict(
    "_ClientGetObjectInformationResponseTypeDef",
    {
        "SchemaFacets": List[ClientGetObjectInformationResponseSchemaFacetsTypeDef],
        "ObjectIdentifier": str,
    },
    total=False,
)


class ClientGetObjectInformationResponseTypeDef(
    _ClientGetObjectInformationResponseTypeDef
):
    """
    Type definition for `ClientGetObjectInformation` `Response`

    - **SchemaFacets** *(list) --*

      The facets attached to the specified object. Although the response does not include minor
      version information, the most recently applied minor version of each Facet is in effect. See
      GetAppliedSchemaVersion for details.

      - *(dict) --*

        A facet.

        - **SchemaArn** *(string) --*

          The ARN of the schema that contains the facet with no minor component. See  arns and
          `In-Place Schema Upgrade
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
          for a description of when to provide minor versions.

        - **FacetName** *(string) --*

          The name of the facet.

    - **ObjectIdentifier** *(string) --*

      The ``ObjectIdentifier`` of the specified object.
    """


_ClientGetSchemaAsJsonResponseTypeDef = TypedDict(
    "_ClientGetSchemaAsJsonResponseTypeDef", {"Name": str, "Document": str}, total=False
)


class ClientGetSchemaAsJsonResponseTypeDef(_ClientGetSchemaAsJsonResponseTypeDef):
    """
    Type definition for `ClientGetSchemaAsJson` `Response`

    - **Name** *(string) --*

      The name of the retrieved schema.

    - **Document** *(string) --*

      The JSON representation of the schema document.
    """


_ClientGetTypedLinkFacetInformationResponseTypeDef = TypedDict(
    "_ClientGetTypedLinkFacetInformationResponseTypeDef",
    {"IdentityAttributeOrder": List[str]},
    total=False,
)


class ClientGetTypedLinkFacetInformationResponseTypeDef(
    _ClientGetTypedLinkFacetInformationResponseTypeDef
):
    """
    Type definition for `ClientGetTypedLinkFacetInformation` `Response`

    - **IdentityAttributeOrder** *(list) --*

      The order of identity attributes for the facet, from most significant to least significant.
      The ability to filter typed links considers the order that the attributes are defined on the
      typed link facet. When providing ranges to typed link selection, any inexact ranges must be
      specified at the end. Any attributes that do not have a range specified are presumed to match
      the entire range. Filters are interpreted in the order of the attributes on the typed link
      facet, not the order in which they are supplied to any API calls. For more information about
      identity attributes, see `Typed Links
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_links.html#directory_objects_links_typedlink>`__
      .

      - *(string) --*
    """


_ClientListAppliedSchemaArnsResponseTypeDef = TypedDict(
    "_ClientListAppliedSchemaArnsResponseTypeDef",
    {"SchemaArns": List[str], "NextToken": str},
    total=False,
)


class ClientListAppliedSchemaArnsResponseTypeDef(
    _ClientListAppliedSchemaArnsResponseTypeDef
):
    """
    Type definition for `ClientListAppliedSchemaArns` `Response`

    - **SchemaArns** *(list) --*

      The ARNs of schemas that are applied to the directory.

      - *(string) --*

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesKeyTypeDef = TypedDict(
    "_ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesKeyTypeDef(
    _ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesKeyTypeDef
):
    """
    Type definition for `ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributes` `Key`

    The key of the attribute.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --*

      The name of the facet that the attribute exists within.

    - **Name** *(string) --*

      The name of the attribute.
    """


_ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesValueTypeDef = TypedDict(
    "_ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesValueTypeDef(
    _ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesValueTypeDef
):
    """
    Type definition for `ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributes` `Value`

    The value of the attribute.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesTypeDef = TypedDict(
    "_ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesTypeDef",
    {
        "Key": ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesKeyTypeDef,
        "Value": ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesValueTypeDef,
    },
    total=False,
)


class ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesTypeDef(
    _ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesTypeDef
):
    """
    Type definition for `ClientListAttachedIndicesResponseIndexAttachments` `IndexedAttributes`

    The combination of an attribute key and an attribute value.

    - **Key** *(dict) --*

      The key of the attribute.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --*

        The name of the facet that the attribute exists within.

      - **Name** *(string) --*

        The name of the attribute.

    - **Value** *(dict) --*

      The value of the attribute.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientListAttachedIndicesResponseIndexAttachmentsTypeDef = TypedDict(
    "_ClientListAttachedIndicesResponseIndexAttachmentsTypeDef",
    {
        "IndexedAttributes": List[
            ClientListAttachedIndicesResponseIndexAttachmentsIndexedAttributesTypeDef
        ],
        "ObjectIdentifier": str,
    },
    total=False,
)


class ClientListAttachedIndicesResponseIndexAttachmentsTypeDef(
    _ClientListAttachedIndicesResponseIndexAttachmentsTypeDef
):
    """
    Type definition for `ClientListAttachedIndicesResponse` `IndexAttachments`

    Represents an index and an attached object.

    - **IndexedAttributes** *(list) --*

      The indexed attribute values.

      - *(dict) --*

        The combination of an attribute key and an attribute value.

        - **Key** *(dict) --*

          The key of the attribute.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

          - **FacetName** *(string) --*

            The name of the facet that the attribute exists within.

          - **Name** *(string) --*

            The name of the attribute.

        - **Value** *(dict) --*

          The value of the attribute.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.

    - **ObjectIdentifier** *(string) --*

      In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to the index.
      In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the index attached to
      the object. This field will always contain the ``ObjectIdentifier`` of the object on the
      opposite side of the attachment specified in the query.
    """


_ClientListAttachedIndicesResponseTypeDef = TypedDict(
    "_ClientListAttachedIndicesResponseTypeDef",
    {
        "IndexAttachments": List[
            ClientListAttachedIndicesResponseIndexAttachmentsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListAttachedIndicesResponseTypeDef(
    _ClientListAttachedIndicesResponseTypeDef
):
    """
    Type definition for `ClientListAttachedIndices` `Response`

    - **IndexAttachments** *(list) --*

      The indices attached to the specified object.

      - *(dict) --*

        Represents an index and an attached object.

        - **IndexedAttributes** *(list) --*

          The indexed attribute values.

          - *(dict) --*

            The combination of an attribute key and an attribute value.

            - **Key** *(dict) --*

              The key of the attribute.

              - **SchemaArn** *(string) --*

                The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

              - **FacetName** *(string) --*

                The name of the facet that the attribute exists within.

              - **Name** *(string) --*

                The name of the attribute.

            - **Value** *(dict) --*

              The value of the attribute.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

        - **ObjectIdentifier** *(string) --*

          In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to the index.
          In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the index attached to
          the object. This field will always contain the ``ObjectIdentifier`` of the object on the
          opposite side of the attachment specified in the query.

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientListAttachedIndicesTargetReferenceTypeDef = TypedDict(
    "_ClientListAttachedIndicesTargetReferenceTypeDef", {"Selector": str}, total=False
)


class ClientListAttachedIndicesTargetReferenceTypeDef(
    _ClientListAttachedIndicesTargetReferenceTypeDef
):
    """
    Type definition for `ClientListAttachedIndices` `TargetReference`

    A reference to the object that has indices attached.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListDevelopmentSchemaArnsResponseTypeDef = TypedDict(
    "_ClientListDevelopmentSchemaArnsResponseTypeDef",
    {"SchemaArns": List[str], "NextToken": str},
    total=False,
)


class ClientListDevelopmentSchemaArnsResponseTypeDef(
    _ClientListDevelopmentSchemaArnsResponseTypeDef
):
    """
    Type definition for `ClientListDevelopmentSchemaArns` `Response`

    - **SchemaArns** *(list) --*

      The ARNs of retrieved development schemas.

      - *(string) --*

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientListDirectoriesResponseDirectoriesTypeDef = TypedDict(
    "_ClientListDirectoriesResponseDirectoriesTypeDef",
    {"Name": str, "DirectoryArn": str, "State": str, "CreationDateTime": datetime},
    total=False,
)


class ClientListDirectoriesResponseDirectoriesTypeDef(
    _ClientListDirectoriesResponseDirectoriesTypeDef
):
    """
    Type definition for `ClientListDirectoriesResponse` `Directories`

    Directory structure that includes the directory name and directory ARN.

    - **Name** *(string) --*

      The name of the directory.

    - **DirectoryArn** *(string) --*

      The Amazon Resource Name (ARN) that is associated with the directory. For more
      information, see  arns .

    - **State** *(string) --*

      The state of the directory. Can be either ``Enabled`` , ``Disabled`` , or ``Deleted`` .

    - **CreationDateTime** *(datetime) --*

      The date and time when the directory was created.
    """


_ClientListDirectoriesResponseTypeDef = TypedDict(
    "_ClientListDirectoriesResponseTypeDef",
    {
        "Directories": List[ClientListDirectoriesResponseDirectoriesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListDirectoriesResponseTypeDef(_ClientListDirectoriesResponseTypeDef):
    """
    Type definition for `ClientListDirectories` `Response`

    - **Directories** *(list) --*

      Lists all directories that are associated with your account in pagination fashion.

      - *(dict) --*

        Directory structure that includes the directory name and directory ARN.

        - **Name** *(string) --*

          The name of the directory.

        - **DirectoryArn** *(string) --*

          The Amazon Resource Name (ARN) that is associated with the directory. For more
          information, see  arns .

        - **State** *(string) --*

          The state of the directory. Can be either ``Enabled`` , ``Disabled`` , or ``Deleted`` .

        - **CreationDateTime** *(datetime) --*

          The date and time when the directory was created.

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientListFacetAttributesResponseAttributesAttributeDefinitionDefaultValueTypeDef = TypedDict(
    "_ClientListFacetAttributesResponseAttributesAttributeDefinitionDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListFacetAttributesResponseAttributesAttributeDefinitionDefaultValueTypeDef(
    _ClientListFacetAttributesResponseAttributesAttributeDefinitionDefaultValueTypeDef
):
    """
    Type definition for `ClientListFacetAttributesResponseAttributesAttributeDefinition` `DefaultValue`

    The default value of the attribute (if configured).

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientListFacetAttributesResponseAttributesAttributeDefinitionRulesTypeDef = TypedDict(
    "_ClientListFacetAttributesResponseAttributesAttributeDefinitionRulesTypeDef",
    {"Type": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientListFacetAttributesResponseAttributesAttributeDefinitionRulesTypeDef(
    _ClientListFacetAttributesResponseAttributesAttributeDefinitionRulesTypeDef
):
    """
    Type definition for `ClientListFacetAttributesResponseAttributesAttributeDefinition` `Rules`

    Contains an Amazon Resource Name (ARN) and parameters that are associated with the
    rule.

    - **Type** *(string) --*

      The type of attribute validation rule.

    - **Parameters** *(dict) --*

      The minimum and maximum parameters that are associated with the rule.

      - *(string) --*

        - *(string) --*
    """


_ClientListFacetAttributesResponseAttributesAttributeDefinitionTypeDef = TypedDict(
    "_ClientListFacetAttributesResponseAttributesAttributeDefinitionTypeDef",
    {
        "Type": str,
        "DefaultValue": ClientListFacetAttributesResponseAttributesAttributeDefinitionDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[
            str,
            ClientListFacetAttributesResponseAttributesAttributeDefinitionRulesTypeDef,
        ],
    },
    total=False,
)


class ClientListFacetAttributesResponseAttributesAttributeDefinitionTypeDef(
    _ClientListFacetAttributesResponseAttributesAttributeDefinitionTypeDef
):
    """
    Type definition for `ClientListFacetAttributesResponseAttributes` `AttributeDefinition`

    A facet attribute consists of either a definition or a reference. This structure contains
    the attribute definition. See `Attribute References
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
    for more information.

    - **Type** *(string) --*

      The type of the attribute.

    - **DefaultValue** *(dict) --*

      The default value of the attribute (if configured).

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.

    - **IsImmutable** *(boolean) --*

      Whether the attribute is mutable or not.

    - **Rules** *(dict) --*

      Validation rules attached to the attribute definition.

      - *(string) --*

        - *(dict) --*

          Contains an Amazon Resource Name (ARN) and parameters that are associated with the
          rule.

          - **Type** *(string) --*

            The type of attribute validation rule.

          - **Parameters** *(dict) --*

            The minimum and maximum parameters that are associated with the rule.

            - *(string) --*

              - *(string) --*
    """


_ClientListFacetAttributesResponseAttributesAttributeReferenceTypeDef = TypedDict(
    "_ClientListFacetAttributesResponseAttributesAttributeReferenceTypeDef",
    {"TargetFacetName": str, "TargetAttributeName": str},
    total=False,
)


class ClientListFacetAttributesResponseAttributesAttributeReferenceTypeDef(
    _ClientListFacetAttributesResponseAttributesAttributeReferenceTypeDef
):
    """
    Type definition for `ClientListFacetAttributesResponseAttributes` `AttributeReference`

    An attribute reference that is associated with the attribute. See `Attribute References
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
    for more information.

    - **TargetFacetName** *(string) --*

      The target facet name that is associated with the facet reference. See `Attribute
      References
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
      for more information.

    - **TargetAttributeName** *(string) --*

      The target attribute name that is associated with the facet reference. See `Attribute
      References
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
      for more information.
    """


_ClientListFacetAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientListFacetAttributesResponseAttributesTypeDef",
    {
        "Name": str,
        "AttributeDefinition": ClientListFacetAttributesResponseAttributesAttributeDefinitionTypeDef,
        "AttributeReference": ClientListFacetAttributesResponseAttributesAttributeReferenceTypeDef,
        "RequiredBehavior": str,
    },
    total=False,
)


class ClientListFacetAttributesResponseAttributesTypeDef(
    _ClientListFacetAttributesResponseAttributesTypeDef
):
    """
    Type definition for `ClientListFacetAttributesResponse` `Attributes`

    An attribute that is associated with the  Facet .

    - **Name** *(string) --*

      The name of the facet attribute.

    - **AttributeDefinition** *(dict) --*

      A facet attribute consists of either a definition or a reference. This structure contains
      the attribute definition. See `Attribute References
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
      for more information.

      - **Type** *(string) --*

        The type of the attribute.

      - **DefaultValue** *(dict) --*

        The default value of the attribute (if configured).

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.

      - **IsImmutable** *(boolean) --*

        Whether the attribute is mutable or not.

      - **Rules** *(dict) --*

        Validation rules attached to the attribute definition.

        - *(string) --*

          - *(dict) --*

            Contains an Amazon Resource Name (ARN) and parameters that are associated with the
            rule.

            - **Type** *(string) --*

              The type of attribute validation rule.

            - **Parameters** *(dict) --*

              The minimum and maximum parameters that are associated with the rule.

              - *(string) --*

                - *(string) --*

    - **AttributeReference** *(dict) --*

      An attribute reference that is associated with the attribute. See `Attribute References
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
      for more information.

      - **TargetFacetName** *(string) --*

        The target facet name that is associated with the facet reference. See `Attribute
        References
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
        for more information.

      - **TargetAttributeName** *(string) --*

        The target attribute name that is associated with the facet reference. See `Attribute
        References
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
        for more information.

    - **RequiredBehavior** *(string) --*

      The required behavior of the ``FacetAttribute`` .
    """


_ClientListFacetAttributesResponseTypeDef = TypedDict(
    "_ClientListFacetAttributesResponseTypeDef",
    {
        "Attributes": List[ClientListFacetAttributesResponseAttributesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListFacetAttributesResponseTypeDef(
    _ClientListFacetAttributesResponseTypeDef
):
    """
    Type definition for `ClientListFacetAttributes` `Response`

    - **Attributes** *(list) --*

      The attributes attached to the facet.

      - *(dict) --*

        An attribute that is associated with the  Facet .

        - **Name** *(string) --*

          The name of the facet attribute.

        - **AttributeDefinition** *(dict) --*

          A facet attribute consists of either a definition or a reference. This structure contains
          the attribute definition. See `Attribute References
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
          for more information.

          - **Type** *(string) --*

            The type of the attribute.

          - **DefaultValue** *(dict) --*

            The default value of the attribute (if configured).

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.

          - **IsImmutable** *(boolean) --*

            Whether the attribute is mutable or not.

          - **Rules** *(dict) --*

            Validation rules attached to the attribute definition.

            - *(string) --*

              - *(dict) --*

                Contains an Amazon Resource Name (ARN) and parameters that are associated with the
                rule.

                - **Type** *(string) --*

                  The type of attribute validation rule.

                - **Parameters** *(dict) --*

                  The minimum and maximum parameters that are associated with the rule.

                  - *(string) --*

                    - *(string) --*

        - **AttributeReference** *(dict) --*

          An attribute reference that is associated with the attribute. See `Attribute References
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
          for more information.

          - **TargetFacetName** *(string) --*

            The target facet name that is associated with the facet reference. See `Attribute
            References
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
            for more information.

          - **TargetAttributeName** *(string) --*

            The target attribute name that is associated with the facet reference. See `Attribute
            References
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
            for more information.

        - **RequiredBehavior** *(string) --*

          The required behavior of the ``FacetAttribute`` .

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientListFacetNamesResponseTypeDef = TypedDict(
    "_ClientListFacetNamesResponseTypeDef",
    {"FacetNames": List[str], "NextToken": str},
    total=False,
)


class ClientListFacetNamesResponseTypeDef(_ClientListFacetNamesResponseTypeDef):
    """
    Type definition for `ClientListFacetNames` `Response`

    - **FacetNames** *(list) --*

      The names of facets that exist within the schema.

      - *(string) --*

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef(
    _ClientListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef
):
    """
    Type definition for `ClientListIncomingTypedLinksFilterAttributeRangesRange` `EndValue`

    The attribute value to terminate the range at.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef(
    _ClientListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef
):
    """
    Type definition for `ClientListIncomingTypedLinksFilterAttributeRangesRange` `StartValue`

    The value to start the range at.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_RequiredClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef = TypedDict(
    "_RequiredClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef",
    {"StartMode": str, "EndMode": str},
)
_OptionalClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef = TypedDict(
    "_OptionalClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef",
    {
        "StartValue": ClientListIncomingTypedLinksFilterAttributeRangesRangeStartValueTypeDef,
        "EndValue": ClientListIncomingTypedLinksFilterAttributeRangesRangeEndValueTypeDef,
    },
    total=False,
)


class ClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef(
    _RequiredClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef,
    _OptionalClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef,
):
    """
    Type definition for `ClientListIncomingTypedLinksFilterAttributeRanges` `Range`

    The range of attribute values that are being selected.

    - **StartMode** *(string) --* **[REQUIRED]**

      The inclusive or exclusive range start.

    - **StartValue** *(dict) --*

      The value to start the range at.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.

    - **EndMode** *(string) --* **[REQUIRED]**

      The inclusive or exclusive range end.

    - **EndValue** *(dict) --*

      The attribute value to terminate the range at.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_RequiredClientListIncomingTypedLinksFilterAttributeRangesTypeDef = TypedDict(
    "_RequiredClientListIncomingTypedLinksFilterAttributeRangesTypeDef",
    {"Range": ClientListIncomingTypedLinksFilterAttributeRangesRangeTypeDef},
)
_OptionalClientListIncomingTypedLinksFilterAttributeRangesTypeDef = TypedDict(
    "_OptionalClientListIncomingTypedLinksFilterAttributeRangesTypeDef",
    {"AttributeName": str},
    total=False,
)


class ClientListIncomingTypedLinksFilterAttributeRangesTypeDef(
    _RequiredClientListIncomingTypedLinksFilterAttributeRangesTypeDef,
    _OptionalClientListIncomingTypedLinksFilterAttributeRangesTypeDef,
):
    """
    Type definition for `ClientListIncomingTypedLinks` `FilterAttributeRanges`

    Identifies the range of attributes that are used by a specified filter.

    - **AttributeName** *(string) --*

      The unique name of the typed link attribute.

    - **Range** *(dict) --* **[REQUIRED]**

      The range of attribute values that are being selected.

      - **StartMode** *(string) --* **[REQUIRED]**

        The inclusive or exclusive range start.

      - **StartValue** *(dict) --*

        The value to start the range at.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.

      - **EndMode** *(string) --* **[REQUIRED]**

        The inclusive or exclusive range end.

      - **EndValue** *(dict) --*

        The attribute value to terminate the range at.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.
    """


_ClientListIncomingTypedLinksFilterTypedLinkTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksFilterTypedLinkTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
)


class ClientListIncomingTypedLinksFilterTypedLinkTypeDef(
    _ClientListIncomingTypedLinksFilterTypedLinkTypeDef
):
    """
    Type definition for `ClientListIncomingTypedLinks` `FilterTypedLink`

    Filters are interpreted in the order of the attributes on the typed link facet, not the order in
    which they are supplied to any API calls.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
      arns .

    - **TypedLinkName** *(string) --* **[REQUIRED]**

      The unique name of the typed link facet.
    """


_ClientListIncomingTypedLinksObjectReferenceTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientListIncomingTypedLinksObjectReferenceTypeDef(
    _ClientListIncomingTypedLinksObjectReferenceTypeDef
):
    """
    Type definition for `ClientListIncomingTypedLinks` `ObjectReference`

    Reference that identifies the object whose attributes will be listed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef(
    _ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef
):
    """
    Type definition for `ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValues` `Value`

    The value for the typed link.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesTypeDef(
    _ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesTypeDef
):
    """
    Type definition for `ClientListIncomingTypedLinksResponseLinkSpecifiers` `IdentityAttributeValues`

    Identifies the attribute name and value for a typed link.

    - **AttributeName** *(string) --*

      The attribute name of the typed link.

    - **Value** *(dict) --*

      The value for the typed link.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientListIncomingTypedLinksResponseLinkSpecifiersSourceObjectReferenceTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksResponseLinkSpecifiersSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientListIncomingTypedLinksResponseLinkSpecifiersSourceObjectReferenceTypeDef(
    _ClientListIncomingTypedLinksResponseLinkSpecifiersSourceObjectReferenceTypeDef
):
    """
    Type definition for `ClientListIncomingTypedLinksResponseLinkSpecifiers` `SourceObjectReference`

    Identifies the source object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading
      to it from the directory root. Use the link names from each parent/child link to
      construct the path. Path selectors start with a slash (/) and link names are separated
      by slashes. For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
      Cloud Directory. When creating objects, the system will provide you with the identifier
      of the created object. An object’s identifier is immutable and no two objects will ever
      share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListIncomingTypedLinksResponseLinkSpecifiersTargetObjectReferenceTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksResponseLinkSpecifiersTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientListIncomingTypedLinksResponseLinkSpecifiersTargetObjectReferenceTypeDef(
    _ClientListIncomingTypedLinksResponseLinkSpecifiersTargetObjectReferenceTypeDef
):
    """
    Type definition for `ClientListIncomingTypedLinksResponseLinkSpecifiers` `TargetObjectReference`

    Identifies the target object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading
      to it from the directory root. Use the link names from each parent/child link to
      construct the path. Path selectors start with a slash (/) and link names are separated
      by slashes. For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
      Cloud Directory. When creating objects, the system will provide you with the identifier
      of the created object. An object’s identifier is immutable and no two objects will ever
      share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListIncomingTypedLinksResponseLinkSpecifiersTypedLinkFacetTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksResponseLinkSpecifiersTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ClientListIncomingTypedLinksResponseLinkSpecifiersTypedLinkFacetTypeDef(
    _ClientListIncomingTypedLinksResponseLinkSpecifiersTypedLinkFacetTypeDef
):
    """
    Type definition for `ClientListIncomingTypedLinksResponseLinkSpecifiers` `TypedLinkFacet`

    Identifies the typed link facet that is associated with the typed link.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) that is associated with the schema. For more
      information, see  arns .

    - **TypedLinkName** *(string) --*

      The unique name of the typed link facet.
    """


_ClientListIncomingTypedLinksResponseLinkSpecifiersTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksResponseLinkSpecifiersTypeDef",
    {
        "TypedLinkFacet": ClientListIncomingTypedLinksResponseLinkSpecifiersTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientListIncomingTypedLinksResponseLinkSpecifiersSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientListIncomingTypedLinksResponseLinkSpecifiersTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientListIncomingTypedLinksResponseLinkSpecifiersIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientListIncomingTypedLinksResponseLinkSpecifiersTypeDef(
    _ClientListIncomingTypedLinksResponseLinkSpecifiersTypeDef
):
    """
    Type definition for `ClientListIncomingTypedLinksResponse` `LinkSpecifiers`

    Contains all the information that is used to uniquely identify a typed link. The parameters
    discussed in this topic are used to uniquely specify the typed link being operated on. The
    AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts
    one as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API
    operations provide typed link specifiers as output. You can also construct a typed link
    specifier from scratch.

    - **TypedLinkFacet** *(dict) --*

      Identifies the typed link facet that is associated with the typed link.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) that is associated with the schema. For more
        information, see  arns .

      - **TypedLinkName** *(string) --*

        The unique name of the typed link facet.

    - **SourceObjectReference** *(dict) --*

      Identifies the source object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading
        to it from the directory root. Use the link names from each parent/child link to
        construct the path. Path selectors start with a slash (/) and link names are separated
        by slashes. For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
        Cloud Directory. When creating objects, the system will provide you with the identifier
        of the created object. An object’s identifier is immutable and no two objects will ever
        share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **TargetObjectReference** *(dict) --*

      Identifies the target object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading
        to it from the directory root. Use the link names from each parent/child link to
        construct the path. Path selectors start with a slash (/) and link names are separated
        by slashes. For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
        Cloud Directory. When creating objects, the system will provide you with the identifier
        of the created object. An object’s identifier is immutable and no two objects will ever
        share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **IdentityAttributeValues** *(list) --*

      Identifies the attribute value to update.

      - *(dict) --*

        Identifies the attribute name and value for a typed link.

        - **AttributeName** *(string) --*

          The attribute name of the typed link.

        - **Value** *(dict) --*

          The value for the typed link.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ClientListIncomingTypedLinksResponseTypeDef = TypedDict(
    "_ClientListIncomingTypedLinksResponseTypeDef",
    {
        "LinkSpecifiers": List[
            ClientListIncomingTypedLinksResponseLinkSpecifiersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListIncomingTypedLinksResponseTypeDef(
    _ClientListIncomingTypedLinksResponseTypeDef
):
    """
    Type definition for `ClientListIncomingTypedLinks` `Response`

    - **LinkSpecifiers** *(list) --*

      Returns one or more typed link specifiers as output.

      - *(dict) --*

        Contains all the information that is used to uniquely identify a typed link. The parameters
        discussed in this topic are used to uniquely specify the typed link being operated on. The
        AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts
        one as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API
        operations provide typed link specifiers as output. You can also construct a typed link
        specifier from scratch.

        - **TypedLinkFacet** *(dict) --*

          Identifies the typed link facet that is associated with the typed link.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) that is associated with the schema. For more
            information, see  arns .

          - **TypedLinkName** *(string) --*

            The unique name of the typed link facet.

        - **SourceObjectReference** *(dict) --*

          Identifies the source object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links leading
            to it from the directory root. Use the link names from each parent/child link to
            construct the path. Path selectors start with a slash (/) and link names are separated
            by slashes. For more information about paths, see `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
            Cloud Directory. When creating objects, the system will provide you with the identifier
            of the created object. An object’s identifier is immutable and no two objects will ever
            share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **TargetObjectReference** *(dict) --*

          Identifies the target object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links leading
            to it from the directory root. Use the link names from each parent/child link to
            construct the path. Path selectors start with a slash (/) and link names are separated
            by slashes. For more information about paths, see `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
            Cloud Directory. When creating objects, the system will provide you with the identifier
            of the created object. An object’s identifier is immutable and no two objects will ever
            share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **IdentityAttributeValues** *(list) --*

          Identifies the attribute value to update.

          - *(dict) --*

            Identifies the attribute name and value for a typed link.

            - **AttributeName** *(string) --*

              The attribute name of the typed link.

            - **Value** *(dict) --*

              The value for the typed link.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientListIndexIndexReferenceTypeDef = TypedDict(
    "_ClientListIndexIndexReferenceTypeDef", {"Selector": str}, total=False
)


class ClientListIndexIndexReferenceTypeDef(_ClientListIndexIndexReferenceTypeDef):
    """
    Type definition for `ClientListIndex` `IndexReference`

    The reference to the index to list.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef = TypedDict(
    "_ClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
)


class ClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef(
    _ClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef
):
    """
    Type definition for `ClientListIndexRangesOnIndexedValues` `AttributeKey`

    The key of the attribute that the attribute range covers.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --* **[REQUIRED]**

      The name of the facet that the attribute exists within.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.
    """


_ClientListIndexRangesOnIndexedValuesRangeEndValueTypeDef = TypedDict(
    "_ClientListIndexRangesOnIndexedValuesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListIndexRangesOnIndexedValuesRangeEndValueTypeDef(
    _ClientListIndexRangesOnIndexedValuesRangeEndValueTypeDef
):
    """
    Type definition for `ClientListIndexRangesOnIndexedValuesRange` `EndValue`

    The attribute value to terminate the range at.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientListIndexRangesOnIndexedValuesRangeStartValueTypeDef = TypedDict(
    "_ClientListIndexRangesOnIndexedValuesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListIndexRangesOnIndexedValuesRangeStartValueTypeDef(
    _ClientListIndexRangesOnIndexedValuesRangeStartValueTypeDef
):
    """
    Type definition for `ClientListIndexRangesOnIndexedValuesRange` `StartValue`

    The value to start the range at.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_RequiredClientListIndexRangesOnIndexedValuesRangeTypeDef = TypedDict(
    "_RequiredClientListIndexRangesOnIndexedValuesRangeTypeDef",
    {"StartMode": str, "EndMode": str},
)
_OptionalClientListIndexRangesOnIndexedValuesRangeTypeDef = TypedDict(
    "_OptionalClientListIndexRangesOnIndexedValuesRangeTypeDef",
    {
        "StartValue": ClientListIndexRangesOnIndexedValuesRangeStartValueTypeDef,
        "EndValue": ClientListIndexRangesOnIndexedValuesRangeEndValueTypeDef,
    },
    total=False,
)


class ClientListIndexRangesOnIndexedValuesRangeTypeDef(
    _RequiredClientListIndexRangesOnIndexedValuesRangeTypeDef,
    _OptionalClientListIndexRangesOnIndexedValuesRangeTypeDef,
):
    """
    Type definition for `ClientListIndexRangesOnIndexedValues` `Range`

    The range of attribute values being selected.

    - **StartMode** *(string) --* **[REQUIRED]**

      The inclusive or exclusive range start.

    - **StartValue** *(dict) --*

      The value to start the range at.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.

    - **EndMode** *(string) --* **[REQUIRED]**

      The inclusive or exclusive range end.

    - **EndValue** *(dict) --*

      The attribute value to terminate the range at.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientListIndexRangesOnIndexedValuesTypeDef = TypedDict(
    "_ClientListIndexRangesOnIndexedValuesTypeDef",
    {
        "AttributeKey": ClientListIndexRangesOnIndexedValuesAttributeKeyTypeDef,
        "Range": ClientListIndexRangesOnIndexedValuesRangeTypeDef,
    },
    total=False,
)


class ClientListIndexRangesOnIndexedValuesTypeDef(
    _ClientListIndexRangesOnIndexedValuesTypeDef
):
    """
    Type definition for `ClientListIndex` `RangesOnIndexedValues`

    A range of attributes.

    - **AttributeKey** *(dict) --*

      The key of the attribute that the attribute range covers.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --* **[REQUIRED]**

        The name of the facet that the attribute exists within.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the attribute.

    - **Range** *(dict) --*

      The range of attribute values being selected.

      - **StartMode** *(string) --* **[REQUIRED]**

        The inclusive or exclusive range start.

      - **StartValue** *(dict) --*

        The value to start the range at.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.

      - **EndMode** *(string) --* **[REQUIRED]**

        The inclusive or exclusive range end.

      - **EndValue** *(dict) --*

        The attribute value to terminate the range at.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.
    """


_ClientListIndexResponseIndexAttachmentsIndexedAttributesKeyTypeDef = TypedDict(
    "_ClientListIndexResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientListIndexResponseIndexAttachmentsIndexedAttributesKeyTypeDef(
    _ClientListIndexResponseIndexAttachmentsIndexedAttributesKeyTypeDef
):
    """
    Type definition for `ClientListIndexResponseIndexAttachmentsIndexedAttributes` `Key`

    The key of the attribute.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --*

      The name of the facet that the attribute exists within.

    - **Name** *(string) --*

      The name of the attribute.
    """


_ClientListIndexResponseIndexAttachmentsIndexedAttributesValueTypeDef = TypedDict(
    "_ClientListIndexResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListIndexResponseIndexAttachmentsIndexedAttributesValueTypeDef(
    _ClientListIndexResponseIndexAttachmentsIndexedAttributesValueTypeDef
):
    """
    Type definition for `ClientListIndexResponseIndexAttachmentsIndexedAttributes` `Value`

    The value of the attribute.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientListIndexResponseIndexAttachmentsIndexedAttributesTypeDef = TypedDict(
    "_ClientListIndexResponseIndexAttachmentsIndexedAttributesTypeDef",
    {
        "Key": ClientListIndexResponseIndexAttachmentsIndexedAttributesKeyTypeDef,
        "Value": ClientListIndexResponseIndexAttachmentsIndexedAttributesValueTypeDef,
    },
    total=False,
)


class ClientListIndexResponseIndexAttachmentsIndexedAttributesTypeDef(
    _ClientListIndexResponseIndexAttachmentsIndexedAttributesTypeDef
):
    """
    Type definition for `ClientListIndexResponseIndexAttachments` `IndexedAttributes`

    The combination of an attribute key and an attribute value.

    - **Key** *(dict) --*

      The key of the attribute.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --*

        The name of the facet that the attribute exists within.

      - **Name** *(string) --*

        The name of the attribute.

    - **Value** *(dict) --*

      The value of the attribute.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientListIndexResponseIndexAttachmentsTypeDef = TypedDict(
    "_ClientListIndexResponseIndexAttachmentsTypeDef",
    {
        "IndexedAttributes": List[
            ClientListIndexResponseIndexAttachmentsIndexedAttributesTypeDef
        ],
        "ObjectIdentifier": str,
    },
    total=False,
)


class ClientListIndexResponseIndexAttachmentsTypeDef(
    _ClientListIndexResponseIndexAttachmentsTypeDef
):
    """
    Type definition for `ClientListIndexResponse` `IndexAttachments`

    Represents an index and an attached object.

    - **IndexedAttributes** *(list) --*

      The indexed attribute values.

      - *(dict) --*

        The combination of an attribute key and an attribute value.

        - **Key** *(dict) --*

          The key of the attribute.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

          - **FacetName** *(string) --*

            The name of the facet that the attribute exists within.

          - **Name** *(string) --*

            The name of the attribute.

        - **Value** *(dict) --*

          The value of the attribute.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.

    - **ObjectIdentifier** *(string) --*

      In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to the index.
      In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the index attached to
      the object. This field will always contain the ``ObjectIdentifier`` of the object on the
      opposite side of the attachment specified in the query.
    """


_ClientListIndexResponseTypeDef = TypedDict(
    "_ClientListIndexResponseTypeDef",
    {
        "IndexAttachments": List[ClientListIndexResponseIndexAttachmentsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListIndexResponseTypeDef(_ClientListIndexResponseTypeDef):
    """
    Type definition for `ClientListIndex` `Response`

    - **IndexAttachments** *(list) --*

      The objects and indexed values attached to the index.

      - *(dict) --*

        Represents an index and an attached object.

        - **IndexedAttributes** *(list) --*

          The indexed attribute values.

          - *(dict) --*

            The combination of an attribute key and an attribute value.

            - **Key** *(dict) --*

              The key of the attribute.

              - **SchemaArn** *(string) --*

                The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

              - **FacetName** *(string) --*

                The name of the facet that the attribute exists within.

              - **Name** *(string) --*

                The name of the attribute.

            - **Value** *(dict) --*

              The value of the attribute.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

        - **ObjectIdentifier** *(string) --*

          In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to the index.
          In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the index attached to
          the object. This field will always contain the ``ObjectIdentifier`` of the object on the
          opposite side of the attachment specified in the query.

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientListManagedSchemaArnsResponseTypeDef = TypedDict(
    "_ClientListManagedSchemaArnsResponseTypeDef",
    {"SchemaArns": List[str], "NextToken": str},
    total=False,
)


class ClientListManagedSchemaArnsResponseTypeDef(
    _ClientListManagedSchemaArnsResponseTypeDef
):
    """
    Type definition for `ClientListManagedSchemaArns` `Response`

    - **SchemaArns** *(list) --*

      The ARNs for all AWS managed schemas.

      - *(string) --*

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientListObjectAttributesFacetFilterTypeDef = TypedDict(
    "_ClientListObjectAttributesFacetFilterTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientListObjectAttributesFacetFilterTypeDef(
    _ClientListObjectAttributesFacetFilterTypeDef
):
    """
    Type definition for `ClientListObjectAttributes` `FacetFilter`

    Used to filter the list of object attributes that are associated with a certain facet.

    - **SchemaArn** *(string) --*

      The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place
      Schema Upgrade
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
      for a description of when to provide minor versions.

    - **FacetName** *(string) --*

      The name of the facet.
    """


_ClientListObjectAttributesObjectReferenceTypeDef = TypedDict(
    "_ClientListObjectAttributesObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientListObjectAttributesObjectReferenceTypeDef(
    _ClientListObjectAttributesObjectReferenceTypeDef
):
    """
    Type definition for `ClientListObjectAttributes` `ObjectReference`

    The reference that identifies the object whose attributes will be listed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListObjectAttributesResponseAttributesKeyTypeDef = TypedDict(
    "_ClientListObjectAttributesResponseAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ClientListObjectAttributesResponseAttributesKeyTypeDef(
    _ClientListObjectAttributesResponseAttributesKeyTypeDef
):
    """
    Type definition for `ClientListObjectAttributesResponseAttributes` `Key`

    The key of the attribute.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --*

      The name of the facet that the attribute exists within.

    - **Name** *(string) --*

      The name of the attribute.
    """


_ClientListObjectAttributesResponseAttributesValueTypeDef = TypedDict(
    "_ClientListObjectAttributesResponseAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListObjectAttributesResponseAttributesValueTypeDef(
    _ClientListObjectAttributesResponseAttributesValueTypeDef
):
    """
    Type definition for `ClientListObjectAttributesResponseAttributes` `Value`

    The value of the attribute.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientListObjectAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientListObjectAttributesResponseAttributesTypeDef",
    {
        "Key": ClientListObjectAttributesResponseAttributesKeyTypeDef,
        "Value": ClientListObjectAttributesResponseAttributesValueTypeDef,
    },
    total=False,
)


class ClientListObjectAttributesResponseAttributesTypeDef(
    _ClientListObjectAttributesResponseAttributesTypeDef
):
    """
    Type definition for `ClientListObjectAttributesResponse` `Attributes`

    The combination of an attribute key and an attribute value.

    - **Key** *(dict) --*

      The key of the attribute.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --*

        The name of the facet that the attribute exists within.

      - **Name** *(string) --*

        The name of the attribute.

    - **Value** *(dict) --*

      The value of the attribute.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientListObjectAttributesResponseTypeDef = TypedDict(
    "_ClientListObjectAttributesResponseTypeDef",
    {
        "Attributes": List[ClientListObjectAttributesResponseAttributesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListObjectAttributesResponseTypeDef(
    _ClientListObjectAttributesResponseTypeDef
):
    """
    Type definition for `ClientListObjectAttributes` `Response`

    - **Attributes** *(list) --*

      Attributes map that is associated with the object. ``AttributeArn`` is the key, and attribute
      value is the value.

      - *(dict) --*

        The combination of an attribute key and an attribute value.

        - **Key** *(dict) --*

          The key of the attribute.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

          - **FacetName** *(string) --*

            The name of the facet that the attribute exists within.

          - **Name** *(string) --*

            The name of the attribute.

        - **Value** *(dict) --*

          The value of the attribute.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientListObjectChildrenObjectReferenceTypeDef = TypedDict(
    "_ClientListObjectChildrenObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientListObjectChildrenObjectReferenceTypeDef(
    _ClientListObjectChildrenObjectReferenceTypeDef
):
    """
    Type definition for `ClientListObjectChildren` `ObjectReference`

    The reference that identifies the object for which child objects are being listed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListObjectChildrenResponseTypeDef = TypedDict(
    "_ClientListObjectChildrenResponseTypeDef",
    {"Children": Dict[str, str], "NextToken": str},
    total=False,
)


class ClientListObjectChildrenResponseTypeDef(_ClientListObjectChildrenResponseTypeDef):
    """
    Type definition for `ClientListObjectChildren` `Response`

    - **Children** *(dict) --*

      Children structure, which is a map with key as the ``LinkName`` and ``ObjectIdentifier`` as
      the value.

      - *(string) --*

        - *(string) --*

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientListObjectParentPathsObjectReferenceTypeDef = TypedDict(
    "_ClientListObjectParentPathsObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientListObjectParentPathsObjectReferenceTypeDef(
    _ClientListObjectParentPathsObjectReferenceTypeDef
):
    """
    Type definition for `ClientListObjectParentPaths` `ObjectReference`

    The reference that identifies the object whose parent paths are listed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListObjectParentPathsResponsePathToObjectIdentifiersListTypeDef = TypedDict(
    "_ClientListObjectParentPathsResponsePathToObjectIdentifiersListTypeDef",
    {"Path": str, "ObjectIdentifiers": List[str]},
    total=False,
)


class ClientListObjectParentPathsResponsePathToObjectIdentifiersListTypeDef(
    _ClientListObjectParentPathsResponsePathToObjectIdentifiersListTypeDef
):
    """
    Type definition for `ClientListObjectParentPathsResponse` `PathToObjectIdentifiersList`

    Returns the path to the ``ObjectIdentifiers`` that is associated with the directory.

    - **Path** *(string) --*

      The path that is used to identify the object starting from directory root.

    - **ObjectIdentifiers** *(list) --*

      Lists ``ObjectIdentifiers`` starting from directory root to the object in the request.

      - *(string) --*
    """


_ClientListObjectParentPathsResponseTypeDef = TypedDict(
    "_ClientListObjectParentPathsResponseTypeDef",
    {
        "PathToObjectIdentifiersList": List[
            ClientListObjectParentPathsResponsePathToObjectIdentifiersListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListObjectParentPathsResponseTypeDef(
    _ClientListObjectParentPathsResponseTypeDef
):
    """
    Type definition for `ClientListObjectParentPaths` `Response`

    - **PathToObjectIdentifiersList** *(list) --*

      Returns the path to the ``ObjectIdentifiers`` that are associated with the directory.

      - *(dict) --*

        Returns the path to the ``ObjectIdentifiers`` that is associated with the directory.

        - **Path** *(string) --*

          The path that is used to identify the object starting from directory root.

        - **ObjectIdentifiers** *(list) --*

          Lists ``ObjectIdentifiers`` starting from directory root to the object in the request.

          - *(string) --*

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientListObjectParentsObjectReferenceTypeDef = TypedDict(
    "_ClientListObjectParentsObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientListObjectParentsObjectReferenceTypeDef(
    _ClientListObjectParentsObjectReferenceTypeDef
):
    """
    Type definition for `ClientListObjectParents` `ObjectReference`

    The reference that identifies the object for which parent objects are being listed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListObjectParentsResponseParentLinksTypeDef = TypedDict(
    "_ClientListObjectParentsResponseParentLinksTypeDef",
    {"ObjectIdentifier": str, "LinkName": str},
    total=False,
)


class ClientListObjectParentsResponseParentLinksTypeDef(
    _ClientListObjectParentsResponseParentLinksTypeDef
):
    """
    Type definition for `ClientListObjectParentsResponse` `ParentLinks`

    A pair of ObjectIdentifier and LinkName.

    - **ObjectIdentifier** *(string) --*

      The ID that is associated with the object.

    - **LinkName** *(string) --*

      The name of the link between the parent and the child object.
    """


_ClientListObjectParentsResponseTypeDef = TypedDict(
    "_ClientListObjectParentsResponseTypeDef",
    {
        "Parents": Dict[str, str],
        "NextToken": str,
        "ParentLinks": List[ClientListObjectParentsResponseParentLinksTypeDef],
    },
    total=False,
)


class ClientListObjectParentsResponseTypeDef(_ClientListObjectParentsResponseTypeDef):
    """
    Type definition for `ClientListObjectParents` `Response`

    - **Parents** *(dict) --*

      The parent structure, which is a map with key as the ``ObjectIdentifier`` and LinkName as the
      value.

      - *(string) --*

        - *(string) --*

    - **NextToken** *(string) --*

      The pagination token.

    - **ParentLinks** *(list) --*

      Returns a list of parent reference and LinkName Tuples.

      - *(dict) --*

        A pair of ObjectIdentifier and LinkName.

        - **ObjectIdentifier** *(string) --*

          The ID that is associated with the object.

        - **LinkName** *(string) --*

          The name of the link between the parent and the child object.
    """


_ClientListObjectPoliciesObjectReferenceTypeDef = TypedDict(
    "_ClientListObjectPoliciesObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientListObjectPoliciesObjectReferenceTypeDef(
    _ClientListObjectPoliciesObjectReferenceTypeDef
):
    """
    Type definition for `ClientListObjectPolicies` `ObjectReference`

    Reference that identifies the object for which policies will be listed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListObjectPoliciesResponseTypeDef = TypedDict(
    "_ClientListObjectPoliciesResponseTypeDef",
    {"AttachedPolicyIds": List[str], "NextToken": str},
    total=False,
)


class ClientListObjectPoliciesResponseTypeDef(_ClientListObjectPoliciesResponseTypeDef):
    """
    Type definition for `ClientListObjectPolicies` `Response`

    - **AttachedPolicyIds** *(list) --*

      A list of policy ``ObjectIdentifiers`` , that are attached to the object.

      - *(string) --*

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef(
    _ClientListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef
):
    """
    Type definition for `ClientListOutgoingTypedLinksFilterAttributeRangesRange` `EndValue`

    The attribute value to terminate the range at.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef(
    _ClientListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef
):
    """
    Type definition for `ClientListOutgoingTypedLinksFilterAttributeRangesRange` `StartValue`

    The value to start the range at.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_RequiredClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef = TypedDict(
    "_RequiredClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef",
    {"StartMode": str, "EndMode": str},
)
_OptionalClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef = TypedDict(
    "_OptionalClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef",
    {
        "StartValue": ClientListOutgoingTypedLinksFilterAttributeRangesRangeStartValueTypeDef,
        "EndValue": ClientListOutgoingTypedLinksFilterAttributeRangesRangeEndValueTypeDef,
    },
    total=False,
)


class ClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef(
    _RequiredClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef,
    _OptionalClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef,
):
    """
    Type definition for `ClientListOutgoingTypedLinksFilterAttributeRanges` `Range`

    The range of attribute values that are being selected.

    - **StartMode** *(string) --* **[REQUIRED]**

      The inclusive or exclusive range start.

    - **StartValue** *(dict) --*

      The value to start the range at.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.

    - **EndMode** *(string) --* **[REQUIRED]**

      The inclusive or exclusive range end.

    - **EndValue** *(dict) --*

      The attribute value to terminate the range at.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_RequiredClientListOutgoingTypedLinksFilterAttributeRangesTypeDef = TypedDict(
    "_RequiredClientListOutgoingTypedLinksFilterAttributeRangesTypeDef",
    {"Range": ClientListOutgoingTypedLinksFilterAttributeRangesRangeTypeDef},
)
_OptionalClientListOutgoingTypedLinksFilterAttributeRangesTypeDef = TypedDict(
    "_OptionalClientListOutgoingTypedLinksFilterAttributeRangesTypeDef",
    {"AttributeName": str},
    total=False,
)


class ClientListOutgoingTypedLinksFilterAttributeRangesTypeDef(
    _RequiredClientListOutgoingTypedLinksFilterAttributeRangesTypeDef,
    _OptionalClientListOutgoingTypedLinksFilterAttributeRangesTypeDef,
):
    """
    Type definition for `ClientListOutgoingTypedLinks` `FilterAttributeRanges`

    Identifies the range of attributes that are used by a specified filter.

    - **AttributeName** *(string) --*

      The unique name of the typed link attribute.

    - **Range** *(dict) --* **[REQUIRED]**

      The range of attribute values that are being selected.

      - **StartMode** *(string) --* **[REQUIRED]**

        The inclusive or exclusive range start.

      - **StartValue** *(dict) --*

        The value to start the range at.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.

      - **EndMode** *(string) --* **[REQUIRED]**

        The inclusive or exclusive range end.

      - **EndValue** *(dict) --*

        The attribute value to terminate the range at.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.
    """


_ClientListOutgoingTypedLinksFilterTypedLinkTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksFilterTypedLinkTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
)


class ClientListOutgoingTypedLinksFilterTypedLinkTypeDef(
    _ClientListOutgoingTypedLinksFilterTypedLinkTypeDef
):
    """
    Type definition for `ClientListOutgoingTypedLinks` `FilterTypedLink`

    Filters are interpreted in the order of the attributes defined on the typed link facet, not the
    order they are supplied to any API calls.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
      arns .

    - **TypedLinkName** *(string) --* **[REQUIRED]**

      The unique name of the typed link facet.
    """


_ClientListOutgoingTypedLinksObjectReferenceTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientListOutgoingTypedLinksObjectReferenceTypeDef(
    _ClientListOutgoingTypedLinksObjectReferenceTypeDef
):
    """
    Type definition for `ClientListOutgoingTypedLinks` `ObjectReference`

    A reference that identifies the object whose attributes will be listed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef(
    _ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef
):
    """
    Type definition for `ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValues` `Value`

    The value for the typed link.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef(
    _ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef
):
    """
    Type definition for `ClientListOutgoingTypedLinksResponseTypedLinkSpecifiers` `IdentityAttributeValues`

    Identifies the attribute name and value for a typed link.

    - **AttributeName** *(string) --*

      The attribute name of the typed link.

    - **Value** *(dict) --*

      The value for the typed link.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef(
    _ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef
):
    """
    Type definition for `ClientListOutgoingTypedLinksResponseTypedLinkSpecifiers` `SourceObjectReference`

    Identifies the source object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading
      to it from the directory root. Use the link names from each parent/child link to
      construct the path. Path selectors start with a slash (/) and link names are separated
      by slashes. For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
      Cloud Directory. When creating objects, the system will provide you with the identifier
      of the created object. An object’s identifier is immutable and no two objects will ever
      share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef(
    _ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef
):
    """
    Type definition for `ClientListOutgoingTypedLinksResponseTypedLinkSpecifiers` `TargetObjectReference`

    Identifies the target object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading
      to it from the directory root. Use the link names from each parent/child link to
      construct the path. Path selectors start with a slash (/) and link names are separated
      by slashes. For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
      Cloud Directory. When creating objects, the system will provide you with the identifier
      of the created object. An object’s identifier is immutable and no two objects will ever
      share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypedLinkFacetTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypedLinkFacetTypeDef(
    _ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypedLinkFacetTypeDef
):
    """
    Type definition for `ClientListOutgoingTypedLinksResponseTypedLinkSpecifiers` `TypedLinkFacet`

    Identifies the typed link facet that is associated with the typed link.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) that is associated with the schema. For more
      information, see  arns .

    - **TypedLinkName** *(string) --*

      The unique name of the typed link facet.
    """


_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypeDef",
    {
        "TypedLinkFacet": ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypeDef(
    _ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypeDef
):
    """
    Type definition for `ClientListOutgoingTypedLinksResponse` `TypedLinkSpecifiers`

    Contains all the information that is used to uniquely identify a typed link. The parameters
    discussed in this topic are used to uniquely specify the typed link being operated on. The
    AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts
    one as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API
    operations provide typed link specifiers as output. You can also construct a typed link
    specifier from scratch.

    - **TypedLinkFacet** *(dict) --*

      Identifies the typed link facet that is associated with the typed link.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) that is associated with the schema. For more
        information, see  arns .

      - **TypedLinkName** *(string) --*

        The unique name of the typed link facet.

    - **SourceObjectReference** *(dict) --*

      Identifies the source object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading
        to it from the directory root. Use the link names from each parent/child link to
        construct the path. Path selectors start with a slash (/) and link names are separated
        by slashes. For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
        Cloud Directory. When creating objects, the system will provide you with the identifier
        of the created object. An object’s identifier is immutable and no two objects will ever
        share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **TargetObjectReference** *(dict) --*

      Identifies the target object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading
        to it from the directory root. Use the link names from each parent/child link to
        construct the path. Path selectors start with a slash (/) and link names are separated
        by slashes. For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
        Cloud Directory. When creating objects, the system will provide you with the identifier
        of the created object. An object’s identifier is immutable and no two objects will ever
        share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **IdentityAttributeValues** *(list) --*

      Identifies the attribute value to update.

      - *(dict) --*

        Identifies the attribute name and value for a typed link.

        - **AttributeName** *(string) --*

          The attribute name of the typed link.

        - **Value** *(dict) --*

          The value for the typed link.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ClientListOutgoingTypedLinksResponseTypeDef = TypedDict(
    "_ClientListOutgoingTypedLinksResponseTypeDef",
    {
        "TypedLinkSpecifiers": List[
            ClientListOutgoingTypedLinksResponseTypedLinkSpecifiersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListOutgoingTypedLinksResponseTypeDef(
    _ClientListOutgoingTypedLinksResponseTypeDef
):
    """
    Type definition for `ClientListOutgoingTypedLinks` `Response`

    - **TypedLinkSpecifiers** *(list) --*

      Returns a typed link specifier as output.

      - *(dict) --*

        Contains all the information that is used to uniquely identify a typed link. The parameters
        discussed in this topic are used to uniquely specify the typed link being operated on. The
        AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts
        one as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API
        operations provide typed link specifiers as output. You can also construct a typed link
        specifier from scratch.

        - **TypedLinkFacet** *(dict) --*

          Identifies the typed link facet that is associated with the typed link.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) that is associated with the schema. For more
            information, see  arns .

          - **TypedLinkName** *(string) --*

            The unique name of the typed link facet.

        - **SourceObjectReference** *(dict) --*

          Identifies the source object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links leading
            to it from the directory root. Use the link names from each parent/child link to
            construct the path. Path selectors start with a slash (/) and link names are separated
            by slashes. For more information about paths, see `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
            Cloud Directory. When creating objects, the system will provide you with the identifier
            of the created object. An object’s identifier is immutable and no two objects will ever
            share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **TargetObjectReference** *(dict) --*

          Identifies the target object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links leading
            to it from the directory root. Use the link names from each parent/child link to
            construct the path. Path selectors start with a slash (/) and link names are separated
            by slashes. For more information about paths, see `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
            Cloud Directory. When creating objects, the system will provide you with the identifier
            of the created object. An object’s identifier is immutable and no two objects will ever
            share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **IdentityAttributeValues** *(list) --*

          Identifies the attribute value to update.

          - *(dict) --*

            Identifies the attribute name and value for a typed link.

            - **AttributeName** *(string) --*

              The attribute name of the typed link.

            - **Value** *(dict) --*

              The value for the typed link.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientListPolicyAttachmentsPolicyReferenceTypeDef = TypedDict(
    "_ClientListPolicyAttachmentsPolicyReferenceTypeDef", {"Selector": str}, total=False
)


class ClientListPolicyAttachmentsPolicyReferenceTypeDef(
    _ClientListPolicyAttachmentsPolicyReferenceTypeDef
):
    """
    Type definition for `ClientListPolicyAttachments` `PolicyReference`

    The reference that identifies the policy object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientListPolicyAttachmentsResponseTypeDef = TypedDict(
    "_ClientListPolicyAttachmentsResponseTypeDef",
    {"ObjectIdentifiers": List[str], "NextToken": str},
    total=False,
)


class ClientListPolicyAttachmentsResponseTypeDef(
    _ClientListPolicyAttachmentsResponseTypeDef
):
    """
    Type definition for `ClientListPolicyAttachments` `Response`

    - **ObjectIdentifiers** *(list) --*

      A list of ``ObjectIdentifiers`` to which the policy is attached.

      - *(string) --*

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientListPublishedSchemaArnsResponseTypeDef = TypedDict(
    "_ClientListPublishedSchemaArnsResponseTypeDef",
    {"SchemaArns": List[str], "NextToken": str},
    total=False,
)


class ClientListPublishedSchemaArnsResponseTypeDef(
    _ClientListPublishedSchemaArnsResponseTypeDef
):
    """
    Type definition for `ClientListPublishedSchemaArns` `Response`

    - **SchemaArns** *(list) --*

      The ARNs of published schemas.

      - *(string) --*

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientListTagsForResourceResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseTagsTypeDef(
    _ClientListTagsForResourceResponseTagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `Tags`

    The tag structure that contains a tag key and value.

    - **Key** *(string) --*

      The key that is associated with the tag.

    - **Value** *(string) --*

      The value that is associated with the tag.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"Tags": List[ClientListTagsForResourceResponseTagsTypeDef], "NextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **Tags** *(list) --*

      A list of tag key value pairs that are associated with the response.

      - *(dict) --*

        The tag structure that contains a tag key and value.

        - **Key** *(string) --*

          The key that is associated with the tag.

        - **Value** *(string) --*

          The value that is associated with the tag.

    - **NextToken** *(string) --*

      The token to use to retrieve the next page of results. This value is null when there are no
      more results to return.
    """


_ClientListTypedLinkFacetAttributesResponseAttributesDefaultValueTypeDef = TypedDict(
    "_ClientListTypedLinkFacetAttributesResponseAttributesDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientListTypedLinkFacetAttributesResponseAttributesDefaultValueTypeDef(
    _ClientListTypedLinkFacetAttributesResponseAttributesDefaultValueTypeDef
):
    """
    Type definition for `ClientListTypedLinkFacetAttributesResponseAttributes` `DefaultValue`

    The default value of the attribute (if configured).

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientListTypedLinkFacetAttributesResponseAttributesRulesTypeDef = TypedDict(
    "_ClientListTypedLinkFacetAttributesResponseAttributesRulesTypeDef",
    {"Type": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientListTypedLinkFacetAttributesResponseAttributesRulesTypeDef(
    _ClientListTypedLinkFacetAttributesResponseAttributesRulesTypeDef
):
    """
    Type definition for `ClientListTypedLinkFacetAttributesResponseAttributes` `Rules`

    Contains an Amazon Resource Name (ARN) and parameters that are associated with the
    rule.

    - **Type** *(string) --*

      The type of attribute validation rule.

    - **Parameters** *(dict) --*

      The minimum and maximum parameters that are associated with the rule.

      - *(string) --*

        - *(string) --*
    """


_ClientListTypedLinkFacetAttributesResponseAttributesTypeDef = TypedDict(
    "_ClientListTypedLinkFacetAttributesResponseAttributesTypeDef",
    {
        "Name": str,
        "Type": str,
        "DefaultValue": ClientListTypedLinkFacetAttributesResponseAttributesDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[
            str, ClientListTypedLinkFacetAttributesResponseAttributesRulesTypeDef
        ],
        "RequiredBehavior": str,
    },
    total=False,
)


class ClientListTypedLinkFacetAttributesResponseAttributesTypeDef(
    _ClientListTypedLinkFacetAttributesResponseAttributesTypeDef
):
    """
    Type definition for `ClientListTypedLinkFacetAttributesResponse` `Attributes`

    A typed link attribute definition.

    - **Name** *(string) --*

      The unique name of the typed link attribute.

    - **Type** *(string) --*

      The type of the attribute.

    - **DefaultValue** *(dict) --*

      The default value of the attribute (if configured).

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.

    - **IsImmutable** *(boolean) --*

      Whether the attribute is mutable or not.

    - **Rules** *(dict) --*

      Validation rules that are attached to the attribute definition.

      - *(string) --*

        - *(dict) --*

          Contains an Amazon Resource Name (ARN) and parameters that are associated with the
          rule.

          - **Type** *(string) --*

            The type of attribute validation rule.

          - **Parameters** *(dict) --*

            The minimum and maximum parameters that are associated with the rule.

            - *(string) --*

              - *(string) --*

    - **RequiredBehavior** *(string) --*

      The required behavior of the ``TypedLinkAttributeDefinition`` .
    """


_ClientListTypedLinkFacetAttributesResponseTypeDef = TypedDict(
    "_ClientListTypedLinkFacetAttributesResponseTypeDef",
    {
        "Attributes": List[ClientListTypedLinkFacetAttributesResponseAttributesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListTypedLinkFacetAttributesResponseTypeDef(
    _ClientListTypedLinkFacetAttributesResponseTypeDef
):
    """
    Type definition for `ClientListTypedLinkFacetAttributes` `Response`

    - **Attributes** *(list) --*

      An ordered set of attributes associate with the typed link.

      - *(dict) --*

        A typed link attribute definition.

        - **Name** *(string) --*

          The unique name of the typed link attribute.

        - **Type** *(string) --*

          The type of the attribute.

        - **DefaultValue** *(dict) --*

          The default value of the attribute (if configured).

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.

        - **IsImmutable** *(boolean) --*

          Whether the attribute is mutable or not.

        - **Rules** *(dict) --*

          Validation rules that are attached to the attribute definition.

          - *(string) --*

            - *(dict) --*

              Contains an Amazon Resource Name (ARN) and parameters that are associated with the
              rule.

              - **Type** *(string) --*

                The type of attribute validation rule.

              - **Parameters** *(dict) --*

                The minimum and maximum parameters that are associated with the rule.

                - *(string) --*

                  - *(string) --*

        - **RequiredBehavior** *(string) --*

          The required behavior of the ``TypedLinkAttributeDefinition`` .

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientListTypedLinkFacetNamesResponseTypeDef = TypedDict(
    "_ClientListTypedLinkFacetNamesResponseTypeDef",
    {"FacetNames": List[str], "NextToken": str},
    total=False,
)


class ClientListTypedLinkFacetNamesResponseTypeDef(
    _ClientListTypedLinkFacetNamesResponseTypeDef
):
    """
    Type definition for `ClientListTypedLinkFacetNames` `Response`

    - **FacetNames** *(list) --*

      The names of typed link facets that exist within the schema.

      - *(string) --*

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientLookupPolicyObjectReferenceTypeDef = TypedDict(
    "_ClientLookupPolicyObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientLookupPolicyObjectReferenceTypeDef(
    _ClientLookupPolicyObjectReferenceTypeDef
):
    """
    Type definition for `ClientLookupPolicy` `ObjectReference`

    Reference that identifies the object whose policies will be looked up.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientLookupPolicyResponsePolicyToPathListPoliciesTypeDef = TypedDict(
    "_ClientLookupPolicyResponsePolicyToPathListPoliciesTypeDef",
    {"PolicyId": str, "ObjectIdentifier": str, "PolicyType": str},
    total=False,
)


class ClientLookupPolicyResponsePolicyToPathListPoliciesTypeDef(
    _ClientLookupPolicyResponsePolicyToPathListPoliciesTypeDef
):
    """
    Type definition for `ClientLookupPolicyResponsePolicyToPathList` `Policies`

    Contains the ``PolicyType`` , ``PolicyId`` , and the ``ObjectIdentifier`` to which it
    is attached. For more information, see `Policies
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
    .

    - **PolicyId** *(string) --*

      The ID of ``PolicyAttachment`` .

    - **ObjectIdentifier** *(string) --*

      The ``ObjectIdentifier`` that is associated with ``PolicyAttachment`` .

    - **PolicyType** *(string) --*

      The type of policy that can be associated with ``PolicyAttachment`` .
    """


_ClientLookupPolicyResponsePolicyToPathListTypeDef = TypedDict(
    "_ClientLookupPolicyResponsePolicyToPathListTypeDef",
    {
        "Path": str,
        "Policies": List[ClientLookupPolicyResponsePolicyToPathListPoliciesTypeDef],
    },
    total=False,
)


class ClientLookupPolicyResponsePolicyToPathListTypeDef(
    _ClientLookupPolicyResponsePolicyToPathListTypeDef
):
    """
    Type definition for `ClientLookupPolicyResponse` `PolicyToPathList`

    Used when a regular object exists in a  Directory and you want to find all of the policies
    that are associated with that object and the parent to that object.

    - **Path** *(string) --*

      The path that is referenced from the root.

    - **Policies** *(list) --*

      List of policy objects.

      - *(dict) --*

        Contains the ``PolicyType`` , ``PolicyId`` , and the ``ObjectIdentifier`` to which it
        is attached. For more information, see `Policies
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
        .

        - **PolicyId** *(string) --*

          The ID of ``PolicyAttachment`` .

        - **ObjectIdentifier** *(string) --*

          The ``ObjectIdentifier`` that is associated with ``PolicyAttachment`` .

        - **PolicyType** *(string) --*

          The type of policy that can be associated with ``PolicyAttachment`` .
    """


_ClientLookupPolicyResponseTypeDef = TypedDict(
    "_ClientLookupPolicyResponseTypeDef",
    {
        "PolicyToPathList": List[ClientLookupPolicyResponsePolicyToPathListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientLookupPolicyResponseTypeDef(_ClientLookupPolicyResponseTypeDef):
    """
    Type definition for `ClientLookupPolicy` `Response`

    - **PolicyToPathList** *(list) --*

      Provides list of path to policies. Policies contain ``PolicyId`` , ``ObjectIdentifier`` , and
      ``PolicyType`` . For more information, see `Policies
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
      .

      - *(dict) --*

        Used when a regular object exists in a  Directory and you want to find all of the policies
        that are associated with that object and the parent to that object.

        - **Path** *(string) --*

          The path that is referenced from the root.

        - **Policies** *(list) --*

          List of policy objects.

          - *(dict) --*

            Contains the ``PolicyType`` , ``PolicyId`` , and the ``ObjectIdentifier`` to which it
            is attached. For more information, see `Policies
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
            .

            - **PolicyId** *(string) --*

              The ID of ``PolicyAttachment`` .

            - **ObjectIdentifier** *(string) --*

              The ``ObjectIdentifier`` that is associated with ``PolicyAttachment`` .

            - **PolicyType** *(string) --*

              The type of policy that can be associated with ``PolicyAttachment`` .

    - **NextToken** *(string) --*

      The pagination token.
    """


_ClientPublishSchemaResponseTypeDef = TypedDict(
    "_ClientPublishSchemaResponseTypeDef", {"PublishedSchemaArn": str}, total=False
)


class ClientPublishSchemaResponseTypeDef(_ClientPublishSchemaResponseTypeDef):
    """
    Type definition for `ClientPublishSchema` `Response`

    - **PublishedSchemaArn** *(string) --*

      The ARN that is associated with the published schema. For more information, see  arns .
    """


_ClientPutSchemaFromJsonResponseTypeDef = TypedDict(
    "_ClientPutSchemaFromJsonResponseTypeDef", {"Arn": str}, total=False
)


class ClientPutSchemaFromJsonResponseTypeDef(_ClientPutSchemaFromJsonResponseTypeDef):
    """
    Type definition for `ClientPutSchemaFromJson` `Response`

    - **Arn** *(string) --*

      The ARN of the schema to update.
    """


_ClientRemoveFacetFromObjectObjectReferenceTypeDef = TypedDict(
    "_ClientRemoveFacetFromObjectObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ClientRemoveFacetFromObjectObjectReferenceTypeDef(
    _ClientRemoveFacetFromObjectObjectReferenceTypeDef
):
    """
    Type definition for `ClientRemoveFacetFromObject` `ObjectReference`

    A reference to the object to remove the facet from.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientRemoveFacetFromObjectSchemaFacetTypeDef = TypedDict(
    "_ClientRemoveFacetFromObjectSchemaFacetTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ClientRemoveFacetFromObjectSchemaFacetTypeDef(
    _ClientRemoveFacetFromObjectSchemaFacetTypeDef
):
    """
    Type definition for `ClientRemoveFacetFromObject` `SchemaFacet`

    The facet to remove. See  SchemaFacet for details.

    - **SchemaArn** *(string) --*

      The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place
      Schema Upgrade
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
      for a description of when to provide minor versions.

    - **FacetName** *(string) --*

      The name of the facet.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    The tag structure that contains a tag key and value.

    - **Key** *(string) --*

      The key that is associated with the tag.

    - **Value** *(string) --*

      The value that is associated with the tag.
    """


_ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionDefaultValueTypeDef = TypedDict(
    "_ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionDefaultValueTypeDef(
    _ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionDefaultValueTypeDef
):
    """
    Type definition for `ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinition` `DefaultValue`

    The default value of the attribute (if configured).

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionRulesTypeDef = TypedDict(
    "_ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionRulesTypeDef",
    {"Type": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionRulesTypeDef(
    _ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionRulesTypeDef
):
    """
    Type definition for `ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinition` `Rules`

    Contains an Amazon Resource Name (ARN) and parameters that are associated with the
    rule.

    - **Type** *(string) --*

      The type of attribute validation rule.

    - **Parameters** *(dict) --*

      The minimum and maximum parameters that are associated with the rule.

      - *(string) --*

        - *(string) --*
    """


_RequiredClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef = TypedDict(
    "_RequiredClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef",
    {"Type": str},
)
_OptionalClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef = TypedDict(
    "_OptionalClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef",
    {
        "DefaultValue": ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[
            str,
            ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionRulesTypeDef,
        ],
    },
    total=False,
)


class ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef(
    _RequiredClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef,
    _OptionalClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef,
):
    """
    Type definition for `ClientUpdateFacetAttributeUpdatesAttribute` `AttributeDefinition`

    A facet attribute consists of either a definition or a reference. This structure contains
    the attribute definition. See `Attribute References
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
    for more information.

    - **Type** *(string) --* **[REQUIRED]**

      The type of the attribute.

    - **DefaultValue** *(dict) --*

      The default value of the attribute (if configured).

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.

    - **IsImmutable** *(boolean) --*

      Whether the attribute is mutable or not.

    - **Rules** *(dict) --*

      Validation rules attached to the attribute definition.

      - *(string) --*

        - *(dict) --*

          Contains an Amazon Resource Name (ARN) and parameters that are associated with the
          rule.

          - **Type** *(string) --*

            The type of attribute validation rule.

          - **Parameters** *(dict) --*

            The minimum and maximum parameters that are associated with the rule.

            - *(string) --*

              - *(string) --*
    """


_ClientUpdateFacetAttributeUpdatesAttributeAttributeReferenceTypeDef = TypedDict(
    "_ClientUpdateFacetAttributeUpdatesAttributeAttributeReferenceTypeDef",
    {"TargetFacetName": str, "TargetAttributeName": str},
)


class ClientUpdateFacetAttributeUpdatesAttributeAttributeReferenceTypeDef(
    _ClientUpdateFacetAttributeUpdatesAttributeAttributeReferenceTypeDef
):
    """
    Type definition for `ClientUpdateFacetAttributeUpdatesAttribute` `AttributeReference`

    An attribute reference that is associated with the attribute. See `Attribute References
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
    for more information.

    - **TargetFacetName** *(string) --* **[REQUIRED]**

      The target facet name that is associated with the facet reference. See `Attribute
      References
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
      for more information.

    - **TargetAttributeName** *(string) --* **[REQUIRED]**

      The target attribute name that is associated with the facet reference. See `Attribute
      References
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
      for more information.
    """


_RequiredClientUpdateFacetAttributeUpdatesAttributeTypeDef = TypedDict(
    "_RequiredClientUpdateFacetAttributeUpdatesAttributeTypeDef", {"Name": str}
)
_OptionalClientUpdateFacetAttributeUpdatesAttributeTypeDef = TypedDict(
    "_OptionalClientUpdateFacetAttributeUpdatesAttributeTypeDef",
    {
        "AttributeDefinition": ClientUpdateFacetAttributeUpdatesAttributeAttributeDefinitionTypeDef,
        "AttributeReference": ClientUpdateFacetAttributeUpdatesAttributeAttributeReferenceTypeDef,
        "RequiredBehavior": str,
    },
    total=False,
)


class ClientUpdateFacetAttributeUpdatesAttributeTypeDef(
    _RequiredClientUpdateFacetAttributeUpdatesAttributeTypeDef,
    _OptionalClientUpdateFacetAttributeUpdatesAttributeTypeDef,
):
    """
    Type definition for `ClientUpdateFacetAttributeUpdates` `Attribute`

    The attribute to update.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the facet attribute.

    - **AttributeDefinition** *(dict) --*

      A facet attribute consists of either a definition or a reference. This structure contains
      the attribute definition. See `Attribute References
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
      for more information.

      - **Type** *(string) --* **[REQUIRED]**

        The type of the attribute.

      - **DefaultValue** *(dict) --*

        The default value of the attribute (if configured).

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.

      - **IsImmutable** *(boolean) --*

        Whether the attribute is mutable or not.

      - **Rules** *(dict) --*

        Validation rules attached to the attribute definition.

        - *(string) --*

          - *(dict) --*

            Contains an Amazon Resource Name (ARN) and parameters that are associated with the
            rule.

            - **Type** *(string) --*

              The type of attribute validation rule.

            - **Parameters** *(dict) --*

              The minimum and maximum parameters that are associated with the rule.

              - *(string) --*

                - *(string) --*

    - **AttributeReference** *(dict) --*

      An attribute reference that is associated with the attribute. See `Attribute References
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
      for more information.

      - **TargetFacetName** *(string) --* **[REQUIRED]**

        The target facet name that is associated with the facet reference. See `Attribute
        References
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
        for more information.

      - **TargetAttributeName** *(string) --* **[REQUIRED]**

        The target attribute name that is associated with the facet reference. See `Attribute
        References
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
        for more information.

    - **RequiredBehavior** *(string) --*

      The required behavior of the ``FacetAttribute`` .
    """


_ClientUpdateFacetAttributeUpdatesTypeDef = TypedDict(
    "_ClientUpdateFacetAttributeUpdatesTypeDef",
    {"Attribute": ClientUpdateFacetAttributeUpdatesAttributeTypeDef, "Action": str},
    total=False,
)


class ClientUpdateFacetAttributeUpdatesTypeDef(
    _ClientUpdateFacetAttributeUpdatesTypeDef
):
    """
    Type definition for `ClientUpdateFacet` `AttributeUpdates`

    A structure that contains information used to update an attribute.

    - **Attribute** *(dict) --*

      The attribute to update.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the facet attribute.

      - **AttributeDefinition** *(dict) --*

        A facet attribute consists of either a definition or a reference. This structure contains
        the attribute definition. See `Attribute References
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
        for more information.

        - **Type** *(string) --* **[REQUIRED]**

          The type of the attribute.

        - **DefaultValue** *(dict) --*

          The default value of the attribute (if configured).

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.

        - **IsImmutable** *(boolean) --*

          Whether the attribute is mutable or not.

        - **Rules** *(dict) --*

          Validation rules attached to the attribute definition.

          - *(string) --*

            - *(dict) --*

              Contains an Amazon Resource Name (ARN) and parameters that are associated with the
              rule.

              - **Type** *(string) --*

                The type of attribute validation rule.

              - **Parameters** *(dict) --*

                The minimum and maximum parameters that are associated with the rule.

                - *(string) --*

                  - *(string) --*

      - **AttributeReference** *(dict) --*

        An attribute reference that is associated with the attribute. See `Attribute References
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
        for more information.

        - **TargetFacetName** *(string) --* **[REQUIRED]**

          The target facet name that is associated with the facet reference. See `Attribute
          References
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
          for more information.

        - **TargetAttributeName** *(string) --* **[REQUIRED]**

          The target attribute name that is associated with the facet reference. See `Attribute
          References
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
          for more information.

      - **RequiredBehavior** *(string) --*

        The required behavior of the ``FacetAttribute`` .

    - **Action** *(string) --*

      The action to perform when updating the attribute.
    """


_ClientUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef = TypedDict(
    "_ClientUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef(
    _ClientUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef
):
    """
    Type definition for `ClientUpdateLinkAttributesAttributeUpdatesAttributeAction` `AttributeUpdateValue`

    The value that you want to update to.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef = TypedDict(
    "_ClientUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef",
    {
        "AttributeActionType": str,
        "AttributeUpdateValue": ClientUpdateLinkAttributesAttributeUpdatesAttributeActionAttributeUpdateValueTypeDef,
    },
    total=False,
)


class ClientUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef(
    _ClientUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef
):
    """
    Type definition for `ClientUpdateLinkAttributesAttributeUpdates` `AttributeAction`

    The action to perform as part of the attribute update.

    - **AttributeActionType** *(string) --*

      A type that can be either ``UPDATE_OR_CREATE`` or ``DELETE`` .

    - **AttributeUpdateValue** *(dict) --*

      The value that you want to update to.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef = TypedDict(
    "_ClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
)


class ClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef(
    _ClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef
):
    """
    Type definition for `ClientUpdateLinkAttributesAttributeUpdates` `AttributeKey`

    The key of the attribute being updated.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --* **[REQUIRED]**

      The name of the facet that the attribute exists within.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.
    """


_ClientUpdateLinkAttributesAttributeUpdatesTypeDef = TypedDict(
    "_ClientUpdateLinkAttributesAttributeUpdatesTypeDef",
    {
        "AttributeKey": ClientUpdateLinkAttributesAttributeUpdatesAttributeKeyTypeDef,
        "AttributeAction": ClientUpdateLinkAttributesAttributeUpdatesAttributeActionTypeDef,
    },
    total=False,
)


class ClientUpdateLinkAttributesAttributeUpdatesTypeDef(
    _ClientUpdateLinkAttributesAttributeUpdatesTypeDef
):
    """
    Type definition for `ClientUpdateLinkAttributes` `AttributeUpdates`

    Structure that contains attribute update information.

    - **AttributeKey** *(dict) --*

      The key of the attribute being updated.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --* **[REQUIRED]**

        The name of the facet that the attribute exists within.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the attribute.

    - **AttributeAction** *(dict) --*

      The action to perform as part of the attribute update.

      - **AttributeActionType** *(string) --*

        A type that can be either ``UPDATE_OR_CREATE`` or ``DELETE`` .

      - **AttributeUpdateValue** *(dict) --*

        The value that you want to update to.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.
    """


_ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef(
    _ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef
):
    """
    Type definition for `ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValues` `Value`

    The value for the typed link.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef = TypedDict(
    "_ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesValueTypeDef,
    },
)


class ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef(
    _ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
):
    """
    Type definition for `ClientUpdateLinkAttributesTypedLinkSpecifier` `IdentityAttributeValues`

    Identifies the attribute name and value for a typed link.

    - **AttributeName** *(string) --* **[REQUIRED]**

      The attribute name of the typed link.

    - **Value** *(dict) --* **[REQUIRED]**

      The value for the typed link.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef = TypedDict(
    "_ClientUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef(
    _ClientUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef
):
    """
    Type definition for `ClientUpdateLinkAttributesTypedLinkSpecifier` `SourceObjectReference`

    Identifies the source object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the
      path. Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef = TypedDict(
    "_ClientUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef(
    _ClientUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef
):
    """
    Type definition for `ClientUpdateLinkAttributesTypedLinkSpecifier` `TargetObjectReference`

    Identifies the target object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the
      path. Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the
      same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef = TypedDict(
    "_ClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
)


class ClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef(
    _ClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef
):
    """
    Type definition for `ClientUpdateLinkAttributesTypedLinkSpecifier` `TypedLinkFacet`

    Identifies the typed link facet that is associated with the typed link.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
      arns .

    - **TypedLinkName** *(string) --* **[REQUIRED]**

      The unique name of the typed link facet.
    """


_ClientUpdateLinkAttributesTypedLinkSpecifierTypeDef = TypedDict(
    "_ClientUpdateLinkAttributesTypedLinkSpecifierTypeDef",
    {
        "TypedLinkFacet": ClientUpdateLinkAttributesTypedLinkSpecifierTypedLinkFacetTypeDef,
        "SourceObjectReference": ClientUpdateLinkAttributesTypedLinkSpecifierSourceObjectReferenceTypeDef,
        "TargetObjectReference": ClientUpdateLinkAttributesTypedLinkSpecifierTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ClientUpdateLinkAttributesTypedLinkSpecifierIdentityAttributeValuesTypeDef
        ],
    },
)


class ClientUpdateLinkAttributesTypedLinkSpecifierTypeDef(
    _ClientUpdateLinkAttributesTypedLinkSpecifierTypeDef
):
    """
    Type definition for `ClientUpdateLinkAttributes` `TypedLinkSpecifier`

    Allows a typed link specifier to be accepted as input.

    - **TypedLinkFacet** *(dict) --* **[REQUIRED]**

      Identifies the typed link facet that is associated with the typed link.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
        arns .

      - **TypedLinkName** *(string) --* **[REQUIRED]**

        The unique name of the typed link facet.

    - **SourceObjectReference** *(dict) --* **[REQUIRED]**

      Identifies the source object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to it
        from the directory root. Use the link names from each parent/child link to construct the
        path. Path selectors start with a slash (/) and link names are separated by slashes. For more
        information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share the
        same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **TargetObjectReference** *(dict) --* **[REQUIRED]**

      Identifies the target object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading to it
        from the directory root. Use the link names from each parent/child link to construct the
        path. Path selectors start with a slash (/) and link names are separated by slashes. For more
        information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
        Directory. When creating objects, the system will provide you with the identifier of the
        created object. An object’s identifier is immutable and no two objects will ever share the
        same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **IdentityAttributeValues** *(list) --* **[REQUIRED]**

      Identifies the attribute value to update.

      - *(dict) --*

        Identifies the attribute name and value for a typed link.

        - **AttributeName** *(string) --* **[REQUIRED]**

          The attribute name of the typed link.

        - **Value** *(dict) --* **[REQUIRED]**

          The value for the typed link.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef = TypedDict(
    "_ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef(
    _ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef
):
    """
    Type definition for `ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeAction` `ObjectAttributeUpdateValue`

    The value that you want to update to.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef = TypedDict(
    "_ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef",
    {
        "ObjectAttributeActionType": str,
        "ObjectAttributeUpdateValue": ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionObjectAttributeUpdateValueTypeDef,
    },
    total=False,
)


class ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef(
    _ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef
):
    """
    Type definition for `ClientUpdateObjectAttributesAttributeUpdates` `ObjectAttributeAction`

    The action to perform as part of the attribute update.

    - **ObjectAttributeActionType** *(string) --*

      A type that can be either ``Update`` or ``Delete`` .

    - **ObjectAttributeUpdateValue** *(dict) --*

      The value that you want to update to.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef = TypedDict(
    "_ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
)


class ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef(
    _ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef
):
    """
    Type definition for `ClientUpdateObjectAttributesAttributeUpdates` `ObjectAttributeKey`

    The key of the attribute being updated.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --* **[REQUIRED]**

      The name of the facet that the attribute exists within.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.
    """


_ClientUpdateObjectAttributesAttributeUpdatesTypeDef = TypedDict(
    "_ClientUpdateObjectAttributesAttributeUpdatesTypeDef",
    {
        "ObjectAttributeKey": ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeKeyTypeDef,
        "ObjectAttributeAction": ClientUpdateObjectAttributesAttributeUpdatesObjectAttributeActionTypeDef,
    },
    total=False,
)


class ClientUpdateObjectAttributesAttributeUpdatesTypeDef(
    _ClientUpdateObjectAttributesAttributeUpdatesTypeDef
):
    """
    Type definition for `ClientUpdateObjectAttributes` `AttributeUpdates`

    Structure that contains attribute update information.

    - **ObjectAttributeKey** *(dict) --*

      The key of the attribute being updated.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --* **[REQUIRED]**

        The name of the facet that the attribute exists within.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the attribute.

    - **ObjectAttributeAction** *(dict) --*

      The action to perform as part of the attribute update.

      - **ObjectAttributeActionType** *(string) --*

        A type that can be either ``Update`` or ``Delete`` .

      - **ObjectAttributeUpdateValue** *(dict) --*

        The value that you want to update to.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.
    """


_ClientUpdateObjectAttributesObjectReferenceTypeDef = TypedDict(
    "_ClientUpdateObjectAttributesObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ClientUpdateObjectAttributesObjectReferenceTypeDef(
    _ClientUpdateObjectAttributesObjectReferenceTypeDef
):
    """
    Type definition for `ClientUpdateObjectAttributes` `ObjectReference`

    The reference that identifies the object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ClientUpdateObjectAttributesResponseTypeDef = TypedDict(
    "_ClientUpdateObjectAttributesResponseTypeDef",
    {"ObjectIdentifier": str},
    total=False,
)


class ClientUpdateObjectAttributesResponseTypeDef(
    _ClientUpdateObjectAttributesResponseTypeDef
):
    """
    Type definition for `ClientUpdateObjectAttributes` `Response`

    - **ObjectIdentifier** *(string) --*

      The ``ObjectIdentifier`` of the updated object.
    """


_ClientUpdateSchemaResponseTypeDef = TypedDict(
    "_ClientUpdateSchemaResponseTypeDef", {"SchemaArn": str}, total=False
)


class ClientUpdateSchemaResponseTypeDef(_ClientUpdateSchemaResponseTypeDef):
    """
    Type definition for `ClientUpdateSchema` `Response`

    - **SchemaArn** *(string) --*

      The ARN that is associated with the updated schema. For more information, see  arns .
    """


_ClientUpdateTypedLinkFacetAttributeUpdatesAttributeDefaultValueTypeDef = TypedDict(
    "_ClientUpdateTypedLinkFacetAttributeUpdatesAttributeDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ClientUpdateTypedLinkFacetAttributeUpdatesAttributeDefaultValueTypeDef(
    _ClientUpdateTypedLinkFacetAttributeUpdatesAttributeDefaultValueTypeDef
):
    """
    Type definition for `ClientUpdateTypedLinkFacetAttributeUpdatesAttribute` `DefaultValue`

    The default value of the attribute (if configured).

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ClientUpdateTypedLinkFacetAttributeUpdatesAttributeRulesTypeDef = TypedDict(
    "_ClientUpdateTypedLinkFacetAttributeUpdatesAttributeRulesTypeDef",
    {"Type": str, "Parameters": Dict[str, str]},
    total=False,
)


class ClientUpdateTypedLinkFacetAttributeUpdatesAttributeRulesTypeDef(
    _ClientUpdateTypedLinkFacetAttributeUpdatesAttributeRulesTypeDef
):
    """
    Type definition for `ClientUpdateTypedLinkFacetAttributeUpdatesAttribute` `Rules`

    Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.

    - **Type** *(string) --*

      The type of attribute validation rule.

    - **Parameters** *(dict) --*

      The minimum and maximum parameters that are associated with the rule.

      - *(string) --*

        - *(string) --*
    """


_RequiredClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef = TypedDict(
    "_RequiredClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef",
    {"Name": str, "Type": str, "RequiredBehavior": str},
)
_OptionalClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef = TypedDict(
    "_OptionalClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef",
    {
        "DefaultValue": ClientUpdateTypedLinkFacetAttributeUpdatesAttributeDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[
            str, ClientUpdateTypedLinkFacetAttributeUpdatesAttributeRulesTypeDef
        ],
    },
    total=False,
)


class ClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef(
    _RequiredClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef,
    _OptionalClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef,
):
    """
    Type definition for `ClientUpdateTypedLinkFacetAttributeUpdates` `Attribute`

    The attribute to update.

    - **Name** *(string) --* **[REQUIRED]**

      The unique name of the typed link attribute.

    - **Type** *(string) --* **[REQUIRED]**

      The type of the attribute.

    - **DefaultValue** *(dict) --*

      The default value of the attribute (if configured).

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.

    - **IsImmutable** *(boolean) --*

      Whether the attribute is mutable or not.

    - **Rules** *(dict) --*

      Validation rules that are attached to the attribute definition.

      - *(string) --*

        - *(dict) --*

          Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.

          - **Type** *(string) --*

            The type of attribute validation rule.

          - **Parameters** *(dict) --*

            The minimum and maximum parameters that are associated with the rule.

            - *(string) --*

              - *(string) --*

    - **RequiredBehavior** *(string) --* **[REQUIRED]**

      The required behavior of the ``TypedLinkAttributeDefinition`` .
    """


_ClientUpdateTypedLinkFacetAttributeUpdatesTypeDef = TypedDict(
    "_ClientUpdateTypedLinkFacetAttributeUpdatesTypeDef",
    {
        "Attribute": ClientUpdateTypedLinkFacetAttributeUpdatesAttributeTypeDef,
        "Action": str,
    },
)


class ClientUpdateTypedLinkFacetAttributeUpdatesTypeDef(
    _ClientUpdateTypedLinkFacetAttributeUpdatesTypeDef
):
    """
    Type definition for `ClientUpdateTypedLinkFacet` `AttributeUpdates`

    A typed link facet attribute update.

    - **Attribute** *(dict) --* **[REQUIRED]**

      The attribute to update.

      - **Name** *(string) --* **[REQUIRED]**

        The unique name of the typed link attribute.

      - **Type** *(string) --* **[REQUIRED]**

        The type of the attribute.

      - **DefaultValue** *(dict) --*

        The default value of the attribute (if configured).

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.

      - **IsImmutable** *(boolean) --*

        Whether the attribute is mutable or not.

      - **Rules** *(dict) --*

        Validation rules that are attached to the attribute definition.

        - *(string) --*

          - *(dict) --*

            Contains an Amazon Resource Name (ARN) and parameters that are associated with the rule.

            - **Type** *(string) --*

              The type of attribute validation rule.

            - **Parameters** *(dict) --*

              The minimum and maximum parameters that are associated with the rule.

              - *(string) --*

                - *(string) --*

      - **RequiredBehavior** *(string) --* **[REQUIRED]**

        The required behavior of the ``TypedLinkAttributeDefinition`` .

    - **Action** *(string) --* **[REQUIRED]**

      The action to perform when updating the attribute.
    """


_ClientUpgradeAppliedSchemaResponseTypeDef = TypedDict(
    "_ClientUpgradeAppliedSchemaResponseTypeDef",
    {"UpgradedSchemaArn": str, "DirectoryArn": str},
    total=False,
)


class ClientUpgradeAppliedSchemaResponseTypeDef(
    _ClientUpgradeAppliedSchemaResponseTypeDef
):
    """
    Type definition for `ClientUpgradeAppliedSchema` `Response`

    - **UpgradedSchemaArn** *(string) --*

      The ARN of the upgraded schema that is returned as part of the response.

    - **DirectoryArn** *(string) --*

      The ARN of the directory that is returned as part of the response.
    """


_ClientUpgradePublishedSchemaResponseTypeDef = TypedDict(
    "_ClientUpgradePublishedSchemaResponseTypeDef",
    {"UpgradedSchemaArn": str},
    total=False,
)


class ClientUpgradePublishedSchemaResponseTypeDef(
    _ClientUpgradePublishedSchemaResponseTypeDef
):
    """
    Type definition for `ClientUpgradePublishedSchema` `Response`

    - **UpgradedSchemaArn** *(string) --*

      The ARN of the upgraded schema that is returned as part of the response.
    """


_ListAppliedSchemaArnsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAppliedSchemaArnsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAppliedSchemaArnsPaginatePaginationConfigTypeDef(
    _ListAppliedSchemaArnsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAppliedSchemaArnsPaginate` `PaginationConfig`

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


_ListAppliedSchemaArnsPaginateResponseTypeDef = TypedDict(
    "_ListAppliedSchemaArnsPaginateResponseTypeDef",
    {"SchemaArns": List[str]},
    total=False,
)


class ListAppliedSchemaArnsPaginateResponseTypeDef(
    _ListAppliedSchemaArnsPaginateResponseTypeDef
):
    """
    Type definition for `ListAppliedSchemaArnsPaginate` `Response`

    - **SchemaArns** *(list) --*

      The ARNs of schemas that are applied to the directory.

      - *(string) --*
    """


_ListAttachedIndicesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAttachedIndicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAttachedIndicesPaginatePaginationConfigTypeDef(
    _ListAttachedIndicesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAttachedIndicesPaginate` `PaginationConfig`

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


_ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef = TypedDict(
    "_ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef(
    _ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef
):
    """
    Type definition for `ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributes` `Key`

    The key of the attribute.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --*

      The name of the facet that the attribute exists within.

    - **Name** *(string) --*

      The name of the attribute.
    """


_ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef = TypedDict(
    "_ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef(
    _ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef
):
    """
    Type definition for `ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributes` `Value`

    The value of the attribute.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesTypeDef = TypedDict(
    "_ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesTypeDef",
    {
        "Key": ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef,
        "Value": ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef,
    },
    total=False,
)


class ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesTypeDef(
    _ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesTypeDef
):
    """
    Type definition for `ListAttachedIndicesPaginateResponseIndexAttachments` `IndexedAttributes`

    The combination of an attribute key and an attribute value.

    - **Key** *(dict) --*

      The key of the attribute.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --*

        The name of the facet that the attribute exists within.

      - **Name** *(string) --*

        The name of the attribute.

    - **Value** *(dict) --*

      The value of the attribute.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ListAttachedIndicesPaginateResponseIndexAttachmentsTypeDef = TypedDict(
    "_ListAttachedIndicesPaginateResponseIndexAttachmentsTypeDef",
    {
        "IndexedAttributes": List[
            ListAttachedIndicesPaginateResponseIndexAttachmentsIndexedAttributesTypeDef
        ],
        "ObjectIdentifier": str,
    },
    total=False,
)


class ListAttachedIndicesPaginateResponseIndexAttachmentsTypeDef(
    _ListAttachedIndicesPaginateResponseIndexAttachmentsTypeDef
):
    """
    Type definition for `ListAttachedIndicesPaginateResponse` `IndexAttachments`

    Represents an index and an attached object.

    - **IndexedAttributes** *(list) --*

      The indexed attribute values.

      - *(dict) --*

        The combination of an attribute key and an attribute value.

        - **Key** *(dict) --*

          The key of the attribute.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

          - **FacetName** *(string) --*

            The name of the facet that the attribute exists within.

          - **Name** *(string) --*

            The name of the attribute.

        - **Value** *(dict) --*

          The value of the attribute.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.

    - **ObjectIdentifier** *(string) --*

      In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to the index.
      In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the index attached to
      the object. This field will always contain the ``ObjectIdentifier`` of the object on the
      opposite side of the attachment specified in the query.
    """


_ListAttachedIndicesPaginateResponseTypeDef = TypedDict(
    "_ListAttachedIndicesPaginateResponseTypeDef",
    {
        "IndexAttachments": List[
            ListAttachedIndicesPaginateResponseIndexAttachmentsTypeDef
        ]
    },
    total=False,
)


class ListAttachedIndicesPaginateResponseTypeDef(
    _ListAttachedIndicesPaginateResponseTypeDef
):
    """
    Type definition for `ListAttachedIndicesPaginate` `Response`

    - **IndexAttachments** *(list) --*

      The indices attached to the specified object.

      - *(dict) --*

        Represents an index and an attached object.

        - **IndexedAttributes** *(list) --*

          The indexed attribute values.

          - *(dict) --*

            The combination of an attribute key and an attribute value.

            - **Key** *(dict) --*

              The key of the attribute.

              - **SchemaArn** *(string) --*

                The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

              - **FacetName** *(string) --*

                The name of the facet that the attribute exists within.

              - **Name** *(string) --*

                The name of the attribute.

            - **Value** *(dict) --*

              The value of the attribute.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

        - **ObjectIdentifier** *(string) --*

          In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to the index.
          In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the index attached to
          the object. This field will always contain the ``ObjectIdentifier`` of the object on the
          opposite side of the attachment specified in the query.
    """


_ListAttachedIndicesPaginateTargetReferenceTypeDef = TypedDict(
    "_ListAttachedIndicesPaginateTargetReferenceTypeDef", {"Selector": str}, total=False
)


class ListAttachedIndicesPaginateTargetReferenceTypeDef(
    _ListAttachedIndicesPaginateTargetReferenceTypeDef
):
    """
    Type definition for `ListAttachedIndicesPaginate` `TargetReference`

    A reference to the object that has indices attached.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListDevelopmentSchemaArnsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDevelopmentSchemaArnsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDevelopmentSchemaArnsPaginatePaginationConfigTypeDef(
    _ListDevelopmentSchemaArnsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDevelopmentSchemaArnsPaginate` `PaginationConfig`

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


_ListDevelopmentSchemaArnsPaginateResponseTypeDef = TypedDict(
    "_ListDevelopmentSchemaArnsPaginateResponseTypeDef",
    {"SchemaArns": List[str]},
    total=False,
)


class ListDevelopmentSchemaArnsPaginateResponseTypeDef(
    _ListDevelopmentSchemaArnsPaginateResponseTypeDef
):
    """
    Type definition for `ListDevelopmentSchemaArnsPaginate` `Response`

    - **SchemaArns** *(list) --*

      The ARNs of retrieved development schemas.

      - *(string) --*
    """


_ListDirectoriesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDirectoriesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDirectoriesPaginatePaginationConfigTypeDef(
    _ListDirectoriesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDirectoriesPaginate` `PaginationConfig`

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


_ListDirectoriesPaginateResponseDirectoriesTypeDef = TypedDict(
    "_ListDirectoriesPaginateResponseDirectoriesTypeDef",
    {"Name": str, "DirectoryArn": str, "State": str, "CreationDateTime": datetime},
    total=False,
)


class ListDirectoriesPaginateResponseDirectoriesTypeDef(
    _ListDirectoriesPaginateResponseDirectoriesTypeDef
):
    """
    Type definition for `ListDirectoriesPaginateResponse` `Directories`

    Directory structure that includes the directory name and directory ARN.

    - **Name** *(string) --*

      The name of the directory.

    - **DirectoryArn** *(string) --*

      The Amazon Resource Name (ARN) that is associated with the directory. For more
      information, see  arns .

    - **State** *(string) --*

      The state of the directory. Can be either ``Enabled`` , ``Disabled`` , or ``Deleted`` .

    - **CreationDateTime** *(datetime) --*

      The date and time when the directory was created.
    """


_ListDirectoriesPaginateResponseTypeDef = TypedDict(
    "_ListDirectoriesPaginateResponseTypeDef",
    {"Directories": List[ListDirectoriesPaginateResponseDirectoriesTypeDef]},
    total=False,
)


class ListDirectoriesPaginateResponseTypeDef(_ListDirectoriesPaginateResponseTypeDef):
    """
    Type definition for `ListDirectoriesPaginate` `Response`

    - **Directories** *(list) --*

      Lists all directories that are associated with your account in pagination fashion.

      - *(dict) --*

        Directory structure that includes the directory name and directory ARN.

        - **Name** *(string) --*

          The name of the directory.

        - **DirectoryArn** *(string) --*

          The Amazon Resource Name (ARN) that is associated with the directory. For more
          information, see  arns .

        - **State** *(string) --*

          The state of the directory. Can be either ``Enabled`` , ``Disabled`` , or ``Deleted`` .

        - **CreationDateTime** *(datetime) --*

          The date and time when the directory was created.
    """


_ListFacetAttributesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFacetAttributesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFacetAttributesPaginatePaginationConfigTypeDef(
    _ListFacetAttributesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListFacetAttributesPaginate` `PaginationConfig`

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


_ListFacetAttributesPaginateResponseAttributesAttributeDefinitionDefaultValueTypeDef = TypedDict(
    "_ListFacetAttributesPaginateResponseAttributesAttributeDefinitionDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListFacetAttributesPaginateResponseAttributesAttributeDefinitionDefaultValueTypeDef(
    _ListFacetAttributesPaginateResponseAttributesAttributeDefinitionDefaultValueTypeDef
):
    """
    Type definition for `ListFacetAttributesPaginateResponseAttributesAttributeDefinition` `DefaultValue`

    The default value of the attribute (if configured).

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ListFacetAttributesPaginateResponseAttributesAttributeDefinitionRulesTypeDef = TypedDict(
    "_ListFacetAttributesPaginateResponseAttributesAttributeDefinitionRulesTypeDef",
    {"Type": str, "Parameters": Dict[str, str]},
    total=False,
)


class ListFacetAttributesPaginateResponseAttributesAttributeDefinitionRulesTypeDef(
    _ListFacetAttributesPaginateResponseAttributesAttributeDefinitionRulesTypeDef
):
    """
    Type definition for `ListFacetAttributesPaginateResponseAttributesAttributeDefinition` `Rules`

    Contains an Amazon Resource Name (ARN) and parameters that are associated with the
    rule.

    - **Type** *(string) --*

      The type of attribute validation rule.

    - **Parameters** *(dict) --*

      The minimum and maximum parameters that are associated with the rule.

      - *(string) --*

        - *(string) --*
    """


_ListFacetAttributesPaginateResponseAttributesAttributeDefinitionTypeDef = TypedDict(
    "_ListFacetAttributesPaginateResponseAttributesAttributeDefinitionTypeDef",
    {
        "Type": str,
        "DefaultValue": ListFacetAttributesPaginateResponseAttributesAttributeDefinitionDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[
            str,
            ListFacetAttributesPaginateResponseAttributesAttributeDefinitionRulesTypeDef,
        ],
    },
    total=False,
)


class ListFacetAttributesPaginateResponseAttributesAttributeDefinitionTypeDef(
    _ListFacetAttributesPaginateResponseAttributesAttributeDefinitionTypeDef
):
    """
    Type definition for `ListFacetAttributesPaginateResponseAttributes` `AttributeDefinition`

    A facet attribute consists of either a definition or a reference. This structure contains
    the attribute definition. See `Attribute References
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
    for more information.

    - **Type** *(string) --*

      The type of the attribute.

    - **DefaultValue** *(dict) --*

      The default value of the attribute (if configured).

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.

    - **IsImmutable** *(boolean) --*

      Whether the attribute is mutable or not.

    - **Rules** *(dict) --*

      Validation rules attached to the attribute definition.

      - *(string) --*

        - *(dict) --*

          Contains an Amazon Resource Name (ARN) and parameters that are associated with the
          rule.

          - **Type** *(string) --*

            The type of attribute validation rule.

          - **Parameters** *(dict) --*

            The minimum and maximum parameters that are associated with the rule.

            - *(string) --*

              - *(string) --*
    """


_ListFacetAttributesPaginateResponseAttributesAttributeReferenceTypeDef = TypedDict(
    "_ListFacetAttributesPaginateResponseAttributesAttributeReferenceTypeDef",
    {"TargetFacetName": str, "TargetAttributeName": str},
    total=False,
)


class ListFacetAttributesPaginateResponseAttributesAttributeReferenceTypeDef(
    _ListFacetAttributesPaginateResponseAttributesAttributeReferenceTypeDef
):
    """
    Type definition for `ListFacetAttributesPaginateResponseAttributes` `AttributeReference`

    An attribute reference that is associated with the attribute. See `Attribute References
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
    for more information.

    - **TargetFacetName** *(string) --*

      The target facet name that is associated with the facet reference. See `Attribute
      References
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
      for more information.

    - **TargetAttributeName** *(string) --*

      The target attribute name that is associated with the facet reference. See `Attribute
      References
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
      for more information.
    """


_ListFacetAttributesPaginateResponseAttributesTypeDef = TypedDict(
    "_ListFacetAttributesPaginateResponseAttributesTypeDef",
    {
        "Name": str,
        "AttributeDefinition": ListFacetAttributesPaginateResponseAttributesAttributeDefinitionTypeDef,
        "AttributeReference": ListFacetAttributesPaginateResponseAttributesAttributeReferenceTypeDef,
        "RequiredBehavior": str,
    },
    total=False,
)


class ListFacetAttributesPaginateResponseAttributesTypeDef(
    _ListFacetAttributesPaginateResponseAttributesTypeDef
):
    """
    Type definition for `ListFacetAttributesPaginateResponse` `Attributes`

    An attribute that is associated with the  Facet .

    - **Name** *(string) --*

      The name of the facet attribute.

    - **AttributeDefinition** *(dict) --*

      A facet attribute consists of either a definition or a reference. This structure contains
      the attribute definition. See `Attribute References
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
      for more information.

      - **Type** *(string) --*

        The type of the attribute.

      - **DefaultValue** *(dict) --*

        The default value of the attribute (if configured).

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.

      - **IsImmutable** *(boolean) --*

        Whether the attribute is mutable or not.

      - **Rules** *(dict) --*

        Validation rules attached to the attribute definition.

        - *(string) --*

          - *(dict) --*

            Contains an Amazon Resource Name (ARN) and parameters that are associated with the
            rule.

            - **Type** *(string) --*

              The type of attribute validation rule.

            - **Parameters** *(dict) --*

              The minimum and maximum parameters that are associated with the rule.

              - *(string) --*

                - *(string) --*

    - **AttributeReference** *(dict) --*

      An attribute reference that is associated with the attribute. See `Attribute References
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
      for more information.

      - **TargetFacetName** *(string) --*

        The target facet name that is associated with the facet reference. See `Attribute
        References
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
        for more information.

      - **TargetAttributeName** *(string) --*

        The target attribute name that is associated with the facet reference. See `Attribute
        References
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
        for more information.

    - **RequiredBehavior** *(string) --*

      The required behavior of the ``FacetAttribute`` .
    """


_ListFacetAttributesPaginateResponseTypeDef = TypedDict(
    "_ListFacetAttributesPaginateResponseTypeDef",
    {"Attributes": List[ListFacetAttributesPaginateResponseAttributesTypeDef]},
    total=False,
)


class ListFacetAttributesPaginateResponseTypeDef(
    _ListFacetAttributesPaginateResponseTypeDef
):
    """
    Type definition for `ListFacetAttributesPaginate` `Response`

    - **Attributes** *(list) --*

      The attributes attached to the facet.

      - *(dict) --*

        An attribute that is associated with the  Facet .

        - **Name** *(string) --*

          The name of the facet attribute.

        - **AttributeDefinition** *(dict) --*

          A facet attribute consists of either a definition or a reference. This structure contains
          the attribute definition. See `Attribute References
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
          for more information.

          - **Type** *(string) --*

            The type of the attribute.

          - **DefaultValue** *(dict) --*

            The default value of the attribute (if configured).

            - **StringValue** *(string) --*

              A string data value.

            - **BinaryValue** *(bytes) --*

              A binary data value.

            - **BooleanValue** *(boolean) --*

              A Boolean data value.

            - **NumberValue** *(string) --*

              A number data value.

            - **DatetimeValue** *(datetime) --*

              A date and time value.

          - **IsImmutable** *(boolean) --*

            Whether the attribute is mutable or not.

          - **Rules** *(dict) --*

            Validation rules attached to the attribute definition.

            - *(string) --*

              - *(dict) --*

                Contains an Amazon Resource Name (ARN) and parameters that are associated with the
                rule.

                - **Type** *(string) --*

                  The type of attribute validation rule.

                - **Parameters** *(dict) --*

                  The minimum and maximum parameters that are associated with the rule.

                  - *(string) --*

                    - *(string) --*

        - **AttributeReference** *(dict) --*

          An attribute reference that is associated with the attribute. See `Attribute References
          <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
          for more information.

          - **TargetFacetName** *(string) --*

            The target facet name that is associated with the facet reference. See `Attribute
            References
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
            for more information.

          - **TargetAttributeName** *(string) --*

            The target attribute name that is associated with the facet reference. See `Attribute
            References
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_attributereferences.html>`__
            for more information.

        - **RequiredBehavior** *(string) --*

          The required behavior of the ``FacetAttribute`` .
    """


_ListFacetNamesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFacetNamesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFacetNamesPaginatePaginationConfigTypeDef(
    _ListFacetNamesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListFacetNamesPaginate` `PaginationConfig`

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


_ListFacetNamesPaginateResponseTypeDef = TypedDict(
    "_ListFacetNamesPaginateResponseTypeDef", {"FacetNames": List[str]}, total=False
)


class ListFacetNamesPaginateResponseTypeDef(_ListFacetNamesPaginateResponseTypeDef):
    """
    Type definition for `ListFacetNamesPaginate` `Response`

    - **FacetNames** *(list) --*

      The names of facets that exist within the schema.

      - *(string) --*
    """


_ListIncomingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListIncomingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef(
    _ListIncomingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef
):
    """
    Type definition for `ListIncomingTypedLinksPaginateFilterAttributeRangesRange` `EndValue`

    The attribute value to terminate the range at.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ListIncomingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListIncomingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef(
    _ListIncomingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef
):
    """
    Type definition for `ListIncomingTypedLinksPaginateFilterAttributeRangesRange` `StartValue`

    The value to start the range at.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_RequiredListIncomingTypedLinksPaginateFilterAttributeRangesRangeTypeDef = TypedDict(
    "_RequiredListIncomingTypedLinksPaginateFilterAttributeRangesRangeTypeDef",
    {"StartMode": str, "EndMode": str},
)
_OptionalListIncomingTypedLinksPaginateFilterAttributeRangesRangeTypeDef = TypedDict(
    "_OptionalListIncomingTypedLinksPaginateFilterAttributeRangesRangeTypeDef",
    {
        "StartValue": ListIncomingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef,
        "EndValue": ListIncomingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef,
    },
    total=False,
)


class ListIncomingTypedLinksPaginateFilterAttributeRangesRangeTypeDef(
    _RequiredListIncomingTypedLinksPaginateFilterAttributeRangesRangeTypeDef,
    _OptionalListIncomingTypedLinksPaginateFilterAttributeRangesRangeTypeDef,
):
    """
    Type definition for `ListIncomingTypedLinksPaginateFilterAttributeRanges` `Range`

    The range of attribute values that are being selected.

    - **StartMode** *(string) --* **[REQUIRED]**

      The inclusive or exclusive range start.

    - **StartValue** *(dict) --*

      The value to start the range at.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.

    - **EndMode** *(string) --* **[REQUIRED]**

      The inclusive or exclusive range end.

    - **EndValue** *(dict) --*

      The attribute value to terminate the range at.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_RequiredListIncomingTypedLinksPaginateFilterAttributeRangesTypeDef = TypedDict(
    "_RequiredListIncomingTypedLinksPaginateFilterAttributeRangesTypeDef",
    {"Range": ListIncomingTypedLinksPaginateFilterAttributeRangesRangeTypeDef},
)
_OptionalListIncomingTypedLinksPaginateFilterAttributeRangesTypeDef = TypedDict(
    "_OptionalListIncomingTypedLinksPaginateFilterAttributeRangesTypeDef",
    {"AttributeName": str},
    total=False,
)


class ListIncomingTypedLinksPaginateFilterAttributeRangesTypeDef(
    _RequiredListIncomingTypedLinksPaginateFilterAttributeRangesTypeDef,
    _OptionalListIncomingTypedLinksPaginateFilterAttributeRangesTypeDef,
):
    """
    Type definition for `ListIncomingTypedLinksPaginate` `FilterAttributeRanges`

    Identifies the range of attributes that are used by a specified filter.

    - **AttributeName** *(string) --*

      The unique name of the typed link attribute.

    - **Range** *(dict) --* **[REQUIRED]**

      The range of attribute values that are being selected.

      - **StartMode** *(string) --* **[REQUIRED]**

        The inclusive or exclusive range start.

      - **StartValue** *(dict) --*

        The value to start the range at.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.

      - **EndMode** *(string) --* **[REQUIRED]**

        The inclusive or exclusive range end.

      - **EndValue** *(dict) --*

        The attribute value to terminate the range at.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.
    """


_ListIncomingTypedLinksPaginateFilterTypedLinkTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateFilterTypedLinkTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
)


class ListIncomingTypedLinksPaginateFilterTypedLinkTypeDef(
    _ListIncomingTypedLinksPaginateFilterTypedLinkTypeDef
):
    """
    Type definition for `ListIncomingTypedLinksPaginate` `FilterTypedLink`

    Filters are interpreted in the order of the attributes on the typed link facet, not the order in
    which they are supplied to any API calls.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
      arns .

    - **TypedLinkName** *(string) --* **[REQUIRED]**

      The unique name of the typed link facet.
    """


_ListIncomingTypedLinksPaginateObjectReferenceTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ListIncomingTypedLinksPaginateObjectReferenceTypeDef(
    _ListIncomingTypedLinksPaginateObjectReferenceTypeDef
):
    """
    Type definition for `ListIncomingTypedLinksPaginate` `ObjectReference`

    Reference that identifies the object whose attributes will be listed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListIncomingTypedLinksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListIncomingTypedLinksPaginatePaginationConfigTypeDef(
    _ListIncomingTypedLinksPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListIncomingTypedLinksPaginate` `PaginationConfig`

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


_ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef(
    _ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef
):
    """
    Type definition for `ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValues` `Value`

    The value for the typed link.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesTypeDef(
    _ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesTypeDef
):
    """
    Type definition for `ListIncomingTypedLinksPaginateResponseLinkSpecifiers` `IdentityAttributeValues`

    Identifies the attribute name and value for a typed link.

    - **AttributeName** *(string) --*

      The attribute name of the typed link.

    - **Value** *(dict) --*

      The value for the typed link.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ListIncomingTypedLinksPaginateResponseLinkSpecifiersSourceObjectReferenceTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateResponseLinkSpecifiersSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ListIncomingTypedLinksPaginateResponseLinkSpecifiersSourceObjectReferenceTypeDef(
    _ListIncomingTypedLinksPaginateResponseLinkSpecifiersSourceObjectReferenceTypeDef
):
    """
    Type definition for `ListIncomingTypedLinksPaginateResponseLinkSpecifiers` `SourceObjectReference`

    Identifies the source object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading
      to it from the directory root. Use the link names from each parent/child link to
      construct the path. Path selectors start with a slash (/) and link names are separated
      by slashes. For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
      Cloud Directory. When creating objects, the system will provide you with the identifier
      of the created object. An object’s identifier is immutable and no two objects will ever
      share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListIncomingTypedLinksPaginateResponseLinkSpecifiersTargetObjectReferenceTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateResponseLinkSpecifiersTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ListIncomingTypedLinksPaginateResponseLinkSpecifiersTargetObjectReferenceTypeDef(
    _ListIncomingTypedLinksPaginateResponseLinkSpecifiersTargetObjectReferenceTypeDef
):
    """
    Type definition for `ListIncomingTypedLinksPaginateResponseLinkSpecifiers` `TargetObjectReference`

    Identifies the target object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading
      to it from the directory root. Use the link names from each parent/child link to
      construct the path. Path selectors start with a slash (/) and link names are separated
      by slashes. For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
      Cloud Directory. When creating objects, the system will provide you with the identifier
      of the created object. An object’s identifier is immutable and no two objects will ever
      share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypedLinkFacetTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypedLinkFacetTypeDef(
    _ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypedLinkFacetTypeDef
):
    """
    Type definition for `ListIncomingTypedLinksPaginateResponseLinkSpecifiers` `TypedLinkFacet`

    Identifies the typed link facet that is associated with the typed link.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) that is associated with the schema. For more
      information, see  arns .

    - **TypedLinkName** *(string) --*

      The unique name of the typed link facet.
    """


_ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypeDef",
    {
        "TypedLinkFacet": ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypedLinkFacetTypeDef,
        "SourceObjectReference": ListIncomingTypedLinksPaginateResponseLinkSpecifiersSourceObjectReferenceTypeDef,
        "TargetObjectReference": ListIncomingTypedLinksPaginateResponseLinkSpecifiersTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ListIncomingTypedLinksPaginateResponseLinkSpecifiersIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypeDef(
    _ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypeDef
):
    """
    Type definition for `ListIncomingTypedLinksPaginateResponse` `LinkSpecifiers`

    Contains all the information that is used to uniquely identify a typed link. The parameters
    discussed in this topic are used to uniquely specify the typed link being operated on. The
    AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts
    one as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API
    operations provide typed link specifiers as output. You can also construct a typed link
    specifier from scratch.

    - **TypedLinkFacet** *(dict) --*

      Identifies the typed link facet that is associated with the typed link.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) that is associated with the schema. For more
        information, see  arns .

      - **TypedLinkName** *(string) --*

        The unique name of the typed link facet.

    - **SourceObjectReference** *(dict) --*

      Identifies the source object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading
        to it from the directory root. Use the link names from each parent/child link to
        construct the path. Path selectors start with a slash (/) and link names are separated
        by slashes. For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
        Cloud Directory. When creating objects, the system will provide you with the identifier
        of the created object. An object’s identifier is immutable and no two objects will ever
        share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **TargetObjectReference** *(dict) --*

      Identifies the target object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading
        to it from the directory root. Use the link names from each parent/child link to
        construct the path. Path selectors start with a slash (/) and link names are separated
        by slashes. For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
        Cloud Directory. When creating objects, the system will provide you with the identifier
        of the created object. An object’s identifier is immutable and no two objects will ever
        share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **IdentityAttributeValues** *(list) --*

      Identifies the attribute value to update.

      - *(dict) --*

        Identifies the attribute name and value for a typed link.

        - **AttributeName** *(string) --*

          The attribute name of the typed link.

        - **Value** *(dict) --*

          The value for the typed link.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ListIncomingTypedLinksPaginateResponseTypeDef = TypedDict(
    "_ListIncomingTypedLinksPaginateResponseTypeDef",
    {
        "LinkSpecifiers": List[
            ListIncomingTypedLinksPaginateResponseLinkSpecifiersTypeDef
        ]
    },
    total=False,
)


class ListIncomingTypedLinksPaginateResponseTypeDef(
    _ListIncomingTypedLinksPaginateResponseTypeDef
):
    """
    Type definition for `ListIncomingTypedLinksPaginate` `Response`

    - **LinkSpecifiers** *(list) --*

      Returns one or more typed link specifiers as output.

      - *(dict) --*

        Contains all the information that is used to uniquely identify a typed link. The parameters
        discussed in this topic are used to uniquely specify the typed link being operated on. The
        AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts
        one as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API
        operations provide typed link specifiers as output. You can also construct a typed link
        specifier from scratch.

        - **TypedLinkFacet** *(dict) --*

          Identifies the typed link facet that is associated with the typed link.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) that is associated with the schema. For more
            information, see  arns .

          - **TypedLinkName** *(string) --*

            The unique name of the typed link facet.

        - **SourceObjectReference** *(dict) --*

          Identifies the source object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links leading
            to it from the directory root. Use the link names from each parent/child link to
            construct the path. Path selectors start with a slash (/) and link names are separated
            by slashes. For more information about paths, see `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
            Cloud Directory. When creating objects, the system will provide you with the identifier
            of the created object. An object’s identifier is immutable and no two objects will ever
            share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **TargetObjectReference** *(dict) --*

          Identifies the target object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links leading
            to it from the directory root. Use the link names from each parent/child link to
            construct the path. Path selectors start with a slash (/) and link names are separated
            by slashes. For more information about paths, see `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
            Cloud Directory. When creating objects, the system will provide you with the identifier
            of the created object. An object’s identifier is immutable and no two objects will ever
            share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **IdentityAttributeValues** *(list) --*

          Identifies the attribute value to update.

          - *(dict) --*

            Identifies the attribute name and value for a typed link.

            - **AttributeName** *(string) --*

              The attribute name of the typed link.

            - **Value** *(dict) --*

              The value for the typed link.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.
    """


_ListIndexPaginateIndexReferenceTypeDef = TypedDict(
    "_ListIndexPaginateIndexReferenceTypeDef", {"Selector": str}, total=False
)


class ListIndexPaginateIndexReferenceTypeDef(_ListIndexPaginateIndexReferenceTypeDef):
    """
    Type definition for `ListIndexPaginate` `IndexReference`

    The reference to the index to list.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListIndexPaginatePaginationConfigTypeDef = TypedDict(
    "_ListIndexPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListIndexPaginatePaginationConfigTypeDef(
    _ListIndexPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListIndexPaginate` `PaginationConfig`

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


_ListIndexPaginateRangesOnIndexedValuesAttributeKeyTypeDef = TypedDict(
    "_ListIndexPaginateRangesOnIndexedValuesAttributeKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
)


class ListIndexPaginateRangesOnIndexedValuesAttributeKeyTypeDef(
    _ListIndexPaginateRangesOnIndexedValuesAttributeKeyTypeDef
):
    """
    Type definition for `ListIndexPaginateRangesOnIndexedValues` `AttributeKey`

    The key of the attribute that the attribute range covers.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --* **[REQUIRED]**

      The name of the facet that the attribute exists within.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the attribute.
    """


_ListIndexPaginateRangesOnIndexedValuesRangeEndValueTypeDef = TypedDict(
    "_ListIndexPaginateRangesOnIndexedValuesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListIndexPaginateRangesOnIndexedValuesRangeEndValueTypeDef(
    _ListIndexPaginateRangesOnIndexedValuesRangeEndValueTypeDef
):
    """
    Type definition for `ListIndexPaginateRangesOnIndexedValuesRange` `EndValue`

    The attribute value to terminate the range at.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ListIndexPaginateRangesOnIndexedValuesRangeStartValueTypeDef = TypedDict(
    "_ListIndexPaginateRangesOnIndexedValuesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListIndexPaginateRangesOnIndexedValuesRangeStartValueTypeDef(
    _ListIndexPaginateRangesOnIndexedValuesRangeStartValueTypeDef
):
    """
    Type definition for `ListIndexPaginateRangesOnIndexedValuesRange` `StartValue`

    The value to start the range at.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_RequiredListIndexPaginateRangesOnIndexedValuesRangeTypeDef = TypedDict(
    "_RequiredListIndexPaginateRangesOnIndexedValuesRangeTypeDef",
    {"StartMode": str, "EndMode": str},
)
_OptionalListIndexPaginateRangesOnIndexedValuesRangeTypeDef = TypedDict(
    "_OptionalListIndexPaginateRangesOnIndexedValuesRangeTypeDef",
    {
        "StartValue": ListIndexPaginateRangesOnIndexedValuesRangeStartValueTypeDef,
        "EndValue": ListIndexPaginateRangesOnIndexedValuesRangeEndValueTypeDef,
    },
    total=False,
)


class ListIndexPaginateRangesOnIndexedValuesRangeTypeDef(
    _RequiredListIndexPaginateRangesOnIndexedValuesRangeTypeDef,
    _OptionalListIndexPaginateRangesOnIndexedValuesRangeTypeDef,
):
    """
    Type definition for `ListIndexPaginateRangesOnIndexedValues` `Range`

    The range of attribute values being selected.

    - **StartMode** *(string) --* **[REQUIRED]**

      The inclusive or exclusive range start.

    - **StartValue** *(dict) --*

      The value to start the range at.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.

    - **EndMode** *(string) --* **[REQUIRED]**

      The inclusive or exclusive range end.

    - **EndValue** *(dict) --*

      The attribute value to terminate the range at.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ListIndexPaginateRangesOnIndexedValuesTypeDef = TypedDict(
    "_ListIndexPaginateRangesOnIndexedValuesTypeDef",
    {
        "AttributeKey": ListIndexPaginateRangesOnIndexedValuesAttributeKeyTypeDef,
        "Range": ListIndexPaginateRangesOnIndexedValuesRangeTypeDef,
    },
    total=False,
)


class ListIndexPaginateRangesOnIndexedValuesTypeDef(
    _ListIndexPaginateRangesOnIndexedValuesTypeDef
):
    """
    Type definition for `ListIndexPaginate` `RangesOnIndexedValues`

    A range of attributes.

    - **AttributeKey** *(dict) --*

      The key of the attribute that the attribute range covers.

      - **SchemaArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --* **[REQUIRED]**

        The name of the facet that the attribute exists within.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the attribute.

    - **Range** *(dict) --*

      The range of attribute values being selected.

      - **StartMode** *(string) --* **[REQUIRED]**

        The inclusive or exclusive range start.

      - **StartValue** *(dict) --*

        The value to start the range at.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.

      - **EndMode** *(string) --* **[REQUIRED]**

        The inclusive or exclusive range end.

      - **EndValue** *(dict) --*

        The attribute value to terminate the range at.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.
    """


_ListIndexPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef = TypedDict(
    "_ListIndexPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ListIndexPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef(
    _ListIndexPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef
):
    """
    Type definition for `ListIndexPaginateResponseIndexAttachmentsIndexedAttributes` `Key`

    The key of the attribute.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --*

      The name of the facet that the attribute exists within.

    - **Name** *(string) --*

      The name of the attribute.
    """


_ListIndexPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef = TypedDict(
    "_ListIndexPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListIndexPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef(
    _ListIndexPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef
):
    """
    Type definition for `ListIndexPaginateResponseIndexAttachmentsIndexedAttributes` `Value`

    The value of the attribute.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ListIndexPaginateResponseIndexAttachmentsIndexedAttributesTypeDef = TypedDict(
    "_ListIndexPaginateResponseIndexAttachmentsIndexedAttributesTypeDef",
    {
        "Key": ListIndexPaginateResponseIndexAttachmentsIndexedAttributesKeyTypeDef,
        "Value": ListIndexPaginateResponseIndexAttachmentsIndexedAttributesValueTypeDef,
    },
    total=False,
)


class ListIndexPaginateResponseIndexAttachmentsIndexedAttributesTypeDef(
    _ListIndexPaginateResponseIndexAttachmentsIndexedAttributesTypeDef
):
    """
    Type definition for `ListIndexPaginateResponseIndexAttachments` `IndexedAttributes`

    The combination of an attribute key and an attribute value.

    - **Key** *(dict) --*

      The key of the attribute.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --*

        The name of the facet that the attribute exists within.

      - **Name** *(string) --*

        The name of the attribute.

    - **Value** *(dict) --*

      The value of the attribute.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ListIndexPaginateResponseIndexAttachmentsTypeDef = TypedDict(
    "_ListIndexPaginateResponseIndexAttachmentsTypeDef",
    {
        "IndexedAttributes": List[
            ListIndexPaginateResponseIndexAttachmentsIndexedAttributesTypeDef
        ],
        "ObjectIdentifier": str,
    },
    total=False,
)


class ListIndexPaginateResponseIndexAttachmentsTypeDef(
    _ListIndexPaginateResponseIndexAttachmentsTypeDef
):
    """
    Type definition for `ListIndexPaginateResponse` `IndexAttachments`

    Represents an index and an attached object.

    - **IndexedAttributes** *(list) --*

      The indexed attribute values.

      - *(dict) --*

        The combination of an attribute key and an attribute value.

        - **Key** *(dict) --*

          The key of the attribute.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

          - **FacetName** *(string) --*

            The name of the facet that the attribute exists within.

          - **Name** *(string) --*

            The name of the attribute.

        - **Value** *(dict) --*

          The value of the attribute.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.

    - **ObjectIdentifier** *(string) --*

      In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to the index.
      In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the index attached to
      the object. This field will always contain the ``ObjectIdentifier`` of the object on the
      opposite side of the attachment specified in the query.
    """


_ListIndexPaginateResponseTypeDef = TypedDict(
    "_ListIndexPaginateResponseTypeDef",
    {"IndexAttachments": List[ListIndexPaginateResponseIndexAttachmentsTypeDef]},
    total=False,
)


class ListIndexPaginateResponseTypeDef(_ListIndexPaginateResponseTypeDef):
    """
    Type definition for `ListIndexPaginate` `Response`

    - **IndexAttachments** *(list) --*

      The objects and indexed values attached to the index.

      - *(dict) --*

        Represents an index and an attached object.

        - **IndexedAttributes** *(list) --*

          The indexed attribute values.

          - *(dict) --*

            The combination of an attribute key and an attribute value.

            - **Key** *(dict) --*

              The key of the attribute.

              - **SchemaArn** *(string) --*

                The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

              - **FacetName** *(string) --*

                The name of the facet that the attribute exists within.

              - **Name** *(string) --*

                The name of the attribute.

            - **Value** *(dict) --*

              The value of the attribute.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.

        - **ObjectIdentifier** *(string) --*

          In response to  ListIndex , the ``ObjectIdentifier`` of the object attached to the index.
          In response to  ListAttachedIndices , the ``ObjectIdentifier`` of the index attached to
          the object. This field will always contain the ``ObjectIdentifier`` of the object on the
          opposite side of the attachment specified in the query.
    """


_ListManagedSchemaArnsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListManagedSchemaArnsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListManagedSchemaArnsPaginatePaginationConfigTypeDef(
    _ListManagedSchemaArnsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListManagedSchemaArnsPaginate` `PaginationConfig`

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


_ListManagedSchemaArnsPaginateResponseTypeDef = TypedDict(
    "_ListManagedSchemaArnsPaginateResponseTypeDef",
    {"SchemaArns": List[str]},
    total=False,
)


class ListManagedSchemaArnsPaginateResponseTypeDef(
    _ListManagedSchemaArnsPaginateResponseTypeDef
):
    """
    Type definition for `ListManagedSchemaArnsPaginate` `Response`

    - **SchemaArns** *(list) --*

      The ARNs for all AWS managed schemas.

      - *(string) --*
    """


_ListObjectAttributesPaginateFacetFilterTypeDef = TypedDict(
    "_ListObjectAttributesPaginateFacetFilterTypeDef",
    {"SchemaArn": str, "FacetName": str},
    total=False,
)


class ListObjectAttributesPaginateFacetFilterTypeDef(
    _ListObjectAttributesPaginateFacetFilterTypeDef
):
    """
    Type definition for `ListObjectAttributesPaginate` `FacetFilter`

    Used to filter the list of object attributes that are associated with a certain facet.

    - **SchemaArn** *(string) --*

      The ARN of the schema that contains the facet with no minor component. See  arns and `In-Place
      Schema Upgrade
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_inplaceschemaupgrade.html>`__
      for a description of when to provide minor versions.

    - **FacetName** *(string) --*

      The name of the facet.
    """


_ListObjectAttributesPaginateObjectReferenceTypeDef = TypedDict(
    "_ListObjectAttributesPaginateObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ListObjectAttributesPaginateObjectReferenceTypeDef(
    _ListObjectAttributesPaginateObjectReferenceTypeDef
):
    """
    Type definition for `ListObjectAttributesPaginate` `ObjectReference`

    The reference that identifies the object whose attributes will be listed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListObjectAttributesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListObjectAttributesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListObjectAttributesPaginatePaginationConfigTypeDef(
    _ListObjectAttributesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListObjectAttributesPaginate` `PaginationConfig`

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


_ListObjectAttributesPaginateResponseAttributesKeyTypeDef = TypedDict(
    "_ListObjectAttributesPaginateResponseAttributesKeyTypeDef",
    {"SchemaArn": str, "FacetName": str, "Name": str},
    total=False,
)


class ListObjectAttributesPaginateResponseAttributesKeyTypeDef(
    _ListObjectAttributesPaginateResponseAttributesKeyTypeDef
):
    """
    Type definition for `ListObjectAttributesPaginateResponseAttributes` `Key`

    The key of the attribute.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

    - **FacetName** *(string) --*

      The name of the facet that the attribute exists within.

    - **Name** *(string) --*

      The name of the attribute.
    """


_ListObjectAttributesPaginateResponseAttributesValueTypeDef = TypedDict(
    "_ListObjectAttributesPaginateResponseAttributesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListObjectAttributesPaginateResponseAttributesValueTypeDef(
    _ListObjectAttributesPaginateResponseAttributesValueTypeDef
):
    """
    Type definition for `ListObjectAttributesPaginateResponseAttributes` `Value`

    The value of the attribute.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ListObjectAttributesPaginateResponseAttributesTypeDef = TypedDict(
    "_ListObjectAttributesPaginateResponseAttributesTypeDef",
    {
        "Key": ListObjectAttributesPaginateResponseAttributesKeyTypeDef,
        "Value": ListObjectAttributesPaginateResponseAttributesValueTypeDef,
    },
    total=False,
)


class ListObjectAttributesPaginateResponseAttributesTypeDef(
    _ListObjectAttributesPaginateResponseAttributesTypeDef
):
    """
    Type definition for `ListObjectAttributesPaginateResponse` `Attributes`

    The combination of an attribute key and an attribute value.

    - **Key** *(dict) --*

      The key of the attribute.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

      - **FacetName** *(string) --*

        The name of the facet that the attribute exists within.

      - **Name** *(string) --*

        The name of the attribute.

    - **Value** *(dict) --*

      The value of the attribute.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ListObjectAttributesPaginateResponseTypeDef = TypedDict(
    "_ListObjectAttributesPaginateResponseTypeDef",
    {"Attributes": List[ListObjectAttributesPaginateResponseAttributesTypeDef]},
    total=False,
)


class ListObjectAttributesPaginateResponseTypeDef(
    _ListObjectAttributesPaginateResponseTypeDef
):
    """
    Type definition for `ListObjectAttributesPaginate` `Response`

    - **Attributes** *(list) --*

      Attributes map that is associated with the object. ``AttributeArn`` is the key, and attribute
      value is the value.

      - *(dict) --*

        The combination of an attribute key and an attribute value.

        - **Key** *(dict) --*

          The key of the attribute.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

          - **FacetName** *(string) --*

            The name of the facet that the attribute exists within.

          - **Name** *(string) --*

            The name of the attribute.

        - **Value** *(dict) --*

          The value of the attribute.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ListObjectParentPathsPaginateObjectReferenceTypeDef = TypedDict(
    "_ListObjectParentPathsPaginateObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ListObjectParentPathsPaginateObjectReferenceTypeDef(
    _ListObjectParentPathsPaginateObjectReferenceTypeDef
):
    """
    Type definition for `ListObjectParentPathsPaginate` `ObjectReference`

    The reference that identifies the object whose parent paths are listed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListObjectParentPathsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListObjectParentPathsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListObjectParentPathsPaginatePaginationConfigTypeDef(
    _ListObjectParentPathsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListObjectParentPathsPaginate` `PaginationConfig`

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


_ListObjectParentPathsPaginateResponsePathToObjectIdentifiersListTypeDef = TypedDict(
    "_ListObjectParentPathsPaginateResponsePathToObjectIdentifiersListTypeDef",
    {"Path": str, "ObjectIdentifiers": List[str]},
    total=False,
)


class ListObjectParentPathsPaginateResponsePathToObjectIdentifiersListTypeDef(
    _ListObjectParentPathsPaginateResponsePathToObjectIdentifiersListTypeDef
):
    """
    Type definition for `ListObjectParentPathsPaginateResponse` `PathToObjectIdentifiersList`

    Returns the path to the ``ObjectIdentifiers`` that is associated with the directory.

    - **Path** *(string) --*

      The path that is used to identify the object starting from directory root.

    - **ObjectIdentifiers** *(list) --*

      Lists ``ObjectIdentifiers`` starting from directory root to the object in the request.

      - *(string) --*
    """


_ListObjectParentPathsPaginateResponseTypeDef = TypedDict(
    "_ListObjectParentPathsPaginateResponseTypeDef",
    {
        "PathToObjectIdentifiersList": List[
            ListObjectParentPathsPaginateResponsePathToObjectIdentifiersListTypeDef
        ]
    },
    total=False,
)


class ListObjectParentPathsPaginateResponseTypeDef(
    _ListObjectParentPathsPaginateResponseTypeDef
):
    """
    Type definition for `ListObjectParentPathsPaginate` `Response`

    - **PathToObjectIdentifiersList** *(list) --*

      Returns the path to the ``ObjectIdentifiers`` that are associated with the directory.

      - *(dict) --*

        Returns the path to the ``ObjectIdentifiers`` that is associated with the directory.

        - **Path** *(string) --*

          The path that is used to identify the object starting from directory root.

        - **ObjectIdentifiers** *(list) --*

          Lists ``ObjectIdentifiers`` starting from directory root to the object in the request.

          - *(string) --*
    """


_ListObjectPoliciesPaginateObjectReferenceTypeDef = TypedDict(
    "_ListObjectPoliciesPaginateObjectReferenceTypeDef", {"Selector": str}, total=False
)


class ListObjectPoliciesPaginateObjectReferenceTypeDef(
    _ListObjectPoliciesPaginateObjectReferenceTypeDef
):
    """
    Type definition for `ListObjectPoliciesPaginate` `ObjectReference`

    Reference that identifies the object for which policies will be listed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListObjectPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListObjectPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListObjectPoliciesPaginatePaginationConfigTypeDef(
    _ListObjectPoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListObjectPoliciesPaginate` `PaginationConfig`

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


_ListObjectPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListObjectPoliciesPaginateResponseTypeDef",
    {"AttachedPolicyIds": List[str]},
    total=False,
)


class ListObjectPoliciesPaginateResponseTypeDef(
    _ListObjectPoliciesPaginateResponseTypeDef
):
    """
    Type definition for `ListObjectPoliciesPaginate` `Response`

    - **AttachedPolicyIds** *(list) --*

      A list of policy ``ObjectIdentifiers`` , that are attached to the object.

      - *(string) --*
    """


_ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef(
    _ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef
):
    """
    Type definition for `ListOutgoingTypedLinksPaginateFilterAttributeRangesRange` `EndValue`

    The attribute value to terminate the range at.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef(
    _ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef
):
    """
    Type definition for `ListOutgoingTypedLinksPaginateFilterAttributeRangesRange` `StartValue`

    The value to start the range at.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_RequiredListOutgoingTypedLinksPaginateFilterAttributeRangesRangeTypeDef = TypedDict(
    "_RequiredListOutgoingTypedLinksPaginateFilterAttributeRangesRangeTypeDef",
    {"StartMode": str, "EndMode": str},
)
_OptionalListOutgoingTypedLinksPaginateFilterAttributeRangesRangeTypeDef = TypedDict(
    "_OptionalListOutgoingTypedLinksPaginateFilterAttributeRangesRangeTypeDef",
    {
        "StartValue": ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeStartValueTypeDef,
        "EndValue": ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeEndValueTypeDef,
    },
    total=False,
)


class ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeTypeDef(
    _RequiredListOutgoingTypedLinksPaginateFilterAttributeRangesRangeTypeDef,
    _OptionalListOutgoingTypedLinksPaginateFilterAttributeRangesRangeTypeDef,
):
    """
    Type definition for `ListOutgoingTypedLinksPaginateFilterAttributeRanges` `Range`

    The range of attribute values that are being selected.

    - **StartMode** *(string) --* **[REQUIRED]**

      The inclusive or exclusive range start.

    - **StartValue** *(dict) --*

      The value to start the range at.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.

    - **EndMode** *(string) --* **[REQUIRED]**

      The inclusive or exclusive range end.

    - **EndValue** *(dict) --*

      The attribute value to terminate the range at.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_RequiredListOutgoingTypedLinksPaginateFilterAttributeRangesTypeDef = TypedDict(
    "_RequiredListOutgoingTypedLinksPaginateFilterAttributeRangesTypeDef",
    {"Range": ListOutgoingTypedLinksPaginateFilterAttributeRangesRangeTypeDef},
)
_OptionalListOutgoingTypedLinksPaginateFilterAttributeRangesTypeDef = TypedDict(
    "_OptionalListOutgoingTypedLinksPaginateFilterAttributeRangesTypeDef",
    {"AttributeName": str},
    total=False,
)


class ListOutgoingTypedLinksPaginateFilterAttributeRangesTypeDef(
    _RequiredListOutgoingTypedLinksPaginateFilterAttributeRangesTypeDef,
    _OptionalListOutgoingTypedLinksPaginateFilterAttributeRangesTypeDef,
):
    """
    Type definition for `ListOutgoingTypedLinksPaginate` `FilterAttributeRanges`

    Identifies the range of attributes that are used by a specified filter.

    - **AttributeName** *(string) --*

      The unique name of the typed link attribute.

    - **Range** *(dict) --* **[REQUIRED]**

      The range of attribute values that are being selected.

      - **StartMode** *(string) --* **[REQUIRED]**

        The inclusive or exclusive range start.

      - **StartValue** *(dict) --*

        The value to start the range at.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.

      - **EndMode** *(string) --* **[REQUIRED]**

        The inclusive or exclusive range end.

      - **EndValue** *(dict) --*

        The attribute value to terminate the range at.

        - **StringValue** *(string) --*

          A string data value.

        - **BinaryValue** *(bytes) --*

          A binary data value.

        - **BooleanValue** *(boolean) --*

          A Boolean data value.

        - **NumberValue** *(string) --*

          A number data value.

        - **DatetimeValue** *(datetime) --*

          A date and time value.
    """


_ListOutgoingTypedLinksPaginateFilterTypedLinkTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateFilterTypedLinkTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
)


class ListOutgoingTypedLinksPaginateFilterTypedLinkTypeDef(
    _ListOutgoingTypedLinksPaginateFilterTypedLinkTypeDef
):
    """
    Type definition for `ListOutgoingTypedLinksPaginate` `FilterTypedLink`

    Filters are interpreted in the order of the attributes defined on the typed link facet, not the
    order they are supplied to any API calls.

    - **SchemaArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that is associated with the schema. For more information, see
      arns .

    - **TypedLinkName** *(string) --* **[REQUIRED]**

      The unique name of the typed link facet.
    """


_ListOutgoingTypedLinksPaginateObjectReferenceTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ListOutgoingTypedLinksPaginateObjectReferenceTypeDef(
    _ListOutgoingTypedLinksPaginateObjectReferenceTypeDef
):
    """
    Type definition for `ListOutgoingTypedLinksPaginate` `ObjectReference`

    A reference that identifies the object whose attributes will be listed.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListOutgoingTypedLinksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListOutgoingTypedLinksPaginatePaginationConfigTypeDef(
    _ListOutgoingTypedLinksPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListOutgoingTypedLinksPaginate` `PaginationConfig`

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


_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef(
    _ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef
):
    """
    Type definition for `ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValues` `Value`

    The value for the typed link.

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef",
    {
        "AttributeName": str,
        "Value": ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesValueTypeDef,
    },
    total=False,
)


class ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef(
    _ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef
):
    """
    Type definition for `ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiers` `IdentityAttributeValues`

    Identifies the attribute name and value for a typed link.

    - **AttributeName** *(string) --*

      The attribute name of the typed link.

    - **Value** *(dict) --*

      The value for the typed link.

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.
    """


_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef(
    _ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef
):
    """
    Type definition for `ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiers` `SourceObjectReference`

    Identifies the source object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading
      to it from the directory root. Use the link names from each parent/child link to
      construct the path. Path selectors start with a slash (/) and link names are separated
      by slashes. For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
      Cloud Directory. When creating objects, the system will provide you with the identifier
      of the created object. An object’s identifier is immutable and no two objects will ever
      share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef(
    _ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef
):
    """
    Type definition for `ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiers` `TargetObjectReference`

    Identifies the target object that the typed link will attach to.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading
      to it from the directory root. Use the link names from each parent/child link to
      construct the path. Path selectors start with a slash (/) and link names are separated
      by slashes. For more information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
      Cloud Directory. When creating objects, the system will provide you with the identifier
      of the created object. An object’s identifier is immutable and no two objects will ever
      share the same object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypedLinkFacetTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypedLinkFacetTypeDef",
    {"SchemaArn": str, "TypedLinkName": str},
    total=False,
)


class ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypedLinkFacetTypeDef(
    _ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypedLinkFacetTypeDef
):
    """
    Type definition for `ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiers` `TypedLinkFacet`

    Identifies the typed link facet that is associated with the typed link.

    - **SchemaArn** *(string) --*

      The Amazon Resource Name (ARN) that is associated with the schema. For more
      information, see  arns .

    - **TypedLinkName** *(string) --*

      The unique name of the typed link facet.
    """


_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypeDef",
    {
        "TypedLinkFacet": ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypedLinkFacetTypeDef,
        "SourceObjectReference": ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersSourceObjectReferenceTypeDef,
        "TargetObjectReference": ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTargetObjectReferenceTypeDef,
        "IdentityAttributeValues": List[
            ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersIdentityAttributeValuesTypeDef
        ],
    },
    total=False,
)


class ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypeDef(
    _ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypeDef
):
    """
    Type definition for `ListOutgoingTypedLinksPaginateResponse` `TypedLinkSpecifiers`

    Contains all the information that is used to uniquely identify a typed link. The parameters
    discussed in this topic are used to uniquely specify the typed link being operated on. The
    AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts
    one as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API
    operations provide typed link specifiers as output. You can also construct a typed link
    specifier from scratch.

    - **TypedLinkFacet** *(dict) --*

      Identifies the typed link facet that is associated with the typed link.

      - **SchemaArn** *(string) --*

        The Amazon Resource Name (ARN) that is associated with the schema. For more
        information, see  arns .

      - **TypedLinkName** *(string) --*

        The unique name of the typed link facet.

    - **SourceObjectReference** *(dict) --*

      Identifies the source object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading
        to it from the directory root. Use the link names from each parent/child link to
        construct the path. Path selectors start with a slash (/) and link names are separated
        by slashes. For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
        Cloud Directory. When creating objects, the system will provide you with the identifier
        of the created object. An object’s identifier is immutable and no two objects will ever
        share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **TargetObjectReference** *(dict) --*

      Identifies the target object that the typed link will attach to.

      - **Selector** *(string) --*

        A path selector supports easy selection of an object by the parent/child links leading
        to it from the directory root. Use the link names from each parent/child link to
        construct the path. Path selectors start with a slash (/) and link names are separated
        by slashes. For more information about paths, see `Access Objects
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
        . You can identify an object in one of the following ways:

        * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
        Cloud Directory. When creating objects, the system will provide you with the identifier
        of the created object. An object’s identifier is immutable and no two objects will ever
        share the same object identifier

        * */some/path* - Identifies the object based on path

        * *#SomeBatchReference* - Identifies the object in a batch call

    - **IdentityAttributeValues** *(list) --*

      Identifies the attribute value to update.

      - *(dict) --*

        Identifies the attribute name and value for a typed link.

        - **AttributeName** *(string) --*

          The attribute name of the typed link.

        - **Value** *(dict) --*

          The value for the typed link.

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.
    """


_ListOutgoingTypedLinksPaginateResponseTypeDef = TypedDict(
    "_ListOutgoingTypedLinksPaginateResponseTypeDef",
    {
        "TypedLinkSpecifiers": List[
            ListOutgoingTypedLinksPaginateResponseTypedLinkSpecifiersTypeDef
        ]
    },
    total=False,
)


class ListOutgoingTypedLinksPaginateResponseTypeDef(
    _ListOutgoingTypedLinksPaginateResponseTypeDef
):
    """
    Type definition for `ListOutgoingTypedLinksPaginate` `Response`

    - **TypedLinkSpecifiers** *(list) --*

      Returns a typed link specifier as output.

      - *(dict) --*

        Contains all the information that is used to uniquely identify a typed link. The parameters
        discussed in this topic are used to uniquely specify the typed link being operated on. The
        AttachTypedLink API returns a typed link specifier while the  DetachTypedLink API accepts
        one as input. Similarly, the  ListIncomingTypedLinks and  ListOutgoingTypedLinks API
        operations provide typed link specifiers as output. You can also construct a typed link
        specifier from scratch.

        - **TypedLinkFacet** *(dict) --*

          Identifies the typed link facet that is associated with the typed link.

          - **SchemaArn** *(string) --*

            The Amazon Resource Name (ARN) that is associated with the schema. For more
            information, see  arns .

          - **TypedLinkName** *(string) --*

            The unique name of the typed link facet.

        - **SourceObjectReference** *(dict) --*

          Identifies the source object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links leading
            to it from the directory root. Use the link names from each parent/child link to
            construct the path. Path selectors start with a slash (/) and link names are separated
            by slashes. For more information about paths, see `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
            Cloud Directory. When creating objects, the system will provide you with the identifier
            of the created object. An object’s identifier is immutable and no two objects will ever
            share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **TargetObjectReference** *(dict) --*

          Identifies the target object that the typed link will attach to.

          - **Selector** *(string) --*

            A path selector supports easy selection of an object by the parent/child links leading
            to it from the directory root. Use the link names from each parent/child link to
            construct the path. Path selectors start with a slash (/) and link names are separated
            by slashes. For more information about paths, see `Access Objects
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
            . You can identify an object in one of the following ways:

            * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon
            Cloud Directory. When creating objects, the system will provide you with the identifier
            of the created object. An object’s identifier is immutable and no two objects will ever
            share the same object identifier

            * */some/path* - Identifies the object based on path

            * *#SomeBatchReference* - Identifies the object in a batch call

        - **IdentityAttributeValues** *(list) --*

          Identifies the attribute value to update.

          - *(dict) --*

            Identifies the attribute name and value for a typed link.

            - **AttributeName** *(string) --*

              The attribute name of the typed link.

            - **Value** *(dict) --*

              The value for the typed link.

              - **StringValue** *(string) --*

                A string data value.

              - **BinaryValue** *(bytes) --*

                A binary data value.

              - **BooleanValue** *(boolean) --*

                A Boolean data value.

              - **NumberValue** *(string) --*

                A number data value.

              - **DatetimeValue** *(datetime) --*

                A date and time value.
    """


_ListPolicyAttachmentsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPolicyAttachmentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPolicyAttachmentsPaginatePaginationConfigTypeDef(
    _ListPolicyAttachmentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPolicyAttachmentsPaginate` `PaginationConfig`

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


_ListPolicyAttachmentsPaginatePolicyReferenceTypeDef = TypedDict(
    "_ListPolicyAttachmentsPaginatePolicyReferenceTypeDef",
    {"Selector": str},
    total=False,
)


class ListPolicyAttachmentsPaginatePolicyReferenceTypeDef(
    _ListPolicyAttachmentsPaginatePolicyReferenceTypeDef
):
    """
    Type definition for `ListPolicyAttachmentsPaginate` `PolicyReference`

    The reference that identifies the policy object.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_ListPolicyAttachmentsPaginateResponseTypeDef = TypedDict(
    "_ListPolicyAttachmentsPaginateResponseTypeDef",
    {"ObjectIdentifiers": List[str]},
    total=False,
)


class ListPolicyAttachmentsPaginateResponseTypeDef(
    _ListPolicyAttachmentsPaginateResponseTypeDef
):
    """
    Type definition for `ListPolicyAttachmentsPaginate` `Response`

    - **ObjectIdentifiers** *(list) --*

      A list of ``ObjectIdentifiers`` to which the policy is attached.

      - *(string) --*
    """


_ListPublishedSchemaArnsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPublishedSchemaArnsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPublishedSchemaArnsPaginatePaginationConfigTypeDef(
    _ListPublishedSchemaArnsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPublishedSchemaArnsPaginate` `PaginationConfig`

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


_ListPublishedSchemaArnsPaginateResponseTypeDef = TypedDict(
    "_ListPublishedSchemaArnsPaginateResponseTypeDef",
    {"SchemaArns": List[str]},
    total=False,
)


class ListPublishedSchemaArnsPaginateResponseTypeDef(
    _ListPublishedSchemaArnsPaginateResponseTypeDef
):
    """
    Type definition for `ListPublishedSchemaArnsPaginate` `Response`

    - **SchemaArns** *(list) --*

      The ARNs of published schemas.

      - *(string) --*
    """


_ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagsForResourcePaginatePaginationConfigTypeDef(
    _ListTagsForResourcePaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginate` `PaginationConfig`

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


_ListTagsForResourcePaginateResponseTagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListTagsForResourcePaginateResponseTagsTypeDef(
    _ListTagsForResourcePaginateResponseTagsTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginateResponse` `Tags`

    The tag structure that contains a tag key and value.

    - **Key** *(string) --*

      The key that is associated with the tag.

    - **Value** *(string) --*

      The value that is associated with the tag.
    """


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {"Tags": List[ListTagsForResourcePaginateResponseTagsTypeDef]},
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(
    _ListTagsForResourcePaginateResponseTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginate` `Response`

    - **Tags** *(list) --*

      A list of tag key value pairs that are associated with the response.

      - *(dict) --*

        The tag structure that contains a tag key and value.

        - **Key** *(string) --*

          The key that is associated with the tag.

        - **Value** *(string) --*

          The value that is associated with the tag.
    """


_ListTypedLinkFacetAttributesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTypedLinkFacetAttributesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTypedLinkFacetAttributesPaginatePaginationConfigTypeDef(
    _ListTypedLinkFacetAttributesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTypedLinkFacetAttributesPaginate` `PaginationConfig`

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


_ListTypedLinkFacetAttributesPaginateResponseAttributesDefaultValueTypeDef = TypedDict(
    "_ListTypedLinkFacetAttributesPaginateResponseAttributesDefaultValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "BooleanValue": bool,
        "NumberValue": str,
        "DatetimeValue": datetime,
    },
    total=False,
)


class ListTypedLinkFacetAttributesPaginateResponseAttributesDefaultValueTypeDef(
    _ListTypedLinkFacetAttributesPaginateResponseAttributesDefaultValueTypeDef
):
    """
    Type definition for `ListTypedLinkFacetAttributesPaginateResponseAttributes` `DefaultValue`

    The default value of the attribute (if configured).

    - **StringValue** *(string) --*

      A string data value.

    - **BinaryValue** *(bytes) --*

      A binary data value.

    - **BooleanValue** *(boolean) --*

      A Boolean data value.

    - **NumberValue** *(string) --*

      A number data value.

    - **DatetimeValue** *(datetime) --*

      A date and time value.
    """


_ListTypedLinkFacetAttributesPaginateResponseAttributesRulesTypeDef = TypedDict(
    "_ListTypedLinkFacetAttributesPaginateResponseAttributesRulesTypeDef",
    {"Type": str, "Parameters": Dict[str, str]},
    total=False,
)


class ListTypedLinkFacetAttributesPaginateResponseAttributesRulesTypeDef(
    _ListTypedLinkFacetAttributesPaginateResponseAttributesRulesTypeDef
):
    """
    Type definition for `ListTypedLinkFacetAttributesPaginateResponseAttributes` `Rules`

    Contains an Amazon Resource Name (ARN) and parameters that are associated with the
    rule.

    - **Type** *(string) --*

      The type of attribute validation rule.

    - **Parameters** *(dict) --*

      The minimum and maximum parameters that are associated with the rule.

      - *(string) --*

        - *(string) --*
    """


_ListTypedLinkFacetAttributesPaginateResponseAttributesTypeDef = TypedDict(
    "_ListTypedLinkFacetAttributesPaginateResponseAttributesTypeDef",
    {
        "Name": str,
        "Type": str,
        "DefaultValue": ListTypedLinkFacetAttributesPaginateResponseAttributesDefaultValueTypeDef,
        "IsImmutable": bool,
        "Rules": Dict[
            str, ListTypedLinkFacetAttributesPaginateResponseAttributesRulesTypeDef
        ],
        "RequiredBehavior": str,
    },
    total=False,
)


class ListTypedLinkFacetAttributesPaginateResponseAttributesTypeDef(
    _ListTypedLinkFacetAttributesPaginateResponseAttributesTypeDef
):
    """
    Type definition for `ListTypedLinkFacetAttributesPaginateResponse` `Attributes`

    A typed link attribute definition.

    - **Name** *(string) --*

      The unique name of the typed link attribute.

    - **Type** *(string) --*

      The type of the attribute.

    - **DefaultValue** *(dict) --*

      The default value of the attribute (if configured).

      - **StringValue** *(string) --*

        A string data value.

      - **BinaryValue** *(bytes) --*

        A binary data value.

      - **BooleanValue** *(boolean) --*

        A Boolean data value.

      - **NumberValue** *(string) --*

        A number data value.

      - **DatetimeValue** *(datetime) --*

        A date and time value.

    - **IsImmutable** *(boolean) --*

      Whether the attribute is mutable or not.

    - **Rules** *(dict) --*

      Validation rules that are attached to the attribute definition.

      - *(string) --*

        - *(dict) --*

          Contains an Amazon Resource Name (ARN) and parameters that are associated with the
          rule.

          - **Type** *(string) --*

            The type of attribute validation rule.

          - **Parameters** *(dict) --*

            The minimum and maximum parameters that are associated with the rule.

            - *(string) --*

              - *(string) --*

    - **RequiredBehavior** *(string) --*

      The required behavior of the ``TypedLinkAttributeDefinition`` .
    """


_ListTypedLinkFacetAttributesPaginateResponseTypeDef = TypedDict(
    "_ListTypedLinkFacetAttributesPaginateResponseTypeDef",
    {"Attributes": List[ListTypedLinkFacetAttributesPaginateResponseAttributesTypeDef]},
    total=False,
)


class ListTypedLinkFacetAttributesPaginateResponseTypeDef(
    _ListTypedLinkFacetAttributesPaginateResponseTypeDef
):
    """
    Type definition for `ListTypedLinkFacetAttributesPaginate` `Response`

    - **Attributes** *(list) --*

      An ordered set of attributes associate with the typed link.

      - *(dict) --*

        A typed link attribute definition.

        - **Name** *(string) --*

          The unique name of the typed link attribute.

        - **Type** *(string) --*

          The type of the attribute.

        - **DefaultValue** *(dict) --*

          The default value of the attribute (if configured).

          - **StringValue** *(string) --*

            A string data value.

          - **BinaryValue** *(bytes) --*

            A binary data value.

          - **BooleanValue** *(boolean) --*

            A Boolean data value.

          - **NumberValue** *(string) --*

            A number data value.

          - **DatetimeValue** *(datetime) --*

            A date and time value.

        - **IsImmutable** *(boolean) --*

          Whether the attribute is mutable or not.

        - **Rules** *(dict) --*

          Validation rules that are attached to the attribute definition.

          - *(string) --*

            - *(dict) --*

              Contains an Amazon Resource Name (ARN) and parameters that are associated with the
              rule.

              - **Type** *(string) --*

                The type of attribute validation rule.

              - **Parameters** *(dict) --*

                The minimum and maximum parameters that are associated with the rule.

                - *(string) --*

                  - *(string) --*

        - **RequiredBehavior** *(string) --*

          The required behavior of the ``TypedLinkAttributeDefinition`` .
    """


_ListTypedLinkFacetNamesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTypedLinkFacetNamesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTypedLinkFacetNamesPaginatePaginationConfigTypeDef(
    _ListTypedLinkFacetNamesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTypedLinkFacetNamesPaginate` `PaginationConfig`

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


_ListTypedLinkFacetNamesPaginateResponseTypeDef = TypedDict(
    "_ListTypedLinkFacetNamesPaginateResponseTypeDef",
    {"FacetNames": List[str]},
    total=False,
)


class ListTypedLinkFacetNamesPaginateResponseTypeDef(
    _ListTypedLinkFacetNamesPaginateResponseTypeDef
):
    """
    Type definition for `ListTypedLinkFacetNamesPaginate` `Response`

    - **FacetNames** *(list) --*

      The names of typed link facets that exist within the schema.

      - *(string) --*
    """


_LookupPolicyPaginateObjectReferenceTypeDef = TypedDict(
    "_LookupPolicyPaginateObjectReferenceTypeDef", {"Selector": str}, total=False
)


class LookupPolicyPaginateObjectReferenceTypeDef(
    _LookupPolicyPaginateObjectReferenceTypeDef
):
    """
    Type definition for `LookupPolicyPaginate` `ObjectReference`

    Reference that identifies the object whose policies will be looked up.

    - **Selector** *(string) --*

      A path selector supports easy selection of an object by the parent/child links leading to it
      from the directory root. Use the link names from each parent/child link to construct the path.
      Path selectors start with a slash (/) and link names are separated by slashes. For more
      information about paths, see `Access Objects
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/directory_objects_access_objects.html>`__
      . You can identify an object in one of the following ways:

      * *$ObjectIdentifier* - An object identifier is an opaque string provided by Amazon Cloud
      Directory. When creating objects, the system will provide you with the identifier of the
      created object. An object’s identifier is immutable and no two objects will ever share the same
      object identifier

      * */some/path* - Identifies the object based on path

      * *#SomeBatchReference* - Identifies the object in a batch call
    """


_LookupPolicyPaginatePaginationConfigTypeDef = TypedDict(
    "_LookupPolicyPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class LookupPolicyPaginatePaginationConfigTypeDef(
    _LookupPolicyPaginatePaginationConfigTypeDef
):
    """
    Type definition for `LookupPolicyPaginate` `PaginationConfig`

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


_LookupPolicyPaginateResponsePolicyToPathListPoliciesTypeDef = TypedDict(
    "_LookupPolicyPaginateResponsePolicyToPathListPoliciesTypeDef",
    {"PolicyId": str, "ObjectIdentifier": str, "PolicyType": str},
    total=False,
)


class LookupPolicyPaginateResponsePolicyToPathListPoliciesTypeDef(
    _LookupPolicyPaginateResponsePolicyToPathListPoliciesTypeDef
):
    """
    Type definition for `LookupPolicyPaginateResponsePolicyToPathList` `Policies`

    Contains the ``PolicyType`` , ``PolicyId`` , and the ``ObjectIdentifier`` to which it
    is attached. For more information, see `Policies
    <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
    .

    - **PolicyId** *(string) --*

      The ID of ``PolicyAttachment`` .

    - **ObjectIdentifier** *(string) --*

      The ``ObjectIdentifier`` that is associated with ``PolicyAttachment`` .

    - **PolicyType** *(string) --*

      The type of policy that can be associated with ``PolicyAttachment`` .
    """


_LookupPolicyPaginateResponsePolicyToPathListTypeDef = TypedDict(
    "_LookupPolicyPaginateResponsePolicyToPathListTypeDef",
    {
        "Path": str,
        "Policies": List[LookupPolicyPaginateResponsePolicyToPathListPoliciesTypeDef],
    },
    total=False,
)


class LookupPolicyPaginateResponsePolicyToPathListTypeDef(
    _LookupPolicyPaginateResponsePolicyToPathListTypeDef
):
    """
    Type definition for `LookupPolicyPaginateResponse` `PolicyToPathList`

    Used when a regular object exists in a  Directory and you want to find all of the policies
    that are associated with that object and the parent to that object.

    - **Path** *(string) --*

      The path that is referenced from the root.

    - **Policies** *(list) --*

      List of policy objects.

      - *(dict) --*

        Contains the ``PolicyType`` , ``PolicyId`` , and the ``ObjectIdentifier`` to which it
        is attached. For more information, see `Policies
        <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
        .

        - **PolicyId** *(string) --*

          The ID of ``PolicyAttachment`` .

        - **ObjectIdentifier** *(string) --*

          The ``ObjectIdentifier`` that is associated with ``PolicyAttachment`` .

        - **PolicyType** *(string) --*

          The type of policy that can be associated with ``PolicyAttachment`` .
    """


_LookupPolicyPaginateResponseTypeDef = TypedDict(
    "_LookupPolicyPaginateResponseTypeDef",
    {"PolicyToPathList": List[LookupPolicyPaginateResponsePolicyToPathListTypeDef]},
    total=False,
)


class LookupPolicyPaginateResponseTypeDef(_LookupPolicyPaginateResponseTypeDef):
    """
    Type definition for `LookupPolicyPaginate` `Response`

    - **PolicyToPathList** *(list) --*

      Provides list of path to policies. Policies contain ``PolicyId`` , ``ObjectIdentifier`` , and
      ``PolicyType`` . For more information, see `Policies
      <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
      .

      - *(dict) --*

        Used when a regular object exists in a  Directory and you want to find all of the policies
        that are associated with that object and the parent to that object.

        - **Path** *(string) --*

          The path that is referenced from the root.

        - **Policies** *(list) --*

          List of policy objects.

          - *(dict) --*

            Contains the ``PolicyType`` , ``PolicyId`` , and the ``ObjectIdentifier`` to which it
            is attached. For more information, see `Policies
            <https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies>`__
            .

            - **PolicyId** *(string) --*

              The ID of ``PolicyAttachment`` .

            - **ObjectIdentifier** *(string) --*

              The ``ObjectIdentifier`` that is associated with ``PolicyAttachment`` .

            - **PolicyType** *(string) --*

              The type of policy that can be associated with ``PolicyAttachment`` .
    """

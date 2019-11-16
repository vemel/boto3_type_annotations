"Main interface for servicecatalog type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientBatchAssociateServiceActionWithProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef",
    "ClientBatchAssociateServiceActionWithProvisioningArtifactResponseTypeDef",
    "ClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef",
    "ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef",
    "ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseTypeDef",
    "ClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef",
    "ClientCopyProductResponseTypeDef",
    "ClientCreateConstraintResponseConstraintDetailTypeDef",
    "ClientCreateConstraintResponseTypeDef",
    "ClientCreatePortfolioResponsePortfolioDetailTypeDef",
    "ClientCreatePortfolioResponseTagsTypeDef",
    "ClientCreatePortfolioResponseTypeDef",
    "ClientCreatePortfolioShareOrganizationNodeTypeDef",
    "ClientCreatePortfolioShareResponseTypeDef",
    "ClientCreatePortfolioTagsTypeDef",
    "ClientCreateProductProvisioningArtifactParametersTypeDef",
    "ClientCreateProductResponseProductViewDetailProductViewSummaryTypeDef",
    "ClientCreateProductResponseProductViewDetailTypeDef",
    "ClientCreateProductResponseProvisioningArtifactDetailTypeDef",
    "ClientCreateProductResponseTagsTypeDef",
    "ClientCreateProductResponseTypeDef",
    "ClientCreateProductTagsTypeDef",
    "ClientCreateProvisionedProductPlanProvisioningParametersTypeDef",
    "ClientCreateProvisionedProductPlanResponseTypeDef",
    "ClientCreateProvisionedProductPlanTagsTypeDef",
    "ClientCreateProvisioningArtifactParametersTypeDef",
    "ClientCreateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef",
    "ClientCreateProvisioningArtifactResponseTypeDef",
    "ClientCreateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef",
    "ClientCreateServiceActionResponseServiceActionDetailTypeDef",
    "ClientCreateServiceActionResponseTypeDef",
    "ClientCreateTagOptionResponseTagOptionDetailTypeDef",
    "ClientCreateTagOptionResponseTypeDef",
    "ClientDeletePortfolioShareOrganizationNodeTypeDef",
    "ClientDeletePortfolioShareResponseTypeDef",
    "ClientDescribeConstraintResponseConstraintDetailTypeDef",
    "ClientDescribeConstraintResponseTypeDef",
    "ClientDescribeCopyProductStatusResponseTypeDef",
    "ClientDescribePortfolioResponseBudgetsTypeDef",
    "ClientDescribePortfolioResponsePortfolioDetailTypeDef",
    "ClientDescribePortfolioResponseTagOptionsTypeDef",
    "ClientDescribePortfolioResponseTagsTypeDef",
    "ClientDescribePortfolioResponseTypeDef",
    "ClientDescribePortfolioShareStatusResponseShareDetailsShareErrorsTypeDef",
    "ClientDescribePortfolioShareStatusResponseShareDetailsTypeDef",
    "ClientDescribePortfolioShareStatusResponseTypeDef",
    "ClientDescribeProductAsAdminResponseBudgetsTypeDef",
    "ClientDescribeProductAsAdminResponseProductViewDetailProductViewSummaryTypeDef",
    "ClientDescribeProductAsAdminResponseProductViewDetailTypeDef",
    "ClientDescribeProductAsAdminResponseProvisioningArtifactSummariesTypeDef",
    "ClientDescribeProductAsAdminResponseTagOptionsTypeDef",
    "ClientDescribeProductAsAdminResponseTagsTypeDef",
    "ClientDescribeProductAsAdminResponseTypeDef",
    "ClientDescribeProductResponseBudgetsTypeDef",
    "ClientDescribeProductResponseProductViewSummaryTypeDef",
    "ClientDescribeProductResponseProvisioningArtifactsTypeDef",
    "ClientDescribeProductResponseTypeDef",
    "ClientDescribeProductViewResponseProductViewSummaryTypeDef",
    "ClientDescribeProductViewResponseProvisioningArtifactsTypeDef",
    "ClientDescribeProductViewResponseTypeDef",
    "ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsProvisioningParametersTypeDef",
    "ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTagsTypeDef",
    "ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTypeDef",
    "ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTargetTypeDef",
    "ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTypeDef",
    "ClientDescribeProvisionedProductPlanResponseResourceChangesTypeDef",
    "ClientDescribeProvisionedProductPlanResponseTypeDef",
    "ClientDescribeProvisionedProductResponseCloudWatchDashboardsTypeDef",
    "ClientDescribeProvisionedProductResponseProvisionedProductDetailTypeDef",
    "ClientDescribeProvisionedProductResponseTypeDef",
    "ClientDescribeProvisioningArtifactResponseProvisioningArtifactDetailTypeDef",
    "ClientDescribeProvisioningArtifactResponseTypeDef",
    "ClientDescribeProvisioningParametersResponseConstraintSummariesTypeDef",
    "ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersParameterConstraintsTypeDef",
    "ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersTypeDef",
    "ClientDescribeProvisioningParametersResponseProvisioningArtifactPreferencesTypeDef",
    "ClientDescribeProvisioningParametersResponseTagOptionsTypeDef",
    "ClientDescribeProvisioningParametersResponseUsageInstructionsTypeDef",
    "ClientDescribeProvisioningParametersResponseTypeDef",
    "ClientDescribeRecordResponseRecordDetailRecordErrorsTypeDef",
    "ClientDescribeRecordResponseRecordDetailRecordTagsTypeDef",
    "ClientDescribeRecordResponseRecordDetailTypeDef",
    "ClientDescribeRecordResponseRecordOutputsTypeDef",
    "ClientDescribeRecordResponseTypeDef",
    "ClientDescribeServiceActionExecutionParametersResponseServiceActionParametersTypeDef",
    "ClientDescribeServiceActionExecutionParametersResponseTypeDef",
    "ClientDescribeServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef",
    "ClientDescribeServiceActionResponseServiceActionDetailTypeDef",
    "ClientDescribeServiceActionResponseTypeDef",
    "ClientDescribeTagOptionResponseTagOptionDetailTypeDef",
    "ClientDescribeTagOptionResponseTypeDef",
    "ClientExecuteProvisionedProductPlanResponseRecordDetailRecordErrorsTypeDef",
    "ClientExecuteProvisionedProductPlanResponseRecordDetailRecordTagsTypeDef",
    "ClientExecuteProvisionedProductPlanResponseRecordDetailTypeDef",
    "ClientExecuteProvisionedProductPlanResponseTypeDef",
    "ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordErrorsTypeDef",
    "ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordTagsTypeDef",
    "ClientExecuteProvisionedProductServiceActionResponseRecordDetailTypeDef",
    "ClientExecuteProvisionedProductServiceActionResponseTypeDef",
    "ClientGetAwsOrganizationsAccessStatusResponseTypeDef",
    "ClientListAcceptedPortfolioSharesResponsePortfolioDetailsTypeDef",
    "ClientListAcceptedPortfolioSharesResponseTypeDef",
    "ClientListBudgetsForResourceResponseBudgetsTypeDef",
    "ClientListBudgetsForResourceResponseTypeDef",
    "ClientListConstraintsForPortfolioResponseConstraintDetailsTypeDef",
    "ClientListConstraintsForPortfolioResponseTypeDef",
    "ClientListLaunchPathsResponseLaunchPathSummariesConstraintSummariesTypeDef",
    "ClientListLaunchPathsResponseLaunchPathSummariesTagsTypeDef",
    "ClientListLaunchPathsResponseLaunchPathSummariesTypeDef",
    "ClientListLaunchPathsResponseTypeDef",
    "ClientListOrganizationPortfolioAccessResponseOrganizationNodesTypeDef",
    "ClientListOrganizationPortfolioAccessResponseTypeDef",
    "ClientListPortfolioAccessResponseTypeDef",
    "ClientListPortfoliosForProductResponsePortfolioDetailsTypeDef",
    "ClientListPortfoliosForProductResponseTypeDef",
    "ClientListPortfoliosResponsePortfolioDetailsTypeDef",
    "ClientListPortfoliosResponseTypeDef",
    "ClientListPrincipalsForPortfolioResponsePrincipalsTypeDef",
    "ClientListPrincipalsForPortfolioResponseTypeDef",
    "ClientListProvisionedProductPlansAccessLevelFilterTypeDef",
    "ClientListProvisionedProductPlansResponseProvisionedProductPlansTypeDef",
    "ClientListProvisionedProductPlansResponseTypeDef",
    "ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProductViewSummaryTypeDef",
    "ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProvisioningArtifactTypeDef",
    "ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsTypeDef",
    "ClientListProvisioningArtifactsForServiceActionResponseTypeDef",
    "ClientListProvisioningArtifactsResponseProvisioningArtifactDetailsTypeDef",
    "ClientListProvisioningArtifactsResponseTypeDef",
    "ClientListRecordHistoryAccessLevelFilterTypeDef",
    "ClientListRecordHistoryResponseRecordDetailsRecordErrorsTypeDef",
    "ClientListRecordHistoryResponseRecordDetailsRecordTagsTypeDef",
    "ClientListRecordHistoryResponseRecordDetailsTypeDef",
    "ClientListRecordHistoryResponseTypeDef",
    "ClientListRecordHistorySearchFilterTypeDef",
    "ClientListResourcesForTagOptionResponseResourceDetailsTypeDef",
    "ClientListResourcesForTagOptionResponseTypeDef",
    "ClientListServiceActionsForProvisioningArtifactResponseServiceActionSummariesTypeDef",
    "ClientListServiceActionsForProvisioningArtifactResponseTypeDef",
    "ClientListServiceActionsResponseServiceActionSummariesTypeDef",
    "ClientListServiceActionsResponseTypeDef",
    "ClientListStackInstancesForProvisionedProductResponseStackInstancesTypeDef",
    "ClientListStackInstancesForProvisionedProductResponseTypeDef",
    "ClientListTagOptionsFiltersTypeDef",
    "ClientListTagOptionsResponseTagOptionDetailsTypeDef",
    "ClientListTagOptionsResponseTypeDef",
    "ClientProvisionProductProvisioningParametersTypeDef",
    "ClientProvisionProductProvisioningPreferencesTypeDef",
    "ClientProvisionProductResponseRecordDetailRecordErrorsTypeDef",
    "ClientProvisionProductResponseRecordDetailRecordTagsTypeDef",
    "ClientProvisionProductResponseRecordDetailTypeDef",
    "ClientProvisionProductResponseTypeDef",
    "ClientProvisionProductTagsTypeDef",
    "ClientScanProvisionedProductsAccessLevelFilterTypeDef",
    "ClientScanProvisionedProductsResponseProvisionedProductsTypeDef",
    "ClientScanProvisionedProductsResponseTypeDef",
    "ClientSearchProductsAsAdminResponseProductViewDetailsProductViewSummaryTypeDef",
    "ClientSearchProductsAsAdminResponseProductViewDetailsTypeDef",
    "ClientSearchProductsAsAdminResponseTypeDef",
    "ClientSearchProductsResponseProductViewAggregationsTypeDef",
    "ClientSearchProductsResponseProductViewSummariesTypeDef",
    "ClientSearchProductsResponseTypeDef",
    "ClientSearchProvisionedProductsAccessLevelFilterTypeDef",
    "ClientSearchProvisionedProductsResponseProvisionedProductsTagsTypeDef",
    "ClientSearchProvisionedProductsResponseProvisionedProductsTypeDef",
    "ClientSearchProvisionedProductsResponseTypeDef",
    "ClientTerminateProvisionedProductResponseRecordDetailRecordErrorsTypeDef",
    "ClientTerminateProvisionedProductResponseRecordDetailRecordTagsTypeDef",
    "ClientTerminateProvisionedProductResponseRecordDetailTypeDef",
    "ClientTerminateProvisionedProductResponseTypeDef",
    "ClientUpdateConstraintResponseConstraintDetailTypeDef",
    "ClientUpdateConstraintResponseTypeDef",
    "ClientUpdatePortfolioAddTagsTypeDef",
    "ClientUpdatePortfolioResponsePortfolioDetailTypeDef",
    "ClientUpdatePortfolioResponseTagsTypeDef",
    "ClientUpdatePortfolioResponseTypeDef",
    "ClientUpdateProductAddTagsTypeDef",
    "ClientUpdateProductResponseProductViewDetailProductViewSummaryTypeDef",
    "ClientUpdateProductResponseProductViewDetailTypeDef",
    "ClientUpdateProductResponseTagsTypeDef",
    "ClientUpdateProductResponseTypeDef",
    "ClientUpdateProvisionedProductPropertiesResponseTypeDef",
    "ClientUpdateProvisionedProductProvisioningParametersTypeDef",
    "ClientUpdateProvisionedProductProvisioningPreferencesTypeDef",
    "ClientUpdateProvisionedProductResponseRecordDetailRecordErrorsTypeDef",
    "ClientUpdateProvisionedProductResponseRecordDetailRecordTagsTypeDef",
    "ClientUpdateProvisionedProductResponseRecordDetailTypeDef",
    "ClientUpdateProvisionedProductResponseTypeDef",
    "ClientUpdateProvisionedProductTagsTypeDef",
    "ClientUpdateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef",
    "ClientUpdateProvisioningArtifactResponseTypeDef",
    "ClientUpdateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef",
    "ClientUpdateServiceActionResponseServiceActionDetailTypeDef",
    "ClientUpdateServiceActionResponseTypeDef",
    "ClientUpdateTagOptionResponseTagOptionDetailTypeDef",
    "ClientUpdateTagOptionResponseTypeDef",
    "ListAcceptedPortfolioSharesPaginatePaginationConfigTypeDef",
    "ListAcceptedPortfolioSharesPaginateResponsePortfolioDetailsTypeDef",
    "ListAcceptedPortfolioSharesPaginateResponseTypeDef",
    "ListConstraintsForPortfolioPaginatePaginationConfigTypeDef",
    "ListConstraintsForPortfolioPaginateResponseConstraintDetailsTypeDef",
    "ListConstraintsForPortfolioPaginateResponseTypeDef",
    "ListLaunchPathsPaginatePaginationConfigTypeDef",
    "ListLaunchPathsPaginateResponseLaunchPathSummariesConstraintSummariesTypeDef",
    "ListLaunchPathsPaginateResponseLaunchPathSummariesTagsTypeDef",
    "ListLaunchPathsPaginateResponseLaunchPathSummariesTypeDef",
    "ListLaunchPathsPaginateResponseTypeDef",
    "ListOrganizationPortfolioAccessPaginatePaginationConfigTypeDef",
    "ListOrganizationPortfolioAccessPaginateResponseOrganizationNodesTypeDef",
    "ListOrganizationPortfolioAccessPaginateResponseTypeDef",
    "ListPortfoliosForProductPaginatePaginationConfigTypeDef",
    "ListPortfoliosForProductPaginateResponsePortfolioDetailsTypeDef",
    "ListPortfoliosForProductPaginateResponseTypeDef",
    "ListPortfoliosPaginatePaginationConfigTypeDef",
    "ListPortfoliosPaginateResponsePortfolioDetailsTypeDef",
    "ListPortfoliosPaginateResponseTypeDef",
    "ListPrincipalsForPortfolioPaginatePaginationConfigTypeDef",
    "ListPrincipalsForPortfolioPaginateResponsePrincipalsTypeDef",
    "ListPrincipalsForPortfolioPaginateResponseTypeDef",
    "ListProvisionedProductPlansPaginateAccessLevelFilterTypeDef",
    "ListProvisionedProductPlansPaginatePaginationConfigTypeDef",
    "ListProvisionedProductPlansPaginateResponseProvisionedProductPlansTypeDef",
    "ListProvisionedProductPlansPaginateResponseTypeDef",
    "ListProvisioningArtifactsForServiceActionPaginatePaginationConfigTypeDef",
    "ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProductViewSummaryTypeDef",
    "ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProvisioningArtifactTypeDef",
    "ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsTypeDef",
    "ListProvisioningArtifactsForServiceActionPaginateResponseTypeDef",
    "ListRecordHistoryPaginateAccessLevelFilterTypeDef",
    "ListRecordHistoryPaginatePaginationConfigTypeDef",
    "ListRecordHistoryPaginateResponseRecordDetailsRecordErrorsTypeDef",
    "ListRecordHistoryPaginateResponseRecordDetailsRecordTagsTypeDef",
    "ListRecordHistoryPaginateResponseRecordDetailsTypeDef",
    "ListRecordHistoryPaginateResponseTypeDef",
    "ListRecordHistoryPaginateSearchFilterTypeDef",
    "ListResourcesForTagOptionPaginatePaginationConfigTypeDef",
    "ListResourcesForTagOptionPaginateResponseResourceDetailsTypeDef",
    "ListResourcesForTagOptionPaginateResponseTypeDef",
    "ListServiceActionsForProvisioningArtifactPaginatePaginationConfigTypeDef",
    "ListServiceActionsForProvisioningArtifactPaginateResponseServiceActionSummariesTypeDef",
    "ListServiceActionsForProvisioningArtifactPaginateResponseTypeDef",
    "ListServiceActionsPaginatePaginationConfigTypeDef",
    "ListServiceActionsPaginateResponseServiceActionSummariesTypeDef",
    "ListServiceActionsPaginateResponseTypeDef",
    "ListTagOptionsPaginateFiltersTypeDef",
    "ListTagOptionsPaginatePaginationConfigTypeDef",
    "ListTagOptionsPaginateResponseTagOptionDetailsTypeDef",
    "ListTagOptionsPaginateResponseTypeDef",
    "ScanProvisionedProductsPaginateAccessLevelFilterTypeDef",
    "ScanProvisionedProductsPaginatePaginationConfigTypeDef",
    "ScanProvisionedProductsPaginateResponseProvisionedProductsTypeDef",
    "ScanProvisionedProductsPaginateResponseTypeDef",
    "SearchProductsAsAdminPaginatePaginationConfigTypeDef",
    "SearchProductsAsAdminPaginateResponseProductViewDetailsProductViewSummaryTypeDef",
    "SearchProductsAsAdminPaginateResponseProductViewDetailsTypeDef",
    "SearchProductsAsAdminPaginateResponseTypeDef",
)


_ClientBatchAssociateServiceActionWithProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef = TypedDict(
    "_ClientBatchAssociateServiceActionWithProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef",
    {
        "ServiceActionId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)


class ClientBatchAssociateServiceActionWithProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef(
    _ClientBatchAssociateServiceActionWithProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef
):
    """
    Type definition for `ClientBatchAssociateServiceActionWithProvisioningArtifactResponse` `FailedServiceActionAssociations`

    An object containing information about the error, along with identifying information about
    the self-service action and its associations.

    - **ServiceActionId** *(string) --*

      The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .

    - **ProductId** *(string) --*

      The product identifier. For example, ``prod-abcdzk7xy33qa`` .

    - **ProvisioningArtifactId** *(string) --*

      The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .

    - **ErrorCode** *(string) --*

      The error code. Valid values are listed below.

    - **ErrorMessage** *(string) --*

      A text description of the error.
    """


_ClientBatchAssociateServiceActionWithProvisioningArtifactResponseTypeDef = TypedDict(
    "_ClientBatchAssociateServiceActionWithProvisioningArtifactResponseTypeDef",
    {
        "FailedServiceActionAssociations": List[
            ClientBatchAssociateServiceActionWithProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef
        ]
    },
    total=False,
)


class ClientBatchAssociateServiceActionWithProvisioningArtifactResponseTypeDef(
    _ClientBatchAssociateServiceActionWithProvisioningArtifactResponseTypeDef
):
    """
    Type definition for `ClientBatchAssociateServiceActionWithProvisioningArtifact` `Response`

    - **FailedServiceActionAssociations** *(list) --*

      An object that contains a list of errors, along with information to help you identify the
      self-service action.

      - *(dict) --*

        An object containing information about the error, along with identifying information about
        the self-service action and its associations.

        - **ServiceActionId** *(string) --*

          The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .

        - **ProductId** *(string) --*

          The product identifier. For example, ``prod-abcdzk7xy33qa`` .

        - **ProvisioningArtifactId** *(string) --*

          The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .

        - **ErrorCode** *(string) --*

          The error code. Valid values are listed below.

        - **ErrorMessage** *(string) --*

          A text description of the error.
    """


_ClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef = TypedDict(
    "_ClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef",
    {"ServiceActionId": str, "ProductId": str, "ProvisioningArtifactId": str},
)


class ClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef(
    _ClientBatchAssociateServiceActionWithProvisioningArtifactServiceActionAssociationsTypeDef
):
    """
    Type definition for `ClientBatchAssociateServiceActionWithProvisioningArtifact` `ServiceActionAssociations`

    A self-service action association consisting of the Action ID, the Product ID, and the
    Provisioning Artifact ID.

    - **ServiceActionId** *(string) --* **[REQUIRED]**

      The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .

    - **ProductId** *(string) --* **[REQUIRED]**

      The product identifier. For example, ``prod-abcdzk7xy33qa`` .

    - **ProvisioningArtifactId** *(string) --* **[REQUIRED]**

      The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .
    """


_ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef = TypedDict(
    "_ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef",
    {
        "ServiceActionId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)


class ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef(
    _ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef
):
    """
    Type definition for `ClientBatchDisassociateServiceActionFromProvisioningArtifactResponse` `FailedServiceActionAssociations`

    An object containing information about the error, along with identifying information about
    the self-service action and its associations.

    - **ServiceActionId** *(string) --*

      The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .

    - **ProductId** *(string) --*

      The product identifier. For example, ``prod-abcdzk7xy33qa`` .

    - **ProvisioningArtifactId** *(string) --*

      The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .

    - **ErrorCode** *(string) --*

      The error code. Valid values are listed below.

    - **ErrorMessage** *(string) --*

      A text description of the error.
    """


_ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseTypeDef = TypedDict(
    "_ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseTypeDef",
    {
        "FailedServiceActionAssociations": List[
            ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseFailedServiceActionAssociationsTypeDef
        ]
    },
    total=False,
)


class ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseTypeDef(
    _ClientBatchDisassociateServiceActionFromProvisioningArtifactResponseTypeDef
):
    """
    Type definition for `ClientBatchDisassociateServiceActionFromProvisioningArtifact` `Response`

    - **FailedServiceActionAssociations** *(list) --*

      An object that contains a list of errors, along with information to help you identify the
      self-service action.

      - *(dict) --*

        An object containing information about the error, along with identifying information about
        the self-service action and its associations.

        - **ServiceActionId** *(string) --*

          The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .

        - **ProductId** *(string) --*

          The product identifier. For example, ``prod-abcdzk7xy33qa`` .

        - **ProvisioningArtifactId** *(string) --*

          The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .

        - **ErrorCode** *(string) --*

          The error code. Valid values are listed below.

        - **ErrorMessage** *(string) --*

          A text description of the error.
    """


_ClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef = TypedDict(
    "_ClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef",
    {"ServiceActionId": str, "ProductId": str, "ProvisioningArtifactId": str},
)


class ClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef(
    _ClientBatchDisassociateServiceActionFromProvisioningArtifactServiceActionAssociationsTypeDef
):
    """
    Type definition for `ClientBatchDisassociateServiceActionFromProvisioningArtifact` `ServiceActionAssociations`

    A self-service action association consisting of the Action ID, the Product ID, and the
    Provisioning Artifact ID.

    - **ServiceActionId** *(string) --* **[REQUIRED]**

      The self-service action identifier. For example, ``act-fs7abcd89wxyz`` .

    - **ProductId** *(string) --* **[REQUIRED]**

      The product identifier. For example, ``prod-abcdzk7xy33qa`` .

    - **ProvisioningArtifactId** *(string) --* **[REQUIRED]**

      The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .
    """


_ClientCopyProductResponseTypeDef = TypedDict(
    "_ClientCopyProductResponseTypeDef", {"CopyProductToken": str}, total=False
)


class ClientCopyProductResponseTypeDef(_ClientCopyProductResponseTypeDef):
    """
    Type definition for `ClientCopyProduct` `Response`

    - **CopyProductToken** *(string) --*

      The token to use to track the progress of the operation.
    """


_ClientCreateConstraintResponseConstraintDetailTypeDef = TypedDict(
    "_ClientCreateConstraintResponseConstraintDetailTypeDef",
    {"ConstraintId": str, "Type": str, "Description": str, "Owner": str},
    total=False,
)


class ClientCreateConstraintResponseConstraintDetailTypeDef(
    _ClientCreateConstraintResponseConstraintDetailTypeDef
):
    """
    Type definition for `ClientCreateConstraintResponse` `ConstraintDetail`

    Information about the constraint.

    - **ConstraintId** *(string) --*

      The identifier of the constraint.

    - **Type** *(string) --*

      The type of constraint.

      * ``LAUNCH``

      * ``NOTIFICATION``

      * STACKSET

      * ``TEMPLATE``

    - **Description** *(string) --*

      The description of the constraint.

    - **Owner** *(string) --*

      The owner of the constraint.
    """


_ClientCreateConstraintResponseTypeDef = TypedDict(
    "_ClientCreateConstraintResponseTypeDef",
    {
        "ConstraintDetail": ClientCreateConstraintResponseConstraintDetailTypeDef,
        "ConstraintParameters": str,
        "Status": str,
    },
    total=False,
)


class ClientCreateConstraintResponseTypeDef(_ClientCreateConstraintResponseTypeDef):
    """
    Type definition for `ClientCreateConstraint` `Response`

    - **ConstraintDetail** *(dict) --*

      Information about the constraint.

      - **ConstraintId** *(string) --*

        The identifier of the constraint.

      - **Type** *(string) --*

        The type of constraint.

        * ``LAUNCH``

        * ``NOTIFICATION``

        * STACKSET

        * ``TEMPLATE``

      - **Description** *(string) --*

        The description of the constraint.

      - **Owner** *(string) --*

        The owner of the constraint.

    - **ConstraintParameters** *(string) --*

      The constraint parameters.

    - **Status** *(string) --*

      The status of the current request.
    """


_ClientCreatePortfolioResponsePortfolioDetailTypeDef = TypedDict(
    "_ClientCreatePortfolioResponsePortfolioDetailTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)


class ClientCreatePortfolioResponsePortfolioDetailTypeDef(
    _ClientCreatePortfolioResponsePortfolioDetailTypeDef
):
    """
    Type definition for `ClientCreatePortfolioResponse` `PortfolioDetail`

    Information about the portfolio.

    - **Id** *(string) --*

      The portfolio identifier.

    - **ARN** *(string) --*

      The ARN assigned to the portfolio.

    - **DisplayName** *(string) --*

      The name to use for display purposes.

    - **Description** *(string) --*

      The description of the portfolio.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **ProviderName** *(string) --*

      The name of the portfolio provider.
    """


_ClientCreatePortfolioResponseTagsTypeDef = TypedDict(
    "_ClientCreatePortfolioResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreatePortfolioResponseTagsTypeDef(
    _ClientCreatePortfolioResponseTagsTypeDef
):
    """
    Type definition for `ClientCreatePortfolioResponse` `Tags`

    Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
    created when provisioning a product.

    - **Key** *(string) --*

      The tag key.

    - **Value** *(string) --*

      The value for this key.
    """


_ClientCreatePortfolioResponseTypeDef = TypedDict(
    "_ClientCreatePortfolioResponseTypeDef",
    {
        "PortfolioDetail": ClientCreatePortfolioResponsePortfolioDetailTypeDef,
        "Tags": List[ClientCreatePortfolioResponseTagsTypeDef],
    },
    total=False,
)


class ClientCreatePortfolioResponseTypeDef(_ClientCreatePortfolioResponseTypeDef):
    """
    Type definition for `ClientCreatePortfolio` `Response`

    - **PortfolioDetail** *(dict) --*

      Information about the portfolio.

      - **Id** *(string) --*

        The portfolio identifier.

      - **ARN** *(string) --*

        The ARN assigned to the portfolio.

      - **DisplayName** *(string) --*

        The name to use for display purposes.

      - **Description** *(string) --*

        The description of the portfolio.

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

      - **ProviderName** *(string) --*

        The name of the portfolio provider.

    - **Tags** *(list) --*

      Information about the tags associated with the portfolio.

      - *(dict) --*

        Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
        created when provisioning a product.

        - **Key** *(string) --*

          The tag key.

        - **Value** *(string) --*

          The value for this key.
    """


_ClientCreatePortfolioShareOrganizationNodeTypeDef = TypedDict(
    "_ClientCreatePortfolioShareOrganizationNodeTypeDef",
    {"Type": str, "Value": str},
    total=False,
)


class ClientCreatePortfolioShareOrganizationNodeTypeDef(
    _ClientCreatePortfolioShareOrganizationNodeTypeDef
):
    """
    Type definition for `ClientCreatePortfolioShare` `OrganizationNode`

    The organization node to whom you are going to share. If ``OrganizationNode`` is passed in,
    ``PortfolioShare`` will be created for the node and its children (when applies), and a
    ``PortfolioShareToken`` will be returned in the output in order for the administrator to monitor
    the status of the ``PortfolioShare`` creation process.

    - **Type** *(string) --*

      The organization node type.

    - **Value** *(string) --*

      The identifier of the organization node.
    """


_ClientCreatePortfolioShareResponseTypeDef = TypedDict(
    "_ClientCreatePortfolioShareResponseTypeDef",
    {"PortfolioShareToken": str},
    total=False,
)


class ClientCreatePortfolioShareResponseTypeDef(
    _ClientCreatePortfolioShareResponseTypeDef
):
    """
    Type definition for `ClientCreatePortfolioShare` `Response`

    - **PortfolioShareToken** *(string) --*

      The portfolio share unique identifier. This will only be returned if portfolio is shared to
      an organization node.
    """


_ClientCreatePortfolioTagsTypeDef = TypedDict(
    "_ClientCreatePortfolioTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreatePortfolioTagsTypeDef(_ClientCreatePortfolioTagsTypeDef):
    """
    Type definition for `ClientCreatePortfolio` `Tags`

    Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
    created when provisioning a product.

    - **Key** *(string) --* **[REQUIRED]**

      The tag key.

    - **Value** *(string) --* **[REQUIRED]**

      The value for this key.
    """


_RequiredClientCreateProductProvisioningArtifactParametersTypeDef = TypedDict(
    "_RequiredClientCreateProductProvisioningArtifactParametersTypeDef",
    {"Info": Dict[str, str]},
)
_OptionalClientCreateProductProvisioningArtifactParametersTypeDef = TypedDict(
    "_OptionalClientCreateProductProvisioningArtifactParametersTypeDef",
    {"Name": str, "Description": str, "Type": str, "DisableTemplateValidation": bool},
    total=False,
)


class ClientCreateProductProvisioningArtifactParametersTypeDef(
    _RequiredClientCreateProductProvisioningArtifactParametersTypeDef,
    _OptionalClientCreateProductProvisioningArtifactParametersTypeDef,
):
    """
    Type definition for `ClientCreateProduct` `ProvisioningArtifactParameters`

    The configuration of the provisioning artifact.

    - **Name** *(string) --*

      The name of the provisioning artifact (for example, v1 v2beta). No spaces are allowed.

    - **Description** *(string) --*

      The description of the provisioning artifact, including how it differs from the previous
      provisioning artifact.

    - **Info** *(dict) --* **[REQUIRED]**

      The URL of the CloudFormation template in Amazon S3. Specify the URL in JSON format as follows:

       ``"LoadTemplateFromURL": "https://s3.amazonaws.com/cf-templates-ozkq9d3hgiq2-us-east-1/..."``

      - *(string) --*

        - *(string) --*

    - **Type** *(string) --*

      The type of provisioning artifact.

      * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template

      * ``MARKETPLACE_AMI`` - AWS Marketplace AMI

      * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources

    - **DisableTemplateValidation** *(boolean) --*

      If set to true, AWS Service Catalog stops validating the specified provisioning artifact even
      if it is invalid.
    """


_ClientCreateProductResponseProductViewDetailProductViewSummaryTypeDef = TypedDict(
    "_ClientCreateProductResponseProductViewDetailProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": str,
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ClientCreateProductResponseProductViewDetailProductViewSummaryTypeDef(
    _ClientCreateProductResponseProductViewDetailProductViewSummaryTypeDef
):
    """
    Type definition for `ClientCreateProductResponseProductViewDetail` `ProductViewSummary`

    Summary information about the product view.

    - **Id** *(string) --*

      The product view identifier.

    - **ProductId** *(string) --*

      The product identifier.

    - **Name** *(string) --*

      The name of the product.

    - **Owner** *(string) --*

      The owner of the product. Contact the product administrator for the significance of this
      value.

    - **ShortDescription** *(string) --*

      Short description of the product.

    - **Type** *(string) --*

      The product type. Contact the product administrator for the significance of this value.
      If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

    - **Distributor** *(string) --*

      The distributor of the product. Contact the product administrator for the significance of
      this value.

    - **HasDefaultPath** *(boolean) --*

      Indicates whether the product has a default path. If the product does not have a default
      path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is
      not required, and the output of  ProductViewSummary can be used directly with
      DescribeProvisioningParameters .

    - **SupportEmail** *(string) --*

      The email contact information to obtain support for this Product.

    - **SupportDescription** *(string) --*

      The description of the support for this Product.

    - **SupportUrl** *(string) --*

      The URL information to obtain support for this Product.
    """


_ClientCreateProductResponseProductViewDetailTypeDef = TypedDict(
    "_ClientCreateProductResponseProductViewDetailTypeDef",
    {
        "ProductViewSummary": ClientCreateProductResponseProductViewDetailProductViewSummaryTypeDef,
        "Status": str,
        "ProductARN": str,
        "CreatedTime": datetime,
    },
    total=False,
)


class ClientCreateProductResponseProductViewDetailTypeDef(
    _ClientCreateProductResponseProductViewDetailTypeDef
):
    """
    Type definition for `ClientCreateProductResponse` `ProductViewDetail`

    Information about the product view.

    - **ProductViewSummary** *(dict) --*

      Summary information about the product view.

      - **Id** *(string) --*

        The product view identifier.

      - **ProductId** *(string) --*

        The product identifier.

      - **Name** *(string) --*

        The name of the product.

      - **Owner** *(string) --*

        The owner of the product. Contact the product administrator for the significance of this
        value.

      - **ShortDescription** *(string) --*

        Short description of the product.

      - **Type** *(string) --*

        The product type. Contact the product administrator for the significance of this value.
        If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

      - **Distributor** *(string) --*

        The distributor of the product. Contact the product administrator for the significance of
        this value.

      - **HasDefaultPath** *(boolean) --*

        Indicates whether the product has a default path. If the product does not have a default
        path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is
        not required, and the output of  ProductViewSummary can be used directly with
        DescribeProvisioningParameters .

      - **SupportEmail** *(string) --*

        The email contact information to obtain support for this Product.

      - **SupportDescription** *(string) --*

        The description of the support for this Product.

      - **SupportUrl** *(string) --*

        The URL information to obtain support for this Product.

    - **Status** *(string) --*

      The status of the product.

      * ``AVAILABLE`` - The product is ready for use.

      * ``CREATING`` - Product creation has started; the product is not ready for use.

      * ``FAILED`` - An action failed.

    - **ProductARN** *(string) --*

      The ARN of the product.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.
    """


_ClientCreateProductResponseProvisioningArtifactDetailTypeDef = TypedDict(
    "_ClientCreateProductResponseProvisioningArtifactDetailTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Type": str,
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": str,
    },
    total=False,
)


class ClientCreateProductResponseProvisioningArtifactDetailTypeDef(
    _ClientCreateProductResponseProvisioningArtifactDetailTypeDef
):
    """
    Type definition for `ClientCreateProductResponse` `ProvisioningArtifactDetail`

    Information about the provisioning artifact.

    - **Id** *(string) --*

      The identifier of the provisioning artifact.

    - **Name** *(string) --*

      The name of the provisioning artifact.

    - **Description** *(string) --*

      The description of the provisioning artifact.

    - **Type** *(string) --*

      The type of provisioning artifact.

      * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template

      * ``MARKETPLACE_AMI`` - AWS Marketplace AMI

      * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **Active** *(boolean) --*

      Indicates whether the product version is active.

    - **Guidance** *(string) --*

      Information set by the administrator to provide guidance to end users about which
      provisioning artifacts to use.
    """


_ClientCreateProductResponseTagsTypeDef = TypedDict(
    "_ClientCreateProductResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateProductResponseTagsTypeDef(_ClientCreateProductResponseTagsTypeDef):
    """
    Type definition for `ClientCreateProductResponse` `Tags`

    Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
    created when provisioning a product.

    - **Key** *(string) --*

      The tag key.

    - **Value** *(string) --*

      The value for this key.
    """


_ClientCreateProductResponseTypeDef = TypedDict(
    "_ClientCreateProductResponseTypeDef",
    {
        "ProductViewDetail": ClientCreateProductResponseProductViewDetailTypeDef,
        "ProvisioningArtifactDetail": ClientCreateProductResponseProvisioningArtifactDetailTypeDef,
        "Tags": List[ClientCreateProductResponseTagsTypeDef],
    },
    total=False,
)


class ClientCreateProductResponseTypeDef(_ClientCreateProductResponseTypeDef):
    """
    Type definition for `ClientCreateProduct` `Response`

    - **ProductViewDetail** *(dict) --*

      Information about the product view.

      - **ProductViewSummary** *(dict) --*

        Summary information about the product view.

        - **Id** *(string) --*

          The product view identifier.

        - **ProductId** *(string) --*

          The product identifier.

        - **Name** *(string) --*

          The name of the product.

        - **Owner** *(string) --*

          The owner of the product. Contact the product administrator for the significance of this
          value.

        - **ShortDescription** *(string) --*

          Short description of the product.

        - **Type** *(string) --*

          The product type. Contact the product administrator for the significance of this value.
          If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

        - **Distributor** *(string) --*

          The distributor of the product. Contact the product administrator for the significance of
          this value.

        - **HasDefaultPath** *(boolean) --*

          Indicates whether the product has a default path. If the product does not have a default
          path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is
          not required, and the output of  ProductViewSummary can be used directly with
          DescribeProvisioningParameters .

        - **SupportEmail** *(string) --*

          The email contact information to obtain support for this Product.

        - **SupportDescription** *(string) --*

          The description of the support for this Product.

        - **SupportUrl** *(string) --*

          The URL information to obtain support for this Product.

      - **Status** *(string) --*

        The status of the product.

        * ``AVAILABLE`` - The product is ready for use.

        * ``CREATING`` - Product creation has started; the product is not ready for use.

        * ``FAILED`` - An action failed.

      - **ProductARN** *(string) --*

        The ARN of the product.

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

    - **ProvisioningArtifactDetail** *(dict) --*

      Information about the provisioning artifact.

      - **Id** *(string) --*

        The identifier of the provisioning artifact.

      - **Name** *(string) --*

        The name of the provisioning artifact.

      - **Description** *(string) --*

        The description of the provisioning artifact.

      - **Type** *(string) --*

        The type of provisioning artifact.

        * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template

        * ``MARKETPLACE_AMI`` - AWS Marketplace AMI

        * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

      - **Active** *(boolean) --*

        Indicates whether the product version is active.

      - **Guidance** *(string) --*

        Information set by the administrator to provide guidance to end users about which
        provisioning artifacts to use.

    - **Tags** *(list) --*

      Information about the tags associated with the product.

      - *(dict) --*

        Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
        created when provisioning a product.

        - **Key** *(string) --*

          The tag key.

        - **Value** *(string) --*

          The value for this key.
    """


_ClientCreateProductTagsTypeDef = TypedDict(
    "_ClientCreateProductTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateProductTagsTypeDef(_ClientCreateProductTagsTypeDef):
    """
    Type definition for `ClientCreateProduct` `Tags`

    Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
    created when provisioning a product.

    - **Key** *(string) --* **[REQUIRED]**

      The tag key.

    - **Value** *(string) --* **[REQUIRED]**

      The value for this key.
    """


_ClientCreateProvisionedProductPlanProvisioningParametersTypeDef = TypedDict(
    "_ClientCreateProvisionedProductPlanProvisioningParametersTypeDef",
    {"Key": str, "Value": str, "UsePreviousValue": bool},
    total=False,
)


class ClientCreateProvisionedProductPlanProvisioningParametersTypeDef(
    _ClientCreateProvisionedProductPlanProvisioningParametersTypeDef
):
    """
    Type definition for `ClientCreateProvisionedProductPlan` `ProvisioningParameters`

    The parameter key-value pair used to update a provisioned product.

    - **Key** *(string) --*

      The parameter key.

    - **Value** *(string) --*

      The parameter value.

    - **UsePreviousValue** *(boolean) --*

      If set to true, ``Value`` is ignored and the previous parameter value is kept.
    """


_ClientCreateProvisionedProductPlanResponseTypeDef = TypedDict(
    "_ClientCreateProvisionedProductPlanResponseTypeDef",
    {
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionedProductName": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)


class ClientCreateProvisionedProductPlanResponseTypeDef(
    _ClientCreateProvisionedProductPlanResponseTypeDef
):
    """
    Type definition for `ClientCreateProvisionedProductPlan` `Response`

    - **PlanName** *(string) --*

      The name of the plan.

    - **PlanId** *(string) --*

      The plan identifier.

    - **ProvisionProductId** *(string) --*

      The product identifier.

    - **ProvisionedProductName** *(string) --*

      The user-friendly name of the provisioned product.

    - **ProvisioningArtifactId** *(string) --*

      The identifier of the provisioning artifact.
    """


_ClientCreateProvisionedProductPlanTagsTypeDef = TypedDict(
    "_ClientCreateProvisionedProductPlanTagsTypeDef", {"Key": str, "Value": str}
)


class ClientCreateProvisionedProductPlanTagsTypeDef(
    _ClientCreateProvisionedProductPlanTagsTypeDef
):
    """
    Type definition for `ClientCreateProvisionedProductPlan` `Tags`

    Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
    created when provisioning a product.

    - **Key** *(string) --* **[REQUIRED]**

      The tag key.

    - **Value** *(string) --* **[REQUIRED]**

      The value for this key.
    """


_RequiredClientCreateProvisioningArtifactParametersTypeDef = TypedDict(
    "_RequiredClientCreateProvisioningArtifactParametersTypeDef",
    {"Info": Dict[str, str]},
)
_OptionalClientCreateProvisioningArtifactParametersTypeDef = TypedDict(
    "_OptionalClientCreateProvisioningArtifactParametersTypeDef",
    {"Name": str, "Description": str, "Type": str, "DisableTemplateValidation": bool},
    total=False,
)


class ClientCreateProvisioningArtifactParametersTypeDef(
    _RequiredClientCreateProvisioningArtifactParametersTypeDef,
    _OptionalClientCreateProvisioningArtifactParametersTypeDef,
):
    """
    Type definition for `ClientCreateProvisioningArtifact` `Parameters`

    The configuration for the provisioning artifact.

    - **Name** *(string) --*

      The name of the provisioning artifact (for example, v1 v2beta). No spaces are allowed.

    - **Description** *(string) --*

      The description of the provisioning artifact, including how it differs from the previous
      provisioning artifact.

    - **Info** *(dict) --* **[REQUIRED]**

      The URL of the CloudFormation template in Amazon S3. Specify the URL in JSON format as follows:

       ``"LoadTemplateFromURL": "https://s3.amazonaws.com/cf-templates-ozkq9d3hgiq2-us-east-1/..."``

      - *(string) --*

        - *(string) --*

    - **Type** *(string) --*

      The type of provisioning artifact.

      * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template

      * ``MARKETPLACE_AMI`` - AWS Marketplace AMI

      * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources

    - **DisableTemplateValidation** *(boolean) --*

      If set to true, AWS Service Catalog stops validating the specified provisioning artifact even
      if it is invalid.
    """


_ClientCreateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef = TypedDict(
    "_ClientCreateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Type": str,
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": str,
    },
    total=False,
)


class ClientCreateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef(
    _ClientCreateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef
):
    """
    Type definition for `ClientCreateProvisioningArtifactResponse` `ProvisioningArtifactDetail`

    Information about the provisioning artifact.

    - **Id** *(string) --*

      The identifier of the provisioning artifact.

    - **Name** *(string) --*

      The name of the provisioning artifact.

    - **Description** *(string) --*

      The description of the provisioning artifact.

    - **Type** *(string) --*

      The type of provisioning artifact.

      * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template

      * ``MARKETPLACE_AMI`` - AWS Marketplace AMI

      * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **Active** *(boolean) --*

      Indicates whether the product version is active.

    - **Guidance** *(string) --*

      Information set by the administrator to provide guidance to end users about which
      provisioning artifacts to use.
    """


_ClientCreateProvisioningArtifactResponseTypeDef = TypedDict(
    "_ClientCreateProvisioningArtifactResponseTypeDef",
    {
        "ProvisioningArtifactDetail": ClientCreateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef,
        "Info": Dict[str, str],
        "Status": str,
    },
    total=False,
)


class ClientCreateProvisioningArtifactResponseTypeDef(
    _ClientCreateProvisioningArtifactResponseTypeDef
):
    """
    Type definition for `ClientCreateProvisioningArtifact` `Response`

    - **ProvisioningArtifactDetail** *(dict) --*

      Information about the provisioning artifact.

      - **Id** *(string) --*

        The identifier of the provisioning artifact.

      - **Name** *(string) --*

        The name of the provisioning artifact.

      - **Description** *(string) --*

        The description of the provisioning artifact.

      - **Type** *(string) --*

        The type of provisioning artifact.

        * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template

        * ``MARKETPLACE_AMI`` - AWS Marketplace AMI

        * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

      - **Active** *(boolean) --*

        Indicates whether the product version is active.

      - **Guidance** *(string) --*

        Information set by the administrator to provide guidance to end users about which
        provisioning artifacts to use.

    - **Info** *(dict) --*

      The URL of the CloudFormation template in Amazon S3, in JSON format.

      - *(string) --*

        - *(string) --*

    - **Status** *(string) --*

      The status of the current request.
    """


_ClientCreateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef = TypedDict(
    "_ClientCreateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)


class ClientCreateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef(
    _ClientCreateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef
):
    """
    Type definition for `ClientCreateServiceActionResponseServiceActionDetail` `ServiceActionSummary`

    Summary information about the self-service action.

    - **Id** *(string) --*

      The self-service action identifier.

    - **Name** *(string) --*

      The self-service action name.

    - **Description** *(string) --*

      The self-service action description.

    - **DefinitionType** *(string) --*

      The self-service action definition type. For example, ``SSM_AUTOMATION`` .
    """


_ClientCreateServiceActionResponseServiceActionDetailTypeDef = TypedDict(
    "_ClientCreateServiceActionResponseServiceActionDetailTypeDef",
    {
        "ServiceActionSummary": ClientCreateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef,
        "Definition": Dict[str, str],
    },
    total=False,
)


class ClientCreateServiceActionResponseServiceActionDetailTypeDef(
    _ClientCreateServiceActionResponseServiceActionDetailTypeDef
):
    """
    Type definition for `ClientCreateServiceActionResponse` `ServiceActionDetail`

    An object containing information about the self-service action.

    - **ServiceActionSummary** *(dict) --*

      Summary information about the self-service action.

      - **Id** *(string) --*

        The self-service action identifier.

      - **Name** *(string) --*

        The self-service action name.

      - **Description** *(string) --*

        The self-service action description.

      - **DefinitionType** *(string) --*

        The self-service action definition type. For example, ``SSM_AUTOMATION`` .

    - **Definition** *(dict) --*

      A map that defines the self-service action.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateServiceActionResponseTypeDef = TypedDict(
    "_ClientCreateServiceActionResponseTypeDef",
    {
        "ServiceActionDetail": ClientCreateServiceActionResponseServiceActionDetailTypeDef
    },
    total=False,
)


class ClientCreateServiceActionResponseTypeDef(
    _ClientCreateServiceActionResponseTypeDef
):
    """
    Type definition for `ClientCreateServiceAction` `Response`

    - **ServiceActionDetail** *(dict) --*

      An object containing information about the self-service action.

      - **ServiceActionSummary** *(dict) --*

        Summary information about the self-service action.

        - **Id** *(string) --*

          The self-service action identifier.

        - **Name** *(string) --*

          The self-service action name.

        - **Description** *(string) --*

          The self-service action description.

        - **DefinitionType** *(string) --*

          The self-service action definition type. For example, ``SSM_AUTOMATION`` .

      - **Definition** *(dict) --*

        A map that defines the self-service action.

        - *(string) --*

          - *(string) --*
    """


_ClientCreateTagOptionResponseTagOptionDetailTypeDef = TypedDict(
    "_ClientCreateTagOptionResponseTagOptionDetailTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)


class ClientCreateTagOptionResponseTagOptionDetailTypeDef(
    _ClientCreateTagOptionResponseTagOptionDetailTypeDef
):
    """
    Type definition for `ClientCreateTagOptionResponse` `TagOptionDetail`

    Information about the TagOption.

    - **Key** *(string) --*

      The TagOption key.

    - **Value** *(string) --*

      The TagOption value.

    - **Active** *(boolean) --*

      The TagOption active state.

    - **Id** *(string) --*

      The TagOption identifier.
    """


_ClientCreateTagOptionResponseTypeDef = TypedDict(
    "_ClientCreateTagOptionResponseTypeDef",
    {"TagOptionDetail": ClientCreateTagOptionResponseTagOptionDetailTypeDef},
    total=False,
)


class ClientCreateTagOptionResponseTypeDef(_ClientCreateTagOptionResponseTypeDef):
    """
    Type definition for `ClientCreateTagOption` `Response`

    - **TagOptionDetail** *(dict) --*

      Information about the TagOption.

      - **Key** *(string) --*

        The TagOption key.

      - **Value** *(string) --*

        The TagOption value.

      - **Active** *(boolean) --*

        The TagOption active state.

      - **Id** *(string) --*

        The TagOption identifier.
    """


_ClientDeletePortfolioShareOrganizationNodeTypeDef = TypedDict(
    "_ClientDeletePortfolioShareOrganizationNodeTypeDef",
    {"Type": str, "Value": str},
    total=False,
)


class ClientDeletePortfolioShareOrganizationNodeTypeDef(
    _ClientDeletePortfolioShareOrganizationNodeTypeDef
):
    """
    Type definition for `ClientDeletePortfolioShare` `OrganizationNode`

    The organization node to whom you are going to stop sharing.

    - **Type** *(string) --*

      The organization node type.

    - **Value** *(string) --*

      The identifier of the organization node.
    """


_ClientDeletePortfolioShareResponseTypeDef = TypedDict(
    "_ClientDeletePortfolioShareResponseTypeDef",
    {"PortfolioShareToken": str},
    total=False,
)


class ClientDeletePortfolioShareResponseTypeDef(
    _ClientDeletePortfolioShareResponseTypeDef
):
    """
    Type definition for `ClientDeletePortfolioShare` `Response`

    - **PortfolioShareToken** *(string) --*

      The portfolio share unique identifier. This will only be returned if delete is made to an
      organization node.
    """


_ClientDescribeConstraintResponseConstraintDetailTypeDef = TypedDict(
    "_ClientDescribeConstraintResponseConstraintDetailTypeDef",
    {"ConstraintId": str, "Type": str, "Description": str, "Owner": str},
    total=False,
)


class ClientDescribeConstraintResponseConstraintDetailTypeDef(
    _ClientDescribeConstraintResponseConstraintDetailTypeDef
):
    """
    Type definition for `ClientDescribeConstraintResponse` `ConstraintDetail`

    Information about the constraint.

    - **ConstraintId** *(string) --*

      The identifier of the constraint.

    - **Type** *(string) --*

      The type of constraint.

      * ``LAUNCH``

      * ``NOTIFICATION``

      * STACKSET

      * ``TEMPLATE``

    - **Description** *(string) --*

      The description of the constraint.

    - **Owner** *(string) --*

      The owner of the constraint.
    """


_ClientDescribeConstraintResponseTypeDef = TypedDict(
    "_ClientDescribeConstraintResponseTypeDef",
    {
        "ConstraintDetail": ClientDescribeConstraintResponseConstraintDetailTypeDef,
        "ConstraintParameters": str,
        "Status": str,
    },
    total=False,
)


class ClientDescribeConstraintResponseTypeDef(_ClientDescribeConstraintResponseTypeDef):
    """
    Type definition for `ClientDescribeConstraint` `Response`

    - **ConstraintDetail** *(dict) --*

      Information about the constraint.

      - **ConstraintId** *(string) --*

        The identifier of the constraint.

      - **Type** *(string) --*

        The type of constraint.

        * ``LAUNCH``

        * ``NOTIFICATION``

        * STACKSET

        * ``TEMPLATE``

      - **Description** *(string) --*

        The description of the constraint.

      - **Owner** *(string) --*

        The owner of the constraint.

    - **ConstraintParameters** *(string) --*

      The constraint parameters.

    - **Status** *(string) --*

      The status of the current request.
    """


_ClientDescribeCopyProductStatusResponseTypeDef = TypedDict(
    "_ClientDescribeCopyProductStatusResponseTypeDef",
    {"CopyProductStatus": str, "TargetProductId": str, "StatusDetail": str},
    total=False,
)


class ClientDescribeCopyProductStatusResponseTypeDef(
    _ClientDescribeCopyProductStatusResponseTypeDef
):
    """
    Type definition for `ClientDescribeCopyProductStatus` `Response`

    - **CopyProductStatus** *(string) --*

      The status of the copy product operation.

    - **TargetProductId** *(string) --*

      The identifier of the copied product.

    - **StatusDetail** *(string) --*

      The status message.
    """


_ClientDescribePortfolioResponseBudgetsTypeDef = TypedDict(
    "_ClientDescribePortfolioResponseBudgetsTypeDef", {"BudgetName": str}, total=False
)


class ClientDescribePortfolioResponseBudgetsTypeDef(
    _ClientDescribePortfolioResponseBudgetsTypeDef
):
    """
    Type definition for `ClientDescribePortfolioResponse` `Budgets`

    Information about a budget.

    - **BudgetName** *(string) --*

      Name of the associated budget.
    """


_ClientDescribePortfolioResponsePortfolioDetailTypeDef = TypedDict(
    "_ClientDescribePortfolioResponsePortfolioDetailTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)


class ClientDescribePortfolioResponsePortfolioDetailTypeDef(
    _ClientDescribePortfolioResponsePortfolioDetailTypeDef
):
    """
    Type definition for `ClientDescribePortfolioResponse` `PortfolioDetail`

    Information about the portfolio.

    - **Id** *(string) --*

      The portfolio identifier.

    - **ARN** *(string) --*

      The ARN assigned to the portfolio.

    - **DisplayName** *(string) --*

      The name to use for display purposes.

    - **Description** *(string) --*

      The description of the portfolio.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **ProviderName** *(string) --*

      The name of the portfolio provider.
    """


_ClientDescribePortfolioResponseTagOptionsTypeDef = TypedDict(
    "_ClientDescribePortfolioResponseTagOptionsTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)


class ClientDescribePortfolioResponseTagOptionsTypeDef(
    _ClientDescribePortfolioResponseTagOptionsTypeDef
):
    """
    Type definition for `ClientDescribePortfolioResponse` `TagOptions`

    Information about a TagOption.

    - **Key** *(string) --*

      The TagOption key.

    - **Value** *(string) --*

      The TagOption value.

    - **Active** *(boolean) --*

      The TagOption active state.

    - **Id** *(string) --*

      The TagOption identifier.
    """


_ClientDescribePortfolioResponseTagsTypeDef = TypedDict(
    "_ClientDescribePortfolioResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribePortfolioResponseTagsTypeDef(
    _ClientDescribePortfolioResponseTagsTypeDef
):
    """
    Type definition for `ClientDescribePortfolioResponse` `Tags`

    Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
    created when provisioning a product.

    - **Key** *(string) --*

      The tag key.

    - **Value** *(string) --*

      The value for this key.
    """


_ClientDescribePortfolioResponseTypeDef = TypedDict(
    "_ClientDescribePortfolioResponseTypeDef",
    {
        "PortfolioDetail": ClientDescribePortfolioResponsePortfolioDetailTypeDef,
        "Tags": List[ClientDescribePortfolioResponseTagsTypeDef],
        "TagOptions": List[ClientDescribePortfolioResponseTagOptionsTypeDef],
        "Budgets": List[ClientDescribePortfolioResponseBudgetsTypeDef],
    },
    total=False,
)


class ClientDescribePortfolioResponseTypeDef(_ClientDescribePortfolioResponseTypeDef):
    """
    Type definition for `ClientDescribePortfolio` `Response`

    - **PortfolioDetail** *(dict) --*

      Information about the portfolio.

      - **Id** *(string) --*

        The portfolio identifier.

      - **ARN** *(string) --*

        The ARN assigned to the portfolio.

      - **DisplayName** *(string) --*

        The name to use for display purposes.

      - **Description** *(string) --*

        The description of the portfolio.

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

      - **ProviderName** *(string) --*

        The name of the portfolio provider.

    - **Tags** *(list) --*

      Information about the tags associated with the portfolio.

      - *(dict) --*

        Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
        created when provisioning a product.

        - **Key** *(string) --*

          The tag key.

        - **Value** *(string) --*

          The value for this key.

    - **TagOptions** *(list) --*

      Information about the TagOptions associated with the portfolio.

      - *(dict) --*

        Information about a TagOption.

        - **Key** *(string) --*

          The TagOption key.

        - **Value** *(string) --*

          The TagOption value.

        - **Active** *(boolean) --*

          The TagOption active state.

        - **Id** *(string) --*

          The TagOption identifier.

    - **Budgets** *(list) --*

      Information about the associated budgets.

      - *(dict) --*

        Information about a budget.

        - **BudgetName** *(string) --*

          Name of the associated budget.
    """


_ClientDescribePortfolioShareStatusResponseShareDetailsShareErrorsTypeDef = TypedDict(
    "_ClientDescribePortfolioShareStatusResponseShareDetailsShareErrorsTypeDef",
    {"Accounts": List[str], "Message": str, "Error": str},
    total=False,
)


class ClientDescribePortfolioShareStatusResponseShareDetailsShareErrorsTypeDef(
    _ClientDescribePortfolioShareStatusResponseShareDetailsShareErrorsTypeDef
):
    """
    Type definition for `ClientDescribePortfolioShareStatusResponseShareDetails` `ShareErrors`

    Errors that occurred during the portfolio share operation.

    - **Accounts** *(list) --*

      List of accounts impacted by the error.

      - *(string) --*

    - **Message** *(string) --*

      Information about the error.

    - **Error** *(string) --*

      Error type that happened when processing the operation.
    """


_ClientDescribePortfolioShareStatusResponseShareDetailsTypeDef = TypedDict(
    "_ClientDescribePortfolioShareStatusResponseShareDetailsTypeDef",
    {
        "SuccessfulShares": List[str],
        "ShareErrors": List[
            ClientDescribePortfolioShareStatusResponseShareDetailsShareErrorsTypeDef
        ],
    },
    total=False,
)


class ClientDescribePortfolioShareStatusResponseShareDetailsTypeDef(
    _ClientDescribePortfolioShareStatusResponseShareDetailsTypeDef
):
    """
    Type definition for `ClientDescribePortfolioShareStatusResponse` `ShareDetails`

    Information about the portfolio share operation.

    - **SuccessfulShares** *(list) --*

      List of accounts for whom the operation succeeded.

      - *(string) --*

    - **ShareErrors** *(list) --*

      List of errors.

      - *(dict) --*

        Errors that occurred during the portfolio share operation.

        - **Accounts** *(list) --*

          List of accounts impacted by the error.

          - *(string) --*

        - **Message** *(string) --*

          Information about the error.

        - **Error** *(string) --*

          Error type that happened when processing the operation.
    """


_ClientDescribePortfolioShareStatusResponseTypeDef = TypedDict(
    "_ClientDescribePortfolioShareStatusResponseTypeDef",
    {
        "PortfolioShareToken": str,
        "PortfolioId": str,
        "OrganizationNodeValue": str,
        "Status": str,
        "ShareDetails": ClientDescribePortfolioShareStatusResponseShareDetailsTypeDef,
    },
    total=False,
)


class ClientDescribePortfolioShareStatusResponseTypeDef(
    _ClientDescribePortfolioShareStatusResponseTypeDef
):
    """
    Type definition for `ClientDescribePortfolioShareStatus` `Response`

    - **PortfolioShareToken** *(string) --*

      The token for the portfolio share operation. For example, ``share-6v24abcdefghi`` .

    - **PortfolioId** *(string) --*

      The portfolio identifier.

    - **OrganizationNodeValue** *(string) --*

      Organization node identifier. It can be either account id, organizational unit id or
      organization id.

    - **Status** *(string) --*

      Status of the portfolio share operation.

    - **ShareDetails** *(dict) --*

      Information about the portfolio share operation.

      - **SuccessfulShares** *(list) --*

        List of accounts for whom the operation succeeded.

        - *(string) --*

      - **ShareErrors** *(list) --*

        List of errors.

        - *(dict) --*

          Errors that occurred during the portfolio share operation.

          - **Accounts** *(list) --*

            List of accounts impacted by the error.

            - *(string) --*

          - **Message** *(string) --*

            Information about the error.

          - **Error** *(string) --*

            Error type that happened when processing the operation.
    """


_ClientDescribeProductAsAdminResponseBudgetsTypeDef = TypedDict(
    "_ClientDescribeProductAsAdminResponseBudgetsTypeDef",
    {"BudgetName": str},
    total=False,
)


class ClientDescribeProductAsAdminResponseBudgetsTypeDef(
    _ClientDescribeProductAsAdminResponseBudgetsTypeDef
):
    """
    Type definition for `ClientDescribeProductAsAdminResponse` `Budgets`

    Information about a budget.

    - **BudgetName** *(string) --*

      Name of the associated budget.
    """


_ClientDescribeProductAsAdminResponseProductViewDetailProductViewSummaryTypeDef = TypedDict(
    "_ClientDescribeProductAsAdminResponseProductViewDetailProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": str,
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ClientDescribeProductAsAdminResponseProductViewDetailProductViewSummaryTypeDef(
    _ClientDescribeProductAsAdminResponseProductViewDetailProductViewSummaryTypeDef
):
    """
    Type definition for `ClientDescribeProductAsAdminResponseProductViewDetail` `ProductViewSummary`

    Summary information about the product view.

    - **Id** *(string) --*

      The product view identifier.

    - **ProductId** *(string) --*

      The product identifier.

    - **Name** *(string) --*

      The name of the product.

    - **Owner** *(string) --*

      The owner of the product. Contact the product administrator for the significance of this
      value.

    - **ShortDescription** *(string) --*

      Short description of the product.

    - **Type** *(string) --*

      The product type. Contact the product administrator for the significance of this value.
      If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

    - **Distributor** *(string) --*

      The distributor of the product. Contact the product administrator for the significance of
      this value.

    - **HasDefaultPath** *(boolean) --*

      Indicates whether the product has a default path. If the product does not have a default
      path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is
      not required, and the output of  ProductViewSummary can be used directly with
      DescribeProvisioningParameters .

    - **SupportEmail** *(string) --*

      The email contact information to obtain support for this Product.

    - **SupportDescription** *(string) --*

      The description of the support for this Product.

    - **SupportUrl** *(string) --*

      The URL information to obtain support for this Product.
    """


_ClientDescribeProductAsAdminResponseProductViewDetailTypeDef = TypedDict(
    "_ClientDescribeProductAsAdminResponseProductViewDetailTypeDef",
    {
        "ProductViewSummary": ClientDescribeProductAsAdminResponseProductViewDetailProductViewSummaryTypeDef,
        "Status": str,
        "ProductARN": str,
        "CreatedTime": datetime,
    },
    total=False,
)


class ClientDescribeProductAsAdminResponseProductViewDetailTypeDef(
    _ClientDescribeProductAsAdminResponseProductViewDetailTypeDef
):
    """
    Type definition for `ClientDescribeProductAsAdminResponse` `ProductViewDetail`

    Information about the product view.

    - **ProductViewSummary** *(dict) --*

      Summary information about the product view.

      - **Id** *(string) --*

        The product view identifier.

      - **ProductId** *(string) --*

        The product identifier.

      - **Name** *(string) --*

        The name of the product.

      - **Owner** *(string) --*

        The owner of the product. Contact the product administrator for the significance of this
        value.

      - **ShortDescription** *(string) --*

        Short description of the product.

      - **Type** *(string) --*

        The product type. Contact the product administrator for the significance of this value.
        If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

      - **Distributor** *(string) --*

        The distributor of the product. Contact the product administrator for the significance of
        this value.

      - **HasDefaultPath** *(boolean) --*

        Indicates whether the product has a default path. If the product does not have a default
        path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is
        not required, and the output of  ProductViewSummary can be used directly with
        DescribeProvisioningParameters .

      - **SupportEmail** *(string) --*

        The email contact information to obtain support for this Product.

      - **SupportDescription** *(string) --*

        The description of the support for this Product.

      - **SupportUrl** *(string) --*

        The URL information to obtain support for this Product.

    - **Status** *(string) --*

      The status of the product.

      * ``AVAILABLE`` - The product is ready for use.

      * ``CREATING`` - Product creation has started; the product is not ready for use.

      * ``FAILED`` - An action failed.

    - **ProductARN** *(string) --*

      The ARN of the product.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.
    """


_ClientDescribeProductAsAdminResponseProvisioningArtifactSummariesTypeDef = TypedDict(
    "_ClientDescribeProductAsAdminResponseProvisioningArtifactSummariesTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProvisioningArtifactMetadata": Dict[str, str],
    },
    total=False,
)


class ClientDescribeProductAsAdminResponseProvisioningArtifactSummariesTypeDef(
    _ClientDescribeProductAsAdminResponseProvisioningArtifactSummariesTypeDef
):
    """
    Type definition for `ClientDescribeProductAsAdminResponse` `ProvisioningArtifactSummaries`

    Summary information about a provisioning artifact (also known as a version) for a product.

    - **Id** *(string) --*

      The identifier of the provisioning artifact.

    - **Name** *(string) --*

      The name of the provisioning artifact.

    - **Description** *(string) --*

      The description of the provisioning artifact.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **ProvisioningArtifactMetadata** *(dict) --*

      The metadata for the provisioning artifact. This is used with AWS Marketplace products.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeProductAsAdminResponseTagOptionsTypeDef = TypedDict(
    "_ClientDescribeProductAsAdminResponseTagOptionsTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)


class ClientDescribeProductAsAdminResponseTagOptionsTypeDef(
    _ClientDescribeProductAsAdminResponseTagOptionsTypeDef
):
    """
    Type definition for `ClientDescribeProductAsAdminResponse` `TagOptions`

    Information about a TagOption.

    - **Key** *(string) --*

      The TagOption key.

    - **Value** *(string) --*

      The TagOption value.

    - **Active** *(boolean) --*

      The TagOption active state.

    - **Id** *(string) --*

      The TagOption identifier.
    """


_ClientDescribeProductAsAdminResponseTagsTypeDef = TypedDict(
    "_ClientDescribeProductAsAdminResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeProductAsAdminResponseTagsTypeDef(
    _ClientDescribeProductAsAdminResponseTagsTypeDef
):
    """
    Type definition for `ClientDescribeProductAsAdminResponse` `Tags`

    Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
    created when provisioning a product.

    - **Key** *(string) --*

      The tag key.

    - **Value** *(string) --*

      The value for this key.
    """


_ClientDescribeProductAsAdminResponseTypeDef = TypedDict(
    "_ClientDescribeProductAsAdminResponseTypeDef",
    {
        "ProductViewDetail": ClientDescribeProductAsAdminResponseProductViewDetailTypeDef,
        "ProvisioningArtifactSummaries": List[
            ClientDescribeProductAsAdminResponseProvisioningArtifactSummariesTypeDef
        ],
        "Tags": List[ClientDescribeProductAsAdminResponseTagsTypeDef],
        "TagOptions": List[ClientDescribeProductAsAdminResponseTagOptionsTypeDef],
        "Budgets": List[ClientDescribeProductAsAdminResponseBudgetsTypeDef],
    },
    total=False,
)


class ClientDescribeProductAsAdminResponseTypeDef(
    _ClientDescribeProductAsAdminResponseTypeDef
):
    """
    Type definition for `ClientDescribeProductAsAdmin` `Response`

    - **ProductViewDetail** *(dict) --*

      Information about the product view.

      - **ProductViewSummary** *(dict) --*

        Summary information about the product view.

        - **Id** *(string) --*

          The product view identifier.

        - **ProductId** *(string) --*

          The product identifier.

        - **Name** *(string) --*

          The name of the product.

        - **Owner** *(string) --*

          The owner of the product. Contact the product administrator for the significance of this
          value.

        - **ShortDescription** *(string) --*

          Short description of the product.

        - **Type** *(string) --*

          The product type. Contact the product administrator for the significance of this value.
          If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

        - **Distributor** *(string) --*

          The distributor of the product. Contact the product administrator for the significance of
          this value.

        - **HasDefaultPath** *(boolean) --*

          Indicates whether the product has a default path. If the product does not have a default
          path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is
          not required, and the output of  ProductViewSummary can be used directly with
          DescribeProvisioningParameters .

        - **SupportEmail** *(string) --*

          The email contact information to obtain support for this Product.

        - **SupportDescription** *(string) --*

          The description of the support for this Product.

        - **SupportUrl** *(string) --*

          The URL information to obtain support for this Product.

      - **Status** *(string) --*

        The status of the product.

        * ``AVAILABLE`` - The product is ready for use.

        * ``CREATING`` - Product creation has started; the product is not ready for use.

        * ``FAILED`` - An action failed.

      - **ProductARN** *(string) --*

        The ARN of the product.

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

    - **ProvisioningArtifactSummaries** *(list) --*

      Information about the provisioning artifacts (also known as versions) for the specified
      product.

      - *(dict) --*

        Summary information about a provisioning artifact (also known as a version) for a product.

        - **Id** *(string) --*

          The identifier of the provisioning artifact.

        - **Name** *(string) --*

          The name of the provisioning artifact.

        - **Description** *(string) --*

          The description of the provisioning artifact.

        - **CreatedTime** *(datetime) --*

          The UTC time stamp of the creation time.

        - **ProvisioningArtifactMetadata** *(dict) --*

          The metadata for the provisioning artifact. This is used with AWS Marketplace products.

          - *(string) --*

            - *(string) --*

    - **Tags** *(list) --*

      Information about the tags associated with the product.

      - *(dict) --*

        Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
        created when provisioning a product.

        - **Key** *(string) --*

          The tag key.

        - **Value** *(string) --*

          The value for this key.

    - **TagOptions** *(list) --*

      Information about the TagOptions associated with the product.

      - *(dict) --*

        Information about a TagOption.

        - **Key** *(string) --*

          The TagOption key.

        - **Value** *(string) --*

          The TagOption value.

        - **Active** *(boolean) --*

          The TagOption active state.

        - **Id** *(string) --*

          The TagOption identifier.

    - **Budgets** *(list) --*

      Information about the associated budgets.

      - *(dict) --*

        Information about a budget.

        - **BudgetName** *(string) --*

          Name of the associated budget.
    """


_ClientDescribeProductResponseBudgetsTypeDef = TypedDict(
    "_ClientDescribeProductResponseBudgetsTypeDef", {"BudgetName": str}, total=False
)


class ClientDescribeProductResponseBudgetsTypeDef(
    _ClientDescribeProductResponseBudgetsTypeDef
):
    """
    Type definition for `ClientDescribeProductResponse` `Budgets`

    Information about a budget.

    - **BudgetName** *(string) --*

      Name of the associated budget.
    """


_ClientDescribeProductResponseProductViewSummaryTypeDef = TypedDict(
    "_ClientDescribeProductResponseProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": str,
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ClientDescribeProductResponseProductViewSummaryTypeDef(
    _ClientDescribeProductResponseProductViewSummaryTypeDef
):
    """
    Type definition for `ClientDescribeProductResponse` `ProductViewSummary`

    Summary information about the product view.

    - **Id** *(string) --*

      The product view identifier.

    - **ProductId** *(string) --*

      The product identifier.

    - **Name** *(string) --*

      The name of the product.

    - **Owner** *(string) --*

      The owner of the product. Contact the product administrator for the significance of this
      value.

    - **ShortDescription** *(string) --*

      Short description of the product.

    - **Type** *(string) --*

      The product type. Contact the product administrator for the significance of this value. If
      this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

    - **Distributor** *(string) --*

      The distributor of the product. Contact the product administrator for the significance of
      this value.

    - **HasDefaultPath** *(boolean) --*

      Indicates whether the product has a default path. If the product does not have a default
      path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is
      not required, and the output of  ProductViewSummary can be used directly with
      DescribeProvisioningParameters .

    - **SupportEmail** *(string) --*

      The email contact information to obtain support for this Product.

    - **SupportDescription** *(string) --*

      The description of the support for this Product.

    - **SupportUrl** *(string) --*

      The URL information to obtain support for this Product.
    """


_ClientDescribeProductResponseProvisioningArtifactsTypeDef = TypedDict(
    "_ClientDescribeProductResponseProvisioningArtifactsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "Guidance": str,
    },
    total=False,
)


class ClientDescribeProductResponseProvisioningArtifactsTypeDef(
    _ClientDescribeProductResponseProvisioningArtifactsTypeDef
):
    """
    Type definition for `ClientDescribeProductResponse` `ProvisioningArtifacts`

    Information about a provisioning artifact. A provisioning artifact is also known as a
    product version.

    - **Id** *(string) --*

      The identifier of the provisioning artifact.

    - **Name** *(string) --*

      The name of the provisioning artifact.

    - **Description** *(string) --*

      The description of the provisioning artifact.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **Guidance** *(string) --*

      Information set by the administrator to provide guidance to end users about which
      provisioning artifacts to use.
    """


_ClientDescribeProductResponseTypeDef = TypedDict(
    "_ClientDescribeProductResponseTypeDef",
    {
        "ProductViewSummary": ClientDescribeProductResponseProductViewSummaryTypeDef,
        "ProvisioningArtifacts": List[
            ClientDescribeProductResponseProvisioningArtifactsTypeDef
        ],
        "Budgets": List[ClientDescribeProductResponseBudgetsTypeDef],
    },
    total=False,
)


class ClientDescribeProductResponseTypeDef(_ClientDescribeProductResponseTypeDef):
    """
    Type definition for `ClientDescribeProduct` `Response`

    - **ProductViewSummary** *(dict) --*

      Summary information about the product view.

      - **Id** *(string) --*

        The product view identifier.

      - **ProductId** *(string) --*

        The product identifier.

      - **Name** *(string) --*

        The name of the product.

      - **Owner** *(string) --*

        The owner of the product. Contact the product administrator for the significance of this
        value.

      - **ShortDescription** *(string) --*

        Short description of the product.

      - **Type** *(string) --*

        The product type. Contact the product administrator for the significance of this value. If
        this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

      - **Distributor** *(string) --*

        The distributor of the product. Contact the product administrator for the significance of
        this value.

      - **HasDefaultPath** *(boolean) --*

        Indicates whether the product has a default path. If the product does not have a default
        path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is
        not required, and the output of  ProductViewSummary can be used directly with
        DescribeProvisioningParameters .

      - **SupportEmail** *(string) --*

        The email contact information to obtain support for this Product.

      - **SupportDescription** *(string) --*

        The description of the support for this Product.

      - **SupportUrl** *(string) --*

        The URL information to obtain support for this Product.

    - **ProvisioningArtifacts** *(list) --*

      Information about the provisioning artifacts for the specified product.

      - *(dict) --*

        Information about a provisioning artifact. A provisioning artifact is also known as a
        product version.

        - **Id** *(string) --*

          The identifier of the provisioning artifact.

        - **Name** *(string) --*

          The name of the provisioning artifact.

        - **Description** *(string) --*

          The description of the provisioning artifact.

        - **CreatedTime** *(datetime) --*

          The UTC time stamp of the creation time.

        - **Guidance** *(string) --*

          Information set by the administrator to provide guidance to end users about which
          provisioning artifacts to use.

    - **Budgets** *(list) --*

      Information about the associated budgets.

      - *(dict) --*

        Information about a budget.

        - **BudgetName** *(string) --*

          Name of the associated budget.
    """


_ClientDescribeProductViewResponseProductViewSummaryTypeDef = TypedDict(
    "_ClientDescribeProductViewResponseProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": str,
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ClientDescribeProductViewResponseProductViewSummaryTypeDef(
    _ClientDescribeProductViewResponseProductViewSummaryTypeDef
):
    """
    Type definition for `ClientDescribeProductViewResponse` `ProductViewSummary`

    Summary information about the product.

    - **Id** *(string) --*

      The product view identifier.

    - **ProductId** *(string) --*

      The product identifier.

    - **Name** *(string) --*

      The name of the product.

    - **Owner** *(string) --*

      The owner of the product. Contact the product administrator for the significance of this
      value.

    - **ShortDescription** *(string) --*

      Short description of the product.

    - **Type** *(string) --*

      The product type. Contact the product administrator for the significance of this value. If
      this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

    - **Distributor** *(string) --*

      The distributor of the product. Contact the product administrator for the significance of
      this value.

    - **HasDefaultPath** *(boolean) --*

      Indicates whether the product has a default path. If the product does not have a default
      path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is
      not required, and the output of  ProductViewSummary can be used directly with
      DescribeProvisioningParameters .

    - **SupportEmail** *(string) --*

      The email contact information to obtain support for this Product.

    - **SupportDescription** *(string) --*

      The description of the support for this Product.

    - **SupportUrl** *(string) --*

      The URL information to obtain support for this Product.
    """


_ClientDescribeProductViewResponseProvisioningArtifactsTypeDef = TypedDict(
    "_ClientDescribeProductViewResponseProvisioningArtifactsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "Guidance": str,
    },
    total=False,
)


class ClientDescribeProductViewResponseProvisioningArtifactsTypeDef(
    _ClientDescribeProductViewResponseProvisioningArtifactsTypeDef
):
    """
    Type definition for `ClientDescribeProductViewResponse` `ProvisioningArtifacts`

    Information about a provisioning artifact. A provisioning artifact is also known as a
    product version.

    - **Id** *(string) --*

      The identifier of the provisioning artifact.

    - **Name** *(string) --*

      The name of the provisioning artifact.

    - **Description** *(string) --*

      The description of the provisioning artifact.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **Guidance** *(string) --*

      Information set by the administrator to provide guidance to end users about which
      provisioning artifacts to use.
    """


_ClientDescribeProductViewResponseTypeDef = TypedDict(
    "_ClientDescribeProductViewResponseTypeDef",
    {
        "ProductViewSummary": ClientDescribeProductViewResponseProductViewSummaryTypeDef,
        "ProvisioningArtifacts": List[
            ClientDescribeProductViewResponseProvisioningArtifactsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeProductViewResponseTypeDef(
    _ClientDescribeProductViewResponseTypeDef
):
    """
    Type definition for `ClientDescribeProductView` `Response`

    - **ProductViewSummary** *(dict) --*

      Summary information about the product.

      - **Id** *(string) --*

        The product view identifier.

      - **ProductId** *(string) --*

        The product identifier.

      - **Name** *(string) --*

        The name of the product.

      - **Owner** *(string) --*

        The owner of the product. Contact the product administrator for the significance of this
        value.

      - **ShortDescription** *(string) --*

        Short description of the product.

      - **Type** *(string) --*

        The product type. Contact the product administrator for the significance of this value. If
        this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

      - **Distributor** *(string) --*

        The distributor of the product. Contact the product administrator for the significance of
        this value.

      - **HasDefaultPath** *(boolean) --*

        Indicates whether the product has a default path. If the product does not have a default
        path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is
        not required, and the output of  ProductViewSummary can be used directly with
        DescribeProvisioningParameters .

      - **SupportEmail** *(string) --*

        The email contact information to obtain support for this Product.

      - **SupportDescription** *(string) --*

        The description of the support for this Product.

      - **SupportUrl** *(string) --*

        The URL information to obtain support for this Product.

    - **ProvisioningArtifacts** *(list) --*

      Information about the provisioning artifacts for the product.

      - *(dict) --*

        Information about a provisioning artifact. A provisioning artifact is also known as a
        product version.

        - **Id** *(string) --*

          The identifier of the provisioning artifact.

        - **Name** *(string) --*

          The name of the provisioning artifact.

        - **Description** *(string) --*

          The description of the provisioning artifact.

        - **CreatedTime** *(datetime) --*

          The UTC time stamp of the creation time.

        - **Guidance** *(string) --*

          Information set by the administrator to provide guidance to end users about which
          provisioning artifacts to use.
    """


_ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsProvisioningParametersTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsProvisioningParametersTypeDef",
    {"Key": str, "Value": str, "UsePreviousValue": bool},
    total=False,
)


class ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsProvisioningParametersTypeDef(
    _ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsProvisioningParametersTypeDef
):
    """
    Type definition for `ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetails` `ProvisioningParameters`

    The parameter key-value pair used to update a provisioned product.

    - **Key** *(string) --*

      The parameter key.

    - **Value** *(string) --*

      The parameter value.

    - **UsePreviousValue** *(boolean) --*

      If set to true, ``Value`` is ignored and the previous parameter value is kept.
    """


_ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTagsTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTagsTypeDef(
    _ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTagsTypeDef
):
    """
    Type definition for `ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetails` `Tags`

    Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
    created when provisioning a product.

    - **Key** *(string) --*

      The tag key.

    - **Value** *(string) --*

      The value for this key.
    """


_ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTypeDef",
    {
        "CreatedTime": datetime,
        "PathId": str,
        "ProductId": str,
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionProductName": str,
        "PlanType": str,
        "ProvisioningArtifactId": str,
        "Status": str,
        "UpdatedTime": datetime,
        "NotificationArns": List[str],
        "ProvisioningParameters": List[
            ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsProvisioningParametersTypeDef
        ],
        "Tags": List[
            ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTagsTypeDef
        ],
        "StatusMessage": str,
    },
    total=False,
)


class ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTypeDef(
    _ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTypeDef
):
    """
    Type definition for `ClientDescribeProvisionedProductPlanResponse` `ProvisionedProductPlanDetails`

    Information about the plan.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **PathId** *(string) --*

      The path identifier of the product. This value is optional if the product has a default
      path, and required if the product has more than one path. To list the paths for a product,
      use  ListLaunchPaths .

    - **ProductId** *(string) --*

      The product identifier.

    - **PlanName** *(string) --*

      The name of the plan.

    - **PlanId** *(string) --*

      The plan identifier.

    - **ProvisionProductId** *(string) --*

      The product identifier.

    - **ProvisionProductName** *(string) --*

      The user-friendly name of the provisioned product.

    - **PlanType** *(string) --*

      The plan type.

    - **ProvisioningArtifactId** *(string) --*

      The identifier of the provisioning artifact.

    - **Status** *(string) --*

      The status.

    - **UpdatedTime** *(datetime) --*

      The time when the plan was last updated.

    - **NotificationArns** *(list) --*

      Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.

      - *(string) --*

    - **ProvisioningParameters** *(list) --*

      Parameters specified by the administrator that are required for provisioning the product.

      - *(dict) --*

        The parameter key-value pair used to update a provisioned product.

        - **Key** *(string) --*

          The parameter key.

        - **Value** *(string) --*

          The parameter value.

        - **UsePreviousValue** *(boolean) --*

          If set to true, ``Value`` is ignored and the previous parameter value is kept.

    - **Tags** *(list) --*

      One or more tags.

      - *(dict) --*

        Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
        created when provisioning a product.

        - **Key** *(string) --*

          The tag key.

        - **Value** *(string) --*

          The value for this key.

    - **StatusMessage** *(string) --*

      The status message.
    """


_ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTargetTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTargetTypeDef",
    {"Attribute": str, "Name": str, "RequiresRecreation": str},
    total=False,
)


class ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTargetTypeDef(
    _ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTargetTypeDef
):
    """
    Type definition for `ClientDescribeProvisionedProductPlanResponseResourceChangesDetails` `Target`

    Information about the resource attribute to be modified.

    - **Attribute** *(string) --*

      The attribute to be changed.

    - **Name** *(string) --*

      If the attribute is ``Properties`` , the value is the name of the property.
      Otherwise, the value is null.

    - **RequiresRecreation** *(string) --*

      If the attribute is ``Properties`` , indicates whether a change to this property
      causes the resource to be re-created.
    """


_ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTypeDef",
    {
        "Target": ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTargetTypeDef,
        "Evaluation": str,
        "CausingEntity": str,
    },
    total=False,
)


class ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTypeDef(
    _ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTypeDef
):
    """
    Type definition for `ClientDescribeProvisionedProductPlanResponseResourceChanges` `Details`

    Information about a change to a resource attribute.

    - **Target** *(dict) --*

      Information about the resource attribute to be modified.

      - **Attribute** *(string) --*

        The attribute to be changed.

      - **Name** *(string) --*

        If the attribute is ``Properties`` , the value is the name of the property.
        Otherwise, the value is null.

      - **RequiresRecreation** *(string) --*

        If the attribute is ``Properties`` , indicates whether a change to this property
        causes the resource to be re-created.

    - **Evaluation** *(string) --*

      For static evaluations, the value of the resource attribute will change and the new
      value is known. For dynamic evaluations, the value might change, and any new value
      will be determined when the plan is updated.

    - **CausingEntity** *(string) --*

      The ID of the entity that caused the change.
    """


_ClientDescribeProvisionedProductPlanResponseResourceChangesTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductPlanResponseResourceChangesTypeDef",
    {
        "Action": str,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Replacement": str,
        "Scope": List[str],
        "Details": List[
            ClientDescribeProvisionedProductPlanResponseResourceChangesDetailsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeProvisionedProductPlanResponseResourceChangesTypeDef(
    _ClientDescribeProvisionedProductPlanResponseResourceChangesTypeDef
):
    """
    Type definition for `ClientDescribeProvisionedProductPlanResponse` `ResourceChanges`

    Information about a resource change that will occur when a plan is executed.

    - **Action** *(string) --*

      The change action.

    - **LogicalResourceId** *(string) --*

      The ID of the resource, as defined in the CloudFormation template.

    - **PhysicalResourceId** *(string) --*

      The ID of the resource, if it was already created.

    - **ResourceType** *(string) --*

      The type of resource.

    - **Replacement** *(string) --*

      If the change type is ``Modify`` , indicates whether the existing resource is deleted and
      replaced with a new one.

    - **Scope** *(list) --*

      The change scope.

      - *(string) --*

    - **Details** *(list) --*

      Information about the resource changes.

      - *(dict) --*

        Information about a change to a resource attribute.

        - **Target** *(dict) --*

          Information about the resource attribute to be modified.

          - **Attribute** *(string) --*

            The attribute to be changed.

          - **Name** *(string) --*

            If the attribute is ``Properties`` , the value is the name of the property.
            Otherwise, the value is null.

          - **RequiresRecreation** *(string) --*

            If the attribute is ``Properties`` , indicates whether a change to this property
            causes the resource to be re-created.

        - **Evaluation** *(string) --*

          For static evaluations, the value of the resource attribute will change and the new
          value is known. For dynamic evaluations, the value might change, and any new value
          will be determined when the plan is updated.

        - **CausingEntity** *(string) --*

          The ID of the entity that caused the change.
    """


_ClientDescribeProvisionedProductPlanResponseTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductPlanResponseTypeDef",
    {
        "ProvisionedProductPlanDetails": ClientDescribeProvisionedProductPlanResponseProvisionedProductPlanDetailsTypeDef,
        "ResourceChanges": List[
            ClientDescribeProvisionedProductPlanResponseResourceChangesTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientDescribeProvisionedProductPlanResponseTypeDef(
    _ClientDescribeProvisionedProductPlanResponseTypeDef
):
    """
    Type definition for `ClientDescribeProvisionedProductPlan` `Response`

    - **ProvisionedProductPlanDetails** *(dict) --*

      Information about the plan.

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

      - **PathId** *(string) --*

        The path identifier of the product. This value is optional if the product has a default
        path, and required if the product has more than one path. To list the paths for a product,
        use  ListLaunchPaths .

      - **ProductId** *(string) --*

        The product identifier.

      - **PlanName** *(string) --*

        The name of the plan.

      - **PlanId** *(string) --*

        The plan identifier.

      - **ProvisionProductId** *(string) --*

        The product identifier.

      - **ProvisionProductName** *(string) --*

        The user-friendly name of the provisioned product.

      - **PlanType** *(string) --*

        The plan type.

      - **ProvisioningArtifactId** *(string) --*

        The identifier of the provisioning artifact.

      - **Status** *(string) --*

        The status.

      - **UpdatedTime** *(datetime) --*

        The time when the plan was last updated.

      - **NotificationArns** *(list) --*

        Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.

        - *(string) --*

      - **ProvisioningParameters** *(list) --*

        Parameters specified by the administrator that are required for provisioning the product.

        - *(dict) --*

          The parameter key-value pair used to update a provisioned product.

          - **Key** *(string) --*

            The parameter key.

          - **Value** *(string) --*

            The parameter value.

          - **UsePreviousValue** *(boolean) --*

            If set to true, ``Value`` is ignored and the previous parameter value is kept.

      - **Tags** *(list) --*

        One or more tags.

        - *(dict) --*

          Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
          created when provisioning a product.

          - **Key** *(string) --*

            The tag key.

          - **Value** *(string) --*

            The value for this key.

      - **StatusMessage** *(string) --*

        The status message.

    - **ResourceChanges** *(list) --*

      Information about the resource changes that will occur when the plan is executed.

      - *(dict) --*

        Information about a resource change that will occur when a plan is executed.

        - **Action** *(string) --*

          The change action.

        - **LogicalResourceId** *(string) --*

          The ID of the resource, as defined in the CloudFormation template.

        - **PhysicalResourceId** *(string) --*

          The ID of the resource, if it was already created.

        - **ResourceType** *(string) --*

          The type of resource.

        - **Replacement** *(string) --*

          If the change type is ``Modify`` , indicates whether the existing resource is deleted and
          replaced with a new one.

        - **Scope** *(list) --*

          The change scope.

          - *(string) --*

        - **Details** *(list) --*

          Information about the resource changes.

          - *(dict) --*

            Information about a change to a resource attribute.

            - **Target** *(dict) --*

              Information about the resource attribute to be modified.

              - **Attribute** *(string) --*

                The attribute to be changed.

              - **Name** *(string) --*

                If the attribute is ``Properties`` , the value is the name of the property.
                Otherwise, the value is null.

              - **RequiresRecreation** *(string) --*

                If the attribute is ``Properties`` , indicates whether a change to this property
                causes the resource to be re-created.

            - **Evaluation** *(string) --*

              For static evaluations, the value of the resource attribute will change and the new
              value is known. For dynamic evaluations, the value might change, and any new value
              will be determined when the plan is updated.

            - **CausingEntity** *(string) --*

              The ID of the entity that caused the change.

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientDescribeProvisionedProductResponseCloudWatchDashboardsTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductResponseCloudWatchDashboardsTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeProvisionedProductResponseCloudWatchDashboardsTypeDef(
    _ClientDescribeProvisionedProductResponseCloudWatchDashboardsTypeDef
):
    """
    Type definition for `ClientDescribeProvisionedProductResponse` `CloudWatchDashboards`

    Information about a CloudWatch dashboard.

    - **Name** *(string) --*

      The name of the CloudWatch dashboard.
    """


_ClientDescribeProvisionedProductResponseProvisionedProductDetailTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductResponseProvisionedProductDetailTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": str,
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)


class ClientDescribeProvisionedProductResponseProvisionedProductDetailTypeDef(
    _ClientDescribeProvisionedProductResponseProvisionedProductDetailTypeDef
):
    """
    Type definition for `ClientDescribeProvisionedProductResponse` `ProvisionedProductDetail`

    Information about the provisioned product.

    - **Name** *(string) --*

      The user-friendly name of the provisioned product.

    - **Arn** *(string) --*

      The ARN of the provisioned product.

    - **Type** *(string) --*

      The type of provisioned product. The supported values are ``CFN_STACK`` and
      ``CFN_STACKSET`` .

    - **Id** *(string) --*

      The identifier of the provisioned product.

    - **Status** *(string) --*

      The current status of the provisioned product.

      * ``AVAILABLE`` - Stable state, ready to perform any operation. The most recent operation
      succeeded and completed.

      * ``UNDER_CHANGE`` - Transitive state. Operations performed might not have valid results.
      Wait for an ``AVAILABLE`` status before performing operations.

      * ``TAINTED`` - Stable state, ready to perform any operation. The stack has completed the
      requested operation but is not exactly what was requested. For example, a request to update
      to a new version failed and the stack rolled back to the current version.

      * ``ERROR`` - An unexpected error occurred. The provisioned product exists but the stack is
      not running. For example, CloudFormation received a parameter value that was not valid and
      could not launch the stack.

      * ``PLAN_IN_PROGRESS`` - Transitive state. The plan operations were performed to provision
      a new product, but resources have not yet been created. After reviewing the list of
      resources to be created, execute the plan. Wait for an ``AVAILABLE`` status before
      performing operations.

    - **StatusMessage** *(string) --*

      The current status message of the provisioned product.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **IdempotencyToken** *(string) --*

      A unique identifier that you provide to ensure idempotency. If multiple requests differ
      only by the idempotency token, the same response is returned for each repeated request.

    - **LastRecordId** *(string) --*

      The record identifier of the last request performed on this provisioned product.

    - **ProductId** *(string) --*

      The product identifier. For example, ``prod-abcdzk7xy33qa`` .

    - **ProvisioningArtifactId** *(string) --*

      The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .
    """


_ClientDescribeProvisionedProductResponseTypeDef = TypedDict(
    "_ClientDescribeProvisionedProductResponseTypeDef",
    {
        "ProvisionedProductDetail": ClientDescribeProvisionedProductResponseProvisionedProductDetailTypeDef,
        "CloudWatchDashboards": List[
            ClientDescribeProvisionedProductResponseCloudWatchDashboardsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeProvisionedProductResponseTypeDef(
    _ClientDescribeProvisionedProductResponseTypeDef
):
    """
    Type definition for `ClientDescribeProvisionedProduct` `Response`

    - **ProvisionedProductDetail** *(dict) --*

      Information about the provisioned product.

      - **Name** *(string) --*

        The user-friendly name of the provisioned product.

      - **Arn** *(string) --*

        The ARN of the provisioned product.

      - **Type** *(string) --*

        The type of provisioned product. The supported values are ``CFN_STACK`` and
        ``CFN_STACKSET`` .

      - **Id** *(string) --*

        The identifier of the provisioned product.

      - **Status** *(string) --*

        The current status of the provisioned product.

        * ``AVAILABLE`` - Stable state, ready to perform any operation. The most recent operation
        succeeded and completed.

        * ``UNDER_CHANGE`` - Transitive state. Operations performed might not have valid results.
        Wait for an ``AVAILABLE`` status before performing operations.

        * ``TAINTED`` - Stable state, ready to perform any operation. The stack has completed the
        requested operation but is not exactly what was requested. For example, a request to update
        to a new version failed and the stack rolled back to the current version.

        * ``ERROR`` - An unexpected error occurred. The provisioned product exists but the stack is
        not running. For example, CloudFormation received a parameter value that was not valid and
        could not launch the stack.

        * ``PLAN_IN_PROGRESS`` - Transitive state. The plan operations were performed to provision
        a new product, but resources have not yet been created. After reviewing the list of
        resources to be created, execute the plan. Wait for an ``AVAILABLE`` status before
        performing operations.

      - **StatusMessage** *(string) --*

        The current status message of the provisioned product.

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

      - **IdempotencyToken** *(string) --*

        A unique identifier that you provide to ensure idempotency. If multiple requests differ
        only by the idempotency token, the same response is returned for each repeated request.

      - **LastRecordId** *(string) --*

        The record identifier of the last request performed on this provisioned product.

      - **ProductId** *(string) --*

        The product identifier. For example, ``prod-abcdzk7xy33qa`` .

      - **ProvisioningArtifactId** *(string) --*

        The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .

    - **CloudWatchDashboards** *(list) --*

      Any CloudWatch dashboards that were created when provisioning the product.

      - *(dict) --*

        Information about a CloudWatch dashboard.

        - **Name** *(string) --*

          The name of the CloudWatch dashboard.
    """


_ClientDescribeProvisioningArtifactResponseProvisioningArtifactDetailTypeDef = TypedDict(
    "_ClientDescribeProvisioningArtifactResponseProvisioningArtifactDetailTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Type": str,
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": str,
    },
    total=False,
)


class ClientDescribeProvisioningArtifactResponseProvisioningArtifactDetailTypeDef(
    _ClientDescribeProvisioningArtifactResponseProvisioningArtifactDetailTypeDef
):
    """
    Type definition for `ClientDescribeProvisioningArtifactResponse` `ProvisioningArtifactDetail`

    Information about the provisioning artifact.

    - **Id** *(string) --*

      The identifier of the provisioning artifact.

    - **Name** *(string) --*

      The name of the provisioning artifact.

    - **Description** *(string) --*

      The description of the provisioning artifact.

    - **Type** *(string) --*

      The type of provisioning artifact.

      * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template

      * ``MARKETPLACE_AMI`` - AWS Marketplace AMI

      * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **Active** *(boolean) --*

      Indicates whether the product version is active.

    - **Guidance** *(string) --*

      Information set by the administrator to provide guidance to end users about which
      provisioning artifacts to use.
    """


_ClientDescribeProvisioningArtifactResponseTypeDef = TypedDict(
    "_ClientDescribeProvisioningArtifactResponseTypeDef",
    {
        "ProvisioningArtifactDetail": ClientDescribeProvisioningArtifactResponseProvisioningArtifactDetailTypeDef,
        "Info": Dict[str, str],
        "Status": str,
    },
    total=False,
)


class ClientDescribeProvisioningArtifactResponseTypeDef(
    _ClientDescribeProvisioningArtifactResponseTypeDef
):
    """
    Type definition for `ClientDescribeProvisioningArtifact` `Response`

    - **ProvisioningArtifactDetail** *(dict) --*

      Information about the provisioning artifact.

      - **Id** *(string) --*

        The identifier of the provisioning artifact.

      - **Name** *(string) --*

        The name of the provisioning artifact.

      - **Description** *(string) --*

        The description of the provisioning artifact.

      - **Type** *(string) --*

        The type of provisioning artifact.

        * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template

        * ``MARKETPLACE_AMI`` - AWS Marketplace AMI

        * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

      - **Active** *(boolean) --*

        Indicates whether the product version is active.

      - **Guidance** *(string) --*

        Information set by the administrator to provide guidance to end users about which
        provisioning artifacts to use.

    - **Info** *(dict) --*

      The URL of the CloudFormation template in Amazon S3.

      - *(string) --*

        - *(string) --*

    - **Status** *(string) --*

      The status of the current request.
    """


_ClientDescribeProvisioningParametersResponseConstraintSummariesTypeDef = TypedDict(
    "_ClientDescribeProvisioningParametersResponseConstraintSummariesTypeDef",
    {"Type": str, "Description": str},
    total=False,
)


class ClientDescribeProvisioningParametersResponseConstraintSummariesTypeDef(
    _ClientDescribeProvisioningParametersResponseConstraintSummariesTypeDef
):
    """
    Type definition for `ClientDescribeProvisioningParametersResponse` `ConstraintSummaries`

    Summary information about a constraint.

    - **Type** *(string) --*

      The type of constraint.

      * ``LAUNCH``

      * ``NOTIFICATION``

      * STACKSET

      * ``TEMPLATE``

    - **Description** *(string) --*

      The description of the constraint.
    """


_ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersParameterConstraintsTypeDef = TypedDict(
    "_ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersParameterConstraintsTypeDef",
    {"AllowedValues": List[str]},
    total=False,
)


class ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersParameterConstraintsTypeDef(
    _ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersParameterConstraintsTypeDef
):
    """
    Type definition for `ClientDescribeProvisioningParametersResponseProvisioningArtifactParameters` `ParameterConstraints`

    Constraints that the administrator has put on a parameter.

    - **AllowedValues** *(list) --*

      The values that the administrator has allowed for the parameter.

      - *(string) --*
    """


_ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersTypeDef = TypedDict(
    "_ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersTypeDef",
    {
        "ParameterKey": str,
        "DefaultValue": str,
        "ParameterType": str,
        "IsNoEcho": bool,
        "Description": str,
        "ParameterConstraints": ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersParameterConstraintsTypeDef,
    },
    total=False,
)


class ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersTypeDef(
    _ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersTypeDef
):
    """
    Type definition for `ClientDescribeProvisioningParametersResponse` `ProvisioningArtifactParameters`

    Information about a parameter used to provision a product.

    - **ParameterKey** *(string) --*

      The parameter key.

    - **DefaultValue** *(string) --*

      The default value.

    - **ParameterType** *(string) --*

      The parameter type.

    - **IsNoEcho** *(boolean) --*

      If this value is true, the value for this parameter is obfuscated from view when the
      parameter is retrieved. This parameter is used to hide sensitive information.

    - **Description** *(string) --*

      The description of the parameter.

    - **ParameterConstraints** *(dict) --*

      Constraints that the administrator has put on a parameter.

      - **AllowedValues** *(list) --*

        The values that the administrator has allowed for the parameter.

        - *(string) --*
    """


_ClientDescribeProvisioningParametersResponseProvisioningArtifactPreferencesTypeDef = TypedDict(
    "_ClientDescribeProvisioningParametersResponseProvisioningArtifactPreferencesTypeDef",
    {"StackSetAccounts": List[str], "StackSetRegions": List[str]},
    total=False,
)


class ClientDescribeProvisioningParametersResponseProvisioningArtifactPreferencesTypeDef(
    _ClientDescribeProvisioningParametersResponseProvisioningArtifactPreferencesTypeDef
):
    """
    Type definition for `ClientDescribeProvisioningParametersResponse` `ProvisioningArtifactPreferences`

    An object that contains information about preferences, such as regions and accounts, for the
    provisioning artifact.

    - **StackSetAccounts** *(list) --*

      One or more AWS accounts where stack instances are deployed from the stack set. These
      accounts can be scoped in ``ProvisioningPreferences$StackSetAccounts`` and
      ``UpdateProvisioningPreferences$StackSetAccounts`` .

      Applicable only to a ``CFN_STACKSET`` provisioned product type.

      - *(string) --*

    - **StackSetRegions** *(list) --*

      One or more AWS Regions where stack instances are deployed from the stack set. These
      regions can be scoped in ``ProvisioningPreferences$StackSetRegions`` and
      ``UpdateProvisioningPreferences$StackSetRegions`` .

      Applicable only to a ``CFN_STACKSET`` provisioned product type.

      - *(string) --*
    """


_ClientDescribeProvisioningParametersResponseTagOptionsTypeDef = TypedDict(
    "_ClientDescribeProvisioningParametersResponseTagOptionsTypeDef",
    {"Key": str, "Values": List[str]},
    total=False,
)


class ClientDescribeProvisioningParametersResponseTagOptionsTypeDef(
    _ClientDescribeProvisioningParametersResponseTagOptionsTypeDef
):
    """
    Type definition for `ClientDescribeProvisioningParametersResponse` `TagOptions`

    Summary information about a TagOption.

    - **Key** *(string) --*

      The TagOption key.

    - **Values** *(list) --*

      The TagOption value.

      - *(string) --*
    """


_ClientDescribeProvisioningParametersResponseUsageInstructionsTypeDef = TypedDict(
    "_ClientDescribeProvisioningParametersResponseUsageInstructionsTypeDef",
    {"Type": str, "Value": str},
    total=False,
)


class ClientDescribeProvisioningParametersResponseUsageInstructionsTypeDef(
    _ClientDescribeProvisioningParametersResponseUsageInstructionsTypeDef
):
    """
    Type definition for `ClientDescribeProvisioningParametersResponse` `UsageInstructions`

    Additional information provided by the administrator.

    - **Type** *(string) --*

      The usage instruction type for the value.

    - **Value** *(string) --*

      The usage instruction value for this type.
    """


_ClientDescribeProvisioningParametersResponseTypeDef = TypedDict(
    "_ClientDescribeProvisioningParametersResponseTypeDef",
    {
        "ProvisioningArtifactParameters": List[
            ClientDescribeProvisioningParametersResponseProvisioningArtifactParametersTypeDef
        ],
        "ConstraintSummaries": List[
            ClientDescribeProvisioningParametersResponseConstraintSummariesTypeDef
        ],
        "UsageInstructions": List[
            ClientDescribeProvisioningParametersResponseUsageInstructionsTypeDef
        ],
        "TagOptions": List[
            ClientDescribeProvisioningParametersResponseTagOptionsTypeDef
        ],
        "ProvisioningArtifactPreferences": ClientDescribeProvisioningParametersResponseProvisioningArtifactPreferencesTypeDef,
    },
    total=False,
)


class ClientDescribeProvisioningParametersResponseTypeDef(
    _ClientDescribeProvisioningParametersResponseTypeDef
):
    """
    Type definition for `ClientDescribeProvisioningParameters` `Response`

    - **ProvisioningArtifactParameters** *(list) --*

      Information about the parameters used to provision the product.

      - *(dict) --*

        Information about a parameter used to provision a product.

        - **ParameterKey** *(string) --*

          The parameter key.

        - **DefaultValue** *(string) --*

          The default value.

        - **ParameterType** *(string) --*

          The parameter type.

        - **IsNoEcho** *(boolean) --*

          If this value is true, the value for this parameter is obfuscated from view when the
          parameter is retrieved. This parameter is used to hide sensitive information.

        - **Description** *(string) --*

          The description of the parameter.

        - **ParameterConstraints** *(dict) --*

          Constraints that the administrator has put on a parameter.

          - **AllowedValues** *(list) --*

            The values that the administrator has allowed for the parameter.

            - *(string) --*

    - **ConstraintSummaries** *(list) --*

      Information about the constraints used to provision the product.

      - *(dict) --*

        Summary information about a constraint.

        - **Type** *(string) --*

          The type of constraint.

          * ``LAUNCH``

          * ``NOTIFICATION``

          * STACKSET

          * ``TEMPLATE``

        - **Description** *(string) --*

          The description of the constraint.

    - **UsageInstructions** *(list) --*

      Any additional metadata specifically related to the provisioning of the product. For example,
      see the ``Version`` field of the CloudFormation template.

      - *(dict) --*

        Additional information provided by the administrator.

        - **Type** *(string) --*

          The usage instruction type for the value.

        - **Value** *(string) --*

          The usage instruction value for this type.

    - **TagOptions** *(list) --*

      Information about the TagOptions associated with the resource.

      - *(dict) --*

        Summary information about a TagOption.

        - **Key** *(string) --*

          The TagOption key.

        - **Values** *(list) --*

          The TagOption value.

          - *(string) --*

    - **ProvisioningArtifactPreferences** *(dict) --*

      An object that contains information about preferences, such as regions and accounts, for the
      provisioning artifact.

      - **StackSetAccounts** *(list) --*

        One or more AWS accounts where stack instances are deployed from the stack set. These
        accounts can be scoped in ``ProvisioningPreferences$StackSetAccounts`` and
        ``UpdateProvisioningPreferences$StackSetAccounts`` .

        Applicable only to a ``CFN_STACKSET`` provisioned product type.

        - *(string) --*

      - **StackSetRegions** *(list) --*

        One or more AWS Regions where stack instances are deployed from the stack set. These
        regions can be scoped in ``ProvisioningPreferences$StackSetRegions`` and
        ``UpdateProvisioningPreferences$StackSetRegions`` .

        Applicable only to a ``CFN_STACKSET`` provisioned product type.

        - *(string) --*
    """


_ClientDescribeRecordResponseRecordDetailRecordErrorsTypeDef = TypedDict(
    "_ClientDescribeRecordResponseRecordDetailRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)


class ClientDescribeRecordResponseRecordDetailRecordErrorsTypeDef(
    _ClientDescribeRecordResponseRecordDetailRecordErrorsTypeDef
):
    """
    Type definition for `ClientDescribeRecordResponseRecordDetail` `RecordErrors`

    The error code and description resulting from an operation.

    - **Code** *(string) --*

      The numeric value of the error.

    - **Description** *(string) --*

      The description of the error.
    """


_ClientDescribeRecordResponseRecordDetailRecordTagsTypeDef = TypedDict(
    "_ClientDescribeRecordResponseRecordDetailRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientDescribeRecordResponseRecordDetailRecordTagsTypeDef(
    _ClientDescribeRecordResponseRecordDetailRecordTagsTypeDef
):
    """
    Type definition for `ClientDescribeRecordResponseRecordDetail` `RecordTags`

    Information about a tag, which is a key-value pair.

    - **Key** *(string) --*

      The key for this tag.

    - **Value** *(string) --*

      The value for this tag.
    """


_ClientDescribeRecordResponseRecordDetailTypeDef = TypedDict(
    "_ClientDescribeRecordResponseRecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": str,
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[
            ClientDescribeRecordResponseRecordDetailRecordErrorsTypeDef
        ],
        "RecordTags": List[ClientDescribeRecordResponseRecordDetailRecordTagsTypeDef],
    },
    total=False,
)


class ClientDescribeRecordResponseRecordDetailTypeDef(
    _ClientDescribeRecordResponseRecordDetailTypeDef
):
    """
    Type definition for `ClientDescribeRecordResponse` `RecordDetail`

    Information about the product.

    - **RecordId** *(string) --*

      The identifier of the record.

    - **ProvisionedProductName** *(string) --*

      The user-friendly name of the provisioned product.

    - **Status** *(string) --*

      The status of the provisioned product.

      * ``CREATED`` - The request was created but the operation has not started.

      * ``IN_PROGRESS`` - The requested operation is in progress.

      * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested
      operation failed and some remediation is occurring. For example, a rollback.

      * ``SUCCEEDED`` - The requested operation has successfully completed.

      * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using the
      error messages returned.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **UpdatedTime** *(datetime) --*

      The time when the record was last updated.

    - **ProvisionedProductType** *(string) --*

      The type of provisioned product. The supported values are ``CFN_STACK`` and
      ``CFN_STACKSET`` .

    - **RecordType** *(string) --*

      The record type.

      * ``PROVISION_PRODUCT``

      * ``UPDATE_PROVISIONED_PRODUCT``

      * ``TERMINATE_PROVISIONED_PRODUCT``

    - **ProvisionedProductId** *(string) --*

      The identifier of the provisioned product.

    - **ProductId** *(string) --*

      The product identifier.

    - **ProvisioningArtifactId** *(string) --*

      The identifier of the provisioning artifact.

    - **PathId** *(string) --*

      The path identifier.

    - **RecordErrors** *(list) --*

      The errors that occurred.

      - *(dict) --*

        The error code and description resulting from an operation.

        - **Code** *(string) --*

          The numeric value of the error.

        - **Description** *(string) --*

          The description of the error.

    - **RecordTags** *(list) --*

      One or more tags.

      - *(dict) --*

        Information about a tag, which is a key-value pair.

        - **Key** *(string) --*

          The key for this tag.

        - **Value** *(string) --*

          The value for this tag.
    """


_ClientDescribeRecordResponseRecordOutputsTypeDef = TypedDict(
    "_ClientDescribeRecordResponseRecordOutputsTypeDef",
    {"OutputKey": str, "OutputValue": str, "Description": str},
    total=False,
)


class ClientDescribeRecordResponseRecordOutputsTypeDef(
    _ClientDescribeRecordResponseRecordOutputsTypeDef
):
    """
    Type definition for `ClientDescribeRecordResponse` `RecordOutputs`

    The output for the product created as the result of a request. For example, the output for
    a CloudFormation-backed product that creates an S3 bucket would include the S3 bucket URL.

    - **OutputKey** *(string) --*

      The output key.

    - **OutputValue** *(string) --*

      The output value.

    - **Description** *(string) --*

      The description of the output.
    """


_ClientDescribeRecordResponseTypeDef = TypedDict(
    "_ClientDescribeRecordResponseTypeDef",
    {
        "RecordDetail": ClientDescribeRecordResponseRecordDetailTypeDef,
        "RecordOutputs": List[ClientDescribeRecordResponseRecordOutputsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)


class ClientDescribeRecordResponseTypeDef(_ClientDescribeRecordResponseTypeDef):
    """
    Type definition for `ClientDescribeRecord` `Response`

    - **RecordDetail** *(dict) --*

      Information about the product.

      - **RecordId** *(string) --*

        The identifier of the record.

      - **ProvisionedProductName** *(string) --*

        The user-friendly name of the provisioned product.

      - **Status** *(string) --*

        The status of the provisioned product.

        * ``CREATED`` - The request was created but the operation has not started.

        * ``IN_PROGRESS`` - The requested operation is in progress.

        * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested
        operation failed and some remediation is occurring. For example, a rollback.

        * ``SUCCEEDED`` - The requested operation has successfully completed.

        * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using the
        error messages returned.

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

      - **UpdatedTime** *(datetime) --*

        The time when the record was last updated.

      - **ProvisionedProductType** *(string) --*

        The type of provisioned product. The supported values are ``CFN_STACK`` and
        ``CFN_STACKSET`` .

      - **RecordType** *(string) --*

        The record type.

        * ``PROVISION_PRODUCT``

        * ``UPDATE_PROVISIONED_PRODUCT``

        * ``TERMINATE_PROVISIONED_PRODUCT``

      - **ProvisionedProductId** *(string) --*

        The identifier of the provisioned product.

      - **ProductId** *(string) --*

        The product identifier.

      - **ProvisioningArtifactId** *(string) --*

        The identifier of the provisioning artifact.

      - **PathId** *(string) --*

        The path identifier.

      - **RecordErrors** *(list) --*

        The errors that occurred.

        - *(dict) --*

          The error code and description resulting from an operation.

          - **Code** *(string) --*

            The numeric value of the error.

          - **Description** *(string) --*

            The description of the error.

      - **RecordTags** *(list) --*

        One or more tags.

        - *(dict) --*

          Information about a tag, which is a key-value pair.

          - **Key** *(string) --*

            The key for this tag.

          - **Value** *(string) --*

            The value for this tag.

    - **RecordOutputs** *(list) --*

      Information about the product created as the result of a request. For example, the output for
      a CloudFormation-backed product that creates an S3 bucket would include the S3 bucket URL.

      - *(dict) --*

        The output for the product created as the result of a request. For example, the output for
        a CloudFormation-backed product that creates an S3 bucket would include the S3 bucket URL.

        - **OutputKey** *(string) --*

          The output key.

        - **OutputValue** *(string) --*

          The output value.

        - **Description** *(string) --*

          The description of the output.

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientDescribeServiceActionExecutionParametersResponseServiceActionParametersTypeDef = TypedDict(
    "_ClientDescribeServiceActionExecutionParametersResponseServiceActionParametersTypeDef",
    {"Name": str, "Type": str, "DefaultValues": List[str]},
    total=False,
)


class ClientDescribeServiceActionExecutionParametersResponseServiceActionParametersTypeDef(
    _ClientDescribeServiceActionExecutionParametersResponseServiceActionParametersTypeDef
):
    """
    Type definition for `ClientDescribeServiceActionExecutionParametersResponse` `ServiceActionParameters`

    - **Name** *(string) --*

    - **Type** *(string) --*

    - **DefaultValues** *(list) --*

      - *(string) --*
    """


_ClientDescribeServiceActionExecutionParametersResponseTypeDef = TypedDict(
    "_ClientDescribeServiceActionExecutionParametersResponseTypeDef",
    {
        "ServiceActionParameters": List[
            ClientDescribeServiceActionExecutionParametersResponseServiceActionParametersTypeDef
        ]
    },
    total=False,
)


class ClientDescribeServiceActionExecutionParametersResponseTypeDef(
    _ClientDescribeServiceActionExecutionParametersResponseTypeDef
):
    """
    Type definition for `ClientDescribeServiceActionExecutionParameters` `Response`

    - **ServiceActionParameters** *(list) --*

      - *(dict) --*

        - **Name** *(string) --*

        - **Type** *(string) --*

        - **DefaultValues** *(list) --*

          - *(string) --*
    """


_ClientDescribeServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef = TypedDict(
    "_ClientDescribeServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)


class ClientDescribeServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef(
    _ClientDescribeServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef
):
    """
    Type definition for `ClientDescribeServiceActionResponseServiceActionDetail` `ServiceActionSummary`

    Summary information about the self-service action.

    - **Id** *(string) --*

      The self-service action identifier.

    - **Name** *(string) --*

      The self-service action name.

    - **Description** *(string) --*

      The self-service action description.

    - **DefinitionType** *(string) --*

      The self-service action definition type. For example, ``SSM_AUTOMATION`` .
    """


_ClientDescribeServiceActionResponseServiceActionDetailTypeDef = TypedDict(
    "_ClientDescribeServiceActionResponseServiceActionDetailTypeDef",
    {
        "ServiceActionSummary": ClientDescribeServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef,
        "Definition": Dict[str, str],
    },
    total=False,
)


class ClientDescribeServiceActionResponseServiceActionDetailTypeDef(
    _ClientDescribeServiceActionResponseServiceActionDetailTypeDef
):
    """
    Type definition for `ClientDescribeServiceActionResponse` `ServiceActionDetail`

    Detailed information about the self-service action.

    - **ServiceActionSummary** *(dict) --*

      Summary information about the self-service action.

      - **Id** *(string) --*

        The self-service action identifier.

      - **Name** *(string) --*

        The self-service action name.

      - **Description** *(string) --*

        The self-service action description.

      - **DefinitionType** *(string) --*

        The self-service action definition type. For example, ``SSM_AUTOMATION`` .

    - **Definition** *(dict) --*

      A map that defines the self-service action.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeServiceActionResponseTypeDef = TypedDict(
    "_ClientDescribeServiceActionResponseTypeDef",
    {
        "ServiceActionDetail": ClientDescribeServiceActionResponseServiceActionDetailTypeDef
    },
    total=False,
)


class ClientDescribeServiceActionResponseTypeDef(
    _ClientDescribeServiceActionResponseTypeDef
):
    """
    Type definition for `ClientDescribeServiceAction` `Response`

    - **ServiceActionDetail** *(dict) --*

      Detailed information about the self-service action.

      - **ServiceActionSummary** *(dict) --*

        Summary information about the self-service action.

        - **Id** *(string) --*

          The self-service action identifier.

        - **Name** *(string) --*

          The self-service action name.

        - **Description** *(string) --*

          The self-service action description.

        - **DefinitionType** *(string) --*

          The self-service action definition type. For example, ``SSM_AUTOMATION`` .

      - **Definition** *(dict) --*

        A map that defines the self-service action.

        - *(string) --*

          - *(string) --*
    """


_ClientDescribeTagOptionResponseTagOptionDetailTypeDef = TypedDict(
    "_ClientDescribeTagOptionResponseTagOptionDetailTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)


class ClientDescribeTagOptionResponseTagOptionDetailTypeDef(
    _ClientDescribeTagOptionResponseTagOptionDetailTypeDef
):
    """
    Type definition for `ClientDescribeTagOptionResponse` `TagOptionDetail`

    Information about the TagOption.

    - **Key** *(string) --*

      The TagOption key.

    - **Value** *(string) --*

      The TagOption value.

    - **Active** *(boolean) --*

      The TagOption active state.

    - **Id** *(string) --*

      The TagOption identifier.
    """


_ClientDescribeTagOptionResponseTypeDef = TypedDict(
    "_ClientDescribeTagOptionResponseTypeDef",
    {"TagOptionDetail": ClientDescribeTagOptionResponseTagOptionDetailTypeDef},
    total=False,
)


class ClientDescribeTagOptionResponseTypeDef(_ClientDescribeTagOptionResponseTypeDef):
    """
    Type definition for `ClientDescribeTagOption` `Response`

    - **TagOptionDetail** *(dict) --*

      Information about the TagOption.

      - **Key** *(string) --*

        The TagOption key.

      - **Value** *(string) --*

        The TagOption value.

      - **Active** *(boolean) --*

        The TagOption active state.

      - **Id** *(string) --*

        The TagOption identifier.
    """


_ClientExecuteProvisionedProductPlanResponseRecordDetailRecordErrorsTypeDef = TypedDict(
    "_ClientExecuteProvisionedProductPlanResponseRecordDetailRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)


class ClientExecuteProvisionedProductPlanResponseRecordDetailRecordErrorsTypeDef(
    _ClientExecuteProvisionedProductPlanResponseRecordDetailRecordErrorsTypeDef
):
    """
    Type definition for `ClientExecuteProvisionedProductPlanResponseRecordDetail` `RecordErrors`

    The error code and description resulting from an operation.

    - **Code** *(string) --*

      The numeric value of the error.

    - **Description** *(string) --*

      The description of the error.
    """


_ClientExecuteProvisionedProductPlanResponseRecordDetailRecordTagsTypeDef = TypedDict(
    "_ClientExecuteProvisionedProductPlanResponseRecordDetailRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientExecuteProvisionedProductPlanResponseRecordDetailRecordTagsTypeDef(
    _ClientExecuteProvisionedProductPlanResponseRecordDetailRecordTagsTypeDef
):
    """
    Type definition for `ClientExecuteProvisionedProductPlanResponseRecordDetail` `RecordTags`

    Information about a tag, which is a key-value pair.

    - **Key** *(string) --*

      The key for this tag.

    - **Value** *(string) --*

      The value for this tag.
    """


_ClientExecuteProvisionedProductPlanResponseRecordDetailTypeDef = TypedDict(
    "_ClientExecuteProvisionedProductPlanResponseRecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": str,
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[
            ClientExecuteProvisionedProductPlanResponseRecordDetailRecordErrorsTypeDef
        ],
        "RecordTags": List[
            ClientExecuteProvisionedProductPlanResponseRecordDetailRecordTagsTypeDef
        ],
    },
    total=False,
)


class ClientExecuteProvisionedProductPlanResponseRecordDetailTypeDef(
    _ClientExecuteProvisionedProductPlanResponseRecordDetailTypeDef
):
    """
    Type definition for `ClientExecuteProvisionedProductPlanResponse` `RecordDetail`

    Information about the result of provisioning the product.

    - **RecordId** *(string) --*

      The identifier of the record.

    - **ProvisionedProductName** *(string) --*

      The user-friendly name of the provisioned product.

    - **Status** *(string) --*

      The status of the provisioned product.

      * ``CREATED`` - The request was created but the operation has not started.

      * ``IN_PROGRESS`` - The requested operation is in progress.

      * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested
      operation failed and some remediation is occurring. For example, a rollback.

      * ``SUCCEEDED`` - The requested operation has successfully completed.

      * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using the
      error messages returned.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **UpdatedTime** *(datetime) --*

      The time when the record was last updated.

    - **ProvisionedProductType** *(string) --*

      The type of provisioned product. The supported values are ``CFN_STACK`` and
      ``CFN_STACKSET`` .

    - **RecordType** *(string) --*

      The record type.

      * ``PROVISION_PRODUCT``

      * ``UPDATE_PROVISIONED_PRODUCT``

      * ``TERMINATE_PROVISIONED_PRODUCT``

    - **ProvisionedProductId** *(string) --*

      The identifier of the provisioned product.

    - **ProductId** *(string) --*

      The product identifier.

    - **ProvisioningArtifactId** *(string) --*

      The identifier of the provisioning artifact.

    - **PathId** *(string) --*

      The path identifier.

    - **RecordErrors** *(list) --*

      The errors that occurred.

      - *(dict) --*

        The error code and description resulting from an operation.

        - **Code** *(string) --*

          The numeric value of the error.

        - **Description** *(string) --*

          The description of the error.

    - **RecordTags** *(list) --*

      One or more tags.

      - *(dict) --*

        Information about a tag, which is a key-value pair.

        - **Key** *(string) --*

          The key for this tag.

        - **Value** *(string) --*

          The value for this tag.
    """


_ClientExecuteProvisionedProductPlanResponseTypeDef = TypedDict(
    "_ClientExecuteProvisionedProductPlanResponseTypeDef",
    {"RecordDetail": ClientExecuteProvisionedProductPlanResponseRecordDetailTypeDef},
    total=False,
)


class ClientExecuteProvisionedProductPlanResponseTypeDef(
    _ClientExecuteProvisionedProductPlanResponseTypeDef
):
    """
    Type definition for `ClientExecuteProvisionedProductPlan` `Response`

    - **RecordDetail** *(dict) --*

      Information about the result of provisioning the product.

      - **RecordId** *(string) --*

        The identifier of the record.

      - **ProvisionedProductName** *(string) --*

        The user-friendly name of the provisioned product.

      - **Status** *(string) --*

        The status of the provisioned product.

        * ``CREATED`` - The request was created but the operation has not started.

        * ``IN_PROGRESS`` - The requested operation is in progress.

        * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested
        operation failed and some remediation is occurring. For example, a rollback.

        * ``SUCCEEDED`` - The requested operation has successfully completed.

        * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using the
        error messages returned.

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

      - **UpdatedTime** *(datetime) --*

        The time when the record was last updated.

      - **ProvisionedProductType** *(string) --*

        The type of provisioned product. The supported values are ``CFN_STACK`` and
        ``CFN_STACKSET`` .

      - **RecordType** *(string) --*

        The record type.

        * ``PROVISION_PRODUCT``

        * ``UPDATE_PROVISIONED_PRODUCT``

        * ``TERMINATE_PROVISIONED_PRODUCT``

      - **ProvisionedProductId** *(string) --*

        The identifier of the provisioned product.

      - **ProductId** *(string) --*

        The product identifier.

      - **ProvisioningArtifactId** *(string) --*

        The identifier of the provisioning artifact.

      - **PathId** *(string) --*

        The path identifier.

      - **RecordErrors** *(list) --*

        The errors that occurred.

        - *(dict) --*

          The error code and description resulting from an operation.

          - **Code** *(string) --*

            The numeric value of the error.

          - **Description** *(string) --*

            The description of the error.

      - **RecordTags** *(list) --*

        One or more tags.

        - *(dict) --*

          Information about a tag, which is a key-value pair.

          - **Key** *(string) --*

            The key for this tag.

          - **Value** *(string) --*

            The value for this tag.
    """


_ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordErrorsTypeDef = TypedDict(
    "_ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)


class ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordErrorsTypeDef(
    _ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordErrorsTypeDef
):
    """
    Type definition for `ClientExecuteProvisionedProductServiceActionResponseRecordDetail` `RecordErrors`

    The error code and description resulting from an operation.

    - **Code** *(string) --*

      The numeric value of the error.

    - **Description** *(string) --*

      The description of the error.
    """


_ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordTagsTypeDef = TypedDict(
    "_ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordTagsTypeDef(
    _ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordTagsTypeDef
):
    """
    Type definition for `ClientExecuteProvisionedProductServiceActionResponseRecordDetail` `RecordTags`

    Information about a tag, which is a key-value pair.

    - **Key** *(string) --*

      The key for this tag.

    - **Value** *(string) --*

      The value for this tag.
    """


_ClientExecuteProvisionedProductServiceActionResponseRecordDetailTypeDef = TypedDict(
    "_ClientExecuteProvisionedProductServiceActionResponseRecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": str,
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[
            ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordErrorsTypeDef
        ],
        "RecordTags": List[
            ClientExecuteProvisionedProductServiceActionResponseRecordDetailRecordTagsTypeDef
        ],
    },
    total=False,
)


class ClientExecuteProvisionedProductServiceActionResponseRecordDetailTypeDef(
    _ClientExecuteProvisionedProductServiceActionResponseRecordDetailTypeDef
):
    """
    Type definition for `ClientExecuteProvisionedProductServiceActionResponse` `RecordDetail`

    An object containing detailed information about the result of provisioning the product.

    - **RecordId** *(string) --*

      The identifier of the record.

    - **ProvisionedProductName** *(string) --*

      The user-friendly name of the provisioned product.

    - **Status** *(string) --*

      The status of the provisioned product.

      * ``CREATED`` - The request was created but the operation has not started.

      * ``IN_PROGRESS`` - The requested operation is in progress.

      * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested
      operation failed and some remediation is occurring. For example, a rollback.

      * ``SUCCEEDED`` - The requested operation has successfully completed.

      * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using the
      error messages returned.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **UpdatedTime** *(datetime) --*

      The time when the record was last updated.

    - **ProvisionedProductType** *(string) --*

      The type of provisioned product. The supported values are ``CFN_STACK`` and
      ``CFN_STACKSET`` .

    - **RecordType** *(string) --*

      The record type.

      * ``PROVISION_PRODUCT``

      * ``UPDATE_PROVISIONED_PRODUCT``

      * ``TERMINATE_PROVISIONED_PRODUCT``

    - **ProvisionedProductId** *(string) --*

      The identifier of the provisioned product.

    - **ProductId** *(string) --*

      The product identifier.

    - **ProvisioningArtifactId** *(string) --*

      The identifier of the provisioning artifact.

    - **PathId** *(string) --*

      The path identifier.

    - **RecordErrors** *(list) --*

      The errors that occurred.

      - *(dict) --*

        The error code and description resulting from an operation.

        - **Code** *(string) --*

          The numeric value of the error.

        - **Description** *(string) --*

          The description of the error.

    - **RecordTags** *(list) --*

      One or more tags.

      - *(dict) --*

        Information about a tag, which is a key-value pair.

        - **Key** *(string) --*

          The key for this tag.

        - **Value** *(string) --*

          The value for this tag.
    """


_ClientExecuteProvisionedProductServiceActionResponseTypeDef = TypedDict(
    "_ClientExecuteProvisionedProductServiceActionResponseTypeDef",
    {
        "RecordDetail": ClientExecuteProvisionedProductServiceActionResponseRecordDetailTypeDef
    },
    total=False,
)


class ClientExecuteProvisionedProductServiceActionResponseTypeDef(
    _ClientExecuteProvisionedProductServiceActionResponseTypeDef
):
    """
    Type definition for `ClientExecuteProvisionedProductServiceAction` `Response`

    - **RecordDetail** *(dict) --*

      An object containing detailed information about the result of provisioning the product.

      - **RecordId** *(string) --*

        The identifier of the record.

      - **ProvisionedProductName** *(string) --*

        The user-friendly name of the provisioned product.

      - **Status** *(string) --*

        The status of the provisioned product.

        * ``CREATED`` - The request was created but the operation has not started.

        * ``IN_PROGRESS`` - The requested operation is in progress.

        * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested
        operation failed and some remediation is occurring. For example, a rollback.

        * ``SUCCEEDED`` - The requested operation has successfully completed.

        * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using the
        error messages returned.

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

      - **UpdatedTime** *(datetime) --*

        The time when the record was last updated.

      - **ProvisionedProductType** *(string) --*

        The type of provisioned product. The supported values are ``CFN_STACK`` and
        ``CFN_STACKSET`` .

      - **RecordType** *(string) --*

        The record type.

        * ``PROVISION_PRODUCT``

        * ``UPDATE_PROVISIONED_PRODUCT``

        * ``TERMINATE_PROVISIONED_PRODUCT``

      - **ProvisionedProductId** *(string) --*

        The identifier of the provisioned product.

      - **ProductId** *(string) --*

        The product identifier.

      - **ProvisioningArtifactId** *(string) --*

        The identifier of the provisioning artifact.

      - **PathId** *(string) --*

        The path identifier.

      - **RecordErrors** *(list) --*

        The errors that occurred.

        - *(dict) --*

          The error code and description resulting from an operation.

          - **Code** *(string) --*

            The numeric value of the error.

          - **Description** *(string) --*

            The description of the error.

      - **RecordTags** *(list) --*

        One or more tags.

        - *(dict) --*

          Information about a tag, which is a key-value pair.

          - **Key** *(string) --*

            The key for this tag.

          - **Value** *(string) --*

            The value for this tag.
    """


_ClientGetAwsOrganizationsAccessStatusResponseTypeDef = TypedDict(
    "_ClientGetAwsOrganizationsAccessStatusResponseTypeDef",
    {"AccessStatus": str},
    total=False,
)


class ClientGetAwsOrganizationsAccessStatusResponseTypeDef(
    _ClientGetAwsOrganizationsAccessStatusResponseTypeDef
):
    """
    Type definition for `ClientGetAwsOrganizationsAccessStatus` `Response`

    - **AccessStatus** *(string) --*

      The status of the portfolio share feature.
    """


_ClientListAcceptedPortfolioSharesResponsePortfolioDetailsTypeDef = TypedDict(
    "_ClientListAcceptedPortfolioSharesResponsePortfolioDetailsTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)


class ClientListAcceptedPortfolioSharesResponsePortfolioDetailsTypeDef(
    _ClientListAcceptedPortfolioSharesResponsePortfolioDetailsTypeDef
):
    """
    Type definition for `ClientListAcceptedPortfolioSharesResponse` `PortfolioDetails`

    Information about a portfolio.

    - **Id** *(string) --*

      The portfolio identifier.

    - **ARN** *(string) --*

      The ARN assigned to the portfolio.

    - **DisplayName** *(string) --*

      The name to use for display purposes.

    - **Description** *(string) --*

      The description of the portfolio.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **ProviderName** *(string) --*

      The name of the portfolio provider.
    """


_ClientListAcceptedPortfolioSharesResponseTypeDef = TypedDict(
    "_ClientListAcceptedPortfolioSharesResponseTypeDef",
    {
        "PortfolioDetails": List[
            ClientListAcceptedPortfolioSharesResponsePortfolioDetailsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListAcceptedPortfolioSharesResponseTypeDef(
    _ClientListAcceptedPortfolioSharesResponseTypeDef
):
    """
    Type definition for `ClientListAcceptedPortfolioShares` `Response`

    - **PortfolioDetails** *(list) --*

      Information about the portfolios.

      - *(dict) --*

        Information about a portfolio.

        - **Id** *(string) --*

          The portfolio identifier.

        - **ARN** *(string) --*

          The ARN assigned to the portfolio.

        - **DisplayName** *(string) --*

          The name to use for display purposes.

        - **Description** *(string) --*

          The description of the portfolio.

        - **CreatedTime** *(datetime) --*

          The UTC time stamp of the creation time.

        - **ProviderName** *(string) --*

          The name of the portfolio provider.

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientListBudgetsForResourceResponseBudgetsTypeDef = TypedDict(
    "_ClientListBudgetsForResourceResponseBudgetsTypeDef",
    {"BudgetName": str},
    total=False,
)


class ClientListBudgetsForResourceResponseBudgetsTypeDef(
    _ClientListBudgetsForResourceResponseBudgetsTypeDef
):
    """
    Type definition for `ClientListBudgetsForResourceResponse` `Budgets`

    Information about a budget.

    - **BudgetName** *(string) --*

      Name of the associated budget.
    """


_ClientListBudgetsForResourceResponseTypeDef = TypedDict(
    "_ClientListBudgetsForResourceResponseTypeDef",
    {
        "Budgets": List[ClientListBudgetsForResourceResponseBudgetsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListBudgetsForResourceResponseTypeDef(
    _ClientListBudgetsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListBudgetsForResource` `Response`

    - **Budgets** *(list) --*

      Information about the associated budgets.

      - *(dict) --*

        Information about a budget.

        - **BudgetName** *(string) --*

          Name of the associated budget.

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientListConstraintsForPortfolioResponseConstraintDetailsTypeDef = TypedDict(
    "_ClientListConstraintsForPortfolioResponseConstraintDetailsTypeDef",
    {"ConstraintId": str, "Type": str, "Description": str, "Owner": str},
    total=False,
)


class ClientListConstraintsForPortfolioResponseConstraintDetailsTypeDef(
    _ClientListConstraintsForPortfolioResponseConstraintDetailsTypeDef
):
    """
    Type definition for `ClientListConstraintsForPortfolioResponse` `ConstraintDetails`

    Information about a constraint.

    - **ConstraintId** *(string) --*

      The identifier of the constraint.

    - **Type** *(string) --*

      The type of constraint.

      * ``LAUNCH``

      * ``NOTIFICATION``

      * STACKSET

      * ``TEMPLATE``

    - **Description** *(string) --*

      The description of the constraint.

    - **Owner** *(string) --*

      The owner of the constraint.
    """


_ClientListConstraintsForPortfolioResponseTypeDef = TypedDict(
    "_ClientListConstraintsForPortfolioResponseTypeDef",
    {
        "ConstraintDetails": List[
            ClientListConstraintsForPortfolioResponseConstraintDetailsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListConstraintsForPortfolioResponseTypeDef(
    _ClientListConstraintsForPortfolioResponseTypeDef
):
    """
    Type definition for `ClientListConstraintsForPortfolio` `Response`

    - **ConstraintDetails** *(list) --*

      Information about the constraints.

      - *(dict) --*

        Information about a constraint.

        - **ConstraintId** *(string) --*

          The identifier of the constraint.

        - **Type** *(string) --*

          The type of constraint.

          * ``LAUNCH``

          * ``NOTIFICATION``

          * STACKSET

          * ``TEMPLATE``

        - **Description** *(string) --*

          The description of the constraint.

        - **Owner** *(string) --*

          The owner of the constraint.

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientListLaunchPathsResponseLaunchPathSummariesConstraintSummariesTypeDef = TypedDict(
    "_ClientListLaunchPathsResponseLaunchPathSummariesConstraintSummariesTypeDef",
    {"Type": str, "Description": str},
    total=False,
)


class ClientListLaunchPathsResponseLaunchPathSummariesConstraintSummariesTypeDef(
    _ClientListLaunchPathsResponseLaunchPathSummariesConstraintSummariesTypeDef
):
    """
    Type definition for `ClientListLaunchPathsResponseLaunchPathSummaries` `ConstraintSummaries`

    Summary information about a constraint.

    - **Type** *(string) --*

      The type of constraint.

      * ``LAUNCH``

      * ``NOTIFICATION``

      * STACKSET

      * ``TEMPLATE``

    - **Description** *(string) --*

      The description of the constraint.
    """


_ClientListLaunchPathsResponseLaunchPathSummariesTagsTypeDef = TypedDict(
    "_ClientListLaunchPathsResponseLaunchPathSummariesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListLaunchPathsResponseLaunchPathSummariesTagsTypeDef(
    _ClientListLaunchPathsResponseLaunchPathSummariesTagsTypeDef
):
    """
    Type definition for `ClientListLaunchPathsResponseLaunchPathSummaries` `Tags`

    Information about a tag. A tag is a key-value pair. Tags are propagated to the
    resources created when provisioning a product.

    - **Key** *(string) --*

      The tag key.

    - **Value** *(string) --*

      The value for this key.
    """


_ClientListLaunchPathsResponseLaunchPathSummariesTypeDef = TypedDict(
    "_ClientListLaunchPathsResponseLaunchPathSummariesTypeDef",
    {
        "Id": str,
        "ConstraintSummaries": List[
            ClientListLaunchPathsResponseLaunchPathSummariesConstraintSummariesTypeDef
        ],
        "Tags": List[ClientListLaunchPathsResponseLaunchPathSummariesTagsTypeDef],
        "Name": str,
    },
    total=False,
)


class ClientListLaunchPathsResponseLaunchPathSummariesTypeDef(
    _ClientListLaunchPathsResponseLaunchPathSummariesTypeDef
):
    """
    Type definition for `ClientListLaunchPathsResponse` `LaunchPathSummaries`

    Summary information about a product path for a user.

    - **Id** *(string) --*

      The identifier of the product path.

    - **ConstraintSummaries** *(list) --*

      The constraints on the portfolio-product relationship.

      - *(dict) --*

        Summary information about a constraint.

        - **Type** *(string) --*

          The type of constraint.

          * ``LAUNCH``

          * ``NOTIFICATION``

          * STACKSET

          * ``TEMPLATE``

        - **Description** *(string) --*

          The description of the constraint.

    - **Tags** *(list) --*

      The tags associated with this product path.

      - *(dict) --*

        Information about a tag. A tag is a key-value pair. Tags are propagated to the
        resources created when provisioning a product.

        - **Key** *(string) --*

          The tag key.

        - **Value** *(string) --*

          The value for this key.

    - **Name** *(string) --*

      The name of the portfolio to which the user was assigned.
    """


_ClientListLaunchPathsResponseTypeDef = TypedDict(
    "_ClientListLaunchPathsResponseTypeDef",
    {
        "LaunchPathSummaries": List[
            ClientListLaunchPathsResponseLaunchPathSummariesTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListLaunchPathsResponseTypeDef(_ClientListLaunchPathsResponseTypeDef):
    """
    Type definition for `ClientListLaunchPaths` `Response`

    - **LaunchPathSummaries** *(list) --*

      Information about the launch path.

      - *(dict) --*

        Summary information about a product path for a user.

        - **Id** *(string) --*

          The identifier of the product path.

        - **ConstraintSummaries** *(list) --*

          The constraints on the portfolio-product relationship.

          - *(dict) --*

            Summary information about a constraint.

            - **Type** *(string) --*

              The type of constraint.

              * ``LAUNCH``

              * ``NOTIFICATION``

              * STACKSET

              * ``TEMPLATE``

            - **Description** *(string) --*

              The description of the constraint.

        - **Tags** *(list) --*

          The tags associated with this product path.

          - *(dict) --*

            Information about a tag. A tag is a key-value pair. Tags are propagated to the
            resources created when provisioning a product.

            - **Key** *(string) --*

              The tag key.

            - **Value** *(string) --*

              The value for this key.

        - **Name** *(string) --*

          The name of the portfolio to which the user was assigned.

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientListOrganizationPortfolioAccessResponseOrganizationNodesTypeDef = TypedDict(
    "_ClientListOrganizationPortfolioAccessResponseOrganizationNodesTypeDef",
    {"Type": str, "Value": str},
    total=False,
)


class ClientListOrganizationPortfolioAccessResponseOrganizationNodesTypeDef(
    _ClientListOrganizationPortfolioAccessResponseOrganizationNodesTypeDef
):
    """
    Type definition for `ClientListOrganizationPortfolioAccessResponse` `OrganizationNodes`

    Information about the organization node.

    - **Type** *(string) --*

      The organization node type.

    - **Value** *(string) --*

      The identifier of the organization node.
    """


_ClientListOrganizationPortfolioAccessResponseTypeDef = TypedDict(
    "_ClientListOrganizationPortfolioAccessResponseTypeDef",
    {
        "OrganizationNodes": List[
            ClientListOrganizationPortfolioAccessResponseOrganizationNodesTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListOrganizationPortfolioAccessResponseTypeDef(
    _ClientListOrganizationPortfolioAccessResponseTypeDef
):
    """
    Type definition for `ClientListOrganizationPortfolioAccess` `Response`

    - **OrganizationNodes** *(list) --*

      Displays information about the organization nodes.

      - *(dict) --*

        Information about the organization node.

        - **Type** *(string) --*

          The organization node type.

        - **Value** *(string) --*

          The identifier of the organization node.

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientListPortfolioAccessResponseTypeDef = TypedDict(
    "_ClientListPortfolioAccessResponseTypeDef",
    {"AccountIds": List[str], "NextPageToken": str},
    total=False,
)


class ClientListPortfolioAccessResponseTypeDef(
    _ClientListPortfolioAccessResponseTypeDef
):
    """
    Type definition for `ClientListPortfolioAccess` `Response`

    - **AccountIds** *(list) --*

      Information about the AWS accounts with access to the portfolio.

      - *(string) --*

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientListPortfoliosForProductResponsePortfolioDetailsTypeDef = TypedDict(
    "_ClientListPortfoliosForProductResponsePortfolioDetailsTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)


class ClientListPortfoliosForProductResponsePortfolioDetailsTypeDef(
    _ClientListPortfoliosForProductResponsePortfolioDetailsTypeDef
):
    """
    Type definition for `ClientListPortfoliosForProductResponse` `PortfolioDetails`

    Information about a portfolio.

    - **Id** *(string) --*

      The portfolio identifier.

    - **ARN** *(string) --*

      The ARN assigned to the portfolio.

    - **DisplayName** *(string) --*

      The name to use for display purposes.

    - **Description** *(string) --*

      The description of the portfolio.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **ProviderName** *(string) --*

      The name of the portfolio provider.
    """


_ClientListPortfoliosForProductResponseTypeDef = TypedDict(
    "_ClientListPortfoliosForProductResponseTypeDef",
    {
        "PortfolioDetails": List[
            ClientListPortfoliosForProductResponsePortfolioDetailsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListPortfoliosForProductResponseTypeDef(
    _ClientListPortfoliosForProductResponseTypeDef
):
    """
    Type definition for `ClientListPortfoliosForProduct` `Response`

    - **PortfolioDetails** *(list) --*

      Information about the portfolios.

      - *(dict) --*

        Information about a portfolio.

        - **Id** *(string) --*

          The portfolio identifier.

        - **ARN** *(string) --*

          The ARN assigned to the portfolio.

        - **DisplayName** *(string) --*

          The name to use for display purposes.

        - **Description** *(string) --*

          The description of the portfolio.

        - **CreatedTime** *(datetime) --*

          The UTC time stamp of the creation time.

        - **ProviderName** *(string) --*

          The name of the portfolio provider.

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientListPortfoliosResponsePortfolioDetailsTypeDef = TypedDict(
    "_ClientListPortfoliosResponsePortfolioDetailsTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)


class ClientListPortfoliosResponsePortfolioDetailsTypeDef(
    _ClientListPortfoliosResponsePortfolioDetailsTypeDef
):
    """
    Type definition for `ClientListPortfoliosResponse` `PortfolioDetails`

    Information about a portfolio.

    - **Id** *(string) --*

      The portfolio identifier.

    - **ARN** *(string) --*

      The ARN assigned to the portfolio.

    - **DisplayName** *(string) --*

      The name to use for display purposes.

    - **Description** *(string) --*

      The description of the portfolio.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **ProviderName** *(string) --*

      The name of the portfolio provider.
    """


_ClientListPortfoliosResponseTypeDef = TypedDict(
    "_ClientListPortfoliosResponseTypeDef",
    {
        "PortfolioDetails": List[ClientListPortfoliosResponsePortfolioDetailsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListPortfoliosResponseTypeDef(_ClientListPortfoliosResponseTypeDef):
    """
    Type definition for `ClientListPortfolios` `Response`

    - **PortfolioDetails** *(list) --*

      Information about the portfolios.

      - *(dict) --*

        Information about a portfolio.

        - **Id** *(string) --*

          The portfolio identifier.

        - **ARN** *(string) --*

          The ARN assigned to the portfolio.

        - **DisplayName** *(string) --*

          The name to use for display purposes.

        - **Description** *(string) --*

          The description of the portfolio.

        - **CreatedTime** *(datetime) --*

          The UTC time stamp of the creation time.

        - **ProviderName** *(string) --*

          The name of the portfolio provider.

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientListPrincipalsForPortfolioResponsePrincipalsTypeDef = TypedDict(
    "_ClientListPrincipalsForPortfolioResponsePrincipalsTypeDef",
    {"PrincipalARN": str, "PrincipalType": str},
    total=False,
)


class ClientListPrincipalsForPortfolioResponsePrincipalsTypeDef(
    _ClientListPrincipalsForPortfolioResponsePrincipalsTypeDef
):
    """
    Type definition for `ClientListPrincipalsForPortfolioResponse` `Principals`

    Information about a principal.

    - **PrincipalARN** *(string) --*

      The ARN of the principal (IAM user, role, or group).

    - **PrincipalType** *(string) --*

      The principal type. The supported value is ``IAM`` .
    """


_ClientListPrincipalsForPortfolioResponseTypeDef = TypedDict(
    "_ClientListPrincipalsForPortfolioResponseTypeDef",
    {
        "Principals": List[ClientListPrincipalsForPortfolioResponsePrincipalsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListPrincipalsForPortfolioResponseTypeDef(
    _ClientListPrincipalsForPortfolioResponseTypeDef
):
    """
    Type definition for `ClientListPrincipalsForPortfolio` `Response`

    - **Principals** *(list) --*

      The IAM principals (users or roles) associated with the portfolio.

      - *(dict) --*

        Information about a principal.

        - **PrincipalARN** *(string) --*

          The ARN of the principal (IAM user, role, or group).

        - **PrincipalType** *(string) --*

          The principal type. The supported value is ``IAM`` .

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientListProvisionedProductPlansAccessLevelFilterTypeDef = TypedDict(
    "_ClientListProvisionedProductPlansAccessLevelFilterTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListProvisionedProductPlansAccessLevelFilterTypeDef(
    _ClientListProvisionedProductPlansAccessLevelFilterTypeDef
):
    """
    Type definition for `ClientListProvisionedProductPlans` `AccessLevelFilter`

    The access level to use to obtain results. The default is ``User`` .

    - **Key** *(string) --*

      The access level.

      * ``Account`` - Filter results based on the account.

      * ``Role`` - Filter results based on the federated role of the specified user.

      * ``User`` - Filter results based on the specified user.

    - **Value** *(string) --*

      The user to which the access level applies. The only supported value is ``Self`` .
    """


_ClientListProvisionedProductPlansResponseProvisionedProductPlansTypeDef = TypedDict(
    "_ClientListProvisionedProductPlansResponseProvisionedProductPlansTypeDef",
    {
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionProductName": str,
        "PlanType": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)


class ClientListProvisionedProductPlansResponseProvisionedProductPlansTypeDef(
    _ClientListProvisionedProductPlansResponseProvisionedProductPlansTypeDef
):
    """
    Type definition for `ClientListProvisionedProductPlansResponse` `ProvisionedProductPlans`

    Summary information about a plan.

    - **PlanName** *(string) --*

      The name of the plan.

    - **PlanId** *(string) --*

      The plan identifier.

    - **ProvisionProductId** *(string) --*

      The product identifier.

    - **ProvisionProductName** *(string) --*

      The user-friendly name of the provisioned product.

    - **PlanType** *(string) --*

      The plan type.

    - **ProvisioningArtifactId** *(string) --*

      The identifier of the provisioning artifact.
    """


_ClientListProvisionedProductPlansResponseTypeDef = TypedDict(
    "_ClientListProvisionedProductPlansResponseTypeDef",
    {
        "ProvisionedProductPlans": List[
            ClientListProvisionedProductPlansResponseProvisionedProductPlansTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListProvisionedProductPlansResponseTypeDef(
    _ClientListProvisionedProductPlansResponseTypeDef
):
    """
    Type definition for `ClientListProvisionedProductPlans` `Response`

    - **ProvisionedProductPlans** *(list) --*

      Information about the plans.

      - *(dict) --*

        Summary information about a plan.

        - **PlanName** *(string) --*

          The name of the plan.

        - **PlanId** *(string) --*

          The plan identifier.

        - **ProvisionProductId** *(string) --*

          The product identifier.

        - **ProvisionProductName** *(string) --*

          The user-friendly name of the provisioned product.

        - **PlanType** *(string) --*

          The plan type.

        - **ProvisioningArtifactId** *(string) --*

          The identifier of the provisioning artifact.

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProductViewSummaryTypeDef = TypedDict(
    "_ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": str,
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProductViewSummaryTypeDef(
    _ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProductViewSummaryTypeDef
):
    """
    Type definition for `ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViews` `ProductViewSummary`

    Summary information about a product view.

    - **Id** *(string) --*

      The product view identifier.

    - **ProductId** *(string) --*

      The product identifier.

    - **Name** *(string) --*

      The name of the product.

    - **Owner** *(string) --*

      The owner of the product. Contact the product administrator for the significance of
      this value.

    - **ShortDescription** *(string) --*

      Short description of the product.

    - **Type** *(string) --*

      The product type. Contact the product administrator for the significance of this value.
      If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

    - **Distributor** *(string) --*

      The distributor of the product. Contact the product administrator for the significance
      of this value.

    - **HasDefaultPath** *(boolean) --*

      Indicates whether the product has a default path. If the product does not have a
      default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,
      ListLaunchPaths is not required, and the output of  ProductViewSummary can be used
      directly with  DescribeProvisioningParameters .

    - **SupportEmail** *(string) --*

      The email contact information to obtain support for this Product.

    - **SupportDescription** *(string) --*

      The description of the support for this Product.

    - **SupportUrl** *(string) --*

      The URL information to obtain support for this Product.
    """


_ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProvisioningArtifactTypeDef = TypedDict(
    "_ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProvisioningArtifactTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "Guidance": str,
    },
    total=False,
)


class ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProvisioningArtifactTypeDef(
    _ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProvisioningArtifactTypeDef
):
    """
    Type definition for `ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViews` `ProvisioningArtifact`

    Information about a provisioning artifact. A provisioning artifact is also known as a
    product version.

    - **Id** *(string) --*

      The identifier of the provisioning artifact.

    - **Name** *(string) --*

      The name of the provisioning artifact.

    - **Description** *(string) --*

      The description of the provisioning artifact.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **Guidance** *(string) --*

      Information set by the administrator to provide guidance to end users about which
      provisioning artifacts to use.
    """


_ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsTypeDef = TypedDict(
    "_ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsTypeDef",
    {
        "ProductViewSummary": ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProductViewSummaryTypeDef,
        "ProvisioningArtifact": ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsProvisioningArtifactTypeDef,
    },
    total=False,
)


class ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsTypeDef(
    _ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsTypeDef
):
    """
    Type definition for `ClientListProvisioningArtifactsForServiceActionResponse` `ProvisioningArtifactViews`

    An object that contains summary information about a product view and a provisioning
    artifact.

    - **ProductViewSummary** *(dict) --*

      Summary information about a product view.

      - **Id** *(string) --*

        The product view identifier.

      - **ProductId** *(string) --*

        The product identifier.

      - **Name** *(string) --*

        The name of the product.

      - **Owner** *(string) --*

        The owner of the product. Contact the product administrator for the significance of
        this value.

      - **ShortDescription** *(string) --*

        Short description of the product.

      - **Type** *(string) --*

        The product type. Contact the product administrator for the significance of this value.
        If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

      - **Distributor** *(string) --*

        The distributor of the product. Contact the product administrator for the significance
        of this value.

      - **HasDefaultPath** *(boolean) --*

        Indicates whether the product has a default path. If the product does not have a
        default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,
        ListLaunchPaths is not required, and the output of  ProductViewSummary can be used
        directly with  DescribeProvisioningParameters .

      - **SupportEmail** *(string) --*

        The email contact information to obtain support for this Product.

      - **SupportDescription** *(string) --*

        The description of the support for this Product.

      - **SupportUrl** *(string) --*

        The URL information to obtain support for this Product.

    - **ProvisioningArtifact** *(dict) --*

      Information about a provisioning artifact. A provisioning artifact is also known as a
      product version.

      - **Id** *(string) --*

        The identifier of the provisioning artifact.

      - **Name** *(string) --*

        The name of the provisioning artifact.

      - **Description** *(string) --*

        The description of the provisioning artifact.

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

      - **Guidance** *(string) --*

        Information set by the administrator to provide guidance to end users about which
        provisioning artifacts to use.
    """


_ClientListProvisioningArtifactsForServiceActionResponseTypeDef = TypedDict(
    "_ClientListProvisioningArtifactsForServiceActionResponseTypeDef",
    {
        "ProvisioningArtifactViews": List[
            ClientListProvisioningArtifactsForServiceActionResponseProvisioningArtifactViewsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListProvisioningArtifactsForServiceActionResponseTypeDef(
    _ClientListProvisioningArtifactsForServiceActionResponseTypeDef
):
    """
    Type definition for `ClientListProvisioningArtifactsForServiceAction` `Response`

    - **ProvisioningArtifactViews** *(list) --*

      An array of objects with information about product views and provisioning artifacts.

      - *(dict) --*

        An object that contains summary information about a product view and a provisioning
        artifact.

        - **ProductViewSummary** *(dict) --*

          Summary information about a product view.

          - **Id** *(string) --*

            The product view identifier.

          - **ProductId** *(string) --*

            The product identifier.

          - **Name** *(string) --*

            The name of the product.

          - **Owner** *(string) --*

            The owner of the product. Contact the product administrator for the significance of
            this value.

          - **ShortDescription** *(string) --*

            Short description of the product.

          - **Type** *(string) --*

            The product type. Contact the product administrator for the significance of this value.
            If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

          - **Distributor** *(string) --*

            The distributor of the product. Contact the product administrator for the significance
            of this value.

          - **HasDefaultPath** *(boolean) --*

            Indicates whether the product has a default path. If the product does not have a
            default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,
            ListLaunchPaths is not required, and the output of  ProductViewSummary can be used
            directly with  DescribeProvisioningParameters .

          - **SupportEmail** *(string) --*

            The email contact information to obtain support for this Product.

          - **SupportDescription** *(string) --*

            The description of the support for this Product.

          - **SupportUrl** *(string) --*

            The URL information to obtain support for this Product.

        - **ProvisioningArtifact** *(dict) --*

          Information about a provisioning artifact. A provisioning artifact is also known as a
          product version.

          - **Id** *(string) --*

            The identifier of the provisioning artifact.

          - **Name** *(string) --*

            The name of the provisioning artifact.

          - **Description** *(string) --*

            The description of the provisioning artifact.

          - **CreatedTime** *(datetime) --*

            The UTC time stamp of the creation time.

          - **Guidance** *(string) --*

            Information set by the administrator to provide guidance to end users about which
            provisioning artifacts to use.

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientListProvisioningArtifactsResponseProvisioningArtifactDetailsTypeDef = TypedDict(
    "_ClientListProvisioningArtifactsResponseProvisioningArtifactDetailsTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Type": str,
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": str,
    },
    total=False,
)


class ClientListProvisioningArtifactsResponseProvisioningArtifactDetailsTypeDef(
    _ClientListProvisioningArtifactsResponseProvisioningArtifactDetailsTypeDef
):
    """
    Type definition for `ClientListProvisioningArtifactsResponse` `ProvisioningArtifactDetails`

    Information about a provisioning artifact (also known as a version) for a product.

    - **Id** *(string) --*

      The identifier of the provisioning artifact.

    - **Name** *(string) --*

      The name of the provisioning artifact.

    - **Description** *(string) --*

      The description of the provisioning artifact.

    - **Type** *(string) --*

      The type of provisioning artifact.

      * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template

      * ``MARKETPLACE_AMI`` - AWS Marketplace AMI

      * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **Active** *(boolean) --*

      Indicates whether the product version is active.

    - **Guidance** *(string) --*

      Information set by the administrator to provide guidance to end users about which
      provisioning artifacts to use.
    """


_ClientListProvisioningArtifactsResponseTypeDef = TypedDict(
    "_ClientListProvisioningArtifactsResponseTypeDef",
    {
        "ProvisioningArtifactDetails": List[
            ClientListProvisioningArtifactsResponseProvisioningArtifactDetailsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListProvisioningArtifactsResponseTypeDef(
    _ClientListProvisioningArtifactsResponseTypeDef
):
    """
    Type definition for `ClientListProvisioningArtifacts` `Response`

    - **ProvisioningArtifactDetails** *(list) --*

      Information about the provisioning artifacts.

      - *(dict) --*

        Information about a provisioning artifact (also known as a version) for a product.

        - **Id** *(string) --*

          The identifier of the provisioning artifact.

        - **Name** *(string) --*

          The name of the provisioning artifact.

        - **Description** *(string) --*

          The description of the provisioning artifact.

        - **Type** *(string) --*

          The type of provisioning artifact.

          * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template

          * ``MARKETPLACE_AMI`` - AWS Marketplace AMI

          * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources

        - **CreatedTime** *(datetime) --*

          The UTC time stamp of the creation time.

        - **Active** *(boolean) --*

          Indicates whether the product version is active.

        - **Guidance** *(string) --*

          Information set by the administrator to provide guidance to end users about which
          provisioning artifacts to use.

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientListRecordHistoryAccessLevelFilterTypeDef = TypedDict(
    "_ClientListRecordHistoryAccessLevelFilterTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListRecordHistoryAccessLevelFilterTypeDef(
    _ClientListRecordHistoryAccessLevelFilterTypeDef
):
    """
    Type definition for `ClientListRecordHistory` `AccessLevelFilter`

    The access level to use to obtain results. The default is ``User`` .

    - **Key** *(string) --*

      The access level.

      * ``Account`` - Filter results based on the account.

      * ``Role`` - Filter results based on the federated role of the specified user.

      * ``User`` - Filter results based on the specified user.

    - **Value** *(string) --*

      The user to which the access level applies. The only supported value is ``Self`` .
    """


_ClientListRecordHistoryResponseRecordDetailsRecordErrorsTypeDef = TypedDict(
    "_ClientListRecordHistoryResponseRecordDetailsRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)


class ClientListRecordHistoryResponseRecordDetailsRecordErrorsTypeDef(
    _ClientListRecordHistoryResponseRecordDetailsRecordErrorsTypeDef
):
    """
    Type definition for `ClientListRecordHistoryResponseRecordDetails` `RecordErrors`

    The error code and description resulting from an operation.

    - **Code** *(string) --*

      The numeric value of the error.

    - **Description** *(string) --*

      The description of the error.
    """


_ClientListRecordHistoryResponseRecordDetailsRecordTagsTypeDef = TypedDict(
    "_ClientListRecordHistoryResponseRecordDetailsRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListRecordHistoryResponseRecordDetailsRecordTagsTypeDef(
    _ClientListRecordHistoryResponseRecordDetailsRecordTagsTypeDef
):
    """
    Type definition for `ClientListRecordHistoryResponseRecordDetails` `RecordTags`

    Information about a tag, which is a key-value pair.

    - **Key** *(string) --*

      The key for this tag.

    - **Value** *(string) --*

      The value for this tag.
    """


_ClientListRecordHistoryResponseRecordDetailsTypeDef = TypedDict(
    "_ClientListRecordHistoryResponseRecordDetailsTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": str,
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[
            ClientListRecordHistoryResponseRecordDetailsRecordErrorsTypeDef
        ],
        "RecordTags": List[
            ClientListRecordHistoryResponseRecordDetailsRecordTagsTypeDef
        ],
    },
    total=False,
)


class ClientListRecordHistoryResponseRecordDetailsTypeDef(
    _ClientListRecordHistoryResponseRecordDetailsTypeDef
):
    """
    Type definition for `ClientListRecordHistoryResponse` `RecordDetails`

    Information about a request operation.

    - **RecordId** *(string) --*

      The identifier of the record.

    - **ProvisionedProductName** *(string) --*

      The user-friendly name of the provisioned product.

    - **Status** *(string) --*

      The status of the provisioned product.

      * ``CREATED`` - The request was created but the operation has not started.

      * ``IN_PROGRESS`` - The requested operation is in progress.

      * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested
      operation failed and some remediation is occurring. For example, a rollback.

      * ``SUCCEEDED`` - The requested operation has successfully completed.

      * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using
      the error messages returned.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **UpdatedTime** *(datetime) --*

      The time when the record was last updated.

    - **ProvisionedProductType** *(string) --*

      The type of provisioned product. The supported values are ``CFN_STACK`` and
      ``CFN_STACKSET`` .

    - **RecordType** *(string) --*

      The record type.

      * ``PROVISION_PRODUCT``

      * ``UPDATE_PROVISIONED_PRODUCT``

      * ``TERMINATE_PROVISIONED_PRODUCT``

    - **ProvisionedProductId** *(string) --*

      The identifier of the provisioned product.

    - **ProductId** *(string) --*

      The product identifier.

    - **ProvisioningArtifactId** *(string) --*

      The identifier of the provisioning artifact.

    - **PathId** *(string) --*

      The path identifier.

    - **RecordErrors** *(list) --*

      The errors that occurred.

      - *(dict) --*

        The error code and description resulting from an operation.

        - **Code** *(string) --*

          The numeric value of the error.

        - **Description** *(string) --*

          The description of the error.

    - **RecordTags** *(list) --*

      One or more tags.

      - *(dict) --*

        Information about a tag, which is a key-value pair.

        - **Key** *(string) --*

          The key for this tag.

        - **Value** *(string) --*

          The value for this tag.
    """


_ClientListRecordHistoryResponseTypeDef = TypedDict(
    "_ClientListRecordHistoryResponseTypeDef",
    {
        "RecordDetails": List[ClientListRecordHistoryResponseRecordDetailsTypeDef],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListRecordHistoryResponseTypeDef(_ClientListRecordHistoryResponseTypeDef):
    """
    Type definition for `ClientListRecordHistory` `Response`

    - **RecordDetails** *(list) --*

      The records, in reverse chronological order.

      - *(dict) --*

        Information about a request operation.

        - **RecordId** *(string) --*

          The identifier of the record.

        - **ProvisionedProductName** *(string) --*

          The user-friendly name of the provisioned product.

        - **Status** *(string) --*

          The status of the provisioned product.

          * ``CREATED`` - The request was created but the operation has not started.

          * ``IN_PROGRESS`` - The requested operation is in progress.

          * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested
          operation failed and some remediation is occurring. For example, a rollback.

          * ``SUCCEEDED`` - The requested operation has successfully completed.

          * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using
          the error messages returned.

        - **CreatedTime** *(datetime) --*

          The UTC time stamp of the creation time.

        - **UpdatedTime** *(datetime) --*

          The time when the record was last updated.

        - **ProvisionedProductType** *(string) --*

          The type of provisioned product. The supported values are ``CFN_STACK`` and
          ``CFN_STACKSET`` .

        - **RecordType** *(string) --*

          The record type.

          * ``PROVISION_PRODUCT``

          * ``UPDATE_PROVISIONED_PRODUCT``

          * ``TERMINATE_PROVISIONED_PRODUCT``

        - **ProvisionedProductId** *(string) --*

          The identifier of the provisioned product.

        - **ProductId** *(string) --*

          The product identifier.

        - **ProvisioningArtifactId** *(string) --*

          The identifier of the provisioning artifact.

        - **PathId** *(string) --*

          The path identifier.

        - **RecordErrors** *(list) --*

          The errors that occurred.

          - *(dict) --*

            The error code and description resulting from an operation.

            - **Code** *(string) --*

              The numeric value of the error.

            - **Description** *(string) --*

              The description of the error.

        - **RecordTags** *(list) --*

          One or more tags.

          - *(dict) --*

            Information about a tag, which is a key-value pair.

            - **Key** *(string) --*

              The key for this tag.

            - **Value** *(string) --*

              The value for this tag.

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientListRecordHistorySearchFilterTypeDef = TypedDict(
    "_ClientListRecordHistorySearchFilterTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListRecordHistorySearchFilterTypeDef(
    _ClientListRecordHistorySearchFilterTypeDef
):
    """
    Type definition for `ClientListRecordHistory` `SearchFilter`

    The search filter to scope the results.

    - **Key** *(string) --*

      The filter key.

      * ``product`` - Filter results based on the specified product identifier.

      * ``provisionedproduct`` - Filter results based on the provisioned product identifier.

    - **Value** *(string) --*

      The filter value.
    """


_ClientListResourcesForTagOptionResponseResourceDetailsTypeDef = TypedDict(
    "_ClientListResourcesForTagOptionResponseResourceDetailsTypeDef",
    {"Id": str, "ARN": str, "Name": str, "Description": str, "CreatedTime": datetime},
    total=False,
)


class ClientListResourcesForTagOptionResponseResourceDetailsTypeDef(
    _ClientListResourcesForTagOptionResponseResourceDetailsTypeDef
):
    """
    Type definition for `ClientListResourcesForTagOptionResponse` `ResourceDetails`

    Information about a resource.

    - **Id** *(string) --*

      The identifier of the resource.

    - **ARN** *(string) --*

      The ARN of the resource.

    - **Name** *(string) --*

      The name of the resource.

    - **Description** *(string) --*

      The description of the resource.

    - **CreatedTime** *(datetime) --*

      The creation time of the resource.
    """


_ClientListResourcesForTagOptionResponseTypeDef = TypedDict(
    "_ClientListResourcesForTagOptionResponseTypeDef",
    {
        "ResourceDetails": List[
            ClientListResourcesForTagOptionResponseResourceDetailsTypeDef
        ],
        "PageToken": str,
    },
    total=False,
)


class ClientListResourcesForTagOptionResponseTypeDef(
    _ClientListResourcesForTagOptionResponseTypeDef
):
    """
    Type definition for `ClientListResourcesForTagOption` `Response`

    - **ResourceDetails** *(list) --*

      Information about the resources.

      - *(dict) --*

        Information about a resource.

        - **Id** *(string) --*

          The identifier of the resource.

        - **ARN** *(string) --*

          The ARN of the resource.

        - **Name** *(string) --*

          The name of the resource.

        - **Description** *(string) --*

          The description of the resource.

        - **CreatedTime** *(datetime) --*

          The creation time of the resource.

    - **PageToken** *(string) --*

      The page token for the next set of results. To retrieve the first set of results, use null.
    """


_ClientListServiceActionsForProvisioningArtifactResponseServiceActionSummariesTypeDef = TypedDict(
    "_ClientListServiceActionsForProvisioningArtifactResponseServiceActionSummariesTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)


class ClientListServiceActionsForProvisioningArtifactResponseServiceActionSummariesTypeDef(
    _ClientListServiceActionsForProvisioningArtifactResponseServiceActionSummariesTypeDef
):
    """
    Type definition for `ClientListServiceActionsForProvisioningArtifactResponse` `ServiceActionSummaries`

    Detailed information about the self-service action.

    - **Id** *(string) --*

      The self-service action identifier.

    - **Name** *(string) --*

      The self-service action name.

    - **Description** *(string) --*

      The self-service action description.

    - **DefinitionType** *(string) --*

      The self-service action definition type. For example, ``SSM_AUTOMATION`` .
    """


_ClientListServiceActionsForProvisioningArtifactResponseTypeDef = TypedDict(
    "_ClientListServiceActionsForProvisioningArtifactResponseTypeDef",
    {
        "ServiceActionSummaries": List[
            ClientListServiceActionsForProvisioningArtifactResponseServiceActionSummariesTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListServiceActionsForProvisioningArtifactResponseTypeDef(
    _ClientListServiceActionsForProvisioningArtifactResponseTypeDef
):
    """
    Type definition for `ClientListServiceActionsForProvisioningArtifact` `Response`

    - **ServiceActionSummaries** *(list) --*

      An object containing information about the self-service actions associated with the
      provisioning artifact.

      - *(dict) --*

        Detailed information about the self-service action.

        - **Id** *(string) --*

          The self-service action identifier.

        - **Name** *(string) --*

          The self-service action name.

        - **Description** *(string) --*

          The self-service action description.

        - **DefinitionType** *(string) --*

          The self-service action definition type. For example, ``SSM_AUTOMATION`` .

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientListServiceActionsResponseServiceActionSummariesTypeDef = TypedDict(
    "_ClientListServiceActionsResponseServiceActionSummariesTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)


class ClientListServiceActionsResponseServiceActionSummariesTypeDef(
    _ClientListServiceActionsResponseServiceActionSummariesTypeDef
):
    """
    Type definition for `ClientListServiceActionsResponse` `ServiceActionSummaries`

    Detailed information about the self-service action.

    - **Id** *(string) --*

      The self-service action identifier.

    - **Name** *(string) --*

      The self-service action name.

    - **Description** *(string) --*

      The self-service action description.

    - **DefinitionType** *(string) --*

      The self-service action definition type. For example, ``SSM_AUTOMATION`` .
    """


_ClientListServiceActionsResponseTypeDef = TypedDict(
    "_ClientListServiceActionsResponseTypeDef",
    {
        "ServiceActionSummaries": List[
            ClientListServiceActionsResponseServiceActionSummariesTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListServiceActionsResponseTypeDef(_ClientListServiceActionsResponseTypeDef):
    """
    Type definition for `ClientListServiceActions` `Response`

    - **ServiceActionSummaries** *(list) --*

      An object containing information about the service actions associated with the provisioning
      artifact.

      - *(dict) --*

        Detailed information about the self-service action.

        - **Id** *(string) --*

          The self-service action identifier.

        - **Name** *(string) --*

          The self-service action name.

        - **Description** *(string) --*

          The self-service action description.

        - **DefinitionType** *(string) --*

          The self-service action definition type. For example, ``SSM_AUTOMATION`` .

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientListStackInstancesForProvisionedProductResponseStackInstancesTypeDef = TypedDict(
    "_ClientListStackInstancesForProvisionedProductResponseStackInstancesTypeDef",
    {"Account": str, "Region": str, "StackInstanceStatus": str},
    total=False,
)


class ClientListStackInstancesForProvisionedProductResponseStackInstancesTypeDef(
    _ClientListStackInstancesForProvisionedProductResponseStackInstancesTypeDef
):
    """
    Type definition for `ClientListStackInstancesForProvisionedProductResponse` `StackInstances`

    An AWS CloudFormation stack, in a specific account and region, that's part of a stack set
    operation. A stack instance is a reference to an attempted or actual stack in a given
    account within a given region. A stack instance can exist without a stack—for example, if
    the stack couldn't be created for some reason. A stack instance is associated with only one
    stack set. Each stack instance contains the ID of its associated stack set, as well as the
    ID of the actual stack and the stack status.

    - **Account** *(string) --*

      The name of the AWS account that the stack instance is associated with.

    - **Region** *(string) --*

      The name of the AWS region that the stack instance is associated with.

    - **StackInstanceStatus** *(string) --*

      The status of the stack instance, in terms of its synchronization with its associated
      stack set.

      * ``INOPERABLE`` : A ``DeleteStackInstances`` operation has failed and left the stack in
      an unstable state. Stacks in this state are excluded from further ``UpdateStackSet``
      operations. You might need to perform a ``DeleteStackInstances`` operation, with
      ``RetainStacks`` set to true, to delete the stack instance, and then delete the stack
      manually.

      * ``OUTDATED`` : The stack isn't currently up to date with the stack set because either
      the associated stack failed during a ``CreateStackSet`` or ``UpdateStackSet`` operation,
      or the stack was part of a ``CreateStackSet`` or ``UpdateStackSet`` operation that failed
      or was stopped before the stack was created or updated.

      * ``CURRENT`` : The stack is currently up to date with the stack set.
    """


_ClientListStackInstancesForProvisionedProductResponseTypeDef = TypedDict(
    "_ClientListStackInstancesForProvisionedProductResponseTypeDef",
    {
        "StackInstances": List[
            ClientListStackInstancesForProvisionedProductResponseStackInstancesTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientListStackInstancesForProvisionedProductResponseTypeDef(
    _ClientListStackInstancesForProvisionedProductResponseTypeDef
):
    """
    Type definition for `ClientListStackInstancesForProvisionedProduct` `Response`

    - **StackInstances** *(list) --*

      List of stack instances.

      - *(dict) --*

        An AWS CloudFormation stack, in a specific account and region, that's part of a stack set
        operation. A stack instance is a reference to an attempted or actual stack in a given
        account within a given region. A stack instance can exist without a stack—for example, if
        the stack couldn't be created for some reason. A stack instance is associated with only one
        stack set. Each stack instance contains the ID of its associated stack set, as well as the
        ID of the actual stack and the stack status.

        - **Account** *(string) --*

          The name of the AWS account that the stack instance is associated with.

        - **Region** *(string) --*

          The name of the AWS region that the stack instance is associated with.

        - **StackInstanceStatus** *(string) --*

          The status of the stack instance, in terms of its synchronization with its associated
          stack set.

          * ``INOPERABLE`` : A ``DeleteStackInstances`` operation has failed and left the stack in
          an unstable state. Stacks in this state are excluded from further ``UpdateStackSet``
          operations. You might need to perform a ``DeleteStackInstances`` operation, with
          ``RetainStacks`` set to true, to delete the stack instance, and then delete the stack
          manually.

          * ``OUTDATED`` : The stack isn't currently up to date with the stack set because either
          the associated stack failed during a ``CreateStackSet`` or ``UpdateStackSet`` operation,
          or the stack was part of a ``CreateStackSet`` or ``UpdateStackSet`` operation that failed
          or was stopped before the stack was created or updated.

          * ``CURRENT`` : The stack is currently up to date with the stack set.

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientListTagOptionsFiltersTypeDef = TypedDict(
    "_ClientListTagOptionsFiltersTypeDef",
    {"Key": str, "Value": str, "Active": bool},
    total=False,
)


class ClientListTagOptionsFiltersTypeDef(_ClientListTagOptionsFiltersTypeDef):
    """
    Type definition for `ClientListTagOptions` `Filters`

    The search filters. If no search filters are specified, the output includes all TagOptions.

    - **Key** *(string) --*

      The TagOption key.

    - **Value** *(string) --*

      The TagOption value.

    - **Active** *(boolean) --*

      The active state.
    """


_ClientListTagOptionsResponseTagOptionDetailsTypeDef = TypedDict(
    "_ClientListTagOptionsResponseTagOptionDetailsTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)


class ClientListTagOptionsResponseTagOptionDetailsTypeDef(
    _ClientListTagOptionsResponseTagOptionDetailsTypeDef
):
    """
    Type definition for `ClientListTagOptionsResponse` `TagOptionDetails`

    Information about a TagOption.

    - **Key** *(string) --*

      The TagOption key.

    - **Value** *(string) --*

      The TagOption value.

    - **Active** *(boolean) --*

      The TagOption active state.

    - **Id** *(string) --*

      The TagOption identifier.
    """


_ClientListTagOptionsResponseTypeDef = TypedDict(
    "_ClientListTagOptionsResponseTypeDef",
    {
        "TagOptionDetails": List[ClientListTagOptionsResponseTagOptionDetailsTypeDef],
        "PageToken": str,
    },
    total=False,
)


class ClientListTagOptionsResponseTypeDef(_ClientListTagOptionsResponseTypeDef):
    """
    Type definition for `ClientListTagOptions` `Response`

    - **TagOptionDetails** *(list) --*

      Information about the TagOptions.

      - *(dict) --*

        Information about a TagOption.

        - **Key** *(string) --*

          The TagOption key.

        - **Value** *(string) --*

          The TagOption value.

        - **Active** *(boolean) --*

          The TagOption active state.

        - **Id** *(string) --*

          The TagOption identifier.

    - **PageToken** *(string) --*

      The page token for the next set of results. To retrieve the first set of results, use null.
    """


_ClientProvisionProductProvisioningParametersTypeDef = TypedDict(
    "_ClientProvisionProductProvisioningParametersTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientProvisionProductProvisioningParametersTypeDef(
    _ClientProvisionProductProvisioningParametersTypeDef
):
    """
    Type definition for `ClientProvisionProduct` `ProvisioningParameters`

    Information about a parameter used to provision a product.

    - **Key** *(string) --*

      The parameter key.

    - **Value** *(string) --*

      The parameter value.
    """


_ClientProvisionProductProvisioningPreferencesTypeDef = TypedDict(
    "_ClientProvisionProductProvisioningPreferencesTypeDef",
    {
        "StackSetAccounts": List[str],
        "StackSetRegions": List[str],
        "StackSetFailureToleranceCount": int,
        "StackSetFailureTolerancePercentage": int,
        "StackSetMaxConcurrencyCount": int,
        "StackSetMaxConcurrencyPercentage": int,
    },
    total=False,
)


class ClientProvisionProductProvisioningPreferencesTypeDef(
    _ClientProvisionProductProvisioningPreferencesTypeDef
):
    """
    Type definition for `ClientProvisionProduct` `ProvisioningPreferences`

    An object that contains information about the provisioning preferences for a stack set.

    - **StackSetAccounts** *(list) --*

      One or more AWS accounts that will have access to the provisioned product.

      Applicable only to a ``CFN_STACKSET`` provisioned product type.

      The AWS accounts specified should be within the list of accounts in the ``STACKSET``
      constraint. To get the list of accounts in the ``STACKSET`` constraint, use the
      ``DescribeProvisioningParameters`` operation.

      If no values are specified, the default value is all accounts from the ``STACKSET`` constraint.

      - *(string) --*

    - **StackSetRegions** *(list) --*

      One or more AWS Regions where the provisioned product will be available.

      Applicable only to a ``CFN_STACKSET`` provisioned product type.

      The specified regions should be within the list of regions from the ``STACKSET`` constraint. To
      get the list of regions in the ``STACKSET`` constraint, use the
      ``DescribeProvisioningParameters`` operation.

      If no values are specified, the default value is all regions from the ``STACKSET`` constraint.

      - *(string) --*

    - **StackSetFailureToleranceCount** *(integer) --*

      The number of accounts, per region, for which this operation can fail before AWS Service
      Catalog stops the operation in that region. If the operation is stopped in a region, AWS
      Service Catalog doesn't attempt the operation in any subsequent regions.

      Applicable only to a ``CFN_STACKSET`` provisioned product type.

      Conditional: You must specify either ``StackSetFailureToleranceCount`` or
      ``StackSetFailureTolerancePercentage`` , but not both.

      The default value is ``0`` if no value is specified.

    - **StackSetFailureTolerancePercentage** *(integer) --*

      The percentage of accounts, per region, for which this stack operation can fail before AWS
      Service Catalog stops the operation in that region. If the operation is stopped in a region,
      AWS Service Catalog doesn't attempt the operation in any subsequent regions.

      When calculating the number of accounts based on the specified percentage, AWS Service Catalog
      rounds down to the next whole number.

      Applicable only to a ``CFN_STACKSET`` provisioned product type.

      Conditional: You must specify either ``StackSetFailureToleranceCount`` or
      ``StackSetFailureTolerancePercentage`` , but not both.

    - **StackSetMaxConcurrencyCount** *(integer) --*

      The maximum number of accounts in which to perform this operation at one time. This is
      dependent on the value of ``StackSetFailureToleranceCount`` . ``StackSetMaxConcurrentCount`` is
      at most one more than the ``StackSetFailureToleranceCount`` .

      Note that this setting lets you specify the maximum for operations. For large deployments,
      under certain circumstances the actual number of accounts acted upon concurrently may be lower
      due to service throttling.

      Applicable only to a ``CFN_STACKSET`` provisioned product type.

      Conditional: You must specify either ``StackSetMaxConcurrentCount`` or
      ``StackSetMaxConcurrentPercentage`` , but not both.

    - **StackSetMaxConcurrencyPercentage** *(integer) --*

      The maximum percentage of accounts in which to perform this operation at one time.

      When calculating the number of accounts based on the specified percentage, AWS Service Catalog
      rounds down to the next whole number. This is true except in cases where rounding down would
      result is zero. In this case, AWS Service Catalog sets the number as ``1`` instead.

      Note that this setting lets you specify the maximum for operations. For large deployments,
      under certain circumstances the actual number of accounts acted upon concurrently may be lower
      due to service throttling.

      Applicable only to a ``CFN_STACKSET`` provisioned product type.

      Conditional: You must specify either ``StackSetMaxConcurrentCount`` or
      ``StackSetMaxConcurrentPercentage`` , but not both.
    """


_ClientProvisionProductResponseRecordDetailRecordErrorsTypeDef = TypedDict(
    "_ClientProvisionProductResponseRecordDetailRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)


class ClientProvisionProductResponseRecordDetailRecordErrorsTypeDef(
    _ClientProvisionProductResponseRecordDetailRecordErrorsTypeDef
):
    """
    Type definition for `ClientProvisionProductResponseRecordDetail` `RecordErrors`

    The error code and description resulting from an operation.

    - **Code** *(string) --*

      The numeric value of the error.

    - **Description** *(string) --*

      The description of the error.
    """


_ClientProvisionProductResponseRecordDetailRecordTagsTypeDef = TypedDict(
    "_ClientProvisionProductResponseRecordDetailRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientProvisionProductResponseRecordDetailRecordTagsTypeDef(
    _ClientProvisionProductResponseRecordDetailRecordTagsTypeDef
):
    """
    Type definition for `ClientProvisionProductResponseRecordDetail` `RecordTags`

    Information about a tag, which is a key-value pair.

    - **Key** *(string) --*

      The key for this tag.

    - **Value** *(string) --*

      The value for this tag.
    """


_ClientProvisionProductResponseRecordDetailTypeDef = TypedDict(
    "_ClientProvisionProductResponseRecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": str,
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[
            ClientProvisionProductResponseRecordDetailRecordErrorsTypeDef
        ],
        "RecordTags": List[ClientProvisionProductResponseRecordDetailRecordTagsTypeDef],
    },
    total=False,
)


class ClientProvisionProductResponseRecordDetailTypeDef(
    _ClientProvisionProductResponseRecordDetailTypeDef
):
    """
    Type definition for `ClientProvisionProductResponse` `RecordDetail`

    Information about the result of provisioning the product.

    - **RecordId** *(string) --*

      The identifier of the record.

    - **ProvisionedProductName** *(string) --*

      The user-friendly name of the provisioned product.

    - **Status** *(string) --*

      The status of the provisioned product.

      * ``CREATED`` - The request was created but the operation has not started.

      * ``IN_PROGRESS`` - The requested operation is in progress.

      * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested
      operation failed and some remediation is occurring. For example, a rollback.

      * ``SUCCEEDED`` - The requested operation has successfully completed.

      * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using the
      error messages returned.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **UpdatedTime** *(datetime) --*

      The time when the record was last updated.

    - **ProvisionedProductType** *(string) --*

      The type of provisioned product. The supported values are ``CFN_STACK`` and
      ``CFN_STACKSET`` .

    - **RecordType** *(string) --*

      The record type.

      * ``PROVISION_PRODUCT``

      * ``UPDATE_PROVISIONED_PRODUCT``

      * ``TERMINATE_PROVISIONED_PRODUCT``

    - **ProvisionedProductId** *(string) --*

      The identifier of the provisioned product.

    - **ProductId** *(string) --*

      The product identifier.

    - **ProvisioningArtifactId** *(string) --*

      The identifier of the provisioning artifact.

    - **PathId** *(string) --*

      The path identifier.

    - **RecordErrors** *(list) --*

      The errors that occurred.

      - *(dict) --*

        The error code and description resulting from an operation.

        - **Code** *(string) --*

          The numeric value of the error.

        - **Description** *(string) --*

          The description of the error.

    - **RecordTags** *(list) --*

      One or more tags.

      - *(dict) --*

        Information about a tag, which is a key-value pair.

        - **Key** *(string) --*

          The key for this tag.

        - **Value** *(string) --*

          The value for this tag.
    """


_ClientProvisionProductResponseTypeDef = TypedDict(
    "_ClientProvisionProductResponseTypeDef",
    {"RecordDetail": ClientProvisionProductResponseRecordDetailTypeDef},
    total=False,
)


class ClientProvisionProductResponseTypeDef(_ClientProvisionProductResponseTypeDef):
    """
    Type definition for `ClientProvisionProduct` `Response`

    - **RecordDetail** *(dict) --*

      Information about the result of provisioning the product.

      - **RecordId** *(string) --*

        The identifier of the record.

      - **ProvisionedProductName** *(string) --*

        The user-friendly name of the provisioned product.

      - **Status** *(string) --*

        The status of the provisioned product.

        * ``CREATED`` - The request was created but the operation has not started.

        * ``IN_PROGRESS`` - The requested operation is in progress.

        * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested
        operation failed and some remediation is occurring. For example, a rollback.

        * ``SUCCEEDED`` - The requested operation has successfully completed.

        * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using the
        error messages returned.

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

      - **UpdatedTime** *(datetime) --*

        The time when the record was last updated.

      - **ProvisionedProductType** *(string) --*

        The type of provisioned product. The supported values are ``CFN_STACK`` and
        ``CFN_STACKSET`` .

      - **RecordType** *(string) --*

        The record type.

        * ``PROVISION_PRODUCT``

        * ``UPDATE_PROVISIONED_PRODUCT``

        * ``TERMINATE_PROVISIONED_PRODUCT``

      - **ProvisionedProductId** *(string) --*

        The identifier of the provisioned product.

      - **ProductId** *(string) --*

        The product identifier.

      - **ProvisioningArtifactId** *(string) --*

        The identifier of the provisioning artifact.

      - **PathId** *(string) --*

        The path identifier.

      - **RecordErrors** *(list) --*

        The errors that occurred.

        - *(dict) --*

          The error code and description resulting from an operation.

          - **Code** *(string) --*

            The numeric value of the error.

          - **Description** *(string) --*

            The description of the error.

      - **RecordTags** *(list) --*

        One or more tags.

        - *(dict) --*

          Information about a tag, which is a key-value pair.

          - **Key** *(string) --*

            The key for this tag.

          - **Value** *(string) --*

            The value for this tag.
    """


_ClientProvisionProductTagsTypeDef = TypedDict(
    "_ClientProvisionProductTagsTypeDef", {"Key": str, "Value": str}
)


class ClientProvisionProductTagsTypeDef(_ClientProvisionProductTagsTypeDef):
    """
    Type definition for `ClientProvisionProduct` `Tags`

    Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
    created when provisioning a product.

    - **Key** *(string) --* **[REQUIRED]**

      The tag key.

    - **Value** *(string) --* **[REQUIRED]**

      The value for this key.
    """


_ClientScanProvisionedProductsAccessLevelFilterTypeDef = TypedDict(
    "_ClientScanProvisionedProductsAccessLevelFilterTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientScanProvisionedProductsAccessLevelFilterTypeDef(
    _ClientScanProvisionedProductsAccessLevelFilterTypeDef
):
    """
    Type definition for `ClientScanProvisionedProducts` `AccessLevelFilter`

    The access level to use to obtain results. The default is ``User`` .

    - **Key** *(string) --*

      The access level.

      * ``Account`` - Filter results based on the account.

      * ``Role`` - Filter results based on the federated role of the specified user.

      * ``User`` - Filter results based on the specified user.

    - **Value** *(string) --*

      The user to which the access level applies. The only supported value is ``Self`` .
    """


_ClientScanProvisionedProductsResponseProvisionedProductsTypeDef = TypedDict(
    "_ClientScanProvisionedProductsResponseProvisionedProductsTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": str,
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)


class ClientScanProvisionedProductsResponseProvisionedProductsTypeDef(
    _ClientScanProvisionedProductsResponseProvisionedProductsTypeDef
):
    """
    Type definition for `ClientScanProvisionedProductsResponse` `ProvisionedProducts`

    Information about a provisioned product.

    - **Name** *(string) --*

      The user-friendly name of the provisioned product.

    - **Arn** *(string) --*

      The ARN of the provisioned product.

    - **Type** *(string) --*

      The type of provisioned product. The supported values are ``CFN_STACK`` and
      ``CFN_STACKSET`` .

    - **Id** *(string) --*

      The identifier of the provisioned product.

    - **Status** *(string) --*

      The current status of the provisioned product.

      * ``AVAILABLE`` - Stable state, ready to perform any operation. The most recent operation
      succeeded and completed.

      * ``UNDER_CHANGE`` - Transitive state. Operations performed might not have valid results.
      Wait for an ``AVAILABLE`` status before performing operations.

      * ``TAINTED`` - Stable state, ready to perform any operation. The stack has completed the
      requested operation but is not exactly what was requested. For example, a request to
      update to a new version failed and the stack rolled back to the current version.

      * ``ERROR`` - An unexpected error occurred. The provisioned product exists but the stack
      is not running. For example, CloudFormation received a parameter value that was not valid
      and could not launch the stack.

      * ``PLAN_IN_PROGRESS`` - Transitive state. The plan operations were performed to
      provision a new product, but resources have not yet been created. After reviewing the
      list of resources to be created, execute the plan. Wait for an ``AVAILABLE`` status
      before performing operations.

    - **StatusMessage** *(string) --*

      The current status message of the provisioned product.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **IdempotencyToken** *(string) --*

      A unique identifier that you provide to ensure idempotency. If multiple requests differ
      only by the idempotency token, the same response is returned for each repeated request.

    - **LastRecordId** *(string) --*

      The record identifier of the last request performed on this provisioned product.

    - **ProductId** *(string) --*

      The product identifier. For example, ``prod-abcdzk7xy33qa`` .

    - **ProvisioningArtifactId** *(string) --*

      The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .
    """


_ClientScanProvisionedProductsResponseTypeDef = TypedDict(
    "_ClientScanProvisionedProductsResponseTypeDef",
    {
        "ProvisionedProducts": List[
            ClientScanProvisionedProductsResponseProvisionedProductsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientScanProvisionedProductsResponseTypeDef(
    _ClientScanProvisionedProductsResponseTypeDef
):
    """
    Type definition for `ClientScanProvisionedProducts` `Response`

    - **ProvisionedProducts** *(list) --*

      Information about the provisioned products.

      - *(dict) --*

        Information about a provisioned product.

        - **Name** *(string) --*

          The user-friendly name of the provisioned product.

        - **Arn** *(string) --*

          The ARN of the provisioned product.

        - **Type** *(string) --*

          The type of provisioned product. The supported values are ``CFN_STACK`` and
          ``CFN_STACKSET`` .

        - **Id** *(string) --*

          The identifier of the provisioned product.

        - **Status** *(string) --*

          The current status of the provisioned product.

          * ``AVAILABLE`` - Stable state, ready to perform any operation. The most recent operation
          succeeded and completed.

          * ``UNDER_CHANGE`` - Transitive state. Operations performed might not have valid results.
          Wait for an ``AVAILABLE`` status before performing operations.

          * ``TAINTED`` - Stable state, ready to perform any operation. The stack has completed the
          requested operation but is not exactly what was requested. For example, a request to
          update to a new version failed and the stack rolled back to the current version.

          * ``ERROR`` - An unexpected error occurred. The provisioned product exists but the stack
          is not running. For example, CloudFormation received a parameter value that was not valid
          and could not launch the stack.

          * ``PLAN_IN_PROGRESS`` - Transitive state. The plan operations were performed to
          provision a new product, but resources have not yet been created. After reviewing the
          list of resources to be created, execute the plan. Wait for an ``AVAILABLE`` status
          before performing operations.

        - **StatusMessage** *(string) --*

          The current status message of the provisioned product.

        - **CreatedTime** *(datetime) --*

          The UTC time stamp of the creation time.

        - **IdempotencyToken** *(string) --*

          A unique identifier that you provide to ensure idempotency. If multiple requests differ
          only by the idempotency token, the same response is returned for each repeated request.

        - **LastRecordId** *(string) --*

          The record identifier of the last request performed on this provisioned product.

        - **ProductId** *(string) --*

          The product identifier. For example, ``prod-abcdzk7xy33qa`` .

        - **ProvisioningArtifactId** *(string) --*

          The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientSearchProductsAsAdminResponseProductViewDetailsProductViewSummaryTypeDef = TypedDict(
    "_ClientSearchProductsAsAdminResponseProductViewDetailsProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": str,
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ClientSearchProductsAsAdminResponseProductViewDetailsProductViewSummaryTypeDef(
    _ClientSearchProductsAsAdminResponseProductViewDetailsProductViewSummaryTypeDef
):
    """
    Type definition for `ClientSearchProductsAsAdminResponseProductViewDetails` `ProductViewSummary`

    Summary information about the product view.

    - **Id** *(string) --*

      The product view identifier.

    - **ProductId** *(string) --*

      The product identifier.

    - **Name** *(string) --*

      The name of the product.

    - **Owner** *(string) --*

      The owner of the product. Contact the product administrator for the significance of
      this value.

    - **ShortDescription** *(string) --*

      Short description of the product.

    - **Type** *(string) --*

      The product type. Contact the product administrator for the significance of this value.
      If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

    - **Distributor** *(string) --*

      The distributor of the product. Contact the product administrator for the significance
      of this value.

    - **HasDefaultPath** *(boolean) --*

      Indicates whether the product has a default path. If the product does not have a
      default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,
      ListLaunchPaths is not required, and the output of  ProductViewSummary can be used
      directly with  DescribeProvisioningParameters .

    - **SupportEmail** *(string) --*

      The email contact information to obtain support for this Product.

    - **SupportDescription** *(string) --*

      The description of the support for this Product.

    - **SupportUrl** *(string) --*

      The URL information to obtain support for this Product.
    """


_ClientSearchProductsAsAdminResponseProductViewDetailsTypeDef = TypedDict(
    "_ClientSearchProductsAsAdminResponseProductViewDetailsTypeDef",
    {
        "ProductViewSummary": ClientSearchProductsAsAdminResponseProductViewDetailsProductViewSummaryTypeDef,
        "Status": str,
        "ProductARN": str,
        "CreatedTime": datetime,
    },
    total=False,
)


class ClientSearchProductsAsAdminResponseProductViewDetailsTypeDef(
    _ClientSearchProductsAsAdminResponseProductViewDetailsTypeDef
):
    """
    Type definition for `ClientSearchProductsAsAdminResponse` `ProductViewDetails`

    Information about a product view.

    - **ProductViewSummary** *(dict) --*

      Summary information about the product view.

      - **Id** *(string) --*

        The product view identifier.

      - **ProductId** *(string) --*

        The product identifier.

      - **Name** *(string) --*

        The name of the product.

      - **Owner** *(string) --*

        The owner of the product. Contact the product administrator for the significance of
        this value.

      - **ShortDescription** *(string) --*

        Short description of the product.

      - **Type** *(string) --*

        The product type. Contact the product administrator for the significance of this value.
        If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

      - **Distributor** *(string) --*

        The distributor of the product. Contact the product administrator for the significance
        of this value.

      - **HasDefaultPath** *(boolean) --*

        Indicates whether the product has a default path. If the product does not have a
        default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,
        ListLaunchPaths is not required, and the output of  ProductViewSummary can be used
        directly with  DescribeProvisioningParameters .

      - **SupportEmail** *(string) --*

        The email contact information to obtain support for this Product.

      - **SupportDescription** *(string) --*

        The description of the support for this Product.

      - **SupportUrl** *(string) --*

        The URL information to obtain support for this Product.

    - **Status** *(string) --*

      The status of the product.

      * ``AVAILABLE`` - The product is ready for use.

      * ``CREATING`` - Product creation has started; the product is not ready for use.

      * ``FAILED`` - An action failed.

    - **ProductARN** *(string) --*

      The ARN of the product.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.
    """


_ClientSearchProductsAsAdminResponseTypeDef = TypedDict(
    "_ClientSearchProductsAsAdminResponseTypeDef",
    {
        "ProductViewDetails": List[
            ClientSearchProductsAsAdminResponseProductViewDetailsTypeDef
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientSearchProductsAsAdminResponseTypeDef(
    _ClientSearchProductsAsAdminResponseTypeDef
):
    """
    Type definition for `ClientSearchProductsAsAdmin` `Response`

    - **ProductViewDetails** *(list) --*

      Information about the product views.

      - *(dict) --*

        Information about a product view.

        - **ProductViewSummary** *(dict) --*

          Summary information about the product view.

          - **Id** *(string) --*

            The product view identifier.

          - **ProductId** *(string) --*

            The product identifier.

          - **Name** *(string) --*

            The name of the product.

          - **Owner** *(string) --*

            The owner of the product. Contact the product administrator for the significance of
            this value.

          - **ShortDescription** *(string) --*

            Short description of the product.

          - **Type** *(string) --*

            The product type. Contact the product administrator for the significance of this value.
            If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

          - **Distributor** *(string) --*

            The distributor of the product. Contact the product administrator for the significance
            of this value.

          - **HasDefaultPath** *(boolean) --*

            Indicates whether the product has a default path. If the product does not have a
            default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,
            ListLaunchPaths is not required, and the output of  ProductViewSummary can be used
            directly with  DescribeProvisioningParameters .

          - **SupportEmail** *(string) --*

            The email contact information to obtain support for this Product.

          - **SupportDescription** *(string) --*

            The description of the support for this Product.

          - **SupportUrl** *(string) --*

            The URL information to obtain support for this Product.

        - **Status** *(string) --*

          The status of the product.

          * ``AVAILABLE`` - The product is ready for use.

          * ``CREATING`` - Product creation has started; the product is not ready for use.

          * ``FAILED`` - An action failed.

        - **ProductARN** *(string) --*

          The ARN of the product.

        - **CreatedTime** *(datetime) --*

          The UTC time stamp of the creation time.

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientSearchProductsResponseProductViewAggregationsTypeDef = TypedDict(
    "_ClientSearchProductsResponseProductViewAggregationsTypeDef",
    {"Value": str, "ApproximateCount": int},
    total=False,
)


class ClientSearchProductsResponseProductViewAggregationsTypeDef(
    _ClientSearchProductsResponseProductViewAggregationsTypeDef
):
    """
    Type definition for `ClientSearchProductsResponse` `ProductViewAggregations`

    A single product view aggregation value/count pair, containing metadata about each
    product to which the calling user has access.

    - **Value** *(string) --*

      The value of the product view aggregation.

    - **ApproximateCount** *(integer) --*

      An approximate count of the products that match the value.
    """


_ClientSearchProductsResponseProductViewSummariesTypeDef = TypedDict(
    "_ClientSearchProductsResponseProductViewSummariesTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": str,
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ClientSearchProductsResponseProductViewSummariesTypeDef(
    _ClientSearchProductsResponseProductViewSummariesTypeDef
):
    """
    Type definition for `ClientSearchProductsResponse` `ProductViewSummaries`

    Summary information about a product view.

    - **Id** *(string) --*

      The product view identifier.

    - **ProductId** *(string) --*

      The product identifier.

    - **Name** *(string) --*

      The name of the product.

    - **Owner** *(string) --*

      The owner of the product. Contact the product administrator for the significance of this
      value.

    - **ShortDescription** *(string) --*

      Short description of the product.

    - **Type** *(string) --*

      The product type. Contact the product administrator for the significance of this value.
      If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

    - **Distributor** *(string) --*

      The distributor of the product. Contact the product administrator for the significance of
      this value.

    - **HasDefaultPath** *(boolean) --*

      Indicates whether the product has a default path. If the product does not have a default
      path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is
      not required, and the output of  ProductViewSummary can be used directly with
      DescribeProvisioningParameters .

    - **SupportEmail** *(string) --*

      The email contact information to obtain support for this Product.

    - **SupportDescription** *(string) --*

      The description of the support for this Product.

    - **SupportUrl** *(string) --*

      The URL information to obtain support for this Product.
    """


_ClientSearchProductsResponseTypeDef = TypedDict(
    "_ClientSearchProductsResponseTypeDef",
    {
        "ProductViewSummaries": List[
            ClientSearchProductsResponseProductViewSummariesTypeDef
        ],
        "ProductViewAggregations": Dict[
            str, List[ClientSearchProductsResponseProductViewAggregationsTypeDef]
        ],
        "NextPageToken": str,
    },
    total=False,
)


class ClientSearchProductsResponseTypeDef(_ClientSearchProductsResponseTypeDef):
    """
    Type definition for `ClientSearchProducts` `Response`

    - **ProductViewSummaries** *(list) --*

      Information about the product views.

      - *(dict) --*

        Summary information about a product view.

        - **Id** *(string) --*

          The product view identifier.

        - **ProductId** *(string) --*

          The product identifier.

        - **Name** *(string) --*

          The name of the product.

        - **Owner** *(string) --*

          The owner of the product. Contact the product administrator for the significance of this
          value.

        - **ShortDescription** *(string) --*

          Short description of the product.

        - **Type** *(string) --*

          The product type. Contact the product administrator for the significance of this value.
          If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

        - **Distributor** *(string) --*

          The distributor of the product. Contact the product administrator for the significance of
          this value.

        - **HasDefaultPath** *(boolean) --*

          Indicates whether the product has a default path. If the product does not have a default
          path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is
          not required, and the output of  ProductViewSummary can be used directly with
          DescribeProvisioningParameters .

        - **SupportEmail** *(string) --*

          The email contact information to obtain support for this Product.

        - **SupportDescription** *(string) --*

          The description of the support for this Product.

        - **SupportUrl** *(string) --*

          The URL information to obtain support for this Product.

    - **ProductViewAggregations** *(dict) --*

      The product view aggregations.

      - *(string) --*

        - *(list) --*

          - *(dict) --*

            A single product view aggregation value/count pair, containing metadata about each
            product to which the calling user has access.

            - **Value** *(string) --*

              The value of the product view aggregation.

            - **ApproximateCount** *(integer) --*

              An approximate count of the products that match the value.

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientSearchProvisionedProductsAccessLevelFilterTypeDef = TypedDict(
    "_ClientSearchProvisionedProductsAccessLevelFilterTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientSearchProvisionedProductsAccessLevelFilterTypeDef(
    _ClientSearchProvisionedProductsAccessLevelFilterTypeDef
):
    """
    Type definition for `ClientSearchProvisionedProducts` `AccessLevelFilter`

    The access level to use to obtain results. The default is ``User`` .

    - **Key** *(string) --*

      The access level.

      * ``Account`` - Filter results based on the account.

      * ``Role`` - Filter results based on the federated role of the specified user.

      * ``User`` - Filter results based on the specified user.

    - **Value** *(string) --*

      The user to which the access level applies. The only supported value is ``Self`` .
    """


_ClientSearchProvisionedProductsResponseProvisionedProductsTagsTypeDef = TypedDict(
    "_ClientSearchProvisionedProductsResponseProvisionedProductsTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientSearchProvisionedProductsResponseProvisionedProductsTagsTypeDef(
    _ClientSearchProvisionedProductsResponseProvisionedProductsTagsTypeDef
):
    """
    Type definition for `ClientSearchProvisionedProductsResponseProvisionedProducts` `Tags`

    Information about a tag. A tag is a key-value pair. Tags are propagated to the
    resources created when provisioning a product.

    - **Key** *(string) --*

      The tag key.

    - **Value** *(string) --*

      The value for this key.
    """


_ClientSearchProvisionedProductsResponseProvisionedProductsTypeDef = TypedDict(
    "_ClientSearchProvisionedProductsResponseProvisionedProductsTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": str,
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "Tags": List[
            ClientSearchProvisionedProductsResponseProvisionedProductsTagsTypeDef
        ],
        "PhysicalId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "UserArn": str,
        "UserArnSession": str,
    },
    total=False,
)


class ClientSearchProvisionedProductsResponseProvisionedProductsTypeDef(
    _ClientSearchProvisionedProductsResponseProvisionedProductsTypeDef
):
    """
    Type definition for `ClientSearchProvisionedProductsResponse` `ProvisionedProducts`

    Information about a provisioned product.

    - **Name** *(string) --*

      The user-friendly name of the provisioned product.

    - **Arn** *(string) --*

      The ARN of the provisioned product.

    - **Type** *(string) --*

      The type of provisioned product. The supported values are ``CFN_STACK`` and
      ``CFN_STACKSET`` .

    - **Id** *(string) --*

      The identifier of the provisioned product.

    - **Status** *(string) --*

      The current status of the provisioned product.

      * ``AVAILABLE`` - Stable state, ready to perform any operation. The most recent operation
      succeeded and completed.

      * ``UNDER_CHANGE`` - Transitive state. Operations performed might not have valid results.
      Wait for an ``AVAILABLE`` status before performing operations.

      * ``TAINTED`` - Stable state, ready to perform any operation. The stack has completed the
      requested operation but is not exactly what was requested. For example, a request to
      update to a new version failed and the stack rolled back to the current version.

      * ``ERROR`` - An unexpected error occurred. The provisioned product exists but the stack
      is not running. For example, CloudFormation received a parameter value that was not valid
      and could not launch the stack.

      * ``PLAN_IN_PROGRESS`` - Transitive state. The plan operations were performed to
      provision a new product, but resources have not yet been created. After reviewing the
      list of resources to be created, execute the plan. Wait for an ``AVAILABLE`` status
      before performing operations.

    - **StatusMessage** *(string) --*

      The current status message of the provisioned product.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **IdempotencyToken** *(string) --*

      A unique identifier that you provide to ensure idempotency. If multiple requests differ
      only by the idempotency token, the same response is returned for each repeated request.

    - **LastRecordId** *(string) --*

      The record identifier of the last request performed on this provisioned product.

    - **Tags** *(list) --*

      One or more tags.

      - *(dict) --*

        Information about a tag. A tag is a key-value pair. Tags are propagated to the
        resources created when provisioning a product.

        - **Key** *(string) --*

          The tag key.

        - **Value** *(string) --*

          The value for this key.

    - **PhysicalId** *(string) --*

      The assigned identifier for the resource, such as an EC2 instance ID or an S3 bucket name.

    - **ProductId** *(string) --*

      The product identifier.

    - **ProvisioningArtifactId** *(string) --*

      The identifier of the provisioning artifact.

    - **UserArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM user.

    - **UserArnSession** *(string) --*

      The ARN of the IAM user in the session. This ARN might contain a session ID.
    """


_ClientSearchProvisionedProductsResponseTypeDef = TypedDict(
    "_ClientSearchProvisionedProductsResponseTypeDef",
    {
        "ProvisionedProducts": List[
            ClientSearchProvisionedProductsResponseProvisionedProductsTypeDef
        ],
        "TotalResultsCount": int,
        "NextPageToken": str,
    },
    total=False,
)


class ClientSearchProvisionedProductsResponseTypeDef(
    _ClientSearchProvisionedProductsResponseTypeDef
):
    """
    Type definition for `ClientSearchProvisionedProducts` `Response`

    - **ProvisionedProducts** *(list) --*

      Information about the provisioned products.

      - *(dict) --*

        Information about a provisioned product.

        - **Name** *(string) --*

          The user-friendly name of the provisioned product.

        - **Arn** *(string) --*

          The ARN of the provisioned product.

        - **Type** *(string) --*

          The type of provisioned product. The supported values are ``CFN_STACK`` and
          ``CFN_STACKSET`` .

        - **Id** *(string) --*

          The identifier of the provisioned product.

        - **Status** *(string) --*

          The current status of the provisioned product.

          * ``AVAILABLE`` - Stable state, ready to perform any operation. The most recent operation
          succeeded and completed.

          * ``UNDER_CHANGE`` - Transitive state. Operations performed might not have valid results.
          Wait for an ``AVAILABLE`` status before performing operations.

          * ``TAINTED`` - Stable state, ready to perform any operation. The stack has completed the
          requested operation but is not exactly what was requested. For example, a request to
          update to a new version failed and the stack rolled back to the current version.

          * ``ERROR`` - An unexpected error occurred. The provisioned product exists but the stack
          is not running. For example, CloudFormation received a parameter value that was not valid
          and could not launch the stack.

          * ``PLAN_IN_PROGRESS`` - Transitive state. The plan operations were performed to
          provision a new product, but resources have not yet been created. After reviewing the
          list of resources to be created, execute the plan. Wait for an ``AVAILABLE`` status
          before performing operations.

        - **StatusMessage** *(string) --*

          The current status message of the provisioned product.

        - **CreatedTime** *(datetime) --*

          The UTC time stamp of the creation time.

        - **IdempotencyToken** *(string) --*

          A unique identifier that you provide to ensure idempotency. If multiple requests differ
          only by the idempotency token, the same response is returned for each repeated request.

        - **LastRecordId** *(string) --*

          The record identifier of the last request performed on this provisioned product.

        - **Tags** *(list) --*

          One or more tags.

          - *(dict) --*

            Information about a tag. A tag is a key-value pair. Tags are propagated to the
            resources created when provisioning a product.

            - **Key** *(string) --*

              The tag key.

            - **Value** *(string) --*

              The value for this key.

        - **PhysicalId** *(string) --*

          The assigned identifier for the resource, such as an EC2 instance ID or an S3 bucket name.

        - **ProductId** *(string) --*

          The product identifier.

        - **ProvisioningArtifactId** *(string) --*

          The identifier of the provisioning artifact.

        - **UserArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM user.

        - **UserArnSession** *(string) --*

          The ARN of the IAM user in the session. This ARN might contain a session ID.

    - **TotalResultsCount** *(integer) --*

      The number of provisioned products found.

    - **NextPageToken** *(string) --*

      The page token to use to retrieve the next set of results. If there are no additional
      results, this value is null.
    """


_ClientTerminateProvisionedProductResponseRecordDetailRecordErrorsTypeDef = TypedDict(
    "_ClientTerminateProvisionedProductResponseRecordDetailRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)


class ClientTerminateProvisionedProductResponseRecordDetailRecordErrorsTypeDef(
    _ClientTerminateProvisionedProductResponseRecordDetailRecordErrorsTypeDef
):
    """
    Type definition for `ClientTerminateProvisionedProductResponseRecordDetail` `RecordErrors`

    The error code and description resulting from an operation.

    - **Code** *(string) --*

      The numeric value of the error.

    - **Description** *(string) --*

      The description of the error.
    """


_ClientTerminateProvisionedProductResponseRecordDetailRecordTagsTypeDef = TypedDict(
    "_ClientTerminateProvisionedProductResponseRecordDetailRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientTerminateProvisionedProductResponseRecordDetailRecordTagsTypeDef(
    _ClientTerminateProvisionedProductResponseRecordDetailRecordTagsTypeDef
):
    """
    Type definition for `ClientTerminateProvisionedProductResponseRecordDetail` `RecordTags`

    Information about a tag, which is a key-value pair.

    - **Key** *(string) --*

      The key for this tag.

    - **Value** *(string) --*

      The value for this tag.
    """


_ClientTerminateProvisionedProductResponseRecordDetailTypeDef = TypedDict(
    "_ClientTerminateProvisionedProductResponseRecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": str,
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[
            ClientTerminateProvisionedProductResponseRecordDetailRecordErrorsTypeDef
        ],
        "RecordTags": List[
            ClientTerminateProvisionedProductResponseRecordDetailRecordTagsTypeDef
        ],
    },
    total=False,
)


class ClientTerminateProvisionedProductResponseRecordDetailTypeDef(
    _ClientTerminateProvisionedProductResponseRecordDetailTypeDef
):
    """
    Type definition for `ClientTerminateProvisionedProductResponse` `RecordDetail`

    Information about the result of this request.

    - **RecordId** *(string) --*

      The identifier of the record.

    - **ProvisionedProductName** *(string) --*

      The user-friendly name of the provisioned product.

    - **Status** *(string) --*

      The status of the provisioned product.

      * ``CREATED`` - The request was created but the operation has not started.

      * ``IN_PROGRESS`` - The requested operation is in progress.

      * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested
      operation failed and some remediation is occurring. For example, a rollback.

      * ``SUCCEEDED`` - The requested operation has successfully completed.

      * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using the
      error messages returned.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **UpdatedTime** *(datetime) --*

      The time when the record was last updated.

    - **ProvisionedProductType** *(string) --*

      The type of provisioned product. The supported values are ``CFN_STACK`` and
      ``CFN_STACKSET`` .

    - **RecordType** *(string) --*

      The record type.

      * ``PROVISION_PRODUCT``

      * ``UPDATE_PROVISIONED_PRODUCT``

      * ``TERMINATE_PROVISIONED_PRODUCT``

    - **ProvisionedProductId** *(string) --*

      The identifier of the provisioned product.

    - **ProductId** *(string) --*

      The product identifier.

    - **ProvisioningArtifactId** *(string) --*

      The identifier of the provisioning artifact.

    - **PathId** *(string) --*

      The path identifier.

    - **RecordErrors** *(list) --*

      The errors that occurred.

      - *(dict) --*

        The error code and description resulting from an operation.

        - **Code** *(string) --*

          The numeric value of the error.

        - **Description** *(string) --*

          The description of the error.

    - **RecordTags** *(list) --*

      One or more tags.

      - *(dict) --*

        Information about a tag, which is a key-value pair.

        - **Key** *(string) --*

          The key for this tag.

        - **Value** *(string) --*

          The value for this tag.
    """


_ClientTerminateProvisionedProductResponseTypeDef = TypedDict(
    "_ClientTerminateProvisionedProductResponseTypeDef",
    {"RecordDetail": ClientTerminateProvisionedProductResponseRecordDetailTypeDef},
    total=False,
)


class ClientTerminateProvisionedProductResponseTypeDef(
    _ClientTerminateProvisionedProductResponseTypeDef
):
    """
    Type definition for `ClientTerminateProvisionedProduct` `Response`

    - **RecordDetail** *(dict) --*

      Information about the result of this request.

      - **RecordId** *(string) --*

        The identifier of the record.

      - **ProvisionedProductName** *(string) --*

        The user-friendly name of the provisioned product.

      - **Status** *(string) --*

        The status of the provisioned product.

        * ``CREATED`` - The request was created but the operation has not started.

        * ``IN_PROGRESS`` - The requested operation is in progress.

        * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested
        operation failed and some remediation is occurring. For example, a rollback.

        * ``SUCCEEDED`` - The requested operation has successfully completed.

        * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using the
        error messages returned.

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

      - **UpdatedTime** *(datetime) --*

        The time when the record was last updated.

      - **ProvisionedProductType** *(string) --*

        The type of provisioned product. The supported values are ``CFN_STACK`` and
        ``CFN_STACKSET`` .

      - **RecordType** *(string) --*

        The record type.

        * ``PROVISION_PRODUCT``

        * ``UPDATE_PROVISIONED_PRODUCT``

        * ``TERMINATE_PROVISIONED_PRODUCT``

      - **ProvisionedProductId** *(string) --*

        The identifier of the provisioned product.

      - **ProductId** *(string) --*

        The product identifier.

      - **ProvisioningArtifactId** *(string) --*

        The identifier of the provisioning artifact.

      - **PathId** *(string) --*

        The path identifier.

      - **RecordErrors** *(list) --*

        The errors that occurred.

        - *(dict) --*

          The error code and description resulting from an operation.

          - **Code** *(string) --*

            The numeric value of the error.

          - **Description** *(string) --*

            The description of the error.

      - **RecordTags** *(list) --*

        One or more tags.

        - *(dict) --*

          Information about a tag, which is a key-value pair.

          - **Key** *(string) --*

            The key for this tag.

          - **Value** *(string) --*

            The value for this tag.
    """


_ClientUpdateConstraintResponseConstraintDetailTypeDef = TypedDict(
    "_ClientUpdateConstraintResponseConstraintDetailTypeDef",
    {"ConstraintId": str, "Type": str, "Description": str, "Owner": str},
    total=False,
)


class ClientUpdateConstraintResponseConstraintDetailTypeDef(
    _ClientUpdateConstraintResponseConstraintDetailTypeDef
):
    """
    Type definition for `ClientUpdateConstraintResponse` `ConstraintDetail`

    Information about the constraint.

    - **ConstraintId** *(string) --*

      The identifier of the constraint.

    - **Type** *(string) --*

      The type of constraint.

      * ``LAUNCH``

      * ``NOTIFICATION``

      * STACKSET

      * ``TEMPLATE``

    - **Description** *(string) --*

      The description of the constraint.

    - **Owner** *(string) --*

      The owner of the constraint.
    """


_ClientUpdateConstraintResponseTypeDef = TypedDict(
    "_ClientUpdateConstraintResponseTypeDef",
    {
        "ConstraintDetail": ClientUpdateConstraintResponseConstraintDetailTypeDef,
        "ConstraintParameters": str,
        "Status": str,
    },
    total=False,
)


class ClientUpdateConstraintResponseTypeDef(_ClientUpdateConstraintResponseTypeDef):
    """
    Type definition for `ClientUpdateConstraint` `Response`

    - **ConstraintDetail** *(dict) --*

      Information about the constraint.

      - **ConstraintId** *(string) --*

        The identifier of the constraint.

      - **Type** *(string) --*

        The type of constraint.

        * ``LAUNCH``

        * ``NOTIFICATION``

        * STACKSET

        * ``TEMPLATE``

      - **Description** *(string) --*

        The description of the constraint.

      - **Owner** *(string) --*

        The owner of the constraint.

    - **ConstraintParameters** *(string) --*

      The constraint parameters.

    - **Status** *(string) --*

      The status of the current request.
    """


_ClientUpdatePortfolioAddTagsTypeDef = TypedDict(
    "_ClientUpdatePortfolioAddTagsTypeDef", {"Key": str, "Value": str}
)


class ClientUpdatePortfolioAddTagsTypeDef(_ClientUpdatePortfolioAddTagsTypeDef):
    """
    Type definition for `ClientUpdatePortfolio` `AddTags`

    Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
    created when provisioning a product.

    - **Key** *(string) --* **[REQUIRED]**

      The tag key.

    - **Value** *(string) --* **[REQUIRED]**

      The value for this key.
    """


_ClientUpdatePortfolioResponsePortfolioDetailTypeDef = TypedDict(
    "_ClientUpdatePortfolioResponsePortfolioDetailTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)


class ClientUpdatePortfolioResponsePortfolioDetailTypeDef(
    _ClientUpdatePortfolioResponsePortfolioDetailTypeDef
):
    """
    Type definition for `ClientUpdatePortfolioResponse` `PortfolioDetail`

    Information about the portfolio.

    - **Id** *(string) --*

      The portfolio identifier.

    - **ARN** *(string) --*

      The ARN assigned to the portfolio.

    - **DisplayName** *(string) --*

      The name to use for display purposes.

    - **Description** *(string) --*

      The description of the portfolio.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **ProviderName** *(string) --*

      The name of the portfolio provider.
    """


_ClientUpdatePortfolioResponseTagsTypeDef = TypedDict(
    "_ClientUpdatePortfolioResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientUpdatePortfolioResponseTagsTypeDef(
    _ClientUpdatePortfolioResponseTagsTypeDef
):
    """
    Type definition for `ClientUpdatePortfolioResponse` `Tags`

    Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
    created when provisioning a product.

    - **Key** *(string) --*

      The tag key.

    - **Value** *(string) --*

      The value for this key.
    """


_ClientUpdatePortfolioResponseTypeDef = TypedDict(
    "_ClientUpdatePortfolioResponseTypeDef",
    {
        "PortfolioDetail": ClientUpdatePortfolioResponsePortfolioDetailTypeDef,
        "Tags": List[ClientUpdatePortfolioResponseTagsTypeDef],
    },
    total=False,
)


class ClientUpdatePortfolioResponseTypeDef(_ClientUpdatePortfolioResponseTypeDef):
    """
    Type definition for `ClientUpdatePortfolio` `Response`

    - **PortfolioDetail** *(dict) --*

      Information about the portfolio.

      - **Id** *(string) --*

        The portfolio identifier.

      - **ARN** *(string) --*

        The ARN assigned to the portfolio.

      - **DisplayName** *(string) --*

        The name to use for display purposes.

      - **Description** *(string) --*

        The description of the portfolio.

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

      - **ProviderName** *(string) --*

        The name of the portfolio provider.

    - **Tags** *(list) --*

      Information about the tags associated with the portfolio.

      - *(dict) --*

        Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
        created when provisioning a product.

        - **Key** *(string) --*

          The tag key.

        - **Value** *(string) --*

          The value for this key.
    """


_ClientUpdateProductAddTagsTypeDef = TypedDict(
    "_ClientUpdateProductAddTagsTypeDef", {"Key": str, "Value": str}
)


class ClientUpdateProductAddTagsTypeDef(_ClientUpdateProductAddTagsTypeDef):
    """
    Type definition for `ClientUpdateProduct` `AddTags`

    Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
    created when provisioning a product.

    - **Key** *(string) --* **[REQUIRED]**

      The tag key.

    - **Value** *(string) --* **[REQUIRED]**

      The value for this key.
    """


_ClientUpdateProductResponseProductViewDetailProductViewSummaryTypeDef = TypedDict(
    "_ClientUpdateProductResponseProductViewDetailProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": str,
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ClientUpdateProductResponseProductViewDetailProductViewSummaryTypeDef(
    _ClientUpdateProductResponseProductViewDetailProductViewSummaryTypeDef
):
    """
    Type definition for `ClientUpdateProductResponseProductViewDetail` `ProductViewSummary`

    Summary information about the product view.

    - **Id** *(string) --*

      The product view identifier.

    - **ProductId** *(string) --*

      The product identifier.

    - **Name** *(string) --*

      The name of the product.

    - **Owner** *(string) --*

      The owner of the product. Contact the product administrator for the significance of this
      value.

    - **ShortDescription** *(string) --*

      Short description of the product.

    - **Type** *(string) --*

      The product type. Contact the product administrator for the significance of this value.
      If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

    - **Distributor** *(string) --*

      The distributor of the product. Contact the product administrator for the significance of
      this value.

    - **HasDefaultPath** *(boolean) --*

      Indicates whether the product has a default path. If the product does not have a default
      path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is
      not required, and the output of  ProductViewSummary can be used directly with
      DescribeProvisioningParameters .

    - **SupportEmail** *(string) --*

      The email contact information to obtain support for this Product.

    - **SupportDescription** *(string) --*

      The description of the support for this Product.

    - **SupportUrl** *(string) --*

      The URL information to obtain support for this Product.
    """


_ClientUpdateProductResponseProductViewDetailTypeDef = TypedDict(
    "_ClientUpdateProductResponseProductViewDetailTypeDef",
    {
        "ProductViewSummary": ClientUpdateProductResponseProductViewDetailProductViewSummaryTypeDef,
        "Status": str,
        "ProductARN": str,
        "CreatedTime": datetime,
    },
    total=False,
)


class ClientUpdateProductResponseProductViewDetailTypeDef(
    _ClientUpdateProductResponseProductViewDetailTypeDef
):
    """
    Type definition for `ClientUpdateProductResponse` `ProductViewDetail`

    Information about the product view.

    - **ProductViewSummary** *(dict) --*

      Summary information about the product view.

      - **Id** *(string) --*

        The product view identifier.

      - **ProductId** *(string) --*

        The product identifier.

      - **Name** *(string) --*

        The name of the product.

      - **Owner** *(string) --*

        The owner of the product. Contact the product administrator for the significance of this
        value.

      - **ShortDescription** *(string) --*

        Short description of the product.

      - **Type** *(string) --*

        The product type. Contact the product administrator for the significance of this value.
        If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

      - **Distributor** *(string) --*

        The distributor of the product. Contact the product administrator for the significance of
        this value.

      - **HasDefaultPath** *(boolean) --*

        Indicates whether the product has a default path. If the product does not have a default
        path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is
        not required, and the output of  ProductViewSummary can be used directly with
        DescribeProvisioningParameters .

      - **SupportEmail** *(string) --*

        The email contact information to obtain support for this Product.

      - **SupportDescription** *(string) --*

        The description of the support for this Product.

      - **SupportUrl** *(string) --*

        The URL information to obtain support for this Product.

    - **Status** *(string) --*

      The status of the product.

      * ``AVAILABLE`` - The product is ready for use.

      * ``CREATING`` - Product creation has started; the product is not ready for use.

      * ``FAILED`` - An action failed.

    - **ProductARN** *(string) --*

      The ARN of the product.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.
    """


_ClientUpdateProductResponseTagsTypeDef = TypedDict(
    "_ClientUpdateProductResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientUpdateProductResponseTagsTypeDef(_ClientUpdateProductResponseTagsTypeDef):
    """
    Type definition for `ClientUpdateProductResponse` `Tags`

    Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
    created when provisioning a product.

    - **Key** *(string) --*

      The tag key.

    - **Value** *(string) --*

      The value for this key.
    """


_ClientUpdateProductResponseTypeDef = TypedDict(
    "_ClientUpdateProductResponseTypeDef",
    {
        "ProductViewDetail": ClientUpdateProductResponseProductViewDetailTypeDef,
        "Tags": List[ClientUpdateProductResponseTagsTypeDef],
    },
    total=False,
)


class ClientUpdateProductResponseTypeDef(_ClientUpdateProductResponseTypeDef):
    """
    Type definition for `ClientUpdateProduct` `Response`

    - **ProductViewDetail** *(dict) --*

      Information about the product view.

      - **ProductViewSummary** *(dict) --*

        Summary information about the product view.

        - **Id** *(string) --*

          The product view identifier.

        - **ProductId** *(string) --*

          The product identifier.

        - **Name** *(string) --*

          The name of the product.

        - **Owner** *(string) --*

          The owner of the product. Contact the product administrator for the significance of this
          value.

        - **ShortDescription** *(string) --*

          Short description of the product.

        - **Type** *(string) --*

          The product type. Contact the product administrator for the significance of this value.
          If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

        - **Distributor** *(string) --*

          The distributor of the product. Contact the product administrator for the significance of
          this value.

        - **HasDefaultPath** *(boolean) --*

          Indicates whether the product has a default path. If the product does not have a default
          path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is
          not required, and the output of  ProductViewSummary can be used directly with
          DescribeProvisioningParameters .

        - **SupportEmail** *(string) --*

          The email contact information to obtain support for this Product.

        - **SupportDescription** *(string) --*

          The description of the support for this Product.

        - **SupportUrl** *(string) --*

          The URL information to obtain support for this Product.

      - **Status** *(string) --*

        The status of the product.

        * ``AVAILABLE`` - The product is ready for use.

        * ``CREATING`` - Product creation has started; the product is not ready for use.

        * ``FAILED`` - An action failed.

      - **ProductARN** *(string) --*

        The ARN of the product.

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

    - **Tags** *(list) --*

      Information about the tags associated with the product.

      - *(dict) --*

        Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
        created when provisioning a product.

        - **Key** *(string) --*

          The tag key.

        - **Value** *(string) --*

          The value for this key.
    """


_ClientUpdateProvisionedProductPropertiesResponseTypeDef = TypedDict(
    "_ClientUpdateProvisionedProductPropertiesResponseTypeDef",
    {
        "ProvisionedProductId": str,
        "ProvisionedProductProperties": Dict[str, str],
        "RecordId": str,
        "Status": str,
    },
    total=False,
)


class ClientUpdateProvisionedProductPropertiesResponseTypeDef(
    _ClientUpdateProvisionedProductPropertiesResponseTypeDef
):
    """
    Type definition for `ClientUpdateProvisionedProductProperties` `Response`

    - **ProvisionedProductId** *(string) --*

      The provisioned product identifier.

    - **ProvisionedProductProperties** *(dict) --*

      A map that contains the properties updated.

      - *(string) --*

        - *(string) --*

    - **RecordId** *(string) --*

      The identifier of the record.

    - **Status** *(string) --*

      The status of the request.
    """


_ClientUpdateProvisionedProductProvisioningParametersTypeDef = TypedDict(
    "_ClientUpdateProvisionedProductProvisioningParametersTypeDef",
    {"Key": str, "Value": str, "UsePreviousValue": bool},
    total=False,
)


class ClientUpdateProvisionedProductProvisioningParametersTypeDef(
    _ClientUpdateProvisionedProductProvisioningParametersTypeDef
):
    """
    Type definition for `ClientUpdateProvisionedProduct` `ProvisioningParameters`

    The parameter key-value pair used to update a provisioned product.

    - **Key** *(string) --*

      The parameter key.

    - **Value** *(string) --*

      The parameter value.

    - **UsePreviousValue** *(boolean) --*

      If set to true, ``Value`` is ignored and the previous parameter value is kept.
    """


_ClientUpdateProvisionedProductProvisioningPreferencesTypeDef = TypedDict(
    "_ClientUpdateProvisionedProductProvisioningPreferencesTypeDef",
    {
        "StackSetAccounts": List[str],
        "StackSetRegions": List[str],
        "StackSetFailureToleranceCount": int,
        "StackSetFailureTolerancePercentage": int,
        "StackSetMaxConcurrencyCount": int,
        "StackSetMaxConcurrencyPercentage": int,
        "StackSetOperationType": str,
    },
    total=False,
)


class ClientUpdateProvisionedProductProvisioningPreferencesTypeDef(
    _ClientUpdateProvisionedProductProvisioningPreferencesTypeDef
):
    """
    Type definition for `ClientUpdateProvisionedProduct` `ProvisioningPreferences`

    An object that contains information about the provisioning preferences for a stack set.

    - **StackSetAccounts** *(list) --*

      One or more AWS accounts that will have access to the provisioned product.

      Applicable only to a ``CFN_STACKSET`` provisioned product type.

      The AWS accounts specified should be within the list of accounts in the ``STACKSET``
      constraint. To get the list of accounts in the ``STACKSET`` constraint, use the
      ``DescribeProvisioningParameters`` operation.

      If no values are specified, the default value is all accounts from the ``STACKSET`` constraint.

      - *(string) --*

    - **StackSetRegions** *(list) --*

      One or more AWS Regions where the provisioned product will be available.

      Applicable only to a ``CFN_STACKSET`` provisioned product type.

      The specified regions should be within the list of regions from the ``STACKSET`` constraint. To
      get the list of regions in the ``STACKSET`` constraint, use the
      ``DescribeProvisioningParameters`` operation.

      If no values are specified, the default value is all regions from the ``STACKSET`` constraint.

      - *(string) --*

    - **StackSetFailureToleranceCount** *(integer) --*

      The number of accounts, per region, for which this operation can fail before AWS Service
      Catalog stops the operation in that region. If the operation is stopped in a region, AWS
      Service Catalog doesn't attempt the operation in any subsequent regions.

      Applicable only to a ``CFN_STACKSET`` provisioned product type.

      Conditional: You must specify either ``StackSetFailureToleranceCount`` or
      ``StackSetFailureTolerancePercentage`` , but not both.

      The default value is ``0`` if no value is specified.

    - **StackSetFailureTolerancePercentage** *(integer) --*

      The percentage of accounts, per region, for which this stack operation can fail before AWS
      Service Catalog stops the operation in that region. If the operation is stopped in a region,
      AWS Service Catalog doesn't attempt the operation in any subsequent regions.

      When calculating the number of accounts based on the specified percentage, AWS Service Catalog
      rounds down to the next whole number.

      Applicable only to a ``CFN_STACKSET`` provisioned product type.

      Conditional: You must specify either ``StackSetFailureToleranceCount`` or
      ``StackSetFailureTolerancePercentage`` , but not both.

    - **StackSetMaxConcurrencyCount** *(integer) --*

      The maximum number of accounts in which to perform this operation at one time. This is
      dependent on the value of ``StackSetFailureToleranceCount`` . ``StackSetMaxConcurrentCount`` is
      at most one more than the ``StackSetFailureToleranceCount`` .

      Note that this setting lets you specify the maximum for operations. For large deployments,
      under certain circumstances the actual number of accounts acted upon concurrently may be lower
      due to service throttling.

      Applicable only to a ``CFN_STACKSET`` provisioned product type.

      Conditional: You must specify either ``StackSetMaxConcurrentCount`` or
      ``StackSetMaxConcurrentPercentage`` , but not both.

    - **StackSetMaxConcurrencyPercentage** *(integer) --*

      The maximum percentage of accounts in which to perform this operation at one time.

      When calculating the number of accounts based on the specified percentage, AWS Service Catalog
      rounds down to the next whole number. This is true except in cases where rounding down would
      result is zero. In this case, AWS Service Catalog sets the number as ``1`` instead.

      Note that this setting lets you specify the maximum for operations. For large deployments,
      under certain circumstances the actual number of accounts acted upon concurrently may be lower
      due to service throttling.

      Applicable only to a ``CFN_STACKSET`` provisioned product type.

      Conditional: You must specify either ``StackSetMaxConcurrentCount`` or
      ``StackSetMaxConcurrentPercentage`` , but not both.

    - **StackSetOperationType** *(string) --*

      Determines what action AWS Service Catalog performs to a stack set or a stack instance
      represented by the provisioned product. The default value is ``UPDATE`` if nothing is specified.

      Applicable only to a ``CFN_STACKSET`` provisioned product type.

        CREATE

      Creates a new stack instance in the stack set represented by the provisioned product. In this
      case, only new stack instances are created based on accounts and regions; if new ProductId or
      ProvisioningArtifactID are passed, they will be ignored.

        UPDATE

      Updates the stack set represented by the provisioned product and also its stack instances.

        DELETE

      Deletes a stack instance in the stack set represented by the provisioned product.
    """


_ClientUpdateProvisionedProductResponseRecordDetailRecordErrorsTypeDef = TypedDict(
    "_ClientUpdateProvisionedProductResponseRecordDetailRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)


class ClientUpdateProvisionedProductResponseRecordDetailRecordErrorsTypeDef(
    _ClientUpdateProvisionedProductResponseRecordDetailRecordErrorsTypeDef
):
    """
    Type definition for `ClientUpdateProvisionedProductResponseRecordDetail` `RecordErrors`

    The error code and description resulting from an operation.

    - **Code** *(string) --*

      The numeric value of the error.

    - **Description** *(string) --*

      The description of the error.
    """


_ClientUpdateProvisionedProductResponseRecordDetailRecordTagsTypeDef = TypedDict(
    "_ClientUpdateProvisionedProductResponseRecordDetailRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientUpdateProvisionedProductResponseRecordDetailRecordTagsTypeDef(
    _ClientUpdateProvisionedProductResponseRecordDetailRecordTagsTypeDef
):
    """
    Type definition for `ClientUpdateProvisionedProductResponseRecordDetail` `RecordTags`

    Information about a tag, which is a key-value pair.

    - **Key** *(string) --*

      The key for this tag.

    - **Value** *(string) --*

      The value for this tag.
    """


_ClientUpdateProvisionedProductResponseRecordDetailTypeDef = TypedDict(
    "_ClientUpdateProvisionedProductResponseRecordDetailTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": str,
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[
            ClientUpdateProvisionedProductResponseRecordDetailRecordErrorsTypeDef
        ],
        "RecordTags": List[
            ClientUpdateProvisionedProductResponseRecordDetailRecordTagsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateProvisionedProductResponseRecordDetailTypeDef(
    _ClientUpdateProvisionedProductResponseRecordDetailTypeDef
):
    """
    Type definition for `ClientUpdateProvisionedProductResponse` `RecordDetail`

    Information about the result of the request.

    - **RecordId** *(string) --*

      The identifier of the record.

    - **ProvisionedProductName** *(string) --*

      The user-friendly name of the provisioned product.

    - **Status** *(string) --*

      The status of the provisioned product.

      * ``CREATED`` - The request was created but the operation has not started.

      * ``IN_PROGRESS`` - The requested operation is in progress.

      * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested
      operation failed and some remediation is occurring. For example, a rollback.

      * ``SUCCEEDED`` - The requested operation has successfully completed.

      * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using the
      error messages returned.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **UpdatedTime** *(datetime) --*

      The time when the record was last updated.

    - **ProvisionedProductType** *(string) --*

      The type of provisioned product. The supported values are ``CFN_STACK`` and
      ``CFN_STACKSET`` .

    - **RecordType** *(string) --*

      The record type.

      * ``PROVISION_PRODUCT``

      * ``UPDATE_PROVISIONED_PRODUCT``

      * ``TERMINATE_PROVISIONED_PRODUCT``

    - **ProvisionedProductId** *(string) --*

      The identifier of the provisioned product.

    - **ProductId** *(string) --*

      The product identifier.

    - **ProvisioningArtifactId** *(string) --*

      The identifier of the provisioning artifact.

    - **PathId** *(string) --*

      The path identifier.

    - **RecordErrors** *(list) --*

      The errors that occurred.

      - *(dict) --*

        The error code and description resulting from an operation.

        - **Code** *(string) --*

          The numeric value of the error.

        - **Description** *(string) --*

          The description of the error.

    - **RecordTags** *(list) --*

      One or more tags.

      - *(dict) --*

        Information about a tag, which is a key-value pair.

        - **Key** *(string) --*

          The key for this tag.

        - **Value** *(string) --*

          The value for this tag.
    """


_ClientUpdateProvisionedProductResponseTypeDef = TypedDict(
    "_ClientUpdateProvisionedProductResponseTypeDef",
    {"RecordDetail": ClientUpdateProvisionedProductResponseRecordDetailTypeDef},
    total=False,
)


class ClientUpdateProvisionedProductResponseTypeDef(
    _ClientUpdateProvisionedProductResponseTypeDef
):
    """
    Type definition for `ClientUpdateProvisionedProduct` `Response`

    - **RecordDetail** *(dict) --*

      Information about the result of the request.

      - **RecordId** *(string) --*

        The identifier of the record.

      - **ProvisionedProductName** *(string) --*

        The user-friendly name of the provisioned product.

      - **Status** *(string) --*

        The status of the provisioned product.

        * ``CREATED`` - The request was created but the operation has not started.

        * ``IN_PROGRESS`` - The requested operation is in progress.

        * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested
        operation failed and some remediation is occurring. For example, a rollback.

        * ``SUCCEEDED`` - The requested operation has successfully completed.

        * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using the
        error messages returned.

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

      - **UpdatedTime** *(datetime) --*

        The time when the record was last updated.

      - **ProvisionedProductType** *(string) --*

        The type of provisioned product. The supported values are ``CFN_STACK`` and
        ``CFN_STACKSET`` .

      - **RecordType** *(string) --*

        The record type.

        * ``PROVISION_PRODUCT``

        * ``UPDATE_PROVISIONED_PRODUCT``

        * ``TERMINATE_PROVISIONED_PRODUCT``

      - **ProvisionedProductId** *(string) --*

        The identifier of the provisioned product.

      - **ProductId** *(string) --*

        The product identifier.

      - **ProvisioningArtifactId** *(string) --*

        The identifier of the provisioning artifact.

      - **PathId** *(string) --*

        The path identifier.

      - **RecordErrors** *(list) --*

        The errors that occurred.

        - *(dict) --*

          The error code and description resulting from an operation.

          - **Code** *(string) --*

            The numeric value of the error.

          - **Description** *(string) --*

            The description of the error.

      - **RecordTags** *(list) --*

        One or more tags.

        - *(dict) --*

          Information about a tag, which is a key-value pair.

          - **Key** *(string) --*

            The key for this tag.

          - **Value** *(string) --*

            The value for this tag.
    """


_ClientUpdateProvisionedProductTagsTypeDef = TypedDict(
    "_ClientUpdateProvisionedProductTagsTypeDef", {"Key": str, "Value": str}
)


class ClientUpdateProvisionedProductTagsTypeDef(
    _ClientUpdateProvisionedProductTagsTypeDef
):
    """
    Type definition for `ClientUpdateProvisionedProduct` `Tags`

    Information about a tag. A tag is a key-value pair. Tags are propagated to the resources
    created when provisioning a product.

    - **Key** *(string) --* **[REQUIRED]**

      The tag key.

    - **Value** *(string) --* **[REQUIRED]**

      The value for this key.
    """


_ClientUpdateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef = TypedDict(
    "_ClientUpdateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Type": str,
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": str,
    },
    total=False,
)


class ClientUpdateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef(
    _ClientUpdateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef
):
    """
    Type definition for `ClientUpdateProvisioningArtifactResponse` `ProvisioningArtifactDetail`

    Information about the provisioning artifact.

    - **Id** *(string) --*

      The identifier of the provisioning artifact.

    - **Name** *(string) --*

      The name of the provisioning artifact.

    - **Description** *(string) --*

      The description of the provisioning artifact.

    - **Type** *(string) --*

      The type of provisioning artifact.

      * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template

      * ``MARKETPLACE_AMI`` - AWS Marketplace AMI

      * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **Active** *(boolean) --*

      Indicates whether the product version is active.

    - **Guidance** *(string) --*

      Information set by the administrator to provide guidance to end users about which
      provisioning artifacts to use.
    """


_ClientUpdateProvisioningArtifactResponseTypeDef = TypedDict(
    "_ClientUpdateProvisioningArtifactResponseTypeDef",
    {
        "ProvisioningArtifactDetail": ClientUpdateProvisioningArtifactResponseProvisioningArtifactDetailTypeDef,
        "Info": Dict[str, str],
        "Status": str,
    },
    total=False,
)


class ClientUpdateProvisioningArtifactResponseTypeDef(
    _ClientUpdateProvisioningArtifactResponseTypeDef
):
    """
    Type definition for `ClientUpdateProvisioningArtifact` `Response`

    - **ProvisioningArtifactDetail** *(dict) --*

      Information about the provisioning artifact.

      - **Id** *(string) --*

        The identifier of the provisioning artifact.

      - **Name** *(string) --*

        The name of the provisioning artifact.

      - **Description** *(string) --*

        The description of the provisioning artifact.

      - **Type** *(string) --*

        The type of provisioning artifact.

        * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template

        * ``MARKETPLACE_AMI`` - AWS Marketplace AMI

        * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

      - **Active** *(boolean) --*

        Indicates whether the product version is active.

      - **Guidance** *(string) --*

        Information set by the administrator to provide guidance to end users about which
        provisioning artifacts to use.

    - **Info** *(dict) --*

      The URL of the CloudFormation template in Amazon S3.

      - *(string) --*

        - *(string) --*

    - **Status** *(string) --*

      The status of the current request.
    """


_ClientUpdateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef = TypedDict(
    "_ClientUpdateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)


class ClientUpdateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef(
    _ClientUpdateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef
):
    """
    Type definition for `ClientUpdateServiceActionResponseServiceActionDetail` `ServiceActionSummary`

    Summary information about the self-service action.

    - **Id** *(string) --*

      The self-service action identifier.

    - **Name** *(string) --*

      The self-service action name.

    - **Description** *(string) --*

      The self-service action description.

    - **DefinitionType** *(string) --*

      The self-service action definition type. For example, ``SSM_AUTOMATION`` .
    """


_ClientUpdateServiceActionResponseServiceActionDetailTypeDef = TypedDict(
    "_ClientUpdateServiceActionResponseServiceActionDetailTypeDef",
    {
        "ServiceActionSummary": ClientUpdateServiceActionResponseServiceActionDetailServiceActionSummaryTypeDef,
        "Definition": Dict[str, str],
    },
    total=False,
)


class ClientUpdateServiceActionResponseServiceActionDetailTypeDef(
    _ClientUpdateServiceActionResponseServiceActionDetailTypeDef
):
    """
    Type definition for `ClientUpdateServiceActionResponse` `ServiceActionDetail`

    Detailed information about the self-service action.

    - **ServiceActionSummary** *(dict) --*

      Summary information about the self-service action.

      - **Id** *(string) --*

        The self-service action identifier.

      - **Name** *(string) --*

        The self-service action name.

      - **Description** *(string) --*

        The self-service action description.

      - **DefinitionType** *(string) --*

        The self-service action definition type. For example, ``SSM_AUTOMATION`` .

    - **Definition** *(dict) --*

      A map that defines the self-service action.

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateServiceActionResponseTypeDef = TypedDict(
    "_ClientUpdateServiceActionResponseTypeDef",
    {
        "ServiceActionDetail": ClientUpdateServiceActionResponseServiceActionDetailTypeDef
    },
    total=False,
)


class ClientUpdateServiceActionResponseTypeDef(
    _ClientUpdateServiceActionResponseTypeDef
):
    """
    Type definition for `ClientUpdateServiceAction` `Response`

    - **ServiceActionDetail** *(dict) --*

      Detailed information about the self-service action.

      - **ServiceActionSummary** *(dict) --*

        Summary information about the self-service action.

        - **Id** *(string) --*

          The self-service action identifier.

        - **Name** *(string) --*

          The self-service action name.

        - **Description** *(string) --*

          The self-service action description.

        - **DefinitionType** *(string) --*

          The self-service action definition type. For example, ``SSM_AUTOMATION`` .

      - **Definition** *(dict) --*

        A map that defines the self-service action.

        - *(string) --*

          - *(string) --*
    """


_ClientUpdateTagOptionResponseTagOptionDetailTypeDef = TypedDict(
    "_ClientUpdateTagOptionResponseTagOptionDetailTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)


class ClientUpdateTagOptionResponseTagOptionDetailTypeDef(
    _ClientUpdateTagOptionResponseTagOptionDetailTypeDef
):
    """
    Type definition for `ClientUpdateTagOptionResponse` `TagOptionDetail`

    Information about the TagOption.

    - **Key** *(string) --*

      The TagOption key.

    - **Value** *(string) --*

      The TagOption value.

    - **Active** *(boolean) --*

      The TagOption active state.

    - **Id** *(string) --*

      The TagOption identifier.
    """


_ClientUpdateTagOptionResponseTypeDef = TypedDict(
    "_ClientUpdateTagOptionResponseTypeDef",
    {"TagOptionDetail": ClientUpdateTagOptionResponseTagOptionDetailTypeDef},
    total=False,
)


class ClientUpdateTagOptionResponseTypeDef(_ClientUpdateTagOptionResponseTypeDef):
    """
    Type definition for `ClientUpdateTagOption` `Response`

    - **TagOptionDetail** *(dict) --*

      Information about the TagOption.

      - **Key** *(string) --*

        The TagOption key.

      - **Value** *(string) --*

        The TagOption value.

      - **Active** *(boolean) --*

        The TagOption active state.

      - **Id** *(string) --*

        The TagOption identifier.
    """


_ListAcceptedPortfolioSharesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAcceptedPortfolioSharesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAcceptedPortfolioSharesPaginatePaginationConfigTypeDef(
    _ListAcceptedPortfolioSharesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAcceptedPortfolioSharesPaginate` `PaginationConfig`

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


_ListAcceptedPortfolioSharesPaginateResponsePortfolioDetailsTypeDef = TypedDict(
    "_ListAcceptedPortfolioSharesPaginateResponsePortfolioDetailsTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)


class ListAcceptedPortfolioSharesPaginateResponsePortfolioDetailsTypeDef(
    _ListAcceptedPortfolioSharesPaginateResponsePortfolioDetailsTypeDef
):
    """
    Type definition for `ListAcceptedPortfolioSharesPaginateResponse` `PortfolioDetails`

    Information about a portfolio.

    - **Id** *(string) --*

      The portfolio identifier.

    - **ARN** *(string) --*

      The ARN assigned to the portfolio.

    - **DisplayName** *(string) --*

      The name to use for display purposes.

    - **Description** *(string) --*

      The description of the portfolio.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **ProviderName** *(string) --*

      The name of the portfolio provider.
    """


_ListAcceptedPortfolioSharesPaginateResponseTypeDef = TypedDict(
    "_ListAcceptedPortfolioSharesPaginateResponseTypeDef",
    {
        "PortfolioDetails": List[
            ListAcceptedPortfolioSharesPaginateResponsePortfolioDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListAcceptedPortfolioSharesPaginateResponseTypeDef(
    _ListAcceptedPortfolioSharesPaginateResponseTypeDef
):
    """
    Type definition for `ListAcceptedPortfolioSharesPaginate` `Response`

    - **PortfolioDetails** *(list) --*

      Information about the portfolios.

      - *(dict) --*

        Information about a portfolio.

        - **Id** *(string) --*

          The portfolio identifier.

        - **ARN** *(string) --*

          The ARN assigned to the portfolio.

        - **DisplayName** *(string) --*

          The name to use for display purposes.

        - **Description** *(string) --*

          The description of the portfolio.

        - **CreatedTime** *(datetime) --*

          The UTC time stamp of the creation time.

        - **ProviderName** *(string) --*

          The name of the portfolio provider.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListConstraintsForPortfolioPaginatePaginationConfigTypeDef = TypedDict(
    "_ListConstraintsForPortfolioPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListConstraintsForPortfolioPaginatePaginationConfigTypeDef(
    _ListConstraintsForPortfolioPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListConstraintsForPortfolioPaginate` `PaginationConfig`

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


_ListConstraintsForPortfolioPaginateResponseConstraintDetailsTypeDef = TypedDict(
    "_ListConstraintsForPortfolioPaginateResponseConstraintDetailsTypeDef",
    {"ConstraintId": str, "Type": str, "Description": str, "Owner": str},
    total=False,
)


class ListConstraintsForPortfolioPaginateResponseConstraintDetailsTypeDef(
    _ListConstraintsForPortfolioPaginateResponseConstraintDetailsTypeDef
):
    """
    Type definition for `ListConstraintsForPortfolioPaginateResponse` `ConstraintDetails`

    Information about a constraint.

    - **ConstraintId** *(string) --*

      The identifier of the constraint.

    - **Type** *(string) --*

      The type of constraint.

      * ``LAUNCH``

      * ``NOTIFICATION``

      * STACKSET

      * ``TEMPLATE``

    - **Description** *(string) --*

      The description of the constraint.

    - **Owner** *(string) --*

      The owner of the constraint.
    """


_ListConstraintsForPortfolioPaginateResponseTypeDef = TypedDict(
    "_ListConstraintsForPortfolioPaginateResponseTypeDef",
    {
        "ConstraintDetails": List[
            ListConstraintsForPortfolioPaginateResponseConstraintDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListConstraintsForPortfolioPaginateResponseTypeDef(
    _ListConstraintsForPortfolioPaginateResponseTypeDef
):
    """
    Type definition for `ListConstraintsForPortfolioPaginate` `Response`

    - **ConstraintDetails** *(list) --*

      Information about the constraints.

      - *(dict) --*

        Information about a constraint.

        - **ConstraintId** *(string) --*

          The identifier of the constraint.

        - **Type** *(string) --*

          The type of constraint.

          * ``LAUNCH``

          * ``NOTIFICATION``

          * STACKSET

          * ``TEMPLATE``

        - **Description** *(string) --*

          The description of the constraint.

        - **Owner** *(string) --*

          The owner of the constraint.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListLaunchPathsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListLaunchPathsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListLaunchPathsPaginatePaginationConfigTypeDef(
    _ListLaunchPathsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListLaunchPathsPaginate` `PaginationConfig`

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


_ListLaunchPathsPaginateResponseLaunchPathSummariesConstraintSummariesTypeDef = TypedDict(
    "_ListLaunchPathsPaginateResponseLaunchPathSummariesConstraintSummariesTypeDef",
    {"Type": str, "Description": str},
    total=False,
)


class ListLaunchPathsPaginateResponseLaunchPathSummariesConstraintSummariesTypeDef(
    _ListLaunchPathsPaginateResponseLaunchPathSummariesConstraintSummariesTypeDef
):
    """
    Type definition for `ListLaunchPathsPaginateResponseLaunchPathSummaries` `ConstraintSummaries`

    Summary information about a constraint.

    - **Type** *(string) --*

      The type of constraint.

      * ``LAUNCH``

      * ``NOTIFICATION``

      * STACKSET

      * ``TEMPLATE``

    - **Description** *(string) --*

      The description of the constraint.
    """


_ListLaunchPathsPaginateResponseLaunchPathSummariesTagsTypeDef = TypedDict(
    "_ListLaunchPathsPaginateResponseLaunchPathSummariesTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListLaunchPathsPaginateResponseLaunchPathSummariesTagsTypeDef(
    _ListLaunchPathsPaginateResponseLaunchPathSummariesTagsTypeDef
):
    """
    Type definition for `ListLaunchPathsPaginateResponseLaunchPathSummaries` `Tags`

    Information about a tag. A tag is a key-value pair. Tags are propagated to the
    resources created when provisioning a product.

    - **Key** *(string) --*

      The tag key.

    - **Value** *(string) --*

      The value for this key.
    """


_ListLaunchPathsPaginateResponseLaunchPathSummariesTypeDef = TypedDict(
    "_ListLaunchPathsPaginateResponseLaunchPathSummariesTypeDef",
    {
        "Id": str,
        "ConstraintSummaries": List[
            ListLaunchPathsPaginateResponseLaunchPathSummariesConstraintSummariesTypeDef
        ],
        "Tags": List[ListLaunchPathsPaginateResponseLaunchPathSummariesTagsTypeDef],
        "Name": str,
    },
    total=False,
)


class ListLaunchPathsPaginateResponseLaunchPathSummariesTypeDef(
    _ListLaunchPathsPaginateResponseLaunchPathSummariesTypeDef
):
    """
    Type definition for `ListLaunchPathsPaginateResponse` `LaunchPathSummaries`

    Summary information about a product path for a user.

    - **Id** *(string) --*

      The identifier of the product path.

    - **ConstraintSummaries** *(list) --*

      The constraints on the portfolio-product relationship.

      - *(dict) --*

        Summary information about a constraint.

        - **Type** *(string) --*

          The type of constraint.

          * ``LAUNCH``

          * ``NOTIFICATION``

          * STACKSET

          * ``TEMPLATE``

        - **Description** *(string) --*

          The description of the constraint.

    - **Tags** *(list) --*

      The tags associated with this product path.

      - *(dict) --*

        Information about a tag. A tag is a key-value pair. Tags are propagated to the
        resources created when provisioning a product.

        - **Key** *(string) --*

          The tag key.

        - **Value** *(string) --*

          The value for this key.

    - **Name** *(string) --*

      The name of the portfolio to which the user was assigned.
    """


_ListLaunchPathsPaginateResponseTypeDef = TypedDict(
    "_ListLaunchPathsPaginateResponseTypeDef",
    {
        "LaunchPathSummaries": List[
            ListLaunchPathsPaginateResponseLaunchPathSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListLaunchPathsPaginateResponseTypeDef(_ListLaunchPathsPaginateResponseTypeDef):
    """
    Type definition for `ListLaunchPathsPaginate` `Response`

    - **LaunchPathSummaries** *(list) --*

      Information about the launch path.

      - *(dict) --*

        Summary information about a product path for a user.

        - **Id** *(string) --*

          The identifier of the product path.

        - **ConstraintSummaries** *(list) --*

          The constraints on the portfolio-product relationship.

          - *(dict) --*

            Summary information about a constraint.

            - **Type** *(string) --*

              The type of constraint.

              * ``LAUNCH``

              * ``NOTIFICATION``

              * STACKSET

              * ``TEMPLATE``

            - **Description** *(string) --*

              The description of the constraint.

        - **Tags** *(list) --*

          The tags associated with this product path.

          - *(dict) --*

            Information about a tag. A tag is a key-value pair. Tags are propagated to the
            resources created when provisioning a product.

            - **Key** *(string) --*

              The tag key.

            - **Value** *(string) --*

              The value for this key.

        - **Name** *(string) --*

          The name of the portfolio to which the user was assigned.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListOrganizationPortfolioAccessPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOrganizationPortfolioAccessPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListOrganizationPortfolioAccessPaginatePaginationConfigTypeDef(
    _ListOrganizationPortfolioAccessPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListOrganizationPortfolioAccessPaginate` `PaginationConfig`

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


_ListOrganizationPortfolioAccessPaginateResponseOrganizationNodesTypeDef = TypedDict(
    "_ListOrganizationPortfolioAccessPaginateResponseOrganizationNodesTypeDef",
    {"Type": str, "Value": str},
    total=False,
)


class ListOrganizationPortfolioAccessPaginateResponseOrganizationNodesTypeDef(
    _ListOrganizationPortfolioAccessPaginateResponseOrganizationNodesTypeDef
):
    """
    Type definition for `ListOrganizationPortfolioAccessPaginateResponse` `OrganizationNodes`

    Information about the organization node.

    - **Type** *(string) --*

      The organization node type.

    - **Value** *(string) --*

      The identifier of the organization node.
    """


_ListOrganizationPortfolioAccessPaginateResponseTypeDef = TypedDict(
    "_ListOrganizationPortfolioAccessPaginateResponseTypeDef",
    {
        "OrganizationNodes": List[
            ListOrganizationPortfolioAccessPaginateResponseOrganizationNodesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListOrganizationPortfolioAccessPaginateResponseTypeDef(
    _ListOrganizationPortfolioAccessPaginateResponseTypeDef
):
    """
    Type definition for `ListOrganizationPortfolioAccessPaginate` `Response`

    - **OrganizationNodes** *(list) --*

      Displays information about the organization nodes.

      - *(dict) --*

        Information about the organization node.

        - **Type** *(string) --*

          The organization node type.

        - **Value** *(string) --*

          The identifier of the organization node.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListPortfoliosForProductPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPortfoliosForProductPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPortfoliosForProductPaginatePaginationConfigTypeDef(
    _ListPortfoliosForProductPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPortfoliosForProductPaginate` `PaginationConfig`

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


_ListPortfoliosForProductPaginateResponsePortfolioDetailsTypeDef = TypedDict(
    "_ListPortfoliosForProductPaginateResponsePortfolioDetailsTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)


class ListPortfoliosForProductPaginateResponsePortfolioDetailsTypeDef(
    _ListPortfoliosForProductPaginateResponsePortfolioDetailsTypeDef
):
    """
    Type definition for `ListPortfoliosForProductPaginateResponse` `PortfolioDetails`

    Information about a portfolio.

    - **Id** *(string) --*

      The portfolio identifier.

    - **ARN** *(string) --*

      The ARN assigned to the portfolio.

    - **DisplayName** *(string) --*

      The name to use for display purposes.

    - **Description** *(string) --*

      The description of the portfolio.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **ProviderName** *(string) --*

      The name of the portfolio provider.
    """


_ListPortfoliosForProductPaginateResponseTypeDef = TypedDict(
    "_ListPortfoliosForProductPaginateResponseTypeDef",
    {
        "PortfolioDetails": List[
            ListPortfoliosForProductPaginateResponsePortfolioDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListPortfoliosForProductPaginateResponseTypeDef(
    _ListPortfoliosForProductPaginateResponseTypeDef
):
    """
    Type definition for `ListPortfoliosForProductPaginate` `Response`

    - **PortfolioDetails** *(list) --*

      Information about the portfolios.

      - *(dict) --*

        Information about a portfolio.

        - **Id** *(string) --*

          The portfolio identifier.

        - **ARN** *(string) --*

          The ARN assigned to the portfolio.

        - **DisplayName** *(string) --*

          The name to use for display purposes.

        - **Description** *(string) --*

          The description of the portfolio.

        - **CreatedTime** *(datetime) --*

          The UTC time stamp of the creation time.

        - **ProviderName** *(string) --*

          The name of the portfolio provider.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListPortfoliosPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPortfoliosPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPortfoliosPaginatePaginationConfigTypeDef(
    _ListPortfoliosPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPortfoliosPaginate` `PaginationConfig`

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


_ListPortfoliosPaginateResponsePortfolioDetailsTypeDef = TypedDict(
    "_ListPortfoliosPaginateResponsePortfolioDetailsTypeDef",
    {
        "Id": str,
        "ARN": str,
        "DisplayName": str,
        "Description": str,
        "CreatedTime": datetime,
        "ProviderName": str,
    },
    total=False,
)


class ListPortfoliosPaginateResponsePortfolioDetailsTypeDef(
    _ListPortfoliosPaginateResponsePortfolioDetailsTypeDef
):
    """
    Type definition for `ListPortfoliosPaginateResponse` `PortfolioDetails`

    Information about a portfolio.

    - **Id** *(string) --*

      The portfolio identifier.

    - **ARN** *(string) --*

      The ARN assigned to the portfolio.

    - **DisplayName** *(string) --*

      The name to use for display purposes.

    - **Description** *(string) --*

      The description of the portfolio.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **ProviderName** *(string) --*

      The name of the portfolio provider.
    """


_ListPortfoliosPaginateResponseTypeDef = TypedDict(
    "_ListPortfoliosPaginateResponseTypeDef",
    {
        "PortfolioDetails": List[ListPortfoliosPaginateResponsePortfolioDetailsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListPortfoliosPaginateResponseTypeDef(_ListPortfoliosPaginateResponseTypeDef):
    """
    Type definition for `ListPortfoliosPaginate` `Response`

    - **PortfolioDetails** *(list) --*

      Information about the portfolios.

      - *(dict) --*

        Information about a portfolio.

        - **Id** *(string) --*

          The portfolio identifier.

        - **ARN** *(string) --*

          The ARN assigned to the portfolio.

        - **DisplayName** *(string) --*

          The name to use for display purposes.

        - **Description** *(string) --*

          The description of the portfolio.

        - **CreatedTime** *(datetime) --*

          The UTC time stamp of the creation time.

        - **ProviderName** *(string) --*

          The name of the portfolio provider.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListPrincipalsForPortfolioPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPrincipalsForPortfolioPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPrincipalsForPortfolioPaginatePaginationConfigTypeDef(
    _ListPrincipalsForPortfolioPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPrincipalsForPortfolioPaginate` `PaginationConfig`

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


_ListPrincipalsForPortfolioPaginateResponsePrincipalsTypeDef = TypedDict(
    "_ListPrincipalsForPortfolioPaginateResponsePrincipalsTypeDef",
    {"PrincipalARN": str, "PrincipalType": str},
    total=False,
)


class ListPrincipalsForPortfolioPaginateResponsePrincipalsTypeDef(
    _ListPrincipalsForPortfolioPaginateResponsePrincipalsTypeDef
):
    """
    Type definition for `ListPrincipalsForPortfolioPaginateResponse` `Principals`

    Information about a principal.

    - **PrincipalARN** *(string) --*

      The ARN of the principal (IAM user, role, or group).

    - **PrincipalType** *(string) --*

      The principal type. The supported value is ``IAM`` .
    """


_ListPrincipalsForPortfolioPaginateResponseTypeDef = TypedDict(
    "_ListPrincipalsForPortfolioPaginateResponseTypeDef",
    {
        "Principals": List[ListPrincipalsForPortfolioPaginateResponsePrincipalsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListPrincipalsForPortfolioPaginateResponseTypeDef(
    _ListPrincipalsForPortfolioPaginateResponseTypeDef
):
    """
    Type definition for `ListPrincipalsForPortfolioPaginate` `Response`

    - **Principals** *(list) --*

      The IAM principals (users or roles) associated with the portfolio.

      - *(dict) --*

        Information about a principal.

        - **PrincipalARN** *(string) --*

          The ARN of the principal (IAM user, role, or group).

        - **PrincipalType** *(string) --*

          The principal type. The supported value is ``IAM`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListProvisionedProductPlansPaginateAccessLevelFilterTypeDef = TypedDict(
    "_ListProvisionedProductPlansPaginateAccessLevelFilterTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListProvisionedProductPlansPaginateAccessLevelFilterTypeDef(
    _ListProvisionedProductPlansPaginateAccessLevelFilterTypeDef
):
    """
    Type definition for `ListProvisionedProductPlansPaginate` `AccessLevelFilter`

    The access level to use to obtain results. The default is ``User`` .

    - **Key** *(string) --*

      The access level.

      * ``Account`` - Filter results based on the account.

      * ``Role`` - Filter results based on the federated role of the specified user.

      * ``User`` - Filter results based on the specified user.

    - **Value** *(string) --*

      The user to which the access level applies. The only supported value is ``Self`` .
    """


_ListProvisionedProductPlansPaginatePaginationConfigTypeDef = TypedDict(
    "_ListProvisionedProductPlansPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListProvisionedProductPlansPaginatePaginationConfigTypeDef(
    _ListProvisionedProductPlansPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListProvisionedProductPlansPaginate` `PaginationConfig`

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


_ListProvisionedProductPlansPaginateResponseProvisionedProductPlansTypeDef = TypedDict(
    "_ListProvisionedProductPlansPaginateResponseProvisionedProductPlansTypeDef",
    {
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionProductName": str,
        "PlanType": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)


class ListProvisionedProductPlansPaginateResponseProvisionedProductPlansTypeDef(
    _ListProvisionedProductPlansPaginateResponseProvisionedProductPlansTypeDef
):
    """
    Type definition for `ListProvisionedProductPlansPaginateResponse` `ProvisionedProductPlans`

    Summary information about a plan.

    - **PlanName** *(string) --*

      The name of the plan.

    - **PlanId** *(string) --*

      The plan identifier.

    - **ProvisionProductId** *(string) --*

      The product identifier.

    - **ProvisionProductName** *(string) --*

      The user-friendly name of the provisioned product.

    - **PlanType** *(string) --*

      The plan type.

    - **ProvisioningArtifactId** *(string) --*

      The identifier of the provisioning artifact.
    """


_ListProvisionedProductPlansPaginateResponseTypeDef = TypedDict(
    "_ListProvisionedProductPlansPaginateResponseTypeDef",
    {
        "ProvisionedProductPlans": List[
            ListProvisionedProductPlansPaginateResponseProvisionedProductPlansTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListProvisionedProductPlansPaginateResponseTypeDef(
    _ListProvisionedProductPlansPaginateResponseTypeDef
):
    """
    Type definition for `ListProvisionedProductPlansPaginate` `Response`

    - **ProvisionedProductPlans** *(list) --*

      Information about the plans.

      - *(dict) --*

        Summary information about a plan.

        - **PlanName** *(string) --*

          The name of the plan.

        - **PlanId** *(string) --*

          The plan identifier.

        - **ProvisionProductId** *(string) --*

          The product identifier.

        - **ProvisionProductName** *(string) --*

          The user-friendly name of the provisioned product.

        - **PlanType** *(string) --*

          The plan type.

        - **ProvisioningArtifactId** *(string) --*

          The identifier of the provisioning artifact.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListProvisioningArtifactsForServiceActionPaginatePaginationConfigTypeDef = TypedDict(
    "_ListProvisioningArtifactsForServiceActionPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListProvisioningArtifactsForServiceActionPaginatePaginationConfigTypeDef(
    _ListProvisioningArtifactsForServiceActionPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListProvisioningArtifactsForServiceActionPaginate` `PaginationConfig`

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


_ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProductViewSummaryTypeDef = TypedDict(
    "_ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": str,
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProductViewSummaryTypeDef(
    _ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProductViewSummaryTypeDef
):
    """
    Type definition for `ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViews` `ProductViewSummary`

    Summary information about a product view.

    - **Id** *(string) --*

      The product view identifier.

    - **ProductId** *(string) --*

      The product identifier.

    - **Name** *(string) --*

      The name of the product.

    - **Owner** *(string) --*

      The owner of the product. Contact the product administrator for the significance of
      this value.

    - **ShortDescription** *(string) --*

      Short description of the product.

    - **Type** *(string) --*

      The product type. Contact the product administrator for the significance of this value.
      If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

    - **Distributor** *(string) --*

      The distributor of the product. Contact the product administrator for the significance
      of this value.

    - **HasDefaultPath** *(boolean) --*

      Indicates whether the product has a default path. If the product does not have a
      default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,
      ListLaunchPaths is not required, and the output of  ProductViewSummary can be used
      directly with  DescribeProvisioningParameters .

    - **SupportEmail** *(string) --*

      The email contact information to obtain support for this Product.

    - **SupportDescription** *(string) --*

      The description of the support for this Product.

    - **SupportUrl** *(string) --*

      The URL information to obtain support for this Product.
    """


_ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProvisioningArtifactTypeDef = TypedDict(
    "_ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProvisioningArtifactTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "CreatedTime": datetime,
        "Guidance": str,
    },
    total=False,
)


class ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProvisioningArtifactTypeDef(
    _ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProvisioningArtifactTypeDef
):
    """
    Type definition for `ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViews` `ProvisioningArtifact`

    Information about a provisioning artifact. A provisioning artifact is also known as a
    product version.

    - **Id** *(string) --*

      The identifier of the provisioning artifact.

    - **Name** *(string) --*

      The name of the provisioning artifact.

    - **Description** *(string) --*

      The description of the provisioning artifact.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **Guidance** *(string) --*

      Information set by the administrator to provide guidance to end users about which
      provisioning artifacts to use.
    """


_ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsTypeDef = TypedDict(
    "_ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsTypeDef",
    {
        "ProductViewSummary": ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProductViewSummaryTypeDef,
        "ProvisioningArtifact": ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsProvisioningArtifactTypeDef,
    },
    total=False,
)


class ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsTypeDef(
    _ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsTypeDef
):
    """
    Type definition for `ListProvisioningArtifactsForServiceActionPaginateResponse` `ProvisioningArtifactViews`

    An object that contains summary information about a product view and a provisioning
    artifact.

    - **ProductViewSummary** *(dict) --*

      Summary information about a product view.

      - **Id** *(string) --*

        The product view identifier.

      - **ProductId** *(string) --*

        The product identifier.

      - **Name** *(string) --*

        The name of the product.

      - **Owner** *(string) --*

        The owner of the product. Contact the product administrator for the significance of
        this value.

      - **ShortDescription** *(string) --*

        Short description of the product.

      - **Type** *(string) --*

        The product type. Contact the product administrator for the significance of this value.
        If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

      - **Distributor** *(string) --*

        The distributor of the product. Contact the product administrator for the significance
        of this value.

      - **HasDefaultPath** *(boolean) --*

        Indicates whether the product has a default path. If the product does not have a
        default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,
        ListLaunchPaths is not required, and the output of  ProductViewSummary can be used
        directly with  DescribeProvisioningParameters .

      - **SupportEmail** *(string) --*

        The email contact information to obtain support for this Product.

      - **SupportDescription** *(string) --*

        The description of the support for this Product.

      - **SupportUrl** *(string) --*

        The URL information to obtain support for this Product.

    - **ProvisioningArtifact** *(dict) --*

      Information about a provisioning artifact. A provisioning artifact is also known as a
      product version.

      - **Id** *(string) --*

        The identifier of the provisioning artifact.

      - **Name** *(string) --*

        The name of the provisioning artifact.

      - **Description** *(string) --*

        The description of the provisioning artifact.

      - **CreatedTime** *(datetime) --*

        The UTC time stamp of the creation time.

      - **Guidance** *(string) --*

        Information set by the administrator to provide guidance to end users about which
        provisioning artifacts to use.
    """


_ListProvisioningArtifactsForServiceActionPaginateResponseTypeDef = TypedDict(
    "_ListProvisioningArtifactsForServiceActionPaginateResponseTypeDef",
    {
        "ProvisioningArtifactViews": List[
            ListProvisioningArtifactsForServiceActionPaginateResponseProvisioningArtifactViewsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListProvisioningArtifactsForServiceActionPaginateResponseTypeDef(
    _ListProvisioningArtifactsForServiceActionPaginateResponseTypeDef
):
    """
    Type definition for `ListProvisioningArtifactsForServiceActionPaginate` `Response`

    - **ProvisioningArtifactViews** *(list) --*

      An array of objects with information about product views and provisioning artifacts.

      - *(dict) --*

        An object that contains summary information about a product view and a provisioning
        artifact.

        - **ProductViewSummary** *(dict) --*

          Summary information about a product view.

          - **Id** *(string) --*

            The product view identifier.

          - **ProductId** *(string) --*

            The product identifier.

          - **Name** *(string) --*

            The name of the product.

          - **Owner** *(string) --*

            The owner of the product. Contact the product administrator for the significance of
            this value.

          - **ShortDescription** *(string) --*

            Short description of the product.

          - **Type** *(string) --*

            The product type. Contact the product administrator for the significance of this value.
            If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

          - **Distributor** *(string) --*

            The distributor of the product. Contact the product administrator for the significance
            of this value.

          - **HasDefaultPath** *(boolean) --*

            Indicates whether the product has a default path. If the product does not have a
            default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,
            ListLaunchPaths is not required, and the output of  ProductViewSummary can be used
            directly with  DescribeProvisioningParameters .

          - **SupportEmail** *(string) --*

            The email contact information to obtain support for this Product.

          - **SupportDescription** *(string) --*

            The description of the support for this Product.

          - **SupportUrl** *(string) --*

            The URL information to obtain support for this Product.

        - **ProvisioningArtifact** *(dict) --*

          Information about a provisioning artifact. A provisioning artifact is also known as a
          product version.

          - **Id** *(string) --*

            The identifier of the provisioning artifact.

          - **Name** *(string) --*

            The name of the provisioning artifact.

          - **Description** *(string) --*

            The description of the provisioning artifact.

          - **CreatedTime** *(datetime) --*

            The UTC time stamp of the creation time.

          - **Guidance** *(string) --*

            Information set by the administrator to provide guidance to end users about which
            provisioning artifacts to use.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListRecordHistoryPaginateAccessLevelFilterTypeDef = TypedDict(
    "_ListRecordHistoryPaginateAccessLevelFilterTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListRecordHistoryPaginateAccessLevelFilterTypeDef(
    _ListRecordHistoryPaginateAccessLevelFilterTypeDef
):
    """
    Type definition for `ListRecordHistoryPaginate` `AccessLevelFilter`

    The access level to use to obtain results. The default is ``User`` .

    - **Key** *(string) --*

      The access level.

      * ``Account`` - Filter results based on the account.

      * ``Role`` - Filter results based on the federated role of the specified user.

      * ``User`` - Filter results based on the specified user.

    - **Value** *(string) --*

      The user to which the access level applies. The only supported value is ``Self`` .
    """


_ListRecordHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRecordHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRecordHistoryPaginatePaginationConfigTypeDef(
    _ListRecordHistoryPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRecordHistoryPaginate` `PaginationConfig`

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


_ListRecordHistoryPaginateResponseRecordDetailsRecordErrorsTypeDef = TypedDict(
    "_ListRecordHistoryPaginateResponseRecordDetailsRecordErrorsTypeDef",
    {"Code": str, "Description": str},
    total=False,
)


class ListRecordHistoryPaginateResponseRecordDetailsRecordErrorsTypeDef(
    _ListRecordHistoryPaginateResponseRecordDetailsRecordErrorsTypeDef
):
    """
    Type definition for `ListRecordHistoryPaginateResponseRecordDetails` `RecordErrors`

    The error code and description resulting from an operation.

    - **Code** *(string) --*

      The numeric value of the error.

    - **Description** *(string) --*

      The description of the error.
    """


_ListRecordHistoryPaginateResponseRecordDetailsRecordTagsTypeDef = TypedDict(
    "_ListRecordHistoryPaginateResponseRecordDetailsRecordTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListRecordHistoryPaginateResponseRecordDetailsRecordTagsTypeDef(
    _ListRecordHistoryPaginateResponseRecordDetailsRecordTagsTypeDef
):
    """
    Type definition for `ListRecordHistoryPaginateResponseRecordDetails` `RecordTags`

    Information about a tag, which is a key-value pair.

    - **Key** *(string) --*

      The key for this tag.

    - **Value** *(string) --*

      The value for this tag.
    """


_ListRecordHistoryPaginateResponseRecordDetailsTypeDef = TypedDict(
    "_ListRecordHistoryPaginateResponseRecordDetailsTypeDef",
    {
        "RecordId": str,
        "ProvisionedProductName": str,
        "Status": str,
        "CreatedTime": datetime,
        "UpdatedTime": datetime,
        "ProvisionedProductType": str,
        "RecordType": str,
        "ProvisionedProductId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PathId": str,
        "RecordErrors": List[
            ListRecordHistoryPaginateResponseRecordDetailsRecordErrorsTypeDef
        ],
        "RecordTags": List[
            ListRecordHistoryPaginateResponseRecordDetailsRecordTagsTypeDef
        ],
    },
    total=False,
)


class ListRecordHistoryPaginateResponseRecordDetailsTypeDef(
    _ListRecordHistoryPaginateResponseRecordDetailsTypeDef
):
    """
    Type definition for `ListRecordHistoryPaginateResponse` `RecordDetails`

    Information about a request operation.

    - **RecordId** *(string) --*

      The identifier of the record.

    - **ProvisionedProductName** *(string) --*

      The user-friendly name of the provisioned product.

    - **Status** *(string) --*

      The status of the provisioned product.

      * ``CREATED`` - The request was created but the operation has not started.

      * ``IN_PROGRESS`` - The requested operation is in progress.

      * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested
      operation failed and some remediation is occurring. For example, a rollback.

      * ``SUCCEEDED`` - The requested operation has successfully completed.

      * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using
      the error messages returned.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **UpdatedTime** *(datetime) --*

      The time when the record was last updated.

    - **ProvisionedProductType** *(string) --*

      The type of provisioned product. The supported values are ``CFN_STACK`` and
      ``CFN_STACKSET`` .

    - **RecordType** *(string) --*

      The record type.

      * ``PROVISION_PRODUCT``

      * ``UPDATE_PROVISIONED_PRODUCT``

      * ``TERMINATE_PROVISIONED_PRODUCT``

    - **ProvisionedProductId** *(string) --*

      The identifier of the provisioned product.

    - **ProductId** *(string) --*

      The product identifier.

    - **ProvisioningArtifactId** *(string) --*

      The identifier of the provisioning artifact.

    - **PathId** *(string) --*

      The path identifier.

    - **RecordErrors** *(list) --*

      The errors that occurred.

      - *(dict) --*

        The error code and description resulting from an operation.

        - **Code** *(string) --*

          The numeric value of the error.

        - **Description** *(string) --*

          The description of the error.

    - **RecordTags** *(list) --*

      One or more tags.

      - *(dict) --*

        Information about a tag, which is a key-value pair.

        - **Key** *(string) --*

          The key for this tag.

        - **Value** *(string) --*

          The value for this tag.
    """


_ListRecordHistoryPaginateResponseTypeDef = TypedDict(
    "_ListRecordHistoryPaginateResponseTypeDef",
    {
        "RecordDetails": List[ListRecordHistoryPaginateResponseRecordDetailsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListRecordHistoryPaginateResponseTypeDef(
    _ListRecordHistoryPaginateResponseTypeDef
):
    """
    Type definition for `ListRecordHistoryPaginate` `Response`

    - **RecordDetails** *(list) --*

      The records, in reverse chronological order.

      - *(dict) --*

        Information about a request operation.

        - **RecordId** *(string) --*

          The identifier of the record.

        - **ProvisionedProductName** *(string) --*

          The user-friendly name of the provisioned product.

        - **Status** *(string) --*

          The status of the provisioned product.

          * ``CREATED`` - The request was created but the operation has not started.

          * ``IN_PROGRESS`` - The requested operation is in progress.

          * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested
          operation failed and some remediation is occurring. For example, a rollback.

          * ``SUCCEEDED`` - The requested operation has successfully completed.

          * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using
          the error messages returned.

        - **CreatedTime** *(datetime) --*

          The UTC time stamp of the creation time.

        - **UpdatedTime** *(datetime) --*

          The time when the record was last updated.

        - **ProvisionedProductType** *(string) --*

          The type of provisioned product. The supported values are ``CFN_STACK`` and
          ``CFN_STACKSET`` .

        - **RecordType** *(string) --*

          The record type.

          * ``PROVISION_PRODUCT``

          * ``UPDATE_PROVISIONED_PRODUCT``

          * ``TERMINATE_PROVISIONED_PRODUCT``

        - **ProvisionedProductId** *(string) --*

          The identifier of the provisioned product.

        - **ProductId** *(string) --*

          The product identifier.

        - **ProvisioningArtifactId** *(string) --*

          The identifier of the provisioning artifact.

        - **PathId** *(string) --*

          The path identifier.

        - **RecordErrors** *(list) --*

          The errors that occurred.

          - *(dict) --*

            The error code and description resulting from an operation.

            - **Code** *(string) --*

              The numeric value of the error.

            - **Description** *(string) --*

              The description of the error.

        - **RecordTags** *(list) --*

          One or more tags.

          - *(dict) --*

            Information about a tag, which is a key-value pair.

            - **Key** *(string) --*

              The key for this tag.

            - **Value** *(string) --*

              The value for this tag.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListRecordHistoryPaginateSearchFilterTypeDef = TypedDict(
    "_ListRecordHistoryPaginateSearchFilterTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListRecordHistoryPaginateSearchFilterTypeDef(
    _ListRecordHistoryPaginateSearchFilterTypeDef
):
    """
    Type definition for `ListRecordHistoryPaginate` `SearchFilter`

    The search filter to scope the results.

    - **Key** *(string) --*

      The filter key.

      * ``product`` - Filter results based on the specified product identifier.

      * ``provisionedproduct`` - Filter results based on the provisioned product identifier.

    - **Value** *(string) --*

      The filter value.
    """


_ListResourcesForTagOptionPaginatePaginationConfigTypeDef = TypedDict(
    "_ListResourcesForTagOptionPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListResourcesForTagOptionPaginatePaginationConfigTypeDef(
    _ListResourcesForTagOptionPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListResourcesForTagOptionPaginate` `PaginationConfig`

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


_ListResourcesForTagOptionPaginateResponseResourceDetailsTypeDef = TypedDict(
    "_ListResourcesForTagOptionPaginateResponseResourceDetailsTypeDef",
    {"Id": str, "ARN": str, "Name": str, "Description": str, "CreatedTime": datetime},
    total=False,
)


class ListResourcesForTagOptionPaginateResponseResourceDetailsTypeDef(
    _ListResourcesForTagOptionPaginateResponseResourceDetailsTypeDef
):
    """
    Type definition for `ListResourcesForTagOptionPaginateResponse` `ResourceDetails`

    Information about a resource.

    - **Id** *(string) --*

      The identifier of the resource.

    - **ARN** *(string) --*

      The ARN of the resource.

    - **Name** *(string) --*

      The name of the resource.

    - **Description** *(string) --*

      The description of the resource.

    - **CreatedTime** *(datetime) --*

      The creation time of the resource.
    """


_ListResourcesForTagOptionPaginateResponseTypeDef = TypedDict(
    "_ListResourcesForTagOptionPaginateResponseTypeDef",
    {
        "ResourceDetails": List[
            ListResourcesForTagOptionPaginateResponseResourceDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListResourcesForTagOptionPaginateResponseTypeDef(
    _ListResourcesForTagOptionPaginateResponseTypeDef
):
    """
    Type definition for `ListResourcesForTagOptionPaginate` `Response`

    - **ResourceDetails** *(list) --*

      Information about the resources.

      - *(dict) --*

        Information about a resource.

        - **Id** *(string) --*

          The identifier of the resource.

        - **ARN** *(string) --*

          The ARN of the resource.

        - **Name** *(string) --*

          The name of the resource.

        - **Description** *(string) --*

          The description of the resource.

        - **CreatedTime** *(datetime) --*

          The creation time of the resource.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListServiceActionsForProvisioningArtifactPaginatePaginationConfigTypeDef = TypedDict(
    "_ListServiceActionsForProvisioningArtifactPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListServiceActionsForProvisioningArtifactPaginatePaginationConfigTypeDef(
    _ListServiceActionsForProvisioningArtifactPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListServiceActionsForProvisioningArtifactPaginate` `PaginationConfig`

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


_ListServiceActionsForProvisioningArtifactPaginateResponseServiceActionSummariesTypeDef = TypedDict(
    "_ListServiceActionsForProvisioningArtifactPaginateResponseServiceActionSummariesTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)


class ListServiceActionsForProvisioningArtifactPaginateResponseServiceActionSummariesTypeDef(
    _ListServiceActionsForProvisioningArtifactPaginateResponseServiceActionSummariesTypeDef
):
    """
    Type definition for `ListServiceActionsForProvisioningArtifactPaginateResponse` `ServiceActionSummaries`

    Detailed information about the self-service action.

    - **Id** *(string) --*

      The self-service action identifier.

    - **Name** *(string) --*

      The self-service action name.

    - **Description** *(string) --*

      The self-service action description.

    - **DefinitionType** *(string) --*

      The self-service action definition type. For example, ``SSM_AUTOMATION`` .
    """


_ListServiceActionsForProvisioningArtifactPaginateResponseTypeDef = TypedDict(
    "_ListServiceActionsForProvisioningArtifactPaginateResponseTypeDef",
    {
        "ServiceActionSummaries": List[
            ListServiceActionsForProvisioningArtifactPaginateResponseServiceActionSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListServiceActionsForProvisioningArtifactPaginateResponseTypeDef(
    _ListServiceActionsForProvisioningArtifactPaginateResponseTypeDef
):
    """
    Type definition for `ListServiceActionsForProvisioningArtifactPaginate` `Response`

    - **ServiceActionSummaries** *(list) --*

      An object containing information about the self-service actions associated with the
      provisioning artifact.

      - *(dict) --*

        Detailed information about the self-service action.

        - **Id** *(string) --*

          The self-service action identifier.

        - **Name** *(string) --*

          The self-service action name.

        - **Description** *(string) --*

          The self-service action description.

        - **DefinitionType** *(string) --*

          The self-service action definition type. For example, ``SSM_AUTOMATION`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListServiceActionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListServiceActionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListServiceActionsPaginatePaginationConfigTypeDef(
    _ListServiceActionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListServiceActionsPaginate` `PaginationConfig`

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


_ListServiceActionsPaginateResponseServiceActionSummariesTypeDef = TypedDict(
    "_ListServiceActionsPaginateResponseServiceActionSummariesTypeDef",
    {"Id": str, "Name": str, "Description": str, "DefinitionType": str},
    total=False,
)


class ListServiceActionsPaginateResponseServiceActionSummariesTypeDef(
    _ListServiceActionsPaginateResponseServiceActionSummariesTypeDef
):
    """
    Type definition for `ListServiceActionsPaginateResponse` `ServiceActionSummaries`

    Detailed information about the self-service action.

    - **Id** *(string) --*

      The self-service action identifier.

    - **Name** *(string) --*

      The self-service action name.

    - **Description** *(string) --*

      The self-service action description.

    - **DefinitionType** *(string) --*

      The self-service action definition type. For example, ``SSM_AUTOMATION`` .
    """


_ListServiceActionsPaginateResponseTypeDef = TypedDict(
    "_ListServiceActionsPaginateResponseTypeDef",
    {
        "ServiceActionSummaries": List[
            ListServiceActionsPaginateResponseServiceActionSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListServiceActionsPaginateResponseTypeDef(
    _ListServiceActionsPaginateResponseTypeDef
):
    """
    Type definition for `ListServiceActionsPaginate` `Response`

    - **ServiceActionSummaries** *(list) --*

      An object containing information about the service actions associated with the provisioning
      artifact.

      - *(dict) --*

        Detailed information about the self-service action.

        - **Id** *(string) --*

          The self-service action identifier.

        - **Name** *(string) --*

          The self-service action name.

        - **Description** *(string) --*

          The self-service action description.

        - **DefinitionType** *(string) --*

          The self-service action definition type. For example, ``SSM_AUTOMATION`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListTagOptionsPaginateFiltersTypeDef = TypedDict(
    "_ListTagOptionsPaginateFiltersTypeDef",
    {"Key": str, "Value": str, "Active": bool},
    total=False,
)


class ListTagOptionsPaginateFiltersTypeDef(_ListTagOptionsPaginateFiltersTypeDef):
    """
    Type definition for `ListTagOptionsPaginate` `Filters`

    The search filters. If no search filters are specified, the output includes all TagOptions.

    - **Key** *(string) --*

      The TagOption key.

    - **Value** *(string) --*

      The TagOption value.

    - **Active** *(boolean) --*

      The active state.
    """


_ListTagOptionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagOptionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTagOptionsPaginatePaginationConfigTypeDef(
    _ListTagOptionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTagOptionsPaginate` `PaginationConfig`

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


_ListTagOptionsPaginateResponseTagOptionDetailsTypeDef = TypedDict(
    "_ListTagOptionsPaginateResponseTagOptionDetailsTypeDef",
    {"Key": str, "Value": str, "Active": bool, "Id": str},
    total=False,
)


class ListTagOptionsPaginateResponseTagOptionDetailsTypeDef(
    _ListTagOptionsPaginateResponseTagOptionDetailsTypeDef
):
    """
    Type definition for `ListTagOptionsPaginateResponse` `TagOptionDetails`

    Information about a TagOption.

    - **Key** *(string) --*

      The TagOption key.

    - **Value** *(string) --*

      The TagOption value.

    - **Active** *(boolean) --*

      The TagOption active state.

    - **Id** *(string) --*

      The TagOption identifier.
    """


_ListTagOptionsPaginateResponseTypeDef = TypedDict(
    "_ListTagOptionsPaginateResponseTypeDef",
    {
        "TagOptionDetails": List[ListTagOptionsPaginateResponseTagOptionDetailsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListTagOptionsPaginateResponseTypeDef(_ListTagOptionsPaginateResponseTypeDef):
    """
    Type definition for `ListTagOptionsPaginate` `Response`

    - **TagOptionDetails** *(list) --*

      Information about the TagOptions.

      - *(dict) --*

        Information about a TagOption.

        - **Key** *(string) --*

          The TagOption key.

        - **Value** *(string) --*

          The TagOption value.

        - **Active** *(boolean) --*

          The TagOption active state.

        - **Id** *(string) --*

          The TagOption identifier.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ScanProvisionedProductsPaginateAccessLevelFilterTypeDef = TypedDict(
    "_ScanProvisionedProductsPaginateAccessLevelFilterTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ScanProvisionedProductsPaginateAccessLevelFilterTypeDef(
    _ScanProvisionedProductsPaginateAccessLevelFilterTypeDef
):
    """
    Type definition for `ScanProvisionedProductsPaginate` `AccessLevelFilter`

    The access level to use to obtain results. The default is ``User`` .

    - **Key** *(string) --*

      The access level.

      * ``Account`` - Filter results based on the account.

      * ``Role`` - Filter results based on the federated role of the specified user.

      * ``User`` - Filter results based on the specified user.

    - **Value** *(string) --*

      The user to which the access level applies. The only supported value is ``Self`` .
    """


_ScanProvisionedProductsPaginatePaginationConfigTypeDef = TypedDict(
    "_ScanProvisionedProductsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ScanProvisionedProductsPaginatePaginationConfigTypeDef(
    _ScanProvisionedProductsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ScanProvisionedProductsPaginate` `PaginationConfig`

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


_ScanProvisionedProductsPaginateResponseProvisionedProductsTypeDef = TypedDict(
    "_ScanProvisionedProductsPaginateResponseProvisionedProductsTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": str,
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
    total=False,
)


class ScanProvisionedProductsPaginateResponseProvisionedProductsTypeDef(
    _ScanProvisionedProductsPaginateResponseProvisionedProductsTypeDef
):
    """
    Type definition for `ScanProvisionedProductsPaginateResponse` `ProvisionedProducts`

    Information about a provisioned product.

    - **Name** *(string) --*

      The user-friendly name of the provisioned product.

    - **Arn** *(string) --*

      The ARN of the provisioned product.

    - **Type** *(string) --*

      The type of provisioned product. The supported values are ``CFN_STACK`` and
      ``CFN_STACKSET`` .

    - **Id** *(string) --*

      The identifier of the provisioned product.

    - **Status** *(string) --*

      The current status of the provisioned product.

      * ``AVAILABLE`` - Stable state, ready to perform any operation. The most recent operation
      succeeded and completed.

      * ``UNDER_CHANGE`` - Transitive state. Operations performed might not have valid results.
      Wait for an ``AVAILABLE`` status before performing operations.

      * ``TAINTED`` - Stable state, ready to perform any operation. The stack has completed the
      requested operation but is not exactly what was requested. For example, a request to
      update to a new version failed and the stack rolled back to the current version.

      * ``ERROR`` - An unexpected error occurred. The provisioned product exists but the stack
      is not running. For example, CloudFormation received a parameter value that was not valid
      and could not launch the stack.

      * ``PLAN_IN_PROGRESS`` - Transitive state. The plan operations were performed to
      provision a new product, but resources have not yet been created. After reviewing the
      list of resources to be created, execute the plan. Wait for an ``AVAILABLE`` status
      before performing operations.

    - **StatusMessage** *(string) --*

      The current status message of the provisioned product.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.

    - **IdempotencyToken** *(string) --*

      A unique identifier that you provide to ensure idempotency. If multiple requests differ
      only by the idempotency token, the same response is returned for each repeated request.

    - **LastRecordId** *(string) --*

      The record identifier of the last request performed on this provisioned product.

    - **ProductId** *(string) --*

      The product identifier. For example, ``prod-abcdzk7xy33qa`` .

    - **ProvisioningArtifactId** *(string) --*

      The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .
    """


_ScanProvisionedProductsPaginateResponseTypeDef = TypedDict(
    "_ScanProvisionedProductsPaginateResponseTypeDef",
    {
        "ProvisionedProducts": List[
            ScanProvisionedProductsPaginateResponseProvisionedProductsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ScanProvisionedProductsPaginateResponseTypeDef(
    _ScanProvisionedProductsPaginateResponseTypeDef
):
    """
    Type definition for `ScanProvisionedProductsPaginate` `Response`

    - **ProvisionedProducts** *(list) --*

      Information about the provisioned products.

      - *(dict) --*

        Information about a provisioned product.

        - **Name** *(string) --*

          The user-friendly name of the provisioned product.

        - **Arn** *(string) --*

          The ARN of the provisioned product.

        - **Type** *(string) --*

          The type of provisioned product. The supported values are ``CFN_STACK`` and
          ``CFN_STACKSET`` .

        - **Id** *(string) --*

          The identifier of the provisioned product.

        - **Status** *(string) --*

          The current status of the provisioned product.

          * ``AVAILABLE`` - Stable state, ready to perform any operation. The most recent operation
          succeeded and completed.

          * ``UNDER_CHANGE`` - Transitive state. Operations performed might not have valid results.
          Wait for an ``AVAILABLE`` status before performing operations.

          * ``TAINTED`` - Stable state, ready to perform any operation. The stack has completed the
          requested operation but is not exactly what was requested. For example, a request to
          update to a new version failed and the stack rolled back to the current version.

          * ``ERROR`` - An unexpected error occurred. The provisioned product exists but the stack
          is not running. For example, CloudFormation received a parameter value that was not valid
          and could not launch the stack.

          * ``PLAN_IN_PROGRESS`` - Transitive state. The plan operations were performed to
          provision a new product, but resources have not yet been created. After reviewing the
          list of resources to be created, execute the plan. Wait for an ``AVAILABLE`` status
          before performing operations.

        - **StatusMessage** *(string) --*

          The current status message of the provisioned product.

        - **CreatedTime** *(datetime) --*

          The UTC time stamp of the creation time.

        - **IdempotencyToken** *(string) --*

          A unique identifier that you provide to ensure idempotency. If multiple requests differ
          only by the idempotency token, the same response is returned for each repeated request.

        - **LastRecordId** *(string) --*

          The record identifier of the last request performed on this provisioned product.

        - **ProductId** *(string) --*

          The product identifier. For example, ``prod-abcdzk7xy33qa`` .

        - **ProvisioningArtifactId** *(string) --*

          The identifier of the provisioning artifact. For example, ``pa-4abcdjnxjj6ne`` .

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_SearchProductsAsAdminPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchProductsAsAdminPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchProductsAsAdminPaginatePaginationConfigTypeDef(
    _SearchProductsAsAdminPaginatePaginationConfigTypeDef
):
    """
    Type definition for `SearchProductsAsAdminPaginate` `PaginationConfig`

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


_SearchProductsAsAdminPaginateResponseProductViewDetailsProductViewSummaryTypeDef = TypedDict(
    "_SearchProductsAsAdminPaginateResponseProductViewDetailsProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": str,
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class SearchProductsAsAdminPaginateResponseProductViewDetailsProductViewSummaryTypeDef(
    _SearchProductsAsAdminPaginateResponseProductViewDetailsProductViewSummaryTypeDef
):
    """
    Type definition for `SearchProductsAsAdminPaginateResponseProductViewDetails` `ProductViewSummary`

    Summary information about the product view.

    - **Id** *(string) --*

      The product view identifier.

    - **ProductId** *(string) --*

      The product identifier.

    - **Name** *(string) --*

      The name of the product.

    - **Owner** *(string) --*

      The owner of the product. Contact the product administrator for the significance of
      this value.

    - **ShortDescription** *(string) --*

      Short description of the product.

    - **Type** *(string) --*

      The product type. Contact the product administrator for the significance of this value.
      If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

    - **Distributor** *(string) --*

      The distributor of the product. Contact the product administrator for the significance
      of this value.

    - **HasDefaultPath** *(boolean) --*

      Indicates whether the product has a default path. If the product does not have a
      default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,
      ListLaunchPaths is not required, and the output of  ProductViewSummary can be used
      directly with  DescribeProvisioningParameters .

    - **SupportEmail** *(string) --*

      The email contact information to obtain support for this Product.

    - **SupportDescription** *(string) --*

      The description of the support for this Product.

    - **SupportUrl** *(string) --*

      The URL information to obtain support for this Product.
    """


_SearchProductsAsAdminPaginateResponseProductViewDetailsTypeDef = TypedDict(
    "_SearchProductsAsAdminPaginateResponseProductViewDetailsTypeDef",
    {
        "ProductViewSummary": SearchProductsAsAdminPaginateResponseProductViewDetailsProductViewSummaryTypeDef,
        "Status": str,
        "ProductARN": str,
        "CreatedTime": datetime,
    },
    total=False,
)


class SearchProductsAsAdminPaginateResponseProductViewDetailsTypeDef(
    _SearchProductsAsAdminPaginateResponseProductViewDetailsTypeDef
):
    """
    Type definition for `SearchProductsAsAdminPaginateResponse` `ProductViewDetails`

    Information about a product view.

    - **ProductViewSummary** *(dict) --*

      Summary information about the product view.

      - **Id** *(string) --*

        The product view identifier.

      - **ProductId** *(string) --*

        The product identifier.

      - **Name** *(string) --*

        The name of the product.

      - **Owner** *(string) --*

        The owner of the product. Contact the product administrator for the significance of
        this value.

      - **ShortDescription** *(string) --*

        Short description of the product.

      - **Type** *(string) --*

        The product type. Contact the product administrator for the significance of this value.
        If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

      - **Distributor** *(string) --*

        The distributor of the product. Contact the product administrator for the significance
        of this value.

      - **HasDefaultPath** *(boolean) --*

        Indicates whether the product has a default path. If the product does not have a
        default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,
        ListLaunchPaths is not required, and the output of  ProductViewSummary can be used
        directly with  DescribeProvisioningParameters .

      - **SupportEmail** *(string) --*

        The email contact information to obtain support for this Product.

      - **SupportDescription** *(string) --*

        The description of the support for this Product.

      - **SupportUrl** *(string) --*

        The URL information to obtain support for this Product.

    - **Status** *(string) --*

      The status of the product.

      * ``AVAILABLE`` - The product is ready for use.

      * ``CREATING`` - Product creation has started; the product is not ready for use.

      * ``FAILED`` - An action failed.

    - **ProductARN** *(string) --*

      The ARN of the product.

    - **CreatedTime** *(datetime) --*

      The UTC time stamp of the creation time.
    """


_SearchProductsAsAdminPaginateResponseTypeDef = TypedDict(
    "_SearchProductsAsAdminPaginateResponseTypeDef",
    {
        "ProductViewDetails": List[
            SearchProductsAsAdminPaginateResponseProductViewDetailsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class SearchProductsAsAdminPaginateResponseTypeDef(
    _SearchProductsAsAdminPaginateResponseTypeDef
):
    """
    Type definition for `SearchProductsAsAdminPaginate` `Response`

    - **ProductViewDetails** *(list) --*

      Information about the product views.

      - *(dict) --*

        Information about a product view.

        - **ProductViewSummary** *(dict) --*

          Summary information about the product view.

          - **Id** *(string) --*

            The product view identifier.

          - **ProductId** *(string) --*

            The product identifier.

          - **Name** *(string) --*

            The name of the product.

          - **Owner** *(string) --*

            The owner of the product. Contact the product administrator for the significance of
            this value.

          - **ShortDescription** *(string) --*

            Short description of the product.

          - **Type** *(string) --*

            The product type. Contact the product administrator for the significance of this value.
            If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

          - **Distributor** *(string) --*

            The distributor of the product. Contact the product administrator for the significance
            of this value.

          - **HasDefaultPath** *(boolean) --*

            Indicates whether the product has a default path. If the product does not have a
            default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,
            ListLaunchPaths is not required, and the output of  ProductViewSummary can be used
            directly with  DescribeProvisioningParameters .

          - **SupportEmail** *(string) --*

            The email contact information to obtain support for this Product.

          - **SupportDescription** *(string) --*

            The description of the support for this Product.

          - **SupportUrl** *(string) --*

            The URL information to obtain support for this Product.

        - **Status** *(string) --*

          The status of the product.

          * ``AVAILABLE`` - The product is ready for use.

          * ``CREATING`` - Product creation has started; the product is not ready for use.

          * ``FAILED`` - An action failed.

        - **ProductARN** *(string) --*

          The ARN of the product.

        - **CreatedTime** *(datetime) --*

          The UTC time stamp of the creation time.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """

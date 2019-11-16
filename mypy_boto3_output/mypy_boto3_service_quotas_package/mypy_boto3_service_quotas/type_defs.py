"Main interface for service-quotas type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientGetAssociationForServiceQuotaTemplateResponseTypeDef",
    "ClientGetAwsDefaultServiceQuotaResponseQuotaErrorReasonTypeDef",
    "ClientGetAwsDefaultServiceQuotaResponseQuotaPeriodTypeDef",
    "ClientGetAwsDefaultServiceQuotaResponseQuotaUsageMetricTypeDef",
    "ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef",
    "ClientGetAwsDefaultServiceQuotaResponseTypeDef",
    "ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef",
    "ClientGetRequestedServiceQuotaChangeResponseTypeDef",
    "ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef",
    "ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef",
    "ClientGetServiceQuotaResponseQuotaErrorReasonTypeDef",
    "ClientGetServiceQuotaResponseQuotaPeriodTypeDef",
    "ClientGetServiceQuotaResponseQuotaUsageMetricTypeDef",
    "ClientGetServiceQuotaResponseQuotaTypeDef",
    "ClientGetServiceQuotaResponseTypeDef",
    "ClientListAwsDefaultServiceQuotasResponseQuotasErrorReasonTypeDef",
    "ClientListAwsDefaultServiceQuotasResponseQuotasPeriodTypeDef",
    "ClientListAwsDefaultServiceQuotasResponseQuotasUsageMetricTypeDef",
    "ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef",
    "ClientListAwsDefaultServiceQuotasResponseTypeDef",
    "ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef",
    "ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    "ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef",
    "ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    "ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef",
    "ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    "ClientListServiceQuotasResponseQuotasErrorReasonTypeDef",
    "ClientListServiceQuotasResponseQuotasPeriodTypeDef",
    "ClientListServiceQuotasResponseQuotasUsageMetricTypeDef",
    "ClientListServiceQuotasResponseQuotasTypeDef",
    "ClientListServiceQuotasResponseTypeDef",
    "ClientListServicesResponseServicesTypeDef",
    "ClientListServicesResponseTypeDef",
    "ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef",
    "ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef",
    "ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef",
    "ClientRequestServiceQuotaIncreaseResponseTypeDef",
    "ListAWSDefaultServiceQuotasPaginatePaginationConfigTypeDef",
    "ListAWSDefaultServiceQuotasPaginateResponseQuotasErrorReasonTypeDef",
    "ListAWSDefaultServiceQuotasPaginateResponseQuotasPeriodTypeDef",
    "ListAWSDefaultServiceQuotasPaginateResponseQuotasUsageMetricTypeDef",
    "ListAWSDefaultServiceQuotasPaginateResponseQuotasTypeDef",
    "ListAWSDefaultServiceQuotasPaginateResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaPaginatePaginationConfigTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseRequestedQuotasTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryPaginatePaginationConfigTypeDef",
    "ListRequestedServiceQuotaChangeHistoryPaginateResponseRequestedQuotasTypeDef",
    "ListRequestedServiceQuotaChangeHistoryPaginateResponseTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplatePaginatePaginationConfigTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseTypeDef",
    "ListServiceQuotasPaginatePaginationConfigTypeDef",
    "ListServiceQuotasPaginateResponseQuotasErrorReasonTypeDef",
    "ListServiceQuotasPaginateResponseQuotasPeriodTypeDef",
    "ListServiceQuotasPaginateResponseQuotasUsageMetricTypeDef",
    "ListServiceQuotasPaginateResponseQuotasTypeDef",
    "ListServiceQuotasPaginateResponseTypeDef",
    "ListServicesPaginatePaginationConfigTypeDef",
    "ListServicesPaginateResponseServicesTypeDef",
    "ListServicesPaginateResponseTypeDef",
)


_ClientGetAssociationForServiceQuotaTemplateResponseTypeDef = TypedDict(
    "_ClientGetAssociationForServiceQuotaTemplateResponseTypeDef",
    {"ServiceQuotaTemplateAssociationStatus": str},
    total=False,
)


class ClientGetAssociationForServiceQuotaTemplateResponseTypeDef(
    _ClientGetAssociationForServiceQuotaTemplateResponseTypeDef
):
    """
    Type definition for `ClientGetAssociationForServiceQuotaTemplate` `Response`

    - **ServiceQuotaTemplateAssociationStatus** *(string) --*

      Specifies whether the template is ``ASSOCIATED`` or ``DISASSOCIATED`` . If the template is
      ``ASSOCIATED`` , then it requests service quota increases for all new accounts created in
      your organization.
    """


_ClientGetAwsDefaultServiceQuotaResponseQuotaErrorReasonTypeDef = TypedDict(
    "_ClientGetAwsDefaultServiceQuotaResponseQuotaErrorReasonTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientGetAwsDefaultServiceQuotaResponseQuotaErrorReasonTypeDef(
    _ClientGetAwsDefaultServiceQuotaResponseQuotaErrorReasonTypeDef
):
    """
    Type definition for `ClientGetAwsDefaultServiceQuotaResponseQuota` `ErrorReason`

    Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

    - **ErrorCode** *(string) --*

      Service Quotas returns the following error values.

       ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have permission
       to call the service or service quota. To resolve the error, you need permission to
       access the service or service quota.

       ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is throttling
       Service Quotas.

       ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has availability
       issues.

       ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
       Quotas.

    - **ErrorMessage** *(string) --*

      The error message that provides more detail.
    """


_ClientGetAwsDefaultServiceQuotaResponseQuotaPeriodTypeDef = TypedDict(
    "_ClientGetAwsDefaultServiceQuotaResponseQuotaPeriodTypeDef",
    {"PeriodValue": int, "PeriodUnit": str},
    total=False,
)


class ClientGetAwsDefaultServiceQuotaResponseQuotaPeriodTypeDef(
    _ClientGetAwsDefaultServiceQuotaResponseQuotaPeriodTypeDef
):
    """
    Type definition for `ClientGetAwsDefaultServiceQuotaResponseQuota` `Period`

    Identifies the unit and value of how time is measured.

    - **PeriodValue** *(integer) --*

      The value of a period.

    - **PeriodUnit** *(string) --*

      The time unit of a period.
    """


_ClientGetAwsDefaultServiceQuotaResponseQuotaUsageMetricTypeDef = TypedDict(
    "_ClientGetAwsDefaultServiceQuotaResponseQuotaUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)


class ClientGetAwsDefaultServiceQuotaResponseQuotaUsageMetricTypeDef(
    _ClientGetAwsDefaultServiceQuotaResponseQuotaUsageMetricTypeDef
):
    """
    Type definition for `ClientGetAwsDefaultServiceQuotaResponseQuota` `UsageMetric`

    Specifies the details about the measurement.

    - **MetricNamespace** *(string) --*

      The namespace of the metric. The namespace is a container for CloudWatch metrics. You can
      specify a name for the namespace when you create a metric.

    - **MetricName** *(string) --*

      The name of the CloudWatch metric that measures usage of a service quota. This is a
      required field.

    - **MetricDimensions** *(dict) --*

      A dimension is a name/value pair that is part of the identity of a metric. Every metric
      has specific characteristics that describe it, and you can think of dimensions as
      categories for those characteristics. These dimensions are part of the CloudWatch Metric
      Identity that measures usage against a particular service quota.

      - *(string) --*

        - *(string) --*

    - **MetricStatisticRecommendation** *(string) --*

      Statistics are metric data aggregations over specified periods of time. This is the
      recommended statistic to use when comparing usage in the CloudWatch Metric against your
      Service Quota.
    """


_ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef = TypedDict(
    "_ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": ClientGetAwsDefaultServiceQuotaResponseQuotaUsageMetricTypeDef,
        "Period": ClientGetAwsDefaultServiceQuotaResponseQuotaPeriodTypeDef,
        "ErrorReason": ClientGetAwsDefaultServiceQuotaResponseQuotaErrorReasonTypeDef,
    },
    total=False,
)


class ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef(
    _ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef
):
    """
    Type definition for `ClientGetAwsDefaultServiceQuotaResponse` `Quota`

    Returns the  ServiceQuota object which contains all values for a quota.

    - **ServiceCode** *(string) --*

      Specifies the service that you want to use.

    - **ServiceName** *(string) --*

      The name of the AWS service specified in the increase request.

    - **QuotaArn** *(string) --*

      The Amazon Resource Name (ARN) of the service quota.

    - **QuotaCode** *(string) --*

      The code identifier for the service quota specified.

    - **QuotaName** *(string) --*

      The name identifier of the service quota.

    - **Value** *(float) --*

      The value of service quota.

    - **Unit** *(string) --*

      The unit of measurement for the value of the service quota.

    - **Adjustable** *(boolean) --*

      Specifies if the quota value can be increased.

    - **GlobalQuota** *(boolean) --*

      Specifies if the quota is global.

    - **UsageMetric** *(dict) --*

      Specifies the details about the measurement.

      - **MetricNamespace** *(string) --*

        The namespace of the metric. The namespace is a container for CloudWatch metrics. You can
        specify a name for the namespace when you create a metric.

      - **MetricName** *(string) --*

        The name of the CloudWatch metric that measures usage of a service quota. This is a
        required field.

      - **MetricDimensions** *(dict) --*

        A dimension is a name/value pair that is part of the identity of a metric. Every metric
        has specific characteristics that describe it, and you can think of dimensions as
        categories for those characteristics. These dimensions are part of the CloudWatch Metric
        Identity that measures usage against a particular service quota.

        - *(string) --*

          - *(string) --*

      - **MetricStatisticRecommendation** *(string) --*

        Statistics are metric data aggregations over specified periods of time. This is the
        recommended statistic to use when comparing usage in the CloudWatch Metric against your
        Service Quota.

    - **Period** *(dict) --*

      Identifies the unit and value of how time is measured.

      - **PeriodValue** *(integer) --*

        The value of a period.

      - **PeriodUnit** *(string) --*

        The time unit of a period.

    - **ErrorReason** *(dict) --*

      Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

      - **ErrorCode** *(string) --*

        Service Quotas returns the following error values.

         ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have permission
         to call the service or service quota. To resolve the error, you need permission to
         access the service or service quota.

         ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is throttling
         Service Quotas.

         ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has availability
         issues.

         ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
         Quotas.

      - **ErrorMessage** *(string) --*

        The error message that provides more detail.
    """


_ClientGetAwsDefaultServiceQuotaResponseTypeDef = TypedDict(
    "_ClientGetAwsDefaultServiceQuotaResponseTypeDef",
    {"Quota": ClientGetAwsDefaultServiceQuotaResponseQuotaTypeDef},
    total=False,
)


class ClientGetAwsDefaultServiceQuotaResponseTypeDef(
    _ClientGetAwsDefaultServiceQuotaResponseTypeDef
):
    """
    Type definition for `ClientGetAwsDefaultServiceQuota` `Response`

    - **Quota** *(dict) --*

      Returns the  ServiceQuota object which contains all values for a quota.

      - **ServiceCode** *(string) --*

        Specifies the service that you want to use.

      - **ServiceName** *(string) --*

        The name of the AWS service specified in the increase request.

      - **QuotaArn** *(string) --*

        The Amazon Resource Name (ARN) of the service quota.

      - **QuotaCode** *(string) --*

        The code identifier for the service quota specified.

      - **QuotaName** *(string) --*

        The name identifier of the service quota.

      - **Value** *(float) --*

        The value of service quota.

      - **Unit** *(string) --*

        The unit of measurement for the value of the service quota.

      - **Adjustable** *(boolean) --*

        Specifies if the quota value can be increased.

      - **GlobalQuota** *(boolean) --*

        Specifies if the quota is global.

      - **UsageMetric** *(dict) --*

        Specifies the details about the measurement.

        - **MetricNamespace** *(string) --*

          The namespace of the metric. The namespace is a container for CloudWatch metrics. You can
          specify a name for the namespace when you create a metric.

        - **MetricName** *(string) --*

          The name of the CloudWatch metric that measures usage of a service quota. This is a
          required field.

        - **MetricDimensions** *(dict) --*

          A dimension is a name/value pair that is part of the identity of a metric. Every metric
          has specific characteristics that describe it, and you can think of dimensions as
          categories for those characteristics. These dimensions are part of the CloudWatch Metric
          Identity that measures usage against a particular service quota.

          - *(string) --*

            - *(string) --*

        - **MetricStatisticRecommendation** *(string) --*

          Statistics are metric data aggregations over specified periods of time. This is the
          recommended statistic to use when comparing usage in the CloudWatch Metric against your
          Service Quota.

      - **Period** *(dict) --*

        Identifies the unit and value of how time is measured.

        - **PeriodValue** *(integer) --*

          The value of a period.

        - **PeriodUnit** *(string) --*

          The time unit of a period.

      - **ErrorReason** *(dict) --*

        Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

        - **ErrorCode** *(string) --*

          Service Quotas returns the following error values.

           ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have permission
           to call the service or service quota. To resolve the error, you need permission to
           access the service or service quota.

           ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is throttling
           Service Quotas.

           ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has availability
           issues.

           ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
           Quotas.

        - **ErrorMessage** *(string) --*

          The error message that provides more detail.
    """


_ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef = TypedDict(
    "_ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": str,
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
    },
    total=False,
)


class ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef(
    _ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef
):
    """
    Type definition for `ClientGetRequestedServiceQuotaChangeResponse` `RequestedQuota`

    Returns the ``RequestedServiceQuotaChange`` object for the specific increase request.

    - **Id** *(string) --*

      The unique identifier of a requested service quota change.

    - **CaseId** *(string) --*

      The case Id for the service quota increase request.

    - **ServiceCode** *(string) --*

      Specifies the service that you want to use.

    - **ServiceName** *(string) --*

      The name of the AWS service specified in the increase request.

    - **QuotaCode** *(string) --*

      Specifies the service quota that you want to use.

    - **QuotaName** *(string) --*

      Name of the service quota.

    - **DesiredValue** *(float) --*

      New increased value for the service quota.

    - **Status** *(string) --*

      State of the service quota increase request.

    - **Created** *(datetime) --*

      The date and time when the service quota increase request was received and the case Id was
      created.

    - **LastUpdated** *(datetime) --*

      The date and time of the most recent change in the service quota increase request.

    - **Requester** *(string) --*

      The IAM identity who submitted the service quota increase request.

    - **QuotaArn** *(string) --*

      The Amazon Resource Name (ARN) of the service quota.

    - **GlobalQuota** *(boolean) --*

      Identifies if the quota is global.

    - **Unit** *(string) --*

      Specifies the unit used for the quota.
    """


_ClientGetRequestedServiceQuotaChangeResponseTypeDef = TypedDict(
    "_ClientGetRequestedServiceQuotaChangeResponseTypeDef",
    {
        "RequestedQuota": ClientGetRequestedServiceQuotaChangeResponseRequestedQuotaTypeDef
    },
    total=False,
)


class ClientGetRequestedServiceQuotaChangeResponseTypeDef(
    _ClientGetRequestedServiceQuotaChangeResponseTypeDef
):
    """
    Type definition for `ClientGetRequestedServiceQuotaChange` `Response`

    - **RequestedQuota** *(dict) --*

      Returns the ``RequestedServiceQuotaChange`` object for the specific increase request.

      - **Id** *(string) --*

        The unique identifier of a requested service quota change.

      - **CaseId** *(string) --*

        The case Id for the service quota increase request.

      - **ServiceCode** *(string) --*

        Specifies the service that you want to use.

      - **ServiceName** *(string) --*

        The name of the AWS service specified in the increase request.

      - **QuotaCode** *(string) --*

        Specifies the service quota that you want to use.

      - **QuotaName** *(string) --*

        Name of the service quota.

      - **DesiredValue** *(float) --*

        New increased value for the service quota.

      - **Status** *(string) --*

        State of the service quota increase request.

      - **Created** *(datetime) --*

        The date and time when the service quota increase request was received and the case Id was
        created.

      - **LastUpdated** *(datetime) --*

        The date and time of the most recent change in the service quota increase request.

      - **Requester** *(string) --*

        The IAM identity who submitted the service quota increase request.

      - **QuotaArn** *(string) --*

        The Amazon Resource Name (ARN) of the service quota.

      - **GlobalQuota** *(boolean) --*

        Identifies if the quota is global.

      - **Unit** *(string) --*

        Specifies the unit used for the quota.
    """


_ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef = TypedDict(
    "_ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "AwsRegion": str,
        "Unit": str,
        "GlobalQuota": bool,
    },
    total=False,
)


class ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef(
    _ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef
):
    """
    Type definition for `ClientGetServiceQuotaIncreaseRequestFromTemplateResponse` `ServiceQuotaIncreaseRequestInTemplate`

    This object contains the details about the quota increase request.

    - **ServiceCode** *(string) --*

      The code identifier for the AWS service specified in the increase request.

    - **ServiceName** *(string) --*

      The name of the AWS service specified in the increase request.

    - **QuotaCode** *(string) --*

      The code identifier for the service quota specified in the increase request.

    - **QuotaName** *(string) --*

      The name of the service quota in the increase request.

    - **DesiredValue** *(float) --*

      Identifies the new, increased value of the service quota in the increase request.

    - **AwsRegion** *(string) --*

      The AWS Region where the increase request occurs.

    - **Unit** *(string) --*

      The unit of measure for the increase request.

    - **GlobalQuota** *(boolean) --*

      Specifies if the quota is a global quota.
    """


_ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef = TypedDict(
    "_ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplate": ClientGetServiceQuotaIncreaseRequestFromTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef
    },
    total=False,
)


class ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef(
    _ClientGetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef
):
    """
    Type definition for `ClientGetServiceQuotaIncreaseRequestFromTemplate` `Response`

    - **ServiceQuotaIncreaseRequestInTemplate** *(dict) --*

      This object contains the details about the quota increase request.

      - **ServiceCode** *(string) --*

        The code identifier for the AWS service specified in the increase request.

      - **ServiceName** *(string) --*

        The name of the AWS service specified in the increase request.

      - **QuotaCode** *(string) --*

        The code identifier for the service quota specified in the increase request.

      - **QuotaName** *(string) --*

        The name of the service quota in the increase request.

      - **DesiredValue** *(float) --*

        Identifies the new, increased value of the service quota in the increase request.

      - **AwsRegion** *(string) --*

        The AWS Region where the increase request occurs.

      - **Unit** *(string) --*

        The unit of measure for the increase request.

      - **GlobalQuota** *(boolean) --*

        Specifies if the quota is a global quota.
    """


_ClientGetServiceQuotaResponseQuotaErrorReasonTypeDef = TypedDict(
    "_ClientGetServiceQuotaResponseQuotaErrorReasonTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientGetServiceQuotaResponseQuotaErrorReasonTypeDef(
    _ClientGetServiceQuotaResponseQuotaErrorReasonTypeDef
):
    """
    Type definition for `ClientGetServiceQuotaResponseQuota` `ErrorReason`

    Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

    - **ErrorCode** *(string) --*

      Service Quotas returns the following error values.

       ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have permission
       to call the service or service quota. To resolve the error, you need permission to
       access the service or service quota.

       ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is throttling
       Service Quotas.

       ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has availability
       issues.

       ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
       Quotas.

    - **ErrorMessage** *(string) --*

      The error message that provides more detail.
    """


_ClientGetServiceQuotaResponseQuotaPeriodTypeDef = TypedDict(
    "_ClientGetServiceQuotaResponseQuotaPeriodTypeDef",
    {"PeriodValue": int, "PeriodUnit": str},
    total=False,
)


class ClientGetServiceQuotaResponseQuotaPeriodTypeDef(
    _ClientGetServiceQuotaResponseQuotaPeriodTypeDef
):
    """
    Type definition for `ClientGetServiceQuotaResponseQuota` `Period`

    Identifies the unit and value of how time is measured.

    - **PeriodValue** *(integer) --*

      The value of a period.

    - **PeriodUnit** *(string) --*

      The time unit of a period.
    """


_ClientGetServiceQuotaResponseQuotaUsageMetricTypeDef = TypedDict(
    "_ClientGetServiceQuotaResponseQuotaUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)


class ClientGetServiceQuotaResponseQuotaUsageMetricTypeDef(
    _ClientGetServiceQuotaResponseQuotaUsageMetricTypeDef
):
    """
    Type definition for `ClientGetServiceQuotaResponseQuota` `UsageMetric`

    Specifies the details about the measurement.

    - **MetricNamespace** *(string) --*

      The namespace of the metric. The namespace is a container for CloudWatch metrics. You can
      specify a name for the namespace when you create a metric.

    - **MetricName** *(string) --*

      The name of the CloudWatch metric that measures usage of a service quota. This is a
      required field.

    - **MetricDimensions** *(dict) --*

      A dimension is a name/value pair that is part of the identity of a metric. Every metric
      has specific characteristics that describe it, and you can think of dimensions as
      categories for those characteristics. These dimensions are part of the CloudWatch Metric
      Identity that measures usage against a particular service quota.

      - *(string) --*

        - *(string) --*

    - **MetricStatisticRecommendation** *(string) --*

      Statistics are metric data aggregations over specified periods of time. This is the
      recommended statistic to use when comparing usage in the CloudWatch Metric against your
      Service Quota.
    """


_ClientGetServiceQuotaResponseQuotaTypeDef = TypedDict(
    "_ClientGetServiceQuotaResponseQuotaTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": ClientGetServiceQuotaResponseQuotaUsageMetricTypeDef,
        "Period": ClientGetServiceQuotaResponseQuotaPeriodTypeDef,
        "ErrorReason": ClientGetServiceQuotaResponseQuotaErrorReasonTypeDef,
    },
    total=False,
)


class ClientGetServiceQuotaResponseQuotaTypeDef(
    _ClientGetServiceQuotaResponseQuotaTypeDef
):
    """
    Type definition for `ClientGetServiceQuotaResponse` `Quota`

    Returns the  ServiceQuota object which contains all values for a quota.

    - **ServiceCode** *(string) --*

      Specifies the service that you want to use.

    - **ServiceName** *(string) --*

      The name of the AWS service specified in the increase request.

    - **QuotaArn** *(string) --*

      The Amazon Resource Name (ARN) of the service quota.

    - **QuotaCode** *(string) --*

      The code identifier for the service quota specified.

    - **QuotaName** *(string) --*

      The name identifier of the service quota.

    - **Value** *(float) --*

      The value of service quota.

    - **Unit** *(string) --*

      The unit of measurement for the value of the service quota.

    - **Adjustable** *(boolean) --*

      Specifies if the quota value can be increased.

    - **GlobalQuota** *(boolean) --*

      Specifies if the quota is global.

    - **UsageMetric** *(dict) --*

      Specifies the details about the measurement.

      - **MetricNamespace** *(string) --*

        The namespace of the metric. The namespace is a container for CloudWatch metrics. You can
        specify a name for the namespace when you create a metric.

      - **MetricName** *(string) --*

        The name of the CloudWatch metric that measures usage of a service quota. This is a
        required field.

      - **MetricDimensions** *(dict) --*

        A dimension is a name/value pair that is part of the identity of a metric. Every metric
        has specific characteristics that describe it, and you can think of dimensions as
        categories for those characteristics. These dimensions are part of the CloudWatch Metric
        Identity that measures usage against a particular service quota.

        - *(string) --*

          - *(string) --*

      - **MetricStatisticRecommendation** *(string) --*

        Statistics are metric data aggregations over specified periods of time. This is the
        recommended statistic to use when comparing usage in the CloudWatch Metric against your
        Service Quota.

    - **Period** *(dict) --*

      Identifies the unit and value of how time is measured.

      - **PeriodValue** *(integer) --*

        The value of a period.

      - **PeriodUnit** *(string) --*

        The time unit of a period.

    - **ErrorReason** *(dict) --*

      Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

      - **ErrorCode** *(string) --*

        Service Quotas returns the following error values.

         ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have permission
         to call the service or service quota. To resolve the error, you need permission to
         access the service or service quota.

         ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is throttling
         Service Quotas.

         ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has availability
         issues.

         ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
         Quotas.

      - **ErrorMessage** *(string) --*

        The error message that provides more detail.
    """


_ClientGetServiceQuotaResponseTypeDef = TypedDict(
    "_ClientGetServiceQuotaResponseTypeDef",
    {"Quota": ClientGetServiceQuotaResponseQuotaTypeDef},
    total=False,
)


class ClientGetServiceQuotaResponseTypeDef(_ClientGetServiceQuotaResponseTypeDef):
    """
    Type definition for `ClientGetServiceQuota` `Response`

    - **Quota** *(dict) --*

      Returns the  ServiceQuota object which contains all values for a quota.

      - **ServiceCode** *(string) --*

        Specifies the service that you want to use.

      - **ServiceName** *(string) --*

        The name of the AWS service specified in the increase request.

      - **QuotaArn** *(string) --*

        The Amazon Resource Name (ARN) of the service quota.

      - **QuotaCode** *(string) --*

        The code identifier for the service quota specified.

      - **QuotaName** *(string) --*

        The name identifier of the service quota.

      - **Value** *(float) --*

        The value of service quota.

      - **Unit** *(string) --*

        The unit of measurement for the value of the service quota.

      - **Adjustable** *(boolean) --*

        Specifies if the quota value can be increased.

      - **GlobalQuota** *(boolean) --*

        Specifies if the quota is global.

      - **UsageMetric** *(dict) --*

        Specifies the details about the measurement.

        - **MetricNamespace** *(string) --*

          The namespace of the metric. The namespace is a container for CloudWatch metrics. You can
          specify a name for the namespace when you create a metric.

        - **MetricName** *(string) --*

          The name of the CloudWatch metric that measures usage of a service quota. This is a
          required field.

        - **MetricDimensions** *(dict) --*

          A dimension is a name/value pair that is part of the identity of a metric. Every metric
          has specific characteristics that describe it, and you can think of dimensions as
          categories for those characteristics. These dimensions are part of the CloudWatch Metric
          Identity that measures usage against a particular service quota.

          - *(string) --*

            - *(string) --*

        - **MetricStatisticRecommendation** *(string) --*

          Statistics are metric data aggregations over specified periods of time. This is the
          recommended statistic to use when comparing usage in the CloudWatch Metric against your
          Service Quota.

      - **Period** *(dict) --*

        Identifies the unit and value of how time is measured.

        - **PeriodValue** *(integer) --*

          The value of a period.

        - **PeriodUnit** *(string) --*

          The time unit of a period.

      - **ErrorReason** *(dict) --*

        Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

        - **ErrorCode** *(string) --*

          Service Quotas returns the following error values.

           ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have permission
           to call the service or service quota. To resolve the error, you need permission to
           access the service or service quota.

           ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is throttling
           Service Quotas.

           ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has availability
           issues.

           ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
           Quotas.

        - **ErrorMessage** *(string) --*

          The error message that provides more detail.
    """


_ClientListAwsDefaultServiceQuotasResponseQuotasErrorReasonTypeDef = TypedDict(
    "_ClientListAwsDefaultServiceQuotasResponseQuotasErrorReasonTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientListAwsDefaultServiceQuotasResponseQuotasErrorReasonTypeDef(
    _ClientListAwsDefaultServiceQuotasResponseQuotasErrorReasonTypeDef
):
    """
    Type definition for `ClientListAwsDefaultServiceQuotasResponseQuotas` `ErrorReason`

    Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

    - **ErrorCode** *(string) --*

      Service Quotas returns the following error values.

       ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have
       permission to call the service or service quota. To resolve the error, you need
       permission to access the service or service quota.

       ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is
       throttling Service Quotas.

       ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has
       availability issues.

       ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
       Quotas.

    - **ErrorMessage** *(string) --*

      The error message that provides more detail.
    """


_ClientListAwsDefaultServiceQuotasResponseQuotasPeriodTypeDef = TypedDict(
    "_ClientListAwsDefaultServiceQuotasResponseQuotasPeriodTypeDef",
    {"PeriodValue": int, "PeriodUnit": str},
    total=False,
)


class ClientListAwsDefaultServiceQuotasResponseQuotasPeriodTypeDef(
    _ClientListAwsDefaultServiceQuotasResponseQuotasPeriodTypeDef
):
    """
    Type definition for `ClientListAwsDefaultServiceQuotasResponseQuotas` `Period`

    Identifies the unit and value of how time is measured.

    - **PeriodValue** *(integer) --*

      The value of a period.

    - **PeriodUnit** *(string) --*

      The time unit of a period.
    """


_ClientListAwsDefaultServiceQuotasResponseQuotasUsageMetricTypeDef = TypedDict(
    "_ClientListAwsDefaultServiceQuotasResponseQuotasUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)


class ClientListAwsDefaultServiceQuotasResponseQuotasUsageMetricTypeDef(
    _ClientListAwsDefaultServiceQuotasResponseQuotasUsageMetricTypeDef
):
    """
    Type definition for `ClientListAwsDefaultServiceQuotasResponseQuotas` `UsageMetric`

    Specifies the details about the measurement.

    - **MetricNamespace** *(string) --*

      The namespace of the metric. The namespace is a container for CloudWatch metrics. You
      can specify a name for the namespace when you create a metric.

    - **MetricName** *(string) --*

      The name of the CloudWatch metric that measures usage of a service quota. This is a
      required field.

    - **MetricDimensions** *(dict) --*

      A dimension is a name/value pair that is part of the identity of a metric. Every metric
      has specific characteristics that describe it, and you can think of dimensions as
      categories for those characteristics. These dimensions are part of the CloudWatch
      Metric Identity that measures usage against a particular service quota.

      - *(string) --*

        - *(string) --*

    - **MetricStatisticRecommendation** *(string) --*

      Statistics are metric data aggregations over specified periods of time. This is the
      recommended statistic to use when comparing usage in the CloudWatch Metric against your
      Service Quota.
    """


_ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef = TypedDict(
    "_ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": ClientListAwsDefaultServiceQuotasResponseQuotasUsageMetricTypeDef,
        "Period": ClientListAwsDefaultServiceQuotasResponseQuotasPeriodTypeDef,
        "ErrorReason": ClientListAwsDefaultServiceQuotasResponseQuotasErrorReasonTypeDef,
    },
    total=False,
)


class ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef(
    _ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef
):
    """
    Type definition for `ClientListAwsDefaultServiceQuotasResponse` `Quotas`

    A structure that contains the full set of details that define the service quota.

    - **ServiceCode** *(string) --*

      Specifies the service that you want to use.

    - **ServiceName** *(string) --*

      The name of the AWS service specified in the increase request.

    - **QuotaArn** *(string) --*

      The Amazon Resource Name (ARN) of the service quota.

    - **QuotaCode** *(string) --*

      The code identifier for the service quota specified.

    - **QuotaName** *(string) --*

      The name identifier of the service quota.

    - **Value** *(float) --*

      The value of service quota.

    - **Unit** *(string) --*

      The unit of measurement for the value of the service quota.

    - **Adjustable** *(boolean) --*

      Specifies if the quota value can be increased.

    - **GlobalQuota** *(boolean) --*

      Specifies if the quota is global.

    - **UsageMetric** *(dict) --*

      Specifies the details about the measurement.

      - **MetricNamespace** *(string) --*

        The namespace of the metric. The namespace is a container for CloudWatch metrics. You
        can specify a name for the namespace when you create a metric.

      - **MetricName** *(string) --*

        The name of the CloudWatch metric that measures usage of a service quota. This is a
        required field.

      - **MetricDimensions** *(dict) --*

        A dimension is a name/value pair that is part of the identity of a metric. Every metric
        has specific characteristics that describe it, and you can think of dimensions as
        categories for those characteristics. These dimensions are part of the CloudWatch
        Metric Identity that measures usage against a particular service quota.

        - *(string) --*

          - *(string) --*

      - **MetricStatisticRecommendation** *(string) --*

        Statistics are metric data aggregations over specified periods of time. This is the
        recommended statistic to use when comparing usage in the CloudWatch Metric against your
        Service Quota.

    - **Period** *(dict) --*

      Identifies the unit and value of how time is measured.

      - **PeriodValue** *(integer) --*

        The value of a period.

      - **PeriodUnit** *(string) --*

        The time unit of a period.

    - **ErrorReason** *(dict) --*

      Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

      - **ErrorCode** *(string) --*

        Service Quotas returns the following error values.

         ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have
         permission to call the service or service quota. To resolve the error, you need
         permission to access the service or service quota.

         ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is
         throttling Service Quotas.

         ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has
         availability issues.

         ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
         Quotas.

      - **ErrorMessage** *(string) --*

        The error message that provides more detail.
    """


_ClientListAwsDefaultServiceQuotasResponseTypeDef = TypedDict(
    "_ClientListAwsDefaultServiceQuotasResponseTypeDef",
    {
        "NextToken": str,
        "Quotas": List[ClientListAwsDefaultServiceQuotasResponseQuotasTypeDef],
    },
    total=False,
)


class ClientListAwsDefaultServiceQuotasResponseTypeDef(
    _ClientListAwsDefaultServiceQuotasResponseTypeDef
):
    """
    Type definition for `ClientListAwsDefaultServiceQuotas` `Response`

    - **NextToken** *(string) --*

      (Optional) Use this parameter in a request if you receive a ``NextToken`` response in a
      previous request that indicates that there's more output available. In a subsequent call, set
      it to the value of the previous call's ``NextToken`` response to indicate where the output
      should continue from.

    - **Quotas** *(list) --*

      A list of the quotas in the account with the AWS default values.

      - *(dict) --*

        A structure that contains the full set of details that define the service quota.

        - **ServiceCode** *(string) --*

          Specifies the service that you want to use.

        - **ServiceName** *(string) --*

          The name of the AWS service specified in the increase request.

        - **QuotaArn** *(string) --*

          The Amazon Resource Name (ARN) of the service quota.

        - **QuotaCode** *(string) --*

          The code identifier for the service quota specified.

        - **QuotaName** *(string) --*

          The name identifier of the service quota.

        - **Value** *(float) --*

          The value of service quota.

        - **Unit** *(string) --*

          The unit of measurement for the value of the service quota.

        - **Adjustable** *(boolean) --*

          Specifies if the quota value can be increased.

        - **GlobalQuota** *(boolean) --*

          Specifies if the quota is global.

        - **UsageMetric** *(dict) --*

          Specifies the details about the measurement.

          - **MetricNamespace** *(string) --*

            The namespace of the metric. The namespace is a container for CloudWatch metrics. You
            can specify a name for the namespace when you create a metric.

          - **MetricName** *(string) --*

            The name of the CloudWatch metric that measures usage of a service quota. This is a
            required field.

          - **MetricDimensions** *(dict) --*

            A dimension is a name/value pair that is part of the identity of a metric. Every metric
            has specific characteristics that describe it, and you can think of dimensions as
            categories for those characteristics. These dimensions are part of the CloudWatch
            Metric Identity that measures usage against a particular service quota.

            - *(string) --*

              - *(string) --*

          - **MetricStatisticRecommendation** *(string) --*

            Statistics are metric data aggregations over specified periods of time. This is the
            recommended statistic to use when comparing usage in the CloudWatch Metric against your
            Service Quota.

        - **Period** *(dict) --*

          Identifies the unit and value of how time is measured.

          - **PeriodValue** *(integer) --*

            The value of a period.

          - **PeriodUnit** *(string) --*

            The time unit of a period.

        - **ErrorReason** *(dict) --*

          Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

          - **ErrorCode** *(string) --*

            Service Quotas returns the following error values.

             ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have
             permission to call the service or service quota. To resolve the error, you need
             permission to access the service or service quota.

             ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is
             throttling Service Quotas.

             ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has
             availability issues.

             ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
             Quotas.

          - **ErrorMessage** *(string) --*

            The error message that provides more detail.
    """


_ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef = TypedDict(
    "_ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": str,
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
    },
    total=False,
)


class ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef(
    _ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef
):
    """
    Type definition for `ClientListRequestedServiceQuotaChangeHistoryByQuotaResponse` `RequestedQuotas`

    A structure that contains information about a requested change for a quota.

    - **Id** *(string) --*

      The unique identifier of a requested service quota change.

    - **CaseId** *(string) --*

      The case Id for the service quota increase request.

    - **ServiceCode** *(string) --*

      Specifies the service that you want to use.

    - **ServiceName** *(string) --*

      The name of the AWS service specified in the increase request.

    - **QuotaCode** *(string) --*

      Specifies the service quota that you want to use.

    - **QuotaName** *(string) --*

      Name of the service quota.

    - **DesiredValue** *(float) --*

      New increased value for the service quota.

    - **Status** *(string) --*

      State of the service quota increase request.

    - **Created** *(datetime) --*

      The date and time when the service quota increase request was received and the case Id
      was created.

    - **LastUpdated** *(datetime) --*

      The date and time of the most recent change in the service quota increase request.

    - **Requester** *(string) --*

      The IAM identity who submitted the service quota increase request.

    - **QuotaArn** *(string) --*

      The Amazon Resource Name (ARN) of the service quota.

    - **GlobalQuota** *(boolean) --*

      Identifies if the quota is global.

    - **Unit** *(string) --*

      Specifies the unit used for the quota.
    """


_ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef = TypedDict(
    "_ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    {
        "NextToken": str,
        "RequestedQuotas": List[
            ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseRequestedQuotasTypeDef
        ],
    },
    total=False,
)


class ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef(
    _ClientListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef
):
    """
    Type definition for `ClientListRequestedServiceQuotaChangeHistoryByQuota` `Response`

    - **NextToken** *(string) --*

      If present in the response, this value indicates there's more output available that what's
      included in the current response. This can occur even when the response includes no values at
      all, such as when you ask for a filtered view of a very long list. Use this value in the
      ``NextToken`` request parameter in a subsequent call to the operation to continue processing
      and get the next part of the output. You should repeat this until the ``NextToken`` response
      element comes back empty (as ``null`` ).

    - **RequestedQuotas** *(list) --*

      Returns a list of service quota requests.

      - *(dict) --*

        A structure that contains information about a requested change for a quota.

        - **Id** *(string) --*

          The unique identifier of a requested service quota change.

        - **CaseId** *(string) --*

          The case Id for the service quota increase request.

        - **ServiceCode** *(string) --*

          Specifies the service that you want to use.

        - **ServiceName** *(string) --*

          The name of the AWS service specified in the increase request.

        - **QuotaCode** *(string) --*

          Specifies the service quota that you want to use.

        - **QuotaName** *(string) --*

          Name of the service quota.

        - **DesiredValue** *(float) --*

          New increased value for the service quota.

        - **Status** *(string) --*

          State of the service quota increase request.

        - **Created** *(datetime) --*

          The date and time when the service quota increase request was received and the case Id
          was created.

        - **LastUpdated** *(datetime) --*

          The date and time of the most recent change in the service quota increase request.

        - **Requester** *(string) --*

          The IAM identity who submitted the service quota increase request.

        - **QuotaArn** *(string) --*

          The Amazon Resource Name (ARN) of the service quota.

        - **GlobalQuota** *(boolean) --*

          Identifies if the quota is global.

        - **Unit** *(string) --*

          Specifies the unit used for the quota.
    """


_ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef = TypedDict(
    "_ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": str,
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
    },
    total=False,
)


class ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef(
    _ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef
):
    """
    Type definition for `ClientListRequestedServiceQuotaChangeHistoryResponse` `RequestedQuotas`

    A structure that contains information about a requested change for a quota.

    - **Id** *(string) --*

      The unique identifier of a requested service quota change.

    - **CaseId** *(string) --*

      The case Id for the service quota increase request.

    - **ServiceCode** *(string) --*

      Specifies the service that you want to use.

    - **ServiceName** *(string) --*

      The name of the AWS service specified in the increase request.

    - **QuotaCode** *(string) --*

      Specifies the service quota that you want to use.

    - **QuotaName** *(string) --*

      Name of the service quota.

    - **DesiredValue** *(float) --*

      New increased value for the service quota.

    - **Status** *(string) --*

      State of the service quota increase request.

    - **Created** *(datetime) --*

      The date and time when the service quota increase request was received and the case Id
      was created.

    - **LastUpdated** *(datetime) --*

      The date and time of the most recent change in the service quota increase request.

    - **Requester** *(string) --*

      The IAM identity who submitted the service quota increase request.

    - **QuotaArn** *(string) --*

      The Amazon Resource Name (ARN) of the service quota.

    - **GlobalQuota** *(boolean) --*

      Identifies if the quota is global.

    - **Unit** *(string) --*

      Specifies the unit used for the quota.
    """


_ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef = TypedDict(
    "_ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    {
        "NextToken": str,
        "RequestedQuotas": List[
            ClientListRequestedServiceQuotaChangeHistoryResponseRequestedQuotasTypeDef
        ],
    },
    total=False,
)


class ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef(
    _ClientListRequestedServiceQuotaChangeHistoryResponseTypeDef
):
    """
    Type definition for `ClientListRequestedServiceQuotaChangeHistory` `Response`

    - **NextToken** *(string) --*

      If present in the response, this value indicates there's more output available that what's
      included in the current response. This can occur even when the response includes no values at
      all, such as when you ask for a filtered view of a very long list. Use this value in the
      ``NextToken`` request parameter in a subsequent call to the operation to continue processing
      and get the next part of the output. You should repeat this until the ``NextToken`` response
      element comes back empty (as ``null`` ).

    - **RequestedQuotas** *(list) --*

      Returns a list of service quota requests.

      - *(dict) --*

        A structure that contains information about a requested change for a quota.

        - **Id** *(string) --*

          The unique identifier of a requested service quota change.

        - **CaseId** *(string) --*

          The case Id for the service quota increase request.

        - **ServiceCode** *(string) --*

          Specifies the service that you want to use.

        - **ServiceName** *(string) --*

          The name of the AWS service specified in the increase request.

        - **QuotaCode** *(string) --*

          Specifies the service quota that you want to use.

        - **QuotaName** *(string) --*

          Name of the service quota.

        - **DesiredValue** *(float) --*

          New increased value for the service quota.

        - **Status** *(string) --*

          State of the service quota increase request.

        - **Created** *(datetime) --*

          The date and time when the service quota increase request was received and the case Id
          was created.

        - **LastUpdated** *(datetime) --*

          The date and time of the most recent change in the service quota increase request.

        - **Requester** *(string) --*

          The IAM identity who submitted the service quota increase request.

        - **QuotaArn** *(string) --*

          The Amazon Resource Name (ARN) of the service quota.

        - **GlobalQuota** *(boolean) --*

          Identifies if the quota is global.

        - **Unit** *(string) --*

          Specifies the unit used for the quota.
    """


_ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef = TypedDict(
    "_ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "AwsRegion": str,
        "Unit": str,
        "GlobalQuota": bool,
    },
    total=False,
)


class ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef(
    _ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef
):
    """
    Type definition for `ClientListServiceQuotaIncreaseRequestsInTemplateResponse` `ServiceQuotaIncreaseRequestInTemplateList`

    A structure that contains information about one service quota increase request.

    - **ServiceCode** *(string) --*

      The code identifier for the AWS service specified in the increase request.

    - **ServiceName** *(string) --*

      The name of the AWS service specified in the increase request.

    - **QuotaCode** *(string) --*

      The code identifier for the service quota specified in the increase request.

    - **QuotaName** *(string) --*

      The name of the service quota in the increase request.

    - **DesiredValue** *(float) --*

      Identifies the new, increased value of the service quota in the increase request.

    - **AwsRegion** *(string) --*

      The AWS Region where the increase request occurs.

    - **Unit** *(string) --*

      The unit of measure for the increase request.

    - **GlobalQuota** *(boolean) --*

      Specifies if the quota is a global quota.
    """


_ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef = TypedDict(
    "_ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplateList": List[
            ClientListServiceQuotaIncreaseRequestsInTemplateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef(
    _ClientListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef
):
    """
    Type definition for `ClientListServiceQuotaIncreaseRequestsInTemplate` `Response`

    - **ServiceQuotaIncreaseRequestInTemplateList** *(list) --*

      Returns the list of values of the quota increase request in the template.

      - *(dict) --*

        A structure that contains information about one service quota increase request.

        - **ServiceCode** *(string) --*

          The code identifier for the AWS service specified in the increase request.

        - **ServiceName** *(string) --*

          The name of the AWS service specified in the increase request.

        - **QuotaCode** *(string) --*

          The code identifier for the service quota specified in the increase request.

        - **QuotaName** *(string) --*

          The name of the service quota in the increase request.

        - **DesiredValue** *(float) --*

          Identifies the new, increased value of the service quota in the increase request.

        - **AwsRegion** *(string) --*

          The AWS Region where the increase request occurs.

        - **Unit** *(string) --*

          The unit of measure for the increase request.

        - **GlobalQuota** *(boolean) --*

          Specifies if the quota is a global quota.

    - **NextToken** *(string) --*

      If present in the response, this value indicates there's more output available that what's
      included in the current response. This can occur even when the response includes no values at
      all, such as when you ask for a filtered view of a very long list. Use this value in the
      ``NextToken`` request parameter in a subsequent call to the operation to continue processing
      and get the next part of the output. You should repeat this until the ``NextToken`` response
      element comes back empty (as ``null`` ).
    """


_ClientListServiceQuotasResponseQuotasErrorReasonTypeDef = TypedDict(
    "_ClientListServiceQuotasResponseQuotasErrorReasonTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientListServiceQuotasResponseQuotasErrorReasonTypeDef(
    _ClientListServiceQuotasResponseQuotasErrorReasonTypeDef
):
    """
    Type definition for `ClientListServiceQuotasResponseQuotas` `ErrorReason`

    Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

    - **ErrorCode** *(string) --*

      Service Quotas returns the following error values.

       ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have
       permission to call the service or service quota. To resolve the error, you need
       permission to access the service or service quota.

       ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is
       throttling Service Quotas.

       ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has
       availability issues.

       ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
       Quotas.

    - **ErrorMessage** *(string) --*

      The error message that provides more detail.
    """


_ClientListServiceQuotasResponseQuotasPeriodTypeDef = TypedDict(
    "_ClientListServiceQuotasResponseQuotasPeriodTypeDef",
    {"PeriodValue": int, "PeriodUnit": str},
    total=False,
)


class ClientListServiceQuotasResponseQuotasPeriodTypeDef(
    _ClientListServiceQuotasResponseQuotasPeriodTypeDef
):
    """
    Type definition for `ClientListServiceQuotasResponseQuotas` `Period`

    Identifies the unit and value of how time is measured.

    - **PeriodValue** *(integer) --*

      The value of a period.

    - **PeriodUnit** *(string) --*

      The time unit of a period.
    """


_ClientListServiceQuotasResponseQuotasUsageMetricTypeDef = TypedDict(
    "_ClientListServiceQuotasResponseQuotasUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)


class ClientListServiceQuotasResponseQuotasUsageMetricTypeDef(
    _ClientListServiceQuotasResponseQuotasUsageMetricTypeDef
):
    """
    Type definition for `ClientListServiceQuotasResponseQuotas` `UsageMetric`

    Specifies the details about the measurement.

    - **MetricNamespace** *(string) --*

      The namespace of the metric. The namespace is a container for CloudWatch metrics. You
      can specify a name for the namespace when you create a metric.

    - **MetricName** *(string) --*

      The name of the CloudWatch metric that measures usage of a service quota. This is a
      required field.

    - **MetricDimensions** *(dict) --*

      A dimension is a name/value pair that is part of the identity of a metric. Every metric
      has specific characteristics that describe it, and you can think of dimensions as
      categories for those characteristics. These dimensions are part of the CloudWatch
      Metric Identity that measures usage against a particular service quota.

      - *(string) --*

        - *(string) --*

    - **MetricStatisticRecommendation** *(string) --*

      Statistics are metric data aggregations over specified periods of time. This is the
      recommended statistic to use when comparing usage in the CloudWatch Metric against your
      Service Quota.
    """


_ClientListServiceQuotasResponseQuotasTypeDef = TypedDict(
    "_ClientListServiceQuotasResponseQuotasTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": ClientListServiceQuotasResponseQuotasUsageMetricTypeDef,
        "Period": ClientListServiceQuotasResponseQuotasPeriodTypeDef,
        "ErrorReason": ClientListServiceQuotasResponseQuotasErrorReasonTypeDef,
    },
    total=False,
)


class ClientListServiceQuotasResponseQuotasTypeDef(
    _ClientListServiceQuotasResponseQuotasTypeDef
):
    """
    Type definition for `ClientListServiceQuotasResponse` `Quotas`

    A structure that contains the full set of details that define the service quota.

    - **ServiceCode** *(string) --*

      Specifies the service that you want to use.

    - **ServiceName** *(string) --*

      The name of the AWS service specified in the increase request.

    - **QuotaArn** *(string) --*

      The Amazon Resource Name (ARN) of the service quota.

    - **QuotaCode** *(string) --*

      The code identifier for the service quota specified.

    - **QuotaName** *(string) --*

      The name identifier of the service quota.

    - **Value** *(float) --*

      The value of service quota.

    - **Unit** *(string) --*

      The unit of measurement for the value of the service quota.

    - **Adjustable** *(boolean) --*

      Specifies if the quota value can be increased.

    - **GlobalQuota** *(boolean) --*

      Specifies if the quota is global.

    - **UsageMetric** *(dict) --*

      Specifies the details about the measurement.

      - **MetricNamespace** *(string) --*

        The namespace of the metric. The namespace is a container for CloudWatch metrics. You
        can specify a name for the namespace when you create a metric.

      - **MetricName** *(string) --*

        The name of the CloudWatch metric that measures usage of a service quota. This is a
        required field.

      - **MetricDimensions** *(dict) --*

        A dimension is a name/value pair that is part of the identity of a metric. Every metric
        has specific characteristics that describe it, and you can think of dimensions as
        categories for those characteristics. These dimensions are part of the CloudWatch
        Metric Identity that measures usage against a particular service quota.

        - *(string) --*

          - *(string) --*

      - **MetricStatisticRecommendation** *(string) --*

        Statistics are metric data aggregations over specified periods of time. This is the
        recommended statistic to use when comparing usage in the CloudWatch Metric against your
        Service Quota.

    - **Period** *(dict) --*

      Identifies the unit and value of how time is measured.

      - **PeriodValue** *(integer) --*

        The value of a period.

      - **PeriodUnit** *(string) --*

        The time unit of a period.

    - **ErrorReason** *(dict) --*

      Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

      - **ErrorCode** *(string) --*

        Service Quotas returns the following error values.

         ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have
         permission to call the service or service quota. To resolve the error, you need
         permission to access the service or service quota.

         ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is
         throttling Service Quotas.

         ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has
         availability issues.

         ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
         Quotas.

      - **ErrorMessage** *(string) --*

        The error message that provides more detail.
    """


_ClientListServiceQuotasResponseTypeDef = TypedDict(
    "_ClientListServiceQuotasResponseTypeDef",
    {"NextToken": str, "Quotas": List[ClientListServiceQuotasResponseQuotasTypeDef]},
    total=False,
)


class ClientListServiceQuotasResponseTypeDef(_ClientListServiceQuotasResponseTypeDef):
    """
    Type definition for `ClientListServiceQuotas` `Response`

    - **NextToken** *(string) --*

      If present in the response, this value indicates there's more output available that what's
      included in the current response. This can occur even when the response includes no values at
      all, such as when you ask for a filtered view of a very long list. Use this value in the
      ``NextToken`` request parameter in a subsequent call to the operation to continue processing
      and get the next part of the output. You should repeat this until the ``NextToken`` response
      element comes back empty (as ``null`` ).

    - **Quotas** *(list) --*

      The response information for a quota lists all attribute information for the quota.

      - *(dict) --*

        A structure that contains the full set of details that define the service quota.

        - **ServiceCode** *(string) --*

          Specifies the service that you want to use.

        - **ServiceName** *(string) --*

          The name of the AWS service specified in the increase request.

        - **QuotaArn** *(string) --*

          The Amazon Resource Name (ARN) of the service quota.

        - **QuotaCode** *(string) --*

          The code identifier for the service quota specified.

        - **QuotaName** *(string) --*

          The name identifier of the service quota.

        - **Value** *(float) --*

          The value of service quota.

        - **Unit** *(string) --*

          The unit of measurement for the value of the service quota.

        - **Adjustable** *(boolean) --*

          Specifies if the quota value can be increased.

        - **GlobalQuota** *(boolean) --*

          Specifies if the quota is global.

        - **UsageMetric** *(dict) --*

          Specifies the details about the measurement.

          - **MetricNamespace** *(string) --*

            The namespace of the metric. The namespace is a container for CloudWatch metrics. You
            can specify a name for the namespace when you create a metric.

          - **MetricName** *(string) --*

            The name of the CloudWatch metric that measures usage of a service quota. This is a
            required field.

          - **MetricDimensions** *(dict) --*

            A dimension is a name/value pair that is part of the identity of a metric. Every metric
            has specific characteristics that describe it, and you can think of dimensions as
            categories for those characteristics. These dimensions are part of the CloudWatch
            Metric Identity that measures usage against a particular service quota.

            - *(string) --*

              - *(string) --*

          - **MetricStatisticRecommendation** *(string) --*

            Statistics are metric data aggregations over specified periods of time. This is the
            recommended statistic to use when comparing usage in the CloudWatch Metric against your
            Service Quota.

        - **Period** *(dict) --*

          Identifies the unit and value of how time is measured.

          - **PeriodValue** *(integer) --*

            The value of a period.

          - **PeriodUnit** *(string) --*

            The time unit of a period.

        - **ErrorReason** *(dict) --*

          Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

          - **ErrorCode** *(string) --*

            Service Quotas returns the following error values.

             ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have
             permission to call the service or service quota. To resolve the error, you need
             permission to access the service or service quota.

             ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is
             throttling Service Quotas.

             ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has
             availability issues.

             ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
             Quotas.

          - **ErrorMessage** *(string) --*

            The error message that provides more detail.
    """


_ClientListServicesResponseServicesTypeDef = TypedDict(
    "_ClientListServicesResponseServicesTypeDef",
    {"ServiceCode": str, "ServiceName": str},
    total=False,
)


class ClientListServicesResponseServicesTypeDef(
    _ClientListServicesResponseServicesTypeDef
):
    """
    Type definition for `ClientListServicesResponse` `Services`

    A structure that contains the ``ServiceName`` and ``ServiceCode`` . It does not include all
    details of the service quota. To get those values, use the  ListServiceQuotas operation.

    - **ServiceCode** *(string) --*

      Specifies the service that you want to use.

    - **ServiceName** *(string) --*

      The name of the AWS service specified in the increase request.
    """


_ClientListServicesResponseTypeDef = TypedDict(
    "_ClientListServicesResponseTypeDef",
    {"NextToken": str, "Services": List[ClientListServicesResponseServicesTypeDef]},
    total=False,
)


class ClientListServicesResponseTypeDef(_ClientListServicesResponseTypeDef):
    """
    Type definition for `ClientListServices` `Response`

    - **NextToken** *(string) --*

      If present in the response, this value indicates there's more output available that what's
      included in the current response. This can occur even when the response includes no values at
      all, such as when you ask for a filtered view of a very long list. Use this value in the
      ``NextToken`` request parameter in a subsequent call to the operation to continue processing
      and get the next part of the output. You should repeat this until the ``NextToken`` response
      element comes back empty (as ``null`` ).

    - **Services** *(list) --*

      Returns a list of services.

      - *(dict) --*

        A structure that contains the ``ServiceName`` and ``ServiceCode`` . It does not include all
        details of the service quota. To get those values, use the  ListServiceQuotas operation.

        - **ServiceCode** *(string) --*

          Specifies the service that you want to use.

        - **ServiceName** *(string) --*

          The name of the AWS service specified in the increase request.
    """


_ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef = TypedDict(
    "_ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "AwsRegion": str,
        "Unit": str,
        "GlobalQuota": bool,
    },
    total=False,
)


class ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef(
    _ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef
):
    """
    Type definition for `ClientPutServiceQuotaIncreaseRequestIntoTemplateResponse` `ServiceQuotaIncreaseRequestInTemplate`

    A structure that contains information about one service quota increase request.

    - **ServiceCode** *(string) --*

      The code identifier for the AWS service specified in the increase request.

    - **ServiceName** *(string) --*

      The name of the AWS service specified in the increase request.

    - **QuotaCode** *(string) --*

      The code identifier for the service quota specified in the increase request.

    - **QuotaName** *(string) --*

      The name of the service quota in the increase request.

    - **DesiredValue** *(float) --*

      Identifies the new, increased value of the service quota in the increase request.

    - **AwsRegion** *(string) --*

      The AWS Region where the increase request occurs.

    - **Unit** *(string) --*

      The unit of measure for the increase request.

    - **GlobalQuota** *(boolean) --*

      Specifies if the quota is a global quota.
    """


_ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef = TypedDict(
    "_ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplate": ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseServiceQuotaIncreaseRequestInTemplateTypeDef
    },
    total=False,
)


class ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef(
    _ClientPutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef
):
    """
    Type definition for `ClientPutServiceQuotaIncreaseRequestIntoTemplate` `Response`

    - **ServiceQuotaIncreaseRequestInTemplate** *(dict) --*

      A structure that contains information about one service quota increase request.

      - **ServiceCode** *(string) --*

        The code identifier for the AWS service specified in the increase request.

      - **ServiceName** *(string) --*

        The name of the AWS service specified in the increase request.

      - **QuotaCode** *(string) --*

        The code identifier for the service quota specified in the increase request.

      - **QuotaName** *(string) --*

        The name of the service quota in the increase request.

      - **DesiredValue** *(float) --*

        Identifies the new, increased value of the service quota in the increase request.

      - **AwsRegion** *(string) --*

        The AWS Region where the increase request occurs.

      - **Unit** *(string) --*

        The unit of measure for the increase request.

      - **GlobalQuota** *(boolean) --*

        Specifies if the quota is a global quota.
    """


_ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef = TypedDict(
    "_ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": str,
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
    },
    total=False,
)


class ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef(
    _ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef
):
    """
    Type definition for `ClientRequestServiceQuotaIncreaseResponse` `RequestedQuota`

    Returns a list of service quota requests.

    - **Id** *(string) --*

      The unique identifier of a requested service quota change.

    - **CaseId** *(string) --*

      The case Id for the service quota increase request.

    - **ServiceCode** *(string) --*

      Specifies the service that you want to use.

    - **ServiceName** *(string) --*

      The name of the AWS service specified in the increase request.

    - **QuotaCode** *(string) --*

      Specifies the service quota that you want to use.

    - **QuotaName** *(string) --*

      Name of the service quota.

    - **DesiredValue** *(float) --*

      New increased value for the service quota.

    - **Status** *(string) --*

      State of the service quota increase request.

    - **Created** *(datetime) --*

      The date and time when the service quota increase request was received and the case Id was
      created.

    - **LastUpdated** *(datetime) --*

      The date and time of the most recent change in the service quota increase request.

    - **Requester** *(string) --*

      The IAM identity who submitted the service quota increase request.

    - **QuotaArn** *(string) --*

      The Amazon Resource Name (ARN) of the service quota.

    - **GlobalQuota** *(boolean) --*

      Identifies if the quota is global.

    - **Unit** *(string) --*

      Specifies the unit used for the quota.
    """


_ClientRequestServiceQuotaIncreaseResponseTypeDef = TypedDict(
    "_ClientRequestServiceQuotaIncreaseResponseTypeDef",
    {"RequestedQuota": ClientRequestServiceQuotaIncreaseResponseRequestedQuotaTypeDef},
    total=False,
)


class ClientRequestServiceQuotaIncreaseResponseTypeDef(
    _ClientRequestServiceQuotaIncreaseResponseTypeDef
):
    """
    Type definition for `ClientRequestServiceQuotaIncrease` `Response`

    - **RequestedQuota** *(dict) --*

      Returns a list of service quota requests.

      - **Id** *(string) --*

        The unique identifier of a requested service quota change.

      - **CaseId** *(string) --*

        The case Id for the service quota increase request.

      - **ServiceCode** *(string) --*

        Specifies the service that you want to use.

      - **ServiceName** *(string) --*

        The name of the AWS service specified in the increase request.

      - **QuotaCode** *(string) --*

        Specifies the service quota that you want to use.

      - **QuotaName** *(string) --*

        Name of the service quota.

      - **DesiredValue** *(float) --*

        New increased value for the service quota.

      - **Status** *(string) --*

        State of the service quota increase request.

      - **Created** *(datetime) --*

        The date and time when the service quota increase request was received and the case Id was
        created.

      - **LastUpdated** *(datetime) --*

        The date and time of the most recent change in the service quota increase request.

      - **Requester** *(string) --*

        The IAM identity who submitted the service quota increase request.

      - **QuotaArn** *(string) --*

        The Amazon Resource Name (ARN) of the service quota.

      - **GlobalQuota** *(boolean) --*

        Identifies if the quota is global.

      - **Unit** *(string) --*

        Specifies the unit used for the quota.
    """


_ListAWSDefaultServiceQuotasPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAWSDefaultServiceQuotasPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAWSDefaultServiceQuotasPaginatePaginationConfigTypeDef(
    _ListAWSDefaultServiceQuotasPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAWSDefaultServiceQuotasPaginate` `PaginationConfig`

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


_ListAWSDefaultServiceQuotasPaginateResponseQuotasErrorReasonTypeDef = TypedDict(
    "_ListAWSDefaultServiceQuotasPaginateResponseQuotasErrorReasonTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ListAWSDefaultServiceQuotasPaginateResponseQuotasErrorReasonTypeDef(
    _ListAWSDefaultServiceQuotasPaginateResponseQuotasErrorReasonTypeDef
):
    """
    Type definition for `ListAWSDefaultServiceQuotasPaginateResponseQuotas` `ErrorReason`

    Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

    - **ErrorCode** *(string) --*

      Service Quotas returns the following error values.

       ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have
       permission to call the service or service quota. To resolve the error, you need
       permission to access the service or service quota.

       ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is
       throttling Service Quotas.

       ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has
       availability issues.

       ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
       Quotas.

    - **ErrorMessage** *(string) --*

      The error message that provides more detail.
    """


_ListAWSDefaultServiceQuotasPaginateResponseQuotasPeriodTypeDef = TypedDict(
    "_ListAWSDefaultServiceQuotasPaginateResponseQuotasPeriodTypeDef",
    {"PeriodValue": int, "PeriodUnit": str},
    total=False,
)


class ListAWSDefaultServiceQuotasPaginateResponseQuotasPeriodTypeDef(
    _ListAWSDefaultServiceQuotasPaginateResponseQuotasPeriodTypeDef
):
    """
    Type definition for `ListAWSDefaultServiceQuotasPaginateResponseQuotas` `Period`

    Identifies the unit and value of how time is measured.

    - **PeriodValue** *(integer) --*

      The value of a period.

    - **PeriodUnit** *(string) --*

      The time unit of a period.
    """


_ListAWSDefaultServiceQuotasPaginateResponseQuotasUsageMetricTypeDef = TypedDict(
    "_ListAWSDefaultServiceQuotasPaginateResponseQuotasUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)


class ListAWSDefaultServiceQuotasPaginateResponseQuotasUsageMetricTypeDef(
    _ListAWSDefaultServiceQuotasPaginateResponseQuotasUsageMetricTypeDef
):
    """
    Type definition for `ListAWSDefaultServiceQuotasPaginateResponseQuotas` `UsageMetric`

    Specifies the details about the measurement.

    - **MetricNamespace** *(string) --*

      The namespace of the metric. The namespace is a container for CloudWatch metrics. You
      can specify a name for the namespace when you create a metric.

    - **MetricName** *(string) --*

      The name of the CloudWatch metric that measures usage of a service quota. This is a
      required field.

    - **MetricDimensions** *(dict) --*

      A dimension is a name/value pair that is part of the identity of a metric. Every metric
      has specific characteristics that describe it, and you can think of dimensions as
      categories for those characteristics. These dimensions are part of the CloudWatch
      Metric Identity that measures usage against a particular service quota.

      - *(string) --*

        - *(string) --*

    - **MetricStatisticRecommendation** *(string) --*

      Statistics are metric data aggregations over specified periods of time. This is the
      recommended statistic to use when comparing usage in the CloudWatch Metric against your
      Service Quota.
    """


_ListAWSDefaultServiceQuotasPaginateResponseQuotasTypeDef = TypedDict(
    "_ListAWSDefaultServiceQuotasPaginateResponseQuotasTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": ListAWSDefaultServiceQuotasPaginateResponseQuotasUsageMetricTypeDef,
        "Period": ListAWSDefaultServiceQuotasPaginateResponseQuotasPeriodTypeDef,
        "ErrorReason": ListAWSDefaultServiceQuotasPaginateResponseQuotasErrorReasonTypeDef,
    },
    total=False,
)


class ListAWSDefaultServiceQuotasPaginateResponseQuotasTypeDef(
    _ListAWSDefaultServiceQuotasPaginateResponseQuotasTypeDef
):
    """
    Type definition for `ListAWSDefaultServiceQuotasPaginateResponse` `Quotas`

    A structure that contains the full set of details that define the service quota.

    - **ServiceCode** *(string) --*

      Specifies the service that you want to use.

    - **ServiceName** *(string) --*

      The name of the AWS service specified in the increase request.

    - **QuotaArn** *(string) --*

      The Amazon Resource Name (ARN) of the service quota.

    - **QuotaCode** *(string) --*

      The code identifier for the service quota specified.

    - **QuotaName** *(string) --*

      The name identifier of the service quota.

    - **Value** *(float) --*

      The value of service quota.

    - **Unit** *(string) --*

      The unit of measurement for the value of the service quota.

    - **Adjustable** *(boolean) --*

      Specifies if the quota value can be increased.

    - **GlobalQuota** *(boolean) --*

      Specifies if the quota is global.

    - **UsageMetric** *(dict) --*

      Specifies the details about the measurement.

      - **MetricNamespace** *(string) --*

        The namespace of the metric. The namespace is a container for CloudWatch metrics. You
        can specify a name for the namespace when you create a metric.

      - **MetricName** *(string) --*

        The name of the CloudWatch metric that measures usage of a service quota. This is a
        required field.

      - **MetricDimensions** *(dict) --*

        A dimension is a name/value pair that is part of the identity of a metric. Every metric
        has specific characteristics that describe it, and you can think of dimensions as
        categories for those characteristics. These dimensions are part of the CloudWatch
        Metric Identity that measures usage against a particular service quota.

        - *(string) --*

          - *(string) --*

      - **MetricStatisticRecommendation** *(string) --*

        Statistics are metric data aggregations over specified periods of time. This is the
        recommended statistic to use when comparing usage in the CloudWatch Metric against your
        Service Quota.

    - **Period** *(dict) --*

      Identifies the unit and value of how time is measured.

      - **PeriodValue** *(integer) --*

        The value of a period.

      - **PeriodUnit** *(string) --*

        The time unit of a period.

    - **ErrorReason** *(dict) --*

      Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

      - **ErrorCode** *(string) --*

        Service Quotas returns the following error values.

         ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have
         permission to call the service or service quota. To resolve the error, you need
         permission to access the service or service quota.

         ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is
         throttling Service Quotas.

         ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has
         availability issues.

         ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
         Quotas.

      - **ErrorMessage** *(string) --*

        The error message that provides more detail.
    """


_ListAWSDefaultServiceQuotasPaginateResponseTypeDef = TypedDict(
    "_ListAWSDefaultServiceQuotasPaginateResponseTypeDef",
    {"Quotas": List[ListAWSDefaultServiceQuotasPaginateResponseQuotasTypeDef]},
    total=False,
)


class ListAWSDefaultServiceQuotasPaginateResponseTypeDef(
    _ListAWSDefaultServiceQuotasPaginateResponseTypeDef
):
    """
    Type definition for `ListAWSDefaultServiceQuotasPaginate` `Response`

    - **Quotas** *(list) --*

      A list of the quotas in the account with the AWS default values.

      - *(dict) --*

        A structure that contains the full set of details that define the service quota.

        - **ServiceCode** *(string) --*

          Specifies the service that you want to use.

        - **ServiceName** *(string) --*

          The name of the AWS service specified in the increase request.

        - **QuotaArn** *(string) --*

          The Amazon Resource Name (ARN) of the service quota.

        - **QuotaCode** *(string) --*

          The code identifier for the service quota specified.

        - **QuotaName** *(string) --*

          The name identifier of the service quota.

        - **Value** *(float) --*

          The value of service quota.

        - **Unit** *(string) --*

          The unit of measurement for the value of the service quota.

        - **Adjustable** *(boolean) --*

          Specifies if the quota value can be increased.

        - **GlobalQuota** *(boolean) --*

          Specifies if the quota is global.

        - **UsageMetric** *(dict) --*

          Specifies the details about the measurement.

          - **MetricNamespace** *(string) --*

            The namespace of the metric. The namespace is a container for CloudWatch metrics. You
            can specify a name for the namespace when you create a metric.

          - **MetricName** *(string) --*

            The name of the CloudWatch metric that measures usage of a service quota. This is a
            required field.

          - **MetricDimensions** *(dict) --*

            A dimension is a name/value pair that is part of the identity of a metric. Every metric
            has specific characteristics that describe it, and you can think of dimensions as
            categories for those characteristics. These dimensions are part of the CloudWatch
            Metric Identity that measures usage against a particular service quota.

            - *(string) --*

              - *(string) --*

          - **MetricStatisticRecommendation** *(string) --*

            Statistics are metric data aggregations over specified periods of time. This is the
            recommended statistic to use when comparing usage in the CloudWatch Metric against your
            Service Quota.

        - **Period** *(dict) --*

          Identifies the unit and value of how time is measured.

          - **PeriodValue** *(integer) --*

            The value of a period.

          - **PeriodUnit** *(string) --*

            The time unit of a period.

        - **ErrorReason** *(dict) --*

          Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

          - **ErrorCode** *(string) --*

            Service Quotas returns the following error values.

             ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have
             permission to call the service or service quota. To resolve the error, you need
             permission to access the service or service quota.

             ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is
             throttling Service Quotas.

             ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has
             availability issues.

             ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
             Quotas.

          - **ErrorMessage** *(string) --*

            The error message that provides more detail.
    """


_ListRequestedServiceQuotaChangeHistoryByQuotaPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRequestedServiceQuotaChangeHistoryByQuotaPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRequestedServiceQuotaChangeHistoryByQuotaPaginatePaginationConfigTypeDef(
    _ListRequestedServiceQuotaChangeHistoryByQuotaPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRequestedServiceQuotaChangeHistoryByQuotaPaginate` `PaginationConfig`

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


_ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseRequestedQuotasTypeDef = TypedDict(
    "_ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseRequestedQuotasTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": str,
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
    },
    total=False,
)


class ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseRequestedQuotasTypeDef(
    _ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseRequestedQuotasTypeDef
):
    """
    Type definition for `ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponse` `RequestedQuotas`

    A structure that contains information about a requested change for a quota.

    - **Id** *(string) --*

      The unique identifier of a requested service quota change.

    - **CaseId** *(string) --*

      The case Id for the service quota increase request.

    - **ServiceCode** *(string) --*

      Specifies the service that you want to use.

    - **ServiceName** *(string) --*

      The name of the AWS service specified in the increase request.

    - **QuotaCode** *(string) --*

      Specifies the service quota that you want to use.

    - **QuotaName** *(string) --*

      Name of the service quota.

    - **DesiredValue** *(float) --*

      New increased value for the service quota.

    - **Status** *(string) --*

      State of the service quota increase request.

    - **Created** *(datetime) --*

      The date and time when the service quota increase request was received and the case Id
      was created.

    - **LastUpdated** *(datetime) --*

      The date and time of the most recent change in the service quota increase request.

    - **Requester** *(string) --*

      The IAM identity who submitted the service quota increase request.

    - **QuotaArn** *(string) --*

      The Amazon Resource Name (ARN) of the service quota.

    - **GlobalQuota** *(boolean) --*

      Identifies if the quota is global.

    - **Unit** *(string) --*

      Specifies the unit used for the quota.
    """


_ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseTypeDef = TypedDict(
    "_ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseTypeDef",
    {
        "RequestedQuotas": List[
            ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseRequestedQuotasTypeDef
        ]
    },
    total=False,
)


class ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseTypeDef(
    _ListRequestedServiceQuotaChangeHistoryByQuotaPaginateResponseTypeDef
):
    """
    Type definition for `ListRequestedServiceQuotaChangeHistoryByQuotaPaginate` `Response`

    - **RequestedQuotas** *(list) --*

      Returns a list of service quota requests.

      - *(dict) --*

        A structure that contains information about a requested change for a quota.

        - **Id** *(string) --*

          The unique identifier of a requested service quota change.

        - **CaseId** *(string) --*

          The case Id for the service quota increase request.

        - **ServiceCode** *(string) --*

          Specifies the service that you want to use.

        - **ServiceName** *(string) --*

          The name of the AWS service specified in the increase request.

        - **QuotaCode** *(string) --*

          Specifies the service quota that you want to use.

        - **QuotaName** *(string) --*

          Name of the service quota.

        - **DesiredValue** *(float) --*

          New increased value for the service quota.

        - **Status** *(string) --*

          State of the service quota increase request.

        - **Created** *(datetime) --*

          The date and time when the service quota increase request was received and the case Id
          was created.

        - **LastUpdated** *(datetime) --*

          The date and time of the most recent change in the service quota increase request.

        - **Requester** *(string) --*

          The IAM identity who submitted the service quota increase request.

        - **QuotaArn** *(string) --*

          The Amazon Resource Name (ARN) of the service quota.

        - **GlobalQuota** *(boolean) --*

          Identifies if the quota is global.

        - **Unit** *(string) --*

          Specifies the unit used for the quota.
    """


_ListRequestedServiceQuotaChangeHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRequestedServiceQuotaChangeHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRequestedServiceQuotaChangeHistoryPaginatePaginationConfigTypeDef(
    _ListRequestedServiceQuotaChangeHistoryPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRequestedServiceQuotaChangeHistoryPaginate` `PaginationConfig`

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


_ListRequestedServiceQuotaChangeHistoryPaginateResponseRequestedQuotasTypeDef = TypedDict(
    "_ListRequestedServiceQuotaChangeHistoryPaginateResponseRequestedQuotasTypeDef",
    {
        "Id": str,
        "CaseId": str,
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "Status": str,
        "Created": datetime,
        "LastUpdated": datetime,
        "Requester": str,
        "QuotaArn": str,
        "GlobalQuota": bool,
        "Unit": str,
    },
    total=False,
)


class ListRequestedServiceQuotaChangeHistoryPaginateResponseRequestedQuotasTypeDef(
    _ListRequestedServiceQuotaChangeHistoryPaginateResponseRequestedQuotasTypeDef
):
    """
    Type definition for `ListRequestedServiceQuotaChangeHistoryPaginateResponse` `RequestedQuotas`

    A structure that contains information about a requested change for a quota.

    - **Id** *(string) --*

      The unique identifier of a requested service quota change.

    - **CaseId** *(string) --*

      The case Id for the service quota increase request.

    - **ServiceCode** *(string) --*

      Specifies the service that you want to use.

    - **ServiceName** *(string) --*

      The name of the AWS service specified in the increase request.

    - **QuotaCode** *(string) --*

      Specifies the service quota that you want to use.

    - **QuotaName** *(string) --*

      Name of the service quota.

    - **DesiredValue** *(float) --*

      New increased value for the service quota.

    - **Status** *(string) --*

      State of the service quota increase request.

    - **Created** *(datetime) --*

      The date and time when the service quota increase request was received and the case Id
      was created.

    - **LastUpdated** *(datetime) --*

      The date and time of the most recent change in the service quota increase request.

    - **Requester** *(string) --*

      The IAM identity who submitted the service quota increase request.

    - **QuotaArn** *(string) --*

      The Amazon Resource Name (ARN) of the service quota.

    - **GlobalQuota** *(boolean) --*

      Identifies if the quota is global.

    - **Unit** *(string) --*

      Specifies the unit used for the quota.
    """


_ListRequestedServiceQuotaChangeHistoryPaginateResponseTypeDef = TypedDict(
    "_ListRequestedServiceQuotaChangeHistoryPaginateResponseTypeDef",
    {
        "RequestedQuotas": List[
            ListRequestedServiceQuotaChangeHistoryPaginateResponseRequestedQuotasTypeDef
        ]
    },
    total=False,
)


class ListRequestedServiceQuotaChangeHistoryPaginateResponseTypeDef(
    _ListRequestedServiceQuotaChangeHistoryPaginateResponseTypeDef
):
    """
    Type definition for `ListRequestedServiceQuotaChangeHistoryPaginate` `Response`

    - **RequestedQuotas** *(list) --*

      Returns a list of service quota requests.

      - *(dict) --*

        A structure that contains information about a requested change for a quota.

        - **Id** *(string) --*

          The unique identifier of a requested service quota change.

        - **CaseId** *(string) --*

          The case Id for the service quota increase request.

        - **ServiceCode** *(string) --*

          Specifies the service that you want to use.

        - **ServiceName** *(string) --*

          The name of the AWS service specified in the increase request.

        - **QuotaCode** *(string) --*

          Specifies the service quota that you want to use.

        - **QuotaName** *(string) --*

          Name of the service quota.

        - **DesiredValue** *(float) --*

          New increased value for the service quota.

        - **Status** *(string) --*

          State of the service quota increase request.

        - **Created** *(datetime) --*

          The date and time when the service quota increase request was received and the case Id
          was created.

        - **LastUpdated** *(datetime) --*

          The date and time of the most recent change in the service quota increase request.

        - **Requester** *(string) --*

          The IAM identity who submitted the service quota increase request.

        - **QuotaArn** *(string) --*

          The Amazon Resource Name (ARN) of the service quota.

        - **GlobalQuota** *(boolean) --*

          Identifies if the quota is global.

        - **Unit** *(string) --*

          Specifies the unit used for the quota.
    """


_ListServiceQuotaIncreaseRequestsInTemplatePaginatePaginationConfigTypeDef = TypedDict(
    "_ListServiceQuotaIncreaseRequestsInTemplatePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListServiceQuotaIncreaseRequestsInTemplatePaginatePaginationConfigTypeDef(
    _ListServiceQuotaIncreaseRequestsInTemplatePaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListServiceQuotaIncreaseRequestsInTemplatePaginate` `PaginationConfig`

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


_ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef = TypedDict(
    "_ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaCode": str,
        "QuotaName": str,
        "DesiredValue": float,
        "AwsRegion": str,
        "Unit": str,
        "GlobalQuota": bool,
    },
    total=False,
)


class ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef(
    _ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef
):
    """
    Type definition for `ListServiceQuotaIncreaseRequestsInTemplatePaginateResponse` `ServiceQuotaIncreaseRequestInTemplateList`

    A structure that contains information about one service quota increase request.

    - **ServiceCode** *(string) --*

      The code identifier for the AWS service specified in the increase request.

    - **ServiceName** *(string) --*

      The name of the AWS service specified in the increase request.

    - **QuotaCode** *(string) --*

      The code identifier for the service quota specified in the increase request.

    - **QuotaName** *(string) --*

      The name of the service quota in the increase request.

    - **DesiredValue** *(float) --*

      Identifies the new, increased value of the service quota in the increase request.

    - **AwsRegion** *(string) --*

      The AWS Region where the increase request occurs.

    - **Unit** *(string) --*

      The unit of measure for the increase request.

    - **GlobalQuota** *(boolean) --*

      Specifies if the quota is a global quota.
    """


_ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseTypeDef = TypedDict(
    "_ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseTypeDef",
    {
        "ServiceQuotaIncreaseRequestInTemplateList": List[
            ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseServiceQuotaIncreaseRequestInTemplateListTypeDef
        ]
    },
    total=False,
)


class ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseTypeDef(
    _ListServiceQuotaIncreaseRequestsInTemplatePaginateResponseTypeDef
):
    """
    Type definition for `ListServiceQuotaIncreaseRequestsInTemplatePaginate` `Response`

    - **ServiceQuotaIncreaseRequestInTemplateList** *(list) --*

      Returns the list of values of the quota increase request in the template.

      - *(dict) --*

        A structure that contains information about one service quota increase request.

        - **ServiceCode** *(string) --*

          The code identifier for the AWS service specified in the increase request.

        - **ServiceName** *(string) --*

          The name of the AWS service specified in the increase request.

        - **QuotaCode** *(string) --*

          The code identifier for the service quota specified in the increase request.

        - **QuotaName** *(string) --*

          The name of the service quota in the increase request.

        - **DesiredValue** *(float) --*

          Identifies the new, increased value of the service quota in the increase request.

        - **AwsRegion** *(string) --*

          The AWS Region where the increase request occurs.

        - **Unit** *(string) --*

          The unit of measure for the increase request.

        - **GlobalQuota** *(boolean) --*

          Specifies if the quota is a global quota.
    """


_ListServiceQuotasPaginatePaginationConfigTypeDef = TypedDict(
    "_ListServiceQuotasPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListServiceQuotasPaginatePaginationConfigTypeDef(
    _ListServiceQuotasPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListServiceQuotasPaginate` `PaginationConfig`

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


_ListServiceQuotasPaginateResponseQuotasErrorReasonTypeDef = TypedDict(
    "_ListServiceQuotasPaginateResponseQuotasErrorReasonTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ListServiceQuotasPaginateResponseQuotasErrorReasonTypeDef(
    _ListServiceQuotasPaginateResponseQuotasErrorReasonTypeDef
):
    """
    Type definition for `ListServiceQuotasPaginateResponseQuotas` `ErrorReason`

    Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

    - **ErrorCode** *(string) --*

      Service Quotas returns the following error values.

       ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have
       permission to call the service or service quota. To resolve the error, you need
       permission to access the service or service quota.

       ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is
       throttling Service Quotas.

       ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has
       availability issues.

       ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
       Quotas.

    - **ErrorMessage** *(string) --*

      The error message that provides more detail.
    """


_ListServiceQuotasPaginateResponseQuotasPeriodTypeDef = TypedDict(
    "_ListServiceQuotasPaginateResponseQuotasPeriodTypeDef",
    {"PeriodValue": int, "PeriodUnit": str},
    total=False,
)


class ListServiceQuotasPaginateResponseQuotasPeriodTypeDef(
    _ListServiceQuotasPaginateResponseQuotasPeriodTypeDef
):
    """
    Type definition for `ListServiceQuotasPaginateResponseQuotas` `Period`

    Identifies the unit and value of how time is measured.

    - **PeriodValue** *(integer) --*

      The value of a period.

    - **PeriodUnit** *(string) --*

      The time unit of a period.
    """


_ListServiceQuotasPaginateResponseQuotasUsageMetricTypeDef = TypedDict(
    "_ListServiceQuotasPaginateResponseQuotasUsageMetricTypeDef",
    {
        "MetricNamespace": str,
        "MetricName": str,
        "MetricDimensions": Dict[str, str],
        "MetricStatisticRecommendation": str,
    },
    total=False,
)


class ListServiceQuotasPaginateResponseQuotasUsageMetricTypeDef(
    _ListServiceQuotasPaginateResponseQuotasUsageMetricTypeDef
):
    """
    Type definition for `ListServiceQuotasPaginateResponseQuotas` `UsageMetric`

    Specifies the details about the measurement.

    - **MetricNamespace** *(string) --*

      The namespace of the metric. The namespace is a container for CloudWatch metrics. You
      can specify a name for the namespace when you create a metric.

    - **MetricName** *(string) --*

      The name of the CloudWatch metric that measures usage of a service quota. This is a
      required field.

    - **MetricDimensions** *(dict) --*

      A dimension is a name/value pair that is part of the identity of a metric. Every metric
      has specific characteristics that describe it, and you can think of dimensions as
      categories for those characteristics. These dimensions are part of the CloudWatch
      Metric Identity that measures usage against a particular service quota.

      - *(string) --*

        - *(string) --*

    - **MetricStatisticRecommendation** *(string) --*

      Statistics are metric data aggregations over specified periods of time. This is the
      recommended statistic to use when comparing usage in the CloudWatch Metric against your
      Service Quota.
    """


_ListServiceQuotasPaginateResponseQuotasTypeDef = TypedDict(
    "_ListServiceQuotasPaginateResponseQuotasTypeDef",
    {
        "ServiceCode": str,
        "ServiceName": str,
        "QuotaArn": str,
        "QuotaCode": str,
        "QuotaName": str,
        "Value": float,
        "Unit": str,
        "Adjustable": bool,
        "GlobalQuota": bool,
        "UsageMetric": ListServiceQuotasPaginateResponseQuotasUsageMetricTypeDef,
        "Period": ListServiceQuotasPaginateResponseQuotasPeriodTypeDef,
        "ErrorReason": ListServiceQuotasPaginateResponseQuotasErrorReasonTypeDef,
    },
    total=False,
)


class ListServiceQuotasPaginateResponseQuotasTypeDef(
    _ListServiceQuotasPaginateResponseQuotasTypeDef
):
    """
    Type definition for `ListServiceQuotasPaginateResponse` `Quotas`

    A structure that contains the full set of details that define the service quota.

    - **ServiceCode** *(string) --*

      Specifies the service that you want to use.

    - **ServiceName** *(string) --*

      The name of the AWS service specified in the increase request.

    - **QuotaArn** *(string) --*

      The Amazon Resource Name (ARN) of the service quota.

    - **QuotaCode** *(string) --*

      The code identifier for the service quota specified.

    - **QuotaName** *(string) --*

      The name identifier of the service quota.

    - **Value** *(float) --*

      The value of service quota.

    - **Unit** *(string) --*

      The unit of measurement for the value of the service quota.

    - **Adjustable** *(boolean) --*

      Specifies if the quota value can be increased.

    - **GlobalQuota** *(boolean) --*

      Specifies if the quota is global.

    - **UsageMetric** *(dict) --*

      Specifies the details about the measurement.

      - **MetricNamespace** *(string) --*

        The namespace of the metric. The namespace is a container for CloudWatch metrics. You
        can specify a name for the namespace when you create a metric.

      - **MetricName** *(string) --*

        The name of the CloudWatch metric that measures usage of a service quota. This is a
        required field.

      - **MetricDimensions** *(dict) --*

        A dimension is a name/value pair that is part of the identity of a metric. Every metric
        has specific characteristics that describe it, and you can think of dimensions as
        categories for those characteristics. These dimensions are part of the CloudWatch
        Metric Identity that measures usage against a particular service quota.

        - *(string) --*

          - *(string) --*

      - **MetricStatisticRecommendation** *(string) --*

        Statistics are metric data aggregations over specified periods of time. This is the
        recommended statistic to use when comparing usage in the CloudWatch Metric against your
        Service Quota.

    - **Period** *(dict) --*

      Identifies the unit and value of how time is measured.

      - **PeriodValue** *(integer) --*

        The value of a period.

      - **PeriodUnit** *(string) --*

        The time unit of a period.

    - **ErrorReason** *(dict) --*

      Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

      - **ErrorCode** *(string) --*

        Service Quotas returns the following error values.

         ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have
         permission to call the service or service quota. To resolve the error, you need
         permission to access the service or service quota.

         ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is
         throttling Service Quotas.

         ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has
         availability issues.

         ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
         Quotas.

      - **ErrorMessage** *(string) --*

        The error message that provides more detail.
    """


_ListServiceQuotasPaginateResponseTypeDef = TypedDict(
    "_ListServiceQuotasPaginateResponseTypeDef",
    {"Quotas": List[ListServiceQuotasPaginateResponseQuotasTypeDef]},
    total=False,
)


class ListServiceQuotasPaginateResponseTypeDef(
    _ListServiceQuotasPaginateResponseTypeDef
):
    """
    Type definition for `ListServiceQuotasPaginate` `Response`

    - **Quotas** *(list) --*

      The response information for a quota lists all attribute information for the quota.

      - *(dict) --*

        A structure that contains the full set of details that define the service quota.

        - **ServiceCode** *(string) --*

          Specifies the service that you want to use.

        - **ServiceName** *(string) --*

          The name of the AWS service specified in the increase request.

        - **QuotaArn** *(string) --*

          The Amazon Resource Name (ARN) of the service quota.

        - **QuotaCode** *(string) --*

          The code identifier for the service quota specified.

        - **QuotaName** *(string) --*

          The name identifier of the service quota.

        - **Value** *(float) --*

          The value of service quota.

        - **Unit** *(string) --*

          The unit of measurement for the value of the service quota.

        - **Adjustable** *(boolean) --*

          Specifies if the quota value can be increased.

        - **GlobalQuota** *(boolean) --*

          Specifies if the quota is global.

        - **UsageMetric** *(dict) --*

          Specifies the details about the measurement.

          - **MetricNamespace** *(string) --*

            The namespace of the metric. The namespace is a container for CloudWatch metrics. You
            can specify a name for the namespace when you create a metric.

          - **MetricName** *(string) --*

            The name of the CloudWatch metric that measures usage of a service quota. This is a
            required field.

          - **MetricDimensions** *(dict) --*

            A dimension is a name/value pair that is part of the identity of a metric. Every metric
            has specific characteristics that describe it, and you can think of dimensions as
            categories for those characteristics. These dimensions are part of the CloudWatch
            Metric Identity that measures usage against a particular service quota.

            - *(string) --*

              - *(string) --*

          - **MetricStatisticRecommendation** *(string) --*

            Statistics are metric data aggregations over specified periods of time. This is the
            recommended statistic to use when comparing usage in the CloudWatch Metric against your
            Service Quota.

        - **Period** *(dict) --*

          Identifies the unit and value of how time is measured.

          - **PeriodValue** *(integer) --*

            The value of a period.

          - **PeriodUnit** *(string) --*

            The time unit of a period.

        - **ErrorReason** *(dict) --*

          Specifies the ``ErrorCode`` and ``ErrorMessage`` when success isn't achieved.

          - **ErrorCode** *(string) --*

            Service Quotas returns the following error values.

             ``DEPENDENCY_ACCESS_DENIED_ERROR`` is returned when the caller does not have
             permission to call the service or service quota. To resolve the error, you need
             permission to access the service or service quota.

             ``DEPENDENCY_THROTTLING_ERROR`` is returned when the service being called is
             throttling Service Quotas.

             ``DEPENDENCY_SERVICE_ERROR`` is returned when the service being called has
             availability issues.

             ``SERVICE_QUOTA_NOT_AVAILABLE_ERROR`` is returned when there was an error in Service
             Quotas.

          - **ErrorMessage** *(string) --*

            The error message that provides more detail.
    """


_ListServicesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListServicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListServicesPaginatePaginationConfigTypeDef(
    _ListServicesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListServicesPaginate` `PaginationConfig`

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


_ListServicesPaginateResponseServicesTypeDef = TypedDict(
    "_ListServicesPaginateResponseServicesTypeDef",
    {"ServiceCode": str, "ServiceName": str},
    total=False,
)


class ListServicesPaginateResponseServicesTypeDef(
    _ListServicesPaginateResponseServicesTypeDef
):
    """
    Type definition for `ListServicesPaginateResponse` `Services`

    A structure that contains the ``ServiceName`` and ``ServiceCode`` . It does not include all
    details of the service quota. To get those values, use the  ListServiceQuotas operation.

    - **ServiceCode** *(string) --*

      Specifies the service that you want to use.

    - **ServiceName** *(string) --*

      The name of the AWS service specified in the increase request.
    """


_ListServicesPaginateResponseTypeDef = TypedDict(
    "_ListServicesPaginateResponseTypeDef",
    {"Services": List[ListServicesPaginateResponseServicesTypeDef]},
    total=False,
)


class ListServicesPaginateResponseTypeDef(_ListServicesPaginateResponseTypeDef):
    """
    Type definition for `ListServicesPaginate` `Response`

    - **Services** *(list) --*

      Returns a list of services.

      - *(dict) --*

        A structure that contains the ``ServiceName`` and ``ServiceCode`` . It does not include all
        details of the service quota. To get those values, use the  ListServiceQuotas operation.

        - **ServiceCode** *(string) --*

          Specifies the service that you want to use.

        - **ServiceName** *(string) --*

          The name of the AWS service specified in the increase request.
    """

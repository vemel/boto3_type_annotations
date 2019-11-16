"Main interface for elasticbeanstalk type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientApplyEnvironmentManagedActionResponseTypeDef",
    "ClientCheckDnsAvailabilityResponseTypeDef",
    "ClientComposeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef",
    "ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef",
    "ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef",
    "ClientComposeEnvironmentsResponseEnvironmentsResourcesTypeDef",
    "ClientComposeEnvironmentsResponseEnvironmentsTierTypeDef",
    "ClientComposeEnvironmentsResponseEnvironmentsTypeDef",
    "ClientComposeEnvironmentsResponseTypeDef",
    "ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    "ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    "ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    "ClientCreateApplicationResourceLifecycleConfigTypeDef",
    "ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    "ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    "ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    "ClientCreateApplicationResponseApplicationResourceLifecycleConfigTypeDef",
    "ClientCreateApplicationResponseApplicationTypeDef",
    "ClientCreateApplicationResponseTypeDef",
    "ClientCreateApplicationTagsTypeDef",
    "ClientCreateApplicationVersionBuildConfigurationTypeDef",
    "ClientCreateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef",
    "ClientCreateApplicationVersionResponseApplicationVersionSourceBundleTypeDef",
    "ClientCreateApplicationVersionResponseApplicationVersionTypeDef",
    "ClientCreateApplicationVersionResponseTypeDef",
    "ClientCreateApplicationVersionSourceBuildInformationTypeDef",
    "ClientCreateApplicationVersionSourceBundleTypeDef",
    "ClientCreateApplicationVersionTagsTypeDef",
    "ClientCreateConfigurationTemplateOptionSettingsTypeDef",
    "ClientCreateConfigurationTemplateResponseOptionSettingsTypeDef",
    "ClientCreateConfigurationTemplateResponseTypeDef",
    "ClientCreateConfigurationTemplateSourceConfigurationTypeDef",
    "ClientCreateConfigurationTemplateTagsTypeDef",
    "ClientCreateEnvironmentOptionSettingsTypeDef",
    "ClientCreateEnvironmentOptionsToRemoveTypeDef",
    "ClientCreateEnvironmentResponseEnvironmentLinksTypeDef",
    "ClientCreateEnvironmentResponseResourcesLoadBalancerListenersTypeDef",
    "ClientCreateEnvironmentResponseResourcesLoadBalancerTypeDef",
    "ClientCreateEnvironmentResponseResourcesTypeDef",
    "ClientCreateEnvironmentResponseTierTypeDef",
    "ClientCreateEnvironmentResponseTypeDef",
    "ClientCreateEnvironmentTagsTypeDef",
    "ClientCreateEnvironmentTierTypeDef",
    "ClientCreatePlatformVersionOptionSettingsTypeDef",
    "ClientCreatePlatformVersionPlatformDefinitionBundleTypeDef",
    "ClientCreatePlatformVersionResponseBuilderTypeDef",
    "ClientCreatePlatformVersionResponsePlatformSummaryTypeDef",
    "ClientCreatePlatformVersionResponseTypeDef",
    "ClientCreatePlatformVersionTagsTypeDef",
    "ClientCreateStorageLocationResponseTypeDef",
    "ClientDeletePlatformVersionResponsePlatformSummaryTypeDef",
    "ClientDeletePlatformVersionResponseTypeDef",
    "ClientDescribeAccountAttributesResponseResourceQuotasApplicationQuotaTypeDef",
    "ClientDescribeAccountAttributesResponseResourceQuotasApplicationVersionQuotaTypeDef",
    "ClientDescribeAccountAttributesResponseResourceQuotasConfigurationTemplateQuotaTypeDef",
    "ClientDescribeAccountAttributesResponseResourceQuotasCustomPlatformQuotaTypeDef",
    "ClientDescribeAccountAttributesResponseResourceQuotasEnvironmentQuotaTypeDef",
    "ClientDescribeAccountAttributesResponseResourceQuotasTypeDef",
    "ClientDescribeAccountAttributesResponseTypeDef",
    "ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBuildInformationTypeDef",
    "ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBundleTypeDef",
    "ClientDescribeApplicationVersionsResponseApplicationVersionsTypeDef",
    "ClientDescribeApplicationVersionsResponseTypeDef",
    "ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    "ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    "ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    "ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigTypeDef",
    "ClientDescribeApplicationsResponseApplicationsTypeDef",
    "ClientDescribeApplicationsResponseTypeDef",
    "ClientDescribeConfigurationOptionsOptionsTypeDef",
    "ClientDescribeConfigurationOptionsResponseOptionsRegexTypeDef",
    "ClientDescribeConfigurationOptionsResponseOptionsTypeDef",
    "ClientDescribeConfigurationOptionsResponseTypeDef",
    "ClientDescribeConfigurationSettingsResponseConfigurationSettingsOptionSettingsTypeDef",
    "ClientDescribeConfigurationSettingsResponseConfigurationSettingsTypeDef",
    "ClientDescribeConfigurationSettingsResponseTypeDef",
    "ClientDescribeEnvironmentHealthResponseApplicationMetricsLatencyTypeDef",
    "ClientDescribeEnvironmentHealthResponseApplicationMetricsStatusCodesTypeDef",
    "ClientDescribeEnvironmentHealthResponseApplicationMetricsTypeDef",
    "ClientDescribeEnvironmentHealthResponseInstancesHealthTypeDef",
    "ClientDescribeEnvironmentHealthResponseTypeDef",
    "ClientDescribeEnvironmentManagedActionHistoryResponseManagedActionHistoryItemsTypeDef",
    "ClientDescribeEnvironmentManagedActionHistoryResponseTypeDef",
    "ClientDescribeEnvironmentManagedActionsResponseManagedActionsTypeDef",
    "ClientDescribeEnvironmentManagedActionsResponseTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesAutoScalingGroupsTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesInstancesTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchConfigurationsTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchTemplatesTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLoadBalancersTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesQueuesTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTriggersTypeDef",
    "ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTypeDef",
    "ClientDescribeEnvironmentResourcesResponseTypeDef",
    "ClientDescribeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef",
    "ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef",
    "ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef",
    "ClientDescribeEnvironmentsResponseEnvironmentsResourcesTypeDef",
    "ClientDescribeEnvironmentsResponseEnvironmentsTierTypeDef",
    "ClientDescribeEnvironmentsResponseEnvironmentsTypeDef",
    "ClientDescribeEnvironmentsResponseTypeDef",
    "ClientDescribeEventsResponseEventsTypeDef",
    "ClientDescribeEventsResponseTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsLatencyTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsStatusCodesTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListDeploymentTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListSystemCPUUtilizationTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListSystemTypeDef",
    "ClientDescribeInstancesHealthResponseInstanceHealthListTypeDef",
    "ClientDescribeInstancesHealthResponseTypeDef",
    "ClientDescribePlatformVersionResponsePlatformDescriptionCustomAmiListTypeDef",
    "ClientDescribePlatformVersionResponsePlatformDescriptionFrameworksTypeDef",
    "ClientDescribePlatformVersionResponsePlatformDescriptionProgrammingLanguagesTypeDef",
    "ClientDescribePlatformVersionResponsePlatformDescriptionTypeDef",
    "ClientDescribePlatformVersionResponseTypeDef",
    "ClientListAvailableSolutionStacksResponseSolutionStackDetailsTypeDef",
    "ClientListAvailableSolutionStacksResponseTypeDef",
    "ClientListPlatformVersionsFiltersTypeDef",
    "ClientListPlatformVersionsResponsePlatformSummaryListTypeDef",
    "ClientListPlatformVersionsResponseTypeDef",
    "ClientListTagsForResourceResponseResourceTagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientRetrieveEnvironmentInfoResponseEnvironmentInfoTypeDef",
    "ClientRetrieveEnvironmentInfoResponseTypeDef",
    "ClientTerminateEnvironmentResponseEnvironmentLinksTypeDef",
    "ClientTerminateEnvironmentResponseResourcesLoadBalancerListenersTypeDef",
    "ClientTerminateEnvironmentResponseResourcesLoadBalancerTypeDef",
    "ClientTerminateEnvironmentResponseResourcesTypeDef",
    "ClientTerminateEnvironmentResponseTierTypeDef",
    "ClientTerminateEnvironmentResponseTypeDef",
    "ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    "ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    "ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    "ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigTypeDef",
    "ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    "ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    "ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    "ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigTypeDef",
    "ClientUpdateApplicationResourceLifecycleResponseTypeDef",
    "ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    "ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    "ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    "ClientUpdateApplicationResponseApplicationResourceLifecycleConfigTypeDef",
    "ClientUpdateApplicationResponseApplicationTypeDef",
    "ClientUpdateApplicationResponseTypeDef",
    "ClientUpdateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef",
    "ClientUpdateApplicationVersionResponseApplicationVersionSourceBundleTypeDef",
    "ClientUpdateApplicationVersionResponseApplicationVersionTypeDef",
    "ClientUpdateApplicationVersionResponseTypeDef",
    "ClientUpdateConfigurationTemplateOptionSettingsTypeDef",
    "ClientUpdateConfigurationTemplateOptionsToRemoveTypeDef",
    "ClientUpdateConfigurationTemplateResponseOptionSettingsTypeDef",
    "ClientUpdateConfigurationTemplateResponseTypeDef",
    "ClientUpdateEnvironmentOptionSettingsTypeDef",
    "ClientUpdateEnvironmentOptionsToRemoveTypeDef",
    "ClientUpdateEnvironmentResponseEnvironmentLinksTypeDef",
    "ClientUpdateEnvironmentResponseResourcesLoadBalancerListenersTypeDef",
    "ClientUpdateEnvironmentResponseResourcesLoadBalancerTypeDef",
    "ClientUpdateEnvironmentResponseResourcesTypeDef",
    "ClientUpdateEnvironmentResponseTierTypeDef",
    "ClientUpdateEnvironmentResponseTypeDef",
    "ClientUpdateEnvironmentTierTypeDef",
    "ClientUpdateTagsForResourceTagsToAddTypeDef",
    "ClientValidateConfigurationSettingsOptionSettingsTypeDef",
    "ClientValidateConfigurationSettingsResponseMessagesTypeDef",
    "ClientValidateConfigurationSettingsResponseTypeDef",
    "DescribeApplicationVersionsPaginatePaginationConfigTypeDef",
    "DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBuildInformationTypeDef",
    "DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBundleTypeDef",
    "DescribeApplicationVersionsPaginateResponseApplicationVersionsTypeDef",
    "DescribeApplicationVersionsPaginateResponseTypeDef",
    "DescribeEnvironmentManagedActionHistoryPaginatePaginationConfigTypeDef",
    "DescribeEnvironmentManagedActionHistoryPaginateResponseManagedActionHistoryItemsTypeDef",
    "DescribeEnvironmentManagedActionHistoryPaginateResponseTypeDef",
    "DescribeEnvironmentsPaginatePaginationConfigTypeDef",
    "DescribeEnvironmentsPaginateResponseEnvironmentsEnvironmentLinksTypeDef",
    "DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerListenersTypeDef",
    "DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerTypeDef",
    "DescribeEnvironmentsPaginateResponseEnvironmentsResourcesTypeDef",
    "DescribeEnvironmentsPaginateResponseEnvironmentsTierTypeDef",
    "DescribeEnvironmentsPaginateResponseEnvironmentsTypeDef",
    "DescribeEnvironmentsPaginateResponseTypeDef",
    "DescribeEventsPaginatePaginationConfigTypeDef",
    "DescribeEventsPaginateResponseEventsTypeDef",
    "DescribeEventsPaginateResponseTypeDef",
    "ListPlatformVersionsPaginateFiltersTypeDef",
    "ListPlatformVersionsPaginatePaginationConfigTypeDef",
    "ListPlatformVersionsPaginateResponsePlatformSummaryListTypeDef",
    "ListPlatformVersionsPaginateResponseTypeDef",
)


_ClientApplyEnvironmentManagedActionResponseTypeDef = TypedDict(
    "_ClientApplyEnvironmentManagedActionResponseTypeDef",
    {"ActionId": str, "ActionDescription": str, "ActionType": str, "Status": str},
    total=False,
)


class ClientApplyEnvironmentManagedActionResponseTypeDef(
    _ClientApplyEnvironmentManagedActionResponseTypeDef
):
    """
    Type definition for `ClientApplyEnvironmentManagedAction` `Response`

    The result message containing information about the managed action.

    - **ActionId** *(string) --*

      The action ID of the managed action.

    - **ActionDescription** *(string) --*

      A description of the managed action.

    - **ActionType** *(string) --*

      The type of managed action.

    - **Status** *(string) --*

      The status of the managed action.
    """


_ClientCheckDnsAvailabilityResponseTypeDef = TypedDict(
    "_ClientCheckDnsAvailabilityResponseTypeDef",
    {"Available": bool, "FullyQualifiedCNAME": str},
    total=False,
)


class ClientCheckDnsAvailabilityResponseTypeDef(
    _ClientCheckDnsAvailabilityResponseTypeDef
):
    """
    Type definition for `ClientCheckDnsAvailability` `Response`

    Indicates if the specified CNAME is available.

    - **Available** *(boolean) --*

      Indicates if the specified CNAME is available:

      * ``true`` : The CNAME is available.

      * ``false`` : The CNAME is not available.

    - **FullyQualifiedCNAME** *(string) --*

      The fully qualified CNAME to reserve when  CreateEnvironment is called with the provided
      prefix.
    """


_ClientComposeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef = TypedDict(
    "_ClientComposeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef",
    {"LinkName": str, "EnvironmentName": str},
    total=False,
)


class ClientComposeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef(
    _ClientComposeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef
):
    """
    Type definition for `ClientComposeEnvironmentsResponseEnvironments` `EnvironmentLinks`

    A link to another environment, defined in the environment's manifest. Links provide
    connection information in system properties that can be used to connect to another
    environment in the same group. See `Environment Manifest (env.yaml)
    <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__
    for details.

    - **LinkName** *(string) --*

      The name of the link.

    - **EnvironmentName** *(string) --*

      The name of the linked environment (the dependency).
    """


_ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef = TypedDict(
    "_ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef",
    {"Protocol": str, "Port": int},
    total=False,
)


class ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef(
    _ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef
):
    """
    Type definition for `ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancer` `Listeners`

    Describes the properties of a Listener for the LoadBalancer.

    - **Protocol** *(string) --*

      The protocol that is used by the Listener.

    - **Port** *(integer) --*

      The port that is used by the Listener.
    """


_ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef = TypedDict(
    "_ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List[
            ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef
        ],
    },
    total=False,
)


class ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef(
    _ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef
):
    """
    Type definition for `ClientComposeEnvironmentsResponseEnvironmentsResources` `LoadBalancer`

    Describes the LoadBalancer.

    - **LoadBalancerName** *(string) --*

      The name of the LoadBalancer.

    - **Domain** *(string) --*

      The domain name of the LoadBalancer.

    - **Listeners** *(list) --*

      A list of Listeners used by the LoadBalancer.

      - *(dict) --*

        Describes the properties of a Listener for the LoadBalancer.

        - **Protocol** *(string) --*

          The protocol that is used by the Listener.

        - **Port** *(integer) --*

          The port that is used by the Listener.
    """


_ClientComposeEnvironmentsResponseEnvironmentsResourcesTypeDef = TypedDict(
    "_ClientComposeEnvironmentsResponseEnvironmentsResourcesTypeDef",
    {
        "LoadBalancer": ClientComposeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef
    },
    total=False,
)


class ClientComposeEnvironmentsResponseEnvironmentsResourcesTypeDef(
    _ClientComposeEnvironmentsResponseEnvironmentsResourcesTypeDef
):
    """
    Type definition for `ClientComposeEnvironmentsResponseEnvironments` `Resources`

    The description of the AWS resources used by this environment.

    - **LoadBalancer** *(dict) --*

      Describes the LoadBalancer.

      - **LoadBalancerName** *(string) --*

        The name of the LoadBalancer.

      - **Domain** *(string) --*

        The domain name of the LoadBalancer.

      - **Listeners** *(list) --*

        A list of Listeners used by the LoadBalancer.

        - *(dict) --*

          Describes the properties of a Listener for the LoadBalancer.

          - **Protocol** *(string) --*

            The protocol that is used by the Listener.

          - **Port** *(integer) --*

            The port that is used by the Listener.
    """


_ClientComposeEnvironmentsResponseEnvironmentsTierTypeDef = TypedDict(
    "_ClientComposeEnvironmentsResponseEnvironmentsTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)


class ClientComposeEnvironmentsResponseEnvironmentsTierTypeDef(
    _ClientComposeEnvironmentsResponseEnvironmentsTierTypeDef
):
    """
    Type definition for `ClientComposeEnvironmentsResponseEnvironments` `Tier`

    Describes the current tier of this environment.

    - **Name** *(string) --*

      The name of this environment tier.

      Valid values:

      * For *Web server tier* – ``WebServer``

      * For *Worker tier* – ``Worker``

    - **Type** *(string) --*

      The type of this environment tier.

      Valid values:

      * For *Web server tier* – ``Standard``

      * For *Worker tier* – ``SQS/HTTP``

    - **Version** *(string) --*

      The version of this environment tier. When you don't set a value to it, Elastic
      Beanstalk uses the latest compatible worker tier version.

      .. note::

        This member is deprecated. Any specific version that you set may become out of date.
        We recommend leaving it unspecified.
    """


_ClientComposeEnvironmentsResponseEnvironmentsTypeDef = TypedDict(
    "_ClientComposeEnvironmentsResponseEnvironmentsTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": str,
        "AbortableOperationInProgress": bool,
        "Health": str,
        "HealthStatus": str,
        "Resources": ClientComposeEnvironmentsResponseEnvironmentsResourcesTypeDef,
        "Tier": ClientComposeEnvironmentsResponseEnvironmentsTierTypeDef,
        "EnvironmentLinks": List[
            ClientComposeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef
        ],
        "EnvironmentArn": str,
    },
    total=False,
)


class ClientComposeEnvironmentsResponseEnvironmentsTypeDef(
    _ClientComposeEnvironmentsResponseEnvironmentsTypeDef
):
    """
    Type definition for `ClientComposeEnvironmentsResponse` `Environments`

    Describes the properties of an environment.

    - **EnvironmentName** *(string) --*

      The name of this environment.

    - **EnvironmentId** *(string) --*

      The ID of this environment.

    - **ApplicationName** *(string) --*

      The name of the application associated with this environment.

    - **VersionLabel** *(string) --*

      The application version deployed in this environment.

    - **SolutionStackName** *(string) --*

      The name of the ``SolutionStack`` deployed with this environment.

    - **PlatformArn** *(string) --*

      The ARN of the platform.

    - **TemplateName** *(string) --*

      The name of the configuration template used to originally launch this environment.

    - **Description** *(string) --*

      Describes this environment.

    - **EndpointURL** *(string) --*

      For load-balanced, autoscaling environments, the URL to the LoadBalancer. For
      single-instance environments, the IP address of the instance.

    - **CNAME** *(string) --*

      The URL to the CNAME for this environment.

    - **DateCreated** *(datetime) --*

      The creation date for this environment.

    - **DateUpdated** *(datetime) --*

      The last modified date for this environment.

    - **Status** *(string) --*

      The current operational status of the environment:

      * ``Launching`` : Environment is in the process of initial deployment.

      * ``Updating`` : Environment is in the process of updating its configuration settings or
      application version.

      * ``Ready`` : Environment is available to have an action performed on it, such as update
      or terminate.

      * ``Terminating`` : Environment is in the shut-down process.

      * ``Terminated`` : Environment is not running.

    - **AbortableOperationInProgress** *(boolean) --*

      Indicates if there is an in-progress environment configuration update or application
      version deployment that you can cancel.

       ``true:`` There is an update in progress.

       ``false:`` There are no updates currently in progress.

    - **Health** *(string) --*

      Describes the health status of the environment. AWS Elastic Beanstalk indicates the
      failure levels for a running environment:

      * ``Red`` : Indicates the environment is not responsive. Occurs when three or more
      consecutive failures occur for an environment.

      * ``Yellow`` : Indicates that something is wrong. Occurs when two consecutive failures
      occur for an environment.

      * ``Green`` : Indicates the environment is healthy and fully functional.

      * ``Grey`` : Default health for a new environment. The environment is not fully launched
      and health checks have not started or health checks are suspended during an
      ``UpdateEnvironment`` or ``RestartEnvironment`` request.

      Default: ``Grey``

    - **HealthStatus** *(string) --*

      Returns the health status of the application running in your environment. For more
      information, see `Health Colors and Statuses
      <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

    - **Resources** *(dict) --*

      The description of the AWS resources used by this environment.

      - **LoadBalancer** *(dict) --*

        Describes the LoadBalancer.

        - **LoadBalancerName** *(string) --*

          The name of the LoadBalancer.

        - **Domain** *(string) --*

          The domain name of the LoadBalancer.

        - **Listeners** *(list) --*

          A list of Listeners used by the LoadBalancer.

          - *(dict) --*

            Describes the properties of a Listener for the LoadBalancer.

            - **Protocol** *(string) --*

              The protocol that is used by the Listener.

            - **Port** *(integer) --*

              The port that is used by the Listener.

    - **Tier** *(dict) --*

      Describes the current tier of this environment.

      - **Name** *(string) --*

        The name of this environment tier.

        Valid values:

        * For *Web server tier* – ``WebServer``

        * For *Worker tier* – ``Worker``

      - **Type** *(string) --*

        The type of this environment tier.

        Valid values:

        * For *Web server tier* – ``Standard``

        * For *Worker tier* – ``SQS/HTTP``

      - **Version** *(string) --*

        The version of this environment tier. When you don't set a value to it, Elastic
        Beanstalk uses the latest compatible worker tier version.

        .. note::

          This member is deprecated. Any specific version that you set may become out of date.
          We recommend leaving it unspecified.

    - **EnvironmentLinks** *(list) --*

      A list of links to other environments in the same group.

      - *(dict) --*

        A link to another environment, defined in the environment's manifest. Links provide
        connection information in system properties that can be used to connect to another
        environment in the same group. See `Environment Manifest (env.yaml)
        <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__
        for details.

        - **LinkName** *(string) --*

          The name of the link.

        - **EnvironmentName** *(string) --*

          The name of the linked environment (the dependency).

    - **EnvironmentArn** *(string) --*

      The environment's Amazon Resource Name (ARN), which can be used in other API requests
      that require an ARN.
    """


_ClientComposeEnvironmentsResponseTypeDef = TypedDict(
    "_ClientComposeEnvironmentsResponseTypeDef",
    {
        "Environments": List[ClientComposeEnvironmentsResponseEnvironmentsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientComposeEnvironmentsResponseTypeDef(
    _ClientComposeEnvironmentsResponseTypeDef
):
    """
    Type definition for `ClientComposeEnvironments` `Response`

    Result message containing a list of environment descriptions.

    - **Environments** *(list) --*

      Returns an  EnvironmentDescription list.

      - *(dict) --*

        Describes the properties of an environment.

        - **EnvironmentName** *(string) --*

          The name of this environment.

        - **EnvironmentId** *(string) --*

          The ID of this environment.

        - **ApplicationName** *(string) --*

          The name of the application associated with this environment.

        - **VersionLabel** *(string) --*

          The application version deployed in this environment.

        - **SolutionStackName** *(string) --*

          The name of the ``SolutionStack`` deployed with this environment.

        - **PlatformArn** *(string) --*

          The ARN of the platform.

        - **TemplateName** *(string) --*

          The name of the configuration template used to originally launch this environment.

        - **Description** *(string) --*

          Describes this environment.

        - **EndpointURL** *(string) --*

          For load-balanced, autoscaling environments, the URL to the LoadBalancer. For
          single-instance environments, the IP address of the instance.

        - **CNAME** *(string) --*

          The URL to the CNAME for this environment.

        - **DateCreated** *(datetime) --*

          The creation date for this environment.

        - **DateUpdated** *(datetime) --*

          The last modified date for this environment.

        - **Status** *(string) --*

          The current operational status of the environment:

          * ``Launching`` : Environment is in the process of initial deployment.

          * ``Updating`` : Environment is in the process of updating its configuration settings or
          application version.

          * ``Ready`` : Environment is available to have an action performed on it, such as update
          or terminate.

          * ``Terminating`` : Environment is in the shut-down process.

          * ``Terminated`` : Environment is not running.

        - **AbortableOperationInProgress** *(boolean) --*

          Indicates if there is an in-progress environment configuration update or application
          version deployment that you can cancel.

           ``true:`` There is an update in progress.

           ``false:`` There are no updates currently in progress.

        - **Health** *(string) --*

          Describes the health status of the environment. AWS Elastic Beanstalk indicates the
          failure levels for a running environment:

          * ``Red`` : Indicates the environment is not responsive. Occurs when three or more
          consecutive failures occur for an environment.

          * ``Yellow`` : Indicates that something is wrong. Occurs when two consecutive failures
          occur for an environment.

          * ``Green`` : Indicates the environment is healthy and fully functional.

          * ``Grey`` : Default health for a new environment. The environment is not fully launched
          and health checks have not started or health checks are suspended during an
          ``UpdateEnvironment`` or ``RestartEnvironment`` request.

          Default: ``Grey``

        - **HealthStatus** *(string) --*

          Returns the health status of the application running in your environment. For more
          information, see `Health Colors and Statuses
          <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

        - **Resources** *(dict) --*

          The description of the AWS resources used by this environment.

          - **LoadBalancer** *(dict) --*

            Describes the LoadBalancer.

            - **LoadBalancerName** *(string) --*

              The name of the LoadBalancer.

            - **Domain** *(string) --*

              The domain name of the LoadBalancer.

            - **Listeners** *(list) --*

              A list of Listeners used by the LoadBalancer.

              - *(dict) --*

                Describes the properties of a Listener for the LoadBalancer.

                - **Protocol** *(string) --*

                  The protocol that is used by the Listener.

                - **Port** *(integer) --*

                  The port that is used by the Listener.

        - **Tier** *(dict) --*

          Describes the current tier of this environment.

          - **Name** *(string) --*

            The name of this environment tier.

            Valid values:

            * For *Web server tier* – ``WebServer``

            * For *Worker tier* – ``Worker``

          - **Type** *(string) --*

            The type of this environment tier.

            Valid values:

            * For *Web server tier* – ``Standard``

            * For *Worker tier* – ``SQS/HTTP``

          - **Version** *(string) --*

            The version of this environment tier. When you don't set a value to it, Elastic
            Beanstalk uses the latest compatible worker tier version.

            .. note::

              This member is deprecated. Any specific version that you set may become out of date.
              We recommend leaving it unspecified.

        - **EnvironmentLinks** *(list) --*

          A list of links to other environments in the same group.

          - *(dict) --*

            A link to another environment, defined in the environment's manifest. Links provide
            connection information in system properties that can be used to connect to another
            environment in the same group. See `Environment Manifest (env.yaml)
            <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__
            for details.

            - **LinkName** *(string) --*

              The name of the link.

            - **EnvironmentName** *(string) --*

              The name of the linked environment (the dependency).

        - **EnvironmentArn** *(string) --*

          The environment's Amazon Resource Name (ARN), which can be used in other API requests
          that require an ARN.

    - **NextToken** *(string) --*

      In a paginated request, the token that you can pass in a subsequent request to get the next
      response page.
    """


_RequiredClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "_RequiredClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"Enabled": bool},
)
_OptionalClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "_OptionalClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"MaxAgeInDays": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef(
    _RequiredClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    _OptionalClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
):
    """
    Type definition for `ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfig` `MaxAgeRule`

    Specify a max age rule to restrict the length of time that application versions are retained
    for an application.

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Specify ``true`` to apply the rule, or ``false`` to disable it.

    - **MaxAgeInDays** *(integer) --*

      Specify the number of days to retain an application versions.

    - **DeleteSourceFromS3** *(boolean) --*

      Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk
      deletes the application version.
    """


_RequiredClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "_RequiredClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"Enabled": bool},
)
_OptionalClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "_OptionalClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"MaxCount": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef(
    _RequiredClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
    _OptionalClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
):
    """
    Type definition for `ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfig` `MaxCountRule`

    Specify a max count rule to restrict the number of application versions that are retained for
    an application.

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Specify ``true`` to apply the rule, or ``false`` to disable it.

    - **MaxCount** *(integer) --*

      Specify the maximum number of application versions to retain.

    - **DeleteSourceFromS3** *(boolean) --*

      Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk
      deletes the application version.
    """


_ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef = TypedDict(
    "_ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
        "MaxAgeRule": ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef(
    _ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef
):
    """
    Type definition for `ClientCreateApplicationResourceLifecycleConfig` `VersionLifecycleConfig`

    The application version lifecycle configuration.

    - **MaxCountRule** *(dict) --*

      Specify a max count rule to restrict the number of application versions that are retained for
      an application.

      - **Enabled** *(boolean) --* **[REQUIRED]**

        Specify ``true`` to apply the rule, or ``false`` to disable it.

      - **MaxCount** *(integer) --*

        Specify the maximum number of application versions to retain.

      - **DeleteSourceFromS3** *(boolean) --*

        Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk
        deletes the application version.

    - **MaxAgeRule** *(dict) --*

      Specify a max age rule to restrict the length of time that application versions are retained
      for an application.

      - **Enabled** *(boolean) --* **[REQUIRED]**

        Specify ``true`` to apply the rule, or ``false`` to disable it.

      - **MaxAgeInDays** *(integer) --*

        Specify the number of days to retain an application versions.

      - **DeleteSourceFromS3** *(boolean) --*

        Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk
        deletes the application version.
    """


_ClientCreateApplicationResourceLifecycleConfigTypeDef = TypedDict(
    "_ClientCreateApplicationResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": ClientCreateApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResourceLifecycleConfigTypeDef(
    _ClientCreateApplicationResourceLifecycleConfigTypeDef
):
    """
    Type definition for `ClientCreateApplication` `ResourceLifecycleConfig`

    Specify an application resource lifecycle configuration to prevent your application from
    accumulating too many versions.

    - **ServiceRole** *(string) --*

      The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

      The ``ServiceRole`` property is required the first time that you provide a
      ``VersionLifecycleConfig`` for the application in one of the supporting calls
      (``CreateApplication`` or ``UpdateApplicationResourceLifecycle`` ). After you provide it once,
      in either one of the calls, Elastic Beanstalk persists the Service Role with the application,
      and you don't need to specify it again in subsequent ``UpdateApplicationResourceLifecycle``
      calls. You can, however, specify it in subsequent calls to change the Service Role to another
      value.

    - **VersionLifecycleConfig** *(dict) --*

      The application version lifecycle configuration.

      - **MaxCountRule** *(dict) --*

        Specify a max count rule to restrict the number of application versions that are retained for
        an application.

        - **Enabled** *(boolean) --* **[REQUIRED]**

          Specify ``true`` to apply the rule, or ``false`` to disable it.

        - **MaxCount** *(integer) --*

          Specify the maximum number of application versions to retain.

        - **DeleteSourceFromS3** *(boolean) --*

          Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk
          deletes the application version.

      - **MaxAgeRule** *(dict) --*

        Specify a max age rule to restrict the length of time that application versions are retained
        for an application.

        - **Enabled** *(boolean) --* **[REQUIRED]**

          Specify ``true`` to apply the rule, or ``false`` to disable it.

        - **MaxAgeInDays** *(integer) --*

          Specify the number of days to retain an application versions.

        - **DeleteSourceFromS3** *(boolean) --*

          Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk
          deletes the application version.
    """


_ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"Enabled": bool, "MaxAgeInDays": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef(
    _ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfig` `MaxAgeRule`

    Specify a max age rule to restrict the length of time that application versions are
    retained for an application.

    - **Enabled** *(boolean) --*

      Specify ``true`` to apply the rule, or ``false`` to disable it.

    - **MaxAgeInDays** *(integer) --*

      Specify the number of days to retain an application versions.

    - **DeleteSourceFromS3** *(boolean) --*

      Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
      Beanstalk deletes the application version.
    """


_ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"Enabled": bool, "MaxCount": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef(
    _ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfig` `MaxCountRule`

    Specify a max count rule to restrict the number of application versions that are
    retained for an application.

    - **Enabled** *(boolean) --*

      Specify ``true`` to apply the rule, or ``false`` to disable it.

    - **MaxCount** *(integer) --*

      Specify the maximum number of application versions to retain.

    - **DeleteSourceFromS3** *(boolean) --*

      Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
      Beanstalk deletes the application version.
    """


_ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
        "MaxAgeRule": ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef(
    _ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplicationResourceLifecycleConfig` `VersionLifecycleConfig`

    The application version lifecycle configuration.

    - **MaxCountRule** *(dict) --*

      Specify a max count rule to restrict the number of application versions that are
      retained for an application.

      - **Enabled** *(boolean) --*

        Specify ``true`` to apply the rule, or ``false`` to disable it.

      - **MaxCount** *(integer) --*

        Specify the maximum number of application versions to retain.

      - **DeleteSourceFromS3** *(boolean) --*

        Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
        Beanstalk deletes the application version.

    - **MaxAgeRule** *(dict) --*

      Specify a max age rule to restrict the length of time that application versions are
      retained for an application.

      - **Enabled** *(boolean) --*

        Specify ``true`` to apply the rule, or ``false`` to disable it.

      - **MaxAgeInDays** *(integer) --*

        Specify the number of days to retain an application versions.

      - **DeleteSourceFromS3** *(boolean) --*

        Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
        Beanstalk deletes the application version.
    """


_ClientCreateApplicationResponseApplicationResourceLifecycleConfigTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": ClientCreateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationResourceLifecycleConfigTypeDef(
    _ClientCreateApplicationResponseApplicationResourceLifecycleConfigTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponseApplication` `ResourceLifecycleConfig`

    The lifecycle settings for the application.

    - **ServiceRole** *(string) --*

      The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

      The ``ServiceRole`` property is required the first time that you provide a
      ``VersionLifecycleConfig`` for the application in one of the supporting calls
      (``CreateApplication`` or ``UpdateApplicationResourceLifecycle`` ). After you provide it
      once, in either one of the calls, Elastic Beanstalk persists the Service Role with the
      application, and you don't need to specify it again in subsequent
      ``UpdateApplicationResourceLifecycle`` calls. You can, however, specify it in subsequent
      calls to change the Service Role to another value.

    - **VersionLifecycleConfig** *(dict) --*

      The application version lifecycle configuration.

      - **MaxCountRule** *(dict) --*

        Specify a max count rule to restrict the number of application versions that are
        retained for an application.

        - **Enabled** *(boolean) --*

          Specify ``true`` to apply the rule, or ``false`` to disable it.

        - **MaxCount** *(integer) --*

          Specify the maximum number of application versions to retain.

        - **DeleteSourceFromS3** *(boolean) --*

          Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
          Beanstalk deletes the application version.

      - **MaxAgeRule** *(dict) --*

        Specify a max age rule to restrict the length of time that application versions are
        retained for an application.

        - **Enabled** *(boolean) --*

          Specify ``true`` to apply the rule, or ``false`` to disable it.

        - **MaxAgeInDays** *(integer) --*

          Specify the number of days to retain an application versions.

        - **DeleteSourceFromS3** *(boolean) --*

          Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
          Beanstalk deletes the application version.
    """


_ClientCreateApplicationResponseApplicationTypeDef = TypedDict(
    "_ClientCreateApplicationResponseApplicationTypeDef",
    {
        "ApplicationArn": str,
        "ApplicationName": str,
        "Description": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Versions": List[str],
        "ConfigurationTemplates": List[str],
        "ResourceLifecycleConfig": ClientCreateApplicationResponseApplicationResourceLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientCreateApplicationResponseApplicationTypeDef(
    _ClientCreateApplicationResponseApplicationTypeDef
):
    """
    Type definition for `ClientCreateApplicationResponse` `Application`

    The  ApplicationDescription of the application.

    - **ApplicationArn** *(string) --*

      The Amazon Resource Name (ARN) of the application.

    - **ApplicationName** *(string) --*

      The name of the application.

    - **Description** *(string) --*

      User-defined description of the application.

    - **DateCreated** *(datetime) --*

      The date when the application was created.

    - **DateUpdated** *(datetime) --*

      The date when the application was last modified.

    - **Versions** *(list) --*

      The names of the versions for this application.

      - *(string) --*

    - **ConfigurationTemplates** *(list) --*

      The names of the configuration templates associated with this application.

      - *(string) --*

    - **ResourceLifecycleConfig** *(dict) --*

      The lifecycle settings for the application.

      - **ServiceRole** *(string) --*

        The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

        The ``ServiceRole`` property is required the first time that you provide a
        ``VersionLifecycleConfig`` for the application in one of the supporting calls
        (``CreateApplication`` or ``UpdateApplicationResourceLifecycle`` ). After you provide it
        once, in either one of the calls, Elastic Beanstalk persists the Service Role with the
        application, and you don't need to specify it again in subsequent
        ``UpdateApplicationResourceLifecycle`` calls. You can, however, specify it in subsequent
        calls to change the Service Role to another value.

      - **VersionLifecycleConfig** *(dict) --*

        The application version lifecycle configuration.

        - **MaxCountRule** *(dict) --*

          Specify a max count rule to restrict the number of application versions that are
          retained for an application.

          - **Enabled** *(boolean) --*

            Specify ``true`` to apply the rule, or ``false`` to disable it.

          - **MaxCount** *(integer) --*

            Specify the maximum number of application versions to retain.

          - **DeleteSourceFromS3** *(boolean) --*

            Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
            Beanstalk deletes the application version.

        - **MaxAgeRule** *(dict) --*

          Specify a max age rule to restrict the length of time that application versions are
          retained for an application.

          - **Enabled** *(boolean) --*

            Specify ``true`` to apply the rule, or ``false`` to disable it.

          - **MaxAgeInDays** *(integer) --*

            Specify the number of days to retain an application versions.

          - **DeleteSourceFromS3** *(boolean) --*

            Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
            Beanstalk deletes the application version.
    """


_ClientCreateApplicationResponseTypeDef = TypedDict(
    "_ClientCreateApplicationResponseTypeDef",
    {"Application": ClientCreateApplicationResponseApplicationTypeDef},
    total=False,
)


class ClientCreateApplicationResponseTypeDef(_ClientCreateApplicationResponseTypeDef):
    """
    Type definition for `ClientCreateApplication` `Response`

    Result message containing a single description of an application.

    - **Application** *(dict) --*

      The  ApplicationDescription of the application.

      - **ApplicationArn** *(string) --*

        The Amazon Resource Name (ARN) of the application.

      - **ApplicationName** *(string) --*

        The name of the application.

      - **Description** *(string) --*

        User-defined description of the application.

      - **DateCreated** *(datetime) --*

        The date when the application was created.

      - **DateUpdated** *(datetime) --*

        The date when the application was last modified.

      - **Versions** *(list) --*

        The names of the versions for this application.

        - *(string) --*

      - **ConfigurationTemplates** *(list) --*

        The names of the configuration templates associated with this application.

        - *(string) --*

      - **ResourceLifecycleConfig** *(dict) --*

        The lifecycle settings for the application.

        - **ServiceRole** *(string) --*

          The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

          The ``ServiceRole`` property is required the first time that you provide a
          ``VersionLifecycleConfig`` for the application in one of the supporting calls
          (``CreateApplication`` or ``UpdateApplicationResourceLifecycle`` ). After you provide it
          once, in either one of the calls, Elastic Beanstalk persists the Service Role with the
          application, and you don't need to specify it again in subsequent
          ``UpdateApplicationResourceLifecycle`` calls. You can, however, specify it in subsequent
          calls to change the Service Role to another value.

        - **VersionLifecycleConfig** *(dict) --*

          The application version lifecycle configuration.

          - **MaxCountRule** *(dict) --*

            Specify a max count rule to restrict the number of application versions that are
            retained for an application.

            - **Enabled** *(boolean) --*

              Specify ``true`` to apply the rule, or ``false`` to disable it.

            - **MaxCount** *(integer) --*

              Specify the maximum number of application versions to retain.

            - **DeleteSourceFromS3** *(boolean) --*

              Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
              Beanstalk deletes the application version.

          - **MaxAgeRule** *(dict) --*

            Specify a max age rule to restrict the length of time that application versions are
            retained for an application.

            - **Enabled** *(boolean) --*

              Specify ``true`` to apply the rule, or ``false`` to disable it.

            - **MaxAgeInDays** *(integer) --*

              Specify the number of days to retain an application versions.

            - **DeleteSourceFromS3** *(boolean) --*

              Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
              Beanstalk deletes the application version.
    """


_ClientCreateApplicationTagsTypeDef = TypedDict(
    "_ClientCreateApplicationTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateApplicationTagsTypeDef(_ClientCreateApplicationTagsTypeDef):
    """
    Type definition for `ClientCreateApplication` `Tags`

    Describes a tag applied to a resource in an environment.

    - **Key** *(string) --*

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_RequiredClientCreateApplicationVersionBuildConfigurationTypeDef = TypedDict(
    "_RequiredClientCreateApplicationVersionBuildConfigurationTypeDef",
    {"CodeBuildServiceRole": str, "Image": str},
)
_OptionalClientCreateApplicationVersionBuildConfigurationTypeDef = TypedDict(
    "_OptionalClientCreateApplicationVersionBuildConfigurationTypeDef",
    {"ArtifactName": str, "ComputeType": str, "TimeoutInMinutes": int},
    total=False,
)


class ClientCreateApplicationVersionBuildConfigurationTypeDef(
    _RequiredClientCreateApplicationVersionBuildConfigurationTypeDef,
    _OptionalClientCreateApplicationVersionBuildConfigurationTypeDef,
):
    """
    Type definition for `ClientCreateApplicationVersion` `BuildConfiguration`

    Settings for an AWS CodeBuild build.

    - **ArtifactName** *(string) --*

      The name of the artifact of the CodeBuild build. If provided, Elastic Beanstalk stores the
      build artifact in the S3 location *S3-bucket* /resources/*application-name*
      /codebuild/codebuild-*version-label* -*artifact-name* .zip. If not provided, Elastic Beanstalk
      stores the build artifact in the S3 location *S3-bucket* /resources/*application-name*
      /codebuild/codebuild-*version-label* .zip.

    - **CodeBuildServiceRole** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that
      enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

    - **ComputeType** *(string) --*

      Information about the compute resources the build project will use.

      * ``BUILD_GENERAL1_SMALL: Use up to 3 GB memory and 2 vCPUs for builds``

      * ``BUILD_GENERAL1_MEDIUM: Use up to 7 GB memory and 4 vCPUs for builds``

      * ``BUILD_GENERAL1_LARGE: Use up to 15 GB memory and 8 vCPUs for builds``

    - **Image** *(string) --* **[REQUIRED]**

      The ID of the Docker image to use for this build project.

    - **TimeoutInMinutes** *(integer) --*

      How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any
      related build that does not get marked as completed. The default is 60 minutes.
    """


_ClientCreateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef = TypedDict(
    "_ClientCreateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef",
    {"SourceType": str, "SourceRepository": str, "SourceLocation": str},
    total=False,
)


class ClientCreateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef(
    _ClientCreateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef
):
    """
    Type definition for `ClientCreateApplicationVersionResponseApplicationVersion` `SourceBuildInformation`

    If the version's source code was retrieved from AWS CodeCommit, the location of the source
    code for the application version.

    - **SourceType** *(string) --*

      The type of repository.

      * ``Git``

      * ``Zip``

    - **SourceRepository** *(string) --*

      Location where the repository is stored.

      * ``CodeCommit``

      * ``S3``

    - **SourceLocation** *(string) --*

      The location of the source code, as a formatted string, depending on the value of
      ``SourceRepository``

      * For ``CodeCommit`` , the format is the repository name and commit ID, separated by a
      forward slash. For example, ``my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`` .

      * For ``S3`` , the format is the S3 bucket name and object key, separated by a forward
      slash. For example, ``my-s3-bucket/Folders/my-source-file`` .
    """


_ClientCreateApplicationVersionResponseApplicationVersionSourceBundleTypeDef = TypedDict(
    "_ClientCreateApplicationVersionResponseApplicationVersionSourceBundleTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientCreateApplicationVersionResponseApplicationVersionSourceBundleTypeDef(
    _ClientCreateApplicationVersionResponseApplicationVersionSourceBundleTypeDef
):
    """
    Type definition for `ClientCreateApplicationVersionResponseApplicationVersion` `SourceBundle`

    The storage location of the application version's source bundle in Amazon S3.

    - **S3Bucket** *(string) --*

      The Amazon S3 bucket where the data is located.

    - **S3Key** *(string) --*

      The Amazon S3 key where the data is located.
    """


_ClientCreateApplicationVersionResponseApplicationVersionTypeDef = TypedDict(
    "_ClientCreateApplicationVersionResponseApplicationVersionTypeDef",
    {
        "ApplicationVersionArn": str,
        "ApplicationName": str,
        "Description": str,
        "VersionLabel": str,
        "SourceBuildInformation": ClientCreateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef,
        "BuildArn": str,
        "SourceBundle": ClientCreateApplicationVersionResponseApplicationVersionSourceBundleTypeDef,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": str,
    },
    total=False,
)


class ClientCreateApplicationVersionResponseApplicationVersionTypeDef(
    _ClientCreateApplicationVersionResponseApplicationVersionTypeDef
):
    """
    Type definition for `ClientCreateApplicationVersionResponse` `ApplicationVersion`

    The  ApplicationVersionDescription of the application version.

    - **ApplicationVersionArn** *(string) --*

      The Amazon Resource Name (ARN) of the application version.

    - **ApplicationName** *(string) --*

      The name of the application to which the application version belongs.

    - **Description** *(string) --*

      The description of the application version.

    - **VersionLabel** *(string) --*

      A unique identifier for the application version.

    - **SourceBuildInformation** *(dict) --*

      If the version's source code was retrieved from AWS CodeCommit, the location of the source
      code for the application version.

      - **SourceType** *(string) --*

        The type of repository.

        * ``Git``

        * ``Zip``

      - **SourceRepository** *(string) --*

        Location where the repository is stored.

        * ``CodeCommit``

        * ``S3``

      - **SourceLocation** *(string) --*

        The location of the source code, as a formatted string, depending on the value of
        ``SourceRepository``

        * For ``CodeCommit`` , the format is the repository name and commit ID, separated by a
        forward slash. For example, ``my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`` .

        * For ``S3`` , the format is the S3 bucket name and object key, separated by a forward
        slash. For example, ``my-s3-bucket/Folders/my-source-file`` .

    - **BuildArn** *(string) --*

      Reference to the artifact from the AWS CodeBuild build.

    - **SourceBundle** *(dict) --*

      The storage location of the application version's source bundle in Amazon S3.

      - **S3Bucket** *(string) --*

        The Amazon S3 bucket where the data is located.

      - **S3Key** *(string) --*

        The Amazon S3 key where the data is located.

    - **DateCreated** *(datetime) --*

      The creation date of the application version.

    - **DateUpdated** *(datetime) --*

      The last modified date of the application version.

    - **Status** *(string) --*

      The processing status of the application version. Reflects the state of the application
      version during its creation. Many of the values are only applicable if you specified
      ``True`` for the ``Process`` parameter of the ``CreateApplicationVersion`` action. The
      following list describes the possible values.

      * ``Unprocessed`` – Application version wasn't pre-processed or validated. Elastic
      Beanstalk will validate configuration files during deployment of the application version to
      an environment.

      * ``Processing`` – Elastic Beanstalk is currently processing the application version.

      * ``Building`` – Application version is currently undergoing an AWS CodeBuild build.

      * ``Processed`` – Elastic Beanstalk was successfully pre-processed and validated.

      * ``Failed`` – Either the AWS CodeBuild build failed or configuration files didn't pass
      validation. This application version isn't usable.
    """


_ClientCreateApplicationVersionResponseTypeDef = TypedDict(
    "_ClientCreateApplicationVersionResponseTypeDef",
    {
        "ApplicationVersion": ClientCreateApplicationVersionResponseApplicationVersionTypeDef
    },
    total=False,
)


class ClientCreateApplicationVersionResponseTypeDef(
    _ClientCreateApplicationVersionResponseTypeDef
):
    """
    Type definition for `ClientCreateApplicationVersion` `Response`

    Result message wrapping a single description of an application version.

    - **ApplicationVersion** *(dict) --*

      The  ApplicationVersionDescription of the application version.

      - **ApplicationVersionArn** *(string) --*

        The Amazon Resource Name (ARN) of the application version.

      - **ApplicationName** *(string) --*

        The name of the application to which the application version belongs.

      - **Description** *(string) --*

        The description of the application version.

      - **VersionLabel** *(string) --*

        A unique identifier for the application version.

      - **SourceBuildInformation** *(dict) --*

        If the version's source code was retrieved from AWS CodeCommit, the location of the source
        code for the application version.

        - **SourceType** *(string) --*

          The type of repository.

          * ``Git``

          * ``Zip``

        - **SourceRepository** *(string) --*

          Location where the repository is stored.

          * ``CodeCommit``

          * ``S3``

        - **SourceLocation** *(string) --*

          The location of the source code, as a formatted string, depending on the value of
          ``SourceRepository``

          * For ``CodeCommit`` , the format is the repository name and commit ID, separated by a
          forward slash. For example, ``my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`` .

          * For ``S3`` , the format is the S3 bucket name and object key, separated by a forward
          slash. For example, ``my-s3-bucket/Folders/my-source-file`` .

      - **BuildArn** *(string) --*

        Reference to the artifact from the AWS CodeBuild build.

      - **SourceBundle** *(dict) --*

        The storage location of the application version's source bundle in Amazon S3.

        - **S3Bucket** *(string) --*

          The Amazon S3 bucket where the data is located.

        - **S3Key** *(string) --*

          The Amazon S3 key where the data is located.

      - **DateCreated** *(datetime) --*

        The creation date of the application version.

      - **DateUpdated** *(datetime) --*

        The last modified date of the application version.

      - **Status** *(string) --*

        The processing status of the application version. Reflects the state of the application
        version during its creation. Many of the values are only applicable if you specified
        ``True`` for the ``Process`` parameter of the ``CreateApplicationVersion`` action. The
        following list describes the possible values.

        * ``Unprocessed`` – Application version wasn't pre-processed or validated. Elastic
        Beanstalk will validate configuration files during deployment of the application version to
        an environment.

        * ``Processing`` – Elastic Beanstalk is currently processing the application version.

        * ``Building`` – Application version is currently undergoing an AWS CodeBuild build.

        * ``Processed`` – Elastic Beanstalk was successfully pre-processed and validated.

        * ``Failed`` – Either the AWS CodeBuild build failed or configuration files didn't pass
        validation. This application version isn't usable.
    """


_ClientCreateApplicationVersionSourceBuildInformationTypeDef = TypedDict(
    "_ClientCreateApplicationVersionSourceBuildInformationTypeDef",
    {"SourceType": str, "SourceRepository": str, "SourceLocation": str},
)


class ClientCreateApplicationVersionSourceBuildInformationTypeDef(
    _ClientCreateApplicationVersionSourceBuildInformationTypeDef
):
    """
    Type definition for `ClientCreateApplicationVersion` `SourceBuildInformation`

    Specify a commit in an AWS CodeCommit Git repository to use as the source code for the
    application version.

    - **SourceType** *(string) --* **[REQUIRED]**

      The type of repository.

      * ``Git``

      * ``Zip``

    - **SourceRepository** *(string) --* **[REQUIRED]**

      Location where the repository is stored.

      * ``CodeCommit``

      * ``S3``

    - **SourceLocation** *(string) --* **[REQUIRED]**

      The location of the source code, as a formatted string, depending on the value of
      ``SourceRepository``

      * For ``CodeCommit`` , the format is the repository name and commit ID, separated by a forward
      slash. For example, ``my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`` .

      * For ``S3`` , the format is the S3 bucket name and object key, separated by a forward slash.
      For example, ``my-s3-bucket/Folders/my-source-file`` .
    """


_ClientCreateApplicationVersionSourceBundleTypeDef = TypedDict(
    "_ClientCreateApplicationVersionSourceBundleTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientCreateApplicationVersionSourceBundleTypeDef(
    _ClientCreateApplicationVersionSourceBundleTypeDef
):
    """
    Type definition for `ClientCreateApplicationVersion` `SourceBundle`

    The Amazon S3 bucket and key that identify the location of the source bundle for this version.

    .. note::

      The Amazon S3 bucket must be in the same region as the environment.

    Specify a source bundle in S3 or a commit in an AWS CodeCommit repository (with
    ``SourceBuildInformation`` ), but not both. If neither ``SourceBundle`` nor
    ``SourceBuildInformation`` are provided, Elastic Beanstalk uses a sample application.

    - **S3Bucket** *(string) --*

      The Amazon S3 bucket where the data is located.

    - **S3Key** *(string) --*

      The Amazon S3 key where the data is located.
    """


_ClientCreateApplicationVersionTagsTypeDef = TypedDict(
    "_ClientCreateApplicationVersionTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateApplicationVersionTagsTypeDef(
    _ClientCreateApplicationVersionTagsTypeDef
):
    """
    Type definition for `ClientCreateApplicationVersion` `Tags`

    Describes a tag applied to a resource in an environment.

    - **Key** *(string) --*

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientCreateConfigurationTemplateOptionSettingsTypeDef = TypedDict(
    "_ClientCreateConfigurationTemplateOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)


class ClientCreateConfigurationTemplateOptionSettingsTypeDef(
    _ClientCreateConfigurationTemplateOptionSettingsTypeDef
):
    """
    Type definition for `ClientCreateConfigurationTemplate` `OptionSettings`

    A specification identifying an individual configuration option along with its current value.
    For a list of possible option values, go to `Option Values
    <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS
    Elastic Beanstalk Developer Guide* .

    - **ResourceName** *(string) --*

      A unique resource name for a time-based scaling configuration option.

    - **Namespace** *(string) --*

      A unique namespace identifying the option's associated AWS resource.

    - **OptionName** *(string) --*

      The name of the configuration option.

    - **Value** *(string) --*

      The current value for the configuration option.
    """


_ClientCreateConfigurationTemplateResponseOptionSettingsTypeDef = TypedDict(
    "_ClientCreateConfigurationTemplateResponseOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)


class ClientCreateConfigurationTemplateResponseOptionSettingsTypeDef(
    _ClientCreateConfigurationTemplateResponseOptionSettingsTypeDef
):
    """
    Type definition for `ClientCreateConfigurationTemplateResponse` `OptionSettings`

    A specification identifying an individual configuration option along with its current
    value. For a list of possible option values, go to `Option Values
    <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the
    *AWS Elastic Beanstalk Developer Guide* .

    - **ResourceName** *(string) --*

      A unique resource name for a time-based scaling configuration option.

    - **Namespace** *(string) --*

      A unique namespace identifying the option's associated AWS resource.

    - **OptionName** *(string) --*

      The name of the configuration option.

    - **Value** *(string) --*

      The current value for the configuration option.
    """


_ClientCreateConfigurationTemplateResponseTypeDef = TypedDict(
    "_ClientCreateConfigurationTemplateResponseTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "ApplicationName": str,
        "TemplateName": str,
        "Description": str,
        "EnvironmentName": str,
        "DeploymentStatus": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "OptionSettings": List[
            ClientCreateConfigurationTemplateResponseOptionSettingsTypeDef
        ],
    },
    total=False,
)


class ClientCreateConfigurationTemplateResponseTypeDef(
    _ClientCreateConfigurationTemplateResponseTypeDef
):
    """
    Type definition for `ClientCreateConfigurationTemplate` `Response`

    Describes the settings for a configuration set.

    - **SolutionStackName** *(string) --*

      The name of the solution stack this configuration set uses.

    - **PlatformArn** *(string) --*

      The ARN of the platform.

    - **ApplicationName** *(string) --*

      The name of the application associated with this configuration set.

    - **TemplateName** *(string) --*

      If not ``null`` , the name of the configuration template for this configuration set.

    - **Description** *(string) --*

      Describes this configuration set.

    - **EnvironmentName** *(string) --*

      If not ``null`` , the name of the environment for this configuration set.

    - **DeploymentStatus** *(string) --*

      If this configuration set is associated with an environment, the ``DeploymentStatus``
      parameter indicates the deployment status of this configuration set:

      * ``null`` : This configuration is not associated with a running environment.

      * ``pending`` : This is a draft configuration that is not deployed to the associated
      environment but is in the process of deploying.

      * ``deployed`` : This is the configuration that is currently deployed to the associated
      running environment.

      * ``failed`` : This is a draft configuration that failed to successfully deploy.

    - **DateCreated** *(datetime) --*

      The date (in UTC time) when this configuration set was created.

    - **DateUpdated** *(datetime) --*

      The date (in UTC time) when this configuration set was last modified.

    - **OptionSettings** *(list) --*

      A list of the configuration options and their values in this configuration set.

      - *(dict) --*

        A specification identifying an individual configuration option along with its current
        value. For a list of possible option values, go to `Option Values
        <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the
        *AWS Elastic Beanstalk Developer Guide* .

        - **ResourceName** *(string) --*

          A unique resource name for a time-based scaling configuration option.

        - **Namespace** *(string) --*

          A unique namespace identifying the option's associated AWS resource.

        - **OptionName** *(string) --*

          The name of the configuration option.

        - **Value** *(string) --*

          The current value for the configuration option.
    """


_ClientCreateConfigurationTemplateSourceConfigurationTypeDef = TypedDict(
    "_ClientCreateConfigurationTemplateSourceConfigurationTypeDef",
    {"ApplicationName": str, "TemplateName": str},
    total=False,
)


class ClientCreateConfigurationTemplateSourceConfigurationTypeDef(
    _ClientCreateConfigurationTemplateSourceConfigurationTypeDef
):
    """
    Type definition for `ClientCreateConfigurationTemplate` `SourceConfiguration`

    If specified, AWS Elastic Beanstalk uses the configuration values from the specified
    configuration template to create a new configuration.

    Values specified in the ``OptionSettings`` parameter of this call overrides any values obtained
    from the ``SourceConfiguration`` .

    If no configuration template is found, returns an ``InvalidParameterValue`` error.

    Constraint: If both the solution stack name parameter and the source configuration parameters are
    specified, the solution stack of the source configuration template must match the specified
    solution stack name or else AWS Elastic Beanstalk returns an ``InvalidParameterCombination``
    error.

    - **ApplicationName** *(string) --*

      The name of the application associated with the configuration.

    - **TemplateName** *(string) --*

      The name of the configuration template.
    """


_ClientCreateConfigurationTemplateTagsTypeDef = TypedDict(
    "_ClientCreateConfigurationTemplateTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientCreateConfigurationTemplateTagsTypeDef(
    _ClientCreateConfigurationTemplateTagsTypeDef
):
    """
    Type definition for `ClientCreateConfigurationTemplate` `Tags`

    Describes a tag applied to a resource in an environment.

    - **Key** *(string) --*

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientCreateEnvironmentOptionSettingsTypeDef = TypedDict(
    "_ClientCreateEnvironmentOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)


class ClientCreateEnvironmentOptionSettingsTypeDef(
    _ClientCreateEnvironmentOptionSettingsTypeDef
):
    """
    Type definition for `ClientCreateEnvironment` `OptionSettings`

    A specification identifying an individual configuration option along with its current value.
    For a list of possible option values, go to `Option Values
    <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS
    Elastic Beanstalk Developer Guide* .

    - **ResourceName** *(string) --*

      A unique resource name for a time-based scaling configuration option.

    - **Namespace** *(string) --*

      A unique namespace identifying the option's associated AWS resource.

    - **OptionName** *(string) --*

      The name of the configuration option.

    - **Value** *(string) --*

      The current value for the configuration option.
    """


_ClientCreateEnvironmentOptionsToRemoveTypeDef = TypedDict(
    "_ClientCreateEnvironmentOptionsToRemoveTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str},
    total=False,
)


class ClientCreateEnvironmentOptionsToRemoveTypeDef(
    _ClientCreateEnvironmentOptionsToRemoveTypeDef
):
    """
    Type definition for `ClientCreateEnvironment` `OptionsToRemove`

    A specification identifying an individual configuration option.

    - **ResourceName** *(string) --*

      A unique resource name for a time-based scaling configuration option.

    - **Namespace** *(string) --*

      A unique namespace identifying the option's associated AWS resource.

    - **OptionName** *(string) --*

      The name of the configuration option.
    """


_ClientCreateEnvironmentResponseEnvironmentLinksTypeDef = TypedDict(
    "_ClientCreateEnvironmentResponseEnvironmentLinksTypeDef",
    {"LinkName": str, "EnvironmentName": str},
    total=False,
)


class ClientCreateEnvironmentResponseEnvironmentLinksTypeDef(
    _ClientCreateEnvironmentResponseEnvironmentLinksTypeDef
):
    """
    Type definition for `ClientCreateEnvironmentResponse` `EnvironmentLinks`

    A link to another environment, defined in the environment's manifest. Links provide
    connection information in system properties that can be used to connect to another
    environment in the same group. See `Environment Manifest (env.yaml)
    <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__
    for details.

    - **LinkName** *(string) --*

      The name of the link.

    - **EnvironmentName** *(string) --*

      The name of the linked environment (the dependency).
    """


_ClientCreateEnvironmentResponseResourcesLoadBalancerListenersTypeDef = TypedDict(
    "_ClientCreateEnvironmentResponseResourcesLoadBalancerListenersTypeDef",
    {"Protocol": str, "Port": int},
    total=False,
)


class ClientCreateEnvironmentResponseResourcesLoadBalancerListenersTypeDef(
    _ClientCreateEnvironmentResponseResourcesLoadBalancerListenersTypeDef
):
    """
    Type definition for `ClientCreateEnvironmentResponseResourcesLoadBalancer` `Listeners`

    Describes the properties of a Listener for the LoadBalancer.

    - **Protocol** *(string) --*

      The protocol that is used by the Listener.

    - **Port** *(integer) --*

      The port that is used by the Listener.
    """


_ClientCreateEnvironmentResponseResourcesLoadBalancerTypeDef = TypedDict(
    "_ClientCreateEnvironmentResponseResourcesLoadBalancerTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List[
            ClientCreateEnvironmentResponseResourcesLoadBalancerListenersTypeDef
        ],
    },
    total=False,
)


class ClientCreateEnvironmentResponseResourcesLoadBalancerTypeDef(
    _ClientCreateEnvironmentResponseResourcesLoadBalancerTypeDef
):
    """
    Type definition for `ClientCreateEnvironmentResponseResources` `LoadBalancer`

    Describes the LoadBalancer.

    - **LoadBalancerName** *(string) --*

      The name of the LoadBalancer.

    - **Domain** *(string) --*

      The domain name of the LoadBalancer.

    - **Listeners** *(list) --*

      A list of Listeners used by the LoadBalancer.

      - *(dict) --*

        Describes the properties of a Listener for the LoadBalancer.

        - **Protocol** *(string) --*

          The protocol that is used by the Listener.

        - **Port** *(integer) --*

          The port that is used by the Listener.
    """


_ClientCreateEnvironmentResponseResourcesTypeDef = TypedDict(
    "_ClientCreateEnvironmentResponseResourcesTypeDef",
    {"LoadBalancer": ClientCreateEnvironmentResponseResourcesLoadBalancerTypeDef},
    total=False,
)


class ClientCreateEnvironmentResponseResourcesTypeDef(
    _ClientCreateEnvironmentResponseResourcesTypeDef
):
    """
    Type definition for `ClientCreateEnvironmentResponse` `Resources`

    The description of the AWS resources used by this environment.

    - **LoadBalancer** *(dict) --*

      Describes the LoadBalancer.

      - **LoadBalancerName** *(string) --*

        The name of the LoadBalancer.

      - **Domain** *(string) --*

        The domain name of the LoadBalancer.

      - **Listeners** *(list) --*

        A list of Listeners used by the LoadBalancer.

        - *(dict) --*

          Describes the properties of a Listener for the LoadBalancer.

          - **Protocol** *(string) --*

            The protocol that is used by the Listener.

          - **Port** *(integer) --*

            The port that is used by the Listener.
    """


_ClientCreateEnvironmentResponseTierTypeDef = TypedDict(
    "_ClientCreateEnvironmentResponseTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)


class ClientCreateEnvironmentResponseTierTypeDef(
    _ClientCreateEnvironmentResponseTierTypeDef
):
    """
    Type definition for `ClientCreateEnvironmentResponse` `Tier`

    Describes the current tier of this environment.

    - **Name** *(string) --*

      The name of this environment tier.

      Valid values:

      * For *Web server tier* – ``WebServer``

      * For *Worker tier* – ``Worker``

    - **Type** *(string) --*

      The type of this environment tier.

      Valid values:

      * For *Web server tier* – ``Standard``

      * For *Worker tier* – ``SQS/HTTP``

    - **Version** *(string) --*

      The version of this environment tier. When you don't set a value to it, Elastic Beanstalk
      uses the latest compatible worker tier version.

      .. note::

        This member is deprecated. Any specific version that you set may become out of date. We
        recommend leaving it unspecified.
    """


_ClientCreateEnvironmentResponseTypeDef = TypedDict(
    "_ClientCreateEnvironmentResponseTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": str,
        "AbortableOperationInProgress": bool,
        "Health": str,
        "HealthStatus": str,
        "Resources": ClientCreateEnvironmentResponseResourcesTypeDef,
        "Tier": ClientCreateEnvironmentResponseTierTypeDef,
        "EnvironmentLinks": List[
            ClientCreateEnvironmentResponseEnvironmentLinksTypeDef
        ],
        "EnvironmentArn": str,
    },
    total=False,
)


class ClientCreateEnvironmentResponseTypeDef(_ClientCreateEnvironmentResponseTypeDef):
    """
    Type definition for `ClientCreateEnvironment` `Response`

    Describes the properties of an environment.

    - **EnvironmentName** *(string) --*

      The name of this environment.

    - **EnvironmentId** *(string) --*

      The ID of this environment.

    - **ApplicationName** *(string) --*

      The name of the application associated with this environment.

    - **VersionLabel** *(string) --*

      The application version deployed in this environment.

    - **SolutionStackName** *(string) --*

      The name of the ``SolutionStack`` deployed with this environment.

    - **PlatformArn** *(string) --*

      The ARN of the platform.

    - **TemplateName** *(string) --*

      The name of the configuration template used to originally launch this environment.

    - **Description** *(string) --*

      Describes this environment.

    - **EndpointURL** *(string) --*

      For load-balanced, autoscaling environments, the URL to the LoadBalancer. For single-instance
      environments, the IP address of the instance.

    - **CNAME** *(string) --*

      The URL to the CNAME for this environment.

    - **DateCreated** *(datetime) --*

      The creation date for this environment.

    - **DateUpdated** *(datetime) --*

      The last modified date for this environment.

    - **Status** *(string) --*

      The current operational status of the environment:

      * ``Launching`` : Environment is in the process of initial deployment.

      * ``Updating`` : Environment is in the process of updating its configuration settings or
      application version.

      * ``Ready`` : Environment is available to have an action performed on it, such as update or
      terminate.

      * ``Terminating`` : Environment is in the shut-down process.

      * ``Terminated`` : Environment is not running.

    - **AbortableOperationInProgress** *(boolean) --*

      Indicates if there is an in-progress environment configuration update or application version
      deployment that you can cancel.

       ``true:`` There is an update in progress.

       ``false:`` There are no updates currently in progress.

    - **Health** *(string) --*

      Describes the health status of the environment. AWS Elastic Beanstalk indicates the failure
      levels for a running environment:

      * ``Red`` : Indicates the environment is not responsive. Occurs when three or more
      consecutive failures occur for an environment.

      * ``Yellow`` : Indicates that something is wrong. Occurs when two consecutive failures occur
      for an environment.

      * ``Green`` : Indicates the environment is healthy and fully functional.

      * ``Grey`` : Default health for a new environment. The environment is not fully launched and
      health checks have not started or health checks are suspended during an ``UpdateEnvironment``
      or ``RestartEnvironment`` request.

      Default: ``Grey``

    - **HealthStatus** *(string) --*

      Returns the health status of the application running in your environment. For more
      information, see `Health Colors and Statuses
      <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

    - **Resources** *(dict) --*

      The description of the AWS resources used by this environment.

      - **LoadBalancer** *(dict) --*

        Describes the LoadBalancer.

        - **LoadBalancerName** *(string) --*

          The name of the LoadBalancer.

        - **Domain** *(string) --*

          The domain name of the LoadBalancer.

        - **Listeners** *(list) --*

          A list of Listeners used by the LoadBalancer.

          - *(dict) --*

            Describes the properties of a Listener for the LoadBalancer.

            - **Protocol** *(string) --*

              The protocol that is used by the Listener.

            - **Port** *(integer) --*

              The port that is used by the Listener.

    - **Tier** *(dict) --*

      Describes the current tier of this environment.

      - **Name** *(string) --*

        The name of this environment tier.

        Valid values:

        * For *Web server tier* – ``WebServer``

        * For *Worker tier* – ``Worker``

      - **Type** *(string) --*

        The type of this environment tier.

        Valid values:

        * For *Web server tier* – ``Standard``

        * For *Worker tier* – ``SQS/HTTP``

      - **Version** *(string) --*

        The version of this environment tier. When you don't set a value to it, Elastic Beanstalk
        uses the latest compatible worker tier version.

        .. note::

          This member is deprecated. Any specific version that you set may become out of date. We
          recommend leaving it unspecified.

    - **EnvironmentLinks** *(list) --*

      A list of links to other environments in the same group.

      - *(dict) --*

        A link to another environment, defined in the environment's manifest. Links provide
        connection information in system properties that can be used to connect to another
        environment in the same group. See `Environment Manifest (env.yaml)
        <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__
        for details.

        - **LinkName** *(string) --*

          The name of the link.

        - **EnvironmentName** *(string) --*

          The name of the linked environment (the dependency).

    - **EnvironmentArn** *(string) --*

      The environment's Amazon Resource Name (ARN), which can be used in other API requests that
      require an ARN.
    """


_ClientCreateEnvironmentTagsTypeDef = TypedDict(
    "_ClientCreateEnvironmentTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateEnvironmentTagsTypeDef(_ClientCreateEnvironmentTagsTypeDef):
    """
    Type definition for `ClientCreateEnvironment` `Tags`

    Describes a tag applied to a resource in an environment.

    - **Key** *(string) --*

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientCreateEnvironmentTierTypeDef = TypedDict(
    "_ClientCreateEnvironmentTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)


class ClientCreateEnvironmentTierTypeDef(_ClientCreateEnvironmentTierTypeDef):
    """
    Type definition for `ClientCreateEnvironment` `Tier`

    This specifies the tier to use for creating this environment.

    - **Name** *(string) --*

      The name of this environment tier.

      Valid values:

      * For *Web server tier* – ``WebServer``

      * For *Worker tier* – ``Worker``

    - **Type** *(string) --*

      The type of this environment tier.

      Valid values:

      * For *Web server tier* – ``Standard``

      * For *Worker tier* – ``SQS/HTTP``

    - **Version** *(string) --*

      The version of this environment tier. When you don't set a value to it, Elastic Beanstalk uses
      the latest compatible worker tier version.

      .. note::

        This member is deprecated. Any specific version that you set may become out of date. We
        recommend leaving it unspecified.
    """


_ClientCreatePlatformVersionOptionSettingsTypeDef = TypedDict(
    "_ClientCreatePlatformVersionOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)


class ClientCreatePlatformVersionOptionSettingsTypeDef(
    _ClientCreatePlatformVersionOptionSettingsTypeDef
):
    """
    Type definition for `ClientCreatePlatformVersion` `OptionSettings`

    A specification identifying an individual configuration option along with its current value.
    For a list of possible option values, go to `Option Values
    <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS
    Elastic Beanstalk Developer Guide* .

    - **ResourceName** *(string) --*

      A unique resource name for a time-based scaling configuration option.

    - **Namespace** *(string) --*

      A unique namespace identifying the option's associated AWS resource.

    - **OptionName** *(string) --*

      The name of the configuration option.

    - **Value** *(string) --*

      The current value for the configuration option.
    """


_ClientCreatePlatformVersionPlatformDefinitionBundleTypeDef = TypedDict(
    "_ClientCreatePlatformVersionPlatformDefinitionBundleTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientCreatePlatformVersionPlatformDefinitionBundleTypeDef(
    _ClientCreatePlatformVersionPlatformDefinitionBundleTypeDef
):
    """
    Type definition for `ClientCreatePlatformVersion` `PlatformDefinitionBundle`

    The location of the platform definition archive in Amazon S3.

    - **S3Bucket** *(string) --*

      The Amazon S3 bucket where the data is located.

    - **S3Key** *(string) --*

      The Amazon S3 key where the data is located.
    """


_ClientCreatePlatformVersionResponseBuilderTypeDef = TypedDict(
    "_ClientCreatePlatformVersionResponseBuilderTypeDef", {"ARN": str}, total=False
)


class ClientCreatePlatformVersionResponseBuilderTypeDef(
    _ClientCreatePlatformVersionResponseBuilderTypeDef
):
    """
    Type definition for `ClientCreatePlatformVersionResponse` `Builder`

    The builder used to create the custom platform.

    - **ARN** *(string) --*

      The ARN of the builder.
    """


_ClientCreatePlatformVersionResponsePlatformSummaryTypeDef = TypedDict(
    "_ClientCreatePlatformVersionResponsePlatformSummaryTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformStatus": str,
        "PlatformCategory": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
    },
    total=False,
)


class ClientCreatePlatformVersionResponsePlatformSummaryTypeDef(
    _ClientCreatePlatformVersionResponsePlatformSummaryTypeDef
):
    """
    Type definition for `ClientCreatePlatformVersionResponse` `PlatformSummary`

    Detailed information about the new version of the custom platform.

    - **PlatformArn** *(string) --*

      The ARN of the platform.

    - **PlatformOwner** *(string) --*

      The AWS account ID of the person who created the platform.

    - **PlatformStatus** *(string) --*

      The status of the platform. You can create an environment from the platform once it is
      ready.

    - **PlatformCategory** *(string) --*

      The category of platform.

    - **OperatingSystemName** *(string) --*

      The operating system used by the platform.

    - **OperatingSystemVersion** *(string) --*

      The version of the operating system used by the platform.

    - **SupportedTierList** *(list) --*

      The tiers in which the platform runs.

      - *(string) --*

    - **SupportedAddonList** *(list) --*

      The additions associated with the platform.

      - *(string) --*
    """


_ClientCreatePlatformVersionResponseTypeDef = TypedDict(
    "_ClientCreatePlatformVersionResponseTypeDef",
    {
        "PlatformSummary": ClientCreatePlatformVersionResponsePlatformSummaryTypeDef,
        "Builder": ClientCreatePlatformVersionResponseBuilderTypeDef,
    },
    total=False,
)


class ClientCreatePlatformVersionResponseTypeDef(
    _ClientCreatePlatformVersionResponseTypeDef
):
    """
    Type definition for `ClientCreatePlatformVersion` `Response`

    - **PlatformSummary** *(dict) --*

      Detailed information about the new version of the custom platform.

      - **PlatformArn** *(string) --*

        The ARN of the platform.

      - **PlatformOwner** *(string) --*

        The AWS account ID of the person who created the platform.

      - **PlatformStatus** *(string) --*

        The status of the platform. You can create an environment from the platform once it is
        ready.

      - **PlatformCategory** *(string) --*

        The category of platform.

      - **OperatingSystemName** *(string) --*

        The operating system used by the platform.

      - **OperatingSystemVersion** *(string) --*

        The version of the operating system used by the platform.

      - **SupportedTierList** *(list) --*

        The tiers in which the platform runs.

        - *(string) --*

      - **SupportedAddonList** *(list) --*

        The additions associated with the platform.

        - *(string) --*

    - **Builder** *(dict) --*

      The builder used to create the custom platform.

      - **ARN** *(string) --*

        The ARN of the builder.
    """


_ClientCreatePlatformVersionTagsTypeDef = TypedDict(
    "_ClientCreatePlatformVersionTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreatePlatformVersionTagsTypeDef(_ClientCreatePlatformVersionTagsTypeDef):
    """
    Type definition for `ClientCreatePlatformVersion` `Tags`

    Describes a tag applied to a resource in an environment.

    - **Key** *(string) --*

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientCreateStorageLocationResponseTypeDef = TypedDict(
    "_ClientCreateStorageLocationResponseTypeDef", {"S3Bucket": str}, total=False
)


class ClientCreateStorageLocationResponseTypeDef(
    _ClientCreateStorageLocationResponseTypeDef
):
    """
    Type definition for `ClientCreateStorageLocation` `Response`

    Results of a  CreateStorageLocationResult call.

    - **S3Bucket** *(string) --*

      The name of the Amazon S3 bucket created.
    """


_ClientDeletePlatformVersionResponsePlatformSummaryTypeDef = TypedDict(
    "_ClientDeletePlatformVersionResponsePlatformSummaryTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformStatus": str,
        "PlatformCategory": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
    },
    total=False,
)


class ClientDeletePlatformVersionResponsePlatformSummaryTypeDef(
    _ClientDeletePlatformVersionResponsePlatformSummaryTypeDef
):
    """
    Type definition for `ClientDeletePlatformVersionResponse` `PlatformSummary`

    Detailed information about the version of the custom platform.

    - **PlatformArn** *(string) --*

      The ARN of the platform.

    - **PlatformOwner** *(string) --*

      The AWS account ID of the person who created the platform.

    - **PlatformStatus** *(string) --*

      The status of the platform. You can create an environment from the platform once it is
      ready.

    - **PlatformCategory** *(string) --*

      The category of platform.

    - **OperatingSystemName** *(string) --*

      The operating system used by the platform.

    - **OperatingSystemVersion** *(string) --*

      The version of the operating system used by the platform.

    - **SupportedTierList** *(list) --*

      The tiers in which the platform runs.

      - *(string) --*

    - **SupportedAddonList** *(list) --*

      The additions associated with the platform.

      - *(string) --*
    """


_ClientDeletePlatformVersionResponseTypeDef = TypedDict(
    "_ClientDeletePlatformVersionResponseTypeDef",
    {"PlatformSummary": ClientDeletePlatformVersionResponsePlatformSummaryTypeDef},
    total=False,
)


class ClientDeletePlatformVersionResponseTypeDef(
    _ClientDeletePlatformVersionResponseTypeDef
):
    """
    Type definition for `ClientDeletePlatformVersion` `Response`

    - **PlatformSummary** *(dict) --*

      Detailed information about the version of the custom platform.

      - **PlatformArn** *(string) --*

        The ARN of the platform.

      - **PlatformOwner** *(string) --*

        The AWS account ID of the person who created the platform.

      - **PlatformStatus** *(string) --*

        The status of the platform. You can create an environment from the platform once it is
        ready.

      - **PlatformCategory** *(string) --*

        The category of platform.

      - **OperatingSystemName** *(string) --*

        The operating system used by the platform.

      - **OperatingSystemVersion** *(string) --*

        The version of the operating system used by the platform.

      - **SupportedTierList** *(list) --*

        The tiers in which the platform runs.

        - *(string) --*

      - **SupportedAddonList** *(list) --*

        The additions associated with the platform.

        - *(string) --*
    """


_ClientDescribeAccountAttributesResponseResourceQuotasApplicationQuotaTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseResourceQuotasApplicationQuotaTypeDef",
    {"Maximum": int},
    total=False,
)


class ClientDescribeAccountAttributesResponseResourceQuotasApplicationQuotaTypeDef(
    _ClientDescribeAccountAttributesResponseResourceQuotasApplicationQuotaTypeDef
):
    """
    Type definition for `ClientDescribeAccountAttributesResponseResourceQuotas` `ApplicationQuota`

    The quota for applications in the AWS account.

    - **Maximum** *(integer) --*

      The maximum number of instances of this Elastic Beanstalk resource type that an AWS
      account can use.
    """


_ClientDescribeAccountAttributesResponseResourceQuotasApplicationVersionQuotaTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseResourceQuotasApplicationVersionQuotaTypeDef",
    {"Maximum": int},
    total=False,
)


class ClientDescribeAccountAttributesResponseResourceQuotasApplicationVersionQuotaTypeDef(
    _ClientDescribeAccountAttributesResponseResourceQuotasApplicationVersionQuotaTypeDef
):
    """
    Type definition for `ClientDescribeAccountAttributesResponseResourceQuotas` `ApplicationVersionQuota`

    The quota for application versions in the AWS account.

    - **Maximum** *(integer) --*

      The maximum number of instances of this Elastic Beanstalk resource type that an AWS
      account can use.
    """


_ClientDescribeAccountAttributesResponseResourceQuotasConfigurationTemplateQuotaTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseResourceQuotasConfigurationTemplateQuotaTypeDef",
    {"Maximum": int},
    total=False,
)


class ClientDescribeAccountAttributesResponseResourceQuotasConfigurationTemplateQuotaTypeDef(
    _ClientDescribeAccountAttributesResponseResourceQuotasConfigurationTemplateQuotaTypeDef
):
    """
    Type definition for `ClientDescribeAccountAttributesResponseResourceQuotas` `ConfigurationTemplateQuota`

    The quota for configuration templates in the AWS account.

    - **Maximum** *(integer) --*

      The maximum number of instances of this Elastic Beanstalk resource type that an AWS
      account can use.
    """


_ClientDescribeAccountAttributesResponseResourceQuotasCustomPlatformQuotaTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseResourceQuotasCustomPlatformQuotaTypeDef",
    {"Maximum": int},
    total=False,
)


class ClientDescribeAccountAttributesResponseResourceQuotasCustomPlatformQuotaTypeDef(
    _ClientDescribeAccountAttributesResponseResourceQuotasCustomPlatformQuotaTypeDef
):
    """
    Type definition for `ClientDescribeAccountAttributesResponseResourceQuotas` `CustomPlatformQuota`

    The quota for custom platforms in the AWS account.

    - **Maximum** *(integer) --*

      The maximum number of instances of this Elastic Beanstalk resource type that an AWS
      account can use.
    """


_ClientDescribeAccountAttributesResponseResourceQuotasEnvironmentQuotaTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseResourceQuotasEnvironmentQuotaTypeDef",
    {"Maximum": int},
    total=False,
)


class ClientDescribeAccountAttributesResponseResourceQuotasEnvironmentQuotaTypeDef(
    _ClientDescribeAccountAttributesResponseResourceQuotasEnvironmentQuotaTypeDef
):
    """
    Type definition for `ClientDescribeAccountAttributesResponseResourceQuotas` `EnvironmentQuota`

    The quota for environments in the AWS account.

    - **Maximum** *(integer) --*

      The maximum number of instances of this Elastic Beanstalk resource type that an AWS
      account can use.
    """


_ClientDescribeAccountAttributesResponseResourceQuotasTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseResourceQuotasTypeDef",
    {
        "ApplicationQuota": ClientDescribeAccountAttributesResponseResourceQuotasApplicationQuotaTypeDef,
        "ApplicationVersionQuota": ClientDescribeAccountAttributesResponseResourceQuotasApplicationVersionQuotaTypeDef,
        "EnvironmentQuota": ClientDescribeAccountAttributesResponseResourceQuotasEnvironmentQuotaTypeDef,
        "ConfigurationTemplateQuota": ClientDescribeAccountAttributesResponseResourceQuotasConfigurationTemplateQuotaTypeDef,
        "CustomPlatformQuota": ClientDescribeAccountAttributesResponseResourceQuotasCustomPlatformQuotaTypeDef,
    },
    total=False,
)


class ClientDescribeAccountAttributesResponseResourceQuotasTypeDef(
    _ClientDescribeAccountAttributesResponseResourceQuotasTypeDef
):
    """
    Type definition for `ClientDescribeAccountAttributesResponse` `ResourceQuotas`

    The Elastic Beanstalk resource quotas associated with the calling AWS account.

    - **ApplicationQuota** *(dict) --*

      The quota for applications in the AWS account.

      - **Maximum** *(integer) --*

        The maximum number of instances of this Elastic Beanstalk resource type that an AWS
        account can use.

    - **ApplicationVersionQuota** *(dict) --*

      The quota for application versions in the AWS account.

      - **Maximum** *(integer) --*

        The maximum number of instances of this Elastic Beanstalk resource type that an AWS
        account can use.

    - **EnvironmentQuota** *(dict) --*

      The quota for environments in the AWS account.

      - **Maximum** *(integer) --*

        The maximum number of instances of this Elastic Beanstalk resource type that an AWS
        account can use.

    - **ConfigurationTemplateQuota** *(dict) --*

      The quota for configuration templates in the AWS account.

      - **Maximum** *(integer) --*

        The maximum number of instances of this Elastic Beanstalk resource type that an AWS
        account can use.

    - **CustomPlatformQuota** *(dict) --*

      The quota for custom platforms in the AWS account.

      - **Maximum** *(integer) --*

        The maximum number of instances of this Elastic Beanstalk resource type that an AWS
        account can use.
    """


_ClientDescribeAccountAttributesResponseTypeDef = TypedDict(
    "_ClientDescribeAccountAttributesResponseTypeDef",
    {"ResourceQuotas": ClientDescribeAccountAttributesResponseResourceQuotasTypeDef},
    total=False,
)


class ClientDescribeAccountAttributesResponseTypeDef(
    _ClientDescribeAccountAttributesResponseTypeDef
):
    """
    Type definition for `ClientDescribeAccountAttributes` `Response`

    - **ResourceQuotas** *(dict) --*

      The Elastic Beanstalk resource quotas associated with the calling AWS account.

      - **ApplicationQuota** *(dict) --*

        The quota for applications in the AWS account.

        - **Maximum** *(integer) --*

          The maximum number of instances of this Elastic Beanstalk resource type that an AWS
          account can use.

      - **ApplicationVersionQuota** *(dict) --*

        The quota for application versions in the AWS account.

        - **Maximum** *(integer) --*

          The maximum number of instances of this Elastic Beanstalk resource type that an AWS
          account can use.

      - **EnvironmentQuota** *(dict) --*

        The quota for environments in the AWS account.

        - **Maximum** *(integer) --*

          The maximum number of instances of this Elastic Beanstalk resource type that an AWS
          account can use.

      - **ConfigurationTemplateQuota** *(dict) --*

        The quota for configuration templates in the AWS account.

        - **Maximum** *(integer) --*

          The maximum number of instances of this Elastic Beanstalk resource type that an AWS
          account can use.

      - **CustomPlatformQuota** *(dict) --*

        The quota for custom platforms in the AWS account.

        - **Maximum** *(integer) --*

          The maximum number of instances of this Elastic Beanstalk resource type that an AWS
          account can use.
    """


_ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBuildInformationTypeDef = TypedDict(
    "_ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBuildInformationTypeDef",
    {"SourceType": str, "SourceRepository": str, "SourceLocation": str},
    total=False,
)


class ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBuildInformationTypeDef(
    _ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBuildInformationTypeDef
):
    """
    Type definition for `ClientDescribeApplicationVersionsResponseApplicationVersions` `SourceBuildInformation`

    If the version's source code was retrieved from AWS CodeCommit, the location of the
    source code for the application version.

    - **SourceType** *(string) --*

      The type of repository.

      * ``Git``

      * ``Zip``

    - **SourceRepository** *(string) --*

      Location where the repository is stored.

      * ``CodeCommit``

      * ``S3``

    - **SourceLocation** *(string) --*

      The location of the source code, as a formatted string, depending on the value of
      ``SourceRepository``

      * For ``CodeCommit`` , the format is the repository name and commit ID, separated by a
      forward slash. For example, ``my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`` .

      * For ``S3`` , the format is the S3 bucket name and object key, separated by a forward
      slash. For example, ``my-s3-bucket/Folders/my-source-file`` .
    """


_ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBundleTypeDef = TypedDict(
    "_ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBundleTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBundleTypeDef(
    _ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBundleTypeDef
):
    """
    Type definition for `ClientDescribeApplicationVersionsResponseApplicationVersions` `SourceBundle`

    The storage location of the application version's source bundle in Amazon S3.

    - **S3Bucket** *(string) --*

      The Amazon S3 bucket where the data is located.

    - **S3Key** *(string) --*

      The Amazon S3 key where the data is located.
    """


_ClientDescribeApplicationVersionsResponseApplicationVersionsTypeDef = TypedDict(
    "_ClientDescribeApplicationVersionsResponseApplicationVersionsTypeDef",
    {
        "ApplicationVersionArn": str,
        "ApplicationName": str,
        "Description": str,
        "VersionLabel": str,
        "SourceBuildInformation": ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBuildInformationTypeDef,
        "BuildArn": str,
        "SourceBundle": ClientDescribeApplicationVersionsResponseApplicationVersionsSourceBundleTypeDef,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": str,
    },
    total=False,
)


class ClientDescribeApplicationVersionsResponseApplicationVersionsTypeDef(
    _ClientDescribeApplicationVersionsResponseApplicationVersionsTypeDef
):
    """
    Type definition for `ClientDescribeApplicationVersionsResponse` `ApplicationVersions`

    Describes the properties of an application version.

    - **ApplicationVersionArn** *(string) --*

      The Amazon Resource Name (ARN) of the application version.

    - **ApplicationName** *(string) --*

      The name of the application to which the application version belongs.

    - **Description** *(string) --*

      The description of the application version.

    - **VersionLabel** *(string) --*

      A unique identifier for the application version.

    - **SourceBuildInformation** *(dict) --*

      If the version's source code was retrieved from AWS CodeCommit, the location of the
      source code for the application version.

      - **SourceType** *(string) --*

        The type of repository.

        * ``Git``

        * ``Zip``

      - **SourceRepository** *(string) --*

        Location where the repository is stored.

        * ``CodeCommit``

        * ``S3``

      - **SourceLocation** *(string) --*

        The location of the source code, as a formatted string, depending on the value of
        ``SourceRepository``

        * For ``CodeCommit`` , the format is the repository name and commit ID, separated by a
        forward slash. For example, ``my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`` .

        * For ``S3`` , the format is the S3 bucket name and object key, separated by a forward
        slash. For example, ``my-s3-bucket/Folders/my-source-file`` .

    - **BuildArn** *(string) --*

      Reference to the artifact from the AWS CodeBuild build.

    - **SourceBundle** *(dict) --*

      The storage location of the application version's source bundle in Amazon S3.

      - **S3Bucket** *(string) --*

        The Amazon S3 bucket where the data is located.

      - **S3Key** *(string) --*

        The Amazon S3 key where the data is located.

    - **DateCreated** *(datetime) --*

      The creation date of the application version.

    - **DateUpdated** *(datetime) --*

      The last modified date of the application version.

    - **Status** *(string) --*

      The processing status of the application version. Reflects the state of the application
      version during its creation. Many of the values are only applicable if you specified
      ``True`` for the ``Process`` parameter of the ``CreateApplicationVersion`` action. The
      following list describes the possible values.

      * ``Unprocessed`` – Application version wasn't pre-processed or validated. Elastic
      Beanstalk will validate configuration files during deployment of the application version
      to an environment.

      * ``Processing`` – Elastic Beanstalk is currently processing the application version.

      * ``Building`` – Application version is currently undergoing an AWS CodeBuild build.

      * ``Processed`` – Elastic Beanstalk was successfully pre-processed and validated.

      * ``Failed`` – Either the AWS CodeBuild build failed or configuration files didn't pass
      validation. This application version isn't usable.
    """


_ClientDescribeApplicationVersionsResponseTypeDef = TypedDict(
    "_ClientDescribeApplicationVersionsResponseTypeDef",
    {
        "ApplicationVersions": List[
            ClientDescribeApplicationVersionsResponseApplicationVersionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeApplicationVersionsResponseTypeDef(
    _ClientDescribeApplicationVersionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeApplicationVersions` `Response`

    Result message wrapping a list of application version descriptions.

    - **ApplicationVersions** *(list) --*

      List of ``ApplicationVersionDescription`` objects sorted in order of creation.

      - *(dict) --*

        Describes the properties of an application version.

        - **ApplicationVersionArn** *(string) --*

          The Amazon Resource Name (ARN) of the application version.

        - **ApplicationName** *(string) --*

          The name of the application to which the application version belongs.

        - **Description** *(string) --*

          The description of the application version.

        - **VersionLabel** *(string) --*

          A unique identifier for the application version.

        - **SourceBuildInformation** *(dict) --*

          If the version's source code was retrieved from AWS CodeCommit, the location of the
          source code for the application version.

          - **SourceType** *(string) --*

            The type of repository.

            * ``Git``

            * ``Zip``

          - **SourceRepository** *(string) --*

            Location where the repository is stored.

            * ``CodeCommit``

            * ``S3``

          - **SourceLocation** *(string) --*

            The location of the source code, as a formatted string, depending on the value of
            ``SourceRepository``

            * For ``CodeCommit`` , the format is the repository name and commit ID, separated by a
            forward slash. For example, ``my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`` .

            * For ``S3`` , the format is the S3 bucket name and object key, separated by a forward
            slash. For example, ``my-s3-bucket/Folders/my-source-file`` .

        - **BuildArn** *(string) --*

          Reference to the artifact from the AWS CodeBuild build.

        - **SourceBundle** *(dict) --*

          The storage location of the application version's source bundle in Amazon S3.

          - **S3Bucket** *(string) --*

            The Amazon S3 bucket where the data is located.

          - **S3Key** *(string) --*

            The Amazon S3 key where the data is located.

        - **DateCreated** *(datetime) --*

          The creation date of the application version.

        - **DateUpdated** *(datetime) --*

          The last modified date of the application version.

        - **Status** *(string) --*

          The processing status of the application version. Reflects the state of the application
          version during its creation. Many of the values are only applicable if you specified
          ``True`` for the ``Process`` parameter of the ``CreateApplicationVersion`` action. The
          following list describes the possible values.

          * ``Unprocessed`` – Application version wasn't pre-processed or validated. Elastic
          Beanstalk will validate configuration files during deployment of the application version
          to an environment.

          * ``Processing`` – Elastic Beanstalk is currently processing the application version.

          * ``Building`` – Application version is currently undergoing an AWS CodeBuild build.

          * ``Processed`` – Elastic Beanstalk was successfully pre-processed and validated.

          * ``Failed`` – Either the AWS CodeBuild build failed or configuration files didn't pass
          validation. This application version isn't usable.

    - **NextToken** *(string) --*

      In a paginated request, the token that you can pass in a subsequent request to get the next
      response page.
    """


_ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "_ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"Enabled": bool, "MaxAgeInDays": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef(
    _ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef
):
    """
    Type definition for `ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfig` `MaxAgeRule`

    Specify a max age rule to restrict the length of time that application versions are
    retained for an application.

    - **Enabled** *(boolean) --*

      Specify ``true`` to apply the rule, or ``false`` to disable it.

    - **MaxAgeInDays** *(integer) --*

      Specify the number of days to retain an application versions.

    - **DeleteSourceFromS3** *(boolean) --*

      Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
      Beanstalk deletes the application version.
    """


_ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "_ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"Enabled": bool, "MaxCount": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef(
    _ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef
):
    """
    Type definition for `ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfig` `MaxCountRule`

    Specify a max count rule to restrict the number of application versions that are
    retained for an application.

    - **Enabled** *(boolean) --*

      Specify ``true`` to apply the rule, or ``false`` to disable it.

    - **MaxCount** *(integer) --*

      Specify the maximum number of application versions to retain.

    - **DeleteSourceFromS3** *(boolean) --*

      Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
      Beanstalk deletes the application version.
    """


_ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigTypeDef = TypedDict(
    "_ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
        "MaxAgeRule": ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigTypeDef(
    _ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigTypeDef
):
    """
    Type definition for `ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfig` `VersionLifecycleConfig`

    The application version lifecycle configuration.

    - **MaxCountRule** *(dict) --*

      Specify a max count rule to restrict the number of application versions that are
      retained for an application.

      - **Enabled** *(boolean) --*

        Specify ``true`` to apply the rule, or ``false`` to disable it.

      - **MaxCount** *(integer) --*

        Specify the maximum number of application versions to retain.

      - **DeleteSourceFromS3** *(boolean) --*

        Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
        Beanstalk deletes the application version.

    - **MaxAgeRule** *(dict) --*

      Specify a max age rule to restrict the length of time that application versions are
      retained for an application.

      - **Enabled** *(boolean) --*

        Specify ``true`` to apply the rule, or ``false`` to disable it.

      - **MaxAgeInDays** *(integer) --*

        Specify the number of days to retain an application versions.

      - **DeleteSourceFromS3** *(boolean) --*

        Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
        Beanstalk deletes the application version.
    """


_ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigTypeDef = TypedDict(
    "_ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigVersionLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigTypeDef(
    _ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigTypeDef
):
    """
    Type definition for `ClientDescribeApplicationsResponseApplications` `ResourceLifecycleConfig`

    The lifecycle settings for the application.

    - **ServiceRole** *(string) --*

      The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

      The ``ServiceRole`` property is required the first time that you provide a
      ``VersionLifecycleConfig`` for the application in one of the supporting calls
      (``CreateApplication`` or ``UpdateApplicationResourceLifecycle`` ). After you provide
      it once, in either one of the calls, Elastic Beanstalk persists the Service Role with
      the application, and you don't need to specify it again in subsequent
      ``UpdateApplicationResourceLifecycle`` calls. You can, however, specify it in
      subsequent calls to change the Service Role to another value.

    - **VersionLifecycleConfig** *(dict) --*

      The application version lifecycle configuration.

      - **MaxCountRule** *(dict) --*

        Specify a max count rule to restrict the number of application versions that are
        retained for an application.

        - **Enabled** *(boolean) --*

          Specify ``true`` to apply the rule, or ``false`` to disable it.

        - **MaxCount** *(integer) --*

          Specify the maximum number of application versions to retain.

        - **DeleteSourceFromS3** *(boolean) --*

          Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
          Beanstalk deletes the application version.

      - **MaxAgeRule** *(dict) --*

        Specify a max age rule to restrict the length of time that application versions are
        retained for an application.

        - **Enabled** *(boolean) --*

          Specify ``true`` to apply the rule, or ``false`` to disable it.

        - **MaxAgeInDays** *(integer) --*

          Specify the number of days to retain an application versions.

        - **DeleteSourceFromS3** *(boolean) --*

          Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
          Beanstalk deletes the application version.
    """


_ClientDescribeApplicationsResponseApplicationsTypeDef = TypedDict(
    "_ClientDescribeApplicationsResponseApplicationsTypeDef",
    {
        "ApplicationArn": str,
        "ApplicationName": str,
        "Description": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Versions": List[str],
        "ConfigurationTemplates": List[str],
        "ResourceLifecycleConfig": ClientDescribeApplicationsResponseApplicationsResourceLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientDescribeApplicationsResponseApplicationsTypeDef(
    _ClientDescribeApplicationsResponseApplicationsTypeDef
):
    """
    Type definition for `ClientDescribeApplicationsResponse` `Applications`

    Describes the properties of an application.

    - **ApplicationArn** *(string) --*

      The Amazon Resource Name (ARN) of the application.

    - **ApplicationName** *(string) --*

      The name of the application.

    - **Description** *(string) --*

      User-defined description of the application.

    - **DateCreated** *(datetime) --*

      The date when the application was created.

    - **DateUpdated** *(datetime) --*

      The date when the application was last modified.

    - **Versions** *(list) --*

      The names of the versions for this application.

      - *(string) --*

    - **ConfigurationTemplates** *(list) --*

      The names of the configuration templates associated with this application.

      - *(string) --*

    - **ResourceLifecycleConfig** *(dict) --*

      The lifecycle settings for the application.

      - **ServiceRole** *(string) --*

        The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

        The ``ServiceRole`` property is required the first time that you provide a
        ``VersionLifecycleConfig`` for the application in one of the supporting calls
        (``CreateApplication`` or ``UpdateApplicationResourceLifecycle`` ). After you provide
        it once, in either one of the calls, Elastic Beanstalk persists the Service Role with
        the application, and you don't need to specify it again in subsequent
        ``UpdateApplicationResourceLifecycle`` calls. You can, however, specify it in
        subsequent calls to change the Service Role to another value.

      - **VersionLifecycleConfig** *(dict) --*

        The application version lifecycle configuration.

        - **MaxCountRule** *(dict) --*

          Specify a max count rule to restrict the number of application versions that are
          retained for an application.

          - **Enabled** *(boolean) --*

            Specify ``true`` to apply the rule, or ``false`` to disable it.

          - **MaxCount** *(integer) --*

            Specify the maximum number of application versions to retain.

          - **DeleteSourceFromS3** *(boolean) --*

            Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
            Beanstalk deletes the application version.

        - **MaxAgeRule** *(dict) --*

          Specify a max age rule to restrict the length of time that application versions are
          retained for an application.

          - **Enabled** *(boolean) --*

            Specify ``true`` to apply the rule, or ``false`` to disable it.

          - **MaxAgeInDays** *(integer) --*

            Specify the number of days to retain an application versions.

          - **DeleteSourceFromS3** *(boolean) --*

            Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
            Beanstalk deletes the application version.
    """


_ClientDescribeApplicationsResponseTypeDef = TypedDict(
    "_ClientDescribeApplicationsResponseTypeDef",
    {"Applications": List[ClientDescribeApplicationsResponseApplicationsTypeDef]},
    total=False,
)


class ClientDescribeApplicationsResponseTypeDef(
    _ClientDescribeApplicationsResponseTypeDef
):
    """
    Type definition for `ClientDescribeApplications` `Response`

    Result message containing a list of application descriptions.

    - **Applications** *(list) --*

      This parameter contains a list of  ApplicationDescription .

      - *(dict) --*

        Describes the properties of an application.

        - **ApplicationArn** *(string) --*

          The Amazon Resource Name (ARN) of the application.

        - **ApplicationName** *(string) --*

          The name of the application.

        - **Description** *(string) --*

          User-defined description of the application.

        - **DateCreated** *(datetime) --*

          The date when the application was created.

        - **DateUpdated** *(datetime) --*

          The date when the application was last modified.

        - **Versions** *(list) --*

          The names of the versions for this application.

          - *(string) --*

        - **ConfigurationTemplates** *(list) --*

          The names of the configuration templates associated with this application.

          - *(string) --*

        - **ResourceLifecycleConfig** *(dict) --*

          The lifecycle settings for the application.

          - **ServiceRole** *(string) --*

            The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

            The ``ServiceRole`` property is required the first time that you provide a
            ``VersionLifecycleConfig`` for the application in one of the supporting calls
            (``CreateApplication`` or ``UpdateApplicationResourceLifecycle`` ). After you provide
            it once, in either one of the calls, Elastic Beanstalk persists the Service Role with
            the application, and you don't need to specify it again in subsequent
            ``UpdateApplicationResourceLifecycle`` calls. You can, however, specify it in
            subsequent calls to change the Service Role to another value.

          - **VersionLifecycleConfig** *(dict) --*

            The application version lifecycle configuration.

            - **MaxCountRule** *(dict) --*

              Specify a max count rule to restrict the number of application versions that are
              retained for an application.

              - **Enabled** *(boolean) --*

                Specify ``true`` to apply the rule, or ``false`` to disable it.

              - **MaxCount** *(integer) --*

                Specify the maximum number of application versions to retain.

              - **DeleteSourceFromS3** *(boolean) --*

                Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
                Beanstalk deletes the application version.

            - **MaxAgeRule** *(dict) --*

              Specify a max age rule to restrict the length of time that application versions are
              retained for an application.

              - **Enabled** *(boolean) --*

                Specify ``true`` to apply the rule, or ``false`` to disable it.

              - **MaxAgeInDays** *(integer) --*

                Specify the number of days to retain an application versions.

              - **DeleteSourceFromS3** *(boolean) --*

                Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
                Beanstalk deletes the application version.
    """


_ClientDescribeConfigurationOptionsOptionsTypeDef = TypedDict(
    "_ClientDescribeConfigurationOptionsOptionsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str},
    total=False,
)


class ClientDescribeConfigurationOptionsOptionsTypeDef(
    _ClientDescribeConfigurationOptionsOptionsTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationOptions` `Options`

    A specification identifying an individual configuration option.

    - **ResourceName** *(string) --*

      A unique resource name for a time-based scaling configuration option.

    - **Namespace** *(string) --*

      A unique namespace identifying the option's associated AWS resource.

    - **OptionName** *(string) --*

      The name of the configuration option.
    """


_ClientDescribeConfigurationOptionsResponseOptionsRegexTypeDef = TypedDict(
    "_ClientDescribeConfigurationOptionsResponseOptionsRegexTypeDef",
    {"Pattern": str, "Label": str},
    total=False,
)


class ClientDescribeConfigurationOptionsResponseOptionsRegexTypeDef(
    _ClientDescribeConfigurationOptionsResponseOptionsRegexTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationOptionsResponseOptions` `Regex`

    If specified, the configuration option must be a string value that satisfies this regular
    expression.

    - **Pattern** *(string) --*

      The regular expression pattern that a string configuration option value with this
      restriction must match.

    - **Label** *(string) --*

      A unique name representing this regular expression.
    """


_ClientDescribeConfigurationOptionsResponseOptionsTypeDef = TypedDict(
    "_ClientDescribeConfigurationOptionsResponseOptionsTypeDef",
    {
        "Namespace": str,
        "Name": str,
        "DefaultValue": str,
        "ChangeSeverity": str,
        "UserDefined": bool,
        "ValueType": str,
        "ValueOptions": List[str],
        "MinValue": int,
        "MaxValue": int,
        "MaxLength": int,
        "Regex": ClientDescribeConfigurationOptionsResponseOptionsRegexTypeDef,
    },
    total=False,
)


class ClientDescribeConfigurationOptionsResponseOptionsTypeDef(
    _ClientDescribeConfigurationOptionsResponseOptionsTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationOptionsResponse` `Options`

    Describes the possible values for a configuration option.

    - **Namespace** *(string) --*

      A unique namespace identifying the option's associated AWS resource.

    - **Name** *(string) --*

      The name of the configuration option.

    - **DefaultValue** *(string) --*

      The default value for this configuration option.

    - **ChangeSeverity** *(string) --*

      An indication of which action is required if the value for this configuration option
      changes:

      * ``NoInterruption`` : There is no interruption to the environment or application
      availability.

      * ``RestartEnvironment`` : The environment is entirely restarted, all AWS resources are
      deleted and recreated, and the environment is unavailable during the process.

      * ``RestartApplicationServer`` : The environment is available the entire time. However, a
      short application outage occurs when the application servers on the running Amazon EC2
      instances are restarted.

    - **UserDefined** *(boolean) --*

      An indication of whether the user defined this configuration option:

      * ``true`` : This configuration option was defined by the user. It is a valid choice for
      specifying if this as an ``Option to Remove`` when updating configuration settings.

      * ``false`` : This configuration was not defined by the user.

      Constraint: You can remove only ``UserDefined`` options from a configuration.

      Valid Values: ``true`` | ``false``

    - **ValueType** *(string) --*

      An indication of which type of values this option has and whether it is allowable to
      select one or more than one of the possible values:

      * ``Scalar`` : Values for this option are a single selection from the possible values, or
      an unformatted string, or numeric value governed by the ``MIN/MAX/Regex`` constraints.

      * ``List`` : Values for this option are multiple selections from the possible values.

      * ``Boolean`` : Values for this option are either ``true`` or ``false`` .

      * ``Json`` : Values for this option are a JSON representation of a ``ConfigDocument`` .

    - **ValueOptions** *(list) --*

      If specified, values for the configuration option are selected from this list.

      - *(string) --*

    - **MinValue** *(integer) --*

      If specified, the configuration option must be a numeric value greater than this value.

    - **MaxValue** *(integer) --*

      If specified, the configuration option must be a numeric value less than this value.

    - **MaxLength** *(integer) --*

      If specified, the configuration option must be a string value no longer than this value.

    - **Regex** *(dict) --*

      If specified, the configuration option must be a string value that satisfies this regular
      expression.

      - **Pattern** *(string) --*

        The regular expression pattern that a string configuration option value with this
        restriction must match.

      - **Label** *(string) --*

        A unique name representing this regular expression.
    """


_ClientDescribeConfigurationOptionsResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationOptionsResponseTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "Options": List[ClientDescribeConfigurationOptionsResponseOptionsTypeDef],
    },
    total=False,
)


class ClientDescribeConfigurationOptionsResponseTypeDef(
    _ClientDescribeConfigurationOptionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationOptions` `Response`

    Describes the settings for a specified configuration set.

    - **SolutionStackName** *(string) --*

      The name of the solution stack these configuration options belong to.

    - **PlatformArn** *(string) --*

      The ARN of the platform.

    - **Options** *(list) --*

      A list of  ConfigurationOptionDescription .

      - *(dict) --*

        Describes the possible values for a configuration option.

        - **Namespace** *(string) --*

          A unique namespace identifying the option's associated AWS resource.

        - **Name** *(string) --*

          The name of the configuration option.

        - **DefaultValue** *(string) --*

          The default value for this configuration option.

        - **ChangeSeverity** *(string) --*

          An indication of which action is required if the value for this configuration option
          changes:

          * ``NoInterruption`` : There is no interruption to the environment or application
          availability.

          * ``RestartEnvironment`` : The environment is entirely restarted, all AWS resources are
          deleted and recreated, and the environment is unavailable during the process.

          * ``RestartApplicationServer`` : The environment is available the entire time. However, a
          short application outage occurs when the application servers on the running Amazon EC2
          instances are restarted.

        - **UserDefined** *(boolean) --*

          An indication of whether the user defined this configuration option:

          * ``true`` : This configuration option was defined by the user. It is a valid choice for
          specifying if this as an ``Option to Remove`` when updating configuration settings.

          * ``false`` : This configuration was not defined by the user.

          Constraint: You can remove only ``UserDefined`` options from a configuration.

          Valid Values: ``true`` | ``false``

        - **ValueType** *(string) --*

          An indication of which type of values this option has and whether it is allowable to
          select one or more than one of the possible values:

          * ``Scalar`` : Values for this option are a single selection from the possible values, or
          an unformatted string, or numeric value governed by the ``MIN/MAX/Regex`` constraints.

          * ``List`` : Values for this option are multiple selections from the possible values.

          * ``Boolean`` : Values for this option are either ``true`` or ``false`` .

          * ``Json`` : Values for this option are a JSON representation of a ``ConfigDocument`` .

        - **ValueOptions** *(list) --*

          If specified, values for the configuration option are selected from this list.

          - *(string) --*

        - **MinValue** *(integer) --*

          If specified, the configuration option must be a numeric value greater than this value.

        - **MaxValue** *(integer) --*

          If specified, the configuration option must be a numeric value less than this value.

        - **MaxLength** *(integer) --*

          If specified, the configuration option must be a string value no longer than this value.

        - **Regex** *(dict) --*

          If specified, the configuration option must be a string value that satisfies this regular
          expression.

          - **Pattern** *(string) --*

            The regular expression pattern that a string configuration option value with this
            restriction must match.

          - **Label** *(string) --*

            A unique name representing this regular expression.
    """


_ClientDescribeConfigurationSettingsResponseConfigurationSettingsOptionSettingsTypeDef = TypedDict(
    "_ClientDescribeConfigurationSettingsResponseConfigurationSettingsOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)


class ClientDescribeConfigurationSettingsResponseConfigurationSettingsOptionSettingsTypeDef(
    _ClientDescribeConfigurationSettingsResponseConfigurationSettingsOptionSettingsTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationSettingsResponseConfigurationSettings` `OptionSettings`

    A specification identifying an individual configuration option along with its current
    value. For a list of possible option values, go to `Option Values
    <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the
    *AWS Elastic Beanstalk Developer Guide* .

    - **ResourceName** *(string) --*

      A unique resource name for a time-based scaling configuration option.

    - **Namespace** *(string) --*

      A unique namespace identifying the option's associated AWS resource.

    - **OptionName** *(string) --*

      The name of the configuration option.

    - **Value** *(string) --*

      The current value for the configuration option.
    """


_ClientDescribeConfigurationSettingsResponseConfigurationSettingsTypeDef = TypedDict(
    "_ClientDescribeConfigurationSettingsResponseConfigurationSettingsTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "ApplicationName": str,
        "TemplateName": str,
        "Description": str,
        "EnvironmentName": str,
        "DeploymentStatus": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "OptionSettings": List[
            ClientDescribeConfigurationSettingsResponseConfigurationSettingsOptionSettingsTypeDef
        ],
    },
    total=False,
)


class ClientDescribeConfigurationSettingsResponseConfigurationSettingsTypeDef(
    _ClientDescribeConfigurationSettingsResponseConfigurationSettingsTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationSettingsResponse` `ConfigurationSettings`

    Describes the settings for a configuration set.

    - **SolutionStackName** *(string) --*

      The name of the solution stack this configuration set uses.

    - **PlatformArn** *(string) --*

      The ARN of the platform.

    - **ApplicationName** *(string) --*

      The name of the application associated with this configuration set.

    - **TemplateName** *(string) --*

      If not ``null`` , the name of the configuration template for this configuration set.

    - **Description** *(string) --*

      Describes this configuration set.

    - **EnvironmentName** *(string) --*

      If not ``null`` , the name of the environment for this configuration set.

    - **DeploymentStatus** *(string) --*

      If this configuration set is associated with an environment, the ``DeploymentStatus``
      parameter indicates the deployment status of this configuration set:

      * ``null`` : This configuration is not associated with a running environment.

      * ``pending`` : This is a draft configuration that is not deployed to the associated
      environment but is in the process of deploying.

      * ``deployed`` : This is the configuration that is currently deployed to the associated
      running environment.

      * ``failed`` : This is a draft configuration that failed to successfully deploy.

    - **DateCreated** *(datetime) --*

      The date (in UTC time) when this configuration set was created.

    - **DateUpdated** *(datetime) --*

      The date (in UTC time) when this configuration set was last modified.

    - **OptionSettings** *(list) --*

      A list of the configuration options and their values in this configuration set.

      - *(dict) --*

        A specification identifying an individual configuration option along with its current
        value. For a list of possible option values, go to `Option Values
        <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the
        *AWS Elastic Beanstalk Developer Guide* .

        - **ResourceName** *(string) --*

          A unique resource name for a time-based scaling configuration option.

        - **Namespace** *(string) --*

          A unique namespace identifying the option's associated AWS resource.

        - **OptionName** *(string) --*

          The name of the configuration option.

        - **Value** *(string) --*

          The current value for the configuration option.
    """


_ClientDescribeConfigurationSettingsResponseTypeDef = TypedDict(
    "_ClientDescribeConfigurationSettingsResponseTypeDef",
    {
        "ConfigurationSettings": List[
            ClientDescribeConfigurationSettingsResponseConfigurationSettingsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeConfigurationSettingsResponseTypeDef(
    _ClientDescribeConfigurationSettingsResponseTypeDef
):
    """
    Type definition for `ClientDescribeConfigurationSettings` `Response`

    The results from a request to change the configuration settings of an environment.

    - **ConfigurationSettings** *(list) --*

      A list of  ConfigurationSettingsDescription .

      - *(dict) --*

        Describes the settings for a configuration set.

        - **SolutionStackName** *(string) --*

          The name of the solution stack this configuration set uses.

        - **PlatformArn** *(string) --*

          The ARN of the platform.

        - **ApplicationName** *(string) --*

          The name of the application associated with this configuration set.

        - **TemplateName** *(string) --*

          If not ``null`` , the name of the configuration template for this configuration set.

        - **Description** *(string) --*

          Describes this configuration set.

        - **EnvironmentName** *(string) --*

          If not ``null`` , the name of the environment for this configuration set.

        - **DeploymentStatus** *(string) --*

          If this configuration set is associated with an environment, the ``DeploymentStatus``
          parameter indicates the deployment status of this configuration set:

          * ``null`` : This configuration is not associated with a running environment.

          * ``pending`` : This is a draft configuration that is not deployed to the associated
          environment but is in the process of deploying.

          * ``deployed`` : This is the configuration that is currently deployed to the associated
          running environment.

          * ``failed`` : This is a draft configuration that failed to successfully deploy.

        - **DateCreated** *(datetime) --*

          The date (in UTC time) when this configuration set was created.

        - **DateUpdated** *(datetime) --*

          The date (in UTC time) when this configuration set was last modified.

        - **OptionSettings** *(list) --*

          A list of the configuration options and their values in this configuration set.

          - *(dict) --*

            A specification identifying an individual configuration option along with its current
            value. For a list of possible option values, go to `Option Values
            <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the
            *AWS Elastic Beanstalk Developer Guide* .

            - **ResourceName** *(string) --*

              A unique resource name for a time-based scaling configuration option.

            - **Namespace** *(string) --*

              A unique namespace identifying the option's associated AWS resource.

            - **OptionName** *(string) --*

              The name of the configuration option.

            - **Value** *(string) --*

              The current value for the configuration option.
    """


_ClientDescribeEnvironmentHealthResponseApplicationMetricsLatencyTypeDef = TypedDict(
    "_ClientDescribeEnvironmentHealthResponseApplicationMetricsLatencyTypeDef",
    {
        "P999": float,
        "P99": float,
        "P95": float,
        "P90": float,
        "P85": float,
        "P75": float,
        "P50": float,
        "P10": float,
    },
    total=False,
)


class ClientDescribeEnvironmentHealthResponseApplicationMetricsLatencyTypeDef(
    _ClientDescribeEnvironmentHealthResponseApplicationMetricsLatencyTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentHealthResponseApplicationMetrics` `Latency`

    Represents the average latency for the slowest X percent of requests over the last 10
    seconds. Latencies are in seconds with one millisecond resolution.

    - **P999** *(float) --*

      The average latency for the slowest 0.1 percent of requests over the last 10 seconds.

    - **P99** *(float) --*

      The average latency for the slowest 1 percent of requests over the last 10 seconds.

    - **P95** *(float) --*

      The average latency for the slowest 5 percent of requests over the last 10 seconds.

    - **P90** *(float) --*

      The average latency for the slowest 10 percent of requests over the last 10 seconds.

    - **P85** *(float) --*

      The average latency for the slowest 15 percent of requests over the last 10 seconds.

    - **P75** *(float) --*

      The average latency for the slowest 25 percent of requests over the last 10 seconds.

    - **P50** *(float) --*

      The average latency for the slowest 50 percent of requests over the last 10 seconds.

    - **P10** *(float) --*

      The average latency for the slowest 90 percent of requests over the last 10 seconds.
    """


_ClientDescribeEnvironmentHealthResponseApplicationMetricsStatusCodesTypeDef = TypedDict(
    "_ClientDescribeEnvironmentHealthResponseApplicationMetricsStatusCodesTypeDef",
    {"Status2xx": int, "Status3xx": int, "Status4xx": int, "Status5xx": int},
    total=False,
)


class ClientDescribeEnvironmentHealthResponseApplicationMetricsStatusCodesTypeDef(
    _ClientDescribeEnvironmentHealthResponseApplicationMetricsStatusCodesTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentHealthResponseApplicationMetrics` `StatusCodes`

    Represents the percentage of requests over the last 10 seconds that resulted in each type
    of status code response.

    - **Status2xx** *(integer) --*

      The percentage of requests over the last 10 seconds that resulted in a 2xx (200, 201,
      etc.) status code.

    - **Status3xx** *(integer) --*

      The percentage of requests over the last 10 seconds that resulted in a 3xx (300, 301,
      etc.) status code.

    - **Status4xx** *(integer) --*

      The percentage of requests over the last 10 seconds that resulted in a 4xx (400, 401,
      etc.) status code.

    - **Status5xx** *(integer) --*

      The percentage of requests over the last 10 seconds that resulted in a 5xx (500, 501,
      etc.) status code.
    """


_ClientDescribeEnvironmentHealthResponseApplicationMetricsTypeDef = TypedDict(
    "_ClientDescribeEnvironmentHealthResponseApplicationMetricsTypeDef",
    {
        "Duration": int,
        "RequestCount": int,
        "StatusCodes": ClientDescribeEnvironmentHealthResponseApplicationMetricsStatusCodesTypeDef,
        "Latency": ClientDescribeEnvironmentHealthResponseApplicationMetricsLatencyTypeDef,
    },
    total=False,
)


class ClientDescribeEnvironmentHealthResponseApplicationMetricsTypeDef(
    _ClientDescribeEnvironmentHealthResponseApplicationMetricsTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentHealthResponse` `ApplicationMetrics`

    Application request metrics for the environment.

    - **Duration** *(integer) --*

      The amount of time that the metrics cover (usually 10 seconds). For example, you might have
      5 requests (``request_count`` ) within the most recent time slice of 10 seconds
      (``duration`` ).

    - **RequestCount** *(integer) --*

      Average number of requests handled by the web server per second over the last 10 seconds.

    - **StatusCodes** *(dict) --*

      Represents the percentage of requests over the last 10 seconds that resulted in each type
      of status code response.

      - **Status2xx** *(integer) --*

        The percentage of requests over the last 10 seconds that resulted in a 2xx (200, 201,
        etc.) status code.

      - **Status3xx** *(integer) --*

        The percentage of requests over the last 10 seconds that resulted in a 3xx (300, 301,
        etc.) status code.

      - **Status4xx** *(integer) --*

        The percentage of requests over the last 10 seconds that resulted in a 4xx (400, 401,
        etc.) status code.

      - **Status5xx** *(integer) --*

        The percentage of requests over the last 10 seconds that resulted in a 5xx (500, 501,
        etc.) status code.

    - **Latency** *(dict) --*

      Represents the average latency for the slowest X percent of requests over the last 10
      seconds. Latencies are in seconds with one millisecond resolution.

      - **P999** *(float) --*

        The average latency for the slowest 0.1 percent of requests over the last 10 seconds.

      - **P99** *(float) --*

        The average latency for the slowest 1 percent of requests over the last 10 seconds.

      - **P95** *(float) --*

        The average latency for the slowest 5 percent of requests over the last 10 seconds.

      - **P90** *(float) --*

        The average latency for the slowest 10 percent of requests over the last 10 seconds.

      - **P85** *(float) --*

        The average latency for the slowest 15 percent of requests over the last 10 seconds.

      - **P75** *(float) --*

        The average latency for the slowest 25 percent of requests over the last 10 seconds.

      - **P50** *(float) --*

        The average latency for the slowest 50 percent of requests over the last 10 seconds.

      - **P10** *(float) --*

        The average latency for the slowest 90 percent of requests over the last 10 seconds.
    """


_ClientDescribeEnvironmentHealthResponseInstancesHealthTypeDef = TypedDict(
    "_ClientDescribeEnvironmentHealthResponseInstancesHealthTypeDef",
    {
        "NoData": int,
        "Unknown": int,
        "Pending": int,
        "Ok": int,
        "Info": int,
        "Warning": int,
        "Degraded": int,
        "Severe": int,
    },
    total=False,
)


class ClientDescribeEnvironmentHealthResponseInstancesHealthTypeDef(
    _ClientDescribeEnvironmentHealthResponseInstancesHealthTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentHealthResponse` `InstancesHealth`

    Summary health information for the instances in the environment.

    - **NoData** *(integer) --*

       **Grey.** AWS Elastic Beanstalk and the health agent are reporting no data on an instance.

    - **Unknown** *(integer) --*

       **Grey.** AWS Elastic Beanstalk and the health agent are reporting an insufficient amount
       of data on an instance.

    - **Pending** *(integer) --*

       **Grey.** An operation is in progress on an instance within the command timeout.

    - **Ok** *(integer) --*

       **Green.** An instance is passing health checks and the health agent is not reporting any
       problems.

    - **Info** *(integer) --*

       **Green.** An operation is in progress on an instance.

    - **Warning** *(integer) --*

       **Yellow.** The health agent is reporting a moderate number of request failures or other
       issues for an instance or environment.

    - **Degraded** *(integer) --*

       **Red.** The health agent is reporting a high number of request failures or other issues
       for an instance or environment.

    - **Severe** *(integer) --*

       **Red.** The health agent is reporting a very high number of request failures or other
       issues for an instance or environment.
    """


_ClientDescribeEnvironmentHealthResponseTypeDef = TypedDict(
    "_ClientDescribeEnvironmentHealthResponseTypeDef",
    {
        "EnvironmentName": str,
        "HealthStatus": str,
        "Status": str,
        "Color": str,
        "Causes": List[str],
        "ApplicationMetrics": ClientDescribeEnvironmentHealthResponseApplicationMetricsTypeDef,
        "InstancesHealth": ClientDescribeEnvironmentHealthResponseInstancesHealthTypeDef,
        "RefreshedAt": datetime,
    },
    total=False,
)


class ClientDescribeEnvironmentHealthResponseTypeDef(
    _ClientDescribeEnvironmentHealthResponseTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentHealth` `Response`

    Health details for an AWS Elastic Beanstalk environment.

    - **EnvironmentName** *(string) --*

      The environment's name.

    - **HealthStatus** *(string) --*

      The `health status
      <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ of
      the environment. For example, ``Ok`` .

    - **Status** *(string) --*

      The environment's operational status. ``Ready`` , ``Launching`` , ``Updating`` ,
      ``Terminating`` , or ``Terminated`` .

    - **Color** *(string) --*

      The `health color
      <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ of
      the environment.

    - **Causes** *(list) --*

      Descriptions of the data that contributed to the environment's current health status.

      - *(string) --*

    - **ApplicationMetrics** *(dict) --*

      Application request metrics for the environment.

      - **Duration** *(integer) --*

        The amount of time that the metrics cover (usually 10 seconds). For example, you might have
        5 requests (``request_count`` ) within the most recent time slice of 10 seconds
        (``duration`` ).

      - **RequestCount** *(integer) --*

        Average number of requests handled by the web server per second over the last 10 seconds.

      - **StatusCodes** *(dict) --*

        Represents the percentage of requests over the last 10 seconds that resulted in each type
        of status code response.

        - **Status2xx** *(integer) --*

          The percentage of requests over the last 10 seconds that resulted in a 2xx (200, 201,
          etc.) status code.

        - **Status3xx** *(integer) --*

          The percentage of requests over the last 10 seconds that resulted in a 3xx (300, 301,
          etc.) status code.

        - **Status4xx** *(integer) --*

          The percentage of requests over the last 10 seconds that resulted in a 4xx (400, 401,
          etc.) status code.

        - **Status5xx** *(integer) --*

          The percentage of requests over the last 10 seconds that resulted in a 5xx (500, 501,
          etc.) status code.

      - **Latency** *(dict) --*

        Represents the average latency for the slowest X percent of requests over the last 10
        seconds. Latencies are in seconds with one millisecond resolution.

        - **P999** *(float) --*

          The average latency for the slowest 0.1 percent of requests over the last 10 seconds.

        - **P99** *(float) --*

          The average latency for the slowest 1 percent of requests over the last 10 seconds.

        - **P95** *(float) --*

          The average latency for the slowest 5 percent of requests over the last 10 seconds.

        - **P90** *(float) --*

          The average latency for the slowest 10 percent of requests over the last 10 seconds.

        - **P85** *(float) --*

          The average latency for the slowest 15 percent of requests over the last 10 seconds.

        - **P75** *(float) --*

          The average latency for the slowest 25 percent of requests over the last 10 seconds.

        - **P50** *(float) --*

          The average latency for the slowest 50 percent of requests over the last 10 seconds.

        - **P10** *(float) --*

          The average latency for the slowest 90 percent of requests over the last 10 seconds.

    - **InstancesHealth** *(dict) --*

      Summary health information for the instances in the environment.

      - **NoData** *(integer) --*

         **Grey.** AWS Elastic Beanstalk and the health agent are reporting no data on an instance.

      - **Unknown** *(integer) --*

         **Grey.** AWS Elastic Beanstalk and the health agent are reporting an insufficient amount
         of data on an instance.

      - **Pending** *(integer) --*

         **Grey.** An operation is in progress on an instance within the command timeout.

      - **Ok** *(integer) --*

         **Green.** An instance is passing health checks and the health agent is not reporting any
         problems.

      - **Info** *(integer) --*

         **Green.** An operation is in progress on an instance.

      - **Warning** *(integer) --*

         **Yellow.** The health agent is reporting a moderate number of request failures or other
         issues for an instance or environment.

      - **Degraded** *(integer) --*

         **Red.** The health agent is reporting a high number of request failures or other issues
         for an instance or environment.

      - **Severe** *(integer) --*

         **Red.** The health agent is reporting a very high number of request failures or other
         issues for an instance or environment.

    - **RefreshedAt** *(datetime) --*

      The date and time that the health information was retrieved.
    """


_ClientDescribeEnvironmentManagedActionHistoryResponseManagedActionHistoryItemsTypeDef = TypedDict(
    "_ClientDescribeEnvironmentManagedActionHistoryResponseManagedActionHistoryItemsTypeDef",
    {
        "ActionId": str,
        "ActionType": str,
        "ActionDescription": str,
        "FailureType": str,
        "Status": str,
        "FailureDescription": str,
        "ExecutedTime": datetime,
        "FinishedTime": datetime,
    },
    total=False,
)


class ClientDescribeEnvironmentManagedActionHistoryResponseManagedActionHistoryItemsTypeDef(
    _ClientDescribeEnvironmentManagedActionHistoryResponseManagedActionHistoryItemsTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentManagedActionHistoryResponse` `ManagedActionHistoryItems`

    The record of a completed or failed managed action.

    - **ActionId** *(string) --*

      A unique identifier for the managed action.

    - **ActionType** *(string) --*

      The type of the managed action.

    - **ActionDescription** *(string) --*

      A description of the managed action.

    - **FailureType** *(string) --*

      If the action failed, the type of failure.

    - **Status** *(string) --*

      The status of the action.

    - **FailureDescription** *(string) --*

      If the action failed, a description of the failure.

    - **ExecutedTime** *(datetime) --*

      The date and time that the action started executing.

    - **FinishedTime** *(datetime) --*

      The date and time that the action finished executing.
    """


_ClientDescribeEnvironmentManagedActionHistoryResponseTypeDef = TypedDict(
    "_ClientDescribeEnvironmentManagedActionHistoryResponseTypeDef",
    {
        "ManagedActionHistoryItems": List[
            ClientDescribeEnvironmentManagedActionHistoryResponseManagedActionHistoryItemsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeEnvironmentManagedActionHistoryResponseTypeDef(
    _ClientDescribeEnvironmentManagedActionHistoryResponseTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentManagedActionHistory` `Response`

    A result message containing a list of completed and failed managed actions.

    - **ManagedActionHistoryItems** *(list) --*

      A list of completed and failed managed actions.

      - *(dict) --*

        The record of a completed or failed managed action.

        - **ActionId** *(string) --*

          A unique identifier for the managed action.

        - **ActionType** *(string) --*

          The type of the managed action.

        - **ActionDescription** *(string) --*

          A description of the managed action.

        - **FailureType** *(string) --*

          If the action failed, the type of failure.

        - **Status** *(string) --*

          The status of the action.

        - **FailureDescription** *(string) --*

          If the action failed, a description of the failure.

        - **ExecutedTime** *(datetime) --*

          The date and time that the action started executing.

        - **FinishedTime** *(datetime) --*

          The date and time that the action finished executing.

    - **NextToken** *(string) --*

      A pagination token that you pass to  DescribeEnvironmentManagedActionHistory to get the next
      page of results.
    """


_ClientDescribeEnvironmentManagedActionsResponseManagedActionsTypeDef = TypedDict(
    "_ClientDescribeEnvironmentManagedActionsResponseManagedActionsTypeDef",
    {
        "ActionId": str,
        "ActionDescription": str,
        "ActionType": str,
        "Status": str,
        "WindowStartTime": datetime,
    },
    total=False,
)


class ClientDescribeEnvironmentManagedActionsResponseManagedActionsTypeDef(
    _ClientDescribeEnvironmentManagedActionsResponseManagedActionsTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentManagedActionsResponse` `ManagedActions`

    The record of an upcoming or in-progress managed action.

    - **ActionId** *(string) --*

      A unique identifier for the managed action.

    - **ActionDescription** *(string) --*

      A description of the managed action.

    - **ActionType** *(string) --*

      The type of managed action.

    - **Status** *(string) --*

      The status of the managed action. If the action is ``Scheduled`` , you can apply it
      immediately with  ApplyEnvironmentManagedAction .

    - **WindowStartTime** *(datetime) --*

      The start time of the maintenance window in which the managed action will execute.
    """


_ClientDescribeEnvironmentManagedActionsResponseTypeDef = TypedDict(
    "_ClientDescribeEnvironmentManagedActionsResponseTypeDef",
    {
        "ManagedActions": List[
            ClientDescribeEnvironmentManagedActionsResponseManagedActionsTypeDef
        ]
    },
    total=False,
)


class ClientDescribeEnvironmentManagedActionsResponseTypeDef(
    _ClientDescribeEnvironmentManagedActionsResponseTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentManagedActions` `Response`

    The result message containing a list of managed actions.

    - **ManagedActions** *(list) --*

      A list of upcoming and in-progress managed actions.

      - *(dict) --*

        The record of an upcoming or in-progress managed action.

        - **ActionId** *(string) --*

          A unique identifier for the managed action.

        - **ActionDescription** *(string) --*

          A description of the managed action.

        - **ActionType** *(string) --*

          The type of managed action.

        - **Status** *(string) --*

          The status of the managed action. If the action is ``Scheduled`` , you can apply it
          immediately with  ApplyEnvironmentManagedAction .

        - **WindowStartTime** *(datetime) --*

          The start time of the maintenance window in which the managed action will execute.
    """


_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesAutoScalingGroupsTypeDef = TypedDict(
    "_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesAutoScalingGroupsTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesAutoScalingGroupsTypeDef(
    _ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesAutoScalingGroupsTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentResourcesResponseEnvironmentResources` `AutoScalingGroups`

    Describes an Auto Scaling launch configuration.

    - **Name** *(string) --*

      The name of the ``AutoScalingGroup`` .
    """


_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesInstancesTypeDef = TypedDict(
    "_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesInstancesTypeDef",
    {"Id": str},
    total=False,
)


class ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesInstancesTypeDef(
    _ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesInstancesTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentResourcesResponseEnvironmentResources` `Instances`

    The description of an Amazon EC2 instance.

    - **Id** *(string) --*

      The ID of the Amazon EC2 instance.
    """


_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchConfigurationsTypeDef = TypedDict(
    "_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchConfigurationsTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchConfigurationsTypeDef(
    _ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchConfigurationsTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentResourcesResponseEnvironmentResources` `LaunchConfigurations`

    Describes an Auto Scaling launch configuration.

    - **Name** *(string) --*

      The name of the launch configuration.
    """


_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchTemplatesTypeDef = TypedDict(
    "_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchTemplatesTypeDef",
    {"Id": str},
    total=False,
)


class ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchTemplatesTypeDef(
    _ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchTemplatesTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentResourcesResponseEnvironmentResources` `LaunchTemplates`

    Describes an Amazon EC2 launch template.

    - **Id** *(string) --*

      The ID of the launch template.
    """


_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLoadBalancersTypeDef = TypedDict(
    "_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLoadBalancersTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLoadBalancersTypeDef(
    _ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLoadBalancersTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentResourcesResponseEnvironmentResources` `LoadBalancers`

    Describes a LoadBalancer.

    - **Name** *(string) --*

      The name of the LoadBalancer.
    """


_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesQueuesTypeDef = TypedDict(
    "_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesQueuesTypeDef",
    {"Name": str, "URL": str},
    total=False,
)


class ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesQueuesTypeDef(
    _ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesQueuesTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentResourcesResponseEnvironmentResources` `Queues`

    Describes a queue.

    - **Name** *(string) --*

      The name of the queue.

    - **URL** *(string) --*

      The URL of the queue.
    """


_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTriggersTypeDef = TypedDict(
    "_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTriggersTypeDef",
    {"Name": str},
    total=False,
)


class ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTriggersTypeDef(
    _ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTriggersTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentResourcesResponseEnvironmentResources` `Triggers`

    Describes a trigger.

    - **Name** *(string) --*

      The name of the trigger.
    """


_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTypeDef = TypedDict(
    "_ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTypeDef",
    {
        "EnvironmentName": str,
        "AutoScalingGroups": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesAutoScalingGroupsTypeDef
        ],
        "Instances": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesInstancesTypeDef
        ],
        "LaunchConfigurations": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchConfigurationsTypeDef
        ],
        "LaunchTemplates": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLaunchTemplatesTypeDef
        ],
        "LoadBalancers": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesLoadBalancersTypeDef
        ],
        "Triggers": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTriggersTypeDef
        ],
        "Queues": List[
            ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesQueuesTypeDef
        ],
    },
    total=False,
)


class ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTypeDef(
    _ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentResourcesResponse` `EnvironmentResources`

    A list of  EnvironmentResourceDescription .

    - **EnvironmentName** *(string) --*

      The name of the environment.

    - **AutoScalingGroups** *(list) --*

      The ``AutoScalingGroups`` used by this environment.

      - *(dict) --*

        Describes an Auto Scaling launch configuration.

        - **Name** *(string) --*

          The name of the ``AutoScalingGroup`` .

    - **Instances** *(list) --*

      The Amazon EC2 instances used by this environment.

      - *(dict) --*

        The description of an Amazon EC2 instance.

        - **Id** *(string) --*

          The ID of the Amazon EC2 instance.

    - **LaunchConfigurations** *(list) --*

      The Auto Scaling launch configurations in use by this environment.

      - *(dict) --*

        Describes an Auto Scaling launch configuration.

        - **Name** *(string) --*

          The name of the launch configuration.

    - **LaunchTemplates** *(list) --*

      The Amazon EC2 launch templates in use by this environment.

      - *(dict) --*

        Describes an Amazon EC2 launch template.

        - **Id** *(string) --*

          The ID of the launch template.

    - **LoadBalancers** *(list) --*

      The LoadBalancers in use by this environment.

      - *(dict) --*

        Describes a LoadBalancer.

        - **Name** *(string) --*

          The name of the LoadBalancer.

    - **Triggers** *(list) --*

      The ``AutoScaling`` triggers in use by this environment.

      - *(dict) --*

        Describes a trigger.

        - **Name** *(string) --*

          The name of the trigger.

    - **Queues** *(list) --*

      The queues used by this environment.

      - *(dict) --*

        Describes a queue.

        - **Name** *(string) --*

          The name of the queue.

        - **URL** *(string) --*

          The URL of the queue.
    """


_ClientDescribeEnvironmentResourcesResponseTypeDef = TypedDict(
    "_ClientDescribeEnvironmentResourcesResponseTypeDef",
    {
        "EnvironmentResources": ClientDescribeEnvironmentResourcesResponseEnvironmentResourcesTypeDef
    },
    total=False,
)


class ClientDescribeEnvironmentResourcesResponseTypeDef(
    _ClientDescribeEnvironmentResourcesResponseTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentResources` `Response`

    Result message containing a list of environment resource descriptions.

    - **EnvironmentResources** *(dict) --*

      A list of  EnvironmentResourceDescription .

      - **EnvironmentName** *(string) --*

        The name of the environment.

      - **AutoScalingGroups** *(list) --*

        The ``AutoScalingGroups`` used by this environment.

        - *(dict) --*

          Describes an Auto Scaling launch configuration.

          - **Name** *(string) --*

            The name of the ``AutoScalingGroup`` .

      - **Instances** *(list) --*

        The Amazon EC2 instances used by this environment.

        - *(dict) --*

          The description of an Amazon EC2 instance.

          - **Id** *(string) --*

            The ID of the Amazon EC2 instance.

      - **LaunchConfigurations** *(list) --*

        The Auto Scaling launch configurations in use by this environment.

        - *(dict) --*

          Describes an Auto Scaling launch configuration.

          - **Name** *(string) --*

            The name of the launch configuration.

      - **LaunchTemplates** *(list) --*

        The Amazon EC2 launch templates in use by this environment.

        - *(dict) --*

          Describes an Amazon EC2 launch template.

          - **Id** *(string) --*

            The ID of the launch template.

      - **LoadBalancers** *(list) --*

        The LoadBalancers in use by this environment.

        - *(dict) --*

          Describes a LoadBalancer.

          - **Name** *(string) --*

            The name of the LoadBalancer.

      - **Triggers** *(list) --*

        The ``AutoScaling`` triggers in use by this environment.

        - *(dict) --*

          Describes a trigger.

          - **Name** *(string) --*

            The name of the trigger.

      - **Queues** *(list) --*

        The queues used by this environment.

        - *(dict) --*

          Describes a queue.

          - **Name** *(string) --*

            The name of the queue.

          - **URL** *(string) --*

            The URL of the queue.
    """


_ClientDescribeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef",
    {"LinkName": str, "EnvironmentName": str},
    total=False,
)


class ClientDescribeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef(
    _ClientDescribeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentsResponseEnvironments` `EnvironmentLinks`

    A link to another environment, defined in the environment's manifest. Links provide
    connection information in system properties that can be used to connect to another
    environment in the same group. See `Environment Manifest (env.yaml)
    <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__
    for details.

    - **LinkName** *(string) --*

      The name of the link.

    - **EnvironmentName** *(string) --*

      The name of the linked environment (the dependency).
    """


_ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef",
    {"Protocol": str, "Port": int},
    total=False,
)


class ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef(
    _ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancer` `Listeners`

    Describes the properties of a Listener for the LoadBalancer.

    - **Protocol** *(string) --*

      The protocol that is used by the Listener.

    - **Port** *(integer) --*

      The port that is used by the Listener.
    """


_ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List[
            ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerListenersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef(
    _ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentsResponseEnvironmentsResources` `LoadBalancer`

    Describes the LoadBalancer.

    - **LoadBalancerName** *(string) --*

      The name of the LoadBalancer.

    - **Domain** *(string) --*

      The domain name of the LoadBalancer.

    - **Listeners** *(list) --*

      A list of Listeners used by the LoadBalancer.

      - *(dict) --*

        Describes the properties of a Listener for the LoadBalancer.

        - **Protocol** *(string) --*

          The protocol that is used by the Listener.

        - **Port** *(integer) --*

          The port that is used by the Listener.
    """


_ClientDescribeEnvironmentsResponseEnvironmentsResourcesTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseEnvironmentsResourcesTypeDef",
    {
        "LoadBalancer": ClientDescribeEnvironmentsResponseEnvironmentsResourcesLoadBalancerTypeDef
    },
    total=False,
)


class ClientDescribeEnvironmentsResponseEnvironmentsResourcesTypeDef(
    _ClientDescribeEnvironmentsResponseEnvironmentsResourcesTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentsResponseEnvironments` `Resources`

    The description of the AWS resources used by this environment.

    - **LoadBalancer** *(dict) --*

      Describes the LoadBalancer.

      - **LoadBalancerName** *(string) --*

        The name of the LoadBalancer.

      - **Domain** *(string) --*

        The domain name of the LoadBalancer.

      - **Listeners** *(list) --*

        A list of Listeners used by the LoadBalancer.

        - *(dict) --*

          Describes the properties of a Listener for the LoadBalancer.

          - **Protocol** *(string) --*

            The protocol that is used by the Listener.

          - **Port** *(integer) --*

            The port that is used by the Listener.
    """


_ClientDescribeEnvironmentsResponseEnvironmentsTierTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseEnvironmentsTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)


class ClientDescribeEnvironmentsResponseEnvironmentsTierTypeDef(
    _ClientDescribeEnvironmentsResponseEnvironmentsTierTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentsResponseEnvironments` `Tier`

    Describes the current tier of this environment.

    - **Name** *(string) --*

      The name of this environment tier.

      Valid values:

      * For *Web server tier* – ``WebServer``

      * For *Worker tier* – ``Worker``

    - **Type** *(string) --*

      The type of this environment tier.

      Valid values:

      * For *Web server tier* – ``Standard``

      * For *Worker tier* – ``SQS/HTTP``

    - **Version** *(string) --*

      The version of this environment tier. When you don't set a value to it, Elastic
      Beanstalk uses the latest compatible worker tier version.

      .. note::

        This member is deprecated. Any specific version that you set may become out of date.
        We recommend leaving it unspecified.
    """


_ClientDescribeEnvironmentsResponseEnvironmentsTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseEnvironmentsTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": str,
        "AbortableOperationInProgress": bool,
        "Health": str,
        "HealthStatus": str,
        "Resources": ClientDescribeEnvironmentsResponseEnvironmentsResourcesTypeDef,
        "Tier": ClientDescribeEnvironmentsResponseEnvironmentsTierTypeDef,
        "EnvironmentLinks": List[
            ClientDescribeEnvironmentsResponseEnvironmentsEnvironmentLinksTypeDef
        ],
        "EnvironmentArn": str,
    },
    total=False,
)


class ClientDescribeEnvironmentsResponseEnvironmentsTypeDef(
    _ClientDescribeEnvironmentsResponseEnvironmentsTypeDef
):
    """
    Type definition for `ClientDescribeEnvironmentsResponse` `Environments`

    Describes the properties of an environment.

    - **EnvironmentName** *(string) --*

      The name of this environment.

    - **EnvironmentId** *(string) --*

      The ID of this environment.

    - **ApplicationName** *(string) --*

      The name of the application associated with this environment.

    - **VersionLabel** *(string) --*

      The application version deployed in this environment.

    - **SolutionStackName** *(string) --*

      The name of the ``SolutionStack`` deployed with this environment.

    - **PlatformArn** *(string) --*

      The ARN of the platform.

    - **TemplateName** *(string) --*

      The name of the configuration template used to originally launch this environment.

    - **Description** *(string) --*

      Describes this environment.

    - **EndpointURL** *(string) --*

      For load-balanced, autoscaling environments, the URL to the LoadBalancer. For
      single-instance environments, the IP address of the instance.

    - **CNAME** *(string) --*

      The URL to the CNAME for this environment.

    - **DateCreated** *(datetime) --*

      The creation date for this environment.

    - **DateUpdated** *(datetime) --*

      The last modified date for this environment.

    - **Status** *(string) --*

      The current operational status of the environment:

      * ``Launching`` : Environment is in the process of initial deployment.

      * ``Updating`` : Environment is in the process of updating its configuration settings or
      application version.

      * ``Ready`` : Environment is available to have an action performed on it, such as update
      or terminate.

      * ``Terminating`` : Environment is in the shut-down process.

      * ``Terminated`` : Environment is not running.

    - **AbortableOperationInProgress** *(boolean) --*

      Indicates if there is an in-progress environment configuration update or application
      version deployment that you can cancel.

       ``true:`` There is an update in progress.

       ``false:`` There are no updates currently in progress.

    - **Health** *(string) --*

      Describes the health status of the environment. AWS Elastic Beanstalk indicates the
      failure levels for a running environment:

      * ``Red`` : Indicates the environment is not responsive. Occurs when three or more
      consecutive failures occur for an environment.

      * ``Yellow`` : Indicates that something is wrong. Occurs when two consecutive failures
      occur for an environment.

      * ``Green`` : Indicates the environment is healthy and fully functional.

      * ``Grey`` : Default health for a new environment. The environment is not fully launched
      and health checks have not started or health checks are suspended during an
      ``UpdateEnvironment`` or ``RestartEnvironment`` request.

      Default: ``Grey``

    - **HealthStatus** *(string) --*

      Returns the health status of the application running in your environment. For more
      information, see `Health Colors and Statuses
      <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

    - **Resources** *(dict) --*

      The description of the AWS resources used by this environment.

      - **LoadBalancer** *(dict) --*

        Describes the LoadBalancer.

        - **LoadBalancerName** *(string) --*

          The name of the LoadBalancer.

        - **Domain** *(string) --*

          The domain name of the LoadBalancer.

        - **Listeners** *(list) --*

          A list of Listeners used by the LoadBalancer.

          - *(dict) --*

            Describes the properties of a Listener for the LoadBalancer.

            - **Protocol** *(string) --*

              The protocol that is used by the Listener.

            - **Port** *(integer) --*

              The port that is used by the Listener.

    - **Tier** *(dict) --*

      Describes the current tier of this environment.

      - **Name** *(string) --*

        The name of this environment tier.

        Valid values:

        * For *Web server tier* – ``WebServer``

        * For *Worker tier* – ``Worker``

      - **Type** *(string) --*

        The type of this environment tier.

        Valid values:

        * For *Web server tier* – ``Standard``

        * For *Worker tier* – ``SQS/HTTP``

      - **Version** *(string) --*

        The version of this environment tier. When you don't set a value to it, Elastic
        Beanstalk uses the latest compatible worker tier version.

        .. note::

          This member is deprecated. Any specific version that you set may become out of date.
          We recommend leaving it unspecified.

    - **EnvironmentLinks** *(list) --*

      A list of links to other environments in the same group.

      - *(dict) --*

        A link to another environment, defined in the environment's manifest. Links provide
        connection information in system properties that can be used to connect to another
        environment in the same group. See `Environment Manifest (env.yaml)
        <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__
        for details.

        - **LinkName** *(string) --*

          The name of the link.

        - **EnvironmentName** *(string) --*

          The name of the linked environment (the dependency).

    - **EnvironmentArn** *(string) --*

      The environment's Amazon Resource Name (ARN), which can be used in other API requests
      that require an ARN.
    """


_ClientDescribeEnvironmentsResponseTypeDef = TypedDict(
    "_ClientDescribeEnvironmentsResponseTypeDef",
    {
        "Environments": List[ClientDescribeEnvironmentsResponseEnvironmentsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeEnvironmentsResponseTypeDef(
    _ClientDescribeEnvironmentsResponseTypeDef
):
    """
    Type definition for `ClientDescribeEnvironments` `Response`

    Result message containing a list of environment descriptions.

    - **Environments** *(list) --*

      Returns an  EnvironmentDescription list.

      - *(dict) --*

        Describes the properties of an environment.

        - **EnvironmentName** *(string) --*

          The name of this environment.

        - **EnvironmentId** *(string) --*

          The ID of this environment.

        - **ApplicationName** *(string) --*

          The name of the application associated with this environment.

        - **VersionLabel** *(string) --*

          The application version deployed in this environment.

        - **SolutionStackName** *(string) --*

          The name of the ``SolutionStack`` deployed with this environment.

        - **PlatformArn** *(string) --*

          The ARN of the platform.

        - **TemplateName** *(string) --*

          The name of the configuration template used to originally launch this environment.

        - **Description** *(string) --*

          Describes this environment.

        - **EndpointURL** *(string) --*

          For load-balanced, autoscaling environments, the URL to the LoadBalancer. For
          single-instance environments, the IP address of the instance.

        - **CNAME** *(string) --*

          The URL to the CNAME for this environment.

        - **DateCreated** *(datetime) --*

          The creation date for this environment.

        - **DateUpdated** *(datetime) --*

          The last modified date for this environment.

        - **Status** *(string) --*

          The current operational status of the environment:

          * ``Launching`` : Environment is in the process of initial deployment.

          * ``Updating`` : Environment is in the process of updating its configuration settings or
          application version.

          * ``Ready`` : Environment is available to have an action performed on it, such as update
          or terminate.

          * ``Terminating`` : Environment is in the shut-down process.

          * ``Terminated`` : Environment is not running.

        - **AbortableOperationInProgress** *(boolean) --*

          Indicates if there is an in-progress environment configuration update or application
          version deployment that you can cancel.

           ``true:`` There is an update in progress.

           ``false:`` There are no updates currently in progress.

        - **Health** *(string) --*

          Describes the health status of the environment. AWS Elastic Beanstalk indicates the
          failure levels for a running environment:

          * ``Red`` : Indicates the environment is not responsive. Occurs when three or more
          consecutive failures occur for an environment.

          * ``Yellow`` : Indicates that something is wrong. Occurs when two consecutive failures
          occur for an environment.

          * ``Green`` : Indicates the environment is healthy and fully functional.

          * ``Grey`` : Default health for a new environment. The environment is not fully launched
          and health checks have not started or health checks are suspended during an
          ``UpdateEnvironment`` or ``RestartEnvironment`` request.

          Default: ``Grey``

        - **HealthStatus** *(string) --*

          Returns the health status of the application running in your environment. For more
          information, see `Health Colors and Statuses
          <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

        - **Resources** *(dict) --*

          The description of the AWS resources used by this environment.

          - **LoadBalancer** *(dict) --*

            Describes the LoadBalancer.

            - **LoadBalancerName** *(string) --*

              The name of the LoadBalancer.

            - **Domain** *(string) --*

              The domain name of the LoadBalancer.

            - **Listeners** *(list) --*

              A list of Listeners used by the LoadBalancer.

              - *(dict) --*

                Describes the properties of a Listener for the LoadBalancer.

                - **Protocol** *(string) --*

                  The protocol that is used by the Listener.

                - **Port** *(integer) --*

                  The port that is used by the Listener.

        - **Tier** *(dict) --*

          Describes the current tier of this environment.

          - **Name** *(string) --*

            The name of this environment tier.

            Valid values:

            * For *Web server tier* – ``WebServer``

            * For *Worker tier* – ``Worker``

          - **Type** *(string) --*

            The type of this environment tier.

            Valid values:

            * For *Web server tier* – ``Standard``

            * For *Worker tier* – ``SQS/HTTP``

          - **Version** *(string) --*

            The version of this environment tier. When you don't set a value to it, Elastic
            Beanstalk uses the latest compatible worker tier version.

            .. note::

              This member is deprecated. Any specific version that you set may become out of date.
              We recommend leaving it unspecified.

        - **EnvironmentLinks** *(list) --*

          A list of links to other environments in the same group.

          - *(dict) --*

            A link to another environment, defined in the environment's manifest. Links provide
            connection information in system properties that can be used to connect to another
            environment in the same group. See `Environment Manifest (env.yaml)
            <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__
            for details.

            - **LinkName** *(string) --*

              The name of the link.

            - **EnvironmentName** *(string) --*

              The name of the linked environment (the dependency).

        - **EnvironmentArn** *(string) --*

          The environment's Amazon Resource Name (ARN), which can be used in other API requests
          that require an ARN.

    - **NextToken** *(string) --*

      In a paginated request, the token that you can pass in a subsequent request to get the next
      response page.
    """


_ClientDescribeEventsResponseEventsTypeDef = TypedDict(
    "_ClientDescribeEventsResponseEventsTypeDef",
    {
        "EventDate": datetime,
        "Message": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "TemplateName": str,
        "EnvironmentName": str,
        "PlatformArn": str,
        "RequestId": str,
        "Severity": str,
    },
    total=False,
)


class ClientDescribeEventsResponseEventsTypeDef(
    _ClientDescribeEventsResponseEventsTypeDef
):
    """
    Type definition for `ClientDescribeEventsResponse` `Events`

    Describes an event.

    - **EventDate** *(datetime) --*

      The date when the event occurred.

    - **Message** *(string) --*

      The event message.

    - **ApplicationName** *(string) --*

      The application associated with the event.

    - **VersionLabel** *(string) --*

      The release label for the application version associated with this event.

    - **TemplateName** *(string) --*

      The name of the configuration associated with this event.

    - **EnvironmentName** *(string) --*

      The name of the environment associated with this event.

    - **PlatformArn** *(string) --*

      The ARN of the platform.

    - **RequestId** *(string) --*

      The web service request ID for the activity of this event.

    - **Severity** *(string) --*

      The severity level of this event.
    """


_ClientDescribeEventsResponseTypeDef = TypedDict(
    "_ClientDescribeEventsResponseTypeDef",
    {"Events": List[ClientDescribeEventsResponseEventsTypeDef], "NextToken": str},
    total=False,
)


class ClientDescribeEventsResponseTypeDef(_ClientDescribeEventsResponseTypeDef):
    """
    Type definition for `ClientDescribeEvents` `Response`

    Result message wrapping a list of event descriptions.

    - **Events** *(list) --*

      A list of  EventDescription .

      - *(dict) --*

        Describes an event.

        - **EventDate** *(datetime) --*

          The date when the event occurred.

        - **Message** *(string) --*

          The event message.

        - **ApplicationName** *(string) --*

          The application associated with the event.

        - **VersionLabel** *(string) --*

          The release label for the application version associated with this event.

        - **TemplateName** *(string) --*

          The name of the configuration associated with this event.

        - **EnvironmentName** *(string) --*

          The name of the environment associated with this event.

        - **PlatformArn** *(string) --*

          The ARN of the platform.

        - **RequestId** *(string) --*

          The web service request ID for the activity of this event.

        - **Severity** *(string) --*

          The severity level of this event.

    - **NextToken** *(string) --*

      If returned, this indicates that there are more results to obtain. Use this token in the next
       DescribeEvents call to get the next batch of events.
    """


_ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsLatencyTypeDef = TypedDict(
    "_ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsLatencyTypeDef",
    {
        "P999": float,
        "P99": float,
        "P95": float,
        "P90": float,
        "P85": float,
        "P75": float,
        "P50": float,
        "P10": float,
    },
    total=False,
)


class ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsLatencyTypeDef(
    _ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsLatencyTypeDef
):
    """
    Type definition for `ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetrics` `Latency`

    Represents the average latency for the slowest X percent of requests over the last 10
    seconds. Latencies are in seconds with one millisecond resolution.

    - **P999** *(float) --*

      The average latency for the slowest 0.1 percent of requests over the last 10 seconds.

    - **P99** *(float) --*

      The average latency for the slowest 1 percent of requests over the last 10 seconds.

    - **P95** *(float) --*

      The average latency for the slowest 5 percent of requests over the last 10 seconds.

    - **P90** *(float) --*

      The average latency for the slowest 10 percent of requests over the last 10 seconds.

    - **P85** *(float) --*

      The average latency for the slowest 15 percent of requests over the last 10 seconds.

    - **P75** *(float) --*

      The average latency for the slowest 25 percent of requests over the last 10 seconds.

    - **P50** *(float) --*

      The average latency for the slowest 50 percent of requests over the last 10 seconds.

    - **P10** *(float) --*

      The average latency for the slowest 90 percent of requests over the last 10 seconds.
    """


_ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsStatusCodesTypeDef = TypedDict(
    "_ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsStatusCodesTypeDef",
    {"Status2xx": int, "Status3xx": int, "Status4xx": int, "Status5xx": int},
    total=False,
)


class ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsStatusCodesTypeDef(
    _ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsStatusCodesTypeDef
):
    """
    Type definition for `ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetrics` `StatusCodes`

    Represents the percentage of requests over the last 10 seconds that resulted in each
    type of status code response.

    - **Status2xx** *(integer) --*

      The percentage of requests over the last 10 seconds that resulted in a 2xx (200, 201,
      etc.) status code.

    - **Status3xx** *(integer) --*

      The percentage of requests over the last 10 seconds that resulted in a 3xx (300, 301,
      etc.) status code.

    - **Status4xx** *(integer) --*

      The percentage of requests over the last 10 seconds that resulted in a 4xx (400, 401,
      etc.) status code.

    - **Status5xx** *(integer) --*

      The percentage of requests over the last 10 seconds that resulted in a 5xx (500, 501,
      etc.) status code.
    """


_ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsTypeDef = TypedDict(
    "_ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsTypeDef",
    {
        "Duration": int,
        "RequestCount": int,
        "StatusCodes": ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsStatusCodesTypeDef,
        "Latency": ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsLatencyTypeDef,
    },
    total=False,
)


class ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsTypeDef(
    _ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsTypeDef
):
    """
    Type definition for `ClientDescribeInstancesHealthResponseInstanceHealthList` `ApplicationMetrics`

    Request metrics from your application.

    - **Duration** *(integer) --*

      The amount of time that the metrics cover (usually 10 seconds). For example, you might
      have 5 requests (``request_count`` ) within the most recent time slice of 10 seconds
      (``duration`` ).

    - **RequestCount** *(integer) --*

      Average number of requests handled by the web server per second over the last 10
      seconds.

    - **StatusCodes** *(dict) --*

      Represents the percentage of requests over the last 10 seconds that resulted in each
      type of status code response.

      - **Status2xx** *(integer) --*

        The percentage of requests over the last 10 seconds that resulted in a 2xx (200, 201,
        etc.) status code.

      - **Status3xx** *(integer) --*

        The percentage of requests over the last 10 seconds that resulted in a 3xx (300, 301,
        etc.) status code.

      - **Status4xx** *(integer) --*

        The percentage of requests over the last 10 seconds that resulted in a 4xx (400, 401,
        etc.) status code.

      - **Status5xx** *(integer) --*

        The percentage of requests over the last 10 seconds that resulted in a 5xx (500, 501,
        etc.) status code.

    - **Latency** *(dict) --*

      Represents the average latency for the slowest X percent of requests over the last 10
      seconds. Latencies are in seconds with one millisecond resolution.

      - **P999** *(float) --*

        The average latency for the slowest 0.1 percent of requests over the last 10 seconds.

      - **P99** *(float) --*

        The average latency for the slowest 1 percent of requests over the last 10 seconds.

      - **P95** *(float) --*

        The average latency for the slowest 5 percent of requests over the last 10 seconds.

      - **P90** *(float) --*

        The average latency for the slowest 10 percent of requests over the last 10 seconds.

      - **P85** *(float) --*

        The average latency for the slowest 15 percent of requests over the last 10 seconds.

      - **P75** *(float) --*

        The average latency for the slowest 25 percent of requests over the last 10 seconds.

      - **P50** *(float) --*

        The average latency for the slowest 50 percent of requests over the last 10 seconds.

      - **P10** *(float) --*

        The average latency for the slowest 90 percent of requests over the last 10 seconds.
    """


_ClientDescribeInstancesHealthResponseInstanceHealthListDeploymentTypeDef = TypedDict(
    "_ClientDescribeInstancesHealthResponseInstanceHealthListDeploymentTypeDef",
    {
        "VersionLabel": str,
        "DeploymentId": int,
        "Status": str,
        "DeploymentTime": datetime,
    },
    total=False,
)


class ClientDescribeInstancesHealthResponseInstanceHealthListDeploymentTypeDef(
    _ClientDescribeInstancesHealthResponseInstanceHealthListDeploymentTypeDef
):
    """
    Type definition for `ClientDescribeInstancesHealthResponseInstanceHealthList` `Deployment`

    Information about the most recent deployment to an instance.

    - **VersionLabel** *(string) --*

      The version label of the application version in the deployment.

    - **DeploymentId** *(integer) --*

      The ID of the deployment. This number increases by one each time that you deploy source
      code or change instance configuration settings.

    - **Status** *(string) --*

      The status of the deployment:

      * ``In Progress`` : The deployment is in progress.

      * ``Deployed`` : The deployment succeeded.

      * ``Failed`` : The deployment failed.

    - **DeploymentTime** *(datetime) --*

      For in-progress deployments, the time that the deployment started.

      For completed deployments, the time that the deployment ended.
    """


_ClientDescribeInstancesHealthResponseInstanceHealthListSystemCPUUtilizationTypeDef = TypedDict(
    "_ClientDescribeInstancesHealthResponseInstanceHealthListSystemCPUUtilizationTypeDef",
    {
        "User": float,
        "Nice": float,
        "System": float,
        "Idle": float,
        "IOWait": float,
        "IRQ": float,
        "SoftIRQ": float,
        "Privileged": float,
    },
    total=False,
)


class ClientDescribeInstancesHealthResponseInstanceHealthListSystemCPUUtilizationTypeDef(
    _ClientDescribeInstancesHealthResponseInstanceHealthListSystemCPUUtilizationTypeDef
):
    """
    Type definition for `ClientDescribeInstancesHealthResponseInstanceHealthListSystem` `CPUUtilization`

    CPU utilization metrics for the instance.

    - **User** *(float) --*

      Percentage of time that the CPU has spent in the ``User`` state over the last 10
      seconds.

    - **Nice** *(float) --*

      Available on Linux environments only.

      Percentage of time that the CPU has spent in the ``Nice`` state over the last 10
      seconds.

    - **System** *(float) --*

      Available on Linux environments only.

      Percentage of time that the CPU has spent in the ``System`` state over the last 10
      seconds.

    - **Idle** *(float) --*

      Percentage of time that the CPU has spent in the ``Idle`` state over the last 10
      seconds.

    - **IOWait** *(float) --*

      Available on Linux environments only.

      Percentage of time that the CPU has spent in the ``I/O Wait`` state over the last 10
      seconds.

    - **IRQ** *(float) --*

      Available on Linux environments only.

      Percentage of time that the CPU has spent in the ``IRQ`` state over the last 10
      seconds.

    - **SoftIRQ** *(float) --*

      Available on Linux environments only.

      Percentage of time that the CPU has spent in the ``SoftIRQ`` state over the last 10
      seconds.

    - **Privileged** *(float) --*

      Available on Windows environments only.

      Percentage of time that the CPU has spent in the ``Privileged`` state over the last
      10 seconds.
    """


_ClientDescribeInstancesHealthResponseInstanceHealthListSystemTypeDef = TypedDict(
    "_ClientDescribeInstancesHealthResponseInstanceHealthListSystemTypeDef",
    {
        "CPUUtilization": ClientDescribeInstancesHealthResponseInstanceHealthListSystemCPUUtilizationTypeDef,
        "LoadAverage": List[float],
    },
    total=False,
)


class ClientDescribeInstancesHealthResponseInstanceHealthListSystemTypeDef(
    _ClientDescribeInstancesHealthResponseInstanceHealthListSystemTypeDef
):
    """
    Type definition for `ClientDescribeInstancesHealthResponseInstanceHealthList` `System`

    Operating system metrics from the instance.

    - **CPUUtilization** *(dict) --*

      CPU utilization metrics for the instance.

      - **User** *(float) --*

        Percentage of time that the CPU has spent in the ``User`` state over the last 10
        seconds.

      - **Nice** *(float) --*

        Available on Linux environments only.

        Percentage of time that the CPU has spent in the ``Nice`` state over the last 10
        seconds.

      - **System** *(float) --*

        Available on Linux environments only.

        Percentage of time that the CPU has spent in the ``System`` state over the last 10
        seconds.

      - **Idle** *(float) --*

        Percentage of time that the CPU has spent in the ``Idle`` state over the last 10
        seconds.

      - **IOWait** *(float) --*

        Available on Linux environments only.

        Percentage of time that the CPU has spent in the ``I/O Wait`` state over the last 10
        seconds.

      - **IRQ** *(float) --*

        Available on Linux environments only.

        Percentage of time that the CPU has spent in the ``IRQ`` state over the last 10
        seconds.

      - **SoftIRQ** *(float) --*

        Available on Linux environments only.

        Percentage of time that the CPU has spent in the ``SoftIRQ`` state over the last 10
        seconds.

      - **Privileged** *(float) --*

        Available on Windows environments only.

        Percentage of time that the CPU has spent in the ``Privileged`` state over the last
        10 seconds.

    - **LoadAverage** *(list) --*

      Load average in the last 1-minute, 5-minute, and 15-minute periods. For more
      information, see `Operating System Metrics
      <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-metrics.html#health-enhanced-metrics-os>`__
      .

      - *(float) --*
    """


_ClientDescribeInstancesHealthResponseInstanceHealthListTypeDef = TypedDict(
    "_ClientDescribeInstancesHealthResponseInstanceHealthListTypeDef",
    {
        "InstanceId": str,
        "HealthStatus": str,
        "Color": str,
        "Causes": List[str],
        "LaunchedAt": datetime,
        "ApplicationMetrics": ClientDescribeInstancesHealthResponseInstanceHealthListApplicationMetricsTypeDef,
        "System": ClientDescribeInstancesHealthResponseInstanceHealthListSystemTypeDef,
        "Deployment": ClientDescribeInstancesHealthResponseInstanceHealthListDeploymentTypeDef,
        "AvailabilityZone": str,
        "InstanceType": str,
    },
    total=False,
)


class ClientDescribeInstancesHealthResponseInstanceHealthListTypeDef(
    _ClientDescribeInstancesHealthResponseInstanceHealthListTypeDef
):
    """
    Type definition for `ClientDescribeInstancesHealthResponse` `InstanceHealthList`

    Detailed health information about an Amazon EC2 instance in your Elastic Beanstalk
    environment.

    - **InstanceId** *(string) --*

      The ID of the Amazon EC2 instance.

    - **HealthStatus** *(string) --*

      Returns the health status of the specified instance. For more information, see `Health
      Colors and Statuses
      <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

    - **Color** *(string) --*

      Represents the color indicator that gives you information about the health of the EC2
      instance. For more information, see `Health Colors and Statuses
      <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

    - **Causes** *(list) --*

      Represents the causes, which provide more information about the current health status.

      - *(string) --*

    - **LaunchedAt** *(datetime) --*

      The time at which the EC2 instance was launched.

    - **ApplicationMetrics** *(dict) --*

      Request metrics from your application.

      - **Duration** *(integer) --*

        The amount of time that the metrics cover (usually 10 seconds). For example, you might
        have 5 requests (``request_count`` ) within the most recent time slice of 10 seconds
        (``duration`` ).

      - **RequestCount** *(integer) --*

        Average number of requests handled by the web server per second over the last 10
        seconds.

      - **StatusCodes** *(dict) --*

        Represents the percentage of requests over the last 10 seconds that resulted in each
        type of status code response.

        - **Status2xx** *(integer) --*

          The percentage of requests over the last 10 seconds that resulted in a 2xx (200, 201,
          etc.) status code.

        - **Status3xx** *(integer) --*

          The percentage of requests over the last 10 seconds that resulted in a 3xx (300, 301,
          etc.) status code.

        - **Status4xx** *(integer) --*

          The percentage of requests over the last 10 seconds that resulted in a 4xx (400, 401,
          etc.) status code.

        - **Status5xx** *(integer) --*

          The percentage of requests over the last 10 seconds that resulted in a 5xx (500, 501,
          etc.) status code.

      - **Latency** *(dict) --*

        Represents the average latency for the slowest X percent of requests over the last 10
        seconds. Latencies are in seconds with one millisecond resolution.

        - **P999** *(float) --*

          The average latency for the slowest 0.1 percent of requests over the last 10 seconds.

        - **P99** *(float) --*

          The average latency for the slowest 1 percent of requests over the last 10 seconds.

        - **P95** *(float) --*

          The average latency for the slowest 5 percent of requests over the last 10 seconds.

        - **P90** *(float) --*

          The average latency for the slowest 10 percent of requests over the last 10 seconds.

        - **P85** *(float) --*

          The average latency for the slowest 15 percent of requests over the last 10 seconds.

        - **P75** *(float) --*

          The average latency for the slowest 25 percent of requests over the last 10 seconds.

        - **P50** *(float) --*

          The average latency for the slowest 50 percent of requests over the last 10 seconds.

        - **P10** *(float) --*

          The average latency for the slowest 90 percent of requests over the last 10 seconds.

    - **System** *(dict) --*

      Operating system metrics from the instance.

      - **CPUUtilization** *(dict) --*

        CPU utilization metrics for the instance.

        - **User** *(float) --*

          Percentage of time that the CPU has spent in the ``User`` state over the last 10
          seconds.

        - **Nice** *(float) --*

          Available on Linux environments only.

          Percentage of time that the CPU has spent in the ``Nice`` state over the last 10
          seconds.

        - **System** *(float) --*

          Available on Linux environments only.

          Percentage of time that the CPU has spent in the ``System`` state over the last 10
          seconds.

        - **Idle** *(float) --*

          Percentage of time that the CPU has spent in the ``Idle`` state over the last 10
          seconds.

        - **IOWait** *(float) --*

          Available on Linux environments only.

          Percentage of time that the CPU has spent in the ``I/O Wait`` state over the last 10
          seconds.

        - **IRQ** *(float) --*

          Available on Linux environments only.

          Percentage of time that the CPU has spent in the ``IRQ`` state over the last 10
          seconds.

        - **SoftIRQ** *(float) --*

          Available on Linux environments only.

          Percentage of time that the CPU has spent in the ``SoftIRQ`` state over the last 10
          seconds.

        - **Privileged** *(float) --*

          Available on Windows environments only.

          Percentage of time that the CPU has spent in the ``Privileged`` state over the last
          10 seconds.

      - **LoadAverage** *(list) --*

        Load average in the last 1-minute, 5-minute, and 15-minute periods. For more
        information, see `Operating System Metrics
        <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-metrics.html#health-enhanced-metrics-os>`__
        .

        - *(float) --*

    - **Deployment** *(dict) --*

      Information about the most recent deployment to an instance.

      - **VersionLabel** *(string) --*

        The version label of the application version in the deployment.

      - **DeploymentId** *(integer) --*

        The ID of the deployment. This number increases by one each time that you deploy source
        code or change instance configuration settings.

      - **Status** *(string) --*

        The status of the deployment:

        * ``In Progress`` : The deployment is in progress.

        * ``Deployed`` : The deployment succeeded.

        * ``Failed`` : The deployment failed.

      - **DeploymentTime** *(datetime) --*

        For in-progress deployments, the time that the deployment started.

        For completed deployments, the time that the deployment ended.

    - **AvailabilityZone** *(string) --*

      The availability zone in which the instance runs.

    - **InstanceType** *(string) --*

      The instance's type.
    """


_ClientDescribeInstancesHealthResponseTypeDef = TypedDict(
    "_ClientDescribeInstancesHealthResponseTypeDef",
    {
        "InstanceHealthList": List[
            ClientDescribeInstancesHealthResponseInstanceHealthListTypeDef
        ],
        "RefreshedAt": datetime,
        "NextToken": str,
    },
    total=False,
)


class ClientDescribeInstancesHealthResponseTypeDef(
    _ClientDescribeInstancesHealthResponseTypeDef
):
    """
    Type definition for `ClientDescribeInstancesHealth` `Response`

    Detailed health information about the Amazon EC2 instances in an AWS Elastic Beanstalk
    environment.

    - **InstanceHealthList** *(list) --*

      Detailed health information about each instance.

      The output differs slightly between Linux and Windows environments. There is a difference in
      the members that are supported under the ``<CPUUtilization>`` type.

      - *(dict) --*

        Detailed health information about an Amazon EC2 instance in your Elastic Beanstalk
        environment.

        - **InstanceId** *(string) --*

          The ID of the Amazon EC2 instance.

        - **HealthStatus** *(string) --*

          Returns the health status of the specified instance. For more information, see `Health
          Colors and Statuses
          <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

        - **Color** *(string) --*

          Represents the color indicator that gives you information about the health of the EC2
          instance. For more information, see `Health Colors and Statuses
          <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

        - **Causes** *(list) --*

          Represents the causes, which provide more information about the current health status.

          - *(string) --*

        - **LaunchedAt** *(datetime) --*

          The time at which the EC2 instance was launched.

        - **ApplicationMetrics** *(dict) --*

          Request metrics from your application.

          - **Duration** *(integer) --*

            The amount of time that the metrics cover (usually 10 seconds). For example, you might
            have 5 requests (``request_count`` ) within the most recent time slice of 10 seconds
            (``duration`` ).

          - **RequestCount** *(integer) --*

            Average number of requests handled by the web server per second over the last 10
            seconds.

          - **StatusCodes** *(dict) --*

            Represents the percentage of requests over the last 10 seconds that resulted in each
            type of status code response.

            - **Status2xx** *(integer) --*

              The percentage of requests over the last 10 seconds that resulted in a 2xx (200, 201,
              etc.) status code.

            - **Status3xx** *(integer) --*

              The percentage of requests over the last 10 seconds that resulted in a 3xx (300, 301,
              etc.) status code.

            - **Status4xx** *(integer) --*

              The percentage of requests over the last 10 seconds that resulted in a 4xx (400, 401,
              etc.) status code.

            - **Status5xx** *(integer) --*

              The percentage of requests over the last 10 seconds that resulted in a 5xx (500, 501,
              etc.) status code.

          - **Latency** *(dict) --*

            Represents the average latency for the slowest X percent of requests over the last 10
            seconds. Latencies are in seconds with one millisecond resolution.

            - **P999** *(float) --*

              The average latency for the slowest 0.1 percent of requests over the last 10 seconds.

            - **P99** *(float) --*

              The average latency for the slowest 1 percent of requests over the last 10 seconds.

            - **P95** *(float) --*

              The average latency for the slowest 5 percent of requests over the last 10 seconds.

            - **P90** *(float) --*

              The average latency for the slowest 10 percent of requests over the last 10 seconds.

            - **P85** *(float) --*

              The average latency for the slowest 15 percent of requests over the last 10 seconds.

            - **P75** *(float) --*

              The average latency for the slowest 25 percent of requests over the last 10 seconds.

            - **P50** *(float) --*

              The average latency for the slowest 50 percent of requests over the last 10 seconds.

            - **P10** *(float) --*

              The average latency for the slowest 90 percent of requests over the last 10 seconds.

        - **System** *(dict) --*

          Operating system metrics from the instance.

          - **CPUUtilization** *(dict) --*

            CPU utilization metrics for the instance.

            - **User** *(float) --*

              Percentage of time that the CPU has spent in the ``User`` state over the last 10
              seconds.

            - **Nice** *(float) --*

              Available on Linux environments only.

              Percentage of time that the CPU has spent in the ``Nice`` state over the last 10
              seconds.

            - **System** *(float) --*

              Available on Linux environments only.

              Percentage of time that the CPU has spent in the ``System`` state over the last 10
              seconds.

            - **Idle** *(float) --*

              Percentage of time that the CPU has spent in the ``Idle`` state over the last 10
              seconds.

            - **IOWait** *(float) --*

              Available on Linux environments only.

              Percentage of time that the CPU has spent in the ``I/O Wait`` state over the last 10
              seconds.

            - **IRQ** *(float) --*

              Available on Linux environments only.

              Percentage of time that the CPU has spent in the ``IRQ`` state over the last 10
              seconds.

            - **SoftIRQ** *(float) --*

              Available on Linux environments only.

              Percentage of time that the CPU has spent in the ``SoftIRQ`` state over the last 10
              seconds.

            - **Privileged** *(float) --*

              Available on Windows environments only.

              Percentage of time that the CPU has spent in the ``Privileged`` state over the last
              10 seconds.

          - **LoadAverage** *(list) --*

            Load average in the last 1-minute, 5-minute, and 15-minute periods. For more
            information, see `Operating System Metrics
            <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-metrics.html#health-enhanced-metrics-os>`__
            .

            - *(float) --*

        - **Deployment** *(dict) --*

          Information about the most recent deployment to an instance.

          - **VersionLabel** *(string) --*

            The version label of the application version in the deployment.

          - **DeploymentId** *(integer) --*

            The ID of the deployment. This number increases by one each time that you deploy source
            code or change instance configuration settings.

          - **Status** *(string) --*

            The status of the deployment:

            * ``In Progress`` : The deployment is in progress.

            * ``Deployed`` : The deployment succeeded.

            * ``Failed`` : The deployment failed.

          - **DeploymentTime** *(datetime) --*

            For in-progress deployments, the time that the deployment started.

            For completed deployments, the time that the deployment ended.

        - **AvailabilityZone** *(string) --*

          The availability zone in which the instance runs.

        - **InstanceType** *(string) --*

          The instance's type.

    - **RefreshedAt** *(datetime) --*

      The date and time that the health information was retrieved.

    - **NextToken** *(string) --*

      Pagination token for the next page of results, if available.
    """


_ClientDescribePlatformVersionResponsePlatformDescriptionCustomAmiListTypeDef = TypedDict(
    "_ClientDescribePlatformVersionResponsePlatformDescriptionCustomAmiListTypeDef",
    {"VirtualizationType": str, "ImageId": str},
    total=False,
)


class ClientDescribePlatformVersionResponsePlatformDescriptionCustomAmiListTypeDef(
    _ClientDescribePlatformVersionResponsePlatformDescriptionCustomAmiListTypeDef
):
    """
    Type definition for `ClientDescribePlatformVersionResponsePlatformDescription` `CustomAmiList`

    A custom AMI available to platforms.

    - **VirtualizationType** *(string) --*

      The type of virtualization used to create the custom AMI.

    - **ImageId** *(string) --*

      THe ID of the image used to create the custom AMI.
    """


_ClientDescribePlatformVersionResponsePlatformDescriptionFrameworksTypeDef = TypedDict(
    "_ClientDescribePlatformVersionResponsePlatformDescriptionFrameworksTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientDescribePlatformVersionResponsePlatformDescriptionFrameworksTypeDef(
    _ClientDescribePlatformVersionResponsePlatformDescriptionFrameworksTypeDef
):
    """
    Type definition for `ClientDescribePlatformVersionResponsePlatformDescription` `Frameworks`

    A framework supported by the custom platform.

    - **Name** *(string) --*

      The name of the framework.

    - **Version** *(string) --*

      The version of the framework.
    """


_ClientDescribePlatformVersionResponsePlatformDescriptionProgrammingLanguagesTypeDef = TypedDict(
    "_ClientDescribePlatformVersionResponsePlatformDescriptionProgrammingLanguagesTypeDef",
    {"Name": str, "Version": str},
    total=False,
)


class ClientDescribePlatformVersionResponsePlatformDescriptionProgrammingLanguagesTypeDef(
    _ClientDescribePlatformVersionResponsePlatformDescriptionProgrammingLanguagesTypeDef
):
    """
    Type definition for `ClientDescribePlatformVersionResponsePlatformDescription` `ProgrammingLanguages`

    A programming language supported by the platform.

    - **Name** *(string) --*

      The name of the programming language.

    - **Version** *(string) --*

      The version of the programming language.
    """


_ClientDescribePlatformVersionResponsePlatformDescriptionTypeDef = TypedDict(
    "_ClientDescribePlatformVersionResponsePlatformDescriptionTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformName": str,
        "PlatformVersion": str,
        "SolutionStackName": str,
        "PlatformStatus": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "PlatformCategory": str,
        "Description": str,
        "Maintainer": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "ProgrammingLanguages": List[
            ClientDescribePlatformVersionResponsePlatformDescriptionProgrammingLanguagesTypeDef
        ],
        "Frameworks": List[
            ClientDescribePlatformVersionResponsePlatformDescriptionFrameworksTypeDef
        ],
        "CustomAmiList": List[
            ClientDescribePlatformVersionResponsePlatformDescriptionCustomAmiListTypeDef
        ],
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
    },
    total=False,
)


class ClientDescribePlatformVersionResponsePlatformDescriptionTypeDef(
    _ClientDescribePlatformVersionResponsePlatformDescriptionTypeDef
):
    """
    Type definition for `ClientDescribePlatformVersionResponse` `PlatformDescription`

    Detailed information about the version of the platform.

    - **PlatformArn** *(string) --*

      The ARN of the platform.

    - **PlatformOwner** *(string) --*

      The AWS account ID of the person who created the platform.

    - **PlatformName** *(string) --*

      The name of the platform.

    - **PlatformVersion** *(string) --*

      The version of the platform.

    - **SolutionStackName** *(string) --*

      The name of the solution stack used by the platform.

    - **PlatformStatus** *(string) --*

      The status of the platform.

    - **DateCreated** *(datetime) --*

      The date when the platform was created.

    - **DateUpdated** *(datetime) --*

      The date when the platform was last updated.

    - **PlatformCategory** *(string) --*

      The category of the platform.

    - **Description** *(string) --*

      The description of the platform.

    - **Maintainer** *(string) --*

      Information about the maintainer of the platform.

    - **OperatingSystemName** *(string) --*

      The operating system used by the platform.

    - **OperatingSystemVersion** *(string) --*

      The version of the operating system used by the platform.

    - **ProgrammingLanguages** *(list) --*

      The programming languages supported by the platform.

      - *(dict) --*

        A programming language supported by the platform.

        - **Name** *(string) --*

          The name of the programming language.

        - **Version** *(string) --*

          The version of the programming language.

    - **Frameworks** *(list) --*

      The frameworks supported by the platform.

      - *(dict) --*

        A framework supported by the custom platform.

        - **Name** *(string) --*

          The name of the framework.

        - **Version** *(string) --*

          The version of the framework.

    - **CustomAmiList** *(list) --*

      The custom AMIs supported by the platform.

      - *(dict) --*

        A custom AMI available to platforms.

        - **VirtualizationType** *(string) --*

          The type of virtualization used to create the custom AMI.

        - **ImageId** *(string) --*

          THe ID of the image used to create the custom AMI.

    - **SupportedTierList** *(list) --*

      The tiers supported by the platform.

      - *(string) --*

    - **SupportedAddonList** *(list) --*

      The additions supported by the platform.

      - *(string) --*
    """


_ClientDescribePlatformVersionResponseTypeDef = TypedDict(
    "_ClientDescribePlatformVersionResponseTypeDef",
    {
        "PlatformDescription": ClientDescribePlatformVersionResponsePlatformDescriptionTypeDef
    },
    total=False,
)


class ClientDescribePlatformVersionResponseTypeDef(
    _ClientDescribePlatformVersionResponseTypeDef
):
    """
    Type definition for `ClientDescribePlatformVersion` `Response`

    - **PlatformDescription** *(dict) --*

      Detailed information about the version of the platform.

      - **PlatformArn** *(string) --*

        The ARN of the platform.

      - **PlatformOwner** *(string) --*

        The AWS account ID of the person who created the platform.

      - **PlatformName** *(string) --*

        The name of the platform.

      - **PlatformVersion** *(string) --*

        The version of the platform.

      - **SolutionStackName** *(string) --*

        The name of the solution stack used by the platform.

      - **PlatformStatus** *(string) --*

        The status of the platform.

      - **DateCreated** *(datetime) --*

        The date when the platform was created.

      - **DateUpdated** *(datetime) --*

        The date when the platform was last updated.

      - **PlatformCategory** *(string) --*

        The category of the platform.

      - **Description** *(string) --*

        The description of the platform.

      - **Maintainer** *(string) --*

        Information about the maintainer of the platform.

      - **OperatingSystemName** *(string) --*

        The operating system used by the platform.

      - **OperatingSystemVersion** *(string) --*

        The version of the operating system used by the platform.

      - **ProgrammingLanguages** *(list) --*

        The programming languages supported by the platform.

        - *(dict) --*

          A programming language supported by the platform.

          - **Name** *(string) --*

            The name of the programming language.

          - **Version** *(string) --*

            The version of the programming language.

      - **Frameworks** *(list) --*

        The frameworks supported by the platform.

        - *(dict) --*

          A framework supported by the custom platform.

          - **Name** *(string) --*

            The name of the framework.

          - **Version** *(string) --*

            The version of the framework.

      - **CustomAmiList** *(list) --*

        The custom AMIs supported by the platform.

        - *(dict) --*

          A custom AMI available to platforms.

          - **VirtualizationType** *(string) --*

            The type of virtualization used to create the custom AMI.

          - **ImageId** *(string) --*

            THe ID of the image used to create the custom AMI.

      - **SupportedTierList** *(list) --*

        The tiers supported by the platform.

        - *(string) --*

      - **SupportedAddonList** *(list) --*

        The additions supported by the platform.

        - *(string) --*
    """


_ClientListAvailableSolutionStacksResponseSolutionStackDetailsTypeDef = TypedDict(
    "_ClientListAvailableSolutionStacksResponseSolutionStackDetailsTypeDef",
    {"SolutionStackName": str, "PermittedFileTypes": List[str]},
    total=False,
)


class ClientListAvailableSolutionStacksResponseSolutionStackDetailsTypeDef(
    _ClientListAvailableSolutionStacksResponseSolutionStackDetailsTypeDef
):
    """
    Type definition for `ClientListAvailableSolutionStacksResponse` `SolutionStackDetails`

    Describes the solution stack.

    - **SolutionStackName** *(string) --*

      The name of the solution stack.

    - **PermittedFileTypes** *(list) --*

      The permitted file types allowed for a solution stack.

      - *(string) --*
    """


_ClientListAvailableSolutionStacksResponseTypeDef = TypedDict(
    "_ClientListAvailableSolutionStacksResponseTypeDef",
    {
        "SolutionStacks": List[str],
        "SolutionStackDetails": List[
            ClientListAvailableSolutionStacksResponseSolutionStackDetailsTypeDef
        ],
    },
    total=False,
)


class ClientListAvailableSolutionStacksResponseTypeDef(
    _ClientListAvailableSolutionStacksResponseTypeDef
):
    """
    Type definition for `ClientListAvailableSolutionStacks` `Response`

    A list of available AWS Elastic Beanstalk solution stacks.

    - **SolutionStacks** *(list) --*

      A list of available solution stacks.

      - *(string) --*

    - **SolutionStackDetails** *(list) --*

      A list of available solution stacks and their  SolutionStackDescription .

      - *(dict) --*

        Describes the solution stack.

        - **SolutionStackName** *(string) --*

          The name of the solution stack.

        - **PermittedFileTypes** *(list) --*

          The permitted file types allowed for a solution stack.

          - *(string) --*
    """


_ClientListPlatformVersionsFiltersTypeDef = TypedDict(
    "_ClientListPlatformVersionsFiltersTypeDef",
    {"Type": str, "Operator": str, "Values": List[str]},
    total=False,
)


class ClientListPlatformVersionsFiltersTypeDef(
    _ClientListPlatformVersionsFiltersTypeDef
):
    """
    Type definition for `ClientListPlatformVersions` `Filters`

    Specify criteria to restrict the results when listing custom platforms.

    The filter is evaluated as the expression:

     ``Type``  ``Operator``  ``Values[i]``

    - **Type** *(string) --*

      The custom platform attribute to which the filter values are applied.

      Valid Values: ``PlatformName`` | ``PlatformVersion`` | ``PlatformStatus`` | ``PlatformOwner``

    - **Operator** *(string) --*

      The operator to apply to the ``Type`` with each of the ``Values`` .

      Valid Values: ``=`` (equal to) | ``!=`` (not equal to) | ``<`` (less than) | ``<=`` (less
      than or equal to) | ``>`` (greater than) | ``>=`` (greater than or equal to) | ``contains`` |
      ``begins_with`` | ``ends_with``

    - **Values** *(list) --*

      The list of values applied to the custom platform attribute.

      - *(string) --*
    """


_ClientListPlatformVersionsResponsePlatformSummaryListTypeDef = TypedDict(
    "_ClientListPlatformVersionsResponsePlatformSummaryListTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformStatus": str,
        "PlatformCategory": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
    },
    total=False,
)


class ClientListPlatformVersionsResponsePlatformSummaryListTypeDef(
    _ClientListPlatformVersionsResponsePlatformSummaryListTypeDef
):
    """
    Type definition for `ClientListPlatformVersionsResponse` `PlatformSummaryList`

    Detailed information about a platform.

    - **PlatformArn** *(string) --*

      The ARN of the platform.

    - **PlatformOwner** *(string) --*

      The AWS account ID of the person who created the platform.

    - **PlatformStatus** *(string) --*

      The status of the platform. You can create an environment from the platform once it is
      ready.

    - **PlatformCategory** *(string) --*

      The category of platform.

    - **OperatingSystemName** *(string) --*

      The operating system used by the platform.

    - **OperatingSystemVersion** *(string) --*

      The version of the operating system used by the platform.

    - **SupportedTierList** *(list) --*

      The tiers in which the platform runs.

      - *(string) --*

    - **SupportedAddonList** *(list) --*

      The additions associated with the platform.

      - *(string) --*
    """


_ClientListPlatformVersionsResponseTypeDef = TypedDict(
    "_ClientListPlatformVersionsResponseTypeDef",
    {
        "PlatformSummaryList": List[
            ClientListPlatformVersionsResponsePlatformSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListPlatformVersionsResponseTypeDef(
    _ClientListPlatformVersionsResponseTypeDef
):
    """
    Type definition for `ClientListPlatformVersions` `Response`

    - **PlatformSummaryList** *(list) --*

      Detailed information about the platforms.

      - *(dict) --*

        Detailed information about a platform.

        - **PlatformArn** *(string) --*

          The ARN of the platform.

        - **PlatformOwner** *(string) --*

          The AWS account ID of the person who created the platform.

        - **PlatformStatus** *(string) --*

          The status of the platform. You can create an environment from the platform once it is
          ready.

        - **PlatformCategory** *(string) --*

          The category of platform.

        - **OperatingSystemName** *(string) --*

          The operating system used by the platform.

        - **OperatingSystemVersion** *(string) --*

          The version of the operating system used by the platform.

        - **SupportedTierList** *(list) --*

          The tiers in which the platform runs.

          - *(string) --*

        - **SupportedAddonList** *(list) --*

          The additions associated with the platform.

          - *(string) --*

    - **NextToken** *(string) --*

      The starting index into the remaining list of platforms. if this value is not ``null`` , you
      can use it in a subsequent ``ListPlatformVersion`` call.
    """


_ClientListTagsForResourceResponseResourceTagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseResourceTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponseResourceTagsTypeDef(
    _ClientListTagsForResourceResponseResourceTagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `ResourceTags`

    Describes a tag applied to a resource in an environment.

    - **Key** *(string) --*

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {
        "ResourceArn": str,
        "ResourceTags": List[ClientListTagsForResourceResponseResourceTagsTypeDef],
    },
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **ResourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the resouce for which a tag list was requested.

    - **ResourceTags** *(list) --*

      A list of tag key-value pairs.

      - *(dict) --*

        Describes a tag applied to a resource in an environment.

        - **Key** *(string) --*

          The key of the tag.

        - **Value** *(string) --*

          The value of the tag.
    """


_ClientRetrieveEnvironmentInfoResponseEnvironmentInfoTypeDef = TypedDict(
    "_ClientRetrieveEnvironmentInfoResponseEnvironmentInfoTypeDef",
    {
        "InfoType": str,
        "Ec2InstanceId": str,
        "SampleTimestamp": datetime,
        "Message": str,
    },
    total=False,
)


class ClientRetrieveEnvironmentInfoResponseEnvironmentInfoTypeDef(
    _ClientRetrieveEnvironmentInfoResponseEnvironmentInfoTypeDef
):
    """
    Type definition for `ClientRetrieveEnvironmentInfoResponse` `EnvironmentInfo`

    The information retrieved from the Amazon EC2 instances.

    - **InfoType** *(string) --*

      The type of information retrieved.

    - **Ec2InstanceId** *(string) --*

      The Amazon EC2 Instance ID for this information.

    - **SampleTimestamp** *(datetime) --*

      The time stamp when this information was retrieved.

    - **Message** *(string) --*

      The retrieved information. Currently contains a presigned Amazon S3 URL. The files are
      deleted after 15 minutes.

      Anyone in possession of this URL can access the files before they are deleted. Make the
      URL available only to trusted parties.
    """


_ClientRetrieveEnvironmentInfoResponseTypeDef = TypedDict(
    "_ClientRetrieveEnvironmentInfoResponseTypeDef",
    {
        "EnvironmentInfo": List[
            ClientRetrieveEnvironmentInfoResponseEnvironmentInfoTypeDef
        ]
    },
    total=False,
)


class ClientRetrieveEnvironmentInfoResponseTypeDef(
    _ClientRetrieveEnvironmentInfoResponseTypeDef
):
    """
    Type definition for `ClientRetrieveEnvironmentInfo` `Response`

    Result message containing a description of the requested environment info.

    - **EnvironmentInfo** *(list) --*

      The  EnvironmentInfoDescription of the environment.

      - *(dict) --*

        The information retrieved from the Amazon EC2 instances.

        - **InfoType** *(string) --*

          The type of information retrieved.

        - **Ec2InstanceId** *(string) --*

          The Amazon EC2 Instance ID for this information.

        - **SampleTimestamp** *(datetime) --*

          The time stamp when this information was retrieved.

        - **Message** *(string) --*

          The retrieved information. Currently contains a presigned Amazon S3 URL. The files are
          deleted after 15 minutes.

          Anyone in possession of this URL can access the files before they are deleted. Make the
          URL available only to trusted parties.
    """


_ClientTerminateEnvironmentResponseEnvironmentLinksTypeDef = TypedDict(
    "_ClientTerminateEnvironmentResponseEnvironmentLinksTypeDef",
    {"LinkName": str, "EnvironmentName": str},
    total=False,
)


class ClientTerminateEnvironmentResponseEnvironmentLinksTypeDef(
    _ClientTerminateEnvironmentResponseEnvironmentLinksTypeDef
):
    """
    Type definition for `ClientTerminateEnvironmentResponse` `EnvironmentLinks`

    A link to another environment, defined in the environment's manifest. Links provide
    connection information in system properties that can be used to connect to another
    environment in the same group. See `Environment Manifest (env.yaml)
    <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__
    for details.

    - **LinkName** *(string) --*

      The name of the link.

    - **EnvironmentName** *(string) --*

      The name of the linked environment (the dependency).
    """


_ClientTerminateEnvironmentResponseResourcesLoadBalancerListenersTypeDef = TypedDict(
    "_ClientTerminateEnvironmentResponseResourcesLoadBalancerListenersTypeDef",
    {"Protocol": str, "Port": int},
    total=False,
)


class ClientTerminateEnvironmentResponseResourcesLoadBalancerListenersTypeDef(
    _ClientTerminateEnvironmentResponseResourcesLoadBalancerListenersTypeDef
):
    """
    Type definition for `ClientTerminateEnvironmentResponseResourcesLoadBalancer` `Listeners`

    Describes the properties of a Listener for the LoadBalancer.

    - **Protocol** *(string) --*

      The protocol that is used by the Listener.

    - **Port** *(integer) --*

      The port that is used by the Listener.
    """


_ClientTerminateEnvironmentResponseResourcesLoadBalancerTypeDef = TypedDict(
    "_ClientTerminateEnvironmentResponseResourcesLoadBalancerTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List[
            ClientTerminateEnvironmentResponseResourcesLoadBalancerListenersTypeDef
        ],
    },
    total=False,
)


class ClientTerminateEnvironmentResponseResourcesLoadBalancerTypeDef(
    _ClientTerminateEnvironmentResponseResourcesLoadBalancerTypeDef
):
    """
    Type definition for `ClientTerminateEnvironmentResponseResources` `LoadBalancer`

    Describes the LoadBalancer.

    - **LoadBalancerName** *(string) --*

      The name of the LoadBalancer.

    - **Domain** *(string) --*

      The domain name of the LoadBalancer.

    - **Listeners** *(list) --*

      A list of Listeners used by the LoadBalancer.

      - *(dict) --*

        Describes the properties of a Listener for the LoadBalancer.

        - **Protocol** *(string) --*

          The protocol that is used by the Listener.

        - **Port** *(integer) --*

          The port that is used by the Listener.
    """


_ClientTerminateEnvironmentResponseResourcesTypeDef = TypedDict(
    "_ClientTerminateEnvironmentResponseResourcesTypeDef",
    {"LoadBalancer": ClientTerminateEnvironmentResponseResourcesLoadBalancerTypeDef},
    total=False,
)


class ClientTerminateEnvironmentResponseResourcesTypeDef(
    _ClientTerminateEnvironmentResponseResourcesTypeDef
):
    """
    Type definition for `ClientTerminateEnvironmentResponse` `Resources`

    The description of the AWS resources used by this environment.

    - **LoadBalancer** *(dict) --*

      Describes the LoadBalancer.

      - **LoadBalancerName** *(string) --*

        The name of the LoadBalancer.

      - **Domain** *(string) --*

        The domain name of the LoadBalancer.

      - **Listeners** *(list) --*

        A list of Listeners used by the LoadBalancer.

        - *(dict) --*

          Describes the properties of a Listener for the LoadBalancer.

          - **Protocol** *(string) --*

            The protocol that is used by the Listener.

          - **Port** *(integer) --*

            The port that is used by the Listener.
    """


_ClientTerminateEnvironmentResponseTierTypeDef = TypedDict(
    "_ClientTerminateEnvironmentResponseTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)


class ClientTerminateEnvironmentResponseTierTypeDef(
    _ClientTerminateEnvironmentResponseTierTypeDef
):
    """
    Type definition for `ClientTerminateEnvironmentResponse` `Tier`

    Describes the current tier of this environment.

    - **Name** *(string) --*

      The name of this environment tier.

      Valid values:

      * For *Web server tier* – ``WebServer``

      * For *Worker tier* – ``Worker``

    - **Type** *(string) --*

      The type of this environment tier.

      Valid values:

      * For *Web server tier* – ``Standard``

      * For *Worker tier* – ``SQS/HTTP``

    - **Version** *(string) --*

      The version of this environment tier. When you don't set a value to it, Elastic Beanstalk
      uses the latest compatible worker tier version.

      .. note::

        This member is deprecated. Any specific version that you set may become out of date. We
        recommend leaving it unspecified.
    """


_ClientTerminateEnvironmentResponseTypeDef = TypedDict(
    "_ClientTerminateEnvironmentResponseTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": str,
        "AbortableOperationInProgress": bool,
        "Health": str,
        "HealthStatus": str,
        "Resources": ClientTerminateEnvironmentResponseResourcesTypeDef,
        "Tier": ClientTerminateEnvironmentResponseTierTypeDef,
        "EnvironmentLinks": List[
            ClientTerminateEnvironmentResponseEnvironmentLinksTypeDef
        ],
        "EnvironmentArn": str,
    },
    total=False,
)


class ClientTerminateEnvironmentResponseTypeDef(
    _ClientTerminateEnvironmentResponseTypeDef
):
    """
    Type definition for `ClientTerminateEnvironment` `Response`

    Describes the properties of an environment.

    - **EnvironmentName** *(string) --*

      The name of this environment.

    - **EnvironmentId** *(string) --*

      The ID of this environment.

    - **ApplicationName** *(string) --*

      The name of the application associated with this environment.

    - **VersionLabel** *(string) --*

      The application version deployed in this environment.

    - **SolutionStackName** *(string) --*

      The name of the ``SolutionStack`` deployed with this environment.

    - **PlatformArn** *(string) --*

      The ARN of the platform.

    - **TemplateName** *(string) --*

      The name of the configuration template used to originally launch this environment.

    - **Description** *(string) --*

      Describes this environment.

    - **EndpointURL** *(string) --*

      For load-balanced, autoscaling environments, the URL to the LoadBalancer. For single-instance
      environments, the IP address of the instance.

    - **CNAME** *(string) --*

      The URL to the CNAME for this environment.

    - **DateCreated** *(datetime) --*

      The creation date for this environment.

    - **DateUpdated** *(datetime) --*

      The last modified date for this environment.

    - **Status** *(string) --*

      The current operational status of the environment:

      * ``Launching`` : Environment is in the process of initial deployment.

      * ``Updating`` : Environment is in the process of updating its configuration settings or
      application version.

      * ``Ready`` : Environment is available to have an action performed on it, such as update or
      terminate.

      * ``Terminating`` : Environment is in the shut-down process.

      * ``Terminated`` : Environment is not running.

    - **AbortableOperationInProgress** *(boolean) --*

      Indicates if there is an in-progress environment configuration update or application version
      deployment that you can cancel.

       ``true:`` There is an update in progress.

       ``false:`` There are no updates currently in progress.

    - **Health** *(string) --*

      Describes the health status of the environment. AWS Elastic Beanstalk indicates the failure
      levels for a running environment:

      * ``Red`` : Indicates the environment is not responsive. Occurs when three or more
      consecutive failures occur for an environment.

      * ``Yellow`` : Indicates that something is wrong. Occurs when two consecutive failures occur
      for an environment.

      * ``Green`` : Indicates the environment is healthy and fully functional.

      * ``Grey`` : Default health for a new environment. The environment is not fully launched and
      health checks have not started or health checks are suspended during an ``UpdateEnvironment``
      or ``RestartEnvironment`` request.

      Default: ``Grey``

    - **HealthStatus** *(string) --*

      Returns the health status of the application running in your environment. For more
      information, see `Health Colors and Statuses
      <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

    - **Resources** *(dict) --*

      The description of the AWS resources used by this environment.

      - **LoadBalancer** *(dict) --*

        Describes the LoadBalancer.

        - **LoadBalancerName** *(string) --*

          The name of the LoadBalancer.

        - **Domain** *(string) --*

          The domain name of the LoadBalancer.

        - **Listeners** *(list) --*

          A list of Listeners used by the LoadBalancer.

          - *(dict) --*

            Describes the properties of a Listener for the LoadBalancer.

            - **Protocol** *(string) --*

              The protocol that is used by the Listener.

            - **Port** *(integer) --*

              The port that is used by the Listener.

    - **Tier** *(dict) --*

      Describes the current tier of this environment.

      - **Name** *(string) --*

        The name of this environment tier.

        Valid values:

        * For *Web server tier* – ``WebServer``

        * For *Worker tier* – ``Worker``

      - **Type** *(string) --*

        The type of this environment tier.

        Valid values:

        * For *Web server tier* – ``Standard``

        * For *Worker tier* – ``SQS/HTTP``

      - **Version** *(string) --*

        The version of this environment tier. When you don't set a value to it, Elastic Beanstalk
        uses the latest compatible worker tier version.

        .. note::

          This member is deprecated. Any specific version that you set may become out of date. We
          recommend leaving it unspecified.

    - **EnvironmentLinks** *(list) --*

      A list of links to other environments in the same group.

      - *(dict) --*

        A link to another environment, defined in the environment's manifest. Links provide
        connection information in system properties that can be used to connect to another
        environment in the same group. See `Environment Manifest (env.yaml)
        <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__
        for details.

        - **LinkName** *(string) --*

          The name of the link.

        - **EnvironmentName** *(string) --*

          The name of the linked environment (the dependency).

    - **EnvironmentArn** *(string) --*

      The environment's Amazon Resource Name (ARN), which can be used in other API requests that
      require an ARN.
    """


_RequiredClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"Enabled": bool},
)
_OptionalClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"MaxAgeInDays": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef(
    _RequiredClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    _OptionalClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfig` `MaxAgeRule`

    Specify a max age rule to restrict the length of time that application versions are retained
    for an application.

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Specify ``true`` to apply the rule, or ``false`` to disable it.

    - **MaxAgeInDays** *(integer) --*

      Specify the number of days to retain an application versions.

    - **DeleteSourceFromS3** *(boolean) --*

      Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk
      deletes the application version.
    """


_RequiredClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "_RequiredClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"Enabled": bool},
)
_OptionalClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "_OptionalClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"MaxCount": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef(
    _RequiredClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
    _OptionalClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
):
    """
    Type definition for `ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfig` `MaxCountRule`

    Specify a max count rule to restrict the number of application versions that are retained for
    an application.

    - **Enabled** *(boolean) --* **[REQUIRED]**

      Specify ``true`` to apply the rule, or ``false`` to disable it.

    - **MaxCount** *(integer) --*

      Specify the maximum number of application versions to retain.

    - **DeleteSourceFromS3** *(boolean) --*

      Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk
      deletes the application version.
    """


_ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigTypeDef = TypedDict(
    "_ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
        "MaxAgeRule": ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigTypeDef(
    _ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResourceLifecycleResourceLifecycleConfig` `VersionLifecycleConfig`

    The application version lifecycle configuration.

    - **MaxCountRule** *(dict) --*

      Specify a max count rule to restrict the number of application versions that are retained for
      an application.

      - **Enabled** *(boolean) --* **[REQUIRED]**

        Specify ``true`` to apply the rule, or ``false`` to disable it.

      - **MaxCount** *(integer) --*

        Specify the maximum number of application versions to retain.

      - **DeleteSourceFromS3** *(boolean) --*

        Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk
        deletes the application version.

    - **MaxAgeRule** *(dict) --*

      Specify a max age rule to restrict the length of time that application versions are retained
      for an application.

      - **Enabled** *(boolean) --* **[REQUIRED]**

        Specify ``true`` to apply the rule, or ``false`` to disable it.

      - **MaxAgeInDays** *(integer) --*

        Specify the number of days to retain an application versions.

      - **DeleteSourceFromS3** *(boolean) --*

        Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk
        deletes the application version.
    """


_ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigTypeDef = TypedDict(
    "_ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigVersionLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigTypeDef(
    _ClientUpdateApplicationResourceLifecycleResourceLifecycleConfigTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResourceLifecycle` `ResourceLifecycleConfig`

    The lifecycle configuration.

    - **ServiceRole** *(string) --*

      The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

      The ``ServiceRole`` property is required the first time that you provide a
      ``VersionLifecycleConfig`` for the application in one of the supporting calls
      (``CreateApplication`` or ``UpdateApplicationResourceLifecycle`` ). After you provide it once,
      in either one of the calls, Elastic Beanstalk persists the Service Role with the application,
      and you don't need to specify it again in subsequent ``UpdateApplicationResourceLifecycle``
      calls. You can, however, specify it in subsequent calls to change the Service Role to another
      value.

    - **VersionLifecycleConfig** *(dict) --*

      The application version lifecycle configuration.

      - **MaxCountRule** *(dict) --*

        Specify a max count rule to restrict the number of application versions that are retained for
        an application.

        - **Enabled** *(boolean) --* **[REQUIRED]**

          Specify ``true`` to apply the rule, or ``false`` to disable it.

        - **MaxCount** *(integer) --*

          Specify the maximum number of application versions to retain.

        - **DeleteSourceFromS3** *(boolean) --*

          Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk
          deletes the application version.

      - **MaxAgeRule** *(dict) --*

        Specify a max age rule to restrict the length of time that application versions are retained
        for an application.

        - **Enabled** *(boolean) --* **[REQUIRED]**

          Specify ``true`` to apply the rule, or ``false`` to disable it.

        - **MaxAgeInDays** *(integer) --*

          Specify the number of days to retain an application versions.

        - **DeleteSourceFromS3** *(boolean) --*

          Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk
          deletes the application version.
    """


_ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "_ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"Enabled": bool, "MaxAgeInDays": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef(
    _ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfig` `MaxAgeRule`

    Specify a max age rule to restrict the length of time that application versions are
    retained for an application.

    - **Enabled** *(boolean) --*

      Specify ``true`` to apply the rule, or ``false`` to disable it.

    - **MaxAgeInDays** *(integer) --*

      Specify the number of days to retain an application versions.

    - **DeleteSourceFromS3** *(boolean) --*

      Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
      Beanstalk deletes the application version.
    """


_ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "_ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"Enabled": bool, "MaxCount": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef(
    _ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfig` `MaxCountRule`

    Specify a max count rule to restrict the number of application versions that are retained
    for an application.

    - **Enabled** *(boolean) --*

      Specify ``true`` to apply the rule, or ``false`` to disable it.

    - **MaxCount** *(integer) --*

      Specify the maximum number of application versions to retain.

    - **DeleteSourceFromS3** *(boolean) --*

      Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
      Beanstalk deletes the application version.
    """


_ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigTypeDef = TypedDict(
    "_ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
        "MaxAgeRule": ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigTypeDef(
    _ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfig` `VersionLifecycleConfig`

    The application version lifecycle configuration.

    - **MaxCountRule** *(dict) --*

      Specify a max count rule to restrict the number of application versions that are retained
      for an application.

      - **Enabled** *(boolean) --*

        Specify ``true`` to apply the rule, or ``false`` to disable it.

      - **MaxCount** *(integer) --*

        Specify the maximum number of application versions to retain.

      - **DeleteSourceFromS3** *(boolean) --*

        Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
        Beanstalk deletes the application version.

    - **MaxAgeRule** *(dict) --*

      Specify a max age rule to restrict the length of time that application versions are
      retained for an application.

      - **Enabled** *(boolean) --*

        Specify ``true`` to apply the rule, or ``false`` to disable it.

      - **MaxAgeInDays** *(integer) --*

        Specify the number of days to retain an application versions.

      - **DeleteSourceFromS3** *(boolean) --*

        Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
        Beanstalk deletes the application version.
    """


_ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigTypeDef = TypedDict(
    "_ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigVersionLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigTypeDef(
    _ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResourceLifecycleResponse` `ResourceLifecycleConfig`

    The lifecycle configuration.

    - **ServiceRole** *(string) --*

      The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

      The ``ServiceRole`` property is required the first time that you provide a
      ``VersionLifecycleConfig`` for the application in one of the supporting calls
      (``CreateApplication`` or ``UpdateApplicationResourceLifecycle`` ). After you provide it
      once, in either one of the calls, Elastic Beanstalk persists the Service Role with the
      application, and you don't need to specify it again in subsequent
      ``UpdateApplicationResourceLifecycle`` calls. You can, however, specify it in subsequent
      calls to change the Service Role to another value.

    - **VersionLifecycleConfig** *(dict) --*

      The application version lifecycle configuration.

      - **MaxCountRule** *(dict) --*

        Specify a max count rule to restrict the number of application versions that are retained
        for an application.

        - **Enabled** *(boolean) --*

          Specify ``true`` to apply the rule, or ``false`` to disable it.

        - **MaxCount** *(integer) --*

          Specify the maximum number of application versions to retain.

        - **DeleteSourceFromS3** *(boolean) --*

          Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
          Beanstalk deletes the application version.

      - **MaxAgeRule** *(dict) --*

        Specify a max age rule to restrict the length of time that application versions are
        retained for an application.

        - **Enabled** *(boolean) --*

          Specify ``true`` to apply the rule, or ``false`` to disable it.

        - **MaxAgeInDays** *(integer) --*

          Specify the number of days to retain an application versions.

        - **DeleteSourceFromS3** *(boolean) --*

          Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
          Beanstalk deletes the application version.
    """


_ClientUpdateApplicationResourceLifecycleResponseTypeDef = TypedDict(
    "_ClientUpdateApplicationResourceLifecycleResponseTypeDef",
    {
        "ApplicationName": str,
        "ResourceLifecycleConfig": ClientUpdateApplicationResourceLifecycleResponseResourceLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResourceLifecycleResponseTypeDef(
    _ClientUpdateApplicationResourceLifecycleResponseTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResourceLifecycle` `Response`

    - **ApplicationName** *(string) --*

      The name of the application.

    - **ResourceLifecycleConfig** *(dict) --*

      The lifecycle configuration.

      - **ServiceRole** *(string) --*

        The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

        The ``ServiceRole`` property is required the first time that you provide a
        ``VersionLifecycleConfig`` for the application in one of the supporting calls
        (``CreateApplication`` or ``UpdateApplicationResourceLifecycle`` ). After you provide it
        once, in either one of the calls, Elastic Beanstalk persists the Service Role with the
        application, and you don't need to specify it again in subsequent
        ``UpdateApplicationResourceLifecycle`` calls. You can, however, specify it in subsequent
        calls to change the Service Role to another value.

      - **VersionLifecycleConfig** *(dict) --*

        The application version lifecycle configuration.

        - **MaxCountRule** *(dict) --*

          Specify a max count rule to restrict the number of application versions that are retained
          for an application.

          - **Enabled** *(boolean) --*

            Specify ``true`` to apply the rule, or ``false`` to disable it.

          - **MaxCount** *(integer) --*

            Specify the maximum number of application versions to retain.

          - **DeleteSourceFromS3** *(boolean) --*

            Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
            Beanstalk deletes the application version.

        - **MaxAgeRule** *(dict) --*

          Specify a max age rule to restrict the length of time that application versions are
          retained for an application.

          - **Enabled** *(boolean) --*

            Specify ``true`` to apply the rule, or ``false`` to disable it.

          - **MaxAgeInDays** *(integer) --*

            Specify the number of days to retain an application versions.

          - **DeleteSourceFromS3** *(boolean) --*

            Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
            Beanstalk deletes the application version.
    """


_ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef",
    {"Enabled": bool, "MaxAgeInDays": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef(
    _ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfig` `MaxAgeRule`

    Specify a max age rule to restrict the length of time that application versions are
    retained for an application.

    - **Enabled** *(boolean) --*

      Specify ``true`` to apply the rule, or ``false`` to disable it.

    - **MaxAgeInDays** *(integer) --*

      Specify the number of days to retain an application versions.

    - **DeleteSourceFromS3** *(boolean) --*

      Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
      Beanstalk deletes the application version.
    """


_ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef",
    {"Enabled": bool, "MaxCount": int, "DeleteSourceFromS3": bool},
    total=False,
)


class ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef(
    _ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfig` `MaxCountRule`

    Specify a max count rule to restrict the number of application versions that are
    retained for an application.

    - **Enabled** *(boolean) --*

      Specify ``true`` to apply the rule, or ``false`` to disable it.

    - **MaxCount** *(integer) --*

      Specify the maximum number of application versions to retain.

    - **DeleteSourceFromS3** *(boolean) --*

      Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
      Beanstalk deletes the application version.
    """


_ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxCountRuleTypeDef,
        "MaxAgeRule": ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigMaxAgeRuleTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef(
    _ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplicationResourceLifecycleConfig` `VersionLifecycleConfig`

    The application version lifecycle configuration.

    - **MaxCountRule** *(dict) --*

      Specify a max count rule to restrict the number of application versions that are
      retained for an application.

      - **Enabled** *(boolean) --*

        Specify ``true`` to apply the rule, or ``false`` to disable it.

      - **MaxCount** *(integer) --*

        Specify the maximum number of application versions to retain.

      - **DeleteSourceFromS3** *(boolean) --*

        Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
        Beanstalk deletes the application version.

    - **MaxAgeRule** *(dict) --*

      Specify a max age rule to restrict the length of time that application versions are
      retained for an application.

      - **Enabled** *(boolean) --*

        Specify ``true`` to apply the rule, or ``false`` to disable it.

      - **MaxAgeInDays** *(integer) --*

        Specify the number of days to retain an application versions.

      - **DeleteSourceFromS3** *(boolean) --*

        Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
        Beanstalk deletes the application version.
    """


_ClientUpdateApplicationResponseApplicationResourceLifecycleConfigTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": ClientUpdateApplicationResponseApplicationResourceLifecycleConfigVersionLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationResourceLifecycleConfigTypeDef(
    _ClientUpdateApplicationResponseApplicationResourceLifecycleConfigTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponseApplication` `ResourceLifecycleConfig`

    The lifecycle settings for the application.

    - **ServiceRole** *(string) --*

      The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

      The ``ServiceRole`` property is required the first time that you provide a
      ``VersionLifecycleConfig`` for the application in one of the supporting calls
      (``CreateApplication`` or ``UpdateApplicationResourceLifecycle`` ). After you provide it
      once, in either one of the calls, Elastic Beanstalk persists the Service Role with the
      application, and you don't need to specify it again in subsequent
      ``UpdateApplicationResourceLifecycle`` calls. You can, however, specify it in subsequent
      calls to change the Service Role to another value.

    - **VersionLifecycleConfig** *(dict) --*

      The application version lifecycle configuration.

      - **MaxCountRule** *(dict) --*

        Specify a max count rule to restrict the number of application versions that are
        retained for an application.

        - **Enabled** *(boolean) --*

          Specify ``true`` to apply the rule, or ``false`` to disable it.

        - **MaxCount** *(integer) --*

          Specify the maximum number of application versions to retain.

        - **DeleteSourceFromS3** *(boolean) --*

          Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
          Beanstalk deletes the application version.

      - **MaxAgeRule** *(dict) --*

        Specify a max age rule to restrict the length of time that application versions are
        retained for an application.

        - **Enabled** *(boolean) --*

          Specify ``true`` to apply the rule, or ``false`` to disable it.

        - **MaxAgeInDays** *(integer) --*

          Specify the number of days to retain an application versions.

        - **DeleteSourceFromS3** *(boolean) --*

          Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
          Beanstalk deletes the application version.
    """


_ClientUpdateApplicationResponseApplicationTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseApplicationTypeDef",
    {
        "ApplicationArn": str,
        "ApplicationName": str,
        "Description": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Versions": List[str],
        "ConfigurationTemplates": List[str],
        "ResourceLifecycleConfig": ClientUpdateApplicationResponseApplicationResourceLifecycleConfigTypeDef,
    },
    total=False,
)


class ClientUpdateApplicationResponseApplicationTypeDef(
    _ClientUpdateApplicationResponseApplicationTypeDef
):
    """
    Type definition for `ClientUpdateApplicationResponse` `Application`

    The  ApplicationDescription of the application.

    - **ApplicationArn** *(string) --*

      The Amazon Resource Name (ARN) of the application.

    - **ApplicationName** *(string) --*

      The name of the application.

    - **Description** *(string) --*

      User-defined description of the application.

    - **DateCreated** *(datetime) --*

      The date when the application was created.

    - **DateUpdated** *(datetime) --*

      The date when the application was last modified.

    - **Versions** *(list) --*

      The names of the versions for this application.

      - *(string) --*

    - **ConfigurationTemplates** *(list) --*

      The names of the configuration templates associated with this application.

      - *(string) --*

    - **ResourceLifecycleConfig** *(dict) --*

      The lifecycle settings for the application.

      - **ServiceRole** *(string) --*

        The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

        The ``ServiceRole`` property is required the first time that you provide a
        ``VersionLifecycleConfig`` for the application in one of the supporting calls
        (``CreateApplication`` or ``UpdateApplicationResourceLifecycle`` ). After you provide it
        once, in either one of the calls, Elastic Beanstalk persists the Service Role with the
        application, and you don't need to specify it again in subsequent
        ``UpdateApplicationResourceLifecycle`` calls. You can, however, specify it in subsequent
        calls to change the Service Role to another value.

      - **VersionLifecycleConfig** *(dict) --*

        The application version lifecycle configuration.

        - **MaxCountRule** *(dict) --*

          Specify a max count rule to restrict the number of application versions that are
          retained for an application.

          - **Enabled** *(boolean) --*

            Specify ``true`` to apply the rule, or ``false`` to disable it.

          - **MaxCount** *(integer) --*

            Specify the maximum number of application versions to retain.

          - **DeleteSourceFromS3** *(boolean) --*

            Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
            Beanstalk deletes the application version.

        - **MaxAgeRule** *(dict) --*

          Specify a max age rule to restrict the length of time that application versions are
          retained for an application.

          - **Enabled** *(boolean) --*

            Specify ``true`` to apply the rule, or ``false`` to disable it.

          - **MaxAgeInDays** *(integer) --*

            Specify the number of days to retain an application versions.

          - **DeleteSourceFromS3** *(boolean) --*

            Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
            Beanstalk deletes the application version.
    """


_ClientUpdateApplicationResponseTypeDef = TypedDict(
    "_ClientUpdateApplicationResponseTypeDef",
    {"Application": ClientUpdateApplicationResponseApplicationTypeDef},
    total=False,
)


class ClientUpdateApplicationResponseTypeDef(_ClientUpdateApplicationResponseTypeDef):
    """
    Type definition for `ClientUpdateApplication` `Response`

    Result message containing a single description of an application.

    - **Application** *(dict) --*

      The  ApplicationDescription of the application.

      - **ApplicationArn** *(string) --*

        The Amazon Resource Name (ARN) of the application.

      - **ApplicationName** *(string) --*

        The name of the application.

      - **Description** *(string) --*

        User-defined description of the application.

      - **DateCreated** *(datetime) --*

        The date when the application was created.

      - **DateUpdated** *(datetime) --*

        The date when the application was last modified.

      - **Versions** *(list) --*

        The names of the versions for this application.

        - *(string) --*

      - **ConfigurationTemplates** *(list) --*

        The names of the configuration templates associated with this application.

        - *(string) --*

      - **ResourceLifecycleConfig** *(dict) --*

        The lifecycle settings for the application.

        - **ServiceRole** *(string) --*

          The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

          The ``ServiceRole`` property is required the first time that you provide a
          ``VersionLifecycleConfig`` for the application in one of the supporting calls
          (``CreateApplication`` or ``UpdateApplicationResourceLifecycle`` ). After you provide it
          once, in either one of the calls, Elastic Beanstalk persists the Service Role with the
          application, and you don't need to specify it again in subsequent
          ``UpdateApplicationResourceLifecycle`` calls. You can, however, specify it in subsequent
          calls to change the Service Role to another value.

        - **VersionLifecycleConfig** *(dict) --*

          The application version lifecycle configuration.

          - **MaxCountRule** *(dict) --*

            Specify a max count rule to restrict the number of application versions that are
            retained for an application.

            - **Enabled** *(boolean) --*

              Specify ``true`` to apply the rule, or ``false`` to disable it.

            - **MaxCount** *(integer) --*

              Specify the maximum number of application versions to retain.

            - **DeleteSourceFromS3** *(boolean) --*

              Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
              Beanstalk deletes the application version.

          - **MaxAgeRule** *(dict) --*

            Specify a max age rule to restrict the length of time that application versions are
            retained for an application.

            - **Enabled** *(boolean) --*

              Specify ``true`` to apply the rule, or ``false`` to disable it.

            - **MaxAgeInDays** *(integer) --*

              Specify the number of days to retain an application versions.

            - **DeleteSourceFromS3** *(boolean) --*

              Set to ``true`` to delete a version's source bundle from Amazon S3 when Elastic
              Beanstalk deletes the application version.
    """


_ClientUpdateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef = TypedDict(
    "_ClientUpdateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef",
    {"SourceType": str, "SourceRepository": str, "SourceLocation": str},
    total=False,
)


class ClientUpdateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef(
    _ClientUpdateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef
):
    """
    Type definition for `ClientUpdateApplicationVersionResponseApplicationVersion` `SourceBuildInformation`

    If the version's source code was retrieved from AWS CodeCommit, the location of the source
    code for the application version.

    - **SourceType** *(string) --*

      The type of repository.

      * ``Git``

      * ``Zip``

    - **SourceRepository** *(string) --*

      Location where the repository is stored.

      * ``CodeCommit``

      * ``S3``

    - **SourceLocation** *(string) --*

      The location of the source code, as a formatted string, depending on the value of
      ``SourceRepository``

      * For ``CodeCommit`` , the format is the repository name and commit ID, separated by a
      forward slash. For example, ``my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`` .

      * For ``S3`` , the format is the S3 bucket name and object key, separated by a forward
      slash. For example, ``my-s3-bucket/Folders/my-source-file`` .
    """


_ClientUpdateApplicationVersionResponseApplicationVersionSourceBundleTypeDef = TypedDict(
    "_ClientUpdateApplicationVersionResponseApplicationVersionSourceBundleTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientUpdateApplicationVersionResponseApplicationVersionSourceBundleTypeDef(
    _ClientUpdateApplicationVersionResponseApplicationVersionSourceBundleTypeDef
):
    """
    Type definition for `ClientUpdateApplicationVersionResponseApplicationVersion` `SourceBundle`

    The storage location of the application version's source bundle in Amazon S3.

    - **S3Bucket** *(string) --*

      The Amazon S3 bucket where the data is located.

    - **S3Key** *(string) --*

      The Amazon S3 key where the data is located.
    """


_ClientUpdateApplicationVersionResponseApplicationVersionTypeDef = TypedDict(
    "_ClientUpdateApplicationVersionResponseApplicationVersionTypeDef",
    {
        "ApplicationVersionArn": str,
        "ApplicationName": str,
        "Description": str,
        "VersionLabel": str,
        "SourceBuildInformation": ClientUpdateApplicationVersionResponseApplicationVersionSourceBuildInformationTypeDef,
        "BuildArn": str,
        "SourceBundle": ClientUpdateApplicationVersionResponseApplicationVersionSourceBundleTypeDef,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": str,
    },
    total=False,
)


class ClientUpdateApplicationVersionResponseApplicationVersionTypeDef(
    _ClientUpdateApplicationVersionResponseApplicationVersionTypeDef
):
    """
    Type definition for `ClientUpdateApplicationVersionResponse` `ApplicationVersion`

    The  ApplicationVersionDescription of the application version.

    - **ApplicationVersionArn** *(string) --*

      The Amazon Resource Name (ARN) of the application version.

    - **ApplicationName** *(string) --*

      The name of the application to which the application version belongs.

    - **Description** *(string) --*

      The description of the application version.

    - **VersionLabel** *(string) --*

      A unique identifier for the application version.

    - **SourceBuildInformation** *(dict) --*

      If the version's source code was retrieved from AWS CodeCommit, the location of the source
      code for the application version.

      - **SourceType** *(string) --*

        The type of repository.

        * ``Git``

        * ``Zip``

      - **SourceRepository** *(string) --*

        Location where the repository is stored.

        * ``CodeCommit``

        * ``S3``

      - **SourceLocation** *(string) --*

        The location of the source code, as a formatted string, depending on the value of
        ``SourceRepository``

        * For ``CodeCommit`` , the format is the repository name and commit ID, separated by a
        forward slash. For example, ``my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`` .

        * For ``S3`` , the format is the S3 bucket name and object key, separated by a forward
        slash. For example, ``my-s3-bucket/Folders/my-source-file`` .

    - **BuildArn** *(string) --*

      Reference to the artifact from the AWS CodeBuild build.

    - **SourceBundle** *(dict) --*

      The storage location of the application version's source bundle in Amazon S3.

      - **S3Bucket** *(string) --*

        The Amazon S3 bucket where the data is located.

      - **S3Key** *(string) --*

        The Amazon S3 key where the data is located.

    - **DateCreated** *(datetime) --*

      The creation date of the application version.

    - **DateUpdated** *(datetime) --*

      The last modified date of the application version.

    - **Status** *(string) --*

      The processing status of the application version. Reflects the state of the application
      version during its creation. Many of the values are only applicable if you specified
      ``True`` for the ``Process`` parameter of the ``CreateApplicationVersion`` action. The
      following list describes the possible values.

      * ``Unprocessed`` – Application version wasn't pre-processed or validated. Elastic
      Beanstalk will validate configuration files during deployment of the application version to
      an environment.

      * ``Processing`` – Elastic Beanstalk is currently processing the application version.

      * ``Building`` – Application version is currently undergoing an AWS CodeBuild build.

      * ``Processed`` – Elastic Beanstalk was successfully pre-processed and validated.

      * ``Failed`` – Either the AWS CodeBuild build failed or configuration files didn't pass
      validation. This application version isn't usable.
    """


_ClientUpdateApplicationVersionResponseTypeDef = TypedDict(
    "_ClientUpdateApplicationVersionResponseTypeDef",
    {
        "ApplicationVersion": ClientUpdateApplicationVersionResponseApplicationVersionTypeDef
    },
    total=False,
)


class ClientUpdateApplicationVersionResponseTypeDef(
    _ClientUpdateApplicationVersionResponseTypeDef
):
    """
    Type definition for `ClientUpdateApplicationVersion` `Response`

    Result message wrapping a single description of an application version.

    - **ApplicationVersion** *(dict) --*

      The  ApplicationVersionDescription of the application version.

      - **ApplicationVersionArn** *(string) --*

        The Amazon Resource Name (ARN) of the application version.

      - **ApplicationName** *(string) --*

        The name of the application to which the application version belongs.

      - **Description** *(string) --*

        The description of the application version.

      - **VersionLabel** *(string) --*

        A unique identifier for the application version.

      - **SourceBuildInformation** *(dict) --*

        If the version's source code was retrieved from AWS CodeCommit, the location of the source
        code for the application version.

        - **SourceType** *(string) --*

          The type of repository.

          * ``Git``

          * ``Zip``

        - **SourceRepository** *(string) --*

          Location where the repository is stored.

          * ``CodeCommit``

          * ``S3``

        - **SourceLocation** *(string) --*

          The location of the source code, as a formatted string, depending on the value of
          ``SourceRepository``

          * For ``CodeCommit`` , the format is the repository name and commit ID, separated by a
          forward slash. For example, ``my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`` .

          * For ``S3`` , the format is the S3 bucket name and object key, separated by a forward
          slash. For example, ``my-s3-bucket/Folders/my-source-file`` .

      - **BuildArn** *(string) --*

        Reference to the artifact from the AWS CodeBuild build.

      - **SourceBundle** *(dict) --*

        The storage location of the application version's source bundle in Amazon S3.

        - **S3Bucket** *(string) --*

          The Amazon S3 bucket where the data is located.

        - **S3Key** *(string) --*

          The Amazon S3 key where the data is located.

      - **DateCreated** *(datetime) --*

        The creation date of the application version.

      - **DateUpdated** *(datetime) --*

        The last modified date of the application version.

      - **Status** *(string) --*

        The processing status of the application version. Reflects the state of the application
        version during its creation. Many of the values are only applicable if you specified
        ``True`` for the ``Process`` parameter of the ``CreateApplicationVersion`` action. The
        following list describes the possible values.

        * ``Unprocessed`` – Application version wasn't pre-processed or validated. Elastic
        Beanstalk will validate configuration files during deployment of the application version to
        an environment.

        * ``Processing`` – Elastic Beanstalk is currently processing the application version.

        * ``Building`` – Application version is currently undergoing an AWS CodeBuild build.

        * ``Processed`` – Elastic Beanstalk was successfully pre-processed and validated.

        * ``Failed`` – Either the AWS CodeBuild build failed or configuration files didn't pass
        validation. This application version isn't usable.
    """


_ClientUpdateConfigurationTemplateOptionSettingsTypeDef = TypedDict(
    "_ClientUpdateConfigurationTemplateOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)


class ClientUpdateConfigurationTemplateOptionSettingsTypeDef(
    _ClientUpdateConfigurationTemplateOptionSettingsTypeDef
):
    """
    Type definition for `ClientUpdateConfigurationTemplate` `OptionSettings`

    A specification identifying an individual configuration option along with its current value.
    For a list of possible option values, go to `Option Values
    <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS
    Elastic Beanstalk Developer Guide* .

    - **ResourceName** *(string) --*

      A unique resource name for a time-based scaling configuration option.

    - **Namespace** *(string) --*

      A unique namespace identifying the option's associated AWS resource.

    - **OptionName** *(string) --*

      The name of the configuration option.

    - **Value** *(string) --*

      The current value for the configuration option.
    """


_ClientUpdateConfigurationTemplateOptionsToRemoveTypeDef = TypedDict(
    "_ClientUpdateConfigurationTemplateOptionsToRemoveTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str},
    total=False,
)


class ClientUpdateConfigurationTemplateOptionsToRemoveTypeDef(
    _ClientUpdateConfigurationTemplateOptionsToRemoveTypeDef
):
    """
    Type definition for `ClientUpdateConfigurationTemplate` `OptionsToRemove`

    A specification identifying an individual configuration option.

    - **ResourceName** *(string) --*

      A unique resource name for a time-based scaling configuration option.

    - **Namespace** *(string) --*

      A unique namespace identifying the option's associated AWS resource.

    - **OptionName** *(string) --*

      The name of the configuration option.
    """


_ClientUpdateConfigurationTemplateResponseOptionSettingsTypeDef = TypedDict(
    "_ClientUpdateConfigurationTemplateResponseOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)


class ClientUpdateConfigurationTemplateResponseOptionSettingsTypeDef(
    _ClientUpdateConfigurationTemplateResponseOptionSettingsTypeDef
):
    """
    Type definition for `ClientUpdateConfigurationTemplateResponse` `OptionSettings`

    A specification identifying an individual configuration option along with its current
    value. For a list of possible option values, go to `Option Values
    <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the
    *AWS Elastic Beanstalk Developer Guide* .

    - **ResourceName** *(string) --*

      A unique resource name for a time-based scaling configuration option.

    - **Namespace** *(string) --*

      A unique namespace identifying the option's associated AWS resource.

    - **OptionName** *(string) --*

      The name of the configuration option.

    - **Value** *(string) --*

      The current value for the configuration option.
    """


_ClientUpdateConfigurationTemplateResponseTypeDef = TypedDict(
    "_ClientUpdateConfigurationTemplateResponseTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "ApplicationName": str,
        "TemplateName": str,
        "Description": str,
        "EnvironmentName": str,
        "DeploymentStatus": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "OptionSettings": List[
            ClientUpdateConfigurationTemplateResponseOptionSettingsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateConfigurationTemplateResponseTypeDef(
    _ClientUpdateConfigurationTemplateResponseTypeDef
):
    """
    Type definition for `ClientUpdateConfigurationTemplate` `Response`

    Describes the settings for a configuration set.

    - **SolutionStackName** *(string) --*

      The name of the solution stack this configuration set uses.

    - **PlatformArn** *(string) --*

      The ARN of the platform.

    - **ApplicationName** *(string) --*

      The name of the application associated with this configuration set.

    - **TemplateName** *(string) --*

      If not ``null`` , the name of the configuration template for this configuration set.

    - **Description** *(string) --*

      Describes this configuration set.

    - **EnvironmentName** *(string) --*

      If not ``null`` , the name of the environment for this configuration set.

    - **DeploymentStatus** *(string) --*

      If this configuration set is associated with an environment, the ``DeploymentStatus``
      parameter indicates the deployment status of this configuration set:

      * ``null`` : This configuration is not associated with a running environment.

      * ``pending`` : This is a draft configuration that is not deployed to the associated
      environment but is in the process of deploying.

      * ``deployed`` : This is the configuration that is currently deployed to the associated
      running environment.

      * ``failed`` : This is a draft configuration that failed to successfully deploy.

    - **DateCreated** *(datetime) --*

      The date (in UTC time) when this configuration set was created.

    - **DateUpdated** *(datetime) --*

      The date (in UTC time) when this configuration set was last modified.

    - **OptionSettings** *(list) --*

      A list of the configuration options and their values in this configuration set.

      - *(dict) --*

        A specification identifying an individual configuration option along with its current
        value. For a list of possible option values, go to `Option Values
        <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the
        *AWS Elastic Beanstalk Developer Guide* .

        - **ResourceName** *(string) --*

          A unique resource name for a time-based scaling configuration option.

        - **Namespace** *(string) --*

          A unique namespace identifying the option's associated AWS resource.

        - **OptionName** *(string) --*

          The name of the configuration option.

        - **Value** *(string) --*

          The current value for the configuration option.
    """


_ClientUpdateEnvironmentOptionSettingsTypeDef = TypedDict(
    "_ClientUpdateEnvironmentOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)


class ClientUpdateEnvironmentOptionSettingsTypeDef(
    _ClientUpdateEnvironmentOptionSettingsTypeDef
):
    """
    Type definition for `ClientUpdateEnvironment` `OptionSettings`

    A specification identifying an individual configuration option along with its current value.
    For a list of possible option values, go to `Option Values
    <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS
    Elastic Beanstalk Developer Guide* .

    - **ResourceName** *(string) --*

      A unique resource name for a time-based scaling configuration option.

    - **Namespace** *(string) --*

      A unique namespace identifying the option's associated AWS resource.

    - **OptionName** *(string) --*

      The name of the configuration option.

    - **Value** *(string) --*

      The current value for the configuration option.
    """


_ClientUpdateEnvironmentOptionsToRemoveTypeDef = TypedDict(
    "_ClientUpdateEnvironmentOptionsToRemoveTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str},
    total=False,
)


class ClientUpdateEnvironmentOptionsToRemoveTypeDef(
    _ClientUpdateEnvironmentOptionsToRemoveTypeDef
):
    """
    Type definition for `ClientUpdateEnvironment` `OptionsToRemove`

    A specification identifying an individual configuration option.

    - **ResourceName** *(string) --*

      A unique resource name for a time-based scaling configuration option.

    - **Namespace** *(string) --*

      A unique namespace identifying the option's associated AWS resource.

    - **OptionName** *(string) --*

      The name of the configuration option.
    """


_ClientUpdateEnvironmentResponseEnvironmentLinksTypeDef = TypedDict(
    "_ClientUpdateEnvironmentResponseEnvironmentLinksTypeDef",
    {"LinkName": str, "EnvironmentName": str},
    total=False,
)


class ClientUpdateEnvironmentResponseEnvironmentLinksTypeDef(
    _ClientUpdateEnvironmentResponseEnvironmentLinksTypeDef
):
    """
    Type definition for `ClientUpdateEnvironmentResponse` `EnvironmentLinks`

    A link to another environment, defined in the environment's manifest. Links provide
    connection information in system properties that can be used to connect to another
    environment in the same group. See `Environment Manifest (env.yaml)
    <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__
    for details.

    - **LinkName** *(string) --*

      The name of the link.

    - **EnvironmentName** *(string) --*

      The name of the linked environment (the dependency).
    """


_ClientUpdateEnvironmentResponseResourcesLoadBalancerListenersTypeDef = TypedDict(
    "_ClientUpdateEnvironmentResponseResourcesLoadBalancerListenersTypeDef",
    {"Protocol": str, "Port": int},
    total=False,
)


class ClientUpdateEnvironmentResponseResourcesLoadBalancerListenersTypeDef(
    _ClientUpdateEnvironmentResponseResourcesLoadBalancerListenersTypeDef
):
    """
    Type definition for `ClientUpdateEnvironmentResponseResourcesLoadBalancer` `Listeners`

    Describes the properties of a Listener for the LoadBalancer.

    - **Protocol** *(string) --*

      The protocol that is used by the Listener.

    - **Port** *(integer) --*

      The port that is used by the Listener.
    """


_ClientUpdateEnvironmentResponseResourcesLoadBalancerTypeDef = TypedDict(
    "_ClientUpdateEnvironmentResponseResourcesLoadBalancerTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List[
            ClientUpdateEnvironmentResponseResourcesLoadBalancerListenersTypeDef
        ],
    },
    total=False,
)


class ClientUpdateEnvironmentResponseResourcesLoadBalancerTypeDef(
    _ClientUpdateEnvironmentResponseResourcesLoadBalancerTypeDef
):
    """
    Type definition for `ClientUpdateEnvironmentResponseResources` `LoadBalancer`

    Describes the LoadBalancer.

    - **LoadBalancerName** *(string) --*

      The name of the LoadBalancer.

    - **Domain** *(string) --*

      The domain name of the LoadBalancer.

    - **Listeners** *(list) --*

      A list of Listeners used by the LoadBalancer.

      - *(dict) --*

        Describes the properties of a Listener for the LoadBalancer.

        - **Protocol** *(string) --*

          The protocol that is used by the Listener.

        - **Port** *(integer) --*

          The port that is used by the Listener.
    """


_ClientUpdateEnvironmentResponseResourcesTypeDef = TypedDict(
    "_ClientUpdateEnvironmentResponseResourcesTypeDef",
    {"LoadBalancer": ClientUpdateEnvironmentResponseResourcesLoadBalancerTypeDef},
    total=False,
)


class ClientUpdateEnvironmentResponseResourcesTypeDef(
    _ClientUpdateEnvironmentResponseResourcesTypeDef
):
    """
    Type definition for `ClientUpdateEnvironmentResponse` `Resources`

    The description of the AWS resources used by this environment.

    - **LoadBalancer** *(dict) --*

      Describes the LoadBalancer.

      - **LoadBalancerName** *(string) --*

        The name of the LoadBalancer.

      - **Domain** *(string) --*

        The domain name of the LoadBalancer.

      - **Listeners** *(list) --*

        A list of Listeners used by the LoadBalancer.

        - *(dict) --*

          Describes the properties of a Listener for the LoadBalancer.

          - **Protocol** *(string) --*

            The protocol that is used by the Listener.

          - **Port** *(integer) --*

            The port that is used by the Listener.
    """


_ClientUpdateEnvironmentResponseTierTypeDef = TypedDict(
    "_ClientUpdateEnvironmentResponseTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)


class ClientUpdateEnvironmentResponseTierTypeDef(
    _ClientUpdateEnvironmentResponseTierTypeDef
):
    """
    Type definition for `ClientUpdateEnvironmentResponse` `Tier`

    Describes the current tier of this environment.

    - **Name** *(string) --*

      The name of this environment tier.

      Valid values:

      * For *Web server tier* – ``WebServer``

      * For *Worker tier* – ``Worker``

    - **Type** *(string) --*

      The type of this environment tier.

      Valid values:

      * For *Web server tier* – ``Standard``

      * For *Worker tier* – ``SQS/HTTP``

    - **Version** *(string) --*

      The version of this environment tier. When you don't set a value to it, Elastic Beanstalk
      uses the latest compatible worker tier version.

      .. note::

        This member is deprecated. Any specific version that you set may become out of date. We
        recommend leaving it unspecified.
    """


_ClientUpdateEnvironmentResponseTypeDef = TypedDict(
    "_ClientUpdateEnvironmentResponseTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": str,
        "AbortableOperationInProgress": bool,
        "Health": str,
        "HealthStatus": str,
        "Resources": ClientUpdateEnvironmentResponseResourcesTypeDef,
        "Tier": ClientUpdateEnvironmentResponseTierTypeDef,
        "EnvironmentLinks": List[
            ClientUpdateEnvironmentResponseEnvironmentLinksTypeDef
        ],
        "EnvironmentArn": str,
    },
    total=False,
)


class ClientUpdateEnvironmentResponseTypeDef(_ClientUpdateEnvironmentResponseTypeDef):
    """
    Type definition for `ClientUpdateEnvironment` `Response`

    Describes the properties of an environment.

    - **EnvironmentName** *(string) --*

      The name of this environment.

    - **EnvironmentId** *(string) --*

      The ID of this environment.

    - **ApplicationName** *(string) --*

      The name of the application associated with this environment.

    - **VersionLabel** *(string) --*

      The application version deployed in this environment.

    - **SolutionStackName** *(string) --*

      The name of the ``SolutionStack`` deployed with this environment.

    - **PlatformArn** *(string) --*

      The ARN of the platform.

    - **TemplateName** *(string) --*

      The name of the configuration template used to originally launch this environment.

    - **Description** *(string) --*

      Describes this environment.

    - **EndpointURL** *(string) --*

      For load-balanced, autoscaling environments, the URL to the LoadBalancer. For single-instance
      environments, the IP address of the instance.

    - **CNAME** *(string) --*

      The URL to the CNAME for this environment.

    - **DateCreated** *(datetime) --*

      The creation date for this environment.

    - **DateUpdated** *(datetime) --*

      The last modified date for this environment.

    - **Status** *(string) --*

      The current operational status of the environment:

      * ``Launching`` : Environment is in the process of initial deployment.

      * ``Updating`` : Environment is in the process of updating its configuration settings or
      application version.

      * ``Ready`` : Environment is available to have an action performed on it, such as update or
      terminate.

      * ``Terminating`` : Environment is in the shut-down process.

      * ``Terminated`` : Environment is not running.

    - **AbortableOperationInProgress** *(boolean) --*

      Indicates if there is an in-progress environment configuration update or application version
      deployment that you can cancel.

       ``true:`` There is an update in progress.

       ``false:`` There are no updates currently in progress.

    - **Health** *(string) --*

      Describes the health status of the environment. AWS Elastic Beanstalk indicates the failure
      levels for a running environment:

      * ``Red`` : Indicates the environment is not responsive. Occurs when three or more
      consecutive failures occur for an environment.

      * ``Yellow`` : Indicates that something is wrong. Occurs when two consecutive failures occur
      for an environment.

      * ``Green`` : Indicates the environment is healthy and fully functional.

      * ``Grey`` : Default health for a new environment. The environment is not fully launched and
      health checks have not started or health checks are suspended during an ``UpdateEnvironment``
      or ``RestartEnvironment`` request.

      Default: ``Grey``

    - **HealthStatus** *(string) --*

      Returns the health status of the application running in your environment. For more
      information, see `Health Colors and Statuses
      <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

    - **Resources** *(dict) --*

      The description of the AWS resources used by this environment.

      - **LoadBalancer** *(dict) --*

        Describes the LoadBalancer.

        - **LoadBalancerName** *(string) --*

          The name of the LoadBalancer.

        - **Domain** *(string) --*

          The domain name of the LoadBalancer.

        - **Listeners** *(list) --*

          A list of Listeners used by the LoadBalancer.

          - *(dict) --*

            Describes the properties of a Listener for the LoadBalancer.

            - **Protocol** *(string) --*

              The protocol that is used by the Listener.

            - **Port** *(integer) --*

              The port that is used by the Listener.

    - **Tier** *(dict) --*

      Describes the current tier of this environment.

      - **Name** *(string) --*

        The name of this environment tier.

        Valid values:

        * For *Web server tier* – ``WebServer``

        * For *Worker tier* – ``Worker``

      - **Type** *(string) --*

        The type of this environment tier.

        Valid values:

        * For *Web server tier* – ``Standard``

        * For *Worker tier* – ``SQS/HTTP``

      - **Version** *(string) --*

        The version of this environment tier. When you don't set a value to it, Elastic Beanstalk
        uses the latest compatible worker tier version.

        .. note::

          This member is deprecated. Any specific version that you set may become out of date. We
          recommend leaving it unspecified.

    - **EnvironmentLinks** *(list) --*

      A list of links to other environments in the same group.

      - *(dict) --*

        A link to another environment, defined in the environment's manifest. Links provide
        connection information in system properties that can be used to connect to another
        environment in the same group. See `Environment Manifest (env.yaml)
        <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__
        for details.

        - **LinkName** *(string) --*

          The name of the link.

        - **EnvironmentName** *(string) --*

          The name of the linked environment (the dependency).

    - **EnvironmentArn** *(string) --*

      The environment's Amazon Resource Name (ARN), which can be used in other API requests that
      require an ARN.
    """


_ClientUpdateEnvironmentTierTypeDef = TypedDict(
    "_ClientUpdateEnvironmentTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)


class ClientUpdateEnvironmentTierTypeDef(_ClientUpdateEnvironmentTierTypeDef):
    """
    Type definition for `ClientUpdateEnvironment` `Tier`

    This specifies the tier to use to update the environment.

    Condition: At this time, if you change the tier version, name, or type, AWS Elastic Beanstalk
    returns ``InvalidParameterValue`` error.

    - **Name** *(string) --*

      The name of this environment tier.

      Valid values:

      * For *Web server tier* – ``WebServer``

      * For *Worker tier* – ``Worker``

    - **Type** *(string) --*

      The type of this environment tier.

      Valid values:

      * For *Web server tier* – ``Standard``

      * For *Worker tier* – ``SQS/HTTP``

    - **Version** *(string) --*

      The version of this environment tier. When you don't set a value to it, Elastic Beanstalk uses
      the latest compatible worker tier version.

      .. note::

        This member is deprecated. Any specific version that you set may become out of date. We
        recommend leaving it unspecified.
    """


_ClientUpdateTagsForResourceTagsToAddTypeDef = TypedDict(
    "_ClientUpdateTagsForResourceTagsToAddTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientUpdateTagsForResourceTagsToAddTypeDef(
    _ClientUpdateTagsForResourceTagsToAddTypeDef
):
    """
    Type definition for `ClientUpdateTagsForResource` `TagsToAdd`

    Describes a tag applied to a resource in an environment.

    - **Key** *(string) --*

      The key of the tag.

    - **Value** *(string) --*

      The value of the tag.
    """


_ClientValidateConfigurationSettingsOptionSettingsTypeDef = TypedDict(
    "_ClientValidateConfigurationSettingsOptionSettingsTypeDef",
    {"ResourceName": str, "Namespace": str, "OptionName": str, "Value": str},
    total=False,
)


class ClientValidateConfigurationSettingsOptionSettingsTypeDef(
    _ClientValidateConfigurationSettingsOptionSettingsTypeDef
):
    """
    Type definition for `ClientValidateConfigurationSettings` `OptionSettings`

    A specification identifying an individual configuration option along with its current value.
    For a list of possible option values, go to `Option Values
    <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html>`__ in the *AWS
    Elastic Beanstalk Developer Guide* .

    - **ResourceName** *(string) --*

      A unique resource name for a time-based scaling configuration option.

    - **Namespace** *(string) --*

      A unique namespace identifying the option's associated AWS resource.

    - **OptionName** *(string) --*

      The name of the configuration option.

    - **Value** *(string) --*

      The current value for the configuration option.
    """


_ClientValidateConfigurationSettingsResponseMessagesTypeDef = TypedDict(
    "_ClientValidateConfigurationSettingsResponseMessagesTypeDef",
    {"Message": str, "Severity": str, "Namespace": str, "OptionName": str},
    total=False,
)


class ClientValidateConfigurationSettingsResponseMessagesTypeDef(
    _ClientValidateConfigurationSettingsResponseMessagesTypeDef
):
    """
    Type definition for `ClientValidateConfigurationSettingsResponse` `Messages`

    An error or warning for a desired configuration option value.

    - **Message** *(string) --*

      A message describing the error or warning.

    - **Severity** *(string) --*

      An indication of the severity of this message:

      * ``error`` : This message indicates that this is not a valid setting for an option.

      * ``warning`` : This message is providing information you should take into account.

    - **Namespace** *(string) --*

      The namespace to which the option belongs.

    - **OptionName** *(string) --*

      The name of the option.
    """


_ClientValidateConfigurationSettingsResponseTypeDef = TypedDict(
    "_ClientValidateConfigurationSettingsResponseTypeDef",
    {"Messages": List[ClientValidateConfigurationSettingsResponseMessagesTypeDef]},
    total=False,
)


class ClientValidateConfigurationSettingsResponseTypeDef(
    _ClientValidateConfigurationSettingsResponseTypeDef
):
    """
    Type definition for `ClientValidateConfigurationSettings` `Response`

    Provides a list of validation messages.

    - **Messages** *(list) --*

      A list of  ValidationMessage .

      - *(dict) --*

        An error or warning for a desired configuration option value.

        - **Message** *(string) --*

          A message describing the error or warning.

        - **Severity** *(string) --*

          An indication of the severity of this message:

          * ``error`` : This message indicates that this is not a valid setting for an option.

          * ``warning`` : This message is providing information you should take into account.

        - **Namespace** *(string) --*

          The namespace to which the option belongs.

        - **OptionName** *(string) --*

          The name of the option.
    """


_DescribeApplicationVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeApplicationVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeApplicationVersionsPaginatePaginationConfigTypeDef(
    _DescribeApplicationVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeApplicationVersionsPaginate` `PaginationConfig`

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


_DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBuildInformationTypeDef = TypedDict(
    "_DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBuildInformationTypeDef",
    {"SourceType": str, "SourceRepository": str, "SourceLocation": str},
    total=False,
)


class DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBuildInformationTypeDef(
    _DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBuildInformationTypeDef
):
    """
    Type definition for `DescribeApplicationVersionsPaginateResponseApplicationVersions` `SourceBuildInformation`

    If the version's source code was retrieved from AWS CodeCommit, the location of the
    source code for the application version.

    - **SourceType** *(string) --*

      The type of repository.

      * ``Git``

      * ``Zip``

    - **SourceRepository** *(string) --*

      Location where the repository is stored.

      * ``CodeCommit``

      * ``S3``

    - **SourceLocation** *(string) --*

      The location of the source code, as a formatted string, depending on the value of
      ``SourceRepository``

      * For ``CodeCommit`` , the format is the repository name and commit ID, separated by a
      forward slash. For example, ``my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`` .

      * For ``S3`` , the format is the S3 bucket name and object key, separated by a forward
      slash. For example, ``my-s3-bucket/Folders/my-source-file`` .
    """


_DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBundleTypeDef = TypedDict(
    "_DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBundleTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBundleTypeDef(
    _DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBundleTypeDef
):
    """
    Type definition for `DescribeApplicationVersionsPaginateResponseApplicationVersions` `SourceBundle`

    The storage location of the application version's source bundle in Amazon S3.

    - **S3Bucket** *(string) --*

      The Amazon S3 bucket where the data is located.

    - **S3Key** *(string) --*

      The Amazon S3 key where the data is located.
    """


_DescribeApplicationVersionsPaginateResponseApplicationVersionsTypeDef = TypedDict(
    "_DescribeApplicationVersionsPaginateResponseApplicationVersionsTypeDef",
    {
        "ApplicationVersionArn": str,
        "ApplicationName": str,
        "Description": str,
        "VersionLabel": str,
        "SourceBuildInformation": DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBuildInformationTypeDef,
        "BuildArn": str,
        "SourceBundle": DescribeApplicationVersionsPaginateResponseApplicationVersionsSourceBundleTypeDef,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": str,
    },
    total=False,
)


class DescribeApplicationVersionsPaginateResponseApplicationVersionsTypeDef(
    _DescribeApplicationVersionsPaginateResponseApplicationVersionsTypeDef
):
    """
    Type definition for `DescribeApplicationVersionsPaginateResponse` `ApplicationVersions`

    Describes the properties of an application version.

    - **ApplicationVersionArn** *(string) --*

      The Amazon Resource Name (ARN) of the application version.

    - **ApplicationName** *(string) --*

      The name of the application to which the application version belongs.

    - **Description** *(string) --*

      The description of the application version.

    - **VersionLabel** *(string) --*

      A unique identifier for the application version.

    - **SourceBuildInformation** *(dict) --*

      If the version's source code was retrieved from AWS CodeCommit, the location of the
      source code for the application version.

      - **SourceType** *(string) --*

        The type of repository.

        * ``Git``

        * ``Zip``

      - **SourceRepository** *(string) --*

        Location where the repository is stored.

        * ``CodeCommit``

        * ``S3``

      - **SourceLocation** *(string) --*

        The location of the source code, as a formatted string, depending on the value of
        ``SourceRepository``

        * For ``CodeCommit`` , the format is the repository name and commit ID, separated by a
        forward slash. For example, ``my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`` .

        * For ``S3`` , the format is the S3 bucket name and object key, separated by a forward
        slash. For example, ``my-s3-bucket/Folders/my-source-file`` .

    - **BuildArn** *(string) --*

      Reference to the artifact from the AWS CodeBuild build.

    - **SourceBundle** *(dict) --*

      The storage location of the application version's source bundle in Amazon S3.

      - **S3Bucket** *(string) --*

        The Amazon S3 bucket where the data is located.

      - **S3Key** *(string) --*

        The Amazon S3 key where the data is located.

    - **DateCreated** *(datetime) --*

      The creation date of the application version.

    - **DateUpdated** *(datetime) --*

      The last modified date of the application version.

    - **Status** *(string) --*

      The processing status of the application version. Reflects the state of the application
      version during its creation. Many of the values are only applicable if you specified
      ``True`` for the ``Process`` parameter of the ``CreateApplicationVersion`` action. The
      following list describes the possible values.

      * ``Unprocessed`` – Application version wasn't pre-processed or validated. Elastic
      Beanstalk will validate configuration files during deployment of the application version
      to an environment.

      * ``Processing`` – Elastic Beanstalk is currently processing the application version.

      * ``Building`` – Application version is currently undergoing an AWS CodeBuild build.

      * ``Processed`` – Elastic Beanstalk was successfully pre-processed and validated.

      * ``Failed`` – Either the AWS CodeBuild build failed or configuration files didn't pass
      validation. This application version isn't usable.
    """


_DescribeApplicationVersionsPaginateResponseTypeDef = TypedDict(
    "_DescribeApplicationVersionsPaginateResponseTypeDef",
    {
        "ApplicationVersions": List[
            DescribeApplicationVersionsPaginateResponseApplicationVersionsTypeDef
        ]
    },
    total=False,
)


class DescribeApplicationVersionsPaginateResponseTypeDef(
    _DescribeApplicationVersionsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeApplicationVersionsPaginate` `Response`

    Result message wrapping a list of application version descriptions.

    - **ApplicationVersions** *(list) --*

      List of ``ApplicationVersionDescription`` objects sorted in order of creation.

      - *(dict) --*

        Describes the properties of an application version.

        - **ApplicationVersionArn** *(string) --*

          The Amazon Resource Name (ARN) of the application version.

        - **ApplicationName** *(string) --*

          The name of the application to which the application version belongs.

        - **Description** *(string) --*

          The description of the application version.

        - **VersionLabel** *(string) --*

          A unique identifier for the application version.

        - **SourceBuildInformation** *(dict) --*

          If the version's source code was retrieved from AWS CodeCommit, the location of the
          source code for the application version.

          - **SourceType** *(string) --*

            The type of repository.

            * ``Git``

            * ``Zip``

          - **SourceRepository** *(string) --*

            Location where the repository is stored.

            * ``CodeCommit``

            * ``S3``

          - **SourceLocation** *(string) --*

            The location of the source code, as a formatted string, depending on the value of
            ``SourceRepository``

            * For ``CodeCommit`` , the format is the repository name and commit ID, separated by a
            forward slash. For example, ``my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a`` .

            * For ``S3`` , the format is the S3 bucket name and object key, separated by a forward
            slash. For example, ``my-s3-bucket/Folders/my-source-file`` .

        - **BuildArn** *(string) --*

          Reference to the artifact from the AWS CodeBuild build.

        - **SourceBundle** *(dict) --*

          The storage location of the application version's source bundle in Amazon S3.

          - **S3Bucket** *(string) --*

            The Amazon S3 bucket where the data is located.

          - **S3Key** *(string) --*

            The Amazon S3 key where the data is located.

        - **DateCreated** *(datetime) --*

          The creation date of the application version.

        - **DateUpdated** *(datetime) --*

          The last modified date of the application version.

        - **Status** *(string) --*

          The processing status of the application version. Reflects the state of the application
          version during its creation. Many of the values are only applicable if you specified
          ``True`` for the ``Process`` parameter of the ``CreateApplicationVersion`` action. The
          following list describes the possible values.

          * ``Unprocessed`` – Application version wasn't pre-processed or validated. Elastic
          Beanstalk will validate configuration files during deployment of the application version
          to an environment.

          * ``Processing`` – Elastic Beanstalk is currently processing the application version.

          * ``Building`` – Application version is currently undergoing an AWS CodeBuild build.

          * ``Processed`` – Elastic Beanstalk was successfully pre-processed and validated.

          * ``Failed`` – Either the AWS CodeBuild build failed or configuration files didn't pass
          validation. This application version isn't usable.
    """


_DescribeEnvironmentManagedActionHistoryPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEnvironmentManagedActionHistoryPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEnvironmentManagedActionHistoryPaginatePaginationConfigTypeDef(
    _DescribeEnvironmentManagedActionHistoryPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeEnvironmentManagedActionHistoryPaginate` `PaginationConfig`

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


_DescribeEnvironmentManagedActionHistoryPaginateResponseManagedActionHistoryItemsTypeDef = TypedDict(
    "_DescribeEnvironmentManagedActionHistoryPaginateResponseManagedActionHistoryItemsTypeDef",
    {
        "ActionId": str,
        "ActionType": str,
        "ActionDescription": str,
        "FailureType": str,
        "Status": str,
        "FailureDescription": str,
        "ExecutedTime": datetime,
        "FinishedTime": datetime,
    },
    total=False,
)


class DescribeEnvironmentManagedActionHistoryPaginateResponseManagedActionHistoryItemsTypeDef(
    _DescribeEnvironmentManagedActionHistoryPaginateResponseManagedActionHistoryItemsTypeDef
):
    """
    Type definition for `DescribeEnvironmentManagedActionHistoryPaginateResponse` `ManagedActionHistoryItems`

    The record of a completed or failed managed action.

    - **ActionId** *(string) --*

      A unique identifier for the managed action.

    - **ActionType** *(string) --*

      The type of the managed action.

    - **ActionDescription** *(string) --*

      A description of the managed action.

    - **FailureType** *(string) --*

      If the action failed, the type of failure.

    - **Status** *(string) --*

      The status of the action.

    - **FailureDescription** *(string) --*

      If the action failed, a description of the failure.

    - **ExecutedTime** *(datetime) --*

      The date and time that the action started executing.

    - **FinishedTime** *(datetime) --*

      The date and time that the action finished executing.
    """


_DescribeEnvironmentManagedActionHistoryPaginateResponseTypeDef = TypedDict(
    "_DescribeEnvironmentManagedActionHistoryPaginateResponseTypeDef",
    {
        "ManagedActionHistoryItems": List[
            DescribeEnvironmentManagedActionHistoryPaginateResponseManagedActionHistoryItemsTypeDef
        ]
    },
    total=False,
)


class DescribeEnvironmentManagedActionHistoryPaginateResponseTypeDef(
    _DescribeEnvironmentManagedActionHistoryPaginateResponseTypeDef
):
    """
    Type definition for `DescribeEnvironmentManagedActionHistoryPaginate` `Response`

    A result message containing a list of completed and failed managed actions.

    - **ManagedActionHistoryItems** *(list) --*

      A list of completed and failed managed actions.

      - *(dict) --*

        The record of a completed or failed managed action.

        - **ActionId** *(string) --*

          A unique identifier for the managed action.

        - **ActionType** *(string) --*

          The type of the managed action.

        - **ActionDescription** *(string) --*

          A description of the managed action.

        - **FailureType** *(string) --*

          If the action failed, the type of failure.

        - **Status** *(string) --*

          The status of the action.

        - **FailureDescription** *(string) --*

          If the action failed, a description of the failure.

        - **ExecutedTime** *(datetime) --*

          The date and time that the action started executing.

        - **FinishedTime** *(datetime) --*

          The date and time that the action finished executing.
    """


_DescribeEnvironmentsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEnvironmentsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEnvironmentsPaginatePaginationConfigTypeDef(
    _DescribeEnvironmentsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeEnvironmentsPaginate` `PaginationConfig`

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


_DescribeEnvironmentsPaginateResponseEnvironmentsEnvironmentLinksTypeDef = TypedDict(
    "_DescribeEnvironmentsPaginateResponseEnvironmentsEnvironmentLinksTypeDef",
    {"LinkName": str, "EnvironmentName": str},
    total=False,
)


class DescribeEnvironmentsPaginateResponseEnvironmentsEnvironmentLinksTypeDef(
    _DescribeEnvironmentsPaginateResponseEnvironmentsEnvironmentLinksTypeDef
):
    """
    Type definition for `DescribeEnvironmentsPaginateResponseEnvironments` `EnvironmentLinks`

    A link to another environment, defined in the environment's manifest. Links provide
    connection information in system properties that can be used to connect to another
    environment in the same group. See `Environment Manifest (env.yaml)
    <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__
    for details.

    - **LinkName** *(string) --*

      The name of the link.

    - **EnvironmentName** *(string) --*

      The name of the linked environment (the dependency).
    """


_DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerListenersTypeDef = TypedDict(
    "_DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerListenersTypeDef",
    {"Protocol": str, "Port": int},
    total=False,
)


class DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerListenersTypeDef(
    _DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerListenersTypeDef
):
    """
    Type definition for `DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancer` `Listeners`

    Describes the properties of a Listener for the LoadBalancer.

    - **Protocol** *(string) --*

      The protocol that is used by the Listener.

    - **Port** *(integer) --*

      The port that is used by the Listener.
    """


_DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerTypeDef = TypedDict(
    "_DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List[
            DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerListenersTypeDef
        ],
    },
    total=False,
)


class DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerTypeDef(
    _DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerTypeDef
):
    """
    Type definition for `DescribeEnvironmentsPaginateResponseEnvironmentsResources` `LoadBalancer`

    Describes the LoadBalancer.

    - **LoadBalancerName** *(string) --*

      The name of the LoadBalancer.

    - **Domain** *(string) --*

      The domain name of the LoadBalancer.

    - **Listeners** *(list) --*

      A list of Listeners used by the LoadBalancer.

      - *(dict) --*

        Describes the properties of a Listener for the LoadBalancer.

        - **Protocol** *(string) --*

          The protocol that is used by the Listener.

        - **Port** *(integer) --*

          The port that is used by the Listener.
    """


_DescribeEnvironmentsPaginateResponseEnvironmentsResourcesTypeDef = TypedDict(
    "_DescribeEnvironmentsPaginateResponseEnvironmentsResourcesTypeDef",
    {
        "LoadBalancer": DescribeEnvironmentsPaginateResponseEnvironmentsResourcesLoadBalancerTypeDef
    },
    total=False,
)


class DescribeEnvironmentsPaginateResponseEnvironmentsResourcesTypeDef(
    _DescribeEnvironmentsPaginateResponseEnvironmentsResourcesTypeDef
):
    """
    Type definition for `DescribeEnvironmentsPaginateResponseEnvironments` `Resources`

    The description of the AWS resources used by this environment.

    - **LoadBalancer** *(dict) --*

      Describes the LoadBalancer.

      - **LoadBalancerName** *(string) --*

        The name of the LoadBalancer.

      - **Domain** *(string) --*

        The domain name of the LoadBalancer.

      - **Listeners** *(list) --*

        A list of Listeners used by the LoadBalancer.

        - *(dict) --*

          Describes the properties of a Listener for the LoadBalancer.

          - **Protocol** *(string) --*

            The protocol that is used by the Listener.

          - **Port** *(integer) --*

            The port that is used by the Listener.
    """


_DescribeEnvironmentsPaginateResponseEnvironmentsTierTypeDef = TypedDict(
    "_DescribeEnvironmentsPaginateResponseEnvironmentsTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)


class DescribeEnvironmentsPaginateResponseEnvironmentsTierTypeDef(
    _DescribeEnvironmentsPaginateResponseEnvironmentsTierTypeDef
):
    """
    Type definition for `DescribeEnvironmentsPaginateResponseEnvironments` `Tier`

    Describes the current tier of this environment.

    - **Name** *(string) --*

      The name of this environment tier.

      Valid values:

      * For *Web server tier* – ``WebServer``

      * For *Worker tier* – ``Worker``

    - **Type** *(string) --*

      The type of this environment tier.

      Valid values:

      * For *Web server tier* – ``Standard``

      * For *Worker tier* – ``SQS/HTTP``

    - **Version** *(string) --*

      The version of this environment tier. When you don't set a value to it, Elastic
      Beanstalk uses the latest compatible worker tier version.

      .. note::

        This member is deprecated. Any specific version that you set may become out of date.
        We recommend leaving it unspecified.
    """


_DescribeEnvironmentsPaginateResponseEnvironmentsTypeDef = TypedDict(
    "_DescribeEnvironmentsPaginateResponseEnvironmentsTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": str,
        "AbortableOperationInProgress": bool,
        "Health": str,
        "HealthStatus": str,
        "Resources": DescribeEnvironmentsPaginateResponseEnvironmentsResourcesTypeDef,
        "Tier": DescribeEnvironmentsPaginateResponseEnvironmentsTierTypeDef,
        "EnvironmentLinks": List[
            DescribeEnvironmentsPaginateResponseEnvironmentsEnvironmentLinksTypeDef
        ],
        "EnvironmentArn": str,
    },
    total=False,
)


class DescribeEnvironmentsPaginateResponseEnvironmentsTypeDef(
    _DescribeEnvironmentsPaginateResponseEnvironmentsTypeDef
):
    """
    Type definition for `DescribeEnvironmentsPaginateResponse` `Environments`

    Describes the properties of an environment.

    - **EnvironmentName** *(string) --*

      The name of this environment.

    - **EnvironmentId** *(string) --*

      The ID of this environment.

    - **ApplicationName** *(string) --*

      The name of the application associated with this environment.

    - **VersionLabel** *(string) --*

      The application version deployed in this environment.

    - **SolutionStackName** *(string) --*

      The name of the ``SolutionStack`` deployed with this environment.

    - **PlatformArn** *(string) --*

      The ARN of the platform.

    - **TemplateName** *(string) --*

      The name of the configuration template used to originally launch this environment.

    - **Description** *(string) --*

      Describes this environment.

    - **EndpointURL** *(string) --*

      For load-balanced, autoscaling environments, the URL to the LoadBalancer. For
      single-instance environments, the IP address of the instance.

    - **CNAME** *(string) --*

      The URL to the CNAME for this environment.

    - **DateCreated** *(datetime) --*

      The creation date for this environment.

    - **DateUpdated** *(datetime) --*

      The last modified date for this environment.

    - **Status** *(string) --*

      The current operational status of the environment:

      * ``Launching`` : Environment is in the process of initial deployment.

      * ``Updating`` : Environment is in the process of updating its configuration settings or
      application version.

      * ``Ready`` : Environment is available to have an action performed on it, such as update
      or terminate.

      * ``Terminating`` : Environment is in the shut-down process.

      * ``Terminated`` : Environment is not running.

    - **AbortableOperationInProgress** *(boolean) --*

      Indicates if there is an in-progress environment configuration update or application
      version deployment that you can cancel.

       ``true:`` There is an update in progress.

       ``false:`` There are no updates currently in progress.

    - **Health** *(string) --*

      Describes the health status of the environment. AWS Elastic Beanstalk indicates the
      failure levels for a running environment:

      * ``Red`` : Indicates the environment is not responsive. Occurs when three or more
      consecutive failures occur for an environment.

      * ``Yellow`` : Indicates that something is wrong. Occurs when two consecutive failures
      occur for an environment.

      * ``Green`` : Indicates the environment is healthy and fully functional.

      * ``Grey`` : Default health for a new environment. The environment is not fully launched
      and health checks have not started or health checks are suspended during an
      ``UpdateEnvironment`` or ``RestartEnvironment`` request.

      Default: ``Grey``

    - **HealthStatus** *(string) --*

      Returns the health status of the application running in your environment. For more
      information, see `Health Colors and Statuses
      <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

    - **Resources** *(dict) --*

      The description of the AWS resources used by this environment.

      - **LoadBalancer** *(dict) --*

        Describes the LoadBalancer.

        - **LoadBalancerName** *(string) --*

          The name of the LoadBalancer.

        - **Domain** *(string) --*

          The domain name of the LoadBalancer.

        - **Listeners** *(list) --*

          A list of Listeners used by the LoadBalancer.

          - *(dict) --*

            Describes the properties of a Listener for the LoadBalancer.

            - **Protocol** *(string) --*

              The protocol that is used by the Listener.

            - **Port** *(integer) --*

              The port that is used by the Listener.

    - **Tier** *(dict) --*

      Describes the current tier of this environment.

      - **Name** *(string) --*

        The name of this environment tier.

        Valid values:

        * For *Web server tier* – ``WebServer``

        * For *Worker tier* – ``Worker``

      - **Type** *(string) --*

        The type of this environment tier.

        Valid values:

        * For *Web server tier* – ``Standard``

        * For *Worker tier* – ``SQS/HTTP``

      - **Version** *(string) --*

        The version of this environment tier. When you don't set a value to it, Elastic
        Beanstalk uses the latest compatible worker tier version.

        .. note::

          This member is deprecated. Any specific version that you set may become out of date.
          We recommend leaving it unspecified.

    - **EnvironmentLinks** *(list) --*

      A list of links to other environments in the same group.

      - *(dict) --*

        A link to another environment, defined in the environment's manifest. Links provide
        connection information in system properties that can be used to connect to another
        environment in the same group. See `Environment Manifest (env.yaml)
        <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__
        for details.

        - **LinkName** *(string) --*

          The name of the link.

        - **EnvironmentName** *(string) --*

          The name of the linked environment (the dependency).

    - **EnvironmentArn** *(string) --*

      The environment's Amazon Resource Name (ARN), which can be used in other API requests
      that require an ARN.
    """


_DescribeEnvironmentsPaginateResponseTypeDef = TypedDict(
    "_DescribeEnvironmentsPaginateResponseTypeDef",
    {"Environments": List[DescribeEnvironmentsPaginateResponseEnvironmentsTypeDef]},
    total=False,
)


class DescribeEnvironmentsPaginateResponseTypeDef(
    _DescribeEnvironmentsPaginateResponseTypeDef
):
    """
    Type definition for `DescribeEnvironmentsPaginate` `Response`

    Result message containing a list of environment descriptions.

    - **Environments** *(list) --*

      Returns an  EnvironmentDescription list.

      - *(dict) --*

        Describes the properties of an environment.

        - **EnvironmentName** *(string) --*

          The name of this environment.

        - **EnvironmentId** *(string) --*

          The ID of this environment.

        - **ApplicationName** *(string) --*

          The name of the application associated with this environment.

        - **VersionLabel** *(string) --*

          The application version deployed in this environment.

        - **SolutionStackName** *(string) --*

          The name of the ``SolutionStack`` deployed with this environment.

        - **PlatformArn** *(string) --*

          The ARN of the platform.

        - **TemplateName** *(string) --*

          The name of the configuration template used to originally launch this environment.

        - **Description** *(string) --*

          Describes this environment.

        - **EndpointURL** *(string) --*

          For load-balanced, autoscaling environments, the URL to the LoadBalancer. For
          single-instance environments, the IP address of the instance.

        - **CNAME** *(string) --*

          The URL to the CNAME for this environment.

        - **DateCreated** *(datetime) --*

          The creation date for this environment.

        - **DateUpdated** *(datetime) --*

          The last modified date for this environment.

        - **Status** *(string) --*

          The current operational status of the environment:

          * ``Launching`` : Environment is in the process of initial deployment.

          * ``Updating`` : Environment is in the process of updating its configuration settings or
          application version.

          * ``Ready`` : Environment is available to have an action performed on it, such as update
          or terminate.

          * ``Terminating`` : Environment is in the shut-down process.

          * ``Terminated`` : Environment is not running.

        - **AbortableOperationInProgress** *(boolean) --*

          Indicates if there is an in-progress environment configuration update or application
          version deployment that you can cancel.

           ``true:`` There is an update in progress.

           ``false:`` There are no updates currently in progress.

        - **Health** *(string) --*

          Describes the health status of the environment. AWS Elastic Beanstalk indicates the
          failure levels for a running environment:

          * ``Red`` : Indicates the environment is not responsive. Occurs when three or more
          consecutive failures occur for an environment.

          * ``Yellow`` : Indicates that something is wrong. Occurs when two consecutive failures
          occur for an environment.

          * ``Green`` : Indicates the environment is healthy and fully functional.

          * ``Grey`` : Default health for a new environment. The environment is not fully launched
          and health checks have not started or health checks are suspended during an
          ``UpdateEnvironment`` or ``RestartEnvironment`` request.

          Default: ``Grey``

        - **HealthStatus** *(string) --*

          Returns the health status of the application running in your environment. For more
          information, see `Health Colors and Statuses
          <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html>`__ .

        - **Resources** *(dict) --*

          The description of the AWS resources used by this environment.

          - **LoadBalancer** *(dict) --*

            Describes the LoadBalancer.

            - **LoadBalancerName** *(string) --*

              The name of the LoadBalancer.

            - **Domain** *(string) --*

              The domain name of the LoadBalancer.

            - **Listeners** *(list) --*

              A list of Listeners used by the LoadBalancer.

              - *(dict) --*

                Describes the properties of a Listener for the LoadBalancer.

                - **Protocol** *(string) --*

                  The protocol that is used by the Listener.

                - **Port** *(integer) --*

                  The port that is used by the Listener.

        - **Tier** *(dict) --*

          Describes the current tier of this environment.

          - **Name** *(string) --*

            The name of this environment tier.

            Valid values:

            * For *Web server tier* – ``WebServer``

            * For *Worker tier* – ``Worker``

          - **Type** *(string) --*

            The type of this environment tier.

            Valid values:

            * For *Web server tier* – ``Standard``

            * For *Worker tier* – ``SQS/HTTP``

          - **Version** *(string) --*

            The version of this environment tier. When you don't set a value to it, Elastic
            Beanstalk uses the latest compatible worker tier version.

            .. note::

              This member is deprecated. Any specific version that you set may become out of date.
              We recommend leaving it unspecified.

        - **EnvironmentLinks** *(list) --*

          A list of links to other environments in the same group.

          - *(dict) --*

            A link to another environment, defined in the environment's manifest. Links provide
            connection information in system properties that can be used to connect to another
            environment in the same group. See `Environment Manifest (env.yaml)
            <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html>`__
            for details.

            - **LinkName** *(string) --*

              The name of the link.

            - **EnvironmentName** *(string) --*

              The name of the linked environment (the dependency).

        - **EnvironmentArn** *(string) --*

          The environment's Amazon Resource Name (ARN), which can be used in other API requests
          that require an ARN.
    """


_DescribeEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEventsPaginatePaginationConfigTypeDef(
    _DescribeEventsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeEventsPaginate` `PaginationConfig`

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


_DescribeEventsPaginateResponseEventsTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseEventsTypeDef",
    {
        "EventDate": datetime,
        "Message": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "TemplateName": str,
        "EnvironmentName": str,
        "PlatformArn": str,
        "RequestId": str,
        "Severity": str,
    },
    total=False,
)


class DescribeEventsPaginateResponseEventsTypeDef(
    _DescribeEventsPaginateResponseEventsTypeDef
):
    """
    Type definition for `DescribeEventsPaginateResponse` `Events`

    Describes an event.

    - **EventDate** *(datetime) --*

      The date when the event occurred.

    - **Message** *(string) --*

      The event message.

    - **ApplicationName** *(string) --*

      The application associated with the event.

    - **VersionLabel** *(string) --*

      The release label for the application version associated with this event.

    - **TemplateName** *(string) --*

      The name of the configuration associated with this event.

    - **EnvironmentName** *(string) --*

      The name of the environment associated with this event.

    - **PlatformArn** *(string) --*

      The ARN of the platform.

    - **RequestId** *(string) --*

      The web service request ID for the activity of this event.

    - **Severity** *(string) --*

      The severity level of this event.
    """


_DescribeEventsPaginateResponseTypeDef = TypedDict(
    "_DescribeEventsPaginateResponseTypeDef",
    {"Events": List[DescribeEventsPaginateResponseEventsTypeDef]},
    total=False,
)


class DescribeEventsPaginateResponseTypeDef(_DescribeEventsPaginateResponseTypeDef):
    """
    Type definition for `DescribeEventsPaginate` `Response`

    Result message wrapping a list of event descriptions.

    - **Events** *(list) --*

      A list of  EventDescription .

      - *(dict) --*

        Describes an event.

        - **EventDate** *(datetime) --*

          The date when the event occurred.

        - **Message** *(string) --*

          The event message.

        - **ApplicationName** *(string) --*

          The application associated with the event.

        - **VersionLabel** *(string) --*

          The release label for the application version associated with this event.

        - **TemplateName** *(string) --*

          The name of the configuration associated with this event.

        - **EnvironmentName** *(string) --*

          The name of the environment associated with this event.

        - **PlatformArn** *(string) --*

          The ARN of the platform.

        - **RequestId** *(string) --*

          The web service request ID for the activity of this event.

        - **Severity** *(string) --*

          The severity level of this event.
    """


_ListPlatformVersionsPaginateFiltersTypeDef = TypedDict(
    "_ListPlatformVersionsPaginateFiltersTypeDef",
    {"Type": str, "Operator": str, "Values": List[str]},
    total=False,
)


class ListPlatformVersionsPaginateFiltersTypeDef(
    _ListPlatformVersionsPaginateFiltersTypeDef
):
    """
    Type definition for `ListPlatformVersionsPaginate` `Filters`

    Specify criteria to restrict the results when listing custom platforms.

    The filter is evaluated as the expression:

     ``Type``  ``Operator``  ``Values[i]``

    - **Type** *(string) --*

      The custom platform attribute to which the filter values are applied.

      Valid Values: ``PlatformName`` | ``PlatformVersion`` | ``PlatformStatus`` | ``PlatformOwner``

    - **Operator** *(string) --*

      The operator to apply to the ``Type`` with each of the ``Values`` .

      Valid Values: ``=`` (equal to) | ``!=`` (not equal to) | ``<`` (less than) | ``<=`` (less
      than or equal to) | ``>`` (greater than) | ``>=`` (greater than or equal to) | ``contains`` |
      ``begins_with`` | ``ends_with``

    - **Values** *(list) --*

      The list of values applied to the custom platform attribute.

      - *(string) --*
    """


_ListPlatformVersionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPlatformVersionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPlatformVersionsPaginatePaginationConfigTypeDef(
    _ListPlatformVersionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPlatformVersionsPaginate` `PaginationConfig`

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


_ListPlatformVersionsPaginateResponsePlatformSummaryListTypeDef = TypedDict(
    "_ListPlatformVersionsPaginateResponsePlatformSummaryListTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformStatus": str,
        "PlatformCategory": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
    },
    total=False,
)


class ListPlatformVersionsPaginateResponsePlatformSummaryListTypeDef(
    _ListPlatformVersionsPaginateResponsePlatformSummaryListTypeDef
):
    """
    Type definition for `ListPlatformVersionsPaginateResponse` `PlatformSummaryList`

    Detailed information about a platform.

    - **PlatformArn** *(string) --*

      The ARN of the platform.

    - **PlatformOwner** *(string) --*

      The AWS account ID of the person who created the platform.

    - **PlatformStatus** *(string) --*

      The status of the platform. You can create an environment from the platform once it is
      ready.

    - **PlatformCategory** *(string) --*

      The category of platform.

    - **OperatingSystemName** *(string) --*

      The operating system used by the platform.

    - **OperatingSystemVersion** *(string) --*

      The version of the operating system used by the platform.

    - **SupportedTierList** *(list) --*

      The tiers in which the platform runs.

      - *(string) --*

    - **SupportedAddonList** *(list) --*

      The additions associated with the platform.

      - *(string) --*
    """


_ListPlatformVersionsPaginateResponseTypeDef = TypedDict(
    "_ListPlatformVersionsPaginateResponseTypeDef",
    {
        "PlatformSummaryList": List[
            ListPlatformVersionsPaginateResponsePlatformSummaryListTypeDef
        ]
    },
    total=False,
)


class ListPlatformVersionsPaginateResponseTypeDef(
    _ListPlatformVersionsPaginateResponseTypeDef
):
    """
    Type definition for `ListPlatformVersionsPaginate` `Response`

    - **PlatformSummaryList** *(list) --*

      Detailed information about the platforms.

      - *(dict) --*

        Detailed information about a platform.

        - **PlatformArn** *(string) --*

          The ARN of the platform.

        - **PlatformOwner** *(string) --*

          The AWS account ID of the person who created the platform.

        - **PlatformStatus** *(string) --*

          The status of the platform. You can create an environment from the platform once it is
          ready.

        - **PlatformCategory** *(string) --*

          The category of platform.

        - **OperatingSystemName** *(string) --*

          The operating system used by the platform.

        - **OperatingSystemVersion** *(string) --*

          The version of the operating system used by the platform.

        - **SupportedTierList** *(list) --*

          The tiers in which the platform runs.

          - *(string) --*

        - **SupportedAddonList** *(list) --*

          The additions associated with the platform.

          - *(string) --*
    """

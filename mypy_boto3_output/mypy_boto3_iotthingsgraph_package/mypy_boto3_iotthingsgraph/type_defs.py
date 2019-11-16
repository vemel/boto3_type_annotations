"Main interface for iotthingsgraph type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateFlowTemplateResponsesummaryTypeDef",
    "ClientCreateFlowTemplateResponseTypeDef",
    "ClientCreateFlowTemplatedefinitionTypeDef",
    "ClientCreateSystemInstanceResponsesummaryTypeDef",
    "ClientCreateSystemInstanceResponseTypeDef",
    "ClientCreateSystemInstancedefinitionTypeDef",
    "ClientCreateSystemInstancemetricsConfigurationTypeDef",
    "ClientCreateSystemInstancetagsTypeDef",
    "ClientCreateSystemTemplateResponsesummaryTypeDef",
    "ClientCreateSystemTemplateResponseTypeDef",
    "ClientCreateSystemTemplatedefinitionTypeDef",
    "ClientDeleteNamespaceResponseTypeDef",
    "ClientDeploySystemInstanceResponsesummaryTypeDef",
    "ClientDeploySystemInstanceResponseTypeDef",
    "ClientDescribeNamespaceResponseTypeDef",
    "ClientGetEntitiesResponsedescriptionsdefinitionTypeDef",
    "ClientGetEntitiesResponsedescriptionsTypeDef",
    "ClientGetEntitiesResponseTypeDef",
    "ClientGetFlowTemplateResponsedescriptiondefinitionTypeDef",
    "ClientGetFlowTemplateResponsedescriptionsummaryTypeDef",
    "ClientGetFlowTemplateResponsedescriptionTypeDef",
    "ClientGetFlowTemplateResponseTypeDef",
    "ClientGetFlowTemplateRevisionsResponsesummariesTypeDef",
    "ClientGetFlowTemplateRevisionsResponseTypeDef",
    "ClientGetNamespaceDeletionStatusResponseTypeDef",
    "ClientGetSystemInstanceResponsedescriptiondefinitionTypeDef",
    "ClientGetSystemInstanceResponsedescriptionmetricsConfigurationTypeDef",
    "ClientGetSystemInstanceResponsedescriptionsummaryTypeDef",
    "ClientGetSystemInstanceResponsedescriptionvalidatedDependencyRevisionsTypeDef",
    "ClientGetSystemInstanceResponsedescriptionTypeDef",
    "ClientGetSystemInstanceResponseTypeDef",
    "ClientGetSystemTemplateResponsedescriptiondefinitionTypeDef",
    "ClientGetSystemTemplateResponsedescriptionsummaryTypeDef",
    "ClientGetSystemTemplateResponsedescriptionTypeDef",
    "ClientGetSystemTemplateResponseTypeDef",
    "ClientGetSystemTemplateRevisionsResponsesummariesTypeDef",
    "ClientGetSystemTemplateRevisionsResponseTypeDef",
    "ClientGetUploadStatusResponseTypeDef",
    "ClientListFlowExecutionMessagesResponsemessagesTypeDef",
    "ClientListFlowExecutionMessagesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientSearchEntitiesResponsedescriptionsdefinitionTypeDef",
    "ClientSearchEntitiesResponsedescriptionsTypeDef",
    "ClientSearchEntitiesResponseTypeDef",
    "ClientSearchEntitiesfiltersTypeDef",
    "ClientSearchFlowExecutionsResponsesummariesTypeDef",
    "ClientSearchFlowExecutionsResponseTypeDef",
    "ClientSearchFlowTemplatesResponsesummariesTypeDef",
    "ClientSearchFlowTemplatesResponseTypeDef",
    "ClientSearchFlowTemplatesfiltersTypeDef",
    "ClientSearchSystemInstancesResponsesummariesTypeDef",
    "ClientSearchSystemInstancesResponseTypeDef",
    "ClientSearchSystemInstancesfiltersTypeDef",
    "ClientSearchSystemTemplatesResponsesummariesTypeDef",
    "ClientSearchSystemTemplatesResponseTypeDef",
    "ClientSearchSystemTemplatesfiltersTypeDef",
    "ClientSearchThingsResponsethingsTypeDef",
    "ClientSearchThingsResponseTypeDef",
    "ClientTagResourcetagsTypeDef",
    "ClientUndeploySystemInstanceResponsesummaryTypeDef",
    "ClientUndeploySystemInstanceResponseTypeDef",
    "ClientUpdateFlowTemplateResponsesummaryTypeDef",
    "ClientUpdateFlowTemplateResponseTypeDef",
    "ClientUpdateFlowTemplatedefinitionTypeDef",
    "ClientUpdateSystemTemplateResponsesummaryTypeDef",
    "ClientUpdateSystemTemplateResponseTypeDef",
    "ClientUpdateSystemTemplatedefinitionTypeDef",
    "ClientUploadEntityDefinitionsResponseTypeDef",
    "ClientUploadEntityDefinitionsdocumentTypeDef",
    "GetFlowTemplateRevisionsPaginatePaginationConfigTypeDef",
    "GetFlowTemplateRevisionsPaginateResponsesummariesTypeDef",
    "GetFlowTemplateRevisionsPaginateResponseTypeDef",
    "GetSystemTemplateRevisionsPaginatePaginationConfigTypeDef",
    "GetSystemTemplateRevisionsPaginateResponsesummariesTypeDef",
    "GetSystemTemplateRevisionsPaginateResponseTypeDef",
    "ListFlowExecutionMessagesPaginatePaginationConfigTypeDef",
    "ListFlowExecutionMessagesPaginateResponsemessagesTypeDef",
    "ListFlowExecutionMessagesPaginateResponseTypeDef",
    "ListTagsForResourcePaginatePaginationConfigTypeDef",
    "ListTagsForResourcePaginateResponsetagsTypeDef",
    "ListTagsForResourcePaginateResponseTypeDef",
    "SearchEntitiesPaginatePaginationConfigTypeDef",
    "SearchEntitiesPaginateResponsedescriptionsdefinitionTypeDef",
    "SearchEntitiesPaginateResponsedescriptionsTypeDef",
    "SearchEntitiesPaginateResponseTypeDef",
    "SearchEntitiesPaginatefiltersTypeDef",
    "SearchFlowExecutionsPaginatePaginationConfigTypeDef",
    "SearchFlowExecutionsPaginateResponsesummariesTypeDef",
    "SearchFlowExecutionsPaginateResponseTypeDef",
    "SearchFlowTemplatesPaginatePaginationConfigTypeDef",
    "SearchFlowTemplatesPaginateResponsesummariesTypeDef",
    "SearchFlowTemplatesPaginateResponseTypeDef",
    "SearchFlowTemplatesPaginatefiltersTypeDef",
    "SearchSystemInstancesPaginatePaginationConfigTypeDef",
    "SearchSystemInstancesPaginateResponsesummariesTypeDef",
    "SearchSystemInstancesPaginateResponseTypeDef",
    "SearchSystemInstancesPaginatefiltersTypeDef",
    "SearchSystemTemplatesPaginatePaginationConfigTypeDef",
    "SearchSystemTemplatesPaginateResponsesummariesTypeDef",
    "SearchSystemTemplatesPaginateResponseTypeDef",
    "SearchSystemTemplatesPaginatefiltersTypeDef",
    "SearchThingsPaginatePaginationConfigTypeDef",
    "SearchThingsPaginateResponsethingsTypeDef",
    "SearchThingsPaginateResponseTypeDef",
)


_ClientCreateFlowTemplateResponsesummaryTypeDef = TypedDict(
    "_ClientCreateFlowTemplateResponsesummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientCreateFlowTemplateResponsesummaryTypeDef(
    _ClientCreateFlowTemplateResponsesummaryTypeDef
):
    """
    Type definition for `ClientCreateFlowTemplateResponse` `summary`

    The summary object that describes the created workflow.

    - **id** *(string) --*

      The ID of the workflow.

    - **arn** *(string) --*

      The ARN of the workflow.

    - **revisionNumber** *(integer) --*

      The revision number of the workflow.

    - **createdAt** *(datetime) --*

      The date when the workflow was created.
    """


_ClientCreateFlowTemplateResponseTypeDef = TypedDict(
    "_ClientCreateFlowTemplateResponseTypeDef",
    {"summary": ClientCreateFlowTemplateResponsesummaryTypeDef},
    total=False,
)


class ClientCreateFlowTemplateResponseTypeDef(_ClientCreateFlowTemplateResponseTypeDef):
    """
    Type definition for `ClientCreateFlowTemplate` `Response`

    - **summary** *(dict) --*

      The summary object that describes the created workflow.

      - **id** *(string) --*

        The ID of the workflow.

      - **arn** *(string) --*

        The ARN of the workflow.

      - **revisionNumber** *(integer) --*

        The revision number of the workflow.

      - **createdAt** *(datetime) --*

        The date when the workflow was created.
    """


_ClientCreateFlowTemplatedefinitionTypeDef = TypedDict(
    "_ClientCreateFlowTemplatedefinitionTypeDef", {"language": str, "text": str}
)


class ClientCreateFlowTemplatedefinitionTypeDef(
    _ClientCreateFlowTemplatedefinitionTypeDef
):
    """
    Type definition for `ClientCreateFlowTemplate` `definition`

    The workflow ``DefinitionDocument`` .

    - **language** *(string) --* **[REQUIRED]**

      The language used to define the entity. ``GRAPHQL`` is the only valid value.

    - **text** *(string) --* **[REQUIRED]**

      The GraphQL text that defines the entity.
    """


_ClientCreateSystemInstanceResponsesummaryTypeDef = TypedDict(
    "_ClientCreateSystemInstanceResponsesummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "status": str,
        "target": str,
        "greengrassGroupName": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "greengrassGroupId": str,
        "greengrassGroupVersionId": str,
    },
    total=False,
)


class ClientCreateSystemInstanceResponsesummaryTypeDef(
    _ClientCreateSystemInstanceResponsesummaryTypeDef
):
    """
    Type definition for `ClientCreateSystemInstanceResponse` `summary`

    The summary object that describes the new system instance.

    - **id** *(string) --*

      The ID of the system instance.

    - **arn** *(string) --*

      The ARN of the system instance.

    - **status** *(string) --*

      The status of the system instance.

    - **target** *(string) --*

      The target of the system instance.

    - **greengrassGroupName** *(string) --*

      The ID of the Greengrass group where the system instance is deployed.

    - **createdAt** *(datetime) --*

      The date when the system instance was created.

    - **updatedAt** *(datetime) --*

      The date and time when the system instance was last updated.

    - **greengrassGroupId** *(string) --*

      The ID of the Greengrass group where the system instance is deployed.

    - **greengrassGroupVersionId** *(string) --*

      The version of the Greengrass group where the system instance is deployed.
    """


_ClientCreateSystemInstanceResponseTypeDef = TypedDict(
    "_ClientCreateSystemInstanceResponseTypeDef",
    {"summary": ClientCreateSystemInstanceResponsesummaryTypeDef},
    total=False,
)


class ClientCreateSystemInstanceResponseTypeDef(
    _ClientCreateSystemInstanceResponseTypeDef
):
    """
    Type definition for `ClientCreateSystemInstance` `Response`

    - **summary** *(dict) --*

      The summary object that describes the new system instance.

      - **id** *(string) --*

        The ID of the system instance.

      - **arn** *(string) --*

        The ARN of the system instance.

      - **status** *(string) --*

        The status of the system instance.

      - **target** *(string) --*

        The target of the system instance.

      - **greengrassGroupName** *(string) --*

        The ID of the Greengrass group where the system instance is deployed.

      - **createdAt** *(datetime) --*

        The date when the system instance was created.

      - **updatedAt** *(datetime) --*

        The date and time when the system instance was last updated.

      - **greengrassGroupId** *(string) --*

        The ID of the Greengrass group where the system instance is deployed.

      - **greengrassGroupVersionId** *(string) --*

        The version of the Greengrass group where the system instance is deployed.
    """


_ClientCreateSystemInstancedefinitionTypeDef = TypedDict(
    "_ClientCreateSystemInstancedefinitionTypeDef", {"language": str, "text": str}
)


class ClientCreateSystemInstancedefinitionTypeDef(
    _ClientCreateSystemInstancedefinitionTypeDef
):
    """
    Type definition for `ClientCreateSystemInstance` `definition`

    A document that defines an entity.

    - **language** *(string) --* **[REQUIRED]**

      The language used to define the entity. ``GRAPHQL`` is the only valid value.

    - **text** *(string) --* **[REQUIRED]**

      The GraphQL text that defines the entity.
    """


_ClientCreateSystemInstancemetricsConfigurationTypeDef = TypedDict(
    "_ClientCreateSystemInstancemetricsConfigurationTypeDef",
    {"cloudMetricEnabled": bool, "metricRuleRoleArn": str},
    total=False,
)


class ClientCreateSystemInstancemetricsConfigurationTypeDef(
    _ClientCreateSystemInstancemetricsConfigurationTypeDef
):
    """
    Type definition for `ClientCreateSystemInstance` `metricsConfiguration`

    An object that specifies whether cloud metrics are collected in a deployment and, if so, what
    role is used to collect metrics.

    - **cloudMetricEnabled** *(boolean) --*

      A Boolean that specifies whether cloud metrics are collected.

    - **metricRuleRoleArn** *(string) --*

      The ARN of the role that is used to collect cloud metrics.
    """


_ClientCreateSystemInstancetagsTypeDef = TypedDict(
    "_ClientCreateSystemInstancetagsTypeDef", {"key": str, "value": str}
)


class ClientCreateSystemInstancetagsTypeDef(_ClientCreateSystemInstancetagsTypeDef):
    """
    Type definition for `ClientCreateSystemInstance` `tags`

    Metadata assigned to an AWS IoT Things Graph resource consisting of a key-value pair.

    - **key** *(string) --* **[REQUIRED]**

      The required name of the tag. The string value can be from 1 to 128 Unicode characters in
      length.

    - **value** *(string) --* **[REQUIRED]**

      The optional value of the tag. The string value can be from 1 to 256 Unicode characters in
      length.
    """


_ClientCreateSystemTemplateResponsesummaryTypeDef = TypedDict(
    "_ClientCreateSystemTemplateResponsesummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientCreateSystemTemplateResponsesummaryTypeDef(
    _ClientCreateSystemTemplateResponsesummaryTypeDef
):
    """
    Type definition for `ClientCreateSystemTemplateResponse` `summary`

    The summary object that describes the created system.

    - **id** *(string) --*

      The ID of the system.

    - **arn** *(string) --*

      The ARN of the system.

    - **revisionNumber** *(integer) --*

      The revision number of the system.

    - **createdAt** *(datetime) --*

      The date when the system was created.
    """


_ClientCreateSystemTemplateResponseTypeDef = TypedDict(
    "_ClientCreateSystemTemplateResponseTypeDef",
    {"summary": ClientCreateSystemTemplateResponsesummaryTypeDef},
    total=False,
)


class ClientCreateSystemTemplateResponseTypeDef(
    _ClientCreateSystemTemplateResponseTypeDef
):
    """
    Type definition for `ClientCreateSystemTemplate` `Response`

    - **summary** *(dict) --*

      The summary object that describes the created system.

      - **id** *(string) --*

        The ID of the system.

      - **arn** *(string) --*

        The ARN of the system.

      - **revisionNumber** *(integer) --*

        The revision number of the system.

      - **createdAt** *(datetime) --*

        The date when the system was created.
    """


_ClientCreateSystemTemplatedefinitionTypeDef = TypedDict(
    "_ClientCreateSystemTemplatedefinitionTypeDef", {"language": str, "text": str}
)


class ClientCreateSystemTemplatedefinitionTypeDef(
    _ClientCreateSystemTemplatedefinitionTypeDef
):
    """
    Type definition for `ClientCreateSystemTemplate` `definition`

    The ``DefinitionDocument`` used to create the system.

    - **language** *(string) --* **[REQUIRED]**

      The language used to define the entity. ``GRAPHQL`` is the only valid value.

    - **text** *(string) --* **[REQUIRED]**

      The GraphQL text that defines the entity.
    """


_ClientDeleteNamespaceResponseTypeDef = TypedDict(
    "_ClientDeleteNamespaceResponseTypeDef",
    {"namespaceArn": str, "namespaceName": str},
    total=False,
)


class ClientDeleteNamespaceResponseTypeDef(_ClientDeleteNamespaceResponseTypeDef):
    """
    Type definition for `ClientDeleteNamespace` `Response`

    - **namespaceArn** *(string) --*

      The ARN of the namespace to be deleted.

    - **namespaceName** *(string) --*

      The name of the namespace to be deleted.
    """


_ClientDeploySystemInstanceResponsesummaryTypeDef = TypedDict(
    "_ClientDeploySystemInstanceResponsesummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "status": str,
        "target": str,
        "greengrassGroupName": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "greengrassGroupId": str,
        "greengrassGroupVersionId": str,
    },
    total=False,
)


class ClientDeploySystemInstanceResponsesummaryTypeDef(
    _ClientDeploySystemInstanceResponsesummaryTypeDef
):
    """
    Type definition for `ClientDeploySystemInstanceResponse` `summary`

    An object that contains summary information about a system instance that was deployed.

    - **id** *(string) --*

      The ID of the system instance.

    - **arn** *(string) --*

      The ARN of the system instance.

    - **status** *(string) --*

      The status of the system instance.

    - **target** *(string) --*

      The target of the system instance.

    - **greengrassGroupName** *(string) --*

      The ID of the Greengrass group where the system instance is deployed.

    - **createdAt** *(datetime) --*

      The date when the system instance was created.

    - **updatedAt** *(datetime) --*

      The date and time when the system instance was last updated.

    - **greengrassGroupId** *(string) --*

      The ID of the Greengrass group where the system instance is deployed.

    - **greengrassGroupVersionId** *(string) --*

      The version of the Greengrass group where the system instance is deployed.
    """


_ClientDeploySystemInstanceResponseTypeDef = TypedDict(
    "_ClientDeploySystemInstanceResponseTypeDef",
    {
        "summary": ClientDeploySystemInstanceResponsesummaryTypeDef,
        "greengrassDeploymentId": str,
    },
    total=False,
)


class ClientDeploySystemInstanceResponseTypeDef(
    _ClientDeploySystemInstanceResponseTypeDef
):
    """
    Type definition for `ClientDeploySystemInstance` `Response`

    - **summary** *(dict) --*

      An object that contains summary information about a system instance that was deployed.

      - **id** *(string) --*

        The ID of the system instance.

      - **arn** *(string) --*

        The ARN of the system instance.

      - **status** *(string) --*

        The status of the system instance.

      - **target** *(string) --*

        The target of the system instance.

      - **greengrassGroupName** *(string) --*

        The ID of the Greengrass group where the system instance is deployed.

      - **createdAt** *(datetime) --*

        The date when the system instance was created.

      - **updatedAt** *(datetime) --*

        The date and time when the system instance was last updated.

      - **greengrassGroupId** *(string) --*

        The ID of the Greengrass group where the system instance is deployed.

      - **greengrassGroupVersionId** *(string) --*

        The version of the Greengrass group where the system instance is deployed.

    - **greengrassDeploymentId** *(string) --*

      The ID of the Greengrass deployment used to deploy the system instance.
    """


_ClientDescribeNamespaceResponseTypeDef = TypedDict(
    "_ClientDescribeNamespaceResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "trackingNamespaceName": str,
        "trackingNamespaceVersion": int,
        "namespaceVersion": int,
    },
    total=False,
)


class ClientDescribeNamespaceResponseTypeDef(_ClientDescribeNamespaceResponseTypeDef):
    """
    Type definition for `ClientDescribeNamespace` `Response`

    - **namespaceArn** *(string) --*

      The ARN of the namespace.

    - **namespaceName** *(string) --*

      The name of the namespace.

    - **trackingNamespaceName** *(string) --*

      The name of the public namespace that the latest namespace version is tracking.

    - **trackingNamespaceVersion** *(integer) --*

      The version of the public namespace that the latest version is tracking.

    - **namespaceVersion** *(integer) --*

      The version of the user's namespace to describe.
    """


_ClientGetEntitiesResponsedescriptionsdefinitionTypeDef = TypedDict(
    "_ClientGetEntitiesResponsedescriptionsdefinitionTypeDef",
    {"language": str, "text": str},
    total=False,
)


class ClientGetEntitiesResponsedescriptionsdefinitionTypeDef(
    _ClientGetEntitiesResponsedescriptionsdefinitionTypeDef
):
    """
    Type definition for `ClientGetEntitiesResponsedescriptions` `definition`

    The definition document of the entity.

    - **language** *(string) --*

      The language used to define the entity. ``GRAPHQL`` is the only valid value.

    - **text** *(string) --*

      The GraphQL text that defines the entity.
    """


_ClientGetEntitiesResponsedescriptionsTypeDef = TypedDict(
    "_ClientGetEntitiesResponsedescriptionsTypeDef",
    {
        "id": str,
        "arn": str,
        "type": str,
        "createdAt": datetime,
        "definition": ClientGetEntitiesResponsedescriptionsdefinitionTypeDef,
    },
    total=False,
)


class ClientGetEntitiesResponsedescriptionsTypeDef(
    _ClientGetEntitiesResponsedescriptionsTypeDef
):
    """
    Type definition for `ClientGetEntitiesResponse` `descriptions`

    Describes the properties of an entity.

    - **id** *(string) --*

      The entity ID.

    - **arn** *(string) --*

      The entity ARN.

    - **type** *(string) --*

      The entity type.

    - **createdAt** *(datetime) --*

      The time at which the entity was created.

    - **definition** *(dict) --*

      The definition document of the entity.

      - **language** *(string) --*

        The language used to define the entity. ``GRAPHQL`` is the only valid value.

      - **text** *(string) --*

        The GraphQL text that defines the entity.
    """


_ClientGetEntitiesResponseTypeDef = TypedDict(
    "_ClientGetEntitiesResponseTypeDef",
    {"descriptions": List[ClientGetEntitiesResponsedescriptionsTypeDef]},
    total=False,
)


class ClientGetEntitiesResponseTypeDef(_ClientGetEntitiesResponseTypeDef):
    """
    Type definition for `ClientGetEntities` `Response`

    - **descriptions** *(list) --*

      An array of descriptions for the specified entities.

      - *(dict) --*

        Describes the properties of an entity.

        - **id** *(string) --*

          The entity ID.

        - **arn** *(string) --*

          The entity ARN.

        - **type** *(string) --*

          The entity type.

        - **createdAt** *(datetime) --*

          The time at which the entity was created.

        - **definition** *(dict) --*

          The definition document of the entity.

          - **language** *(string) --*

            The language used to define the entity. ``GRAPHQL`` is the only valid value.

          - **text** *(string) --*

            The GraphQL text that defines the entity.
    """


_ClientGetFlowTemplateResponsedescriptiondefinitionTypeDef = TypedDict(
    "_ClientGetFlowTemplateResponsedescriptiondefinitionTypeDef",
    {"language": str, "text": str},
    total=False,
)


class ClientGetFlowTemplateResponsedescriptiondefinitionTypeDef(
    _ClientGetFlowTemplateResponsedescriptiondefinitionTypeDef
):
    """
    Type definition for `ClientGetFlowTemplateResponsedescription` `definition`

    A workflow's definition document.

    - **language** *(string) --*

      The language used to define the entity. ``GRAPHQL`` is the only valid value.

    - **text** *(string) --*

      The GraphQL text that defines the entity.
    """


_ClientGetFlowTemplateResponsedescriptionsummaryTypeDef = TypedDict(
    "_ClientGetFlowTemplateResponsedescriptionsummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientGetFlowTemplateResponsedescriptionsummaryTypeDef(
    _ClientGetFlowTemplateResponsedescriptionsummaryTypeDef
):
    """
    Type definition for `ClientGetFlowTemplateResponsedescription` `summary`

    An object that contains summary information about a workflow.

    - **id** *(string) --*

      The ID of the workflow.

    - **arn** *(string) --*

      The ARN of the workflow.

    - **revisionNumber** *(integer) --*

      The revision number of the workflow.

    - **createdAt** *(datetime) --*

      The date when the workflow was created.
    """


_ClientGetFlowTemplateResponsedescriptionTypeDef = TypedDict(
    "_ClientGetFlowTemplateResponsedescriptionTypeDef",
    {
        "summary": ClientGetFlowTemplateResponsedescriptionsummaryTypeDef,
        "definition": ClientGetFlowTemplateResponsedescriptiondefinitionTypeDef,
        "validatedNamespaceVersion": int,
    },
    total=False,
)


class ClientGetFlowTemplateResponsedescriptionTypeDef(
    _ClientGetFlowTemplateResponsedescriptionTypeDef
):
    """
    Type definition for `ClientGetFlowTemplateResponse` `description`

    The object that describes the specified workflow.

    - **summary** *(dict) --*

      An object that contains summary information about a workflow.

      - **id** *(string) --*

        The ID of the workflow.

      - **arn** *(string) --*

        The ARN of the workflow.

      - **revisionNumber** *(integer) --*

        The revision number of the workflow.

      - **createdAt** *(datetime) --*

        The date when the workflow was created.

    - **definition** *(dict) --*

      A workflow's definition document.

      - **language** *(string) --*

        The language used to define the entity. ``GRAPHQL`` is the only valid value.

      - **text** *(string) --*

        The GraphQL text that defines the entity.

    - **validatedNamespaceVersion** *(integer) --*

      The version of the user's namespace against which the workflow was validated. Use this
      value in your system instance.
    """


_ClientGetFlowTemplateResponseTypeDef = TypedDict(
    "_ClientGetFlowTemplateResponseTypeDef",
    {"description": ClientGetFlowTemplateResponsedescriptionTypeDef},
    total=False,
)


class ClientGetFlowTemplateResponseTypeDef(_ClientGetFlowTemplateResponseTypeDef):
    """
    Type definition for `ClientGetFlowTemplate` `Response`

    - **description** *(dict) --*

      The object that describes the specified workflow.

      - **summary** *(dict) --*

        An object that contains summary information about a workflow.

        - **id** *(string) --*

          The ID of the workflow.

        - **arn** *(string) --*

          The ARN of the workflow.

        - **revisionNumber** *(integer) --*

          The revision number of the workflow.

        - **createdAt** *(datetime) --*

          The date when the workflow was created.

      - **definition** *(dict) --*

        A workflow's definition document.

        - **language** *(string) --*

          The language used to define the entity. ``GRAPHQL`` is the only valid value.

        - **text** *(string) --*

          The GraphQL text that defines the entity.

      - **validatedNamespaceVersion** *(integer) --*

        The version of the user's namespace against which the workflow was validated. Use this
        value in your system instance.
    """


_ClientGetFlowTemplateRevisionsResponsesummariesTypeDef = TypedDict(
    "_ClientGetFlowTemplateRevisionsResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientGetFlowTemplateRevisionsResponsesummariesTypeDef(
    _ClientGetFlowTemplateRevisionsResponsesummariesTypeDef
):
    """
    Type definition for `ClientGetFlowTemplateRevisionsResponse` `summaries`

    An object that contains summary information about a workflow.

    - **id** *(string) --*

      The ID of the workflow.

    - **arn** *(string) --*

      The ARN of the workflow.

    - **revisionNumber** *(integer) --*

      The revision number of the workflow.

    - **createdAt** *(datetime) --*

      The date when the workflow was created.
    """


_ClientGetFlowTemplateRevisionsResponseTypeDef = TypedDict(
    "_ClientGetFlowTemplateRevisionsResponseTypeDef",
    {
        "summaries": List[ClientGetFlowTemplateRevisionsResponsesummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientGetFlowTemplateRevisionsResponseTypeDef(
    _ClientGetFlowTemplateRevisionsResponseTypeDef
):
    """
    Type definition for `ClientGetFlowTemplateRevisions` `Response`

    - **summaries** *(list) --*

      An array of objects that provide summary data about each revision.

      - *(dict) --*

        An object that contains summary information about a workflow.

        - **id** *(string) --*

          The ID of the workflow.

        - **arn** *(string) --*

          The ARN of the workflow.

        - **revisionNumber** *(integer) --*

          The revision number of the workflow.

        - **createdAt** *(datetime) --*

          The date when the workflow was created.

    - **nextToken** *(string) --*

      The string to specify as ``nextToken`` when you request the next page of results.
    """


_ClientGetNamespaceDeletionStatusResponseTypeDef = TypedDict(
    "_ClientGetNamespaceDeletionStatusResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "status": str,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)


class ClientGetNamespaceDeletionStatusResponseTypeDef(
    _ClientGetNamespaceDeletionStatusResponseTypeDef
):
    """
    Type definition for `ClientGetNamespaceDeletionStatus` `Response`

    - **namespaceArn** *(string) --*

      The ARN of the namespace that is being deleted.

    - **namespaceName** *(string) --*

      The name of the namespace that is being deleted.

    - **status** *(string) --*

      The status of the deletion request.

    - **errorCode** *(string) --*

      An error code returned by the namespace deletion task.

    - **errorMessage** *(string) --*

      An error code returned by the namespace deletion task.
    """


_ClientGetSystemInstanceResponsedescriptiondefinitionTypeDef = TypedDict(
    "_ClientGetSystemInstanceResponsedescriptiondefinitionTypeDef",
    {"language": str, "text": str},
    total=False,
)


class ClientGetSystemInstanceResponsedescriptiondefinitionTypeDef(
    _ClientGetSystemInstanceResponsedescriptiondefinitionTypeDef
):
    """
    Type definition for `ClientGetSystemInstanceResponsedescription` `definition`

    A document that defines an entity.

    - **language** *(string) --*

      The language used to define the entity. ``GRAPHQL`` is the only valid value.

    - **text** *(string) --*

      The GraphQL text that defines the entity.
    """


_ClientGetSystemInstanceResponsedescriptionmetricsConfigurationTypeDef = TypedDict(
    "_ClientGetSystemInstanceResponsedescriptionmetricsConfigurationTypeDef",
    {"cloudMetricEnabled": bool, "metricRuleRoleArn": str},
    total=False,
)


class ClientGetSystemInstanceResponsedescriptionmetricsConfigurationTypeDef(
    _ClientGetSystemInstanceResponsedescriptionmetricsConfigurationTypeDef
):
    """
    Type definition for `ClientGetSystemInstanceResponsedescription` `metricsConfiguration`

    An object that specifies whether cloud metrics are collected in a deployment and, if so,
    what role is used to collect metrics.

    - **cloudMetricEnabled** *(boolean) --*

      A Boolean that specifies whether cloud metrics are collected.

    - **metricRuleRoleArn** *(string) --*

      The ARN of the role that is used to collect cloud metrics.
    """


_ClientGetSystemInstanceResponsedescriptionsummaryTypeDef = TypedDict(
    "_ClientGetSystemInstanceResponsedescriptionsummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "status": str,
        "target": str,
        "greengrassGroupName": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "greengrassGroupId": str,
        "greengrassGroupVersionId": str,
    },
    total=False,
)


class ClientGetSystemInstanceResponsedescriptionsummaryTypeDef(
    _ClientGetSystemInstanceResponsedescriptionsummaryTypeDef
):
    """
    Type definition for `ClientGetSystemInstanceResponsedescription` `summary`

    An object that contains summary information about a system instance.

    - **id** *(string) --*

      The ID of the system instance.

    - **arn** *(string) --*

      The ARN of the system instance.

    - **status** *(string) --*

      The status of the system instance.

    - **target** *(string) --*

      The target of the system instance.

    - **greengrassGroupName** *(string) --*

      The ID of the Greengrass group where the system instance is deployed.

    - **createdAt** *(datetime) --*

      The date when the system instance was created.

    - **updatedAt** *(datetime) --*

      The date and time when the system instance was last updated.

    - **greengrassGroupId** *(string) --*

      The ID of the Greengrass group where the system instance is deployed.

    - **greengrassGroupVersionId** *(string) --*

      The version of the Greengrass group where the system instance is deployed.
    """


_ClientGetSystemInstanceResponsedescriptionvalidatedDependencyRevisionsTypeDef = TypedDict(
    "_ClientGetSystemInstanceResponsedescriptionvalidatedDependencyRevisionsTypeDef",
    {"id": str, "revisionNumber": int},
    total=False,
)


class ClientGetSystemInstanceResponsedescriptionvalidatedDependencyRevisionsTypeDef(
    _ClientGetSystemInstanceResponsedescriptionvalidatedDependencyRevisionsTypeDef
):
    """
    Type definition for `ClientGetSystemInstanceResponsedescription` `validatedDependencyRevisions`

    An object that contains the ID and revision number of a workflow or system that is part
    of a deployment.

    - **id** *(string) --*

      The ID of the workflow or system.

    - **revisionNumber** *(integer) --*

      The revision number of the workflow or system.
    """


_ClientGetSystemInstanceResponsedescriptionTypeDef = TypedDict(
    "_ClientGetSystemInstanceResponsedescriptionTypeDef",
    {
        "summary": ClientGetSystemInstanceResponsedescriptionsummaryTypeDef,
        "definition": ClientGetSystemInstanceResponsedescriptiondefinitionTypeDef,
        "s3BucketName": str,
        "metricsConfiguration": ClientGetSystemInstanceResponsedescriptionmetricsConfigurationTypeDef,
        "validatedNamespaceVersion": int,
        "validatedDependencyRevisions": List[
            ClientGetSystemInstanceResponsedescriptionvalidatedDependencyRevisionsTypeDef
        ],
        "flowActionsRoleArn": str,
    },
    total=False,
)


class ClientGetSystemInstanceResponsedescriptionTypeDef(
    _ClientGetSystemInstanceResponsedescriptionTypeDef
):
    """
    Type definition for `ClientGetSystemInstanceResponse` `description`

    An object that describes the system instance.

    - **summary** *(dict) --*

      An object that contains summary information about a system instance.

      - **id** *(string) --*

        The ID of the system instance.

      - **arn** *(string) --*

        The ARN of the system instance.

      - **status** *(string) --*

        The status of the system instance.

      - **target** *(string) --*

        The target of the system instance.

      - **greengrassGroupName** *(string) --*

        The ID of the Greengrass group where the system instance is deployed.

      - **createdAt** *(datetime) --*

        The date when the system instance was created.

      - **updatedAt** *(datetime) --*

        The date and time when the system instance was last updated.

      - **greengrassGroupId** *(string) --*

        The ID of the Greengrass group where the system instance is deployed.

      - **greengrassGroupVersionId** *(string) --*

        The version of the Greengrass group where the system instance is deployed.

    - **definition** *(dict) --*

      A document that defines an entity.

      - **language** *(string) --*

        The language used to define the entity. ``GRAPHQL`` is the only valid value.

      - **text** *(string) --*

        The GraphQL text that defines the entity.

    - **s3BucketName** *(string) --*

      The Amazon Simple Storage Service bucket where information about a system instance is
      stored.

    - **metricsConfiguration** *(dict) --*

      An object that specifies whether cloud metrics are collected in a deployment and, if so,
      what role is used to collect metrics.

      - **cloudMetricEnabled** *(boolean) --*

        A Boolean that specifies whether cloud metrics are collected.

      - **metricRuleRoleArn** *(string) --*

        The ARN of the role that is used to collect cloud metrics.

    - **validatedNamespaceVersion** *(integer) --*

      The version of the user's namespace against which the system instance was validated.

    - **validatedDependencyRevisions** *(list) --*

      A list of objects that contain all of the IDs and revision numbers of workflows and systems
      that are used in a system instance.

      - *(dict) --*

        An object that contains the ID and revision number of a workflow or system that is part
        of a deployment.

        - **id** *(string) --*

          The ID of the workflow or system.

        - **revisionNumber** *(integer) --*

          The revision number of the workflow or system.

    - **flowActionsRoleArn** *(string) --*

      The AWS Identity and Access Management (IAM) role that AWS IoT Things Graph assumes during
      flow execution in a cloud deployment. This role must have read and write permissionss to
      AWS Lambda and AWS IoT and to any other AWS services that the flow uses.
    """


_ClientGetSystemInstanceResponseTypeDef = TypedDict(
    "_ClientGetSystemInstanceResponseTypeDef",
    {"description": ClientGetSystemInstanceResponsedescriptionTypeDef},
    total=False,
)


class ClientGetSystemInstanceResponseTypeDef(_ClientGetSystemInstanceResponseTypeDef):
    """
    Type definition for `ClientGetSystemInstance` `Response`

    - **description** *(dict) --*

      An object that describes the system instance.

      - **summary** *(dict) --*

        An object that contains summary information about a system instance.

        - **id** *(string) --*

          The ID of the system instance.

        - **arn** *(string) --*

          The ARN of the system instance.

        - **status** *(string) --*

          The status of the system instance.

        - **target** *(string) --*

          The target of the system instance.

        - **greengrassGroupName** *(string) --*

          The ID of the Greengrass group where the system instance is deployed.

        - **createdAt** *(datetime) --*

          The date when the system instance was created.

        - **updatedAt** *(datetime) --*

          The date and time when the system instance was last updated.

        - **greengrassGroupId** *(string) --*

          The ID of the Greengrass group where the system instance is deployed.

        - **greengrassGroupVersionId** *(string) --*

          The version of the Greengrass group where the system instance is deployed.

      - **definition** *(dict) --*

        A document that defines an entity.

        - **language** *(string) --*

          The language used to define the entity. ``GRAPHQL`` is the only valid value.

        - **text** *(string) --*

          The GraphQL text that defines the entity.

      - **s3BucketName** *(string) --*

        The Amazon Simple Storage Service bucket where information about a system instance is
        stored.

      - **metricsConfiguration** *(dict) --*

        An object that specifies whether cloud metrics are collected in a deployment and, if so,
        what role is used to collect metrics.

        - **cloudMetricEnabled** *(boolean) --*

          A Boolean that specifies whether cloud metrics are collected.

        - **metricRuleRoleArn** *(string) --*

          The ARN of the role that is used to collect cloud metrics.

      - **validatedNamespaceVersion** *(integer) --*

        The version of the user's namespace against which the system instance was validated.

      - **validatedDependencyRevisions** *(list) --*

        A list of objects that contain all of the IDs and revision numbers of workflows and systems
        that are used in a system instance.

        - *(dict) --*

          An object that contains the ID and revision number of a workflow or system that is part
          of a deployment.

          - **id** *(string) --*

            The ID of the workflow or system.

          - **revisionNumber** *(integer) --*

            The revision number of the workflow or system.

      - **flowActionsRoleArn** *(string) --*

        The AWS Identity and Access Management (IAM) role that AWS IoT Things Graph assumes during
        flow execution in a cloud deployment. This role must have read and write permissionss to
        AWS Lambda and AWS IoT and to any other AWS services that the flow uses.
    """


_ClientGetSystemTemplateResponsedescriptiondefinitionTypeDef = TypedDict(
    "_ClientGetSystemTemplateResponsedescriptiondefinitionTypeDef",
    {"language": str, "text": str},
    total=False,
)


class ClientGetSystemTemplateResponsedescriptiondefinitionTypeDef(
    _ClientGetSystemTemplateResponsedescriptiondefinitionTypeDef
):
    """
    Type definition for `ClientGetSystemTemplateResponsedescription` `definition`

    The definition document of a system.

    - **language** *(string) --*

      The language used to define the entity. ``GRAPHQL`` is the only valid value.

    - **text** *(string) --*

      The GraphQL text that defines the entity.
    """


_ClientGetSystemTemplateResponsedescriptionsummaryTypeDef = TypedDict(
    "_ClientGetSystemTemplateResponsedescriptionsummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientGetSystemTemplateResponsedescriptionsummaryTypeDef(
    _ClientGetSystemTemplateResponsedescriptionsummaryTypeDef
):
    """
    Type definition for `ClientGetSystemTemplateResponsedescription` `summary`

    An object that contains summary information about a system.

    - **id** *(string) --*

      The ID of the system.

    - **arn** *(string) --*

      The ARN of the system.

    - **revisionNumber** *(integer) --*

      The revision number of the system.

    - **createdAt** *(datetime) --*

      The date when the system was created.
    """


_ClientGetSystemTemplateResponsedescriptionTypeDef = TypedDict(
    "_ClientGetSystemTemplateResponsedescriptionTypeDef",
    {
        "summary": ClientGetSystemTemplateResponsedescriptionsummaryTypeDef,
        "definition": ClientGetSystemTemplateResponsedescriptiondefinitionTypeDef,
        "validatedNamespaceVersion": int,
    },
    total=False,
)


class ClientGetSystemTemplateResponsedescriptionTypeDef(
    _ClientGetSystemTemplateResponsedescriptionTypeDef
):
    """
    Type definition for `ClientGetSystemTemplateResponse` `description`

    An object that contains summary data about the system.

    - **summary** *(dict) --*

      An object that contains summary information about a system.

      - **id** *(string) --*

        The ID of the system.

      - **arn** *(string) --*

        The ARN of the system.

      - **revisionNumber** *(integer) --*

        The revision number of the system.

      - **createdAt** *(datetime) --*

        The date when the system was created.

    - **definition** *(dict) --*

      The definition document of a system.

      - **language** *(string) --*

        The language used to define the entity. ``GRAPHQL`` is the only valid value.

      - **text** *(string) --*

        The GraphQL text that defines the entity.

    - **validatedNamespaceVersion** *(integer) --*

      The namespace version against which the system was validated. Use this value in your system
      instance.
    """


_ClientGetSystemTemplateResponseTypeDef = TypedDict(
    "_ClientGetSystemTemplateResponseTypeDef",
    {"description": ClientGetSystemTemplateResponsedescriptionTypeDef},
    total=False,
)


class ClientGetSystemTemplateResponseTypeDef(_ClientGetSystemTemplateResponseTypeDef):
    """
    Type definition for `ClientGetSystemTemplate` `Response`

    - **description** *(dict) --*

      An object that contains summary data about the system.

      - **summary** *(dict) --*

        An object that contains summary information about a system.

        - **id** *(string) --*

          The ID of the system.

        - **arn** *(string) --*

          The ARN of the system.

        - **revisionNumber** *(integer) --*

          The revision number of the system.

        - **createdAt** *(datetime) --*

          The date when the system was created.

      - **definition** *(dict) --*

        The definition document of a system.

        - **language** *(string) --*

          The language used to define the entity. ``GRAPHQL`` is the only valid value.

        - **text** *(string) --*

          The GraphQL text that defines the entity.

      - **validatedNamespaceVersion** *(integer) --*

        The namespace version against which the system was validated. Use this value in your system
        instance.
    """


_ClientGetSystemTemplateRevisionsResponsesummariesTypeDef = TypedDict(
    "_ClientGetSystemTemplateRevisionsResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientGetSystemTemplateRevisionsResponsesummariesTypeDef(
    _ClientGetSystemTemplateRevisionsResponsesummariesTypeDef
):
    """
    Type definition for `ClientGetSystemTemplateRevisionsResponse` `summaries`

    An object that contains information about a system.

    - **id** *(string) --*

      The ID of the system.

    - **arn** *(string) --*

      The ARN of the system.

    - **revisionNumber** *(integer) --*

      The revision number of the system.

    - **createdAt** *(datetime) --*

      The date when the system was created.
    """


_ClientGetSystemTemplateRevisionsResponseTypeDef = TypedDict(
    "_ClientGetSystemTemplateRevisionsResponseTypeDef",
    {
        "summaries": List[ClientGetSystemTemplateRevisionsResponsesummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientGetSystemTemplateRevisionsResponseTypeDef(
    _ClientGetSystemTemplateRevisionsResponseTypeDef
):
    """
    Type definition for `ClientGetSystemTemplateRevisions` `Response`

    - **summaries** *(list) --*

      An array of objects that contain summary data about the system template revisions.

      - *(dict) --*

        An object that contains information about a system.

        - **id** *(string) --*

          The ID of the system.

        - **arn** *(string) --*

          The ARN of the system.

        - **revisionNumber** *(integer) --*

          The revision number of the system.

        - **createdAt** *(datetime) --*

          The date when the system was created.

    - **nextToken** *(string) --*

      The string to specify as ``nextToken`` when you request the next page of results.
    """


_ClientGetUploadStatusResponseTypeDef = TypedDict(
    "_ClientGetUploadStatusResponseTypeDef",
    {
        "uploadId": str,
        "uploadStatus": str,
        "namespaceArn": str,
        "namespaceName": str,
        "namespaceVersion": int,
        "failureReason": List[str],
        "createdDate": datetime,
    },
    total=False,
)


class ClientGetUploadStatusResponseTypeDef(_ClientGetUploadStatusResponseTypeDef):
    """
    Type definition for `ClientGetUploadStatus` `Response`

    - **uploadId** *(string) --*

      The ID of the upload.

    - **uploadStatus** *(string) --*

      The status of the upload. The initial status is ``IN_PROGRESS`` . The response show all
      validation failures if the upload fails.

    - **namespaceArn** *(string) --*

      The ARN of the upload.

    - **namespaceName** *(string) --*

      The name of the upload's namespace.

    - **namespaceVersion** *(integer) --*

      The version of the user's namespace. Defaults to the latest version of the user's namespace.

    - **failureReason** *(list) --*

      The reason for an upload failure.

      - *(string) --*

    - **createdDate** *(datetime) --*

      The date at which the upload was created.
    """


_ClientListFlowExecutionMessagesResponsemessagesTypeDef = TypedDict(
    "_ClientListFlowExecutionMessagesResponsemessagesTypeDef",
    {"messageId": str, "eventType": str, "timestamp": datetime, "payload": str},
    total=False,
)


class ClientListFlowExecutionMessagesResponsemessagesTypeDef(
    _ClientListFlowExecutionMessagesResponsemessagesTypeDef
):
    """
    Type definition for `ClientListFlowExecutionMessagesResponse` `messages`

    An object that contains information about a flow event.

    - **messageId** *(string) --*

      The unique identifier of the message.

    - **eventType** *(string) --*

      The type of flow event .

    - **timestamp** *(datetime) --*

      The date and time when the message was last updated.

    - **payload** *(string) --*

      A string containing information about the flow event.
    """


_ClientListFlowExecutionMessagesResponseTypeDef = TypedDict(
    "_ClientListFlowExecutionMessagesResponseTypeDef",
    {
        "messages": List[ClientListFlowExecutionMessagesResponsemessagesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListFlowExecutionMessagesResponseTypeDef(
    _ClientListFlowExecutionMessagesResponseTypeDef
):
    """
    Type definition for `ClientListFlowExecutionMessages` `Response`

    - **messages** *(list) --*

      A list of objects that contain information about events in the specified flow execution.

      - *(dict) --*

        An object that contains information about a flow event.

        - **messageId** *(string) --*

          The unique identifier of the message.

        - **eventType** *(string) --*

          The type of flow event .

        - **timestamp** *(datetime) --*

          The date and time when the message was last updated.

        - **payload** *(string) --*

          A string containing information about the flow event.

    - **nextToken** *(string) --*

      The string to specify as ``nextToken`` when you request the next page of results.
    """


_ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ClientListTagsForResourceResponsetagsTypeDef(
    _ClientListTagsForResourceResponsetagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `tags`

    Metadata assigned to an AWS IoT Things Graph resource consisting of a key-value pair.

    - **key** *(string) --*

      The required name of the tag. The string value can be from 1 to 128 Unicode characters in
      length.

    - **value** *(string) --*

      The optional value of the tag. The string value can be from 1 to 256 Unicode characters
      in length.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef], "nextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **tags** *(list) --*

      List of tags returned by the ``ListTagsForResource`` operation.

      - *(dict) --*

        Metadata assigned to an AWS IoT Things Graph resource consisting of a key-value pair.

        - **key** *(string) --*

          The required name of the tag. The string value can be from 1 to 128 Unicode characters in
          length.

        - **value** *(string) --*

          The optional value of the tag. The string value can be from 1 to 256 Unicode characters
          in length.

    - **nextToken** *(string) --*

      The token that specifies the next page of results to return.
    """


_ClientSearchEntitiesResponsedescriptionsdefinitionTypeDef = TypedDict(
    "_ClientSearchEntitiesResponsedescriptionsdefinitionTypeDef",
    {"language": str, "text": str},
    total=False,
)


class ClientSearchEntitiesResponsedescriptionsdefinitionTypeDef(
    _ClientSearchEntitiesResponsedescriptionsdefinitionTypeDef
):
    """
    Type definition for `ClientSearchEntitiesResponsedescriptions` `definition`

    The definition document of the entity.

    - **language** *(string) --*

      The language used to define the entity. ``GRAPHQL`` is the only valid value.

    - **text** *(string) --*

      The GraphQL text that defines the entity.
    """


_ClientSearchEntitiesResponsedescriptionsTypeDef = TypedDict(
    "_ClientSearchEntitiesResponsedescriptionsTypeDef",
    {
        "id": str,
        "arn": str,
        "type": str,
        "createdAt": datetime,
        "definition": ClientSearchEntitiesResponsedescriptionsdefinitionTypeDef,
    },
    total=False,
)


class ClientSearchEntitiesResponsedescriptionsTypeDef(
    _ClientSearchEntitiesResponsedescriptionsTypeDef
):
    """
    Type definition for `ClientSearchEntitiesResponse` `descriptions`

    Describes the properties of an entity.

    - **id** *(string) --*

      The entity ID.

    - **arn** *(string) --*

      The entity ARN.

    - **type** *(string) --*

      The entity type.

    - **createdAt** *(datetime) --*

      The time at which the entity was created.

    - **definition** *(dict) --*

      The definition document of the entity.

      - **language** *(string) --*

        The language used to define the entity. ``GRAPHQL`` is the only valid value.

      - **text** *(string) --*

        The GraphQL text that defines the entity.
    """


_ClientSearchEntitiesResponseTypeDef = TypedDict(
    "_ClientSearchEntitiesResponseTypeDef",
    {
        "descriptions": List[ClientSearchEntitiesResponsedescriptionsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientSearchEntitiesResponseTypeDef(_ClientSearchEntitiesResponseTypeDef):
    """
    Type definition for `ClientSearchEntities` `Response`

    - **descriptions** *(list) --*

      An array of descriptions for each entity returned in the search result.

      - *(dict) --*

        Describes the properties of an entity.

        - **id** *(string) --*

          The entity ID.

        - **arn** *(string) --*

          The entity ARN.

        - **type** *(string) --*

          The entity type.

        - **createdAt** *(datetime) --*

          The time at which the entity was created.

        - **definition** *(dict) --*

          The definition document of the entity.

          - **language** *(string) --*

            The language used to define the entity. ``GRAPHQL`` is the only valid value.

          - **text** *(string) --*

            The GraphQL text that defines the entity.

    - **nextToken** *(string) --*

      The string to specify as ``nextToken`` when you request the next page of results.
    """


_ClientSearchEntitiesfiltersTypeDef = TypedDict(
    "_ClientSearchEntitiesfiltersTypeDef",
    {"name": str, "value": List[str]},
    total=False,
)


class ClientSearchEntitiesfiltersTypeDef(_ClientSearchEntitiesfiltersTypeDef):
    """
    Type definition for `ClientSearchEntities` `filters`

    An object that filters an entity search. Multiple filters function as OR criteria in the
    search. For example a search that includes a ``NAMESPACE`` and a ``REFERENCED_ENTITY_ID``
    filter searches for entities in the specified namespace that use the entity specified by the
    value of ``REFERENCED_ENTITY_ID`` .

    - **name** *(string) --*

      The name of the entity search filter field. ``REFERENCED_ENTITY_ID`` filters on entities that
      are used by the entity in the result set. For example, you can filter on the ID of a property
      that is used in a state.

    - **value** *(list) --*

      An array of string values for the search filter field. Multiple values function as AND
      criteria in the search.

      - *(string) --*
    """


_ClientSearchFlowExecutionsResponsesummariesTypeDef = TypedDict(
    "_ClientSearchFlowExecutionsResponsesummariesTypeDef",
    {
        "flowExecutionId": str,
        "status": str,
        "systemInstanceId": str,
        "flowTemplateId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
    total=False,
)


class ClientSearchFlowExecutionsResponsesummariesTypeDef(
    _ClientSearchFlowExecutionsResponsesummariesTypeDef
):
    """
    Type definition for `ClientSearchFlowExecutionsResponse` `summaries`

    An object that contains summary information about a flow execution.

    - **flowExecutionId** *(string) --*

      The ID of the flow execution.

    - **status** *(string) --*

      The current status of the flow execution.

    - **systemInstanceId** *(string) --*

      The ID of the system instance that contains the flow.

    - **flowTemplateId** *(string) --*

      The ID of the flow.

    - **createdAt** *(datetime) --*

      The date and time when the flow execution summary was created.

    - **updatedAt** *(datetime) --*

      The date and time when the flow execution summary was last updated.
    """


_ClientSearchFlowExecutionsResponseTypeDef = TypedDict(
    "_ClientSearchFlowExecutionsResponseTypeDef",
    {
        "summaries": List[ClientSearchFlowExecutionsResponsesummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientSearchFlowExecutionsResponseTypeDef(
    _ClientSearchFlowExecutionsResponseTypeDef
):
    """
    Type definition for `ClientSearchFlowExecutions` `Response`

    - **summaries** *(list) --*

      An array of objects that contain summary information about each workflow execution in the
      result set.

      - *(dict) --*

        An object that contains summary information about a flow execution.

        - **flowExecutionId** *(string) --*

          The ID of the flow execution.

        - **status** *(string) --*

          The current status of the flow execution.

        - **systemInstanceId** *(string) --*

          The ID of the system instance that contains the flow.

        - **flowTemplateId** *(string) --*

          The ID of the flow.

        - **createdAt** *(datetime) --*

          The date and time when the flow execution summary was created.

        - **updatedAt** *(datetime) --*

          The date and time when the flow execution summary was last updated.

    - **nextToken** *(string) --*

      The string to specify as ``nextToken`` when you request the next page of results.
    """


_ClientSearchFlowTemplatesResponsesummariesTypeDef = TypedDict(
    "_ClientSearchFlowTemplatesResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientSearchFlowTemplatesResponsesummariesTypeDef(
    _ClientSearchFlowTemplatesResponsesummariesTypeDef
):
    """
    Type definition for `ClientSearchFlowTemplatesResponse` `summaries`

    An object that contains summary information about a workflow.

    - **id** *(string) --*

      The ID of the workflow.

    - **arn** *(string) --*

      The ARN of the workflow.

    - **revisionNumber** *(integer) --*

      The revision number of the workflow.

    - **createdAt** *(datetime) --*

      The date when the workflow was created.
    """


_ClientSearchFlowTemplatesResponseTypeDef = TypedDict(
    "_ClientSearchFlowTemplatesResponseTypeDef",
    {
        "summaries": List[ClientSearchFlowTemplatesResponsesummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientSearchFlowTemplatesResponseTypeDef(
    _ClientSearchFlowTemplatesResponseTypeDef
):
    """
    Type definition for `ClientSearchFlowTemplates` `Response`

    - **summaries** *(list) --*

      An array of objects that contain summary information about each workflow in the result set.

      - *(dict) --*

        An object that contains summary information about a workflow.

        - **id** *(string) --*

          The ID of the workflow.

        - **arn** *(string) --*

          The ARN of the workflow.

        - **revisionNumber** *(integer) --*

          The revision number of the workflow.

        - **createdAt** *(datetime) --*

          The date when the workflow was created.

    - **nextToken** *(string) --*

      The string to specify as ``nextToken`` when you request the next page of results.
    """


_ClientSearchFlowTemplatesfiltersTypeDef = TypedDict(
    "_ClientSearchFlowTemplatesfiltersTypeDef", {"name": str, "value": List[str]}
)


class ClientSearchFlowTemplatesfiltersTypeDef(_ClientSearchFlowTemplatesfiltersTypeDef):
    """
    Type definition for `ClientSearchFlowTemplates` `filters`

    An object that filters a workflow search.

    - **name** *(string) --* **[REQUIRED]**

      The name of the search filter field.

    - **value** *(list) --* **[REQUIRED]**

      An array of string values for the search filter field. Multiple values function as AND
      criteria in the search.

      - *(string) --*
    """


_ClientSearchSystemInstancesResponsesummariesTypeDef = TypedDict(
    "_ClientSearchSystemInstancesResponsesummariesTypeDef",
    {
        "id": str,
        "arn": str,
        "status": str,
        "target": str,
        "greengrassGroupName": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "greengrassGroupId": str,
        "greengrassGroupVersionId": str,
    },
    total=False,
)


class ClientSearchSystemInstancesResponsesummariesTypeDef(
    _ClientSearchSystemInstancesResponsesummariesTypeDef
):
    """
    Type definition for `ClientSearchSystemInstancesResponse` `summaries`

    An object that contains summary information about a system instance.

    - **id** *(string) --*

      The ID of the system instance.

    - **arn** *(string) --*

      The ARN of the system instance.

    - **status** *(string) --*

      The status of the system instance.

    - **target** *(string) --*

      The target of the system instance.

    - **greengrassGroupName** *(string) --*

      The ID of the Greengrass group where the system instance is deployed.

    - **createdAt** *(datetime) --*

      The date when the system instance was created.

    - **updatedAt** *(datetime) --*

      The date and time when the system instance was last updated.

    - **greengrassGroupId** *(string) --*

      The ID of the Greengrass group where the system instance is deployed.

    - **greengrassGroupVersionId** *(string) --*

      The version of the Greengrass group where the system instance is deployed.
    """


_ClientSearchSystemInstancesResponseTypeDef = TypedDict(
    "_ClientSearchSystemInstancesResponseTypeDef",
    {
        "summaries": List[ClientSearchSystemInstancesResponsesummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientSearchSystemInstancesResponseTypeDef(
    _ClientSearchSystemInstancesResponseTypeDef
):
    """
    Type definition for `ClientSearchSystemInstances` `Response`

    - **summaries** *(list) --*

      An array of objects that contain summary data abour the system instances in the result set.

      - *(dict) --*

        An object that contains summary information about a system instance.

        - **id** *(string) --*

          The ID of the system instance.

        - **arn** *(string) --*

          The ARN of the system instance.

        - **status** *(string) --*

          The status of the system instance.

        - **target** *(string) --*

          The target of the system instance.

        - **greengrassGroupName** *(string) --*

          The ID of the Greengrass group where the system instance is deployed.

        - **createdAt** *(datetime) --*

          The date when the system instance was created.

        - **updatedAt** *(datetime) --*

          The date and time when the system instance was last updated.

        - **greengrassGroupId** *(string) --*

          The ID of the Greengrass group where the system instance is deployed.

        - **greengrassGroupVersionId** *(string) --*

          The version of the Greengrass group where the system instance is deployed.

    - **nextToken** *(string) --*

      The string to specify as ``nextToken`` when you request the next page of results.
    """


_ClientSearchSystemInstancesfiltersTypeDef = TypedDict(
    "_ClientSearchSystemInstancesfiltersTypeDef",
    {"name": str, "value": List[str]},
    total=False,
)


class ClientSearchSystemInstancesfiltersTypeDef(
    _ClientSearchSystemInstancesfiltersTypeDef
):
    """
    Type definition for `ClientSearchSystemInstances` `filters`

    An object that filters a system instance search. Multiple filters function as OR criteria in
    the search. For example a search that includes a GREENGRASS_GROUP_NAME and a STATUS filter
    searches for system instances in the specified Greengrass group that have the specified status.

    - **name** *(string) --*

      The name of the search filter field.

    - **value** *(list) --*

      An array of string values for the search filter field. Multiple values function as AND
      criteria in the search.

      - *(string) --*
    """


_ClientSearchSystemTemplatesResponsesummariesTypeDef = TypedDict(
    "_ClientSearchSystemTemplatesResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientSearchSystemTemplatesResponsesummariesTypeDef(
    _ClientSearchSystemTemplatesResponsesummariesTypeDef
):
    """
    Type definition for `ClientSearchSystemTemplatesResponse` `summaries`

    An object that contains information about a system.

    - **id** *(string) --*

      The ID of the system.

    - **arn** *(string) --*

      The ARN of the system.

    - **revisionNumber** *(integer) --*

      The revision number of the system.

    - **createdAt** *(datetime) --*

      The date when the system was created.
    """


_ClientSearchSystemTemplatesResponseTypeDef = TypedDict(
    "_ClientSearchSystemTemplatesResponseTypeDef",
    {
        "summaries": List[ClientSearchSystemTemplatesResponsesummariesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientSearchSystemTemplatesResponseTypeDef(
    _ClientSearchSystemTemplatesResponseTypeDef
):
    """
    Type definition for `ClientSearchSystemTemplates` `Response`

    - **summaries** *(list) --*

      An array of objects that contain summary information about each system deployment in the
      result set.

      - *(dict) --*

        An object that contains information about a system.

        - **id** *(string) --*

          The ID of the system.

        - **arn** *(string) --*

          The ARN of the system.

        - **revisionNumber** *(integer) --*

          The revision number of the system.

        - **createdAt** *(datetime) --*

          The date when the system was created.

    - **nextToken** *(string) --*

      The string to specify as ``nextToken`` when you request the next page of results.
    """


_ClientSearchSystemTemplatesfiltersTypeDef = TypedDict(
    "_ClientSearchSystemTemplatesfiltersTypeDef", {"name": str, "value": List[str]}
)


class ClientSearchSystemTemplatesfiltersTypeDef(
    _ClientSearchSystemTemplatesfiltersTypeDef
):
    """
    Type definition for `ClientSearchSystemTemplates` `filters`

    An object that filters a system search.

    - **name** *(string) --* **[REQUIRED]**

      The name of the system search filter field.

    - **value** *(list) --* **[REQUIRED]**

      An array of string values for the search filter field. Multiple values function as AND
      criteria in the search.

      - *(string) --*
    """


_ClientSearchThingsResponsethingsTypeDef = TypedDict(
    "_ClientSearchThingsResponsethingsTypeDef",
    {"thingArn": str, "thingName": str},
    total=False,
)


class ClientSearchThingsResponsethingsTypeDef(_ClientSearchThingsResponsethingsTypeDef):
    """
    Type definition for `ClientSearchThingsResponse` `things`

    An AWS IoT thing.

    - **thingArn** *(string) --*

      The ARN of the thing.

    - **thingName** *(string) --*

      The name of the thing.
    """


_ClientSearchThingsResponseTypeDef = TypedDict(
    "_ClientSearchThingsResponseTypeDef",
    {"things": List[ClientSearchThingsResponsethingsTypeDef], "nextToken": str},
    total=False,
)


class ClientSearchThingsResponseTypeDef(_ClientSearchThingsResponseTypeDef):
    """
    Type definition for `ClientSearchThings` `Response`

    - **things** *(list) --*

      An array of things in the result set.

      - *(dict) --*

        An AWS IoT thing.

        - **thingArn** *(string) --*

          The ARN of the thing.

        - **thingName** *(string) --*

          The name of the thing.

    - **nextToken** *(string) --*

      The string to specify as ``nextToken`` when you request the next page of results.
    """


_ClientTagResourcetagsTypeDef = TypedDict(
    "_ClientTagResourcetagsTypeDef", {"key": str, "value": str}
)


class ClientTagResourcetagsTypeDef(_ClientTagResourcetagsTypeDef):
    """
    Type definition for `ClientTagResource` `tags`

    Metadata assigned to an AWS IoT Things Graph resource consisting of a key-value pair.

    - **key** *(string) --* **[REQUIRED]**

      The required name of the tag. The string value can be from 1 to 128 Unicode characters in
      length.

    - **value** *(string) --* **[REQUIRED]**

      The optional value of the tag. The string value can be from 1 to 256 Unicode characters in
      length.
    """


_ClientUndeploySystemInstanceResponsesummaryTypeDef = TypedDict(
    "_ClientUndeploySystemInstanceResponsesummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "status": str,
        "target": str,
        "greengrassGroupName": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "greengrassGroupId": str,
        "greengrassGroupVersionId": str,
    },
    total=False,
)


class ClientUndeploySystemInstanceResponsesummaryTypeDef(
    _ClientUndeploySystemInstanceResponsesummaryTypeDef
):
    """
    Type definition for `ClientUndeploySystemInstanceResponse` `summary`

    An object that contains summary information about the system instance that was removed from
    its target.

    - **id** *(string) --*

      The ID of the system instance.

    - **arn** *(string) --*

      The ARN of the system instance.

    - **status** *(string) --*

      The status of the system instance.

    - **target** *(string) --*

      The target of the system instance.

    - **greengrassGroupName** *(string) --*

      The ID of the Greengrass group where the system instance is deployed.

    - **createdAt** *(datetime) --*

      The date when the system instance was created.

    - **updatedAt** *(datetime) --*

      The date and time when the system instance was last updated.

    - **greengrassGroupId** *(string) --*

      The ID of the Greengrass group where the system instance is deployed.

    - **greengrassGroupVersionId** *(string) --*

      The version of the Greengrass group where the system instance is deployed.
    """


_ClientUndeploySystemInstanceResponseTypeDef = TypedDict(
    "_ClientUndeploySystemInstanceResponseTypeDef",
    {"summary": ClientUndeploySystemInstanceResponsesummaryTypeDef},
    total=False,
)


class ClientUndeploySystemInstanceResponseTypeDef(
    _ClientUndeploySystemInstanceResponseTypeDef
):
    """
    Type definition for `ClientUndeploySystemInstance` `Response`

    - **summary** *(dict) --*

      An object that contains summary information about the system instance that was removed from
      its target.

      - **id** *(string) --*

        The ID of the system instance.

      - **arn** *(string) --*

        The ARN of the system instance.

      - **status** *(string) --*

        The status of the system instance.

      - **target** *(string) --*

        The target of the system instance.

      - **greengrassGroupName** *(string) --*

        The ID of the Greengrass group where the system instance is deployed.

      - **createdAt** *(datetime) --*

        The date when the system instance was created.

      - **updatedAt** *(datetime) --*

        The date and time when the system instance was last updated.

      - **greengrassGroupId** *(string) --*

        The ID of the Greengrass group where the system instance is deployed.

      - **greengrassGroupVersionId** *(string) --*

        The version of the Greengrass group where the system instance is deployed.
    """


_ClientUpdateFlowTemplateResponsesummaryTypeDef = TypedDict(
    "_ClientUpdateFlowTemplateResponsesummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientUpdateFlowTemplateResponsesummaryTypeDef(
    _ClientUpdateFlowTemplateResponsesummaryTypeDef
):
    """
    Type definition for `ClientUpdateFlowTemplateResponse` `summary`

    An object containing summary information about the updated workflow.

    - **id** *(string) --*

      The ID of the workflow.

    - **arn** *(string) --*

      The ARN of the workflow.

    - **revisionNumber** *(integer) --*

      The revision number of the workflow.

    - **createdAt** *(datetime) --*

      The date when the workflow was created.
    """


_ClientUpdateFlowTemplateResponseTypeDef = TypedDict(
    "_ClientUpdateFlowTemplateResponseTypeDef",
    {"summary": ClientUpdateFlowTemplateResponsesummaryTypeDef},
    total=False,
)


class ClientUpdateFlowTemplateResponseTypeDef(_ClientUpdateFlowTemplateResponseTypeDef):
    """
    Type definition for `ClientUpdateFlowTemplate` `Response`

    - **summary** *(dict) --*

      An object containing summary information about the updated workflow.

      - **id** *(string) --*

        The ID of the workflow.

      - **arn** *(string) --*

        The ARN of the workflow.

      - **revisionNumber** *(integer) --*

        The revision number of the workflow.

      - **createdAt** *(datetime) --*

        The date when the workflow was created.
    """


_ClientUpdateFlowTemplatedefinitionTypeDef = TypedDict(
    "_ClientUpdateFlowTemplatedefinitionTypeDef", {"language": str, "text": str}
)


class ClientUpdateFlowTemplatedefinitionTypeDef(
    _ClientUpdateFlowTemplatedefinitionTypeDef
):
    """
    Type definition for `ClientUpdateFlowTemplate` `definition`

    The ``DefinitionDocument`` that contains the updated workflow definition.

    - **language** *(string) --* **[REQUIRED]**

      The language used to define the entity. ``GRAPHQL`` is the only valid value.

    - **text** *(string) --* **[REQUIRED]**

      The GraphQL text that defines the entity.
    """


_ClientUpdateSystemTemplateResponsesummaryTypeDef = TypedDict(
    "_ClientUpdateSystemTemplateResponsesummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class ClientUpdateSystemTemplateResponsesummaryTypeDef(
    _ClientUpdateSystemTemplateResponsesummaryTypeDef
):
    """
    Type definition for `ClientUpdateSystemTemplateResponse` `summary`

    An object containing summary information about the updated system.

    - **id** *(string) --*

      The ID of the system.

    - **arn** *(string) --*

      The ARN of the system.

    - **revisionNumber** *(integer) --*

      The revision number of the system.

    - **createdAt** *(datetime) --*

      The date when the system was created.
    """


_ClientUpdateSystemTemplateResponseTypeDef = TypedDict(
    "_ClientUpdateSystemTemplateResponseTypeDef",
    {"summary": ClientUpdateSystemTemplateResponsesummaryTypeDef},
    total=False,
)


class ClientUpdateSystemTemplateResponseTypeDef(
    _ClientUpdateSystemTemplateResponseTypeDef
):
    """
    Type definition for `ClientUpdateSystemTemplate` `Response`

    - **summary** *(dict) --*

      An object containing summary information about the updated system.

      - **id** *(string) --*

        The ID of the system.

      - **arn** *(string) --*

        The ARN of the system.

      - **revisionNumber** *(integer) --*

        The revision number of the system.

      - **createdAt** *(datetime) --*

        The date when the system was created.
    """


_ClientUpdateSystemTemplatedefinitionTypeDef = TypedDict(
    "_ClientUpdateSystemTemplatedefinitionTypeDef", {"language": str, "text": str}
)


class ClientUpdateSystemTemplatedefinitionTypeDef(
    _ClientUpdateSystemTemplatedefinitionTypeDef
):
    """
    Type definition for `ClientUpdateSystemTemplate` `definition`

    The ``DefinitionDocument`` that contains the updated system definition.

    - **language** *(string) --* **[REQUIRED]**

      The language used to define the entity. ``GRAPHQL`` is the only valid value.

    - **text** *(string) --* **[REQUIRED]**

      The GraphQL text that defines the entity.
    """


_ClientUploadEntityDefinitionsResponseTypeDef = TypedDict(
    "_ClientUploadEntityDefinitionsResponseTypeDef", {"uploadId": str}, total=False
)


class ClientUploadEntityDefinitionsResponseTypeDef(
    _ClientUploadEntityDefinitionsResponseTypeDef
):
    """
    Type definition for `ClientUploadEntityDefinitions` `Response`

    - **uploadId** *(string) --*

      The ID that specifies the upload action. You can use this to track the status of the upload.
    """


_ClientUploadEntityDefinitionsdocumentTypeDef = TypedDict(
    "_ClientUploadEntityDefinitionsdocumentTypeDef", {"language": str, "text": str}
)


class ClientUploadEntityDefinitionsdocumentTypeDef(
    _ClientUploadEntityDefinitionsdocumentTypeDef
):
    """
    Type definition for `ClientUploadEntityDefinitions` `document`

    The ``DefinitionDocument`` that defines the updated entities.

    - **language** *(string) --* **[REQUIRED]**

      The language used to define the entity. ``GRAPHQL`` is the only valid value.

    - **text** *(string) --* **[REQUIRED]**

      The GraphQL text that defines the entity.
    """


_GetFlowTemplateRevisionsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetFlowTemplateRevisionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetFlowTemplateRevisionsPaginatePaginationConfigTypeDef(
    _GetFlowTemplateRevisionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetFlowTemplateRevisionsPaginate` `PaginationConfig`

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


_GetFlowTemplateRevisionsPaginateResponsesummariesTypeDef = TypedDict(
    "_GetFlowTemplateRevisionsPaginateResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class GetFlowTemplateRevisionsPaginateResponsesummariesTypeDef(
    _GetFlowTemplateRevisionsPaginateResponsesummariesTypeDef
):
    """
    Type definition for `GetFlowTemplateRevisionsPaginateResponse` `summaries`

    An object that contains summary information about a workflow.

    - **id** *(string) --*

      The ID of the workflow.

    - **arn** *(string) --*

      The ARN of the workflow.

    - **revisionNumber** *(integer) --*

      The revision number of the workflow.

    - **createdAt** *(datetime) --*

      The date when the workflow was created.
    """


_GetFlowTemplateRevisionsPaginateResponseTypeDef = TypedDict(
    "_GetFlowTemplateRevisionsPaginateResponseTypeDef",
    {
        "summaries": List[GetFlowTemplateRevisionsPaginateResponsesummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetFlowTemplateRevisionsPaginateResponseTypeDef(
    _GetFlowTemplateRevisionsPaginateResponseTypeDef
):
    """
    Type definition for `GetFlowTemplateRevisionsPaginate` `Response`

    - **summaries** *(list) --*

      An array of objects that provide summary data about each revision.

      - *(dict) --*

        An object that contains summary information about a workflow.

        - **id** *(string) --*

          The ID of the workflow.

        - **arn** *(string) --*

          The ARN of the workflow.

        - **revisionNumber** *(integer) --*

          The revision number of the workflow.

        - **createdAt** *(datetime) --*

          The date when the workflow was created.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_GetSystemTemplateRevisionsPaginatePaginationConfigTypeDef = TypedDict(
    "_GetSystemTemplateRevisionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetSystemTemplateRevisionsPaginatePaginationConfigTypeDef(
    _GetSystemTemplateRevisionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetSystemTemplateRevisionsPaginate` `PaginationConfig`

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


_GetSystemTemplateRevisionsPaginateResponsesummariesTypeDef = TypedDict(
    "_GetSystemTemplateRevisionsPaginateResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class GetSystemTemplateRevisionsPaginateResponsesummariesTypeDef(
    _GetSystemTemplateRevisionsPaginateResponsesummariesTypeDef
):
    """
    Type definition for `GetSystemTemplateRevisionsPaginateResponse` `summaries`

    An object that contains information about a system.

    - **id** *(string) --*

      The ID of the system.

    - **arn** *(string) --*

      The ARN of the system.

    - **revisionNumber** *(integer) --*

      The revision number of the system.

    - **createdAt** *(datetime) --*

      The date when the system was created.
    """


_GetSystemTemplateRevisionsPaginateResponseTypeDef = TypedDict(
    "_GetSystemTemplateRevisionsPaginateResponseTypeDef",
    {
        "summaries": List[GetSystemTemplateRevisionsPaginateResponsesummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class GetSystemTemplateRevisionsPaginateResponseTypeDef(
    _GetSystemTemplateRevisionsPaginateResponseTypeDef
):
    """
    Type definition for `GetSystemTemplateRevisionsPaginate` `Response`

    - **summaries** *(list) --*

      An array of objects that contain summary data about the system template revisions.

      - *(dict) --*

        An object that contains information about a system.

        - **id** *(string) --*

          The ID of the system.

        - **arn** *(string) --*

          The ARN of the system.

        - **revisionNumber** *(integer) --*

          The revision number of the system.

        - **createdAt** *(datetime) --*

          The date when the system was created.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListFlowExecutionMessagesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFlowExecutionMessagesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFlowExecutionMessagesPaginatePaginationConfigTypeDef(
    _ListFlowExecutionMessagesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListFlowExecutionMessagesPaginate` `PaginationConfig`

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


_ListFlowExecutionMessagesPaginateResponsemessagesTypeDef = TypedDict(
    "_ListFlowExecutionMessagesPaginateResponsemessagesTypeDef",
    {"messageId": str, "eventType": str, "timestamp": datetime, "payload": str},
    total=False,
)


class ListFlowExecutionMessagesPaginateResponsemessagesTypeDef(
    _ListFlowExecutionMessagesPaginateResponsemessagesTypeDef
):
    """
    Type definition for `ListFlowExecutionMessagesPaginateResponse` `messages`

    An object that contains information about a flow event.

    - **messageId** *(string) --*

      The unique identifier of the message.

    - **eventType** *(string) --*

      The type of flow event .

    - **timestamp** *(datetime) --*

      The date and time when the message was last updated.

    - **payload** *(string) --*

      A string containing information about the flow event.
    """


_ListFlowExecutionMessagesPaginateResponseTypeDef = TypedDict(
    "_ListFlowExecutionMessagesPaginateResponseTypeDef",
    {
        "messages": List[ListFlowExecutionMessagesPaginateResponsemessagesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListFlowExecutionMessagesPaginateResponseTypeDef(
    _ListFlowExecutionMessagesPaginateResponseTypeDef
):
    """
    Type definition for `ListFlowExecutionMessagesPaginate` `Response`

    - **messages** *(list) --*

      A list of objects that contain information about events in the specified flow execution.

      - *(dict) --*

        An object that contains information about a flow event.

        - **messageId** *(string) --*

          The unique identifier of the message.

        - **eventType** *(string) --*

          The type of flow event .

        - **timestamp** *(datetime) --*

          The date and time when the message was last updated.

        - **payload** *(string) --*

          A string containing information about the flow event.

    - **NextToken** *(string) --*

      A token to resume pagination.
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


_ListTagsForResourcePaginateResponsetagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponsetagsTypeDef",
    {"key": str, "value": str},
    total=False,
)


class ListTagsForResourcePaginateResponsetagsTypeDef(
    _ListTagsForResourcePaginateResponsetagsTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginateResponse` `tags`

    Metadata assigned to an AWS IoT Things Graph resource consisting of a key-value pair.

    - **key** *(string) --*

      The required name of the tag. The string value can be from 1 to 128 Unicode characters in
      length.

    - **value** *(string) --*

      The optional value of the tag. The string value can be from 1 to 256 Unicode characters
      in length.
    """


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {"tags": List[ListTagsForResourcePaginateResponsetagsTypeDef], "NextToken": str},
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(
    _ListTagsForResourcePaginateResponseTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginate` `Response`

    - **tags** *(list) --*

      List of tags returned by the ``ListTagsForResource`` operation.

      - *(dict) --*

        Metadata assigned to an AWS IoT Things Graph resource consisting of a key-value pair.

        - **key** *(string) --*

          The required name of the tag. The string value can be from 1 to 128 Unicode characters in
          length.

        - **value** *(string) --*

          The optional value of the tag. The string value can be from 1 to 256 Unicode characters
          in length.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_SearchEntitiesPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchEntitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchEntitiesPaginatePaginationConfigTypeDef(
    _SearchEntitiesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `SearchEntitiesPaginate` `PaginationConfig`

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


_SearchEntitiesPaginateResponsedescriptionsdefinitionTypeDef = TypedDict(
    "_SearchEntitiesPaginateResponsedescriptionsdefinitionTypeDef",
    {"language": str, "text": str},
    total=False,
)


class SearchEntitiesPaginateResponsedescriptionsdefinitionTypeDef(
    _SearchEntitiesPaginateResponsedescriptionsdefinitionTypeDef
):
    """
    Type definition for `SearchEntitiesPaginateResponsedescriptions` `definition`

    The definition document of the entity.

    - **language** *(string) --*

      The language used to define the entity. ``GRAPHQL`` is the only valid value.

    - **text** *(string) --*

      The GraphQL text that defines the entity.
    """


_SearchEntitiesPaginateResponsedescriptionsTypeDef = TypedDict(
    "_SearchEntitiesPaginateResponsedescriptionsTypeDef",
    {
        "id": str,
        "arn": str,
        "type": str,
        "createdAt": datetime,
        "definition": SearchEntitiesPaginateResponsedescriptionsdefinitionTypeDef,
    },
    total=False,
)


class SearchEntitiesPaginateResponsedescriptionsTypeDef(
    _SearchEntitiesPaginateResponsedescriptionsTypeDef
):
    """
    Type definition for `SearchEntitiesPaginateResponse` `descriptions`

    Describes the properties of an entity.

    - **id** *(string) --*

      The entity ID.

    - **arn** *(string) --*

      The entity ARN.

    - **type** *(string) --*

      The entity type.

    - **createdAt** *(datetime) --*

      The time at which the entity was created.

    - **definition** *(dict) --*

      The definition document of the entity.

      - **language** *(string) --*

        The language used to define the entity. ``GRAPHQL`` is the only valid value.

      - **text** *(string) --*

        The GraphQL text that defines the entity.
    """


_SearchEntitiesPaginateResponseTypeDef = TypedDict(
    "_SearchEntitiesPaginateResponseTypeDef",
    {
        "descriptions": List[SearchEntitiesPaginateResponsedescriptionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class SearchEntitiesPaginateResponseTypeDef(_SearchEntitiesPaginateResponseTypeDef):
    """
    Type definition for `SearchEntitiesPaginate` `Response`

    - **descriptions** *(list) --*

      An array of descriptions for each entity returned in the search result.

      - *(dict) --*

        Describes the properties of an entity.

        - **id** *(string) --*

          The entity ID.

        - **arn** *(string) --*

          The entity ARN.

        - **type** *(string) --*

          The entity type.

        - **createdAt** *(datetime) --*

          The time at which the entity was created.

        - **definition** *(dict) --*

          The definition document of the entity.

          - **language** *(string) --*

            The language used to define the entity. ``GRAPHQL`` is the only valid value.

          - **text** *(string) --*

            The GraphQL text that defines the entity.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_SearchEntitiesPaginatefiltersTypeDef = TypedDict(
    "_SearchEntitiesPaginatefiltersTypeDef",
    {"name": str, "value": List[str]},
    total=False,
)


class SearchEntitiesPaginatefiltersTypeDef(_SearchEntitiesPaginatefiltersTypeDef):
    """
    Type definition for `SearchEntitiesPaginate` `filters`

    An object that filters an entity search. Multiple filters function as OR criteria in the
    search. For example a search that includes a ``NAMESPACE`` and a ``REFERENCED_ENTITY_ID``
    filter searches for entities in the specified namespace that use the entity specified by the
    value of ``REFERENCED_ENTITY_ID`` .

    - **name** *(string) --*

      The name of the entity search filter field. ``REFERENCED_ENTITY_ID`` filters on entities that
      are used by the entity in the result set. For example, you can filter on the ID of a property
      that is used in a state.

    - **value** *(list) --*

      An array of string values for the search filter field. Multiple values function as AND
      criteria in the search.

      - *(string) --*
    """


_SearchFlowExecutionsPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchFlowExecutionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchFlowExecutionsPaginatePaginationConfigTypeDef(
    _SearchFlowExecutionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `SearchFlowExecutionsPaginate` `PaginationConfig`

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


_SearchFlowExecutionsPaginateResponsesummariesTypeDef = TypedDict(
    "_SearchFlowExecutionsPaginateResponsesummariesTypeDef",
    {
        "flowExecutionId": str,
        "status": str,
        "systemInstanceId": str,
        "flowTemplateId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
    total=False,
)


class SearchFlowExecutionsPaginateResponsesummariesTypeDef(
    _SearchFlowExecutionsPaginateResponsesummariesTypeDef
):
    """
    Type definition for `SearchFlowExecutionsPaginateResponse` `summaries`

    An object that contains summary information about a flow execution.

    - **flowExecutionId** *(string) --*

      The ID of the flow execution.

    - **status** *(string) --*

      The current status of the flow execution.

    - **systemInstanceId** *(string) --*

      The ID of the system instance that contains the flow.

    - **flowTemplateId** *(string) --*

      The ID of the flow.

    - **createdAt** *(datetime) --*

      The date and time when the flow execution summary was created.

    - **updatedAt** *(datetime) --*

      The date and time when the flow execution summary was last updated.
    """


_SearchFlowExecutionsPaginateResponseTypeDef = TypedDict(
    "_SearchFlowExecutionsPaginateResponseTypeDef",
    {
        "summaries": List[SearchFlowExecutionsPaginateResponsesummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class SearchFlowExecutionsPaginateResponseTypeDef(
    _SearchFlowExecutionsPaginateResponseTypeDef
):
    """
    Type definition for `SearchFlowExecutionsPaginate` `Response`

    - **summaries** *(list) --*

      An array of objects that contain summary information about each workflow execution in the
      result set.

      - *(dict) --*

        An object that contains summary information about a flow execution.

        - **flowExecutionId** *(string) --*

          The ID of the flow execution.

        - **status** *(string) --*

          The current status of the flow execution.

        - **systemInstanceId** *(string) --*

          The ID of the system instance that contains the flow.

        - **flowTemplateId** *(string) --*

          The ID of the flow.

        - **createdAt** *(datetime) --*

          The date and time when the flow execution summary was created.

        - **updatedAt** *(datetime) --*

          The date and time when the flow execution summary was last updated.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_SearchFlowTemplatesPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchFlowTemplatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchFlowTemplatesPaginatePaginationConfigTypeDef(
    _SearchFlowTemplatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `SearchFlowTemplatesPaginate` `PaginationConfig`

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


_SearchFlowTemplatesPaginateResponsesummariesTypeDef = TypedDict(
    "_SearchFlowTemplatesPaginateResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class SearchFlowTemplatesPaginateResponsesummariesTypeDef(
    _SearchFlowTemplatesPaginateResponsesummariesTypeDef
):
    """
    Type definition for `SearchFlowTemplatesPaginateResponse` `summaries`

    An object that contains summary information about a workflow.

    - **id** *(string) --*

      The ID of the workflow.

    - **arn** *(string) --*

      The ARN of the workflow.

    - **revisionNumber** *(integer) --*

      The revision number of the workflow.

    - **createdAt** *(datetime) --*

      The date when the workflow was created.
    """


_SearchFlowTemplatesPaginateResponseTypeDef = TypedDict(
    "_SearchFlowTemplatesPaginateResponseTypeDef",
    {
        "summaries": List[SearchFlowTemplatesPaginateResponsesummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class SearchFlowTemplatesPaginateResponseTypeDef(
    _SearchFlowTemplatesPaginateResponseTypeDef
):
    """
    Type definition for `SearchFlowTemplatesPaginate` `Response`

    - **summaries** *(list) --*

      An array of objects that contain summary information about each workflow in the result set.

      - *(dict) --*

        An object that contains summary information about a workflow.

        - **id** *(string) --*

          The ID of the workflow.

        - **arn** *(string) --*

          The ARN of the workflow.

        - **revisionNumber** *(integer) --*

          The revision number of the workflow.

        - **createdAt** *(datetime) --*

          The date when the workflow was created.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_SearchFlowTemplatesPaginatefiltersTypeDef = TypedDict(
    "_SearchFlowTemplatesPaginatefiltersTypeDef", {"name": str, "value": List[str]}
)


class SearchFlowTemplatesPaginatefiltersTypeDef(
    _SearchFlowTemplatesPaginatefiltersTypeDef
):
    """
    Type definition for `SearchFlowTemplatesPaginate` `filters`

    An object that filters a workflow search.

    - **name** *(string) --* **[REQUIRED]**

      The name of the search filter field.

    - **value** *(list) --* **[REQUIRED]**

      An array of string values for the search filter field. Multiple values function as AND
      criteria in the search.

      - *(string) --*
    """


_SearchSystemInstancesPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchSystemInstancesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchSystemInstancesPaginatePaginationConfigTypeDef(
    _SearchSystemInstancesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `SearchSystemInstancesPaginate` `PaginationConfig`

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


_SearchSystemInstancesPaginateResponsesummariesTypeDef = TypedDict(
    "_SearchSystemInstancesPaginateResponsesummariesTypeDef",
    {
        "id": str,
        "arn": str,
        "status": str,
        "target": str,
        "greengrassGroupName": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "greengrassGroupId": str,
        "greengrassGroupVersionId": str,
    },
    total=False,
)


class SearchSystemInstancesPaginateResponsesummariesTypeDef(
    _SearchSystemInstancesPaginateResponsesummariesTypeDef
):
    """
    Type definition for `SearchSystemInstancesPaginateResponse` `summaries`

    An object that contains summary information about a system instance.

    - **id** *(string) --*

      The ID of the system instance.

    - **arn** *(string) --*

      The ARN of the system instance.

    - **status** *(string) --*

      The status of the system instance.

    - **target** *(string) --*

      The target of the system instance.

    - **greengrassGroupName** *(string) --*

      The ID of the Greengrass group where the system instance is deployed.

    - **createdAt** *(datetime) --*

      The date when the system instance was created.

    - **updatedAt** *(datetime) --*

      The date and time when the system instance was last updated.

    - **greengrassGroupId** *(string) --*

      The ID of the Greengrass group where the system instance is deployed.

    - **greengrassGroupVersionId** *(string) --*

      The version of the Greengrass group where the system instance is deployed.
    """


_SearchSystemInstancesPaginateResponseTypeDef = TypedDict(
    "_SearchSystemInstancesPaginateResponseTypeDef",
    {
        "summaries": List[SearchSystemInstancesPaginateResponsesummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class SearchSystemInstancesPaginateResponseTypeDef(
    _SearchSystemInstancesPaginateResponseTypeDef
):
    """
    Type definition for `SearchSystemInstancesPaginate` `Response`

    - **summaries** *(list) --*

      An array of objects that contain summary data abour the system instances in the result set.

      - *(dict) --*

        An object that contains summary information about a system instance.

        - **id** *(string) --*

          The ID of the system instance.

        - **arn** *(string) --*

          The ARN of the system instance.

        - **status** *(string) --*

          The status of the system instance.

        - **target** *(string) --*

          The target of the system instance.

        - **greengrassGroupName** *(string) --*

          The ID of the Greengrass group where the system instance is deployed.

        - **createdAt** *(datetime) --*

          The date when the system instance was created.

        - **updatedAt** *(datetime) --*

          The date and time when the system instance was last updated.

        - **greengrassGroupId** *(string) --*

          The ID of the Greengrass group where the system instance is deployed.

        - **greengrassGroupVersionId** *(string) --*

          The version of the Greengrass group where the system instance is deployed.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_SearchSystemInstancesPaginatefiltersTypeDef = TypedDict(
    "_SearchSystemInstancesPaginatefiltersTypeDef",
    {"name": str, "value": List[str]},
    total=False,
)


class SearchSystemInstancesPaginatefiltersTypeDef(
    _SearchSystemInstancesPaginatefiltersTypeDef
):
    """
    Type definition for `SearchSystemInstancesPaginate` `filters`

    An object that filters a system instance search. Multiple filters function as OR criteria in
    the search. For example a search that includes a GREENGRASS_GROUP_NAME and a STATUS filter
    searches for system instances in the specified Greengrass group that have the specified status.

    - **name** *(string) --*

      The name of the search filter field.

    - **value** *(list) --*

      An array of string values for the search filter field. Multiple values function as AND
      criteria in the search.

      - *(string) --*
    """


_SearchSystemTemplatesPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchSystemTemplatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchSystemTemplatesPaginatePaginationConfigTypeDef(
    _SearchSystemTemplatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `SearchSystemTemplatesPaginate` `PaginationConfig`

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


_SearchSystemTemplatesPaginateResponsesummariesTypeDef = TypedDict(
    "_SearchSystemTemplatesPaginateResponsesummariesTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class SearchSystemTemplatesPaginateResponsesummariesTypeDef(
    _SearchSystemTemplatesPaginateResponsesummariesTypeDef
):
    """
    Type definition for `SearchSystemTemplatesPaginateResponse` `summaries`

    An object that contains information about a system.

    - **id** *(string) --*

      The ID of the system.

    - **arn** *(string) --*

      The ARN of the system.

    - **revisionNumber** *(integer) --*

      The revision number of the system.

    - **createdAt** *(datetime) --*

      The date when the system was created.
    """


_SearchSystemTemplatesPaginateResponseTypeDef = TypedDict(
    "_SearchSystemTemplatesPaginateResponseTypeDef",
    {
        "summaries": List[SearchSystemTemplatesPaginateResponsesummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class SearchSystemTemplatesPaginateResponseTypeDef(
    _SearchSystemTemplatesPaginateResponseTypeDef
):
    """
    Type definition for `SearchSystemTemplatesPaginate` `Response`

    - **summaries** *(list) --*

      An array of objects that contain summary information about each system deployment in the
      result set.

      - *(dict) --*

        An object that contains information about a system.

        - **id** *(string) --*

          The ID of the system.

        - **arn** *(string) --*

          The ARN of the system.

        - **revisionNumber** *(integer) --*

          The revision number of the system.

        - **createdAt** *(datetime) --*

          The date when the system was created.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_SearchSystemTemplatesPaginatefiltersTypeDef = TypedDict(
    "_SearchSystemTemplatesPaginatefiltersTypeDef", {"name": str, "value": List[str]}
)


class SearchSystemTemplatesPaginatefiltersTypeDef(
    _SearchSystemTemplatesPaginatefiltersTypeDef
):
    """
    Type definition for `SearchSystemTemplatesPaginate` `filters`

    An object that filters a system search.

    - **name** *(string) --* **[REQUIRED]**

      The name of the system search filter field.

    - **value** *(list) --* **[REQUIRED]**

      An array of string values for the search filter field. Multiple values function as AND
      criteria in the search.

      - *(string) --*
    """


_SearchThingsPaginatePaginationConfigTypeDef = TypedDict(
    "_SearchThingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class SearchThingsPaginatePaginationConfigTypeDef(
    _SearchThingsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `SearchThingsPaginate` `PaginationConfig`

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


_SearchThingsPaginateResponsethingsTypeDef = TypedDict(
    "_SearchThingsPaginateResponsethingsTypeDef",
    {"thingArn": str, "thingName": str},
    total=False,
)


class SearchThingsPaginateResponsethingsTypeDef(
    _SearchThingsPaginateResponsethingsTypeDef
):
    """
    Type definition for `SearchThingsPaginateResponse` `things`

    An AWS IoT thing.

    - **thingArn** *(string) --*

      The ARN of the thing.

    - **thingName** *(string) --*

      The name of the thing.
    """


_SearchThingsPaginateResponseTypeDef = TypedDict(
    "_SearchThingsPaginateResponseTypeDef",
    {"things": List[SearchThingsPaginateResponsethingsTypeDef], "NextToken": str},
    total=False,
)


class SearchThingsPaginateResponseTypeDef(_SearchThingsPaginateResponseTypeDef):
    """
    Type definition for `SearchThingsPaginate` `Response`

    - **things** *(list) --*

      An array of things in the result set.

      - *(dict) --*

        An AWS IoT thing.

        - **thingArn** *(string) --*

          The ARN of the thing.

        - **thingName** *(string) --*

          The name of the thing.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """

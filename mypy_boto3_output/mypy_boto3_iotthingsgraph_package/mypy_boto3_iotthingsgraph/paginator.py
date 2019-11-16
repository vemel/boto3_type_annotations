"Main interface for iotthingsgraph Paginators"
from __future__ import annotations

from datetime import datetime
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_iotthingsgraph.type_defs import (
    GetFlowTemplateRevisionsPaginatePaginationConfigTypeDef,
    GetFlowTemplateRevisionsPaginateResponseTypeDef,
    GetSystemTemplateRevisionsPaginatePaginationConfigTypeDef,
    GetSystemTemplateRevisionsPaginateResponseTypeDef,
    ListFlowExecutionMessagesPaginatePaginationConfigTypeDef,
    ListFlowExecutionMessagesPaginateResponseTypeDef,
    ListTagsForResourcePaginatePaginationConfigTypeDef,
    ListTagsForResourcePaginateResponseTypeDef,
    SearchEntitiesPaginatePaginationConfigTypeDef,
    SearchEntitiesPaginateResponseTypeDef,
    SearchEntitiesPaginatefiltersTypeDef,
    SearchFlowExecutionsPaginatePaginationConfigTypeDef,
    SearchFlowExecutionsPaginateResponseTypeDef,
    SearchFlowTemplatesPaginatePaginationConfigTypeDef,
    SearchFlowTemplatesPaginateResponseTypeDef,
    SearchFlowTemplatesPaginatefiltersTypeDef,
    SearchSystemInstancesPaginatePaginationConfigTypeDef,
    SearchSystemInstancesPaginateResponseTypeDef,
    SearchSystemInstancesPaginatefiltersTypeDef,
    SearchSystemTemplatesPaginatePaginationConfigTypeDef,
    SearchSystemTemplatesPaginateResponseTypeDef,
    SearchSystemTemplatesPaginatefiltersTypeDef,
    SearchThingsPaginatePaginationConfigTypeDef,
    SearchThingsPaginateResponseTypeDef,
)


__all__ = (
    "GetFlowTemplateRevisionsPaginator",
    "GetSystemTemplateRevisionsPaginator",
    "ListFlowExecutionMessagesPaginator",
    "ListTagsForResourcePaginator",
    "SearchEntitiesPaginator",
    "SearchFlowExecutionsPaginator",
    "SearchFlowTemplatesPaginator",
    "SearchSystemInstancesPaginator",
    "SearchSystemTemplatesPaginator",
    "SearchThingsPaginator",
)


class GetFlowTemplateRevisionsPaginator(Boto3Paginator):
    """
    Paginator for `get_flow_template_revisions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        id: str,
        PaginationConfig: GetFlowTemplateRevisionsPaginatePaginationConfigTypeDef = None,
    ) -> GetFlowTemplateRevisionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`IoTThingsGraph.Client.get_flow_template_revisions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/GetFlowTemplateRevisions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              id='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type id: string
        :param id: **[REQUIRED]**

          The ID of the workflow.

          The ID should be in the following format.

           ``urn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME``

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'summaries': [
                    {
                        'id': 'string',
                        'arn': 'string',
                        'revisionNumber': 123,
                        'createdAt': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class GetSystemTemplateRevisionsPaginator(Boto3Paginator):
    """
    Paginator for `get_system_template_revisions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        id: str,
        PaginationConfig: GetSystemTemplateRevisionsPaginatePaginationConfigTypeDef = None,
    ) -> GetSystemTemplateRevisionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`IoTThingsGraph.Client.get_system_template_revisions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/GetSystemTemplateRevisions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              id='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type id: string
        :param id: **[REQUIRED]**

          The ID of the system template.

          The ID should be in the following format.

           ``urn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME``

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'summaries': [
                    {
                        'id': 'string',
                        'arn': 'string',
                        'revisionNumber': 123,
                        'createdAt': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class ListFlowExecutionMessagesPaginator(Boto3Paginator):
    """
    Paginator for `list_flow_execution_messages`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        flowExecutionId: str,
        PaginationConfig: ListFlowExecutionMessagesPaginatePaginationConfigTypeDef = None,
    ) -> ListFlowExecutionMessagesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`IoTThingsGraph.Client.list_flow_execution_messages`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/ListFlowExecutionMessages>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              flowExecutionId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type flowExecutionId: string
        :param flowExecutionId: **[REQUIRED]**

          The ID of the flow execution.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'messages': [
                    {
                        'messageId': 'string',
                        'eventType':
                        'EXECUTION_STARTED'|'EXECUTION_FAILED'|'EXECUTION_ABORTED'|'EXECUTION_SUCCEEDED'
                        |'STEP_STARTED'|'STEP_FAILED'|'STEP_SUCCEEDED'|'ACTIVITY_SCHEDULED'
                        |'ACTIVITY_STARTED'|'ACTIVITY_FAILED'|'ACTIVITY_SUCCEEDED'
                        |'START_FLOW_EXECUTION_TASK'|'SCHEDULE_NEXT_READY_STEPS_TASK'|'THING_ACTION_TASK'
                        |'THING_ACTION_TASK_FAILED'|'THING_ACTION_TASK_SUCCEEDED'
                        |'ACKNOWLEDGE_TASK_MESSAGE',
                        'timestamp': datetime(2015, 1, 1),
                        'payload': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    Paginator for `list_tags_for_resource`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        resourceArn: str,
        PaginationConfig: ListTagsForResourcePaginatePaginationConfigTypeDef = None,
    ) -> ListTagsForResourcePaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`IoTThingsGraph.Client.list_tags_for_resource`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/ListTagsForResource>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              resourceArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource whose tags are to be returned.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class SearchEntitiesPaginator(Boto3Paginator):
    """
    Paginator for `search_entities`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        entityTypes: List[str],
        filters: List[SearchEntitiesPaginatefiltersTypeDef] = None,
        namespaceVersion: int = None,
        PaginationConfig: SearchEntitiesPaginatePaginationConfigTypeDef = None,
    ) -> SearchEntitiesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`IoTThingsGraph.Client.search_entities`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/SearchEntities>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              entityTypes=[
                  'DEVICE'|'SERVICE'|'DEVICE_MODEL'|'CAPABILITY'|'STATE'|'ACTION'|'EVENT'|'PROPERTY'
                  |'MAPPING'|'ENUM',
              ],
              filters=[
                  {
                      'name': 'NAME'|'NAMESPACE'|'SEMANTIC_TYPE_PATH'|'REFERENCED_ENTITY_ID',
                      'value': [
                          'string',
                      ]
                  },
              ],
              namespaceVersion=123,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type entityTypes: list
        :param entityTypes: **[REQUIRED]**

          The entity types for which to search.

          - *(string) --*

        :type filters: list
        :param filters:

          Optional filter to apply to the search. Valid filters are ``NAME``  ``NAMESPACE`` ,
          ``SEMANTIC_TYPE_PATH`` and ``REFERENCED_ENTITY_ID`` . ``REFERENCED_ENTITY_ID`` filters on
          entities that are used by the entity in the result set. For example, you can filter on the ID of
          a property that is used in a state.

          Multiple filters function as OR criteria in the query. Multiple values passed inside the filter
          function as AND criteria.

          - *(dict) --*

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

        :type namespaceVersion: integer
        :param namespaceVersion:

          The version of the user's namespace. Defaults to the latest version of the user's namespace.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'descriptions': [
                    {
                        'id': 'string',
                        'arn': 'string',
                        'type':
                        'DEVICE'|'SERVICE'|'DEVICE_MODEL'|'CAPABILITY'|'STATE'|'ACTION'|'EVENT'|'PROPERTY'
                        |'MAPPING'|'ENUM',
                        'createdAt': datetime(2015, 1, 1),
                        'definition': {
                            'language': 'GRAPHQL',
                            'text': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class SearchFlowExecutionsPaginator(Boto3Paginator):
    """
    Paginator for `search_flow_executions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        systemInstanceId: str,
        flowExecutionId: str = None,
        startTime: datetime = None,
        endTime: datetime = None,
        PaginationConfig: SearchFlowExecutionsPaginatePaginationConfigTypeDef = None,
    ) -> SearchFlowExecutionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`IoTThingsGraph.Client.search_flow_executions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/SearchFlowExecutions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              systemInstanceId='string',
              flowExecutionId='string',
              startTime=datetime(2015, 1, 1),
              endTime=datetime(2015, 1, 1),
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type systemInstanceId: string
        :param systemInstanceId: **[REQUIRED]**

          The ID of the system instance that contains the flow.

        :type flowExecutionId: string
        :param flowExecutionId:

          The ID of a flow execution.

        :type startTime: datetime
        :param startTime:

          The date and time of the earliest flow execution to return.

        :type endTime: datetime
        :param endTime:

          The date and time of the latest flow execution to return.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'summaries': [
                    {
                        'flowExecutionId': 'string',
                        'status': 'RUNNING'|'ABORTED'|'SUCCEEDED'|'FAILED',
                        'systemInstanceId': 'string',
                        'flowTemplateId': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'updatedAt': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class SearchFlowTemplatesPaginator(Boto3Paginator):
    """
    Paginator for `search_flow_templates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filters: List[SearchFlowTemplatesPaginatefiltersTypeDef] = None,
        PaginationConfig: SearchFlowTemplatesPaginatePaginationConfigTypeDef = None,
    ) -> SearchFlowTemplatesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`IoTThingsGraph.Client.search_flow_templates`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/SearchFlowTemplates>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              filters=[
                  {
                      'name': 'DEVICE_MODEL_ID',
                      'value': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type filters: list
        :param filters:

          An array of objects that limit the result set. The only valid filter is ``DEVICE_MODEL_ID`` .

          - *(dict) --*

            An object that filters a workflow search.

            - **name** *(string) --* **[REQUIRED]**

              The name of the search filter field.

            - **value** *(list) --* **[REQUIRED]**

              An array of string values for the search filter field. Multiple values function as AND
              criteria in the search.

              - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'summaries': [
                    {
                        'id': 'string',
                        'arn': 'string',
                        'revisionNumber': 123,
                        'createdAt': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class SearchSystemInstancesPaginator(Boto3Paginator):
    """
    Paginator for `search_system_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filters: List[SearchSystemInstancesPaginatefiltersTypeDef] = None,
        PaginationConfig: SearchSystemInstancesPaginatePaginationConfigTypeDef = None,
    ) -> SearchSystemInstancesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`IoTThingsGraph.Client.search_system_instances`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/SearchSystemInstances>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              filters=[
                  {
                      'name': 'SYSTEM_TEMPLATE_ID'|'STATUS'|'GREENGRASS_GROUP_NAME',
                      'value': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type filters: list
        :param filters:

          Optional filter to apply to the search. Valid filters are ``SYSTEM_TEMPLATE_ID`` , ``STATUS`` ,
          and ``GREENGRASS_GROUP_NAME`` .

          Multiple filters function as OR criteria in the query. Multiple values passed inside the filter
          function as AND criteria.

          - *(dict) --*

            An object that filters a system instance search. Multiple filters function as OR criteria in
            the search. For example a search that includes a GREENGRASS_GROUP_NAME and a STATUS filter
            searches for system instances in the specified Greengrass group that have the specified status.

            - **name** *(string) --*

              The name of the search filter field.

            - **value** *(list) --*

              An array of string values for the search filter field. Multiple values function as AND
              criteria in the search.

              - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'summaries': [
                    {
                        'id': 'string',
                        'arn': 'string',
                        'status':
                        'NOT_DEPLOYED'|'BOOTSTRAP'|'DEPLOY_IN_PROGRESS'|'DEPLOYED_IN_TARGET'
                        |'UNDEPLOY_IN_PROGRESS'|'FAILED'|'PENDING_DELETE'|'DELETED_IN_TARGET',
                        'target': 'GREENGRASS'|'CLOUD',
                        'greengrassGroupName': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'updatedAt': datetime(2015, 1, 1),
                        'greengrassGroupId': 'string',
                        'greengrassGroupVersionId': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class SearchSystemTemplatesPaginator(Boto3Paginator):
    """
    Paginator for `search_system_templates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        filters: List[SearchSystemTemplatesPaginatefiltersTypeDef] = None,
        PaginationConfig: SearchSystemTemplatesPaginatePaginationConfigTypeDef = None,
    ) -> SearchSystemTemplatesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`IoTThingsGraph.Client.search_system_templates`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/SearchSystemTemplates>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              filters=[
                  {
                      'name': 'FLOW_TEMPLATE_ID',
                      'value': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type filters: list
        :param filters:

          An array of filters that limit the result set. The only valid filter is ``FLOW_TEMPLATE_ID`` .

          - *(dict) --*

            An object that filters a system search.

            - **name** *(string) --* **[REQUIRED]**

              The name of the system search filter field.

            - **value** *(list) --* **[REQUIRED]**

              An array of string values for the search filter field. Multiple values function as AND
              criteria in the search.

              - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'summaries': [
                    {
                        'id': 'string',
                        'arn': 'string',
                        'revisionNumber': 123,
                        'createdAt': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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


class SearchThingsPaginator(Boto3Paginator):
    """
    Paginator for `search_things`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        entityId: str,
        namespaceVersion: int = None,
        PaginationConfig: SearchThingsPaginatePaginationConfigTypeDef = None,
    ) -> SearchThingsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`IoTThingsGraph.Client.search_things`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/SearchThings>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              entityId='string',
              namespaceVersion=123,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type entityId: string
        :param entityId: **[REQUIRED]**

          The ID of the entity to which the things are associated.

          The IDs should be in the following format.

           ``urn:tdm:REGION/ACCOUNT ID/default:device:DEVICENAME``

        :type namespaceVersion: integer
        :param namespaceVersion:

          The version of the user's namespace. Defaults to the latest version of the user's namespace.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'things': [
                    {
                        'thingArn': 'string',
                        'thingName': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

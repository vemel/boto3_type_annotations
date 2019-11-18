"Main interface for connect Client"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_connect.client as client_scope

# pylint: disable=import-self
import mypy_boto3_connect.paginator as paginator_scope
from mypy_boto3_connect.type_defs import (
    ClientCreateUserIdentityInfoTypeDef,
    ClientCreateUserPhoneConfigTypeDef,
    ClientCreateUserResponseTypeDef,
    ClientDescribeUserHierarchyGroupResponseTypeDef,
    ClientDescribeUserHierarchyStructureResponseTypeDef,
    ClientDescribeUserResponseTypeDef,
    ClientGetContactAttributesResponseTypeDef,
    ClientGetCurrentMetricDataCurrentMetricsTypeDef,
    ClientGetCurrentMetricDataFiltersTypeDef,
    ClientGetCurrentMetricDataResponseTypeDef,
    ClientGetFederationTokenResponseTypeDef,
    ClientGetMetricDataFiltersTypeDef,
    ClientGetMetricDataHistoricalMetricsTypeDef,
    ClientGetMetricDataResponseTypeDef,
    ClientListContactFlowsResponseTypeDef,
    ClientListHoursOfOperationsResponseTypeDef,
    ClientListPhoneNumbersResponseTypeDef,
    ClientListQueuesResponseTypeDef,
    ClientListRoutingProfilesResponseTypeDef,
    ClientListSecurityProfilesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListUserHierarchyGroupsResponseTypeDef,
    ClientListUsersResponseTypeDef,
    ClientStartOutboundVoiceContactResponseTypeDef,
    ClientUpdateUserIdentityInfoIdentityInfoTypeDef,
    ClientUpdateUserPhoneConfigPhoneConfigTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> None:
        """
        Check if an operation can be paginated.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_user(
        self,
        Username: str,
        PhoneConfig: ClientCreateUserPhoneConfigTypeDef,
        SecurityProfileIds: List[str],
        RoutingProfileId: str,
        InstanceId: str,
        Password: str = None,
        IdentityInfo: ClientCreateUserIdentityInfoTypeDef = None,
        DirectoryUserId: str = None,
        HierarchyGroupId: str = None,
        Tags: List[str] = None,
    ) -> ClientCreateUserResponseTypeDef:
        """
        Creates a user account for the specified Amazon Connect instance.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/CreateUser>`_

        **Request Syntax**
        ::

          response = client.create_user(
              Username='string',
              Password='string',
              IdentityInfo={
                  'FirstName': 'string',
                  'LastName': 'string',
                  'Email': 'string'
              },
              PhoneConfig={
                  'PhoneType': 'SOFT_PHONE'|'DESK_PHONE',
                  'AutoAccept': True|False,
                  'AfterContactWorkTimeLimit': 123,
                  'DeskPhoneNumber': 'string'
              },
              DirectoryUserId='string',
              SecurityProfileIds=[
                  'string',
              ],
              RoutingProfileId='string',
              HierarchyGroupId='string',
              InstanceId='string',
              Tags={
                  'string': 'string'
              }
          )
        :type Username: string
        :param Username: **[REQUIRED]**

          The user name for the account. For instances not using SAML for identity management, the user
          name can include up to 20 characters. If you are using SAML for identity management, the user
          name can include up to 64 characters from [a-zA-Z0-9_-.\\@]+.

        :type Password: string
        :param Password:

          The password for the user account. A password is required if you are using Amazon Connect for
          identity management. Otherwise, it is an error to include a password.

        :type IdentityInfo: dict
        :param IdentityInfo:

          The information about the identity of the user.

          - **FirstName** *(string) --*

            The first name. This is required if you are using Amazon Connect or SAML for identity
            management.

          - **LastName** *(string) --*

            The last name. This is required if you are using Amazon Connect or SAML for identity management.

          - **Email** *(string) --*

            The email address. If you are using SAML for identity management and include this parameter, an
            error is returned.

        :type PhoneConfig: dict
        :param PhoneConfig: **[REQUIRED]**

          The phone settings for the user.

          - **PhoneType** *(string) --* **[REQUIRED]**

            The phone type.

          - **AutoAccept** *(boolean) --*

            The Auto accept setting.

          - **AfterContactWorkTimeLimit** *(integer) --*

            The After Call Work (ACW) timeout setting, in seconds.

          - **DeskPhoneNumber** *(string) --*

            The phone number for the user's desk phone.

        :type DirectoryUserId: string
        :param DirectoryUserId:

          The identifier of the user account in the directory used for identity management. If Amazon
          Connect cannot access the directory, you can specify this identifier to authenticate users. If
          you include the identifier, we assume that Amazon Connect cannot access the directory. Otherwise,
          the identity information is used to authenticate users from your directory.

          This parameter is required if you are using an existing directory for identity management in
          Amazon Connect when Amazon Connect cannot access your directory to authenticate users. If you are
          using SAML for identity management and include this parameter, an error is returned.

        :type SecurityProfileIds: list
        :param SecurityProfileIds: **[REQUIRED]**

          The identifier of the security profile for the user.

          - *(string) --*

        :type RoutingProfileId: string
        :param RoutingProfileId: **[REQUIRED]**

          The identifier of the routing profile for the user.

        :type HierarchyGroupId: string
        :param HierarchyGroupId:

          The identifier of the hierarchy group for the user.

        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type Tags: dict
        :param Tags:

          One or more tags.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UserId': 'string',
                'UserArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **UserId** *(string) --*

              The identifier of the user account.

            - **UserArn** *(string) --*

              The Amazon Resource Name (ARN) of the user account.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_user(self, InstanceId: str, UserId: str) -> None:
        """
        Deletes a user account from the specified Amazon Connect instance.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/DeleteUser>`_

        **Request Syntax**
        ::

          response = client.delete_user(
              InstanceId='string',
              UserId='string'
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The identifier of the user.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_user(
        self, UserId: str, InstanceId: str
    ) -> ClientDescribeUserResponseTypeDef:
        """
        Describes the specified user account. You can find the instance ID in the console (it’s the final
        part of the ARN). The console does not display the user IDs. Instead, list the users and note the
        IDs provided in the output.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/DescribeUser>`_

        **Request Syntax**
        ::

          response = client.describe_user(
              UserId='string',
              InstanceId='string'
          )
        :type UserId: string
        :param UserId: **[REQUIRED]**

          The identifier of the user account.

        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'User': {
                    'Id': 'string',
                    'Arn': 'string',
                    'Username': 'string',
                    'IdentityInfo': {
                        'FirstName': 'string',
                        'LastName': 'string',
                        'Email': 'string'
                    },
                    'PhoneConfig': {
                        'PhoneType': 'SOFT_PHONE'|'DESK_PHONE',
                        'AutoAccept': True|False,
                        'AfterContactWorkTimeLimit': 123,
                        'DeskPhoneNumber': 'string'
                    },
                    'DirectoryUserId': 'string',
                    'SecurityProfileIds': [
                        'string',
                    ],
                    'RoutingProfileId': 'string',
                    'HierarchyGroupId': 'string',
                    'Tags': {
                        'string': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **User** *(dict) --*

              Information about the user account and configuration settings.

              - **Id** *(string) --*

                The identifier of the user account.

              - **Arn** *(string) --*

                The Amazon Resource Name (ARN) of the user account.

              - **Username** *(string) --*

                The user name assigned to the user account.

              - **IdentityInfo** *(dict) --*

                Information about the user identity.

                - **FirstName** *(string) --*

                  The first name. This is required if you are using Amazon Connect or SAML for identity
                  management.

                - **LastName** *(string) --*

                  The last name. This is required if you are using Amazon Connect or SAML for identity
                  management.

                - **Email** *(string) --*

                  The email address. If you are using SAML for identity management and include this
                  parameter, an error is returned.

              - **PhoneConfig** *(dict) --*

                Information about the phone configuration for the user.

                - **PhoneType** *(string) --*

                  The phone type.

                - **AutoAccept** *(boolean) --*

                  The Auto accept setting.

                - **AfterContactWorkTimeLimit** *(integer) --*

                  The After Call Work (ACW) timeout setting, in seconds.

                - **DeskPhoneNumber** *(string) --*

                  The phone number for the user's desk phone.

              - **DirectoryUserId** *(string) --*

                The identifier of the user account in the directory used for identity management.

              - **SecurityProfileIds** *(list) --*

                The identifiers of the security profiles for the user.

                - *(string) --*

              - **RoutingProfileId** *(string) --*

                The identifier of the routing profile for the user.

              - **HierarchyGroupId** *(string) --*

                The identifier of the hierarchy group for the user.

              - **Tags** *(dict) --*

                The tags.

                - *(string) --*

                  - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_user_hierarchy_group(
        self, HierarchyGroupId: str, InstanceId: str
    ) -> ClientDescribeUserHierarchyGroupResponseTypeDef:
        """
        Describes the specified hierarchy group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/DescribeUserHierarchyGroup>`_

        **Request Syntax**
        ::

          response = client.describe_user_hierarchy_group(
              HierarchyGroupId='string',
              InstanceId='string'
          )
        :type HierarchyGroupId: string
        :param HierarchyGroupId: **[REQUIRED]**

          The identifier of the hierarchy group.

        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'HierarchyGroup': {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string',
                    'LevelId': 'string',
                    'HierarchyPath': {
                        'LevelOne': {
                            'Id': 'string',
                            'Arn': 'string',
                            'Name': 'string'
                        },
                        'LevelTwo': {
                            'Id': 'string',
                            'Arn': 'string',
                            'Name': 'string'
                        },
                        'LevelThree': {
                            'Id': 'string',
                            'Arn': 'string',
                            'Name': 'string'
                        },
                        'LevelFour': {
                            'Id': 'string',
                            'Arn': 'string',
                            'Name': 'string'
                        },
                        'LevelFive': {
                            'Id': 'string',
                            'Arn': 'string',
                            'Name': 'string'
                        }
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **HierarchyGroup** *(dict) --*

              Information about the hierarchy group.

              - **Id** *(string) --*

                The identifier of the hierarchy group.

              - **Arn** *(string) --*

                The Amazon Resource Name (ARN) of the hierarchy group.

              - **Name** *(string) --*

                The name of the hierarchy group.

              - **LevelId** *(string) --*

                The identifier of the level in the hierarchy group.

              - **HierarchyPath** *(dict) --*

                Information about the levels in the hierarchy group.

                - **LevelOne** *(dict) --*

                  Information about level one.

                  - **Id** *(string) --*

                    The identifier of the hierarchy group.

                  - **Arn** *(string) --*

                    The Amazon Resource Name (ARN) of the hierarchy group.

                  - **Name** *(string) --*

                    The name of the hierarchy group.

                - **LevelTwo** *(dict) --*

                  Information about level two.

                  - **Id** *(string) --*

                    The identifier of the hierarchy group.

                  - **Arn** *(string) --*

                    The Amazon Resource Name (ARN) of the hierarchy group.

                  - **Name** *(string) --*

                    The name of the hierarchy group.

                - **LevelThree** *(dict) --*

                  Information about level three.

                  - **Id** *(string) --*

                    The identifier of the hierarchy group.

                  - **Arn** *(string) --*

                    The Amazon Resource Name (ARN) of the hierarchy group.

                  - **Name** *(string) --*

                    The name of the hierarchy group.

                - **LevelFour** *(dict) --*

                  Information about level four.

                  - **Id** *(string) --*

                    The identifier of the hierarchy group.

                  - **Arn** *(string) --*

                    The Amazon Resource Name (ARN) of the hierarchy group.

                  - **Name** *(string) --*

                    The name of the hierarchy group.

                - **LevelFive** *(dict) --*

                  Information about level five.

                  - **Id** *(string) --*

                    The identifier of the hierarchy group.

                  - **Arn** *(string) --*

                    The Amazon Resource Name (ARN) of the hierarchy group.

                  - **Name** *(string) --*

                    The name of the hierarchy group.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_user_hierarchy_structure(
        self, InstanceId: str
    ) -> ClientDescribeUserHierarchyStructureResponseTypeDef:
        """
        Describes the hierarchy structure of the specified Amazon Connect instance.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/DescribeUserHierarchyStructure>`_

        **Request Syntax**
        ::

          response = client.describe_user_hierarchy_structure(
              InstanceId='string'
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'HierarchyStructure': {
                    'LevelOne': {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string'
                    },
                    'LevelTwo': {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string'
                    },
                    'LevelThree': {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string'
                    },
                    'LevelFour': {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string'
                    },
                    'LevelFive': {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **HierarchyStructure** *(dict) --*

              Information about the hierarchy structure.

              - **LevelOne** *(dict) --*

                Information about level one.

                - **Id** *(string) --*

                  The identifier of the hierarchy level.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the hierarchy level.

                - **Name** *(string) --*

                  The name of the hierarchy level.

              - **LevelTwo** *(dict) --*

                Information about level two.

                - **Id** *(string) --*

                  The identifier of the hierarchy level.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the hierarchy level.

                - **Name** *(string) --*

                  The name of the hierarchy level.

              - **LevelThree** *(dict) --*

                Information about level three.

                - **Id** *(string) --*

                  The identifier of the hierarchy level.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the hierarchy level.

                - **Name** *(string) --*

                  The name of the hierarchy level.

              - **LevelFour** *(dict) --*

                Information about level four.

                - **Id** *(string) --*

                  The identifier of the hierarchy level.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the hierarchy level.

                - **Name** *(string) --*

                  The name of the hierarchy level.

              - **LevelFive** *(dict) --*

                Information about level five.

                - **Id** *(string) --*

                  The identifier of the hierarchy level.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the hierarchy level.

                - **Name** *(string) --*

                  The name of the hierarchy level.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        Generate a presigned url given a client, its method, and arguments

        :type ClientMethod: string
        :param ClientMethod: The client method to presign for

        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.

        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

        :returns: The presigned url
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_contact_attributes(
        self, InstanceId: str, InitialContactId: str
    ) -> ClientGetContactAttributesResponseTypeDef:
        """
        Retrieves the contact attributes for the specified contact.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/GetContactAttributes>`_

        **Request Syntax**
        ::

          response = client.get_contact_attributes(
              InstanceId='string',
              InitialContactId='string'
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type InitialContactId: string
        :param InitialContactId: **[REQUIRED]**

          The identifier of the initial contact.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Attributes': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Attributes** *(dict) --*

              Information about the attributes.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_current_metric_data(
        self,
        InstanceId: str,
        Filters: ClientGetCurrentMetricDataFiltersTypeDef,
        CurrentMetrics: List[ClientGetCurrentMetricDataCurrentMetricsTypeDef],
        Groupings: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetCurrentMetricDataResponseTypeDef:
        """
        Gets the real-time metric data from the specified Amazon Connect instance.

        For more information, see `Real-time Metrics Reports
        <https://docs.aws.amazon.com/connect/latest/adminguide/real-time-metrics-reports.html>`__ in the
        *Amazon Connect Administrator Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/GetCurrentMetricData>`_

        **Request Syntax**
        ::

          response = client.get_current_metric_data(
              InstanceId='string',
              Filters={
                  'Queues': [
                      'string',
                  ],
                  'Channels': [
                      'VOICE',
                  ]
              },
              Groupings=[
                  'QUEUE'|'CHANNEL',
              ],
              CurrentMetrics=[
                  {
                      'Name':
                      'AGENTS_ONLINE'|'AGENTS_AVAILABLE'|'AGENTS_ON_CALL'|'AGENTS_NON_PRODUCTIVE'
                      |'AGENTS_AFTER_CONTACT_WORK'|'AGENTS_ERROR'|'AGENTS_STAFFED'|'CONTACTS_IN_QUEUE'
                      |'OLDEST_CONTACT_AGE'|'CONTACTS_SCHEDULED',
                      'Unit': 'SECONDS'|'COUNT'|'PERCENT'
                  },
              ],
              NextToken='string',
              MaxResults=123
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type Filters: dict
        :param Filters: **[REQUIRED]**

          The queues, up to 100, or channels, to use to filter the metrics returned. Metric data is
          retrieved only for the resources associated with the queues or channels included in the filter.
          You can include both queue IDs and queue ARNs in the same request. The only supported channel is
          ``VOICE`` .

          - **Queues** *(list) --*

            The queues to use to filter the metrics. You can specify up to 100 queues per request.

            - *(string) --*

          - **Channels** *(list) --*

            The channel to use to filter the metrics.

            - *(string) --*

        :type Groupings: list
        :param Groupings:

          The grouping applied to the metrics returned. For example, when grouped by ``QUEUE`` , the
          metrics returned apply to each queue rather than aggregated for all queues. If you group by
          ``CHANNEL`` , you should include a Channels filter. The only supported channel is ``VOICE`` .

          If no ``Grouping`` is included in the request, a summary of metrics is returned.

          - *(string) --*

        :type CurrentMetrics: list
        :param CurrentMetrics: **[REQUIRED]**

          The metrics to retrieve. Specify the name and unit for each metric. The following metrics are
          available:

            AGENTS_AFTER_CONTACT_WORK

          Unit: COUNT

            AGENTS_AVAILABLE

          Unit: COUNT

            AGENTS_ERROR

          Unit: COUNT

            AGENTS_NON_PRODUCTIVE

          Unit: COUNT

            AGENTS_ON_CALL

          Unit: COUNT

            AGENTS_ONLINE

          Unit: COUNT

            AGENTS_STAFFED

          Unit: COUNT

            CONTACTS_IN_QUEUE

          Unit: COUNT

            CONTACTS_SCHEDULED

          Unit: COUNT

            OLDEST_CONTACT_AGE

          Unit: SECONDS

          - *(dict) --*

            Contains information about a real-time metric.

            - **Name** *(string) --*

              The name of the metric.

            - **Unit** *(string) --*

              The unit for the metric.

        :type NextToken: string
        :param NextToken:

          The token for the next set of results. Use the value returned in the previous response in the
          next request to retrieve the next set of results.

          The token expires after 5 minutes from the time it is created. Subsequent requests that use the
          token must use the same request parameters as the request that generated the token.

        :type MaxResults: integer
        :param MaxResults:

          The maximimum number of results to return per page.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'MetricResults': [
                    {
                        'Dimensions': {
                            'Queue': {
                                'Id': 'string',
                                'Arn': 'string'
                            },
                            'Channel': 'VOICE'
                        },
                        'Collections': [
                            {
                                'Metric': {
                                    'Name':
                                    'AGENTS_ONLINE'|'AGENTS_AVAILABLE'|'AGENTS_ON_CALL'
                                    |'AGENTS_NON_PRODUCTIVE'|'AGENTS_AFTER_CONTACT_WORK'|'AGENTS_ERROR'
                                    |'AGENTS_STAFFED'|'CONTACTS_IN_QUEUE'|'OLDEST_CONTACT_AGE'
                                    |'CONTACTS_SCHEDULED',
                                    'Unit': 'SECONDS'|'COUNT'|'PERCENT'
                                },
                                'Value': 123.0
                            },
                        ]
                    },
                ],
                'DataSnapshotTime': datetime(2015, 1, 1)
            }
          **Response Structure**

          - *(dict) --*

            - **NextToken** *(string) --*

              If there are additional results, this is the token for the next set of results.

              The token expires after 5 minutes from the time it is created. Subsequent requests that use
              the token must use the same request parameters as the request that generated the token.

            - **MetricResults** *(list) --*

              Information about the real-time metrics.

              - *(dict) --*

                Contains information about a set of real-time metrics.

                - **Dimensions** *(dict) --*

                  The dimensions for the metrics.

                  - **Queue** *(dict) --*

                    Information about the queue for which metrics are returned.

                    - **Id** *(string) --*

                      The identifier of the queue.

                    - **Arn** *(string) --*

                      The Amazon Resource Name (ARN) of the queue.

                  - **Channel** *(string) --*

                    The channel used for grouping and filters.

                - **Collections** *(list) --*

                  The set of metrics.

                  - *(dict) --*

                    Contains the data for a real-time metric.

                    - **Metric** *(dict) --*

                      Information about the metric.

                      - **Name** *(string) --*

                        The name of the metric.

                      - **Unit** *(string) --*

                        The unit for the metric.

                    - **Value** *(float) --*

                      The value of the metric.

            - **DataSnapshotTime** *(datetime) --*

              The time at which the metrics were retrieved and cached for pagination.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_federation_token(
        self, InstanceId: str
    ) -> ClientGetFederationTokenResponseTypeDef:
        """
        Retrieves a token for federation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/GetFederationToken>`_

        **Request Syntax**
        ::

          response = client.get_federation_token(
              InstanceId='string'
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Credentials': {
                    'AccessToken': 'string',
                    'AccessTokenExpiration': datetime(2015, 1, 1),
                    'RefreshToken': 'string',
                    'RefreshTokenExpiration': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Credentials** *(dict) --*

              The credentials to use for federation.

              - **AccessToken** *(string) --*

                An access token generated for a federated user to access Amazon Connect.

              - **AccessTokenExpiration** *(datetime) --*

                A token generated with an expiration time for the session a user is logged in to Amazon
                Connect.

              - **RefreshToken** *(string) --*

                Renews a token generated for a user to access the Amazon Connect instance.

              - **RefreshTokenExpiration** *(datetime) --*

                Renews the expiration timer for a generated token.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_metric_data(
        self,
        InstanceId: str,
        StartTime: datetime,
        EndTime: datetime,
        Filters: ClientGetMetricDataFiltersTypeDef,
        HistoricalMetrics: List[ClientGetMetricDataHistoricalMetricsTypeDef],
        Groupings: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetMetricDataResponseTypeDef:
        """
        Gets historical metric data from the specified Amazon Connect instance.

        For more information, see `Historical Metrics Reports
        <https://docs.aws.amazon.com/connect/latest/adminguide/historical-metrics.html>`__ in the *Amazon
        Connect Administrator Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/GetMetricData>`_

        **Request Syntax**
        ::

          response = client.get_metric_data(
              InstanceId='string',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Filters={
                  'Queues': [
                      'string',
                  ],
                  'Channels': [
                      'VOICE',
                  ]
              },
              Groupings=[
                  'QUEUE'|'CHANNEL',
              ],
              HistoricalMetrics=[
                  {
                      'Name':
                      'CONTACTS_QUEUED'|'CONTACTS_HANDLED'|'CONTACTS_ABANDONED'|'CONTACTS_CONSULTED'
                      |'CONTACTS_AGENT_HUNG_UP_FIRST'|'CONTACTS_HANDLED_INCOMING'
                      |'CONTACTS_HANDLED_OUTBOUND'|'CONTACTS_HOLD_ABANDONS'|'CONTACTS_TRANSFERRED_IN'
                      |'CONTACTS_TRANSFERRED_OUT'|'CONTACTS_TRANSFERRED_IN_FROM_QUEUE'
                      |'CONTACTS_TRANSFERRED_OUT_FROM_QUEUE'|'CONTACTS_MISSED'|'CALLBACK_CONTACTS_HANDLED'
                      |'API_CONTACTS_HANDLED'|'OCCUPANCY'|'HANDLE_TIME'|'AFTER_CONTACT_WORK_TIME'
                      |'QUEUED_TIME'|'ABANDON_TIME'|'QUEUE_ANSWER_TIME'|'HOLD_TIME'|'INTERACTION_TIME'
                      |'INTERACTION_AND_HOLD_TIME'|'SERVICE_LEVEL',
                      'Threshold': {
                          'Comparison': 'LT',
                          'ThresholdValue': 123.0
                      },
                      'Statistic': 'SUM'|'MAX'|'AVG',
                      'Unit': 'SECONDS'|'COUNT'|'PERCENT'
                  },
              ],
              NextToken='string',
              MaxResults=123
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type StartTime: datetime
        :param StartTime: **[REQUIRED]**

          The timestamp, in UNIX Epoch time format, at which to start the reporting interval for the
          retrieval of historical metrics data. The time must be specified using a multiple of 5 minutes,
          such as 10:05, 10:10, 10:15.

          The start time cannot be earlier than 24 hours before the time of the request. Historical metrics
          are available only for 24 hours.

        :type EndTime: datetime
        :param EndTime: **[REQUIRED]**

          The timestamp, in UNIX Epoch time format, at which to end the reporting interval for the
          retrieval of historical metrics data. The time must be specified using an interval of 5 minutes,
          such as 11:00, 11:05, 11:10, and must be later than the start time timestamp.

          The time range between the start and end time must be less than 24 hours.

        :type Filters: dict
        :param Filters: **[REQUIRED]**

          The queues, up to 100, or channels, to use to filter the metrics returned. Metric data is
          retrieved only for the resources associated with the queues or channels included in the filter.
          You can include both queue IDs and queue ARNs in the same request. The only supported channel is
          ``VOICE`` .

          - **Queues** *(list) --*

            The queues to use to filter the metrics. You can specify up to 100 queues per request.

            - *(string) --*

          - **Channels** *(list) --*

            The channel to use to filter the metrics.

            - *(string) --*

        :type Groupings: list
        :param Groupings:

          The grouping applied to the metrics returned. For example, when results are grouped by queue, the
          metrics returned are grouped by queue. The values returned apply to the metrics for each queue
          rather than aggregated for all queues.

          The only supported grouping is ``QUEUE`` .

          If no grouping is specified, a summary of metrics for all queues is returned.

          - *(string) --*

        :type HistoricalMetrics: list
        :param HistoricalMetrics: **[REQUIRED]**

          The metrics to retrieve. Specify the name, unit, and statistic for each metric. The following
          historical metrics are available:

            ABANDON_TIME

          Unit: SECONDS

          Statistic: AVG

            AFTER_CONTACT_WORK_TIME

          Unit: SECONDS

          Statistic: AVG

            API_CONTACTS_HANDLED

          Unit: COUNT

          Statistic: SUM

            CALLBACK_CONTACTS_HANDLED

          Unit: COUNT

          Statistic: SUM

            CONTACTS_ABANDONED

          Unit: COUNT

          Statistic: SUM

            CONTACTS_AGENT_HUNG_UP_FIRST

          Unit: COUNT

          Statistic: SUM

            CONTACTS_CONSULTED

          Unit: COUNT

          Statistic: SUM

            CONTACTS_HANDLED

          Unit: COUNT

          Statistic: SUM

            CONTACTS_HANDLED_INCOMING

          Unit: COUNT

          Statistic: SUM

            CONTACTS_HANDLED_OUTBOUND

          Unit: COUNT

          Statistic: SUM

            CONTACTS_HOLD_ABANDONS

          Unit: COUNT

          Statistic: SUM

            CONTACTS_MISSED

          Unit: COUNT

          Statistic: SUM

            CONTACTS_QUEUED

          Unit: COUNT

          Statistic: SUM

            CONTACTS_TRANSFERRED_IN

          Unit: COUNT

          Statistic: SUM

            CONTACTS_TRANSFERRED_IN_FROM_QUEUE

          Unit: COUNT

          Statistic: SUM

            CONTACTS_TRANSFERRED_OUT

          Unit: COUNT

          Statistic: SUM

            CONTACTS_TRANSFERRED_OUT_FROM_QUEUE

          Unit: COUNT

          Statistic: SUM

            HANDLE_TIME

          Unit: SECONDS

          Statistic: AVG

            HOLD_TIME

          Unit: SECONDS

          Statistic: AVG

            INTERACTION_AND_HOLD_TIME

          Unit: SECONDS

          Statistic: AVG

            INTERACTION_TIME

          Unit: SECONDS

          Statistic: AVG

            OCCUPANCY

          Unit: PERCENT

          Statistic: AVG

            QUEUE_ANSWER_TIME

          Unit: SECONDS

          Statistic: AVG

            QUEUED_TIME

          Unit: SECONDS

          Statistic: MAX

            SERVICE_LEVEL

          Unit: PERCENT

          Statistic: AVG

          Threshold: Only "Less than" comparisons are supported, with the following service level
          thresholds: 15, 20, 25, 30, 45, 60, 90, 120, 180, 240, 300, 600

          - *(dict) --*

            Contains information about a historical metric.

            - **Name** *(string) --*

              The name of the metric.

            - **Threshold** *(dict) --*

              The threshold for the metric, used with service level metrics.

              - **Comparison** *(string) --*

                The type of comparison. Only "less than" (LT) comparisons are supported.

              - **ThresholdValue** *(float) --*

                The threshold value to compare.

            - **Statistic** *(string) --*

              The statistic for the metric.

            - **Unit** *(string) --*

              The unit for the metric.

        :type NextToken: string
        :param NextToken:

          The token for the next set of results. Use the value returned in the previous response in the
          next request to retrieve the next set of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximimum number of results to return per page.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'MetricResults': [
                    {
                        'Dimensions': {
                            'Queue': {
                                'Id': 'string',
                                'Arn': 'string'
                            },
                            'Channel': 'VOICE'
                        },
                        'Collections': [
                            {
                                'Metric': {
                                    'Name':
                                    'CONTACTS_QUEUED'|'CONTACTS_HANDLED'|'CONTACTS_ABANDONED'
                                    |'CONTACTS_CONSULTED'|'CONTACTS_AGENT_HUNG_UP_FIRST'
                                    |'CONTACTS_HANDLED_INCOMING'|'CONTACTS_HANDLED_OUTBOUND'
                                    |'CONTACTS_HOLD_ABANDONS'|'CONTACTS_TRANSFERRED_IN'
                                    |'CONTACTS_TRANSFERRED_OUT'|'CONTACTS_TRANSFERRED_IN_FROM_QUEUE'
                                    |'CONTACTS_TRANSFERRED_OUT_FROM_QUEUE'|'CONTACTS_MISSED'
                                    |'CALLBACK_CONTACTS_HANDLED'|'API_CONTACTS_HANDLED'|'OCCUPANCY'
                                    |'HANDLE_TIME'|'AFTER_CONTACT_WORK_TIME'|'QUEUED_TIME'|'ABANDON_TIME'
                                    |'QUEUE_ANSWER_TIME'|'HOLD_TIME'|'INTERACTION_TIME'
                                    |'INTERACTION_AND_HOLD_TIME'|'SERVICE_LEVEL',
                                    'Threshold': {
                                        'Comparison': 'LT',
                                        'ThresholdValue': 123.0
                                    },
                                    'Statistic': 'SUM'|'MAX'|'AVG',
                                    'Unit': 'SECONDS'|'COUNT'|'PERCENT'
                                },
                                'Value': 123.0
                            },
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextToken** *(string) --*

              If there are additional results, this is the token for the next set of results.

              The token expires after 5 minutes from the time it is created. Subsequent requests that use
              the token must use the same request parameters as the request that generated the token.

            - **MetricResults** *(list) --*

              Information about the historical metrics.

              If no grouping is specified, a summary of metric data is returned.

              - *(dict) --*

                Contains information about the historical metrics retrieved.

                - **Dimensions** *(dict) --*

                  The dimension for the metrics.

                  - **Queue** *(dict) --*

                    Information about the queue for which metrics are returned.

                    - **Id** *(string) --*

                      The identifier of the queue.

                    - **Arn** *(string) --*

                      The Amazon Resource Name (ARN) of the queue.

                  - **Channel** *(string) --*

                    The channel used for grouping and filters.

                - **Collections** *(list) --*

                  The set of metrics.

                  - *(dict) --*

                    Contains the data for a historical metric.

                    - **Metric** *(dict) --*

                      Information about the metric.

                      - **Name** *(string) --*

                        The name of the metric.

                      - **Threshold** *(dict) --*

                        The threshold for the metric, used with service level metrics.

                        - **Comparison** *(string) --*

                          The type of comparison. Only "less than" (LT) comparisons are supported.

                        - **ThresholdValue** *(float) --*

                          The threshold value to compare.

                      - **Statistic** *(string) --*

                        The statistic for the metric.

                      - **Unit** *(string) --*

                        The unit for the metric.

                    - **Value** *(float) --*

                      The value of the metric.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_contact_flows(
        self,
        InstanceId: str,
        ContactFlowTypes: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListContactFlowsResponseTypeDef:
        """
        Provides information about the contact flows for the specified Amazon Connect instance.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListContactFlows>`_

        **Request Syntax**
        ::

          response = client.list_contact_flows(
              InstanceId='string',
              ContactFlowTypes=[
                  'CONTACT_FLOW'|'CUSTOMER_QUEUE'|'CUSTOMER_HOLD'|'CUSTOMER_WHISPER'|'AGENT_HOLD'
                  |'AGENT_WHISPER'|'OUTBOUND_WHISPER'|'AGENT_TRANSFER'|'QUEUE_TRANSFER',
              ],
              NextToken='string',
              MaxResults=123
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type ContactFlowTypes: list
        :param ContactFlowTypes:

          The type of contact flow.

          - *(string) --*

        :type NextToken: string
        :param NextToken:

          The token for the next set of results. Use the value returned in the previous response in the
          next request to retrieve the next set of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximimum number of results to return per page.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ContactFlowSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string',
                        'ContactFlowType':
                        'CONTACT_FLOW'|'CUSTOMER_QUEUE'|'CUSTOMER_HOLD'|'CUSTOMER_WHISPER'|'AGENT_HOLD'
                        |'AGENT_WHISPER'|'OUTBOUND_WHISPER'|'AGENT_TRANSFER'|'QUEUE_TRANSFER'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ContactFlowSummaryList** *(list) --*

              Information about the contact flows.

              - *(dict) --*

                Contains summary information about a contact flow.

                - **Id** *(string) --*

                  The identifier of the contact flow.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the contact flow.

                - **Name** *(string) --*

                  The name of the contact flow.

                - **ContactFlowType** *(string) --*

                  The type of contact flow.

            - **NextToken** *(string) --*

              If there are additional results, this is the token for the next set of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_hours_of_operations(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListHoursOfOperationsResponseTypeDef:
        """
        Provides information about the hours of operation for the specified Amazon Connect instance.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListHoursOfOperations>`_

        **Request Syntax**
        ::

          response = client.list_hours_of_operations(
              InstanceId='string',
              NextToken='string',
              MaxResults=123
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type NextToken: string
        :param NextToken:

          The token for the next set of results. Use the value returned in the previous response in the
          next request to retrieve the next set of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximimum number of results to return per page.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'HoursOfOperationSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **HoursOfOperationSummaryList** *(list) --*

              Information about the hours of operation.

              - *(dict) --*

                Contains summary information about hours of operation for a contact center.

                - **Id** *(string) --*

                  The identifier of the hours of operation.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the hours of operation.

                - **Name** *(string) --*

                  The name of the hours of operation.

            - **NextToken** *(string) --*

              If there are additional results, this is the token for the next set of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_phone_numbers(
        self,
        InstanceId: str,
        PhoneNumberTypes: List[str] = None,
        PhoneNumberCountryCodes: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListPhoneNumbersResponseTypeDef:
        """
        Provides information about the phone numbers for the specified Amazon Connect instance.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListPhoneNumbers>`_

        **Request Syntax**
        ::

          response = client.list_phone_numbers(
              InstanceId='string',
              PhoneNumberTypes=[
                  'TOLL_FREE'|'DID',
              ],
              PhoneNumberCountryCodes=[
                  'AF'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'
                  |'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BA'|'BW'|'BR'|'IO'|'VG'|'BN'|'BG'|'BF'|'BI'
                  |'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CK'|'CR'|'HR'|'CU'
                  |'CW'|'CY'|'CZ'|'CD'|'DK'|'DJ'|'DM'|'DO'|'TL'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'
                  |'FO'|'FJ'|'FI'|'FR'|'PF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GU'|'GT'|'GG'
                  |'GN'|'GW'|'GY'|'HT'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'CI'
                  |'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'
                  |'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'
                  |'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'AN'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'
                  |'KP'|'MP'|'NO'|'OM'|'PK'|'PW'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'CG'
                  |'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'
                  |'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'KR'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'
                  |'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'VI'|'UG'
                  |'UA'|'AE'|'GB'|'US'|'UY'|'UZ'|'VU'|'VA'|'VE'|'VN'|'WF'|'EH'|'YE'|'ZM'|'ZW',
              ],
              NextToken='string',
              MaxResults=123
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type PhoneNumberTypes: list
        :param PhoneNumberTypes:

          The type of phone number.

          - *(string) --*

        :type PhoneNumberCountryCodes: list
        :param PhoneNumberCountryCodes:

          The ISO country code.

          - *(string) --*

        :type NextToken: string
        :param NextToken:

          The token for the next set of results. Use the value returned in the previous response in the
          next request to retrieve the next set of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximimum number of results to return per page.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PhoneNumberSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'PhoneNumber': 'string',
                        'PhoneNumberType': 'TOLL_FREE'|'DID',
                        'PhoneNumberCountryCode':
                        'AF'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'
                        |'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BA'|'BW'|'BR'|'IO'|'VG'|'BN'
                        |'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'
                        |'CK'|'CR'|'HR'|'CU'|'CW'|'CY'|'CZ'|'CD'|'DK'|'DJ'|'DM'|'DO'|'TL'|'EC'|'EG'|'SV'
                        |'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'PF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'
                        |'GR'|'GL'|'GD'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'
                        |'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'CI'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KW'|'KG'
                        |'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'
                        |'MT'|'MH'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'
                        |'NR'|'NP'|'NL'|'AN'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'KP'|'MP'|'NO'|'OM'|'PK'|'PW'
                        |'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'CG'|'RE'|'RO'|'RU'|'RW'|'BL'
                        |'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'
                        |'SK'|'SI'|'SB'|'SO'|'ZA'|'KR'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'
                        |'TJ'|'TZ'|'TH'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'VI'|'UG'|'UA'|'AE'
                        |'GB'|'US'|'UY'|'UZ'|'VU'|'VA'|'VE'|'VN'|'WF'|'EH'|'YE'|'ZM'|'ZW'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **PhoneNumberSummaryList** *(list) --*

              Information about the phone numbers.

              - *(dict) --*

                Contains summary information about a phone number for a contact center.

                - **Id** *(string) --*

                  The identifier of the phone number.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the phone number.

                - **PhoneNumber** *(string) --*

                  The phone number.

                - **PhoneNumberType** *(string) --*

                  The type of phone number.

                - **PhoneNumberCountryCode** *(string) --*

                  The ISO country code.

            - **NextToken** *(string) --*

              If there are additional results, this is the token for the next set of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_queues(
        self,
        InstanceId: str,
        QueueTypes: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListQueuesResponseTypeDef:
        """
        Provides information about the queues for the specified Amazon Connect instance.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListQueues>`_

        **Request Syntax**
        ::

          response = client.list_queues(
              InstanceId='string',
              QueueTypes=[
                  'STANDARD'|'AGENT',
              ],
              NextToken='string',
              MaxResults=123
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type QueueTypes: list
        :param QueueTypes:

          The type of queue.

          - *(string) --*

        :type NextToken: string
        :param NextToken:

          The token for the next set of results. Use the value returned in the previous response in the
          next request to retrieve the next set of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximimum number of results to return per page.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'QueueSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string',
                        'QueueType': 'STANDARD'|'AGENT'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **QueueSummaryList** *(list) --*

              Information about the queues.

              - *(dict) --*

                Contains summary information about a queue.

                - **Id** *(string) --*

                  The identifier of the queue.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the queue.

                - **Name** *(string) --*

                  The name of the queue.

                - **QueueType** *(string) --*

                  The type of queue.

            - **NextToken** *(string) --*

              If there are additional results, this is the token for the next set of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_routing_profiles(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListRoutingProfilesResponseTypeDef:
        """
        Provides summary information about the routing profiles for the specified Amazon Connect instance.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListRoutingProfiles>`_

        **Request Syntax**
        ::

          response = client.list_routing_profiles(
              InstanceId='string',
              NextToken='string',
              MaxResults=123
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type NextToken: string
        :param NextToken:

          The token for the next set of results. Use the value returned in the previous response in the
          next request to retrieve the next set of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximimum number of results to return per page.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RoutingProfileSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **RoutingProfileSummaryList** *(list) --*

              Information about the routing profiles.

              - *(dict) --*

                Contains summary information about a routing profile.

                - **Id** *(string) --*

                  The identifier of the routing profile.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the routing profile.

                - **Name** *(string) --*

                  The name of the routing profile.

            - **NextToken** *(string) --*

              If there are additional results, this is the token for the next set of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_security_profiles(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListSecurityProfilesResponseTypeDef:
        """
        Provides summary information about the security profiles for the specified Amazon Connect instance.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListSecurityProfiles>`_

        **Request Syntax**
        ::

          response = client.list_security_profiles(
              InstanceId='string',
              NextToken='string',
              MaxResults=123
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type NextToken: string
        :param NextToken:

          The token for the next set of results. Use the value returned in the previous response in the
          next request to retrieve the next set of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximimum number of results to return per page.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SecurityProfileSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **SecurityProfileSummaryList** *(list) --*

              Information about the security profiles.

              - *(dict) --*

                Contains information about a security profile.

                - **Id** *(string) --*

                  The identifier of the security profile.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the security profile.

                - **Name** *(string) --*

                  The name of the security profile.

            - **NextToken** *(string) --*

              If there are additional results, this is the token for the next set of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, resourceArn: str
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              resourceArn='string'
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **tags** *(dict) --*

              Information about the tags.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_user_hierarchy_groups(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListUserHierarchyGroupsResponseTypeDef:
        """
        Provides summary information about the hierarchy groups for the specified Amazon Connect instance.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListUserHierarchyGroups>`_

        **Request Syntax**
        ::

          response = client.list_user_hierarchy_groups(
              InstanceId='string',
              NextToken='string',
              MaxResults=123
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type NextToken: string
        :param NextToken:

          The token for the next set of results. Use the value returned in the previous response in the
          next request to retrieve the next set of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximimum number of results to return per page.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UserHierarchyGroupSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **UserHierarchyGroupSummaryList** *(list) --*

              Information about the hierarchy groups.

              - *(dict) --*

                Contains summary information about a hierarchy group.

                - **Id** *(string) --*

                  The identifier of the hierarchy group.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the hierarchy group.

                - **Name** *(string) --*

                  The name of the hierarchy group.

            - **NextToken** *(string) --*

              If there are additional results, this is the token for the next set of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_users(
        self, InstanceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListUsersResponseTypeDef:
        """
        Provides summary information about the users for the specified Amazon Connect instance.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/ListUsers>`_

        **Request Syntax**
        ::

          response = client.list_users(
              InstanceId='string',
              NextToken='string',
              MaxResults=123
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type NextToken: string
        :param NextToken:

          The token for the next set of results. Use the value returned in the previous response in the
          next request to retrieve the next set of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximimum number of results to return per page.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UserSummaryList': [
                    {
                        'Id': 'string',
                        'Arn': 'string',
                        'Username': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **UserSummaryList** *(list) --*

              Information about the users.

              - *(dict) --*

                Contains summary information about a user.

                - **Id** *(string) --*

                  The identifier of the user account.

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the user account.

                - **Username** *(string) --*

                  The Amazon Connect user name of the user account.

            - **NextToken** *(string) --*

              If there are additional results, this is the token for the next set of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_outbound_voice_contact(
        self,
        DestinationPhoneNumber: str,
        ContactFlowId: str,
        InstanceId: str,
        ClientToken: str = None,
        SourcePhoneNumber: str = None,
        QueueId: str = None,
        Attributes: Dict[str, str] = None,
    ) -> ClientStartOutboundVoiceContactResponseTypeDef:
        """
        Initiates a contact flow to place an outbound call to a customer.

        There is a 60 second dialing timeout for this operation. If the call is not connected after 60
        seconds, it fails.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/StartOutboundVoiceContact>`_

        **Request Syntax**
        ::

          response = client.start_outbound_voice_contact(
              DestinationPhoneNumber='string',
              ContactFlowId='string',
              InstanceId='string',
              ClientToken='string',
              SourcePhoneNumber='string',
              QueueId='string',
              Attributes={
                  'string': 'string'
              }
          )
        :type DestinationPhoneNumber: string
        :param DestinationPhoneNumber: **[REQUIRED]**

          The phone number of the customer, in E.164 format.

        :type ContactFlowId: string
        :param ContactFlowId: **[REQUIRED]**

          The identifier of the contact flow for the outbound call.

        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type ClientToken: string
        :param ClientToken:

          A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
          The token is valid for 7 days after creation. If a contact is already started, the contact ID is
          returned. If the contact is disconnected, a new contact is started.

          This field is autopopulated if not provided.

        :type SourcePhoneNumber: string
        :param SourcePhoneNumber:

          The phone number associated with the Amazon Connect instance, in E.164 format. If you do not
          specify a source phone number, you must specify a queue.

        :type QueueId: string
        :param QueueId:

          The queue for the call. If you specify a queue, the phone displayed for caller ID is the phone
          number specified in the queue. If you do not specify a queue, the queue defined in the contact
          flow is used. If you do not specify a queue, you must specify a source phone number.

        :type Attributes: dict
        :param Attributes:

          A custom key-value pair using an attribute map. The attributes are standard Amazon Connect
          attributes, and can be accessed in contact flows just like any other contact attributes.

          There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can
          include only alphanumeric, dash, and underscore characters.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ContactId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ContactId** *(string) --*

              The identifier of this contact within the Amazon Connect instance.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_contact(self, ContactId: str, InstanceId: str) -> Dict[str, Any]:
        """
        Ends the specified contact.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/StopContact>`_

        **Request Syntax**
        ::

          response = client.stop_contact(
              ContactId='string',
              InstanceId='string'
          )
        :type ContactId: string
        :param ContactId: **[REQUIRED]**

          The ID of the contact.

        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> None:
        """
        Adds the specified tags to the specified resource.

        The supported resource type is users.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              resourceArn='string',
              tags={
                  'string': 'string'
              }
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource.

        :type tags: dict
        :param tags: **[REQUIRED]**

          One or more tags. For example, { "tags": {"key1":"value1", "key2":"value2"} }.

          - *(string) --*

            - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> None:
        """
        Removes the specified tags from the specified resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              resourceArn='string',
              tagKeys=[
                  'string',
              ]
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource.

        :type tagKeys: list
        :param tagKeys: **[REQUIRED]**

          The tag keys.

          - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_contact_attributes(
        self, InitialContactId: str, InstanceId: str, Attributes: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        Creates or updates the contact attributes associated with the specified contact.

        You can add or update attributes for both ongoing and completed contacts. For example, you can
        update the customer's name or the reason the customer called while the call is active, or add notes
        about steps that the agent took during the call that are displayed to the next agent that takes the
        call. You can also update attributes for a contact using data from your CRM application and save
        the data with the contact in Amazon Connect. You could also flag calls for additional analysis,
        such as legal review or identifying abusive callers.

        Contact attributes are available in Amazon Connect for 24 months, and are then deleted.

         **Important:** You cannot use the operation to update attributes for contacts that occurred prior
         to the release of the API, September 12, 2018. You can update attributes only for contacts that
         started after the release of the API. If you attempt to update attributes for a contact that
         occurred prior to the release of the API, a 400 error is returned. This applies also to queued
         callbacks that were initiated prior to the release of the API but are still active in your
         instance.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/UpdateContactAttributes>`_

        **Request Syntax**
        ::

          response = client.update_contact_attributes(
              InitialContactId='string',
              InstanceId='string',
              Attributes={
                  'string': 'string'
              }
          )
        :type InitialContactId: string
        :param InitialContactId: **[REQUIRED]**

          The identifier of the contact. This is the identifier of the contact associated with the first
          interaction with the contact center.

        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :type Attributes: dict
        :param Attributes: **[REQUIRED]**

          The Amazon Connect attributes. These attributes can be accessed in contact flows just like any
          other contact attributes.

          You can have up to 32,768 UTF-8 bytes across all attributes for a contact. Attribute keys can
          include only alphanumeric, dash, and underscore characters.

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user_hierarchy(
        self, UserId: str, InstanceId: str, HierarchyGroupId: str = None
    ) -> None:
        """
        Assigns the specified hierarchy group to the specified user.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/UpdateUserHierarchy>`_

        **Request Syntax**
        ::

          response = client.update_user_hierarchy(
              HierarchyGroupId='string',
              UserId='string',
              InstanceId='string'
          )
        :type HierarchyGroupId: string
        :param HierarchyGroupId:

          The identifier of the hierarchy group.

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The identifier of the user account.

        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user_identity_info(
        self,
        IdentityInfo: ClientUpdateUserIdentityInfoIdentityInfoTypeDef,
        UserId: str,
        InstanceId: str,
    ) -> None:
        """
        Updates the identity information for the specified user.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/UpdateUserIdentityInfo>`_

        **Request Syntax**
        ::

          response = client.update_user_identity_info(
              IdentityInfo={
                  'FirstName': 'string',
                  'LastName': 'string',
                  'Email': 'string'
              },
              UserId='string',
              InstanceId='string'
          )
        :type IdentityInfo: dict
        :param IdentityInfo: **[REQUIRED]**

          The identity information for the user.

          - **FirstName** *(string) --*

            The first name. This is required if you are using Amazon Connect or SAML for identity
            management.

          - **LastName** *(string) --*

            The last name. This is required if you are using Amazon Connect or SAML for identity management.

          - **Email** *(string) --*

            The email address. If you are using SAML for identity management and include this parameter, an
            error is returned.

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The identifier of the user account.

        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user_phone_config(
        self,
        PhoneConfig: ClientUpdateUserPhoneConfigPhoneConfigTypeDef,
        UserId: str,
        InstanceId: str,
    ) -> None:
        """
        Updates the phone configuration settings for the specified user.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/UpdateUserPhoneConfig>`_

        **Request Syntax**
        ::

          response = client.update_user_phone_config(
              PhoneConfig={
                  'PhoneType': 'SOFT_PHONE'|'DESK_PHONE',
                  'AutoAccept': True|False,
                  'AfterContactWorkTimeLimit': 123,
                  'DeskPhoneNumber': 'string'
              },
              UserId='string',
              InstanceId='string'
          )
        :type PhoneConfig: dict
        :param PhoneConfig: **[REQUIRED]**

          Information about phone configuration settings for the user.

          - **PhoneType** *(string) --* **[REQUIRED]**

            The phone type.

          - **AutoAccept** *(boolean) --*

            The Auto accept setting.

          - **AfterContactWorkTimeLimit** *(integer) --*

            The After Call Work (ACW) timeout setting, in seconds.

          - **DeskPhoneNumber** *(string) --*

            The phone number for the user's desk phone.

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The identifier of the user account.

        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user_routing_profile(
        self, RoutingProfileId: str, UserId: str, InstanceId: str
    ) -> None:
        """
        Assigns the specified routing profile to the specified user.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/UpdateUserRoutingProfile>`_

        **Request Syntax**
        ::

          response = client.update_user_routing_profile(
              RoutingProfileId='string',
              UserId='string',
              InstanceId='string'
          )
        :type RoutingProfileId: string
        :param RoutingProfileId: **[REQUIRED]**

          The identifier of the routing profile for the user.

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The identifier of the user account.

        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_user_security_profiles(
        self, SecurityProfileIds: List[str], UserId: str, InstanceId: str
    ) -> None:
        """
        Assigns the specified security profiles to the specified user.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/UpdateUserSecurityProfiles>`_

        **Request Syntax**
        ::

          response = client.update_user_security_profiles(
              SecurityProfileIds=[
                  'string',
              ],
              UserId='string',
              InstanceId='string'
          )
        :type SecurityProfileIds: list
        :param SecurityProfileIds: **[REQUIRED]**

          The identifiers of the security profiles for the user.

          - *(string) --*

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The identifier of the user account.

        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**

          The identifier of the Amazon Connect instance.

        :returns: None
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_metric_data"]
    ) -> paginator_scope.GetMetricDataPaginator:
        """
        Get Paginator for `get_metric_data` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_contact_flows"]
    ) -> paginator_scope.ListContactFlowsPaginator:
        """
        Get Paginator for `list_contact_flows` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_hours_of_operations"]
    ) -> paginator_scope.ListHoursOfOperationsPaginator:
        """
        Get Paginator for `list_hours_of_operations` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_phone_numbers"]
    ) -> paginator_scope.ListPhoneNumbersPaginator:
        """
        Get Paginator for `list_phone_numbers` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_queues"]
    ) -> paginator_scope.ListQueuesPaginator:
        """
        Get Paginator for `list_queues` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_routing_profiles"]
    ) -> paginator_scope.ListRoutingProfilesPaginator:
        """
        Get Paginator for `list_routing_profiles` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_security_profiles"]
    ) -> paginator_scope.ListSecurityProfilesPaginator:
        """
        Get Paginator for `list_security_profiles` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_user_hierarchy_groups"]
    ) -> paginator_scope.ListUserHierarchyGroupsPaginator:
        """
        Get Paginator for `list_user_hierarchy_groups` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_users"]
    ) -> paginator_scope.ListUsersPaginator:
        """
        Get Paginator for `list_users` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        """
        Create a paginator for an operation.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.

        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """


class Exceptions:
    ClientError: Boto3ClientError
    ContactNotFoundException: Boto3ClientError
    DestinationNotAllowedException: Boto3ClientError
    DuplicateResourceException: Boto3ClientError
    InternalServiceException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    OutboundContactNotPermittedException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    UserNotFoundException: Boto3ClientError

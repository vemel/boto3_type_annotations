"Main interface for appmesh Client"
from __future__ import annotations

from typing import Any, Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_appmesh.client as client_scope

# pylint: disable=import-self
import mypy_boto3_appmesh.paginator as paginator_scope
from mypy_boto3_appmesh.type_defs import (
    ClientCreateMeshResponseTypeDef,
    ClientCreateMeshspecTypeDef,
    ClientCreateMeshtagsTypeDef,
    ClientCreateRouteResponseTypeDef,
    ClientCreateRoutespecTypeDef,
    ClientCreateRoutetagsTypeDef,
    ClientCreateVirtualNodeResponseTypeDef,
    ClientCreateVirtualNodespecTypeDef,
    ClientCreateVirtualNodetagsTypeDef,
    ClientCreateVirtualRouterResponseTypeDef,
    ClientCreateVirtualRouterspecTypeDef,
    ClientCreateVirtualRoutertagsTypeDef,
    ClientCreateVirtualServiceResponseTypeDef,
    ClientCreateVirtualServicespecTypeDef,
    ClientCreateVirtualServicetagsTypeDef,
    ClientDeleteMeshResponseTypeDef,
    ClientDeleteRouteResponseTypeDef,
    ClientDeleteVirtualNodeResponseTypeDef,
    ClientDeleteVirtualRouterResponseTypeDef,
    ClientDeleteVirtualServiceResponseTypeDef,
    ClientDescribeMeshResponseTypeDef,
    ClientDescribeRouteResponseTypeDef,
    ClientDescribeVirtualNodeResponseTypeDef,
    ClientDescribeVirtualRouterResponseTypeDef,
    ClientDescribeVirtualServiceResponseTypeDef,
    ClientListMeshesResponseTypeDef,
    ClientListRoutesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListVirtualNodesResponseTypeDef,
    ClientListVirtualRoutersResponseTypeDef,
    ClientListVirtualServicesResponseTypeDef,
    ClientTagResourcetagsTypeDef,
    ClientUpdateMeshResponseTypeDef,
    ClientUpdateMeshspecTypeDef,
    ClientUpdateRouteResponseTypeDef,
    ClientUpdateRoutespecTypeDef,
    ClientUpdateVirtualNodeResponseTypeDef,
    ClientUpdateVirtualNodespecTypeDef,
    ClientUpdateVirtualRouterResponseTypeDef,
    ClientUpdateVirtualRouterspecTypeDef,
    ClientUpdateVirtualServiceResponseTypeDef,
    ClientUpdateVirtualServicespecTypeDef,
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
    def create_mesh(
        self,
        meshName: str,
        clientToken: str = None,
        spec: ClientCreateMeshspecTypeDef = None,
        tags: List[ClientCreateMeshtagsTypeDef] = None,
    ) -> ClientCreateMeshResponseTypeDef:
        """
        Creates a service mesh. A service mesh is a logical boundary for network traffic between the
        services that reside within it.

        After you create your service mesh, you can create virtual services, virtual nodes, virtual
        routers, and routes to distribute traffic between the applications in your mesh.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/CreateMesh>`_

        **Request Syntax**
        ::

          response = client.create_mesh(
              clientToken='string',
              meshName='string',
              spec={
                  'egressFilter': {
                      'type': 'ALLOW_ALL'|'DROP_ALL'
                  }
              },
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ]
          )
        :type clientToken: string
        :param clientToken:

          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up
          to 36 letters, numbers, hyphens, and underscores are allowed.

          This field is autopopulated if not provided.

        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name to use for the service mesh.

        :type spec: dict
        :param spec:

          The service mesh specification to apply.

          - **egressFilter** *(dict) --*

            The egress filter rules for the service mesh.

            - **type** *(string) --* **[REQUIRED]**

              The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only from
              virtual nodes to other defined resources in the service mesh (and any traffic to
              ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to ``ALLOW_ALL``
              to allow egress to any endpoint inside or outside of the service mesh.

        :type tags: list
        :param tags:

          Optional metadata that you can apply to the service mesh to assist with categorization and
          organization. Each tag consists of a key and an optional value, both of which you define. Tag
          keys can have a maximum character length of 128 characters, and tag values can have a maximum
          length of 256 characters.

          - *(dict) --*

            Optional metadata that you apply to a resource to assist with categorization and organization.
            Each tag consists of a key and an optional value, both of which you define. Tag keys can have a
            maximum character length of 128 characters, and tag values can have a maximum length of 256
            characters.

            - **key** *(string) --* **[REQUIRED]**

              One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
              a category for more specific tag values.

            - **value** *(string) --*

              The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor
              within a tag category (key).

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'mesh': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'egressFilter': {
                            'type': 'ALLOW_ALL'|'DROP_ALL'
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **mesh** *(dict) --*

              The full description of your service mesh following the create call.

              - **meshName** *(string) --*

                The name of the service mesh.

              - **metadata** *(dict) --*

                The associated metadata for the service mesh.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **spec** *(dict) --*

                The associated specification for the service mesh.

                - **egressFilter** *(dict) --*

                  The egress filter rules for the service mesh.

                  - **type** *(string) --*

                    The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
                    from virtual nodes to other defined resources in the service mesh (and any traffic to
                    ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
                    ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.

              - **status** *(dict) --*

                The status of the service mesh.

                - **status** *(string) --*

                  The current mesh status.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_route(
        self,
        meshName: str,
        routeName: str,
        spec: ClientCreateRoutespecTypeDef,
        virtualRouterName: str,
        clientToken: str = None,
        tags: List[ClientCreateRoutetagsTypeDef] = None,
    ) -> ClientCreateRouteResponseTypeDef:
        """
        Creates a route that is associated with a virtual router.

        You can use the ``prefix`` parameter in your route specification for path-based routing of
        requests. For example, if your virtual service name is ``my-service.local`` and you want the route
        to match requests to ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

        If your route matches a request, you can distribute traffic to one or more target virtual nodes
        with relative weighting.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/CreateRoute>`_

        **Request Syntax**
        ::

          response = client.create_route(
              clientToken='string',
              meshName='string',
              routeName='string',
              spec={
                  'grpcRoute': {
                      'action': {
                          'weightedTargets': [
                              {
                                  'virtualNode': 'string',
                                  'weight': 123
                              },
                          ]
                      },
                      'match': {
                          'metadata': [
                              {
                                  'invert': True|False,
                                  'match': {
                                      'exact': 'string',
                                      'prefix': 'string',
                                      'range': {
                                          'end': 123,
                                          'start': 123
                                      },
                                      'regex': 'string',
                                      'suffix': 'string'
                                  },
                                  'name': 'string'
                              },
                          ],
                          'methodName': 'string',
                          'serviceName': 'string'
                      },
                      'retryPolicy': {
                          'grpcRetryEvents': [
                              'cancelled'|'deadline-exceeded'|'internal'|'resource-exhausted'|'unavailable',
                          ],
                          'httpRetryEvents': [
                              'string',
                          ],
                          'maxRetries': 123,
                          'perRetryTimeout': {
                              'unit': 'ms'|'s',
                              'value': 123
                          },
                          'tcpRetryEvents': [
                              'connection-error',
                          ]
                      }
                  },
                  'http2Route': {
                      'action': {
                          'weightedTargets': [
                              {
                                  'virtualNode': 'string',
                                  'weight': 123
                              },
                          ]
                      },
                      'match': {
                          'headers': [
                              {
                                  'invert': True|False,
                                  'match': {
                                      'exact': 'string',
                                      'prefix': 'string',
                                      'range': {
                                          'end': 123,
                                          'start': 123
                                      },
                                      'regex': 'string',
                                      'suffix': 'string'
                                  },
                                  'name': 'string'
                              },
                          ],
                          'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                          'prefix': 'string',
                          'scheme': 'http'|'https'
                      },
                      'retryPolicy': {
                          'httpRetryEvents': [
                              'string',
                          ],
                          'maxRetries': 123,
                          'perRetryTimeout': {
                              'unit': 'ms'|'s',
                              'value': 123
                          },
                          'tcpRetryEvents': [
                              'connection-error',
                          ]
                      }
                  },
                  'httpRoute': {
                      'action': {
                          'weightedTargets': [
                              {
                                  'virtualNode': 'string',
                                  'weight': 123
                              },
                          ]
                      },
                      'match': {
                          'headers': [
                              {
                                  'invert': True|False,
                                  'match': {
                                      'exact': 'string',
                                      'prefix': 'string',
                                      'range': {
                                          'end': 123,
                                          'start': 123
                                      },
                                      'regex': 'string',
                                      'suffix': 'string'
                                  },
                                  'name': 'string'
                              },
                          ],
                          'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                          'prefix': 'string',
                          'scheme': 'http'|'https'
                      },
                      'retryPolicy': {
                          'httpRetryEvents': [
                              'string',
                          ],
                          'maxRetries': 123,
                          'perRetryTimeout': {
                              'unit': 'ms'|'s',
                              'value': 123
                          },
                          'tcpRetryEvents': [
                              'connection-error',
                          ]
                      }
                  },
                  'priority': 123,
                  'tcpRoute': {
                      'action': {
                          'weightedTargets': [
                              {
                                  'virtualNode': 'string',
                                  'weight': 123
                              },
                          ]
                      }
                  }
              },
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ],
              virtualRouterName='string'
          )
        :type clientToken: string
        :param clientToken:

          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up
          to 36 letters, numbers, hyphens, and underscores are allowed.

          This field is autopopulated if not provided.

        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh to create the route in.

        :type routeName: string
        :param routeName: **[REQUIRED]**

          The name to use for the route.

        :type spec: dict
        :param spec: **[REQUIRED]**

          The route specification to apply.

          - **grpcRoute** *(dict) --*

            An object that represents the specification of a GRPC route.

            - **action** *(dict) --* **[REQUIRED]**

              An object that represents the action to take if a match is determined.

              - **weightedTargets** *(list) --* **[REQUIRED]**

                An object that represents the targets that traffic is routed to when a request matches the
                route.

                - *(dict) --*

                  An object that represents a target and its relative weight. Traffic is distributed across
                  targets according to their relative weight. For example, a weighted target with a
                  relative weight of 50 receives five times as much traffic as one with a relative weight
                  of 10. The total weight for all targets combined must be less than or equal to 100.

                  - **virtualNode** *(string) --* **[REQUIRED]**

                    The virtual node to associate with the weighted target.

                  - **weight** *(integer) --* **[REQUIRED]**

                    The relative weight of the weighted target.

            - **match** *(dict) --* **[REQUIRED]**

              An object that represents the criteria for determining a request match.

              - **metadata** *(list) --*

                An object that represents the data to match from the request.

                - *(dict) --*

                  An object that represents the match metadata for the route.

                  - **invert** *(boolean) --*

                    Specify ``True`` to match anything except the match criteria. The default value is
                    ``False`` .

                  - **match** *(dict) --*

                    An object that represents the data to match from the request.

                    - **exact** *(string) --*

                      The value sent by the client must match the specified value exactly.

                    - **prefix** *(string) --*

                      The value sent by the client must begin with the specified characters.

                    - **range** *(dict) --*

                      An object that represents the range of values to match on.

                      - **end** *(integer) --* **[REQUIRED]**

                        The end of the range.

                      - **start** *(integer) --* **[REQUIRED]**

                        The start of the range.

                    - **regex** *(string) --*

                      The value sent by the client must include the specified characters.

                    - **suffix** *(string) --*

                      The value sent by the client must end with the specified characters.

                  - **name** *(string) --* **[REQUIRED]**

                    The name of the route.

              - **methodName** *(string) --*

                The method name to match from the request. If you specify a name, you must also specify a
                ``serviceName`` .

              - **serviceName** *(string) --*

                The fully qualified domain name for the service to match from the request.

            - **retryPolicy** *(dict) --*

              An object that represents a retry policy.

              - **grpcRetryEvents** *(list) --*

                Specify at least one of the valid values.

                - *(string) --*

              - **httpRetryEvents** *(list) --*

                Specify at least one of the following values.

                * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
                and 511

                * **gateway-error** – HTTP status codes 502, 503, and 504

                * **client-error** – HTTP status code 409

                * **stream-error** – Retry on refused stream

                - *(string) --*

              - **maxRetries** *(integer) --* **[REQUIRED]**

                The maximum number of retry attempts.

              - **perRetryTimeout** *(dict) --* **[REQUIRED]**

                An object that represents a duration of time.

                - **unit** *(string) --*

                  A unit of time.

                - **value** *(integer) --*

                  A number of time units.

              - **tcpRetryEvents** *(list) --*

                Specify a valid value.

                - *(string) --*

          - **http2Route** *(dict) --*

            An object that represents the specification of an HTTP2 route.

            - **action** *(dict) --* **[REQUIRED]**

              An object that represents the action to take if a match is determined.

              - **weightedTargets** *(list) --* **[REQUIRED]**

                An object that represents the targets that traffic is routed to when a request matches the
                route.

                - *(dict) --*

                  An object that represents a target and its relative weight. Traffic is distributed across
                  targets according to their relative weight. For example, a weighted target with a
                  relative weight of 50 receives five times as much traffic as one with a relative weight
                  of 10. The total weight for all targets combined must be less than or equal to 100.

                  - **virtualNode** *(string) --* **[REQUIRED]**

                    The virtual node to associate with the weighted target.

                  - **weight** *(integer) --* **[REQUIRED]**

                    The relative weight of the weighted target.

            - **match** *(dict) --* **[REQUIRED]**

              An object that represents the criteria for determining a request match.

              - **headers** *(list) --*

                An object that represents the client request headers to match on.

                - *(dict) --*

                  An object that represents the HTTP header in the request.

                  - **invert** *(boolean) --*

                    Specify ``True`` to match anything except the match criteria. The default value is
                    ``False`` .

                  - **match** *(dict) --*

                    The ``HeaderMatchMethod`` object.

                    - **exact** *(string) --*

                      The value sent by the client must match the specified value exactly.

                    - **prefix** *(string) --*

                      The value sent by the client must begin with the specified characters.

                    - **range** *(dict) --*

                      An object that represents the range of values to match on.

                      - **end** *(integer) --* **[REQUIRED]**

                        The end of the range.

                      - **start** *(integer) --* **[REQUIRED]**

                        The start of the range.

                    - **regex** *(string) --*

                      The value sent by the client must include the specified characters.

                    - **suffix** *(string) --*

                      The value sent by the client must end with the specified characters.

                  - **name** *(string) --* **[REQUIRED]**

                    A name for the HTTP header in the client request that will be matched on.

              - **method** *(string) --*

                The client request method to match on. Specify only one.

              - **prefix** *(string) --* **[REQUIRED]**

                Specifies the path to match requests with. This parameter must always start with ``/`` ,
                which by itself matches all requests to the virtual service name. You can also match for
                path-based routing of requests. For example, if your virtual service name is
                ``my-service.local`` and you want the route to match requests to
                ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

              - **scheme** *(string) --*

                The client request scheme to match on. Specify only one.

            - **retryPolicy** *(dict) --*

              An object that represents a retry policy.

              - **httpRetryEvents** *(list) --*

                Specify at least one of the following values.

                * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
                and 511

                * **gateway-error** – HTTP status codes 502, 503, and 504

                * **client-error** – HTTP status code 409

                * **stream-error** – Retry on refused stream

                - *(string) --*

              - **maxRetries** *(integer) --* **[REQUIRED]**

                The maximum number of retry attempts.

              - **perRetryTimeout** *(dict) --* **[REQUIRED]**

                An object that represents a duration of time.

                - **unit** *(string) --*

                  A unit of time.

                - **value** *(integer) --*

                  A number of time units.

              - **tcpRetryEvents** *(list) --*

                Specify a valid value.

                - *(string) --*

          - **httpRoute** *(dict) --*

            An object that represents the specification of an HTTP route.

            - **action** *(dict) --* **[REQUIRED]**

              An object that represents the action to take if a match is determined.

              - **weightedTargets** *(list) --* **[REQUIRED]**

                An object that represents the targets that traffic is routed to when a request matches the
                route.

                - *(dict) --*

                  An object that represents a target and its relative weight. Traffic is distributed across
                  targets according to their relative weight. For example, a weighted target with a
                  relative weight of 50 receives five times as much traffic as one with a relative weight
                  of 10. The total weight for all targets combined must be less than or equal to 100.

                  - **virtualNode** *(string) --* **[REQUIRED]**

                    The virtual node to associate with the weighted target.

                  - **weight** *(integer) --* **[REQUIRED]**

                    The relative weight of the weighted target.

            - **match** *(dict) --* **[REQUIRED]**

              An object that represents the criteria for determining a request match.

              - **headers** *(list) --*

                An object that represents the client request headers to match on.

                - *(dict) --*

                  An object that represents the HTTP header in the request.

                  - **invert** *(boolean) --*

                    Specify ``True`` to match anything except the match criteria. The default value is
                    ``False`` .

                  - **match** *(dict) --*

                    The ``HeaderMatchMethod`` object.

                    - **exact** *(string) --*

                      The value sent by the client must match the specified value exactly.

                    - **prefix** *(string) --*

                      The value sent by the client must begin with the specified characters.

                    - **range** *(dict) --*

                      An object that represents the range of values to match on.

                      - **end** *(integer) --* **[REQUIRED]**

                        The end of the range.

                      - **start** *(integer) --* **[REQUIRED]**

                        The start of the range.

                    - **regex** *(string) --*

                      The value sent by the client must include the specified characters.

                    - **suffix** *(string) --*

                      The value sent by the client must end with the specified characters.

                  - **name** *(string) --* **[REQUIRED]**

                    A name for the HTTP header in the client request that will be matched on.

              - **method** *(string) --*

                The client request method to match on. Specify only one.

              - **prefix** *(string) --* **[REQUIRED]**

                Specifies the path to match requests with. This parameter must always start with ``/`` ,
                which by itself matches all requests to the virtual service name. You can also match for
                path-based routing of requests. For example, if your virtual service name is
                ``my-service.local`` and you want the route to match requests to
                ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

              - **scheme** *(string) --*

                The client request scheme to match on. Specify only one.

            - **retryPolicy** *(dict) --*

              An object that represents a retry policy.

              - **httpRetryEvents** *(list) --*

                Specify at least one of the following values.

                * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
                and 511

                * **gateway-error** – HTTP status codes 502, 503, and 504

                * **client-error** – HTTP status code 409

                * **stream-error** – Retry on refused stream

                - *(string) --*

              - **maxRetries** *(integer) --* **[REQUIRED]**

                The maximum number of retry attempts.

              - **perRetryTimeout** *(dict) --* **[REQUIRED]**

                An object that represents a duration of time.

                - **unit** *(string) --*

                  A unit of time.

                - **value** *(integer) --*

                  A number of time units.

              - **tcpRetryEvents** *(list) --*

                Specify a valid value.

                - *(string) --*

          - **priority** *(integer) --*

            The priority for the route. Routes are matched based on the specified value, where 0 is the
            highest priority.

          - **tcpRoute** *(dict) --*

            An object that represents the specification of a TCP route.

            - **action** *(dict) --* **[REQUIRED]**

              The action to take if a match is determined.

              - **weightedTargets** *(list) --* **[REQUIRED]**

                An object that represents the targets that traffic is routed to when a request matches the
                route.

                - *(dict) --*

                  An object that represents a target and its relative weight. Traffic is distributed across
                  targets according to their relative weight. For example, a weighted target with a
                  relative weight of 50 receives five times as much traffic as one with a relative weight
                  of 10. The total weight for all targets combined must be less than or equal to 100.

                  - **virtualNode** *(string) --* **[REQUIRED]**

                    The virtual node to associate with the weighted target.

                  - **weight** *(integer) --* **[REQUIRED]**

                    The relative weight of the weighted target.

        :type tags: list
        :param tags:

          Optional metadata that you can apply to the route to assist with categorization and organization.
          Each tag consists of a key and an optional value, both of which you define. Tag keys can have a
          maximum character length of 128 characters, and tag values can have a maximum length of 256
          characters.

          - *(dict) --*

            Optional metadata that you apply to a resource to assist with categorization and organization.
            Each tag consists of a key and an optional value, both of which you define. Tag keys can have a
            maximum character length of 128 characters, and tag values can have a maximum length of 256
            characters.

            - **key** *(string) --* **[REQUIRED]**

              One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
              a category for more specific tag values.

            - **value** *(string) --*

              The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor
              within a tag category (key).

        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**

          The name of the virtual router in which to create the route.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'route': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'routeName': 'string',
                    'spec': {
                        'grpcRoute': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            },
                            'match': {
                                'metadata': [
                                    {
                                        'invert': True|False,
                                        'match': {
                                            'exact': 'string',
                                            'prefix': 'string',
                                            'range': {
                                                'end': 123,
                                                'start': 123
                                            },
                                            'regex': 'string',
                                            'suffix': 'string'
                                        },
                                        'name': 'string'
                                    },
                                ],
                                'methodName': 'string',
                                'serviceName': 'string'
                            },
                            'retryPolicy': {
                                'grpcRetryEvents': [
                                    'cancelled'|'deadline-exceeded'|'internal'|'resource-exhausted'
                                    |'unavailable',
                                ],
                                'httpRetryEvents': [
                                    'string',
                                ],
                                'maxRetries': 123,
                                'perRetryTimeout': {
                                    'unit': 'ms'|'s',
                                    'value': 123
                                },
                                'tcpRetryEvents': [
                                    'connection-error',
                                ]
                            }
                        },
                        'http2Route': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            },
                            'match': {
                                'headers': [
                                    {
                                        'invert': True|False,
                                        'match': {
                                            'exact': 'string',
                                            'prefix': 'string',
                                            'range': {
                                                'end': 123,
                                                'start': 123
                                            },
                                            'regex': 'string',
                                            'suffix': 'string'
                                        },
                                        'name': 'string'
                                    },
                                ],
                                'method':
                                'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                                'prefix': 'string',
                                'scheme': 'http'|'https'
                            },
                            'retryPolicy': {
                                'httpRetryEvents': [
                                    'string',
                                ],
                                'maxRetries': 123,
                                'perRetryTimeout': {
                                    'unit': 'ms'|'s',
                                    'value': 123
                                },
                                'tcpRetryEvents': [
                                    'connection-error',
                                ]
                            }
                        },
                        'httpRoute': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            },
                            'match': {
                                'headers': [
                                    {
                                        'invert': True|False,
                                        'match': {
                                            'exact': 'string',
                                            'prefix': 'string',
                                            'range': {
                                                'end': 123,
                                                'start': 123
                                            },
                                            'regex': 'string',
                                            'suffix': 'string'
                                        },
                                        'name': 'string'
                                    },
                                ],
                                'method':
                                'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                                'prefix': 'string',
                                'scheme': 'http'|'https'
                            },
                            'retryPolicy': {
                                'httpRetryEvents': [
                                    'string',
                                ],
                                'maxRetries': 123,
                                'perRetryTimeout': {
                                    'unit': 'ms'|'s',
                                    'value': 123
                                },
                                'tcpRetryEvents': [
                                    'connection-error',
                                ]
                            }
                        },
                        'priority': 123,
                        'tcpRoute': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualRouterName': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **route** *(dict) --*

              The full description of your mesh following the create call.

              - **meshName** *(string) --*

                The name of the service mesh that the route resides in.

              - **metadata** *(dict) --*

                The associated metadata for the route.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **routeName** *(string) --*

                The name of the route.

              - **spec** *(dict) --*

                The specifications of the route.

                - **grpcRoute** *(dict) --*

                  An object that represents the specification of a GRPC route.

                  - **action** *(dict) --*

                    An object that represents the action to take if a match is determined.

                    - **weightedTargets** *(list) --*

                      An object that represents the targets that traffic is routed to when a request
                      matches the route.

                      - *(dict) --*

                        An object that represents a target and its relative weight. Traffic is distributed
                        across targets according to their relative weight. For example, a weighted target
                        with a relative weight of 50 receives five times as much traffic as one with a
                        relative weight of 10. The total weight for all targets combined must be less than
                        or equal to 100.

                        - **virtualNode** *(string) --*

                          The virtual node to associate with the weighted target.

                        - **weight** *(integer) --*

                          The relative weight of the weighted target.

                  - **match** *(dict) --*

                    An object that represents the criteria for determining a request match.

                    - **metadata** *(list) --*

                      An object that represents the data to match from the request.

                      - *(dict) --*

                        An object that represents the match metadata for the route.

                        - **invert** *(boolean) --*

                          Specify ``True`` to match anything except the match criteria. The default value
                          is ``False`` .

                        - **match** *(dict) --*

                          An object that represents the data to match from the request.

                          - **exact** *(string) --*

                            The value sent by the client must match the specified value exactly.

                          - **prefix** *(string) --*

                            The value sent by the client must begin with the specified characters.

                          - **range** *(dict) --*

                            An object that represents the range of values to match on.

                            - **end** *(integer) --*

                              The end of the range.

                            - **start** *(integer) --*

                              The start of the range.

                          - **regex** *(string) --*

                            The value sent by the client must include the specified characters.

                          - **suffix** *(string) --*

                            The value sent by the client must end with the specified characters.

                        - **name** *(string) --*

                          The name of the route.

                    - **methodName** *(string) --*

                      The method name to match from the request. If you specify a name, you must also
                      specify a ``serviceName`` .

                    - **serviceName** *(string) --*

                      The fully qualified domain name for the service to match from the request.

                  - **retryPolicy** *(dict) --*

                    An object that represents a retry policy.

                    - **grpcRetryEvents** *(list) --*

                      Specify at least one of the valid values.

                      - *(string) --*

                    - **httpRetryEvents** *(list) --*

                      Specify at least one of the following values.

                      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
                      510, and 511

                      * **gateway-error** – HTTP status codes 502, 503, and 504

                      * **client-error** – HTTP status code 409

                      * **stream-error** – Retry on refused stream

                      - *(string) --*

                    - **maxRetries** *(integer) --*

                      The maximum number of retry attempts.

                    - **perRetryTimeout** *(dict) --*

                      An object that represents a duration of time.

                      - **unit** *(string) --*

                        A unit of time.

                      - **value** *(integer) --*

                        A number of time units.

                    - **tcpRetryEvents** *(list) --*

                      Specify a valid value.

                      - *(string) --*

                - **http2Route** *(dict) --*

                  An object that represents the specification of an HTTP2 route.

                  - **action** *(dict) --*

                    An object that represents the action to take if a match is determined.

                    - **weightedTargets** *(list) --*

                      An object that represents the targets that traffic is routed to when a request
                      matches the route.

                      - *(dict) --*

                        An object that represents a target and its relative weight. Traffic is distributed
                        across targets according to their relative weight. For example, a weighted target
                        with a relative weight of 50 receives five times as much traffic as one with a
                        relative weight of 10. The total weight for all targets combined must be less than
                        or equal to 100.

                        - **virtualNode** *(string) --*

                          The virtual node to associate with the weighted target.

                        - **weight** *(integer) --*

                          The relative weight of the weighted target.

                  - **match** *(dict) --*

                    An object that represents the criteria for determining a request match.

                    - **headers** *(list) --*

                      An object that represents the client request headers to match on.

                      - *(dict) --*

                        An object that represents the HTTP header in the request.

                        - **invert** *(boolean) --*

                          Specify ``True`` to match anything except the match criteria. The default value
                          is ``False`` .

                        - **match** *(dict) --*

                          The ``HeaderMatchMethod`` object.

                          - **exact** *(string) --*

                            The value sent by the client must match the specified value exactly.

                          - **prefix** *(string) --*

                            The value sent by the client must begin with the specified characters.

                          - **range** *(dict) --*

                            An object that represents the range of values to match on.

                            - **end** *(integer) --*

                              The end of the range.

                            - **start** *(integer) --*

                              The start of the range.

                          - **regex** *(string) --*

                            The value sent by the client must include the specified characters.

                          - **suffix** *(string) --*

                            The value sent by the client must end with the specified characters.

                        - **name** *(string) --*

                          A name for the HTTP header in the client request that will be matched on.

                    - **method** *(string) --*

                      The client request method to match on. Specify only one.

                    - **prefix** *(string) --*

                      Specifies the path to match requests with. This parameter must always start with
                      ``/`` , which by itself matches all requests to the virtual service name. You can
                      also match for path-based routing of requests. For example, if your virtual service
                      name is ``my-service.local`` and you want the route to match requests to
                      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

                    - **scheme** *(string) --*

                      The client request scheme to match on. Specify only one.

                  - **retryPolicy** *(dict) --*

                    An object that represents a retry policy.

                    - **httpRetryEvents** *(list) --*

                      Specify at least one of the following values.

                      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
                      510, and 511

                      * **gateway-error** – HTTP status codes 502, 503, and 504

                      * **client-error** – HTTP status code 409

                      * **stream-error** – Retry on refused stream

                      - *(string) --*

                    - **maxRetries** *(integer) --*

                      The maximum number of retry attempts.

                    - **perRetryTimeout** *(dict) --*

                      An object that represents a duration of time.

                      - **unit** *(string) --*

                        A unit of time.

                      - **value** *(integer) --*

                        A number of time units.

                    - **tcpRetryEvents** *(list) --*

                      Specify a valid value.

                      - *(string) --*

                - **httpRoute** *(dict) --*

                  An object that represents the specification of an HTTP route.

                  - **action** *(dict) --*

                    An object that represents the action to take if a match is determined.

                    - **weightedTargets** *(list) --*

                      An object that represents the targets that traffic is routed to when a request
                      matches the route.

                      - *(dict) --*

                        An object that represents a target and its relative weight. Traffic is distributed
                        across targets according to their relative weight. For example, a weighted target
                        with a relative weight of 50 receives five times as much traffic as one with a
                        relative weight of 10. The total weight for all targets combined must be less than
                        or equal to 100.

                        - **virtualNode** *(string) --*

                          The virtual node to associate with the weighted target.

                        - **weight** *(integer) --*

                          The relative weight of the weighted target.

                  - **match** *(dict) --*

                    An object that represents the criteria for determining a request match.

                    - **headers** *(list) --*

                      An object that represents the client request headers to match on.

                      - *(dict) --*

                        An object that represents the HTTP header in the request.

                        - **invert** *(boolean) --*

                          Specify ``True`` to match anything except the match criteria. The default value
                          is ``False`` .

                        - **match** *(dict) --*

                          The ``HeaderMatchMethod`` object.

                          - **exact** *(string) --*

                            The value sent by the client must match the specified value exactly.

                          - **prefix** *(string) --*

                            The value sent by the client must begin with the specified characters.

                          - **range** *(dict) --*

                            An object that represents the range of values to match on.

                            - **end** *(integer) --*

                              The end of the range.

                            - **start** *(integer) --*

                              The start of the range.

                          - **regex** *(string) --*

                            The value sent by the client must include the specified characters.

                          - **suffix** *(string) --*

                            The value sent by the client must end with the specified characters.

                        - **name** *(string) --*

                          A name for the HTTP header in the client request that will be matched on.

                    - **method** *(string) --*

                      The client request method to match on. Specify only one.

                    - **prefix** *(string) --*

                      Specifies the path to match requests with. This parameter must always start with
                      ``/`` , which by itself matches all requests to the virtual service name. You can
                      also match for path-based routing of requests. For example, if your virtual service
                      name is ``my-service.local`` and you want the route to match requests to
                      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

                    - **scheme** *(string) --*

                      The client request scheme to match on. Specify only one.

                  - **retryPolicy** *(dict) --*

                    An object that represents a retry policy.

                    - **httpRetryEvents** *(list) --*

                      Specify at least one of the following values.

                      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
                      510, and 511

                      * **gateway-error** – HTTP status codes 502, 503, and 504

                      * **client-error** – HTTP status code 409

                      * **stream-error** – Retry on refused stream

                      - *(string) --*

                    - **maxRetries** *(integer) --*

                      The maximum number of retry attempts.

                    - **perRetryTimeout** *(dict) --*

                      An object that represents a duration of time.

                      - **unit** *(string) --*

                        A unit of time.

                      - **value** *(integer) --*

                        A number of time units.

                    - **tcpRetryEvents** *(list) --*

                      Specify a valid value.

                      - *(string) --*

                - **priority** *(integer) --*

                  The priority for the route. Routes are matched based on the specified value, where 0 is
                  the highest priority.

                - **tcpRoute** *(dict) --*

                  An object that represents the specification of a TCP route.

                  - **action** *(dict) --*

                    The action to take if a match is determined.

                    - **weightedTargets** *(list) --*

                      An object that represents the targets that traffic is routed to when a request
                      matches the route.

                      - *(dict) --*

                        An object that represents a target and its relative weight. Traffic is distributed
                        across targets according to their relative weight. For example, a weighted target
                        with a relative weight of 50 receives five times as much traffic as one with a
                        relative weight of 10. The total weight for all targets combined must be less than
                        or equal to 100.

                        - **virtualNode** *(string) --*

                          The virtual node to associate with the weighted target.

                        - **weight** *(integer) --*

                          The relative weight of the weighted target.

              - **status** *(dict) --*

                The status of the route.

                - **status** *(string) --*

                  The current status for the route.

              - **virtualRouterName** *(string) --*

                The virtual router that the route is associated with.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_virtual_node(
        self,
        meshName: str,
        spec: ClientCreateVirtualNodespecTypeDef,
        virtualNodeName: str,
        clientToken: str = None,
        tags: List[ClientCreateVirtualNodetagsTypeDef] = None,
    ) -> ClientCreateVirtualNodeResponseTypeDef:
        """
        Creates a virtual node within a service mesh.

        A virtual node acts as a logical pointer to a particular task group, such as an Amazon ECS service
        or a Kubernetes deployment. When you create a virtual node, you can specify the service discovery
        information for your task group.

        Any inbound traffic that your virtual node expects should be specified as a ``listener`` . Any
        outbound traffic that your virtual node expects to reach should be specified as a ``backend`` .

        The response metadata for your new virtual node contains the ``arn`` that is associated with the
        virtual node. Set this value (either the full ARN or the truncated resource name: for example,
        ``mesh/default/virtualNode/simpleapp`` ) as the ``APPMESH_VIRTUAL_NODE_NAME`` environment variable
        for your task group's Envoy proxy container in your task definition or pod spec. This is then
        mapped to the ``node.id`` and ``node.cluster`` Envoy parameters.

        .. note::

          If you require your Envoy stats or tracing to use a different name, you can override the
          ``node.cluster`` value that is set by ``APPMESH_VIRTUAL_NODE_NAME`` with the
          ``APPMESH_VIRTUAL_NODE_CLUSTER`` environment variable.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/CreateVirtualNode>`_

        **Request Syntax**
        ::

          response = client.create_virtual_node(
              clientToken='string',
              meshName='string',
              spec={
                  'backends': [
                      {
                          'virtualService': {
                              'virtualServiceName': 'string'
                          }
                      },
                  ],
                  'listeners': [
                      {
                          'healthCheck': {
                              'healthyThreshold': 123,
                              'intervalMillis': 123,
                              'path': 'string',
                              'port': 123,
                              'protocol': 'grpc'|'http'|'http2'|'tcp',
                              'timeoutMillis': 123,
                              'unhealthyThreshold': 123
                          },
                          'portMapping': {
                              'port': 123,
                              'protocol': 'grpc'|'http'|'http2'|'tcp'
                          }
                      },
                  ],
                  'logging': {
                      'accessLog': {
                          'file': {
                              'path': 'string'
                          }
                      }
                  },
                  'serviceDiscovery': {
                      'awsCloudMap': {
                          'attributes': [
                              {
                                  'key': 'string',
                                  'value': 'string'
                              },
                          ],
                          'namespaceName': 'string',
                          'serviceName': 'string'
                      },
                      'dns': {
                          'hostname': 'string'
                      }
                  }
              },
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ],
              virtualNodeName='string'
          )
        :type clientToken: string
        :param clientToken:

          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up
          to 36 letters, numbers, hyphens, and underscores are allowed.

          This field is autopopulated if not provided.

        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh to create the virtual node in.

        :type spec: dict
        :param spec: **[REQUIRED]**

          The virtual node specification to apply.

          - **backends** *(list) --*

            The backends that the virtual node is expected to send outbound traffic to.

            - *(dict) --*

              An object that represents the backends that a virtual node is expected to send outbound
              traffic to.

              - **virtualService** *(dict) --*

                Specifies a virtual service to use as a backend for a virtual node.

                - **virtualServiceName** *(string) --* **[REQUIRED]**

                  The name of the virtual service that is acting as a virtual node backend.

          - **listeners** *(list) --*

            The listeners that the virtual node is expected to receive inbound traffic from. You can
            specify one listener.

            - *(dict) --*

              An object that represents a listener for a virtual node.

              - **healthCheck** *(dict) --*

                The health check information for the listener.

                - **healthyThreshold** *(integer) --* **[REQUIRED]**

                  The number of consecutive successful health checks that must occur before declaring
                  listener healthy.

                - **intervalMillis** *(integer) --* **[REQUIRED]**

                  The time period in milliseconds between each health check execution.

                - **path** *(string) --*

                  The destination path for the health check request. This is required only if the specified
                  protocol is HTTP. If the protocol is TCP, this parameter is ignored.

                - **port** *(integer) --*

                  The destination port for the health check request. This port must match the port defined
                  in the  PortMapping for the listener.

                - **protocol** *(string) --* **[REQUIRED]**

                  The protocol for the health check request.

                - **timeoutMillis** *(integer) --* **[REQUIRED]**

                  The amount of time to wait when receiving a response from the health check, in
                  milliseconds.

                - **unhealthyThreshold** *(integer) --* **[REQUIRED]**

                  The number of consecutive failed health checks that must occur before declaring a virtual
                  node unhealthy.

              - **portMapping** *(dict) --* **[REQUIRED]**

                The port mapping information for the listener.

                - **port** *(integer) --* **[REQUIRED]**

                  The port used for the port mapping.

                - **protocol** *(string) --* **[REQUIRED]**

                  The protocol used for the port mapping. Specify one protocol.

          - **logging** *(dict) --*

            The inbound and outbound access logging information for the virtual node.

            - **accessLog** *(dict) --*

              The access log configuration for a virtual node.

              - **file** *(dict) --*

                The file object to send virtual node access logs to.

                - **path** *(string) --* **[REQUIRED]**

                  The file path to write access logs to. You can use ``/dev/stdout`` to send access logs to
                  standard out and configure your Envoy container to use a log driver, such as ``awslogs``
                  , to export the access logs to a log storage service such as Amazon CloudWatch Logs. You
                  can also specify a path in the Envoy container's file system to write the files to disk.

                  .. note::

                    The Envoy process must have write permissions to the path that you specify here.
                    Otherwise, Envoy fails to bootstrap properly.

          - **serviceDiscovery** *(dict) --*

            The service discovery information for the virtual node. If your virtual node does not expect
            ingress traffic, you can omit this parameter.

            - **awsCloudMap** *(dict) --*

              Specifies any AWS Cloud Map information for the virtual node.

              - **attributes** *(list) --*

                A string map that contains attributes with values that you can use to filter instances by
                any custom attribute that you specified when you registered the instance. Only instances
                that match all of the specified key/value pairs will be returned.

                - *(dict) --*

                  An object that represents the AWS Cloud Map attribute information for your virtual node.

                  - **key** *(string) --* **[REQUIRED]**

                    The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
                    instance that contains the specified key and value is returned.

                  - **value** *(string) --* **[REQUIRED]**

                    The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
                    instance that contains the specified key and value is returned.

              - **namespaceName** *(string) --* **[REQUIRED]**

                The name of the AWS Cloud Map namespace to use.

              - **serviceName** *(string) --* **[REQUIRED]**

                The name of the AWS Cloud Map service to use.

            - **dns** *(dict) --*

              Specifies the DNS information for the virtual node.

              - **hostname** *(string) --* **[REQUIRED]**

                Specifies the DNS service discovery hostname for the virtual node.

        :type tags: list
        :param tags:

          Optional metadata that you can apply to the virtual node to assist with categorization and
          organization. Each tag consists of a key and an optional value, both of which you define. Tag
          keys can have a maximum character length of 128 characters, and tag values can have a maximum
          length of 256 characters.

          - *(dict) --*

            Optional metadata that you apply to a resource to assist with categorization and organization.
            Each tag consists of a key and an optional value, both of which you define. Tag keys can have a
            maximum character length of 128 characters, and tag values can have a maximum length of 256
            characters.

            - **key** *(string) --* **[REQUIRED]**

              One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
              a category for more specific tag values.

            - **value** *(string) --*

              The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor
              within a tag category (key).

        :type virtualNodeName: string
        :param virtualNodeName: **[REQUIRED]**

          The name to use for the virtual node.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'virtualNode': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'backends': [
                            {
                                'virtualService': {
                                    'virtualServiceName': 'string'
                                }
                            },
                        ],
                        'listeners': [
                            {
                                'healthCheck': {
                                    'healthyThreshold': 123,
                                    'intervalMillis': 123,
                                    'path': 'string',
                                    'port': 123,
                                    'protocol': 'grpc'|'http'|'http2'|'tcp',
                                    'timeoutMillis': 123,
                                    'unhealthyThreshold': 123
                                },
                                'portMapping': {
                                    'port': 123,
                                    'protocol': 'grpc'|'http'|'http2'|'tcp'
                                }
                            },
                        ],
                        'logging': {
                            'accessLog': {
                                'file': {
                                    'path': 'string'
                                }
                            }
                        },
                        'serviceDiscovery': {
                            'awsCloudMap': {
                                'attributes': [
                                    {
                                        'key': 'string',
                                        'value': 'string'
                                    },
                                ],
                                'namespaceName': 'string',
                                'serviceName': 'string'
                            },
                            'dns': {
                                'hostname': 'string'
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualNodeName': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **virtualNode** *(dict) --*

              The full description of your virtual node following the create call.

              - **meshName** *(string) --*

                The name of the service mesh that the virtual node resides in.

              - **metadata** *(dict) --*

                The associated metadata for the virtual node.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **spec** *(dict) --*

                The specifications of the virtual node.

                - **backends** *(list) --*

                  The backends that the virtual node is expected to send outbound traffic to.

                  - *(dict) --*

                    An object that represents the backends that a virtual node is expected to send outbound
                    traffic to.

                    - **virtualService** *(dict) --*

                      Specifies a virtual service to use as a backend for a virtual node.

                      - **virtualServiceName** *(string) --*

                        The name of the virtual service that is acting as a virtual node backend.

                - **listeners** *(list) --*

                  The listeners that the virtual node is expected to receive inbound traffic from. You can
                  specify one listener.

                  - *(dict) --*

                    An object that represents a listener for a virtual node.

                    - **healthCheck** *(dict) --*

                      The health check information for the listener.

                      - **healthyThreshold** *(integer) --*

                        The number of consecutive successful health checks that must occur before declaring
                        listener healthy.

                      - **intervalMillis** *(integer) --*

                        The time period in milliseconds between each health check execution.

                      - **path** *(string) --*

                        The destination path for the health check request. This is required only if the
                        specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

                      - **port** *(integer) --*

                        The destination port for the health check request. This port must match the port
                        defined in the  PortMapping for the listener.

                      - **protocol** *(string) --*

                        The protocol for the health check request.

                      - **timeoutMillis** *(integer) --*

                        The amount of time to wait when receiving a response from the health check, in
                        milliseconds.

                      - **unhealthyThreshold** *(integer) --*

                        The number of consecutive failed health checks that must occur before declaring a
                        virtual node unhealthy.

                    - **portMapping** *(dict) --*

                      The port mapping information for the listener.

                      - **port** *(integer) --*

                        The port used for the port mapping.

                      - **protocol** *(string) --*

                        The protocol used for the port mapping. Specify one protocol.

                - **logging** *(dict) --*

                  The inbound and outbound access logging information for the virtual node.

                  - **accessLog** *(dict) --*

                    The access log configuration for a virtual node.

                    - **file** *(dict) --*

                      The file object to send virtual node access logs to.

                      - **path** *(string) --*

                        The file path to write access logs to. You can use ``/dev/stdout`` to send access
                        logs to standard out and configure your Envoy container to use a log driver, such
                        as ``awslogs`` , to export the access logs to a log storage service such as Amazon
                        CloudWatch Logs. You can also specify a path in the Envoy container's file system
                        to write the files to disk.

                        .. note::

                          The Envoy process must have write permissions to the path that you specify here.
                          Otherwise, Envoy fails to bootstrap properly.

                - **serviceDiscovery** *(dict) --*

                  The service discovery information for the virtual node. If your virtual node does not
                  expect ingress traffic, you can omit this parameter.

                  - **awsCloudMap** *(dict) --*

                    Specifies any AWS Cloud Map information for the virtual node.

                    - **attributes** *(list) --*

                      A string map that contains attributes with values that you can use to filter
                      instances by any custom attribute that you specified when you registered the
                      instance. Only instances that match all of the specified key/value pairs will be
                      returned.

                      - *(dict) --*

                        An object that represents the AWS Cloud Map attribute information for your virtual
                        node.

                        - **key** *(string) --*

                          The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                          service instance that contains the specified key and value is returned.

                        - **value** *(string) --*

                          The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                          service instance that contains the specified key and value is returned.

                    - **namespaceName** *(string) --*

                      The name of the AWS Cloud Map namespace to use.

                    - **serviceName** *(string) --*

                      The name of the AWS Cloud Map service to use.

                  - **dns** *(dict) --*

                    Specifies the DNS information for the virtual node.

                    - **hostname** *(string) --*

                      Specifies the DNS service discovery hostname for the virtual node.

              - **status** *(dict) --*

                The current status for the virtual node.

                - **status** *(string) --*

                  The current status of the virtual node.

              - **virtualNodeName** *(string) --*

                The name of the virtual node.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_virtual_router(
        self,
        meshName: str,
        spec: ClientCreateVirtualRouterspecTypeDef,
        virtualRouterName: str,
        clientToken: str = None,
        tags: List[ClientCreateVirtualRoutertagsTypeDef] = None,
    ) -> ClientCreateVirtualRouterResponseTypeDef:
        """
        Creates a virtual router within a service mesh.

        Any inbound traffic that your virtual router expects should be specified as a ``listener`` .

        Virtual routers handle traffic for one or more virtual services within your mesh. After you create
        your virtual router, create and associate routes for your virtual router that direct incoming
        requests to different virtual nodes.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/CreateVirtualRouter>`_

        **Request Syntax**
        ::

          response = client.create_virtual_router(
              clientToken='string',
              meshName='string',
              spec={
                  'listeners': [
                      {
                          'portMapping': {
                              'port': 123,
                              'protocol': 'grpc'|'http'|'http2'|'tcp'
                          }
                      },
                  ]
              },
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ],
              virtualRouterName='string'
          )
        :type clientToken: string
        :param clientToken:

          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up
          to 36 letters, numbers, hyphens, and underscores are allowed.

          This field is autopopulated if not provided.

        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh to create the virtual router in.

        :type spec: dict
        :param spec: **[REQUIRED]**

          The virtual router specification to apply.

          - **listeners** *(list) --*

            The listeners that the virtual router is expected to receive inbound traffic from. You can
            specify one listener.

            - *(dict) --*

              An object that represents a virtual router listener.

              - **portMapping** *(dict) --* **[REQUIRED]**

                An object that represents a port mapping.

                - **port** *(integer) --* **[REQUIRED]**

                  The port used for the port mapping.

                - **protocol** *(string) --* **[REQUIRED]**

                  The protocol used for the port mapping. Specify one protocol.

        :type tags: list
        :param tags:

          Optional metadata that you can apply to the virtual router to assist with categorization and
          organization. Each tag consists of a key and an optional value, both of which you define. Tag
          keys can have a maximum character length of 128 characters, and tag values can have a maximum
          length of 256 characters.

          - *(dict) --*

            Optional metadata that you apply to a resource to assist with categorization and organization.
            Each tag consists of a key and an optional value, both of which you define. Tag keys can have a
            maximum character length of 128 characters, and tag values can have a maximum length of 256
            characters.

            - **key** *(string) --* **[REQUIRED]**

              One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
              a category for more specific tag values.

            - **value** *(string) --*

              The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor
              within a tag category (key).

        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**

          The name to use for the virtual router.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'virtualRouter': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'listeners': [
                            {
                                'portMapping': {
                                    'port': 123,
                                    'protocol': 'grpc'|'http'|'http2'|'tcp'
                                }
                            },
                        ]
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualRouterName': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **virtualRouter** *(dict) --*

              The full description of your virtual router following the create call.

              - **meshName** *(string) --*

                The name of the service mesh that the virtual router resides in.

              - **metadata** *(dict) --*

                The associated metadata for the virtual router.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **spec** *(dict) --*

                The specifications of the virtual router.

                - **listeners** *(list) --*

                  The listeners that the virtual router is expected to receive inbound traffic from. You
                  can specify one listener.

                  - *(dict) --*

                    An object that represents a virtual router listener.

                    - **portMapping** *(dict) --*

                      An object that represents a port mapping.

                      - **port** *(integer) --*

                        The port used for the port mapping.

                      - **protocol** *(string) --*

                        The protocol used for the port mapping. Specify one protocol.

              - **status** *(dict) --*

                The current status of the virtual router.

                - **status** *(string) --*

                  The current status of the virtual router.

              - **virtualRouterName** *(string) --*

                The name of the virtual router.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_virtual_service(
        self,
        meshName: str,
        spec: ClientCreateVirtualServicespecTypeDef,
        virtualServiceName: str,
        clientToken: str = None,
        tags: List[ClientCreateVirtualServicetagsTypeDef] = None,
    ) -> ClientCreateVirtualServiceResponseTypeDef:
        """
        Creates a virtual service within a service mesh.

        A virtual service is an abstraction of a real service that is provided by a virtual node directly
        or indirectly by means of a virtual router. Dependent services call your virtual service by its
        ``virtualServiceName`` , and those requests are routed to the virtual node or virtual router that
        is specified as the provider for the virtual service.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/CreateVirtualService>`_

        **Request Syntax**
        ::

          response = client.create_virtual_service(
              clientToken='string',
              meshName='string',
              spec={
                  'provider': {
                      'virtualNode': {
                          'virtualNodeName': 'string'
                      },
                      'virtualRouter': {
                          'virtualRouterName': 'string'
                      }
                  }
              },
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ],
              virtualServiceName='string'
          )
        :type clientToken: string
        :param clientToken:

          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up
          to 36 letters, numbers, hyphens, and underscores are allowed.

          This field is autopopulated if not provided.

        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh to create the virtual service in.

        :type spec: dict
        :param spec: **[REQUIRED]**

          The virtual service specification to apply.

          - **provider** *(dict) --*

            The App Mesh object that is acting as the provider for a virtual service. You can specify a
            single virtual node or virtual router.

            - **virtualNode** *(dict) --*

              The virtual node associated with a virtual service.

              - **virtualNodeName** *(string) --* **[REQUIRED]**

                The name of the virtual node that is acting as a service provider.

            - **virtualRouter** *(dict) --*

              The virtual router associated with a virtual service.

              - **virtualRouterName** *(string) --* **[REQUIRED]**

                The name of the virtual router that is acting as a service provider.

        :type tags: list
        :param tags:

          Optional metadata that you can apply to the virtual service to assist with categorization and
          organization. Each tag consists of a key and an optional value, both of which you define. Tag
          keys can have a maximum character length of 128 characters, and tag values can have a maximum
          length of 256 characters.

          - *(dict) --*

            Optional metadata that you apply to a resource to assist with categorization and organization.
            Each tag consists of a key and an optional value, both of which you define. Tag keys can have a
            maximum character length of 128 characters, and tag values can have a maximum length of 256
            characters.

            - **key** *(string) --* **[REQUIRED]**

              One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
              a category for more specific tag values.

            - **value** *(string) --*

              The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor
              within a tag category (key).

        :type virtualServiceName: string
        :param virtualServiceName: **[REQUIRED]**

          The name to use for the virtual service.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'virtualService': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'provider': {
                            'virtualNode': {
                                'virtualNodeName': 'string'
                            },
                            'virtualRouter': {
                                'virtualRouterName': 'string'
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualServiceName': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **virtualService** *(dict) --*

              The full description of your virtual service following the create call.

              - **meshName** *(string) --*

                The name of the service mesh that the virtual service resides in.

              - **metadata** *(dict) --*

                An object that represents metadata for a resource.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **spec** *(dict) --*

                The specifications of the virtual service.

                - **provider** *(dict) --*

                  The App Mesh object that is acting as the provider for a virtual service. You can specify
                  a single virtual node or virtual router.

                  - **virtualNode** *(dict) --*

                    The virtual node associated with a virtual service.

                    - **virtualNodeName** *(string) --*

                      The name of the virtual node that is acting as a service provider.

                  - **virtualRouter** *(dict) --*

                    The virtual router associated with a virtual service.

                    - **virtualRouterName** *(string) --*

                      The name of the virtual router that is acting as a service provider.

              - **status** *(dict) --*

                The current status of the virtual service.

                - **status** *(string) --*

                  The current status of the virtual service.

              - **virtualServiceName** *(string) --*

                The name of the virtual service.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_mesh(self, meshName: str) -> ClientDeleteMeshResponseTypeDef:
        """
        Deletes an existing service mesh.

        You must delete all resources (virtual services, routes, virtual routers, and virtual nodes) in the
        service mesh before you can delete the mesh itself.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/DeleteMesh>`_

        **Request Syntax**
        ::

          response = client.delete_mesh(
              meshName='string'
          )
        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'mesh': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'egressFilter': {
                            'type': 'ALLOW_ALL'|'DROP_ALL'
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **mesh** *(dict) --*

              The service mesh that was deleted.

              - **meshName** *(string) --*

                The name of the service mesh.

              - **metadata** *(dict) --*

                The associated metadata for the service mesh.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **spec** *(dict) --*

                The associated specification for the service mesh.

                - **egressFilter** *(dict) --*

                  The egress filter rules for the service mesh.

                  - **type** *(string) --*

                    The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
                    from virtual nodes to other defined resources in the service mesh (and any traffic to
                    ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
                    ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.

              - **status** *(dict) --*

                The status of the service mesh.

                - **status** *(string) --*

                  The current mesh status.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_route(
        self, meshName: str, routeName: str, virtualRouterName: str
    ) -> ClientDeleteRouteResponseTypeDef:
        """
        Deletes an existing route.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/DeleteRoute>`_

        **Request Syntax**
        ::

          response = client.delete_route(
              meshName='string',
              routeName='string',
              virtualRouterName='string'
          )
        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh to delete the route in.

        :type routeName: string
        :param routeName: **[REQUIRED]**

          The name of the route to delete.

        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**

          The name of the virtual router to delete the route in.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'route': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'routeName': 'string',
                    'spec': {
                        'grpcRoute': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            },
                            'match': {
                                'metadata': [
                                    {
                                        'invert': True|False,
                                        'match': {
                                            'exact': 'string',
                                            'prefix': 'string',
                                            'range': {
                                                'end': 123,
                                                'start': 123
                                            },
                                            'regex': 'string',
                                            'suffix': 'string'
                                        },
                                        'name': 'string'
                                    },
                                ],
                                'methodName': 'string',
                                'serviceName': 'string'
                            },
                            'retryPolicy': {
                                'grpcRetryEvents': [
                                    'cancelled'|'deadline-exceeded'|'internal'|'resource-exhausted'
                                    |'unavailable',
                                ],
                                'httpRetryEvents': [
                                    'string',
                                ],
                                'maxRetries': 123,
                                'perRetryTimeout': {
                                    'unit': 'ms'|'s',
                                    'value': 123
                                },
                                'tcpRetryEvents': [
                                    'connection-error',
                                ]
                            }
                        },
                        'http2Route': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            },
                            'match': {
                                'headers': [
                                    {
                                        'invert': True|False,
                                        'match': {
                                            'exact': 'string',
                                            'prefix': 'string',
                                            'range': {
                                                'end': 123,
                                                'start': 123
                                            },
                                            'regex': 'string',
                                            'suffix': 'string'
                                        },
                                        'name': 'string'
                                    },
                                ],
                                'method':
                                'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                                'prefix': 'string',
                                'scheme': 'http'|'https'
                            },
                            'retryPolicy': {
                                'httpRetryEvents': [
                                    'string',
                                ],
                                'maxRetries': 123,
                                'perRetryTimeout': {
                                    'unit': 'ms'|'s',
                                    'value': 123
                                },
                                'tcpRetryEvents': [
                                    'connection-error',
                                ]
                            }
                        },
                        'httpRoute': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            },
                            'match': {
                                'headers': [
                                    {
                                        'invert': True|False,
                                        'match': {
                                            'exact': 'string',
                                            'prefix': 'string',
                                            'range': {
                                                'end': 123,
                                                'start': 123
                                            },
                                            'regex': 'string',
                                            'suffix': 'string'
                                        },
                                        'name': 'string'
                                    },
                                ],
                                'method':
                                'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                                'prefix': 'string',
                                'scheme': 'http'|'https'
                            },
                            'retryPolicy': {
                                'httpRetryEvents': [
                                    'string',
                                ],
                                'maxRetries': 123,
                                'perRetryTimeout': {
                                    'unit': 'ms'|'s',
                                    'value': 123
                                },
                                'tcpRetryEvents': [
                                    'connection-error',
                                ]
                            }
                        },
                        'priority': 123,
                        'tcpRoute': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualRouterName': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **route** *(dict) --*

              The route that was deleted.

              - **meshName** *(string) --*

                The name of the service mesh that the route resides in.

              - **metadata** *(dict) --*

                The associated metadata for the route.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **routeName** *(string) --*

                The name of the route.

              - **spec** *(dict) --*

                The specifications of the route.

                - **grpcRoute** *(dict) --*

                  An object that represents the specification of a GRPC route.

                  - **action** *(dict) --*

                    An object that represents the action to take if a match is determined.

                    - **weightedTargets** *(list) --*

                      An object that represents the targets that traffic is routed to when a request
                      matches the route.

                      - *(dict) --*

                        An object that represents a target and its relative weight. Traffic is distributed
                        across targets according to their relative weight. For example, a weighted target
                        with a relative weight of 50 receives five times as much traffic as one with a
                        relative weight of 10. The total weight for all targets combined must be less than
                        or equal to 100.

                        - **virtualNode** *(string) --*

                          The virtual node to associate with the weighted target.

                        - **weight** *(integer) --*

                          The relative weight of the weighted target.

                  - **match** *(dict) --*

                    An object that represents the criteria for determining a request match.

                    - **metadata** *(list) --*

                      An object that represents the data to match from the request.

                      - *(dict) --*

                        An object that represents the match metadata for the route.

                        - **invert** *(boolean) --*

                          Specify ``True`` to match anything except the match criteria. The default value
                          is ``False`` .

                        - **match** *(dict) --*

                          An object that represents the data to match from the request.

                          - **exact** *(string) --*

                            The value sent by the client must match the specified value exactly.

                          - **prefix** *(string) --*

                            The value sent by the client must begin with the specified characters.

                          - **range** *(dict) --*

                            An object that represents the range of values to match on.

                            - **end** *(integer) --*

                              The end of the range.

                            - **start** *(integer) --*

                              The start of the range.

                          - **regex** *(string) --*

                            The value sent by the client must include the specified characters.

                          - **suffix** *(string) --*

                            The value sent by the client must end with the specified characters.

                        - **name** *(string) --*

                          The name of the route.

                    - **methodName** *(string) --*

                      The method name to match from the request. If you specify a name, you must also
                      specify a ``serviceName`` .

                    - **serviceName** *(string) --*

                      The fully qualified domain name for the service to match from the request.

                  - **retryPolicy** *(dict) --*

                    An object that represents a retry policy.

                    - **grpcRetryEvents** *(list) --*

                      Specify at least one of the valid values.

                      - *(string) --*

                    - **httpRetryEvents** *(list) --*

                      Specify at least one of the following values.

                      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
                      510, and 511

                      * **gateway-error** – HTTP status codes 502, 503, and 504

                      * **client-error** – HTTP status code 409

                      * **stream-error** – Retry on refused stream

                      - *(string) --*

                    - **maxRetries** *(integer) --*

                      The maximum number of retry attempts.

                    - **perRetryTimeout** *(dict) --*

                      An object that represents a duration of time.

                      - **unit** *(string) --*

                        A unit of time.

                      - **value** *(integer) --*

                        A number of time units.

                    - **tcpRetryEvents** *(list) --*

                      Specify a valid value.

                      - *(string) --*

                - **http2Route** *(dict) --*

                  An object that represents the specification of an HTTP2 route.

                  - **action** *(dict) --*

                    An object that represents the action to take if a match is determined.

                    - **weightedTargets** *(list) --*

                      An object that represents the targets that traffic is routed to when a request
                      matches the route.

                      - *(dict) --*

                        An object that represents a target and its relative weight. Traffic is distributed
                        across targets according to their relative weight. For example, a weighted target
                        with a relative weight of 50 receives five times as much traffic as one with a
                        relative weight of 10. The total weight for all targets combined must be less than
                        or equal to 100.

                        - **virtualNode** *(string) --*

                          The virtual node to associate with the weighted target.

                        - **weight** *(integer) --*

                          The relative weight of the weighted target.

                  - **match** *(dict) --*

                    An object that represents the criteria for determining a request match.

                    - **headers** *(list) --*

                      An object that represents the client request headers to match on.

                      - *(dict) --*

                        An object that represents the HTTP header in the request.

                        - **invert** *(boolean) --*

                          Specify ``True`` to match anything except the match criteria. The default value
                          is ``False`` .

                        - **match** *(dict) --*

                          The ``HeaderMatchMethod`` object.

                          - **exact** *(string) --*

                            The value sent by the client must match the specified value exactly.

                          - **prefix** *(string) --*

                            The value sent by the client must begin with the specified characters.

                          - **range** *(dict) --*

                            An object that represents the range of values to match on.

                            - **end** *(integer) --*

                              The end of the range.

                            - **start** *(integer) --*

                              The start of the range.

                          - **regex** *(string) --*

                            The value sent by the client must include the specified characters.

                          - **suffix** *(string) --*

                            The value sent by the client must end with the specified characters.

                        - **name** *(string) --*

                          A name for the HTTP header in the client request that will be matched on.

                    - **method** *(string) --*

                      The client request method to match on. Specify only one.

                    - **prefix** *(string) --*

                      Specifies the path to match requests with. This parameter must always start with
                      ``/`` , which by itself matches all requests to the virtual service name. You can
                      also match for path-based routing of requests. For example, if your virtual service
                      name is ``my-service.local`` and you want the route to match requests to
                      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

                    - **scheme** *(string) --*

                      The client request scheme to match on. Specify only one.

                  - **retryPolicy** *(dict) --*

                    An object that represents a retry policy.

                    - **httpRetryEvents** *(list) --*

                      Specify at least one of the following values.

                      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
                      510, and 511

                      * **gateway-error** – HTTP status codes 502, 503, and 504

                      * **client-error** – HTTP status code 409

                      * **stream-error** – Retry on refused stream

                      - *(string) --*

                    - **maxRetries** *(integer) --*

                      The maximum number of retry attempts.

                    - **perRetryTimeout** *(dict) --*

                      An object that represents a duration of time.

                      - **unit** *(string) --*

                        A unit of time.

                      - **value** *(integer) --*

                        A number of time units.

                    - **tcpRetryEvents** *(list) --*

                      Specify a valid value.

                      - *(string) --*

                - **httpRoute** *(dict) --*

                  An object that represents the specification of an HTTP route.

                  - **action** *(dict) --*

                    An object that represents the action to take if a match is determined.

                    - **weightedTargets** *(list) --*

                      An object that represents the targets that traffic is routed to when a request
                      matches the route.

                      - *(dict) --*

                        An object that represents a target and its relative weight. Traffic is distributed
                        across targets according to their relative weight. For example, a weighted target
                        with a relative weight of 50 receives five times as much traffic as one with a
                        relative weight of 10. The total weight for all targets combined must be less than
                        or equal to 100.

                        - **virtualNode** *(string) --*

                          The virtual node to associate with the weighted target.

                        - **weight** *(integer) --*

                          The relative weight of the weighted target.

                  - **match** *(dict) --*

                    An object that represents the criteria for determining a request match.

                    - **headers** *(list) --*

                      An object that represents the client request headers to match on.

                      - *(dict) --*

                        An object that represents the HTTP header in the request.

                        - **invert** *(boolean) --*

                          Specify ``True`` to match anything except the match criteria. The default value
                          is ``False`` .

                        - **match** *(dict) --*

                          The ``HeaderMatchMethod`` object.

                          - **exact** *(string) --*

                            The value sent by the client must match the specified value exactly.

                          - **prefix** *(string) --*

                            The value sent by the client must begin with the specified characters.

                          - **range** *(dict) --*

                            An object that represents the range of values to match on.

                            - **end** *(integer) --*

                              The end of the range.

                            - **start** *(integer) --*

                              The start of the range.

                          - **regex** *(string) --*

                            The value sent by the client must include the specified characters.

                          - **suffix** *(string) --*

                            The value sent by the client must end with the specified characters.

                        - **name** *(string) --*

                          A name for the HTTP header in the client request that will be matched on.

                    - **method** *(string) --*

                      The client request method to match on. Specify only one.

                    - **prefix** *(string) --*

                      Specifies the path to match requests with. This parameter must always start with
                      ``/`` , which by itself matches all requests to the virtual service name. You can
                      also match for path-based routing of requests. For example, if your virtual service
                      name is ``my-service.local`` and you want the route to match requests to
                      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

                    - **scheme** *(string) --*

                      The client request scheme to match on. Specify only one.

                  - **retryPolicy** *(dict) --*

                    An object that represents a retry policy.

                    - **httpRetryEvents** *(list) --*

                      Specify at least one of the following values.

                      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
                      510, and 511

                      * **gateway-error** – HTTP status codes 502, 503, and 504

                      * **client-error** – HTTP status code 409

                      * **stream-error** – Retry on refused stream

                      - *(string) --*

                    - **maxRetries** *(integer) --*

                      The maximum number of retry attempts.

                    - **perRetryTimeout** *(dict) --*

                      An object that represents a duration of time.

                      - **unit** *(string) --*

                        A unit of time.

                      - **value** *(integer) --*

                        A number of time units.

                    - **tcpRetryEvents** *(list) --*

                      Specify a valid value.

                      - *(string) --*

                - **priority** *(integer) --*

                  The priority for the route. Routes are matched based on the specified value, where 0 is
                  the highest priority.

                - **tcpRoute** *(dict) --*

                  An object that represents the specification of a TCP route.

                  - **action** *(dict) --*

                    The action to take if a match is determined.

                    - **weightedTargets** *(list) --*

                      An object that represents the targets that traffic is routed to when a request
                      matches the route.

                      - *(dict) --*

                        An object that represents a target and its relative weight. Traffic is distributed
                        across targets according to their relative weight. For example, a weighted target
                        with a relative weight of 50 receives five times as much traffic as one with a
                        relative weight of 10. The total weight for all targets combined must be less than
                        or equal to 100.

                        - **virtualNode** *(string) --*

                          The virtual node to associate with the weighted target.

                        - **weight** *(integer) --*

                          The relative weight of the weighted target.

              - **status** *(dict) --*

                The status of the route.

                - **status** *(string) --*

                  The current status for the route.

              - **virtualRouterName** *(string) --*

                The virtual router that the route is associated with.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_virtual_node(
        self, meshName: str, virtualNodeName: str
    ) -> ClientDeleteVirtualNodeResponseTypeDef:
        """
        Deletes an existing virtual node.

        You must delete any virtual services that list a virtual node as a service provider before you can
        delete the virtual node itself.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/DeleteVirtualNode>`_

        **Request Syntax**
        ::

          response = client.delete_virtual_node(
              meshName='string',
              virtualNodeName='string'
          )
        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh to delete the virtual node in.

        :type virtualNodeName: string
        :param virtualNodeName: **[REQUIRED]**

          The name of the virtual node to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'virtualNode': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'backends': [
                            {
                                'virtualService': {
                                    'virtualServiceName': 'string'
                                }
                            },
                        ],
                        'listeners': [
                            {
                                'healthCheck': {
                                    'healthyThreshold': 123,
                                    'intervalMillis': 123,
                                    'path': 'string',
                                    'port': 123,
                                    'protocol': 'grpc'|'http'|'http2'|'tcp',
                                    'timeoutMillis': 123,
                                    'unhealthyThreshold': 123
                                },
                                'portMapping': {
                                    'port': 123,
                                    'protocol': 'grpc'|'http'|'http2'|'tcp'
                                }
                            },
                        ],
                        'logging': {
                            'accessLog': {
                                'file': {
                                    'path': 'string'
                                }
                            }
                        },
                        'serviceDiscovery': {
                            'awsCloudMap': {
                                'attributes': [
                                    {
                                        'key': 'string',
                                        'value': 'string'
                                    },
                                ],
                                'namespaceName': 'string',
                                'serviceName': 'string'
                            },
                            'dns': {
                                'hostname': 'string'
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualNodeName': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **virtualNode** *(dict) --*

              The virtual node that was deleted.

              - **meshName** *(string) --*

                The name of the service mesh that the virtual node resides in.

              - **metadata** *(dict) --*

                The associated metadata for the virtual node.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **spec** *(dict) --*

                The specifications of the virtual node.

                - **backends** *(list) --*

                  The backends that the virtual node is expected to send outbound traffic to.

                  - *(dict) --*

                    An object that represents the backends that a virtual node is expected to send outbound
                    traffic to.

                    - **virtualService** *(dict) --*

                      Specifies a virtual service to use as a backend for a virtual node.

                      - **virtualServiceName** *(string) --*

                        The name of the virtual service that is acting as a virtual node backend.

                - **listeners** *(list) --*

                  The listeners that the virtual node is expected to receive inbound traffic from. You can
                  specify one listener.

                  - *(dict) --*

                    An object that represents a listener for a virtual node.

                    - **healthCheck** *(dict) --*

                      The health check information for the listener.

                      - **healthyThreshold** *(integer) --*

                        The number of consecutive successful health checks that must occur before declaring
                        listener healthy.

                      - **intervalMillis** *(integer) --*

                        The time period in milliseconds between each health check execution.

                      - **path** *(string) --*

                        The destination path for the health check request. This is required only if the
                        specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

                      - **port** *(integer) --*

                        The destination port for the health check request. This port must match the port
                        defined in the  PortMapping for the listener.

                      - **protocol** *(string) --*

                        The protocol for the health check request.

                      - **timeoutMillis** *(integer) --*

                        The amount of time to wait when receiving a response from the health check, in
                        milliseconds.

                      - **unhealthyThreshold** *(integer) --*

                        The number of consecutive failed health checks that must occur before declaring a
                        virtual node unhealthy.

                    - **portMapping** *(dict) --*

                      The port mapping information for the listener.

                      - **port** *(integer) --*

                        The port used for the port mapping.

                      - **protocol** *(string) --*

                        The protocol used for the port mapping. Specify one protocol.

                - **logging** *(dict) --*

                  The inbound and outbound access logging information for the virtual node.

                  - **accessLog** *(dict) --*

                    The access log configuration for a virtual node.

                    - **file** *(dict) --*

                      The file object to send virtual node access logs to.

                      - **path** *(string) --*

                        The file path to write access logs to. You can use ``/dev/stdout`` to send access
                        logs to standard out and configure your Envoy container to use a log driver, such
                        as ``awslogs`` , to export the access logs to a log storage service such as Amazon
                        CloudWatch Logs. You can also specify a path in the Envoy container's file system
                        to write the files to disk.

                        .. note::

                          The Envoy process must have write permissions to the path that you specify here.
                          Otherwise, Envoy fails to bootstrap properly.

                - **serviceDiscovery** *(dict) --*

                  The service discovery information for the virtual node. If your virtual node does not
                  expect ingress traffic, you can omit this parameter.

                  - **awsCloudMap** *(dict) --*

                    Specifies any AWS Cloud Map information for the virtual node.

                    - **attributes** *(list) --*

                      A string map that contains attributes with values that you can use to filter
                      instances by any custom attribute that you specified when you registered the
                      instance. Only instances that match all of the specified key/value pairs will be
                      returned.

                      - *(dict) --*

                        An object that represents the AWS Cloud Map attribute information for your virtual
                        node.

                        - **key** *(string) --*

                          The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                          service instance that contains the specified key and value is returned.

                        - **value** *(string) --*

                          The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                          service instance that contains the specified key and value is returned.

                    - **namespaceName** *(string) --*

                      The name of the AWS Cloud Map namespace to use.

                    - **serviceName** *(string) --*

                      The name of the AWS Cloud Map service to use.

                  - **dns** *(dict) --*

                    Specifies the DNS information for the virtual node.

                    - **hostname** *(string) --*

                      Specifies the DNS service discovery hostname for the virtual node.

              - **status** *(dict) --*

                The current status for the virtual node.

                - **status** *(string) --*

                  The current status of the virtual node.

              - **virtualNodeName** *(string) --*

                The name of the virtual node.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_virtual_router(
        self, meshName: str, virtualRouterName: str
    ) -> ClientDeleteVirtualRouterResponseTypeDef:
        """
        Deletes an existing virtual router.

        You must delete any routes associated with the virtual router before you can delete the router
        itself.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/DeleteVirtualRouter>`_

        **Request Syntax**
        ::

          response = client.delete_virtual_router(
              meshName='string',
              virtualRouterName='string'
          )
        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh to delete the virtual router in.

        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**

          The name of the virtual router to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'virtualRouter': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'listeners': [
                            {
                                'portMapping': {
                                    'port': 123,
                                    'protocol': 'grpc'|'http'|'http2'|'tcp'
                                }
                            },
                        ]
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualRouterName': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **virtualRouter** *(dict) --*

              The virtual router that was deleted.

              - **meshName** *(string) --*

                The name of the service mesh that the virtual router resides in.

              - **metadata** *(dict) --*

                The associated metadata for the virtual router.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **spec** *(dict) --*

                The specifications of the virtual router.

                - **listeners** *(list) --*

                  The listeners that the virtual router is expected to receive inbound traffic from. You
                  can specify one listener.

                  - *(dict) --*

                    An object that represents a virtual router listener.

                    - **portMapping** *(dict) --*

                      An object that represents a port mapping.

                      - **port** *(integer) --*

                        The port used for the port mapping.

                      - **protocol** *(string) --*

                        The protocol used for the port mapping. Specify one protocol.

              - **status** *(dict) --*

                The current status of the virtual router.

                - **status** *(string) --*

                  The current status of the virtual router.

              - **virtualRouterName** *(string) --*

                The name of the virtual router.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_virtual_service(
        self, meshName: str, virtualServiceName: str
    ) -> ClientDeleteVirtualServiceResponseTypeDef:
        """
        Deletes an existing virtual service.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/DeleteVirtualService>`_

        **Request Syntax**
        ::

          response = client.delete_virtual_service(
              meshName='string',
              virtualServiceName='string'
          )
        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh to delete the virtual service in.

        :type virtualServiceName: string
        :param virtualServiceName: **[REQUIRED]**

          The name of the virtual service to delete.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'virtualService': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'provider': {
                            'virtualNode': {
                                'virtualNodeName': 'string'
                            },
                            'virtualRouter': {
                                'virtualRouterName': 'string'
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualServiceName': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **virtualService** *(dict) --*

              The virtual service that was deleted.

              - **meshName** *(string) --*

                The name of the service mesh that the virtual service resides in.

              - **metadata** *(dict) --*

                An object that represents metadata for a resource.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **spec** *(dict) --*

                The specifications of the virtual service.

                - **provider** *(dict) --*

                  The App Mesh object that is acting as the provider for a virtual service. You can specify
                  a single virtual node or virtual router.

                  - **virtualNode** *(dict) --*

                    The virtual node associated with a virtual service.

                    - **virtualNodeName** *(string) --*

                      The name of the virtual node that is acting as a service provider.

                  - **virtualRouter** *(dict) --*

                    The virtual router associated with a virtual service.

                    - **virtualRouterName** *(string) --*

                      The name of the virtual router that is acting as a service provider.

              - **status** *(dict) --*

                The current status of the virtual service.

                - **status** *(string) --*

                  The current status of the virtual service.

              - **virtualServiceName** *(string) --*

                The name of the virtual service.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_mesh(self, meshName: str) -> ClientDescribeMeshResponseTypeDef:
        """
        Describes an existing service mesh.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/DescribeMesh>`_

        **Request Syntax**
        ::

          response = client.describe_mesh(
              meshName='string'
          )
        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh to describe.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'mesh': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'egressFilter': {
                            'type': 'ALLOW_ALL'|'DROP_ALL'
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **mesh** *(dict) --*

              The full description of your service mesh.

              - **meshName** *(string) --*

                The name of the service mesh.

              - **metadata** *(dict) --*

                The associated metadata for the service mesh.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **spec** *(dict) --*

                The associated specification for the service mesh.

                - **egressFilter** *(dict) --*

                  The egress filter rules for the service mesh.

                  - **type** *(string) --*

                    The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
                    from virtual nodes to other defined resources in the service mesh (and any traffic to
                    ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
                    ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.

              - **status** *(dict) --*

                The status of the service mesh.

                - **status** *(string) --*

                  The current mesh status.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_route(
        self, meshName: str, routeName: str, virtualRouterName: str
    ) -> ClientDescribeRouteResponseTypeDef:
        """
        Describes an existing route.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/DescribeRoute>`_

        **Request Syntax**
        ::

          response = client.describe_route(
              meshName='string',
              routeName='string',
              virtualRouterName='string'
          )
        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh that the route resides in.

        :type routeName: string
        :param routeName: **[REQUIRED]**

          The name of the route to describe.

        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**

          The name of the virtual router that the route is associated with.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'route': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'routeName': 'string',
                    'spec': {
                        'grpcRoute': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            },
                            'match': {
                                'metadata': [
                                    {
                                        'invert': True|False,
                                        'match': {
                                            'exact': 'string',
                                            'prefix': 'string',
                                            'range': {
                                                'end': 123,
                                                'start': 123
                                            },
                                            'regex': 'string',
                                            'suffix': 'string'
                                        },
                                        'name': 'string'
                                    },
                                ],
                                'methodName': 'string',
                                'serviceName': 'string'
                            },
                            'retryPolicy': {
                                'grpcRetryEvents': [
                                    'cancelled'|'deadline-exceeded'|'internal'|'resource-exhausted'
                                    |'unavailable',
                                ],
                                'httpRetryEvents': [
                                    'string',
                                ],
                                'maxRetries': 123,
                                'perRetryTimeout': {
                                    'unit': 'ms'|'s',
                                    'value': 123
                                },
                                'tcpRetryEvents': [
                                    'connection-error',
                                ]
                            }
                        },
                        'http2Route': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            },
                            'match': {
                                'headers': [
                                    {
                                        'invert': True|False,
                                        'match': {
                                            'exact': 'string',
                                            'prefix': 'string',
                                            'range': {
                                                'end': 123,
                                                'start': 123
                                            },
                                            'regex': 'string',
                                            'suffix': 'string'
                                        },
                                        'name': 'string'
                                    },
                                ],
                                'method':
                                'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                                'prefix': 'string',
                                'scheme': 'http'|'https'
                            },
                            'retryPolicy': {
                                'httpRetryEvents': [
                                    'string',
                                ],
                                'maxRetries': 123,
                                'perRetryTimeout': {
                                    'unit': 'ms'|'s',
                                    'value': 123
                                },
                                'tcpRetryEvents': [
                                    'connection-error',
                                ]
                            }
                        },
                        'httpRoute': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            },
                            'match': {
                                'headers': [
                                    {
                                        'invert': True|False,
                                        'match': {
                                            'exact': 'string',
                                            'prefix': 'string',
                                            'range': {
                                                'end': 123,
                                                'start': 123
                                            },
                                            'regex': 'string',
                                            'suffix': 'string'
                                        },
                                        'name': 'string'
                                    },
                                ],
                                'method':
                                'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                                'prefix': 'string',
                                'scheme': 'http'|'https'
                            },
                            'retryPolicy': {
                                'httpRetryEvents': [
                                    'string',
                                ],
                                'maxRetries': 123,
                                'perRetryTimeout': {
                                    'unit': 'ms'|'s',
                                    'value': 123
                                },
                                'tcpRetryEvents': [
                                    'connection-error',
                                ]
                            }
                        },
                        'priority': 123,
                        'tcpRoute': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualRouterName': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **route** *(dict) --*

              The full description of your route.

              - **meshName** *(string) --*

                The name of the service mesh that the route resides in.

              - **metadata** *(dict) --*

                The associated metadata for the route.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **routeName** *(string) --*

                The name of the route.

              - **spec** *(dict) --*

                The specifications of the route.

                - **grpcRoute** *(dict) --*

                  An object that represents the specification of a GRPC route.

                  - **action** *(dict) --*

                    An object that represents the action to take if a match is determined.

                    - **weightedTargets** *(list) --*

                      An object that represents the targets that traffic is routed to when a request
                      matches the route.

                      - *(dict) --*

                        An object that represents a target and its relative weight. Traffic is distributed
                        across targets according to their relative weight. For example, a weighted target
                        with a relative weight of 50 receives five times as much traffic as one with a
                        relative weight of 10. The total weight for all targets combined must be less than
                        or equal to 100.

                        - **virtualNode** *(string) --*

                          The virtual node to associate with the weighted target.

                        - **weight** *(integer) --*

                          The relative weight of the weighted target.

                  - **match** *(dict) --*

                    An object that represents the criteria for determining a request match.

                    - **metadata** *(list) --*

                      An object that represents the data to match from the request.

                      - *(dict) --*

                        An object that represents the match metadata for the route.

                        - **invert** *(boolean) --*

                          Specify ``True`` to match anything except the match criteria. The default value
                          is ``False`` .

                        - **match** *(dict) --*

                          An object that represents the data to match from the request.

                          - **exact** *(string) --*

                            The value sent by the client must match the specified value exactly.

                          - **prefix** *(string) --*

                            The value sent by the client must begin with the specified characters.

                          - **range** *(dict) --*

                            An object that represents the range of values to match on.

                            - **end** *(integer) --*

                              The end of the range.

                            - **start** *(integer) --*

                              The start of the range.

                          - **regex** *(string) --*

                            The value sent by the client must include the specified characters.

                          - **suffix** *(string) --*

                            The value sent by the client must end with the specified characters.

                        - **name** *(string) --*

                          The name of the route.

                    - **methodName** *(string) --*

                      The method name to match from the request. If you specify a name, you must also
                      specify a ``serviceName`` .

                    - **serviceName** *(string) --*

                      The fully qualified domain name for the service to match from the request.

                  - **retryPolicy** *(dict) --*

                    An object that represents a retry policy.

                    - **grpcRetryEvents** *(list) --*

                      Specify at least one of the valid values.

                      - *(string) --*

                    - **httpRetryEvents** *(list) --*

                      Specify at least one of the following values.

                      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
                      510, and 511

                      * **gateway-error** – HTTP status codes 502, 503, and 504

                      * **client-error** – HTTP status code 409

                      * **stream-error** – Retry on refused stream

                      - *(string) --*

                    - **maxRetries** *(integer) --*

                      The maximum number of retry attempts.

                    - **perRetryTimeout** *(dict) --*

                      An object that represents a duration of time.

                      - **unit** *(string) --*

                        A unit of time.

                      - **value** *(integer) --*

                        A number of time units.

                    - **tcpRetryEvents** *(list) --*

                      Specify a valid value.

                      - *(string) --*

                - **http2Route** *(dict) --*

                  An object that represents the specification of an HTTP2 route.

                  - **action** *(dict) --*

                    An object that represents the action to take if a match is determined.

                    - **weightedTargets** *(list) --*

                      An object that represents the targets that traffic is routed to when a request
                      matches the route.

                      - *(dict) --*

                        An object that represents a target and its relative weight. Traffic is distributed
                        across targets according to their relative weight. For example, a weighted target
                        with a relative weight of 50 receives five times as much traffic as one with a
                        relative weight of 10. The total weight for all targets combined must be less than
                        or equal to 100.

                        - **virtualNode** *(string) --*

                          The virtual node to associate with the weighted target.

                        - **weight** *(integer) --*

                          The relative weight of the weighted target.

                  - **match** *(dict) --*

                    An object that represents the criteria for determining a request match.

                    - **headers** *(list) --*

                      An object that represents the client request headers to match on.

                      - *(dict) --*

                        An object that represents the HTTP header in the request.

                        - **invert** *(boolean) --*

                          Specify ``True`` to match anything except the match criteria. The default value
                          is ``False`` .

                        - **match** *(dict) --*

                          The ``HeaderMatchMethod`` object.

                          - **exact** *(string) --*

                            The value sent by the client must match the specified value exactly.

                          - **prefix** *(string) --*

                            The value sent by the client must begin with the specified characters.

                          - **range** *(dict) --*

                            An object that represents the range of values to match on.

                            - **end** *(integer) --*

                              The end of the range.

                            - **start** *(integer) --*

                              The start of the range.

                          - **regex** *(string) --*

                            The value sent by the client must include the specified characters.

                          - **suffix** *(string) --*

                            The value sent by the client must end with the specified characters.

                        - **name** *(string) --*

                          A name for the HTTP header in the client request that will be matched on.

                    - **method** *(string) --*

                      The client request method to match on. Specify only one.

                    - **prefix** *(string) --*

                      Specifies the path to match requests with. This parameter must always start with
                      ``/`` , which by itself matches all requests to the virtual service name. You can
                      also match for path-based routing of requests. For example, if your virtual service
                      name is ``my-service.local`` and you want the route to match requests to
                      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

                    - **scheme** *(string) --*

                      The client request scheme to match on. Specify only one.

                  - **retryPolicy** *(dict) --*

                    An object that represents a retry policy.

                    - **httpRetryEvents** *(list) --*

                      Specify at least one of the following values.

                      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
                      510, and 511

                      * **gateway-error** – HTTP status codes 502, 503, and 504

                      * **client-error** – HTTP status code 409

                      * **stream-error** – Retry on refused stream

                      - *(string) --*

                    - **maxRetries** *(integer) --*

                      The maximum number of retry attempts.

                    - **perRetryTimeout** *(dict) --*

                      An object that represents a duration of time.

                      - **unit** *(string) --*

                        A unit of time.

                      - **value** *(integer) --*

                        A number of time units.

                    - **tcpRetryEvents** *(list) --*

                      Specify a valid value.

                      - *(string) --*

                - **httpRoute** *(dict) --*

                  An object that represents the specification of an HTTP route.

                  - **action** *(dict) --*

                    An object that represents the action to take if a match is determined.

                    - **weightedTargets** *(list) --*

                      An object that represents the targets that traffic is routed to when a request
                      matches the route.

                      - *(dict) --*

                        An object that represents a target and its relative weight. Traffic is distributed
                        across targets according to their relative weight. For example, a weighted target
                        with a relative weight of 50 receives five times as much traffic as one with a
                        relative weight of 10. The total weight for all targets combined must be less than
                        or equal to 100.

                        - **virtualNode** *(string) --*

                          The virtual node to associate with the weighted target.

                        - **weight** *(integer) --*

                          The relative weight of the weighted target.

                  - **match** *(dict) --*

                    An object that represents the criteria for determining a request match.

                    - **headers** *(list) --*

                      An object that represents the client request headers to match on.

                      - *(dict) --*

                        An object that represents the HTTP header in the request.

                        - **invert** *(boolean) --*

                          Specify ``True`` to match anything except the match criteria. The default value
                          is ``False`` .

                        - **match** *(dict) --*

                          The ``HeaderMatchMethod`` object.

                          - **exact** *(string) --*

                            The value sent by the client must match the specified value exactly.

                          - **prefix** *(string) --*

                            The value sent by the client must begin with the specified characters.

                          - **range** *(dict) --*

                            An object that represents the range of values to match on.

                            - **end** *(integer) --*

                              The end of the range.

                            - **start** *(integer) --*

                              The start of the range.

                          - **regex** *(string) --*

                            The value sent by the client must include the specified characters.

                          - **suffix** *(string) --*

                            The value sent by the client must end with the specified characters.

                        - **name** *(string) --*

                          A name for the HTTP header in the client request that will be matched on.

                    - **method** *(string) --*

                      The client request method to match on. Specify only one.

                    - **prefix** *(string) --*

                      Specifies the path to match requests with. This parameter must always start with
                      ``/`` , which by itself matches all requests to the virtual service name. You can
                      also match for path-based routing of requests. For example, if your virtual service
                      name is ``my-service.local`` and you want the route to match requests to
                      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

                    - **scheme** *(string) --*

                      The client request scheme to match on. Specify only one.

                  - **retryPolicy** *(dict) --*

                    An object that represents a retry policy.

                    - **httpRetryEvents** *(list) --*

                      Specify at least one of the following values.

                      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
                      510, and 511

                      * **gateway-error** – HTTP status codes 502, 503, and 504

                      * **client-error** – HTTP status code 409

                      * **stream-error** – Retry on refused stream

                      - *(string) --*

                    - **maxRetries** *(integer) --*

                      The maximum number of retry attempts.

                    - **perRetryTimeout** *(dict) --*

                      An object that represents a duration of time.

                      - **unit** *(string) --*

                        A unit of time.

                      - **value** *(integer) --*

                        A number of time units.

                    - **tcpRetryEvents** *(list) --*

                      Specify a valid value.

                      - *(string) --*

                - **priority** *(integer) --*

                  The priority for the route. Routes are matched based on the specified value, where 0 is
                  the highest priority.

                - **tcpRoute** *(dict) --*

                  An object that represents the specification of a TCP route.

                  - **action** *(dict) --*

                    The action to take if a match is determined.

                    - **weightedTargets** *(list) --*

                      An object that represents the targets that traffic is routed to when a request
                      matches the route.

                      - *(dict) --*

                        An object that represents a target and its relative weight. Traffic is distributed
                        across targets according to their relative weight. For example, a weighted target
                        with a relative weight of 50 receives five times as much traffic as one with a
                        relative weight of 10. The total weight for all targets combined must be less than
                        or equal to 100.

                        - **virtualNode** *(string) --*

                          The virtual node to associate with the weighted target.

                        - **weight** *(integer) --*

                          The relative weight of the weighted target.

              - **status** *(dict) --*

                The status of the route.

                - **status** *(string) --*

                  The current status for the route.

              - **virtualRouterName** *(string) --*

                The virtual router that the route is associated with.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_virtual_node(
        self, meshName: str, virtualNodeName: str
    ) -> ClientDescribeVirtualNodeResponseTypeDef:
        """
        Describes an existing virtual node.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/DescribeVirtualNode>`_

        **Request Syntax**
        ::

          response = client.describe_virtual_node(
              meshName='string',
              virtualNodeName='string'
          )
        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh that the virtual node resides in.

        :type virtualNodeName: string
        :param virtualNodeName: **[REQUIRED]**

          The name of the virtual node to describe.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'virtualNode': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'backends': [
                            {
                                'virtualService': {
                                    'virtualServiceName': 'string'
                                }
                            },
                        ],
                        'listeners': [
                            {
                                'healthCheck': {
                                    'healthyThreshold': 123,
                                    'intervalMillis': 123,
                                    'path': 'string',
                                    'port': 123,
                                    'protocol': 'grpc'|'http'|'http2'|'tcp',
                                    'timeoutMillis': 123,
                                    'unhealthyThreshold': 123
                                },
                                'portMapping': {
                                    'port': 123,
                                    'protocol': 'grpc'|'http'|'http2'|'tcp'
                                }
                            },
                        ],
                        'logging': {
                            'accessLog': {
                                'file': {
                                    'path': 'string'
                                }
                            }
                        },
                        'serviceDiscovery': {
                            'awsCloudMap': {
                                'attributes': [
                                    {
                                        'key': 'string',
                                        'value': 'string'
                                    },
                                ],
                                'namespaceName': 'string',
                                'serviceName': 'string'
                            },
                            'dns': {
                                'hostname': 'string'
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualNodeName': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **virtualNode** *(dict) --*

              The full description of your virtual node.

              - **meshName** *(string) --*

                The name of the service mesh that the virtual node resides in.

              - **metadata** *(dict) --*

                The associated metadata for the virtual node.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **spec** *(dict) --*

                The specifications of the virtual node.

                - **backends** *(list) --*

                  The backends that the virtual node is expected to send outbound traffic to.

                  - *(dict) --*

                    An object that represents the backends that a virtual node is expected to send outbound
                    traffic to.

                    - **virtualService** *(dict) --*

                      Specifies a virtual service to use as a backend for a virtual node.

                      - **virtualServiceName** *(string) --*

                        The name of the virtual service that is acting as a virtual node backend.

                - **listeners** *(list) --*

                  The listeners that the virtual node is expected to receive inbound traffic from. You can
                  specify one listener.

                  - *(dict) --*

                    An object that represents a listener for a virtual node.

                    - **healthCheck** *(dict) --*

                      The health check information for the listener.

                      - **healthyThreshold** *(integer) --*

                        The number of consecutive successful health checks that must occur before declaring
                        listener healthy.

                      - **intervalMillis** *(integer) --*

                        The time period in milliseconds between each health check execution.

                      - **path** *(string) --*

                        The destination path for the health check request. This is required only if the
                        specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

                      - **port** *(integer) --*

                        The destination port for the health check request. This port must match the port
                        defined in the  PortMapping for the listener.

                      - **protocol** *(string) --*

                        The protocol for the health check request.

                      - **timeoutMillis** *(integer) --*

                        The amount of time to wait when receiving a response from the health check, in
                        milliseconds.

                      - **unhealthyThreshold** *(integer) --*

                        The number of consecutive failed health checks that must occur before declaring a
                        virtual node unhealthy.

                    - **portMapping** *(dict) --*

                      The port mapping information for the listener.

                      - **port** *(integer) --*

                        The port used for the port mapping.

                      - **protocol** *(string) --*

                        The protocol used for the port mapping. Specify one protocol.

                - **logging** *(dict) --*

                  The inbound and outbound access logging information for the virtual node.

                  - **accessLog** *(dict) --*

                    The access log configuration for a virtual node.

                    - **file** *(dict) --*

                      The file object to send virtual node access logs to.

                      - **path** *(string) --*

                        The file path to write access logs to. You can use ``/dev/stdout`` to send access
                        logs to standard out and configure your Envoy container to use a log driver, such
                        as ``awslogs`` , to export the access logs to a log storage service such as Amazon
                        CloudWatch Logs. You can also specify a path in the Envoy container's file system
                        to write the files to disk.

                        .. note::

                          The Envoy process must have write permissions to the path that you specify here.
                          Otherwise, Envoy fails to bootstrap properly.

                - **serviceDiscovery** *(dict) --*

                  The service discovery information for the virtual node. If your virtual node does not
                  expect ingress traffic, you can omit this parameter.

                  - **awsCloudMap** *(dict) --*

                    Specifies any AWS Cloud Map information for the virtual node.

                    - **attributes** *(list) --*

                      A string map that contains attributes with values that you can use to filter
                      instances by any custom attribute that you specified when you registered the
                      instance. Only instances that match all of the specified key/value pairs will be
                      returned.

                      - *(dict) --*

                        An object that represents the AWS Cloud Map attribute information for your virtual
                        node.

                        - **key** *(string) --*

                          The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                          service instance that contains the specified key and value is returned.

                        - **value** *(string) --*

                          The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                          service instance that contains the specified key and value is returned.

                    - **namespaceName** *(string) --*

                      The name of the AWS Cloud Map namespace to use.

                    - **serviceName** *(string) --*

                      The name of the AWS Cloud Map service to use.

                  - **dns** *(dict) --*

                    Specifies the DNS information for the virtual node.

                    - **hostname** *(string) --*

                      Specifies the DNS service discovery hostname for the virtual node.

              - **status** *(dict) --*

                The current status for the virtual node.

                - **status** *(string) --*

                  The current status of the virtual node.

              - **virtualNodeName** *(string) --*

                The name of the virtual node.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_virtual_router(
        self, meshName: str, virtualRouterName: str
    ) -> ClientDescribeVirtualRouterResponseTypeDef:
        """
        Describes an existing virtual router.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/DescribeVirtualRouter>`_

        **Request Syntax**
        ::

          response = client.describe_virtual_router(
              meshName='string',
              virtualRouterName='string'
          )
        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh that the virtual router resides in.

        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**

          The name of the virtual router to describe.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'virtualRouter': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'listeners': [
                            {
                                'portMapping': {
                                    'port': 123,
                                    'protocol': 'grpc'|'http'|'http2'|'tcp'
                                }
                            },
                        ]
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualRouterName': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **virtualRouter** *(dict) --*

              The full description of your virtual router.

              - **meshName** *(string) --*

                The name of the service mesh that the virtual router resides in.

              - **metadata** *(dict) --*

                The associated metadata for the virtual router.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **spec** *(dict) --*

                The specifications of the virtual router.

                - **listeners** *(list) --*

                  The listeners that the virtual router is expected to receive inbound traffic from. You
                  can specify one listener.

                  - *(dict) --*

                    An object that represents a virtual router listener.

                    - **portMapping** *(dict) --*

                      An object that represents a port mapping.

                      - **port** *(integer) --*

                        The port used for the port mapping.

                      - **protocol** *(string) --*

                        The protocol used for the port mapping. Specify one protocol.

              - **status** *(dict) --*

                The current status of the virtual router.

                - **status** *(string) --*

                  The current status of the virtual router.

              - **virtualRouterName** *(string) --*

                The name of the virtual router.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_virtual_service(
        self, meshName: str, virtualServiceName: str
    ) -> ClientDescribeVirtualServiceResponseTypeDef:
        """
        Describes an existing virtual service.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/DescribeVirtualService>`_

        **Request Syntax**
        ::

          response = client.describe_virtual_service(
              meshName='string',
              virtualServiceName='string'
          )
        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh that the virtual service resides in.

        :type virtualServiceName: string
        :param virtualServiceName: **[REQUIRED]**

          The name of the virtual service to describe.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'virtualService': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'provider': {
                            'virtualNode': {
                                'virtualNodeName': 'string'
                            },
                            'virtualRouter': {
                                'virtualRouterName': 'string'
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualServiceName': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **virtualService** *(dict) --*

              The full description of your virtual service.

              - **meshName** *(string) --*

                The name of the service mesh that the virtual service resides in.

              - **metadata** *(dict) --*

                An object that represents metadata for a resource.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **spec** *(dict) --*

                The specifications of the virtual service.

                - **provider** *(dict) --*

                  The App Mesh object that is acting as the provider for a virtual service. You can specify
                  a single virtual node or virtual router.

                  - **virtualNode** *(dict) --*

                    The virtual node associated with a virtual service.

                    - **virtualNodeName** *(string) --*

                      The name of the virtual node that is acting as a service provider.

                  - **virtualRouter** *(dict) --*

                    The virtual router associated with a virtual service.

                    - **virtualRouterName** *(string) --*

                      The name of the virtual router that is acting as a service provider.

              - **status** *(dict) --*

                The current status of the virtual service.

                - **status** *(string) --*

                  The current status of the virtual service.

              - **virtualServiceName** *(string) --*

                The name of the virtual service.

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
    def list_meshes(
        self, limit: int = None, nextToken: str = None
    ) -> ClientListMeshesResponseTypeDef:
        """
        Returns a list of existing service meshes.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/ListMeshes>`_

        **Request Syntax**
        ::

          response = client.list_meshes(
              limit=123,
              nextToken='string'
          )
        :type limit: integer
        :param limit:

          The maximum number of results returned by ``ListMeshes`` in paginated output. When you use this
          parameter, ``ListMeshes`` returns only ``limit`` results in a single page along with a
          ``nextToken`` response element. You can see the remaining results of the initial request by
          sending another ``ListMeshes`` request with the returned ``nextToken`` value. This value can be
          between 1 and 100. If you don't use this parameter, ``ListMeshes`` returns up to 100 results and
          a ``nextToken`` value if applicable.

        :type nextToken: string
        :param nextToken:

          The ``nextToken`` value returned from a previous paginated ``ListMeshes`` request where ``limit``
          was used and the results exceeded the value of that parameter. Pagination continues from the end
          of the previous results that returned the ``nextToken`` value.

          .. note::

            This token should be treated as an opaque identifier that is used only to retrieve the next
            items in a list and not for other programmatic purposes.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'meshes': [
                    {
                        'arn': 'string',
                        'meshName': 'string'
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **meshes** *(list) --*

              The list of existing service meshes.

              - *(dict) --*

                An object that represents a service mesh returned by a list operation.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) of the service mesh.

                - **meshName** *(string) --*

                  The name of the service mesh.

            - **nextToken** *(string) --*

              The ``nextToken`` value to include in a future ``ListMeshes`` request. When the results of a
              ``ListMeshes`` request exceed ``limit`` , you can use this value to retrieve the next page of
              results. This value is ``null`` when there are no more results to return.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_routes(
        self,
        meshName: str,
        virtualRouterName: str,
        limit: int = None,
        nextToken: str = None,
    ) -> ClientListRoutesResponseTypeDef:
        """
        Returns a list of existing routes in a service mesh.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/ListRoutes>`_

        **Request Syntax**
        ::

          response = client.list_routes(
              limit=123,
              meshName='string',
              nextToken='string',
              virtualRouterName='string'
          )
        :type limit: integer
        :param limit:

          The maximum number of results returned by ``ListRoutes`` in paginated output. When you use this
          parameter, ``ListRoutes`` returns only ``limit`` results in a single page along with a
          ``nextToken`` response element. You can see the remaining results of the initial request by
          sending another ``ListRoutes`` request with the returned ``nextToken`` value. This value can be
          between 1 and 100. If you don't use this parameter, ``ListRoutes`` returns up to 100 results and
          a ``nextToken`` value if applicable.

        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh to list routes in.

        :type nextToken: string
        :param nextToken:

          The ``nextToken`` value returned from a previous paginated ``ListRoutes`` request where ``limit``
          was used and the results exceeded the value of that parameter. Pagination continues from the end
          of the previous results that returned the ``nextToken`` value.

        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**

          The name of the virtual router to list routes in.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'nextToken': 'string',
                'routes': [
                    {
                        'arn': 'string',
                        'meshName': 'string',
                        'routeName': 'string',
                        'virtualRouterName': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **nextToken** *(string) --*

              The ``nextToken`` value to include in a future ``ListRoutes`` request. When the results of a
              ``ListRoutes`` request exceed ``limit`` , you can use this value to retrieve the next page of
              results. This value is ``null`` when there are no more results to return.

            - **routes** *(list) --*

              The list of existing routes for the specified service mesh and virtual router.

              - *(dict) --*

                An object that represents a route returned by a list operation.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the route.

                - **meshName** *(string) --*

                  The name of the service mesh that the route resides in.

                - **routeName** *(string) --*

                  The name of the route.

                - **virtualRouterName** *(string) --*

                  The virtual router that the route is associated with.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, resourceArn: str, limit: int = None, nextToken: str = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        List the tags for an App Mesh resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              limit=123,
              nextToken='string',
              resourceArn='string'
          )
        :type limit: integer
        :param limit:

          The maximum number of tag results returned by ``ListTagsForResource`` in paginated output. When
          this parameter is used, ``ListTagsForResource`` returns only ``limit`` results in a single page
          along with a ``nextToken`` response element. You can see the remaining results of the initial
          request by sending another ``ListTagsForResource`` request with the returned ``nextToken`` value.
          This value can be between 1 and 100. If you don't use this parameter, ``ListTagsForResource``
          returns up to 100 results and a ``nextToken`` value if applicable.

        :type nextToken: string
        :param nextToken:

          The ``nextToken`` value returned from a previous paginated ``ListTagsForResource`` request where
          ``limit`` was used and the results exceeded the value of that parameter. Pagination continues
          from the end of the previous results that returned the ``nextToken`` value.

        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) that identifies the resource to list the tags for.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'nextToken': 'string',
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **nextToken** *(string) --*

              The ``nextToken`` value to include in a future ``ListTagsForResource`` request. When the
              results of a ``ListTagsForResource`` request exceed ``limit`` , you can use this value to
              retrieve the next page of results. This value is ``null`` when there are no more results to
              return.

            - **tags** *(list) --*

              The tags for the resource.

              - *(dict) --*

                Optional metadata that you apply to a resource to assist with categorization and
                organization. Each tag consists of a key and an optional value, both of which you define.
                Tag keys can have a maximum character length of 128 characters, and tag values can have a
                maximum length of 256 characters.

                - **key** *(string) --*

                  One part of a key-value pair that make up a tag. A ``key`` is a general label that acts
                  like a category for more specific tag values.

                - **value** *(string) --*

                  The optional part of a key-value pair that make up a tag. A ``value`` acts as a
                  descriptor within a tag category (key).

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_virtual_nodes(
        self, meshName: str, limit: int = None, nextToken: str = None
    ) -> ClientListVirtualNodesResponseTypeDef:
        """
        Returns a list of existing virtual nodes.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/ListVirtualNodes>`_

        **Request Syntax**
        ::

          response = client.list_virtual_nodes(
              limit=123,
              meshName='string',
              nextToken='string'
          )
        :type limit: integer
        :param limit:

          The maximum number of results returned by ``ListVirtualNodes`` in paginated output. When you use
          this parameter, ``ListVirtualNodes`` returns only ``limit`` results in a single page along with a
          ``nextToken`` response element. You can see the remaining results of the initial request by
          sending another ``ListVirtualNodes`` request with the returned ``nextToken`` value. This value
          can be between 1 and 100. If you don't use this parameter, ``ListVirtualNodes`` returns up to 100
          results and a ``nextToken`` value if applicable.

        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh to list virtual nodes in.

        :type nextToken: string
        :param nextToken:

          The ``nextToken`` value returned from a previous paginated ``ListVirtualNodes`` request where
          ``limit`` was used and the results exceeded the value of that parameter. Pagination continues
          from the end of the previous results that returned the ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'nextToken': 'string',
                'virtualNodes': [
                    {
                        'arn': 'string',
                        'meshName': 'string',
                        'virtualNodeName': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **nextToken** *(string) --*

              The ``nextToken`` value to include in a future ``ListVirtualNodes`` request. When the results
              of a ``ListVirtualNodes`` request exceed ``limit`` , you can use this value to retrieve the
              next page of results. This value is ``null`` when there are no more results to return.

            - **virtualNodes** *(list) --*

              The list of existing virtual nodes for the specified service mesh.

              - *(dict) --*

                An object that represents a virtual node returned by a list operation.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the virtual node.

                - **meshName** *(string) --*

                  The name of the service mesh that the virtual node resides in.

                - **virtualNodeName** *(string) --*

                  The name of the virtual node.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_virtual_routers(
        self, meshName: str, limit: int = None, nextToken: str = None
    ) -> ClientListVirtualRoutersResponseTypeDef:
        """
        Returns a list of existing virtual routers in a service mesh.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/ListVirtualRouters>`_

        **Request Syntax**
        ::

          response = client.list_virtual_routers(
              limit=123,
              meshName='string',
              nextToken='string'
          )
        :type limit: integer
        :param limit:

          The maximum number of results returned by ``ListVirtualRouters`` in paginated output. When you
          use this parameter, ``ListVirtualRouters`` returns only ``limit`` results in a single page along
          with a ``nextToken`` response element. You can see the remaining results of the initial request
          by sending another ``ListVirtualRouters`` request with the returned ``nextToken`` value. This
          value can be between 1 and 100. If you don't use this parameter, ``ListVirtualRouters`` returns
          up to 100 results and a ``nextToken`` value if applicable.

        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh to list virtual routers in.

        :type nextToken: string
        :param nextToken:

          The ``nextToken`` value returned from a previous paginated ``ListVirtualRouters`` request where
          ``limit`` was used and the results exceeded the value of that parameter. Pagination continues
          from the end of the previous results that returned the ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'nextToken': 'string',
                'virtualRouters': [
                    {
                        'arn': 'string',
                        'meshName': 'string',
                        'virtualRouterName': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **nextToken** *(string) --*

              The ``nextToken`` value to include in a future ``ListVirtualRouters`` request. When the
              results of a ``ListVirtualRouters`` request exceed ``limit`` , you can use this value to
              retrieve the next page of results. This value is ``null`` when there are no more results to
              return.

            - **virtualRouters** *(list) --*

              The list of existing virtual routers for the specified service mesh.

              - *(dict) --*

                An object that represents a virtual router returned by a list operation.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the virtual router.

                - **meshName** *(string) --*

                  The name of the service mesh that the virtual router resides in.

                - **virtualRouterName** *(string) --*

                  The name of the virtual router.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_virtual_services(
        self, meshName: str, limit: int = None, nextToken: str = None
    ) -> ClientListVirtualServicesResponseTypeDef:
        """
        Returns a list of existing virtual services in a service mesh.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/ListVirtualServices>`_

        **Request Syntax**
        ::

          response = client.list_virtual_services(
              limit=123,
              meshName='string',
              nextToken='string'
          )
        :type limit: integer
        :param limit:

          The maximum number of results returned by ``ListVirtualServices`` in paginated output. When you
          use this parameter, ``ListVirtualServices`` returns only ``limit`` results in a single page along
          with a ``nextToken`` response element. You can see the remaining results of the initial request
          by sending another ``ListVirtualServices`` request with the returned ``nextToken`` value. This
          value can be between 1 and 100. If you don't use this parameter, ``ListVirtualServices`` returns
          up to 100 results and a ``nextToken`` value if applicable.

        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh to list virtual services in.

        :type nextToken: string
        :param nextToken:

          The ``nextToken`` value returned from a previous paginated ``ListVirtualServices`` request where
          ``limit`` was used and the results exceeded the value of that parameter. Pagination continues
          from the end of the previous results that returned the ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'nextToken': 'string',
                'virtualServices': [
                    {
                        'arn': 'string',
                        'meshName': 'string',
                        'virtualServiceName': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **nextToken** *(string) --*

              The ``nextToken`` value to include in a future ``ListVirtualServices`` request. When the
              results of a ``ListVirtualServices`` request exceed ``limit`` , you can use this value to
              retrieve the next page of results. This value is ``null`` when there are no more results to
              return.

            - **virtualServices** *(list) --*

              The list of existing virtual services for the specified service mesh.

              - *(dict) --*

                An object that represents a virtual service returned by a list operation.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the virtual service.

                - **meshName** *(string) --*

                  The name of the service mesh that the virtual service resides in.

                - **virtualServiceName** *(string) --*

                  The name of the virtual service.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(
        self, resourceArn: str, tags: List[ClientTagResourcetagsTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates the specified tags to a resource with the specified ``resourceArn`` . If existing tags
        on a resource aren't specified in the request parameters, they aren't changed. When a resource is
        deleted, the tags associated with that resource are also deleted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              resourceArn='string',
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ]
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource to add tags to.

        :type tags: list
        :param tags: **[REQUIRED]**

          The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a
          maximum character length of 128 characters, and tag values can have a maximum length of 256
          characters.

          - *(dict) --*

            Optional metadata that you apply to a resource to assist with categorization and organization.
            Each tag consists of a key and an optional value, both of which you define. Tag keys can have a
            maximum character length of 128 characters, and tag values can have a maximum length of 256
            characters.

            - **key** *(string) --* **[REQUIRED]**

              One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like
              a category for more specific tag values.

            - **value** *(string) --*

              The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor
              within a tag category (key).

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes specified tags from a resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/UntagResource>`_

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

          The Amazon Resource Name (ARN) of the resource to delete tags from.

        :type tagKeys: list
        :param tagKeys: **[REQUIRED]**

          The keys of the tags to be removed.

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
    def update_mesh(
        self,
        meshName: str,
        clientToken: str = None,
        spec: ClientUpdateMeshspecTypeDef = None,
    ) -> ClientUpdateMeshResponseTypeDef:
        """
        Updates an existing service mesh.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/UpdateMesh>`_

        **Request Syntax**
        ::

          response = client.update_mesh(
              clientToken='string',
              meshName='string',
              spec={
                  'egressFilter': {
                      'type': 'ALLOW_ALL'|'DROP_ALL'
                  }
              }
          )
        :type clientToken: string
        :param clientToken:

          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up
          to 36 letters, numbers, hyphens, and underscores are allowed.

          This field is autopopulated if not provided.

        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh to update.

        :type spec: dict
        :param spec:

          The service mesh specification to apply.

          - **egressFilter** *(dict) --*

            The egress filter rules for the service mesh.

            - **type** *(string) --* **[REQUIRED]**

              The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only from
              virtual nodes to other defined resources in the service mesh (and any traffic to
              ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to ``ALLOW_ALL``
              to allow egress to any endpoint inside or outside of the service mesh.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'mesh': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'egressFilter': {
                            'type': 'ALLOW_ALL'|'DROP_ALL'
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **mesh** *(dict) --*

              An object that represents a service mesh returned by a describe operation.

              - **meshName** *(string) --*

                The name of the service mesh.

              - **metadata** *(dict) --*

                The associated metadata for the service mesh.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **spec** *(dict) --*

                The associated specification for the service mesh.

                - **egressFilter** *(dict) --*

                  The egress filter rules for the service mesh.

                  - **type** *(string) --*

                    The egress filter type. By default, the type is ``DROP_ALL`` , which allows egress only
                    from virtual nodes to other defined resources in the service mesh (and any traffic to
                    ``*.amazonaws.com`` for AWS API calls). You can set the egress filter type to
                    ``ALLOW_ALL`` to allow egress to any endpoint inside or outside of the service mesh.

              - **status** *(dict) --*

                The status of the service mesh.

                - **status** *(string) --*

                  The current mesh status.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_route(
        self,
        meshName: str,
        routeName: str,
        spec: ClientUpdateRoutespecTypeDef,
        virtualRouterName: str,
        clientToken: str = None,
    ) -> ClientUpdateRouteResponseTypeDef:
        """
        Updates an existing route for a specified service mesh and virtual router.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/UpdateRoute>`_

        **Request Syntax**
        ::

          response = client.update_route(
              clientToken='string',
              meshName='string',
              routeName='string',
              spec={
                  'grpcRoute': {
                      'action': {
                          'weightedTargets': [
                              {
                                  'virtualNode': 'string',
                                  'weight': 123
                              },
                          ]
                      },
                      'match': {
                          'metadata': [
                              {
                                  'invert': True|False,
                                  'match': {
                                      'exact': 'string',
                                      'prefix': 'string',
                                      'range': {
                                          'end': 123,
                                          'start': 123
                                      },
                                      'regex': 'string',
                                      'suffix': 'string'
                                  },
                                  'name': 'string'
                              },
                          ],
                          'methodName': 'string',
                          'serviceName': 'string'
                      },
                      'retryPolicy': {
                          'grpcRetryEvents': [
                              'cancelled'|'deadline-exceeded'|'internal'|'resource-exhausted'|'unavailable',
                          ],
                          'httpRetryEvents': [
                              'string',
                          ],
                          'maxRetries': 123,
                          'perRetryTimeout': {
                              'unit': 'ms'|'s',
                              'value': 123
                          },
                          'tcpRetryEvents': [
                              'connection-error',
                          ]
                      }
                  },
                  'http2Route': {
                      'action': {
                          'weightedTargets': [
                              {
                                  'virtualNode': 'string',
                                  'weight': 123
                              },
                          ]
                      },
                      'match': {
                          'headers': [
                              {
                                  'invert': True|False,
                                  'match': {
                                      'exact': 'string',
                                      'prefix': 'string',
                                      'range': {
                                          'end': 123,
                                          'start': 123
                                      },
                                      'regex': 'string',
                                      'suffix': 'string'
                                  },
                                  'name': 'string'
                              },
                          ],
                          'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                          'prefix': 'string',
                          'scheme': 'http'|'https'
                      },
                      'retryPolicy': {
                          'httpRetryEvents': [
                              'string',
                          ],
                          'maxRetries': 123,
                          'perRetryTimeout': {
                              'unit': 'ms'|'s',
                              'value': 123
                          },
                          'tcpRetryEvents': [
                              'connection-error',
                          ]
                      }
                  },
                  'httpRoute': {
                      'action': {
                          'weightedTargets': [
                              {
                                  'virtualNode': 'string',
                                  'weight': 123
                              },
                          ]
                      },
                      'match': {
                          'headers': [
                              {
                                  'invert': True|False,
                                  'match': {
                                      'exact': 'string',
                                      'prefix': 'string',
                                      'range': {
                                          'end': 123,
                                          'start': 123
                                      },
                                      'regex': 'string',
                                      'suffix': 'string'
                                  },
                                  'name': 'string'
                              },
                          ],
                          'method': 'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                          'prefix': 'string',
                          'scheme': 'http'|'https'
                      },
                      'retryPolicy': {
                          'httpRetryEvents': [
                              'string',
                          ],
                          'maxRetries': 123,
                          'perRetryTimeout': {
                              'unit': 'ms'|'s',
                              'value': 123
                          },
                          'tcpRetryEvents': [
                              'connection-error',
                          ]
                      }
                  },
                  'priority': 123,
                  'tcpRoute': {
                      'action': {
                          'weightedTargets': [
                              {
                                  'virtualNode': 'string',
                                  'weight': 123
                              },
                          ]
                      }
                  }
              },
              virtualRouterName='string'
          )
        :type clientToken: string
        :param clientToken:

          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up
          to 36 letters, numbers, hyphens, and underscores are allowed.

          This field is autopopulated if not provided.

        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh that the route resides in.

        :type routeName: string
        :param routeName: **[REQUIRED]**

          The name of the route to update.

        :type spec: dict
        :param spec: **[REQUIRED]**

          The new route specification to apply. This overwrites the existing data.

          - **grpcRoute** *(dict) --*

            An object that represents the specification of a GRPC route.

            - **action** *(dict) --* **[REQUIRED]**

              An object that represents the action to take if a match is determined.

              - **weightedTargets** *(list) --* **[REQUIRED]**

                An object that represents the targets that traffic is routed to when a request matches the
                route.

                - *(dict) --*

                  An object that represents a target and its relative weight. Traffic is distributed across
                  targets according to their relative weight. For example, a weighted target with a
                  relative weight of 50 receives five times as much traffic as one with a relative weight
                  of 10. The total weight for all targets combined must be less than or equal to 100.

                  - **virtualNode** *(string) --* **[REQUIRED]**

                    The virtual node to associate with the weighted target.

                  - **weight** *(integer) --* **[REQUIRED]**

                    The relative weight of the weighted target.

            - **match** *(dict) --* **[REQUIRED]**

              An object that represents the criteria for determining a request match.

              - **metadata** *(list) --*

                An object that represents the data to match from the request.

                - *(dict) --*

                  An object that represents the match metadata for the route.

                  - **invert** *(boolean) --*

                    Specify ``True`` to match anything except the match criteria. The default value is
                    ``False`` .

                  - **match** *(dict) --*

                    An object that represents the data to match from the request.

                    - **exact** *(string) --*

                      The value sent by the client must match the specified value exactly.

                    - **prefix** *(string) --*

                      The value sent by the client must begin with the specified characters.

                    - **range** *(dict) --*

                      An object that represents the range of values to match on.

                      - **end** *(integer) --* **[REQUIRED]**

                        The end of the range.

                      - **start** *(integer) --* **[REQUIRED]**

                        The start of the range.

                    - **regex** *(string) --*

                      The value sent by the client must include the specified characters.

                    - **suffix** *(string) --*

                      The value sent by the client must end with the specified characters.

                  - **name** *(string) --* **[REQUIRED]**

                    The name of the route.

              - **methodName** *(string) --*

                The method name to match from the request. If you specify a name, you must also specify a
                ``serviceName`` .

              - **serviceName** *(string) --*

                The fully qualified domain name for the service to match from the request.

            - **retryPolicy** *(dict) --*

              An object that represents a retry policy.

              - **grpcRetryEvents** *(list) --*

                Specify at least one of the valid values.

                - *(string) --*

              - **httpRetryEvents** *(list) --*

                Specify at least one of the following values.

                * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
                and 511

                * **gateway-error** – HTTP status codes 502, 503, and 504

                * **client-error** – HTTP status code 409

                * **stream-error** – Retry on refused stream

                - *(string) --*

              - **maxRetries** *(integer) --* **[REQUIRED]**

                The maximum number of retry attempts.

              - **perRetryTimeout** *(dict) --* **[REQUIRED]**

                An object that represents a duration of time.

                - **unit** *(string) --*

                  A unit of time.

                - **value** *(integer) --*

                  A number of time units.

              - **tcpRetryEvents** *(list) --*

                Specify a valid value.

                - *(string) --*

          - **http2Route** *(dict) --*

            An object that represents the specification of an HTTP2 route.

            - **action** *(dict) --* **[REQUIRED]**

              An object that represents the action to take if a match is determined.

              - **weightedTargets** *(list) --* **[REQUIRED]**

                An object that represents the targets that traffic is routed to when a request matches the
                route.

                - *(dict) --*

                  An object that represents a target and its relative weight. Traffic is distributed across
                  targets according to their relative weight. For example, a weighted target with a
                  relative weight of 50 receives five times as much traffic as one with a relative weight
                  of 10. The total weight for all targets combined must be less than or equal to 100.

                  - **virtualNode** *(string) --* **[REQUIRED]**

                    The virtual node to associate with the weighted target.

                  - **weight** *(integer) --* **[REQUIRED]**

                    The relative weight of the weighted target.

            - **match** *(dict) --* **[REQUIRED]**

              An object that represents the criteria for determining a request match.

              - **headers** *(list) --*

                An object that represents the client request headers to match on.

                - *(dict) --*

                  An object that represents the HTTP header in the request.

                  - **invert** *(boolean) --*

                    Specify ``True`` to match anything except the match criteria. The default value is
                    ``False`` .

                  - **match** *(dict) --*

                    The ``HeaderMatchMethod`` object.

                    - **exact** *(string) --*

                      The value sent by the client must match the specified value exactly.

                    - **prefix** *(string) --*

                      The value sent by the client must begin with the specified characters.

                    - **range** *(dict) --*

                      An object that represents the range of values to match on.

                      - **end** *(integer) --* **[REQUIRED]**

                        The end of the range.

                      - **start** *(integer) --* **[REQUIRED]**

                        The start of the range.

                    - **regex** *(string) --*

                      The value sent by the client must include the specified characters.

                    - **suffix** *(string) --*

                      The value sent by the client must end with the specified characters.

                  - **name** *(string) --* **[REQUIRED]**

                    A name for the HTTP header in the client request that will be matched on.

              - **method** *(string) --*

                The client request method to match on. Specify only one.

              - **prefix** *(string) --* **[REQUIRED]**

                Specifies the path to match requests with. This parameter must always start with ``/`` ,
                which by itself matches all requests to the virtual service name. You can also match for
                path-based routing of requests. For example, if your virtual service name is
                ``my-service.local`` and you want the route to match requests to
                ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

              - **scheme** *(string) --*

                The client request scheme to match on. Specify only one.

            - **retryPolicy** *(dict) --*

              An object that represents a retry policy.

              - **httpRetryEvents** *(list) --*

                Specify at least one of the following values.

                * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
                and 511

                * **gateway-error** – HTTP status codes 502, 503, and 504

                * **client-error** – HTTP status code 409

                * **stream-error** – Retry on refused stream

                - *(string) --*

              - **maxRetries** *(integer) --* **[REQUIRED]**

                The maximum number of retry attempts.

              - **perRetryTimeout** *(dict) --* **[REQUIRED]**

                An object that represents a duration of time.

                - **unit** *(string) --*

                  A unit of time.

                - **value** *(integer) --*

                  A number of time units.

              - **tcpRetryEvents** *(list) --*

                Specify a valid value.

                - *(string) --*

          - **httpRoute** *(dict) --*

            An object that represents the specification of an HTTP route.

            - **action** *(dict) --* **[REQUIRED]**

              An object that represents the action to take if a match is determined.

              - **weightedTargets** *(list) --* **[REQUIRED]**

                An object that represents the targets that traffic is routed to when a request matches the
                route.

                - *(dict) --*

                  An object that represents a target and its relative weight. Traffic is distributed across
                  targets according to their relative weight. For example, a weighted target with a
                  relative weight of 50 receives five times as much traffic as one with a relative weight
                  of 10. The total weight for all targets combined must be less than or equal to 100.

                  - **virtualNode** *(string) --* **[REQUIRED]**

                    The virtual node to associate with the weighted target.

                  - **weight** *(integer) --* **[REQUIRED]**

                    The relative weight of the weighted target.

            - **match** *(dict) --* **[REQUIRED]**

              An object that represents the criteria for determining a request match.

              - **headers** *(list) --*

                An object that represents the client request headers to match on.

                - *(dict) --*

                  An object that represents the HTTP header in the request.

                  - **invert** *(boolean) --*

                    Specify ``True`` to match anything except the match criteria. The default value is
                    ``False`` .

                  - **match** *(dict) --*

                    The ``HeaderMatchMethod`` object.

                    - **exact** *(string) --*

                      The value sent by the client must match the specified value exactly.

                    - **prefix** *(string) --*

                      The value sent by the client must begin with the specified characters.

                    - **range** *(dict) --*

                      An object that represents the range of values to match on.

                      - **end** *(integer) --* **[REQUIRED]**

                        The end of the range.

                      - **start** *(integer) --* **[REQUIRED]**

                        The start of the range.

                    - **regex** *(string) --*

                      The value sent by the client must include the specified characters.

                    - **suffix** *(string) --*

                      The value sent by the client must end with the specified characters.

                  - **name** *(string) --* **[REQUIRED]**

                    A name for the HTTP header in the client request that will be matched on.

              - **method** *(string) --*

                The client request method to match on. Specify only one.

              - **prefix** *(string) --* **[REQUIRED]**

                Specifies the path to match requests with. This parameter must always start with ``/`` ,
                which by itself matches all requests to the virtual service name. You can also match for
                path-based routing of requests. For example, if your virtual service name is
                ``my-service.local`` and you want the route to match requests to
                ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

              - **scheme** *(string) --*

                The client request scheme to match on. Specify only one.

            - **retryPolicy** *(dict) --*

              An object that represents a retry policy.

              - **httpRetryEvents** *(list) --*

                Specify at least one of the following values.

                * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510,
                and 511

                * **gateway-error** – HTTP status codes 502, 503, and 504

                * **client-error** – HTTP status code 409

                * **stream-error** – Retry on refused stream

                - *(string) --*

              - **maxRetries** *(integer) --* **[REQUIRED]**

                The maximum number of retry attempts.

              - **perRetryTimeout** *(dict) --* **[REQUIRED]**

                An object that represents a duration of time.

                - **unit** *(string) --*

                  A unit of time.

                - **value** *(integer) --*

                  A number of time units.

              - **tcpRetryEvents** *(list) --*

                Specify a valid value.

                - *(string) --*

          - **priority** *(integer) --*

            The priority for the route. Routes are matched based on the specified value, where 0 is the
            highest priority.

          - **tcpRoute** *(dict) --*

            An object that represents the specification of a TCP route.

            - **action** *(dict) --* **[REQUIRED]**

              The action to take if a match is determined.

              - **weightedTargets** *(list) --* **[REQUIRED]**

                An object that represents the targets that traffic is routed to when a request matches the
                route.

                - *(dict) --*

                  An object that represents a target and its relative weight. Traffic is distributed across
                  targets according to their relative weight. For example, a weighted target with a
                  relative weight of 50 receives five times as much traffic as one with a relative weight
                  of 10. The total weight for all targets combined must be less than or equal to 100.

                  - **virtualNode** *(string) --* **[REQUIRED]**

                    The virtual node to associate with the weighted target.

                  - **weight** *(integer) --* **[REQUIRED]**

                    The relative weight of the weighted target.

        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**

          The name of the virtual router that the route is associated with.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'route': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'routeName': 'string',
                    'spec': {
                        'grpcRoute': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            },
                            'match': {
                                'metadata': [
                                    {
                                        'invert': True|False,
                                        'match': {
                                            'exact': 'string',
                                            'prefix': 'string',
                                            'range': {
                                                'end': 123,
                                                'start': 123
                                            },
                                            'regex': 'string',
                                            'suffix': 'string'
                                        },
                                        'name': 'string'
                                    },
                                ],
                                'methodName': 'string',
                                'serviceName': 'string'
                            },
                            'retryPolicy': {
                                'grpcRetryEvents': [
                                    'cancelled'|'deadline-exceeded'|'internal'|'resource-exhausted'
                                    |'unavailable',
                                ],
                                'httpRetryEvents': [
                                    'string',
                                ],
                                'maxRetries': 123,
                                'perRetryTimeout': {
                                    'unit': 'ms'|'s',
                                    'value': 123
                                },
                                'tcpRetryEvents': [
                                    'connection-error',
                                ]
                            }
                        },
                        'http2Route': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            },
                            'match': {
                                'headers': [
                                    {
                                        'invert': True|False,
                                        'match': {
                                            'exact': 'string',
                                            'prefix': 'string',
                                            'range': {
                                                'end': 123,
                                                'start': 123
                                            },
                                            'regex': 'string',
                                            'suffix': 'string'
                                        },
                                        'name': 'string'
                                    },
                                ],
                                'method':
                                'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                                'prefix': 'string',
                                'scheme': 'http'|'https'
                            },
                            'retryPolicy': {
                                'httpRetryEvents': [
                                    'string',
                                ],
                                'maxRetries': 123,
                                'perRetryTimeout': {
                                    'unit': 'ms'|'s',
                                    'value': 123
                                },
                                'tcpRetryEvents': [
                                    'connection-error',
                                ]
                            }
                        },
                        'httpRoute': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            },
                            'match': {
                                'headers': [
                                    {
                                        'invert': True|False,
                                        'match': {
                                            'exact': 'string',
                                            'prefix': 'string',
                                            'range': {
                                                'end': 123,
                                                'start': 123
                                            },
                                            'regex': 'string',
                                            'suffix': 'string'
                                        },
                                        'name': 'string'
                                    },
                                ],
                                'method':
                                'CONNECT'|'DELETE'|'GET'|'HEAD'|'OPTIONS'|'PATCH'|'POST'|'PUT'|'TRACE',
                                'prefix': 'string',
                                'scheme': 'http'|'https'
                            },
                            'retryPolicy': {
                                'httpRetryEvents': [
                                    'string',
                                ],
                                'maxRetries': 123,
                                'perRetryTimeout': {
                                    'unit': 'ms'|'s',
                                    'value': 123
                                },
                                'tcpRetryEvents': [
                                    'connection-error',
                                ]
                            }
                        },
                        'priority': 123,
                        'tcpRoute': {
                            'action': {
                                'weightedTargets': [
                                    {
                                        'virtualNode': 'string',
                                        'weight': 123
                                    },
                                ]
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualRouterName': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **route** *(dict) --*

              A full description of the route that was updated.

              - **meshName** *(string) --*

                The name of the service mesh that the route resides in.

              - **metadata** *(dict) --*

                The associated metadata for the route.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **routeName** *(string) --*

                The name of the route.

              - **spec** *(dict) --*

                The specifications of the route.

                - **grpcRoute** *(dict) --*

                  An object that represents the specification of a GRPC route.

                  - **action** *(dict) --*

                    An object that represents the action to take if a match is determined.

                    - **weightedTargets** *(list) --*

                      An object that represents the targets that traffic is routed to when a request
                      matches the route.

                      - *(dict) --*

                        An object that represents a target and its relative weight. Traffic is distributed
                        across targets according to their relative weight. For example, a weighted target
                        with a relative weight of 50 receives five times as much traffic as one with a
                        relative weight of 10. The total weight for all targets combined must be less than
                        or equal to 100.

                        - **virtualNode** *(string) --*

                          The virtual node to associate with the weighted target.

                        - **weight** *(integer) --*

                          The relative weight of the weighted target.

                  - **match** *(dict) --*

                    An object that represents the criteria for determining a request match.

                    - **metadata** *(list) --*

                      An object that represents the data to match from the request.

                      - *(dict) --*

                        An object that represents the match metadata for the route.

                        - **invert** *(boolean) --*

                          Specify ``True`` to match anything except the match criteria. The default value
                          is ``False`` .

                        - **match** *(dict) --*

                          An object that represents the data to match from the request.

                          - **exact** *(string) --*

                            The value sent by the client must match the specified value exactly.

                          - **prefix** *(string) --*

                            The value sent by the client must begin with the specified characters.

                          - **range** *(dict) --*

                            An object that represents the range of values to match on.

                            - **end** *(integer) --*

                              The end of the range.

                            - **start** *(integer) --*

                              The start of the range.

                          - **regex** *(string) --*

                            The value sent by the client must include the specified characters.

                          - **suffix** *(string) --*

                            The value sent by the client must end with the specified characters.

                        - **name** *(string) --*

                          The name of the route.

                    - **methodName** *(string) --*

                      The method name to match from the request. If you specify a name, you must also
                      specify a ``serviceName`` .

                    - **serviceName** *(string) --*

                      The fully qualified domain name for the service to match from the request.

                  - **retryPolicy** *(dict) --*

                    An object that represents a retry policy.

                    - **grpcRetryEvents** *(list) --*

                      Specify at least one of the valid values.

                      - *(string) --*

                    - **httpRetryEvents** *(list) --*

                      Specify at least one of the following values.

                      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
                      510, and 511

                      * **gateway-error** – HTTP status codes 502, 503, and 504

                      * **client-error** – HTTP status code 409

                      * **stream-error** – Retry on refused stream

                      - *(string) --*

                    - **maxRetries** *(integer) --*

                      The maximum number of retry attempts.

                    - **perRetryTimeout** *(dict) --*

                      An object that represents a duration of time.

                      - **unit** *(string) --*

                        A unit of time.

                      - **value** *(integer) --*

                        A number of time units.

                    - **tcpRetryEvents** *(list) --*

                      Specify a valid value.

                      - *(string) --*

                - **http2Route** *(dict) --*

                  An object that represents the specification of an HTTP2 route.

                  - **action** *(dict) --*

                    An object that represents the action to take if a match is determined.

                    - **weightedTargets** *(list) --*

                      An object that represents the targets that traffic is routed to when a request
                      matches the route.

                      - *(dict) --*

                        An object that represents a target and its relative weight. Traffic is distributed
                        across targets according to their relative weight. For example, a weighted target
                        with a relative weight of 50 receives five times as much traffic as one with a
                        relative weight of 10. The total weight for all targets combined must be less than
                        or equal to 100.

                        - **virtualNode** *(string) --*

                          The virtual node to associate with the weighted target.

                        - **weight** *(integer) --*

                          The relative weight of the weighted target.

                  - **match** *(dict) --*

                    An object that represents the criteria for determining a request match.

                    - **headers** *(list) --*

                      An object that represents the client request headers to match on.

                      - *(dict) --*

                        An object that represents the HTTP header in the request.

                        - **invert** *(boolean) --*

                          Specify ``True`` to match anything except the match criteria. The default value
                          is ``False`` .

                        - **match** *(dict) --*

                          The ``HeaderMatchMethod`` object.

                          - **exact** *(string) --*

                            The value sent by the client must match the specified value exactly.

                          - **prefix** *(string) --*

                            The value sent by the client must begin with the specified characters.

                          - **range** *(dict) --*

                            An object that represents the range of values to match on.

                            - **end** *(integer) --*

                              The end of the range.

                            - **start** *(integer) --*

                              The start of the range.

                          - **regex** *(string) --*

                            The value sent by the client must include the specified characters.

                          - **suffix** *(string) --*

                            The value sent by the client must end with the specified characters.

                        - **name** *(string) --*

                          A name for the HTTP header in the client request that will be matched on.

                    - **method** *(string) --*

                      The client request method to match on. Specify only one.

                    - **prefix** *(string) --*

                      Specifies the path to match requests with. This parameter must always start with
                      ``/`` , which by itself matches all requests to the virtual service name. You can
                      also match for path-based routing of requests. For example, if your virtual service
                      name is ``my-service.local`` and you want the route to match requests to
                      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

                    - **scheme** *(string) --*

                      The client request scheme to match on. Specify only one.

                  - **retryPolicy** *(dict) --*

                    An object that represents a retry policy.

                    - **httpRetryEvents** *(list) --*

                      Specify at least one of the following values.

                      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
                      510, and 511

                      * **gateway-error** – HTTP status codes 502, 503, and 504

                      * **client-error** – HTTP status code 409

                      * **stream-error** – Retry on refused stream

                      - *(string) --*

                    - **maxRetries** *(integer) --*

                      The maximum number of retry attempts.

                    - **perRetryTimeout** *(dict) --*

                      An object that represents a duration of time.

                      - **unit** *(string) --*

                        A unit of time.

                      - **value** *(integer) --*

                        A number of time units.

                    - **tcpRetryEvents** *(list) --*

                      Specify a valid value.

                      - *(string) --*

                - **httpRoute** *(dict) --*

                  An object that represents the specification of an HTTP route.

                  - **action** *(dict) --*

                    An object that represents the action to take if a match is determined.

                    - **weightedTargets** *(list) --*

                      An object that represents the targets that traffic is routed to when a request
                      matches the route.

                      - *(dict) --*

                        An object that represents a target and its relative weight. Traffic is distributed
                        across targets according to their relative weight. For example, a weighted target
                        with a relative weight of 50 receives five times as much traffic as one with a
                        relative weight of 10. The total weight for all targets combined must be less than
                        or equal to 100.

                        - **virtualNode** *(string) --*

                          The virtual node to associate with the weighted target.

                        - **weight** *(integer) --*

                          The relative weight of the weighted target.

                  - **match** *(dict) --*

                    An object that represents the criteria for determining a request match.

                    - **headers** *(list) --*

                      An object that represents the client request headers to match on.

                      - *(dict) --*

                        An object that represents the HTTP header in the request.

                        - **invert** *(boolean) --*

                          Specify ``True`` to match anything except the match criteria. The default value
                          is ``False`` .

                        - **match** *(dict) --*

                          The ``HeaderMatchMethod`` object.

                          - **exact** *(string) --*

                            The value sent by the client must match the specified value exactly.

                          - **prefix** *(string) --*

                            The value sent by the client must begin with the specified characters.

                          - **range** *(dict) --*

                            An object that represents the range of values to match on.

                            - **end** *(integer) --*

                              The end of the range.

                            - **start** *(integer) --*

                              The start of the range.

                          - **regex** *(string) --*

                            The value sent by the client must include the specified characters.

                          - **suffix** *(string) --*

                            The value sent by the client must end with the specified characters.

                        - **name** *(string) --*

                          A name for the HTTP header in the client request that will be matched on.

                    - **method** *(string) --*

                      The client request method to match on. Specify only one.

                    - **prefix** *(string) --*

                      Specifies the path to match requests with. This parameter must always start with
                      ``/`` , which by itself matches all requests to the virtual service name. You can
                      also match for path-based routing of requests. For example, if your virtual service
                      name is ``my-service.local`` and you want the route to match requests to
                      ``my-service.local/metrics`` , your prefix should be ``/metrics`` .

                    - **scheme** *(string) --*

                      The client request scheme to match on. Specify only one.

                  - **retryPolicy** *(dict) --*

                    An object that represents a retry policy.

                    - **httpRetryEvents** *(list) --*

                      Specify at least one of the following values.

                      * **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508,
                      510, and 511

                      * **gateway-error** – HTTP status codes 502, 503, and 504

                      * **client-error** – HTTP status code 409

                      * **stream-error** – Retry on refused stream

                      - *(string) --*

                    - **maxRetries** *(integer) --*

                      The maximum number of retry attempts.

                    - **perRetryTimeout** *(dict) --*

                      An object that represents a duration of time.

                      - **unit** *(string) --*

                        A unit of time.

                      - **value** *(integer) --*

                        A number of time units.

                    - **tcpRetryEvents** *(list) --*

                      Specify a valid value.

                      - *(string) --*

                - **priority** *(integer) --*

                  The priority for the route. Routes are matched based on the specified value, where 0 is
                  the highest priority.

                - **tcpRoute** *(dict) --*

                  An object that represents the specification of a TCP route.

                  - **action** *(dict) --*

                    The action to take if a match is determined.

                    - **weightedTargets** *(list) --*

                      An object that represents the targets that traffic is routed to when a request
                      matches the route.

                      - *(dict) --*

                        An object that represents a target and its relative weight. Traffic is distributed
                        across targets according to their relative weight. For example, a weighted target
                        with a relative weight of 50 receives five times as much traffic as one with a
                        relative weight of 10. The total weight for all targets combined must be less than
                        or equal to 100.

                        - **virtualNode** *(string) --*

                          The virtual node to associate with the weighted target.

                        - **weight** *(integer) --*

                          The relative weight of the weighted target.

              - **status** *(dict) --*

                The status of the route.

                - **status** *(string) --*

                  The current status for the route.

              - **virtualRouterName** *(string) --*

                The virtual router that the route is associated with.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_virtual_node(
        self,
        meshName: str,
        spec: ClientUpdateVirtualNodespecTypeDef,
        virtualNodeName: str,
        clientToken: str = None,
    ) -> ClientUpdateVirtualNodeResponseTypeDef:
        """
        Updates an existing virtual node in a specified service mesh.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/UpdateVirtualNode>`_

        **Request Syntax**
        ::

          response = client.update_virtual_node(
              clientToken='string',
              meshName='string',
              spec={
                  'backends': [
                      {
                          'virtualService': {
                              'virtualServiceName': 'string'
                          }
                      },
                  ],
                  'listeners': [
                      {
                          'healthCheck': {
                              'healthyThreshold': 123,
                              'intervalMillis': 123,
                              'path': 'string',
                              'port': 123,
                              'protocol': 'grpc'|'http'|'http2'|'tcp',
                              'timeoutMillis': 123,
                              'unhealthyThreshold': 123
                          },
                          'portMapping': {
                              'port': 123,
                              'protocol': 'grpc'|'http'|'http2'|'tcp'
                          }
                      },
                  ],
                  'logging': {
                      'accessLog': {
                          'file': {
                              'path': 'string'
                          }
                      }
                  },
                  'serviceDiscovery': {
                      'awsCloudMap': {
                          'attributes': [
                              {
                                  'key': 'string',
                                  'value': 'string'
                              },
                          ],
                          'namespaceName': 'string',
                          'serviceName': 'string'
                      },
                      'dns': {
                          'hostname': 'string'
                      }
                  }
              },
              virtualNodeName='string'
          )
        :type clientToken: string
        :param clientToken:

          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up
          to 36 letters, numbers, hyphens, and underscores are allowed.

          This field is autopopulated if not provided.

        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh that the virtual node resides in.

        :type spec: dict
        :param spec: **[REQUIRED]**

          The new virtual node specification to apply. This overwrites the existing data.

          - **backends** *(list) --*

            The backends that the virtual node is expected to send outbound traffic to.

            - *(dict) --*

              An object that represents the backends that a virtual node is expected to send outbound
              traffic to.

              - **virtualService** *(dict) --*

                Specifies a virtual service to use as a backend for a virtual node.

                - **virtualServiceName** *(string) --* **[REQUIRED]**

                  The name of the virtual service that is acting as a virtual node backend.

          - **listeners** *(list) --*

            The listeners that the virtual node is expected to receive inbound traffic from. You can
            specify one listener.

            - *(dict) --*

              An object that represents a listener for a virtual node.

              - **healthCheck** *(dict) --*

                The health check information for the listener.

                - **healthyThreshold** *(integer) --* **[REQUIRED]**

                  The number of consecutive successful health checks that must occur before declaring
                  listener healthy.

                - **intervalMillis** *(integer) --* **[REQUIRED]**

                  The time period in milliseconds between each health check execution.

                - **path** *(string) --*

                  The destination path for the health check request. This is required only if the specified
                  protocol is HTTP. If the protocol is TCP, this parameter is ignored.

                - **port** *(integer) --*

                  The destination port for the health check request. This port must match the port defined
                  in the  PortMapping for the listener.

                - **protocol** *(string) --* **[REQUIRED]**

                  The protocol for the health check request.

                - **timeoutMillis** *(integer) --* **[REQUIRED]**

                  The amount of time to wait when receiving a response from the health check, in
                  milliseconds.

                - **unhealthyThreshold** *(integer) --* **[REQUIRED]**

                  The number of consecutive failed health checks that must occur before declaring a virtual
                  node unhealthy.

              - **portMapping** *(dict) --* **[REQUIRED]**

                The port mapping information for the listener.

                - **port** *(integer) --* **[REQUIRED]**

                  The port used for the port mapping.

                - **protocol** *(string) --* **[REQUIRED]**

                  The protocol used for the port mapping. Specify one protocol.

          - **logging** *(dict) --*

            The inbound and outbound access logging information for the virtual node.

            - **accessLog** *(dict) --*

              The access log configuration for a virtual node.

              - **file** *(dict) --*

                The file object to send virtual node access logs to.

                - **path** *(string) --* **[REQUIRED]**

                  The file path to write access logs to. You can use ``/dev/stdout`` to send access logs to
                  standard out and configure your Envoy container to use a log driver, such as ``awslogs``
                  , to export the access logs to a log storage service such as Amazon CloudWatch Logs. You
                  can also specify a path in the Envoy container's file system to write the files to disk.

                  .. note::

                    The Envoy process must have write permissions to the path that you specify here.
                    Otherwise, Envoy fails to bootstrap properly.

          - **serviceDiscovery** *(dict) --*

            The service discovery information for the virtual node. If your virtual node does not expect
            ingress traffic, you can omit this parameter.

            - **awsCloudMap** *(dict) --*

              Specifies any AWS Cloud Map information for the virtual node.

              - **attributes** *(list) --*

                A string map that contains attributes with values that you can use to filter instances by
                any custom attribute that you specified when you registered the instance. Only instances
                that match all of the specified key/value pairs will be returned.

                - *(dict) --*

                  An object that represents the AWS Cloud Map attribute information for your virtual node.

                  - **key** *(string) --* **[REQUIRED]**

                    The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
                    instance that contains the specified key and value is returned.

                  - **value** *(string) --* **[REQUIRED]**

                    The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map service
                    instance that contains the specified key and value is returned.

              - **namespaceName** *(string) --* **[REQUIRED]**

                The name of the AWS Cloud Map namespace to use.

              - **serviceName** *(string) --* **[REQUIRED]**

                The name of the AWS Cloud Map service to use.

            - **dns** *(dict) --*

              Specifies the DNS information for the virtual node.

              - **hostname** *(string) --* **[REQUIRED]**

                Specifies the DNS service discovery hostname for the virtual node.

        :type virtualNodeName: string
        :param virtualNodeName: **[REQUIRED]**

          The name of the virtual node to update.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'virtualNode': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'backends': [
                            {
                                'virtualService': {
                                    'virtualServiceName': 'string'
                                }
                            },
                        ],
                        'listeners': [
                            {
                                'healthCheck': {
                                    'healthyThreshold': 123,
                                    'intervalMillis': 123,
                                    'path': 'string',
                                    'port': 123,
                                    'protocol': 'grpc'|'http'|'http2'|'tcp',
                                    'timeoutMillis': 123,
                                    'unhealthyThreshold': 123
                                },
                                'portMapping': {
                                    'port': 123,
                                    'protocol': 'grpc'|'http'|'http2'|'tcp'
                                }
                            },
                        ],
                        'logging': {
                            'accessLog': {
                                'file': {
                                    'path': 'string'
                                }
                            }
                        },
                        'serviceDiscovery': {
                            'awsCloudMap': {
                                'attributes': [
                                    {
                                        'key': 'string',
                                        'value': 'string'
                                    },
                                ],
                                'namespaceName': 'string',
                                'serviceName': 'string'
                            },
                            'dns': {
                                'hostname': 'string'
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualNodeName': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **virtualNode** *(dict) --*

              A full description of the virtual node that was updated.

              - **meshName** *(string) --*

                The name of the service mesh that the virtual node resides in.

              - **metadata** *(dict) --*

                The associated metadata for the virtual node.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **spec** *(dict) --*

                The specifications of the virtual node.

                - **backends** *(list) --*

                  The backends that the virtual node is expected to send outbound traffic to.

                  - *(dict) --*

                    An object that represents the backends that a virtual node is expected to send outbound
                    traffic to.

                    - **virtualService** *(dict) --*

                      Specifies a virtual service to use as a backend for a virtual node.

                      - **virtualServiceName** *(string) --*

                        The name of the virtual service that is acting as a virtual node backend.

                - **listeners** *(list) --*

                  The listeners that the virtual node is expected to receive inbound traffic from. You can
                  specify one listener.

                  - *(dict) --*

                    An object that represents a listener for a virtual node.

                    - **healthCheck** *(dict) --*

                      The health check information for the listener.

                      - **healthyThreshold** *(integer) --*

                        The number of consecutive successful health checks that must occur before declaring
                        listener healthy.

                      - **intervalMillis** *(integer) --*

                        The time period in milliseconds between each health check execution.

                      - **path** *(string) --*

                        The destination path for the health check request. This is required only if the
                        specified protocol is HTTP. If the protocol is TCP, this parameter is ignored.

                      - **port** *(integer) --*

                        The destination port for the health check request. This port must match the port
                        defined in the  PortMapping for the listener.

                      - **protocol** *(string) --*

                        The protocol for the health check request.

                      - **timeoutMillis** *(integer) --*

                        The amount of time to wait when receiving a response from the health check, in
                        milliseconds.

                      - **unhealthyThreshold** *(integer) --*

                        The number of consecutive failed health checks that must occur before declaring a
                        virtual node unhealthy.

                    - **portMapping** *(dict) --*

                      The port mapping information for the listener.

                      - **port** *(integer) --*

                        The port used for the port mapping.

                      - **protocol** *(string) --*

                        The protocol used for the port mapping. Specify one protocol.

                - **logging** *(dict) --*

                  The inbound and outbound access logging information for the virtual node.

                  - **accessLog** *(dict) --*

                    The access log configuration for a virtual node.

                    - **file** *(dict) --*

                      The file object to send virtual node access logs to.

                      - **path** *(string) --*

                        The file path to write access logs to. You can use ``/dev/stdout`` to send access
                        logs to standard out and configure your Envoy container to use a log driver, such
                        as ``awslogs`` , to export the access logs to a log storage service such as Amazon
                        CloudWatch Logs. You can also specify a path in the Envoy container's file system
                        to write the files to disk.

                        .. note::

                          The Envoy process must have write permissions to the path that you specify here.
                          Otherwise, Envoy fails to bootstrap properly.

                - **serviceDiscovery** *(dict) --*

                  The service discovery information for the virtual node. If your virtual node does not
                  expect ingress traffic, you can omit this parameter.

                  - **awsCloudMap** *(dict) --*

                    Specifies any AWS Cloud Map information for the virtual node.

                    - **attributes** *(list) --*

                      A string map that contains attributes with values that you can use to filter
                      instances by any custom attribute that you specified when you registered the
                      instance. Only instances that match all of the specified key/value pairs will be
                      returned.

                      - *(dict) --*

                        An object that represents the AWS Cloud Map attribute information for your virtual
                        node.

                        - **key** *(string) --*

                          The name of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                          service instance that contains the specified key and value is returned.

                        - **value** *(string) --*

                          The value of an AWS Cloud Map service instance attribute key. Any AWS Cloud Map
                          service instance that contains the specified key and value is returned.

                    - **namespaceName** *(string) --*

                      The name of the AWS Cloud Map namespace to use.

                    - **serviceName** *(string) --*

                      The name of the AWS Cloud Map service to use.

                  - **dns** *(dict) --*

                    Specifies the DNS information for the virtual node.

                    - **hostname** *(string) --*

                      Specifies the DNS service discovery hostname for the virtual node.

              - **status** *(dict) --*

                The current status for the virtual node.

                - **status** *(string) --*

                  The current status of the virtual node.

              - **virtualNodeName** *(string) --*

                The name of the virtual node.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_virtual_router(
        self,
        meshName: str,
        spec: ClientUpdateVirtualRouterspecTypeDef,
        virtualRouterName: str,
        clientToken: str = None,
    ) -> ClientUpdateVirtualRouterResponseTypeDef:
        """
        Updates an existing virtual router in a specified service mesh.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/UpdateVirtualRouter>`_

        **Request Syntax**
        ::

          response = client.update_virtual_router(
              clientToken='string',
              meshName='string',
              spec={
                  'listeners': [
                      {
                          'portMapping': {
                              'port': 123,
                              'protocol': 'grpc'|'http'|'http2'|'tcp'
                          }
                      },
                  ]
              },
              virtualRouterName='string'
          )
        :type clientToken: string
        :param clientToken:

          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up
          to 36 letters, numbers, hyphens, and underscores are allowed.

          This field is autopopulated if not provided.

        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh that the virtual router resides in.

        :type spec: dict
        :param spec: **[REQUIRED]**

          The new virtual router specification to apply. This overwrites the existing data.

          - **listeners** *(list) --*

            The listeners that the virtual router is expected to receive inbound traffic from. You can
            specify one listener.

            - *(dict) --*

              An object that represents a virtual router listener.

              - **portMapping** *(dict) --* **[REQUIRED]**

                An object that represents a port mapping.

                - **port** *(integer) --* **[REQUIRED]**

                  The port used for the port mapping.

                - **protocol** *(string) --* **[REQUIRED]**

                  The protocol used for the port mapping. Specify one protocol.

        :type virtualRouterName: string
        :param virtualRouterName: **[REQUIRED]**

          The name of the virtual router to update.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'virtualRouter': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'listeners': [
                            {
                                'portMapping': {
                                    'port': 123,
                                    'protocol': 'grpc'|'http'|'http2'|'tcp'
                                }
                            },
                        ]
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualRouterName': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **virtualRouter** *(dict) --*

              A full description of the virtual router that was updated.

              - **meshName** *(string) --*

                The name of the service mesh that the virtual router resides in.

              - **metadata** *(dict) --*

                The associated metadata for the virtual router.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **spec** *(dict) --*

                The specifications of the virtual router.

                - **listeners** *(list) --*

                  The listeners that the virtual router is expected to receive inbound traffic from. You
                  can specify one listener.

                  - *(dict) --*

                    An object that represents a virtual router listener.

                    - **portMapping** *(dict) --*

                      An object that represents a port mapping.

                      - **port** *(integer) --*

                        The port used for the port mapping.

                      - **protocol** *(string) --*

                        The protocol used for the port mapping. Specify one protocol.

              - **status** *(dict) --*

                The current status of the virtual router.

                - **status** *(string) --*

                  The current status of the virtual router.

              - **virtualRouterName** *(string) --*

                The name of the virtual router.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_virtual_service(
        self,
        meshName: str,
        spec: ClientUpdateVirtualServicespecTypeDef,
        virtualServiceName: str,
        clientToken: str = None,
    ) -> ClientUpdateVirtualServiceResponseTypeDef:
        """
        Updates an existing virtual service in a specified service mesh.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/UpdateVirtualService>`_

        **Request Syntax**
        ::

          response = client.update_virtual_service(
              clientToken='string',
              meshName='string',
              spec={
                  'provider': {
                      'virtualNode': {
                          'virtualNodeName': 'string'
                      },
                      'virtualRouter': {
                          'virtualRouterName': 'string'
                      }
                  }
              },
              virtualServiceName='string'
          )
        :type clientToken: string
        :param clientToken:

          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up
          to 36 letters, numbers, hyphens, and underscores are allowed.

          This field is autopopulated if not provided.

        :type meshName: string
        :param meshName: **[REQUIRED]**

          The name of the service mesh that the virtual service resides in.

        :type spec: dict
        :param spec: **[REQUIRED]**

          The new virtual service specification to apply. This overwrites the existing data.

          - **provider** *(dict) --*

            The App Mesh object that is acting as the provider for a virtual service. You can specify a
            single virtual node or virtual router.

            - **virtualNode** *(dict) --*

              The virtual node associated with a virtual service.

              - **virtualNodeName** *(string) --* **[REQUIRED]**

                The name of the virtual node that is acting as a service provider.

            - **virtualRouter** *(dict) --*

              The virtual router associated with a virtual service.

              - **virtualRouterName** *(string) --* **[REQUIRED]**

                The name of the virtual router that is acting as a service provider.

        :type virtualServiceName: string
        :param virtualServiceName: **[REQUIRED]**

          The name of the virtual service to update.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'virtualService': {
                    'meshName': 'string',
                    'metadata': {
                        'arn': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'uid': 'string',
                        'version': 123
                    },
                    'spec': {
                        'provider': {
                            'virtualNode': {
                                'virtualNodeName': 'string'
                            },
                            'virtualRouter': {
                                'virtualRouterName': 'string'
                            }
                        }
                    },
                    'status': {
                        'status': 'ACTIVE'|'DELETED'|'INACTIVE'
                    },
                    'virtualServiceName': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **virtualService** *(dict) --*

              A full description of the virtual service that was updated.

              - **meshName** *(string) --*

                The name of the service mesh that the virtual service resides in.

              - **metadata** *(dict) --*

                An object that represents metadata for a resource.

                - **arn** *(string) --*

                  The full Amazon Resource Name (ARN) for the resource.

                - **createdAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was created.

                - **lastUpdatedAt** *(datetime) --*

                  The Unix epoch timestamp in seconds for when the resource was last updated.

                - **uid** *(string) --*

                  The unique identifier for the resource.

                - **version** *(integer) --*

                  The version of the resource. Resources are created at version 1, and this version is
                  incremented each time that they're updated.

              - **spec** *(dict) --*

                The specifications of the virtual service.

                - **provider** *(dict) --*

                  The App Mesh object that is acting as the provider for a virtual service. You can specify
                  a single virtual node or virtual router.

                  - **virtualNode** *(dict) --*

                    The virtual node associated with a virtual service.

                    - **virtualNodeName** *(string) --*

                      The name of the virtual node that is acting as a service provider.

                  - **virtualRouter** *(dict) --*

                    The virtual router associated with a virtual service.

                    - **virtualRouterName** *(string) --*

                      The name of the virtual router that is acting as a service provider.

              - **status** *(dict) --*

                The current status of the virtual service.

                - **status** *(string) --*

                  The current status of the virtual service.

              - **virtualServiceName** *(string) --*

                The name of the virtual service.

        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_meshes"]
    ) -> paginator_scope.ListMeshesPaginator:
        """
        Get Paginator for `list_meshes` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_routes"]
    ) -> paginator_scope.ListRoutesPaginator:
        """
        Get Paginator for `list_routes` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> paginator_scope.ListTagsForResourcePaginator:
        """
        Get Paginator for `list_tags_for_resource` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_virtual_nodes"]
    ) -> paginator_scope.ListVirtualNodesPaginator:
        """
        Get Paginator for `list_virtual_nodes` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_virtual_routers"]
    ) -> paginator_scope.ListVirtualRoutersPaginator:
        """
        Get Paginator for `list_virtual_routers` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_virtual_services"]
    ) -> paginator_scope.ListVirtualServicesPaginator:
        """
        Get Paginator for `list_virtual_services` operation.
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
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ConflictException: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    TooManyTagsException: Boto3ClientError

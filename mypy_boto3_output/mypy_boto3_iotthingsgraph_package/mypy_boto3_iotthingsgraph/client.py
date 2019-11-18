"Main interface for iotthingsgraph Client"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

# pylint: disable=import-self
import mypy_boto3_iotthingsgraph.client as client_scope

# pylint: disable=import-self
import mypy_boto3_iotthingsgraph.paginator as paginator_scope
from mypy_boto3_iotthingsgraph.type_defs import (
    ClientCreateFlowTemplateResponseTypeDef,
    ClientCreateFlowTemplatedefinitionTypeDef,
    ClientCreateSystemInstanceResponseTypeDef,
    ClientCreateSystemInstancedefinitionTypeDef,
    ClientCreateSystemInstancemetricsConfigurationTypeDef,
    ClientCreateSystemInstancetagsTypeDef,
    ClientCreateSystemTemplateResponseTypeDef,
    ClientCreateSystemTemplatedefinitionTypeDef,
    ClientDeleteNamespaceResponseTypeDef,
    ClientDeploySystemInstanceResponseTypeDef,
    ClientDescribeNamespaceResponseTypeDef,
    ClientGetEntitiesResponseTypeDef,
    ClientGetFlowTemplateResponseTypeDef,
    ClientGetFlowTemplateRevisionsResponseTypeDef,
    ClientGetNamespaceDeletionStatusResponseTypeDef,
    ClientGetSystemInstanceResponseTypeDef,
    ClientGetSystemTemplateResponseTypeDef,
    ClientGetSystemTemplateRevisionsResponseTypeDef,
    ClientGetUploadStatusResponseTypeDef,
    ClientListFlowExecutionMessagesResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientSearchEntitiesResponseTypeDef,
    ClientSearchEntitiesfiltersTypeDef,
    ClientSearchFlowExecutionsResponseTypeDef,
    ClientSearchFlowTemplatesResponseTypeDef,
    ClientSearchFlowTemplatesfiltersTypeDef,
    ClientSearchSystemInstancesResponseTypeDef,
    ClientSearchSystemInstancesfiltersTypeDef,
    ClientSearchSystemTemplatesResponseTypeDef,
    ClientSearchSystemTemplatesfiltersTypeDef,
    ClientSearchThingsResponseTypeDef,
    ClientTagResourcetagsTypeDef,
    ClientUndeploySystemInstanceResponseTypeDef,
    ClientUpdateFlowTemplateResponseTypeDef,
    ClientUpdateFlowTemplatedefinitionTypeDef,
    ClientUpdateSystemTemplateResponseTypeDef,
    ClientUpdateSystemTemplatedefinitionTypeDef,
    ClientUploadEntityDefinitionsResponseTypeDef,
    ClientUploadEntityDefinitionsdocumentTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_entity_to_thing(
        self, thingName: str, entityId: str, namespaceVersion: int = None
    ) -> Dict[str, Any]:
        """
        Associates a device with a concrete thing that is in the user's registry.

        A thing can be associated with only one device at a time. If you associate a thing with a new
        device id, its previous association will be removed.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/AssociateEntityToThing>`_

        **Request Syntax**
        ::

          response = client.associate_entity_to_thing(
              thingName='string',
              entityId='string',
              namespaceVersion=123
          )
        :type thingName: string
        :param thingName: **[REQUIRED]**

          The name of the thing to which the entity is to be associated.

        :type entityId: string
        :param entityId: **[REQUIRED]**

          The ID of the device to be associated with the thing.

          The ID should be in the following format.

           ``urn:tdm:REGION/ACCOUNT ID/default:device:DEVICENAME``

        :type namespaceVersion: integer
        :param namespaceVersion:

          The version of the user's namespace. Defaults to the latest version of the user's namespace.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

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
    def create_flow_template(
        self,
        definition: ClientCreateFlowTemplatedefinitionTypeDef,
        compatibleNamespaceVersion: int = None,
    ) -> ClientCreateFlowTemplateResponseTypeDef:
        """
        Creates a workflow template. Workflows can be created only in the user's namespace. (The public
        namespace contains only entities.) The workflow can contain only entities in the specified
        namespace. The workflow is validated against the entities in the latest version of the user's
        namespace unless another namespace version is specified in the request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/CreateFlowTemplate>`_

        **Request Syntax**
        ::

          response = client.create_flow_template(
              definition={
                  'language': 'GRAPHQL',
                  'text': 'string'
              },
              compatibleNamespaceVersion=123
          )
        :type definition: dict
        :param definition: **[REQUIRED]**

          The workflow ``DefinitionDocument`` .

          - **language** *(string) --* **[REQUIRED]**

            The language used to define the entity. ``GRAPHQL`` is the only valid value.

          - **text** *(string) --* **[REQUIRED]**

            The GraphQL text that defines the entity.

        :type compatibleNamespaceVersion: integer
        :param compatibleNamespaceVersion:

          The namespace version in which the workflow is to be created.

          If no value is specified, the latest version is used by default.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'summary': {
                    'id': 'string',
                    'arn': 'string',
                    'revisionNumber': 123,
                    'createdAt': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_system_instance(
        self,
        definition: ClientCreateSystemInstancedefinitionTypeDef,
        target: str,
        tags: List[ClientCreateSystemInstancetagsTypeDef] = None,
        greengrassGroupName: str = None,
        s3BucketName: str = None,
        metricsConfiguration: ClientCreateSystemInstancemetricsConfigurationTypeDef = None,
        flowActionsRoleArn: str = None,
    ) -> ClientCreateSystemInstanceResponseTypeDef:
        """
        Creates a system instance.

        This action validates the system instance, prepares the deployment-related resources. For
        Greengrass deployments, it updates the Greengrass group that is specified by the
        ``greengrassGroupName`` parameter. It also adds a file to the S3 bucket specified by the
        ``s3BucketName`` parameter. You need to call ``DeploySystemInstance`` after running this action.

        For Greengrass deployments, since this action modifies and adds resources to a Greengrass group and
        an S3 bucket on the caller's behalf, the calling identity must have write permissions to both the
        specified Greengrass group and S3 bucket. Otherwise, the call will fail with an authorization error.

        For cloud deployments, this action requires a ``flowActionsRoleArn`` value. This is an IAM role
        that has permissions to access AWS services, such as AWS Lambda and AWS IoT, that the flow uses
        when it executes.

        If the definition document doesn't specify a version of the user's namespace, the latest version
        will be used by default.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/CreateSystemInstance>`_

        **Request Syntax**
        ::

          response = client.create_system_instance(
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ],
              definition={
                  'language': 'GRAPHQL',
                  'text': 'string'
              },
              target='GREENGRASS'|'CLOUD',
              greengrassGroupName='string',
              s3BucketName='string',
              metricsConfiguration={
                  'cloudMetricEnabled': True|False,
                  'metricRuleRoleArn': 'string'
              },
              flowActionsRoleArn='string'
          )
        :type tags: list
        :param tags:

          Metadata, consisting of key-value pairs, that can be used to categorize your system instances.

          - *(dict) --*

            Metadata assigned to an AWS IoT Things Graph resource consisting of a key-value pair.

            - **key** *(string) --* **[REQUIRED]**

              The required name of the tag. The string value can be from 1 to 128 Unicode characters in
              length.

            - **value** *(string) --* **[REQUIRED]**

              The optional value of the tag. The string value can be from 1 to 256 Unicode characters in
              length.

        :type definition: dict
        :param definition: **[REQUIRED]**

          A document that defines an entity.

          - **language** *(string) --* **[REQUIRED]**

            The language used to define the entity. ``GRAPHQL`` is the only valid value.

          - **text** *(string) --* **[REQUIRED]**

            The GraphQL text that defines the entity.

        :type target: string
        :param target: **[REQUIRED]**

          The target type of the deployment. Valid values are ``GREENGRASS`` and ``CLOUD`` .

        :type greengrassGroupName: string
        :param greengrassGroupName:

          The name of the Greengrass group where the system instance will be deployed. This value is
          required if the value of the ``target`` parameter is ``GREENGRASS`` .

        :type s3BucketName: string
        :param s3BucketName:

          The name of the Amazon Simple Storage Service bucket that will be used to store and deploy the
          system instance's resource file. This value is required if the value of the ``target`` parameter
          is ``GREENGRASS`` .

        :type metricsConfiguration: dict
        :param metricsConfiguration:

          An object that specifies whether cloud metrics are collected in a deployment and, if so, what
          role is used to collect metrics.

          - **cloudMetricEnabled** *(boolean) --*

            A Boolean that specifies whether cloud metrics are collected.

          - **metricRuleRoleArn** *(string) --*

            The ARN of the role that is used to collect cloud metrics.

        :type flowActionsRoleArn: string
        :param flowActionsRoleArn:

          The ARN of the IAM role that AWS IoT Things Graph will assume when it executes the flow. This
          role must have read and write access to AWS Lambda and AWS IoT and any other AWS services that
          the flow uses when it executes. This value is required if the value of the ``target`` parameter
          is ``CLOUD`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'summary': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_system_template(
        self,
        definition: ClientCreateSystemTemplatedefinitionTypeDef,
        compatibleNamespaceVersion: int = None,
    ) -> ClientCreateSystemTemplateResponseTypeDef:
        """
        Creates a system. The system is validated against the entities in the latest version of the user's
        namespace unless another namespace version is specified in the request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/CreateSystemTemplate>`_

        **Request Syntax**
        ::

          response = client.create_system_template(
              definition={
                  'language': 'GRAPHQL',
                  'text': 'string'
              },
              compatibleNamespaceVersion=123
          )
        :type definition: dict
        :param definition: **[REQUIRED]**

          The ``DefinitionDocument`` used to create the system.

          - **language** *(string) --* **[REQUIRED]**

            The language used to define the entity. ``GRAPHQL`` is the only valid value.

          - **text** *(string) --* **[REQUIRED]**

            The GraphQL text that defines the entity.

        :type compatibleNamespaceVersion: integer
        :param compatibleNamespaceVersion:

          The namespace version in which the system is to be created.

          If no value is specified, the latest version is used by default.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'summary': {
                    'id': 'string',
                    'arn': 'string',
                    'revisionNumber': 123,
                    'createdAt': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_flow_template(self, id: str) -> Dict[str, Any]:
        """
        Deletes a workflow. Any new system or deployment that contains this workflow will fail to update or
        deploy. Existing deployments that contain the workflow will continue to run (since they use a
        snapshot of the workflow taken at the time of deployment).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/DeleteFlowTemplate>`_

        **Request Syntax**
        ::

          response = client.delete_flow_template(
              id='string'
          )
        :type id: string
        :param id: **[REQUIRED]**

          The ID of the workflow to be deleted.

          The ID should be in the following format.

           ``urn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME``

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_namespace(
        self, *args: Any, **kwargs: Any
    ) -> ClientDeleteNamespaceResponseTypeDef:
        """
        Deletes the specified namespace. This action deletes all of the entities in the namespace. Delete
        the systems and flows that use entities in the namespace before performing this action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/DeleteNamespace>`_

        **Request Syntax**
        ::

          response = client.delete_namespace()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'namespaceArn': 'string',
                'namespaceName': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **namespaceArn** *(string) --*

              The ARN of the namespace to be deleted.

            - **namespaceName** *(string) --*

              The name of the namespace to be deleted.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_system_instance(self, id: str = None) -> Dict[str, Any]:
        """
        Deletes a system instance. Only system instances that have never been deployed, or that have been
        undeployed can be deleted.

        Users can create a new system instance that has the same ID as a deleted system instance.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/DeleteSystemInstance>`_

        **Request Syntax**
        ::

          response = client.delete_system_instance(
              id='string'
          )
        :type id: string
        :param id:

          The ID of the system instance to be deleted.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_system_template(self, id: str) -> Dict[str, Any]:
        """
        Deletes a system. New deployments can't contain the system after its deletion. Existing deployments
        that contain the system will continue to work because they use a snapshot of the system that is
        taken when it is deployed.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/DeleteSystemTemplate>`_

        **Request Syntax**
        ::

          response = client.delete_system_template(
              id='string'
          )
        :type id: string
        :param id: **[REQUIRED]**

          The ID of the system to be deleted.

          The ID should be in the following format.

           ``urn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME``

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deploy_system_instance(
        self, id: str = None
    ) -> ClientDeploySystemInstanceResponseTypeDef:
        """
         **Greengrass and Cloud Deployments**

        Deploys the system instance to the target specified in ``CreateSystemInstance`` .

         **Greengrass Deployments**

        If the system or any workflows and entities have been updated before this action is called, then
        the deployment will create a new Amazon Simple Storage Service resource file and then deploy it.

        Since this action creates a Greengrass deployment on the caller's behalf, the calling identity must
        have write permissions to the specified Greengrass group. Otherwise, the call will fail with an
        authorization error.

        For information about the artifacts that get added to your Greengrass core device when you use this
        API, see `AWS IoT Things Graph and AWS IoT Greengrass
        <https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-greengrass.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/DeploySystemInstance>`_

        **Request Syntax**
        ::

          response = client.deploy_system_instance(
              id='string'
          )
        :type id: string
        :param id:

          The ID of the system instance. This value is returned by the ``CreateSystemInstance`` action.

          The ID should be in the following format.

           ``urn:tdm:REGION/ACCOUNT ID/default:deployment:DEPLOYMENTNAME``

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'summary': {
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
                'greengrassDeploymentId': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deprecate_flow_template(self, id: str) -> Dict[str, Any]:
        """
        Deprecates the specified workflow. This action marks the workflow for deletion. Deprecated flows
        can't be deployed, but existing deployments will continue to run.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/DeprecateFlowTemplate>`_

        **Request Syntax**
        ::

          response = client.deprecate_flow_template(
              id='string'
          )
        :type id: string
        :param id: **[REQUIRED]**

          The ID of the workflow to be deleted.

          The ID should be in the following format.

           ``urn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME``

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deprecate_system_template(self, id: str) -> Dict[str, Any]:
        """
        Deprecates the specified system.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/DeprecateSystemTemplate>`_

        **Request Syntax**
        ::

          response = client.deprecate_system_template(
              id='string'
          )
        :type id: string
        :param id: **[REQUIRED]**

          The ID of the system to delete.

          The ID should be in the following format.

           ``urn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME``

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_namespace(
        self, namespaceName: str = None
    ) -> ClientDescribeNamespaceResponseTypeDef:
        """
        Gets the latest version of the user's namespace and the public version that it is tracking.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/DescribeNamespace>`_

        **Request Syntax**
        ::

          response = client.describe_namespace(
              namespaceName='string'
          )
        :type namespaceName: string
        :param namespaceName:

          The name of the user's namespace. Set this to ``aws`` to get the public namespace.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'namespaceArn': 'string',
                'namespaceName': 'string',
                'trackingNamespaceName': 'string',
                'trackingNamespaceVersion': 123,
                'namespaceVersion': 123
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def dissociate_entity_from_thing(
        self, thingName: str, entityType: str
    ) -> Dict[str, Any]:
        """
        Dissociates a device entity from a concrete thing. The action takes only the type of the entity
        that you need to dissociate because only one entity of a particular type can be associated with a
        thing.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/DissociateEntityFromThing>`_

        **Request Syntax**
        ::

          response = client.dissociate_entity_from_thing(
              thingName='string',
              entityType=
                  'DEVICE'|'SERVICE'|'DEVICE_MODEL'|'CAPABILITY'|'STATE'|'ACTION'|'EVENT'|'PROPERTY'
                  |'MAPPING'|'ENUM'
          )
        :type thingName: string
        :param thingName: **[REQUIRED]**

          The name of the thing to disassociate.

        :type entityType: string
        :param entityType: **[REQUIRED]**

          The entity type from which to disassociate the thing.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
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
    def get_entities(
        self, ids: List[str], namespaceVersion: int = None
    ) -> ClientGetEntitiesResponseTypeDef:
        """
        Gets definitions of the specified entities. Uses the latest version of the user's namespace by
        default. This API returns the following TDM entities.

        * Properties

        * States

        * Events

        * Actions

        * Capabilities

        * Mappings

        * Devices

        * Device Models

        * Services

        This action doesn't return definitions for systems, flows, and deployments.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/GetEntities>`_

        **Request Syntax**
        ::

          response = client.get_entities(
              ids=[
                  'string',
              ],
              namespaceVersion=123
          )
        :type ids: list
        :param ids: **[REQUIRED]**

          An array of entity IDs.

          The IDs should be in the following format.

           ``urn:tdm:REGION/ACCOUNT ID/default:device:DEVICENAME``

          - *(string) --*

        :type namespaceVersion: integer
        :param namespaceVersion:

          The version of the user's namespace. Defaults to the latest version of the user's namespace.

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
                ]
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_flow_template(
        self, id: str, revisionNumber: int = None
    ) -> ClientGetFlowTemplateResponseTypeDef:
        """
        Gets the latest version of the ``DefinitionDocument`` and ``FlowTemplateSummary`` for the specified
        workflow.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/GetFlowTemplate>`_

        **Request Syntax**
        ::

          response = client.get_flow_template(
              id='string',
              revisionNumber=123
          )
        :type id: string
        :param id: **[REQUIRED]**

          The ID of the workflow.

          The ID should be in the following format.

           ``urn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME``

        :type revisionNumber: integer
        :param revisionNumber:

          The number of the workflow revision to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'description': {
                    'summary': {
                        'id': 'string',
                        'arn': 'string',
                        'revisionNumber': 123,
                        'createdAt': datetime(2015, 1, 1)
                    },
                    'definition': {
                        'language': 'GRAPHQL',
                        'text': 'string'
                    },
                    'validatedNamespaceVersion': 123
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_flow_template_revisions(
        self, id: str, nextToken: str = None, maxResults: int = None
    ) -> ClientGetFlowTemplateRevisionsResponseTypeDef:
        """
        Gets revisions of the specified workflow. Only the last 100 revisions are stored. If the workflow
        has been deprecated, this action will return revisions that occurred before the deprecation. This
        action won't work for workflows that have been deleted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/GetFlowTemplateRevisions>`_

        **Request Syntax**
        ::

          response = client.get_flow_template_revisions(
              id='string',
              nextToken='string',
              maxResults=123
          )
        :type id: string
        :param id: **[REQUIRED]**

          The ID of the workflow.

          The ID should be in the following format.

           ``urn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME``

        :type nextToken: string
        :param nextToken:

          The string that specifies the next page of results. Use this when you're paginating results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return in the response.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              The string to specify as ``nextToken`` when you request the next page of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_namespace_deletion_status(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetNamespaceDeletionStatusResponseTypeDef:
        """
        Gets the status of a namespace deletion task.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/GetNamespaceDeletionStatus>`_

        **Request Syntax**
        ::

          response = client.get_namespace_deletion_status()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'namespaceArn': 'string',
                'namespaceName': 'string',
                'status': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
                'errorCode': 'VALIDATION_FAILED',
                'errorMessage': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_system_instance(self, id: str) -> ClientGetSystemInstanceResponseTypeDef:
        """
        Gets a system instance.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/GetSystemInstance>`_

        **Request Syntax**
        ::

          response = client.get_system_instance(
              id='string'
          )
        :type id: string
        :param id: **[REQUIRED]**

          The ID of the system deployment instance. This value is returned by ``CreateSystemInstance`` .

          The ID should be in the following format.

           ``urn:tdm:REGION/ACCOUNT ID/default:deployment:DEPLOYMENTNAME``

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'description': {
                    'summary': {
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
                    'definition': {
                        'language': 'GRAPHQL',
                        'text': 'string'
                    },
                    's3BucketName': 'string',
                    'metricsConfiguration': {
                        'cloudMetricEnabled': True|False,
                        'metricRuleRoleArn': 'string'
                    },
                    'validatedNamespaceVersion': 123,
                    'validatedDependencyRevisions': [
                        {
                            'id': 'string',
                            'revisionNumber': 123
                        },
                    ],
                    'flowActionsRoleArn': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_system_template(
        self, id: str, revisionNumber: int = None
    ) -> ClientGetSystemTemplateResponseTypeDef:
        """
        Gets a system.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/GetSystemTemplate>`_

        **Request Syntax**
        ::

          response = client.get_system_template(
              id='string',
              revisionNumber=123
          )
        :type id: string
        :param id: **[REQUIRED]**

          The ID of the system to get. This ID must be in the user's namespace.

          The ID should be in the following format.

           ``urn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME``

        :type revisionNumber: integer
        :param revisionNumber:

          The number that specifies the revision of the system to get.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'description': {
                    'summary': {
                        'id': 'string',
                        'arn': 'string',
                        'revisionNumber': 123,
                        'createdAt': datetime(2015, 1, 1)
                    },
                    'definition': {
                        'language': 'GRAPHQL',
                        'text': 'string'
                    },
                    'validatedNamespaceVersion': 123
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_system_template_revisions(
        self, id: str, nextToken: str = None, maxResults: int = None
    ) -> ClientGetSystemTemplateRevisionsResponseTypeDef:
        """
        Gets revisions made to the specified system template. Only the previous 100 revisions are stored.
        If the system has been deprecated, this action will return the revisions that occurred before its
        deprecation. This action won't work with systems that have been deleted.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/GetSystemTemplateRevisions>`_

        **Request Syntax**
        ::

          response = client.get_system_template_revisions(
              id='string',
              nextToken='string',
              maxResults=123
          )
        :type id: string
        :param id: **[REQUIRED]**

          The ID of the system template.

          The ID should be in the following format.

           ``urn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME``

        :type nextToken: string
        :param nextToken:

          The string that specifies the next page of results. Use this when you're paginating results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return in the response.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              The string to specify as ``nextToken`` when you request the next page of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_upload_status(self, uploadId: str) -> ClientGetUploadStatusResponseTypeDef:
        """
        Gets the status of the specified upload.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/GetUploadStatus>`_

        **Request Syntax**
        ::

          response = client.get_upload_status(
              uploadId='string'
          )
        :type uploadId: string
        :param uploadId: **[REQUIRED]**

          The ID of the upload. This value is returned by the ``UploadEntityDefinitions`` action.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'uploadId': 'string',
                'uploadStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
                'namespaceArn': 'string',
                'namespaceName': 'string',
                'namespaceVersion': 123,
                'failureReason': [
                    'string',
                ],
                'createdDate': datetime(2015, 1, 1)
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_flow_execution_messages(
        self, flowExecutionId: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListFlowExecutionMessagesResponseTypeDef:
        """
        Returns a list of objects that contain information about events in a flow execution.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/ListFlowExecutionMessages>`_

        **Request Syntax**
        ::

          response = client.list_flow_execution_messages(
              flowExecutionId='string',
              nextToken='string',
              maxResults=123
          )
        :type flowExecutionId: string
        :param flowExecutionId: **[REQUIRED]**

          The ID of the flow execution.

        :type nextToken: string
        :param nextToken:

          The string that specifies the next page of results. Use this when you're paginating results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return in the response.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              The string to specify as ``nextToken`` when you request the next page of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, resourceArn: str, maxResults: int = None, nextToken: str = None
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Lists all tags on an AWS IoT Things Graph resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              maxResults=123,
              resourceArn='string',
              nextToken='string'
          )
        :type maxResults: integer
        :param maxResults:

          The maximum number of tags to return.

        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource whose tags are to be returned.

        :type nextToken: string
        :param nextToken:

          The token that specifies the next page of results to return.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              The token that specifies the next page of results to return.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_entities(
        self,
        entityTypes: List[str],
        filters: List[ClientSearchEntitiesfiltersTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
        namespaceVersion: int = None,
    ) -> ClientSearchEntitiesResponseTypeDef:
        """
        Searches for entities of the specified type. You can search for entities in your namespace and the
        public namespace that you're tracking.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/SearchEntities>`_

        **Request Syntax**
        ::

          response = client.search_entities(
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
              nextToken='string',
              maxResults=123,
              namespaceVersion=123
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

        :type nextToken: string
        :param nextToken:

          The string that specifies the next page of results. Use this when you're paginating results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return in the response.

        :type namespaceVersion: integer
        :param namespaceVersion:

          The version of the user's namespace. Defaults to the latest version of the user's namespace.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              The string to specify as ``nextToken`` when you request the next page of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_flow_executions(
        self,
        systemInstanceId: str,
        flowExecutionId: str = None,
        startTime: datetime = None,
        endTime: datetime = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientSearchFlowExecutionsResponseTypeDef:
        """
        Searches for AWS IoT Things Graph workflow execution instances.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/SearchFlowExecutions>`_

        **Request Syntax**
        ::

          response = client.search_flow_executions(
              systemInstanceId='string',
              flowExecutionId='string',
              startTime=datetime(2015, 1, 1),
              endTime=datetime(2015, 1, 1),
              nextToken='string',
              maxResults=123
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

        :type nextToken: string
        :param nextToken:

          The string that specifies the next page of results. Use this when you're paginating results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return in the response.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              The string to specify as ``nextToken`` when you request the next page of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_flow_templates(
        self,
        filters: List[ClientSearchFlowTemplatesfiltersTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientSearchFlowTemplatesResponseTypeDef:
        """
        Searches for summary information about workflows.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/SearchFlowTemplates>`_

        **Request Syntax**
        ::

          response = client.search_flow_templates(
              filters=[
                  {
                      'name': 'DEVICE_MODEL_ID',
                      'value': [
                          'string',
                      ]
                  },
              ],
              nextToken='string',
              maxResults=123
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

        :type nextToken: string
        :param nextToken:

          The string that specifies the next page of results. Use this when you're paginating results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return in the response.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              The string to specify as ``nextToken`` when you request the next page of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_system_instances(
        self,
        filters: List[ClientSearchSystemInstancesfiltersTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientSearchSystemInstancesResponseTypeDef:
        """
        Searches for system instances in the user's account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/SearchSystemInstances>`_

        **Request Syntax**
        ::

          response = client.search_system_instances(
              filters=[
                  {
                      'name': 'SYSTEM_TEMPLATE_ID'|'STATUS'|'GREENGRASS_GROUP_NAME',
                      'value': [
                          'string',
                      ]
                  },
              ],
              nextToken='string',
              maxResults=123
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

        :type nextToken: string
        :param nextToken:

          The string that specifies the next page of results. Use this when you're paginating results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return in the response.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              The string to specify as ``nextToken`` when you request the next page of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_system_templates(
        self,
        filters: List[ClientSearchSystemTemplatesfiltersTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientSearchSystemTemplatesResponseTypeDef:
        """
        Searches for summary information about systems in the user's account. You can filter by the ID of a
        workflow to return only systems that use the specified workflow.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/SearchSystemTemplates>`_

        **Request Syntax**
        ::

          response = client.search_system_templates(
              filters=[
                  {
                      'name': 'FLOW_TEMPLATE_ID',
                      'value': [
                          'string',
                      ]
                  },
              ],
              nextToken='string',
              maxResults=123
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

        :type nextToken: string
        :param nextToken:

          The string that specifies the next page of results. Use this when you're paginating results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return in the response.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              The string to specify as ``nextToken`` when you request the next page of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def search_things(
        self,
        entityId: str,
        nextToken: str = None,
        maxResults: int = None,
        namespaceVersion: int = None,
    ) -> ClientSearchThingsResponseTypeDef:
        """
        Searches for things associated with the specified entity. You can search by both device and device
        model.

        For example, if two different devices, camera1 and camera2, implement the camera device model, the
        user can associate thing1 to camera1 and thing2 to camera2. ``SearchThings(camera2)`` will return
        only thing2, but ``SearchThings(camera)`` will return both thing1 and thing2.

        This action searches for exact matches and doesn't perform partial text matching.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/SearchThings>`_

        **Request Syntax**
        ::

          response = client.search_things(
              entityId='string',
              nextToken='string',
              maxResults=123,
              namespaceVersion=123
          )
        :type entityId: string
        :param entityId: **[REQUIRED]**

          The ID of the entity to which the things are associated.

          The IDs should be in the following format.

           ``urn:tdm:REGION/ACCOUNT ID/default:device:DEVICENAME``

        :type nextToken: string
        :param nextToken:

          The string that specifies the next page of results. Use this when you're paginating results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return in the response.

        :type namespaceVersion: integer
        :param namespaceVersion:

          The version of the user's namespace. Defaults to the latest version of the user's namespace.

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
                'nextToken': 'string'
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

            - **nextToken** *(string) --*

              The string to specify as ``nextToken`` when you request the next page of results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(
        self, resourceArn: str, tags: List[ClientTagResourcetagsTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a tag for the specified resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/TagResource>`_

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

          The Amazon Resource Name (ARN) of the resource whose tags are returned.

        :type tags: list
        :param tags: **[REQUIRED]**

          A list of tags to add to the resource.>

          - *(dict) --*

            Metadata assigned to an AWS IoT Things Graph resource consisting of a key-value pair.

            - **key** *(string) --* **[REQUIRED]**

              The required name of the tag. The string value can be from 1 to 128 Unicode characters in
              length.

            - **value** *(string) --* **[REQUIRED]**

              The optional value of the tag. The string value can be from 1 to 256 Unicode characters in
              length.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def undeploy_system_instance(
        self, id: str = None
    ) -> ClientUndeploySystemInstanceResponseTypeDef:
        """
        Removes a system instance from its target (Cloud or Greengrass).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/UndeploySystemInstance>`_

        **Request Syntax**
        ::

          response = client.undeploy_system_instance(
              id='string'
          )
        :type id: string
        :param id:

          The ID of the system instance to remove from its target.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'summary': {
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
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag from the specified resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/UntagResource>`_

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

          The Amazon Resource Name (ARN) of the resource whose tags are to be removed.

        :type tagKeys: list
        :param tagKeys: **[REQUIRED]**

          A list of tag key names to remove from the resource. You don't specify the value. Both the key
          and its associated value are removed.

          This parameter to the API requires a JSON text string argument. For information on how to format
          a JSON parameter for the various command line tool environments, see `Using JSON for Parameters
          <https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters.html#cli-using-param-json>`__
          in the *AWS CLI User Guide* .

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
    def update_flow_template(
        self,
        id: str,
        definition: ClientUpdateFlowTemplatedefinitionTypeDef,
        compatibleNamespaceVersion: int = None,
    ) -> ClientUpdateFlowTemplateResponseTypeDef:
        """
        Updates the specified workflow. All deployed systems and system instances that use the workflow
        will see the changes in the flow when it is redeployed. If you don't want this behavior, copy the
        workflow (creating a new workflow with a different ID), and update the copy. The workflow can
        contain only entities in the specified namespace.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/UpdateFlowTemplate>`_

        **Request Syntax**
        ::

          response = client.update_flow_template(
              id='string',
              definition={
                  'language': 'GRAPHQL',
                  'text': 'string'
              },
              compatibleNamespaceVersion=123
          )
        :type id: string
        :param id: **[REQUIRED]**

          The ID of the workflow to be updated.

          The ID should be in the following format.

           ``urn:tdm:REGION/ACCOUNT ID/default:workflow:WORKFLOWNAME``

        :type definition: dict
        :param definition: **[REQUIRED]**

          The ``DefinitionDocument`` that contains the updated workflow definition.

          - **language** *(string) --* **[REQUIRED]**

            The language used to define the entity. ``GRAPHQL`` is the only valid value.

          - **text** *(string) --* **[REQUIRED]**

            The GraphQL text that defines the entity.

        :type compatibleNamespaceVersion: integer
        :param compatibleNamespaceVersion:

          The version of the user's namespace.

          If no value is specified, the latest version is used by default. Use the
          ``GetFlowTemplateRevisions`` if you want to find earlier revisions of the flow to update.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'summary': {
                    'id': 'string',
                    'arn': 'string',
                    'revisionNumber': 123,
                    'createdAt': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_system_template(
        self,
        id: str,
        definition: ClientUpdateSystemTemplatedefinitionTypeDef,
        compatibleNamespaceVersion: int = None,
    ) -> ClientUpdateSystemTemplateResponseTypeDef:
        """
        Updates the specified system. You don't need to run this action after updating a workflow. Any
        deployment that uses the system will see the changes in the system when it is redeployed.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/UpdateSystemTemplate>`_

        **Request Syntax**
        ::

          response = client.update_system_template(
              id='string',
              definition={
                  'language': 'GRAPHQL',
                  'text': 'string'
              },
              compatibleNamespaceVersion=123
          )
        :type id: string
        :param id: **[REQUIRED]**

          The ID of the system to be updated.

          The ID should be in the following format.

           ``urn:tdm:REGION/ACCOUNT ID/default:system:SYSTEMNAME``

        :type definition: dict
        :param definition: **[REQUIRED]**

          The ``DefinitionDocument`` that contains the updated system definition.

          - **language** *(string) --* **[REQUIRED]**

            The language used to define the entity. ``GRAPHQL`` is the only valid value.

          - **text** *(string) --* **[REQUIRED]**

            The GraphQL text that defines the entity.

        :type compatibleNamespaceVersion: integer
        :param compatibleNamespaceVersion:

          The version of the user's namespace. Defaults to the latest version of the user's namespace.

          If no value is specified, the latest version is used by default.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'summary': {
                    'id': 'string',
                    'arn': 'string',
                    'revisionNumber': 123,
                    'createdAt': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upload_entity_definitions(
        self,
        document: ClientUploadEntityDefinitionsdocumentTypeDef = None,
        syncWithPublicNamespace: bool = None,
        deprecateExistingEntities: bool = None,
    ) -> ClientUploadEntityDefinitionsResponseTypeDef:
        """
        Asynchronously uploads one or more entity definitions to the user's namespace. The ``document``
        parameter is required if ``syncWithPublicNamespace`` and ``deleteExistingEntites`` are false. If
        the ``syncWithPublicNamespace`` parameter is set to ``true`` , the user's namespace will
        synchronize with the latest version of the public namespace. If ``deprecateExistingEntities`` is
        set to true, all entities in the latest version will be deleted before the new
        ``DefinitionDocument`` is uploaded.

        When a user uploads entity definitions for the first time, the service creates a new namespace for
        the user. The new namespace tracks the public namespace. Currently users can have only one
        namespace. The namespace version increments whenever a user uploads entity definitions that are
        backwards-incompatible and whenever a user sets the ``syncWithPublicNamespace`` parameter or the
        ``deprecateExistingEntities`` parameter to ``true`` .

        The IDs for all of the entities should be in URN format. Each entity must be in the user's
        namespace. Users can't create entities in the public namespace, but entity definitions can refer to
        entities in the public namespace.

        Valid entities are ``Device`` , ``DeviceModel`` , ``Service`` , ``Capability`` , ``State`` ,
        ``Action`` , ``Event`` , ``Property`` , ``Mapping`` , ``Enum`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iotthingsgraph-2018-09-06/UploadEntityDefinitions>`_

        **Request Syntax**
        ::

          response = client.upload_entity_definitions(
              document={
                  'language': 'GRAPHQL',
                  'text': 'string'
              },
              syncWithPublicNamespace=True|False,
              deprecateExistingEntities=True|False
          )
        :type document: dict
        :param document:

          The ``DefinitionDocument`` that defines the updated entities.

          - **language** *(string) --* **[REQUIRED]**

            The language used to define the entity. ``GRAPHQL`` is the only valid value.

          - **text** *(string) --* **[REQUIRED]**

            The GraphQL text that defines the entity.

        :type syncWithPublicNamespace: boolean
        :param syncWithPublicNamespace:

          A Boolean that specifies whether to synchronize with the latest version of the public namespace.
          If set to ``true`` , the upload will create a new namespace version.

        :type deprecateExistingEntities: boolean
        :param deprecateExistingEntities:

          A Boolean that specifies whether to deprecate all entities in the latest version before uploading
          the new ``DefinitionDocument`` . If set to ``true`` , the upload will create a new namespace
          version.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'uploadId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **uploadId** *(string) --*

              The ID that specifies the upload action. You can use this to track the status of the upload.

        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_flow_template_revisions"]
    ) -> paginator_scope.GetFlowTemplateRevisionsPaginator:
        """
        Get Paginator for `get_flow_template_revisions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_system_template_revisions"]
    ) -> paginator_scope.GetSystemTemplateRevisionsPaginator:
        """
        Get Paginator for `get_system_template_revisions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_flow_execution_messages"]
    ) -> paginator_scope.ListFlowExecutionMessagesPaginator:
        """
        Get Paginator for `list_flow_execution_messages` operation.
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
        self, operation_name: Literal["search_entities"]
    ) -> paginator_scope.SearchEntitiesPaginator:
        """
        Get Paginator for `search_entities` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["search_flow_executions"]
    ) -> paginator_scope.SearchFlowExecutionsPaginator:
        """
        Get Paginator for `search_flow_executions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["search_flow_templates"]
    ) -> paginator_scope.SearchFlowTemplatesPaginator:
        """
        Get Paginator for `search_flow_templates` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["search_system_instances"]
    ) -> paginator_scope.SearchSystemInstancesPaginator:
        """
        Get Paginator for `search_system_instances` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["search_system_templates"]
    ) -> paginator_scope.SearchSystemTemplatesPaginator:
        """
        Get Paginator for `search_system_templates` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["search_things"]
    ) -> paginator_scope.SearchThingsPaginator:
        """
        Get Paginator for `search_things` operation.
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
    InternalFailureException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ThrottlingException: Boto3ClientError

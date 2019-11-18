"Main interface for dms Client"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from typing_extensions import Literal, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

# pylint: disable=import-self
import mypy_boto3_dms.client as client_scope

# pylint: disable=import-self
import mypy_boto3_dms.paginator as paginator_scope
from mypy_boto3_dms.type_defs import (
    ClientAddTagsToResourceTagsTypeDef,
    ClientApplyPendingMaintenanceActionResponseTypeDef,
    ClientCreateEndpointDmsTransferSettingsTypeDef,
    ClientCreateEndpointDynamoDbSettingsTypeDef,
    ClientCreateEndpointElasticsearchSettingsTypeDef,
    ClientCreateEndpointKinesisSettingsTypeDef,
    ClientCreateEndpointMongoDbSettingsTypeDef,
    ClientCreateEndpointRedshiftSettingsTypeDef,
    ClientCreateEndpointResponseTypeDef,
    ClientCreateEndpointS3SettingsTypeDef,
    ClientCreateEndpointTagsTypeDef,
    ClientCreateEventSubscriptionResponseTypeDef,
    ClientCreateEventSubscriptionTagsTypeDef,
    ClientCreateReplicationInstanceResponseTypeDef,
    ClientCreateReplicationInstanceTagsTypeDef,
    ClientCreateReplicationSubnetGroupResponseTypeDef,
    ClientCreateReplicationSubnetGroupTagsTypeDef,
    ClientCreateReplicationTaskTagsTypeDef,
    ClientDeleteCertificateResponseTypeDef,
    ClientDeleteConnectionResponseTypeDef,
    ClientDeleteEndpointResponseTypeDef,
    ClientDeleteEventSubscriptionResponseTypeDef,
    ClientDeleteReplicationInstanceResponseTypeDef,
    ClientDescribeAccountAttributesResponseTypeDef,
    ClientDescribeCertificatesFiltersTypeDef,
    ClientDescribeCertificatesResponseTypeDef,
    ClientDescribeConnectionsFiltersTypeDef,
    ClientDescribeConnectionsResponseTypeDef,
    ClientDescribeEndpointTypesFiltersTypeDef,
    ClientDescribeEndpointTypesResponseTypeDef,
    ClientDescribeEndpointsFiltersTypeDef,
    ClientDescribeEndpointsResponseTypeDef,
    ClientDescribeEventCategoriesFiltersTypeDef,
    ClientDescribeEventCategoriesResponseTypeDef,
    ClientDescribeEventSubscriptionsFiltersTypeDef,
    ClientDescribeEventSubscriptionsResponseTypeDef,
    ClientDescribeEventsFiltersTypeDef,
    ClientDescribeEventsResponseTypeDef,
    ClientDescribeOrderableReplicationInstancesResponseTypeDef,
    ClientDescribePendingMaintenanceActionsFiltersTypeDef,
    ClientDescribePendingMaintenanceActionsResponseTypeDef,
    ClientDescribeRefreshSchemasStatusResponseTypeDef,
    ClientDescribeReplicationInstanceTaskLogsResponseTypeDef,
    ClientDescribeReplicationInstancesFiltersTypeDef,
    ClientDescribeReplicationInstancesResponseTypeDef,
    ClientDescribeReplicationSubnetGroupsFiltersTypeDef,
    ClientDescribeReplicationSubnetGroupsResponseTypeDef,
    ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef,
    ClientDescribeReplicationTasksFiltersTypeDef,
    ClientDescribeSchemasResponseTypeDef,
    ClientDescribeTableStatisticsFiltersTypeDef,
    ClientDescribeTableStatisticsResponseTypeDef,
    ClientImportCertificateResponseTypeDef,
    ClientImportCertificateTagsTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientModifyEndpointDmsTransferSettingsTypeDef,
    ClientModifyEndpointDynamoDbSettingsTypeDef,
    ClientModifyEndpointElasticsearchSettingsTypeDef,
    ClientModifyEndpointKinesisSettingsTypeDef,
    ClientModifyEndpointMongoDbSettingsTypeDef,
    ClientModifyEndpointRedshiftSettingsTypeDef,
    ClientModifyEndpointResponseTypeDef,
    ClientModifyEndpointS3SettingsTypeDef,
    ClientModifyEventSubscriptionResponseTypeDef,
    ClientModifyReplicationInstanceResponseTypeDef,
    ClientModifyReplicationSubnetGroupResponseTypeDef,
    ClientRebootReplicationInstanceResponseTypeDef,
    ClientRefreshSchemasResponseTypeDef,
    ClientReloadTablesResponseTypeDef,
    ClientReloadTablesTablesToReloadTypeDef,
    ClientTestConnectionResponseTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_dms.waiter as waiter_scope


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags_to_resource(
        self, ResourceArn: str, Tags: List[ClientAddTagsToResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds metadata tags to an AWS DMS resource, including replication instance, endpoint, security
        group, and migration task. These tags can also be used with cost allocation reporting to track cost
        associated with DMS resources, or used in a Condition statement in an IAM policy for DMS.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/AddTagsToResource>`_

        **Request Syntax**
        ::

          response = client.add_tags_to_resource(
              ResourceArn='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          Identifies the AWS DMS resource to which tags should be added. The value for this parameter is an
          Amazon Resource Name (ARN).

          For AWS DMS, you can tag a replication instance, an endpoint, or a replication task.

        :type Tags: list
        :param Tags: **[REQUIRED]**

          One or more tags to be assigned to the resource.

          - *(dict) --*

            - **Key** *(string) --*

              A key is the required name of the tag. The string value can be from 1 to 128 Unicode
              characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
              contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
              (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

            - **Value** *(string) --*

              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
              characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
              contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
              (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def apply_pending_maintenance_action(
        self, ReplicationInstanceArn: str, ApplyAction: str, OptInType: str
    ) -> ClientApplyPendingMaintenanceActionResponseTypeDef:
        """
        Applies a pending maintenance action to a resource (for example, to a replication instance).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ApplyPendingMaintenanceAction>`_

        **Request Syntax**
        ::

          response = client.apply_pending_maintenance_action(
              ReplicationInstanceArn='string',
              ApplyAction='string',
              OptInType='string'
          )
        :type ReplicationInstanceArn: string
        :param ReplicationInstanceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the AWS DMS resource that the pending maintenance action
          applies to.

        :type ApplyAction: string
        :param ApplyAction: **[REQUIRED]**

          The pending maintenance action to apply to this resource.

        :type OptInType: string
        :param OptInType: **[REQUIRED]**

          A value that specifies the type of opt-in request, or undoes an opt-in request. You can't undo an
          opt-in request of type ``immediate`` .

          Valid values:

          * ``immediate`` - Apply the maintenance action immediately.

          * ``next-maintenance`` - Apply the maintenance action during the next maintenance window for the
          resource.

          * ``undo-opt-in`` - Cancel any existing ``next-maintenance`` opt-in requests.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResourcePendingMaintenanceActions': {
                    'ResourceIdentifier': 'string',
                    'PendingMaintenanceActionDetails': [
                        {
                            'Action': 'string',
                            'AutoAppliedAfterDate': datetime(2015, 1, 1),
                            'ForcedApplyDate': datetime(2015, 1, 1),
                            'OptInStatus': 'string',
                            'CurrentApplyDate': datetime(2015, 1, 1),
                            'Description': 'string'
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ResourcePendingMaintenanceActions** *(dict) --*

              The AWS DMS resource that the pending maintenance action will be applied to.

              - **ResourceIdentifier** *(string) --*

                The Amazon Resource Name (ARN) of the DMS resource that the pending maintenance action
                applies to. For information about creating an ARN, see `Constructing an Amazon Resource
                Name (ARN) for AWS DMS
                <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.AWS.ARN.html>`__ in the
                DMS documentation.

              - **PendingMaintenanceActionDetails** *(list) --*

                Detailed information about the pending maintenance action.

                - *(dict) --*

                  - **Action** *(string) --*

                    The type of pending maintenance action that is available for the resource.

                  - **AutoAppliedAfterDate** *(datetime) --*

                    The date of the maintenance window when the action will be applied. The maintenance
                    action will be applied to the resource during its first maintenance window after this
                    date. If this date is specified, any ``next-maintenance`` opt-in requests are ignored.

                  - **ForcedApplyDate** *(datetime) --*

                    The date when the maintenance action will be automatically applied. The maintenance
                    action will be applied to the resource on this date regardless of the maintenance
                    window for the resource. If this date is specified, any ``immediate`` opt-in requests
                    are ignored.

                  - **OptInStatus** *(string) --*

                    Indicates the type of opt-in request that has been received for the resource.

                  - **CurrentApplyDate** *(datetime) --*

                    The effective date when the pending maintenance action will be applied to the resource.
                    This date takes into account opt-in requests received from the
                    ``ApplyPendingMaintenanceAction`` API, the ``AutoAppliedAfterDate`` , and the
                    ``ForcedApplyDate`` . This value is blank if an opt-in request has not been received
                    and nothing has been specified as ``AutoAppliedAfterDate`` or ``ForcedApplyDate`` .

                  - **Description** *(string) --*

                    A description providing more detail about the maintenance action.

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
    def create_endpoint(
        self,
        EndpointIdentifier: str,
        EndpointType: str,
        EngineName: str,
        Username: str = None,
        Password: str = None,
        ServerName: str = None,
        Port: int = None,
        DatabaseName: str = None,
        ExtraConnectionAttributes: str = None,
        KmsKeyId: str = None,
        Tags: List[ClientCreateEndpointTagsTypeDef] = None,
        CertificateArn: str = None,
        SslMode: str = None,
        ServiceAccessRoleArn: str = None,
        ExternalTableDefinition: str = None,
        DynamoDbSettings: ClientCreateEndpointDynamoDbSettingsTypeDef = None,
        S3Settings: ClientCreateEndpointS3SettingsTypeDef = None,
        DmsTransferSettings: ClientCreateEndpointDmsTransferSettingsTypeDef = None,
        MongoDbSettings: ClientCreateEndpointMongoDbSettingsTypeDef = None,
        KinesisSettings: ClientCreateEndpointKinesisSettingsTypeDef = None,
        ElasticsearchSettings: ClientCreateEndpointElasticsearchSettingsTypeDef = None,
        RedshiftSettings: ClientCreateEndpointRedshiftSettingsTypeDef = None,
    ) -> ClientCreateEndpointResponseTypeDef:
        """
        Creates an endpoint using the provided settings.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/CreateEndpoint>`_

        **Request Syntax**
        ::

          response = client.create_endpoint(
              EndpointIdentifier='string',
              EndpointType='source'|'target',
              EngineName='string',
              Username='string',
              Password='string',
              ServerName='string',
              Port=123,
              DatabaseName='string',
              ExtraConnectionAttributes='string',
              KmsKeyId='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              CertificateArn='string',
              SslMode='none'|'require'|'verify-ca'|'verify-full',
              ServiceAccessRoleArn='string',
              ExternalTableDefinition='string',
              DynamoDbSettings={
                  'ServiceAccessRoleArn': 'string'
              },
              S3Settings={
                  'ServiceAccessRoleArn': 'string',
                  'ExternalTableDefinition': 'string',
                  'CsvRowDelimiter': 'string',
                  'CsvDelimiter': 'string',
                  'BucketFolder': 'string',
                  'BucketName': 'string',
                  'CompressionType': 'none'|'gzip',
                  'EncryptionMode': 'sse-s3'|'sse-kms',
                  'ServerSideEncryptionKmsKeyId': 'string',
                  'DataFormat': 'csv'|'parquet',
                  'EncodingType': 'plain'|'plain-dictionary'|'rle-dictionary',
                  'DictPageSizeLimit': 123,
                  'RowGroupLength': 123,
                  'DataPageSize': 123,
                  'ParquetVersion': 'parquet-1-0'|'parquet-2-0',
                  'EnableStatistics': True|False,
                  'IncludeOpForFullLoad': True|False,
                  'CdcInsertsOnly': True|False,
                  'TimestampColumnName': 'string',
                  'ParquetTimestampInMillisecond': True|False
              },
              DmsTransferSettings={
                  'ServiceAccessRoleArn': 'string',
                  'BucketName': 'string'
              },
              MongoDbSettings={
                  'Username': 'string',
                  'Password': 'string',
                  'ServerName': 'string',
                  'Port': 123,
                  'DatabaseName': 'string',
                  'AuthType': 'no'|'password',
                  'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
                  'NestingLevel': 'none'|'one',
                  'ExtractDocId': 'string',
                  'DocsToInvestigate': 'string',
                  'AuthSource': 'string',
                  'KmsKeyId': 'string'
              },
              KinesisSettings={
                  'StreamArn': 'string',
                  'MessageFormat': 'json',
                  'ServiceAccessRoleArn': 'string'
              },
              ElasticsearchSettings={
                  'ServiceAccessRoleArn': 'string',
                  'EndpointUri': 'string',
                  'FullLoadErrorPercentage': 123,
                  'ErrorRetryDuration': 123
              },
              RedshiftSettings={
                  'AcceptAnyDate': True|False,
                  'AfterConnectScript': 'string',
                  'BucketFolder': 'string',
                  'BucketName': 'string',
                  'ConnectionTimeout': 123,
                  'DatabaseName': 'string',
                  'DateFormat': 'string',
                  'EmptyAsNull': True|False,
                  'EncryptionMode': 'sse-s3'|'sse-kms',
                  'FileTransferUploadStreams': 123,
                  'LoadTimeout': 123,
                  'MaxFileSize': 123,
                  'Password': 'string',
                  'Port': 123,
                  'RemoveQuotes': True|False,
                  'ReplaceInvalidChars': 'string',
                  'ReplaceChars': 'string',
                  'ServerName': 'string',
                  'ServiceAccessRoleArn': 'string',
                  'ServerSideEncryptionKmsKeyId': 'string',
                  'TimeFormat': 'string',
                  'TrimBlanks': True|False,
                  'TruncateColumns': True|False,
                  'Username': 'string',
                  'WriteBufferSize': 123
              }
          )
        :type EndpointIdentifier: string
        :param EndpointIdentifier: **[REQUIRED]**

          The database endpoint identifier. Identifiers must begin with a letter; must contain only ASCII
          letters, digits, and hyphens; and must not end with a hyphen or contain two consecutive hyphens.

        :type EndpointType: string
        :param EndpointType: **[REQUIRED]**

          The type of endpoint. Valid values are ``source`` and ``target`` .

        :type EngineName: string
        :param EngineName: **[REQUIRED]**

          The type of engine for the endpoint. Valid values, depending on the ``EndpointType`` value,
          include ``mysql`` , ``oracle`` , ``postgres`` , ``mariadb`` , ``aurora`` , ``aurora-postgresql``
          , ``redshift`` , ``s3`` , ``db2`` , ``azuredb`` , ``sybase`` , ``dynamodb`` , ``mongodb`` , and
          ``sqlserver`` .

        :type Username: string
        :param Username:

          The user name to be used to log in to the endpoint database.

        :type Password: string
        :param Password:

          The password to be used to log in to the endpoint database.

        :type ServerName: string
        :param ServerName:

          The name of the server where the endpoint database resides.

        :type Port: integer
        :param Port:

          The port used by the endpoint database.

        :type DatabaseName: string
        :param DatabaseName:

          The name of the endpoint database.

        :type ExtraConnectionAttributes: string
        :param ExtraConnectionAttributes:

          Additional attributes associated with the connection. Each attribute is specified as a name-value
          pair associated by an equal sign (=). Multiple attributes are separated by a semicolon (;) with
          no additional white space. For information on the attributes available for connecting your source
          or target endpoint, see `Working with AWS DMS Endpoints
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html>`__ in the *AWS Database
          Migration Service User Guide.*

        :type KmsKeyId: string
        :param KmsKeyId:

          An AWS KMS key identifier that is used to encrypt the connection parameters for the endpoint.

          If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
          encryption key.

          AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different
          default encryption key for each AWS Region.

        :type Tags: list
        :param Tags:

          One or more tags to be assigned to the endpoint.

          - *(dict) --*

            - **Key** *(string) --*

              A key is the required name of the tag. The string value can be from 1 to 128 Unicode
              characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
              contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
              (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

            - **Value** *(string) --*

              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
              characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
              contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
              (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

        :type CertificateArn: string
        :param CertificateArn:

          The Amazon Resource Name (ARN) for the certificate.

        :type SslMode: string
        :param SslMode:

          The Secure Sockets Layer (SSL) mode to use for the SSL connection. The default is ``none``

        :type ServiceAccessRoleArn: string
        :param ServiceAccessRoleArn:

          The Amazon Resource Name (ARN) for the service access role that you want to use to create the
          endpoint.

        :type ExternalTableDefinition: string
        :param ExternalTableDefinition:

          The external table definition.

        :type DynamoDbSettings: dict
        :param DynamoDbSettings:

          Settings in JSON format for the target Amazon DynamoDB endpoint. For more information about the
          available settings, see `Using Object Mapping to Migrate Data to DynamoDB
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html>`__ in the *AWS
          Database Migration Service User Guide.*

          - **ServiceAccessRoleArn** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) used by the service access IAM role.

        :type S3Settings: dict
        :param S3Settings:

          Settings in JSON format for the target Amazon S3 endpoint. For more information about the
          available settings, see `Extra Connection Attributes When Using Amazon S3 as a Target for AWS DMS
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring>`__
          in the *AWS Database Migration Service User Guide.*

          - **ServiceAccessRoleArn** *(string) --*

            The Amazon Resource Name (ARN) used by the service access IAM role.

          - **ExternalTableDefinition** *(string) --*

            The external table definition.

          - **CsvRowDelimiter** *(string) --*

            The delimiter used to separate rows in the source files. The default is a carriage return
            (``\\n`` ).

          - **CsvDelimiter** *(string) --*

            The delimiter used to separate columns in the source files. The default is a comma.

          - **BucketFolder** *(string) --*

            An optional parameter to set a folder name in the S3 bucket. If provided, tables are created in
            the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this parameter is not
            specified, then the path used is `` *schema_name* /*table_name* /`` .

          - **BucketName** *(string) --*

            The name of the S3 bucket.

          - **CompressionType** *(string) --*

            An optional parameter to use GZIP to compress the target files. Set to GZIP to compress the
            target files. Set to NONE (the default) or do not use to leave the files uncompressed. Applies
            to both .csv and .parquet file formats.

          - **EncryptionMode** *(string) --*

            The type of server-side encryption that you want to use for your data. This encryption type is
            part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose
            either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , you need an AWS Identity
            and Access Management (IAM) role with permission to allow ``"arn:aws:s3:::dms-*"`` to use the
            following actions:

            * ``s3:CreateBucket``

            * ``s3:ListBucket``

            * ``s3:DeleteBucket``

            * ``s3:GetBucketLocation``

            * ``s3:GetObject``

            * ``s3:PutObject``

            * ``s3:DeleteObject``

            * ``s3:GetObjectVersion``

            * ``s3:GetBucketPolicy``

            * ``s3:PutBucketPolicy``

            * ``s3:DeleteBucketPolicy``

          - **ServerSideEncryptionKmsKeyId** *(string) --*

            If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID. The key
            that you use needs an attached policy that enables AWS Identity and Access Management (IAM)
            user permissions and allows use of the key.

            Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value* --endpoint-type
            target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value* ,BucketFolder=*value*
            ,BucketName=*value* ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

          - **DataFormat** *(string) --*

            The format of the data that you want to use for output. You can choose one of the following:

            * ``csv`` : This is a row-based file format with comma-separated values (.csv).

            * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features
            efficient compression and provides faster query response.

          - **EncodingType** *(string) --*

            The type of encoding you are using:

            * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
            repeated values more efficiently. This is the default.

            * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

            * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column. The
            dictionary is stored in a dictionary page for each column chunk.

          - **DictPageSizeLimit** *(integer) --*

            The maximum size of an encoded dictionary page of a column. If the dictionary page exceeds
            this, this column is stored using an encoding type of ``PLAIN`` . This parameter defaults to
            1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it reverts to ``PLAIN``
            encoding. This size is used for .parquet file format only.

          - **RowGroupLength** *(integer) --*

            The number of rows in a row group. A smaller row group size provides faster reads. But as the
            number of row groups grows, the slower writes become. This parameter defaults to 10,000 rows.
            This number is used for .parquet file format only.

            If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row group
            length in bytes (64 * 1024 * 1024).

          - **DataPageSize** *(integer) --*

            The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB). This
            number is used for .parquet file format only.

          - **ParquetVersion** *(string) --*

            The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the default) or
            ``parquet_2_0`` .

          - **EnableStatistics** *(boolean) --*

            A value that enables statistics for Parquet pages and row groups. Choose ``true`` to enable
            statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` , ``MAX`` , and
            ``MIN`` values. This parameter defaults to ``true`` . This value is used for .parquet file
            format only.

          - **IncludeOpForFullLoad** *(boolean) --*

            A value that enables a full load to write INSERT operations to the comma-separated value (.csv)
            output files only to indicate how the rows were added to the source database.

            .. note::

              AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

            For full load, records can only be inserted. By default (the ``false`` setting), no information
            is recorded in these output files for a full load to indicate that the rows were inserted at
            the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or ``y`` , the INSERT is
            recorded as an I annotation in the first field of the .csv file. This allows the format of your
            target records from a full load to be consistent with the target records from a CDC load.

            .. note::

              This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv files
              only. For more information about how these settings work together, see `Indicating Source DB
              Operations in Migrated S3 Data
              <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
              in the *AWS Database Migration Service User Guide.* .

          - **CdcInsertsOnly** *(boolean) --*

            A value that enables a change data capture (CDC) load to write only INSERT operations to .csv
            or columnar storage (.parquet) output files. By default (the ``false`` setting), the first
            field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D (DELETE).
            These values indicate whether the row was inserted, updated, or deleted at the source database
            for a CDC load to the target.

            If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database are
            migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are recorded
            depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad`` is set to
            ``true`` , the first field of every CDC record is set to I to indicate the INSERT operation at
            the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every CDC record is written
            without a first field to indicate the INSERT operation at the source. For more information
            about how these settings work together, see `Indicating Source DB Operations in Migrated S3
            Data
            <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
            in the *AWS Database Migration Service User Guide.* .

            .. note::

              AWS DMS supports this interaction between the ``CdcInsertsOnly`` and ``IncludeOpForFullLoad``
              parameters in versions 3.1.4 and later.

          - **TimestampColumnName** *(string) --*

            A value that when nonblank causes AWS DMS to add a column with timestamp information to the
            endpoint data for an Amazon S3 target.

            .. note::

              AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

            DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your
            migrated data when you set ``TimestampColumnName`` to a nonblank value.

            For a full load, each row of this timestamp column contains a timestamp for when the data was
            transferred from the source to the target by DMS.

            For a change data capture (CDC) load, each row of the timestamp column contains the timestamp
            for the commit of that row in the source database.

            The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By
            default, the precision of this value is in microseconds. For a CDC load, the rounding of the
            precision depends on the commit timestamp supported by DMS for the source database.

            When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for the
            timestamp column that you set with ``TimestampColumnName`` .

          - **ParquetTimestampInMillisecond** *(boolean) --*

            A value that specifies the precision of any ``TIMESTAMP`` column values that are written to an
            Amazon S3 object file in .parquet format.

            .. note::

              AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and later.

            When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
            ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise, DMS
            writes them with microsecond precision.

            Currently, Amazon Athena and AWS Glue can handle only millisecond precision for ``TIMESTAMP``
            values. Set this parameter to ``true`` for S3 endpoint object files that are .parquet formatted
            only if you plan to query or process the data with Athena or AWS Glue.

            .. note::

              AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format with
              microsecond precision.

              Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the timestamp
              column value that is inserted by setting the ``TimestampColumnName`` parameter.

        :type DmsTransferSettings: dict
        :param DmsTransferSettings:

          The settings in JSON format for the DMS transfer type of source endpoint.

          Possible settings include the following:

          * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3 bucket.

          * ``BucketName`` - The name of the S3 bucket to use.

          * ``CompressionType`` - An optional parameter to use GZIP to compress the target files. To use
          GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed, don't use this
          value.

          Shorthand syntax for these settings is as follows:
          ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

          JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string", "BucketName":
          "string", "CompressionType": "none"|"gzip" }``

          - **ServiceAccessRoleArn** *(string) --*

            The IAM role that has permission to access the Amazon S3 bucket.

          - **BucketName** *(string) --*

            The name of the S3 bucket to use.

        :type MongoDbSettings: dict
        :param MongoDbSettings:

          Settings in JSON format for the source MongoDB endpoint. For more information about the available
          settings, see the configuration properties section in `Using MongoDB as a Target for AWS Database
          Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html>`__
          in the *AWS Database Migration Service User Guide.*

          - **Username** *(string) --*

            The user name you use to access the MongoDB source endpoint.

          - **Password** *(string) --*

            The password for the user account you use to access the MongoDB source endpoint.

          - **ServerName** *(string) --*

            The name of the server on the MongoDB source endpoint.

          - **Port** *(integer) --*

            The port value for the MongoDB source endpoint.

          - **DatabaseName** *(string) --*

            The database name on the MongoDB source endpoint.

          - **AuthType** *(string) --*

            The authentication type you use to access the MongoDB source endpoint.

            Valid values: NO, PASSWORD

            When NO is selected, user name and password parameters are not used and can be empty.

          - **AuthMechanism** *(string) --*

            The authentication mechanism you use to access the MongoDB source endpoint.

            Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

            DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use SCRAM_SHA_1.
            This setting is not used when authType=No.

          - **NestingLevel** *(string) --*

            Specifies either document or table mode.

            Valid values: NONE, ONE

            Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

          - **ExtractDocId** *(string) --*

            Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

            Default value is false.

          - **DocsToInvestigate** *(string) --*

            Indicates the number of documents to preview to determine the document organization. Use this
            setting when ``NestingLevel`` is set to ONE.

            Must be a positive value greater than 0. Default value is 1000.

          - **AuthSource** *(string) --*

            The MongoDB database name. This setting is not used when ``authType=NO`` .

            The default is admin.

          - **KmsKeyId** *(string) --*

            The AWS KMS key identifier that is used to encrypt the content on the replication instance. If
            you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
            encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS
            account has a different default encryption key for each AWS Region.

        :type KinesisSettings: dict
        :param KinesisSettings:

          Settings in JSON format for the target Amazon Kinesis Data Streams endpoint. For more information
          about the available settings, see `Using Object Mapping to Migrate Data to a Kinesis Data Stream
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping>`__
          in the *AWS Database Migration User Guide.*

          - **StreamArn** *(string) --*

            The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

          - **MessageFormat** *(string) --*

            The output format for the records created on the endpoint. The message format is ``JSON`` .

          - **ServiceAccessRoleArn** *(string) --*

            The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon Kinesis
            data stream.

        :type ElasticsearchSettings: dict
        :param ElasticsearchSettings:

          Settings in JSON format for the target Elasticsearch endpoint. For more information about the
          available settings, see `Extra Connection Attributes When Using Elasticsearch as a Target for AWS
          DMS
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration>`__
          in the *AWS Database Migration User Guide.*

          - **ServiceAccessRoleArn** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) used by service to access the IAM role.

          - **EndpointUri** *(string) --* **[REQUIRED]**

            The endpoint for the Elasticsearch cluster.

          - **FullLoadErrorPercentage** *(integer) --*

            The maximum percentage of records that can fail to be written before a full load operation
            stops.

          - **ErrorRetryDuration** *(integer) --*

            The maximum number of seconds that DMS retries failed API requests to the Elasticsearch cluster.

        :type RedshiftSettings: dict
        :param RedshiftSettings:

          - **AcceptAnyDate** *(boolean) --*

            A value that indicates to allow any date format, including invalid formats such as 00/00/00
            00:00:00, to be loaded without generating an error. You can choose ``true`` or ``false`` (the
            default).

            This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the
            DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT
            specification, Amazon Redshift inserts a NULL value into that field.

          - **AfterConnectScript** *(string) --*

            Code to run after connecting. This parameter should contain the code itself, not the name of a
            file containing the code.

          - **BucketFolder** *(string) --*

            The location where the comma-separated value (.csv) files are stored before being uploaded to
            the S3 bucket.

          - **BucketName** *(string) --*

            The name of the S3 bucket you want to use

          - **ConnectionTimeout** *(integer) --*

            A value that sets the amount of time to wait (in milliseconds) before timing out, beginning
            from when you initially establish a connection.

          - **DatabaseName** *(string) --*

            The name of the Amazon Redshift data warehouse (service) that you are working with.

          - **DateFormat** *(string) --*

            The date format that you are using. Valid values are ``auto`` (case-sensitive), your date
            format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it defaults
            to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some that aren't
            supported when you use a date format string.

            If your date and time values use formats different from each other, set this to ``auto`` .

          - **EmptyAsNull** *(boolean) --*

            A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as NULL. A
            value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is ``false`` .

          - **EncryptionMode** *(string) --*

            The type of server-side encryption that you want to use for your data. This encryption type is
            part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose
            either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , create an AWS Identity and
            Access Management (IAM) role with a policy that allows ``"arn:aws:s3:::*"`` to use the
            following actions: ``"s3:PutObject", "s3:ListBucket"``

          - **FileTransferUploadStreams** *(integer) --*

            The number of threads used to upload a single file. This parameter accepts a value from 1
            through 64. It defaults to 10.

          - **LoadTimeout** *(integer) --*

            The amount of time to wait (in milliseconds) before timing out, beginning from when you begin
            loading.

          - **MaxFileSize** *(integer) --*

            The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This
            accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

          - **Password** *(string) --*

            The password for the user named in the ``username`` property.

          - **Port** *(integer) --*

            The port number for Amazon Redshift. The default value is 5439.

          - **RemoveQuotes** *(boolean) --*

            A value that specifies to remove surrounding quotation marks from strings in the incoming data.
            All characters within the quotation marks, including delimiters, are retained. Choose ``true``
            to remove quotation marks. The default is ``false`` .

          - **ReplaceInvalidChars** *(string) --*

            A list of characters that you want to replace. Use with ``ReplaceChars`` .

          - **ReplaceChars** *(string) --*

            A value that specifies to replaces the invalid characters specified in ``ReplaceInvalidChars``
            , substituting the specified characters instead. The default is ``"?"`` .

          - **ServerName** *(string) --*

            The name of the Amazon Redshift cluster you are using.

          - **ServiceAccessRoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift service.

          - **ServerSideEncryptionKmsKeyId** *(string) --*

            The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide this key
            ID. The key that you use needs an attached policy that enables IAM user permissions and allows
            use of the key.

          - **TimeFormat** *(string) --*

            The time format that you want to use. Valid values are ``auto`` (case-sensitive),
            ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10. Using
            ``auto`` recognizes most strings, even some that aren't supported when you use a time format
            string.

            If your date and time values use formats different from each other, set this parameter to
            ``auto`` .

          - **TrimBlanks** *(boolean) --*

            A value that specifies to remove the trailing white space characters from a VARCHAR string.
            This parameter applies only to columns with a VARCHAR data type. Choose ``true`` to remove
            unneeded white space. The default is ``false`` .

          - **TruncateColumns** *(boolean) --*

            A value that specifies to truncate data in columns to the appropriate number of characters, so
            that the data fits in the column. This parameter applies only to columns with a VARCHAR or CHAR
            data type, and rows with a size of 4 MB or less. Choose ``true`` to truncate data. The default
            is ``false`` .

          - **Username** *(string) --*

            An Amazon Redshift user name for a registered user.

          - **WriteBufferSize** *(integer) --*

            The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The
            default is 1,024. Use this setting to tune performance.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Endpoint': {
                    'EndpointIdentifier': 'string',
                    'EndpointType': 'source'|'target',
                    'EngineName': 'string',
                    'EngineDisplayName': 'string',
                    'Username': 'string',
                    'ServerName': 'string',
                    'Port': 123,
                    'DatabaseName': 'string',
                    'ExtraConnectionAttributes': 'string',
                    'Status': 'string',
                    'KmsKeyId': 'string',
                    'EndpointArn': 'string',
                    'CertificateArn': 'string',
                    'SslMode': 'none'|'require'|'verify-ca'|'verify-full',
                    'ServiceAccessRoleArn': 'string',
                    'ExternalTableDefinition': 'string',
                    'ExternalId': 'string',
                    'DynamoDbSettings': {
                        'ServiceAccessRoleArn': 'string'
                    },
                    'S3Settings': {
                        'ServiceAccessRoleArn': 'string',
                        'ExternalTableDefinition': 'string',
                        'CsvRowDelimiter': 'string',
                        'CsvDelimiter': 'string',
                        'BucketFolder': 'string',
                        'BucketName': 'string',
                        'CompressionType': 'none'|'gzip',
                        'EncryptionMode': 'sse-s3'|'sse-kms',
                        'ServerSideEncryptionKmsKeyId': 'string',
                        'DataFormat': 'csv'|'parquet',
                        'EncodingType': 'plain'|'plain-dictionary'|'rle-dictionary',
                        'DictPageSizeLimit': 123,
                        'RowGroupLength': 123,
                        'DataPageSize': 123,
                        'ParquetVersion': 'parquet-1-0'|'parquet-2-0',
                        'EnableStatistics': True|False,
                        'IncludeOpForFullLoad': True|False,
                        'CdcInsertsOnly': True|False,
                        'TimestampColumnName': 'string',
                        'ParquetTimestampInMillisecond': True|False
                    },
                    'DmsTransferSettings': {
                        'ServiceAccessRoleArn': 'string',
                        'BucketName': 'string'
                    },
                    'MongoDbSettings': {
                        'Username': 'string',
                        'Password': 'string',
                        'ServerName': 'string',
                        'Port': 123,
                        'DatabaseName': 'string',
                        'AuthType': 'no'|'password',
                        'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
                        'NestingLevel': 'none'|'one',
                        'ExtractDocId': 'string',
                        'DocsToInvestigate': 'string',
                        'AuthSource': 'string',
                        'KmsKeyId': 'string'
                    },
                    'KinesisSettings': {
                        'StreamArn': 'string',
                        'MessageFormat': 'json',
                        'ServiceAccessRoleArn': 'string'
                    },
                    'ElasticsearchSettings': {
                        'ServiceAccessRoleArn': 'string',
                        'EndpointUri': 'string',
                        'FullLoadErrorPercentage': 123,
                        'ErrorRetryDuration': 123
                    },
                    'RedshiftSettings': {
                        'AcceptAnyDate': True|False,
                        'AfterConnectScript': 'string',
                        'BucketFolder': 'string',
                        'BucketName': 'string',
                        'ConnectionTimeout': 123,
                        'DatabaseName': 'string',
                        'DateFormat': 'string',
                        'EmptyAsNull': True|False,
                        'EncryptionMode': 'sse-s3'|'sse-kms',
                        'FileTransferUploadStreams': 123,
                        'LoadTimeout': 123,
                        'MaxFileSize': 123,
                        'Password': 'string',
                        'Port': 123,
                        'RemoveQuotes': True|False,
                        'ReplaceInvalidChars': 'string',
                        'ReplaceChars': 'string',
                        'ServerName': 'string',
                        'ServiceAccessRoleArn': 'string',
                        'ServerSideEncryptionKmsKeyId': 'string',
                        'TimeFormat': 'string',
                        'TrimBlanks': True|False,
                        'TruncateColumns': True|False,
                        'Username': 'string',
                        'WriteBufferSize': 123
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Endpoint** *(dict) --*

              The endpoint that was created.

              - **EndpointIdentifier** *(string) --*

                The database endpoint identifier. Identifiers must begin with a letter; must contain only
                ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
                consecutive hyphens.

              - **EndpointType** *(string) --*

                The type of endpoint. Valid values are ``source`` and ``target`` .

              - **EngineName** *(string) --*

                The database engine name. Valid values, depending on the EndpointType, include mysql,
                oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
                dynamodb, mongodb, and sqlserver.

              - **EngineDisplayName** *(string) --*

                The expanded name for the engine name. For example, if the ``EngineName`` parameter is
                "aurora," this value would be "Amazon Aurora MySQL."

              - **Username** *(string) --*

                The user name used to connect to the endpoint.

              - **ServerName** *(string) --*

                The name of the server at the endpoint.

              - **Port** *(integer) --*

                The port value used to access the endpoint.

              - **DatabaseName** *(string) --*

                The name of the database at the endpoint.

              - **ExtraConnectionAttributes** *(string) --*

                Additional connection attributes used to connect to the endpoint.

              - **Status** *(string) --*

                The status of the endpoint.

              - **KmsKeyId** *(string) --*

                An AWS KMS key identifier that is used to encrypt the connection parameters for the
                endpoint.

                If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
                encryption key.

                AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
                different default encryption key for each AWS Region.

              - **EndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **CertificateArn** *(string) --*

                The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

              - **SslMode** *(string) --*

                The SSL mode used to connect to the endpoint. The default value is ``none`` .

              - **ServiceAccessRoleArn** *(string) --*

                The Amazon Resource Name (ARN) used by the service access IAM role.

              - **ExternalTableDefinition** *(string) --*

                The external table definition.

              - **ExternalId** *(string) --*

                Value returned by a call to CreateEndpoint that can be used for cross-account validation.
                Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

              - **DynamoDbSettings** *(dict) --*

                The settings for the target DynamoDB database. For more information, see the
                ``DynamoDBSettings`` structure.

                - **ServiceAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) used by the service access IAM role.

              - **S3Settings** *(dict) --*

                The settings for the S3 target endpoint. For more information, see the ``S3Settings``
                structure.

                - **ServiceAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) used by the service access IAM role.

                - **ExternalTableDefinition** *(string) --*

                  The external table definition.

                - **CsvRowDelimiter** *(string) --*

                  The delimiter used to separate rows in the source files. The default is a carriage return
                  (``\\n`` ).

                - **CsvDelimiter** *(string) --*

                  The delimiter used to separate columns in the source files. The default is a comma.

                - **BucketFolder** *(string) --*

                  An optional parameter to set a folder name in the S3 bucket. If provided, tables are
                  created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
                  parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

                - **BucketName** *(string) --*

                  The name of the S3 bucket.

                - **CompressionType** *(string) --*

                  An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
                  the target files. Set to NONE (the default) or do not use to leave the files
                  uncompressed. Applies to both .csv and .parquet file formats.

                - **EncryptionMode** *(string) --*

                  The type of server-side encryption that you want to use for your data. This encryption
                  type is part of the endpoint settings or the extra connections attributes for Amazon S3.
                  You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , you
                  need an AWS Identity and Access Management (IAM) role with permission to allow
                  ``"arn:aws:s3:::dms-*"`` to use the following actions:

                  * ``s3:CreateBucket``

                  * ``s3:ListBucket``

                  * ``s3:DeleteBucket``

                  * ``s3:GetBucketLocation``

                  * ``s3:GetObject``

                  * ``s3:PutObject``

                  * ``s3:DeleteObject``

                  * ``s3:GetObjectVersion``

                  * ``s3:GetBucketPolicy``

                  * ``s3:PutBucketPolicy``

                  * ``s3:DeleteBucketPolicy``

                - **ServerSideEncryptionKmsKeyId** *(string) --*

                  If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID. The
                  key that you use needs an attached policy that enables AWS Identity and Access Management
                  (IAM) user permissions and allows use of the key.

                  Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
                  --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
                  ,BucketFolder=*value* ,BucketName=*value*
                  ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

                - **DataFormat** *(string) --*

                  The format of the data that you want to use for output. You can choose one of the
                  following:

                  * ``csv`` : This is a row-based file format with comma-separated values (.csv).

                  * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features
                  efficient compression and provides faster query response.

                - **EncodingType** *(string) --*

                  The type of encoding you are using:

                  * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
                  repeated values more efficiently. This is the default.

                  * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

                  * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
                  The dictionary is stored in a dictionary page for each column chunk.

                - **DictPageSizeLimit** *(integer) --*

                  The maximum size of an encoded dictionary page of a column. If the dictionary page
                  exceeds this, this column is stored using an encoding type of ``PLAIN`` . This parameter
                  defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it
                  reverts to ``PLAIN`` encoding. This size is used for .parquet file format only.

                - **RowGroupLength** *(integer) --*

                  The number of rows in a row group. A smaller row group size provides faster reads. But as
                  the number of row groups grows, the slower writes become. This parameter defaults to
                  10,000 rows. This number is used for .parquet file format only.

                  If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
                  group length in bytes (64 * 1024 * 1024).

                - **DataPageSize** *(integer) --*

                  The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB).
                  This number is used for .parquet file format only.

                - **ParquetVersion** *(string) --*

                  The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
                  default) or ``parquet_2_0`` .

                - **EnableStatistics** *(boolean) --*

                  A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
                  enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
                  ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
                  for .parquet file format only.

                - **IncludeOpForFullLoad** *(boolean) --*

                  A value that enables a full load to write INSERT operations to the comma-separated value
                  (.csv) output files only to indicate how the rows were added to the source database.

                  .. note::

                    AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

                  For full load, records can only be inserted. By default (the ``false`` setting), no
                  information is recorded in these output files for a full load to indicate that the rows
                  were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
                  ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
                  This allows the format of your target records from a full load to be consistent with the
                  target records from a CDC load.

                  .. note::

                    This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
                    files only. For more information about how these settings work together, see
                    `Indicating Source DB Operations in Migrated S3 Data
                    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
                    in the *AWS Database Migration Service User Guide.* .

                - **CdcInsertsOnly** *(boolean) --*

                  A value that enables a change data capture (CDC) load to write only INSERT operations to
                  .csv or columnar storage (.parquet) output files. By default (the ``false`` setting), the
                  first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D
                  (DELETE). These values indicate whether the row was inserted, updated, or deleted at the
                  source database for a CDC load to the target.

                  If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database
                  are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are
                  recorded depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad``
                  is set to ``true`` , the first field of every CDC record is set to I to indicate the
                  INSERT operation at the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every
                  CDC record is written without a first field to indicate the INSERT operation at the
                  source. For more information about how these settings work together, see `Indicating
                  Source DB Operations in Migrated S3 Data
                  <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
                  in the *AWS Database Migration Service User Guide.* .

                  .. note::

                    AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
                    ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

                - **TimestampColumnName** *(string) --*

                  A value that when nonblank causes AWS DMS to add a column with timestamp information to
                  the endpoint data for an Amazon S3 target.

                  .. note::

                    AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

                  DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your
                  migrated data when you set ``TimestampColumnName`` to a nonblank value.

                  For a full load, each row of this timestamp column contains a timestamp for when the data
                  was transferred from the source to the target by DMS.

                  For a change data capture (CDC) load, each row of the timestamp column contains the
                  timestamp for the commit of that row in the source database.

                  The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By
                  default, the precision of this value is in microseconds. For a CDC load, the rounding of
                  the precision depends on the commit timestamp supported by DMS for the source database.

                  When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
                  the timestamp column that you set with ``TimestampColumnName`` .

                - **ParquetTimestampInMillisecond** *(boolean) --*

                  A value that specifies the precision of any ``TIMESTAMP`` column values that are written
                  to an Amazon S3 object file in .parquet format.

                  .. note::

                    AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and
                    later.

                  When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
                  ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise,
                  DMS writes them with microsecond precision.

                  Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
                  ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
                  are .parquet formatted only if you plan to query or process the data with Athena or AWS
                  Glue.

                  .. note::

                    AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
                    with microsecond precision.

                    Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
                    timestamp column value that is inserted by setting the ``TimestampColumnName``
                    parameter.

              - **DmsTransferSettings** *(dict) --*

                The settings in JSON format for the DMS transfer type of source endpoint.

                Possible settings include the following:

                * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
                bucket.

                * ``BucketName`` - The name of the S3 bucket to use.

                * ``CompressionType`` - An optional parameter to use GZIP to compress the target files. To
                use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed, don't
                use this value.

                Shorthand syntax for these settings is as follows:
                ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

                JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
                "BucketName": "string", "CompressionType": "none"|"gzip" }``

                - **ServiceAccessRoleArn** *(string) --*

                  The IAM role that has permission to access the Amazon S3 bucket.

                - **BucketName** *(string) --*

                  The name of the S3 bucket to use.

              - **MongoDbSettings** *(dict) --*

                The settings for the MongoDB source endpoint. For more information, see the
                ``MongoDbSettings`` structure.

                - **Username** *(string) --*

                  The user name you use to access the MongoDB source endpoint.

                - **Password** *(string) --*

                  The password for the user account you use to access the MongoDB source endpoint.

                - **ServerName** *(string) --*

                  The name of the server on the MongoDB source endpoint.

                - **Port** *(integer) --*

                  The port value for the MongoDB source endpoint.

                - **DatabaseName** *(string) --*

                  The database name on the MongoDB source endpoint.

                - **AuthType** *(string) --*

                  The authentication type you use to access the MongoDB source endpoint.

                  Valid values: NO, PASSWORD

                  When NO is selected, user name and password parameters are not used and can be empty.

                - **AuthMechanism** *(string) --*

                  The authentication mechanism you use to access the MongoDB source endpoint.

                  Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

                  DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
                  SCRAM_SHA_1. This setting is not used when authType=No.

                - **NestingLevel** *(string) --*

                  Specifies either document or table mode.

                  Valid values: NONE, ONE

                  Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

                - **ExtractDocId** *(string) --*

                  Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

                  Default value is false.

                - **DocsToInvestigate** *(string) --*

                  Indicates the number of documents to preview to determine the document organization. Use
                  this setting when ``NestingLevel`` is set to ONE.

                  Must be a positive value greater than 0. Default value is 1000.

                - **AuthSource** *(string) --*

                  The MongoDB database name. This setting is not used when ``authType=NO`` .

                  The default is admin.

                - **KmsKeyId** *(string) --*

                  The AWS KMS key identifier that is used to encrypt the content on the replication
                  instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses
                  your default encryption key. AWS KMS creates the default encryption key for your AWS
                  account. Your AWS account has a different default encryption key for each AWS Region.

              - **KinesisSettings** *(dict) --*

                The settings for the Amazon Kinesis source endpoint. For more information, see the
                ``KinesisSettings`` structure.

                - **StreamArn** *(string) --*

                  The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

                - **MessageFormat** *(string) --*

                  The output format for the records created on the endpoint. The message format is ``JSON``
                  .

                - **ServiceAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
                  Kinesis data stream.

              - **ElasticsearchSettings** *(dict) --*

                The settings for the Elasticsearch source endpoint. For more information, see the
                ``ElasticsearchSettings`` structure.

                - **ServiceAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) used by service to access the IAM role.

                - **EndpointUri** *(string) --*

                  The endpoint for the Elasticsearch cluster.

                - **FullLoadErrorPercentage** *(integer) --*

                  The maximum percentage of records that can fail to be written before a full load
                  operation stops.

                - **ErrorRetryDuration** *(integer) --*

                  The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
                  cluster.

              - **RedshiftSettings** *(dict) --*

                Settings for the Amazon Redshift endpoint.

                - **AcceptAnyDate** *(boolean) --*

                  A value that indicates to allow any date format, including invalid formats such as
                  00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
                  ``false`` (the default).

                  This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with
                  the DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT
                  specification, Amazon Redshift inserts a NULL value into that field.

                - **AfterConnectScript** *(string) --*

                  Code to run after connecting. This parameter should contain the code itself, not the name
                  of a file containing the code.

                - **BucketFolder** *(string) --*

                  The location where the comma-separated value (.csv) files are stored before being
                  uploaded to the S3 bucket.

                - **BucketName** *(string) --*

                  The name of the S3 bucket you want to use

                - **ConnectionTimeout** *(integer) --*

                  A value that sets the amount of time to wait (in milliseconds) before timing out,
                  beginning from when you initially establish a connection.

                - **DatabaseName** *(string) --*

                  The name of the Amazon Redshift data warehouse (service) that you are working with.

                - **DateFormat** *(string) --*

                  The date format that you are using. Valid values are ``auto`` (case-sensitive), your date
                  format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it
                  defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some
                  that aren't supported when you use a date format string.

                  If your date and time values use formats different from each other, set this to ``auto`` .

                - **EmptyAsNull** *(boolean) --*

                  A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
                  NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
                  ``false`` .

                - **EncryptionMode** *(string) --*

                  The type of server-side encryption that you want to use for your data. This encryption
                  type is part of the endpoint settings or the extra connections attributes for Amazon S3.
                  You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
                  create an AWS Identity and Access Management (IAM) role with a policy that allows
                  ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

                - **FileTransferUploadStreams** *(integer) --*

                  The number of threads used to upload a single file. This parameter accepts a value from 1
                  through 64. It defaults to 10.

                - **LoadTimeout** *(integer) --*

                  The amount of time to wait (in milliseconds) before timing out, beginning from when you
                  begin loading.

                - **MaxFileSize** *(integer) --*

                  The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This
                  accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

                - **Password** *(string) --*

                  The password for the user named in the ``username`` property.

                - **Port** *(integer) --*

                  The port number for Amazon Redshift. The default value is 5439.

                - **RemoveQuotes** *(boolean) --*

                  A value that specifies to remove surrounding quotation marks from strings in the incoming
                  data. All characters within the quotation marks, including delimiters, are retained.
                  Choose ``true`` to remove quotation marks. The default is ``false`` .

                - **ReplaceInvalidChars** *(string) --*

                  A list of characters that you want to replace. Use with ``ReplaceChars`` .

                - **ReplaceChars** *(string) --*

                  A value that specifies to replaces the invalid characters specified in
                  ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
                  ``"?"`` .

                - **ServerName** *(string) --*

                  The name of the Amazon Redshift cluster you are using.

                - **ServiceAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
                  service.

                - **ServerSideEncryptionKmsKeyId** *(string) --*

                  The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
                  this key ID. The key that you use needs an attached policy that enables IAM user
                  permissions and allows use of the key.

                - **TimeFormat** *(string) --*

                  The time format that you want to use. Valid values are ``auto`` (case-sensitive),
                  ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10.
                  Using ``auto`` recognizes most strings, even some that aren't supported when you use a
                  time format string.

                  If your date and time values use formats different from each other, set this parameter to
                  ``auto`` .

                - **TrimBlanks** *(boolean) --*

                  A value that specifies to remove the trailing white space characters from a VARCHAR
                  string. This parameter applies only to columns with a VARCHAR data type. Choose ``true``
                  to remove unneeded white space. The default is ``false`` .

                - **TruncateColumns** *(boolean) --*

                  A value that specifies to truncate data in columns to the appropriate number of
                  characters, so that the data fits in the column. This parameter applies only to columns
                  with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
                  to truncate data. The default is ``false`` .

                - **Username** *(string) --*

                  An Amazon Redshift user name for a registered user.

                - **WriteBufferSize** *(integer) --*

                  The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The
                  default is 1,024. Use this setting to tune performance.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str = None,
        EventCategories: List[str] = None,
        SourceIds: List[str] = None,
        Enabled: bool = None,
        Tags: List[ClientCreateEventSubscriptionTagsTypeDef] = None,
    ) -> ClientCreateEventSubscriptionResponseTypeDef:
        """
        Creates an AWS DMS event notification subscription.

        You can specify the type of source (``SourceType`` ) you want to be notified of, provide a list of
        AWS DMS source IDs (``SourceIds`` ) that triggers the events, and provide a list of event
        categories (``EventCategories`` ) for events you want to be notified of. If you specify both the
        ``SourceType`` and ``SourceIds`` , such as ``SourceType = replication-instance`` and
        ``SourceIdentifier = my-replinstance`` , you will be notified of all the replication instance
        events for the specified source. If you specify a ``SourceType`` but don't specify a
        ``SourceIdentifier`` , you receive notice of the events for that source type for all your AWS DMS
        sources. If you don't specify either ``SourceType`` nor ``SourceIdentifier`` , you will be notified
        of events generated from all AWS DMS sources belonging to your customer account.

        For more information about AWS DMS events, see `Working with Events and Notifications
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html>`__ in the *AWS Database
        Migration Service User Guide.*

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/CreateEventSubscription>`_

        **Request Syntax**
        ::

          response = client.create_event_subscription(
              SubscriptionName='string',
              SnsTopicArn='string',
              SourceType='string',
              EventCategories=[
                  'string',
              ],
              SourceIds=[
                  'string',
              ],
              Enabled=True|False,
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type SubscriptionName: string
        :param SubscriptionName: **[REQUIRED]**

          The name of the AWS DMS event notification subscription. This name must be less than 255
          characters.

        :type SnsTopicArn: string
        :param SnsTopicArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification. The ARN is
          created by Amazon SNS when you create a topic and subscribe to it.

        :type SourceType: string
        :param SourceType:

          The type of AWS DMS resource that generates the events. For example, if you want to be notified
          of events generated by a replication instance, you set this parameter to ``replication-instance``
          . If this value is not specified, all events are returned.

          Valid values: ``replication-instance`` | ``replication-task``

        :type EventCategories: list
        :param EventCategories:

          A list of event categories for a source type that you want to subscribe to. For more information,
          see `Working with Events and Notifications
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html>`__ in the *AWS Database
          Migration Service User Guide.*

          - *(string) --*

        :type SourceIds: list
        :param SourceIds:

          A list of identifiers for which AWS DMS provides notification events.

          If you don't specify a value, notifications are provided for all sources.

          If you specify multiple values, they must be of the same type. For example, if you specify a
          database instance ID, then all of the other values must be database instance IDs.

          - *(string) --*

        :type Enabled: boolean
        :param Enabled:

          A Boolean value; set to ``true`` to activate the subscription, or set to ``false`` to create the
          subscription but not activate it.

        :type Tags: list
        :param Tags:

          One or more tags to be assigned to the event subscription.

          - *(dict) --*

            - **Key** *(string) --*

              A key is the required name of the tag. The string value can be from 1 to 128 Unicode
              characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
              contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
              (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

            - **Value** *(string) --*

              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
              characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
              contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
              (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EventSubscription': {
                    'CustomerAwsId': 'string',
                    'CustSubscriptionId': 'string',
                    'SnsTopicArn': 'string',
                    'Status': 'string',
                    'SubscriptionCreationTime': 'string',
                    'SourceType': 'string',
                    'SourceIdsList': [
                        'string',
                    ],
                    'EventCategoriesList': [
                        'string',
                    ],
                    'Enabled': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **EventSubscription** *(dict) --*

              The event subscription that was created.

              - **CustomerAwsId** *(string) --*

                The AWS customer account associated with the AWS DMS event notification subscription.

              - **CustSubscriptionId** *(string) --*

                The AWS DMS event notification subscription Id.

              - **SnsTopicArn** *(string) --*

                The topic ARN of the AWS DMS event notification subscription.

              - **Status** *(string) --*

                The status of the AWS DMS event notification subscription.

                Constraints:

                Can be one of the following: creating | modifying | deleting | active | no-permission |
                topic-not-exist

                The status "no-permission" indicates that AWS DMS no longer has permission to post to the
                SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
                subscription was created.

              - **SubscriptionCreationTime** *(string) --*

                The time the RDS event notification subscription was created.

              - **SourceType** *(string) --*

                The type of AWS DMS resource that generates events.

                Valid values: replication-instance | replication-server | security-group | replication-task

              - **SourceIdsList** *(list) --*

                A list of source Ids for the event subscription.

                - *(string) --*

              - **EventCategoriesList** *(list) --*

                A lists of event categories.

                - *(string) --*

              - **Enabled** *(boolean) --*

                Boolean value that indicates if the event subscription is enabled.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_replication_instance(
        self,
        ReplicationInstanceIdentifier: str,
        ReplicationInstanceClass: str,
        AllocatedStorage: int = None,
        VpcSecurityGroupIds: List[str] = None,
        AvailabilityZone: str = None,
        ReplicationSubnetGroupIdentifier: str = None,
        PreferredMaintenanceWindow: str = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        Tags: List[ClientCreateReplicationInstanceTagsTypeDef] = None,
        KmsKeyId: str = None,
        PubliclyAccessible: bool = None,
        DnsNameServers: str = None,
    ) -> ClientCreateReplicationInstanceResponseTypeDef:
        """
        Creates the replication instance using the specified parameters.

        AWS DMS requires that your account have certain roles with appropriate permissions before you can
        create a replication instance. For information on the required roles, see `Creating the IAM Roles
        to Use With the AWS CLI and AWS DMS API
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.APIRole.html>`__ . For information
        on the required permissions, see `IAM Permissions Needed to Use AWS DMS
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.IAMPermissions.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/CreateReplicationInstance>`_

        **Request Syntax**
        ::

          response = client.create_replication_instance(
              ReplicationInstanceIdentifier='string',
              AllocatedStorage=123,
              ReplicationInstanceClass='string',
              VpcSecurityGroupIds=[
                  'string',
              ],
              AvailabilityZone='string',
              ReplicationSubnetGroupIdentifier='string',
              PreferredMaintenanceWindow='string',
              MultiAZ=True|False,
              EngineVersion='string',
              AutoMinorVersionUpgrade=True|False,
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              KmsKeyId='string',
              PubliclyAccessible=True|False,
              DnsNameServers='string'
          )
        :type ReplicationInstanceIdentifier: string
        :param ReplicationInstanceIdentifier: **[REQUIRED]**

          The replication instance identifier. This parameter is stored as a lowercase string.

          Constraints:

          * Must contain from 1 to 63 alphanumeric characters or hyphens.

          * First character must be a letter.

          * Cannot end with a hyphen or contain two consecutive hyphens.

          Example: ``myrepinstance``

        :type AllocatedStorage: integer
        :param AllocatedStorage:

          The amount of storage (in gigabytes) to be initially allocated for the replication instance.

        :type ReplicationInstanceClass: string
        :param ReplicationInstanceClass: **[REQUIRED]**

          The compute and memory capacity of the replication instance as specified by the replication
          instance class.

          Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large |
          dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

        :type VpcSecurityGroupIds: list
        :param VpcSecurityGroupIds:

          Specifies the VPC security group to be used with the replication instance. The VPC security group
          must work with the VPC containing the replication instance.

          - *(string) --*

        :type AvailabilityZone: string
        :param AvailabilityZone:

          The AWS Availability Zone where the replication instance will be created. The default value is a
          random, system-chosen Availability Zone in the endpoint's AWS Region, for example: ``us-east-1d``

        :type ReplicationSubnetGroupIdentifier: string
        :param ReplicationSubnetGroupIdentifier:

          A subnet group to associate with the replication instance.

        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow:

          The weekly time range during which system maintenance can occur, in Universal Coordinated Time
          (UTC).

          Format: ``ddd:hh24:mi-ddd:hh24:mi``

          Default: A 30-minute window selected at random from an 8-hour block of time per AWS Region,
          occurring on a random day of the week.

          Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun

          Constraints: Minimum 30-minute window.

        :type MultiAZ: boolean
        :param MultiAZ:

          Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
          ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

        :type EngineVersion: string
        :param EngineVersion:

          The engine version number of the replication instance.

        :type AutoMinorVersionUpgrade: boolean
        :param AutoMinorVersionUpgrade:

          Indicates whether minor engine upgrades will be applied automatically to the replication instance
          during the maintenance window. This parameter defaults to ``true`` .

          Default: ``true``

        :type Tags: list
        :param Tags:

          One or more tags to be assigned to the replication instance.

          - *(dict) --*

            - **Key** *(string) --*

              A key is the required name of the tag. The string value can be from 1 to 128 Unicode
              characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
              contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
              (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

            - **Value** *(string) --*

              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
              characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
              contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
              (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

        :type KmsKeyId: string
        :param KmsKeyId:

          An AWS KMS key identifier that is used to encrypt the data on the replication instance.

          If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
          encryption key.

          AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different
          default encryption key for each AWS Region.

        :type PubliclyAccessible: boolean
        :param PubliclyAccessible:

          Specifies the accessibility options for the replication instance. A value of ``true`` represents
          an instance with a public IP address. A value of ``false`` represents an instance with a private
          IP address. The default value is ``true`` .

        :type DnsNameServers: string
        :param DnsNameServers:

          A list of DNS name servers supported for the replication instance.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationInstance': {
                    'ReplicationInstanceIdentifier': 'string',
                    'ReplicationInstanceClass': 'string',
                    'ReplicationInstanceStatus': 'string',
                    'AllocatedStorage': 123,
                    'InstanceCreateTime': datetime(2015, 1, 1),
                    'VpcSecurityGroups': [
                        {
                            'VpcSecurityGroupId': 'string',
                            'Status': 'string'
                        },
                    ],
                    'AvailabilityZone': 'string',
                    'ReplicationSubnetGroup': {
                        'ReplicationSubnetGroupIdentifier': 'string',
                        'ReplicationSubnetGroupDescription': 'string',
                        'VpcId': 'string',
                        'SubnetGroupStatus': 'string',
                        'Subnets': [
                            {
                                'SubnetIdentifier': 'string',
                                'SubnetAvailabilityZone': {
                                    'Name': 'string'
                                },
                                'SubnetStatus': 'string'
                            },
                        ]
                    },
                    'PreferredMaintenanceWindow': 'string',
                    'PendingModifiedValues': {
                        'ReplicationInstanceClass': 'string',
                        'AllocatedStorage': 123,
                        'MultiAZ': True|False,
                        'EngineVersion': 'string'
                    },
                    'MultiAZ': True|False,
                    'EngineVersion': 'string',
                    'AutoMinorVersionUpgrade': True|False,
                    'KmsKeyId': 'string',
                    'ReplicationInstanceArn': 'string',
                    'ReplicationInstancePublicIpAddress': 'string',
                    'ReplicationInstancePrivateIpAddress': 'string',
                    'ReplicationInstancePublicIpAddresses': [
                        'string',
                    ],
                    'ReplicationInstancePrivateIpAddresses': [
                        'string',
                    ],
                    'PubliclyAccessible': True|False,
                    'SecondaryAvailabilityZone': 'string',
                    'FreeUntil': datetime(2015, 1, 1),
                    'DnsNameServers': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationInstance** *(dict) --*

              The replication instance that was created.

              - **ReplicationInstanceIdentifier** *(string) --*

                The replication instance identifier. This parameter is stored as a lowercase string.

                Constraints:

                * Must contain from 1 to 63 alphanumeric characters or hyphens.

                * First character must be a letter.

                * Cannot end with a hyphen or contain two consecutive hyphens.

                Example: ``myrepinstance``

              - **ReplicationInstanceClass** *(string) --*

                The compute and memory capacity of the replication instance.

                Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large |
                dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

              - **ReplicationInstanceStatus** *(string) --*

                The status of the replication instance.

              - **AllocatedStorage** *(integer) --*

                The amount of storage (in gigabytes) that is allocated for the replication instance.

              - **InstanceCreateTime** *(datetime) --*

                The time the replication instance was created.

              - **VpcSecurityGroups** *(list) --*

                The VPC security group for the instance.

                - *(dict) --*

                  - **VpcSecurityGroupId** *(string) --*

                    The VPC security group Id.

                  - **Status** *(string) --*

                    The status of the VPC security group.

              - **AvailabilityZone** *(string) --*

                The Availability Zone for the instance.

              - **ReplicationSubnetGroup** *(dict) --*

                The subnet group for the replication instance.

                - **ReplicationSubnetGroupIdentifier** *(string) --*

                  The identifier of the replication instance subnet group.

                - **ReplicationSubnetGroupDescription** *(string) --*

                  A description for the replication subnet group.

                - **VpcId** *(string) --*

                  The ID of the VPC.

                - **SubnetGroupStatus** *(string) --*

                  The status of the subnet group.

                - **Subnets** *(list) --*

                  The subnets that are in the subnet group.

                  - *(dict) --*

                    - **SubnetIdentifier** *(string) --*

                      The subnet identifier.

                    - **SubnetAvailabilityZone** *(dict) --*

                      The Availability Zone of the subnet.

                      - **Name** *(string) --*

                        The name of the availability zone.

                    - **SubnetStatus** *(string) --*

                      The status of the subnet.

              - **PreferredMaintenanceWindow** *(string) --*

                The maintenance window times for the replication instance.

              - **PendingModifiedValues** *(dict) --*

                The pending modification values.

                - **ReplicationInstanceClass** *(string) --*

                  The compute and memory capacity of the replication instance.

                  Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
                  | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

                - **AllocatedStorage** *(integer) --*

                  The amount of storage (in gigabytes) that is allocated for the replication instance.

                - **MultiAZ** *(boolean) --*

                  Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
                  ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

                - **EngineVersion** *(string) --*

                  The engine version number of the replication instance.

              - **MultiAZ** *(boolean) --*

                Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
                ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

              - **EngineVersion** *(string) --*

                The engine version number of the replication instance.

              - **AutoMinorVersionUpgrade** *(boolean) --*

                Boolean value indicating if minor version upgrades will be automatically applied to the
                instance.

              - **KmsKeyId** *(string) --*

                An AWS KMS key identifier that is used to encrypt the data on the replication instance.

                If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
                encryption key.

                AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
                different default encryption key for each AWS Region.

              - **ReplicationInstanceArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication instance.

              - **ReplicationInstancePublicIpAddress** *(string) --*

                The public IP address of the replication instance.

              - **ReplicationInstancePrivateIpAddress** *(string) --*

                The private IP address of the replication instance.

              - **ReplicationInstancePublicIpAddresses** *(list) --*

                One or more public IP addresses for the replication instance.

                - *(string) --*

              - **ReplicationInstancePrivateIpAddresses** *(list) --*

                One or more private IP addresses for the replication instance.

                - *(string) --*

              - **PubliclyAccessible** *(boolean) --*

                Specifies the accessibility options for the replication instance. A value of ``true``
                represents an instance with a public IP address. A value of ``false`` represents an
                instance with a private IP address. The default value is ``true`` .

              - **SecondaryAvailabilityZone** *(string) --*

                The availability zone of the standby replication instance in a Multi-AZ deployment.

              - **FreeUntil** *(datetime) --*

                The expiration date of the free replication instance that is part of the Free DMS program.

              - **DnsNameServers** *(string) --*

                The DNS name servers for the replication instance.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_replication_subnet_group(
        self,
        ReplicationSubnetGroupIdentifier: str,
        ReplicationSubnetGroupDescription: str,
        SubnetIds: List[str],
        Tags: List[ClientCreateReplicationSubnetGroupTagsTypeDef] = None,
    ) -> ClientCreateReplicationSubnetGroupResponseTypeDef:
        """
        Creates a replication subnet group given a list of the subnet IDs in a VPC.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/CreateReplicationSubnetGroup>`_

        **Request Syntax**
        ::

          response = client.create_replication_subnet_group(
              ReplicationSubnetGroupIdentifier='string',
              ReplicationSubnetGroupDescription='string',
              SubnetIds=[
                  'string',
              ],
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type ReplicationSubnetGroupIdentifier: string
        :param ReplicationSubnetGroupIdentifier: **[REQUIRED]**

          The name for the replication subnet group. This value is stored as a lowercase string.

          Constraints: Must contain no more than 255 alphanumeric characters, periods, spaces, underscores,
          or hyphens. Must not be "default".

          Example: ``mySubnetgroup``

        :type ReplicationSubnetGroupDescription: string
        :param ReplicationSubnetGroupDescription: **[REQUIRED]**

          The description for the subnet group.

        :type SubnetIds: list
        :param SubnetIds: **[REQUIRED]**

          One or more subnet IDs to be assigned to the subnet group.

          - *(string) --*

        :type Tags: list
        :param Tags:

          One or more tags to be assigned to the subnet group.

          - *(dict) --*

            - **Key** *(string) --*

              A key is the required name of the tag. The string value can be from 1 to 128 Unicode
              characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
              contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
              (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

            - **Value** *(string) --*

              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
              characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
              contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
              (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationSubnetGroup': {
                    'ReplicationSubnetGroupIdentifier': 'string',
                    'ReplicationSubnetGroupDescription': 'string',
                    'VpcId': 'string',
                    'SubnetGroupStatus': 'string',
                    'Subnets': [
                        {
                            'SubnetIdentifier': 'string',
                            'SubnetAvailabilityZone': {
                                'Name': 'string'
                            },
                            'SubnetStatus': 'string'
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationSubnetGroup** *(dict) --*

              The replication subnet group that was created.

              - **ReplicationSubnetGroupIdentifier** *(string) --*

                The identifier of the replication instance subnet group.

              - **ReplicationSubnetGroupDescription** *(string) --*

                A description for the replication subnet group.

              - **VpcId** *(string) --*

                The ID of the VPC.

              - **SubnetGroupStatus** *(string) --*

                The status of the subnet group.

              - **Subnets** *(list) --*

                The subnets that are in the subnet group.

                - *(dict) --*

                  - **SubnetIdentifier** *(string) --*

                    The subnet identifier.

                  - **SubnetAvailabilityZone** *(dict) --*

                    The Availability Zone of the subnet.

                    - **Name** *(string) --*

                      The name of the availability zone.

                  - **SubnetStatus** *(string) --*

                    The status of the subnet.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_replication_task(
        self,
        ReplicationTaskIdentifier: str,
        SourceEndpointArn: str,
        TargetEndpointArn: str,
        ReplicationInstanceArn: str,
        MigrationType: str,
        TableMappings: str,
        ReplicationTaskSettings: str = None,
        CdcStartTime: datetime = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None,
        Tags: List[ClientCreateReplicationTaskTagsTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        Creates a replication task using the specified parameters.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/CreateReplicationTask>`_

        **Request Syntax**
        ::

          response = client.create_replication_task(
              ReplicationTaskIdentifier='string',
              SourceEndpointArn='string',
              TargetEndpointArn='string',
              ReplicationInstanceArn='string',
              MigrationType='full-load'|'cdc'|'full-load-and-cdc',
              TableMappings='string',
              ReplicationTaskSettings='string',
              CdcStartTime=datetime(2015, 1, 1),
              CdcStartPosition='string',
              CdcStopPosition='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type ReplicationTaskIdentifier: string
        :param ReplicationTaskIdentifier: **[REQUIRED]**

          An identifier for the replication task.

          Constraints:

          * Must contain from 1 to 255 alphanumeric characters or hyphens.

          * First character must be a letter.

          * Cannot end with a hyphen or contain two consecutive hyphens.

        :type SourceEndpointArn: string
        :param SourceEndpointArn: **[REQUIRED]**

          An Amazon Resource Name (ARN) that uniquely identifies the source endpoint.

        :type TargetEndpointArn: string
        :param TargetEndpointArn: **[REQUIRED]**

          An Amazon Resource Name (ARN) that uniquely identifies the target endpoint.

        :type ReplicationInstanceArn: string
        :param ReplicationInstanceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of a replication instance.

        :type MigrationType: string
        :param MigrationType: **[REQUIRED]**

          The migration type. Valid values: ``full-load`` | ``cdc`` | ``full-load-and-cdc``

        :type TableMappings: string
        :param TableMappings: **[REQUIRED]**

          The table mappings for the task, in JSON format. For more information, see `Table Mapping
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html>`__
          in the *AWS Database Migration User Guide.*

        :type ReplicationTaskSettings: string
        :param ReplicationTaskSettings:

          Overall settings for the task, in JSON format. For more information, see `Task Settings
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html>`__
          in the *AWS Database Migration User Guide.*

        :type CdcStartTime: datetime
        :param CdcStartTime:

          Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or
          CdcStartPosition to specify when you want a CDC operation to start. Specifying both values
          results in an error.

          Timestamp Example: --cdc-start-time “2018-03-08T12:12:12”

        :type CdcStartPosition: string
        :param CdcStartPosition:

          Indicates when you want a change data capture (CDC) operation to start. Use either
          CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying
          both values results in an error.

          The value can be in date, checkpoint, or LSN/SCN format.

          Date Example: --cdc-start-position “2018-03-08T12:12:12”

          Checkpoint Example: --cdc-start-position
          "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"
        "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"

          LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”

          .. note::

            When you use this task setting with a source PostgreSQL database, a logical replication slot
            should already be created and associated with the source endpoint. You can verify this by
            setting the ``slotName`` extra connection attribute to the name of this logical replication
            slot. For more information, see `Extra Connection Attributes When Using PostgreSQL as a Source
            for AWS DMS
            <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`__
            .

        :type CdcStopPosition: string
        :param CdcStopPosition:

          Indicates when you want a change data capture (CDC) operation to stop. The value can be either
          server time or commit time.

          Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”

          Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12 “

        :type Tags: list
        :param Tags:

          One or more tags to be assigned to the replication task.

          - *(dict) --*

            - **Key** *(string) --*

              A key is the required name of the tag. The string value can be from 1 to 128 Unicode
              characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
              contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
              (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

            - **Value** *(string) --*

              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
              characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
              contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
              (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationTask': {
                    'ReplicationTaskIdentifier': 'string',
                    'SourceEndpointArn': 'string',
                    'TargetEndpointArn': 'string',
                    'ReplicationInstanceArn': 'string',
                    'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
                    'TableMappings': 'string',
                    'ReplicationTaskSettings': 'string',
                    'Status': 'string',
                    'LastFailureMessage': 'string',
                    'StopReason': 'string',
                    'ReplicationTaskCreationDate': datetime(2015, 1, 1),
                    'ReplicationTaskStartDate': datetime(2015, 1, 1),
                    'CdcStartPosition': 'string',
                    'CdcStopPosition': 'string',
                    'RecoveryCheckpoint': 'string',
                    'ReplicationTaskArn': 'string',
                    'ReplicationTaskStats': {
                        'FullLoadProgressPercent': 123,
                        'ElapsedTimeMillis': 123,
                        'TablesLoaded': 123,
                        'TablesLoading': 123,
                        'TablesQueued': 123,
                        'TablesErrored': 123,
                        'FreshStartDate': datetime(2015, 1, 1),
                        'StartDate': datetime(2015, 1, 1),
                        'StopDate': datetime(2015, 1, 1),
                        'FullLoadStartDate': datetime(2015, 1, 1),
                        'FullLoadFinishDate': datetime(2015, 1, 1)
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationTask** *(dict) --*

              The replication task that was created.

              - **ReplicationTaskIdentifier** *(string) --*

                The user-assigned replication task identifier or name.

                Constraints:

                * Must contain from 1 to 255 alphanumeric characters or hyphens.

                * First character must be a letter.

                * Cannot end with a hyphen or contain two consecutive hyphens.

              - **SourceEndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **TargetEndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **ReplicationInstanceArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication instance.

              - **MigrationType** *(string) --*

                The type of migration.

              - **TableMappings** *(string) --*

                Table mappings specified in the task.

              - **ReplicationTaskSettings** *(string) --*

                The settings for the replication task.

              - **Status** *(string) --*

                The status of the replication task.

              - **LastFailureMessage** *(string) --*

                The last error (failure) message generated for the replication instance.

              - **StopReason** *(string) --*

                The reason the replication task was stopped.

              - **ReplicationTaskCreationDate** *(datetime) --*

                The date the replication task was created.

              - **ReplicationTaskStartDate** *(datetime) --*

                The date the replication task is scheduled to start.

              - **CdcStartPosition** *(string) --*

                Indicates when you want a change data capture (CDC) operation to start. Use either
                ``CdcStartPosition`` or ``CdcStartTime`` to specify when you want the CDC operation to
                start. Specifying both values results in an error.

                The value can be in date, checkpoint, or LSN/SCN format.

                Date Example: --cdc-start-position “2018-03-08T12:12:12”

                Checkpoint Example: --cdc-start-position
                "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"
        "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"

                LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”

              - **CdcStopPosition** *(string) --*

                Indicates when you want a change data capture (CDC) operation to stop. The value can be
                either server time or commit time.

                Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”

                Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12 “

              - **RecoveryCheckpoint** *(string) --*

                Indicates the last checkpoint that occurred during a change data capture (CDC) operation.
                You can provide this value to the ``CdcStartPosition`` parameter to start a CDC operation
                that begins at that checkpoint.

              - **ReplicationTaskArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication task.

              - **ReplicationTaskStats** *(dict) --*

                The statistics for the task, including elapsed time, tables loaded, and table errors.

                - **FullLoadProgressPercent** *(integer) --*

                  The percent complete for the full load migration task.

                - **ElapsedTimeMillis** *(integer) --*

                  The elapsed time of the task, in milliseconds.

                - **TablesLoaded** *(integer) --*

                  The number of tables loaded for this task.

                - **TablesLoading** *(integer) --*

                  The number of tables currently loading for this task.

                - **TablesQueued** *(integer) --*

                  The number of tables queued for this task.

                - **TablesErrored** *(integer) --*

                  The number of errors that have occurred during this task.

                - **FreshStartDate** *(datetime) --*

                  The date the replication task was started either with a fresh start or a target reload.

                - **StartDate** *(datetime) --*

                  The date the replication task was started either with a fresh start or a resume. For more
                  information, see `StartReplicationTaskType
                  <https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html#DMS-StartReplicationTask-request-StartReplicationTaskType>`__
                  .

                - **StopDate** *(datetime) --*

                  The date the replication task was stopped.

                - **FullLoadStartDate** *(datetime) --*

                  The date the the replication task full load was started.

                - **FullLoadFinishDate** *(datetime) --*

                  The date the replication task full load was completed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_certificate(
        self, CertificateArn: str
    ) -> ClientDeleteCertificateResponseTypeDef:
        """
        Deletes the specified certificate.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DeleteCertificate>`_

        **Request Syntax**
        ::

          response = client.delete_certificate(
              CertificateArn='string'
          )
        :type CertificateArn: string
        :param CertificateArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the deleted certificate.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Certificate': {
                    'CertificateIdentifier': 'string',
                    'CertificateCreationDate': datetime(2015, 1, 1),
                    'CertificatePem': 'string',
                    'CertificateWallet': b'bytes',
                    'CertificateArn': 'string',
                    'CertificateOwner': 'string',
                    'ValidFromDate': datetime(2015, 1, 1),
                    'ValidToDate': datetime(2015, 1, 1),
                    'SigningAlgorithm': 'string',
                    'KeyLength': 123
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Certificate** *(dict) --*

              The Secure Sockets Layer (SSL) certificate.

              - **CertificateIdentifier** *(string) --*

                A customer-assigned name for the certificate. Identifiers must begin with a letter; must
                contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain
                two consecutive hyphens.

              - **CertificateCreationDate** *(datetime) --*

                The date that the certificate was created.

              - **CertificatePem** *(string) --*

                The contents of a ``.pem`` file, which contains an X.509 certificate.

              - **CertificateWallet** *(bytes) --*

                The location of an imported Oracle Wallet certificate for use with SSL.

              - **CertificateArn** *(string) --*

                The Amazon Resource Name (ARN) for the certificate.

              - **CertificateOwner** *(string) --*

                The owner of the certificate.

              - **ValidFromDate** *(datetime) --*

                The beginning date that the certificate is valid.

              - **ValidToDate** *(datetime) --*

                The final date that the certificate is valid.

              - **SigningAlgorithm** *(string) --*

                The signing algorithm for the certificate.

              - **KeyLength** *(integer) --*

                The key length of the cryptographic algorithm being used.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_connection(
        self, EndpointArn: str, ReplicationInstanceArn: str
    ) -> ClientDeleteConnectionResponseTypeDef:
        """
        Deletes the connection between a replication instance and an endpoint.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DeleteConnection>`_

        **Request Syntax**
        ::

          response = client.delete_connection(
              EndpointArn='string',
              ReplicationInstanceArn='string'
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

        :type ReplicationInstanceArn: string
        :param ReplicationInstanceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the replication instance.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Connection': {
                    'ReplicationInstanceArn': 'string',
                    'EndpointArn': 'string',
                    'Status': 'string',
                    'LastFailureMessage': 'string',
                    'EndpointIdentifier': 'string',
                    'ReplicationInstanceIdentifier': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Connection** *(dict) --*

              The connection that is being deleted.

              - **ReplicationInstanceArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication instance.

              - **EndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **Status** *(string) --*

                The connection status.

              - **LastFailureMessage** *(string) --*

                The error message when the connection last failed.

              - **EndpointIdentifier** *(string) --*

                The identifier of the endpoint. Identifiers must begin with a letter; must contain only
                ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
                consecutive hyphens.

              - **ReplicationInstanceIdentifier** *(string) --*

                The replication instance identifier. This parameter is stored as a lowercase string.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_endpoint(self, EndpointArn: str) -> ClientDeleteEndpointResponseTypeDef:
        """
        Deletes the specified endpoint.

        .. note::

          All tasks associated with the endpoint must be deleted before you can delete the endpoint.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DeleteEndpoint>`_

        **Request Syntax**
        ::

          response = client.delete_endpoint(
              EndpointArn='string'
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Endpoint': {
                    'EndpointIdentifier': 'string',
                    'EndpointType': 'source'|'target',
                    'EngineName': 'string',
                    'EngineDisplayName': 'string',
                    'Username': 'string',
                    'ServerName': 'string',
                    'Port': 123,
                    'DatabaseName': 'string',
                    'ExtraConnectionAttributes': 'string',
                    'Status': 'string',
                    'KmsKeyId': 'string',
                    'EndpointArn': 'string',
                    'CertificateArn': 'string',
                    'SslMode': 'none'|'require'|'verify-ca'|'verify-full',
                    'ServiceAccessRoleArn': 'string',
                    'ExternalTableDefinition': 'string',
                    'ExternalId': 'string',
                    'DynamoDbSettings': {
                        'ServiceAccessRoleArn': 'string'
                    },
                    'S3Settings': {
                        'ServiceAccessRoleArn': 'string',
                        'ExternalTableDefinition': 'string',
                        'CsvRowDelimiter': 'string',
                        'CsvDelimiter': 'string',
                        'BucketFolder': 'string',
                        'BucketName': 'string',
                        'CompressionType': 'none'|'gzip',
                        'EncryptionMode': 'sse-s3'|'sse-kms',
                        'ServerSideEncryptionKmsKeyId': 'string',
                        'DataFormat': 'csv'|'parquet',
                        'EncodingType': 'plain'|'plain-dictionary'|'rle-dictionary',
                        'DictPageSizeLimit': 123,
                        'RowGroupLength': 123,
                        'DataPageSize': 123,
                        'ParquetVersion': 'parquet-1-0'|'parquet-2-0',
                        'EnableStatistics': True|False,
                        'IncludeOpForFullLoad': True|False,
                        'CdcInsertsOnly': True|False,
                        'TimestampColumnName': 'string',
                        'ParquetTimestampInMillisecond': True|False
                    },
                    'DmsTransferSettings': {
                        'ServiceAccessRoleArn': 'string',
                        'BucketName': 'string'
                    },
                    'MongoDbSettings': {
                        'Username': 'string',
                        'Password': 'string',
                        'ServerName': 'string',
                        'Port': 123,
                        'DatabaseName': 'string',
                        'AuthType': 'no'|'password',
                        'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
                        'NestingLevel': 'none'|'one',
                        'ExtractDocId': 'string',
                        'DocsToInvestigate': 'string',
                        'AuthSource': 'string',
                        'KmsKeyId': 'string'
                    },
                    'KinesisSettings': {
                        'StreamArn': 'string',
                        'MessageFormat': 'json',
                        'ServiceAccessRoleArn': 'string'
                    },
                    'ElasticsearchSettings': {
                        'ServiceAccessRoleArn': 'string',
                        'EndpointUri': 'string',
                        'FullLoadErrorPercentage': 123,
                        'ErrorRetryDuration': 123
                    },
                    'RedshiftSettings': {
                        'AcceptAnyDate': True|False,
                        'AfterConnectScript': 'string',
                        'BucketFolder': 'string',
                        'BucketName': 'string',
                        'ConnectionTimeout': 123,
                        'DatabaseName': 'string',
                        'DateFormat': 'string',
                        'EmptyAsNull': True|False,
                        'EncryptionMode': 'sse-s3'|'sse-kms',
                        'FileTransferUploadStreams': 123,
                        'LoadTimeout': 123,
                        'MaxFileSize': 123,
                        'Password': 'string',
                        'Port': 123,
                        'RemoveQuotes': True|False,
                        'ReplaceInvalidChars': 'string',
                        'ReplaceChars': 'string',
                        'ServerName': 'string',
                        'ServiceAccessRoleArn': 'string',
                        'ServerSideEncryptionKmsKeyId': 'string',
                        'TimeFormat': 'string',
                        'TrimBlanks': True|False,
                        'TruncateColumns': True|False,
                        'Username': 'string',
                        'WriteBufferSize': 123
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Endpoint** *(dict) --*

              The endpoint that was deleted.

              - **EndpointIdentifier** *(string) --*

                The database endpoint identifier. Identifiers must begin with a letter; must contain only
                ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
                consecutive hyphens.

              - **EndpointType** *(string) --*

                The type of endpoint. Valid values are ``source`` and ``target`` .

              - **EngineName** *(string) --*

                The database engine name. Valid values, depending on the EndpointType, include mysql,
                oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
                dynamodb, mongodb, and sqlserver.

              - **EngineDisplayName** *(string) --*

                The expanded name for the engine name. For example, if the ``EngineName`` parameter is
                "aurora," this value would be "Amazon Aurora MySQL."

              - **Username** *(string) --*

                The user name used to connect to the endpoint.

              - **ServerName** *(string) --*

                The name of the server at the endpoint.

              - **Port** *(integer) --*

                The port value used to access the endpoint.

              - **DatabaseName** *(string) --*

                The name of the database at the endpoint.

              - **ExtraConnectionAttributes** *(string) --*

                Additional connection attributes used to connect to the endpoint.

              - **Status** *(string) --*

                The status of the endpoint.

              - **KmsKeyId** *(string) --*

                An AWS KMS key identifier that is used to encrypt the connection parameters for the
                endpoint.

                If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
                encryption key.

                AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
                different default encryption key for each AWS Region.

              - **EndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **CertificateArn** *(string) --*

                The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

              - **SslMode** *(string) --*

                The SSL mode used to connect to the endpoint. The default value is ``none`` .

              - **ServiceAccessRoleArn** *(string) --*

                The Amazon Resource Name (ARN) used by the service access IAM role.

              - **ExternalTableDefinition** *(string) --*

                The external table definition.

              - **ExternalId** *(string) --*

                Value returned by a call to CreateEndpoint that can be used for cross-account validation.
                Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

              - **DynamoDbSettings** *(dict) --*

                The settings for the target DynamoDB database. For more information, see the
                ``DynamoDBSettings`` structure.

                - **ServiceAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) used by the service access IAM role.

              - **S3Settings** *(dict) --*

                The settings for the S3 target endpoint. For more information, see the ``S3Settings``
                structure.

                - **ServiceAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) used by the service access IAM role.

                - **ExternalTableDefinition** *(string) --*

                  The external table definition.

                - **CsvRowDelimiter** *(string) --*

                  The delimiter used to separate rows in the source files. The default is a carriage return
                  (``\\n`` ).

                - **CsvDelimiter** *(string) --*

                  The delimiter used to separate columns in the source files. The default is a comma.

                - **BucketFolder** *(string) --*

                  An optional parameter to set a folder name in the S3 bucket. If provided, tables are
                  created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
                  parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

                - **BucketName** *(string) --*

                  The name of the S3 bucket.

                - **CompressionType** *(string) --*

                  An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
                  the target files. Set to NONE (the default) or do not use to leave the files
                  uncompressed. Applies to both .csv and .parquet file formats.

                - **EncryptionMode** *(string) --*

                  The type of server-side encryption that you want to use for your data. This encryption
                  type is part of the endpoint settings or the extra connections attributes for Amazon S3.
                  You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , you
                  need an AWS Identity and Access Management (IAM) role with permission to allow
                  ``"arn:aws:s3:::dms-*"`` to use the following actions:

                  * ``s3:CreateBucket``

                  * ``s3:ListBucket``

                  * ``s3:DeleteBucket``

                  * ``s3:GetBucketLocation``

                  * ``s3:GetObject``

                  * ``s3:PutObject``

                  * ``s3:DeleteObject``

                  * ``s3:GetObjectVersion``

                  * ``s3:GetBucketPolicy``

                  * ``s3:PutBucketPolicy``

                  * ``s3:DeleteBucketPolicy``

                - **ServerSideEncryptionKmsKeyId** *(string) --*

                  If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID. The
                  key that you use needs an attached policy that enables AWS Identity and Access Management
                  (IAM) user permissions and allows use of the key.

                  Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
                  --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
                  ,BucketFolder=*value* ,BucketName=*value*
                  ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

                - **DataFormat** *(string) --*

                  The format of the data that you want to use for output. You can choose one of the
                  following:

                  * ``csv`` : This is a row-based file format with comma-separated values (.csv).

                  * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features
                  efficient compression and provides faster query response.

                - **EncodingType** *(string) --*

                  The type of encoding you are using:

                  * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
                  repeated values more efficiently. This is the default.

                  * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

                  * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
                  The dictionary is stored in a dictionary page for each column chunk.

                - **DictPageSizeLimit** *(integer) --*

                  The maximum size of an encoded dictionary page of a column. If the dictionary page
                  exceeds this, this column is stored using an encoding type of ``PLAIN`` . This parameter
                  defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it
                  reverts to ``PLAIN`` encoding. This size is used for .parquet file format only.

                - **RowGroupLength** *(integer) --*

                  The number of rows in a row group. A smaller row group size provides faster reads. But as
                  the number of row groups grows, the slower writes become. This parameter defaults to
                  10,000 rows. This number is used for .parquet file format only.

                  If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
                  group length in bytes (64 * 1024 * 1024).

                - **DataPageSize** *(integer) --*

                  The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB).
                  This number is used for .parquet file format only.

                - **ParquetVersion** *(string) --*

                  The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
                  default) or ``parquet_2_0`` .

                - **EnableStatistics** *(boolean) --*

                  A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
                  enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
                  ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
                  for .parquet file format only.

                - **IncludeOpForFullLoad** *(boolean) --*

                  A value that enables a full load to write INSERT operations to the comma-separated value
                  (.csv) output files only to indicate how the rows were added to the source database.

                  .. note::

                    AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

                  For full load, records can only be inserted. By default (the ``false`` setting), no
                  information is recorded in these output files for a full load to indicate that the rows
                  were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
                  ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
                  This allows the format of your target records from a full load to be consistent with the
                  target records from a CDC load.

                  .. note::

                    This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
                    files only. For more information about how these settings work together, see
                    `Indicating Source DB Operations in Migrated S3 Data
                    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
                    in the *AWS Database Migration Service User Guide.* .

                - **CdcInsertsOnly** *(boolean) --*

                  A value that enables a change data capture (CDC) load to write only INSERT operations to
                  .csv or columnar storage (.parquet) output files. By default (the ``false`` setting), the
                  first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D
                  (DELETE). These values indicate whether the row was inserted, updated, or deleted at the
                  source database for a CDC load to the target.

                  If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database
                  are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are
                  recorded depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad``
                  is set to ``true`` , the first field of every CDC record is set to I to indicate the
                  INSERT operation at the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every
                  CDC record is written without a first field to indicate the INSERT operation at the
                  source. For more information about how these settings work together, see `Indicating
                  Source DB Operations in Migrated S3 Data
                  <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
                  in the *AWS Database Migration Service User Guide.* .

                  .. note::

                    AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
                    ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

                - **TimestampColumnName** *(string) --*

                  A value that when nonblank causes AWS DMS to add a column with timestamp information to
                  the endpoint data for an Amazon S3 target.

                  .. note::

                    AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

                  DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your
                  migrated data when you set ``TimestampColumnName`` to a nonblank value.

                  For a full load, each row of this timestamp column contains a timestamp for when the data
                  was transferred from the source to the target by DMS.

                  For a change data capture (CDC) load, each row of the timestamp column contains the
                  timestamp for the commit of that row in the source database.

                  The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By
                  default, the precision of this value is in microseconds. For a CDC load, the rounding of
                  the precision depends on the commit timestamp supported by DMS for the source database.

                  When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
                  the timestamp column that you set with ``TimestampColumnName`` .

                - **ParquetTimestampInMillisecond** *(boolean) --*

                  A value that specifies the precision of any ``TIMESTAMP`` column values that are written
                  to an Amazon S3 object file in .parquet format.

                  .. note::

                    AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and
                    later.

                  When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
                  ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise,
                  DMS writes them with microsecond precision.

                  Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
                  ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
                  are .parquet formatted only if you plan to query or process the data with Athena or AWS
                  Glue.

                  .. note::

                    AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
                    with microsecond precision.

                    Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
                    timestamp column value that is inserted by setting the ``TimestampColumnName``
                    parameter.

              - **DmsTransferSettings** *(dict) --*

                The settings in JSON format for the DMS transfer type of source endpoint.

                Possible settings include the following:

                * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
                bucket.

                * ``BucketName`` - The name of the S3 bucket to use.

                * ``CompressionType`` - An optional parameter to use GZIP to compress the target files. To
                use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed, don't
                use this value.

                Shorthand syntax for these settings is as follows:
                ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

                JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
                "BucketName": "string", "CompressionType": "none"|"gzip" }``

                - **ServiceAccessRoleArn** *(string) --*

                  The IAM role that has permission to access the Amazon S3 bucket.

                - **BucketName** *(string) --*

                  The name of the S3 bucket to use.

              - **MongoDbSettings** *(dict) --*

                The settings for the MongoDB source endpoint. For more information, see the
                ``MongoDbSettings`` structure.

                - **Username** *(string) --*

                  The user name you use to access the MongoDB source endpoint.

                - **Password** *(string) --*

                  The password for the user account you use to access the MongoDB source endpoint.

                - **ServerName** *(string) --*

                  The name of the server on the MongoDB source endpoint.

                - **Port** *(integer) --*

                  The port value for the MongoDB source endpoint.

                - **DatabaseName** *(string) --*

                  The database name on the MongoDB source endpoint.

                - **AuthType** *(string) --*

                  The authentication type you use to access the MongoDB source endpoint.

                  Valid values: NO, PASSWORD

                  When NO is selected, user name and password parameters are not used and can be empty.

                - **AuthMechanism** *(string) --*

                  The authentication mechanism you use to access the MongoDB source endpoint.

                  Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

                  DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
                  SCRAM_SHA_1. This setting is not used when authType=No.

                - **NestingLevel** *(string) --*

                  Specifies either document or table mode.

                  Valid values: NONE, ONE

                  Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

                - **ExtractDocId** *(string) --*

                  Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

                  Default value is false.

                - **DocsToInvestigate** *(string) --*

                  Indicates the number of documents to preview to determine the document organization. Use
                  this setting when ``NestingLevel`` is set to ONE.

                  Must be a positive value greater than 0. Default value is 1000.

                - **AuthSource** *(string) --*

                  The MongoDB database name. This setting is not used when ``authType=NO`` .

                  The default is admin.

                - **KmsKeyId** *(string) --*

                  The AWS KMS key identifier that is used to encrypt the content on the replication
                  instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses
                  your default encryption key. AWS KMS creates the default encryption key for your AWS
                  account. Your AWS account has a different default encryption key for each AWS Region.

              - **KinesisSettings** *(dict) --*

                The settings for the Amazon Kinesis source endpoint. For more information, see the
                ``KinesisSettings`` structure.

                - **StreamArn** *(string) --*

                  The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

                - **MessageFormat** *(string) --*

                  The output format for the records created on the endpoint. The message format is ``JSON``
                  .

                - **ServiceAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
                  Kinesis data stream.

              - **ElasticsearchSettings** *(dict) --*

                The settings for the Elasticsearch source endpoint. For more information, see the
                ``ElasticsearchSettings`` structure.

                - **ServiceAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) used by service to access the IAM role.

                - **EndpointUri** *(string) --*

                  The endpoint for the Elasticsearch cluster.

                - **FullLoadErrorPercentage** *(integer) --*

                  The maximum percentage of records that can fail to be written before a full load
                  operation stops.

                - **ErrorRetryDuration** *(integer) --*

                  The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
                  cluster.

              - **RedshiftSettings** *(dict) --*

                Settings for the Amazon Redshift endpoint.

                - **AcceptAnyDate** *(boolean) --*

                  A value that indicates to allow any date format, including invalid formats such as
                  00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
                  ``false`` (the default).

                  This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with
                  the DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT
                  specification, Amazon Redshift inserts a NULL value into that field.

                - **AfterConnectScript** *(string) --*

                  Code to run after connecting. This parameter should contain the code itself, not the name
                  of a file containing the code.

                - **BucketFolder** *(string) --*

                  The location where the comma-separated value (.csv) files are stored before being
                  uploaded to the S3 bucket.

                - **BucketName** *(string) --*

                  The name of the S3 bucket you want to use

                - **ConnectionTimeout** *(integer) --*

                  A value that sets the amount of time to wait (in milliseconds) before timing out,
                  beginning from when you initially establish a connection.

                - **DatabaseName** *(string) --*

                  The name of the Amazon Redshift data warehouse (service) that you are working with.

                - **DateFormat** *(string) --*

                  The date format that you are using. Valid values are ``auto`` (case-sensitive), your date
                  format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it
                  defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some
                  that aren't supported when you use a date format string.

                  If your date and time values use formats different from each other, set this to ``auto`` .

                - **EmptyAsNull** *(boolean) --*

                  A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
                  NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
                  ``false`` .

                - **EncryptionMode** *(string) --*

                  The type of server-side encryption that you want to use for your data. This encryption
                  type is part of the endpoint settings or the extra connections attributes for Amazon S3.
                  You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
                  create an AWS Identity and Access Management (IAM) role with a policy that allows
                  ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

                - **FileTransferUploadStreams** *(integer) --*

                  The number of threads used to upload a single file. This parameter accepts a value from 1
                  through 64. It defaults to 10.

                - **LoadTimeout** *(integer) --*

                  The amount of time to wait (in milliseconds) before timing out, beginning from when you
                  begin loading.

                - **MaxFileSize** *(integer) --*

                  The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This
                  accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

                - **Password** *(string) --*

                  The password for the user named in the ``username`` property.

                - **Port** *(integer) --*

                  The port number for Amazon Redshift. The default value is 5439.

                - **RemoveQuotes** *(boolean) --*

                  A value that specifies to remove surrounding quotation marks from strings in the incoming
                  data. All characters within the quotation marks, including delimiters, are retained.
                  Choose ``true`` to remove quotation marks. The default is ``false`` .

                - **ReplaceInvalidChars** *(string) --*

                  A list of characters that you want to replace. Use with ``ReplaceChars`` .

                - **ReplaceChars** *(string) --*

                  A value that specifies to replaces the invalid characters specified in
                  ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
                  ``"?"`` .

                - **ServerName** *(string) --*

                  The name of the Amazon Redshift cluster you are using.

                - **ServiceAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
                  service.

                - **ServerSideEncryptionKmsKeyId** *(string) --*

                  The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
                  this key ID. The key that you use needs an attached policy that enables IAM user
                  permissions and allows use of the key.

                - **TimeFormat** *(string) --*

                  The time format that you want to use. Valid values are ``auto`` (case-sensitive),
                  ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10.
                  Using ``auto`` recognizes most strings, even some that aren't supported when you use a
                  time format string.

                  If your date and time values use formats different from each other, set this parameter to
                  ``auto`` .

                - **TrimBlanks** *(boolean) --*

                  A value that specifies to remove the trailing white space characters from a VARCHAR
                  string. This parameter applies only to columns with a VARCHAR data type. Choose ``true``
                  to remove unneeded white space. The default is ``false`` .

                - **TruncateColumns** *(boolean) --*

                  A value that specifies to truncate data in columns to the appropriate number of
                  characters, so that the data fits in the column. This parameter applies only to columns
                  with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
                  to truncate data. The default is ``false`` .

                - **Username** *(string) --*

                  An Amazon Redshift user name for a registered user.

                - **WriteBufferSize** *(integer) --*

                  The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The
                  default is 1,024. Use this setting to tune performance.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_event_subscription(
        self, SubscriptionName: str
    ) -> ClientDeleteEventSubscriptionResponseTypeDef:
        """
        Deletes an AWS DMS event subscription.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DeleteEventSubscription>`_

        **Request Syntax**
        ::

          response = client.delete_event_subscription(
              SubscriptionName='string'
          )
        :type SubscriptionName: string
        :param SubscriptionName: **[REQUIRED]**

          The name of the DMS event notification subscription to be deleted.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EventSubscription': {
                    'CustomerAwsId': 'string',
                    'CustSubscriptionId': 'string',
                    'SnsTopicArn': 'string',
                    'Status': 'string',
                    'SubscriptionCreationTime': 'string',
                    'SourceType': 'string',
                    'SourceIdsList': [
                        'string',
                    ],
                    'EventCategoriesList': [
                        'string',
                    ],
                    'Enabled': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **EventSubscription** *(dict) --*

              The event subscription that was deleted.

              - **CustomerAwsId** *(string) --*

                The AWS customer account associated with the AWS DMS event notification subscription.

              - **CustSubscriptionId** *(string) --*

                The AWS DMS event notification subscription Id.

              - **SnsTopicArn** *(string) --*

                The topic ARN of the AWS DMS event notification subscription.

              - **Status** *(string) --*

                The status of the AWS DMS event notification subscription.

                Constraints:

                Can be one of the following: creating | modifying | deleting | active | no-permission |
                topic-not-exist

                The status "no-permission" indicates that AWS DMS no longer has permission to post to the
                SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
                subscription was created.

              - **SubscriptionCreationTime** *(string) --*

                The time the RDS event notification subscription was created.

              - **SourceType** *(string) --*

                The type of AWS DMS resource that generates events.

                Valid values: replication-instance | replication-server | security-group | replication-task

              - **SourceIdsList** *(list) --*

                A list of source Ids for the event subscription.

                - *(string) --*

              - **EventCategoriesList** *(list) --*

                A lists of event categories.

                - *(string) --*

              - **Enabled** *(boolean) --*

                Boolean value that indicates if the event subscription is enabled.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_replication_instance(
        self, ReplicationInstanceArn: str
    ) -> ClientDeleteReplicationInstanceResponseTypeDef:
        """
        Deletes the specified replication instance.

        .. note::

          You must delete any migration tasks that are associated with the replication instance before you
          can delete it.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DeleteReplicationInstance>`_

        **Request Syntax**
        ::

          response = client.delete_replication_instance(
              ReplicationInstanceArn='string'
          )
        :type ReplicationInstanceArn: string
        :param ReplicationInstanceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the replication instance to be deleted.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationInstance': {
                    'ReplicationInstanceIdentifier': 'string',
                    'ReplicationInstanceClass': 'string',
                    'ReplicationInstanceStatus': 'string',
                    'AllocatedStorage': 123,
                    'InstanceCreateTime': datetime(2015, 1, 1),
                    'VpcSecurityGroups': [
                        {
                            'VpcSecurityGroupId': 'string',
                            'Status': 'string'
                        },
                    ],
                    'AvailabilityZone': 'string',
                    'ReplicationSubnetGroup': {
                        'ReplicationSubnetGroupIdentifier': 'string',
                        'ReplicationSubnetGroupDescription': 'string',
                        'VpcId': 'string',
                        'SubnetGroupStatus': 'string',
                        'Subnets': [
                            {
                                'SubnetIdentifier': 'string',
                                'SubnetAvailabilityZone': {
                                    'Name': 'string'
                                },
                                'SubnetStatus': 'string'
                            },
                        ]
                    },
                    'PreferredMaintenanceWindow': 'string',
                    'PendingModifiedValues': {
                        'ReplicationInstanceClass': 'string',
                        'AllocatedStorage': 123,
                        'MultiAZ': True|False,
                        'EngineVersion': 'string'
                    },
                    'MultiAZ': True|False,
                    'EngineVersion': 'string',
                    'AutoMinorVersionUpgrade': True|False,
                    'KmsKeyId': 'string',
                    'ReplicationInstanceArn': 'string',
                    'ReplicationInstancePublicIpAddress': 'string',
                    'ReplicationInstancePrivateIpAddress': 'string',
                    'ReplicationInstancePublicIpAddresses': [
                        'string',
                    ],
                    'ReplicationInstancePrivateIpAddresses': [
                        'string',
                    ],
                    'PubliclyAccessible': True|False,
                    'SecondaryAvailabilityZone': 'string',
                    'FreeUntil': datetime(2015, 1, 1),
                    'DnsNameServers': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationInstance** *(dict) --*

              The replication instance that was deleted.

              - **ReplicationInstanceIdentifier** *(string) --*

                The replication instance identifier. This parameter is stored as a lowercase string.

                Constraints:

                * Must contain from 1 to 63 alphanumeric characters or hyphens.

                * First character must be a letter.

                * Cannot end with a hyphen or contain two consecutive hyphens.

                Example: ``myrepinstance``

              - **ReplicationInstanceClass** *(string) --*

                The compute and memory capacity of the replication instance.

                Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large |
                dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

              - **ReplicationInstanceStatus** *(string) --*

                The status of the replication instance.

              - **AllocatedStorage** *(integer) --*

                The amount of storage (in gigabytes) that is allocated for the replication instance.

              - **InstanceCreateTime** *(datetime) --*

                The time the replication instance was created.

              - **VpcSecurityGroups** *(list) --*

                The VPC security group for the instance.

                - *(dict) --*

                  - **VpcSecurityGroupId** *(string) --*

                    The VPC security group Id.

                  - **Status** *(string) --*

                    The status of the VPC security group.

              - **AvailabilityZone** *(string) --*

                The Availability Zone for the instance.

              - **ReplicationSubnetGroup** *(dict) --*

                The subnet group for the replication instance.

                - **ReplicationSubnetGroupIdentifier** *(string) --*

                  The identifier of the replication instance subnet group.

                - **ReplicationSubnetGroupDescription** *(string) --*

                  A description for the replication subnet group.

                - **VpcId** *(string) --*

                  The ID of the VPC.

                - **SubnetGroupStatus** *(string) --*

                  The status of the subnet group.

                - **Subnets** *(list) --*

                  The subnets that are in the subnet group.

                  - *(dict) --*

                    - **SubnetIdentifier** *(string) --*

                      The subnet identifier.

                    - **SubnetAvailabilityZone** *(dict) --*

                      The Availability Zone of the subnet.

                      - **Name** *(string) --*

                        The name of the availability zone.

                    - **SubnetStatus** *(string) --*

                      The status of the subnet.

              - **PreferredMaintenanceWindow** *(string) --*

                The maintenance window times for the replication instance.

              - **PendingModifiedValues** *(dict) --*

                The pending modification values.

                - **ReplicationInstanceClass** *(string) --*

                  The compute and memory capacity of the replication instance.

                  Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
                  | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

                - **AllocatedStorage** *(integer) --*

                  The amount of storage (in gigabytes) that is allocated for the replication instance.

                - **MultiAZ** *(boolean) --*

                  Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
                  ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

                - **EngineVersion** *(string) --*

                  The engine version number of the replication instance.

              - **MultiAZ** *(boolean) --*

                Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
                ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

              - **EngineVersion** *(string) --*

                The engine version number of the replication instance.

              - **AutoMinorVersionUpgrade** *(boolean) --*

                Boolean value indicating if minor version upgrades will be automatically applied to the
                instance.

              - **KmsKeyId** *(string) --*

                An AWS KMS key identifier that is used to encrypt the data on the replication instance.

                If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
                encryption key.

                AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
                different default encryption key for each AWS Region.

              - **ReplicationInstanceArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication instance.

              - **ReplicationInstancePublicIpAddress** *(string) --*

                The public IP address of the replication instance.

              - **ReplicationInstancePrivateIpAddress** *(string) --*

                The private IP address of the replication instance.

              - **ReplicationInstancePublicIpAddresses** *(list) --*

                One or more public IP addresses for the replication instance.

                - *(string) --*

              - **ReplicationInstancePrivateIpAddresses** *(list) --*

                One or more private IP addresses for the replication instance.

                - *(string) --*

              - **PubliclyAccessible** *(boolean) --*

                Specifies the accessibility options for the replication instance. A value of ``true``
                represents an instance with a public IP address. A value of ``false`` represents an
                instance with a private IP address. The default value is ``true`` .

              - **SecondaryAvailabilityZone** *(string) --*

                The availability zone of the standby replication instance in a Multi-AZ deployment.

              - **FreeUntil** *(datetime) --*

                The expiration date of the free replication instance that is part of the Free DMS program.

              - **DnsNameServers** *(string) --*

                The DNS name servers for the replication instance.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_replication_subnet_group(
        self, ReplicationSubnetGroupIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes a subnet group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DeleteReplicationSubnetGroup>`_

        **Request Syntax**
        ::

          response = client.delete_replication_subnet_group(
              ReplicationSubnetGroupIdentifier='string'
          )
        :type ReplicationSubnetGroupIdentifier: string
        :param ReplicationSubnetGroupIdentifier: **[REQUIRED]**

          The subnet group name of the replication instance.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_replication_task(self, ReplicationTaskArn: str) -> Dict[str, Any]:
        """
        Deletes the specified replication task.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DeleteReplicationTask>`_

        **Request Syntax**
        ::

          response = client.delete_replication_task(
              ReplicationTaskArn='string'
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the replication task to be deleted.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationTask': {
                    'ReplicationTaskIdentifier': 'string',
                    'SourceEndpointArn': 'string',
                    'TargetEndpointArn': 'string',
                    'ReplicationInstanceArn': 'string',
                    'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
                    'TableMappings': 'string',
                    'ReplicationTaskSettings': 'string',
                    'Status': 'string',
                    'LastFailureMessage': 'string',
                    'StopReason': 'string',
                    'ReplicationTaskCreationDate': datetime(2015, 1, 1),
                    'ReplicationTaskStartDate': datetime(2015, 1, 1),
                    'CdcStartPosition': 'string',
                    'CdcStopPosition': 'string',
                    'RecoveryCheckpoint': 'string',
                    'ReplicationTaskArn': 'string',
                    'ReplicationTaskStats': {
                        'FullLoadProgressPercent': 123,
                        'ElapsedTimeMillis': 123,
                        'TablesLoaded': 123,
                        'TablesLoading': 123,
                        'TablesQueued': 123,
                        'TablesErrored': 123,
                        'FreshStartDate': datetime(2015, 1, 1),
                        'StartDate': datetime(2015, 1, 1),
                        'StopDate': datetime(2015, 1, 1),
                        'FullLoadStartDate': datetime(2015, 1, 1),
                        'FullLoadFinishDate': datetime(2015, 1, 1)
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationTask** *(dict) --*

              The deleted replication task.

              - **ReplicationTaskIdentifier** *(string) --*

                The user-assigned replication task identifier or name.

                Constraints:

                * Must contain from 1 to 255 alphanumeric characters or hyphens.

                * First character must be a letter.

                * Cannot end with a hyphen or contain two consecutive hyphens.

              - **SourceEndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **TargetEndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **ReplicationInstanceArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication instance.

              - **MigrationType** *(string) --*

                The type of migration.

              - **TableMappings** *(string) --*

                Table mappings specified in the task.

              - **ReplicationTaskSettings** *(string) --*

                The settings for the replication task.

              - **Status** *(string) --*

                The status of the replication task.

              - **LastFailureMessage** *(string) --*

                The last error (failure) message generated for the replication instance.

              - **StopReason** *(string) --*

                The reason the replication task was stopped.

              - **ReplicationTaskCreationDate** *(datetime) --*

                The date the replication task was created.

              - **ReplicationTaskStartDate** *(datetime) --*

                The date the replication task is scheduled to start.

              - **CdcStartPosition** *(string) --*

                Indicates when you want a change data capture (CDC) operation to start. Use either
                ``CdcStartPosition`` or ``CdcStartTime`` to specify when you want the CDC operation to
                start. Specifying both values results in an error.

                The value can be in date, checkpoint, or LSN/SCN format.

                Date Example: --cdc-start-position “2018-03-08T12:12:12”

                Checkpoint Example: --cdc-start-position
                "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"
        "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"

                LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”

              - **CdcStopPosition** *(string) --*

                Indicates when you want a change data capture (CDC) operation to stop. The value can be
                either server time or commit time.

                Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”

                Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12 “

              - **RecoveryCheckpoint** *(string) --*

                Indicates the last checkpoint that occurred during a change data capture (CDC) operation.
                You can provide this value to the ``CdcStartPosition`` parameter to start a CDC operation
                that begins at that checkpoint.

              - **ReplicationTaskArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication task.

              - **ReplicationTaskStats** *(dict) --*

                The statistics for the task, including elapsed time, tables loaded, and table errors.

                - **FullLoadProgressPercent** *(integer) --*

                  The percent complete for the full load migration task.

                - **ElapsedTimeMillis** *(integer) --*

                  The elapsed time of the task, in milliseconds.

                - **TablesLoaded** *(integer) --*

                  The number of tables loaded for this task.

                - **TablesLoading** *(integer) --*

                  The number of tables currently loading for this task.

                - **TablesQueued** *(integer) --*

                  The number of tables queued for this task.

                - **TablesErrored** *(integer) --*

                  The number of errors that have occurred during this task.

                - **FreshStartDate** *(datetime) --*

                  The date the replication task was started either with a fresh start or a target reload.

                - **StartDate** *(datetime) --*

                  The date the replication task was started either with a fresh start or a resume. For more
                  information, see `StartReplicationTaskType
                  <https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html#DMS-StartReplicationTask-request-StartReplicationTaskType>`__
                  .

                - **StopDate** *(datetime) --*

                  The date the replication task was stopped.

                - **FullLoadStartDate** *(datetime) --*

                  The date the the replication task full load was started.

                - **FullLoadFinishDate** *(datetime) --*

                  The date the replication task full load was completed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_account_attributes(
        self, *args: Any, **kwargs: Any
    ) -> ClientDescribeAccountAttributesResponseTypeDef:
        """
        Lists all of the AWS DMS attributes for a customer account. These attributes include AWS DMS quotas
        for the account and a unique account identifier in a particular DMS region. DMS quotas include a
        list of resource quotas supported by the account, such as the number of replication instances
        allowed. The description for each resource quota, includes the quota name, current usage toward
        that quota, and the quota's maximum value. DMS uses the unique account identifier to name each
        artifact used by DMS in the given region.

        This command does not take any parameters.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeAccountAttributes>`_

        **Request Syntax**
        ::

          response = client.describe_account_attributes()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AccountQuotas': [
                    {
                        'AccountQuotaName': 'string',
                        'Used': 123,
                        'Max': 123
                    },
                ],
                'UniqueAccountIdentifier': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **AccountQuotas** *(list) --*

              Account quota information.

              - *(dict) --*

                Describes a quota for an AWS account, for example, the number of replication instances
                allowed.

                - **AccountQuotaName** *(string) --*

                  The name of the AWS DMS quota for this AWS account.

                - **Used** *(integer) --*

                  The amount currently used toward the quota maximum.

                - **Max** *(integer) --*

                  The maximum allowed value for the quota.

            - **UniqueAccountIdentifier** *(string) --*

              A unique AWS DMS identifier for an account in a particular AWS Region. The value of this
              identifier has the following format: ``c99999999999`` . DMS uses this identifier to name
              artifacts. For example, DMS uses this identifier to name the default Amazon S3 bucket for
              storing task assessment reports in a given AWS Region. The format of this S3 bucket name is
              the following: ``dms-*AccountNumber* -*UniqueAccountIdentifier* .`` Here is an example name
              for this default S3 bucket: ``dms-111122223333-c44445555666`` .

              .. note::

                AWS DMS supports the ``UniqueAccountIdentifier`` parameter in versions 3.1.4 and later.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_certificates(
        self,
        Filters: List[ClientDescribeCertificatesFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeCertificatesResponseTypeDef:
        """
        Provides a description of the certificate.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeCertificates>`_

        **Request Syntax**
        ::

          response = client.describe_certificates(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker='string'
          )
        :type Filters: list
        :param Filters:

          Filters applied to the certificate described in the form of key-value pairs.

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that the remaining results can be retrieved.

          Default: 10

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous request. If this parameter is specified, the
          response includes only records beyond the marker, up to the vlue specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'Certificates': [
                    {
                        'CertificateIdentifier': 'string',
                        'CertificateCreationDate': datetime(2015, 1, 1),
                        'CertificatePem': 'string',
                        'CertificateWallet': b'bytes',
                        'CertificateArn': 'string',
                        'CertificateOwner': 'string',
                        'ValidFromDate': datetime(2015, 1, 1),
                        'ValidToDate': datetime(2015, 1, 1),
                        'SigningAlgorithm': 'string',
                        'KeyLength': 123
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Marker** *(string) --*

              The pagination token.

            - **Certificates** *(list) --*

              The Secure Sockets Layer (SSL) certificates associated with the replication instance.

              - *(dict) --*

                The SSL certificate that can be used to encrypt connections between the endpoints and the
                replication instance.

                - **CertificateIdentifier** *(string) --*

                  A customer-assigned name for the certificate. Identifiers must begin with a letter; must
                  contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or
                  contain two consecutive hyphens.

                - **CertificateCreationDate** *(datetime) --*

                  The date that the certificate was created.

                - **CertificatePem** *(string) --*

                  The contents of a ``.pem`` file, which contains an X.509 certificate.

                - **CertificateWallet** *(bytes) --*

                  The location of an imported Oracle Wallet certificate for use with SSL.

                - **CertificateArn** *(string) --*

                  The Amazon Resource Name (ARN) for the certificate.

                - **CertificateOwner** *(string) --*

                  The owner of the certificate.

                - **ValidFromDate** *(datetime) --*

                  The beginning date that the certificate is valid.

                - **ValidToDate** *(datetime) --*

                  The final date that the certificate is valid.

                - **SigningAlgorithm** *(string) --*

                  The signing algorithm for the certificate.

                - **KeyLength** *(integer) --*

                  The key length of the cryptographic algorithm being used.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_connections(
        self,
        Filters: List[ClientDescribeConnectionsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeConnectionsResponseTypeDef:
        """
        Describes the status of the connections that have been made between the replication instance and an
        endpoint. Connections are created when you test an endpoint.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeConnections>`_

        **Request Syntax**
        ::

          response = client.describe_connections(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker='string'
          )
        :type Filters: list
        :param Filters:

          The filters applied to the connection.

          Valid filter names: endpoint-arn | replication-instance-arn

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that the remaining results can be retrieved.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous request. If this parameter is specified, the
          response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'Connections': [
                    {
                        'ReplicationInstanceArn': 'string',
                        'EndpointArn': 'string',
                        'Status': 'string',
                        'LastFailureMessage': 'string',
                        'EndpointIdentifier': 'string',
                        'ReplicationInstanceIdentifier': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Marker** *(string) --*

              An optional pagination token provided by a previous request. If this parameter is specified,
              the response includes only records beyond the marker, up to the value specified by
              ``MaxRecords`` .

            - **Connections** *(list) --*

              A description of the connections.

              - *(dict) --*

                - **ReplicationInstanceArn** *(string) --*

                  The Amazon Resource Name (ARN) of the replication instance.

                - **EndpointArn** *(string) --*

                  The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

                - **Status** *(string) --*

                  The connection status.

                - **LastFailureMessage** *(string) --*

                  The error message when the connection last failed.

                - **EndpointIdentifier** *(string) --*

                  The identifier of the endpoint. Identifiers must begin with a letter; must contain only
                  ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
                  consecutive hyphens.

                - **ReplicationInstanceIdentifier** *(string) --*

                  The replication instance identifier. This parameter is stored as a lowercase string.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_endpoint_types(
        self,
        Filters: List[ClientDescribeEndpointTypesFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEndpointTypesResponseTypeDef:
        """
        Returns information about the type of endpoints available.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeEndpointTypes>`_

        **Request Syntax**
        ::

          response = client.describe_endpoint_types(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker='string'
          )
        :type Filters: list
        :param Filters:

          Filters applied to the describe action.

          Valid filter names: engine-name | endpoint-type

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that the remaining results can be retrieved.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous request. If this parameter is specified, the
          response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'SupportedEndpointTypes': [
                    {
                        'EngineName': 'string',
                        'SupportsCDC': True|False,
                        'EndpointType': 'source'|'target',
                        'EngineDisplayName': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Marker** *(string) --*

              An optional pagination token provided by a previous request. If this parameter is specified,
              the response includes only records beyond the marker, up to the value specified by
              ``MaxRecords`` .

            - **SupportedEndpointTypes** *(list) --*

              The types of endpoints that are supported.

              - *(dict) --*

                - **EngineName** *(string) --*

                  The database engine name. Valid values, depending on the EndpointType, include mysql,
                  oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
                  dynamodb, mongodb, and sqlserver.

                - **SupportsCDC** *(boolean) --*

                  Indicates if Change Data Capture (CDC) is supported.

                - **EndpointType** *(string) --*

                  The type of endpoint. Valid values are ``source`` and ``target`` .

                - **EngineDisplayName** *(string) --*

                  The expanded name for the engine name. For example, if the ``EngineName`` parameter is
                  "aurora," this value would be "Amazon Aurora MySQL."

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_endpoints(
        self,
        Filters: List[ClientDescribeEndpointsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEndpointsResponseTypeDef:
        """
        Returns information about the endpoints for your account in the current region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeEndpoints>`_

        **Request Syntax**
        ::

          response = client.describe_endpoints(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker='string'
          )
        :type Filters: list
        :param Filters:

          Filters applied to the describe action.

          Valid filter names: endpoint-arn | endpoint-type | endpoint-id | engine-name

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that the remaining results can be retrieved.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous request. If this parameter is specified, the
          response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'Endpoints': [
                    {
                        'EndpointIdentifier': 'string',
                        'EndpointType': 'source'|'target',
                        'EngineName': 'string',
                        'EngineDisplayName': 'string',
                        'Username': 'string',
                        'ServerName': 'string',
                        'Port': 123,
                        'DatabaseName': 'string',
                        'ExtraConnectionAttributes': 'string',
                        'Status': 'string',
                        'KmsKeyId': 'string',
                        'EndpointArn': 'string',
                        'CertificateArn': 'string',
                        'SslMode': 'none'|'require'|'verify-ca'|'verify-full',
                        'ServiceAccessRoleArn': 'string',
                        'ExternalTableDefinition': 'string',
                        'ExternalId': 'string',
                        'DynamoDbSettings': {
                            'ServiceAccessRoleArn': 'string'
                        },
                        'S3Settings': {
                            'ServiceAccessRoleArn': 'string',
                            'ExternalTableDefinition': 'string',
                            'CsvRowDelimiter': 'string',
                            'CsvDelimiter': 'string',
                            'BucketFolder': 'string',
                            'BucketName': 'string',
                            'CompressionType': 'none'|'gzip',
                            'EncryptionMode': 'sse-s3'|'sse-kms',
                            'ServerSideEncryptionKmsKeyId': 'string',
                            'DataFormat': 'csv'|'parquet',
                            'EncodingType': 'plain'|'plain-dictionary'|'rle-dictionary',
                            'DictPageSizeLimit': 123,
                            'RowGroupLength': 123,
                            'DataPageSize': 123,
                            'ParquetVersion': 'parquet-1-0'|'parquet-2-0',
                            'EnableStatistics': True|False,
                            'IncludeOpForFullLoad': True|False,
                            'CdcInsertsOnly': True|False,
                            'TimestampColumnName': 'string',
                            'ParquetTimestampInMillisecond': True|False
                        },
                        'DmsTransferSettings': {
                            'ServiceAccessRoleArn': 'string',
                            'BucketName': 'string'
                        },
                        'MongoDbSettings': {
                            'Username': 'string',
                            'Password': 'string',
                            'ServerName': 'string',
                            'Port': 123,
                            'DatabaseName': 'string',
                            'AuthType': 'no'|'password',
                            'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
                            'NestingLevel': 'none'|'one',
                            'ExtractDocId': 'string',
                            'DocsToInvestigate': 'string',
                            'AuthSource': 'string',
                            'KmsKeyId': 'string'
                        },
                        'KinesisSettings': {
                            'StreamArn': 'string',
                            'MessageFormat': 'json',
                            'ServiceAccessRoleArn': 'string'
                        },
                        'ElasticsearchSettings': {
                            'ServiceAccessRoleArn': 'string',
                            'EndpointUri': 'string',
                            'FullLoadErrorPercentage': 123,
                            'ErrorRetryDuration': 123
                        },
                        'RedshiftSettings': {
                            'AcceptAnyDate': True|False,
                            'AfterConnectScript': 'string',
                            'BucketFolder': 'string',
                            'BucketName': 'string',
                            'ConnectionTimeout': 123,
                            'DatabaseName': 'string',
                            'DateFormat': 'string',
                            'EmptyAsNull': True|False,
                            'EncryptionMode': 'sse-s3'|'sse-kms',
                            'FileTransferUploadStreams': 123,
                            'LoadTimeout': 123,
                            'MaxFileSize': 123,
                            'Password': 'string',
                            'Port': 123,
                            'RemoveQuotes': True|False,
                            'ReplaceInvalidChars': 'string',
                            'ReplaceChars': 'string',
                            'ServerName': 'string',
                            'ServiceAccessRoleArn': 'string',
                            'ServerSideEncryptionKmsKeyId': 'string',
                            'TimeFormat': 'string',
                            'TrimBlanks': True|False,
                            'TruncateColumns': True|False,
                            'Username': 'string',
                            'WriteBufferSize': 123
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Marker** *(string) --*

              An optional pagination token provided by a previous request. If this parameter is specified,
              the response includes only records beyond the marker, up to the value specified by
              ``MaxRecords`` .

            - **Endpoints** *(list) --*

              Endpoint description.

              - *(dict) --*

                - **EndpointIdentifier** *(string) --*

                  The database endpoint identifier. Identifiers must begin with a letter; must contain only
                  ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
                  consecutive hyphens.

                - **EndpointType** *(string) --*

                  The type of endpoint. Valid values are ``source`` and ``target`` .

                - **EngineName** *(string) --*

                  The database engine name. Valid values, depending on the EndpointType, include mysql,
                  oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
                  dynamodb, mongodb, and sqlserver.

                - **EngineDisplayName** *(string) --*

                  The expanded name for the engine name. For example, if the ``EngineName`` parameter is
                  "aurora," this value would be "Amazon Aurora MySQL."

                - **Username** *(string) --*

                  The user name used to connect to the endpoint.

                - **ServerName** *(string) --*

                  The name of the server at the endpoint.

                - **Port** *(integer) --*

                  The port value used to access the endpoint.

                - **DatabaseName** *(string) --*

                  The name of the database at the endpoint.

                - **ExtraConnectionAttributes** *(string) --*

                  Additional connection attributes used to connect to the endpoint.

                - **Status** *(string) --*

                  The status of the endpoint.

                - **KmsKeyId** *(string) --*

                  An AWS KMS key identifier that is used to encrypt the connection parameters for the
                  endpoint.

                  If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your
                  default encryption key.

                  AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
                  different default encryption key for each AWS Region.

                - **EndpointArn** *(string) --*

                  The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

                - **CertificateArn** *(string) --*

                  The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

                - **SslMode** *(string) --*

                  The SSL mode used to connect to the endpoint. The default value is ``none`` .

                - **ServiceAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) used by the service access IAM role.

                - **ExternalTableDefinition** *(string) --*

                  The external table definition.

                - **ExternalId** *(string) --*

                  Value returned by a call to CreateEndpoint that can be used for cross-account validation.
                  Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

                - **DynamoDbSettings** *(dict) --*

                  The settings for the target DynamoDB database. For more information, see the
                  ``DynamoDBSettings`` structure.

                  - **ServiceAccessRoleArn** *(string) --*

                    The Amazon Resource Name (ARN) used by the service access IAM role.

                - **S3Settings** *(dict) --*

                  The settings for the S3 target endpoint. For more information, see the ``S3Settings``
                  structure.

                  - **ServiceAccessRoleArn** *(string) --*

                    The Amazon Resource Name (ARN) used by the service access IAM role.

                  - **ExternalTableDefinition** *(string) --*

                    The external table definition.

                  - **CsvRowDelimiter** *(string) --*

                    The delimiter used to separate rows in the source files. The default is a carriage
                    return (``\\n`` ).

                  - **CsvDelimiter** *(string) --*

                    The delimiter used to separate columns in the source files. The default is a comma.

                  - **BucketFolder** *(string) --*

                    An optional parameter to set a folder name in the S3 bucket. If provided, tables are
                    created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
                    parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

                  - **BucketName** *(string) --*

                    The name of the S3 bucket.

                  - **CompressionType** *(string) --*

                    An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
                    the target files. Set to NONE (the default) or do not use to leave the files
                    uncompressed. Applies to both .csv and .parquet file formats.

                  - **EncryptionMode** *(string) --*

                    The type of server-side encryption that you want to use for your data. This encryption
                    type is part of the endpoint settings or the extra connections attributes for Amazon
                    S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
                    you need an AWS Identity and Access Management (IAM) role with permission to allow
                    ``"arn:aws:s3:::dms-*"`` to use the following actions:

                    * ``s3:CreateBucket``

                    * ``s3:ListBucket``

                    * ``s3:DeleteBucket``

                    * ``s3:GetBucketLocation``

                    * ``s3:GetObject``

                    * ``s3:PutObject``

                    * ``s3:DeleteObject``

                    * ``s3:GetObjectVersion``

                    * ``s3:GetBucketPolicy``

                    * ``s3:PutBucketPolicy``

                    * ``s3:DeleteBucketPolicy``

                  - **ServerSideEncryptionKmsKeyId** *(string) --*

                    If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID.
                    The key that you use needs an attached policy that enables AWS Identity and Access
                    Management (IAM) user permissions and allows use of the key.

                    Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
                    --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
                    ,BucketFolder=*value* ,BucketName=*value*
                    ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

                  - **DataFormat** *(string) --*

                    The format of the data that you want to use for output. You can choose one of the
                    following:

                    * ``csv`` : This is a row-based file format with comma-separated values (.csv).

                    * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that
                    features efficient compression and provides faster query response.

                  - **EncodingType** *(string) --*

                    The type of encoding you are using:

                    * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
                    repeated values more efficiently. This is the default.

                    * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

                    * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
                    The dictionary is stored in a dictionary page for each column chunk.

                  - **DictPageSizeLimit** *(integer) --*

                    The maximum size of an encoded dictionary page of a column. If the dictionary page
                    exceeds this, this column is stored using an encoding type of ``PLAIN`` . This
                    parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page
                    before it reverts to ``PLAIN`` encoding. This size is used for .parquet file format
                    only.

                  - **RowGroupLength** *(integer) --*

                    The number of rows in a row group. A smaller row group size provides faster reads. But
                    as the number of row groups grows, the slower writes become. This parameter defaults to
                    10,000 rows. This number is used for .parquet file format only.

                    If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
                    group length in bytes (64 * 1024 * 1024).

                  - **DataPageSize** *(integer) --*

                    The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1
                    MiB). This number is used for .parquet file format only.

                  - **ParquetVersion** *(string) --*

                    The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
                    default) or ``parquet_2_0`` .

                  - **EnableStatistics** *(boolean) --*

                    A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
                    enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
                    ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
                    for .parquet file format only.

                  - **IncludeOpForFullLoad** *(boolean) --*

                    A value that enables a full load to write INSERT operations to the comma-separated
                    value (.csv) output files only to indicate how the rows were added to the source
                    database.

                    .. note::

                      AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

                    For full load, records can only be inserted. By default (the ``false`` setting), no
                    information is recorded in these output files for a full load to indicate that the rows
                    were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
                    ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
                    This allows the format of your target records from a full load to be consistent with
                    the target records from a CDC load.

                    .. note::

                      This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
                      files only. For more information about how these settings work together, see
                      `Indicating Source DB Operations in Migrated S3 Data
                      <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
                      in the *AWS Database Migration Service User Guide.* .

                  - **CdcInsertsOnly** *(boolean) --*

                    A value that enables a change data capture (CDC) load to write only INSERT operations
                    to .csv or columnar storage (.parquet) output files. By default (the ``false``
                    setting), the first field in a .csv or .parquet record contains the letter I (INSERT),
                    U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated,
                    or deleted at the source database for a CDC load to the target.

                    If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source
                    database are migrated to the .csv or .parquet file. For .csv format only, how these
                    INSERTs are recorded depends on the value of ``IncludeOpForFullLoad`` . If
                    ``IncludeOpForFullLoad`` is set to ``true`` , the first field of every CDC record is
                    set to I to indicate the INSERT operation at the source. If ``IncludeOpForFullLoad`` is
                    set to ``false`` , every CDC record is written without a first field to indicate the
                    INSERT operation at the source. For more information about how these settings work
                    together, see `Indicating Source DB Operations in Migrated S3 Data
                    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
                    in the *AWS Database Migration Service User Guide.* .

                    .. note::

                      AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
                      ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

                  - **TimestampColumnName** *(string) --*

                    A value that when nonblank causes AWS DMS to add a column with timestamp information to
                    the endpoint data for an Amazon S3 target.

                    .. note::

                      AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

                    DMS includes an additional ``STRING`` column in the .csv or .parquet object files of
                    your migrated data when you set ``TimestampColumnName`` to a nonblank value.

                    For a full load, each row of this timestamp column contains a timestamp for when the
                    data was transferred from the source to the target by DMS.

                    For a change data capture (CDC) load, each row of the timestamp column contains the
                    timestamp for the commit of that row in the source database.

                    The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` .
                    By default, the precision of this value is in microseconds. For a CDC load, the
                    rounding of the precision depends on the commit timestamp supported by DMS for the
                    source database.

                    When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
                    the timestamp column that you set with ``TimestampColumnName`` .

                  - **ParquetTimestampInMillisecond** *(boolean) --*

                    A value that specifies the precision of any ``TIMESTAMP`` column values that are
                    written to an Amazon S3 object file in .parquet format.

                    .. note::

                      AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4
                      and later.

                    When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
                    ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision.
                    Otherwise, DMS writes them with microsecond precision.

                    Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
                    ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
                    are .parquet formatted only if you plan to query or process the data with Athena or AWS
                    Glue.

                    .. note::

                      AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
                      with microsecond precision.

                      Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
                      timestamp column value that is inserted by setting the ``TimestampColumnName``
                      parameter.

                - **DmsTransferSettings** *(dict) --*

                  The settings in JSON format for the DMS transfer type of source endpoint.

                  Possible settings include the following:

                  * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
                  bucket.

                  * ``BucketName`` - The name of the S3 bucket to use.

                  * ``CompressionType`` - An optional parameter to use GZIP to compress the target files.
                  To use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed,
                  don't use this value.

                  Shorthand syntax for these settings is as follows:
                  ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

                  JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
                  "BucketName": "string", "CompressionType": "none"|"gzip" }``

                  - **ServiceAccessRoleArn** *(string) --*

                    The IAM role that has permission to access the Amazon S3 bucket.

                  - **BucketName** *(string) --*

                    The name of the S3 bucket to use.

                - **MongoDbSettings** *(dict) --*

                  The settings for the MongoDB source endpoint. For more information, see the
                  ``MongoDbSettings`` structure.

                  - **Username** *(string) --*

                    The user name you use to access the MongoDB source endpoint.

                  - **Password** *(string) --*

                    The password for the user account you use to access the MongoDB source endpoint.

                  - **ServerName** *(string) --*

                    The name of the server on the MongoDB source endpoint.

                  - **Port** *(integer) --*

                    The port value for the MongoDB source endpoint.

                  - **DatabaseName** *(string) --*

                    The database name on the MongoDB source endpoint.

                  - **AuthType** *(string) --*

                    The authentication type you use to access the MongoDB source endpoint.

                    Valid values: NO, PASSWORD

                    When NO is selected, user name and password parameters are not used and can be empty.

                  - **AuthMechanism** *(string) --*

                    The authentication mechanism you use to access the MongoDB source endpoint.

                    Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

                    DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
                    SCRAM_SHA_1. This setting is not used when authType=No.

                  - **NestingLevel** *(string) --*

                    Specifies either document or table mode.

                    Valid values: NONE, ONE

                    Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

                  - **ExtractDocId** *(string) --*

                    Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

                    Default value is false.

                  - **DocsToInvestigate** *(string) --*

                    Indicates the number of documents to preview to determine the document organization.
                    Use this setting when ``NestingLevel`` is set to ONE.

                    Must be a positive value greater than 0. Default value is 1000.

                  - **AuthSource** *(string) --*

                    The MongoDB database name. This setting is not used when ``authType=NO`` .

                    The default is admin.

                  - **KmsKeyId** *(string) --*

                    The AWS KMS key identifier that is used to encrypt the content on the replication
                    instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS
                    uses your default encryption key. AWS KMS creates the default encryption key for your
                    AWS account. Your AWS account has a different default encryption key for each AWS
                    Region.

                - **KinesisSettings** *(dict) --*

                  The settings for the Amazon Kinesis source endpoint. For more information, see the
                  ``KinesisSettings`` structure.

                  - **StreamArn** *(string) --*

                    The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

                  - **MessageFormat** *(string) --*

                    The output format for the records created on the endpoint. The message format is
                    ``JSON`` .

                  - **ServiceAccessRoleArn** *(string) --*

                    The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
                    Kinesis data stream.

                - **ElasticsearchSettings** *(dict) --*

                  The settings for the Elasticsearch source endpoint. For more information, see the
                  ``ElasticsearchSettings`` structure.

                  - **ServiceAccessRoleArn** *(string) --*

                    The Amazon Resource Name (ARN) used by service to access the IAM role.

                  - **EndpointUri** *(string) --*

                    The endpoint for the Elasticsearch cluster.

                  - **FullLoadErrorPercentage** *(integer) --*

                    The maximum percentage of records that can fail to be written before a full load
                    operation stops.

                  - **ErrorRetryDuration** *(integer) --*

                    The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
                    cluster.

                - **RedshiftSettings** *(dict) --*

                  Settings for the Amazon Redshift endpoint.

                  - **AcceptAnyDate** *(boolean) --*

                    A value that indicates to allow any date format, including invalid formats such as
                    00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
                    ``false`` (the default).

                    This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE
                    with the DATEFORMAT parameter. If the date format for the data doesn't match the
                    DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.

                  - **AfterConnectScript** *(string) --*

                    Code to run after connecting. This parameter should contain the code itself, not the
                    name of a file containing the code.

                  - **BucketFolder** *(string) --*

                    The location where the comma-separated value (.csv) files are stored before being
                    uploaded to the S3 bucket.

                  - **BucketName** *(string) --*

                    The name of the S3 bucket you want to use

                  - **ConnectionTimeout** *(integer) --*

                    A value that sets the amount of time to wait (in milliseconds) before timing out,
                    beginning from when you initially establish a connection.

                  - **DatabaseName** *(string) --*

                    The name of the Amazon Redshift data warehouse (service) that you are working with.

                  - **DateFormat** *(string) --*

                    The date format that you are using. Valid values are ``auto`` (case-sensitive), your
                    date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL),
                    it defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even
                    some that aren't supported when you use a date format string.

                    If your date and time values use formats different from each other, set this to
                    ``auto`` .

                  - **EmptyAsNull** *(boolean) --*

                    A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
                    NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
                    ``false`` .

                  - **EncryptionMode** *(string) --*

                    The type of server-side encryption that you want to use for your data. This encryption
                    type is part of the endpoint settings or the extra connections attributes for Amazon
                    S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
                    create an AWS Identity and Access Management (IAM) role with a policy that allows
                    ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

                  - **FileTransferUploadStreams** *(integer) --*

                    The number of threads used to upload a single file. This parameter accepts a value from
                    1 through 64. It defaults to 10.

                  - **LoadTimeout** *(integer) --*

                    The amount of time to wait (in milliseconds) before timing out, beginning from when you
                    begin loading.

                  - **MaxFileSize** *(integer) --*

                    The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift.
                    This accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

                  - **Password** *(string) --*

                    The password for the user named in the ``username`` property.

                  - **Port** *(integer) --*

                    The port number for Amazon Redshift. The default value is 5439.

                  - **RemoveQuotes** *(boolean) --*

                    A value that specifies to remove surrounding quotation marks from strings in the
                    incoming data. All characters within the quotation marks, including delimiters, are
                    retained. Choose ``true`` to remove quotation marks. The default is ``false`` .

                  - **ReplaceInvalidChars** *(string) --*

                    A list of characters that you want to replace. Use with ``ReplaceChars`` .

                  - **ReplaceChars** *(string) --*

                    A value that specifies to replaces the invalid characters specified in
                    ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
                    ``"?"`` .

                  - **ServerName** *(string) --*

                    The name of the Amazon Redshift cluster you are using.

                  - **ServiceAccessRoleArn** *(string) --*

                    The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
                    service.

                  - **ServerSideEncryptionKmsKeyId** *(string) --*

                    The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
                    this key ID. The key that you use needs an attached policy that enables IAM user
                    permissions and allows use of the key.

                  - **TimeFormat** *(string) --*

                    The time format that you want to use. Valid values are ``auto`` (case-sensitive),
                    ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to
                    10. Using ``auto`` recognizes most strings, even some that aren't supported when you
                    use a time format string.

                    If your date and time values use formats different from each other, set this parameter
                    to ``auto`` .

                  - **TrimBlanks** *(boolean) --*

                    A value that specifies to remove the trailing white space characters from a VARCHAR
                    string. This parameter applies only to columns with a VARCHAR data type. Choose
                    ``true`` to remove unneeded white space. The default is ``false`` .

                  - **TruncateColumns** *(boolean) --*

                    A value that specifies to truncate data in columns to the appropriate number of
                    characters, so that the data fits in the column. This parameter applies only to columns
                    with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
                    to truncate data. The default is ``false`` .

                  - **Username** *(string) --*

                    An Amazon Redshift user name for a registered user.

                  - **WriteBufferSize** *(integer) --*

                    The size of the write buffer to use in rows. Valid values range from 1 through 2,048.
                    The default is 1,024. Use this setting to tune performance.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_event_categories(
        self,
        SourceType: str = None,
        Filters: List[ClientDescribeEventCategoriesFiltersTypeDef] = None,
    ) -> ClientDescribeEventCategoriesResponseTypeDef:
        """
        Lists categories for all event source types, or, if specified, for a specified source type. You can
        see a list of the event categories and source types in `Working with Events and Notifications
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html>`__ in the *AWS Database
        Migration Service User Guide.*

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeEventCategories>`_

        **Request Syntax**
        ::

          response = client.describe_event_categories(
              SourceType='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ]
          )
        :type SourceType: string
        :param SourceType:

          The type of AWS DMS resource that generates events.

          Valid values: replication-instance | replication-task

        :type Filters: list
        :param Filters:

          Filters applied to the action.

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EventCategoryGroupList': [
                    {
                        'SourceType': 'string',
                        'EventCategories': [
                            'string',
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **EventCategoryGroupList** *(list) --*

              A list of event categories.

              - *(dict) --*

                - **SourceType** *(string) --*

                  The type of AWS DMS resource that generates events.

                  Valid values: replication-instance | replication-server | security-group |
                  replication-task

                - **EventCategories** *(list) --*

                  A list of event categories from a source type that you've chosen.

                  - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_event_subscriptions(
        self,
        SubscriptionName: str = None,
        Filters: List[ClientDescribeEventSubscriptionsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEventSubscriptionsResponseTypeDef:
        """
        Lists all the event subscriptions for a customer account. The description of a subscription
        includes ``SubscriptionName`` , ``SNSTopicARN`` , ``CustomerID`` , ``SourceType`` , ``SourceID`` ,
        ``CreationTime`` , and ``Status`` .

        If you specify ``SubscriptionName`` , this action lists the description for that subscription.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeEventSubscriptions>`_

        **Request Syntax**
        ::

          response = client.describe_event_subscriptions(
              SubscriptionName='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker='string'
          )
        :type SubscriptionName: string
        :param SubscriptionName:

          The name of the AWS DMS event subscription to be described.

        :type Filters: list
        :param Filters:

          Filters applied to the action.

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that the remaining results can be retrieved.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous request. If this parameter is specified, the
          response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'EventSubscriptionsList': [
                    {
                        'CustomerAwsId': 'string',
                        'CustSubscriptionId': 'string',
                        'SnsTopicArn': 'string',
                        'Status': 'string',
                        'SubscriptionCreationTime': 'string',
                        'SourceType': 'string',
                        'SourceIdsList': [
                            'string',
                        ],
                        'EventCategoriesList': [
                            'string',
                        ],
                        'Enabled': True|False
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Marker** *(string) --*

              An optional pagination token provided by a previous request. If this parameter is specified,
              the response includes only records beyond the marker, up to the value specified by
              ``MaxRecords`` .

            - **EventSubscriptionsList** *(list) --*

              A list of event subscriptions.

              - *(dict) --*

                - **CustomerAwsId** *(string) --*

                  The AWS customer account associated with the AWS DMS event notification subscription.

                - **CustSubscriptionId** *(string) --*

                  The AWS DMS event notification subscription Id.

                - **SnsTopicArn** *(string) --*

                  The topic ARN of the AWS DMS event notification subscription.

                - **Status** *(string) --*

                  The status of the AWS DMS event notification subscription.

                  Constraints:

                  Can be one of the following: creating | modifying | deleting | active | no-permission |
                  topic-not-exist

                  The status "no-permission" indicates that AWS DMS no longer has permission to post to the
                  SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
                  subscription was created.

                - **SubscriptionCreationTime** *(string) --*

                  The time the RDS event notification subscription was created.

                - **SourceType** *(string) --*

                  The type of AWS DMS resource that generates events.

                  Valid values: replication-instance | replication-server | security-group |
                  replication-task

                - **SourceIdsList** *(list) --*

                  A list of source Ids for the event subscription.

                  - *(string) --*

                - **EventCategoriesList** *(list) --*

                  A lists of event categories.

                  - *(string) --*

                - **Enabled** *(boolean) --*

                  Boolean value that indicates if the event subscription is enabled.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_events(
        self,
        SourceIdentifier: str = None,
        SourceType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[ClientDescribeEventsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeEventsResponseTypeDef:
        """
        Lists events for a given source identifier and source type. You can also specify a start and end
        time. For more information on AWS DMS events, see `Working with Events and Notifications
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html>`__ in the *AWS Database
        Migration User Guide.*

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeEvents>`_

        **Request Syntax**
        ::

          response = client.describe_events(
              SourceIdentifier='string',
              SourceType='replication-instance',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Duration=123,
              EventCategories=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker='string'
          )
        :type SourceIdentifier: string
        :param SourceIdentifier:

          The identifier of an event source.

        :type SourceType: string
        :param SourceType:

          The type of AWS DMS resource that generates events.

          Valid values: replication-instance | replication-task

        :type StartTime: datetime
        :param StartTime:

          The start time for the events to be listed.

        :type EndTime: datetime
        :param EndTime:

          The end time for the events to be listed.

        :type Duration: integer
        :param Duration:

          The duration of the events to be listed.

        :type EventCategories: list
        :param EventCategories:

          A list of event categories for the source type that you've chosen.

          - *(string) --*

        :type Filters: list
        :param Filters:

          Filters applied to the action.

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that the remaining results can be retrieved.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous request. If this parameter is specified, the
          response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'Events': [
                    {
                        'SourceIdentifier': 'string',
                        'SourceType': 'replication-instance',
                        'Message': 'string',
                        'EventCategories': [
                            'string',
                        ],
                        'Date': datetime(2015, 1, 1)
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Marker** *(string) --*

              An optional pagination token provided by a previous request. If this parameter is specified,
              the response includes only records beyond the marker, up to the value specified by
              ``MaxRecords`` .

            - **Events** *(list) --*

              The events described.

              - *(dict) --*

                - **SourceIdentifier** *(string) --*

                  The identifier of an event source.

                - **SourceType** *(string) --*

                  The type of AWS DMS resource that generates events.

                  Valid values: replication-instance | endpoint | replication-task

                - **Message** *(string) --*

                  The event message.

                - **EventCategories** *(list) --*

                  The event categories available for the specified source type.

                  - *(string) --*

                - **Date** *(datetime) --*

                  The date of the event.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_orderable_replication_instances(
        self, MaxRecords: int = None, Marker: str = None
    ) -> ClientDescribeOrderableReplicationInstancesResponseTypeDef:
        """
        Returns information about the replication instance types that can be created in the specified
        region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeOrderableReplicationInstances>`_

        **Request Syntax**
        ::

          response = client.describe_orderable_replication_instances(
              MaxRecords=123,
              Marker='string'
          )
        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that the remaining results can be retrieved.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous request. If this parameter is specified, the
          response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'OrderableReplicationInstances': [
                    {
                        'EngineVersion': 'string',
                        'ReplicationInstanceClass': 'string',
                        'StorageType': 'string',
                        'MinAllocatedStorage': 123,
                        'MaxAllocatedStorage': 123,
                        'DefaultAllocatedStorage': 123,
                        'IncludedAllocatedStorage': 123,
                        'AvailabilityZones': [
                            'string',
                        ],
                        'ReleaseStatus': 'beta'
                    },
                ],
                'Marker': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **OrderableReplicationInstances** *(list) --*

              The order-able replication instances available.

              - *(dict) --*

                - **EngineVersion** *(string) --*

                  The version of the replication engine.

                - **ReplicationInstanceClass** *(string) --*

                  The compute and memory capacity of the replication instance.

                  Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
                  | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

                - **StorageType** *(string) --*

                  The type of storage used by the replication instance.

                - **MinAllocatedStorage** *(integer) --*

                  The minimum amount of storage (in gigabytes) that can be allocated for the replication
                  instance.

                - **MaxAllocatedStorage** *(integer) --*

                  The minimum amount of storage (in gigabytes) that can be allocated for the replication
                  instance.

                - **DefaultAllocatedStorage** *(integer) --*

                  The default amount of storage (in gigabytes) that is allocated for the replication
                  instance.

                - **IncludedAllocatedStorage** *(integer) --*

                  The amount of storage (in gigabytes) that is allocated for the replication instance.

                - **AvailabilityZones** *(list) --*

                  List of Availability Zones for this replication instance.

                  - *(string) --*

                - **ReleaseStatus** *(string) --*

                  The value returned when the specified ``EngineVersion`` of the replication instance is in
                  Beta or test mode. This indicates some features might not work as expected.

                  .. note::

                    AWS DMS supports the ``ReleaseStatus`` parameter in versions 3.1.4 and later.

            - **Marker** *(string) --*

              An optional pagination token provided by a previous request. If this parameter is specified,
              the response includes only records beyond the marker, up to the value specified by
              ``MaxRecords`` .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_pending_maintenance_actions(
        self,
        ReplicationInstanceArn: str = None,
        Filters: List[ClientDescribePendingMaintenanceActionsFiltersTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> ClientDescribePendingMaintenanceActionsResponseTypeDef:
        """
        For internal use only

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribePendingMaintenanceActions>`_

        **Request Syntax**
        ::

          response = client.describe_pending_maintenance_actions(
              ReplicationInstanceArn='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              Marker='string',
              MaxRecords=123
          )
        :type ReplicationInstanceArn: string
        :param ReplicationInstanceArn:

          The Amazon Resource Name (ARN) of the replication instance.

        :type Filters: list
        :param Filters:

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous request. If this parameter is specified, the
          response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that the remaining results can be retrieved.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PendingMaintenanceActions': [
                    {
                        'ResourceIdentifier': 'string',
                        'PendingMaintenanceActionDetails': [
                            {
                                'Action': 'string',
                                'AutoAppliedAfterDate': datetime(2015, 1, 1),
                                'ForcedApplyDate': datetime(2015, 1, 1),
                                'OptInStatus': 'string',
                                'CurrentApplyDate': datetime(2015, 1, 1),
                                'Description': 'string'
                            },
                        ]
                    },
                ],
                'Marker': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **PendingMaintenanceActions** *(list) --*

              The pending maintenance action.

              - *(dict) --*

                - **ResourceIdentifier** *(string) --*

                  The Amazon Resource Name (ARN) of the DMS resource that the pending maintenance action
                  applies to. For information about creating an ARN, see `Constructing an Amazon Resource
                  Name (ARN) for AWS DMS
                  <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.AWS.ARN.html>`__ in
                  the DMS documentation.

                - **PendingMaintenanceActionDetails** *(list) --*

                  Detailed information about the pending maintenance action.

                  - *(dict) --*

                    - **Action** *(string) --*

                      The type of pending maintenance action that is available for the resource.

                    - **AutoAppliedAfterDate** *(datetime) --*

                      The date of the maintenance window when the action will be applied. The maintenance
                      action will be applied to the resource during its first maintenance window after this
                      date. If this date is specified, any ``next-maintenance`` opt-in requests are ignored.

                    - **ForcedApplyDate** *(datetime) --*

                      The date when the maintenance action will be automatically applied. The maintenance
                      action will be applied to the resource on this date regardless of the maintenance
                      window for the resource. If this date is specified, any ``immediate`` opt-in requests
                      are ignored.

                    - **OptInStatus** *(string) --*

                      Indicates the type of opt-in request that has been received for the resource.

                    - **CurrentApplyDate** *(datetime) --*

                      The effective date when the pending maintenance action will be applied to the
                      resource. This date takes into account opt-in requests received from the
                      ``ApplyPendingMaintenanceAction`` API, the ``AutoAppliedAfterDate`` , and the
                      ``ForcedApplyDate`` . This value is blank if an opt-in request has not been received
                      and nothing has been specified as ``AutoAppliedAfterDate`` or ``ForcedApplyDate`` .

                    - **Description** *(string) --*

                      A description providing more detail about the maintenance action.

            - **Marker** *(string) --*

              An optional pagination token provided by a previous request. If this parameter is specified,
              the response includes only records beyond the marker, up to the value specified by
              ``MaxRecords`` .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_refresh_schemas_status(
        self, EndpointArn: str
    ) -> ClientDescribeRefreshSchemasStatusResponseTypeDef:
        """
        Returns the status of the RefreshSchemas operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeRefreshSchemasStatus>`_

        **Request Syntax**
        ::

          response = client.describe_refresh_schemas_status(
              EndpointArn='string'
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RefreshSchemasStatus': {
                    'EndpointArn': 'string',
                    'ReplicationInstanceArn': 'string',
                    'Status': 'successful'|'failed'|'refreshing',
                    'LastRefreshDate': datetime(2015, 1, 1),
                    'LastFailureMessage': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **RefreshSchemasStatus** *(dict) --*

              The status of the schema.

              - **EndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **ReplicationInstanceArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication instance.

              - **Status** *(string) --*

                The status of the schema.

              - **LastRefreshDate** *(datetime) --*

                The date the schema was last refreshed.

              - **LastFailureMessage** *(string) --*

                The last failure message for the schema.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_replication_instance_task_logs(
        self, ReplicationInstanceArn: str, MaxRecords: int = None, Marker: str = None
    ) -> ClientDescribeReplicationInstanceTaskLogsResponseTypeDef:
        """
        Returns information about the task logs for the specified task.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeReplicationInstanceTaskLogs>`_

        **Request Syntax**
        ::

          response = client.describe_replication_instance_task_logs(
              ReplicationInstanceArn='string',
              MaxRecords=123,
              Marker='string'
          )
        :type ReplicationInstanceArn: string
        :param ReplicationInstanceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the replication instance.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that the remaining results can be retrieved.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous request. If this parameter is specified, the
          response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationInstanceArn': 'string',
                'ReplicationInstanceTaskLogs': [
                    {
                        'ReplicationTaskName': 'string',
                        'ReplicationTaskArn': 'string',
                        'ReplicationInstanceTaskLogSize': 123
                    },
                ],
                'Marker': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationInstanceArn** *(string) --*

              The Amazon Resource Name (ARN) of the replication instance.

            - **ReplicationInstanceTaskLogs** *(list) --*

              An array of replication task log metadata. Each member of the array contains the replication
              task name, ARN, and task log size (in bytes).

              - *(dict) --*

                Contains metadata for a replication instance task log.

                - **ReplicationTaskName** *(string) --*

                  The name of the replication task.

                - **ReplicationTaskArn** *(string) --*

                  The Amazon Resource Name (ARN) of the replication task.

                - **ReplicationInstanceTaskLogSize** *(integer) --*

                  The size, in bytes, of the replication task log.

            - **Marker** *(string) --*

              An optional pagination token provided by a previous request. If this parameter is specified,
              the response includes only records beyond the marker, up to the value specified by
              ``MaxRecords`` .

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_replication_instances(
        self,
        Filters: List[ClientDescribeReplicationInstancesFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeReplicationInstancesResponseTypeDef:
        """
        Returns information about replication instances for your account in the current region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeReplicationInstances>`_

        **Request Syntax**
        ::

          response = client.describe_replication_instances(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker='string'
          )
        :type Filters: list
        :param Filters:

          Filters applied to the describe action.

          Valid filter names: replication-instance-arn | replication-instance-id |
          replication-instance-class | engine-version

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that the remaining results can be retrieved.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous request. If this parameter is specified, the
          response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'ReplicationInstances': [
                    {
                        'ReplicationInstanceIdentifier': 'string',
                        'ReplicationInstanceClass': 'string',
                        'ReplicationInstanceStatus': 'string',
                        'AllocatedStorage': 123,
                        'InstanceCreateTime': datetime(2015, 1, 1),
                        'VpcSecurityGroups': [
                            {
                                'VpcSecurityGroupId': 'string',
                                'Status': 'string'
                            },
                        ],
                        'AvailabilityZone': 'string',
                        'ReplicationSubnetGroup': {
                            'ReplicationSubnetGroupIdentifier': 'string',
                            'ReplicationSubnetGroupDescription': 'string',
                            'VpcId': 'string',
                            'SubnetGroupStatus': 'string',
                            'Subnets': [
                                {
                                    'SubnetIdentifier': 'string',
                                    'SubnetAvailabilityZone': {
                                        'Name': 'string'
                                    },
                                    'SubnetStatus': 'string'
                                },
                            ]
                        },
                        'PreferredMaintenanceWindow': 'string',
                        'PendingModifiedValues': {
                            'ReplicationInstanceClass': 'string',
                            'AllocatedStorage': 123,
                            'MultiAZ': True|False,
                            'EngineVersion': 'string'
                        },
                        'MultiAZ': True|False,
                        'EngineVersion': 'string',
                        'AutoMinorVersionUpgrade': True|False,
                        'KmsKeyId': 'string',
                        'ReplicationInstanceArn': 'string',
                        'ReplicationInstancePublicIpAddress': 'string',
                        'ReplicationInstancePrivateIpAddress': 'string',
                        'ReplicationInstancePublicIpAddresses': [
                            'string',
                        ],
                        'ReplicationInstancePrivateIpAddresses': [
                            'string',
                        ],
                        'PubliclyAccessible': True|False,
                        'SecondaryAvailabilityZone': 'string',
                        'FreeUntil': datetime(2015, 1, 1),
                        'DnsNameServers': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Marker** *(string) --*

              An optional pagination token provided by a previous request. If this parameter is specified,
              the response includes only records beyond the marker, up to the value specified by
              ``MaxRecords`` .

            - **ReplicationInstances** *(list) --*

              The replication instances described.

              - *(dict) --*

                - **ReplicationInstanceIdentifier** *(string) --*

                  The replication instance identifier. This parameter is stored as a lowercase string.

                  Constraints:

                  * Must contain from 1 to 63 alphanumeric characters or hyphens.

                  * First character must be a letter.

                  * Cannot end with a hyphen or contain two consecutive hyphens.

                  Example: ``myrepinstance``

                - **ReplicationInstanceClass** *(string) --*

                  The compute and memory capacity of the replication instance.

                  Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
                  | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

                - **ReplicationInstanceStatus** *(string) --*

                  The status of the replication instance.

                - **AllocatedStorage** *(integer) --*

                  The amount of storage (in gigabytes) that is allocated for the replication instance.

                - **InstanceCreateTime** *(datetime) --*

                  The time the replication instance was created.

                - **VpcSecurityGroups** *(list) --*

                  The VPC security group for the instance.

                  - *(dict) --*

                    - **VpcSecurityGroupId** *(string) --*

                      The VPC security group Id.

                    - **Status** *(string) --*

                      The status of the VPC security group.

                - **AvailabilityZone** *(string) --*

                  The Availability Zone for the instance.

                - **ReplicationSubnetGroup** *(dict) --*

                  The subnet group for the replication instance.

                  - **ReplicationSubnetGroupIdentifier** *(string) --*

                    The identifier of the replication instance subnet group.

                  - **ReplicationSubnetGroupDescription** *(string) --*

                    A description for the replication subnet group.

                  - **VpcId** *(string) --*

                    The ID of the VPC.

                  - **SubnetGroupStatus** *(string) --*

                    The status of the subnet group.

                  - **Subnets** *(list) --*

                    The subnets that are in the subnet group.

                    - *(dict) --*

                      - **SubnetIdentifier** *(string) --*

                        The subnet identifier.

                      - **SubnetAvailabilityZone** *(dict) --*

                        The Availability Zone of the subnet.

                        - **Name** *(string) --*

                          The name of the availability zone.

                      - **SubnetStatus** *(string) --*

                        The status of the subnet.

                - **PreferredMaintenanceWindow** *(string) --*

                  The maintenance window times for the replication instance.

                - **PendingModifiedValues** *(dict) --*

                  The pending modification values.

                  - **ReplicationInstanceClass** *(string) --*

                    The compute and memory capacity of the replication instance.

                    Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large |
                    dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

                  - **AllocatedStorage** *(integer) --*

                    The amount of storage (in gigabytes) that is allocated for the replication instance.

                  - **MultiAZ** *(boolean) --*

                    Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
                    ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

                  - **EngineVersion** *(string) --*

                    The engine version number of the replication instance.

                - **MultiAZ** *(boolean) --*

                  Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
                  ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

                - **EngineVersion** *(string) --*

                  The engine version number of the replication instance.

                - **AutoMinorVersionUpgrade** *(boolean) --*

                  Boolean value indicating if minor version upgrades will be automatically applied to the
                  instance.

                - **KmsKeyId** *(string) --*

                  An AWS KMS key identifier that is used to encrypt the data on the replication instance.

                  If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your
                  default encryption key.

                  AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
                  different default encryption key for each AWS Region.

                - **ReplicationInstanceArn** *(string) --*

                  The Amazon Resource Name (ARN) of the replication instance.

                - **ReplicationInstancePublicIpAddress** *(string) --*

                  The public IP address of the replication instance.

                - **ReplicationInstancePrivateIpAddress** *(string) --*

                  The private IP address of the replication instance.

                - **ReplicationInstancePublicIpAddresses** *(list) --*

                  One or more public IP addresses for the replication instance.

                  - *(string) --*

                - **ReplicationInstancePrivateIpAddresses** *(list) --*

                  One or more private IP addresses for the replication instance.

                  - *(string) --*

                - **PubliclyAccessible** *(boolean) --*

                  Specifies the accessibility options for the replication instance. A value of ``true``
                  represents an instance with a public IP address. A value of ``false`` represents an
                  instance with a private IP address. The default value is ``true`` .

                - **SecondaryAvailabilityZone** *(string) --*

                  The availability zone of the standby replication instance in a Multi-AZ deployment.

                - **FreeUntil** *(datetime) --*

                  The expiration date of the free replication instance that is part of the Free DMS program.

                - **DnsNameServers** *(string) --*

                  The DNS name servers for the replication instance.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_replication_subnet_groups(
        self,
        Filters: List[ClientDescribeReplicationSubnetGroupsFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> ClientDescribeReplicationSubnetGroupsResponseTypeDef:
        """
        Returns information about the replication subnet groups.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeReplicationSubnetGroups>`_

        **Request Syntax**
        ::

          response = client.describe_replication_subnet_groups(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker='string'
          )
        :type Filters: list
        :param Filters:

          Filters applied to the describe action.

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that the remaining results can be retrieved.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous request. If this parameter is specified, the
          response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'ReplicationSubnetGroups': [
                    {
                        'ReplicationSubnetGroupIdentifier': 'string',
                        'ReplicationSubnetGroupDescription': 'string',
                        'VpcId': 'string',
                        'SubnetGroupStatus': 'string',
                        'Subnets': [
                            {
                                'SubnetIdentifier': 'string',
                                'SubnetAvailabilityZone': {
                                    'Name': 'string'
                                },
                                'SubnetStatus': 'string'
                            },
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Marker** *(string) --*

              An optional pagination token provided by a previous request. If this parameter is specified,
              the response includes only records beyond the marker, up to the value specified by
              ``MaxRecords`` .

            - **ReplicationSubnetGroups** *(list) --*

              A description of the replication subnet groups.

              - *(dict) --*

                - **ReplicationSubnetGroupIdentifier** *(string) --*

                  The identifier of the replication instance subnet group.

                - **ReplicationSubnetGroupDescription** *(string) --*

                  A description for the replication subnet group.

                - **VpcId** *(string) --*

                  The ID of the VPC.

                - **SubnetGroupStatus** *(string) --*

                  The status of the subnet group.

                - **Subnets** *(list) --*

                  The subnets that are in the subnet group.

                  - *(dict) --*

                    - **SubnetIdentifier** *(string) --*

                      The subnet identifier.

                    - **SubnetAvailabilityZone** *(dict) --*

                      The Availability Zone of the subnet.

                      - **Name** *(string) --*

                        The name of the availability zone.

                    - **SubnetStatus** *(string) --*

                      The status of the subnet.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_replication_task_assessment_results(
        self, ReplicationTaskArn: str = None, MaxRecords: int = None, Marker: str = None
    ) -> ClientDescribeReplicationTaskAssessmentResultsResponseTypeDef:
        """
        Returns the task assessment results from Amazon S3. This action always returns the latest results.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeReplicationTaskAssessmentResults>`_

        **Request Syntax**
        ::

          response = client.describe_replication_task_assessment_results(
              ReplicationTaskArn='string',
              MaxRecords=123,
              Marker='string'
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn:

          - The Amazon Resource Name (ARN) string that uniquely identifies the task. When this input
          parameter is specified the API will return only one result and ignore the values of the
          max-records and marker parameters.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that the remaining results can be retrieved.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous request. If this parameter is specified, the
          response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'BucketName': 'string',
                'ReplicationTaskAssessmentResults': [
                    {
                        'ReplicationTaskIdentifier': 'string',
                        'ReplicationTaskArn': 'string',
                        'ReplicationTaskLastAssessmentDate': datetime(2015, 1, 1),
                        'AssessmentStatus': 'string',
                        'AssessmentResultsFile': 'string',
                        'AssessmentResults': 'string',
                        'S3ObjectUrl': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Marker** *(string) --*

              An optional pagination token provided by a previous request. If this parameter is specified,
              the response includes only records beyond the marker, up to the value specified by
              ``MaxRecords`` .

            - **BucketName** *(string) --*

              - The Amazon S3 bucket where the task assessment report is located.

            - **ReplicationTaskAssessmentResults** *(list) --*

              The task assessment report.

              - *(dict) --*

                The task assessment report in JSON format.

                - **ReplicationTaskIdentifier** *(string) --*

                  The replication task identifier of the task on which the task assessment was run.

                - **ReplicationTaskArn** *(string) --*

                  The Amazon Resource Name (ARN) of the replication task.

                - **ReplicationTaskLastAssessmentDate** *(datetime) --*

                  The date the task assessment was completed.

                - **AssessmentStatus** *(string) --*

                  The status of the task assessment.

                - **AssessmentResultsFile** *(string) --*

                  The file containing the results of the task assessment.

                - **AssessmentResults** *(string) --*

                  The task assessment results in JSON format.

                - **S3ObjectUrl** *(string) --*

                  The URL of the S3 object containing the task assessment results.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_replication_tasks(
        self,
        Filters: List[ClientDescribeReplicationTasksFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
    ) -> Dict[str, Any]:
        """
        Returns information about replication tasks for your account in the current region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeReplicationTasks>`_

        **Request Syntax**
        ::

          response = client.describe_replication_tasks(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker='string',
              WithoutSettings=True|False
          )
        :type Filters: list
        :param Filters:

          Filters applied to the describe action.

          Valid filter names: replication-task-arn | replication-task-id | migration-type | endpoint-arn |
          replication-instance-arn

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that the remaining results can be retrieved.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous request. If this parameter is specified, the
          response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

        :type WithoutSettings: boolean
        :param WithoutSettings:

          An option to set to avoid returning information about settings. Use this to reduce overhead when
          setting information is too large. To use this option, choose ``true`` ; otherwise, choose
          ``false`` (the default).

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'ReplicationTasks': [
                    {
                        'ReplicationTaskIdentifier': 'string',
                        'SourceEndpointArn': 'string',
                        'TargetEndpointArn': 'string',
                        'ReplicationInstanceArn': 'string',
                        'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
                        'TableMappings': 'string',
                        'ReplicationTaskSettings': 'string',
                        'Status': 'string',
                        'LastFailureMessage': 'string',
                        'StopReason': 'string',
                        'ReplicationTaskCreationDate': datetime(2015, 1, 1),
                        'ReplicationTaskStartDate': datetime(2015, 1, 1),
                        'CdcStartPosition': 'string',
                        'CdcStopPosition': 'string',
                        'RecoveryCheckpoint': 'string',
                        'ReplicationTaskArn': 'string',
                        'ReplicationTaskStats': {
                            'FullLoadProgressPercent': 123,
                            'ElapsedTimeMillis': 123,
                            'TablesLoaded': 123,
                            'TablesLoading': 123,
                            'TablesQueued': 123,
                            'TablesErrored': 123,
                            'FreshStartDate': datetime(2015, 1, 1),
                            'StartDate': datetime(2015, 1, 1),
                            'StopDate': datetime(2015, 1, 1),
                            'FullLoadStartDate': datetime(2015, 1, 1),
                            'FullLoadFinishDate': datetime(2015, 1, 1)
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Marker** *(string) --*

              An optional pagination token provided by a previous request. If this parameter is specified,
              the response includes only records beyond the marker, up to the value specified by
              ``MaxRecords`` .

            - **ReplicationTasks** *(list) --*

              A description of the replication tasks.

              - *(dict) --*

                - **ReplicationTaskIdentifier** *(string) --*

                  The user-assigned replication task identifier or name.

                  Constraints:

                  * Must contain from 1 to 255 alphanumeric characters or hyphens.

                  * First character must be a letter.

                  * Cannot end with a hyphen or contain two consecutive hyphens.

                - **SourceEndpointArn** *(string) --*

                  The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

                - **TargetEndpointArn** *(string) --*

                  The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

                - **ReplicationInstanceArn** *(string) --*

                  The Amazon Resource Name (ARN) of the replication instance.

                - **MigrationType** *(string) --*

                  The type of migration.

                - **TableMappings** *(string) --*

                  Table mappings specified in the task.

                - **ReplicationTaskSettings** *(string) --*

                  The settings for the replication task.

                - **Status** *(string) --*

                  The status of the replication task.

                - **LastFailureMessage** *(string) --*

                  The last error (failure) message generated for the replication instance.

                - **StopReason** *(string) --*

                  The reason the replication task was stopped.

                - **ReplicationTaskCreationDate** *(datetime) --*

                  The date the replication task was created.

                - **ReplicationTaskStartDate** *(datetime) --*

                  The date the replication task is scheduled to start.

                - **CdcStartPosition** *(string) --*

                  Indicates when you want a change data capture (CDC) operation to start. Use either
                  ``CdcStartPosition`` or ``CdcStartTime`` to specify when you want the CDC operation to
                  start. Specifying both values results in an error.

                  The value can be in date, checkpoint, or LSN/SCN format.

                  Date Example: --cdc-start-position “2018-03-08T12:12:12”

                  Checkpoint Example: --cdc-start-position
                  "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"
        "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"

                  LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”

                - **CdcStopPosition** *(string) --*

                  Indicates when you want a change data capture (CDC) operation to stop. The value can be
                  either server time or commit time.

                  Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”

                  Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12 “

                - **RecoveryCheckpoint** *(string) --*

                  Indicates the last checkpoint that occurred during a change data capture (CDC) operation.
                  You can provide this value to the ``CdcStartPosition`` parameter to start a CDC operation
                  that begins at that checkpoint.

                - **ReplicationTaskArn** *(string) --*

                  The Amazon Resource Name (ARN) of the replication task.

                - **ReplicationTaskStats** *(dict) --*

                  The statistics for the task, including elapsed time, tables loaded, and table errors.

                  - **FullLoadProgressPercent** *(integer) --*

                    The percent complete for the full load migration task.

                  - **ElapsedTimeMillis** *(integer) --*

                    The elapsed time of the task, in milliseconds.

                  - **TablesLoaded** *(integer) --*

                    The number of tables loaded for this task.

                  - **TablesLoading** *(integer) --*

                    The number of tables currently loading for this task.

                  - **TablesQueued** *(integer) --*

                    The number of tables queued for this task.

                  - **TablesErrored** *(integer) --*

                    The number of errors that have occurred during this task.

                  - **FreshStartDate** *(datetime) --*

                    The date the replication task was started either with a fresh start or a target reload.

                  - **StartDate** *(datetime) --*

                    The date the replication task was started either with a fresh start or a resume. For
                    more information, see `StartReplicationTaskType
                    <https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html#DMS-StartReplicationTask-request-StartReplicationTaskType>`__
                    .

                  - **StopDate** *(datetime) --*

                    The date the replication task was stopped.

                  - **FullLoadStartDate** *(datetime) --*

                    The date the the replication task full load was started.

                  - **FullLoadFinishDate** *(datetime) --*

                    The date the replication task full load was completed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_schemas(
        self, EndpointArn: str, MaxRecords: int = None, Marker: str = None
    ) -> ClientDescribeSchemasResponseTypeDef:
        """
        Returns information about the schema for the specified endpoint.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeSchemas>`_

        **Request Syntax**
        ::

          response = client.describe_schemas(
              EndpointArn='string',
              MaxRecords=123,
              Marker='string'
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that the remaining results can be retrieved.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous request. If this parameter is specified, the
          response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Marker': 'string',
                'Schemas': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Marker** *(string) --*

              An optional pagination token provided by a previous request. If this parameter is specified,
              the response includes only records beyond the marker, up to the value specified by
              ``MaxRecords`` .

            - **Schemas** *(list) --*

              The described schema.

              - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_table_statistics(
        self,
        ReplicationTaskArn: str,
        MaxRecords: int = None,
        Marker: str = None,
        Filters: List[ClientDescribeTableStatisticsFiltersTypeDef] = None,
    ) -> ClientDescribeTableStatisticsResponseTypeDef:
        """
        Returns table statistics on the database migration task, including table name, rows inserted, rows
        updated, and rows deleted.

        Note that the "last updated" column the DMS console only indicates the time that AWS DMS last
        updated the table statistics record for a table. It does not indicate the time of the last update
        to the table.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeTableStatistics>`_

        **Request Syntax**
        ::

          response = client.describe_table_statistics(
              ReplicationTaskArn='string',
              MaxRecords=123,
              Marker='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ]
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the replication task.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the response so
          that the remaining results can be retrieved.

          Default: 100

          Constraints: Minimum 20, maximum 500.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous request. If this parameter is specified, the
          response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

        :type Filters: list
        :param Filters:

          Filters applied to the describe table statistics action.

          Valid filter names: schema-name | table-name | table-state

          A combination of filters creates an AND condition where each record matches all specified filters.

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationTaskArn': 'string',
                'TableStatistics': [
                    {
                        'SchemaName': 'string',
                        'TableName': 'string',
                        'Inserts': 123,
                        'Deletes': 123,
                        'Updates': 123,
                        'Ddls': 123,
                        'FullLoadRows': 123,
                        'FullLoadCondtnlChkFailedRows': 123,
                        'FullLoadErrorRows': 123,
                        'LastUpdateTime': datetime(2015, 1, 1),
                        'TableState': 'string',
                        'ValidationPendingRecords': 123,
                        'ValidationFailedRecords': 123,
                        'ValidationSuspendedRecords': 123,
                        'ValidationState': 'string',
                        'ValidationStateDetails': 'string'
                    },
                ],
                'Marker': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationTaskArn** *(string) --*

              The Amazon Resource Name (ARN) of the replication task.

            - **TableStatistics** *(list) --*

              The table statistics.

              - *(dict) --*

                - **SchemaName** *(string) --*

                  The schema name.

                - **TableName** *(string) --*

                  The name of the table.

                - **Inserts** *(integer) --*

                  The number of insert actions performed on a table.

                - **Deletes** *(integer) --*

                  The number of delete actions performed on a table.

                - **Updates** *(integer) --*

                  The number of update actions performed on a table.

                - **Ddls** *(integer) --*

                  The Data Definition Language (DDL) used to build and modify the structure of your tables.

                - **FullLoadRows** *(integer) --*

                  The number of rows added during the Full Load operation.

                - **FullLoadCondtnlChkFailedRows** *(integer) --*

                  The number of rows that failed conditional checks during the Full Load operation (valid
                  only for DynamoDB as a target migrations).

                - **FullLoadErrorRows** *(integer) --*

                  The number of rows that failed to load during the Full Load operation (valid only for
                  DynamoDB as a target migrations).

                - **LastUpdateTime** *(datetime) --*

                  The last time the table was updated.

                - **TableState** *(string) --*

                  The state of the tables described.

                  Valid states: Table does not exist | Before load | Full load | Table completed | Table
                  cancelled | Table error | Table all | Table updates | Table is being reloaded

                - **ValidationPendingRecords** *(integer) --*

                  The number of records that have yet to be validated.

                - **ValidationFailedRecords** *(integer) --*

                  The number of records that failed validation.

                - **ValidationSuspendedRecords** *(integer) --*

                  The number of records that could not be validated.

                - **ValidationState** *(string) --*

                  The validation state of the table.

                  The parameter can have the following values

                  * Not enabled—Validation is not enabled for the table in the migration task.

                  * Pending records—Some records in the table are waiting for validation.

                  * Mismatched records—Some records in the table do not match between the source and target.

                  * Suspended records—Some records in the table could not be validated.

                  * No primary key—The table could not be validated because it had no primary key.

                  * Table error—The table was not validated because it was in an error state and some data
                  was not migrated.

                  * Validated—All rows in the table were validated. If the table is updated, the status can
                  change from Validated.

                  * Error—The table could not be validated because of an unexpected error.

                - **ValidationStateDetails** *(string) --*

                  Additional details about the state of validation.

            - **Marker** *(string) --*

              An optional pagination token provided by a previous request. If this parameter is specified,
              the response includes only records beyond the marker, up to the value specified by
              ``MaxRecords`` .

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
    def import_certificate(
        self,
        CertificateIdentifier: str,
        CertificatePem: str = None,
        CertificateWallet: bytes = None,
        Tags: List[ClientImportCertificateTagsTypeDef] = None,
    ) -> ClientImportCertificateResponseTypeDef:
        """
        Uploads the specified certificate.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ImportCertificate>`_

        **Request Syntax**
        ::

          response = client.import_certificate(
              CertificateIdentifier='string',
              CertificatePem='string',
              CertificateWallet=b'bytes',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type CertificateIdentifier: string
        :param CertificateIdentifier: **[REQUIRED]**

          A customer-assigned name for the certificate. Identifiers must begin with a letter; must contain
          only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
          consecutive hyphens.

        :type CertificatePem: string
        :param CertificatePem:

          The contents of a ``.pem`` file, which contains an X.509 certificate.

        :type CertificateWallet: bytes
        :param CertificateWallet:

          The location of an imported Oracle Wallet certificate for use with SSL.

        :type Tags: list
        :param Tags:

          The tags associated with the certificate.

          - *(dict) --*

            - **Key** *(string) --*

              A key is the required name of the tag. The string value can be from 1 to 128 Unicode
              characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
              contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
              (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

            - **Value** *(string) --*

              A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
              characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
              contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+', '-'
              (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Certificate': {
                    'CertificateIdentifier': 'string',
                    'CertificateCreationDate': datetime(2015, 1, 1),
                    'CertificatePem': 'string',
                    'CertificateWallet': b'bytes',
                    'CertificateArn': 'string',
                    'CertificateOwner': 'string',
                    'ValidFromDate': datetime(2015, 1, 1),
                    'ValidToDate': datetime(2015, 1, 1),
                    'SigningAlgorithm': 'string',
                    'KeyLength': 123
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Certificate** *(dict) --*

              The certificate to be uploaded.

              - **CertificateIdentifier** *(string) --*

                A customer-assigned name for the certificate. Identifiers must begin with a letter; must
                contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain
                two consecutive hyphens.

              - **CertificateCreationDate** *(datetime) --*

                The date that the certificate was created.

              - **CertificatePem** *(string) --*

                The contents of a ``.pem`` file, which contains an X.509 certificate.

              - **CertificateWallet** *(bytes) --*

                The location of an imported Oracle Wallet certificate for use with SSL.

              - **CertificateArn** *(string) --*

                The Amazon Resource Name (ARN) for the certificate.

              - **CertificateOwner** *(string) --*

                The owner of the certificate.

              - **ValidFromDate** *(datetime) --*

                The beginning date that the certificate is valid.

              - **ValidToDate** *(datetime) --*

                The final date that the certificate is valid.

              - **SigningAlgorithm** *(string) --*

                The signing algorithm for the certificate.

              - **KeyLength** *(integer) --*

                The key length of the cryptographic algorithm being used.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceArn: str
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Lists all tags for an AWS DMS resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              ResourceArn='string'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) string that uniquely identifies the AWS DMS resource.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TagList': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **TagList** *(list) --*

              A list of tags for the resource.

              - *(dict) --*

                - **Key** *(string) --*

                  A key is the required name of the tag. The string value can be from 1 to 128 Unicode
                  characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
                  contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+',
                  '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

                - **Value** *(string) --*

                  A value is the optional value of the tag. The string value can be from 1 to 256 Unicode
                  characters in length and cannot be prefixed with "aws:" or "dms:". The string can only
                  contain only the set of Unicode letters, digits, white-space, '_', '.', '/', '=', '+',
                  '-' (Java regex: "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$").

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_endpoint(
        self,
        EndpointArn: str,
        EndpointIdentifier: str = None,
        EndpointType: str = None,
        EngineName: str = None,
        Username: str = None,
        Password: str = None,
        ServerName: str = None,
        Port: int = None,
        DatabaseName: str = None,
        ExtraConnectionAttributes: str = None,
        CertificateArn: str = None,
        SslMode: str = None,
        ServiceAccessRoleArn: str = None,
        ExternalTableDefinition: str = None,
        DynamoDbSettings: ClientModifyEndpointDynamoDbSettingsTypeDef = None,
        S3Settings: ClientModifyEndpointS3SettingsTypeDef = None,
        DmsTransferSettings: ClientModifyEndpointDmsTransferSettingsTypeDef = None,
        MongoDbSettings: ClientModifyEndpointMongoDbSettingsTypeDef = None,
        KinesisSettings: ClientModifyEndpointKinesisSettingsTypeDef = None,
        ElasticsearchSettings: ClientModifyEndpointElasticsearchSettingsTypeDef = None,
        RedshiftSettings: ClientModifyEndpointRedshiftSettingsTypeDef = None,
    ) -> ClientModifyEndpointResponseTypeDef:
        """
        Modifies the specified endpoint.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ModifyEndpoint>`_

        **Request Syntax**
        ::

          response = client.modify_endpoint(
              EndpointArn='string',
              EndpointIdentifier='string',
              EndpointType='source'|'target',
              EngineName='string',
              Username='string',
              Password='string',
              ServerName='string',
              Port=123,
              DatabaseName='string',
              ExtraConnectionAttributes='string',
              CertificateArn='string',
              SslMode='none'|'require'|'verify-ca'|'verify-full',
              ServiceAccessRoleArn='string',
              ExternalTableDefinition='string',
              DynamoDbSettings={
                  'ServiceAccessRoleArn': 'string'
              },
              S3Settings={
                  'ServiceAccessRoleArn': 'string',
                  'ExternalTableDefinition': 'string',
                  'CsvRowDelimiter': 'string',
                  'CsvDelimiter': 'string',
                  'BucketFolder': 'string',
                  'BucketName': 'string',
                  'CompressionType': 'none'|'gzip',
                  'EncryptionMode': 'sse-s3'|'sse-kms',
                  'ServerSideEncryptionKmsKeyId': 'string',
                  'DataFormat': 'csv'|'parquet',
                  'EncodingType': 'plain'|'plain-dictionary'|'rle-dictionary',
                  'DictPageSizeLimit': 123,
                  'RowGroupLength': 123,
                  'DataPageSize': 123,
                  'ParquetVersion': 'parquet-1-0'|'parquet-2-0',
                  'EnableStatistics': True|False,
                  'IncludeOpForFullLoad': True|False,
                  'CdcInsertsOnly': True|False,
                  'TimestampColumnName': 'string',
                  'ParquetTimestampInMillisecond': True|False
              },
              DmsTransferSettings={
                  'ServiceAccessRoleArn': 'string',
                  'BucketName': 'string'
              },
              MongoDbSettings={
                  'Username': 'string',
                  'Password': 'string',
                  'ServerName': 'string',
                  'Port': 123,
                  'DatabaseName': 'string',
                  'AuthType': 'no'|'password',
                  'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
                  'NestingLevel': 'none'|'one',
                  'ExtractDocId': 'string',
                  'DocsToInvestigate': 'string',
                  'AuthSource': 'string',
                  'KmsKeyId': 'string'
              },
              KinesisSettings={
                  'StreamArn': 'string',
                  'MessageFormat': 'json',
                  'ServiceAccessRoleArn': 'string'
              },
              ElasticsearchSettings={
                  'ServiceAccessRoleArn': 'string',
                  'EndpointUri': 'string',
                  'FullLoadErrorPercentage': 123,
                  'ErrorRetryDuration': 123
              },
              RedshiftSettings={
                  'AcceptAnyDate': True|False,
                  'AfterConnectScript': 'string',
                  'BucketFolder': 'string',
                  'BucketName': 'string',
                  'ConnectionTimeout': 123,
                  'DatabaseName': 'string',
                  'DateFormat': 'string',
                  'EmptyAsNull': True|False,
                  'EncryptionMode': 'sse-s3'|'sse-kms',
                  'FileTransferUploadStreams': 123,
                  'LoadTimeout': 123,
                  'MaxFileSize': 123,
                  'Password': 'string',
                  'Port': 123,
                  'RemoveQuotes': True|False,
                  'ReplaceInvalidChars': 'string',
                  'ReplaceChars': 'string',
                  'ServerName': 'string',
                  'ServiceAccessRoleArn': 'string',
                  'ServerSideEncryptionKmsKeyId': 'string',
                  'TimeFormat': 'string',
                  'TrimBlanks': True|False,
                  'TruncateColumns': True|False,
                  'Username': 'string',
                  'WriteBufferSize': 123
              }
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

        :type EndpointIdentifier: string
        :param EndpointIdentifier:

          The database endpoint identifier. Identifiers must begin with a letter; must contain only ASCII
          letters, digits, and hyphens; and must not end with a hyphen or contain two consecutive hyphens.

        :type EndpointType: string
        :param EndpointType:

          The type of endpoint. Valid values are ``source`` and ``target`` .

        :type EngineName: string
        :param EngineName:

          The type of engine for the endpoint. Valid values, depending on the EndpointType, include mysql,
          oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
          dynamodb, mongodb, and sqlserver.

        :type Username: string
        :param Username:

          The user name to be used to login to the endpoint database.

        :type Password: string
        :param Password:

          The password to be used to login to the endpoint database.

        :type ServerName: string
        :param ServerName:

          The name of the server where the endpoint database resides.

        :type Port: integer
        :param Port:

          The port used by the endpoint database.

        :type DatabaseName: string
        :param DatabaseName:

          The name of the endpoint database.

        :type ExtraConnectionAttributes: string
        :param ExtraConnectionAttributes:

          Additional attributes associated with the connection. To reset this parameter, pass the empty
          string ("") as an argument.

        :type CertificateArn: string
        :param CertificateArn:

          The Amazon Resource Name (ARN) of the certificate used for SSL connection.

        :type SslMode: string
        :param SslMode:

          The SSL mode used to connect to the endpoint. The default value is ``none`` .

        :type ServiceAccessRoleArn: string
        :param ServiceAccessRoleArn:

          The Amazon Resource Name (ARN) for the service access role you want to use to modify the endpoint.

        :type ExternalTableDefinition: string
        :param ExternalTableDefinition:

          The external table definition.

        :type DynamoDbSettings: dict
        :param DynamoDbSettings:

          Settings in JSON format for the target Amazon DynamoDB endpoint. For more information about the
          available settings, see `Using Object Mapping to Migrate Data to DynamoDB
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html>`__ in the *AWS
          Database Migration Service User Guide.*

          - **ServiceAccessRoleArn** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) used by the service access IAM role.

        :type S3Settings: dict
        :param S3Settings:

          Settings in JSON format for the target Amazon S3 endpoint. For more information about the
          available settings, see `Extra Connection Attributes When Using Amazon S3 as a Target for AWS DMS
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring>`__
          in the *AWS Database Migration Service User Guide.*

          - **ServiceAccessRoleArn** *(string) --*

            The Amazon Resource Name (ARN) used by the service access IAM role.

          - **ExternalTableDefinition** *(string) --*

            The external table definition.

          - **CsvRowDelimiter** *(string) --*

            The delimiter used to separate rows in the source files. The default is a carriage return
            (``\\n`` ).

          - **CsvDelimiter** *(string) --*

            The delimiter used to separate columns in the source files. The default is a comma.

          - **BucketFolder** *(string) --*

            An optional parameter to set a folder name in the S3 bucket. If provided, tables are created in
            the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this parameter is not
            specified, then the path used is `` *schema_name* /*table_name* /`` .

          - **BucketName** *(string) --*

            The name of the S3 bucket.

          - **CompressionType** *(string) --*

            An optional parameter to use GZIP to compress the target files. Set to GZIP to compress the
            target files. Set to NONE (the default) or do not use to leave the files uncompressed. Applies
            to both .csv and .parquet file formats.

          - **EncryptionMode** *(string) --*

            The type of server-side encryption that you want to use for your data. This encryption type is
            part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose
            either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , you need an AWS Identity
            and Access Management (IAM) role with permission to allow ``"arn:aws:s3:::dms-*"`` to use the
            following actions:

            * ``s3:CreateBucket``

            * ``s3:ListBucket``

            * ``s3:DeleteBucket``

            * ``s3:GetBucketLocation``

            * ``s3:GetObject``

            * ``s3:PutObject``

            * ``s3:DeleteObject``

            * ``s3:GetObjectVersion``

            * ``s3:GetBucketPolicy``

            * ``s3:PutBucketPolicy``

            * ``s3:DeleteBucketPolicy``

          - **ServerSideEncryptionKmsKeyId** *(string) --*

            If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID. The key
            that you use needs an attached policy that enables AWS Identity and Access Management (IAM)
            user permissions and allows use of the key.

            Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value* --endpoint-type
            target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value* ,BucketFolder=*value*
            ,BucketName=*value* ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

          - **DataFormat** *(string) --*

            The format of the data that you want to use for output. You can choose one of the following:

            * ``csv`` : This is a row-based file format with comma-separated values (.csv).

            * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features
            efficient compression and provides faster query response.

          - **EncodingType** *(string) --*

            The type of encoding you are using:

            * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
            repeated values more efficiently. This is the default.

            * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

            * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column. The
            dictionary is stored in a dictionary page for each column chunk.

          - **DictPageSizeLimit** *(integer) --*

            The maximum size of an encoded dictionary page of a column. If the dictionary page exceeds
            this, this column is stored using an encoding type of ``PLAIN`` . This parameter defaults to
            1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it reverts to ``PLAIN``
            encoding. This size is used for .parquet file format only.

          - **RowGroupLength** *(integer) --*

            The number of rows in a row group. A smaller row group size provides faster reads. But as the
            number of row groups grows, the slower writes become. This parameter defaults to 10,000 rows.
            This number is used for .parquet file format only.

            If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row group
            length in bytes (64 * 1024 * 1024).

          - **DataPageSize** *(integer) --*

            The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB). This
            number is used for .parquet file format only.

          - **ParquetVersion** *(string) --*

            The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the default) or
            ``parquet_2_0`` .

          - **EnableStatistics** *(boolean) --*

            A value that enables statistics for Parquet pages and row groups. Choose ``true`` to enable
            statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` , ``MAX`` , and
            ``MIN`` values. This parameter defaults to ``true`` . This value is used for .parquet file
            format only.

          - **IncludeOpForFullLoad** *(boolean) --*

            A value that enables a full load to write INSERT operations to the comma-separated value (.csv)
            output files only to indicate how the rows were added to the source database.

            .. note::

              AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

            For full load, records can only be inserted. By default (the ``false`` setting), no information
            is recorded in these output files for a full load to indicate that the rows were inserted at
            the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or ``y`` , the INSERT is
            recorded as an I annotation in the first field of the .csv file. This allows the format of your
            target records from a full load to be consistent with the target records from a CDC load.

            .. note::

              This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv files
              only. For more information about how these settings work together, see `Indicating Source DB
              Operations in Migrated S3 Data
              <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
              in the *AWS Database Migration Service User Guide.* .

          - **CdcInsertsOnly** *(boolean) --*

            A value that enables a change data capture (CDC) load to write only INSERT operations to .csv
            or columnar storage (.parquet) output files. By default (the ``false`` setting), the first
            field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D (DELETE).
            These values indicate whether the row was inserted, updated, or deleted at the source database
            for a CDC load to the target.

            If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database are
            migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are recorded
            depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad`` is set to
            ``true`` , the first field of every CDC record is set to I to indicate the INSERT operation at
            the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every CDC record is written
            without a first field to indicate the INSERT operation at the source. For more information
            about how these settings work together, see `Indicating Source DB Operations in Migrated S3
            Data
            <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
            in the *AWS Database Migration Service User Guide.* .

            .. note::

              AWS DMS supports this interaction between the ``CdcInsertsOnly`` and ``IncludeOpForFullLoad``
              parameters in versions 3.1.4 and later.

          - **TimestampColumnName** *(string) --*

            A value that when nonblank causes AWS DMS to add a column with timestamp information to the
            endpoint data for an Amazon S3 target.

            .. note::

              AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

            DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your
            migrated data when you set ``TimestampColumnName`` to a nonblank value.

            For a full load, each row of this timestamp column contains a timestamp for when the data was
            transferred from the source to the target by DMS.

            For a change data capture (CDC) load, each row of the timestamp column contains the timestamp
            for the commit of that row in the source database.

            The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By
            default, the precision of this value is in microseconds. For a CDC load, the rounding of the
            precision depends on the commit timestamp supported by DMS for the source database.

            When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for the
            timestamp column that you set with ``TimestampColumnName`` .

          - **ParquetTimestampInMillisecond** *(boolean) --*

            A value that specifies the precision of any ``TIMESTAMP`` column values that are written to an
            Amazon S3 object file in .parquet format.

            .. note::

              AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and later.

            When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
            ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise, DMS
            writes them with microsecond precision.

            Currently, Amazon Athena and AWS Glue can handle only millisecond precision for ``TIMESTAMP``
            values. Set this parameter to ``true`` for S3 endpoint object files that are .parquet formatted
            only if you plan to query or process the data with Athena or AWS Glue.

            .. note::

              AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format with
              microsecond precision.

              Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the timestamp
              column value that is inserted by setting the ``TimestampColumnName`` parameter.

        :type DmsTransferSettings: dict
        :param DmsTransferSettings:

          The settings in JSON format for the DMS transfer type of source endpoint.

          Attributes include the following:

          * serviceAccessRoleArn - The IAM role that has permission to access the Amazon S3 bucket.

          * BucketName - The name of the S3 bucket to use.

          * compressionType - An optional parameter to use GZIP to compress the target files. Set to NONE
          (the default) or do not use to leave the files uncompressed.

          Shorthand syntax: ServiceAccessRoleArn=string ,BucketName=string,CompressionType=string

          JSON syntax:

          { "ServiceAccessRoleArn": "string", "BucketName": "string", "CompressionType": "none"|"gzip" }

          - **ServiceAccessRoleArn** *(string) --*

            The IAM role that has permission to access the Amazon S3 bucket.

          - **BucketName** *(string) --*

            The name of the S3 bucket to use.

        :type MongoDbSettings: dict
        :param MongoDbSettings:

          Settings in JSON format for the source MongoDB endpoint. For more information about the available
          settings, see the configuration properties section in `Using MongoDB as a Target for AWS Database
          Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html>`__
          in the *AWS Database Migration Service User Guide.*

          - **Username** *(string) --*

            The user name you use to access the MongoDB source endpoint.

          - **Password** *(string) --*

            The password for the user account you use to access the MongoDB source endpoint.

          - **ServerName** *(string) --*

            The name of the server on the MongoDB source endpoint.

          - **Port** *(integer) --*

            The port value for the MongoDB source endpoint.

          - **DatabaseName** *(string) --*

            The database name on the MongoDB source endpoint.

          - **AuthType** *(string) --*

            The authentication type you use to access the MongoDB source endpoint.

            Valid values: NO, PASSWORD

            When NO is selected, user name and password parameters are not used and can be empty.

          - **AuthMechanism** *(string) --*

            The authentication mechanism you use to access the MongoDB source endpoint.

            Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

            DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use SCRAM_SHA_1.
            This setting is not used when authType=No.

          - **NestingLevel** *(string) --*

            Specifies either document or table mode.

            Valid values: NONE, ONE

            Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

          - **ExtractDocId** *(string) --*

            Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

            Default value is false.

          - **DocsToInvestigate** *(string) --*

            Indicates the number of documents to preview to determine the document organization. Use this
            setting when ``NestingLevel`` is set to ONE.

            Must be a positive value greater than 0. Default value is 1000.

          - **AuthSource** *(string) --*

            The MongoDB database name. This setting is not used when ``authType=NO`` .

            The default is admin.

          - **KmsKeyId** *(string) --*

            The AWS KMS key identifier that is used to encrypt the content on the replication instance. If
            you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
            encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS
            account has a different default encryption key for each AWS Region.

        :type KinesisSettings: dict
        :param KinesisSettings:

          Settings in JSON format for the target Amazon Kinesis Data Streams endpoint. For more information
          about the available settings, see `Using Object Mapping to Migrate Data to a Kinesis Data Stream
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping>`__
          in the *AWS Database Migration User Guide.*

          - **StreamArn** *(string) --*

            The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

          - **MessageFormat** *(string) --*

            The output format for the records created on the endpoint. The message format is ``JSON`` .

          - **ServiceAccessRoleArn** *(string) --*

            The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon Kinesis
            data stream.

        :type ElasticsearchSettings: dict
        :param ElasticsearchSettings:

          Settings in JSON format for the target Elasticsearch endpoint. For more information about the
          available settings, see `Extra Connection Attributes When Using Elasticsearch as a Target for AWS
          DMS
          <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration>`__
          in the *AWS Database Migration User Guide.*

          - **ServiceAccessRoleArn** *(string) --* **[REQUIRED]**

            The Amazon Resource Name (ARN) used by service to access the IAM role.

          - **EndpointUri** *(string) --* **[REQUIRED]**

            The endpoint for the Elasticsearch cluster.

          - **FullLoadErrorPercentage** *(integer) --*

            The maximum percentage of records that can fail to be written before a full load operation
            stops.

          - **ErrorRetryDuration** *(integer) --*

            The maximum number of seconds that DMS retries failed API requests to the Elasticsearch cluster.

        :type RedshiftSettings: dict
        :param RedshiftSettings:

          - **AcceptAnyDate** *(boolean) --*

            A value that indicates to allow any date format, including invalid formats such as 00/00/00
            00:00:00, to be loaded without generating an error. You can choose ``true`` or ``false`` (the
            default).

            This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the
            DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT
            specification, Amazon Redshift inserts a NULL value into that field.

          - **AfterConnectScript** *(string) --*

            Code to run after connecting. This parameter should contain the code itself, not the name of a
            file containing the code.

          - **BucketFolder** *(string) --*

            The location where the comma-separated value (.csv) files are stored before being uploaded to
            the S3 bucket.

          - **BucketName** *(string) --*

            The name of the S3 bucket you want to use

          - **ConnectionTimeout** *(integer) --*

            A value that sets the amount of time to wait (in milliseconds) before timing out, beginning
            from when you initially establish a connection.

          - **DatabaseName** *(string) --*

            The name of the Amazon Redshift data warehouse (service) that you are working with.

          - **DateFormat** *(string) --*

            The date format that you are using. Valid values are ``auto`` (case-sensitive), your date
            format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it defaults
            to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some that aren't
            supported when you use a date format string.

            If your date and time values use formats different from each other, set this to ``auto`` .

          - **EmptyAsNull** *(boolean) --*

            A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as NULL. A
            value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is ``false`` .

          - **EncryptionMode** *(string) --*

            The type of server-side encryption that you want to use for your data. This encryption type is
            part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose
            either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , create an AWS Identity and
            Access Management (IAM) role with a policy that allows ``"arn:aws:s3:::*"`` to use the
            following actions: ``"s3:PutObject", "s3:ListBucket"``

          - **FileTransferUploadStreams** *(integer) --*

            The number of threads used to upload a single file. This parameter accepts a value from 1
            through 64. It defaults to 10.

          - **LoadTimeout** *(integer) --*

            The amount of time to wait (in milliseconds) before timing out, beginning from when you begin
            loading.

          - **MaxFileSize** *(integer) --*

            The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This
            accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

          - **Password** *(string) --*

            The password for the user named in the ``username`` property.

          - **Port** *(integer) --*

            The port number for Amazon Redshift. The default value is 5439.

          - **RemoveQuotes** *(boolean) --*

            A value that specifies to remove surrounding quotation marks from strings in the incoming data.
            All characters within the quotation marks, including delimiters, are retained. Choose ``true``
            to remove quotation marks. The default is ``false`` .

          - **ReplaceInvalidChars** *(string) --*

            A list of characters that you want to replace. Use with ``ReplaceChars`` .

          - **ReplaceChars** *(string) --*

            A value that specifies to replaces the invalid characters specified in ``ReplaceInvalidChars``
            , substituting the specified characters instead. The default is ``"?"`` .

          - **ServerName** *(string) --*

            The name of the Amazon Redshift cluster you are using.

          - **ServiceAccessRoleArn** *(string) --*

            The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift service.

          - **ServerSideEncryptionKmsKeyId** *(string) --*

            The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide this key
            ID. The key that you use needs an attached policy that enables IAM user permissions and allows
            use of the key.

          - **TimeFormat** *(string) --*

            The time format that you want to use. Valid values are ``auto`` (case-sensitive),
            ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10. Using
            ``auto`` recognizes most strings, even some that aren't supported when you use a time format
            string.

            If your date and time values use formats different from each other, set this parameter to
            ``auto`` .

          - **TrimBlanks** *(boolean) --*

            A value that specifies to remove the trailing white space characters from a VARCHAR string.
            This parameter applies only to columns with a VARCHAR data type. Choose ``true`` to remove
            unneeded white space. The default is ``false`` .

          - **TruncateColumns** *(boolean) --*

            A value that specifies to truncate data in columns to the appropriate number of characters, so
            that the data fits in the column. This parameter applies only to columns with a VARCHAR or CHAR
            data type, and rows with a size of 4 MB or less. Choose ``true`` to truncate data. The default
            is ``false`` .

          - **Username** *(string) --*

            An Amazon Redshift user name for a registered user.

          - **WriteBufferSize** *(integer) --*

            The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The
            default is 1,024. Use this setting to tune performance.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Endpoint': {
                    'EndpointIdentifier': 'string',
                    'EndpointType': 'source'|'target',
                    'EngineName': 'string',
                    'EngineDisplayName': 'string',
                    'Username': 'string',
                    'ServerName': 'string',
                    'Port': 123,
                    'DatabaseName': 'string',
                    'ExtraConnectionAttributes': 'string',
                    'Status': 'string',
                    'KmsKeyId': 'string',
                    'EndpointArn': 'string',
                    'CertificateArn': 'string',
                    'SslMode': 'none'|'require'|'verify-ca'|'verify-full',
                    'ServiceAccessRoleArn': 'string',
                    'ExternalTableDefinition': 'string',
                    'ExternalId': 'string',
                    'DynamoDbSettings': {
                        'ServiceAccessRoleArn': 'string'
                    },
                    'S3Settings': {
                        'ServiceAccessRoleArn': 'string',
                        'ExternalTableDefinition': 'string',
                        'CsvRowDelimiter': 'string',
                        'CsvDelimiter': 'string',
                        'BucketFolder': 'string',
                        'BucketName': 'string',
                        'CompressionType': 'none'|'gzip',
                        'EncryptionMode': 'sse-s3'|'sse-kms',
                        'ServerSideEncryptionKmsKeyId': 'string',
                        'DataFormat': 'csv'|'parquet',
                        'EncodingType': 'plain'|'plain-dictionary'|'rle-dictionary',
                        'DictPageSizeLimit': 123,
                        'RowGroupLength': 123,
                        'DataPageSize': 123,
                        'ParquetVersion': 'parquet-1-0'|'parquet-2-0',
                        'EnableStatistics': True|False,
                        'IncludeOpForFullLoad': True|False,
                        'CdcInsertsOnly': True|False,
                        'TimestampColumnName': 'string',
                        'ParquetTimestampInMillisecond': True|False
                    },
                    'DmsTransferSettings': {
                        'ServiceAccessRoleArn': 'string',
                        'BucketName': 'string'
                    },
                    'MongoDbSettings': {
                        'Username': 'string',
                        'Password': 'string',
                        'ServerName': 'string',
                        'Port': 123,
                        'DatabaseName': 'string',
                        'AuthType': 'no'|'password',
                        'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
                        'NestingLevel': 'none'|'one',
                        'ExtractDocId': 'string',
                        'DocsToInvestigate': 'string',
                        'AuthSource': 'string',
                        'KmsKeyId': 'string'
                    },
                    'KinesisSettings': {
                        'StreamArn': 'string',
                        'MessageFormat': 'json',
                        'ServiceAccessRoleArn': 'string'
                    },
                    'ElasticsearchSettings': {
                        'ServiceAccessRoleArn': 'string',
                        'EndpointUri': 'string',
                        'FullLoadErrorPercentage': 123,
                        'ErrorRetryDuration': 123
                    },
                    'RedshiftSettings': {
                        'AcceptAnyDate': True|False,
                        'AfterConnectScript': 'string',
                        'BucketFolder': 'string',
                        'BucketName': 'string',
                        'ConnectionTimeout': 123,
                        'DatabaseName': 'string',
                        'DateFormat': 'string',
                        'EmptyAsNull': True|False,
                        'EncryptionMode': 'sse-s3'|'sse-kms',
                        'FileTransferUploadStreams': 123,
                        'LoadTimeout': 123,
                        'MaxFileSize': 123,
                        'Password': 'string',
                        'Port': 123,
                        'RemoveQuotes': True|False,
                        'ReplaceInvalidChars': 'string',
                        'ReplaceChars': 'string',
                        'ServerName': 'string',
                        'ServiceAccessRoleArn': 'string',
                        'ServerSideEncryptionKmsKeyId': 'string',
                        'TimeFormat': 'string',
                        'TrimBlanks': True|False,
                        'TruncateColumns': True|False,
                        'Username': 'string',
                        'WriteBufferSize': 123
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Endpoint** *(dict) --*

              The modified endpoint.

              - **EndpointIdentifier** *(string) --*

                The database endpoint identifier. Identifiers must begin with a letter; must contain only
                ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
                consecutive hyphens.

              - **EndpointType** *(string) --*

                The type of endpoint. Valid values are ``source`` and ``target`` .

              - **EngineName** *(string) --*

                The database engine name. Valid values, depending on the EndpointType, include mysql,
                oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2, azuredb, sybase,
                dynamodb, mongodb, and sqlserver.

              - **EngineDisplayName** *(string) --*

                The expanded name for the engine name. For example, if the ``EngineName`` parameter is
                "aurora," this value would be "Amazon Aurora MySQL."

              - **Username** *(string) --*

                The user name used to connect to the endpoint.

              - **ServerName** *(string) --*

                The name of the server at the endpoint.

              - **Port** *(integer) --*

                The port value used to access the endpoint.

              - **DatabaseName** *(string) --*

                The name of the database at the endpoint.

              - **ExtraConnectionAttributes** *(string) --*

                Additional connection attributes used to connect to the endpoint.

              - **Status** *(string) --*

                The status of the endpoint.

              - **KmsKeyId** *(string) --*

                An AWS KMS key identifier that is used to encrypt the connection parameters for the
                endpoint.

                If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
                encryption key.

                AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
                different default encryption key for each AWS Region.

              - **EndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **CertificateArn** *(string) --*

                The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

              - **SslMode** *(string) --*

                The SSL mode used to connect to the endpoint. The default value is ``none`` .

              - **ServiceAccessRoleArn** *(string) --*

                The Amazon Resource Name (ARN) used by the service access IAM role.

              - **ExternalTableDefinition** *(string) --*

                The external table definition.

              - **ExternalId** *(string) --*

                Value returned by a call to CreateEndpoint that can be used for cross-account validation.
                Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.

              - **DynamoDbSettings** *(dict) --*

                The settings for the target DynamoDB database. For more information, see the
                ``DynamoDBSettings`` structure.

                - **ServiceAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) used by the service access IAM role.

              - **S3Settings** *(dict) --*

                The settings for the S3 target endpoint. For more information, see the ``S3Settings``
                structure.

                - **ServiceAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) used by the service access IAM role.

                - **ExternalTableDefinition** *(string) --*

                  The external table definition.

                - **CsvRowDelimiter** *(string) --*

                  The delimiter used to separate rows in the source files. The default is a carriage return
                  (``\\n`` ).

                - **CsvDelimiter** *(string) --*

                  The delimiter used to separate columns in the source files. The default is a comma.

                - **BucketFolder** *(string) --*

                  An optional parameter to set a folder name in the S3 bucket. If provided, tables are
                  created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If this
                  parameter is not specified, then the path used is `` *schema_name* /*table_name* /`` .

                - **BucketName** *(string) --*

                  The name of the S3 bucket.

                - **CompressionType** *(string) --*

                  An optional parameter to use GZIP to compress the target files. Set to GZIP to compress
                  the target files. Set to NONE (the default) or do not use to leave the files
                  uncompressed. Applies to both .csv and .parquet file formats.

                - **EncryptionMode** *(string) --*

                  The type of server-side encryption that you want to use for your data. This encryption
                  type is part of the endpoint settings or the extra connections attributes for Amazon S3.
                  You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` , you
                  need an AWS Identity and Access Management (IAM) role with permission to allow
                  ``"arn:aws:s3:::dms-*"`` to use the following actions:

                  * ``s3:CreateBucket``

                  * ``s3:ListBucket``

                  * ``s3:DeleteBucket``

                  * ``s3:GetBucketLocation``

                  * ``s3:GetObject``

                  * ``s3:PutObject``

                  * ``s3:DeleteObject``

                  * ``s3:GetObjectVersion``

                  * ``s3:GetBucketPolicy``

                  * ``s3:PutBucketPolicy``

                  * ``s3:DeleteBucketPolicy``

                - **ServerSideEncryptionKmsKeyId** *(string) --*

                  If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID. The
                  key that you use needs an attached policy that enables AWS Identity and Access Management
                  (IAM) user permissions and allows use of the key.

                  Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
                  --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=*value*
                  ,BucketFolder=*value* ,BucketName=*value*
                  ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

                - **DataFormat** *(string) --*

                  The format of the data that you want to use for output. You can choose one of the
                  following:

                  * ``csv`` : This is a row-based file format with comma-separated values (.csv).

                  * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features
                  efficient compression and provides faster query response.

                - **EncodingType** *(string) --*

                  The type of encoding you are using:

                  * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store
                  repeated values more efficiently. This is the default.

                  * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

                  * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column.
                  The dictionary is stored in a dictionary page for each column chunk.

                - **DictPageSizeLimit** *(integer) --*

                  The maximum size of an encoded dictionary page of a column. If the dictionary page
                  exceeds this, this column is stored using an encoding type of ``PLAIN`` . This parameter
                  defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it
                  reverts to ``PLAIN`` encoding. This size is used for .parquet file format only.

                - **RowGroupLength** *(integer) --*

                  The number of rows in a row group. A smaller row group size provides faster reads. But as
                  the number of row groups grows, the slower writes become. This parameter defaults to
                  10,000 rows. This number is used for .parquet file format only.

                  If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row
                  group length in bytes (64 * 1024 * 1024).

                - **DataPageSize** *(integer) --*

                  The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB).
                  This number is used for .parquet file format only.

                - **ParquetVersion** *(string) --*

                  The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the
                  default) or ``parquet_2_0`` .

                - **EnableStatistics** *(boolean) --*

                  A value that enables statistics for Parquet pages and row groups. Choose ``true`` to
                  enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` ,
                  ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used
                  for .parquet file format only.

                - **IncludeOpForFullLoad** *(boolean) --*

                  A value that enables a full load to write INSERT operations to the comma-separated value
                  (.csv) output files only to indicate how the rows were added to the source database.

                  .. note::

                    AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

                  For full load, records can only be inserted. By default (the ``false`` setting), no
                  information is recorded in these output files for a full load to indicate that the rows
                  were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or
                  ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file.
                  This allows the format of your target records from a full load to be consistent with the
                  target records from a CDC load.

                  .. note::

                    This setting works together with the ``CdcInsertsOnly`` parameter for output to .csv
                    files only. For more information about how these settings work together, see
                    `Indicating Source DB Operations in Migrated S3 Data
                    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
                    in the *AWS Database Migration Service User Guide.* .

                - **CdcInsertsOnly** *(boolean) --*

                  A value that enables a change data capture (CDC) load to write only INSERT operations to
                  .csv or columnar storage (.parquet) output files. By default (the ``false`` setting), the
                  first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D
                  (DELETE). These values indicate whether the row was inserted, updated, or deleted at the
                  source database for a CDC load to the target.

                  If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database
                  are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are
                  recorded depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad``
                  is set to ``true`` , the first field of every CDC record is set to I to indicate the
                  INSERT operation at the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every
                  CDC record is written without a first field to indicate the INSERT operation at the
                  source. For more information about how these settings work together, see `Indicating
                  Source DB Operations in Migrated S3 Data
                  <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
                  in the *AWS Database Migration Service User Guide.* .

                  .. note::

                    AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
                    ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

                - **TimestampColumnName** *(string) --*

                  A value that when nonblank causes AWS DMS to add a column with timestamp information to
                  the endpoint data for an Amazon S3 target.

                  .. note::

                    AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

                  DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your
                  migrated data when you set ``TimestampColumnName`` to a nonblank value.

                  For a full load, each row of this timestamp column contains a timestamp for when the data
                  was transferred from the source to the target by DMS.

                  For a change data capture (CDC) load, each row of the timestamp column contains the
                  timestamp for the commit of that row in the source database.

                  The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By
                  default, the precision of this value is in microseconds. For a CDC load, the rounding of
                  the precision depends on the commit timestamp supported by DMS for the source database.

                  When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for
                  the timestamp column that you set with ``TimestampColumnName`` .

                - **ParquetTimestampInMillisecond** *(boolean) --*

                  A value that specifies the precision of any ``TIMESTAMP`` column values that are written
                  to an Amazon S3 object file in .parquet format.

                  .. note::

                    AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and
                    later.

                  When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all
                  ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise,
                  DMS writes them with microsecond precision.

                  Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
                  ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that
                  are .parquet formatted only if you plan to query or process the data with Athena or AWS
                  Glue.

                  .. note::

                    AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format
                    with microsecond precision.

                    Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the
                    timestamp column value that is inserted by setting the ``TimestampColumnName``
                    parameter.

              - **DmsTransferSettings** *(dict) --*

                The settings in JSON format for the DMS transfer type of source endpoint.

                Possible settings include the following:

                * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon S3
                bucket.

                * ``BucketName`` - The name of the S3 bucket to use.

                * ``CompressionType`` - An optional parameter to use GZIP to compress the target files. To
                use GZIP, set this value to ``NONE`` (the default). To keep the files uncompressed, don't
                use this value.

                Shorthand syntax for these settings is as follows:
                ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

                JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn": "string",
                "BucketName": "string", "CompressionType": "none"|"gzip" }``

                - **ServiceAccessRoleArn** *(string) --*

                  The IAM role that has permission to access the Amazon S3 bucket.

                - **BucketName** *(string) --*

                  The name of the S3 bucket to use.

              - **MongoDbSettings** *(dict) --*

                The settings for the MongoDB source endpoint. For more information, see the
                ``MongoDbSettings`` structure.

                - **Username** *(string) --*

                  The user name you use to access the MongoDB source endpoint.

                - **Password** *(string) --*

                  The password for the user account you use to access the MongoDB source endpoint.

                - **ServerName** *(string) --*

                  The name of the server on the MongoDB source endpoint.

                - **Port** *(integer) --*

                  The port value for the MongoDB source endpoint.

                - **DatabaseName** *(string) --*

                  The database name on the MongoDB source endpoint.

                - **AuthType** *(string) --*

                  The authentication type you use to access the MongoDB source endpoint.

                  Valid values: NO, PASSWORD

                  When NO is selected, user name and password parameters are not used and can be empty.

                - **AuthMechanism** *(string) --*

                  The authentication mechanism you use to access the MongoDB source endpoint.

                  Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

                  DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
                  SCRAM_SHA_1. This setting is not used when authType=No.

                - **NestingLevel** *(string) --*

                  Specifies either document or table mode.

                  Valid values: NONE, ONE

                  Default value is NONE. Specify NONE to use document mode. Specify ONE to use table mode.

                - **ExtractDocId** *(string) --*

                  Specifies the document ID. Use this setting when ``NestingLevel`` is set to NONE.

                  Default value is false.

                - **DocsToInvestigate** *(string) --*

                  Indicates the number of documents to preview to determine the document organization. Use
                  this setting when ``NestingLevel`` is set to ONE.

                  Must be a positive value greater than 0. Default value is 1000.

                - **AuthSource** *(string) --*

                  The MongoDB database name. This setting is not used when ``authType=NO`` .

                  The default is admin.

                - **KmsKeyId** *(string) --*

                  The AWS KMS key identifier that is used to encrypt the content on the replication
                  instance. If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses
                  your default encryption key. AWS KMS creates the default encryption key for your AWS
                  account. Your AWS account has a different default encryption key for each AWS Region.

              - **KinesisSettings** *(dict) --*

                The settings for the Amazon Kinesis source endpoint. For more information, see the
                ``KinesisSettings`` structure.

                - **StreamArn** *(string) --*

                  The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

                - **MessageFormat** *(string) --*

                  The output format for the records created on the endpoint. The message format is ``JSON``
                  .

                - **ServiceAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the Amazon
                  Kinesis data stream.

              - **ElasticsearchSettings** *(dict) --*

                The settings for the Elasticsearch source endpoint. For more information, see the
                ``ElasticsearchSettings`` structure.

                - **ServiceAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) used by service to access the IAM role.

                - **EndpointUri** *(string) --*

                  The endpoint for the Elasticsearch cluster.

                - **FullLoadErrorPercentage** *(integer) --*

                  The maximum percentage of records that can fail to be written before a full load
                  operation stops.

                - **ErrorRetryDuration** *(integer) --*

                  The maximum number of seconds that DMS retries failed API requests to the Elasticsearch
                  cluster.

              - **RedshiftSettings** *(dict) --*

                Settings for the Amazon Redshift endpoint.

                - **AcceptAnyDate** *(boolean) --*

                  A value that indicates to allow any date format, including invalid formats such as
                  00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or
                  ``false`` (the default).

                  This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with
                  the DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT
                  specification, Amazon Redshift inserts a NULL value into that field.

                - **AfterConnectScript** *(string) --*

                  Code to run after connecting. This parameter should contain the code itself, not the name
                  of a file containing the code.

                - **BucketFolder** *(string) --*

                  The location where the comma-separated value (.csv) files are stored before being
                  uploaded to the S3 bucket.

                - **BucketName** *(string) --*

                  The name of the S3 bucket you want to use

                - **ConnectionTimeout** *(integer) --*

                  A value that sets the amount of time to wait (in milliseconds) before timing out,
                  beginning from when you initially establish a connection.

                - **DatabaseName** *(string) --*

                  The name of the Amazon Redshift data warehouse (service) that you are working with.

                - **DateFormat** *(string) --*

                  The date format that you are using. Valid values are ``auto`` (case-sensitive), your date
                  format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it
                  defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some
                  that aren't supported when you use a date format string.

                  If your date and time values use formats different from each other, set this to ``auto`` .

                - **EmptyAsNull** *(boolean) --*

                  A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as
                  NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is
                  ``false`` .

                - **EncryptionMode** *(string) --*

                  The type of server-side encryption that you want to use for your data. This encryption
                  type is part of the endpoint settings or the extra connections attributes for Amazon S3.
                  You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . To use ``SSE_S3`` ,
                  create an AWS Identity and Access Management (IAM) role with a policy that allows
                  ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

                - **FileTransferUploadStreams** *(integer) --*

                  The number of threads used to upload a single file. This parameter accepts a value from 1
                  through 64. It defaults to 10.

                - **LoadTimeout** *(integer) --*

                  The amount of time to wait (in milliseconds) before timing out, beginning from when you
                  begin loading.

                - **MaxFileSize** *(integer) --*

                  The maximum size (in KB) of any .csv file used to transfer data to Amazon Redshift. This
                  accepts a value from 1 through 1,048,576. It defaults to 32,768 KB (32 MB).

                - **Password** *(string) --*

                  The password for the user named in the ``username`` property.

                - **Port** *(integer) --*

                  The port number for Amazon Redshift. The default value is 5439.

                - **RemoveQuotes** *(boolean) --*

                  A value that specifies to remove surrounding quotation marks from strings in the incoming
                  data. All characters within the quotation marks, including delimiters, are retained.
                  Choose ``true`` to remove quotation marks. The default is ``false`` .

                - **ReplaceInvalidChars** *(string) --*

                  A list of characters that you want to replace. Use with ``ReplaceChars`` .

                - **ReplaceChars** *(string) --*

                  A value that specifies to replaces the invalid characters specified in
                  ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is
                  ``"?"`` .

                - **ServerName** *(string) --*

                  The name of the Amazon Redshift cluster you are using.

                - **ServiceAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift
                  service.

                - **ServerSideEncryptionKmsKeyId** *(string) --*

                  The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide
                  this key ID. The key that you use needs an attached policy that enables IAM user
                  permissions and allows use of the key.

                - **TimeFormat** *(string) --*

                  The time format that you want to use. Valid values are ``auto`` (case-sensitive),
                  ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10.
                  Using ``auto`` recognizes most strings, even some that aren't supported when you use a
                  time format string.

                  If your date and time values use formats different from each other, set this parameter to
                  ``auto`` .

                - **TrimBlanks** *(boolean) --*

                  A value that specifies to remove the trailing white space characters from a VARCHAR
                  string. This parameter applies only to columns with a VARCHAR data type. Choose ``true``
                  to remove unneeded white space. The default is ``false`` .

                - **TruncateColumns** *(boolean) --*

                  A value that specifies to truncate data in columns to the appropriate number of
                  characters, so that the data fits in the column. This parameter applies only to columns
                  with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true``
                  to truncate data. The default is ``false`` .

                - **Username** *(string) --*

                  An Amazon Redshift user name for a registered user.

                - **WriteBufferSize** *(integer) --*

                  The size of the write buffer to use in rows. Valid values range from 1 through 2,048. The
                  default is 1,024. Use this setting to tune performance.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str = None,
        SourceType: str = None,
        EventCategories: List[str] = None,
        Enabled: bool = None,
    ) -> ClientModifyEventSubscriptionResponseTypeDef:
        """
        Modifies an existing AWS DMS event notification subscription.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ModifyEventSubscription>`_

        **Request Syntax**
        ::

          response = client.modify_event_subscription(
              SubscriptionName='string',
              SnsTopicArn='string',
              SourceType='string',
              EventCategories=[
                  'string',
              ],
              Enabled=True|False
          )
        :type SubscriptionName: string
        :param SubscriptionName: **[REQUIRED]**

          The name of the AWS DMS event notification subscription to be modified.

        :type SnsTopicArn: string
        :param SnsTopicArn:

          The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification. The ARN is
          created by Amazon SNS when you create a topic and subscribe to it.

        :type SourceType: string
        :param SourceType:

          The type of AWS DMS resource that generates the events you want to subscribe to.

          Valid values: replication-instance | replication-task

        :type EventCategories: list
        :param EventCategories:

          A list of event categories for a source type that you want to subscribe to. Use the
          ``DescribeEventCategories`` action to see a list of event categories.

          - *(string) --*

        :type Enabled: boolean
        :param Enabled:

          A Boolean value; set to **true** to activate the subscription.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EventSubscription': {
                    'CustomerAwsId': 'string',
                    'CustSubscriptionId': 'string',
                    'SnsTopicArn': 'string',
                    'Status': 'string',
                    'SubscriptionCreationTime': 'string',
                    'SourceType': 'string',
                    'SourceIdsList': [
                        'string',
                    ],
                    'EventCategoriesList': [
                        'string',
                    ],
                    'Enabled': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **EventSubscription** *(dict) --*

              The modified event subscription.

              - **CustomerAwsId** *(string) --*

                The AWS customer account associated with the AWS DMS event notification subscription.

              - **CustSubscriptionId** *(string) --*

                The AWS DMS event notification subscription Id.

              - **SnsTopicArn** *(string) --*

                The topic ARN of the AWS DMS event notification subscription.

              - **Status** *(string) --*

                The status of the AWS DMS event notification subscription.

                Constraints:

                Can be one of the following: creating | modifying | deleting | active | no-permission |
                topic-not-exist

                The status "no-permission" indicates that AWS DMS no longer has permission to post to the
                SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the
                subscription was created.

              - **SubscriptionCreationTime** *(string) --*

                The time the RDS event notification subscription was created.

              - **SourceType** *(string) --*

                The type of AWS DMS resource that generates events.

                Valid values: replication-instance | replication-server | security-group | replication-task

              - **SourceIdsList** *(list) --*

                A list of source Ids for the event subscription.

                - *(string) --*

              - **EventCategoriesList** *(list) --*

                A lists of event categories.

                - *(string) --*

              - **Enabled** *(boolean) --*

                Boolean value that indicates if the event subscription is enabled.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_replication_instance(
        self,
        ReplicationInstanceArn: str,
        AllocatedStorage: int = None,
        ApplyImmediately: bool = None,
        ReplicationInstanceClass: str = None,
        VpcSecurityGroupIds: List[str] = None,
        PreferredMaintenanceWindow: str = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AllowMajorVersionUpgrade: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        ReplicationInstanceIdentifier: str = None,
    ) -> ClientModifyReplicationInstanceResponseTypeDef:
        """
        Modifies the replication instance to apply new settings. You can change one or more parameters by
        specifying these parameters and the new values in the request.

        Some settings are applied during the maintenance window.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ModifyReplicationInstance>`_

        **Request Syntax**
        ::

          response = client.modify_replication_instance(
              ReplicationInstanceArn='string',
              AllocatedStorage=123,
              ApplyImmediately=True|False,
              ReplicationInstanceClass='string',
              VpcSecurityGroupIds=[
                  'string',
              ],
              PreferredMaintenanceWindow='string',
              MultiAZ=True|False,
              EngineVersion='string',
              AllowMajorVersionUpgrade=True|False,
              AutoMinorVersionUpgrade=True|False,
              ReplicationInstanceIdentifier='string'
          )
        :type ReplicationInstanceArn: string
        :param ReplicationInstanceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the replication instance.

        :type AllocatedStorage: integer
        :param AllocatedStorage:

          The amount of storage (in gigabytes) to be allocated for the replication instance.

        :type ApplyImmediately: boolean
        :param ApplyImmediately:

          Indicates whether the changes should be applied immediately or during the next maintenance window.

        :type ReplicationInstanceClass: string
        :param ReplicationInstanceClass:

          The compute and memory capacity of the replication instance.

          Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large |
          dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

        :type VpcSecurityGroupIds: list
        :param VpcSecurityGroupIds:

          Specifies the VPC security group to be used with the replication instance. The VPC security group
          must work with the VPC containing the replication instance.

          - *(string) --*

        :type PreferredMaintenanceWindow: string
        :param PreferredMaintenanceWindow:

          The weekly time range (in UTC) during which system maintenance can occur, which might result in
          an outage. Changing this parameter does not result in an outage, except in the following
          situation, and the change is asynchronously applied as soon as possible. If moving this window to
          the current time, there must be at least 30 minutes between the current time and end of the
          window to ensure pending changes are applied.

          Default: Uses existing setting

          Format: ddd:hh24:mi-ddd:hh24:mi

          Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun

          Constraints: Must be at least 30 minutes

        :type MultiAZ: boolean
        :param MultiAZ:

          Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
          ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

        :type EngineVersion: string
        :param EngineVersion:

          The engine version number of the replication instance.

        :type AllowMajorVersionUpgrade: boolean
        :param AllowMajorVersionUpgrade:

          Indicates that major version upgrades are allowed. Changing this parameter does not result in an
          outage, and the change is asynchronously applied as soon as possible.

          This parameter must be set to ``true`` when specifying a value for the ``EngineVersion``
          parameter that is a different major version than the replication instance's current version.

        :type AutoMinorVersionUpgrade: boolean
        :param AutoMinorVersionUpgrade:

          Indicates that minor version upgrades will be applied automatically to the replication instance
          during the maintenance window. Changing this parameter does not result in an outage except in the
          following case and the change is asynchronously applied as soon as possible. An outage will
          result if this parameter is set to ``true`` during the maintenance window, and a newer minor
          version is available, and AWS DMS has enabled auto patching for that engine version.

        :type ReplicationInstanceIdentifier: string
        :param ReplicationInstanceIdentifier:

          The replication instance identifier. This parameter is stored as a lowercase string.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationInstance': {
                    'ReplicationInstanceIdentifier': 'string',
                    'ReplicationInstanceClass': 'string',
                    'ReplicationInstanceStatus': 'string',
                    'AllocatedStorage': 123,
                    'InstanceCreateTime': datetime(2015, 1, 1),
                    'VpcSecurityGroups': [
                        {
                            'VpcSecurityGroupId': 'string',
                            'Status': 'string'
                        },
                    ],
                    'AvailabilityZone': 'string',
                    'ReplicationSubnetGroup': {
                        'ReplicationSubnetGroupIdentifier': 'string',
                        'ReplicationSubnetGroupDescription': 'string',
                        'VpcId': 'string',
                        'SubnetGroupStatus': 'string',
                        'Subnets': [
                            {
                                'SubnetIdentifier': 'string',
                                'SubnetAvailabilityZone': {
                                    'Name': 'string'
                                },
                                'SubnetStatus': 'string'
                            },
                        ]
                    },
                    'PreferredMaintenanceWindow': 'string',
                    'PendingModifiedValues': {
                        'ReplicationInstanceClass': 'string',
                        'AllocatedStorage': 123,
                        'MultiAZ': True|False,
                        'EngineVersion': 'string'
                    },
                    'MultiAZ': True|False,
                    'EngineVersion': 'string',
                    'AutoMinorVersionUpgrade': True|False,
                    'KmsKeyId': 'string',
                    'ReplicationInstanceArn': 'string',
                    'ReplicationInstancePublicIpAddress': 'string',
                    'ReplicationInstancePrivateIpAddress': 'string',
                    'ReplicationInstancePublicIpAddresses': [
                        'string',
                    ],
                    'ReplicationInstancePrivateIpAddresses': [
                        'string',
                    ],
                    'PubliclyAccessible': True|False,
                    'SecondaryAvailabilityZone': 'string',
                    'FreeUntil': datetime(2015, 1, 1),
                    'DnsNameServers': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationInstance** *(dict) --*

              The modified replication instance.

              - **ReplicationInstanceIdentifier** *(string) --*

                The replication instance identifier. This parameter is stored as a lowercase string.

                Constraints:

                * Must contain from 1 to 63 alphanumeric characters or hyphens.

                * First character must be a letter.

                * Cannot end with a hyphen or contain two consecutive hyphens.

                Example: ``myrepinstance``

              - **ReplicationInstanceClass** *(string) --*

                The compute and memory capacity of the replication instance.

                Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large |
                dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

              - **ReplicationInstanceStatus** *(string) --*

                The status of the replication instance.

              - **AllocatedStorage** *(integer) --*

                The amount of storage (in gigabytes) that is allocated for the replication instance.

              - **InstanceCreateTime** *(datetime) --*

                The time the replication instance was created.

              - **VpcSecurityGroups** *(list) --*

                The VPC security group for the instance.

                - *(dict) --*

                  - **VpcSecurityGroupId** *(string) --*

                    The VPC security group Id.

                  - **Status** *(string) --*

                    The status of the VPC security group.

              - **AvailabilityZone** *(string) --*

                The Availability Zone for the instance.

              - **ReplicationSubnetGroup** *(dict) --*

                The subnet group for the replication instance.

                - **ReplicationSubnetGroupIdentifier** *(string) --*

                  The identifier of the replication instance subnet group.

                - **ReplicationSubnetGroupDescription** *(string) --*

                  A description for the replication subnet group.

                - **VpcId** *(string) --*

                  The ID of the VPC.

                - **SubnetGroupStatus** *(string) --*

                  The status of the subnet group.

                - **Subnets** *(list) --*

                  The subnets that are in the subnet group.

                  - *(dict) --*

                    - **SubnetIdentifier** *(string) --*

                      The subnet identifier.

                    - **SubnetAvailabilityZone** *(dict) --*

                      The Availability Zone of the subnet.

                      - **Name** *(string) --*

                        The name of the availability zone.

                    - **SubnetStatus** *(string) --*

                      The status of the subnet.

              - **PreferredMaintenanceWindow** *(string) --*

                The maintenance window times for the replication instance.

              - **PendingModifiedValues** *(dict) --*

                The pending modification values.

                - **ReplicationInstanceClass** *(string) --*

                  The compute and memory capacity of the replication instance.

                  Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
                  | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

                - **AllocatedStorage** *(integer) --*

                  The amount of storage (in gigabytes) that is allocated for the replication instance.

                - **MultiAZ** *(boolean) --*

                  Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
                  ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

                - **EngineVersion** *(string) --*

                  The engine version number of the replication instance.

              - **MultiAZ** *(boolean) --*

                Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
                ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

              - **EngineVersion** *(string) --*

                The engine version number of the replication instance.

              - **AutoMinorVersionUpgrade** *(boolean) --*

                Boolean value indicating if minor version upgrades will be automatically applied to the
                instance.

              - **KmsKeyId** *(string) --*

                An AWS KMS key identifier that is used to encrypt the data on the replication instance.

                If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
                encryption key.

                AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
                different default encryption key for each AWS Region.

              - **ReplicationInstanceArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication instance.

              - **ReplicationInstancePublicIpAddress** *(string) --*

                The public IP address of the replication instance.

              - **ReplicationInstancePrivateIpAddress** *(string) --*

                The private IP address of the replication instance.

              - **ReplicationInstancePublicIpAddresses** *(list) --*

                One or more public IP addresses for the replication instance.

                - *(string) --*

              - **ReplicationInstancePrivateIpAddresses** *(list) --*

                One or more private IP addresses for the replication instance.

                - *(string) --*

              - **PubliclyAccessible** *(boolean) --*

                Specifies the accessibility options for the replication instance. A value of ``true``
                represents an instance with a public IP address. A value of ``false`` represents an
                instance with a private IP address. The default value is ``true`` .

              - **SecondaryAvailabilityZone** *(string) --*

                The availability zone of the standby replication instance in a Multi-AZ deployment.

              - **FreeUntil** *(datetime) --*

                The expiration date of the free replication instance that is part of the Free DMS program.

              - **DnsNameServers** *(string) --*

                The DNS name servers for the replication instance.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_replication_subnet_group(
        self,
        ReplicationSubnetGroupIdentifier: str,
        SubnetIds: List[str],
        ReplicationSubnetGroupDescription: str = None,
    ) -> ClientModifyReplicationSubnetGroupResponseTypeDef:
        """
        Modifies the settings for the specified replication subnet group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ModifyReplicationSubnetGroup>`_

        **Request Syntax**
        ::

          response = client.modify_replication_subnet_group(
              ReplicationSubnetGroupIdentifier='string',
              ReplicationSubnetGroupDescription='string',
              SubnetIds=[
                  'string',
              ]
          )
        :type ReplicationSubnetGroupIdentifier: string
        :param ReplicationSubnetGroupIdentifier: **[REQUIRED]**

          The name of the replication instance subnet group.

        :type ReplicationSubnetGroupDescription: string
        :param ReplicationSubnetGroupDescription:

          A description for the replication instance subnet group.

        :type SubnetIds: list
        :param SubnetIds: **[REQUIRED]**

          A list of subnet IDs.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationSubnetGroup': {
                    'ReplicationSubnetGroupIdentifier': 'string',
                    'ReplicationSubnetGroupDescription': 'string',
                    'VpcId': 'string',
                    'SubnetGroupStatus': 'string',
                    'Subnets': [
                        {
                            'SubnetIdentifier': 'string',
                            'SubnetAvailabilityZone': {
                                'Name': 'string'
                            },
                            'SubnetStatus': 'string'
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationSubnetGroup** *(dict) --*

              The modified replication subnet group.

              - **ReplicationSubnetGroupIdentifier** *(string) --*

                The identifier of the replication instance subnet group.

              - **ReplicationSubnetGroupDescription** *(string) --*

                A description for the replication subnet group.

              - **VpcId** *(string) --*

                The ID of the VPC.

              - **SubnetGroupStatus** *(string) --*

                The status of the subnet group.

              - **Subnets** *(list) --*

                The subnets that are in the subnet group.

                - *(dict) --*

                  - **SubnetIdentifier** *(string) --*

                    The subnet identifier.

                  - **SubnetAvailabilityZone** *(dict) --*

                    The Availability Zone of the subnet.

                    - **Name** *(string) --*

                      The name of the availability zone.

                  - **SubnetStatus** *(string) --*

                    The status of the subnet.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def modify_replication_task(
        self,
        ReplicationTaskArn: str,
        ReplicationTaskIdentifier: str = None,
        MigrationType: str = None,
        TableMappings: str = None,
        ReplicationTaskSettings: str = None,
        CdcStartTime: datetime = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None,
    ) -> Dict[str, Any]:
        """
        Modifies the specified replication task.

        You can't modify the task endpoints. The task must be stopped before you can modify it.

        For more information about AWS DMS tasks, see `Working with Migration Tasks
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html>`__ in the *AWS Database
        Migration Service User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ModifyReplicationTask>`_

        **Request Syntax**
        ::

          response = client.modify_replication_task(
              ReplicationTaskArn='string',
              ReplicationTaskIdentifier='string',
              MigrationType='full-load'|'cdc'|'full-load-and-cdc',
              TableMappings='string',
              ReplicationTaskSettings='string',
              CdcStartTime=datetime(2015, 1, 1),
              CdcStartPosition='string',
              CdcStopPosition='string'
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the replication task.

        :type ReplicationTaskIdentifier: string
        :param ReplicationTaskIdentifier:

          The replication task identifier.

          Constraints:

          * Must contain from 1 to 255 alphanumeric characters or hyphens.

          * First character must be a letter.

          * Cannot end with a hyphen or contain two consecutive hyphens.

        :type MigrationType: string
        :param MigrationType:

          The migration type. Valid values: ``full-load`` | ``cdc`` | ``full-load-and-cdc``

        :type TableMappings: string
        :param TableMappings:

          When using the AWS CLI or boto3, provide the path of the JSON file that contains the table
          mappings. Precede the path with ``file://`` . When working with the DMS API, provide the JSON as
          the parameter value, for example: ``--table-mappings file://mappingfile.json``

        :type ReplicationTaskSettings: string
        :param ReplicationTaskSettings:

          JSON file that contains settings for the task, such as target metadata settings.

        :type CdcStartTime: datetime
        :param CdcStartTime:

          Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or
          CdcStartPosition to specify when you want a CDC operation to start. Specifying both values
          results in an error.

          Timestamp Example: --cdc-start-time “2018-03-08T12:12:12”

        :type CdcStartPosition: string
        :param CdcStartPosition:

          Indicates when you want a change data capture (CDC) operation to start. Use either
          CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying
          both values results in an error.

          The value can be in date, checkpoint, or LSN/SCN format.

          Date Example: --cdc-start-position “2018-03-08T12:12:12”

          Checkpoint Example: --cdc-start-position
          "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"
        "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"

          LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”

          .. note::

            When you use this task setting with a source PostgreSQL database, a logical replication slot
            should already be created and associated with the source endpoint. You can verify this by
            setting the ``slotName`` extra connection attribute to the name of this logical replication
            slot. For more information, see `Extra Connection Attributes When Using PostgreSQL as a Source
            for AWS DMS
            <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`__
            .

        :type CdcStopPosition: string
        :param CdcStopPosition:

          Indicates when you want a change data capture (CDC) operation to stop. The value can be either
          server time or commit time.

          Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”

          Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12 “

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationTask': {
                    'ReplicationTaskIdentifier': 'string',
                    'SourceEndpointArn': 'string',
                    'TargetEndpointArn': 'string',
                    'ReplicationInstanceArn': 'string',
                    'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
                    'TableMappings': 'string',
                    'ReplicationTaskSettings': 'string',
                    'Status': 'string',
                    'LastFailureMessage': 'string',
                    'StopReason': 'string',
                    'ReplicationTaskCreationDate': datetime(2015, 1, 1),
                    'ReplicationTaskStartDate': datetime(2015, 1, 1),
                    'CdcStartPosition': 'string',
                    'CdcStopPosition': 'string',
                    'RecoveryCheckpoint': 'string',
                    'ReplicationTaskArn': 'string',
                    'ReplicationTaskStats': {
                        'FullLoadProgressPercent': 123,
                        'ElapsedTimeMillis': 123,
                        'TablesLoaded': 123,
                        'TablesLoading': 123,
                        'TablesQueued': 123,
                        'TablesErrored': 123,
                        'FreshStartDate': datetime(2015, 1, 1),
                        'StartDate': datetime(2015, 1, 1),
                        'StopDate': datetime(2015, 1, 1),
                        'FullLoadStartDate': datetime(2015, 1, 1),
                        'FullLoadFinishDate': datetime(2015, 1, 1)
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationTask** *(dict) --*

              The replication task that was modified.

              - **ReplicationTaskIdentifier** *(string) --*

                The user-assigned replication task identifier or name.

                Constraints:

                * Must contain from 1 to 255 alphanumeric characters or hyphens.

                * First character must be a letter.

                * Cannot end with a hyphen or contain two consecutive hyphens.

              - **SourceEndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **TargetEndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **ReplicationInstanceArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication instance.

              - **MigrationType** *(string) --*

                The type of migration.

              - **TableMappings** *(string) --*

                Table mappings specified in the task.

              - **ReplicationTaskSettings** *(string) --*

                The settings for the replication task.

              - **Status** *(string) --*

                The status of the replication task.

              - **LastFailureMessage** *(string) --*

                The last error (failure) message generated for the replication instance.

              - **StopReason** *(string) --*

                The reason the replication task was stopped.

              - **ReplicationTaskCreationDate** *(datetime) --*

                The date the replication task was created.

              - **ReplicationTaskStartDate** *(datetime) --*

                The date the replication task is scheduled to start.

              - **CdcStartPosition** *(string) --*

                Indicates when you want a change data capture (CDC) operation to start. Use either
                ``CdcStartPosition`` or ``CdcStartTime`` to specify when you want the CDC operation to
                start. Specifying both values results in an error.

                The value can be in date, checkpoint, or LSN/SCN format.

                Date Example: --cdc-start-position “2018-03-08T12:12:12”

                Checkpoint Example: --cdc-start-position
                "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"
        "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"

                LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”

              - **CdcStopPosition** *(string) --*

                Indicates when you want a change data capture (CDC) operation to stop. The value can be
                either server time or commit time.

                Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”

                Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12 “

              - **RecoveryCheckpoint** *(string) --*

                Indicates the last checkpoint that occurred during a change data capture (CDC) operation.
                You can provide this value to the ``CdcStartPosition`` parameter to start a CDC operation
                that begins at that checkpoint.

              - **ReplicationTaskArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication task.

              - **ReplicationTaskStats** *(dict) --*

                The statistics for the task, including elapsed time, tables loaded, and table errors.

                - **FullLoadProgressPercent** *(integer) --*

                  The percent complete for the full load migration task.

                - **ElapsedTimeMillis** *(integer) --*

                  The elapsed time of the task, in milliseconds.

                - **TablesLoaded** *(integer) --*

                  The number of tables loaded for this task.

                - **TablesLoading** *(integer) --*

                  The number of tables currently loading for this task.

                - **TablesQueued** *(integer) --*

                  The number of tables queued for this task.

                - **TablesErrored** *(integer) --*

                  The number of errors that have occurred during this task.

                - **FreshStartDate** *(datetime) --*

                  The date the replication task was started either with a fresh start or a target reload.

                - **StartDate** *(datetime) --*

                  The date the replication task was started either with a fresh start or a resume. For more
                  information, see `StartReplicationTaskType
                  <https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html#DMS-StartReplicationTask-request-StartReplicationTaskType>`__
                  .

                - **StopDate** *(datetime) --*

                  The date the replication task was stopped.

                - **FullLoadStartDate** *(datetime) --*

                  The date the the replication task full load was started.

                - **FullLoadFinishDate** *(datetime) --*

                  The date the replication task full load was completed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reboot_replication_instance(
        self, ReplicationInstanceArn: str, ForceFailover: bool = None
    ) -> ClientRebootReplicationInstanceResponseTypeDef:
        """
        Reboots a replication instance. Rebooting results in a momentary outage, until the replication
        instance becomes available again.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/RebootReplicationInstance>`_

        **Request Syntax**
        ::

          response = client.reboot_replication_instance(
              ReplicationInstanceArn='string',
              ForceFailover=True|False
          )
        :type ReplicationInstanceArn: string
        :param ReplicationInstanceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the replication instance.

        :type ForceFailover: boolean
        :param ForceFailover:

          If this parameter is ``true`` , the reboot is conducted through a Multi-AZ failover. (If the
          instance isn't configured for Multi-AZ, then you can't specify ``true`` .)

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationInstance': {
                    'ReplicationInstanceIdentifier': 'string',
                    'ReplicationInstanceClass': 'string',
                    'ReplicationInstanceStatus': 'string',
                    'AllocatedStorage': 123,
                    'InstanceCreateTime': datetime(2015, 1, 1),
                    'VpcSecurityGroups': [
                        {
                            'VpcSecurityGroupId': 'string',
                            'Status': 'string'
                        },
                    ],
                    'AvailabilityZone': 'string',
                    'ReplicationSubnetGroup': {
                        'ReplicationSubnetGroupIdentifier': 'string',
                        'ReplicationSubnetGroupDescription': 'string',
                        'VpcId': 'string',
                        'SubnetGroupStatus': 'string',
                        'Subnets': [
                            {
                                'SubnetIdentifier': 'string',
                                'SubnetAvailabilityZone': {
                                    'Name': 'string'
                                },
                                'SubnetStatus': 'string'
                            },
                        ]
                    },
                    'PreferredMaintenanceWindow': 'string',
                    'PendingModifiedValues': {
                        'ReplicationInstanceClass': 'string',
                        'AllocatedStorage': 123,
                        'MultiAZ': True|False,
                        'EngineVersion': 'string'
                    },
                    'MultiAZ': True|False,
                    'EngineVersion': 'string',
                    'AutoMinorVersionUpgrade': True|False,
                    'KmsKeyId': 'string',
                    'ReplicationInstanceArn': 'string',
                    'ReplicationInstancePublicIpAddress': 'string',
                    'ReplicationInstancePrivateIpAddress': 'string',
                    'ReplicationInstancePublicIpAddresses': [
                        'string',
                    ],
                    'ReplicationInstancePrivateIpAddresses': [
                        'string',
                    ],
                    'PubliclyAccessible': True|False,
                    'SecondaryAvailabilityZone': 'string',
                    'FreeUntil': datetime(2015, 1, 1),
                    'DnsNameServers': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationInstance** *(dict) --*

              The replication instance that is being rebooted.

              - **ReplicationInstanceIdentifier** *(string) --*

                The replication instance identifier. This parameter is stored as a lowercase string.

                Constraints:

                * Must contain from 1 to 63 alphanumeric characters or hyphens.

                * First character must be a letter.

                * Cannot end with a hyphen or contain two consecutive hyphens.

                Example: ``myrepinstance``

              - **ReplicationInstanceClass** *(string) --*

                The compute and memory capacity of the replication instance.

                Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large |
                dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

              - **ReplicationInstanceStatus** *(string) --*

                The status of the replication instance.

              - **AllocatedStorage** *(integer) --*

                The amount of storage (in gigabytes) that is allocated for the replication instance.

              - **InstanceCreateTime** *(datetime) --*

                The time the replication instance was created.

              - **VpcSecurityGroups** *(list) --*

                The VPC security group for the instance.

                - *(dict) --*

                  - **VpcSecurityGroupId** *(string) --*

                    The VPC security group Id.

                  - **Status** *(string) --*

                    The status of the VPC security group.

              - **AvailabilityZone** *(string) --*

                The Availability Zone for the instance.

              - **ReplicationSubnetGroup** *(dict) --*

                The subnet group for the replication instance.

                - **ReplicationSubnetGroupIdentifier** *(string) --*

                  The identifier of the replication instance subnet group.

                - **ReplicationSubnetGroupDescription** *(string) --*

                  A description for the replication subnet group.

                - **VpcId** *(string) --*

                  The ID of the VPC.

                - **SubnetGroupStatus** *(string) --*

                  The status of the subnet group.

                - **Subnets** *(list) --*

                  The subnets that are in the subnet group.

                  - *(dict) --*

                    - **SubnetIdentifier** *(string) --*

                      The subnet identifier.

                    - **SubnetAvailabilityZone** *(dict) --*

                      The Availability Zone of the subnet.

                      - **Name** *(string) --*

                        The name of the availability zone.

                    - **SubnetStatus** *(string) --*

                      The status of the subnet.

              - **PreferredMaintenanceWindow** *(string) --*

                The maintenance window times for the replication instance.

              - **PendingModifiedValues** *(dict) --*

                The pending modification values.

                - **ReplicationInstanceClass** *(string) --*

                  The compute and memory capacity of the replication instance.

                  Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large
                  | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

                - **AllocatedStorage** *(integer) --*

                  The amount of storage (in gigabytes) that is allocated for the replication instance.

                - **MultiAZ** *(boolean) --*

                  Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
                  ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

                - **EngineVersion** *(string) --*

                  The engine version number of the replication instance.

              - **MultiAZ** *(boolean) --*

                Specifies whether the replication instance is a Multi-AZ deployment. You cannot set the
                ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

              - **EngineVersion** *(string) --*

                The engine version number of the replication instance.

              - **AutoMinorVersionUpgrade** *(boolean) --*

                Boolean value indicating if minor version upgrades will be automatically applied to the
                instance.

              - **KmsKeyId** *(string) --*

                An AWS KMS key identifier that is used to encrypt the data on the replication instance.

                If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses your default
                encryption key.

                AWS KMS creates the default encryption key for your AWS account. Your AWS account has a
                different default encryption key for each AWS Region.

              - **ReplicationInstanceArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication instance.

              - **ReplicationInstancePublicIpAddress** *(string) --*

                The public IP address of the replication instance.

              - **ReplicationInstancePrivateIpAddress** *(string) --*

                The private IP address of the replication instance.

              - **ReplicationInstancePublicIpAddresses** *(list) --*

                One or more public IP addresses for the replication instance.

                - *(string) --*

              - **ReplicationInstancePrivateIpAddresses** *(list) --*

                One or more private IP addresses for the replication instance.

                - *(string) --*

              - **PubliclyAccessible** *(boolean) --*

                Specifies the accessibility options for the replication instance. A value of ``true``
                represents an instance with a public IP address. A value of ``false`` represents an
                instance with a private IP address. The default value is ``true`` .

              - **SecondaryAvailabilityZone** *(string) --*

                The availability zone of the standby replication instance in a Multi-AZ deployment.

              - **FreeUntil** *(datetime) --*

                The expiration date of the free replication instance that is part of the Free DMS program.

              - **DnsNameServers** *(string) --*

                The DNS name servers for the replication instance.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def refresh_schemas(
        self, EndpointArn: str, ReplicationInstanceArn: str
    ) -> ClientRefreshSchemasResponseTypeDef:
        """
        Populates the schema for the specified endpoint. This is an asynchronous operation and can take
        several minutes. You can check the status of this operation by calling the
        DescribeRefreshSchemasStatus operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/RefreshSchemas>`_

        **Request Syntax**
        ::

          response = client.refresh_schemas(
              EndpointArn='string',
              ReplicationInstanceArn='string'
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

        :type ReplicationInstanceArn: string
        :param ReplicationInstanceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the replication instance.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RefreshSchemasStatus': {
                    'EndpointArn': 'string',
                    'ReplicationInstanceArn': 'string',
                    'Status': 'successful'|'failed'|'refreshing',
                    'LastRefreshDate': datetime(2015, 1, 1),
                    'LastFailureMessage': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **RefreshSchemasStatus** *(dict) --*

              The status of the refreshed schema.

              - **EndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **ReplicationInstanceArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication instance.

              - **Status** *(string) --*

                The status of the schema.

              - **LastRefreshDate** *(datetime) --*

                The date the schema was last refreshed.

              - **LastFailureMessage** *(string) --*

                The last failure message for the schema.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload_tables(
        self,
        ReplicationTaskArn: str,
        TablesToReload: List[ClientReloadTablesTablesToReloadTypeDef],
        ReloadOption: str = None,
    ) -> ClientReloadTablesResponseTypeDef:
        """
        Reloads the target database table with the source data.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ReloadTables>`_

        **Request Syntax**
        ::

          response = client.reload_tables(
              ReplicationTaskArn='string',
              TablesToReload=[
                  {
                      'SchemaName': 'string',
                      'TableName': 'string'
                  },
              ],
              ReloadOption='data-reload'|'validate-only'
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the replication task.

        :type TablesToReload: list
        :param TablesToReload: **[REQUIRED]**

          The name and schema of the table to be reloaded.

          - *(dict) --*

            - **SchemaName** *(string) --*

              The schema name of the table to be reloaded.

            - **TableName** *(string) --*

              The table name of the table to be reloaded.

        :type ReloadOption: string
        :param ReloadOption:

          Options for reload. Specify ``data-reload`` to reload the data and re-validate it if validation
          is enabled. Specify ``validate-only`` to re-validate the table. This option applies only when
          validation is enabled for the task.

          Valid values: data-reload, validate-only

          Default value is data-reload.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationTaskArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationTaskArn** *(string) --*

              The Amazon Resource Name (ARN) of the replication task.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags_from_resource(
        self, ResourceArn: str, TagKeys: List[str]
    ) -> Dict[str, Any]:
        """
        Removes metadata tags from a DMS resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/RemoveTagsFromResource>`_

        **Request Syntax**
        ::

          response = client.remove_tags_from_resource(
              ResourceArn='string',
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          An AWS DMS resource from which you want to remove tag(s). The value for this parameter is an
          Amazon Resource Name (ARN).

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          The tag key (name) of the tag to be removed.

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
    def start_replication_task(
        self,
        ReplicationTaskArn: str,
        StartReplicationTaskType: str,
        CdcStartTime: datetime = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None,
    ) -> Dict[str, Any]:
        """
        Starts the replication task.

        For more information about AWS DMS tasks, see `Working with Migration Tasks
        <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html>`__ in the *AWS Database
        Migration Service User Guide.*

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/StartReplicationTask>`_

        **Request Syntax**
        ::

          response = client.start_replication_task(
              ReplicationTaskArn='string',
              StartReplicationTaskType='start-replication'|'resume-processing'|'reload-target',
              CdcStartTime=datetime(2015, 1, 1),
              CdcStartPosition='string',
              CdcStopPosition='string'
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the replication task to be started.

        :type StartReplicationTaskType: string
        :param StartReplicationTaskType: **[REQUIRED]**

          The type of replication task.

        :type CdcStartTime: datetime
        :param CdcStartTime:

          Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or
          CdcStartPosition to specify when you want a CDC operation to start. Specifying both values
          results in an error.

          Timestamp Example: --cdc-start-time “2018-03-08T12:12:12”

        :type CdcStartPosition: string
        :param CdcStartPosition:

          Indicates when you want a change data capture (CDC) operation to start. Use either
          CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying
          both values results in an error.

          The value can be in date, checkpoint, or LSN/SCN format.

          Date Example: --cdc-start-position “2018-03-08T12:12:12”

          Checkpoint Example: --cdc-start-position
          "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"
        "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"

          LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”

          .. note::

            When you use this task setting with a source PostgreSQL database, a logical replication slot
            should already be created and associated with the source endpoint. You can verify this by
            setting the ``slotName`` extra connection attribute to the name of this logical replication
            slot. For more information, see `Extra Connection Attributes When Using PostgreSQL as a Source
            for AWS DMS
            <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`__
            .

        :type CdcStopPosition: string
        :param CdcStopPosition:

          Indicates when you want a change data capture (CDC) operation to stop. The value can be either
          server time or commit time.

          Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”

          Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12 “

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationTask': {
                    'ReplicationTaskIdentifier': 'string',
                    'SourceEndpointArn': 'string',
                    'TargetEndpointArn': 'string',
                    'ReplicationInstanceArn': 'string',
                    'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
                    'TableMappings': 'string',
                    'ReplicationTaskSettings': 'string',
                    'Status': 'string',
                    'LastFailureMessage': 'string',
                    'StopReason': 'string',
                    'ReplicationTaskCreationDate': datetime(2015, 1, 1),
                    'ReplicationTaskStartDate': datetime(2015, 1, 1),
                    'CdcStartPosition': 'string',
                    'CdcStopPosition': 'string',
                    'RecoveryCheckpoint': 'string',
                    'ReplicationTaskArn': 'string',
                    'ReplicationTaskStats': {
                        'FullLoadProgressPercent': 123,
                        'ElapsedTimeMillis': 123,
                        'TablesLoaded': 123,
                        'TablesLoading': 123,
                        'TablesQueued': 123,
                        'TablesErrored': 123,
                        'FreshStartDate': datetime(2015, 1, 1),
                        'StartDate': datetime(2015, 1, 1),
                        'StopDate': datetime(2015, 1, 1),
                        'FullLoadStartDate': datetime(2015, 1, 1),
                        'FullLoadFinishDate': datetime(2015, 1, 1)
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationTask** *(dict) --*

              The replication task started.

              - **ReplicationTaskIdentifier** *(string) --*

                The user-assigned replication task identifier or name.

                Constraints:

                * Must contain from 1 to 255 alphanumeric characters or hyphens.

                * First character must be a letter.

                * Cannot end with a hyphen or contain two consecutive hyphens.

              - **SourceEndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **TargetEndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **ReplicationInstanceArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication instance.

              - **MigrationType** *(string) --*

                The type of migration.

              - **TableMappings** *(string) --*

                Table mappings specified in the task.

              - **ReplicationTaskSettings** *(string) --*

                The settings for the replication task.

              - **Status** *(string) --*

                The status of the replication task.

              - **LastFailureMessage** *(string) --*

                The last error (failure) message generated for the replication instance.

              - **StopReason** *(string) --*

                The reason the replication task was stopped.

              - **ReplicationTaskCreationDate** *(datetime) --*

                The date the replication task was created.

              - **ReplicationTaskStartDate** *(datetime) --*

                The date the replication task is scheduled to start.

              - **CdcStartPosition** *(string) --*

                Indicates when you want a change data capture (CDC) operation to start. Use either
                ``CdcStartPosition`` or ``CdcStartTime`` to specify when you want the CDC operation to
                start. Specifying both values results in an error.

                The value can be in date, checkpoint, or LSN/SCN format.

                Date Example: --cdc-start-position “2018-03-08T12:12:12”

                Checkpoint Example: --cdc-start-position
                "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"
        "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"

                LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”

              - **CdcStopPosition** *(string) --*

                Indicates when you want a change data capture (CDC) operation to stop. The value can be
                either server time or commit time.

                Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”

                Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12 “

              - **RecoveryCheckpoint** *(string) --*

                Indicates the last checkpoint that occurred during a change data capture (CDC) operation.
                You can provide this value to the ``CdcStartPosition`` parameter to start a CDC operation
                that begins at that checkpoint.

              - **ReplicationTaskArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication task.

              - **ReplicationTaskStats** *(dict) --*

                The statistics for the task, including elapsed time, tables loaded, and table errors.

                - **FullLoadProgressPercent** *(integer) --*

                  The percent complete for the full load migration task.

                - **ElapsedTimeMillis** *(integer) --*

                  The elapsed time of the task, in milliseconds.

                - **TablesLoaded** *(integer) --*

                  The number of tables loaded for this task.

                - **TablesLoading** *(integer) --*

                  The number of tables currently loading for this task.

                - **TablesQueued** *(integer) --*

                  The number of tables queued for this task.

                - **TablesErrored** *(integer) --*

                  The number of errors that have occurred during this task.

                - **FreshStartDate** *(datetime) --*

                  The date the replication task was started either with a fresh start or a target reload.

                - **StartDate** *(datetime) --*

                  The date the replication task was started either with a fresh start or a resume. For more
                  information, see `StartReplicationTaskType
                  <https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html#DMS-StartReplicationTask-request-StartReplicationTaskType>`__
                  .

                - **StopDate** *(datetime) --*

                  The date the replication task was stopped.

                - **FullLoadStartDate** *(datetime) --*

                  The date the the replication task full load was started.

                - **FullLoadFinishDate** *(datetime) --*

                  The date the replication task full load was completed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def start_replication_task_assessment(
        self, ReplicationTaskArn: str
    ) -> Dict[str, Any]:
        """
        Starts the replication task assessment for unsupported data types in the source database.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/StartReplicationTaskAssessment>`_

        **Request Syntax**
        ::

          response = client.start_replication_task_assessment(
              ReplicationTaskArn='string'
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the replication task.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationTask': {
                    'ReplicationTaskIdentifier': 'string',
                    'SourceEndpointArn': 'string',
                    'TargetEndpointArn': 'string',
                    'ReplicationInstanceArn': 'string',
                    'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
                    'TableMappings': 'string',
                    'ReplicationTaskSettings': 'string',
                    'Status': 'string',
                    'LastFailureMessage': 'string',
                    'StopReason': 'string',
                    'ReplicationTaskCreationDate': datetime(2015, 1, 1),
                    'ReplicationTaskStartDate': datetime(2015, 1, 1),
                    'CdcStartPosition': 'string',
                    'CdcStopPosition': 'string',
                    'RecoveryCheckpoint': 'string',
                    'ReplicationTaskArn': 'string',
                    'ReplicationTaskStats': {
                        'FullLoadProgressPercent': 123,
                        'ElapsedTimeMillis': 123,
                        'TablesLoaded': 123,
                        'TablesLoading': 123,
                        'TablesQueued': 123,
                        'TablesErrored': 123,
                        'FreshStartDate': datetime(2015, 1, 1),
                        'StartDate': datetime(2015, 1, 1),
                        'StopDate': datetime(2015, 1, 1),
                        'FullLoadStartDate': datetime(2015, 1, 1),
                        'FullLoadFinishDate': datetime(2015, 1, 1)
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationTask** *(dict) --*

              The assessed replication task.

              - **ReplicationTaskIdentifier** *(string) --*

                The user-assigned replication task identifier or name.

                Constraints:

                * Must contain from 1 to 255 alphanumeric characters or hyphens.

                * First character must be a letter.

                * Cannot end with a hyphen or contain two consecutive hyphens.

              - **SourceEndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **TargetEndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **ReplicationInstanceArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication instance.

              - **MigrationType** *(string) --*

                The type of migration.

              - **TableMappings** *(string) --*

                Table mappings specified in the task.

              - **ReplicationTaskSettings** *(string) --*

                The settings for the replication task.

              - **Status** *(string) --*

                The status of the replication task.

              - **LastFailureMessage** *(string) --*

                The last error (failure) message generated for the replication instance.

              - **StopReason** *(string) --*

                The reason the replication task was stopped.

              - **ReplicationTaskCreationDate** *(datetime) --*

                The date the replication task was created.

              - **ReplicationTaskStartDate** *(datetime) --*

                The date the replication task is scheduled to start.

              - **CdcStartPosition** *(string) --*

                Indicates when you want a change data capture (CDC) operation to start. Use either
                ``CdcStartPosition`` or ``CdcStartTime`` to specify when you want the CDC operation to
                start. Specifying both values results in an error.

                The value can be in date, checkpoint, or LSN/SCN format.

                Date Example: --cdc-start-position “2018-03-08T12:12:12”

                Checkpoint Example: --cdc-start-position
                "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"
        "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"

                LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”

              - **CdcStopPosition** *(string) --*

                Indicates when you want a change data capture (CDC) operation to stop. The value can be
                either server time or commit time.

                Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”

                Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12 “

              - **RecoveryCheckpoint** *(string) --*

                Indicates the last checkpoint that occurred during a change data capture (CDC) operation.
                You can provide this value to the ``CdcStartPosition`` parameter to start a CDC operation
                that begins at that checkpoint.

              - **ReplicationTaskArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication task.

              - **ReplicationTaskStats** *(dict) --*

                The statistics for the task, including elapsed time, tables loaded, and table errors.

                - **FullLoadProgressPercent** *(integer) --*

                  The percent complete for the full load migration task.

                - **ElapsedTimeMillis** *(integer) --*

                  The elapsed time of the task, in milliseconds.

                - **TablesLoaded** *(integer) --*

                  The number of tables loaded for this task.

                - **TablesLoading** *(integer) --*

                  The number of tables currently loading for this task.

                - **TablesQueued** *(integer) --*

                  The number of tables queued for this task.

                - **TablesErrored** *(integer) --*

                  The number of errors that have occurred during this task.

                - **FreshStartDate** *(datetime) --*

                  The date the replication task was started either with a fresh start or a target reload.

                - **StartDate** *(datetime) --*

                  The date the replication task was started either with a fresh start or a resume. For more
                  information, see `StartReplicationTaskType
                  <https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html#DMS-StartReplicationTask-request-StartReplicationTaskType>`__
                  .

                - **StopDate** *(datetime) --*

                  The date the replication task was stopped.

                - **FullLoadStartDate** *(datetime) --*

                  The date the the replication task full load was started.

                - **FullLoadFinishDate** *(datetime) --*

                  The date the replication task full load was completed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def stop_replication_task(self, ReplicationTaskArn: str) -> Dict[str, Any]:
        """
        Stops the replication task.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/StopReplicationTask>`_

        **Request Syntax**
        ::

          response = client.stop_replication_task(
              ReplicationTaskArn='string'
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn: **[REQUIRED]**

          The Amazon Resource Name(ARN) of the replication task to be stopped.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReplicationTask': {
                    'ReplicationTaskIdentifier': 'string',
                    'SourceEndpointArn': 'string',
                    'TargetEndpointArn': 'string',
                    'ReplicationInstanceArn': 'string',
                    'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
                    'TableMappings': 'string',
                    'ReplicationTaskSettings': 'string',
                    'Status': 'string',
                    'LastFailureMessage': 'string',
                    'StopReason': 'string',
                    'ReplicationTaskCreationDate': datetime(2015, 1, 1),
                    'ReplicationTaskStartDate': datetime(2015, 1, 1),
                    'CdcStartPosition': 'string',
                    'CdcStopPosition': 'string',
                    'RecoveryCheckpoint': 'string',
                    'ReplicationTaskArn': 'string',
                    'ReplicationTaskStats': {
                        'FullLoadProgressPercent': 123,
                        'ElapsedTimeMillis': 123,
                        'TablesLoaded': 123,
                        'TablesLoading': 123,
                        'TablesQueued': 123,
                        'TablesErrored': 123,
                        'FreshStartDate': datetime(2015, 1, 1),
                        'StartDate': datetime(2015, 1, 1),
                        'StopDate': datetime(2015, 1, 1),
                        'FullLoadStartDate': datetime(2015, 1, 1),
                        'FullLoadFinishDate': datetime(2015, 1, 1)
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationTask** *(dict) --*

              The replication task stopped.

              - **ReplicationTaskIdentifier** *(string) --*

                The user-assigned replication task identifier or name.

                Constraints:

                * Must contain from 1 to 255 alphanumeric characters or hyphens.

                * First character must be a letter.

                * Cannot end with a hyphen or contain two consecutive hyphens.

              - **SourceEndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **TargetEndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **ReplicationInstanceArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication instance.

              - **MigrationType** *(string) --*

                The type of migration.

              - **TableMappings** *(string) --*

                Table mappings specified in the task.

              - **ReplicationTaskSettings** *(string) --*

                The settings for the replication task.

              - **Status** *(string) --*

                The status of the replication task.

              - **LastFailureMessage** *(string) --*

                The last error (failure) message generated for the replication instance.

              - **StopReason** *(string) --*

                The reason the replication task was stopped.

              - **ReplicationTaskCreationDate** *(datetime) --*

                The date the replication task was created.

              - **ReplicationTaskStartDate** *(datetime) --*

                The date the replication task is scheduled to start.

              - **CdcStartPosition** *(string) --*

                Indicates when you want a change data capture (CDC) operation to start. Use either
                ``CdcStartPosition`` or ``CdcStartTime`` to specify when you want the CDC operation to
                start. Specifying both values results in an error.

                The value can be in date, checkpoint, or LSN/SCN format.

                Date Example: --cdc-start-position “2018-03-08T12:12:12”

                Checkpoint Example: --cdc-start-position
                "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"
        "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"

                LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”

              - **CdcStopPosition** *(string) --*

                Indicates when you want a change data capture (CDC) operation to stop. The value can be
                either server time or commit time.

                Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”

                Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12 “

              - **RecoveryCheckpoint** *(string) --*

                Indicates the last checkpoint that occurred during a change data capture (CDC) operation.
                You can provide this value to the ``CdcStartPosition`` parameter to start a CDC operation
                that begins at that checkpoint.

              - **ReplicationTaskArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication task.

              - **ReplicationTaskStats** *(dict) --*

                The statistics for the task, including elapsed time, tables loaded, and table errors.

                - **FullLoadProgressPercent** *(integer) --*

                  The percent complete for the full load migration task.

                - **ElapsedTimeMillis** *(integer) --*

                  The elapsed time of the task, in milliseconds.

                - **TablesLoaded** *(integer) --*

                  The number of tables loaded for this task.

                - **TablesLoading** *(integer) --*

                  The number of tables currently loading for this task.

                - **TablesQueued** *(integer) --*

                  The number of tables queued for this task.

                - **TablesErrored** *(integer) --*

                  The number of errors that have occurred during this task.

                - **FreshStartDate** *(datetime) --*

                  The date the replication task was started either with a fresh start or a target reload.

                - **StartDate** *(datetime) --*

                  The date the replication task was started either with a fresh start or a resume. For more
                  information, see `StartReplicationTaskType
                  <https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html#DMS-StartReplicationTask-request-StartReplicationTaskType>`__
                  .

                - **StopDate** *(datetime) --*

                  The date the replication task was stopped.

                - **FullLoadStartDate** *(datetime) --*

                  The date the the replication task full load was started.

                - **FullLoadFinishDate** *(datetime) --*

                  The date the replication task full load was completed.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def test_connection(
        self, ReplicationInstanceArn: str, EndpointArn: str
    ) -> ClientTestConnectionResponseTypeDef:
        """
        Tests the connection between the replication instance and the endpoint.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/TestConnection>`_

        **Request Syntax**
        ::

          response = client.test_connection(
              ReplicationInstanceArn='string',
              EndpointArn='string'
          )
        :type ReplicationInstanceArn: string
        :param ReplicationInstanceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the replication instance.

        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Connection': {
                    'ReplicationInstanceArn': 'string',
                    'EndpointArn': 'string',
                    'Status': 'string',
                    'LastFailureMessage': 'string',
                    'EndpointIdentifier': 'string',
                    'ReplicationInstanceIdentifier': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Connection** *(dict) --*

              The connection tested.

              - **ReplicationInstanceArn** *(string) --*

                The Amazon Resource Name (ARN) of the replication instance.

              - **EndpointArn** *(string) --*

                The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

              - **Status** *(string) --*

                The connection status.

              - **LastFailureMessage** *(string) --*

                The error message when the connection last failed.

              - **EndpointIdentifier** *(string) --*

                The identifier of the endpoint. Identifiers must begin with a letter; must contain only
                ASCII letters, digits, and hyphens; and must not end with a hyphen or contain two
                consecutive hyphens.

              - **ReplicationInstanceIdentifier** *(string) --*

                The replication instance identifier. This parameter is stored as a lowercase string.

        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_certificates"]
    ) -> paginator_scope.DescribeCertificatesPaginator:
        """
        Get Paginator for `describe_certificates` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_connections"]
    ) -> paginator_scope.DescribeConnectionsPaginator:
        """
        Get Paginator for `describe_connections` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_endpoint_types"]
    ) -> paginator_scope.DescribeEndpointTypesPaginator:
        """
        Get Paginator for `describe_endpoint_types` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_endpoints"]
    ) -> paginator_scope.DescribeEndpointsPaginator:
        """
        Get Paginator for `describe_endpoints` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> paginator_scope.DescribeEventSubscriptionsPaginator:
        """
        Get Paginator for `describe_event_subscriptions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_events"]
    ) -> paginator_scope.DescribeEventsPaginator:
        """
        Get Paginator for `describe_events` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_orderable_replication_instances"]
    ) -> paginator_scope.DescribeOrderableReplicationInstancesPaginator:
        """
        Get Paginator for `describe_orderable_replication_instances` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_replication_instances"]
    ) -> paginator_scope.DescribeReplicationInstancesPaginator:
        """
        Get Paginator for `describe_replication_instances` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_replication_subnet_groups"]
    ) -> paginator_scope.DescribeReplicationSubnetGroupsPaginator:
        """
        Get Paginator for `describe_replication_subnet_groups` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_replication_task_assessment_results"]
    ) -> paginator_scope.DescribeReplicationTaskAssessmentResultsPaginator:
        """
        Get Paginator for `describe_replication_task_assessment_results` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_replication_tasks"]
    ) -> paginator_scope.DescribeReplicationTasksPaginator:
        """
        Get Paginator for `describe_replication_tasks` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_schemas"]
    ) -> paginator_scope.DescribeSchemasPaginator:
        """
        Get Paginator for `describe_schemas` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_table_statistics"]
    ) -> paginator_scope.DescribeTableStatisticsPaginator:
        """
        Get Paginator for `describe_table_statistics` operation.
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

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["endpoint_deleted"]
    ) -> waiter_scope.EndpointDeletedWaiter:
        """
        Get Waiter `endpoint_deleted`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["replication_instance_available"]
    ) -> waiter_scope.ReplicationInstanceAvailableWaiter:
        """
        Get Waiter `replication_instance_available`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["replication_instance_deleted"]
    ) -> waiter_scope.ReplicationInstanceDeletedWaiter:
        """
        Get Waiter `replication_instance_deleted`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["replication_task_deleted"]
    ) -> waiter_scope.ReplicationTaskDeletedWaiter:
        """
        Get Waiter `replication_task_deleted`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["replication_task_ready"]
    ) -> waiter_scope.ReplicationTaskReadyWaiter:
        """
        Get Waiter `replication_task_ready`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["replication_task_running"]
    ) -> waiter_scope.ReplicationTaskRunningWaiter:
        """
        Get Waiter `replication_task_running`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["replication_task_stopped"]
    ) -> waiter_scope.ReplicationTaskStoppedWaiter:
        """
        Get Waiter `replication_task_stopped`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["test_connection_succeeds"]
    ) -> waiter_scope.TestConnectionSucceedsWaiter:
        """
        Get Waiter `test_connection_succeeds`.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        """
        Returns an object that can wait for some condition.

        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.

        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """


class Exceptions:
    AccessDeniedFault: Boto3ClientError
    ClientError: Boto3ClientError
    InsufficientResourceCapacityFault: Boto3ClientError
    InvalidCertificateFault: Boto3ClientError
    InvalidResourceStateFault: Boto3ClientError
    InvalidSubnet: Boto3ClientError
    KMSAccessDeniedFault: Boto3ClientError
    KMSDisabledFault: Boto3ClientError
    KMSInvalidStateFault: Boto3ClientError
    KMSKeyNotAccessibleFault: Boto3ClientError
    KMSNotFoundFault: Boto3ClientError
    KMSThrottlingFault: Boto3ClientError
    ReplicationSubnetGroupDoesNotCoverEnoughAZs: Boto3ClientError
    ResourceAlreadyExistsFault: Boto3ClientError
    ResourceNotFoundFault: Boto3ClientError
    ResourceQuotaExceededFault: Boto3ClientError
    SNSInvalidTopicFault: Boto3ClientError
    SNSNoAuthorizationFault: Boto3ClientError
    StorageQuotaExceededFault: Boto3ClientError
    SubnetAlreadyInUse: Boto3ClientError
    UpgradeDependencyFailureFault: Boto3ClientError

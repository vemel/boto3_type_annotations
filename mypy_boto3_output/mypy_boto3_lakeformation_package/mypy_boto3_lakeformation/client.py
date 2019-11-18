"Main interface for lakeformation Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_lakeformation.client as client_scope
from mypy_boto3_lakeformation.type_defs import (
    ClientBatchGrantPermissionsEntriesTypeDef,
    ClientBatchGrantPermissionsResponseTypeDef,
    ClientBatchRevokePermissionsEntriesTypeDef,
    ClientBatchRevokePermissionsResponseTypeDef,
    ClientDescribeResourceResponseTypeDef,
    ClientGetDataLakeSettingsResponseTypeDef,
    ClientGetEffectivePermissionsForPathResponseTypeDef,
    ClientGrantPermissionsPrincipalTypeDef,
    ClientGrantPermissionsResourceTypeDef,
    ClientListPermissionsPrincipalTypeDef,
    ClientListPermissionsResourceTypeDef,
    ClientListPermissionsResponseTypeDef,
    ClientListResourcesFilterConditionListTypeDef,
    ClientListResourcesResponseTypeDef,
    ClientPutDataLakeSettingsDataLakeSettingsTypeDef,
    ClientRevokePermissionsPrincipalTypeDef,
    ClientRevokePermissionsResourceTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_grant_permissions(
        self,
        Entries: List[ClientBatchGrantPermissionsEntriesTypeDef],
        CatalogId: str = None,
    ) -> ClientBatchGrantPermissionsResponseTypeDef:
        """
        Batch operation to grant permissions to the principal.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lakeformation-2017-03-31/BatchGrantPermissions>`_

        **Request Syntax**
        ::

          response = client.batch_grant_permissions(
              CatalogId='string',
              Entries=[
                  {
                      'Id': 'string',
                      'Principal': {
                          'DataLakePrincipalIdentifier': 'string'
                      },
                      'Resource': {
                          'Catalog': {}
                          ,
                          'Database': {
                              'Name': 'string'
                          },
                          'Table': {
                              'DatabaseName': 'string',
                              'Name': 'string'
                          },
                          'TableWithColumns': {
                              'DatabaseName': 'string',
                              'Name': 'string',
                              'ColumnNames': [
                                  'string',
                              ],
                              'ColumnWildcard': {
                                  'ExcludedColumnNames': [
                                      'string',
                                  ]
                              }
                          },
                          'DataLocation': {
                              'ResourceArn': 'string'
                          }
                      },
                      'Permissions': [
                          'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'
                          |'DATA_LOCATION_ACCESS',
                      ],
                      'PermissionsWithGrantOption': [
                          'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'
                          |'DATA_LOCATION_ACCESS',
                      ]
                  },
              ]
          )
        :type CatalogId: string
        :param CatalogId:

          The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
          persistent metadata store. It contains database definitions, table definitions, and other control
          information to manage your AWS Lake Formation environment.

        :type Entries: list
        :param Entries: **[REQUIRED]**

          A list of up to 20 entries for resource permissions to be granted by batch operation to the
          principal.

          - *(dict) --*

            A permission to a resource granted by batch operation to the principal.

            - **Id** *(string) --* **[REQUIRED]**

              A unique identifier for the batch permissions request entry.

            - **Principal** *(dict) --*

              The principal to be granted a permission.

              - **DataLakePrincipalIdentifier** *(string) --*

                An identifier for the AWS Lake Formation principal.

            - **Resource** *(dict) --*

              The resource to which the principal is to be granted a permission.

              - **Catalog** *(dict) --*

                The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
                persistent metadata store. It contains database definitions, table definitions, and other
                control information to manage your AWS Lake Formation environment.

              - **Database** *(dict) --*

                The database for the resource. Unique to the Data Catalog. A database is a set of
                associated table definitions organized into a logical group. You can Grant and Revoke
                database permissions to a principal.

                - **Name** *(string) --* **[REQUIRED]**

                  The name of the database resource. Unique to the Data Catalog.

              - **Table** *(dict) --*

                The table for the resource. A table is a metadata definition that represents your data. You
                can Grant and Revoke table privileges to a principal.

                - **DatabaseName** *(string) --* **[REQUIRED]**

                  The name of the database for the table. Unique to a Data Catalog. A database is a set of
                  associated table definitions organized into a logical group. You can Grant and Revoke
                  database privileges to a principal.

                - **Name** *(string) --* **[REQUIRED]**

                  The name of the table.

              - **TableWithColumns** *(dict) --*

                The table with columns for the resource. A principal with permissions to this resource can
                select metadata from the columns of a table in the Data Catalog and the underlying data in
                Amazon S3.

                - **DatabaseName** *(string) --*

                  The name of the database for the table with columns resource. Unique to the Data Catalog.
                  A database is a set of associated table definitions organized into a logical group. You
                  can Grant and Revoke database privileges to a principal.

                - **Name** *(string) --*

                  The name of the table resource. A table is a metadata definition that represents your
                  data. You can Grant and Revoke table privileges to a principal.

                - **ColumnNames** *(list) --*

                  The list of column names for the table. At least one of ``ColumnNames`` or
                  ``ColumnWildcard`` is required.

                  - *(string) --*

                - **ColumnWildcard** *(dict) --*

                  A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
                  ``ColumnWildcard`` is required.

                  - **ExcludedColumnNames** *(list) --*

                    Excludes column names. Any column with this name will be excluded.

                    - *(string) --*

              - **DataLocation** *(dict) --*

                The location of an Amazon S3 path where permissions are granted or revoked.

                - **ResourceArn** *(string) --* **[REQUIRED]**

                  The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

            - **Permissions** *(list) --*

              The permissions to be granted.

              - *(string) --*

            - **PermissionsWithGrantOption** *(list) --*

              Indicates if the option to pass permissions is granted.

              - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Failures': [
                    {
                        'RequestEntry': {
                            'Id': 'string',
                            'Principal': {
                                'DataLakePrincipalIdentifier': 'string'
                            },
                            'Resource': {
                                'Catalog': {},
                                'Database': {
                                    'Name': 'string'
                                },
                                'Table': {
                                    'DatabaseName': 'string',
                                    'Name': 'string'
                                },
                                'TableWithColumns': {
                                    'DatabaseName': 'string',
                                    'Name': 'string',
                                    'ColumnNames': [
                                        'string',
                                    ],
                                    'ColumnWildcard': {
                                        'ExcludedColumnNames': [
                                            'string',
                                        ]
                                    }
                                },
                                'DataLocation': {
                                    'ResourceArn': 'string'
                                }
                            },
                            'Permissions': [
                                'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'
                                |'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                            ],
                            'PermissionsWithGrantOption': [
                                'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'
                                |'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                            ]
                        },
                        'Error': {
                            'ErrorCode': 'string',
                            'ErrorMessage': 'string'
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Failures** *(list) --*

              A list of failures to grant permissions to the resources.

              - *(dict) --*

                A list of failures when performing a batch grant or batch revoke operation.

                - **RequestEntry** *(dict) --*

                  An identifier for an entry of the batch request.

                  - **Id** *(string) --*

                    A unique identifier for the batch permissions request entry.

                  - **Principal** *(dict) --*

                    The principal to be granted a permission.

                    - **DataLakePrincipalIdentifier** *(string) --*

                      An identifier for the AWS Lake Formation principal.

                  - **Resource** *(dict) --*

                    The resource to which the principal is to be granted a permission.

                    - **Catalog** *(dict) --*

                      The identifier for the Data Catalog. By default, the account ID. The Data Catalog is
                      the persistent metadata store. It contains database definitions, table definitions,
                      and other control information to manage your AWS Lake Formation environment.

                    - **Database** *(dict) --*

                      The database for the resource. Unique to the Data Catalog. A database is a set of
                      associated table definitions organized into a logical group. You can Grant and Revoke
                      database permissions to a principal.

                      - **Name** *(string) --*

                        The name of the database resource. Unique to the Data Catalog.

                    - **Table** *(dict) --*

                      The table for the resource. A table is a metadata definition that represents your
                      data. You can Grant and Revoke table privileges to a principal.

                      - **DatabaseName** *(string) --*

                        The name of the database for the table. Unique to a Data Catalog. A database is a
                        set of associated table definitions organized into a logical group. You can Grant
                        and Revoke database privileges to a principal.

                      - **Name** *(string) --*

                        The name of the table.

                    - **TableWithColumns** *(dict) --*

                      The table with columns for the resource. A principal with permissions to this
                      resource can select metadata from the columns of a table in the Data Catalog and the
                      underlying data in Amazon S3.

                      - **DatabaseName** *(string) --*

                        The name of the database for the table with columns resource. Unique to the Data
                        Catalog. A database is a set of associated table definitions organized into a
                        logical group. You can Grant and Revoke database privileges to a principal.

                      - **Name** *(string) --*

                        The name of the table resource. A table is a metadata definition that represents
                        your data. You can Grant and Revoke table privileges to a principal.

                      - **ColumnNames** *(list) --*

                        The list of column names for the table. At least one of ``ColumnNames`` or
                        ``ColumnWildcard`` is required.

                        - *(string) --*

                      - **ColumnWildcard** *(dict) --*

                        A wildcard specified by a ``ColumnWildcard`` object. At least one of
                        ``ColumnNames`` or ``ColumnWildcard`` is required.

                        - **ExcludedColumnNames** *(list) --*

                          Excludes column names. Any column with this name will be excluded.

                          - *(string) --*

                    - **DataLocation** *(dict) --*

                      The location of an Amazon S3 path where permissions are granted or revoked.

                      - **ResourceArn** *(string) --*

                        The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

                  - **Permissions** *(list) --*

                    The permissions to be granted.

                    - *(string) --*

                  - **PermissionsWithGrantOption** *(list) --*

                    Indicates if the option to pass permissions is granted.

                    - *(string) --*

                - **Error** *(dict) --*

                  An error message that applies to the failure of the entry.

                  - **ErrorCode** *(string) --*

                    The code associated with this error.

                  - **ErrorMessage** *(string) --*

                    A message describing the error.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_revoke_permissions(
        self,
        Entries: List[ClientBatchRevokePermissionsEntriesTypeDef],
        CatalogId: str = None,
    ) -> ClientBatchRevokePermissionsResponseTypeDef:
        """
        Batch operation to revoke permissions from the principal.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lakeformation-2017-03-31/BatchRevokePermissions>`_

        **Request Syntax**
        ::

          response = client.batch_revoke_permissions(
              CatalogId='string',
              Entries=[
                  {
                      'Id': 'string',
                      'Principal': {
                          'DataLakePrincipalIdentifier': 'string'
                      },
                      'Resource': {
                          'Catalog': {}
                          ,
                          'Database': {
                              'Name': 'string'
                          },
                          'Table': {
                              'DatabaseName': 'string',
                              'Name': 'string'
                          },
                          'TableWithColumns': {
                              'DatabaseName': 'string',
                              'Name': 'string',
                              'ColumnNames': [
                                  'string',
                              ],
                              'ColumnWildcard': {
                                  'ExcludedColumnNames': [
                                      'string',
                                  ]
                              }
                          },
                          'DataLocation': {
                              'ResourceArn': 'string'
                          }
                      },
                      'Permissions': [
                          'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'
                          |'DATA_LOCATION_ACCESS',
                      ],
                      'PermissionsWithGrantOption': [
                          'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'
                          |'DATA_LOCATION_ACCESS',
                      ]
                  },
              ]
          )
        :type CatalogId: string
        :param CatalogId:

          The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
          persistent metadata store. It contains database definitions, table definitions, and other control
          information to manage your AWS Lake Formation environment.

        :type Entries: list
        :param Entries: **[REQUIRED]**

          A list of up to 20 entries for resource permissions to be revoked by batch operation to the
          principal.

          - *(dict) --*

            A permission to a resource granted by batch operation to the principal.

            - **Id** *(string) --* **[REQUIRED]**

              A unique identifier for the batch permissions request entry.

            - **Principal** *(dict) --*

              The principal to be granted a permission.

              - **DataLakePrincipalIdentifier** *(string) --*

                An identifier for the AWS Lake Formation principal.

            - **Resource** *(dict) --*

              The resource to which the principal is to be granted a permission.

              - **Catalog** *(dict) --*

                The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
                persistent metadata store. It contains database definitions, table definitions, and other
                control information to manage your AWS Lake Formation environment.

              - **Database** *(dict) --*

                The database for the resource. Unique to the Data Catalog. A database is a set of
                associated table definitions organized into a logical group. You can Grant and Revoke
                database permissions to a principal.

                - **Name** *(string) --* **[REQUIRED]**

                  The name of the database resource. Unique to the Data Catalog.

              - **Table** *(dict) --*

                The table for the resource. A table is a metadata definition that represents your data. You
                can Grant and Revoke table privileges to a principal.

                - **DatabaseName** *(string) --* **[REQUIRED]**

                  The name of the database for the table. Unique to a Data Catalog. A database is a set of
                  associated table definitions organized into a logical group. You can Grant and Revoke
                  database privileges to a principal.

                - **Name** *(string) --* **[REQUIRED]**

                  The name of the table.

              - **TableWithColumns** *(dict) --*

                The table with columns for the resource. A principal with permissions to this resource can
                select metadata from the columns of a table in the Data Catalog and the underlying data in
                Amazon S3.

                - **DatabaseName** *(string) --*

                  The name of the database for the table with columns resource. Unique to the Data Catalog.
                  A database is a set of associated table definitions organized into a logical group. You
                  can Grant and Revoke database privileges to a principal.

                - **Name** *(string) --*

                  The name of the table resource. A table is a metadata definition that represents your
                  data. You can Grant and Revoke table privileges to a principal.

                - **ColumnNames** *(list) --*

                  The list of column names for the table. At least one of ``ColumnNames`` or
                  ``ColumnWildcard`` is required.

                  - *(string) --*

                - **ColumnWildcard** *(dict) --*

                  A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
                  ``ColumnWildcard`` is required.

                  - **ExcludedColumnNames** *(list) --*

                    Excludes column names. Any column with this name will be excluded.

                    - *(string) --*

              - **DataLocation** *(dict) --*

                The location of an Amazon S3 path where permissions are granted or revoked.

                - **ResourceArn** *(string) --* **[REQUIRED]**

                  The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

            - **Permissions** *(list) --*

              The permissions to be granted.

              - *(string) --*

            - **PermissionsWithGrantOption** *(list) --*

              Indicates if the option to pass permissions is granted.

              - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Failures': [
                    {
                        'RequestEntry': {
                            'Id': 'string',
                            'Principal': {
                                'DataLakePrincipalIdentifier': 'string'
                            },
                            'Resource': {
                                'Catalog': {},
                                'Database': {
                                    'Name': 'string'
                                },
                                'Table': {
                                    'DatabaseName': 'string',
                                    'Name': 'string'
                                },
                                'TableWithColumns': {
                                    'DatabaseName': 'string',
                                    'Name': 'string',
                                    'ColumnNames': [
                                        'string',
                                    ],
                                    'ColumnWildcard': {
                                        'ExcludedColumnNames': [
                                            'string',
                                        ]
                                    }
                                },
                                'DataLocation': {
                                    'ResourceArn': 'string'
                                }
                            },
                            'Permissions': [
                                'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'
                                |'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                            ],
                            'PermissionsWithGrantOption': [
                                'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'
                                |'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                            ]
                        },
                        'Error': {
                            'ErrorCode': 'string',
                            'ErrorMessage': 'string'
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Failures** *(list) --*

              A list of failures to revoke permissions to the resources.

              - *(dict) --*

                A list of failures when performing a batch grant or batch revoke operation.

                - **RequestEntry** *(dict) --*

                  An identifier for an entry of the batch request.

                  - **Id** *(string) --*

                    A unique identifier for the batch permissions request entry.

                  - **Principal** *(dict) --*

                    The principal to be granted a permission.

                    - **DataLakePrincipalIdentifier** *(string) --*

                      An identifier for the AWS Lake Formation principal.

                  - **Resource** *(dict) --*

                    The resource to which the principal is to be granted a permission.

                    - **Catalog** *(dict) --*

                      The identifier for the Data Catalog. By default, the account ID. The Data Catalog is
                      the persistent metadata store. It contains database definitions, table definitions,
                      and other control information to manage your AWS Lake Formation environment.

                    - **Database** *(dict) --*

                      The database for the resource. Unique to the Data Catalog. A database is a set of
                      associated table definitions organized into a logical group. You can Grant and Revoke
                      database permissions to a principal.

                      - **Name** *(string) --*

                        The name of the database resource. Unique to the Data Catalog.

                    - **Table** *(dict) --*

                      The table for the resource. A table is a metadata definition that represents your
                      data. You can Grant and Revoke table privileges to a principal.

                      - **DatabaseName** *(string) --*

                        The name of the database for the table. Unique to a Data Catalog. A database is a
                        set of associated table definitions organized into a logical group. You can Grant
                        and Revoke database privileges to a principal.

                      - **Name** *(string) --*

                        The name of the table.

                    - **TableWithColumns** *(dict) --*

                      The table with columns for the resource. A principal with permissions to this
                      resource can select metadata from the columns of a table in the Data Catalog and the
                      underlying data in Amazon S3.

                      - **DatabaseName** *(string) --*

                        The name of the database for the table with columns resource. Unique to the Data
                        Catalog. A database is a set of associated table definitions organized into a
                        logical group. You can Grant and Revoke database privileges to a principal.

                      - **Name** *(string) --*

                        The name of the table resource. A table is a metadata definition that represents
                        your data. You can Grant and Revoke table privileges to a principal.

                      - **ColumnNames** *(list) --*

                        The list of column names for the table. At least one of ``ColumnNames`` or
                        ``ColumnWildcard`` is required.

                        - *(string) --*

                      - **ColumnWildcard** *(dict) --*

                        A wildcard specified by a ``ColumnWildcard`` object. At least one of
                        ``ColumnNames`` or ``ColumnWildcard`` is required.

                        - **ExcludedColumnNames** *(list) --*

                          Excludes column names. Any column with this name will be excluded.

                          - *(string) --*

                    - **DataLocation** *(dict) --*

                      The location of an Amazon S3 path where permissions are granted or revoked.

                      - **ResourceArn** *(string) --*

                        The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

                  - **Permissions** *(list) --*

                    The permissions to be granted.

                    - *(string) --*

                  - **PermissionsWithGrantOption** *(list) --*

                    Indicates if the option to pass permissions is granted.

                    - *(string) --*

                - **Error** *(dict) --*

                  An error message that applies to the failure of the entry.

                  - **ErrorCode** *(string) --*

                    The code associated with this error.

                  - **ErrorMessage** *(string) --*

                    A message describing the error.

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
    def deregister_resource(self, ResourceArn: str) -> Dict[str, Any]:
        """
        Deregisters the resource as managed by the Data Catalog.

        When you deregister a path, Lake Formation removes the path from the inline policy attached to your
        service-linked role.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lakeformation-2017-03-31/DeregisterResource>`_

        **Request Syntax**
        ::

          response = client.deregister_resource(
              ResourceArn='string'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource that you want to deregister.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_resource(
        self, ResourceArn: str
    ) -> ClientDescribeResourceResponseTypeDef:
        """
        Retrieves the current data access role for the given resource registered in AWS Lake Formation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lakeformation-2017-03-31/DescribeResource>`_

        **Request Syntax**
        ::

          response = client.describe_resource(
              ResourceArn='string'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The resource ARN.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResourceInfo': {
                    'ResourceArn': 'string',
                    'RoleArn': 'string',
                    'LastModified': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **ResourceInfo** *(dict) --*

              A structure containing information about an AWS Lake Formation resource.

              - **ResourceArn** *(string) --*

                The Amazon Resource Name (ARN) of the resource.

              - **RoleArn** *(string) --*

                The IAM role that registered a resource.

              - **LastModified** *(datetime) --*

                The date and time the resource was last modified.

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
    def get_data_lake_settings(
        self, CatalogId: str = None
    ) -> ClientGetDataLakeSettingsResponseTypeDef:
        """
        The AWS Lake Formation principal.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lakeformation-2017-03-31/GetDataLakeSettings>`_

        **Request Syntax**
        ::

          response = client.get_data_lake_settings(
              CatalogId='string'
          )
        :type CatalogId: string
        :param CatalogId:

          The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
          persistent metadata store. It contains database definitions, table definitions, and other control
          information to manage your AWS Lake Formation environment.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DataLakeSettings': {
                    'DataLakeAdmins': [
                        {
                            'DataLakePrincipalIdentifier': 'string'
                        },
                    ],
                    'CreateDatabaseDefaultPermissions': [
                        {
                            'Principal': {
                                'DataLakePrincipalIdentifier': 'string'
                            },
                            'Permissions': [
                                'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'
                                |'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                            ]
                        },
                    ],
                    'CreateTableDefaultPermissions': [
                        {
                            'Principal': {
                                'DataLakePrincipalIdentifier': 'string'
                            },
                            'Permissions': [
                                'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'
                                |'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                            ]
                        },
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **DataLakeSettings** *(dict) --*

              A list of AWS Lake Formation principals.

              - **DataLakeAdmins** *(list) --*

                A list of AWS Lake Formation principals.

                - *(dict) --*

                  The AWS Lake Formation principal.

                  - **DataLakePrincipalIdentifier** *(string) --*

                    An identifier for the AWS Lake Formation principal.

              - **CreateDatabaseDefaultPermissions** *(list) --*

                A list of up to three principal permissions entries for default create database permissions.

                - *(dict) --*

                  Permissions granted to a principal.

                  - **Principal** *(dict) --*

                    The principal who is granted permissions.

                    - **DataLakePrincipalIdentifier** *(string) --*

                      An identifier for the AWS Lake Formation principal.

                  - **Permissions** *(list) --*

                    The permissions that are granted to the principal.

                    - *(string) --*

              - **CreateTableDefaultPermissions** *(list) --*

                A list of up to three principal permissions entries for default create table permissions.

                - *(dict) --*

                  Permissions granted to a principal.

                  - **Principal** *(dict) --*

                    The principal who is granted permissions.

                    - **DataLakePrincipalIdentifier** *(string) --*

                      An identifier for the AWS Lake Formation principal.

                  - **Permissions** *(list) --*

                    The permissions that are granted to the principal.

                    - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_effective_permissions_for_path(
        self,
        ResourceArn: str,
        CatalogId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientGetEffectivePermissionsForPathResponseTypeDef:
        """
        Returns the permissions for a specified table or database resource located at a path in Amazon S3.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lakeformation-2017-03-31/GetEffectivePermissionsForPath>`_

        **Request Syntax**
        ::

          response = client.get_effective_permissions_for_path(
              CatalogId='string',
              ResourceArn='string',
              NextToken='string',
              MaxResults=123
          )
        :type CatalogId: string
        :param CatalogId:

          The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
          persistent metadata store. It contains database definitions, table definitions, and other control
          information to manage your AWS Lake Formation environment.

        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource for which you want to get permissions.

        :type NextToken: string
        :param NextToken:

          A continuation token, if this is not the first call to retrieve this list.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Permissions': [
                    {
                        'Principal': {
                            'DataLakePrincipalIdentifier': 'string'
                        },
                        'Resource': {
                            'Catalog': {},
                            'Database': {
                                'Name': 'string'
                            },
                            'Table': {
                                'DatabaseName': 'string',
                                'Name': 'string'
                            },
                            'TableWithColumns': {
                                'DatabaseName': 'string',
                                'Name': 'string',
                                'ColumnNames': [
                                    'string',
                                ],
                                'ColumnWildcard': {
                                    'ExcludedColumnNames': [
                                        'string',
                                    ]
                                }
                            },
                            'DataLocation': {
                                'ResourceArn': 'string'
                            }
                        },
                        'Permissions': [
                            'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'
                            |'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                        ],
                        'PermissionsWithGrantOption': [
                            'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'
                            |'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                        ]
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Permissions** *(list) --*

              A list of the permissions for the specified table or database resource located at the path in
              Amazon S3.

              - *(dict) --*

                The permissions granted or revoked on a resource.

                - **Principal** *(dict) --*

                  The Data Lake principal to be granted or revoked permissions.

                  - **DataLakePrincipalIdentifier** *(string) --*

                    An identifier for the AWS Lake Formation principal.

                - **Resource** *(dict) --*

                  The resource where permissions are to be granted or revoked.

                  - **Catalog** *(dict) --*

                    The identifier for the Data Catalog. By default, the account ID. The Data Catalog is
                    the persistent metadata store. It contains database definitions, table definitions, and
                    other control information to manage your AWS Lake Formation environment.

                  - **Database** *(dict) --*

                    The database for the resource. Unique to the Data Catalog. A database is a set of
                    associated table definitions organized into a logical group. You can Grant and Revoke
                    database permissions to a principal.

                    - **Name** *(string) --*

                      The name of the database resource. Unique to the Data Catalog.

                  - **Table** *(dict) --*

                    The table for the resource. A table is a metadata definition that represents your data.
                    You can Grant and Revoke table privileges to a principal.

                    - **DatabaseName** *(string) --*

                      The name of the database for the table. Unique to a Data Catalog. A database is a set
                      of associated table definitions organized into a logical group. You can Grant and
                      Revoke database privileges to a principal.

                    - **Name** *(string) --*

                      The name of the table.

                  - **TableWithColumns** *(dict) --*

                    The table with columns for the resource. A principal with permissions to this resource
                    can select metadata from the columns of a table in the Data Catalog and the underlying
                    data in Amazon S3.

                    - **DatabaseName** *(string) --*

                      The name of the database for the table with columns resource. Unique to the Data
                      Catalog. A database is a set of associated table definitions organized into a logical
                      group. You can Grant and Revoke database privileges to a principal.

                    - **Name** *(string) --*

                      The name of the table resource. A table is a metadata definition that represents your
                      data. You can Grant and Revoke table privileges to a principal.

                    - **ColumnNames** *(list) --*

                      The list of column names for the table. At least one of ``ColumnNames`` or
                      ``ColumnWildcard`` is required.

                      - *(string) --*

                    - **ColumnWildcard** *(dict) --*

                      A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames``
                      or ``ColumnWildcard`` is required.

                      - **ExcludedColumnNames** *(list) --*

                        Excludes column names. Any column with this name will be excluded.

                        - *(string) --*

                  - **DataLocation** *(dict) --*

                    The location of an Amazon S3 path where permissions are granted or revoked.

                    - **ResourceArn** *(string) --*

                      The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

                - **Permissions** *(list) --*

                  The permissions to be granted or revoked on the resource.

                  - *(string) --*

                - **PermissionsWithGrantOption** *(list) --*

                  Indicates whether to grant the ability to grant permissions (as a subset of permissions
                  granted).

                  - *(string) --*

            - **NextToken** *(string) --*

              A continuation token, if this is not the first call to retrieve this list.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def grant_permissions(
        self,
        Principal: ClientGrantPermissionsPrincipalTypeDef,
        Resource: ClientGrantPermissionsResourceTypeDef,
        Permissions: List[str],
        CatalogId: str = None,
        PermissionsWithGrantOption: List[str] = None,
    ) -> Dict[str, Any]:
        """
        Grants permissions to the principal to access metadata in the Data Catalog and data organized in
        underlying data storage such as Amazon S3.

        For information about permissions, see `Security and Access Control to Metadata and Data
        <https://docs-aws.amazon.com/michigan/latest/dg/security-data-access.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lakeformation-2017-03-31/GrantPermissions>`_

        **Request Syntax**
        ::

          response = client.grant_permissions(
              CatalogId='string',
              Principal={
                  'DataLakePrincipalIdentifier': 'string'
              },
              Resource={
                  'Catalog': {}
                  ,
                  'Database': {
                      'Name': 'string'
                  },
                  'Table': {
                      'DatabaseName': 'string',
                      'Name': 'string'
                  },
                  'TableWithColumns': {
                      'DatabaseName': 'string',
                      'Name': 'string',
                      'ColumnNames': [
                          'string',
                      ],
                      'ColumnWildcard': {
                          'ExcludedColumnNames': [
                              'string',
                          ]
                      }
                  },
                  'DataLocation': {
                      'ResourceArn': 'string'
                  }
              },
              Permissions=[
                  'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'
                  |'DATA_LOCATION_ACCESS',
              ],
              PermissionsWithGrantOption=[
                  'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'
                  |'DATA_LOCATION_ACCESS',
              ]
          )
        :type CatalogId: string
        :param CatalogId:

          The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
          persistent metadata store. It contains database definitions, table definitions, and other control
          information to manage your AWS Lake Formation environment.

        :type Principal: dict
        :param Principal: **[REQUIRED]**

          The principal to be granted the permissions on the resource. Supported principals are IAM users
          or IAM roles, and they are defined by their principal type and their ARN.

          Note that if you define a resource with a particular ARN, then later delete, and recreate a
          resource with that same ARN, the resource maintains the permissions already granted.

          - **DataLakePrincipalIdentifier** *(string) --*

            An identifier for the AWS Lake Formation principal.

        :type Resource: dict
        :param Resource: **[REQUIRED]**

          The resource to which permissions are to be granted. Resources in AWS Lake Formation are the Data
          Catalog, databases, and tables.

          - **Catalog** *(dict) --*

            The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
            persistent metadata store. It contains database definitions, table definitions, and other
            control information to manage your AWS Lake Formation environment.

          - **Database** *(dict) --*

            The database for the resource. Unique to the Data Catalog. A database is a set of associated
            table definitions organized into a logical group. You can Grant and Revoke database permissions
            to a principal.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the database resource. Unique to the Data Catalog.

          - **Table** *(dict) --*

            The table for the resource. A table is a metadata definition that represents your data. You can
            Grant and Revoke table privileges to a principal.

            - **DatabaseName** *(string) --* **[REQUIRED]**

              The name of the database for the table. Unique to a Data Catalog. A database is a set of
              associated table definitions organized into a logical group. You can Grant and Revoke
              database privileges to a principal.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the table.

          - **TableWithColumns** *(dict) --*

            The table with columns for the resource. A principal with permissions to this resource can
            select metadata from the columns of a table in the Data Catalog and the underlying data in
            Amazon S3.

            - **DatabaseName** *(string) --*

              The name of the database for the table with columns resource. Unique to the Data Catalog. A
              database is a set of associated table definitions organized into a logical group. You can
              Grant and Revoke database privileges to a principal.

            - **Name** *(string) --*

              The name of the table resource. A table is a metadata definition that represents your data.
              You can Grant and Revoke table privileges to a principal.

            - **ColumnNames** *(list) --*

              The list of column names for the table. At least one of ``ColumnNames`` or ``ColumnWildcard``
              is required.

              - *(string) --*

            - **ColumnWildcard** *(dict) --*

              A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
              ``ColumnWildcard`` is required.

              - **ExcludedColumnNames** *(list) --*

                Excludes column names. Any column with this name will be excluded.

                - *(string) --*

          - **DataLocation** *(dict) --*

            The location of an Amazon S3 path where permissions are granted or revoked.

            - **ResourceArn** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

        :type Permissions: list
        :param Permissions: **[REQUIRED]**

          The permissions granted to the principal on the resource. AWS Lake Formation defines privileges
          to grant and revoke access to metadata in the Data Catalog and data organized in underlying data
          storage such as Amazon S3. AWS Lake Formation requires that each principal be authorized to
          perform a specific task on AWS Lake Formation resources.

          - *(string) --*

        :type PermissionsWithGrantOption: list
        :param PermissionsWithGrantOption:

          Indicates a list of the granted permissions that the principal may pass to other users. These
          permissions may only be a subset of the permissions granted in the ``Privileges`` .

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
    def list_permissions(
        self,
        CatalogId: str = None,
        Principal: ClientListPermissionsPrincipalTypeDef = None,
        ResourceType: str = None,
        Resource: ClientListPermissionsResourceTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListPermissionsResponseTypeDef:
        """
        Returns a list of the principal permissions on the resource, filtered by the permissions of the
        caller. For example, if you are granted an ALTER permission, you are able to see only the principal
        permissions for ALTER.

        This operation returns only those permissions that have been explicitly granted.

        For information about permissions, see `Security and Access Control to Metadata and Data
        <https://docs-aws.amazon.com/michigan/latest/dg/security-data-access.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lakeformation-2017-03-31/ListPermissions>`_

        **Request Syntax**
        ::

          response = client.list_permissions(
              CatalogId='string',
              Principal={
                  'DataLakePrincipalIdentifier': 'string'
              },
              ResourceType='CATALOG'|'DATABASE'|'TABLE'|'DATA_LOCATION',
              Resource={
                  'Catalog': {}
                  ,
                  'Database': {
                      'Name': 'string'
                  },
                  'Table': {
                      'DatabaseName': 'string',
                      'Name': 'string'
                  },
                  'TableWithColumns': {
                      'DatabaseName': 'string',
                      'Name': 'string',
                      'ColumnNames': [
                          'string',
                      ],
                      'ColumnWildcard': {
                          'ExcludedColumnNames': [
                              'string',
                          ]
                      }
                  },
                  'DataLocation': {
                      'ResourceArn': 'string'
                  }
              },
              NextToken='string',
              MaxResults=123
          )
        :type CatalogId: string
        :param CatalogId:

          The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
          persistent metadata store. It contains database definitions, table definitions, and other control
          information to manage your AWS Lake Formation environment.

        :type Principal: dict
        :param Principal:

          Specifies a principal to filter the permissions returned.

          - **DataLakePrincipalIdentifier** *(string) --*

            An identifier for the AWS Lake Formation principal.

        :type ResourceType: string
        :param ResourceType:

          Specifies a resource type to filter the permissions returned.

        :type Resource: dict
        :param Resource:

          A resource where you will get a list of the principal permissions.

          This operation does not support getting privileges on a table with columns. Instead, call this
          operation on the table, and the operation returns the table and the table w columns.

          - **Catalog** *(dict) --*

            The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
            persistent metadata store. It contains database definitions, table definitions, and other
            control information to manage your AWS Lake Formation environment.

          - **Database** *(dict) --*

            The database for the resource. Unique to the Data Catalog. A database is a set of associated
            table definitions organized into a logical group. You can Grant and Revoke database permissions
            to a principal.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the database resource. Unique to the Data Catalog.

          - **Table** *(dict) --*

            The table for the resource. A table is a metadata definition that represents your data. You can
            Grant and Revoke table privileges to a principal.

            - **DatabaseName** *(string) --* **[REQUIRED]**

              The name of the database for the table. Unique to a Data Catalog. A database is a set of
              associated table definitions organized into a logical group. You can Grant and Revoke
              database privileges to a principal.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the table.

          - **TableWithColumns** *(dict) --*

            The table with columns for the resource. A principal with permissions to this resource can
            select metadata from the columns of a table in the Data Catalog and the underlying data in
            Amazon S3.

            - **DatabaseName** *(string) --*

              The name of the database for the table with columns resource. Unique to the Data Catalog. A
              database is a set of associated table definitions organized into a logical group. You can
              Grant and Revoke database privileges to a principal.

            - **Name** *(string) --*

              The name of the table resource. A table is a metadata definition that represents your data.
              You can Grant and Revoke table privileges to a principal.

            - **ColumnNames** *(list) --*

              The list of column names for the table. At least one of ``ColumnNames`` or ``ColumnWildcard``
              is required.

              - *(string) --*

            - **ColumnWildcard** *(dict) --*

              A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
              ``ColumnWildcard`` is required.

              - **ExcludedColumnNames** *(list) --*

                Excludes column names. Any column with this name will be excluded.

                - *(string) --*

          - **DataLocation** *(dict) --*

            The location of an Amazon S3 path where permissions are granted or revoked.

            - **ResourceArn** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

        :type NextToken: string
        :param NextToken:

          A continuation token, if this is not the first call to retrieve this list.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PrincipalResourcePermissions': [
                    {
                        'Principal': {
                            'DataLakePrincipalIdentifier': 'string'
                        },
                        'Resource': {
                            'Catalog': {},
                            'Database': {
                                'Name': 'string'
                            },
                            'Table': {
                                'DatabaseName': 'string',
                                'Name': 'string'
                            },
                            'TableWithColumns': {
                                'DatabaseName': 'string',
                                'Name': 'string',
                                'ColumnNames': [
                                    'string',
                                ],
                                'ColumnWildcard': {
                                    'ExcludedColumnNames': [
                                        'string',
                                    ]
                                }
                            },
                            'DataLocation': {
                                'ResourceArn': 'string'
                            }
                        },
                        'Permissions': [
                            'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'
                            |'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                        ],
                        'PermissionsWithGrantOption': [
                            'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'
                            |'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                        ]
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **PrincipalResourcePermissions** *(list) --*

              A list of principals and their permissions on the resource for the specified principal and
              resource types.

              - *(dict) --*

                The permissions granted or revoked on a resource.

                - **Principal** *(dict) --*

                  The Data Lake principal to be granted or revoked permissions.

                  - **DataLakePrincipalIdentifier** *(string) --*

                    An identifier for the AWS Lake Formation principal.

                - **Resource** *(dict) --*

                  The resource where permissions are to be granted or revoked.

                  - **Catalog** *(dict) --*

                    The identifier for the Data Catalog. By default, the account ID. The Data Catalog is
                    the persistent metadata store. It contains database definitions, table definitions, and
                    other control information to manage your AWS Lake Formation environment.

                  - **Database** *(dict) --*

                    The database for the resource. Unique to the Data Catalog. A database is a set of
                    associated table definitions organized into a logical group. You can Grant and Revoke
                    database permissions to a principal.

                    - **Name** *(string) --*

                      The name of the database resource. Unique to the Data Catalog.

                  - **Table** *(dict) --*

                    The table for the resource. A table is a metadata definition that represents your data.
                    You can Grant and Revoke table privileges to a principal.

                    - **DatabaseName** *(string) --*

                      The name of the database for the table. Unique to a Data Catalog. A database is a set
                      of associated table definitions organized into a logical group. You can Grant and
                      Revoke database privileges to a principal.

                    - **Name** *(string) --*

                      The name of the table.

                  - **TableWithColumns** *(dict) --*

                    The table with columns for the resource. A principal with permissions to this resource
                    can select metadata from the columns of a table in the Data Catalog and the underlying
                    data in Amazon S3.

                    - **DatabaseName** *(string) --*

                      The name of the database for the table with columns resource. Unique to the Data
                      Catalog. A database is a set of associated table definitions organized into a logical
                      group. You can Grant and Revoke database privileges to a principal.

                    - **Name** *(string) --*

                      The name of the table resource. A table is a metadata definition that represents your
                      data. You can Grant and Revoke table privileges to a principal.

                    - **ColumnNames** *(list) --*

                      The list of column names for the table. At least one of ``ColumnNames`` or
                      ``ColumnWildcard`` is required.

                      - *(string) --*

                    - **ColumnWildcard** *(dict) --*

                      A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames``
                      or ``ColumnWildcard`` is required.

                      - **ExcludedColumnNames** *(list) --*

                        Excludes column names. Any column with this name will be excluded.

                        - *(string) --*

                  - **DataLocation** *(dict) --*

                    The location of an Amazon S3 path where permissions are granted or revoked.

                    - **ResourceArn** *(string) --*

                      The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

                - **Permissions** *(list) --*

                  The permissions to be granted or revoked on the resource.

                  - *(string) --*

                - **PermissionsWithGrantOption** *(list) --*

                  Indicates whether to grant the ability to grant permissions (as a subset of permissions
                  granted).

                  - *(string) --*

            - **NextToken** *(string) --*

              A continuation token, if this is not the first call to retrieve this list.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resources(
        self,
        FilterConditionList: List[ClientListResourcesFilterConditionListTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientListResourcesResponseTypeDef:
        """
        Lists the resources registered to be managed by the Data Catalog.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lakeformation-2017-03-31/ListResources>`_

        **Request Syntax**
        ::

          response = client.list_resources(
              FilterConditionList=[
                  {
                      'Field': 'RESOURCE_ARN'|'ROLE_ARN'|'LAST_MODIFIED',
                      'ComparisonOperator':
                      'EQ'|'NE'|'LE'|'LT'|'GE'|'GT'|'CONTAINS'|'NOT_CONTAINS'|'BEGINS_WITH'|'IN'|'BETWEEN',
                      'StringValueList': [
                          'string',
                      ]
                  },
              ],
              MaxResults=123,
              NextToken='string'
          )
        :type FilterConditionList: list
        :param FilterConditionList:

          Any applicable row-level and/or column-level filtering conditions for the resources.

          - *(dict) --*

            This structure describes the filtering of columns in a table based on a filter condition.

            - **Field** *(string) --*

              The field to filter in the filter condition.

            - **ComparisonOperator** *(string) --*

              The comparison operator used in the filter condition.

            - **StringValueList** *(list) --*

              A string with values used in evaluating the filter condition.

              - *(string) --*

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of resource results.

        :type NextToken: string
        :param NextToken:

          A continuation token, if this is not the first call to retrieve these resources.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResourceInfoList': [
                    {
                        'ResourceArn': 'string',
                        'RoleArn': 'string',
                        'LastModified': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ResourceInfoList** *(list) --*

              A summary of the data lake resources.

              - *(dict) --*

                A structure containing information about an AWS Lake Formation resource.

                - **ResourceArn** *(string) --*

                  The Amazon Resource Name (ARN) of the resource.

                - **RoleArn** *(string) --*

                  The IAM role that registered a resource.

                - **LastModified** *(datetime) --*

                  The date and time the resource was last modified.

            - **NextToken** *(string) --*

              A continuation token, if this is not the first call to retrieve these resources.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_data_lake_settings(
        self,
        DataLakeSettings: ClientPutDataLakeSettingsDataLakeSettingsTypeDef,
        CatalogId: str = None,
    ) -> Dict[str, Any]:
        """
        The AWS Lake Formation principal.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lakeformation-2017-03-31/PutDataLakeSettings>`_

        **Request Syntax**
        ::

          response = client.put_data_lake_settings(
              CatalogId='string',
              DataLakeSettings={
                  'DataLakeAdmins': [
                      {
                          'DataLakePrincipalIdentifier': 'string'
                      },
                  ],
                  'CreateDatabaseDefaultPermissions': [
                      {
                          'Principal': {
                              'DataLakePrincipalIdentifier': 'string'
                          },
                          'Permissions': [
                              'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'
                              |'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                          ]
                      },
                  ],
                  'CreateTableDefaultPermissions': [
                      {
                          'Principal': {
                              'DataLakePrincipalIdentifier': 'string'
                          },
                          'Permissions': [
                              'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'
                              |'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                          ]
                      },
                  ]
              }
          )
        :type CatalogId: string
        :param CatalogId:

          The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
          persistent metadata store. It contains database definitions, table definitions, and other control
          information to manage your AWS Lake Formation environment.

        :type DataLakeSettings: dict
        :param DataLakeSettings: **[REQUIRED]**

          A list of AWS Lake Formation principals.

          - **DataLakeAdmins** *(list) --*

            A list of AWS Lake Formation principals.

            - *(dict) --*

              The AWS Lake Formation principal.

              - **DataLakePrincipalIdentifier** *(string) --*

                An identifier for the AWS Lake Formation principal.

          - **CreateDatabaseDefaultPermissions** *(list) --*

            A list of up to three principal permissions entries for default create database permissions.

            - *(dict) --*

              Permissions granted to a principal.

              - **Principal** *(dict) --*

                The principal who is granted permissions.

                - **DataLakePrincipalIdentifier** *(string) --*

                  An identifier for the AWS Lake Formation principal.

              - **Permissions** *(list) --*

                The permissions that are granted to the principal.

                - *(string) --*

          - **CreateTableDefaultPermissions** *(list) --*

            A list of up to three principal permissions entries for default create table permissions.

            - *(dict) --*

              Permissions granted to a principal.

              - **Principal** *(dict) --*

                The principal who is granted permissions.

                - **DataLakePrincipalIdentifier** *(string) --*

                  An identifier for the AWS Lake Formation principal.

              - **Permissions** *(list) --*

                The permissions that are granted to the principal.

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
    def register_resource(
        self, ResourceArn: str, UseServiceLinkedRole: bool = None, RoleArn: str = None
    ) -> Dict[str, Any]:
        """
        Registers the resource as managed by the Data Catalog.

        To add or update data, Lake Formation needs read/write access to the chosen Amazon S3 path. Choose
        a role that you know has permission to do this, or choose the
        AWSServiceRoleForLakeFormationDataAccess service-linked role. When you register the first Amazon S3
        path, the service-linked role and a new inline policy are created on your behalf. Lake Formation
        adds the first path to the inline policy and attaches it to the service-linked role. When you
        register subsequent paths, Lake Formation adds the path to the existing policy.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lakeformation-2017-03-31/RegisterResource>`_

        **Request Syntax**
        ::

          response = client.register_resource(
              ResourceArn='string',
              UseServiceLinkedRole=True|False,
              RoleArn='string'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource that you want to register.

        :type UseServiceLinkedRole: boolean
        :param UseServiceLinkedRole:

          Designates a trusted caller, an IAM principal, by registering this caller with the Data Catalog.

        :type RoleArn: string
        :param RoleArn:

          The identifier for the role.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_permissions(
        self,
        Principal: ClientRevokePermissionsPrincipalTypeDef,
        Resource: ClientRevokePermissionsResourceTypeDef,
        Permissions: List[str],
        CatalogId: str = None,
        PermissionsWithGrantOption: List[str] = None,
    ) -> Dict[str, Any]:
        """
        Revokes permissions to the principal to access metadata in the Data Catalog and data organized in
        underlying data storage such as Amazon S3.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lakeformation-2017-03-31/RevokePermissions>`_

        **Request Syntax**
        ::

          response = client.revoke_permissions(
              CatalogId='string',
              Principal={
                  'DataLakePrincipalIdentifier': 'string'
              },
              Resource={
                  'Catalog': {}
                  ,
                  'Database': {
                      'Name': 'string'
                  },
                  'Table': {
                      'DatabaseName': 'string',
                      'Name': 'string'
                  },
                  'TableWithColumns': {
                      'DatabaseName': 'string',
                      'Name': 'string',
                      'ColumnNames': [
                          'string',
                      ],
                      'ColumnWildcard': {
                          'ExcludedColumnNames': [
                              'string',
                          ]
                      }
                  },
                  'DataLocation': {
                      'ResourceArn': 'string'
                  }
              },
              Permissions=[
                  'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'
                  |'DATA_LOCATION_ACCESS',
              ],
              PermissionsWithGrantOption=[
                  'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'|'CREATE_DATABASE'|'CREATE_TABLE'
                  |'DATA_LOCATION_ACCESS',
              ]
          )
        :type CatalogId: string
        :param CatalogId:

          The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
          persistent metadata store. It contains database definitions, table definitions, and other control
          information to manage your AWS Lake Formation environment.

        :type Principal: dict
        :param Principal: **[REQUIRED]**

          The principal to be revoked permissions on the resource.

          - **DataLakePrincipalIdentifier** *(string) --*

            An identifier for the AWS Lake Formation principal.

        :type Resource: dict
        :param Resource: **[REQUIRED]**

          The resource to which permissions are to be revoked.

          - **Catalog** *(dict) --*

            The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
            persistent metadata store. It contains database definitions, table definitions, and other
            control information to manage your AWS Lake Formation environment.

          - **Database** *(dict) --*

            The database for the resource. Unique to the Data Catalog. A database is a set of associated
            table definitions organized into a logical group. You can Grant and Revoke database permissions
            to a principal.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the database resource. Unique to the Data Catalog.

          - **Table** *(dict) --*

            The table for the resource. A table is a metadata definition that represents your data. You can
            Grant and Revoke table privileges to a principal.

            - **DatabaseName** *(string) --* **[REQUIRED]**

              The name of the database for the table. Unique to a Data Catalog. A database is a set of
              associated table definitions organized into a logical group. You can Grant and Revoke
              database privileges to a principal.

            - **Name** *(string) --* **[REQUIRED]**

              The name of the table.

          - **TableWithColumns** *(dict) --*

            The table with columns for the resource. A principal with permissions to this resource can
            select metadata from the columns of a table in the Data Catalog and the underlying data in
            Amazon S3.

            - **DatabaseName** *(string) --*

              The name of the database for the table with columns resource. Unique to the Data Catalog. A
              database is a set of associated table definitions organized into a logical group. You can
              Grant and Revoke database privileges to a principal.

            - **Name** *(string) --*

              The name of the table resource. A table is a metadata definition that represents your data.
              You can Grant and Revoke table privileges to a principal.

            - **ColumnNames** *(list) --*

              The list of column names for the table. At least one of ``ColumnNames`` or ``ColumnWildcard``
              is required.

              - *(string) --*

            - **ColumnWildcard** *(dict) --*

              A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
              ``ColumnWildcard`` is required.

              - **ExcludedColumnNames** *(list) --*

                Excludes column names. Any column with this name will be excluded.

                - *(string) --*

          - **DataLocation** *(dict) --*

            The location of an Amazon S3 path where permissions are granted or revoked.

            - **ResourceArn** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

        :type Permissions: list
        :param Permissions: **[REQUIRED]**

          The permissions revoked to the principal on the resource. For information about permissions, see
          `Security and Access Control to Metadata and Data
          <https://docs-aws.amazon.com/michigan/latest/dg/security-data-access.html>`__ .

          - *(string) --*

        :type PermissionsWithGrantOption: list
        :param PermissionsWithGrantOption:

          Indicates a list of permissions for which to revoke the grant option allowing the principal to
          pass permissions to other principals.

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
    def update_resource(self, RoleArn: str, ResourceArn: str) -> Dict[str, Any]:
        """
        Updates the data access role used for vending access to the given (registered) resource in AWS Lake
        Formation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lakeformation-2017-03-31/UpdateResource>`_

        **Request Syntax**
        ::

          response = client.update_resource(
              RoleArn='string',
              ResourceArn='string'
          )
        :type RoleArn: string
        :param RoleArn: **[REQUIRED]**

          The new role to use for the given resource registered in AWS Lake Formation.

        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The resource ARN.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """


class Exceptions:
    AlreadyExistsException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentModificationException: Boto3ClientError
    EntityNotFoundException: Boto3ClientError
    InternalServiceException: Boto3ClientError
    InvalidInputException: Boto3ClientError
    OperationTimeoutException: Boto3ClientError

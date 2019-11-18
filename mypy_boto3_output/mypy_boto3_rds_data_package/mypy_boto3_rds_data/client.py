"Main interface for rds-data Client"
from __future__ import annotations

from typing import Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_rds_data.client as client_scope
from mypy_boto3_rds_data.type_defs import (
    ClientBatchExecuteStatementResponseTypeDef,
    ClientBatchExecuteStatementparameterSetsTypeDef,
    ClientBeginTransactionResponseTypeDef,
    ClientCommitTransactionResponseTypeDef,
    ClientExecuteSqlResponseTypeDef,
    ClientExecuteStatementResponseTypeDef,
    ClientExecuteStatementparametersTypeDef,
    ClientExecuteStatementresultSetOptionsTypeDef,
    ClientRollbackTransactionResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_execute_statement(
        self,
        resourceArn: str,
        secretArn: str,
        sql: str,
        database: str = None,
        parameterSets: List[
            List[ClientBatchExecuteStatementparameterSetsTypeDef]
        ] = None,
        schema: str = None,
        transactionId: str = None,
    ) -> ClientBatchExecuteStatementResponseTypeDef:
        """
        Runs a batch SQL statement over an array of data.

        You can run bulk update and insert operations for multiple records using a DML statement with
        different parameter sets. Bulk operations can provide a significant performance improvement over
        individual insert and update operations.

        .. warning::

          If a call isn't part of a transaction because it doesn't include the ``transactionID`` parameter,
          changes that result from the call are committed automatically.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rds-data-2018-08-01/BatchExecuteStatement>`_

        **Request Syntax**
        ::

          response = client.batch_execute_statement(
              database='string',
              parameterSets=[
                  [
                      {
                          'name': 'string',
                          'value': {
                              'arrayValue': {
                                  'arrayValues': [
                                      {'... recursive ...'},
                                  ],
                                  'booleanValues': [
                                      True|False,
                                  ],
                                  'doubleValues': [
                                      123.0,
                                  ],
                                  'longValues': [
                                      123,
                                  ],
                                  'stringValues': [
                                      'string',
                                  ]
                              },
                              'blobValue': b'bytes',
                              'booleanValue': True|False,
                              'doubleValue': 123.0,
                              'isNull': True|False,
                              'longValue': 123,
                              'stringValue': 'string'
                          }
                      },
                  ],
              ],
              resourceArn='string',
              schema='string',
              secretArn='string',
              sql='string',
              transactionId='string'
          )
        :type database: string
        :param database:

          The name of the database.

        :type parameterSets: list
        :param parameterSets:

          The parameter set for the batch operation.

          - *(list) --*

            - *(dict) --*

              A parameter used in a SQL statement.

              - **name** *(string) --*

                The name of the parameter.

              - **value** *(dict) --*

                The value of the parameter.

                - **arrayValue** *(dict) --*

                  An array of values.

                  - **arrayValues** *(list) --*

                    An array of arrays.

                    - *(dict) --*

                      Contains an array.

                  - **booleanValues** *(list) --*

                    An array of Boolean values.

                    - *(boolean) --*

                  - **doubleValues** *(list) --*

                    An array of integers.

                    - *(float) --*

                  - **longValues** *(list) --*

                    An array of floating point numbers.

                    - *(integer) --*

                  - **stringValues** *(list) --*

                    An array of strings.

                    - *(string) --*

                - **blobValue** *(bytes) --*

                  A value of BLOB data type.

                - **booleanValue** *(boolean) --*

                  A value of Boolean data type.

                - **doubleValue** *(float) --*

                  A value of double data type.

                - **isNull** *(boolean) --*

                  A NULL value.

                - **longValue** *(integer) --*

                  A value of long data type.

                - **stringValue** *(string) --*

                  A value of string data type.

        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.

        :type schema: string
        :param schema:

          The name of the database schema.

        :type secretArn: string
        :param secretArn: **[REQUIRED]**

          The name or ARN of the secret that enables access to the DB cluster.

        :type sql: string
        :param sql: **[REQUIRED]**

          The SQL statement to run.

        :type transactionId: string
        :param transactionId:

          The identifier of a transaction that was started by using the ``BeginTransaction`` operation.
          Specify the transaction ID of the transaction that you want to include the SQL statement in.

          If the SQL statement is not part of a transaction, don't set this parameter.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'updateResults': [
                    {
                        'generatedFields': [
                            {
                                'arrayValue': {
                                    'arrayValues': [
                                        {'... recursive ...'},
                                    ],
                                    'booleanValues': [
                                        True|False,
                                    ],
                                    'doubleValues': [
                                        123.0,
                                    ],
                                    'longValues': [
                                        123,
                                    ],
                                    'stringValues': [
                                        'string',
                                    ]
                                },
                                'blobValue': b'bytes',
                                'booleanValue': True|False,
                                'doubleValue': 123.0,
                                'isNull': True|False,
                                'longValue': 123,
                                'stringValue': 'string'
                            },
                        ]
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            The response elements represent the output of a SQL statement over an array of data.

            - **updateResults** *(list) --*

              The execution results of each batch entry.

              - *(dict) --*

                The response elements represent the results of an update.

                - **generatedFields** *(list) --*

                  Values for fields generated during the request.

                  - *(dict) --*

                    Contains a value.

                    - **arrayValue** *(dict) --*

                      An array of values.

                      - **arrayValues** *(list) --*

                        An array of arrays.

                        - *(dict) --*

                          Contains an array.

                      - **booleanValues** *(list) --*

                        An array of Boolean values.

                        - *(boolean) --*

                      - **doubleValues** *(list) --*

                        An array of integers.

                        - *(float) --*

                      - **longValues** *(list) --*

                        An array of floating point numbers.

                        - *(integer) --*

                      - **stringValues** *(list) --*

                        An array of strings.

                        - *(string) --*

                    - **blobValue** *(bytes) --*

                      A value of BLOB data type.

                    - **booleanValue** *(boolean) --*

                      A value of Boolean data type.

                    - **doubleValue** *(float) --*

                      A value of double data type.

                    - **isNull** *(boolean) --*

                      A NULL value.

                    - **longValue** *(integer) --*

                      A value of long data type.

                    - **stringValue** *(string) --*

                      A value of string data type.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def begin_transaction(
        self, resourceArn: str, secretArn: str, database: str = None, schema: str = None
    ) -> ClientBeginTransactionResponseTypeDef:
        """
        Starts a SQL transaction.

         ``<important> <p>A transaction can run for a maximum of 24 hours. A transaction is terminated and
         rolled back automatically after 24 hours.</p> <p>A transaction times out if no calls use its
         transaction ID in three minutes. If a transaction times out before it's committed, it's rolled
         back automatically.</p> <p>DDL statements inside a transaction cause an implicit commit. We
         recommend that you run each DDL statement in a separate <code>ExecuteStatement</code> call with
         <code>continueAfterTimeout</code> enabled.</p> </important>``

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rds-data-2018-08-01/BeginTransaction>`_

        **Request Syntax**
        ::

          response = client.begin_transaction(
              database='string',
              resourceArn='string',
              schema='string',
              secretArn='string'
          )
        :type database: string
        :param database:

          The name of the database.

        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.

        :type schema: string
        :param schema:

          The name of the database schema.

        :type secretArn: string
        :param secretArn: **[REQUIRED]**

          The name or ARN of the secret that enables access to the DB cluster.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'transactionId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            The response elements represent the output of a request to start a SQL transaction.

            - **transactionId** *(string) --*

              The transaction ID of the transaction started by the call.

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
    def commit_transaction(
        self, resourceArn: str, secretArn: str, transactionId: str
    ) -> ClientCommitTransactionResponseTypeDef:
        """
        Ends a SQL transaction started with the ``BeginTransaction`` operation and commits the changes.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rds-data-2018-08-01/CommitTransaction>`_

        **Request Syntax**
        ::

          response = client.commit_transaction(
              resourceArn='string',
              secretArn='string',
              transactionId='string'
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.

        :type secretArn: string
        :param secretArn: **[REQUIRED]**

          The name or ARN of the secret that enables access to the DB cluster.

        :type transactionId: string
        :param transactionId: **[REQUIRED]**

          The identifier of the transaction to end and commit.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'transactionStatus': 'string'
            }
          **Response Structure**

          - *(dict) --*

            The response elements represent the output of a commit transaction request.

            - **transactionStatus** *(string) --*

              The status of the commit operation.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def execute_sql(
        self,
        awsSecretStoreArn: str,
        dbClusterOrInstanceArn: str,
        sqlStatements: str,
        database: str = None,
        schema: str = None,
    ) -> ClientExecuteSqlResponseTypeDef:
        """
        Runs one or more SQL statements.

        .. warning::

          This operation is deprecated. Use the ``BatchExecuteStatement`` or ``ExecuteStatement`` operation.

        .. danger::

            This operation is deprecated and may not function as expected. This operation should not be
            used going forward and is only kept for the purpose of backwards compatiblity.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rds-data-2018-08-01/ExecuteSql>`_

        **Request Syntax**
        ::

          response = client.execute_sql(
              awsSecretStoreArn='string',
              database='string',
              dbClusterOrInstanceArn='string',
              schema='string',
              sqlStatements='string'
          )
        :type awsSecretStoreArn: string
        :param awsSecretStoreArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the secret that enables access to the DB cluster.

        :type database: string
        :param database:

          The name of the database.

        :type dbClusterOrInstanceArn: string
        :param dbClusterOrInstanceArn: **[REQUIRED]**

          The ARN of the Aurora Serverless DB cluster.

        :type schema: string
        :param schema:

          The name of the database schema.

        :type sqlStatements: string
        :param sqlStatements: **[REQUIRED]**

          One or more SQL statements to run on the DB cluster.

          You can separate SQL statements from each other with a semicolon (;). Any valid SQL statement is
          permitted, including data definition, data manipulation, and commit statements.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'sqlStatementResults': [
                    {
                        'numberOfRecordsUpdated': 123,
                        'resultFrame': {
                            'records': [
                                {
                                    'values': [
                                        {
                                            'arrayValues': [
                                                {'... recursive ...'},
                                            ],
                                            'bigIntValue': 123,
                                            'bitValue': True|False,
                                            'blobValue': b'bytes',
                                            'doubleValue': 123.0,
                                            'intValue': 123,
                                            'isNull': True|False,
                                            'realValue': ...,
                                            'stringValue': 'string',
                                            'structValue': {
                                                'attributes': [
                                                    {'... recursive ...'},
                                                ]
                                            }
                                        },
                                    ]
                                },
                            ],
                            'resultSetMetadata': {
                                'columnCount': 123,
                                'columnMetadata': [
                                    {
                                        'arrayBaseColumnType': 123,
                                        'isAutoIncrement': True|False,
                                        'isCaseSensitive': True|False,
                                        'isCurrency': True|False,
                                        'isSigned': True|False,
                                        'label': 'string',
                                        'name': 'string',
                                        'nullable': 123,
                                        'precision': 123,
                                        'scale': 123,
                                        'schemaName': 'string',
                                        'tableName': 'string',
                                        'type': 123,
                                        'typeName': 'string'
                                    },
                                ]
                            }
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            The response elements represent the output of a request to run one or more SQL statements.

            - **sqlStatementResults** *(list) --*

              The results of the SQL statement or statements.

              - *(dict) --*

                The result of a SQL statement.

                 ``<important> <p>This data type is deprecated.</p> </important>``

                - **numberOfRecordsUpdated** *(integer) --*

                  The number of records updated by a SQL statement.

                - **resultFrame** *(dict) --*

                  The result set of the SQL statement.

                  - **records** *(list) --*

                    The records in the result set.

                    - *(dict) --*

                      A record returned by a call.

                      - **values** *(list) --*

                        The values returned in the record.

                        - *(dict) --*

                          Contains the value of a column.

                           ``<important> <p>This data type is deprecated.</p> </important>``

                          - **arrayValues** *(list) --*

                            An array of column values.

                            - *(dict) --*

                              Contains the value of a column.

                               ``<important> <p>This data type is deprecated.</p> </important>``

                          - **bigIntValue** *(integer) --*

                            A value for a column of big integer data type.

                          - **bitValue** *(boolean) --*

                            A value for a column of BIT data type.

                          - **blobValue** *(bytes) --*

                            A value for a column of BLOB data type.

                          - **doubleValue** *(float) --*

                            A value for a column of double data type.

                          - **intValue** *(integer) --*

                            A value for a column of integer data type.

                          - **isNull** *(boolean) --*

                            A NULL value.

                          - **realValue** *(float) --*

                            A value for a column of real data type.

                          - **stringValue** *(string) --*

                            A value for a column of string data type.

                          - **structValue** *(dict) --*

                            A value for a column of STRUCT data type.

                            - **attributes** *(list) --*

                              The attributes returned in the record.

                              - *(dict) --*

                                Contains the value of a column.

                                 ``<important> <p>This data type is deprecated.</p> </important>``

                  - **resultSetMetadata** *(dict) --*

                    The result-set metadata in the result set.

                    - **columnCount** *(integer) --*

                      The number of columns in the result set.

                    - **columnMetadata** *(list) --*

                      The metadata of the columns in the result set.

                      - *(dict) --*

                        Contains the metadata for a column.

                        - **arrayBaseColumnType** *(integer) --*

                          The type of the column.

                        - **isAutoIncrement** *(boolean) --*

                          A value that indicates whether the column increments automatically.

                        - **isCaseSensitive** *(boolean) --*

                          A value that indicates whether the column is case-sensitive.

                        - **isCurrency** *(boolean) --*

                          A value that indicates whether the column contains currency values.

                        - **isSigned** *(boolean) --*

                          A value that indicates whether an integer column is signed.

                        - **label** *(string) --*

                          The label for the column.

                        - **name** *(string) --*

                          The name of the column.

                        - **nullable** *(integer) --*

                          A value that indicates whether the column is nullable.

                        - **precision** *(integer) --*

                          The precision value of a decimal number column.

                        - **scale** *(integer) --*

                          The scale value of a decimal number column.

                        - **schemaName** *(string) --*

                          The name of the schema that owns the table that includes the column.

                        - **tableName** *(string) --*

                          The name of the table that includes the column.

                        - **type** *(integer) --*

                          The type of the column.

                        - **typeName** *(string) --*

                          The database-specific data type of the column.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def execute_statement(
        self,
        resourceArn: str,
        secretArn: str,
        sql: str,
        continueAfterTimeout: bool = None,
        database: str = None,
        includeResultMetadata: bool = None,
        parameters: List[ClientExecuteStatementparametersTypeDef] = None,
        resultSetOptions: ClientExecuteStatementresultSetOptionsTypeDef = None,
        schema: str = None,
        transactionId: str = None,
    ) -> ClientExecuteStatementResponseTypeDef:
        """
        Runs a SQL statement against a database.

        .. warning::

          If a call isn't part of a transaction because it doesn't include the ``transactionID`` parameter,
          changes that result from the call are committed automatically.

        The response size limit is 1 MB or 1,000 records. If the call returns more than 1 MB of response
        data or over 1,000 records, the call is terminated.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rds-data-2018-08-01/ExecuteStatement>`_

        **Request Syntax**
        ::

          response = client.execute_statement(
              continueAfterTimeout=True|False,
              database='string',
              includeResultMetadata=True|False,
              parameters=[
                  {
                      'name': 'string',
                      'value': {
                          'arrayValue': {
                              'arrayValues': [
                                  {'... recursive ...'},
                              ],
                              'booleanValues': [
                                  True|False,
                              ],
                              'doubleValues': [
                                  123.0,
                              ],
                              'longValues': [
                                  123,
                              ],
                              'stringValues': [
                                  'string',
                              ]
                          },
                          'blobValue': b'bytes',
                          'booleanValue': True|False,
                          'doubleValue': 123.0,
                          'isNull': True|False,
                          'longValue': 123,
                          'stringValue': 'string'
                      }
                  },
              ],
              resourceArn='string',
              resultSetOptions={
                  'decimalReturnType': 'DOUBLE_OR_LONG'|'STRING'
              },
              schema='string',
              secretArn='string',
              sql='string',
              transactionId='string'
          )
        :type continueAfterTimeout: boolean
        :param continueAfterTimeout:

          A value that indicates whether to continue running the statement after the call times out. By
          default, the statement stops running when the call times out.

          .. warning::

            For DDL statements, we recommend continuing to run the statement after the call times out. When
            a DDL statement terminates before it is finished running, it can result in errors and possibly
            corrupted data structures.

        :type database: string
        :param database:

          The name of the database.

        :type includeResultMetadata: boolean
        :param includeResultMetadata:

          A value that indicates whether to include metadata in the results.

        :type parameters: list
        :param parameters:

          The parameters for the SQL statement.

          - *(dict) --*

            A parameter used in a SQL statement.

            - **name** *(string) --*

              The name of the parameter.

            - **value** *(dict) --*

              The value of the parameter.

              - **arrayValue** *(dict) --*

                An array of values.

                - **arrayValues** *(list) --*

                  An array of arrays.

                  - *(dict) --*

                    Contains an array.

                - **booleanValues** *(list) --*

                  An array of Boolean values.

                  - *(boolean) --*

                - **doubleValues** *(list) --*

                  An array of integers.

                  - *(float) --*

                - **longValues** *(list) --*

                  An array of floating point numbers.

                  - *(integer) --*

                - **stringValues** *(list) --*

                  An array of strings.

                  - *(string) --*

              - **blobValue** *(bytes) --*

                A value of BLOB data type.

              - **booleanValue** *(boolean) --*

                A value of Boolean data type.

              - **doubleValue** *(float) --*

                A value of double data type.

              - **isNull** *(boolean) --*

                A NULL value.

              - **longValue** *(integer) --*

                A value of long data type.

              - **stringValue** *(string) --*

                A value of string data type.

        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.

        :type resultSetOptions: dict
        :param resultSetOptions:

          Options that control how the result set is returned.

          - **decimalReturnType** *(string) --*

            A value that indicates how a field of ``DECIMAL`` type is represented in the response. The
            value of ``STRING`` , the default, specifies that it is converted to a String value. The value
            of ``DOUBLE_OR_LONG`` specifies that it is converted to a Long value if its scale is 0, or to a
            Double value otherwise.

            .. warning::

              Conversion to Double or Long can result in roundoff errors due to precision loss. We
              recommend converting to String, especially when working with currency values.

        :type schema: string
        :param schema:

          The name of the database schema.

        :type secretArn: string
        :param secretArn: **[REQUIRED]**

          The name or ARN of the secret that enables access to the DB cluster.

        :type sql: string
        :param sql: **[REQUIRED]**

          The SQL statement to run.

        :type transactionId: string
        :param transactionId:

          The identifier of a transaction that was started by using the ``BeginTransaction`` operation.
          Specify the transaction ID of the transaction that you want to include the SQL statement in.

          If the SQL statement is not part of a transaction, don't set this parameter.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'columnMetadata': [
                    {
                        'arrayBaseColumnType': 123,
                        'isAutoIncrement': True|False,
                        'isCaseSensitive': True|False,
                        'isCurrency': True|False,
                        'isSigned': True|False,
                        'label': 'string',
                        'name': 'string',
                        'nullable': 123,
                        'precision': 123,
                        'scale': 123,
                        'schemaName': 'string',
                        'tableName': 'string',
                        'type': 123,
                        'typeName': 'string'
                    },
                ],
                'generatedFields': [
                    {
                        'arrayValue': {
                            'arrayValues': [
                                {'... recursive ...'},
                            ],
                            'booleanValues': [
                                True|False,
                            ],
                            'doubleValues': [
                                123.0,
                            ],
                            'longValues': [
                                123,
                            ],
                            'stringValues': [
                                'string',
                            ]
                        },
                        'blobValue': b'bytes',
                        'booleanValue': True|False,
                        'doubleValue': 123.0,
                        'isNull': True|False,
                        'longValue': 123,
                        'stringValue': 'string'
                    },
                ],
                'numberOfRecordsUpdated': 123,
                'records': [
                    [
                        {
                            'arrayValue': {
                                'arrayValues': [
                                    {'... recursive ...'},
                                ],
                                'booleanValues': [
                                    True|False,
                                ],
                                'doubleValues': [
                                    123.0,
                                ],
                                'longValues': [
                                    123,
                                ],
                                'stringValues': [
                                    'string',
                                ]
                            },
                            'blobValue': b'bytes',
                            'booleanValue': True|False,
                            'doubleValue': 123.0,
                            'isNull': True|False,
                            'longValue': 123,
                            'stringValue': 'string'
                        },
                    ],
                ]
            }
          **Response Structure**

          - *(dict) --*

            The response elements represent the output of a request to run a SQL statement against a
            database.

            - **columnMetadata** *(list) --*

              Metadata for the columns included in the results.

              - *(dict) --*

                Contains the metadata for a column.

                - **arrayBaseColumnType** *(integer) --*

                  The type of the column.

                - **isAutoIncrement** *(boolean) --*

                  A value that indicates whether the column increments automatically.

                - **isCaseSensitive** *(boolean) --*

                  A value that indicates whether the column is case-sensitive.

                - **isCurrency** *(boolean) --*

                  A value that indicates whether the column contains currency values.

                - **isSigned** *(boolean) --*

                  A value that indicates whether an integer column is signed.

                - **label** *(string) --*

                  The label for the column.

                - **name** *(string) --*

                  The name of the column.

                - **nullable** *(integer) --*

                  A value that indicates whether the column is nullable.

                - **precision** *(integer) --*

                  The precision value of a decimal number column.

                - **scale** *(integer) --*

                  The scale value of a decimal number column.

                - **schemaName** *(string) --*

                  The name of the schema that owns the table that includes the column.

                - **tableName** *(string) --*

                  The name of the table that includes the column.

                - **type** *(integer) --*

                  The type of the column.

                - **typeName** *(string) --*

                  The database-specific data type of the column.

            - **generatedFields** *(list) --*

              Values for fields generated during the request.

               ``<note> <p>The <code>generatedFields</code> data isn't supported by Aurora PostgreSQL. To
               get the values of generated fields, use the <code>RETURNING</code> clause. For more
               information, see <a href="https://www.postgresql.org/docs/10/dml-returning.html">Returning
               Data From Modified Rows</a> in the PostgreSQL documentation.</p> </note>``

              - *(dict) --*

                Contains a value.

                - **arrayValue** *(dict) --*

                  An array of values.

                  - **arrayValues** *(list) --*

                    An array of arrays.

                    - *(dict) --*

                      Contains an array.

                  - **booleanValues** *(list) --*

                    An array of Boolean values.

                    - *(boolean) --*

                  - **doubleValues** *(list) --*

                    An array of integers.

                    - *(float) --*

                  - **longValues** *(list) --*

                    An array of floating point numbers.

                    - *(integer) --*

                  - **stringValues** *(list) --*

                    An array of strings.

                    - *(string) --*

                - **blobValue** *(bytes) --*

                  A value of BLOB data type.

                - **booleanValue** *(boolean) --*

                  A value of Boolean data type.

                - **doubleValue** *(float) --*

                  A value of double data type.

                - **isNull** *(boolean) --*

                  A NULL value.

                - **longValue** *(integer) --*

                  A value of long data type.

                - **stringValue** *(string) --*

                  A value of string data type.

            - **numberOfRecordsUpdated** *(integer) --*

              The number of records updated by the request.

            - **records** *(list) --*

              The records returned by the SQL statement.

              - *(list) --*

                - *(dict) --*

                  Contains a value.

                  - **arrayValue** *(dict) --*

                    An array of values.

                    - **arrayValues** *(list) --*

                      An array of arrays.

                      - *(dict) --*

                        Contains an array.

                    - **booleanValues** *(list) --*

                      An array of Boolean values.

                      - *(boolean) --*

                    - **doubleValues** *(list) --*

                      An array of integers.

                      - *(float) --*

                    - **longValues** *(list) --*

                      An array of floating point numbers.

                      - *(integer) --*

                    - **stringValues** *(list) --*

                      An array of strings.

                      - *(string) --*

                  - **blobValue** *(bytes) --*

                    A value of BLOB data type.

                  - **booleanValue** *(boolean) --*

                    A value of Boolean data type.

                  - **doubleValue** *(float) --*

                    A value of double data type.

                  - **isNull** *(boolean) --*

                    A NULL value.

                  - **longValue** *(integer) --*

                    A value of long data type.

                  - **stringValue** *(string) --*

                    A value of string data type.

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
    def rollback_transaction(
        self, resourceArn: str, secretArn: str, transactionId: str
    ) -> ClientRollbackTransactionResponseTypeDef:
        """
        Performs a rollback of a transaction. Rolling back a transaction cancels its changes.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rds-data-2018-08-01/RollbackTransaction>`_

        **Request Syntax**
        ::

          response = client.rollback_transaction(
              resourceArn='string',
              secretArn='string',
              transactionId='string'
          )
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.

        :type secretArn: string
        :param secretArn: **[REQUIRED]**

          The name or ARN of the secret that enables access to the DB cluster.

        :type transactionId: string
        :param transactionId: **[REQUIRED]**

          The identifier of the transaction to roll back.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'transactionStatus': 'string'
            }
          **Response Structure**

          - *(dict) --*

            The response elements represent the output of a request to perform a rollback of a transaction.

            - **transactionStatus** *(string) --*

              The status of the rollback operation.

        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ServiceUnavailableError: Boto3ClientError
    StatementTimeoutException: Boto3ClientError

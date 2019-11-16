"Main interface for rds-data type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsarrayValueTypeDef",
    "ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsTypeDef",
    "ClientBatchExecuteStatementResponseupdateResultsTypeDef",
    "ClientBatchExecuteStatementResponseTypeDef",
    "ClientBatchExecuteStatementparameterSetsvaluearrayValueTypeDef",
    "ClientBatchExecuteStatementparameterSetsvalueTypeDef",
    "ClientBatchExecuteStatementparameterSetsTypeDef",
    "ClientBeginTransactionResponseTypeDef",
    "ClientCommitTransactionResponseTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesstructValueTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadatacolumnMetadataTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadataTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsresultFrameTypeDef",
    "ClientExecuteSqlResponsesqlStatementResultsTypeDef",
    "ClientExecuteSqlResponseTypeDef",
    "ClientExecuteStatementResponsecolumnMetadataTypeDef",
    "ClientExecuteStatementResponsegeneratedFieldsarrayValueTypeDef",
    "ClientExecuteStatementResponsegeneratedFieldsTypeDef",
    "ClientExecuteStatementResponserecordsarrayValueTypeDef",
    "ClientExecuteStatementResponserecordsTypeDef",
    "ClientExecuteStatementResponseTypeDef",
    "ClientExecuteStatementparametersvaluearrayValueTypeDef",
    "ClientExecuteStatementparametersvalueTypeDef",
    "ClientExecuteStatementparametersTypeDef",
    "ClientExecuteStatementresultSetOptionsTypeDef",
    "ClientRollbackTransactionResponseTypeDef",
)


_ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsarrayValueTypeDef = TypedDict(
    "_ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsarrayValueTypeDef",
    {
        "arrayValues": List[Dict],
        "booleanValues": List[bool],
        "doubleValues": List[float],
        "longValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)


class ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsarrayValueTypeDef(
    _ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsarrayValueTypeDef
):
    """
    Type definition for `ClientBatchExecuteStatementResponseupdateResultsgeneratedFields` `arrayValue`

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
    """


_ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsTypeDef = TypedDict(
    "_ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsTypeDef",
    {
        "arrayValue": ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsarrayValueTypeDef,
        "blobValue": bytes,
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)


class ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsTypeDef(
    _ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsTypeDef
):
    """
    Type definition for `ClientBatchExecuteStatementResponseupdateResults` `generatedFields`

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


_ClientBatchExecuteStatementResponseupdateResultsTypeDef = TypedDict(
    "_ClientBatchExecuteStatementResponseupdateResultsTypeDef",
    {
        "generatedFields": List[
            ClientBatchExecuteStatementResponseupdateResultsgeneratedFieldsTypeDef
        ]
    },
    total=False,
)


class ClientBatchExecuteStatementResponseupdateResultsTypeDef(
    _ClientBatchExecuteStatementResponseupdateResultsTypeDef
):
    """
    Type definition for `ClientBatchExecuteStatementResponse` `updateResults`

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


_ClientBatchExecuteStatementResponseTypeDef = TypedDict(
    "_ClientBatchExecuteStatementResponseTypeDef",
    {"updateResults": List[ClientBatchExecuteStatementResponseupdateResultsTypeDef]},
    total=False,
)


class ClientBatchExecuteStatementResponseTypeDef(
    _ClientBatchExecuteStatementResponseTypeDef
):
    """
    Type definition for `ClientBatchExecuteStatement` `Response`

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


_ClientBatchExecuteStatementparameterSetsvaluearrayValueTypeDef = TypedDict(
    "_ClientBatchExecuteStatementparameterSetsvaluearrayValueTypeDef",
    {
        "arrayValues": List[Dict],
        "booleanValues": List[bool],
        "doubleValues": List[float],
        "longValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)


class ClientBatchExecuteStatementparameterSetsvaluearrayValueTypeDef(
    _ClientBatchExecuteStatementparameterSetsvaluearrayValueTypeDef
):
    """
    Type definition for `ClientBatchExecuteStatementparameterSetsvalue` `arrayValue`

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
    """


_ClientBatchExecuteStatementparameterSetsvalueTypeDef = TypedDict(
    "_ClientBatchExecuteStatementparameterSetsvalueTypeDef",
    {
        "arrayValue": ClientBatchExecuteStatementparameterSetsvaluearrayValueTypeDef,
        "blobValue": bytes,
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)


class ClientBatchExecuteStatementparameterSetsvalueTypeDef(
    _ClientBatchExecuteStatementparameterSetsvalueTypeDef
):
    """
    Type definition for `ClientBatchExecuteStatementparameterSets` `value`

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
    """


_ClientBatchExecuteStatementparameterSetsTypeDef = TypedDict(
    "_ClientBatchExecuteStatementparameterSetsTypeDef",
    {"name": str, "value": ClientBatchExecuteStatementparameterSetsvalueTypeDef},
    total=False,
)


class ClientBatchExecuteStatementparameterSetsTypeDef(
    _ClientBatchExecuteStatementparameterSetsTypeDef
):
    """
    Type definition for `ClientBatchExecuteStatement` `parameterSets`

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
    """


_ClientBeginTransactionResponseTypeDef = TypedDict(
    "_ClientBeginTransactionResponseTypeDef", {"transactionId": str}, total=False
)


class ClientBeginTransactionResponseTypeDef(_ClientBeginTransactionResponseTypeDef):
    """
    Type definition for `ClientBeginTransaction` `Response`

    The response elements represent the output of a request to start a SQL transaction.

    - **transactionId** *(string) --*

      The transaction ID of the transaction started by the call.
    """


_ClientCommitTransactionResponseTypeDef = TypedDict(
    "_ClientCommitTransactionResponseTypeDef", {"transactionStatus": str}, total=False
)


class ClientCommitTransactionResponseTypeDef(_ClientCommitTransactionResponseTypeDef):
    """
    Type definition for `ClientCommitTransaction` `Response`

    The response elements represent the output of a commit transaction request.

    - **transactionStatus** *(string) --*

      The status of the commit operation.
    """


_ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesstructValueTypeDef = TypedDict(
    "_ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesstructValueTypeDef",
    {"attributes": List[Dict]},
    total=False,
)


class ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesstructValueTypeDef(
    _ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesstructValueTypeDef
):
    """
    Type definition for `ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvalues` `structValue`

    A value for a column of STRUCT data type.

    - **attributes** *(list) --*

      The attributes returned in the record.

      - *(dict) --*

        Contains the value of a column.

         ``<important> <p>This data type is deprecated.</p> </important>``
    """


_ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesTypeDef = TypedDict(
    "_ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesTypeDef",
    {
        "arrayValues": List[Dict],
        "bigIntValue": int,
        "bitValue": bool,
        "blobValue": bytes,
        "doubleValue": float,
        "intValue": int,
        "isNull": bool,
        "realValue": float,
        "stringValue": str,
        "structValue": ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesstructValueTypeDef,
    },
    total=False,
)


class ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesTypeDef(
    _ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesTypeDef
):
    """
    Type definition for `ClientExecuteSqlResponsesqlStatementResultsresultFramerecords` `values`

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
    """


_ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsTypeDef = TypedDict(
    "_ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsTypeDef",
    {
        "values": List[
            ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsvaluesTypeDef
        ]
    },
    total=False,
)


class ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsTypeDef(
    _ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsTypeDef
):
    """
    Type definition for `ClientExecuteSqlResponsesqlStatementResultsresultFrame` `records`

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
    """


_ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadatacolumnMetadataTypeDef = TypedDict(
    "_ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadatacolumnMetadataTypeDef",
    {
        "arrayBaseColumnType": int,
        "isAutoIncrement": bool,
        "isCaseSensitive": bool,
        "isCurrency": bool,
        "isSigned": bool,
        "label": str,
        "name": str,
        "nullable": int,
        "precision": int,
        "scale": int,
        "schemaName": str,
        "tableName": str,
        "type": int,
        "typeName": str,
    },
    total=False,
)


class ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadatacolumnMetadataTypeDef(
    _ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadatacolumnMetadataTypeDef
):
    """
    Type definition for `ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadata` `columnMetadata`

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


_ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadataTypeDef = TypedDict(
    "_ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadataTypeDef",
    {
        "columnCount": int,
        "columnMetadata": List[
            ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadatacolumnMetadataTypeDef
        ],
    },
    total=False,
)


class ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadataTypeDef(
    _ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadataTypeDef
):
    """
    Type definition for `ClientExecuteSqlResponsesqlStatementResultsresultFrame` `resultSetMetadata`

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


_ClientExecuteSqlResponsesqlStatementResultsresultFrameTypeDef = TypedDict(
    "_ClientExecuteSqlResponsesqlStatementResultsresultFrameTypeDef",
    {
        "records": List[
            ClientExecuteSqlResponsesqlStatementResultsresultFramerecordsTypeDef
        ],
        "resultSetMetadata": ClientExecuteSqlResponsesqlStatementResultsresultFrameresultSetMetadataTypeDef,
    },
    total=False,
)


class ClientExecuteSqlResponsesqlStatementResultsresultFrameTypeDef(
    _ClientExecuteSqlResponsesqlStatementResultsresultFrameTypeDef
):
    """
    Type definition for `ClientExecuteSqlResponsesqlStatementResults` `resultFrame`

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


_ClientExecuteSqlResponsesqlStatementResultsTypeDef = TypedDict(
    "_ClientExecuteSqlResponsesqlStatementResultsTypeDef",
    {
        "numberOfRecordsUpdated": int,
        "resultFrame": ClientExecuteSqlResponsesqlStatementResultsresultFrameTypeDef,
    },
    total=False,
)


class ClientExecuteSqlResponsesqlStatementResultsTypeDef(
    _ClientExecuteSqlResponsesqlStatementResultsTypeDef
):
    """
    Type definition for `ClientExecuteSqlResponse` `sqlStatementResults`

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


_ClientExecuteSqlResponseTypeDef = TypedDict(
    "_ClientExecuteSqlResponseTypeDef",
    {"sqlStatementResults": List[ClientExecuteSqlResponsesqlStatementResultsTypeDef]},
    total=False,
)


class ClientExecuteSqlResponseTypeDef(_ClientExecuteSqlResponseTypeDef):
    """
    Type definition for `ClientExecuteSql` `Response`

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


_ClientExecuteStatementResponsecolumnMetadataTypeDef = TypedDict(
    "_ClientExecuteStatementResponsecolumnMetadataTypeDef",
    {
        "arrayBaseColumnType": int,
        "isAutoIncrement": bool,
        "isCaseSensitive": bool,
        "isCurrency": bool,
        "isSigned": bool,
        "label": str,
        "name": str,
        "nullable": int,
        "precision": int,
        "scale": int,
        "schemaName": str,
        "tableName": str,
        "type": int,
        "typeName": str,
    },
    total=False,
)


class ClientExecuteStatementResponsecolumnMetadataTypeDef(
    _ClientExecuteStatementResponsecolumnMetadataTypeDef
):
    """
    Type definition for `ClientExecuteStatementResponse` `columnMetadata`

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


_ClientExecuteStatementResponsegeneratedFieldsarrayValueTypeDef = TypedDict(
    "_ClientExecuteStatementResponsegeneratedFieldsarrayValueTypeDef",
    {
        "arrayValues": List[Dict],
        "booleanValues": List[bool],
        "doubleValues": List[float],
        "longValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)


class ClientExecuteStatementResponsegeneratedFieldsarrayValueTypeDef(
    _ClientExecuteStatementResponsegeneratedFieldsarrayValueTypeDef
):
    """
    Type definition for `ClientExecuteStatementResponsegeneratedFields` `arrayValue`

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
    """


_ClientExecuteStatementResponsegeneratedFieldsTypeDef = TypedDict(
    "_ClientExecuteStatementResponsegeneratedFieldsTypeDef",
    {
        "arrayValue": ClientExecuteStatementResponsegeneratedFieldsarrayValueTypeDef,
        "blobValue": bytes,
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)


class ClientExecuteStatementResponsegeneratedFieldsTypeDef(
    _ClientExecuteStatementResponsegeneratedFieldsTypeDef
):
    """
    Type definition for `ClientExecuteStatementResponse` `generatedFields`

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


_ClientExecuteStatementResponserecordsarrayValueTypeDef = TypedDict(
    "_ClientExecuteStatementResponserecordsarrayValueTypeDef",
    {
        "arrayValues": List[Dict],
        "booleanValues": List[bool],
        "doubleValues": List[float],
        "longValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)


class ClientExecuteStatementResponserecordsarrayValueTypeDef(
    _ClientExecuteStatementResponserecordsarrayValueTypeDef
):
    """
    Type definition for `ClientExecuteStatementResponserecords` `arrayValue`

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
    """


_ClientExecuteStatementResponserecordsTypeDef = TypedDict(
    "_ClientExecuteStatementResponserecordsTypeDef",
    {
        "arrayValue": ClientExecuteStatementResponserecordsarrayValueTypeDef,
        "blobValue": bytes,
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)


class ClientExecuteStatementResponserecordsTypeDef(
    _ClientExecuteStatementResponserecordsTypeDef
):
    """
    Type definition for `ClientExecuteStatementResponse` `records`

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


_ClientExecuteStatementResponseTypeDef = TypedDict(
    "_ClientExecuteStatementResponseTypeDef",
    {
        "columnMetadata": List[ClientExecuteStatementResponsecolumnMetadataTypeDef],
        "generatedFields": List[ClientExecuteStatementResponsegeneratedFieldsTypeDef],
        "numberOfRecordsUpdated": int,
        "records": List[List[ClientExecuteStatementResponserecordsTypeDef]],
    },
    total=False,
)


class ClientExecuteStatementResponseTypeDef(_ClientExecuteStatementResponseTypeDef):
    """
    Type definition for `ClientExecuteStatement` `Response`

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


_ClientExecuteStatementparametersvaluearrayValueTypeDef = TypedDict(
    "_ClientExecuteStatementparametersvaluearrayValueTypeDef",
    {
        "arrayValues": List[Dict],
        "booleanValues": List[bool],
        "doubleValues": List[float],
        "longValues": List[int],
        "stringValues": List[str],
    },
    total=False,
)


class ClientExecuteStatementparametersvaluearrayValueTypeDef(
    _ClientExecuteStatementparametersvaluearrayValueTypeDef
):
    """
    Type definition for `ClientExecuteStatementparametersvalue` `arrayValue`

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
    """


_ClientExecuteStatementparametersvalueTypeDef = TypedDict(
    "_ClientExecuteStatementparametersvalueTypeDef",
    {
        "arrayValue": ClientExecuteStatementparametersvaluearrayValueTypeDef,
        "blobValue": bytes,
        "booleanValue": bool,
        "doubleValue": float,
        "isNull": bool,
        "longValue": int,
        "stringValue": str,
    },
    total=False,
)


class ClientExecuteStatementparametersvalueTypeDef(
    _ClientExecuteStatementparametersvalueTypeDef
):
    """
    Type definition for `ClientExecuteStatementparameters` `value`

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
    """


_ClientExecuteStatementparametersTypeDef = TypedDict(
    "_ClientExecuteStatementparametersTypeDef",
    {"name": str, "value": ClientExecuteStatementparametersvalueTypeDef},
    total=False,
)


class ClientExecuteStatementparametersTypeDef(_ClientExecuteStatementparametersTypeDef):
    """
    Type definition for `ClientExecuteStatement` `parameters`

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
    """


_ClientExecuteStatementresultSetOptionsTypeDef = TypedDict(
    "_ClientExecuteStatementresultSetOptionsTypeDef",
    {"decimalReturnType": str},
    total=False,
)


class ClientExecuteStatementresultSetOptionsTypeDef(
    _ClientExecuteStatementresultSetOptionsTypeDef
):
    """
    Type definition for `ClientExecuteStatement` `resultSetOptions`

    Options that control how the result set is returned.

    - **decimalReturnType** *(string) --*

      A value that indicates how a field of ``DECIMAL`` type is represented in the response. The
      value of ``STRING`` , the default, specifies that it is converted to a String value. The value
      of ``DOUBLE_OR_LONG`` specifies that it is converted to a Long value if its scale is 0, or to a
      Double value otherwise.

      .. warning::

        Conversion to Double or Long can result in roundoff errors due to precision loss. We
        recommend converting to String, especially when working with currency values.
    """


_ClientRollbackTransactionResponseTypeDef = TypedDict(
    "_ClientRollbackTransactionResponseTypeDef", {"transactionStatus": str}, total=False
)


class ClientRollbackTransactionResponseTypeDef(
    _ClientRollbackTransactionResponseTypeDef
):
    """
    Type definition for `ClientRollbackTransaction` `Response`

    The response elements represent the output of a request to perform a rollback of a transaction.

    - **transactionStatus** *(string) --*

      The status of the rollback operation.
    """

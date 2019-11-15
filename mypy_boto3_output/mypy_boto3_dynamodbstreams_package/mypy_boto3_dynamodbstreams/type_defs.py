"Main interface for dynamodbstreams type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


_ClientDescribeStreamResponseStreamDescriptionKeySchemaTypeDef = TypedDict(
    "_ClientDescribeStreamResponseStreamDescriptionKeySchemaTypeDef",
    {"AttributeName": str, "KeyType": str},
    total=False,
)


class ClientDescribeStreamResponseStreamDescriptionKeySchemaTypeDef(
    _ClientDescribeStreamResponseStreamDescriptionKeySchemaTypeDef
):
    """
    Type definition for `ClientDescribeStreamResponseStreamDescription` `KeySchema`

    Represents *a single element* of a key schema. A key schema specifies the attributes that
    make up the primary key of a table, or the key attributes of an index.

    A ``KeySchemaElement`` represents exactly one attribute of the primary key. For example,
    a simple primary key (partition key) would be represented by one ``KeySchemaElement`` . A
    composite primary key (partition key and sort key) would require one ``KeySchemaElement``
    for the partition key, and another ``KeySchemaElement`` for the sort key.

    .. note::

      The partition key of an item is also known as its *hash attribute* . The term "hash
      attribute" derives from DynamoDB's usage of an internal hash function to evenly
      distribute data items across partitions, based on their partition key values.

      The sort key of an item is also known as its *range attribute* . The term "range
      attribute" derives from the way DynamoDB stores items with the same partition key
      physically close together, in sorted order by the sort key value.

    - **AttributeName** *(string) --*

      The name of a key attribute.

    - **KeyType** *(string) --*

      The attribute data, consisting of the data type and the attribute value itself.
    """


_ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef = TypedDict(
    "_ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef",
    {"StartingSequenceNumber": str, "EndingSequenceNumber": str},
    total=False,
)


class ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef(
    _ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef
):
    """
    Type definition for `ClientDescribeStreamResponseStreamDescriptionShards` `SequenceNumberRange`

    The range of possible sequence numbers for the shard.

    - **StartingSequenceNumber** *(string) --*

      The first sequence number.

    - **EndingSequenceNumber** *(string) --*

      The last sequence number.
    """


_ClientDescribeStreamResponseStreamDescriptionShardsTypeDef = TypedDict(
    "_ClientDescribeStreamResponseStreamDescriptionShardsTypeDef",
    {
        "ShardId": str,
        "SequenceNumberRange": ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef,
        "ParentShardId": str,
    },
    total=False,
)


class ClientDescribeStreamResponseStreamDescriptionShardsTypeDef(
    _ClientDescribeStreamResponseStreamDescriptionShardsTypeDef
):
    """
    Type definition for `ClientDescribeStreamResponseStreamDescription` `Shards`

    A uniquely identified group of stream records within a stream.

    - **ShardId** *(string) --*

      The system-generated identifier for this shard.

    - **SequenceNumberRange** *(dict) --*

      The range of possible sequence numbers for the shard.

      - **StartingSequenceNumber** *(string) --*

        The first sequence number.

      - **EndingSequenceNumber** *(string) --*

        The last sequence number.

    - **ParentShardId** *(string) --*

      The shard ID of the current shard's parent.
    """


_ClientDescribeStreamResponseStreamDescriptionTypeDef = TypedDict(
    "_ClientDescribeStreamResponseStreamDescriptionTypeDef",
    {
        "StreamArn": str,
        "StreamLabel": str,
        "StreamStatus": str,
        "StreamViewType": str,
        "CreationRequestDateTime": datetime,
        "TableName": str,
        "KeySchema": List[
            ClientDescribeStreamResponseStreamDescriptionKeySchemaTypeDef
        ],
        "Shards": List[ClientDescribeStreamResponseStreamDescriptionShardsTypeDef],
        "LastEvaluatedShardId": str,
    },
    total=False,
)


class ClientDescribeStreamResponseStreamDescriptionTypeDef(
    _ClientDescribeStreamResponseStreamDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeStreamResponse` `StreamDescription`

    A complete description of the stream, including its creation date and time, the DynamoDB
    table associated with the stream, the shard IDs within the stream, and the beginning and
    ending sequence numbers of stream records within the shards.

    - **StreamArn** *(string) --*

      The Amazon Resource Name (ARN) for the stream.

    - **StreamLabel** *(string) --*

      A timestamp, in ISO 8601 format, for this stream.

      Note that ``LatestStreamLabel`` is not a unique identifier for the stream, because it is
      possible that a stream from another table might have the same timestamp. However, the
      combination of the following three elements is guaranteed to be unique:

      * the AWS customer ID.

      * the table name

      * the ``StreamLabel``

    - **StreamStatus** *(string) --*

      Indicates the current status of the stream:

      * ``ENABLING`` - Streams is currently being enabled on the DynamoDB table.

      * ``ENABLED`` - the stream is enabled.

      * ``DISABLING`` - Streams is currently being disabled on the DynamoDB table.

      * ``DISABLED`` - the stream is disabled.

    - **StreamViewType** *(string) --*

      Indicates the format of the records within this stream:

      * ``KEYS_ONLY`` - only the key attributes of items that were modified in the DynamoDB table.

      * ``NEW_IMAGE`` - entire items from the table, as they appeared after they were modified.

      * ``OLD_IMAGE`` - entire items from the table, as they appeared before they were modified.

      * ``NEW_AND_OLD_IMAGES`` - both the new and the old images of the items from the table.

    - **CreationRequestDateTime** *(datetime) --*

      The date and time when the request to create this stream was issued.

    - **TableName** *(string) --*

      The DynamoDB table with which the stream is associated.

    - **KeySchema** *(list) --*

      The key attribute(s) of the stream's DynamoDB table.

      - *(dict) --*

        Represents *a single element* of a key schema. A key schema specifies the attributes that
        make up the primary key of a table, or the key attributes of an index.

        A ``KeySchemaElement`` represents exactly one attribute of the primary key. For example,
        a simple primary key (partition key) would be represented by one ``KeySchemaElement`` . A
        composite primary key (partition key and sort key) would require one ``KeySchemaElement``
        for the partition key, and another ``KeySchemaElement`` for the sort key.

        .. note::

          The partition key of an item is also known as its *hash attribute* . The term "hash
          attribute" derives from DynamoDB's usage of an internal hash function to evenly
          distribute data items across partitions, based on their partition key values.

          The sort key of an item is also known as its *range attribute* . The term "range
          attribute" derives from the way DynamoDB stores items with the same partition key
          physically close together, in sorted order by the sort key value.

        - **AttributeName** *(string) --*

          The name of a key attribute.

        - **KeyType** *(string) --*

          The attribute data, consisting of the data type and the attribute value itself.

    - **Shards** *(list) --*

      The shards that comprise the stream.

      - *(dict) --*

        A uniquely identified group of stream records within a stream.

        - **ShardId** *(string) --*

          The system-generated identifier for this shard.

        - **SequenceNumberRange** *(dict) --*

          The range of possible sequence numbers for the shard.

          - **StartingSequenceNumber** *(string) --*

            The first sequence number.

          - **EndingSequenceNumber** *(string) --*

            The last sequence number.

        - **ParentShardId** *(string) --*

          The shard ID of the current shard's parent.

    - **LastEvaluatedShardId** *(string) --*

      The shard ID of the item where the operation stopped, inclusive of the previous result set.
      Use this value to start a new operation, excluding this value in the new request.

      If ``LastEvaluatedShardId`` is empty, then the "last page" of results has been processed
      and there is currently no more data to be retrieved.

      If ``LastEvaluatedShardId`` is not empty, it does not necessarily mean that there is more
      data in the result set. The only way to know when you have reached the end of the result
      set is when ``LastEvaluatedShardId`` is empty.
    """


_ClientDescribeStreamResponseTypeDef = TypedDict(
    "_ClientDescribeStreamResponseTypeDef",
    {"StreamDescription": ClientDescribeStreamResponseStreamDescriptionTypeDef},
    total=False,
)


class ClientDescribeStreamResponseTypeDef(_ClientDescribeStreamResponseTypeDef):
    """
    Type definition for `ClientDescribeStream` `Response`

    Represents the output of a ``DescribeStream`` operation.

    - **StreamDescription** *(dict) --*

      A complete description of the stream, including its creation date and time, the DynamoDB
      table associated with the stream, the shard IDs within the stream, and the beginning and
      ending sequence numbers of stream records within the shards.

      - **StreamArn** *(string) --*

        The Amazon Resource Name (ARN) for the stream.

      - **StreamLabel** *(string) --*

        A timestamp, in ISO 8601 format, for this stream.

        Note that ``LatestStreamLabel`` is not a unique identifier for the stream, because it is
        possible that a stream from another table might have the same timestamp. However, the
        combination of the following three elements is guaranteed to be unique:

        * the AWS customer ID.

        * the table name

        * the ``StreamLabel``

      - **StreamStatus** *(string) --*

        Indicates the current status of the stream:

        * ``ENABLING`` - Streams is currently being enabled on the DynamoDB table.

        * ``ENABLED`` - the stream is enabled.

        * ``DISABLING`` - Streams is currently being disabled on the DynamoDB table.

        * ``DISABLED`` - the stream is disabled.

      - **StreamViewType** *(string) --*

        Indicates the format of the records within this stream:

        * ``KEYS_ONLY`` - only the key attributes of items that were modified in the DynamoDB table.

        * ``NEW_IMAGE`` - entire items from the table, as they appeared after they were modified.

        * ``OLD_IMAGE`` - entire items from the table, as they appeared before they were modified.

        * ``NEW_AND_OLD_IMAGES`` - both the new and the old images of the items from the table.

      - **CreationRequestDateTime** *(datetime) --*

        The date and time when the request to create this stream was issued.

      - **TableName** *(string) --*

        The DynamoDB table with which the stream is associated.

      - **KeySchema** *(list) --*

        The key attribute(s) of the stream's DynamoDB table.

        - *(dict) --*

          Represents *a single element* of a key schema. A key schema specifies the attributes that
          make up the primary key of a table, or the key attributes of an index.

          A ``KeySchemaElement`` represents exactly one attribute of the primary key. For example,
          a simple primary key (partition key) would be represented by one ``KeySchemaElement`` . A
          composite primary key (partition key and sort key) would require one ``KeySchemaElement``
          for the partition key, and another ``KeySchemaElement`` for the sort key.

          .. note::

            The partition key of an item is also known as its *hash attribute* . The term "hash
            attribute" derives from DynamoDB's usage of an internal hash function to evenly
            distribute data items across partitions, based on their partition key values.

            The sort key of an item is also known as its *range attribute* . The term "range
            attribute" derives from the way DynamoDB stores items with the same partition key
            physically close together, in sorted order by the sort key value.

          - **AttributeName** *(string) --*

            The name of a key attribute.

          - **KeyType** *(string) --*

            The attribute data, consisting of the data type and the attribute value itself.

      - **Shards** *(list) --*

        The shards that comprise the stream.

        - *(dict) --*

          A uniquely identified group of stream records within a stream.

          - **ShardId** *(string) --*

            The system-generated identifier for this shard.

          - **SequenceNumberRange** *(dict) --*

            The range of possible sequence numbers for the shard.

            - **StartingSequenceNumber** *(string) --*

              The first sequence number.

            - **EndingSequenceNumber** *(string) --*

              The last sequence number.

          - **ParentShardId** *(string) --*

            The shard ID of the current shard's parent.

      - **LastEvaluatedShardId** *(string) --*

        The shard ID of the item where the operation stopped, inclusive of the previous result set.
        Use this value to start a new operation, excluding this value in the new request.

        If ``LastEvaluatedShardId`` is empty, then the "last page" of results has been processed
        and there is currently no more data to be retrieved.

        If ``LastEvaluatedShardId`` is not empty, it does not necessarily mean that there is more
        data in the result set. The only way to know when you have reached the end of the result
        set is when ``LastEvaluatedShardId`` is empty.
    """


_ClientGetRecordsResponseRecordsdynamodbKeysTypeDef = TypedDict(
    "_ClientGetRecordsResponseRecordsdynamodbKeysTypeDef",
    {
        "S": str,
        "N": str,
        "B": bytes,
        "SS": List[str],
        "NS": List[str],
        "BS": List[bytes],
        "M": Dict[str, Dict],
        "L": List[Dict],
        "NULL": bool,
        "BOOL": bool,
    },
    total=False,
)


class ClientGetRecordsResponseRecordsdynamodbKeysTypeDef(
    _ClientGetRecordsResponseRecordsdynamodbKeysTypeDef
):
    """
    Type definition for `ClientGetRecordsResponseRecordsdynamodb` `Keys`

    Represents the data for an attribute. You can set one, and only one, of the
    elements.

    Each attribute in an item is a name-value pair. An attribute can be single-valued
    or multi-valued set. For example, a book item can have title and authors
    attributes. Each book has one title but can have many authors. The multi-valued
    attribute is a set; duplicate values are not allowed.

    - **S** *(string) --*

      A String data type.

    - **N** *(string) --*

      A Number data type.

    - **B** *(bytes) --*

      A Binary data type.

    - **SS** *(list) --*

      A String Set data type.

      - *(string) --*

    - **NS** *(list) --*

      A Number Set data type.

      - *(string) --*

    - **BS** *(list) --*

      A Binary Set data type.

      - *(bytes) --*

    - **M** *(dict) --*

      A Map data type.

      - *(string) --*

        - *(dict) --*

          Represents the data for an attribute. You can set one, and only one, of the
          elements.

          Each attribute in an item is a name-value pair. An attribute can be
          single-valued or multi-valued set. For example, a book item can have title
          and authors attributes. Each book has one title but can have many authors.
          The multi-valued attribute is a set; duplicate values are not allowed.

    - **L** *(list) --*

      A List data type.

      - *(dict) --*

        Represents the data for an attribute. You can set one, and only one, of the
        elements.

        Each attribute in an item is a name-value pair. An attribute can be
        single-valued or multi-valued set. For example, a book item can have title and
        authors attributes. Each book has one title but can have many authors. The
        multi-valued attribute is a set; duplicate values are not allowed.

    - **NULL** *(boolean) --*

      A Null data type.

    - **BOOL** *(boolean) --*

      A Boolean data type.
    """


_ClientGetRecordsResponseRecordsdynamodbNewImageTypeDef = TypedDict(
    "_ClientGetRecordsResponseRecordsdynamodbNewImageTypeDef",
    {
        "S": str,
        "N": str,
        "B": bytes,
        "SS": List[str],
        "NS": List[str],
        "BS": List[bytes],
        "M": Dict[str, Dict],
        "L": List[Dict],
        "NULL": bool,
        "BOOL": bool,
    },
    total=False,
)


class ClientGetRecordsResponseRecordsdynamodbNewImageTypeDef(
    _ClientGetRecordsResponseRecordsdynamodbNewImageTypeDef
):
    """
    Type definition for `ClientGetRecordsResponseRecordsdynamodb` `NewImage`

    Represents the data for an attribute. You can set one, and only one, of the
    elements.

    Each attribute in an item is a name-value pair. An attribute can be single-valued
    or multi-valued set. For example, a book item can have title and authors
    attributes. Each book has one title but can have many authors. The multi-valued
    attribute is a set; duplicate values are not allowed.

    - **S** *(string) --*

      A String data type.

    - **N** *(string) --*

      A Number data type.

    - **B** *(bytes) --*

      A Binary data type.

    - **SS** *(list) --*

      A String Set data type.

      - *(string) --*

    - **NS** *(list) --*

      A Number Set data type.

      - *(string) --*

    - **BS** *(list) --*

      A Binary Set data type.

      - *(bytes) --*

    - **M** *(dict) --*

      A Map data type.

      - *(string) --*

        - *(dict) --*

          Represents the data for an attribute. You can set one, and only one, of the
          elements.

          Each attribute in an item is a name-value pair. An attribute can be
          single-valued or multi-valued set. For example, a book item can have title
          and authors attributes. Each book has one title but can have many authors.
          The multi-valued attribute is a set; duplicate values are not allowed.

    - **L** *(list) --*

      A List data type.

      - *(dict) --*

        Represents the data for an attribute. You can set one, and only one, of the
        elements.

        Each attribute in an item is a name-value pair. An attribute can be
        single-valued or multi-valued set. For example, a book item can have title and
        authors attributes. Each book has one title but can have many authors. The
        multi-valued attribute is a set; duplicate values are not allowed.

    - **NULL** *(boolean) --*

      A Null data type.

    - **BOOL** *(boolean) --*

      A Boolean data type.
    """


_ClientGetRecordsResponseRecordsdynamodbOldImageTypeDef = TypedDict(
    "_ClientGetRecordsResponseRecordsdynamodbOldImageTypeDef",
    {
        "S": str,
        "N": str,
        "B": bytes,
        "SS": List[str],
        "NS": List[str],
        "BS": List[bytes],
        "M": Dict[str, Dict],
        "L": List[Dict],
        "NULL": bool,
        "BOOL": bool,
    },
    total=False,
)


class ClientGetRecordsResponseRecordsdynamodbOldImageTypeDef(
    _ClientGetRecordsResponseRecordsdynamodbOldImageTypeDef
):
    """
    Type definition for `ClientGetRecordsResponseRecordsdynamodb` `OldImage`

    Represents the data for an attribute. You can set one, and only one, of the
    elements.

    Each attribute in an item is a name-value pair. An attribute can be single-valued
    or multi-valued set. For example, a book item can have title and authors
    attributes. Each book has one title but can have many authors. The multi-valued
    attribute is a set; duplicate values are not allowed.

    - **S** *(string) --*

      A String data type.

    - **N** *(string) --*

      A Number data type.

    - **B** *(bytes) --*

      A Binary data type.

    - **SS** *(list) --*

      A String Set data type.

      - *(string) --*

    - **NS** *(list) --*

      A Number Set data type.

      - *(string) --*

    - **BS** *(list) --*

      A Binary Set data type.

      - *(bytes) --*

    - **M** *(dict) --*

      A Map data type.

      - *(string) --*

        - *(dict) --*

          Represents the data for an attribute. You can set one, and only one, of the
          elements.

          Each attribute in an item is a name-value pair. An attribute can be
          single-valued or multi-valued set. For example, a book item can have title
          and authors attributes. Each book has one title but can have many authors.
          The multi-valued attribute is a set; duplicate values are not allowed.

    - **L** *(list) --*

      A List data type.

      - *(dict) --*

        Represents the data for an attribute. You can set one, and only one, of the
        elements.

        Each attribute in an item is a name-value pair. An attribute can be
        single-valued or multi-valued set. For example, a book item can have title and
        authors attributes. Each book has one title but can have many authors. The
        multi-valued attribute is a set; duplicate values are not allowed.

    - **NULL** *(boolean) --*

      A Null data type.

    - **BOOL** *(boolean) --*

      A Boolean data type.
    """


_ClientGetRecordsResponseRecordsdynamodbTypeDef = TypedDict(
    "_ClientGetRecordsResponseRecordsdynamodbTypeDef",
    {
        "ApproximateCreationDateTime": datetime,
        "Keys": Dict[str, ClientGetRecordsResponseRecordsdynamodbKeysTypeDef],
        "NewImage": Dict[str, ClientGetRecordsResponseRecordsdynamodbNewImageTypeDef],
        "OldImage": Dict[str, ClientGetRecordsResponseRecordsdynamodbOldImageTypeDef],
        "SequenceNumber": str,
        "SizeBytes": int,
        "StreamViewType": str,
    },
    total=False,
)


class ClientGetRecordsResponseRecordsdynamodbTypeDef(
    _ClientGetRecordsResponseRecordsdynamodbTypeDef
):
    """
    Type definition for `ClientGetRecordsResponseRecords` `dynamodb`

    The main body of the stream record, containing all of the DynamoDB-specific fields.

    - **ApproximateCreationDateTime** *(datetime) --*

      The approximate date and time when the stream record was created, in `UNIX epoch time
      <http://www.epochconverter.com/>`__ format.

    - **Keys** *(dict) --*

      The primary key attribute(s) for the DynamoDB item that was modified.

      - *(string) --*

        - *(dict) --*

          Represents the data for an attribute. You can set one, and only one, of the
          elements.

          Each attribute in an item is a name-value pair. An attribute can be single-valued
          or multi-valued set. For example, a book item can have title and authors
          attributes. Each book has one title but can have many authors. The multi-valued
          attribute is a set; duplicate values are not allowed.

          - **S** *(string) --*

            A String data type.

          - **N** *(string) --*

            A Number data type.

          - **B** *(bytes) --*

            A Binary data type.

          - **SS** *(list) --*

            A String Set data type.

            - *(string) --*

          - **NS** *(list) --*

            A Number Set data type.

            - *(string) --*

          - **BS** *(list) --*

            A Binary Set data type.

            - *(bytes) --*

          - **M** *(dict) --*

            A Map data type.

            - *(string) --*

              - *(dict) --*

                Represents the data for an attribute. You can set one, and only one, of the
                elements.

                Each attribute in an item is a name-value pair. An attribute can be
                single-valued or multi-valued set. For example, a book item can have title
                and authors attributes. Each book has one title but can have many authors.
                The multi-valued attribute is a set; duplicate values are not allowed.

          - **L** *(list) --*

            A List data type.

            - *(dict) --*

              Represents the data for an attribute. You can set one, and only one, of the
              elements.

              Each attribute in an item is a name-value pair. An attribute can be
              single-valued or multi-valued set. For example, a book item can have title and
              authors attributes. Each book has one title but can have many authors. The
              multi-valued attribute is a set; duplicate values are not allowed.

          - **NULL** *(boolean) --*

            A Null data type.

          - **BOOL** *(boolean) --*

            A Boolean data type.

    - **NewImage** *(dict) --*

      The item in the DynamoDB table as it appeared after it was modified.

      - *(string) --*

        - *(dict) --*

          Represents the data for an attribute. You can set one, and only one, of the
          elements.

          Each attribute in an item is a name-value pair. An attribute can be single-valued
          or multi-valued set. For example, a book item can have title and authors
          attributes. Each book has one title but can have many authors. The multi-valued
          attribute is a set; duplicate values are not allowed.

          - **S** *(string) --*

            A String data type.

          - **N** *(string) --*

            A Number data type.

          - **B** *(bytes) --*

            A Binary data type.

          - **SS** *(list) --*

            A String Set data type.

            - *(string) --*

          - **NS** *(list) --*

            A Number Set data type.

            - *(string) --*

          - **BS** *(list) --*

            A Binary Set data type.

            - *(bytes) --*

          - **M** *(dict) --*

            A Map data type.

            - *(string) --*

              - *(dict) --*

                Represents the data for an attribute. You can set one, and only one, of the
                elements.

                Each attribute in an item is a name-value pair. An attribute can be
                single-valued or multi-valued set. For example, a book item can have title
                and authors attributes. Each book has one title but can have many authors.
                The multi-valued attribute is a set; duplicate values are not allowed.

          - **L** *(list) --*

            A List data type.

            - *(dict) --*

              Represents the data for an attribute. You can set one, and only one, of the
              elements.

              Each attribute in an item is a name-value pair. An attribute can be
              single-valued or multi-valued set. For example, a book item can have title and
              authors attributes. Each book has one title but can have many authors. The
              multi-valued attribute is a set; duplicate values are not allowed.

          - **NULL** *(boolean) --*

            A Null data type.

          - **BOOL** *(boolean) --*

            A Boolean data type.

    - **OldImage** *(dict) --*

      The item in the DynamoDB table as it appeared before it was modified.

      - *(string) --*

        - *(dict) --*

          Represents the data for an attribute. You can set one, and only one, of the
          elements.

          Each attribute in an item is a name-value pair. An attribute can be single-valued
          or multi-valued set. For example, a book item can have title and authors
          attributes. Each book has one title but can have many authors. The multi-valued
          attribute is a set; duplicate values are not allowed.

          - **S** *(string) --*

            A String data type.

          - **N** *(string) --*

            A Number data type.

          - **B** *(bytes) --*

            A Binary data type.

          - **SS** *(list) --*

            A String Set data type.

            - *(string) --*

          - **NS** *(list) --*

            A Number Set data type.

            - *(string) --*

          - **BS** *(list) --*

            A Binary Set data type.

            - *(bytes) --*

          - **M** *(dict) --*

            A Map data type.

            - *(string) --*

              - *(dict) --*

                Represents the data for an attribute. You can set one, and only one, of the
                elements.

                Each attribute in an item is a name-value pair. An attribute can be
                single-valued or multi-valued set. For example, a book item can have title
                and authors attributes. Each book has one title but can have many authors.
                The multi-valued attribute is a set; duplicate values are not allowed.

          - **L** *(list) --*

            A List data type.

            - *(dict) --*

              Represents the data for an attribute. You can set one, and only one, of the
              elements.

              Each attribute in an item is a name-value pair. An attribute can be
              single-valued or multi-valued set. For example, a book item can have title and
              authors attributes. Each book has one title but can have many authors. The
              multi-valued attribute is a set; duplicate values are not allowed.

          - **NULL** *(boolean) --*

            A Null data type.

          - **BOOL** *(boolean) --*

            A Boolean data type.

    - **SequenceNumber** *(string) --*

      The sequence number of the stream record.

    - **SizeBytes** *(integer) --*

      The size of the stream record, in bytes.

    - **StreamViewType** *(string) --*

      The type of data from the modified DynamoDB item that was captured in this stream
      record:

      * ``KEYS_ONLY`` - only the key attributes of the modified item.

      * ``NEW_IMAGE`` - the entire item, as it appeared after it was modified.

      * ``OLD_IMAGE`` - the entire item, as it appeared before it was modified.

      * ``NEW_AND_OLD_IMAGES`` - both the new and the old item images of the item.
    """


_ClientGetRecordsResponseRecordsuserIdentityTypeDef = TypedDict(
    "_ClientGetRecordsResponseRecordsuserIdentityTypeDef",
    {"PrincipalId": str, "Type": str},
    total=False,
)


class ClientGetRecordsResponseRecordsuserIdentityTypeDef(
    _ClientGetRecordsResponseRecordsuserIdentityTypeDef
):
    """
    Type definition for `ClientGetRecordsResponseRecords` `userIdentity`

    Items that are deleted by the Time to Live process after expiration have the following
    fields:

    * Records[].userIdentity.type "Service"

    * Records[].userIdentity.principalId "dynamodb.amazonaws.com"

    - **PrincipalId** *(string) --*

      A unique identifier for the entity that made the call. For Time To Live, the
      principalId is "dynamodb.amazonaws.com".

    - **Type** *(string) --*

      The type of the identity. For Time To Live, the type is "Service".
    """


_ClientGetRecordsResponseRecordsTypeDef = TypedDict(
    "_ClientGetRecordsResponseRecordsTypeDef",
    {
        "eventID": str,
        "eventName": str,
        "eventVersion": str,
        "eventSource": str,
        "awsRegion": str,
        "dynamodb": ClientGetRecordsResponseRecordsdynamodbTypeDef,
        "userIdentity": ClientGetRecordsResponseRecordsuserIdentityTypeDef,
    },
    total=False,
)


class ClientGetRecordsResponseRecordsTypeDef(_ClientGetRecordsResponseRecordsTypeDef):
    """
    Type definition for `ClientGetRecordsResponse` `Records`

    A description of a unique event within a stream.

    - **eventID** *(string) --*

      A globally unique identifier for the event that was recorded in this stream record.

    - **eventName** *(string) --*

      The type of data modification that was performed on the DynamoDB table:

      * ``INSERT`` - a new item was added to the table.

      * ``MODIFY`` - one or more of an existing item's attributes were modified.

      * ``REMOVE`` - the item was deleted from the table

    - **eventVersion** *(string) --*

      The version number of the stream record format. This number is updated whenever the
      structure of ``Record`` is modified.

      Client applications must not assume that ``eventVersion`` will remain at a particular
      value, as this number is subject to change at any time. In general, ``eventVersion`` will
      only increase as the low-level DynamoDB Streams API evolves.

    - **eventSource** *(string) --*

      The AWS service from which the stream record originated. For DynamoDB Streams, this is
      ``aws:dynamodb`` .

    - **awsRegion** *(string) --*

      The region in which the ``GetRecords`` request was received.

    - **dynamodb** *(dict) --*

      The main body of the stream record, containing all of the DynamoDB-specific fields.

      - **ApproximateCreationDateTime** *(datetime) --*

        The approximate date and time when the stream record was created, in `UNIX epoch time
        <http://www.epochconverter.com/>`__ format.

      - **Keys** *(dict) --*

        The primary key attribute(s) for the DynamoDB item that was modified.

        - *(string) --*

          - *(dict) --*

            Represents the data for an attribute. You can set one, and only one, of the
            elements.

            Each attribute in an item is a name-value pair. An attribute can be single-valued
            or multi-valued set. For example, a book item can have title and authors
            attributes. Each book has one title but can have many authors. The multi-valued
            attribute is a set; duplicate values are not allowed.

            - **S** *(string) --*

              A String data type.

            - **N** *(string) --*

              A Number data type.

            - **B** *(bytes) --*

              A Binary data type.

            - **SS** *(list) --*

              A String Set data type.

              - *(string) --*

            - **NS** *(list) --*

              A Number Set data type.

              - *(string) --*

            - **BS** *(list) --*

              A Binary Set data type.

              - *(bytes) --*

            - **M** *(dict) --*

              A Map data type.

              - *(string) --*

                - *(dict) --*

                  Represents the data for an attribute. You can set one, and only one, of the
                  elements.

                  Each attribute in an item is a name-value pair. An attribute can be
                  single-valued or multi-valued set. For example, a book item can have title
                  and authors attributes. Each book has one title but can have many authors.
                  The multi-valued attribute is a set; duplicate values are not allowed.

            - **L** *(list) --*

              A List data type.

              - *(dict) --*

                Represents the data for an attribute. You can set one, and only one, of the
                elements.

                Each attribute in an item is a name-value pair. An attribute can be
                single-valued or multi-valued set. For example, a book item can have title and
                authors attributes. Each book has one title but can have many authors. The
                multi-valued attribute is a set; duplicate values are not allowed.

            - **NULL** *(boolean) --*

              A Null data type.

            - **BOOL** *(boolean) --*

              A Boolean data type.

      - **NewImage** *(dict) --*

        The item in the DynamoDB table as it appeared after it was modified.

        - *(string) --*

          - *(dict) --*

            Represents the data for an attribute. You can set one, and only one, of the
            elements.

            Each attribute in an item is a name-value pair. An attribute can be single-valued
            or multi-valued set. For example, a book item can have title and authors
            attributes. Each book has one title but can have many authors. The multi-valued
            attribute is a set; duplicate values are not allowed.

            - **S** *(string) --*

              A String data type.

            - **N** *(string) --*

              A Number data type.

            - **B** *(bytes) --*

              A Binary data type.

            - **SS** *(list) --*

              A String Set data type.

              - *(string) --*

            - **NS** *(list) --*

              A Number Set data type.

              - *(string) --*

            - **BS** *(list) --*

              A Binary Set data type.

              - *(bytes) --*

            - **M** *(dict) --*

              A Map data type.

              - *(string) --*

                - *(dict) --*

                  Represents the data for an attribute. You can set one, and only one, of the
                  elements.

                  Each attribute in an item is a name-value pair. An attribute can be
                  single-valued or multi-valued set. For example, a book item can have title
                  and authors attributes. Each book has one title but can have many authors.
                  The multi-valued attribute is a set; duplicate values are not allowed.

            - **L** *(list) --*

              A List data type.

              - *(dict) --*

                Represents the data for an attribute. You can set one, and only one, of the
                elements.

                Each attribute in an item is a name-value pair. An attribute can be
                single-valued or multi-valued set. For example, a book item can have title and
                authors attributes. Each book has one title but can have many authors. The
                multi-valued attribute is a set; duplicate values are not allowed.

            - **NULL** *(boolean) --*

              A Null data type.

            - **BOOL** *(boolean) --*

              A Boolean data type.

      - **OldImage** *(dict) --*

        The item in the DynamoDB table as it appeared before it was modified.

        - *(string) --*

          - *(dict) --*

            Represents the data for an attribute. You can set one, and only one, of the
            elements.

            Each attribute in an item is a name-value pair. An attribute can be single-valued
            or multi-valued set. For example, a book item can have title and authors
            attributes. Each book has one title but can have many authors. The multi-valued
            attribute is a set; duplicate values are not allowed.

            - **S** *(string) --*

              A String data type.

            - **N** *(string) --*

              A Number data type.

            - **B** *(bytes) --*

              A Binary data type.

            - **SS** *(list) --*

              A String Set data type.

              - *(string) --*

            - **NS** *(list) --*

              A Number Set data type.

              - *(string) --*

            - **BS** *(list) --*

              A Binary Set data type.

              - *(bytes) --*

            - **M** *(dict) --*

              A Map data type.

              - *(string) --*

                - *(dict) --*

                  Represents the data for an attribute. You can set one, and only one, of the
                  elements.

                  Each attribute in an item is a name-value pair. An attribute can be
                  single-valued or multi-valued set. For example, a book item can have title
                  and authors attributes. Each book has one title but can have many authors.
                  The multi-valued attribute is a set; duplicate values are not allowed.

            - **L** *(list) --*

              A List data type.

              - *(dict) --*

                Represents the data for an attribute. You can set one, and only one, of the
                elements.

                Each attribute in an item is a name-value pair. An attribute can be
                single-valued or multi-valued set. For example, a book item can have title and
                authors attributes. Each book has one title but can have many authors. The
                multi-valued attribute is a set; duplicate values are not allowed.

            - **NULL** *(boolean) --*

              A Null data type.

            - **BOOL** *(boolean) --*

              A Boolean data type.

      - **SequenceNumber** *(string) --*

        The sequence number of the stream record.

      - **SizeBytes** *(integer) --*

        The size of the stream record, in bytes.

      - **StreamViewType** *(string) --*

        The type of data from the modified DynamoDB item that was captured in this stream
        record:

        * ``KEYS_ONLY`` - only the key attributes of the modified item.

        * ``NEW_IMAGE`` - the entire item, as it appeared after it was modified.

        * ``OLD_IMAGE`` - the entire item, as it appeared before it was modified.

        * ``NEW_AND_OLD_IMAGES`` - both the new and the old item images of the item.

    - **userIdentity** *(dict) --*

      Items that are deleted by the Time to Live process after expiration have the following
      fields:

      * Records[].userIdentity.type "Service"

      * Records[].userIdentity.principalId "dynamodb.amazonaws.com"

      - **PrincipalId** *(string) --*

        A unique identifier for the entity that made the call. For Time To Live, the
        principalId is "dynamodb.amazonaws.com".

      - **Type** *(string) --*

        The type of the identity. For Time To Live, the type is "Service".
    """


_ClientGetRecordsResponseTypeDef = TypedDict(
    "_ClientGetRecordsResponseTypeDef",
    {"Records": List[ClientGetRecordsResponseRecordsTypeDef], "NextShardIterator": str},
    total=False,
)


class ClientGetRecordsResponseTypeDef(_ClientGetRecordsResponseTypeDef):
    """
    Type definition for `ClientGetRecords` `Response`

    Represents the output of a ``GetRecords`` operation.

    - **Records** *(list) --*

      The stream records from the shard, which were retrieved using the shard iterator.

      - *(dict) --*

        A description of a unique event within a stream.

        - **eventID** *(string) --*

          A globally unique identifier for the event that was recorded in this stream record.

        - **eventName** *(string) --*

          The type of data modification that was performed on the DynamoDB table:

          * ``INSERT`` - a new item was added to the table.

          * ``MODIFY`` - one or more of an existing item's attributes were modified.

          * ``REMOVE`` - the item was deleted from the table

        - **eventVersion** *(string) --*

          The version number of the stream record format. This number is updated whenever the
          structure of ``Record`` is modified.

          Client applications must not assume that ``eventVersion`` will remain at a particular
          value, as this number is subject to change at any time. In general, ``eventVersion`` will
          only increase as the low-level DynamoDB Streams API evolves.

        - **eventSource** *(string) --*

          The AWS service from which the stream record originated. For DynamoDB Streams, this is
          ``aws:dynamodb`` .

        - **awsRegion** *(string) --*

          The region in which the ``GetRecords`` request was received.

        - **dynamodb** *(dict) --*

          The main body of the stream record, containing all of the DynamoDB-specific fields.

          - **ApproximateCreationDateTime** *(datetime) --*

            The approximate date and time when the stream record was created, in `UNIX epoch time
            <http://www.epochconverter.com/>`__ format.

          - **Keys** *(dict) --*

            The primary key attribute(s) for the DynamoDB item that was modified.

            - *(string) --*

              - *(dict) --*

                Represents the data for an attribute. You can set one, and only one, of the
                elements.

                Each attribute in an item is a name-value pair. An attribute can be single-valued
                or multi-valued set. For example, a book item can have title and authors
                attributes. Each book has one title but can have many authors. The multi-valued
                attribute is a set; duplicate values are not allowed.

                - **S** *(string) --*

                  A String data type.

                - **N** *(string) --*

                  A Number data type.

                - **B** *(bytes) --*

                  A Binary data type.

                - **SS** *(list) --*

                  A String Set data type.

                  - *(string) --*

                - **NS** *(list) --*

                  A Number Set data type.

                  - *(string) --*

                - **BS** *(list) --*

                  A Binary Set data type.

                  - *(bytes) --*

                - **M** *(dict) --*

                  A Map data type.

                  - *(string) --*

                    - *(dict) --*

                      Represents the data for an attribute. You can set one, and only one, of the
                      elements.

                      Each attribute in an item is a name-value pair. An attribute can be
                      single-valued or multi-valued set. For example, a book item can have title
                      and authors attributes. Each book has one title but can have many authors.
                      The multi-valued attribute is a set; duplicate values are not allowed.

                - **L** *(list) --*

                  A List data type.

                  - *(dict) --*

                    Represents the data for an attribute. You can set one, and only one, of the
                    elements.

                    Each attribute in an item is a name-value pair. An attribute can be
                    single-valued or multi-valued set. For example, a book item can have title and
                    authors attributes. Each book has one title but can have many authors. The
                    multi-valued attribute is a set; duplicate values are not allowed.

                - **NULL** *(boolean) --*

                  A Null data type.

                - **BOOL** *(boolean) --*

                  A Boolean data type.

          - **NewImage** *(dict) --*

            The item in the DynamoDB table as it appeared after it was modified.

            - *(string) --*

              - *(dict) --*

                Represents the data for an attribute. You can set one, and only one, of the
                elements.

                Each attribute in an item is a name-value pair. An attribute can be single-valued
                or multi-valued set. For example, a book item can have title and authors
                attributes. Each book has one title but can have many authors. The multi-valued
                attribute is a set; duplicate values are not allowed.

                - **S** *(string) --*

                  A String data type.

                - **N** *(string) --*

                  A Number data type.

                - **B** *(bytes) --*

                  A Binary data type.

                - **SS** *(list) --*

                  A String Set data type.

                  - *(string) --*

                - **NS** *(list) --*

                  A Number Set data type.

                  - *(string) --*

                - **BS** *(list) --*

                  A Binary Set data type.

                  - *(bytes) --*

                - **M** *(dict) --*

                  A Map data type.

                  - *(string) --*

                    - *(dict) --*

                      Represents the data for an attribute. You can set one, and only one, of the
                      elements.

                      Each attribute in an item is a name-value pair. An attribute can be
                      single-valued or multi-valued set. For example, a book item can have title
                      and authors attributes. Each book has one title but can have many authors.
                      The multi-valued attribute is a set; duplicate values are not allowed.

                - **L** *(list) --*

                  A List data type.

                  - *(dict) --*

                    Represents the data for an attribute. You can set one, and only one, of the
                    elements.

                    Each attribute in an item is a name-value pair. An attribute can be
                    single-valued or multi-valued set. For example, a book item can have title and
                    authors attributes. Each book has one title but can have many authors. The
                    multi-valued attribute is a set; duplicate values are not allowed.

                - **NULL** *(boolean) --*

                  A Null data type.

                - **BOOL** *(boolean) --*

                  A Boolean data type.

          - **OldImage** *(dict) --*

            The item in the DynamoDB table as it appeared before it was modified.

            - *(string) --*

              - *(dict) --*

                Represents the data for an attribute. You can set one, and only one, of the
                elements.

                Each attribute in an item is a name-value pair. An attribute can be single-valued
                or multi-valued set. For example, a book item can have title and authors
                attributes. Each book has one title but can have many authors. The multi-valued
                attribute is a set; duplicate values are not allowed.

                - **S** *(string) --*

                  A String data type.

                - **N** *(string) --*

                  A Number data type.

                - **B** *(bytes) --*

                  A Binary data type.

                - **SS** *(list) --*

                  A String Set data type.

                  - *(string) --*

                - **NS** *(list) --*

                  A Number Set data type.

                  - *(string) --*

                - **BS** *(list) --*

                  A Binary Set data type.

                  - *(bytes) --*

                - **M** *(dict) --*

                  A Map data type.

                  - *(string) --*

                    - *(dict) --*

                      Represents the data for an attribute. You can set one, and only one, of the
                      elements.

                      Each attribute in an item is a name-value pair. An attribute can be
                      single-valued or multi-valued set. For example, a book item can have title
                      and authors attributes. Each book has one title but can have many authors.
                      The multi-valued attribute is a set; duplicate values are not allowed.

                - **L** *(list) --*

                  A List data type.

                  - *(dict) --*

                    Represents the data for an attribute. You can set one, and only one, of the
                    elements.

                    Each attribute in an item is a name-value pair. An attribute can be
                    single-valued or multi-valued set. For example, a book item can have title and
                    authors attributes. Each book has one title but can have many authors. The
                    multi-valued attribute is a set; duplicate values are not allowed.

                - **NULL** *(boolean) --*

                  A Null data type.

                - **BOOL** *(boolean) --*

                  A Boolean data type.

          - **SequenceNumber** *(string) --*

            The sequence number of the stream record.

          - **SizeBytes** *(integer) --*

            The size of the stream record, in bytes.

          - **StreamViewType** *(string) --*

            The type of data from the modified DynamoDB item that was captured in this stream
            record:

            * ``KEYS_ONLY`` - only the key attributes of the modified item.

            * ``NEW_IMAGE`` - the entire item, as it appeared after it was modified.

            * ``OLD_IMAGE`` - the entire item, as it appeared before it was modified.

            * ``NEW_AND_OLD_IMAGES`` - both the new and the old item images of the item.

        - **userIdentity** *(dict) --*

          Items that are deleted by the Time to Live process after expiration have the following
          fields:

          * Records[].userIdentity.type "Service"

          * Records[].userIdentity.principalId "dynamodb.amazonaws.com"

          - **PrincipalId** *(string) --*

            A unique identifier for the entity that made the call. For Time To Live, the
            principalId is "dynamodb.amazonaws.com".

          - **Type** *(string) --*

            The type of the identity. For Time To Live, the type is "Service".

    - **NextShardIterator** *(string) --*

      The next position in the shard from which to start sequentially reading stream records. If
      set to ``null`` , the shard has been closed and the requested iterator will not return any
      more data.
    """


_ClientGetShardIteratorResponseTypeDef = TypedDict(
    "_ClientGetShardIteratorResponseTypeDef", {"ShardIterator": str}, total=False
)


class ClientGetShardIteratorResponseTypeDef(_ClientGetShardIteratorResponseTypeDef):
    """
    Type definition for `ClientGetShardIterator` `Response`

    Represents the output of a ``GetShardIterator`` operation.

    - **ShardIterator** *(string) --*

      The position in the shard from which to start reading stream records sequentially. A shard
      iterator specifies this position using the sequence number of a stream record in a shard.
    """


_ClientListStreamsResponseStreamsTypeDef = TypedDict(
    "_ClientListStreamsResponseStreamsTypeDef",
    {"StreamArn": str, "TableName": str, "StreamLabel": str},
    total=False,
)


class ClientListStreamsResponseStreamsTypeDef(_ClientListStreamsResponseStreamsTypeDef):
    """
    Type definition for `ClientListStreamsResponse` `Streams`

    Represents all of the data describing a particular stream.

    - **StreamArn** *(string) --*

      The Amazon Resource Name (ARN) for the stream.

    - **TableName** *(string) --*

      The DynamoDB table with which the stream is associated.

    - **StreamLabel** *(string) --*

      A timestamp, in ISO 8601 format, for this stream.

      Note that ``LatestStreamLabel`` is not a unique identifier for the stream, because it is
      possible that a stream from another table might have the same timestamp. However, the
      combination of the following three elements is guaranteed to be unique:

      * the AWS customer ID.

      * the table name

      * the ``StreamLabel``
    """


_ClientListStreamsResponseTypeDef = TypedDict(
    "_ClientListStreamsResponseTypeDef",
    {
        "Streams": List[ClientListStreamsResponseStreamsTypeDef],
        "LastEvaluatedStreamArn": str,
    },
    total=False,
)


class ClientListStreamsResponseTypeDef(_ClientListStreamsResponseTypeDef):
    """
    Type definition for `ClientListStreams` `Response`

    Represents the output of a ``ListStreams`` operation.

    - **Streams** *(list) --*

      A list of stream descriptors associated with the current account and endpoint.

      - *(dict) --*

        Represents all of the data describing a particular stream.

        - **StreamArn** *(string) --*

          The Amazon Resource Name (ARN) for the stream.

        - **TableName** *(string) --*

          The DynamoDB table with which the stream is associated.

        - **StreamLabel** *(string) --*

          A timestamp, in ISO 8601 format, for this stream.

          Note that ``LatestStreamLabel`` is not a unique identifier for the stream, because it is
          possible that a stream from another table might have the same timestamp. However, the
          combination of the following three elements is guaranteed to be unique:

          * the AWS customer ID.

          * the table name

          * the ``StreamLabel``

    - **LastEvaluatedStreamArn** *(string) --*

      The stream ARN of the item where the operation stopped, inclusive of the previous result set.
      Use this value to start a new operation, excluding this value in the new request.

      If ``LastEvaluatedStreamArn`` is empty, then the "last page" of results has been processed
      and there is no more data to be retrieved.

      If ``LastEvaluatedStreamArn`` is not empty, it does not necessarily mean that there is more
      data in the result set. The only way to know when you have reached the end of the result set
      is when ``LastEvaluatedStreamArn`` is empty.
    """

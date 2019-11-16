"Main interface for kinesis type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientDescribeLimitsResponseTypeDef",
    "ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef",
    "ClientDescribeStreamConsumerResponseTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionEnhancedMonitoringTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionShardsTypeDef",
    "ClientDescribeStreamResponseStreamDescriptionTypeDef",
    "ClientDescribeStreamResponseTypeDef",
    "ClientDescribeStreamSummaryResponseStreamDescriptionSummaryEnhancedMonitoringTypeDef",
    "ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef",
    "ClientDescribeStreamSummaryResponseTypeDef",
    "ClientDisableEnhancedMonitoringResponseTypeDef",
    "ClientEnableEnhancedMonitoringResponseTypeDef",
    "ClientGetRecordsResponseRecordsTypeDef",
    "ClientGetRecordsResponseTypeDef",
    "ClientGetShardIteratorResponseTypeDef",
    "ClientListShardsResponseShardsHashKeyRangeTypeDef",
    "ClientListShardsResponseShardsSequenceNumberRangeTypeDef",
    "ClientListShardsResponseShardsTypeDef",
    "ClientListShardsResponseTypeDef",
    "ClientListStreamConsumersResponseConsumersTypeDef",
    "ClientListStreamConsumersResponseTypeDef",
    "ClientListStreamsResponseTypeDef",
    "ClientListTagsForStreamResponseTagsTypeDef",
    "ClientListTagsForStreamResponseTypeDef",
    "ClientPutRecordResponseTypeDef",
    "ClientPutRecordsRecordsTypeDef",
    "ClientPutRecordsResponseRecordsTypeDef",
    "ClientPutRecordsResponseTypeDef",
    "ClientRegisterStreamConsumerResponseConsumerTypeDef",
    "ClientRegisterStreamConsumerResponseTypeDef",
    "ClientSubscribeToShardStartingPositionTypeDef",
    "ClientUpdateShardCountResponseTypeDef",
    "DescribeStreamPaginatePaginationConfigTypeDef",
    "DescribeStreamPaginateResponseStreamDescriptionEnhancedMonitoringTypeDef",
    "DescribeStreamPaginateResponseStreamDescriptionShardsHashKeyRangeTypeDef",
    "DescribeStreamPaginateResponseStreamDescriptionShardsSequenceNumberRangeTypeDef",
    "DescribeStreamPaginateResponseStreamDescriptionShardsTypeDef",
    "DescribeStreamPaginateResponseStreamDescriptionTypeDef",
    "DescribeStreamPaginateResponseTypeDef",
    "ListShardsPaginatePaginationConfigTypeDef",
    "ListShardsPaginateResponseShardsHashKeyRangeTypeDef",
    "ListShardsPaginateResponseShardsSequenceNumberRangeTypeDef",
    "ListShardsPaginateResponseShardsTypeDef",
    "ListShardsPaginateResponseTypeDef",
    "ListStreamConsumersPaginatePaginationConfigTypeDef",
    "ListStreamConsumersPaginateResponseConsumersTypeDef",
    "ListStreamConsumersPaginateResponseTypeDef",
    "ListStreamsPaginatePaginationConfigTypeDef",
    "ListStreamsPaginateResponseTypeDef",
    "StreamExistsWaitWaiterConfigTypeDef",
    "StreamNotExistsWaitWaiterConfigTypeDef",
)


_ClientDescribeLimitsResponseTypeDef = TypedDict(
    "_ClientDescribeLimitsResponseTypeDef",
    {"ShardLimit": int, "OpenShardCount": int},
    total=False,
)


class ClientDescribeLimitsResponseTypeDef(_ClientDescribeLimitsResponseTypeDef):
    """
    Type definition for `ClientDescribeLimits` `Response`

    - **ShardLimit** *(integer) --*

      The maximum number of shards.

    - **OpenShardCount** *(integer) --*

      The number of open shards.
    """


_ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef = TypedDict(
    "_ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": str,
        "ConsumerCreationTimestamp": datetime,
        "StreamARN": str,
    },
    total=False,
)


class ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef(
    _ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeStreamConsumerResponse` `ConsumerDescription`

    An object that represents the details of the consumer.

    - **ConsumerName** *(string) --*

      The name of the consumer is something you choose when you register the consumer.

    - **ConsumerARN** *(string) --*

      When you register a consumer, Kinesis Data Streams generates an ARN for it. You need this
      ARN to be able to call  SubscribeToShard .

      If you delete a consumer and then create a new one with the same name, it won't have the
      same ARN. That's because consumer ARNs contain the creation timestamp. This is important to
      keep in mind if you have IAM policies that reference consumer ARNs.

    - **ConsumerStatus** *(string) --*

      A consumer can't read data while in the ``CREATING`` or ``DELETING`` states.

    - **ConsumerCreationTimestamp** *(datetime) --*

    - **StreamARN** *(string) --*

      The ARN of the stream with which you registered the consumer.
    """


_ClientDescribeStreamConsumerResponseTypeDef = TypedDict(
    "_ClientDescribeStreamConsumerResponseTypeDef",
    {
        "ConsumerDescription": ClientDescribeStreamConsumerResponseConsumerDescriptionTypeDef
    },
    total=False,
)


class ClientDescribeStreamConsumerResponseTypeDef(
    _ClientDescribeStreamConsumerResponseTypeDef
):
    """
    Type definition for `ClientDescribeStreamConsumer` `Response`

    - **ConsumerDescription** *(dict) --*

      An object that represents the details of the consumer.

      - **ConsumerName** *(string) --*

        The name of the consumer is something you choose when you register the consumer.

      - **ConsumerARN** *(string) --*

        When you register a consumer, Kinesis Data Streams generates an ARN for it. You need this
        ARN to be able to call  SubscribeToShard .

        If you delete a consumer and then create a new one with the same name, it won't have the
        same ARN. That's because consumer ARNs contain the creation timestamp. This is important to
        keep in mind if you have IAM policies that reference consumer ARNs.

      - **ConsumerStatus** *(string) --*

        A consumer can't read data while in the ``CREATING`` or ``DELETING`` states.

      - **ConsumerCreationTimestamp** *(datetime) --*

      - **StreamARN** *(string) --*

        The ARN of the stream with which you registered the consumer.
    """


_ClientDescribeStreamResponseStreamDescriptionEnhancedMonitoringTypeDef = TypedDict(
    "_ClientDescribeStreamResponseStreamDescriptionEnhancedMonitoringTypeDef",
    {"ShardLevelMetrics": List[str]},
    total=False,
)


class ClientDescribeStreamResponseStreamDescriptionEnhancedMonitoringTypeDef(
    _ClientDescribeStreamResponseStreamDescriptionEnhancedMonitoringTypeDef
):
    """
    Type definition for `ClientDescribeStreamResponseStreamDescription` `EnhancedMonitoring`

    Represents enhanced metrics types.

    - **ShardLevelMetrics** *(list) --*

      List of shard-level metrics.

      The following are the valid shard-level metrics. The value "``ALL`` " enhances every
      metric.

      * ``IncomingBytes``

      * ``IncomingRecords``

      * ``OutgoingBytes``

      * ``OutgoingRecords``

      * ``WriteProvisionedThroughputExceeded``

      * ``ReadProvisionedThroughputExceeded``

      * ``IteratorAgeMilliseconds``

      * ``ALL``

      For more information, see `Monitoring the Amazon Kinesis Data Streams Service with
      Amazon CloudWatch
      <http://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html>`__ in
      the *Amazon Kinesis Data Streams Developer Guide* .

      - *(string) --*
    """


_ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef = TypedDict(
    "_ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef",
    {"StartingHashKey": str, "EndingHashKey": str},
    total=False,
)


class ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef(
    _ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef
):
    """
    Type definition for `ClientDescribeStreamResponseStreamDescriptionShards` `HashKeyRange`

    The range of possible hash key values for the shard, which is a set of ordered
    contiguous positive integers.

    - **StartingHashKey** *(string) --*

      The starting hash key of the hash key range.

    - **EndingHashKey** *(string) --*

      The ending hash key of the hash key range.
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

      The starting sequence number for the range.

    - **EndingSequenceNumber** *(string) --*

      The ending sequence number for the range. Shards that are in the OPEN state have an
      ending sequence number of ``null`` .
    """


_ClientDescribeStreamResponseStreamDescriptionShardsTypeDef = TypedDict(
    "_ClientDescribeStreamResponseStreamDescriptionShardsTypeDef",
    {
        "ShardId": str,
        "ParentShardId": str,
        "AdjacentParentShardId": str,
        "HashKeyRange": ClientDescribeStreamResponseStreamDescriptionShardsHashKeyRangeTypeDef,
        "SequenceNumberRange": ClientDescribeStreamResponseStreamDescriptionShardsSequenceNumberRangeTypeDef,
    },
    total=False,
)


class ClientDescribeStreamResponseStreamDescriptionShardsTypeDef(
    _ClientDescribeStreamResponseStreamDescriptionShardsTypeDef
):
    """
    Type definition for `ClientDescribeStreamResponseStreamDescription` `Shards`

    A uniquely identified group of data records in a Kinesis data stream.

    - **ShardId** *(string) --*

      The unique identifier of the shard within the stream.

    - **ParentShardId** *(string) --*

      The shard ID of the shard's parent.

    - **AdjacentParentShardId** *(string) --*

      The shard ID of the shard adjacent to the shard's parent.

    - **HashKeyRange** *(dict) --*

      The range of possible hash key values for the shard, which is a set of ordered
      contiguous positive integers.

      - **StartingHashKey** *(string) --*

        The starting hash key of the hash key range.

      - **EndingHashKey** *(string) --*

        The ending hash key of the hash key range.

    - **SequenceNumberRange** *(dict) --*

      The range of possible sequence numbers for the shard.

      - **StartingSequenceNumber** *(string) --*

        The starting sequence number for the range.

      - **EndingSequenceNumber** *(string) --*

        The ending sequence number for the range. Shards that are in the OPEN state have an
        ending sequence number of ``null`` .
    """


_ClientDescribeStreamResponseStreamDescriptionTypeDef = TypedDict(
    "_ClientDescribeStreamResponseStreamDescriptionTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": str,
        "Shards": List[ClientDescribeStreamResponseStreamDescriptionShardsTypeDef],
        "HasMoreShards": bool,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List[
            ClientDescribeStreamResponseStreamDescriptionEnhancedMonitoringTypeDef
        ],
        "EncryptionType": str,
        "KeyId": str,
    },
    total=False,
)


class ClientDescribeStreamResponseStreamDescriptionTypeDef(
    _ClientDescribeStreamResponseStreamDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeStreamResponse` `StreamDescription`

    The current status of the stream, the stream Amazon Resource Name (ARN), an array of shard
    objects that comprise the stream, and whether there are more shards available.

    - **StreamName** *(string) --*

      The name of the stream being described.

    - **StreamARN** *(string) --*

      The Amazon Resource Name (ARN) for the stream being described.

    - **StreamStatus** *(string) --*

      The current status of the stream being described. The stream status is one of the following
      states:

      * ``CREATING`` - The stream is being created. Kinesis Data Streams immediately returns and
      sets ``StreamStatus`` to ``CREATING`` .

      * ``DELETING`` - The stream is being deleted. The specified stream is in the ``DELETING``
      state until Kinesis Data Streams completes the deletion.

      * ``ACTIVE`` - The stream exists and is ready for read and write operations or deletion.
      You should perform read and write operations only on an ``ACTIVE`` stream.

      * ``UPDATING`` - Shards in the stream are being merged or split. Read and write operations
      continue to work while the stream is in the ``UPDATING`` state.

    - **Shards** *(list) --*

      The shards that comprise the stream.

      - *(dict) --*

        A uniquely identified group of data records in a Kinesis data stream.

        - **ShardId** *(string) --*

          The unique identifier of the shard within the stream.

        - **ParentShardId** *(string) --*

          The shard ID of the shard's parent.

        - **AdjacentParentShardId** *(string) --*

          The shard ID of the shard adjacent to the shard's parent.

        - **HashKeyRange** *(dict) --*

          The range of possible hash key values for the shard, which is a set of ordered
          contiguous positive integers.

          - **StartingHashKey** *(string) --*

            The starting hash key of the hash key range.

          - **EndingHashKey** *(string) --*

            The ending hash key of the hash key range.

        - **SequenceNumberRange** *(dict) --*

          The range of possible sequence numbers for the shard.

          - **StartingSequenceNumber** *(string) --*

            The starting sequence number for the range.

          - **EndingSequenceNumber** *(string) --*

            The ending sequence number for the range. Shards that are in the OPEN state have an
            ending sequence number of ``null`` .

    - **HasMoreShards** *(boolean) --*

      If set to ``true`` , more shards in the stream are available to describe.

    - **RetentionPeriodHours** *(integer) --*

      The current retention period, in hours.

    - **StreamCreationTimestamp** *(datetime) --*

      The approximate time that the stream was created.

    - **EnhancedMonitoring** *(list) --*

      Represents the current enhanced monitoring settings of the stream.

      - *(dict) --*

        Represents enhanced metrics types.

        - **ShardLevelMetrics** *(list) --*

          List of shard-level metrics.

          The following are the valid shard-level metrics. The value "``ALL`` " enhances every
          metric.

          * ``IncomingBytes``

          * ``IncomingRecords``

          * ``OutgoingBytes``

          * ``OutgoingRecords``

          * ``WriteProvisionedThroughputExceeded``

          * ``ReadProvisionedThroughputExceeded``

          * ``IteratorAgeMilliseconds``

          * ``ALL``

          For more information, see `Monitoring the Amazon Kinesis Data Streams Service with
          Amazon CloudWatch
          <http://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html>`__ in
          the *Amazon Kinesis Data Streams Developer Guide* .

          - *(string) --*

    - **EncryptionType** *(string) --*

      The server-side encryption type used on the stream. This parameter can be one of the
      following values:

      * ``NONE`` : Do not encrypt the records in the stream.

      * ``KMS`` : Use server-side encryption on the records in the stream using a
      customer-managed AWS KMS key.

    - **KeyId** *(string) --*

      The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a
      globally unique identifier, a fully specified ARN to either an alias or a key, or an alias
      name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by
      specifying the alias ``aws/kinesis`` .

      * Key ARN example:
      ``arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012``

      * Alias ARN example: ``arn:aws:kms:us-east-1:123456789012:alias/MyAliasName``

      * Globally unique key ID example: ``12345678-1234-1234-1234-123456789012``

      * Alias name example: ``alias/MyAliasName``

      * Master key owned by Kinesis Data Streams: ``alias/aws/kinesis``
    """


_ClientDescribeStreamResponseTypeDef = TypedDict(
    "_ClientDescribeStreamResponseTypeDef",
    {"StreamDescription": ClientDescribeStreamResponseStreamDescriptionTypeDef},
    total=False,
)


class ClientDescribeStreamResponseTypeDef(_ClientDescribeStreamResponseTypeDef):
    """
    Type definition for `ClientDescribeStream` `Response`

    Represents the output for ``DescribeStream`` .

    - **StreamDescription** *(dict) --*

      The current status of the stream, the stream Amazon Resource Name (ARN), an array of shard
      objects that comprise the stream, and whether there are more shards available.

      - **StreamName** *(string) --*

        The name of the stream being described.

      - **StreamARN** *(string) --*

        The Amazon Resource Name (ARN) for the stream being described.

      - **StreamStatus** *(string) --*

        The current status of the stream being described. The stream status is one of the following
        states:

        * ``CREATING`` - The stream is being created. Kinesis Data Streams immediately returns and
        sets ``StreamStatus`` to ``CREATING`` .

        * ``DELETING`` - The stream is being deleted. The specified stream is in the ``DELETING``
        state until Kinesis Data Streams completes the deletion.

        * ``ACTIVE`` - The stream exists and is ready for read and write operations or deletion.
        You should perform read and write operations only on an ``ACTIVE`` stream.

        * ``UPDATING`` - Shards in the stream are being merged or split. Read and write operations
        continue to work while the stream is in the ``UPDATING`` state.

      - **Shards** *(list) --*

        The shards that comprise the stream.

        - *(dict) --*

          A uniquely identified group of data records in a Kinesis data stream.

          - **ShardId** *(string) --*

            The unique identifier of the shard within the stream.

          - **ParentShardId** *(string) --*

            The shard ID of the shard's parent.

          - **AdjacentParentShardId** *(string) --*

            The shard ID of the shard adjacent to the shard's parent.

          - **HashKeyRange** *(dict) --*

            The range of possible hash key values for the shard, which is a set of ordered
            contiguous positive integers.

            - **StartingHashKey** *(string) --*

              The starting hash key of the hash key range.

            - **EndingHashKey** *(string) --*

              The ending hash key of the hash key range.

          - **SequenceNumberRange** *(dict) --*

            The range of possible sequence numbers for the shard.

            - **StartingSequenceNumber** *(string) --*

              The starting sequence number for the range.

            - **EndingSequenceNumber** *(string) --*

              The ending sequence number for the range. Shards that are in the OPEN state have an
              ending sequence number of ``null`` .

      - **HasMoreShards** *(boolean) --*

        If set to ``true`` , more shards in the stream are available to describe.

      - **RetentionPeriodHours** *(integer) --*

        The current retention period, in hours.

      - **StreamCreationTimestamp** *(datetime) --*

        The approximate time that the stream was created.

      - **EnhancedMonitoring** *(list) --*

        Represents the current enhanced monitoring settings of the stream.

        - *(dict) --*

          Represents enhanced metrics types.

          - **ShardLevelMetrics** *(list) --*

            List of shard-level metrics.

            The following are the valid shard-level metrics. The value "``ALL`` " enhances every
            metric.

            * ``IncomingBytes``

            * ``IncomingRecords``

            * ``OutgoingBytes``

            * ``OutgoingRecords``

            * ``WriteProvisionedThroughputExceeded``

            * ``ReadProvisionedThroughputExceeded``

            * ``IteratorAgeMilliseconds``

            * ``ALL``

            For more information, see `Monitoring the Amazon Kinesis Data Streams Service with
            Amazon CloudWatch
            <http://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html>`__ in
            the *Amazon Kinesis Data Streams Developer Guide* .

            - *(string) --*

      - **EncryptionType** *(string) --*

        The server-side encryption type used on the stream. This parameter can be one of the
        following values:

        * ``NONE`` : Do not encrypt the records in the stream.

        * ``KMS`` : Use server-side encryption on the records in the stream using a
        customer-managed AWS KMS key.

      - **KeyId** *(string) --*

        The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a
        globally unique identifier, a fully specified ARN to either an alias or a key, or an alias
        name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by
        specifying the alias ``aws/kinesis`` .

        * Key ARN example:
        ``arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012``

        * Alias ARN example: ``arn:aws:kms:us-east-1:123456789012:alias/MyAliasName``

        * Globally unique key ID example: ``12345678-1234-1234-1234-123456789012``

        * Alias name example: ``alias/MyAliasName``

        * Master key owned by Kinesis Data Streams: ``alias/aws/kinesis``
    """


_ClientDescribeStreamSummaryResponseStreamDescriptionSummaryEnhancedMonitoringTypeDef = TypedDict(
    "_ClientDescribeStreamSummaryResponseStreamDescriptionSummaryEnhancedMonitoringTypeDef",
    {"ShardLevelMetrics": List[str]},
    total=False,
)


class ClientDescribeStreamSummaryResponseStreamDescriptionSummaryEnhancedMonitoringTypeDef(
    _ClientDescribeStreamSummaryResponseStreamDescriptionSummaryEnhancedMonitoringTypeDef
):
    """
    Type definition for `ClientDescribeStreamSummaryResponseStreamDescriptionSummary` `EnhancedMonitoring`

    Represents enhanced metrics types.

    - **ShardLevelMetrics** *(list) --*

      List of shard-level metrics.

      The following are the valid shard-level metrics. The value "``ALL`` " enhances every
      metric.

      * ``IncomingBytes``

      * ``IncomingRecords``

      * ``OutgoingBytes``

      * ``OutgoingRecords``

      * ``WriteProvisionedThroughputExceeded``

      * ``ReadProvisionedThroughputExceeded``

      * ``IteratorAgeMilliseconds``

      * ``ALL``

      For more information, see `Monitoring the Amazon Kinesis Data Streams Service with
      Amazon CloudWatch
      <http://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html>`__ in
      the *Amazon Kinesis Data Streams Developer Guide* .

      - *(string) --*
    """


_ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef = TypedDict(
    "_ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": str,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List[
            ClientDescribeStreamSummaryResponseStreamDescriptionSummaryEnhancedMonitoringTypeDef
        ],
        "EncryptionType": str,
        "KeyId": str,
        "OpenShardCount": int,
        "ConsumerCount": int,
    },
    total=False,
)


class ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef(
    _ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef
):
    """
    Type definition for `ClientDescribeStreamSummaryResponse` `StreamDescriptionSummary`

    A  StreamDescriptionSummary containing information about the stream.

    - **StreamName** *(string) --*

      The name of the stream being described.

    - **StreamARN** *(string) --*

      The Amazon Resource Name (ARN) for the stream being described.

    - **StreamStatus** *(string) --*

      The current status of the stream being described. The stream status is one of the following
      states:

      * ``CREATING`` - The stream is being created. Kinesis Data Streams immediately returns and
      sets ``StreamStatus`` to ``CREATING`` .

      * ``DELETING`` - The stream is being deleted. The specified stream is in the ``DELETING``
      state until Kinesis Data Streams completes the deletion.

      * ``ACTIVE`` - The stream exists and is ready for read and write operations or deletion.
      You should perform read and write operations only on an ``ACTIVE`` stream.

      * ``UPDATING`` - Shards in the stream are being merged or split. Read and write operations
      continue to work while the stream is in the ``UPDATING`` state.

    - **RetentionPeriodHours** *(integer) --*

      The current retention period, in hours.

    - **StreamCreationTimestamp** *(datetime) --*

      The approximate time that the stream was created.

    - **EnhancedMonitoring** *(list) --*

      Represents the current enhanced monitoring settings of the stream.

      - *(dict) --*

        Represents enhanced metrics types.

        - **ShardLevelMetrics** *(list) --*

          List of shard-level metrics.

          The following are the valid shard-level metrics. The value "``ALL`` " enhances every
          metric.

          * ``IncomingBytes``

          * ``IncomingRecords``

          * ``OutgoingBytes``

          * ``OutgoingRecords``

          * ``WriteProvisionedThroughputExceeded``

          * ``ReadProvisionedThroughputExceeded``

          * ``IteratorAgeMilliseconds``

          * ``ALL``

          For more information, see `Monitoring the Amazon Kinesis Data Streams Service with
          Amazon CloudWatch
          <http://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html>`__ in
          the *Amazon Kinesis Data Streams Developer Guide* .

          - *(string) --*

    - **EncryptionType** *(string) --*

      The encryption type used. This value is one of the following:

      * ``KMS``

      * ``NONE``

    - **KeyId** *(string) --*

      The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a
      globally unique identifier, a fully specified ARN to either an alias or a key, or an alias
      name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by
      specifying the alias ``aws/kinesis`` .

      * Key ARN example:
      ``arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012``

      * Alias ARN example: ``arn:aws:kms:us-east-1:123456789012:alias/MyAliasName``

      * Globally unique key ID example: ``12345678-1234-1234-1234-123456789012``

      * Alias name example: ``alias/MyAliasName``

      * Master key owned by Kinesis Data Streams: ``alias/aws/kinesis``

    - **OpenShardCount** *(integer) --*

      The number of open shards in the stream.

    - **ConsumerCount** *(integer) --*

      The number of enhanced fan-out consumers registered with the stream.
    """


_ClientDescribeStreamSummaryResponseTypeDef = TypedDict(
    "_ClientDescribeStreamSummaryResponseTypeDef",
    {
        "StreamDescriptionSummary": ClientDescribeStreamSummaryResponseStreamDescriptionSummaryTypeDef
    },
    total=False,
)


class ClientDescribeStreamSummaryResponseTypeDef(
    _ClientDescribeStreamSummaryResponseTypeDef
):
    """
    Type definition for `ClientDescribeStreamSummary` `Response`

    - **StreamDescriptionSummary** *(dict) --*

      A  StreamDescriptionSummary containing information about the stream.

      - **StreamName** *(string) --*

        The name of the stream being described.

      - **StreamARN** *(string) --*

        The Amazon Resource Name (ARN) for the stream being described.

      - **StreamStatus** *(string) --*

        The current status of the stream being described. The stream status is one of the following
        states:

        * ``CREATING`` - The stream is being created. Kinesis Data Streams immediately returns and
        sets ``StreamStatus`` to ``CREATING`` .

        * ``DELETING`` - The stream is being deleted. The specified stream is in the ``DELETING``
        state until Kinesis Data Streams completes the deletion.

        * ``ACTIVE`` - The stream exists and is ready for read and write operations or deletion.
        You should perform read and write operations only on an ``ACTIVE`` stream.

        * ``UPDATING`` - Shards in the stream are being merged or split. Read and write operations
        continue to work while the stream is in the ``UPDATING`` state.

      - **RetentionPeriodHours** *(integer) --*

        The current retention period, in hours.

      - **StreamCreationTimestamp** *(datetime) --*

        The approximate time that the stream was created.

      - **EnhancedMonitoring** *(list) --*

        Represents the current enhanced monitoring settings of the stream.

        - *(dict) --*

          Represents enhanced metrics types.

          - **ShardLevelMetrics** *(list) --*

            List of shard-level metrics.

            The following are the valid shard-level metrics. The value "``ALL`` " enhances every
            metric.

            * ``IncomingBytes``

            * ``IncomingRecords``

            * ``OutgoingBytes``

            * ``OutgoingRecords``

            * ``WriteProvisionedThroughputExceeded``

            * ``ReadProvisionedThroughputExceeded``

            * ``IteratorAgeMilliseconds``

            * ``ALL``

            For more information, see `Monitoring the Amazon Kinesis Data Streams Service with
            Amazon CloudWatch
            <http://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html>`__ in
            the *Amazon Kinesis Data Streams Developer Guide* .

            - *(string) --*

      - **EncryptionType** *(string) --*

        The encryption type used. This value is one of the following:

        * ``KMS``

        * ``NONE``

      - **KeyId** *(string) --*

        The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a
        globally unique identifier, a fully specified ARN to either an alias or a key, or an alias
        name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by
        specifying the alias ``aws/kinesis`` .

        * Key ARN example:
        ``arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012``

        * Alias ARN example: ``arn:aws:kms:us-east-1:123456789012:alias/MyAliasName``

        * Globally unique key ID example: ``12345678-1234-1234-1234-123456789012``

        * Alias name example: ``alias/MyAliasName``

        * Master key owned by Kinesis Data Streams: ``alias/aws/kinesis``

      - **OpenShardCount** *(integer) --*

        The number of open shards in the stream.

      - **ConsumerCount** *(integer) --*

        The number of enhanced fan-out consumers registered with the stream.
    """


_ClientDisableEnhancedMonitoringResponseTypeDef = TypedDict(
    "_ClientDisableEnhancedMonitoringResponseTypeDef",
    {
        "StreamName": str,
        "CurrentShardLevelMetrics": List[str],
        "DesiredShardLevelMetrics": List[str],
    },
    total=False,
)


class ClientDisableEnhancedMonitoringResponseTypeDef(
    _ClientDisableEnhancedMonitoringResponseTypeDef
):
    """
    Type definition for `ClientDisableEnhancedMonitoring` `Response`

    Represents the output for  EnableEnhancedMonitoring and  DisableEnhancedMonitoring .

    - **StreamName** *(string) --*

      The name of the Kinesis data stream.

    - **CurrentShardLevelMetrics** *(list) --*

      Represents the current state of the metrics that are in the enhanced state before the
      operation.

      - *(string) --*

    - **DesiredShardLevelMetrics** *(list) --*

      Represents the list of all the metrics that would be in the enhanced state after the
      operation.

      - *(string) --*
    """


_ClientEnableEnhancedMonitoringResponseTypeDef = TypedDict(
    "_ClientEnableEnhancedMonitoringResponseTypeDef",
    {
        "StreamName": str,
        "CurrentShardLevelMetrics": List[str],
        "DesiredShardLevelMetrics": List[str],
    },
    total=False,
)


class ClientEnableEnhancedMonitoringResponseTypeDef(
    _ClientEnableEnhancedMonitoringResponseTypeDef
):
    """
    Type definition for `ClientEnableEnhancedMonitoring` `Response`

    Represents the output for  EnableEnhancedMonitoring and  DisableEnhancedMonitoring .

    - **StreamName** *(string) --*

      The name of the Kinesis data stream.

    - **CurrentShardLevelMetrics** *(list) --*

      Represents the current state of the metrics that are in the enhanced state before the
      operation.

      - *(string) --*

    - **DesiredShardLevelMetrics** *(list) --*

      Represents the list of all the metrics that would be in the enhanced state after the
      operation.

      - *(string) --*
    """


_ClientGetRecordsResponseRecordsTypeDef = TypedDict(
    "_ClientGetRecordsResponseRecordsTypeDef",
    {
        "SequenceNumber": str,
        "ApproximateArrivalTimestamp": datetime,
        "Data": bytes,
        "PartitionKey": str,
        "EncryptionType": str,
    },
    total=False,
)


class ClientGetRecordsResponseRecordsTypeDef(_ClientGetRecordsResponseRecordsTypeDef):
    """
    Type definition for `ClientGetRecordsResponse` `Records`

    The unit of data of the Kinesis data stream, which is composed of a sequence number, a
    partition key, and a data blob.

    - **SequenceNumber** *(string) --*

      The unique identifier of the record within its shard.

    - **ApproximateArrivalTimestamp** *(datetime) --*

      The approximate time that the record was inserted into the stream.

    - **Data** *(bytes) --*

      The data blob. The data in the blob is both opaque and immutable to Kinesis Data Streams,
      which does not inspect, interpret, or change the data in the blob in any way. When the
      data blob (the payload before base64-encoding) is added to the partition key size, the
      total size must not exceed the maximum record size (1 MB).

    - **PartitionKey** *(string) --*

      Identifies which shard in the stream the data record is assigned to.

    - **EncryptionType** *(string) --*

      The encryption type used on the record. This parameter can be one of the following values:

      * ``NONE`` : Do not encrypt the records in the stream.

      * ``KMS`` : Use server-side encryption on the records in the stream using a
      customer-managed AWS KMS key.
    """


_ClientGetRecordsResponseTypeDef = TypedDict(
    "_ClientGetRecordsResponseTypeDef",
    {
        "Records": List[ClientGetRecordsResponseRecordsTypeDef],
        "NextShardIterator": str,
        "MillisBehindLatest": int,
    },
    total=False,
)


class ClientGetRecordsResponseTypeDef(_ClientGetRecordsResponseTypeDef):
    """
    Type definition for `ClientGetRecords` `Response`

    Represents the output for  GetRecords .

    - **Records** *(list) --*

      The data records retrieved from the shard.

      - *(dict) --*

        The unit of data of the Kinesis data stream, which is composed of a sequence number, a
        partition key, and a data blob.

        - **SequenceNumber** *(string) --*

          The unique identifier of the record within its shard.

        - **ApproximateArrivalTimestamp** *(datetime) --*

          The approximate time that the record was inserted into the stream.

        - **Data** *(bytes) --*

          The data blob. The data in the blob is both opaque and immutable to Kinesis Data Streams,
          which does not inspect, interpret, or change the data in the blob in any way. When the
          data blob (the payload before base64-encoding) is added to the partition key size, the
          total size must not exceed the maximum record size (1 MB).

        - **PartitionKey** *(string) --*

          Identifies which shard in the stream the data record is assigned to.

        - **EncryptionType** *(string) --*

          The encryption type used on the record. This parameter can be one of the following values:

          * ``NONE`` : Do not encrypt the records in the stream.

          * ``KMS`` : Use server-side encryption on the records in the stream using a
          customer-managed AWS KMS key.

    - **NextShardIterator** *(string) --*

      The next position in the shard from which to start sequentially reading data records. If set
      to ``null`` , the shard has been closed and the requested iterator does not return any more
      data.

    - **MillisBehindLatest** *(integer) --*

      The number of milliseconds the  GetRecords response is from the tip of the stream, indicating
      how far behind current time the consumer is. A value of zero indicates that record processing
      is caught up, and there are no new records to process at this moment.
    """


_ClientGetShardIteratorResponseTypeDef = TypedDict(
    "_ClientGetShardIteratorResponseTypeDef", {"ShardIterator": str}, total=False
)


class ClientGetShardIteratorResponseTypeDef(_ClientGetShardIteratorResponseTypeDef):
    """
    Type definition for `ClientGetShardIterator` `Response`

    Represents the output for ``GetShardIterator`` .

    - **ShardIterator** *(string) --*

      The position in the shard from which to start reading data records sequentially. A shard
      iterator specifies this position using the sequence number of a data record in a shard.
    """


_ClientListShardsResponseShardsHashKeyRangeTypeDef = TypedDict(
    "_ClientListShardsResponseShardsHashKeyRangeTypeDef",
    {"StartingHashKey": str, "EndingHashKey": str},
    total=False,
)


class ClientListShardsResponseShardsHashKeyRangeTypeDef(
    _ClientListShardsResponseShardsHashKeyRangeTypeDef
):
    """
    Type definition for `ClientListShardsResponseShards` `HashKeyRange`

    The range of possible hash key values for the shard, which is a set of ordered contiguous
    positive integers.

    - **StartingHashKey** *(string) --*

      The starting hash key of the hash key range.

    - **EndingHashKey** *(string) --*

      The ending hash key of the hash key range.
    """


_ClientListShardsResponseShardsSequenceNumberRangeTypeDef = TypedDict(
    "_ClientListShardsResponseShardsSequenceNumberRangeTypeDef",
    {"StartingSequenceNumber": str, "EndingSequenceNumber": str},
    total=False,
)


class ClientListShardsResponseShardsSequenceNumberRangeTypeDef(
    _ClientListShardsResponseShardsSequenceNumberRangeTypeDef
):
    """
    Type definition for `ClientListShardsResponseShards` `SequenceNumberRange`

    The range of possible sequence numbers for the shard.

    - **StartingSequenceNumber** *(string) --*

      The starting sequence number for the range.

    - **EndingSequenceNumber** *(string) --*

      The ending sequence number for the range. Shards that are in the OPEN state have an
      ending sequence number of ``null`` .
    """


_ClientListShardsResponseShardsTypeDef = TypedDict(
    "_ClientListShardsResponseShardsTypeDef",
    {
        "ShardId": str,
        "ParentShardId": str,
        "AdjacentParentShardId": str,
        "HashKeyRange": ClientListShardsResponseShardsHashKeyRangeTypeDef,
        "SequenceNumberRange": ClientListShardsResponseShardsSequenceNumberRangeTypeDef,
    },
    total=False,
)


class ClientListShardsResponseShardsTypeDef(_ClientListShardsResponseShardsTypeDef):
    """
    Type definition for `ClientListShardsResponse` `Shards`

    A uniquely identified group of data records in a Kinesis data stream.

    - **ShardId** *(string) --*

      The unique identifier of the shard within the stream.

    - **ParentShardId** *(string) --*

      The shard ID of the shard's parent.

    - **AdjacentParentShardId** *(string) --*

      The shard ID of the shard adjacent to the shard's parent.

    - **HashKeyRange** *(dict) --*

      The range of possible hash key values for the shard, which is a set of ordered contiguous
      positive integers.

      - **StartingHashKey** *(string) --*

        The starting hash key of the hash key range.

      - **EndingHashKey** *(string) --*

        The ending hash key of the hash key range.

    - **SequenceNumberRange** *(dict) --*

      The range of possible sequence numbers for the shard.

      - **StartingSequenceNumber** *(string) --*

        The starting sequence number for the range.

      - **EndingSequenceNumber** *(string) --*

        The ending sequence number for the range. Shards that are in the OPEN state have an
        ending sequence number of ``null`` .
    """


_ClientListShardsResponseTypeDef = TypedDict(
    "_ClientListShardsResponseTypeDef",
    {"Shards": List[ClientListShardsResponseShardsTypeDef], "NextToken": str},
    total=False,
)


class ClientListShardsResponseTypeDef(_ClientListShardsResponseTypeDef):
    """
    Type definition for `ClientListShards` `Response`

    - **Shards** *(list) --*

      An array of JSON objects. Each object represents one shard and specifies the IDs of the
      shard, the shard's parent, and the shard that's adjacent to the shard's parent. Each object
      also contains the starting and ending hash keys and the starting and ending sequence numbers
      for the shard.

      - *(dict) --*

        A uniquely identified group of data records in a Kinesis data stream.

        - **ShardId** *(string) --*

          The unique identifier of the shard within the stream.

        - **ParentShardId** *(string) --*

          The shard ID of the shard's parent.

        - **AdjacentParentShardId** *(string) --*

          The shard ID of the shard adjacent to the shard's parent.

        - **HashKeyRange** *(dict) --*

          The range of possible hash key values for the shard, which is a set of ordered contiguous
          positive integers.

          - **StartingHashKey** *(string) --*

            The starting hash key of the hash key range.

          - **EndingHashKey** *(string) --*

            The ending hash key of the hash key range.

        - **SequenceNumberRange** *(dict) --*

          The range of possible sequence numbers for the shard.

          - **StartingSequenceNumber** *(string) --*

            The starting sequence number for the range.

          - **EndingSequenceNumber** *(string) --*

            The ending sequence number for the range. Shards that are in the OPEN state have an
            ending sequence number of ``null`` .

    - **NextToken** *(string) --*

      When the number of shards in the data stream is greater than the default value for the
      ``MaxResults`` parameter, or if you explicitly specify a value for ``MaxResults`` that is
      less than the number of shards in the data stream, the response includes a pagination token
      named ``NextToken`` . You can specify this ``NextToken`` value in a subsequent call to
      ``ListShards`` to list the next set of shards. For more information about the use of this
      pagination token when calling the ``ListShards`` operation, see  ListShardsInput$NextToken .

      .. warning::

        Tokens expire after 300 seconds. When you obtain a value for ``NextToken`` in the response
        to a call to ``ListShards`` , you have 300 seconds to use that value. If you specify an
        expired token in a call to ``ListShards`` , you get ``ExpiredNextTokenException`` .
    """


_ClientListStreamConsumersResponseConsumersTypeDef = TypedDict(
    "_ClientListStreamConsumersResponseConsumersTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": str,
        "ConsumerCreationTimestamp": datetime,
    },
    total=False,
)


class ClientListStreamConsumersResponseConsumersTypeDef(
    _ClientListStreamConsumersResponseConsumersTypeDef
):
    """
    Type definition for `ClientListStreamConsumersResponse` `Consumers`

    An object that represents the details of the consumer you registered.

    - **ConsumerName** *(string) --*

      The name of the consumer is something you choose when you register the consumer.

    - **ConsumerARN** *(string) --*

      When you register a consumer, Kinesis Data Streams generates an ARN for it. You need this
      ARN to be able to call  SubscribeToShard .

      If you delete a consumer and then create a new one with the same name, it won't have the
      same ARN. That's because consumer ARNs contain the creation timestamp. This is important
      to keep in mind if you have IAM policies that reference consumer ARNs.

    - **ConsumerStatus** *(string) --*

      A consumer can't read data while in the ``CREATING`` or ``DELETING`` states.

    - **ConsumerCreationTimestamp** *(datetime) --*
    """


_ClientListStreamConsumersResponseTypeDef = TypedDict(
    "_ClientListStreamConsumersResponseTypeDef",
    {
        "Consumers": List[ClientListStreamConsumersResponseConsumersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListStreamConsumersResponseTypeDef(
    _ClientListStreamConsumersResponseTypeDef
):
    """
    Type definition for `ClientListStreamConsumers` `Response`

    - **Consumers** *(list) --*

      An array of JSON objects. Each object represents one registered consumer.

      - *(dict) --*

        An object that represents the details of the consumer you registered.

        - **ConsumerName** *(string) --*

          The name of the consumer is something you choose when you register the consumer.

        - **ConsumerARN** *(string) --*

          When you register a consumer, Kinesis Data Streams generates an ARN for it. You need this
          ARN to be able to call  SubscribeToShard .

          If you delete a consumer and then create a new one with the same name, it won't have the
          same ARN. That's because consumer ARNs contain the creation timestamp. This is important
          to keep in mind if you have IAM policies that reference consumer ARNs.

        - **ConsumerStatus** *(string) --*

          A consumer can't read data while in the ``CREATING`` or ``DELETING`` states.

        - **ConsumerCreationTimestamp** *(datetime) --*

    - **NextToken** *(string) --*

      When the number of consumers that are registered with the data stream is greater than the
      default value for the ``MaxResults`` parameter, or if you explicitly specify a value for
      ``MaxResults`` that is less than the number of registered consumers, the response includes a
      pagination token named ``NextToken`` . You can specify this ``NextToken`` value in a
      subsequent call to ``ListStreamConsumers`` to list the next set of registered consumers. For
      more information about the use of this pagination token when calling the
      ``ListStreamConsumers`` operation, see  ListStreamConsumersInput$NextToken .

      .. warning::

        Tokens expire after 300 seconds. When you obtain a value for ``NextToken`` in the response
        to a call to ``ListStreamConsumers`` , you have 300 seconds to use that value. If you
        specify an expired token in a call to ``ListStreamConsumers`` , you get
        ``ExpiredNextTokenException`` .
    """


_ClientListStreamsResponseTypeDef = TypedDict(
    "_ClientListStreamsResponseTypeDef",
    {"StreamNames": List[str], "HasMoreStreams": bool},
    total=False,
)


class ClientListStreamsResponseTypeDef(_ClientListStreamsResponseTypeDef):
    """
    Type definition for `ClientListStreams` `Response`

    Represents the output for ``ListStreams`` .

    - **StreamNames** *(list) --*

      The names of the streams that are associated with the AWS account making the ``ListStreams``
      request.

      - *(string) --*

    - **HasMoreStreams** *(boolean) --*

      If set to ``true`` , there are more streams available to list.
    """


_ClientListTagsForStreamResponseTagsTypeDef = TypedDict(
    "_ClientListTagsForStreamResponseTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForStreamResponseTagsTypeDef(
    _ClientListTagsForStreamResponseTagsTypeDef
):
    """
    Type definition for `ClientListTagsForStreamResponse` `Tags`

    Metadata assigned to the stream, consisting of a key-value pair.

    - **Key** *(string) --*

      A unique identifier for the tag. Maximum length: 128 characters. Valid characters:
      Unicode letters, digits, white space, _ . / = + - % @

    - **Value** *(string) --*

      An optional string, typically used to describe or define the tag. Maximum length: 256
      characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @
    """


_ClientListTagsForStreamResponseTypeDef = TypedDict(
    "_ClientListTagsForStreamResponseTypeDef",
    {"Tags": List[ClientListTagsForStreamResponseTagsTypeDef], "HasMoreTags": bool},
    total=False,
)


class ClientListTagsForStreamResponseTypeDef(_ClientListTagsForStreamResponseTypeDef):
    """
    Type definition for `ClientListTagsForStream` `Response`

    Represents the output for ``ListTagsForStream`` .

    - **Tags** *(list) --*

      A list of tags associated with ``StreamName`` , starting with the first tag after
      ``ExclusiveStartTagKey`` and up to the specified ``Limit`` .

      - *(dict) --*

        Metadata assigned to the stream, consisting of a key-value pair.

        - **Key** *(string) --*

          A unique identifier for the tag. Maximum length: 128 characters. Valid characters:
          Unicode letters, digits, white space, _ . / = + - % @

        - **Value** *(string) --*

          An optional string, typically used to describe or define the tag. Maximum length: 256
          characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @

    - **HasMoreTags** *(boolean) --*

      If set to ``true`` , more tags are available. To request additional tags, set
      ``ExclusiveStartTagKey`` to the key of the last tag returned.
    """


_ClientPutRecordResponseTypeDef = TypedDict(
    "_ClientPutRecordResponseTypeDef",
    {"ShardId": str, "SequenceNumber": str, "EncryptionType": str},
    total=False,
)


class ClientPutRecordResponseTypeDef(_ClientPutRecordResponseTypeDef):
    """
    Type definition for `ClientPutRecord` `Response`

    Represents the output for ``PutRecord`` .

    - **ShardId** *(string) --*

      The shard ID of the shard where the data record was placed.

    - **SequenceNumber** *(string) --*

      The sequence number identifier that was assigned to the put data record. The sequence number
      for the record is unique across all records in the stream. A sequence number is the
      identifier associated with every record put into the stream.

    - **EncryptionType** *(string) --*

      The encryption type to use on the record. This parameter can be one of the following values:

      * ``NONE`` : Do not encrypt the records in the stream.

      * ``KMS`` : Use server-side encryption on the records in the stream using a customer-managed
      AWS KMS key.
    """


_RequiredClientPutRecordsRecordsTypeDef = TypedDict(
    "_RequiredClientPutRecordsRecordsTypeDef", {"Data": bytes, "PartitionKey": str}
)
_OptionalClientPutRecordsRecordsTypeDef = TypedDict(
    "_OptionalClientPutRecordsRecordsTypeDef", {"ExplicitHashKey": str}, total=False
)


class ClientPutRecordsRecordsTypeDef(
    _RequiredClientPutRecordsRecordsTypeDef, _OptionalClientPutRecordsRecordsTypeDef
):
    """
    Type definition for `ClientPutRecords` `Records`

    Represents the output for ``PutRecords`` .

    - **Data** *(bytes) --* **[REQUIRED]**

      The data blob to put into the record, which is base64-encoded when the blob is serialized.
      When the data blob (the payload before base64-encoding) is added to the partition key size,
      the total size must not exceed the maximum record size (1 MB).

    - **ExplicitHashKey** *(string) --*

      The hash value used to determine explicitly the shard that the data record is assigned to by
      overriding the partition key hash.

    - **PartitionKey** *(string) --* **[REQUIRED]**

      Determines which shard in the stream the data record is assigned to. Partition keys are
      Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis
      Data Streams uses the partition key as input to a hash function that maps the partition key
      and associated data to a specific shard. Specifically, an MD5 hash function is used to map
      partition keys to 128-bit integer values and to map associated data records to shards. As a
      result of this hashing mechanism, all data records with the same partition key map to the
      same shard within the stream.
    """


_ClientPutRecordsResponseRecordsTypeDef = TypedDict(
    "_ClientPutRecordsResponseRecordsTypeDef",
    {"SequenceNumber": str, "ShardId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientPutRecordsResponseRecordsTypeDef(_ClientPutRecordsResponseRecordsTypeDef):
    """
    Type definition for `ClientPutRecordsResponse` `Records`

    Represents the result of an individual record from a ``PutRecords`` request. A record that
    is successfully added to a stream includes ``SequenceNumber`` and ``ShardId`` in the
    result. A record that fails to be added to the stream includes ``ErrorCode`` and
    ``ErrorMessage`` in the result.

    - **SequenceNumber** *(string) --*

      The sequence number for an individual record result.

    - **ShardId** *(string) --*

      The shard ID for an individual record result.

    - **ErrorCode** *(string) --*

      The error code for an individual record result. ``ErrorCodes`` can be either
      ``ProvisionedThroughputExceededException`` or ``InternalFailure`` .

    - **ErrorMessage** *(string) --*

      The error message for an individual record result. An ``ErrorCode`` value of
      ``ProvisionedThroughputExceededException`` has an error message that includes the account
      ID, stream name, and shard ID. An ``ErrorCode`` value of ``InternalFailure`` has the
      error message ``"Internal Service Failure"`` .
    """


_ClientPutRecordsResponseTypeDef = TypedDict(
    "_ClientPutRecordsResponseTypeDef",
    {
        "FailedRecordCount": int,
        "Records": List[ClientPutRecordsResponseRecordsTypeDef],
        "EncryptionType": str,
    },
    total=False,
)


class ClientPutRecordsResponseTypeDef(_ClientPutRecordsResponseTypeDef):
    """
    Type definition for `ClientPutRecords` `Response`

     ``PutRecords`` results.

    - **FailedRecordCount** *(integer) --*

      The number of unsuccessfully processed records in a ``PutRecords`` request.

    - **Records** *(list) --*

      An array of successfully and unsuccessfully processed record results, correlated with the
      request by natural ordering. A record that is successfully added to a stream includes
      ``SequenceNumber`` and ``ShardId`` in the result. A record that fails to be added to a stream
      includes ``ErrorCode`` and ``ErrorMessage`` in the result.

      - *(dict) --*

        Represents the result of an individual record from a ``PutRecords`` request. A record that
        is successfully added to a stream includes ``SequenceNumber`` and ``ShardId`` in the
        result. A record that fails to be added to the stream includes ``ErrorCode`` and
        ``ErrorMessage`` in the result.

        - **SequenceNumber** *(string) --*

          The sequence number for an individual record result.

        - **ShardId** *(string) --*

          The shard ID for an individual record result.

        - **ErrorCode** *(string) --*

          The error code for an individual record result. ``ErrorCodes`` can be either
          ``ProvisionedThroughputExceededException`` or ``InternalFailure`` .

        - **ErrorMessage** *(string) --*

          The error message for an individual record result. An ``ErrorCode`` value of
          ``ProvisionedThroughputExceededException`` has an error message that includes the account
          ID, stream name, and shard ID. An ``ErrorCode`` value of ``InternalFailure`` has the
          error message ``"Internal Service Failure"`` .

    - **EncryptionType** *(string) --*

      The encryption type used on the records. This parameter can be one of the following values:

      * ``NONE`` : Do not encrypt the records.

      * ``KMS`` : Use server-side encryption on the records using a customer-managed AWS KMS key.
    """


_ClientRegisterStreamConsumerResponseConsumerTypeDef = TypedDict(
    "_ClientRegisterStreamConsumerResponseConsumerTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": str,
        "ConsumerCreationTimestamp": datetime,
    },
    total=False,
)


class ClientRegisterStreamConsumerResponseConsumerTypeDef(
    _ClientRegisterStreamConsumerResponseConsumerTypeDef
):
    """
    Type definition for `ClientRegisterStreamConsumerResponse` `Consumer`

    An object that represents the details of the consumer you registered. When you register a
    consumer, it gets an ARN that is generated by Kinesis Data Streams.

    - **ConsumerName** *(string) --*

      The name of the consumer is something you choose when you register the consumer.

    - **ConsumerARN** *(string) --*

      When you register a consumer, Kinesis Data Streams generates an ARN for it. You need this
      ARN to be able to call  SubscribeToShard .

      If you delete a consumer and then create a new one with the same name, it won't have the
      same ARN. That's because consumer ARNs contain the creation timestamp. This is important to
      keep in mind if you have IAM policies that reference consumer ARNs.

    - **ConsumerStatus** *(string) --*

      A consumer can't read data while in the ``CREATING`` or ``DELETING`` states.

    - **ConsumerCreationTimestamp** *(datetime) --*
    """


_ClientRegisterStreamConsumerResponseTypeDef = TypedDict(
    "_ClientRegisterStreamConsumerResponseTypeDef",
    {"Consumer": ClientRegisterStreamConsumerResponseConsumerTypeDef},
    total=False,
)


class ClientRegisterStreamConsumerResponseTypeDef(
    _ClientRegisterStreamConsumerResponseTypeDef
):
    """
    Type definition for `ClientRegisterStreamConsumer` `Response`

    - **Consumer** *(dict) --*

      An object that represents the details of the consumer you registered. When you register a
      consumer, it gets an ARN that is generated by Kinesis Data Streams.

      - **ConsumerName** *(string) --*

        The name of the consumer is something you choose when you register the consumer.

      - **ConsumerARN** *(string) --*

        When you register a consumer, Kinesis Data Streams generates an ARN for it. You need this
        ARN to be able to call  SubscribeToShard .

        If you delete a consumer and then create a new one with the same name, it won't have the
        same ARN. That's because consumer ARNs contain the creation timestamp. This is important to
        keep in mind if you have IAM policies that reference consumer ARNs.

      - **ConsumerStatus** *(string) --*

        A consumer can't read data while in the ``CREATING`` or ``DELETING`` states.

      - **ConsumerCreationTimestamp** *(datetime) --*
    """


_RequiredClientSubscribeToShardStartingPositionTypeDef = TypedDict(
    "_RequiredClientSubscribeToShardStartingPositionTypeDef", {"Type": str}
)
_OptionalClientSubscribeToShardStartingPositionTypeDef = TypedDict(
    "_OptionalClientSubscribeToShardStartingPositionTypeDef",
    {"SequenceNumber": str, "Timestamp": datetime},
    total=False,
)


class ClientSubscribeToShardStartingPositionTypeDef(
    _RequiredClientSubscribeToShardStartingPositionTypeDef,
    _OptionalClientSubscribeToShardStartingPositionTypeDef,
):
    """
    Type definition for `ClientSubscribeToShard` `StartingPosition`

    - **Type** *(string) --* **[REQUIRED]**

    - **SequenceNumber** *(string) --*

    - **Timestamp** *(datetime) --*
    """


_ClientUpdateShardCountResponseTypeDef = TypedDict(
    "_ClientUpdateShardCountResponseTypeDef",
    {"StreamName": str, "CurrentShardCount": int, "TargetShardCount": int},
    total=False,
)


class ClientUpdateShardCountResponseTypeDef(_ClientUpdateShardCountResponseTypeDef):
    """
    Type definition for `ClientUpdateShardCount` `Response`

    - **StreamName** *(string) --*

      The name of the stream.

    - **CurrentShardCount** *(integer) --*

      The current number of shards.

    - **TargetShardCount** *(integer) --*

      The updated number of shards.
    """


_DescribeStreamPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeStreamPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeStreamPaginatePaginationConfigTypeDef(
    _DescribeStreamPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeStreamPaginate` `PaginationConfig`

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


_DescribeStreamPaginateResponseStreamDescriptionEnhancedMonitoringTypeDef = TypedDict(
    "_DescribeStreamPaginateResponseStreamDescriptionEnhancedMonitoringTypeDef",
    {"ShardLevelMetrics": List[str]},
    total=False,
)


class DescribeStreamPaginateResponseStreamDescriptionEnhancedMonitoringTypeDef(
    _DescribeStreamPaginateResponseStreamDescriptionEnhancedMonitoringTypeDef
):
    """
    Type definition for `DescribeStreamPaginateResponseStreamDescription` `EnhancedMonitoring`

    Represents enhanced metrics types.

    - **ShardLevelMetrics** *(list) --*

      List of shard-level metrics.

      The following are the valid shard-level metrics. The value "``ALL`` " enhances every
      metric.

      * ``IncomingBytes``

      * ``IncomingRecords``

      * ``OutgoingBytes``

      * ``OutgoingRecords``

      * ``WriteProvisionedThroughputExceeded``

      * ``ReadProvisionedThroughputExceeded``

      * ``IteratorAgeMilliseconds``

      * ``ALL``

      For more information, see `Monitoring the Amazon Kinesis Data Streams Service with
      Amazon CloudWatch
      <http://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html>`__ in
      the *Amazon Kinesis Data Streams Developer Guide* .

      - *(string) --*
    """


_DescribeStreamPaginateResponseStreamDescriptionShardsHashKeyRangeTypeDef = TypedDict(
    "_DescribeStreamPaginateResponseStreamDescriptionShardsHashKeyRangeTypeDef",
    {"StartingHashKey": str, "EndingHashKey": str},
    total=False,
)


class DescribeStreamPaginateResponseStreamDescriptionShardsHashKeyRangeTypeDef(
    _DescribeStreamPaginateResponseStreamDescriptionShardsHashKeyRangeTypeDef
):
    """
    Type definition for `DescribeStreamPaginateResponseStreamDescriptionShards` `HashKeyRange`

    The range of possible hash key values for the shard, which is a set of ordered
    contiguous positive integers.

    - **StartingHashKey** *(string) --*

      The starting hash key of the hash key range.

    - **EndingHashKey** *(string) --*

      The ending hash key of the hash key range.
    """


_DescribeStreamPaginateResponseStreamDescriptionShardsSequenceNumberRangeTypeDef = TypedDict(
    "_DescribeStreamPaginateResponseStreamDescriptionShardsSequenceNumberRangeTypeDef",
    {"StartingSequenceNumber": str, "EndingSequenceNumber": str},
    total=False,
)


class DescribeStreamPaginateResponseStreamDescriptionShardsSequenceNumberRangeTypeDef(
    _DescribeStreamPaginateResponseStreamDescriptionShardsSequenceNumberRangeTypeDef
):
    """
    Type definition for `DescribeStreamPaginateResponseStreamDescriptionShards` `SequenceNumberRange`

    The range of possible sequence numbers for the shard.

    - **StartingSequenceNumber** *(string) --*

      The starting sequence number for the range.

    - **EndingSequenceNumber** *(string) --*

      The ending sequence number for the range. Shards that are in the OPEN state have an
      ending sequence number of ``null`` .
    """


_DescribeStreamPaginateResponseStreamDescriptionShardsTypeDef = TypedDict(
    "_DescribeStreamPaginateResponseStreamDescriptionShardsTypeDef",
    {
        "ShardId": str,
        "ParentShardId": str,
        "AdjacentParentShardId": str,
        "HashKeyRange": DescribeStreamPaginateResponseStreamDescriptionShardsHashKeyRangeTypeDef,
        "SequenceNumberRange": DescribeStreamPaginateResponseStreamDescriptionShardsSequenceNumberRangeTypeDef,
    },
    total=False,
)


class DescribeStreamPaginateResponseStreamDescriptionShardsTypeDef(
    _DescribeStreamPaginateResponseStreamDescriptionShardsTypeDef
):
    """
    Type definition for `DescribeStreamPaginateResponseStreamDescription` `Shards`

    A uniquely identified group of data records in a Kinesis data stream.

    - **ShardId** *(string) --*

      The unique identifier of the shard within the stream.

    - **ParentShardId** *(string) --*

      The shard ID of the shard's parent.

    - **AdjacentParentShardId** *(string) --*

      The shard ID of the shard adjacent to the shard's parent.

    - **HashKeyRange** *(dict) --*

      The range of possible hash key values for the shard, which is a set of ordered
      contiguous positive integers.

      - **StartingHashKey** *(string) --*

        The starting hash key of the hash key range.

      - **EndingHashKey** *(string) --*

        The ending hash key of the hash key range.

    - **SequenceNumberRange** *(dict) --*

      The range of possible sequence numbers for the shard.

      - **StartingSequenceNumber** *(string) --*

        The starting sequence number for the range.

      - **EndingSequenceNumber** *(string) --*

        The ending sequence number for the range. Shards that are in the OPEN state have an
        ending sequence number of ``null`` .
    """


_DescribeStreamPaginateResponseStreamDescriptionTypeDef = TypedDict(
    "_DescribeStreamPaginateResponseStreamDescriptionTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": str,
        "Shards": List[DescribeStreamPaginateResponseStreamDescriptionShardsTypeDef],
        "HasMoreShards": bool,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List[
            DescribeStreamPaginateResponseStreamDescriptionEnhancedMonitoringTypeDef
        ],
        "EncryptionType": str,
        "KeyId": str,
    },
    total=False,
)


class DescribeStreamPaginateResponseStreamDescriptionTypeDef(
    _DescribeStreamPaginateResponseStreamDescriptionTypeDef
):
    """
    Type definition for `DescribeStreamPaginateResponse` `StreamDescription`

    The current status of the stream, the stream Amazon Resource Name (ARN), an array of shard
    objects that comprise the stream, and whether there are more shards available.

    - **StreamName** *(string) --*

      The name of the stream being described.

    - **StreamARN** *(string) --*

      The Amazon Resource Name (ARN) for the stream being described.

    - **StreamStatus** *(string) --*

      The current status of the stream being described. The stream status is one of the following
      states:

      * ``CREATING`` - The stream is being created. Kinesis Data Streams immediately returns and
      sets ``StreamStatus`` to ``CREATING`` .

      * ``DELETING`` - The stream is being deleted. The specified stream is in the ``DELETING``
      state until Kinesis Data Streams completes the deletion.

      * ``ACTIVE`` - The stream exists and is ready for read and write operations or deletion.
      You should perform read and write operations only on an ``ACTIVE`` stream.

      * ``UPDATING`` - Shards in the stream are being merged or split. Read and write operations
      continue to work while the stream is in the ``UPDATING`` state.

    - **Shards** *(list) --*

      The shards that comprise the stream.

      - *(dict) --*

        A uniquely identified group of data records in a Kinesis data stream.

        - **ShardId** *(string) --*

          The unique identifier of the shard within the stream.

        - **ParentShardId** *(string) --*

          The shard ID of the shard's parent.

        - **AdjacentParentShardId** *(string) --*

          The shard ID of the shard adjacent to the shard's parent.

        - **HashKeyRange** *(dict) --*

          The range of possible hash key values for the shard, which is a set of ordered
          contiguous positive integers.

          - **StartingHashKey** *(string) --*

            The starting hash key of the hash key range.

          - **EndingHashKey** *(string) --*

            The ending hash key of the hash key range.

        - **SequenceNumberRange** *(dict) --*

          The range of possible sequence numbers for the shard.

          - **StartingSequenceNumber** *(string) --*

            The starting sequence number for the range.

          - **EndingSequenceNumber** *(string) --*

            The ending sequence number for the range. Shards that are in the OPEN state have an
            ending sequence number of ``null`` .

    - **HasMoreShards** *(boolean) --*

      If set to ``true`` , more shards in the stream are available to describe.

    - **RetentionPeriodHours** *(integer) --*

      The current retention period, in hours.

    - **StreamCreationTimestamp** *(datetime) --*

      The approximate time that the stream was created.

    - **EnhancedMonitoring** *(list) --*

      Represents the current enhanced monitoring settings of the stream.

      - *(dict) --*

        Represents enhanced metrics types.

        - **ShardLevelMetrics** *(list) --*

          List of shard-level metrics.

          The following are the valid shard-level metrics. The value "``ALL`` " enhances every
          metric.

          * ``IncomingBytes``

          * ``IncomingRecords``

          * ``OutgoingBytes``

          * ``OutgoingRecords``

          * ``WriteProvisionedThroughputExceeded``

          * ``ReadProvisionedThroughputExceeded``

          * ``IteratorAgeMilliseconds``

          * ``ALL``

          For more information, see `Monitoring the Amazon Kinesis Data Streams Service with
          Amazon CloudWatch
          <http://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html>`__ in
          the *Amazon Kinesis Data Streams Developer Guide* .

          - *(string) --*

    - **EncryptionType** *(string) --*

      The server-side encryption type used on the stream. This parameter can be one of the
      following values:

      * ``NONE`` : Do not encrypt the records in the stream.

      * ``KMS`` : Use server-side encryption on the records in the stream using a
      customer-managed AWS KMS key.

    - **KeyId** *(string) --*

      The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a
      globally unique identifier, a fully specified ARN to either an alias or a key, or an alias
      name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by
      specifying the alias ``aws/kinesis`` .

      * Key ARN example:
      ``arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012``

      * Alias ARN example: ``arn:aws:kms:us-east-1:123456789012:alias/MyAliasName``

      * Globally unique key ID example: ``12345678-1234-1234-1234-123456789012``

      * Alias name example: ``alias/MyAliasName``

      * Master key owned by Kinesis Data Streams: ``alias/aws/kinesis``
    """


_DescribeStreamPaginateResponseTypeDef = TypedDict(
    "_DescribeStreamPaginateResponseTypeDef",
    {
        "StreamDescription": DescribeStreamPaginateResponseStreamDescriptionTypeDef,
        "NextToken": str,
    },
    total=False,
)


class DescribeStreamPaginateResponseTypeDef(_DescribeStreamPaginateResponseTypeDef):
    """
    Type definition for `DescribeStreamPaginate` `Response`

    Represents the output for ``DescribeStream`` .

    - **StreamDescription** *(dict) --*

      The current status of the stream, the stream Amazon Resource Name (ARN), an array of shard
      objects that comprise the stream, and whether there are more shards available.

      - **StreamName** *(string) --*

        The name of the stream being described.

      - **StreamARN** *(string) --*

        The Amazon Resource Name (ARN) for the stream being described.

      - **StreamStatus** *(string) --*

        The current status of the stream being described. The stream status is one of the following
        states:

        * ``CREATING`` - The stream is being created. Kinesis Data Streams immediately returns and
        sets ``StreamStatus`` to ``CREATING`` .

        * ``DELETING`` - The stream is being deleted. The specified stream is in the ``DELETING``
        state until Kinesis Data Streams completes the deletion.

        * ``ACTIVE`` - The stream exists and is ready for read and write operations or deletion.
        You should perform read and write operations only on an ``ACTIVE`` stream.

        * ``UPDATING`` - Shards in the stream are being merged or split. Read and write operations
        continue to work while the stream is in the ``UPDATING`` state.

      - **Shards** *(list) --*

        The shards that comprise the stream.

        - *(dict) --*

          A uniquely identified group of data records in a Kinesis data stream.

          - **ShardId** *(string) --*

            The unique identifier of the shard within the stream.

          - **ParentShardId** *(string) --*

            The shard ID of the shard's parent.

          - **AdjacentParentShardId** *(string) --*

            The shard ID of the shard adjacent to the shard's parent.

          - **HashKeyRange** *(dict) --*

            The range of possible hash key values for the shard, which is a set of ordered
            contiguous positive integers.

            - **StartingHashKey** *(string) --*

              The starting hash key of the hash key range.

            - **EndingHashKey** *(string) --*

              The ending hash key of the hash key range.

          - **SequenceNumberRange** *(dict) --*

            The range of possible sequence numbers for the shard.

            - **StartingSequenceNumber** *(string) --*

              The starting sequence number for the range.

            - **EndingSequenceNumber** *(string) --*

              The ending sequence number for the range. Shards that are in the OPEN state have an
              ending sequence number of ``null`` .

      - **HasMoreShards** *(boolean) --*

        If set to ``true`` , more shards in the stream are available to describe.

      - **RetentionPeriodHours** *(integer) --*

        The current retention period, in hours.

      - **StreamCreationTimestamp** *(datetime) --*

        The approximate time that the stream was created.

      - **EnhancedMonitoring** *(list) --*

        Represents the current enhanced monitoring settings of the stream.

        - *(dict) --*

          Represents enhanced metrics types.

          - **ShardLevelMetrics** *(list) --*

            List of shard-level metrics.

            The following are the valid shard-level metrics. The value "``ALL`` " enhances every
            metric.

            * ``IncomingBytes``

            * ``IncomingRecords``

            * ``OutgoingBytes``

            * ``OutgoingRecords``

            * ``WriteProvisionedThroughputExceeded``

            * ``ReadProvisionedThroughputExceeded``

            * ``IteratorAgeMilliseconds``

            * ``ALL``

            For more information, see `Monitoring the Amazon Kinesis Data Streams Service with
            Amazon CloudWatch
            <http://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html>`__ in
            the *Amazon Kinesis Data Streams Developer Guide* .

            - *(string) --*

      - **EncryptionType** *(string) --*

        The server-side encryption type used on the stream. This parameter can be one of the
        following values:

        * ``NONE`` : Do not encrypt the records in the stream.

        * ``KMS`` : Use server-side encryption on the records in the stream using a
        customer-managed AWS KMS key.

      - **KeyId** *(string) --*

        The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a
        globally unique identifier, a fully specified ARN to either an alias or a key, or an alias
        name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by
        specifying the alias ``aws/kinesis`` .

        * Key ARN example:
        ``arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012``

        * Alias ARN example: ``arn:aws:kms:us-east-1:123456789012:alias/MyAliasName``

        * Globally unique key ID example: ``12345678-1234-1234-1234-123456789012``

        * Alias name example: ``alias/MyAliasName``

        * Master key owned by Kinesis Data Streams: ``alias/aws/kinesis``

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListShardsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListShardsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListShardsPaginatePaginationConfigTypeDef(
    _ListShardsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListShardsPaginate` `PaginationConfig`

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


_ListShardsPaginateResponseShardsHashKeyRangeTypeDef = TypedDict(
    "_ListShardsPaginateResponseShardsHashKeyRangeTypeDef",
    {"StartingHashKey": str, "EndingHashKey": str},
    total=False,
)


class ListShardsPaginateResponseShardsHashKeyRangeTypeDef(
    _ListShardsPaginateResponseShardsHashKeyRangeTypeDef
):
    """
    Type definition for `ListShardsPaginateResponseShards` `HashKeyRange`

    The range of possible hash key values for the shard, which is a set of ordered contiguous
    positive integers.

    - **StartingHashKey** *(string) --*

      The starting hash key of the hash key range.

    - **EndingHashKey** *(string) --*

      The ending hash key of the hash key range.
    """


_ListShardsPaginateResponseShardsSequenceNumberRangeTypeDef = TypedDict(
    "_ListShardsPaginateResponseShardsSequenceNumberRangeTypeDef",
    {"StartingSequenceNumber": str, "EndingSequenceNumber": str},
    total=False,
)


class ListShardsPaginateResponseShardsSequenceNumberRangeTypeDef(
    _ListShardsPaginateResponseShardsSequenceNumberRangeTypeDef
):
    """
    Type definition for `ListShardsPaginateResponseShards` `SequenceNumberRange`

    The range of possible sequence numbers for the shard.

    - **StartingSequenceNumber** *(string) --*

      The starting sequence number for the range.

    - **EndingSequenceNumber** *(string) --*

      The ending sequence number for the range. Shards that are in the OPEN state have an
      ending sequence number of ``null`` .
    """


_ListShardsPaginateResponseShardsTypeDef = TypedDict(
    "_ListShardsPaginateResponseShardsTypeDef",
    {
        "ShardId": str,
        "ParentShardId": str,
        "AdjacentParentShardId": str,
        "HashKeyRange": ListShardsPaginateResponseShardsHashKeyRangeTypeDef,
        "SequenceNumberRange": ListShardsPaginateResponseShardsSequenceNumberRangeTypeDef,
    },
    total=False,
)


class ListShardsPaginateResponseShardsTypeDef(_ListShardsPaginateResponseShardsTypeDef):
    """
    Type definition for `ListShardsPaginateResponse` `Shards`

    A uniquely identified group of data records in a Kinesis data stream.

    - **ShardId** *(string) --*

      The unique identifier of the shard within the stream.

    - **ParentShardId** *(string) --*

      The shard ID of the shard's parent.

    - **AdjacentParentShardId** *(string) --*

      The shard ID of the shard adjacent to the shard's parent.

    - **HashKeyRange** *(dict) --*

      The range of possible hash key values for the shard, which is a set of ordered contiguous
      positive integers.

      - **StartingHashKey** *(string) --*

        The starting hash key of the hash key range.

      - **EndingHashKey** *(string) --*

        The ending hash key of the hash key range.

    - **SequenceNumberRange** *(dict) --*

      The range of possible sequence numbers for the shard.

      - **StartingSequenceNumber** *(string) --*

        The starting sequence number for the range.

      - **EndingSequenceNumber** *(string) --*

        The ending sequence number for the range. Shards that are in the OPEN state have an
        ending sequence number of ``null`` .
    """


_ListShardsPaginateResponseTypeDef = TypedDict(
    "_ListShardsPaginateResponseTypeDef",
    {"Shards": List[ListShardsPaginateResponseShardsTypeDef]},
    total=False,
)


class ListShardsPaginateResponseTypeDef(_ListShardsPaginateResponseTypeDef):
    """
    Type definition for `ListShardsPaginate` `Response`

    - **Shards** *(list) --*

      An array of JSON objects. Each object represents one shard and specifies the IDs of the
      shard, the shard's parent, and the shard that's adjacent to the shard's parent. Each object
      also contains the starting and ending hash keys and the starting and ending sequence numbers
      for the shard.

      - *(dict) --*

        A uniquely identified group of data records in a Kinesis data stream.

        - **ShardId** *(string) --*

          The unique identifier of the shard within the stream.

        - **ParentShardId** *(string) --*

          The shard ID of the shard's parent.

        - **AdjacentParentShardId** *(string) --*

          The shard ID of the shard adjacent to the shard's parent.

        - **HashKeyRange** *(dict) --*

          The range of possible hash key values for the shard, which is a set of ordered contiguous
          positive integers.

          - **StartingHashKey** *(string) --*

            The starting hash key of the hash key range.

          - **EndingHashKey** *(string) --*

            The ending hash key of the hash key range.

        - **SequenceNumberRange** *(dict) --*

          The range of possible sequence numbers for the shard.

          - **StartingSequenceNumber** *(string) --*

            The starting sequence number for the range.

          - **EndingSequenceNumber** *(string) --*

            The ending sequence number for the range. Shards that are in the OPEN state have an
            ending sequence number of ``null`` .
    """


_ListStreamConsumersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStreamConsumersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStreamConsumersPaginatePaginationConfigTypeDef(
    _ListStreamConsumersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListStreamConsumersPaginate` `PaginationConfig`

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


_ListStreamConsumersPaginateResponseConsumersTypeDef = TypedDict(
    "_ListStreamConsumersPaginateResponseConsumersTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": str,
        "ConsumerCreationTimestamp": datetime,
    },
    total=False,
)


class ListStreamConsumersPaginateResponseConsumersTypeDef(
    _ListStreamConsumersPaginateResponseConsumersTypeDef
):
    """
    Type definition for `ListStreamConsumersPaginateResponse` `Consumers`

    An object that represents the details of the consumer you registered.

    - **ConsumerName** *(string) --*

      The name of the consumer is something you choose when you register the consumer.

    - **ConsumerARN** *(string) --*

      When you register a consumer, Kinesis Data Streams generates an ARN for it. You need this
      ARN to be able to call  SubscribeToShard .

      If you delete a consumer and then create a new one with the same name, it won't have the
      same ARN. That's because consumer ARNs contain the creation timestamp. This is important
      to keep in mind if you have IAM policies that reference consumer ARNs.

    - **ConsumerStatus** *(string) --*

      A consumer can't read data while in the ``CREATING`` or ``DELETING`` states.

    - **ConsumerCreationTimestamp** *(datetime) --*
    """


_ListStreamConsumersPaginateResponseTypeDef = TypedDict(
    "_ListStreamConsumersPaginateResponseTypeDef",
    {"Consumers": List[ListStreamConsumersPaginateResponseConsumersTypeDef]},
    total=False,
)


class ListStreamConsumersPaginateResponseTypeDef(
    _ListStreamConsumersPaginateResponseTypeDef
):
    """
    Type definition for `ListStreamConsumersPaginate` `Response`

    - **Consumers** *(list) --*

      An array of JSON objects. Each object represents one registered consumer.

      - *(dict) --*

        An object that represents the details of the consumer you registered.

        - **ConsumerName** *(string) --*

          The name of the consumer is something you choose when you register the consumer.

        - **ConsumerARN** *(string) --*

          When you register a consumer, Kinesis Data Streams generates an ARN for it. You need this
          ARN to be able to call  SubscribeToShard .

          If you delete a consumer and then create a new one with the same name, it won't have the
          same ARN. That's because consumer ARNs contain the creation timestamp. This is important
          to keep in mind if you have IAM policies that reference consumer ARNs.

        - **ConsumerStatus** *(string) --*

          A consumer can't read data while in the ``CREATING`` or ``DELETING`` states.

        - **ConsumerCreationTimestamp** *(datetime) --*
    """


_ListStreamsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListStreamsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListStreamsPaginatePaginationConfigTypeDef(
    _ListStreamsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListStreamsPaginate` `PaginationConfig`

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


_ListStreamsPaginateResponseTypeDef = TypedDict(
    "_ListStreamsPaginateResponseTypeDef",
    {"StreamNames": List[str], "HasMoreStreams": bool, "NextToken": str},
    total=False,
)


class ListStreamsPaginateResponseTypeDef(_ListStreamsPaginateResponseTypeDef):
    """
    Type definition for `ListStreamsPaginate` `Response`

    Represents the output for ``ListStreams`` .

    - **StreamNames** *(list) --*

      The names of the streams that are associated with the AWS account making the ``ListStreams``
      request.

      - *(string) --*

    - **HasMoreStreams** *(boolean) --*

      If set to ``true`` , there are more streams available to list.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_StreamExistsWaitWaiterConfigTypeDef = TypedDict(
    "_StreamExistsWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class StreamExistsWaitWaiterConfigTypeDef(_StreamExistsWaitWaiterConfigTypeDef):
    """
    Type definition for `StreamExistsWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 10

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 18
    """


_StreamNotExistsWaitWaiterConfigTypeDef = TypedDict(
    "_StreamNotExistsWaitWaiterConfigTypeDef",
    {"Delay": int, "MaxAttempts": int},
    total=False,
)


class StreamNotExistsWaitWaiterConfigTypeDef(_StreamNotExistsWaitWaiterConfigTypeDef):
    """
    Type definition for `StreamNotExistsWait` `WaiterConfig`

    A dictionary that provides parameters to control waiting behavior.

    - **Delay** *(integer) --*

      The amount of time in seconds to wait between attempts. Default: 10

    - **MaxAttempts** *(integer) --*

      The maximum number of attempts to be made. Default: 18
    """

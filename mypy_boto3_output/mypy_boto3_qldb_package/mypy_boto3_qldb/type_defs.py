"Main interface for qldb type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateLedgerResponseTypeDef",
    "ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationEncryptionConfigurationTypeDef",
    "ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationTypeDef",
    "ClientDescribeJournalS3ExportResponseExportDescriptionTypeDef",
    "ClientDescribeJournalS3ExportResponseTypeDef",
    "ClientDescribeLedgerResponseTypeDef",
    "ClientExportJournalToS3ResponseTypeDef",
    "ClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef",
    "ClientExportJournalToS3S3ExportConfigurationTypeDef",
    "ClientGetBlockBlockAddressTypeDef",
    "ClientGetBlockDigestTipAddressTypeDef",
    "ClientGetBlockResponseBlockTypeDef",
    "ClientGetBlockResponseProofTypeDef",
    "ClientGetBlockResponseTypeDef",
    "ClientGetDigestResponseDigestTipAddressTypeDef",
    "ClientGetDigestResponseTypeDef",
    "ClientGetRevisionBlockAddressTypeDef",
    "ClientGetRevisionDigestTipAddressTypeDef",
    "ClientGetRevisionResponseProofTypeDef",
    "ClientGetRevisionResponseRevisionTypeDef",
    "ClientGetRevisionResponseTypeDef",
    "ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef",
    "ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationTypeDef",
    "ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsTypeDef",
    "ClientListJournalS3ExportsForLedgerResponseTypeDef",
    "ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef",
    "ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationTypeDef",
    "ClientListJournalS3ExportsResponseJournalS3ExportsTypeDef",
    "ClientListJournalS3ExportsResponseTypeDef",
    "ClientListLedgersResponseLedgersTypeDef",
    "ClientListLedgersResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientUpdateLedgerResponseTypeDef",
)


_ClientCreateLedgerResponseTypeDef = TypedDict(
    "_ClientCreateLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": str,
        "CreationDateTime": datetime,
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientCreateLedgerResponseTypeDef(_ClientCreateLedgerResponseTypeDef):
    """
    Type definition for `ClientCreateLedger` `Response`

    - **Name** *(string) --*

      The name of the ledger.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the ledger.

    - **State** *(string) --*

      The current status of the ledger.

    - **CreationDateTime** *(datetime) --*

      The date and time, in epoch time format, when the ledger was created. (Epoch time format is
      the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

    - **DeletionProtection** *(boolean) --*

      The flag that prevents a ledger from being deleted by any user. If not provided on ledger
      creation, this feature is enabled (``true`` ) by default.

      If deletion protection is enabled, you must first disable it before you can delete the ledger
      using the QLDB API or the AWS Command Line Interface (AWS CLI). You can disable it by calling
      the ``UpdateLedger`` operation to set the flag to ``false`` . The QLDB console disables
      deletion protection for you when you use it to delete a ledger.
    """


_ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationEncryptionConfigurationTypeDef",
    {"ObjectEncryptionType": str, "KmsKeyArn": str},
    total=False,
)


class ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationEncryptionConfigurationTypeDef(
    _ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfiguration` `EncryptionConfiguration`

    The encryption settings that are used by a journal export job to write data in an Amazon
    S3 bucket.

    - **ObjectEncryptionType** *(string) --*

      The Amazon S3 object encryption type.

      To learn more about server-side encryption options in Amazon S3, see `Protecting Data
      Using Server-Side Encryption
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`__ in the
      *Amazon S3 Developer Guide* .

    - **KmsKeyArn** *(string) --*

      The Amazon Resource Name (ARN) for a customer master key (CMK) in AWS Key Management
      Service (AWS KMS).

      You must provide a ``KmsKeyArn`` if you specify ``SSE_KMS`` as the
      ``ObjectEncryptionType`` .

       ``KmsKeyArn`` is not required if you specify ``SSE_S3`` as the
       ``ObjectEncryptionType`` .
    """


_ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationTypeDef = TypedDict(
    "_ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationTypeDef",
    {
        "Bucket": str,
        "Prefix": str,
        "EncryptionConfiguration": ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationTypeDef(
    _ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationTypeDef
):
    """
    Type definition for `ClientDescribeJournalS3ExportResponseExportDescription` `S3ExportConfiguration`

    The Amazon Simple Storage Service (Amazon S3) bucket location in which a journal export job
    writes the journal contents.

    - **Bucket** *(string) --*

      The Amazon S3 bucket name in which a journal export job writes the journal contents.

      The bucket name must comply with the Amazon S3 bucket naming conventions. For more
      information, see `Bucket Restrictions and Limitations
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html>`__ in the
      *Amazon S3 Developer Guide* .

    - **Prefix** *(string) --*

      The prefix for the Amazon S3 bucket in which a journal export job writes the journal
      contents.

      The prefix must comply with Amazon S3 key naming rules and restrictions. For more
      information, see `Object Key and Metadata
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html>`__ in the *Amazon S3
      Developer Guide* .

      The following are examples of valid ``Prefix`` values:

      * ``JournalExports-ForMyLedger/Testing/``

      * ``JournalExports``

      * ``My:Tests/``

    - **EncryptionConfiguration** *(dict) --*

      The encryption settings that are used by a journal export job to write data in an Amazon
      S3 bucket.

      - **ObjectEncryptionType** *(string) --*

        The Amazon S3 object encryption type.

        To learn more about server-side encryption options in Amazon S3, see `Protecting Data
        Using Server-Side Encryption
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`__ in the
        *Amazon S3 Developer Guide* .

      - **KmsKeyArn** *(string) --*

        The Amazon Resource Name (ARN) for a customer master key (CMK) in AWS Key Management
        Service (AWS KMS).

        You must provide a ``KmsKeyArn`` if you specify ``SSE_KMS`` as the
        ``ObjectEncryptionType`` .

         ``KmsKeyArn`` is not required if you specify ``SSE_S3`` as the
         ``ObjectEncryptionType`` .
    """


_ClientDescribeJournalS3ExportResponseExportDescriptionTypeDef = TypedDict(
    "_ClientDescribeJournalS3ExportResponseExportDescriptionTypeDef",
    {
        "LedgerName": str,
        "ExportId": str,
        "ExportCreationTime": datetime,
        "Status": str,
        "InclusiveStartTime": datetime,
        "ExclusiveEndTime": datetime,
        "S3ExportConfiguration": ClientDescribeJournalS3ExportResponseExportDescriptionS3ExportConfigurationTypeDef,
        "RoleArn": str,
    },
    total=False,
)


class ClientDescribeJournalS3ExportResponseExportDescriptionTypeDef(
    _ClientDescribeJournalS3ExportResponseExportDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeJournalS3ExportResponse` `ExportDescription`

    Information about the journal export job returned by a ``DescribeJournalS3Export`` request.

    - **LedgerName** *(string) --*

      The name of the ledger.

    - **ExportId** *(string) --*

      The unique ID of the journal export job.

    - **ExportCreationTime** *(datetime) --*

      The date and time, in epoch time format, when the export job was created. (Epoch time
      format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

    - **Status** *(string) --*

      The current state of the journal export job.

    - **InclusiveStartTime** *(datetime) --*

      The inclusive start date and time for the range of journal contents that are specified in
      the original export request.

    - **ExclusiveEndTime** *(datetime) --*

      The exclusive end date and time for the range of journal contents that are specified in the
      original export request.

    - **S3ExportConfiguration** *(dict) --*

      The Amazon Simple Storage Service (Amazon S3) bucket location in which a journal export job
      writes the journal contents.

      - **Bucket** *(string) --*

        The Amazon S3 bucket name in which a journal export job writes the journal contents.

        The bucket name must comply with the Amazon S3 bucket naming conventions. For more
        information, see `Bucket Restrictions and Limitations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html>`__ in the
        *Amazon S3 Developer Guide* .

      - **Prefix** *(string) --*

        The prefix for the Amazon S3 bucket in which a journal export job writes the journal
        contents.

        The prefix must comply with Amazon S3 key naming rules and restrictions. For more
        information, see `Object Key and Metadata
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html>`__ in the *Amazon S3
        Developer Guide* .

        The following are examples of valid ``Prefix`` values:

        * ``JournalExports-ForMyLedger/Testing/``

        * ``JournalExports``

        * ``My:Tests/``

      - **EncryptionConfiguration** *(dict) --*

        The encryption settings that are used by a journal export job to write data in an Amazon
        S3 bucket.

        - **ObjectEncryptionType** *(string) --*

          The Amazon S3 object encryption type.

          To learn more about server-side encryption options in Amazon S3, see `Protecting Data
          Using Server-Side Encryption
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`__ in the
          *Amazon S3 Developer Guide* .

        - **KmsKeyArn** *(string) --*

          The Amazon Resource Name (ARN) for a customer master key (CMK) in AWS Key Management
          Service (AWS KMS).

          You must provide a ``KmsKeyArn`` if you specify ``SSE_KMS`` as the
          ``ObjectEncryptionType`` .

           ``KmsKeyArn`` is not required if you specify ``SSE_S3`` as the
           ``ObjectEncryptionType`` .

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal
      export job to do the following:

      * Write objects into your Amazon Simple Storage Service (Amazon S3) bucket.

      * (Optional) Use your customer master key (CMK) in AWS Key Management Service (AWS KMS) for
      server-side encryption of your exported data.
    """


_ClientDescribeJournalS3ExportResponseTypeDef = TypedDict(
    "_ClientDescribeJournalS3ExportResponseTypeDef",
    {
        "ExportDescription": ClientDescribeJournalS3ExportResponseExportDescriptionTypeDef
    },
    total=False,
)


class ClientDescribeJournalS3ExportResponseTypeDef(
    _ClientDescribeJournalS3ExportResponseTypeDef
):
    """
    Type definition for `ClientDescribeJournalS3Export` `Response`

    - **ExportDescription** *(dict) --*

      Information about the journal export job returned by a ``DescribeJournalS3Export`` request.

      - **LedgerName** *(string) --*

        The name of the ledger.

      - **ExportId** *(string) --*

        The unique ID of the journal export job.

      - **ExportCreationTime** *(datetime) --*

        The date and time, in epoch time format, when the export job was created. (Epoch time
        format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

      - **Status** *(string) --*

        The current state of the journal export job.

      - **InclusiveStartTime** *(datetime) --*

        The inclusive start date and time for the range of journal contents that are specified in
        the original export request.

      - **ExclusiveEndTime** *(datetime) --*

        The exclusive end date and time for the range of journal contents that are specified in the
        original export request.

      - **S3ExportConfiguration** *(dict) --*

        The Amazon Simple Storage Service (Amazon S3) bucket location in which a journal export job
        writes the journal contents.

        - **Bucket** *(string) --*

          The Amazon S3 bucket name in which a journal export job writes the journal contents.

          The bucket name must comply with the Amazon S3 bucket naming conventions. For more
          information, see `Bucket Restrictions and Limitations
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html>`__ in the
          *Amazon S3 Developer Guide* .

        - **Prefix** *(string) --*

          The prefix for the Amazon S3 bucket in which a journal export job writes the journal
          contents.

          The prefix must comply with Amazon S3 key naming rules and restrictions. For more
          information, see `Object Key and Metadata
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html>`__ in the *Amazon S3
          Developer Guide* .

          The following are examples of valid ``Prefix`` values:

          * ``JournalExports-ForMyLedger/Testing/``

          * ``JournalExports``

          * ``My:Tests/``

        - **EncryptionConfiguration** *(dict) --*

          The encryption settings that are used by a journal export job to write data in an Amazon
          S3 bucket.

          - **ObjectEncryptionType** *(string) --*

            The Amazon S3 object encryption type.

            To learn more about server-side encryption options in Amazon S3, see `Protecting Data
            Using Server-Side Encryption
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`__ in the
            *Amazon S3 Developer Guide* .

          - **KmsKeyArn** *(string) --*

            The Amazon Resource Name (ARN) for a customer master key (CMK) in AWS Key Management
            Service (AWS KMS).

            You must provide a ``KmsKeyArn`` if you specify ``SSE_KMS`` as the
            ``ObjectEncryptionType`` .

             ``KmsKeyArn`` is not required if you specify ``SSE_S3`` as the
             ``ObjectEncryptionType`` .

      - **RoleArn** *(string) --*

        The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal
        export job to do the following:

        * Write objects into your Amazon Simple Storage Service (Amazon S3) bucket.

        * (Optional) Use your customer master key (CMK) in AWS Key Management Service (AWS KMS) for
        server-side encryption of your exported data.
    """


_ClientDescribeLedgerResponseTypeDef = TypedDict(
    "_ClientDescribeLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": str,
        "CreationDateTime": datetime,
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientDescribeLedgerResponseTypeDef(_ClientDescribeLedgerResponseTypeDef):
    """
    Type definition for `ClientDescribeLedger` `Response`

    - **Name** *(string) --*

      The name of the ledger.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the ledger.

    - **State** *(string) --*

      The current status of the ledger.

    - **CreationDateTime** *(datetime) --*

      The date and time, in epoch time format, when the ledger was created. (Epoch time format is
      the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

    - **DeletionProtection** *(boolean) --*

      The flag that prevents a ledger from being deleted by any user. If not provided on ledger
      creation, this feature is enabled (``true`` ) by default.

      If deletion protection is enabled, you must first disable it before you can delete the ledger
      using the QLDB API or the AWS Command Line Interface (AWS CLI). You can disable it by calling
      the ``UpdateLedger`` operation to set the flag to ``false`` . The QLDB console disables
      deletion protection for you when you use it to delete a ledger.
    """


_ClientExportJournalToS3ResponseTypeDef = TypedDict(
    "_ClientExportJournalToS3ResponseTypeDef", {"ExportId": str}, total=False
)


class ClientExportJournalToS3ResponseTypeDef(_ClientExportJournalToS3ResponseTypeDef):
    """
    Type definition for `ClientExportJournalToS3` `Response`

    - **ExportId** *(string) --*

      The unique ID that QLDB assigns to each journal export job.

      To describe your export request and check the status of the job, you can use ``ExportId`` to
      call ``DescribeJournalS3Export`` .
    """


_RequiredClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef",
    {"ObjectEncryptionType": str},
)
_OptionalClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef",
    {"KmsKeyArn": str},
    total=False,
)


class ClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef(
    _RequiredClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef,
    _OptionalClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef,
):
    """
    Type definition for `ClientExportJournalToS3S3ExportConfiguration` `EncryptionConfiguration`

    The encryption settings that are used by a journal export job to write data in an Amazon S3
    bucket.

    - **ObjectEncryptionType** *(string) --* **[REQUIRED]**

      The Amazon S3 object encryption type.

      To learn more about server-side encryption options in Amazon S3, see `Protecting Data Using
      Server-Side Encryption
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`__ in the *Amazon
      S3 Developer Guide* .

    - **KmsKeyArn** *(string) --*

      The Amazon Resource Name (ARN) for a customer master key (CMK) in AWS Key Management Service
      (AWS KMS).

      You must provide a ``KmsKeyArn`` if you specify ``SSE_KMS`` as the ``ObjectEncryptionType`` .

       ``KmsKeyArn`` is not required if you specify ``SSE_S3`` as the ``ObjectEncryptionType`` .
    """


_ClientExportJournalToS3S3ExportConfigurationTypeDef = TypedDict(
    "_ClientExportJournalToS3S3ExportConfigurationTypeDef",
    {
        "Bucket": str,
        "Prefix": str,
        "EncryptionConfiguration": ClientExportJournalToS3S3ExportConfigurationEncryptionConfigurationTypeDef,
    },
)


class ClientExportJournalToS3S3ExportConfigurationTypeDef(
    _ClientExportJournalToS3S3ExportConfigurationTypeDef
):
    """
    Type definition for `ClientExportJournalToS3` `S3ExportConfiguration`

    The configuration settings of the Amazon S3 bucket destination for your export request.

    - **Bucket** *(string) --* **[REQUIRED]**

      The Amazon S3 bucket name in which a journal export job writes the journal contents.

      The bucket name must comply with the Amazon S3 bucket naming conventions. For more information,
      see `Bucket Restrictions and Limitations
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html>`__ in the *Amazon S3
      Developer Guide* .

    - **Prefix** *(string) --* **[REQUIRED]**

      The prefix for the Amazon S3 bucket in which a journal export job writes the journal contents.

      The prefix must comply with Amazon S3 key naming rules and restrictions. For more information,
      see `Object Key and Metadata
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html>`__ in the *Amazon S3
      Developer Guide* .

      The following are examples of valid ``Prefix`` values:

      * ``JournalExports-ForMyLedger/Testing/``

      * ``JournalExports``

      * ``My:Tests/``

    - **EncryptionConfiguration** *(dict) --* **[REQUIRED]**

      The encryption settings that are used by a journal export job to write data in an Amazon S3
      bucket.

      - **ObjectEncryptionType** *(string) --* **[REQUIRED]**

        The Amazon S3 object encryption type.

        To learn more about server-side encryption options in Amazon S3, see `Protecting Data Using
        Server-Side Encryption
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`__ in the *Amazon
        S3 Developer Guide* .

      - **KmsKeyArn** *(string) --*

        The Amazon Resource Name (ARN) for a customer master key (CMK) in AWS Key Management Service
        (AWS KMS).

        You must provide a ``KmsKeyArn`` if you specify ``SSE_KMS`` as the ``ObjectEncryptionType`` .

         ``KmsKeyArn`` is not required if you specify ``SSE_S3`` as the ``ObjectEncryptionType`` .
    """


_ClientGetBlockBlockAddressTypeDef = TypedDict(
    "_ClientGetBlockBlockAddressTypeDef", {"IonText": str}, total=False
)


class ClientGetBlockBlockAddressTypeDef(_ClientGetBlockBlockAddressTypeDef):
    """
    Type definition for `ClientGetBlock` `BlockAddress`

    The location of the block that you want to request. An address is an Amazon Ion structure that
    has two fields: ``strandId`` and ``sequenceNo`` .

    For example: ``{strandId:"BlFTjlSXze9BIh1KOszcE3",sequenceNo:14}``

    - **IonText** *(string) --*

      An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientGetBlockDigestTipAddressTypeDef = TypedDict(
    "_ClientGetBlockDigestTipAddressTypeDef", {"IonText": str}, total=False
)


class ClientGetBlockDigestTipAddressTypeDef(_ClientGetBlockDigestTipAddressTypeDef):
    """
    Type definition for `ClientGetBlock` `DigestTipAddress`

    The latest block location covered by the digest for which to request a proof. An address is an
    Amazon Ion structure that has two fields: ``strandId`` and ``sequenceNo`` .

    For example: ``{strandId:"BlFTjlSXze9BIh1KOszcE3",sequenceNo:49}``

    - **IonText** *(string) --*

      An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientGetBlockResponseBlockTypeDef = TypedDict(
    "_ClientGetBlockResponseBlockTypeDef", {"IonText": str}, total=False
)


class ClientGetBlockResponseBlockTypeDef(_ClientGetBlockResponseBlockTypeDef):
    """
    Type definition for `ClientGetBlockResponse` `Block`

    The block data object in Amazon Ion format.

    - **IonText** *(string) --*

      An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientGetBlockResponseProofTypeDef = TypedDict(
    "_ClientGetBlockResponseProofTypeDef", {"IonText": str}, total=False
)


class ClientGetBlockResponseProofTypeDef(_ClientGetBlockResponseProofTypeDef):
    """
    Type definition for `ClientGetBlockResponse` `Proof`

    The proof object in Amazon Ion format returned by a ``GetBlock`` request. A proof contains
    the list of hash values required to recalculate the specified digest using a Merkle tree,
    starting with the specified block.

    - **IonText** *(string) --*

      An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientGetBlockResponseTypeDef = TypedDict(
    "_ClientGetBlockResponseTypeDef",
    {
        "Block": ClientGetBlockResponseBlockTypeDef,
        "Proof": ClientGetBlockResponseProofTypeDef,
    },
    total=False,
)


class ClientGetBlockResponseTypeDef(_ClientGetBlockResponseTypeDef):
    """
    Type definition for `ClientGetBlock` `Response`

    - **Block** *(dict) --*

      The block data object in Amazon Ion format.

      - **IonText** *(string) --*

        An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.

    - **Proof** *(dict) --*

      The proof object in Amazon Ion format returned by a ``GetBlock`` request. A proof contains
      the list of hash values required to recalculate the specified digest using a Merkle tree,
      starting with the specified block.

      - **IonText** *(string) --*

        An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientGetDigestResponseDigestTipAddressTypeDef = TypedDict(
    "_ClientGetDigestResponseDigestTipAddressTypeDef", {"IonText": str}, total=False
)


class ClientGetDigestResponseDigestTipAddressTypeDef(
    _ClientGetDigestResponseDigestTipAddressTypeDef
):
    """
    Type definition for `ClientGetDigestResponse` `DigestTipAddress`

    The latest block location covered by the digest that you requested. An address is an Amazon
    Ion structure that has two fields: ``strandId`` and ``sequenceNo`` .

    - **IonText** *(string) --*

      An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientGetDigestResponseTypeDef = TypedDict(
    "_ClientGetDigestResponseTypeDef",
    {
        "Digest": bytes,
        "DigestTipAddress": ClientGetDigestResponseDigestTipAddressTypeDef,
    },
    total=False,
)


class ClientGetDigestResponseTypeDef(_ClientGetDigestResponseTypeDef):
    """
    Type definition for `ClientGetDigest` `Response`

    - **Digest** *(bytes) --*

      The 256-bit hash value representing the digest returned by a ``GetDigest`` request.

    - **DigestTipAddress** *(dict) --*

      The latest block location covered by the digest that you requested. An address is an Amazon
      Ion structure that has two fields: ``strandId`` and ``sequenceNo`` .

      - **IonText** *(string) --*

        An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientGetRevisionBlockAddressTypeDef = TypedDict(
    "_ClientGetRevisionBlockAddressTypeDef", {"IonText": str}, total=False
)


class ClientGetRevisionBlockAddressTypeDef(_ClientGetRevisionBlockAddressTypeDef):
    """
    Type definition for `ClientGetRevision` `BlockAddress`

    The block location of the document revision to be verified. An address is an Amazon Ion structure
    that has two fields: ``strandId`` and ``sequenceNo`` .

    For example: ``{strandId:"BlFTjlSXze9BIh1KOszcE3",sequenceNo:14}``

    - **IonText** *(string) --*

      An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientGetRevisionDigestTipAddressTypeDef = TypedDict(
    "_ClientGetRevisionDigestTipAddressTypeDef", {"IonText": str}, total=False
)


class ClientGetRevisionDigestTipAddressTypeDef(
    _ClientGetRevisionDigestTipAddressTypeDef
):
    """
    Type definition for `ClientGetRevision` `DigestTipAddress`

    The latest block location covered by the digest for which to request a proof. An address is an
    Amazon Ion structure that has two fields: ``strandId`` and ``sequenceNo`` .

    For example: ``{strandId:"BlFTjlSXze9BIh1KOszcE3",sequenceNo:49}``

    - **IonText** *(string) --*

      An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientGetRevisionResponseProofTypeDef = TypedDict(
    "_ClientGetRevisionResponseProofTypeDef", {"IonText": str}, total=False
)


class ClientGetRevisionResponseProofTypeDef(_ClientGetRevisionResponseProofTypeDef):
    """
    Type definition for `ClientGetRevisionResponse` `Proof`

    The proof object in Amazon Ion format returned by a ``GetRevision`` request. A proof contains
    the list of hash values that are required to recalculate the specified digest using a Merkle
    tree, starting with the specified document revision.

    - **IonText** *(string) --*

      An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientGetRevisionResponseRevisionTypeDef = TypedDict(
    "_ClientGetRevisionResponseRevisionTypeDef", {"IonText": str}, total=False
)


class ClientGetRevisionResponseRevisionTypeDef(
    _ClientGetRevisionResponseRevisionTypeDef
):
    """
    Type definition for `ClientGetRevisionResponse` `Revision`

    The document revision data object in Amazon Ion format.

    - **IonText** *(string) --*

      An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientGetRevisionResponseTypeDef = TypedDict(
    "_ClientGetRevisionResponseTypeDef",
    {
        "Proof": ClientGetRevisionResponseProofTypeDef,
        "Revision": ClientGetRevisionResponseRevisionTypeDef,
    },
    total=False,
)


class ClientGetRevisionResponseTypeDef(_ClientGetRevisionResponseTypeDef):
    """
    Type definition for `ClientGetRevision` `Response`

    - **Proof** *(dict) --*

      The proof object in Amazon Ion format returned by a ``GetRevision`` request. A proof contains
      the list of hash values that are required to recalculate the specified digest using a Merkle
      tree, starting with the specified document revision.

      - **IonText** *(string) --*

        An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.

    - **Revision** *(dict) --*

      The document revision data object in Amazon Ion format.

      - **IonText** *(string) --*

        An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef",
    {"ObjectEncryptionType": str, "KmsKeyArn": str},
    total=False,
)


class ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef(
    _ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfiguration` `EncryptionConfiguration`

    The encryption settings that are used by a journal export job to write data in an
    Amazon S3 bucket.

    - **ObjectEncryptionType** *(string) --*

      The Amazon S3 object encryption type.

      To learn more about server-side encryption options in Amazon S3, see `Protecting Data
      Using Server-Side Encryption
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`__ in the
      *Amazon S3 Developer Guide* .

    - **KmsKeyArn** *(string) --*

      The Amazon Resource Name (ARN) for a customer master key (CMK) in AWS Key Management
      Service (AWS KMS).

      You must provide a ``KmsKeyArn`` if you specify ``SSE_KMS`` as the
      ``ObjectEncryptionType`` .

       ``KmsKeyArn`` is not required if you specify ``SSE_S3`` as the
       ``ObjectEncryptionType`` .
    """


_ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationTypeDef = TypedDict(
    "_ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationTypeDef",
    {
        "Bucket": str,
        "Prefix": str,
        "EncryptionConfiguration": ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationTypeDef(
    _ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationTypeDef
):
    """
    Type definition for `ClientListJournalS3ExportsForLedgerResponseJournalS3Exports` `S3ExportConfiguration`

    The Amazon Simple Storage Service (Amazon S3) bucket location in which a journal export
    job writes the journal contents.

    - **Bucket** *(string) --*

      The Amazon S3 bucket name in which a journal export job writes the journal contents.

      The bucket name must comply with the Amazon S3 bucket naming conventions. For more
      information, see `Bucket Restrictions and Limitations
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html>`__ in the
      *Amazon S3 Developer Guide* .

    - **Prefix** *(string) --*

      The prefix for the Amazon S3 bucket in which a journal export job writes the journal
      contents.

      The prefix must comply with Amazon S3 key naming rules and restrictions. For more
      information, see `Object Key and Metadata
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html>`__ in the *Amazon
      S3 Developer Guide* .

      The following are examples of valid ``Prefix`` values:

      * ``JournalExports-ForMyLedger/Testing/``

      * ``JournalExports``

      * ``My:Tests/``

    - **EncryptionConfiguration** *(dict) --*

      The encryption settings that are used by a journal export job to write data in an
      Amazon S3 bucket.

      - **ObjectEncryptionType** *(string) --*

        The Amazon S3 object encryption type.

        To learn more about server-side encryption options in Amazon S3, see `Protecting Data
        Using Server-Side Encryption
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`__ in the
        *Amazon S3 Developer Guide* .

      - **KmsKeyArn** *(string) --*

        The Amazon Resource Name (ARN) for a customer master key (CMK) in AWS Key Management
        Service (AWS KMS).

        You must provide a ``KmsKeyArn`` if you specify ``SSE_KMS`` as the
        ``ObjectEncryptionType`` .

         ``KmsKeyArn`` is not required if you specify ``SSE_S3`` as the
         ``ObjectEncryptionType`` .
    """


_ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsTypeDef = TypedDict(
    "_ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsTypeDef",
    {
        "LedgerName": str,
        "ExportId": str,
        "ExportCreationTime": datetime,
        "Status": str,
        "InclusiveStartTime": datetime,
        "ExclusiveEndTime": datetime,
        "S3ExportConfiguration": ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsS3ExportConfigurationTypeDef,
        "RoleArn": str,
    },
    total=False,
)


class ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsTypeDef(
    _ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsTypeDef
):
    """
    Type definition for `ClientListJournalS3ExportsForLedgerResponse` `JournalS3Exports`

    The information about a journal export job, including the ledger name, export ID, when it
    was created, current status, and its start and end time export parameters.

    - **LedgerName** *(string) --*

      The name of the ledger.

    - **ExportId** *(string) --*

      The unique ID of the journal export job.

    - **ExportCreationTime** *(datetime) --*

      The date and time, in epoch time format, when the export job was created. (Epoch time
      format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

    - **Status** *(string) --*

      The current state of the journal export job.

    - **InclusiveStartTime** *(datetime) --*

      The inclusive start date and time for the range of journal contents that are specified in
      the original export request.

    - **ExclusiveEndTime** *(datetime) --*

      The exclusive end date and time for the range of journal contents that are specified in
      the original export request.

    - **S3ExportConfiguration** *(dict) --*

      The Amazon Simple Storage Service (Amazon S3) bucket location in which a journal export
      job writes the journal contents.

      - **Bucket** *(string) --*

        The Amazon S3 bucket name in which a journal export job writes the journal contents.

        The bucket name must comply with the Amazon S3 bucket naming conventions. For more
        information, see `Bucket Restrictions and Limitations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html>`__ in the
        *Amazon S3 Developer Guide* .

      - **Prefix** *(string) --*

        The prefix for the Amazon S3 bucket in which a journal export job writes the journal
        contents.

        The prefix must comply with Amazon S3 key naming rules and restrictions. For more
        information, see `Object Key and Metadata
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html>`__ in the *Amazon
        S3 Developer Guide* .

        The following are examples of valid ``Prefix`` values:

        * ``JournalExports-ForMyLedger/Testing/``

        * ``JournalExports``

        * ``My:Tests/``

      - **EncryptionConfiguration** *(dict) --*

        The encryption settings that are used by a journal export job to write data in an
        Amazon S3 bucket.

        - **ObjectEncryptionType** *(string) --*

          The Amazon S3 object encryption type.

          To learn more about server-side encryption options in Amazon S3, see `Protecting Data
          Using Server-Side Encryption
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`__ in the
          *Amazon S3 Developer Guide* .

        - **KmsKeyArn** *(string) --*

          The Amazon Resource Name (ARN) for a customer master key (CMK) in AWS Key Management
          Service (AWS KMS).

          You must provide a ``KmsKeyArn`` if you specify ``SSE_KMS`` as the
          ``ObjectEncryptionType`` .

           ``KmsKeyArn`` is not required if you specify ``SSE_S3`` as the
           ``ObjectEncryptionType`` .

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal
      export job to do the following:

      * Write objects into your Amazon Simple Storage Service (Amazon S3) bucket.

      * (Optional) Use your customer master key (CMK) in AWS Key Management Service (AWS KMS)
      for server-side encryption of your exported data.
    """


_ClientListJournalS3ExportsForLedgerResponseTypeDef = TypedDict(
    "_ClientListJournalS3ExportsForLedgerResponseTypeDef",
    {
        "JournalS3Exports": List[
            ClientListJournalS3ExportsForLedgerResponseJournalS3ExportsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListJournalS3ExportsForLedgerResponseTypeDef(
    _ClientListJournalS3ExportsForLedgerResponseTypeDef
):
    """
    Type definition for `ClientListJournalS3ExportsForLedger` `Response`

    - **JournalS3Exports** *(list) --*

      The array of journal export job descriptions that are associated with the specified ledger.

      - *(dict) --*

        The information about a journal export job, including the ledger name, export ID, when it
        was created, current status, and its start and end time export parameters.

        - **LedgerName** *(string) --*

          The name of the ledger.

        - **ExportId** *(string) --*

          The unique ID of the journal export job.

        - **ExportCreationTime** *(datetime) --*

          The date and time, in epoch time format, when the export job was created. (Epoch time
          format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

        - **Status** *(string) --*

          The current state of the journal export job.

        - **InclusiveStartTime** *(datetime) --*

          The inclusive start date and time for the range of journal contents that are specified in
          the original export request.

        - **ExclusiveEndTime** *(datetime) --*

          The exclusive end date and time for the range of journal contents that are specified in
          the original export request.

        - **S3ExportConfiguration** *(dict) --*

          The Amazon Simple Storage Service (Amazon S3) bucket location in which a journal export
          job writes the journal contents.

          - **Bucket** *(string) --*

            The Amazon S3 bucket name in which a journal export job writes the journal contents.

            The bucket name must comply with the Amazon S3 bucket naming conventions. For more
            information, see `Bucket Restrictions and Limitations
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html>`__ in the
            *Amazon S3 Developer Guide* .

          - **Prefix** *(string) --*

            The prefix for the Amazon S3 bucket in which a journal export job writes the journal
            contents.

            The prefix must comply with Amazon S3 key naming rules and restrictions. For more
            information, see `Object Key and Metadata
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html>`__ in the *Amazon
            S3 Developer Guide* .

            The following are examples of valid ``Prefix`` values:

            * ``JournalExports-ForMyLedger/Testing/``

            * ``JournalExports``

            * ``My:Tests/``

          - **EncryptionConfiguration** *(dict) --*

            The encryption settings that are used by a journal export job to write data in an
            Amazon S3 bucket.

            - **ObjectEncryptionType** *(string) --*

              The Amazon S3 object encryption type.

              To learn more about server-side encryption options in Amazon S3, see `Protecting Data
              Using Server-Side Encryption
              <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`__ in the
              *Amazon S3 Developer Guide* .

            - **KmsKeyArn** *(string) --*

              The Amazon Resource Name (ARN) for a customer master key (CMK) in AWS Key Management
              Service (AWS KMS).

              You must provide a ``KmsKeyArn`` if you specify ``SSE_KMS`` as the
              ``ObjectEncryptionType`` .

               ``KmsKeyArn`` is not required if you specify ``SSE_S3`` as the
               ``ObjectEncryptionType`` .

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal
          export job to do the following:

          * Write objects into your Amazon Simple Storage Service (Amazon S3) bucket.

          * (Optional) Use your customer master key (CMK) in AWS Key Management Service (AWS KMS)
          for server-side encryption of your exported data.

    - **NextToken** *(string) --*

      * If ``NextToken`` is empty, then the last page of results has been processed and there are
      no more results to be retrieved.

      * If ``NextToken`` is *not* empty, then there are more results available. To retrieve the
      next page of results, use the value of ``NextToken`` in a subsequent
      ``ListJournalS3ExportsForLedger`` call.
    """


_ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef = TypedDict(
    "_ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef",
    {"ObjectEncryptionType": str, "KmsKeyArn": str},
    total=False,
)


class ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef(
    _ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef
):
    """
    Type definition for `ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfiguration` `EncryptionConfiguration`

    The encryption settings that are used by a journal export job to write data in an
    Amazon S3 bucket.

    - **ObjectEncryptionType** *(string) --*

      The Amazon S3 object encryption type.

      To learn more about server-side encryption options in Amazon S3, see `Protecting Data
      Using Server-Side Encryption
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`__ in the
      *Amazon S3 Developer Guide* .

    - **KmsKeyArn** *(string) --*

      The Amazon Resource Name (ARN) for a customer master key (CMK) in AWS Key Management
      Service (AWS KMS).

      You must provide a ``KmsKeyArn`` if you specify ``SSE_KMS`` as the
      ``ObjectEncryptionType`` .

       ``KmsKeyArn`` is not required if you specify ``SSE_S3`` as the
       ``ObjectEncryptionType`` .
    """


_ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationTypeDef = TypedDict(
    "_ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationTypeDef",
    {
        "Bucket": str,
        "Prefix": str,
        "EncryptionConfiguration": ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationEncryptionConfigurationTypeDef,
    },
    total=False,
)


class ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationTypeDef(
    _ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationTypeDef
):
    """
    Type definition for `ClientListJournalS3ExportsResponseJournalS3Exports` `S3ExportConfiguration`

    The Amazon Simple Storage Service (Amazon S3) bucket location in which a journal export
    job writes the journal contents.

    - **Bucket** *(string) --*

      The Amazon S3 bucket name in which a journal export job writes the journal contents.

      The bucket name must comply with the Amazon S3 bucket naming conventions. For more
      information, see `Bucket Restrictions and Limitations
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html>`__ in the
      *Amazon S3 Developer Guide* .

    - **Prefix** *(string) --*

      The prefix for the Amazon S3 bucket in which a journal export job writes the journal
      contents.

      The prefix must comply with Amazon S3 key naming rules and restrictions. For more
      information, see `Object Key and Metadata
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html>`__ in the *Amazon
      S3 Developer Guide* .

      The following are examples of valid ``Prefix`` values:

      * ``JournalExports-ForMyLedger/Testing/``

      * ``JournalExports``

      * ``My:Tests/``

    - **EncryptionConfiguration** *(dict) --*

      The encryption settings that are used by a journal export job to write data in an
      Amazon S3 bucket.

      - **ObjectEncryptionType** *(string) --*

        The Amazon S3 object encryption type.

        To learn more about server-side encryption options in Amazon S3, see `Protecting Data
        Using Server-Side Encryption
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`__ in the
        *Amazon S3 Developer Guide* .

      - **KmsKeyArn** *(string) --*

        The Amazon Resource Name (ARN) for a customer master key (CMK) in AWS Key Management
        Service (AWS KMS).

        You must provide a ``KmsKeyArn`` if you specify ``SSE_KMS`` as the
        ``ObjectEncryptionType`` .

         ``KmsKeyArn`` is not required if you specify ``SSE_S3`` as the
         ``ObjectEncryptionType`` .
    """


_ClientListJournalS3ExportsResponseJournalS3ExportsTypeDef = TypedDict(
    "_ClientListJournalS3ExportsResponseJournalS3ExportsTypeDef",
    {
        "LedgerName": str,
        "ExportId": str,
        "ExportCreationTime": datetime,
        "Status": str,
        "InclusiveStartTime": datetime,
        "ExclusiveEndTime": datetime,
        "S3ExportConfiguration": ClientListJournalS3ExportsResponseJournalS3ExportsS3ExportConfigurationTypeDef,
        "RoleArn": str,
    },
    total=False,
)


class ClientListJournalS3ExportsResponseJournalS3ExportsTypeDef(
    _ClientListJournalS3ExportsResponseJournalS3ExportsTypeDef
):
    """
    Type definition for `ClientListJournalS3ExportsResponse` `JournalS3Exports`

    The information about a journal export job, including the ledger name, export ID, when it
    was created, current status, and its start and end time export parameters.

    - **LedgerName** *(string) --*

      The name of the ledger.

    - **ExportId** *(string) --*

      The unique ID of the journal export job.

    - **ExportCreationTime** *(datetime) --*

      The date and time, in epoch time format, when the export job was created. (Epoch time
      format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

    - **Status** *(string) --*

      The current state of the journal export job.

    - **InclusiveStartTime** *(datetime) --*

      The inclusive start date and time for the range of journal contents that are specified in
      the original export request.

    - **ExclusiveEndTime** *(datetime) --*

      The exclusive end date and time for the range of journal contents that are specified in
      the original export request.

    - **S3ExportConfiguration** *(dict) --*

      The Amazon Simple Storage Service (Amazon S3) bucket location in which a journal export
      job writes the journal contents.

      - **Bucket** *(string) --*

        The Amazon S3 bucket name in which a journal export job writes the journal contents.

        The bucket name must comply with the Amazon S3 bucket naming conventions. For more
        information, see `Bucket Restrictions and Limitations
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html>`__ in the
        *Amazon S3 Developer Guide* .

      - **Prefix** *(string) --*

        The prefix for the Amazon S3 bucket in which a journal export job writes the journal
        contents.

        The prefix must comply with Amazon S3 key naming rules and restrictions. For more
        information, see `Object Key and Metadata
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html>`__ in the *Amazon
        S3 Developer Guide* .

        The following are examples of valid ``Prefix`` values:

        * ``JournalExports-ForMyLedger/Testing/``

        * ``JournalExports``

        * ``My:Tests/``

      - **EncryptionConfiguration** *(dict) --*

        The encryption settings that are used by a journal export job to write data in an
        Amazon S3 bucket.

        - **ObjectEncryptionType** *(string) --*

          The Amazon S3 object encryption type.

          To learn more about server-side encryption options in Amazon S3, see `Protecting Data
          Using Server-Side Encryption
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`__ in the
          *Amazon S3 Developer Guide* .

        - **KmsKeyArn** *(string) --*

          The Amazon Resource Name (ARN) for a customer master key (CMK) in AWS Key Management
          Service (AWS KMS).

          You must provide a ``KmsKeyArn`` if you specify ``SSE_KMS`` as the
          ``ObjectEncryptionType`` .

           ``KmsKeyArn`` is not required if you specify ``SSE_S3`` as the
           ``ObjectEncryptionType`` .

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal
      export job to do the following:

      * Write objects into your Amazon Simple Storage Service (Amazon S3) bucket.

      * (Optional) Use your customer master key (CMK) in AWS Key Management Service (AWS KMS)
      for server-side encryption of your exported data.
    """


_ClientListJournalS3ExportsResponseTypeDef = TypedDict(
    "_ClientListJournalS3ExportsResponseTypeDef",
    {
        "JournalS3Exports": List[
            ClientListJournalS3ExportsResponseJournalS3ExportsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListJournalS3ExportsResponseTypeDef(
    _ClientListJournalS3ExportsResponseTypeDef
):
    """
    Type definition for `ClientListJournalS3Exports` `Response`

    - **JournalS3Exports** *(list) --*

      The array of journal export job descriptions for all ledgers that are associated with the
      current AWS account and Region.

      - *(dict) --*

        The information about a journal export job, including the ledger name, export ID, when it
        was created, current status, and its start and end time export parameters.

        - **LedgerName** *(string) --*

          The name of the ledger.

        - **ExportId** *(string) --*

          The unique ID of the journal export job.

        - **ExportCreationTime** *(datetime) --*

          The date and time, in epoch time format, when the export job was created. (Epoch time
          format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

        - **Status** *(string) --*

          The current state of the journal export job.

        - **InclusiveStartTime** *(datetime) --*

          The inclusive start date and time for the range of journal contents that are specified in
          the original export request.

        - **ExclusiveEndTime** *(datetime) --*

          The exclusive end date and time for the range of journal contents that are specified in
          the original export request.

        - **S3ExportConfiguration** *(dict) --*

          The Amazon Simple Storage Service (Amazon S3) bucket location in which a journal export
          job writes the journal contents.

          - **Bucket** *(string) --*

            The Amazon S3 bucket name in which a journal export job writes the journal contents.

            The bucket name must comply with the Amazon S3 bucket naming conventions. For more
            information, see `Bucket Restrictions and Limitations
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html>`__ in the
            *Amazon S3 Developer Guide* .

          - **Prefix** *(string) --*

            The prefix for the Amazon S3 bucket in which a journal export job writes the journal
            contents.

            The prefix must comply with Amazon S3 key naming rules and restrictions. For more
            information, see `Object Key and Metadata
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html>`__ in the *Amazon
            S3 Developer Guide* .

            The following are examples of valid ``Prefix`` values:

            * ``JournalExports-ForMyLedger/Testing/``

            * ``JournalExports``

            * ``My:Tests/``

          - **EncryptionConfiguration** *(dict) --*

            The encryption settings that are used by a journal export job to write data in an
            Amazon S3 bucket.

            - **ObjectEncryptionType** *(string) --*

              The Amazon S3 object encryption type.

              To learn more about server-side encryption options in Amazon S3, see `Protecting Data
              Using Server-Side Encryption
              <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`__ in the
              *Amazon S3 Developer Guide* .

            - **KmsKeyArn** *(string) --*

              The Amazon Resource Name (ARN) for a customer master key (CMK) in AWS Key Management
              Service (AWS KMS).

              You must provide a ``KmsKeyArn`` if you specify ``SSE_KMS`` as the
              ``ObjectEncryptionType`` .

               ``KmsKeyArn`` is not required if you specify ``SSE_S3`` as the
               ``ObjectEncryptionType`` .

        - **RoleArn** *(string) --*

          The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal
          export job to do the following:

          * Write objects into your Amazon Simple Storage Service (Amazon S3) bucket.

          * (Optional) Use your customer master key (CMK) in AWS Key Management Service (AWS KMS)
          for server-side encryption of your exported data.

    - **NextToken** *(string) --*

      * If ``NextToken`` is empty, then the last page of results has been processed and there are
      no more results to be retrieved.

      * If ``NextToken`` is *not* empty, then there are more results available. To retrieve the
      next page of results, use the value of ``NextToken`` in a subsequent ``ListJournalS3Exports``
      call.
    """


_ClientListLedgersResponseLedgersTypeDef = TypedDict(
    "_ClientListLedgersResponseLedgersTypeDef",
    {"Name": str, "State": str, "CreationDateTime": datetime},
    total=False,
)


class ClientListLedgersResponseLedgersTypeDef(_ClientListLedgersResponseLedgersTypeDef):
    """
    Type definition for `ClientListLedgersResponse` `Ledgers`

    Information about a ledger, including its name, state, and when it was created.

    - **Name** *(string) --*

      The name of the ledger.

    - **State** *(string) --*

      The current status of the ledger.

    - **CreationDateTime** *(datetime) --*

      The date and time, in epoch time format, when the ledger was created. (Epoch time format
      is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)
    """


_ClientListLedgersResponseTypeDef = TypedDict(
    "_ClientListLedgersResponseTypeDef",
    {"Ledgers": List[ClientListLedgersResponseLedgersTypeDef], "NextToken": str},
    total=False,
)


class ClientListLedgersResponseTypeDef(_ClientListLedgersResponseTypeDef):
    """
    Type definition for `ClientListLedgers` `Response`

    - **Ledgers** *(list) --*

      The array of ledger summaries that are associated with the current AWS account and Region.

      - *(dict) --*

        Information about a ledger, including its name, state, and when it was created.

        - **Name** *(string) --*

          The name of the ledger.

        - **State** *(string) --*

          The current status of the ledger.

        - **CreationDateTime** *(datetime) --*

          The date and time, in epoch time format, when the ledger was created. (Epoch time format
          is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

    - **NextToken** *(string) --*

      A pagination token, indicating whether there are more results available:

      * If ``NextToken`` is empty, then the last page of results has been processed and there are
      no more results to be retrieved.

      * If ``NextToken`` is *not* empty, then there are more results available. To retrieve the
      next page of results, use the value of ``NextToken`` in a subsequent ``ListLedgers`` call.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **Tags** *(dict) --*

      The tags that are currently associated with the specified Amazon QLDB resource.

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateLedgerResponseTypeDef = TypedDict(
    "_ClientUpdateLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": str,
        "CreationDateTime": datetime,
        "DeletionProtection": bool,
    },
    total=False,
)


class ClientUpdateLedgerResponseTypeDef(_ClientUpdateLedgerResponseTypeDef):
    """
    Type definition for `ClientUpdateLedger` `Response`

    - **Name** *(string) --*

      The name of the ledger.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) for the ledger.

    - **State** *(string) --*

      The current status of the ledger.

    - **CreationDateTime** *(datetime) --*

      The date and time, in epoch time format, when the ledger was created. (Epoch time format is
      the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)

    - **DeletionProtection** *(boolean) --*

      The flag that prevents a ledger from being deleted by any user. If not provided on ledger
      creation, this feature is enabled (``true`` ) by default.

      If deletion protection is enabled, you must first disable it before you can delete the ledger
      using the QLDB API or the AWS Command Line Interface (AWS CLI). You can disable it by calling
      the ``UpdateLedger`` operation to set the flag to ``false`` . The QLDB console disables
      deletion protection for you when you use it to delete a ledger.
    """

"Main interface for qldb Client"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_qldb.client as client_scope
from mypy_boto3_qldb.type_defs import (
    ClientCreateLedgerResponseTypeDef,
    ClientDescribeJournalS3ExportResponseTypeDef,
    ClientDescribeLedgerResponseTypeDef,
    ClientExportJournalToS3ResponseTypeDef,
    ClientExportJournalToS3S3ExportConfigurationTypeDef,
    ClientGetBlockBlockAddressTypeDef,
    ClientGetBlockDigestTipAddressTypeDef,
    ClientGetBlockResponseTypeDef,
    ClientGetDigestResponseTypeDef,
    ClientGetRevisionBlockAddressTypeDef,
    ClientGetRevisionDigestTipAddressTypeDef,
    ClientGetRevisionResponseTypeDef,
    ClientListJournalS3ExportsForLedgerResponseTypeDef,
    ClientListJournalS3ExportsResponseTypeDef,
    ClientListLedgersResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientUpdateLedgerResponseTypeDef,
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
    def create_ledger(
        self,
        Name: str,
        PermissionsMode: str,
        Tags: List[str] = None,
        DeletionProtection: bool = None,
    ) -> ClientCreateLedgerResponseTypeDef:
        """
        Creates a new ledger in your AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/CreateLedger>`_

        **Request Syntax**
        ::

          response = client.create_ledger(
              Name='string',
              Tags={
                  'string': 'string'
              },
              PermissionsMode='ALLOW_ALL',
              DeletionProtection=True|False
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the ledger that you want to create. The name must be unique among all of your ledgers
          in the current AWS Region.

        :type Tags: dict
        :param Tags:

          The key-value pairs to add as tags to the ledger that you want to create. Tag keys are case
          sensitive. Tag values are case sensitive and can be null.

          - *(string) --*

            - *(string) --*

        :type PermissionsMode: string
        :param PermissionsMode: **[REQUIRED]**

          The permissions mode to assign to the ledger that you want to create.

        :type DeletionProtection: boolean
        :param DeletionProtection:

          The flag that prevents a ledger from being deleted by any user. If not provided on ledger
          creation, this feature is enabled (``true`` ) by default.

          If deletion protection is enabled, you must first disable it before you can delete the ledger
          using the QLDB API or the AWS Command Line Interface (AWS CLI). You can disable it by calling the
          ``UpdateLedger`` operation to set the flag to ``false`` . The QLDB console disables deletion
          protection for you when you use it to delete a ledger.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string',
                'Arn': 'string',
                'State': 'CREATING'|'ACTIVE'|'DELETING'|'DELETED',
                'CreationDateTime': datetime(2015, 1, 1),
                'DeletionProtection': True|False
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_ledger(self, Name: str) -> None:
        """
        Deletes a ledger and all of its contents. This action is irreversible.

        If deletion protection is enabled, you must first disable it before you can delete the ledger using
        the QLDB API or the AWS Command Line Interface (AWS CLI). You can disable it by calling the
        ``UpdateLedger`` operation to set the flag to ``false`` . The QLDB console disables deletion
        protection for you when you use it to delete a ledger.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/DeleteLedger>`_

        **Request Syntax**
        ::

          response = client.delete_ledger(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the ledger that you want to delete.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_journal_s3_export(
        self, Name: str, ExportId: str
    ) -> ClientDescribeJournalS3ExportResponseTypeDef:
        """
        Returns information about a journal export job, including the ledger name, export ID, when it was
        created, current status, and its start and end time export parameters.

        If the export job with the given ``ExportId`` doesn't exist, then throws
        ``ResourceNotFoundException`` .

        If the ledger with the given ``Name`` doesn't exist, then throws ``ResourceNotFoundException`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/DescribeJournalS3Export>`_

        **Request Syntax**
        ::

          response = client.describe_journal_s3_export(
              Name='string',
              ExportId='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the ledger.

        :type ExportId: string
        :param ExportId: **[REQUIRED]**

          The unique ID of the journal export job that you want to describe.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ExportDescription': {
                    'LedgerName': 'string',
                    'ExportId': 'string',
                    'ExportCreationTime': datetime(2015, 1, 1),
                    'Status': 'IN_PROGRESS'|'COMPLETED'|'CANCELLED',
                    'InclusiveStartTime': datetime(2015, 1, 1),
                    'ExclusiveEndTime': datetime(2015, 1, 1),
                    'S3ExportConfiguration': {
                        'Bucket': 'string',
                        'Prefix': 'string',
                        'EncryptionConfiguration': {
                            'ObjectEncryptionType': 'SSE_KMS'|'SSE_S3'|'NO_ENCRYPTION',
                            'KmsKeyArn': 'string'
                        }
                    },
                    'RoleArn': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_ledger(self, Name: str) -> ClientDescribeLedgerResponseTypeDef:
        """
        Returns information about a ledger, including its state and when it was created.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/DescribeLedger>`_

        **Request Syntax**
        ::

          response = client.describe_ledger(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the ledger that you want to describe.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string',
                'Arn': 'string',
                'State': 'CREATING'|'ACTIVE'|'DELETING'|'DELETED',
                'CreationDateTime': datetime(2015, 1, 1),
                'DeletionProtection': True|False
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def export_journal_to_s3(
        self,
        Name: str,
        InclusiveStartTime: datetime,
        ExclusiveEndTime: datetime,
        S3ExportConfiguration: ClientExportJournalToS3S3ExportConfigurationTypeDef,
        RoleArn: str,
    ) -> ClientExportJournalToS3ResponseTypeDef:
        """
        Exports journal contents within a date and time range from a ledger into a specified Amazon Simple
        Storage Service (Amazon S3) bucket. The data is written as files in Amazon Ion format.

        If the ledger with the given ``Name`` doesn't exist, then throws ``ResourceNotFoundException`` .

        If the ledger with the given ``Name`` is in ``CREATING`` status, then throws
        ``ResourcePreconditionNotMetException`` .

        You can initiate up to two concurrent journal export requests for each ledger. Beyond this limit,
        journal export requests throw ``LimitExceededException`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/ExportJournalToS3>`_

        **Request Syntax**
        ::

          response = client.export_journal_to_s3(
              Name='string',
              InclusiveStartTime=datetime(2015, 1, 1),
              ExclusiveEndTime=datetime(2015, 1, 1),
              S3ExportConfiguration={
                  'Bucket': 'string',
                  'Prefix': 'string',
                  'EncryptionConfiguration': {
                      'ObjectEncryptionType': 'SSE_KMS'|'SSE_S3'|'NO_ENCRYPTION',
                      'KmsKeyArn': 'string'
                  }
              },
              RoleArn='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the ledger.

        :type InclusiveStartTime: datetime
        :param InclusiveStartTime: **[REQUIRED]**

          The inclusive start date and time for the range of journal contents that you want to export.

          The ``InclusiveStartTime`` must be in ``ISO 8601`` date and time format and in Universal
          Coordinated Time (UTC). For example: ``2019-06-13T21:36:34Z``

          The ``InclusiveStartTime`` must be before ``ExclusiveEndTime`` .

          If you provide an ``InclusiveStartTime`` that is before the ledger's ``CreationDateTime`` ,
          Amazon QLDB defaults it to the ledger's ``CreationDateTime`` .

        :type ExclusiveEndTime: datetime
        :param ExclusiveEndTime: **[REQUIRED]**

          The exclusive end date and time for the range of journal contents that you want to export.

          The ``ExclusiveEndTime`` must be in ``ISO 8601`` date and time format and in Universal
          Coordinated Time (UTC). For example: ``2019-06-13T21:36:34Z``

          The ``ExclusiveEndTime`` must be less than or equal to the current UTC date and time.

        :type S3ExportConfiguration: dict
        :param S3ExportConfiguration: **[REQUIRED]**

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

        :type RoleArn: string
        :param RoleArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal export
          job to do the following:

          * Write objects into your Amazon Simple Storage Service (Amazon S3) bucket.

          * (Optional) Use your customer master key (CMK) in AWS Key Management Service (AWS KMS) for
          server-side encryption of your exported data.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ExportId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ExportId** *(string) --*

              The unique ID that QLDB assigns to each journal export job.

              To describe your export request and check the status of the job, you can use ``ExportId`` to
              call ``DescribeJournalS3Export`` .

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
    def get_block(
        self,
        Name: str,
        BlockAddress: ClientGetBlockBlockAddressTypeDef,
        DigestTipAddress: ClientGetBlockDigestTipAddressTypeDef = None,
    ) -> ClientGetBlockResponseTypeDef:
        """
        Returns a journal block object at a specified address in a ledger. Also returns a proof of the
        specified block for verification if ``DigestTipAddress`` is provided.

        If the specified ledger doesn't exist or is in ``DELETING`` status, then throws
        ``ResourceNotFoundException`` .

        If the specified ledger is in ``CREATING`` status, then throws
        ``ResourcePreconditionNotMetException`` .

        If no block exists with the specified address, then throws ``InvalidParameterException`` .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/GetBlock>`_

        **Request Syntax**
        ::

          response = client.get_block(
              Name='string',
              BlockAddress={
                  'IonText': 'string'
              },
              DigestTipAddress={
                  'IonText': 'string'
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the ledger.

        :type BlockAddress: dict
        :param BlockAddress: **[REQUIRED]**

          The location of the block that you want to request. An address is an Amazon Ion structure that
          has two fields: ``strandId`` and ``sequenceNo`` .

          For example: ``{strandId:"BlFTjlSXze9BIh1KOszcE3",sequenceNo:14}``

          - **IonText** *(string) --*

            An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.

        :type DigestTipAddress: dict
        :param DigestTipAddress:

          The latest block location covered by the digest for which to request a proof. An address is an
          Amazon Ion structure that has two fields: ``strandId`` and ``sequenceNo`` .

          For example: ``{strandId:"BlFTjlSXze9BIh1KOszcE3",sequenceNo:49}``

          - **IonText** *(string) --*

            An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Block': {
                    'IonText': 'string'
                },
                'Proof': {
                    'IonText': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_digest(self, Name: str) -> ClientGetDigestResponseTypeDef:
        """
        Returns the digest of a ledger at the latest committed block in the journal. The response includes
        a 256-bit hash value and a block address.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/GetDigest>`_

        **Request Syntax**
        ::

          response = client.get_digest(
              Name='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the ledger.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Digest': b'bytes',
                'DigestTipAddress': {
                    'IonText': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Digest** *(bytes) --*

              The 256-bit hash value representing the digest returned by a ``GetDigest`` request.

            - **DigestTipAddress** *(dict) --*

              The latest block location covered by the digest that you requested. An address is an Amazon
              Ion structure that has two fields: ``strandId`` and ``sequenceNo`` .

              - **IonText** *(string) --*

                An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_revision(
        self,
        Name: str,
        BlockAddress: ClientGetRevisionBlockAddressTypeDef,
        DocumentId: str,
        DigestTipAddress: ClientGetRevisionDigestTipAddressTypeDef = None,
    ) -> ClientGetRevisionResponseTypeDef:
        """
        Returns a revision data object for a specified document ID and block address. Also returns a proof
        of the specified revision for verification if ``DigestTipAddress`` is provided.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/GetRevision>`_

        **Request Syntax**
        ::

          response = client.get_revision(
              Name='string',
              BlockAddress={
                  'IonText': 'string'
              },
              DocumentId='string',
              DigestTipAddress={
                  'IonText': 'string'
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the ledger.

        :type BlockAddress: dict
        :param BlockAddress: **[REQUIRED]**

          The block location of the document revision to be verified. An address is an Amazon Ion structure
          that has two fields: ``strandId`` and ``sequenceNo`` .

          For example: ``{strandId:"BlFTjlSXze9BIh1KOszcE3",sequenceNo:14}``

          - **IonText** *(string) --*

            An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.

        :type DocumentId: string
        :param DocumentId: **[REQUIRED]**

          The unique ID of the document to be verified.

        :type DigestTipAddress: dict
        :param DigestTipAddress:

          The latest block location covered by the digest for which to request a proof. An address is an
          Amazon Ion structure that has two fields: ``strandId`` and ``sequenceNo`` .

          For example: ``{strandId:"BlFTjlSXze9BIh1KOszcE3",sequenceNo:49}``

          - **IonText** *(string) --*

            An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Proof': {
                    'IonText': 'string'
                },
                'Revision': {
                    'IonText': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_journal_s3_exports(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListJournalS3ExportsResponseTypeDef:
        """
        Returns an array of journal export job descriptions for all ledgers that are associated with the
        current AWS account and Region.

        This action returns a maximum of ``MaxResults`` items, and is paginated so that you can retrieve
        all the items by calling ``ListJournalS3Exports`` multiple times.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/ListJournalS3Exports>`_

        **Request Syntax**
        ::

          response = client.list_journal_s3_exports(
              MaxResults=123,
              NextToken='string'
          )
        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single ``ListJournalS3Exports`` request. (The actual
          number of results returned might be fewer.)

        :type NextToken: string
        :param NextToken:

          A pagination token, indicating that you want to retrieve the next page of results. If you
          received a value for ``NextToken`` in the response from a previous ``ListJournalS3Exports`` call,
          then you should use that value as input here.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JournalS3Exports': [
                    {
                        'LedgerName': 'string',
                        'ExportId': 'string',
                        'ExportCreationTime': datetime(2015, 1, 1),
                        'Status': 'IN_PROGRESS'|'COMPLETED'|'CANCELLED',
                        'InclusiveStartTime': datetime(2015, 1, 1),
                        'ExclusiveEndTime': datetime(2015, 1, 1),
                        'S3ExportConfiguration': {
                            'Bucket': 'string',
                            'Prefix': 'string',
                            'EncryptionConfiguration': {
                                'ObjectEncryptionType': 'SSE_KMS'|'SSE_S3'|'NO_ENCRYPTION',
                                'KmsKeyArn': 'string'
                            }
                        },
                        'RoleArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_journal_s3_exports_for_ledger(
        self, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> ClientListJournalS3ExportsForLedgerResponseTypeDef:
        """
        Returns an array of journal export job descriptions for a specified ledger.

        This action returns a maximum of ``MaxResults`` items, and is paginated so that you can retrieve
        all the items by calling ``ListJournalS3ExportsForLedger`` multiple times.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/ListJournalS3ExportsForLedger>`_

        **Request Syntax**
        ::

          response = client.list_journal_s3_exports_for_ledger(
              Name='string',
              MaxResults=123,
              NextToken='string'
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the ledger.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single ``ListJournalS3ExportsForLedger`` request.
          (The actual number of results returned might be fewer.)

        :type NextToken: string
        :param NextToken:

          A pagination token, indicating that you want to retrieve the next page of results. If you
          received a value for ``NextToken`` in the response from a previous
          ``ListJournalS3ExportsForLedger`` call, then you should use that value as input here.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JournalS3Exports': [
                    {
                        'LedgerName': 'string',
                        'ExportId': 'string',
                        'ExportCreationTime': datetime(2015, 1, 1),
                        'Status': 'IN_PROGRESS'|'COMPLETED'|'CANCELLED',
                        'InclusiveStartTime': datetime(2015, 1, 1),
                        'ExclusiveEndTime': datetime(2015, 1, 1),
                        'S3ExportConfiguration': {
                            'Bucket': 'string',
                            'Prefix': 'string',
                            'EncryptionConfiguration': {
                                'ObjectEncryptionType': 'SSE_KMS'|'SSE_S3'|'NO_ENCRYPTION',
                                'KmsKeyArn': 'string'
                            }
                        },
                        'RoleArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_ledgers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ClientListLedgersResponseTypeDef:
        """
        Returns an array of ledger summaries that are associated with the current AWS account and Region.

        This action returns a maximum of 100 items and is paginated so that you can retrieve all the items
        by calling ``ListLedgers`` multiple times.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/ListLedgers>`_

        **Request Syntax**
        ::

          response = client.list_ledgers(
              MaxResults=123,
              NextToken='string'
          )
        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single ``ListLedgers`` request. (The actual number
          of results returned might be fewer.)

        :type NextToken: string
        :param NextToken:

          A pagination token, indicating that you want to retrieve the next page of results. If you
          received a value for ``NextToken`` in the response from a previous ``ListLedgers`` call, then you
          should use that value as input here.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Ledgers': [
                    {
                        'Name': 'string',
                        'State': 'CREATING'|'ACTIVE'|'DELETING'|'DELETED',
                        'CreationDateTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

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

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(
        self, ResourceArn: str
    ) -> ClientListTagsForResourceResponseTypeDef:
        """
        Returns all tags for a specified Amazon QLDB resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              ResourceArn='string'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) for which you want to list the tags. For example:

           ``arn:aws:qldb:us-east-1:123456789012:ledger/exampleLedger``

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Tags** *(dict) --*

              The tags that are currently associated with the specified Amazon QLDB resource.

              - *(string) --*

                - *(string) --*

        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, ResourceArn: str, Tags: List[str]) -> Dict[str, Any]:
        """
        Adds one or more tags to a specified Amazon QLDB resource.

        A resource can have up to 50 tags. If you try to create more than 50 tags for a resource, your
        request fails and returns an error.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              ResourceArn='string',
              Tags={
                  'string': 'string'
              }
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) to which you want to add the tags. For example:

           ``arn:aws:qldb:us-east-1:123456789012:ledger/exampleLedger``

        :type Tags: dict
        :param Tags: **[REQUIRED]**

          The key-value pairs to add as tags to the specified QLDB resource. Tag keys are case sensitive.
          If you specify a key that already exists for the resource, your request fails and returns an
          error. Tag values are case sensitive and can be null.

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
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from a specified Amazon QLDB resource. You can specify up to 50 tag keys
        to remove.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              ResourceArn='string',
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) from which you want to remove the tags. For example:

           ``arn:aws:qldb:us-east-1:123456789012:ledger/exampleLedger``

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          The list of tag keys that you want to remove.

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
    def update_ledger(
        self, Name: str, DeletionProtection: bool = None
    ) -> ClientUpdateLedgerResponseTypeDef:
        """
        Updates properties on a ledger.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/qldb-2019-01-02/UpdateLedger>`_

        **Request Syntax**
        ::

          response = client.update_ledger(
              Name='string',
              DeletionProtection=True|False
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the ledger.

        :type DeletionProtection: boolean
        :param DeletionProtection:

          The flag that prevents a ledger from being deleted by any user. If not provided on ledger
          creation, this feature is enabled (``true`` ) by default.

          If deletion protection is enabled, you must first disable it before you can delete the ledger
          using the QLDB API or the AWS Command Line Interface (AWS CLI). You can disable it by calling the
          ``UpdateLedger`` operation to set the flag to ``false`` . The QLDB console disables deletion
          protection for you when you use it to delete a ledger.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string',
                'Arn': 'string',
                'State': 'CREATING'|'ACTIVE'|'DELETING'|'DELETED',
                'CreationDateTime': datetime(2015, 1, 1),
                'DeletionProtection': True|False
            }
          **Response Structure**

          - *(dict) --*

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


class Exceptions:
    ClientError: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourcePreconditionNotMetException: Boto3ClientError

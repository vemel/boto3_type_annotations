"Main interface for qldb-session Client"
from __future__ import annotations

from typing import Dict
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_qldb_session.client as client_scope
from mypy_boto3_qldb_session.type_defs import (
    ClientSendCommandCommitTransactionTypeDef,
    ClientSendCommandExecuteStatementTypeDef,
    ClientSendCommandFetchPageTypeDef,
    ClientSendCommandResponseTypeDef,
    ClientSendCommandStartSessionTypeDef,
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
    def send_command(
        self,
        SessionToken: str = None,
        StartSession: ClientSendCommandStartSessionTypeDef = None,
        StartTransaction: Dict = None,
        EndSession: Dict = None,
        CommitTransaction: ClientSendCommandCommitTransactionTypeDef = None,
        AbortTransaction: Dict = None,
        ExecuteStatement: ClientSendCommandExecuteStatementTypeDef = None,
        FetchPage: ClientSendCommandFetchPageTypeDef = None,
    ) -> ClientSendCommandResponseTypeDef:
        """
        Sends a command to an Amazon QLDB ledger.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/qldb-session-2019-07-11/SendCommand>`_

        **Request Syntax**
        ::

          response = client.send_command(
              SessionToken='string',
              StartSession={
                  'LedgerName': 'string'
              },
              StartTransaction={}
              ,
              EndSession={}
              ,
              CommitTransaction={
                  'TransactionId': 'string',
                  'CommitDigest': b'bytes'
              },
              AbortTransaction={}
              ,
              ExecuteStatement={
                  'TransactionId': 'string',
                  'Statement': 'string',
                  'Parameters': [
                      {
                          'IonBinary': b'bytes',
                          'IonText': 'string'
                      },
                  ]
              },
              FetchPage={
                  'TransactionId': 'string',
                  'NextPageToken': 'string'
              }
          )
        :type SessionToken: string
        :param SessionToken:

          Specifies the session token for the current command. A session token is constant throughout the
          life of the session.

          To obtain a session token, run the ``StartSession`` command. This ``SessionToken`` is required
          for every subsequent command that is issued during the current session.

        :type StartSession: dict
        :param StartSession:

          Command to start a new session. A session token is obtained as part of the response.

          - **LedgerName** *(string) --* **[REQUIRED]**

            The name of the ledger to start a new session against.

        :type StartTransaction: dict
        :param StartTransaction:

          Command to start a new transaction.

        :type EndSession: dict
        :param EndSession:

          Command to end the current session.

        :type CommitTransaction: dict
        :param CommitTransaction:

          Command to commit the specified transaction.

          - **TransactionId** *(string) --* **[REQUIRED]**

            Specifies the transaction id of the transaction to commit.

          - **CommitDigest** *(bytes) --* **[REQUIRED]**

            Specifies the commit digest for the transaction to commit. For every active transaction, the
            commit digest must be passed. QLDB validates ``CommitDigest`` and rejects the commit with an
            error if the digest computed on the client does not match the digest computed by QLDB.

        :type AbortTransaction: dict
        :param AbortTransaction:

          Command to abort the current transaction.

        :type ExecuteStatement: dict
        :param ExecuteStatement:

          Command to execute a statement in the specified transaction.

          - **TransactionId** *(string) --* **[REQUIRED]**

            Specifies the transaction id of the request.

          - **Statement** *(string) --* **[REQUIRED]**

            Specifies the statement of the request.

          - **Parameters** *(list) --*

            Specifies the parameters for the parameterized statement in the request.

            - *(dict) --*

              A structure that can contains values in multiple encoding formats.

              - **IonBinary** *(bytes) --*

                An Amazon Ion binary value contained in a ``ValueHolder`` structure.

              - **IonText** *(string) --*

                An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.

        :type FetchPage: dict
        :param FetchPage:

          Command to fetch a page.

          - **TransactionId** *(string) --* **[REQUIRED]**

            Specifies the transaction id of the page to be fetched.

          - **NextPageToken** *(string) --* **[REQUIRED]**

            Specifies the next page token of the page to be fetched.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'StartSession': {
                    'SessionToken': 'string'
                },
                'StartTransaction': {
                    'TransactionId': 'string'
                },
                'EndSession': {},
                'CommitTransaction': {
                    'TransactionId': 'string',
                    'CommitDigest': b'bytes'
                },
                'AbortTransaction': {},
                'ExecuteStatement': {
                    'FirstPage': {
                        'Values': [
                            {
                                'IonBinary': b'bytes',
                                'IonText': 'string'
                            },
                        ],
                        'NextPageToken': 'string'
                    }
                },
                'FetchPage': {
                    'Page': {
                        'Values': [
                            {
                                'IonBinary': b'bytes',
                                'IonText': 'string'
                            },
                        ],
                        'NextPageToken': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **StartSession** *(dict) --*

              Contains the details of the started session that includes a session token. This
              ``SessionToken`` is required for every subsequent command that is issued during the current
              session.

              - **SessionToken** *(string) --*

                Session token of the started session. This ``SessionToken`` is required for every
                subsequent command that is issued during the current session.

            - **StartTransaction** *(dict) --*

              Contains the details of the started transaction.

              - **TransactionId** *(string) --*

                The transaction id of the started transaction.

            - **EndSession** *(dict) --*

              Contains the details of the ended session.

            - **CommitTransaction** *(dict) --*

              Contains the details of the committed transaction.

              - **TransactionId** *(string) --*

                The transaction id of the committed transaction.

              - **CommitDigest** *(bytes) --*

                The commit digest of the committed transaction.

            - **AbortTransaction** *(dict) --*

              Contains the details of the aborted transaction.

            - **ExecuteStatement** *(dict) --*

              Contains the details of the executed statement.

              - **FirstPage** *(dict) --*

                Contains the details of the first fetched page.

                - **Values** *(list) --*

                  A structure that contains values in multiple encoding formats.

                  - *(dict) --*

                    A structure that can contains values in multiple encoding formats.

                    - **IonBinary** *(bytes) --*

                      An Amazon Ion binary value contained in a ``ValueHolder`` structure.

                    - **IonText** *(string) --*

                      An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.

                - **NextPageToken** *(string) --*

                  The token of the next page.

            - **FetchPage** *(dict) --*

              Contains the details of the fetched page.

              - **Page** *(dict) --*

                Contains details of the fetched page.

                - **Values** *(list) --*

                  A structure that contains values in multiple encoding formats.

                  - *(dict) --*

                    A structure that can contains values in multiple encoding formats.

                    - **IonBinary** *(bytes) --*

                      An Amazon Ion binary value contained in a ``ValueHolder`` structure.

                    - **IonText** *(string) --*

                      An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.

                - **NextPageToken** *(string) --*

                  The token of the next page.

        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    InvalidSessionException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    OccConflictException: Boto3ClientError
    RateExceededException: Boto3ClientError

"Main interface for qldb-session type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientSendCommandCommitTransactionTypeDef",
    "ClientSendCommandExecuteStatementParametersTypeDef",
    "ClientSendCommandExecuteStatementTypeDef",
    "ClientSendCommandFetchPageTypeDef",
    "ClientSendCommandResponseCommitTransactionTypeDef",
    "ClientSendCommandResponseExecuteStatementFirstPageValuesTypeDef",
    "ClientSendCommandResponseExecuteStatementFirstPageTypeDef",
    "ClientSendCommandResponseExecuteStatementTypeDef",
    "ClientSendCommandResponseFetchPagePageValuesTypeDef",
    "ClientSendCommandResponseFetchPagePageTypeDef",
    "ClientSendCommandResponseFetchPageTypeDef",
    "ClientSendCommandResponseStartSessionTypeDef",
    "ClientSendCommandResponseStartTransactionTypeDef",
    "ClientSendCommandResponseTypeDef",
    "ClientSendCommandStartSessionTypeDef",
)


_ClientSendCommandCommitTransactionTypeDef = TypedDict(
    "_ClientSendCommandCommitTransactionTypeDef",
    {"TransactionId": str, "CommitDigest": bytes},
)


class ClientSendCommandCommitTransactionTypeDef(
    _ClientSendCommandCommitTransactionTypeDef
):
    """
    Type definition for `ClientSendCommand` `CommitTransaction`

    Command to commit the specified transaction.

    - **TransactionId** *(string) --* **[REQUIRED]**

      Specifies the transaction id of the transaction to commit.

    - **CommitDigest** *(bytes) --* **[REQUIRED]**

      Specifies the commit digest for the transaction to commit. For every active transaction, the
      commit digest must be passed. QLDB validates ``CommitDigest`` and rejects the commit with an
      error if the digest computed on the client does not match the digest computed by QLDB.
    """


_ClientSendCommandExecuteStatementParametersTypeDef = TypedDict(
    "_ClientSendCommandExecuteStatementParametersTypeDef",
    {"IonBinary": bytes, "IonText": str},
    total=False,
)


class ClientSendCommandExecuteStatementParametersTypeDef(
    _ClientSendCommandExecuteStatementParametersTypeDef
):
    """
    Type definition for `ClientSendCommandExecuteStatement` `Parameters`

    A structure that can contains values in multiple encoding formats.

    - **IonBinary** *(bytes) --*

      An Amazon Ion binary value contained in a ``ValueHolder`` structure.

    - **IonText** *(string) --*

      An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_RequiredClientSendCommandExecuteStatementTypeDef = TypedDict(
    "_RequiredClientSendCommandExecuteStatementTypeDef",
    {"TransactionId": str, "Statement": str},
)
_OptionalClientSendCommandExecuteStatementTypeDef = TypedDict(
    "_OptionalClientSendCommandExecuteStatementTypeDef",
    {"Parameters": List[ClientSendCommandExecuteStatementParametersTypeDef]},
    total=False,
)


class ClientSendCommandExecuteStatementTypeDef(
    _RequiredClientSendCommandExecuteStatementTypeDef,
    _OptionalClientSendCommandExecuteStatementTypeDef,
):
    """
    Type definition for `ClientSendCommand` `ExecuteStatement`

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
    """


_ClientSendCommandFetchPageTypeDef = TypedDict(
    "_ClientSendCommandFetchPageTypeDef", {"TransactionId": str, "NextPageToken": str}
)


class ClientSendCommandFetchPageTypeDef(_ClientSendCommandFetchPageTypeDef):
    """
    Type definition for `ClientSendCommand` `FetchPage`

    Command to fetch a page.

    - **TransactionId** *(string) --* **[REQUIRED]**

      Specifies the transaction id of the page to be fetched.

    - **NextPageToken** *(string) --* **[REQUIRED]**

      Specifies the next page token of the page to be fetched.
    """


_ClientSendCommandResponseCommitTransactionTypeDef = TypedDict(
    "_ClientSendCommandResponseCommitTransactionTypeDef",
    {"TransactionId": str, "CommitDigest": bytes},
    total=False,
)


class ClientSendCommandResponseCommitTransactionTypeDef(
    _ClientSendCommandResponseCommitTransactionTypeDef
):
    """
    Type definition for `ClientSendCommandResponse` `CommitTransaction`

    Contains the details of the committed transaction.

    - **TransactionId** *(string) --*

      The transaction id of the committed transaction.

    - **CommitDigest** *(bytes) --*

      The commit digest of the committed transaction.
    """


_ClientSendCommandResponseExecuteStatementFirstPageValuesTypeDef = TypedDict(
    "_ClientSendCommandResponseExecuteStatementFirstPageValuesTypeDef",
    {"IonBinary": bytes, "IonText": str},
    total=False,
)


class ClientSendCommandResponseExecuteStatementFirstPageValuesTypeDef(
    _ClientSendCommandResponseExecuteStatementFirstPageValuesTypeDef
):
    """
    Type definition for `ClientSendCommandResponseExecuteStatementFirstPage` `Values`

    A structure that can contains values in multiple encoding formats.

    - **IonBinary** *(bytes) --*

      An Amazon Ion binary value contained in a ``ValueHolder`` structure.

    - **IonText** *(string) --*

      An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientSendCommandResponseExecuteStatementFirstPageTypeDef = TypedDict(
    "_ClientSendCommandResponseExecuteStatementFirstPageTypeDef",
    {
        "Values": List[ClientSendCommandResponseExecuteStatementFirstPageValuesTypeDef],
        "NextPageToken": str,
    },
    total=False,
)


class ClientSendCommandResponseExecuteStatementFirstPageTypeDef(
    _ClientSendCommandResponseExecuteStatementFirstPageTypeDef
):
    """
    Type definition for `ClientSendCommandResponseExecuteStatement` `FirstPage`

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
    """


_ClientSendCommandResponseExecuteStatementTypeDef = TypedDict(
    "_ClientSendCommandResponseExecuteStatementTypeDef",
    {"FirstPage": ClientSendCommandResponseExecuteStatementFirstPageTypeDef},
    total=False,
)


class ClientSendCommandResponseExecuteStatementTypeDef(
    _ClientSendCommandResponseExecuteStatementTypeDef
):
    """
    Type definition for `ClientSendCommandResponse` `ExecuteStatement`

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
    """


_ClientSendCommandResponseFetchPagePageValuesTypeDef = TypedDict(
    "_ClientSendCommandResponseFetchPagePageValuesTypeDef",
    {"IonBinary": bytes, "IonText": str},
    total=False,
)


class ClientSendCommandResponseFetchPagePageValuesTypeDef(
    _ClientSendCommandResponseFetchPagePageValuesTypeDef
):
    """
    Type definition for `ClientSendCommandResponseFetchPagePage` `Values`

    A structure that can contains values in multiple encoding formats.

    - **IonBinary** *(bytes) --*

      An Amazon Ion binary value contained in a ``ValueHolder`` structure.

    - **IonText** *(string) --*

      An Amazon Ion plaintext value contained in a ``ValueHolder`` structure.
    """


_ClientSendCommandResponseFetchPagePageTypeDef = TypedDict(
    "_ClientSendCommandResponseFetchPagePageTypeDef",
    {
        "Values": List[ClientSendCommandResponseFetchPagePageValuesTypeDef],
        "NextPageToken": str,
    },
    total=False,
)


class ClientSendCommandResponseFetchPagePageTypeDef(
    _ClientSendCommandResponseFetchPagePageTypeDef
):
    """
    Type definition for `ClientSendCommandResponseFetchPage` `Page`

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


_ClientSendCommandResponseFetchPageTypeDef = TypedDict(
    "_ClientSendCommandResponseFetchPageTypeDef",
    {"Page": ClientSendCommandResponseFetchPagePageTypeDef},
    total=False,
)


class ClientSendCommandResponseFetchPageTypeDef(
    _ClientSendCommandResponseFetchPageTypeDef
):
    """
    Type definition for `ClientSendCommandResponse` `FetchPage`

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


_ClientSendCommandResponseStartSessionTypeDef = TypedDict(
    "_ClientSendCommandResponseStartSessionTypeDef", {"SessionToken": str}, total=False
)


class ClientSendCommandResponseStartSessionTypeDef(
    _ClientSendCommandResponseStartSessionTypeDef
):
    """
    Type definition for `ClientSendCommandResponse` `StartSession`

    Contains the details of the started session that includes a session token. This
    ``SessionToken`` is required for every subsequent command that is issued during the current
    session.

    - **SessionToken** *(string) --*

      Session token of the started session. This ``SessionToken`` is required for every
      subsequent command that is issued during the current session.
    """


_ClientSendCommandResponseStartTransactionTypeDef = TypedDict(
    "_ClientSendCommandResponseStartTransactionTypeDef",
    {"TransactionId": str},
    total=False,
)


class ClientSendCommandResponseStartTransactionTypeDef(
    _ClientSendCommandResponseStartTransactionTypeDef
):
    """
    Type definition for `ClientSendCommandResponse` `StartTransaction`

    Contains the details of the started transaction.

    - **TransactionId** *(string) --*

      The transaction id of the started transaction.
    """


_ClientSendCommandResponseTypeDef = TypedDict(
    "_ClientSendCommandResponseTypeDef",
    {
        "StartSession": ClientSendCommandResponseStartSessionTypeDef,
        "StartTransaction": ClientSendCommandResponseStartTransactionTypeDef,
        "EndSession": Dict,
        "CommitTransaction": ClientSendCommandResponseCommitTransactionTypeDef,
        "AbortTransaction": Dict,
        "ExecuteStatement": ClientSendCommandResponseExecuteStatementTypeDef,
        "FetchPage": ClientSendCommandResponseFetchPageTypeDef,
    },
    total=False,
)


class ClientSendCommandResponseTypeDef(_ClientSendCommandResponseTypeDef):
    """
    Type definition for `ClientSendCommand` `Response`

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


_ClientSendCommandStartSessionTypeDef = TypedDict(
    "_ClientSendCommandStartSessionTypeDef", {"LedgerName": str}
)


class ClientSendCommandStartSessionTypeDef(_ClientSendCommandStartSessionTypeDef):
    """
    Type definition for `ClientSendCommand` `StartSession`

    Command to start a new session. A session token is obtained as part of the response.

    - **LedgerName** *(string) --* **[REQUIRED]**

      The name of the ledger to start a new session against.
    """

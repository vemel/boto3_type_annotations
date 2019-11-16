"Main interface for kms type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCancelKeyDeletionResponseTypeDef",
    "ClientCreateCustomKeyStoreResponseTypeDef",
    "ClientCreateGrantConstraintsTypeDef",
    "ClientCreateGrantResponseTypeDef",
    "ClientCreateKeyResponseKeyMetadataTypeDef",
    "ClientCreateKeyResponseTypeDef",
    "ClientCreateKeyTagsTypeDef",
    "ClientDecryptResponseTypeDef",
    "ClientDescribeCustomKeyStoresResponseCustomKeyStoresTypeDef",
    "ClientDescribeCustomKeyStoresResponseTypeDef",
    "ClientDescribeKeyResponseKeyMetadataTypeDef",
    "ClientDescribeKeyResponseTypeDef",
    "ClientEncryptResponseTypeDef",
    "ClientGenerateDataKeyResponseTypeDef",
    "ClientGenerateDataKeyWithoutPlaintextResponseTypeDef",
    "ClientGenerateRandomResponseTypeDef",
    "ClientGetKeyPolicyResponseTypeDef",
    "ClientGetKeyRotationStatusResponseTypeDef",
    "ClientGetParametersForImportResponseTypeDef",
    "ClientListAliasesResponseAliasesTypeDef",
    "ClientListAliasesResponseTypeDef",
    "ClientListGrantsResponseGrantsConstraintsTypeDef",
    "ClientListGrantsResponseGrantsTypeDef",
    "ClientListGrantsResponseTypeDef",
    "ClientListKeyPoliciesResponseTypeDef",
    "ClientListKeysResponseKeysTypeDef",
    "ClientListKeysResponseTypeDef",
    "ClientListResourceTagsResponseTagsTypeDef",
    "ClientListResourceTagsResponseTypeDef",
    "ClientListRetirableGrantsResponseGrantsConstraintsTypeDef",
    "ClientListRetirableGrantsResponseGrantsTypeDef",
    "ClientListRetirableGrantsResponseTypeDef",
    "ClientReEncryptResponseTypeDef",
    "ClientScheduleKeyDeletionResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ListAliasesPaginatePaginationConfigTypeDef",
    "ListAliasesPaginateResponseAliasesTypeDef",
    "ListAliasesPaginateResponseTypeDef",
    "ListGrantsPaginatePaginationConfigTypeDef",
    "ListGrantsPaginateResponseGrantsConstraintsTypeDef",
    "ListGrantsPaginateResponseGrantsTypeDef",
    "ListGrantsPaginateResponseTypeDef",
    "ListKeyPoliciesPaginatePaginationConfigTypeDef",
    "ListKeyPoliciesPaginateResponseTypeDef",
    "ListKeysPaginatePaginationConfigTypeDef",
    "ListKeysPaginateResponseKeysTypeDef",
    "ListKeysPaginateResponseTypeDef",
)


_ClientCancelKeyDeletionResponseTypeDef = TypedDict(
    "_ClientCancelKeyDeletionResponseTypeDef", {"KeyId": str}, total=False
)


class ClientCancelKeyDeletionResponseTypeDef(_ClientCancelKeyDeletionResponseTypeDef):
    """
    Type definition for `ClientCancelKeyDeletion` `Response`

    - **KeyId** *(string) --*

      The unique identifier of the master key for which deletion is canceled.
    """


_ClientCreateCustomKeyStoreResponseTypeDef = TypedDict(
    "_ClientCreateCustomKeyStoreResponseTypeDef", {"CustomKeyStoreId": str}, total=False
)


class ClientCreateCustomKeyStoreResponseTypeDef(
    _ClientCreateCustomKeyStoreResponseTypeDef
):
    """
    Type definition for `ClientCreateCustomKeyStore` `Response`

    - **CustomKeyStoreId** *(string) --*

      A unique identifier for the new custom key store.
    """


_ClientCreateGrantConstraintsTypeDef = TypedDict(
    "_ClientCreateGrantConstraintsTypeDef",
    {
        "EncryptionContextSubset": Dict[str, str],
        "EncryptionContextEquals": Dict[str, str],
    },
    total=False,
)


class ClientCreateGrantConstraintsTypeDef(_ClientCreateGrantConstraintsTypeDef):
    """
    Type definition for `ClientCreateGrant` `Constraints`

    Allows a cryptographic operation only when the encryption context matches or includes the
    encryption context specified in this structure. For more information about encryption context,
    see `Encryption Context
    <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context>`__ in the *
    *AWS Key Management Service Developer Guide* * .

    - **EncryptionContextSubset** *(dict) --*

      A list of key-value pairs that must be included in the encryption context of the cryptographic
      operation request. The grant allows the cryptographic operation only when the encryption
      context in the request includes the key-value pairs specified in this constraint, although it
      can include additional key-value pairs.

      - *(string) --*

        - *(string) --*

    - **EncryptionContextEquals** *(dict) --*

      A list of key-value pairs that must match the encryption context in the cryptographic operation
      request. The grant allows the operation only when the encryption context in the request is the
      same as the encryption context specified in this constraint.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateGrantResponseTypeDef = TypedDict(
    "_ClientCreateGrantResponseTypeDef",
    {"GrantToken": str, "GrantId": str},
    total=False,
)


class ClientCreateGrantResponseTypeDef(_ClientCreateGrantResponseTypeDef):
    """
    Type definition for `ClientCreateGrant` `Response`

    - **GrantToken** *(string) --*

      The grant token.

      For more information, see `Grant Tokens
      <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the
      *AWS Key Management Service Developer Guide* .

    - **GrantId** *(string) --*

      The unique identifier for the grant.

      You can use the ``GrantId`` in a subsequent  RetireGrant or  RevokeGrant operation.
    """


_ClientCreateKeyResponseKeyMetadataTypeDef = TypedDict(
    "_ClientCreateKeyResponseKeyMetadataTypeDef",
    {
        "AWSAccountId": str,
        "KeyId": str,
        "Arn": str,
        "CreationDate": datetime,
        "Enabled": bool,
        "Description": str,
        "KeyUsage": str,
        "KeyState": str,
        "DeletionDate": datetime,
        "ValidTo": datetime,
        "Origin": str,
        "CustomKeyStoreId": str,
        "CloudHsmClusterId": str,
        "ExpirationModel": str,
        "KeyManager": str,
    },
    total=False,
)


class ClientCreateKeyResponseKeyMetadataTypeDef(
    _ClientCreateKeyResponseKeyMetadataTypeDef
):
    """
    Type definition for `ClientCreateKeyResponse` `KeyMetadata`

    Metadata associated with the CMK.

    - **AWSAccountId** *(string) --*

      The twelve-digit account ID of the AWS account that owns the CMK.

    - **KeyId** *(string) --*

      The globally unique identifier for the CMK.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the CMK. For examples, see `AWS Key Management Service
      (AWS KMS)
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms>`__
      in the Example ARNs section of the *AWS General Reference* .

    - **CreationDate** *(datetime) --*

      The date and time when the CMK was created.

    - **Enabled** *(boolean) --*

      Specifies whether the CMK is enabled. When ``KeyState`` is ``Enabled`` this value is true,
      otherwise it is false.

    - **Description** *(string) --*

      The description of the CMK.

    - **KeyUsage** *(string) --*

      The cryptographic operations for which you can use the CMK. The only valid value is
      ``ENCRYPT_DECRYPT`` , which means you can use the CMK to encrypt and decrypt data.

    - **KeyState** *(string) --*

      The state of the CMK.

      For more information about how key state affects the use of a CMK, see `How Key State
      Affects the Use of a Customer Master Key
      <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
      Management Service Developer Guide* .

    - **DeletionDate** *(datetime) --*

      The date and time after which AWS KMS deletes the CMK. This value is present only when
      ``KeyState`` is ``PendingDeletion`` .

    - **ValidTo** *(datetime) --*

      The time at which the imported key material expires. When the key material expires, AWS KMS
      deletes the key material and the CMK becomes unusable. This value is present only for CMKs
      whose ``Origin`` is ``EXTERNAL`` and whose ``ExpirationModel`` is ``KEY_MATERIAL_EXPIRES``
      , otherwise this value is omitted.

    - **Origin** *(string) --*

      The source of the CMK's key material. When this value is ``AWS_KMS`` , AWS KMS created the
      key material. When this value is ``EXTERNAL`` , the key material was imported from your
      existing key management infrastructure or the CMK lacks key material. When this value is
      ``AWS_CLOUDHSM`` , the key material was created in the AWS CloudHSM cluster associated with
      a custom key store.

    - **CustomKeyStoreId** *(string) --*

      A unique identifier for the `custom key store
      <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
      that contains the CMK. This value is present only when the CMK is created in a custom key
      store.

    - **CloudHsmClusterId** *(string) --*

      The cluster ID of the AWS CloudHSM cluster that contains the key material for the CMK. When
      you create a CMK in a `custom key store
      <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ ,
      AWS KMS creates the key material for the CMK in the associated AWS CloudHSM cluster. This
      value is present only when the CMK is created in a custom key store.

    - **ExpirationModel** *(string) --*

      Specifies whether the CMK's key material expires. This value is present only when
      ``Origin`` is ``EXTERNAL`` , otherwise this value is omitted.

    - **KeyManager** *(string) --*

      The manager of the CMK. CMKs in your AWS account are either customer managed or AWS
      managed. For more information about the difference, see `Customer Master Keys
      <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__ in the
      *AWS Key Management Service Developer Guide* .
    """


_ClientCreateKeyResponseTypeDef = TypedDict(
    "_ClientCreateKeyResponseTypeDef",
    {"KeyMetadata": ClientCreateKeyResponseKeyMetadataTypeDef},
    total=False,
)


class ClientCreateKeyResponseTypeDef(_ClientCreateKeyResponseTypeDef):
    """
    Type definition for `ClientCreateKey` `Response`

    - **KeyMetadata** *(dict) --*

      Metadata associated with the CMK.

      - **AWSAccountId** *(string) --*

        The twelve-digit account ID of the AWS account that owns the CMK.

      - **KeyId** *(string) --*

        The globally unique identifier for the CMK.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the CMK. For examples, see `AWS Key Management Service
        (AWS KMS)
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms>`__
        in the Example ARNs section of the *AWS General Reference* .

      - **CreationDate** *(datetime) --*

        The date and time when the CMK was created.

      - **Enabled** *(boolean) --*

        Specifies whether the CMK is enabled. When ``KeyState`` is ``Enabled`` this value is true,
        otherwise it is false.

      - **Description** *(string) --*

        The description of the CMK.

      - **KeyUsage** *(string) --*

        The cryptographic operations for which you can use the CMK. The only valid value is
        ``ENCRYPT_DECRYPT`` , which means you can use the CMK to encrypt and decrypt data.

      - **KeyState** *(string) --*

        The state of the CMK.

        For more information about how key state affects the use of a CMK, see `How Key State
        Affects the Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

      - **DeletionDate** *(datetime) --*

        The date and time after which AWS KMS deletes the CMK. This value is present only when
        ``KeyState`` is ``PendingDeletion`` .

      - **ValidTo** *(datetime) --*

        The time at which the imported key material expires. When the key material expires, AWS KMS
        deletes the key material and the CMK becomes unusable. This value is present only for CMKs
        whose ``Origin`` is ``EXTERNAL`` and whose ``ExpirationModel`` is ``KEY_MATERIAL_EXPIRES``
        , otherwise this value is omitted.

      - **Origin** *(string) --*

        The source of the CMK's key material. When this value is ``AWS_KMS`` , AWS KMS created the
        key material. When this value is ``EXTERNAL`` , the key material was imported from your
        existing key management infrastructure or the CMK lacks key material. When this value is
        ``AWS_CLOUDHSM`` , the key material was created in the AWS CloudHSM cluster associated with
        a custom key store.

      - **CustomKeyStoreId** *(string) --*

        A unique identifier for the `custom key store
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
        that contains the CMK. This value is present only when the CMK is created in a custom key
        store.

      - **CloudHsmClusterId** *(string) --*

        The cluster ID of the AWS CloudHSM cluster that contains the key material for the CMK. When
        you create a CMK in a `custom key store
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ ,
        AWS KMS creates the key material for the CMK in the associated AWS CloudHSM cluster. This
        value is present only when the CMK is created in a custom key store.

      - **ExpirationModel** *(string) --*

        Specifies whether the CMK's key material expires. This value is present only when
        ``Origin`` is ``EXTERNAL`` , otherwise this value is omitted.

      - **KeyManager** *(string) --*

        The manager of the CMK. CMKs in your AWS account are either customer managed or AWS
        managed. For more information about the difference, see `Customer Master Keys
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__ in the
        *AWS Key Management Service Developer Guide* .
    """


_ClientCreateKeyTagsTypeDef = TypedDict(
    "_ClientCreateKeyTagsTypeDef", {"TagKey": str, "TagValue": str}
)


class ClientCreateKeyTagsTypeDef(_ClientCreateKeyTagsTypeDef):
    """
    Type definition for `ClientCreateKey` `Tags`

    A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both
    required, but tag values can be empty (null) strings.

    For information about the rules that apply to tag keys and tag values, see `User-Defined Tag
    Restrictions
    <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__
    in the *AWS Billing and Cost Management User Guide* .

    - **TagKey** *(string) --* **[REQUIRED]**

      The key of the tag.

    - **TagValue** *(string) --* **[REQUIRED]**

      The value of the tag.
    """


_ClientDecryptResponseTypeDef = TypedDict(
    "_ClientDecryptResponseTypeDef", {"KeyId": str, "Plaintext": bytes}, total=False
)


class ClientDecryptResponseTypeDef(_ClientDecryptResponseTypeDef):
    """
    Type definition for `ClientDecrypt` `Response`

    - **KeyId** *(string) --*

      ARN of the key used to perform the decryption. This value is returned if no errors are
      encountered during the operation.

    - **Plaintext** *(bytes) --*

      Decrypted plaintext data. When you use the HTTP API or the AWS CLI, the value is
      Base64-encoded. Otherwise, it is not encoded.
    """


_ClientDescribeCustomKeyStoresResponseCustomKeyStoresTypeDef = TypedDict(
    "_ClientDescribeCustomKeyStoresResponseCustomKeyStoresTypeDef",
    {
        "CustomKeyStoreId": str,
        "CustomKeyStoreName": str,
        "CloudHsmClusterId": str,
        "TrustAnchorCertificate": str,
        "ConnectionState": str,
        "ConnectionErrorCode": str,
        "CreationDate": datetime,
    },
    total=False,
)


class ClientDescribeCustomKeyStoresResponseCustomKeyStoresTypeDef(
    _ClientDescribeCustomKeyStoresResponseCustomKeyStoresTypeDef
):
    """
    Type definition for `ClientDescribeCustomKeyStoresResponse` `CustomKeyStores`

    Contains information about each custom key store in the custom key store list.

    - **CustomKeyStoreId** *(string) --*

      A unique identifier for the custom key store.

    - **CustomKeyStoreName** *(string) --*

      The user-specified friendly name for the custom key store.

    - **CloudHsmClusterId** *(string) --*

      A unique identifier for the AWS CloudHSM cluster that is associated with the custom key
      store.

    - **TrustAnchorCertificate** *(string) --*

      The trust anchor certificate of the associated AWS CloudHSM cluster. When you `initialize
      the cluster
      <https://docs.aws.amazon.com/cloudhsm/latest/userguide/initialize-cluster.html#sign-csr>`__
      , you create this certificate and save it in the ``customerCA.crt`` file.

    - **ConnectionState** *(string) --*

      Indicates whether the custom key store is connected to its AWS CloudHSM cluster.

      You can create and use CMKs in your custom key stores only when its connection state is
      ``CONNECTED`` .

      The value is ``DISCONNECTED`` if the key store has never been connected or you use the
      DisconnectCustomKeyStore operation to disconnect it. If the value is ``CONNECTED`` but
      you are having trouble using the custom key store, make sure that its associated AWS
      CloudHSM cluster is active and contains at least one active HSM.

      A value of ``FAILED`` indicates that an attempt to connect was unsuccessful. For help
      resolving a connection failure, see `Troubleshooting a Custom Key Store
      <https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html>`__ in the *AWS
      Key Management Service Developer Guide* .

    - **ConnectionErrorCode** *(string) --*

      Describes the connection error. Valid values are:

      * ``CLUSTER_NOT_FOUND`` - AWS KMS cannot find the AWS CloudHSM cluster with the specified
      cluster ID.

      * ``INSUFFICIENT_CLOUDHSM_HSMS`` - The associated AWS CloudHSM cluster does not contain
      any active HSMs. To connect a custom key store to its AWS CloudHSM cluster, the cluster
      must contain at least one active HSM.

      * ``INTERNAL_ERROR`` - AWS KMS could not complete the request due to an internal error.
      Retry the request. For ``ConnectCustomKeyStore`` requests, disconnect the custom key
      store before trying to connect again.

      * ``INVALID_CREDENTIALS`` - AWS KMS does not have the correct password for the
      ``kmsuser`` crypto user in the AWS CloudHSM cluster.

      * ``NETWORK_ERRORS`` - Network errors are preventing AWS KMS from connecting to the
      custom key store.

      * ``USER_LOCKED_OUT`` - The ``kmsuser`` CU account is locked out of the associated AWS
      CloudHSM cluster due to too many failed password attempts. Before you can connect your
      custom key store to its AWS CloudHSM cluster, you must change the ``kmsuser`` account
      password and update the password value for the custom key store.

      For help with connection failures, see `Troubleshooting Custom Key Stores
      <https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html>`__ in the *AWS
      Key Management Service Developer Guide* .

    - **CreationDate** *(datetime) --*

      The date and time when the custom key store was created.
    """


_ClientDescribeCustomKeyStoresResponseTypeDef = TypedDict(
    "_ClientDescribeCustomKeyStoresResponseTypeDef",
    {
        "CustomKeyStores": List[
            ClientDescribeCustomKeyStoresResponseCustomKeyStoresTypeDef
        ],
        "NextMarker": str,
        "Truncated": bool,
    },
    total=False,
)


class ClientDescribeCustomKeyStoresResponseTypeDef(
    _ClientDescribeCustomKeyStoresResponseTypeDef
):
    """
    Type definition for `ClientDescribeCustomKeyStores` `Response`

    - **CustomKeyStores** *(list) --*

      Contains metadata about each custom key store.

      - *(dict) --*

        Contains information about each custom key store in the custom key store list.

        - **CustomKeyStoreId** *(string) --*

          A unique identifier for the custom key store.

        - **CustomKeyStoreName** *(string) --*

          The user-specified friendly name for the custom key store.

        - **CloudHsmClusterId** *(string) --*

          A unique identifier for the AWS CloudHSM cluster that is associated with the custom key
          store.

        - **TrustAnchorCertificate** *(string) --*

          The trust anchor certificate of the associated AWS CloudHSM cluster. When you `initialize
          the cluster
          <https://docs.aws.amazon.com/cloudhsm/latest/userguide/initialize-cluster.html#sign-csr>`__
          , you create this certificate and save it in the ``customerCA.crt`` file.

        - **ConnectionState** *(string) --*

          Indicates whether the custom key store is connected to its AWS CloudHSM cluster.

          You can create and use CMKs in your custom key stores only when its connection state is
          ``CONNECTED`` .

          The value is ``DISCONNECTED`` if the key store has never been connected or you use the
          DisconnectCustomKeyStore operation to disconnect it. If the value is ``CONNECTED`` but
          you are having trouble using the custom key store, make sure that its associated AWS
          CloudHSM cluster is active and contains at least one active HSM.

          A value of ``FAILED`` indicates that an attempt to connect was unsuccessful. For help
          resolving a connection failure, see `Troubleshooting a Custom Key Store
          <https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html>`__ in the *AWS
          Key Management Service Developer Guide* .

        - **ConnectionErrorCode** *(string) --*

          Describes the connection error. Valid values are:

          * ``CLUSTER_NOT_FOUND`` - AWS KMS cannot find the AWS CloudHSM cluster with the specified
          cluster ID.

          * ``INSUFFICIENT_CLOUDHSM_HSMS`` - The associated AWS CloudHSM cluster does not contain
          any active HSMs. To connect a custom key store to its AWS CloudHSM cluster, the cluster
          must contain at least one active HSM.

          * ``INTERNAL_ERROR`` - AWS KMS could not complete the request due to an internal error.
          Retry the request. For ``ConnectCustomKeyStore`` requests, disconnect the custom key
          store before trying to connect again.

          * ``INVALID_CREDENTIALS`` - AWS KMS does not have the correct password for the
          ``kmsuser`` crypto user in the AWS CloudHSM cluster.

          * ``NETWORK_ERRORS`` - Network errors are preventing AWS KMS from connecting to the
          custom key store.

          * ``USER_LOCKED_OUT`` - The ``kmsuser`` CU account is locked out of the associated AWS
          CloudHSM cluster due to too many failed password attempts. Before you can connect your
          custom key store to its AWS CloudHSM cluster, you must change the ``kmsuser`` account
          password and update the password value for the custom key store.

          For help with connection failures, see `Troubleshooting Custom Key Stores
          <https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html>`__ in the *AWS
          Key Management Service Developer Guide* .

        - **CreationDate** *(datetime) --*

          The date and time when the custom key store was created.

    - **NextMarker** *(string) --*

      When ``Truncated`` is true, this element is present and contains the value to use for the
      ``Marker`` parameter in a subsequent request.

    - **Truncated** *(boolean) --*

      A flag that indicates whether there are more items in the list. When this value is true, the
      list in this response is truncated. To get more items, pass the value of the ``NextMarker``
      element in thisresponse to the ``Marker`` parameter in a subsequent request.
    """


_ClientDescribeKeyResponseKeyMetadataTypeDef = TypedDict(
    "_ClientDescribeKeyResponseKeyMetadataTypeDef",
    {
        "AWSAccountId": str,
        "KeyId": str,
        "Arn": str,
        "CreationDate": datetime,
        "Enabled": bool,
        "Description": str,
        "KeyUsage": str,
        "KeyState": str,
        "DeletionDate": datetime,
        "ValidTo": datetime,
        "Origin": str,
        "CustomKeyStoreId": str,
        "CloudHsmClusterId": str,
        "ExpirationModel": str,
        "KeyManager": str,
    },
    total=False,
)


class ClientDescribeKeyResponseKeyMetadataTypeDef(
    _ClientDescribeKeyResponseKeyMetadataTypeDef
):
    """
    Type definition for `ClientDescribeKeyResponse` `KeyMetadata`

    Metadata associated with the key.

    - **AWSAccountId** *(string) --*

      The twelve-digit account ID of the AWS account that owns the CMK.

    - **KeyId** *(string) --*

      The globally unique identifier for the CMK.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the CMK. For examples, see `AWS Key Management Service
      (AWS KMS)
      <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms>`__
      in the Example ARNs section of the *AWS General Reference* .

    - **CreationDate** *(datetime) --*

      The date and time when the CMK was created.

    - **Enabled** *(boolean) --*

      Specifies whether the CMK is enabled. When ``KeyState`` is ``Enabled`` this value is true,
      otherwise it is false.

    - **Description** *(string) --*

      The description of the CMK.

    - **KeyUsage** *(string) --*

      The cryptographic operations for which you can use the CMK. The only valid value is
      ``ENCRYPT_DECRYPT`` , which means you can use the CMK to encrypt and decrypt data.

    - **KeyState** *(string) --*

      The state of the CMK.

      For more information about how key state affects the use of a CMK, see `How Key State
      Affects the Use of a Customer Master Key
      <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
      Management Service Developer Guide* .

    - **DeletionDate** *(datetime) --*

      The date and time after which AWS KMS deletes the CMK. This value is present only when
      ``KeyState`` is ``PendingDeletion`` .

    - **ValidTo** *(datetime) --*

      The time at which the imported key material expires. When the key material expires, AWS KMS
      deletes the key material and the CMK becomes unusable. This value is present only for CMKs
      whose ``Origin`` is ``EXTERNAL`` and whose ``ExpirationModel`` is ``KEY_MATERIAL_EXPIRES``
      , otherwise this value is omitted.

    - **Origin** *(string) --*

      The source of the CMK's key material. When this value is ``AWS_KMS`` , AWS KMS created the
      key material. When this value is ``EXTERNAL`` , the key material was imported from your
      existing key management infrastructure or the CMK lacks key material. When this value is
      ``AWS_CLOUDHSM`` , the key material was created in the AWS CloudHSM cluster associated with
      a custom key store.

    - **CustomKeyStoreId** *(string) --*

      A unique identifier for the `custom key store
      <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
      that contains the CMK. This value is present only when the CMK is created in a custom key
      store.

    - **CloudHsmClusterId** *(string) --*

      The cluster ID of the AWS CloudHSM cluster that contains the key material for the CMK. When
      you create a CMK in a `custom key store
      <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ ,
      AWS KMS creates the key material for the CMK in the associated AWS CloudHSM cluster. This
      value is present only when the CMK is created in a custom key store.

    - **ExpirationModel** *(string) --*

      Specifies whether the CMK's key material expires. This value is present only when
      ``Origin`` is ``EXTERNAL`` , otherwise this value is omitted.

    - **KeyManager** *(string) --*

      The manager of the CMK. CMKs in your AWS account are either customer managed or AWS
      managed. For more information about the difference, see `Customer Master Keys
      <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__ in the
      *AWS Key Management Service Developer Guide* .
    """


_ClientDescribeKeyResponseTypeDef = TypedDict(
    "_ClientDescribeKeyResponseTypeDef",
    {"KeyMetadata": ClientDescribeKeyResponseKeyMetadataTypeDef},
    total=False,
)


class ClientDescribeKeyResponseTypeDef(_ClientDescribeKeyResponseTypeDef):
    """
    Type definition for `ClientDescribeKey` `Response`

    - **KeyMetadata** *(dict) --*

      Metadata associated with the key.

      - **AWSAccountId** *(string) --*

        The twelve-digit account ID of the AWS account that owns the CMK.

      - **KeyId** *(string) --*

        The globally unique identifier for the CMK.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the CMK. For examples, see `AWS Key Management Service
        (AWS KMS)
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms>`__
        in the Example ARNs section of the *AWS General Reference* .

      - **CreationDate** *(datetime) --*

        The date and time when the CMK was created.

      - **Enabled** *(boolean) --*

        Specifies whether the CMK is enabled. When ``KeyState`` is ``Enabled`` this value is true,
        otherwise it is false.

      - **Description** *(string) --*

        The description of the CMK.

      - **KeyUsage** *(string) --*

        The cryptographic operations for which you can use the CMK. The only valid value is
        ``ENCRYPT_DECRYPT`` , which means you can use the CMK to encrypt and decrypt data.

      - **KeyState** *(string) --*

        The state of the CMK.

        For more information about how key state affects the use of a CMK, see `How Key State
        Affects the Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

      - **DeletionDate** *(datetime) --*

        The date and time after which AWS KMS deletes the CMK. This value is present only when
        ``KeyState`` is ``PendingDeletion`` .

      - **ValidTo** *(datetime) --*

        The time at which the imported key material expires. When the key material expires, AWS KMS
        deletes the key material and the CMK becomes unusable. This value is present only for CMKs
        whose ``Origin`` is ``EXTERNAL`` and whose ``ExpirationModel`` is ``KEY_MATERIAL_EXPIRES``
        , otherwise this value is omitted.

      - **Origin** *(string) --*

        The source of the CMK's key material. When this value is ``AWS_KMS`` , AWS KMS created the
        key material. When this value is ``EXTERNAL`` , the key material was imported from your
        existing key management infrastructure or the CMK lacks key material. When this value is
        ``AWS_CLOUDHSM`` , the key material was created in the AWS CloudHSM cluster associated with
        a custom key store.

      - **CustomKeyStoreId** *(string) --*

        A unique identifier for the `custom key store
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
        that contains the CMK. This value is present only when the CMK is created in a custom key
        store.

      - **CloudHsmClusterId** *(string) --*

        The cluster ID of the AWS CloudHSM cluster that contains the key material for the CMK. When
        you create a CMK in a `custom key store
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ ,
        AWS KMS creates the key material for the CMK in the associated AWS CloudHSM cluster. This
        value is present only when the CMK is created in a custom key store.

      - **ExpirationModel** *(string) --*

        Specifies whether the CMK's key material expires. This value is present only when
        ``Origin`` is ``EXTERNAL`` , otherwise this value is omitted.

      - **KeyManager** *(string) --*

        The manager of the CMK. CMKs in your AWS account are either customer managed or AWS
        managed. For more information about the difference, see `Customer Master Keys
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__ in the
        *AWS Key Management Service Developer Guide* .
    """


_ClientEncryptResponseTypeDef = TypedDict(
    "_ClientEncryptResponseTypeDef",
    {"CiphertextBlob": bytes, "KeyId": str},
    total=False,
)


class ClientEncryptResponseTypeDef(_ClientEncryptResponseTypeDef):
    """
    Type definition for `ClientEncrypt` `Response`

    - **CiphertextBlob** *(bytes) --*

      The encrypted plaintext. When you use the HTTP API or the AWS CLI, the value is
      Base64-encoded. Otherwise, it is not encoded.

    - **KeyId** *(string) --*

      The ID of the key used during encryption.
    """


_ClientGenerateDataKeyResponseTypeDef = TypedDict(
    "_ClientGenerateDataKeyResponseTypeDef",
    {"CiphertextBlob": bytes, "Plaintext": bytes, "KeyId": str},
    total=False,
)


class ClientGenerateDataKeyResponseTypeDef(_ClientGenerateDataKeyResponseTypeDef):
    """
    Type definition for `ClientGenerateDataKey` `Response`

    - **CiphertextBlob** *(bytes) --*

      The encrypted copy of the data key. When you use the HTTP API or the AWS CLI, the value is
      Base64-encoded. Otherwise, it is not encoded.

    - **Plaintext** *(bytes) --*

      The plaintext data key. When you use the HTTP API or the AWS CLI, the value is
      Base64-encoded. Otherwise, it is not encoded. Use this data key to encrypt your data outside
      of KMS. Then, remove it from memory as soon as possible.

    - **KeyId** *(string) --*

      The identifier of the CMK that encrypted the data key.
    """


_ClientGenerateDataKeyWithoutPlaintextResponseTypeDef = TypedDict(
    "_ClientGenerateDataKeyWithoutPlaintextResponseTypeDef",
    {"CiphertextBlob": bytes, "KeyId": str},
    total=False,
)


class ClientGenerateDataKeyWithoutPlaintextResponseTypeDef(
    _ClientGenerateDataKeyWithoutPlaintextResponseTypeDef
):
    """
    Type definition for `ClientGenerateDataKeyWithoutPlaintext` `Response`

    - **CiphertextBlob** *(bytes) --*

      The encrypted data key. When you use the HTTP API or the AWS CLI, the value is
      Base64-encoded. Otherwise, it is not encoded.

    - **KeyId** *(string) --*

      The identifier of the CMK that encrypted the data key.
    """


_ClientGenerateRandomResponseTypeDef = TypedDict(
    "_ClientGenerateRandomResponseTypeDef", {"Plaintext": bytes}, total=False
)


class ClientGenerateRandomResponseTypeDef(_ClientGenerateRandomResponseTypeDef):
    """
    Type definition for `ClientGenerateRandom` `Response`

    - **Plaintext** *(bytes) --*

      The random byte string. When you use the HTTP API or the AWS CLI, the value is
      Base64-encoded. Otherwise, it is not encoded.
    """


_ClientGetKeyPolicyResponseTypeDef = TypedDict(
    "_ClientGetKeyPolicyResponseTypeDef", {"Policy": str}, total=False
)


class ClientGetKeyPolicyResponseTypeDef(_ClientGetKeyPolicyResponseTypeDef):
    """
    Type definition for `ClientGetKeyPolicy` `Response`

    - **Policy** *(string) --*

      A key policy document in JSON format.
    """


_ClientGetKeyRotationStatusResponseTypeDef = TypedDict(
    "_ClientGetKeyRotationStatusResponseTypeDef",
    {"KeyRotationEnabled": bool},
    total=False,
)


class ClientGetKeyRotationStatusResponseTypeDef(
    _ClientGetKeyRotationStatusResponseTypeDef
):
    """
    Type definition for `ClientGetKeyRotationStatus` `Response`

    - **KeyRotationEnabled** *(boolean) --*

      A Boolean value that specifies whether key rotation is enabled.
    """


_ClientGetParametersForImportResponseTypeDef = TypedDict(
    "_ClientGetParametersForImportResponseTypeDef",
    {
        "KeyId": str,
        "ImportToken": bytes,
        "PublicKey": bytes,
        "ParametersValidTo": datetime,
    },
    total=False,
)


class ClientGetParametersForImportResponseTypeDef(
    _ClientGetParametersForImportResponseTypeDef
):
    """
    Type definition for `ClientGetParametersForImport` `Response`

    - **KeyId** *(string) --*

      The identifier of the CMK to use in a subsequent  ImportKeyMaterial request. This is the same
      CMK specified in the ``GetParametersForImport`` request.

    - **ImportToken** *(bytes) --*

      The import token to send in a subsequent  ImportKeyMaterial request.

    - **PublicKey** *(bytes) --*

      The public key to use to encrypt the key material before importing it with  ImportKeyMaterial
      .

    - **ParametersValidTo** *(datetime) --*

      The time at which the import token and public key are no longer valid. After this time, you
      cannot use them to make an  ImportKeyMaterial request and you must send another
      ``GetParametersForImport`` request to get new ones.
    """


_ClientListAliasesResponseAliasesTypeDef = TypedDict(
    "_ClientListAliasesResponseAliasesTypeDef",
    {"AliasName": str, "AliasArn": str, "TargetKeyId": str},
    total=False,
)


class ClientListAliasesResponseAliasesTypeDef(_ClientListAliasesResponseAliasesTypeDef):
    """
    Type definition for `ClientListAliasesResponse` `Aliases`

    Contains information about an alias.

    - **AliasName** *(string) --*

      String that contains the alias. This value begins with ``alias/`` .

    - **AliasArn** *(string) --*

      String that contains the key ARN.

    - **TargetKeyId** *(string) --*

      String that contains the key identifier referred to by the alias.
    """


_ClientListAliasesResponseTypeDef = TypedDict(
    "_ClientListAliasesResponseTypeDef",
    {
        "Aliases": List[ClientListAliasesResponseAliasesTypeDef],
        "NextMarker": str,
        "Truncated": bool,
    },
    total=False,
)


class ClientListAliasesResponseTypeDef(_ClientListAliasesResponseTypeDef):
    """
    Type definition for `ClientListAliases` `Response`

    - **Aliases** *(list) --*

      A list of aliases.

      - *(dict) --*

        Contains information about an alias.

        - **AliasName** *(string) --*

          String that contains the alias. This value begins with ``alias/`` .

        - **AliasArn** *(string) --*

          String that contains the key ARN.

        - **TargetKeyId** *(string) --*

          String that contains the key identifier referred to by the alias.

    - **NextMarker** *(string) --*

      When ``Truncated`` is true, this element is present and contains the value to use for the
      ``Marker`` parameter in a subsequent request.

    - **Truncated** *(boolean) --*

      A flag that indicates whether there are more items in the list. When this value is true, the
      list in this response is truncated. To get more items, pass the value of the ``NextMarker``
      element in thisresponse to the ``Marker`` parameter in a subsequent request.
    """


_ClientListGrantsResponseGrantsConstraintsTypeDef = TypedDict(
    "_ClientListGrantsResponseGrantsConstraintsTypeDef",
    {
        "EncryptionContextSubset": Dict[str, str],
        "EncryptionContextEquals": Dict[str, str],
    },
    total=False,
)


class ClientListGrantsResponseGrantsConstraintsTypeDef(
    _ClientListGrantsResponseGrantsConstraintsTypeDef
):
    """
    Type definition for `ClientListGrantsResponseGrants` `Constraints`

    A list of key-value pairs that must be present in the encryption context of certain
    subsequent operations that the grant allows.

    - **EncryptionContextSubset** *(dict) --*

      A list of key-value pairs that must be included in the encryption context of the
      cryptographic operation request. The grant allows the cryptographic operation only when
      the encryption context in the request includes the key-value pairs specified in this
      constraint, although it can include additional key-value pairs.

      - *(string) --*

        - *(string) --*

    - **EncryptionContextEquals** *(dict) --*

      A list of key-value pairs that must match the encryption context in the cryptographic
      operation request. The grant allows the operation only when the encryption context in
      the request is the same as the encryption context specified in this constraint.

      - *(string) --*

        - *(string) --*
    """


_ClientListGrantsResponseGrantsTypeDef = TypedDict(
    "_ClientListGrantsResponseGrantsTypeDef",
    {
        "KeyId": str,
        "GrantId": str,
        "Name": str,
        "CreationDate": datetime,
        "GranteePrincipal": str,
        "RetiringPrincipal": str,
        "IssuingAccount": str,
        "Operations": List[str],
        "Constraints": ClientListGrantsResponseGrantsConstraintsTypeDef,
    },
    total=False,
)


class ClientListGrantsResponseGrantsTypeDef(_ClientListGrantsResponseGrantsTypeDef):
    """
    Type definition for `ClientListGrantsResponse` `Grants`

    Contains information about an entry in a list of grants.

    - **KeyId** *(string) --*

      The unique identifier for the customer master key (CMK) to which the grant applies.

    - **GrantId** *(string) --*

      The unique identifier for the grant.

    - **Name** *(string) --*

      The friendly name that identifies the grant. If a name was provided in the  CreateGrant
      request, that name is returned. Otherwise this value is null.

    - **CreationDate** *(datetime) --*

      The date and time when the grant was created.

    - **GranteePrincipal** *(string) --*

      The principal that receives the grant's permissions.

    - **RetiringPrincipal** *(string) --*

      The principal that can retire the grant.

    - **IssuingAccount** *(string) --*

      The AWS account under which the grant was issued.

    - **Operations** *(list) --*

      The list of operations permitted by the grant.

      - *(string) --*

    - **Constraints** *(dict) --*

      A list of key-value pairs that must be present in the encryption context of certain
      subsequent operations that the grant allows.

      - **EncryptionContextSubset** *(dict) --*

        A list of key-value pairs that must be included in the encryption context of the
        cryptographic operation request. The grant allows the cryptographic operation only when
        the encryption context in the request includes the key-value pairs specified in this
        constraint, although it can include additional key-value pairs.

        - *(string) --*

          - *(string) --*

      - **EncryptionContextEquals** *(dict) --*

        A list of key-value pairs that must match the encryption context in the cryptographic
        operation request. The grant allows the operation only when the encryption context in
        the request is the same as the encryption context specified in this constraint.

        - *(string) --*

          - *(string) --*
    """


_ClientListGrantsResponseTypeDef = TypedDict(
    "_ClientListGrantsResponseTypeDef",
    {
        "Grants": List[ClientListGrantsResponseGrantsTypeDef],
        "NextMarker": str,
        "Truncated": bool,
    },
    total=False,
)


class ClientListGrantsResponseTypeDef(_ClientListGrantsResponseTypeDef):
    """
    Type definition for `ClientListGrants` `Response`

    - **Grants** *(list) --*

      A list of grants.

      - *(dict) --*

        Contains information about an entry in a list of grants.

        - **KeyId** *(string) --*

          The unique identifier for the customer master key (CMK) to which the grant applies.

        - **GrantId** *(string) --*

          The unique identifier for the grant.

        - **Name** *(string) --*

          The friendly name that identifies the grant. If a name was provided in the  CreateGrant
          request, that name is returned. Otherwise this value is null.

        - **CreationDate** *(datetime) --*

          The date and time when the grant was created.

        - **GranteePrincipal** *(string) --*

          The principal that receives the grant's permissions.

        - **RetiringPrincipal** *(string) --*

          The principal that can retire the grant.

        - **IssuingAccount** *(string) --*

          The AWS account under which the grant was issued.

        - **Operations** *(list) --*

          The list of operations permitted by the grant.

          - *(string) --*

        - **Constraints** *(dict) --*

          A list of key-value pairs that must be present in the encryption context of certain
          subsequent operations that the grant allows.

          - **EncryptionContextSubset** *(dict) --*

            A list of key-value pairs that must be included in the encryption context of the
            cryptographic operation request. The grant allows the cryptographic operation only when
            the encryption context in the request includes the key-value pairs specified in this
            constraint, although it can include additional key-value pairs.

            - *(string) --*

              - *(string) --*

          - **EncryptionContextEquals** *(dict) --*

            A list of key-value pairs that must match the encryption context in the cryptographic
            operation request. The grant allows the operation only when the encryption context in
            the request is the same as the encryption context specified in this constraint.

            - *(string) --*

              - *(string) --*

    - **NextMarker** *(string) --*

      When ``Truncated`` is true, this element is present and contains the value to use for the
      ``Marker`` parameter in a subsequent request.

    - **Truncated** *(boolean) --*

      A flag that indicates whether there are more items in the list. When this value is true, the
      list in this response is truncated. To get more items, pass the value of the ``NextMarker``
      element in thisresponse to the ``Marker`` parameter in a subsequent request.
    """


_ClientListKeyPoliciesResponseTypeDef = TypedDict(
    "_ClientListKeyPoliciesResponseTypeDef",
    {"PolicyNames": List[str], "NextMarker": str, "Truncated": bool},
    total=False,
)


class ClientListKeyPoliciesResponseTypeDef(_ClientListKeyPoliciesResponseTypeDef):
    """
    Type definition for `ClientListKeyPolicies` `Response`

    - **PolicyNames** *(list) --*

      A list of key policy names. The only valid value is ``default`` .

      - *(string) --*

    - **NextMarker** *(string) --*

      When ``Truncated`` is true, this element is present and contains the value to use for the
      ``Marker`` parameter in a subsequent request.

    - **Truncated** *(boolean) --*

      A flag that indicates whether there are more items in the list. When this value is true, the
      list in this response is truncated. To get more items, pass the value of the ``NextMarker``
      element in thisresponse to the ``Marker`` parameter in a subsequent request.
    """


_ClientListKeysResponseKeysTypeDef = TypedDict(
    "_ClientListKeysResponseKeysTypeDef", {"KeyId": str, "KeyArn": str}, total=False
)


class ClientListKeysResponseKeysTypeDef(_ClientListKeysResponseKeysTypeDef):
    """
    Type definition for `ClientListKeysResponse` `Keys`

    Contains information about each entry in the key list.

    - **KeyId** *(string) --*

      Unique identifier of the key.

    - **KeyArn** *(string) --*

      ARN of the key.
    """


_ClientListKeysResponseTypeDef = TypedDict(
    "_ClientListKeysResponseTypeDef",
    {
        "Keys": List[ClientListKeysResponseKeysTypeDef],
        "NextMarker": str,
        "Truncated": bool,
    },
    total=False,
)


class ClientListKeysResponseTypeDef(_ClientListKeysResponseTypeDef):
    """
    Type definition for `ClientListKeys` `Response`

    - **Keys** *(list) --*

      A list of customer master keys (CMKs).

      - *(dict) --*

        Contains information about each entry in the key list.

        - **KeyId** *(string) --*

          Unique identifier of the key.

        - **KeyArn** *(string) --*

          ARN of the key.

    - **NextMarker** *(string) --*

      When ``Truncated`` is true, this element is present and contains the value to use for the
      ``Marker`` parameter in a subsequent request.

    - **Truncated** *(boolean) --*

      A flag that indicates whether there are more items in the list. When this value is true, the
      list in this response is truncated. To get more items, pass the value of the ``NextMarker``
      element in thisresponse to the ``Marker`` parameter in a subsequent request.
    """


_ClientListResourceTagsResponseTagsTypeDef = TypedDict(
    "_ClientListResourceTagsResponseTagsTypeDef",
    {"TagKey": str, "TagValue": str},
    total=False,
)


class ClientListResourceTagsResponseTagsTypeDef(
    _ClientListResourceTagsResponseTagsTypeDef
):
    """
    Type definition for `ClientListResourceTagsResponse` `Tags`

    A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are
    both required, but tag values can be empty (null) strings.

    For information about the rules that apply to tag keys and tag values, see `User-Defined
    Tag Restrictions
    <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__
    in the *AWS Billing and Cost Management User Guide* .

    - **TagKey** *(string) --*

      The key of the tag.

    - **TagValue** *(string) --*

      The value of the tag.
    """


_ClientListResourceTagsResponseTypeDef = TypedDict(
    "_ClientListResourceTagsResponseTypeDef",
    {
        "Tags": List[ClientListResourceTagsResponseTagsTypeDef],
        "NextMarker": str,
        "Truncated": bool,
    },
    total=False,
)


class ClientListResourceTagsResponseTypeDef(_ClientListResourceTagsResponseTypeDef):
    """
    Type definition for `ClientListResourceTags` `Response`

    - **Tags** *(list) --*

      A list of tags. Each tag consists of a tag key and a tag value.

      - *(dict) --*

        A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are
        both required, but tag values can be empty (null) strings.

        For information about the rules that apply to tag keys and tag values, see `User-Defined
        Tag Restrictions
        <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__
        in the *AWS Billing and Cost Management User Guide* .

        - **TagKey** *(string) --*

          The key of the tag.

        - **TagValue** *(string) --*

          The value of the tag.

    - **NextMarker** *(string) --*

      When ``Truncated`` is true, this element is present and contains the value to use for the
      ``Marker`` parameter in a subsequent request.

      Do not assume or infer any information from this value.

    - **Truncated** *(boolean) --*

      A flag that indicates whether there are more items in the list. When this value is true, the
      list in this response is truncated. To get more items, pass the value of the ``NextMarker``
      element in thisresponse to the ``Marker`` parameter in a subsequent request.
    """


_ClientListRetirableGrantsResponseGrantsConstraintsTypeDef = TypedDict(
    "_ClientListRetirableGrantsResponseGrantsConstraintsTypeDef",
    {
        "EncryptionContextSubset": Dict[str, str],
        "EncryptionContextEquals": Dict[str, str],
    },
    total=False,
)


class ClientListRetirableGrantsResponseGrantsConstraintsTypeDef(
    _ClientListRetirableGrantsResponseGrantsConstraintsTypeDef
):
    """
    Type definition for `ClientListRetirableGrantsResponseGrants` `Constraints`

    A list of key-value pairs that must be present in the encryption context of certain
    subsequent operations that the grant allows.

    - **EncryptionContextSubset** *(dict) --*

      A list of key-value pairs that must be included in the encryption context of the
      cryptographic operation request. The grant allows the cryptographic operation only when
      the encryption context in the request includes the key-value pairs specified in this
      constraint, although it can include additional key-value pairs.

      - *(string) --*

        - *(string) --*

    - **EncryptionContextEquals** *(dict) --*

      A list of key-value pairs that must match the encryption context in the cryptographic
      operation request. The grant allows the operation only when the encryption context in
      the request is the same as the encryption context specified in this constraint.

      - *(string) --*

        - *(string) --*
    """


_ClientListRetirableGrantsResponseGrantsTypeDef = TypedDict(
    "_ClientListRetirableGrantsResponseGrantsTypeDef",
    {
        "KeyId": str,
        "GrantId": str,
        "Name": str,
        "CreationDate": datetime,
        "GranteePrincipal": str,
        "RetiringPrincipal": str,
        "IssuingAccount": str,
        "Operations": List[str],
        "Constraints": ClientListRetirableGrantsResponseGrantsConstraintsTypeDef,
    },
    total=False,
)


class ClientListRetirableGrantsResponseGrantsTypeDef(
    _ClientListRetirableGrantsResponseGrantsTypeDef
):
    """
    Type definition for `ClientListRetirableGrantsResponse` `Grants`

    Contains information about an entry in a list of grants.

    - **KeyId** *(string) --*

      The unique identifier for the customer master key (CMK) to which the grant applies.

    - **GrantId** *(string) --*

      The unique identifier for the grant.

    - **Name** *(string) --*

      The friendly name that identifies the grant. If a name was provided in the  CreateGrant
      request, that name is returned. Otherwise this value is null.

    - **CreationDate** *(datetime) --*

      The date and time when the grant was created.

    - **GranteePrincipal** *(string) --*

      The principal that receives the grant's permissions.

    - **RetiringPrincipal** *(string) --*

      The principal that can retire the grant.

    - **IssuingAccount** *(string) --*

      The AWS account under which the grant was issued.

    - **Operations** *(list) --*

      The list of operations permitted by the grant.

      - *(string) --*

    - **Constraints** *(dict) --*

      A list of key-value pairs that must be present in the encryption context of certain
      subsequent operations that the grant allows.

      - **EncryptionContextSubset** *(dict) --*

        A list of key-value pairs that must be included in the encryption context of the
        cryptographic operation request. The grant allows the cryptographic operation only when
        the encryption context in the request includes the key-value pairs specified in this
        constraint, although it can include additional key-value pairs.

        - *(string) --*

          - *(string) --*

      - **EncryptionContextEquals** *(dict) --*

        A list of key-value pairs that must match the encryption context in the cryptographic
        operation request. The grant allows the operation only when the encryption context in
        the request is the same as the encryption context specified in this constraint.

        - *(string) --*

          - *(string) --*
    """


_ClientListRetirableGrantsResponseTypeDef = TypedDict(
    "_ClientListRetirableGrantsResponseTypeDef",
    {
        "Grants": List[ClientListRetirableGrantsResponseGrantsTypeDef],
        "NextMarker": str,
        "Truncated": bool,
    },
    total=False,
)


class ClientListRetirableGrantsResponseTypeDef(
    _ClientListRetirableGrantsResponseTypeDef
):
    """
    Type definition for `ClientListRetirableGrants` `Response`

    - **Grants** *(list) --*

      A list of grants.

      - *(dict) --*

        Contains information about an entry in a list of grants.

        - **KeyId** *(string) --*

          The unique identifier for the customer master key (CMK) to which the grant applies.

        - **GrantId** *(string) --*

          The unique identifier for the grant.

        - **Name** *(string) --*

          The friendly name that identifies the grant. If a name was provided in the  CreateGrant
          request, that name is returned. Otherwise this value is null.

        - **CreationDate** *(datetime) --*

          The date and time when the grant was created.

        - **GranteePrincipal** *(string) --*

          The principal that receives the grant's permissions.

        - **RetiringPrincipal** *(string) --*

          The principal that can retire the grant.

        - **IssuingAccount** *(string) --*

          The AWS account under which the grant was issued.

        - **Operations** *(list) --*

          The list of operations permitted by the grant.

          - *(string) --*

        - **Constraints** *(dict) --*

          A list of key-value pairs that must be present in the encryption context of certain
          subsequent operations that the grant allows.

          - **EncryptionContextSubset** *(dict) --*

            A list of key-value pairs that must be included in the encryption context of the
            cryptographic operation request. The grant allows the cryptographic operation only when
            the encryption context in the request includes the key-value pairs specified in this
            constraint, although it can include additional key-value pairs.

            - *(string) --*

              - *(string) --*

          - **EncryptionContextEquals** *(dict) --*

            A list of key-value pairs that must match the encryption context in the cryptographic
            operation request. The grant allows the operation only when the encryption context in
            the request is the same as the encryption context specified in this constraint.

            - *(string) --*

              - *(string) --*

    - **NextMarker** *(string) --*

      When ``Truncated`` is true, this element is present and contains the value to use for the
      ``Marker`` parameter in a subsequent request.

    - **Truncated** *(boolean) --*

      A flag that indicates whether there are more items in the list. When this value is true, the
      list in this response is truncated. To get more items, pass the value of the ``NextMarker``
      element in thisresponse to the ``Marker`` parameter in a subsequent request.
    """


_ClientReEncryptResponseTypeDef = TypedDict(
    "_ClientReEncryptResponseTypeDef",
    {"CiphertextBlob": bytes, "SourceKeyId": str, "KeyId": str},
    total=False,
)


class ClientReEncryptResponseTypeDef(_ClientReEncryptResponseTypeDef):
    """
    Type definition for `ClientReEncrypt` `Response`

    - **CiphertextBlob** *(bytes) --*

      The reencrypted data. When you use the HTTP API or the AWS CLI, the value is Base64-encoded.
      Otherwise, it is not encoded.

    - **SourceKeyId** *(string) --*

      Unique identifier of the CMK used to originally encrypt the data.

    - **KeyId** *(string) --*

      Unique identifier of the CMK used to reencrypt the data.
    """


_ClientScheduleKeyDeletionResponseTypeDef = TypedDict(
    "_ClientScheduleKeyDeletionResponseTypeDef",
    {"KeyId": str, "DeletionDate": datetime},
    total=False,
)


class ClientScheduleKeyDeletionResponseTypeDef(
    _ClientScheduleKeyDeletionResponseTypeDef
):
    """
    Type definition for `ClientScheduleKeyDeletion` `Response`

    - **KeyId** *(string) --*

      The unique identifier of the customer master key (CMK) for which deletion is scheduled.

    - **DeletionDate** *(datetime) --*

      The date and time after which AWS KMS deletes the customer master key (CMK).
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"TagKey": str, "TagValue": str}
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both
    required, but tag values can be empty (null) strings.

    For information about the rules that apply to tag keys and tag values, see `User-Defined Tag
    Restrictions
    <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__
    in the *AWS Billing and Cost Management User Guide* .

    - **TagKey** *(string) --* **[REQUIRED]**

      The key of the tag.

    - **TagValue** *(string) --* **[REQUIRED]**

      The value of the tag.
    """


_ListAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAliasesPaginatePaginationConfigTypeDef(
    _ListAliasesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAliasesPaginate` `PaginationConfig`

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


_ListAliasesPaginateResponseAliasesTypeDef = TypedDict(
    "_ListAliasesPaginateResponseAliasesTypeDef",
    {"AliasName": str, "AliasArn": str, "TargetKeyId": str},
    total=False,
)


class ListAliasesPaginateResponseAliasesTypeDef(
    _ListAliasesPaginateResponseAliasesTypeDef
):
    """
    Type definition for `ListAliasesPaginateResponse` `Aliases`

    Contains information about an alias.

    - **AliasName** *(string) --*

      String that contains the alias. This value begins with ``alias/`` .

    - **AliasArn** *(string) --*

      String that contains the key ARN.

    - **TargetKeyId** *(string) --*

      String that contains the key identifier referred to by the alias.
    """


_ListAliasesPaginateResponseTypeDef = TypedDict(
    "_ListAliasesPaginateResponseTypeDef",
    {
        "Aliases": List[ListAliasesPaginateResponseAliasesTypeDef],
        "Truncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListAliasesPaginateResponseTypeDef(_ListAliasesPaginateResponseTypeDef):
    """
    Type definition for `ListAliasesPaginate` `Response`

    - **Aliases** *(list) --*

      A list of aliases.

      - *(dict) --*

        Contains information about an alias.

        - **AliasName** *(string) --*

          String that contains the alias. This value begins with ``alias/`` .

        - **AliasArn** *(string) --*

          String that contains the key ARN.

        - **TargetKeyId** *(string) --*

          String that contains the key identifier referred to by the alias.

    - **Truncated** *(boolean) --*

      A flag that indicates whether there are more items in the list. When this value is true, the
      list in this response is truncated. To get more items, pass the value of the ``NextMarker``
      element in thisresponse to the ``Marker`` parameter in a subsequent request.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListGrantsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListGrantsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListGrantsPaginatePaginationConfigTypeDef(
    _ListGrantsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListGrantsPaginate` `PaginationConfig`

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


_ListGrantsPaginateResponseGrantsConstraintsTypeDef = TypedDict(
    "_ListGrantsPaginateResponseGrantsConstraintsTypeDef",
    {
        "EncryptionContextSubset": Dict[str, str],
        "EncryptionContextEquals": Dict[str, str],
    },
    total=False,
)


class ListGrantsPaginateResponseGrantsConstraintsTypeDef(
    _ListGrantsPaginateResponseGrantsConstraintsTypeDef
):
    """
    Type definition for `ListGrantsPaginateResponseGrants` `Constraints`

    A list of key-value pairs that must be present in the encryption context of certain
    subsequent operations that the grant allows.

    - **EncryptionContextSubset** *(dict) --*

      A list of key-value pairs that must be included in the encryption context of the
      cryptographic operation request. The grant allows the cryptographic operation only when
      the encryption context in the request includes the key-value pairs specified in this
      constraint, although it can include additional key-value pairs.

      - *(string) --*

        - *(string) --*

    - **EncryptionContextEquals** *(dict) --*

      A list of key-value pairs that must match the encryption context in the cryptographic
      operation request. The grant allows the operation only when the encryption context in
      the request is the same as the encryption context specified in this constraint.

      - *(string) --*

        - *(string) --*
    """


_ListGrantsPaginateResponseGrantsTypeDef = TypedDict(
    "_ListGrantsPaginateResponseGrantsTypeDef",
    {
        "KeyId": str,
        "GrantId": str,
        "Name": str,
        "CreationDate": datetime,
        "GranteePrincipal": str,
        "RetiringPrincipal": str,
        "IssuingAccount": str,
        "Operations": List[str],
        "Constraints": ListGrantsPaginateResponseGrantsConstraintsTypeDef,
    },
    total=False,
)


class ListGrantsPaginateResponseGrantsTypeDef(_ListGrantsPaginateResponseGrantsTypeDef):
    """
    Type definition for `ListGrantsPaginateResponse` `Grants`

    Contains information about an entry in a list of grants.

    - **KeyId** *(string) --*

      The unique identifier for the customer master key (CMK) to which the grant applies.

    - **GrantId** *(string) --*

      The unique identifier for the grant.

    - **Name** *(string) --*

      The friendly name that identifies the grant. If a name was provided in the  CreateGrant
      request, that name is returned. Otherwise this value is null.

    - **CreationDate** *(datetime) --*

      The date and time when the grant was created.

    - **GranteePrincipal** *(string) --*

      The principal that receives the grant's permissions.

    - **RetiringPrincipal** *(string) --*

      The principal that can retire the grant.

    - **IssuingAccount** *(string) --*

      The AWS account under which the grant was issued.

    - **Operations** *(list) --*

      The list of operations permitted by the grant.

      - *(string) --*

    - **Constraints** *(dict) --*

      A list of key-value pairs that must be present in the encryption context of certain
      subsequent operations that the grant allows.

      - **EncryptionContextSubset** *(dict) --*

        A list of key-value pairs that must be included in the encryption context of the
        cryptographic operation request. The grant allows the cryptographic operation only when
        the encryption context in the request includes the key-value pairs specified in this
        constraint, although it can include additional key-value pairs.

        - *(string) --*

          - *(string) --*

      - **EncryptionContextEquals** *(dict) --*

        A list of key-value pairs that must match the encryption context in the cryptographic
        operation request. The grant allows the operation only when the encryption context in
        the request is the same as the encryption context specified in this constraint.

        - *(string) --*

          - *(string) --*
    """


_ListGrantsPaginateResponseTypeDef = TypedDict(
    "_ListGrantsPaginateResponseTypeDef",
    {
        "Grants": List[ListGrantsPaginateResponseGrantsTypeDef],
        "Truncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListGrantsPaginateResponseTypeDef(_ListGrantsPaginateResponseTypeDef):
    """
    Type definition for `ListGrantsPaginate` `Response`

    - **Grants** *(list) --*

      A list of grants.

      - *(dict) --*

        Contains information about an entry in a list of grants.

        - **KeyId** *(string) --*

          The unique identifier for the customer master key (CMK) to which the grant applies.

        - **GrantId** *(string) --*

          The unique identifier for the grant.

        - **Name** *(string) --*

          The friendly name that identifies the grant. If a name was provided in the  CreateGrant
          request, that name is returned. Otherwise this value is null.

        - **CreationDate** *(datetime) --*

          The date and time when the grant was created.

        - **GranteePrincipal** *(string) --*

          The principal that receives the grant's permissions.

        - **RetiringPrincipal** *(string) --*

          The principal that can retire the grant.

        - **IssuingAccount** *(string) --*

          The AWS account under which the grant was issued.

        - **Operations** *(list) --*

          The list of operations permitted by the grant.

          - *(string) --*

        - **Constraints** *(dict) --*

          A list of key-value pairs that must be present in the encryption context of certain
          subsequent operations that the grant allows.

          - **EncryptionContextSubset** *(dict) --*

            A list of key-value pairs that must be included in the encryption context of the
            cryptographic operation request. The grant allows the cryptographic operation only when
            the encryption context in the request includes the key-value pairs specified in this
            constraint, although it can include additional key-value pairs.

            - *(string) --*

              - *(string) --*

          - **EncryptionContextEquals** *(dict) --*

            A list of key-value pairs that must match the encryption context in the cryptographic
            operation request. The grant allows the operation only when the encryption context in
            the request is the same as the encryption context specified in this constraint.

            - *(string) --*

              - *(string) --*

    - **Truncated** *(boolean) --*

      A flag that indicates whether there are more items in the list. When this value is true, the
      list in this response is truncated. To get more items, pass the value of the ``NextMarker``
      element in thisresponse to the ``Marker`` parameter in a subsequent request.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListKeyPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListKeyPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListKeyPoliciesPaginatePaginationConfigTypeDef(
    _ListKeyPoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListKeyPoliciesPaginate` `PaginationConfig`

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


_ListKeyPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListKeyPoliciesPaginateResponseTypeDef",
    {"PolicyNames": List[str], "Truncated": bool, "NextToken": str},
    total=False,
)


class ListKeyPoliciesPaginateResponseTypeDef(_ListKeyPoliciesPaginateResponseTypeDef):
    """
    Type definition for `ListKeyPoliciesPaginate` `Response`

    - **PolicyNames** *(list) --*

      A list of key policy names. The only valid value is ``default`` .

      - *(string) --*

    - **Truncated** *(boolean) --*

      A flag that indicates whether there are more items in the list. When this value is true, the
      list in this response is truncated. To get more items, pass the value of the ``NextMarker``
      element in thisresponse to the ``Marker`` parameter in a subsequent request.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListKeysPaginatePaginationConfigTypeDef = TypedDict(
    "_ListKeysPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListKeysPaginatePaginationConfigTypeDef(_ListKeysPaginatePaginationConfigTypeDef):
    """
    Type definition for `ListKeysPaginate` `PaginationConfig`

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


_ListKeysPaginateResponseKeysTypeDef = TypedDict(
    "_ListKeysPaginateResponseKeysTypeDef", {"KeyId": str, "KeyArn": str}, total=False
)


class ListKeysPaginateResponseKeysTypeDef(_ListKeysPaginateResponseKeysTypeDef):
    """
    Type definition for `ListKeysPaginateResponse` `Keys`

    Contains information about each entry in the key list.

    - **KeyId** *(string) --*

      Unique identifier of the key.

    - **KeyArn** *(string) --*

      ARN of the key.
    """


_ListKeysPaginateResponseTypeDef = TypedDict(
    "_ListKeysPaginateResponseTypeDef",
    {
        "Keys": List[ListKeysPaginateResponseKeysTypeDef],
        "Truncated": bool,
        "NextToken": str,
    },
    total=False,
)


class ListKeysPaginateResponseTypeDef(_ListKeysPaginateResponseTypeDef):
    """
    Type definition for `ListKeysPaginate` `Response`

    - **Keys** *(list) --*

      A list of customer master keys (CMKs).

      - *(dict) --*

        Contains information about each entry in the key list.

        - **KeyId** *(string) --*

          Unique identifier of the key.

        - **KeyArn** *(string) --*

          ARN of the key.

    - **Truncated** *(boolean) --*

      A flag that indicates whether there are more items in the list. When this value is true, the
      list in this response is truncated. To get more items, pass the value of the ``NextMarker``
      element in thisresponse to the ``Marker`` parameter in a subsequent request.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """

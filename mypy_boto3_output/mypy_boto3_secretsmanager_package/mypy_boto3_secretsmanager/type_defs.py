"Main interface for secretsmanager type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCancelRotateSecretResponseTypeDef",
    "ClientCreateSecretResponseTypeDef",
    "ClientCreateSecretTagsTypeDef",
    "ClientDeleteResourcePolicyResponseTypeDef",
    "ClientDeleteSecretResponseTypeDef",
    "ClientDescribeSecretResponseRotationRulesTypeDef",
    "ClientDescribeSecretResponseTagsTypeDef",
    "ClientDescribeSecretResponseTypeDef",
    "ClientGetRandomPasswordResponseTypeDef",
    "ClientGetResourcePolicyResponseTypeDef",
    "ClientGetSecretValueResponseTypeDef",
    "ClientListSecretVersionIdsResponseVersionsTypeDef",
    "ClientListSecretVersionIdsResponseTypeDef",
    "ClientListSecretsResponseSecretListRotationRulesTypeDef",
    "ClientListSecretsResponseSecretListTagsTypeDef",
    "ClientListSecretsResponseSecretListTypeDef",
    "ClientListSecretsResponseTypeDef",
    "ClientPutResourcePolicyResponseTypeDef",
    "ClientPutSecretValueResponseTypeDef",
    "ClientRestoreSecretResponseTypeDef",
    "ClientRotateSecretResponseTypeDef",
    "ClientRotateSecretRotationRulesTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateSecretResponseTypeDef",
    "ClientUpdateSecretVersionStageResponseTypeDef",
    "ListSecretsPaginatePaginationConfigTypeDef",
    "ListSecretsPaginateResponseSecretListRotationRulesTypeDef",
    "ListSecretsPaginateResponseSecretListTagsTypeDef",
    "ListSecretsPaginateResponseSecretListTypeDef",
    "ListSecretsPaginateResponseTypeDef",
)


_ClientCancelRotateSecretResponseTypeDef = TypedDict(
    "_ClientCancelRotateSecretResponseTypeDef",
    {"ARN": str, "Name": str, "VersionId": str},
    total=False,
)


class ClientCancelRotateSecretResponseTypeDef(_ClientCancelRotateSecretResponseTypeDef):
    """
    Type definition for `ClientCancelRotateSecret` `Response`

    - **ARN** *(string) --*

      The ARN of the secret for which rotation was canceled.

    - **Name** *(string) --*

      The friendly name of the secret for which rotation was canceled.

    - **VersionId** *(string) --*

      The unique identifier of the version of the secret that was created during the rotation. This
      version might not be complete, and should be evaluated for possible deletion. At the very
      least, you should remove the ``VersionStage`` value ``AWSPENDING`` to enable this version to
      be deleted. Failing to clean up a cancelled rotation can block you from successfully starting
      future rotations.
    """


_ClientCreateSecretResponseTypeDef = TypedDict(
    "_ClientCreateSecretResponseTypeDef",
    {"ARN": str, "Name": str, "VersionId": str},
    total=False,
)


class ClientCreateSecretResponseTypeDef(_ClientCreateSecretResponseTypeDef):
    """
    Type definition for `ClientCreateSecret` `Response`

    - **ARN** *(string) --*

      The Amazon Resource Name (ARN) of the secret that you just created.

      .. note::

        Secrets Manager automatically adds several random characters to the name at the end of the
        ARN when you initially create a secret. This affects only the ARN and not the actual
        friendly name. This ensures that if you create a new secret with the same name as an old
        secret that you previously deleted, then users with access to the old secret *don't*
        automatically get access to the new secret because the ARNs are different.

    - **Name** *(string) --*

      The friendly name of the secret that you just created.

    - **VersionId** *(string) --*

      The unique identifier that's associated with the version of the secret you just created.
    """


_ClientCreateSecretTagsTypeDef = TypedDict(
    "_ClientCreateSecretTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateSecretTagsTypeDef(_ClientCreateSecretTagsTypeDef):
    """
    Type definition for `ClientCreateSecret` `Tags`

    A structure that contains information about a tag.

    - **Key** *(string) --*

      The key identifier, or name, of the tag.

    - **Value** *(string) --*

      The string value that's associated with the key of the tag.
    """


_ClientDeleteResourcePolicyResponseTypeDef = TypedDict(
    "_ClientDeleteResourcePolicyResponseTypeDef", {"ARN": str, "Name": str}, total=False
)


class ClientDeleteResourcePolicyResponseTypeDef(
    _ClientDeleteResourcePolicyResponseTypeDef
):
    """
    Type definition for `ClientDeleteResourcePolicy` `Response`

    - **ARN** *(string) --*

      The ARN of the secret that the resource-based policy was deleted for.

    - **Name** *(string) --*

      The friendly name of the secret that the resource-based policy was deleted for.
    """


_ClientDeleteSecretResponseTypeDef = TypedDict(
    "_ClientDeleteSecretResponseTypeDef",
    {"ARN": str, "Name": str, "DeletionDate": datetime},
    total=False,
)


class ClientDeleteSecretResponseTypeDef(_ClientDeleteSecretResponseTypeDef):
    """
    Type definition for `ClientDeleteSecret` `Response`

    - **ARN** *(string) --*

      The ARN of the secret that is now scheduled for deletion.

    - **Name** *(string) --*

      The friendly name of the secret that is now scheduled for deletion.

    - **DeletionDate** *(datetime) --*

      The date and time after which this secret can be deleted by Secrets Manager and can no longer
      be restored. This value is the date and time of the delete request plus the number of days
      specified in ``RecoveryWindowInDays`` .
    """


_ClientDescribeSecretResponseRotationRulesTypeDef = TypedDict(
    "_ClientDescribeSecretResponseRotationRulesTypeDef",
    {"AutomaticallyAfterDays": int},
    total=False,
)


class ClientDescribeSecretResponseRotationRulesTypeDef(
    _ClientDescribeSecretResponseRotationRulesTypeDef
):
    """
    Type definition for `ClientDescribeSecretResponse` `RotationRules`

    A structure that contains the rotation configuration for this secret.

    - **AutomaticallyAfterDays** *(integer) --*

      Specifies the number of days between automatic scheduled rotations of the secret.

      Secrets Manager schedules the next rotation when the previous one is complete. Secrets
      Manager schedules the date by adding the rotation interval (number of days) to the actual
      date of the last rotation. The service chooses the hour within that 24-hour date window
      randomly. The minute is also chosen somewhat randomly, but weighted towards the top of the
      hour and influenced by a variety of factors that help distribute load.
    """


_ClientDescribeSecretResponseTagsTypeDef = TypedDict(
    "_ClientDescribeSecretResponseTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientDescribeSecretResponseTagsTypeDef(_ClientDescribeSecretResponseTagsTypeDef):
    """
    Type definition for `ClientDescribeSecretResponse` `Tags`

    A structure that contains information about a tag.

    - **Key** *(string) --*

      The key identifier, or name, of the tag.

    - **Value** *(string) --*

      The string value that's associated with the key of the tag.
    """


_ClientDescribeSecretResponseTypeDef = TypedDict(
    "_ClientDescribeSecretResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "Description": str,
        "KmsKeyId": str,
        "RotationEnabled": bool,
        "RotationLambdaARN": str,
        "RotationRules": ClientDescribeSecretResponseRotationRulesTypeDef,
        "LastRotatedDate": datetime,
        "LastChangedDate": datetime,
        "LastAccessedDate": datetime,
        "DeletedDate": datetime,
        "Tags": List[ClientDescribeSecretResponseTagsTypeDef],
        "VersionIdsToStages": Dict[str, List[str]],
        "OwningService": str,
    },
    total=False,
)


class ClientDescribeSecretResponseTypeDef(_ClientDescribeSecretResponseTypeDef):
    """
    Type definition for `ClientDescribeSecret` `Response`

    - **ARN** *(string) --*

      The ARN of the secret.

    - **Name** *(string) --*

      The user-provided friendly name of the secret.

    - **Description** *(string) --*

      The user-provided description of the secret.

    - **KmsKeyId** *(string) --*

      The ARN or alias of the AWS KMS customer master key (CMK) that's used to encrypt the
      ``SecretString`` or ``SecretBinary`` fields in each version of the secret. If you don't
      provide a key, then Secrets Manager defaults to encrypting the secret fields with the default
      AWS KMS CMK (the one named ``awssecretsmanager`` ) for this account.

    - **RotationEnabled** *(boolean) --*

      Specifies whether automatic rotation is enabled for this secret.

      To enable rotation, use  RotateSecret with ``AutomaticallyRotateAfterDays`` set to a value
      greater than 0. To disable rotation, use  CancelRotateSecret .

    - **RotationLambdaARN** *(string) --*

      The ARN of a Lambda function that's invoked by Secrets Manager to rotate the secret either
      automatically per the schedule or manually by a call to ``RotateSecret`` .

    - **RotationRules** *(dict) --*

      A structure that contains the rotation configuration for this secret.

      - **AutomaticallyAfterDays** *(integer) --*

        Specifies the number of days between automatic scheduled rotations of the secret.

        Secrets Manager schedules the next rotation when the previous one is complete. Secrets
        Manager schedules the date by adding the rotation interval (number of days) to the actual
        date of the last rotation. The service chooses the hour within that 24-hour date window
        randomly. The minute is also chosen somewhat randomly, but weighted towards the top of the
        hour and influenced by a variety of factors that help distribute load.

    - **LastRotatedDate** *(datetime) --*

      The most recent date and time that the Secrets Manager rotation process was successfully
      completed. This value is null if the secret has never rotated.

    - **LastChangedDate** *(datetime) --*

      The last date and time that this secret was modified in any way.

    - **LastAccessedDate** *(datetime) --*

      The last date that this secret was accessed. This value is truncated to midnight of the date
      and therefore shows only the date, not the time.

    - **DeletedDate** *(datetime) --*

      This value exists if the secret is scheduled for deletion. Some time after the specified date
      and time, Secrets Manager deletes the secret and all of its versions.

      If a secret is scheduled for deletion, then its details, including the encrypted secret
      information, is not accessible. To cancel a scheduled deletion and restore access, use
      RestoreSecret .

    - **Tags** *(list) --*

      The list of user-defined tags that are associated with the secret. To add tags to a secret,
      use  TagResource . To remove tags, use  UntagResource .

      - *(dict) --*

        A structure that contains information about a tag.

        - **Key** *(string) --*

          The key identifier, or name, of the tag.

        - **Value** *(string) --*

          The string value that's associated with the key of the tag.

    - **VersionIdsToStages** *(dict) --*

      A list of all of the currently assigned ``VersionStage`` staging labels and the ``VersionId``
      that each is attached to. Staging labels are used to keep track of the different versions
      during the rotation process.

      .. note::

        A version that does not have any staging labels attached is considered deprecated and
        subject to deletion. Such versions are not included in this list.

      - *(string) --*

        - *(list) --*

          - *(string) --*

    - **OwningService** *(string) --*
    """


_ClientGetRandomPasswordResponseTypeDef = TypedDict(
    "_ClientGetRandomPasswordResponseTypeDef", {"RandomPassword": str}, total=False
)


class ClientGetRandomPasswordResponseTypeDef(_ClientGetRandomPasswordResponseTypeDef):
    """
    Type definition for `ClientGetRandomPassword` `Response`

    - **RandomPassword** *(string) --*

      A string with the generated password.
    """


_ClientGetResourcePolicyResponseTypeDef = TypedDict(
    "_ClientGetResourcePolicyResponseTypeDef",
    {"ARN": str, "Name": str, "ResourcePolicy": str},
    total=False,
)


class ClientGetResourcePolicyResponseTypeDef(_ClientGetResourcePolicyResponseTypeDef):
    """
    Type definition for `ClientGetResourcePolicy` `Response`

    - **ARN** *(string) --*

      The ARN of the secret that the resource-based policy was retrieved for.

    - **Name** *(string) --*

      The friendly name of the secret that the resource-based policy was retrieved for.

    - **ResourcePolicy** *(string) --*

      A JSON-formatted string that describes the permissions that are associated with the attached
      secret. These permissions are combined with any permissions that are associated with the user
      or role that attempts to access this secret. The combined permissions specify who can access
      the secret and what actions they can perform. For more information, see `Authentication and
      Access Control for AWS Secrets Manager
      <http://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html>`__ in the
      *AWS Secrets Manager User Guide* .
    """


_ClientGetSecretValueResponseTypeDef = TypedDict(
    "_ClientGetSecretValueResponseTypeDef",
    {
        "ARN": str,
        "Name": str,
        "VersionId": str,
        "SecretBinary": bytes,
        "SecretString": str,
        "VersionStages": List[str],
        "CreatedDate": datetime,
    },
    total=False,
)


class ClientGetSecretValueResponseTypeDef(_ClientGetSecretValueResponseTypeDef):
    """
    Type definition for `ClientGetSecretValue` `Response`

    - **ARN** *(string) --*

      The ARN of the secret.

    - **Name** *(string) --*

      The friendly name of the secret.

    - **VersionId** *(string) --*

      The unique identifier of this version of the secret.

    - **SecretBinary** *(bytes) --*

      The decrypted part of the protected secret information that was originally provided as binary
      data in the form of a byte array. The response parameter represents the binary data as a
      `base64-encoded <https://tools.ietf.org/html/rfc4648#section-4>`__ string.

      This parameter is not used if the secret is created by the Secrets Manager console.

      If you store custom information in this field of the secret, then you must code your Lambda
      rotation function to parse and interpret whatever you store in the ``SecretString`` or
      ``SecretBinary`` fields.

    - **SecretString** *(string) --*

      The decrypted part of the protected secret information that was originally provided as a
      string.

      If you create this secret by using the Secrets Manager console then only the ``SecretString``
      parameter contains data. Secrets Manager stores the information as a JSON structure of
      key/value pairs that the Lambda rotation function knows how to parse.

      If you store custom information in the secret by using the  CreateSecret ,  UpdateSecret , or
       PutSecretValue API operations instead of the Secrets Manager console, or by using the
       **Other secret type** in the console, then you must code your Lambda rotation function to
       parse and interpret those values.

    - **VersionStages** *(list) --*

      A list of all of the staging labels currently attached to this version of the secret.

      - *(string) --*

    - **CreatedDate** *(datetime) --*

      The date and time that this version of the secret was created.
    """


_ClientListSecretVersionIdsResponseVersionsTypeDef = TypedDict(
    "_ClientListSecretVersionIdsResponseVersionsTypeDef",
    {
        "VersionId": str,
        "VersionStages": List[str],
        "LastAccessedDate": datetime,
        "CreatedDate": datetime,
    },
    total=False,
)


class ClientListSecretVersionIdsResponseVersionsTypeDef(
    _ClientListSecretVersionIdsResponseVersionsTypeDef
):
    """
    Type definition for `ClientListSecretVersionIdsResponse` `Versions`

    A structure that contains information about one version of a secret.

    - **VersionId** *(string) --*

      The unique version identifier of this version of the secret.

    - **VersionStages** *(list) --*

      An array of staging labels that are currently associated with this version of the secret.

      - *(string) --*

    - **LastAccessedDate** *(datetime) --*

      The date that this version of the secret was last accessed. Note that the resolution of
      this field is at the date level and does not include the time.

    - **CreatedDate** *(datetime) --*

      The date and time this version of the secret was created.
    """


_ClientListSecretVersionIdsResponseTypeDef = TypedDict(
    "_ClientListSecretVersionIdsResponseTypeDef",
    {
        "Versions": List[ClientListSecretVersionIdsResponseVersionsTypeDef],
        "NextToken": str,
        "ARN": str,
        "Name": str,
    },
    total=False,
)


class ClientListSecretVersionIdsResponseTypeDef(
    _ClientListSecretVersionIdsResponseTypeDef
):
    """
    Type definition for `ClientListSecretVersionIds` `Response`

    - **Versions** *(list) --*

      The list of the currently available versions of the specified secret.

      - *(dict) --*

        A structure that contains information about one version of a secret.

        - **VersionId** *(string) --*

          The unique version identifier of this version of the secret.

        - **VersionStages** *(list) --*

          An array of staging labels that are currently associated with this version of the secret.

          - *(string) --*

        - **LastAccessedDate** *(datetime) --*

          The date that this version of the secret was last accessed. Note that the resolution of
          this field is at the date level and does not include the time.

        - **CreatedDate** *(datetime) --*

          The date and time this version of the secret was created.

    - **NextToken** *(string) --*

      If present in the response, this value indicates that there's more output available than
      what's included in the current response. This can occur even when the response includes no
      values at all, such as when you ask for a filtered view of a very long list. Use this value
      in the ``NextToken`` request parameter in a subsequent call to the operation to continue
      processing and get the next part of the output. You should repeat this until the
      ``NextToken`` response element comes back empty (as ``null`` ).

    - **ARN** *(string) --*

      The Amazon Resource Name (ARN) for the secret.

      .. note::

        Secrets Manager automatically adds several random characters to the name at the end of the
        ARN when you initially create a secret. This affects only the ARN and not the actual
        friendly name. This ensures that if you create a new secret with the same name as an old
        secret that you previously deleted, then users with access to the old secret *don't*
        automatically get access to the new secret because the ARNs are different.

    - **Name** *(string) --*

      The friendly name of the secret.
    """


_ClientListSecretsResponseSecretListRotationRulesTypeDef = TypedDict(
    "_ClientListSecretsResponseSecretListRotationRulesTypeDef",
    {"AutomaticallyAfterDays": int},
    total=False,
)


class ClientListSecretsResponseSecretListRotationRulesTypeDef(
    _ClientListSecretsResponseSecretListRotationRulesTypeDef
):
    """
    Type definition for `ClientListSecretsResponseSecretList` `RotationRules`

    A structure that defines the rotation configuration for the secret.

    - **AutomaticallyAfterDays** *(integer) --*

      Specifies the number of days between automatic scheduled rotations of the secret.

      Secrets Manager schedules the next rotation when the previous one is complete. Secrets
      Manager schedules the date by adding the rotation interval (number of days) to the
      actual date of the last rotation. The service chooses the hour within that 24-hour date
      window randomly. The minute is also chosen somewhat randomly, but weighted towards the
      top of the hour and influenced by a variety of factors that help distribute load.
    """


_ClientListSecretsResponseSecretListTagsTypeDef = TypedDict(
    "_ClientListSecretsResponseSecretListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListSecretsResponseSecretListTagsTypeDef(
    _ClientListSecretsResponseSecretListTagsTypeDef
):
    """
    Type definition for `ClientListSecretsResponseSecretList` `Tags`

    A structure that contains information about a tag.

    - **Key** *(string) --*

      The key identifier, or name, of the tag.

    - **Value** *(string) --*

      The string value that's associated with the key of the tag.
    """


_ClientListSecretsResponseSecretListTypeDef = TypedDict(
    "_ClientListSecretsResponseSecretListTypeDef",
    {
        "ARN": str,
        "Name": str,
        "Description": str,
        "KmsKeyId": str,
        "RotationEnabled": bool,
        "RotationLambdaARN": str,
        "RotationRules": ClientListSecretsResponseSecretListRotationRulesTypeDef,
        "LastRotatedDate": datetime,
        "LastChangedDate": datetime,
        "LastAccessedDate": datetime,
        "DeletedDate": datetime,
        "Tags": List[ClientListSecretsResponseSecretListTagsTypeDef],
        "SecretVersionsToStages": Dict[str, List[str]],
        "OwningService": str,
    },
    total=False,
)


class ClientListSecretsResponseSecretListTypeDef(
    _ClientListSecretsResponseSecretListTypeDef
):
    """
    Type definition for `ClientListSecretsResponse` `SecretList`

    A structure that contains the details about a secret. It does not include the encrypted
    ``SecretString`` and ``SecretBinary`` values. To get those values, use the  GetSecretValue
    operation.

    - **ARN** *(string) --*

      The Amazon Resource Name (ARN) of the secret.

      For more information about ARNs in Secrets Manager, see `Policy Resources
      <https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#iam-resources>`__
      in the *AWS Secrets Manager User Guide* .

    - **Name** *(string) --*

      The friendly name of the secret. You can use forward slashes in the name to represent a
      path hierarchy. For example, ``/prod/databases/dbserver1`` could represent the secret for
      a server named ``dbserver1`` in the folder ``databases`` in the folder ``prod`` .

    - **Description** *(string) --*

      The user-provided description of the secret.

    - **KmsKeyId** *(string) --*

      The ARN or alias of the AWS KMS customer master key (CMK) that's used to encrypt the
      ``SecretString`` and ``SecretBinary`` fields in each version of the secret. If you don't
      provide a key, then Secrets Manager defaults to encrypting the secret fields with the
      default KMS CMK (the one named ``awssecretsmanager`` ) for this account.

    - **RotationEnabled** *(boolean) --*

      Indicated whether automatic, scheduled rotation is enabled for this secret.

    - **RotationLambdaARN** *(string) --*

      The ARN of an AWS Lambda function that's invoked by Secrets Manager to rotate and expire
      the secret either automatically per the schedule or manually by a call to  RotateSecret .

    - **RotationRules** *(dict) --*

      A structure that defines the rotation configuration for the secret.

      - **AutomaticallyAfterDays** *(integer) --*

        Specifies the number of days between automatic scheduled rotations of the secret.

        Secrets Manager schedules the next rotation when the previous one is complete. Secrets
        Manager schedules the date by adding the rotation interval (number of days) to the
        actual date of the last rotation. The service chooses the hour within that 24-hour date
        window randomly. The minute is also chosen somewhat randomly, but weighted towards the
        top of the hour and influenced by a variety of factors that help distribute load.

    - **LastRotatedDate** *(datetime) --*

      The last date and time that the rotation process for this secret was invoked.

    - **LastChangedDate** *(datetime) --*

      The last date and time that this secret was modified in any way.

    - **LastAccessedDate** *(datetime) --*

      The last date that this secret was accessed. This value is truncated to midnight of the
      date and therefore shows only the date, not the time.

    - **DeletedDate** *(datetime) --*

      The date and time on which this secret was deleted. Not present on active secrets. The
      secret can be recovered until the number of days in the recovery window has passed, as
      specified in the ``RecoveryWindowInDays`` parameter of the  DeleteSecret operation.

    - **Tags** *(list) --*

      The list of user-defined tags that are associated with the secret. To add tags to a
      secret, use  TagResource . To remove tags, use  UntagResource .

      - *(dict) --*

        A structure that contains information about a tag.

        - **Key** *(string) --*

          The key identifier, or name, of the tag.

        - **Value** *(string) --*

          The string value that's associated with the key of the tag.

    - **SecretVersionsToStages** *(dict) --*

      A list of all of the currently assigned ``SecretVersionStage`` staging labels and the
      ``SecretVersionId`` that each is attached to. Staging labels are used to keep track of
      the different versions during the rotation process.

      .. note::

        A version that does not have any ``SecretVersionStage`` is considered deprecated and
        subject to deletion. Such versions are not included in this list.

      - *(string) --*

        - *(list) --*

          - *(string) --*

    - **OwningService** *(string) --*
    """


_ClientListSecretsResponseTypeDef = TypedDict(
    "_ClientListSecretsResponseTypeDef",
    {"SecretList": List[ClientListSecretsResponseSecretListTypeDef], "NextToken": str},
    total=False,
)


class ClientListSecretsResponseTypeDef(_ClientListSecretsResponseTypeDef):
    """
    Type definition for `ClientListSecrets` `Response`

    - **SecretList** *(list) --*

      A list of the secrets in the account.

      - *(dict) --*

        A structure that contains the details about a secret. It does not include the encrypted
        ``SecretString`` and ``SecretBinary`` values. To get those values, use the  GetSecretValue
        operation.

        - **ARN** *(string) --*

          The Amazon Resource Name (ARN) of the secret.

          For more information about ARNs in Secrets Manager, see `Policy Resources
          <https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#iam-resources>`__
          in the *AWS Secrets Manager User Guide* .

        - **Name** *(string) --*

          The friendly name of the secret. You can use forward slashes in the name to represent a
          path hierarchy. For example, ``/prod/databases/dbserver1`` could represent the secret for
          a server named ``dbserver1`` in the folder ``databases`` in the folder ``prod`` .

        - **Description** *(string) --*

          The user-provided description of the secret.

        - **KmsKeyId** *(string) --*

          The ARN or alias of the AWS KMS customer master key (CMK) that's used to encrypt the
          ``SecretString`` and ``SecretBinary`` fields in each version of the secret. If you don't
          provide a key, then Secrets Manager defaults to encrypting the secret fields with the
          default KMS CMK (the one named ``awssecretsmanager`` ) for this account.

        - **RotationEnabled** *(boolean) --*

          Indicated whether automatic, scheduled rotation is enabled for this secret.

        - **RotationLambdaARN** *(string) --*

          The ARN of an AWS Lambda function that's invoked by Secrets Manager to rotate and expire
          the secret either automatically per the schedule or manually by a call to  RotateSecret .

        - **RotationRules** *(dict) --*

          A structure that defines the rotation configuration for the secret.

          - **AutomaticallyAfterDays** *(integer) --*

            Specifies the number of days between automatic scheduled rotations of the secret.

            Secrets Manager schedules the next rotation when the previous one is complete. Secrets
            Manager schedules the date by adding the rotation interval (number of days) to the
            actual date of the last rotation. The service chooses the hour within that 24-hour date
            window randomly. The minute is also chosen somewhat randomly, but weighted towards the
            top of the hour and influenced by a variety of factors that help distribute load.

        - **LastRotatedDate** *(datetime) --*

          The last date and time that the rotation process for this secret was invoked.

        - **LastChangedDate** *(datetime) --*

          The last date and time that this secret was modified in any way.

        - **LastAccessedDate** *(datetime) --*

          The last date that this secret was accessed. This value is truncated to midnight of the
          date and therefore shows only the date, not the time.

        - **DeletedDate** *(datetime) --*

          The date and time on which this secret was deleted. Not present on active secrets. The
          secret can be recovered until the number of days in the recovery window has passed, as
          specified in the ``RecoveryWindowInDays`` parameter of the  DeleteSecret operation.

        - **Tags** *(list) --*

          The list of user-defined tags that are associated with the secret. To add tags to a
          secret, use  TagResource . To remove tags, use  UntagResource .

          - *(dict) --*

            A structure that contains information about a tag.

            - **Key** *(string) --*

              The key identifier, or name, of the tag.

            - **Value** *(string) --*

              The string value that's associated with the key of the tag.

        - **SecretVersionsToStages** *(dict) --*

          A list of all of the currently assigned ``SecretVersionStage`` staging labels and the
          ``SecretVersionId`` that each is attached to. Staging labels are used to keep track of
          the different versions during the rotation process.

          .. note::

            A version that does not have any ``SecretVersionStage`` is considered deprecated and
            subject to deletion. Such versions are not included in this list.

          - *(string) --*

            - *(list) --*

              - *(string) --*

        - **OwningService** *(string) --*

    - **NextToken** *(string) --*

      If present in the response, this value indicates that there's more output available than
      what's included in the current response. This can occur even when the response includes no
      values at all, such as when you ask for a filtered view of a very long list. Use this value
      in the ``NextToken`` request parameter in a subsequent call to the operation to continue
      processing and get the next part of the output. You should repeat this until the
      ``NextToken`` response element comes back empty (as ``null`` ).
    """


_ClientPutResourcePolicyResponseTypeDef = TypedDict(
    "_ClientPutResourcePolicyResponseTypeDef", {"ARN": str, "Name": str}, total=False
)


class ClientPutResourcePolicyResponseTypeDef(_ClientPutResourcePolicyResponseTypeDef):
    """
    Type definition for `ClientPutResourcePolicy` `Response`

    - **ARN** *(string) --*

      The ARN of the secret that the resource-based policy was retrieved for.

    - **Name** *(string) --*

      The friendly name of the secret that the resource-based policy was retrieved for.
    """


_ClientPutSecretValueResponseTypeDef = TypedDict(
    "_ClientPutSecretValueResponseTypeDef",
    {"ARN": str, "Name": str, "VersionId": str, "VersionStages": List[str]},
    total=False,
)


class ClientPutSecretValueResponseTypeDef(_ClientPutSecretValueResponseTypeDef):
    """
    Type definition for `ClientPutSecretValue` `Response`

    - **ARN** *(string) --*

      The Amazon Resource Name (ARN) for the secret for which you just created a version.

    - **Name** *(string) --*

      The friendly name of the secret for which you just created or updated a version.

    - **VersionId** *(string) --*

      The unique identifier of the version of the secret you just created or updated.

    - **VersionStages** *(list) --*

      The list of staging labels that are currently attached to this version of the secret. Staging
      labels are used to track a version as it progresses through the secret rotation process.

      - *(string) --*
    """


_ClientRestoreSecretResponseTypeDef = TypedDict(
    "_ClientRestoreSecretResponseTypeDef", {"ARN": str, "Name": str}, total=False
)


class ClientRestoreSecretResponseTypeDef(_ClientRestoreSecretResponseTypeDef):
    """
    Type definition for `ClientRestoreSecret` `Response`

    - **ARN** *(string) --*

      The ARN of the secret that was restored.

    - **Name** *(string) --*

      The friendly name of the secret that was restored.
    """


_ClientRotateSecretResponseTypeDef = TypedDict(
    "_ClientRotateSecretResponseTypeDef",
    {"ARN": str, "Name": str, "VersionId": str},
    total=False,
)


class ClientRotateSecretResponseTypeDef(_ClientRotateSecretResponseTypeDef):
    """
    Type definition for `ClientRotateSecret` `Response`

    - **ARN** *(string) --*

      The ARN of the secret.

    - **Name** *(string) --*

      The friendly name of the secret.

    - **VersionId** *(string) --*

      The ID of the new version of the secret created by the rotation started by this request.
    """


_ClientRotateSecretRotationRulesTypeDef = TypedDict(
    "_ClientRotateSecretRotationRulesTypeDef",
    {"AutomaticallyAfterDays": int},
    total=False,
)


class ClientRotateSecretRotationRulesTypeDef(_ClientRotateSecretRotationRulesTypeDef):
    """
    Type definition for `ClientRotateSecret` `RotationRules`

    A structure that defines the rotation configuration for this secret.

    - **AutomaticallyAfterDays** *(integer) --*

      Specifies the number of days between automatic scheduled rotations of the secret.

      Secrets Manager schedules the next rotation when the previous one is complete. Secrets Manager
      schedules the date by adding the rotation interval (number of days) to the actual date of the
      last rotation. The service chooses the hour within that 24-hour date window randomly. The
      minute is also chosen somewhat randomly, but weighted towards the top of the hour and
      influenced by a variety of factors that help distribute load.
    """


_ClientTagResourceTagsTypeDef = TypedDict(
    "_ClientTagResourceTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourceTagsTypeDef(_ClientTagResourceTagsTypeDef):
    """
    Type definition for `ClientTagResource` `Tags`

    A structure that contains information about a tag.

    - **Key** *(string) --*

      The key identifier, or name, of the tag.

    - **Value** *(string) --*

      The string value that's associated with the key of the tag.
    """


_ClientUpdateSecretResponseTypeDef = TypedDict(
    "_ClientUpdateSecretResponseTypeDef",
    {"ARN": str, "Name": str, "VersionId": str},
    total=False,
)


class ClientUpdateSecretResponseTypeDef(_ClientUpdateSecretResponseTypeDef):
    """
    Type definition for `ClientUpdateSecret` `Response`

    - **ARN** *(string) --*

      The ARN of the secret that was updated.

      .. note::

        Secrets Manager automatically adds several random characters to the name at the end of the
        ARN when you initially create a secret. This affects only the ARN and not the actual
        friendly name. This ensures that if you create a new secret with the same name as an old
        secret that you previously deleted, then users with access to the old secret *don't*
        automatically get access to the new secret because the ARNs are different.

    - **Name** *(string) --*

      The friendly name of the secret that was updated.

    - **VersionId** *(string) --*

      If a new version of the secret was created by this operation, then ``VersionId`` contains the
      unique identifier of the new version.
    """


_ClientUpdateSecretVersionStageResponseTypeDef = TypedDict(
    "_ClientUpdateSecretVersionStageResponseTypeDef",
    {"ARN": str, "Name": str},
    total=False,
)


class ClientUpdateSecretVersionStageResponseTypeDef(
    _ClientUpdateSecretVersionStageResponseTypeDef
):
    """
    Type definition for `ClientUpdateSecretVersionStage` `Response`

    - **ARN** *(string) --*

      The ARN of the secret with the staging label that was modified.

    - **Name** *(string) --*

      The friendly name of the secret with the staging label that was modified.
    """


_ListSecretsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSecretsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSecretsPaginatePaginationConfigTypeDef(
    _ListSecretsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSecretsPaginate` `PaginationConfig`

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


_ListSecretsPaginateResponseSecretListRotationRulesTypeDef = TypedDict(
    "_ListSecretsPaginateResponseSecretListRotationRulesTypeDef",
    {"AutomaticallyAfterDays": int},
    total=False,
)


class ListSecretsPaginateResponseSecretListRotationRulesTypeDef(
    _ListSecretsPaginateResponseSecretListRotationRulesTypeDef
):
    """
    Type definition for `ListSecretsPaginateResponseSecretList` `RotationRules`

    A structure that defines the rotation configuration for the secret.

    - **AutomaticallyAfterDays** *(integer) --*

      Specifies the number of days between automatic scheduled rotations of the secret.

      Secrets Manager schedules the next rotation when the previous one is complete. Secrets
      Manager schedules the date by adding the rotation interval (number of days) to the
      actual date of the last rotation. The service chooses the hour within that 24-hour date
      window randomly. The minute is also chosen somewhat randomly, but weighted towards the
      top of the hour and influenced by a variety of factors that help distribute load.
    """


_ListSecretsPaginateResponseSecretListTagsTypeDef = TypedDict(
    "_ListSecretsPaginateResponseSecretListTagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListSecretsPaginateResponseSecretListTagsTypeDef(
    _ListSecretsPaginateResponseSecretListTagsTypeDef
):
    """
    Type definition for `ListSecretsPaginateResponseSecretList` `Tags`

    A structure that contains information about a tag.

    - **Key** *(string) --*

      The key identifier, or name, of the tag.

    - **Value** *(string) --*

      The string value that's associated with the key of the tag.
    """


_ListSecretsPaginateResponseSecretListTypeDef = TypedDict(
    "_ListSecretsPaginateResponseSecretListTypeDef",
    {
        "ARN": str,
        "Name": str,
        "Description": str,
        "KmsKeyId": str,
        "RotationEnabled": bool,
        "RotationLambdaARN": str,
        "RotationRules": ListSecretsPaginateResponseSecretListRotationRulesTypeDef,
        "LastRotatedDate": datetime,
        "LastChangedDate": datetime,
        "LastAccessedDate": datetime,
        "DeletedDate": datetime,
        "Tags": List[ListSecretsPaginateResponseSecretListTagsTypeDef],
        "SecretVersionsToStages": Dict[str, List[str]],
        "OwningService": str,
    },
    total=False,
)


class ListSecretsPaginateResponseSecretListTypeDef(
    _ListSecretsPaginateResponseSecretListTypeDef
):
    """
    Type definition for `ListSecretsPaginateResponse` `SecretList`

    A structure that contains the details about a secret. It does not include the encrypted
    ``SecretString`` and ``SecretBinary`` values. To get those values, use the  GetSecretValue
    operation.

    - **ARN** *(string) --*

      The Amazon Resource Name (ARN) of the secret.

      For more information about ARNs in Secrets Manager, see `Policy Resources
      <https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#iam-resources>`__
      in the *AWS Secrets Manager User Guide* .

    - **Name** *(string) --*

      The friendly name of the secret. You can use forward slashes in the name to represent a
      path hierarchy. For example, ``/prod/databases/dbserver1`` could represent the secret for
      a server named ``dbserver1`` in the folder ``databases`` in the folder ``prod`` .

    - **Description** *(string) --*

      The user-provided description of the secret.

    - **KmsKeyId** *(string) --*

      The ARN or alias of the AWS KMS customer master key (CMK) that's used to encrypt the
      ``SecretString`` and ``SecretBinary`` fields in each version of the secret. If you don't
      provide a key, then Secrets Manager defaults to encrypting the secret fields with the
      default KMS CMK (the one named ``awssecretsmanager`` ) for this account.

    - **RotationEnabled** *(boolean) --*

      Indicated whether automatic, scheduled rotation is enabled for this secret.

    - **RotationLambdaARN** *(string) --*

      The ARN of an AWS Lambda function that's invoked by Secrets Manager to rotate and expire
      the secret either automatically per the schedule or manually by a call to  RotateSecret .

    - **RotationRules** *(dict) --*

      A structure that defines the rotation configuration for the secret.

      - **AutomaticallyAfterDays** *(integer) --*

        Specifies the number of days between automatic scheduled rotations of the secret.

        Secrets Manager schedules the next rotation when the previous one is complete. Secrets
        Manager schedules the date by adding the rotation interval (number of days) to the
        actual date of the last rotation. The service chooses the hour within that 24-hour date
        window randomly. The minute is also chosen somewhat randomly, but weighted towards the
        top of the hour and influenced by a variety of factors that help distribute load.

    - **LastRotatedDate** *(datetime) --*

      The last date and time that the rotation process for this secret was invoked.

    - **LastChangedDate** *(datetime) --*

      The last date and time that this secret was modified in any way.

    - **LastAccessedDate** *(datetime) --*

      The last date that this secret was accessed. This value is truncated to midnight of the
      date and therefore shows only the date, not the time.

    - **DeletedDate** *(datetime) --*

      The date and time on which this secret was deleted. Not present on active secrets. The
      secret can be recovered until the number of days in the recovery window has passed, as
      specified in the ``RecoveryWindowInDays`` parameter of the  DeleteSecret operation.

    - **Tags** *(list) --*

      The list of user-defined tags that are associated with the secret. To add tags to a
      secret, use  TagResource . To remove tags, use  UntagResource .

      - *(dict) --*

        A structure that contains information about a tag.

        - **Key** *(string) --*

          The key identifier, or name, of the tag.

        - **Value** *(string) --*

          The string value that's associated with the key of the tag.

    - **SecretVersionsToStages** *(dict) --*

      A list of all of the currently assigned ``SecretVersionStage`` staging labels and the
      ``SecretVersionId`` that each is attached to. Staging labels are used to keep track of
      the different versions during the rotation process.

      .. note::

        A version that does not have any ``SecretVersionStage`` is considered deprecated and
        subject to deletion. Such versions are not included in this list.

      - *(string) --*

        - *(list) --*

          - *(string) --*

    - **OwningService** *(string) --*
    """


_ListSecretsPaginateResponseTypeDef = TypedDict(
    "_ListSecretsPaginateResponseTypeDef",
    {"SecretList": List[ListSecretsPaginateResponseSecretListTypeDef]},
    total=False,
)


class ListSecretsPaginateResponseTypeDef(_ListSecretsPaginateResponseTypeDef):
    """
    Type definition for `ListSecretsPaginate` `Response`

    - **SecretList** *(list) --*

      A list of the secrets in the account.

      - *(dict) --*

        A structure that contains the details about a secret. It does not include the encrypted
        ``SecretString`` and ``SecretBinary`` values. To get those values, use the  GetSecretValue
        operation.

        - **ARN** *(string) --*

          The Amazon Resource Name (ARN) of the secret.

          For more information about ARNs in Secrets Manager, see `Policy Resources
          <https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#iam-resources>`__
          in the *AWS Secrets Manager User Guide* .

        - **Name** *(string) --*

          The friendly name of the secret. You can use forward slashes in the name to represent a
          path hierarchy. For example, ``/prod/databases/dbserver1`` could represent the secret for
          a server named ``dbserver1`` in the folder ``databases`` in the folder ``prod`` .

        - **Description** *(string) --*

          The user-provided description of the secret.

        - **KmsKeyId** *(string) --*

          The ARN or alias of the AWS KMS customer master key (CMK) that's used to encrypt the
          ``SecretString`` and ``SecretBinary`` fields in each version of the secret. If you don't
          provide a key, then Secrets Manager defaults to encrypting the secret fields with the
          default KMS CMK (the one named ``awssecretsmanager`` ) for this account.

        - **RotationEnabled** *(boolean) --*

          Indicated whether automatic, scheduled rotation is enabled for this secret.

        - **RotationLambdaARN** *(string) --*

          The ARN of an AWS Lambda function that's invoked by Secrets Manager to rotate and expire
          the secret either automatically per the schedule or manually by a call to  RotateSecret .

        - **RotationRules** *(dict) --*

          A structure that defines the rotation configuration for the secret.

          - **AutomaticallyAfterDays** *(integer) --*

            Specifies the number of days between automatic scheduled rotations of the secret.

            Secrets Manager schedules the next rotation when the previous one is complete. Secrets
            Manager schedules the date by adding the rotation interval (number of days) to the
            actual date of the last rotation. The service chooses the hour within that 24-hour date
            window randomly. The minute is also chosen somewhat randomly, but weighted towards the
            top of the hour and influenced by a variety of factors that help distribute load.

        - **LastRotatedDate** *(datetime) --*

          The last date and time that the rotation process for this secret was invoked.

        - **LastChangedDate** *(datetime) --*

          The last date and time that this secret was modified in any way.

        - **LastAccessedDate** *(datetime) --*

          The last date that this secret was accessed. This value is truncated to midnight of the
          date and therefore shows only the date, not the time.

        - **DeletedDate** *(datetime) --*

          The date and time on which this secret was deleted. Not present on active secrets. The
          secret can be recovered until the number of days in the recovery window has passed, as
          specified in the ``RecoveryWindowInDays`` parameter of the  DeleteSecret operation.

        - **Tags** *(list) --*

          The list of user-defined tags that are associated with the secret. To add tags to a
          secret, use  TagResource . To remove tags, use  UntagResource .

          - *(dict) --*

            A structure that contains information about a tag.

            - **Key** *(string) --*

              The key identifier, or name, of the tag.

            - **Value** *(string) --*

              The string value that's associated with the key of the tag.

        - **SecretVersionsToStages** *(dict) --*

          A list of all of the currently assigned ``SecretVersionStage`` staging labels and the
          ``SecretVersionId`` that each is attached to. Staging labels are used to keep track of
          the different versions during the rotation process.

          .. note::

            A version that does not have any ``SecretVersionStage`` is considered deprecated and
            subject to deletion. Such versions are not included in this list.

          - *(string) --*

            - *(list) --*

              - *(string) --*

        - **OwningService** *(string) --*
    """

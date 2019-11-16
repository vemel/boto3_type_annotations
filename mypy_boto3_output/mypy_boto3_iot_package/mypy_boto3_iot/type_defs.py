"Main interface for iot type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


_ClientAssociateTargetsWithJobResponseTypeDef = TypedDict(
    "_ClientAssociateTargetsWithJobResponseTypeDef",
    {"jobArn": str, "jobId": str, "description": str},
    total=False,
)


class ClientAssociateTargetsWithJobResponseTypeDef(
    _ClientAssociateTargetsWithJobResponseTypeDef
):
    """
    Type definition for `ClientAssociateTargetsWithJob` `Response`

    - **jobArn** *(string) --*

      An ARN identifying the job.

    - **jobId** *(string) --*

      The unique identifier you assigned to this job when it was created.

    - **description** *(string) --*

      A short text description of the job.
    """


_ClientCancelJobResponseTypeDef = TypedDict(
    "_ClientCancelJobResponseTypeDef",
    {"jobArn": str, "jobId": str, "description": str},
    total=False,
)


class ClientCancelJobResponseTypeDef(_ClientCancelJobResponseTypeDef):
    """
    Type definition for `ClientCancelJob` `Response`

    - **jobArn** *(string) --*

      The job ARN.

    - **jobId** *(string) --*

      The unique identifier you assigned to this job when it was created.

    - **description** *(string) --*

      A short text description of the job.
    """


_ClientCreateAuthorizerResponseTypeDef = TypedDict(
    "_ClientCreateAuthorizerResponseTypeDef",
    {"authorizerName": str, "authorizerArn": str},
    total=False,
)


class ClientCreateAuthorizerResponseTypeDef(_ClientCreateAuthorizerResponseTypeDef):
    """
    Type definition for `ClientCreateAuthorizer` `Response`

    - **authorizerName** *(string) --*

      The authorizer's name.

    - **authorizerArn** *(string) --*

      The authorizer ARN.
    """


_ClientCreateBillingGroupResponseTypeDef = TypedDict(
    "_ClientCreateBillingGroupResponseTypeDef",
    {"billingGroupName": str, "billingGroupArn": str, "billingGroupId": str},
    total=False,
)


class ClientCreateBillingGroupResponseTypeDef(_ClientCreateBillingGroupResponseTypeDef):
    """
    Type definition for `ClientCreateBillingGroup` `Response`

    - **billingGroupName** *(string) --*

      The name you gave to the billing group.

    - **billingGroupArn** *(string) --*

      The ARN of the billing group.

    - **billingGroupId** *(string) --*

      The ID of the billing group.
    """


_ClientCreateBillingGroupbillingGroupPropertiesTypeDef = TypedDict(
    "_ClientCreateBillingGroupbillingGroupPropertiesTypeDef",
    {"billingGroupDescription": str},
    total=False,
)


class ClientCreateBillingGroupbillingGroupPropertiesTypeDef(
    _ClientCreateBillingGroupbillingGroupPropertiesTypeDef
):
    """
    Type definition for `ClientCreateBillingGroup` `billingGroupProperties`

    The properties of the billing group.

    - **billingGroupDescription** *(string) --*

      The description of the billing group.
    """


_ClientCreateBillingGrouptagsTypeDef = TypedDict(
    "_ClientCreateBillingGrouptagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateBillingGrouptagsTypeDef(_ClientCreateBillingGrouptagsTypeDef):
    """
    Type definition for `ClientCreateBillingGroup` `tags`

    A set of key/value pairs that are used to manage the resource.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientCreateCertificateFromCsrResponseTypeDef = TypedDict(
    "_ClientCreateCertificateFromCsrResponseTypeDef",
    {"certificateArn": str, "certificateId": str, "certificatePem": str},
    total=False,
)


class ClientCreateCertificateFromCsrResponseTypeDef(
    _ClientCreateCertificateFromCsrResponseTypeDef
):
    """
    Type definition for `ClientCreateCertificateFromCsr` `Response`

    The output from the CreateCertificateFromCsr operation.

    - **certificateArn** *(string) --*

      The Amazon Resource Name (ARN) of the certificate. You can use the ARN as a principal for
      policy operations.

    - **certificateId** *(string) --*

      The ID of the certificate. Certificate management operations only take a certificateId.

    - **certificatePem** *(string) --*

      The certificate data, in PEM format.
    """


_ClientCreateDynamicThingGroupResponseTypeDef = TypedDict(
    "_ClientCreateDynamicThingGroupResponseTypeDef",
    {
        "thingGroupName": str,
        "thingGroupArn": str,
        "thingGroupId": str,
        "indexName": str,
        "queryString": str,
        "queryVersion": str,
    },
    total=False,
)


class ClientCreateDynamicThingGroupResponseTypeDef(
    _ClientCreateDynamicThingGroupResponseTypeDef
):
    """
    Type definition for `ClientCreateDynamicThingGroup` `Response`

    - **thingGroupName** *(string) --*

      The dynamic thing group name.

    - **thingGroupArn** *(string) --*

      The dynamic thing group ARN.

    - **thingGroupId** *(string) --*

      The dynamic thing group ID.

    - **indexName** *(string) --*

      The dynamic thing group index name.

    - **queryString** *(string) --*

      The dynamic thing group search query string.

    - **queryVersion** *(string) --*

      The dynamic thing group query version.
    """


_ClientCreateDynamicThingGrouptagsTypeDef = TypedDict(
    "_ClientCreateDynamicThingGrouptagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateDynamicThingGrouptagsTypeDef(
    _ClientCreateDynamicThingGrouptagsTypeDef
):
    """
    Type definition for `ClientCreateDynamicThingGroup` `tags`

    A set of key/value pairs that are used to manage the resource.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientCreateDynamicThingGroupthingGroupPropertiesattributePayloadTypeDef = TypedDict(
    "_ClientCreateDynamicThingGroupthingGroupPropertiesattributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)


class ClientCreateDynamicThingGroupthingGroupPropertiesattributePayloadTypeDef(
    _ClientCreateDynamicThingGroupthingGroupPropertiesattributePayloadTypeDef
):
    """
    Type definition for `ClientCreateDynamicThingGroupthingGroupProperties` `attributePayload`

    The thing group attributes in JSON format.

    - **attributes** *(dict) --*

      A JSON string containing up to three key-value pair in JSON format. For example:

       ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``

      - *(string) --*

        - *(string) --*

    - **merge** *(boolean) --*

      Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with
      the attributes stored in the registry, instead of overwriting them.

      To remove an attribute, call ``UpdateThing`` with an empty attribute value.

      .. note::

        The ``merge`` attribute is only valid when calling ``UpdateThing`` or ``UpdateThingGroup`` .
    """


_ClientCreateDynamicThingGroupthingGroupPropertiesTypeDef = TypedDict(
    "_ClientCreateDynamicThingGroupthingGroupPropertiesTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": ClientCreateDynamicThingGroupthingGroupPropertiesattributePayloadTypeDef,
    },
    total=False,
)


class ClientCreateDynamicThingGroupthingGroupPropertiesTypeDef(
    _ClientCreateDynamicThingGroupthingGroupPropertiesTypeDef
):
    """
    Type definition for `ClientCreateDynamicThingGroup` `thingGroupProperties`

    The dynamic thing group properties.

    - **thingGroupDescription** *(string) --*

      The thing group description.

    - **attributePayload** *(dict) --*

      The thing group attributes in JSON format.

      - **attributes** *(dict) --*

        A JSON string containing up to three key-value pair in JSON format. For example:

         ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``

        - *(string) --*

          - *(string) --*

      - **merge** *(boolean) --*

        Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with
        the attributes stored in the registry, instead of overwriting them.

        To remove an attribute, call ``UpdateThing`` with an empty attribute value.

        .. note::

          The ``merge`` attribute is only valid when calling ``UpdateThing`` or ``UpdateThingGroup`` .
    """


_ClientCreateJobResponseTypeDef = TypedDict(
    "_ClientCreateJobResponseTypeDef",
    {"jobArn": str, "jobId": str, "description": str},
    total=False,
)


class ClientCreateJobResponseTypeDef(_ClientCreateJobResponseTypeDef):
    """
    Type definition for `ClientCreateJob` `Response`

    - **jobArn** *(string) --*

      The job ARN.

    - **jobId** *(string) --*

      The unique identifier you assigned to this job.

    - **description** *(string) --*

      The job description.
    """


_ClientCreateJobabortConfigcriteriaListTypeDef = TypedDict(
    "_ClientCreateJobabortConfigcriteriaListTypeDef",
    {
        "failureType": str,
        "action": str,
        "thresholdPercentage": float,
        "minNumberOfExecutedThings": int,
    },
)


class ClientCreateJobabortConfigcriteriaListTypeDef(
    _ClientCreateJobabortConfigcriteriaListTypeDef
):
    """
    Type definition for `ClientCreateJobabortConfig` `criteriaList`

    Details of abort criteria to define rules to abort the job.

    - **failureType** *(string) --* **[REQUIRED]**

      The type of job execution failure to define a rule to initiate a job abort.

    - **action** *(string) --* **[REQUIRED]**

      The type of abort action to initiate a job abort.

    - **thresholdPercentage** *(float) --* **[REQUIRED]**

      The threshold as a percentage of the total number of executed things that will initiate a
      job abort.

      AWS IoT supports up to two digits after the decimal (for example, 10.9 and 10.99, but not
      10.999).

    - **minNumberOfExecutedThings** *(integer) --* **[REQUIRED]**

      Minimum number of executed things before evaluating an abort rule.
    """


_ClientCreateJobabortConfigTypeDef = TypedDict(
    "_ClientCreateJobabortConfigTypeDef",
    {"criteriaList": List[ClientCreateJobabortConfigcriteriaListTypeDef]},
)


class ClientCreateJobabortConfigTypeDef(_ClientCreateJobabortConfigTypeDef):
    """
    Type definition for `ClientCreateJob` `abortConfig`

    Allows you to create criteria to abort a job.

    - **criteriaList** *(list) --* **[REQUIRED]**

      The list of abort criteria to define rules to abort the job.

      - *(dict) --*

        Details of abort criteria to define rules to abort the job.

        - **failureType** *(string) --* **[REQUIRED]**

          The type of job execution failure to define a rule to initiate a job abort.

        - **action** *(string) --* **[REQUIRED]**

          The type of abort action to initiate a job abort.

        - **thresholdPercentage** *(float) --* **[REQUIRED]**

          The threshold as a percentage of the total number of executed things that will initiate a
          job abort.

          AWS IoT supports up to two digits after the decimal (for example, 10.9 and 10.99, but not
          10.999).

        - **minNumberOfExecutedThings** *(integer) --* **[REQUIRED]**

          Minimum number of executed things before evaluating an abort rule.
    """


_ClientCreateJobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef = TypedDict(
    "_ClientCreateJobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef",
    {"numberOfNotifiedThings": int, "numberOfSucceededThings": int},
    total=False,
)


class ClientCreateJobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef(
    _ClientCreateJobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef
):
    """
    Type definition for `ClientCreateJobjobExecutionsRolloutConfigexponentialRate` `rateIncreaseCriteria`

    The criteria to initiate the increase in rate of rollout for a job.

    AWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).

    - **numberOfNotifiedThings** *(integer) --*

      The threshold for number of notified things that will initiate the increase in rate of
      rollout.

    - **numberOfSucceededThings** *(integer) --*

      The threshold for number of succeeded things that will initiate the increase in rate of
      rollout.
    """


_ClientCreateJobjobExecutionsRolloutConfigexponentialRateTypeDef = TypedDict(
    "_ClientCreateJobjobExecutionsRolloutConfigexponentialRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": ClientCreateJobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef,
    },
)


class ClientCreateJobjobExecutionsRolloutConfigexponentialRateTypeDef(
    _ClientCreateJobjobExecutionsRolloutConfigexponentialRateTypeDef
):
    """
    Type definition for `ClientCreateJobjobExecutionsRolloutConfig` `exponentialRate`

    The rate of increase for a job rollout. This parameter allows you to define an exponential rate
    for a job rollout.

    - **baseRatePerMinute** *(integer) --* **[REQUIRED]**

      The minimum number of things that will be notified of a pending job, per minute at the start
      of job rollout. This parameter allows you to define the initial rate of rollout.

    - **incrementFactor** *(float) --* **[REQUIRED]**

      The exponential factor to increase the rate of rollout for a job.

    - **rateIncreaseCriteria** *(dict) --* **[REQUIRED]**

      The criteria to initiate the increase in rate of rollout for a job.

      AWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).

      - **numberOfNotifiedThings** *(integer) --*

        The threshold for number of notified things that will initiate the increase in rate of
        rollout.

      - **numberOfSucceededThings** *(integer) --*

        The threshold for number of succeeded things that will initiate the increase in rate of
        rollout.
    """


_ClientCreateJobjobExecutionsRolloutConfigTypeDef = TypedDict(
    "_ClientCreateJobjobExecutionsRolloutConfigTypeDef",
    {
        "maximumPerMinute": int,
        "exponentialRate": ClientCreateJobjobExecutionsRolloutConfigexponentialRateTypeDef,
    },
    total=False,
)


class ClientCreateJobjobExecutionsRolloutConfigTypeDef(
    _ClientCreateJobjobExecutionsRolloutConfigTypeDef
):
    """
    Type definition for `ClientCreateJob` `jobExecutionsRolloutConfig`

    Allows you to create a staged rollout of the job.

    - **maximumPerMinute** *(integer) --*

      The maximum number of things that will be notified of a pending job, per minute. This parameter
      allows you to create a staged rollout.

    - **exponentialRate** *(dict) --*

      The rate of increase for a job rollout. This parameter allows you to define an exponential rate
      for a job rollout.

      - **baseRatePerMinute** *(integer) --* **[REQUIRED]**

        The minimum number of things that will be notified of a pending job, per minute at the start
        of job rollout. This parameter allows you to define the initial rate of rollout.

      - **incrementFactor** *(float) --* **[REQUIRED]**

        The exponential factor to increase the rate of rollout for a job.

      - **rateIncreaseCriteria** *(dict) --* **[REQUIRED]**

        The criteria to initiate the increase in rate of rollout for a job.

        AWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).

        - **numberOfNotifiedThings** *(integer) --*

          The threshold for number of notified things that will initiate the increase in rate of
          rollout.

        - **numberOfSucceededThings** *(integer) --*

          The threshold for number of succeeded things that will initiate the increase in rate of
          rollout.
    """


_ClientCreateJobpresignedUrlConfigTypeDef = TypedDict(
    "_ClientCreateJobpresignedUrlConfigTypeDef",
    {"roleArn": str, "expiresInSec": int},
    total=False,
)


class ClientCreateJobpresignedUrlConfigTypeDef(
    _ClientCreateJobpresignedUrlConfigTypeDef
):
    """
    Type definition for `ClientCreateJob` `presignedUrlConfig`

    Configuration information for pre-signed S3 URLs.

    - **roleArn** *(string) --*

      The ARN of an IAM role that grants grants permission to download files from the S3 bucket where
      the job data/updates are stored. The role must also grant permission for IoT to download the
      files.

    - **expiresInSec** *(integer) --*

      How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value
      is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job
      document.
    """


_ClientCreateJobtagsTypeDef = TypedDict(
    "_ClientCreateJobtagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateJobtagsTypeDef(_ClientCreateJobtagsTypeDef):
    """
    Type definition for `ClientCreateJob` `tags`

    A set of key/value pairs that are used to manage the resource.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientCreateJobtimeoutConfigTypeDef = TypedDict(
    "_ClientCreateJobtimeoutConfigTypeDef",
    {"inProgressTimeoutInMinutes": int},
    total=False,
)


class ClientCreateJobtimeoutConfigTypeDef(_ClientCreateJobtimeoutConfigTypeDef):
    """
    Type definition for `ClientCreateJob` `timeoutConfig`

    Specifies the amount of time each device has to finish its execution of the job. The timer is
    started when the job execution status is set to ``IN_PROGRESS`` . If the job execution status is
    not set to another terminal state before the time expires, it will be automatically set to
    ``TIMED_OUT`` .

    - **inProgressTimeoutInMinutes** *(integer) --*

      Specifies the amount of time, in minutes, this device has to finish execution of this job. The
      timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in
      progress timer can't be updated and will apply to all job executions for the job. Whenever a
      job execution remains in the IN_PROGRESS status for longer than this interval, the job
      execution will fail and switch to the terminal ``TIMED_OUT`` status.
    """


_ClientCreateKeysAndCertificateResponsekeyPairTypeDef = TypedDict(
    "_ClientCreateKeysAndCertificateResponsekeyPairTypeDef",
    {"PublicKey": str, "PrivateKey": str},
    total=False,
)


class ClientCreateKeysAndCertificateResponsekeyPairTypeDef(
    _ClientCreateKeysAndCertificateResponsekeyPairTypeDef
):
    """
    Type definition for `ClientCreateKeysAndCertificateResponse` `keyPair`

    The generated key pair.

    - **PublicKey** *(string) --*

      The public key.

    - **PrivateKey** *(string) --*

      The private key.
    """


_ClientCreateKeysAndCertificateResponseTypeDef = TypedDict(
    "_ClientCreateKeysAndCertificateResponseTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "certificatePem": str,
        "keyPair": ClientCreateKeysAndCertificateResponsekeyPairTypeDef,
    },
    total=False,
)


class ClientCreateKeysAndCertificateResponseTypeDef(
    _ClientCreateKeysAndCertificateResponseTypeDef
):
    """
    Type definition for `ClientCreateKeysAndCertificate` `Response`

    The output of the CreateKeysAndCertificate operation.

    - **certificateArn** *(string) --*

      The ARN of the certificate.

    - **certificateId** *(string) --*

      The ID of the certificate. AWS IoT issues a default subject name for the certificate (for
      example, AWS IoT Certificate).

    - **certificatePem** *(string) --*

      The certificate data, in PEM format.

    - **keyPair** *(dict) --*

      The generated key pair.

      - **PublicKey** *(string) --*

        The public key.

      - **PrivateKey** *(string) --*

        The private key.
    """


_ClientCreateMitigationActionResponseTypeDef = TypedDict(
    "_ClientCreateMitigationActionResponseTypeDef",
    {"actionArn": str, "actionId": str},
    total=False,
)


class ClientCreateMitigationActionResponseTypeDef(
    _ClientCreateMitigationActionResponseTypeDef
):
    """
    Type definition for `ClientCreateMitigationAction` `Response`

    - **actionArn** *(string) --*

      The ARN for the new mitigation action.

    - **actionId** *(string) --*

      A unique identifier for the new mitigation action.
    """


_RequiredClientCreateMitigationActionactionParamsaddThingsToThingGroupParamsTypeDef = TypedDict(
    "_RequiredClientCreateMitigationActionactionParamsaddThingsToThingGroupParamsTypeDef",
    {"thingGroupNames": List[str]},
)
_OptionalClientCreateMitigationActionactionParamsaddThingsToThingGroupParamsTypeDef = TypedDict(
    "_OptionalClientCreateMitigationActionactionParamsaddThingsToThingGroupParamsTypeDef",
    {"overrideDynamicGroups": bool},
    total=False,
)


class ClientCreateMitigationActionactionParamsaddThingsToThingGroupParamsTypeDef(
    _RequiredClientCreateMitigationActionactionParamsaddThingsToThingGroupParamsTypeDef,
    _OptionalClientCreateMitigationActionactionParamsaddThingsToThingGroupParamsTypeDef,
):
    """
    Type definition for `ClientCreateMitigationActionactionParams` `addThingsToThingGroupParams`

    Parameters to define a mitigation action that moves devices associated with a certificate to
    one or more specified thing groups, typically for quarantine.

    - **thingGroupNames** *(list) --* **[REQUIRED]**

      The list of groups to which you want to add the things that triggered the mitigation action.
      You can add a thing to a maximum of 10 groups, but you cannot add a thing to more than one
      group in the same hierarchy.

      - *(string) --*

    - **overrideDynamicGroups** *(boolean) --*

      Specifies if this mitigation action can move the things that triggered the mitigation action
      even if they are part of one or more dynamic things groups.
    """


_ClientCreateMitigationActionactionParamsenableIoTLoggingParamsTypeDef = TypedDict(
    "_ClientCreateMitigationActionactionParamsenableIoTLoggingParamsTypeDef",
    {"roleArnForLogging": str, "logLevel": str},
)


class ClientCreateMitigationActionactionParamsenableIoTLoggingParamsTypeDef(
    _ClientCreateMitigationActionactionParamsenableIoTLoggingParamsTypeDef
):
    """
    Type definition for `ClientCreateMitigationActionactionParams` `enableIoTLoggingParams`

    Parameters to define a mitigation action that enables AWS IoT logging at a specified level of
    detail.

    - **roleArnForLogging** *(string) --* **[REQUIRED]**

      The ARN of the IAM role used for logging.

    - **logLevel** *(string) --* **[REQUIRED]**

      Specifies the types of information to be logged.
    """


_ClientCreateMitigationActionactionParamspublishFindingToSnsParamsTypeDef = TypedDict(
    "_ClientCreateMitigationActionactionParamspublishFindingToSnsParamsTypeDef",
    {"topicArn": str},
)


class ClientCreateMitigationActionactionParamspublishFindingToSnsParamsTypeDef(
    _ClientCreateMitigationActionactionParamspublishFindingToSnsParamsTypeDef
):
    """
    Type definition for `ClientCreateMitigationActionactionParams` `publishFindingToSnsParams`

    Parameters to define a mitigation action that publishes findings to Amazon SNS. You can
    implement your own custom actions in response to the Amazon SNS messages.

    - **topicArn** *(string) --* **[REQUIRED]**

      The ARN of the topic to which you want to publish the findings.
    """


_ClientCreateMitigationActionactionParamsreplaceDefaultPolicyVersionParamsTypeDef = TypedDict(
    "_ClientCreateMitigationActionactionParamsreplaceDefaultPolicyVersionParamsTypeDef",
    {"templateName": str},
)


class ClientCreateMitigationActionactionParamsreplaceDefaultPolicyVersionParamsTypeDef(
    _ClientCreateMitigationActionactionParamsreplaceDefaultPolicyVersionParamsTypeDef
):
    """
    Type definition for `ClientCreateMitigationActionactionParams` `replaceDefaultPolicyVersionParams`

    Parameters to define a mitigation action that adds a blank policy to restrict permissions.

    - **templateName** *(string) --* **[REQUIRED]**

      The name of the template to be applied. The only supported value is ``BLANK_POLICY`` .
    """


_ClientCreateMitigationActionactionParamsupdateCACertificateParamsTypeDef = TypedDict(
    "_ClientCreateMitigationActionactionParamsupdateCACertificateParamsTypeDef",
    {"action": str},
)


class ClientCreateMitigationActionactionParamsupdateCACertificateParamsTypeDef(
    _ClientCreateMitigationActionactionParamsupdateCACertificateParamsTypeDef
):
    """
    Type definition for `ClientCreateMitigationActionactionParams` `updateCACertificateParams`

    Parameters to define a mitigation action that changes the state of the CA certificate to
    inactive.

    - **action** *(string) --* **[REQUIRED]**

      The action that you want to apply to the CA cerrtificate. The only supported value is
      ``DEACTIVATE`` .
    """


_ClientCreateMitigationActionactionParamsupdateDeviceCertificateParamsTypeDef = TypedDict(
    "_ClientCreateMitigationActionactionParamsupdateDeviceCertificateParamsTypeDef",
    {"action": str},
)


class ClientCreateMitigationActionactionParamsupdateDeviceCertificateParamsTypeDef(
    _ClientCreateMitigationActionactionParamsupdateDeviceCertificateParamsTypeDef
):
    """
    Type definition for `ClientCreateMitigationActionactionParams` `updateDeviceCertificateParams`

    Parameters to define a mitigation action that changes the state of the device certificate to
    inactive.

    - **action** *(string) --* **[REQUIRED]**

      The action that you want to apply to the device cerrtificate. The only supported value is
      ``DEACTIVATE`` .
    """


_ClientCreateMitigationActionactionParamsTypeDef = TypedDict(
    "_ClientCreateMitigationActionactionParamsTypeDef",
    {
        "updateDeviceCertificateParams": ClientCreateMitigationActionactionParamsupdateDeviceCertificateParamsTypeDef,
        "updateCACertificateParams": ClientCreateMitigationActionactionParamsupdateCACertificateParamsTypeDef,
        "addThingsToThingGroupParams": ClientCreateMitigationActionactionParamsaddThingsToThingGroupParamsTypeDef,
        "replaceDefaultPolicyVersionParams": ClientCreateMitigationActionactionParamsreplaceDefaultPolicyVersionParamsTypeDef,
        "enableIoTLoggingParams": ClientCreateMitigationActionactionParamsenableIoTLoggingParamsTypeDef,
        "publishFindingToSnsParams": ClientCreateMitigationActionactionParamspublishFindingToSnsParamsTypeDef,
    },
    total=False,
)


class ClientCreateMitigationActionactionParamsTypeDef(
    _ClientCreateMitigationActionactionParamsTypeDef
):
    """
    Type definition for `ClientCreateMitigationAction` `actionParams`

    Defines the type of action and the parameters for that action.

    - **updateDeviceCertificateParams** *(dict) --*

      Parameters to define a mitigation action that changes the state of the device certificate to
      inactive.

      - **action** *(string) --* **[REQUIRED]**

        The action that you want to apply to the device cerrtificate. The only supported value is
        ``DEACTIVATE`` .

    - **updateCACertificateParams** *(dict) --*

      Parameters to define a mitigation action that changes the state of the CA certificate to
      inactive.

      - **action** *(string) --* **[REQUIRED]**

        The action that you want to apply to the CA cerrtificate. The only supported value is
        ``DEACTIVATE`` .

    - **addThingsToThingGroupParams** *(dict) --*

      Parameters to define a mitigation action that moves devices associated with a certificate to
      one or more specified thing groups, typically for quarantine.

      - **thingGroupNames** *(list) --* **[REQUIRED]**

        The list of groups to which you want to add the things that triggered the mitigation action.
        You can add a thing to a maximum of 10 groups, but you cannot add a thing to more than one
        group in the same hierarchy.

        - *(string) --*

      - **overrideDynamicGroups** *(boolean) --*

        Specifies if this mitigation action can move the things that triggered the mitigation action
        even if they are part of one or more dynamic things groups.

    - **replaceDefaultPolicyVersionParams** *(dict) --*

      Parameters to define a mitigation action that adds a blank policy to restrict permissions.

      - **templateName** *(string) --* **[REQUIRED]**

        The name of the template to be applied. The only supported value is ``BLANK_POLICY`` .

    - **enableIoTLoggingParams** *(dict) --*

      Parameters to define a mitigation action that enables AWS IoT logging at a specified level of
      detail.

      - **roleArnForLogging** *(string) --* **[REQUIRED]**

        The ARN of the IAM role used for logging.

      - **logLevel** *(string) --* **[REQUIRED]**

        Specifies the types of information to be logged.

    - **publishFindingToSnsParams** *(dict) --*

      Parameters to define a mitigation action that publishes findings to Amazon SNS. You can
      implement your own custom actions in response to the Amazon SNS messages.

      - **topicArn** *(string) --* **[REQUIRED]**

        The ARN of the topic to which you want to publish the findings.
    """


_ClientCreateMitigationActiontagsTypeDef = TypedDict(
    "_ClientCreateMitigationActiontagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateMitigationActiontagsTypeDef(_ClientCreateMitigationActiontagsTypeDef):
    """
    Type definition for `ClientCreateMitigationAction` `tags`

    A set of key/value pairs that are used to manage the resource.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientCreateOtaUpdateResponseTypeDef = TypedDict(
    "_ClientCreateOtaUpdateResponseTypeDef",
    {
        "otaUpdateId": str,
        "awsIotJobId": str,
        "otaUpdateArn": str,
        "awsIotJobArn": str,
        "otaUpdateStatus": str,
    },
    total=False,
)


class ClientCreateOtaUpdateResponseTypeDef(_ClientCreateOtaUpdateResponseTypeDef):
    """
    Type definition for `ClientCreateOtaUpdate` `Response`

    - **otaUpdateId** *(string) --*

      The OTA update ID.

    - **awsIotJobId** *(string) --*

      The AWS IoT job ID associated with the OTA update.

    - **otaUpdateArn** *(string) --*

      The OTA update ARN.

    - **awsIotJobArn** *(string) --*

      The AWS IoT job ARN associated with the OTA update.

    - **otaUpdateStatus** *(string) --*

      The OTA update status.
    """


_ClientCreateOtaUpdateawsJobExecutionsRolloutConfigTypeDef = TypedDict(
    "_ClientCreateOtaUpdateawsJobExecutionsRolloutConfigTypeDef",
    {"maximumPerMinute": int},
    total=False,
)


class ClientCreateOtaUpdateawsJobExecutionsRolloutConfigTypeDef(
    _ClientCreateOtaUpdateawsJobExecutionsRolloutConfigTypeDef
):
    """
    Type definition for `ClientCreateOtaUpdate` `awsJobExecutionsRolloutConfig`

    Configuration for the rollout of OTA updates.

    - **maximumPerMinute** *(integer) --*

      The maximum number of OTA update job executions started per minute.
    """


_ClientCreateOtaUpdatefilescodeSigningcustomCodeSigningcertificateChainTypeDef = TypedDict(
    "_ClientCreateOtaUpdatefilescodeSigningcustomCodeSigningcertificateChainTypeDef",
    {"certificateName": str, "inlineDocument": str},
    total=False,
)


class ClientCreateOtaUpdatefilescodeSigningcustomCodeSigningcertificateChainTypeDef(
    _ClientCreateOtaUpdatefilescodeSigningcustomCodeSigningcertificateChainTypeDef
):
    """
    Type definition for `ClientCreateOtaUpdatefilescodeSigningcustomCodeSigning` `certificateChain`

    The certificate chain.

    - **certificateName** *(string) --*

      The name of the certificate.

    - **inlineDocument** *(string) --*

      A base64 encoded binary representation of the code signing certificate chain.
    """


_ClientCreateOtaUpdatefilescodeSigningcustomCodeSigningsignatureTypeDef = TypedDict(
    "_ClientCreateOtaUpdatefilescodeSigningcustomCodeSigningsignatureTypeDef",
    {"inlineDocument": bytes},
    total=False,
)


class ClientCreateOtaUpdatefilescodeSigningcustomCodeSigningsignatureTypeDef(
    _ClientCreateOtaUpdatefilescodeSigningcustomCodeSigningsignatureTypeDef
):
    """
    Type definition for `ClientCreateOtaUpdatefilescodeSigningcustomCodeSigning` `signature`

    The signature for the file.

    - **inlineDocument** *(bytes) --*

      A base64 encoded binary representation of the code signing signature.
    """


_ClientCreateOtaUpdatefilescodeSigningcustomCodeSigningTypeDef = TypedDict(
    "_ClientCreateOtaUpdatefilescodeSigningcustomCodeSigningTypeDef",
    {
        "signature": ClientCreateOtaUpdatefilescodeSigningcustomCodeSigningsignatureTypeDef,
        "certificateChain": ClientCreateOtaUpdatefilescodeSigningcustomCodeSigningcertificateChainTypeDef,
        "hashAlgorithm": str,
        "signatureAlgorithm": str,
    },
    total=False,
)


class ClientCreateOtaUpdatefilescodeSigningcustomCodeSigningTypeDef(
    _ClientCreateOtaUpdatefilescodeSigningcustomCodeSigningTypeDef
):
    """
    Type definition for `ClientCreateOtaUpdatefilescodeSigning` `customCodeSigning`

    A custom method for code signing a file.

    - **signature** *(dict) --*

      The signature for the file.

      - **inlineDocument** *(bytes) --*

        A base64 encoded binary representation of the code signing signature.

    - **certificateChain** *(dict) --*

      The certificate chain.

      - **certificateName** *(string) --*

        The name of the certificate.

      - **inlineDocument** *(string) --*

        A base64 encoded binary representation of the code signing certificate chain.

    - **hashAlgorithm** *(string) --*

      The hash algorithm used to code sign the file.

    - **signatureAlgorithm** *(string) --*

      The signature algorithm used to code sign the file.
    """


_ClientCreateOtaUpdatefilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef = TypedDict(
    "_ClientCreateOtaUpdatefilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef",
    {"bucket": str, "prefix": str},
    total=False,
)


class ClientCreateOtaUpdatefilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef(
    _ClientCreateOtaUpdatefilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef
):
    """
    Type definition for `ClientCreateOtaUpdatefilescodeSigningstartSigningJobParameterdestination` `s3Destination`

    Describes the location in S3 of the updated firmware.

    - **bucket** *(string) --*

      The S3 bucket that contains the updated firmware.

    - **prefix** *(string) --*

      The S3 prefix.
    """


_ClientCreateOtaUpdatefilescodeSigningstartSigningJobParameterdestinationTypeDef = TypedDict(
    "_ClientCreateOtaUpdatefilescodeSigningstartSigningJobParameterdestinationTypeDef",
    {
        "s3Destination": ClientCreateOtaUpdatefilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef
    },
    total=False,
)


class ClientCreateOtaUpdatefilescodeSigningstartSigningJobParameterdestinationTypeDef(
    _ClientCreateOtaUpdatefilescodeSigningstartSigningJobParameterdestinationTypeDef
):
    """
    Type definition for `ClientCreateOtaUpdatefilescodeSigningstartSigningJobParameter` `destination`

    The location to write the code-signed file.

    - **s3Destination** *(dict) --*

      Describes the location in S3 of the updated firmware.

      - **bucket** *(string) --*

        The S3 bucket that contains the updated firmware.

      - **prefix** *(string) --*

        The S3 prefix.
    """


_ClientCreateOtaUpdatefilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef = TypedDict(
    "_ClientCreateOtaUpdatefilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef",
    {"certificateArn": str, "platform": str, "certificatePathOnDevice": str},
    total=False,
)


class ClientCreateOtaUpdatefilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef(
    _ClientCreateOtaUpdatefilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef
):
    """
    Type definition for `ClientCreateOtaUpdatefilescodeSigningstartSigningJobParameter` `signingProfileParameter`

    Describes the code-signing profile.

    - **certificateArn** *(string) --*

      Certificate ARN.

    - **platform** *(string) --*

      The hardware platform of your device.

    - **certificatePathOnDevice** *(string) --*

      The location of the code-signing certificate on your device.
    """


_ClientCreateOtaUpdatefilescodeSigningstartSigningJobParameterTypeDef = TypedDict(
    "_ClientCreateOtaUpdatefilescodeSigningstartSigningJobParameterTypeDef",
    {
        "signingProfileParameter": ClientCreateOtaUpdatefilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef,
        "signingProfileName": str,
        "destination": ClientCreateOtaUpdatefilescodeSigningstartSigningJobParameterdestinationTypeDef,
    },
    total=False,
)


class ClientCreateOtaUpdatefilescodeSigningstartSigningJobParameterTypeDef(
    _ClientCreateOtaUpdatefilescodeSigningstartSigningJobParameterTypeDef
):
    """
    Type definition for `ClientCreateOtaUpdatefilescodeSigning` `startSigningJobParameter`

    Describes the code-signing job.

    - **signingProfileParameter** *(dict) --*

      Describes the code-signing profile.

      - **certificateArn** *(string) --*

        Certificate ARN.

      - **platform** *(string) --*

        The hardware platform of your device.

      - **certificatePathOnDevice** *(string) --*

        The location of the code-signing certificate on your device.

    - **signingProfileName** *(string) --*

      The code-signing profile name.

    - **destination** *(dict) --*

      The location to write the code-signed file.

      - **s3Destination** *(dict) --*

        Describes the location in S3 of the updated firmware.

        - **bucket** *(string) --*

          The S3 bucket that contains the updated firmware.

        - **prefix** *(string) --*

          The S3 prefix.
    """


_ClientCreateOtaUpdatefilescodeSigningTypeDef = TypedDict(
    "_ClientCreateOtaUpdatefilescodeSigningTypeDef",
    {
        "awsSignerJobId": str,
        "startSigningJobParameter": ClientCreateOtaUpdatefilescodeSigningstartSigningJobParameterTypeDef,
        "customCodeSigning": ClientCreateOtaUpdatefilescodeSigningcustomCodeSigningTypeDef,
    },
    total=False,
)


class ClientCreateOtaUpdatefilescodeSigningTypeDef(
    _ClientCreateOtaUpdatefilescodeSigningTypeDef
):
    """
    Type definition for `ClientCreateOtaUpdatefiles` `codeSigning`

    The code signing method of the file.

    - **awsSignerJobId** *(string) --*

      The ID of the AWSSignerJob which was created to sign the file.

    - **startSigningJobParameter** *(dict) --*

      Describes the code-signing job.

      - **signingProfileParameter** *(dict) --*

        Describes the code-signing profile.

        - **certificateArn** *(string) --*

          Certificate ARN.

        - **platform** *(string) --*

          The hardware platform of your device.

        - **certificatePathOnDevice** *(string) --*

          The location of the code-signing certificate on your device.

      - **signingProfileName** *(string) --*

        The code-signing profile name.

      - **destination** *(dict) --*

        The location to write the code-signed file.

        - **s3Destination** *(dict) --*

          Describes the location in S3 of the updated firmware.

          - **bucket** *(string) --*

            The S3 bucket that contains the updated firmware.

          - **prefix** *(string) --*

            The S3 prefix.

    - **customCodeSigning** *(dict) --*

      A custom method for code signing a file.

      - **signature** *(dict) --*

        The signature for the file.

        - **inlineDocument** *(bytes) --*

          A base64 encoded binary representation of the code signing signature.

      - **certificateChain** *(dict) --*

        The certificate chain.

        - **certificateName** *(string) --*

          The name of the certificate.

        - **inlineDocument** *(string) --*

          A base64 encoded binary representation of the code signing certificate chain.

      - **hashAlgorithm** *(string) --*

        The hash algorithm used to code sign the file.

      - **signatureAlgorithm** *(string) --*

        The signature algorithm used to code sign the file.
    """


_ClientCreateOtaUpdatefilesfileLocations3LocationTypeDef = TypedDict(
    "_ClientCreateOtaUpdatefilesfileLocations3LocationTypeDef",
    {"bucket": str, "key": str, "version": str},
    total=False,
)


class ClientCreateOtaUpdatefilesfileLocations3LocationTypeDef(
    _ClientCreateOtaUpdatefilesfileLocations3LocationTypeDef
):
    """
    Type definition for `ClientCreateOtaUpdatefilesfileLocation` `s3Location`

    The location of the updated firmware in S3.

    - **bucket** *(string) --*

      The S3 bucket.

    - **key** *(string) --*

      The S3 key.

    - **version** *(string) --*

      The S3 bucket version.
    """


_ClientCreateOtaUpdatefilesfileLocationstreamTypeDef = TypedDict(
    "_ClientCreateOtaUpdatefilesfileLocationstreamTypeDef",
    {"streamId": str, "fileId": int},
    total=False,
)


class ClientCreateOtaUpdatefilesfileLocationstreamTypeDef(
    _ClientCreateOtaUpdatefilesfileLocationstreamTypeDef
):
    """
    Type definition for `ClientCreateOtaUpdatefilesfileLocation` `stream`

    The stream that contains the OTA update.

    - **streamId** *(string) --*

      The stream ID.

    - **fileId** *(integer) --*

      The ID of a file associated with a stream.
    """


_ClientCreateOtaUpdatefilesfileLocationTypeDef = TypedDict(
    "_ClientCreateOtaUpdatefilesfileLocationTypeDef",
    {
        "stream": ClientCreateOtaUpdatefilesfileLocationstreamTypeDef,
        "s3Location": ClientCreateOtaUpdatefilesfileLocations3LocationTypeDef,
    },
    total=False,
)


class ClientCreateOtaUpdatefilesfileLocationTypeDef(
    _ClientCreateOtaUpdatefilesfileLocationTypeDef
):
    """
    Type definition for `ClientCreateOtaUpdatefiles` `fileLocation`

    The location of the updated firmware.

    - **stream** *(dict) --*

      The stream that contains the OTA update.

      - **streamId** *(string) --*

        The stream ID.

      - **fileId** *(integer) --*

        The ID of a file associated with a stream.

    - **s3Location** *(dict) --*

      The location of the updated firmware in S3.

      - **bucket** *(string) --*

        The S3 bucket.

      - **key** *(string) --*

        The S3 key.

      - **version** *(string) --*

        The S3 bucket version.
    """


_ClientCreateOtaUpdatefilesTypeDef = TypedDict(
    "_ClientCreateOtaUpdatefilesTypeDef",
    {
        "fileName": str,
        "fileVersion": str,
        "fileLocation": ClientCreateOtaUpdatefilesfileLocationTypeDef,
        "codeSigning": ClientCreateOtaUpdatefilescodeSigningTypeDef,
        "attributes": Dict[str, str],
    },
    total=False,
)


class ClientCreateOtaUpdatefilesTypeDef(_ClientCreateOtaUpdatefilesTypeDef):
    """
    Type definition for `ClientCreateOtaUpdate` `files`

    Describes a file to be associated with an OTA update.

    - **fileName** *(string) --*

      The name of the file.

    - **fileVersion** *(string) --*

      The file version.

    - **fileLocation** *(dict) --*

      The location of the updated firmware.

      - **stream** *(dict) --*

        The stream that contains the OTA update.

        - **streamId** *(string) --*

          The stream ID.

        - **fileId** *(integer) --*

          The ID of a file associated with a stream.

      - **s3Location** *(dict) --*

        The location of the updated firmware in S3.

        - **bucket** *(string) --*

          The S3 bucket.

        - **key** *(string) --*

          The S3 key.

        - **version** *(string) --*

          The S3 bucket version.

    - **codeSigning** *(dict) --*

      The code signing method of the file.

      - **awsSignerJobId** *(string) --*

        The ID of the AWSSignerJob which was created to sign the file.

      - **startSigningJobParameter** *(dict) --*

        Describes the code-signing job.

        - **signingProfileParameter** *(dict) --*

          Describes the code-signing profile.

          - **certificateArn** *(string) --*

            Certificate ARN.

          - **platform** *(string) --*

            The hardware platform of your device.

          - **certificatePathOnDevice** *(string) --*

            The location of the code-signing certificate on your device.

        - **signingProfileName** *(string) --*

          The code-signing profile name.

        - **destination** *(dict) --*

          The location to write the code-signed file.

          - **s3Destination** *(dict) --*

            Describes the location in S3 of the updated firmware.

            - **bucket** *(string) --*

              The S3 bucket that contains the updated firmware.

            - **prefix** *(string) --*

              The S3 prefix.

      - **customCodeSigning** *(dict) --*

        A custom method for code signing a file.

        - **signature** *(dict) --*

          The signature for the file.

          - **inlineDocument** *(bytes) --*

            A base64 encoded binary representation of the code signing signature.

        - **certificateChain** *(dict) --*

          The certificate chain.

          - **certificateName** *(string) --*

            The name of the certificate.

          - **inlineDocument** *(string) --*

            A base64 encoded binary representation of the code signing certificate chain.

        - **hashAlgorithm** *(string) --*

          The hash algorithm used to code sign the file.

        - **signatureAlgorithm** *(string) --*

          The signature algorithm used to code sign the file.

    - **attributes** *(dict) --*

      A list of name/attribute pairs.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateOtaUpdatetagsTypeDef = TypedDict(
    "_ClientCreateOtaUpdatetagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateOtaUpdatetagsTypeDef(_ClientCreateOtaUpdatetagsTypeDef):
    """
    Type definition for `ClientCreateOtaUpdate` `tags`

    A set of key/value pairs that are used to manage the resource.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientCreatePolicyResponseTypeDef = TypedDict(
    "_ClientCreatePolicyResponseTypeDef",
    {
        "policyName": str,
        "policyArn": str,
        "policyDocument": str,
        "policyVersionId": str,
    },
    total=False,
)


class ClientCreatePolicyResponseTypeDef(_ClientCreatePolicyResponseTypeDef):
    """
    Type definition for `ClientCreatePolicy` `Response`

    The output from the CreatePolicy operation.

    - **policyName** *(string) --*

      The policy name.

    - **policyArn** *(string) --*

      The policy ARN.

    - **policyDocument** *(string) --*

      The JSON document that describes the policy.

    - **policyVersionId** *(string) --*

      The policy version ID.
    """


_ClientCreatePolicyVersionResponseTypeDef = TypedDict(
    "_ClientCreatePolicyVersionResponseTypeDef",
    {
        "policyArn": str,
        "policyDocument": str,
        "policyVersionId": str,
        "isDefaultVersion": bool,
    },
    total=False,
)


class ClientCreatePolicyVersionResponseTypeDef(
    _ClientCreatePolicyVersionResponseTypeDef
):
    """
    Type definition for `ClientCreatePolicyVersion` `Response`

    The output of the CreatePolicyVersion operation.

    - **policyArn** *(string) --*

      The policy ARN.

    - **policyDocument** *(string) --*

      The JSON document that describes the policy.

    - **policyVersionId** *(string) --*

      The policy version ID.

    - **isDefaultVersion** *(boolean) --*

      Specifies whether the policy version is the default.
    """


_ClientCreateRoleAliasResponseTypeDef = TypedDict(
    "_ClientCreateRoleAliasResponseTypeDef",
    {"roleAlias": str, "roleAliasArn": str},
    total=False,
)


class ClientCreateRoleAliasResponseTypeDef(_ClientCreateRoleAliasResponseTypeDef):
    """
    Type definition for `ClientCreateRoleAlias` `Response`

    - **roleAlias** *(string) --*

      The role alias.

    - **roleAliasArn** *(string) --*

      The role alias ARN.
    """


_ClientCreateScheduledAuditResponseTypeDef = TypedDict(
    "_ClientCreateScheduledAuditResponseTypeDef",
    {"scheduledAuditArn": str},
    total=False,
)


class ClientCreateScheduledAuditResponseTypeDef(
    _ClientCreateScheduledAuditResponseTypeDef
):
    """
    Type definition for `ClientCreateScheduledAudit` `Response`

    - **scheduledAuditArn** *(string) --*

      The ARN of the scheduled audit.
    """


_ClientCreateScheduledAudittagsTypeDef = TypedDict(
    "_ClientCreateScheduledAudittagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateScheduledAudittagsTypeDef(_ClientCreateScheduledAudittagsTypeDef):
    """
    Type definition for `ClientCreateScheduledAudit` `tags`

    A set of key/value pairs that are used to manage the resource.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientCreateSecurityProfileResponseTypeDef = TypedDict(
    "_ClientCreateSecurityProfileResponseTypeDef",
    {"securityProfileName": str, "securityProfileArn": str},
    total=False,
)


class ClientCreateSecurityProfileResponseTypeDef(
    _ClientCreateSecurityProfileResponseTypeDef
):
    """
    Type definition for `ClientCreateSecurityProfile` `Response`

    - **securityProfileName** *(string) --*

      The name you gave to the security profile.

    - **securityProfileArn** *(string) --*

      The ARN of the security profile.
    """


_ClientCreateSecurityProfilealertTargetsTypeDef = TypedDict(
    "_ClientCreateSecurityProfilealertTargetsTypeDef",
    {"alertTargetArn": str, "roleArn": str},
)


class ClientCreateSecurityProfilealertTargetsTypeDef(
    _ClientCreateSecurityProfilealertTargetsTypeDef
):
    """
    Type definition for `ClientCreateSecurityProfile` `alertTargets`

    A structure containing the alert target ARN and the role ARN.

    - **alertTargetArn** *(string) --* **[REQUIRED]**

      The ARN of the notification target to which alerts are sent.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that grants permission to send alerts to the notification target.
    """


_ClientCreateSecurityProfilebehaviorscriteriastatisticalThresholdTypeDef = TypedDict(
    "_ClientCreateSecurityProfilebehaviorscriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)


class ClientCreateSecurityProfilebehaviorscriteriastatisticalThresholdTypeDef(
    _ClientCreateSecurityProfilebehaviorscriteriastatisticalThresholdTypeDef
):
    """
    Type definition for `ClientCreateSecurityProfilebehaviorscriteria` `statisticalThreshold`

    A statistical ranking (percentile) which indicates a threshold value by which a behavior is
    determined to be in compliance or in violation of the behavior.

    - **statistic** *(string) --*

      The percentile which resolves to a threshold value by which compliance with a behavior is
      determined. Metrics are collected over the specified period (``durationSeconds`` ) from
      all reporting devices in your account and statistical ranks are calculated. Then, the
      measurements from a device are collected over the same period. If the accumulated
      measurements from the device fall above or below (``comparisonOperator`` ) the value
      associated with the percentile specified, then the device is considered to be in
      compliance with the behavior, otherwise a violation occurs.
    """


_ClientCreateSecurityProfilebehaviorscriteriavalueTypeDef = TypedDict(
    "_ClientCreateSecurityProfilebehaviorscriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ClientCreateSecurityProfilebehaviorscriteriavalueTypeDef(
    _ClientCreateSecurityProfilebehaviorscriteriavalueTypeDef
):
    """
    Type definition for `ClientCreateSecurityProfilebehaviorscriteria` `value`

    The value to be compared with the ``metric`` .

    - **count** *(integer) --*

      If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric
      value to be compared with the ``metric`` .

    - **cidrs** *(list) --*

      If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
      be compared with the ``metric`` .

      - *(string) --*

    - **ports** *(list) --*

      If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
      be compared with the ``metric`` .

      - *(integer) --*
    """


_ClientCreateSecurityProfilebehaviorscriteriaTypeDef = TypedDict(
    "_ClientCreateSecurityProfilebehaviorscriteriaTypeDef",
    {
        "comparisonOperator": str,
        "value": ClientCreateSecurityProfilebehaviorscriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientCreateSecurityProfilebehaviorscriteriastatisticalThresholdTypeDef,
    },
    total=False,
)


class ClientCreateSecurityProfilebehaviorscriteriaTypeDef(
    _ClientCreateSecurityProfilebehaviorscriteriaTypeDef
):
    """
    Type definition for `ClientCreateSecurityProfilebehaviors` `criteria`

    The criteria that determine if a device is behaving normally in regard to the ``metric`` .

    - **comparisonOperator** *(string) --*

      The operator that relates the thing measured (``metric`` ) to the criteria (containing a
      ``value`` or ``statisticalThreshold`` ).

    - **value** *(dict) --*

      The value to be compared with the ``metric`` .

      - **count** *(integer) --*

        If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric
        value to be compared with the ``metric`` .

      - **cidrs** *(list) --*

        If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
        be compared with the ``metric`` .

        - *(string) --*

      - **ports** *(list) --*

        If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
        be compared with the ``metric`` .

        - *(integer) --*

    - **durationSeconds** *(integer) --*

      Use this to specify the time duration over which the behavior is evaluated, for those
      criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
      ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated
      over this time duration before being used to calculate percentiles, and later, measurements
      from an individual device are also accumulated over this time duration before being given a
      percentile rank.

    - **consecutiveDatapointsToAlarm** *(integer) --*

      If a device is in violation of the behavior for the specified number of consecutive
      datapoints, an alarm occurs. If not specified, the default is 1.

    - **consecutiveDatapointsToClear** *(integer) --*

      If an alarm has occurred and the offending device is no longer in violation of the behavior
      for the specified number of consecutive datapoints, the alarm is cleared. If not specified,
      the default is 1.

    - **statisticalThreshold** *(dict) --*

      A statistical ranking (percentile) which indicates a threshold value by which a behavior is
      determined to be in compliance or in violation of the behavior.

      - **statistic** *(string) --*

        The percentile which resolves to a threshold value by which compliance with a behavior is
        determined. Metrics are collected over the specified period (``durationSeconds`` ) from
        all reporting devices in your account and statistical ranks are calculated. Then, the
        measurements from a device are collected over the same period. If the accumulated
        measurements from the device fall above or below (``comparisonOperator`` ) the value
        associated with the percentile specified, then the device is considered to be in
        compliance with the behavior, otherwise a violation occurs.
    """


_RequiredClientCreateSecurityProfilebehaviorsTypeDef = TypedDict(
    "_RequiredClientCreateSecurityProfilebehaviorsTypeDef", {"name": str}
)
_OptionalClientCreateSecurityProfilebehaviorsTypeDef = TypedDict(
    "_OptionalClientCreateSecurityProfilebehaviorsTypeDef",
    {"metric": str, "criteria": ClientCreateSecurityProfilebehaviorscriteriaTypeDef},
    total=False,
)


class ClientCreateSecurityProfilebehaviorsTypeDef(
    _RequiredClientCreateSecurityProfilebehaviorsTypeDef,
    _OptionalClientCreateSecurityProfilebehaviorsTypeDef,
):
    """
    Type definition for `ClientCreateSecurityProfile` `behaviors`

    A Device Defender security profile behavior.

    - **name** *(string) --* **[REQUIRED]**

      The name you have given to the behavior.

    - **metric** *(string) --*

      What is measured by the behavior.

    - **criteria** *(dict) --*

      The criteria that determine if a device is behaving normally in regard to the ``metric`` .

      - **comparisonOperator** *(string) --*

        The operator that relates the thing measured (``metric`` ) to the criteria (containing a
        ``value`` or ``statisticalThreshold`` ).

      - **value** *(dict) --*

        The value to be compared with the ``metric`` .

        - **count** *(integer) --*

          If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric
          value to be compared with the ``metric`` .

        - **cidrs** *(list) --*

          If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
          be compared with the ``metric`` .

          - *(string) --*

        - **ports** *(list) --*

          If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
          be compared with the ``metric`` .

          - *(integer) --*

      - **durationSeconds** *(integer) --*

        Use this to specify the time duration over which the behavior is evaluated, for those
        criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
        ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated
        over this time duration before being used to calculate percentiles, and later, measurements
        from an individual device are also accumulated over this time duration before being given a
        percentile rank.

      - **consecutiveDatapointsToAlarm** *(integer) --*

        If a device is in violation of the behavior for the specified number of consecutive
        datapoints, an alarm occurs. If not specified, the default is 1.

      - **consecutiveDatapointsToClear** *(integer) --*

        If an alarm has occurred and the offending device is no longer in violation of the behavior
        for the specified number of consecutive datapoints, the alarm is cleared. If not specified,
        the default is 1.

      - **statisticalThreshold** *(dict) --*

        A statistical ranking (percentile) which indicates a threshold value by which a behavior is
        determined to be in compliance or in violation of the behavior.

        - **statistic** *(string) --*

          The percentile which resolves to a threshold value by which compliance with a behavior is
          determined. Metrics are collected over the specified period (``durationSeconds`` ) from
          all reporting devices in your account and statistical ranks are calculated. Then, the
          measurements from a device are collected over the same period. If the accumulated
          measurements from the device fall above or below (``comparisonOperator`` ) the value
          associated with the percentile specified, then the device is considered to be in
          compliance with the behavior, otherwise a violation occurs.
    """


_ClientCreateSecurityProfiletagsTypeDef = TypedDict(
    "_ClientCreateSecurityProfiletagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateSecurityProfiletagsTypeDef(_ClientCreateSecurityProfiletagsTypeDef):
    """
    Type definition for `ClientCreateSecurityProfile` `tags`

    A set of key/value pairs that are used to manage the resource.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientCreateStreamResponseTypeDef = TypedDict(
    "_ClientCreateStreamResponseTypeDef",
    {"streamId": str, "streamArn": str, "description": str, "streamVersion": int},
    total=False,
)


class ClientCreateStreamResponseTypeDef(_ClientCreateStreamResponseTypeDef):
    """
    Type definition for `ClientCreateStream` `Response`

    - **streamId** *(string) --*

      The stream ID.

    - **streamArn** *(string) --*

      The stream ARN.

    - **description** *(string) --*

      A description of the stream.

    - **streamVersion** *(integer) --*

      The version of the stream.
    """


_ClientCreateStreamfiless3LocationTypeDef = TypedDict(
    "_ClientCreateStreamfiless3LocationTypeDef",
    {"bucket": str, "key": str, "version": str},
    total=False,
)


class ClientCreateStreamfiless3LocationTypeDef(
    _ClientCreateStreamfiless3LocationTypeDef
):
    """
    Type definition for `ClientCreateStreamfiles` `s3Location`

    The location of the file in S3.

    - **bucket** *(string) --*

      The S3 bucket.

    - **key** *(string) --*

      The S3 key.

    - **version** *(string) --*

      The S3 bucket version.
    """


_ClientCreateStreamfilesTypeDef = TypedDict(
    "_ClientCreateStreamfilesTypeDef",
    {"fileId": int, "s3Location": ClientCreateStreamfiless3LocationTypeDef},
    total=False,
)


class ClientCreateStreamfilesTypeDef(_ClientCreateStreamfilesTypeDef):
    """
    Type definition for `ClientCreateStream` `files`

    Represents a file to stream.

    - **fileId** *(integer) --*

      The file ID.

    - **s3Location** *(dict) --*

      The location of the file in S3.

      - **bucket** *(string) --*

        The S3 bucket.

      - **key** *(string) --*

        The S3 key.

      - **version** *(string) --*

        The S3 bucket version.
    """


_ClientCreateStreamtagsTypeDef = TypedDict(
    "_ClientCreateStreamtagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateStreamtagsTypeDef(_ClientCreateStreamtagsTypeDef):
    """
    Type definition for `ClientCreateStream` `tags`

    A set of key/value pairs that are used to manage the resource.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientCreateThingGroupResponseTypeDef = TypedDict(
    "_ClientCreateThingGroupResponseTypeDef",
    {"thingGroupName": str, "thingGroupArn": str, "thingGroupId": str},
    total=False,
)


class ClientCreateThingGroupResponseTypeDef(_ClientCreateThingGroupResponseTypeDef):
    """
    Type definition for `ClientCreateThingGroup` `Response`

    - **thingGroupName** *(string) --*

      The thing group name.

    - **thingGroupArn** *(string) --*

      The thing group ARN.

    - **thingGroupId** *(string) --*

      The thing group ID.
    """


_ClientCreateThingGrouptagsTypeDef = TypedDict(
    "_ClientCreateThingGrouptagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateThingGrouptagsTypeDef(_ClientCreateThingGrouptagsTypeDef):
    """
    Type definition for `ClientCreateThingGroup` `tags`

    A set of key/value pairs that are used to manage the resource.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientCreateThingGroupthingGroupPropertiesattributePayloadTypeDef = TypedDict(
    "_ClientCreateThingGroupthingGroupPropertiesattributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)


class ClientCreateThingGroupthingGroupPropertiesattributePayloadTypeDef(
    _ClientCreateThingGroupthingGroupPropertiesattributePayloadTypeDef
):
    """
    Type definition for `ClientCreateThingGroupthingGroupProperties` `attributePayload`

    The thing group attributes in JSON format.

    - **attributes** *(dict) --*

      A JSON string containing up to three key-value pair in JSON format. For example:

       ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``

      - *(string) --*

        - *(string) --*

    - **merge** *(boolean) --*

      Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with
      the attributes stored in the registry, instead of overwriting them.

      To remove an attribute, call ``UpdateThing`` with an empty attribute value.

      .. note::

        The ``merge`` attribute is only valid when calling ``UpdateThing`` or ``UpdateThingGroup`` .
    """


_ClientCreateThingGroupthingGroupPropertiesTypeDef = TypedDict(
    "_ClientCreateThingGroupthingGroupPropertiesTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": ClientCreateThingGroupthingGroupPropertiesattributePayloadTypeDef,
    },
    total=False,
)


class ClientCreateThingGroupthingGroupPropertiesTypeDef(
    _ClientCreateThingGroupthingGroupPropertiesTypeDef
):
    """
    Type definition for `ClientCreateThingGroup` `thingGroupProperties`

    The thing group properties.

    - **thingGroupDescription** *(string) --*

      The thing group description.

    - **attributePayload** *(dict) --*

      The thing group attributes in JSON format.

      - **attributes** *(dict) --*

        A JSON string containing up to three key-value pair in JSON format. For example:

         ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``

        - *(string) --*

          - *(string) --*

      - **merge** *(boolean) --*

        Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with
        the attributes stored in the registry, instead of overwriting them.

        To remove an attribute, call ``UpdateThing`` with an empty attribute value.

        .. note::

          The ``merge`` attribute is only valid when calling ``UpdateThing`` or ``UpdateThingGroup`` .
    """


_ClientCreateThingResponseTypeDef = TypedDict(
    "_ClientCreateThingResponseTypeDef",
    {"thingName": str, "thingArn": str, "thingId": str},
    total=False,
)


class ClientCreateThingResponseTypeDef(_ClientCreateThingResponseTypeDef):
    """
    Type definition for `ClientCreateThing` `Response`

    The output of the CreateThing operation.

    - **thingName** *(string) --*

      The name of the new thing.

    - **thingArn** *(string) --*

      The ARN of the new thing.

    - **thingId** *(string) --*

      The thing ID.
    """


_ClientCreateThingTypeResponseTypeDef = TypedDict(
    "_ClientCreateThingTypeResponseTypeDef",
    {"thingTypeName": str, "thingTypeArn": str, "thingTypeId": str},
    total=False,
)


class ClientCreateThingTypeResponseTypeDef(_ClientCreateThingTypeResponseTypeDef):
    """
    Type definition for `ClientCreateThingType` `Response`

    The output of the CreateThingType operation.

    - **thingTypeName** *(string) --*

      The name of the thing type.

    - **thingTypeArn** *(string) --*

      The Amazon Resource Name (ARN) of the thing type.

    - **thingTypeId** *(string) --*

      The thing type ID.
    """


_ClientCreateThingTypetagsTypeDef = TypedDict(
    "_ClientCreateThingTypetagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientCreateThingTypetagsTypeDef(_ClientCreateThingTypetagsTypeDef):
    """
    Type definition for `ClientCreateThingType` `tags`

    A set of key/value pairs that are used to manage the resource.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientCreateThingTypethingTypePropertiesTypeDef = TypedDict(
    "_ClientCreateThingTypethingTypePropertiesTypeDef",
    {"thingTypeDescription": str, "searchableAttributes": List[str]},
    total=False,
)


class ClientCreateThingTypethingTypePropertiesTypeDef(
    _ClientCreateThingTypethingTypePropertiesTypeDef
):
    """
    Type definition for `ClientCreateThingType` `thingTypeProperties`

    The ThingTypeProperties for the thing type to create. It contains information about the new thing
    type including a description, and a list of searchable thing attribute names.

    - **thingTypeDescription** *(string) --*

      The description of the thing type.

    - **searchableAttributes** *(list) --*

      A list of searchable thing attribute names.

      - *(string) --*
    """


_ClientCreateThingattributePayloadTypeDef = TypedDict(
    "_ClientCreateThingattributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)


class ClientCreateThingattributePayloadTypeDef(
    _ClientCreateThingattributePayloadTypeDef
):
    """
    Type definition for `ClientCreateThing` `attributePayload`

    The attribute payload, which consists of up to three name/value pairs in a JSON document. For
    example:

     ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``

    - **attributes** *(dict) --*

      A JSON string containing up to three key-value pair in JSON format. For example:

       ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``

      - *(string) --*

        - *(string) --*

    - **merge** *(boolean) --*

      Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with
      the attributes stored in the registry, instead of overwriting them.

      To remove an attribute, call ``UpdateThing`` with an empty attribute value.

      .. note::

        The ``merge`` attribute is only valid when calling ``UpdateThing`` or ``UpdateThingGroup`` .
    """


_ClientCreateTopicRuletopicRulePayloadactionscloudwatchAlarmTypeDef = TypedDict(
    "_ClientCreateTopicRuletopicRulePayloadactionscloudwatchAlarmTypeDef",
    {"roleArn": str, "alarmName": str, "stateReason": str, "stateValue": str},
)


class ClientCreateTopicRuletopicRulePayloadactionscloudwatchAlarmTypeDef(
    _ClientCreateTopicRuletopicRulePayloadactionscloudwatchAlarmTypeDef
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloadactions` `cloudwatchAlarm`

    Change the state of a CloudWatch alarm.

    - **roleArn** *(string) --* **[REQUIRED]**

      The IAM role that allows access to the CloudWatch alarm.

    - **alarmName** *(string) --* **[REQUIRED]**

      The CloudWatch alarm name.

    - **stateReason** *(string) --* **[REQUIRED]**

      The reason for the alarm change.

    - **stateValue** *(string) --* **[REQUIRED]**

      The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
    """


_RequiredClientCreateTopicRuletopicRulePayloadactionscloudwatchMetricTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloadactionscloudwatchMetricTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
    },
)
_OptionalClientCreateTopicRuletopicRulePayloadactionscloudwatchMetricTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloadactionscloudwatchMetricTypeDef",
    {"metricTimestamp": str},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloadactionscloudwatchMetricTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloadactionscloudwatchMetricTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloadactionscloudwatchMetricTypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloadactions` `cloudwatchMetric`

    Capture a CloudWatch metric.

    - **roleArn** *(string) --* **[REQUIRED]**

      The IAM role that allows access to the CloudWatch metric.

    - **metricNamespace** *(string) --* **[REQUIRED]**

      The CloudWatch metric namespace name.

    - **metricName** *(string) --* **[REQUIRED]**

      The CloudWatch metric name.

    - **metricValue** *(string) --* **[REQUIRED]**

      The CloudWatch metric value.

    - **metricUnit** *(string) --* **[REQUIRED]**

      The `metric unit
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
      supported by CloudWatch.

    - **metricTimestamp** *(string) --*

      An optional `Unix timestamp
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
      .
    """


_RequiredClientCreateTopicRuletopicRulePayloadactionsdynamoDBTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloadactionsdynamoDBTypeDef",
    {"tableName": str, "roleArn": str, "hashKeyField": str, "hashKeyValue": str},
)
_OptionalClientCreateTopicRuletopicRulePayloadactionsdynamoDBTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloadactionsdynamoDBTypeDef",
    {
        "operation": str,
        "hashKeyType": str,
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": str,
        "payloadField": str,
    },
    total=False,
)


class ClientCreateTopicRuletopicRulePayloadactionsdynamoDBTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloadactionsdynamoDBTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloadactionsdynamoDBTypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloadactions` `dynamoDB`

    Write to a DynamoDB table.

    - **tableName** *(string) --* **[REQUIRED]**

      The name of the DynamoDB table.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access to the DynamoDB table.

    - **operation** *(string) --*

      The type of operation to be performed. This follows the substitution template, so it can
      be ``${operation}`` , but the substitution must result in one of the following:
      ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

    - **hashKeyField** *(string) --* **[REQUIRED]**

      The hash key name.

    - **hashKeyValue** *(string) --* **[REQUIRED]**

      The hash key value.

    - **hashKeyType** *(string) --*

      The hash key type. Valid values are "STRING" or "NUMBER"

    - **rangeKeyField** *(string) --*

      The range key name.

    - **rangeKeyValue** *(string) --*

      The range key value.

    - **rangeKeyType** *(string) --*

      The range key type. Valid values are "STRING" or "NUMBER"

    - **payloadField** *(string) --*

      The action payload. This name can be customized.
    """


_ClientCreateTopicRuletopicRulePayloadactionsdynamoDBv2putItemTypeDef = TypedDict(
    "_ClientCreateTopicRuletopicRulePayloadactionsdynamoDBv2putItemTypeDef",
    {"tableName": str},
)


class ClientCreateTopicRuletopicRulePayloadactionsdynamoDBv2putItemTypeDef(
    _ClientCreateTopicRuletopicRulePayloadactionsdynamoDBv2putItemTypeDef
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloadactionsdynamoDBv2` `putItem`

    Specifies the DynamoDB table to which the message data will be written. For example:

     ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
     "my-table" } } }``

    Each attribute in the message payload will be written to a separate column in the
    DynamoDB database.

    - **tableName** *(string) --* **[REQUIRED]**

      The table where the message data will be written.
    """


_ClientCreateTopicRuletopicRulePayloadactionsdynamoDBv2TypeDef = TypedDict(
    "_ClientCreateTopicRuletopicRulePayloadactionsdynamoDBv2TypeDef",
    {
        "roleArn": str,
        "putItem": ClientCreateTopicRuletopicRulePayloadactionsdynamoDBv2putItemTypeDef,
    },
)


class ClientCreateTopicRuletopicRulePayloadactionsdynamoDBv2TypeDef(
    _ClientCreateTopicRuletopicRulePayloadactionsdynamoDBv2TypeDef
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloadactions` `dynamoDBv2`

    Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to
    write each attribute in an MQTT message payload into a separate DynamoDB column.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access to the DynamoDB table.

    - **putItem** *(dict) --* **[REQUIRED]**

      Specifies the DynamoDB table to which the message data will be written. For example:

       ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
       "my-table" } } }``

      Each attribute in the message payload will be written to a separate column in the
      DynamoDB database.

      - **tableName** *(string) --* **[REQUIRED]**

        The table where the message data will be written.
    """


_ClientCreateTopicRuletopicRulePayloadactionselasticsearchTypeDef = TypedDict(
    "_ClientCreateTopicRuletopicRulePayloadactionselasticsearchTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
)


class ClientCreateTopicRuletopicRulePayloadactionselasticsearchTypeDef(
    _ClientCreateTopicRuletopicRulePayloadactionselasticsearchTypeDef
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloadactions` `elasticsearch`

    Write data to an Amazon Elasticsearch Service domain.

    - **roleArn** *(string) --* **[REQUIRED]**

      The IAM role ARN that has access to Elasticsearch.

    - **endpoint** *(string) --* **[REQUIRED]**

      The endpoint of your Elasticsearch domain.

    - **index** *(string) --* **[REQUIRED]**

      The Elasticsearch index where you want to store your data.

    - **type** *(string) --* **[REQUIRED]**

      The type of document you are storing.

    - **id** *(string) --* **[REQUIRED]**

      The unique identifier for the document you are storing.
    """


_RequiredClientCreateTopicRuletopicRulePayloadactionsfirehoseTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloadactionsfirehoseTypeDef",
    {"roleArn": str, "deliveryStreamName": str},
)
_OptionalClientCreateTopicRuletopicRulePayloadactionsfirehoseTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloadactionsfirehoseTypeDef",
    {"separator": str},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloadactionsfirehoseTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloadactionsfirehoseTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloadactionsfirehoseTypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloadactions` `firehose`

    Write to an Amazon Kinesis Firehose stream.

    - **roleArn** *(string) --* **[REQUIRED]**

      The IAM role that grants access to the Amazon Kinesis Firehose stream.

    - **deliveryStreamName** *(string) --* **[REQUIRED]**

      The delivery stream name.

    - **separator** *(string) --*

      A character separator that will be used to separate records written to the Firehose
      stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ','
      (comma).
    """


_ClientCreateTopicRuletopicRulePayloadactionsiotAnalyticsTypeDef = TypedDict(
    "_ClientCreateTopicRuletopicRulePayloadactionsiotAnalyticsTypeDef",
    {"channelArn": str, "channelName": str, "roleArn": str},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloadactionsiotAnalyticsTypeDef(
    _ClientCreateTopicRuletopicRulePayloadactionsiotAnalyticsTypeDef
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloadactions` `iotAnalytics`

    Sends message data to an AWS IoT Analytics channel.

    - **channelArn** *(string) --*

      (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

    - **channelName** *(string) --*

      The name of the IoT Analytics channel to which message data will be sent.

    - **roleArn** *(string) --*

      The ARN of the role which has a policy that grants IoT Analytics permission to send
      message data via IoT Analytics (iotanalytics:BatchPutMessage).
    """


_RequiredClientCreateTopicRuletopicRulePayloadactionsiotEventsTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloadactionsiotEventsTypeDef",
    {"inputName": str, "roleArn": str},
)
_OptionalClientCreateTopicRuletopicRulePayloadactionsiotEventsTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloadactionsiotEventsTypeDef",
    {"messageId": str},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloadactionsiotEventsTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloadactionsiotEventsTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloadactionsiotEventsTypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloadactions` `iotEvents`

    Sends an input to an AWS IoT Events detector.

    - **inputName** *(string) --* **[REQUIRED]**

      The name of the AWS IoT Events input.

    - **messageId** *(string) --*

      [Optional] Use this to ensure that only one input (message) with a given messageId will
      be processed by an AWS IoT Events detector.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events
      detector. ("Action":"iotevents:BatchPutMessage").
    """


_RequiredClientCreateTopicRuletopicRulePayloadactionskinesisTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloadactionskinesisTypeDef",
    {"roleArn": str, "streamName": str},
)
_OptionalClientCreateTopicRuletopicRulePayloadactionskinesisTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloadactionskinesisTypeDef",
    {"partitionKey": str},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloadactionskinesisTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloadactionskinesisTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloadactionskinesisTypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloadactions` `kinesis`

    Write data to an Amazon Kinesis stream.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access to the Amazon Kinesis stream.

    - **streamName** *(string) --* **[REQUIRED]**

      The name of the Amazon Kinesis stream.

    - **partitionKey** *(string) --*

      The partition key.
    """


_ClientCreateTopicRuletopicRulePayloadactionslambdaTypeDef = TypedDict(
    "_ClientCreateTopicRuletopicRulePayloadactionslambdaTypeDef", {"functionArn": str}
)


class ClientCreateTopicRuletopicRulePayloadactionslambdaTypeDef(
    _ClientCreateTopicRuletopicRulePayloadactionslambdaTypeDef
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloadactions` `lambda`

    Invoke a Lambda function.

    - **functionArn** *(string) --* **[REQUIRED]**

      The ARN of the Lambda function.
    """


_RequiredClientCreateTopicRuletopicRulePayloadactionsrepublishTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloadactionsrepublishTypeDef",
    {"roleArn": str, "topic": str},
)
_OptionalClientCreateTopicRuletopicRulePayloadactionsrepublishTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloadactionsrepublishTypeDef",
    {"qos": int},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloadactionsrepublishTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloadactionsrepublishTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloadactionsrepublishTypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloadactions` `republish`

    Publish to another MQTT topic.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access.

    - **topic** *(string) --* **[REQUIRED]**

      The name of the MQTT topic.

    - **qos** *(integer) --*

      The Quality of Service (QoS) level to use when republishing messages. The default value
      is 0.
    """


_RequiredClientCreateTopicRuletopicRulePayloadactionss3TypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloadactionss3TypeDef",
    {"roleArn": str, "bucketName": str, "key": str},
)
_OptionalClientCreateTopicRuletopicRulePayloadactionss3TypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloadactionss3TypeDef",
    {"cannedAcl": str},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloadactionss3TypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloadactionss3TypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloadactionss3TypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloadactions` `s3`

    Write to an Amazon S3 bucket.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access.

    - **bucketName** *(string) --* **[REQUIRED]**

      The Amazon S3 bucket.

    - **key** *(string) --* **[REQUIRED]**

      The object key.

    - **cannedAcl** *(string) --*

      The Amazon S3 canned ACL that controls access to the object identified by the object key.
      For more information, see `S3 canned ACLs
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .
    """


_ClientCreateTopicRuletopicRulePayloadactionssalesforceTypeDef = TypedDict(
    "_ClientCreateTopicRuletopicRulePayloadactionssalesforceTypeDef",
    {"token": str, "url": str},
)


class ClientCreateTopicRuletopicRulePayloadactionssalesforceTypeDef(
    _ClientCreateTopicRuletopicRulePayloadactionssalesforceTypeDef
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloadactions` `salesforce`

    Send a message to a Salesforce IoT Cloud Input Stream.

    - **token** *(string) --* **[REQUIRED]**

      The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token
      is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

    - **url** *(string) --* **[REQUIRED]**

      The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the
      Salesforce IoT Cloud platform after creation of the Input Stream.
    """


_RequiredClientCreateTopicRuletopicRulePayloadactionssnsTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloadactionssnsTypeDef",
    {"targetArn": str, "roleArn": str},
)
_OptionalClientCreateTopicRuletopicRulePayloadactionssnsTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloadactionssnsTypeDef",
    {"messageFormat": str},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloadactionssnsTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloadactionssnsTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloadactionssnsTypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloadactions` `sns`

    Publish to an Amazon SNS topic.

    - **targetArn** *(string) --* **[REQUIRED]**

      The ARN of the SNS topic.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access.

    - **messageFormat** *(string) --*

      (Optional) The message format of the message to publish. Accepted values are "JSON" and
      "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if
      the payload should be parsed and relevant platform-specific bits of the payload should be
      extracted. To read more about SNS message formats, see
      `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
      <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official
      documentation.
    """


_RequiredClientCreateTopicRuletopicRulePayloadactionssqsTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloadactionssqsTypeDef",
    {"roleArn": str, "queueUrl": str},
)
_OptionalClientCreateTopicRuletopicRulePayloadactionssqsTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloadactionssqsTypeDef",
    {"useBase64": bool},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloadactionssqsTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloadactionssqsTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloadactionssqsTypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloadactions` `sqs`

    Publish to an Amazon SQS queue.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access.

    - **queueUrl** *(string) --* **[REQUIRED]**

      The URL of the Amazon SQS queue.

    - **useBase64** *(boolean) --*

      Specifies whether to use Base64 encoding.
    """


_RequiredClientCreateTopicRuletopicRulePayloadactionsstepFunctionsTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloadactionsstepFunctionsTypeDef",
    {"stateMachineName": str, "roleArn": str},
)
_OptionalClientCreateTopicRuletopicRulePayloadactionsstepFunctionsTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloadactionsstepFunctionsTypeDef",
    {"executionNamePrefix": str},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloadactionsstepFunctionsTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloadactionsstepFunctionsTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloadactionsstepFunctionsTypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloadactions` `stepFunctions`

    Starts execution of a Step Functions state machine.

    - **executionNamePrefix** *(string) --*

      (Optional) A name will be given to the state machine execution consisting of this prefix
      followed by a UUID. Step Functions automatically creates a unique name for each state
      machine execution if one is not provided.

    - **stateMachineName** *(string) --* **[REQUIRED]**

      The name of the Step Functions state machine whose execution will be started.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that grants IoT permission to start execution of a state machine
      ("Action":"states:StartExecution").
    """


_ClientCreateTopicRuletopicRulePayloadactionsTypeDef = TypedDict(
    "_ClientCreateTopicRuletopicRulePayloadactionsTypeDef",
    {
        "dynamoDB": ClientCreateTopicRuletopicRulePayloadactionsdynamoDBTypeDef,
        "dynamoDBv2": ClientCreateTopicRuletopicRulePayloadactionsdynamoDBv2TypeDef,
        "lambda": ClientCreateTopicRuletopicRulePayloadactionslambdaTypeDef,
        "sns": ClientCreateTopicRuletopicRulePayloadactionssnsTypeDef,
        "sqs": ClientCreateTopicRuletopicRulePayloadactionssqsTypeDef,
        "kinesis": ClientCreateTopicRuletopicRulePayloadactionskinesisTypeDef,
        "republish": ClientCreateTopicRuletopicRulePayloadactionsrepublishTypeDef,
        "s3": ClientCreateTopicRuletopicRulePayloadactionss3TypeDef,
        "firehose": ClientCreateTopicRuletopicRulePayloadactionsfirehoseTypeDef,
        "cloudwatchMetric": ClientCreateTopicRuletopicRulePayloadactionscloudwatchMetricTypeDef,
        "cloudwatchAlarm": ClientCreateTopicRuletopicRulePayloadactionscloudwatchAlarmTypeDef,
        "elasticsearch": ClientCreateTopicRuletopicRulePayloadactionselasticsearchTypeDef,
        "salesforce": ClientCreateTopicRuletopicRulePayloadactionssalesforceTypeDef,
        "iotAnalytics": ClientCreateTopicRuletopicRulePayloadactionsiotAnalyticsTypeDef,
        "iotEvents": ClientCreateTopicRuletopicRulePayloadactionsiotEventsTypeDef,
        "stepFunctions": ClientCreateTopicRuletopicRulePayloadactionsstepFunctionsTypeDef,
    },
    total=False,
)


class ClientCreateTopicRuletopicRulePayloadactionsTypeDef(
    _ClientCreateTopicRuletopicRulePayloadactionsTypeDef
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayload` `actions`

    Describes the actions associated with a rule.

    - **dynamoDB** *(dict) --*

      Write to a DynamoDB table.

      - **tableName** *(string) --* **[REQUIRED]**

        The name of the DynamoDB table.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access to the DynamoDB table.

      - **operation** *(string) --*

        The type of operation to be performed. This follows the substitution template, so it can
        be ``${operation}`` , but the substitution must result in one of the following:
        ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

      - **hashKeyField** *(string) --* **[REQUIRED]**

        The hash key name.

      - **hashKeyValue** *(string) --* **[REQUIRED]**

        The hash key value.

      - **hashKeyType** *(string) --*

        The hash key type. Valid values are "STRING" or "NUMBER"

      - **rangeKeyField** *(string) --*

        The range key name.

      - **rangeKeyValue** *(string) --*

        The range key value.

      - **rangeKeyType** *(string) --*

        The range key type. Valid values are "STRING" or "NUMBER"

      - **payloadField** *(string) --*

        The action payload. This name can be customized.

    - **dynamoDBv2** *(dict) --*

      Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to
      write each attribute in an MQTT message payload into a separate DynamoDB column.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access to the DynamoDB table.

      - **putItem** *(dict) --* **[REQUIRED]**

        Specifies the DynamoDB table to which the message data will be written. For example:

         ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
         "my-table" } } }``

        Each attribute in the message payload will be written to a separate column in the
        DynamoDB database.

        - **tableName** *(string) --* **[REQUIRED]**

          The table where the message data will be written.

    - **lambda** *(dict) --*

      Invoke a Lambda function.

      - **functionArn** *(string) --* **[REQUIRED]**

        The ARN of the Lambda function.

    - **sns** *(dict) --*

      Publish to an Amazon SNS topic.

      - **targetArn** *(string) --* **[REQUIRED]**

        The ARN of the SNS topic.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access.

      - **messageFormat** *(string) --*

        (Optional) The message format of the message to publish. Accepted values are "JSON" and
        "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if
        the payload should be parsed and relevant platform-specific bits of the payload should be
        extracted. To read more about SNS message formats, see
        `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
        <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official
        documentation.

    - **sqs** *(dict) --*

      Publish to an Amazon SQS queue.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access.

      - **queueUrl** *(string) --* **[REQUIRED]**

        The URL of the Amazon SQS queue.

      - **useBase64** *(boolean) --*

        Specifies whether to use Base64 encoding.

    - **kinesis** *(dict) --*

      Write data to an Amazon Kinesis stream.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access to the Amazon Kinesis stream.

      - **streamName** *(string) --* **[REQUIRED]**

        The name of the Amazon Kinesis stream.

      - **partitionKey** *(string) --*

        The partition key.

    - **republish** *(dict) --*

      Publish to another MQTT topic.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access.

      - **topic** *(string) --* **[REQUIRED]**

        The name of the MQTT topic.

      - **qos** *(integer) --*

        The Quality of Service (QoS) level to use when republishing messages. The default value
        is 0.

    - **s3** *(dict) --*

      Write to an Amazon S3 bucket.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access.

      - **bucketName** *(string) --* **[REQUIRED]**

        The Amazon S3 bucket.

      - **key** *(string) --* **[REQUIRED]**

        The object key.

      - **cannedAcl** *(string) --*

        The Amazon S3 canned ACL that controls access to the object identified by the object key.
        For more information, see `S3 canned ACLs
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

    - **firehose** *(dict) --*

      Write to an Amazon Kinesis Firehose stream.

      - **roleArn** *(string) --* **[REQUIRED]**

        The IAM role that grants access to the Amazon Kinesis Firehose stream.

      - **deliveryStreamName** *(string) --* **[REQUIRED]**

        The delivery stream name.

      - **separator** *(string) --*

        A character separator that will be used to separate records written to the Firehose
        stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ','
        (comma).

    - **cloudwatchMetric** *(dict) --*

      Capture a CloudWatch metric.

      - **roleArn** *(string) --* **[REQUIRED]**

        The IAM role that allows access to the CloudWatch metric.

      - **metricNamespace** *(string) --* **[REQUIRED]**

        The CloudWatch metric namespace name.

      - **metricName** *(string) --* **[REQUIRED]**

        The CloudWatch metric name.

      - **metricValue** *(string) --* **[REQUIRED]**

        The CloudWatch metric value.

      - **metricUnit** *(string) --* **[REQUIRED]**

        The `metric unit
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
        supported by CloudWatch.

      - **metricTimestamp** *(string) --*

        An optional `Unix timestamp
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
        .

    - **cloudwatchAlarm** *(dict) --*

      Change the state of a CloudWatch alarm.

      - **roleArn** *(string) --* **[REQUIRED]**

        The IAM role that allows access to the CloudWatch alarm.

      - **alarmName** *(string) --* **[REQUIRED]**

        The CloudWatch alarm name.

      - **stateReason** *(string) --* **[REQUIRED]**

        The reason for the alarm change.

      - **stateValue** *(string) --* **[REQUIRED]**

        The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

    - **elasticsearch** *(dict) --*

      Write data to an Amazon Elasticsearch Service domain.

      - **roleArn** *(string) --* **[REQUIRED]**

        The IAM role ARN that has access to Elasticsearch.

      - **endpoint** *(string) --* **[REQUIRED]**

        The endpoint of your Elasticsearch domain.

      - **index** *(string) --* **[REQUIRED]**

        The Elasticsearch index where you want to store your data.

      - **type** *(string) --* **[REQUIRED]**

        The type of document you are storing.

      - **id** *(string) --* **[REQUIRED]**

        The unique identifier for the document you are storing.

    - **salesforce** *(dict) --*

      Send a message to a Salesforce IoT Cloud Input Stream.

      - **token** *(string) --* **[REQUIRED]**

        The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token
        is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

      - **url** *(string) --* **[REQUIRED]**

        The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the
        Salesforce IoT Cloud platform after creation of the Input Stream.

    - **iotAnalytics** *(dict) --*

      Sends message data to an AWS IoT Analytics channel.

      - **channelArn** *(string) --*

        (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

      - **channelName** *(string) --*

        The name of the IoT Analytics channel to which message data will be sent.

      - **roleArn** *(string) --*

        The ARN of the role which has a policy that grants IoT Analytics permission to send
        message data via IoT Analytics (iotanalytics:BatchPutMessage).

    - **iotEvents** *(dict) --*

      Sends an input to an AWS IoT Events detector.

      - **inputName** *(string) --* **[REQUIRED]**

        The name of the AWS IoT Events input.

      - **messageId** *(string) --*

        [Optional] Use this to ensure that only one input (message) with a given messageId will
        be processed by an AWS IoT Events detector.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events
        detector. ("Action":"iotevents:BatchPutMessage").

    - **stepFunctions** *(dict) --*

      Starts execution of a Step Functions state machine.

      - **executionNamePrefix** *(string) --*

        (Optional) A name will be given to the state machine execution consisting of this prefix
        followed by a UUID. Step Functions automatically creates a unique name for each state
        machine execution if one is not provided.

      - **stateMachineName** *(string) --* **[REQUIRED]**

        The name of the Step Functions state machine whose execution will be started.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role that grants IoT permission to start execution of a state machine
        ("Action":"states:StartExecution").
    """


_ClientCreateTopicRuletopicRulePayloaderrorActioncloudwatchAlarmTypeDef = TypedDict(
    "_ClientCreateTopicRuletopicRulePayloaderrorActioncloudwatchAlarmTypeDef",
    {"roleArn": str, "alarmName": str, "stateReason": str, "stateValue": str},
)


class ClientCreateTopicRuletopicRulePayloaderrorActioncloudwatchAlarmTypeDef(
    _ClientCreateTopicRuletopicRulePayloaderrorActioncloudwatchAlarmTypeDef
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloaderrorAction` `cloudwatchAlarm`

    Change the state of a CloudWatch alarm.

    - **roleArn** *(string) --* **[REQUIRED]**

      The IAM role that allows access to the CloudWatch alarm.

    - **alarmName** *(string) --* **[REQUIRED]**

      The CloudWatch alarm name.

    - **stateReason** *(string) --* **[REQUIRED]**

      The reason for the alarm change.

    - **stateValue** *(string) --* **[REQUIRED]**

      The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
    """


_RequiredClientCreateTopicRuletopicRulePayloaderrorActioncloudwatchMetricTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloaderrorActioncloudwatchMetricTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
    },
)
_OptionalClientCreateTopicRuletopicRulePayloaderrorActioncloudwatchMetricTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloaderrorActioncloudwatchMetricTypeDef",
    {"metricTimestamp": str},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloaderrorActioncloudwatchMetricTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloaderrorActioncloudwatchMetricTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloaderrorActioncloudwatchMetricTypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloaderrorAction` `cloudwatchMetric`

    Capture a CloudWatch metric.

    - **roleArn** *(string) --* **[REQUIRED]**

      The IAM role that allows access to the CloudWatch metric.

    - **metricNamespace** *(string) --* **[REQUIRED]**

      The CloudWatch metric namespace name.

    - **metricName** *(string) --* **[REQUIRED]**

      The CloudWatch metric name.

    - **metricValue** *(string) --* **[REQUIRED]**

      The CloudWatch metric value.

    - **metricUnit** *(string) --* **[REQUIRED]**

      The `metric unit
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
      supported by CloudWatch.

    - **metricTimestamp** *(string) --*

      An optional `Unix timestamp
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
      .
    """


_RequiredClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBTypeDef",
    {"tableName": str, "roleArn": str, "hashKeyField": str, "hashKeyValue": str},
)
_OptionalClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBTypeDef",
    {
        "operation": str,
        "hashKeyType": str,
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": str,
        "payloadField": str,
    },
    total=False,
)


class ClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBTypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloaderrorAction` `dynamoDB`

    Write to a DynamoDB table.

    - **tableName** *(string) --* **[REQUIRED]**

      The name of the DynamoDB table.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access to the DynamoDB table.

    - **operation** *(string) --*

      The type of operation to be performed. This follows the substitution template, so it can be
      ``${operation}`` , but the substitution must result in one of the following: ``INSERT`` ,
      ``UPDATE`` , or ``DELETE`` .

    - **hashKeyField** *(string) --* **[REQUIRED]**

      The hash key name.

    - **hashKeyValue** *(string) --* **[REQUIRED]**

      The hash key value.

    - **hashKeyType** *(string) --*

      The hash key type. Valid values are "STRING" or "NUMBER"

    - **rangeKeyField** *(string) --*

      The range key name.

    - **rangeKeyValue** *(string) --*

      The range key value.

    - **rangeKeyType** *(string) --*

      The range key type. Valid values are "STRING" or "NUMBER"

    - **payloadField** *(string) --*

      The action payload. This name can be customized.
    """


_ClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBv2putItemTypeDef = TypedDict(
    "_ClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBv2putItemTypeDef",
    {"tableName": str},
)


class ClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBv2putItemTypeDef(
    _ClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBv2putItemTypeDef
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBv2` `putItem`

    Specifies the DynamoDB table to which the message data will be written. For example:

     ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
     "my-table" } } }``

    Each attribute in the message payload will be written to a separate column in the DynamoDB
    database.

    - **tableName** *(string) --* **[REQUIRED]**

      The table where the message data will be written.
    """


_ClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBv2TypeDef = TypedDict(
    "_ClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBv2TypeDef",
    {
        "roleArn": str,
        "putItem": ClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBv2putItemTypeDef,
    },
)


class ClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBv2TypeDef(
    _ClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBv2TypeDef
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloaderrorAction` `dynamoDBv2`

    Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to
    write each attribute in an MQTT message payload into a separate DynamoDB column.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access to the DynamoDB table.

    - **putItem** *(dict) --* **[REQUIRED]**

      Specifies the DynamoDB table to which the message data will be written. For example:

       ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
       "my-table" } } }``

      Each attribute in the message payload will be written to a separate column in the DynamoDB
      database.

      - **tableName** *(string) --* **[REQUIRED]**

        The table where the message data will be written.
    """


_ClientCreateTopicRuletopicRulePayloaderrorActionelasticsearchTypeDef = TypedDict(
    "_ClientCreateTopicRuletopicRulePayloaderrorActionelasticsearchTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
)


class ClientCreateTopicRuletopicRulePayloaderrorActionelasticsearchTypeDef(
    _ClientCreateTopicRuletopicRulePayloaderrorActionelasticsearchTypeDef
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloaderrorAction` `elasticsearch`

    Write data to an Amazon Elasticsearch Service domain.

    - **roleArn** *(string) --* **[REQUIRED]**

      The IAM role ARN that has access to Elasticsearch.

    - **endpoint** *(string) --* **[REQUIRED]**

      The endpoint of your Elasticsearch domain.

    - **index** *(string) --* **[REQUIRED]**

      The Elasticsearch index where you want to store your data.

    - **type** *(string) --* **[REQUIRED]**

      The type of document you are storing.

    - **id** *(string) --* **[REQUIRED]**

      The unique identifier for the document you are storing.
    """


_RequiredClientCreateTopicRuletopicRulePayloaderrorActionfirehoseTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloaderrorActionfirehoseTypeDef",
    {"roleArn": str, "deliveryStreamName": str},
)
_OptionalClientCreateTopicRuletopicRulePayloaderrorActionfirehoseTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloaderrorActionfirehoseTypeDef",
    {"separator": str},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloaderrorActionfirehoseTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloaderrorActionfirehoseTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloaderrorActionfirehoseTypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloaderrorAction` `firehose`

    Write to an Amazon Kinesis Firehose stream.

    - **roleArn** *(string) --* **[REQUIRED]**

      The IAM role that grants access to the Amazon Kinesis Firehose stream.

    - **deliveryStreamName** *(string) --* **[REQUIRED]**

      The delivery stream name.

    - **separator** *(string) --*

      A character separator that will be used to separate records written to the Firehose stream.
      Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientCreateTopicRuletopicRulePayloaderrorActioniotAnalyticsTypeDef = TypedDict(
    "_ClientCreateTopicRuletopicRulePayloaderrorActioniotAnalyticsTypeDef",
    {"channelArn": str, "channelName": str, "roleArn": str},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloaderrorActioniotAnalyticsTypeDef(
    _ClientCreateTopicRuletopicRulePayloaderrorActioniotAnalyticsTypeDef
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloaderrorAction` `iotAnalytics`

    Sends message data to an AWS IoT Analytics channel.

    - **channelArn** *(string) --*

      (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

    - **channelName** *(string) --*

      The name of the IoT Analytics channel to which message data will be sent.

    - **roleArn** *(string) --*

      The ARN of the role which has a policy that grants IoT Analytics permission to send message
      data via IoT Analytics (iotanalytics:BatchPutMessage).
    """


_RequiredClientCreateTopicRuletopicRulePayloaderrorActioniotEventsTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloaderrorActioniotEventsTypeDef",
    {"inputName": str, "roleArn": str},
)
_OptionalClientCreateTopicRuletopicRulePayloaderrorActioniotEventsTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloaderrorActioniotEventsTypeDef",
    {"messageId": str},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloaderrorActioniotEventsTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloaderrorActioniotEventsTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloaderrorActioniotEventsTypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloaderrorAction` `iotEvents`

    Sends an input to an AWS IoT Events detector.

    - **inputName** *(string) --* **[REQUIRED]**

      The name of the AWS IoT Events input.

    - **messageId** *(string) --*

      [Optional] Use this to ensure that only one input (message) with a given messageId will be
      processed by an AWS IoT Events detector.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events
      detector. ("Action":"iotevents:BatchPutMessage").
    """


_RequiredClientCreateTopicRuletopicRulePayloaderrorActionkinesisTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloaderrorActionkinesisTypeDef",
    {"roleArn": str, "streamName": str},
)
_OptionalClientCreateTopicRuletopicRulePayloaderrorActionkinesisTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloaderrorActionkinesisTypeDef",
    {"partitionKey": str},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloaderrorActionkinesisTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloaderrorActionkinesisTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloaderrorActionkinesisTypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloaderrorAction` `kinesis`

    Write data to an Amazon Kinesis stream.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access to the Amazon Kinesis stream.

    - **streamName** *(string) --* **[REQUIRED]**

      The name of the Amazon Kinesis stream.

    - **partitionKey** *(string) --*

      The partition key.
    """


_ClientCreateTopicRuletopicRulePayloaderrorActionlambdaTypeDef = TypedDict(
    "_ClientCreateTopicRuletopicRulePayloaderrorActionlambdaTypeDef",
    {"functionArn": str},
)


class ClientCreateTopicRuletopicRulePayloaderrorActionlambdaTypeDef(
    _ClientCreateTopicRuletopicRulePayloaderrorActionlambdaTypeDef
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloaderrorAction` `lambda`

    Invoke a Lambda function.

    - **functionArn** *(string) --* **[REQUIRED]**

      The ARN of the Lambda function.
    """


_RequiredClientCreateTopicRuletopicRulePayloaderrorActionrepublishTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloaderrorActionrepublishTypeDef",
    {"roleArn": str, "topic": str},
)
_OptionalClientCreateTopicRuletopicRulePayloaderrorActionrepublishTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloaderrorActionrepublishTypeDef",
    {"qos": int},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloaderrorActionrepublishTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloaderrorActionrepublishTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloaderrorActionrepublishTypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloaderrorAction` `republish`

    Publish to another MQTT topic.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access.

    - **topic** *(string) --* **[REQUIRED]**

      The name of the MQTT topic.

    - **qos** *(integer) --*

      The Quality of Service (QoS) level to use when republishing messages. The default value is
      0.
    """


_RequiredClientCreateTopicRuletopicRulePayloaderrorActions3TypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloaderrorActions3TypeDef",
    {"roleArn": str, "bucketName": str, "key": str},
)
_OptionalClientCreateTopicRuletopicRulePayloaderrorActions3TypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloaderrorActions3TypeDef",
    {"cannedAcl": str},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloaderrorActions3TypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloaderrorActions3TypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloaderrorActions3TypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloaderrorAction` `s3`

    Write to an Amazon S3 bucket.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access.

    - **bucketName** *(string) --* **[REQUIRED]**

      The Amazon S3 bucket.

    - **key** *(string) --* **[REQUIRED]**

      The object key.

    - **cannedAcl** *(string) --*

      The Amazon S3 canned ACL that controls access to the object identified by the object key.
      For more information, see `S3 canned ACLs
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .
    """


_ClientCreateTopicRuletopicRulePayloaderrorActionsalesforceTypeDef = TypedDict(
    "_ClientCreateTopicRuletopicRulePayloaderrorActionsalesforceTypeDef",
    {"token": str, "url": str},
)


class ClientCreateTopicRuletopicRulePayloaderrorActionsalesforceTypeDef(
    _ClientCreateTopicRuletopicRulePayloaderrorActionsalesforceTypeDef
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloaderrorAction` `salesforce`

    Send a message to a Salesforce IoT Cloud Input Stream.

    - **token** *(string) --* **[REQUIRED]**

      The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token
      is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

    - **url** *(string) --* **[REQUIRED]**

      The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the
      Salesforce IoT Cloud platform after creation of the Input Stream.
    """


_RequiredClientCreateTopicRuletopicRulePayloaderrorActionsnsTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloaderrorActionsnsTypeDef",
    {"targetArn": str, "roleArn": str},
)
_OptionalClientCreateTopicRuletopicRulePayloaderrorActionsnsTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloaderrorActionsnsTypeDef",
    {"messageFormat": str},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloaderrorActionsnsTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloaderrorActionsnsTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloaderrorActionsnsTypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloaderrorAction` `sns`

    Publish to an Amazon SNS topic.

    - **targetArn** *(string) --* **[REQUIRED]**

      The ARN of the SNS topic.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access.

    - **messageFormat** *(string) --*

      (Optional) The message format of the message to publish. Accepted values are "JSON" and
      "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if
      the payload should be parsed and relevant platform-specific bits of the payload should be
      extracted. To read more about SNS message formats, see
      `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
      <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official
      documentation.
    """


_RequiredClientCreateTopicRuletopicRulePayloaderrorActionsqsTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloaderrorActionsqsTypeDef",
    {"roleArn": str, "queueUrl": str},
)
_OptionalClientCreateTopicRuletopicRulePayloaderrorActionsqsTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloaderrorActionsqsTypeDef",
    {"useBase64": bool},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloaderrorActionsqsTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloaderrorActionsqsTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloaderrorActionsqsTypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloaderrorAction` `sqs`

    Publish to an Amazon SQS queue.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access.

    - **queueUrl** *(string) --* **[REQUIRED]**

      The URL of the Amazon SQS queue.

    - **useBase64** *(boolean) --*

      Specifies whether to use Base64 encoding.
    """


_RequiredClientCreateTopicRuletopicRulePayloaderrorActionstepFunctionsTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloaderrorActionstepFunctionsTypeDef",
    {"stateMachineName": str, "roleArn": str},
)
_OptionalClientCreateTopicRuletopicRulePayloaderrorActionstepFunctionsTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloaderrorActionstepFunctionsTypeDef",
    {"executionNamePrefix": str},
    total=False,
)


class ClientCreateTopicRuletopicRulePayloaderrorActionstepFunctionsTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloaderrorActionstepFunctionsTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloaderrorActionstepFunctionsTypeDef,
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayloaderrorAction` `stepFunctions`

    Starts execution of a Step Functions state machine.

    - **executionNamePrefix** *(string) --*

      (Optional) A name will be given to the state machine execution consisting of this prefix
      followed by a UUID. Step Functions automatically creates a unique name for each state
      machine execution if one is not provided.

    - **stateMachineName** *(string) --* **[REQUIRED]**

      The name of the Step Functions state machine whose execution will be started.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that grants IoT permission to start execution of a state machine
      ("Action":"states:StartExecution").
    """


_ClientCreateTopicRuletopicRulePayloaderrorActionTypeDef = TypedDict(
    "_ClientCreateTopicRuletopicRulePayloaderrorActionTypeDef",
    {
        "dynamoDB": ClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBTypeDef,
        "dynamoDBv2": ClientCreateTopicRuletopicRulePayloaderrorActiondynamoDBv2TypeDef,
        "lambda": ClientCreateTopicRuletopicRulePayloaderrorActionlambdaTypeDef,
        "sns": ClientCreateTopicRuletopicRulePayloaderrorActionsnsTypeDef,
        "sqs": ClientCreateTopicRuletopicRulePayloaderrorActionsqsTypeDef,
        "kinesis": ClientCreateTopicRuletopicRulePayloaderrorActionkinesisTypeDef,
        "republish": ClientCreateTopicRuletopicRulePayloaderrorActionrepublishTypeDef,
        "s3": ClientCreateTopicRuletopicRulePayloaderrorActions3TypeDef,
        "firehose": ClientCreateTopicRuletopicRulePayloaderrorActionfirehoseTypeDef,
        "cloudwatchMetric": ClientCreateTopicRuletopicRulePayloaderrorActioncloudwatchMetricTypeDef,
        "cloudwatchAlarm": ClientCreateTopicRuletopicRulePayloaderrorActioncloudwatchAlarmTypeDef,
        "elasticsearch": ClientCreateTopicRuletopicRulePayloaderrorActionelasticsearchTypeDef,
        "salesforce": ClientCreateTopicRuletopicRulePayloaderrorActionsalesforceTypeDef,
        "iotAnalytics": ClientCreateTopicRuletopicRulePayloaderrorActioniotAnalyticsTypeDef,
        "iotEvents": ClientCreateTopicRuletopicRulePayloaderrorActioniotEventsTypeDef,
        "stepFunctions": ClientCreateTopicRuletopicRulePayloaderrorActionstepFunctionsTypeDef,
    },
    total=False,
)


class ClientCreateTopicRuletopicRulePayloaderrorActionTypeDef(
    _ClientCreateTopicRuletopicRulePayloaderrorActionTypeDef
):
    """
    Type definition for `ClientCreateTopicRuletopicRulePayload` `errorAction`

    The action to take when an error occurs.

    - **dynamoDB** *(dict) --*

      Write to a DynamoDB table.

      - **tableName** *(string) --* **[REQUIRED]**

        The name of the DynamoDB table.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access to the DynamoDB table.

      - **operation** *(string) --*

        The type of operation to be performed. This follows the substitution template, so it can be
        ``${operation}`` , but the substitution must result in one of the following: ``INSERT`` ,
        ``UPDATE`` , or ``DELETE`` .

      - **hashKeyField** *(string) --* **[REQUIRED]**

        The hash key name.

      - **hashKeyValue** *(string) --* **[REQUIRED]**

        The hash key value.

      - **hashKeyType** *(string) --*

        The hash key type. Valid values are "STRING" or "NUMBER"

      - **rangeKeyField** *(string) --*

        The range key name.

      - **rangeKeyValue** *(string) --*

        The range key value.

      - **rangeKeyType** *(string) --*

        The range key type. Valid values are "STRING" or "NUMBER"

      - **payloadField** *(string) --*

        The action payload. This name can be customized.

    - **dynamoDBv2** *(dict) --*

      Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to
      write each attribute in an MQTT message payload into a separate DynamoDB column.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access to the DynamoDB table.

      - **putItem** *(dict) --* **[REQUIRED]**

        Specifies the DynamoDB table to which the message data will be written. For example:

         ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
         "my-table" } } }``

        Each attribute in the message payload will be written to a separate column in the DynamoDB
        database.

        - **tableName** *(string) --* **[REQUIRED]**

          The table where the message data will be written.

    - **lambda** *(dict) --*

      Invoke a Lambda function.

      - **functionArn** *(string) --* **[REQUIRED]**

        The ARN of the Lambda function.

    - **sns** *(dict) --*

      Publish to an Amazon SNS topic.

      - **targetArn** *(string) --* **[REQUIRED]**

        The ARN of the SNS topic.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access.

      - **messageFormat** *(string) --*

        (Optional) The message format of the message to publish. Accepted values are "JSON" and
        "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if
        the payload should be parsed and relevant platform-specific bits of the payload should be
        extracted. To read more about SNS message formats, see
        `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
        <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official
        documentation.

    - **sqs** *(dict) --*

      Publish to an Amazon SQS queue.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access.

      - **queueUrl** *(string) --* **[REQUIRED]**

        The URL of the Amazon SQS queue.

      - **useBase64** *(boolean) --*

        Specifies whether to use Base64 encoding.

    - **kinesis** *(dict) --*

      Write data to an Amazon Kinesis stream.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access to the Amazon Kinesis stream.

      - **streamName** *(string) --* **[REQUIRED]**

        The name of the Amazon Kinesis stream.

      - **partitionKey** *(string) --*

        The partition key.

    - **republish** *(dict) --*

      Publish to another MQTT topic.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access.

      - **topic** *(string) --* **[REQUIRED]**

        The name of the MQTT topic.

      - **qos** *(integer) --*

        The Quality of Service (QoS) level to use when republishing messages. The default value is
        0.

    - **s3** *(dict) --*

      Write to an Amazon S3 bucket.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access.

      - **bucketName** *(string) --* **[REQUIRED]**

        The Amazon S3 bucket.

      - **key** *(string) --* **[REQUIRED]**

        The object key.

      - **cannedAcl** *(string) --*

        The Amazon S3 canned ACL that controls access to the object identified by the object key.
        For more information, see `S3 canned ACLs
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

    - **firehose** *(dict) --*

      Write to an Amazon Kinesis Firehose stream.

      - **roleArn** *(string) --* **[REQUIRED]**

        The IAM role that grants access to the Amazon Kinesis Firehose stream.

      - **deliveryStreamName** *(string) --* **[REQUIRED]**

        The delivery stream name.

      - **separator** *(string) --*

        A character separator that will be used to separate records written to the Firehose stream.
        Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

    - **cloudwatchMetric** *(dict) --*

      Capture a CloudWatch metric.

      - **roleArn** *(string) --* **[REQUIRED]**

        The IAM role that allows access to the CloudWatch metric.

      - **metricNamespace** *(string) --* **[REQUIRED]**

        The CloudWatch metric namespace name.

      - **metricName** *(string) --* **[REQUIRED]**

        The CloudWatch metric name.

      - **metricValue** *(string) --* **[REQUIRED]**

        The CloudWatch metric value.

      - **metricUnit** *(string) --* **[REQUIRED]**

        The `metric unit
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
        supported by CloudWatch.

      - **metricTimestamp** *(string) --*

        An optional `Unix timestamp
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
        .

    - **cloudwatchAlarm** *(dict) --*

      Change the state of a CloudWatch alarm.

      - **roleArn** *(string) --* **[REQUIRED]**

        The IAM role that allows access to the CloudWatch alarm.

      - **alarmName** *(string) --* **[REQUIRED]**

        The CloudWatch alarm name.

      - **stateReason** *(string) --* **[REQUIRED]**

        The reason for the alarm change.

      - **stateValue** *(string) --* **[REQUIRED]**

        The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

    - **elasticsearch** *(dict) --*

      Write data to an Amazon Elasticsearch Service domain.

      - **roleArn** *(string) --* **[REQUIRED]**

        The IAM role ARN that has access to Elasticsearch.

      - **endpoint** *(string) --* **[REQUIRED]**

        The endpoint of your Elasticsearch domain.

      - **index** *(string) --* **[REQUIRED]**

        The Elasticsearch index where you want to store your data.

      - **type** *(string) --* **[REQUIRED]**

        The type of document you are storing.

      - **id** *(string) --* **[REQUIRED]**

        The unique identifier for the document you are storing.

    - **salesforce** *(dict) --*

      Send a message to a Salesforce IoT Cloud Input Stream.

      - **token** *(string) --* **[REQUIRED]**

        The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token
        is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

      - **url** *(string) --* **[REQUIRED]**

        The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the
        Salesforce IoT Cloud platform after creation of the Input Stream.

    - **iotAnalytics** *(dict) --*

      Sends message data to an AWS IoT Analytics channel.

      - **channelArn** *(string) --*

        (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

      - **channelName** *(string) --*

        The name of the IoT Analytics channel to which message data will be sent.

      - **roleArn** *(string) --*

        The ARN of the role which has a policy that grants IoT Analytics permission to send message
        data via IoT Analytics (iotanalytics:BatchPutMessage).

    - **iotEvents** *(dict) --*

      Sends an input to an AWS IoT Events detector.

      - **inputName** *(string) --* **[REQUIRED]**

        The name of the AWS IoT Events input.

      - **messageId** *(string) --*

        [Optional] Use this to ensure that only one input (message) with a given messageId will be
        processed by an AWS IoT Events detector.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events
        detector. ("Action":"iotevents:BatchPutMessage").

    - **stepFunctions** *(dict) --*

      Starts execution of a Step Functions state machine.

      - **executionNamePrefix** *(string) --*

        (Optional) A name will be given to the state machine execution consisting of this prefix
        followed by a UUID. Step Functions automatically creates a unique name for each state
        machine execution if one is not provided.

      - **stateMachineName** *(string) --* **[REQUIRED]**

        The name of the Step Functions state machine whose execution will be started.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role that grants IoT permission to start execution of a state machine
        ("Action":"states:StartExecution").
    """


_RequiredClientCreateTopicRuletopicRulePayloadTypeDef = TypedDict(
    "_RequiredClientCreateTopicRuletopicRulePayloadTypeDef",
    {"sql": str, "actions": List[ClientCreateTopicRuletopicRulePayloadactionsTypeDef]},
)
_OptionalClientCreateTopicRuletopicRulePayloadTypeDef = TypedDict(
    "_OptionalClientCreateTopicRuletopicRulePayloadTypeDef",
    {
        "description": str,
        "ruleDisabled": bool,
        "awsIotSqlVersion": str,
        "errorAction": ClientCreateTopicRuletopicRulePayloaderrorActionTypeDef,
    },
    total=False,
)


class ClientCreateTopicRuletopicRulePayloadTypeDef(
    _RequiredClientCreateTopicRuletopicRulePayloadTypeDef,
    _OptionalClientCreateTopicRuletopicRulePayloadTypeDef,
):
    """
    Type definition for `ClientCreateTopicRule` `topicRulePayload`

    The rule payload.

    - **sql** *(string) --* **[REQUIRED]**

      The SQL statement used to query the topic. For more information, see `AWS IoT SQL Reference
      <https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference>`__
      in the *AWS IoT Developer Guide* .

    - **description** *(string) --*

      The description of the rule.

    - **actions** *(list) --* **[REQUIRED]**

      The actions associated with the rule.

      - *(dict) --*

        Describes the actions associated with a rule.

        - **dynamoDB** *(dict) --*

          Write to a DynamoDB table.

          - **tableName** *(string) --* **[REQUIRED]**

            The name of the DynamoDB table.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the IAM role that grants access to the DynamoDB table.

          - **operation** *(string) --*

            The type of operation to be performed. This follows the substitution template, so it can
            be ``${operation}`` , but the substitution must result in one of the following:
            ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

          - **hashKeyField** *(string) --* **[REQUIRED]**

            The hash key name.

          - **hashKeyValue** *(string) --* **[REQUIRED]**

            The hash key value.

          - **hashKeyType** *(string) --*

            The hash key type. Valid values are "STRING" or "NUMBER"

          - **rangeKeyField** *(string) --*

            The range key name.

          - **rangeKeyValue** *(string) --*

            The range key value.

          - **rangeKeyType** *(string) --*

            The range key type. Valid values are "STRING" or "NUMBER"

          - **payloadField** *(string) --*

            The action payload. This name can be customized.

        - **dynamoDBv2** *(dict) --*

          Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to
          write each attribute in an MQTT message payload into a separate DynamoDB column.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the IAM role that grants access to the DynamoDB table.

          - **putItem** *(dict) --* **[REQUIRED]**

            Specifies the DynamoDB table to which the message data will be written. For example:

             ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
             "my-table" } } }``

            Each attribute in the message payload will be written to a separate column in the
            DynamoDB database.

            - **tableName** *(string) --* **[REQUIRED]**

              The table where the message data will be written.

        - **lambda** *(dict) --*

          Invoke a Lambda function.

          - **functionArn** *(string) --* **[REQUIRED]**

            The ARN of the Lambda function.

        - **sns** *(dict) --*

          Publish to an Amazon SNS topic.

          - **targetArn** *(string) --* **[REQUIRED]**

            The ARN of the SNS topic.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the IAM role that grants access.

          - **messageFormat** *(string) --*

            (Optional) The message format of the message to publish. Accepted values are "JSON" and
            "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if
            the payload should be parsed and relevant platform-specific bits of the payload should be
            extracted. To read more about SNS message formats, see
            `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
            <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official
            documentation.

        - **sqs** *(dict) --*

          Publish to an Amazon SQS queue.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the IAM role that grants access.

          - **queueUrl** *(string) --* **[REQUIRED]**

            The URL of the Amazon SQS queue.

          - **useBase64** *(boolean) --*

            Specifies whether to use Base64 encoding.

        - **kinesis** *(dict) --*

          Write data to an Amazon Kinesis stream.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the IAM role that grants access to the Amazon Kinesis stream.

          - **streamName** *(string) --* **[REQUIRED]**

            The name of the Amazon Kinesis stream.

          - **partitionKey** *(string) --*

            The partition key.

        - **republish** *(dict) --*

          Publish to another MQTT topic.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the IAM role that grants access.

          - **topic** *(string) --* **[REQUIRED]**

            The name of the MQTT topic.

          - **qos** *(integer) --*

            The Quality of Service (QoS) level to use when republishing messages. The default value
            is 0.

        - **s3** *(dict) --*

          Write to an Amazon S3 bucket.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the IAM role that grants access.

          - **bucketName** *(string) --* **[REQUIRED]**

            The Amazon S3 bucket.

          - **key** *(string) --* **[REQUIRED]**

            The object key.

          - **cannedAcl** *(string) --*

            The Amazon S3 canned ACL that controls access to the object identified by the object key.
            For more information, see `S3 canned ACLs
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

        - **firehose** *(dict) --*

          Write to an Amazon Kinesis Firehose stream.

          - **roleArn** *(string) --* **[REQUIRED]**

            The IAM role that grants access to the Amazon Kinesis Firehose stream.

          - **deliveryStreamName** *(string) --* **[REQUIRED]**

            The delivery stream name.

          - **separator** *(string) --*

            A character separator that will be used to separate records written to the Firehose
            stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ','
            (comma).

        - **cloudwatchMetric** *(dict) --*

          Capture a CloudWatch metric.

          - **roleArn** *(string) --* **[REQUIRED]**

            The IAM role that allows access to the CloudWatch metric.

          - **metricNamespace** *(string) --* **[REQUIRED]**

            The CloudWatch metric namespace name.

          - **metricName** *(string) --* **[REQUIRED]**

            The CloudWatch metric name.

          - **metricValue** *(string) --* **[REQUIRED]**

            The CloudWatch metric value.

          - **metricUnit** *(string) --* **[REQUIRED]**

            The `metric unit
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
            supported by CloudWatch.

          - **metricTimestamp** *(string) --*

            An optional `Unix timestamp
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
            .

        - **cloudwatchAlarm** *(dict) --*

          Change the state of a CloudWatch alarm.

          - **roleArn** *(string) --* **[REQUIRED]**

            The IAM role that allows access to the CloudWatch alarm.

          - **alarmName** *(string) --* **[REQUIRED]**

            The CloudWatch alarm name.

          - **stateReason** *(string) --* **[REQUIRED]**

            The reason for the alarm change.

          - **stateValue** *(string) --* **[REQUIRED]**

            The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

        - **elasticsearch** *(dict) --*

          Write data to an Amazon Elasticsearch Service domain.

          - **roleArn** *(string) --* **[REQUIRED]**

            The IAM role ARN that has access to Elasticsearch.

          - **endpoint** *(string) --* **[REQUIRED]**

            The endpoint of your Elasticsearch domain.

          - **index** *(string) --* **[REQUIRED]**

            The Elasticsearch index where you want to store your data.

          - **type** *(string) --* **[REQUIRED]**

            The type of document you are storing.

          - **id** *(string) --* **[REQUIRED]**

            The unique identifier for the document you are storing.

        - **salesforce** *(dict) --*

          Send a message to a Salesforce IoT Cloud Input Stream.

          - **token** *(string) --* **[REQUIRED]**

            The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token
            is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

          - **url** *(string) --* **[REQUIRED]**

            The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the
            Salesforce IoT Cloud platform after creation of the Input Stream.

        - **iotAnalytics** *(dict) --*

          Sends message data to an AWS IoT Analytics channel.

          - **channelArn** *(string) --*

            (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

          - **channelName** *(string) --*

            The name of the IoT Analytics channel to which message data will be sent.

          - **roleArn** *(string) --*

            The ARN of the role which has a policy that grants IoT Analytics permission to send
            message data via IoT Analytics (iotanalytics:BatchPutMessage).

        - **iotEvents** *(dict) --*

          Sends an input to an AWS IoT Events detector.

          - **inputName** *(string) --* **[REQUIRED]**

            The name of the AWS IoT Events input.

          - **messageId** *(string) --*

            [Optional] Use this to ensure that only one input (message) with a given messageId will
            be processed by an AWS IoT Events detector.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events
            detector. ("Action":"iotevents:BatchPutMessage").

        - **stepFunctions** *(dict) --*

          Starts execution of a Step Functions state machine.

          - **executionNamePrefix** *(string) --*

            (Optional) A name will be given to the state machine execution consisting of this prefix
            followed by a UUID. Step Functions automatically creates a unique name for each state
            machine execution if one is not provided.

          - **stateMachineName** *(string) --* **[REQUIRED]**

            The name of the Step Functions state machine whose execution will be started.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the role that grants IoT permission to start execution of a state machine
            ("Action":"states:StartExecution").

    - **ruleDisabled** *(boolean) --*

      Specifies whether the rule is disabled.

    - **awsIotSqlVersion** *(string) --*

      The version of the SQL rules engine to use when evaluating the rule.

    - **errorAction** *(dict) --*

      The action to take when an error occurs.

      - **dynamoDB** *(dict) --*

        Write to a DynamoDB table.

        - **tableName** *(string) --* **[REQUIRED]**

          The name of the DynamoDB table.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the IAM role that grants access to the DynamoDB table.

        - **operation** *(string) --*

          The type of operation to be performed. This follows the substitution template, so it can be
          ``${operation}`` , but the substitution must result in one of the following: ``INSERT`` ,
          ``UPDATE`` , or ``DELETE`` .

        - **hashKeyField** *(string) --* **[REQUIRED]**

          The hash key name.

        - **hashKeyValue** *(string) --* **[REQUIRED]**

          The hash key value.

        - **hashKeyType** *(string) --*

          The hash key type. Valid values are "STRING" or "NUMBER"

        - **rangeKeyField** *(string) --*

          The range key name.

        - **rangeKeyValue** *(string) --*

          The range key value.

        - **rangeKeyType** *(string) --*

          The range key type. Valid values are "STRING" or "NUMBER"

        - **payloadField** *(string) --*

          The action payload. This name can be customized.

      - **dynamoDBv2** *(dict) --*

        Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to
        write each attribute in an MQTT message payload into a separate DynamoDB column.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the IAM role that grants access to the DynamoDB table.

        - **putItem** *(dict) --* **[REQUIRED]**

          Specifies the DynamoDB table to which the message data will be written. For example:

           ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
           "my-table" } } }``

          Each attribute in the message payload will be written to a separate column in the DynamoDB
          database.

          - **tableName** *(string) --* **[REQUIRED]**

            The table where the message data will be written.

      - **lambda** *(dict) --*

        Invoke a Lambda function.

        - **functionArn** *(string) --* **[REQUIRED]**

          The ARN of the Lambda function.

      - **sns** *(dict) --*

        Publish to an Amazon SNS topic.

        - **targetArn** *(string) --* **[REQUIRED]**

          The ARN of the SNS topic.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the IAM role that grants access.

        - **messageFormat** *(string) --*

          (Optional) The message format of the message to publish. Accepted values are "JSON" and
          "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if
          the payload should be parsed and relevant platform-specific bits of the payload should be
          extracted. To read more about SNS message formats, see
          `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
          <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official
          documentation.

      - **sqs** *(dict) --*

        Publish to an Amazon SQS queue.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the IAM role that grants access.

        - **queueUrl** *(string) --* **[REQUIRED]**

          The URL of the Amazon SQS queue.

        - **useBase64** *(boolean) --*

          Specifies whether to use Base64 encoding.

      - **kinesis** *(dict) --*

        Write data to an Amazon Kinesis stream.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the IAM role that grants access to the Amazon Kinesis stream.

        - **streamName** *(string) --* **[REQUIRED]**

          The name of the Amazon Kinesis stream.

        - **partitionKey** *(string) --*

          The partition key.

      - **republish** *(dict) --*

        Publish to another MQTT topic.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the IAM role that grants access.

        - **topic** *(string) --* **[REQUIRED]**

          The name of the MQTT topic.

        - **qos** *(integer) --*

          The Quality of Service (QoS) level to use when republishing messages. The default value is
          0.

      - **s3** *(dict) --*

        Write to an Amazon S3 bucket.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the IAM role that grants access.

        - **bucketName** *(string) --* **[REQUIRED]**

          The Amazon S3 bucket.

        - **key** *(string) --* **[REQUIRED]**

          The object key.

        - **cannedAcl** *(string) --*

          The Amazon S3 canned ACL that controls access to the object identified by the object key.
          For more information, see `S3 canned ACLs
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

      - **firehose** *(dict) --*

        Write to an Amazon Kinesis Firehose stream.

        - **roleArn** *(string) --* **[REQUIRED]**

          The IAM role that grants access to the Amazon Kinesis Firehose stream.

        - **deliveryStreamName** *(string) --* **[REQUIRED]**

          The delivery stream name.

        - **separator** *(string) --*

          A character separator that will be used to separate records written to the Firehose stream.
          Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

      - **cloudwatchMetric** *(dict) --*

        Capture a CloudWatch metric.

        - **roleArn** *(string) --* **[REQUIRED]**

          The IAM role that allows access to the CloudWatch metric.

        - **metricNamespace** *(string) --* **[REQUIRED]**

          The CloudWatch metric namespace name.

        - **metricName** *(string) --* **[REQUIRED]**

          The CloudWatch metric name.

        - **metricValue** *(string) --* **[REQUIRED]**

          The CloudWatch metric value.

        - **metricUnit** *(string) --* **[REQUIRED]**

          The `metric unit
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
          supported by CloudWatch.

        - **metricTimestamp** *(string) --*

          An optional `Unix timestamp
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
          .

      - **cloudwatchAlarm** *(dict) --*

        Change the state of a CloudWatch alarm.

        - **roleArn** *(string) --* **[REQUIRED]**

          The IAM role that allows access to the CloudWatch alarm.

        - **alarmName** *(string) --* **[REQUIRED]**

          The CloudWatch alarm name.

        - **stateReason** *(string) --* **[REQUIRED]**

          The reason for the alarm change.

        - **stateValue** *(string) --* **[REQUIRED]**

          The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

      - **elasticsearch** *(dict) --*

        Write data to an Amazon Elasticsearch Service domain.

        - **roleArn** *(string) --* **[REQUIRED]**

          The IAM role ARN that has access to Elasticsearch.

        - **endpoint** *(string) --* **[REQUIRED]**

          The endpoint of your Elasticsearch domain.

        - **index** *(string) --* **[REQUIRED]**

          The Elasticsearch index where you want to store your data.

        - **type** *(string) --* **[REQUIRED]**

          The type of document you are storing.

        - **id** *(string) --* **[REQUIRED]**

          The unique identifier for the document you are storing.

      - **salesforce** *(dict) --*

        Send a message to a Salesforce IoT Cloud Input Stream.

        - **token** *(string) --* **[REQUIRED]**

          The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token
          is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

        - **url** *(string) --* **[REQUIRED]**

          The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the
          Salesforce IoT Cloud platform after creation of the Input Stream.

      - **iotAnalytics** *(dict) --*

        Sends message data to an AWS IoT Analytics channel.

        - **channelArn** *(string) --*

          (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

        - **channelName** *(string) --*

          The name of the IoT Analytics channel to which message data will be sent.

        - **roleArn** *(string) --*

          The ARN of the role which has a policy that grants IoT Analytics permission to send message
          data via IoT Analytics (iotanalytics:BatchPutMessage).

      - **iotEvents** *(dict) --*

        Sends an input to an AWS IoT Events detector.

        - **inputName** *(string) --* **[REQUIRED]**

          The name of the AWS IoT Events input.

        - **messageId** *(string) --*

          [Optional] Use this to ensure that only one input (message) with a given messageId will be
          processed by an AWS IoT Events detector.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events
          detector. ("Action":"iotevents:BatchPutMessage").

      - **stepFunctions** *(dict) --*

        Starts execution of a Step Functions state machine.

        - **executionNamePrefix** *(string) --*

          (Optional) A name will be given to the state machine execution consisting of this prefix
          followed by a UUID. Step Functions automatically creates a unique name for each state
          machine execution if one is not provided.

        - **stateMachineName** *(string) --* **[REQUIRED]**

          The name of the Step Functions state machine whose execution will be started.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the role that grants IoT permission to start execution of a state machine
          ("Action":"states:StartExecution").
    """


_ClientDescribeAccountAuditConfigurationResponseauditCheckConfigurationsTypeDef = TypedDict(
    "_ClientDescribeAccountAuditConfigurationResponseauditCheckConfigurationsTypeDef",
    {"enabled": bool},
    total=False,
)


class ClientDescribeAccountAuditConfigurationResponseauditCheckConfigurationsTypeDef(
    _ClientDescribeAccountAuditConfigurationResponseauditCheckConfigurationsTypeDef
):
    """
    Type definition for `ClientDescribeAccountAuditConfigurationResponse` `auditCheckConfigurations`

    Which audit checks are enabled and disabled for this account.

    - **enabled** *(boolean) --*

      True if this audit check is enabled for this account.
    """


_ClientDescribeAccountAuditConfigurationResponseauditNotificationTargetConfigurationsTypeDef = TypedDict(
    "_ClientDescribeAccountAuditConfigurationResponseauditNotificationTargetConfigurationsTypeDef",
    {"targetArn": str, "roleArn": str, "enabled": bool},
    total=False,
)


class ClientDescribeAccountAuditConfigurationResponseauditNotificationTargetConfigurationsTypeDef(
    _ClientDescribeAccountAuditConfigurationResponseauditNotificationTargetConfigurationsTypeDef
):
    """
    Type definition for `ClientDescribeAccountAuditConfigurationResponse` `auditNotificationTargetConfigurations`

    Information about the targets to which audit notifications are sent.

    - **targetArn** *(string) --*

      The ARN of the target (SNS topic) to which audit notifications are sent.

    - **roleArn** *(string) --*

      The ARN of the role that grants permission to send notifications to the target.

    - **enabled** *(boolean) --*

      True if notifications to the target are enabled.
    """


_ClientDescribeAccountAuditConfigurationResponseTypeDef = TypedDict(
    "_ClientDescribeAccountAuditConfigurationResponseTypeDef",
    {
        "roleArn": str,
        "auditNotificationTargetConfigurations": Dict[
            str,
            ClientDescribeAccountAuditConfigurationResponseauditNotificationTargetConfigurationsTypeDef,
        ],
        "auditCheckConfigurations": Dict[
            str,
            ClientDescribeAccountAuditConfigurationResponseauditCheckConfigurationsTypeDef,
        ],
    },
    total=False,
)


class ClientDescribeAccountAuditConfigurationResponseTypeDef(
    _ClientDescribeAccountAuditConfigurationResponseTypeDef
):
    """
    Type definition for `ClientDescribeAccountAuditConfiguration` `Response`

    - **roleArn** *(string) --*

      The ARN of the role that grants permission to AWS IoT to access information about your
      devices, policies, certificates, and other items as required when performing an audit.

      On the first call to ``UpdateAccountAuditConfiguration`` , this parameter is required.

    - **auditNotificationTargetConfigurations** *(dict) --*

      Information about the targets to which audit notifications are sent for this account.

      - *(string) --*

        - *(dict) --*

          Information about the targets to which audit notifications are sent.

          - **targetArn** *(string) --*

            The ARN of the target (SNS topic) to which audit notifications are sent.

          - **roleArn** *(string) --*

            The ARN of the role that grants permission to send notifications to the target.

          - **enabled** *(boolean) --*

            True if notifications to the target are enabled.

    - **auditCheckConfigurations** *(dict) --*

      Which audit checks are enabled and disabled for this account.

      - *(string) --*

        An audit check name. Checks must be enabled for your account. (Use
        ``DescribeAccountAuditConfiguration`` to see the list of all checks, including those that
        are enabled or use ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)

        - *(dict) --*

          Which audit checks are enabled and disabled for this account.

          - **enabled** *(boolean) --*

            True if this audit check is enabled for this account.
    """


_ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "_ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)


class ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef(
    _ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef
):
    """
    Type definition for `ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifier` `policyVersionIdentifier`

    The version of the policy associated with the resource.

    - **policyName** *(string) --*

      The name of the policy.

    - **policyVersionId** *(string) --*

      The ID of the version of the policy associated with the resource.
    """


_ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierTypeDef = TypedDict(
    "_ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
    },
    total=False,
)


class ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierTypeDef(
    _ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierTypeDef
):
    """
    Type definition for `ClientDescribeAuditFindingResponsefindingnonCompliantResource` `resourceIdentifier`

    Information that identifies the noncompliant resource.

    - **deviceCertificateId** *(string) --*

      The ID of the certificate attached to the resource.

    - **caCertificateId** *(string) --*

      The ID of the CA certificate used to authorize the certificate.

    - **cognitoIdentityPoolId** *(string) --*

      The ID of the Amazon Cognito identity pool.

    - **clientId** *(string) --*

      The client ID.

    - **policyVersionIdentifier** *(dict) --*

      The version of the policy associated with the resource.

      - **policyName** *(string) --*

        The name of the policy.

      - **policyVersionId** *(string) --*

        The ID of the version of the policy associated with the resource.

    - **account** *(string) --*

      The account with which the resource is associated.
    """


_ClientDescribeAuditFindingResponsefindingnonCompliantResourceTypeDef = TypedDict(
    "_ClientDescribeAuditFindingResponsefindingnonCompliantResourceTypeDef",
    {
        "resourceType": str,
        "resourceIdentifier": ClientDescribeAuditFindingResponsefindingnonCompliantResourceresourceIdentifierTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)


class ClientDescribeAuditFindingResponsefindingnonCompliantResourceTypeDef(
    _ClientDescribeAuditFindingResponsefindingnonCompliantResourceTypeDef
):
    """
    Type definition for `ClientDescribeAuditFindingResponsefinding` `nonCompliantResource`

    The resource that was found to be noncompliant with the audit check.

    - **resourceType** *(string) --*

      The type of the noncompliant resource.

    - **resourceIdentifier** *(dict) --*

      Information that identifies the noncompliant resource.

      - **deviceCertificateId** *(string) --*

        The ID of the certificate attached to the resource.

      - **caCertificateId** *(string) --*

        The ID of the CA certificate used to authorize the certificate.

      - **cognitoIdentityPoolId** *(string) --*

        The ID of the Amazon Cognito identity pool.

      - **clientId** *(string) --*

        The client ID.

      - **policyVersionIdentifier** *(dict) --*

        The version of the policy associated with the resource.

        - **policyName** *(string) --*

          The name of the policy.

        - **policyVersionId** *(string) --*

          The ID of the version of the policy associated with the resource.

      - **account** *(string) --*

        The account with which the resource is associated.

    - **additionalInfo** *(dict) --*

      Other information about the noncompliant resource.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "_ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)


class ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef(
    _ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef
):
    """
    Type definition for `ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifier` `policyVersionIdentifier`

    The version of the policy associated with the resource.

    - **policyName** *(string) --*

      The name of the policy.

    - **policyVersionId** *(string) --*

      The ID of the version of the policy associated with the resource.
    """


_ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierTypeDef = TypedDict(
    "_ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
    },
    total=False,
)


class ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierTypeDef(
    _ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierTypeDef
):
    """
    Type definition for `ClientDescribeAuditFindingResponsefindingrelatedResources` `resourceIdentifier`

    Information that identifies the resource.

    - **deviceCertificateId** *(string) --*

      The ID of the certificate attached to the resource.

    - **caCertificateId** *(string) --*

      The ID of the CA certificate used to authorize the certificate.

    - **cognitoIdentityPoolId** *(string) --*

      The ID of the Amazon Cognito identity pool.

    - **clientId** *(string) --*

      The client ID.

    - **policyVersionIdentifier** *(dict) --*

      The version of the policy associated with the resource.

      - **policyName** *(string) --*

        The name of the policy.

      - **policyVersionId** *(string) --*

        The ID of the version of the policy associated with the resource.

    - **account** *(string) --*

      The account with which the resource is associated.
    """


_ClientDescribeAuditFindingResponsefindingrelatedResourcesTypeDef = TypedDict(
    "_ClientDescribeAuditFindingResponsefindingrelatedResourcesTypeDef",
    {
        "resourceType": str,
        "resourceIdentifier": ClientDescribeAuditFindingResponsefindingrelatedResourcesresourceIdentifierTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)


class ClientDescribeAuditFindingResponsefindingrelatedResourcesTypeDef(
    _ClientDescribeAuditFindingResponsefindingrelatedResourcesTypeDef
):
    """
    Type definition for `ClientDescribeAuditFindingResponsefinding` `relatedResources`

    Information about a related resource.

    - **resourceType** *(string) --*

      The type of resource.

    - **resourceIdentifier** *(dict) --*

      Information that identifies the resource.

      - **deviceCertificateId** *(string) --*

        The ID of the certificate attached to the resource.

      - **caCertificateId** *(string) --*

        The ID of the CA certificate used to authorize the certificate.

      - **cognitoIdentityPoolId** *(string) --*

        The ID of the Amazon Cognito identity pool.

      - **clientId** *(string) --*

        The client ID.

      - **policyVersionIdentifier** *(dict) --*

        The version of the policy associated with the resource.

        - **policyName** *(string) --*

          The name of the policy.

        - **policyVersionId** *(string) --*

          The ID of the version of the policy associated with the resource.

      - **account** *(string) --*

        The account with which the resource is associated.

    - **additionalInfo** *(dict) --*

      Other information about the resource.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeAuditFindingResponsefindingTypeDef = TypedDict(
    "_ClientDescribeAuditFindingResponsefindingTypeDef",
    {
        "findingId": str,
        "taskId": str,
        "checkName": str,
        "taskStartTime": datetime,
        "findingTime": datetime,
        "severity": str,
        "nonCompliantResource": ClientDescribeAuditFindingResponsefindingnonCompliantResourceTypeDef,
        "relatedResources": List[
            ClientDescribeAuditFindingResponsefindingrelatedResourcesTypeDef
        ],
        "reasonForNonCompliance": str,
        "reasonForNonComplianceCode": str,
    },
    total=False,
)


class ClientDescribeAuditFindingResponsefindingTypeDef(
    _ClientDescribeAuditFindingResponsefindingTypeDef
):
    """
    Type definition for `ClientDescribeAuditFindingResponse` `finding`

    The findings (results) of the audit.

    - **findingId** *(string) --*

      A unique identifier for this set of audit findings. This identifier is used to apply
      mitigation tasks to one or more sets of findings.

    - **taskId** *(string) --*

      The ID of the audit that generated this result (finding).

    - **checkName** *(string) --*

      The audit check that generated this result.

    - **taskStartTime** *(datetime) --*

      The time the audit started.

    - **findingTime** *(datetime) --*

      The time the result (finding) was discovered.

    - **severity** *(string) --*

      The severity of the result (finding).

    - **nonCompliantResource** *(dict) --*

      The resource that was found to be noncompliant with the audit check.

      - **resourceType** *(string) --*

        The type of the noncompliant resource.

      - **resourceIdentifier** *(dict) --*

        Information that identifies the noncompliant resource.

        - **deviceCertificateId** *(string) --*

          The ID of the certificate attached to the resource.

        - **caCertificateId** *(string) --*

          The ID of the CA certificate used to authorize the certificate.

        - **cognitoIdentityPoolId** *(string) --*

          The ID of the Amazon Cognito identity pool.

        - **clientId** *(string) --*

          The client ID.

        - **policyVersionIdentifier** *(dict) --*

          The version of the policy associated with the resource.

          - **policyName** *(string) --*

            The name of the policy.

          - **policyVersionId** *(string) --*

            The ID of the version of the policy associated with the resource.

        - **account** *(string) --*

          The account with which the resource is associated.

      - **additionalInfo** *(dict) --*

        Other information about the noncompliant resource.

        - *(string) --*

          - *(string) --*

    - **relatedResources** *(list) --*

      The list of related resources.

      - *(dict) --*

        Information about a related resource.

        - **resourceType** *(string) --*

          The type of resource.

        - **resourceIdentifier** *(dict) --*

          Information that identifies the resource.

          - **deviceCertificateId** *(string) --*

            The ID of the certificate attached to the resource.

          - **caCertificateId** *(string) --*

            The ID of the CA certificate used to authorize the certificate.

          - **cognitoIdentityPoolId** *(string) --*

            The ID of the Amazon Cognito identity pool.

          - **clientId** *(string) --*

            The client ID.

          - **policyVersionIdentifier** *(dict) --*

            The version of the policy associated with the resource.

            - **policyName** *(string) --*

              The name of the policy.

            - **policyVersionId** *(string) --*

              The ID of the version of the policy associated with the resource.

          - **account** *(string) --*

            The account with which the resource is associated.

        - **additionalInfo** *(dict) --*

          Other information about the resource.

          - *(string) --*

            - *(string) --*

    - **reasonForNonCompliance** *(string) --*

      The reason the resource was noncompliant.

    - **reasonForNonComplianceCode** *(string) --*

      A code that indicates the reason that the resource was noncompliant.
    """


_ClientDescribeAuditFindingResponseTypeDef = TypedDict(
    "_ClientDescribeAuditFindingResponseTypeDef",
    {"finding": ClientDescribeAuditFindingResponsefindingTypeDef},
    total=False,
)


class ClientDescribeAuditFindingResponseTypeDef(
    _ClientDescribeAuditFindingResponseTypeDef
):
    """
    Type definition for `ClientDescribeAuditFinding` `Response`

    - **finding** *(dict) --*

      The findings (results) of the audit.

      - **findingId** *(string) --*

        A unique identifier for this set of audit findings. This identifier is used to apply
        mitigation tasks to one or more sets of findings.

      - **taskId** *(string) --*

        The ID of the audit that generated this result (finding).

      - **checkName** *(string) --*

        The audit check that generated this result.

      - **taskStartTime** *(datetime) --*

        The time the audit started.

      - **findingTime** *(datetime) --*

        The time the result (finding) was discovered.

      - **severity** *(string) --*

        The severity of the result (finding).

      - **nonCompliantResource** *(dict) --*

        The resource that was found to be noncompliant with the audit check.

        - **resourceType** *(string) --*

          The type of the noncompliant resource.

        - **resourceIdentifier** *(dict) --*

          Information that identifies the noncompliant resource.

          - **deviceCertificateId** *(string) --*

            The ID of the certificate attached to the resource.

          - **caCertificateId** *(string) --*

            The ID of the CA certificate used to authorize the certificate.

          - **cognitoIdentityPoolId** *(string) --*

            The ID of the Amazon Cognito identity pool.

          - **clientId** *(string) --*

            The client ID.

          - **policyVersionIdentifier** *(dict) --*

            The version of the policy associated with the resource.

            - **policyName** *(string) --*

              The name of the policy.

            - **policyVersionId** *(string) --*

              The ID of the version of the policy associated with the resource.

          - **account** *(string) --*

            The account with which the resource is associated.

        - **additionalInfo** *(dict) --*

          Other information about the noncompliant resource.

          - *(string) --*

            - *(string) --*

      - **relatedResources** *(list) --*

        The list of related resources.

        - *(dict) --*

          Information about a related resource.

          - **resourceType** *(string) --*

            The type of resource.

          - **resourceIdentifier** *(dict) --*

            Information that identifies the resource.

            - **deviceCertificateId** *(string) --*

              The ID of the certificate attached to the resource.

            - **caCertificateId** *(string) --*

              The ID of the CA certificate used to authorize the certificate.

            - **cognitoIdentityPoolId** *(string) --*

              The ID of the Amazon Cognito identity pool.

            - **clientId** *(string) --*

              The client ID.

            - **policyVersionIdentifier** *(dict) --*

              The version of the policy associated with the resource.

              - **policyName** *(string) --*

                The name of the policy.

              - **policyVersionId** *(string) --*

                The ID of the version of the policy associated with the resource.

            - **account** *(string) --*

              The account with which the resource is associated.

          - **additionalInfo** *(dict) --*

            Other information about the resource.

            - *(string) --*

              - *(string) --*

      - **reasonForNonCompliance** *(string) --*

        The reason the resource was noncompliant.

      - **reasonForNonComplianceCode** *(string) --*

        A code that indicates the reason that the resource was noncompliant.
    """


_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsaddThingsToThingGroupParamsTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsaddThingsToThingGroupParamsTypeDef",
    {"thingGroupNames": List[str], "overrideDynamicGroups": bool},
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsaddThingsToThingGroupParamsTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsaddThingsToThingGroupParamsTypeDef
):
    """
    Type definition for `ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParams` `addThingsToThingGroupParams`

    Parameters to define a mitigation action that moves devices associated with a
    certificate to one or more specified thing groups, typically for quarantine.

    - **thingGroupNames** *(list) --*

      The list of groups to which you want to add the things that triggered the mitigation
      action. You can add a thing to a maximum of 10 groups, but you cannot add a thing to
      more than one group in the same hierarchy.

      - *(string) --*

    - **overrideDynamicGroups** *(boolean) --*

      Specifies if this mitigation action can move the things that triggered the mitigation
      action even if they are part of one or more dynamic things groups.
    """


_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsenableIoTLoggingParamsTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsenableIoTLoggingParamsTypeDef",
    {"roleArnForLogging": str, "logLevel": str},
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsenableIoTLoggingParamsTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsenableIoTLoggingParamsTypeDef
):
    """
    Type definition for `ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParams` `enableIoTLoggingParams`

    Parameters to define a mitigation action that enables AWS IoT logging at a specified
    level of detail.

    - **roleArnForLogging** *(string) --*

      The ARN of the IAM role used for logging.

    - **logLevel** *(string) --*

      Specifies the types of information to be logged.
    """


_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamspublishFindingToSnsParamsTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamspublishFindingToSnsParamsTypeDef",
    {"topicArn": str},
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamspublishFindingToSnsParamsTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamspublishFindingToSnsParamsTypeDef
):
    """
    Type definition for `ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParams` `publishFindingToSnsParams`

    Parameters to define a mitigation action that publishes findings to Amazon SNS. You can
    implement your own custom actions in response to the Amazon SNS messages.

    - **topicArn** *(string) --*

      The ARN of the topic to which you want to publish the findings.
    """


_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsreplaceDefaultPolicyVersionParamsTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsreplaceDefaultPolicyVersionParamsTypeDef",
    {"templateName": str},
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsreplaceDefaultPolicyVersionParamsTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsreplaceDefaultPolicyVersionParamsTypeDef
):
    """
    Type definition for `ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParams` `replaceDefaultPolicyVersionParams`

    Parameters to define a mitigation action that adds a blank policy to restrict
    permissions.

    - **templateName** *(string) --*

      The name of the template to be applied. The only supported value is ``BLANK_POLICY`` .
    """


_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateCACertificateParamsTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateCACertificateParamsTypeDef",
    {"action": str},
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateCACertificateParamsTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateCACertificateParamsTypeDef
):
    """
    Type definition for `ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParams` `updateCACertificateParams`

    Parameters to define a mitigation action that changes the state of the CA certificate
    to inactive.

    - **action** *(string) --*

      The action that you want to apply to the CA cerrtificate. The only supported value is
      ``DEACTIVATE`` .
    """


_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateDeviceCertificateParamsTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateDeviceCertificateParamsTypeDef",
    {"action": str},
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateDeviceCertificateParamsTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateDeviceCertificateParamsTypeDef
):
    """
    Type definition for `ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParams` `updateDeviceCertificateParams`

    Parameters to define a mitigation action that changes the state of the device
    certificate to inactive.

    - **action** *(string) --*

      The action that you want to apply to the device cerrtificate. The only supported
      value is ``DEACTIVATE`` .
    """


_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsTypeDef",
    {
        "updateDeviceCertificateParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateDeviceCertificateParamsTypeDef,
        "updateCACertificateParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsupdateCACertificateParamsTypeDef,
        "addThingsToThingGroupParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsaddThingsToThingGroupParamsTypeDef,
        "replaceDefaultPolicyVersionParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsreplaceDefaultPolicyVersionParamsTypeDef,
        "enableIoTLoggingParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsenableIoTLoggingParamsTypeDef,
        "publishFindingToSnsParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamspublishFindingToSnsParamsTypeDef,
    },
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsTypeDef
):
    """
    Type definition for `ClientDescribeAuditMitigationActionsTaskResponseactionsDefinition` `actionParams`

    The set of parameters for this mitigation action. The parameters vary, depending on the
    kind of action you apply.

    - **updateDeviceCertificateParams** *(dict) --*

      Parameters to define a mitigation action that changes the state of the device
      certificate to inactive.

      - **action** *(string) --*

        The action that you want to apply to the device cerrtificate. The only supported
        value is ``DEACTIVATE`` .

    - **updateCACertificateParams** *(dict) --*

      Parameters to define a mitigation action that changes the state of the CA certificate
      to inactive.

      - **action** *(string) --*

        The action that you want to apply to the CA cerrtificate. The only supported value is
        ``DEACTIVATE`` .

    - **addThingsToThingGroupParams** *(dict) --*

      Parameters to define a mitigation action that moves devices associated with a
      certificate to one or more specified thing groups, typically for quarantine.

      - **thingGroupNames** *(list) --*

        The list of groups to which you want to add the things that triggered the mitigation
        action. You can add a thing to a maximum of 10 groups, but you cannot add a thing to
        more than one group in the same hierarchy.

        - *(string) --*

      - **overrideDynamicGroups** *(boolean) --*

        Specifies if this mitigation action can move the things that triggered the mitigation
        action even if they are part of one or more dynamic things groups.

    - **replaceDefaultPolicyVersionParams** *(dict) --*

      Parameters to define a mitigation action that adds a blank policy to restrict
      permissions.

      - **templateName** *(string) --*

        The name of the template to be applied. The only supported value is ``BLANK_POLICY`` .

    - **enableIoTLoggingParams** *(dict) --*

      Parameters to define a mitigation action that enables AWS IoT logging at a specified
      level of detail.

      - **roleArnForLogging** *(string) --*

        The ARN of the IAM role used for logging.

      - **logLevel** *(string) --*

        Specifies the types of information to be logged.

    - **publishFindingToSnsParams** *(dict) --*

      Parameters to define a mitigation action that publishes findings to Amazon SNS. You can
      implement your own custom actions in response to the Amazon SNS messages.

      - **topicArn** *(string) --*

        The ARN of the topic to which you want to publish the findings.
    """


_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionTypeDef",
    {
        "name": str,
        "id": str,
        "roleArn": str,
        "actionParams": ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionactionParamsTypeDef,
    },
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionTypeDef
):
    """
    Type definition for `ClientDescribeAuditMitigationActionsTaskResponse` `actionsDefinition`

    Describes which changes should be applied as part of a mitigation action.

    - **name** *(string) --*

      A user-friendly name for the mitigation action.

    - **id** *(string) --*

      A unique identifier for the mitigation action.

    - **roleArn** *(string) --*

      The IAM role ARN used to apply this mitigation action.

    - **actionParams** *(dict) --*

      The set of parameters for this mitigation action. The parameters vary, depending on the
      kind of action you apply.

      - **updateDeviceCertificateParams** *(dict) --*

        Parameters to define a mitigation action that changes the state of the device
        certificate to inactive.

        - **action** *(string) --*

          The action that you want to apply to the device cerrtificate. The only supported
          value is ``DEACTIVATE`` .

      - **updateCACertificateParams** *(dict) --*

        Parameters to define a mitigation action that changes the state of the CA certificate
        to inactive.

        - **action** *(string) --*

          The action that you want to apply to the CA cerrtificate. The only supported value is
          ``DEACTIVATE`` .

      - **addThingsToThingGroupParams** *(dict) --*

        Parameters to define a mitigation action that moves devices associated with a
        certificate to one or more specified thing groups, typically for quarantine.

        - **thingGroupNames** *(list) --*

          The list of groups to which you want to add the things that triggered the mitigation
          action. You can add a thing to a maximum of 10 groups, but you cannot add a thing to
          more than one group in the same hierarchy.

          - *(string) --*

        - **overrideDynamicGroups** *(boolean) --*

          Specifies if this mitigation action can move the things that triggered the mitigation
          action even if they are part of one or more dynamic things groups.

      - **replaceDefaultPolicyVersionParams** *(dict) --*

        Parameters to define a mitigation action that adds a blank policy to restrict
        permissions.

        - **templateName** *(string) --*

          The name of the template to be applied. The only supported value is ``BLANK_POLICY`` .

      - **enableIoTLoggingParams** *(dict) --*

        Parameters to define a mitigation action that enables AWS IoT logging at a specified
        level of detail.

        - **roleArnForLogging** *(string) --*

          The ARN of the IAM role used for logging.

        - **logLevel** *(string) --*

          Specifies the types of information to be logged.

      - **publishFindingToSnsParams** *(dict) --*

        Parameters to define a mitigation action that publishes findings to Amazon SNS. You can
        implement your own custom actions in response to the Amazon SNS messages.

        - **topicArn** *(string) --*

          The ARN of the topic to which you want to publish the findings.
    """


_ClientDescribeAuditMitigationActionsTaskResponsetargetTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponsetargetTypeDef",
    {
        "auditTaskId": str,
        "findingIds": List[str],
        "auditCheckToReasonCodeFilter": Dict[str, List[str]],
    },
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponsetargetTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponsetargetTypeDef
):
    """
    Type definition for `ClientDescribeAuditMitigationActionsTaskResponse` `target`

    Identifies the findings to which the mitigation actions are applied. This can be by audit
    checks, by audit task, or a set of findings.

    - **auditTaskId** *(string) --*

      If the task will apply a mitigation action to findings from a specific audit, this value
      uniquely identifies the audit.

    - **findingIds** *(list) --*

      If the task will apply a mitigation action to one or more listed findings, this value
      uniquely identifies those findings.

      - *(string) --*

    - **auditCheckToReasonCodeFilter** *(dict) --*

      Specifies a filter in the form of an audit check and set of reason codes that identify the
      findings from the audit to which the audit mitigation actions task apply.

      - *(string) --*

        An audit check name. Checks must be enabled for your account. (Use
        ``DescribeAccountAuditConfiguration`` to see the list of all checks, including those that
        are enabled or use ``UpdateAccountAuditConfiguration`` to select which checks are
        enabled.)

        - *(list) --*

          - *(string) --*
    """


_ClientDescribeAuditMitigationActionsTaskResponsetaskStatisticsTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponsetaskStatisticsTypeDef",
    {
        "totalFindingsCount": int,
        "failedFindingsCount": int,
        "succeededFindingsCount": int,
        "skippedFindingsCount": int,
        "canceledFindingsCount": int,
    },
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponsetaskStatisticsTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponsetaskStatisticsTypeDef
):
    """
    Type definition for `ClientDescribeAuditMitigationActionsTaskResponse` `taskStatistics`

    Provides summary counts of how many tasks for findings are in a particular state. This
    information is included in the response from DescribeAuditMitigationActionsTask.

    - **totalFindingsCount** *(integer) --*

      The total number of findings to which a task is being applied.

    - **failedFindingsCount** *(integer) --*

      The number of findings for which at least one of the actions failed when applied.

    - **succeededFindingsCount** *(integer) --*

      The number of findings for which all mitigation actions succeeded when applied.

    - **skippedFindingsCount** *(integer) --*

      The number of findings skipped because of filter conditions provided in the parameters
      to the command.

    - **canceledFindingsCount** *(integer) --*

      The number of findings to which the mitigation action task was canceled when applied.
    """


_ClientDescribeAuditMitigationActionsTaskResponseTypeDef = TypedDict(
    "_ClientDescribeAuditMitigationActionsTaskResponseTypeDef",
    {
        "taskStatus": str,
        "startTime": datetime,
        "endTime": datetime,
        "taskStatistics": Dict[
            str, ClientDescribeAuditMitigationActionsTaskResponsetaskStatisticsTypeDef
        ],
        "target": ClientDescribeAuditMitigationActionsTaskResponsetargetTypeDef,
        "auditCheckToActionsMapping": Dict[str, List[str]],
        "actionsDefinition": List[
            ClientDescribeAuditMitigationActionsTaskResponseactionsDefinitionTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAuditMitigationActionsTaskResponseTypeDef(
    _ClientDescribeAuditMitigationActionsTaskResponseTypeDef
):
    """
    Type definition for `ClientDescribeAuditMitigationActionsTask` `Response`

    - **taskStatus** *(string) --*

      The current status of the task.

    - **startTime** *(datetime) --*

      The date and time when the task was started.

    - **endTime** *(datetime) --*

      The date and time when the task was completed or canceled.

    - **taskStatistics** *(dict) --*

      Aggregate counts of the results when the mitigation tasks were applied to the findings for
      this audit mitigation actions task.

      - *(string) --*

        An audit check name. Checks must be enabled for your account. (Use
        ``DescribeAccountAuditConfiguration`` to see the list of all checks, including those that
        are enabled or use ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)

        - *(dict) --*

          Provides summary counts of how many tasks for findings are in a particular state. This
          information is included in the response from DescribeAuditMitigationActionsTask.

          - **totalFindingsCount** *(integer) --*

            The total number of findings to which a task is being applied.

          - **failedFindingsCount** *(integer) --*

            The number of findings for which at least one of the actions failed when applied.

          - **succeededFindingsCount** *(integer) --*

            The number of findings for which all mitigation actions succeeded when applied.

          - **skippedFindingsCount** *(integer) --*

            The number of findings skipped because of filter conditions provided in the parameters
            to the command.

          - **canceledFindingsCount** *(integer) --*

            The number of findings to which the mitigation action task was canceled when applied.

    - **target** *(dict) --*

      Identifies the findings to which the mitigation actions are applied. This can be by audit
      checks, by audit task, or a set of findings.

      - **auditTaskId** *(string) --*

        If the task will apply a mitigation action to findings from a specific audit, this value
        uniquely identifies the audit.

      - **findingIds** *(list) --*

        If the task will apply a mitigation action to one or more listed findings, this value
        uniquely identifies those findings.

        - *(string) --*

      - **auditCheckToReasonCodeFilter** *(dict) --*

        Specifies a filter in the form of an audit check and set of reason codes that identify the
        findings from the audit to which the audit mitigation actions task apply.

        - *(string) --*

          An audit check name. Checks must be enabled for your account. (Use
          ``DescribeAccountAuditConfiguration`` to see the list of all checks, including those that
          are enabled or use ``UpdateAccountAuditConfiguration`` to select which checks are
          enabled.)

          - *(list) --*

            - *(string) --*

    - **auditCheckToActionsMapping** *(dict) --*

      Specifies the mitigation actions that should be applied to specific audit checks.

      - *(string) --*

        An audit check name. Checks must be enabled for your account. (Use
        ``DescribeAccountAuditConfiguration`` to see the list of all checks, including those that
        are enabled or use ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)

        - *(list) --*

          - *(string) --*

    - **actionsDefinition** *(list) --*

      Specifies the mitigation actions and their parameters that are applied as part of this task.

      - *(dict) --*

        Describes which changes should be applied as part of a mitigation action.

        - **name** *(string) --*

          A user-friendly name for the mitigation action.

        - **id** *(string) --*

          A unique identifier for the mitigation action.

        - **roleArn** *(string) --*

          The IAM role ARN used to apply this mitigation action.

        - **actionParams** *(dict) --*

          The set of parameters for this mitigation action. The parameters vary, depending on the
          kind of action you apply.

          - **updateDeviceCertificateParams** *(dict) --*

            Parameters to define a mitigation action that changes the state of the device
            certificate to inactive.

            - **action** *(string) --*

              The action that you want to apply to the device cerrtificate. The only supported
              value is ``DEACTIVATE`` .

          - **updateCACertificateParams** *(dict) --*

            Parameters to define a mitigation action that changes the state of the CA certificate
            to inactive.

            - **action** *(string) --*

              The action that you want to apply to the CA cerrtificate. The only supported value is
              ``DEACTIVATE`` .

          - **addThingsToThingGroupParams** *(dict) --*

            Parameters to define a mitigation action that moves devices associated with a
            certificate to one or more specified thing groups, typically for quarantine.

            - **thingGroupNames** *(list) --*

              The list of groups to which you want to add the things that triggered the mitigation
              action. You can add a thing to a maximum of 10 groups, but you cannot add a thing to
              more than one group in the same hierarchy.

              - *(string) --*

            - **overrideDynamicGroups** *(boolean) --*

              Specifies if this mitigation action can move the things that triggered the mitigation
              action even if they are part of one or more dynamic things groups.

          - **replaceDefaultPolicyVersionParams** *(dict) --*

            Parameters to define a mitigation action that adds a blank policy to restrict
            permissions.

            - **templateName** *(string) --*

              The name of the template to be applied. The only supported value is ``BLANK_POLICY`` .

          - **enableIoTLoggingParams** *(dict) --*

            Parameters to define a mitigation action that enables AWS IoT logging at a specified
            level of detail.

            - **roleArnForLogging** *(string) --*

              The ARN of the IAM role used for logging.

            - **logLevel** *(string) --*

              Specifies the types of information to be logged.

          - **publishFindingToSnsParams** *(dict) --*

            Parameters to define a mitigation action that publishes findings to Amazon SNS. You can
            implement your own custom actions in response to the Amazon SNS messages.

            - **topicArn** *(string) --*

              The ARN of the topic to which you want to publish the findings.
    """


_ClientDescribeAuditTaskResponseauditDetailsTypeDef = TypedDict(
    "_ClientDescribeAuditTaskResponseauditDetailsTypeDef",
    {
        "checkRunStatus": str,
        "checkCompliant": bool,
        "totalResourcesCount": int,
        "nonCompliantResourcesCount": int,
        "errorCode": str,
        "message": str,
    },
    total=False,
)


class ClientDescribeAuditTaskResponseauditDetailsTypeDef(
    _ClientDescribeAuditTaskResponseauditDetailsTypeDef
):
    """
    Type definition for `ClientDescribeAuditTaskResponse` `auditDetails`

    Information about the audit check.

    - **checkRunStatus** *(string) --*

      The completion status of this check. One of "IN_PROGRESS",
      "WAITING_FOR_DATA_COLLECTION", "CANCELED", "COMPLETED_COMPLIANT",
      "COMPLETED_NON_COMPLIANT", or "FAILED".

    - **checkCompliant** *(boolean) --*

      True if the check is complete and found all resources compliant.

    - **totalResourcesCount** *(integer) --*

      The number of resources on which the check was performed.

    - **nonCompliantResourcesCount** *(integer) --*

      The number of resources that were found noncompliant during the check.

    - **errorCode** *(string) --*

      The code of any error encountered when this check is performed during this audit. One
      of "INSUFFICIENT_PERMISSIONS" or "AUDIT_CHECK_DISABLED".

    - **message** *(string) --*

      The message associated with any error encountered when this check is performed during
      this audit.
    """


_ClientDescribeAuditTaskResponsetaskStatisticsTypeDef = TypedDict(
    "_ClientDescribeAuditTaskResponsetaskStatisticsTypeDef",
    {
        "totalChecks": int,
        "inProgressChecks": int,
        "waitingForDataCollectionChecks": int,
        "compliantChecks": int,
        "nonCompliantChecks": int,
        "failedChecks": int,
        "canceledChecks": int,
    },
    total=False,
)


class ClientDescribeAuditTaskResponsetaskStatisticsTypeDef(
    _ClientDescribeAuditTaskResponsetaskStatisticsTypeDef
):
    """
    Type definition for `ClientDescribeAuditTaskResponse` `taskStatistics`

    Statistical information about the audit.

    - **totalChecks** *(integer) --*

      The number of checks in this audit.

    - **inProgressChecks** *(integer) --*

      The number of checks in progress.

    - **waitingForDataCollectionChecks** *(integer) --*

      The number of checks waiting for data collection.

    - **compliantChecks** *(integer) --*

      The number of checks that found compliant resources.

    - **nonCompliantChecks** *(integer) --*

      The number of checks that found noncompliant resources.

    - **failedChecks** *(integer) --*

      The number of checks.

    - **canceledChecks** *(integer) --*

      The number of checks that did not run because the audit was canceled.
    """


_ClientDescribeAuditTaskResponseTypeDef = TypedDict(
    "_ClientDescribeAuditTaskResponseTypeDef",
    {
        "taskStatus": str,
        "taskType": str,
        "taskStartTime": datetime,
        "taskStatistics": ClientDescribeAuditTaskResponsetaskStatisticsTypeDef,
        "scheduledAuditName": str,
        "auditDetails": Dict[str, ClientDescribeAuditTaskResponseauditDetailsTypeDef],
    },
    total=False,
)


class ClientDescribeAuditTaskResponseTypeDef(_ClientDescribeAuditTaskResponseTypeDef):
    """
    Type definition for `ClientDescribeAuditTask` `Response`

    - **taskStatus** *(string) --*

      The status of the audit: one of "IN_PROGRESS", "COMPLETED", "FAILED", or "CANCELED".

    - **taskType** *(string) --*

      The type of audit: "ON_DEMAND_AUDIT_TASK" or "SCHEDULED_AUDIT_TASK".

    - **taskStartTime** *(datetime) --*

      The time the audit started.

    - **taskStatistics** *(dict) --*

      Statistical information about the audit.

      - **totalChecks** *(integer) --*

        The number of checks in this audit.

      - **inProgressChecks** *(integer) --*

        The number of checks in progress.

      - **waitingForDataCollectionChecks** *(integer) --*

        The number of checks waiting for data collection.

      - **compliantChecks** *(integer) --*

        The number of checks that found compliant resources.

      - **nonCompliantChecks** *(integer) --*

        The number of checks that found noncompliant resources.

      - **failedChecks** *(integer) --*

        The number of checks.

      - **canceledChecks** *(integer) --*

        The number of checks that did not run because the audit was canceled.

    - **scheduledAuditName** *(string) --*

      The name of the scheduled audit (only if the audit was a scheduled audit).

    - **auditDetails** *(dict) --*

      Detailed information about each check performed during this audit.

      - *(string) --*

        An audit check name. Checks must be enabled for your account. (Use
        ``DescribeAccountAuditConfiguration`` to see the list of all checks, including those that
        are enabled or use ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)

        - *(dict) --*

          Information about the audit check.

          - **checkRunStatus** *(string) --*

            The completion status of this check. One of "IN_PROGRESS",
            "WAITING_FOR_DATA_COLLECTION", "CANCELED", "COMPLETED_COMPLIANT",
            "COMPLETED_NON_COMPLIANT", or "FAILED".

          - **checkCompliant** *(boolean) --*

            True if the check is complete and found all resources compliant.

          - **totalResourcesCount** *(integer) --*

            The number of resources on which the check was performed.

          - **nonCompliantResourcesCount** *(integer) --*

            The number of resources that were found noncompliant during the check.

          - **errorCode** *(string) --*

            The code of any error encountered when this check is performed during this audit. One
            of "INSUFFICIENT_PERMISSIONS" or "AUDIT_CHECK_DISABLED".

          - **message** *(string) --*

            The message associated with any error encountered when this check is performed during
            this audit.
    """


_ClientDescribeAuthorizerResponseauthorizerDescriptionTypeDef = TypedDict(
    "_ClientDescribeAuthorizerResponseauthorizerDescriptionTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
        "authorizerFunctionArn": str,
        "tokenKeyName": str,
        "tokenSigningPublicKeys": Dict[str, str],
        "status": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeAuthorizerResponseauthorizerDescriptionTypeDef(
    _ClientDescribeAuthorizerResponseauthorizerDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeAuthorizerResponse` `authorizerDescription`

    The authorizer description.

    - **authorizerName** *(string) --*

      The authorizer name.

    - **authorizerArn** *(string) --*

      The authorizer ARN.

    - **authorizerFunctionArn** *(string) --*

      The authorizer's Lambda function ARN.

    - **tokenKeyName** *(string) --*

      The key used to extract the token from the HTTP headers.

    - **tokenSigningPublicKeys** *(dict) --*

      The public keys used to validate the token signature returned by your custom authentication
      service.

      - *(string) --*

        - *(string) --*

    - **status** *(string) --*

      The status of the authorizer.

    - **creationDate** *(datetime) --*

      The UNIX timestamp of when the authorizer was created.

    - **lastModifiedDate** *(datetime) --*

      The UNIX timestamp of when the authorizer was last updated.
    """


_ClientDescribeAuthorizerResponseTypeDef = TypedDict(
    "_ClientDescribeAuthorizerResponseTypeDef",
    {
        "authorizerDescription": ClientDescribeAuthorizerResponseauthorizerDescriptionTypeDef
    },
    total=False,
)


class ClientDescribeAuthorizerResponseTypeDef(_ClientDescribeAuthorizerResponseTypeDef):
    """
    Type definition for `ClientDescribeAuthorizer` `Response`

    - **authorizerDescription** *(dict) --*

      The authorizer description.

      - **authorizerName** *(string) --*

        The authorizer name.

      - **authorizerArn** *(string) --*

        The authorizer ARN.

      - **authorizerFunctionArn** *(string) --*

        The authorizer's Lambda function ARN.

      - **tokenKeyName** *(string) --*

        The key used to extract the token from the HTTP headers.

      - **tokenSigningPublicKeys** *(dict) --*

        The public keys used to validate the token signature returned by your custom authentication
        service.

        - *(string) --*

          - *(string) --*

      - **status** *(string) --*

        The status of the authorizer.

      - **creationDate** *(datetime) --*

        The UNIX timestamp of when the authorizer was created.

      - **lastModifiedDate** *(datetime) --*

        The UNIX timestamp of when the authorizer was last updated.
    """


_ClientDescribeBillingGroupResponsebillingGroupMetadataTypeDef = TypedDict(
    "_ClientDescribeBillingGroupResponsebillingGroupMetadataTypeDef",
    {"creationDate": datetime},
    total=False,
)


class ClientDescribeBillingGroupResponsebillingGroupMetadataTypeDef(
    _ClientDescribeBillingGroupResponsebillingGroupMetadataTypeDef
):
    """
    Type definition for `ClientDescribeBillingGroupResponse` `billingGroupMetadata`

    Additional information about the billing group.

    - **creationDate** *(datetime) --*

      The date the billing group was created.
    """


_ClientDescribeBillingGroupResponsebillingGroupPropertiesTypeDef = TypedDict(
    "_ClientDescribeBillingGroupResponsebillingGroupPropertiesTypeDef",
    {"billingGroupDescription": str},
    total=False,
)


class ClientDescribeBillingGroupResponsebillingGroupPropertiesTypeDef(
    _ClientDescribeBillingGroupResponsebillingGroupPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeBillingGroupResponse` `billingGroupProperties`

    The properties of the billing group.

    - **billingGroupDescription** *(string) --*

      The description of the billing group.
    """


_ClientDescribeBillingGroupResponseTypeDef = TypedDict(
    "_ClientDescribeBillingGroupResponseTypeDef",
    {
        "billingGroupName": str,
        "billingGroupId": str,
        "billingGroupArn": str,
        "version": int,
        "billingGroupProperties": ClientDescribeBillingGroupResponsebillingGroupPropertiesTypeDef,
        "billingGroupMetadata": ClientDescribeBillingGroupResponsebillingGroupMetadataTypeDef,
    },
    total=False,
)


class ClientDescribeBillingGroupResponseTypeDef(
    _ClientDescribeBillingGroupResponseTypeDef
):
    """
    Type definition for `ClientDescribeBillingGroup` `Response`

    - **billingGroupName** *(string) --*

      The name of the billing group.

    - **billingGroupId** *(string) --*

      The ID of the billing group.

    - **billingGroupArn** *(string) --*

      The ARN of the billing group.

    - **version** *(integer) --*

      The version of the billing group.

    - **billingGroupProperties** *(dict) --*

      The properties of the billing group.

      - **billingGroupDescription** *(string) --*

        The description of the billing group.

    - **billingGroupMetadata** *(dict) --*

      Additional information about the billing group.

      - **creationDate** *(datetime) --*

        The date the billing group was created.
    """


_ClientDescribeCaCertificateResponsecertificateDescriptionvalidityTypeDef = TypedDict(
    "_ClientDescribeCaCertificateResponsecertificateDescriptionvalidityTypeDef",
    {"notBefore": datetime, "notAfter": datetime},
    total=False,
)


class ClientDescribeCaCertificateResponsecertificateDescriptionvalidityTypeDef(
    _ClientDescribeCaCertificateResponsecertificateDescriptionvalidityTypeDef
):
    """
    Type definition for `ClientDescribeCaCertificateResponsecertificateDescription` `validity`

    When the CA certificate is valid.

    - **notBefore** *(datetime) --*

      The certificate is not valid before this date.

    - **notAfter** *(datetime) --*

      The certificate is not valid after this date.
    """


_ClientDescribeCaCertificateResponsecertificateDescriptionTypeDef = TypedDict(
    "_ClientDescribeCaCertificateResponsecertificateDescriptionTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": str,
        "certificatePem": str,
        "ownedBy": str,
        "creationDate": datetime,
        "autoRegistrationStatus": str,
        "lastModifiedDate": datetime,
        "customerVersion": int,
        "generationId": str,
        "validity": ClientDescribeCaCertificateResponsecertificateDescriptionvalidityTypeDef,
    },
    total=False,
)


class ClientDescribeCaCertificateResponsecertificateDescriptionTypeDef(
    _ClientDescribeCaCertificateResponsecertificateDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeCaCertificateResponse` `certificateDescription`

    The CA certificate description.

    - **certificateArn** *(string) --*

      The CA certificate ARN.

    - **certificateId** *(string) --*

      The CA certificate ID.

    - **status** *(string) --*

      The status of a CA certificate.

    - **certificatePem** *(string) --*

      The CA certificate data, in PEM format.

    - **ownedBy** *(string) --*

      The owner of the CA certificate.

    - **creationDate** *(datetime) --*

      The date the CA certificate was created.

    - **autoRegistrationStatus** *(string) --*

      Whether the CA certificate configured for auto registration of device certificates. Valid
      values are "ENABLE" and "DISABLE"

    - **lastModifiedDate** *(datetime) --*

      The date the CA certificate was last modified.

    - **customerVersion** *(integer) --*

      The customer version of the CA certificate.

    - **generationId** *(string) --*

      The generation ID of the CA certificate.

    - **validity** *(dict) --*

      When the CA certificate is valid.

      - **notBefore** *(datetime) --*

        The certificate is not valid before this date.

      - **notAfter** *(datetime) --*

        The certificate is not valid after this date.
    """


_ClientDescribeCaCertificateResponseregistrationConfigTypeDef = TypedDict(
    "_ClientDescribeCaCertificateResponseregistrationConfigTypeDef",
    {"templateBody": str, "roleArn": str},
    total=False,
)


class ClientDescribeCaCertificateResponseregistrationConfigTypeDef(
    _ClientDescribeCaCertificateResponseregistrationConfigTypeDef
):
    """
    Type definition for `ClientDescribeCaCertificateResponse` `registrationConfig`

    Information about the registration configuration.

    - **templateBody** *(string) --*

      The template body.

    - **roleArn** *(string) --*

      The ARN of the role.
    """


_ClientDescribeCaCertificateResponseTypeDef = TypedDict(
    "_ClientDescribeCaCertificateResponseTypeDef",
    {
        "certificateDescription": ClientDescribeCaCertificateResponsecertificateDescriptionTypeDef,
        "registrationConfig": ClientDescribeCaCertificateResponseregistrationConfigTypeDef,
    },
    total=False,
)


class ClientDescribeCaCertificateResponseTypeDef(
    _ClientDescribeCaCertificateResponseTypeDef
):
    """
    Type definition for `ClientDescribeCaCertificate` `Response`

    The output from the DescribeCACertificate operation.

    - **certificateDescription** *(dict) --*

      The CA certificate description.

      - **certificateArn** *(string) --*

        The CA certificate ARN.

      - **certificateId** *(string) --*

        The CA certificate ID.

      - **status** *(string) --*

        The status of a CA certificate.

      - **certificatePem** *(string) --*

        The CA certificate data, in PEM format.

      - **ownedBy** *(string) --*

        The owner of the CA certificate.

      - **creationDate** *(datetime) --*

        The date the CA certificate was created.

      - **autoRegistrationStatus** *(string) --*

        Whether the CA certificate configured for auto registration of device certificates. Valid
        values are "ENABLE" and "DISABLE"

      - **lastModifiedDate** *(datetime) --*

        The date the CA certificate was last modified.

      - **customerVersion** *(integer) --*

        The customer version of the CA certificate.

      - **generationId** *(string) --*

        The generation ID of the CA certificate.

      - **validity** *(dict) --*

        When the CA certificate is valid.

        - **notBefore** *(datetime) --*

          The certificate is not valid before this date.

        - **notAfter** *(datetime) --*

          The certificate is not valid after this date.

    - **registrationConfig** *(dict) --*

      Information about the registration configuration.

      - **templateBody** *(string) --*

        The template body.

      - **roleArn** *(string) --*

        The ARN of the role.
    """


_ClientDescribeCertificateResponsecertificateDescriptiontransferDataTypeDef = TypedDict(
    "_ClientDescribeCertificateResponsecertificateDescriptiontransferDataTypeDef",
    {
        "transferMessage": str,
        "rejectReason": str,
        "transferDate": datetime,
        "acceptDate": datetime,
        "rejectDate": datetime,
    },
    total=False,
)


class ClientDescribeCertificateResponsecertificateDescriptiontransferDataTypeDef(
    _ClientDescribeCertificateResponsecertificateDescriptiontransferDataTypeDef
):
    """
    Type definition for `ClientDescribeCertificateResponsecertificateDescription` `transferData`

    The transfer data.

    - **transferMessage** *(string) --*

      The transfer message.

    - **rejectReason** *(string) --*

      The reason why the transfer was rejected.

    - **transferDate** *(datetime) --*

      The date the transfer took place.

    - **acceptDate** *(datetime) --*

      The date the transfer was accepted.

    - **rejectDate** *(datetime) --*

      The date the transfer was rejected.
    """


_ClientDescribeCertificateResponsecertificateDescriptionvalidityTypeDef = TypedDict(
    "_ClientDescribeCertificateResponsecertificateDescriptionvalidityTypeDef",
    {"notBefore": datetime, "notAfter": datetime},
    total=False,
)


class ClientDescribeCertificateResponsecertificateDescriptionvalidityTypeDef(
    _ClientDescribeCertificateResponsecertificateDescriptionvalidityTypeDef
):
    """
    Type definition for `ClientDescribeCertificateResponsecertificateDescription` `validity`

    When the certificate is valid.

    - **notBefore** *(datetime) --*

      The certificate is not valid before this date.

    - **notAfter** *(datetime) --*

      The certificate is not valid after this date.
    """


_ClientDescribeCertificateResponsecertificateDescriptionTypeDef = TypedDict(
    "_ClientDescribeCertificateResponsecertificateDescriptionTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "caCertificateId": str,
        "status": str,
        "certificatePem": str,
        "ownedBy": str,
        "previousOwnedBy": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "customerVersion": int,
        "transferData": ClientDescribeCertificateResponsecertificateDescriptiontransferDataTypeDef,
        "generationId": str,
        "validity": ClientDescribeCertificateResponsecertificateDescriptionvalidityTypeDef,
    },
    total=False,
)


class ClientDescribeCertificateResponsecertificateDescriptionTypeDef(
    _ClientDescribeCertificateResponsecertificateDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeCertificateResponse` `certificateDescription`

    The description of the certificate.

    - **certificateArn** *(string) --*

      The ARN of the certificate.

    - **certificateId** *(string) --*

      The ID of the certificate.

    - **caCertificateId** *(string) --*

      The certificate ID of the CA certificate used to sign this certificate.

    - **status** *(string) --*

      The status of the certificate.

    - **certificatePem** *(string) --*

      The certificate data, in PEM format.

    - **ownedBy** *(string) --*

      The ID of the AWS account that owns the certificate.

    - **previousOwnedBy** *(string) --*

      The ID of the AWS account of the previous owner of the certificate.

    - **creationDate** *(datetime) --*

      The date and time the certificate was created.

    - **lastModifiedDate** *(datetime) --*

      The date and time the certificate was last modified.

    - **customerVersion** *(integer) --*

      The customer version of the certificate.

    - **transferData** *(dict) --*

      The transfer data.

      - **transferMessage** *(string) --*

        The transfer message.

      - **rejectReason** *(string) --*

        The reason why the transfer was rejected.

      - **transferDate** *(datetime) --*

        The date the transfer took place.

      - **acceptDate** *(datetime) --*

        The date the transfer was accepted.

      - **rejectDate** *(datetime) --*

        The date the transfer was rejected.

    - **generationId** *(string) --*

      The generation ID of the certificate.

    - **validity** *(dict) --*

      When the certificate is valid.

      - **notBefore** *(datetime) --*

        The certificate is not valid before this date.

      - **notAfter** *(datetime) --*

        The certificate is not valid after this date.
    """


_ClientDescribeCertificateResponseTypeDef = TypedDict(
    "_ClientDescribeCertificateResponseTypeDef",
    {
        "certificateDescription": ClientDescribeCertificateResponsecertificateDescriptionTypeDef
    },
    total=False,
)


class ClientDescribeCertificateResponseTypeDef(
    _ClientDescribeCertificateResponseTypeDef
):
    """
    Type definition for `ClientDescribeCertificate` `Response`

    The output of the DescribeCertificate operation.

    - **certificateDescription** *(dict) --*

      The description of the certificate.

      - **certificateArn** *(string) --*

        The ARN of the certificate.

      - **certificateId** *(string) --*

        The ID of the certificate.

      - **caCertificateId** *(string) --*

        The certificate ID of the CA certificate used to sign this certificate.

      - **status** *(string) --*

        The status of the certificate.

      - **certificatePem** *(string) --*

        The certificate data, in PEM format.

      - **ownedBy** *(string) --*

        The ID of the AWS account that owns the certificate.

      - **previousOwnedBy** *(string) --*

        The ID of the AWS account of the previous owner of the certificate.

      - **creationDate** *(datetime) --*

        The date and time the certificate was created.

      - **lastModifiedDate** *(datetime) --*

        The date and time the certificate was last modified.

      - **customerVersion** *(integer) --*

        The customer version of the certificate.

      - **transferData** *(dict) --*

        The transfer data.

        - **transferMessage** *(string) --*

          The transfer message.

        - **rejectReason** *(string) --*

          The reason why the transfer was rejected.

        - **transferDate** *(datetime) --*

          The date the transfer took place.

        - **acceptDate** *(datetime) --*

          The date the transfer was accepted.

        - **rejectDate** *(datetime) --*

          The date the transfer was rejected.

      - **generationId** *(string) --*

        The generation ID of the certificate.

      - **validity** *(dict) --*

        When the certificate is valid.

        - **notBefore** *(datetime) --*

          The certificate is not valid before this date.

        - **notAfter** *(datetime) --*

          The certificate is not valid after this date.
    """


_ClientDescribeDefaultAuthorizerResponseauthorizerDescriptionTypeDef = TypedDict(
    "_ClientDescribeDefaultAuthorizerResponseauthorizerDescriptionTypeDef",
    {
        "authorizerName": str,
        "authorizerArn": str,
        "authorizerFunctionArn": str,
        "tokenKeyName": str,
        "tokenSigningPublicKeys": Dict[str, str],
        "status": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeDefaultAuthorizerResponseauthorizerDescriptionTypeDef(
    _ClientDescribeDefaultAuthorizerResponseauthorizerDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeDefaultAuthorizerResponse` `authorizerDescription`

    The default authorizer's description.

    - **authorizerName** *(string) --*

      The authorizer name.

    - **authorizerArn** *(string) --*

      The authorizer ARN.

    - **authorizerFunctionArn** *(string) --*

      The authorizer's Lambda function ARN.

    - **tokenKeyName** *(string) --*

      The key used to extract the token from the HTTP headers.

    - **tokenSigningPublicKeys** *(dict) --*

      The public keys used to validate the token signature returned by your custom authentication
      service.

      - *(string) --*

        - *(string) --*

    - **status** *(string) --*

      The status of the authorizer.

    - **creationDate** *(datetime) --*

      The UNIX timestamp of when the authorizer was created.

    - **lastModifiedDate** *(datetime) --*

      The UNIX timestamp of when the authorizer was last updated.
    """


_ClientDescribeDefaultAuthorizerResponseTypeDef = TypedDict(
    "_ClientDescribeDefaultAuthorizerResponseTypeDef",
    {
        "authorizerDescription": ClientDescribeDefaultAuthorizerResponseauthorizerDescriptionTypeDef
    },
    total=False,
)


class ClientDescribeDefaultAuthorizerResponseTypeDef(
    _ClientDescribeDefaultAuthorizerResponseTypeDef
):
    """
    Type definition for `ClientDescribeDefaultAuthorizer` `Response`

    - **authorizerDescription** *(dict) --*

      The default authorizer's description.

      - **authorizerName** *(string) --*

        The authorizer name.

      - **authorizerArn** *(string) --*

        The authorizer ARN.

      - **authorizerFunctionArn** *(string) --*

        The authorizer's Lambda function ARN.

      - **tokenKeyName** *(string) --*

        The key used to extract the token from the HTTP headers.

      - **tokenSigningPublicKeys** *(dict) --*

        The public keys used to validate the token signature returned by your custom authentication
        service.

        - *(string) --*

          - *(string) --*

      - **status** *(string) --*

        The status of the authorizer.

      - **creationDate** *(datetime) --*

        The UNIX timestamp of when the authorizer was created.

      - **lastModifiedDate** *(datetime) --*

        The UNIX timestamp of when the authorizer was last updated.
    """


_ClientDescribeEndpointResponseTypeDef = TypedDict(
    "_ClientDescribeEndpointResponseTypeDef", {"endpointAddress": str}, total=False
)


class ClientDescribeEndpointResponseTypeDef(_ClientDescribeEndpointResponseTypeDef):
    """
    Type definition for `ClientDescribeEndpoint` `Response`

    The output from the DescribeEndpoint operation.

    - **endpointAddress** *(string) --*

      The endpoint. The format of the endpoint is as follows: *identifier* .iot.*region*
      .amazonaws.com.
    """


_ClientDescribeEventConfigurationsResponseeventConfigurationsTypeDef = TypedDict(
    "_ClientDescribeEventConfigurationsResponseeventConfigurationsTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientDescribeEventConfigurationsResponseeventConfigurationsTypeDef(
    _ClientDescribeEventConfigurationsResponseeventConfigurationsTypeDef
):
    """
    Type definition for `ClientDescribeEventConfigurationsResponse` `eventConfigurations`

    Configuration.

    - **Enabled** *(boolean) --*

      True to enable the configuration.
    """


_ClientDescribeEventConfigurationsResponseTypeDef = TypedDict(
    "_ClientDescribeEventConfigurationsResponseTypeDef",
    {
        "eventConfigurations": Dict[
            str, ClientDescribeEventConfigurationsResponseeventConfigurationsTypeDef
        ],
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeEventConfigurationsResponseTypeDef(
    _ClientDescribeEventConfigurationsResponseTypeDef
):
    """
    Type definition for `ClientDescribeEventConfigurations` `Response`

    - **eventConfigurations** *(dict) --*

      The event configurations.

      - *(string) --*

        - *(dict) --*

          Configuration.

          - **Enabled** *(boolean) --*

            True to enable the configuration.

    - **creationDate** *(datetime) --*

      The creation date of the event configuration.

    - **lastModifiedDate** *(datetime) --*

      The date the event configurations were last modified.
    """


_ClientDescribeIndexResponseTypeDef = TypedDict(
    "_ClientDescribeIndexResponseTypeDef",
    {"indexName": str, "indexStatus": str, "schema": str},
    total=False,
)


class ClientDescribeIndexResponseTypeDef(_ClientDescribeIndexResponseTypeDef):
    """
    Type definition for `ClientDescribeIndex` `Response`

    - **indexName** *(string) --*

      The index name.

    - **indexStatus** *(string) --*

      The index status.

    - **schema** *(string) --*

      Contains a value that specifies the type of indexing performed. Valid values are:

      * REGISTRY – Your thing index contains only registry data.

      * REGISTRY_AND_SHADOW - Your thing index contains registry data and shadow data.

      * REGISTRY_AND_CONNECTIVITY_STATUS - Your thing index contains registry data and thing
      connectivity status data.

      * REGISTRY_AND_SHADOW_AND_CONNECTIVITY_STATUS - Your thing index contains registry data,
      shadow data, and thing connectivity status data.
    """


_ClientDescribeJobExecutionResponseexecutionstatusDetailsTypeDef = TypedDict(
    "_ClientDescribeJobExecutionResponseexecutionstatusDetailsTypeDef",
    {"detailsMap": Dict[str, str]},
    total=False,
)


class ClientDescribeJobExecutionResponseexecutionstatusDetailsTypeDef(
    _ClientDescribeJobExecutionResponseexecutionstatusDetailsTypeDef
):
    """
    Type definition for `ClientDescribeJobExecutionResponseexecution` `statusDetails`

    A collection of name/value pairs that describe the status of the job execution.

    - **detailsMap** *(dict) --*

      The job execution status.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeJobExecutionResponseexecutionTypeDef = TypedDict(
    "_ClientDescribeJobExecutionResponseexecutionTypeDef",
    {
        "jobId": str,
        "status": str,
        "forceCanceled": bool,
        "statusDetails": ClientDescribeJobExecutionResponseexecutionstatusDetailsTypeDef,
        "thingArn": str,
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
        "versionNumber": int,
        "approximateSecondsBeforeTimedOut": int,
    },
    total=False,
)


class ClientDescribeJobExecutionResponseexecutionTypeDef(
    _ClientDescribeJobExecutionResponseexecutionTypeDef
):
    """
    Type definition for `ClientDescribeJobExecutionResponse` `execution`

    Information about the job execution.

    - **jobId** *(string) --*

      The unique identifier you assigned to the job when it was created.

    - **status** *(string) --*

      The status of the job execution (IN_PROGRESS, QUEUED, FAILED, SUCCEEDED, TIMED_OUT,
      CANCELED, or REJECTED).

    - **forceCanceled** *(boolean) --*

      Will be ``true`` if the job execution was canceled with the optional ``force`` parameter
      set to ``true`` .

    - **statusDetails** *(dict) --*

      A collection of name/value pairs that describe the status of the job execution.

      - **detailsMap** *(dict) --*

        The job execution status.

        - *(string) --*

          - *(string) --*

    - **thingArn** *(string) --*

      The ARN of the thing on which the job execution is running.

    - **queuedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job execution was queued.

    - **startedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job execution started.

    - **lastUpdatedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job execution was last updated.

    - **executionNumber** *(integer) --*

      A string (consisting of the digits "0" through "9") which identifies this particular job
      execution on this particular device. It can be used in commands which return or update job
      execution information.

    - **versionNumber** *(integer) --*

      The version of the job execution. Job execution versions are incremented each time they are
      updated by a device.

    - **approximateSecondsBeforeTimedOut** *(integer) --*

      The estimated number of seconds that remain before the job execution status will be changed
      to ``TIMED_OUT`` . The timeout interval can be anywhere between 1 minute and 7 days (1 to
      10080 minutes). The actual job execution timeout can occur up to 60 seconds later than the
      estimated duration. This value will not be included if the job execution has reached a
      terminal status.
    """


_ClientDescribeJobExecutionResponseTypeDef = TypedDict(
    "_ClientDescribeJobExecutionResponseTypeDef",
    {"execution": ClientDescribeJobExecutionResponseexecutionTypeDef},
    total=False,
)


class ClientDescribeJobExecutionResponseTypeDef(
    _ClientDescribeJobExecutionResponseTypeDef
):
    """
    Type definition for `ClientDescribeJobExecution` `Response`

    - **execution** *(dict) --*

      Information about the job execution.

      - **jobId** *(string) --*

        The unique identifier you assigned to the job when it was created.

      - **status** *(string) --*

        The status of the job execution (IN_PROGRESS, QUEUED, FAILED, SUCCEEDED, TIMED_OUT,
        CANCELED, or REJECTED).

      - **forceCanceled** *(boolean) --*

        Will be ``true`` if the job execution was canceled with the optional ``force`` parameter
        set to ``true`` .

      - **statusDetails** *(dict) --*

        A collection of name/value pairs that describe the status of the job execution.

        - **detailsMap** *(dict) --*

          The job execution status.

          - *(string) --*

            - *(string) --*

      - **thingArn** *(string) --*

        The ARN of the thing on which the job execution is running.

      - **queuedAt** *(datetime) --*

        The time, in seconds since the epoch, when the job execution was queued.

      - **startedAt** *(datetime) --*

        The time, in seconds since the epoch, when the job execution started.

      - **lastUpdatedAt** *(datetime) --*

        The time, in seconds since the epoch, when the job execution was last updated.

      - **executionNumber** *(integer) --*

        A string (consisting of the digits "0" through "9") which identifies this particular job
        execution on this particular device. It can be used in commands which return or update job
        execution information.

      - **versionNumber** *(integer) --*

        The version of the job execution. Job execution versions are incremented each time they are
        updated by a device.

      - **approximateSecondsBeforeTimedOut** *(integer) --*

        The estimated number of seconds that remain before the job execution status will be changed
        to ``TIMED_OUT`` . The timeout interval can be anywhere between 1 minute and 7 days (1 to
        10080 minutes). The actual job execution timeout can occur up to 60 seconds later than the
        estimated duration. This value will not be included if the job execution has reached a
        terminal status.
    """


_ClientDescribeJobResponsejobabortConfigcriteriaListTypeDef = TypedDict(
    "_ClientDescribeJobResponsejobabortConfigcriteriaListTypeDef",
    {
        "failureType": str,
        "action": str,
        "thresholdPercentage": float,
        "minNumberOfExecutedThings": int,
    },
    total=False,
)


class ClientDescribeJobResponsejobabortConfigcriteriaListTypeDef(
    _ClientDescribeJobResponsejobabortConfigcriteriaListTypeDef
):
    """
    Type definition for `ClientDescribeJobResponsejobabortConfig` `criteriaList`

    Details of abort criteria to define rules to abort the job.

    - **failureType** *(string) --*

      The type of job execution failure to define a rule to initiate a job abort.

    - **action** *(string) --*

      The type of abort action to initiate a job abort.

    - **thresholdPercentage** *(float) --*

      The threshold as a percentage of the total number of executed things that will
      initiate a job abort.

      AWS IoT supports up to two digits after the decimal (for example, 10.9 and 10.99, but
      not 10.999).

    - **minNumberOfExecutedThings** *(integer) --*

      Minimum number of executed things before evaluating an abort rule.
    """


_ClientDescribeJobResponsejobabortConfigTypeDef = TypedDict(
    "_ClientDescribeJobResponsejobabortConfigTypeDef",
    {"criteriaList": List[ClientDescribeJobResponsejobabortConfigcriteriaListTypeDef]},
    total=False,
)


class ClientDescribeJobResponsejobabortConfigTypeDef(
    _ClientDescribeJobResponsejobabortConfigTypeDef
):
    """
    Type definition for `ClientDescribeJobResponsejob` `abortConfig`

    Configuration for criteria to abort the job.

    - **criteriaList** *(list) --*

      The list of abort criteria to define rules to abort the job.

      - *(dict) --*

        Details of abort criteria to define rules to abort the job.

        - **failureType** *(string) --*

          The type of job execution failure to define a rule to initiate a job abort.

        - **action** *(string) --*

          The type of abort action to initiate a job abort.

        - **thresholdPercentage** *(float) --*

          The threshold as a percentage of the total number of executed things that will
          initiate a job abort.

          AWS IoT supports up to two digits after the decimal (for example, 10.9 and 10.99, but
          not 10.999).

        - **minNumberOfExecutedThings** *(integer) --*

          Minimum number of executed things before evaluating an abort rule.
    """


_ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef = TypedDict(
    "_ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef",
    {"numberOfNotifiedThings": int, "numberOfSucceededThings": int},
    total=False,
)


class ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef(
    _ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef
):
    """
    Type definition for `ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRate` `rateIncreaseCriteria`

    The criteria to initiate the increase in rate of rollout for a job.

    AWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).

    - **numberOfNotifiedThings** *(integer) --*

      The threshold for number of notified things that will initiate the increase in rate
      of rollout.

    - **numberOfSucceededThings** *(integer) --*

      The threshold for number of succeeded things that will initiate the increase in rate
      of rollout.
    """


_ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRateTypeDef = TypedDict(
    "_ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRateTypeDef(
    _ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRateTypeDef
):
    """
    Type definition for `ClientDescribeJobResponsejobjobExecutionsRolloutConfig` `exponentialRate`

    The rate of increase for a job rollout. This parameter allows you to define an
    exponential rate for a job rollout.

    - **baseRatePerMinute** *(integer) --*

      The minimum number of things that will be notified of a pending job, per minute at the
      start of job rollout. This parameter allows you to define the initial rate of rollout.

    - **incrementFactor** *(float) --*

      The exponential factor to increase the rate of rollout for a job.

    - **rateIncreaseCriteria** *(dict) --*

      The criteria to initiate the increase in rate of rollout for a job.

      AWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).

      - **numberOfNotifiedThings** *(integer) --*

        The threshold for number of notified things that will initiate the increase in rate
        of rollout.

      - **numberOfSucceededThings** *(integer) --*

        The threshold for number of succeeded things that will initiate the increase in rate
        of rollout.
    """


_ClientDescribeJobResponsejobjobExecutionsRolloutConfigTypeDef = TypedDict(
    "_ClientDescribeJobResponsejobjobExecutionsRolloutConfigTypeDef",
    {
        "maximumPerMinute": int,
        "exponentialRate": ClientDescribeJobResponsejobjobExecutionsRolloutConfigexponentialRateTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponsejobjobExecutionsRolloutConfigTypeDef(
    _ClientDescribeJobResponsejobjobExecutionsRolloutConfigTypeDef
):
    """
    Type definition for `ClientDescribeJobResponsejob` `jobExecutionsRolloutConfig`

    Allows you to create a staged rollout of a job.

    - **maximumPerMinute** *(integer) --*

      The maximum number of things that will be notified of a pending job, per minute. This
      parameter allows you to create a staged rollout.

    - **exponentialRate** *(dict) --*

      The rate of increase for a job rollout. This parameter allows you to define an
      exponential rate for a job rollout.

      - **baseRatePerMinute** *(integer) --*

        The minimum number of things that will be notified of a pending job, per minute at the
        start of job rollout. This parameter allows you to define the initial rate of rollout.

      - **incrementFactor** *(float) --*

        The exponential factor to increase the rate of rollout for a job.

      - **rateIncreaseCriteria** *(dict) --*

        The criteria to initiate the increase in rate of rollout for a job.

        AWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).

        - **numberOfNotifiedThings** *(integer) --*

          The threshold for number of notified things that will initiate the increase in rate
          of rollout.

        - **numberOfSucceededThings** *(integer) --*

          The threshold for number of succeeded things that will initiate the increase in rate
          of rollout.
    """


_ClientDescribeJobResponsejobjobProcessDetailsTypeDef = TypedDict(
    "_ClientDescribeJobResponsejobjobProcessDetailsTypeDef",
    {
        "processingTargets": List[str],
        "numberOfCanceledThings": int,
        "numberOfSucceededThings": int,
        "numberOfFailedThings": int,
        "numberOfRejectedThings": int,
        "numberOfQueuedThings": int,
        "numberOfInProgressThings": int,
        "numberOfRemovedThings": int,
        "numberOfTimedOutThings": int,
    },
    total=False,
)


class ClientDescribeJobResponsejobjobProcessDetailsTypeDef(
    _ClientDescribeJobResponsejobjobProcessDetailsTypeDef
):
    """
    Type definition for `ClientDescribeJobResponsejob` `jobProcessDetails`

    Details about the job process.

    - **processingTargets** *(list) --*

      The target devices to which the job execution is being rolled out. This value will be
      null after the job execution has finished rolling out to all the target devices.

      - *(string) --*

    - **numberOfCanceledThings** *(integer) --*

      The number of things that cancelled the job.

    - **numberOfSucceededThings** *(integer) --*

      The number of things which successfully completed the job.

    - **numberOfFailedThings** *(integer) --*

      The number of things that failed executing the job.

    - **numberOfRejectedThings** *(integer) --*

      The number of things that rejected the job.

    - **numberOfQueuedThings** *(integer) --*

      The number of things that are awaiting execution of the job.

    - **numberOfInProgressThings** *(integer) --*

      The number of things currently executing the job.

    - **numberOfRemovedThings** *(integer) --*

      The number of things that are no longer scheduled to execute the job because they have
      been deleted or have been removed from the group that was a target of the job.

    - **numberOfTimedOutThings** *(integer) --*

      The number of things whose job execution status is ``TIMED_OUT`` .
    """


_ClientDescribeJobResponsejobpresignedUrlConfigTypeDef = TypedDict(
    "_ClientDescribeJobResponsejobpresignedUrlConfigTypeDef",
    {"roleArn": str, "expiresInSec": int},
    total=False,
)


class ClientDescribeJobResponsejobpresignedUrlConfigTypeDef(
    _ClientDescribeJobResponsejobpresignedUrlConfigTypeDef
):
    """
    Type definition for `ClientDescribeJobResponsejob` `presignedUrlConfig`

    Configuration for pre-signed S3 URLs.

    - **roleArn** *(string) --*

      The ARN of an IAM role that grants grants permission to download files from the S3 bucket
      where the job data/updates are stored. The role must also grant permission for IoT to
      download the files.

    - **expiresInSec** *(integer) --*

      How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default
      value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request
      for the job document.
    """


_ClientDescribeJobResponsejobtimeoutConfigTypeDef = TypedDict(
    "_ClientDescribeJobResponsejobtimeoutConfigTypeDef",
    {"inProgressTimeoutInMinutes": int},
    total=False,
)


class ClientDescribeJobResponsejobtimeoutConfigTypeDef(
    _ClientDescribeJobResponsejobtimeoutConfigTypeDef
):
    """
    Type definition for `ClientDescribeJobResponsejob` `timeoutConfig`

    Specifies the amount of time each device has to finish its execution of the job. A timer is
    started when the job execution status is set to ``IN_PROGRESS`` . If the job execution
    status is not set to another terminal state before the timer expires, it will be
    automatically set to ``TIMED_OUT`` .

    - **inProgressTimeoutInMinutes** *(integer) --*

      Specifies the amount of time, in minutes, this device has to finish execution of this
      job. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080
      minutes). The in progress timer can't be updated and will apply to all job executions for
      the job. Whenever a job execution remains in the IN_PROGRESS status for longer than this
      interval, the job execution will fail and switch to the terminal ``TIMED_OUT`` status.
    """


_ClientDescribeJobResponsejobTypeDef = TypedDict(
    "_ClientDescribeJobResponsejobTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "targetSelection": str,
        "status": str,
        "forceCanceled": bool,
        "reasonCode": str,
        "comment": str,
        "targets": List[str],
        "description": str,
        "presignedUrlConfig": ClientDescribeJobResponsejobpresignedUrlConfigTypeDef,
        "jobExecutionsRolloutConfig": ClientDescribeJobResponsejobjobExecutionsRolloutConfigTypeDef,
        "abortConfig": ClientDescribeJobResponsejobabortConfigTypeDef,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "completedAt": datetime,
        "jobProcessDetails": ClientDescribeJobResponsejobjobProcessDetailsTypeDef,
        "timeoutConfig": ClientDescribeJobResponsejobtimeoutConfigTypeDef,
    },
    total=False,
)


class ClientDescribeJobResponsejobTypeDef(_ClientDescribeJobResponsejobTypeDef):
    """
    Type definition for `ClientDescribeJobResponse` `job`

    Information about the job.

    - **jobArn** *(string) --*

      An ARN identifying the job with format "arn:aws:iot:region:account:job/jobId".

    - **jobId** *(string) --*

      The unique identifier you assigned to this job when it was created.

    - **targetSelection** *(string) --*

      Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all
      those things specified as targets have completed the job (SNAPSHOT). If continuous, the job
      may also be run on a thing when a change is detected in a target. For example, a job will
      run on a device when the thing representing the device is added to a target group, even
      after the job was completed by all things originally in the group.

    - **status** *(string) --*

      The status of the job, one of ``IN_PROGRESS`` , ``CANCELED`` , ``DELETION_IN_PROGRESS`` or
      ``COMPLETED`` .

    - **forceCanceled** *(boolean) --*

      Will be ``true`` if the job was canceled with the optional ``force`` parameter set to
      ``true`` .

    - **reasonCode** *(string) --*

      If the job was updated, provides the reason code for the update.

    - **comment** *(string) --*

      If the job was updated, describes the reason for the update.

    - **targets** *(list) --*

      A list of IoT things and thing groups to which the job should be sent.

      - *(string) --*

    - **description** *(string) --*

      A short text description of the job.

    - **presignedUrlConfig** *(dict) --*

      Configuration for pre-signed S3 URLs.

      - **roleArn** *(string) --*

        The ARN of an IAM role that grants grants permission to download files from the S3 bucket
        where the job data/updates are stored. The role must also grant permission for IoT to
        download the files.

      - **expiresInSec** *(integer) --*

        How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default
        value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request
        for the job document.

    - **jobExecutionsRolloutConfig** *(dict) --*

      Allows you to create a staged rollout of a job.

      - **maximumPerMinute** *(integer) --*

        The maximum number of things that will be notified of a pending job, per minute. This
        parameter allows you to create a staged rollout.

      - **exponentialRate** *(dict) --*

        The rate of increase for a job rollout. This parameter allows you to define an
        exponential rate for a job rollout.

        - **baseRatePerMinute** *(integer) --*

          The minimum number of things that will be notified of a pending job, per minute at the
          start of job rollout. This parameter allows you to define the initial rate of rollout.

        - **incrementFactor** *(float) --*

          The exponential factor to increase the rate of rollout for a job.

        - **rateIncreaseCriteria** *(dict) --*

          The criteria to initiate the increase in rate of rollout for a job.

          AWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).

          - **numberOfNotifiedThings** *(integer) --*

            The threshold for number of notified things that will initiate the increase in rate
            of rollout.

          - **numberOfSucceededThings** *(integer) --*

            The threshold for number of succeeded things that will initiate the increase in rate
            of rollout.

    - **abortConfig** *(dict) --*

      Configuration for criteria to abort the job.

      - **criteriaList** *(list) --*

        The list of abort criteria to define rules to abort the job.

        - *(dict) --*

          Details of abort criteria to define rules to abort the job.

          - **failureType** *(string) --*

            The type of job execution failure to define a rule to initiate a job abort.

          - **action** *(string) --*

            The type of abort action to initiate a job abort.

          - **thresholdPercentage** *(float) --*

            The threshold as a percentage of the total number of executed things that will
            initiate a job abort.

            AWS IoT supports up to two digits after the decimal (for example, 10.9 and 10.99, but
            not 10.999).

          - **minNumberOfExecutedThings** *(integer) --*

            Minimum number of executed things before evaluating an abort rule.

    - **createdAt** *(datetime) --*

      The time, in seconds since the epoch, when the job was created.

    - **lastUpdatedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job was last updated.

    - **completedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job was completed.

    - **jobProcessDetails** *(dict) --*

      Details about the job process.

      - **processingTargets** *(list) --*

        The target devices to which the job execution is being rolled out. This value will be
        null after the job execution has finished rolling out to all the target devices.

        - *(string) --*

      - **numberOfCanceledThings** *(integer) --*

        The number of things that cancelled the job.

      - **numberOfSucceededThings** *(integer) --*

        The number of things which successfully completed the job.

      - **numberOfFailedThings** *(integer) --*

        The number of things that failed executing the job.

      - **numberOfRejectedThings** *(integer) --*

        The number of things that rejected the job.

      - **numberOfQueuedThings** *(integer) --*

        The number of things that are awaiting execution of the job.

      - **numberOfInProgressThings** *(integer) --*

        The number of things currently executing the job.

      - **numberOfRemovedThings** *(integer) --*

        The number of things that are no longer scheduled to execute the job because they have
        been deleted or have been removed from the group that was a target of the job.

      - **numberOfTimedOutThings** *(integer) --*

        The number of things whose job execution status is ``TIMED_OUT`` .

    - **timeoutConfig** *(dict) --*

      Specifies the amount of time each device has to finish its execution of the job. A timer is
      started when the job execution status is set to ``IN_PROGRESS`` . If the job execution
      status is not set to another terminal state before the timer expires, it will be
      automatically set to ``TIMED_OUT`` .

      - **inProgressTimeoutInMinutes** *(integer) --*

        Specifies the amount of time, in minutes, this device has to finish execution of this
        job. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080
        minutes). The in progress timer can't be updated and will apply to all job executions for
        the job. Whenever a job execution remains in the IN_PROGRESS status for longer than this
        interval, the job execution will fail and switch to the terminal ``TIMED_OUT`` status.
    """


_ClientDescribeJobResponseTypeDef = TypedDict(
    "_ClientDescribeJobResponseTypeDef",
    {"documentSource": str, "job": ClientDescribeJobResponsejobTypeDef},
    total=False,
)


class ClientDescribeJobResponseTypeDef(_ClientDescribeJobResponseTypeDef):
    """
    Type definition for `ClientDescribeJob` `Response`

    - **documentSource** *(string) --*

      An S3 link to the job document.

    - **job** *(dict) --*

      Information about the job.

      - **jobArn** *(string) --*

        An ARN identifying the job with format "arn:aws:iot:region:account:job/jobId".

      - **jobId** *(string) --*

        The unique identifier you assigned to this job when it was created.

      - **targetSelection** *(string) --*

        Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all
        those things specified as targets have completed the job (SNAPSHOT). If continuous, the job
        may also be run on a thing when a change is detected in a target. For example, a job will
        run on a device when the thing representing the device is added to a target group, even
        after the job was completed by all things originally in the group.

      - **status** *(string) --*

        The status of the job, one of ``IN_PROGRESS`` , ``CANCELED`` , ``DELETION_IN_PROGRESS`` or
        ``COMPLETED`` .

      - **forceCanceled** *(boolean) --*

        Will be ``true`` if the job was canceled with the optional ``force`` parameter set to
        ``true`` .

      - **reasonCode** *(string) --*

        If the job was updated, provides the reason code for the update.

      - **comment** *(string) --*

        If the job was updated, describes the reason for the update.

      - **targets** *(list) --*

        A list of IoT things and thing groups to which the job should be sent.

        - *(string) --*

      - **description** *(string) --*

        A short text description of the job.

      - **presignedUrlConfig** *(dict) --*

        Configuration for pre-signed S3 URLs.

        - **roleArn** *(string) --*

          The ARN of an IAM role that grants grants permission to download files from the S3 bucket
          where the job data/updates are stored. The role must also grant permission for IoT to
          download the files.

        - **expiresInSec** *(integer) --*

          How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default
          value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request
          for the job document.

      - **jobExecutionsRolloutConfig** *(dict) --*

        Allows you to create a staged rollout of a job.

        - **maximumPerMinute** *(integer) --*

          The maximum number of things that will be notified of a pending job, per minute. This
          parameter allows you to create a staged rollout.

        - **exponentialRate** *(dict) --*

          The rate of increase for a job rollout. This parameter allows you to define an
          exponential rate for a job rollout.

          - **baseRatePerMinute** *(integer) --*

            The minimum number of things that will be notified of a pending job, per minute at the
            start of job rollout. This parameter allows you to define the initial rate of rollout.

          - **incrementFactor** *(float) --*

            The exponential factor to increase the rate of rollout for a job.

          - **rateIncreaseCriteria** *(dict) --*

            The criteria to initiate the increase in rate of rollout for a job.

            AWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).

            - **numberOfNotifiedThings** *(integer) --*

              The threshold for number of notified things that will initiate the increase in rate
              of rollout.

            - **numberOfSucceededThings** *(integer) --*

              The threshold for number of succeeded things that will initiate the increase in rate
              of rollout.

      - **abortConfig** *(dict) --*

        Configuration for criteria to abort the job.

        - **criteriaList** *(list) --*

          The list of abort criteria to define rules to abort the job.

          - *(dict) --*

            Details of abort criteria to define rules to abort the job.

            - **failureType** *(string) --*

              The type of job execution failure to define a rule to initiate a job abort.

            - **action** *(string) --*

              The type of abort action to initiate a job abort.

            - **thresholdPercentage** *(float) --*

              The threshold as a percentage of the total number of executed things that will
              initiate a job abort.

              AWS IoT supports up to two digits after the decimal (for example, 10.9 and 10.99, but
              not 10.999).

            - **minNumberOfExecutedThings** *(integer) --*

              Minimum number of executed things before evaluating an abort rule.

      - **createdAt** *(datetime) --*

        The time, in seconds since the epoch, when the job was created.

      - **lastUpdatedAt** *(datetime) --*

        The time, in seconds since the epoch, when the job was last updated.

      - **completedAt** *(datetime) --*

        The time, in seconds since the epoch, when the job was completed.

      - **jobProcessDetails** *(dict) --*

        Details about the job process.

        - **processingTargets** *(list) --*

          The target devices to which the job execution is being rolled out. This value will be
          null after the job execution has finished rolling out to all the target devices.

          - *(string) --*

        - **numberOfCanceledThings** *(integer) --*

          The number of things that cancelled the job.

        - **numberOfSucceededThings** *(integer) --*

          The number of things which successfully completed the job.

        - **numberOfFailedThings** *(integer) --*

          The number of things that failed executing the job.

        - **numberOfRejectedThings** *(integer) --*

          The number of things that rejected the job.

        - **numberOfQueuedThings** *(integer) --*

          The number of things that are awaiting execution of the job.

        - **numberOfInProgressThings** *(integer) --*

          The number of things currently executing the job.

        - **numberOfRemovedThings** *(integer) --*

          The number of things that are no longer scheduled to execute the job because they have
          been deleted or have been removed from the group that was a target of the job.

        - **numberOfTimedOutThings** *(integer) --*

          The number of things whose job execution status is ``TIMED_OUT`` .

      - **timeoutConfig** *(dict) --*

        Specifies the amount of time each device has to finish its execution of the job. A timer is
        started when the job execution status is set to ``IN_PROGRESS`` . If the job execution
        status is not set to another terminal state before the timer expires, it will be
        automatically set to ``TIMED_OUT`` .

        - **inProgressTimeoutInMinutes** *(integer) --*

          Specifies the amount of time, in minutes, this device has to finish execution of this
          job. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080
          minutes). The in progress timer can't be updated and will apply to all job executions for
          the job. Whenever a job execution remains in the IN_PROGRESS status for longer than this
          interval, the job execution will fail and switch to the terminal ``TIMED_OUT`` status.
    """


_ClientDescribeMitigationActionResponseactionParamsaddThingsToThingGroupParamsTypeDef = TypedDict(
    "_ClientDescribeMitigationActionResponseactionParamsaddThingsToThingGroupParamsTypeDef",
    {"thingGroupNames": List[str], "overrideDynamicGroups": bool},
    total=False,
)


class ClientDescribeMitigationActionResponseactionParamsaddThingsToThingGroupParamsTypeDef(
    _ClientDescribeMitigationActionResponseactionParamsaddThingsToThingGroupParamsTypeDef
):
    """
    Type definition for `ClientDescribeMitigationActionResponseactionParams` `addThingsToThingGroupParams`

    Parameters to define a mitigation action that moves devices associated with a certificate
    to one or more specified thing groups, typically for quarantine.

    - **thingGroupNames** *(list) --*

      The list of groups to which you want to add the things that triggered the mitigation
      action. You can add a thing to a maximum of 10 groups, but you cannot add a thing to more
      than one group in the same hierarchy.

      - *(string) --*

    - **overrideDynamicGroups** *(boolean) --*

      Specifies if this mitigation action can move the things that triggered the mitigation
      action even if they are part of one or more dynamic things groups.
    """


_ClientDescribeMitigationActionResponseactionParamsenableIoTLoggingParamsTypeDef = TypedDict(
    "_ClientDescribeMitigationActionResponseactionParamsenableIoTLoggingParamsTypeDef",
    {"roleArnForLogging": str, "logLevel": str},
    total=False,
)


class ClientDescribeMitigationActionResponseactionParamsenableIoTLoggingParamsTypeDef(
    _ClientDescribeMitigationActionResponseactionParamsenableIoTLoggingParamsTypeDef
):
    """
    Type definition for `ClientDescribeMitigationActionResponseactionParams` `enableIoTLoggingParams`

    Parameters to define a mitigation action that enables AWS IoT logging at a specified level
    of detail.

    - **roleArnForLogging** *(string) --*

      The ARN of the IAM role used for logging.

    - **logLevel** *(string) --*

      Specifies the types of information to be logged.
    """


_ClientDescribeMitigationActionResponseactionParamspublishFindingToSnsParamsTypeDef = TypedDict(
    "_ClientDescribeMitigationActionResponseactionParamspublishFindingToSnsParamsTypeDef",
    {"topicArn": str},
    total=False,
)


class ClientDescribeMitigationActionResponseactionParamspublishFindingToSnsParamsTypeDef(
    _ClientDescribeMitigationActionResponseactionParamspublishFindingToSnsParamsTypeDef
):
    """
    Type definition for `ClientDescribeMitigationActionResponseactionParams` `publishFindingToSnsParams`

    Parameters to define a mitigation action that publishes findings to Amazon SNS. You can
    implement your own custom actions in response to the Amazon SNS messages.

    - **topicArn** *(string) --*

      The ARN of the topic to which you want to publish the findings.
    """


_ClientDescribeMitigationActionResponseactionParamsreplaceDefaultPolicyVersionParamsTypeDef = TypedDict(
    "_ClientDescribeMitigationActionResponseactionParamsreplaceDefaultPolicyVersionParamsTypeDef",
    {"templateName": str},
    total=False,
)


class ClientDescribeMitigationActionResponseactionParamsreplaceDefaultPolicyVersionParamsTypeDef(
    _ClientDescribeMitigationActionResponseactionParamsreplaceDefaultPolicyVersionParamsTypeDef
):
    """
    Type definition for `ClientDescribeMitigationActionResponseactionParams` `replaceDefaultPolicyVersionParams`

    Parameters to define a mitigation action that adds a blank policy to restrict permissions.

    - **templateName** *(string) --*

      The name of the template to be applied. The only supported value is ``BLANK_POLICY`` .
    """


_ClientDescribeMitigationActionResponseactionParamsupdateCACertificateParamsTypeDef = TypedDict(
    "_ClientDescribeMitigationActionResponseactionParamsupdateCACertificateParamsTypeDef",
    {"action": str},
    total=False,
)


class ClientDescribeMitigationActionResponseactionParamsupdateCACertificateParamsTypeDef(
    _ClientDescribeMitigationActionResponseactionParamsupdateCACertificateParamsTypeDef
):
    """
    Type definition for `ClientDescribeMitigationActionResponseactionParams` `updateCACertificateParams`

    Parameters to define a mitigation action that changes the state of the CA certificate to
    inactive.

    - **action** *(string) --*

      The action that you want to apply to the CA cerrtificate. The only supported value is
      ``DEACTIVATE`` .
    """


_ClientDescribeMitigationActionResponseactionParamsupdateDeviceCertificateParamsTypeDef = TypedDict(
    "_ClientDescribeMitigationActionResponseactionParamsupdateDeviceCertificateParamsTypeDef",
    {"action": str},
    total=False,
)


class ClientDescribeMitigationActionResponseactionParamsupdateDeviceCertificateParamsTypeDef(
    _ClientDescribeMitigationActionResponseactionParamsupdateDeviceCertificateParamsTypeDef
):
    """
    Type definition for `ClientDescribeMitigationActionResponseactionParams` `updateDeviceCertificateParams`

    Parameters to define a mitigation action that changes the state of the device certificate
    to inactive.

    - **action** *(string) --*

      The action that you want to apply to the device cerrtificate. The only supported value is
      ``DEACTIVATE`` .
    """


_ClientDescribeMitigationActionResponseactionParamsTypeDef = TypedDict(
    "_ClientDescribeMitigationActionResponseactionParamsTypeDef",
    {
        "updateDeviceCertificateParams": ClientDescribeMitigationActionResponseactionParamsupdateDeviceCertificateParamsTypeDef,
        "updateCACertificateParams": ClientDescribeMitigationActionResponseactionParamsupdateCACertificateParamsTypeDef,
        "addThingsToThingGroupParams": ClientDescribeMitigationActionResponseactionParamsaddThingsToThingGroupParamsTypeDef,
        "replaceDefaultPolicyVersionParams": ClientDescribeMitigationActionResponseactionParamsreplaceDefaultPolicyVersionParamsTypeDef,
        "enableIoTLoggingParams": ClientDescribeMitigationActionResponseactionParamsenableIoTLoggingParamsTypeDef,
        "publishFindingToSnsParams": ClientDescribeMitigationActionResponseactionParamspublishFindingToSnsParamsTypeDef,
    },
    total=False,
)


class ClientDescribeMitigationActionResponseactionParamsTypeDef(
    _ClientDescribeMitigationActionResponseactionParamsTypeDef
):
    """
    Type definition for `ClientDescribeMitigationActionResponse` `actionParams`

    Parameters that control how the mitigation action is applied, specific to the type of
    mitigation action.

    - **updateDeviceCertificateParams** *(dict) --*

      Parameters to define a mitigation action that changes the state of the device certificate
      to inactive.

      - **action** *(string) --*

        The action that you want to apply to the device cerrtificate. The only supported value is
        ``DEACTIVATE`` .

    - **updateCACertificateParams** *(dict) --*

      Parameters to define a mitigation action that changes the state of the CA certificate to
      inactive.

      - **action** *(string) --*

        The action that you want to apply to the CA cerrtificate. The only supported value is
        ``DEACTIVATE`` .

    - **addThingsToThingGroupParams** *(dict) --*

      Parameters to define a mitigation action that moves devices associated with a certificate
      to one or more specified thing groups, typically for quarantine.

      - **thingGroupNames** *(list) --*

        The list of groups to which you want to add the things that triggered the mitigation
        action. You can add a thing to a maximum of 10 groups, but you cannot add a thing to more
        than one group in the same hierarchy.

        - *(string) --*

      - **overrideDynamicGroups** *(boolean) --*

        Specifies if this mitigation action can move the things that triggered the mitigation
        action even if they are part of one or more dynamic things groups.

    - **replaceDefaultPolicyVersionParams** *(dict) --*

      Parameters to define a mitigation action that adds a blank policy to restrict permissions.

      - **templateName** *(string) --*

        The name of the template to be applied. The only supported value is ``BLANK_POLICY`` .

    - **enableIoTLoggingParams** *(dict) --*

      Parameters to define a mitigation action that enables AWS IoT logging at a specified level
      of detail.

      - **roleArnForLogging** *(string) --*

        The ARN of the IAM role used for logging.

      - **logLevel** *(string) --*

        Specifies the types of information to be logged.

    - **publishFindingToSnsParams** *(dict) --*

      Parameters to define a mitigation action that publishes findings to Amazon SNS. You can
      implement your own custom actions in response to the Amazon SNS messages.

      - **topicArn** *(string) --*

        The ARN of the topic to which you want to publish the findings.
    """


_ClientDescribeMitigationActionResponseTypeDef = TypedDict(
    "_ClientDescribeMitigationActionResponseTypeDef",
    {
        "actionName": str,
        "actionType": str,
        "actionArn": str,
        "actionId": str,
        "roleArn": str,
        "actionParams": ClientDescribeMitigationActionResponseactionParamsTypeDef,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeMitigationActionResponseTypeDef(
    _ClientDescribeMitigationActionResponseTypeDef
):
    """
    Type definition for `ClientDescribeMitigationAction` `Response`

    - **actionName** *(string) --*

      The friendly name that uniquely identifies the mitigation action.

    - **actionType** *(string) --*

      The type of mitigation action.

    - **actionArn** *(string) --*

      The ARN that identifies this migration action.

    - **actionId** *(string) --*

      A unique identifier for this action.

    - **roleArn** *(string) --*

      The ARN of the IAM role used to apply this action.

    - **actionParams** *(dict) --*

      Parameters that control how the mitigation action is applied, specific to the type of
      mitigation action.

      - **updateDeviceCertificateParams** *(dict) --*

        Parameters to define a mitigation action that changes the state of the device certificate
        to inactive.

        - **action** *(string) --*

          The action that you want to apply to the device cerrtificate. The only supported value is
          ``DEACTIVATE`` .

      - **updateCACertificateParams** *(dict) --*

        Parameters to define a mitigation action that changes the state of the CA certificate to
        inactive.

        - **action** *(string) --*

          The action that you want to apply to the CA cerrtificate. The only supported value is
          ``DEACTIVATE`` .

      - **addThingsToThingGroupParams** *(dict) --*

        Parameters to define a mitigation action that moves devices associated with a certificate
        to one or more specified thing groups, typically for quarantine.

        - **thingGroupNames** *(list) --*

          The list of groups to which you want to add the things that triggered the mitigation
          action. You can add a thing to a maximum of 10 groups, but you cannot add a thing to more
          than one group in the same hierarchy.

          - *(string) --*

        - **overrideDynamicGroups** *(boolean) --*

          Specifies if this mitigation action can move the things that triggered the mitigation
          action even if they are part of one or more dynamic things groups.

      - **replaceDefaultPolicyVersionParams** *(dict) --*

        Parameters to define a mitigation action that adds a blank policy to restrict permissions.

        - **templateName** *(string) --*

          The name of the template to be applied. The only supported value is ``BLANK_POLICY`` .

      - **enableIoTLoggingParams** *(dict) --*

        Parameters to define a mitigation action that enables AWS IoT logging at a specified level
        of detail.

        - **roleArnForLogging** *(string) --*

          The ARN of the IAM role used for logging.

        - **logLevel** *(string) --*

          Specifies the types of information to be logged.

      - **publishFindingToSnsParams** *(dict) --*

        Parameters to define a mitigation action that publishes findings to Amazon SNS. You can
        implement your own custom actions in response to the Amazon SNS messages.

        - **topicArn** *(string) --*

          The ARN of the topic to which you want to publish the findings.

    - **creationDate** *(datetime) --*

      The date and time when the mitigation action was added to your AWS account.

    - **lastModifiedDate** *(datetime) --*

      The date and time when the mitigation action was last changed.
    """


_ClientDescribeRoleAliasResponseroleAliasDescriptionTypeDef = TypedDict(
    "_ClientDescribeRoleAliasResponseroleAliasDescriptionTypeDef",
    {
        "roleAlias": str,
        "roleAliasArn": str,
        "roleArn": str,
        "owner": str,
        "credentialDurationSeconds": int,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeRoleAliasResponseroleAliasDescriptionTypeDef(
    _ClientDescribeRoleAliasResponseroleAliasDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeRoleAliasResponse` `roleAliasDescription`

    The role alias description.

    - **roleAlias** *(string) --*

      The role alias.

    - **roleAliasArn** *(string) --*

      The ARN of the role alias.

    - **roleArn** *(string) --*

      The role ARN.

    - **owner** *(string) --*

      The role alias owner.

    - **credentialDurationSeconds** *(integer) --*

      The number of seconds for which the credential is valid.

    - **creationDate** *(datetime) --*

      The UNIX timestamp of when the role alias was created.

    - **lastModifiedDate** *(datetime) --*

      The UNIX timestamp of when the role alias was last modified.
    """


_ClientDescribeRoleAliasResponseTypeDef = TypedDict(
    "_ClientDescribeRoleAliasResponseTypeDef",
    {
        "roleAliasDescription": ClientDescribeRoleAliasResponseroleAliasDescriptionTypeDef
    },
    total=False,
)


class ClientDescribeRoleAliasResponseTypeDef(_ClientDescribeRoleAliasResponseTypeDef):
    """
    Type definition for `ClientDescribeRoleAlias` `Response`

    - **roleAliasDescription** *(dict) --*

      The role alias description.

      - **roleAlias** *(string) --*

        The role alias.

      - **roleAliasArn** *(string) --*

        The ARN of the role alias.

      - **roleArn** *(string) --*

        The role ARN.

      - **owner** *(string) --*

        The role alias owner.

      - **credentialDurationSeconds** *(integer) --*

        The number of seconds for which the credential is valid.

      - **creationDate** *(datetime) --*

        The UNIX timestamp of when the role alias was created.

      - **lastModifiedDate** *(datetime) --*

        The UNIX timestamp of when the role alias was last modified.
    """


_ClientDescribeScheduledAuditResponseTypeDef = TypedDict(
    "_ClientDescribeScheduledAuditResponseTypeDef",
    {
        "frequency": str,
        "dayOfMonth": str,
        "dayOfWeek": str,
        "targetCheckNames": List[str],
        "scheduledAuditName": str,
        "scheduledAuditArn": str,
    },
    total=False,
)


class ClientDescribeScheduledAuditResponseTypeDef(
    _ClientDescribeScheduledAuditResponseTypeDef
):
    """
    Type definition for `ClientDescribeScheduledAudit` `Response`

    - **frequency** *(string) --*

      How often the scheduled audit takes place. One of "DAILY", "WEEKLY", "BIWEEKLY", or
      "MONTHLY". The start time of each audit is determined by the system.

    - **dayOfMonth** *(string) --*

      The day of the month on which the scheduled audit takes place. Will be "1" through "31" or
      "LAST". If days 29-31 are specified, and the month does not have that many days, the audit
      takes place on the "LAST" day of the month.

    - **dayOfWeek** *(string) --*

      The day of the week on which the scheduled audit takes place. One of "SUN", "MON", "TUE",
      "WED", "THU", "FRI", or "SAT".

    - **targetCheckNames** *(list) --*

      Which checks are performed during the scheduled audit. Checks must be enabled for your
      account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks, including
      those that are enabled or use ``UpdateAccountAuditConfiguration`` to select which checks are
      enabled.)

      - *(string) --*

        An audit check name. Checks must be enabled for your account. (Use
        ``DescribeAccountAuditConfiguration`` to see the list of all checks, including those that
        are enabled or use ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)

    - **scheduledAuditName** *(string) --*

      The name of the scheduled audit.

    - **scheduledAuditArn** *(string) --*

      The ARN of the scheduled audit.
    """


_ClientDescribeSecurityProfileResponsealertTargetsTypeDef = TypedDict(
    "_ClientDescribeSecurityProfileResponsealertTargetsTypeDef",
    {"alertTargetArn": str, "roleArn": str},
    total=False,
)


class ClientDescribeSecurityProfileResponsealertTargetsTypeDef(
    _ClientDescribeSecurityProfileResponsealertTargetsTypeDef
):
    """
    Type definition for `ClientDescribeSecurityProfileResponse` `alertTargets`

    A structure containing the alert target ARN and the role ARN.

    - **alertTargetArn** *(string) --*

      The ARN of the notification target to which alerts are sent.

    - **roleArn** *(string) --*

      The ARN of the role that grants permission to send alerts to the notification target.
    """


_ClientDescribeSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef = TypedDict(
    "_ClientDescribeSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)


class ClientDescribeSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef(
    _ClientDescribeSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef
):
    """
    Type definition for `ClientDescribeSecurityProfileResponsebehaviorscriteria` `statisticalThreshold`

    A statistical ranking (percentile) which indicates a threshold value by which a
    behavior is determined to be in compliance or in violation of the behavior.

    - **statistic** *(string) --*

      The percentile which resolves to a threshold value by which compliance with a
      behavior is determined. Metrics are collected over the specified period
      (``durationSeconds`` ) from all reporting devices in your account and statistical
      ranks are calculated. Then, the measurements from a device are collected over the
      same period. If the accumulated measurements from the device fall above or below
      (``comparisonOperator`` ) the value associated with the percentile specified, then
      the device is considered to be in compliance with the behavior, otherwise a violation
      occurs.
    """


_ClientDescribeSecurityProfileResponsebehaviorscriteriavalueTypeDef = TypedDict(
    "_ClientDescribeSecurityProfileResponsebehaviorscriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ClientDescribeSecurityProfileResponsebehaviorscriteriavalueTypeDef(
    _ClientDescribeSecurityProfileResponsebehaviorscriteriavalueTypeDef
):
    """
    Type definition for `ClientDescribeSecurityProfileResponsebehaviorscriteria` `value`

    The value to be compared with the ``metric`` .

    - **count** *(integer) --*

      If the ``comparisonOperator`` calls for a numeric value, use this to specify that
      numeric value to be compared with the ``metric`` .

    - **cidrs** *(list) --*

      If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set
      to be compared with the ``metric`` .

      - *(string) --*

    - **ports** *(list) --*

      If the ``comparisonOperator`` calls for a set of ports, use this to specify that set
      to be compared with the ``metric`` .

      - *(integer) --*
    """


_ClientDescribeSecurityProfileResponsebehaviorscriteriaTypeDef = TypedDict(
    "_ClientDescribeSecurityProfileResponsebehaviorscriteriaTypeDef",
    {
        "comparisonOperator": str,
        "value": ClientDescribeSecurityProfileResponsebehaviorscriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientDescribeSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef,
    },
    total=False,
)


class ClientDescribeSecurityProfileResponsebehaviorscriteriaTypeDef(
    _ClientDescribeSecurityProfileResponsebehaviorscriteriaTypeDef
):
    """
    Type definition for `ClientDescribeSecurityProfileResponsebehaviors` `criteria`

    The criteria that determine if a device is behaving normally in regard to the ``metric`` .

    - **comparisonOperator** *(string) --*

      The operator that relates the thing measured (``metric`` ) to the criteria (containing
      a ``value`` or ``statisticalThreshold`` ).

    - **value** *(dict) --*

      The value to be compared with the ``metric`` .

      - **count** *(integer) --*

        If the ``comparisonOperator`` calls for a numeric value, use this to specify that
        numeric value to be compared with the ``metric`` .

      - **cidrs** *(list) --*

        If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set
        to be compared with the ``metric`` .

        - *(string) --*

      - **ports** *(list) --*

        If the ``comparisonOperator`` calls for a set of ports, use this to specify that set
        to be compared with the ``metric`` .

        - *(integer) --*

    - **durationSeconds** *(integer) --*

      Use this to specify the time duration over which the behavior is evaluated, for those
      criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
      ``statisticalThreshhold`` metric comparison, measurements from all devices are
      accumulated over this time duration before being used to calculate percentiles, and
      later, measurements from an individual device are also accumulated over this time
      duration before being given a percentile rank.

    - **consecutiveDatapointsToAlarm** *(integer) --*

      If a device is in violation of the behavior for the specified number of consecutive
      datapoints, an alarm occurs. If not specified, the default is 1.

    - **consecutiveDatapointsToClear** *(integer) --*

      If an alarm has occurred and the offending device is no longer in violation of the
      behavior for the specified number of consecutive datapoints, the alarm is cleared. If
      not specified, the default is 1.

    - **statisticalThreshold** *(dict) --*

      A statistical ranking (percentile) which indicates a threshold value by which a
      behavior is determined to be in compliance or in violation of the behavior.

      - **statistic** *(string) --*

        The percentile which resolves to a threshold value by which compliance with a
        behavior is determined. Metrics are collected over the specified period
        (``durationSeconds`` ) from all reporting devices in your account and statistical
        ranks are calculated. Then, the measurements from a device are collected over the
        same period. If the accumulated measurements from the device fall above or below
        (``comparisonOperator`` ) the value associated with the percentile specified, then
        the device is considered to be in compliance with the behavior, otherwise a violation
        occurs.
    """


_ClientDescribeSecurityProfileResponsebehaviorsTypeDef = TypedDict(
    "_ClientDescribeSecurityProfileResponsebehaviorsTypeDef",
    {
        "name": str,
        "metric": str,
        "criteria": ClientDescribeSecurityProfileResponsebehaviorscriteriaTypeDef,
    },
    total=False,
)


class ClientDescribeSecurityProfileResponsebehaviorsTypeDef(
    _ClientDescribeSecurityProfileResponsebehaviorsTypeDef
):
    """
    Type definition for `ClientDescribeSecurityProfileResponse` `behaviors`

    A Device Defender security profile behavior.

    - **name** *(string) --*

      The name you have given to the behavior.

    - **metric** *(string) --*

      What is measured by the behavior.

    - **criteria** *(dict) --*

      The criteria that determine if a device is behaving normally in regard to the ``metric`` .

      - **comparisonOperator** *(string) --*

        The operator that relates the thing measured (``metric`` ) to the criteria (containing
        a ``value`` or ``statisticalThreshold`` ).

      - **value** *(dict) --*

        The value to be compared with the ``metric`` .

        - **count** *(integer) --*

          If the ``comparisonOperator`` calls for a numeric value, use this to specify that
          numeric value to be compared with the ``metric`` .

        - **cidrs** *(list) --*

          If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set
          to be compared with the ``metric`` .

          - *(string) --*

        - **ports** *(list) --*

          If the ``comparisonOperator`` calls for a set of ports, use this to specify that set
          to be compared with the ``metric`` .

          - *(integer) --*

      - **durationSeconds** *(integer) --*

        Use this to specify the time duration over which the behavior is evaluated, for those
        criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
        ``statisticalThreshhold`` metric comparison, measurements from all devices are
        accumulated over this time duration before being used to calculate percentiles, and
        later, measurements from an individual device are also accumulated over this time
        duration before being given a percentile rank.

      - **consecutiveDatapointsToAlarm** *(integer) --*

        If a device is in violation of the behavior for the specified number of consecutive
        datapoints, an alarm occurs. If not specified, the default is 1.

      - **consecutiveDatapointsToClear** *(integer) --*

        If an alarm has occurred and the offending device is no longer in violation of the
        behavior for the specified number of consecutive datapoints, the alarm is cleared. If
        not specified, the default is 1.

      - **statisticalThreshold** *(dict) --*

        A statistical ranking (percentile) which indicates a threshold value by which a
        behavior is determined to be in compliance or in violation of the behavior.

        - **statistic** *(string) --*

          The percentile which resolves to a threshold value by which compliance with a
          behavior is determined. Metrics are collected over the specified period
          (``durationSeconds`` ) from all reporting devices in your account and statistical
          ranks are calculated. Then, the measurements from a device are collected over the
          same period. If the accumulated measurements from the device fall above or below
          (``comparisonOperator`` ) the value associated with the percentile specified, then
          the device is considered to be in compliance with the behavior, otherwise a violation
          occurs.
    """


_ClientDescribeSecurityProfileResponseTypeDef = TypedDict(
    "_ClientDescribeSecurityProfileResponseTypeDef",
    {
        "securityProfileName": str,
        "securityProfileArn": str,
        "securityProfileDescription": str,
        "behaviors": List[ClientDescribeSecurityProfileResponsebehaviorsTypeDef],
        "alertTargets": Dict[
            str, ClientDescribeSecurityProfileResponsealertTargetsTypeDef
        ],
        "additionalMetricsToRetain": List[str],
        "version": int,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)


class ClientDescribeSecurityProfileResponseTypeDef(
    _ClientDescribeSecurityProfileResponseTypeDef
):
    """
    Type definition for `ClientDescribeSecurityProfile` `Response`

    - **securityProfileName** *(string) --*

      The name of the security profile.

    - **securityProfileArn** *(string) --*

      The ARN of the security profile.

    - **securityProfileDescription** *(string) --*

      A description of the security profile (associated with the security profile when it was
      created or updated).

    - **behaviors** *(list) --*

      Specifies the behaviors that, when violated by a device (thing), cause an alert.

      - *(dict) --*

        A Device Defender security profile behavior.

        - **name** *(string) --*

          The name you have given to the behavior.

        - **metric** *(string) --*

          What is measured by the behavior.

        - **criteria** *(dict) --*

          The criteria that determine if a device is behaving normally in regard to the ``metric`` .

          - **comparisonOperator** *(string) --*

            The operator that relates the thing measured (``metric`` ) to the criteria (containing
            a ``value`` or ``statisticalThreshold`` ).

          - **value** *(dict) --*

            The value to be compared with the ``metric`` .

            - **count** *(integer) --*

              If the ``comparisonOperator`` calls for a numeric value, use this to specify that
              numeric value to be compared with the ``metric`` .

            - **cidrs** *(list) --*

              If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set
              to be compared with the ``metric`` .

              - *(string) --*

            - **ports** *(list) --*

              If the ``comparisonOperator`` calls for a set of ports, use this to specify that set
              to be compared with the ``metric`` .

              - *(integer) --*

          - **durationSeconds** *(integer) --*

            Use this to specify the time duration over which the behavior is evaluated, for those
            criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
            ``statisticalThreshhold`` metric comparison, measurements from all devices are
            accumulated over this time duration before being used to calculate percentiles, and
            later, measurements from an individual device are also accumulated over this time
            duration before being given a percentile rank.

          - **consecutiveDatapointsToAlarm** *(integer) --*

            If a device is in violation of the behavior for the specified number of consecutive
            datapoints, an alarm occurs. If not specified, the default is 1.

          - **consecutiveDatapointsToClear** *(integer) --*

            If an alarm has occurred and the offending device is no longer in violation of the
            behavior for the specified number of consecutive datapoints, the alarm is cleared. If
            not specified, the default is 1.

          - **statisticalThreshold** *(dict) --*

            A statistical ranking (percentile) which indicates a threshold value by which a
            behavior is determined to be in compliance or in violation of the behavior.

            - **statistic** *(string) --*

              The percentile which resolves to a threshold value by which compliance with a
              behavior is determined. Metrics are collected over the specified period
              (``durationSeconds`` ) from all reporting devices in your account and statistical
              ranks are calculated. Then, the measurements from a device are collected over the
              same period. If the accumulated measurements from the device fall above or below
              (``comparisonOperator`` ) the value associated with the percentile specified, then
              the device is considered to be in compliance with the behavior, otherwise a violation
              occurs.

    - **alertTargets** *(dict) --*

      Where the alerts are sent. (Alerts are always sent to the console.)

      - *(string) --*

        The type of alert target: one of "SNS".

        - *(dict) --*

          A structure containing the alert target ARN and the role ARN.

          - **alertTargetArn** *(string) --*

            The ARN of the notification target to which alerts are sent.

          - **roleArn** *(string) --*

            The ARN of the role that grants permission to send alerts to the notification target.

    - **additionalMetricsToRetain** *(list) --*

      A list of metrics whose data is retained (stored). By default, data is retained for any
      metric used in the profile's ``behaviors`` , but it is also retained for any metric specified
      here.

      - *(string) --*

    - **version** *(integer) --*

      The version of the security profile. A new version is generated whenever the security profile
      is updated.

    - **creationDate** *(datetime) --*

      The time the security profile was created.

    - **lastModifiedDate** *(datetime) --*

      The time the security profile was last modified.
    """


_ClientDescribeStreamResponsestreamInfofiless3LocationTypeDef = TypedDict(
    "_ClientDescribeStreamResponsestreamInfofiless3LocationTypeDef",
    {"bucket": str, "key": str, "version": str},
    total=False,
)


class ClientDescribeStreamResponsestreamInfofiless3LocationTypeDef(
    _ClientDescribeStreamResponsestreamInfofiless3LocationTypeDef
):
    """
    Type definition for `ClientDescribeStreamResponsestreamInfofiles` `s3Location`

    The location of the file in S3.

    - **bucket** *(string) --*

      The S3 bucket.

    - **key** *(string) --*

      The S3 key.

    - **version** *(string) --*

      The S3 bucket version.
    """


_ClientDescribeStreamResponsestreamInfofilesTypeDef = TypedDict(
    "_ClientDescribeStreamResponsestreamInfofilesTypeDef",
    {
        "fileId": int,
        "s3Location": ClientDescribeStreamResponsestreamInfofiless3LocationTypeDef,
    },
    total=False,
)


class ClientDescribeStreamResponsestreamInfofilesTypeDef(
    _ClientDescribeStreamResponsestreamInfofilesTypeDef
):
    """
    Type definition for `ClientDescribeStreamResponsestreamInfo` `files`

    Represents a file to stream.

    - **fileId** *(integer) --*

      The file ID.

    - **s3Location** *(dict) --*

      The location of the file in S3.

      - **bucket** *(string) --*

        The S3 bucket.

      - **key** *(string) --*

        The S3 key.

      - **version** *(string) --*

        The S3 bucket version.
    """


_ClientDescribeStreamResponsestreamInfoTypeDef = TypedDict(
    "_ClientDescribeStreamResponsestreamInfoTypeDef",
    {
        "streamId": str,
        "streamArn": str,
        "streamVersion": int,
        "description": str,
        "files": List[ClientDescribeStreamResponsestreamInfofilesTypeDef],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "roleArn": str,
    },
    total=False,
)


class ClientDescribeStreamResponsestreamInfoTypeDef(
    _ClientDescribeStreamResponsestreamInfoTypeDef
):
    """
    Type definition for `ClientDescribeStreamResponse` `streamInfo`

    Information about the stream.

    - **streamId** *(string) --*

      The stream ID.

    - **streamArn** *(string) --*

      The stream ARN.

    - **streamVersion** *(integer) --*

      The stream version.

    - **description** *(string) --*

      The description of the stream.

    - **files** *(list) --*

      The files to stream.

      - *(dict) --*

        Represents a file to stream.

        - **fileId** *(integer) --*

          The file ID.

        - **s3Location** *(dict) --*

          The location of the file in S3.

          - **bucket** *(string) --*

            The S3 bucket.

          - **key** *(string) --*

            The S3 key.

          - **version** *(string) --*

            The S3 bucket version.

    - **createdAt** *(datetime) --*

      The date when the stream was created.

    - **lastUpdatedAt** *(datetime) --*

      The date when the stream was last updated.

    - **roleArn** *(string) --*

      An IAM role AWS IoT assumes to access your S3 files.
    """


_ClientDescribeStreamResponseTypeDef = TypedDict(
    "_ClientDescribeStreamResponseTypeDef",
    {"streamInfo": ClientDescribeStreamResponsestreamInfoTypeDef},
    total=False,
)


class ClientDescribeStreamResponseTypeDef(_ClientDescribeStreamResponseTypeDef):
    """
    Type definition for `ClientDescribeStream` `Response`

    - **streamInfo** *(dict) --*

      Information about the stream.

      - **streamId** *(string) --*

        The stream ID.

      - **streamArn** *(string) --*

        The stream ARN.

      - **streamVersion** *(integer) --*

        The stream version.

      - **description** *(string) --*

        The description of the stream.

      - **files** *(list) --*

        The files to stream.

        - *(dict) --*

          Represents a file to stream.

          - **fileId** *(integer) --*

            The file ID.

          - **s3Location** *(dict) --*

            The location of the file in S3.

            - **bucket** *(string) --*

              The S3 bucket.

            - **key** *(string) --*

              The S3 key.

            - **version** *(string) --*

              The S3 bucket version.

      - **createdAt** *(datetime) --*

        The date when the stream was created.

      - **lastUpdatedAt** *(datetime) --*

        The date when the stream was last updated.

      - **roleArn** *(string) --*

        An IAM role AWS IoT assumes to access your S3 files.
    """


_ClientDescribeThingGroupResponsethingGroupMetadatarootToParentThingGroupsTypeDef = TypedDict(
    "_ClientDescribeThingGroupResponsethingGroupMetadatarootToParentThingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)


class ClientDescribeThingGroupResponsethingGroupMetadatarootToParentThingGroupsTypeDef(
    _ClientDescribeThingGroupResponsethingGroupMetadatarootToParentThingGroupsTypeDef
):
    """
    Type definition for `ClientDescribeThingGroupResponsethingGroupMetadata` `rootToParentThingGroups`

    The name and ARN of a group.

    - **groupName** *(string) --*

      The group name.

    - **groupArn** *(string) --*

      The group ARN.
    """


_ClientDescribeThingGroupResponsethingGroupMetadataTypeDef = TypedDict(
    "_ClientDescribeThingGroupResponsethingGroupMetadataTypeDef",
    {
        "parentGroupName": str,
        "rootToParentThingGroups": List[
            ClientDescribeThingGroupResponsethingGroupMetadatarootToParentThingGroupsTypeDef
        ],
        "creationDate": datetime,
    },
    total=False,
)


class ClientDescribeThingGroupResponsethingGroupMetadataTypeDef(
    _ClientDescribeThingGroupResponsethingGroupMetadataTypeDef
):
    """
    Type definition for `ClientDescribeThingGroupResponse` `thingGroupMetadata`

    Thing group metadata.

    - **parentGroupName** *(string) --*

      The parent thing group name.

    - **rootToParentThingGroups** *(list) --*

      The root parent thing group.

      - *(dict) --*

        The name and ARN of a group.

        - **groupName** *(string) --*

          The group name.

        - **groupArn** *(string) --*

          The group ARN.

    - **creationDate** *(datetime) --*

      The UNIX timestamp of when the thing group was created.
    """


_ClientDescribeThingGroupResponsethingGroupPropertiesattributePayloadTypeDef = TypedDict(
    "_ClientDescribeThingGroupResponsethingGroupPropertiesattributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)


class ClientDescribeThingGroupResponsethingGroupPropertiesattributePayloadTypeDef(
    _ClientDescribeThingGroupResponsethingGroupPropertiesattributePayloadTypeDef
):
    """
    Type definition for `ClientDescribeThingGroupResponsethingGroupProperties` `attributePayload`

    The thing group attributes in JSON format.

    - **attributes** *(dict) --*

      A JSON string containing up to three key-value pair in JSON format. For example:

       ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``

      - *(string) --*

        - *(string) --*

    - **merge** *(boolean) --*

      Specifies whether the list of attributes provided in the ``AttributePayload`` is merged
      with the attributes stored in the registry, instead of overwriting them.

      To remove an attribute, call ``UpdateThing`` with an empty attribute value.

      .. note::

        The ``merge`` attribute is only valid when calling ``UpdateThing`` or
        ``UpdateThingGroup`` .
    """


_ClientDescribeThingGroupResponsethingGroupPropertiesTypeDef = TypedDict(
    "_ClientDescribeThingGroupResponsethingGroupPropertiesTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": ClientDescribeThingGroupResponsethingGroupPropertiesattributePayloadTypeDef,
    },
    total=False,
)


class ClientDescribeThingGroupResponsethingGroupPropertiesTypeDef(
    _ClientDescribeThingGroupResponsethingGroupPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeThingGroupResponse` `thingGroupProperties`

    The thing group properties.

    - **thingGroupDescription** *(string) --*

      The thing group description.

    - **attributePayload** *(dict) --*

      The thing group attributes in JSON format.

      - **attributes** *(dict) --*

        A JSON string containing up to three key-value pair in JSON format. For example:

         ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``

        - *(string) --*

          - *(string) --*

      - **merge** *(boolean) --*

        Specifies whether the list of attributes provided in the ``AttributePayload`` is merged
        with the attributes stored in the registry, instead of overwriting them.

        To remove an attribute, call ``UpdateThing`` with an empty attribute value.

        .. note::

          The ``merge`` attribute is only valid when calling ``UpdateThing`` or
          ``UpdateThingGroup`` .
    """


_ClientDescribeThingGroupResponseTypeDef = TypedDict(
    "_ClientDescribeThingGroupResponseTypeDef",
    {
        "thingGroupName": str,
        "thingGroupId": str,
        "thingGroupArn": str,
        "version": int,
        "thingGroupProperties": ClientDescribeThingGroupResponsethingGroupPropertiesTypeDef,
        "thingGroupMetadata": ClientDescribeThingGroupResponsethingGroupMetadataTypeDef,
        "indexName": str,
        "queryString": str,
        "queryVersion": str,
        "status": str,
    },
    total=False,
)


class ClientDescribeThingGroupResponseTypeDef(_ClientDescribeThingGroupResponseTypeDef):
    """
    Type definition for `ClientDescribeThingGroup` `Response`

    - **thingGroupName** *(string) --*

      The name of the thing group.

    - **thingGroupId** *(string) --*

      The thing group ID.

    - **thingGroupArn** *(string) --*

      The thing group ARN.

    - **version** *(integer) --*

      The version of the thing group.

    - **thingGroupProperties** *(dict) --*

      The thing group properties.

      - **thingGroupDescription** *(string) --*

        The thing group description.

      - **attributePayload** *(dict) --*

        The thing group attributes in JSON format.

        - **attributes** *(dict) --*

          A JSON string containing up to three key-value pair in JSON format. For example:

           ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``

          - *(string) --*

            - *(string) --*

        - **merge** *(boolean) --*

          Specifies whether the list of attributes provided in the ``AttributePayload`` is merged
          with the attributes stored in the registry, instead of overwriting them.

          To remove an attribute, call ``UpdateThing`` with an empty attribute value.

          .. note::

            The ``merge`` attribute is only valid when calling ``UpdateThing`` or
            ``UpdateThingGroup`` .

    - **thingGroupMetadata** *(dict) --*

      Thing group metadata.

      - **parentGroupName** *(string) --*

        The parent thing group name.

      - **rootToParentThingGroups** *(list) --*

        The root parent thing group.

        - *(dict) --*

          The name and ARN of a group.

          - **groupName** *(string) --*

            The group name.

          - **groupArn** *(string) --*

            The group ARN.

      - **creationDate** *(datetime) --*

        The UNIX timestamp of when the thing group was created.

    - **indexName** *(string) --*

      The dynamic thing group index name.

    - **queryString** *(string) --*

      The dynamic thing group search query string.

    - **queryVersion** *(string) --*

      The dynamic thing group query version.

    - **status** *(string) --*

      The dynamic thing group status.
    """


_ClientDescribeThingRegistrationTaskResponseTypeDef = TypedDict(
    "_ClientDescribeThingRegistrationTaskResponseTypeDef",
    {
        "taskId": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "templateBody": str,
        "inputFileBucket": str,
        "inputFileKey": str,
        "roleArn": str,
        "status": str,
        "message": str,
        "successCount": int,
        "failureCount": int,
        "percentageProgress": int,
    },
    total=False,
)


class ClientDescribeThingRegistrationTaskResponseTypeDef(
    _ClientDescribeThingRegistrationTaskResponseTypeDef
):
    """
    Type definition for `ClientDescribeThingRegistrationTask` `Response`

    - **taskId** *(string) --*

      The task ID.

    - **creationDate** *(datetime) --*

      The task creation date.

    - **lastModifiedDate** *(datetime) --*

      The date when the task was last modified.

    - **templateBody** *(string) --*

      The task's template.

    - **inputFileBucket** *(string) --*

      The S3 bucket that contains the input file.

    - **inputFileKey** *(string) --*

      The input file key.

    - **roleArn** *(string) --*

      The role ARN that grants access to the input file bucket.

    - **status** *(string) --*

      The status of the bulk thing provisioning task.

    - **message** *(string) --*

      The message.

    - **successCount** *(integer) --*

      The number of things successfully provisioned.

    - **failureCount** *(integer) --*

      The number of things that failed to be provisioned.

    - **percentageProgress** *(integer) --*

      The progress of the bulk provisioning task expressed as a percentage.
    """


_ClientDescribeThingResponseTypeDef = TypedDict(
    "_ClientDescribeThingResponseTypeDef",
    {
        "defaultClientId": str,
        "thingName": str,
        "thingId": str,
        "thingArn": str,
        "thingTypeName": str,
        "attributes": Dict[str, str],
        "version": int,
        "billingGroupName": str,
    },
    total=False,
)


class ClientDescribeThingResponseTypeDef(_ClientDescribeThingResponseTypeDef):
    """
    Type definition for `ClientDescribeThing` `Response`

    The output from the DescribeThing operation.

    - **defaultClientId** *(string) --*

      The default client ID.

    - **thingName** *(string) --*

      The name of the thing.

    - **thingId** *(string) --*

      The ID of the thing to describe.

    - **thingArn** *(string) --*

      The ARN of the thing to describe.

    - **thingTypeName** *(string) --*

      The thing type name.

    - **attributes** *(dict) --*

      The thing attributes.

      - *(string) --*

        - *(string) --*

    - **version** *(integer) --*

      The current version of the thing record in the registry.

      .. note::

        To avoid unintentional changes to the information in the registry, you can pass the version
        information in the ``expectedVersion`` parameter of the ``UpdateThing`` and ``DeleteThing``
        calls.

    - **billingGroupName** *(string) --*

      The name of the billing group the thing belongs to.
    """


_ClientDescribeThingTypeResponsethingTypeMetadataTypeDef = TypedDict(
    "_ClientDescribeThingTypeResponsethingTypeMetadataTypeDef",
    {"deprecated": bool, "deprecationDate": datetime, "creationDate": datetime},
    total=False,
)


class ClientDescribeThingTypeResponsethingTypeMetadataTypeDef(
    _ClientDescribeThingTypeResponsethingTypeMetadataTypeDef
):
    """
    Type definition for `ClientDescribeThingTypeResponse` `thingTypeMetadata`

    The ThingTypeMetadata contains additional information about the thing type including:
    creation date and time, a value indicating whether the thing type is deprecated, and a date
    and time when it was deprecated.

    - **deprecated** *(boolean) --*

      Whether the thing type is deprecated. If **true** , no new things could be associated with
      this type.

    - **deprecationDate** *(datetime) --*

      The date and time when the thing type was deprecated.

    - **creationDate** *(datetime) --*

      The date and time when the thing type was created.
    """


_ClientDescribeThingTypeResponsethingTypePropertiesTypeDef = TypedDict(
    "_ClientDescribeThingTypeResponsethingTypePropertiesTypeDef",
    {"thingTypeDescription": str, "searchableAttributes": List[str]},
    total=False,
)


class ClientDescribeThingTypeResponsethingTypePropertiesTypeDef(
    _ClientDescribeThingTypeResponsethingTypePropertiesTypeDef
):
    """
    Type definition for `ClientDescribeThingTypeResponse` `thingTypeProperties`

    The ThingTypeProperties contains information about the thing type including description, and
    a list of searchable thing attribute names.

    - **thingTypeDescription** *(string) --*

      The description of the thing type.

    - **searchableAttributes** *(list) --*

      A list of searchable thing attribute names.

      - *(string) --*
    """


_ClientDescribeThingTypeResponseTypeDef = TypedDict(
    "_ClientDescribeThingTypeResponseTypeDef",
    {
        "thingTypeName": str,
        "thingTypeId": str,
        "thingTypeArn": str,
        "thingTypeProperties": ClientDescribeThingTypeResponsethingTypePropertiesTypeDef,
        "thingTypeMetadata": ClientDescribeThingTypeResponsethingTypeMetadataTypeDef,
    },
    total=False,
)


class ClientDescribeThingTypeResponseTypeDef(_ClientDescribeThingTypeResponseTypeDef):
    """
    Type definition for `ClientDescribeThingType` `Response`

    The output for the DescribeThingType operation.

    - **thingTypeName** *(string) --*

      The name of the thing type.

    - **thingTypeId** *(string) --*

      The thing type ID.

    - **thingTypeArn** *(string) --*

      The thing type ARN.

    - **thingTypeProperties** *(dict) --*

      The ThingTypeProperties contains information about the thing type including description, and
      a list of searchable thing attribute names.

      - **thingTypeDescription** *(string) --*

        The description of the thing type.

      - **searchableAttributes** *(list) --*

        A list of searchable thing attribute names.

        - *(string) --*

    - **thingTypeMetadata** *(dict) --*

      The ThingTypeMetadata contains additional information about the thing type including:
      creation date and time, a value indicating whether the thing type is deprecated, and a date
      and time when it was deprecated.

      - **deprecated** *(boolean) --*

        Whether the thing type is deprecated. If **true** , no new things could be associated with
        this type.

      - **deprecationDate** *(datetime) --*

        The date and time when the thing type was deprecated.

      - **creationDate** *(datetime) --*

        The date and time when the thing type was created.
    """


_ClientGetCardinalityResponseTypeDef = TypedDict(
    "_ClientGetCardinalityResponseTypeDef", {"cardinality": int}, total=False
)


class ClientGetCardinalityResponseTypeDef(_ClientGetCardinalityResponseTypeDef):
    """
    Type definition for `ClientGetCardinality` `Response`

    - **cardinality** *(integer) --*

      The number of things that match the query.
    """


_ClientGetEffectivePoliciesResponseeffectivePoliciesTypeDef = TypedDict(
    "_ClientGetEffectivePoliciesResponseeffectivePoliciesTypeDef",
    {"policyName": str, "policyArn": str, "policyDocument": str},
    total=False,
)


class ClientGetEffectivePoliciesResponseeffectivePoliciesTypeDef(
    _ClientGetEffectivePoliciesResponseeffectivePoliciesTypeDef
):
    """
    Type definition for `ClientGetEffectivePoliciesResponse` `effectivePolicies`

    The policy that has the effect on the authorization results.

    - **policyName** *(string) --*

      The policy name.

    - **policyArn** *(string) --*

      The policy ARN.

    - **policyDocument** *(string) --*

      The IAM policy document.
    """


_ClientGetEffectivePoliciesResponseTypeDef = TypedDict(
    "_ClientGetEffectivePoliciesResponseTypeDef",
    {
        "effectivePolicies": List[
            ClientGetEffectivePoliciesResponseeffectivePoliciesTypeDef
        ]
    },
    total=False,
)


class ClientGetEffectivePoliciesResponseTypeDef(
    _ClientGetEffectivePoliciesResponseTypeDef
):
    """
    Type definition for `ClientGetEffectivePolicies` `Response`

    - **effectivePolicies** *(list) --*

      The effective policies.

      - *(dict) --*

        The policy that has the effect on the authorization results.

        - **policyName** *(string) --*

          The policy name.

        - **policyArn** *(string) --*

          The policy ARN.

        - **policyDocument** *(string) --*

          The IAM policy document.
    """


_ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationcustomFieldsTypeDef = TypedDict(
    "_ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationcustomFieldsTypeDef",
    {"name": str, "type": str},
    total=False,
)


class ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationcustomFieldsTypeDef(
    _ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationcustomFieldsTypeDef
):
    """
    Type definition for `ClientGetIndexingConfigurationResponsethingGroupIndexingConfiguration` `customFields`

    Describes the name and data type at a field.

    - **name** *(string) --*

      The name of the field.

    - **type** *(string) --*

      The datatype of the field.
    """


_ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationmanagedFieldsTypeDef = TypedDict(
    "_ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationmanagedFieldsTypeDef",
    {"name": str, "type": str},
    total=False,
)


class ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationmanagedFieldsTypeDef(
    _ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationmanagedFieldsTypeDef
):
    """
    Type definition for `ClientGetIndexingConfigurationResponsethingGroupIndexingConfiguration` `managedFields`

    Describes the name and data type at a field.

    - **name** *(string) --*

      The name of the field.

    - **type** *(string) --*

      The datatype of the field.
    """


_ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationTypeDef = TypedDict(
    "_ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationTypeDef",
    {
        "thingGroupIndexingMode": str,
        "managedFields": List[
            ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationmanagedFieldsTypeDef
        ],
        "customFields": List[
            ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationcustomFieldsTypeDef
        ],
    },
    total=False,
)


class ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationTypeDef(
    _ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationTypeDef
):
    """
    Type definition for `ClientGetIndexingConfigurationResponse` `thingGroupIndexingConfiguration`

    The index configuration.

    - **thingGroupIndexingMode** *(string) --*

      Thing group indexing mode.

    - **managedFields** *(list) --*

      Contains fields that are indexed and whose types are already known by the Fleet Indexing
      service.

      - *(dict) --*

        Describes the name and data type at a field.

        - **name** *(string) --*

          The name of the field.

        - **type** *(string) --*

          The datatype of the field.

    - **customFields** *(list) --*

      Contains custom field names and their data type.

      - *(dict) --*

        Describes the name and data type at a field.

        - **name** *(string) --*

          The name of the field.

        - **type** *(string) --*

          The datatype of the field.
    """


_ClientGetIndexingConfigurationResponsethingIndexingConfigurationcustomFieldsTypeDef = TypedDict(
    "_ClientGetIndexingConfigurationResponsethingIndexingConfigurationcustomFieldsTypeDef",
    {"name": str, "type": str},
    total=False,
)


class ClientGetIndexingConfigurationResponsethingIndexingConfigurationcustomFieldsTypeDef(
    _ClientGetIndexingConfigurationResponsethingIndexingConfigurationcustomFieldsTypeDef
):
    """
    Type definition for `ClientGetIndexingConfigurationResponsethingIndexingConfiguration` `customFields`

    Describes the name and data type at a field.

    - **name** *(string) --*

      The name of the field.

    - **type** *(string) --*

      The datatype of the field.
    """


_ClientGetIndexingConfigurationResponsethingIndexingConfigurationmanagedFieldsTypeDef = TypedDict(
    "_ClientGetIndexingConfigurationResponsethingIndexingConfigurationmanagedFieldsTypeDef",
    {"name": str, "type": str},
    total=False,
)


class ClientGetIndexingConfigurationResponsethingIndexingConfigurationmanagedFieldsTypeDef(
    _ClientGetIndexingConfigurationResponsethingIndexingConfigurationmanagedFieldsTypeDef
):
    """
    Type definition for `ClientGetIndexingConfigurationResponsethingIndexingConfiguration` `managedFields`

    Describes the name and data type at a field.

    - **name** *(string) --*

      The name of the field.

    - **type** *(string) --*

      The datatype of the field.
    """


_ClientGetIndexingConfigurationResponsethingIndexingConfigurationTypeDef = TypedDict(
    "_ClientGetIndexingConfigurationResponsethingIndexingConfigurationTypeDef",
    {
        "thingIndexingMode": str,
        "thingConnectivityIndexingMode": str,
        "managedFields": List[
            ClientGetIndexingConfigurationResponsethingIndexingConfigurationmanagedFieldsTypeDef
        ],
        "customFields": List[
            ClientGetIndexingConfigurationResponsethingIndexingConfigurationcustomFieldsTypeDef
        ],
    },
    total=False,
)


class ClientGetIndexingConfigurationResponsethingIndexingConfigurationTypeDef(
    _ClientGetIndexingConfigurationResponsethingIndexingConfigurationTypeDef
):
    """
    Type definition for `ClientGetIndexingConfigurationResponse` `thingIndexingConfiguration`

    Thing indexing configuration.

    - **thingIndexingMode** *(string) --*

      Thing indexing mode. Valid values are:

      * REGISTRY – Your thing index contains registry data only.

      * REGISTRY_AND_SHADOW - Your thing index contains registry and shadow data.

      * OFF - Thing indexing is disabled.

    - **thingConnectivityIndexingMode** *(string) --*

      Thing connectivity indexing mode. Valid values are:

      * STATUS – Your thing index contains connectivity status. To enable thing connectivity
      indexing, thingIndexMode must not be set to OFF.

      * OFF - Thing connectivity status indexing is disabled.

    - **managedFields** *(list) --*

      Contains fields that are indexed and whose types are already known by the Fleet Indexing
      service.

      - *(dict) --*

        Describes the name and data type at a field.

        - **name** *(string) --*

          The name of the field.

        - **type** *(string) --*

          The datatype of the field.

    - **customFields** *(list) --*

      Contains custom field names and their data type.

      - *(dict) --*

        Describes the name and data type at a field.

        - **name** *(string) --*

          The name of the field.

        - **type** *(string) --*

          The datatype of the field.
    """


_ClientGetIndexingConfigurationResponseTypeDef = TypedDict(
    "_ClientGetIndexingConfigurationResponseTypeDef",
    {
        "thingIndexingConfiguration": ClientGetIndexingConfigurationResponsethingIndexingConfigurationTypeDef,
        "thingGroupIndexingConfiguration": ClientGetIndexingConfigurationResponsethingGroupIndexingConfigurationTypeDef,
    },
    total=False,
)


class ClientGetIndexingConfigurationResponseTypeDef(
    _ClientGetIndexingConfigurationResponseTypeDef
):
    """
    Type definition for `ClientGetIndexingConfiguration` `Response`

    - **thingIndexingConfiguration** *(dict) --*

      Thing indexing configuration.

      - **thingIndexingMode** *(string) --*

        Thing indexing mode. Valid values are:

        * REGISTRY – Your thing index contains registry data only.

        * REGISTRY_AND_SHADOW - Your thing index contains registry and shadow data.

        * OFF - Thing indexing is disabled.

      - **thingConnectivityIndexingMode** *(string) --*

        Thing connectivity indexing mode. Valid values are:

        * STATUS – Your thing index contains connectivity status. To enable thing connectivity
        indexing, thingIndexMode must not be set to OFF.

        * OFF - Thing connectivity status indexing is disabled.

      - **managedFields** *(list) --*

        Contains fields that are indexed and whose types are already known by the Fleet Indexing
        service.

        - *(dict) --*

          Describes the name and data type at a field.

          - **name** *(string) --*

            The name of the field.

          - **type** *(string) --*

            The datatype of the field.

      - **customFields** *(list) --*

        Contains custom field names and their data type.

        - *(dict) --*

          Describes the name and data type at a field.

          - **name** *(string) --*

            The name of the field.

          - **type** *(string) --*

            The datatype of the field.

    - **thingGroupIndexingConfiguration** *(dict) --*

      The index configuration.

      - **thingGroupIndexingMode** *(string) --*

        Thing group indexing mode.

      - **managedFields** *(list) --*

        Contains fields that are indexed and whose types are already known by the Fleet Indexing
        service.

        - *(dict) --*

          Describes the name and data type at a field.

          - **name** *(string) --*

            The name of the field.

          - **type** *(string) --*

            The datatype of the field.

      - **customFields** *(list) --*

        Contains custom field names and their data type.

        - *(dict) --*

          Describes the name and data type at a field.

          - **name** *(string) --*

            The name of the field.

          - **type** *(string) --*

            The datatype of the field.
    """


_ClientGetJobDocumentResponseTypeDef = TypedDict(
    "_ClientGetJobDocumentResponseTypeDef", {"document": str}, total=False
)


class ClientGetJobDocumentResponseTypeDef(_ClientGetJobDocumentResponseTypeDef):
    """
    Type definition for `ClientGetJobDocument` `Response`

    - **document** *(string) --*

      The job document content.
    """


_ClientGetLoggingOptionsResponseTypeDef = TypedDict(
    "_ClientGetLoggingOptionsResponseTypeDef",
    {"roleArn": str, "logLevel": str},
    total=False,
)


class ClientGetLoggingOptionsResponseTypeDef(_ClientGetLoggingOptionsResponseTypeDef):
    """
    Type definition for `ClientGetLoggingOptions` `Response`

    The output from the GetLoggingOptions operation.

    - **roleArn** *(string) --*

      The ARN of the IAM role that grants access.

    - **logLevel** *(string) --*

      The logging level.
    """


_ClientGetOtaUpdateResponseotaUpdateInfoawsJobExecutionsRolloutConfigTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfoawsJobExecutionsRolloutConfigTypeDef",
    {"maximumPerMinute": int},
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfoawsJobExecutionsRolloutConfigTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfoawsJobExecutionsRolloutConfigTypeDef
):
    """
    Type definition for `ClientGetOtaUpdateResponseotaUpdateInfo` `awsJobExecutionsRolloutConfig`

    Configuration for the rollout of OTA updates.

    - **maximumPerMinute** *(integer) --*

      The maximum number of OTA update job executions started per minute.
    """


_ClientGetOtaUpdateResponseotaUpdateInfoerrorInfoTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfoerrorInfoTypeDef",
    {"code": str, "message": str},
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfoerrorInfoTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfoerrorInfoTypeDef
):
    """
    Type definition for `ClientGetOtaUpdateResponseotaUpdateInfo` `errorInfo`

    Error information associated with the OTA update.

    - **code** *(string) --*

      The error code.

    - **message** *(string) --*

      The error message.
    """


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef",
    {"certificateName": str, "inlineDocument": str},
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef
):
    """
    Type definition for `ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigning` `certificateChain`

    The certificate chain.

    - **certificateName** *(string) --*

      The name of the certificate.

    - **inlineDocument** *(string) --*

      A base64 encoded binary representation of the code signing certificate chain.
    """


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef",
    {"inlineDocument": bytes},
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef
):
    """
    Type definition for `ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigning` `signature`

    The signature for the file.

    - **inlineDocument** *(bytes) --*

      A base64 encoded binary representation of the code signing signature.
    """


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningTypeDef",
    {
        "signature": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningsignatureTypeDef,
        "certificateChain": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningcertificateChainTypeDef,
        "hashAlgorithm": str,
        "signatureAlgorithm": str,
    },
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningTypeDef
):
    """
    Type definition for `ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigning` `customCodeSigning`

    A custom method for code signing a file.

    - **signature** *(dict) --*

      The signature for the file.

      - **inlineDocument** *(bytes) --*

        A base64 encoded binary representation of the code signing signature.

    - **certificateChain** *(dict) --*

      The certificate chain.

      - **certificateName** *(string) --*

        The name of the certificate.

      - **inlineDocument** *(string) --*

        A base64 encoded binary representation of the code signing certificate chain.

    - **hashAlgorithm** *(string) --*

      The hash algorithm used to code sign the file.

    - **signatureAlgorithm** *(string) --*

      The signature algorithm used to code sign the file.
    """


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef",
    {"bucket": str, "prefix": str},
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef
):
    """
    Type definition for `ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestination` `s3Destination`

    Describes the location in S3 of the updated firmware.

    - **bucket** *(string) --*

      The S3 bucket that contains the updated firmware.

    - **prefix** *(string) --*

      The S3 prefix.
    """


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef",
    {
        "s3Destination": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinations3DestinationTypeDef
    },
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef
):
    """
    Type definition for `ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameter` `destination`

    The location to write the code-signed file.

    - **s3Destination** *(dict) --*

      Describes the location in S3 of the updated firmware.

      - **bucket** *(string) --*

        The S3 bucket that contains the updated firmware.

      - **prefix** *(string) --*

        The S3 prefix.
    """


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef",
    {"certificateArn": str, "platform": str, "certificatePathOnDevice": str},
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef
):
    """
    Type definition for `ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameter` `signingProfileParameter`

    Describes the code-signing profile.

    - **certificateArn** *(string) --*

      Certificate ARN.

    - **platform** *(string) --*

      The hardware platform of your device.

    - **certificatePathOnDevice** *(string) --*

      The location of the code-signing certificate on your device.
    """


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterTypeDef",
    {
        "signingProfileParameter": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParametersigningProfileParameterTypeDef,
        "signingProfileName": str,
        "destination": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterdestinationTypeDef,
    },
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterTypeDef
):
    """
    Type definition for `ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigning` `startSigningJobParameter`

    Describes the code-signing job.

    - **signingProfileParameter** *(dict) --*

      Describes the code-signing profile.

      - **certificateArn** *(string) --*

        Certificate ARN.

      - **platform** *(string) --*

        The hardware platform of your device.

      - **certificatePathOnDevice** *(string) --*

        The location of the code-signing certificate on your device.

    - **signingProfileName** *(string) --*

      The code-signing profile name.

    - **destination** *(dict) --*

      The location to write the code-signed file.

      - **s3Destination** *(dict) --*

        Describes the location in S3 of the updated firmware.

        - **bucket** *(string) --*

          The S3 bucket that contains the updated firmware.

        - **prefix** *(string) --*

          The S3 prefix.
    """


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningTypeDef",
    {
        "awsSignerJobId": str,
        "startSigningJobParameter": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningstartSigningJobParameterTypeDef,
        "customCodeSigning": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningcustomCodeSigningTypeDef,
    },
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningTypeDef
):
    """
    Type definition for `ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFiles` `codeSigning`

    The code signing method of the file.

    - **awsSignerJobId** *(string) --*

      The ID of the AWSSignerJob which was created to sign the file.

    - **startSigningJobParameter** *(dict) --*

      Describes the code-signing job.

      - **signingProfileParameter** *(dict) --*

        Describes the code-signing profile.

        - **certificateArn** *(string) --*

          Certificate ARN.

        - **platform** *(string) --*

          The hardware platform of your device.

        - **certificatePathOnDevice** *(string) --*

          The location of the code-signing certificate on your device.

      - **signingProfileName** *(string) --*

        The code-signing profile name.

      - **destination** *(dict) --*

        The location to write the code-signed file.

        - **s3Destination** *(dict) --*

          Describes the location in S3 of the updated firmware.

          - **bucket** *(string) --*

            The S3 bucket that contains the updated firmware.

          - **prefix** *(string) --*

            The S3 prefix.

    - **customCodeSigning** *(dict) --*

      A custom method for code signing a file.

      - **signature** *(dict) --*

        The signature for the file.

        - **inlineDocument** *(bytes) --*

          A base64 encoded binary representation of the code signing signature.

      - **certificateChain** *(dict) --*

        The certificate chain.

        - **certificateName** *(string) --*

          The name of the certificate.

        - **inlineDocument** *(string) --*

          A base64 encoded binary representation of the code signing certificate chain.

      - **hashAlgorithm** *(string) --*

        The hash algorithm used to code sign the file.

      - **signatureAlgorithm** *(string) --*

        The signature algorithm used to code sign the file.
    """


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocations3LocationTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocations3LocationTypeDef",
    {"bucket": str, "key": str, "version": str},
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocations3LocationTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocations3LocationTypeDef
):
    """
    Type definition for `ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocation` `s3Location`

    The location of the updated firmware in S3.

    - **bucket** *(string) --*

      The S3 bucket.

    - **key** *(string) --*

      The S3 key.

    - **version** *(string) --*

      The S3 bucket version.
    """


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationstreamTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationstreamTypeDef",
    {"streamId": str, "fileId": int},
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationstreamTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationstreamTypeDef
):
    """
    Type definition for `ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocation` `stream`

    The stream that contains the OTA update.

    - **streamId** *(string) --*

      The stream ID.

    - **fileId** *(integer) --*

      The ID of a file associated with a stream.
    """


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationTypeDef",
    {
        "stream": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationstreamTypeDef,
        "s3Location": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocations3LocationTypeDef,
    },
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationTypeDef
):
    """
    Type definition for `ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFiles` `fileLocation`

    The location of the updated firmware.

    - **stream** *(dict) --*

      The stream that contains the OTA update.

      - **streamId** *(string) --*

        The stream ID.

      - **fileId** *(integer) --*

        The ID of a file associated with a stream.

    - **s3Location** *(dict) --*

      The location of the updated firmware in S3.

      - **bucket** *(string) --*

        The S3 bucket.

      - **key** *(string) --*

        The S3 key.

      - **version** *(string) --*

        The S3 bucket version.
    """


_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesTypeDef",
    {
        "fileName": str,
        "fileVersion": str,
        "fileLocation": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesfileLocationTypeDef,
        "codeSigning": ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilescodeSigningTypeDef,
        "attributes": Dict[str, str],
    },
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesTypeDef
):
    """
    Type definition for `ClientGetOtaUpdateResponseotaUpdateInfo` `otaUpdateFiles`

    Describes a file to be associated with an OTA update.

    - **fileName** *(string) --*

      The name of the file.

    - **fileVersion** *(string) --*

      The file version.

    - **fileLocation** *(dict) --*

      The location of the updated firmware.

      - **stream** *(dict) --*

        The stream that contains the OTA update.

        - **streamId** *(string) --*

          The stream ID.

        - **fileId** *(integer) --*

          The ID of a file associated with a stream.

      - **s3Location** *(dict) --*

        The location of the updated firmware in S3.

        - **bucket** *(string) --*

          The S3 bucket.

        - **key** *(string) --*

          The S3 key.

        - **version** *(string) --*

          The S3 bucket version.

    - **codeSigning** *(dict) --*

      The code signing method of the file.

      - **awsSignerJobId** *(string) --*

        The ID of the AWSSignerJob which was created to sign the file.

      - **startSigningJobParameter** *(dict) --*

        Describes the code-signing job.

        - **signingProfileParameter** *(dict) --*

          Describes the code-signing profile.

          - **certificateArn** *(string) --*

            Certificate ARN.

          - **platform** *(string) --*

            The hardware platform of your device.

          - **certificatePathOnDevice** *(string) --*

            The location of the code-signing certificate on your device.

        - **signingProfileName** *(string) --*

          The code-signing profile name.

        - **destination** *(dict) --*

          The location to write the code-signed file.

          - **s3Destination** *(dict) --*

            Describes the location in S3 of the updated firmware.

            - **bucket** *(string) --*

              The S3 bucket that contains the updated firmware.

            - **prefix** *(string) --*

              The S3 prefix.

      - **customCodeSigning** *(dict) --*

        A custom method for code signing a file.

        - **signature** *(dict) --*

          The signature for the file.

          - **inlineDocument** *(bytes) --*

            A base64 encoded binary representation of the code signing signature.

        - **certificateChain** *(dict) --*

          The certificate chain.

          - **certificateName** *(string) --*

            The name of the certificate.

          - **inlineDocument** *(string) --*

            A base64 encoded binary representation of the code signing certificate chain.

        - **hashAlgorithm** *(string) --*

          The hash algorithm used to code sign the file.

        - **signatureAlgorithm** *(string) --*

          The signature algorithm used to code sign the file.

    - **attributes** *(dict) --*

      A list of name/attribute pairs.

      - *(string) --*

        - *(string) --*
    """


_ClientGetOtaUpdateResponseotaUpdateInfoTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseotaUpdateInfoTypeDef",
    {
        "otaUpdateId": str,
        "otaUpdateArn": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "description": str,
        "targets": List[str],
        "awsJobExecutionsRolloutConfig": ClientGetOtaUpdateResponseotaUpdateInfoawsJobExecutionsRolloutConfigTypeDef,
        "targetSelection": str,
        "otaUpdateFiles": List[
            ClientGetOtaUpdateResponseotaUpdateInfootaUpdateFilesTypeDef
        ],
        "otaUpdateStatus": str,
        "awsIotJobId": str,
        "awsIotJobArn": str,
        "errorInfo": ClientGetOtaUpdateResponseotaUpdateInfoerrorInfoTypeDef,
        "additionalParameters": Dict[str, str],
    },
    total=False,
)


class ClientGetOtaUpdateResponseotaUpdateInfoTypeDef(
    _ClientGetOtaUpdateResponseotaUpdateInfoTypeDef
):
    """
    Type definition for `ClientGetOtaUpdateResponse` `otaUpdateInfo`

    The OTA update info.

    - **otaUpdateId** *(string) --*

      The OTA update ID.

    - **otaUpdateArn** *(string) --*

      The OTA update ARN.

    - **creationDate** *(datetime) --*

      The date when the OTA update was created.

    - **lastModifiedDate** *(datetime) --*

      The date when the OTA update was last updated.

    - **description** *(string) --*

      A description of the OTA update.

    - **targets** *(list) --*

      The targets of the OTA update.

      - *(string) --*

    - **awsJobExecutionsRolloutConfig** *(dict) --*

      Configuration for the rollout of OTA updates.

      - **maximumPerMinute** *(integer) --*

        The maximum number of OTA update job executions started per minute.

    - **targetSelection** *(string) --*

      Specifies whether the OTA update will continue to run (CONTINUOUS), or will be complete
      after all those things specified as targets have completed the OTA update (SNAPSHOT). If
      continuous, the OTA update may also be run on a thing when a change is detected in a
      target. For example, an OTA update will run on a thing when the thing is added to a target
      group, even after the OTA update was completed by all things originally in the group.

    - **otaUpdateFiles** *(list) --*

      A list of files associated with the OTA update.

      - *(dict) --*

        Describes a file to be associated with an OTA update.

        - **fileName** *(string) --*

          The name of the file.

        - **fileVersion** *(string) --*

          The file version.

        - **fileLocation** *(dict) --*

          The location of the updated firmware.

          - **stream** *(dict) --*

            The stream that contains the OTA update.

            - **streamId** *(string) --*

              The stream ID.

            - **fileId** *(integer) --*

              The ID of a file associated with a stream.

          - **s3Location** *(dict) --*

            The location of the updated firmware in S3.

            - **bucket** *(string) --*

              The S3 bucket.

            - **key** *(string) --*

              The S3 key.

            - **version** *(string) --*

              The S3 bucket version.

        - **codeSigning** *(dict) --*

          The code signing method of the file.

          - **awsSignerJobId** *(string) --*

            The ID of the AWSSignerJob which was created to sign the file.

          - **startSigningJobParameter** *(dict) --*

            Describes the code-signing job.

            - **signingProfileParameter** *(dict) --*

              Describes the code-signing profile.

              - **certificateArn** *(string) --*

                Certificate ARN.

              - **platform** *(string) --*

                The hardware platform of your device.

              - **certificatePathOnDevice** *(string) --*

                The location of the code-signing certificate on your device.

            - **signingProfileName** *(string) --*

              The code-signing profile name.

            - **destination** *(dict) --*

              The location to write the code-signed file.

              - **s3Destination** *(dict) --*

                Describes the location in S3 of the updated firmware.

                - **bucket** *(string) --*

                  The S3 bucket that contains the updated firmware.

                - **prefix** *(string) --*

                  The S3 prefix.

          - **customCodeSigning** *(dict) --*

            A custom method for code signing a file.

            - **signature** *(dict) --*

              The signature for the file.

              - **inlineDocument** *(bytes) --*

                A base64 encoded binary representation of the code signing signature.

            - **certificateChain** *(dict) --*

              The certificate chain.

              - **certificateName** *(string) --*

                The name of the certificate.

              - **inlineDocument** *(string) --*

                A base64 encoded binary representation of the code signing certificate chain.

            - **hashAlgorithm** *(string) --*

              The hash algorithm used to code sign the file.

            - **signatureAlgorithm** *(string) --*

              The signature algorithm used to code sign the file.

        - **attributes** *(dict) --*

          A list of name/attribute pairs.

          - *(string) --*

            - *(string) --*

    - **otaUpdateStatus** *(string) --*

      The status of the OTA update.

    - **awsIotJobId** *(string) --*

      The AWS IoT job ID associated with the OTA update.

    - **awsIotJobArn** *(string) --*

      The AWS IoT job ARN associated with the OTA update.

    - **errorInfo** *(dict) --*

      Error information associated with the OTA update.

      - **code** *(string) --*

        The error code.

      - **message** *(string) --*

        The error message.

    - **additionalParameters** *(dict) --*

      A collection of name/value pairs

      - *(string) --*

        - *(string) --*
    """


_ClientGetOtaUpdateResponseTypeDef = TypedDict(
    "_ClientGetOtaUpdateResponseTypeDef",
    {"otaUpdateInfo": ClientGetOtaUpdateResponseotaUpdateInfoTypeDef},
    total=False,
)


class ClientGetOtaUpdateResponseTypeDef(_ClientGetOtaUpdateResponseTypeDef):
    """
    Type definition for `ClientGetOtaUpdate` `Response`

    - **otaUpdateInfo** *(dict) --*

      The OTA update info.

      - **otaUpdateId** *(string) --*

        The OTA update ID.

      - **otaUpdateArn** *(string) --*

        The OTA update ARN.

      - **creationDate** *(datetime) --*

        The date when the OTA update was created.

      - **lastModifiedDate** *(datetime) --*

        The date when the OTA update was last updated.

      - **description** *(string) --*

        A description of the OTA update.

      - **targets** *(list) --*

        The targets of the OTA update.

        - *(string) --*

      - **awsJobExecutionsRolloutConfig** *(dict) --*

        Configuration for the rollout of OTA updates.

        - **maximumPerMinute** *(integer) --*

          The maximum number of OTA update job executions started per minute.

      - **targetSelection** *(string) --*

        Specifies whether the OTA update will continue to run (CONTINUOUS), or will be complete
        after all those things specified as targets have completed the OTA update (SNAPSHOT). If
        continuous, the OTA update may also be run on a thing when a change is detected in a
        target. For example, an OTA update will run on a thing when the thing is added to a target
        group, even after the OTA update was completed by all things originally in the group.

      - **otaUpdateFiles** *(list) --*

        A list of files associated with the OTA update.

        - *(dict) --*

          Describes a file to be associated with an OTA update.

          - **fileName** *(string) --*

            The name of the file.

          - **fileVersion** *(string) --*

            The file version.

          - **fileLocation** *(dict) --*

            The location of the updated firmware.

            - **stream** *(dict) --*

              The stream that contains the OTA update.

              - **streamId** *(string) --*

                The stream ID.

              - **fileId** *(integer) --*

                The ID of a file associated with a stream.

            - **s3Location** *(dict) --*

              The location of the updated firmware in S3.

              - **bucket** *(string) --*

                The S3 bucket.

              - **key** *(string) --*

                The S3 key.

              - **version** *(string) --*

                The S3 bucket version.

          - **codeSigning** *(dict) --*

            The code signing method of the file.

            - **awsSignerJobId** *(string) --*

              The ID of the AWSSignerJob which was created to sign the file.

            - **startSigningJobParameter** *(dict) --*

              Describes the code-signing job.

              - **signingProfileParameter** *(dict) --*

                Describes the code-signing profile.

                - **certificateArn** *(string) --*

                  Certificate ARN.

                - **platform** *(string) --*

                  The hardware platform of your device.

                - **certificatePathOnDevice** *(string) --*

                  The location of the code-signing certificate on your device.

              - **signingProfileName** *(string) --*

                The code-signing profile name.

              - **destination** *(dict) --*

                The location to write the code-signed file.

                - **s3Destination** *(dict) --*

                  Describes the location in S3 of the updated firmware.

                  - **bucket** *(string) --*

                    The S3 bucket that contains the updated firmware.

                  - **prefix** *(string) --*

                    The S3 prefix.

            - **customCodeSigning** *(dict) --*

              A custom method for code signing a file.

              - **signature** *(dict) --*

                The signature for the file.

                - **inlineDocument** *(bytes) --*

                  A base64 encoded binary representation of the code signing signature.

              - **certificateChain** *(dict) --*

                The certificate chain.

                - **certificateName** *(string) --*

                  The name of the certificate.

                - **inlineDocument** *(string) --*

                  A base64 encoded binary representation of the code signing certificate chain.

              - **hashAlgorithm** *(string) --*

                The hash algorithm used to code sign the file.

              - **signatureAlgorithm** *(string) --*

                The signature algorithm used to code sign the file.

          - **attributes** *(dict) --*

            A list of name/attribute pairs.

            - *(string) --*

              - *(string) --*

      - **otaUpdateStatus** *(string) --*

        The status of the OTA update.

      - **awsIotJobId** *(string) --*

        The AWS IoT job ID associated with the OTA update.

      - **awsIotJobArn** *(string) --*

        The AWS IoT job ARN associated with the OTA update.

      - **errorInfo** *(dict) --*

        Error information associated with the OTA update.

        - **code** *(string) --*

          The error code.

        - **message** *(string) --*

          The error message.

      - **additionalParameters** *(dict) --*

        A collection of name/value pairs

        - *(string) --*

          - *(string) --*
    """


_ClientGetPercentilesResponsepercentilesTypeDef = TypedDict(
    "_ClientGetPercentilesResponsepercentilesTypeDef",
    {"percent": float, "value": float},
    total=False,
)


class ClientGetPercentilesResponsepercentilesTypeDef(
    _ClientGetPercentilesResponsepercentilesTypeDef
):
    """
    Type definition for `ClientGetPercentilesResponse` `percentiles`

    Describes the percentile and percentile value.

    - **percent** *(float) --*

      The percentile.

    - **value** *(float) --*

      The value.
    """


_ClientGetPercentilesResponseTypeDef = TypedDict(
    "_ClientGetPercentilesResponseTypeDef",
    {"percentiles": List[ClientGetPercentilesResponsepercentilesTypeDef]},
    total=False,
)


class ClientGetPercentilesResponseTypeDef(_ClientGetPercentilesResponseTypeDef):
    """
    Type definition for `ClientGetPercentiles` `Response`

    - **percentiles** *(list) --*

      The percentile values of the aggregated fields.

      - *(dict) --*

        Describes the percentile and percentile value.

        - **percent** *(float) --*

          The percentile.

        - **value** *(float) --*

          The value.
    """


_ClientGetPolicyResponseTypeDef = TypedDict(
    "_ClientGetPolicyResponseTypeDef",
    {
        "policyName": str,
        "policyArn": str,
        "policyDocument": str,
        "defaultVersionId": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "generationId": str,
    },
    total=False,
)


class ClientGetPolicyResponseTypeDef(_ClientGetPolicyResponseTypeDef):
    """
    Type definition for `ClientGetPolicy` `Response`

    The output from the GetPolicy operation.

    - **policyName** *(string) --*

      The policy name.

    - **policyArn** *(string) --*

      The policy ARN.

    - **policyDocument** *(string) --*

      The JSON document that describes the policy.

    - **defaultVersionId** *(string) --*

      The default policy version ID.

    - **creationDate** *(datetime) --*

      The date the policy was created.

    - **lastModifiedDate** *(datetime) --*

      The date the policy was last modified.

    - **generationId** *(string) --*

      The generation ID of the policy.
    """


_ClientGetPolicyVersionResponseTypeDef = TypedDict(
    "_ClientGetPolicyVersionResponseTypeDef",
    {
        "policyArn": str,
        "policyName": str,
        "policyDocument": str,
        "policyVersionId": str,
        "isDefaultVersion": bool,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "generationId": str,
    },
    total=False,
)


class ClientGetPolicyVersionResponseTypeDef(_ClientGetPolicyVersionResponseTypeDef):
    """
    Type definition for `ClientGetPolicyVersion` `Response`

    The output from the GetPolicyVersion operation.

    - **policyArn** *(string) --*

      The policy ARN.

    - **policyName** *(string) --*

      The policy name.

    - **policyDocument** *(string) --*

      The JSON document that describes the policy.

    - **policyVersionId** *(string) --*

      The policy version ID.

    - **isDefaultVersion** *(boolean) --*

      Specifies whether the policy version is the default.

    - **creationDate** *(datetime) --*

      The date the policy was created.

    - **lastModifiedDate** *(datetime) --*

      The date the policy was last modified.

    - **generationId** *(string) --*

      The generation ID of the policy version.
    """


_ClientGetRegistrationCodeResponseTypeDef = TypedDict(
    "_ClientGetRegistrationCodeResponseTypeDef", {"registrationCode": str}, total=False
)


class ClientGetRegistrationCodeResponseTypeDef(
    _ClientGetRegistrationCodeResponseTypeDef
):
    """
    Type definition for `ClientGetRegistrationCode` `Response`

    The output from the GetRegistrationCode operation.

    - **registrationCode** *(string) --*

      The CA certificate registration code.
    """


_ClientGetStatisticsResponsestatisticsTypeDef = TypedDict(
    "_ClientGetStatisticsResponsestatisticsTypeDef",
    {
        "count": int,
        "average": float,
        "sum": float,
        "minimum": float,
        "maximum": float,
        "sumOfSquares": float,
        "variance": float,
        "stdDeviation": float,
    },
    total=False,
)


class ClientGetStatisticsResponsestatisticsTypeDef(
    _ClientGetStatisticsResponsestatisticsTypeDef
):
    """
    Type definition for `ClientGetStatisticsResponse` `statistics`

    The statistics returned by the Fleet Indexing service based on the query and aggregation
    field.

    - **count** *(integer) --*

      The count of things that match the query.

    - **average** *(float) --*

      The average of the aggregated field values.

    - **sum** *(float) --*

      The sum of the aggregated field values.

    - **minimum** *(float) --*

      The minimum aggregated field value.

    - **maximum** *(float) --*

      The maximum aggregated field value.

    - **sumOfSquares** *(float) --*

      The sum of the squares of the aggregated field values.

    - **variance** *(float) --*

      The variance of the aggregated field values.

    - **stdDeviation** *(float) --*

      The standard deviation of the aggregated field valuesl
    """


_ClientGetStatisticsResponseTypeDef = TypedDict(
    "_ClientGetStatisticsResponseTypeDef",
    {"statistics": ClientGetStatisticsResponsestatisticsTypeDef},
    total=False,
)


class ClientGetStatisticsResponseTypeDef(_ClientGetStatisticsResponseTypeDef):
    """
    Type definition for `ClientGetStatistics` `Response`

    - **statistics** *(dict) --*

      The statistics returned by the Fleet Indexing service based on the query and aggregation
      field.

      - **count** *(integer) --*

        The count of things that match the query.

      - **average** *(float) --*

        The average of the aggregated field values.

      - **sum** *(float) --*

        The sum of the aggregated field values.

      - **minimum** *(float) --*

        The minimum aggregated field value.

      - **maximum** *(float) --*

        The maximum aggregated field value.

      - **sumOfSquares** *(float) --*

        The sum of the squares of the aggregated field values.

      - **variance** *(float) --*

        The variance of the aggregated field values.

      - **stdDeviation** *(float) --*

        The standard deviation of the aggregated field valuesl
    """


_ClientGetTopicRuleResponseruleactionscloudwatchAlarmTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionscloudwatchAlarmTypeDef",
    {"roleArn": str, "alarmName": str, "stateReason": str, "stateValue": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionscloudwatchAlarmTypeDef(
    _ClientGetTopicRuleResponseruleactionscloudwatchAlarmTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleactions` `cloudwatchAlarm`

    Change the state of a CloudWatch alarm.

    - **roleArn** *(string) --*

      The IAM role that allows access to the CloudWatch alarm.

    - **alarmName** *(string) --*

      The CloudWatch alarm name.

    - **stateReason** *(string) --*

      The reason for the alarm change.

    - **stateValue** *(string) --*

      The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
    """


_ClientGetTopicRuleResponseruleactionscloudwatchMetricTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionscloudwatchMetricTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
        "metricTimestamp": str,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleactionscloudwatchMetricTypeDef(
    _ClientGetTopicRuleResponseruleactionscloudwatchMetricTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleactions` `cloudwatchMetric`

    Capture a CloudWatch metric.

    - **roleArn** *(string) --*

      The IAM role that allows access to the CloudWatch metric.

    - **metricNamespace** *(string) --*

      The CloudWatch metric namespace name.

    - **metricName** *(string) --*

      The CloudWatch metric name.

    - **metricValue** *(string) --*

      The CloudWatch metric value.

    - **metricUnit** *(string) --*

      The `metric unit
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
      supported by CloudWatch.

    - **metricTimestamp** *(string) --*

      An optional `Unix timestamp
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
      .
    """


_ClientGetTopicRuleResponseruleactionsdynamoDBTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsdynamoDBTypeDef",
    {
        "tableName": str,
        "roleArn": str,
        "operation": str,
        "hashKeyField": str,
        "hashKeyValue": str,
        "hashKeyType": str,
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": str,
        "payloadField": str,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleactionsdynamoDBTypeDef(
    _ClientGetTopicRuleResponseruleactionsdynamoDBTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleactions` `dynamoDB`

    Write to a DynamoDB table.

    - **tableName** *(string) --*

      The name of the DynamoDB table.

    - **roleArn** *(string) --*

      The ARN of the IAM role that grants access to the DynamoDB table.

    - **operation** *(string) --*

      The type of operation to be performed. This follows the substitution template, so it
      can be ``${operation}`` , but the substitution must result in one of the following:
      ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

    - **hashKeyField** *(string) --*

      The hash key name.

    - **hashKeyValue** *(string) --*

      The hash key value.

    - **hashKeyType** *(string) --*

      The hash key type. Valid values are "STRING" or "NUMBER"

    - **rangeKeyField** *(string) --*

      The range key name.

    - **rangeKeyValue** *(string) --*

      The range key value.

    - **rangeKeyType** *(string) --*

      The range key type. Valid values are "STRING" or "NUMBER"

    - **payloadField** *(string) --*

      The action payload. This name can be customized.
    """


_ClientGetTopicRuleResponseruleactionsdynamoDBv2putItemTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsdynamoDBv2putItemTypeDef",
    {"tableName": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionsdynamoDBv2putItemTypeDef(
    _ClientGetTopicRuleResponseruleactionsdynamoDBv2putItemTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleactionsdynamoDBv2` `putItem`

    Specifies the DynamoDB table to which the message data will be written. For example:

     ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
     "my-table" } } }``

    Each attribute in the message payload will be written to a separate column in the
    DynamoDB database.

    - **tableName** *(string) --*

      The table where the message data will be written.
    """


_ClientGetTopicRuleResponseruleactionsdynamoDBv2TypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsdynamoDBv2TypeDef",
    {
        "roleArn": str,
        "putItem": ClientGetTopicRuleResponseruleactionsdynamoDBv2putItemTypeDef,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleactionsdynamoDBv2TypeDef(
    _ClientGetTopicRuleResponseruleactionsdynamoDBv2TypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleactions` `dynamoDBv2`

    Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you
    to write each attribute in an MQTT message payload into a separate DynamoDB column.

    - **roleArn** *(string) --*

      The ARN of the IAM role that grants access to the DynamoDB table.

    - **putItem** *(dict) --*

      Specifies the DynamoDB table to which the message data will be written. For example:

       ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
       "my-table" } } }``

      Each attribute in the message payload will be written to a separate column in the
      DynamoDB database.

      - **tableName** *(string) --*

        The table where the message data will be written.
    """


_ClientGetTopicRuleResponseruleactionselasticsearchTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionselasticsearchTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionselasticsearchTypeDef(
    _ClientGetTopicRuleResponseruleactionselasticsearchTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleactions` `elasticsearch`

    Write data to an Amazon Elasticsearch Service domain.

    - **roleArn** *(string) --*

      The IAM role ARN that has access to Elasticsearch.

    - **endpoint** *(string) --*

      The endpoint of your Elasticsearch domain.

    - **index** *(string) --*

      The Elasticsearch index where you want to store your data.

    - **type** *(string) --*

      The type of document you are storing.

    - **id** *(string) --*

      The unique identifier for the document you are storing.
    """


_ClientGetTopicRuleResponseruleactionsfirehoseTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsfirehoseTypeDef",
    {"roleArn": str, "deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionsfirehoseTypeDef(
    _ClientGetTopicRuleResponseruleactionsfirehoseTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleactions` `firehose`

    Write to an Amazon Kinesis Firehose stream.

    - **roleArn** *(string) --*

      The IAM role that grants access to the Amazon Kinesis Firehose stream.

    - **deliveryStreamName** *(string) --*

      The delivery stream name.

    - **separator** *(string) --*

      A character separator that will be used to separate records written to the Firehose
      stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline),
      ',' (comma).
    """


_ClientGetTopicRuleResponseruleactionsiotAnalyticsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsiotAnalyticsTypeDef",
    {"channelArn": str, "channelName": str, "roleArn": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionsiotAnalyticsTypeDef(
    _ClientGetTopicRuleResponseruleactionsiotAnalyticsTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleactions` `iotAnalytics`

    Sends message data to an AWS IoT Analytics channel.

    - **channelArn** *(string) --*

      (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

    - **channelName** *(string) --*

      The name of the IoT Analytics channel to which message data will be sent.

    - **roleArn** *(string) --*

      The ARN of the role which has a policy that grants IoT Analytics permission to send
      message data via IoT Analytics (iotanalytics:BatchPutMessage).
    """


_ClientGetTopicRuleResponseruleactionsiotEventsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsiotEventsTypeDef",
    {"inputName": str, "messageId": str, "roleArn": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionsiotEventsTypeDef(
    _ClientGetTopicRuleResponseruleactionsiotEventsTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleactions` `iotEvents`

    Sends an input to an AWS IoT Events detector.

    - **inputName** *(string) --*

      The name of the AWS IoT Events input.

    - **messageId** *(string) --*

      [Optional] Use this to ensure that only one input (message) with a given messageId
      will be processed by an AWS IoT Events detector.

    - **roleArn** *(string) --*

      The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT
      Events detector. ("Action":"iotevents:BatchPutMessage").
    """


_ClientGetTopicRuleResponseruleactionskinesisTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionskinesisTypeDef",
    {"roleArn": str, "streamName": str, "partitionKey": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionskinesisTypeDef(
    _ClientGetTopicRuleResponseruleactionskinesisTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleactions` `kinesis`

    Write data to an Amazon Kinesis stream.

    - **roleArn** *(string) --*

      The ARN of the IAM role that grants access to the Amazon Kinesis stream.

    - **streamName** *(string) --*

      The name of the Amazon Kinesis stream.

    - **partitionKey** *(string) --*

      The partition key.
    """


_ClientGetTopicRuleResponseruleactionslambdaTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionslambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionslambdaTypeDef(
    _ClientGetTopicRuleResponseruleactionslambdaTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleactions` `lambda`

    Invoke a Lambda function.

    - **functionArn** *(string) --*

      The ARN of the Lambda function.
    """


_ClientGetTopicRuleResponseruleactionsrepublishTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsrepublishTypeDef",
    {"roleArn": str, "topic": str, "qos": int},
    total=False,
)


class ClientGetTopicRuleResponseruleactionsrepublishTypeDef(
    _ClientGetTopicRuleResponseruleactionsrepublishTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleactions` `republish`

    Publish to another MQTT topic.

    - **roleArn** *(string) --*

      The ARN of the IAM role that grants access.

    - **topic** *(string) --*

      The name of the MQTT topic.

    - **qos** *(integer) --*

      The Quality of Service (QoS) level to use when republishing messages. The default
      value is 0.
    """


_ClientGetTopicRuleResponseruleactionss3TypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionss3TypeDef",
    {"roleArn": str, "bucketName": str, "key": str, "cannedAcl": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionss3TypeDef(
    _ClientGetTopicRuleResponseruleactionss3TypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleactions` `s3`

    Write to an Amazon S3 bucket.

    - **roleArn** *(string) --*

      The ARN of the IAM role that grants access.

    - **bucketName** *(string) --*

      The Amazon S3 bucket.

    - **key** *(string) --*

      The object key.

    - **cannedAcl** *(string) --*

      The Amazon S3 canned ACL that controls access to the object identified by the object
      key. For more information, see `S3 canned ACLs
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .
    """


_ClientGetTopicRuleResponseruleactionssalesforceTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionssalesforceTypeDef",
    {"token": str, "url": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionssalesforceTypeDef(
    _ClientGetTopicRuleResponseruleactionssalesforceTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleactions` `salesforce`

    Send a message to a Salesforce IoT Cloud Input Stream.

    - **token** *(string) --*

      The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The
      token is available from the Salesforce IoT Cloud platform after creation of the Input
      Stream.

    - **url** *(string) --*

      The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from
      the Salesforce IoT Cloud platform after creation of the Input Stream.
    """


_ClientGetTopicRuleResponseruleactionssnsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionssnsTypeDef",
    {"targetArn": str, "roleArn": str, "messageFormat": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionssnsTypeDef(
    _ClientGetTopicRuleResponseruleactionssnsTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleactions` `sns`

    Publish to an Amazon SNS topic.

    - **targetArn** *(string) --*

      The ARN of the SNS topic.

    - **roleArn** *(string) --*

      The ARN of the IAM role that grants access.

    - **messageFormat** *(string) --*

      (Optional) The message format of the message to publish. Accepted values are "JSON"
      and "RAW". The default value of the attribute is "RAW". SNS uses this setting to
      determine if the payload should be parsed and relevant platform-specific bits of the
      payload should be extracted. To read more about SNS message formats, see
      `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
      <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their
      official documentation.
    """


_ClientGetTopicRuleResponseruleactionssqsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionssqsTypeDef",
    {"roleArn": str, "queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientGetTopicRuleResponseruleactionssqsTypeDef(
    _ClientGetTopicRuleResponseruleactionssqsTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleactions` `sqs`

    Publish to an Amazon SQS queue.

    - **roleArn** *(string) --*

      The ARN of the IAM role that grants access.

    - **queueUrl** *(string) --*

      The URL of the Amazon SQS queue.

    - **useBase64** *(boolean) --*

      Specifies whether to use Base64 encoding.
    """


_ClientGetTopicRuleResponseruleactionsstepFunctionsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsstepFunctionsTypeDef",
    {"executionNamePrefix": str, "stateMachineName": str, "roleArn": str},
    total=False,
)


class ClientGetTopicRuleResponseruleactionsstepFunctionsTypeDef(
    _ClientGetTopicRuleResponseruleactionsstepFunctionsTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleactions` `stepFunctions`

    Starts execution of a Step Functions state machine.

    - **executionNamePrefix** *(string) --*

      (Optional) A name will be given to the state machine execution consisting of this
      prefix followed by a UUID. Step Functions automatically creates a unique name for
      each state machine execution if one is not provided.

    - **stateMachineName** *(string) --*

      The name of the Step Functions state machine whose execution will be started.

    - **roleArn** *(string) --*

      The ARN of the role that grants IoT permission to start execution of a state machine
      ("Action":"states:StartExecution").
    """


_ClientGetTopicRuleResponseruleactionsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleactionsTypeDef",
    {
        "dynamoDB": ClientGetTopicRuleResponseruleactionsdynamoDBTypeDef,
        "dynamoDBv2": ClientGetTopicRuleResponseruleactionsdynamoDBv2TypeDef,
        "lambda": ClientGetTopicRuleResponseruleactionslambdaTypeDef,
        "sns": ClientGetTopicRuleResponseruleactionssnsTypeDef,
        "sqs": ClientGetTopicRuleResponseruleactionssqsTypeDef,
        "kinesis": ClientGetTopicRuleResponseruleactionskinesisTypeDef,
        "republish": ClientGetTopicRuleResponseruleactionsrepublishTypeDef,
        "s3": ClientGetTopicRuleResponseruleactionss3TypeDef,
        "firehose": ClientGetTopicRuleResponseruleactionsfirehoseTypeDef,
        "cloudwatchMetric": ClientGetTopicRuleResponseruleactionscloudwatchMetricTypeDef,
        "cloudwatchAlarm": ClientGetTopicRuleResponseruleactionscloudwatchAlarmTypeDef,
        "elasticsearch": ClientGetTopicRuleResponseruleactionselasticsearchTypeDef,
        "salesforce": ClientGetTopicRuleResponseruleactionssalesforceTypeDef,
        "iotAnalytics": ClientGetTopicRuleResponseruleactionsiotAnalyticsTypeDef,
        "iotEvents": ClientGetTopicRuleResponseruleactionsiotEventsTypeDef,
        "stepFunctions": ClientGetTopicRuleResponseruleactionsstepFunctionsTypeDef,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleactionsTypeDef(
    _ClientGetTopicRuleResponseruleactionsTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponserule` `actions`

    Describes the actions associated with a rule.

    - **dynamoDB** *(dict) --*

      Write to a DynamoDB table.

      - **tableName** *(string) --*

        The name of the DynamoDB table.

      - **roleArn** *(string) --*

        The ARN of the IAM role that grants access to the DynamoDB table.

      - **operation** *(string) --*

        The type of operation to be performed. This follows the substitution template, so it
        can be ``${operation}`` , but the substitution must result in one of the following:
        ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

      - **hashKeyField** *(string) --*

        The hash key name.

      - **hashKeyValue** *(string) --*

        The hash key value.

      - **hashKeyType** *(string) --*

        The hash key type. Valid values are "STRING" or "NUMBER"

      - **rangeKeyField** *(string) --*

        The range key name.

      - **rangeKeyValue** *(string) --*

        The range key value.

      - **rangeKeyType** *(string) --*

        The range key type. Valid values are "STRING" or "NUMBER"

      - **payloadField** *(string) --*

        The action payload. This name can be customized.

    - **dynamoDBv2** *(dict) --*

      Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you
      to write each attribute in an MQTT message payload into a separate DynamoDB column.

      - **roleArn** *(string) --*

        The ARN of the IAM role that grants access to the DynamoDB table.

      - **putItem** *(dict) --*

        Specifies the DynamoDB table to which the message data will be written. For example:

         ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
         "my-table" } } }``

        Each attribute in the message payload will be written to a separate column in the
        DynamoDB database.

        - **tableName** *(string) --*

          The table where the message data will be written.

    - **lambda** *(dict) --*

      Invoke a Lambda function.

      - **functionArn** *(string) --*

        The ARN of the Lambda function.

    - **sns** *(dict) --*

      Publish to an Amazon SNS topic.

      - **targetArn** *(string) --*

        The ARN of the SNS topic.

      - **roleArn** *(string) --*

        The ARN of the IAM role that grants access.

      - **messageFormat** *(string) --*

        (Optional) The message format of the message to publish. Accepted values are "JSON"
        and "RAW". The default value of the attribute is "RAW". SNS uses this setting to
        determine if the payload should be parsed and relevant platform-specific bits of the
        payload should be extracted. To read more about SNS message formats, see
        `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
        <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their
        official documentation.

    - **sqs** *(dict) --*

      Publish to an Amazon SQS queue.

      - **roleArn** *(string) --*

        The ARN of the IAM role that grants access.

      - **queueUrl** *(string) --*

        The URL of the Amazon SQS queue.

      - **useBase64** *(boolean) --*

        Specifies whether to use Base64 encoding.

    - **kinesis** *(dict) --*

      Write data to an Amazon Kinesis stream.

      - **roleArn** *(string) --*

        The ARN of the IAM role that grants access to the Amazon Kinesis stream.

      - **streamName** *(string) --*

        The name of the Amazon Kinesis stream.

      - **partitionKey** *(string) --*

        The partition key.

    - **republish** *(dict) --*

      Publish to another MQTT topic.

      - **roleArn** *(string) --*

        The ARN of the IAM role that grants access.

      - **topic** *(string) --*

        The name of the MQTT topic.

      - **qos** *(integer) --*

        The Quality of Service (QoS) level to use when republishing messages. The default
        value is 0.

    - **s3** *(dict) --*

      Write to an Amazon S3 bucket.

      - **roleArn** *(string) --*

        The ARN of the IAM role that grants access.

      - **bucketName** *(string) --*

        The Amazon S3 bucket.

      - **key** *(string) --*

        The object key.

      - **cannedAcl** *(string) --*

        The Amazon S3 canned ACL that controls access to the object identified by the object
        key. For more information, see `S3 canned ACLs
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

    - **firehose** *(dict) --*

      Write to an Amazon Kinesis Firehose stream.

      - **roleArn** *(string) --*

        The IAM role that grants access to the Amazon Kinesis Firehose stream.

      - **deliveryStreamName** *(string) --*

        The delivery stream name.

      - **separator** *(string) --*

        A character separator that will be used to separate records written to the Firehose
        stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline),
        ',' (comma).

    - **cloudwatchMetric** *(dict) --*

      Capture a CloudWatch metric.

      - **roleArn** *(string) --*

        The IAM role that allows access to the CloudWatch metric.

      - **metricNamespace** *(string) --*

        The CloudWatch metric namespace name.

      - **metricName** *(string) --*

        The CloudWatch metric name.

      - **metricValue** *(string) --*

        The CloudWatch metric value.

      - **metricUnit** *(string) --*

        The `metric unit
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
        supported by CloudWatch.

      - **metricTimestamp** *(string) --*

        An optional `Unix timestamp
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
        .

    - **cloudwatchAlarm** *(dict) --*

      Change the state of a CloudWatch alarm.

      - **roleArn** *(string) --*

        The IAM role that allows access to the CloudWatch alarm.

      - **alarmName** *(string) --*

        The CloudWatch alarm name.

      - **stateReason** *(string) --*

        The reason for the alarm change.

      - **stateValue** *(string) --*

        The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

    - **elasticsearch** *(dict) --*

      Write data to an Amazon Elasticsearch Service domain.

      - **roleArn** *(string) --*

        The IAM role ARN that has access to Elasticsearch.

      - **endpoint** *(string) --*

        The endpoint of your Elasticsearch domain.

      - **index** *(string) --*

        The Elasticsearch index where you want to store your data.

      - **type** *(string) --*

        The type of document you are storing.

      - **id** *(string) --*

        The unique identifier for the document you are storing.

    - **salesforce** *(dict) --*

      Send a message to a Salesforce IoT Cloud Input Stream.

      - **token** *(string) --*

        The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The
        token is available from the Salesforce IoT Cloud platform after creation of the Input
        Stream.

      - **url** *(string) --*

        The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from
        the Salesforce IoT Cloud platform after creation of the Input Stream.

    - **iotAnalytics** *(dict) --*

      Sends message data to an AWS IoT Analytics channel.

      - **channelArn** *(string) --*

        (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

      - **channelName** *(string) --*

        The name of the IoT Analytics channel to which message data will be sent.

      - **roleArn** *(string) --*

        The ARN of the role which has a policy that grants IoT Analytics permission to send
        message data via IoT Analytics (iotanalytics:BatchPutMessage).

    - **iotEvents** *(dict) --*

      Sends an input to an AWS IoT Events detector.

      - **inputName** *(string) --*

        The name of the AWS IoT Events input.

      - **messageId** *(string) --*

        [Optional] Use this to ensure that only one input (message) with a given messageId
        will be processed by an AWS IoT Events detector.

      - **roleArn** *(string) --*

        The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT
        Events detector. ("Action":"iotevents:BatchPutMessage").

    - **stepFunctions** *(dict) --*

      Starts execution of a Step Functions state machine.

      - **executionNamePrefix** *(string) --*

        (Optional) A name will be given to the state machine execution consisting of this
        prefix followed by a UUID. Step Functions automatically creates a unique name for
        each state machine execution if one is not provided.

      - **stateMachineName** *(string) --*

        The name of the Step Functions state machine whose execution will be started.

      - **roleArn** *(string) --*

        The ARN of the role that grants IoT permission to start execution of a state machine
        ("Action":"states:StartExecution").
    """


_ClientGetTopicRuleResponseruleerrorActioncloudwatchAlarmTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActioncloudwatchAlarmTypeDef",
    {"roleArn": str, "alarmName": str, "stateReason": str, "stateValue": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActioncloudwatchAlarmTypeDef(
    _ClientGetTopicRuleResponseruleerrorActioncloudwatchAlarmTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleerrorAction` `cloudwatchAlarm`

    Change the state of a CloudWatch alarm.

    - **roleArn** *(string) --*

      The IAM role that allows access to the CloudWatch alarm.

    - **alarmName** *(string) --*

      The CloudWatch alarm name.

    - **stateReason** *(string) --*

      The reason for the alarm change.

    - **stateValue** *(string) --*

      The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
    """


_ClientGetTopicRuleResponseruleerrorActioncloudwatchMetricTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActioncloudwatchMetricTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
        "metricTimestamp": str,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActioncloudwatchMetricTypeDef(
    _ClientGetTopicRuleResponseruleerrorActioncloudwatchMetricTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleerrorAction` `cloudwatchMetric`

    Capture a CloudWatch metric.

    - **roleArn** *(string) --*

      The IAM role that allows access to the CloudWatch metric.

    - **metricNamespace** *(string) --*

      The CloudWatch metric namespace name.

    - **metricName** *(string) --*

      The CloudWatch metric name.

    - **metricValue** *(string) --*

      The CloudWatch metric value.

    - **metricUnit** *(string) --*

      The `metric unit
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
      supported by CloudWatch.

    - **metricTimestamp** *(string) --*

      An optional `Unix timestamp
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
      .
    """


_ClientGetTopicRuleResponseruleerrorActiondynamoDBTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActiondynamoDBTypeDef",
    {
        "tableName": str,
        "roleArn": str,
        "operation": str,
        "hashKeyField": str,
        "hashKeyValue": str,
        "hashKeyType": str,
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": str,
        "payloadField": str,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActiondynamoDBTypeDef(
    _ClientGetTopicRuleResponseruleerrorActiondynamoDBTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleerrorAction` `dynamoDB`

    Write to a DynamoDB table.

    - **tableName** *(string) --*

      The name of the DynamoDB table.

    - **roleArn** *(string) --*

      The ARN of the IAM role that grants access to the DynamoDB table.

    - **operation** *(string) --*

      The type of operation to be performed. This follows the substitution template, so it
      can be ``${operation}`` , but the substitution must result in one of the following:
      ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

    - **hashKeyField** *(string) --*

      The hash key name.

    - **hashKeyValue** *(string) --*

      The hash key value.

    - **hashKeyType** *(string) --*

      The hash key type. Valid values are "STRING" or "NUMBER"

    - **rangeKeyField** *(string) --*

      The range key name.

    - **rangeKeyValue** *(string) --*

      The range key value.

    - **rangeKeyType** *(string) --*

      The range key type. Valid values are "STRING" or "NUMBER"

    - **payloadField** *(string) --*

      The action payload. This name can be customized.
    """


_ClientGetTopicRuleResponseruleerrorActiondynamoDBv2putItemTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActiondynamoDBv2putItemTypeDef",
    {"tableName": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActiondynamoDBv2putItemTypeDef(
    _ClientGetTopicRuleResponseruleerrorActiondynamoDBv2putItemTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleerrorActiondynamoDBv2` `putItem`

    Specifies the DynamoDB table to which the message data will be written. For example:

     ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
     "my-table" } } }``

    Each attribute in the message payload will be written to a separate column in the
    DynamoDB database.

    - **tableName** *(string) --*

      The table where the message data will be written.
    """


_ClientGetTopicRuleResponseruleerrorActiondynamoDBv2TypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActiondynamoDBv2TypeDef",
    {
        "roleArn": str,
        "putItem": ClientGetTopicRuleResponseruleerrorActiondynamoDBv2putItemTypeDef,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActiondynamoDBv2TypeDef(
    _ClientGetTopicRuleResponseruleerrorActiondynamoDBv2TypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleerrorAction` `dynamoDBv2`

    Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to
    write each attribute in an MQTT message payload into a separate DynamoDB column.

    - **roleArn** *(string) --*

      The ARN of the IAM role that grants access to the DynamoDB table.

    - **putItem** *(dict) --*

      Specifies the DynamoDB table to which the message data will be written. For example:

       ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
       "my-table" } } }``

      Each attribute in the message payload will be written to a separate column in the
      DynamoDB database.

      - **tableName** *(string) --*

        The table where the message data will be written.
    """


_ClientGetTopicRuleResponseruleerrorActionelasticsearchTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionelasticsearchTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionelasticsearchTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionelasticsearchTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleerrorAction` `elasticsearch`

    Write data to an Amazon Elasticsearch Service domain.

    - **roleArn** *(string) --*

      The IAM role ARN that has access to Elasticsearch.

    - **endpoint** *(string) --*

      The endpoint of your Elasticsearch domain.

    - **index** *(string) --*

      The Elasticsearch index where you want to store your data.

    - **type** *(string) --*

      The type of document you are storing.

    - **id** *(string) --*

      The unique identifier for the document you are storing.
    """


_ClientGetTopicRuleResponseruleerrorActionfirehoseTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionfirehoseTypeDef",
    {"roleArn": str, "deliveryStreamName": str, "separator": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionfirehoseTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionfirehoseTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleerrorAction` `firehose`

    Write to an Amazon Kinesis Firehose stream.

    - **roleArn** *(string) --*

      The IAM role that grants access to the Amazon Kinesis Firehose stream.

    - **deliveryStreamName** *(string) --*

      The delivery stream name.

    - **separator** *(string) --*

      A character separator that will be used to separate records written to the Firehose
      stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ','
      (comma).
    """


_ClientGetTopicRuleResponseruleerrorActioniotAnalyticsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActioniotAnalyticsTypeDef",
    {"channelArn": str, "channelName": str, "roleArn": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActioniotAnalyticsTypeDef(
    _ClientGetTopicRuleResponseruleerrorActioniotAnalyticsTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleerrorAction` `iotAnalytics`

    Sends message data to an AWS IoT Analytics channel.

    - **channelArn** *(string) --*

      (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

    - **channelName** *(string) --*

      The name of the IoT Analytics channel to which message data will be sent.

    - **roleArn** *(string) --*

      The ARN of the role which has a policy that grants IoT Analytics permission to send
      message data via IoT Analytics (iotanalytics:BatchPutMessage).
    """


_ClientGetTopicRuleResponseruleerrorActioniotEventsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActioniotEventsTypeDef",
    {"inputName": str, "messageId": str, "roleArn": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActioniotEventsTypeDef(
    _ClientGetTopicRuleResponseruleerrorActioniotEventsTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleerrorAction` `iotEvents`

    Sends an input to an AWS IoT Events detector.

    - **inputName** *(string) --*

      The name of the AWS IoT Events input.

    - **messageId** *(string) --*

      [Optional] Use this to ensure that only one input (message) with a given messageId will
      be processed by an AWS IoT Events detector.

    - **roleArn** *(string) --*

      The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT
      Events detector. ("Action":"iotevents:BatchPutMessage").
    """


_ClientGetTopicRuleResponseruleerrorActionkinesisTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionkinesisTypeDef",
    {"roleArn": str, "streamName": str, "partitionKey": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionkinesisTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionkinesisTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleerrorAction` `kinesis`

    Write data to an Amazon Kinesis stream.

    - **roleArn** *(string) --*

      The ARN of the IAM role that grants access to the Amazon Kinesis stream.

    - **streamName** *(string) --*

      The name of the Amazon Kinesis stream.

    - **partitionKey** *(string) --*

      The partition key.
    """


_ClientGetTopicRuleResponseruleerrorActionlambdaTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionlambdaTypeDef",
    {"functionArn": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionlambdaTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionlambdaTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleerrorAction` `lambda`

    Invoke a Lambda function.

    - **functionArn** *(string) --*

      The ARN of the Lambda function.
    """


_ClientGetTopicRuleResponseruleerrorActionrepublishTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionrepublishTypeDef",
    {"roleArn": str, "topic": str, "qos": int},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionrepublishTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionrepublishTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleerrorAction` `republish`

    Publish to another MQTT topic.

    - **roleArn** *(string) --*

      The ARN of the IAM role that grants access.

    - **topic** *(string) --*

      The name of the MQTT topic.

    - **qos** *(integer) --*

      The Quality of Service (QoS) level to use when republishing messages. The default value
      is 0.
    """


_ClientGetTopicRuleResponseruleerrorActions3TypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActions3TypeDef",
    {"roleArn": str, "bucketName": str, "key": str, "cannedAcl": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActions3TypeDef(
    _ClientGetTopicRuleResponseruleerrorActions3TypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleerrorAction` `s3`

    Write to an Amazon S3 bucket.

    - **roleArn** *(string) --*

      The ARN of the IAM role that grants access.

    - **bucketName** *(string) --*

      The Amazon S3 bucket.

    - **key** *(string) --*

      The object key.

    - **cannedAcl** *(string) --*

      The Amazon S3 canned ACL that controls access to the object identified by the object
      key. For more information, see `S3 canned ACLs
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .
    """


_ClientGetTopicRuleResponseruleerrorActionsalesforceTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionsalesforceTypeDef",
    {"token": str, "url": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionsalesforceTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionsalesforceTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleerrorAction` `salesforce`

    Send a message to a Salesforce IoT Cloud Input Stream.

    - **token** *(string) --*

      The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The
      token is available from the Salesforce IoT Cloud platform after creation of the Input
      Stream.

    - **url** *(string) --*

      The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the
      Salesforce IoT Cloud platform after creation of the Input Stream.
    """


_ClientGetTopicRuleResponseruleerrorActionsnsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionsnsTypeDef",
    {"targetArn": str, "roleArn": str, "messageFormat": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionsnsTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionsnsTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleerrorAction` `sns`

    Publish to an Amazon SNS topic.

    - **targetArn** *(string) --*

      The ARN of the SNS topic.

    - **roleArn** *(string) --*

      The ARN of the IAM role that grants access.

    - **messageFormat** *(string) --*

      (Optional) The message format of the message to publish. Accepted values are "JSON" and
      "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine
      if the payload should be parsed and relevant platform-specific bits of the payload
      should be extracted. To read more about SNS message formats, see
      `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
      <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their
      official documentation.
    """


_ClientGetTopicRuleResponseruleerrorActionsqsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionsqsTypeDef",
    {"roleArn": str, "queueUrl": str, "useBase64": bool},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionsqsTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionsqsTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleerrorAction` `sqs`

    Publish to an Amazon SQS queue.

    - **roleArn** *(string) --*

      The ARN of the IAM role that grants access.

    - **queueUrl** *(string) --*

      The URL of the Amazon SQS queue.

    - **useBase64** *(boolean) --*

      Specifies whether to use Base64 encoding.
    """


_ClientGetTopicRuleResponseruleerrorActionstepFunctionsTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionstepFunctionsTypeDef",
    {"executionNamePrefix": str, "stateMachineName": str, "roleArn": str},
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionstepFunctionsTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionstepFunctionsTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponseruleerrorAction` `stepFunctions`

    Starts execution of a Step Functions state machine.

    - **executionNamePrefix** *(string) --*

      (Optional) A name will be given to the state machine execution consisting of this
      prefix followed by a UUID. Step Functions automatically creates a unique name for each
      state machine execution if one is not provided.

    - **stateMachineName** *(string) --*

      The name of the Step Functions state machine whose execution will be started.

    - **roleArn** *(string) --*

      The ARN of the role that grants IoT permission to start execution of a state machine
      ("Action":"states:StartExecution").
    """


_ClientGetTopicRuleResponseruleerrorActionTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleerrorActionTypeDef",
    {
        "dynamoDB": ClientGetTopicRuleResponseruleerrorActiondynamoDBTypeDef,
        "dynamoDBv2": ClientGetTopicRuleResponseruleerrorActiondynamoDBv2TypeDef,
        "lambda": ClientGetTopicRuleResponseruleerrorActionlambdaTypeDef,
        "sns": ClientGetTopicRuleResponseruleerrorActionsnsTypeDef,
        "sqs": ClientGetTopicRuleResponseruleerrorActionsqsTypeDef,
        "kinesis": ClientGetTopicRuleResponseruleerrorActionkinesisTypeDef,
        "republish": ClientGetTopicRuleResponseruleerrorActionrepublishTypeDef,
        "s3": ClientGetTopicRuleResponseruleerrorActions3TypeDef,
        "firehose": ClientGetTopicRuleResponseruleerrorActionfirehoseTypeDef,
        "cloudwatchMetric": ClientGetTopicRuleResponseruleerrorActioncloudwatchMetricTypeDef,
        "cloudwatchAlarm": ClientGetTopicRuleResponseruleerrorActioncloudwatchAlarmTypeDef,
        "elasticsearch": ClientGetTopicRuleResponseruleerrorActionelasticsearchTypeDef,
        "salesforce": ClientGetTopicRuleResponseruleerrorActionsalesforceTypeDef,
        "iotAnalytics": ClientGetTopicRuleResponseruleerrorActioniotAnalyticsTypeDef,
        "iotEvents": ClientGetTopicRuleResponseruleerrorActioniotEventsTypeDef,
        "stepFunctions": ClientGetTopicRuleResponseruleerrorActionstepFunctionsTypeDef,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleerrorActionTypeDef(
    _ClientGetTopicRuleResponseruleerrorActionTypeDef
):
    """
    Type definition for `ClientGetTopicRuleResponserule` `errorAction`

    The action to perform when an error occurs.

    - **dynamoDB** *(dict) --*

      Write to a DynamoDB table.

      - **tableName** *(string) --*

        The name of the DynamoDB table.

      - **roleArn** *(string) --*

        The ARN of the IAM role that grants access to the DynamoDB table.

      - **operation** *(string) --*

        The type of operation to be performed. This follows the substitution template, so it
        can be ``${operation}`` , but the substitution must result in one of the following:
        ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

      - **hashKeyField** *(string) --*

        The hash key name.

      - **hashKeyValue** *(string) --*

        The hash key value.

      - **hashKeyType** *(string) --*

        The hash key type. Valid values are "STRING" or "NUMBER"

      - **rangeKeyField** *(string) --*

        The range key name.

      - **rangeKeyValue** *(string) --*

        The range key value.

      - **rangeKeyType** *(string) --*

        The range key type. Valid values are "STRING" or "NUMBER"

      - **payloadField** *(string) --*

        The action payload. This name can be customized.

    - **dynamoDBv2** *(dict) --*

      Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to
      write each attribute in an MQTT message payload into a separate DynamoDB column.

      - **roleArn** *(string) --*

        The ARN of the IAM role that grants access to the DynamoDB table.

      - **putItem** *(dict) --*

        Specifies the DynamoDB table to which the message data will be written. For example:

         ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
         "my-table" } } }``

        Each attribute in the message payload will be written to a separate column in the
        DynamoDB database.

        - **tableName** *(string) --*

          The table where the message data will be written.

    - **lambda** *(dict) --*

      Invoke a Lambda function.

      - **functionArn** *(string) --*

        The ARN of the Lambda function.

    - **sns** *(dict) --*

      Publish to an Amazon SNS topic.

      - **targetArn** *(string) --*

        The ARN of the SNS topic.

      - **roleArn** *(string) --*

        The ARN of the IAM role that grants access.

      - **messageFormat** *(string) --*

        (Optional) The message format of the message to publish. Accepted values are "JSON" and
        "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine
        if the payload should be parsed and relevant platform-specific bits of the payload
        should be extracted. To read more about SNS message formats, see
        `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
        <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their
        official documentation.

    - **sqs** *(dict) --*

      Publish to an Amazon SQS queue.

      - **roleArn** *(string) --*

        The ARN of the IAM role that grants access.

      - **queueUrl** *(string) --*

        The URL of the Amazon SQS queue.

      - **useBase64** *(boolean) --*

        Specifies whether to use Base64 encoding.

    - **kinesis** *(dict) --*

      Write data to an Amazon Kinesis stream.

      - **roleArn** *(string) --*

        The ARN of the IAM role that grants access to the Amazon Kinesis stream.

      - **streamName** *(string) --*

        The name of the Amazon Kinesis stream.

      - **partitionKey** *(string) --*

        The partition key.

    - **republish** *(dict) --*

      Publish to another MQTT topic.

      - **roleArn** *(string) --*

        The ARN of the IAM role that grants access.

      - **topic** *(string) --*

        The name of the MQTT topic.

      - **qos** *(integer) --*

        The Quality of Service (QoS) level to use when republishing messages. The default value
        is 0.

    - **s3** *(dict) --*

      Write to an Amazon S3 bucket.

      - **roleArn** *(string) --*

        The ARN of the IAM role that grants access.

      - **bucketName** *(string) --*

        The Amazon S3 bucket.

      - **key** *(string) --*

        The object key.

      - **cannedAcl** *(string) --*

        The Amazon S3 canned ACL that controls access to the object identified by the object
        key. For more information, see `S3 canned ACLs
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

    - **firehose** *(dict) --*

      Write to an Amazon Kinesis Firehose stream.

      - **roleArn** *(string) --*

        The IAM role that grants access to the Amazon Kinesis Firehose stream.

      - **deliveryStreamName** *(string) --*

        The delivery stream name.

      - **separator** *(string) --*

        A character separator that will be used to separate records written to the Firehose
        stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ','
        (comma).

    - **cloudwatchMetric** *(dict) --*

      Capture a CloudWatch metric.

      - **roleArn** *(string) --*

        The IAM role that allows access to the CloudWatch metric.

      - **metricNamespace** *(string) --*

        The CloudWatch metric namespace name.

      - **metricName** *(string) --*

        The CloudWatch metric name.

      - **metricValue** *(string) --*

        The CloudWatch metric value.

      - **metricUnit** *(string) --*

        The `metric unit
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
        supported by CloudWatch.

      - **metricTimestamp** *(string) --*

        An optional `Unix timestamp
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
        .

    - **cloudwatchAlarm** *(dict) --*

      Change the state of a CloudWatch alarm.

      - **roleArn** *(string) --*

        The IAM role that allows access to the CloudWatch alarm.

      - **alarmName** *(string) --*

        The CloudWatch alarm name.

      - **stateReason** *(string) --*

        The reason for the alarm change.

      - **stateValue** *(string) --*

        The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

    - **elasticsearch** *(dict) --*

      Write data to an Amazon Elasticsearch Service domain.

      - **roleArn** *(string) --*

        The IAM role ARN that has access to Elasticsearch.

      - **endpoint** *(string) --*

        The endpoint of your Elasticsearch domain.

      - **index** *(string) --*

        The Elasticsearch index where you want to store your data.

      - **type** *(string) --*

        The type of document you are storing.

      - **id** *(string) --*

        The unique identifier for the document you are storing.

    - **salesforce** *(dict) --*

      Send a message to a Salesforce IoT Cloud Input Stream.

      - **token** *(string) --*

        The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The
        token is available from the Salesforce IoT Cloud platform after creation of the Input
        Stream.

      - **url** *(string) --*

        The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the
        Salesforce IoT Cloud platform after creation of the Input Stream.

    - **iotAnalytics** *(dict) --*

      Sends message data to an AWS IoT Analytics channel.

      - **channelArn** *(string) --*

        (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

      - **channelName** *(string) --*

        The name of the IoT Analytics channel to which message data will be sent.

      - **roleArn** *(string) --*

        The ARN of the role which has a policy that grants IoT Analytics permission to send
        message data via IoT Analytics (iotanalytics:BatchPutMessage).

    - **iotEvents** *(dict) --*

      Sends an input to an AWS IoT Events detector.

      - **inputName** *(string) --*

        The name of the AWS IoT Events input.

      - **messageId** *(string) --*

        [Optional] Use this to ensure that only one input (message) with a given messageId will
        be processed by an AWS IoT Events detector.

      - **roleArn** *(string) --*

        The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT
        Events detector. ("Action":"iotevents:BatchPutMessage").

    - **stepFunctions** *(dict) --*

      Starts execution of a Step Functions state machine.

      - **executionNamePrefix** *(string) --*

        (Optional) A name will be given to the state machine execution consisting of this
        prefix followed by a UUID. Step Functions automatically creates a unique name for each
        state machine execution if one is not provided.

      - **stateMachineName** *(string) --*

        The name of the Step Functions state machine whose execution will be started.

      - **roleArn** *(string) --*

        The ARN of the role that grants IoT permission to start execution of a state machine
        ("Action":"states:StartExecution").
    """


_ClientGetTopicRuleResponseruleTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseruleTypeDef",
    {
        "ruleName": str,
        "sql": str,
        "description": str,
        "createdAt": datetime,
        "actions": List[ClientGetTopicRuleResponseruleactionsTypeDef],
        "ruleDisabled": bool,
        "awsIotSqlVersion": str,
        "errorAction": ClientGetTopicRuleResponseruleerrorActionTypeDef,
    },
    total=False,
)


class ClientGetTopicRuleResponseruleTypeDef(_ClientGetTopicRuleResponseruleTypeDef):
    """
    Type definition for `ClientGetTopicRuleResponse` `rule`

    The rule.

    - **ruleName** *(string) --*

      The name of the rule.

    - **sql** *(string) --*

      The SQL statement used to query the topic. When using a SQL query with multiple lines, be
      sure to escape the newline characters.

    - **description** *(string) --*

      The description of the rule.

    - **createdAt** *(datetime) --*

      The date and time the rule was created.

    - **actions** *(list) --*

      The actions associated with the rule.

      - *(dict) --*

        Describes the actions associated with a rule.

        - **dynamoDB** *(dict) --*

          Write to a DynamoDB table.

          - **tableName** *(string) --*

            The name of the DynamoDB table.

          - **roleArn** *(string) --*

            The ARN of the IAM role that grants access to the DynamoDB table.

          - **operation** *(string) --*

            The type of operation to be performed. This follows the substitution template, so it
            can be ``${operation}`` , but the substitution must result in one of the following:
            ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

          - **hashKeyField** *(string) --*

            The hash key name.

          - **hashKeyValue** *(string) --*

            The hash key value.

          - **hashKeyType** *(string) --*

            The hash key type. Valid values are "STRING" or "NUMBER"

          - **rangeKeyField** *(string) --*

            The range key name.

          - **rangeKeyValue** *(string) --*

            The range key value.

          - **rangeKeyType** *(string) --*

            The range key type. Valid values are "STRING" or "NUMBER"

          - **payloadField** *(string) --*

            The action payload. This name can be customized.

        - **dynamoDBv2** *(dict) --*

          Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you
          to write each attribute in an MQTT message payload into a separate DynamoDB column.

          - **roleArn** *(string) --*

            The ARN of the IAM role that grants access to the DynamoDB table.

          - **putItem** *(dict) --*

            Specifies the DynamoDB table to which the message data will be written. For example:

             ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
             "my-table" } } }``

            Each attribute in the message payload will be written to a separate column in the
            DynamoDB database.

            - **tableName** *(string) --*

              The table where the message data will be written.

        - **lambda** *(dict) --*

          Invoke a Lambda function.

          - **functionArn** *(string) --*

            The ARN of the Lambda function.

        - **sns** *(dict) --*

          Publish to an Amazon SNS topic.

          - **targetArn** *(string) --*

            The ARN of the SNS topic.

          - **roleArn** *(string) --*

            The ARN of the IAM role that grants access.

          - **messageFormat** *(string) --*

            (Optional) The message format of the message to publish. Accepted values are "JSON"
            and "RAW". The default value of the attribute is "RAW". SNS uses this setting to
            determine if the payload should be parsed and relevant platform-specific bits of the
            payload should be extracted. To read more about SNS message formats, see
            `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
            <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their
            official documentation.

        - **sqs** *(dict) --*

          Publish to an Amazon SQS queue.

          - **roleArn** *(string) --*

            The ARN of the IAM role that grants access.

          - **queueUrl** *(string) --*

            The URL of the Amazon SQS queue.

          - **useBase64** *(boolean) --*

            Specifies whether to use Base64 encoding.

        - **kinesis** *(dict) --*

          Write data to an Amazon Kinesis stream.

          - **roleArn** *(string) --*

            The ARN of the IAM role that grants access to the Amazon Kinesis stream.

          - **streamName** *(string) --*

            The name of the Amazon Kinesis stream.

          - **partitionKey** *(string) --*

            The partition key.

        - **republish** *(dict) --*

          Publish to another MQTT topic.

          - **roleArn** *(string) --*

            The ARN of the IAM role that grants access.

          - **topic** *(string) --*

            The name of the MQTT topic.

          - **qos** *(integer) --*

            The Quality of Service (QoS) level to use when republishing messages. The default
            value is 0.

        - **s3** *(dict) --*

          Write to an Amazon S3 bucket.

          - **roleArn** *(string) --*

            The ARN of the IAM role that grants access.

          - **bucketName** *(string) --*

            The Amazon S3 bucket.

          - **key** *(string) --*

            The object key.

          - **cannedAcl** *(string) --*

            The Amazon S3 canned ACL that controls access to the object identified by the object
            key. For more information, see `S3 canned ACLs
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

        - **firehose** *(dict) --*

          Write to an Amazon Kinesis Firehose stream.

          - **roleArn** *(string) --*

            The IAM role that grants access to the Amazon Kinesis Firehose stream.

          - **deliveryStreamName** *(string) --*

            The delivery stream name.

          - **separator** *(string) --*

            A character separator that will be used to separate records written to the Firehose
            stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline),
            ',' (comma).

        - **cloudwatchMetric** *(dict) --*

          Capture a CloudWatch metric.

          - **roleArn** *(string) --*

            The IAM role that allows access to the CloudWatch metric.

          - **metricNamespace** *(string) --*

            The CloudWatch metric namespace name.

          - **metricName** *(string) --*

            The CloudWatch metric name.

          - **metricValue** *(string) --*

            The CloudWatch metric value.

          - **metricUnit** *(string) --*

            The `metric unit
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
            supported by CloudWatch.

          - **metricTimestamp** *(string) --*

            An optional `Unix timestamp
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
            .

        - **cloudwatchAlarm** *(dict) --*

          Change the state of a CloudWatch alarm.

          - **roleArn** *(string) --*

            The IAM role that allows access to the CloudWatch alarm.

          - **alarmName** *(string) --*

            The CloudWatch alarm name.

          - **stateReason** *(string) --*

            The reason for the alarm change.

          - **stateValue** *(string) --*

            The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

        - **elasticsearch** *(dict) --*

          Write data to an Amazon Elasticsearch Service domain.

          - **roleArn** *(string) --*

            The IAM role ARN that has access to Elasticsearch.

          - **endpoint** *(string) --*

            The endpoint of your Elasticsearch domain.

          - **index** *(string) --*

            The Elasticsearch index where you want to store your data.

          - **type** *(string) --*

            The type of document you are storing.

          - **id** *(string) --*

            The unique identifier for the document you are storing.

        - **salesforce** *(dict) --*

          Send a message to a Salesforce IoT Cloud Input Stream.

          - **token** *(string) --*

            The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The
            token is available from the Salesforce IoT Cloud platform after creation of the Input
            Stream.

          - **url** *(string) --*

            The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from
            the Salesforce IoT Cloud platform after creation of the Input Stream.

        - **iotAnalytics** *(dict) --*

          Sends message data to an AWS IoT Analytics channel.

          - **channelArn** *(string) --*

            (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

          - **channelName** *(string) --*

            The name of the IoT Analytics channel to which message data will be sent.

          - **roleArn** *(string) --*

            The ARN of the role which has a policy that grants IoT Analytics permission to send
            message data via IoT Analytics (iotanalytics:BatchPutMessage).

        - **iotEvents** *(dict) --*

          Sends an input to an AWS IoT Events detector.

          - **inputName** *(string) --*

            The name of the AWS IoT Events input.

          - **messageId** *(string) --*

            [Optional] Use this to ensure that only one input (message) with a given messageId
            will be processed by an AWS IoT Events detector.

          - **roleArn** *(string) --*

            The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT
            Events detector. ("Action":"iotevents:BatchPutMessage").

        - **stepFunctions** *(dict) --*

          Starts execution of a Step Functions state machine.

          - **executionNamePrefix** *(string) --*

            (Optional) A name will be given to the state machine execution consisting of this
            prefix followed by a UUID. Step Functions automatically creates a unique name for
            each state machine execution if one is not provided.

          - **stateMachineName** *(string) --*

            The name of the Step Functions state machine whose execution will be started.

          - **roleArn** *(string) --*

            The ARN of the role that grants IoT permission to start execution of a state machine
            ("Action":"states:StartExecution").

    - **ruleDisabled** *(boolean) --*

      Specifies whether the rule is disabled.

    - **awsIotSqlVersion** *(string) --*

      The version of the SQL rules engine to use when evaluating the rule.

    - **errorAction** *(dict) --*

      The action to perform when an error occurs.

      - **dynamoDB** *(dict) --*

        Write to a DynamoDB table.

        - **tableName** *(string) --*

          The name of the DynamoDB table.

        - **roleArn** *(string) --*

          The ARN of the IAM role that grants access to the DynamoDB table.

        - **operation** *(string) --*

          The type of operation to be performed. This follows the substitution template, so it
          can be ``${operation}`` , but the substitution must result in one of the following:
          ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

        - **hashKeyField** *(string) --*

          The hash key name.

        - **hashKeyValue** *(string) --*

          The hash key value.

        - **hashKeyType** *(string) --*

          The hash key type. Valid values are "STRING" or "NUMBER"

        - **rangeKeyField** *(string) --*

          The range key name.

        - **rangeKeyValue** *(string) --*

          The range key value.

        - **rangeKeyType** *(string) --*

          The range key type. Valid values are "STRING" or "NUMBER"

        - **payloadField** *(string) --*

          The action payload. This name can be customized.

      - **dynamoDBv2** *(dict) --*

        Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to
        write each attribute in an MQTT message payload into a separate DynamoDB column.

        - **roleArn** *(string) --*

          The ARN of the IAM role that grants access to the DynamoDB table.

        - **putItem** *(dict) --*

          Specifies the DynamoDB table to which the message data will be written. For example:

           ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
           "my-table" } } }``

          Each attribute in the message payload will be written to a separate column in the
          DynamoDB database.

          - **tableName** *(string) --*

            The table where the message data will be written.

      - **lambda** *(dict) --*

        Invoke a Lambda function.

        - **functionArn** *(string) --*

          The ARN of the Lambda function.

      - **sns** *(dict) --*

        Publish to an Amazon SNS topic.

        - **targetArn** *(string) --*

          The ARN of the SNS topic.

        - **roleArn** *(string) --*

          The ARN of the IAM role that grants access.

        - **messageFormat** *(string) --*

          (Optional) The message format of the message to publish. Accepted values are "JSON" and
          "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine
          if the payload should be parsed and relevant platform-specific bits of the payload
          should be extracted. To read more about SNS message formats, see
          `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
          <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their
          official documentation.

      - **sqs** *(dict) --*

        Publish to an Amazon SQS queue.

        - **roleArn** *(string) --*

          The ARN of the IAM role that grants access.

        - **queueUrl** *(string) --*

          The URL of the Amazon SQS queue.

        - **useBase64** *(boolean) --*

          Specifies whether to use Base64 encoding.

      - **kinesis** *(dict) --*

        Write data to an Amazon Kinesis stream.

        - **roleArn** *(string) --*

          The ARN of the IAM role that grants access to the Amazon Kinesis stream.

        - **streamName** *(string) --*

          The name of the Amazon Kinesis stream.

        - **partitionKey** *(string) --*

          The partition key.

      - **republish** *(dict) --*

        Publish to another MQTT topic.

        - **roleArn** *(string) --*

          The ARN of the IAM role that grants access.

        - **topic** *(string) --*

          The name of the MQTT topic.

        - **qos** *(integer) --*

          The Quality of Service (QoS) level to use when republishing messages. The default value
          is 0.

      - **s3** *(dict) --*

        Write to an Amazon S3 bucket.

        - **roleArn** *(string) --*

          The ARN of the IAM role that grants access.

        - **bucketName** *(string) --*

          The Amazon S3 bucket.

        - **key** *(string) --*

          The object key.

        - **cannedAcl** *(string) --*

          The Amazon S3 canned ACL that controls access to the object identified by the object
          key. For more information, see `S3 canned ACLs
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

      - **firehose** *(dict) --*

        Write to an Amazon Kinesis Firehose stream.

        - **roleArn** *(string) --*

          The IAM role that grants access to the Amazon Kinesis Firehose stream.

        - **deliveryStreamName** *(string) --*

          The delivery stream name.

        - **separator** *(string) --*

          A character separator that will be used to separate records written to the Firehose
          stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ','
          (comma).

      - **cloudwatchMetric** *(dict) --*

        Capture a CloudWatch metric.

        - **roleArn** *(string) --*

          The IAM role that allows access to the CloudWatch metric.

        - **metricNamespace** *(string) --*

          The CloudWatch metric namespace name.

        - **metricName** *(string) --*

          The CloudWatch metric name.

        - **metricValue** *(string) --*

          The CloudWatch metric value.

        - **metricUnit** *(string) --*

          The `metric unit
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
          supported by CloudWatch.

        - **metricTimestamp** *(string) --*

          An optional `Unix timestamp
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
          .

      - **cloudwatchAlarm** *(dict) --*

        Change the state of a CloudWatch alarm.

        - **roleArn** *(string) --*

          The IAM role that allows access to the CloudWatch alarm.

        - **alarmName** *(string) --*

          The CloudWatch alarm name.

        - **stateReason** *(string) --*

          The reason for the alarm change.

        - **stateValue** *(string) --*

          The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

      - **elasticsearch** *(dict) --*

        Write data to an Amazon Elasticsearch Service domain.

        - **roleArn** *(string) --*

          The IAM role ARN that has access to Elasticsearch.

        - **endpoint** *(string) --*

          The endpoint of your Elasticsearch domain.

        - **index** *(string) --*

          The Elasticsearch index where you want to store your data.

        - **type** *(string) --*

          The type of document you are storing.

        - **id** *(string) --*

          The unique identifier for the document you are storing.

      - **salesforce** *(dict) --*

        Send a message to a Salesforce IoT Cloud Input Stream.

        - **token** *(string) --*

          The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The
          token is available from the Salesforce IoT Cloud platform after creation of the Input
          Stream.

        - **url** *(string) --*

          The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the
          Salesforce IoT Cloud platform after creation of the Input Stream.

      - **iotAnalytics** *(dict) --*

        Sends message data to an AWS IoT Analytics channel.

        - **channelArn** *(string) --*

          (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

        - **channelName** *(string) --*

          The name of the IoT Analytics channel to which message data will be sent.

        - **roleArn** *(string) --*

          The ARN of the role which has a policy that grants IoT Analytics permission to send
          message data via IoT Analytics (iotanalytics:BatchPutMessage).

      - **iotEvents** *(dict) --*

        Sends an input to an AWS IoT Events detector.

        - **inputName** *(string) --*

          The name of the AWS IoT Events input.

        - **messageId** *(string) --*

          [Optional] Use this to ensure that only one input (message) with a given messageId will
          be processed by an AWS IoT Events detector.

        - **roleArn** *(string) --*

          The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT
          Events detector. ("Action":"iotevents:BatchPutMessage").

      - **stepFunctions** *(dict) --*

        Starts execution of a Step Functions state machine.

        - **executionNamePrefix** *(string) --*

          (Optional) A name will be given to the state machine execution consisting of this
          prefix followed by a UUID. Step Functions automatically creates a unique name for each
          state machine execution if one is not provided.

        - **stateMachineName** *(string) --*

          The name of the Step Functions state machine whose execution will be started.

        - **roleArn** *(string) --*

          The ARN of the role that grants IoT permission to start execution of a state machine
          ("Action":"states:StartExecution").
    """


_ClientGetTopicRuleResponseTypeDef = TypedDict(
    "_ClientGetTopicRuleResponseTypeDef",
    {"ruleArn": str, "rule": ClientGetTopicRuleResponseruleTypeDef},
    total=False,
)


class ClientGetTopicRuleResponseTypeDef(_ClientGetTopicRuleResponseTypeDef):
    """
    Type definition for `ClientGetTopicRule` `Response`

    The output from the GetTopicRule operation.

    - **ruleArn** *(string) --*

      The rule ARN.

    - **rule** *(dict) --*

      The rule.

      - **ruleName** *(string) --*

        The name of the rule.

      - **sql** *(string) --*

        The SQL statement used to query the topic. When using a SQL query with multiple lines, be
        sure to escape the newline characters.

      - **description** *(string) --*

        The description of the rule.

      - **createdAt** *(datetime) --*

        The date and time the rule was created.

      - **actions** *(list) --*

        The actions associated with the rule.

        - *(dict) --*

          Describes the actions associated with a rule.

          - **dynamoDB** *(dict) --*

            Write to a DynamoDB table.

            - **tableName** *(string) --*

              The name of the DynamoDB table.

            - **roleArn** *(string) --*

              The ARN of the IAM role that grants access to the DynamoDB table.

            - **operation** *(string) --*

              The type of operation to be performed. This follows the substitution template, so it
              can be ``${operation}`` , but the substitution must result in one of the following:
              ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

            - **hashKeyField** *(string) --*

              The hash key name.

            - **hashKeyValue** *(string) --*

              The hash key value.

            - **hashKeyType** *(string) --*

              The hash key type. Valid values are "STRING" or "NUMBER"

            - **rangeKeyField** *(string) --*

              The range key name.

            - **rangeKeyValue** *(string) --*

              The range key value.

            - **rangeKeyType** *(string) --*

              The range key type. Valid values are "STRING" or "NUMBER"

            - **payloadField** *(string) --*

              The action payload. This name can be customized.

          - **dynamoDBv2** *(dict) --*

            Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you
            to write each attribute in an MQTT message payload into a separate DynamoDB column.

            - **roleArn** *(string) --*

              The ARN of the IAM role that grants access to the DynamoDB table.

            - **putItem** *(dict) --*

              Specifies the DynamoDB table to which the message data will be written. For example:

               ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
               "my-table" } } }``

              Each attribute in the message payload will be written to a separate column in the
              DynamoDB database.

              - **tableName** *(string) --*

                The table where the message data will be written.

          - **lambda** *(dict) --*

            Invoke a Lambda function.

            - **functionArn** *(string) --*

              The ARN of the Lambda function.

          - **sns** *(dict) --*

            Publish to an Amazon SNS topic.

            - **targetArn** *(string) --*

              The ARN of the SNS topic.

            - **roleArn** *(string) --*

              The ARN of the IAM role that grants access.

            - **messageFormat** *(string) --*

              (Optional) The message format of the message to publish. Accepted values are "JSON"
              and "RAW". The default value of the attribute is "RAW". SNS uses this setting to
              determine if the payload should be parsed and relevant platform-specific bits of the
              payload should be extracted. To read more about SNS message formats, see
              `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
              <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their
              official documentation.

          - **sqs** *(dict) --*

            Publish to an Amazon SQS queue.

            - **roleArn** *(string) --*

              The ARN of the IAM role that grants access.

            - **queueUrl** *(string) --*

              The URL of the Amazon SQS queue.

            - **useBase64** *(boolean) --*

              Specifies whether to use Base64 encoding.

          - **kinesis** *(dict) --*

            Write data to an Amazon Kinesis stream.

            - **roleArn** *(string) --*

              The ARN of the IAM role that grants access to the Amazon Kinesis stream.

            - **streamName** *(string) --*

              The name of the Amazon Kinesis stream.

            - **partitionKey** *(string) --*

              The partition key.

          - **republish** *(dict) --*

            Publish to another MQTT topic.

            - **roleArn** *(string) --*

              The ARN of the IAM role that grants access.

            - **topic** *(string) --*

              The name of the MQTT topic.

            - **qos** *(integer) --*

              The Quality of Service (QoS) level to use when republishing messages. The default
              value is 0.

          - **s3** *(dict) --*

            Write to an Amazon S3 bucket.

            - **roleArn** *(string) --*

              The ARN of the IAM role that grants access.

            - **bucketName** *(string) --*

              The Amazon S3 bucket.

            - **key** *(string) --*

              The object key.

            - **cannedAcl** *(string) --*

              The Amazon S3 canned ACL that controls access to the object identified by the object
              key. For more information, see `S3 canned ACLs
              <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

          - **firehose** *(dict) --*

            Write to an Amazon Kinesis Firehose stream.

            - **roleArn** *(string) --*

              The IAM role that grants access to the Amazon Kinesis Firehose stream.

            - **deliveryStreamName** *(string) --*

              The delivery stream name.

            - **separator** *(string) --*

              A character separator that will be used to separate records written to the Firehose
              stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline),
              ',' (comma).

          - **cloudwatchMetric** *(dict) --*

            Capture a CloudWatch metric.

            - **roleArn** *(string) --*

              The IAM role that allows access to the CloudWatch metric.

            - **metricNamespace** *(string) --*

              The CloudWatch metric namespace name.

            - **metricName** *(string) --*

              The CloudWatch metric name.

            - **metricValue** *(string) --*

              The CloudWatch metric value.

            - **metricUnit** *(string) --*

              The `metric unit
              <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
              supported by CloudWatch.

            - **metricTimestamp** *(string) --*

              An optional `Unix timestamp
              <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
              .

          - **cloudwatchAlarm** *(dict) --*

            Change the state of a CloudWatch alarm.

            - **roleArn** *(string) --*

              The IAM role that allows access to the CloudWatch alarm.

            - **alarmName** *(string) --*

              The CloudWatch alarm name.

            - **stateReason** *(string) --*

              The reason for the alarm change.

            - **stateValue** *(string) --*

              The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

          - **elasticsearch** *(dict) --*

            Write data to an Amazon Elasticsearch Service domain.

            - **roleArn** *(string) --*

              The IAM role ARN that has access to Elasticsearch.

            - **endpoint** *(string) --*

              The endpoint of your Elasticsearch domain.

            - **index** *(string) --*

              The Elasticsearch index where you want to store your data.

            - **type** *(string) --*

              The type of document you are storing.

            - **id** *(string) --*

              The unique identifier for the document you are storing.

          - **salesforce** *(dict) --*

            Send a message to a Salesforce IoT Cloud Input Stream.

            - **token** *(string) --*

              The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The
              token is available from the Salesforce IoT Cloud platform after creation of the Input
              Stream.

            - **url** *(string) --*

              The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from
              the Salesforce IoT Cloud platform after creation of the Input Stream.

          - **iotAnalytics** *(dict) --*

            Sends message data to an AWS IoT Analytics channel.

            - **channelArn** *(string) --*

              (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

            - **channelName** *(string) --*

              The name of the IoT Analytics channel to which message data will be sent.

            - **roleArn** *(string) --*

              The ARN of the role which has a policy that grants IoT Analytics permission to send
              message data via IoT Analytics (iotanalytics:BatchPutMessage).

          - **iotEvents** *(dict) --*

            Sends an input to an AWS IoT Events detector.

            - **inputName** *(string) --*

              The name of the AWS IoT Events input.

            - **messageId** *(string) --*

              [Optional] Use this to ensure that only one input (message) with a given messageId
              will be processed by an AWS IoT Events detector.

            - **roleArn** *(string) --*

              The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT
              Events detector. ("Action":"iotevents:BatchPutMessage").

          - **stepFunctions** *(dict) --*

            Starts execution of a Step Functions state machine.

            - **executionNamePrefix** *(string) --*

              (Optional) A name will be given to the state machine execution consisting of this
              prefix followed by a UUID. Step Functions automatically creates a unique name for
              each state machine execution if one is not provided.

            - **stateMachineName** *(string) --*

              The name of the Step Functions state machine whose execution will be started.

            - **roleArn** *(string) --*

              The ARN of the role that grants IoT permission to start execution of a state machine
              ("Action":"states:StartExecution").

      - **ruleDisabled** *(boolean) --*

        Specifies whether the rule is disabled.

      - **awsIotSqlVersion** *(string) --*

        The version of the SQL rules engine to use when evaluating the rule.

      - **errorAction** *(dict) --*

        The action to perform when an error occurs.

        - **dynamoDB** *(dict) --*

          Write to a DynamoDB table.

          - **tableName** *(string) --*

            The name of the DynamoDB table.

          - **roleArn** *(string) --*

            The ARN of the IAM role that grants access to the DynamoDB table.

          - **operation** *(string) --*

            The type of operation to be performed. This follows the substitution template, so it
            can be ``${operation}`` , but the substitution must result in one of the following:
            ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

          - **hashKeyField** *(string) --*

            The hash key name.

          - **hashKeyValue** *(string) --*

            The hash key value.

          - **hashKeyType** *(string) --*

            The hash key type. Valid values are "STRING" or "NUMBER"

          - **rangeKeyField** *(string) --*

            The range key name.

          - **rangeKeyValue** *(string) --*

            The range key value.

          - **rangeKeyType** *(string) --*

            The range key type. Valid values are "STRING" or "NUMBER"

          - **payloadField** *(string) --*

            The action payload. This name can be customized.

        - **dynamoDBv2** *(dict) --*

          Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to
          write each attribute in an MQTT message payload into a separate DynamoDB column.

          - **roleArn** *(string) --*

            The ARN of the IAM role that grants access to the DynamoDB table.

          - **putItem** *(dict) --*

            Specifies the DynamoDB table to which the message data will be written. For example:

             ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
             "my-table" } } }``

            Each attribute in the message payload will be written to a separate column in the
            DynamoDB database.

            - **tableName** *(string) --*

              The table where the message data will be written.

        - **lambda** *(dict) --*

          Invoke a Lambda function.

          - **functionArn** *(string) --*

            The ARN of the Lambda function.

        - **sns** *(dict) --*

          Publish to an Amazon SNS topic.

          - **targetArn** *(string) --*

            The ARN of the SNS topic.

          - **roleArn** *(string) --*

            The ARN of the IAM role that grants access.

          - **messageFormat** *(string) --*

            (Optional) The message format of the message to publish. Accepted values are "JSON" and
            "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine
            if the payload should be parsed and relevant platform-specific bits of the payload
            should be extracted. To read more about SNS message formats, see
            `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
            <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their
            official documentation.

        - **sqs** *(dict) --*

          Publish to an Amazon SQS queue.

          - **roleArn** *(string) --*

            The ARN of the IAM role that grants access.

          - **queueUrl** *(string) --*

            The URL of the Amazon SQS queue.

          - **useBase64** *(boolean) --*

            Specifies whether to use Base64 encoding.

        - **kinesis** *(dict) --*

          Write data to an Amazon Kinesis stream.

          - **roleArn** *(string) --*

            The ARN of the IAM role that grants access to the Amazon Kinesis stream.

          - **streamName** *(string) --*

            The name of the Amazon Kinesis stream.

          - **partitionKey** *(string) --*

            The partition key.

        - **republish** *(dict) --*

          Publish to another MQTT topic.

          - **roleArn** *(string) --*

            The ARN of the IAM role that grants access.

          - **topic** *(string) --*

            The name of the MQTT topic.

          - **qos** *(integer) --*

            The Quality of Service (QoS) level to use when republishing messages. The default value
            is 0.

        - **s3** *(dict) --*

          Write to an Amazon S3 bucket.

          - **roleArn** *(string) --*

            The ARN of the IAM role that grants access.

          - **bucketName** *(string) --*

            The Amazon S3 bucket.

          - **key** *(string) --*

            The object key.

          - **cannedAcl** *(string) --*

            The Amazon S3 canned ACL that controls access to the object identified by the object
            key. For more information, see `S3 canned ACLs
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

        - **firehose** *(dict) --*

          Write to an Amazon Kinesis Firehose stream.

          - **roleArn** *(string) --*

            The IAM role that grants access to the Amazon Kinesis Firehose stream.

          - **deliveryStreamName** *(string) --*

            The delivery stream name.

          - **separator** *(string) --*

            A character separator that will be used to separate records written to the Firehose
            stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ','
            (comma).

        - **cloudwatchMetric** *(dict) --*

          Capture a CloudWatch metric.

          - **roleArn** *(string) --*

            The IAM role that allows access to the CloudWatch metric.

          - **metricNamespace** *(string) --*

            The CloudWatch metric namespace name.

          - **metricName** *(string) --*

            The CloudWatch metric name.

          - **metricValue** *(string) --*

            The CloudWatch metric value.

          - **metricUnit** *(string) --*

            The `metric unit
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
            supported by CloudWatch.

          - **metricTimestamp** *(string) --*

            An optional `Unix timestamp
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
            .

        - **cloudwatchAlarm** *(dict) --*

          Change the state of a CloudWatch alarm.

          - **roleArn** *(string) --*

            The IAM role that allows access to the CloudWatch alarm.

          - **alarmName** *(string) --*

            The CloudWatch alarm name.

          - **stateReason** *(string) --*

            The reason for the alarm change.

          - **stateValue** *(string) --*

            The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

        - **elasticsearch** *(dict) --*

          Write data to an Amazon Elasticsearch Service domain.

          - **roleArn** *(string) --*

            The IAM role ARN that has access to Elasticsearch.

          - **endpoint** *(string) --*

            The endpoint of your Elasticsearch domain.

          - **index** *(string) --*

            The Elasticsearch index where you want to store your data.

          - **type** *(string) --*

            The type of document you are storing.

          - **id** *(string) --*

            The unique identifier for the document you are storing.

        - **salesforce** *(dict) --*

          Send a message to a Salesforce IoT Cloud Input Stream.

          - **token** *(string) --*

            The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The
            token is available from the Salesforce IoT Cloud platform after creation of the Input
            Stream.

          - **url** *(string) --*

            The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the
            Salesforce IoT Cloud platform after creation of the Input Stream.

        - **iotAnalytics** *(dict) --*

          Sends message data to an AWS IoT Analytics channel.

          - **channelArn** *(string) --*

            (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

          - **channelName** *(string) --*

            The name of the IoT Analytics channel to which message data will be sent.

          - **roleArn** *(string) --*

            The ARN of the role which has a policy that grants IoT Analytics permission to send
            message data via IoT Analytics (iotanalytics:BatchPutMessage).

        - **iotEvents** *(dict) --*

          Sends an input to an AWS IoT Events detector.

          - **inputName** *(string) --*

            The name of the AWS IoT Events input.

          - **messageId** *(string) --*

            [Optional] Use this to ensure that only one input (message) with a given messageId will
            be processed by an AWS IoT Events detector.

          - **roleArn** *(string) --*

            The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT
            Events detector. ("Action":"iotevents:BatchPutMessage").

        - **stepFunctions** *(dict) --*

          Starts execution of a Step Functions state machine.

          - **executionNamePrefix** *(string) --*

            (Optional) A name will be given to the state machine execution consisting of this
            prefix followed by a UUID. Step Functions automatically creates a unique name for each
            state machine execution if one is not provided.

          - **stateMachineName** *(string) --*

            The name of the Step Functions state machine whose execution will be started.

          - **roleArn** *(string) --*

            The ARN of the role that grants IoT permission to start execution of a state machine
            ("Action":"states:StartExecution").
    """


_ClientGetV2LoggingOptionsResponseTypeDef = TypedDict(
    "_ClientGetV2LoggingOptionsResponseTypeDef",
    {"roleArn": str, "defaultLogLevel": str, "disableAllLogs": bool},
    total=False,
)


class ClientGetV2LoggingOptionsResponseTypeDef(
    _ClientGetV2LoggingOptionsResponseTypeDef
):
    """
    Type definition for `ClientGetV2LoggingOptions` `Response`

    - **roleArn** *(string) --*

      The IAM role ARN AWS IoT uses to write to your CloudWatch logs.

    - **defaultLogLevel** *(string) --*

      The default log level.

    - **disableAllLogs** *(boolean) --*

      Disables all logs.
    """


_ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef = TypedDict(
    "_ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)


class ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef(
    _ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef
):
    """
    Type definition for `ClientListActiveViolationsResponseactiveViolationsbehaviorcriteria` `statisticalThreshold`

    A statistical ranking (percentile) which indicates a threshold value by which a
    behavior is determined to be in compliance or in violation of the behavior.

    - **statistic** *(string) --*

      The percentile which resolves to a threshold value by which compliance with a
      behavior is determined. Metrics are collected over the specified period
      (``durationSeconds`` ) from all reporting devices in your account and statistical
      ranks are calculated. Then, the measurements from a device are collected over the
      same period. If the accumulated measurements from the device fall above or below
      (``comparisonOperator`` ) the value associated with the percentile specified, then
      the device is considered to be in compliance with the behavior, otherwise a
      violation occurs.
    """


_ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriavalueTypeDef = TypedDict(
    "_ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriavalueTypeDef(
    _ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriavalueTypeDef
):
    """
    Type definition for `ClientListActiveViolationsResponseactiveViolationsbehaviorcriteria` `value`

    The value to be compared with the ``metric`` .

    - **count** *(integer) --*

      If the ``comparisonOperator`` calls for a numeric value, use this to specify that
      numeric value to be compared with the ``metric`` .

    - **cidrs** *(list) --*

      If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
      set to be compared with the ``metric`` .

      - *(string) --*

    - **ports** *(list) --*

      If the ``comparisonOperator`` calls for a set of ports, use this to specify that
      set to be compared with the ``metric`` .

      - *(integer) --*
    """


_ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriaTypeDef = TypedDict(
    "_ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriaTypeDef",
    {
        "comparisonOperator": str,
        "value": ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef,
    },
    total=False,
)


class ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriaTypeDef(
    _ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriaTypeDef
):
    """
    Type definition for `ClientListActiveViolationsResponseactiveViolationsbehavior` `criteria`

    The criteria that determine if a device is behaving normally in regard to the
    ``metric`` .

    - **comparisonOperator** *(string) --*

      The operator that relates the thing measured (``metric`` ) to the criteria
      (containing a ``value`` or ``statisticalThreshold`` ).

    - **value** *(dict) --*

      The value to be compared with the ``metric`` .

      - **count** *(integer) --*

        If the ``comparisonOperator`` calls for a numeric value, use this to specify that
        numeric value to be compared with the ``metric`` .

      - **cidrs** *(list) --*

        If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
        set to be compared with the ``metric`` .

        - *(string) --*

      - **ports** *(list) --*

        If the ``comparisonOperator`` calls for a set of ports, use this to specify that
        set to be compared with the ``metric`` .

        - *(integer) --*

    - **durationSeconds** *(integer) --*

      Use this to specify the time duration over which the behavior is evaluated, for those
      criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
      ``statisticalThreshhold`` metric comparison, measurements from all devices are
      accumulated over this time duration before being used to calculate percentiles, and
      later, measurements from an individual device are also accumulated over this time
      duration before being given a percentile rank.

    - **consecutiveDatapointsToAlarm** *(integer) --*

      If a device is in violation of the behavior for the specified number of consecutive
      datapoints, an alarm occurs. If not specified, the default is 1.

    - **consecutiveDatapointsToClear** *(integer) --*

      If an alarm has occurred and the offending device is no longer in violation of the
      behavior for the specified number of consecutive datapoints, the alarm is cleared. If
      not specified, the default is 1.

    - **statisticalThreshold** *(dict) --*

      A statistical ranking (percentile) which indicates a threshold value by which a
      behavior is determined to be in compliance or in violation of the behavior.

      - **statistic** *(string) --*

        The percentile which resolves to a threshold value by which compliance with a
        behavior is determined. Metrics are collected over the specified period
        (``durationSeconds`` ) from all reporting devices in your account and statistical
        ranks are calculated. Then, the measurements from a device are collected over the
        same period. If the accumulated measurements from the device fall above or below
        (``comparisonOperator`` ) the value associated with the percentile specified, then
        the device is considered to be in compliance with the behavior, otherwise a
        violation occurs.
    """


_ClientListActiveViolationsResponseactiveViolationsbehaviorTypeDef = TypedDict(
    "_ClientListActiveViolationsResponseactiveViolationsbehaviorTypeDef",
    {
        "name": str,
        "metric": str,
        "criteria": ClientListActiveViolationsResponseactiveViolationsbehaviorcriteriaTypeDef,
    },
    total=False,
)


class ClientListActiveViolationsResponseactiveViolationsbehaviorTypeDef(
    _ClientListActiveViolationsResponseactiveViolationsbehaviorTypeDef
):
    """
    Type definition for `ClientListActiveViolationsResponseactiveViolations` `behavior`

    The behavior which is being violated.

    - **name** *(string) --*

      The name you have given to the behavior.

    - **metric** *(string) --*

      What is measured by the behavior.

    - **criteria** *(dict) --*

      The criteria that determine if a device is behaving normally in regard to the
      ``metric`` .

      - **comparisonOperator** *(string) --*

        The operator that relates the thing measured (``metric`` ) to the criteria
        (containing a ``value`` or ``statisticalThreshold`` ).

      - **value** *(dict) --*

        The value to be compared with the ``metric`` .

        - **count** *(integer) --*

          If the ``comparisonOperator`` calls for a numeric value, use this to specify that
          numeric value to be compared with the ``metric`` .

        - **cidrs** *(list) --*

          If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
          set to be compared with the ``metric`` .

          - *(string) --*

        - **ports** *(list) --*

          If the ``comparisonOperator`` calls for a set of ports, use this to specify that
          set to be compared with the ``metric`` .

          - *(integer) --*

      - **durationSeconds** *(integer) --*

        Use this to specify the time duration over which the behavior is evaluated, for those
        criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
        ``statisticalThreshhold`` metric comparison, measurements from all devices are
        accumulated over this time duration before being used to calculate percentiles, and
        later, measurements from an individual device are also accumulated over this time
        duration before being given a percentile rank.

      - **consecutiveDatapointsToAlarm** *(integer) --*

        If a device is in violation of the behavior for the specified number of consecutive
        datapoints, an alarm occurs. If not specified, the default is 1.

      - **consecutiveDatapointsToClear** *(integer) --*

        If an alarm has occurred and the offending device is no longer in violation of the
        behavior for the specified number of consecutive datapoints, the alarm is cleared. If
        not specified, the default is 1.

      - **statisticalThreshold** *(dict) --*

        A statistical ranking (percentile) which indicates a threshold value by which a
        behavior is determined to be in compliance or in violation of the behavior.

        - **statistic** *(string) --*

          The percentile which resolves to a threshold value by which compliance with a
          behavior is determined. Metrics are collected over the specified period
          (``durationSeconds`` ) from all reporting devices in your account and statistical
          ranks are calculated. Then, the measurements from a device are collected over the
          same period. If the accumulated measurements from the device fall above or below
          (``comparisonOperator`` ) the value associated with the percentile specified, then
          the device is considered to be in compliance with the behavior, otherwise a
          violation occurs.
    """


_ClientListActiveViolationsResponseactiveViolationslastViolationValueTypeDef = TypedDict(
    "_ClientListActiveViolationsResponseactiveViolationslastViolationValueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ClientListActiveViolationsResponseactiveViolationslastViolationValueTypeDef(
    _ClientListActiveViolationsResponseactiveViolationslastViolationValueTypeDef
):
    """
    Type definition for `ClientListActiveViolationsResponseactiveViolations` `lastViolationValue`

    The value of the metric (the measurement) which caused the most recent violation.

    - **count** *(integer) --*

      If the ``comparisonOperator`` calls for a numeric value, use this to specify that
      numeric value to be compared with the ``metric`` .

    - **cidrs** *(list) --*

      If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
      be compared with the ``metric`` .

      - *(string) --*

    - **ports** *(list) --*

      If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
      be compared with the ``metric`` .

      - *(integer) --*
    """


_ClientListActiveViolationsResponseactiveViolationsTypeDef = TypedDict(
    "_ClientListActiveViolationsResponseactiveViolationsTypeDef",
    {
        "violationId": str,
        "thingName": str,
        "securityProfileName": str,
        "behavior": ClientListActiveViolationsResponseactiveViolationsbehaviorTypeDef,
        "lastViolationValue": ClientListActiveViolationsResponseactiveViolationslastViolationValueTypeDef,
        "lastViolationTime": datetime,
        "violationStartTime": datetime,
    },
    total=False,
)


class ClientListActiveViolationsResponseactiveViolationsTypeDef(
    _ClientListActiveViolationsResponseactiveViolationsTypeDef
):
    """
    Type definition for `ClientListActiveViolationsResponse` `activeViolations`

    Information about an active Device Defender security profile behavior violation.

    - **violationId** *(string) --*

      The ID of the active violation.

    - **thingName** *(string) --*

      The name of the thing responsible for the active violation.

    - **securityProfileName** *(string) --*

      The security profile whose behavior is in violation.

    - **behavior** *(dict) --*

      The behavior which is being violated.

      - **name** *(string) --*

        The name you have given to the behavior.

      - **metric** *(string) --*

        What is measured by the behavior.

      - **criteria** *(dict) --*

        The criteria that determine if a device is behaving normally in regard to the
        ``metric`` .

        - **comparisonOperator** *(string) --*

          The operator that relates the thing measured (``metric`` ) to the criteria
          (containing a ``value`` or ``statisticalThreshold`` ).

        - **value** *(dict) --*

          The value to be compared with the ``metric`` .

          - **count** *(integer) --*

            If the ``comparisonOperator`` calls for a numeric value, use this to specify that
            numeric value to be compared with the ``metric`` .

          - **cidrs** *(list) --*

            If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
            set to be compared with the ``metric`` .

            - *(string) --*

          - **ports** *(list) --*

            If the ``comparisonOperator`` calls for a set of ports, use this to specify that
            set to be compared with the ``metric`` .

            - *(integer) --*

        - **durationSeconds** *(integer) --*

          Use this to specify the time duration over which the behavior is evaluated, for those
          criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
          ``statisticalThreshhold`` metric comparison, measurements from all devices are
          accumulated over this time duration before being used to calculate percentiles, and
          later, measurements from an individual device are also accumulated over this time
          duration before being given a percentile rank.

        - **consecutiveDatapointsToAlarm** *(integer) --*

          If a device is in violation of the behavior for the specified number of consecutive
          datapoints, an alarm occurs. If not specified, the default is 1.

        - **consecutiveDatapointsToClear** *(integer) --*

          If an alarm has occurred and the offending device is no longer in violation of the
          behavior for the specified number of consecutive datapoints, the alarm is cleared. If
          not specified, the default is 1.

        - **statisticalThreshold** *(dict) --*

          A statistical ranking (percentile) which indicates a threshold value by which a
          behavior is determined to be in compliance or in violation of the behavior.

          - **statistic** *(string) --*

            The percentile which resolves to a threshold value by which compliance with a
            behavior is determined. Metrics are collected over the specified period
            (``durationSeconds`` ) from all reporting devices in your account and statistical
            ranks are calculated. Then, the measurements from a device are collected over the
            same period. If the accumulated measurements from the device fall above or below
            (``comparisonOperator`` ) the value associated with the percentile specified, then
            the device is considered to be in compliance with the behavior, otherwise a
            violation occurs.

    - **lastViolationValue** *(dict) --*

      The value of the metric (the measurement) which caused the most recent violation.

      - **count** *(integer) --*

        If the ``comparisonOperator`` calls for a numeric value, use this to specify that
        numeric value to be compared with the ``metric`` .

      - **cidrs** *(list) --*

        If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
        be compared with the ``metric`` .

        - *(string) --*

      - **ports** *(list) --*

        If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
        be compared with the ``metric`` .

        - *(integer) --*

    - **lastViolationTime** *(datetime) --*

      The time the most recent violation occurred.

    - **violationStartTime** *(datetime) --*

      The time the violation started.
    """


_ClientListActiveViolationsResponseTypeDef = TypedDict(
    "_ClientListActiveViolationsResponseTypeDef",
    {
        "activeViolations": List[
            ClientListActiveViolationsResponseactiveViolationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListActiveViolationsResponseTypeDef(
    _ClientListActiveViolationsResponseTypeDef
):
    """
    Type definition for `ClientListActiveViolations` `Response`

    - **activeViolations** *(list) --*

      The list of active violations.

      - *(dict) --*

        Information about an active Device Defender security profile behavior violation.

        - **violationId** *(string) --*

          The ID of the active violation.

        - **thingName** *(string) --*

          The name of the thing responsible for the active violation.

        - **securityProfileName** *(string) --*

          The security profile whose behavior is in violation.

        - **behavior** *(dict) --*

          The behavior which is being violated.

          - **name** *(string) --*

            The name you have given to the behavior.

          - **metric** *(string) --*

            What is measured by the behavior.

          - **criteria** *(dict) --*

            The criteria that determine if a device is behaving normally in regard to the
            ``metric`` .

            - **comparisonOperator** *(string) --*

              The operator that relates the thing measured (``metric`` ) to the criteria
              (containing a ``value`` or ``statisticalThreshold`` ).

            - **value** *(dict) --*

              The value to be compared with the ``metric`` .

              - **count** *(integer) --*

                If the ``comparisonOperator`` calls for a numeric value, use this to specify that
                numeric value to be compared with the ``metric`` .

              - **cidrs** *(list) --*

                If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
                set to be compared with the ``metric`` .

                - *(string) --*

              - **ports** *(list) --*

                If the ``comparisonOperator`` calls for a set of ports, use this to specify that
                set to be compared with the ``metric`` .

                - *(integer) --*

            - **durationSeconds** *(integer) --*

              Use this to specify the time duration over which the behavior is evaluated, for those
              criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
              ``statisticalThreshhold`` metric comparison, measurements from all devices are
              accumulated over this time duration before being used to calculate percentiles, and
              later, measurements from an individual device are also accumulated over this time
              duration before being given a percentile rank.

            - **consecutiveDatapointsToAlarm** *(integer) --*

              If a device is in violation of the behavior for the specified number of consecutive
              datapoints, an alarm occurs. If not specified, the default is 1.

            - **consecutiveDatapointsToClear** *(integer) --*

              If an alarm has occurred and the offending device is no longer in violation of the
              behavior for the specified number of consecutive datapoints, the alarm is cleared. If
              not specified, the default is 1.

            - **statisticalThreshold** *(dict) --*

              A statistical ranking (percentile) which indicates a threshold value by which a
              behavior is determined to be in compliance or in violation of the behavior.

              - **statistic** *(string) --*

                The percentile which resolves to a threshold value by which compliance with a
                behavior is determined. Metrics are collected over the specified period
                (``durationSeconds`` ) from all reporting devices in your account and statistical
                ranks are calculated. Then, the measurements from a device are collected over the
                same period. If the accumulated measurements from the device fall above or below
                (``comparisonOperator`` ) the value associated with the percentile specified, then
                the device is considered to be in compliance with the behavior, otherwise a
                violation occurs.

        - **lastViolationValue** *(dict) --*

          The value of the metric (the measurement) which caused the most recent violation.

          - **count** *(integer) --*

            If the ``comparisonOperator`` calls for a numeric value, use this to specify that
            numeric value to be compared with the ``metric`` .

          - **cidrs** *(list) --*

            If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
            be compared with the ``metric`` .

            - *(string) --*

          - **ports** *(list) --*

            If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
            be compared with the ``metric`` .

            - *(integer) --*

        - **lastViolationTime** *(datetime) --*

          The time the most recent violation occurred.

        - **violationStartTime** *(datetime) --*

          The time the violation started.

    - **nextToken** *(string) --*

      A token that can be used to retrieve the next set of results, or ``null`` if there are no
      additional results.
    """


_ClientListAttachedPoliciesResponsepoliciesTypeDef = TypedDict(
    "_ClientListAttachedPoliciesResponsepoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)


class ClientListAttachedPoliciesResponsepoliciesTypeDef(
    _ClientListAttachedPoliciesResponsepoliciesTypeDef
):
    """
    Type definition for `ClientListAttachedPoliciesResponse` `policies`

    Describes an AWS IoT policy.

    - **policyName** *(string) --*

      The policy name.

    - **policyArn** *(string) --*

      The policy ARN.
    """


_ClientListAttachedPoliciesResponseTypeDef = TypedDict(
    "_ClientListAttachedPoliciesResponseTypeDef",
    {
        "policies": List[ClientListAttachedPoliciesResponsepoliciesTypeDef],
        "nextMarker": str,
    },
    total=False,
)


class ClientListAttachedPoliciesResponseTypeDef(
    _ClientListAttachedPoliciesResponseTypeDef
):
    """
    Type definition for `ClientListAttachedPolicies` `Response`

    - **policies** *(list) --*

      The policies.

      - *(dict) --*

        Describes an AWS IoT policy.

        - **policyName** *(string) --*

          The policy name.

        - **policyArn** *(string) --*

          The policy ARN.

    - **nextMarker** *(string) --*

      The token to retrieve the next set of results, or ``null`` if there are no more results.
    """


_ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "_ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)


class ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef(
    _ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef
):
    """
    Type definition for `ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifier` `policyVersionIdentifier`

    The version of the policy associated with the resource.

    - **policyName** *(string) --*

      The name of the policy.

    - **policyVersionId** *(string) --*

      The ID of the version of the policy associated with the resource.
    """


_ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierTypeDef = TypedDict(
    "_ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
    },
    total=False,
)


class ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierTypeDef(
    _ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierTypeDef
):
    """
    Type definition for `ClientListAuditFindingsResponsefindingsnonCompliantResource` `resourceIdentifier`

    Information that identifies the noncompliant resource.

    - **deviceCertificateId** *(string) --*

      The ID of the certificate attached to the resource.

    - **caCertificateId** *(string) --*

      The ID of the CA certificate used to authorize the certificate.

    - **cognitoIdentityPoolId** *(string) --*

      The ID of the Amazon Cognito identity pool.

    - **clientId** *(string) --*

      The client ID.

    - **policyVersionIdentifier** *(dict) --*

      The version of the policy associated with the resource.

      - **policyName** *(string) --*

        The name of the policy.

      - **policyVersionId** *(string) --*

        The ID of the version of the policy associated with the resource.

    - **account** *(string) --*

      The account with which the resource is associated.
    """


_ClientListAuditFindingsResponsefindingsnonCompliantResourceTypeDef = TypedDict(
    "_ClientListAuditFindingsResponsefindingsnonCompliantResourceTypeDef",
    {
        "resourceType": str,
        "resourceIdentifier": ClientListAuditFindingsResponsefindingsnonCompliantResourceresourceIdentifierTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)


class ClientListAuditFindingsResponsefindingsnonCompliantResourceTypeDef(
    _ClientListAuditFindingsResponsefindingsnonCompliantResourceTypeDef
):
    """
    Type definition for `ClientListAuditFindingsResponsefindings` `nonCompliantResource`

    The resource that was found to be noncompliant with the audit check.

    - **resourceType** *(string) --*

      The type of the noncompliant resource.

    - **resourceIdentifier** *(dict) --*

      Information that identifies the noncompliant resource.

      - **deviceCertificateId** *(string) --*

        The ID of the certificate attached to the resource.

      - **caCertificateId** *(string) --*

        The ID of the CA certificate used to authorize the certificate.

      - **cognitoIdentityPoolId** *(string) --*

        The ID of the Amazon Cognito identity pool.

      - **clientId** *(string) --*

        The client ID.

      - **policyVersionIdentifier** *(dict) --*

        The version of the policy associated with the resource.

        - **policyName** *(string) --*

          The name of the policy.

        - **policyVersionId** *(string) --*

          The ID of the version of the policy associated with the resource.

      - **account** *(string) --*

        The account with which the resource is associated.

    - **additionalInfo** *(dict) --*

      Other information about the noncompliant resource.

      - *(string) --*

        - *(string) --*
    """


_ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "_ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)


class ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef(
    _ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef
):
    """
    Type definition for `ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifier` `policyVersionIdentifier`

    The version of the policy associated with the resource.

    - **policyName** *(string) --*

      The name of the policy.

    - **policyVersionId** *(string) --*

      The ID of the version of the policy associated with the resource.
    """


_ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierTypeDef = TypedDict(
    "_ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
    },
    total=False,
)


class ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierTypeDef(
    _ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierTypeDef
):
    """
    Type definition for `ClientListAuditFindingsResponsefindingsrelatedResources` `resourceIdentifier`

    Information that identifies the resource.

    - **deviceCertificateId** *(string) --*

      The ID of the certificate attached to the resource.

    - **caCertificateId** *(string) --*

      The ID of the CA certificate used to authorize the certificate.

    - **cognitoIdentityPoolId** *(string) --*

      The ID of the Amazon Cognito identity pool.

    - **clientId** *(string) --*

      The client ID.

    - **policyVersionIdentifier** *(dict) --*

      The version of the policy associated with the resource.

      - **policyName** *(string) --*

        The name of the policy.

      - **policyVersionId** *(string) --*

        The ID of the version of the policy associated with the resource.

    - **account** *(string) --*

      The account with which the resource is associated.
    """


_ClientListAuditFindingsResponsefindingsrelatedResourcesTypeDef = TypedDict(
    "_ClientListAuditFindingsResponsefindingsrelatedResourcesTypeDef",
    {
        "resourceType": str,
        "resourceIdentifier": ClientListAuditFindingsResponsefindingsrelatedResourcesresourceIdentifierTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)


class ClientListAuditFindingsResponsefindingsrelatedResourcesTypeDef(
    _ClientListAuditFindingsResponsefindingsrelatedResourcesTypeDef
):
    """
    Type definition for `ClientListAuditFindingsResponsefindings` `relatedResources`

    Information about a related resource.

    - **resourceType** *(string) --*

      The type of resource.

    - **resourceIdentifier** *(dict) --*

      Information that identifies the resource.

      - **deviceCertificateId** *(string) --*

        The ID of the certificate attached to the resource.

      - **caCertificateId** *(string) --*

        The ID of the CA certificate used to authorize the certificate.

      - **cognitoIdentityPoolId** *(string) --*

        The ID of the Amazon Cognito identity pool.

      - **clientId** *(string) --*

        The client ID.

      - **policyVersionIdentifier** *(dict) --*

        The version of the policy associated with the resource.

        - **policyName** *(string) --*

          The name of the policy.

        - **policyVersionId** *(string) --*

          The ID of the version of the policy associated with the resource.

      - **account** *(string) --*

        The account with which the resource is associated.

    - **additionalInfo** *(dict) --*

      Other information about the resource.

      - *(string) --*

        - *(string) --*
    """


_ClientListAuditFindingsResponsefindingsTypeDef = TypedDict(
    "_ClientListAuditFindingsResponsefindingsTypeDef",
    {
        "findingId": str,
        "taskId": str,
        "checkName": str,
        "taskStartTime": datetime,
        "findingTime": datetime,
        "severity": str,
        "nonCompliantResource": ClientListAuditFindingsResponsefindingsnonCompliantResourceTypeDef,
        "relatedResources": List[
            ClientListAuditFindingsResponsefindingsrelatedResourcesTypeDef
        ],
        "reasonForNonCompliance": str,
        "reasonForNonComplianceCode": str,
    },
    total=False,
)


class ClientListAuditFindingsResponsefindingsTypeDef(
    _ClientListAuditFindingsResponsefindingsTypeDef
):
    """
    Type definition for `ClientListAuditFindingsResponse` `findings`

    The findings (results) of the audit.

    - **findingId** *(string) --*

      A unique identifier for this set of audit findings. This identifier is used to apply
      mitigation tasks to one or more sets of findings.

    - **taskId** *(string) --*

      The ID of the audit that generated this result (finding).

    - **checkName** *(string) --*

      The audit check that generated this result.

    - **taskStartTime** *(datetime) --*

      The time the audit started.

    - **findingTime** *(datetime) --*

      The time the result (finding) was discovered.

    - **severity** *(string) --*

      The severity of the result (finding).

    - **nonCompliantResource** *(dict) --*

      The resource that was found to be noncompliant with the audit check.

      - **resourceType** *(string) --*

        The type of the noncompliant resource.

      - **resourceIdentifier** *(dict) --*

        Information that identifies the noncompliant resource.

        - **deviceCertificateId** *(string) --*

          The ID of the certificate attached to the resource.

        - **caCertificateId** *(string) --*

          The ID of the CA certificate used to authorize the certificate.

        - **cognitoIdentityPoolId** *(string) --*

          The ID of the Amazon Cognito identity pool.

        - **clientId** *(string) --*

          The client ID.

        - **policyVersionIdentifier** *(dict) --*

          The version of the policy associated with the resource.

          - **policyName** *(string) --*

            The name of the policy.

          - **policyVersionId** *(string) --*

            The ID of the version of the policy associated with the resource.

        - **account** *(string) --*

          The account with which the resource is associated.

      - **additionalInfo** *(dict) --*

        Other information about the noncompliant resource.

        - *(string) --*

          - *(string) --*

    - **relatedResources** *(list) --*

      The list of related resources.

      - *(dict) --*

        Information about a related resource.

        - **resourceType** *(string) --*

          The type of resource.

        - **resourceIdentifier** *(dict) --*

          Information that identifies the resource.

          - **deviceCertificateId** *(string) --*

            The ID of the certificate attached to the resource.

          - **caCertificateId** *(string) --*

            The ID of the CA certificate used to authorize the certificate.

          - **cognitoIdentityPoolId** *(string) --*

            The ID of the Amazon Cognito identity pool.

          - **clientId** *(string) --*

            The client ID.

          - **policyVersionIdentifier** *(dict) --*

            The version of the policy associated with the resource.

            - **policyName** *(string) --*

              The name of the policy.

            - **policyVersionId** *(string) --*

              The ID of the version of the policy associated with the resource.

          - **account** *(string) --*

            The account with which the resource is associated.

        - **additionalInfo** *(dict) --*

          Other information about the resource.

          - *(string) --*

            - *(string) --*

    - **reasonForNonCompliance** *(string) --*

      The reason the resource was noncompliant.

    - **reasonForNonComplianceCode** *(string) --*

      A code that indicates the reason that the resource was noncompliant.
    """


_ClientListAuditFindingsResponseTypeDef = TypedDict(
    "_ClientListAuditFindingsResponseTypeDef",
    {
        "findings": List[ClientListAuditFindingsResponsefindingsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListAuditFindingsResponseTypeDef(_ClientListAuditFindingsResponseTypeDef):
    """
    Type definition for `ClientListAuditFindings` `Response`

    - **findings** *(list) --*

      The findings (results) of the audit.

      - *(dict) --*

        The findings (results) of the audit.

        - **findingId** *(string) --*

          A unique identifier for this set of audit findings. This identifier is used to apply
          mitigation tasks to one or more sets of findings.

        - **taskId** *(string) --*

          The ID of the audit that generated this result (finding).

        - **checkName** *(string) --*

          The audit check that generated this result.

        - **taskStartTime** *(datetime) --*

          The time the audit started.

        - **findingTime** *(datetime) --*

          The time the result (finding) was discovered.

        - **severity** *(string) --*

          The severity of the result (finding).

        - **nonCompliantResource** *(dict) --*

          The resource that was found to be noncompliant with the audit check.

          - **resourceType** *(string) --*

            The type of the noncompliant resource.

          - **resourceIdentifier** *(dict) --*

            Information that identifies the noncompliant resource.

            - **deviceCertificateId** *(string) --*

              The ID of the certificate attached to the resource.

            - **caCertificateId** *(string) --*

              The ID of the CA certificate used to authorize the certificate.

            - **cognitoIdentityPoolId** *(string) --*

              The ID of the Amazon Cognito identity pool.

            - **clientId** *(string) --*

              The client ID.

            - **policyVersionIdentifier** *(dict) --*

              The version of the policy associated with the resource.

              - **policyName** *(string) --*

                The name of the policy.

              - **policyVersionId** *(string) --*

                The ID of the version of the policy associated with the resource.

            - **account** *(string) --*

              The account with which the resource is associated.

          - **additionalInfo** *(dict) --*

            Other information about the noncompliant resource.

            - *(string) --*

              - *(string) --*

        - **relatedResources** *(list) --*

          The list of related resources.

          - *(dict) --*

            Information about a related resource.

            - **resourceType** *(string) --*

              The type of resource.

            - **resourceIdentifier** *(dict) --*

              Information that identifies the resource.

              - **deviceCertificateId** *(string) --*

                The ID of the certificate attached to the resource.

              - **caCertificateId** *(string) --*

                The ID of the CA certificate used to authorize the certificate.

              - **cognitoIdentityPoolId** *(string) --*

                The ID of the Amazon Cognito identity pool.

              - **clientId** *(string) --*

                The client ID.

              - **policyVersionIdentifier** *(dict) --*

                The version of the policy associated with the resource.

                - **policyName** *(string) --*

                  The name of the policy.

                - **policyVersionId** *(string) --*

                  The ID of the version of the policy associated with the resource.

              - **account** *(string) --*

                The account with which the resource is associated.

            - **additionalInfo** *(dict) --*

              Other information about the resource.

              - *(string) --*

                - *(string) --*

        - **reasonForNonCompliance** *(string) --*

          The reason the resource was noncompliant.

        - **reasonForNonComplianceCode** *(string) --*

          A code that indicates the reason that the resource was noncompliant.

    - **nextToken** *(string) --*

      A token that can be used to retrieve the next set of results, or ``null`` if there are no
      additional results.
    """


_ClientListAuditFindingsresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "_ClientListAuditFindingsresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)


class ClientListAuditFindingsresourceIdentifierpolicyVersionIdentifierTypeDef(
    _ClientListAuditFindingsresourceIdentifierpolicyVersionIdentifierTypeDef
):
    """
    Type definition for `ClientListAuditFindingsresourceIdentifier` `policyVersionIdentifier`

    The version of the policy associated with the resource.

    - **policyName** *(string) --*

      The name of the policy.

    - **policyVersionId** *(string) --*

      The ID of the version of the policy associated with the resource.
    """


_ClientListAuditFindingsresourceIdentifierTypeDef = TypedDict(
    "_ClientListAuditFindingsresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ClientListAuditFindingsresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
    },
    total=False,
)


class ClientListAuditFindingsresourceIdentifierTypeDef(
    _ClientListAuditFindingsresourceIdentifierTypeDef
):
    """
    Type definition for `ClientListAuditFindings` `resourceIdentifier`

    Information identifying the noncompliant resource.

    - **deviceCertificateId** *(string) --*

      The ID of the certificate attached to the resource.

    - **caCertificateId** *(string) --*

      The ID of the CA certificate used to authorize the certificate.

    - **cognitoIdentityPoolId** *(string) --*

      The ID of the Amazon Cognito identity pool.

    - **clientId** *(string) --*

      The client ID.

    - **policyVersionIdentifier** *(dict) --*

      The version of the policy associated with the resource.

      - **policyName** *(string) --*

        The name of the policy.

      - **policyVersionId** *(string) --*

        The ID of the version of the policy associated with the resource.

    - **account** *(string) --*

      The account with which the resource is associated.
    """


_ClientListAuditMitigationActionsExecutionsResponseactionsExecutionsTypeDef = TypedDict(
    "_ClientListAuditMitigationActionsExecutionsResponseactionsExecutionsTypeDef",
    {
        "taskId": str,
        "findingId": str,
        "actionName": str,
        "actionId": str,
        "status": str,
        "startTime": datetime,
        "endTime": datetime,
        "errorCode": str,
        "message": str,
    },
    total=False,
)


class ClientListAuditMitigationActionsExecutionsResponseactionsExecutionsTypeDef(
    _ClientListAuditMitigationActionsExecutionsResponseactionsExecutionsTypeDef
):
    """
    Type definition for `ClientListAuditMitigationActionsExecutionsResponse` `actionsExecutions`

    Returned by ListAuditMitigationActionsTask, this object contains information that describes
    a mitigation action that has been started.

    - **taskId** *(string) --*

      The unique identifier for the task that applies the mitigation action.

    - **findingId** *(string) --*

      The unique identifier for the findings to which the task and associated mitigation action
      are applied.

    - **actionName** *(string) --*

      The friendly name of the mitigation action being applied by the task.

    - **actionId** *(string) --*

      The unique identifier for the mitigation action being applied by the task.

    - **status** *(string) --*

      The current status of the task being executed.

    - **startTime** *(datetime) --*

      The date and time when the task was started.

    - **endTime** *(datetime) --*

      The date and time when the task was completed or canceled. Blank if the task is still
      running.

    - **errorCode** *(string) --*

      If an error occurred, the code that indicates which type of error occurred.

    - **message** *(string) --*

      If an error occurred, a message that describes the error.
    """


_ClientListAuditMitigationActionsExecutionsResponseTypeDef = TypedDict(
    "_ClientListAuditMitigationActionsExecutionsResponseTypeDef",
    {
        "actionsExecutions": List[
            ClientListAuditMitigationActionsExecutionsResponseactionsExecutionsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListAuditMitigationActionsExecutionsResponseTypeDef(
    _ClientListAuditMitigationActionsExecutionsResponseTypeDef
):
    """
    Type definition for `ClientListAuditMitigationActionsExecutions` `Response`

    - **actionsExecutions** *(list) --*

      A set of task execution results based on the input parameters. Details include the mitigation
      action applied, start time, and task status.

      - *(dict) --*

        Returned by ListAuditMitigationActionsTask, this object contains information that describes
        a mitigation action that has been started.

        - **taskId** *(string) --*

          The unique identifier for the task that applies the mitigation action.

        - **findingId** *(string) --*

          The unique identifier for the findings to which the task and associated mitigation action
          are applied.

        - **actionName** *(string) --*

          The friendly name of the mitigation action being applied by the task.

        - **actionId** *(string) --*

          The unique identifier for the mitigation action being applied by the task.

        - **status** *(string) --*

          The current status of the task being executed.

        - **startTime** *(datetime) --*

          The date and time when the task was started.

        - **endTime** *(datetime) --*

          The date and time when the task was completed or canceled. Blank if the task is still
          running.

        - **errorCode** *(string) --*

          If an error occurred, the code that indicates which type of error occurred.

        - **message** *(string) --*

          If an error occurred, a message that describes the error.

    - **nextToken** *(string) --*

      The token for the next set of results.
    """


_ClientListAuditMitigationActionsTasksResponsetasksTypeDef = TypedDict(
    "_ClientListAuditMitigationActionsTasksResponsetasksTypeDef",
    {"taskId": str, "startTime": datetime, "taskStatus": str},
    total=False,
)


class ClientListAuditMitigationActionsTasksResponsetasksTypeDef(
    _ClientListAuditMitigationActionsTasksResponsetasksTypeDef
):
    """
    Type definition for `ClientListAuditMitigationActionsTasksResponse` `tasks`

    Information about an audit mitigation actions task that is returned by
    ``ListAuditMitigationActionsTasks`` .

    - **taskId** *(string) --*

      The unique identifier for the task.

    - **startTime** *(datetime) --*

      The time at which the audit mitigation actions task was started.

    - **taskStatus** *(string) --*

      The current state of the audit mitigation actions task.
    """


_ClientListAuditMitigationActionsTasksResponseTypeDef = TypedDict(
    "_ClientListAuditMitigationActionsTasksResponseTypeDef",
    {
        "tasks": List[ClientListAuditMitigationActionsTasksResponsetasksTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListAuditMitigationActionsTasksResponseTypeDef(
    _ClientListAuditMitigationActionsTasksResponseTypeDef
):
    """
    Type definition for `ClientListAuditMitigationActionsTasks` `Response`

    - **tasks** *(list) --*

      The collection of audit mitigation tasks that matched the filter criteria.

      - *(dict) --*

        Information about an audit mitigation actions task that is returned by
        ``ListAuditMitigationActionsTasks`` .

        - **taskId** *(string) --*

          The unique identifier for the task.

        - **startTime** *(datetime) --*

          The time at which the audit mitigation actions task was started.

        - **taskStatus** *(string) --*

          The current state of the audit mitigation actions task.

    - **nextToken** *(string) --*

      The token for the next set of results.
    """


_ClientListAuditTasksResponsetasksTypeDef = TypedDict(
    "_ClientListAuditTasksResponsetasksTypeDef",
    {"taskId": str, "taskStatus": str, "taskType": str},
    total=False,
)


class ClientListAuditTasksResponsetasksTypeDef(
    _ClientListAuditTasksResponsetasksTypeDef
):
    """
    Type definition for `ClientListAuditTasksResponse` `tasks`

    The audits that were performed.

    - **taskId** *(string) --*

      The ID of this audit.

    - **taskStatus** *(string) --*

      The status of this audit. One of "IN_PROGRESS", "COMPLETED", "FAILED", or "CANCELED".

    - **taskType** *(string) --*

      The type of this audit. One of "ON_DEMAND_AUDIT_TASK" or "SCHEDULED_AUDIT_TASK".
    """


_ClientListAuditTasksResponseTypeDef = TypedDict(
    "_ClientListAuditTasksResponseTypeDef",
    {"tasks": List[ClientListAuditTasksResponsetasksTypeDef], "nextToken": str},
    total=False,
)


class ClientListAuditTasksResponseTypeDef(_ClientListAuditTasksResponseTypeDef):
    """
    Type definition for `ClientListAuditTasks` `Response`

    - **tasks** *(list) --*

      The audits that were performed during the specified time period.

      - *(dict) --*

        The audits that were performed.

        - **taskId** *(string) --*

          The ID of this audit.

        - **taskStatus** *(string) --*

          The status of this audit. One of "IN_PROGRESS", "COMPLETED", "FAILED", or "CANCELED".

        - **taskType** *(string) --*

          The type of this audit. One of "ON_DEMAND_AUDIT_TASK" or "SCHEDULED_AUDIT_TASK".

    - **nextToken** *(string) --*

      A token that can be used to retrieve the next set of results, or ``null`` if there are no
      additional results.
    """


_ClientListAuthorizersResponseauthorizersTypeDef = TypedDict(
    "_ClientListAuthorizersResponseauthorizersTypeDef",
    {"authorizerName": str, "authorizerArn": str},
    total=False,
)


class ClientListAuthorizersResponseauthorizersTypeDef(
    _ClientListAuthorizersResponseauthorizersTypeDef
):
    """
    Type definition for `ClientListAuthorizersResponse` `authorizers`

    The authorizer summary.

    - **authorizerName** *(string) --*

      The authorizer name.

    - **authorizerArn** *(string) --*

      The authorizer ARN.
    """


_ClientListAuthorizersResponseTypeDef = TypedDict(
    "_ClientListAuthorizersResponseTypeDef",
    {
        "authorizers": List[ClientListAuthorizersResponseauthorizersTypeDef],
        "nextMarker": str,
    },
    total=False,
)


class ClientListAuthorizersResponseTypeDef(_ClientListAuthorizersResponseTypeDef):
    """
    Type definition for `ClientListAuthorizers` `Response`

    - **authorizers** *(list) --*

      The authorizers.

      - *(dict) --*

        The authorizer summary.

        - **authorizerName** *(string) --*

          The authorizer name.

        - **authorizerArn** *(string) --*

          The authorizer ARN.

    - **nextMarker** *(string) --*

      A marker used to get the next set of results.
    """


_ClientListBillingGroupsResponsebillingGroupsTypeDef = TypedDict(
    "_ClientListBillingGroupsResponsebillingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)


class ClientListBillingGroupsResponsebillingGroupsTypeDef(
    _ClientListBillingGroupsResponsebillingGroupsTypeDef
):
    """
    Type definition for `ClientListBillingGroupsResponse` `billingGroups`

    The name and ARN of a group.

    - **groupName** *(string) --*

      The group name.

    - **groupArn** *(string) --*

      The group ARN.
    """


_ClientListBillingGroupsResponseTypeDef = TypedDict(
    "_ClientListBillingGroupsResponseTypeDef",
    {
        "billingGroups": List[ClientListBillingGroupsResponsebillingGroupsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListBillingGroupsResponseTypeDef(_ClientListBillingGroupsResponseTypeDef):
    """
    Type definition for `ClientListBillingGroups` `Response`

    - **billingGroups** *(list) --*

      The list of billing groups.

      - *(dict) --*

        The name and ARN of a group.

        - **groupName** *(string) --*

          The group name.

        - **groupArn** *(string) --*

          The group ARN.

    - **nextToken** *(string) --*

      The token used to get the next set of results, or **null** if there are no additional results.
    """


_ClientListCaCertificatesResponsecertificatesTypeDef = TypedDict(
    "_ClientListCaCertificatesResponsecertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": str,
        "creationDate": datetime,
    },
    total=False,
)


class ClientListCaCertificatesResponsecertificatesTypeDef(
    _ClientListCaCertificatesResponsecertificatesTypeDef
):
    """
    Type definition for `ClientListCaCertificatesResponse` `certificates`

    A CA certificate.

    - **certificateArn** *(string) --*

      The ARN of the CA certificate.

    - **certificateId** *(string) --*

      The ID of the CA certificate.

    - **status** *(string) --*

      The status of the CA certificate.

      The status value REGISTER_INACTIVE is deprecated and should not be used.

    - **creationDate** *(datetime) --*

      The date the CA certificate was created.
    """


_ClientListCaCertificatesResponseTypeDef = TypedDict(
    "_ClientListCaCertificatesResponseTypeDef",
    {
        "certificates": List[ClientListCaCertificatesResponsecertificatesTypeDef],
        "nextMarker": str,
    },
    total=False,
)


class ClientListCaCertificatesResponseTypeDef(_ClientListCaCertificatesResponseTypeDef):
    """
    Type definition for `ClientListCaCertificates` `Response`

    The output from the ListCACertificates operation.

    - **certificates** *(list) --*

      The CA certificates registered in your AWS account.

      - *(dict) --*

        A CA certificate.

        - **certificateArn** *(string) --*

          The ARN of the CA certificate.

        - **certificateId** *(string) --*

          The ID of the CA certificate.

        - **status** *(string) --*

          The status of the CA certificate.

          The status value REGISTER_INACTIVE is deprecated and should not be used.

        - **creationDate** *(datetime) --*

          The date the CA certificate was created.

    - **nextMarker** *(string) --*

      The current position within the list of CA certificates.
    """


_ClientListCertificatesByCaResponsecertificatesTypeDef = TypedDict(
    "_ClientListCertificatesByCaResponsecertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": str,
        "creationDate": datetime,
    },
    total=False,
)


class ClientListCertificatesByCaResponsecertificatesTypeDef(
    _ClientListCertificatesByCaResponsecertificatesTypeDef
):
    """
    Type definition for `ClientListCertificatesByCaResponse` `certificates`

    Information about a certificate.

    - **certificateArn** *(string) --*

      The ARN of the certificate.

    - **certificateId** *(string) --*

      The ID of the certificate. (The last part of the certificate ARN contains the certificate
      ID.)

    - **status** *(string) --*

      The status of the certificate.

      The status value REGISTER_INACTIVE is deprecated and should not be used.

    - **creationDate** *(datetime) --*

      The date and time the certificate was created.
    """


_ClientListCertificatesByCaResponseTypeDef = TypedDict(
    "_ClientListCertificatesByCaResponseTypeDef",
    {
        "certificates": List[ClientListCertificatesByCaResponsecertificatesTypeDef],
        "nextMarker": str,
    },
    total=False,
)


class ClientListCertificatesByCaResponseTypeDef(
    _ClientListCertificatesByCaResponseTypeDef
):
    """
    Type definition for `ClientListCertificatesByCa` `Response`

    The output of the ListCertificatesByCA operation.

    - **certificates** *(list) --*

      The device certificates signed by the specified CA certificate.

      - *(dict) --*

        Information about a certificate.

        - **certificateArn** *(string) --*

          The ARN of the certificate.

        - **certificateId** *(string) --*

          The ID of the certificate. (The last part of the certificate ARN contains the certificate
          ID.)

        - **status** *(string) --*

          The status of the certificate.

          The status value REGISTER_INACTIVE is deprecated and should not be used.

        - **creationDate** *(datetime) --*

          The date and time the certificate was created.

    - **nextMarker** *(string) --*

      The marker for the next set of results, or null if there are no additional results.
    """


_ClientListCertificatesResponsecertificatesTypeDef = TypedDict(
    "_ClientListCertificatesResponsecertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": str,
        "creationDate": datetime,
    },
    total=False,
)


class ClientListCertificatesResponsecertificatesTypeDef(
    _ClientListCertificatesResponsecertificatesTypeDef
):
    """
    Type definition for `ClientListCertificatesResponse` `certificates`

    Information about a certificate.

    - **certificateArn** *(string) --*

      The ARN of the certificate.

    - **certificateId** *(string) --*

      The ID of the certificate. (The last part of the certificate ARN contains the certificate
      ID.)

    - **status** *(string) --*

      The status of the certificate.

      The status value REGISTER_INACTIVE is deprecated and should not be used.

    - **creationDate** *(datetime) --*

      The date and time the certificate was created.
    """


_ClientListCertificatesResponseTypeDef = TypedDict(
    "_ClientListCertificatesResponseTypeDef",
    {
        "certificates": List[ClientListCertificatesResponsecertificatesTypeDef],
        "nextMarker": str,
    },
    total=False,
)


class ClientListCertificatesResponseTypeDef(_ClientListCertificatesResponseTypeDef):
    """
    Type definition for `ClientListCertificates` `Response`

    The output of the ListCertificates operation.

    - **certificates** *(list) --*

      The descriptions of the certificates.

      - *(dict) --*

        Information about a certificate.

        - **certificateArn** *(string) --*

          The ARN of the certificate.

        - **certificateId** *(string) --*

          The ID of the certificate. (The last part of the certificate ARN contains the certificate
          ID.)

        - **status** *(string) --*

          The status of the certificate.

          The status value REGISTER_INACTIVE is deprecated and should not be used.

        - **creationDate** *(datetime) --*

          The date and time the certificate was created.

    - **nextMarker** *(string) --*

      The marker for the next set of results, or null if there are no additional results.
    """


_ClientListIndicesResponseTypeDef = TypedDict(
    "_ClientListIndicesResponseTypeDef",
    {"indexNames": List[str], "nextToken": str},
    total=False,
)


class ClientListIndicesResponseTypeDef(_ClientListIndicesResponseTypeDef):
    """
    Type definition for `ClientListIndices` `Response`

    - **indexNames** *(list) --*

      The index names.

      - *(string) --*

    - **nextToken** *(string) --*

      The token used to get the next set of results, or null if there are no additional results.
    """


_ClientListJobExecutionsForJobResponseexecutionSummariesjobExecutionSummaryTypeDef = TypedDict(
    "_ClientListJobExecutionsForJobResponseexecutionSummariesjobExecutionSummaryTypeDef",
    {
        "status": str,
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
    },
    total=False,
)


class ClientListJobExecutionsForJobResponseexecutionSummariesjobExecutionSummaryTypeDef(
    _ClientListJobExecutionsForJobResponseexecutionSummariesjobExecutionSummaryTypeDef
):
    """
    Type definition for `ClientListJobExecutionsForJobResponseexecutionSummaries` `jobExecutionSummary`

    Contains a subset of information about a job execution.

    - **status** *(string) --*

      The status of the job execution.

    - **queuedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job execution was queued.

    - **startedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job execution started.

    - **lastUpdatedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job execution was last updated.

    - **executionNumber** *(integer) --*

      A string (consisting of the digits "0" through "9") which identifies this particular
      job execution on this particular device. It can be used later in commands which return
      or update job execution information.
    """


_ClientListJobExecutionsForJobResponseexecutionSummariesTypeDef = TypedDict(
    "_ClientListJobExecutionsForJobResponseexecutionSummariesTypeDef",
    {
        "thingArn": str,
        "jobExecutionSummary": ClientListJobExecutionsForJobResponseexecutionSummariesjobExecutionSummaryTypeDef,
    },
    total=False,
)


class ClientListJobExecutionsForJobResponseexecutionSummariesTypeDef(
    _ClientListJobExecutionsForJobResponseexecutionSummariesTypeDef
):
    """
    Type definition for `ClientListJobExecutionsForJobResponse` `executionSummaries`

    Contains a summary of information about job executions for a specific job.

    - **thingArn** *(string) --*

      The ARN of the thing on which the job execution is running.

    - **jobExecutionSummary** *(dict) --*

      Contains a subset of information about a job execution.

      - **status** *(string) --*

        The status of the job execution.

      - **queuedAt** *(datetime) --*

        The time, in seconds since the epoch, when the job execution was queued.

      - **startedAt** *(datetime) --*

        The time, in seconds since the epoch, when the job execution started.

      - **lastUpdatedAt** *(datetime) --*

        The time, in seconds since the epoch, when the job execution was last updated.

      - **executionNumber** *(integer) --*

        A string (consisting of the digits "0" through "9") which identifies this particular
        job execution on this particular device. It can be used later in commands which return
        or update job execution information.
    """


_ClientListJobExecutionsForJobResponseTypeDef = TypedDict(
    "_ClientListJobExecutionsForJobResponseTypeDef",
    {
        "executionSummaries": List[
            ClientListJobExecutionsForJobResponseexecutionSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListJobExecutionsForJobResponseTypeDef(
    _ClientListJobExecutionsForJobResponseTypeDef
):
    """
    Type definition for `ClientListJobExecutionsForJob` `Response`

    - **executionSummaries** *(list) --*

      A list of job execution summaries.

      - *(dict) --*

        Contains a summary of information about job executions for a specific job.

        - **thingArn** *(string) --*

          The ARN of the thing on which the job execution is running.

        - **jobExecutionSummary** *(dict) --*

          Contains a subset of information about a job execution.

          - **status** *(string) --*

            The status of the job execution.

          - **queuedAt** *(datetime) --*

            The time, in seconds since the epoch, when the job execution was queued.

          - **startedAt** *(datetime) --*

            The time, in seconds since the epoch, when the job execution started.

          - **lastUpdatedAt** *(datetime) --*

            The time, in seconds since the epoch, when the job execution was last updated.

          - **executionNumber** *(integer) --*

            A string (consisting of the digits "0" through "9") which identifies this particular
            job execution on this particular device. It can be used later in commands which return
            or update job execution information.

    - **nextToken** *(string) --*

      The token for the next set of results, or **null** if there are no additional results.
    """


_ClientListJobExecutionsForThingResponseexecutionSummariesjobExecutionSummaryTypeDef = TypedDict(
    "_ClientListJobExecutionsForThingResponseexecutionSummariesjobExecutionSummaryTypeDef",
    {
        "status": str,
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
    },
    total=False,
)


class ClientListJobExecutionsForThingResponseexecutionSummariesjobExecutionSummaryTypeDef(
    _ClientListJobExecutionsForThingResponseexecutionSummariesjobExecutionSummaryTypeDef
):
    """
    Type definition for `ClientListJobExecutionsForThingResponseexecutionSummaries` `jobExecutionSummary`

    Contains a subset of information about a job execution.

    - **status** *(string) --*

      The status of the job execution.

    - **queuedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job execution was queued.

    - **startedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job execution started.

    - **lastUpdatedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job execution was last updated.

    - **executionNumber** *(integer) --*

      A string (consisting of the digits "0" through "9") which identifies this particular
      job execution on this particular device. It can be used later in commands which return
      or update job execution information.
    """


_ClientListJobExecutionsForThingResponseexecutionSummariesTypeDef = TypedDict(
    "_ClientListJobExecutionsForThingResponseexecutionSummariesTypeDef",
    {
        "jobId": str,
        "jobExecutionSummary": ClientListJobExecutionsForThingResponseexecutionSummariesjobExecutionSummaryTypeDef,
    },
    total=False,
)


class ClientListJobExecutionsForThingResponseexecutionSummariesTypeDef(
    _ClientListJobExecutionsForThingResponseexecutionSummariesTypeDef
):
    """
    Type definition for `ClientListJobExecutionsForThingResponse` `executionSummaries`

    The job execution summary for a thing.

    - **jobId** *(string) --*

      The unique identifier you assigned to this job when it was created.

    - **jobExecutionSummary** *(dict) --*

      Contains a subset of information about a job execution.

      - **status** *(string) --*

        The status of the job execution.

      - **queuedAt** *(datetime) --*

        The time, in seconds since the epoch, when the job execution was queued.

      - **startedAt** *(datetime) --*

        The time, in seconds since the epoch, when the job execution started.

      - **lastUpdatedAt** *(datetime) --*

        The time, in seconds since the epoch, when the job execution was last updated.

      - **executionNumber** *(integer) --*

        A string (consisting of the digits "0" through "9") which identifies this particular
        job execution on this particular device. It can be used later in commands which return
        or update job execution information.
    """


_ClientListJobExecutionsForThingResponseTypeDef = TypedDict(
    "_ClientListJobExecutionsForThingResponseTypeDef",
    {
        "executionSummaries": List[
            ClientListJobExecutionsForThingResponseexecutionSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListJobExecutionsForThingResponseTypeDef(
    _ClientListJobExecutionsForThingResponseTypeDef
):
    """
    Type definition for `ClientListJobExecutionsForThing` `Response`

    - **executionSummaries** *(list) --*

      A list of job execution summaries.

      - *(dict) --*

        The job execution summary for a thing.

        - **jobId** *(string) --*

          The unique identifier you assigned to this job when it was created.

        - **jobExecutionSummary** *(dict) --*

          Contains a subset of information about a job execution.

          - **status** *(string) --*

            The status of the job execution.

          - **queuedAt** *(datetime) --*

            The time, in seconds since the epoch, when the job execution was queued.

          - **startedAt** *(datetime) --*

            The time, in seconds since the epoch, when the job execution started.

          - **lastUpdatedAt** *(datetime) --*

            The time, in seconds since the epoch, when the job execution was last updated.

          - **executionNumber** *(integer) --*

            A string (consisting of the digits "0" through "9") which identifies this particular
            job execution on this particular device. It can be used later in commands which return
            or update job execution information.

    - **nextToken** *(string) --*

      The token for the next set of results, or **null** if there are no additional results.
    """


_ClientListJobsResponsejobsTypeDef = TypedDict(
    "_ClientListJobsResponsejobsTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "thingGroupId": str,
        "targetSelection": str,
        "status": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "completedAt": datetime,
    },
    total=False,
)


class ClientListJobsResponsejobsTypeDef(_ClientListJobsResponsejobsTypeDef):
    """
    Type definition for `ClientListJobsResponse` `jobs`

    The job summary.

    - **jobArn** *(string) --*

      The job ARN.

    - **jobId** *(string) --*

      The unique identifier you assigned to this job when it was created.

    - **thingGroupId** *(string) --*

      The ID of the thing group.

    - **targetSelection** *(string) --*

      Specifies whether the job will continue to run (CONTINUOUS), or will be complete after
      all those things specified as targets have completed the job (SNAPSHOT). If continuous,
      the job may also be run on a thing when a change is detected in a target. For example, a
      job will run on a thing when the thing is added to a target group, even after the job was
      completed by all things originally in the group.

    - **status** *(string) --*

      The job summary status.

    - **createdAt** *(datetime) --*

      The time, in seconds since the epoch, when the job was created.

    - **lastUpdatedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job was last updated.

    - **completedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job completed.
    """


_ClientListJobsResponseTypeDef = TypedDict(
    "_ClientListJobsResponseTypeDef",
    {"jobs": List[ClientListJobsResponsejobsTypeDef], "nextToken": str},
    total=False,
)


class ClientListJobsResponseTypeDef(_ClientListJobsResponseTypeDef):
    """
    Type definition for `ClientListJobs` `Response`

    - **jobs** *(list) --*

      A list of jobs.

      - *(dict) --*

        The job summary.

        - **jobArn** *(string) --*

          The job ARN.

        - **jobId** *(string) --*

          The unique identifier you assigned to this job when it was created.

        - **thingGroupId** *(string) --*

          The ID of the thing group.

        - **targetSelection** *(string) --*

          Specifies whether the job will continue to run (CONTINUOUS), or will be complete after
          all those things specified as targets have completed the job (SNAPSHOT). If continuous,
          the job may also be run on a thing when a change is detected in a target. For example, a
          job will run on a thing when the thing is added to a target group, even after the job was
          completed by all things originally in the group.

        - **status** *(string) --*

          The job summary status.

        - **createdAt** *(datetime) --*

          The time, in seconds since the epoch, when the job was created.

        - **lastUpdatedAt** *(datetime) --*

          The time, in seconds since the epoch, when the job was last updated.

        - **completedAt** *(datetime) --*

          The time, in seconds since the epoch, when the job completed.

    - **nextToken** *(string) --*

      The token for the next set of results, or **null** if there are no additional results.
    """


_ClientListMitigationActionsResponseactionIdentifiersTypeDef = TypedDict(
    "_ClientListMitigationActionsResponseactionIdentifiersTypeDef",
    {"actionName": str, "actionArn": str, "creationDate": datetime},
    total=False,
)


class ClientListMitigationActionsResponseactionIdentifiersTypeDef(
    _ClientListMitigationActionsResponseactionIdentifiersTypeDef
):
    """
    Type definition for `ClientListMitigationActionsResponse` `actionIdentifiers`

    Information that identifies a mitigation action. This information is returned by
    ListMitigationActions.

    - **actionName** *(string) --*

      The friendly name of the mitigation action.

    - **actionArn** *(string) --*

      The IAM role ARN used to apply this mitigation action.

    - **creationDate** *(datetime) --*

      The date when this mitigation action was created.
    """


_ClientListMitigationActionsResponseTypeDef = TypedDict(
    "_ClientListMitigationActionsResponseTypeDef",
    {
        "actionIdentifiers": List[
            ClientListMitigationActionsResponseactionIdentifiersTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListMitigationActionsResponseTypeDef(
    _ClientListMitigationActionsResponseTypeDef
):
    """
    Type definition for `ClientListMitigationActions` `Response`

    - **actionIdentifiers** *(list) --*

      A set of actions that matched the specified filter criteria.

      - *(dict) --*

        Information that identifies a mitigation action. This information is returned by
        ListMitigationActions.

        - **actionName** *(string) --*

          The friendly name of the mitigation action.

        - **actionArn** *(string) --*

          The IAM role ARN used to apply this mitigation action.

        - **creationDate** *(datetime) --*

          The date when this mitigation action was created.

    - **nextToken** *(string) --*

      The token for the next set of results.
    """


_ClientListOtaUpdatesResponseotaUpdatesTypeDef = TypedDict(
    "_ClientListOtaUpdatesResponseotaUpdatesTypeDef",
    {"otaUpdateId": str, "otaUpdateArn": str, "creationDate": datetime},
    total=False,
)


class ClientListOtaUpdatesResponseotaUpdatesTypeDef(
    _ClientListOtaUpdatesResponseotaUpdatesTypeDef
):
    """
    Type definition for `ClientListOtaUpdatesResponse` `otaUpdates`

    An OTA update summary.

    - **otaUpdateId** *(string) --*

      The OTA update ID.

    - **otaUpdateArn** *(string) --*

      The OTA update ARN.

    - **creationDate** *(datetime) --*

      The date when the OTA update was created.
    """


_ClientListOtaUpdatesResponseTypeDef = TypedDict(
    "_ClientListOtaUpdatesResponseTypeDef",
    {
        "otaUpdates": List[ClientListOtaUpdatesResponseotaUpdatesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListOtaUpdatesResponseTypeDef(_ClientListOtaUpdatesResponseTypeDef):
    """
    Type definition for `ClientListOtaUpdates` `Response`

    - **otaUpdates** *(list) --*

      A list of OTA update jobs.

      - *(dict) --*

        An OTA update summary.

        - **otaUpdateId** *(string) --*

          The OTA update ID.

        - **otaUpdateArn** *(string) --*

          The OTA update ARN.

        - **creationDate** *(datetime) --*

          The date when the OTA update was created.

    - **nextToken** *(string) --*

      A token to use to get the next set of results.
    """


_ClientListOutgoingCertificatesResponseoutgoingCertificatesTypeDef = TypedDict(
    "_ClientListOutgoingCertificatesResponseoutgoingCertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "transferredTo": str,
        "transferDate": datetime,
        "transferMessage": str,
        "creationDate": datetime,
    },
    total=False,
)


class ClientListOutgoingCertificatesResponseoutgoingCertificatesTypeDef(
    _ClientListOutgoingCertificatesResponseoutgoingCertificatesTypeDef
):
    """
    Type definition for `ClientListOutgoingCertificatesResponse` `outgoingCertificates`

    A certificate that has been transferred but not yet accepted.

    - **certificateArn** *(string) --*

      The certificate ARN.

    - **certificateId** *(string) --*

      The certificate ID.

    - **transferredTo** *(string) --*

      The AWS account to which the transfer was made.

    - **transferDate** *(datetime) --*

      The date the transfer was initiated.

    - **transferMessage** *(string) --*

      The transfer message.

    - **creationDate** *(datetime) --*

      The certificate creation date.
    """


_ClientListOutgoingCertificatesResponseTypeDef = TypedDict(
    "_ClientListOutgoingCertificatesResponseTypeDef",
    {
        "outgoingCertificates": List[
            ClientListOutgoingCertificatesResponseoutgoingCertificatesTypeDef
        ],
        "nextMarker": str,
    },
    total=False,
)


class ClientListOutgoingCertificatesResponseTypeDef(
    _ClientListOutgoingCertificatesResponseTypeDef
):
    """
    Type definition for `ClientListOutgoingCertificates` `Response`

    The output from the ListOutgoingCertificates operation.

    - **outgoingCertificates** *(list) --*

      The certificates that are being transferred but not yet accepted.

      - *(dict) --*

        A certificate that has been transferred but not yet accepted.

        - **certificateArn** *(string) --*

          The certificate ARN.

        - **certificateId** *(string) --*

          The certificate ID.

        - **transferredTo** *(string) --*

          The AWS account to which the transfer was made.

        - **transferDate** *(datetime) --*

          The date the transfer was initiated.

        - **transferMessage** *(string) --*

          The transfer message.

        - **creationDate** *(datetime) --*

          The certificate creation date.

    - **nextMarker** *(string) --*

      The marker for the next set of results.
    """


_ClientListPoliciesResponsepoliciesTypeDef = TypedDict(
    "_ClientListPoliciesResponsepoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)


class ClientListPoliciesResponsepoliciesTypeDef(
    _ClientListPoliciesResponsepoliciesTypeDef
):
    """
    Type definition for `ClientListPoliciesResponse` `policies`

    Describes an AWS IoT policy.

    - **policyName** *(string) --*

      The policy name.

    - **policyArn** *(string) --*

      The policy ARN.
    """


_ClientListPoliciesResponseTypeDef = TypedDict(
    "_ClientListPoliciesResponseTypeDef",
    {"policies": List[ClientListPoliciesResponsepoliciesTypeDef], "nextMarker": str},
    total=False,
)


class ClientListPoliciesResponseTypeDef(_ClientListPoliciesResponseTypeDef):
    """
    Type definition for `ClientListPolicies` `Response`

    The output from the ListPolicies operation.

    - **policies** *(list) --*

      The descriptions of the policies.

      - *(dict) --*

        Describes an AWS IoT policy.

        - **policyName** *(string) --*

          The policy name.

        - **policyArn** *(string) --*

          The policy ARN.

    - **nextMarker** *(string) --*

      The marker for the next set of results, or null if there are no additional results.
    """


_ClientListPolicyPrincipalsResponseTypeDef = TypedDict(
    "_ClientListPolicyPrincipalsResponseTypeDef",
    {"principals": List[str], "nextMarker": str},
    total=False,
)


class ClientListPolicyPrincipalsResponseTypeDef(
    _ClientListPolicyPrincipalsResponseTypeDef
):
    """
    Type definition for `ClientListPolicyPrincipals` `Response`

    The output from the ListPolicyPrincipals operation.

    - **principals** *(list) --*

      The descriptions of the principals.

      - *(string) --*

    - **nextMarker** *(string) --*

      The marker for the next set of results, or null if there are no additional results.
    """


_ClientListPolicyVersionsResponsepolicyVersionsTypeDef = TypedDict(
    "_ClientListPolicyVersionsResponsepolicyVersionsTypeDef",
    {"versionId": str, "isDefaultVersion": bool, "createDate": datetime},
    total=False,
)


class ClientListPolicyVersionsResponsepolicyVersionsTypeDef(
    _ClientListPolicyVersionsResponsepolicyVersionsTypeDef
):
    """
    Type definition for `ClientListPolicyVersionsResponse` `policyVersions`

    Describes a policy version.

    - **versionId** *(string) --*

      The policy version ID.

    - **isDefaultVersion** *(boolean) --*

      Specifies whether the policy version is the default.

    - **createDate** *(datetime) --*

      The date and time the policy was created.
    """


_ClientListPolicyVersionsResponseTypeDef = TypedDict(
    "_ClientListPolicyVersionsResponseTypeDef",
    {"policyVersions": List[ClientListPolicyVersionsResponsepolicyVersionsTypeDef]},
    total=False,
)


class ClientListPolicyVersionsResponseTypeDef(_ClientListPolicyVersionsResponseTypeDef):
    """
    Type definition for `ClientListPolicyVersions` `Response`

    The output from the ListPolicyVersions operation.

    - **policyVersions** *(list) --*

      The policy versions.

      - *(dict) --*

        Describes a policy version.

        - **versionId** *(string) --*

          The policy version ID.

        - **isDefaultVersion** *(boolean) --*

          Specifies whether the policy version is the default.

        - **createDate** *(datetime) --*

          The date and time the policy was created.
    """


_ClientListPrincipalPoliciesResponsepoliciesTypeDef = TypedDict(
    "_ClientListPrincipalPoliciesResponsepoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)


class ClientListPrincipalPoliciesResponsepoliciesTypeDef(
    _ClientListPrincipalPoliciesResponsepoliciesTypeDef
):
    """
    Type definition for `ClientListPrincipalPoliciesResponse` `policies`

    Describes an AWS IoT policy.

    - **policyName** *(string) --*

      The policy name.

    - **policyArn** *(string) --*

      The policy ARN.
    """


_ClientListPrincipalPoliciesResponseTypeDef = TypedDict(
    "_ClientListPrincipalPoliciesResponseTypeDef",
    {
        "policies": List[ClientListPrincipalPoliciesResponsepoliciesTypeDef],
        "nextMarker": str,
    },
    total=False,
)


class ClientListPrincipalPoliciesResponseTypeDef(
    _ClientListPrincipalPoliciesResponseTypeDef
):
    """
    Type definition for `ClientListPrincipalPolicies` `Response`

    The output from the ListPrincipalPolicies operation.

    - **policies** *(list) --*

      The policies.

      - *(dict) --*

        Describes an AWS IoT policy.

        - **policyName** *(string) --*

          The policy name.

        - **policyArn** *(string) --*

          The policy ARN.

    - **nextMarker** *(string) --*

      The marker for the next set of results, or null if there are no additional results.
    """


_ClientListPrincipalThingsResponseTypeDef = TypedDict(
    "_ClientListPrincipalThingsResponseTypeDef",
    {"things": List[str], "nextToken": str},
    total=False,
)


class ClientListPrincipalThingsResponseTypeDef(
    _ClientListPrincipalThingsResponseTypeDef
):
    """
    Type definition for `ClientListPrincipalThings` `Response`

    The output from the ListPrincipalThings operation.

    - **things** *(list) --*

      The things.

      - *(string) --*

    - **nextToken** *(string) --*

      The token used to get the next set of results, or **null** if there are no additional results.
    """


_ClientListRoleAliasesResponseTypeDef = TypedDict(
    "_ClientListRoleAliasesResponseTypeDef",
    {"roleAliases": List[str], "nextMarker": str},
    total=False,
)


class ClientListRoleAliasesResponseTypeDef(_ClientListRoleAliasesResponseTypeDef):
    """
    Type definition for `ClientListRoleAliases` `Response`

    - **roleAliases** *(list) --*

      The role aliases.

      - *(string) --*

    - **nextMarker** *(string) --*

      A marker used to get the next set of results.
    """


_ClientListScheduledAuditsResponsescheduledAuditsTypeDef = TypedDict(
    "_ClientListScheduledAuditsResponsescheduledAuditsTypeDef",
    {
        "scheduledAuditName": str,
        "scheduledAuditArn": str,
        "frequency": str,
        "dayOfMonth": str,
        "dayOfWeek": str,
    },
    total=False,
)


class ClientListScheduledAuditsResponsescheduledAuditsTypeDef(
    _ClientListScheduledAuditsResponsescheduledAuditsTypeDef
):
    """
    Type definition for `ClientListScheduledAuditsResponse` `scheduledAudits`

    Information about the scheduled audit.

    - **scheduledAuditName** *(string) --*

      The name of the scheduled audit.

    - **scheduledAuditArn** *(string) --*

      The ARN of the scheduled audit.

    - **frequency** *(string) --*

      How often the scheduled audit occurs.

    - **dayOfMonth** *(string) --*

      The day of the month on which the scheduled audit is run (if the ``frequency`` is
      "MONTHLY"). If days 29-31 are specified, and the month does not have that many days, the
      audit takes place on the "LAST" day of the month.

    - **dayOfWeek** *(string) --*

      The day of the week on which the scheduled audit is run (if the ``frequency`` is "WEEKLY"
      or "BIWEEKLY").
    """


_ClientListScheduledAuditsResponseTypeDef = TypedDict(
    "_ClientListScheduledAuditsResponseTypeDef",
    {
        "scheduledAudits": List[
            ClientListScheduledAuditsResponsescheduledAuditsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListScheduledAuditsResponseTypeDef(
    _ClientListScheduledAuditsResponseTypeDef
):
    """
    Type definition for `ClientListScheduledAudits` `Response`

    - **scheduledAudits** *(list) --*

      The list of scheduled audits.

      - *(dict) --*

        Information about the scheduled audit.

        - **scheduledAuditName** *(string) --*

          The name of the scheduled audit.

        - **scheduledAuditArn** *(string) --*

          The ARN of the scheduled audit.

        - **frequency** *(string) --*

          How often the scheduled audit occurs.

        - **dayOfMonth** *(string) --*

          The day of the month on which the scheduled audit is run (if the ``frequency`` is
          "MONTHLY"). If days 29-31 are specified, and the month does not have that many days, the
          audit takes place on the "LAST" day of the month.

        - **dayOfWeek** *(string) --*

          The day of the week on which the scheduled audit is run (if the ``frequency`` is "WEEKLY"
          or "BIWEEKLY").

    - **nextToken** *(string) --*

      A token that can be used to retrieve the next set of results, or ``null`` if there are no
      additional results.
    """


_ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef = TypedDict(
    "_ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef",
    {"name": str, "arn": str},
    total=False,
)


class ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef(
    _ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef
):
    """
    Type definition for `ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappings` `securityProfileIdentifier`

    Information that identifies the security profile.

    - **name** *(string) --*

      The name you have given to the security profile.

    - **arn** *(string) --*

      The ARN of the security profile.
    """


_ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingstargetTypeDef = TypedDict(
    "_ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingstargetTypeDef",
    {"arn": str},
    total=False,
)


class ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingstargetTypeDef(
    _ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingstargetTypeDef
):
    """
    Type definition for `ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappings` `target`

    Information about the target (thing group) associated with the security profile.

    - **arn** *(string) --*

      The ARN of the security profile.
    """


_ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingsTypeDef = TypedDict(
    "_ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingsTypeDef",
    {
        "securityProfileIdentifier": ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef,
        "target": ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingstargetTypeDef,
    },
    total=False,
)


class ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingsTypeDef(
    _ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingsTypeDef
):
    """
    Type definition for `ClientListSecurityProfilesForTargetResponse` `securityProfileTargetMappings`

    Information about a security profile and the target associated with it.

    - **securityProfileIdentifier** *(dict) --*

      Information that identifies the security profile.

      - **name** *(string) --*

        The name you have given to the security profile.

      - **arn** *(string) --*

        The ARN of the security profile.

    - **target** *(dict) --*

      Information about the target (thing group) associated with the security profile.

      - **arn** *(string) --*

        The ARN of the security profile.
    """


_ClientListSecurityProfilesForTargetResponseTypeDef = TypedDict(
    "_ClientListSecurityProfilesForTargetResponseTypeDef",
    {
        "securityProfileTargetMappings": List[
            ClientListSecurityProfilesForTargetResponsesecurityProfileTargetMappingsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListSecurityProfilesForTargetResponseTypeDef(
    _ClientListSecurityProfilesForTargetResponseTypeDef
):
    """
    Type definition for `ClientListSecurityProfilesForTarget` `Response`

    - **securityProfileTargetMappings** *(list) --*

      A list of security profiles and their associated targets.

      - *(dict) --*

        Information about a security profile and the target associated with it.

        - **securityProfileIdentifier** *(dict) --*

          Information that identifies the security profile.

          - **name** *(string) --*

            The name you have given to the security profile.

          - **arn** *(string) --*

            The ARN of the security profile.

        - **target** *(dict) --*

          Information about the target (thing group) associated with the security profile.

          - **arn** *(string) --*

            The ARN of the security profile.

    - **nextToken** *(string) --*

      A token that can be used to retrieve the next set of results, or ``null`` if there are no
      additional results.
    """


_ClientListSecurityProfilesResponsesecurityProfileIdentifiersTypeDef = TypedDict(
    "_ClientListSecurityProfilesResponsesecurityProfileIdentifiersTypeDef",
    {"name": str, "arn": str},
    total=False,
)


class ClientListSecurityProfilesResponsesecurityProfileIdentifiersTypeDef(
    _ClientListSecurityProfilesResponsesecurityProfileIdentifiersTypeDef
):
    """
    Type definition for `ClientListSecurityProfilesResponse` `securityProfileIdentifiers`

    Identifying information for a Device Defender security profile.

    - **name** *(string) --*

      The name you have given to the security profile.

    - **arn** *(string) --*

      The ARN of the security profile.
    """


_ClientListSecurityProfilesResponseTypeDef = TypedDict(
    "_ClientListSecurityProfilesResponseTypeDef",
    {
        "securityProfileIdentifiers": List[
            ClientListSecurityProfilesResponsesecurityProfileIdentifiersTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListSecurityProfilesResponseTypeDef(
    _ClientListSecurityProfilesResponseTypeDef
):
    """
    Type definition for `ClientListSecurityProfiles` `Response`

    - **securityProfileIdentifiers** *(list) --*

      A list of security profile identifiers (names and ARNs).

      - *(dict) --*

        Identifying information for a Device Defender security profile.

        - **name** *(string) --*

          The name you have given to the security profile.

        - **arn** *(string) --*

          The ARN of the security profile.

    - **nextToken** *(string) --*

      A token that can be used to retrieve the next set of results, or ``null`` if there are no
      additional results.
    """


_ClientListStreamsResponsestreamsTypeDef = TypedDict(
    "_ClientListStreamsResponsestreamsTypeDef",
    {"streamId": str, "streamArn": str, "streamVersion": int, "description": str},
    total=False,
)


class ClientListStreamsResponsestreamsTypeDef(_ClientListStreamsResponsestreamsTypeDef):
    """
    Type definition for `ClientListStreamsResponse` `streams`

    A summary of a stream.

    - **streamId** *(string) --*

      The stream ID.

    - **streamArn** *(string) --*

      The stream ARN.

    - **streamVersion** *(integer) --*

      The stream version.

    - **description** *(string) --*

      A description of the stream.
    """


_ClientListStreamsResponseTypeDef = TypedDict(
    "_ClientListStreamsResponseTypeDef",
    {"streams": List[ClientListStreamsResponsestreamsTypeDef], "nextToken": str},
    total=False,
)


class ClientListStreamsResponseTypeDef(_ClientListStreamsResponseTypeDef):
    """
    Type definition for `ClientListStreams` `Response`

    - **streams** *(list) --*

      A list of streams.

      - *(dict) --*

        A summary of a stream.

        - **streamId** *(string) --*

          The stream ID.

        - **streamArn** *(string) --*

          The stream ARN.

        - **streamVersion** *(integer) --*

          The stream version.

        - **description** *(string) --*

          A description of the stream.

    - **nextToken** *(string) --*

      A token used to get the next set of results.
    """


_ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "_ClientListTagsForResourceResponsetagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ClientListTagsForResourceResponsetagsTypeDef(
    _ClientListTagsForResourceResponsetagsTypeDef
):
    """
    Type definition for `ClientListTagsForResourceResponse` `tags`

    A set of key/value pairs that are used to manage the resource.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef",
    {"tags": List[ClientListTagsForResourceResponsetagsTypeDef], "nextToken": str},
    total=False,
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **tags** *(list) --*

      The list of tags assigned to the resource.

      - *(dict) --*

        A set of key/value pairs that are used to manage the resource.

        - **Key** *(string) --*

          The tag's key.

        - **Value** *(string) --*

          The tag's value.

    - **nextToken** *(string) --*

      The token used to get the next set of results, or **null** if there are no additional results.
    """


_ClientListTargetsForPolicyResponseTypeDef = TypedDict(
    "_ClientListTargetsForPolicyResponseTypeDef",
    {"targets": List[str], "nextMarker": str},
    total=False,
)


class ClientListTargetsForPolicyResponseTypeDef(
    _ClientListTargetsForPolicyResponseTypeDef
):
    """
    Type definition for `ClientListTargetsForPolicy` `Response`

    - **targets** *(list) --*

      The policy targets.

      - *(string) --*

    - **nextMarker** *(string) --*

      A marker used to get the next set of results.
    """


_ClientListTargetsForSecurityProfileResponsesecurityProfileTargetsTypeDef = TypedDict(
    "_ClientListTargetsForSecurityProfileResponsesecurityProfileTargetsTypeDef",
    {"arn": str},
    total=False,
)


class ClientListTargetsForSecurityProfileResponsesecurityProfileTargetsTypeDef(
    _ClientListTargetsForSecurityProfileResponsesecurityProfileTargetsTypeDef
):
    """
    Type definition for `ClientListTargetsForSecurityProfileResponse` `securityProfileTargets`

    A target to which an alert is sent when a security profile behavior is violated.

    - **arn** *(string) --*

      The ARN of the security profile.
    """


_ClientListTargetsForSecurityProfileResponseTypeDef = TypedDict(
    "_ClientListTargetsForSecurityProfileResponseTypeDef",
    {
        "securityProfileTargets": List[
            ClientListTargetsForSecurityProfileResponsesecurityProfileTargetsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListTargetsForSecurityProfileResponseTypeDef(
    _ClientListTargetsForSecurityProfileResponseTypeDef
):
    """
    Type definition for `ClientListTargetsForSecurityProfile` `Response`

    - **securityProfileTargets** *(list) --*

      The thing groups to which the security profile is attached.

      - *(dict) --*

        A target to which an alert is sent when a security profile behavior is violated.

        - **arn** *(string) --*

          The ARN of the security profile.

    - **nextToken** *(string) --*

      A token that can be used to retrieve the next set of results, or ``null`` if there are no
      additional results.
    """


_ClientListThingGroupsForThingResponsethingGroupsTypeDef = TypedDict(
    "_ClientListThingGroupsForThingResponsethingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)


class ClientListThingGroupsForThingResponsethingGroupsTypeDef(
    _ClientListThingGroupsForThingResponsethingGroupsTypeDef
):
    """
    Type definition for `ClientListThingGroupsForThingResponse` `thingGroups`

    The name and ARN of a group.

    - **groupName** *(string) --*

      The group name.

    - **groupArn** *(string) --*

      The group ARN.
    """


_ClientListThingGroupsForThingResponseTypeDef = TypedDict(
    "_ClientListThingGroupsForThingResponseTypeDef",
    {
        "thingGroups": List[ClientListThingGroupsForThingResponsethingGroupsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListThingGroupsForThingResponseTypeDef(
    _ClientListThingGroupsForThingResponseTypeDef
):
    """
    Type definition for `ClientListThingGroupsForThing` `Response`

    - **thingGroups** *(list) --*

      The thing groups.

      - *(dict) --*

        The name and ARN of a group.

        - **groupName** *(string) --*

          The group name.

        - **groupArn** *(string) --*

          The group ARN.

    - **nextToken** *(string) --*

      The token used to get the next set of results, or **null** if there are no additional results.
    """


_ClientListThingGroupsResponsethingGroupsTypeDef = TypedDict(
    "_ClientListThingGroupsResponsethingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)


class ClientListThingGroupsResponsethingGroupsTypeDef(
    _ClientListThingGroupsResponsethingGroupsTypeDef
):
    """
    Type definition for `ClientListThingGroupsResponse` `thingGroups`

    The name and ARN of a group.

    - **groupName** *(string) --*

      The group name.

    - **groupArn** *(string) --*

      The group ARN.
    """


_ClientListThingGroupsResponseTypeDef = TypedDict(
    "_ClientListThingGroupsResponseTypeDef",
    {
        "thingGroups": List[ClientListThingGroupsResponsethingGroupsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListThingGroupsResponseTypeDef(_ClientListThingGroupsResponseTypeDef):
    """
    Type definition for `ClientListThingGroups` `Response`

    - **thingGroups** *(list) --*

      The thing groups.

      - *(dict) --*

        The name and ARN of a group.

        - **groupName** *(string) --*

          The group name.

        - **groupArn** *(string) --*

          The group ARN.

    - **nextToken** *(string) --*

      The token used to get the next set of results, or **null** if there are no additional results.
    """


_ClientListThingPrincipalsResponseTypeDef = TypedDict(
    "_ClientListThingPrincipalsResponseTypeDef", {"principals": List[str]}, total=False
)


class ClientListThingPrincipalsResponseTypeDef(
    _ClientListThingPrincipalsResponseTypeDef
):
    """
    Type definition for `ClientListThingPrincipals` `Response`

    The output from the ListThingPrincipals operation.

    - **principals** *(list) --*

      The principals associated with the thing.

      - *(string) --*
    """


_ClientListThingRegistrationTaskReportsResponseTypeDef = TypedDict(
    "_ClientListThingRegistrationTaskReportsResponseTypeDef",
    {"resourceLinks": List[str], "reportType": str, "nextToken": str},
    total=False,
)


class ClientListThingRegistrationTaskReportsResponseTypeDef(
    _ClientListThingRegistrationTaskReportsResponseTypeDef
):
    """
    Type definition for `ClientListThingRegistrationTaskReports` `Response`

    - **resourceLinks** *(list) --*

      Links to the task resources.

      - *(string) --*

    - **reportType** *(string) --*

      The type of task report.

    - **nextToken** *(string) --*

      The token used to get the next set of results, or **null** if there are no additional results.
    """


_ClientListThingRegistrationTasksResponseTypeDef = TypedDict(
    "_ClientListThingRegistrationTasksResponseTypeDef",
    {"taskIds": List[str], "nextToken": str},
    total=False,
)


class ClientListThingRegistrationTasksResponseTypeDef(
    _ClientListThingRegistrationTasksResponseTypeDef
):
    """
    Type definition for `ClientListThingRegistrationTasks` `Response`

    - **taskIds** *(list) --*

      A list of bulk thing provisioning task IDs.

      - *(string) --*

    - **nextToken** *(string) --*

      The token used to get the next set of results, or **null** if there are no additional results.
    """


_ClientListThingTypesResponsethingTypesthingTypeMetadataTypeDef = TypedDict(
    "_ClientListThingTypesResponsethingTypesthingTypeMetadataTypeDef",
    {"deprecated": bool, "deprecationDate": datetime, "creationDate": datetime},
    total=False,
)


class ClientListThingTypesResponsethingTypesthingTypeMetadataTypeDef(
    _ClientListThingTypesResponsethingTypesthingTypeMetadataTypeDef
):
    """
    Type definition for `ClientListThingTypesResponsethingTypes` `thingTypeMetadata`

    The ThingTypeMetadata contains additional information about the thing type including:
    creation date and time, a value indicating whether the thing type is deprecated, and a
    date and time when it was deprecated.

    - **deprecated** *(boolean) --*

      Whether the thing type is deprecated. If **true** , no new things could be associated
      with this type.

    - **deprecationDate** *(datetime) --*

      The date and time when the thing type was deprecated.

    - **creationDate** *(datetime) --*

      The date and time when the thing type was created.
    """


_ClientListThingTypesResponsethingTypesthingTypePropertiesTypeDef = TypedDict(
    "_ClientListThingTypesResponsethingTypesthingTypePropertiesTypeDef",
    {"thingTypeDescription": str, "searchableAttributes": List[str]},
    total=False,
)


class ClientListThingTypesResponsethingTypesthingTypePropertiesTypeDef(
    _ClientListThingTypesResponsethingTypesthingTypePropertiesTypeDef
):
    """
    Type definition for `ClientListThingTypesResponsethingTypes` `thingTypeProperties`

    The ThingTypeProperties for the thing type.

    - **thingTypeDescription** *(string) --*

      The description of the thing type.

    - **searchableAttributes** *(list) --*

      A list of searchable thing attribute names.

      - *(string) --*
    """


_ClientListThingTypesResponsethingTypesTypeDef = TypedDict(
    "_ClientListThingTypesResponsethingTypesTypeDef",
    {
        "thingTypeName": str,
        "thingTypeArn": str,
        "thingTypeProperties": ClientListThingTypesResponsethingTypesthingTypePropertiesTypeDef,
        "thingTypeMetadata": ClientListThingTypesResponsethingTypesthingTypeMetadataTypeDef,
    },
    total=False,
)


class ClientListThingTypesResponsethingTypesTypeDef(
    _ClientListThingTypesResponsethingTypesTypeDef
):
    """
    Type definition for `ClientListThingTypesResponse` `thingTypes`

    The definition of the thing type, including thing type name and description.

    - **thingTypeName** *(string) --*

      The name of the thing type.

    - **thingTypeArn** *(string) --*

      The thing type ARN.

    - **thingTypeProperties** *(dict) --*

      The ThingTypeProperties for the thing type.

      - **thingTypeDescription** *(string) --*

        The description of the thing type.

      - **searchableAttributes** *(list) --*

        A list of searchable thing attribute names.

        - *(string) --*

    - **thingTypeMetadata** *(dict) --*

      The ThingTypeMetadata contains additional information about the thing type including:
      creation date and time, a value indicating whether the thing type is deprecated, and a
      date and time when it was deprecated.

      - **deprecated** *(boolean) --*

        Whether the thing type is deprecated. If **true** , no new things could be associated
        with this type.

      - **deprecationDate** *(datetime) --*

        The date and time when the thing type was deprecated.

      - **creationDate** *(datetime) --*

        The date and time when the thing type was created.
    """


_ClientListThingTypesResponseTypeDef = TypedDict(
    "_ClientListThingTypesResponseTypeDef",
    {
        "thingTypes": List[ClientListThingTypesResponsethingTypesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListThingTypesResponseTypeDef(_ClientListThingTypesResponseTypeDef):
    """
    Type definition for `ClientListThingTypes` `Response`

    The output for the ListThingTypes operation.

    - **thingTypes** *(list) --*

      The thing types.

      - *(dict) --*

        The definition of the thing type, including thing type name and description.

        - **thingTypeName** *(string) --*

          The name of the thing type.

        - **thingTypeArn** *(string) --*

          The thing type ARN.

        - **thingTypeProperties** *(dict) --*

          The ThingTypeProperties for the thing type.

          - **thingTypeDescription** *(string) --*

            The description of the thing type.

          - **searchableAttributes** *(list) --*

            A list of searchable thing attribute names.

            - *(string) --*

        - **thingTypeMetadata** *(dict) --*

          The ThingTypeMetadata contains additional information about the thing type including:
          creation date and time, a value indicating whether the thing type is deprecated, and a
          date and time when it was deprecated.

          - **deprecated** *(boolean) --*

            Whether the thing type is deprecated. If **true** , no new things could be associated
            with this type.

          - **deprecationDate** *(datetime) --*

            The date and time when the thing type was deprecated.

          - **creationDate** *(datetime) --*

            The date and time when the thing type was created.

    - **nextToken** *(string) --*

      The token for the next set of results, or **null** if there are no additional results.
    """


_ClientListThingsInBillingGroupResponseTypeDef = TypedDict(
    "_ClientListThingsInBillingGroupResponseTypeDef",
    {"things": List[str], "nextToken": str},
    total=False,
)


class ClientListThingsInBillingGroupResponseTypeDef(
    _ClientListThingsInBillingGroupResponseTypeDef
):
    """
    Type definition for `ClientListThingsInBillingGroup` `Response`

    - **things** *(list) --*

      A list of things in the billing group.

      - *(string) --*

    - **nextToken** *(string) --*

      The token used to get the next set of results, or **null** if there are no additional results.
    """


_ClientListThingsInThingGroupResponseTypeDef = TypedDict(
    "_ClientListThingsInThingGroupResponseTypeDef",
    {"things": List[str], "nextToken": str},
    total=False,
)


class ClientListThingsInThingGroupResponseTypeDef(
    _ClientListThingsInThingGroupResponseTypeDef
):
    """
    Type definition for `ClientListThingsInThingGroup` `Response`

    - **things** *(list) --*

      The things in the specified thing group.

      - *(string) --*

    - **nextToken** *(string) --*

      The token used to get the next set of results, or **null** if there are no additional results.
    """


_ClientListThingsResponsethingsTypeDef = TypedDict(
    "_ClientListThingsResponsethingsTypeDef",
    {
        "thingName": str,
        "thingTypeName": str,
        "thingArn": str,
        "attributes": Dict[str, str],
        "version": int,
    },
    total=False,
)


class ClientListThingsResponsethingsTypeDef(_ClientListThingsResponsethingsTypeDef):
    """
    Type definition for `ClientListThingsResponse` `things`

    The properties of the thing, including thing name, thing type name, and a list of thing
    attributes.

    - **thingName** *(string) --*

      The name of the thing.

    - **thingTypeName** *(string) --*

      The name of the thing type, if the thing has been associated with a type.

    - **thingArn** *(string) --*

      The thing ARN.

    - **attributes** *(dict) --*

      A list of thing attributes which are name-value pairs.

      - *(string) --*

        - *(string) --*

    - **version** *(integer) --*

      The version of the thing record in the registry.
    """


_ClientListThingsResponseTypeDef = TypedDict(
    "_ClientListThingsResponseTypeDef",
    {"things": List[ClientListThingsResponsethingsTypeDef], "nextToken": str},
    total=False,
)


class ClientListThingsResponseTypeDef(_ClientListThingsResponseTypeDef):
    """
    Type definition for `ClientListThings` `Response`

    The output from the ListThings operation.

    - **things** *(list) --*

      The things.

      - *(dict) --*

        The properties of the thing, including thing name, thing type name, and a list of thing
        attributes.

        - **thingName** *(string) --*

          The name of the thing.

        - **thingTypeName** *(string) --*

          The name of the thing type, if the thing has been associated with a type.

        - **thingArn** *(string) --*

          The thing ARN.

        - **attributes** *(dict) --*

          A list of thing attributes which are name-value pairs.

          - *(string) --*

            - *(string) --*

        - **version** *(integer) --*

          The version of the thing record in the registry.

    - **nextToken** *(string) --*

      The token used to get the next set of results, or **null** if there are no additional results.
    """


_ClientListTopicRulesResponserulesTypeDef = TypedDict(
    "_ClientListTopicRulesResponserulesTypeDef",
    {
        "ruleArn": str,
        "ruleName": str,
        "topicPattern": str,
        "createdAt": datetime,
        "ruleDisabled": bool,
    },
    total=False,
)


class ClientListTopicRulesResponserulesTypeDef(
    _ClientListTopicRulesResponserulesTypeDef
):
    """
    Type definition for `ClientListTopicRulesResponse` `rules`

    Describes a rule.

    - **ruleArn** *(string) --*

      The rule ARN.

    - **ruleName** *(string) --*

      The name of the rule.

    - **topicPattern** *(string) --*

      The pattern for the topic names that apply.

    - **createdAt** *(datetime) --*

      The date and time the rule was created.

    - **ruleDisabled** *(boolean) --*

      Specifies whether the rule is disabled.
    """


_ClientListTopicRulesResponseTypeDef = TypedDict(
    "_ClientListTopicRulesResponseTypeDef",
    {"rules": List[ClientListTopicRulesResponserulesTypeDef], "nextToken": str},
    total=False,
)


class ClientListTopicRulesResponseTypeDef(_ClientListTopicRulesResponseTypeDef):
    """
    Type definition for `ClientListTopicRules` `Response`

    The output from the ListTopicRules operation.

    - **rules** *(list) --*

      The rules.

      - *(dict) --*

        Describes a rule.

        - **ruleArn** *(string) --*

          The rule ARN.

        - **ruleName** *(string) --*

          The name of the rule.

        - **topicPattern** *(string) --*

          The pattern for the topic names that apply.

        - **createdAt** *(datetime) --*

          The date and time the rule was created.

        - **ruleDisabled** *(boolean) --*

          Specifies whether the rule is disabled.

    - **nextToken** *(string) --*

      A token used to retrieve the next value.
    """


_ClientListV2LoggingLevelsResponselogTargetConfigurationslogTargetTypeDef = TypedDict(
    "_ClientListV2LoggingLevelsResponselogTargetConfigurationslogTargetTypeDef",
    {"targetType": str, "targetName": str},
    total=False,
)


class ClientListV2LoggingLevelsResponselogTargetConfigurationslogTargetTypeDef(
    _ClientListV2LoggingLevelsResponselogTargetConfigurationslogTargetTypeDef
):
    """
    Type definition for `ClientListV2LoggingLevelsResponselogTargetConfigurations` `logTarget`

    A log target

    - **targetType** *(string) --*

      The target type.

    - **targetName** *(string) --*

      The target name.
    """


_ClientListV2LoggingLevelsResponselogTargetConfigurationsTypeDef = TypedDict(
    "_ClientListV2LoggingLevelsResponselogTargetConfigurationsTypeDef",
    {
        "logTarget": ClientListV2LoggingLevelsResponselogTargetConfigurationslogTargetTypeDef,
        "logLevel": str,
    },
    total=False,
)


class ClientListV2LoggingLevelsResponselogTargetConfigurationsTypeDef(
    _ClientListV2LoggingLevelsResponselogTargetConfigurationsTypeDef
):
    """
    Type definition for `ClientListV2LoggingLevelsResponse` `logTargetConfigurations`

    The target configuration.

    - **logTarget** *(dict) --*

      A log target

      - **targetType** *(string) --*

        The target type.

      - **targetName** *(string) --*

        The target name.

    - **logLevel** *(string) --*

      The logging level.
    """


_ClientListV2LoggingLevelsResponseTypeDef = TypedDict(
    "_ClientListV2LoggingLevelsResponseTypeDef",
    {
        "logTargetConfigurations": List[
            ClientListV2LoggingLevelsResponselogTargetConfigurationsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListV2LoggingLevelsResponseTypeDef(
    _ClientListV2LoggingLevelsResponseTypeDef
):
    """
    Type definition for `ClientListV2LoggingLevels` `Response`

    - **logTargetConfigurations** *(list) --*

      The logging configuration for a target.

      - *(dict) --*

        The target configuration.

        - **logTarget** *(dict) --*

          A log target

          - **targetType** *(string) --*

            The target type.

          - **targetName** *(string) --*

            The target name.

        - **logLevel** *(string) --*

          The logging level.

    - **nextToken** *(string) --*

      The token used to get the next set of results, or **null** if there are no additional results.
    """


_ClientListViolationEventsResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef = TypedDict(
    "_ClientListViolationEventsResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)


class ClientListViolationEventsResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef(
    _ClientListViolationEventsResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef
):
    """
    Type definition for `ClientListViolationEventsResponseviolationEventsbehaviorcriteria` `statisticalThreshold`

    A statistical ranking (percentile) which indicates a threshold value by which a
    behavior is determined to be in compliance or in violation of the behavior.

    - **statistic** *(string) --*

      The percentile which resolves to a threshold value by which compliance with a
      behavior is determined. Metrics are collected over the specified period
      (``durationSeconds`` ) from all reporting devices in your account and statistical
      ranks are calculated. Then, the measurements from a device are collected over the
      same period. If the accumulated measurements from the device fall above or below
      (``comparisonOperator`` ) the value associated with the percentile specified, then
      the device is considered to be in compliance with the behavior, otherwise a
      violation occurs.
    """


_ClientListViolationEventsResponseviolationEventsbehaviorcriteriavalueTypeDef = TypedDict(
    "_ClientListViolationEventsResponseviolationEventsbehaviorcriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ClientListViolationEventsResponseviolationEventsbehaviorcriteriavalueTypeDef(
    _ClientListViolationEventsResponseviolationEventsbehaviorcriteriavalueTypeDef
):
    """
    Type definition for `ClientListViolationEventsResponseviolationEventsbehaviorcriteria` `value`

    The value to be compared with the ``metric`` .

    - **count** *(integer) --*

      If the ``comparisonOperator`` calls for a numeric value, use this to specify that
      numeric value to be compared with the ``metric`` .

    - **cidrs** *(list) --*

      If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
      set to be compared with the ``metric`` .

      - *(string) --*

    - **ports** *(list) --*

      If the ``comparisonOperator`` calls for a set of ports, use this to specify that
      set to be compared with the ``metric`` .

      - *(integer) --*
    """


_ClientListViolationEventsResponseviolationEventsbehaviorcriteriaTypeDef = TypedDict(
    "_ClientListViolationEventsResponseviolationEventsbehaviorcriteriaTypeDef",
    {
        "comparisonOperator": str,
        "value": ClientListViolationEventsResponseviolationEventsbehaviorcriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientListViolationEventsResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef,
    },
    total=False,
)


class ClientListViolationEventsResponseviolationEventsbehaviorcriteriaTypeDef(
    _ClientListViolationEventsResponseviolationEventsbehaviorcriteriaTypeDef
):
    """
    Type definition for `ClientListViolationEventsResponseviolationEventsbehavior` `criteria`

    The criteria that determine if a device is behaving normally in regard to the
    ``metric`` .

    - **comparisonOperator** *(string) --*

      The operator that relates the thing measured (``metric`` ) to the criteria
      (containing a ``value`` or ``statisticalThreshold`` ).

    - **value** *(dict) --*

      The value to be compared with the ``metric`` .

      - **count** *(integer) --*

        If the ``comparisonOperator`` calls for a numeric value, use this to specify that
        numeric value to be compared with the ``metric`` .

      - **cidrs** *(list) --*

        If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
        set to be compared with the ``metric`` .

        - *(string) --*

      - **ports** *(list) --*

        If the ``comparisonOperator`` calls for a set of ports, use this to specify that
        set to be compared with the ``metric`` .

        - *(integer) --*

    - **durationSeconds** *(integer) --*

      Use this to specify the time duration over which the behavior is evaluated, for those
      criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
      ``statisticalThreshhold`` metric comparison, measurements from all devices are
      accumulated over this time duration before being used to calculate percentiles, and
      later, measurements from an individual device are also accumulated over this time
      duration before being given a percentile rank.

    - **consecutiveDatapointsToAlarm** *(integer) --*

      If a device is in violation of the behavior for the specified number of consecutive
      datapoints, an alarm occurs. If not specified, the default is 1.

    - **consecutiveDatapointsToClear** *(integer) --*

      If an alarm has occurred and the offending device is no longer in violation of the
      behavior for the specified number of consecutive datapoints, the alarm is cleared. If
      not specified, the default is 1.

    - **statisticalThreshold** *(dict) --*

      A statistical ranking (percentile) which indicates a threshold value by which a
      behavior is determined to be in compliance or in violation of the behavior.

      - **statistic** *(string) --*

        The percentile which resolves to a threshold value by which compliance with a
        behavior is determined. Metrics are collected over the specified period
        (``durationSeconds`` ) from all reporting devices in your account and statistical
        ranks are calculated. Then, the measurements from a device are collected over the
        same period. If the accumulated measurements from the device fall above or below
        (``comparisonOperator`` ) the value associated with the percentile specified, then
        the device is considered to be in compliance with the behavior, otherwise a
        violation occurs.
    """


_ClientListViolationEventsResponseviolationEventsbehaviorTypeDef = TypedDict(
    "_ClientListViolationEventsResponseviolationEventsbehaviorTypeDef",
    {
        "name": str,
        "metric": str,
        "criteria": ClientListViolationEventsResponseviolationEventsbehaviorcriteriaTypeDef,
    },
    total=False,
)


class ClientListViolationEventsResponseviolationEventsbehaviorTypeDef(
    _ClientListViolationEventsResponseviolationEventsbehaviorTypeDef
):
    """
    Type definition for `ClientListViolationEventsResponseviolationEvents` `behavior`

    The behavior which was violated.

    - **name** *(string) --*

      The name you have given to the behavior.

    - **metric** *(string) --*

      What is measured by the behavior.

    - **criteria** *(dict) --*

      The criteria that determine if a device is behaving normally in regard to the
      ``metric`` .

      - **comparisonOperator** *(string) --*

        The operator that relates the thing measured (``metric`` ) to the criteria
        (containing a ``value`` or ``statisticalThreshold`` ).

      - **value** *(dict) --*

        The value to be compared with the ``metric`` .

        - **count** *(integer) --*

          If the ``comparisonOperator`` calls for a numeric value, use this to specify that
          numeric value to be compared with the ``metric`` .

        - **cidrs** *(list) --*

          If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
          set to be compared with the ``metric`` .

          - *(string) --*

        - **ports** *(list) --*

          If the ``comparisonOperator`` calls for a set of ports, use this to specify that
          set to be compared with the ``metric`` .

          - *(integer) --*

      - **durationSeconds** *(integer) --*

        Use this to specify the time duration over which the behavior is evaluated, for those
        criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
        ``statisticalThreshhold`` metric comparison, measurements from all devices are
        accumulated over this time duration before being used to calculate percentiles, and
        later, measurements from an individual device are also accumulated over this time
        duration before being given a percentile rank.

      - **consecutiveDatapointsToAlarm** *(integer) --*

        If a device is in violation of the behavior for the specified number of consecutive
        datapoints, an alarm occurs. If not specified, the default is 1.

      - **consecutiveDatapointsToClear** *(integer) --*

        If an alarm has occurred and the offending device is no longer in violation of the
        behavior for the specified number of consecutive datapoints, the alarm is cleared. If
        not specified, the default is 1.

      - **statisticalThreshold** *(dict) --*

        A statistical ranking (percentile) which indicates a threshold value by which a
        behavior is determined to be in compliance or in violation of the behavior.

        - **statistic** *(string) --*

          The percentile which resolves to a threshold value by which compliance with a
          behavior is determined. Metrics are collected over the specified period
          (``durationSeconds`` ) from all reporting devices in your account and statistical
          ranks are calculated. Then, the measurements from a device are collected over the
          same period. If the accumulated measurements from the device fall above or below
          (``comparisonOperator`` ) the value associated with the percentile specified, then
          the device is considered to be in compliance with the behavior, otherwise a
          violation occurs.
    """


_ClientListViolationEventsResponseviolationEventsmetricValueTypeDef = TypedDict(
    "_ClientListViolationEventsResponseviolationEventsmetricValueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ClientListViolationEventsResponseviolationEventsmetricValueTypeDef(
    _ClientListViolationEventsResponseviolationEventsmetricValueTypeDef
):
    """
    Type definition for `ClientListViolationEventsResponseviolationEvents` `metricValue`

    The value of the metric (the measurement).

    - **count** *(integer) --*

      If the ``comparisonOperator`` calls for a numeric value, use this to specify that
      numeric value to be compared with the ``metric`` .

    - **cidrs** *(list) --*

      If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
      be compared with the ``metric`` .

      - *(string) --*

    - **ports** *(list) --*

      If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
      be compared with the ``metric`` .

      - *(integer) --*
    """


_ClientListViolationEventsResponseviolationEventsTypeDef = TypedDict(
    "_ClientListViolationEventsResponseviolationEventsTypeDef",
    {
        "violationId": str,
        "thingName": str,
        "securityProfileName": str,
        "behavior": ClientListViolationEventsResponseviolationEventsbehaviorTypeDef,
        "metricValue": ClientListViolationEventsResponseviolationEventsmetricValueTypeDef,
        "violationEventType": str,
        "violationEventTime": datetime,
    },
    total=False,
)


class ClientListViolationEventsResponseviolationEventsTypeDef(
    _ClientListViolationEventsResponseviolationEventsTypeDef
):
    """
    Type definition for `ClientListViolationEventsResponse` `violationEvents`

    Information about a Device Defender security profile behavior violation.

    - **violationId** *(string) --*

      The ID of the violation event.

    - **thingName** *(string) --*

      The name of the thing responsible for the violation event.

    - **securityProfileName** *(string) --*

      The name of the security profile whose behavior was violated.

    - **behavior** *(dict) --*

      The behavior which was violated.

      - **name** *(string) --*

        The name you have given to the behavior.

      - **metric** *(string) --*

        What is measured by the behavior.

      - **criteria** *(dict) --*

        The criteria that determine if a device is behaving normally in regard to the
        ``metric`` .

        - **comparisonOperator** *(string) --*

          The operator that relates the thing measured (``metric`` ) to the criteria
          (containing a ``value`` or ``statisticalThreshold`` ).

        - **value** *(dict) --*

          The value to be compared with the ``metric`` .

          - **count** *(integer) --*

            If the ``comparisonOperator`` calls for a numeric value, use this to specify that
            numeric value to be compared with the ``metric`` .

          - **cidrs** *(list) --*

            If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
            set to be compared with the ``metric`` .

            - *(string) --*

          - **ports** *(list) --*

            If the ``comparisonOperator`` calls for a set of ports, use this to specify that
            set to be compared with the ``metric`` .

            - *(integer) --*

        - **durationSeconds** *(integer) --*

          Use this to specify the time duration over which the behavior is evaluated, for those
          criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
          ``statisticalThreshhold`` metric comparison, measurements from all devices are
          accumulated over this time duration before being used to calculate percentiles, and
          later, measurements from an individual device are also accumulated over this time
          duration before being given a percentile rank.

        - **consecutiveDatapointsToAlarm** *(integer) --*

          If a device is in violation of the behavior for the specified number of consecutive
          datapoints, an alarm occurs. If not specified, the default is 1.

        - **consecutiveDatapointsToClear** *(integer) --*

          If an alarm has occurred and the offending device is no longer in violation of the
          behavior for the specified number of consecutive datapoints, the alarm is cleared. If
          not specified, the default is 1.

        - **statisticalThreshold** *(dict) --*

          A statistical ranking (percentile) which indicates a threshold value by which a
          behavior is determined to be in compliance or in violation of the behavior.

          - **statistic** *(string) --*

            The percentile which resolves to a threshold value by which compliance with a
            behavior is determined. Metrics are collected over the specified period
            (``durationSeconds`` ) from all reporting devices in your account and statistical
            ranks are calculated. Then, the measurements from a device are collected over the
            same period. If the accumulated measurements from the device fall above or below
            (``comparisonOperator`` ) the value associated with the percentile specified, then
            the device is considered to be in compliance with the behavior, otherwise a
            violation occurs.

    - **metricValue** *(dict) --*

      The value of the metric (the measurement).

      - **count** *(integer) --*

        If the ``comparisonOperator`` calls for a numeric value, use this to specify that
        numeric value to be compared with the ``metric`` .

      - **cidrs** *(list) --*

        If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
        be compared with the ``metric`` .

        - *(string) --*

      - **ports** *(list) --*

        If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
        be compared with the ``metric`` .

        - *(integer) --*

    - **violationEventType** *(string) --*

      The type of violation event.

    - **violationEventTime** *(datetime) --*

      The time the violation event occurred.
    """


_ClientListViolationEventsResponseTypeDef = TypedDict(
    "_ClientListViolationEventsResponseTypeDef",
    {
        "violationEvents": List[
            ClientListViolationEventsResponseviolationEventsTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientListViolationEventsResponseTypeDef(
    _ClientListViolationEventsResponseTypeDef
):
    """
    Type definition for `ClientListViolationEvents` `Response`

    - **violationEvents** *(list) --*

      The security profile violation alerts issued for this account during the given time period,
      potentially filtered by security profile, behavior violated, or thing (device) violating.

      - *(dict) --*

        Information about a Device Defender security profile behavior violation.

        - **violationId** *(string) --*

          The ID of the violation event.

        - **thingName** *(string) --*

          The name of the thing responsible for the violation event.

        - **securityProfileName** *(string) --*

          The name of the security profile whose behavior was violated.

        - **behavior** *(dict) --*

          The behavior which was violated.

          - **name** *(string) --*

            The name you have given to the behavior.

          - **metric** *(string) --*

            What is measured by the behavior.

          - **criteria** *(dict) --*

            The criteria that determine if a device is behaving normally in regard to the
            ``metric`` .

            - **comparisonOperator** *(string) --*

              The operator that relates the thing measured (``metric`` ) to the criteria
              (containing a ``value`` or ``statisticalThreshold`` ).

            - **value** *(dict) --*

              The value to be compared with the ``metric`` .

              - **count** *(integer) --*

                If the ``comparisonOperator`` calls for a numeric value, use this to specify that
                numeric value to be compared with the ``metric`` .

              - **cidrs** *(list) --*

                If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
                set to be compared with the ``metric`` .

                - *(string) --*

              - **ports** *(list) --*

                If the ``comparisonOperator`` calls for a set of ports, use this to specify that
                set to be compared with the ``metric`` .

                - *(integer) --*

            - **durationSeconds** *(integer) --*

              Use this to specify the time duration over which the behavior is evaluated, for those
              criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
              ``statisticalThreshhold`` metric comparison, measurements from all devices are
              accumulated over this time duration before being used to calculate percentiles, and
              later, measurements from an individual device are also accumulated over this time
              duration before being given a percentile rank.

            - **consecutiveDatapointsToAlarm** *(integer) --*

              If a device is in violation of the behavior for the specified number of consecutive
              datapoints, an alarm occurs. If not specified, the default is 1.

            - **consecutiveDatapointsToClear** *(integer) --*

              If an alarm has occurred and the offending device is no longer in violation of the
              behavior for the specified number of consecutive datapoints, the alarm is cleared. If
              not specified, the default is 1.

            - **statisticalThreshold** *(dict) --*

              A statistical ranking (percentile) which indicates a threshold value by which a
              behavior is determined to be in compliance or in violation of the behavior.

              - **statistic** *(string) --*

                The percentile which resolves to a threshold value by which compliance with a
                behavior is determined. Metrics are collected over the specified period
                (``durationSeconds`` ) from all reporting devices in your account and statistical
                ranks are calculated. Then, the measurements from a device are collected over the
                same period. If the accumulated measurements from the device fall above or below
                (``comparisonOperator`` ) the value associated with the percentile specified, then
                the device is considered to be in compliance with the behavior, otherwise a
                violation occurs.

        - **metricValue** *(dict) --*

          The value of the metric (the measurement).

          - **count** *(integer) --*

            If the ``comparisonOperator`` calls for a numeric value, use this to specify that
            numeric value to be compared with the ``metric`` .

          - **cidrs** *(list) --*

            If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
            be compared with the ``metric`` .

            - *(string) --*

          - **ports** *(list) --*

            If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
            be compared with the ``metric`` .

            - *(integer) --*

        - **violationEventType** *(string) --*

          The type of violation event.

        - **violationEventTime** *(datetime) --*

          The time the violation event occurred.

    - **nextToken** *(string) --*

      A token that can be used to retrieve the next set of results, or ``null`` if there are no
      additional results.
    """


_ClientRegisterCaCertificateResponseTypeDef = TypedDict(
    "_ClientRegisterCaCertificateResponseTypeDef",
    {"certificateArn": str, "certificateId": str},
    total=False,
)


class ClientRegisterCaCertificateResponseTypeDef(
    _ClientRegisterCaCertificateResponseTypeDef
):
    """
    Type definition for `ClientRegisterCaCertificate` `Response`

    The output from the RegisterCACertificateResponse operation.

    - **certificateArn** *(string) --*

      The CA certificate ARN.

    - **certificateId** *(string) --*

      The CA certificate identifier.
    """


_ClientRegisterCaCertificateregistrationConfigTypeDef = TypedDict(
    "_ClientRegisterCaCertificateregistrationConfigTypeDef",
    {"templateBody": str, "roleArn": str},
    total=False,
)


class ClientRegisterCaCertificateregistrationConfigTypeDef(
    _ClientRegisterCaCertificateregistrationConfigTypeDef
):
    """
    Type definition for `ClientRegisterCaCertificate` `registrationConfig`

    Information about the registration configuration.

    - **templateBody** *(string) --*

      The template body.

    - **roleArn** *(string) --*

      The ARN of the role.
    """


_ClientRegisterCertificateResponseTypeDef = TypedDict(
    "_ClientRegisterCertificateResponseTypeDef",
    {"certificateArn": str, "certificateId": str},
    total=False,
)


class ClientRegisterCertificateResponseTypeDef(
    _ClientRegisterCertificateResponseTypeDef
):
    """
    Type definition for `ClientRegisterCertificate` `Response`

    The output from the RegisterCertificate operation.

    - **certificateArn** *(string) --*

      The certificate ARN.

    - **certificateId** *(string) --*

      The certificate identifier.
    """


_ClientRegisterThingResponseTypeDef = TypedDict(
    "_ClientRegisterThingResponseTypeDef",
    {"certificatePem": str, "resourceArns": Dict[str, str]},
    total=False,
)


class ClientRegisterThingResponseTypeDef(_ClientRegisterThingResponseTypeDef):
    """
    Type definition for `ClientRegisterThing` `Response`

    - **certificatePem** *(string) --*

      .

    - **resourceArns** *(dict) --*

      ARNs for the generated resources.

      - *(string) --*

        - *(string) --*
    """


_ClientReplaceTopicRuletopicRulePayloadactionscloudwatchAlarmTypeDef = TypedDict(
    "_ClientReplaceTopicRuletopicRulePayloadactionscloudwatchAlarmTypeDef",
    {"roleArn": str, "alarmName": str, "stateReason": str, "stateValue": str},
)


class ClientReplaceTopicRuletopicRulePayloadactionscloudwatchAlarmTypeDef(
    _ClientReplaceTopicRuletopicRulePayloadactionscloudwatchAlarmTypeDef
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloadactions` `cloudwatchAlarm`

    Change the state of a CloudWatch alarm.

    - **roleArn** *(string) --* **[REQUIRED]**

      The IAM role that allows access to the CloudWatch alarm.

    - **alarmName** *(string) --* **[REQUIRED]**

      The CloudWatch alarm name.

    - **stateReason** *(string) --* **[REQUIRED]**

      The reason for the alarm change.

    - **stateValue** *(string) --* **[REQUIRED]**

      The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
    """


_RequiredClientReplaceTopicRuletopicRulePayloadactionscloudwatchMetricTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloadactionscloudwatchMetricTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
    },
)
_OptionalClientReplaceTopicRuletopicRulePayloadactionscloudwatchMetricTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloadactionscloudwatchMetricTypeDef",
    {"metricTimestamp": str},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloadactionscloudwatchMetricTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloadactionscloudwatchMetricTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloadactionscloudwatchMetricTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloadactions` `cloudwatchMetric`

    Capture a CloudWatch metric.

    - **roleArn** *(string) --* **[REQUIRED]**

      The IAM role that allows access to the CloudWatch metric.

    - **metricNamespace** *(string) --* **[REQUIRED]**

      The CloudWatch metric namespace name.

    - **metricName** *(string) --* **[REQUIRED]**

      The CloudWatch metric name.

    - **metricValue** *(string) --* **[REQUIRED]**

      The CloudWatch metric value.

    - **metricUnit** *(string) --* **[REQUIRED]**

      The `metric unit
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
      supported by CloudWatch.

    - **metricTimestamp** *(string) --*

      An optional `Unix timestamp
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
      .
    """


_RequiredClientReplaceTopicRuletopicRulePayloadactionsdynamoDBTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloadactionsdynamoDBTypeDef",
    {"tableName": str, "roleArn": str, "hashKeyField": str, "hashKeyValue": str},
)
_OptionalClientReplaceTopicRuletopicRulePayloadactionsdynamoDBTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloadactionsdynamoDBTypeDef",
    {
        "operation": str,
        "hashKeyType": str,
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": str,
        "payloadField": str,
    },
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloadactionsdynamoDBTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloadactionsdynamoDBTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloadactionsdynamoDBTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloadactions` `dynamoDB`

    Write to a DynamoDB table.

    - **tableName** *(string) --* **[REQUIRED]**

      The name of the DynamoDB table.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access to the DynamoDB table.

    - **operation** *(string) --*

      The type of operation to be performed. This follows the substitution template, so it can
      be ``${operation}`` , but the substitution must result in one of the following:
      ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

    - **hashKeyField** *(string) --* **[REQUIRED]**

      The hash key name.

    - **hashKeyValue** *(string) --* **[REQUIRED]**

      The hash key value.

    - **hashKeyType** *(string) --*

      The hash key type. Valid values are "STRING" or "NUMBER"

    - **rangeKeyField** *(string) --*

      The range key name.

    - **rangeKeyValue** *(string) --*

      The range key value.

    - **rangeKeyType** *(string) --*

      The range key type. Valid values are "STRING" or "NUMBER"

    - **payloadField** *(string) --*

      The action payload. This name can be customized.
    """


_ClientReplaceTopicRuletopicRulePayloadactionsdynamoDBv2putItemTypeDef = TypedDict(
    "_ClientReplaceTopicRuletopicRulePayloadactionsdynamoDBv2putItemTypeDef",
    {"tableName": str},
)


class ClientReplaceTopicRuletopicRulePayloadactionsdynamoDBv2putItemTypeDef(
    _ClientReplaceTopicRuletopicRulePayloadactionsdynamoDBv2putItemTypeDef
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloadactionsdynamoDBv2` `putItem`

    Specifies the DynamoDB table to which the message data will be written. For example:

     ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
     "my-table" } } }``

    Each attribute in the message payload will be written to a separate column in the
    DynamoDB database.

    - **tableName** *(string) --* **[REQUIRED]**

      The table where the message data will be written.
    """


_ClientReplaceTopicRuletopicRulePayloadactionsdynamoDBv2TypeDef = TypedDict(
    "_ClientReplaceTopicRuletopicRulePayloadactionsdynamoDBv2TypeDef",
    {
        "roleArn": str,
        "putItem": ClientReplaceTopicRuletopicRulePayloadactionsdynamoDBv2putItemTypeDef,
    },
)


class ClientReplaceTopicRuletopicRulePayloadactionsdynamoDBv2TypeDef(
    _ClientReplaceTopicRuletopicRulePayloadactionsdynamoDBv2TypeDef
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloadactions` `dynamoDBv2`

    Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to
    write each attribute in an MQTT message payload into a separate DynamoDB column.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access to the DynamoDB table.

    - **putItem** *(dict) --* **[REQUIRED]**

      Specifies the DynamoDB table to which the message data will be written. For example:

       ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
       "my-table" } } }``

      Each attribute in the message payload will be written to a separate column in the
      DynamoDB database.

      - **tableName** *(string) --* **[REQUIRED]**

        The table where the message data will be written.
    """


_ClientReplaceTopicRuletopicRulePayloadactionselasticsearchTypeDef = TypedDict(
    "_ClientReplaceTopicRuletopicRulePayloadactionselasticsearchTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
)


class ClientReplaceTopicRuletopicRulePayloadactionselasticsearchTypeDef(
    _ClientReplaceTopicRuletopicRulePayloadactionselasticsearchTypeDef
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloadactions` `elasticsearch`

    Write data to an Amazon Elasticsearch Service domain.

    - **roleArn** *(string) --* **[REQUIRED]**

      The IAM role ARN that has access to Elasticsearch.

    - **endpoint** *(string) --* **[REQUIRED]**

      The endpoint of your Elasticsearch domain.

    - **index** *(string) --* **[REQUIRED]**

      The Elasticsearch index where you want to store your data.

    - **type** *(string) --* **[REQUIRED]**

      The type of document you are storing.

    - **id** *(string) --* **[REQUIRED]**

      The unique identifier for the document you are storing.
    """


_RequiredClientReplaceTopicRuletopicRulePayloadactionsfirehoseTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloadactionsfirehoseTypeDef",
    {"roleArn": str, "deliveryStreamName": str},
)
_OptionalClientReplaceTopicRuletopicRulePayloadactionsfirehoseTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloadactionsfirehoseTypeDef",
    {"separator": str},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloadactionsfirehoseTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloadactionsfirehoseTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloadactionsfirehoseTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloadactions` `firehose`

    Write to an Amazon Kinesis Firehose stream.

    - **roleArn** *(string) --* **[REQUIRED]**

      The IAM role that grants access to the Amazon Kinesis Firehose stream.

    - **deliveryStreamName** *(string) --* **[REQUIRED]**

      The delivery stream name.

    - **separator** *(string) --*

      A character separator that will be used to separate records written to the Firehose
      stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ','
      (comma).
    """


_ClientReplaceTopicRuletopicRulePayloadactionsiotAnalyticsTypeDef = TypedDict(
    "_ClientReplaceTopicRuletopicRulePayloadactionsiotAnalyticsTypeDef",
    {"channelArn": str, "channelName": str, "roleArn": str},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloadactionsiotAnalyticsTypeDef(
    _ClientReplaceTopicRuletopicRulePayloadactionsiotAnalyticsTypeDef
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloadactions` `iotAnalytics`

    Sends message data to an AWS IoT Analytics channel.

    - **channelArn** *(string) --*

      (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

    - **channelName** *(string) --*

      The name of the IoT Analytics channel to which message data will be sent.

    - **roleArn** *(string) --*

      The ARN of the role which has a policy that grants IoT Analytics permission to send
      message data via IoT Analytics (iotanalytics:BatchPutMessage).
    """


_RequiredClientReplaceTopicRuletopicRulePayloadactionsiotEventsTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloadactionsiotEventsTypeDef",
    {"inputName": str, "roleArn": str},
)
_OptionalClientReplaceTopicRuletopicRulePayloadactionsiotEventsTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloadactionsiotEventsTypeDef",
    {"messageId": str},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloadactionsiotEventsTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloadactionsiotEventsTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloadactionsiotEventsTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloadactions` `iotEvents`

    Sends an input to an AWS IoT Events detector.

    - **inputName** *(string) --* **[REQUIRED]**

      The name of the AWS IoT Events input.

    - **messageId** *(string) --*

      [Optional] Use this to ensure that only one input (message) with a given messageId will
      be processed by an AWS IoT Events detector.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events
      detector. ("Action":"iotevents:BatchPutMessage").
    """


_RequiredClientReplaceTopicRuletopicRulePayloadactionskinesisTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloadactionskinesisTypeDef",
    {"roleArn": str, "streamName": str},
)
_OptionalClientReplaceTopicRuletopicRulePayloadactionskinesisTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloadactionskinesisTypeDef",
    {"partitionKey": str},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloadactionskinesisTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloadactionskinesisTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloadactionskinesisTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloadactions` `kinesis`

    Write data to an Amazon Kinesis stream.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access to the Amazon Kinesis stream.

    - **streamName** *(string) --* **[REQUIRED]**

      The name of the Amazon Kinesis stream.

    - **partitionKey** *(string) --*

      The partition key.
    """


_ClientReplaceTopicRuletopicRulePayloadactionslambdaTypeDef = TypedDict(
    "_ClientReplaceTopicRuletopicRulePayloadactionslambdaTypeDef", {"functionArn": str}
)


class ClientReplaceTopicRuletopicRulePayloadactionslambdaTypeDef(
    _ClientReplaceTopicRuletopicRulePayloadactionslambdaTypeDef
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloadactions` `lambda`

    Invoke a Lambda function.

    - **functionArn** *(string) --* **[REQUIRED]**

      The ARN of the Lambda function.
    """


_RequiredClientReplaceTopicRuletopicRulePayloadactionsrepublishTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloadactionsrepublishTypeDef",
    {"roleArn": str, "topic": str},
)
_OptionalClientReplaceTopicRuletopicRulePayloadactionsrepublishTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloadactionsrepublishTypeDef",
    {"qos": int},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloadactionsrepublishTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloadactionsrepublishTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloadactionsrepublishTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloadactions` `republish`

    Publish to another MQTT topic.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access.

    - **topic** *(string) --* **[REQUIRED]**

      The name of the MQTT topic.

    - **qos** *(integer) --*

      The Quality of Service (QoS) level to use when republishing messages. The default value
      is 0.
    """


_RequiredClientReplaceTopicRuletopicRulePayloadactionss3TypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloadactionss3TypeDef",
    {"roleArn": str, "bucketName": str, "key": str},
)
_OptionalClientReplaceTopicRuletopicRulePayloadactionss3TypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloadactionss3TypeDef",
    {"cannedAcl": str},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloadactionss3TypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloadactionss3TypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloadactionss3TypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloadactions` `s3`

    Write to an Amazon S3 bucket.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access.

    - **bucketName** *(string) --* **[REQUIRED]**

      The Amazon S3 bucket.

    - **key** *(string) --* **[REQUIRED]**

      The object key.

    - **cannedAcl** *(string) --*

      The Amazon S3 canned ACL that controls access to the object identified by the object key.
      For more information, see `S3 canned ACLs
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .
    """


_ClientReplaceTopicRuletopicRulePayloadactionssalesforceTypeDef = TypedDict(
    "_ClientReplaceTopicRuletopicRulePayloadactionssalesforceTypeDef",
    {"token": str, "url": str},
)


class ClientReplaceTopicRuletopicRulePayloadactionssalesforceTypeDef(
    _ClientReplaceTopicRuletopicRulePayloadactionssalesforceTypeDef
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloadactions` `salesforce`

    Send a message to a Salesforce IoT Cloud Input Stream.

    - **token** *(string) --* **[REQUIRED]**

      The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token
      is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

    - **url** *(string) --* **[REQUIRED]**

      The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the
      Salesforce IoT Cloud platform after creation of the Input Stream.
    """


_RequiredClientReplaceTopicRuletopicRulePayloadactionssnsTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloadactionssnsTypeDef",
    {"targetArn": str, "roleArn": str},
)
_OptionalClientReplaceTopicRuletopicRulePayloadactionssnsTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloadactionssnsTypeDef",
    {"messageFormat": str},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloadactionssnsTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloadactionssnsTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloadactionssnsTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloadactions` `sns`

    Publish to an Amazon SNS topic.

    - **targetArn** *(string) --* **[REQUIRED]**

      The ARN of the SNS topic.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access.

    - **messageFormat** *(string) --*

      (Optional) The message format of the message to publish. Accepted values are "JSON" and
      "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if
      the payload should be parsed and relevant platform-specific bits of the payload should be
      extracted. To read more about SNS message formats, see
      `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
      <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official
      documentation.
    """


_RequiredClientReplaceTopicRuletopicRulePayloadactionssqsTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloadactionssqsTypeDef",
    {"roleArn": str, "queueUrl": str},
)
_OptionalClientReplaceTopicRuletopicRulePayloadactionssqsTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloadactionssqsTypeDef",
    {"useBase64": bool},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloadactionssqsTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloadactionssqsTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloadactionssqsTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloadactions` `sqs`

    Publish to an Amazon SQS queue.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access.

    - **queueUrl** *(string) --* **[REQUIRED]**

      The URL of the Amazon SQS queue.

    - **useBase64** *(boolean) --*

      Specifies whether to use Base64 encoding.
    """


_RequiredClientReplaceTopicRuletopicRulePayloadactionsstepFunctionsTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloadactionsstepFunctionsTypeDef",
    {"stateMachineName": str, "roleArn": str},
)
_OptionalClientReplaceTopicRuletopicRulePayloadactionsstepFunctionsTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloadactionsstepFunctionsTypeDef",
    {"executionNamePrefix": str},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloadactionsstepFunctionsTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloadactionsstepFunctionsTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloadactionsstepFunctionsTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloadactions` `stepFunctions`

    Starts execution of a Step Functions state machine.

    - **executionNamePrefix** *(string) --*

      (Optional) A name will be given to the state machine execution consisting of this prefix
      followed by a UUID. Step Functions automatically creates a unique name for each state
      machine execution if one is not provided.

    - **stateMachineName** *(string) --* **[REQUIRED]**

      The name of the Step Functions state machine whose execution will be started.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that grants IoT permission to start execution of a state machine
      ("Action":"states:StartExecution").
    """


_ClientReplaceTopicRuletopicRulePayloadactionsTypeDef = TypedDict(
    "_ClientReplaceTopicRuletopicRulePayloadactionsTypeDef",
    {
        "dynamoDB": ClientReplaceTopicRuletopicRulePayloadactionsdynamoDBTypeDef,
        "dynamoDBv2": ClientReplaceTopicRuletopicRulePayloadactionsdynamoDBv2TypeDef,
        "lambda": ClientReplaceTopicRuletopicRulePayloadactionslambdaTypeDef,
        "sns": ClientReplaceTopicRuletopicRulePayloadactionssnsTypeDef,
        "sqs": ClientReplaceTopicRuletopicRulePayloadactionssqsTypeDef,
        "kinesis": ClientReplaceTopicRuletopicRulePayloadactionskinesisTypeDef,
        "republish": ClientReplaceTopicRuletopicRulePayloadactionsrepublishTypeDef,
        "s3": ClientReplaceTopicRuletopicRulePayloadactionss3TypeDef,
        "firehose": ClientReplaceTopicRuletopicRulePayloadactionsfirehoseTypeDef,
        "cloudwatchMetric": ClientReplaceTopicRuletopicRulePayloadactionscloudwatchMetricTypeDef,
        "cloudwatchAlarm": ClientReplaceTopicRuletopicRulePayloadactionscloudwatchAlarmTypeDef,
        "elasticsearch": ClientReplaceTopicRuletopicRulePayloadactionselasticsearchTypeDef,
        "salesforce": ClientReplaceTopicRuletopicRulePayloadactionssalesforceTypeDef,
        "iotAnalytics": ClientReplaceTopicRuletopicRulePayloadactionsiotAnalyticsTypeDef,
        "iotEvents": ClientReplaceTopicRuletopicRulePayloadactionsiotEventsTypeDef,
        "stepFunctions": ClientReplaceTopicRuletopicRulePayloadactionsstepFunctionsTypeDef,
    },
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloadactionsTypeDef(
    _ClientReplaceTopicRuletopicRulePayloadactionsTypeDef
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayload` `actions`

    Describes the actions associated with a rule.

    - **dynamoDB** *(dict) --*

      Write to a DynamoDB table.

      - **tableName** *(string) --* **[REQUIRED]**

        The name of the DynamoDB table.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access to the DynamoDB table.

      - **operation** *(string) --*

        The type of operation to be performed. This follows the substitution template, so it can
        be ``${operation}`` , but the substitution must result in one of the following:
        ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

      - **hashKeyField** *(string) --* **[REQUIRED]**

        The hash key name.

      - **hashKeyValue** *(string) --* **[REQUIRED]**

        The hash key value.

      - **hashKeyType** *(string) --*

        The hash key type. Valid values are "STRING" or "NUMBER"

      - **rangeKeyField** *(string) --*

        The range key name.

      - **rangeKeyValue** *(string) --*

        The range key value.

      - **rangeKeyType** *(string) --*

        The range key type. Valid values are "STRING" or "NUMBER"

      - **payloadField** *(string) --*

        The action payload. This name can be customized.

    - **dynamoDBv2** *(dict) --*

      Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to
      write each attribute in an MQTT message payload into a separate DynamoDB column.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access to the DynamoDB table.

      - **putItem** *(dict) --* **[REQUIRED]**

        Specifies the DynamoDB table to which the message data will be written. For example:

         ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
         "my-table" } } }``

        Each attribute in the message payload will be written to a separate column in the
        DynamoDB database.

        - **tableName** *(string) --* **[REQUIRED]**

          The table where the message data will be written.

    - **lambda** *(dict) --*

      Invoke a Lambda function.

      - **functionArn** *(string) --* **[REQUIRED]**

        The ARN of the Lambda function.

    - **sns** *(dict) --*

      Publish to an Amazon SNS topic.

      - **targetArn** *(string) --* **[REQUIRED]**

        The ARN of the SNS topic.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access.

      - **messageFormat** *(string) --*

        (Optional) The message format of the message to publish. Accepted values are "JSON" and
        "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if
        the payload should be parsed and relevant platform-specific bits of the payload should be
        extracted. To read more about SNS message formats, see
        `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
        <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official
        documentation.

    - **sqs** *(dict) --*

      Publish to an Amazon SQS queue.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access.

      - **queueUrl** *(string) --* **[REQUIRED]**

        The URL of the Amazon SQS queue.

      - **useBase64** *(boolean) --*

        Specifies whether to use Base64 encoding.

    - **kinesis** *(dict) --*

      Write data to an Amazon Kinesis stream.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access to the Amazon Kinesis stream.

      - **streamName** *(string) --* **[REQUIRED]**

        The name of the Amazon Kinesis stream.

      - **partitionKey** *(string) --*

        The partition key.

    - **republish** *(dict) --*

      Publish to another MQTT topic.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access.

      - **topic** *(string) --* **[REQUIRED]**

        The name of the MQTT topic.

      - **qos** *(integer) --*

        The Quality of Service (QoS) level to use when republishing messages. The default value
        is 0.

    - **s3** *(dict) --*

      Write to an Amazon S3 bucket.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access.

      - **bucketName** *(string) --* **[REQUIRED]**

        The Amazon S3 bucket.

      - **key** *(string) --* **[REQUIRED]**

        The object key.

      - **cannedAcl** *(string) --*

        The Amazon S3 canned ACL that controls access to the object identified by the object key.
        For more information, see `S3 canned ACLs
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

    - **firehose** *(dict) --*

      Write to an Amazon Kinesis Firehose stream.

      - **roleArn** *(string) --* **[REQUIRED]**

        The IAM role that grants access to the Amazon Kinesis Firehose stream.

      - **deliveryStreamName** *(string) --* **[REQUIRED]**

        The delivery stream name.

      - **separator** *(string) --*

        A character separator that will be used to separate records written to the Firehose
        stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ','
        (comma).

    - **cloudwatchMetric** *(dict) --*

      Capture a CloudWatch metric.

      - **roleArn** *(string) --* **[REQUIRED]**

        The IAM role that allows access to the CloudWatch metric.

      - **metricNamespace** *(string) --* **[REQUIRED]**

        The CloudWatch metric namespace name.

      - **metricName** *(string) --* **[REQUIRED]**

        The CloudWatch metric name.

      - **metricValue** *(string) --* **[REQUIRED]**

        The CloudWatch metric value.

      - **metricUnit** *(string) --* **[REQUIRED]**

        The `metric unit
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
        supported by CloudWatch.

      - **metricTimestamp** *(string) --*

        An optional `Unix timestamp
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
        .

    - **cloudwatchAlarm** *(dict) --*

      Change the state of a CloudWatch alarm.

      - **roleArn** *(string) --* **[REQUIRED]**

        The IAM role that allows access to the CloudWatch alarm.

      - **alarmName** *(string) --* **[REQUIRED]**

        The CloudWatch alarm name.

      - **stateReason** *(string) --* **[REQUIRED]**

        The reason for the alarm change.

      - **stateValue** *(string) --* **[REQUIRED]**

        The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

    - **elasticsearch** *(dict) --*

      Write data to an Amazon Elasticsearch Service domain.

      - **roleArn** *(string) --* **[REQUIRED]**

        The IAM role ARN that has access to Elasticsearch.

      - **endpoint** *(string) --* **[REQUIRED]**

        The endpoint of your Elasticsearch domain.

      - **index** *(string) --* **[REQUIRED]**

        The Elasticsearch index where you want to store your data.

      - **type** *(string) --* **[REQUIRED]**

        The type of document you are storing.

      - **id** *(string) --* **[REQUIRED]**

        The unique identifier for the document you are storing.

    - **salesforce** *(dict) --*

      Send a message to a Salesforce IoT Cloud Input Stream.

      - **token** *(string) --* **[REQUIRED]**

        The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token
        is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

      - **url** *(string) --* **[REQUIRED]**

        The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the
        Salesforce IoT Cloud platform after creation of the Input Stream.

    - **iotAnalytics** *(dict) --*

      Sends message data to an AWS IoT Analytics channel.

      - **channelArn** *(string) --*

        (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

      - **channelName** *(string) --*

        The name of the IoT Analytics channel to which message data will be sent.

      - **roleArn** *(string) --*

        The ARN of the role which has a policy that grants IoT Analytics permission to send
        message data via IoT Analytics (iotanalytics:BatchPutMessage).

    - **iotEvents** *(dict) --*

      Sends an input to an AWS IoT Events detector.

      - **inputName** *(string) --* **[REQUIRED]**

        The name of the AWS IoT Events input.

      - **messageId** *(string) --*

        [Optional] Use this to ensure that only one input (message) with a given messageId will
        be processed by an AWS IoT Events detector.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events
        detector. ("Action":"iotevents:BatchPutMessage").

    - **stepFunctions** *(dict) --*

      Starts execution of a Step Functions state machine.

      - **executionNamePrefix** *(string) --*

        (Optional) A name will be given to the state machine execution consisting of this prefix
        followed by a UUID. Step Functions automatically creates a unique name for each state
        machine execution if one is not provided.

      - **stateMachineName** *(string) --* **[REQUIRED]**

        The name of the Step Functions state machine whose execution will be started.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role that grants IoT permission to start execution of a state machine
        ("Action":"states:StartExecution").
    """


_ClientReplaceTopicRuletopicRulePayloaderrorActioncloudwatchAlarmTypeDef = TypedDict(
    "_ClientReplaceTopicRuletopicRulePayloaderrorActioncloudwatchAlarmTypeDef",
    {"roleArn": str, "alarmName": str, "stateReason": str, "stateValue": str},
)


class ClientReplaceTopicRuletopicRulePayloaderrorActioncloudwatchAlarmTypeDef(
    _ClientReplaceTopicRuletopicRulePayloaderrorActioncloudwatchAlarmTypeDef
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloaderrorAction` `cloudwatchAlarm`

    Change the state of a CloudWatch alarm.

    - **roleArn** *(string) --* **[REQUIRED]**

      The IAM role that allows access to the CloudWatch alarm.

    - **alarmName** *(string) --* **[REQUIRED]**

      The CloudWatch alarm name.

    - **stateReason** *(string) --* **[REQUIRED]**

      The reason for the alarm change.

    - **stateValue** *(string) --* **[REQUIRED]**

      The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
    """


_RequiredClientReplaceTopicRuletopicRulePayloaderrorActioncloudwatchMetricTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloaderrorActioncloudwatchMetricTypeDef",
    {
        "roleArn": str,
        "metricNamespace": str,
        "metricName": str,
        "metricValue": str,
        "metricUnit": str,
    },
)
_OptionalClientReplaceTopicRuletopicRulePayloaderrorActioncloudwatchMetricTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloaderrorActioncloudwatchMetricTypeDef",
    {"metricTimestamp": str},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloaderrorActioncloudwatchMetricTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloaderrorActioncloudwatchMetricTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloaderrorActioncloudwatchMetricTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloaderrorAction` `cloudwatchMetric`

    Capture a CloudWatch metric.

    - **roleArn** *(string) --* **[REQUIRED]**

      The IAM role that allows access to the CloudWatch metric.

    - **metricNamespace** *(string) --* **[REQUIRED]**

      The CloudWatch metric namespace name.

    - **metricName** *(string) --* **[REQUIRED]**

      The CloudWatch metric name.

    - **metricValue** *(string) --* **[REQUIRED]**

      The CloudWatch metric value.

    - **metricUnit** *(string) --* **[REQUIRED]**

      The `metric unit
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
      supported by CloudWatch.

    - **metricTimestamp** *(string) --*

      An optional `Unix timestamp
      <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
      .
    """


_RequiredClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBTypeDef",
    {"tableName": str, "roleArn": str, "hashKeyField": str, "hashKeyValue": str},
)
_OptionalClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBTypeDef",
    {
        "operation": str,
        "hashKeyType": str,
        "rangeKeyField": str,
        "rangeKeyValue": str,
        "rangeKeyType": str,
        "payloadField": str,
    },
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloaderrorAction` `dynamoDB`

    Write to a DynamoDB table.

    - **tableName** *(string) --* **[REQUIRED]**

      The name of the DynamoDB table.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access to the DynamoDB table.

    - **operation** *(string) --*

      The type of operation to be performed. This follows the substitution template, so it can be
      ``${operation}`` , but the substitution must result in one of the following: ``INSERT`` ,
      ``UPDATE`` , or ``DELETE`` .

    - **hashKeyField** *(string) --* **[REQUIRED]**

      The hash key name.

    - **hashKeyValue** *(string) --* **[REQUIRED]**

      The hash key value.

    - **hashKeyType** *(string) --*

      The hash key type. Valid values are "STRING" or "NUMBER"

    - **rangeKeyField** *(string) --*

      The range key name.

    - **rangeKeyValue** *(string) --*

      The range key value.

    - **rangeKeyType** *(string) --*

      The range key type. Valid values are "STRING" or "NUMBER"

    - **payloadField** *(string) --*

      The action payload. This name can be customized.
    """


_ClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBv2putItemTypeDef = TypedDict(
    "_ClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBv2putItemTypeDef",
    {"tableName": str},
)


class ClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBv2putItemTypeDef(
    _ClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBv2putItemTypeDef
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBv2` `putItem`

    Specifies the DynamoDB table to which the message data will be written. For example:

     ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
     "my-table" } } }``

    Each attribute in the message payload will be written to a separate column in the DynamoDB
    database.

    - **tableName** *(string) --* **[REQUIRED]**

      The table where the message data will be written.
    """


_ClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBv2TypeDef = TypedDict(
    "_ClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBv2TypeDef",
    {
        "roleArn": str,
        "putItem": ClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBv2putItemTypeDef,
    },
)


class ClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBv2TypeDef(
    _ClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBv2TypeDef
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloaderrorAction` `dynamoDBv2`

    Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to
    write each attribute in an MQTT message payload into a separate DynamoDB column.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access to the DynamoDB table.

    - **putItem** *(dict) --* **[REQUIRED]**

      Specifies the DynamoDB table to which the message data will be written. For example:

       ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
       "my-table" } } }``

      Each attribute in the message payload will be written to a separate column in the DynamoDB
      database.

      - **tableName** *(string) --* **[REQUIRED]**

        The table where the message data will be written.
    """


_ClientReplaceTopicRuletopicRulePayloaderrorActionelasticsearchTypeDef = TypedDict(
    "_ClientReplaceTopicRuletopicRulePayloaderrorActionelasticsearchTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
)


class ClientReplaceTopicRuletopicRulePayloaderrorActionelasticsearchTypeDef(
    _ClientReplaceTopicRuletopicRulePayloaderrorActionelasticsearchTypeDef
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloaderrorAction` `elasticsearch`

    Write data to an Amazon Elasticsearch Service domain.

    - **roleArn** *(string) --* **[REQUIRED]**

      The IAM role ARN that has access to Elasticsearch.

    - **endpoint** *(string) --* **[REQUIRED]**

      The endpoint of your Elasticsearch domain.

    - **index** *(string) --* **[REQUIRED]**

      The Elasticsearch index where you want to store your data.

    - **type** *(string) --* **[REQUIRED]**

      The type of document you are storing.

    - **id** *(string) --* **[REQUIRED]**

      The unique identifier for the document you are storing.
    """


_RequiredClientReplaceTopicRuletopicRulePayloaderrorActionfirehoseTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloaderrorActionfirehoseTypeDef",
    {"roleArn": str, "deliveryStreamName": str},
)
_OptionalClientReplaceTopicRuletopicRulePayloaderrorActionfirehoseTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloaderrorActionfirehoseTypeDef",
    {"separator": str},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloaderrorActionfirehoseTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloaderrorActionfirehoseTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloaderrorActionfirehoseTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloaderrorAction` `firehose`

    Write to an Amazon Kinesis Firehose stream.

    - **roleArn** *(string) --* **[REQUIRED]**

      The IAM role that grants access to the Amazon Kinesis Firehose stream.

    - **deliveryStreamName** *(string) --* **[REQUIRED]**

      The delivery stream name.

    - **separator** *(string) --*

      A character separator that will be used to separate records written to the Firehose stream.
      Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).
    """


_ClientReplaceTopicRuletopicRulePayloaderrorActioniotAnalyticsTypeDef = TypedDict(
    "_ClientReplaceTopicRuletopicRulePayloaderrorActioniotAnalyticsTypeDef",
    {"channelArn": str, "channelName": str, "roleArn": str},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloaderrorActioniotAnalyticsTypeDef(
    _ClientReplaceTopicRuletopicRulePayloaderrorActioniotAnalyticsTypeDef
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloaderrorAction` `iotAnalytics`

    Sends message data to an AWS IoT Analytics channel.

    - **channelArn** *(string) --*

      (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

    - **channelName** *(string) --*

      The name of the IoT Analytics channel to which message data will be sent.

    - **roleArn** *(string) --*

      The ARN of the role which has a policy that grants IoT Analytics permission to send message
      data via IoT Analytics (iotanalytics:BatchPutMessage).
    """


_RequiredClientReplaceTopicRuletopicRulePayloaderrorActioniotEventsTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloaderrorActioniotEventsTypeDef",
    {"inputName": str, "roleArn": str},
)
_OptionalClientReplaceTopicRuletopicRulePayloaderrorActioniotEventsTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloaderrorActioniotEventsTypeDef",
    {"messageId": str},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloaderrorActioniotEventsTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloaderrorActioniotEventsTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloaderrorActioniotEventsTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloaderrorAction` `iotEvents`

    Sends an input to an AWS IoT Events detector.

    - **inputName** *(string) --* **[REQUIRED]**

      The name of the AWS IoT Events input.

    - **messageId** *(string) --*

      [Optional] Use this to ensure that only one input (message) with a given messageId will be
      processed by an AWS IoT Events detector.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events
      detector. ("Action":"iotevents:BatchPutMessage").
    """


_RequiredClientReplaceTopicRuletopicRulePayloaderrorActionkinesisTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloaderrorActionkinesisTypeDef",
    {"roleArn": str, "streamName": str},
)
_OptionalClientReplaceTopicRuletopicRulePayloaderrorActionkinesisTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloaderrorActionkinesisTypeDef",
    {"partitionKey": str},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloaderrorActionkinesisTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloaderrorActionkinesisTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloaderrorActionkinesisTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloaderrorAction` `kinesis`

    Write data to an Amazon Kinesis stream.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access to the Amazon Kinesis stream.

    - **streamName** *(string) --* **[REQUIRED]**

      The name of the Amazon Kinesis stream.

    - **partitionKey** *(string) --*

      The partition key.
    """


_ClientReplaceTopicRuletopicRulePayloaderrorActionlambdaTypeDef = TypedDict(
    "_ClientReplaceTopicRuletopicRulePayloaderrorActionlambdaTypeDef",
    {"functionArn": str},
)


class ClientReplaceTopicRuletopicRulePayloaderrorActionlambdaTypeDef(
    _ClientReplaceTopicRuletopicRulePayloaderrorActionlambdaTypeDef
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloaderrorAction` `lambda`

    Invoke a Lambda function.

    - **functionArn** *(string) --* **[REQUIRED]**

      The ARN of the Lambda function.
    """


_RequiredClientReplaceTopicRuletopicRulePayloaderrorActionrepublishTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloaderrorActionrepublishTypeDef",
    {"roleArn": str, "topic": str},
)
_OptionalClientReplaceTopicRuletopicRulePayloaderrorActionrepublishTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloaderrorActionrepublishTypeDef",
    {"qos": int},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloaderrorActionrepublishTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloaderrorActionrepublishTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloaderrorActionrepublishTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloaderrorAction` `republish`

    Publish to another MQTT topic.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access.

    - **topic** *(string) --* **[REQUIRED]**

      The name of the MQTT topic.

    - **qos** *(integer) --*

      The Quality of Service (QoS) level to use when republishing messages. The default value is
      0.
    """


_RequiredClientReplaceTopicRuletopicRulePayloaderrorActions3TypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloaderrorActions3TypeDef",
    {"roleArn": str, "bucketName": str, "key": str},
)
_OptionalClientReplaceTopicRuletopicRulePayloaderrorActions3TypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloaderrorActions3TypeDef",
    {"cannedAcl": str},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloaderrorActions3TypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloaderrorActions3TypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloaderrorActions3TypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloaderrorAction` `s3`

    Write to an Amazon S3 bucket.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access.

    - **bucketName** *(string) --* **[REQUIRED]**

      The Amazon S3 bucket.

    - **key** *(string) --* **[REQUIRED]**

      The object key.

    - **cannedAcl** *(string) --*

      The Amazon S3 canned ACL that controls access to the object identified by the object key.
      For more information, see `S3 canned ACLs
      <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .
    """


_ClientReplaceTopicRuletopicRulePayloaderrorActionsalesforceTypeDef = TypedDict(
    "_ClientReplaceTopicRuletopicRulePayloaderrorActionsalesforceTypeDef",
    {"token": str, "url": str},
)


class ClientReplaceTopicRuletopicRulePayloaderrorActionsalesforceTypeDef(
    _ClientReplaceTopicRuletopicRulePayloaderrorActionsalesforceTypeDef
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloaderrorAction` `salesforce`

    Send a message to a Salesforce IoT Cloud Input Stream.

    - **token** *(string) --* **[REQUIRED]**

      The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token
      is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

    - **url** *(string) --* **[REQUIRED]**

      The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the
      Salesforce IoT Cloud platform after creation of the Input Stream.
    """


_RequiredClientReplaceTopicRuletopicRulePayloaderrorActionsnsTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloaderrorActionsnsTypeDef",
    {"targetArn": str, "roleArn": str},
)
_OptionalClientReplaceTopicRuletopicRulePayloaderrorActionsnsTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloaderrorActionsnsTypeDef",
    {"messageFormat": str},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloaderrorActionsnsTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloaderrorActionsnsTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloaderrorActionsnsTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloaderrorAction` `sns`

    Publish to an Amazon SNS topic.

    - **targetArn** *(string) --* **[REQUIRED]**

      The ARN of the SNS topic.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access.

    - **messageFormat** *(string) --*

      (Optional) The message format of the message to publish. Accepted values are "JSON" and
      "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if
      the payload should be parsed and relevant platform-specific bits of the payload should be
      extracted. To read more about SNS message formats, see
      `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
      <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official
      documentation.
    """


_RequiredClientReplaceTopicRuletopicRulePayloaderrorActionsqsTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloaderrorActionsqsTypeDef",
    {"roleArn": str, "queueUrl": str},
)
_OptionalClientReplaceTopicRuletopicRulePayloaderrorActionsqsTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloaderrorActionsqsTypeDef",
    {"useBase64": bool},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloaderrorActionsqsTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloaderrorActionsqsTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloaderrorActionsqsTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloaderrorAction` `sqs`

    Publish to an Amazon SQS queue.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access.

    - **queueUrl** *(string) --* **[REQUIRED]**

      The URL of the Amazon SQS queue.

    - **useBase64** *(boolean) --*

      Specifies whether to use Base64 encoding.
    """


_RequiredClientReplaceTopicRuletopicRulePayloaderrorActionstepFunctionsTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloaderrorActionstepFunctionsTypeDef",
    {"stateMachineName": str, "roleArn": str},
)
_OptionalClientReplaceTopicRuletopicRulePayloaderrorActionstepFunctionsTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloaderrorActionstepFunctionsTypeDef",
    {"executionNamePrefix": str},
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloaderrorActionstepFunctionsTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloaderrorActionstepFunctionsTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloaderrorActionstepFunctionsTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayloaderrorAction` `stepFunctions`

    Starts execution of a Step Functions state machine.

    - **executionNamePrefix** *(string) --*

      (Optional) A name will be given to the state machine execution consisting of this prefix
      followed by a UUID. Step Functions automatically creates a unique name for each state
      machine execution if one is not provided.

    - **stateMachineName** *(string) --* **[REQUIRED]**

      The name of the Step Functions state machine whose execution will be started.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that grants IoT permission to start execution of a state machine
      ("Action":"states:StartExecution").
    """


_ClientReplaceTopicRuletopicRulePayloaderrorActionTypeDef = TypedDict(
    "_ClientReplaceTopicRuletopicRulePayloaderrorActionTypeDef",
    {
        "dynamoDB": ClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBTypeDef,
        "dynamoDBv2": ClientReplaceTopicRuletopicRulePayloaderrorActiondynamoDBv2TypeDef,
        "lambda": ClientReplaceTopicRuletopicRulePayloaderrorActionlambdaTypeDef,
        "sns": ClientReplaceTopicRuletopicRulePayloaderrorActionsnsTypeDef,
        "sqs": ClientReplaceTopicRuletopicRulePayloaderrorActionsqsTypeDef,
        "kinesis": ClientReplaceTopicRuletopicRulePayloaderrorActionkinesisTypeDef,
        "republish": ClientReplaceTopicRuletopicRulePayloaderrorActionrepublishTypeDef,
        "s3": ClientReplaceTopicRuletopicRulePayloaderrorActions3TypeDef,
        "firehose": ClientReplaceTopicRuletopicRulePayloaderrorActionfirehoseTypeDef,
        "cloudwatchMetric": ClientReplaceTopicRuletopicRulePayloaderrorActioncloudwatchMetricTypeDef,
        "cloudwatchAlarm": ClientReplaceTopicRuletopicRulePayloaderrorActioncloudwatchAlarmTypeDef,
        "elasticsearch": ClientReplaceTopicRuletopicRulePayloaderrorActionelasticsearchTypeDef,
        "salesforce": ClientReplaceTopicRuletopicRulePayloaderrorActionsalesforceTypeDef,
        "iotAnalytics": ClientReplaceTopicRuletopicRulePayloaderrorActioniotAnalyticsTypeDef,
        "iotEvents": ClientReplaceTopicRuletopicRulePayloaderrorActioniotEventsTypeDef,
        "stepFunctions": ClientReplaceTopicRuletopicRulePayloaderrorActionstepFunctionsTypeDef,
    },
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloaderrorActionTypeDef(
    _ClientReplaceTopicRuletopicRulePayloaderrorActionTypeDef
):
    """
    Type definition for `ClientReplaceTopicRuletopicRulePayload` `errorAction`

    The action to take when an error occurs.

    - **dynamoDB** *(dict) --*

      Write to a DynamoDB table.

      - **tableName** *(string) --* **[REQUIRED]**

        The name of the DynamoDB table.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access to the DynamoDB table.

      - **operation** *(string) --*

        The type of operation to be performed. This follows the substitution template, so it can be
        ``${operation}`` , but the substitution must result in one of the following: ``INSERT`` ,
        ``UPDATE`` , or ``DELETE`` .

      - **hashKeyField** *(string) --* **[REQUIRED]**

        The hash key name.

      - **hashKeyValue** *(string) --* **[REQUIRED]**

        The hash key value.

      - **hashKeyType** *(string) --*

        The hash key type. Valid values are "STRING" or "NUMBER"

      - **rangeKeyField** *(string) --*

        The range key name.

      - **rangeKeyValue** *(string) --*

        The range key value.

      - **rangeKeyType** *(string) --*

        The range key type. Valid values are "STRING" or "NUMBER"

      - **payloadField** *(string) --*

        The action payload. This name can be customized.

    - **dynamoDBv2** *(dict) --*

      Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to
      write each attribute in an MQTT message payload into a separate DynamoDB column.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access to the DynamoDB table.

      - **putItem** *(dict) --* **[REQUIRED]**

        Specifies the DynamoDB table to which the message data will be written. For example:

         ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
         "my-table" } } }``

        Each attribute in the message payload will be written to a separate column in the DynamoDB
        database.

        - **tableName** *(string) --* **[REQUIRED]**

          The table where the message data will be written.

    - **lambda** *(dict) --*

      Invoke a Lambda function.

      - **functionArn** *(string) --* **[REQUIRED]**

        The ARN of the Lambda function.

    - **sns** *(dict) --*

      Publish to an Amazon SNS topic.

      - **targetArn** *(string) --* **[REQUIRED]**

        The ARN of the SNS topic.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access.

      - **messageFormat** *(string) --*

        (Optional) The message format of the message to publish. Accepted values are "JSON" and
        "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if
        the payload should be parsed and relevant platform-specific bits of the payload should be
        extracted. To read more about SNS message formats, see
        `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
        <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official
        documentation.

    - **sqs** *(dict) --*

      Publish to an Amazon SQS queue.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access.

      - **queueUrl** *(string) --* **[REQUIRED]**

        The URL of the Amazon SQS queue.

      - **useBase64** *(boolean) --*

        Specifies whether to use Base64 encoding.

    - **kinesis** *(dict) --*

      Write data to an Amazon Kinesis stream.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access to the Amazon Kinesis stream.

      - **streamName** *(string) --* **[REQUIRED]**

        The name of the Amazon Kinesis stream.

      - **partitionKey** *(string) --*

        The partition key.

    - **republish** *(dict) --*

      Publish to another MQTT topic.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access.

      - **topic** *(string) --* **[REQUIRED]**

        The name of the MQTT topic.

      - **qos** *(integer) --*

        The Quality of Service (QoS) level to use when republishing messages. The default value is
        0.

    - **s3** *(dict) --*

      Write to an Amazon S3 bucket.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the IAM role that grants access.

      - **bucketName** *(string) --* **[REQUIRED]**

        The Amazon S3 bucket.

      - **key** *(string) --* **[REQUIRED]**

        The object key.

      - **cannedAcl** *(string) --*

        The Amazon S3 canned ACL that controls access to the object identified by the object key.
        For more information, see `S3 canned ACLs
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

    - **firehose** *(dict) --*

      Write to an Amazon Kinesis Firehose stream.

      - **roleArn** *(string) --* **[REQUIRED]**

        The IAM role that grants access to the Amazon Kinesis Firehose stream.

      - **deliveryStreamName** *(string) --* **[REQUIRED]**

        The delivery stream name.

      - **separator** *(string) --*

        A character separator that will be used to separate records written to the Firehose stream.
        Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

    - **cloudwatchMetric** *(dict) --*

      Capture a CloudWatch metric.

      - **roleArn** *(string) --* **[REQUIRED]**

        The IAM role that allows access to the CloudWatch metric.

      - **metricNamespace** *(string) --* **[REQUIRED]**

        The CloudWatch metric namespace name.

      - **metricName** *(string) --* **[REQUIRED]**

        The CloudWatch metric name.

      - **metricValue** *(string) --* **[REQUIRED]**

        The CloudWatch metric value.

      - **metricUnit** *(string) --* **[REQUIRED]**

        The `metric unit
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
        supported by CloudWatch.

      - **metricTimestamp** *(string) --*

        An optional `Unix timestamp
        <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
        .

    - **cloudwatchAlarm** *(dict) --*

      Change the state of a CloudWatch alarm.

      - **roleArn** *(string) --* **[REQUIRED]**

        The IAM role that allows access to the CloudWatch alarm.

      - **alarmName** *(string) --* **[REQUIRED]**

        The CloudWatch alarm name.

      - **stateReason** *(string) --* **[REQUIRED]**

        The reason for the alarm change.

      - **stateValue** *(string) --* **[REQUIRED]**

        The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

    - **elasticsearch** *(dict) --*

      Write data to an Amazon Elasticsearch Service domain.

      - **roleArn** *(string) --* **[REQUIRED]**

        The IAM role ARN that has access to Elasticsearch.

      - **endpoint** *(string) --* **[REQUIRED]**

        The endpoint of your Elasticsearch domain.

      - **index** *(string) --* **[REQUIRED]**

        The Elasticsearch index where you want to store your data.

      - **type** *(string) --* **[REQUIRED]**

        The type of document you are storing.

      - **id** *(string) --* **[REQUIRED]**

        The unique identifier for the document you are storing.

    - **salesforce** *(dict) --*

      Send a message to a Salesforce IoT Cloud Input Stream.

      - **token** *(string) --* **[REQUIRED]**

        The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token
        is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

      - **url** *(string) --* **[REQUIRED]**

        The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the
        Salesforce IoT Cloud platform after creation of the Input Stream.

    - **iotAnalytics** *(dict) --*

      Sends message data to an AWS IoT Analytics channel.

      - **channelArn** *(string) --*

        (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

      - **channelName** *(string) --*

        The name of the IoT Analytics channel to which message data will be sent.

      - **roleArn** *(string) --*

        The ARN of the role which has a policy that grants IoT Analytics permission to send message
        data via IoT Analytics (iotanalytics:BatchPutMessage).

    - **iotEvents** *(dict) --*

      Sends an input to an AWS IoT Events detector.

      - **inputName** *(string) --* **[REQUIRED]**

        The name of the AWS IoT Events input.

      - **messageId** *(string) --*

        [Optional] Use this to ensure that only one input (message) with a given messageId will be
        processed by an AWS IoT Events detector.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events
        detector. ("Action":"iotevents:BatchPutMessage").

    - **stepFunctions** *(dict) --*

      Starts execution of a Step Functions state machine.

      - **executionNamePrefix** *(string) --*

        (Optional) A name will be given to the state machine execution consisting of this prefix
        followed by a UUID. Step Functions automatically creates a unique name for each state
        machine execution if one is not provided.

      - **stateMachineName** *(string) --* **[REQUIRED]**

        The name of the Step Functions state machine whose execution will be started.

      - **roleArn** *(string) --* **[REQUIRED]**

        The ARN of the role that grants IoT permission to start execution of a state machine
        ("Action":"states:StartExecution").
    """


_RequiredClientReplaceTopicRuletopicRulePayloadTypeDef = TypedDict(
    "_RequiredClientReplaceTopicRuletopicRulePayloadTypeDef",
    {"sql": str, "actions": List[ClientReplaceTopicRuletopicRulePayloadactionsTypeDef]},
)
_OptionalClientReplaceTopicRuletopicRulePayloadTypeDef = TypedDict(
    "_OptionalClientReplaceTopicRuletopicRulePayloadTypeDef",
    {
        "description": str,
        "ruleDisabled": bool,
        "awsIotSqlVersion": str,
        "errorAction": ClientReplaceTopicRuletopicRulePayloaderrorActionTypeDef,
    },
    total=False,
)


class ClientReplaceTopicRuletopicRulePayloadTypeDef(
    _RequiredClientReplaceTopicRuletopicRulePayloadTypeDef,
    _OptionalClientReplaceTopicRuletopicRulePayloadTypeDef,
):
    """
    Type definition for `ClientReplaceTopicRule` `topicRulePayload`

    The rule payload.

    - **sql** *(string) --* **[REQUIRED]**

      The SQL statement used to query the topic. For more information, see `AWS IoT SQL Reference
      <https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference>`__
      in the *AWS IoT Developer Guide* .

    - **description** *(string) --*

      The description of the rule.

    - **actions** *(list) --* **[REQUIRED]**

      The actions associated with the rule.

      - *(dict) --*

        Describes the actions associated with a rule.

        - **dynamoDB** *(dict) --*

          Write to a DynamoDB table.

          - **tableName** *(string) --* **[REQUIRED]**

            The name of the DynamoDB table.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the IAM role that grants access to the DynamoDB table.

          - **operation** *(string) --*

            The type of operation to be performed. This follows the substitution template, so it can
            be ``${operation}`` , but the substitution must result in one of the following:
            ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

          - **hashKeyField** *(string) --* **[REQUIRED]**

            The hash key name.

          - **hashKeyValue** *(string) --* **[REQUIRED]**

            The hash key value.

          - **hashKeyType** *(string) --*

            The hash key type. Valid values are "STRING" or "NUMBER"

          - **rangeKeyField** *(string) --*

            The range key name.

          - **rangeKeyValue** *(string) --*

            The range key value.

          - **rangeKeyType** *(string) --*

            The range key type. Valid values are "STRING" or "NUMBER"

          - **payloadField** *(string) --*

            The action payload. This name can be customized.

        - **dynamoDBv2** *(dict) --*

          Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to
          write each attribute in an MQTT message payload into a separate DynamoDB column.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the IAM role that grants access to the DynamoDB table.

          - **putItem** *(dict) --* **[REQUIRED]**

            Specifies the DynamoDB table to which the message data will be written. For example:

             ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
             "my-table" } } }``

            Each attribute in the message payload will be written to a separate column in the
            DynamoDB database.

            - **tableName** *(string) --* **[REQUIRED]**

              The table where the message data will be written.

        - **lambda** *(dict) --*

          Invoke a Lambda function.

          - **functionArn** *(string) --* **[REQUIRED]**

            The ARN of the Lambda function.

        - **sns** *(dict) --*

          Publish to an Amazon SNS topic.

          - **targetArn** *(string) --* **[REQUIRED]**

            The ARN of the SNS topic.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the IAM role that grants access.

          - **messageFormat** *(string) --*

            (Optional) The message format of the message to publish. Accepted values are "JSON" and
            "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if
            the payload should be parsed and relevant platform-specific bits of the payload should be
            extracted. To read more about SNS message formats, see
            `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
            <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official
            documentation.

        - **sqs** *(dict) --*

          Publish to an Amazon SQS queue.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the IAM role that grants access.

          - **queueUrl** *(string) --* **[REQUIRED]**

            The URL of the Amazon SQS queue.

          - **useBase64** *(boolean) --*

            Specifies whether to use Base64 encoding.

        - **kinesis** *(dict) --*

          Write data to an Amazon Kinesis stream.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the IAM role that grants access to the Amazon Kinesis stream.

          - **streamName** *(string) --* **[REQUIRED]**

            The name of the Amazon Kinesis stream.

          - **partitionKey** *(string) --*

            The partition key.

        - **republish** *(dict) --*

          Publish to another MQTT topic.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the IAM role that grants access.

          - **topic** *(string) --* **[REQUIRED]**

            The name of the MQTT topic.

          - **qos** *(integer) --*

            The Quality of Service (QoS) level to use when republishing messages. The default value
            is 0.

        - **s3** *(dict) --*

          Write to an Amazon S3 bucket.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the IAM role that grants access.

          - **bucketName** *(string) --* **[REQUIRED]**

            The Amazon S3 bucket.

          - **key** *(string) --* **[REQUIRED]**

            The object key.

          - **cannedAcl** *(string) --*

            The Amazon S3 canned ACL that controls access to the object identified by the object key.
            For more information, see `S3 canned ACLs
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

        - **firehose** *(dict) --*

          Write to an Amazon Kinesis Firehose stream.

          - **roleArn** *(string) --* **[REQUIRED]**

            The IAM role that grants access to the Amazon Kinesis Firehose stream.

          - **deliveryStreamName** *(string) --* **[REQUIRED]**

            The delivery stream name.

          - **separator** *(string) --*

            A character separator that will be used to separate records written to the Firehose
            stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ','
            (comma).

        - **cloudwatchMetric** *(dict) --*

          Capture a CloudWatch metric.

          - **roleArn** *(string) --* **[REQUIRED]**

            The IAM role that allows access to the CloudWatch metric.

          - **metricNamespace** *(string) --* **[REQUIRED]**

            The CloudWatch metric namespace name.

          - **metricName** *(string) --* **[REQUIRED]**

            The CloudWatch metric name.

          - **metricValue** *(string) --* **[REQUIRED]**

            The CloudWatch metric value.

          - **metricUnit** *(string) --* **[REQUIRED]**

            The `metric unit
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
            supported by CloudWatch.

          - **metricTimestamp** *(string) --*

            An optional `Unix timestamp
            <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
            .

        - **cloudwatchAlarm** *(dict) --*

          Change the state of a CloudWatch alarm.

          - **roleArn** *(string) --* **[REQUIRED]**

            The IAM role that allows access to the CloudWatch alarm.

          - **alarmName** *(string) --* **[REQUIRED]**

            The CloudWatch alarm name.

          - **stateReason** *(string) --* **[REQUIRED]**

            The reason for the alarm change.

          - **stateValue** *(string) --* **[REQUIRED]**

            The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

        - **elasticsearch** *(dict) --*

          Write data to an Amazon Elasticsearch Service domain.

          - **roleArn** *(string) --* **[REQUIRED]**

            The IAM role ARN that has access to Elasticsearch.

          - **endpoint** *(string) --* **[REQUIRED]**

            The endpoint of your Elasticsearch domain.

          - **index** *(string) --* **[REQUIRED]**

            The Elasticsearch index where you want to store your data.

          - **type** *(string) --* **[REQUIRED]**

            The type of document you are storing.

          - **id** *(string) --* **[REQUIRED]**

            The unique identifier for the document you are storing.

        - **salesforce** *(dict) --*

          Send a message to a Salesforce IoT Cloud Input Stream.

          - **token** *(string) --* **[REQUIRED]**

            The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token
            is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

          - **url** *(string) --* **[REQUIRED]**

            The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the
            Salesforce IoT Cloud platform after creation of the Input Stream.

        - **iotAnalytics** *(dict) --*

          Sends message data to an AWS IoT Analytics channel.

          - **channelArn** *(string) --*

            (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

          - **channelName** *(string) --*

            The name of the IoT Analytics channel to which message data will be sent.

          - **roleArn** *(string) --*

            The ARN of the role which has a policy that grants IoT Analytics permission to send
            message data via IoT Analytics (iotanalytics:BatchPutMessage).

        - **iotEvents** *(dict) --*

          Sends an input to an AWS IoT Events detector.

          - **inputName** *(string) --* **[REQUIRED]**

            The name of the AWS IoT Events input.

          - **messageId** *(string) --*

            [Optional] Use this to ensure that only one input (message) with a given messageId will
            be processed by an AWS IoT Events detector.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events
            detector. ("Action":"iotevents:BatchPutMessage").

        - **stepFunctions** *(dict) --*

          Starts execution of a Step Functions state machine.

          - **executionNamePrefix** *(string) --*

            (Optional) A name will be given to the state machine execution consisting of this prefix
            followed by a UUID. Step Functions automatically creates a unique name for each state
            machine execution if one is not provided.

          - **stateMachineName** *(string) --* **[REQUIRED]**

            The name of the Step Functions state machine whose execution will be started.

          - **roleArn** *(string) --* **[REQUIRED]**

            The ARN of the role that grants IoT permission to start execution of a state machine
            ("Action":"states:StartExecution").

    - **ruleDisabled** *(boolean) --*

      Specifies whether the rule is disabled.

    - **awsIotSqlVersion** *(string) --*

      The version of the SQL rules engine to use when evaluating the rule.

    - **errorAction** *(dict) --*

      The action to take when an error occurs.

      - **dynamoDB** *(dict) --*

        Write to a DynamoDB table.

        - **tableName** *(string) --* **[REQUIRED]**

          The name of the DynamoDB table.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the IAM role that grants access to the DynamoDB table.

        - **operation** *(string) --*

          The type of operation to be performed. This follows the substitution template, so it can be
          ``${operation}`` , but the substitution must result in one of the following: ``INSERT`` ,
          ``UPDATE`` , or ``DELETE`` .

        - **hashKeyField** *(string) --* **[REQUIRED]**

          The hash key name.

        - **hashKeyValue** *(string) --* **[REQUIRED]**

          The hash key value.

        - **hashKeyType** *(string) --*

          The hash key type. Valid values are "STRING" or "NUMBER"

        - **rangeKeyField** *(string) --*

          The range key name.

        - **rangeKeyValue** *(string) --*

          The range key value.

        - **rangeKeyType** *(string) --*

          The range key type. Valid values are "STRING" or "NUMBER"

        - **payloadField** *(string) --*

          The action payload. This name can be customized.

      - **dynamoDBv2** *(dict) --*

        Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to
        write each attribute in an MQTT message payload into a separate DynamoDB column.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the IAM role that grants access to the DynamoDB table.

        - **putItem** *(dict) --* **[REQUIRED]**

          Specifies the DynamoDB table to which the message data will be written. For example:

           ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName":
           "my-table" } } }``

          Each attribute in the message payload will be written to a separate column in the DynamoDB
          database.

          - **tableName** *(string) --* **[REQUIRED]**

            The table where the message data will be written.

      - **lambda** *(dict) --*

        Invoke a Lambda function.

        - **functionArn** *(string) --* **[REQUIRED]**

          The ARN of the Lambda function.

      - **sns** *(dict) --*

        Publish to an Amazon SNS topic.

        - **targetArn** *(string) --* **[REQUIRED]**

          The ARN of the SNS topic.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the IAM role that grants access.

        - **messageFormat** *(string) --*

          (Optional) The message format of the message to publish. Accepted values are "JSON" and
          "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if
          the payload should be parsed and relevant platform-specific bits of the payload should be
          extracted. To read more about SNS message formats, see
          `https\\://docs.aws.amazon.com/sns/latest/dg/json-formats.html
          <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official
          documentation.

      - **sqs** *(dict) --*

        Publish to an Amazon SQS queue.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the IAM role that grants access.

        - **queueUrl** *(string) --* **[REQUIRED]**

          The URL of the Amazon SQS queue.

        - **useBase64** *(boolean) --*

          Specifies whether to use Base64 encoding.

      - **kinesis** *(dict) --*

        Write data to an Amazon Kinesis stream.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the IAM role that grants access to the Amazon Kinesis stream.

        - **streamName** *(string) --* **[REQUIRED]**

          The name of the Amazon Kinesis stream.

        - **partitionKey** *(string) --*

          The partition key.

      - **republish** *(dict) --*

        Publish to another MQTT topic.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the IAM role that grants access.

        - **topic** *(string) --* **[REQUIRED]**

          The name of the MQTT topic.

        - **qos** *(integer) --*

          The Quality of Service (QoS) level to use when republishing messages. The default value is
          0.

      - **s3** *(dict) --*

        Write to an Amazon S3 bucket.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the IAM role that grants access.

        - **bucketName** *(string) --* **[REQUIRED]**

          The Amazon S3 bucket.

        - **key** *(string) --* **[REQUIRED]**

          The object key.

        - **cannedAcl** *(string) --*

          The Amazon S3 canned ACL that controls access to the object identified by the object key.
          For more information, see `S3 canned ACLs
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

      - **firehose** *(dict) --*

        Write to an Amazon Kinesis Firehose stream.

        - **roleArn** *(string) --* **[REQUIRED]**

          The IAM role that grants access to the Amazon Kinesis Firehose stream.

        - **deliveryStreamName** *(string) --* **[REQUIRED]**

          The delivery stream name.

        - **separator** *(string) --*

          A character separator that will be used to separate records written to the Firehose stream.
          Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

      - **cloudwatchMetric** *(dict) --*

        Capture a CloudWatch metric.

        - **roleArn** *(string) --* **[REQUIRED]**

          The IAM role that allows access to the CloudWatch metric.

        - **metricNamespace** *(string) --* **[REQUIRED]**

          The CloudWatch metric namespace name.

        - **metricName** *(string) --* **[REQUIRED]**

          The CloudWatch metric name.

        - **metricValue** *(string) --* **[REQUIRED]**

          The CloudWatch metric value.

        - **metricUnit** *(string) --* **[REQUIRED]**

          The `metric unit
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__
          supported by CloudWatch.

        - **metricTimestamp** *(string) --*

          An optional `Unix timestamp
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__
          .

      - **cloudwatchAlarm** *(dict) --*

        Change the state of a CloudWatch alarm.

        - **roleArn** *(string) --* **[REQUIRED]**

          The IAM role that allows access to the CloudWatch alarm.

        - **alarmName** *(string) --* **[REQUIRED]**

          The CloudWatch alarm name.

        - **stateReason** *(string) --* **[REQUIRED]**

          The reason for the alarm change.

        - **stateValue** *(string) --* **[REQUIRED]**

          The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

      - **elasticsearch** *(dict) --*

        Write data to an Amazon Elasticsearch Service domain.

        - **roleArn** *(string) --* **[REQUIRED]**

          The IAM role ARN that has access to Elasticsearch.

        - **endpoint** *(string) --* **[REQUIRED]**

          The endpoint of your Elasticsearch domain.

        - **index** *(string) --* **[REQUIRED]**

          The Elasticsearch index where you want to store your data.

        - **type** *(string) --* **[REQUIRED]**

          The type of document you are storing.

        - **id** *(string) --* **[REQUIRED]**

          The unique identifier for the document you are storing.

      - **salesforce** *(dict) --*

        Send a message to a Salesforce IoT Cloud Input Stream.

        - **token** *(string) --* **[REQUIRED]**

          The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token
          is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

        - **url** *(string) --* **[REQUIRED]**

          The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the
          Salesforce IoT Cloud platform after creation of the Input Stream.

      - **iotAnalytics** *(dict) --*

        Sends message data to an AWS IoT Analytics channel.

        - **channelArn** *(string) --*

          (deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

        - **channelName** *(string) --*

          The name of the IoT Analytics channel to which message data will be sent.

        - **roleArn** *(string) --*

          The ARN of the role which has a policy that grants IoT Analytics permission to send message
          data via IoT Analytics (iotanalytics:BatchPutMessage).

      - **iotEvents** *(dict) --*

        Sends an input to an AWS IoT Events detector.

        - **inputName** *(string) --* **[REQUIRED]**

          The name of the AWS IoT Events input.

        - **messageId** *(string) --*

          [Optional] Use this to ensure that only one input (message) with a given messageId will be
          processed by an AWS IoT Events detector.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events
          detector. ("Action":"iotevents:BatchPutMessage").

      - **stepFunctions** *(dict) --*

        Starts execution of a Step Functions state machine.

        - **executionNamePrefix** *(string) --*

          (Optional) A name will be given to the state machine execution consisting of this prefix
          followed by a UUID. Step Functions automatically creates a unique name for each state
          machine execution if one is not provided.

        - **stateMachineName** *(string) --* **[REQUIRED]**

          The name of the Step Functions state machine whose execution will be started.

        - **roleArn** *(string) --* **[REQUIRED]**

          The ARN of the role that grants IoT permission to start execution of a state machine
          ("Action":"states:StartExecution").
    """


_ClientSearchIndexResponsethingGroupsTypeDef = TypedDict(
    "_ClientSearchIndexResponsethingGroupsTypeDef",
    {
        "thingGroupName": str,
        "thingGroupId": str,
        "thingGroupDescription": str,
        "attributes": Dict[str, str],
        "parentGroupNames": List[str],
    },
    total=False,
)


class ClientSearchIndexResponsethingGroupsTypeDef(
    _ClientSearchIndexResponsethingGroupsTypeDef
):
    """
    Type definition for `ClientSearchIndexResponse` `thingGroups`

    The thing group search index document.

    - **thingGroupName** *(string) --*

      The thing group name.

    - **thingGroupId** *(string) --*

      The thing group ID.

    - **thingGroupDescription** *(string) --*

      The thing group description.

    - **attributes** *(dict) --*

      The thing group attributes.

      - *(string) --*

        - *(string) --*

    - **parentGroupNames** *(list) --*

      Parent group names.

      - *(string) --*
    """


_ClientSearchIndexResponsethingsconnectivityTypeDef = TypedDict(
    "_ClientSearchIndexResponsethingsconnectivityTypeDef",
    {"connected": bool, "timestamp": int},
    total=False,
)


class ClientSearchIndexResponsethingsconnectivityTypeDef(
    _ClientSearchIndexResponsethingsconnectivityTypeDef
):
    """
    Type definition for `ClientSearchIndexResponsethings` `connectivity`

    Indicates whether the thing is connected to the AWS IoT service.

    - **connected** *(boolean) --*

      True if the thing is connected to the AWS IoT service; false if it is not connected.

    - **timestamp** *(integer) --*

      The epoch time (in milliseconds) when the thing last connected or disconnected. If the
      thing has been disconnected for more than a few weeks, the time value might be missing.
    """


_ClientSearchIndexResponsethingsTypeDef = TypedDict(
    "_ClientSearchIndexResponsethingsTypeDef",
    {
        "thingName": str,
        "thingId": str,
        "thingTypeName": str,
        "thingGroupNames": List[str],
        "attributes": Dict[str, str],
        "shadow": str,
        "connectivity": ClientSearchIndexResponsethingsconnectivityTypeDef,
    },
    total=False,
)


class ClientSearchIndexResponsethingsTypeDef(_ClientSearchIndexResponsethingsTypeDef):
    """
    Type definition for `ClientSearchIndexResponse` `things`

    The thing search index document.

    - **thingName** *(string) --*

      The thing name.

    - **thingId** *(string) --*

      The thing ID.

    - **thingTypeName** *(string) --*

      The thing type name.

    - **thingGroupNames** *(list) --*

      Thing group names.

      - *(string) --*

    - **attributes** *(dict) --*

      The attributes.

      - *(string) --*

        - *(string) --*

    - **shadow** *(string) --*

      The shadow.

    - **connectivity** *(dict) --*

      Indicates whether the thing is connected to the AWS IoT service.

      - **connected** *(boolean) --*

        True if the thing is connected to the AWS IoT service; false if it is not connected.

      - **timestamp** *(integer) --*

        The epoch time (in milliseconds) when the thing last connected or disconnected. If the
        thing has been disconnected for more than a few weeks, the time value might be missing.
    """


_ClientSearchIndexResponseTypeDef = TypedDict(
    "_ClientSearchIndexResponseTypeDef",
    {
        "nextToken": str,
        "things": List[ClientSearchIndexResponsethingsTypeDef],
        "thingGroups": List[ClientSearchIndexResponsethingGroupsTypeDef],
    },
    total=False,
)


class ClientSearchIndexResponseTypeDef(_ClientSearchIndexResponseTypeDef):
    """
    Type definition for `ClientSearchIndex` `Response`

    - **nextToken** *(string) --*

      The token used to get the next set of results, or null if there are no additional results.

    - **things** *(list) --*

      The things that match the search query.

      - *(dict) --*

        The thing search index document.

        - **thingName** *(string) --*

          The thing name.

        - **thingId** *(string) --*

          The thing ID.

        - **thingTypeName** *(string) --*

          The thing type name.

        - **thingGroupNames** *(list) --*

          Thing group names.

          - *(string) --*

        - **attributes** *(dict) --*

          The attributes.

          - *(string) --*

            - *(string) --*

        - **shadow** *(string) --*

          The shadow.

        - **connectivity** *(dict) --*

          Indicates whether the thing is connected to the AWS IoT service.

          - **connected** *(boolean) --*

            True if the thing is connected to the AWS IoT service; false if it is not connected.

          - **timestamp** *(integer) --*

            The epoch time (in milliseconds) when the thing last connected or disconnected. If the
            thing has been disconnected for more than a few weeks, the time value might be missing.

    - **thingGroups** *(list) --*

      The thing groups that match the search query.

      - *(dict) --*

        The thing group search index document.

        - **thingGroupName** *(string) --*

          The thing group name.

        - **thingGroupId** *(string) --*

          The thing group ID.

        - **thingGroupDescription** *(string) --*

          The thing group description.

        - **attributes** *(dict) --*

          The thing group attributes.

          - *(string) --*

            - *(string) --*

        - **parentGroupNames** *(list) --*

          Parent group names.

          - *(string) --*
    """


_ClientSetDefaultAuthorizerResponseTypeDef = TypedDict(
    "_ClientSetDefaultAuthorizerResponseTypeDef",
    {"authorizerName": str, "authorizerArn": str},
    total=False,
)


class ClientSetDefaultAuthorizerResponseTypeDef(
    _ClientSetDefaultAuthorizerResponseTypeDef
):
    """
    Type definition for `ClientSetDefaultAuthorizer` `Response`

    - **authorizerName** *(string) --*

      The authorizer name.

    - **authorizerArn** *(string) --*

      The authorizer ARN.
    """


_RequiredClientSetLoggingOptionsloggingOptionsPayloadTypeDef = TypedDict(
    "_RequiredClientSetLoggingOptionsloggingOptionsPayloadTypeDef", {"roleArn": str}
)
_OptionalClientSetLoggingOptionsloggingOptionsPayloadTypeDef = TypedDict(
    "_OptionalClientSetLoggingOptionsloggingOptionsPayloadTypeDef",
    {"logLevel": str},
    total=False,
)


class ClientSetLoggingOptionsloggingOptionsPayloadTypeDef(
    _RequiredClientSetLoggingOptionsloggingOptionsPayloadTypeDef,
    _OptionalClientSetLoggingOptionsloggingOptionsPayloadTypeDef,
):
    """
    Type definition for `ClientSetLoggingOptions` `loggingOptionsPayload`

    The logging options payload.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the IAM role that grants access.

    - **logLevel** *(string) --*

      The log level.
    """


_RequiredClientSetV2LoggingLevellogTargetTypeDef = TypedDict(
    "_RequiredClientSetV2LoggingLevellogTargetTypeDef", {"targetType": str}
)
_OptionalClientSetV2LoggingLevellogTargetTypeDef = TypedDict(
    "_OptionalClientSetV2LoggingLevellogTargetTypeDef", {"targetName": str}, total=False
)


class ClientSetV2LoggingLevellogTargetTypeDef(
    _RequiredClientSetV2LoggingLevellogTargetTypeDef,
    _OptionalClientSetV2LoggingLevellogTargetTypeDef,
):
    """
    Type definition for `ClientSetV2LoggingLevel` `logTarget`

    The log target.

    - **targetType** *(string) --* **[REQUIRED]**

      The target type.

    - **targetName** *(string) --*

      The target name.
    """


_ClientStartAuditMitigationActionsTaskResponseTypeDef = TypedDict(
    "_ClientStartAuditMitigationActionsTaskResponseTypeDef",
    {"taskId": str},
    total=False,
)


class ClientStartAuditMitigationActionsTaskResponseTypeDef(
    _ClientStartAuditMitigationActionsTaskResponseTypeDef
):
    """
    Type definition for `ClientStartAuditMitigationActionsTask` `Response`

    - **taskId** *(string) --*

      The unique identifier for the audit mitigation task. This matches the ``taskId`` that you
      specified in the request.
    """


_ClientStartAuditMitigationActionsTasktargetTypeDef = TypedDict(
    "_ClientStartAuditMitigationActionsTasktargetTypeDef",
    {
        "auditTaskId": str,
        "findingIds": List[str],
        "auditCheckToReasonCodeFilter": Dict[str, List[str]],
    },
    total=False,
)


class ClientStartAuditMitigationActionsTasktargetTypeDef(
    _ClientStartAuditMitigationActionsTasktargetTypeDef
):
    """
    Type definition for `ClientStartAuditMitigationActionsTask` `target`

    Specifies the audit findings to which the mitigation actions are applied. You can apply them to a
    type of audit check, to all findings from an audit, or to a speecific set of findings.

    - **auditTaskId** *(string) --*

      If the task will apply a mitigation action to findings from a specific audit, this value
      uniquely identifies the audit.

    - **findingIds** *(list) --*

      If the task will apply a mitigation action to one or more listed findings, this value uniquely
      identifies those findings.

      - *(string) --*

    - **auditCheckToReasonCodeFilter** *(dict) --*

      Specifies a filter in the form of an audit check and set of reason codes that identify the
      findings from the audit to which the audit mitigation actions task apply.

      - *(string) --*

        An audit check name. Checks must be enabled for your account. (Use
        ``DescribeAccountAuditConfiguration`` to see the list of all checks, including those that are
        enabled or use ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)

        - *(list) --*

          - *(string) --*
    """


_ClientStartOnDemandAuditTaskResponseTypeDef = TypedDict(
    "_ClientStartOnDemandAuditTaskResponseTypeDef", {"taskId": str}, total=False
)


class ClientStartOnDemandAuditTaskResponseTypeDef(
    _ClientStartOnDemandAuditTaskResponseTypeDef
):
    """
    Type definition for `ClientStartOnDemandAuditTask` `Response`

    - **taskId** *(string) --*

      The ID of the on-demand audit you started.
    """


_ClientStartThingRegistrationTaskResponseTypeDef = TypedDict(
    "_ClientStartThingRegistrationTaskResponseTypeDef", {"taskId": str}, total=False
)


class ClientStartThingRegistrationTaskResponseTypeDef(
    _ClientStartThingRegistrationTaskResponseTypeDef
):
    """
    Type definition for `ClientStartThingRegistrationTask` `Response`

    - **taskId** *(string) --*

      The bulk thing provisioning task ID.
    """


_ClientTagResourcetagsTypeDef = TypedDict(
    "_ClientTagResourcetagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientTagResourcetagsTypeDef(_ClientTagResourcetagsTypeDef):
    """
    Type definition for `ClientTagResource` `tags`

    A set of key/value pairs that are used to manage the resource.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ClientTestAuthorizationResponseauthResultsallowedpoliciesTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseauthResultsallowedpoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)


class ClientTestAuthorizationResponseauthResultsallowedpoliciesTypeDef(
    _ClientTestAuthorizationResponseauthResultsallowedpoliciesTypeDef
):
    """
    Type definition for `ClientTestAuthorizationResponseauthResultsallowed` `policies`

    Describes an AWS IoT policy.

    - **policyName** *(string) --*

      The policy name.

    - **policyArn** *(string) --*

      The policy ARN.
    """


_ClientTestAuthorizationResponseauthResultsallowedTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseauthResultsallowedTypeDef",
    {
        "policies": List[
            ClientTestAuthorizationResponseauthResultsallowedpoliciesTypeDef
        ]
    },
    total=False,
)


class ClientTestAuthorizationResponseauthResultsallowedTypeDef(
    _ClientTestAuthorizationResponseauthResultsallowedTypeDef
):
    """
    Type definition for `ClientTestAuthorizationResponseauthResults` `allowed`

    The policies and statements that allowed the specified action.

    - **policies** *(list) --*

      A list of policies that allowed the authentication.

      - *(dict) --*

        Describes an AWS IoT policy.

        - **policyName** *(string) --*

          The policy name.

        - **policyArn** *(string) --*

          The policy ARN.
    """


_ClientTestAuthorizationResponseauthResultsauthInfoTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseauthResultsauthInfoTypeDef",
    {"actionType": str, "resources": List[str]},
    total=False,
)


class ClientTestAuthorizationResponseauthResultsauthInfoTypeDef(
    _ClientTestAuthorizationResponseauthResultsauthInfoTypeDef
):
    """
    Type definition for `ClientTestAuthorizationResponseauthResults` `authInfo`

    Authorization information.

    - **actionType** *(string) --*

      The type of action for which the principal is being authorized.

    - **resources** *(list) --*

      The resources for which the principal is being authorized to perform the specified
      action.

      - *(string) --*
    """


_ClientTestAuthorizationResponseauthResultsdeniedexplicitDenypoliciesTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseauthResultsdeniedexplicitDenypoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)


class ClientTestAuthorizationResponseauthResultsdeniedexplicitDenypoliciesTypeDef(
    _ClientTestAuthorizationResponseauthResultsdeniedexplicitDenypoliciesTypeDef
):
    """
    Type definition for `ClientTestAuthorizationResponseauthResultsdeniedexplicitDeny` `policies`

    Describes an AWS IoT policy.

    - **policyName** *(string) --*

      The policy name.

    - **policyArn** *(string) --*

      The policy ARN.
    """


_ClientTestAuthorizationResponseauthResultsdeniedexplicitDenyTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseauthResultsdeniedexplicitDenyTypeDef",
    {
        "policies": List[
            ClientTestAuthorizationResponseauthResultsdeniedexplicitDenypoliciesTypeDef
        ]
    },
    total=False,
)


class ClientTestAuthorizationResponseauthResultsdeniedexplicitDenyTypeDef(
    _ClientTestAuthorizationResponseauthResultsdeniedexplicitDenyTypeDef
):
    """
    Type definition for `ClientTestAuthorizationResponseauthResultsdenied` `explicitDeny`

    Information that explicitly denies the authorization.

    - **policies** *(list) --*

      The policies that denied the authorization.

      - *(dict) --*

        Describes an AWS IoT policy.

        - **policyName** *(string) --*

          The policy name.

        - **policyArn** *(string) --*

          The policy ARN.
    """


_ClientTestAuthorizationResponseauthResultsdeniedimplicitDenypoliciesTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseauthResultsdeniedimplicitDenypoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)


class ClientTestAuthorizationResponseauthResultsdeniedimplicitDenypoliciesTypeDef(
    _ClientTestAuthorizationResponseauthResultsdeniedimplicitDenypoliciesTypeDef
):
    """
    Type definition for `ClientTestAuthorizationResponseauthResultsdeniedimplicitDeny` `policies`

    Describes an AWS IoT policy.

    - **policyName** *(string) --*

      The policy name.

    - **policyArn** *(string) --*

      The policy ARN.
    """


_ClientTestAuthorizationResponseauthResultsdeniedimplicitDenyTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseauthResultsdeniedimplicitDenyTypeDef",
    {
        "policies": List[
            ClientTestAuthorizationResponseauthResultsdeniedimplicitDenypoliciesTypeDef
        ]
    },
    total=False,
)


class ClientTestAuthorizationResponseauthResultsdeniedimplicitDenyTypeDef(
    _ClientTestAuthorizationResponseauthResultsdeniedimplicitDenyTypeDef
):
    """
    Type definition for `ClientTestAuthorizationResponseauthResultsdenied` `implicitDeny`

    Information that implicitly denies the authorization. When a policy doesn't explicitly
    deny or allow an action on a resource it is considered an implicit deny.

    - **policies** *(list) --*

      Policies that don't contain a matching allow or deny statement for the specified
      action on the specified resource.

      - *(dict) --*

        Describes an AWS IoT policy.

        - **policyName** *(string) --*

          The policy name.

        - **policyArn** *(string) --*

          The policy ARN.
    """


_ClientTestAuthorizationResponseauthResultsdeniedTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseauthResultsdeniedTypeDef",
    {
        "implicitDeny": ClientTestAuthorizationResponseauthResultsdeniedimplicitDenyTypeDef,
        "explicitDeny": ClientTestAuthorizationResponseauthResultsdeniedexplicitDenyTypeDef,
    },
    total=False,
)


class ClientTestAuthorizationResponseauthResultsdeniedTypeDef(
    _ClientTestAuthorizationResponseauthResultsdeniedTypeDef
):
    """
    Type definition for `ClientTestAuthorizationResponseauthResults` `denied`

    The policies and statements that denied the specified action.

    - **implicitDeny** *(dict) --*

      Information that implicitly denies the authorization. When a policy doesn't explicitly
      deny or allow an action on a resource it is considered an implicit deny.

      - **policies** *(list) --*

        Policies that don't contain a matching allow or deny statement for the specified
        action on the specified resource.

        - *(dict) --*

          Describes an AWS IoT policy.

          - **policyName** *(string) --*

            The policy name.

          - **policyArn** *(string) --*

            The policy ARN.

    - **explicitDeny** *(dict) --*

      Information that explicitly denies the authorization.

      - **policies** *(list) --*

        The policies that denied the authorization.

        - *(dict) --*

          Describes an AWS IoT policy.

          - **policyName** *(string) --*

            The policy name.

          - **policyArn** *(string) --*

            The policy ARN.
    """


_ClientTestAuthorizationResponseauthResultsTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseauthResultsTypeDef",
    {
        "authInfo": ClientTestAuthorizationResponseauthResultsauthInfoTypeDef,
        "allowed": ClientTestAuthorizationResponseauthResultsallowedTypeDef,
        "denied": ClientTestAuthorizationResponseauthResultsdeniedTypeDef,
        "authDecision": str,
        "missingContextValues": List[str],
    },
    total=False,
)


class ClientTestAuthorizationResponseauthResultsTypeDef(
    _ClientTestAuthorizationResponseauthResultsTypeDef
):
    """
    Type definition for `ClientTestAuthorizationResponse` `authResults`

    The authorizer result.

    - **authInfo** *(dict) --*

      Authorization information.

      - **actionType** *(string) --*

        The type of action for which the principal is being authorized.

      - **resources** *(list) --*

        The resources for which the principal is being authorized to perform the specified
        action.

        - *(string) --*

    - **allowed** *(dict) --*

      The policies and statements that allowed the specified action.

      - **policies** *(list) --*

        A list of policies that allowed the authentication.

        - *(dict) --*

          Describes an AWS IoT policy.

          - **policyName** *(string) --*

            The policy name.

          - **policyArn** *(string) --*

            The policy ARN.

    - **denied** *(dict) --*

      The policies and statements that denied the specified action.

      - **implicitDeny** *(dict) --*

        Information that implicitly denies the authorization. When a policy doesn't explicitly
        deny or allow an action on a resource it is considered an implicit deny.

        - **policies** *(list) --*

          Policies that don't contain a matching allow or deny statement for the specified
          action on the specified resource.

          - *(dict) --*

            Describes an AWS IoT policy.

            - **policyName** *(string) --*

              The policy name.

            - **policyArn** *(string) --*

              The policy ARN.

      - **explicitDeny** *(dict) --*

        Information that explicitly denies the authorization.

        - **policies** *(list) --*

          The policies that denied the authorization.

          - *(dict) --*

            Describes an AWS IoT policy.

            - **policyName** *(string) --*

              The policy name.

            - **policyArn** *(string) --*

              The policy ARN.

    - **authDecision** *(string) --*

      The final authorization decision of this scenario. Multiple statements are taken into
      account when determining the authorization decision. An explicit deny statement can
      override multiple allow statements.

    - **missingContextValues** *(list) --*

      Contains any missing context values found while evaluating policy.

      - *(string) --*
    """


_ClientTestAuthorizationResponseTypeDef = TypedDict(
    "_ClientTestAuthorizationResponseTypeDef",
    {"authResults": List[ClientTestAuthorizationResponseauthResultsTypeDef]},
    total=False,
)


class ClientTestAuthorizationResponseTypeDef(_ClientTestAuthorizationResponseTypeDef):
    """
    Type definition for `ClientTestAuthorization` `Response`

    - **authResults** *(list) --*

      The authentication results.

      - *(dict) --*

        The authorizer result.

        - **authInfo** *(dict) --*

          Authorization information.

          - **actionType** *(string) --*

            The type of action for which the principal is being authorized.

          - **resources** *(list) --*

            The resources for which the principal is being authorized to perform the specified
            action.

            - *(string) --*

        - **allowed** *(dict) --*

          The policies and statements that allowed the specified action.

          - **policies** *(list) --*

            A list of policies that allowed the authentication.

            - *(dict) --*

              Describes an AWS IoT policy.

              - **policyName** *(string) --*

                The policy name.

              - **policyArn** *(string) --*

                The policy ARN.

        - **denied** *(dict) --*

          The policies and statements that denied the specified action.

          - **implicitDeny** *(dict) --*

            Information that implicitly denies the authorization. When a policy doesn't explicitly
            deny or allow an action on a resource it is considered an implicit deny.

            - **policies** *(list) --*

              Policies that don't contain a matching allow or deny statement for the specified
              action on the specified resource.

              - *(dict) --*

                Describes an AWS IoT policy.

                - **policyName** *(string) --*

                  The policy name.

                - **policyArn** *(string) --*

                  The policy ARN.

          - **explicitDeny** *(dict) --*

            Information that explicitly denies the authorization.

            - **policies** *(list) --*

              The policies that denied the authorization.

              - *(dict) --*

                Describes an AWS IoT policy.

                - **policyName** *(string) --*

                  The policy name.

                - **policyArn** *(string) --*

                  The policy ARN.

        - **authDecision** *(string) --*

          The final authorization decision of this scenario. Multiple statements are taken into
          account when determining the authorization decision. An explicit deny statement can
          override multiple allow statements.

        - **missingContextValues** *(list) --*

          Contains any missing context values found while evaluating policy.

          - *(string) --*
    """


_ClientTestAuthorizationauthInfosTypeDef = TypedDict(
    "_ClientTestAuthorizationauthInfosTypeDef",
    {"actionType": str, "resources": List[str]},
    total=False,
)


class ClientTestAuthorizationauthInfosTypeDef(_ClientTestAuthorizationauthInfosTypeDef):
    """
    Type definition for `ClientTestAuthorization` `authInfos`

    A collection of authorization information.

    - **actionType** *(string) --*

      The type of action for which the principal is being authorized.

    - **resources** *(list) --*

      The resources for which the principal is being authorized to perform the specified action.

      - *(string) --*
    """


_ClientTestInvokeAuthorizerResponseTypeDef = TypedDict(
    "_ClientTestInvokeAuthorizerResponseTypeDef",
    {
        "isAuthenticated": bool,
        "principalId": str,
        "policyDocuments": List[str],
        "refreshAfterInSeconds": int,
        "disconnectAfterInSeconds": int,
    },
    total=False,
)


class ClientTestInvokeAuthorizerResponseTypeDef(
    _ClientTestInvokeAuthorizerResponseTypeDef
):
    """
    Type definition for `ClientTestInvokeAuthorizer` `Response`

    - **isAuthenticated** *(boolean) --*

      True if the token is authenticated, otherwise false.

    - **principalId** *(string) --*

      The principal ID.

    - **policyDocuments** *(list) --*

      IAM policy documents.

      - *(string) --*

    - **refreshAfterInSeconds** *(integer) --*

      The number of seconds after which the temporary credentials are refreshed.

    - **disconnectAfterInSeconds** *(integer) --*

      The number of seconds after which the connection is terminated.
    """


_ClientTransferCertificateResponseTypeDef = TypedDict(
    "_ClientTransferCertificateResponseTypeDef",
    {"transferredCertificateArn": str},
    total=False,
)


class ClientTransferCertificateResponseTypeDef(
    _ClientTransferCertificateResponseTypeDef
):
    """
    Type definition for `ClientTransferCertificate` `Response`

    The output from the TransferCertificate operation.

    - **transferredCertificateArn** *(string) --*

      The ARN of the certificate.
    """


_ClientUpdateAccountAuditConfigurationauditCheckConfigurationsTypeDef = TypedDict(
    "_ClientUpdateAccountAuditConfigurationauditCheckConfigurationsTypeDef",
    {"enabled": bool},
    total=False,
)


class ClientUpdateAccountAuditConfigurationauditCheckConfigurationsTypeDef(
    _ClientUpdateAccountAuditConfigurationauditCheckConfigurationsTypeDef
):
    """
    Type definition for `ClientUpdateAccountAuditConfiguration` `auditCheckConfigurations`

    Which audit checks are enabled and disabled for this account.

    - **enabled** *(boolean) --*

      True if this audit check is enabled for this account.
    """


_ClientUpdateAccountAuditConfigurationauditNotificationTargetConfigurationsTypeDef = TypedDict(
    "_ClientUpdateAccountAuditConfigurationauditNotificationTargetConfigurationsTypeDef",
    {"targetArn": str, "roleArn": str, "enabled": bool},
    total=False,
)


class ClientUpdateAccountAuditConfigurationauditNotificationTargetConfigurationsTypeDef(
    _ClientUpdateAccountAuditConfigurationauditNotificationTargetConfigurationsTypeDef
):
    """
    Type definition for `ClientUpdateAccountAuditConfiguration` `auditNotificationTargetConfigurations`

    Information about the targets to which audit notifications are sent.

    - **targetArn** *(string) --*

      The ARN of the target (SNS topic) to which audit notifications are sent.

    - **roleArn** *(string) --*

      The ARN of the role that grants permission to send notifications to the target.

    - **enabled** *(boolean) --*

      True if notifications to the target are enabled.
    """


_ClientUpdateAuthorizerResponseTypeDef = TypedDict(
    "_ClientUpdateAuthorizerResponseTypeDef",
    {"authorizerName": str, "authorizerArn": str},
    total=False,
)


class ClientUpdateAuthorizerResponseTypeDef(_ClientUpdateAuthorizerResponseTypeDef):
    """
    Type definition for `ClientUpdateAuthorizer` `Response`

    - **authorizerName** *(string) --*

      The authorizer name.

    - **authorizerArn** *(string) --*

      The authorizer ARN.
    """


_ClientUpdateBillingGroupResponseTypeDef = TypedDict(
    "_ClientUpdateBillingGroupResponseTypeDef", {"version": int}, total=False
)


class ClientUpdateBillingGroupResponseTypeDef(_ClientUpdateBillingGroupResponseTypeDef):
    """
    Type definition for `ClientUpdateBillingGroup` `Response`

    - **version** *(integer) --*

      The latest version of the billing group.
    """


_ClientUpdateBillingGroupbillingGroupPropertiesTypeDef = TypedDict(
    "_ClientUpdateBillingGroupbillingGroupPropertiesTypeDef",
    {"billingGroupDescription": str},
    total=False,
)


class ClientUpdateBillingGroupbillingGroupPropertiesTypeDef(
    _ClientUpdateBillingGroupbillingGroupPropertiesTypeDef
):
    """
    Type definition for `ClientUpdateBillingGroup` `billingGroupProperties`

    The properties of the billing group.

    - **billingGroupDescription** *(string) --*

      The description of the billing group.
    """


_ClientUpdateCaCertificateregistrationConfigTypeDef = TypedDict(
    "_ClientUpdateCaCertificateregistrationConfigTypeDef",
    {"templateBody": str, "roleArn": str},
    total=False,
)


class ClientUpdateCaCertificateregistrationConfigTypeDef(
    _ClientUpdateCaCertificateregistrationConfigTypeDef
):
    """
    Type definition for `ClientUpdateCaCertificate` `registrationConfig`

    Information about the registration configuration.

    - **templateBody** *(string) --*

      The template body.

    - **roleArn** *(string) --*

      The ARN of the role.
    """


_ClientUpdateDynamicThingGroupResponseTypeDef = TypedDict(
    "_ClientUpdateDynamicThingGroupResponseTypeDef", {"version": int}, total=False
)


class ClientUpdateDynamicThingGroupResponseTypeDef(
    _ClientUpdateDynamicThingGroupResponseTypeDef
):
    """
    Type definition for `ClientUpdateDynamicThingGroup` `Response`

    - **version** *(integer) --*

      The dynamic thing group version.
    """


_ClientUpdateDynamicThingGroupthingGroupPropertiesattributePayloadTypeDef = TypedDict(
    "_ClientUpdateDynamicThingGroupthingGroupPropertiesattributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)


class ClientUpdateDynamicThingGroupthingGroupPropertiesattributePayloadTypeDef(
    _ClientUpdateDynamicThingGroupthingGroupPropertiesattributePayloadTypeDef
):
    """
    Type definition for `ClientUpdateDynamicThingGroupthingGroupProperties` `attributePayload`

    The thing group attributes in JSON format.

    - **attributes** *(dict) --*

      A JSON string containing up to three key-value pair in JSON format. For example:

       ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``

      - *(string) --*

        - *(string) --*

    - **merge** *(boolean) --*

      Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with
      the attributes stored in the registry, instead of overwriting them.

      To remove an attribute, call ``UpdateThing`` with an empty attribute value.

      .. note::

        The ``merge`` attribute is only valid when calling ``UpdateThing`` or ``UpdateThingGroup`` .
    """


_ClientUpdateDynamicThingGroupthingGroupPropertiesTypeDef = TypedDict(
    "_ClientUpdateDynamicThingGroupthingGroupPropertiesTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": ClientUpdateDynamicThingGroupthingGroupPropertiesattributePayloadTypeDef,
    },
    total=False,
)


class ClientUpdateDynamicThingGroupthingGroupPropertiesTypeDef(
    _ClientUpdateDynamicThingGroupthingGroupPropertiesTypeDef
):
    """
    Type definition for `ClientUpdateDynamicThingGroup` `thingGroupProperties`

    The dynamic thing group properties to update.

    - **thingGroupDescription** *(string) --*

      The thing group description.

    - **attributePayload** *(dict) --*

      The thing group attributes in JSON format.

      - **attributes** *(dict) --*

        A JSON string containing up to three key-value pair in JSON format. For example:

         ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``

        - *(string) --*

          - *(string) --*

      - **merge** *(boolean) --*

        Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with
        the attributes stored in the registry, instead of overwriting them.

        To remove an attribute, call ``UpdateThing`` with an empty attribute value.

        .. note::

          The ``merge`` attribute is only valid when calling ``UpdateThing`` or ``UpdateThingGroup`` .
    """


_ClientUpdateEventConfigurationseventConfigurationsTypeDef = TypedDict(
    "_ClientUpdateEventConfigurationseventConfigurationsTypeDef",
    {"Enabled": bool},
    total=False,
)


class ClientUpdateEventConfigurationseventConfigurationsTypeDef(
    _ClientUpdateEventConfigurationseventConfigurationsTypeDef
):
    """
    Type definition for `ClientUpdateEventConfigurations` `eventConfigurations`

    Configuration.

    - **Enabled** *(boolean) --*

      True to enable the configuration.
    """


_ClientUpdateIndexingConfigurationthingGroupIndexingConfigurationcustomFieldsTypeDef = TypedDict(
    "_ClientUpdateIndexingConfigurationthingGroupIndexingConfigurationcustomFieldsTypeDef",
    {"name": str, "type": str},
    total=False,
)


class ClientUpdateIndexingConfigurationthingGroupIndexingConfigurationcustomFieldsTypeDef(
    _ClientUpdateIndexingConfigurationthingGroupIndexingConfigurationcustomFieldsTypeDef
):
    """
    Type definition for `ClientUpdateIndexingConfigurationthingGroupIndexingConfiguration` `customFields`

    Describes the name and data type at a field.

    - **name** *(string) --*

      The name of the field.

    - **type** *(string) --*

      The datatype of the field.
    """


_ClientUpdateIndexingConfigurationthingGroupIndexingConfigurationmanagedFieldsTypeDef = TypedDict(
    "_ClientUpdateIndexingConfigurationthingGroupIndexingConfigurationmanagedFieldsTypeDef",
    {"name": str, "type": str},
    total=False,
)


class ClientUpdateIndexingConfigurationthingGroupIndexingConfigurationmanagedFieldsTypeDef(
    _ClientUpdateIndexingConfigurationthingGroupIndexingConfigurationmanagedFieldsTypeDef
):
    """
    Type definition for `ClientUpdateIndexingConfigurationthingGroupIndexingConfiguration` `managedFields`

    Describes the name and data type at a field.

    - **name** *(string) --*

      The name of the field.

    - **type** *(string) --*

      The datatype of the field.
    """


_RequiredClientUpdateIndexingConfigurationthingGroupIndexingConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateIndexingConfigurationthingGroupIndexingConfigurationTypeDef",
    {"thingGroupIndexingMode": str},
)
_OptionalClientUpdateIndexingConfigurationthingGroupIndexingConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateIndexingConfigurationthingGroupIndexingConfigurationTypeDef",
    {
        "managedFields": List[
            ClientUpdateIndexingConfigurationthingGroupIndexingConfigurationmanagedFieldsTypeDef
        ],
        "customFields": List[
            ClientUpdateIndexingConfigurationthingGroupIndexingConfigurationcustomFieldsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateIndexingConfigurationthingGroupIndexingConfigurationTypeDef(
    _RequiredClientUpdateIndexingConfigurationthingGroupIndexingConfigurationTypeDef,
    _OptionalClientUpdateIndexingConfigurationthingGroupIndexingConfigurationTypeDef,
):
    """
    Type definition for `ClientUpdateIndexingConfiguration` `thingGroupIndexingConfiguration`

    Thing group indexing configuration.

    - **thingGroupIndexingMode** *(string) --* **[REQUIRED]**

      Thing group indexing mode.

    - **managedFields** *(list) --*

      Contains fields that are indexed and whose types are already known by the Fleet Indexing
      service.

      - *(dict) --*

        Describes the name and data type at a field.

        - **name** *(string) --*

          The name of the field.

        - **type** *(string) --*

          The datatype of the field.

    - **customFields** *(list) --*

      Contains custom field names and their data type.

      - *(dict) --*

        Describes the name and data type at a field.

        - **name** *(string) --*

          The name of the field.

        - **type** *(string) --*

          The datatype of the field.
    """


_ClientUpdateIndexingConfigurationthingIndexingConfigurationcustomFieldsTypeDef = TypedDict(
    "_ClientUpdateIndexingConfigurationthingIndexingConfigurationcustomFieldsTypeDef",
    {"name": str, "type": str},
    total=False,
)


class ClientUpdateIndexingConfigurationthingIndexingConfigurationcustomFieldsTypeDef(
    _ClientUpdateIndexingConfigurationthingIndexingConfigurationcustomFieldsTypeDef
):
    """
    Type definition for `ClientUpdateIndexingConfigurationthingIndexingConfiguration` `customFields`

    Describes the name and data type at a field.

    - **name** *(string) --*

      The name of the field.

    - **type** *(string) --*

      The datatype of the field.
    """


_ClientUpdateIndexingConfigurationthingIndexingConfigurationmanagedFieldsTypeDef = TypedDict(
    "_ClientUpdateIndexingConfigurationthingIndexingConfigurationmanagedFieldsTypeDef",
    {"name": str, "type": str},
    total=False,
)


class ClientUpdateIndexingConfigurationthingIndexingConfigurationmanagedFieldsTypeDef(
    _ClientUpdateIndexingConfigurationthingIndexingConfigurationmanagedFieldsTypeDef
):
    """
    Type definition for `ClientUpdateIndexingConfigurationthingIndexingConfiguration` `managedFields`

    Describes the name and data type at a field.

    - **name** *(string) --*

      The name of the field.

    - **type** *(string) --*

      The datatype of the field.
    """


_RequiredClientUpdateIndexingConfigurationthingIndexingConfigurationTypeDef = TypedDict(
    "_RequiredClientUpdateIndexingConfigurationthingIndexingConfigurationTypeDef",
    {"thingIndexingMode": str},
)
_OptionalClientUpdateIndexingConfigurationthingIndexingConfigurationTypeDef = TypedDict(
    "_OptionalClientUpdateIndexingConfigurationthingIndexingConfigurationTypeDef",
    {
        "thingConnectivityIndexingMode": str,
        "managedFields": List[
            ClientUpdateIndexingConfigurationthingIndexingConfigurationmanagedFieldsTypeDef
        ],
        "customFields": List[
            ClientUpdateIndexingConfigurationthingIndexingConfigurationcustomFieldsTypeDef
        ],
    },
    total=False,
)


class ClientUpdateIndexingConfigurationthingIndexingConfigurationTypeDef(
    _RequiredClientUpdateIndexingConfigurationthingIndexingConfigurationTypeDef,
    _OptionalClientUpdateIndexingConfigurationthingIndexingConfigurationTypeDef,
):
    """
    Type definition for `ClientUpdateIndexingConfiguration` `thingIndexingConfiguration`

    Thing indexing configuration.

    - **thingIndexingMode** *(string) --* **[REQUIRED]**

      Thing indexing mode. Valid values are:

      * REGISTRY – Your thing index contains registry data only.

      * REGISTRY_AND_SHADOW - Your thing index contains registry and shadow data.

      * OFF - Thing indexing is disabled.

    - **thingConnectivityIndexingMode** *(string) --*

      Thing connectivity indexing mode. Valid values are:

      * STATUS – Your thing index contains connectivity status. To enable thing connectivity
      indexing, thingIndexMode must not be set to OFF.

      * OFF - Thing connectivity status indexing is disabled.

    - **managedFields** *(list) --*

      Contains fields that are indexed and whose types are already known by the Fleet Indexing
      service.

      - *(dict) --*

        Describes the name and data type at a field.

        - **name** *(string) --*

          The name of the field.

        - **type** *(string) --*

          The datatype of the field.

    - **customFields** *(list) --*

      Contains custom field names and their data type.

      - *(dict) --*

        Describes the name and data type at a field.

        - **name** *(string) --*

          The name of the field.

        - **type** *(string) --*

          The datatype of the field.
    """


_ClientUpdateJobabortConfigcriteriaListTypeDef = TypedDict(
    "_ClientUpdateJobabortConfigcriteriaListTypeDef",
    {
        "failureType": str,
        "action": str,
        "thresholdPercentage": float,
        "minNumberOfExecutedThings": int,
    },
)


class ClientUpdateJobabortConfigcriteriaListTypeDef(
    _ClientUpdateJobabortConfigcriteriaListTypeDef
):
    """
    Type definition for `ClientUpdateJobabortConfig` `criteriaList`

    Details of abort criteria to define rules to abort the job.

    - **failureType** *(string) --* **[REQUIRED]**

      The type of job execution failure to define a rule to initiate a job abort.

    - **action** *(string) --* **[REQUIRED]**

      The type of abort action to initiate a job abort.

    - **thresholdPercentage** *(float) --* **[REQUIRED]**

      The threshold as a percentage of the total number of executed things that will initiate a
      job abort.

      AWS IoT supports up to two digits after the decimal (for example, 10.9 and 10.99, but not
      10.999).

    - **minNumberOfExecutedThings** *(integer) --* **[REQUIRED]**

      Minimum number of executed things before evaluating an abort rule.
    """


_ClientUpdateJobabortConfigTypeDef = TypedDict(
    "_ClientUpdateJobabortConfigTypeDef",
    {"criteriaList": List[ClientUpdateJobabortConfigcriteriaListTypeDef]},
)


class ClientUpdateJobabortConfigTypeDef(_ClientUpdateJobabortConfigTypeDef):
    """
    Type definition for `ClientUpdateJob` `abortConfig`

    Allows you to create criteria to abort a job.

    - **criteriaList** *(list) --* **[REQUIRED]**

      The list of abort criteria to define rules to abort the job.

      - *(dict) --*

        Details of abort criteria to define rules to abort the job.

        - **failureType** *(string) --* **[REQUIRED]**

          The type of job execution failure to define a rule to initiate a job abort.

        - **action** *(string) --* **[REQUIRED]**

          The type of abort action to initiate a job abort.

        - **thresholdPercentage** *(float) --* **[REQUIRED]**

          The threshold as a percentage of the total number of executed things that will initiate a
          job abort.

          AWS IoT supports up to two digits after the decimal (for example, 10.9 and 10.99, but not
          10.999).

        - **minNumberOfExecutedThings** *(integer) --* **[REQUIRED]**

          Minimum number of executed things before evaluating an abort rule.
    """


_ClientUpdateJobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef = TypedDict(
    "_ClientUpdateJobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef",
    {"numberOfNotifiedThings": int, "numberOfSucceededThings": int},
    total=False,
)


class ClientUpdateJobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef(
    _ClientUpdateJobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef
):
    """
    Type definition for `ClientUpdateJobjobExecutionsRolloutConfigexponentialRate` `rateIncreaseCriteria`

    The criteria to initiate the increase in rate of rollout for a job.

    AWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).

    - **numberOfNotifiedThings** *(integer) --*

      The threshold for number of notified things that will initiate the increase in rate of
      rollout.

    - **numberOfSucceededThings** *(integer) --*

      The threshold for number of succeeded things that will initiate the increase in rate of
      rollout.
    """


_ClientUpdateJobjobExecutionsRolloutConfigexponentialRateTypeDef = TypedDict(
    "_ClientUpdateJobjobExecutionsRolloutConfigexponentialRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": ClientUpdateJobjobExecutionsRolloutConfigexponentialRaterateIncreaseCriteriaTypeDef,
    },
)


class ClientUpdateJobjobExecutionsRolloutConfigexponentialRateTypeDef(
    _ClientUpdateJobjobExecutionsRolloutConfigexponentialRateTypeDef
):
    """
    Type definition for `ClientUpdateJobjobExecutionsRolloutConfig` `exponentialRate`

    The rate of increase for a job rollout. This parameter allows you to define an exponential rate
    for a job rollout.

    - **baseRatePerMinute** *(integer) --* **[REQUIRED]**

      The minimum number of things that will be notified of a pending job, per minute at the start
      of job rollout. This parameter allows you to define the initial rate of rollout.

    - **incrementFactor** *(float) --* **[REQUIRED]**

      The exponential factor to increase the rate of rollout for a job.

    - **rateIncreaseCriteria** *(dict) --* **[REQUIRED]**

      The criteria to initiate the increase in rate of rollout for a job.

      AWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).

      - **numberOfNotifiedThings** *(integer) --*

        The threshold for number of notified things that will initiate the increase in rate of
        rollout.

      - **numberOfSucceededThings** *(integer) --*

        The threshold for number of succeeded things that will initiate the increase in rate of
        rollout.
    """


_ClientUpdateJobjobExecutionsRolloutConfigTypeDef = TypedDict(
    "_ClientUpdateJobjobExecutionsRolloutConfigTypeDef",
    {
        "maximumPerMinute": int,
        "exponentialRate": ClientUpdateJobjobExecutionsRolloutConfigexponentialRateTypeDef,
    },
    total=False,
)


class ClientUpdateJobjobExecutionsRolloutConfigTypeDef(
    _ClientUpdateJobjobExecutionsRolloutConfigTypeDef
):
    """
    Type definition for `ClientUpdateJob` `jobExecutionsRolloutConfig`

    Allows you to create a staged rollout of the job.

    - **maximumPerMinute** *(integer) --*

      The maximum number of things that will be notified of a pending job, per minute. This parameter
      allows you to create a staged rollout.

    - **exponentialRate** *(dict) --*

      The rate of increase for a job rollout. This parameter allows you to define an exponential rate
      for a job rollout.

      - **baseRatePerMinute** *(integer) --* **[REQUIRED]**

        The minimum number of things that will be notified of a pending job, per minute at the start
        of job rollout. This parameter allows you to define the initial rate of rollout.

      - **incrementFactor** *(float) --* **[REQUIRED]**

        The exponential factor to increase the rate of rollout for a job.

      - **rateIncreaseCriteria** *(dict) --* **[REQUIRED]**

        The criteria to initiate the increase in rate of rollout for a job.

        AWS IoT supports up to one digit after the decimal (for example, 1.5, but not 1.55).

        - **numberOfNotifiedThings** *(integer) --*

          The threshold for number of notified things that will initiate the increase in rate of
          rollout.

        - **numberOfSucceededThings** *(integer) --*

          The threshold for number of succeeded things that will initiate the increase in rate of
          rollout.
    """


_ClientUpdateJobpresignedUrlConfigTypeDef = TypedDict(
    "_ClientUpdateJobpresignedUrlConfigTypeDef",
    {"roleArn": str, "expiresInSec": int},
    total=False,
)


class ClientUpdateJobpresignedUrlConfigTypeDef(
    _ClientUpdateJobpresignedUrlConfigTypeDef
):
    """
    Type definition for `ClientUpdateJob` `presignedUrlConfig`

    Configuration information for pre-signed S3 URLs.

    - **roleArn** *(string) --*

      The ARN of an IAM role that grants grants permission to download files from the S3 bucket where
      the job data/updates are stored. The role must also grant permission for IoT to download the
      files.

    - **expiresInSec** *(integer) --*

      How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value
      is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job
      document.
    """


_ClientUpdateJobtimeoutConfigTypeDef = TypedDict(
    "_ClientUpdateJobtimeoutConfigTypeDef",
    {"inProgressTimeoutInMinutes": int},
    total=False,
)


class ClientUpdateJobtimeoutConfigTypeDef(_ClientUpdateJobtimeoutConfigTypeDef):
    """
    Type definition for `ClientUpdateJob` `timeoutConfig`

    Specifies the amount of time each device has to finish its execution of the job. The timer is
    started when the job execution status is set to ``IN_PROGRESS`` . If the job execution status is
    not set to another terminal state before the time expires, it will be automatically set to
    ``TIMED_OUT`` .

    - **inProgressTimeoutInMinutes** *(integer) --*

      Specifies the amount of time, in minutes, this device has to finish execution of this job. The
      timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in
      progress timer can't be updated and will apply to all job executions for the job. Whenever a
      job execution remains in the IN_PROGRESS status for longer than this interval, the job
      execution will fail and switch to the terminal ``TIMED_OUT`` status.
    """


_ClientUpdateMitigationActionResponseTypeDef = TypedDict(
    "_ClientUpdateMitigationActionResponseTypeDef",
    {"actionArn": str, "actionId": str},
    total=False,
)


class ClientUpdateMitigationActionResponseTypeDef(
    _ClientUpdateMitigationActionResponseTypeDef
):
    """
    Type definition for `ClientUpdateMitigationAction` `Response`

    - **actionArn** *(string) --*

      The ARN for the new mitigation action.

    - **actionId** *(string) --*

      A unique identifier for the mitigation action.
    """


_RequiredClientUpdateMitigationActionactionParamsaddThingsToThingGroupParamsTypeDef = TypedDict(
    "_RequiredClientUpdateMitigationActionactionParamsaddThingsToThingGroupParamsTypeDef",
    {"thingGroupNames": List[str]},
)
_OptionalClientUpdateMitigationActionactionParamsaddThingsToThingGroupParamsTypeDef = TypedDict(
    "_OptionalClientUpdateMitigationActionactionParamsaddThingsToThingGroupParamsTypeDef",
    {"overrideDynamicGroups": bool},
    total=False,
)


class ClientUpdateMitigationActionactionParamsaddThingsToThingGroupParamsTypeDef(
    _RequiredClientUpdateMitigationActionactionParamsaddThingsToThingGroupParamsTypeDef,
    _OptionalClientUpdateMitigationActionactionParamsaddThingsToThingGroupParamsTypeDef,
):
    """
    Type definition for `ClientUpdateMitigationActionactionParams` `addThingsToThingGroupParams`

    Parameters to define a mitigation action that moves devices associated with a certificate to
    one or more specified thing groups, typically for quarantine.

    - **thingGroupNames** *(list) --* **[REQUIRED]**

      The list of groups to which you want to add the things that triggered the mitigation action.
      You can add a thing to a maximum of 10 groups, but you cannot add a thing to more than one
      group in the same hierarchy.

      - *(string) --*

    - **overrideDynamicGroups** *(boolean) --*

      Specifies if this mitigation action can move the things that triggered the mitigation action
      even if they are part of one or more dynamic things groups.
    """


_ClientUpdateMitigationActionactionParamsenableIoTLoggingParamsTypeDef = TypedDict(
    "_ClientUpdateMitigationActionactionParamsenableIoTLoggingParamsTypeDef",
    {"roleArnForLogging": str, "logLevel": str},
)


class ClientUpdateMitigationActionactionParamsenableIoTLoggingParamsTypeDef(
    _ClientUpdateMitigationActionactionParamsenableIoTLoggingParamsTypeDef
):
    """
    Type definition for `ClientUpdateMitigationActionactionParams` `enableIoTLoggingParams`

    Parameters to define a mitigation action that enables AWS IoT logging at a specified level of
    detail.

    - **roleArnForLogging** *(string) --* **[REQUIRED]**

      The ARN of the IAM role used for logging.

    - **logLevel** *(string) --* **[REQUIRED]**

      Specifies the types of information to be logged.
    """


_ClientUpdateMitigationActionactionParamspublishFindingToSnsParamsTypeDef = TypedDict(
    "_ClientUpdateMitigationActionactionParamspublishFindingToSnsParamsTypeDef",
    {"topicArn": str},
)


class ClientUpdateMitigationActionactionParamspublishFindingToSnsParamsTypeDef(
    _ClientUpdateMitigationActionactionParamspublishFindingToSnsParamsTypeDef
):
    """
    Type definition for `ClientUpdateMitigationActionactionParams` `publishFindingToSnsParams`

    Parameters to define a mitigation action that publishes findings to Amazon SNS. You can
    implement your own custom actions in response to the Amazon SNS messages.

    - **topicArn** *(string) --* **[REQUIRED]**

      The ARN of the topic to which you want to publish the findings.
    """


_ClientUpdateMitigationActionactionParamsreplaceDefaultPolicyVersionParamsTypeDef = TypedDict(
    "_ClientUpdateMitigationActionactionParamsreplaceDefaultPolicyVersionParamsTypeDef",
    {"templateName": str},
)


class ClientUpdateMitigationActionactionParamsreplaceDefaultPolicyVersionParamsTypeDef(
    _ClientUpdateMitigationActionactionParamsreplaceDefaultPolicyVersionParamsTypeDef
):
    """
    Type definition for `ClientUpdateMitigationActionactionParams` `replaceDefaultPolicyVersionParams`

    Parameters to define a mitigation action that adds a blank policy to restrict permissions.

    - **templateName** *(string) --* **[REQUIRED]**

      The name of the template to be applied. The only supported value is ``BLANK_POLICY`` .
    """


_ClientUpdateMitigationActionactionParamsupdateCACertificateParamsTypeDef = TypedDict(
    "_ClientUpdateMitigationActionactionParamsupdateCACertificateParamsTypeDef",
    {"action": str},
)


class ClientUpdateMitigationActionactionParamsupdateCACertificateParamsTypeDef(
    _ClientUpdateMitigationActionactionParamsupdateCACertificateParamsTypeDef
):
    """
    Type definition for `ClientUpdateMitigationActionactionParams` `updateCACertificateParams`

    Parameters to define a mitigation action that changes the state of the CA certificate to
    inactive.

    - **action** *(string) --* **[REQUIRED]**

      The action that you want to apply to the CA cerrtificate. The only supported value is
      ``DEACTIVATE`` .
    """


_ClientUpdateMitigationActionactionParamsupdateDeviceCertificateParamsTypeDef = TypedDict(
    "_ClientUpdateMitigationActionactionParamsupdateDeviceCertificateParamsTypeDef",
    {"action": str},
)


class ClientUpdateMitigationActionactionParamsupdateDeviceCertificateParamsTypeDef(
    _ClientUpdateMitigationActionactionParamsupdateDeviceCertificateParamsTypeDef
):
    """
    Type definition for `ClientUpdateMitigationActionactionParams` `updateDeviceCertificateParams`

    Parameters to define a mitigation action that changes the state of the device certificate to
    inactive.

    - **action** *(string) --* **[REQUIRED]**

      The action that you want to apply to the device cerrtificate. The only supported value is
      ``DEACTIVATE`` .
    """


_ClientUpdateMitigationActionactionParamsTypeDef = TypedDict(
    "_ClientUpdateMitigationActionactionParamsTypeDef",
    {
        "updateDeviceCertificateParams": ClientUpdateMitigationActionactionParamsupdateDeviceCertificateParamsTypeDef,
        "updateCACertificateParams": ClientUpdateMitigationActionactionParamsupdateCACertificateParamsTypeDef,
        "addThingsToThingGroupParams": ClientUpdateMitigationActionactionParamsaddThingsToThingGroupParamsTypeDef,
        "replaceDefaultPolicyVersionParams": ClientUpdateMitigationActionactionParamsreplaceDefaultPolicyVersionParamsTypeDef,
        "enableIoTLoggingParams": ClientUpdateMitigationActionactionParamsenableIoTLoggingParamsTypeDef,
        "publishFindingToSnsParams": ClientUpdateMitigationActionactionParamspublishFindingToSnsParamsTypeDef,
    },
    total=False,
)


class ClientUpdateMitigationActionactionParamsTypeDef(
    _ClientUpdateMitigationActionactionParamsTypeDef
):
    """
    Type definition for `ClientUpdateMitigationAction` `actionParams`

    Defines the type of action and the parameters for that action.

    - **updateDeviceCertificateParams** *(dict) --*

      Parameters to define a mitigation action that changes the state of the device certificate to
      inactive.

      - **action** *(string) --* **[REQUIRED]**

        The action that you want to apply to the device cerrtificate. The only supported value is
        ``DEACTIVATE`` .

    - **updateCACertificateParams** *(dict) --*

      Parameters to define a mitigation action that changes the state of the CA certificate to
      inactive.

      - **action** *(string) --* **[REQUIRED]**

        The action that you want to apply to the CA cerrtificate. The only supported value is
        ``DEACTIVATE`` .

    - **addThingsToThingGroupParams** *(dict) --*

      Parameters to define a mitigation action that moves devices associated with a certificate to
      one or more specified thing groups, typically for quarantine.

      - **thingGroupNames** *(list) --* **[REQUIRED]**

        The list of groups to which you want to add the things that triggered the mitigation action.
        You can add a thing to a maximum of 10 groups, but you cannot add a thing to more than one
        group in the same hierarchy.

        - *(string) --*

      - **overrideDynamicGroups** *(boolean) --*

        Specifies if this mitigation action can move the things that triggered the mitigation action
        even if they are part of one or more dynamic things groups.

    - **replaceDefaultPolicyVersionParams** *(dict) --*

      Parameters to define a mitigation action that adds a blank policy to restrict permissions.

      - **templateName** *(string) --* **[REQUIRED]**

        The name of the template to be applied. The only supported value is ``BLANK_POLICY`` .

    - **enableIoTLoggingParams** *(dict) --*

      Parameters to define a mitigation action that enables AWS IoT logging at a specified level of
      detail.

      - **roleArnForLogging** *(string) --* **[REQUIRED]**

        The ARN of the IAM role used for logging.

      - **logLevel** *(string) --* **[REQUIRED]**

        Specifies the types of information to be logged.

    - **publishFindingToSnsParams** *(dict) --*

      Parameters to define a mitigation action that publishes findings to Amazon SNS. You can
      implement your own custom actions in response to the Amazon SNS messages.

      - **topicArn** *(string) --* **[REQUIRED]**

        The ARN of the topic to which you want to publish the findings.
    """


_ClientUpdateRoleAliasResponseTypeDef = TypedDict(
    "_ClientUpdateRoleAliasResponseTypeDef",
    {"roleAlias": str, "roleAliasArn": str},
    total=False,
)


class ClientUpdateRoleAliasResponseTypeDef(_ClientUpdateRoleAliasResponseTypeDef):
    """
    Type definition for `ClientUpdateRoleAlias` `Response`

    - **roleAlias** *(string) --*

      The role alias.

    - **roleAliasArn** *(string) --*

      The role alias ARN.
    """


_ClientUpdateScheduledAuditResponseTypeDef = TypedDict(
    "_ClientUpdateScheduledAuditResponseTypeDef",
    {"scheduledAuditArn": str},
    total=False,
)


class ClientUpdateScheduledAuditResponseTypeDef(
    _ClientUpdateScheduledAuditResponseTypeDef
):
    """
    Type definition for `ClientUpdateScheduledAudit` `Response`

    - **scheduledAuditArn** *(string) --*

      The ARN of the scheduled audit.
    """


_ClientUpdateSecurityProfileResponsealertTargetsTypeDef = TypedDict(
    "_ClientUpdateSecurityProfileResponsealertTargetsTypeDef",
    {"alertTargetArn": str, "roleArn": str},
    total=False,
)


class ClientUpdateSecurityProfileResponsealertTargetsTypeDef(
    _ClientUpdateSecurityProfileResponsealertTargetsTypeDef
):
    """
    Type definition for `ClientUpdateSecurityProfileResponse` `alertTargets`

    A structure containing the alert target ARN and the role ARN.

    - **alertTargetArn** *(string) --*

      The ARN of the notification target to which alerts are sent.

    - **roleArn** *(string) --*

      The ARN of the role that grants permission to send alerts to the notification target.
    """


_ClientUpdateSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef = TypedDict(
    "_ClientUpdateSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)


class ClientUpdateSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef(
    _ClientUpdateSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef
):
    """
    Type definition for `ClientUpdateSecurityProfileResponsebehaviorscriteria` `statisticalThreshold`

    A statistical ranking (percentile) which indicates a threshold value by which a
    behavior is determined to be in compliance or in violation of the behavior.

    - **statistic** *(string) --*

      The percentile which resolves to a threshold value by which compliance with a
      behavior is determined. Metrics are collected over the specified period
      (``durationSeconds`` ) from all reporting devices in your account and statistical
      ranks are calculated. Then, the measurements from a device are collected over the
      same period. If the accumulated measurements from the device fall above or below
      (``comparisonOperator`` ) the value associated with the percentile specified, then
      the device is considered to be in compliance with the behavior, otherwise a violation
      occurs.
    """


_ClientUpdateSecurityProfileResponsebehaviorscriteriavalueTypeDef = TypedDict(
    "_ClientUpdateSecurityProfileResponsebehaviorscriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ClientUpdateSecurityProfileResponsebehaviorscriteriavalueTypeDef(
    _ClientUpdateSecurityProfileResponsebehaviorscriteriavalueTypeDef
):
    """
    Type definition for `ClientUpdateSecurityProfileResponsebehaviorscriteria` `value`

    The value to be compared with the ``metric`` .

    - **count** *(integer) --*

      If the ``comparisonOperator`` calls for a numeric value, use this to specify that
      numeric value to be compared with the ``metric`` .

    - **cidrs** *(list) --*

      If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set
      to be compared with the ``metric`` .

      - *(string) --*

    - **ports** *(list) --*

      If the ``comparisonOperator`` calls for a set of ports, use this to specify that set
      to be compared with the ``metric`` .

      - *(integer) --*
    """


_ClientUpdateSecurityProfileResponsebehaviorscriteriaTypeDef = TypedDict(
    "_ClientUpdateSecurityProfileResponsebehaviorscriteriaTypeDef",
    {
        "comparisonOperator": str,
        "value": ClientUpdateSecurityProfileResponsebehaviorscriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientUpdateSecurityProfileResponsebehaviorscriteriastatisticalThresholdTypeDef,
    },
    total=False,
)


class ClientUpdateSecurityProfileResponsebehaviorscriteriaTypeDef(
    _ClientUpdateSecurityProfileResponsebehaviorscriteriaTypeDef
):
    """
    Type definition for `ClientUpdateSecurityProfileResponsebehaviors` `criteria`

    The criteria that determine if a device is behaving normally in regard to the ``metric`` .

    - **comparisonOperator** *(string) --*

      The operator that relates the thing measured (``metric`` ) to the criteria (containing
      a ``value`` or ``statisticalThreshold`` ).

    - **value** *(dict) --*

      The value to be compared with the ``metric`` .

      - **count** *(integer) --*

        If the ``comparisonOperator`` calls for a numeric value, use this to specify that
        numeric value to be compared with the ``metric`` .

      - **cidrs** *(list) --*

        If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set
        to be compared with the ``metric`` .

        - *(string) --*

      - **ports** *(list) --*

        If the ``comparisonOperator`` calls for a set of ports, use this to specify that set
        to be compared with the ``metric`` .

        - *(integer) --*

    - **durationSeconds** *(integer) --*

      Use this to specify the time duration over which the behavior is evaluated, for those
      criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
      ``statisticalThreshhold`` metric comparison, measurements from all devices are
      accumulated over this time duration before being used to calculate percentiles, and
      later, measurements from an individual device are also accumulated over this time
      duration before being given a percentile rank.

    - **consecutiveDatapointsToAlarm** *(integer) --*

      If a device is in violation of the behavior for the specified number of consecutive
      datapoints, an alarm occurs. If not specified, the default is 1.

    - **consecutiveDatapointsToClear** *(integer) --*

      If an alarm has occurred and the offending device is no longer in violation of the
      behavior for the specified number of consecutive datapoints, the alarm is cleared. If
      not specified, the default is 1.

    - **statisticalThreshold** *(dict) --*

      A statistical ranking (percentile) which indicates a threshold value by which a
      behavior is determined to be in compliance or in violation of the behavior.

      - **statistic** *(string) --*

        The percentile which resolves to a threshold value by which compliance with a
        behavior is determined. Metrics are collected over the specified period
        (``durationSeconds`` ) from all reporting devices in your account and statistical
        ranks are calculated. Then, the measurements from a device are collected over the
        same period. If the accumulated measurements from the device fall above or below
        (``comparisonOperator`` ) the value associated with the percentile specified, then
        the device is considered to be in compliance with the behavior, otherwise a violation
        occurs.
    """


_ClientUpdateSecurityProfileResponsebehaviorsTypeDef = TypedDict(
    "_ClientUpdateSecurityProfileResponsebehaviorsTypeDef",
    {
        "name": str,
        "metric": str,
        "criteria": ClientUpdateSecurityProfileResponsebehaviorscriteriaTypeDef,
    },
    total=False,
)


class ClientUpdateSecurityProfileResponsebehaviorsTypeDef(
    _ClientUpdateSecurityProfileResponsebehaviorsTypeDef
):
    """
    Type definition for `ClientUpdateSecurityProfileResponse` `behaviors`

    A Device Defender security profile behavior.

    - **name** *(string) --*

      The name you have given to the behavior.

    - **metric** *(string) --*

      What is measured by the behavior.

    - **criteria** *(dict) --*

      The criteria that determine if a device is behaving normally in regard to the ``metric`` .

      - **comparisonOperator** *(string) --*

        The operator that relates the thing measured (``metric`` ) to the criteria (containing
        a ``value`` or ``statisticalThreshold`` ).

      - **value** *(dict) --*

        The value to be compared with the ``metric`` .

        - **count** *(integer) --*

          If the ``comparisonOperator`` calls for a numeric value, use this to specify that
          numeric value to be compared with the ``metric`` .

        - **cidrs** *(list) --*

          If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set
          to be compared with the ``metric`` .

          - *(string) --*

        - **ports** *(list) --*

          If the ``comparisonOperator`` calls for a set of ports, use this to specify that set
          to be compared with the ``metric`` .

          - *(integer) --*

      - **durationSeconds** *(integer) --*

        Use this to specify the time duration over which the behavior is evaluated, for those
        criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
        ``statisticalThreshhold`` metric comparison, measurements from all devices are
        accumulated over this time duration before being used to calculate percentiles, and
        later, measurements from an individual device are also accumulated over this time
        duration before being given a percentile rank.

      - **consecutiveDatapointsToAlarm** *(integer) --*

        If a device is in violation of the behavior for the specified number of consecutive
        datapoints, an alarm occurs. If not specified, the default is 1.

      - **consecutiveDatapointsToClear** *(integer) --*

        If an alarm has occurred and the offending device is no longer in violation of the
        behavior for the specified number of consecutive datapoints, the alarm is cleared. If
        not specified, the default is 1.

      - **statisticalThreshold** *(dict) --*

        A statistical ranking (percentile) which indicates a threshold value by which a
        behavior is determined to be in compliance or in violation of the behavior.

        - **statistic** *(string) --*

          The percentile which resolves to a threshold value by which compliance with a
          behavior is determined. Metrics are collected over the specified period
          (``durationSeconds`` ) from all reporting devices in your account and statistical
          ranks are calculated. Then, the measurements from a device are collected over the
          same period. If the accumulated measurements from the device fall above or below
          (``comparisonOperator`` ) the value associated with the percentile specified, then
          the device is considered to be in compliance with the behavior, otherwise a violation
          occurs.
    """


_ClientUpdateSecurityProfileResponseTypeDef = TypedDict(
    "_ClientUpdateSecurityProfileResponseTypeDef",
    {
        "securityProfileName": str,
        "securityProfileArn": str,
        "securityProfileDescription": str,
        "behaviors": List[ClientUpdateSecurityProfileResponsebehaviorsTypeDef],
        "alertTargets": Dict[
            str, ClientUpdateSecurityProfileResponsealertTargetsTypeDef
        ],
        "additionalMetricsToRetain": List[str],
        "version": int,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)


class ClientUpdateSecurityProfileResponseTypeDef(
    _ClientUpdateSecurityProfileResponseTypeDef
):
    """
    Type definition for `ClientUpdateSecurityProfile` `Response`

    - **securityProfileName** *(string) --*

      The name of the security profile that was updated.

    - **securityProfileArn** *(string) --*

      The ARN of the security profile that was updated.

    - **securityProfileDescription** *(string) --*

      The description of the security profile.

    - **behaviors** *(list) --*

      Specifies the behaviors that, when violated by a device (thing), cause an alert.

      - *(dict) --*

        A Device Defender security profile behavior.

        - **name** *(string) --*

          The name you have given to the behavior.

        - **metric** *(string) --*

          What is measured by the behavior.

        - **criteria** *(dict) --*

          The criteria that determine if a device is behaving normally in regard to the ``metric`` .

          - **comparisonOperator** *(string) --*

            The operator that relates the thing measured (``metric`` ) to the criteria (containing
            a ``value`` or ``statisticalThreshold`` ).

          - **value** *(dict) --*

            The value to be compared with the ``metric`` .

            - **count** *(integer) --*

              If the ``comparisonOperator`` calls for a numeric value, use this to specify that
              numeric value to be compared with the ``metric`` .

            - **cidrs** *(list) --*

              If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set
              to be compared with the ``metric`` .

              - *(string) --*

            - **ports** *(list) --*

              If the ``comparisonOperator`` calls for a set of ports, use this to specify that set
              to be compared with the ``metric`` .

              - *(integer) --*

          - **durationSeconds** *(integer) --*

            Use this to specify the time duration over which the behavior is evaluated, for those
            criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
            ``statisticalThreshhold`` metric comparison, measurements from all devices are
            accumulated over this time duration before being used to calculate percentiles, and
            later, measurements from an individual device are also accumulated over this time
            duration before being given a percentile rank.

          - **consecutiveDatapointsToAlarm** *(integer) --*

            If a device is in violation of the behavior for the specified number of consecutive
            datapoints, an alarm occurs. If not specified, the default is 1.

          - **consecutiveDatapointsToClear** *(integer) --*

            If an alarm has occurred and the offending device is no longer in violation of the
            behavior for the specified number of consecutive datapoints, the alarm is cleared. If
            not specified, the default is 1.

          - **statisticalThreshold** *(dict) --*

            A statistical ranking (percentile) which indicates a threshold value by which a
            behavior is determined to be in compliance or in violation of the behavior.

            - **statistic** *(string) --*

              The percentile which resolves to a threshold value by which compliance with a
              behavior is determined. Metrics are collected over the specified period
              (``durationSeconds`` ) from all reporting devices in your account and statistical
              ranks are calculated. Then, the measurements from a device are collected over the
              same period. If the accumulated measurements from the device fall above or below
              (``comparisonOperator`` ) the value associated with the percentile specified, then
              the device is considered to be in compliance with the behavior, otherwise a violation
              occurs.

    - **alertTargets** *(dict) --*

      Where the alerts are sent. (Alerts are always sent to the console.)

      - *(string) --*

        The type of alert target: one of "SNS".

        - *(dict) --*

          A structure containing the alert target ARN and the role ARN.

          - **alertTargetArn** *(string) --*

            The ARN of the notification target to which alerts are sent.

          - **roleArn** *(string) --*

            The ARN of the role that grants permission to send alerts to the notification target.

    - **additionalMetricsToRetain** *(list) --*

      A list of metrics whose data is retained (stored). By default, data is retained for any
      metric used in the security profile's ``behaviors`` , but it is also retained for any metric
      specified here.

      - *(string) --*

    - **version** *(integer) --*

      The updated version of the security profile.

    - **creationDate** *(datetime) --*

      The time the security profile was created.

    - **lastModifiedDate** *(datetime) --*

      The time the security profile was last modified.
    """


_ClientUpdateSecurityProfilealertTargetsTypeDef = TypedDict(
    "_ClientUpdateSecurityProfilealertTargetsTypeDef",
    {"alertTargetArn": str, "roleArn": str},
)


class ClientUpdateSecurityProfilealertTargetsTypeDef(
    _ClientUpdateSecurityProfilealertTargetsTypeDef
):
    """
    Type definition for `ClientUpdateSecurityProfile` `alertTargets`

    A structure containing the alert target ARN and the role ARN.

    - **alertTargetArn** *(string) --* **[REQUIRED]**

      The ARN of the notification target to which alerts are sent.

    - **roleArn** *(string) --* **[REQUIRED]**

      The ARN of the role that grants permission to send alerts to the notification target.
    """


_ClientUpdateSecurityProfilebehaviorscriteriastatisticalThresholdTypeDef = TypedDict(
    "_ClientUpdateSecurityProfilebehaviorscriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)


class ClientUpdateSecurityProfilebehaviorscriteriastatisticalThresholdTypeDef(
    _ClientUpdateSecurityProfilebehaviorscriteriastatisticalThresholdTypeDef
):
    """
    Type definition for `ClientUpdateSecurityProfilebehaviorscriteria` `statisticalThreshold`

    A statistical ranking (percentile) which indicates a threshold value by which a behavior is
    determined to be in compliance or in violation of the behavior.

    - **statistic** *(string) --*

      The percentile which resolves to a threshold value by which compliance with a behavior is
      determined. Metrics are collected over the specified period (``durationSeconds`` ) from
      all reporting devices in your account and statistical ranks are calculated. Then, the
      measurements from a device are collected over the same period. If the accumulated
      measurements from the device fall above or below (``comparisonOperator`` ) the value
      associated with the percentile specified, then the device is considered to be in
      compliance with the behavior, otherwise a violation occurs.
    """


_ClientUpdateSecurityProfilebehaviorscriteriavalueTypeDef = TypedDict(
    "_ClientUpdateSecurityProfilebehaviorscriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ClientUpdateSecurityProfilebehaviorscriteriavalueTypeDef(
    _ClientUpdateSecurityProfilebehaviorscriteriavalueTypeDef
):
    """
    Type definition for `ClientUpdateSecurityProfilebehaviorscriteria` `value`

    The value to be compared with the ``metric`` .

    - **count** *(integer) --*

      If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric
      value to be compared with the ``metric`` .

    - **cidrs** *(list) --*

      If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
      be compared with the ``metric`` .

      - *(string) --*

    - **ports** *(list) --*

      If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
      be compared with the ``metric`` .

      - *(integer) --*
    """


_ClientUpdateSecurityProfilebehaviorscriteriaTypeDef = TypedDict(
    "_ClientUpdateSecurityProfilebehaviorscriteriaTypeDef",
    {
        "comparisonOperator": str,
        "value": ClientUpdateSecurityProfilebehaviorscriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientUpdateSecurityProfilebehaviorscriteriastatisticalThresholdTypeDef,
    },
    total=False,
)


class ClientUpdateSecurityProfilebehaviorscriteriaTypeDef(
    _ClientUpdateSecurityProfilebehaviorscriteriaTypeDef
):
    """
    Type definition for `ClientUpdateSecurityProfilebehaviors` `criteria`

    The criteria that determine if a device is behaving normally in regard to the ``metric`` .

    - **comparisonOperator** *(string) --*

      The operator that relates the thing measured (``metric`` ) to the criteria (containing a
      ``value`` or ``statisticalThreshold`` ).

    - **value** *(dict) --*

      The value to be compared with the ``metric`` .

      - **count** *(integer) --*

        If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric
        value to be compared with the ``metric`` .

      - **cidrs** *(list) --*

        If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
        be compared with the ``metric`` .

        - *(string) --*

      - **ports** *(list) --*

        If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
        be compared with the ``metric`` .

        - *(integer) --*

    - **durationSeconds** *(integer) --*

      Use this to specify the time duration over which the behavior is evaluated, for those
      criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
      ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated
      over this time duration before being used to calculate percentiles, and later, measurements
      from an individual device are also accumulated over this time duration before being given a
      percentile rank.

    - **consecutiveDatapointsToAlarm** *(integer) --*

      If a device is in violation of the behavior for the specified number of consecutive
      datapoints, an alarm occurs. If not specified, the default is 1.

    - **consecutiveDatapointsToClear** *(integer) --*

      If an alarm has occurred and the offending device is no longer in violation of the behavior
      for the specified number of consecutive datapoints, the alarm is cleared. If not specified,
      the default is 1.

    - **statisticalThreshold** *(dict) --*

      A statistical ranking (percentile) which indicates a threshold value by which a behavior is
      determined to be in compliance or in violation of the behavior.

      - **statistic** *(string) --*

        The percentile which resolves to a threshold value by which compliance with a behavior is
        determined. Metrics are collected over the specified period (``durationSeconds`` ) from
        all reporting devices in your account and statistical ranks are calculated. Then, the
        measurements from a device are collected over the same period. If the accumulated
        measurements from the device fall above or below (``comparisonOperator`` ) the value
        associated with the percentile specified, then the device is considered to be in
        compliance with the behavior, otherwise a violation occurs.
    """


_RequiredClientUpdateSecurityProfilebehaviorsTypeDef = TypedDict(
    "_RequiredClientUpdateSecurityProfilebehaviorsTypeDef", {"name": str}
)
_OptionalClientUpdateSecurityProfilebehaviorsTypeDef = TypedDict(
    "_OptionalClientUpdateSecurityProfilebehaviorsTypeDef",
    {"metric": str, "criteria": ClientUpdateSecurityProfilebehaviorscriteriaTypeDef},
    total=False,
)


class ClientUpdateSecurityProfilebehaviorsTypeDef(
    _RequiredClientUpdateSecurityProfilebehaviorsTypeDef,
    _OptionalClientUpdateSecurityProfilebehaviorsTypeDef,
):
    """
    Type definition for `ClientUpdateSecurityProfile` `behaviors`

    A Device Defender security profile behavior.

    - **name** *(string) --* **[REQUIRED]**

      The name you have given to the behavior.

    - **metric** *(string) --*

      What is measured by the behavior.

    - **criteria** *(dict) --*

      The criteria that determine if a device is behaving normally in regard to the ``metric`` .

      - **comparisonOperator** *(string) --*

        The operator that relates the thing measured (``metric`` ) to the criteria (containing a
        ``value`` or ``statisticalThreshold`` ).

      - **value** *(dict) --*

        The value to be compared with the ``metric`` .

        - **count** *(integer) --*

          If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric
          value to be compared with the ``metric`` .

        - **cidrs** *(list) --*

          If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
          be compared with the ``metric`` .

          - *(string) --*

        - **ports** *(list) --*

          If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
          be compared with the ``metric`` .

          - *(integer) --*

      - **durationSeconds** *(integer) --*

        Use this to specify the time duration over which the behavior is evaluated, for those
        criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
        ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated
        over this time duration before being used to calculate percentiles, and later, measurements
        from an individual device are also accumulated over this time duration before being given a
        percentile rank.

      - **consecutiveDatapointsToAlarm** *(integer) --*

        If a device is in violation of the behavior for the specified number of consecutive
        datapoints, an alarm occurs. If not specified, the default is 1.

      - **consecutiveDatapointsToClear** *(integer) --*

        If an alarm has occurred and the offending device is no longer in violation of the behavior
        for the specified number of consecutive datapoints, the alarm is cleared. If not specified,
        the default is 1.

      - **statisticalThreshold** *(dict) --*

        A statistical ranking (percentile) which indicates a threshold value by which a behavior is
        determined to be in compliance or in violation of the behavior.

        - **statistic** *(string) --*

          The percentile which resolves to a threshold value by which compliance with a behavior is
          determined. Metrics are collected over the specified period (``durationSeconds`` ) from
          all reporting devices in your account and statistical ranks are calculated. Then, the
          measurements from a device are collected over the same period. If the accumulated
          measurements from the device fall above or below (``comparisonOperator`` ) the value
          associated with the percentile specified, then the device is considered to be in
          compliance with the behavior, otherwise a violation occurs.
    """


_ClientUpdateStreamResponseTypeDef = TypedDict(
    "_ClientUpdateStreamResponseTypeDef",
    {"streamId": str, "streamArn": str, "description": str, "streamVersion": int},
    total=False,
)


class ClientUpdateStreamResponseTypeDef(_ClientUpdateStreamResponseTypeDef):
    """
    Type definition for `ClientUpdateStream` `Response`

    - **streamId** *(string) --*

      The stream ID.

    - **streamArn** *(string) --*

      The stream ARN.

    - **description** *(string) --*

      A description of the stream.

    - **streamVersion** *(integer) --*

      The stream version.
    """


_ClientUpdateStreamfiless3LocationTypeDef = TypedDict(
    "_ClientUpdateStreamfiless3LocationTypeDef",
    {"bucket": str, "key": str, "version": str},
    total=False,
)


class ClientUpdateStreamfiless3LocationTypeDef(
    _ClientUpdateStreamfiless3LocationTypeDef
):
    """
    Type definition for `ClientUpdateStreamfiles` `s3Location`

    The location of the file in S3.

    - **bucket** *(string) --*

      The S3 bucket.

    - **key** *(string) --*

      The S3 key.

    - **version** *(string) --*

      The S3 bucket version.
    """


_ClientUpdateStreamfilesTypeDef = TypedDict(
    "_ClientUpdateStreamfilesTypeDef",
    {"fileId": int, "s3Location": ClientUpdateStreamfiless3LocationTypeDef},
    total=False,
)


class ClientUpdateStreamfilesTypeDef(_ClientUpdateStreamfilesTypeDef):
    """
    Type definition for `ClientUpdateStream` `files`

    Represents a file to stream.

    - **fileId** *(integer) --*

      The file ID.

    - **s3Location** *(dict) --*

      The location of the file in S3.

      - **bucket** *(string) --*

        The S3 bucket.

      - **key** *(string) --*

        The S3 key.

      - **version** *(string) --*

        The S3 bucket version.
    """


_ClientUpdateThingGroupResponseTypeDef = TypedDict(
    "_ClientUpdateThingGroupResponseTypeDef", {"version": int}, total=False
)


class ClientUpdateThingGroupResponseTypeDef(_ClientUpdateThingGroupResponseTypeDef):
    """
    Type definition for `ClientUpdateThingGroup` `Response`

    - **version** *(integer) --*

      The version of the updated thing group.
    """


_ClientUpdateThingGroupthingGroupPropertiesattributePayloadTypeDef = TypedDict(
    "_ClientUpdateThingGroupthingGroupPropertiesattributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)


class ClientUpdateThingGroupthingGroupPropertiesattributePayloadTypeDef(
    _ClientUpdateThingGroupthingGroupPropertiesattributePayloadTypeDef
):
    """
    Type definition for `ClientUpdateThingGroupthingGroupProperties` `attributePayload`

    The thing group attributes in JSON format.

    - **attributes** *(dict) --*

      A JSON string containing up to three key-value pair in JSON format. For example:

       ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``

      - *(string) --*

        - *(string) --*

    - **merge** *(boolean) --*

      Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with
      the attributes stored in the registry, instead of overwriting them.

      To remove an attribute, call ``UpdateThing`` with an empty attribute value.

      .. note::

        The ``merge`` attribute is only valid when calling ``UpdateThing`` or ``UpdateThingGroup`` .
    """


_ClientUpdateThingGroupthingGroupPropertiesTypeDef = TypedDict(
    "_ClientUpdateThingGroupthingGroupPropertiesTypeDef",
    {
        "thingGroupDescription": str,
        "attributePayload": ClientUpdateThingGroupthingGroupPropertiesattributePayloadTypeDef,
    },
    total=False,
)


class ClientUpdateThingGroupthingGroupPropertiesTypeDef(
    _ClientUpdateThingGroupthingGroupPropertiesTypeDef
):
    """
    Type definition for `ClientUpdateThingGroup` `thingGroupProperties`

    The thing group properties.

    - **thingGroupDescription** *(string) --*

      The thing group description.

    - **attributePayload** *(dict) --*

      The thing group attributes in JSON format.

      - **attributes** *(dict) --*

        A JSON string containing up to three key-value pair in JSON format. For example:

         ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``

        - *(string) --*

          - *(string) --*

      - **merge** *(boolean) --*

        Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with
        the attributes stored in the registry, instead of overwriting them.

        To remove an attribute, call ``UpdateThing`` with an empty attribute value.

        .. note::

          The ``merge`` attribute is only valid when calling ``UpdateThing`` or ``UpdateThingGroup`` .
    """


_ClientUpdateThingattributePayloadTypeDef = TypedDict(
    "_ClientUpdateThingattributePayloadTypeDef",
    {"attributes": Dict[str, str], "merge": bool},
    total=False,
)


class ClientUpdateThingattributePayloadTypeDef(
    _ClientUpdateThingattributePayloadTypeDef
):
    """
    Type definition for `ClientUpdateThing` `attributePayload`

    A list of thing attributes, a JSON string containing name-value pairs. For example:

     ``{\\"attributes\\":{\\"name1\\":\\"value2\\"}}``

    This data is used to add new attributes or update existing attributes.

    - **attributes** *(dict) --*

      A JSON string containing up to three key-value pair in JSON format. For example:

       ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``

      - *(string) --*

        - *(string) --*

    - **merge** *(boolean) --*

      Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with
      the attributes stored in the registry, instead of overwriting them.

      To remove an attribute, call ``UpdateThing`` with an empty attribute value.

      .. note::

        The ``merge`` attribute is only valid when calling ``UpdateThing`` or ``UpdateThingGroup`` .
    """


_ClientValidateSecurityProfileBehaviorsResponsevalidationErrorsTypeDef = TypedDict(
    "_ClientValidateSecurityProfileBehaviorsResponsevalidationErrorsTypeDef",
    {"errorMessage": str},
    total=False,
)


class ClientValidateSecurityProfileBehaviorsResponsevalidationErrorsTypeDef(
    _ClientValidateSecurityProfileBehaviorsResponsevalidationErrorsTypeDef
):
    """
    Type definition for `ClientValidateSecurityProfileBehaviorsResponse` `validationErrors`

    Information about an error found in a behavior specification.

    - **errorMessage** *(string) --*

      The description of an error found in the behaviors.
    """


_ClientValidateSecurityProfileBehaviorsResponseTypeDef = TypedDict(
    "_ClientValidateSecurityProfileBehaviorsResponseTypeDef",
    {
        "valid": bool,
        "validationErrors": List[
            ClientValidateSecurityProfileBehaviorsResponsevalidationErrorsTypeDef
        ],
    },
    total=False,
)


class ClientValidateSecurityProfileBehaviorsResponseTypeDef(
    _ClientValidateSecurityProfileBehaviorsResponseTypeDef
):
    """
    Type definition for `ClientValidateSecurityProfileBehaviors` `Response`

    - **valid** *(boolean) --*

      True if the behaviors were valid.

    - **validationErrors** *(list) --*

      The list of any errors found in the behaviors.

      - *(dict) --*

        Information about an error found in a behavior specification.

        - **errorMessage** *(string) --*

          The description of an error found in the behaviors.
    """


_ClientValidateSecurityProfileBehaviorsbehaviorscriteriastatisticalThresholdTypeDef = TypedDict(
    "_ClientValidateSecurityProfileBehaviorsbehaviorscriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)


class ClientValidateSecurityProfileBehaviorsbehaviorscriteriastatisticalThresholdTypeDef(
    _ClientValidateSecurityProfileBehaviorsbehaviorscriteriastatisticalThresholdTypeDef
):
    """
    Type definition for `ClientValidateSecurityProfileBehaviorsbehaviorscriteria` `statisticalThreshold`

    A statistical ranking (percentile) which indicates a threshold value by which a behavior is
    determined to be in compliance or in violation of the behavior.

    - **statistic** *(string) --*

      The percentile which resolves to a threshold value by which compliance with a behavior is
      determined. Metrics are collected over the specified period (``durationSeconds`` ) from
      all reporting devices in your account and statistical ranks are calculated. Then, the
      measurements from a device are collected over the same period. If the accumulated
      measurements from the device fall above or below (``comparisonOperator`` ) the value
      associated with the percentile specified, then the device is considered to be in
      compliance with the behavior, otherwise a violation occurs.
    """


_ClientValidateSecurityProfileBehaviorsbehaviorscriteriavalueTypeDef = TypedDict(
    "_ClientValidateSecurityProfileBehaviorsbehaviorscriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ClientValidateSecurityProfileBehaviorsbehaviorscriteriavalueTypeDef(
    _ClientValidateSecurityProfileBehaviorsbehaviorscriteriavalueTypeDef
):
    """
    Type definition for `ClientValidateSecurityProfileBehaviorsbehaviorscriteria` `value`

    The value to be compared with the ``metric`` .

    - **count** *(integer) --*

      If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric
      value to be compared with the ``metric`` .

    - **cidrs** *(list) --*

      If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
      be compared with the ``metric`` .

      - *(string) --*

    - **ports** *(list) --*

      If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
      be compared with the ``metric`` .

      - *(integer) --*
    """


_ClientValidateSecurityProfileBehaviorsbehaviorscriteriaTypeDef = TypedDict(
    "_ClientValidateSecurityProfileBehaviorsbehaviorscriteriaTypeDef",
    {
        "comparisonOperator": str,
        "value": ClientValidateSecurityProfileBehaviorsbehaviorscriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ClientValidateSecurityProfileBehaviorsbehaviorscriteriastatisticalThresholdTypeDef,
    },
    total=False,
)


class ClientValidateSecurityProfileBehaviorsbehaviorscriteriaTypeDef(
    _ClientValidateSecurityProfileBehaviorsbehaviorscriteriaTypeDef
):
    """
    Type definition for `ClientValidateSecurityProfileBehaviorsbehaviors` `criteria`

    The criteria that determine if a device is behaving normally in regard to the ``metric`` .

    - **comparisonOperator** *(string) --*

      The operator that relates the thing measured (``metric`` ) to the criteria (containing a
      ``value`` or ``statisticalThreshold`` ).

    - **value** *(dict) --*

      The value to be compared with the ``metric`` .

      - **count** *(integer) --*

        If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric
        value to be compared with the ``metric`` .

      - **cidrs** *(list) --*

        If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
        be compared with the ``metric`` .

        - *(string) --*

      - **ports** *(list) --*

        If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
        be compared with the ``metric`` .

        - *(integer) --*

    - **durationSeconds** *(integer) --*

      Use this to specify the time duration over which the behavior is evaluated, for those
      criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
      ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated
      over this time duration before being used to calculate percentiles, and later, measurements
      from an individual device are also accumulated over this time duration before being given a
      percentile rank.

    - **consecutiveDatapointsToAlarm** *(integer) --*

      If a device is in violation of the behavior for the specified number of consecutive
      datapoints, an alarm occurs. If not specified, the default is 1.

    - **consecutiveDatapointsToClear** *(integer) --*

      If an alarm has occurred and the offending device is no longer in violation of the behavior
      for the specified number of consecutive datapoints, the alarm is cleared. If not specified,
      the default is 1.

    - **statisticalThreshold** *(dict) --*

      A statistical ranking (percentile) which indicates a threshold value by which a behavior is
      determined to be in compliance or in violation of the behavior.

      - **statistic** *(string) --*

        The percentile which resolves to a threshold value by which compliance with a behavior is
        determined. Metrics are collected over the specified period (``durationSeconds`` ) from
        all reporting devices in your account and statistical ranks are calculated. Then, the
        measurements from a device are collected over the same period. If the accumulated
        measurements from the device fall above or below (``comparisonOperator`` ) the value
        associated with the percentile specified, then the device is considered to be in
        compliance with the behavior, otherwise a violation occurs.
    """


_RequiredClientValidateSecurityProfileBehaviorsbehaviorsTypeDef = TypedDict(
    "_RequiredClientValidateSecurityProfileBehaviorsbehaviorsTypeDef", {"name": str}
)
_OptionalClientValidateSecurityProfileBehaviorsbehaviorsTypeDef = TypedDict(
    "_OptionalClientValidateSecurityProfileBehaviorsbehaviorsTypeDef",
    {
        "metric": str,
        "criteria": ClientValidateSecurityProfileBehaviorsbehaviorscriteriaTypeDef,
    },
    total=False,
)


class ClientValidateSecurityProfileBehaviorsbehaviorsTypeDef(
    _RequiredClientValidateSecurityProfileBehaviorsbehaviorsTypeDef,
    _OptionalClientValidateSecurityProfileBehaviorsbehaviorsTypeDef,
):
    """
    Type definition for `ClientValidateSecurityProfileBehaviors` `behaviors`

    A Device Defender security profile behavior.

    - **name** *(string) --* **[REQUIRED]**

      The name you have given to the behavior.

    - **metric** *(string) --*

      What is measured by the behavior.

    - **criteria** *(dict) --*

      The criteria that determine if a device is behaving normally in regard to the ``metric`` .

      - **comparisonOperator** *(string) --*

        The operator that relates the thing measured (``metric`` ) to the criteria (containing a
        ``value`` or ``statisticalThreshold`` ).

      - **value** *(dict) --*

        The value to be compared with the ``metric`` .

        - **count** *(integer) --*

          If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric
          value to be compared with the ``metric`` .

        - **cidrs** *(list) --*

          If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
          be compared with the ``metric`` .

          - *(string) --*

        - **ports** *(list) --*

          If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
          be compared with the ``metric`` .

          - *(integer) --*

      - **durationSeconds** *(integer) --*

        Use this to specify the time duration over which the behavior is evaluated, for those
        criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
        ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated
        over this time duration before being used to calculate percentiles, and later, measurements
        from an individual device are also accumulated over this time duration before being given a
        percentile rank.

      - **consecutiveDatapointsToAlarm** *(integer) --*

        If a device is in violation of the behavior for the specified number of consecutive
        datapoints, an alarm occurs. If not specified, the default is 1.

      - **consecutiveDatapointsToClear** *(integer) --*

        If an alarm has occurred and the offending device is no longer in violation of the behavior
        for the specified number of consecutive datapoints, the alarm is cleared. If not specified,
        the default is 1.

      - **statisticalThreshold** *(dict) --*

        A statistical ranking (percentile) which indicates a threshold value by which a behavior is
        determined to be in compliance or in violation of the behavior.

        - **statistic** *(string) --*

          The percentile which resolves to a threshold value by which compliance with a behavior is
          determined. Metrics are collected over the specified period (``durationSeconds`` ) from
          all reporting devices in your account and statistical ranks are calculated. Then, the
          measurements from a device are collected over the same period. If the accumulated
          measurements from the device fall above or below (``comparisonOperator`` ) the value
          associated with the percentile specified, then the device is considered to be in
          compliance with the behavior, otherwise a violation occurs.
    """


_ListActiveViolationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListActiveViolationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListActiveViolationsPaginatePaginationConfigTypeDef(
    _ListActiveViolationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListActiveViolationsPaginate` `PaginationConfig`

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


_ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef = TypedDict(
    "_ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)


class ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef(
    _ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef
):
    """
    Type definition for `ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteria` `statisticalThreshold`

    A statistical ranking (percentile) which indicates a threshold value by which a
    behavior is determined to be in compliance or in violation of the behavior.

    - **statistic** *(string) --*

      The percentile which resolves to a threshold value by which compliance with a
      behavior is determined. Metrics are collected over the specified period
      (``durationSeconds`` ) from all reporting devices in your account and statistical
      ranks are calculated. Then, the measurements from a device are collected over the
      same period. If the accumulated measurements from the device fall above or below
      (``comparisonOperator`` ) the value associated with the percentile specified, then
      the device is considered to be in compliance with the behavior, otherwise a
      violation occurs.
    """


_ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriavalueTypeDef = TypedDict(
    "_ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriavalueTypeDef(
    _ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriavalueTypeDef
):
    """
    Type definition for `ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteria` `value`

    The value to be compared with the ``metric`` .

    - **count** *(integer) --*

      If the ``comparisonOperator`` calls for a numeric value, use this to specify that
      numeric value to be compared with the ``metric`` .

    - **cidrs** *(list) --*

      If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
      set to be compared with the ``metric`` .

      - *(string) --*

    - **ports** *(list) --*

      If the ``comparisonOperator`` calls for a set of ports, use this to specify that
      set to be compared with the ``metric`` .

      - *(integer) --*
    """


_ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriaTypeDef = TypedDict(
    "_ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriaTypeDef",
    {
        "comparisonOperator": str,
        "value": ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriastatisticalThresholdTypeDef,
    },
    total=False,
)


class ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriaTypeDef(
    _ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriaTypeDef
):
    """
    Type definition for `ListActiveViolationsPaginateResponseactiveViolationsbehavior` `criteria`

    The criteria that determine if a device is behaving normally in regard to the
    ``metric`` .

    - **comparisonOperator** *(string) --*

      The operator that relates the thing measured (``metric`` ) to the criteria
      (containing a ``value`` or ``statisticalThreshold`` ).

    - **value** *(dict) --*

      The value to be compared with the ``metric`` .

      - **count** *(integer) --*

        If the ``comparisonOperator`` calls for a numeric value, use this to specify that
        numeric value to be compared with the ``metric`` .

      - **cidrs** *(list) --*

        If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
        set to be compared with the ``metric`` .

        - *(string) --*

      - **ports** *(list) --*

        If the ``comparisonOperator`` calls for a set of ports, use this to specify that
        set to be compared with the ``metric`` .

        - *(integer) --*

    - **durationSeconds** *(integer) --*

      Use this to specify the time duration over which the behavior is evaluated, for those
      criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
      ``statisticalThreshhold`` metric comparison, measurements from all devices are
      accumulated over this time duration before being used to calculate percentiles, and
      later, measurements from an individual device are also accumulated over this time
      duration before being given a percentile rank.

    - **consecutiveDatapointsToAlarm** *(integer) --*

      If a device is in violation of the behavior for the specified number of consecutive
      datapoints, an alarm occurs. If not specified, the default is 1.

    - **consecutiveDatapointsToClear** *(integer) --*

      If an alarm has occurred and the offending device is no longer in violation of the
      behavior for the specified number of consecutive datapoints, the alarm is cleared. If
      not specified, the default is 1.

    - **statisticalThreshold** *(dict) --*

      A statistical ranking (percentile) which indicates a threshold value by which a
      behavior is determined to be in compliance or in violation of the behavior.

      - **statistic** *(string) --*

        The percentile which resolves to a threshold value by which compliance with a
        behavior is determined. Metrics are collected over the specified period
        (``durationSeconds`` ) from all reporting devices in your account and statistical
        ranks are calculated. Then, the measurements from a device are collected over the
        same period. If the accumulated measurements from the device fall above or below
        (``comparisonOperator`` ) the value associated with the percentile specified, then
        the device is considered to be in compliance with the behavior, otherwise a
        violation occurs.
    """


_ListActiveViolationsPaginateResponseactiveViolationsbehaviorTypeDef = TypedDict(
    "_ListActiveViolationsPaginateResponseactiveViolationsbehaviorTypeDef",
    {
        "name": str,
        "metric": str,
        "criteria": ListActiveViolationsPaginateResponseactiveViolationsbehaviorcriteriaTypeDef,
    },
    total=False,
)


class ListActiveViolationsPaginateResponseactiveViolationsbehaviorTypeDef(
    _ListActiveViolationsPaginateResponseactiveViolationsbehaviorTypeDef
):
    """
    Type definition for `ListActiveViolationsPaginateResponseactiveViolations` `behavior`

    The behavior which is being violated.

    - **name** *(string) --*

      The name you have given to the behavior.

    - **metric** *(string) --*

      What is measured by the behavior.

    - **criteria** *(dict) --*

      The criteria that determine if a device is behaving normally in regard to the
      ``metric`` .

      - **comparisonOperator** *(string) --*

        The operator that relates the thing measured (``metric`` ) to the criteria
        (containing a ``value`` or ``statisticalThreshold`` ).

      - **value** *(dict) --*

        The value to be compared with the ``metric`` .

        - **count** *(integer) --*

          If the ``comparisonOperator`` calls for a numeric value, use this to specify that
          numeric value to be compared with the ``metric`` .

        - **cidrs** *(list) --*

          If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
          set to be compared with the ``metric`` .

          - *(string) --*

        - **ports** *(list) --*

          If the ``comparisonOperator`` calls for a set of ports, use this to specify that
          set to be compared with the ``metric`` .

          - *(integer) --*

      - **durationSeconds** *(integer) --*

        Use this to specify the time duration over which the behavior is evaluated, for those
        criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
        ``statisticalThreshhold`` metric comparison, measurements from all devices are
        accumulated over this time duration before being used to calculate percentiles, and
        later, measurements from an individual device are also accumulated over this time
        duration before being given a percentile rank.

      - **consecutiveDatapointsToAlarm** *(integer) --*

        If a device is in violation of the behavior for the specified number of consecutive
        datapoints, an alarm occurs. If not specified, the default is 1.

      - **consecutiveDatapointsToClear** *(integer) --*

        If an alarm has occurred and the offending device is no longer in violation of the
        behavior for the specified number of consecutive datapoints, the alarm is cleared. If
        not specified, the default is 1.

      - **statisticalThreshold** *(dict) --*

        A statistical ranking (percentile) which indicates a threshold value by which a
        behavior is determined to be in compliance or in violation of the behavior.

        - **statistic** *(string) --*

          The percentile which resolves to a threshold value by which compliance with a
          behavior is determined. Metrics are collected over the specified period
          (``durationSeconds`` ) from all reporting devices in your account and statistical
          ranks are calculated. Then, the measurements from a device are collected over the
          same period. If the accumulated measurements from the device fall above or below
          (``comparisonOperator`` ) the value associated with the percentile specified, then
          the device is considered to be in compliance with the behavior, otherwise a
          violation occurs.
    """


_ListActiveViolationsPaginateResponseactiveViolationslastViolationValueTypeDef = TypedDict(
    "_ListActiveViolationsPaginateResponseactiveViolationslastViolationValueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ListActiveViolationsPaginateResponseactiveViolationslastViolationValueTypeDef(
    _ListActiveViolationsPaginateResponseactiveViolationslastViolationValueTypeDef
):
    """
    Type definition for `ListActiveViolationsPaginateResponseactiveViolations` `lastViolationValue`

    The value of the metric (the measurement) which caused the most recent violation.

    - **count** *(integer) --*

      If the ``comparisonOperator`` calls for a numeric value, use this to specify that
      numeric value to be compared with the ``metric`` .

    - **cidrs** *(list) --*

      If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
      be compared with the ``metric`` .

      - *(string) --*

    - **ports** *(list) --*

      If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
      be compared with the ``metric`` .

      - *(integer) --*
    """


_ListActiveViolationsPaginateResponseactiveViolationsTypeDef = TypedDict(
    "_ListActiveViolationsPaginateResponseactiveViolationsTypeDef",
    {
        "violationId": str,
        "thingName": str,
        "securityProfileName": str,
        "behavior": ListActiveViolationsPaginateResponseactiveViolationsbehaviorTypeDef,
        "lastViolationValue": ListActiveViolationsPaginateResponseactiveViolationslastViolationValueTypeDef,
        "lastViolationTime": datetime,
        "violationStartTime": datetime,
    },
    total=False,
)


class ListActiveViolationsPaginateResponseactiveViolationsTypeDef(
    _ListActiveViolationsPaginateResponseactiveViolationsTypeDef
):
    """
    Type definition for `ListActiveViolationsPaginateResponse` `activeViolations`

    Information about an active Device Defender security profile behavior violation.

    - **violationId** *(string) --*

      The ID of the active violation.

    - **thingName** *(string) --*

      The name of the thing responsible for the active violation.

    - **securityProfileName** *(string) --*

      The security profile whose behavior is in violation.

    - **behavior** *(dict) --*

      The behavior which is being violated.

      - **name** *(string) --*

        The name you have given to the behavior.

      - **metric** *(string) --*

        What is measured by the behavior.

      - **criteria** *(dict) --*

        The criteria that determine if a device is behaving normally in regard to the
        ``metric`` .

        - **comparisonOperator** *(string) --*

          The operator that relates the thing measured (``metric`` ) to the criteria
          (containing a ``value`` or ``statisticalThreshold`` ).

        - **value** *(dict) --*

          The value to be compared with the ``metric`` .

          - **count** *(integer) --*

            If the ``comparisonOperator`` calls for a numeric value, use this to specify that
            numeric value to be compared with the ``metric`` .

          - **cidrs** *(list) --*

            If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
            set to be compared with the ``metric`` .

            - *(string) --*

          - **ports** *(list) --*

            If the ``comparisonOperator`` calls for a set of ports, use this to specify that
            set to be compared with the ``metric`` .

            - *(integer) --*

        - **durationSeconds** *(integer) --*

          Use this to specify the time duration over which the behavior is evaluated, for those
          criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
          ``statisticalThreshhold`` metric comparison, measurements from all devices are
          accumulated over this time duration before being used to calculate percentiles, and
          later, measurements from an individual device are also accumulated over this time
          duration before being given a percentile rank.

        - **consecutiveDatapointsToAlarm** *(integer) --*

          If a device is in violation of the behavior for the specified number of consecutive
          datapoints, an alarm occurs. If not specified, the default is 1.

        - **consecutiveDatapointsToClear** *(integer) --*

          If an alarm has occurred and the offending device is no longer in violation of the
          behavior for the specified number of consecutive datapoints, the alarm is cleared. If
          not specified, the default is 1.

        - **statisticalThreshold** *(dict) --*

          A statistical ranking (percentile) which indicates a threshold value by which a
          behavior is determined to be in compliance or in violation of the behavior.

          - **statistic** *(string) --*

            The percentile which resolves to a threshold value by which compliance with a
            behavior is determined. Metrics are collected over the specified period
            (``durationSeconds`` ) from all reporting devices in your account and statistical
            ranks are calculated. Then, the measurements from a device are collected over the
            same period. If the accumulated measurements from the device fall above or below
            (``comparisonOperator`` ) the value associated with the percentile specified, then
            the device is considered to be in compliance with the behavior, otherwise a
            violation occurs.

    - **lastViolationValue** *(dict) --*

      The value of the metric (the measurement) which caused the most recent violation.

      - **count** *(integer) --*

        If the ``comparisonOperator`` calls for a numeric value, use this to specify that
        numeric value to be compared with the ``metric`` .

      - **cidrs** *(list) --*

        If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
        be compared with the ``metric`` .

        - *(string) --*

      - **ports** *(list) --*

        If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
        be compared with the ``metric`` .

        - *(integer) --*

    - **lastViolationTime** *(datetime) --*

      The time the most recent violation occurred.

    - **violationStartTime** *(datetime) --*

      The time the violation started.
    """


_ListActiveViolationsPaginateResponseTypeDef = TypedDict(
    "_ListActiveViolationsPaginateResponseTypeDef",
    {
        "activeViolations": List[
            ListActiveViolationsPaginateResponseactiveViolationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListActiveViolationsPaginateResponseTypeDef(
    _ListActiveViolationsPaginateResponseTypeDef
):
    """
    Type definition for `ListActiveViolationsPaginate` `Response`

    - **activeViolations** *(list) --*

      The list of active violations.

      - *(dict) --*

        Information about an active Device Defender security profile behavior violation.

        - **violationId** *(string) --*

          The ID of the active violation.

        - **thingName** *(string) --*

          The name of the thing responsible for the active violation.

        - **securityProfileName** *(string) --*

          The security profile whose behavior is in violation.

        - **behavior** *(dict) --*

          The behavior which is being violated.

          - **name** *(string) --*

            The name you have given to the behavior.

          - **metric** *(string) --*

            What is measured by the behavior.

          - **criteria** *(dict) --*

            The criteria that determine if a device is behaving normally in regard to the
            ``metric`` .

            - **comparisonOperator** *(string) --*

              The operator that relates the thing measured (``metric`` ) to the criteria
              (containing a ``value`` or ``statisticalThreshold`` ).

            - **value** *(dict) --*

              The value to be compared with the ``metric`` .

              - **count** *(integer) --*

                If the ``comparisonOperator`` calls for a numeric value, use this to specify that
                numeric value to be compared with the ``metric`` .

              - **cidrs** *(list) --*

                If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
                set to be compared with the ``metric`` .

                - *(string) --*

              - **ports** *(list) --*

                If the ``comparisonOperator`` calls for a set of ports, use this to specify that
                set to be compared with the ``metric`` .

                - *(integer) --*

            - **durationSeconds** *(integer) --*

              Use this to specify the time duration over which the behavior is evaluated, for those
              criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
              ``statisticalThreshhold`` metric comparison, measurements from all devices are
              accumulated over this time duration before being used to calculate percentiles, and
              later, measurements from an individual device are also accumulated over this time
              duration before being given a percentile rank.

            - **consecutiveDatapointsToAlarm** *(integer) --*

              If a device is in violation of the behavior for the specified number of consecutive
              datapoints, an alarm occurs. If not specified, the default is 1.

            - **consecutiveDatapointsToClear** *(integer) --*

              If an alarm has occurred and the offending device is no longer in violation of the
              behavior for the specified number of consecutive datapoints, the alarm is cleared. If
              not specified, the default is 1.

            - **statisticalThreshold** *(dict) --*

              A statistical ranking (percentile) which indicates a threshold value by which a
              behavior is determined to be in compliance or in violation of the behavior.

              - **statistic** *(string) --*

                The percentile which resolves to a threshold value by which compliance with a
                behavior is determined. Metrics are collected over the specified period
                (``durationSeconds`` ) from all reporting devices in your account and statistical
                ranks are calculated. Then, the measurements from a device are collected over the
                same period. If the accumulated measurements from the device fall above or below
                (``comparisonOperator`` ) the value associated with the percentile specified, then
                the device is considered to be in compliance with the behavior, otherwise a
                violation occurs.

        - **lastViolationValue** *(dict) --*

          The value of the metric (the measurement) which caused the most recent violation.

          - **count** *(integer) --*

            If the ``comparisonOperator`` calls for a numeric value, use this to specify that
            numeric value to be compared with the ``metric`` .

          - **cidrs** *(list) --*

            If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
            be compared with the ``metric`` .

            - *(string) --*

          - **ports** *(list) --*

            If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
            be compared with the ``metric`` .

            - *(integer) --*

        - **lastViolationTime** *(datetime) --*

          The time the most recent violation occurred.

        - **violationStartTime** *(datetime) --*

          The time the violation started.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListAttachedPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAttachedPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAttachedPoliciesPaginatePaginationConfigTypeDef(
    _ListAttachedPoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAttachedPoliciesPaginate` `PaginationConfig`

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


_ListAttachedPoliciesPaginateResponsepoliciesTypeDef = TypedDict(
    "_ListAttachedPoliciesPaginateResponsepoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)


class ListAttachedPoliciesPaginateResponsepoliciesTypeDef(
    _ListAttachedPoliciesPaginateResponsepoliciesTypeDef
):
    """
    Type definition for `ListAttachedPoliciesPaginateResponse` `policies`

    Describes an AWS IoT policy.

    - **policyName** *(string) --*

      The policy name.

    - **policyArn** *(string) --*

      The policy ARN.
    """


_ListAttachedPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListAttachedPoliciesPaginateResponseTypeDef",
    {
        "policies": List[ListAttachedPoliciesPaginateResponsepoliciesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListAttachedPoliciesPaginateResponseTypeDef(
    _ListAttachedPoliciesPaginateResponseTypeDef
):
    """
    Type definition for `ListAttachedPoliciesPaginate` `Response`

    - **policies** *(list) --*

      The policies.

      - *(dict) --*

        Describes an AWS IoT policy.

        - **policyName** *(string) --*

          The policy name.

        - **policyArn** *(string) --*

          The policy ARN.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListAuditFindingsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAuditFindingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAuditFindingsPaginatePaginationConfigTypeDef(
    _ListAuditFindingsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAuditFindingsPaginate` `PaginationConfig`

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


_ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "_ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)


class ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef(
    _ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef
):
    """
    Type definition for `ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifier` `policyVersionIdentifier`

    The version of the policy associated with the resource.

    - **policyName** *(string) --*

      The name of the policy.

    - **policyVersionId** *(string) --*

      The ID of the version of the policy associated with the resource.
    """


_ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierTypeDef = TypedDict(
    "_ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
    },
    total=False,
)


class ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierTypeDef(
    _ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierTypeDef
):
    """
    Type definition for `ListAuditFindingsPaginateResponsefindingsnonCompliantResource` `resourceIdentifier`

    Information that identifies the noncompliant resource.

    - **deviceCertificateId** *(string) --*

      The ID of the certificate attached to the resource.

    - **caCertificateId** *(string) --*

      The ID of the CA certificate used to authorize the certificate.

    - **cognitoIdentityPoolId** *(string) --*

      The ID of the Amazon Cognito identity pool.

    - **clientId** *(string) --*

      The client ID.

    - **policyVersionIdentifier** *(dict) --*

      The version of the policy associated with the resource.

      - **policyName** *(string) --*

        The name of the policy.

      - **policyVersionId** *(string) --*

        The ID of the version of the policy associated with the resource.

    - **account** *(string) --*

      The account with which the resource is associated.
    """


_ListAuditFindingsPaginateResponsefindingsnonCompliantResourceTypeDef = TypedDict(
    "_ListAuditFindingsPaginateResponsefindingsnonCompliantResourceTypeDef",
    {
        "resourceType": str,
        "resourceIdentifier": ListAuditFindingsPaginateResponsefindingsnonCompliantResourceresourceIdentifierTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)


class ListAuditFindingsPaginateResponsefindingsnonCompliantResourceTypeDef(
    _ListAuditFindingsPaginateResponsefindingsnonCompliantResourceTypeDef
):
    """
    Type definition for `ListAuditFindingsPaginateResponsefindings` `nonCompliantResource`

    The resource that was found to be noncompliant with the audit check.

    - **resourceType** *(string) --*

      The type of the noncompliant resource.

    - **resourceIdentifier** *(dict) --*

      Information that identifies the noncompliant resource.

      - **deviceCertificateId** *(string) --*

        The ID of the certificate attached to the resource.

      - **caCertificateId** *(string) --*

        The ID of the CA certificate used to authorize the certificate.

      - **cognitoIdentityPoolId** *(string) --*

        The ID of the Amazon Cognito identity pool.

      - **clientId** *(string) --*

        The client ID.

      - **policyVersionIdentifier** *(dict) --*

        The version of the policy associated with the resource.

        - **policyName** *(string) --*

          The name of the policy.

        - **policyVersionId** *(string) --*

          The ID of the version of the policy associated with the resource.

      - **account** *(string) --*

        The account with which the resource is associated.

    - **additionalInfo** *(dict) --*

      Other information about the noncompliant resource.

      - *(string) --*

        - *(string) --*
    """


_ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "_ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)


class ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef(
    _ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef
):
    """
    Type definition for `ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifier` `policyVersionIdentifier`

    The version of the policy associated with the resource.

    - **policyName** *(string) --*

      The name of the policy.

    - **policyVersionId** *(string) --*

      The ID of the version of the policy associated with the resource.
    """


_ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierTypeDef = TypedDict(
    "_ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
    },
    total=False,
)


class ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierTypeDef(
    _ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierTypeDef
):
    """
    Type definition for `ListAuditFindingsPaginateResponsefindingsrelatedResources` `resourceIdentifier`

    Information that identifies the resource.

    - **deviceCertificateId** *(string) --*

      The ID of the certificate attached to the resource.

    - **caCertificateId** *(string) --*

      The ID of the CA certificate used to authorize the certificate.

    - **cognitoIdentityPoolId** *(string) --*

      The ID of the Amazon Cognito identity pool.

    - **clientId** *(string) --*

      The client ID.

    - **policyVersionIdentifier** *(dict) --*

      The version of the policy associated with the resource.

      - **policyName** *(string) --*

        The name of the policy.

      - **policyVersionId** *(string) --*

        The ID of the version of the policy associated with the resource.

    - **account** *(string) --*

      The account with which the resource is associated.
    """


_ListAuditFindingsPaginateResponsefindingsrelatedResourcesTypeDef = TypedDict(
    "_ListAuditFindingsPaginateResponsefindingsrelatedResourcesTypeDef",
    {
        "resourceType": str,
        "resourceIdentifier": ListAuditFindingsPaginateResponsefindingsrelatedResourcesresourceIdentifierTypeDef,
        "additionalInfo": Dict[str, str],
    },
    total=False,
)


class ListAuditFindingsPaginateResponsefindingsrelatedResourcesTypeDef(
    _ListAuditFindingsPaginateResponsefindingsrelatedResourcesTypeDef
):
    """
    Type definition for `ListAuditFindingsPaginateResponsefindings` `relatedResources`

    Information about a related resource.

    - **resourceType** *(string) --*

      The type of resource.

    - **resourceIdentifier** *(dict) --*

      Information that identifies the resource.

      - **deviceCertificateId** *(string) --*

        The ID of the certificate attached to the resource.

      - **caCertificateId** *(string) --*

        The ID of the CA certificate used to authorize the certificate.

      - **cognitoIdentityPoolId** *(string) --*

        The ID of the Amazon Cognito identity pool.

      - **clientId** *(string) --*

        The client ID.

      - **policyVersionIdentifier** *(dict) --*

        The version of the policy associated with the resource.

        - **policyName** *(string) --*

          The name of the policy.

        - **policyVersionId** *(string) --*

          The ID of the version of the policy associated with the resource.

      - **account** *(string) --*

        The account with which the resource is associated.

    - **additionalInfo** *(dict) --*

      Other information about the resource.

      - *(string) --*

        - *(string) --*
    """


_ListAuditFindingsPaginateResponsefindingsTypeDef = TypedDict(
    "_ListAuditFindingsPaginateResponsefindingsTypeDef",
    {
        "findingId": str,
        "taskId": str,
        "checkName": str,
        "taskStartTime": datetime,
        "findingTime": datetime,
        "severity": str,
        "nonCompliantResource": ListAuditFindingsPaginateResponsefindingsnonCompliantResourceTypeDef,
        "relatedResources": List[
            ListAuditFindingsPaginateResponsefindingsrelatedResourcesTypeDef
        ],
        "reasonForNonCompliance": str,
        "reasonForNonComplianceCode": str,
    },
    total=False,
)


class ListAuditFindingsPaginateResponsefindingsTypeDef(
    _ListAuditFindingsPaginateResponsefindingsTypeDef
):
    """
    Type definition for `ListAuditFindingsPaginateResponse` `findings`

    The findings (results) of the audit.

    - **findingId** *(string) --*

      A unique identifier for this set of audit findings. This identifier is used to apply
      mitigation tasks to one or more sets of findings.

    - **taskId** *(string) --*

      The ID of the audit that generated this result (finding).

    - **checkName** *(string) --*

      The audit check that generated this result.

    - **taskStartTime** *(datetime) --*

      The time the audit started.

    - **findingTime** *(datetime) --*

      The time the result (finding) was discovered.

    - **severity** *(string) --*

      The severity of the result (finding).

    - **nonCompliantResource** *(dict) --*

      The resource that was found to be noncompliant with the audit check.

      - **resourceType** *(string) --*

        The type of the noncompliant resource.

      - **resourceIdentifier** *(dict) --*

        Information that identifies the noncompliant resource.

        - **deviceCertificateId** *(string) --*

          The ID of the certificate attached to the resource.

        - **caCertificateId** *(string) --*

          The ID of the CA certificate used to authorize the certificate.

        - **cognitoIdentityPoolId** *(string) --*

          The ID of the Amazon Cognito identity pool.

        - **clientId** *(string) --*

          The client ID.

        - **policyVersionIdentifier** *(dict) --*

          The version of the policy associated with the resource.

          - **policyName** *(string) --*

            The name of the policy.

          - **policyVersionId** *(string) --*

            The ID of the version of the policy associated with the resource.

        - **account** *(string) --*

          The account with which the resource is associated.

      - **additionalInfo** *(dict) --*

        Other information about the noncompliant resource.

        - *(string) --*

          - *(string) --*

    - **relatedResources** *(list) --*

      The list of related resources.

      - *(dict) --*

        Information about a related resource.

        - **resourceType** *(string) --*

          The type of resource.

        - **resourceIdentifier** *(dict) --*

          Information that identifies the resource.

          - **deviceCertificateId** *(string) --*

            The ID of the certificate attached to the resource.

          - **caCertificateId** *(string) --*

            The ID of the CA certificate used to authorize the certificate.

          - **cognitoIdentityPoolId** *(string) --*

            The ID of the Amazon Cognito identity pool.

          - **clientId** *(string) --*

            The client ID.

          - **policyVersionIdentifier** *(dict) --*

            The version of the policy associated with the resource.

            - **policyName** *(string) --*

              The name of the policy.

            - **policyVersionId** *(string) --*

              The ID of the version of the policy associated with the resource.

          - **account** *(string) --*

            The account with which the resource is associated.

        - **additionalInfo** *(dict) --*

          Other information about the resource.

          - *(string) --*

            - *(string) --*

    - **reasonForNonCompliance** *(string) --*

      The reason the resource was noncompliant.

    - **reasonForNonComplianceCode** *(string) --*

      A code that indicates the reason that the resource was noncompliant.
    """


_ListAuditFindingsPaginateResponseTypeDef = TypedDict(
    "_ListAuditFindingsPaginateResponseTypeDef",
    {
        "findings": List[ListAuditFindingsPaginateResponsefindingsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListAuditFindingsPaginateResponseTypeDef(
    _ListAuditFindingsPaginateResponseTypeDef
):
    """
    Type definition for `ListAuditFindingsPaginate` `Response`

    - **findings** *(list) --*

      The findings (results) of the audit.

      - *(dict) --*

        The findings (results) of the audit.

        - **findingId** *(string) --*

          A unique identifier for this set of audit findings. This identifier is used to apply
          mitigation tasks to one or more sets of findings.

        - **taskId** *(string) --*

          The ID of the audit that generated this result (finding).

        - **checkName** *(string) --*

          The audit check that generated this result.

        - **taskStartTime** *(datetime) --*

          The time the audit started.

        - **findingTime** *(datetime) --*

          The time the result (finding) was discovered.

        - **severity** *(string) --*

          The severity of the result (finding).

        - **nonCompliantResource** *(dict) --*

          The resource that was found to be noncompliant with the audit check.

          - **resourceType** *(string) --*

            The type of the noncompliant resource.

          - **resourceIdentifier** *(dict) --*

            Information that identifies the noncompliant resource.

            - **deviceCertificateId** *(string) --*

              The ID of the certificate attached to the resource.

            - **caCertificateId** *(string) --*

              The ID of the CA certificate used to authorize the certificate.

            - **cognitoIdentityPoolId** *(string) --*

              The ID of the Amazon Cognito identity pool.

            - **clientId** *(string) --*

              The client ID.

            - **policyVersionIdentifier** *(dict) --*

              The version of the policy associated with the resource.

              - **policyName** *(string) --*

                The name of the policy.

              - **policyVersionId** *(string) --*

                The ID of the version of the policy associated with the resource.

            - **account** *(string) --*

              The account with which the resource is associated.

          - **additionalInfo** *(dict) --*

            Other information about the noncompliant resource.

            - *(string) --*

              - *(string) --*

        - **relatedResources** *(list) --*

          The list of related resources.

          - *(dict) --*

            Information about a related resource.

            - **resourceType** *(string) --*

              The type of resource.

            - **resourceIdentifier** *(dict) --*

              Information that identifies the resource.

              - **deviceCertificateId** *(string) --*

                The ID of the certificate attached to the resource.

              - **caCertificateId** *(string) --*

                The ID of the CA certificate used to authorize the certificate.

              - **cognitoIdentityPoolId** *(string) --*

                The ID of the Amazon Cognito identity pool.

              - **clientId** *(string) --*

                The client ID.

              - **policyVersionIdentifier** *(dict) --*

                The version of the policy associated with the resource.

                - **policyName** *(string) --*

                  The name of the policy.

                - **policyVersionId** *(string) --*

                  The ID of the version of the policy associated with the resource.

              - **account** *(string) --*

                The account with which the resource is associated.

            - **additionalInfo** *(dict) --*

              Other information about the resource.

              - *(string) --*

                - *(string) --*

        - **reasonForNonCompliance** *(string) --*

          The reason the resource was noncompliant.

        - **reasonForNonComplianceCode** *(string) --*

          A code that indicates the reason that the resource was noncompliant.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListAuditFindingsPaginateresourceIdentifierpolicyVersionIdentifierTypeDef = TypedDict(
    "_ListAuditFindingsPaginateresourceIdentifierpolicyVersionIdentifierTypeDef",
    {"policyName": str, "policyVersionId": str},
    total=False,
)


class ListAuditFindingsPaginateresourceIdentifierpolicyVersionIdentifierTypeDef(
    _ListAuditFindingsPaginateresourceIdentifierpolicyVersionIdentifierTypeDef
):
    """
    Type definition for `ListAuditFindingsPaginateresourceIdentifier` `policyVersionIdentifier`

    The version of the policy associated with the resource.

    - **policyName** *(string) --*

      The name of the policy.

    - **policyVersionId** *(string) --*

      The ID of the version of the policy associated with the resource.
    """


_ListAuditFindingsPaginateresourceIdentifierTypeDef = TypedDict(
    "_ListAuditFindingsPaginateresourceIdentifierTypeDef",
    {
        "deviceCertificateId": str,
        "caCertificateId": str,
        "cognitoIdentityPoolId": str,
        "clientId": str,
        "policyVersionIdentifier": ListAuditFindingsPaginateresourceIdentifierpolicyVersionIdentifierTypeDef,
        "account": str,
    },
    total=False,
)


class ListAuditFindingsPaginateresourceIdentifierTypeDef(
    _ListAuditFindingsPaginateresourceIdentifierTypeDef
):
    """
    Type definition for `ListAuditFindingsPaginate` `resourceIdentifier`

    Information identifying the noncompliant resource.

    - **deviceCertificateId** *(string) --*

      The ID of the certificate attached to the resource.

    - **caCertificateId** *(string) --*

      The ID of the CA certificate used to authorize the certificate.

    - **cognitoIdentityPoolId** *(string) --*

      The ID of the Amazon Cognito identity pool.

    - **clientId** *(string) --*

      The client ID.

    - **policyVersionIdentifier** *(dict) --*

      The version of the policy associated with the resource.

      - **policyName** *(string) --*

        The name of the policy.

      - **policyVersionId** *(string) --*

        The ID of the version of the policy associated with the resource.

    - **account** *(string) --*

      The account with which the resource is associated.
    """


_ListAuditTasksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAuditTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAuditTasksPaginatePaginationConfigTypeDef(
    _ListAuditTasksPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAuditTasksPaginate` `PaginationConfig`

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


_ListAuditTasksPaginateResponsetasksTypeDef = TypedDict(
    "_ListAuditTasksPaginateResponsetasksTypeDef",
    {"taskId": str, "taskStatus": str, "taskType": str},
    total=False,
)


class ListAuditTasksPaginateResponsetasksTypeDef(
    _ListAuditTasksPaginateResponsetasksTypeDef
):
    """
    Type definition for `ListAuditTasksPaginateResponse` `tasks`

    The audits that were performed.

    - **taskId** *(string) --*

      The ID of this audit.

    - **taskStatus** *(string) --*

      The status of this audit. One of "IN_PROGRESS", "COMPLETED", "FAILED", or "CANCELED".

    - **taskType** *(string) --*

      The type of this audit. One of "ON_DEMAND_AUDIT_TASK" or "SCHEDULED_AUDIT_TASK".
    """


_ListAuditTasksPaginateResponseTypeDef = TypedDict(
    "_ListAuditTasksPaginateResponseTypeDef",
    {"tasks": List[ListAuditTasksPaginateResponsetasksTypeDef], "NextToken": str},
    total=False,
)


class ListAuditTasksPaginateResponseTypeDef(_ListAuditTasksPaginateResponseTypeDef):
    """
    Type definition for `ListAuditTasksPaginate` `Response`

    - **tasks** *(list) --*

      The audits that were performed during the specified time period.

      - *(dict) --*

        The audits that were performed.

        - **taskId** *(string) --*

          The ID of this audit.

        - **taskStatus** *(string) --*

          The status of this audit. One of "IN_PROGRESS", "COMPLETED", "FAILED", or "CANCELED".

        - **taskType** *(string) --*

          The type of this audit. One of "ON_DEMAND_AUDIT_TASK" or "SCHEDULED_AUDIT_TASK".

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListAuthorizersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAuthorizersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAuthorizersPaginatePaginationConfigTypeDef(
    _ListAuthorizersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAuthorizersPaginate` `PaginationConfig`

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


_ListAuthorizersPaginateResponseauthorizersTypeDef = TypedDict(
    "_ListAuthorizersPaginateResponseauthorizersTypeDef",
    {"authorizerName": str, "authorizerArn": str},
    total=False,
)


class ListAuthorizersPaginateResponseauthorizersTypeDef(
    _ListAuthorizersPaginateResponseauthorizersTypeDef
):
    """
    Type definition for `ListAuthorizersPaginateResponse` `authorizers`

    The authorizer summary.

    - **authorizerName** *(string) --*

      The authorizer name.

    - **authorizerArn** *(string) --*

      The authorizer ARN.
    """


_ListAuthorizersPaginateResponseTypeDef = TypedDict(
    "_ListAuthorizersPaginateResponseTypeDef",
    {
        "authorizers": List[ListAuthorizersPaginateResponseauthorizersTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListAuthorizersPaginateResponseTypeDef(_ListAuthorizersPaginateResponseTypeDef):
    """
    Type definition for `ListAuthorizersPaginate` `Response`

    - **authorizers** *(list) --*

      The authorizers.

      - *(dict) --*

        The authorizer summary.

        - **authorizerName** *(string) --*

          The authorizer name.

        - **authorizerArn** *(string) --*

          The authorizer ARN.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListBillingGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListBillingGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListBillingGroupsPaginatePaginationConfigTypeDef(
    _ListBillingGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListBillingGroupsPaginate` `PaginationConfig`

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


_ListBillingGroupsPaginateResponsebillingGroupsTypeDef = TypedDict(
    "_ListBillingGroupsPaginateResponsebillingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)


class ListBillingGroupsPaginateResponsebillingGroupsTypeDef(
    _ListBillingGroupsPaginateResponsebillingGroupsTypeDef
):
    """
    Type definition for `ListBillingGroupsPaginateResponse` `billingGroups`

    The name and ARN of a group.

    - **groupName** *(string) --*

      The group name.

    - **groupArn** *(string) --*

      The group ARN.
    """


_ListBillingGroupsPaginateResponseTypeDef = TypedDict(
    "_ListBillingGroupsPaginateResponseTypeDef",
    {
        "billingGroups": List[ListBillingGroupsPaginateResponsebillingGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListBillingGroupsPaginateResponseTypeDef(
    _ListBillingGroupsPaginateResponseTypeDef
):
    """
    Type definition for `ListBillingGroupsPaginate` `Response`

    - **billingGroups** *(list) --*

      The list of billing groups.

      - *(dict) --*

        The name and ARN of a group.

        - **groupName** *(string) --*

          The group name.

        - **groupArn** *(string) --*

          The group ARN.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListCACertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCACertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCACertificatesPaginatePaginationConfigTypeDef(
    _ListCACertificatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListCACertificatesPaginate` `PaginationConfig`

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


_ListCACertificatesPaginateResponsecertificatesTypeDef = TypedDict(
    "_ListCACertificatesPaginateResponsecertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": str,
        "creationDate": datetime,
    },
    total=False,
)


class ListCACertificatesPaginateResponsecertificatesTypeDef(
    _ListCACertificatesPaginateResponsecertificatesTypeDef
):
    """
    Type definition for `ListCACertificatesPaginateResponse` `certificates`

    A CA certificate.

    - **certificateArn** *(string) --*

      The ARN of the CA certificate.

    - **certificateId** *(string) --*

      The ID of the CA certificate.

    - **status** *(string) --*

      The status of the CA certificate.

      The status value REGISTER_INACTIVE is deprecated and should not be used.

    - **creationDate** *(datetime) --*

      The date the CA certificate was created.
    """


_ListCACertificatesPaginateResponseTypeDef = TypedDict(
    "_ListCACertificatesPaginateResponseTypeDef",
    {
        "certificates": List[ListCACertificatesPaginateResponsecertificatesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListCACertificatesPaginateResponseTypeDef(
    _ListCACertificatesPaginateResponseTypeDef
):
    """
    Type definition for `ListCACertificatesPaginate` `Response`

    The output from the ListCACertificates operation.

    - **certificates** *(list) --*

      The CA certificates registered in your AWS account.

      - *(dict) --*

        A CA certificate.

        - **certificateArn** *(string) --*

          The ARN of the CA certificate.

        - **certificateId** *(string) --*

          The ID of the CA certificate.

        - **status** *(string) --*

          The status of the CA certificate.

          The status value REGISTER_INACTIVE is deprecated and should not be used.

        - **creationDate** *(datetime) --*

          The date the CA certificate was created.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListCertificatesByCAPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCertificatesByCAPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCertificatesByCAPaginatePaginationConfigTypeDef(
    _ListCertificatesByCAPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListCertificatesByCAPaginate` `PaginationConfig`

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


_ListCertificatesByCAPaginateResponsecertificatesTypeDef = TypedDict(
    "_ListCertificatesByCAPaginateResponsecertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": str,
        "creationDate": datetime,
    },
    total=False,
)


class ListCertificatesByCAPaginateResponsecertificatesTypeDef(
    _ListCertificatesByCAPaginateResponsecertificatesTypeDef
):
    """
    Type definition for `ListCertificatesByCAPaginateResponse` `certificates`

    Information about a certificate.

    - **certificateArn** *(string) --*

      The ARN of the certificate.

    - **certificateId** *(string) --*

      The ID of the certificate. (The last part of the certificate ARN contains the certificate
      ID.)

    - **status** *(string) --*

      The status of the certificate.

      The status value REGISTER_INACTIVE is deprecated and should not be used.

    - **creationDate** *(datetime) --*

      The date and time the certificate was created.
    """


_ListCertificatesByCAPaginateResponseTypeDef = TypedDict(
    "_ListCertificatesByCAPaginateResponseTypeDef",
    {
        "certificates": List[ListCertificatesByCAPaginateResponsecertificatesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListCertificatesByCAPaginateResponseTypeDef(
    _ListCertificatesByCAPaginateResponseTypeDef
):
    """
    Type definition for `ListCertificatesByCAPaginate` `Response`

    The output of the ListCertificatesByCA operation.

    - **certificates** *(list) --*

      The device certificates signed by the specified CA certificate.

      - *(dict) --*

        Information about a certificate.

        - **certificateArn** *(string) --*

          The ARN of the certificate.

        - **certificateId** *(string) --*

          The ID of the certificate. (The last part of the certificate ARN contains the certificate
          ID.)

        - **status** *(string) --*

          The status of the certificate.

          The status value REGISTER_INACTIVE is deprecated and should not be used.

        - **creationDate** *(datetime) --*

          The date and time the certificate was created.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListCertificatesPaginatePaginationConfigTypeDef(
    _ListCertificatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListCertificatesPaginate` `PaginationConfig`

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


_ListCertificatesPaginateResponsecertificatesTypeDef = TypedDict(
    "_ListCertificatesPaginateResponsecertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "status": str,
        "creationDate": datetime,
    },
    total=False,
)


class ListCertificatesPaginateResponsecertificatesTypeDef(
    _ListCertificatesPaginateResponsecertificatesTypeDef
):
    """
    Type definition for `ListCertificatesPaginateResponse` `certificates`

    Information about a certificate.

    - **certificateArn** *(string) --*

      The ARN of the certificate.

    - **certificateId** *(string) --*

      The ID of the certificate. (The last part of the certificate ARN contains the certificate
      ID.)

    - **status** *(string) --*

      The status of the certificate.

      The status value REGISTER_INACTIVE is deprecated and should not be used.

    - **creationDate** *(datetime) --*

      The date and time the certificate was created.
    """


_ListCertificatesPaginateResponseTypeDef = TypedDict(
    "_ListCertificatesPaginateResponseTypeDef",
    {
        "certificates": List[ListCertificatesPaginateResponsecertificatesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListCertificatesPaginateResponseTypeDef(_ListCertificatesPaginateResponseTypeDef):
    """
    Type definition for `ListCertificatesPaginate` `Response`

    The output of the ListCertificates operation.

    - **certificates** *(list) --*

      The descriptions of the certificates.

      - *(dict) --*

        Information about a certificate.

        - **certificateArn** *(string) --*

          The ARN of the certificate.

        - **certificateId** *(string) --*

          The ID of the certificate. (The last part of the certificate ARN contains the certificate
          ID.)

        - **status** *(string) --*

          The status of the certificate.

          The status value REGISTER_INACTIVE is deprecated and should not be used.

        - **creationDate** *(datetime) --*

          The date and time the certificate was created.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListIndicesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListIndicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListIndicesPaginatePaginationConfigTypeDef(
    _ListIndicesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListIndicesPaginate` `PaginationConfig`

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


_ListIndicesPaginateResponseTypeDef = TypedDict(
    "_ListIndicesPaginateResponseTypeDef",
    {"indexNames": List[str], "NextToken": str},
    total=False,
)


class ListIndicesPaginateResponseTypeDef(_ListIndicesPaginateResponseTypeDef):
    """
    Type definition for `ListIndicesPaginate` `Response`

    - **indexNames** *(list) --*

      The index names.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListJobExecutionsForJobPaginatePaginationConfigTypeDef = TypedDict(
    "_ListJobExecutionsForJobPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListJobExecutionsForJobPaginatePaginationConfigTypeDef(
    _ListJobExecutionsForJobPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListJobExecutionsForJobPaginate` `PaginationConfig`

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


_ListJobExecutionsForJobPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef = TypedDict(
    "_ListJobExecutionsForJobPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef",
    {
        "status": str,
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
    },
    total=False,
)


class ListJobExecutionsForJobPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef(
    _ListJobExecutionsForJobPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef
):
    """
    Type definition for `ListJobExecutionsForJobPaginateResponseexecutionSummaries` `jobExecutionSummary`

    Contains a subset of information about a job execution.

    - **status** *(string) --*

      The status of the job execution.

    - **queuedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job execution was queued.

    - **startedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job execution started.

    - **lastUpdatedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job execution was last updated.

    - **executionNumber** *(integer) --*

      A string (consisting of the digits "0" through "9") which identifies this particular
      job execution on this particular device. It can be used later in commands which return
      or update job execution information.
    """


_ListJobExecutionsForJobPaginateResponseexecutionSummariesTypeDef = TypedDict(
    "_ListJobExecutionsForJobPaginateResponseexecutionSummariesTypeDef",
    {
        "thingArn": str,
        "jobExecutionSummary": ListJobExecutionsForJobPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef,
    },
    total=False,
)


class ListJobExecutionsForJobPaginateResponseexecutionSummariesTypeDef(
    _ListJobExecutionsForJobPaginateResponseexecutionSummariesTypeDef
):
    """
    Type definition for `ListJobExecutionsForJobPaginateResponse` `executionSummaries`

    Contains a summary of information about job executions for a specific job.

    - **thingArn** *(string) --*

      The ARN of the thing on which the job execution is running.

    - **jobExecutionSummary** *(dict) --*

      Contains a subset of information about a job execution.

      - **status** *(string) --*

        The status of the job execution.

      - **queuedAt** *(datetime) --*

        The time, in seconds since the epoch, when the job execution was queued.

      - **startedAt** *(datetime) --*

        The time, in seconds since the epoch, when the job execution started.

      - **lastUpdatedAt** *(datetime) --*

        The time, in seconds since the epoch, when the job execution was last updated.

      - **executionNumber** *(integer) --*

        A string (consisting of the digits "0" through "9") which identifies this particular
        job execution on this particular device. It can be used later in commands which return
        or update job execution information.
    """


_ListJobExecutionsForJobPaginateResponseTypeDef = TypedDict(
    "_ListJobExecutionsForJobPaginateResponseTypeDef",
    {
        "executionSummaries": List[
            ListJobExecutionsForJobPaginateResponseexecutionSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListJobExecutionsForJobPaginateResponseTypeDef(
    _ListJobExecutionsForJobPaginateResponseTypeDef
):
    """
    Type definition for `ListJobExecutionsForJobPaginate` `Response`

    - **executionSummaries** *(list) --*

      A list of job execution summaries.

      - *(dict) --*

        Contains a summary of information about job executions for a specific job.

        - **thingArn** *(string) --*

          The ARN of the thing on which the job execution is running.

        - **jobExecutionSummary** *(dict) --*

          Contains a subset of information about a job execution.

          - **status** *(string) --*

            The status of the job execution.

          - **queuedAt** *(datetime) --*

            The time, in seconds since the epoch, when the job execution was queued.

          - **startedAt** *(datetime) --*

            The time, in seconds since the epoch, when the job execution started.

          - **lastUpdatedAt** *(datetime) --*

            The time, in seconds since the epoch, when the job execution was last updated.

          - **executionNumber** *(integer) --*

            A string (consisting of the digits "0" through "9") which identifies this particular
            job execution on this particular device. It can be used later in commands which return
            or update job execution information.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListJobExecutionsForThingPaginatePaginationConfigTypeDef = TypedDict(
    "_ListJobExecutionsForThingPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListJobExecutionsForThingPaginatePaginationConfigTypeDef(
    _ListJobExecutionsForThingPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListJobExecutionsForThingPaginate` `PaginationConfig`

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


_ListJobExecutionsForThingPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef = TypedDict(
    "_ListJobExecutionsForThingPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef",
    {
        "status": str,
        "queuedAt": datetime,
        "startedAt": datetime,
        "lastUpdatedAt": datetime,
        "executionNumber": int,
    },
    total=False,
)


class ListJobExecutionsForThingPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef(
    _ListJobExecutionsForThingPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef
):
    """
    Type definition for `ListJobExecutionsForThingPaginateResponseexecutionSummaries` `jobExecutionSummary`

    Contains a subset of information about a job execution.

    - **status** *(string) --*

      The status of the job execution.

    - **queuedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job execution was queued.

    - **startedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job execution started.

    - **lastUpdatedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job execution was last updated.

    - **executionNumber** *(integer) --*

      A string (consisting of the digits "0" through "9") which identifies this particular
      job execution on this particular device. It can be used later in commands which return
      or update job execution information.
    """


_ListJobExecutionsForThingPaginateResponseexecutionSummariesTypeDef = TypedDict(
    "_ListJobExecutionsForThingPaginateResponseexecutionSummariesTypeDef",
    {
        "jobId": str,
        "jobExecutionSummary": ListJobExecutionsForThingPaginateResponseexecutionSummariesjobExecutionSummaryTypeDef,
    },
    total=False,
)


class ListJobExecutionsForThingPaginateResponseexecutionSummariesTypeDef(
    _ListJobExecutionsForThingPaginateResponseexecutionSummariesTypeDef
):
    """
    Type definition for `ListJobExecutionsForThingPaginateResponse` `executionSummaries`

    The job execution summary for a thing.

    - **jobId** *(string) --*

      The unique identifier you assigned to this job when it was created.

    - **jobExecutionSummary** *(dict) --*

      Contains a subset of information about a job execution.

      - **status** *(string) --*

        The status of the job execution.

      - **queuedAt** *(datetime) --*

        The time, in seconds since the epoch, when the job execution was queued.

      - **startedAt** *(datetime) --*

        The time, in seconds since the epoch, when the job execution started.

      - **lastUpdatedAt** *(datetime) --*

        The time, in seconds since the epoch, when the job execution was last updated.

      - **executionNumber** *(integer) --*

        A string (consisting of the digits "0" through "9") which identifies this particular
        job execution on this particular device. It can be used later in commands which return
        or update job execution information.
    """


_ListJobExecutionsForThingPaginateResponseTypeDef = TypedDict(
    "_ListJobExecutionsForThingPaginateResponseTypeDef",
    {
        "executionSummaries": List[
            ListJobExecutionsForThingPaginateResponseexecutionSummariesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListJobExecutionsForThingPaginateResponseTypeDef(
    _ListJobExecutionsForThingPaginateResponseTypeDef
):
    """
    Type definition for `ListJobExecutionsForThingPaginate` `Response`

    - **executionSummaries** *(list) --*

      A list of job execution summaries.

      - *(dict) --*

        The job execution summary for a thing.

        - **jobId** *(string) --*

          The unique identifier you assigned to this job when it was created.

        - **jobExecutionSummary** *(dict) --*

          Contains a subset of information about a job execution.

          - **status** *(string) --*

            The status of the job execution.

          - **queuedAt** *(datetime) --*

            The time, in seconds since the epoch, when the job execution was queued.

          - **startedAt** *(datetime) --*

            The time, in seconds since the epoch, when the job execution started.

          - **lastUpdatedAt** *(datetime) --*

            The time, in seconds since the epoch, when the job execution was last updated.

          - **executionNumber** *(integer) --*

            A string (consisting of the digits "0" through "9") which identifies this particular
            job execution on this particular device. It can be used later in commands which return
            or update job execution information.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListJobsPaginatePaginationConfigTypeDef(_ListJobsPaginatePaginationConfigTypeDef):
    """
    Type definition for `ListJobsPaginate` `PaginationConfig`

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


_ListJobsPaginateResponsejobsTypeDef = TypedDict(
    "_ListJobsPaginateResponsejobsTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "thingGroupId": str,
        "targetSelection": str,
        "status": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "completedAt": datetime,
    },
    total=False,
)


class ListJobsPaginateResponsejobsTypeDef(_ListJobsPaginateResponsejobsTypeDef):
    """
    Type definition for `ListJobsPaginateResponse` `jobs`

    The job summary.

    - **jobArn** *(string) --*

      The job ARN.

    - **jobId** *(string) --*

      The unique identifier you assigned to this job when it was created.

    - **thingGroupId** *(string) --*

      The ID of the thing group.

    - **targetSelection** *(string) --*

      Specifies whether the job will continue to run (CONTINUOUS), or will be complete after
      all those things specified as targets have completed the job (SNAPSHOT). If continuous,
      the job may also be run on a thing when a change is detected in a target. For example, a
      job will run on a thing when the thing is added to a target group, even after the job was
      completed by all things originally in the group.

    - **status** *(string) --*

      The job summary status.

    - **createdAt** *(datetime) --*

      The time, in seconds since the epoch, when the job was created.

    - **lastUpdatedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job was last updated.

    - **completedAt** *(datetime) --*

      The time, in seconds since the epoch, when the job completed.
    """


_ListJobsPaginateResponseTypeDef = TypedDict(
    "_ListJobsPaginateResponseTypeDef",
    {"jobs": List[ListJobsPaginateResponsejobsTypeDef], "NextToken": str},
    total=False,
)


class ListJobsPaginateResponseTypeDef(_ListJobsPaginateResponseTypeDef):
    """
    Type definition for `ListJobsPaginate` `Response`

    - **jobs** *(list) --*

      A list of jobs.

      - *(dict) --*

        The job summary.

        - **jobArn** *(string) --*

          The job ARN.

        - **jobId** *(string) --*

          The unique identifier you assigned to this job when it was created.

        - **thingGroupId** *(string) --*

          The ID of the thing group.

        - **targetSelection** *(string) --*

          Specifies whether the job will continue to run (CONTINUOUS), or will be complete after
          all those things specified as targets have completed the job (SNAPSHOT). If continuous,
          the job may also be run on a thing when a change is detected in a target. For example, a
          job will run on a thing when the thing is added to a target group, even after the job was
          completed by all things originally in the group.

        - **status** *(string) --*

          The job summary status.

        - **createdAt** *(datetime) --*

          The time, in seconds since the epoch, when the job was created.

        - **lastUpdatedAt** *(datetime) --*

          The time, in seconds since the epoch, when the job was last updated.

        - **completedAt** *(datetime) --*

          The time, in seconds since the epoch, when the job completed.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListOTAUpdatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOTAUpdatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListOTAUpdatesPaginatePaginationConfigTypeDef(
    _ListOTAUpdatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListOTAUpdatesPaginate` `PaginationConfig`

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


_ListOTAUpdatesPaginateResponseotaUpdatesTypeDef = TypedDict(
    "_ListOTAUpdatesPaginateResponseotaUpdatesTypeDef",
    {"otaUpdateId": str, "otaUpdateArn": str, "creationDate": datetime},
    total=False,
)


class ListOTAUpdatesPaginateResponseotaUpdatesTypeDef(
    _ListOTAUpdatesPaginateResponseotaUpdatesTypeDef
):
    """
    Type definition for `ListOTAUpdatesPaginateResponse` `otaUpdates`

    An OTA update summary.

    - **otaUpdateId** *(string) --*

      The OTA update ID.

    - **otaUpdateArn** *(string) --*

      The OTA update ARN.

    - **creationDate** *(datetime) --*

      The date when the OTA update was created.
    """


_ListOTAUpdatesPaginateResponseTypeDef = TypedDict(
    "_ListOTAUpdatesPaginateResponseTypeDef",
    {
        "otaUpdates": List[ListOTAUpdatesPaginateResponseotaUpdatesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListOTAUpdatesPaginateResponseTypeDef(_ListOTAUpdatesPaginateResponseTypeDef):
    """
    Type definition for `ListOTAUpdatesPaginate` `Response`

    - **otaUpdates** *(list) --*

      A list of OTA update jobs.

      - *(dict) --*

        An OTA update summary.

        - **otaUpdateId** *(string) --*

          The OTA update ID.

        - **otaUpdateArn** *(string) --*

          The OTA update ARN.

        - **creationDate** *(datetime) --*

          The date when the OTA update was created.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListOutgoingCertificatesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListOutgoingCertificatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListOutgoingCertificatesPaginatePaginationConfigTypeDef(
    _ListOutgoingCertificatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListOutgoingCertificatesPaginate` `PaginationConfig`

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


_ListOutgoingCertificatesPaginateResponseoutgoingCertificatesTypeDef = TypedDict(
    "_ListOutgoingCertificatesPaginateResponseoutgoingCertificatesTypeDef",
    {
        "certificateArn": str,
        "certificateId": str,
        "transferredTo": str,
        "transferDate": datetime,
        "transferMessage": str,
        "creationDate": datetime,
    },
    total=False,
)


class ListOutgoingCertificatesPaginateResponseoutgoingCertificatesTypeDef(
    _ListOutgoingCertificatesPaginateResponseoutgoingCertificatesTypeDef
):
    """
    Type definition for `ListOutgoingCertificatesPaginateResponse` `outgoingCertificates`

    A certificate that has been transferred but not yet accepted.

    - **certificateArn** *(string) --*

      The certificate ARN.

    - **certificateId** *(string) --*

      The certificate ID.

    - **transferredTo** *(string) --*

      The AWS account to which the transfer was made.

    - **transferDate** *(datetime) --*

      The date the transfer was initiated.

    - **transferMessage** *(string) --*

      The transfer message.

    - **creationDate** *(datetime) --*

      The certificate creation date.
    """


_ListOutgoingCertificatesPaginateResponseTypeDef = TypedDict(
    "_ListOutgoingCertificatesPaginateResponseTypeDef",
    {
        "outgoingCertificates": List[
            ListOutgoingCertificatesPaginateResponseoutgoingCertificatesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListOutgoingCertificatesPaginateResponseTypeDef(
    _ListOutgoingCertificatesPaginateResponseTypeDef
):
    """
    Type definition for `ListOutgoingCertificatesPaginate` `Response`

    The output from the ListOutgoingCertificates operation.

    - **outgoingCertificates** *(list) --*

      The certificates that are being transferred but not yet accepted.

      - *(dict) --*

        A certificate that has been transferred but not yet accepted.

        - **certificateArn** *(string) --*

          The certificate ARN.

        - **certificateId** *(string) --*

          The certificate ID.

        - **transferredTo** *(string) --*

          The AWS account to which the transfer was made.

        - **transferDate** *(datetime) --*

          The date the transfer was initiated.

        - **transferMessage** *(string) --*

          The transfer message.

        - **creationDate** *(datetime) --*

          The certificate creation date.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPoliciesPaginatePaginationConfigTypeDef(
    _ListPoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPoliciesPaginate` `PaginationConfig`

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


_ListPoliciesPaginateResponsepoliciesTypeDef = TypedDict(
    "_ListPoliciesPaginateResponsepoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)


class ListPoliciesPaginateResponsepoliciesTypeDef(
    _ListPoliciesPaginateResponsepoliciesTypeDef
):
    """
    Type definition for `ListPoliciesPaginateResponse` `policies`

    Describes an AWS IoT policy.

    - **policyName** *(string) --*

      The policy name.

    - **policyArn** *(string) --*

      The policy ARN.
    """


_ListPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListPoliciesPaginateResponseTypeDef",
    {"policies": List[ListPoliciesPaginateResponsepoliciesTypeDef], "NextToken": str},
    total=False,
)


class ListPoliciesPaginateResponseTypeDef(_ListPoliciesPaginateResponseTypeDef):
    """
    Type definition for `ListPoliciesPaginate` `Response`

    The output from the ListPolicies operation.

    - **policies** *(list) --*

      The descriptions of the policies.

      - *(dict) --*

        Describes an AWS IoT policy.

        - **policyName** *(string) --*

          The policy name.

        - **policyArn** *(string) --*

          The policy ARN.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListPolicyPrincipalsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPolicyPrincipalsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPolicyPrincipalsPaginatePaginationConfigTypeDef(
    _ListPolicyPrincipalsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPolicyPrincipalsPaginate` `PaginationConfig`

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


_ListPolicyPrincipalsPaginateResponseTypeDef = TypedDict(
    "_ListPolicyPrincipalsPaginateResponseTypeDef",
    {"principals": List[str], "NextToken": str},
    total=False,
)


class ListPolicyPrincipalsPaginateResponseTypeDef(
    _ListPolicyPrincipalsPaginateResponseTypeDef
):
    """
    Type definition for `ListPolicyPrincipalsPaginate` `Response`

    The output from the ListPolicyPrincipals operation.

    - **principals** *(list) --*

      The descriptions of the principals.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListPrincipalPoliciesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPrincipalPoliciesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPrincipalPoliciesPaginatePaginationConfigTypeDef(
    _ListPrincipalPoliciesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPrincipalPoliciesPaginate` `PaginationConfig`

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


_ListPrincipalPoliciesPaginateResponsepoliciesTypeDef = TypedDict(
    "_ListPrincipalPoliciesPaginateResponsepoliciesTypeDef",
    {"policyName": str, "policyArn": str},
    total=False,
)


class ListPrincipalPoliciesPaginateResponsepoliciesTypeDef(
    _ListPrincipalPoliciesPaginateResponsepoliciesTypeDef
):
    """
    Type definition for `ListPrincipalPoliciesPaginateResponse` `policies`

    Describes an AWS IoT policy.

    - **policyName** *(string) --*

      The policy name.

    - **policyArn** *(string) --*

      The policy ARN.
    """


_ListPrincipalPoliciesPaginateResponseTypeDef = TypedDict(
    "_ListPrincipalPoliciesPaginateResponseTypeDef",
    {
        "policies": List[ListPrincipalPoliciesPaginateResponsepoliciesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListPrincipalPoliciesPaginateResponseTypeDef(
    _ListPrincipalPoliciesPaginateResponseTypeDef
):
    """
    Type definition for `ListPrincipalPoliciesPaginate` `Response`

    The output from the ListPrincipalPolicies operation.

    - **policies** *(list) --*

      The policies.

      - *(dict) --*

        Describes an AWS IoT policy.

        - **policyName** *(string) --*

          The policy name.

        - **policyArn** *(string) --*

          The policy ARN.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListPrincipalThingsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPrincipalThingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPrincipalThingsPaginatePaginationConfigTypeDef(
    _ListPrincipalThingsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPrincipalThingsPaginate` `PaginationConfig`

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


_ListPrincipalThingsPaginateResponseTypeDef = TypedDict(
    "_ListPrincipalThingsPaginateResponseTypeDef",
    {"things": List[str], "NextToken": str},
    total=False,
)


class ListPrincipalThingsPaginateResponseTypeDef(
    _ListPrincipalThingsPaginateResponseTypeDef
):
    """
    Type definition for `ListPrincipalThingsPaginate` `Response`

    The output from the ListPrincipalThings operation.

    - **things** *(list) --*

      The things.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListRoleAliasesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRoleAliasesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRoleAliasesPaginatePaginationConfigTypeDef(
    _ListRoleAliasesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRoleAliasesPaginate` `PaginationConfig`

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


_ListRoleAliasesPaginateResponseTypeDef = TypedDict(
    "_ListRoleAliasesPaginateResponseTypeDef",
    {"roleAliases": List[str], "NextToken": str},
    total=False,
)


class ListRoleAliasesPaginateResponseTypeDef(_ListRoleAliasesPaginateResponseTypeDef):
    """
    Type definition for `ListRoleAliasesPaginate` `Response`

    - **roleAliases** *(list) --*

      The role aliases.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListScheduledAuditsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListScheduledAuditsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListScheduledAuditsPaginatePaginationConfigTypeDef(
    _ListScheduledAuditsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListScheduledAuditsPaginate` `PaginationConfig`

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


_ListScheduledAuditsPaginateResponsescheduledAuditsTypeDef = TypedDict(
    "_ListScheduledAuditsPaginateResponsescheduledAuditsTypeDef",
    {
        "scheduledAuditName": str,
        "scheduledAuditArn": str,
        "frequency": str,
        "dayOfMonth": str,
        "dayOfWeek": str,
    },
    total=False,
)


class ListScheduledAuditsPaginateResponsescheduledAuditsTypeDef(
    _ListScheduledAuditsPaginateResponsescheduledAuditsTypeDef
):
    """
    Type definition for `ListScheduledAuditsPaginateResponse` `scheduledAudits`

    Information about the scheduled audit.

    - **scheduledAuditName** *(string) --*

      The name of the scheduled audit.

    - **scheduledAuditArn** *(string) --*

      The ARN of the scheduled audit.

    - **frequency** *(string) --*

      How often the scheduled audit occurs.

    - **dayOfMonth** *(string) --*

      The day of the month on which the scheduled audit is run (if the ``frequency`` is
      "MONTHLY"). If days 29-31 are specified, and the month does not have that many days, the
      audit takes place on the "LAST" day of the month.

    - **dayOfWeek** *(string) --*

      The day of the week on which the scheduled audit is run (if the ``frequency`` is "WEEKLY"
      or "BIWEEKLY").
    """


_ListScheduledAuditsPaginateResponseTypeDef = TypedDict(
    "_ListScheduledAuditsPaginateResponseTypeDef",
    {
        "scheduledAudits": List[
            ListScheduledAuditsPaginateResponsescheduledAuditsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListScheduledAuditsPaginateResponseTypeDef(
    _ListScheduledAuditsPaginateResponseTypeDef
):
    """
    Type definition for `ListScheduledAuditsPaginate` `Response`

    - **scheduledAudits** *(list) --*

      The list of scheduled audits.

      - *(dict) --*

        Information about the scheduled audit.

        - **scheduledAuditName** *(string) --*

          The name of the scheduled audit.

        - **scheduledAuditArn** *(string) --*

          The ARN of the scheduled audit.

        - **frequency** *(string) --*

          How often the scheduled audit occurs.

        - **dayOfMonth** *(string) --*

          The day of the month on which the scheduled audit is run (if the ``frequency`` is
          "MONTHLY"). If days 29-31 are specified, and the month does not have that many days, the
          audit takes place on the "LAST" day of the month.

        - **dayOfWeek** *(string) --*

          The day of the week on which the scheduled audit is run (if the ``frequency`` is "WEEKLY"
          or "BIWEEKLY").

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListSecurityProfilesForTargetPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSecurityProfilesForTargetPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSecurityProfilesForTargetPaginatePaginationConfigTypeDef(
    _ListSecurityProfilesForTargetPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSecurityProfilesForTargetPaginate` `PaginationConfig`

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


_ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef = TypedDict(
    "_ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef",
    {"name": str, "arn": str},
    total=False,
)


class ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef(
    _ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef
):
    """
    Type definition for `ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappings` `securityProfileIdentifier`

    Information that identifies the security profile.

    - **name** *(string) --*

      The name you have given to the security profile.

    - **arn** *(string) --*

      The ARN of the security profile.
    """


_ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingstargetTypeDef = TypedDict(
    "_ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingstargetTypeDef",
    {"arn": str},
    total=False,
)


class ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingstargetTypeDef(
    _ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingstargetTypeDef
):
    """
    Type definition for `ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappings` `target`

    Information about the target (thing group) associated with the security profile.

    - **arn** *(string) --*

      The ARN of the security profile.
    """


_ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingsTypeDef = TypedDict(
    "_ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingsTypeDef",
    {
        "securityProfileIdentifier": ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingssecurityProfileIdentifierTypeDef,
        "target": ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingstargetTypeDef,
    },
    total=False,
)


class ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingsTypeDef(
    _ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingsTypeDef
):
    """
    Type definition for `ListSecurityProfilesForTargetPaginateResponse` `securityProfileTargetMappings`

    Information about a security profile and the target associated with it.

    - **securityProfileIdentifier** *(dict) --*

      Information that identifies the security profile.

      - **name** *(string) --*

        The name you have given to the security profile.

      - **arn** *(string) --*

        The ARN of the security profile.

    - **target** *(dict) --*

      Information about the target (thing group) associated with the security profile.

      - **arn** *(string) --*

        The ARN of the security profile.
    """


_ListSecurityProfilesForTargetPaginateResponseTypeDef = TypedDict(
    "_ListSecurityProfilesForTargetPaginateResponseTypeDef",
    {
        "securityProfileTargetMappings": List[
            ListSecurityProfilesForTargetPaginateResponsesecurityProfileTargetMappingsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListSecurityProfilesForTargetPaginateResponseTypeDef(
    _ListSecurityProfilesForTargetPaginateResponseTypeDef
):
    """
    Type definition for `ListSecurityProfilesForTargetPaginate` `Response`

    - **securityProfileTargetMappings** *(list) --*

      A list of security profiles and their associated targets.

      - *(dict) --*

        Information about a security profile and the target associated with it.

        - **securityProfileIdentifier** *(dict) --*

          Information that identifies the security profile.

          - **name** *(string) --*

            The name you have given to the security profile.

          - **arn** *(string) --*

            The ARN of the security profile.

        - **target** *(dict) --*

          Information about the target (thing group) associated with the security profile.

          - **arn** *(string) --*

            The ARN of the security profile.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListSecurityProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListSecurityProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListSecurityProfilesPaginatePaginationConfigTypeDef(
    _ListSecurityProfilesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListSecurityProfilesPaginate` `PaginationConfig`

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


_ListSecurityProfilesPaginateResponsesecurityProfileIdentifiersTypeDef = TypedDict(
    "_ListSecurityProfilesPaginateResponsesecurityProfileIdentifiersTypeDef",
    {"name": str, "arn": str},
    total=False,
)


class ListSecurityProfilesPaginateResponsesecurityProfileIdentifiersTypeDef(
    _ListSecurityProfilesPaginateResponsesecurityProfileIdentifiersTypeDef
):
    """
    Type definition for `ListSecurityProfilesPaginateResponse` `securityProfileIdentifiers`

    Identifying information for a Device Defender security profile.

    - **name** *(string) --*

      The name you have given to the security profile.

    - **arn** *(string) --*

      The ARN of the security profile.
    """


_ListSecurityProfilesPaginateResponseTypeDef = TypedDict(
    "_ListSecurityProfilesPaginateResponseTypeDef",
    {
        "securityProfileIdentifiers": List[
            ListSecurityProfilesPaginateResponsesecurityProfileIdentifiersTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListSecurityProfilesPaginateResponseTypeDef(
    _ListSecurityProfilesPaginateResponseTypeDef
):
    """
    Type definition for `ListSecurityProfilesPaginate` `Response`

    - **securityProfileIdentifiers** *(list) --*

      A list of security profile identifiers (names and ARNs).

      - *(dict) --*

        Identifying information for a Device Defender security profile.

        - **name** *(string) --*

          The name you have given to the security profile.

        - **arn** *(string) --*

          The ARN of the security profile.

    - **NextToken** *(string) --*

      A token to resume pagination.
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


_ListStreamsPaginateResponsestreamsTypeDef = TypedDict(
    "_ListStreamsPaginateResponsestreamsTypeDef",
    {"streamId": str, "streamArn": str, "streamVersion": int, "description": str},
    total=False,
)


class ListStreamsPaginateResponsestreamsTypeDef(
    _ListStreamsPaginateResponsestreamsTypeDef
):
    """
    Type definition for `ListStreamsPaginateResponse` `streams`

    A summary of a stream.

    - **streamId** *(string) --*

      The stream ID.

    - **streamArn** *(string) --*

      The stream ARN.

    - **streamVersion** *(integer) --*

      The stream version.

    - **description** *(string) --*

      A description of the stream.
    """


_ListStreamsPaginateResponseTypeDef = TypedDict(
    "_ListStreamsPaginateResponseTypeDef",
    {"streams": List[ListStreamsPaginateResponsestreamsTypeDef], "NextToken": str},
    total=False,
)


class ListStreamsPaginateResponseTypeDef(_ListStreamsPaginateResponseTypeDef):
    """
    Type definition for `ListStreamsPaginate` `Response`

    - **streams** *(list) --*

      A list of streams.

      - *(dict) --*

        A summary of a stream.

        - **streamId** *(string) --*

          The stream ID.

        - **streamArn** *(string) --*

          The stream ARN.

        - **streamVersion** *(integer) --*

          The stream version.

        - **description** *(string) --*

          A description of the stream.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListTagsForResourcePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTagsForResourcePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "StartingToken": str},
    total=False,
)


class ListTagsForResourcePaginatePaginationConfigTypeDef(
    _ListTagsForResourcePaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginate` `PaginationConfig`

    A dictionary that provides parameters to control pagination.

    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.

    - **StartingToken** *(string) --*

      A token to specify where to start paginating. This is the ``NextToken`` from a previous
      response.
    """


_ListTagsForResourcePaginateResponsetagsTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponsetagsTypeDef",
    {"Key": str, "Value": str},
    total=False,
)


class ListTagsForResourcePaginateResponsetagsTypeDef(
    _ListTagsForResourcePaginateResponsetagsTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginateResponse` `tags`

    A set of key/value pairs that are used to manage the resource.

    - **Key** *(string) --*

      The tag's key.

    - **Value** *(string) --*

      The tag's value.
    """


_ListTagsForResourcePaginateResponseTypeDef = TypedDict(
    "_ListTagsForResourcePaginateResponseTypeDef",
    {"tags": List[ListTagsForResourcePaginateResponsetagsTypeDef], "NextToken": str},
    total=False,
)


class ListTagsForResourcePaginateResponseTypeDef(
    _ListTagsForResourcePaginateResponseTypeDef
):
    """
    Type definition for `ListTagsForResourcePaginate` `Response`

    - **tags** *(list) --*

      The list of tags assigned to the resource.

      - *(dict) --*

        A set of key/value pairs that are used to manage the resource.

        - **Key** *(string) --*

          The tag's key.

        - **Value** *(string) --*

          The tag's value.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListTargetsForPolicyPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTargetsForPolicyPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTargetsForPolicyPaginatePaginationConfigTypeDef(
    _ListTargetsForPolicyPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTargetsForPolicyPaginate` `PaginationConfig`

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


_ListTargetsForPolicyPaginateResponseTypeDef = TypedDict(
    "_ListTargetsForPolicyPaginateResponseTypeDef",
    {"targets": List[str], "NextToken": str},
    total=False,
)


class ListTargetsForPolicyPaginateResponseTypeDef(
    _ListTargetsForPolicyPaginateResponseTypeDef
):
    """
    Type definition for `ListTargetsForPolicyPaginate` `Response`

    - **targets** *(list) --*

      The policy targets.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListTargetsForSecurityProfilePaginatePaginationConfigTypeDef = TypedDict(
    "_ListTargetsForSecurityProfilePaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTargetsForSecurityProfilePaginatePaginationConfigTypeDef(
    _ListTargetsForSecurityProfilePaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTargetsForSecurityProfilePaginate` `PaginationConfig`

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


_ListTargetsForSecurityProfilePaginateResponsesecurityProfileTargetsTypeDef = TypedDict(
    "_ListTargetsForSecurityProfilePaginateResponsesecurityProfileTargetsTypeDef",
    {"arn": str},
    total=False,
)


class ListTargetsForSecurityProfilePaginateResponsesecurityProfileTargetsTypeDef(
    _ListTargetsForSecurityProfilePaginateResponsesecurityProfileTargetsTypeDef
):
    """
    Type definition for `ListTargetsForSecurityProfilePaginateResponse` `securityProfileTargets`

    A target to which an alert is sent when a security profile behavior is violated.

    - **arn** *(string) --*

      The ARN of the security profile.
    """


_ListTargetsForSecurityProfilePaginateResponseTypeDef = TypedDict(
    "_ListTargetsForSecurityProfilePaginateResponseTypeDef",
    {
        "securityProfileTargets": List[
            ListTargetsForSecurityProfilePaginateResponsesecurityProfileTargetsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListTargetsForSecurityProfilePaginateResponseTypeDef(
    _ListTargetsForSecurityProfilePaginateResponseTypeDef
):
    """
    Type definition for `ListTargetsForSecurityProfilePaginate` `Response`

    - **securityProfileTargets** *(list) --*

      The thing groups to which the security profile is attached.

      - *(dict) --*

        A target to which an alert is sent when a security profile behavior is violated.

        - **arn** *(string) --*

          The ARN of the security profile.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListThingGroupsForThingPaginatePaginationConfigTypeDef = TypedDict(
    "_ListThingGroupsForThingPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListThingGroupsForThingPaginatePaginationConfigTypeDef(
    _ListThingGroupsForThingPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListThingGroupsForThingPaginate` `PaginationConfig`

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


_ListThingGroupsForThingPaginateResponsethingGroupsTypeDef = TypedDict(
    "_ListThingGroupsForThingPaginateResponsethingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)


class ListThingGroupsForThingPaginateResponsethingGroupsTypeDef(
    _ListThingGroupsForThingPaginateResponsethingGroupsTypeDef
):
    """
    Type definition for `ListThingGroupsForThingPaginateResponse` `thingGroups`

    The name and ARN of a group.

    - **groupName** *(string) --*

      The group name.

    - **groupArn** *(string) --*

      The group ARN.
    """


_ListThingGroupsForThingPaginateResponseTypeDef = TypedDict(
    "_ListThingGroupsForThingPaginateResponseTypeDef",
    {
        "thingGroups": List[ListThingGroupsForThingPaginateResponsethingGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListThingGroupsForThingPaginateResponseTypeDef(
    _ListThingGroupsForThingPaginateResponseTypeDef
):
    """
    Type definition for `ListThingGroupsForThingPaginate` `Response`

    - **thingGroups** *(list) --*

      The thing groups.

      - *(dict) --*

        The name and ARN of a group.

        - **groupName** *(string) --*

          The group name.

        - **groupArn** *(string) --*

          The group ARN.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListThingGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListThingGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListThingGroupsPaginatePaginationConfigTypeDef(
    _ListThingGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListThingGroupsPaginate` `PaginationConfig`

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


_ListThingGroupsPaginateResponsethingGroupsTypeDef = TypedDict(
    "_ListThingGroupsPaginateResponsethingGroupsTypeDef",
    {"groupName": str, "groupArn": str},
    total=False,
)


class ListThingGroupsPaginateResponsethingGroupsTypeDef(
    _ListThingGroupsPaginateResponsethingGroupsTypeDef
):
    """
    Type definition for `ListThingGroupsPaginateResponse` `thingGroups`

    The name and ARN of a group.

    - **groupName** *(string) --*

      The group name.

    - **groupArn** *(string) --*

      The group ARN.
    """


_ListThingGroupsPaginateResponseTypeDef = TypedDict(
    "_ListThingGroupsPaginateResponseTypeDef",
    {
        "thingGroups": List[ListThingGroupsPaginateResponsethingGroupsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListThingGroupsPaginateResponseTypeDef(_ListThingGroupsPaginateResponseTypeDef):
    """
    Type definition for `ListThingGroupsPaginate` `Response`

    - **thingGroups** *(list) --*

      The thing groups.

      - *(dict) --*

        The name and ARN of a group.

        - **groupName** *(string) --*

          The group name.

        - **groupArn** *(string) --*

          The group ARN.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListThingRegistrationTasksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListThingRegistrationTasksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListThingRegistrationTasksPaginatePaginationConfigTypeDef(
    _ListThingRegistrationTasksPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListThingRegistrationTasksPaginate` `PaginationConfig`

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


_ListThingRegistrationTasksPaginateResponseTypeDef = TypedDict(
    "_ListThingRegistrationTasksPaginateResponseTypeDef",
    {"taskIds": List[str], "NextToken": str},
    total=False,
)


class ListThingRegistrationTasksPaginateResponseTypeDef(
    _ListThingRegistrationTasksPaginateResponseTypeDef
):
    """
    Type definition for `ListThingRegistrationTasksPaginate` `Response`

    - **taskIds** *(list) --*

      A list of bulk thing provisioning task IDs.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListThingTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListThingTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListThingTypesPaginatePaginationConfigTypeDef(
    _ListThingTypesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListThingTypesPaginate` `PaginationConfig`

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


_ListThingTypesPaginateResponsethingTypesthingTypeMetadataTypeDef = TypedDict(
    "_ListThingTypesPaginateResponsethingTypesthingTypeMetadataTypeDef",
    {"deprecated": bool, "deprecationDate": datetime, "creationDate": datetime},
    total=False,
)


class ListThingTypesPaginateResponsethingTypesthingTypeMetadataTypeDef(
    _ListThingTypesPaginateResponsethingTypesthingTypeMetadataTypeDef
):
    """
    Type definition for `ListThingTypesPaginateResponsethingTypes` `thingTypeMetadata`

    The ThingTypeMetadata contains additional information about the thing type including:
    creation date and time, a value indicating whether the thing type is deprecated, and a
    date and time when it was deprecated.

    - **deprecated** *(boolean) --*

      Whether the thing type is deprecated. If **true** , no new things could be associated
      with this type.

    - **deprecationDate** *(datetime) --*

      The date and time when the thing type was deprecated.

    - **creationDate** *(datetime) --*

      The date and time when the thing type was created.
    """


_ListThingTypesPaginateResponsethingTypesthingTypePropertiesTypeDef = TypedDict(
    "_ListThingTypesPaginateResponsethingTypesthingTypePropertiesTypeDef",
    {"thingTypeDescription": str, "searchableAttributes": List[str]},
    total=False,
)


class ListThingTypesPaginateResponsethingTypesthingTypePropertiesTypeDef(
    _ListThingTypesPaginateResponsethingTypesthingTypePropertiesTypeDef
):
    """
    Type definition for `ListThingTypesPaginateResponsethingTypes` `thingTypeProperties`

    The ThingTypeProperties for the thing type.

    - **thingTypeDescription** *(string) --*

      The description of the thing type.

    - **searchableAttributes** *(list) --*

      A list of searchable thing attribute names.

      - *(string) --*
    """


_ListThingTypesPaginateResponsethingTypesTypeDef = TypedDict(
    "_ListThingTypesPaginateResponsethingTypesTypeDef",
    {
        "thingTypeName": str,
        "thingTypeArn": str,
        "thingTypeProperties": ListThingTypesPaginateResponsethingTypesthingTypePropertiesTypeDef,
        "thingTypeMetadata": ListThingTypesPaginateResponsethingTypesthingTypeMetadataTypeDef,
    },
    total=False,
)


class ListThingTypesPaginateResponsethingTypesTypeDef(
    _ListThingTypesPaginateResponsethingTypesTypeDef
):
    """
    Type definition for `ListThingTypesPaginateResponse` `thingTypes`

    The definition of the thing type, including thing type name and description.

    - **thingTypeName** *(string) --*

      The name of the thing type.

    - **thingTypeArn** *(string) --*

      The thing type ARN.

    - **thingTypeProperties** *(dict) --*

      The ThingTypeProperties for the thing type.

      - **thingTypeDescription** *(string) --*

        The description of the thing type.

      - **searchableAttributes** *(list) --*

        A list of searchable thing attribute names.

        - *(string) --*

    - **thingTypeMetadata** *(dict) --*

      The ThingTypeMetadata contains additional information about the thing type including:
      creation date and time, a value indicating whether the thing type is deprecated, and a
      date and time when it was deprecated.

      - **deprecated** *(boolean) --*

        Whether the thing type is deprecated. If **true** , no new things could be associated
        with this type.

      - **deprecationDate** *(datetime) --*

        The date and time when the thing type was deprecated.

      - **creationDate** *(datetime) --*

        The date and time when the thing type was created.
    """


_ListThingTypesPaginateResponseTypeDef = TypedDict(
    "_ListThingTypesPaginateResponseTypeDef",
    {
        "thingTypes": List[ListThingTypesPaginateResponsethingTypesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListThingTypesPaginateResponseTypeDef(_ListThingTypesPaginateResponseTypeDef):
    """
    Type definition for `ListThingTypesPaginate` `Response`

    The output for the ListThingTypes operation.

    - **thingTypes** *(list) --*

      The thing types.

      - *(dict) --*

        The definition of the thing type, including thing type name and description.

        - **thingTypeName** *(string) --*

          The name of the thing type.

        - **thingTypeArn** *(string) --*

          The thing type ARN.

        - **thingTypeProperties** *(dict) --*

          The ThingTypeProperties for the thing type.

          - **thingTypeDescription** *(string) --*

            The description of the thing type.

          - **searchableAttributes** *(list) --*

            A list of searchable thing attribute names.

            - *(string) --*

        - **thingTypeMetadata** *(dict) --*

          The ThingTypeMetadata contains additional information about the thing type including:
          creation date and time, a value indicating whether the thing type is deprecated, and a
          date and time when it was deprecated.

          - **deprecated** *(boolean) --*

            Whether the thing type is deprecated. If **true** , no new things could be associated
            with this type.

          - **deprecationDate** *(datetime) --*

            The date and time when the thing type was deprecated.

          - **creationDate** *(datetime) --*

            The date and time when the thing type was created.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListThingsInBillingGroupPaginatePaginationConfigTypeDef = TypedDict(
    "_ListThingsInBillingGroupPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListThingsInBillingGroupPaginatePaginationConfigTypeDef(
    _ListThingsInBillingGroupPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListThingsInBillingGroupPaginate` `PaginationConfig`

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


_ListThingsInBillingGroupPaginateResponseTypeDef = TypedDict(
    "_ListThingsInBillingGroupPaginateResponseTypeDef",
    {"things": List[str], "NextToken": str},
    total=False,
)


class ListThingsInBillingGroupPaginateResponseTypeDef(
    _ListThingsInBillingGroupPaginateResponseTypeDef
):
    """
    Type definition for `ListThingsInBillingGroupPaginate` `Response`

    - **things** *(list) --*

      A list of things in the billing group.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListThingsInThingGroupPaginatePaginationConfigTypeDef = TypedDict(
    "_ListThingsInThingGroupPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListThingsInThingGroupPaginatePaginationConfigTypeDef(
    _ListThingsInThingGroupPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListThingsInThingGroupPaginate` `PaginationConfig`

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


_ListThingsInThingGroupPaginateResponseTypeDef = TypedDict(
    "_ListThingsInThingGroupPaginateResponseTypeDef",
    {"things": List[str], "NextToken": str},
    total=False,
)


class ListThingsInThingGroupPaginateResponseTypeDef(
    _ListThingsInThingGroupPaginateResponseTypeDef
):
    """
    Type definition for `ListThingsInThingGroupPaginate` `Response`

    - **things** *(list) --*

      The things in the specified thing group.

      - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListThingsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListThingsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListThingsPaginatePaginationConfigTypeDef(
    _ListThingsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListThingsPaginate` `PaginationConfig`

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


_ListThingsPaginateResponsethingsTypeDef = TypedDict(
    "_ListThingsPaginateResponsethingsTypeDef",
    {
        "thingName": str,
        "thingTypeName": str,
        "thingArn": str,
        "attributes": Dict[str, str],
        "version": int,
    },
    total=False,
)


class ListThingsPaginateResponsethingsTypeDef(_ListThingsPaginateResponsethingsTypeDef):
    """
    Type definition for `ListThingsPaginateResponse` `things`

    The properties of the thing, including thing name, thing type name, and a list of thing
    attributes.

    - **thingName** *(string) --*

      The name of the thing.

    - **thingTypeName** *(string) --*

      The name of the thing type, if the thing has been associated with a type.

    - **thingArn** *(string) --*

      The thing ARN.

    - **attributes** *(dict) --*

      A list of thing attributes which are name-value pairs.

      - *(string) --*

        - *(string) --*

    - **version** *(integer) --*

      The version of the thing record in the registry.
    """


_ListThingsPaginateResponseTypeDef = TypedDict(
    "_ListThingsPaginateResponseTypeDef",
    {"things": List[ListThingsPaginateResponsethingsTypeDef], "NextToken": str},
    total=False,
)


class ListThingsPaginateResponseTypeDef(_ListThingsPaginateResponseTypeDef):
    """
    Type definition for `ListThingsPaginate` `Response`

    The output from the ListThings operation.

    - **things** *(list) --*

      The things.

      - *(dict) --*

        The properties of the thing, including thing name, thing type name, and a list of thing
        attributes.

        - **thingName** *(string) --*

          The name of the thing.

        - **thingTypeName** *(string) --*

          The name of the thing type, if the thing has been associated with a type.

        - **thingArn** *(string) --*

          The thing ARN.

        - **attributes** *(dict) --*

          A list of thing attributes which are name-value pairs.

          - *(string) --*

            - *(string) --*

        - **version** *(integer) --*

          The version of the thing record in the registry.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListTopicRulesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListTopicRulesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListTopicRulesPaginatePaginationConfigTypeDef(
    _ListTopicRulesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListTopicRulesPaginate` `PaginationConfig`

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


_ListTopicRulesPaginateResponserulesTypeDef = TypedDict(
    "_ListTopicRulesPaginateResponserulesTypeDef",
    {
        "ruleArn": str,
        "ruleName": str,
        "topicPattern": str,
        "createdAt": datetime,
        "ruleDisabled": bool,
    },
    total=False,
)


class ListTopicRulesPaginateResponserulesTypeDef(
    _ListTopicRulesPaginateResponserulesTypeDef
):
    """
    Type definition for `ListTopicRulesPaginateResponse` `rules`

    Describes a rule.

    - **ruleArn** *(string) --*

      The rule ARN.

    - **ruleName** *(string) --*

      The name of the rule.

    - **topicPattern** *(string) --*

      The pattern for the topic names that apply.

    - **createdAt** *(datetime) --*

      The date and time the rule was created.

    - **ruleDisabled** *(boolean) --*

      Specifies whether the rule is disabled.
    """


_ListTopicRulesPaginateResponseTypeDef = TypedDict(
    "_ListTopicRulesPaginateResponseTypeDef",
    {"rules": List[ListTopicRulesPaginateResponserulesTypeDef], "NextToken": str},
    total=False,
)


class ListTopicRulesPaginateResponseTypeDef(_ListTopicRulesPaginateResponseTypeDef):
    """
    Type definition for `ListTopicRulesPaginate` `Response`

    The output from the ListTopicRules operation.

    - **rules** *(list) --*

      The rules.

      - *(dict) --*

        Describes a rule.

        - **ruleArn** *(string) --*

          The rule ARN.

        - **ruleName** *(string) --*

          The name of the rule.

        - **topicPattern** *(string) --*

          The pattern for the topic names that apply.

        - **createdAt** *(datetime) --*

          The date and time the rule was created.

        - **ruleDisabled** *(boolean) --*

          Specifies whether the rule is disabled.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListV2LoggingLevelsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListV2LoggingLevelsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListV2LoggingLevelsPaginatePaginationConfigTypeDef(
    _ListV2LoggingLevelsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListV2LoggingLevelsPaginate` `PaginationConfig`

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


_ListV2LoggingLevelsPaginateResponselogTargetConfigurationslogTargetTypeDef = TypedDict(
    "_ListV2LoggingLevelsPaginateResponselogTargetConfigurationslogTargetTypeDef",
    {"targetType": str, "targetName": str},
    total=False,
)


class ListV2LoggingLevelsPaginateResponselogTargetConfigurationslogTargetTypeDef(
    _ListV2LoggingLevelsPaginateResponselogTargetConfigurationslogTargetTypeDef
):
    """
    Type definition for `ListV2LoggingLevelsPaginateResponselogTargetConfigurations` `logTarget`

    A log target

    - **targetType** *(string) --*

      The target type.

    - **targetName** *(string) --*

      The target name.
    """


_ListV2LoggingLevelsPaginateResponselogTargetConfigurationsTypeDef = TypedDict(
    "_ListV2LoggingLevelsPaginateResponselogTargetConfigurationsTypeDef",
    {
        "logTarget": ListV2LoggingLevelsPaginateResponselogTargetConfigurationslogTargetTypeDef,
        "logLevel": str,
    },
    total=False,
)


class ListV2LoggingLevelsPaginateResponselogTargetConfigurationsTypeDef(
    _ListV2LoggingLevelsPaginateResponselogTargetConfigurationsTypeDef
):
    """
    Type definition for `ListV2LoggingLevelsPaginateResponse` `logTargetConfigurations`

    The target configuration.

    - **logTarget** *(dict) --*

      A log target

      - **targetType** *(string) --*

        The target type.

      - **targetName** *(string) --*

        The target name.

    - **logLevel** *(string) --*

      The logging level.
    """


_ListV2LoggingLevelsPaginateResponseTypeDef = TypedDict(
    "_ListV2LoggingLevelsPaginateResponseTypeDef",
    {
        "logTargetConfigurations": List[
            ListV2LoggingLevelsPaginateResponselogTargetConfigurationsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListV2LoggingLevelsPaginateResponseTypeDef(
    _ListV2LoggingLevelsPaginateResponseTypeDef
):
    """
    Type definition for `ListV2LoggingLevelsPaginate` `Response`

    - **logTargetConfigurations** *(list) --*

      The logging configuration for a target.

      - *(dict) --*

        The target configuration.

        - **logTarget** *(dict) --*

          A log target

          - **targetType** *(string) --*

            The target type.

          - **targetName** *(string) --*

            The target name.

        - **logLevel** *(string) --*

          The logging level.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListViolationEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListViolationEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListViolationEventsPaginatePaginationConfigTypeDef(
    _ListViolationEventsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListViolationEventsPaginate` `PaginationConfig`

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


_ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef = TypedDict(
    "_ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef",
    {"statistic": str},
    total=False,
)


class ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef(
    _ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef
):
    """
    Type definition for `ListViolationEventsPaginateResponseviolationEventsbehaviorcriteria` `statisticalThreshold`

    A statistical ranking (percentile) which indicates a threshold value by which a
    behavior is determined to be in compliance or in violation of the behavior.

    - **statistic** *(string) --*

      The percentile which resolves to a threshold value by which compliance with a
      behavior is determined. Metrics are collected over the specified period
      (``durationSeconds`` ) from all reporting devices in your account and statistical
      ranks are calculated. Then, the measurements from a device are collected over the
      same period. If the accumulated measurements from the device fall above or below
      (``comparisonOperator`` ) the value associated with the percentile specified, then
      the device is considered to be in compliance with the behavior, otherwise a
      violation occurs.
    """


_ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriavalueTypeDef = TypedDict(
    "_ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriavalueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriavalueTypeDef(
    _ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriavalueTypeDef
):
    """
    Type definition for `ListViolationEventsPaginateResponseviolationEventsbehaviorcriteria` `value`

    The value to be compared with the ``metric`` .

    - **count** *(integer) --*

      If the ``comparisonOperator`` calls for a numeric value, use this to specify that
      numeric value to be compared with the ``metric`` .

    - **cidrs** *(list) --*

      If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
      set to be compared with the ``metric`` .

      - *(string) --*

    - **ports** *(list) --*

      If the ``comparisonOperator`` calls for a set of ports, use this to specify that
      set to be compared with the ``metric`` .

      - *(integer) --*
    """


_ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriaTypeDef = TypedDict(
    "_ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriaTypeDef",
    {
        "comparisonOperator": str,
        "value": ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriavalueTypeDef,
        "durationSeconds": int,
        "consecutiveDatapointsToAlarm": int,
        "consecutiveDatapointsToClear": int,
        "statisticalThreshold": ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriastatisticalThresholdTypeDef,
    },
    total=False,
)


class ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriaTypeDef(
    _ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriaTypeDef
):
    """
    Type definition for `ListViolationEventsPaginateResponseviolationEventsbehavior` `criteria`

    The criteria that determine if a device is behaving normally in regard to the
    ``metric`` .

    - **comparisonOperator** *(string) --*

      The operator that relates the thing measured (``metric`` ) to the criteria
      (containing a ``value`` or ``statisticalThreshold`` ).

    - **value** *(dict) --*

      The value to be compared with the ``metric`` .

      - **count** *(integer) --*

        If the ``comparisonOperator`` calls for a numeric value, use this to specify that
        numeric value to be compared with the ``metric`` .

      - **cidrs** *(list) --*

        If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
        set to be compared with the ``metric`` .

        - *(string) --*

      - **ports** *(list) --*

        If the ``comparisonOperator`` calls for a set of ports, use this to specify that
        set to be compared with the ``metric`` .

        - *(integer) --*

    - **durationSeconds** *(integer) --*

      Use this to specify the time duration over which the behavior is evaluated, for those
      criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
      ``statisticalThreshhold`` metric comparison, measurements from all devices are
      accumulated over this time duration before being used to calculate percentiles, and
      later, measurements from an individual device are also accumulated over this time
      duration before being given a percentile rank.

    - **consecutiveDatapointsToAlarm** *(integer) --*

      If a device is in violation of the behavior for the specified number of consecutive
      datapoints, an alarm occurs. If not specified, the default is 1.

    - **consecutiveDatapointsToClear** *(integer) --*

      If an alarm has occurred and the offending device is no longer in violation of the
      behavior for the specified number of consecutive datapoints, the alarm is cleared. If
      not specified, the default is 1.

    - **statisticalThreshold** *(dict) --*

      A statistical ranking (percentile) which indicates a threshold value by which a
      behavior is determined to be in compliance or in violation of the behavior.

      - **statistic** *(string) --*

        The percentile which resolves to a threshold value by which compliance with a
        behavior is determined. Metrics are collected over the specified period
        (``durationSeconds`` ) from all reporting devices in your account and statistical
        ranks are calculated. Then, the measurements from a device are collected over the
        same period. If the accumulated measurements from the device fall above or below
        (``comparisonOperator`` ) the value associated with the percentile specified, then
        the device is considered to be in compliance with the behavior, otherwise a
        violation occurs.
    """


_ListViolationEventsPaginateResponseviolationEventsbehaviorTypeDef = TypedDict(
    "_ListViolationEventsPaginateResponseviolationEventsbehaviorTypeDef",
    {
        "name": str,
        "metric": str,
        "criteria": ListViolationEventsPaginateResponseviolationEventsbehaviorcriteriaTypeDef,
    },
    total=False,
)


class ListViolationEventsPaginateResponseviolationEventsbehaviorTypeDef(
    _ListViolationEventsPaginateResponseviolationEventsbehaviorTypeDef
):
    """
    Type definition for `ListViolationEventsPaginateResponseviolationEvents` `behavior`

    The behavior which was violated.

    - **name** *(string) --*

      The name you have given to the behavior.

    - **metric** *(string) --*

      What is measured by the behavior.

    - **criteria** *(dict) --*

      The criteria that determine if a device is behaving normally in regard to the
      ``metric`` .

      - **comparisonOperator** *(string) --*

        The operator that relates the thing measured (``metric`` ) to the criteria
        (containing a ``value`` or ``statisticalThreshold`` ).

      - **value** *(dict) --*

        The value to be compared with the ``metric`` .

        - **count** *(integer) --*

          If the ``comparisonOperator`` calls for a numeric value, use this to specify that
          numeric value to be compared with the ``metric`` .

        - **cidrs** *(list) --*

          If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
          set to be compared with the ``metric`` .

          - *(string) --*

        - **ports** *(list) --*

          If the ``comparisonOperator`` calls for a set of ports, use this to specify that
          set to be compared with the ``metric`` .

          - *(integer) --*

      - **durationSeconds** *(integer) --*

        Use this to specify the time duration over which the behavior is evaluated, for those
        criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
        ``statisticalThreshhold`` metric comparison, measurements from all devices are
        accumulated over this time duration before being used to calculate percentiles, and
        later, measurements from an individual device are also accumulated over this time
        duration before being given a percentile rank.

      - **consecutiveDatapointsToAlarm** *(integer) --*

        If a device is in violation of the behavior for the specified number of consecutive
        datapoints, an alarm occurs. If not specified, the default is 1.

      - **consecutiveDatapointsToClear** *(integer) --*

        If an alarm has occurred and the offending device is no longer in violation of the
        behavior for the specified number of consecutive datapoints, the alarm is cleared. If
        not specified, the default is 1.

      - **statisticalThreshold** *(dict) --*

        A statistical ranking (percentile) which indicates a threshold value by which a
        behavior is determined to be in compliance or in violation of the behavior.

        - **statistic** *(string) --*

          The percentile which resolves to a threshold value by which compliance with a
          behavior is determined. Metrics are collected over the specified period
          (``durationSeconds`` ) from all reporting devices in your account and statistical
          ranks are calculated. Then, the measurements from a device are collected over the
          same period. If the accumulated measurements from the device fall above or below
          (``comparisonOperator`` ) the value associated with the percentile specified, then
          the device is considered to be in compliance with the behavior, otherwise a
          violation occurs.
    """


_ListViolationEventsPaginateResponseviolationEventsmetricValueTypeDef = TypedDict(
    "_ListViolationEventsPaginateResponseviolationEventsmetricValueTypeDef",
    {"count": int, "cidrs": List[str], "ports": List[int]},
    total=False,
)


class ListViolationEventsPaginateResponseviolationEventsmetricValueTypeDef(
    _ListViolationEventsPaginateResponseviolationEventsmetricValueTypeDef
):
    """
    Type definition for `ListViolationEventsPaginateResponseviolationEvents` `metricValue`

    The value of the metric (the measurement).

    - **count** *(integer) --*

      If the ``comparisonOperator`` calls for a numeric value, use this to specify that
      numeric value to be compared with the ``metric`` .

    - **cidrs** *(list) --*

      If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
      be compared with the ``metric`` .

      - *(string) --*

    - **ports** *(list) --*

      If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
      be compared with the ``metric`` .

      - *(integer) --*
    """


_ListViolationEventsPaginateResponseviolationEventsTypeDef = TypedDict(
    "_ListViolationEventsPaginateResponseviolationEventsTypeDef",
    {
        "violationId": str,
        "thingName": str,
        "securityProfileName": str,
        "behavior": ListViolationEventsPaginateResponseviolationEventsbehaviorTypeDef,
        "metricValue": ListViolationEventsPaginateResponseviolationEventsmetricValueTypeDef,
        "violationEventType": str,
        "violationEventTime": datetime,
    },
    total=False,
)


class ListViolationEventsPaginateResponseviolationEventsTypeDef(
    _ListViolationEventsPaginateResponseviolationEventsTypeDef
):
    """
    Type definition for `ListViolationEventsPaginateResponse` `violationEvents`

    Information about a Device Defender security profile behavior violation.

    - **violationId** *(string) --*

      The ID of the violation event.

    - **thingName** *(string) --*

      The name of the thing responsible for the violation event.

    - **securityProfileName** *(string) --*

      The name of the security profile whose behavior was violated.

    - **behavior** *(dict) --*

      The behavior which was violated.

      - **name** *(string) --*

        The name you have given to the behavior.

      - **metric** *(string) --*

        What is measured by the behavior.

      - **criteria** *(dict) --*

        The criteria that determine if a device is behaving normally in regard to the
        ``metric`` .

        - **comparisonOperator** *(string) --*

          The operator that relates the thing measured (``metric`` ) to the criteria
          (containing a ``value`` or ``statisticalThreshold`` ).

        - **value** *(dict) --*

          The value to be compared with the ``metric`` .

          - **count** *(integer) --*

            If the ``comparisonOperator`` calls for a numeric value, use this to specify that
            numeric value to be compared with the ``metric`` .

          - **cidrs** *(list) --*

            If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
            set to be compared with the ``metric`` .

            - *(string) --*

          - **ports** *(list) --*

            If the ``comparisonOperator`` calls for a set of ports, use this to specify that
            set to be compared with the ``metric`` .

            - *(integer) --*

        - **durationSeconds** *(integer) --*

          Use this to specify the time duration over which the behavior is evaluated, for those
          criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
          ``statisticalThreshhold`` metric comparison, measurements from all devices are
          accumulated over this time duration before being used to calculate percentiles, and
          later, measurements from an individual device are also accumulated over this time
          duration before being given a percentile rank.

        - **consecutiveDatapointsToAlarm** *(integer) --*

          If a device is in violation of the behavior for the specified number of consecutive
          datapoints, an alarm occurs. If not specified, the default is 1.

        - **consecutiveDatapointsToClear** *(integer) --*

          If an alarm has occurred and the offending device is no longer in violation of the
          behavior for the specified number of consecutive datapoints, the alarm is cleared. If
          not specified, the default is 1.

        - **statisticalThreshold** *(dict) --*

          A statistical ranking (percentile) which indicates a threshold value by which a
          behavior is determined to be in compliance or in violation of the behavior.

          - **statistic** *(string) --*

            The percentile which resolves to a threshold value by which compliance with a
            behavior is determined. Metrics are collected over the specified period
            (``durationSeconds`` ) from all reporting devices in your account and statistical
            ranks are calculated. Then, the measurements from a device are collected over the
            same period. If the accumulated measurements from the device fall above or below
            (``comparisonOperator`` ) the value associated with the percentile specified, then
            the device is considered to be in compliance with the behavior, otherwise a
            violation occurs.

    - **metricValue** *(dict) --*

      The value of the metric (the measurement).

      - **count** *(integer) --*

        If the ``comparisonOperator`` calls for a numeric value, use this to specify that
        numeric value to be compared with the ``metric`` .

      - **cidrs** *(list) --*

        If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
        be compared with the ``metric`` .

        - *(string) --*

      - **ports** *(list) --*

        If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
        be compared with the ``metric`` .

        - *(integer) --*

    - **violationEventType** *(string) --*

      The type of violation event.

    - **violationEventTime** *(datetime) --*

      The time the violation event occurred.
    """


_ListViolationEventsPaginateResponseTypeDef = TypedDict(
    "_ListViolationEventsPaginateResponseTypeDef",
    {
        "violationEvents": List[
            ListViolationEventsPaginateResponseviolationEventsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ListViolationEventsPaginateResponseTypeDef(
    _ListViolationEventsPaginateResponseTypeDef
):
    """
    Type definition for `ListViolationEventsPaginate` `Response`

    - **violationEvents** *(list) --*

      The security profile violation alerts issued for this account during the given time period,
      potentially filtered by security profile, behavior violated, or thing (device) violating.

      - *(dict) --*

        Information about a Device Defender security profile behavior violation.

        - **violationId** *(string) --*

          The ID of the violation event.

        - **thingName** *(string) --*

          The name of the thing responsible for the violation event.

        - **securityProfileName** *(string) --*

          The name of the security profile whose behavior was violated.

        - **behavior** *(dict) --*

          The behavior which was violated.

          - **name** *(string) --*

            The name you have given to the behavior.

          - **metric** *(string) --*

            What is measured by the behavior.

          - **criteria** *(dict) --*

            The criteria that determine if a device is behaving normally in regard to the
            ``metric`` .

            - **comparisonOperator** *(string) --*

              The operator that relates the thing measured (``metric`` ) to the criteria
              (containing a ``value`` or ``statisticalThreshold`` ).

            - **value** *(dict) --*

              The value to be compared with the ``metric`` .

              - **count** *(integer) --*

                If the ``comparisonOperator`` calls for a numeric value, use this to specify that
                numeric value to be compared with the ``metric`` .

              - **cidrs** *(list) --*

                If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that
                set to be compared with the ``metric`` .

                - *(string) --*

              - **ports** *(list) --*

                If the ``comparisonOperator`` calls for a set of ports, use this to specify that
                set to be compared with the ``metric`` .

                - *(integer) --*

            - **durationSeconds** *(integer) --*

              Use this to specify the time duration over which the behavior is evaluated, for those
              criteria which have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a
              ``statisticalThreshhold`` metric comparison, measurements from all devices are
              accumulated over this time duration before being used to calculate percentiles, and
              later, measurements from an individual device are also accumulated over this time
              duration before being given a percentile rank.

            - **consecutiveDatapointsToAlarm** *(integer) --*

              If a device is in violation of the behavior for the specified number of consecutive
              datapoints, an alarm occurs. If not specified, the default is 1.

            - **consecutiveDatapointsToClear** *(integer) --*

              If an alarm has occurred and the offending device is no longer in violation of the
              behavior for the specified number of consecutive datapoints, the alarm is cleared. If
              not specified, the default is 1.

            - **statisticalThreshold** *(dict) --*

              A statistical ranking (percentile) which indicates a threshold value by which a
              behavior is determined to be in compliance or in violation of the behavior.

              - **statistic** *(string) --*

                The percentile which resolves to a threshold value by which compliance with a
                behavior is determined. Metrics are collected over the specified period
                (``durationSeconds`` ) from all reporting devices in your account and statistical
                ranks are calculated. Then, the measurements from a device are collected over the
                same period. If the accumulated measurements from the device fall above or below
                (``comparisonOperator`` ) the value associated with the percentile specified, then
                the device is considered to be in compliance with the behavior, otherwise a
                violation occurs.

        - **metricValue** *(dict) --*

          The value of the metric (the measurement).

          - **count** *(integer) --*

            If the ``comparisonOperator`` calls for a numeric value, use this to specify that
            numeric value to be compared with the ``metric`` .

          - **cidrs** *(list) --*

            If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to
            be compared with the ``metric`` .

            - *(string) --*

          - **ports** *(list) --*

            If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to
            be compared with the ``metric`` .

            - *(integer) --*

        - **violationEventType** *(string) --*

          The type of violation event.

        - **violationEventTime** *(datetime) --*

          The time the violation event occurred.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """
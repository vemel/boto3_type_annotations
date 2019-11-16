"Main interface for mediaconnect type defs"
from __future__ import annotations

from typing import Any, Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientAddFlowOutputsOutputsTypeDef",
    "ClientAddFlowOutputsResponseOutputsTypeDef",
    "ClientAddFlowOutputsResponseTypeDef",
    "ClientCreateFlowEntitlementsTypeDef",
    "ClientCreateFlowOutputsTypeDef",
    "ClientCreateFlowResponseFlowEntitlementsTypeDef",
    "ClientCreateFlowResponseFlowOutputsTypeDef",
    "ClientCreateFlowResponseFlowSourceTypeDef",
    "ClientCreateFlowResponseFlowTypeDef",
    "ClientCreateFlowResponseTypeDef",
    "ClientCreateFlowSourceTypeDef",
    "ClientDeleteFlowResponseTypeDef",
    "ClientDescribeFlowResponseFlowEntitlementsTypeDef",
    "ClientDescribeFlowResponseFlowOutputsTypeDef",
    "ClientDescribeFlowResponseFlowSourceTypeDef",
    "ClientDescribeFlowResponseFlowTypeDef",
    "ClientDescribeFlowResponseMessagesTypeDef",
    "ClientDescribeFlowResponseTypeDef",
    "ClientGrantFlowEntitlementsEntitlementsTypeDef",
    "ClientGrantFlowEntitlementsResponseEntitlementsTypeDef",
    "ClientGrantFlowEntitlementsResponseTypeDef",
    "ClientListEntitlementsResponseTypeDef",
    "ClientListFlowsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientRemoveFlowOutputResponseTypeDef",
    "ClientRevokeFlowEntitlementResponseTypeDef",
    "ClientStartFlowResponseTypeDef",
    "ClientStopFlowResponseTypeDef",
    "ClientUpdateFlowEntitlementResponseEntitlementTypeDef",
    "ClientUpdateFlowEntitlementResponseTypeDef",
    "ClientUpdateFlowOutputResponseOutputTypeDef",
    "ClientUpdateFlowOutputResponseTypeDef",
    "ClientUpdateFlowSourceDecryptionTypeDef",
    "ClientUpdateFlowSourceResponseSourceTypeDef",
    "ClientUpdateFlowSourceResponseTypeDef",
    "ListEntitlementsPaginatePaginationConfigTypeDef",
    "ListEntitlementsPaginateResponseTypeDef",
    "ListFlowsPaginatePaginationConfigTypeDef",
    "ListFlowsPaginateResponseTypeDef",
)


_RequiredClientAddFlowOutputsOutputsTypeDef = TypedDict(
    "_RequiredClientAddFlowOutputsOutputsTypeDef", {"Protocol": str}
)
_OptionalClientAddFlowOutputsOutputsTypeDef = TypedDict(
    "_OptionalClientAddFlowOutputsOutputsTypeDef",
    {
        "CidrAllowList": List[Any],
        "Description": str,
        "Destination": str,
        "Encryption": Dict[str, Any],
        "MaxLatency": int,
        "Name": str,
        "Port": int,
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)


class ClientAddFlowOutputsOutputsTypeDef(
    _RequiredClientAddFlowOutputsOutputsTypeDef,
    _OptionalClientAddFlowOutputsOutputsTypeDef,
):
    """
    Type definition for `ClientAddFlowOutputs` `Outputs`

    - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to initiate
    output requests to this flow. These IP addresses should be in the form of a Classless
    Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

      - *(string) --*

    - **Description** *(string) --* A description of the output. This description appears only on
    the AWS Elemental MediaConnect console and will not be seen by the end user.

    - **Destination** *(string) --* The IP address from which video will be sent to output
    destinations.

    - **Encryption** *(dict) --* The type of key used for the encryption. If no keyType is
    provided, the service will use the default setting (static-key).

      - **Algorithm** *(string) --* **[REQUIRED]** The type of algorithm that is used for the
      encryption (such as aes128, aes192, or aes256).

      - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented by
      a 32-character string, to be used with the key for encrypting content. This parameter is not
      valid for static key encryption.

      - **DeviceId** *(string) --* The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.

      - **KeyType** *(string) --* The type of key that is used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).

      - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created in.
      This parameter is required for SPEKE encryption and is not valid for static key encryption.

      - **ResourceId** *(string) --* An identifier for the content. The service sends this value to
      the key server to identify the current endpoint. The resource ID is also known as the content
      ID. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

      - **RoleArn** *(string) --* **[REQUIRED]** The ARN of the role that you created during setup
      (when you set up AWS Elemental MediaConnect as a trusted entity).

      - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets Manager
      to store the encryption key. This parameter is required for static key encryption and is not
      valid for SPEKE encryption.

      - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to your
      key server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

    - **MaxLatency** *(integer) --* The maximum latency in milliseconds for Zixi-based streams.

    - **Name** *(string) --* The name of the output. This value must be unique within the current
    flow.

    - **Port** *(integer) --* The port to use when content is distributed to this output.

    - **Protocol** *(string) --* **[REQUIRED]** The protocol to use for the output.

    - **RemoteId** *(string) --* The remote ID for the Zixi-pull output stream.

    - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST, RTP, and
    RTP-FEC streams.

    - **StreamId** *(string) --* The stream ID that you want to use for this transport. This
    parameter applies only to Zixi-based streams.
    """


_ClientAddFlowOutputsResponseOutputsTypeDef = TypedDict(
    "_ClientAddFlowOutputsResponseOutputsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Destination": str,
        "Encryption": Dict[str, Any],
        "EntitlementArn": str,
        "MediaLiveInputArn": str,
        "Name": str,
        "OutputArn": str,
        "Port": int,
        "Transport": Dict[str, Any],
    },
    total=False,
)


class ClientAddFlowOutputsResponseOutputsTypeDef(
    _ClientAddFlowOutputsResponseOutputsTypeDef
):
    """
    Type definition for `ClientAddFlowOutputsResponse` `Outputs`

    - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
    transfer cost to be billed to the subscriber.

    - **Description** *(string) --* A description of the output.

    - **Destination** *(string) --* The address where you want to send the output.

    - **Encryption** *(dict) --* The type of key used for the encryption. If no keyType is
    provided, the service will use the default setting (static-key).

      - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
      as aes128, aes192, or aes256).

      - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
      by a 32-character string, to be used with the key for encrypting content. This parameter
      is not valid for static key encryption.

      - **DeviceId** *(string) --* The value of one of the devices that you configured with
      your digital rights management (DRM) platform key provider. This parameter is required
      for SPEKE encryption and is not valid for static key encryption.

      - **KeyType** *(string) --* The type of key that is used for the encryption. If no
      keyType is provided, the service will use the default setting (static-key).

      - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
      in. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

      - **ResourceId** *(string) --* An identifier for the content. The service sends this
      value to the key server to identify the current endpoint. The resource ID is also known
      as the content ID. This parameter is required for SPEKE encryption and is not valid for
      static key encryption.

      - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
      set up AWS Elemental MediaConnect as a trusted entity).

      - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
      Manager to store the encryption key. This parameter is required for static key encryption
      and is not valid for SPEKE encryption.

      - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
      your key server. This parameter is required for SPEKE encryption and is not valid for
      static key encryption.

    - **EntitlementArn** *(string) --* The ARN of the entitlement on the originator''s flow.
    This value is relevant only on entitled flows.

    - **MediaLiveInputArn** *(string) --* The input ARN of the AWS Elemental MediaLive channel.
    This parameter is relevant only for outputs that were added by creating a MediaLive input.

    - **Name** *(string) --* The name of the output. This value must be unique within the
    current flow.

    - **OutputArn** *(string) --* The ARN of the output.

    - **Port** *(integer) --* The port to use when content is distributed to this output.

    - **Transport** *(dict) --* Attributes related to the transport stream that are used in the
    output.

      - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
      initiate output requests to this flow. These IP addresses should be in the form of a
      Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

        - *(string) --*

      - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
      streams.

      - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter
      applies only to RIST-based and Zixi-based streams.

      - **Protocol** *(string) --* The protocol that is used by the source or output.

      - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

      - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST,
      RTP, and RTP-FEC streams.

      - **StreamId** *(string) --* The stream ID that you want to use for this transport. This
      parameter applies only to Zixi-based streams.
    """


_ClientAddFlowOutputsResponseTypeDef = TypedDict(
    "_ClientAddFlowOutputsResponseTypeDef",
    {"FlowArn": str, "Outputs": List[ClientAddFlowOutputsResponseOutputsTypeDef]},
    total=False,
)


class ClientAddFlowOutputsResponseTypeDef(_ClientAddFlowOutputsResponseTypeDef):
    """
    Type definition for `ClientAddFlowOutputs` `Response`

    - **FlowArn** *(string) --* The ARN of the flow that these outputs were added to.

    - **Outputs** *(list) --* The details of the newly added outputs.

      - *(dict) --* The settings for an output.

        - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
        transfer cost to be billed to the subscriber.

        - **Description** *(string) --* A description of the output.

        - **Destination** *(string) --* The address where you want to send the output.

        - **Encryption** *(dict) --* The type of key used for the encryption. If no keyType is
        provided, the service will use the default setting (static-key).

          - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
          as aes128, aes192, or aes256).

          - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
          by a 32-character string, to be used with the key for encrypting content. This parameter
          is not valid for static key encryption.

          - **DeviceId** *(string) --* The value of one of the devices that you configured with
          your digital rights management (DRM) platform key provider. This parameter is required
          for SPEKE encryption and is not valid for static key encryption.

          - **KeyType** *(string) --* The type of key that is used for the encryption. If no
          keyType is provided, the service will use the default setting (static-key).

          - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
          in. This parameter is required for SPEKE encryption and is not valid for static key
          encryption.

          - **ResourceId** *(string) --* An identifier for the content. The service sends this
          value to the key server to identify the current endpoint. The resource ID is also known
          as the content ID. This parameter is required for SPEKE encryption and is not valid for
          static key encryption.

          - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
          set up AWS Elemental MediaConnect as a trusted entity).

          - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
          Manager to store the encryption key. This parameter is required for static key encryption
          and is not valid for SPEKE encryption.

          - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
          your key server. This parameter is required for SPEKE encryption and is not valid for
          static key encryption.

        - **EntitlementArn** *(string) --* The ARN of the entitlement on the originator''s flow.
        This value is relevant only on entitled flows.

        - **MediaLiveInputArn** *(string) --* The input ARN of the AWS Elemental MediaLive channel.
        This parameter is relevant only for outputs that were added by creating a MediaLive input.

        - **Name** *(string) --* The name of the output. This value must be unique within the
        current flow.

        - **OutputArn** *(string) --* The ARN of the output.

        - **Port** *(integer) --* The port to use when content is distributed to this output.

        - **Transport** *(dict) --* Attributes related to the transport stream that are used in the
        output.

          - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
          initiate output requests to this flow. These IP addresses should be in the form of a
          Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

            - *(string) --*

          - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
          streams.

          - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter
          applies only to RIST-based and Zixi-based streams.

          - **Protocol** *(string) --* The protocol that is used by the source or output.

          - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

          - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST,
          RTP, and RTP-FEC streams.

          - **StreamId** *(string) --* The stream ID that you want to use for this transport. This
          parameter applies only to Zixi-based streams.
    """


_RequiredClientCreateFlowEntitlementsTypeDef = TypedDict(
    "_RequiredClientCreateFlowEntitlementsTypeDef", {"Subscribers": List[Any]}
)
_OptionalClientCreateFlowEntitlementsTypeDef = TypedDict(
    "_OptionalClientCreateFlowEntitlementsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": Dict[str, Any],
        "Name": str,
    },
    total=False,
)


class ClientCreateFlowEntitlementsTypeDef(
    _RequiredClientCreateFlowEntitlementsTypeDef,
    _OptionalClientCreateFlowEntitlementsTypeDef,
):
    """
    Type definition for `ClientCreateFlow` `Entitlements`

    - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
    transfer cost to be billed to the subscriber.

    - **Description** *(string) --* A description of the entitlement. This description appears only
    on the AWS Elemental MediaConnect console and will not be seen by the subscriber or end user.

    - **Encryption** *(dict) --* The type of encryption that will be used on the output that is
    associated with this entitlement.

      - **Algorithm** *(string) --* **[REQUIRED]** The type of algorithm that is used for the
      encryption (such as aes128, aes192, or aes256).

      - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented by
      a 32-character string, to be used with the key for encrypting content. This parameter is not
      valid for static key encryption.

      - **DeviceId** *(string) --* The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.

      - **KeyType** *(string) --* The type of key that is used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).

      - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created in.
      This parameter is required for SPEKE encryption and is not valid for static key encryption.

      - **ResourceId** *(string) --* An identifier for the content. The service sends this value to
      the key server to identify the current endpoint. The resource ID is also known as the content
      ID. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

      - **RoleArn** *(string) --* **[REQUIRED]** The ARN of the role that you created during setup
      (when you set up AWS Elemental MediaConnect as a trusted entity).

      - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets Manager
      to store the encryption key. This parameter is required for static key encryption and is not
      valid for SPEKE encryption.

      - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to your
      key server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

    - **Name** *(string) --* The name of the entitlement. This value must be unique within the
    current flow.

    - **Subscribers** *(list) --* **[REQUIRED]** The AWS account IDs that you want to share your
    content with. The receiving accounts (subscribers) will be allowed to create their own flows
    using your content as the source.

      - *(string) --*
    """


_RequiredClientCreateFlowOutputsTypeDef = TypedDict(
    "_RequiredClientCreateFlowOutputsTypeDef", {"Protocol": str}
)
_OptionalClientCreateFlowOutputsTypeDef = TypedDict(
    "_OptionalClientCreateFlowOutputsTypeDef",
    {
        "CidrAllowList": List[Any],
        "Description": str,
        "Destination": str,
        "Encryption": Dict[str, Any],
        "MaxLatency": int,
        "Name": str,
        "Port": int,
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)


class ClientCreateFlowOutputsTypeDef(
    _RequiredClientCreateFlowOutputsTypeDef, _OptionalClientCreateFlowOutputsTypeDef
):
    """
    Type definition for `ClientCreateFlow` `Outputs`

    - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to initiate
    output requests to this flow. These IP addresses should be in the form of a Classless
    Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

      - *(string) --*

    - **Description** *(string) --* A description of the output. This description appears only on
    the AWS Elemental MediaConnect console and will not be seen by the end user.

    - **Destination** *(string) --* The IP address from which video will be sent to output
    destinations.

    - **Encryption** *(dict) --* The type of key used for the encryption. If no keyType is
    provided, the service will use the default setting (static-key).

      - **Algorithm** *(string) --* **[REQUIRED]** The type of algorithm that is used for the
      encryption (such as aes128, aes192, or aes256).

      - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented by
      a 32-character string, to be used with the key for encrypting content. This parameter is not
      valid for static key encryption.

      - **DeviceId** *(string) --* The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.

      - **KeyType** *(string) --* The type of key that is used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).

      - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created in.
      This parameter is required for SPEKE encryption and is not valid for static key encryption.

      - **ResourceId** *(string) --* An identifier for the content. The service sends this value to
      the key server to identify the current endpoint. The resource ID is also known as the content
      ID. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

      - **RoleArn** *(string) --* **[REQUIRED]** The ARN of the role that you created during setup
      (when you set up AWS Elemental MediaConnect as a trusted entity).

      - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets Manager
      to store the encryption key. This parameter is required for static key encryption and is not
      valid for SPEKE encryption.

      - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to your
      key server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

    - **MaxLatency** *(integer) --* The maximum latency in milliseconds for Zixi-based streams.

    - **Name** *(string) --* The name of the output. This value must be unique within the current
    flow.

    - **Port** *(integer) --* The port to use when content is distributed to this output.

    - **Protocol** *(string) --* **[REQUIRED]** The protocol to use for the output.

    - **RemoteId** *(string) --* The remote ID for the Zixi-pull output stream.

    - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST, RTP, and
    RTP-FEC streams.

    - **StreamId** *(string) --* The stream ID that you want to use for this transport. This
    parameter applies only to Zixi-based streams.
    """


_ClientCreateFlowResponseFlowEntitlementsTypeDef = TypedDict(
    "_ClientCreateFlowResponseFlowEntitlementsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": Dict[str, Any],
        "EntitlementArn": str,
        "Name": str,
        "Subscribers": List[Any],
    },
    total=False,
)


class ClientCreateFlowResponseFlowEntitlementsTypeDef(
    _ClientCreateFlowResponseFlowEntitlementsTypeDef
):
    """
    Type definition for `ClientCreateFlowResponseFlow` `Entitlements`

    - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
    transfer cost to be billed to the subscriber.

    - **Description** *(string) --* A description of the entitlement.

    - **Encryption** *(dict) --* The type of encryption that will be used on the output that
    is associated with this entitlement.

      - **Algorithm** *(string) --* The type of algorithm that is used for the encryption
      (such as aes128, aes192, or aes256).

      - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
      represented by a 32-character string, to be used with the key for encrypting content.
      This parameter is not valid for static key encryption.

      - **DeviceId** *(string) --* The value of one of the devices that you configured with
      your digital rights management (DRM) platform key provider. This parameter is required
      for SPEKE encryption and is not valid for static key encryption.

      - **KeyType** *(string) --* The type of key that is used for the encryption. If no
      keyType is provided, the service will use the default setting (static-key).

      - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
      created in. This parameter is required for SPEKE encryption and is not valid for static
      key encryption.

      - **ResourceId** *(string) --* An identifier for the content. The service sends this
      value to the key server to identify the current endpoint. The resource ID is also known
      as the content ID. This parameter is required for SPEKE encryption and is not valid for
      static key encryption.

      - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
      set up AWS Elemental MediaConnect as a trusted entity).

      - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
      Manager to store the encryption key. This parameter is required for static key
      encryption and is not valid for SPEKE encryption.

      - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
      your key server. This parameter is required for SPEKE encryption and is not valid for
      static key encryption.

    - **EntitlementArn** *(string) --* The ARN of the entitlement.

    - **Name** *(string) --* The name of the entitlement.

    - **Subscribers** *(list) --* The AWS account IDs that you want to share your content
    with. The receiving accounts (subscribers) will be allowed to create their own flow using
    your content as the source.

      - *(string) --*
    """


_ClientCreateFlowResponseFlowOutputsTypeDef = TypedDict(
    "_ClientCreateFlowResponseFlowOutputsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Destination": str,
        "Encryption": Dict[str, Any],
        "EntitlementArn": str,
        "MediaLiveInputArn": str,
        "Name": str,
        "OutputArn": str,
        "Port": int,
        "Transport": Dict[str, Any],
    },
    total=False,
)


class ClientCreateFlowResponseFlowOutputsTypeDef(
    _ClientCreateFlowResponseFlowOutputsTypeDef
):
    """
    Type definition for `ClientCreateFlowResponseFlow` `Outputs`

    - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
    transfer cost to be billed to the subscriber.

    - **Description** *(string) --* A description of the output.

    - **Destination** *(string) --* The address where you want to send the output.

    - **Encryption** *(dict) --* The type of key used for the encryption. If no keyType is
    provided, the service will use the default setting (static-key).

      - **Algorithm** *(string) --* The type of algorithm that is used for the encryption
      (such as aes128, aes192, or aes256).

      - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
      represented by a 32-character string, to be used with the key for encrypting content.
      This parameter is not valid for static key encryption.

      - **DeviceId** *(string) --* The value of one of the devices that you configured with
      your digital rights management (DRM) platform key provider. This parameter is required
      for SPEKE encryption and is not valid for static key encryption.

      - **KeyType** *(string) --* The type of key that is used for the encryption. If no
      keyType is provided, the service will use the default setting (static-key).

      - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
      created in. This parameter is required for SPEKE encryption and is not valid for static
      key encryption.

      - **ResourceId** *(string) --* An identifier for the content. The service sends this
      value to the key server to identify the current endpoint. The resource ID is also known
      as the content ID. This parameter is required for SPEKE encryption and is not valid for
      static key encryption.

      - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
      set up AWS Elemental MediaConnect as a trusted entity).

      - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
      Manager to store the encryption key. This parameter is required for static key
      encryption and is not valid for SPEKE encryption.

      - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
      your key server. This parameter is required for SPEKE encryption and is not valid for
      static key encryption.

    - **EntitlementArn** *(string) --* The ARN of the entitlement on the originator''s flow.
    This value is relevant only on entitled flows.

    - **MediaLiveInputArn** *(string) --* The input ARN of the AWS Elemental MediaLive
    channel. This parameter is relevant only for outputs that were added by creating a
    MediaLive input.

    - **Name** *(string) --* The name of the output. This value must be unique within the
    current flow.

    - **OutputArn** *(string) --* The ARN of the output.

    - **Port** *(integer) --* The port to use when content is distributed to this output.

    - **Transport** *(dict) --* Attributes related to the transport stream that are used in
    the output.

      - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
      initiate output requests to this flow. These IP addresses should be in the form of a
      Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

        - *(string) --*

      - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
      streams.

      - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter
      applies only to RIST-based and Zixi-based streams.

      - **Protocol** *(string) --* The protocol that is used by the source or output.

      - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

      - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST,
      RTP, and RTP-FEC streams.

      - **StreamId** *(string) --* The stream ID that you want to use for this transport.
      This parameter applies only to Zixi-based streams.
    """


_ClientCreateFlowResponseFlowSourceTypeDef = TypedDict(
    "_ClientCreateFlowResponseFlowSourceTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Decryption": Dict[str, Any],
        "Description": str,
        "EntitlementArn": str,
        "IngestIp": str,
        "IngestPort": int,
        "Name": str,
        "SourceArn": str,
        "Transport": Dict[str, Any],
        "WhitelistCidr": str,
    },
    total=False,
)


class ClientCreateFlowResponseFlowSourceTypeDef(
    _ClientCreateFlowResponseFlowSourceTypeDef
):
    """
    Type definition for `ClientCreateFlowResponseFlow` `Source`

    - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
    transfer cost to be billed to the subscriber.

    - **Decryption** *(dict) --* The type of encryption that is used on the content ingested
    from this source.

      - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
      as aes128, aes192, or aes256).

      - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
      by a 32-character string, to be used with the key for encrypting content. This parameter
      is not valid for static key encryption.

      - **DeviceId** *(string) --* The value of one of the devices that you configured with
      your digital rights management (DRM) platform key provider. This parameter is required
      for SPEKE encryption and is not valid for static key encryption.

      - **KeyType** *(string) --* The type of key that is used for the encryption. If no
      keyType is provided, the service will use the default setting (static-key).

      - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
      in. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

      - **ResourceId** *(string) --* An identifier for the content. The service sends this
      value to the key server to identify the current endpoint. The resource ID is also known
      as the content ID. This parameter is required for SPEKE encryption and is not valid for
      static key encryption.

      - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
      set up AWS Elemental MediaConnect as a trusted entity).

      - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
      Manager to store the encryption key. This parameter is required for static key encryption
      and is not valid for SPEKE encryption.

      - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
      your key server. This parameter is required for SPEKE encryption and is not valid for
      static key encryption.

    - **Description** *(string) --* A description for the source. This value is not used or
    seen outside of the current AWS Elemental MediaConnect account.

    - **EntitlementArn** *(string) --* The ARN of the entitlement that allows you to subscribe
    to content that comes from another AWS account. The entitlement is set by the content
    originator and the ARN is generated as part of the originator's flow.

    - **IngestIp** *(string) --* The IP address that the flow will be listening on for incoming
    content.

    - **IngestPort** *(integer) --* The port that the flow will be listening on for incoming
    content.

    - **Name** *(string) --* The name of the source.

    - **SourceArn** *(string) --* The ARN of the source.

    - **Transport** *(dict) --* Attributes related to the transport stream that are used in the
    source.

      - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
      initiate output requests to this flow. These IP addresses should be in the form of a
      Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

        - *(string) --*

      - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
      streams.

      - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter
      applies only to RIST-based and Zixi-based streams.

      - **Protocol** *(string) --* The protocol that is used by the source or output.

      - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

      - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST,
      RTP, and RTP-FEC streams.

      - **StreamId** *(string) --* The stream ID that you want to use for this transport. This
      parameter applies only to Zixi-based streams.

    - **WhitelistCidr** *(string) --* The range of IP addresses that should be allowed to
    contribute content to your source. These IP addresses should be in the form of a Classless
    Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    """


_ClientCreateFlowResponseFlowTypeDef = TypedDict(
    "_ClientCreateFlowResponseFlowTypeDef",
    {
        "AvailabilityZone": str,
        "Description": str,
        "EgressIp": str,
        "Entitlements": List[ClientCreateFlowResponseFlowEntitlementsTypeDef],
        "FlowArn": str,
        "Name": str,
        "Outputs": List[ClientCreateFlowResponseFlowOutputsTypeDef],
        "Source": ClientCreateFlowResponseFlowSourceTypeDef,
        "Status": str,
    },
    total=False,
)


class ClientCreateFlowResponseFlowTypeDef(_ClientCreateFlowResponseFlowTypeDef):
    """
    Type definition for `ClientCreateFlowResponse` `Flow`

    - **AvailabilityZone** *(string) --* The Availability Zone that you want to create the flow
    in. These options are limited to the Availability Zones within the current AWS.

    - **Description** *(string) --* A description of the flow. This value is not used or seen
    outside of the current AWS Elemental MediaConnect account.

    - **EgressIp** *(string) --* The IP address from which video will be sent to output
    destinations.

    - **Entitlements** *(list) --* The entitlements in this flow.

      - *(dict) --* The settings for a flow entitlement.

        - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
        transfer cost to be billed to the subscriber.

        - **Description** *(string) --* A description of the entitlement.

        - **Encryption** *(dict) --* The type of encryption that will be used on the output that
        is associated with this entitlement.

          - **Algorithm** *(string) --* The type of algorithm that is used for the encryption
          (such as aes128, aes192, or aes256).

          - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
          represented by a 32-character string, to be used with the key for encrypting content.
          This parameter is not valid for static key encryption.

          - **DeviceId** *(string) --* The value of one of the devices that you configured with
          your digital rights management (DRM) platform key provider. This parameter is required
          for SPEKE encryption and is not valid for static key encryption.

          - **KeyType** *(string) --* The type of key that is used for the encryption. If no
          keyType is provided, the service will use the default setting (static-key).

          - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
          created in. This parameter is required for SPEKE encryption and is not valid for static
          key encryption.

          - **ResourceId** *(string) --* An identifier for the content. The service sends this
          value to the key server to identify the current endpoint. The resource ID is also known
          as the content ID. This parameter is required for SPEKE encryption and is not valid for
          static key encryption.

          - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
          set up AWS Elemental MediaConnect as a trusted entity).

          - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
          Manager to store the encryption key. This parameter is required for static key
          encryption and is not valid for SPEKE encryption.

          - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
          your key server. This parameter is required for SPEKE encryption and is not valid for
          static key encryption.

        - **EntitlementArn** *(string) --* The ARN of the entitlement.

        - **Name** *(string) --* The name of the entitlement.

        - **Subscribers** *(list) --* The AWS account IDs that you want to share your content
        with. The receiving accounts (subscribers) will be allowed to create their own flow using
        your content as the source.

          - *(string) --*

    - **FlowArn** *(string) --* The Amazon Resource Name (ARN), a unique identifier for any AWS
    resource, of the flow.

    - **Name** *(string) --* The name of the flow.

    - **Outputs** *(list) --* The outputs in this flow.

      - *(dict) --* The settings for an output.

        - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
        transfer cost to be billed to the subscriber.

        - **Description** *(string) --* A description of the output.

        - **Destination** *(string) --* The address where you want to send the output.

        - **Encryption** *(dict) --* The type of key used for the encryption. If no keyType is
        provided, the service will use the default setting (static-key).

          - **Algorithm** *(string) --* The type of algorithm that is used for the encryption
          (such as aes128, aes192, or aes256).

          - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
          represented by a 32-character string, to be used with the key for encrypting content.
          This parameter is not valid for static key encryption.

          - **DeviceId** *(string) --* The value of one of the devices that you configured with
          your digital rights management (DRM) platform key provider. This parameter is required
          for SPEKE encryption and is not valid for static key encryption.

          - **KeyType** *(string) --* The type of key that is used for the encryption. If no
          keyType is provided, the service will use the default setting (static-key).

          - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
          created in. This parameter is required for SPEKE encryption and is not valid for static
          key encryption.

          - **ResourceId** *(string) --* An identifier for the content. The service sends this
          value to the key server to identify the current endpoint. The resource ID is also known
          as the content ID. This parameter is required for SPEKE encryption and is not valid for
          static key encryption.

          - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
          set up AWS Elemental MediaConnect as a trusted entity).

          - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
          Manager to store the encryption key. This parameter is required for static key
          encryption and is not valid for SPEKE encryption.

          - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
          your key server. This parameter is required for SPEKE encryption and is not valid for
          static key encryption.

        - **EntitlementArn** *(string) --* The ARN of the entitlement on the originator''s flow.
        This value is relevant only on entitled flows.

        - **MediaLiveInputArn** *(string) --* The input ARN of the AWS Elemental MediaLive
        channel. This parameter is relevant only for outputs that were added by creating a
        MediaLive input.

        - **Name** *(string) --* The name of the output. This value must be unique within the
        current flow.

        - **OutputArn** *(string) --* The ARN of the output.

        - **Port** *(integer) --* The port to use when content is distributed to this output.

        - **Transport** *(dict) --* Attributes related to the transport stream that are used in
        the output.

          - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
          initiate output requests to this flow. These IP addresses should be in the form of a
          Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

            - *(string) --*

          - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
          streams.

          - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter
          applies only to RIST-based and Zixi-based streams.

          - **Protocol** *(string) --* The protocol that is used by the source or output.

          - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

          - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST,
          RTP, and RTP-FEC streams.

          - **StreamId** *(string) --* The stream ID that you want to use for this transport.
          This parameter applies only to Zixi-based streams.

    - **Source** *(dict) --* The settings for the source of the flow.

      - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
      transfer cost to be billed to the subscriber.

      - **Decryption** *(dict) --* The type of encryption that is used on the content ingested
      from this source.

        - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
        as aes128, aes192, or aes256).

        - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
        by a 32-character string, to be used with the key for encrypting content. This parameter
        is not valid for static key encryption.

        - **DeviceId** *(string) --* The value of one of the devices that you configured with
        your digital rights management (DRM) platform key provider. This parameter is required
        for SPEKE encryption and is not valid for static key encryption.

        - **KeyType** *(string) --* The type of key that is used for the encryption. If no
        keyType is provided, the service will use the default setting (static-key).

        - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
        in. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.

        - **ResourceId** *(string) --* An identifier for the content. The service sends this
        value to the key server to identify the current endpoint. The resource ID is also known
        as the content ID. This parameter is required for SPEKE encryption and is not valid for
        static key encryption.

        - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
        set up AWS Elemental MediaConnect as a trusted entity).

        - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
        Manager to store the encryption key. This parameter is required for static key encryption
        and is not valid for SPEKE encryption.

        - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
        your key server. This parameter is required for SPEKE encryption and is not valid for
        static key encryption.

      - **Description** *(string) --* A description for the source. This value is not used or
      seen outside of the current AWS Elemental MediaConnect account.

      - **EntitlementArn** *(string) --* The ARN of the entitlement that allows you to subscribe
      to content that comes from another AWS account. The entitlement is set by the content
      originator and the ARN is generated as part of the originator's flow.

      - **IngestIp** *(string) --* The IP address that the flow will be listening on for incoming
      content.

      - **IngestPort** *(integer) --* The port that the flow will be listening on for incoming
      content.

      - **Name** *(string) --* The name of the source.

      - **SourceArn** *(string) --* The ARN of the source.

      - **Transport** *(dict) --* Attributes related to the transport stream that are used in the
      source.

        - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
        initiate output requests to this flow. These IP addresses should be in the form of a
        Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

          - *(string) --*

        - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
        streams.

        - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter
        applies only to RIST-based and Zixi-based streams.

        - **Protocol** *(string) --* The protocol that is used by the source or output.

        - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

        - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST,
        RTP, and RTP-FEC streams.

        - **StreamId** *(string) --* The stream ID that you want to use for this transport. This
        parameter applies only to Zixi-based streams.

      - **WhitelistCidr** *(string) --* The range of IP addresses that should be allowed to
      contribute content to your source. These IP addresses should be in the form of a Classless
      Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

    - **Status** *(string) --* The current status of the flow.
    """


_ClientCreateFlowResponseTypeDef = TypedDict(
    "_ClientCreateFlowResponseTypeDef",
    {"Flow": ClientCreateFlowResponseFlowTypeDef},
    total=False,
)


class ClientCreateFlowResponseTypeDef(_ClientCreateFlowResponseTypeDef):
    """
    Type definition for `ClientCreateFlow` `Response`

    - **Flow** *(dict) --* The settings for a flow, including its source, outputs, and entitlements.

      - **AvailabilityZone** *(string) --* The Availability Zone that you want to create the flow
      in. These options are limited to the Availability Zones within the current AWS.

      - **Description** *(string) --* A description of the flow. This value is not used or seen
      outside of the current AWS Elemental MediaConnect account.

      - **EgressIp** *(string) --* The IP address from which video will be sent to output
      destinations.

      - **Entitlements** *(list) --* The entitlements in this flow.

        - *(dict) --* The settings for a flow entitlement.

          - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
          transfer cost to be billed to the subscriber.

          - **Description** *(string) --* A description of the entitlement.

          - **Encryption** *(dict) --* The type of encryption that will be used on the output that
          is associated with this entitlement.

            - **Algorithm** *(string) --* The type of algorithm that is used for the encryption
            (such as aes128, aes192, or aes256).

            - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
            represented by a 32-character string, to be used with the key for encrypting content.
            This parameter is not valid for static key encryption.

            - **DeviceId** *(string) --* The value of one of the devices that you configured with
            your digital rights management (DRM) platform key provider. This parameter is required
            for SPEKE encryption and is not valid for static key encryption.

            - **KeyType** *(string) --* The type of key that is used for the encryption. If no
            keyType is provided, the service will use the default setting (static-key).

            - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
            created in. This parameter is required for SPEKE encryption and is not valid for static
            key encryption.

            - **ResourceId** *(string) --* An identifier for the content. The service sends this
            value to the key server to identify the current endpoint. The resource ID is also known
            as the content ID. This parameter is required for SPEKE encryption and is not valid for
            static key encryption.

            - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
            set up AWS Elemental MediaConnect as a trusted entity).

            - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
            Manager to store the encryption key. This parameter is required for static key
            encryption and is not valid for SPEKE encryption.

            - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
            your key server. This parameter is required for SPEKE encryption and is not valid for
            static key encryption.

          - **EntitlementArn** *(string) --* The ARN of the entitlement.

          - **Name** *(string) --* The name of the entitlement.

          - **Subscribers** *(list) --* The AWS account IDs that you want to share your content
          with. The receiving accounts (subscribers) will be allowed to create their own flow using
          your content as the source.

            - *(string) --*

      - **FlowArn** *(string) --* The Amazon Resource Name (ARN), a unique identifier for any AWS
      resource, of the flow.

      - **Name** *(string) --* The name of the flow.

      - **Outputs** *(list) --* The outputs in this flow.

        - *(dict) --* The settings for an output.

          - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
          transfer cost to be billed to the subscriber.

          - **Description** *(string) --* A description of the output.

          - **Destination** *(string) --* The address where you want to send the output.

          - **Encryption** *(dict) --* The type of key used for the encryption. If no keyType is
          provided, the service will use the default setting (static-key).

            - **Algorithm** *(string) --* The type of algorithm that is used for the encryption
            (such as aes128, aes192, or aes256).

            - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
            represented by a 32-character string, to be used with the key for encrypting content.
            This parameter is not valid for static key encryption.

            - **DeviceId** *(string) --* The value of one of the devices that you configured with
            your digital rights management (DRM) platform key provider. This parameter is required
            for SPEKE encryption and is not valid for static key encryption.

            - **KeyType** *(string) --* The type of key that is used for the encryption. If no
            keyType is provided, the service will use the default setting (static-key).

            - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
            created in. This parameter is required for SPEKE encryption and is not valid for static
            key encryption.

            - **ResourceId** *(string) --* An identifier for the content. The service sends this
            value to the key server to identify the current endpoint. The resource ID is also known
            as the content ID. This parameter is required for SPEKE encryption and is not valid for
            static key encryption.

            - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
            set up AWS Elemental MediaConnect as a trusted entity).

            - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
            Manager to store the encryption key. This parameter is required for static key
            encryption and is not valid for SPEKE encryption.

            - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
            your key server. This parameter is required for SPEKE encryption and is not valid for
            static key encryption.

          - **EntitlementArn** *(string) --* The ARN of the entitlement on the originator''s flow.
          This value is relevant only on entitled flows.

          - **MediaLiveInputArn** *(string) --* The input ARN of the AWS Elemental MediaLive
          channel. This parameter is relevant only for outputs that were added by creating a
          MediaLive input.

          - **Name** *(string) --* The name of the output. This value must be unique within the
          current flow.

          - **OutputArn** *(string) --* The ARN of the output.

          - **Port** *(integer) --* The port to use when content is distributed to this output.

          - **Transport** *(dict) --* Attributes related to the transport stream that are used in
          the output.

            - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
            initiate output requests to this flow. These IP addresses should be in the form of a
            Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

              - *(string) --*

            - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
            streams.

            - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter
            applies only to RIST-based and Zixi-based streams.

            - **Protocol** *(string) --* The protocol that is used by the source or output.

            - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

            - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST,
            RTP, and RTP-FEC streams.

            - **StreamId** *(string) --* The stream ID that you want to use for this transport.
            This parameter applies only to Zixi-based streams.

      - **Source** *(dict) --* The settings for the source of the flow.

        - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
        transfer cost to be billed to the subscriber.

        - **Decryption** *(dict) --* The type of encryption that is used on the content ingested
        from this source.

          - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
          as aes128, aes192, or aes256).

          - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
          by a 32-character string, to be used with the key for encrypting content. This parameter
          is not valid for static key encryption.

          - **DeviceId** *(string) --* The value of one of the devices that you configured with
          your digital rights management (DRM) platform key provider. This parameter is required
          for SPEKE encryption and is not valid for static key encryption.

          - **KeyType** *(string) --* The type of key that is used for the encryption. If no
          keyType is provided, the service will use the default setting (static-key).

          - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
          in. This parameter is required for SPEKE encryption and is not valid for static key
          encryption.

          - **ResourceId** *(string) --* An identifier for the content. The service sends this
          value to the key server to identify the current endpoint. The resource ID is also known
          as the content ID. This parameter is required for SPEKE encryption and is not valid for
          static key encryption.

          - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
          set up AWS Elemental MediaConnect as a trusted entity).

          - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
          Manager to store the encryption key. This parameter is required for static key encryption
          and is not valid for SPEKE encryption.

          - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
          your key server. This parameter is required for SPEKE encryption and is not valid for
          static key encryption.

        - **Description** *(string) --* A description for the source. This value is not used or
        seen outside of the current AWS Elemental MediaConnect account.

        - **EntitlementArn** *(string) --* The ARN of the entitlement that allows you to subscribe
        to content that comes from another AWS account. The entitlement is set by the content
        originator and the ARN is generated as part of the originator's flow.

        - **IngestIp** *(string) --* The IP address that the flow will be listening on for incoming
        content.

        - **IngestPort** *(integer) --* The port that the flow will be listening on for incoming
        content.

        - **Name** *(string) --* The name of the source.

        - **SourceArn** *(string) --* The ARN of the source.

        - **Transport** *(dict) --* Attributes related to the transport stream that are used in the
        source.

          - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
          initiate output requests to this flow. These IP addresses should be in the form of a
          Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

            - *(string) --*

          - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
          streams.

          - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter
          applies only to RIST-based and Zixi-based streams.

          - **Protocol** *(string) --* The protocol that is used by the source or output.

          - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

          - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST,
          RTP, and RTP-FEC streams.

          - **StreamId** *(string) --* The stream ID that you want to use for this transport. This
          parameter applies only to Zixi-based streams.

        - **WhitelistCidr** *(string) --* The range of IP addresses that should be allowed to
        contribute content to your source. These IP addresses should be in the form of a Classless
        Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

      - **Status** *(string) --* The current status of the flow.
    """


_ClientCreateFlowSourceTypeDef = TypedDict(
    "_ClientCreateFlowSourceTypeDef",
    {
        "Decryption": Dict[str, Any],
        "Description": str,
        "EntitlementArn": str,
        "IngestPort": int,
        "MaxBitrate": int,
        "MaxLatency": int,
        "Name": str,
        "Protocol": str,
        "StreamId": str,
        "WhitelistCidr": str,
    },
    total=False,
)


class ClientCreateFlowSourceTypeDef(_ClientCreateFlowSourceTypeDef):
    """
    Type definition for `ClientCreateFlow` `Source`

    - **Decryption** *(dict) --* The type of encryption that is used on the content ingested from
    this source.

      - **Algorithm** *(string) --* **[REQUIRED]** The type of algorithm that is used for the
      encryption (such as aes128, aes192, or aes256).

      - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented by a
      32-character string, to be used with the key for encrypting content. This parameter is not
      valid for static key encryption.

      - **DeviceId** *(string) --* The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.

      - **KeyType** *(string) --* The type of key that is used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).

      - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created in.
      This parameter is required for SPEKE encryption and is not valid for static key encryption.

      - **ResourceId** *(string) --* An identifier for the content. The service sends this value to
      the key server to identify the current endpoint. The resource ID is also known as the content
      ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.

      - **RoleArn** *(string) --* **[REQUIRED]** The ARN of the role that you created during setup
      (when you set up AWS Elemental MediaConnect as a trusted entity).

      - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets Manager to
      store the encryption key. This parameter is required for static key encryption and is not valid
      for SPEKE encryption.

      - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to your key
      server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

    - **Description** *(string) --* A description for the source. This value is not used or seen
    outside of the current AWS Elemental MediaConnect account.

    - **EntitlementArn** *(string) --* The ARN of the entitlement that allows you to subscribe to
    this flow. The entitlement is set by the flow originator, and the ARN is generated as part of the
    originator's flow.

    - **IngestPort** *(integer) --* The port that the flow will be listening on for incoming content.

    - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC streams.

    - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter applies only
    to RIST-based and Zixi-based streams.

    - **Name** *(string) --* The name of the source.

    - **Protocol** *(string) --* The protocol that is used by the source.

    - **StreamId** *(string) --* The stream ID that you want to use for this transport. This
    parameter applies only to Zixi-based streams.

    - **WhitelistCidr** *(string) --* The range of IP addresses that should be allowed to contribute
    content to your source. These IP addresses should be in the form of a Classless Inter-Domain
    Routing (CIDR) block; for example, 10.0.0.0/16.
    """


_ClientDeleteFlowResponseTypeDef = TypedDict(
    "_ClientDeleteFlowResponseTypeDef", {"FlowArn": str, "Status": str}, total=False
)


class ClientDeleteFlowResponseTypeDef(_ClientDeleteFlowResponseTypeDef):
    """
    Type definition for `ClientDeleteFlow` `Response`

    - **FlowArn** *(string) --* The ARN of the flow that was deleted.

    - **Status** *(string) --* The status of the flow when the DeleteFlow process begins.
    """


_ClientDescribeFlowResponseFlowEntitlementsTypeDef = TypedDict(
    "_ClientDescribeFlowResponseFlowEntitlementsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": Dict[str, Any],
        "EntitlementArn": str,
        "Name": str,
        "Subscribers": List[Any],
    },
    total=False,
)


class ClientDescribeFlowResponseFlowEntitlementsTypeDef(
    _ClientDescribeFlowResponseFlowEntitlementsTypeDef
):
    """
    Type definition for `ClientDescribeFlowResponseFlow` `Entitlements`

    - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
    transfer cost to be billed to the subscriber.

    - **Description** *(string) --* A description of the entitlement.

    - **Encryption** *(dict) --* The type of encryption that will be used on the output that
    is associated with this entitlement.

      - **Algorithm** *(string) --* The type of algorithm that is used for the encryption
      (such as aes128, aes192, or aes256).

      - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
      represented by a 32-character string, to be used with the key for encrypting content.
      This parameter is not valid for static key encryption.

      - **DeviceId** *(string) --* The value of one of the devices that you configured with
      your digital rights management (DRM) platform key provider. This parameter is required
      for SPEKE encryption and is not valid for static key encryption.

      - **KeyType** *(string) --* The type of key that is used for the encryption. If no
      keyType is provided, the service will use the default setting (static-key).

      - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
      created in. This parameter is required for SPEKE encryption and is not valid for static
      key encryption.

      - **ResourceId** *(string) --* An identifier for the content. The service sends this
      value to the key server to identify the current endpoint. The resource ID is also known
      as the content ID. This parameter is required for SPEKE encryption and is not valid for
      static key encryption.

      - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
      set up AWS Elemental MediaConnect as a trusted entity).

      - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
      Manager to store the encryption key. This parameter is required for static key
      encryption and is not valid for SPEKE encryption.

      - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
      your key server. This parameter is required for SPEKE encryption and is not valid for
      static key encryption.

    - **EntitlementArn** *(string) --* The ARN of the entitlement.

    - **Name** *(string) --* The name of the entitlement.

    - **Subscribers** *(list) --* The AWS account IDs that you want to share your content
    with. The receiving accounts (subscribers) will be allowed to create their own flow using
    your content as the source.

      - *(string) --*
    """


_ClientDescribeFlowResponseFlowOutputsTypeDef = TypedDict(
    "_ClientDescribeFlowResponseFlowOutputsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Destination": str,
        "Encryption": Dict[str, Any],
        "EntitlementArn": str,
        "MediaLiveInputArn": str,
        "Name": str,
        "OutputArn": str,
        "Port": int,
        "Transport": Dict[str, Any],
    },
    total=False,
)


class ClientDescribeFlowResponseFlowOutputsTypeDef(
    _ClientDescribeFlowResponseFlowOutputsTypeDef
):
    """
    Type definition for `ClientDescribeFlowResponseFlow` `Outputs`

    - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
    transfer cost to be billed to the subscriber.

    - **Description** *(string) --* A description of the output.

    - **Destination** *(string) --* The address where you want to send the output.

    - **Encryption** *(dict) --* The type of key used for the encryption. If no keyType is
    provided, the service will use the default setting (static-key).

      - **Algorithm** *(string) --* The type of algorithm that is used for the encryption
      (such as aes128, aes192, or aes256).

      - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
      represented by a 32-character string, to be used with the key for encrypting content.
      This parameter is not valid for static key encryption.

      - **DeviceId** *(string) --* The value of one of the devices that you configured with
      your digital rights management (DRM) platform key provider. This parameter is required
      for SPEKE encryption and is not valid for static key encryption.

      - **KeyType** *(string) --* The type of key that is used for the encryption. If no
      keyType is provided, the service will use the default setting (static-key).

      - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
      created in. This parameter is required for SPEKE encryption and is not valid for static
      key encryption.

      - **ResourceId** *(string) --* An identifier for the content. The service sends this
      value to the key server to identify the current endpoint. The resource ID is also known
      as the content ID. This parameter is required for SPEKE encryption and is not valid for
      static key encryption.

      - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
      set up AWS Elemental MediaConnect as a trusted entity).

      - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
      Manager to store the encryption key. This parameter is required for static key
      encryption and is not valid for SPEKE encryption.

      - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
      your key server. This parameter is required for SPEKE encryption and is not valid for
      static key encryption.

    - **EntitlementArn** *(string) --* The ARN of the entitlement on the originator''s flow.
    This value is relevant only on entitled flows.

    - **MediaLiveInputArn** *(string) --* The input ARN of the AWS Elemental MediaLive
    channel. This parameter is relevant only for outputs that were added by creating a
    MediaLive input.

    - **Name** *(string) --* The name of the output. This value must be unique within the
    current flow.

    - **OutputArn** *(string) --* The ARN of the output.

    - **Port** *(integer) --* The port to use when content is distributed to this output.

    - **Transport** *(dict) --* Attributes related to the transport stream that are used in
    the output.

      - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
      initiate output requests to this flow. These IP addresses should be in the form of a
      Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

        - *(string) --*

      - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
      streams.

      - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter
      applies only to RIST-based and Zixi-based streams.

      - **Protocol** *(string) --* The protocol that is used by the source or output.

      - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

      - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST,
      RTP, and RTP-FEC streams.

      - **StreamId** *(string) --* The stream ID that you want to use for this transport.
      This parameter applies only to Zixi-based streams.
    """


_ClientDescribeFlowResponseFlowSourceTypeDef = TypedDict(
    "_ClientDescribeFlowResponseFlowSourceTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Decryption": Dict[str, Any],
        "Description": str,
        "EntitlementArn": str,
        "IngestIp": str,
        "IngestPort": int,
        "Name": str,
        "SourceArn": str,
        "Transport": Dict[str, Any],
        "WhitelistCidr": str,
    },
    total=False,
)


class ClientDescribeFlowResponseFlowSourceTypeDef(
    _ClientDescribeFlowResponseFlowSourceTypeDef
):
    """
    Type definition for `ClientDescribeFlowResponseFlow` `Source`

    - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
    transfer cost to be billed to the subscriber.

    - **Decryption** *(dict) --* The type of encryption that is used on the content ingested
    from this source.

      - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
      as aes128, aes192, or aes256).

      - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
      by a 32-character string, to be used with the key for encrypting content. This parameter
      is not valid for static key encryption.

      - **DeviceId** *(string) --* The value of one of the devices that you configured with
      your digital rights management (DRM) platform key provider. This parameter is required
      for SPEKE encryption and is not valid for static key encryption.

      - **KeyType** *(string) --* The type of key that is used for the encryption. If no
      keyType is provided, the service will use the default setting (static-key).

      - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
      in. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

      - **ResourceId** *(string) --* An identifier for the content. The service sends this
      value to the key server to identify the current endpoint. The resource ID is also known
      as the content ID. This parameter is required for SPEKE encryption and is not valid for
      static key encryption.

      - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
      set up AWS Elemental MediaConnect as a trusted entity).

      - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
      Manager to store the encryption key. This parameter is required for static key encryption
      and is not valid for SPEKE encryption.

      - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
      your key server. This parameter is required for SPEKE encryption and is not valid for
      static key encryption.

    - **Description** *(string) --* A description for the source. This value is not used or
    seen outside of the current AWS Elemental MediaConnect account.

    - **EntitlementArn** *(string) --* The ARN of the entitlement that allows you to subscribe
    to content that comes from another AWS account. The entitlement is set by the content
    originator and the ARN is generated as part of the originator's flow.

    - **IngestIp** *(string) --* The IP address that the flow will be listening on for incoming
    content.

    - **IngestPort** *(integer) --* The port that the flow will be listening on for incoming
    content.

    - **Name** *(string) --* The name of the source.

    - **SourceArn** *(string) --* The ARN of the source.

    - **Transport** *(dict) --* Attributes related to the transport stream that are used in the
    source.

      - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
      initiate output requests to this flow. These IP addresses should be in the form of a
      Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

        - *(string) --*

      - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
      streams.

      - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter
      applies only to RIST-based and Zixi-based streams.

      - **Protocol** *(string) --* The protocol that is used by the source or output.

      - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

      - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST,
      RTP, and RTP-FEC streams.

      - **StreamId** *(string) --* The stream ID that you want to use for this transport. This
      parameter applies only to Zixi-based streams.

    - **WhitelistCidr** *(string) --* The range of IP addresses that should be allowed to
    contribute content to your source. These IP addresses should be in the form of a Classless
    Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    """


_ClientDescribeFlowResponseFlowTypeDef = TypedDict(
    "_ClientDescribeFlowResponseFlowTypeDef",
    {
        "AvailabilityZone": str,
        "Description": str,
        "EgressIp": str,
        "Entitlements": List[ClientDescribeFlowResponseFlowEntitlementsTypeDef],
        "FlowArn": str,
        "Name": str,
        "Outputs": List[ClientDescribeFlowResponseFlowOutputsTypeDef],
        "Source": ClientDescribeFlowResponseFlowSourceTypeDef,
        "Status": str,
    },
    total=False,
)


class ClientDescribeFlowResponseFlowTypeDef(_ClientDescribeFlowResponseFlowTypeDef):
    """
    Type definition for `ClientDescribeFlowResponse` `Flow`

    - **AvailabilityZone** *(string) --* The Availability Zone that you want to create the flow
    in. These options are limited to the Availability Zones within the current AWS.

    - **Description** *(string) --* A description of the flow. This value is not used or seen
    outside of the current AWS Elemental MediaConnect account.

    - **EgressIp** *(string) --* The IP address from which video will be sent to output
    destinations.

    - **Entitlements** *(list) --* The entitlements in this flow.

      - *(dict) --* The settings for a flow entitlement.

        - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
        transfer cost to be billed to the subscriber.

        - **Description** *(string) --* A description of the entitlement.

        - **Encryption** *(dict) --* The type of encryption that will be used on the output that
        is associated with this entitlement.

          - **Algorithm** *(string) --* The type of algorithm that is used for the encryption
          (such as aes128, aes192, or aes256).

          - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
          represented by a 32-character string, to be used with the key for encrypting content.
          This parameter is not valid for static key encryption.

          - **DeviceId** *(string) --* The value of one of the devices that you configured with
          your digital rights management (DRM) platform key provider. This parameter is required
          for SPEKE encryption and is not valid for static key encryption.

          - **KeyType** *(string) --* The type of key that is used for the encryption. If no
          keyType is provided, the service will use the default setting (static-key).

          - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
          created in. This parameter is required for SPEKE encryption and is not valid for static
          key encryption.

          - **ResourceId** *(string) --* An identifier for the content. The service sends this
          value to the key server to identify the current endpoint. The resource ID is also known
          as the content ID. This parameter is required for SPEKE encryption and is not valid for
          static key encryption.

          - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
          set up AWS Elemental MediaConnect as a trusted entity).

          - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
          Manager to store the encryption key. This parameter is required for static key
          encryption and is not valid for SPEKE encryption.

          - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
          your key server. This parameter is required for SPEKE encryption and is not valid for
          static key encryption.

        - **EntitlementArn** *(string) --* The ARN of the entitlement.

        - **Name** *(string) --* The name of the entitlement.

        - **Subscribers** *(list) --* The AWS account IDs that you want to share your content
        with. The receiving accounts (subscribers) will be allowed to create their own flow using
        your content as the source.

          - *(string) --*

    - **FlowArn** *(string) --* The Amazon Resource Name (ARN), a unique identifier for any AWS
    resource, of the flow.

    - **Name** *(string) --* The name of the flow.

    - **Outputs** *(list) --* The outputs in this flow.

      - *(dict) --* The settings for an output.

        - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
        transfer cost to be billed to the subscriber.

        - **Description** *(string) --* A description of the output.

        - **Destination** *(string) --* The address where you want to send the output.

        - **Encryption** *(dict) --* The type of key used for the encryption. If no keyType is
        provided, the service will use the default setting (static-key).

          - **Algorithm** *(string) --* The type of algorithm that is used for the encryption
          (such as aes128, aes192, or aes256).

          - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
          represented by a 32-character string, to be used with the key for encrypting content.
          This parameter is not valid for static key encryption.

          - **DeviceId** *(string) --* The value of one of the devices that you configured with
          your digital rights management (DRM) platform key provider. This parameter is required
          for SPEKE encryption and is not valid for static key encryption.

          - **KeyType** *(string) --* The type of key that is used for the encryption. If no
          keyType is provided, the service will use the default setting (static-key).

          - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
          created in. This parameter is required for SPEKE encryption and is not valid for static
          key encryption.

          - **ResourceId** *(string) --* An identifier for the content. The service sends this
          value to the key server to identify the current endpoint. The resource ID is also known
          as the content ID. This parameter is required for SPEKE encryption and is not valid for
          static key encryption.

          - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
          set up AWS Elemental MediaConnect as a trusted entity).

          - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
          Manager to store the encryption key. This parameter is required for static key
          encryption and is not valid for SPEKE encryption.

          - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
          your key server. This parameter is required for SPEKE encryption and is not valid for
          static key encryption.

        - **EntitlementArn** *(string) --* The ARN of the entitlement on the originator''s flow.
        This value is relevant only on entitled flows.

        - **MediaLiveInputArn** *(string) --* The input ARN of the AWS Elemental MediaLive
        channel. This parameter is relevant only for outputs that were added by creating a
        MediaLive input.

        - **Name** *(string) --* The name of the output. This value must be unique within the
        current flow.

        - **OutputArn** *(string) --* The ARN of the output.

        - **Port** *(integer) --* The port to use when content is distributed to this output.

        - **Transport** *(dict) --* Attributes related to the transport stream that are used in
        the output.

          - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
          initiate output requests to this flow. These IP addresses should be in the form of a
          Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

            - *(string) --*

          - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
          streams.

          - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter
          applies only to RIST-based and Zixi-based streams.

          - **Protocol** *(string) --* The protocol that is used by the source or output.

          - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

          - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST,
          RTP, and RTP-FEC streams.

          - **StreamId** *(string) --* The stream ID that you want to use for this transport.
          This parameter applies only to Zixi-based streams.

    - **Source** *(dict) --* The settings for the source of the flow.

      - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
      transfer cost to be billed to the subscriber.

      - **Decryption** *(dict) --* The type of encryption that is used on the content ingested
      from this source.

        - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
        as aes128, aes192, or aes256).

        - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
        by a 32-character string, to be used with the key for encrypting content. This parameter
        is not valid for static key encryption.

        - **DeviceId** *(string) --* The value of one of the devices that you configured with
        your digital rights management (DRM) platform key provider. This parameter is required
        for SPEKE encryption and is not valid for static key encryption.

        - **KeyType** *(string) --* The type of key that is used for the encryption. If no
        keyType is provided, the service will use the default setting (static-key).

        - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
        in. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.

        - **ResourceId** *(string) --* An identifier for the content. The service sends this
        value to the key server to identify the current endpoint. The resource ID is also known
        as the content ID. This parameter is required for SPEKE encryption and is not valid for
        static key encryption.

        - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
        set up AWS Elemental MediaConnect as a trusted entity).

        - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
        Manager to store the encryption key. This parameter is required for static key encryption
        and is not valid for SPEKE encryption.

        - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
        your key server. This parameter is required for SPEKE encryption and is not valid for
        static key encryption.

      - **Description** *(string) --* A description for the source. This value is not used or
      seen outside of the current AWS Elemental MediaConnect account.

      - **EntitlementArn** *(string) --* The ARN of the entitlement that allows you to subscribe
      to content that comes from another AWS account. The entitlement is set by the content
      originator and the ARN is generated as part of the originator's flow.

      - **IngestIp** *(string) --* The IP address that the flow will be listening on for incoming
      content.

      - **IngestPort** *(integer) --* The port that the flow will be listening on for incoming
      content.

      - **Name** *(string) --* The name of the source.

      - **SourceArn** *(string) --* The ARN of the source.

      - **Transport** *(dict) --* Attributes related to the transport stream that are used in the
      source.

        - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
        initiate output requests to this flow. These IP addresses should be in the form of a
        Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

          - *(string) --*

        - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
        streams.

        - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter
        applies only to RIST-based and Zixi-based streams.

        - **Protocol** *(string) --* The protocol that is used by the source or output.

        - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

        - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST,
        RTP, and RTP-FEC streams.

        - **StreamId** *(string) --* The stream ID that you want to use for this transport. This
        parameter applies only to Zixi-based streams.

      - **WhitelistCidr** *(string) --* The range of IP addresses that should be allowed to
      contribute content to your source. These IP addresses should be in the form of a Classless
      Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

    - **Status** *(string) --* The current status of the flow.
    """


_ClientDescribeFlowResponseMessagesTypeDef = TypedDict(
    "_ClientDescribeFlowResponseMessagesTypeDef", {"Errors": List[Any]}, total=False
)


class ClientDescribeFlowResponseMessagesTypeDef(
    _ClientDescribeFlowResponseMessagesTypeDef
):
    """
    Type definition for `ClientDescribeFlowResponse` `Messages`

    - **Errors** *(list) --* A list of errors that might have been generated from processes on
    this flow.

      - *(string) --*
    """


_ClientDescribeFlowResponseTypeDef = TypedDict(
    "_ClientDescribeFlowResponseTypeDef",
    {
        "Flow": ClientDescribeFlowResponseFlowTypeDef,
        "Messages": ClientDescribeFlowResponseMessagesTypeDef,
    },
    total=False,
)


class ClientDescribeFlowResponseTypeDef(_ClientDescribeFlowResponseTypeDef):
    """
    Type definition for `ClientDescribeFlow` `Response`

    - **Flow** *(dict) --* The settings for a flow, including its source, outputs, and entitlements.

      - **AvailabilityZone** *(string) --* The Availability Zone that you want to create the flow
      in. These options are limited to the Availability Zones within the current AWS.

      - **Description** *(string) --* A description of the flow. This value is not used or seen
      outside of the current AWS Elemental MediaConnect account.

      - **EgressIp** *(string) --* The IP address from which video will be sent to output
      destinations.

      - **Entitlements** *(list) --* The entitlements in this flow.

        - *(dict) --* The settings for a flow entitlement.

          - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
          transfer cost to be billed to the subscriber.

          - **Description** *(string) --* A description of the entitlement.

          - **Encryption** *(dict) --* The type of encryption that will be used on the output that
          is associated with this entitlement.

            - **Algorithm** *(string) --* The type of algorithm that is used for the encryption
            (such as aes128, aes192, or aes256).

            - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
            represented by a 32-character string, to be used with the key for encrypting content.
            This parameter is not valid for static key encryption.

            - **DeviceId** *(string) --* The value of one of the devices that you configured with
            your digital rights management (DRM) platform key provider. This parameter is required
            for SPEKE encryption and is not valid for static key encryption.

            - **KeyType** *(string) --* The type of key that is used for the encryption. If no
            keyType is provided, the service will use the default setting (static-key).

            - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
            created in. This parameter is required for SPEKE encryption and is not valid for static
            key encryption.

            - **ResourceId** *(string) --* An identifier for the content. The service sends this
            value to the key server to identify the current endpoint. The resource ID is also known
            as the content ID. This parameter is required for SPEKE encryption and is not valid for
            static key encryption.

            - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
            set up AWS Elemental MediaConnect as a trusted entity).

            - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
            Manager to store the encryption key. This parameter is required for static key
            encryption and is not valid for SPEKE encryption.

            - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
            your key server. This parameter is required for SPEKE encryption and is not valid for
            static key encryption.

          - **EntitlementArn** *(string) --* The ARN of the entitlement.

          - **Name** *(string) --* The name of the entitlement.

          - **Subscribers** *(list) --* The AWS account IDs that you want to share your content
          with. The receiving accounts (subscribers) will be allowed to create their own flow using
          your content as the source.

            - *(string) --*

      - **FlowArn** *(string) --* The Amazon Resource Name (ARN), a unique identifier for any AWS
      resource, of the flow.

      - **Name** *(string) --* The name of the flow.

      - **Outputs** *(list) --* The outputs in this flow.

        - *(dict) --* The settings for an output.

          - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
          transfer cost to be billed to the subscriber.

          - **Description** *(string) --* A description of the output.

          - **Destination** *(string) --* The address where you want to send the output.

          - **Encryption** *(dict) --* The type of key used for the encryption. If no keyType is
          provided, the service will use the default setting (static-key).

            - **Algorithm** *(string) --* The type of algorithm that is used for the encryption
            (such as aes128, aes192, or aes256).

            - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value
            represented by a 32-character string, to be used with the key for encrypting content.
            This parameter is not valid for static key encryption.

            - **DeviceId** *(string) --* The value of one of the devices that you configured with
            your digital rights management (DRM) platform key provider. This parameter is required
            for SPEKE encryption and is not valid for static key encryption.

            - **KeyType** *(string) --* The type of key that is used for the encryption. If no
            keyType is provided, the service will use the default setting (static-key).

            - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was
            created in. This parameter is required for SPEKE encryption and is not valid for static
            key encryption.

            - **ResourceId** *(string) --* An identifier for the content. The service sends this
            value to the key server to identify the current endpoint. The resource ID is also known
            as the content ID. This parameter is required for SPEKE encryption and is not valid for
            static key encryption.

            - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
            set up AWS Elemental MediaConnect as a trusted entity).

            - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
            Manager to store the encryption key. This parameter is required for static key
            encryption and is not valid for SPEKE encryption.

            - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
            your key server. This parameter is required for SPEKE encryption and is not valid for
            static key encryption.

          - **EntitlementArn** *(string) --* The ARN of the entitlement on the originator''s flow.
          This value is relevant only on entitled flows.

          - **MediaLiveInputArn** *(string) --* The input ARN of the AWS Elemental MediaLive
          channel. This parameter is relevant only for outputs that were added by creating a
          MediaLive input.

          - **Name** *(string) --* The name of the output. This value must be unique within the
          current flow.

          - **OutputArn** *(string) --* The ARN of the output.

          - **Port** *(integer) --* The port to use when content is distributed to this output.

          - **Transport** *(dict) --* Attributes related to the transport stream that are used in
          the output.

            - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
            initiate output requests to this flow. These IP addresses should be in the form of a
            Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

              - *(string) --*

            - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
            streams.

            - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter
            applies only to RIST-based and Zixi-based streams.

            - **Protocol** *(string) --* The protocol that is used by the source or output.

            - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

            - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST,
            RTP, and RTP-FEC streams.

            - **StreamId** *(string) --* The stream ID that you want to use for this transport.
            This parameter applies only to Zixi-based streams.

      - **Source** *(dict) --* The settings for the source of the flow.

        - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
        transfer cost to be billed to the subscriber.

        - **Decryption** *(dict) --* The type of encryption that is used on the content ingested
        from this source.

          - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
          as aes128, aes192, or aes256).

          - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
          by a 32-character string, to be used with the key for encrypting content. This parameter
          is not valid for static key encryption.

          - **DeviceId** *(string) --* The value of one of the devices that you configured with
          your digital rights management (DRM) platform key provider. This parameter is required
          for SPEKE encryption and is not valid for static key encryption.

          - **KeyType** *(string) --* The type of key that is used for the encryption. If no
          keyType is provided, the service will use the default setting (static-key).

          - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
          in. This parameter is required for SPEKE encryption and is not valid for static key
          encryption.

          - **ResourceId** *(string) --* An identifier for the content. The service sends this
          value to the key server to identify the current endpoint. The resource ID is also known
          as the content ID. This parameter is required for SPEKE encryption and is not valid for
          static key encryption.

          - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
          set up AWS Elemental MediaConnect as a trusted entity).

          - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
          Manager to store the encryption key. This parameter is required for static key encryption
          and is not valid for SPEKE encryption.

          - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
          your key server. This parameter is required for SPEKE encryption and is not valid for
          static key encryption.

        - **Description** *(string) --* A description for the source. This value is not used or
        seen outside of the current AWS Elemental MediaConnect account.

        - **EntitlementArn** *(string) --* The ARN of the entitlement that allows you to subscribe
        to content that comes from another AWS account. The entitlement is set by the content
        originator and the ARN is generated as part of the originator's flow.

        - **IngestIp** *(string) --* The IP address that the flow will be listening on for incoming
        content.

        - **IngestPort** *(integer) --* The port that the flow will be listening on for incoming
        content.

        - **Name** *(string) --* The name of the source.

        - **SourceArn** *(string) --* The ARN of the source.

        - **Transport** *(dict) --* Attributes related to the transport stream that are used in the
        source.

          - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
          initiate output requests to this flow. These IP addresses should be in the form of a
          Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

            - *(string) --*

          - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
          streams.

          - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter
          applies only to RIST-based and Zixi-based streams.

          - **Protocol** *(string) --* The protocol that is used by the source or output.

          - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

          - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST,
          RTP, and RTP-FEC streams.

          - **StreamId** *(string) --* The stream ID that you want to use for this transport. This
          parameter applies only to Zixi-based streams.

        - **WhitelistCidr** *(string) --* The range of IP addresses that should be allowed to
        contribute content to your source. These IP addresses should be in the form of a Classless
        Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

      - **Status** *(string) --* The current status of the flow.

    - **Messages** *(dict) --* Messages that provide the state of the flow.

      - **Errors** *(list) --* A list of errors that might have been generated from processes on
      this flow.

        - *(string) --*
    """


_RequiredClientGrantFlowEntitlementsEntitlementsTypeDef = TypedDict(
    "_RequiredClientGrantFlowEntitlementsEntitlementsTypeDef",
    {"Subscribers": List[Any]},
)
_OptionalClientGrantFlowEntitlementsEntitlementsTypeDef = TypedDict(
    "_OptionalClientGrantFlowEntitlementsEntitlementsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": Dict[str, Any],
        "Name": str,
    },
    total=False,
)


class ClientGrantFlowEntitlementsEntitlementsTypeDef(
    _RequiredClientGrantFlowEntitlementsEntitlementsTypeDef,
    _OptionalClientGrantFlowEntitlementsEntitlementsTypeDef,
):
    """
    Type definition for `ClientGrantFlowEntitlements` `Entitlements`

    - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
    transfer cost to be billed to the subscriber.

    - **Description** *(string) --* A description of the entitlement. This description appears only
    on the AWS Elemental MediaConnect console and will not be seen by the subscriber or end user.

    - **Encryption** *(dict) --* The type of encryption that will be used on the output that is
    associated with this entitlement.

      - **Algorithm** *(string) --* **[REQUIRED]** The type of algorithm that is used for the
      encryption (such as aes128, aes192, or aes256).

      - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented by
      a 32-character string, to be used with the key for encrypting content. This parameter is not
      valid for static key encryption.

      - **DeviceId** *(string) --* The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.

      - **KeyType** *(string) --* The type of key that is used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).

      - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created in.
      This parameter is required for SPEKE encryption and is not valid for static key encryption.

      - **ResourceId** *(string) --* An identifier for the content. The service sends this value to
      the key server to identify the current endpoint. The resource ID is also known as the content
      ID. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

      - **RoleArn** *(string) --* **[REQUIRED]** The ARN of the role that you created during setup
      (when you set up AWS Elemental MediaConnect as a trusted entity).

      - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets Manager
      to store the encryption key. This parameter is required for static key encryption and is not
      valid for SPEKE encryption.

      - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to your
      key server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

    - **Name** *(string) --* The name of the entitlement. This value must be unique within the
    current flow.

    - **Subscribers** *(list) --* **[REQUIRED]** The AWS account IDs that you want to share your
    content with. The receiving accounts (subscribers) will be allowed to create their own flows
    using your content as the source.

      - *(string) --*
    """


_ClientGrantFlowEntitlementsResponseEntitlementsTypeDef = TypedDict(
    "_ClientGrantFlowEntitlementsResponseEntitlementsTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": Dict[str, Any],
        "EntitlementArn": str,
        "Name": str,
        "Subscribers": List[Any],
    },
    total=False,
)


class ClientGrantFlowEntitlementsResponseEntitlementsTypeDef(
    _ClientGrantFlowEntitlementsResponseEntitlementsTypeDef
):
    """
    Type definition for `ClientGrantFlowEntitlementsResponse` `Entitlements`

    - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
    transfer cost to be billed to the subscriber.

    - **Description** *(string) --* A description of the entitlement.

    - **Encryption** *(dict) --* The type of encryption that will be used on the output that is
    associated with this entitlement.

      - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
      as aes128, aes192, or aes256).

      - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
      by a 32-character string, to be used with the key for encrypting content. This parameter
      is not valid for static key encryption.

      - **DeviceId** *(string) --* The value of one of the devices that you configured with
      your digital rights management (DRM) platform key provider. This parameter is required
      for SPEKE encryption and is not valid for static key encryption.

      - **KeyType** *(string) --* The type of key that is used for the encryption. If no
      keyType is provided, the service will use the default setting (static-key).

      - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
      in. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

      - **ResourceId** *(string) --* An identifier for the content. The service sends this
      value to the key server to identify the current endpoint. The resource ID is also known
      as the content ID. This parameter is required for SPEKE encryption and is not valid for
      static key encryption.

      - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
      set up AWS Elemental MediaConnect as a trusted entity).

      - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
      Manager to store the encryption key. This parameter is required for static key encryption
      and is not valid for SPEKE encryption.

      - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
      your key server. This parameter is required for SPEKE encryption and is not valid for
      static key encryption.

    - **EntitlementArn** *(string) --* The ARN of the entitlement.

    - **Name** *(string) --* The name of the entitlement.

    - **Subscribers** *(list) --* The AWS account IDs that you want to share your content with.
    The receiving accounts (subscribers) will be allowed to create their own flow using your
    content as the source.

      - *(string) --*
    """


_ClientGrantFlowEntitlementsResponseTypeDef = TypedDict(
    "_ClientGrantFlowEntitlementsResponseTypeDef",
    {
        "Entitlements": List[ClientGrantFlowEntitlementsResponseEntitlementsTypeDef],
        "FlowArn": str,
    },
    total=False,
)


class ClientGrantFlowEntitlementsResponseTypeDef(
    _ClientGrantFlowEntitlementsResponseTypeDef
):
    """
    Type definition for `ClientGrantFlowEntitlements` `Response`

    - **Entitlements** *(list) --* The entitlements that were just granted.

      - *(dict) --* The settings for a flow entitlement.

        - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
        transfer cost to be billed to the subscriber.

        - **Description** *(string) --* A description of the entitlement.

        - **Encryption** *(dict) --* The type of encryption that will be used on the output that is
        associated with this entitlement.

          - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
          as aes128, aes192, or aes256).

          - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
          by a 32-character string, to be used with the key for encrypting content. This parameter
          is not valid for static key encryption.

          - **DeviceId** *(string) --* The value of one of the devices that you configured with
          your digital rights management (DRM) platform key provider. This parameter is required
          for SPEKE encryption and is not valid for static key encryption.

          - **KeyType** *(string) --* The type of key that is used for the encryption. If no
          keyType is provided, the service will use the default setting (static-key).

          - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
          in. This parameter is required for SPEKE encryption and is not valid for static key
          encryption.

          - **ResourceId** *(string) --* An identifier for the content. The service sends this
          value to the key server to identify the current endpoint. The resource ID is also known
          as the content ID. This parameter is required for SPEKE encryption and is not valid for
          static key encryption.

          - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you
          set up AWS Elemental MediaConnect as a trusted entity).

          - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets
          Manager to store the encryption key. This parameter is required for static key encryption
          and is not valid for SPEKE encryption.

          - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to
          your key server. This parameter is required for SPEKE encryption and is not valid for
          static key encryption.

        - **EntitlementArn** *(string) --* The ARN of the entitlement.

        - **Name** *(string) --* The name of the entitlement.

        - **Subscribers** *(list) --* The AWS account IDs that you want to share your content with.
        The receiving accounts (subscribers) will be allowed to create their own flow using your
        content as the source.

          - *(string) --*

    - **FlowArn** *(string) --* The ARN of the flow that these entitlements were granted to.
    """


_ClientListEntitlementsResponseTypeDef = TypedDict(
    "_ClientListEntitlementsResponseTypeDef",
    {"Entitlements": List[Any], "NextToken": str},
    total=False,
)


class ClientListEntitlementsResponseTypeDef(_ClientListEntitlementsResponseTypeDef):
    """
    Type definition for `ClientListEntitlements` `Response`

    - **Entitlements** *(list) --* A list of entitlements that have been granted to you from other
    AWS accounts.

      - *(dict) --* An entitlement that has been granted to you from other AWS accounts.

        - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
        transfer cost to be billed to the subscriber.

        - **EntitlementArn** *(string) --* The ARN of the entitlement.

        - **EntitlementName** *(string) --* The name of the entitlement.

    - **NextToken** *(string) --* The token that identifies which batch of results that you want to
    see. For example, you submit a ListEntitlements request with MaxResults set at 5. The service
    returns the first batch of results (up to 5) and a NextToken value. To see the next batch of
    results, you can submit the ListEntitlements request a second time and specify the NextToken
    value.
    """


_ClientListFlowsResponseTypeDef = TypedDict(
    "_ClientListFlowsResponseTypeDef",
    {"Flows": List[Dict], "NextToken": str},
    total=False,
)


class ClientListFlowsResponseTypeDef(_ClientListFlowsResponseTypeDef):
    """
    Type definition for `ClientListFlows` `Response`

    - **Flows** *(list) --* A list of flow summaries.

      - *(dict) --* Provides a summary of a flow, including its ARN, Availability Zone, and source
      type.

        - **AvailabilityZone** *(string) --* The Availability Zone that the flow was created in.

        - **Description** *(string) --* A description of the flow.

        - **FlowArn** *(string) --* The ARN of the flow.

        - **Name** *(string) --* The name of the flow.

        - **SourceType** *(string) --* The type of source. This value is either owned (originated
        somewhere other than an AWS Elemental MediaConnect flow owned by another AWS account) or
        entitled (originated at an AWS Elemental MediaConnect flow owned by another AWS account).

        - **Status** *(string) --* The current status of the flow.

    - **NextToken** *(string) --* The token that identifies which batch of results that you want to
    see. For example, you submit a ListFlows request with MaxResults set at 5. The service returns
    the first batch of results (up to 5) and a NextToken value. To see the next batch of results,
    you can submit the ListFlows request a second time and specify the NextToken value.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, Any]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **Tags** *(dict) --* A map from tag keys to values. Tag keys can have a maximum character
    length of 128 characters, and tag values can have a maximum length of 256 characters.

      - *(string) --*

        - *(string) --*
    """


_ClientRemoveFlowOutputResponseTypeDef = TypedDict(
    "_ClientRemoveFlowOutputResponseTypeDef",
    {"FlowArn": str, "OutputArn": str},
    total=False,
)


class ClientRemoveFlowOutputResponseTypeDef(_ClientRemoveFlowOutputResponseTypeDef):
    """
    Type definition for `ClientRemoveFlowOutput` `Response`

    - **FlowArn** *(string) --* The ARN of the flow that is associated with the output you removed.

    - **OutputArn** *(string) --* The ARN of the output that was removed.
    """


_ClientRevokeFlowEntitlementResponseTypeDef = TypedDict(
    "_ClientRevokeFlowEntitlementResponseTypeDef",
    {"EntitlementArn": str, "FlowArn": str},
    total=False,
)


class ClientRevokeFlowEntitlementResponseTypeDef(
    _ClientRevokeFlowEntitlementResponseTypeDef
):
    """
    Type definition for `ClientRevokeFlowEntitlement` `Response`

    - **EntitlementArn** *(string) --* The ARN of the entitlement that was revoked.

    - **FlowArn** *(string) --* The ARN of the flow that the entitlement was revoked from.
    """


_ClientStartFlowResponseTypeDef = TypedDict(
    "_ClientStartFlowResponseTypeDef", {"FlowArn": str, "Status": str}, total=False
)


class ClientStartFlowResponseTypeDef(_ClientStartFlowResponseTypeDef):
    """
    Type definition for `ClientStartFlow` `Response`

    - **FlowArn** *(string) --* The ARN of the flow that you started.

    - **Status** *(string) --* The status of the flow when the StartFlow process begins.
    """


_ClientStopFlowResponseTypeDef = TypedDict(
    "_ClientStopFlowResponseTypeDef", {"FlowArn": str, "Status": str}, total=False
)


class ClientStopFlowResponseTypeDef(_ClientStopFlowResponseTypeDef):
    """
    Type definition for `ClientStopFlow` `Response`

    - **FlowArn** *(string) --* The ARN of the flow that you stopped.

    - **Status** *(string) --* The status of the flow when the StopFlow process begins.
    """


_ClientUpdateFlowEntitlementResponseEntitlementTypeDef = TypedDict(
    "_ClientUpdateFlowEntitlementResponseEntitlementTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Encryption": Dict[str, Any],
        "EntitlementArn": str,
        "Name": str,
        "Subscribers": List[Any],
    },
    total=False,
)


class ClientUpdateFlowEntitlementResponseEntitlementTypeDef(
    _ClientUpdateFlowEntitlementResponseEntitlementTypeDef
):
    """
    Type definition for `ClientUpdateFlowEntitlementResponse` `Entitlement`

    - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
    transfer cost to be billed to the subscriber.

    - **Description** *(string) --* A description of the entitlement.

    - **Encryption** *(dict) --* The type of encryption that will be used on the output that is
    associated with this entitlement.

      - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
      as aes128, aes192, or aes256).

      - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
      by a 32-character string, to be used with the key for encrypting content. This parameter is
      not valid for static key encryption.

      - **DeviceId** *(string) --* The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.

      - **KeyType** *(string) --* The type of key that is used for the encryption. If no keyType
      is provided, the service will use the default setting (static-key).

      - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
      in. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

      - **ResourceId** *(string) --* An identifier for the content. The service sends this value
      to the key server to identify the current endpoint. The resource ID is also known as the
      content ID. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

      - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you set
      up AWS Elemental MediaConnect as a trusted entity).

      - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets Manager
      to store the encryption key. This parameter is required for static key encryption and is
      not valid for SPEKE encryption.

      - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to your
      key server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

    - **EntitlementArn** *(string) --* The ARN of the entitlement.

    - **Name** *(string) --* The name of the entitlement.

    - **Subscribers** *(list) --* The AWS account IDs that you want to share your content with.
    The receiving accounts (subscribers) will be allowed to create their own flow using your
    content as the source.

      - *(string) --*
    """


_ClientUpdateFlowEntitlementResponseTypeDef = TypedDict(
    "_ClientUpdateFlowEntitlementResponseTypeDef",
    {
        "Entitlement": ClientUpdateFlowEntitlementResponseEntitlementTypeDef,
        "FlowArn": str,
    },
    total=False,
)


class ClientUpdateFlowEntitlementResponseTypeDef(
    _ClientUpdateFlowEntitlementResponseTypeDef
):
    """
    Type definition for `ClientUpdateFlowEntitlement` `Response`

    - **Entitlement** *(dict) --* The settings for a flow entitlement.

      - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
      transfer cost to be billed to the subscriber.

      - **Description** *(string) --* A description of the entitlement.

      - **Encryption** *(dict) --* The type of encryption that will be used on the output that is
      associated with this entitlement.

        - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
        as aes128, aes192, or aes256).

        - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
        by a 32-character string, to be used with the key for encrypting content. This parameter is
        not valid for static key encryption.

        - **DeviceId** *(string) --* The value of one of the devices that you configured with your
        digital rights management (DRM) platform key provider. This parameter is required for SPEKE
        encryption and is not valid for static key encryption.

        - **KeyType** *(string) --* The type of key that is used for the encryption. If no keyType
        is provided, the service will use the default setting (static-key).

        - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
        in. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.

        - **ResourceId** *(string) --* An identifier for the content. The service sends this value
        to the key server to identify the current endpoint. The resource ID is also known as the
        content ID. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.

        - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you set
        up AWS Elemental MediaConnect as a trusted entity).

        - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets Manager
        to store the encryption key. This parameter is required for static key encryption and is
        not valid for SPEKE encryption.

        - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to your
        key server. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.

      - **EntitlementArn** *(string) --* The ARN of the entitlement.

      - **Name** *(string) --* The name of the entitlement.

      - **Subscribers** *(list) --* The AWS account IDs that you want to share your content with.
      The receiving accounts (subscribers) will be allowed to create their own flow using your
      content as the source.

        - *(string) --*

    - **FlowArn** *(string) --* The ARN of the flow that this entitlement was granted on.
    """


_ClientUpdateFlowOutputResponseOutputTypeDef = TypedDict(
    "_ClientUpdateFlowOutputResponseOutputTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Description": str,
        "Destination": str,
        "Encryption": Dict[str, Any],
        "EntitlementArn": str,
        "MediaLiveInputArn": str,
        "Name": str,
        "OutputArn": str,
        "Port": int,
        "Transport": Dict[str, Any],
    },
    total=False,
)


class ClientUpdateFlowOutputResponseOutputTypeDef(
    _ClientUpdateFlowOutputResponseOutputTypeDef
):
    """
    Type definition for `ClientUpdateFlowOutputResponse` `Output`

    - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
    transfer cost to be billed to the subscriber.

    - **Description** *(string) --* A description of the output.

    - **Destination** *(string) --* The address where you want to send the output.

    - **Encryption** *(dict) --* The type of key used for the encryption. If no keyType is
    provided, the service will use the default setting (static-key).

      - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
      as aes128, aes192, or aes256).

      - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
      by a 32-character string, to be used with the key for encrypting content. This parameter is
      not valid for static key encryption.

      - **DeviceId** *(string) --* The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.

      - **KeyType** *(string) --* The type of key that is used for the encryption. If no keyType
      is provided, the service will use the default setting (static-key).

      - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
      in. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

      - **ResourceId** *(string) --* An identifier for the content. The service sends this value
      to the key server to identify the current endpoint. The resource ID is also known as the
      content ID. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

      - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you set
      up AWS Elemental MediaConnect as a trusted entity).

      - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets Manager
      to store the encryption key. This parameter is required for static key encryption and is
      not valid for SPEKE encryption.

      - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to your
      key server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

    - **EntitlementArn** *(string) --* The ARN of the entitlement on the originator''s flow. This
    value is relevant only on entitled flows.

    - **MediaLiveInputArn** *(string) --* The input ARN of the AWS Elemental MediaLive channel.
    This parameter is relevant only for outputs that were added by creating a MediaLive input.

    - **Name** *(string) --* The name of the output. This value must be unique within the current
    flow.

    - **OutputArn** *(string) --* The ARN of the output.

    - **Port** *(integer) --* The port to use when content is distributed to this output.

    - **Transport** *(dict) --* Attributes related to the transport stream that are used in the
    output.

      - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
      initiate output requests to this flow. These IP addresses should be in the form of a
      Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

        - *(string) --*

      - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
      streams.

      - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter applies
      only to RIST-based and Zixi-based streams.

      - **Protocol** *(string) --* The protocol that is used by the source or output.

      - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

      - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST, RTP,
      and RTP-FEC streams.

      - **StreamId** *(string) --* The stream ID that you want to use for this transport. This
      parameter applies only to Zixi-based streams.
    """


_ClientUpdateFlowOutputResponseTypeDef = TypedDict(
    "_ClientUpdateFlowOutputResponseTypeDef",
    {"FlowArn": str, "Output": ClientUpdateFlowOutputResponseOutputTypeDef},
    total=False,
)


class ClientUpdateFlowOutputResponseTypeDef(_ClientUpdateFlowOutputResponseTypeDef):
    """
    Type definition for `ClientUpdateFlowOutput` `Response`

    - **FlowArn** *(string) --* The ARN of the flow that is associated with the updated output.

    - **Output** *(dict) --* The settings for an output.

      - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
      transfer cost to be billed to the subscriber.

      - **Description** *(string) --* A description of the output.

      - **Destination** *(string) --* The address where you want to send the output.

      - **Encryption** *(dict) --* The type of key used for the encryption. If no keyType is
      provided, the service will use the default setting (static-key).

        - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
        as aes128, aes192, or aes256).

        - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
        by a 32-character string, to be used with the key for encrypting content. This parameter is
        not valid for static key encryption.

        - **DeviceId** *(string) --* The value of one of the devices that you configured with your
        digital rights management (DRM) platform key provider. This parameter is required for SPEKE
        encryption and is not valid for static key encryption.

        - **KeyType** *(string) --* The type of key that is used for the encryption. If no keyType
        is provided, the service will use the default setting (static-key).

        - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
        in. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.

        - **ResourceId** *(string) --* An identifier for the content. The service sends this value
        to the key server to identify the current endpoint. The resource ID is also known as the
        content ID. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.

        - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you set
        up AWS Elemental MediaConnect as a trusted entity).

        - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets Manager
        to store the encryption key. This parameter is required for static key encryption and is
        not valid for SPEKE encryption.

        - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to your
        key server. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.

      - **EntitlementArn** *(string) --* The ARN of the entitlement on the originator''s flow. This
      value is relevant only on entitled flows.

      - **MediaLiveInputArn** *(string) --* The input ARN of the AWS Elemental MediaLive channel.
      This parameter is relevant only for outputs that were added by creating a MediaLive input.

      - **Name** *(string) --* The name of the output. This value must be unique within the current
      flow.

      - **OutputArn** *(string) --* The ARN of the output.

      - **Port** *(integer) --* The port to use when content is distributed to this output.

      - **Transport** *(dict) --* Attributes related to the transport stream that are used in the
      output.

        - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
        initiate output requests to this flow. These IP addresses should be in the form of a
        Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

          - *(string) --*

        - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
        streams.

        - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter applies
        only to RIST-based and Zixi-based streams.

        - **Protocol** *(string) --* The protocol that is used by the source or output.

        - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

        - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST, RTP,
        and RTP-FEC streams.

        - **StreamId** *(string) --* The stream ID that you want to use for this transport. This
        parameter applies only to Zixi-based streams.
    """


_ClientUpdateFlowSourceDecryptionTypeDef = TypedDict(
    "_ClientUpdateFlowSourceDecryptionTypeDef",
    {
        "Algorithm": str,
        "ConstantInitializationVector": str,
        "DeviceId": str,
        "KeyType": str,
        "Region": str,
        "ResourceId": str,
        "RoleArn": str,
        "SecretArn": str,
        "Url": str,
    },
    total=False,
)


class ClientUpdateFlowSourceDecryptionTypeDef(_ClientUpdateFlowSourceDecryptionTypeDef):
    """
    Type definition for `ClientUpdateFlowSource` `Decryption`

    - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such as
    aes128, aes192, or aes256).

    - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented by a
    32-character string, to be used with the key for encrypting content. This parameter is not valid
    for static key encryption.

    - **DeviceId** *(string) --* The value of one of the devices that you configured with your
    digital rights management (DRM) platform key provider. This parameter is required for SPEKE
    encryption and is not valid for static key encryption.

    - **KeyType** *(string) --* The type of key that is used for the encryption. If no keyType is
    provided, the service will use the default setting (static-key).

    - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created in.
    This parameter is required for SPEKE encryption and is not valid for static key encryption.

    - **ResourceId** *(string) --* An identifier for the content. The service sends this value to the
    key server to identify the current endpoint. The resource ID is also known as the content ID.
    This parameter is required for SPEKE encryption and is not valid for static key encryption.

    - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you set up
    AWS Elemental MediaConnect as a trusted entity).

    - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets Manager to
    store the encryption key. This parameter is required for static key encryption and is not valid
    for SPEKE encryption.

    - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to your key
    server. This parameter is required for SPEKE encryption and is not valid for static key
    encryption.
    """


_ClientUpdateFlowSourceResponseSourceTypeDef = TypedDict(
    "_ClientUpdateFlowSourceResponseSourceTypeDef",
    {
        "DataTransferSubscriberFeePercent": int,
        "Decryption": Dict[str, Any],
        "Description": str,
        "EntitlementArn": str,
        "IngestIp": str,
        "IngestPort": int,
        "Name": str,
        "SourceArn": str,
        "Transport": Dict[str, Any],
        "WhitelistCidr": str,
    },
    total=False,
)


class ClientUpdateFlowSourceResponseSourceTypeDef(
    _ClientUpdateFlowSourceResponseSourceTypeDef
):
    """
    Type definition for `ClientUpdateFlowSourceResponse` `Source`

    - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
    transfer cost to be billed to the subscriber.

    - **Decryption** *(dict) --* The type of encryption that is used on the content ingested from
    this source.

      - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
      as aes128, aes192, or aes256).

      - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
      by a 32-character string, to be used with the key for encrypting content. This parameter is
      not valid for static key encryption.

      - **DeviceId** *(string) --* The value of one of the devices that you configured with your
      digital rights management (DRM) platform key provider. This parameter is required for SPEKE
      encryption and is not valid for static key encryption.

      - **KeyType** *(string) --* The type of key that is used for the encryption. If no keyType
      is provided, the service will use the default setting (static-key).

      - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
      in. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

      - **ResourceId** *(string) --* An identifier for the content. The service sends this value
      to the key server to identify the current endpoint. The resource ID is also known as the
      content ID. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

      - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you set
      up AWS Elemental MediaConnect as a trusted entity).

      - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets Manager
      to store the encryption key. This parameter is required for static key encryption and is
      not valid for SPEKE encryption.

      - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to your
      key server. This parameter is required for SPEKE encryption and is not valid for static key
      encryption.

    - **Description** *(string) --* A description for the source. This value is not used or seen
    outside of the current AWS Elemental MediaConnect account.

    - **EntitlementArn** *(string) --* The ARN of the entitlement that allows you to subscribe to
    content that comes from another AWS account. The entitlement is set by the content originator
    and the ARN is generated as part of the originator's flow.

    - **IngestIp** *(string) --* The IP address that the flow will be listening on for incoming
    content.

    - **IngestPort** *(integer) --* The port that the flow will be listening on for incoming
    content.

    - **Name** *(string) --* The name of the source.

    - **SourceArn** *(string) --* The ARN of the source.

    - **Transport** *(dict) --* Attributes related to the transport stream that are used in the
    source.

      - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
      initiate output requests to this flow. These IP addresses should be in the form of a
      Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

        - *(string) --*

      - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
      streams.

      - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter applies
      only to RIST-based and Zixi-based streams.

      - **Protocol** *(string) --* The protocol that is used by the source or output.

      - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

      - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST, RTP,
      and RTP-FEC streams.

      - **StreamId** *(string) --* The stream ID that you want to use for this transport. This
      parameter applies only to Zixi-based streams.

    - **WhitelistCidr** *(string) --* The range of IP addresses that should be allowed to
    contribute content to your source. These IP addresses should be in the form of a Classless
    Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    """


_ClientUpdateFlowSourceResponseTypeDef = TypedDict(
    "_ClientUpdateFlowSourceResponseTypeDef",
    {"FlowArn": str, "Source": ClientUpdateFlowSourceResponseSourceTypeDef},
    total=False,
)


class ClientUpdateFlowSourceResponseTypeDef(_ClientUpdateFlowSourceResponseTypeDef):
    """
    Type definition for `ClientUpdateFlowSource` `Response`

    - **FlowArn** *(string) --* The ARN of the flow that you want to update.

    - **Source** *(dict) --* The settings for the source of the flow.

      - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
      transfer cost to be billed to the subscriber.

      - **Decryption** *(dict) --* The type of encryption that is used on the content ingested from
      this source.

        - **Algorithm** *(string) --* The type of algorithm that is used for the encryption (such
        as aes128, aes192, or aes256).

        - **ConstantInitializationVector** *(string) --* A 128-bit, 16-byte hex value represented
        by a 32-character string, to be used with the key for encrypting content. This parameter is
        not valid for static key encryption.

        - **DeviceId** *(string) --* The value of one of the devices that you configured with your
        digital rights management (DRM) platform key provider. This parameter is required for SPEKE
        encryption and is not valid for static key encryption.

        - **KeyType** *(string) --* The type of key that is used for the encryption. If no keyType
        is provided, the service will use the default setting (static-key).

        - **Region** *(string) --* The AWS Region that the API Gateway proxy endpoint was created
        in. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.

        - **ResourceId** *(string) --* An identifier for the content. The service sends this value
        to the key server to identify the current endpoint. The resource ID is also known as the
        content ID. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.

        - **RoleArn** *(string) --* The ARN of the role that you created during setup (when you set
        up AWS Elemental MediaConnect as a trusted entity).

        - **SecretArn** *(string) --* The ARN of the secret that you created in AWS Secrets Manager
        to store the encryption key. This parameter is required for static key encryption and is
        not valid for SPEKE encryption.

        - **Url** *(string) --* The URL from the API Gateway proxy that you set up to talk to your
        key server. This parameter is required for SPEKE encryption and is not valid for static key
        encryption.

      - **Description** *(string) --* A description for the source. This value is not used or seen
      outside of the current AWS Elemental MediaConnect account.

      - **EntitlementArn** *(string) --* The ARN of the entitlement that allows you to subscribe to
      content that comes from another AWS account. The entitlement is set by the content originator
      and the ARN is generated as part of the originator's flow.

      - **IngestIp** *(string) --* The IP address that the flow will be listening on for incoming
      content.

      - **IngestPort** *(integer) --* The port that the flow will be listening on for incoming
      content.

      - **Name** *(string) --* The name of the source.

      - **SourceArn** *(string) --* The ARN of the source.

      - **Transport** *(dict) --* Attributes related to the transport stream that are used in the
      source.

        - **CidrAllowList** *(list) --* The range of IP addresses that should be allowed to
        initiate output requests to this flow. These IP addresses should be in the form of a
        Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

          - *(string) --*

        - **MaxBitrate** *(integer) --* The smoothing max bitrate for RIST, RTP, and RTP-FEC
        streams.

        - **MaxLatency** *(integer) --* The maximum latency in milliseconds. This parameter applies
        only to RIST-based and Zixi-based streams.

        - **Protocol** *(string) --* The protocol that is used by the source or output.

        - **RemoteId** *(string) --* The remote ID for the Zixi-pull stream.

        - **SmoothingLatency** *(integer) --* The smoothing latency in milliseconds for RIST, RTP,
        and RTP-FEC streams.

        - **StreamId** *(string) --* The stream ID that you want to use for this transport. This
        parameter applies only to Zixi-based streams.

      - **WhitelistCidr** *(string) --* The range of IP addresses that should be allowed to
      contribute content to your source. These IP addresses should be in the form of a Classless
      Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
    """


_ListEntitlementsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListEntitlementsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListEntitlementsPaginatePaginationConfigTypeDef(
    _ListEntitlementsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListEntitlementsPaginate` `PaginationConfig`

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


_ListEntitlementsPaginateResponseTypeDef = TypedDict(
    "_ListEntitlementsPaginateResponseTypeDef", {"Entitlements": List[Any]}, total=False
)


class ListEntitlementsPaginateResponseTypeDef(_ListEntitlementsPaginateResponseTypeDef):
    """
    Type definition for `ListEntitlementsPaginate` `Response`

    - **Entitlements** *(list) --* A list of entitlements that have been granted to you from other
    AWS accounts.

      - *(dict) --* An entitlement that has been granted to you from other AWS accounts.

        - **DataTransferSubscriberFeePercent** *(integer) --* Percentage from 0-100 of the data
        transfer cost to be billed to the subscriber.

        - **EntitlementArn** *(string) --* The ARN of the entitlement.

        - **EntitlementName** *(string) --* The name of the entitlement.
    """


_ListFlowsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListFlowsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListFlowsPaginatePaginationConfigTypeDef(
    _ListFlowsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListFlowsPaginate` `PaginationConfig`

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


_ListFlowsPaginateResponseTypeDef = TypedDict(
    "_ListFlowsPaginateResponseTypeDef", {"Flows": List[Dict]}, total=False
)


class ListFlowsPaginateResponseTypeDef(_ListFlowsPaginateResponseTypeDef):
    """
    Type definition for `ListFlowsPaginate` `Response`

    - **Flows** *(list) --* A list of flow summaries.

      - *(dict) --* Provides a summary of a flow, including its ARN, Availability Zone, and source
      type.

        - **AvailabilityZone** *(string) --* The Availability Zone that the flow was created in.

        - **Description** *(string) --* A description of the flow.

        - **FlowArn** *(string) --* The ARN of the flow.

        - **Name** *(string) --* The name of the flow.

        - **SourceType** *(string) --* The type of source. This value is either owned (originated
        somewhere other than an AWS Elemental MediaConnect flow owned by another AWS account) or
        entitled (originated at an AWS Elemental MediaConnect flow owned by another AWS account).

        - **Status** *(string) --* The current status of the flow.
    """

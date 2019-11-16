"Main interface for shield type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateProtectionResponseTypeDef",
    "ClientDescribeAttackResponseAttackAttackCountersTypeDef",
    "ClientDescribeAttackResponseAttackAttackPropertiesTopContributorsTypeDef",
    "ClientDescribeAttackResponseAttackAttackPropertiesTypeDef",
    "ClientDescribeAttackResponseAttackMitigationsTypeDef",
    "ClientDescribeAttackResponseAttackSubResourcesAttackVectorsVectorCountersTypeDef",
    "ClientDescribeAttackResponseAttackSubResourcesAttackVectorsTypeDef",
    "ClientDescribeAttackResponseAttackSubResourcesCountersTypeDef",
    "ClientDescribeAttackResponseAttackSubResourcesTypeDef",
    "ClientDescribeAttackResponseAttackTypeDef",
    "ClientDescribeAttackResponseTypeDef",
    "ClientDescribeDrtAccessResponseTypeDef",
    "ClientDescribeEmergencyContactSettingsResponseEmergencyContactListTypeDef",
    "ClientDescribeEmergencyContactSettingsResponseTypeDef",
    "ClientDescribeProtectionResponseProtectionTypeDef",
    "ClientDescribeProtectionResponseTypeDef",
    "ClientDescribeSubscriptionResponseSubscriptionLimitsTypeDef",
    "ClientDescribeSubscriptionResponseSubscriptionTypeDef",
    "ClientDescribeSubscriptionResponseTypeDef",
    "ClientGetSubscriptionStateResponseTypeDef",
    "ClientListAttacksEndTimeTypeDef",
    "ClientListAttacksResponseAttackSummariesAttackVectorsTypeDef",
    "ClientListAttacksResponseAttackSummariesTypeDef",
    "ClientListAttacksResponseTypeDef",
    "ClientListAttacksStartTimeTypeDef",
    "ClientListProtectionsResponseProtectionsTypeDef",
    "ClientListProtectionsResponseTypeDef",
    "ClientUpdateEmergencyContactSettingsEmergencyContactListTypeDef",
    "ListAttacksPaginateEndTimeTypeDef",
    "ListAttacksPaginatePaginationConfigTypeDef",
    "ListAttacksPaginateResponseAttackSummariesAttackVectorsTypeDef",
    "ListAttacksPaginateResponseAttackSummariesTypeDef",
    "ListAttacksPaginateResponseTypeDef",
    "ListAttacksPaginateStartTimeTypeDef",
    "ListProtectionsPaginatePaginationConfigTypeDef",
    "ListProtectionsPaginateResponseProtectionsTypeDef",
    "ListProtectionsPaginateResponseTypeDef",
)


_ClientCreateProtectionResponseTypeDef = TypedDict(
    "_ClientCreateProtectionResponseTypeDef", {"ProtectionId": str}, total=False
)


class ClientCreateProtectionResponseTypeDef(_ClientCreateProtectionResponseTypeDef):
    """
    Type definition for `ClientCreateProtection` `Response`

    - **ProtectionId** *(string) --*

      The unique identifier (ID) for the  Protection object that is created.
    """


_ClientDescribeAttackResponseAttackAttackCountersTypeDef = TypedDict(
    "_ClientDescribeAttackResponseAttackAttackCountersTypeDef",
    {"Name": str, "Max": float, "Average": float, "Sum": float, "N": int, "Unit": str},
    total=False,
)


class ClientDescribeAttackResponseAttackAttackCountersTypeDef(
    _ClientDescribeAttackResponseAttackAttackCountersTypeDef
):
    """
    Type definition for `ClientDescribeAttackResponseAttack` `AttackCounters`

    The counter that describes a DDoS attack.

    - **Name** *(string) --*

      The counter name.

    - **Max** *(float) --*

      The maximum value of the counter for a specified time period.

    - **Average** *(float) --*

      The average value of the counter for a specified time period.

    - **Sum** *(float) --*

      The total of counter values for a specified time period.

    - **N** *(integer) --*

      The number of counters for a specified time period.

    - **Unit** *(string) --*

      The unit of the counters.
    """


_ClientDescribeAttackResponseAttackAttackPropertiesTopContributorsTypeDef = TypedDict(
    "_ClientDescribeAttackResponseAttackAttackPropertiesTopContributorsTypeDef",
    {"Name": str, "Value": int},
    total=False,
)


class ClientDescribeAttackResponseAttackAttackPropertiesTopContributorsTypeDef(
    _ClientDescribeAttackResponseAttackAttackPropertiesTopContributorsTypeDef
):
    """
    Type definition for `ClientDescribeAttackResponseAttackAttackProperties` `TopContributors`

    A contributor to the attack and their contribution.

    - **Name** *(string) --*

      The name of the contributor. This is dependent on the ``AttackPropertyIdentifier``
      . For example, if the ``AttackPropertyIdentifier`` is ``SOURCE_COUNTRY`` , the
      ``Name`` could be ``United States`` .

    - **Value** *(integer) --*

      The contribution of this contributor expressed in  Protection units. For example
      ``10,000`` .
    """


_ClientDescribeAttackResponseAttackAttackPropertiesTypeDef = TypedDict(
    "_ClientDescribeAttackResponseAttackAttackPropertiesTypeDef",
    {
        "AttackLayer": str,
        "AttackPropertyIdentifier": str,
        "TopContributors": List[
            ClientDescribeAttackResponseAttackAttackPropertiesTopContributorsTypeDef
        ],
        "Unit": str,
        "Total": int,
    },
    total=False,
)


class ClientDescribeAttackResponseAttackAttackPropertiesTypeDef(
    _ClientDescribeAttackResponseAttackAttackPropertiesTypeDef
):
    """
    Type definition for `ClientDescribeAttackResponseAttack` `AttackProperties`

    Details of the described attack.

    - **AttackLayer** *(string) --*

      The type of distributed denial of service (DDoS) event that was observed. ``NETWORK``
      indicates layer 3 and layer 4 events and ``APPLICATION`` indicates layer 7 events.

    - **AttackPropertyIdentifier** *(string) --*

      Defines the DDoS attack property information that is provided. The
      ``WORDPRESS_PINGBACK_REFLECTOR`` and ``WORDPRESS_PINGBACK_SOURCE`` values are valid
      only for WordPress reflective pingback DDoS attacks.

    - **TopContributors** *(list) --*

      The array of  Contributor objects that includes the top five contributors to an attack.

      - *(dict) --*

        A contributor to the attack and their contribution.

        - **Name** *(string) --*

          The name of the contributor. This is dependent on the ``AttackPropertyIdentifier``
          . For example, if the ``AttackPropertyIdentifier`` is ``SOURCE_COUNTRY`` , the
          ``Name`` could be ``United States`` .

        - **Value** *(integer) --*

          The contribution of this contributor expressed in  Protection units. For example
          ``10,000`` .

    - **Unit** *(string) --*

      The unit of the ``Value`` of the contributions.

    - **Total** *(integer) --*

      The total contributions made to this attack by all contributors, not just the five
      listed in the ``TopContributors`` list.
    """


_ClientDescribeAttackResponseAttackMitigationsTypeDef = TypedDict(
    "_ClientDescribeAttackResponseAttackMitigationsTypeDef",
    {"MitigationName": str},
    total=False,
)


class ClientDescribeAttackResponseAttackMitigationsTypeDef(
    _ClientDescribeAttackResponseAttackMitigationsTypeDef
):
    """
    Type definition for `ClientDescribeAttackResponseAttack` `Mitigations`

    The mitigation applied to a DDoS attack.

    - **MitigationName** *(string) --*

      The name of the mitigation taken for this attack.
    """


_ClientDescribeAttackResponseAttackSubResourcesAttackVectorsVectorCountersTypeDef = TypedDict(
    "_ClientDescribeAttackResponseAttackSubResourcesAttackVectorsVectorCountersTypeDef",
    {"Name": str, "Max": float, "Average": float, "Sum": float, "N": int, "Unit": str},
    total=False,
)


class ClientDescribeAttackResponseAttackSubResourcesAttackVectorsVectorCountersTypeDef(
    _ClientDescribeAttackResponseAttackSubResourcesAttackVectorsVectorCountersTypeDef
):
    """
    Type definition for `ClientDescribeAttackResponseAttackSubResourcesAttackVectors` `VectorCounters`

    The counter that describes a DDoS attack.

    - **Name** *(string) --*

      The counter name.

    - **Max** *(float) --*

      The maximum value of the counter for a specified time period.

    - **Average** *(float) --*

      The average value of the counter for a specified time period.

    - **Sum** *(float) --*

      The total of counter values for a specified time period.

    - **N** *(integer) --*

      The number of counters for a specified time period.

    - **Unit** *(string) --*

      The unit of the counters.
    """


_ClientDescribeAttackResponseAttackSubResourcesAttackVectorsTypeDef = TypedDict(
    "_ClientDescribeAttackResponseAttackSubResourcesAttackVectorsTypeDef",
    {
        "VectorType": str,
        "VectorCounters": List[
            ClientDescribeAttackResponseAttackSubResourcesAttackVectorsVectorCountersTypeDef
        ],
    },
    total=False,
)


class ClientDescribeAttackResponseAttackSubResourcesAttackVectorsTypeDef(
    _ClientDescribeAttackResponseAttackSubResourcesAttackVectorsTypeDef
):
    """
    Type definition for `ClientDescribeAttackResponseAttackSubResources` `AttackVectors`

    A summary of information about the attack.

    - **VectorType** *(string) --*

      The attack type, for example, SNMP reflection or SYN flood.

    - **VectorCounters** *(list) --*

      The list of counters that describe the details of the attack.

      - *(dict) --*

        The counter that describes a DDoS attack.

        - **Name** *(string) --*

          The counter name.

        - **Max** *(float) --*

          The maximum value of the counter for a specified time period.

        - **Average** *(float) --*

          The average value of the counter for a specified time period.

        - **Sum** *(float) --*

          The total of counter values for a specified time period.

        - **N** *(integer) --*

          The number of counters for a specified time period.

        - **Unit** *(string) --*

          The unit of the counters.
    """


_ClientDescribeAttackResponseAttackSubResourcesCountersTypeDef = TypedDict(
    "_ClientDescribeAttackResponseAttackSubResourcesCountersTypeDef",
    {"Name": str, "Max": float, "Average": float, "Sum": float, "N": int, "Unit": str},
    total=False,
)


class ClientDescribeAttackResponseAttackSubResourcesCountersTypeDef(
    _ClientDescribeAttackResponseAttackSubResourcesCountersTypeDef
):
    """
    Type definition for `ClientDescribeAttackResponseAttackSubResources` `Counters`

    The counter that describes a DDoS attack.

    - **Name** *(string) --*

      The counter name.

    - **Max** *(float) --*

      The maximum value of the counter for a specified time period.

    - **Average** *(float) --*

      The average value of the counter for a specified time period.

    - **Sum** *(float) --*

      The total of counter values for a specified time period.

    - **N** *(integer) --*

      The number of counters for a specified time period.

    - **Unit** *(string) --*

      The unit of the counters.
    """


_ClientDescribeAttackResponseAttackSubResourcesTypeDef = TypedDict(
    "_ClientDescribeAttackResponseAttackSubResourcesTypeDef",
    {
        "Type": str,
        "Id": str,
        "AttackVectors": List[
            ClientDescribeAttackResponseAttackSubResourcesAttackVectorsTypeDef
        ],
        "Counters": List[ClientDescribeAttackResponseAttackSubResourcesCountersTypeDef],
    },
    total=False,
)


class ClientDescribeAttackResponseAttackSubResourcesTypeDef(
    _ClientDescribeAttackResponseAttackSubResourcesTypeDef
):
    """
    Type definition for `ClientDescribeAttackResponseAttack` `SubResources`

    The attack information for the specified SubResource.

    - **Type** *(string) --*

      The ``SubResource`` type.

    - **Id** *(string) --*

      The unique identifier (ID) of the ``SubResource`` .

    - **AttackVectors** *(list) --*

      The list of attack types and associated counters.

      - *(dict) --*

        A summary of information about the attack.

        - **VectorType** *(string) --*

          The attack type, for example, SNMP reflection or SYN flood.

        - **VectorCounters** *(list) --*

          The list of counters that describe the details of the attack.

          - *(dict) --*

            The counter that describes a DDoS attack.

            - **Name** *(string) --*

              The counter name.

            - **Max** *(float) --*

              The maximum value of the counter for a specified time period.

            - **Average** *(float) --*

              The average value of the counter for a specified time period.

            - **Sum** *(float) --*

              The total of counter values for a specified time period.

            - **N** *(integer) --*

              The number of counters for a specified time period.

            - **Unit** *(string) --*

              The unit of the counters.

    - **Counters** *(list) --*

      The counters that describe the details of the attack.

      - *(dict) --*

        The counter that describes a DDoS attack.

        - **Name** *(string) --*

          The counter name.

        - **Max** *(float) --*

          The maximum value of the counter for a specified time period.

        - **Average** *(float) --*

          The average value of the counter for a specified time period.

        - **Sum** *(float) --*

          The total of counter values for a specified time period.

        - **N** *(integer) --*

          The number of counters for a specified time period.

        - **Unit** *(string) --*

          The unit of the counters.
    """


_ClientDescribeAttackResponseAttackTypeDef = TypedDict(
    "_ClientDescribeAttackResponseAttackTypeDef",
    {
        "AttackId": str,
        "ResourceArn": str,
        "SubResources": List[ClientDescribeAttackResponseAttackSubResourcesTypeDef],
        "StartTime": datetime,
        "EndTime": datetime,
        "AttackCounters": List[ClientDescribeAttackResponseAttackAttackCountersTypeDef],
        "AttackProperties": List[
            ClientDescribeAttackResponseAttackAttackPropertiesTypeDef
        ],
        "Mitigations": List[ClientDescribeAttackResponseAttackMitigationsTypeDef],
    },
    total=False,
)


class ClientDescribeAttackResponseAttackTypeDef(
    _ClientDescribeAttackResponseAttackTypeDef
):
    """
    Type definition for `ClientDescribeAttackResponse` `Attack`

    The attack that is described.

    - **AttackId** *(string) --*

      The unique identifier (ID) of the attack.

    - **ResourceArn** *(string) --*

      The ARN (Amazon Resource Name) of the resource that was attacked.

    - **SubResources** *(list) --*

      If applicable, additional detail about the resource being attacked, for example, IP address
      or URL.

      - *(dict) --*

        The attack information for the specified SubResource.

        - **Type** *(string) --*

          The ``SubResource`` type.

        - **Id** *(string) --*

          The unique identifier (ID) of the ``SubResource`` .

        - **AttackVectors** *(list) --*

          The list of attack types and associated counters.

          - *(dict) --*

            A summary of information about the attack.

            - **VectorType** *(string) --*

              The attack type, for example, SNMP reflection or SYN flood.

            - **VectorCounters** *(list) --*

              The list of counters that describe the details of the attack.

              - *(dict) --*

                The counter that describes a DDoS attack.

                - **Name** *(string) --*

                  The counter name.

                - **Max** *(float) --*

                  The maximum value of the counter for a specified time period.

                - **Average** *(float) --*

                  The average value of the counter for a specified time period.

                - **Sum** *(float) --*

                  The total of counter values for a specified time period.

                - **N** *(integer) --*

                  The number of counters for a specified time period.

                - **Unit** *(string) --*

                  The unit of the counters.

        - **Counters** *(list) --*

          The counters that describe the details of the attack.

          - *(dict) --*

            The counter that describes a DDoS attack.

            - **Name** *(string) --*

              The counter name.

            - **Max** *(float) --*

              The maximum value of the counter for a specified time period.

            - **Average** *(float) --*

              The average value of the counter for a specified time period.

            - **Sum** *(float) --*

              The total of counter values for a specified time period.

            - **N** *(integer) --*

              The number of counters for a specified time period.

            - **Unit** *(string) --*

              The unit of the counters.

    - **StartTime** *(datetime) --*

      The time the attack started, in Unix time in seconds. For more information see `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

    - **EndTime** *(datetime) --*

      The time the attack ended, in Unix time in seconds. For more information see `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

    - **AttackCounters** *(list) --*

      List of counters that describe the attack for the specified time period.

      - *(dict) --*

        The counter that describes a DDoS attack.

        - **Name** *(string) --*

          The counter name.

        - **Max** *(float) --*

          The maximum value of the counter for a specified time period.

        - **Average** *(float) --*

          The average value of the counter for a specified time period.

        - **Sum** *(float) --*

          The total of counter values for a specified time period.

        - **N** *(integer) --*

          The number of counters for a specified time period.

        - **Unit** *(string) --*

          The unit of the counters.

    - **AttackProperties** *(list) --*

      The array of  AttackProperty objects.

      - *(dict) --*

        Details of the described attack.

        - **AttackLayer** *(string) --*

          The type of distributed denial of service (DDoS) event that was observed. ``NETWORK``
          indicates layer 3 and layer 4 events and ``APPLICATION`` indicates layer 7 events.

        - **AttackPropertyIdentifier** *(string) --*

          Defines the DDoS attack property information that is provided. The
          ``WORDPRESS_PINGBACK_REFLECTOR`` and ``WORDPRESS_PINGBACK_SOURCE`` values are valid
          only for WordPress reflective pingback DDoS attacks.

        - **TopContributors** *(list) --*

          The array of  Contributor objects that includes the top five contributors to an attack.

          - *(dict) --*

            A contributor to the attack and their contribution.

            - **Name** *(string) --*

              The name of the contributor. This is dependent on the ``AttackPropertyIdentifier``
              . For example, if the ``AttackPropertyIdentifier`` is ``SOURCE_COUNTRY`` , the
              ``Name`` could be ``United States`` .

            - **Value** *(integer) --*

              The contribution of this contributor expressed in  Protection units. For example
              ``10,000`` .

        - **Unit** *(string) --*

          The unit of the ``Value`` of the contributions.

        - **Total** *(integer) --*

          The total contributions made to this attack by all contributors, not just the five
          listed in the ``TopContributors`` list.

    - **Mitigations** *(list) --*

      List of mitigation actions taken for the attack.

      - *(dict) --*

        The mitigation applied to a DDoS attack.

        - **MitigationName** *(string) --*

          The name of the mitigation taken for this attack.
    """


_ClientDescribeAttackResponseTypeDef = TypedDict(
    "_ClientDescribeAttackResponseTypeDef",
    {"Attack": ClientDescribeAttackResponseAttackTypeDef},
    total=False,
)


class ClientDescribeAttackResponseTypeDef(_ClientDescribeAttackResponseTypeDef):
    """
    Type definition for `ClientDescribeAttack` `Response`

    - **Attack** *(dict) --*

      The attack that is described.

      - **AttackId** *(string) --*

        The unique identifier (ID) of the attack.

      - **ResourceArn** *(string) --*

        The ARN (Amazon Resource Name) of the resource that was attacked.

      - **SubResources** *(list) --*

        If applicable, additional detail about the resource being attacked, for example, IP address
        or URL.

        - *(dict) --*

          The attack information for the specified SubResource.

          - **Type** *(string) --*

            The ``SubResource`` type.

          - **Id** *(string) --*

            The unique identifier (ID) of the ``SubResource`` .

          - **AttackVectors** *(list) --*

            The list of attack types and associated counters.

            - *(dict) --*

              A summary of information about the attack.

              - **VectorType** *(string) --*

                The attack type, for example, SNMP reflection or SYN flood.

              - **VectorCounters** *(list) --*

                The list of counters that describe the details of the attack.

                - *(dict) --*

                  The counter that describes a DDoS attack.

                  - **Name** *(string) --*

                    The counter name.

                  - **Max** *(float) --*

                    The maximum value of the counter for a specified time period.

                  - **Average** *(float) --*

                    The average value of the counter for a specified time period.

                  - **Sum** *(float) --*

                    The total of counter values for a specified time period.

                  - **N** *(integer) --*

                    The number of counters for a specified time period.

                  - **Unit** *(string) --*

                    The unit of the counters.

          - **Counters** *(list) --*

            The counters that describe the details of the attack.

            - *(dict) --*

              The counter that describes a DDoS attack.

              - **Name** *(string) --*

                The counter name.

              - **Max** *(float) --*

                The maximum value of the counter for a specified time period.

              - **Average** *(float) --*

                The average value of the counter for a specified time period.

              - **Sum** *(float) --*

                The total of counter values for a specified time period.

              - **N** *(integer) --*

                The number of counters for a specified time period.

              - **Unit** *(string) --*

                The unit of the counters.

      - **StartTime** *(datetime) --*

        The time the attack started, in Unix time in seconds. For more information see `timestamp
        <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

      - **EndTime** *(datetime) --*

        The time the attack ended, in Unix time in seconds. For more information see `timestamp
        <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

      - **AttackCounters** *(list) --*

        List of counters that describe the attack for the specified time period.

        - *(dict) --*

          The counter that describes a DDoS attack.

          - **Name** *(string) --*

            The counter name.

          - **Max** *(float) --*

            The maximum value of the counter for a specified time period.

          - **Average** *(float) --*

            The average value of the counter for a specified time period.

          - **Sum** *(float) --*

            The total of counter values for a specified time period.

          - **N** *(integer) --*

            The number of counters for a specified time period.

          - **Unit** *(string) --*

            The unit of the counters.

      - **AttackProperties** *(list) --*

        The array of  AttackProperty objects.

        - *(dict) --*

          Details of the described attack.

          - **AttackLayer** *(string) --*

            The type of distributed denial of service (DDoS) event that was observed. ``NETWORK``
            indicates layer 3 and layer 4 events and ``APPLICATION`` indicates layer 7 events.

          - **AttackPropertyIdentifier** *(string) --*

            Defines the DDoS attack property information that is provided. The
            ``WORDPRESS_PINGBACK_REFLECTOR`` and ``WORDPRESS_PINGBACK_SOURCE`` values are valid
            only for WordPress reflective pingback DDoS attacks.

          - **TopContributors** *(list) --*

            The array of  Contributor objects that includes the top five contributors to an attack.

            - *(dict) --*

              A contributor to the attack and their contribution.

              - **Name** *(string) --*

                The name of the contributor. This is dependent on the ``AttackPropertyIdentifier``
                . For example, if the ``AttackPropertyIdentifier`` is ``SOURCE_COUNTRY`` , the
                ``Name`` could be ``United States`` .

              - **Value** *(integer) --*

                The contribution of this contributor expressed in  Protection units. For example
                ``10,000`` .

          - **Unit** *(string) --*

            The unit of the ``Value`` of the contributions.

          - **Total** *(integer) --*

            The total contributions made to this attack by all contributors, not just the five
            listed in the ``TopContributors`` list.

      - **Mitigations** *(list) --*

        List of mitigation actions taken for the attack.

        - *(dict) --*

          The mitigation applied to a DDoS attack.

          - **MitigationName** *(string) --*

            The name of the mitigation taken for this attack.
    """


_ClientDescribeDrtAccessResponseTypeDef = TypedDict(
    "_ClientDescribeDrtAccessResponseTypeDef",
    {"RoleArn": str, "LogBucketList": List[str]},
    total=False,
)


class ClientDescribeDrtAccessResponseTypeDef(_ClientDescribeDrtAccessResponseTypeDef):
    """
    Type definition for `ClientDescribeDrtAccess` `Response`

    - **RoleArn** *(string) --*

      The Amazon Resource Name (ARN) of the role the DRT used to access your AWS account.

    - **LogBucketList** *(list) --*

      The list of Amazon S3 buckets accessed by the DRT.

      - *(string) --*
    """


_ClientDescribeEmergencyContactSettingsResponseEmergencyContactListTypeDef = TypedDict(
    "_ClientDescribeEmergencyContactSettingsResponseEmergencyContactListTypeDef",
    {"EmailAddress": str},
    total=False,
)


class ClientDescribeEmergencyContactSettingsResponseEmergencyContactListTypeDef(
    _ClientDescribeEmergencyContactSettingsResponseEmergencyContactListTypeDef
):
    """
    Type definition for `ClientDescribeEmergencyContactSettingsResponse` `EmergencyContactList`

    Contact information that the DRT can use to contact you during a suspected attack.

    - **EmailAddress** *(string) --*

      An email address that the DRT can use to contact you during a suspected attack.
    """


_ClientDescribeEmergencyContactSettingsResponseTypeDef = TypedDict(
    "_ClientDescribeEmergencyContactSettingsResponseTypeDef",
    {
        "EmergencyContactList": List[
            ClientDescribeEmergencyContactSettingsResponseEmergencyContactListTypeDef
        ]
    },
    total=False,
)


class ClientDescribeEmergencyContactSettingsResponseTypeDef(
    _ClientDescribeEmergencyContactSettingsResponseTypeDef
):
    """
    Type definition for `ClientDescribeEmergencyContactSettings` `Response`

    - **EmergencyContactList** *(list) --*

      A list of email addresses that the DRT can use to contact you during a suspected attack.

      - *(dict) --*

        Contact information that the DRT can use to contact you during a suspected attack.

        - **EmailAddress** *(string) --*

          An email address that the DRT can use to contact you during a suspected attack.
    """


_ClientDescribeProtectionResponseProtectionTypeDef = TypedDict(
    "_ClientDescribeProtectionResponseProtectionTypeDef",
    {"Id": str, "Name": str, "ResourceArn": str},
    total=False,
)


class ClientDescribeProtectionResponseProtectionTypeDef(
    _ClientDescribeProtectionResponseProtectionTypeDef
):
    """
    Type definition for `ClientDescribeProtectionResponse` `Protection`

    The  Protection object that is described.

    - **Id** *(string) --*

      The unique identifier (ID) of the protection.

    - **Name** *(string) --*

      The friendly name of the protection. For example, ``My CloudFront distributions`` .

    - **ResourceArn** *(string) --*

      The ARN (Amazon Resource Name) of the AWS resource that is protected.
    """


_ClientDescribeProtectionResponseTypeDef = TypedDict(
    "_ClientDescribeProtectionResponseTypeDef",
    {"Protection": ClientDescribeProtectionResponseProtectionTypeDef},
    total=False,
)


class ClientDescribeProtectionResponseTypeDef(_ClientDescribeProtectionResponseTypeDef):
    """
    Type definition for `ClientDescribeProtection` `Response`

    - **Protection** *(dict) --*

      The  Protection object that is described.

      - **Id** *(string) --*

        The unique identifier (ID) of the protection.

      - **Name** *(string) --*

        The friendly name of the protection. For example, ``My CloudFront distributions`` .

      - **ResourceArn** *(string) --*

        The ARN (Amazon Resource Name) of the AWS resource that is protected.
    """


_ClientDescribeSubscriptionResponseSubscriptionLimitsTypeDef = TypedDict(
    "_ClientDescribeSubscriptionResponseSubscriptionLimitsTypeDef",
    {"Type": str, "Max": int},
    total=False,
)


class ClientDescribeSubscriptionResponseSubscriptionLimitsTypeDef(
    _ClientDescribeSubscriptionResponseSubscriptionLimitsTypeDef
):
    """
    Type definition for `ClientDescribeSubscriptionResponseSubscription` `Limits`

    Specifies how many protections of a given type you can create.

    - **Type** *(string) --*

      The type of protection.

    - **Max** *(integer) --*

      The maximum number of protections that can be created for the specified ``Type`` .
    """


_ClientDescribeSubscriptionResponseSubscriptionTypeDef = TypedDict(
    "_ClientDescribeSubscriptionResponseSubscriptionTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "TimeCommitmentInSeconds": int,
        "AutoRenew": str,
        "Limits": List[ClientDescribeSubscriptionResponseSubscriptionLimitsTypeDef],
    },
    total=False,
)


class ClientDescribeSubscriptionResponseSubscriptionTypeDef(
    _ClientDescribeSubscriptionResponseSubscriptionTypeDef
):
    """
    Type definition for `ClientDescribeSubscriptionResponse` `Subscription`

    The AWS Shield Advanced subscription details for an account.

    - **StartTime** *(datetime) --*

      The start time of the subscription, in Unix time in seconds. For more information see
      `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

    - **EndTime** *(datetime) --*

      The date and time your subscription will end.

    - **TimeCommitmentInSeconds** *(integer) --*

      The length, in seconds, of the AWS Shield Advanced subscription for the account.

    - **AutoRenew** *(string) --*

      If ``ENABLED`` , the subscription will be automatically renewed at the end of the existing
      subscription period.

      When you initally create a subscription, ``AutoRenew`` is set to ``ENABLED`` . You can
      change this by submitting an ``UpdateSubscription`` request. If the ``UpdateSubscription``
      request does not included a value for ``AutoRenew`` , the existing value for ``AutoRenew``
      remains unchanged.

    - **Limits** *(list) --*

      Specifies how many protections of a given type you can create.

      - *(dict) --*

        Specifies how many protections of a given type you can create.

        - **Type** *(string) --*

          The type of protection.

        - **Max** *(integer) --*

          The maximum number of protections that can be created for the specified ``Type`` .
    """


_ClientDescribeSubscriptionResponseTypeDef = TypedDict(
    "_ClientDescribeSubscriptionResponseTypeDef",
    {"Subscription": ClientDescribeSubscriptionResponseSubscriptionTypeDef},
    total=False,
)


class ClientDescribeSubscriptionResponseTypeDef(
    _ClientDescribeSubscriptionResponseTypeDef
):
    """
    Type definition for `ClientDescribeSubscription` `Response`

    - **Subscription** *(dict) --*

      The AWS Shield Advanced subscription details for an account.

      - **StartTime** *(datetime) --*

        The start time of the subscription, in Unix time in seconds. For more information see
        `timestamp
        <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

      - **EndTime** *(datetime) --*

        The date and time your subscription will end.

      - **TimeCommitmentInSeconds** *(integer) --*

        The length, in seconds, of the AWS Shield Advanced subscription for the account.

      - **AutoRenew** *(string) --*

        If ``ENABLED`` , the subscription will be automatically renewed at the end of the existing
        subscription period.

        When you initally create a subscription, ``AutoRenew`` is set to ``ENABLED`` . You can
        change this by submitting an ``UpdateSubscription`` request. If the ``UpdateSubscription``
        request does not included a value for ``AutoRenew`` , the existing value for ``AutoRenew``
        remains unchanged.

      - **Limits** *(list) --*

        Specifies how many protections of a given type you can create.

        - *(dict) --*

          Specifies how many protections of a given type you can create.

          - **Type** *(string) --*

            The type of protection.

          - **Max** *(integer) --*

            The maximum number of protections that can be created for the specified ``Type`` .
    """


_ClientGetSubscriptionStateResponseTypeDef = TypedDict(
    "_ClientGetSubscriptionStateResponseTypeDef",
    {"SubscriptionState": str},
    total=False,
)


class ClientGetSubscriptionStateResponseTypeDef(
    _ClientGetSubscriptionStateResponseTypeDef
):
    """
    Type definition for `ClientGetSubscriptionState` `Response`

    - **SubscriptionState** *(string) --*

      The status of the subscription.
    """


_ClientListAttacksEndTimeTypeDef = TypedDict(
    "_ClientListAttacksEndTimeTypeDef",
    {"FromInclusive": datetime, "ToExclusive": datetime},
    total=False,
)


class ClientListAttacksEndTimeTypeDef(_ClientListAttacksEndTimeTypeDef):
    """
    Type definition for `ClientListAttacks` `EndTime`

    The end of the time period for the attacks. This is a ``timestamp`` type. The sample request
    above indicates a ``number`` type because the default used by WAF is Unix time in seconds.
    However any valid `timestamp format
    <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ is
    allowed.

    - **FromInclusive** *(datetime) --*

      The start time, in Unix time in seconds. For more information see `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

    - **ToExclusive** *(datetime) --*

      The end time, in Unix time in seconds. For more information see `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
    """


_ClientListAttacksResponseAttackSummariesAttackVectorsTypeDef = TypedDict(
    "_ClientListAttacksResponseAttackSummariesAttackVectorsTypeDef",
    {"VectorType": str},
    total=False,
)


class ClientListAttacksResponseAttackSummariesAttackVectorsTypeDef(
    _ClientListAttacksResponseAttackSummariesAttackVectorsTypeDef
):
    """
    Type definition for `ClientListAttacksResponseAttackSummaries` `AttackVectors`

    Describes the attack.

    - **VectorType** *(string) --*

      The attack type. Valid values:

      * UDP_TRAFFIC

      * UDP_FRAGMENT

      * GENERIC_UDP_REFLECTION

      * DNS_REFLECTION

      * NTP_REFLECTION

      * CHARGEN_REFLECTION

      * SSDP_REFLECTION

      * PORT_MAPPER

      * RIP_REFLECTION

      * SNMP_REFLECTION

      * MSSQL_REFLECTION

      * NET_BIOS_REFLECTION

      * SYN_FLOOD

      * ACK_FLOOD

      * REQUEST_FLOOD

      * HTTP_REFLECTION

      * UDS_REFLECTION

      * MEMCACHED_REFLECTION
    """


_ClientListAttacksResponseAttackSummariesTypeDef = TypedDict(
    "_ClientListAttacksResponseAttackSummariesTypeDef",
    {
        "AttackId": str,
        "ResourceArn": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "AttackVectors": List[
            ClientListAttacksResponseAttackSummariesAttackVectorsTypeDef
        ],
    },
    total=False,
)


class ClientListAttacksResponseAttackSummariesTypeDef(
    _ClientListAttacksResponseAttackSummariesTypeDef
):
    """
    Type definition for `ClientListAttacksResponse` `AttackSummaries`

    Summarizes all DDoS attacks for a specified time period.

    - **AttackId** *(string) --*

      The unique identifier (ID) of the attack.

    - **ResourceArn** *(string) --*

      The ARN (Amazon Resource Name) of the resource that was attacked.

    - **StartTime** *(datetime) --*

      The start time of the attack, in Unix time in seconds. For more information see
      `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__
      .

    - **EndTime** *(datetime) --*

      The end time of the attack, in Unix time in seconds. For more information see `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__
      .

    - **AttackVectors** *(list) --*

      The list of attacks for a specified time period.

      - *(dict) --*

        Describes the attack.

        - **VectorType** *(string) --*

          The attack type. Valid values:

          * UDP_TRAFFIC

          * UDP_FRAGMENT

          * GENERIC_UDP_REFLECTION

          * DNS_REFLECTION

          * NTP_REFLECTION

          * CHARGEN_REFLECTION

          * SSDP_REFLECTION

          * PORT_MAPPER

          * RIP_REFLECTION

          * SNMP_REFLECTION

          * MSSQL_REFLECTION

          * NET_BIOS_REFLECTION

          * SYN_FLOOD

          * ACK_FLOOD

          * REQUEST_FLOOD

          * HTTP_REFLECTION

          * UDS_REFLECTION

          * MEMCACHED_REFLECTION
    """


_ClientListAttacksResponseTypeDef = TypedDict(
    "_ClientListAttacksResponseTypeDef",
    {
        "AttackSummaries": List[ClientListAttacksResponseAttackSummariesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListAttacksResponseTypeDef(_ClientListAttacksResponseTypeDef):
    """
    Type definition for `ClientListAttacks` `Response`

    - **AttackSummaries** *(list) --*

      The attack information for the specified time range.

      - *(dict) --*

        Summarizes all DDoS attacks for a specified time period.

        - **AttackId** *(string) --*

          The unique identifier (ID) of the attack.

        - **ResourceArn** *(string) --*

          The ARN (Amazon Resource Name) of the resource that was attacked.

        - **StartTime** *(datetime) --*

          The start time of the attack, in Unix time in seconds. For more information see
          `timestamp
          <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__
          .

        - **EndTime** *(datetime) --*

          The end time of the attack, in Unix time in seconds. For more information see `timestamp
          <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__
          .

        - **AttackVectors** *(list) --*

          The list of attacks for a specified time period.

          - *(dict) --*

            Describes the attack.

            - **VectorType** *(string) --*

              The attack type. Valid values:

              * UDP_TRAFFIC

              * UDP_FRAGMENT

              * GENERIC_UDP_REFLECTION

              * DNS_REFLECTION

              * NTP_REFLECTION

              * CHARGEN_REFLECTION

              * SSDP_REFLECTION

              * PORT_MAPPER

              * RIP_REFLECTION

              * SNMP_REFLECTION

              * MSSQL_REFLECTION

              * NET_BIOS_REFLECTION

              * SYN_FLOOD

              * ACK_FLOOD

              * REQUEST_FLOOD

              * HTTP_REFLECTION

              * UDS_REFLECTION

              * MEMCACHED_REFLECTION

    - **NextToken** *(string) --*

      The token returned by a previous call to indicate that there is more data available. If not
      null, more results are available. Pass this value for the ``NextMarker`` parameter in a
      subsequent call to ``ListAttacks`` to retrieve the next set of items.

      AWS WAF might return the list of  AttackSummary objects in batches smaller than the number
      specified by MaxResults. If there are more  AttackSummary objects to return, AWS WAF will
      always also return a ``NextToken`` .
    """


_ClientListAttacksStartTimeTypeDef = TypedDict(
    "_ClientListAttacksStartTimeTypeDef",
    {"FromInclusive": datetime, "ToExclusive": datetime},
    total=False,
)


class ClientListAttacksStartTimeTypeDef(_ClientListAttacksStartTimeTypeDef):
    """
    Type definition for `ClientListAttacks` `StartTime`

    The start of the time period for the attacks. This is a ``timestamp`` type. The sample request
    above indicates a ``number`` type because the default used by WAF is Unix time in seconds.
    However any valid `timestamp format
    <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ is
    allowed.

    - **FromInclusive** *(datetime) --*

      The start time, in Unix time in seconds. For more information see `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

    - **ToExclusive** *(datetime) --*

      The end time, in Unix time in seconds. For more information see `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
    """


_ClientListProtectionsResponseProtectionsTypeDef = TypedDict(
    "_ClientListProtectionsResponseProtectionsTypeDef",
    {"Id": str, "Name": str, "ResourceArn": str},
    total=False,
)


class ClientListProtectionsResponseProtectionsTypeDef(
    _ClientListProtectionsResponseProtectionsTypeDef
):
    """
    Type definition for `ClientListProtectionsResponse` `Protections`

    An object that represents a resource that is under DDoS protection.

    - **Id** *(string) --*

      The unique identifier (ID) of the protection.

    - **Name** *(string) --*

      The friendly name of the protection. For example, ``My CloudFront distributions`` .

    - **ResourceArn** *(string) --*

      The ARN (Amazon Resource Name) of the AWS resource that is protected.
    """


_ClientListProtectionsResponseTypeDef = TypedDict(
    "_ClientListProtectionsResponseTypeDef",
    {
        "Protections": List[ClientListProtectionsResponseProtectionsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListProtectionsResponseTypeDef(_ClientListProtectionsResponseTypeDef):
    """
    Type definition for `ClientListProtections` `Response`

    - **Protections** *(list) --*

      The array of enabled  Protection objects.

      - *(dict) --*

        An object that represents a resource that is under DDoS protection.

        - **Id** *(string) --*

          The unique identifier (ID) of the protection.

        - **Name** *(string) --*

          The friendly name of the protection. For example, ``My CloudFront distributions`` .

        - **ResourceArn** *(string) --*

          The ARN (Amazon Resource Name) of the AWS resource that is protected.

    - **NextToken** *(string) --*

      If you specify a value for ``MaxResults`` and you have more Protections than the value of
      MaxResults, AWS Shield Advanced returns a NextToken value in the response that allows you to
      list another group of Protections. For the second and subsequent ListProtections requests,
      specify the value of NextToken from the previous response to get information about another
      batch of Protections.

      AWS WAF might return the list of  Protection objects in batches smaller than the number
      specified by MaxResults. If there are more  Protection objects to return, AWS WAF will always
      also return a ``NextToken`` .
    """


_ClientUpdateEmergencyContactSettingsEmergencyContactListTypeDef = TypedDict(
    "_ClientUpdateEmergencyContactSettingsEmergencyContactListTypeDef",
    {"EmailAddress": str},
)


class ClientUpdateEmergencyContactSettingsEmergencyContactListTypeDef(
    _ClientUpdateEmergencyContactSettingsEmergencyContactListTypeDef
):
    """
    Type definition for `ClientUpdateEmergencyContactSettings` `EmergencyContactList`

    Contact information that the DRT can use to contact you during a suspected attack.

    - **EmailAddress** *(string) --* **[REQUIRED]**

      An email address that the DRT can use to contact you during a suspected attack.
    """


_ListAttacksPaginateEndTimeTypeDef = TypedDict(
    "_ListAttacksPaginateEndTimeTypeDef",
    {"FromInclusive": datetime, "ToExclusive": datetime},
    total=False,
)


class ListAttacksPaginateEndTimeTypeDef(_ListAttacksPaginateEndTimeTypeDef):
    """
    Type definition for `ListAttacksPaginate` `EndTime`

    The end of the time period for the attacks. This is a ``timestamp`` type. The sample request
    above indicates a ``number`` type because the default used by WAF is Unix time in seconds.
    However any valid `timestamp format
    <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ is
    allowed.

    - **FromInclusive** *(datetime) --*

      The start time, in Unix time in seconds. For more information see `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

    - **ToExclusive** *(datetime) --*

      The end time, in Unix time in seconds. For more information see `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
    """


_ListAttacksPaginatePaginationConfigTypeDef = TypedDict(
    "_ListAttacksPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListAttacksPaginatePaginationConfigTypeDef(
    _ListAttacksPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListAttacksPaginate` `PaginationConfig`

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


_ListAttacksPaginateResponseAttackSummariesAttackVectorsTypeDef = TypedDict(
    "_ListAttacksPaginateResponseAttackSummariesAttackVectorsTypeDef",
    {"VectorType": str},
    total=False,
)


class ListAttacksPaginateResponseAttackSummariesAttackVectorsTypeDef(
    _ListAttacksPaginateResponseAttackSummariesAttackVectorsTypeDef
):
    """
    Type definition for `ListAttacksPaginateResponseAttackSummaries` `AttackVectors`

    Describes the attack.

    - **VectorType** *(string) --*

      The attack type. Valid values:

      * UDP_TRAFFIC

      * UDP_FRAGMENT

      * GENERIC_UDP_REFLECTION

      * DNS_REFLECTION

      * NTP_REFLECTION

      * CHARGEN_REFLECTION

      * SSDP_REFLECTION

      * PORT_MAPPER

      * RIP_REFLECTION

      * SNMP_REFLECTION

      * MSSQL_REFLECTION

      * NET_BIOS_REFLECTION

      * SYN_FLOOD

      * ACK_FLOOD

      * REQUEST_FLOOD

      * HTTP_REFLECTION

      * UDS_REFLECTION

      * MEMCACHED_REFLECTION
    """


_ListAttacksPaginateResponseAttackSummariesTypeDef = TypedDict(
    "_ListAttacksPaginateResponseAttackSummariesTypeDef",
    {
        "AttackId": str,
        "ResourceArn": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "AttackVectors": List[
            ListAttacksPaginateResponseAttackSummariesAttackVectorsTypeDef
        ],
    },
    total=False,
)


class ListAttacksPaginateResponseAttackSummariesTypeDef(
    _ListAttacksPaginateResponseAttackSummariesTypeDef
):
    """
    Type definition for `ListAttacksPaginateResponse` `AttackSummaries`

    Summarizes all DDoS attacks for a specified time period.

    - **AttackId** *(string) --*

      The unique identifier (ID) of the attack.

    - **ResourceArn** *(string) --*

      The ARN (Amazon Resource Name) of the resource that was attacked.

    - **StartTime** *(datetime) --*

      The start time of the attack, in Unix time in seconds. For more information see
      `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__
      .

    - **EndTime** *(datetime) --*

      The end time of the attack, in Unix time in seconds. For more information see `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__
      .

    - **AttackVectors** *(list) --*

      The list of attacks for a specified time period.

      - *(dict) --*

        Describes the attack.

        - **VectorType** *(string) --*

          The attack type. Valid values:

          * UDP_TRAFFIC

          * UDP_FRAGMENT

          * GENERIC_UDP_REFLECTION

          * DNS_REFLECTION

          * NTP_REFLECTION

          * CHARGEN_REFLECTION

          * SSDP_REFLECTION

          * PORT_MAPPER

          * RIP_REFLECTION

          * SNMP_REFLECTION

          * MSSQL_REFLECTION

          * NET_BIOS_REFLECTION

          * SYN_FLOOD

          * ACK_FLOOD

          * REQUEST_FLOOD

          * HTTP_REFLECTION

          * UDS_REFLECTION

          * MEMCACHED_REFLECTION
    """


_ListAttacksPaginateResponseTypeDef = TypedDict(
    "_ListAttacksPaginateResponseTypeDef",
    {"AttackSummaries": List[ListAttacksPaginateResponseAttackSummariesTypeDef]},
    total=False,
)


class ListAttacksPaginateResponseTypeDef(_ListAttacksPaginateResponseTypeDef):
    """
    Type definition for `ListAttacksPaginate` `Response`

    - **AttackSummaries** *(list) --*

      The attack information for the specified time range.

      - *(dict) --*

        Summarizes all DDoS attacks for a specified time period.

        - **AttackId** *(string) --*

          The unique identifier (ID) of the attack.

        - **ResourceArn** *(string) --*

          The ARN (Amazon Resource Name) of the resource that was attacked.

        - **StartTime** *(datetime) --*

          The start time of the attack, in Unix time in seconds. For more information see
          `timestamp
          <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__
          .

        - **EndTime** *(datetime) --*

          The end time of the attack, in Unix time in seconds. For more information see `timestamp
          <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__
          .

        - **AttackVectors** *(list) --*

          The list of attacks for a specified time period.

          - *(dict) --*

            Describes the attack.

            - **VectorType** *(string) --*

              The attack type. Valid values:

              * UDP_TRAFFIC

              * UDP_FRAGMENT

              * GENERIC_UDP_REFLECTION

              * DNS_REFLECTION

              * NTP_REFLECTION

              * CHARGEN_REFLECTION

              * SSDP_REFLECTION

              * PORT_MAPPER

              * RIP_REFLECTION

              * SNMP_REFLECTION

              * MSSQL_REFLECTION

              * NET_BIOS_REFLECTION

              * SYN_FLOOD

              * ACK_FLOOD

              * REQUEST_FLOOD

              * HTTP_REFLECTION

              * UDS_REFLECTION

              * MEMCACHED_REFLECTION
    """


_ListAttacksPaginateStartTimeTypeDef = TypedDict(
    "_ListAttacksPaginateStartTimeTypeDef",
    {"FromInclusive": datetime, "ToExclusive": datetime},
    total=False,
)


class ListAttacksPaginateStartTimeTypeDef(_ListAttacksPaginateStartTimeTypeDef):
    """
    Type definition for `ListAttacksPaginate` `StartTime`

    The start of the time period for the attacks. This is a ``timestamp`` type. The sample request
    above indicates a ``number`` type because the default used by WAF is Unix time in seconds.
    However any valid `timestamp format
    <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ is
    allowed.

    - **FromInclusive** *(datetime) --*

      The start time, in Unix time in seconds. For more information see `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .

    - **ToExclusive** *(datetime) --*

      The end time, in Unix time in seconds. For more information see `timestamp
      <http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#parameter-types>`__ .
    """


_ListProtectionsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListProtectionsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListProtectionsPaginatePaginationConfigTypeDef(
    _ListProtectionsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListProtectionsPaginate` `PaginationConfig`

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


_ListProtectionsPaginateResponseProtectionsTypeDef = TypedDict(
    "_ListProtectionsPaginateResponseProtectionsTypeDef",
    {"Id": str, "Name": str, "ResourceArn": str},
    total=False,
)


class ListProtectionsPaginateResponseProtectionsTypeDef(
    _ListProtectionsPaginateResponseProtectionsTypeDef
):
    """
    Type definition for `ListProtectionsPaginateResponse` `Protections`

    An object that represents a resource that is under DDoS protection.

    - **Id** *(string) --*

      The unique identifier (ID) of the protection.

    - **Name** *(string) --*

      The friendly name of the protection. For example, ``My CloudFront distributions`` .

    - **ResourceArn** *(string) --*

      The ARN (Amazon Resource Name) of the AWS resource that is protected.
    """


_ListProtectionsPaginateResponseTypeDef = TypedDict(
    "_ListProtectionsPaginateResponseTypeDef",
    {"Protections": List[ListProtectionsPaginateResponseProtectionsTypeDef]},
    total=False,
)


class ListProtectionsPaginateResponseTypeDef(_ListProtectionsPaginateResponseTypeDef):
    """
    Type definition for `ListProtectionsPaginate` `Response`

    - **Protections** *(list) --*

      The array of enabled  Protection objects.

      - *(dict) --*

        An object that represents a resource that is under DDoS protection.

        - **Id** *(string) --*

          The unique identifier (ID) of the protection.

        - **Name** *(string) --*

          The friendly name of the protection. For example, ``My CloudFront distributions`` .

        - **ResourceArn** *(string) --*

          The ARN (Amazon Resource Name) of the AWS resource that is protected.
    """

"Main interface for connect type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateUserIdentityInfoTypeDef",
    "ClientCreateUserPhoneConfigTypeDef",
    "ClientCreateUserResponseTypeDef",
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFiveTypeDef",
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFourTypeDef",
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelOneTypeDef",
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelThreeTypeDef",
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelTwoTypeDef",
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathTypeDef",
    "ClientDescribeUserHierarchyGroupResponseHierarchyGroupTypeDef",
    "ClientDescribeUserHierarchyGroupResponseTypeDef",
    "ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFiveTypeDef",
    "ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFourTypeDef",
    "ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelOneTypeDef",
    "ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelThreeTypeDef",
    "ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelTwoTypeDef",
    "ClientDescribeUserHierarchyStructureResponseHierarchyStructureTypeDef",
    "ClientDescribeUserHierarchyStructureResponseTypeDef",
    "ClientDescribeUserResponseUserIdentityInfoTypeDef",
    "ClientDescribeUserResponseUserPhoneConfigTypeDef",
    "ClientDescribeUserResponseUserTypeDef",
    "ClientDescribeUserResponseTypeDef",
    "ClientGetContactAttributesResponseTypeDef",
    "ClientGetCurrentMetricDataCurrentMetricsTypeDef",
    "ClientGetCurrentMetricDataFiltersTypeDef",
    "ClientGetCurrentMetricDataResponseMetricResultsCollectionsMetricTypeDef",
    "ClientGetCurrentMetricDataResponseMetricResultsCollectionsTypeDef",
    "ClientGetCurrentMetricDataResponseMetricResultsDimensionsQueueTypeDef",
    "ClientGetCurrentMetricDataResponseMetricResultsDimensionsTypeDef",
    "ClientGetCurrentMetricDataResponseMetricResultsTypeDef",
    "ClientGetCurrentMetricDataResponseTypeDef",
    "ClientGetFederationTokenResponseCredentialsTypeDef",
    "ClientGetFederationTokenResponseTypeDef",
    "ClientGetMetricDataFiltersTypeDef",
    "ClientGetMetricDataHistoricalMetricsThresholdTypeDef",
    "ClientGetMetricDataHistoricalMetricsTypeDef",
    "ClientGetMetricDataResponseMetricResultsCollectionsMetricThresholdTypeDef",
    "ClientGetMetricDataResponseMetricResultsCollectionsMetricTypeDef",
    "ClientGetMetricDataResponseMetricResultsCollectionsTypeDef",
    "ClientGetMetricDataResponseMetricResultsDimensionsQueueTypeDef",
    "ClientGetMetricDataResponseMetricResultsDimensionsTypeDef",
    "ClientGetMetricDataResponseMetricResultsTypeDef",
    "ClientGetMetricDataResponseTypeDef",
    "ClientListContactFlowsResponseContactFlowSummaryListTypeDef",
    "ClientListContactFlowsResponseTypeDef",
    "ClientListHoursOfOperationsResponseHoursOfOperationSummaryListTypeDef",
    "ClientListHoursOfOperationsResponseTypeDef",
    "ClientListPhoneNumbersResponsePhoneNumberSummaryListTypeDef",
    "ClientListPhoneNumbersResponseTypeDef",
    "ClientListQueuesResponseQueueSummaryListTypeDef",
    "ClientListQueuesResponseTypeDef",
    "ClientListRoutingProfilesResponseRoutingProfileSummaryListTypeDef",
    "ClientListRoutingProfilesResponseTypeDef",
    "ClientListSecurityProfilesResponseSecurityProfileSummaryListTypeDef",
    "ClientListSecurityProfilesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListUserHierarchyGroupsResponseUserHierarchyGroupSummaryListTypeDef",
    "ClientListUserHierarchyGroupsResponseTypeDef",
    "ClientListUsersResponseUserSummaryListTypeDef",
    "ClientListUsersResponseTypeDef",
    "ClientStartOutboundVoiceContactResponseTypeDef",
    "ClientUpdateUserIdentityInfoIdentityInfoTypeDef",
    "ClientUpdateUserPhoneConfigPhoneConfigTypeDef",
    "GetMetricDataPaginateFiltersTypeDef",
    "GetMetricDataPaginateHistoricalMetricsThresholdTypeDef",
    "GetMetricDataPaginateHistoricalMetricsTypeDef",
    "GetMetricDataPaginatePaginationConfigTypeDef",
    "GetMetricDataPaginateResponseMetricResultsCollectionsMetricThresholdTypeDef",
    "GetMetricDataPaginateResponseMetricResultsCollectionsMetricTypeDef",
    "GetMetricDataPaginateResponseMetricResultsCollectionsTypeDef",
    "GetMetricDataPaginateResponseMetricResultsDimensionsQueueTypeDef",
    "GetMetricDataPaginateResponseMetricResultsDimensionsTypeDef",
    "GetMetricDataPaginateResponseMetricResultsTypeDef",
    "GetMetricDataPaginateResponseTypeDef",
    "ListContactFlowsPaginatePaginationConfigTypeDef",
    "ListContactFlowsPaginateResponseContactFlowSummaryListTypeDef",
    "ListContactFlowsPaginateResponseTypeDef",
    "ListHoursOfOperationsPaginatePaginationConfigTypeDef",
    "ListHoursOfOperationsPaginateResponseHoursOfOperationSummaryListTypeDef",
    "ListHoursOfOperationsPaginateResponseTypeDef",
    "ListPhoneNumbersPaginatePaginationConfigTypeDef",
    "ListPhoneNumbersPaginateResponsePhoneNumberSummaryListTypeDef",
    "ListPhoneNumbersPaginateResponseTypeDef",
    "ListQueuesPaginatePaginationConfigTypeDef",
    "ListQueuesPaginateResponseQueueSummaryListTypeDef",
    "ListQueuesPaginateResponseTypeDef",
    "ListRoutingProfilesPaginatePaginationConfigTypeDef",
    "ListRoutingProfilesPaginateResponseRoutingProfileSummaryListTypeDef",
    "ListRoutingProfilesPaginateResponseTypeDef",
    "ListSecurityProfilesPaginatePaginationConfigTypeDef",
    "ListSecurityProfilesPaginateResponseSecurityProfileSummaryListTypeDef",
    "ListSecurityProfilesPaginateResponseTypeDef",
    "ListUserHierarchyGroupsPaginatePaginationConfigTypeDef",
    "ListUserHierarchyGroupsPaginateResponseUserHierarchyGroupSummaryListTypeDef",
    "ListUserHierarchyGroupsPaginateResponseTypeDef",
    "ListUsersPaginatePaginationConfigTypeDef",
    "ListUsersPaginateResponseUserSummaryListTypeDef",
    "ListUsersPaginateResponseTypeDef",
)


_ClientCreateUserIdentityInfoTypeDef = TypedDict(
    "_ClientCreateUserIdentityInfoTypeDef",
    {"FirstName": str, "LastName": str, "Email": str},
    total=False,
)


class ClientCreateUserIdentityInfoTypeDef(_ClientCreateUserIdentityInfoTypeDef):
    """
    Type definition for `ClientCreateUser` `IdentityInfo`

    The information about the identity of the user.

    - **FirstName** *(string) --*

      The first name. This is required if you are using Amazon Connect or SAML for identity
      management.

    - **LastName** *(string) --*

      The last name. This is required if you are using Amazon Connect or SAML for identity management.

    - **Email** *(string) --*

      The email address. If you are using SAML for identity management and include this parameter, an
      error is returned.
    """


_RequiredClientCreateUserPhoneConfigTypeDef = TypedDict(
    "_RequiredClientCreateUserPhoneConfigTypeDef", {"PhoneType": str}
)
_OptionalClientCreateUserPhoneConfigTypeDef = TypedDict(
    "_OptionalClientCreateUserPhoneConfigTypeDef",
    {"AutoAccept": bool, "AfterContactWorkTimeLimit": int, "DeskPhoneNumber": str},
    total=False,
)


class ClientCreateUserPhoneConfigTypeDef(
    _RequiredClientCreateUserPhoneConfigTypeDef,
    _OptionalClientCreateUserPhoneConfigTypeDef,
):
    """
    Type definition for `ClientCreateUser` `PhoneConfig`

    The phone settings for the user.

    - **PhoneType** *(string) --* **[REQUIRED]**

      The phone type.

    - **AutoAccept** *(boolean) --*

      The Auto accept setting.

    - **AfterContactWorkTimeLimit** *(integer) --*

      The After Call Work (ACW) timeout setting, in seconds.

    - **DeskPhoneNumber** *(string) --*

      The phone number for the user's desk phone.
    """


_ClientCreateUserResponseTypeDef = TypedDict(
    "_ClientCreateUserResponseTypeDef", {"UserId": str, "UserArn": str}, total=False
)


class ClientCreateUserResponseTypeDef(_ClientCreateUserResponseTypeDef):
    """
    Type definition for `ClientCreateUser` `Response`

    - **UserId** *(string) --*

      The identifier of the user account.

    - **UserArn** *(string) --*

      The Amazon Resource Name (ARN) of the user account.
    """


_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFiveTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFiveTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFiveTypeDef(
    _ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFiveTypeDef
):
    """
    Type definition for `ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPath` `LevelFive`

    Information about level five.

    - **Id** *(string) --*

      The identifier of the hierarchy group.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the hierarchy group.

    - **Name** *(string) --*

      The name of the hierarchy group.
    """


_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFourTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFourTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFourTypeDef(
    _ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFourTypeDef
):
    """
    Type definition for `ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPath` `LevelFour`

    Information about level four.

    - **Id** *(string) --*

      The identifier of the hierarchy group.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the hierarchy group.

    - **Name** *(string) --*

      The name of the hierarchy group.
    """


_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelOneTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelOneTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelOneTypeDef(
    _ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelOneTypeDef
):
    """
    Type definition for `ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPath` `LevelOne`

    Information about level one.

    - **Id** *(string) --*

      The identifier of the hierarchy group.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the hierarchy group.

    - **Name** *(string) --*

      The name of the hierarchy group.
    """


_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelThreeTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelThreeTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelThreeTypeDef(
    _ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelThreeTypeDef
):
    """
    Type definition for `ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPath` `LevelThree`

    Information about level three.

    - **Id** *(string) --*

      The identifier of the hierarchy group.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the hierarchy group.

    - **Name** *(string) --*

      The name of the hierarchy group.
    """


_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelTwoTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelTwoTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelTwoTypeDef(
    _ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelTwoTypeDef
):
    """
    Type definition for `ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPath` `LevelTwo`

    Information about level two.

    - **Id** *(string) --*

      The identifier of the hierarchy group.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the hierarchy group.

    - **Name** *(string) --*

      The name of the hierarchy group.
    """


_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathTypeDef",
    {
        "LevelOne": ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelOneTypeDef,
        "LevelTwo": ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelTwoTypeDef,
        "LevelThree": ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelThreeTypeDef,
        "LevelFour": ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFourTypeDef,
        "LevelFive": ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathLevelFiveTypeDef,
    },
    total=False,
)


class ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathTypeDef(
    _ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathTypeDef
):
    """
    Type definition for `ClientDescribeUserHierarchyGroupResponseHierarchyGroup` `HierarchyPath`

    Information about the levels in the hierarchy group.

    - **LevelOne** *(dict) --*

      Information about level one.

      - **Id** *(string) --*

        The identifier of the hierarchy group.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the hierarchy group.

      - **Name** *(string) --*

        The name of the hierarchy group.

    - **LevelTwo** *(dict) --*

      Information about level two.

      - **Id** *(string) --*

        The identifier of the hierarchy group.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the hierarchy group.

      - **Name** *(string) --*

        The name of the hierarchy group.

    - **LevelThree** *(dict) --*

      Information about level three.

      - **Id** *(string) --*

        The identifier of the hierarchy group.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the hierarchy group.

      - **Name** *(string) --*

        The name of the hierarchy group.

    - **LevelFour** *(dict) --*

      Information about level four.

      - **Id** *(string) --*

        The identifier of the hierarchy group.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the hierarchy group.

      - **Name** *(string) --*

        The name of the hierarchy group.

    - **LevelFive** *(dict) --*

      Information about level five.

      - **Id** *(string) --*

        The identifier of the hierarchy group.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the hierarchy group.

      - **Name** *(string) --*

        The name of the hierarchy group.
    """


_ClientDescribeUserHierarchyGroupResponseHierarchyGroupTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyGroupResponseHierarchyGroupTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "LevelId": str,
        "HierarchyPath": ClientDescribeUserHierarchyGroupResponseHierarchyGroupHierarchyPathTypeDef,
    },
    total=False,
)


class ClientDescribeUserHierarchyGroupResponseHierarchyGroupTypeDef(
    _ClientDescribeUserHierarchyGroupResponseHierarchyGroupTypeDef
):
    """
    Type definition for `ClientDescribeUserHierarchyGroupResponse` `HierarchyGroup`

    Information about the hierarchy group.

    - **Id** *(string) --*

      The identifier of the hierarchy group.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the hierarchy group.

    - **Name** *(string) --*

      The name of the hierarchy group.

    - **LevelId** *(string) --*

      The identifier of the level in the hierarchy group.

    - **HierarchyPath** *(dict) --*

      Information about the levels in the hierarchy group.

      - **LevelOne** *(dict) --*

        Information about level one.

        - **Id** *(string) --*

          The identifier of the hierarchy group.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the hierarchy group.

        - **Name** *(string) --*

          The name of the hierarchy group.

      - **LevelTwo** *(dict) --*

        Information about level two.

        - **Id** *(string) --*

          The identifier of the hierarchy group.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the hierarchy group.

        - **Name** *(string) --*

          The name of the hierarchy group.

      - **LevelThree** *(dict) --*

        Information about level three.

        - **Id** *(string) --*

          The identifier of the hierarchy group.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the hierarchy group.

        - **Name** *(string) --*

          The name of the hierarchy group.

      - **LevelFour** *(dict) --*

        Information about level four.

        - **Id** *(string) --*

          The identifier of the hierarchy group.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the hierarchy group.

        - **Name** *(string) --*

          The name of the hierarchy group.

      - **LevelFive** *(dict) --*

        Information about level five.

        - **Id** *(string) --*

          The identifier of the hierarchy group.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the hierarchy group.

        - **Name** *(string) --*

          The name of the hierarchy group.
    """


_ClientDescribeUserHierarchyGroupResponseTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyGroupResponseTypeDef",
    {"HierarchyGroup": ClientDescribeUserHierarchyGroupResponseHierarchyGroupTypeDef},
    total=False,
)


class ClientDescribeUserHierarchyGroupResponseTypeDef(
    _ClientDescribeUserHierarchyGroupResponseTypeDef
):
    """
    Type definition for `ClientDescribeUserHierarchyGroup` `Response`

    - **HierarchyGroup** *(dict) --*

      Information about the hierarchy group.

      - **Id** *(string) --*

        The identifier of the hierarchy group.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the hierarchy group.

      - **Name** *(string) --*

        The name of the hierarchy group.

      - **LevelId** *(string) --*

        The identifier of the level in the hierarchy group.

      - **HierarchyPath** *(dict) --*

        Information about the levels in the hierarchy group.

        - **LevelOne** *(dict) --*

          Information about level one.

          - **Id** *(string) --*

            The identifier of the hierarchy group.

          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) of the hierarchy group.

          - **Name** *(string) --*

            The name of the hierarchy group.

        - **LevelTwo** *(dict) --*

          Information about level two.

          - **Id** *(string) --*

            The identifier of the hierarchy group.

          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) of the hierarchy group.

          - **Name** *(string) --*

            The name of the hierarchy group.

        - **LevelThree** *(dict) --*

          Information about level three.

          - **Id** *(string) --*

            The identifier of the hierarchy group.

          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) of the hierarchy group.

          - **Name** *(string) --*

            The name of the hierarchy group.

        - **LevelFour** *(dict) --*

          Information about level four.

          - **Id** *(string) --*

            The identifier of the hierarchy group.

          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) of the hierarchy group.

          - **Name** *(string) --*

            The name of the hierarchy group.

        - **LevelFive** *(dict) --*

          Information about level five.

          - **Id** *(string) --*

            The identifier of the hierarchy group.

          - **Arn** *(string) --*

            The Amazon Resource Name (ARN) of the hierarchy group.

          - **Name** *(string) --*

            The name of the hierarchy group.
    """


_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFiveTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFiveTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFiveTypeDef(
    _ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFiveTypeDef
):
    """
    Type definition for `ClientDescribeUserHierarchyStructureResponseHierarchyStructure` `LevelFive`

    Information about level five.

    - **Id** *(string) --*

      The identifier of the hierarchy level.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the hierarchy level.

    - **Name** *(string) --*

      The name of the hierarchy level.
    """


_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFourTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFourTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFourTypeDef(
    _ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFourTypeDef
):
    """
    Type definition for `ClientDescribeUserHierarchyStructureResponseHierarchyStructure` `LevelFour`

    Information about level four.

    - **Id** *(string) --*

      The identifier of the hierarchy level.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the hierarchy level.

    - **Name** *(string) --*

      The name of the hierarchy level.
    """


_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelOneTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelOneTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelOneTypeDef(
    _ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelOneTypeDef
):
    """
    Type definition for `ClientDescribeUserHierarchyStructureResponseHierarchyStructure` `LevelOne`

    Information about level one.

    - **Id** *(string) --*

      The identifier of the hierarchy level.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the hierarchy level.

    - **Name** *(string) --*

      The name of the hierarchy level.
    """


_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelThreeTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelThreeTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelThreeTypeDef(
    _ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelThreeTypeDef
):
    """
    Type definition for `ClientDescribeUserHierarchyStructureResponseHierarchyStructure` `LevelThree`

    Information about level three.

    - **Id** *(string) --*

      The identifier of the hierarchy level.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the hierarchy level.

    - **Name** *(string) --*

      The name of the hierarchy level.
    """


_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelTwoTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelTwoTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelTwoTypeDef(
    _ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelTwoTypeDef
):
    """
    Type definition for `ClientDescribeUserHierarchyStructureResponseHierarchyStructure` `LevelTwo`

    Information about level two.

    - **Id** *(string) --*

      The identifier of the hierarchy level.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the hierarchy level.

    - **Name** *(string) --*

      The name of the hierarchy level.
    """


_ClientDescribeUserHierarchyStructureResponseHierarchyStructureTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyStructureResponseHierarchyStructureTypeDef",
    {
        "LevelOne": ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelOneTypeDef,
        "LevelTwo": ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelTwoTypeDef,
        "LevelThree": ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelThreeTypeDef,
        "LevelFour": ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFourTypeDef,
        "LevelFive": ClientDescribeUserHierarchyStructureResponseHierarchyStructureLevelFiveTypeDef,
    },
    total=False,
)


class ClientDescribeUserHierarchyStructureResponseHierarchyStructureTypeDef(
    _ClientDescribeUserHierarchyStructureResponseHierarchyStructureTypeDef
):
    """
    Type definition for `ClientDescribeUserHierarchyStructureResponse` `HierarchyStructure`

    Information about the hierarchy structure.

    - **LevelOne** *(dict) --*

      Information about level one.

      - **Id** *(string) --*

        The identifier of the hierarchy level.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the hierarchy level.

      - **Name** *(string) --*

        The name of the hierarchy level.

    - **LevelTwo** *(dict) --*

      Information about level two.

      - **Id** *(string) --*

        The identifier of the hierarchy level.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the hierarchy level.

      - **Name** *(string) --*

        The name of the hierarchy level.

    - **LevelThree** *(dict) --*

      Information about level three.

      - **Id** *(string) --*

        The identifier of the hierarchy level.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the hierarchy level.

      - **Name** *(string) --*

        The name of the hierarchy level.

    - **LevelFour** *(dict) --*

      Information about level four.

      - **Id** *(string) --*

        The identifier of the hierarchy level.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the hierarchy level.

      - **Name** *(string) --*

        The name of the hierarchy level.

    - **LevelFive** *(dict) --*

      Information about level five.

      - **Id** *(string) --*

        The identifier of the hierarchy level.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the hierarchy level.

      - **Name** *(string) --*

        The name of the hierarchy level.
    """


_ClientDescribeUserHierarchyStructureResponseTypeDef = TypedDict(
    "_ClientDescribeUserHierarchyStructureResponseTypeDef",
    {
        "HierarchyStructure": ClientDescribeUserHierarchyStructureResponseHierarchyStructureTypeDef
    },
    total=False,
)


class ClientDescribeUserHierarchyStructureResponseTypeDef(
    _ClientDescribeUserHierarchyStructureResponseTypeDef
):
    """
    Type definition for `ClientDescribeUserHierarchyStructure` `Response`

    - **HierarchyStructure** *(dict) --*

      Information about the hierarchy structure.

      - **LevelOne** *(dict) --*

        Information about level one.

        - **Id** *(string) --*

          The identifier of the hierarchy level.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the hierarchy level.

        - **Name** *(string) --*

          The name of the hierarchy level.

      - **LevelTwo** *(dict) --*

        Information about level two.

        - **Id** *(string) --*

          The identifier of the hierarchy level.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the hierarchy level.

        - **Name** *(string) --*

          The name of the hierarchy level.

      - **LevelThree** *(dict) --*

        Information about level three.

        - **Id** *(string) --*

          The identifier of the hierarchy level.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the hierarchy level.

        - **Name** *(string) --*

          The name of the hierarchy level.

      - **LevelFour** *(dict) --*

        Information about level four.

        - **Id** *(string) --*

          The identifier of the hierarchy level.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the hierarchy level.

        - **Name** *(string) --*

          The name of the hierarchy level.

      - **LevelFive** *(dict) --*

        Information about level five.

        - **Id** *(string) --*

          The identifier of the hierarchy level.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the hierarchy level.

        - **Name** *(string) --*

          The name of the hierarchy level.
    """


_ClientDescribeUserResponseUserIdentityInfoTypeDef = TypedDict(
    "_ClientDescribeUserResponseUserIdentityInfoTypeDef",
    {"FirstName": str, "LastName": str, "Email": str},
    total=False,
)


class ClientDescribeUserResponseUserIdentityInfoTypeDef(
    _ClientDescribeUserResponseUserIdentityInfoTypeDef
):
    """
    Type definition for `ClientDescribeUserResponseUser` `IdentityInfo`

    Information about the user identity.

    - **FirstName** *(string) --*

      The first name. This is required if you are using Amazon Connect or SAML for identity
      management.

    - **LastName** *(string) --*

      The last name. This is required if you are using Amazon Connect or SAML for identity
      management.

    - **Email** *(string) --*

      The email address. If you are using SAML for identity management and include this
      parameter, an error is returned.
    """


_ClientDescribeUserResponseUserPhoneConfigTypeDef = TypedDict(
    "_ClientDescribeUserResponseUserPhoneConfigTypeDef",
    {
        "PhoneType": str,
        "AutoAccept": bool,
        "AfterContactWorkTimeLimit": int,
        "DeskPhoneNumber": str,
    },
    total=False,
)


class ClientDescribeUserResponseUserPhoneConfigTypeDef(
    _ClientDescribeUserResponseUserPhoneConfigTypeDef
):
    """
    Type definition for `ClientDescribeUserResponseUser` `PhoneConfig`

    Information about the phone configuration for the user.

    - **PhoneType** *(string) --*

      The phone type.

    - **AutoAccept** *(boolean) --*

      The Auto accept setting.

    - **AfterContactWorkTimeLimit** *(integer) --*

      The After Call Work (ACW) timeout setting, in seconds.

    - **DeskPhoneNumber** *(string) --*

      The phone number for the user's desk phone.
    """


_ClientDescribeUserResponseUserTypeDef = TypedDict(
    "_ClientDescribeUserResponseUserTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Username": str,
        "IdentityInfo": ClientDescribeUserResponseUserIdentityInfoTypeDef,
        "PhoneConfig": ClientDescribeUserResponseUserPhoneConfigTypeDef,
        "DirectoryUserId": str,
        "SecurityProfileIds": List[str],
        "RoutingProfileId": str,
        "HierarchyGroupId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeUserResponseUserTypeDef(_ClientDescribeUserResponseUserTypeDef):
    """
    Type definition for `ClientDescribeUserResponse` `User`

    Information about the user account and configuration settings.

    - **Id** *(string) --*

      The identifier of the user account.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the user account.

    - **Username** *(string) --*

      The user name assigned to the user account.

    - **IdentityInfo** *(dict) --*

      Information about the user identity.

      - **FirstName** *(string) --*

        The first name. This is required if you are using Amazon Connect or SAML for identity
        management.

      - **LastName** *(string) --*

        The last name. This is required if you are using Amazon Connect or SAML for identity
        management.

      - **Email** *(string) --*

        The email address. If you are using SAML for identity management and include this
        parameter, an error is returned.

    - **PhoneConfig** *(dict) --*

      Information about the phone configuration for the user.

      - **PhoneType** *(string) --*

        The phone type.

      - **AutoAccept** *(boolean) --*

        The Auto accept setting.

      - **AfterContactWorkTimeLimit** *(integer) --*

        The After Call Work (ACW) timeout setting, in seconds.

      - **DeskPhoneNumber** *(string) --*

        The phone number for the user's desk phone.

    - **DirectoryUserId** *(string) --*

      The identifier of the user account in the directory used for identity management.

    - **SecurityProfileIds** *(list) --*

      The identifiers of the security profiles for the user.

      - *(string) --*

    - **RoutingProfileId** *(string) --*

      The identifier of the routing profile for the user.

    - **HierarchyGroupId** *(string) --*

      The identifier of the hierarchy group for the user.

    - **Tags** *(dict) --*

      The tags.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeUserResponseTypeDef = TypedDict(
    "_ClientDescribeUserResponseTypeDef",
    {"User": ClientDescribeUserResponseUserTypeDef},
    total=False,
)


class ClientDescribeUserResponseTypeDef(_ClientDescribeUserResponseTypeDef):
    """
    Type definition for `ClientDescribeUser` `Response`

    - **User** *(dict) --*

      Information about the user account and configuration settings.

      - **Id** *(string) --*

        The identifier of the user account.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the user account.

      - **Username** *(string) --*

        The user name assigned to the user account.

      - **IdentityInfo** *(dict) --*

        Information about the user identity.

        - **FirstName** *(string) --*

          The first name. This is required if you are using Amazon Connect or SAML for identity
          management.

        - **LastName** *(string) --*

          The last name. This is required if you are using Amazon Connect or SAML for identity
          management.

        - **Email** *(string) --*

          The email address. If you are using SAML for identity management and include this
          parameter, an error is returned.

      - **PhoneConfig** *(dict) --*

        Information about the phone configuration for the user.

        - **PhoneType** *(string) --*

          The phone type.

        - **AutoAccept** *(boolean) --*

          The Auto accept setting.

        - **AfterContactWorkTimeLimit** *(integer) --*

          The After Call Work (ACW) timeout setting, in seconds.

        - **DeskPhoneNumber** *(string) --*

          The phone number for the user's desk phone.

      - **DirectoryUserId** *(string) --*

        The identifier of the user account in the directory used for identity management.

      - **SecurityProfileIds** *(list) --*

        The identifiers of the security profiles for the user.

        - *(string) --*

      - **RoutingProfileId** *(string) --*

        The identifier of the routing profile for the user.

      - **HierarchyGroupId** *(string) --*

        The identifier of the hierarchy group for the user.

      - **Tags** *(dict) --*

        The tags.

        - *(string) --*

          - *(string) --*
    """


_ClientGetContactAttributesResponseTypeDef = TypedDict(
    "_ClientGetContactAttributesResponseTypeDef",
    {"Attributes": Dict[str, str]},
    total=False,
)


class ClientGetContactAttributesResponseTypeDef(
    _ClientGetContactAttributesResponseTypeDef
):
    """
    Type definition for `ClientGetContactAttributes` `Response`

    - **Attributes** *(dict) --*

      Information about the attributes.

      - *(string) --*

        - *(string) --*
    """


_ClientGetCurrentMetricDataCurrentMetricsTypeDef = TypedDict(
    "_ClientGetCurrentMetricDataCurrentMetricsTypeDef",
    {"Name": str, "Unit": str},
    total=False,
)


class ClientGetCurrentMetricDataCurrentMetricsTypeDef(
    _ClientGetCurrentMetricDataCurrentMetricsTypeDef
):
    """
    Type definition for `ClientGetCurrentMetricData` `CurrentMetrics`

    Contains information about a real-time metric.

    - **Name** *(string) --*

      The name of the metric.

    - **Unit** *(string) --*

      The unit for the metric.
    """


_ClientGetCurrentMetricDataFiltersTypeDef = TypedDict(
    "_ClientGetCurrentMetricDataFiltersTypeDef",
    {"Queues": List[str], "Channels": List[str]},
    total=False,
)


class ClientGetCurrentMetricDataFiltersTypeDef(
    _ClientGetCurrentMetricDataFiltersTypeDef
):
    """
    Type definition for `ClientGetCurrentMetricData` `Filters`

    The queues, up to 100, or channels, to use to filter the metrics returned. Metric data is
    retrieved only for the resources associated with the queues or channels included in the filter.
    You can include both queue IDs and queue ARNs in the same request. The only supported channel is
    ``VOICE`` .

    - **Queues** *(list) --*

      The queues to use to filter the metrics. You can specify up to 100 queues per request.

      - *(string) --*

    - **Channels** *(list) --*

      The channel to use to filter the metrics.

      - *(string) --*
    """


_ClientGetCurrentMetricDataResponseMetricResultsCollectionsMetricTypeDef = TypedDict(
    "_ClientGetCurrentMetricDataResponseMetricResultsCollectionsMetricTypeDef",
    {"Name": str, "Unit": str},
    total=False,
)


class ClientGetCurrentMetricDataResponseMetricResultsCollectionsMetricTypeDef(
    _ClientGetCurrentMetricDataResponseMetricResultsCollectionsMetricTypeDef
):
    """
    Type definition for `ClientGetCurrentMetricDataResponseMetricResultsCollections` `Metric`

    Information about the metric.

    - **Name** *(string) --*

      The name of the metric.

    - **Unit** *(string) --*

      The unit for the metric.
    """


_ClientGetCurrentMetricDataResponseMetricResultsCollectionsTypeDef = TypedDict(
    "_ClientGetCurrentMetricDataResponseMetricResultsCollectionsTypeDef",
    {
        "Metric": ClientGetCurrentMetricDataResponseMetricResultsCollectionsMetricTypeDef,
        "Value": float,
    },
    total=False,
)


class ClientGetCurrentMetricDataResponseMetricResultsCollectionsTypeDef(
    _ClientGetCurrentMetricDataResponseMetricResultsCollectionsTypeDef
):
    """
    Type definition for `ClientGetCurrentMetricDataResponseMetricResults` `Collections`

    Contains the data for a real-time metric.

    - **Metric** *(dict) --*

      Information about the metric.

      - **Name** *(string) --*

        The name of the metric.

      - **Unit** *(string) --*

        The unit for the metric.

    - **Value** *(float) --*

      The value of the metric.
    """


_ClientGetCurrentMetricDataResponseMetricResultsDimensionsQueueTypeDef = TypedDict(
    "_ClientGetCurrentMetricDataResponseMetricResultsDimensionsQueueTypeDef",
    {"Id": str, "Arn": str},
    total=False,
)


class ClientGetCurrentMetricDataResponseMetricResultsDimensionsQueueTypeDef(
    _ClientGetCurrentMetricDataResponseMetricResultsDimensionsQueueTypeDef
):
    """
    Type definition for `ClientGetCurrentMetricDataResponseMetricResultsDimensions` `Queue`

    Information about the queue for which metrics are returned.

    - **Id** *(string) --*

      The identifier of the queue.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the queue.
    """


_ClientGetCurrentMetricDataResponseMetricResultsDimensionsTypeDef = TypedDict(
    "_ClientGetCurrentMetricDataResponseMetricResultsDimensionsTypeDef",
    {
        "Queue": ClientGetCurrentMetricDataResponseMetricResultsDimensionsQueueTypeDef,
        "Channel": str,
    },
    total=False,
)


class ClientGetCurrentMetricDataResponseMetricResultsDimensionsTypeDef(
    _ClientGetCurrentMetricDataResponseMetricResultsDimensionsTypeDef
):
    """
    Type definition for `ClientGetCurrentMetricDataResponseMetricResults` `Dimensions`

    The dimensions for the metrics.

    - **Queue** *(dict) --*

      Information about the queue for which metrics are returned.

      - **Id** *(string) --*

        The identifier of the queue.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the queue.

    - **Channel** *(string) --*

      The channel used for grouping and filters.
    """


_ClientGetCurrentMetricDataResponseMetricResultsTypeDef = TypedDict(
    "_ClientGetCurrentMetricDataResponseMetricResultsTypeDef",
    {
        "Dimensions": ClientGetCurrentMetricDataResponseMetricResultsDimensionsTypeDef,
        "Collections": List[
            ClientGetCurrentMetricDataResponseMetricResultsCollectionsTypeDef
        ],
    },
    total=False,
)


class ClientGetCurrentMetricDataResponseMetricResultsTypeDef(
    _ClientGetCurrentMetricDataResponseMetricResultsTypeDef
):
    """
    Type definition for `ClientGetCurrentMetricDataResponse` `MetricResults`

    Contains information about a set of real-time metrics.

    - **Dimensions** *(dict) --*

      The dimensions for the metrics.

      - **Queue** *(dict) --*

        Information about the queue for which metrics are returned.

        - **Id** *(string) --*

          The identifier of the queue.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the queue.

      - **Channel** *(string) --*

        The channel used for grouping and filters.

    - **Collections** *(list) --*

      The set of metrics.

      - *(dict) --*

        Contains the data for a real-time metric.

        - **Metric** *(dict) --*

          Information about the metric.

          - **Name** *(string) --*

            The name of the metric.

          - **Unit** *(string) --*

            The unit for the metric.

        - **Value** *(float) --*

          The value of the metric.
    """


_ClientGetCurrentMetricDataResponseTypeDef = TypedDict(
    "_ClientGetCurrentMetricDataResponseTypeDef",
    {
        "NextToken": str,
        "MetricResults": List[ClientGetCurrentMetricDataResponseMetricResultsTypeDef],
        "DataSnapshotTime": datetime,
    },
    total=False,
)


class ClientGetCurrentMetricDataResponseTypeDef(
    _ClientGetCurrentMetricDataResponseTypeDef
):
    """
    Type definition for `ClientGetCurrentMetricData` `Response`

    - **NextToken** *(string) --*

      If there are additional results, this is the token for the next set of results.

      The token expires after 5 minutes from the time it is created. Subsequent requests that use
      the token must use the same request parameters as the request that generated the token.

    - **MetricResults** *(list) --*

      Information about the real-time metrics.

      - *(dict) --*

        Contains information about a set of real-time metrics.

        - **Dimensions** *(dict) --*

          The dimensions for the metrics.

          - **Queue** *(dict) --*

            Information about the queue for which metrics are returned.

            - **Id** *(string) --*

              The identifier of the queue.

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) of the queue.

          - **Channel** *(string) --*

            The channel used for grouping and filters.

        - **Collections** *(list) --*

          The set of metrics.

          - *(dict) --*

            Contains the data for a real-time metric.

            - **Metric** *(dict) --*

              Information about the metric.

              - **Name** *(string) --*

                The name of the metric.

              - **Unit** *(string) --*

                The unit for the metric.

            - **Value** *(float) --*

              The value of the metric.

    - **DataSnapshotTime** *(datetime) --*

      The time at which the metrics were retrieved and cached for pagination.
    """


_ClientGetFederationTokenResponseCredentialsTypeDef = TypedDict(
    "_ClientGetFederationTokenResponseCredentialsTypeDef",
    {
        "AccessToken": str,
        "AccessTokenExpiration": datetime,
        "RefreshToken": str,
        "RefreshTokenExpiration": datetime,
    },
    total=False,
)


class ClientGetFederationTokenResponseCredentialsTypeDef(
    _ClientGetFederationTokenResponseCredentialsTypeDef
):
    """
    Type definition for `ClientGetFederationTokenResponse` `Credentials`

    The credentials to use for federation.

    - **AccessToken** *(string) --*

      An access token generated for a federated user to access Amazon Connect.

    - **AccessTokenExpiration** *(datetime) --*

      A token generated with an expiration time for the session a user is logged in to Amazon
      Connect.

    - **RefreshToken** *(string) --*

      Renews a token generated for a user to access the Amazon Connect instance.

    - **RefreshTokenExpiration** *(datetime) --*

      Renews the expiration timer for a generated token.
    """


_ClientGetFederationTokenResponseTypeDef = TypedDict(
    "_ClientGetFederationTokenResponseTypeDef",
    {"Credentials": ClientGetFederationTokenResponseCredentialsTypeDef},
    total=False,
)


class ClientGetFederationTokenResponseTypeDef(_ClientGetFederationTokenResponseTypeDef):
    """
    Type definition for `ClientGetFederationToken` `Response`

    - **Credentials** *(dict) --*

      The credentials to use for federation.

      - **AccessToken** *(string) --*

        An access token generated for a federated user to access Amazon Connect.

      - **AccessTokenExpiration** *(datetime) --*

        A token generated with an expiration time for the session a user is logged in to Amazon
        Connect.

      - **RefreshToken** *(string) --*

        Renews a token generated for a user to access the Amazon Connect instance.

      - **RefreshTokenExpiration** *(datetime) --*

        Renews the expiration timer for a generated token.
    """


_ClientGetMetricDataFiltersTypeDef = TypedDict(
    "_ClientGetMetricDataFiltersTypeDef",
    {"Queues": List[str], "Channels": List[str]},
    total=False,
)


class ClientGetMetricDataFiltersTypeDef(_ClientGetMetricDataFiltersTypeDef):
    """
    Type definition for `ClientGetMetricData` `Filters`

    The queues, up to 100, or channels, to use to filter the metrics returned. Metric data is
    retrieved only for the resources associated with the queues or channels included in the filter.
    You can include both queue IDs and queue ARNs in the same request. The only supported channel is
    ``VOICE`` .

    - **Queues** *(list) --*

      The queues to use to filter the metrics. You can specify up to 100 queues per request.

      - *(string) --*

    - **Channels** *(list) --*

      The channel to use to filter the metrics.

      - *(string) --*
    """


_ClientGetMetricDataHistoricalMetricsThresholdTypeDef = TypedDict(
    "_ClientGetMetricDataHistoricalMetricsThresholdTypeDef",
    {"Comparison": str, "ThresholdValue": float},
    total=False,
)


class ClientGetMetricDataHistoricalMetricsThresholdTypeDef(
    _ClientGetMetricDataHistoricalMetricsThresholdTypeDef
):
    """
    Type definition for `ClientGetMetricDataHistoricalMetrics` `Threshold`

    The threshold for the metric, used with service level metrics.

    - **Comparison** *(string) --*

      The type of comparison. Only "less than" (LT) comparisons are supported.

    - **ThresholdValue** *(float) --*

      The threshold value to compare.
    """


_ClientGetMetricDataHistoricalMetricsTypeDef = TypedDict(
    "_ClientGetMetricDataHistoricalMetricsTypeDef",
    {
        "Name": str,
        "Threshold": ClientGetMetricDataHistoricalMetricsThresholdTypeDef,
        "Statistic": str,
        "Unit": str,
    },
    total=False,
)


class ClientGetMetricDataHistoricalMetricsTypeDef(
    _ClientGetMetricDataHistoricalMetricsTypeDef
):
    """
    Type definition for `ClientGetMetricData` `HistoricalMetrics`

    Contains information about a historical metric.

    - **Name** *(string) --*

      The name of the metric.

    - **Threshold** *(dict) --*

      The threshold for the metric, used with service level metrics.

      - **Comparison** *(string) --*

        The type of comparison. Only "less than" (LT) comparisons are supported.

      - **ThresholdValue** *(float) --*

        The threshold value to compare.

    - **Statistic** *(string) --*

      The statistic for the metric.

    - **Unit** *(string) --*

      The unit for the metric.
    """


_ClientGetMetricDataResponseMetricResultsCollectionsMetricThresholdTypeDef = TypedDict(
    "_ClientGetMetricDataResponseMetricResultsCollectionsMetricThresholdTypeDef",
    {"Comparison": str, "ThresholdValue": float},
    total=False,
)


class ClientGetMetricDataResponseMetricResultsCollectionsMetricThresholdTypeDef(
    _ClientGetMetricDataResponseMetricResultsCollectionsMetricThresholdTypeDef
):
    """
    Type definition for `ClientGetMetricDataResponseMetricResultsCollectionsMetric` `Threshold`

    The threshold for the metric, used with service level metrics.

    - **Comparison** *(string) --*

      The type of comparison. Only "less than" (LT) comparisons are supported.

    - **ThresholdValue** *(float) --*

      The threshold value to compare.
    """


_ClientGetMetricDataResponseMetricResultsCollectionsMetricTypeDef = TypedDict(
    "_ClientGetMetricDataResponseMetricResultsCollectionsMetricTypeDef",
    {
        "Name": str,
        "Threshold": ClientGetMetricDataResponseMetricResultsCollectionsMetricThresholdTypeDef,
        "Statistic": str,
        "Unit": str,
    },
    total=False,
)


class ClientGetMetricDataResponseMetricResultsCollectionsMetricTypeDef(
    _ClientGetMetricDataResponseMetricResultsCollectionsMetricTypeDef
):
    """
    Type definition for `ClientGetMetricDataResponseMetricResultsCollections` `Metric`

    Information about the metric.

    - **Name** *(string) --*

      The name of the metric.

    - **Threshold** *(dict) --*

      The threshold for the metric, used with service level metrics.

      - **Comparison** *(string) --*

        The type of comparison. Only "less than" (LT) comparisons are supported.

      - **ThresholdValue** *(float) --*

        The threshold value to compare.

    - **Statistic** *(string) --*

      The statistic for the metric.

    - **Unit** *(string) --*

      The unit for the metric.
    """


_ClientGetMetricDataResponseMetricResultsCollectionsTypeDef = TypedDict(
    "_ClientGetMetricDataResponseMetricResultsCollectionsTypeDef",
    {
        "Metric": ClientGetMetricDataResponseMetricResultsCollectionsMetricTypeDef,
        "Value": float,
    },
    total=False,
)


class ClientGetMetricDataResponseMetricResultsCollectionsTypeDef(
    _ClientGetMetricDataResponseMetricResultsCollectionsTypeDef
):
    """
    Type definition for `ClientGetMetricDataResponseMetricResults` `Collections`

    Contains the data for a historical metric.

    - **Metric** *(dict) --*

      Information about the metric.

      - **Name** *(string) --*

        The name of the metric.

      - **Threshold** *(dict) --*

        The threshold for the metric, used with service level metrics.

        - **Comparison** *(string) --*

          The type of comparison. Only "less than" (LT) comparisons are supported.

        - **ThresholdValue** *(float) --*

          The threshold value to compare.

      - **Statistic** *(string) --*

        The statistic for the metric.

      - **Unit** *(string) --*

        The unit for the metric.

    - **Value** *(float) --*

      The value of the metric.
    """


_ClientGetMetricDataResponseMetricResultsDimensionsQueueTypeDef = TypedDict(
    "_ClientGetMetricDataResponseMetricResultsDimensionsQueueTypeDef",
    {"Id": str, "Arn": str},
    total=False,
)


class ClientGetMetricDataResponseMetricResultsDimensionsQueueTypeDef(
    _ClientGetMetricDataResponseMetricResultsDimensionsQueueTypeDef
):
    """
    Type definition for `ClientGetMetricDataResponseMetricResultsDimensions` `Queue`

    Information about the queue for which metrics are returned.

    - **Id** *(string) --*

      The identifier of the queue.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the queue.
    """


_ClientGetMetricDataResponseMetricResultsDimensionsTypeDef = TypedDict(
    "_ClientGetMetricDataResponseMetricResultsDimensionsTypeDef",
    {
        "Queue": ClientGetMetricDataResponseMetricResultsDimensionsQueueTypeDef,
        "Channel": str,
    },
    total=False,
)


class ClientGetMetricDataResponseMetricResultsDimensionsTypeDef(
    _ClientGetMetricDataResponseMetricResultsDimensionsTypeDef
):
    """
    Type definition for `ClientGetMetricDataResponseMetricResults` `Dimensions`

    The dimension for the metrics.

    - **Queue** *(dict) --*

      Information about the queue for which metrics are returned.

      - **Id** *(string) --*

        The identifier of the queue.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the queue.

    - **Channel** *(string) --*

      The channel used for grouping and filters.
    """


_ClientGetMetricDataResponseMetricResultsTypeDef = TypedDict(
    "_ClientGetMetricDataResponseMetricResultsTypeDef",
    {
        "Dimensions": ClientGetMetricDataResponseMetricResultsDimensionsTypeDef,
        "Collections": List[ClientGetMetricDataResponseMetricResultsCollectionsTypeDef],
    },
    total=False,
)


class ClientGetMetricDataResponseMetricResultsTypeDef(
    _ClientGetMetricDataResponseMetricResultsTypeDef
):
    """
    Type definition for `ClientGetMetricDataResponse` `MetricResults`

    Contains information about the historical metrics retrieved.

    - **Dimensions** *(dict) --*

      The dimension for the metrics.

      - **Queue** *(dict) --*

        Information about the queue for which metrics are returned.

        - **Id** *(string) --*

          The identifier of the queue.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the queue.

      - **Channel** *(string) --*

        The channel used for grouping and filters.

    - **Collections** *(list) --*

      The set of metrics.

      - *(dict) --*

        Contains the data for a historical metric.

        - **Metric** *(dict) --*

          Information about the metric.

          - **Name** *(string) --*

            The name of the metric.

          - **Threshold** *(dict) --*

            The threshold for the metric, used with service level metrics.

            - **Comparison** *(string) --*

              The type of comparison. Only "less than" (LT) comparisons are supported.

            - **ThresholdValue** *(float) --*

              The threshold value to compare.

          - **Statistic** *(string) --*

            The statistic for the metric.

          - **Unit** *(string) --*

            The unit for the metric.

        - **Value** *(float) --*

          The value of the metric.
    """


_ClientGetMetricDataResponseTypeDef = TypedDict(
    "_ClientGetMetricDataResponseTypeDef",
    {
        "NextToken": str,
        "MetricResults": List[ClientGetMetricDataResponseMetricResultsTypeDef],
    },
    total=False,
)


class ClientGetMetricDataResponseTypeDef(_ClientGetMetricDataResponseTypeDef):
    """
    Type definition for `ClientGetMetricData` `Response`

    - **NextToken** *(string) --*

      If there are additional results, this is the token for the next set of results.

      The token expires after 5 minutes from the time it is created. Subsequent requests that use
      the token must use the same request parameters as the request that generated the token.

    - **MetricResults** *(list) --*

      Information about the historical metrics.

      If no grouping is specified, a summary of metric data is returned.

      - *(dict) --*

        Contains information about the historical metrics retrieved.

        - **Dimensions** *(dict) --*

          The dimension for the metrics.

          - **Queue** *(dict) --*

            Information about the queue for which metrics are returned.

            - **Id** *(string) --*

              The identifier of the queue.

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) of the queue.

          - **Channel** *(string) --*

            The channel used for grouping and filters.

        - **Collections** *(list) --*

          The set of metrics.

          - *(dict) --*

            Contains the data for a historical metric.

            - **Metric** *(dict) --*

              Information about the metric.

              - **Name** *(string) --*

                The name of the metric.

              - **Threshold** *(dict) --*

                The threshold for the metric, used with service level metrics.

                - **Comparison** *(string) --*

                  The type of comparison. Only "less than" (LT) comparisons are supported.

                - **ThresholdValue** *(float) --*

                  The threshold value to compare.

              - **Statistic** *(string) --*

                The statistic for the metric.

              - **Unit** *(string) --*

                The unit for the metric.

            - **Value** *(float) --*

              The value of the metric.
    """


_ClientListContactFlowsResponseContactFlowSummaryListTypeDef = TypedDict(
    "_ClientListContactFlowsResponseContactFlowSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str, "ContactFlowType": str},
    total=False,
)


class ClientListContactFlowsResponseContactFlowSummaryListTypeDef(
    _ClientListContactFlowsResponseContactFlowSummaryListTypeDef
):
    """
    Type definition for `ClientListContactFlowsResponse` `ContactFlowSummaryList`

    Contains summary information about a contact flow.

    - **Id** *(string) --*

      The identifier of the contact flow.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the contact flow.

    - **Name** *(string) --*

      The name of the contact flow.

    - **ContactFlowType** *(string) --*

      The type of contact flow.
    """


_ClientListContactFlowsResponseTypeDef = TypedDict(
    "_ClientListContactFlowsResponseTypeDef",
    {
        "ContactFlowSummaryList": List[
            ClientListContactFlowsResponseContactFlowSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListContactFlowsResponseTypeDef(_ClientListContactFlowsResponseTypeDef):
    """
    Type definition for `ClientListContactFlows` `Response`

    - **ContactFlowSummaryList** *(list) --*

      Information about the contact flows.

      - *(dict) --*

        Contains summary information about a contact flow.

        - **Id** *(string) --*

          The identifier of the contact flow.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the contact flow.

        - **Name** *(string) --*

          The name of the contact flow.

        - **ContactFlowType** *(string) --*

          The type of contact flow.

    - **NextToken** *(string) --*

      If there are additional results, this is the token for the next set of results.
    """


_ClientListHoursOfOperationsResponseHoursOfOperationSummaryListTypeDef = TypedDict(
    "_ClientListHoursOfOperationsResponseHoursOfOperationSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientListHoursOfOperationsResponseHoursOfOperationSummaryListTypeDef(
    _ClientListHoursOfOperationsResponseHoursOfOperationSummaryListTypeDef
):
    """
    Type definition for `ClientListHoursOfOperationsResponse` `HoursOfOperationSummaryList`

    Contains summary information about hours of operation for a contact center.

    - **Id** *(string) --*

      The identifier of the hours of operation.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the hours of operation.

    - **Name** *(string) --*

      The name of the hours of operation.
    """


_ClientListHoursOfOperationsResponseTypeDef = TypedDict(
    "_ClientListHoursOfOperationsResponseTypeDef",
    {
        "HoursOfOperationSummaryList": List[
            ClientListHoursOfOperationsResponseHoursOfOperationSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListHoursOfOperationsResponseTypeDef(
    _ClientListHoursOfOperationsResponseTypeDef
):
    """
    Type definition for `ClientListHoursOfOperations` `Response`

    - **HoursOfOperationSummaryList** *(list) --*

      Information about the hours of operation.

      - *(dict) --*

        Contains summary information about hours of operation for a contact center.

        - **Id** *(string) --*

          The identifier of the hours of operation.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the hours of operation.

        - **Name** *(string) --*

          The name of the hours of operation.

    - **NextToken** *(string) --*

      If there are additional results, this is the token for the next set of results.
    """


_ClientListPhoneNumbersResponsePhoneNumberSummaryListTypeDef = TypedDict(
    "_ClientListPhoneNumbersResponsePhoneNumberSummaryListTypeDef",
    {
        "Id": str,
        "Arn": str,
        "PhoneNumber": str,
        "PhoneNumberType": str,
        "PhoneNumberCountryCode": str,
    },
    total=False,
)


class ClientListPhoneNumbersResponsePhoneNumberSummaryListTypeDef(
    _ClientListPhoneNumbersResponsePhoneNumberSummaryListTypeDef
):
    """
    Type definition for `ClientListPhoneNumbersResponse` `PhoneNumberSummaryList`

    Contains summary information about a phone number for a contact center.

    - **Id** *(string) --*

      The identifier of the phone number.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the phone number.

    - **PhoneNumber** *(string) --*

      The phone number.

    - **PhoneNumberType** *(string) --*

      The type of phone number.

    - **PhoneNumberCountryCode** *(string) --*

      The ISO country code.
    """


_ClientListPhoneNumbersResponseTypeDef = TypedDict(
    "_ClientListPhoneNumbersResponseTypeDef",
    {
        "PhoneNumberSummaryList": List[
            ClientListPhoneNumbersResponsePhoneNumberSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListPhoneNumbersResponseTypeDef(_ClientListPhoneNumbersResponseTypeDef):
    """
    Type definition for `ClientListPhoneNumbers` `Response`

    - **PhoneNumberSummaryList** *(list) --*

      Information about the phone numbers.

      - *(dict) --*

        Contains summary information about a phone number for a contact center.

        - **Id** *(string) --*

          The identifier of the phone number.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the phone number.

        - **PhoneNumber** *(string) --*

          The phone number.

        - **PhoneNumberType** *(string) --*

          The type of phone number.

        - **PhoneNumberCountryCode** *(string) --*

          The ISO country code.

    - **NextToken** *(string) --*

      If there are additional results, this is the token for the next set of results.
    """


_ClientListQueuesResponseQueueSummaryListTypeDef = TypedDict(
    "_ClientListQueuesResponseQueueSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str, "QueueType": str},
    total=False,
)


class ClientListQueuesResponseQueueSummaryListTypeDef(
    _ClientListQueuesResponseQueueSummaryListTypeDef
):
    """
    Type definition for `ClientListQueuesResponse` `QueueSummaryList`

    Contains summary information about a queue.

    - **Id** *(string) --*

      The identifier of the queue.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the queue.

    - **Name** *(string) --*

      The name of the queue.

    - **QueueType** *(string) --*

      The type of queue.
    """


_ClientListQueuesResponseTypeDef = TypedDict(
    "_ClientListQueuesResponseTypeDef",
    {
        "QueueSummaryList": List[ClientListQueuesResponseQueueSummaryListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListQueuesResponseTypeDef(_ClientListQueuesResponseTypeDef):
    """
    Type definition for `ClientListQueues` `Response`

    - **QueueSummaryList** *(list) --*

      Information about the queues.

      - *(dict) --*

        Contains summary information about a queue.

        - **Id** *(string) --*

          The identifier of the queue.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the queue.

        - **Name** *(string) --*

          The name of the queue.

        - **QueueType** *(string) --*

          The type of queue.

    - **NextToken** *(string) --*

      If there are additional results, this is the token for the next set of results.
    """


_ClientListRoutingProfilesResponseRoutingProfileSummaryListTypeDef = TypedDict(
    "_ClientListRoutingProfilesResponseRoutingProfileSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientListRoutingProfilesResponseRoutingProfileSummaryListTypeDef(
    _ClientListRoutingProfilesResponseRoutingProfileSummaryListTypeDef
):
    """
    Type definition for `ClientListRoutingProfilesResponse` `RoutingProfileSummaryList`

    Contains summary information about a routing profile.

    - **Id** *(string) --*

      The identifier of the routing profile.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the routing profile.

    - **Name** *(string) --*

      The name of the routing profile.
    """


_ClientListRoutingProfilesResponseTypeDef = TypedDict(
    "_ClientListRoutingProfilesResponseTypeDef",
    {
        "RoutingProfileSummaryList": List[
            ClientListRoutingProfilesResponseRoutingProfileSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListRoutingProfilesResponseTypeDef(
    _ClientListRoutingProfilesResponseTypeDef
):
    """
    Type definition for `ClientListRoutingProfiles` `Response`

    - **RoutingProfileSummaryList** *(list) --*

      Information about the routing profiles.

      - *(dict) --*

        Contains summary information about a routing profile.

        - **Id** *(string) --*

          The identifier of the routing profile.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the routing profile.

        - **Name** *(string) --*

          The name of the routing profile.

    - **NextToken** *(string) --*

      If there are additional results, this is the token for the next set of results.
    """


_ClientListSecurityProfilesResponseSecurityProfileSummaryListTypeDef = TypedDict(
    "_ClientListSecurityProfilesResponseSecurityProfileSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientListSecurityProfilesResponseSecurityProfileSummaryListTypeDef(
    _ClientListSecurityProfilesResponseSecurityProfileSummaryListTypeDef
):
    """
    Type definition for `ClientListSecurityProfilesResponse` `SecurityProfileSummaryList`

    Contains information about a security profile.

    - **Id** *(string) --*

      The identifier of the security profile.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the security profile.

    - **Name** *(string) --*

      The name of the security profile.
    """


_ClientListSecurityProfilesResponseTypeDef = TypedDict(
    "_ClientListSecurityProfilesResponseTypeDef",
    {
        "SecurityProfileSummaryList": List[
            ClientListSecurityProfilesResponseSecurityProfileSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListSecurityProfilesResponseTypeDef(
    _ClientListSecurityProfilesResponseTypeDef
):
    """
    Type definition for `ClientListSecurityProfiles` `Response`

    - **SecurityProfileSummaryList** *(list) --*

      Information about the security profiles.

      - *(dict) --*

        Contains information about a security profile.

        - **Id** *(string) --*

          The identifier of the security profile.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the security profile.

        - **Name** *(string) --*

          The name of the security profile.

    - **NextToken** *(string) --*

      If there are additional results, this is the token for the next set of results.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **tags** *(dict) --*

      Information about the tags.

      - *(string) --*

        - *(string) --*
    """


_ClientListUserHierarchyGroupsResponseUserHierarchyGroupSummaryListTypeDef = TypedDict(
    "_ClientListUserHierarchyGroupsResponseUserHierarchyGroupSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ClientListUserHierarchyGroupsResponseUserHierarchyGroupSummaryListTypeDef(
    _ClientListUserHierarchyGroupsResponseUserHierarchyGroupSummaryListTypeDef
):
    """
    Type definition for `ClientListUserHierarchyGroupsResponse` `UserHierarchyGroupSummaryList`

    Contains summary information about a hierarchy group.

    - **Id** *(string) --*

      The identifier of the hierarchy group.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the hierarchy group.

    - **Name** *(string) --*

      The name of the hierarchy group.
    """


_ClientListUserHierarchyGroupsResponseTypeDef = TypedDict(
    "_ClientListUserHierarchyGroupsResponseTypeDef",
    {
        "UserHierarchyGroupSummaryList": List[
            ClientListUserHierarchyGroupsResponseUserHierarchyGroupSummaryListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListUserHierarchyGroupsResponseTypeDef(
    _ClientListUserHierarchyGroupsResponseTypeDef
):
    """
    Type definition for `ClientListUserHierarchyGroups` `Response`

    - **UserHierarchyGroupSummaryList** *(list) --*

      Information about the hierarchy groups.

      - *(dict) --*

        Contains summary information about a hierarchy group.

        - **Id** *(string) --*

          The identifier of the hierarchy group.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the hierarchy group.

        - **Name** *(string) --*

          The name of the hierarchy group.

    - **NextToken** *(string) --*

      If there are additional results, this is the token for the next set of results.
    """


_ClientListUsersResponseUserSummaryListTypeDef = TypedDict(
    "_ClientListUsersResponseUserSummaryListTypeDef",
    {"Id": str, "Arn": str, "Username": str},
    total=False,
)


class ClientListUsersResponseUserSummaryListTypeDef(
    _ClientListUsersResponseUserSummaryListTypeDef
):
    """
    Type definition for `ClientListUsersResponse` `UserSummaryList`

    Contains summary information about a user.

    - **Id** *(string) --*

      The identifier of the user account.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the user account.

    - **Username** *(string) --*

      The Amazon Connect user name of the user account.
    """


_ClientListUsersResponseTypeDef = TypedDict(
    "_ClientListUsersResponseTypeDef",
    {
        "UserSummaryList": List[ClientListUsersResponseUserSummaryListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListUsersResponseTypeDef(_ClientListUsersResponseTypeDef):
    """
    Type definition for `ClientListUsers` `Response`

    - **UserSummaryList** *(list) --*

      Information about the users.

      - *(dict) --*

        Contains summary information about a user.

        - **Id** *(string) --*

          The identifier of the user account.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the user account.

        - **Username** *(string) --*

          The Amazon Connect user name of the user account.

    - **NextToken** *(string) --*

      If there are additional results, this is the token for the next set of results.
    """


_ClientStartOutboundVoiceContactResponseTypeDef = TypedDict(
    "_ClientStartOutboundVoiceContactResponseTypeDef", {"ContactId": str}, total=False
)


class ClientStartOutboundVoiceContactResponseTypeDef(
    _ClientStartOutboundVoiceContactResponseTypeDef
):
    """
    Type definition for `ClientStartOutboundVoiceContact` `Response`

    - **ContactId** *(string) --*

      The identifier of this contact within the Amazon Connect instance.
    """


_ClientUpdateUserIdentityInfoIdentityInfoTypeDef = TypedDict(
    "_ClientUpdateUserIdentityInfoIdentityInfoTypeDef",
    {"FirstName": str, "LastName": str, "Email": str},
    total=False,
)


class ClientUpdateUserIdentityInfoIdentityInfoTypeDef(
    _ClientUpdateUserIdentityInfoIdentityInfoTypeDef
):
    """
    Type definition for `ClientUpdateUserIdentityInfo` `IdentityInfo`

    The identity information for the user.

    - **FirstName** *(string) --*

      The first name. This is required if you are using Amazon Connect or SAML for identity
      management.

    - **LastName** *(string) --*

      The last name. This is required if you are using Amazon Connect or SAML for identity management.

    - **Email** *(string) --*

      The email address. If you are using SAML for identity management and include this parameter, an
      error is returned.
    """


_RequiredClientUpdateUserPhoneConfigPhoneConfigTypeDef = TypedDict(
    "_RequiredClientUpdateUserPhoneConfigPhoneConfigTypeDef", {"PhoneType": str}
)
_OptionalClientUpdateUserPhoneConfigPhoneConfigTypeDef = TypedDict(
    "_OptionalClientUpdateUserPhoneConfigPhoneConfigTypeDef",
    {"AutoAccept": bool, "AfterContactWorkTimeLimit": int, "DeskPhoneNumber": str},
    total=False,
)


class ClientUpdateUserPhoneConfigPhoneConfigTypeDef(
    _RequiredClientUpdateUserPhoneConfigPhoneConfigTypeDef,
    _OptionalClientUpdateUserPhoneConfigPhoneConfigTypeDef,
):
    """
    Type definition for `ClientUpdateUserPhoneConfig` `PhoneConfig`

    Information about phone configuration settings for the user.

    - **PhoneType** *(string) --* **[REQUIRED]**

      The phone type.

    - **AutoAccept** *(boolean) --*

      The Auto accept setting.

    - **AfterContactWorkTimeLimit** *(integer) --*

      The After Call Work (ACW) timeout setting, in seconds.

    - **DeskPhoneNumber** *(string) --*

      The phone number for the user's desk phone.
    """


_GetMetricDataPaginateFiltersTypeDef = TypedDict(
    "_GetMetricDataPaginateFiltersTypeDef",
    {"Queues": List[str], "Channels": List[str]},
    total=False,
)


class GetMetricDataPaginateFiltersTypeDef(_GetMetricDataPaginateFiltersTypeDef):
    """
    Type definition for `GetMetricDataPaginate` `Filters`

    The queues, up to 100, or channels, to use to filter the metrics returned. Metric data is
    retrieved only for the resources associated with the queues or channels included in the filter.
    You can include both queue IDs and queue ARNs in the same request. The only supported channel is
    ``VOICE`` .

    - **Queues** *(list) --*

      The queues to use to filter the metrics. You can specify up to 100 queues per request.

      - *(string) --*

    - **Channels** *(list) --*

      The channel to use to filter the metrics.

      - *(string) --*
    """


_GetMetricDataPaginateHistoricalMetricsThresholdTypeDef = TypedDict(
    "_GetMetricDataPaginateHistoricalMetricsThresholdTypeDef",
    {"Comparison": str, "ThresholdValue": float},
    total=False,
)


class GetMetricDataPaginateHistoricalMetricsThresholdTypeDef(
    _GetMetricDataPaginateHistoricalMetricsThresholdTypeDef
):
    """
    Type definition for `GetMetricDataPaginateHistoricalMetrics` `Threshold`

    The threshold for the metric, used with service level metrics.

    - **Comparison** *(string) --*

      The type of comparison. Only "less than" (LT) comparisons are supported.

    - **ThresholdValue** *(float) --*

      The threshold value to compare.
    """


_GetMetricDataPaginateHistoricalMetricsTypeDef = TypedDict(
    "_GetMetricDataPaginateHistoricalMetricsTypeDef",
    {
        "Name": str,
        "Threshold": GetMetricDataPaginateHistoricalMetricsThresholdTypeDef,
        "Statistic": str,
        "Unit": str,
    },
    total=False,
)


class GetMetricDataPaginateHistoricalMetricsTypeDef(
    _GetMetricDataPaginateHistoricalMetricsTypeDef
):
    """
    Type definition for `GetMetricDataPaginate` `HistoricalMetrics`

    Contains information about a historical metric.

    - **Name** *(string) --*

      The name of the metric.

    - **Threshold** *(dict) --*

      The threshold for the metric, used with service level metrics.

      - **Comparison** *(string) --*

        The type of comparison. Only "less than" (LT) comparisons are supported.

      - **ThresholdValue** *(float) --*

        The threshold value to compare.

    - **Statistic** *(string) --*

      The statistic for the metric.

    - **Unit** *(string) --*

      The unit for the metric.
    """


_GetMetricDataPaginatePaginationConfigTypeDef = TypedDict(
    "_GetMetricDataPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class GetMetricDataPaginatePaginationConfigTypeDef(
    _GetMetricDataPaginatePaginationConfigTypeDef
):
    """
    Type definition for `GetMetricDataPaginate` `PaginationConfig`

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


_GetMetricDataPaginateResponseMetricResultsCollectionsMetricThresholdTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseMetricResultsCollectionsMetricThresholdTypeDef",
    {"Comparison": str, "ThresholdValue": float},
    total=False,
)


class GetMetricDataPaginateResponseMetricResultsCollectionsMetricThresholdTypeDef(
    _GetMetricDataPaginateResponseMetricResultsCollectionsMetricThresholdTypeDef
):
    """
    Type definition for `GetMetricDataPaginateResponseMetricResultsCollectionsMetric` `Threshold`

    The threshold for the metric, used with service level metrics.

    - **Comparison** *(string) --*

      The type of comparison. Only "less than" (LT) comparisons are supported.

    - **ThresholdValue** *(float) --*

      The threshold value to compare.
    """


_GetMetricDataPaginateResponseMetricResultsCollectionsMetricTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseMetricResultsCollectionsMetricTypeDef",
    {
        "Name": str,
        "Threshold": GetMetricDataPaginateResponseMetricResultsCollectionsMetricThresholdTypeDef,
        "Statistic": str,
        "Unit": str,
    },
    total=False,
)


class GetMetricDataPaginateResponseMetricResultsCollectionsMetricTypeDef(
    _GetMetricDataPaginateResponseMetricResultsCollectionsMetricTypeDef
):
    """
    Type definition for `GetMetricDataPaginateResponseMetricResultsCollections` `Metric`

    Information about the metric.

    - **Name** *(string) --*

      The name of the metric.

    - **Threshold** *(dict) --*

      The threshold for the metric, used with service level metrics.

      - **Comparison** *(string) --*

        The type of comparison. Only "less than" (LT) comparisons are supported.

      - **ThresholdValue** *(float) --*

        The threshold value to compare.

    - **Statistic** *(string) --*

      The statistic for the metric.

    - **Unit** *(string) --*

      The unit for the metric.
    """


_GetMetricDataPaginateResponseMetricResultsCollectionsTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseMetricResultsCollectionsTypeDef",
    {
        "Metric": GetMetricDataPaginateResponseMetricResultsCollectionsMetricTypeDef,
        "Value": float,
    },
    total=False,
)


class GetMetricDataPaginateResponseMetricResultsCollectionsTypeDef(
    _GetMetricDataPaginateResponseMetricResultsCollectionsTypeDef
):
    """
    Type definition for `GetMetricDataPaginateResponseMetricResults` `Collections`

    Contains the data for a historical metric.

    - **Metric** *(dict) --*

      Information about the metric.

      - **Name** *(string) --*

        The name of the metric.

      - **Threshold** *(dict) --*

        The threshold for the metric, used with service level metrics.

        - **Comparison** *(string) --*

          The type of comparison. Only "less than" (LT) comparisons are supported.

        - **ThresholdValue** *(float) --*

          The threshold value to compare.

      - **Statistic** *(string) --*

        The statistic for the metric.

      - **Unit** *(string) --*

        The unit for the metric.

    - **Value** *(float) --*

      The value of the metric.
    """


_GetMetricDataPaginateResponseMetricResultsDimensionsQueueTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseMetricResultsDimensionsQueueTypeDef",
    {"Id": str, "Arn": str},
    total=False,
)


class GetMetricDataPaginateResponseMetricResultsDimensionsQueueTypeDef(
    _GetMetricDataPaginateResponseMetricResultsDimensionsQueueTypeDef
):
    """
    Type definition for `GetMetricDataPaginateResponseMetricResultsDimensions` `Queue`

    Information about the queue for which metrics are returned.

    - **Id** *(string) --*

      The identifier of the queue.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the queue.
    """


_GetMetricDataPaginateResponseMetricResultsDimensionsTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseMetricResultsDimensionsTypeDef",
    {
        "Queue": GetMetricDataPaginateResponseMetricResultsDimensionsQueueTypeDef,
        "Channel": str,
    },
    total=False,
)


class GetMetricDataPaginateResponseMetricResultsDimensionsTypeDef(
    _GetMetricDataPaginateResponseMetricResultsDimensionsTypeDef
):
    """
    Type definition for `GetMetricDataPaginateResponseMetricResults` `Dimensions`

    The dimension for the metrics.

    - **Queue** *(dict) --*

      Information about the queue for which metrics are returned.

      - **Id** *(string) --*

        The identifier of the queue.

      - **Arn** *(string) --*

        The Amazon Resource Name (ARN) of the queue.

    - **Channel** *(string) --*

      The channel used for grouping and filters.
    """


_GetMetricDataPaginateResponseMetricResultsTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseMetricResultsTypeDef",
    {
        "Dimensions": GetMetricDataPaginateResponseMetricResultsDimensionsTypeDef,
        "Collections": List[
            GetMetricDataPaginateResponseMetricResultsCollectionsTypeDef
        ],
    },
    total=False,
)


class GetMetricDataPaginateResponseMetricResultsTypeDef(
    _GetMetricDataPaginateResponseMetricResultsTypeDef
):
    """
    Type definition for `GetMetricDataPaginateResponse` `MetricResults`

    Contains information about the historical metrics retrieved.

    - **Dimensions** *(dict) --*

      The dimension for the metrics.

      - **Queue** *(dict) --*

        Information about the queue for which metrics are returned.

        - **Id** *(string) --*

          The identifier of the queue.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the queue.

      - **Channel** *(string) --*

        The channel used for grouping and filters.

    - **Collections** *(list) --*

      The set of metrics.

      - *(dict) --*

        Contains the data for a historical metric.

        - **Metric** *(dict) --*

          Information about the metric.

          - **Name** *(string) --*

            The name of the metric.

          - **Threshold** *(dict) --*

            The threshold for the metric, used with service level metrics.

            - **Comparison** *(string) --*

              The type of comparison. Only "less than" (LT) comparisons are supported.

            - **ThresholdValue** *(float) --*

              The threshold value to compare.

          - **Statistic** *(string) --*

            The statistic for the metric.

          - **Unit** *(string) --*

            The unit for the metric.

        - **Value** *(float) --*

          The value of the metric.
    """


_GetMetricDataPaginateResponseTypeDef = TypedDict(
    "_GetMetricDataPaginateResponseTypeDef",
    {"MetricResults": List[GetMetricDataPaginateResponseMetricResultsTypeDef]},
    total=False,
)


class GetMetricDataPaginateResponseTypeDef(_GetMetricDataPaginateResponseTypeDef):
    """
    Type definition for `GetMetricDataPaginate` `Response`

    - **MetricResults** *(list) --*

      Information about the historical metrics.

      If no grouping is specified, a summary of metric data is returned.

      - *(dict) --*

        Contains information about the historical metrics retrieved.

        - **Dimensions** *(dict) --*

          The dimension for the metrics.

          - **Queue** *(dict) --*

            Information about the queue for which metrics are returned.

            - **Id** *(string) --*

              The identifier of the queue.

            - **Arn** *(string) --*

              The Amazon Resource Name (ARN) of the queue.

          - **Channel** *(string) --*

            The channel used for grouping and filters.

        - **Collections** *(list) --*

          The set of metrics.

          - *(dict) --*

            Contains the data for a historical metric.

            - **Metric** *(dict) --*

              Information about the metric.

              - **Name** *(string) --*

                The name of the metric.

              - **Threshold** *(dict) --*

                The threshold for the metric, used with service level metrics.

                - **Comparison** *(string) --*

                  The type of comparison. Only "less than" (LT) comparisons are supported.

                - **ThresholdValue** *(float) --*

                  The threshold value to compare.

              - **Statistic** *(string) --*

                The statistic for the metric.

              - **Unit** *(string) --*

                The unit for the metric.

            - **Value** *(float) --*

              The value of the metric.
    """


_ListContactFlowsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListContactFlowsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListContactFlowsPaginatePaginationConfigTypeDef(
    _ListContactFlowsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListContactFlowsPaginate` `PaginationConfig`

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


_ListContactFlowsPaginateResponseContactFlowSummaryListTypeDef = TypedDict(
    "_ListContactFlowsPaginateResponseContactFlowSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str, "ContactFlowType": str},
    total=False,
)


class ListContactFlowsPaginateResponseContactFlowSummaryListTypeDef(
    _ListContactFlowsPaginateResponseContactFlowSummaryListTypeDef
):
    """
    Type definition for `ListContactFlowsPaginateResponse` `ContactFlowSummaryList`

    Contains summary information about a contact flow.

    - **Id** *(string) --*

      The identifier of the contact flow.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the contact flow.

    - **Name** *(string) --*

      The name of the contact flow.

    - **ContactFlowType** *(string) --*

      The type of contact flow.
    """


_ListContactFlowsPaginateResponseTypeDef = TypedDict(
    "_ListContactFlowsPaginateResponseTypeDef",
    {
        "ContactFlowSummaryList": List[
            ListContactFlowsPaginateResponseContactFlowSummaryListTypeDef
        ]
    },
    total=False,
)


class ListContactFlowsPaginateResponseTypeDef(_ListContactFlowsPaginateResponseTypeDef):
    """
    Type definition for `ListContactFlowsPaginate` `Response`

    - **ContactFlowSummaryList** *(list) --*

      Information about the contact flows.

      - *(dict) --*

        Contains summary information about a contact flow.

        - **Id** *(string) --*

          The identifier of the contact flow.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the contact flow.

        - **Name** *(string) --*

          The name of the contact flow.

        - **ContactFlowType** *(string) --*

          The type of contact flow.
    """


_ListHoursOfOperationsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListHoursOfOperationsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListHoursOfOperationsPaginatePaginationConfigTypeDef(
    _ListHoursOfOperationsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListHoursOfOperationsPaginate` `PaginationConfig`

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


_ListHoursOfOperationsPaginateResponseHoursOfOperationSummaryListTypeDef = TypedDict(
    "_ListHoursOfOperationsPaginateResponseHoursOfOperationSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ListHoursOfOperationsPaginateResponseHoursOfOperationSummaryListTypeDef(
    _ListHoursOfOperationsPaginateResponseHoursOfOperationSummaryListTypeDef
):
    """
    Type definition for `ListHoursOfOperationsPaginateResponse` `HoursOfOperationSummaryList`

    Contains summary information about hours of operation for a contact center.

    - **Id** *(string) --*

      The identifier of the hours of operation.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the hours of operation.

    - **Name** *(string) --*

      The name of the hours of operation.
    """


_ListHoursOfOperationsPaginateResponseTypeDef = TypedDict(
    "_ListHoursOfOperationsPaginateResponseTypeDef",
    {
        "HoursOfOperationSummaryList": List[
            ListHoursOfOperationsPaginateResponseHoursOfOperationSummaryListTypeDef
        ]
    },
    total=False,
)


class ListHoursOfOperationsPaginateResponseTypeDef(
    _ListHoursOfOperationsPaginateResponseTypeDef
):
    """
    Type definition for `ListHoursOfOperationsPaginate` `Response`

    - **HoursOfOperationSummaryList** *(list) --*

      Information about the hours of operation.

      - *(dict) --*

        Contains summary information about hours of operation for a contact center.

        - **Id** *(string) --*

          The identifier of the hours of operation.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the hours of operation.

        - **Name** *(string) --*

          The name of the hours of operation.
    """


_ListPhoneNumbersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPhoneNumbersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPhoneNumbersPaginatePaginationConfigTypeDef(
    _ListPhoneNumbersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPhoneNumbersPaginate` `PaginationConfig`

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


_ListPhoneNumbersPaginateResponsePhoneNumberSummaryListTypeDef = TypedDict(
    "_ListPhoneNumbersPaginateResponsePhoneNumberSummaryListTypeDef",
    {
        "Id": str,
        "Arn": str,
        "PhoneNumber": str,
        "PhoneNumberType": str,
        "PhoneNumberCountryCode": str,
    },
    total=False,
)


class ListPhoneNumbersPaginateResponsePhoneNumberSummaryListTypeDef(
    _ListPhoneNumbersPaginateResponsePhoneNumberSummaryListTypeDef
):
    """
    Type definition for `ListPhoneNumbersPaginateResponse` `PhoneNumberSummaryList`

    Contains summary information about a phone number for a contact center.

    - **Id** *(string) --*

      The identifier of the phone number.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the phone number.

    - **PhoneNumber** *(string) --*

      The phone number.

    - **PhoneNumberType** *(string) --*

      The type of phone number.

    - **PhoneNumberCountryCode** *(string) --*

      The ISO country code.
    """


_ListPhoneNumbersPaginateResponseTypeDef = TypedDict(
    "_ListPhoneNumbersPaginateResponseTypeDef",
    {
        "PhoneNumberSummaryList": List[
            ListPhoneNumbersPaginateResponsePhoneNumberSummaryListTypeDef
        ]
    },
    total=False,
)


class ListPhoneNumbersPaginateResponseTypeDef(_ListPhoneNumbersPaginateResponseTypeDef):
    """
    Type definition for `ListPhoneNumbersPaginate` `Response`

    - **PhoneNumberSummaryList** *(list) --*

      Information about the phone numbers.

      - *(dict) --*

        Contains summary information about a phone number for a contact center.

        - **Id** *(string) --*

          The identifier of the phone number.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the phone number.

        - **PhoneNumber** *(string) --*

          The phone number.

        - **PhoneNumberType** *(string) --*

          The type of phone number.

        - **PhoneNumberCountryCode** *(string) --*

          The ISO country code.
    """


_ListQueuesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListQueuesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListQueuesPaginatePaginationConfigTypeDef(
    _ListQueuesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListQueuesPaginate` `PaginationConfig`

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


_ListQueuesPaginateResponseQueueSummaryListTypeDef = TypedDict(
    "_ListQueuesPaginateResponseQueueSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str, "QueueType": str},
    total=False,
)


class ListQueuesPaginateResponseQueueSummaryListTypeDef(
    _ListQueuesPaginateResponseQueueSummaryListTypeDef
):
    """
    Type definition for `ListQueuesPaginateResponse` `QueueSummaryList`

    Contains summary information about a queue.

    - **Id** *(string) --*

      The identifier of the queue.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the queue.

    - **Name** *(string) --*

      The name of the queue.

    - **QueueType** *(string) --*

      The type of queue.
    """


_ListQueuesPaginateResponseTypeDef = TypedDict(
    "_ListQueuesPaginateResponseTypeDef",
    {"QueueSummaryList": List[ListQueuesPaginateResponseQueueSummaryListTypeDef]},
    total=False,
)


class ListQueuesPaginateResponseTypeDef(_ListQueuesPaginateResponseTypeDef):
    """
    Type definition for `ListQueuesPaginate` `Response`

    - **QueueSummaryList** *(list) --*

      Information about the queues.

      - *(dict) --*

        Contains summary information about a queue.

        - **Id** *(string) --*

          The identifier of the queue.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the queue.

        - **Name** *(string) --*

          The name of the queue.

        - **QueueType** *(string) --*

          The type of queue.
    """


_ListRoutingProfilesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListRoutingProfilesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListRoutingProfilesPaginatePaginationConfigTypeDef(
    _ListRoutingProfilesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListRoutingProfilesPaginate` `PaginationConfig`

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


_ListRoutingProfilesPaginateResponseRoutingProfileSummaryListTypeDef = TypedDict(
    "_ListRoutingProfilesPaginateResponseRoutingProfileSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ListRoutingProfilesPaginateResponseRoutingProfileSummaryListTypeDef(
    _ListRoutingProfilesPaginateResponseRoutingProfileSummaryListTypeDef
):
    """
    Type definition for `ListRoutingProfilesPaginateResponse` `RoutingProfileSummaryList`

    Contains summary information about a routing profile.

    - **Id** *(string) --*

      The identifier of the routing profile.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the routing profile.

    - **Name** *(string) --*

      The name of the routing profile.
    """


_ListRoutingProfilesPaginateResponseTypeDef = TypedDict(
    "_ListRoutingProfilesPaginateResponseTypeDef",
    {
        "RoutingProfileSummaryList": List[
            ListRoutingProfilesPaginateResponseRoutingProfileSummaryListTypeDef
        ]
    },
    total=False,
)


class ListRoutingProfilesPaginateResponseTypeDef(
    _ListRoutingProfilesPaginateResponseTypeDef
):
    """
    Type definition for `ListRoutingProfilesPaginate` `Response`

    - **RoutingProfileSummaryList** *(list) --*

      Information about the routing profiles.

      - *(dict) --*

        Contains summary information about a routing profile.

        - **Id** *(string) --*

          The identifier of the routing profile.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the routing profile.

        - **Name** *(string) --*

          The name of the routing profile.
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


_ListSecurityProfilesPaginateResponseSecurityProfileSummaryListTypeDef = TypedDict(
    "_ListSecurityProfilesPaginateResponseSecurityProfileSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ListSecurityProfilesPaginateResponseSecurityProfileSummaryListTypeDef(
    _ListSecurityProfilesPaginateResponseSecurityProfileSummaryListTypeDef
):
    """
    Type definition for `ListSecurityProfilesPaginateResponse` `SecurityProfileSummaryList`

    Contains information about a security profile.

    - **Id** *(string) --*

      The identifier of the security profile.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the security profile.

    - **Name** *(string) --*

      The name of the security profile.
    """


_ListSecurityProfilesPaginateResponseTypeDef = TypedDict(
    "_ListSecurityProfilesPaginateResponseTypeDef",
    {
        "SecurityProfileSummaryList": List[
            ListSecurityProfilesPaginateResponseSecurityProfileSummaryListTypeDef
        ]
    },
    total=False,
)


class ListSecurityProfilesPaginateResponseTypeDef(
    _ListSecurityProfilesPaginateResponseTypeDef
):
    """
    Type definition for `ListSecurityProfilesPaginate` `Response`

    - **SecurityProfileSummaryList** *(list) --*

      Information about the security profiles.

      - *(dict) --*

        Contains information about a security profile.

        - **Id** *(string) --*

          The identifier of the security profile.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the security profile.

        - **Name** *(string) --*

          The name of the security profile.
    """


_ListUserHierarchyGroupsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUserHierarchyGroupsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUserHierarchyGroupsPaginatePaginationConfigTypeDef(
    _ListUserHierarchyGroupsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListUserHierarchyGroupsPaginate` `PaginationConfig`

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


_ListUserHierarchyGroupsPaginateResponseUserHierarchyGroupSummaryListTypeDef = TypedDict(
    "_ListUserHierarchyGroupsPaginateResponseUserHierarchyGroupSummaryListTypeDef",
    {"Id": str, "Arn": str, "Name": str},
    total=False,
)


class ListUserHierarchyGroupsPaginateResponseUserHierarchyGroupSummaryListTypeDef(
    _ListUserHierarchyGroupsPaginateResponseUserHierarchyGroupSummaryListTypeDef
):
    """
    Type definition for `ListUserHierarchyGroupsPaginateResponse` `UserHierarchyGroupSummaryList`

    Contains summary information about a hierarchy group.

    - **Id** *(string) --*

      The identifier of the hierarchy group.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the hierarchy group.

    - **Name** *(string) --*

      The name of the hierarchy group.
    """


_ListUserHierarchyGroupsPaginateResponseTypeDef = TypedDict(
    "_ListUserHierarchyGroupsPaginateResponseTypeDef",
    {
        "UserHierarchyGroupSummaryList": List[
            ListUserHierarchyGroupsPaginateResponseUserHierarchyGroupSummaryListTypeDef
        ]
    },
    total=False,
)


class ListUserHierarchyGroupsPaginateResponseTypeDef(
    _ListUserHierarchyGroupsPaginateResponseTypeDef
):
    """
    Type definition for `ListUserHierarchyGroupsPaginate` `Response`

    - **UserHierarchyGroupSummaryList** *(list) --*

      Information about the hierarchy groups.

      - *(dict) --*

        Contains summary information about a hierarchy group.

        - **Id** *(string) --*

          The identifier of the hierarchy group.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the hierarchy group.

        - **Name** *(string) --*

          The name of the hierarchy group.
    """


_ListUsersPaginatePaginationConfigTypeDef = TypedDict(
    "_ListUsersPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListUsersPaginatePaginationConfigTypeDef(
    _ListUsersPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListUsersPaginate` `PaginationConfig`

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


_ListUsersPaginateResponseUserSummaryListTypeDef = TypedDict(
    "_ListUsersPaginateResponseUserSummaryListTypeDef",
    {"Id": str, "Arn": str, "Username": str},
    total=False,
)


class ListUsersPaginateResponseUserSummaryListTypeDef(
    _ListUsersPaginateResponseUserSummaryListTypeDef
):
    """
    Type definition for `ListUsersPaginateResponse` `UserSummaryList`

    Contains summary information about a user.

    - **Id** *(string) --*

      The identifier of the user account.

    - **Arn** *(string) --*

      The Amazon Resource Name (ARN) of the user account.

    - **Username** *(string) --*

      The Amazon Connect user name of the user account.
    """


_ListUsersPaginateResponseTypeDef = TypedDict(
    "_ListUsersPaginateResponseTypeDef",
    {"UserSummaryList": List[ListUsersPaginateResponseUserSummaryListTypeDef]},
    total=False,
)


class ListUsersPaginateResponseTypeDef(_ListUsersPaginateResponseTypeDef):
    """
    Type definition for `ListUsersPaginate` `Response`

    - **UserSummaryList** *(list) --*

      Information about the users.

      - *(dict) --*

        Contains summary information about a user.

        - **Id** *(string) --*

          The identifier of the user account.

        - **Arn** *(string) --*

          The Amazon Resource Name (ARN) of the user account.

        - **Username** *(string) --*

          The Amazon Connect user name of the user account.
    """

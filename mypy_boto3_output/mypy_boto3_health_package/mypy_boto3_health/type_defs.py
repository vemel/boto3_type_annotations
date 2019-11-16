"Main interface for health type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientDescribeAffectedEntitiesfilterlastUpdatedTimesTypeDef",
    "ClientDescribeAffectedEntitiesfilterTypeDef",
    "ClientDescribeEventAggregatesResponseeventAggregatesTypeDef",
    "ClientDescribeEventAggregatesResponseTypeDef",
    "ClientDescribeEventAggregatesfilterendTimesTypeDef",
    "ClientDescribeEventAggregatesfilterlastUpdatedTimesTypeDef",
    "ClientDescribeEventAggregatesfilterstartTimesTypeDef",
    "ClientDescribeEventAggregatesfilterTypeDef",
    "ClientDescribeEventTypesResponseeventTypesTypeDef",
    "ClientDescribeEventTypesResponseTypeDef",
    "ClientDescribeEventTypesfilterTypeDef",
    "ClientDescribeEventsfilterendTimesTypeDef",
    "ClientDescribeEventsfilterlastUpdatedTimesTypeDef",
    "ClientDescribeEventsfilterstartTimesTypeDef",
    "ClientDescribeEventsfilterTypeDef",
    "DescribeAffectedEntitiesPaginatePaginationConfigTypeDef",
    "DescribeAffectedEntitiesPaginatefilterlastUpdatedTimesTypeDef",
    "DescribeAffectedEntitiesPaginatefilterTypeDef",
    "DescribeEventAggregatesPaginatePaginationConfigTypeDef",
    "DescribeEventAggregatesPaginateResponseeventAggregatesTypeDef",
    "DescribeEventAggregatesPaginateResponseTypeDef",
    "DescribeEventAggregatesPaginatefilterendTimesTypeDef",
    "DescribeEventAggregatesPaginatefilterlastUpdatedTimesTypeDef",
    "DescribeEventAggregatesPaginatefilterstartTimesTypeDef",
    "DescribeEventAggregatesPaginatefilterTypeDef",
    "DescribeEventTypesPaginatePaginationConfigTypeDef",
    "DescribeEventTypesPaginateResponseeventTypesTypeDef",
    "DescribeEventTypesPaginateResponseTypeDef",
    "DescribeEventTypesPaginatefilterTypeDef",
    "DescribeEventsPaginatePaginationConfigTypeDef",
    "DescribeEventsPaginatefilterendTimesTypeDef",
    "DescribeEventsPaginatefilterlastUpdatedTimesTypeDef",
    "DescribeEventsPaginatefilterstartTimesTypeDef",
    "DescribeEventsPaginatefilterTypeDef",
)


_ClientDescribeAffectedEntitiesfilterlastUpdatedTimesTypeDef = TypedDict(
    "_ClientDescribeAffectedEntitiesfilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class ClientDescribeAffectedEntitiesfilterlastUpdatedTimesTypeDef(
    _ClientDescribeAffectedEntitiesfilterlastUpdatedTimesTypeDef
):
    """
    Type definition for `ClientDescribeAffectedEntitiesfilter` `lastUpdatedTimes`

    A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
    ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
    ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
    is set and ``to`` is not set: match items where the timestamp value is equal to or after
    ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
    equal to or before ``to`` .

    - **from** *(datetime) --*

      The starting date and time of a time range.

    - **to** *(datetime) --*

      The ending date and time of a time range.
    """


_RequiredClientDescribeAffectedEntitiesfilterTypeDef = TypedDict(
    "_RequiredClientDescribeAffectedEntitiesfilterTypeDef", {"eventArns": List[str]}
)
_OptionalClientDescribeAffectedEntitiesfilterTypeDef = TypedDict(
    "_OptionalClientDescribeAffectedEntitiesfilterTypeDef",
    {
        "entityArns": List[str],
        "entityValues": List[str],
        "lastUpdatedTimes": List[
            ClientDescribeAffectedEntitiesfilterlastUpdatedTimesTypeDef
        ],
        "tags": List[Dict[str, str]],
        "statusCodes": List[str],
    },
    total=False,
)


class ClientDescribeAffectedEntitiesfilterTypeDef(
    _RequiredClientDescribeAffectedEntitiesfilterTypeDef,
    _OptionalClientDescribeAffectedEntitiesfilterTypeDef,
):
    """
    Type definition for `ClientDescribeAffectedEntities` `filter`

    Values to narrow the results returned. At least one event ARN is required.

    - **eventArns** *(list) --* **[REQUIRED]**

      A list of event ARNs (unique identifiers). For example:
      ``"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
      "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"``

      - *(string) --*

    - **entityArns** *(list) --*

      A list of entity ARNs (unique identifiers).

      - *(string) --*

    - **entityValues** *(list) --*

      A list of IDs for affected entities.

      - *(string) --*

    - **lastUpdatedTimes** *(list) --*

      A list of the most recent dates and times that the entity was updated.

      - *(dict) --*

        A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
        ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
        ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
        is set and ``to`` is not set: match items where the timestamp value is equal to or after
        ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
        equal to or before ``to`` .

        - **from** *(datetime) --*

          The starting date and time of a time range.

        - **to** *(datetime) --*

          The ending date and time of a time range.

    - **tags** *(list) --*

      A map of entity tags attached to the affected entity.

      - *(dict) --*

        - *(string) --*

          - *(string) --*

    - **statusCodes** *(list) --*

      A list of entity status codes (``IMPAIRED`` , ``UNIMPAIRED`` , or ``UNKNOWN`` ).

      - *(string) --*
    """


_ClientDescribeEventAggregatesResponseeventAggregatesTypeDef = TypedDict(
    "_ClientDescribeEventAggregatesResponseeventAggregatesTypeDef",
    {"aggregateValue": str, "count": int},
    total=False,
)


class ClientDescribeEventAggregatesResponseeventAggregatesTypeDef(
    _ClientDescribeEventAggregatesResponseeventAggregatesTypeDef
):
    """
    Type definition for `ClientDescribeEventAggregatesResponse` `eventAggregates`

    The number of events of each issue type. Returned by the  DescribeEventAggregates operation.

    - **aggregateValue** *(string) --*

      The issue type for the associated count.

    - **count** *(integer) --*

      The number of events of the associated issue type.
    """


_ClientDescribeEventAggregatesResponseTypeDef = TypedDict(
    "_ClientDescribeEventAggregatesResponseTypeDef",
    {
        "eventAggregates": List[
            ClientDescribeEventAggregatesResponseeventAggregatesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeEventAggregatesResponseTypeDef(
    _ClientDescribeEventAggregatesResponseTypeDef
):
    """
    Type definition for `ClientDescribeEventAggregates` `Response`

    - **eventAggregates** *(list) --*

      The number of events in each category that meet the optional filter criteria.

      - *(dict) --*

        The number of events of each issue type. Returned by the  DescribeEventAggregates operation.

        - **aggregateValue** *(string) --*

          The issue type for the associated count.

        - **count** *(integer) --*

          The number of events of the associated issue type.

    - **nextToken** *(string) --*

      If the results of a search are large, only a portion of the results are returned, and a
      ``nextToken`` pagination token is returned in the response. To retrieve the next batch of
      results, reissue the search request and include the returned token. When all results have
      been returned, the response does not contain a pagination token value.
    """


_ClientDescribeEventAggregatesfilterendTimesTypeDef = TypedDict(
    "_ClientDescribeEventAggregatesfilterendTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class ClientDescribeEventAggregatesfilterendTimesTypeDef(
    _ClientDescribeEventAggregatesfilterendTimesTypeDef
):
    """
    Type definition for `ClientDescribeEventAggregatesfilter` `endTimes`

    A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
    ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
    ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
    is set and ``to`` is not set: match items where the timestamp value is equal to or after
    ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
    equal to or before ``to`` .

    - **from** *(datetime) --*

      The starting date and time of a time range.

    - **to** *(datetime) --*

      The ending date and time of a time range.
    """


_ClientDescribeEventAggregatesfilterlastUpdatedTimesTypeDef = TypedDict(
    "_ClientDescribeEventAggregatesfilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class ClientDescribeEventAggregatesfilterlastUpdatedTimesTypeDef(
    _ClientDescribeEventAggregatesfilterlastUpdatedTimesTypeDef
):
    """
    Type definition for `ClientDescribeEventAggregatesfilter` `lastUpdatedTimes`

    A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
    ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
    ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
    is set and ``to`` is not set: match items where the timestamp value is equal to or after
    ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
    equal to or before ``to`` .

    - **from** *(datetime) --*

      The starting date and time of a time range.

    - **to** *(datetime) --*

      The ending date and time of a time range.
    """


_ClientDescribeEventAggregatesfilterstartTimesTypeDef = TypedDict(
    "_ClientDescribeEventAggregatesfilterstartTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class ClientDescribeEventAggregatesfilterstartTimesTypeDef(
    _ClientDescribeEventAggregatesfilterstartTimesTypeDef
):
    """
    Type definition for `ClientDescribeEventAggregatesfilter` `startTimes`

    A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
    ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
    ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
    is set and ``to`` is not set: match items where the timestamp value is equal to or after
    ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
    equal to or before ``to`` .

    - **from** *(datetime) --*

      The starting date and time of a time range.

    - **to** *(datetime) --*

      The ending date and time of a time range.
    """


_ClientDescribeEventAggregatesfilterTypeDef = TypedDict(
    "_ClientDescribeEventAggregatesfilterTypeDef",
    {
        "eventArns": List[str],
        "eventTypeCodes": List[str],
        "services": List[str],
        "regions": List[str],
        "availabilityZones": List[str],
        "startTimes": List[ClientDescribeEventAggregatesfilterstartTimesTypeDef],
        "endTimes": List[ClientDescribeEventAggregatesfilterendTimesTypeDef],
        "lastUpdatedTimes": List[
            ClientDescribeEventAggregatesfilterlastUpdatedTimesTypeDef
        ],
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[str],
        "tags": List[Dict[str, str]],
        "eventStatusCodes": List[str],
    },
    total=False,
)


class ClientDescribeEventAggregatesfilterTypeDef(
    _ClientDescribeEventAggregatesfilterTypeDef
):
    """
    Type definition for `ClientDescribeEventAggregates` `filter`

    Values to narrow the results returned.

    - **eventArns** *(list) --*

      A list of event ARNs (unique identifiers). For example:
      ``"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
      "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"``

      - *(string) --*

    - **eventTypeCodes** *(list) --*

      A list of unique identifiers for event types. For example,
      ``"AWS_EC2_SYSTEM_MAINTENANCE_EVENT","AWS_RDS_MAINTENANCE_SCHEDULED"``

      - *(string) --*

    - **services** *(list) --*

      The AWS services associated with the event. For example, ``EC2`` , ``RDS`` .

      - *(string) --*

    - **regions** *(list) --*

      A list of AWS regions.

      - *(string) --*

    - **availabilityZones** *(list) --*

      A list of AWS availability zones.

      - *(string) --*

    - **startTimes** *(list) --*

      A list of dates and times that the event began.

      - *(dict) --*

        A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
        ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
        ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
        is set and ``to`` is not set: match items where the timestamp value is equal to or after
        ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
        equal to or before ``to`` .

        - **from** *(datetime) --*

          The starting date and time of a time range.

        - **to** *(datetime) --*

          The ending date and time of a time range.

    - **endTimes** *(list) --*

      A list of dates and times that the event ended.

      - *(dict) --*

        A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
        ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
        ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
        is set and ``to`` is not set: match items where the timestamp value is equal to or after
        ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
        equal to or before ``to`` .

        - **from** *(datetime) --*

          The starting date and time of a time range.

        - **to** *(datetime) --*

          The ending date and time of a time range.

    - **lastUpdatedTimes** *(list) --*

      A list of dates and times that the event was last updated.

      - *(dict) --*

        A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
        ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
        ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
        is set and ``to`` is not set: match items where the timestamp value is equal to or after
        ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
        equal to or before ``to`` .

        - **from** *(datetime) --*

          The starting date and time of a time range.

        - **to** *(datetime) --*

          The ending date and time of a time range.

    - **entityArns** *(list) --*

      A list of entity ARNs (unique identifiers).

      - *(string) --*

    - **entityValues** *(list) --*

      A list of entity identifiers, such as EC2 instance IDs (``i-34ab692e`` ) or EBS volumes
      (``vol-426ab23e`` ).

      - *(string) --*

    - **eventTypeCategories** *(list) --*

      A list of event type category codes (``issue`` , ``scheduledChange`` , or
      ``accountNotification`` ).

      - *(string) --*

    - **tags** *(list) --*

      A map of entity tags attached to the affected entity.

      - *(dict) --*

        - *(string) --*

          - *(string) --*

    - **eventStatusCodes** *(list) --*

      A list of event status codes.

      - *(string) --*
    """


_ClientDescribeEventTypesResponseeventTypesTypeDef = TypedDict(
    "_ClientDescribeEventTypesResponseeventTypesTypeDef",
    {"service": str, "code": str, "category": str},
    total=False,
)


class ClientDescribeEventTypesResponseeventTypesTypeDef(
    _ClientDescribeEventTypesResponseeventTypesTypeDef
):
    """
    Type definition for `ClientDescribeEventTypesResponse` `eventTypes`

    Metadata about a type of event that is reported by AWS Health. Data consists of the
    category (for example, ``issue`` ), the service (for example, ``EC2`` ), and the event type
    code (for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` ).

    - **service** *(string) --*

      The AWS service that is affected by the event. For example, ``EC2`` , ``RDS`` .

    - **code** *(string) --*

      The unique identifier for the event type. The format is ``AWS_*SERVICE* _*DESCRIPTION* ``
      ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` .

    - **category** *(string) --*

      A list of event type category codes (``issue`` , ``scheduledChange`` , or
      ``accountNotification`` ).
    """


_ClientDescribeEventTypesResponseTypeDef = TypedDict(
    "_ClientDescribeEventTypesResponseTypeDef",
    {
        "eventTypes": List[ClientDescribeEventTypesResponseeventTypesTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientDescribeEventTypesResponseTypeDef(_ClientDescribeEventTypesResponseTypeDef):
    """
    Type definition for `ClientDescribeEventTypes` `Response`

    - **eventTypes** *(list) --*

      A list of event types that match the filter criteria. Event types have a category (``issue``
      , ``accountNotification`` , or ``scheduledChange`` ), a service (for example, ``EC2`` ,
      ``RDS`` , ``DATAPIPELINE`` , ``BILLING`` ), and a code (in the format ``AWS_*SERVICE*
      _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` ).

      - *(dict) --*

        Metadata about a type of event that is reported by AWS Health. Data consists of the
        category (for example, ``issue`` ), the service (for example, ``EC2`` ), and the event type
        code (for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` ).

        - **service** *(string) --*

          The AWS service that is affected by the event. For example, ``EC2`` , ``RDS`` .

        - **code** *(string) --*

          The unique identifier for the event type. The format is ``AWS_*SERVICE* _*DESCRIPTION* ``
          ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` .

        - **category** *(string) --*

          A list of event type category codes (``issue`` , ``scheduledChange`` , or
          ``accountNotification`` ).

    - **nextToken** *(string) --*

      If the results of a search are large, only a portion of the results are returned, and a
      ``nextToken`` pagination token is returned in the response. To retrieve the next batch of
      results, reissue the search request and include the returned token. When all results have
      been returned, the response does not contain a pagination token value.
    """


_ClientDescribeEventTypesfilterTypeDef = TypedDict(
    "_ClientDescribeEventTypesfilterTypeDef",
    {
        "eventTypeCodes": List[str],
        "services": List[str],
        "eventTypeCategories": List[str],
    },
    total=False,
)


class ClientDescribeEventTypesfilterTypeDef(_ClientDescribeEventTypesfilterTypeDef):
    """
    Type definition for `ClientDescribeEventTypes` `filter`

    Values to narrow the results returned.

    - **eventTypeCodes** *(list) --*

      A list of event type codes.

      - *(string) --*

    - **services** *(list) --*

      The AWS services associated with the event. For example, ``EC2`` , ``RDS`` .

      - *(string) --*

    - **eventTypeCategories** *(list) --*

      A list of event type category codes (``issue`` , ``scheduledChange`` , or
      ``accountNotification`` ).

      - *(string) --*
    """


_ClientDescribeEventsfilterendTimesTypeDef = TypedDict(
    "_ClientDescribeEventsfilterendTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class ClientDescribeEventsfilterendTimesTypeDef(
    _ClientDescribeEventsfilterendTimesTypeDef
):
    """
    Type definition for `ClientDescribeEventsfilter` `endTimes`

    A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
    ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
    ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
    is set and ``to`` is not set: match items where the timestamp value is equal to or after
    ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
    equal to or before ``to`` .

    - **from** *(datetime) --*

      The starting date and time of a time range.

    - **to** *(datetime) --*

      The ending date and time of a time range.
    """


_ClientDescribeEventsfilterlastUpdatedTimesTypeDef = TypedDict(
    "_ClientDescribeEventsfilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class ClientDescribeEventsfilterlastUpdatedTimesTypeDef(
    _ClientDescribeEventsfilterlastUpdatedTimesTypeDef
):
    """
    Type definition for `ClientDescribeEventsfilter` `lastUpdatedTimes`

    A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
    ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
    ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
    is set and ``to`` is not set: match items where the timestamp value is equal to or after
    ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
    equal to or before ``to`` .

    - **from** *(datetime) --*

      The starting date and time of a time range.

    - **to** *(datetime) --*

      The ending date and time of a time range.
    """


_ClientDescribeEventsfilterstartTimesTypeDef = TypedDict(
    "_ClientDescribeEventsfilterstartTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class ClientDescribeEventsfilterstartTimesTypeDef(
    _ClientDescribeEventsfilterstartTimesTypeDef
):
    """
    Type definition for `ClientDescribeEventsfilter` `startTimes`

    A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
    ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
    ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
    is set and ``to`` is not set: match items where the timestamp value is equal to or after
    ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
    equal to or before ``to`` .

    - **from** *(datetime) --*

      The starting date and time of a time range.

    - **to** *(datetime) --*

      The ending date and time of a time range.
    """


_ClientDescribeEventsfilterTypeDef = TypedDict(
    "_ClientDescribeEventsfilterTypeDef",
    {
        "eventArns": List[str],
        "eventTypeCodes": List[str],
        "services": List[str],
        "regions": List[str],
        "availabilityZones": List[str],
        "startTimes": List[ClientDescribeEventsfilterstartTimesTypeDef],
        "endTimes": List[ClientDescribeEventsfilterendTimesTypeDef],
        "lastUpdatedTimes": List[ClientDescribeEventsfilterlastUpdatedTimesTypeDef],
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[str],
        "tags": List[Dict[str, str]],
        "eventStatusCodes": List[str],
    },
    total=False,
)


class ClientDescribeEventsfilterTypeDef(_ClientDescribeEventsfilterTypeDef):
    """
    Type definition for `ClientDescribeEvents` `filter`

    Values to narrow the results returned.

    - **eventArns** *(list) --*

      A list of event ARNs (unique identifiers). For example:
      ``"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
      "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"``

      - *(string) --*

    - **eventTypeCodes** *(list) --*

      A list of unique identifiers for event types. For example,
      ``"AWS_EC2_SYSTEM_MAINTENANCE_EVENT","AWS_RDS_MAINTENANCE_SCHEDULED"``

      - *(string) --*

    - **services** *(list) --*

      The AWS services associated with the event. For example, ``EC2`` , ``RDS`` .

      - *(string) --*

    - **regions** *(list) --*

      A list of AWS regions.

      - *(string) --*

    - **availabilityZones** *(list) --*

      A list of AWS availability zones.

      - *(string) --*

    - **startTimes** *(list) --*

      A list of dates and times that the event began.

      - *(dict) --*

        A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
        ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
        ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
        is set and ``to`` is not set: match items where the timestamp value is equal to or after
        ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
        equal to or before ``to`` .

        - **from** *(datetime) --*

          The starting date and time of a time range.

        - **to** *(datetime) --*

          The ending date and time of a time range.

    - **endTimes** *(list) --*

      A list of dates and times that the event ended.

      - *(dict) --*

        A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
        ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
        ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
        is set and ``to`` is not set: match items where the timestamp value is equal to or after
        ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
        equal to or before ``to`` .

        - **from** *(datetime) --*

          The starting date and time of a time range.

        - **to** *(datetime) --*

          The ending date and time of a time range.

    - **lastUpdatedTimes** *(list) --*

      A list of dates and times that the event was last updated.

      - *(dict) --*

        A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
        ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
        ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
        is set and ``to`` is not set: match items where the timestamp value is equal to or after
        ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
        equal to or before ``to`` .

        - **from** *(datetime) --*

          The starting date and time of a time range.

        - **to** *(datetime) --*

          The ending date and time of a time range.

    - **entityArns** *(list) --*

      A list of entity ARNs (unique identifiers).

      - *(string) --*

    - **entityValues** *(list) --*

      A list of entity identifiers, such as EC2 instance IDs (``i-34ab692e`` ) or EBS volumes
      (``vol-426ab23e`` ).

      - *(string) --*

    - **eventTypeCategories** *(list) --*

      A list of event type category codes (``issue`` , ``scheduledChange`` , or
      ``accountNotification`` ).

      - *(string) --*

    - **tags** *(list) --*

      A map of entity tags attached to the affected entity.

      - *(dict) --*

        - *(string) --*

          - *(string) --*

    - **eventStatusCodes** *(list) --*

      A list of event status codes.

      - *(string) --*
    """


_DescribeAffectedEntitiesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeAffectedEntitiesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeAffectedEntitiesPaginatePaginationConfigTypeDef(
    _DescribeAffectedEntitiesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeAffectedEntitiesPaginate` `PaginationConfig`

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


_DescribeAffectedEntitiesPaginatefilterlastUpdatedTimesTypeDef = TypedDict(
    "_DescribeAffectedEntitiesPaginatefilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class DescribeAffectedEntitiesPaginatefilterlastUpdatedTimesTypeDef(
    _DescribeAffectedEntitiesPaginatefilterlastUpdatedTimesTypeDef
):
    """
    Type definition for `DescribeAffectedEntitiesPaginatefilter` `lastUpdatedTimes`

    A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
    ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
    ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
    is set and ``to`` is not set: match items where the timestamp value is equal to or after
    ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
    equal to or before ``to`` .

    - **from** *(datetime) --*

      The starting date and time of a time range.

    - **to** *(datetime) --*

      The ending date and time of a time range.
    """


_RequiredDescribeAffectedEntitiesPaginatefilterTypeDef = TypedDict(
    "_RequiredDescribeAffectedEntitiesPaginatefilterTypeDef", {"eventArns": List[str]}
)
_OptionalDescribeAffectedEntitiesPaginatefilterTypeDef = TypedDict(
    "_OptionalDescribeAffectedEntitiesPaginatefilterTypeDef",
    {
        "entityArns": List[str],
        "entityValues": List[str],
        "lastUpdatedTimes": List[
            DescribeAffectedEntitiesPaginatefilterlastUpdatedTimesTypeDef
        ],
        "tags": List[Dict[str, str]],
        "statusCodes": List[str],
    },
    total=False,
)


class DescribeAffectedEntitiesPaginatefilterTypeDef(
    _RequiredDescribeAffectedEntitiesPaginatefilterTypeDef,
    _OptionalDescribeAffectedEntitiesPaginatefilterTypeDef,
):
    """
    Type definition for `DescribeAffectedEntitiesPaginate` `filter`

    Values to narrow the results returned. At least one event ARN is required.

    - **eventArns** *(list) --* **[REQUIRED]**

      A list of event ARNs (unique identifiers). For example:
      ``"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
      "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"``

      - *(string) --*

    - **entityArns** *(list) --*

      A list of entity ARNs (unique identifiers).

      - *(string) --*

    - **entityValues** *(list) --*

      A list of IDs for affected entities.

      - *(string) --*

    - **lastUpdatedTimes** *(list) --*

      A list of the most recent dates and times that the entity was updated.

      - *(dict) --*

        A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
        ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
        ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
        is set and ``to`` is not set: match items where the timestamp value is equal to or after
        ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
        equal to or before ``to`` .

        - **from** *(datetime) --*

          The starting date and time of a time range.

        - **to** *(datetime) --*

          The ending date and time of a time range.

    - **tags** *(list) --*

      A map of entity tags attached to the affected entity.

      - *(dict) --*

        - *(string) --*

          - *(string) --*

    - **statusCodes** *(list) --*

      A list of entity status codes (``IMPAIRED`` , ``UNIMPAIRED`` , or ``UNKNOWN`` ).

      - *(string) --*
    """


_DescribeEventAggregatesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEventAggregatesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEventAggregatesPaginatePaginationConfigTypeDef(
    _DescribeEventAggregatesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeEventAggregatesPaginate` `PaginationConfig`

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


_DescribeEventAggregatesPaginateResponseeventAggregatesTypeDef = TypedDict(
    "_DescribeEventAggregatesPaginateResponseeventAggregatesTypeDef",
    {"aggregateValue": str, "count": int},
    total=False,
)


class DescribeEventAggregatesPaginateResponseeventAggregatesTypeDef(
    _DescribeEventAggregatesPaginateResponseeventAggregatesTypeDef
):
    """
    Type definition for `DescribeEventAggregatesPaginateResponse` `eventAggregates`

    The number of events of each issue type. Returned by the  DescribeEventAggregates operation.

    - **aggregateValue** *(string) --*

      The issue type for the associated count.

    - **count** *(integer) --*

      The number of events of the associated issue type.
    """


_DescribeEventAggregatesPaginateResponseTypeDef = TypedDict(
    "_DescribeEventAggregatesPaginateResponseTypeDef",
    {
        "eventAggregates": List[
            DescribeEventAggregatesPaginateResponseeventAggregatesTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class DescribeEventAggregatesPaginateResponseTypeDef(
    _DescribeEventAggregatesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeEventAggregatesPaginate` `Response`

    - **eventAggregates** *(list) --*

      The number of events in each category that meet the optional filter criteria.

      - *(dict) --*

        The number of events of each issue type. Returned by the  DescribeEventAggregates operation.

        - **aggregateValue** *(string) --*

          The issue type for the associated count.

        - **count** *(integer) --*

          The number of events of the associated issue type.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeEventAggregatesPaginatefilterendTimesTypeDef = TypedDict(
    "_DescribeEventAggregatesPaginatefilterendTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class DescribeEventAggregatesPaginatefilterendTimesTypeDef(
    _DescribeEventAggregatesPaginatefilterendTimesTypeDef
):
    """
    Type definition for `DescribeEventAggregatesPaginatefilter` `endTimes`

    A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
    ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
    ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
    is set and ``to`` is not set: match items where the timestamp value is equal to or after
    ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
    equal to or before ``to`` .

    - **from** *(datetime) --*

      The starting date and time of a time range.

    - **to** *(datetime) --*

      The ending date and time of a time range.
    """


_DescribeEventAggregatesPaginatefilterlastUpdatedTimesTypeDef = TypedDict(
    "_DescribeEventAggregatesPaginatefilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class DescribeEventAggregatesPaginatefilterlastUpdatedTimesTypeDef(
    _DescribeEventAggregatesPaginatefilterlastUpdatedTimesTypeDef
):
    """
    Type definition for `DescribeEventAggregatesPaginatefilter` `lastUpdatedTimes`

    A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
    ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
    ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
    is set and ``to`` is not set: match items where the timestamp value is equal to or after
    ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
    equal to or before ``to`` .

    - **from** *(datetime) --*

      The starting date and time of a time range.

    - **to** *(datetime) --*

      The ending date and time of a time range.
    """


_DescribeEventAggregatesPaginatefilterstartTimesTypeDef = TypedDict(
    "_DescribeEventAggregatesPaginatefilterstartTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class DescribeEventAggregatesPaginatefilterstartTimesTypeDef(
    _DescribeEventAggregatesPaginatefilterstartTimesTypeDef
):
    """
    Type definition for `DescribeEventAggregatesPaginatefilter` `startTimes`

    A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
    ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
    ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
    is set and ``to`` is not set: match items where the timestamp value is equal to or after
    ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
    equal to or before ``to`` .

    - **from** *(datetime) --*

      The starting date and time of a time range.

    - **to** *(datetime) --*

      The ending date and time of a time range.
    """


_DescribeEventAggregatesPaginatefilterTypeDef = TypedDict(
    "_DescribeEventAggregatesPaginatefilterTypeDef",
    {
        "eventArns": List[str],
        "eventTypeCodes": List[str],
        "services": List[str],
        "regions": List[str],
        "availabilityZones": List[str],
        "startTimes": List[DescribeEventAggregatesPaginatefilterstartTimesTypeDef],
        "endTimes": List[DescribeEventAggregatesPaginatefilterendTimesTypeDef],
        "lastUpdatedTimes": List[
            DescribeEventAggregatesPaginatefilterlastUpdatedTimesTypeDef
        ],
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[str],
        "tags": List[Dict[str, str]],
        "eventStatusCodes": List[str],
    },
    total=False,
)


class DescribeEventAggregatesPaginatefilterTypeDef(
    _DescribeEventAggregatesPaginatefilterTypeDef
):
    """
    Type definition for `DescribeEventAggregatesPaginate` `filter`

    Values to narrow the results returned.

    - **eventArns** *(list) --*

      A list of event ARNs (unique identifiers). For example:
      ``"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
      "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"``

      - *(string) --*

    - **eventTypeCodes** *(list) --*

      A list of unique identifiers for event types. For example,
      ``"AWS_EC2_SYSTEM_MAINTENANCE_EVENT","AWS_RDS_MAINTENANCE_SCHEDULED"``

      - *(string) --*

    - **services** *(list) --*

      The AWS services associated with the event. For example, ``EC2`` , ``RDS`` .

      - *(string) --*

    - **regions** *(list) --*

      A list of AWS regions.

      - *(string) --*

    - **availabilityZones** *(list) --*

      A list of AWS availability zones.

      - *(string) --*

    - **startTimes** *(list) --*

      A list of dates and times that the event began.

      - *(dict) --*

        A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
        ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
        ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
        is set and ``to`` is not set: match items where the timestamp value is equal to or after
        ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
        equal to or before ``to`` .

        - **from** *(datetime) --*

          The starting date and time of a time range.

        - **to** *(datetime) --*

          The ending date and time of a time range.

    - **endTimes** *(list) --*

      A list of dates and times that the event ended.

      - *(dict) --*

        A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
        ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
        ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
        is set and ``to`` is not set: match items where the timestamp value is equal to or after
        ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
        equal to or before ``to`` .

        - **from** *(datetime) --*

          The starting date and time of a time range.

        - **to** *(datetime) --*

          The ending date and time of a time range.

    - **lastUpdatedTimes** *(list) --*

      A list of dates and times that the event was last updated.

      - *(dict) --*

        A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
        ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
        ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
        is set and ``to`` is not set: match items where the timestamp value is equal to or after
        ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
        equal to or before ``to`` .

        - **from** *(datetime) --*

          The starting date and time of a time range.

        - **to** *(datetime) --*

          The ending date and time of a time range.

    - **entityArns** *(list) --*

      A list of entity ARNs (unique identifiers).

      - *(string) --*

    - **entityValues** *(list) --*

      A list of entity identifiers, such as EC2 instance IDs (``i-34ab692e`` ) or EBS volumes
      (``vol-426ab23e`` ).

      - *(string) --*

    - **eventTypeCategories** *(list) --*

      A list of event type category codes (``issue`` , ``scheduledChange`` , or
      ``accountNotification`` ).

      - *(string) --*

    - **tags** *(list) --*

      A map of entity tags attached to the affected entity.

      - *(dict) --*

        - *(string) --*

          - *(string) --*

    - **eventStatusCodes** *(list) --*

      A list of event status codes.

      - *(string) --*
    """


_DescribeEventTypesPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEventTypesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEventTypesPaginatePaginationConfigTypeDef(
    _DescribeEventTypesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeEventTypesPaginate` `PaginationConfig`

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


_DescribeEventTypesPaginateResponseeventTypesTypeDef = TypedDict(
    "_DescribeEventTypesPaginateResponseeventTypesTypeDef",
    {"service": str, "code": str, "category": str},
    total=False,
)


class DescribeEventTypesPaginateResponseeventTypesTypeDef(
    _DescribeEventTypesPaginateResponseeventTypesTypeDef
):
    """
    Type definition for `DescribeEventTypesPaginateResponse` `eventTypes`

    Metadata about a type of event that is reported by AWS Health. Data consists of the
    category (for example, ``issue`` ), the service (for example, ``EC2`` ), and the event type
    code (for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` ).

    - **service** *(string) --*

      The AWS service that is affected by the event. For example, ``EC2`` , ``RDS`` .

    - **code** *(string) --*

      The unique identifier for the event type. The format is ``AWS_*SERVICE* _*DESCRIPTION* ``
      ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` .

    - **category** *(string) --*

      A list of event type category codes (``issue`` , ``scheduledChange`` , or
      ``accountNotification`` ).
    """


_DescribeEventTypesPaginateResponseTypeDef = TypedDict(
    "_DescribeEventTypesPaginateResponseTypeDef",
    {
        "eventTypes": List[DescribeEventTypesPaginateResponseeventTypesTypeDef],
        "NextToken": str,
    },
    total=False,
)


class DescribeEventTypesPaginateResponseTypeDef(
    _DescribeEventTypesPaginateResponseTypeDef
):
    """
    Type definition for `DescribeEventTypesPaginate` `Response`

    - **eventTypes** *(list) --*

      A list of event types that match the filter criteria. Event types have a category (``issue``
      , ``accountNotification`` , or ``scheduledChange`` ), a service (for example, ``EC2`` ,
      ``RDS`` , ``DATAPIPELINE`` , ``BILLING`` ), and a code (in the format ``AWS_*SERVICE*
      _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` ).

      - *(dict) --*

        Metadata about a type of event that is reported by AWS Health. Data consists of the
        category (for example, ``issue`` ), the service (for example, ``EC2`` ), and the event type
        code (for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` ).

        - **service** *(string) --*

          The AWS service that is affected by the event. For example, ``EC2`` , ``RDS`` .

        - **code** *(string) --*

          The unique identifier for the event type. The format is ``AWS_*SERVICE* _*DESCRIPTION* ``
          ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT`` .

        - **category** *(string) --*

          A list of event type category codes (``issue`` , ``scheduledChange`` , or
          ``accountNotification`` ).

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_DescribeEventTypesPaginatefilterTypeDef = TypedDict(
    "_DescribeEventTypesPaginatefilterTypeDef",
    {
        "eventTypeCodes": List[str],
        "services": List[str],
        "eventTypeCategories": List[str],
    },
    total=False,
)


class DescribeEventTypesPaginatefilterTypeDef(_DescribeEventTypesPaginatefilterTypeDef):
    """
    Type definition for `DescribeEventTypesPaginate` `filter`

    Values to narrow the results returned.

    - **eventTypeCodes** *(list) --*

      A list of event type codes.

      - *(string) --*

    - **services** *(list) --*

      The AWS services associated with the event. For example, ``EC2`` , ``RDS`` .

      - *(string) --*

    - **eventTypeCategories** *(list) --*

      A list of event type category codes (``issue`` , ``scheduledChange`` , or
      ``accountNotification`` ).

      - *(string) --*
    """


_DescribeEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_DescribeEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class DescribeEventsPaginatePaginationConfigTypeDef(
    _DescribeEventsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `DescribeEventsPaginate` `PaginationConfig`

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


_DescribeEventsPaginatefilterendTimesTypeDef = TypedDict(
    "_DescribeEventsPaginatefilterendTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class DescribeEventsPaginatefilterendTimesTypeDef(
    _DescribeEventsPaginatefilterendTimesTypeDef
):
    """
    Type definition for `DescribeEventsPaginatefilter` `endTimes`

    A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
    ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
    ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
    is set and ``to`` is not set: match items where the timestamp value is equal to or after
    ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
    equal to or before ``to`` .

    - **from** *(datetime) --*

      The starting date and time of a time range.

    - **to** *(datetime) --*

      The ending date and time of a time range.
    """


_DescribeEventsPaginatefilterlastUpdatedTimesTypeDef = TypedDict(
    "_DescribeEventsPaginatefilterlastUpdatedTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class DescribeEventsPaginatefilterlastUpdatedTimesTypeDef(
    _DescribeEventsPaginatefilterlastUpdatedTimesTypeDef
):
    """
    Type definition for `DescribeEventsPaginatefilter` `lastUpdatedTimes`

    A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
    ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
    ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
    is set and ``to`` is not set: match items where the timestamp value is equal to or after
    ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
    equal to or before ``to`` .

    - **from** *(datetime) --*

      The starting date and time of a time range.

    - **to** *(datetime) --*

      The ending date and time of a time range.
    """


_DescribeEventsPaginatefilterstartTimesTypeDef = TypedDict(
    "_DescribeEventsPaginatefilterstartTimesTypeDef",
    {"from": datetime, "to": datetime},
    total=False,
)


class DescribeEventsPaginatefilterstartTimesTypeDef(
    _DescribeEventsPaginatefilterstartTimesTypeDef
):
    """
    Type definition for `DescribeEventsPaginatefilter` `startTimes`

    A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
    ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
    ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
    is set and ``to`` is not set: match items where the timestamp value is equal to or after
    ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
    equal to or before ``to`` .

    - **from** *(datetime) --*

      The starting date and time of a time range.

    - **to** *(datetime) --*

      The ending date and time of a time range.
    """


_DescribeEventsPaginatefilterTypeDef = TypedDict(
    "_DescribeEventsPaginatefilterTypeDef",
    {
        "eventArns": List[str],
        "eventTypeCodes": List[str],
        "services": List[str],
        "regions": List[str],
        "availabilityZones": List[str],
        "startTimes": List[DescribeEventsPaginatefilterstartTimesTypeDef],
        "endTimes": List[DescribeEventsPaginatefilterendTimesTypeDef],
        "lastUpdatedTimes": List[DescribeEventsPaginatefilterlastUpdatedTimesTypeDef],
        "entityArns": List[str],
        "entityValues": List[str],
        "eventTypeCategories": List[str],
        "tags": List[Dict[str, str]],
        "eventStatusCodes": List[str],
    },
    total=False,
)


class DescribeEventsPaginatefilterTypeDef(_DescribeEventsPaginatefilterTypeDef):
    """
    Type definition for `DescribeEventsPaginate` `filter`

    Values to narrow the results returned.

    - **eventArns** *(list) --*

      A list of event ARNs (unique identifiers). For example:
      ``"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
      "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"``

      - *(string) --*

    - **eventTypeCodes** *(list) --*

      A list of unique identifiers for event types. For example,
      ``"AWS_EC2_SYSTEM_MAINTENANCE_EVENT","AWS_RDS_MAINTENANCE_SCHEDULED"``

      - *(string) --*

    - **services** *(list) --*

      The AWS services associated with the event. For example, ``EC2`` , ``RDS`` .

      - *(string) --*

    - **regions** *(list) --*

      A list of AWS regions.

      - *(string) --*

    - **availabilityZones** *(list) --*

      A list of AWS availability zones.

      - *(string) --*

    - **startTimes** *(list) --*

      A list of dates and times that the event began.

      - *(dict) --*

        A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
        ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
        ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
        is set and ``to`` is not set: match items where the timestamp value is equal to or after
        ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
        equal to or before ``to`` .

        - **from** *(datetime) --*

          The starting date and time of a time range.

        - **to** *(datetime) --*

          The ending date and time of a time range.

    - **endTimes** *(list) --*

      A list of dates and times that the event ended.

      - *(dict) --*

        A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
        ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
        ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
        is set and ``to`` is not set: match items where the timestamp value is equal to or after
        ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
        equal to or before ``to`` .

        - **from** *(datetime) --*

          The starting date and time of a time range.

        - **to** *(datetime) --*

          The ending date and time of a time range.

    - **lastUpdatedTimes** *(list) --*

      A list of dates and times that the event was last updated.

      - *(dict) --*

        A range of dates and times that is used by the  EventFilter and  EntityFilter objects. If
        ``from`` is set and ``to`` is set: match items where the timestamp (``startTime`` ,
        ``endTime`` , or ``lastUpdatedTime`` ) is between ``from`` and ``to`` inclusive. If ``from``
        is set and ``to`` is not set: match items where the timestamp value is equal to or after
        ``from`` . If ``from`` is not set and ``to`` is set: match items where the timestamp value is
        equal to or before ``to`` .

        - **from** *(datetime) --*

          The starting date and time of a time range.

        - **to** *(datetime) --*

          The ending date and time of a time range.

    - **entityArns** *(list) --*

      A list of entity ARNs (unique identifiers).

      - *(string) --*

    - **entityValues** *(list) --*

      A list of entity identifiers, such as EC2 instance IDs (``i-34ab692e`` ) or EBS volumes
      (``vol-426ab23e`` ).

      - *(string) --*

    - **eventTypeCategories** *(list) --*

      A list of event type category codes (``issue`` , ``scheduledChange`` , or
      ``accountNotification`` ).

      - *(string) --*

    - **tags** *(list) --*

      A map of entity tags attached to the affected entity.

      - *(dict) --*

        - *(string) --*

          - *(string) --*

    - **eventStatusCodes** *(list) --*

      A list of event status codes.

      - *(string) --*
    """

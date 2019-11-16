"Main interface for iot1click-devices type defs"
from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientClaimDevicesByClaimCodeResponseTypeDef",
    "ClientDescribeDeviceResponseDeviceDescriptionTypeDef",
    "ClientDescribeDeviceResponseTypeDef",
    "ClientFinalizeDeviceClaimResponseTypeDef",
    "ClientGetDeviceMethodsResponseDeviceMethodsTypeDef",
    "ClientGetDeviceMethodsResponseTypeDef",
    "ClientInitiateDeviceClaimResponseTypeDef",
    "ClientInvokeDeviceMethodDeviceMethodTypeDef",
    "ClientInvokeDeviceMethodResponseTypeDef",
    "ClientListDeviceEventsResponseEventsDeviceTypeDef",
    "ClientListDeviceEventsResponseEventsTypeDef",
    "ClientListDeviceEventsResponseTypeDef",
    "ClientListDevicesResponseDevicesTypeDef",
    "ClientListDevicesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientUnclaimDeviceResponseTypeDef",
    "ListDeviceEventsPaginatePaginationConfigTypeDef",
    "ListDeviceEventsPaginateResponseEventsDeviceTypeDef",
    "ListDeviceEventsPaginateResponseEventsTypeDef",
    "ListDeviceEventsPaginateResponseTypeDef",
    "ListDevicesPaginatePaginationConfigTypeDef",
    "ListDevicesPaginateResponseDevicesTypeDef",
    "ListDevicesPaginateResponseTypeDef",
)


_ClientClaimDevicesByClaimCodeResponseTypeDef = TypedDict(
    "_ClientClaimDevicesByClaimCodeResponseTypeDef",
    {"ClaimCode": str, "Total": int},
    total=False,
)


class ClientClaimDevicesByClaimCodeResponseTypeDef(
    _ClientClaimDevicesByClaimCodeResponseTypeDef
):
    """
    Type definition for `ClientClaimDevicesByClaimCode` `Response`

    200 response

    - **ClaimCode** *(string) --*

      The claim code provided by the device manufacturer.

    - **Total** *(integer) --*

      The total number of devices associated with the claim code that has been processed in the
      claim request.
    """


_ClientDescribeDeviceResponseDeviceDescriptionTypeDef = TypedDict(
    "_ClientDescribeDeviceResponseDeviceDescriptionTypeDef",
    {
        "Arn": str,
        "Attributes": Dict[str, str],
        "DeviceId": str,
        "Enabled": bool,
        "RemainingLife": float,
        "Type": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeDeviceResponseDeviceDescriptionTypeDef(
    _ClientDescribeDeviceResponseDeviceDescriptionTypeDef
):
    """
    Type definition for `ClientDescribeDeviceResponse` `DeviceDescription`

    Device details.

    - **Arn** *(string) --*

      The ARN of the device.

    - **Attributes** *(dict) --*

      An array of zero or more elements of DeviceAttribute objects providing user specified
      device attributes.

      - *(string) --*

        - *(string) --*

    - **DeviceId** *(string) --*

      The unique identifier of the device.

    - **Enabled** *(boolean) --*

      A Boolean value indicating whether or not the device is enabled.

    - **RemainingLife** *(float) --*

      A value between 0 and 1 inclusive, representing the fraction of life remaining for the
      device.

    - **Type** *(string) --*

      The type of the device, such as "button".

    - **Tags** *(dict) --*

      The tags currently associated with the AWS IoT 1-Click device.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeDeviceResponseTypeDef = TypedDict(
    "_ClientDescribeDeviceResponseTypeDef",
    {"DeviceDescription": ClientDescribeDeviceResponseDeviceDescriptionTypeDef},
    total=False,
)


class ClientDescribeDeviceResponseTypeDef(_ClientDescribeDeviceResponseTypeDef):
    """
    Type definition for `ClientDescribeDevice` `Response`

    200 response

    - **DeviceDescription** *(dict) --*

      Device details.

      - **Arn** *(string) --*

        The ARN of the device.

      - **Attributes** *(dict) --*

        An array of zero or more elements of DeviceAttribute objects providing user specified
        device attributes.

        - *(string) --*

          - *(string) --*

      - **DeviceId** *(string) --*

        The unique identifier of the device.

      - **Enabled** *(boolean) --*

        A Boolean value indicating whether or not the device is enabled.

      - **RemainingLife** *(float) --*

        A value between 0 and 1 inclusive, representing the fraction of life remaining for the
        device.

      - **Type** *(string) --*

        The type of the device, such as "button".

      - **Tags** *(dict) --*

        The tags currently associated with the AWS IoT 1-Click device.

        - *(string) --*

          - *(string) --*
    """


_ClientFinalizeDeviceClaimResponseTypeDef = TypedDict(
    "_ClientFinalizeDeviceClaimResponseTypeDef", {"State": str}, total=False
)


class ClientFinalizeDeviceClaimResponseTypeDef(
    _ClientFinalizeDeviceClaimResponseTypeDef
):
    """
    Type definition for `ClientFinalizeDeviceClaim` `Response`

    200 response

    - **State** *(string) --*

      The device's final claim state.
    """


_ClientGetDeviceMethodsResponseDeviceMethodsTypeDef = TypedDict(
    "_ClientGetDeviceMethodsResponseDeviceMethodsTypeDef",
    {"DeviceType": str, "MethodName": str},
    total=False,
)


class ClientGetDeviceMethodsResponseDeviceMethodsTypeDef(
    _ClientGetDeviceMethodsResponseDeviceMethodsTypeDef
):
    """
    Type definition for `ClientGetDeviceMethodsResponse` `DeviceMethods`

    - **DeviceType** *(string) --*

      The type of the device, such as "button".

    - **MethodName** *(string) --*

      The name of the method applicable to the deviceType.
    """


_ClientGetDeviceMethodsResponseTypeDef = TypedDict(
    "_ClientGetDeviceMethodsResponseTypeDef",
    {"DeviceMethods": List[ClientGetDeviceMethodsResponseDeviceMethodsTypeDef]},
    total=False,
)


class ClientGetDeviceMethodsResponseTypeDef(_ClientGetDeviceMethodsResponseTypeDef):
    """
    Type definition for `ClientGetDeviceMethods` `Response`

    200 response

    - **DeviceMethods** *(list) --*

      List of available device APIs.

      - *(dict) --*

        - **DeviceType** *(string) --*

          The type of the device, such as "button".

        - **MethodName** *(string) --*

          The name of the method applicable to the deviceType.
    """


_ClientInitiateDeviceClaimResponseTypeDef = TypedDict(
    "_ClientInitiateDeviceClaimResponseTypeDef", {"State": str}, total=False
)


class ClientInitiateDeviceClaimResponseTypeDef(
    _ClientInitiateDeviceClaimResponseTypeDef
):
    """
    Type definition for `ClientInitiateDeviceClaim` `Response`

    200 response

    - **State** *(string) --*

      The device's final claim state.
    """


_ClientInvokeDeviceMethodDeviceMethodTypeDef = TypedDict(
    "_ClientInvokeDeviceMethodDeviceMethodTypeDef",
    {"DeviceType": str, "MethodName": str},
    total=False,
)


class ClientInvokeDeviceMethodDeviceMethodTypeDef(
    _ClientInvokeDeviceMethodDeviceMethodTypeDef
):
    """
    Type definition for `ClientInvokeDeviceMethod` `DeviceMethod`

    The device method to invoke.

    - **DeviceType** *(string) --*

      The type of the device, such as "button".

    - **MethodName** *(string) --*

      The name of the method applicable to the deviceType.
    """


_ClientInvokeDeviceMethodResponseTypeDef = TypedDict(
    "_ClientInvokeDeviceMethodResponseTypeDef",
    {"DeviceMethodResponse": str},
    total=False,
)


class ClientInvokeDeviceMethodResponseTypeDef(_ClientInvokeDeviceMethodResponseTypeDef):
    """
    Type definition for `ClientInvokeDeviceMethod` `Response`

    200 response

    - **DeviceMethodResponse** *(string) --*

      A JSON encoded string containing the device method response.
    """


_ClientListDeviceEventsResponseEventsDeviceTypeDef = TypedDict(
    "_ClientListDeviceEventsResponseEventsDeviceTypeDef",
    {"Attributes": Dict, "DeviceId": str, "Type": str},
    total=False,
)


class ClientListDeviceEventsResponseEventsDeviceTypeDef(
    _ClientListDeviceEventsResponseEventsDeviceTypeDef
):
    """
    Type definition for `ClientListDeviceEventsResponseEvents` `Device`

    An object representing the device associated with the event.

    - **Attributes** *(dict) --*

      The user specified attributes associated with the device for an event.

    - **DeviceId** *(string) --*

      The unique identifier of the device.

    - **Type** *(string) --*

      The device type, such as "button".
    """


_ClientListDeviceEventsResponseEventsTypeDef = TypedDict(
    "_ClientListDeviceEventsResponseEventsTypeDef",
    {"Device": ClientListDeviceEventsResponseEventsDeviceTypeDef, "StdEvent": str},
    total=False,
)


class ClientListDeviceEventsResponseEventsTypeDef(
    _ClientListDeviceEventsResponseEventsTypeDef
):
    """
    Type definition for `ClientListDeviceEventsResponse` `Events`

    - **Device** *(dict) --*

      An object representing the device associated with the event.

      - **Attributes** *(dict) --*

        The user specified attributes associated with the device for an event.

      - **DeviceId** *(string) --*

        The unique identifier of the device.

      - **Type** *(string) --*

        The device type, such as "button".

    - **StdEvent** *(string) --*

      A serialized JSON object representing the device-type specific event.
    """


_ClientListDeviceEventsResponseTypeDef = TypedDict(
    "_ClientListDeviceEventsResponseTypeDef",
    {"Events": List[ClientListDeviceEventsResponseEventsTypeDef], "NextToken": str},
    total=False,
)


class ClientListDeviceEventsResponseTypeDef(_ClientListDeviceEventsResponseTypeDef):
    """
    Type definition for `ClientListDeviceEvents` `Response`

    200 response

    - **Events** *(list) --*

      An array of zero or more elements describing the event(s) associated with the device.

      - *(dict) --*

        - **Device** *(dict) --*

          An object representing the device associated with the event.

          - **Attributes** *(dict) --*

            The user specified attributes associated with the device for an event.

          - **DeviceId** *(string) --*

            The unique identifier of the device.

          - **Type** *(string) --*

            The device type, such as "button".

        - **StdEvent** *(string) --*

          A serialized JSON object representing the device-type specific event.

    - **NextToken** *(string) --*

      The token to retrieve the next set of results.
    """


_ClientListDevicesResponseDevicesTypeDef = TypedDict(
    "_ClientListDevicesResponseDevicesTypeDef",
    {
        "Arn": str,
        "Attributes": Dict[str, str],
        "DeviceId": str,
        "Enabled": bool,
        "RemainingLife": float,
        "Type": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ClientListDevicesResponseDevicesTypeDef(_ClientListDevicesResponseDevicesTypeDef):
    """
    Type definition for `ClientListDevicesResponse` `Devices`

    - **Arn** *(string) --*

      The ARN of the device.

    - **Attributes** *(dict) --*

      An array of zero or more elements of DeviceAttribute objects providing user specified
      device attributes.

      - *(string) --*

        - *(string) --*

    - **DeviceId** *(string) --*

      The unique identifier of the device.

    - **Enabled** *(boolean) --*

      A Boolean value indicating whether or not the device is enabled.

    - **RemainingLife** *(float) --*

      A value between 0 and 1 inclusive, representing the fraction of life remaining for the
      device.

    - **Type** *(string) --*

      The type of the device, such as "button".

    - **Tags** *(dict) --*

      The tags currently associated with the AWS IoT 1-Click device.

      - *(string) --*

        - *(string) --*
    """


_ClientListDevicesResponseTypeDef = TypedDict(
    "_ClientListDevicesResponseTypeDef",
    {"Devices": List[ClientListDevicesResponseDevicesTypeDef], "NextToken": str},
    total=False,
)


class ClientListDevicesResponseTypeDef(_ClientListDevicesResponseTypeDef):
    """
    Type definition for `ClientListDevices` `Response`

    200 response

    - **Devices** *(list) --*

      A list of devices.

      - *(dict) --*

        - **Arn** *(string) --*

          The ARN of the device.

        - **Attributes** *(dict) --*

          An array of zero or more elements of DeviceAttribute objects providing user specified
          device attributes.

          - *(string) --*

            - *(string) --*

        - **DeviceId** *(string) --*

          The unique identifier of the device.

        - **Enabled** *(boolean) --*

          A Boolean value indicating whether or not the device is enabled.

        - **RemainingLife** *(float) --*

          A value between 0 and 1 inclusive, representing the fraction of life remaining for the
          device.

        - **Type** *(string) --*

          The type of the device, such as "button".

        - **Tags** *(dict) --*

          The tags currently associated with the AWS IoT 1-Click device.

          - *(string) --*

            - *(string) --*

    - **NextToken** *(string) --*

      The token to retrieve the next set of results.
    """


_ClientListTagsForResourceResponseTypeDef = TypedDict(
    "_ClientListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)


class ClientListTagsForResourceResponseTypeDef(
    _ClientListTagsForResourceResponseTypeDef
):
    """
    Type definition for `ClientListTagsForResource` `Response`

    - **Tags** *(dict) --*

      A collection of key/value pairs defining the resource tags. For example, { "tags": {"key1":
      "value1", "key2": "value2"} }. For more information, see `AWS Tagging Strategies
      <https://aws.amazon.com/answers/account-management/aws-tagging-strategies/>`__ .

      - *(string) --*

        - *(string) --*
    """


_ClientUnclaimDeviceResponseTypeDef = TypedDict(
    "_ClientUnclaimDeviceResponseTypeDef", {"State": str}, total=False
)


class ClientUnclaimDeviceResponseTypeDef(_ClientUnclaimDeviceResponseTypeDef):
    """
    Type definition for `ClientUnclaimDevice` `Response`

    200 response

    - **State** *(string) --*

      The device's final claim state.
    """


_ListDeviceEventsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDeviceEventsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDeviceEventsPaginatePaginationConfigTypeDef(
    _ListDeviceEventsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDeviceEventsPaginate` `PaginationConfig`

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


_ListDeviceEventsPaginateResponseEventsDeviceTypeDef = TypedDict(
    "_ListDeviceEventsPaginateResponseEventsDeviceTypeDef",
    {"Attributes": Dict, "DeviceId": str, "Type": str},
    total=False,
)


class ListDeviceEventsPaginateResponseEventsDeviceTypeDef(
    _ListDeviceEventsPaginateResponseEventsDeviceTypeDef
):
    """
    Type definition for `ListDeviceEventsPaginateResponseEvents` `Device`

    An object representing the device associated with the event.

    - **Attributes** *(dict) --*

      The user specified attributes associated with the device for an event.

    - **DeviceId** *(string) --*

      The unique identifier of the device.

    - **Type** *(string) --*

      The device type, such as "button".
    """


_ListDeviceEventsPaginateResponseEventsTypeDef = TypedDict(
    "_ListDeviceEventsPaginateResponseEventsTypeDef",
    {"Device": ListDeviceEventsPaginateResponseEventsDeviceTypeDef, "StdEvent": str},
    total=False,
)


class ListDeviceEventsPaginateResponseEventsTypeDef(
    _ListDeviceEventsPaginateResponseEventsTypeDef
):
    """
    Type definition for `ListDeviceEventsPaginateResponse` `Events`

    - **Device** *(dict) --*

      An object representing the device associated with the event.

      - **Attributes** *(dict) --*

        The user specified attributes associated with the device for an event.

      - **DeviceId** *(string) --*

        The unique identifier of the device.

      - **Type** *(string) --*

        The device type, such as "button".

    - **StdEvent** *(string) --*

      A serialized JSON object representing the device-type specific event.
    """


_ListDeviceEventsPaginateResponseTypeDef = TypedDict(
    "_ListDeviceEventsPaginateResponseTypeDef",
    {"Events": List[ListDeviceEventsPaginateResponseEventsTypeDef]},
    total=False,
)


class ListDeviceEventsPaginateResponseTypeDef(_ListDeviceEventsPaginateResponseTypeDef):
    """
    Type definition for `ListDeviceEventsPaginate` `Response`

    200 response

    - **Events** *(list) --*

      An array of zero or more elements describing the event(s) associated with the device.

      - *(dict) --*

        - **Device** *(dict) --*

          An object representing the device associated with the event.

          - **Attributes** *(dict) --*

            The user specified attributes associated with the device for an event.

          - **DeviceId** *(string) --*

            The unique identifier of the device.

          - **Type** *(string) --*

            The device type, such as "button".

        - **StdEvent** *(string) --*

          A serialized JSON object representing the device-type specific event.
    """


_ListDevicesPaginatePaginationConfigTypeDef = TypedDict(
    "_ListDevicesPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListDevicesPaginatePaginationConfigTypeDef(
    _ListDevicesPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListDevicesPaginate` `PaginationConfig`

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


_ListDevicesPaginateResponseDevicesTypeDef = TypedDict(
    "_ListDevicesPaginateResponseDevicesTypeDef",
    {
        "Arn": str,
        "Attributes": Dict[str, str],
        "DeviceId": str,
        "Enabled": bool,
        "RemainingLife": float,
        "Type": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ListDevicesPaginateResponseDevicesTypeDef(
    _ListDevicesPaginateResponseDevicesTypeDef
):
    """
    Type definition for `ListDevicesPaginateResponse` `Devices`

    - **Arn** *(string) --*

      The ARN of the device.

    - **Attributes** *(dict) --*

      An array of zero or more elements of DeviceAttribute objects providing user specified
      device attributes.

      - *(string) --*

        - *(string) --*

    - **DeviceId** *(string) --*

      The unique identifier of the device.

    - **Enabled** *(boolean) --*

      A Boolean value indicating whether or not the device is enabled.

    - **RemainingLife** *(float) --*

      A value between 0 and 1 inclusive, representing the fraction of life remaining for the
      device.

    - **Type** *(string) --*

      The type of the device, such as "button".

    - **Tags** *(dict) --*

      The tags currently associated with the AWS IoT 1-Click device.

      - *(string) --*

        - *(string) --*
    """


_ListDevicesPaginateResponseTypeDef = TypedDict(
    "_ListDevicesPaginateResponseTypeDef",
    {"Devices": List[ListDevicesPaginateResponseDevicesTypeDef]},
    total=False,
)


class ListDevicesPaginateResponseTypeDef(_ListDevicesPaginateResponseTypeDef):
    """
    Type definition for `ListDevicesPaginate` `Response`

    200 response

    - **Devices** *(list) --*

      A list of devices.

      - *(dict) --*

        - **Arn** *(string) --*

          The ARN of the device.

        - **Attributes** *(dict) --*

          An array of zero or more elements of DeviceAttribute objects providing user specified
          device attributes.

          - *(string) --*

            - *(string) --*

        - **DeviceId** *(string) --*

          The unique identifier of the device.

        - **Enabled** *(boolean) --*

          A Boolean value indicating whether or not the device is enabled.

        - **RemainingLife** *(float) --*

          A value between 0 and 1 inclusive, representing the fraction of life remaining for the
          device.

        - **Type** *(string) --*

          The type of the device, such as "button".

        - **Tags** *(dict) --*

          The tags currently associated with the AWS IoT 1-Click device.

          - *(string) --*

            - *(string) --*
    """

"Main interface for iot1click-projects type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientCreateProjectplacementTemplatedeviceTemplatesTypeDef",
    "ClientCreateProjectplacementTemplateTypeDef",
    "ClientDescribePlacementResponseplacementTypeDef",
    "ClientDescribePlacementResponseTypeDef",
    "ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef",
    "ClientDescribeProjectResponseprojectplacementTemplateTypeDef",
    "ClientDescribeProjectResponseprojectTypeDef",
    "ClientDescribeProjectResponseTypeDef",
    "ClientGetDevicesInPlacementResponseTypeDef",
    "ClientListPlacementsResponseplacementsTypeDef",
    "ClientListPlacementsResponseTypeDef",
    "ClientListProjectsResponseprojectsTypeDef",
    "ClientListProjectsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientUpdateProjectplacementTemplatedeviceTemplatesTypeDef",
    "ClientUpdateProjectplacementTemplateTypeDef",
    "ListPlacementsPaginatePaginationConfigTypeDef",
    "ListPlacementsPaginateResponseplacementsTypeDef",
    "ListPlacementsPaginateResponseTypeDef",
    "ListProjectsPaginatePaginationConfigTypeDef",
    "ListProjectsPaginateResponseprojectsTypeDef",
    "ListProjectsPaginateResponseTypeDef",
)


_ClientCreateProjectplacementTemplatedeviceTemplatesTypeDef = TypedDict(
    "_ClientCreateProjectplacementTemplatedeviceTemplatesTypeDef",
    {"deviceType": str, "callbackOverrides": Dict[str, str]},
    total=False,
)


class ClientCreateProjectplacementTemplatedeviceTemplatesTypeDef(
    _ClientCreateProjectplacementTemplatedeviceTemplatesTypeDef
):
    """
    Type definition for `ClientCreateProjectplacementTemplate` `deviceTemplates`

    An object representing a device for a placement template (see  PlacementTemplate ).

    - **deviceType** *(string) --*

      The device type, which currently must be ``"button"`` .

    - **callbackOverrides** *(dict) --*

      An optional Lambda function to invoke instead of the default Lambda function provided by
      the placement template.

      - *(string) --*

        - *(string) --*
    """


_ClientCreateProjectplacementTemplateTypeDef = TypedDict(
    "_ClientCreateProjectplacementTemplateTypeDef",
    {
        "defaultAttributes": Dict[str, str],
        "deviceTemplates": Dict[
            str, ClientCreateProjectplacementTemplatedeviceTemplatesTypeDef
        ],
    },
    total=False,
)


class ClientCreateProjectplacementTemplateTypeDef(
    _ClientCreateProjectplacementTemplateTypeDef
):
    """
    Type definition for `ClientCreateProject` `placementTemplate`

    The schema defining the placement to be created. A placement template defines placement default
    attributes and device templates. You cannot add or remove device templates after the project has
    been created. However, you can update ``callbackOverrides`` for the device templates using the
    ``UpdateProject`` API.

    - **defaultAttributes** *(dict) --*

      The default attributes (key/value pairs) to be applied to all placements using this template.

      - *(string) --*

        - *(string) --*

    - **deviceTemplates** *(dict) --*

      An object specifying the  DeviceTemplate for all placements using this ( PlacementTemplate )
      template.

      - *(string) --*

        - *(dict) --*

          An object representing a device for a placement template (see  PlacementTemplate ).

          - **deviceType** *(string) --*

            The device type, which currently must be ``"button"`` .

          - **callbackOverrides** *(dict) --*

            An optional Lambda function to invoke instead of the default Lambda function provided by
            the placement template.

            - *(string) --*

              - *(string) --*
    """


_ClientDescribePlacementResponseplacementTypeDef = TypedDict(
    "_ClientDescribePlacementResponseplacementTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "attributes": Dict[str, str],
        "createdDate": datetime,
        "updatedDate": datetime,
    },
    total=False,
)


class ClientDescribePlacementResponseplacementTypeDef(
    _ClientDescribePlacementResponseplacementTypeDef
):
    """
    Type definition for `ClientDescribePlacementResponse` `placement`

    An object describing the placement.

    - **projectName** *(string) --*

      The name of the project containing the placement.

    - **placementName** *(string) --*

      The name of the placement.

    - **attributes** *(dict) --*

      The user-defined attributes associated with the placement.

      - *(string) --*

        - *(string) --*

    - **createdDate** *(datetime) --*

      The date when the placement was initially created, in UNIX epoch time format.

    - **updatedDate** *(datetime) --*

      The date when the placement was last updated, in UNIX epoch time format. If the placement
      was not updated, then ``createdDate`` and ``updatedDate`` are the same.
    """


_ClientDescribePlacementResponseTypeDef = TypedDict(
    "_ClientDescribePlacementResponseTypeDef",
    {"placement": ClientDescribePlacementResponseplacementTypeDef},
    total=False,
)


class ClientDescribePlacementResponseTypeDef(_ClientDescribePlacementResponseTypeDef):
    """
    Type definition for `ClientDescribePlacement` `Response`

    - **placement** *(dict) --*

      An object describing the placement.

      - **projectName** *(string) --*

        The name of the project containing the placement.

      - **placementName** *(string) --*

        The name of the placement.

      - **attributes** *(dict) --*

        The user-defined attributes associated with the placement.

        - *(string) --*

          - *(string) --*

      - **createdDate** *(datetime) --*

        The date when the placement was initially created, in UNIX epoch time format.

      - **updatedDate** *(datetime) --*

        The date when the placement was last updated, in UNIX epoch time format. If the placement
        was not updated, then ``createdDate`` and ``updatedDate`` are the same.
    """


_ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef = TypedDict(
    "_ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef",
    {"deviceType": str, "callbackOverrides": Dict[str, str]},
    total=False,
)


class ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef(
    _ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef
):
    """
    Type definition for `ClientDescribeProjectResponseprojectplacementTemplate` `deviceTemplates`

    An object representing a device for a placement template (see  PlacementTemplate ).

    - **deviceType** *(string) --*

      The device type, which currently must be ``"button"`` .

    - **callbackOverrides** *(dict) --*

      An optional Lambda function to invoke instead of the default Lambda function
      provided by the placement template.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeProjectResponseprojectplacementTemplateTypeDef = TypedDict(
    "_ClientDescribeProjectResponseprojectplacementTemplateTypeDef",
    {
        "defaultAttributes": Dict[str, str],
        "deviceTemplates": Dict[
            str,
            ClientDescribeProjectResponseprojectplacementTemplatedeviceTemplatesTypeDef,
        ],
    },
    total=False,
)


class ClientDescribeProjectResponseprojectplacementTemplateTypeDef(
    _ClientDescribeProjectResponseprojectplacementTemplateTypeDef
):
    """
    Type definition for `ClientDescribeProjectResponseproject` `placementTemplate`

    An object describing the project's placement specifications.

    - **defaultAttributes** *(dict) --*

      The default attributes (key/value pairs) to be applied to all placements using this
      template.

      - *(string) --*

        - *(string) --*

    - **deviceTemplates** *(dict) --*

      An object specifying the  DeviceTemplate for all placements using this (
      PlacementTemplate ) template.

      - *(string) --*

        - *(dict) --*

          An object representing a device for a placement template (see  PlacementTemplate ).

          - **deviceType** *(string) --*

            The device type, which currently must be ``"button"`` .

          - **callbackOverrides** *(dict) --*

            An optional Lambda function to invoke instead of the default Lambda function
            provided by the placement template.

            - *(string) --*

              - *(string) --*
    """


_ClientDescribeProjectResponseprojectTypeDef = TypedDict(
    "_ClientDescribeProjectResponseprojectTypeDef",
    {
        "arn": str,
        "projectName": str,
        "description": str,
        "createdDate": datetime,
        "updatedDate": datetime,
        "placementTemplate": ClientDescribeProjectResponseprojectplacementTemplateTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientDescribeProjectResponseprojectTypeDef(
    _ClientDescribeProjectResponseprojectTypeDef
):
    """
    Type definition for `ClientDescribeProjectResponse` `project`

    An object describing the project.

    - **arn** *(string) --*

      The ARN of the project.

    - **projectName** *(string) --*

      The name of the project for which to obtain information from.

    - **description** *(string) --*

      The description of the project.

    - **createdDate** *(datetime) --*

      The date when the project was originally created, in UNIX epoch time format.

    - **updatedDate** *(datetime) --*

      The date when the project was last updated, in UNIX epoch time format. If the project was
      not updated, then ``createdDate`` and ``updatedDate`` are the same.

    - **placementTemplate** *(dict) --*

      An object describing the project's placement specifications.

      - **defaultAttributes** *(dict) --*

        The default attributes (key/value pairs) to be applied to all placements using this
        template.

        - *(string) --*

          - *(string) --*

      - **deviceTemplates** *(dict) --*

        An object specifying the  DeviceTemplate for all placements using this (
        PlacementTemplate ) template.

        - *(string) --*

          - *(dict) --*

            An object representing a device for a placement template (see  PlacementTemplate ).

            - **deviceType** *(string) --*

              The device type, which currently must be ``"button"`` .

            - **callbackOverrides** *(dict) --*

              An optional Lambda function to invoke instead of the default Lambda function
              provided by the placement template.

              - *(string) --*

                - *(string) --*

    - **tags** *(dict) --*

      The tags (metadata key/value pairs) associated with the project.

      - *(string) --*

        - *(string) --*
    """


_ClientDescribeProjectResponseTypeDef = TypedDict(
    "_ClientDescribeProjectResponseTypeDef",
    {"project": ClientDescribeProjectResponseprojectTypeDef},
    total=False,
)


class ClientDescribeProjectResponseTypeDef(_ClientDescribeProjectResponseTypeDef):
    """
    Type definition for `ClientDescribeProject` `Response`

    - **project** *(dict) --*

      An object describing the project.

      - **arn** *(string) --*

        The ARN of the project.

      - **projectName** *(string) --*

        The name of the project for which to obtain information from.

      - **description** *(string) --*

        The description of the project.

      - **createdDate** *(datetime) --*

        The date when the project was originally created, in UNIX epoch time format.

      - **updatedDate** *(datetime) --*

        The date when the project was last updated, in UNIX epoch time format. If the project was
        not updated, then ``createdDate`` and ``updatedDate`` are the same.

      - **placementTemplate** *(dict) --*

        An object describing the project's placement specifications.

        - **defaultAttributes** *(dict) --*

          The default attributes (key/value pairs) to be applied to all placements using this
          template.

          - *(string) --*

            - *(string) --*

        - **deviceTemplates** *(dict) --*

          An object specifying the  DeviceTemplate for all placements using this (
          PlacementTemplate ) template.

          - *(string) --*

            - *(dict) --*

              An object representing a device for a placement template (see  PlacementTemplate ).

              - **deviceType** *(string) --*

                The device type, which currently must be ``"button"`` .

              - **callbackOverrides** *(dict) --*

                An optional Lambda function to invoke instead of the default Lambda function
                provided by the placement template.

                - *(string) --*

                  - *(string) --*

      - **tags** *(dict) --*

        The tags (metadata key/value pairs) associated with the project.

        - *(string) --*

          - *(string) --*
    """


_ClientGetDevicesInPlacementResponseTypeDef = TypedDict(
    "_ClientGetDevicesInPlacementResponseTypeDef",
    {"devices": Dict[str, str]},
    total=False,
)


class ClientGetDevicesInPlacementResponseTypeDef(
    _ClientGetDevicesInPlacementResponseTypeDef
):
    """
    Type definition for `ClientGetDevicesInPlacement` `Response`

    - **devices** *(dict) --*

      An object containing the devices (zero or more) within the placement.

      - *(string) --*

        - *(string) --*
    """


_ClientListPlacementsResponseplacementsTypeDef = TypedDict(
    "_ClientListPlacementsResponseplacementsTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
    },
    total=False,
)


class ClientListPlacementsResponseplacementsTypeDef(
    _ClientListPlacementsResponseplacementsTypeDef
):
    """
    Type definition for `ClientListPlacementsResponse` `placements`

    An object providing summary information for a particular placement.

    - **projectName** *(string) --*

      The name of the project containing the placement.

    - **placementName** *(string) --*

      The name of the placement being summarized.

    - **createdDate** *(datetime) --*

      The date when the placement was originally created, in UNIX epoch time format.

    - **updatedDate** *(datetime) --*

      The date when the placement was last updated, in UNIX epoch time format. If the placement
      was not updated, then ``createdDate`` and ``updatedDate`` are the same.
    """


_ClientListPlacementsResponseTypeDef = TypedDict(
    "_ClientListPlacementsResponseTypeDef",
    {
        "placements": List[ClientListPlacementsResponseplacementsTypeDef],
        "nextToken": str,
    },
    total=False,
)


class ClientListPlacementsResponseTypeDef(_ClientListPlacementsResponseTypeDef):
    """
    Type definition for `ClientListPlacements` `Response`

    - **placements** *(list) --*

      An object listing the requested placements.

      - *(dict) --*

        An object providing summary information for a particular placement.

        - **projectName** *(string) --*

          The name of the project containing the placement.

        - **placementName** *(string) --*

          The name of the placement being summarized.

        - **createdDate** *(datetime) --*

          The date when the placement was originally created, in UNIX epoch time format.

        - **updatedDate** *(datetime) --*

          The date when the placement was last updated, in UNIX epoch time format. If the placement
          was not updated, then ``createdDate`` and ``updatedDate`` are the same.

    - **nextToken** *(string) --*

      The token used to retrieve the next set of results - will be effectively empty if there are
      no further results.
    """


_ClientListProjectsResponseprojectsTypeDef = TypedDict(
    "_ClientListProjectsResponseprojectsTypeDef",
    {
        "arn": str,
        "projectName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ClientListProjectsResponseprojectsTypeDef(
    _ClientListProjectsResponseprojectsTypeDef
):
    """
    Type definition for `ClientListProjectsResponse` `projects`

    An object providing summary information for a particular project for an associated AWS
    account and region.

    - **arn** *(string) --*

      The ARN of the project.

    - **projectName** *(string) --*

      The name of the project being summarized.

    - **createdDate** *(datetime) --*

      The date when the project was originally created, in UNIX epoch time format.

    - **updatedDate** *(datetime) --*

      The date when the project was last updated, in UNIX epoch time format. If the project was
      not updated, then ``createdDate`` and ``updatedDate`` are the same.

    - **tags** *(dict) --*

      The tags (metadata key/value pairs) associated with the project.

      - *(string) --*

        - *(string) --*
    """


_ClientListProjectsResponseTypeDef = TypedDict(
    "_ClientListProjectsResponseTypeDef",
    {"projects": List[ClientListProjectsResponseprojectsTypeDef], "nextToken": str},
    total=False,
)


class ClientListProjectsResponseTypeDef(_ClientListProjectsResponseTypeDef):
    """
    Type definition for `ClientListProjects` `Response`

    - **projects** *(list) --*

      An object containing the list of projects.

      - *(dict) --*

        An object providing summary information for a particular project for an associated AWS
        account and region.

        - **arn** *(string) --*

          The ARN of the project.

        - **projectName** *(string) --*

          The name of the project being summarized.

        - **createdDate** *(datetime) --*

          The date when the project was originally created, in UNIX epoch time format.

        - **updatedDate** *(datetime) --*

          The date when the project was last updated, in UNIX epoch time format. If the project was
          not updated, then ``createdDate`` and ``updatedDate`` are the same.

        - **tags** *(dict) --*

          The tags (metadata key/value pairs) associated with the project.

          - *(string) --*

            - *(string) --*

    - **nextToken** *(string) --*

      The token used to retrieve the next set of results - will be effectively empty if there are
      no further results.
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

      The tags (metadata key/value pairs) which you have assigned to the resource.

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateProjectplacementTemplatedeviceTemplatesTypeDef = TypedDict(
    "_ClientUpdateProjectplacementTemplatedeviceTemplatesTypeDef",
    {"deviceType": str, "callbackOverrides": Dict[str, str]},
    total=False,
)


class ClientUpdateProjectplacementTemplatedeviceTemplatesTypeDef(
    _ClientUpdateProjectplacementTemplatedeviceTemplatesTypeDef
):
    """
    Type definition for `ClientUpdateProjectplacementTemplate` `deviceTemplates`

    An object representing a device for a placement template (see  PlacementTemplate ).

    - **deviceType** *(string) --*

      The device type, which currently must be ``"button"`` .

    - **callbackOverrides** *(dict) --*

      An optional Lambda function to invoke instead of the default Lambda function provided by
      the placement template.

      - *(string) --*

        - *(string) --*
    """


_ClientUpdateProjectplacementTemplateTypeDef = TypedDict(
    "_ClientUpdateProjectplacementTemplateTypeDef",
    {
        "defaultAttributes": Dict[str, str],
        "deviceTemplates": Dict[
            str, ClientUpdateProjectplacementTemplatedeviceTemplatesTypeDef
        ],
    },
    total=False,
)


class ClientUpdateProjectplacementTemplateTypeDef(
    _ClientUpdateProjectplacementTemplateTypeDef
):
    """
    Type definition for `ClientUpdateProject` `placementTemplate`

    An object defining the project update. Once a project has been created, you cannot add device
    template names to the project. However, for a given ``placementTemplate`` , you can update the
    associated ``callbackOverrides`` for the device definition using this API.

    - **defaultAttributes** *(dict) --*

      The default attributes (key/value pairs) to be applied to all placements using this template.

      - *(string) --*

        - *(string) --*

    - **deviceTemplates** *(dict) --*

      An object specifying the  DeviceTemplate for all placements using this ( PlacementTemplate )
      template.

      - *(string) --*

        - *(dict) --*

          An object representing a device for a placement template (see  PlacementTemplate ).

          - **deviceType** *(string) --*

            The device type, which currently must be ``"button"`` .

          - **callbackOverrides** *(dict) --*

            An optional Lambda function to invoke instead of the default Lambda function provided by
            the placement template.

            - *(string) --*

              - *(string) --*
    """


_ListPlacementsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListPlacementsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListPlacementsPaginatePaginationConfigTypeDef(
    _ListPlacementsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListPlacementsPaginate` `PaginationConfig`

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


_ListPlacementsPaginateResponseplacementsTypeDef = TypedDict(
    "_ListPlacementsPaginateResponseplacementsTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
    },
    total=False,
)


class ListPlacementsPaginateResponseplacementsTypeDef(
    _ListPlacementsPaginateResponseplacementsTypeDef
):
    """
    Type definition for `ListPlacementsPaginateResponse` `placements`

    An object providing summary information for a particular placement.

    - **projectName** *(string) --*

      The name of the project containing the placement.

    - **placementName** *(string) --*

      The name of the placement being summarized.

    - **createdDate** *(datetime) --*

      The date when the placement was originally created, in UNIX epoch time format.

    - **updatedDate** *(datetime) --*

      The date when the placement was last updated, in UNIX epoch time format. If the placement
      was not updated, then ``createdDate`` and ``updatedDate`` are the same.
    """


_ListPlacementsPaginateResponseTypeDef = TypedDict(
    "_ListPlacementsPaginateResponseTypeDef",
    {
        "placements": List[ListPlacementsPaginateResponseplacementsTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ListPlacementsPaginateResponseTypeDef(_ListPlacementsPaginateResponseTypeDef):
    """
    Type definition for `ListPlacementsPaginate` `Response`

    - **placements** *(list) --*

      An object listing the requested placements.

      - *(dict) --*

        An object providing summary information for a particular placement.

        - **projectName** *(string) --*

          The name of the project containing the placement.

        - **placementName** *(string) --*

          The name of the placement being summarized.

        - **createdDate** *(datetime) --*

          The date when the placement was originally created, in UNIX epoch time format.

        - **updatedDate** *(datetime) --*

          The date when the placement was last updated, in UNIX epoch time format. If the placement
          was not updated, then ``createdDate`` and ``updatedDate`` are the same.

    - **NextToken** *(string) --*

      A token to resume pagination.
    """


_ListProjectsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListProjectsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListProjectsPaginatePaginationConfigTypeDef(
    _ListProjectsPaginatePaginationConfigTypeDef
):
    """
    Type definition for `ListProjectsPaginate` `PaginationConfig`

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


_ListProjectsPaginateResponseprojectsTypeDef = TypedDict(
    "_ListProjectsPaginateResponseprojectsTypeDef",
    {
        "arn": str,
        "projectName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ListProjectsPaginateResponseprojectsTypeDef(
    _ListProjectsPaginateResponseprojectsTypeDef
):
    """
    Type definition for `ListProjectsPaginateResponse` `projects`

    An object providing summary information for a particular project for an associated AWS
    account and region.

    - **arn** *(string) --*

      The ARN of the project.

    - **projectName** *(string) --*

      The name of the project being summarized.

    - **createdDate** *(datetime) --*

      The date when the project was originally created, in UNIX epoch time format.

    - **updatedDate** *(datetime) --*

      The date when the project was last updated, in UNIX epoch time format. If the project was
      not updated, then ``createdDate`` and ``updatedDate`` are the same.

    - **tags** *(dict) --*

      The tags (metadata key/value pairs) associated with the project.

      - *(string) --*

        - *(string) --*
    """


_ListProjectsPaginateResponseTypeDef = TypedDict(
    "_ListProjectsPaginateResponseTypeDef",
    {"projects": List[ListProjectsPaginateResponseprojectsTypeDef], "NextToken": str},
    total=False,
)


class ListProjectsPaginateResponseTypeDef(_ListProjectsPaginateResponseTypeDef):
    """
    Type definition for `ListProjectsPaginate` `Response`

    - **projects** *(list) --*

      An object containing the list of projects.

      - *(dict) --*

        An object providing summary information for a particular project for an associated AWS
        account and region.

        - **arn** *(string) --*

          The ARN of the project.

        - **projectName** *(string) --*

          The name of the project being summarized.

        - **createdDate** *(datetime) --*

          The date when the project was originally created, in UNIX epoch time format.

        - **updatedDate** *(datetime) --*

          The date when the project was last updated, in UNIX epoch time format. If the project was
          not updated, then ``createdDate`` and ``updatedDate`` are the same.

        - **tags** *(dict) --*

          The tags (metadata key/value pairs) associated with the project.

          - *(string) --*

            - *(string) --*

    - **NextToken** *(string) --*

      A token to resume pagination.
    """

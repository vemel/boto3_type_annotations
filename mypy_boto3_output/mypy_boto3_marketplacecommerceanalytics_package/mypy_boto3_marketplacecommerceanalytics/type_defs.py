"Main interface for marketplacecommerceanalytics type defs"
from __future__ import annotations

from typing_extensions import TypedDict


__all__ = (
    "ClientGenerateDataSetResponseTypeDef",
    "ClientStartSupportDataExportResponseTypeDef",
)


_ClientGenerateDataSetResponseTypeDef = TypedDict(
    "_ClientGenerateDataSetResponseTypeDef", {"dataSetRequestId": str}, total=False
)


class ClientGenerateDataSetResponseTypeDef(_ClientGenerateDataSetResponseTypeDef):
    """
    Type definition for `ClientGenerateDataSet` `Response`

    - **dataSetRequestId** *(string) --* A unique identifier representing a specific request to the
    GenerateDataSet operation. This identifier can be used to correlate a request with
    notifications from the SNS topic.
    """


_ClientStartSupportDataExportResponseTypeDef = TypedDict(
    "_ClientStartSupportDataExportResponseTypeDef",
    {"dataSetRequestId": str},
    total=False,
)


class ClientStartSupportDataExportResponseTypeDef(
    _ClientStartSupportDataExportResponseTypeDef
):
    """
    Type definition for `ClientStartSupportDataExport` `Response`

    - **dataSetRequestId** *(string) --* A unique identifier representing a specific request to the
    StartSupportDataExport operation. This identifier can be used to correlate a request with
    notifications from the SNS topic.
    """

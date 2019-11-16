"Main interface for textract type defs"
from __future__ import annotations

from typing import List
from typing_extensions import TypedDict


__all__ = (
    "ClientAnalyzeDocumentDocumentS3ObjectTypeDef",
    "ClientAnalyzeDocumentDocumentTypeDef",
    "ClientAnalyzeDocumentResponseBlocksGeometryBoundingBoxTypeDef",
    "ClientAnalyzeDocumentResponseBlocksGeometryPolygonTypeDef",
    "ClientAnalyzeDocumentResponseBlocksGeometryTypeDef",
    "ClientAnalyzeDocumentResponseBlocksRelationshipsTypeDef",
    "ClientAnalyzeDocumentResponseBlocksTypeDef",
    "ClientAnalyzeDocumentResponseDocumentMetadataTypeDef",
    "ClientAnalyzeDocumentResponseTypeDef",
    "ClientDetectDocumentTextDocumentS3ObjectTypeDef",
    "ClientDetectDocumentTextDocumentTypeDef",
    "ClientDetectDocumentTextResponseBlocksGeometryBoundingBoxTypeDef",
    "ClientDetectDocumentTextResponseBlocksGeometryPolygonTypeDef",
    "ClientDetectDocumentTextResponseBlocksGeometryTypeDef",
    "ClientDetectDocumentTextResponseBlocksRelationshipsTypeDef",
    "ClientDetectDocumentTextResponseBlocksTypeDef",
    "ClientDetectDocumentTextResponseDocumentMetadataTypeDef",
    "ClientDetectDocumentTextResponseTypeDef",
    "ClientGetDocumentAnalysisResponseBlocksGeometryBoundingBoxTypeDef",
    "ClientGetDocumentAnalysisResponseBlocksGeometryPolygonTypeDef",
    "ClientGetDocumentAnalysisResponseBlocksGeometryTypeDef",
    "ClientGetDocumentAnalysisResponseBlocksRelationshipsTypeDef",
    "ClientGetDocumentAnalysisResponseBlocksTypeDef",
    "ClientGetDocumentAnalysisResponseDocumentMetadataTypeDef",
    "ClientGetDocumentAnalysisResponseWarningsTypeDef",
    "ClientGetDocumentAnalysisResponseTypeDef",
    "ClientGetDocumentTextDetectionResponseBlocksGeometryBoundingBoxTypeDef",
    "ClientGetDocumentTextDetectionResponseBlocksGeometryPolygonTypeDef",
    "ClientGetDocumentTextDetectionResponseBlocksGeometryTypeDef",
    "ClientGetDocumentTextDetectionResponseBlocksRelationshipsTypeDef",
    "ClientGetDocumentTextDetectionResponseBlocksTypeDef",
    "ClientGetDocumentTextDetectionResponseDocumentMetadataTypeDef",
    "ClientGetDocumentTextDetectionResponseWarningsTypeDef",
    "ClientGetDocumentTextDetectionResponseTypeDef",
    "ClientStartDocumentAnalysisDocumentLocationS3ObjectTypeDef",
    "ClientStartDocumentAnalysisDocumentLocationTypeDef",
    "ClientStartDocumentAnalysisNotificationChannelTypeDef",
    "ClientStartDocumentAnalysisResponseTypeDef",
    "ClientStartDocumentTextDetectionDocumentLocationS3ObjectTypeDef",
    "ClientStartDocumentTextDetectionDocumentLocationTypeDef",
    "ClientStartDocumentTextDetectionNotificationChannelTypeDef",
    "ClientStartDocumentTextDetectionResponseTypeDef",
)


_ClientAnalyzeDocumentDocumentS3ObjectTypeDef = TypedDict(
    "_ClientAnalyzeDocumentDocumentS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientAnalyzeDocumentDocumentS3ObjectTypeDef(
    _ClientAnalyzeDocumentDocumentS3ObjectTypeDef
):
    """
    Type definition for `ClientAnalyzeDocumentDocument` `S3Object`

    Identifies an S3 object as the document source. The maximum size of a document stored in an S3
    bucket is 5 MB.

    - **Bucket** *(string) --*

      The name of the S3 bucket.

    - **Name** *(string) --*

      The file name of the input document. It must be an image file (.JPG or .PNG format).
      Asynchronous operations also support PDF files.

    - **Version** *(string) --*

      If the bucket has versioning enabled, you can specify the object version.
    """


_ClientAnalyzeDocumentDocumentTypeDef = TypedDict(
    "_ClientAnalyzeDocumentDocumentTypeDef",
    {"Bytes": bytes, "S3Object": ClientAnalyzeDocumentDocumentS3ObjectTypeDef},
    total=False,
)


class ClientAnalyzeDocumentDocumentTypeDef(_ClientAnalyzeDocumentDocumentTypeDef):
    """
    Type definition for `ClientAnalyzeDocument` `Document`

    The input document as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call
    Amazon Textract operations, you can't pass image bytes. The document must be an image in JPG or
    PNG format.

    If you are using an AWS SDK to call Amazon Textract, you might not need to base64-encode image
    bytes passed using the ``Bytes`` field.

    - **Bytes** *(bytes) --*

      A blob of base-64 encoded documents bytes. The maximum size of a document that's provided in a
      blob of bytes is 5 MB. The document bytes must be in PNG or JPG format.

      If you are using an AWS SDK to call Amazon Textract, you might not need to base64-encode image
      bytes passed using the ``Bytes`` field.

    - **S3Object** *(dict) --*

      Identifies an S3 object as the document source. The maximum size of a document stored in an S3
      bucket is 5 MB.

      - **Bucket** *(string) --*

        The name of the S3 bucket.

      - **Name** *(string) --*

        The file name of the input document. It must be an image file (.JPG or .PNG format).
        Asynchronous operations also support PDF files.

      - **Version** *(string) --*

        If the bucket has versioning enabled, you can specify the object version.
    """


_ClientAnalyzeDocumentResponseBlocksGeometryBoundingBoxTypeDef = TypedDict(
    "_ClientAnalyzeDocumentResponseBlocksGeometryBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientAnalyzeDocumentResponseBlocksGeometryBoundingBoxTypeDef(
    _ClientAnalyzeDocumentResponseBlocksGeometryBoundingBoxTypeDef
):
    """
    Type definition for `ClientAnalyzeDocumentResponseBlocksGeometry` `BoundingBox`

    An axis-aligned coarse representation of the location of the recognized text on the
    document page.

    - **Width** *(float) --*

      The width of the bounding box as a ratio of the overall document page width.

    - **Height** *(float) --*

      The height of the bounding box as a ratio of the overall document page height.

    - **Left** *(float) --*

      The left coordinate of the bounding box as a ratio of overall document page width.

    - **Top** *(float) --*

      The top coordinate of the bounding box as a ratio of overall document page height.
    """


_ClientAnalyzeDocumentResponseBlocksGeometryPolygonTypeDef = TypedDict(
    "_ClientAnalyzeDocumentResponseBlocksGeometryPolygonTypeDef",
    {"X": float, "Y": float},
    total=False,
)


class ClientAnalyzeDocumentResponseBlocksGeometryPolygonTypeDef(
    _ClientAnalyzeDocumentResponseBlocksGeometryPolygonTypeDef
):
    """
    Type definition for `ClientAnalyzeDocumentResponseBlocksGeometry` `Polygon`

    The X and Y coordinates of a point on a document page. The X and Y values returned
    are ratios of the overall document page size. For example, if the input document is
    700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the
    (350,50) pixel coordinate on the document page.

    An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText .
    ``Polygon`` represents a fine-grained polygon around detected text. For more
    information, see Geometry in the Amazon Textract Developer Guide.

    - **X** *(float) --*

      The value of the X coordinate for a point on a ``Polygon`` .

    - **Y** *(float) --*

      The value of the Y coordinate for a point on a ``Polygon`` .
    """


_ClientAnalyzeDocumentResponseBlocksGeometryTypeDef = TypedDict(
    "_ClientAnalyzeDocumentResponseBlocksGeometryTypeDef",
    {
        "BoundingBox": ClientAnalyzeDocumentResponseBlocksGeometryBoundingBoxTypeDef,
        "Polygon": List[ClientAnalyzeDocumentResponseBlocksGeometryPolygonTypeDef],
    },
    total=False,
)


class ClientAnalyzeDocumentResponseBlocksGeometryTypeDef(
    _ClientAnalyzeDocumentResponseBlocksGeometryTypeDef
):
    """
    Type definition for `ClientAnalyzeDocumentResponseBlocks` `Geometry`

    The location of the recognized text on the image. It includes an axis-aligned, coarse
    bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial
    information.

    - **BoundingBox** *(dict) --*

      An axis-aligned coarse representation of the location of the recognized text on the
      document page.

      - **Width** *(float) --*

        The width of the bounding box as a ratio of the overall document page width.

      - **Height** *(float) --*

        The height of the bounding box as a ratio of the overall document page height.

      - **Left** *(float) --*

        The left coordinate of the bounding box as a ratio of overall document page width.

      - **Top** *(float) --*

        The top coordinate of the bounding box as a ratio of overall document page height.

    - **Polygon** *(list) --*

      Within the bounding box, a fine-grained polygon around the recognized text.

      - *(dict) --*

        The X and Y coordinates of a point on a document page. The X and Y values returned
        are ratios of the overall document page size. For example, if the input document is
        700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the
        (350,50) pixel coordinate on the document page.

        An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText .
        ``Polygon`` represents a fine-grained polygon around detected text. For more
        information, see Geometry in the Amazon Textract Developer Guide.

        - **X** *(float) --*

          The value of the X coordinate for a point on a ``Polygon`` .

        - **Y** *(float) --*

          The value of the Y coordinate for a point on a ``Polygon`` .
    """


_ClientAnalyzeDocumentResponseBlocksRelationshipsTypeDef = TypedDict(
    "_ClientAnalyzeDocumentResponseBlocksRelationshipsTypeDef",
    {"Type": str, "Ids": List[str]},
    total=False,
)


class ClientAnalyzeDocumentResponseBlocksRelationshipsTypeDef(
    _ClientAnalyzeDocumentResponseBlocksRelationshipsTypeDef
):
    """
    Type definition for `ClientAnalyzeDocumentResponseBlocks` `Relationships`

    Information about how blocks are related to each other. A ``Block`` object contains 0
    or more ``Relation`` objects in a list, ``Relationships`` . For more information, see
    Block .

    The ``Type`` element provides the type of the relationship for all blocks in the
    ``IDs`` array.

    - **Type** *(string) --*

      The type of relationship that the blocks in the IDs array have with the current
      block. The relationship can be ``VALUE`` or ``CHILD`` .

    - **Ids** *(list) --*

      An array of IDs for related blocks. You can get the type of the relationship from the
      ``Type`` element.

      - *(string) --*
    """


_ClientAnalyzeDocumentResponseBlocksTypeDef = TypedDict(
    "_ClientAnalyzeDocumentResponseBlocksTypeDef",
    {
        "BlockType": str,
        "Confidence": float,
        "Text": str,
        "RowIndex": int,
        "ColumnIndex": int,
        "RowSpan": int,
        "ColumnSpan": int,
        "Geometry": ClientAnalyzeDocumentResponseBlocksGeometryTypeDef,
        "Id": str,
        "Relationships": List[ClientAnalyzeDocumentResponseBlocksRelationshipsTypeDef],
        "EntityTypes": List[str],
        "SelectionStatus": str,
        "Page": int,
    },
    total=False,
)


class ClientAnalyzeDocumentResponseBlocksTypeDef(
    _ClientAnalyzeDocumentResponseBlocksTypeDef
):
    """
    Type definition for `ClientAnalyzeDocumentResponse` `Blocks`

    A ``Block`` represents items that are recognized in a document within a group of pixels
    close to each other. The information returned in a ``Block`` depends on the type of
    operation. In document-text detection (for example  DetectDocumentText ), you get
    information about the detected words and lines of text. In text analysis (for example
    AnalyzeDocument ), you can also get information about the fields, tables and selection
    elements that are detected in the document.

    An array of ``Block`` objects is returned by both synchronous and asynchronous operations.
    In synchronous operations, such as  DetectDocumentText , the array of ``Block`` objects is
    the entire set of results. In asynchronous operations, such as  GetDocumentAnalysis , the
    array is returned over one or more responses.

    For more information, see `How Amazon Textract Works
    <https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html>`__ .

    - **BlockType** *(string) --*

      The type of text that's recognized in a block. In text-detection operations, the
      following types are returned:

      * *PAGE* - Contains a list of the LINE Block objects that are detected on a document page.

      * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin
      script characters that aren't separated by spaces.

      * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page.

      In text analysis operations, the following types are returned:

      * *PAGE* - Contains a list of child Block objects that are detected on a document page.

      * *KEY_VALUE_SET* - Stores the KEY and VALUE Block objects for a field that's detected on
      a document page. Use the ``EntityType`` field to determine if a KEY_VALUE_SET object is a
      KEY Block object or a VALUE Block object.

      * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin
      script characters that aren't separated by spaces that's detected on a document page.

      * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page.

      * *TABLE* - A table that's detected on a document page. A table is any grid-based
      information with 2 or more rows or columns with a cell span of 1 row and 1 column each.

      * *CELL* - A cell within a detected table. The cell is the parent of the block that
      contains the text in the cell.

      * *SELECTION_ELEMENT* - A selectable element such as a radio button or checkbox that's
      detected on a document page. Use the value of ``SelectionStatus`` to determine the status
      of the selection element.

    - **Confidence** *(float) --*

      The confidence that Amazon Textract has in the accuracy of the recognized text and the
      accuracy of the geometry points around the recognized text.

    - **Text** *(string) --*

      The word or line of text that's recognized by Amazon Textract.

    - **RowIndex** *(integer) --*

      The row in which a table cell is located. The first row position is 1. ``RowIndex`` isn't
      returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

    - **ColumnIndex** *(integer) --*

      The column in which a table cell appears. The first column position is 1. ``ColumnIndex``
      isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

    - **RowSpan** *(integer) --*

      The number of rows that a table spans. ``RowSpan`` isn't returned by
      ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

    - **ColumnSpan** *(integer) --*

      The number of columns that a table cell spans. ``ColumnSpan`` isn't returned by
      ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

    - **Geometry** *(dict) --*

      The location of the recognized text on the image. It includes an axis-aligned, coarse
      bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial
      information.

      - **BoundingBox** *(dict) --*

        An axis-aligned coarse representation of the location of the recognized text on the
        document page.

        - **Width** *(float) --*

          The width of the bounding box as a ratio of the overall document page width.

        - **Height** *(float) --*

          The height of the bounding box as a ratio of the overall document page height.

        - **Left** *(float) --*

          The left coordinate of the bounding box as a ratio of overall document page width.

        - **Top** *(float) --*

          The top coordinate of the bounding box as a ratio of overall document page height.

      - **Polygon** *(list) --*

        Within the bounding box, a fine-grained polygon around the recognized text.

        - *(dict) --*

          The X and Y coordinates of a point on a document page. The X and Y values returned
          are ratios of the overall document page size. For example, if the input document is
          700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the
          (350,50) pixel coordinate on the document page.

          An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText .
          ``Polygon`` represents a fine-grained polygon around detected text. For more
          information, see Geometry in the Amazon Textract Developer Guide.

          - **X** *(float) --*

            The value of the X coordinate for a point on a ``Polygon`` .

          - **Y** *(float) --*

            The value of the Y coordinate for a point on a ``Polygon`` .

    - **Id** *(string) --*

      The identifier for the recognized text. The identifier is only unique for a single
      operation.

    - **Relationships** *(list) --*

      A list of child blocks of the current block. For example a LINE object has child blocks
      for each WORD block that's part of the line of text. There aren't Relationship objects in
      the list for relationships that don't exist, such as when the current block has no child
      blocks. The list size can be the following:

      * 0 - The block has no child blocks.

      * 1 - The block has child blocks.

      - *(dict) --*

        Information about how blocks are related to each other. A ``Block`` object contains 0
        or more ``Relation`` objects in a list, ``Relationships`` . For more information, see
        Block .

        The ``Type`` element provides the type of the relationship for all blocks in the
        ``IDs`` array.

        - **Type** *(string) --*

          The type of relationship that the blocks in the IDs array have with the current
          block. The relationship can be ``VALUE`` or ``CHILD`` .

        - **Ids** *(list) --*

          An array of IDs for related blocks. You can get the type of the relationship from the
          ``Type`` element.

          - *(string) --*

    - **EntityTypes** *(list) --*

      The type of entity. The following can be returned:

      * *KEY* - An identifier for a field on the document.

      * *VALUE* - The field text.

       ``EntityTypes`` isn't returned by ``DetectDocumentText`` and
       ``GetDocumentTextDetection`` .

      - *(string) --*

    - **SelectionStatus** *(string) --*

      The selection status of a selectable element such as a radio button or checkbox.

    - **Page** *(integer) --*

      The page in which a block was detected. ``Page`` is returned by asynchronous operations.
      Page values greater than 1 are only returned for multi-page documents that are in PDF
      format. A scanned image (JPG/PNG), even if it contains multiple document pages, is always
      considered to be a single-page document and the value of ``Page`` is always 1.
      Synchronous operations don't return ``Page`` as every input document is considered to be
      a single-page document.
    """


_ClientAnalyzeDocumentResponseDocumentMetadataTypeDef = TypedDict(
    "_ClientAnalyzeDocumentResponseDocumentMetadataTypeDef", {"Pages": int}, total=False
)


class ClientAnalyzeDocumentResponseDocumentMetadataTypeDef(
    _ClientAnalyzeDocumentResponseDocumentMetadataTypeDef
):
    """
    Type definition for `ClientAnalyzeDocumentResponse` `DocumentMetadata`

    Metadata about the analyzed document. An example is the number of pages.

    - **Pages** *(integer) --*

      The number of pages detected in the document.
    """


_ClientAnalyzeDocumentResponseTypeDef = TypedDict(
    "_ClientAnalyzeDocumentResponseTypeDef",
    {
        "DocumentMetadata": ClientAnalyzeDocumentResponseDocumentMetadataTypeDef,
        "Blocks": List[ClientAnalyzeDocumentResponseBlocksTypeDef],
    },
    total=False,
)


class ClientAnalyzeDocumentResponseTypeDef(_ClientAnalyzeDocumentResponseTypeDef):
    """
    Type definition for `ClientAnalyzeDocument` `Response`

    - **DocumentMetadata** *(dict) --*

      Metadata about the analyzed document. An example is the number of pages.

      - **Pages** *(integer) --*

        The number of pages detected in the document.

    - **Blocks** *(list) --*

      The text that's detected and analyzed by ``AnalyzeDocument`` .

      - *(dict) --*

        A ``Block`` represents items that are recognized in a document within a group of pixels
        close to each other. The information returned in a ``Block`` depends on the type of
        operation. In document-text detection (for example  DetectDocumentText ), you get
        information about the detected words and lines of text. In text analysis (for example
        AnalyzeDocument ), you can also get information about the fields, tables and selection
        elements that are detected in the document.

        An array of ``Block`` objects is returned by both synchronous and asynchronous operations.
        In synchronous operations, such as  DetectDocumentText , the array of ``Block`` objects is
        the entire set of results. In asynchronous operations, such as  GetDocumentAnalysis , the
        array is returned over one or more responses.

        For more information, see `How Amazon Textract Works
        <https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html>`__ .

        - **BlockType** *(string) --*

          The type of text that's recognized in a block. In text-detection operations, the
          following types are returned:

          * *PAGE* - Contains a list of the LINE Block objects that are detected on a document page.

          * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin
          script characters that aren't separated by spaces.

          * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page.

          In text analysis operations, the following types are returned:

          * *PAGE* - Contains a list of child Block objects that are detected on a document page.

          * *KEY_VALUE_SET* - Stores the KEY and VALUE Block objects for a field that's detected on
          a document page. Use the ``EntityType`` field to determine if a KEY_VALUE_SET object is a
          KEY Block object or a VALUE Block object.

          * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin
          script characters that aren't separated by spaces that's detected on a document page.

          * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page.

          * *TABLE* - A table that's detected on a document page. A table is any grid-based
          information with 2 or more rows or columns with a cell span of 1 row and 1 column each.

          * *CELL* - A cell within a detected table. The cell is the parent of the block that
          contains the text in the cell.

          * *SELECTION_ELEMENT* - A selectable element such as a radio button or checkbox that's
          detected on a document page. Use the value of ``SelectionStatus`` to determine the status
          of the selection element.

        - **Confidence** *(float) --*

          The confidence that Amazon Textract has in the accuracy of the recognized text and the
          accuracy of the geometry points around the recognized text.

        - **Text** *(string) --*

          The word or line of text that's recognized by Amazon Textract.

        - **RowIndex** *(integer) --*

          The row in which a table cell is located. The first row position is 1. ``RowIndex`` isn't
          returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

        - **ColumnIndex** *(integer) --*

          The column in which a table cell appears. The first column position is 1. ``ColumnIndex``
          isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

        - **RowSpan** *(integer) --*

          The number of rows that a table spans. ``RowSpan`` isn't returned by
          ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

        - **ColumnSpan** *(integer) --*

          The number of columns that a table cell spans. ``ColumnSpan`` isn't returned by
          ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

        - **Geometry** *(dict) --*

          The location of the recognized text on the image. It includes an axis-aligned, coarse
          bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial
          information.

          - **BoundingBox** *(dict) --*

            An axis-aligned coarse representation of the location of the recognized text on the
            document page.

            - **Width** *(float) --*

              The width of the bounding box as a ratio of the overall document page width.

            - **Height** *(float) --*

              The height of the bounding box as a ratio of the overall document page height.

            - **Left** *(float) --*

              The left coordinate of the bounding box as a ratio of overall document page width.

            - **Top** *(float) --*

              The top coordinate of the bounding box as a ratio of overall document page height.

          - **Polygon** *(list) --*

            Within the bounding box, a fine-grained polygon around the recognized text.

            - *(dict) --*

              The X and Y coordinates of a point on a document page. The X and Y values returned
              are ratios of the overall document page size. For example, if the input document is
              700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the
              (350,50) pixel coordinate on the document page.

              An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText .
              ``Polygon`` represents a fine-grained polygon around detected text. For more
              information, see Geometry in the Amazon Textract Developer Guide.

              - **X** *(float) --*

                The value of the X coordinate for a point on a ``Polygon`` .

              - **Y** *(float) --*

                The value of the Y coordinate for a point on a ``Polygon`` .

        - **Id** *(string) --*

          The identifier for the recognized text. The identifier is only unique for a single
          operation.

        - **Relationships** *(list) --*

          A list of child blocks of the current block. For example a LINE object has child blocks
          for each WORD block that's part of the line of text. There aren't Relationship objects in
          the list for relationships that don't exist, such as when the current block has no child
          blocks. The list size can be the following:

          * 0 - The block has no child blocks.

          * 1 - The block has child blocks.

          - *(dict) --*

            Information about how blocks are related to each other. A ``Block`` object contains 0
            or more ``Relation`` objects in a list, ``Relationships`` . For more information, see
            Block .

            The ``Type`` element provides the type of the relationship for all blocks in the
            ``IDs`` array.

            - **Type** *(string) --*

              The type of relationship that the blocks in the IDs array have with the current
              block. The relationship can be ``VALUE`` or ``CHILD`` .

            - **Ids** *(list) --*

              An array of IDs for related blocks. You can get the type of the relationship from the
              ``Type`` element.

              - *(string) --*

        - **EntityTypes** *(list) --*

          The type of entity. The following can be returned:

          * *KEY* - An identifier for a field on the document.

          * *VALUE* - The field text.

           ``EntityTypes`` isn't returned by ``DetectDocumentText`` and
           ``GetDocumentTextDetection`` .

          - *(string) --*

        - **SelectionStatus** *(string) --*

          The selection status of a selectable element such as a radio button or checkbox.

        - **Page** *(integer) --*

          The page in which a block was detected. ``Page`` is returned by asynchronous operations.
          Page values greater than 1 are only returned for multi-page documents that are in PDF
          format. A scanned image (JPG/PNG), even if it contains multiple document pages, is always
          considered to be a single-page document and the value of ``Page`` is always 1.
          Synchronous operations don't return ``Page`` as every input document is considered to be
          a single-page document.
    """


_ClientDetectDocumentTextDocumentS3ObjectTypeDef = TypedDict(
    "_ClientDetectDocumentTextDocumentS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientDetectDocumentTextDocumentS3ObjectTypeDef(
    _ClientDetectDocumentTextDocumentS3ObjectTypeDef
):
    """
    Type definition for `ClientDetectDocumentTextDocument` `S3Object`

    Identifies an S3 object as the document source. The maximum size of a document stored in an S3
    bucket is 5 MB.

    - **Bucket** *(string) --*

      The name of the S3 bucket.

    - **Name** *(string) --*

      The file name of the input document. It must be an image file (.JPG or .PNG format).
      Asynchronous operations also support PDF files.

    - **Version** *(string) --*

      If the bucket has versioning enabled, you can specify the object version.
    """


_ClientDetectDocumentTextDocumentTypeDef = TypedDict(
    "_ClientDetectDocumentTextDocumentTypeDef",
    {"Bytes": bytes, "S3Object": ClientDetectDocumentTextDocumentS3ObjectTypeDef},
    total=False,
)


class ClientDetectDocumentTextDocumentTypeDef(_ClientDetectDocumentTextDocumentTypeDef):
    """
    Type definition for `ClientDetectDocumentText` `Document`

    The input document as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call
    Amazon Textract operations, you can't pass image bytes. The document must be an image in JPG or
    PNG format.

    If you are using an AWS SDK to call Amazon Textract, you might not need to base64-encode image
    bytes passed using the ``Bytes`` field.

    - **Bytes** *(bytes) --*

      A blob of base-64 encoded documents bytes. The maximum size of a document that's provided in a
      blob of bytes is 5 MB. The document bytes must be in PNG or JPG format.

      If you are using an AWS SDK to call Amazon Textract, you might not need to base64-encode image
      bytes passed using the ``Bytes`` field.

    - **S3Object** *(dict) --*

      Identifies an S3 object as the document source. The maximum size of a document stored in an S3
      bucket is 5 MB.

      - **Bucket** *(string) --*

        The name of the S3 bucket.

      - **Name** *(string) --*

        The file name of the input document. It must be an image file (.JPG or .PNG format).
        Asynchronous operations also support PDF files.

      - **Version** *(string) --*

        If the bucket has versioning enabled, you can specify the object version.
    """


_ClientDetectDocumentTextResponseBlocksGeometryBoundingBoxTypeDef = TypedDict(
    "_ClientDetectDocumentTextResponseBlocksGeometryBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientDetectDocumentTextResponseBlocksGeometryBoundingBoxTypeDef(
    _ClientDetectDocumentTextResponseBlocksGeometryBoundingBoxTypeDef
):
    """
    Type definition for `ClientDetectDocumentTextResponseBlocksGeometry` `BoundingBox`

    An axis-aligned coarse representation of the location of the recognized text on the
    document page.

    - **Width** *(float) --*

      The width of the bounding box as a ratio of the overall document page width.

    - **Height** *(float) --*

      The height of the bounding box as a ratio of the overall document page height.

    - **Left** *(float) --*

      The left coordinate of the bounding box as a ratio of overall document page width.

    - **Top** *(float) --*

      The top coordinate of the bounding box as a ratio of overall document page height.
    """


_ClientDetectDocumentTextResponseBlocksGeometryPolygonTypeDef = TypedDict(
    "_ClientDetectDocumentTextResponseBlocksGeometryPolygonTypeDef",
    {"X": float, "Y": float},
    total=False,
)


class ClientDetectDocumentTextResponseBlocksGeometryPolygonTypeDef(
    _ClientDetectDocumentTextResponseBlocksGeometryPolygonTypeDef
):
    """
    Type definition for `ClientDetectDocumentTextResponseBlocksGeometry` `Polygon`

    The X and Y coordinates of a point on a document page. The X and Y values returned
    are ratios of the overall document page size. For example, if the input document is
    700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the
    (350,50) pixel coordinate on the document page.

    An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText .
    ``Polygon`` represents a fine-grained polygon around detected text. For more
    information, see Geometry in the Amazon Textract Developer Guide.

    - **X** *(float) --*

      The value of the X coordinate for a point on a ``Polygon`` .

    - **Y** *(float) --*

      The value of the Y coordinate for a point on a ``Polygon`` .
    """


_ClientDetectDocumentTextResponseBlocksGeometryTypeDef = TypedDict(
    "_ClientDetectDocumentTextResponseBlocksGeometryTypeDef",
    {
        "BoundingBox": ClientDetectDocumentTextResponseBlocksGeometryBoundingBoxTypeDef,
        "Polygon": List[ClientDetectDocumentTextResponseBlocksGeometryPolygonTypeDef],
    },
    total=False,
)


class ClientDetectDocumentTextResponseBlocksGeometryTypeDef(
    _ClientDetectDocumentTextResponseBlocksGeometryTypeDef
):
    """
    Type definition for `ClientDetectDocumentTextResponseBlocks` `Geometry`

    The location of the recognized text on the image. It includes an axis-aligned, coarse
    bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial
    information.

    - **BoundingBox** *(dict) --*

      An axis-aligned coarse representation of the location of the recognized text on the
      document page.

      - **Width** *(float) --*

        The width of the bounding box as a ratio of the overall document page width.

      - **Height** *(float) --*

        The height of the bounding box as a ratio of the overall document page height.

      - **Left** *(float) --*

        The left coordinate of the bounding box as a ratio of overall document page width.

      - **Top** *(float) --*

        The top coordinate of the bounding box as a ratio of overall document page height.

    - **Polygon** *(list) --*

      Within the bounding box, a fine-grained polygon around the recognized text.

      - *(dict) --*

        The X and Y coordinates of a point on a document page. The X and Y values returned
        are ratios of the overall document page size. For example, if the input document is
        700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the
        (350,50) pixel coordinate on the document page.

        An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText .
        ``Polygon`` represents a fine-grained polygon around detected text. For more
        information, see Geometry in the Amazon Textract Developer Guide.

        - **X** *(float) --*

          The value of the X coordinate for a point on a ``Polygon`` .

        - **Y** *(float) --*

          The value of the Y coordinate for a point on a ``Polygon`` .
    """


_ClientDetectDocumentTextResponseBlocksRelationshipsTypeDef = TypedDict(
    "_ClientDetectDocumentTextResponseBlocksRelationshipsTypeDef",
    {"Type": str, "Ids": List[str]},
    total=False,
)


class ClientDetectDocumentTextResponseBlocksRelationshipsTypeDef(
    _ClientDetectDocumentTextResponseBlocksRelationshipsTypeDef
):
    """
    Type definition for `ClientDetectDocumentTextResponseBlocks` `Relationships`

    Information about how blocks are related to each other. A ``Block`` object contains 0
    or more ``Relation`` objects in a list, ``Relationships`` . For more information, see
    Block .

    The ``Type`` element provides the type of the relationship for all blocks in the
    ``IDs`` array.

    - **Type** *(string) --*

      The type of relationship that the blocks in the IDs array have with the current
      block. The relationship can be ``VALUE`` or ``CHILD`` .

    - **Ids** *(list) --*

      An array of IDs for related blocks. You can get the type of the relationship from the
      ``Type`` element.

      - *(string) --*
    """


_ClientDetectDocumentTextResponseBlocksTypeDef = TypedDict(
    "_ClientDetectDocumentTextResponseBlocksTypeDef",
    {
        "BlockType": str,
        "Confidence": float,
        "Text": str,
        "RowIndex": int,
        "ColumnIndex": int,
        "RowSpan": int,
        "ColumnSpan": int,
        "Geometry": ClientDetectDocumentTextResponseBlocksGeometryTypeDef,
        "Id": str,
        "Relationships": List[
            ClientDetectDocumentTextResponseBlocksRelationshipsTypeDef
        ],
        "EntityTypes": List[str],
        "SelectionStatus": str,
        "Page": int,
    },
    total=False,
)


class ClientDetectDocumentTextResponseBlocksTypeDef(
    _ClientDetectDocumentTextResponseBlocksTypeDef
):
    """
    Type definition for `ClientDetectDocumentTextResponse` `Blocks`

    A ``Block`` represents items that are recognized in a document within a group of pixels
    close to each other. The information returned in a ``Block`` depends on the type of
    operation. In document-text detection (for example  DetectDocumentText ), you get
    information about the detected words and lines of text. In text analysis (for example
    AnalyzeDocument ), you can also get information about the fields, tables and selection
    elements that are detected in the document.

    An array of ``Block`` objects is returned by both synchronous and asynchronous operations.
    In synchronous operations, such as  DetectDocumentText , the array of ``Block`` objects is
    the entire set of results. In asynchronous operations, such as  GetDocumentAnalysis , the
    array is returned over one or more responses.

    For more information, see `How Amazon Textract Works
    <https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html>`__ .

    - **BlockType** *(string) --*

      The type of text that's recognized in a block. In text-detection operations, the
      following types are returned:

      * *PAGE* - Contains a list of the LINE Block objects that are detected on a document page.

      * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin
      script characters that aren't separated by spaces.

      * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page.

      In text analysis operations, the following types are returned:

      * *PAGE* - Contains a list of child Block objects that are detected on a document page.

      * *KEY_VALUE_SET* - Stores the KEY and VALUE Block objects for a field that's detected on
      a document page. Use the ``EntityType`` field to determine if a KEY_VALUE_SET object is a
      KEY Block object or a VALUE Block object.

      * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin
      script characters that aren't separated by spaces that's detected on a document page.

      * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page.

      * *TABLE* - A table that's detected on a document page. A table is any grid-based
      information with 2 or more rows or columns with a cell span of 1 row and 1 column each.

      * *CELL* - A cell within a detected table. The cell is the parent of the block that
      contains the text in the cell.

      * *SELECTION_ELEMENT* - A selectable element such as a radio button or checkbox that's
      detected on a document page. Use the value of ``SelectionStatus`` to determine the status
      of the selection element.

    - **Confidence** *(float) --*

      The confidence that Amazon Textract has in the accuracy of the recognized text and the
      accuracy of the geometry points around the recognized text.

    - **Text** *(string) --*

      The word or line of text that's recognized by Amazon Textract.

    - **RowIndex** *(integer) --*

      The row in which a table cell is located. The first row position is 1. ``RowIndex`` isn't
      returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

    - **ColumnIndex** *(integer) --*

      The column in which a table cell appears. The first column position is 1. ``ColumnIndex``
      isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

    - **RowSpan** *(integer) --*

      The number of rows that a table spans. ``RowSpan`` isn't returned by
      ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

    - **ColumnSpan** *(integer) --*

      The number of columns that a table cell spans. ``ColumnSpan`` isn't returned by
      ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

    - **Geometry** *(dict) --*

      The location of the recognized text on the image. It includes an axis-aligned, coarse
      bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial
      information.

      - **BoundingBox** *(dict) --*

        An axis-aligned coarse representation of the location of the recognized text on the
        document page.

        - **Width** *(float) --*

          The width of the bounding box as a ratio of the overall document page width.

        - **Height** *(float) --*

          The height of the bounding box as a ratio of the overall document page height.

        - **Left** *(float) --*

          The left coordinate of the bounding box as a ratio of overall document page width.

        - **Top** *(float) --*

          The top coordinate of the bounding box as a ratio of overall document page height.

      - **Polygon** *(list) --*

        Within the bounding box, a fine-grained polygon around the recognized text.

        - *(dict) --*

          The X and Y coordinates of a point on a document page. The X and Y values returned
          are ratios of the overall document page size. For example, if the input document is
          700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the
          (350,50) pixel coordinate on the document page.

          An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText .
          ``Polygon`` represents a fine-grained polygon around detected text. For more
          information, see Geometry in the Amazon Textract Developer Guide.

          - **X** *(float) --*

            The value of the X coordinate for a point on a ``Polygon`` .

          - **Y** *(float) --*

            The value of the Y coordinate for a point on a ``Polygon`` .

    - **Id** *(string) --*

      The identifier for the recognized text. The identifier is only unique for a single
      operation.

    - **Relationships** *(list) --*

      A list of child blocks of the current block. For example a LINE object has child blocks
      for each WORD block that's part of the line of text. There aren't Relationship objects in
      the list for relationships that don't exist, such as when the current block has no child
      blocks. The list size can be the following:

      * 0 - The block has no child blocks.

      * 1 - The block has child blocks.

      - *(dict) --*

        Information about how blocks are related to each other. A ``Block`` object contains 0
        or more ``Relation`` objects in a list, ``Relationships`` . For more information, see
        Block .

        The ``Type`` element provides the type of the relationship for all blocks in the
        ``IDs`` array.

        - **Type** *(string) --*

          The type of relationship that the blocks in the IDs array have with the current
          block. The relationship can be ``VALUE`` or ``CHILD`` .

        - **Ids** *(list) --*

          An array of IDs for related blocks. You can get the type of the relationship from the
          ``Type`` element.

          - *(string) --*

    - **EntityTypes** *(list) --*

      The type of entity. The following can be returned:

      * *KEY* - An identifier for a field on the document.

      * *VALUE* - The field text.

       ``EntityTypes`` isn't returned by ``DetectDocumentText`` and
       ``GetDocumentTextDetection`` .

      - *(string) --*

    - **SelectionStatus** *(string) --*

      The selection status of a selectable element such as a radio button or checkbox.

    - **Page** *(integer) --*

      The page in which a block was detected. ``Page`` is returned by asynchronous operations.
      Page values greater than 1 are only returned for multi-page documents that are in PDF
      format. A scanned image (JPG/PNG), even if it contains multiple document pages, is always
      considered to be a single-page document and the value of ``Page`` is always 1.
      Synchronous operations don't return ``Page`` as every input document is considered to be
      a single-page document.
    """


_ClientDetectDocumentTextResponseDocumentMetadataTypeDef = TypedDict(
    "_ClientDetectDocumentTextResponseDocumentMetadataTypeDef",
    {"Pages": int},
    total=False,
)


class ClientDetectDocumentTextResponseDocumentMetadataTypeDef(
    _ClientDetectDocumentTextResponseDocumentMetadataTypeDef
):
    """
    Type definition for `ClientDetectDocumentTextResponse` `DocumentMetadata`

    Metadata about the document. Contains the number of pages that are detected in the document.

    - **Pages** *(integer) --*

      The number of pages detected in the document.
    """


_ClientDetectDocumentTextResponseTypeDef = TypedDict(
    "_ClientDetectDocumentTextResponseTypeDef",
    {
        "DocumentMetadata": ClientDetectDocumentTextResponseDocumentMetadataTypeDef,
        "Blocks": List[ClientDetectDocumentTextResponseBlocksTypeDef],
    },
    total=False,
)


class ClientDetectDocumentTextResponseTypeDef(_ClientDetectDocumentTextResponseTypeDef):
    """
    Type definition for `ClientDetectDocumentText` `Response`

    - **DocumentMetadata** *(dict) --*

      Metadata about the document. Contains the number of pages that are detected in the document.

      - **Pages** *(integer) --*

        The number of pages detected in the document.

    - **Blocks** *(list) --*

      An array of Block objects containing the text detected in the document.

      - *(dict) --*

        A ``Block`` represents items that are recognized in a document within a group of pixels
        close to each other. The information returned in a ``Block`` depends on the type of
        operation. In document-text detection (for example  DetectDocumentText ), you get
        information about the detected words and lines of text. In text analysis (for example
        AnalyzeDocument ), you can also get information about the fields, tables and selection
        elements that are detected in the document.

        An array of ``Block`` objects is returned by both synchronous and asynchronous operations.
        In synchronous operations, such as  DetectDocumentText , the array of ``Block`` objects is
        the entire set of results. In asynchronous operations, such as  GetDocumentAnalysis , the
        array is returned over one or more responses.

        For more information, see `How Amazon Textract Works
        <https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html>`__ .

        - **BlockType** *(string) --*

          The type of text that's recognized in a block. In text-detection operations, the
          following types are returned:

          * *PAGE* - Contains a list of the LINE Block objects that are detected on a document page.

          * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin
          script characters that aren't separated by spaces.

          * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page.

          In text analysis operations, the following types are returned:

          * *PAGE* - Contains a list of child Block objects that are detected on a document page.

          * *KEY_VALUE_SET* - Stores the KEY and VALUE Block objects for a field that's detected on
          a document page. Use the ``EntityType`` field to determine if a KEY_VALUE_SET object is a
          KEY Block object or a VALUE Block object.

          * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin
          script characters that aren't separated by spaces that's detected on a document page.

          * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page.

          * *TABLE* - A table that's detected on a document page. A table is any grid-based
          information with 2 or more rows or columns with a cell span of 1 row and 1 column each.

          * *CELL* - A cell within a detected table. The cell is the parent of the block that
          contains the text in the cell.

          * *SELECTION_ELEMENT* - A selectable element such as a radio button or checkbox that's
          detected on a document page. Use the value of ``SelectionStatus`` to determine the status
          of the selection element.

        - **Confidence** *(float) --*

          The confidence that Amazon Textract has in the accuracy of the recognized text and the
          accuracy of the geometry points around the recognized text.

        - **Text** *(string) --*

          The word or line of text that's recognized by Amazon Textract.

        - **RowIndex** *(integer) --*

          The row in which a table cell is located. The first row position is 1. ``RowIndex`` isn't
          returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

        - **ColumnIndex** *(integer) --*

          The column in which a table cell appears. The first column position is 1. ``ColumnIndex``
          isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

        - **RowSpan** *(integer) --*

          The number of rows that a table spans. ``RowSpan`` isn't returned by
          ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

        - **ColumnSpan** *(integer) --*

          The number of columns that a table cell spans. ``ColumnSpan`` isn't returned by
          ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

        - **Geometry** *(dict) --*

          The location of the recognized text on the image. It includes an axis-aligned, coarse
          bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial
          information.

          - **BoundingBox** *(dict) --*

            An axis-aligned coarse representation of the location of the recognized text on the
            document page.

            - **Width** *(float) --*

              The width of the bounding box as a ratio of the overall document page width.

            - **Height** *(float) --*

              The height of the bounding box as a ratio of the overall document page height.

            - **Left** *(float) --*

              The left coordinate of the bounding box as a ratio of overall document page width.

            - **Top** *(float) --*

              The top coordinate of the bounding box as a ratio of overall document page height.

          - **Polygon** *(list) --*

            Within the bounding box, a fine-grained polygon around the recognized text.

            - *(dict) --*

              The X and Y coordinates of a point on a document page. The X and Y values returned
              are ratios of the overall document page size. For example, if the input document is
              700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the
              (350,50) pixel coordinate on the document page.

              An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText .
              ``Polygon`` represents a fine-grained polygon around detected text. For more
              information, see Geometry in the Amazon Textract Developer Guide.

              - **X** *(float) --*

                The value of the X coordinate for a point on a ``Polygon`` .

              - **Y** *(float) --*

                The value of the Y coordinate for a point on a ``Polygon`` .

        - **Id** *(string) --*

          The identifier for the recognized text. The identifier is only unique for a single
          operation.

        - **Relationships** *(list) --*

          A list of child blocks of the current block. For example a LINE object has child blocks
          for each WORD block that's part of the line of text. There aren't Relationship objects in
          the list for relationships that don't exist, such as when the current block has no child
          blocks. The list size can be the following:

          * 0 - The block has no child blocks.

          * 1 - The block has child blocks.

          - *(dict) --*

            Information about how blocks are related to each other. A ``Block`` object contains 0
            or more ``Relation`` objects in a list, ``Relationships`` . For more information, see
            Block .

            The ``Type`` element provides the type of the relationship for all blocks in the
            ``IDs`` array.

            - **Type** *(string) --*

              The type of relationship that the blocks in the IDs array have with the current
              block. The relationship can be ``VALUE`` or ``CHILD`` .

            - **Ids** *(list) --*

              An array of IDs for related blocks. You can get the type of the relationship from the
              ``Type`` element.

              - *(string) --*

        - **EntityTypes** *(list) --*

          The type of entity. The following can be returned:

          * *KEY* - An identifier for a field on the document.

          * *VALUE* - The field text.

           ``EntityTypes`` isn't returned by ``DetectDocumentText`` and
           ``GetDocumentTextDetection`` .

          - *(string) --*

        - **SelectionStatus** *(string) --*

          The selection status of a selectable element such as a radio button or checkbox.

        - **Page** *(integer) --*

          The page in which a block was detected. ``Page`` is returned by asynchronous operations.
          Page values greater than 1 are only returned for multi-page documents that are in PDF
          format. A scanned image (JPG/PNG), even if it contains multiple document pages, is always
          considered to be a single-page document and the value of ``Page`` is always 1.
          Synchronous operations don't return ``Page`` as every input document is considered to be
          a single-page document.
    """


_ClientGetDocumentAnalysisResponseBlocksGeometryBoundingBoxTypeDef = TypedDict(
    "_ClientGetDocumentAnalysisResponseBlocksGeometryBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientGetDocumentAnalysisResponseBlocksGeometryBoundingBoxTypeDef(
    _ClientGetDocumentAnalysisResponseBlocksGeometryBoundingBoxTypeDef
):
    """
    Type definition for `ClientGetDocumentAnalysisResponseBlocksGeometry` `BoundingBox`

    An axis-aligned coarse representation of the location of the recognized text on the
    document page.

    - **Width** *(float) --*

      The width of the bounding box as a ratio of the overall document page width.

    - **Height** *(float) --*

      The height of the bounding box as a ratio of the overall document page height.

    - **Left** *(float) --*

      The left coordinate of the bounding box as a ratio of overall document page width.

    - **Top** *(float) --*

      The top coordinate of the bounding box as a ratio of overall document page height.
    """


_ClientGetDocumentAnalysisResponseBlocksGeometryPolygonTypeDef = TypedDict(
    "_ClientGetDocumentAnalysisResponseBlocksGeometryPolygonTypeDef",
    {"X": float, "Y": float},
    total=False,
)


class ClientGetDocumentAnalysisResponseBlocksGeometryPolygonTypeDef(
    _ClientGetDocumentAnalysisResponseBlocksGeometryPolygonTypeDef
):
    """
    Type definition for `ClientGetDocumentAnalysisResponseBlocksGeometry` `Polygon`

    The X and Y coordinates of a point on a document page. The X and Y values returned
    are ratios of the overall document page size. For example, if the input document is
    700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the
    (350,50) pixel coordinate on the document page.

    An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText .
    ``Polygon`` represents a fine-grained polygon around detected text. For more
    information, see Geometry in the Amazon Textract Developer Guide.

    - **X** *(float) --*

      The value of the X coordinate for a point on a ``Polygon`` .

    - **Y** *(float) --*

      The value of the Y coordinate for a point on a ``Polygon`` .
    """


_ClientGetDocumentAnalysisResponseBlocksGeometryTypeDef = TypedDict(
    "_ClientGetDocumentAnalysisResponseBlocksGeometryTypeDef",
    {
        "BoundingBox": ClientGetDocumentAnalysisResponseBlocksGeometryBoundingBoxTypeDef,
        "Polygon": List[ClientGetDocumentAnalysisResponseBlocksGeometryPolygonTypeDef],
    },
    total=False,
)


class ClientGetDocumentAnalysisResponseBlocksGeometryTypeDef(
    _ClientGetDocumentAnalysisResponseBlocksGeometryTypeDef
):
    """
    Type definition for `ClientGetDocumentAnalysisResponseBlocks` `Geometry`

    The location of the recognized text on the image. It includes an axis-aligned, coarse
    bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial
    information.

    - **BoundingBox** *(dict) --*

      An axis-aligned coarse representation of the location of the recognized text on the
      document page.

      - **Width** *(float) --*

        The width of the bounding box as a ratio of the overall document page width.

      - **Height** *(float) --*

        The height of the bounding box as a ratio of the overall document page height.

      - **Left** *(float) --*

        The left coordinate of the bounding box as a ratio of overall document page width.

      - **Top** *(float) --*

        The top coordinate of the bounding box as a ratio of overall document page height.

    - **Polygon** *(list) --*

      Within the bounding box, a fine-grained polygon around the recognized text.

      - *(dict) --*

        The X and Y coordinates of a point on a document page. The X and Y values returned
        are ratios of the overall document page size. For example, if the input document is
        700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the
        (350,50) pixel coordinate on the document page.

        An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText .
        ``Polygon`` represents a fine-grained polygon around detected text. For more
        information, see Geometry in the Amazon Textract Developer Guide.

        - **X** *(float) --*

          The value of the X coordinate for a point on a ``Polygon`` .

        - **Y** *(float) --*

          The value of the Y coordinate for a point on a ``Polygon`` .
    """


_ClientGetDocumentAnalysisResponseBlocksRelationshipsTypeDef = TypedDict(
    "_ClientGetDocumentAnalysisResponseBlocksRelationshipsTypeDef",
    {"Type": str, "Ids": List[str]},
    total=False,
)


class ClientGetDocumentAnalysisResponseBlocksRelationshipsTypeDef(
    _ClientGetDocumentAnalysisResponseBlocksRelationshipsTypeDef
):
    """
    Type definition for `ClientGetDocumentAnalysisResponseBlocks` `Relationships`

    Information about how blocks are related to each other. A ``Block`` object contains 0
    or more ``Relation`` objects in a list, ``Relationships`` . For more information, see
    Block .

    The ``Type`` element provides the type of the relationship for all blocks in the
    ``IDs`` array.

    - **Type** *(string) --*

      The type of relationship that the blocks in the IDs array have with the current
      block. The relationship can be ``VALUE`` or ``CHILD`` .

    - **Ids** *(list) --*

      An array of IDs for related blocks. You can get the type of the relationship from the
      ``Type`` element.

      - *(string) --*
    """


_ClientGetDocumentAnalysisResponseBlocksTypeDef = TypedDict(
    "_ClientGetDocumentAnalysisResponseBlocksTypeDef",
    {
        "BlockType": str,
        "Confidence": float,
        "Text": str,
        "RowIndex": int,
        "ColumnIndex": int,
        "RowSpan": int,
        "ColumnSpan": int,
        "Geometry": ClientGetDocumentAnalysisResponseBlocksGeometryTypeDef,
        "Id": str,
        "Relationships": List[
            ClientGetDocumentAnalysisResponseBlocksRelationshipsTypeDef
        ],
        "EntityTypes": List[str],
        "SelectionStatus": str,
        "Page": int,
    },
    total=False,
)


class ClientGetDocumentAnalysisResponseBlocksTypeDef(
    _ClientGetDocumentAnalysisResponseBlocksTypeDef
):
    """
    Type definition for `ClientGetDocumentAnalysisResponse` `Blocks`

    A ``Block`` represents items that are recognized in a document within a group of pixels
    close to each other. The information returned in a ``Block`` depends on the type of
    operation. In document-text detection (for example  DetectDocumentText ), you get
    information about the detected words and lines of text. In text analysis (for example
    AnalyzeDocument ), you can also get information about the fields, tables and selection
    elements that are detected in the document.

    An array of ``Block`` objects is returned by both synchronous and asynchronous operations.
    In synchronous operations, such as  DetectDocumentText , the array of ``Block`` objects is
    the entire set of results. In asynchronous operations, such as  GetDocumentAnalysis , the
    array is returned over one or more responses.

    For more information, see `How Amazon Textract Works
    <https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html>`__ .

    - **BlockType** *(string) --*

      The type of text that's recognized in a block. In text-detection operations, the
      following types are returned:

      * *PAGE* - Contains a list of the LINE Block objects that are detected on a document page.

      * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin
      script characters that aren't separated by spaces.

      * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page.

      In text analysis operations, the following types are returned:

      * *PAGE* - Contains a list of child Block objects that are detected on a document page.

      * *KEY_VALUE_SET* - Stores the KEY and VALUE Block objects for a field that's detected on
      a document page. Use the ``EntityType`` field to determine if a KEY_VALUE_SET object is a
      KEY Block object or a VALUE Block object.

      * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin
      script characters that aren't separated by spaces that's detected on a document page.

      * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page.

      * *TABLE* - A table that's detected on a document page. A table is any grid-based
      information with 2 or more rows or columns with a cell span of 1 row and 1 column each.

      * *CELL* - A cell within a detected table. The cell is the parent of the block that
      contains the text in the cell.

      * *SELECTION_ELEMENT* - A selectable element such as a radio button or checkbox that's
      detected on a document page. Use the value of ``SelectionStatus`` to determine the status
      of the selection element.

    - **Confidence** *(float) --*

      The confidence that Amazon Textract has in the accuracy of the recognized text and the
      accuracy of the geometry points around the recognized text.

    - **Text** *(string) --*

      The word or line of text that's recognized by Amazon Textract.

    - **RowIndex** *(integer) --*

      The row in which a table cell is located. The first row position is 1. ``RowIndex`` isn't
      returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

    - **ColumnIndex** *(integer) --*

      The column in which a table cell appears. The first column position is 1. ``ColumnIndex``
      isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

    - **RowSpan** *(integer) --*

      The number of rows that a table spans. ``RowSpan`` isn't returned by
      ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

    - **ColumnSpan** *(integer) --*

      The number of columns that a table cell spans. ``ColumnSpan`` isn't returned by
      ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

    - **Geometry** *(dict) --*

      The location of the recognized text on the image. It includes an axis-aligned, coarse
      bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial
      information.

      - **BoundingBox** *(dict) --*

        An axis-aligned coarse representation of the location of the recognized text on the
        document page.

        - **Width** *(float) --*

          The width of the bounding box as a ratio of the overall document page width.

        - **Height** *(float) --*

          The height of the bounding box as a ratio of the overall document page height.

        - **Left** *(float) --*

          The left coordinate of the bounding box as a ratio of overall document page width.

        - **Top** *(float) --*

          The top coordinate of the bounding box as a ratio of overall document page height.

      - **Polygon** *(list) --*

        Within the bounding box, a fine-grained polygon around the recognized text.

        - *(dict) --*

          The X and Y coordinates of a point on a document page. The X and Y values returned
          are ratios of the overall document page size. For example, if the input document is
          700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the
          (350,50) pixel coordinate on the document page.

          An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText .
          ``Polygon`` represents a fine-grained polygon around detected text. For more
          information, see Geometry in the Amazon Textract Developer Guide.

          - **X** *(float) --*

            The value of the X coordinate for a point on a ``Polygon`` .

          - **Y** *(float) --*

            The value of the Y coordinate for a point on a ``Polygon`` .

    - **Id** *(string) --*

      The identifier for the recognized text. The identifier is only unique for a single
      operation.

    - **Relationships** *(list) --*

      A list of child blocks of the current block. For example a LINE object has child blocks
      for each WORD block that's part of the line of text. There aren't Relationship objects in
      the list for relationships that don't exist, such as when the current block has no child
      blocks. The list size can be the following:

      * 0 - The block has no child blocks.

      * 1 - The block has child blocks.

      - *(dict) --*

        Information about how blocks are related to each other. A ``Block`` object contains 0
        or more ``Relation`` objects in a list, ``Relationships`` . For more information, see
        Block .

        The ``Type`` element provides the type of the relationship for all blocks in the
        ``IDs`` array.

        - **Type** *(string) --*

          The type of relationship that the blocks in the IDs array have with the current
          block. The relationship can be ``VALUE`` or ``CHILD`` .

        - **Ids** *(list) --*

          An array of IDs for related blocks. You can get the type of the relationship from the
          ``Type`` element.

          - *(string) --*

    - **EntityTypes** *(list) --*

      The type of entity. The following can be returned:

      * *KEY* - An identifier for a field on the document.

      * *VALUE* - The field text.

       ``EntityTypes`` isn't returned by ``DetectDocumentText`` and
       ``GetDocumentTextDetection`` .

      - *(string) --*

    - **SelectionStatus** *(string) --*

      The selection status of a selectable element such as a radio button or checkbox.

    - **Page** *(integer) --*

      The page in which a block was detected. ``Page`` is returned by asynchronous operations.
      Page values greater than 1 are only returned for multi-page documents that are in PDF
      format. A scanned image (JPG/PNG), even if it contains multiple document pages, is always
      considered to be a single-page document and the value of ``Page`` is always 1.
      Synchronous operations don't return ``Page`` as every input document is considered to be
      a single-page document.
    """


_ClientGetDocumentAnalysisResponseDocumentMetadataTypeDef = TypedDict(
    "_ClientGetDocumentAnalysisResponseDocumentMetadataTypeDef",
    {"Pages": int},
    total=False,
)


class ClientGetDocumentAnalysisResponseDocumentMetadataTypeDef(
    _ClientGetDocumentAnalysisResponseDocumentMetadataTypeDef
):
    """
    Type definition for `ClientGetDocumentAnalysisResponse` `DocumentMetadata`

    Information about a document that Amazon Textract processed. ``DocumentMetadata`` is returned
    in every page of paginated responses from an Amazon Textract video operation.

    - **Pages** *(integer) --*

      The number of pages detected in the document.
    """


_ClientGetDocumentAnalysisResponseWarningsTypeDef = TypedDict(
    "_ClientGetDocumentAnalysisResponseWarningsTypeDef",
    {"ErrorCode": str, "Pages": List[int]},
    total=False,
)


class ClientGetDocumentAnalysisResponseWarningsTypeDef(
    _ClientGetDocumentAnalysisResponseWarningsTypeDef
):
    """
    Type definition for `ClientGetDocumentAnalysisResponse` `Warnings`

    A warning about an issue that occurred during asynchronous text analysis (
    StartDocumentAnalysis ) or asynchronous document-text detection (
    StartDocumentTextDetection ).

    - **ErrorCode** *(string) --*

      The error code for the warning.

    - **Pages** *(list) --*

      A list of the pages that the warning applies to.

      - *(integer) --*
    """


_ClientGetDocumentAnalysisResponseTypeDef = TypedDict(
    "_ClientGetDocumentAnalysisResponseTypeDef",
    {
        "DocumentMetadata": ClientGetDocumentAnalysisResponseDocumentMetadataTypeDef,
        "JobStatus": str,
        "NextToken": str,
        "Blocks": List[ClientGetDocumentAnalysisResponseBlocksTypeDef],
        "Warnings": List[ClientGetDocumentAnalysisResponseWarningsTypeDef],
        "StatusMessage": str,
    },
    total=False,
)


class ClientGetDocumentAnalysisResponseTypeDef(
    _ClientGetDocumentAnalysisResponseTypeDef
):
    """
    Type definition for `ClientGetDocumentAnalysis` `Response`

    - **DocumentMetadata** *(dict) --*

      Information about a document that Amazon Textract processed. ``DocumentMetadata`` is returned
      in every page of paginated responses from an Amazon Textract video operation.

      - **Pages** *(integer) --*

        The number of pages detected in the document.

    - **JobStatus** *(string) --*

      The current status of the text detection job.

    - **NextToken** *(string) --*

      If the response is truncated, Amazon Textract returns this token. You can use this token in
      the subsequent request to retrieve the next set of text detection results.

    - **Blocks** *(list) --*

      The results of the text analysis operation.

      - *(dict) --*

        A ``Block`` represents items that are recognized in a document within a group of pixels
        close to each other. The information returned in a ``Block`` depends on the type of
        operation. In document-text detection (for example  DetectDocumentText ), you get
        information about the detected words and lines of text. In text analysis (for example
        AnalyzeDocument ), you can also get information about the fields, tables and selection
        elements that are detected in the document.

        An array of ``Block`` objects is returned by both synchronous and asynchronous operations.
        In synchronous operations, such as  DetectDocumentText , the array of ``Block`` objects is
        the entire set of results. In asynchronous operations, such as  GetDocumentAnalysis , the
        array is returned over one or more responses.

        For more information, see `How Amazon Textract Works
        <https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html>`__ .

        - **BlockType** *(string) --*

          The type of text that's recognized in a block. In text-detection operations, the
          following types are returned:

          * *PAGE* - Contains a list of the LINE Block objects that are detected on a document page.

          * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin
          script characters that aren't separated by spaces.

          * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page.

          In text analysis operations, the following types are returned:

          * *PAGE* - Contains a list of child Block objects that are detected on a document page.

          * *KEY_VALUE_SET* - Stores the KEY and VALUE Block objects for a field that's detected on
          a document page. Use the ``EntityType`` field to determine if a KEY_VALUE_SET object is a
          KEY Block object or a VALUE Block object.

          * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin
          script characters that aren't separated by spaces that's detected on a document page.

          * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page.

          * *TABLE* - A table that's detected on a document page. A table is any grid-based
          information with 2 or more rows or columns with a cell span of 1 row and 1 column each.

          * *CELL* - A cell within a detected table. The cell is the parent of the block that
          contains the text in the cell.

          * *SELECTION_ELEMENT* - A selectable element such as a radio button or checkbox that's
          detected on a document page. Use the value of ``SelectionStatus`` to determine the status
          of the selection element.

        - **Confidence** *(float) --*

          The confidence that Amazon Textract has in the accuracy of the recognized text and the
          accuracy of the geometry points around the recognized text.

        - **Text** *(string) --*

          The word or line of text that's recognized by Amazon Textract.

        - **RowIndex** *(integer) --*

          The row in which a table cell is located. The first row position is 1. ``RowIndex`` isn't
          returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

        - **ColumnIndex** *(integer) --*

          The column in which a table cell appears. The first column position is 1. ``ColumnIndex``
          isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

        - **RowSpan** *(integer) --*

          The number of rows that a table spans. ``RowSpan`` isn't returned by
          ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

        - **ColumnSpan** *(integer) --*

          The number of columns that a table cell spans. ``ColumnSpan`` isn't returned by
          ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

        - **Geometry** *(dict) --*

          The location of the recognized text on the image. It includes an axis-aligned, coarse
          bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial
          information.

          - **BoundingBox** *(dict) --*

            An axis-aligned coarse representation of the location of the recognized text on the
            document page.

            - **Width** *(float) --*

              The width of the bounding box as a ratio of the overall document page width.

            - **Height** *(float) --*

              The height of the bounding box as a ratio of the overall document page height.

            - **Left** *(float) --*

              The left coordinate of the bounding box as a ratio of overall document page width.

            - **Top** *(float) --*

              The top coordinate of the bounding box as a ratio of overall document page height.

          - **Polygon** *(list) --*

            Within the bounding box, a fine-grained polygon around the recognized text.

            - *(dict) --*

              The X and Y coordinates of a point on a document page. The X and Y values returned
              are ratios of the overall document page size. For example, if the input document is
              700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the
              (350,50) pixel coordinate on the document page.

              An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText .
              ``Polygon`` represents a fine-grained polygon around detected text. For more
              information, see Geometry in the Amazon Textract Developer Guide.

              - **X** *(float) --*

                The value of the X coordinate for a point on a ``Polygon`` .

              - **Y** *(float) --*

                The value of the Y coordinate for a point on a ``Polygon`` .

        - **Id** *(string) --*

          The identifier for the recognized text. The identifier is only unique for a single
          operation.

        - **Relationships** *(list) --*

          A list of child blocks of the current block. For example a LINE object has child blocks
          for each WORD block that's part of the line of text. There aren't Relationship objects in
          the list for relationships that don't exist, such as when the current block has no child
          blocks. The list size can be the following:

          * 0 - The block has no child blocks.

          * 1 - The block has child blocks.

          - *(dict) --*

            Information about how blocks are related to each other. A ``Block`` object contains 0
            or more ``Relation`` objects in a list, ``Relationships`` . For more information, see
            Block .

            The ``Type`` element provides the type of the relationship for all blocks in the
            ``IDs`` array.

            - **Type** *(string) --*

              The type of relationship that the blocks in the IDs array have with the current
              block. The relationship can be ``VALUE`` or ``CHILD`` .

            - **Ids** *(list) --*

              An array of IDs for related blocks. You can get the type of the relationship from the
              ``Type`` element.

              - *(string) --*

        - **EntityTypes** *(list) --*

          The type of entity. The following can be returned:

          * *KEY* - An identifier for a field on the document.

          * *VALUE* - The field text.

           ``EntityTypes`` isn't returned by ``DetectDocumentText`` and
           ``GetDocumentTextDetection`` .

          - *(string) --*

        - **SelectionStatus** *(string) --*

          The selection status of a selectable element such as a radio button or checkbox.

        - **Page** *(integer) --*

          The page in which a block was detected. ``Page`` is returned by asynchronous operations.
          Page values greater than 1 are only returned for multi-page documents that are in PDF
          format. A scanned image (JPG/PNG), even if it contains multiple document pages, is always
          considered to be a single-page document and the value of ``Page`` is always 1.
          Synchronous operations don't return ``Page`` as every input document is considered to be
          a single-page document.

    - **Warnings** *(list) --*

      A list of warnings that occurred during the document analysis operation.

      - *(dict) --*

        A warning about an issue that occurred during asynchronous text analysis (
        StartDocumentAnalysis ) or asynchronous document-text detection (
        StartDocumentTextDetection ).

        - **ErrorCode** *(string) --*

          The error code for the warning.

        - **Pages** *(list) --*

          A list of the pages that the warning applies to.

          - *(integer) --*

    - **StatusMessage** *(string) --*

      The current status of an asynchronous document analysis operation.
    """


_ClientGetDocumentTextDetectionResponseBlocksGeometryBoundingBoxTypeDef = TypedDict(
    "_ClientGetDocumentTextDetectionResponseBlocksGeometryBoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)


class ClientGetDocumentTextDetectionResponseBlocksGeometryBoundingBoxTypeDef(
    _ClientGetDocumentTextDetectionResponseBlocksGeometryBoundingBoxTypeDef
):
    """
    Type definition for `ClientGetDocumentTextDetectionResponseBlocksGeometry` `BoundingBox`

    An axis-aligned coarse representation of the location of the recognized text on the
    document page.

    - **Width** *(float) --*

      The width of the bounding box as a ratio of the overall document page width.

    - **Height** *(float) --*

      The height of the bounding box as a ratio of the overall document page height.

    - **Left** *(float) --*

      The left coordinate of the bounding box as a ratio of overall document page width.

    - **Top** *(float) --*

      The top coordinate of the bounding box as a ratio of overall document page height.
    """


_ClientGetDocumentTextDetectionResponseBlocksGeometryPolygonTypeDef = TypedDict(
    "_ClientGetDocumentTextDetectionResponseBlocksGeometryPolygonTypeDef",
    {"X": float, "Y": float},
    total=False,
)


class ClientGetDocumentTextDetectionResponseBlocksGeometryPolygonTypeDef(
    _ClientGetDocumentTextDetectionResponseBlocksGeometryPolygonTypeDef
):
    """
    Type definition for `ClientGetDocumentTextDetectionResponseBlocksGeometry` `Polygon`

    The X and Y coordinates of a point on a document page. The X and Y values returned
    are ratios of the overall document page size. For example, if the input document is
    700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the
    (350,50) pixel coordinate on the document page.

    An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText .
    ``Polygon`` represents a fine-grained polygon around detected text. For more
    information, see Geometry in the Amazon Textract Developer Guide.

    - **X** *(float) --*

      The value of the X coordinate for a point on a ``Polygon`` .

    - **Y** *(float) --*

      The value of the Y coordinate for a point on a ``Polygon`` .
    """


_ClientGetDocumentTextDetectionResponseBlocksGeometryTypeDef = TypedDict(
    "_ClientGetDocumentTextDetectionResponseBlocksGeometryTypeDef",
    {
        "BoundingBox": ClientGetDocumentTextDetectionResponseBlocksGeometryBoundingBoxTypeDef,
        "Polygon": List[
            ClientGetDocumentTextDetectionResponseBlocksGeometryPolygonTypeDef
        ],
    },
    total=False,
)


class ClientGetDocumentTextDetectionResponseBlocksGeometryTypeDef(
    _ClientGetDocumentTextDetectionResponseBlocksGeometryTypeDef
):
    """
    Type definition for `ClientGetDocumentTextDetectionResponseBlocks` `Geometry`

    The location of the recognized text on the image. It includes an axis-aligned, coarse
    bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial
    information.

    - **BoundingBox** *(dict) --*

      An axis-aligned coarse representation of the location of the recognized text on the
      document page.

      - **Width** *(float) --*

        The width of the bounding box as a ratio of the overall document page width.

      - **Height** *(float) --*

        The height of the bounding box as a ratio of the overall document page height.

      - **Left** *(float) --*

        The left coordinate of the bounding box as a ratio of overall document page width.

      - **Top** *(float) --*

        The top coordinate of the bounding box as a ratio of overall document page height.

    - **Polygon** *(list) --*

      Within the bounding box, a fine-grained polygon around the recognized text.

      - *(dict) --*

        The X and Y coordinates of a point on a document page. The X and Y values returned
        are ratios of the overall document page size. For example, if the input document is
        700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the
        (350,50) pixel coordinate on the document page.

        An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText .
        ``Polygon`` represents a fine-grained polygon around detected text. For more
        information, see Geometry in the Amazon Textract Developer Guide.

        - **X** *(float) --*

          The value of the X coordinate for a point on a ``Polygon`` .

        - **Y** *(float) --*

          The value of the Y coordinate for a point on a ``Polygon`` .
    """


_ClientGetDocumentTextDetectionResponseBlocksRelationshipsTypeDef = TypedDict(
    "_ClientGetDocumentTextDetectionResponseBlocksRelationshipsTypeDef",
    {"Type": str, "Ids": List[str]},
    total=False,
)


class ClientGetDocumentTextDetectionResponseBlocksRelationshipsTypeDef(
    _ClientGetDocumentTextDetectionResponseBlocksRelationshipsTypeDef
):
    """
    Type definition for `ClientGetDocumentTextDetectionResponseBlocks` `Relationships`

    Information about how blocks are related to each other. A ``Block`` object contains 0
    or more ``Relation`` objects in a list, ``Relationships`` . For more information, see
    Block .

    The ``Type`` element provides the type of the relationship for all blocks in the
    ``IDs`` array.

    - **Type** *(string) --*

      The type of relationship that the blocks in the IDs array have with the current
      block. The relationship can be ``VALUE`` or ``CHILD`` .

    - **Ids** *(list) --*

      An array of IDs for related blocks. You can get the type of the relationship from the
      ``Type`` element.

      - *(string) --*
    """


_ClientGetDocumentTextDetectionResponseBlocksTypeDef = TypedDict(
    "_ClientGetDocumentTextDetectionResponseBlocksTypeDef",
    {
        "BlockType": str,
        "Confidence": float,
        "Text": str,
        "RowIndex": int,
        "ColumnIndex": int,
        "RowSpan": int,
        "ColumnSpan": int,
        "Geometry": ClientGetDocumentTextDetectionResponseBlocksGeometryTypeDef,
        "Id": str,
        "Relationships": List[
            ClientGetDocumentTextDetectionResponseBlocksRelationshipsTypeDef
        ],
        "EntityTypes": List[str],
        "SelectionStatus": str,
        "Page": int,
    },
    total=False,
)


class ClientGetDocumentTextDetectionResponseBlocksTypeDef(
    _ClientGetDocumentTextDetectionResponseBlocksTypeDef
):
    """
    Type definition for `ClientGetDocumentTextDetectionResponse` `Blocks`

    A ``Block`` represents items that are recognized in a document within a group of pixels
    close to each other. The information returned in a ``Block`` depends on the type of
    operation. In document-text detection (for example  DetectDocumentText ), you get
    information about the detected words and lines of text. In text analysis (for example
    AnalyzeDocument ), you can also get information about the fields, tables and selection
    elements that are detected in the document.

    An array of ``Block`` objects is returned by both synchronous and asynchronous operations.
    In synchronous operations, such as  DetectDocumentText , the array of ``Block`` objects is
    the entire set of results. In asynchronous operations, such as  GetDocumentAnalysis , the
    array is returned over one or more responses.

    For more information, see `How Amazon Textract Works
    <https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html>`__ .

    - **BlockType** *(string) --*

      The type of text that's recognized in a block. In text-detection operations, the
      following types are returned:

      * *PAGE* - Contains a list of the LINE Block objects that are detected on a document page.

      * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin
      script characters that aren't separated by spaces.

      * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page.

      In text analysis operations, the following types are returned:

      * *PAGE* - Contains a list of child Block objects that are detected on a document page.

      * *KEY_VALUE_SET* - Stores the KEY and VALUE Block objects for a field that's detected on
      a document page. Use the ``EntityType`` field to determine if a KEY_VALUE_SET object is a
      KEY Block object or a VALUE Block object.

      * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin
      script characters that aren't separated by spaces that's detected on a document page.

      * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page.

      * *TABLE* - A table that's detected on a document page. A table is any grid-based
      information with 2 or more rows or columns with a cell span of 1 row and 1 column each.

      * *CELL* - A cell within a detected table. The cell is the parent of the block that
      contains the text in the cell.

      * *SELECTION_ELEMENT* - A selectable element such as a radio button or checkbox that's
      detected on a document page. Use the value of ``SelectionStatus`` to determine the status
      of the selection element.

    - **Confidence** *(float) --*

      The confidence that Amazon Textract has in the accuracy of the recognized text and the
      accuracy of the geometry points around the recognized text.

    - **Text** *(string) --*

      The word or line of text that's recognized by Amazon Textract.

    - **RowIndex** *(integer) --*

      The row in which a table cell is located. The first row position is 1. ``RowIndex`` isn't
      returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

    - **ColumnIndex** *(integer) --*

      The column in which a table cell appears. The first column position is 1. ``ColumnIndex``
      isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

    - **RowSpan** *(integer) --*

      The number of rows that a table spans. ``RowSpan`` isn't returned by
      ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

    - **ColumnSpan** *(integer) --*

      The number of columns that a table cell spans. ``ColumnSpan`` isn't returned by
      ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

    - **Geometry** *(dict) --*

      The location of the recognized text on the image. It includes an axis-aligned, coarse
      bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial
      information.

      - **BoundingBox** *(dict) --*

        An axis-aligned coarse representation of the location of the recognized text on the
        document page.

        - **Width** *(float) --*

          The width of the bounding box as a ratio of the overall document page width.

        - **Height** *(float) --*

          The height of the bounding box as a ratio of the overall document page height.

        - **Left** *(float) --*

          The left coordinate of the bounding box as a ratio of overall document page width.

        - **Top** *(float) --*

          The top coordinate of the bounding box as a ratio of overall document page height.

      - **Polygon** *(list) --*

        Within the bounding box, a fine-grained polygon around the recognized text.

        - *(dict) --*

          The X and Y coordinates of a point on a document page. The X and Y values returned
          are ratios of the overall document page size. For example, if the input document is
          700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the
          (350,50) pixel coordinate on the document page.

          An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText .
          ``Polygon`` represents a fine-grained polygon around detected text. For more
          information, see Geometry in the Amazon Textract Developer Guide.

          - **X** *(float) --*

            The value of the X coordinate for a point on a ``Polygon`` .

          - **Y** *(float) --*

            The value of the Y coordinate for a point on a ``Polygon`` .

    - **Id** *(string) --*

      The identifier for the recognized text. The identifier is only unique for a single
      operation.

    - **Relationships** *(list) --*

      A list of child blocks of the current block. For example a LINE object has child blocks
      for each WORD block that's part of the line of text. There aren't Relationship objects in
      the list for relationships that don't exist, such as when the current block has no child
      blocks. The list size can be the following:

      * 0 - The block has no child blocks.

      * 1 - The block has child blocks.

      - *(dict) --*

        Information about how blocks are related to each other. A ``Block`` object contains 0
        or more ``Relation`` objects in a list, ``Relationships`` . For more information, see
        Block .

        The ``Type`` element provides the type of the relationship for all blocks in the
        ``IDs`` array.

        - **Type** *(string) --*

          The type of relationship that the blocks in the IDs array have with the current
          block. The relationship can be ``VALUE`` or ``CHILD`` .

        - **Ids** *(list) --*

          An array of IDs for related blocks. You can get the type of the relationship from the
          ``Type`` element.

          - *(string) --*

    - **EntityTypes** *(list) --*

      The type of entity. The following can be returned:

      * *KEY* - An identifier for a field on the document.

      * *VALUE* - The field text.

       ``EntityTypes`` isn't returned by ``DetectDocumentText`` and
       ``GetDocumentTextDetection`` .

      - *(string) --*

    - **SelectionStatus** *(string) --*

      The selection status of a selectable element such as a radio button or checkbox.

    - **Page** *(integer) --*

      The page in which a block was detected. ``Page`` is returned by asynchronous operations.
      Page values greater than 1 are only returned for multi-page documents that are in PDF
      format. A scanned image (JPG/PNG), even if it contains multiple document pages, is always
      considered to be a single-page document and the value of ``Page`` is always 1.
      Synchronous operations don't return ``Page`` as every input document is considered to be
      a single-page document.
    """


_ClientGetDocumentTextDetectionResponseDocumentMetadataTypeDef = TypedDict(
    "_ClientGetDocumentTextDetectionResponseDocumentMetadataTypeDef",
    {"Pages": int},
    total=False,
)


class ClientGetDocumentTextDetectionResponseDocumentMetadataTypeDef(
    _ClientGetDocumentTextDetectionResponseDocumentMetadataTypeDef
):
    """
    Type definition for `ClientGetDocumentTextDetectionResponse` `DocumentMetadata`

    Information about a document that Amazon Textract processed. ``DocumentMetadata`` is returned
    in every page of paginated responses from an Amazon Textract video operation.

    - **Pages** *(integer) --*

      The number of pages detected in the document.
    """


_ClientGetDocumentTextDetectionResponseWarningsTypeDef = TypedDict(
    "_ClientGetDocumentTextDetectionResponseWarningsTypeDef",
    {"ErrorCode": str, "Pages": List[int]},
    total=False,
)


class ClientGetDocumentTextDetectionResponseWarningsTypeDef(
    _ClientGetDocumentTextDetectionResponseWarningsTypeDef
):
    """
    Type definition for `ClientGetDocumentTextDetectionResponse` `Warnings`

    A warning about an issue that occurred during asynchronous text analysis (
    StartDocumentAnalysis ) or asynchronous document-text detection (
    StartDocumentTextDetection ).

    - **ErrorCode** *(string) --*

      The error code for the warning.

    - **Pages** *(list) --*

      A list of the pages that the warning applies to.

      - *(integer) --*
    """


_ClientGetDocumentTextDetectionResponseTypeDef = TypedDict(
    "_ClientGetDocumentTextDetectionResponseTypeDef",
    {
        "DocumentMetadata": ClientGetDocumentTextDetectionResponseDocumentMetadataTypeDef,
        "JobStatus": str,
        "NextToken": str,
        "Blocks": List[ClientGetDocumentTextDetectionResponseBlocksTypeDef],
        "Warnings": List[ClientGetDocumentTextDetectionResponseWarningsTypeDef],
        "StatusMessage": str,
    },
    total=False,
)


class ClientGetDocumentTextDetectionResponseTypeDef(
    _ClientGetDocumentTextDetectionResponseTypeDef
):
    """
    Type definition for `ClientGetDocumentTextDetection` `Response`

    - **DocumentMetadata** *(dict) --*

      Information about a document that Amazon Textract processed. ``DocumentMetadata`` is returned
      in every page of paginated responses from an Amazon Textract video operation.

      - **Pages** *(integer) --*

        The number of pages detected in the document.

    - **JobStatus** *(string) --*

      The current status of the text detection job.

    - **NextToken** *(string) --*

      If the response is truncated, Amazon Textract returns this token. You can use this token in
      the subsequent request to retrieve the next set of text-detection results.

    - **Blocks** *(list) --*

      The results of the text-detection operation.

      - *(dict) --*

        A ``Block`` represents items that are recognized in a document within a group of pixels
        close to each other. The information returned in a ``Block`` depends on the type of
        operation. In document-text detection (for example  DetectDocumentText ), you get
        information about the detected words and lines of text. In text analysis (for example
        AnalyzeDocument ), you can also get information about the fields, tables and selection
        elements that are detected in the document.

        An array of ``Block`` objects is returned by both synchronous and asynchronous operations.
        In synchronous operations, such as  DetectDocumentText , the array of ``Block`` objects is
        the entire set of results. In asynchronous operations, such as  GetDocumentAnalysis , the
        array is returned over one or more responses.

        For more information, see `How Amazon Textract Works
        <https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html>`__ .

        - **BlockType** *(string) --*

          The type of text that's recognized in a block. In text-detection operations, the
          following types are returned:

          * *PAGE* - Contains a list of the LINE Block objects that are detected on a document page.

          * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin
          script characters that aren't separated by spaces.

          * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page.

          In text analysis operations, the following types are returned:

          * *PAGE* - Contains a list of child Block objects that are detected on a document page.

          * *KEY_VALUE_SET* - Stores the KEY and VALUE Block objects for a field that's detected on
          a document page. Use the ``EntityType`` field to determine if a KEY_VALUE_SET object is a
          KEY Block object or a VALUE Block object.

          * *WORD* - A word detected on a document page. A word is one or more ISO basic Latin
          script characters that aren't separated by spaces that's detected on a document page.

          * *LINE* - A string of tab-delimited, contiguous words that's detected on a document page.

          * *TABLE* - A table that's detected on a document page. A table is any grid-based
          information with 2 or more rows or columns with a cell span of 1 row and 1 column each.

          * *CELL* - A cell within a detected table. The cell is the parent of the block that
          contains the text in the cell.

          * *SELECTION_ELEMENT* - A selectable element such as a radio button or checkbox that's
          detected on a document page. Use the value of ``SelectionStatus`` to determine the status
          of the selection element.

        - **Confidence** *(float) --*

          The confidence that Amazon Textract has in the accuracy of the recognized text and the
          accuracy of the geometry points around the recognized text.

        - **Text** *(string) --*

          The word or line of text that's recognized by Amazon Textract.

        - **RowIndex** *(integer) --*

          The row in which a table cell is located. The first row position is 1. ``RowIndex`` isn't
          returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

        - **ColumnIndex** *(integer) --*

          The column in which a table cell appears. The first column position is 1. ``ColumnIndex``
          isn't returned by ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

        - **RowSpan** *(integer) --*

          The number of rows that a table spans. ``RowSpan`` isn't returned by
          ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

        - **ColumnSpan** *(integer) --*

          The number of columns that a table cell spans. ``ColumnSpan`` isn't returned by
          ``DetectDocumentText`` and ``GetDocumentTextDetection`` .

        - **Geometry** *(dict) --*

          The location of the recognized text on the image. It includes an axis-aligned, coarse
          bounding box that surrounds the text, and a finer-grain polygon for more accurate spatial
          information.

          - **BoundingBox** *(dict) --*

            An axis-aligned coarse representation of the location of the recognized text on the
            document page.

            - **Width** *(float) --*

              The width of the bounding box as a ratio of the overall document page width.

            - **Height** *(float) --*

              The height of the bounding box as a ratio of the overall document page height.

            - **Left** *(float) --*

              The left coordinate of the bounding box as a ratio of overall document page width.

            - **Top** *(float) --*

              The top coordinate of the bounding box as a ratio of overall document page height.

          - **Polygon** *(list) --*

            Within the bounding box, a fine-grained polygon around the recognized text.

            - *(dict) --*

              The X and Y coordinates of a point on a document page. The X and Y values returned
              are ratios of the overall document page size. For example, if the input document is
              700 x 200 and the operation returns X=0.5 and Y=0.25, then the point is at the
              (350,50) pixel coordinate on the document page.

              An array of ``Point`` objects, ``Polygon`` , is returned by  DetectDocumentText .
              ``Polygon`` represents a fine-grained polygon around detected text. For more
              information, see Geometry in the Amazon Textract Developer Guide.

              - **X** *(float) --*

                The value of the X coordinate for a point on a ``Polygon`` .

              - **Y** *(float) --*

                The value of the Y coordinate for a point on a ``Polygon`` .

        - **Id** *(string) --*

          The identifier for the recognized text. The identifier is only unique for a single
          operation.

        - **Relationships** *(list) --*

          A list of child blocks of the current block. For example a LINE object has child blocks
          for each WORD block that's part of the line of text. There aren't Relationship objects in
          the list for relationships that don't exist, such as when the current block has no child
          blocks. The list size can be the following:

          * 0 - The block has no child blocks.

          * 1 - The block has child blocks.

          - *(dict) --*

            Information about how blocks are related to each other. A ``Block`` object contains 0
            or more ``Relation`` objects in a list, ``Relationships`` . For more information, see
            Block .

            The ``Type`` element provides the type of the relationship for all blocks in the
            ``IDs`` array.

            - **Type** *(string) --*

              The type of relationship that the blocks in the IDs array have with the current
              block. The relationship can be ``VALUE`` or ``CHILD`` .

            - **Ids** *(list) --*

              An array of IDs for related blocks. You can get the type of the relationship from the
              ``Type`` element.

              - *(string) --*

        - **EntityTypes** *(list) --*

          The type of entity. The following can be returned:

          * *KEY* - An identifier for a field on the document.

          * *VALUE* - The field text.

           ``EntityTypes`` isn't returned by ``DetectDocumentText`` and
           ``GetDocumentTextDetection`` .

          - *(string) --*

        - **SelectionStatus** *(string) --*

          The selection status of a selectable element such as a radio button or checkbox.

        - **Page** *(integer) --*

          The page in which a block was detected. ``Page`` is returned by asynchronous operations.
          Page values greater than 1 are only returned for multi-page documents that are in PDF
          format. A scanned image (JPG/PNG), even if it contains multiple document pages, is always
          considered to be a single-page document and the value of ``Page`` is always 1.
          Synchronous operations don't return ``Page`` as every input document is considered to be
          a single-page document.

    - **Warnings** *(list) --*

      A list of warnings that occurred during the document text-detection operation.

      - *(dict) --*

        A warning about an issue that occurred during asynchronous text analysis (
        StartDocumentAnalysis ) or asynchronous document-text detection (
        StartDocumentTextDetection ).

        - **ErrorCode** *(string) --*

          The error code for the warning.

        - **Pages** *(list) --*

          A list of the pages that the warning applies to.

          - *(integer) --*

    - **StatusMessage** *(string) --*

      The current status of an asynchronous document text-detection operation.
    """


_ClientStartDocumentAnalysisDocumentLocationS3ObjectTypeDef = TypedDict(
    "_ClientStartDocumentAnalysisDocumentLocationS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientStartDocumentAnalysisDocumentLocationS3ObjectTypeDef(
    _ClientStartDocumentAnalysisDocumentLocationS3ObjectTypeDef
):
    """
    Type definition for `ClientStartDocumentAnalysisDocumentLocation` `S3Object`

    The Amazon S3 bucket that contains the input document.

    - **Bucket** *(string) --*

      The name of the S3 bucket.

    - **Name** *(string) --*

      The file name of the input document. It must be an image file (.JPG or .PNG format).
      Asynchronous operations also support PDF files.

    - **Version** *(string) --*

      If the bucket has versioning enabled, you can specify the object version.
    """


_ClientStartDocumentAnalysisDocumentLocationTypeDef = TypedDict(
    "_ClientStartDocumentAnalysisDocumentLocationTypeDef",
    {"S3Object": ClientStartDocumentAnalysisDocumentLocationS3ObjectTypeDef},
    total=False,
)


class ClientStartDocumentAnalysisDocumentLocationTypeDef(
    _ClientStartDocumentAnalysisDocumentLocationTypeDef
):
    """
    Type definition for `ClientStartDocumentAnalysis` `DocumentLocation`

    The location of the document to be processed.

    - **S3Object** *(dict) --*

      The Amazon S3 bucket that contains the input document.

      - **Bucket** *(string) --*

        The name of the S3 bucket.

      - **Name** *(string) --*

        The file name of the input document. It must be an image file (.JPG or .PNG format).
        Asynchronous operations also support PDF files.

      - **Version** *(string) --*

        If the bucket has versioning enabled, you can specify the object version.
    """


_ClientStartDocumentAnalysisNotificationChannelTypeDef = TypedDict(
    "_ClientStartDocumentAnalysisNotificationChannelTypeDef",
    {"SNSTopicArn": str, "RoleArn": str},
)


class ClientStartDocumentAnalysisNotificationChannelTypeDef(
    _ClientStartDocumentAnalysisNotificationChannelTypeDef
):
    """
    Type definition for `ClientStartDocumentAnalysis` `NotificationChannel`

    The Amazon SNS topic ARN that you want Amazon Textract to publish the completion status of the
    operation to.

    - **SNSTopicArn** *(string) --* **[REQUIRED]**

      The Amazon SNS topic that Amazon Textract posts the completion status to.

    - **RoleArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of an IAM role that gives Amazon Textract publishing permissions
      to the Amazon SNS topic.
    """


_ClientStartDocumentAnalysisResponseTypeDef = TypedDict(
    "_ClientStartDocumentAnalysisResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartDocumentAnalysisResponseTypeDef(
    _ClientStartDocumentAnalysisResponseTypeDef
):
    """
    Type definition for `ClientStartDocumentAnalysis` `Response`

    - **JobId** *(string) --*

      The identifier for the document text detection job. Use ``JobId`` to identify the job in a
      subsequent call to ``GetDocumentAnalysis`` .
    """


_ClientStartDocumentTextDetectionDocumentLocationS3ObjectTypeDef = TypedDict(
    "_ClientStartDocumentTextDetectionDocumentLocationS3ObjectTypeDef",
    {"Bucket": str, "Name": str, "Version": str},
    total=False,
)


class ClientStartDocumentTextDetectionDocumentLocationS3ObjectTypeDef(
    _ClientStartDocumentTextDetectionDocumentLocationS3ObjectTypeDef
):
    """
    Type definition for `ClientStartDocumentTextDetectionDocumentLocation` `S3Object`

    The Amazon S3 bucket that contains the input document.

    - **Bucket** *(string) --*

      The name of the S3 bucket.

    - **Name** *(string) --*

      The file name of the input document. It must be an image file (.JPG or .PNG format).
      Asynchronous operations also support PDF files.

    - **Version** *(string) --*

      If the bucket has versioning enabled, you can specify the object version.
    """


_ClientStartDocumentTextDetectionDocumentLocationTypeDef = TypedDict(
    "_ClientStartDocumentTextDetectionDocumentLocationTypeDef",
    {"S3Object": ClientStartDocumentTextDetectionDocumentLocationS3ObjectTypeDef},
    total=False,
)


class ClientStartDocumentTextDetectionDocumentLocationTypeDef(
    _ClientStartDocumentTextDetectionDocumentLocationTypeDef
):
    """
    Type definition for `ClientStartDocumentTextDetection` `DocumentLocation`

    The location of the document to be processed.

    - **S3Object** *(dict) --*

      The Amazon S3 bucket that contains the input document.

      - **Bucket** *(string) --*

        The name of the S3 bucket.

      - **Name** *(string) --*

        The file name of the input document. It must be an image file (.JPG or .PNG format).
        Asynchronous operations also support PDF files.

      - **Version** *(string) --*

        If the bucket has versioning enabled, you can specify the object version.
    """


_ClientStartDocumentTextDetectionNotificationChannelTypeDef = TypedDict(
    "_ClientStartDocumentTextDetectionNotificationChannelTypeDef",
    {"SNSTopicArn": str, "RoleArn": str},
)


class ClientStartDocumentTextDetectionNotificationChannelTypeDef(
    _ClientStartDocumentTextDetectionNotificationChannelTypeDef
):
    """
    Type definition for `ClientStartDocumentTextDetection` `NotificationChannel`

    The Amazon SNS topic ARN that you want Amazon Textract to publish the completion status of the
    operation to.

    - **SNSTopicArn** *(string) --* **[REQUIRED]**

      The Amazon SNS topic that Amazon Textract posts the completion status to.

    - **RoleArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) of an IAM role that gives Amazon Textract publishing permissions
      to the Amazon SNS topic.
    """


_ClientStartDocumentTextDetectionResponseTypeDef = TypedDict(
    "_ClientStartDocumentTextDetectionResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartDocumentTextDetectionResponseTypeDef(
    _ClientStartDocumentTextDetectionResponseTypeDef
):
    """
    Type definition for `ClientStartDocumentTextDetection` `Response`

    - **JobId** *(string) --*

      The identifier for the document text-detection job. Use ``JobId`` to identify the job in a
      subsequent call to ``GetDocumentTextDetection`` .
    """

"Main interface for s3 Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_s3.type_defs import (
    ListMultipartUploadsPaginatePaginationConfigTypeDef,
    ListMultipartUploadsPaginateResponseTypeDef,
    ListObjectVersionsPaginatePaginationConfigTypeDef,
    ListObjectVersionsPaginateResponseTypeDef,
    ListObjectsPaginatePaginationConfigTypeDef,
    ListObjectsPaginateResponseTypeDef,
    ListObjectsV2PaginatePaginationConfigTypeDef,
    ListObjectsV2PaginateResponseTypeDef,
    ListPartsPaginatePaginationConfigTypeDef,
    ListPartsPaginateResponseTypeDef,
)


__all__ = (
    "ListMultipartUploadsPaginator",
    "ListObjectVersionsPaginator",
    "ListObjectsPaginator",
    "ListObjectsV2Paginator",
    "ListPartsPaginator",
)


class ListMultipartUploadsPaginator(Boto3Paginator):
    """
    Paginator for `list_multipart_uploads`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: str = None,
        Prefix: str = None,
        PaginationConfig: ListMultipartUploadsPaginatePaginationConfigTypeDef = None,
    ) -> ListMultipartUploadsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`S3.Client.list_multipart_uploads`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListMultipartUploads>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Bucket='string',
              Delimiter='string',
              EncodingType='url',
              Prefix='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          Name of the bucket to which the multipart upload was initiated.

        :type Delimiter: string
        :param Delimiter:

          Character you use to group keys.

          All keys that contain the same string between the prefix, if specified, and the first occurrence
          of the delimiter after the prefix are grouped under a single result element, ``CommonPrefixes`` .
          If you don't specify the prefix parameter, then the substring starts at the beginning of the key.
          The keys that are grouped under ``CommonPrefixes`` result element are not returned elsewhere in
          the response.

        :type EncodingType: string
        :param EncodingType:

          Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to
          use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some
          characters, such as characters with an ASCII value from 0 to 10. For characters that are not
          supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the
          response.

        :type Prefix: string
        :param Prefix:

          Lists in-progress uploads only for those keys that begin with the specified prefix. You can use
          prefixes to separate a bucket into different grouping of keys. (You can think of using prefix to
          make groups in the same way you'd use a folder in a file system.)

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Bucket': 'string',
                'KeyMarker': 'string',
                'UploadIdMarker': 'string',
                'Prefix': 'string',
                'Delimiter': 'string',
                'MaxUploads': 123,
                'IsTruncated': True|False,
                'Uploads': [
                    {
                        'UploadId': 'string',
                        'Key': 'string',
                        'Initiated': datetime(2015, 1, 1),
                        'StorageClass':
                        'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'
                        |'GLACIER'|'DEEP_ARCHIVE',
                        'Owner': {
                            'DisplayName': 'string',
                            'ID': 'string'
                        },
                        'Initiator': {
                            'ID': 'string',
                            'DisplayName': 'string'
                        }
                    },
                ],
                'CommonPrefixes': [
                    {
                        'Prefix': 'string'
                    },
                ],
                'EncodingType': 'url',
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Bucket** *(string) --*

              Name of the bucket to which the multipart upload was initiated.

            - **KeyMarker** *(string) --*

              The key at or after which the listing began.

            - **UploadIdMarker** *(string) --*

              Upload ID after which listing began.

            - **Prefix** *(string) --*

              When a prefix is provided in the request, this field contains the specified prefix. The
              result contains only keys starting with the specified prefix.

            - **Delimiter** *(string) --*

              Contains the delimiter you specified in the request. If you don't specify a delimiter in your
              request, this element is absent from the response.

            - **MaxUploads** *(integer) --*

              Maximum number of multipart uploads that could have been included in the response.

            - **IsTruncated** *(boolean) --*

              Indicates whether the returned list of multipart uploads is truncated. A value of true
              indicates that the list was truncated. The list can be truncated if the number of multipart
              uploads exceeds the limit allowed or specified by max uploads.

            - **Uploads** *(list) --*

              Container for elements related to a particular multipart upload. A response can contain zero
              or more Upload elements.

              - *(dict) --*

                Container for the MultipartUpload for the Amazon S3 object.

                - **UploadId** *(string) --*

                  Upload ID that identifies the multipart upload.

                - **Key** *(string) --*

                  Key of the object for which the multipart upload was initiated.

                - **Initiated** *(datetime) --*

                  Date and time at which the multipart upload was initiated.

                - **StorageClass** *(string) --*

                  The class of storage used to store the object.

                - **Owner** *(dict) --*

                  Specifies the owner of the object that is part of the multipart upload.

                  - **DisplayName** *(string) --*

                    Container for the display name of the owner

                  - **ID** *(string) --*

                    Container for the ID of the owner

                - **Initiator** *(dict) --*

                  Identifies who initiated the multipart upload.

                  - **ID** *(string) --*

                    If the principal is an AWS account, it provides the Canonical User ID. If the principal
                    is an IAM User, it provides a user ARN value.

                  - **DisplayName** *(string) --*

                    Name of the Principal.

            - **CommonPrefixes** *(list) --*

              If you specify a delimiter in the request, then the result returns each distinct key prefix
              containing the delimiter in a CommonPrefixes element. The distinct key prefixes are returned
              in the Prefix child element.

              - *(dict) --*

                Container for all (if there are any) keys between Prefix and the next occurrence of the
                string specified by a delimiter. CommonPrefixes lists keys that act like subdirectories in
                the directory specified by Prefix. For example, if the prefix is notes/ and the delimiter
                is a slash (/) as in notes/summer/july, the common prefix is notes/summer/.

                - **Prefix** *(string) --*

                  Container for the specified common prefix.

            - **EncodingType** *(string) --*

              Encoding type used by Amazon S3 to encode object keys in the response.

              If you specify ``encoding-type`` request parameter, Amazon S3 includes this element in the
              response, and returns encoded key name values in the following response elements:

               ``Delimiter`` , ``KeyMarker`` , ``Prefix`` , ``NextKeyMarker`` , ``Key`` .

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListObjectVersionsPaginator(Boto3Paginator):
    """
    Paginator for `list_object_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: str = None,
        Prefix: str = None,
        PaginationConfig: ListObjectVersionsPaginatePaginationConfigTypeDef = None,
    ) -> ListObjectVersionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`S3.Client.list_object_versions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListObjectVersions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Bucket='string',
              Delimiter='string',
              EncodingType='url',
              Prefix='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket that contains the objects.

        :type Delimiter: string
        :param Delimiter:

          A delimiter is a character that you specify to group keys. All keys that contain the same string
          between the ``prefix`` and the first occurrence of the delimiter are grouped under a single
          result element in CommonPrefixes. These groups are counted as one result against the max-keys
          limitation. These keys are not returned elsewhere in the response.

        :type EncodingType: string
        :param EncodingType:

          Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to
          use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some
          characters, such as characters with an ASCII value from 0 to 10. For characters that are not
          supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the
          response.

        :type Prefix: string
        :param Prefix:

          Use this parameter to select only those keys that begin with the specified prefix. You can use
          prefixes to separate a bucket into different groupings of keys. (You can think of using prefix to
          make groups in the same way you'd use a folder in a file system.) You can use prefix with
          delimiter to roll up numerous objects into a single result under CommonPrefixes.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'IsTruncated': True|False,
                'KeyMarker': 'string',
                'VersionIdMarker': 'string',
                'Versions': [
                    {
                        'ETag': 'string',
                        'Size': 123,
                        'StorageClass': 'STANDARD',
                        'Key': 'string',
                        'VersionId': 'string',
                        'IsLatest': True|False,
                        'LastModified': datetime(2015, 1, 1),
                        'Owner': {
                            'DisplayName': 'string',
                            'ID': 'string'
                        }
                    },
                ],
                'DeleteMarkers': [
                    {
                        'Owner': {
                            'DisplayName': 'string',
                            'ID': 'string'
                        },
                        'Key': 'string',
                        'VersionId': 'string',
                        'IsLatest': True|False,
                        'LastModified': datetime(2015, 1, 1)
                    },
                ],
                'Name': 'string',
                'Prefix': 'string',
                'Delimiter': 'string',
                'MaxKeys': 123,
                'CommonPrefixes': [
                    {
                        'Prefix': 'string'
                    },
                ],
                'EncodingType': 'url',
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **IsTruncated** *(boolean) --*

              A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the
              search criteria. If your results were truncated, you can make a follow-up paginated request
              using the NextKeyMarker and NextVersionIdMarker response parameters as a starting place in
              another request to return the rest of the results.

            - **KeyMarker** *(string) --*

              Marks the last Key returned in a truncated response.

            - **VersionIdMarker** *(string) --*

              Marks the last version of the Key returned in a truncated response.

            - **Versions** *(list) --*

              Container for version information.

              - *(dict) --*

                The version of an object.

                - **ETag** *(string) --*

                  The entity tag is an MD5 hash of that version of the object

                - **Size** *(integer) --*

                  Size in bytes of the object.

                - **StorageClass** *(string) --*

                  The class of storage used to store the object.

                - **Key** *(string) --*

                  The object key.

                - **VersionId** *(string) --*

                  Version ID of an object.

                - **IsLatest** *(boolean) --*

                  Specifies whether the object is (true) or is not (false) the latest version of an object.

                - **LastModified** *(datetime) --*

                  Date and time the object was last modified.

                - **Owner** *(dict) --*

                  Specifies the Owner of the object.

                  - **DisplayName** *(string) --*

                    Container for the display name of the owner

                  - **ID** *(string) --*

                    Container for the ID of the owner

            - **DeleteMarkers** *(list) --*

              Container for an object that is a delete marker.

              - *(dict) --*

                Information about the delete marker.

                - **Owner** *(dict) --*

                  The account that created the delete marker.>

                  - **DisplayName** *(string) --*

                    Container for the display name of the owner

                  - **ID** *(string) --*

                    Container for the ID of the owner

                - **Key** *(string) --*

                  The object key.

                - **VersionId** *(string) --*

                  Version ID of an object.

                - **IsLatest** *(boolean) --*

                  Specifies whether the object is (true) or is not (false) the latest version of an object.

                - **LastModified** *(datetime) --*

                  Date and time the object was last modified.

            - **Name** *(string) --*

              Bucket owner's name.

            - **Prefix** *(string) --*

              Selects objects that start with the value supplied by this parameter.

            - **Delimiter** *(string) --*

              The delimeter grouping the included keys. A delimiter is a character that you specify to
              group keys. All keys that contain the same string between the prefix and the first occurrence
              of the delimiter are grouped under a single result element in CommonPrefixes. These groups
              are counted as one result against the max-keys limitation. These keys are not returned
              elsewhere in the response.

            - **MaxKeys** *(integer) --*

              Specifies the maximum number of objects to return.

            - **CommonPrefixes** *(list) --*

              All of the keys rolled up into a common prefix count as a single return when calculating the
              number of returns.

              - *(dict) --*

                Container for all (if there are any) keys between Prefix and the next occurrence of the
                string specified by a delimiter. CommonPrefixes lists keys that act like subdirectories in
                the directory specified by Prefix. For example, if the prefix is notes/ and the delimiter
                is a slash (/) as in notes/summer/july, the common prefix is notes/summer/.

                - **Prefix** *(string) --*

                  Container for the specified common prefix.

            - **EncodingType** *(string) --*

              Encoding type used by Amazon S3 to encode object key names in the XML response.

              If you specify encoding-type request parameter, Amazon S3 includes this element in the
              response, and returns encoded key name values in the following response elements:

               ``KeyMarker, NextKeyMarker, Prefix, Key`` , and ``Delimiter`` .

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListObjectsPaginator(Boto3Paginator):
    """
    Paginator for `list_objects`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: str = None,
        Prefix: str = None,
        RequestPayer: str = None,
        PaginationConfig: ListObjectsPaginatePaginationConfigTypeDef = None,
    ) -> ListObjectsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`S3.Client.list_objects`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListObjects>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Bucket='string',
              Delimiter='string',
              EncodingType='url',
              Prefix='string',
              RequestPayer='requester',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket containing the objects.

        :type Delimiter: string
        :param Delimiter:

          A delimiter is a character you use to group keys.

        :type EncodingType: string
        :param EncodingType:

          Requests Amazon S3 to encode the object keys in the response and specifies the encoding method to
          use. An object key may contain any Unicode character; however, XML 1.0 parser cannot parse some
          characters, such as characters with an ASCII value from 0 to 10. For characters that are not
          supported in XML 1.0, you can add this parameter to request that Amazon S3 encode the keys in the
          response.

        :type Prefix: string
        :param Prefix:

          Limits the response to keys that begin with the specified prefix.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the list objects request.
          Bucket owners need not specify this parameter in their requests.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'IsTruncated': True|False,
                'Marker': 'string',
                'NextMarker': 'string',
                'Contents': [
                    {
                        'Key': 'string',
                        'LastModified': datetime(2015, 1, 1),
                        'ETag': 'string',
                        'Size': 123,
                        'StorageClass':
                        'STANDARD'|'REDUCED_REDUNDANCY'|'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'
                        |'INTELLIGENT_TIERING'|'DEEP_ARCHIVE',
                        'Owner': {
                            'DisplayName': 'string',
                            'ID': 'string'
                        }
                    },
                ],
                'Name': 'string',
                'Prefix': 'string',
                'Delimiter': 'string',
                'MaxKeys': 123,
                'CommonPrefixes': [
                    {
                        'Prefix': 'string'
                    },
                ],
                'EncodingType': 'url',
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **IsTruncated** *(boolean) --*

              A flag that indicates whether or not Amazon S3 returned all of the results that satisfied the
              search criteria.

            - **Marker** *(string) --*

              Indicates where in the bucket listing begins. Marker is included in the response if it was
              sent with the request.

            - **NextMarker** *(string) --*

              When response is truncated (the IsTruncated element value in the response is true), you can
              use the key name in this field as marker in the subsequent request to get next set of
              objects. Amazon S3 lists objects in alphabetical order Note: This element is returned only if
              you have delimiter request parameter specified. If response does not include the NextMaker
              and it is truncated, you can use the value of the last Key in the response as the marker in
              the subsequent request to get the next set of object keys.

            - **Contents** *(list) --*

              Metadata about each object returned.

              - *(dict) --*

                An object consists of data and its descriptive metadata.

                - **Key** *(string) --*

                  The name that you assign to an object. You use the object key to retrieve the object.

                - **LastModified** *(datetime) --*

                  The date the Object was Last Modified

                - **ETag** *(string) --*

                  The entity tag is an MD5 hash of the object. ETag reflects only changes to the contents
                  of an object, not its metadata.

                - **Size** *(integer) --*

                  Size in bytes of the object

                - **StorageClass** *(string) --*

                  The class of storage used to store the object.

                - **Owner** *(dict) --*

                  The owner of the object

                  - **DisplayName** *(string) --*

                    Container for the display name of the owner

                  - **ID** *(string) --*

                    Container for the ID of the owner

            - **Name** *(string) --*

              Name of the bucket.

            - **Prefix** *(string) --*

              Keys that begin with the indicated prefix.

            - **Delimiter** *(string) --*

              Causes keys that contain the same string between the prefix and the first occurrence of the
              delimiter to be rolled up into a single result element in the CommonPrefixes collection.
              These rolled-up keys are not returned elsewhere in the response. Each rolled-up result counts
              as only one return against the MaxKeys value.

            - **MaxKeys** *(integer) --*

              The maximum number of keys returned in the response body.

            - **CommonPrefixes** *(list) --*

              All of the keys rolled up in a common prefix count as a single return when calculating the
              number of returns.

              A response can contain CommonPrefixes only if you specify a delimiter.

              CommonPrefixes contains all (if there are any) keys between Prefix and the next occurrence of
              the string specified by the delimiter.

              CommonPrefixes lists keys that act like subdirectories in the directory specified by Prefix.

              For example, if the prefix is notes/ and the delimiter is a slash (/) as in
              notes/summer/july, the common prefix is notes/summer/. All of the keys that roll up into a
              common prefix count as a single return when calculating the number of returns.

              - *(dict) --*

                Container for all (if there are any) keys between Prefix and the next occurrence of the
                string specified by a delimiter. CommonPrefixes lists keys that act like subdirectories in
                the directory specified by Prefix. For example, if the prefix is notes/ and the delimiter
                is a slash (/) as in notes/summer/july, the common prefix is notes/summer/.

                - **Prefix** *(string) --*

                  Container for the specified common prefix.

            - **EncodingType** *(string) --*

              Encoding type used by Amazon S3 to encode object keys in the response.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListObjectsV2Paginator(Boto3Paginator):
    """
    Paginator for `list_objects_v2`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Bucket: str,
        Delimiter: str = None,
        EncodingType: str = None,
        Prefix: str = None,
        FetchOwner: bool = None,
        StartAfter: str = None,
        RequestPayer: str = None,
        PaginationConfig: ListObjectsV2PaginatePaginationConfigTypeDef = None,
    ) -> ListObjectsV2PaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`S3.Client.list_objects_v2`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListObjectsV2>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Bucket='string',
              Delimiter='string',
              EncodingType='url',
              Prefix='string',
              FetchOwner=True|False,
              StartAfter='string',
              RequestPayer='requester',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          Name of the bucket to list.

        :type Delimiter: string
        :param Delimiter:

          A delimiter is a character you use to group keys.

        :type EncodingType: string
        :param EncodingType:

          Encoding type used by Amazon S3 to encode object keys in the response.

        :type Prefix: string
        :param Prefix:

          Limits the response to keys that begin with the specified prefix.

        :type FetchOwner: boolean
        :param FetchOwner:

          The owner field is not present in listV2 by default, if you want to return owner field with each
          key in the result then set the fetch owner field to true

        :type StartAfter: string
        :param StartAfter:

          StartAfter is where you want Amazon S3 to start listing from. Amazon S3 starts listing after this
          specified key. StartAfter can be any key in the bucket.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the list objects request in
          V2 style. Bucket owners need not specify this parameter in their requests.

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'IsTruncated': True|False,
                'Contents': [
                    {
                        'Key': 'string',
                        'LastModified': datetime(2015, 1, 1),
                        'ETag': 'string',
                        'Size': 123,
                        'StorageClass':
                        'STANDARD'|'REDUCED_REDUNDANCY'|'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'
                        |'INTELLIGENT_TIERING'|'DEEP_ARCHIVE',
                        'Owner': {
                            'DisplayName': 'string',
                            'ID': 'string'
                        }
                    },
                ],
                'Name': 'string',
                'Prefix': 'string',
                'Delimiter': 'string',
                'MaxKeys': 123,
                'CommonPrefixes': [
                    {
                        'Prefix': 'string'
                    },
                ],
                'EncodingType': 'url',
                'KeyCount': 123,
                'ContinuationToken': 'string',
                'StartAfter': 'string',
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **IsTruncated** *(boolean) --*

              Set to false if all of the results were returned. Set to true if more keys are available to
              return. If the number of results exceeds that specified by MaxKeys, all of the results might
              not be returned.

            - **Contents** *(list) --*

              Metadata about each object returned.

              - *(dict) --*

                An object consists of data and its descriptive metadata.

                - **Key** *(string) --*

                  The name that you assign to an object. You use the object key to retrieve the object.

                - **LastModified** *(datetime) --*

                  The date the Object was Last Modified

                - **ETag** *(string) --*

                  The entity tag is an MD5 hash of the object. ETag reflects only changes to the contents
                  of an object, not its metadata.

                - **Size** *(integer) --*

                  Size in bytes of the object

                - **StorageClass** *(string) --*

                  The class of storage used to store the object.

                - **Owner** *(dict) --*

                  The owner of the object

                  - **DisplayName** *(string) --*

                    Container for the display name of the owner

                  - **ID** *(string) --*

                    Container for the ID of the owner

            - **Name** *(string) --*

              Name of the bucket.

            - **Prefix** *(string) --*

              Keys that begin with the indicated prefix.

            - **Delimiter** *(string) --*

              Causes keys that contain the same string between the prefix and the first occurrence of the
              delimiter to be rolled up into a single result element in the CommonPrefixes collection.
              These rolled-up keys are not returned elsewhere in the response. Each rolled-up result counts
              as only one return against the MaxKeys value.

            - **MaxKeys** *(integer) --*

              Sets the maximum number of keys returned in the response. The response might contain fewer
              keys but will never contain more.

            - **CommonPrefixes** *(list) --*

              All of the keys rolled up into a common prefix count as a single return when calculating the
              number of returns.

              A response can contain ``CommonPrefixes`` only if you specify a delimiter.

               ``CommonPrefixes`` contains all (if there are any) keys between ``Prefix`` and the next
               occurrence of the string specified by a delimiter.

               ``CommonPrefixes`` lists keys that act like subdirectories in the directory specified by
               ``Prefix`` .

              For example, if the prefix is ``notes/`` and the delimiter is a slash (``/`` ) as in
              ``notes/summer/july`` , the common prefix is ``notes/summer/`` . All of the keys that roll up
              into a common prefix count as a single return when calculating the number of returns.

              - *(dict) --*

                Container for all (if there are any) keys between Prefix and the next occurrence of the
                string specified by a delimiter. CommonPrefixes lists keys that act like subdirectories in
                the directory specified by Prefix. For example, if the prefix is notes/ and the delimiter
                is a slash (/) as in notes/summer/july, the common prefix is notes/summer/.

                - **Prefix** *(string) --*

                  Container for the specified common prefix.

            - **EncodingType** *(string) --*

              Encoding type used by Amazon S3 to encode object key names in the XML response.

              If you specify the encoding-type request parameter, Amazon S3 includes this element in the
              response, and returns encoded key name values in the following response elements:

               ``Delimiter, Prefix, Key,`` and ``StartAfter`` .

            - **KeyCount** *(integer) --*

              KeyCount is the number of keys returned with this request. KeyCount will always be less than
              equals to MaxKeys field. Say you ask for 50 keys, your result will include less than equals
              50 keys

            - **ContinuationToken** *(string) --*

              If ContinuationToken was sent with the request, it is included in the response.

            - **StartAfter** *(string) --*

              If StartAfter was sent with the request, it is included in the response.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListPartsPaginator(Boto3Paginator):
    """
    Paginator for `list_parts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Bucket: str,
        Key: str,
        UploadId: str,
        RequestPayer: str = None,
        PaginationConfig: ListPartsPaginatePaginationConfigTypeDef = None,
    ) -> ListPartsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`S3.Client.list_parts`.

        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/ListParts>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Bucket='string',
              Key='string',
              UploadId='string',
              RequestPayer='requester',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          Name of the bucket to which the parts are being uploaded.->

        :type Key: string
        :param Key: **[REQUIRED]**

          Object key for which the multipart upload was initiated.

        :type UploadId: string
        :param UploadId: **[REQUIRED]**

          Upload ID identifying the multipart upload whose parts are being listed.

        :type RequestPayer: string
        :param RequestPayer:

          Confirms that the requester knows that she or he will be charged for the request. Bucket owners
          need not specify this parameter in their requests. Documentation on downloading objects from
          requester pays buckets can be found at
          http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html

        :type PaginationConfig: dict
        :param PaginationConfig:

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

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AbortDate': datetime(2015, 1, 1),
                'AbortRuleId': 'string',
                'Bucket': 'string',
                'Key': 'string',
                'UploadId': 'string',
                'PartNumberMarker': 123,
                'MaxParts': 123,
                'IsTruncated': True|False,
                'Parts': [
                    {
                        'PartNumber': 123,
                        'LastModified': datetime(2015, 1, 1),
                        'ETag': 'string',
                        'Size': 123
                    },
                ],
                'Initiator': {
                    'ID': 'string',
                    'DisplayName': 'string'
                },
                'Owner': {
                    'DisplayName': 'string',
                    'ID': 'string'
                },
                'StorageClass':
                'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'GLACIER'
                |'DEEP_ARCHIVE',
                'RequestCharged': 'requester',
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **AbortDate** *(datetime) --*

              If the bucket has a lifecycle rule configured with an action to abort incomplete multipart
              uploads and the prefix in the lifecycle rule matches the object name in the request, then the
              response includes this header indicating when the initiated multipart upload will become
              eligible for abort operation. For more information, see `Aborting Incomplete Multipart
              Uploads Using a Bucket Lifecycle Policy
              <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config>`__
              .

              The response will also include the x-amz-abort-rule-id header that will provide the ID of the
              lifecycle configuration rule that defines this action.

            - **AbortRuleId** *(string) --*

              This header is returned along with the x-amz-abort-date header. It identifies applicable
              lifecycle configuration rule that defines the action to abort incomplete multipart uploads.

            - **Bucket** *(string) --*

              Name of the bucket to which the multipart upload was initiated.

            - **Key** *(string) --*

              Object key for which the multipart upload was initiated.

            - **UploadId** *(string) --*

              Upload ID identifying the multipart upload whose parts are being listed.

            - **PartNumberMarker** *(integer) --*

              When a list is truncated, this element specifies the last part in the list, as well as the
              value to use for the part-number-marker request parameter in a subsequent request.

            - **MaxParts** *(integer) --*

              Maximum number of parts that were allowed in the response.

            - **IsTruncated** *(boolean) --*

              Indicates whether the returned list of parts is truncated. A true value indicates that the
              list was truncated. A list can be truncated if the number of parts exceeds the limit returned
              in the MaxParts element.

            - **Parts** *(list) --*

              Container for elements related to a particular part. A response can contain zero or more Part
              elements.

              - *(dict) --*

                Container for elements related to a part.

                - **PartNumber** *(integer) --*

                  Part number identifying the part. This is a positive integer between 1 and 10,000.

                - **LastModified** *(datetime) --*

                  Date and time at which the part was uploaded.

                - **ETag** *(string) --*

                  Entity tag returned when the part was uploaded.

                - **Size** *(integer) --*

                  Size in bytes of the uploaded part data.

            - **Initiator** *(dict) --*

              Container element that identifies who initiated the multipart upload. If the initiator is an
              AWS account, this element provides the same information as the Owner element. If the
              initiator is an IAM User, then this element provides the user ARN and display name.

              - **ID** *(string) --*

                If the principal is an AWS account, it provides the Canonical User ID. If the principal is
                an IAM User, it provides a user ARN value.

              - **DisplayName** *(string) --*

                Name of the Principal.

            - **Owner** *(dict) --*

              Container element that identifies the object owner, after the object is created. If multipart
              upload is initiated by an IAM user, this element provides the parent account ID and display
              name.

              - **DisplayName** *(string) --*

                Container for the display name of the owner

              - **ID** *(string) --*

                Container for the ID of the owner

            - **StorageClass** *(string) --*

              Class of storage (STANDARD or REDUCED_REDUNDANCY) used to store the uploaded object.

            - **RequestCharged** *(string) --*

              If present, indicates that the requester was successfully charged for the request.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """

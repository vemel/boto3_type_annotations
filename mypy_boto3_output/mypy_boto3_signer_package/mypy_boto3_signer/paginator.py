"Main interface for signer Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_signer.type_defs import (
    ListSigningJobsPaginatePaginationConfigTypeDef,
    ListSigningJobsPaginateResponseTypeDef,
    ListSigningPlatformsPaginatePaginationConfigTypeDef,
    ListSigningPlatformsPaginateResponseTypeDef,
    ListSigningProfilesPaginatePaginationConfigTypeDef,
    ListSigningProfilesPaginateResponseTypeDef,
)


__all__ = (
    "ListSigningJobsPaginator",
    "ListSigningPlatformsPaginator",
    "ListSigningProfilesPaginator",
)


class ListSigningJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_signing_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        status: str = None,
        platformId: str = None,
        requestedBy: str = None,
        PaginationConfig: ListSigningJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListSigningJobsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`signer.Client.list_signing_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/signer-2017-08-25/ListSigningJobs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              status='InProgress'|'Failed'|'Succeeded',
              platformId='string',
              requestedBy='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type status: string
        :param status:

          A status value with which to filter your results.

        :type platformId: string
        :param platformId:

          The ID of microcontroller platform that you specified for the distribution of your code image.

        :type requestedBy: string
        :param requestedBy:

          The IAM principal that requested the signing job.

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
                'jobs': [
                    {
                        'jobId': 'string',
                        'source': {
                            's3': {
                                'bucketName': 'string',
                                'key': 'string',
                                'version': 'string'
                            }
                        },
                        'signedObject': {
                            's3': {
                                'bucketName': 'string',
                                'key': 'string'
                            }
                        },
                        'signingMaterial': {
                            'certificateArn': 'string'
                        },
                        'createdAt': datetime(2015, 1, 1),
                        'status': 'InProgress'|'Failed'|'Succeeded'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **jobs** *(list) --*

              A list of your signing jobs.

              - *(dict) --*

                Contains information about a signing job.

                - **jobId** *(string) --*

                  The ID of the signing job.

                - **source** *(dict) --*

                  A ``Source`` that contains information about a signing job's code image source.

                  - **s3** *(dict) --*

                    The ``S3Source`` object.

                    - **bucketName** *(string) --*

                      Name of the S3 bucket.

                    - **key** *(string) --*

                      Key name of the bucket object that contains your unsigned code.

                    - **version** *(string) --*

                      Version of your source image in your version enabled S3 bucket.

                - **signedObject** *(dict) --*

                  A ``SignedObject`` structure that contains information about a signing job's signed code
                  image.

                  - **s3** *(dict) --*

                    The ``S3SignedObject`` .

                    - **bucketName** *(string) --*

                      Name of the S3 bucket.

                    - **key** *(string) --*

                      Key name that uniquely identifies a signed code image in your bucket.

                - **signingMaterial** *(dict) --*

                  A ``SigningMaterial`` object that contains the Amazon Resource Name (ARN) of the
                  certificate used for the signing job.

                  - **certificateArn** *(string) --*

                    The Amazon Resource Name (ARN) of the certificates that is used to sign your code.

                - **createdAt** *(datetime) --*

                  The date and time that the signing job was created.

                - **status** *(string) --*

                  The status of the signing job.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListSigningPlatformsPaginator(Boto3Paginator):
    """
    Paginator for `list_signing_platforms`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        category: str = None,
        partner: str = None,
        target: str = None,
        PaginationConfig: ListSigningPlatformsPaginatePaginationConfigTypeDef = None,
    ) -> ListSigningPlatformsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`signer.Client.list_signing_platforms`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/signer-2017-08-25/ListSigningPlatforms>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              category='string',
              partner='string',
              target='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type category: string
        :param category:

          The category type of a signing platform.

        :type partner: string
        :param partner:

          Any partner entities connected to a signing platform.

        :type target: string
        :param target:

          The validation template that is used by the target signing platform.

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
                'platforms': [
                    {
                        'platformId': 'string',
                        'displayName': 'string',
                        'partner': 'string',
                        'target': 'string',
                        'category': 'AWSIoT',
                        'signingConfiguration': {
                            'encryptionAlgorithmOptions': {
                                'allowedValues': [
                                    'RSA'|'ECDSA',
                                ],
                                'defaultValue': 'RSA'|'ECDSA'
                            },
                            'hashAlgorithmOptions': {
                                'allowedValues': [
                                    'SHA1'|'SHA256',
                                ],
                                'defaultValue': 'SHA1'|'SHA256'
                            }
                        },
                        'signingImageFormat': {
                            'supportedFormats': [
                                'JSON',
                            ],
                            'defaultFormat': 'JSON'
                        },
                        'maxSizeInMB': 123
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **platforms** *(list) --*

              A list of all platforms that match the request parameters.

              - *(dict) --*

                Contains information about the signing configurations and parameters that is used to
                perform a code signing job.

                - **platformId** *(string) --*

                  The ID of a code signing; platform.

                - **displayName** *(string) --*

                  The display name of a code signing platform.

                - **partner** *(string) --*

                  Any partner entities linked to a code signing platform.

                - **target** *(string) --*

                  The types of targets that can be signed by a code signing platform.

                - **category** *(string) --*

                  The category of a code signing platform.

                - **signingConfiguration** *(dict) --*

                  The configuration of a code signing platform. This includes the designated hash algorithm
                  and encryption algorithm of a signing platform.

                  - **encryptionAlgorithmOptions** *(dict) --*

                    The encryption algorithm options that are available for a code signing job.

                    - **allowedValues** *(list) --*

                      The set of accepted encryption algorithms that are allowed in a code signing job.

                      - *(string) --*

                    - **defaultValue** *(string) --*

                      The default encryption algorithm that is used by a code signing job.

                  - **hashAlgorithmOptions** *(dict) --*

                    The hash algorithm options that are available for a a code signing job.

                    - **allowedValues** *(list) --*

                      The set of accepted hash algorithms allowed in a code signing job.

                      - *(string) --*

                    - **defaultValue** *(string) --*

                      The default hash algorithm that is used in a code signing job.

                - **signingImageFormat** *(dict) --*

                  The image format of a code signing platform or profile.

                  - **supportedFormats** *(list) --*

                    The supported formats of a code signing signing image.

                    - *(string) --*

                  - **defaultFormat** *(string) --*

                    The default format of a code signing signing image.

                - **maxSizeInMB** *(integer) --*

                  The maximum size (in MB) of code that can be signed by a code signing platform.

            - **NextToken** *(string) --*

              A token to resume pagination.

        """


class ListSigningProfilesPaginator(Boto3Paginator):
    """
    Paginator for `list_signing_profiles`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        includeCanceled: bool = None,
        PaginationConfig: ListSigningProfilesPaginatePaginationConfigTypeDef = None,
    ) -> ListSigningProfilesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`signer.Client.list_signing_profiles`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/signer-2017-08-25/ListSigningProfiles>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              includeCanceled=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type includeCanceled: boolean
        :param includeCanceled:

          Designates whether to include profiles with the status of ``CANCELED`` .

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
                'profiles': [
                    {
                        'profileName': 'string',
                        'signingMaterial': {
                            'certificateArn': 'string'
                        },
                        'platformId': 'string',
                        'signingParameters': {
                            'string': 'string'
                        },
                        'status': 'Active'|'Canceled',
                        'arn': 'string',
                        'tags': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **profiles** *(list) --*

              A list of profiles that are available in the AWS account. This includes profiles with the
              status of ``CANCELED`` if the ``includeCanceled`` parameter is set to ``true`` .

              - *(dict) --*

                Contains information about the ACM certificates and code signing configuration parameters
                that can be used by a given code signing user.

                - **profileName** *(string) --*

                  The name of the signing profile.

                - **signingMaterial** *(dict) --*

                  The ACM certificate that is available for use by a signing profile.

                  - **certificateArn** *(string) --*

                    The Amazon Resource Name (ARN) of the certificates that is used to sign your code.

                - **platformId** *(string) --*

                  The ID of a platform that is available for use by a signing profile.

                - **signingParameters** *(dict) --*

                  The parameters that are available for use by a code signing user.

                  - *(string) --*

                    - *(string) --*

                - **status** *(string) --*

                  The status of a code signing profile.

                - **arn** *(string) --*

                  Amazon Resource Name (ARN) for the signing profile.

                - **tags** *(dict) --*

                  A list of tags associated with the signing profile.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.

        """

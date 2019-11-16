"Main interface for snowball Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_snowball.type_defs import (
    DescribeAddressesPaginatePaginationConfigTypeDef,
    DescribeAddressesPaginateResponseTypeDef,
    ListClusterJobsPaginatePaginationConfigTypeDef,
    ListClusterJobsPaginateResponseTypeDef,
    ListClustersPaginatePaginationConfigTypeDef,
    ListClustersPaginateResponseTypeDef,
    ListCompatibleImagesPaginatePaginationConfigTypeDef,
    ListCompatibleImagesPaginateResponseTypeDef,
    ListJobsPaginatePaginationConfigTypeDef,
    ListJobsPaginateResponseTypeDef,
)


__all__ = (
    "DescribeAddressesPaginator",
    "ListClusterJobsPaginator",
    "ListClustersPaginator",
    "ListCompatibleImagesPaginator",
    "ListJobsPaginator",
)


class DescribeAddressesPaginator(Boto3Paginator):
    """
    Paginator for `describe_addresses`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: DescribeAddressesPaginatePaginationConfigTypeDef = None
    ) -> DescribeAddressesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Snowball.Client.describe_addresses`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/DescribeAddresses>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
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
                'Addresses': [
                    {
                        'AddressId': 'string',
                        'Name': 'string',
                        'Company': 'string',
                        'Street1': 'string',
                        'Street2': 'string',
                        'Street3': 'string',
                        'City': 'string',
                        'StateOrProvince': 'string',
                        'PrefectureOrDistrict': 'string',
                        'Landmark': 'string',
                        'Country': 'string',
                        'PostalCode': 'string',
                        'PhoneNumber': 'string',
                        'IsRestricted': True|False
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Addresses** *(list) --*

              The Snowball shipping addresses that were created for this account.

              - *(dict) --*

                The address that you want the Snowball or Snowballs associated with a specific job to be
                shipped to. Addresses are validated at the time of creation. The address you provide must
                be located within the serviceable area of your region. Although no individual elements of
                the ``Address`` are required, if the address is invalid or unsupported, then an exception
                is thrown.

                - **AddressId** *(string) --*

                  The unique ID for an address.

                - **Name** *(string) --*

                  The name of a person to receive a Snowball at an address.

                - **Company** *(string) --*

                  The name of the company to receive a Snowball at an address.

                - **Street1** *(string) --*

                  The first line in a street address that a Snowball is to be delivered to.

                - **Street2** *(string) --*

                  The second line in a street address that a Snowball is to be delivered to.

                - **Street3** *(string) --*

                  The third line in a street address that a Snowball is to be delivered to.

                - **City** *(string) --*

                  The city in an address that a Snowball is to be delivered to.

                - **StateOrProvince** *(string) --*

                  The state or province in an address that a Snowball is to be delivered to.

                - **PrefectureOrDistrict** *(string) --*

                  This field is no longer used and the value is ignored.

                - **Landmark** *(string) --*

                  This field is no longer used and the value is ignored.

                - **Country** *(string) --*

                  The country in an address that a Snowball is to be delivered to.

                - **PostalCode** *(string) --*

                  The postal code in an address that a Snowball is to be delivered to.

                - **PhoneNumber** *(string) --*

                  The phone number associated with an address that a Snowball is to be delivered to.

                - **IsRestricted** *(boolean) --*

                  If the address you are creating is a primary address, then set this option to true. This
                  field is not supported in most regions.

        """


class ListClusterJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_cluster_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ClusterId: str,
        PaginationConfig: ListClusterJobsPaginatePaginationConfigTypeDef = None,
    ) -> ListClusterJobsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Snowball.Client.list_cluster_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/ListClusterJobs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ClusterId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]**

          The 39-character ID for the cluster that you want to list, for example
          ``CID123e4567-e89b-12d3-a456-426655440000`` .

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
                'JobListEntries': [
                    {
                        'JobId': 'string',
                        'JobState':
                        'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'
                        |'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'
                        |'Cancelled'|'Listing'|'Pending',
                        'IsMaster': True|False,
                        'JobType': 'IMPORT'|'EXPORT'|'LOCAL_USE',
                        'SnowballType': 'STANDARD'|'EDGE'|'EDGE_C'|'EDGE_CG',
                        'CreationDate': datetime(2015, 1, 1),
                        'Description': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **JobListEntries** *(list) --*

              Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
              whether the job is a job part, in the case of export jobs.

              - *(dict) --*

                Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
                whether the job is a job part, in the case of an export job.

                - **JobId** *(string) --*

                  The automatically generated ID for a job, for example
                  ``JID123e4567-e89b-12d3-a456-426655440000`` .

                - **JobState** *(string) --*

                  The current state of this job.

                - **IsMaster** *(boolean) --*

                  A value that indicates that this job is a master job. A master job represents a
                  successful request to create an export job. Master jobs aren't associated with any
                  Snowballs. Instead, each master job will have at least one job part, and each job part is
                  associated with a Snowball. It might take some time before the job parts associated with
                  a particular master job are listed, because they are created after the master job is
                  created.

                - **JobType** *(string) --*

                  The type of job.

                - **SnowballType** *(string) --*

                  The type of device used with this job.

                - **CreationDate** *(datetime) --*

                  The creation date for this job.

                - **Description** *(string) --*

                  The optional description of this specific job, for example ``Important Photos
                  2016-08-11`` .

        """


class ListClustersPaginator(Boto3Paginator):
    """
    Paginator for `list_clusters`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListClustersPaginatePaginationConfigTypeDef = None
    ) -> ListClustersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Snowball.Client.list_clusters`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/ListClusters>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
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
                'ClusterListEntries': [
                    {
                        'ClusterId': 'string',
                        'ClusterState': 'AwaitingQuorum'|'Pending'|'InUse'|'Complete'|'Cancelled',
                        'CreationDate': datetime(2015, 1, 1),
                        'Description': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ClusterListEntries** *(list) --*

              Each ``ClusterListEntry`` object contains a cluster's state, a cluster's ID, and other
              important status information.

              - *(dict) --*

                Contains a cluster's state, a cluster's ID, and other important information.

                - **ClusterId** *(string) --*

                  The 39-character ID for the cluster that you want to list, for example
                  ``CID123e4567-e89b-12d3-a456-426655440000`` .

                - **ClusterState** *(string) --*

                  The current state of this cluster. For information about the state of a specific node,
                  see  JobListEntry$JobState .

                - **CreationDate** *(datetime) --*

                  The creation date for this cluster.

                - **Description** *(string) --*

                  Defines an optional description of the cluster, for example ``Environmental Data
                  Cluster-01`` .

        """


class ListCompatibleImagesPaginator(Boto3Paginator):
    """
    Paginator for `list_compatible_images`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: ListCompatibleImagesPaginatePaginationConfigTypeDef = None,
    ) -> ListCompatibleImagesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Snowball.Client.list_compatible_images`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/ListCompatibleImages>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
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
                'CompatibleImages': [
                    {
                        'AmiId': 'string',
                        'Name': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **CompatibleImages** *(list) --*

              A JSON-formatted object that describes a compatible AMI, including the ID and name for a
              Snowball Edge AMI.

              - *(dict) --*

                A JSON-formatted object that describes a compatible Amazon Machine Image (AMI), including
                the ID and name for a Snowball Edge AMI. This AMI is compatible with the device's physical
                hardware requirements, and it should be able to be run in an SBE1 instance on the device.

                - **AmiId** *(string) --*

                  The unique identifier for an individual Snowball Edge AMI.

                - **Name** *(string) --*

                  The optional name of a compatible image.

        """


class ListJobsPaginator(Boto3Paginator):
    """
    Paginator for `list_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListJobsPaginatePaginationConfigTypeDef = None
    ) -> ListJobsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from :py:meth:`Snowball.Client.list_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/ListJobs>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
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
                'JobListEntries': [
                    {
                        'JobId': 'string',
                        'JobState':
                        'New'|'PreparingAppliance'|'PreparingShipment'|'InTransitToCustomer'|'WithCustomer'
                        |'InTransitToAWS'|'WithAWSSortingFacility'|'WithAWS'|'InProgress'|'Complete'
                        |'Cancelled'|'Listing'|'Pending',
                        'IsMaster': True|False,
                        'JobType': 'IMPORT'|'EXPORT'|'LOCAL_USE',
                        'SnowballType': 'STANDARD'|'EDGE'|'EDGE_C'|'EDGE_CG',
                        'CreationDate': datetime(2015, 1, 1),
                        'Description': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **JobListEntries** *(list) --*

              Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
              whether the job is a job part, in the case of export jobs.

              - *(dict) --*

                Each ``JobListEntry`` object contains a job's state, a job's ID, and a value that indicates
                whether the job is a job part, in the case of an export job.

                - **JobId** *(string) --*

                  The automatically generated ID for a job, for example
                  ``JID123e4567-e89b-12d3-a456-426655440000`` .

                - **JobState** *(string) --*

                  The current state of this job.

                - **IsMaster** *(boolean) --*

                  A value that indicates that this job is a master job. A master job represents a
                  successful request to create an export job. Master jobs aren't associated with any
                  Snowballs. Instead, each master job will have at least one job part, and each job part is
                  associated with a Snowball. It might take some time before the job parts associated with
                  a particular master job are listed, because they are created after the master job is
                  created.

                - **JobType** *(string) --*

                  The type of job.

                - **SnowballType** *(string) --*

                  The type of device used with this job.

                - **CreationDate** *(datetime) --*

                  The creation date for this job.

                - **Description** *(string) --*

                  The optional description of this specific job, for example ``Important Photos
                  2016-08-11`` .

        """

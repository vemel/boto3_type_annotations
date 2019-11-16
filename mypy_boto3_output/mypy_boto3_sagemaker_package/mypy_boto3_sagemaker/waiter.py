"Main interface for sagemaker Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_sagemaker.type_defs import (
    EndpointDeletedWaitWaiterConfigTypeDef,
    EndpointInServiceWaitWaiterConfigTypeDef,
    NotebookInstanceDeletedWaitWaiterConfigTypeDef,
    NotebookInstanceInServiceWaitWaiterConfigTypeDef,
    NotebookInstanceStoppedWaitWaiterConfigTypeDef,
    TrainingJobCompletedOrStoppedWaitWaiterConfigTypeDef,
    TransformJobCompletedOrStoppedWaitWaiterConfigTypeDef,
)


__all__ = (
    "EndpointDeletedWaiter",
    "EndpointInServiceWaiter",
    "NotebookInstanceDeletedWaiter",
    "NotebookInstanceInServiceWaiter",
    "NotebookInstanceStoppedWaiter",
    "TrainingJobCompletedOrStoppedWaiter",
    "TransformJobCompletedOrStoppedWaiter",
)


class EndpointDeletedWaiter(Boto3Waiter):
    """
    Waiter for `endpoint_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        EndpointName: str,
        WaiterConfig: EndpointDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`SageMaker.Client.describe_endpoint` every 30 seconds until a successful state is
        reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeEndpoint>`_

        **Request Syntax**
        ::

          waiter.wait(
              EndpointName='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]**

          The name of the endpoint.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60

        :returns: None
        """


class EndpointInServiceWaiter(Boto3Waiter):
    """
    Waiter for `endpoint_in_service` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        EndpointName: str,
        WaiterConfig: EndpointInServiceWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`SageMaker.Client.describe_endpoint` every 30 seconds until a successful state is
        reached. An error is returned after 120 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeEndpoint>`_

        **Request Syntax**
        ::

          waiter.wait(
              EndpointName='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type EndpointName: string
        :param EndpointName: **[REQUIRED]**

          The name of the endpoint.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 120

        :returns: None
        """


class NotebookInstanceDeletedWaiter(Boto3Waiter):
    """
    Waiter for `notebook_instance_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        NotebookInstanceName: str,
        WaiterConfig: NotebookInstanceDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`SageMaker.Client.describe_notebook_instance` every 30 seconds until a successful
        state is reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeNotebookInstance>`_

        **Request Syntax**
        ::

          waiter.wait(
              NotebookInstanceName='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]**

          The name of the notebook instance that you want information about.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60

        :returns: None
        """


class NotebookInstanceInServiceWaiter(Boto3Waiter):
    """
    Waiter for `notebook_instance_in_service` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        NotebookInstanceName: str,
        WaiterConfig: NotebookInstanceInServiceWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`SageMaker.Client.describe_notebook_instance` every 30 seconds until a successful
        state is reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeNotebookInstance>`_

        **Request Syntax**
        ::

          waiter.wait(
              NotebookInstanceName='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]**

          The name of the notebook instance that you want information about.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60

        :returns: None
        """


class NotebookInstanceStoppedWaiter(Boto3Waiter):
    """
    Waiter for `notebook_instance_stopped` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        NotebookInstanceName: str,
        WaiterConfig: NotebookInstanceStoppedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`SageMaker.Client.describe_notebook_instance` every 30 seconds until a successful
        state is reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeNotebookInstance>`_

        **Request Syntax**
        ::

          waiter.wait(
              NotebookInstanceName='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type NotebookInstanceName: string
        :param NotebookInstanceName: **[REQUIRED]**

          The name of the notebook instance that you want information about.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60

        :returns: None
        """


class TrainingJobCompletedOrStoppedWaiter(Boto3Waiter):
    """
    Waiter for `training_job_completed_or_stopped` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        TrainingJobName: str,
        WaiterConfig: TrainingJobCompletedOrStoppedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`SageMaker.Client.describe_training_job` every 120 seconds until a successful state
        is reached. An error is returned after 180 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeTrainingJob>`_

        **Request Syntax**
        ::

          waiter.wait(
              TrainingJobName='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type TrainingJobName: string
        :param TrainingJobName: **[REQUIRED]**

          The name of the training job.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 120

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 180

        :returns: None
        """


class TransformJobCompletedOrStoppedWaiter(Boto3Waiter):
    """
    Waiter for `transform_job_completed_or_stopped` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        TransformJobName: str,
        WaiterConfig: TransformJobCompletedOrStoppedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`SageMaker.Client.describe_transform_job` every 60 seconds until a successful state
        is reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeTransformJob>`_

        **Request Syntax**
        ::

          waiter.wait(
              TransformJobName='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type TransformJobName: string
        :param TransformJobName: **[REQUIRED]**

          The name of the transform job that you want to view details of.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 60

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60

        :returns: None
        """

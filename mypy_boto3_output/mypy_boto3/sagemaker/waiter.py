from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.waiter import Waiter


class EndpointDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, EndpointName: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass


class EndpointInService(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, EndpointName: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass


class NotebookInstanceDeleted(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self, NotebookInstanceName: str, WaiterConfig: Dict[str, Any] = None
    ) -> None:
        pass


class NotebookInstanceInService(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self, NotebookInstanceName: str, WaiterConfig: Dict[str, Any] = None
    ) -> None:
        pass


class NotebookInstanceStopped(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self, NotebookInstanceName: str, WaiterConfig: Dict[str, Any] = None
    ) -> None:
        pass


class TrainingJobCompletedOrStopped(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, TrainingJobName: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass


class TransformJobCompletedOrStopped(Waiter):

    # pylint: disable=arguments-differ
    def wait(self, TransformJobName: str, WaiterConfig: Dict[str, Any] = None) -> None:
        pass

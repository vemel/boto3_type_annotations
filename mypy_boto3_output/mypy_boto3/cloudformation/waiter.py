from __future__ import annotations

from typing import Any
from typing import Dict

from botocore.waiter import Waiter


class ChangeSetCreateComplete(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        ChangeSetName: str,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class StackCreateComplete(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class StackDeleteComplete(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class StackExists(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass


class StackUpdateComplete(Waiter):

    # pylint: disable=arguments-differ
    def wait(
        self,
        StackName: str = None,
        NextToken: str = None,
        WaiterConfig: Dict[str, Any] = None,
    ) -> None:
        pass

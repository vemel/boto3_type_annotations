from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class ChangeSetCreateComplete(Waiter):
    def wait(
        self,
        ChangeSetName: str,
        StackName: Optional[str] = None,
        NextToken: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class StackCreateComplete(Waiter):
    def wait(
        self,
        StackName: Optional[str] = None,
        NextToken: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class StackDeleteComplete(Waiter):
    def wait(
        self,
        StackName: Optional[str] = None,
        NextToken: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class StackExists(Waiter):
    def wait(
        self,
        StackName: Optional[str] = None,
        NextToken: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class StackUpdateComplete(Waiter):
    def wait(
        self,
        StackName: Optional[str] = None,
        NextToken: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass


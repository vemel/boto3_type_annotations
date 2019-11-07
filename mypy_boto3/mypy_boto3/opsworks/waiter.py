from typing import Dict
from typing import List
from typing import Optional

from botocore.waiter import Waiter


class AppExists(Waiter):
    def wait(
        self,
        StackId: Optional[str] = None,
        AppIds: Optional[List] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class DeploymentSuccessful(Waiter):
    def wait(
        self,
        StackId: Optional[str] = None,
        AppId: Optional[str] = None,
        DeploymentIds: Optional[List] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class InstanceOnline(Waiter):
    def wait(
        self,
        StackId: Optional[str] = None,
        LayerId: Optional[str] = None,
        InstanceIds: Optional[List] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class InstanceRegistered(Waiter):
    def wait(
        self,
        StackId: Optional[str] = None,
        LayerId: Optional[str] = None,
        InstanceIds: Optional[List] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class InstanceStopped(Waiter):
    def wait(
        self,
        StackId: Optional[str] = None,
        LayerId: Optional[str] = None,
        InstanceIds: Optional[List] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class InstanceTerminated(Waiter):
    def wait(
        self,
        StackId: Optional[str] = None,
        LayerId: Optional[str] = None,
        InstanceIds: Optional[List] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass


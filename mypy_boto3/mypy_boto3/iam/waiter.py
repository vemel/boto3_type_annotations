from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class InstanceProfileExists(Waiter):
    def wait(
        self,
        InstanceProfileName: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class PolicyExists(Waiter):
    def wait(
        self,
        PolicyArn: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class RoleExists(Waiter):
    def wait(
        self,
        RoleName: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class UserExists(Waiter):
    def wait(
        self,
        UserName: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass


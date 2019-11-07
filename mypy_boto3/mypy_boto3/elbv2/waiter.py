from typing import Dict
from typing import List
from typing import Optional

from botocore.waiter import Waiter


class LoadBalancerAvailable(Waiter):
    def wait(
        self,
        LoadBalancerArns: Optional[List] = None,
        Names: Optional[List] = None,
        Marker: Optional[str] = None,
        PageSize: Optional[int] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class LoadBalancerExists(Waiter):
    def wait(
        self,
        LoadBalancerArns: Optional[List] = None,
        Names: Optional[List] = None,
        Marker: Optional[str] = None,
        PageSize: Optional[int] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class LoadBalancersDeleted(Waiter):
    def wait(
        self,
        LoadBalancerArns: Optional[List] = None,
        Names: Optional[List] = None,
        Marker: Optional[str] = None,
        PageSize: Optional[int] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class TargetDeregistered(Waiter):
    def wait(
        self,
        TargetGroupArn: str,
        Targets: Optional[List] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class TargetInService(Waiter):
    def wait(
        self,
        TargetGroupArn: str,
        Targets: Optional[List] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass


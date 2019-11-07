from typing import Dict
from typing import List
from typing import Optional

from botocore.waiter import Waiter


class ServicesInactive(Waiter):
    def wait(
        self,
        services: List,
        cluster: Optional[str] = None,
        include: Optional[List] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ServicesStable(Waiter):
    def wait(
        self,
        services: List,
        cluster: Optional[str] = None,
        include: Optional[List] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class TasksRunning(Waiter):
    def wait(
        self,
        tasks: List,
        cluster: Optional[str] = None,
        include: Optional[List] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class TasksStopped(Waiter):
    def wait(
        self,
        tasks: List,
        cluster: Optional[str] = None,
        include: Optional[List] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass


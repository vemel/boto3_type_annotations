from typing import Dict
from typing import List
from typing import Optional

from botocore.waiter import Waiter


class EndpointDeleted(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ReplicationInstanceAvailable(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ReplicationInstanceDeleted(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ReplicationTaskDeleted(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        WithoutSettings: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ReplicationTaskReady(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        WithoutSettings: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ReplicationTaskRunning(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        WithoutSettings: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class ReplicationTaskStopped(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        WithoutSettings: Optional[bool] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class TestConnectionSucceeds(Waiter):
    def wait(
        self,
        Filters: Optional[List] = None,
        MaxRecords: Optional[int] = None,
        Marker: Optional[str] = None,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass


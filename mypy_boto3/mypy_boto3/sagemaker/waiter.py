from typing import Dict
from typing import Optional

from botocore.waiter import Waiter


class EndpointDeleted(Waiter):
    def wait(
        self,
        EndpointName: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class EndpointInService(Waiter):
    def wait(
        self,
        EndpointName: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class NotebookInstanceDeleted(Waiter):
    def wait(
        self,
        NotebookInstanceName: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class NotebookInstanceInService(Waiter):
    def wait(
        self,
        NotebookInstanceName: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class NotebookInstanceStopped(Waiter):
    def wait(
        self,
        NotebookInstanceName: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class TrainingJobCompletedOrStopped(Waiter):
    def wait(
        self,
        TrainingJobName: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass



class TransformJobCompletedOrStopped(Waiter):
    def wait(
        self,
        TransformJobName: str,
        WaiterConfig: Optional[Dict] = None,
    ):
        pass


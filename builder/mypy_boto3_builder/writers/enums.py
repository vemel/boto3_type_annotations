from __future__ import annotations

import enum
from typing import List


class ServiceSubmodule(enum.Enum):
    client = "client.py"
    service_resource = "service_resource.py"
    waiter = "waiter.py"
    paginator = "paginator.py"

    @property
    def import_name(self) -> str:
        return self.name

    @property
    def file_name(self) -> str:
        return self.value

    @property
    def class_name(self) -> str:
        if self == ServiceSubmodule.client:
            return "Client"
        if self == ServiceSubmodule.service_resource:
            return "ServiceResource"

        raise ValueError(f"No class name for {self}")

    @property
    def boto3_function_name(self) -> str:
        if self == ServiceSubmodule.client:
            return "client"
        if self == ServiceSubmodule.service_resource:
            return "resource"
        if self == ServiceSubmodule.waiter:
            return "get_waiter"
        if self == ServiceSubmodule.paginator:
            return "get_paginator"

        raise ValueError(f"No boto3 function name for {self}")

    @classmethod
    def get_imported(cls) -> List[ServiceSubmodule]:
        return [
            cls.client,
            cls.service_resource,
        ]

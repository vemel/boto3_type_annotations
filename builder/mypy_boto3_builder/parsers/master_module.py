"""
Parser that produces `structures.MasterModule`.
"""
from typing import Iterable
from boto3.session import Session

from mypy_boto3_builder.structures.master_module import MasterModule
from mypy_boto3_builder.enums.service_name import ServiceName
from mypy_boto3_builder.parsers.fake_service_module import parse_fake_service_module


def parse_master_module(
    session: Session, service_names: Iterable[ServiceName]
) -> MasterModule:
    """
    Parse data for master module.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.

    Returns:
        MasterModule structure.
    """
    result = MasterModule()
    for service_name in service_names:
        result.service_modules.append(parse_fake_service_module(session, service_name))
        result.service_names.append(service_name)

    return result

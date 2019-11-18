"""
Parser that produces `structures.Boto3Module`.
"""
from typing import Iterable
from boto3.session import Session

from mypy_boto3_builder.structures.boto3_module import Boto3Module
from mypy_boto3_builder.enums.service_name import ServiceName
from mypy_boto3_builder.parsers.fake_service_module import parse_fake_service_module


def parse_boto3_module(
    session: Session, service_names: Iterable[ServiceName]
) -> Boto3Module:
    """
    Parse data for boto3-stubs module.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.

    Returns:
        MasterModule structure.
    """
    result = Boto3Module()
    for service_name in service_names:
        result.service_modules.append(parse_fake_service_module(session, service_name))
        result.service_names.append(service_name)

    return result

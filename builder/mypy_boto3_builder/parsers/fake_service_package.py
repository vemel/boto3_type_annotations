"""
Fake parser that produces `structures.ServiceModule` for master module and stubs.
"""
from boto3.session import Session

from mypy_boto3_builder.structures.client import Client
from mypy_boto3_builder.structures.service_resource import ServiceResource
from mypy_boto3_builder.structures.waiter import Waiter
from mypy_boto3_builder.structures.paginator import Paginator
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.enums.service_name import ServiceName
from mypy_boto3_builder.parsers.boto3_utils import get_boto3_resource, get_boto3_client


def parse_fake_service_package(
    session: Session, service_name: ServiceName
) -> ServicePackage:
    """
    Create fake boto3 service module structure.

    Used by stubs and master package.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.

    Returns:
        ServiceModule structure.
    """
    result = ServicePackage(
        name=service_name.module_name,
        pypi_name=service_name.pypi_name,
        service_name=service_name,
        client=Client(),
    )

    boto3_client = get_boto3_client(session, service_name)
    boto3_resource = get_boto3_resource(session, service_name)

    if boto3_resource is not None:
        result.service_resource = ServiceResource()

    if boto3_client.waiter_names:
        result.waiters.append(Waiter("FakeWaiter"))

    session_loader = session._loader  # pylint: disable=protected-access
    if service_name.boto3_name in session_loader.list_available_services(
        "paginators-1"
    ):
        result.paginators.append(Paginator("FakePaginator"))

    return result

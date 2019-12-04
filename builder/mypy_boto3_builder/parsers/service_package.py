"""
Parser that produces `structures.ServiceModule`.
"""
import inspect
from typing import Iterable

from boto3.session import Session
from botocore import xform_name
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter
from botocore.config import Config as Boto3Config

from mypy_boto3_builder.type_defs import Literal
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.structures.function import Function
from mypy_boto3_builder.structures.waiter import Waiter
from mypy_boto3_builder.structures.paginator import Paginator
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.parsers.client import parse_client
from mypy_boto3_builder.parsers.service_resource import parse_service_resource
from mypy_boto3_builder.parsers.helpers import get_public_methods, parse_method
from mypy_boto3_builder.parsers.boto3_utils import get_boto3_client
from mypy_boto3_builder.logger import get_logger


def parse_service_package(
    session: Session, service_name: ServiceName
) -> ServicePackage:
    """
    Extract all data from boto3 service package.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.

    Returns:
        ServiceModule structure.
    """
    logger = get_logger()
    logger.debug("Parsing Client")
    client = parse_client(session, service_name)

    service_resource = parse_service_resource(session, service_name)

    result = ServicePackage(
        name=service_name.module_name,
        pypi_name=service_name.pypi_name,
        service_name=service_name,
        client=client,
        service_resource=service_resource,
    )

    for waiter_name in client.boto3_client.waiter_names:
        logger.debug(f"Parsing Waiter {waiter_name}")
        waiter = client.boto3_client.get_waiter(waiter_name)
        waiter_record = Waiter(
            name=f"{waiter.name}Waiter",
            waiter_name=waiter_name,
            boto3_waiter=waiter,
            docstring=f"Waiter for `{waiter_name}` name.",
        )
        public_methods = get_public_methods(waiter)
        for method_name, public_method in public_methods.items():
            method = parse_method(waiter_name, method_name, public_method)
            method.docstring = (
                f"[{waiter_name}.{method_name} documentation]"
                f"({service_name.doc_link}.Waiter.{waiter_name}.{method_name})"
            )
            waiter_record.methods.append(method)
        result.waiters.append(waiter_record)

    session_loader = session._loader  # pylint: disable=protected-access
    if service_name.boto3_name in session_loader.list_available_services(
        "paginators-1"
    ):
        session_client = get_boto3_client(session, service_name)
        paginator_config = session_loader.load_service_model(
            service_name.boto3_name, "paginators-1", None
        )["pagination"]
        for paginator_name in sorted(paginator_config):
            logger.debug(f"Parsing Paginator {paginator_name}")
            operation_name = xform_name(paginator_name)
            paginator = session_client.get_paginator(operation_name)
            paginator_record = Paginator(
                name=f"{paginator_name}Paginator",
                operation_name=operation_name,
                boto3_paginator=paginator,
                docstring=f"Paginator for `{operation_name}`",
            )
            public_methods = get_public_methods(paginator)
            for method_name, public_method in public_methods.items():
                method = parse_method(paginator_name, method_name, public_method)
                method.docstring = (
                    f"[{paginator_name}.{method_name} documentation]"
                    f"({service_name.doc_link}.Paginator.{paginator_name}.{method_name})"
                )
                paginator_record.methods.append(method)
            result.paginators.append(paginator_record)

    if result.paginators:
        for paginator in result.paginators:
            result.client.methods.append(paginator.get_client_method())
        result.client.methods.append(
            Method(
                name="get_paginator",
                arguments=[
                    Argument("self", None),
                    Argument("operation_name", Type.str),
                ],
                return_type=TypeClass(Boto3Paginator, alias="Boto3Paginator"),
            )
        )

    if result.waiters:
        for waiter in result.waiters:
            result.client.methods.append(waiter.get_client_method())
        result.client.methods.append(
            Method(
                name="get_waiter",
                docstring=inspect.getdoc(client.boto3_client.get_waiter) or "",
                arguments=[Argument("self", None), Argument("waiter_name", Type.str),],
                return_type=TypeClass(Boto3Waiter, alias="Boto3Waiter"),
            )
        )

    result.typed_dicts = result.extract_typed_dicts(result.get_types(), {})
    helper_arguments = [
        Argument("session", TypeClass(Session), Type.none),
        Argument("region_name", Type.str, Type.none),
        Argument("api_version", Type.str, Type.none),
        Argument("use_ssl", Type.bool, Type.none),
        Argument(
            "verify", TypeSubscript(Type.Union, [Type.str, Type.bool]), Type.none,
        ),
        Argument("endpoint_url", Type.str, Type.none),
        Argument("aws_access_key_id", Type.str, Type.none),
        Argument("aws_secret_access_key", Type.str, Type.none),
        Argument("aws_session_token", Type.str, Type.none),
        Argument("config", TypeClass(Boto3Config), Type.none),
    ]
    client_helper = Function(
        name="boto3_client",
        docstring=f"Equivalent of `boto3.client('{service_name.boto3_name}')`, returns a correct type.",
        arguments=helper_arguments,
        return_type=ExternalImport(
            ImportString(service_name.module_name, ServiceModuleName.client.name),
            result.client.name,
        ),
        body=get_helper_body(helper_arguments, "client", service_name),
    )
    result.helper_functions.append(client_helper)
    if result.service_resource:
        resource_helper = Function(
            name="boto3_resource",
            docstring=f"Equivalent of `boto3.resource('{service_name.boto3_name}')`, returns a correct type.",
            arguments=helper_arguments,
            return_type=ExternalImport(
                ImportString(
                    service_name.module_name, ServiceModuleName.service_resource.name
                ),
                result.service_resource.name,
            ),
            body=get_helper_body(helper_arguments, "resource", service_name),
        )
        result.helper_functions.append(resource_helper)

    for paginator in result.paginators:
        result.helper_functions.append(
            Function(
                name=f"get_{paginator.operation_name}_paginator",
                docstring=f"Equivalent of `client.get_paginator('{paginator.operation_name}')`, returns a correct type.",
                arguments=[
                    Argument(
                        name="client",
                        type=ExternalImport(
                            ImportString(
                                service_name.module_name, ServiceModuleName.client.name
                            ),
                            result.client.name,
                        ),
                    )
                ],
                return_type=ExternalImport(
                    ImportString(
                        service_name.module_name, ServiceModuleName.paginator.name
                    ),
                    paginator.name,
                ),
                body=f"return client.get_paginator('{paginator.operation_name}')",
            )
        )

    for waiter in result.waiters:
        result.helper_functions.append(
            Function(
                name=f"get_{waiter.waiter_name}_waiter",
                docstring=f"Equivalent of `client.get_waiter('{waiter.waiter_name}')`, returns a correct type.",
                arguments=[
                    Argument(
                        name="client",
                        type=ExternalImport(
                            ImportString(
                                service_name.module_name, ServiceModuleName.client.name
                            ),
                            result.client.name,
                        ),
                    )
                ],
                return_type=ExternalImport(
                    ImportString(
                        service_name.module_name, ServiceModuleName.waiter.name
                    ),
                    waiter.name,
                ),
                body=f"return client.get_waiter('{waiter.waiter_name}')",
            )
        )

    return result


def get_helper_body(
    arguments: Iterable[Argument],
    function_name: Literal["resource", "client"],
    service_name: ServiceName,
) -> str:
    helper_body_lines = [
        "kwargs: Dict[str, Any] = {}",
    ]
    for argument in arguments:
        if argument.name == "session":
            continue
        helper_body_lines.append(f"if {argument.name} is not None:")
        helper_body_lines.append(f'    kwargs["{argument.name}"] = {argument.name}')
    helper_body_lines.append("if session is not None:")
    helper_body_lines.append(
        f"    return session.{function_name}('{service_name.boto3_name}', **kwargs)"
    )
    helper_body_lines.append(
        f"return boto3.{function_name}('{service_name.boto3_name}', **kwargs)"
    )
    return "\n".join(helper_body_lines)

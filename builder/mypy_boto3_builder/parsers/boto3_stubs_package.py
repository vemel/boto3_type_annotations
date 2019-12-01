"""
Parser that produces `structures.Boto3Module`.
"""
from typing import Iterable

from boto3.session import Session
from botocore.config import Config as Boto3Config

from mypy_boto3_builder.constants import MODULE_NAME
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.structures.function import Function
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.structures.boto3_stubs_package import Boto3StubsPackage
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.enums.service_name import ServiceName
from mypy_boto3_builder.parsers.fake_service_package import parse_fake_service_package


def parse_boto3_stubs_package(
    session: Session, service_names: Iterable[ServiceName]
) -> Boto3StubsPackage:
    """
    Parse data for boto3-stubs package.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.

    Returns:
        MasterModule structure.
    """
    result = Boto3StubsPackage()
    for service_name in service_names:
        result.service_packages.append(
            parse_fake_service_package(session, service_name)
        )
        result.service_names.append(service_name)

    client_function_arguments = [
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

    for service_package in result.service_packages:
        result.init_functions.append(
            Function(
                name=f"client",
                docstring="",
                decorators=[Type.overload],
                arguments=[
                    Argument(
                        "service_name",
                        TypeLiteral(service_package.service_name.boto3_name),
                    ),
                    *client_function_arguments,
                ],
                return_type=ExternalImport(
                    ImportString(MODULE_NAME, service_package.service_name.import_name),
                    service_package.client.name,
                    f"{service_package.service_name.class_prefix}{service_package.client.name}",
                ),
                body=f"...",
            )
        )
        result.session_methods.append(
            Method(
                name=f"client",
                docstring="",
                decorators=[Type.overload],
                arguments=[
                    Argument("self", None),
                    Argument(
                        "service_name",
                        TypeLiteral(service_package.service_name.boto3_name),
                    ),
                    *client_function_arguments,
                ],
                return_type=ExternalImport(
                    ImportString(MODULE_NAME, service_package.service_name.import_name),
                    service_package.client.name,
                    f"{service_package.service_name.class_prefix}{service_package.client.name}",
                ),
                body=f"...",
            )
        )

    for service_package in result.service_packages:
        if not service_package.service_resource:
            continue

        result.init_functions.append(
            Function(
                name=f"resource",
                docstring="",
                decorators=[Type.overload],
                arguments=[
                    Argument(
                        "service_name",
                        TypeLiteral(service_package.service_name.boto3_name),
                    ),
                    *client_function_arguments,
                ],
                return_type=ExternalImport(
                    ImportString(MODULE_NAME, service_package.service_name.import_name),
                    service_package.service_resource.name,
                    f"{service_package.service_name.class_prefix}{service_package.service_resource.name}",
                ),
                body=f"...",
            )
        )
        result.session_methods.append(
            Method(
                name=f"resource",
                docstring="",
                decorators=[Type.overload],
                arguments=[
                    Argument("self", None),
                    Argument(
                        "service_name",
                        TypeLiteral(service_package.service_name.boto3_name),
                    ),
                    *client_function_arguments,
                ],
                return_type=ExternalImport(
                    ImportString(MODULE_NAME, service_package.service_name.import_name),
                    service_package.service_resource.name,
                    f"{service_package.service_name.class_prefix}{service_package.service_resource.name}",
                ),
                body=f"...",
            )
        )

    return result

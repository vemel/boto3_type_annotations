"Main interface for lakeformation type defs"
from __future__ import annotations

from datetime import datetime
from typing import Dict, List
from typing_extensions import TypedDict


__all__ = (
    "ClientBatchGrantPermissionsEntriesPrincipalTypeDef",
    "ClientBatchGrantPermissionsEntriesResourceDataLocationTypeDef",
    "ClientBatchGrantPermissionsEntriesResourceDatabaseTypeDef",
    "ClientBatchGrantPermissionsEntriesResourceTableTypeDef",
    "ClientBatchGrantPermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientBatchGrantPermissionsEntriesResourceTableWithColumnsTypeDef",
    "ClientBatchGrantPermissionsEntriesResourceTypeDef",
    "ClientBatchGrantPermissionsEntriesTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresErrorTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryPrincipalTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresTypeDef",
    "ClientBatchGrantPermissionsResponseTypeDef",
    "ClientBatchRevokePermissionsEntriesPrincipalTypeDef",
    "ClientBatchRevokePermissionsEntriesResourceDataLocationTypeDef",
    "ClientBatchRevokePermissionsEntriesResourceDatabaseTypeDef",
    "ClientBatchRevokePermissionsEntriesResourceTableTypeDef",
    "ClientBatchRevokePermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientBatchRevokePermissionsEntriesResourceTableWithColumnsTypeDef",
    "ClientBatchRevokePermissionsEntriesResourceTypeDef",
    "ClientBatchRevokePermissionsEntriesTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresErrorTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryPrincipalTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresTypeDef",
    "ClientBatchRevokePermissionsResponseTypeDef",
    "ClientDescribeResourceResponseResourceInfoTypeDef",
    "ClientDescribeResourceResponseTypeDef",
    "ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef",
    "ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef",
    "ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef",
    "ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsTypeDef",
    "ClientGetDataLakeSettingsResponseDataLakeSettingsDataLakeAdminsTypeDef",
    "ClientGetDataLakeSettingsResponseDataLakeSettingsTypeDef",
    "ClientGetDataLakeSettingsResponseTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsPrincipalTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceDataLocationTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceDatabaseTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsTypeDef",
    "ClientGetEffectivePermissionsForPathResponseTypeDef",
    "ClientGrantPermissionsPrincipalTypeDef",
    "ClientGrantPermissionsResourceDataLocationTypeDef",
    "ClientGrantPermissionsResourceDatabaseTypeDef",
    "ClientGrantPermissionsResourceTableTypeDef",
    "ClientGrantPermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientGrantPermissionsResourceTableWithColumnsTypeDef",
    "ClientGrantPermissionsResourceTypeDef",
    "ClientListPermissionsPrincipalTypeDef",
    "ClientListPermissionsResourceDataLocationTypeDef",
    "ClientListPermissionsResourceDatabaseTypeDef",
    "ClientListPermissionsResourceTableTypeDef",
    "ClientListPermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientListPermissionsResourceTableWithColumnsTypeDef",
    "ClientListPermissionsResourceTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsPrincipalTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceDataLocationTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceDatabaseTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsTypeDef",
    "ClientListPermissionsResponseTypeDef",
    "ClientListResourcesFilterConditionListTypeDef",
    "ClientListResourcesResponseResourceInfoListTypeDef",
    "ClientListResourcesResponseTypeDef",
    "ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef",
    "ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef",
    "ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef",
    "ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsTypeDef",
    "ClientPutDataLakeSettingsDataLakeSettingsDataLakeAdminsTypeDef",
    "ClientPutDataLakeSettingsDataLakeSettingsTypeDef",
    "ClientRevokePermissionsPrincipalTypeDef",
    "ClientRevokePermissionsResourceDataLocationTypeDef",
    "ClientRevokePermissionsResourceDatabaseTypeDef",
    "ClientRevokePermissionsResourceTableTypeDef",
    "ClientRevokePermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientRevokePermissionsResourceTableWithColumnsTypeDef",
    "ClientRevokePermissionsResourceTypeDef",
)


_ClientBatchGrantPermissionsEntriesPrincipalTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsEntriesPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientBatchGrantPermissionsEntriesPrincipalTypeDef(
    _ClientBatchGrantPermissionsEntriesPrincipalTypeDef
):
    """
    Type definition for `ClientBatchGrantPermissionsEntries` `Principal`

    The principal to be granted a permission.

    - **DataLakePrincipalIdentifier** *(string) --*

      An identifier for the AWS Lake Formation principal.
    """


_ClientBatchGrantPermissionsEntriesResourceDataLocationTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsEntriesResourceDataLocationTypeDef",
    {"ResourceArn": str},
)


class ClientBatchGrantPermissionsEntriesResourceDataLocationTypeDef(
    _ClientBatchGrantPermissionsEntriesResourceDataLocationTypeDef
):
    """
    Type definition for `ClientBatchGrantPermissionsEntriesResource` `DataLocation`

    The location of an Amazon S3 path where permissions are granted or revoked.

    - **ResourceArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
    """


_ClientBatchGrantPermissionsEntriesResourceDatabaseTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsEntriesResourceDatabaseTypeDef", {"Name": str}
)


class ClientBatchGrantPermissionsEntriesResourceDatabaseTypeDef(
    _ClientBatchGrantPermissionsEntriesResourceDatabaseTypeDef
):
    """
    Type definition for `ClientBatchGrantPermissionsEntriesResource` `Database`

    The database for the resource. Unique to the Data Catalog. A database is a set of
    associated table definitions organized into a logical group. You can Grant and Revoke
    database permissions to a principal.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the database resource. Unique to the Data Catalog.
    """


_ClientBatchGrantPermissionsEntriesResourceTableTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsEntriesResourceTableTypeDef",
    {"DatabaseName": str, "Name": str},
)


class ClientBatchGrantPermissionsEntriesResourceTableTypeDef(
    _ClientBatchGrantPermissionsEntriesResourceTableTypeDef
):
    """
    Type definition for `ClientBatchGrantPermissionsEntriesResource` `Table`

    The table for the resource. A table is a metadata definition that represents your data. You
    can Grant and Revoke table privileges to a principal.

    - **DatabaseName** *(string) --* **[REQUIRED]**

      The name of the database for the table. Unique to a Data Catalog. A database is a set of
      associated table definitions organized into a logical group. You can Grant and Revoke
      database privileges to a principal.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the table.
    """


_ClientBatchGrantPermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)


class ClientBatchGrantPermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef(
    _ClientBatchGrantPermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef
):
    """
    Type definition for `ClientBatchGrantPermissionsEntriesResourceTableWithColumns` `ColumnWildcard`

    A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
    ``ColumnWildcard`` is required.

    - **ExcludedColumnNames** *(list) --*

      Excludes column names. Any column with this name will be excluded.

      - *(string) --*
    """


_ClientBatchGrantPermissionsEntriesResourceTableWithColumnsTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsEntriesResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientBatchGrantPermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)


class ClientBatchGrantPermissionsEntriesResourceTableWithColumnsTypeDef(
    _ClientBatchGrantPermissionsEntriesResourceTableWithColumnsTypeDef
):
    """
    Type definition for `ClientBatchGrantPermissionsEntriesResource` `TableWithColumns`

    The table with columns for the resource. A principal with permissions to this resource can
    select metadata from the columns of a table in the Data Catalog and the underlying data in
    Amazon S3.

    - **DatabaseName** *(string) --*

      The name of the database for the table with columns resource. Unique to the Data Catalog.
      A database is a set of associated table definitions organized into a logical group. You
      can Grant and Revoke database privileges to a principal.

    - **Name** *(string) --*

      The name of the table resource. A table is a metadata definition that represents your
      data. You can Grant and Revoke table privileges to a principal.

    - **ColumnNames** *(list) --*

      The list of column names for the table. At least one of ``ColumnNames`` or
      ``ColumnWildcard`` is required.

      - *(string) --*

    - **ColumnWildcard** *(dict) --*

      A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
      ``ColumnWildcard`` is required.

      - **ExcludedColumnNames** *(list) --*

        Excludes column names. Any column with this name will be excluded.

        - *(string) --*
    """


_ClientBatchGrantPermissionsEntriesResourceTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsEntriesResourceTypeDef",
    {
        "Catalog": Dict,
        "Database": ClientBatchGrantPermissionsEntriesResourceDatabaseTypeDef,
        "Table": ClientBatchGrantPermissionsEntriesResourceTableTypeDef,
        "TableWithColumns": ClientBatchGrantPermissionsEntriesResourceTableWithColumnsTypeDef,
        "DataLocation": ClientBatchGrantPermissionsEntriesResourceDataLocationTypeDef,
    },
    total=False,
)


class ClientBatchGrantPermissionsEntriesResourceTypeDef(
    _ClientBatchGrantPermissionsEntriesResourceTypeDef
):
    """
    Type definition for `ClientBatchGrantPermissionsEntries` `Resource`

    The resource to which the principal is to be granted a permission.

    - **Catalog** *(dict) --*

      The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
      persistent metadata store. It contains database definitions, table definitions, and other
      control information to manage your AWS Lake Formation environment.

    - **Database** *(dict) --*

      The database for the resource. Unique to the Data Catalog. A database is a set of
      associated table definitions organized into a logical group. You can Grant and Revoke
      database permissions to a principal.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the database resource. Unique to the Data Catalog.

    - **Table** *(dict) --*

      The table for the resource. A table is a metadata definition that represents your data. You
      can Grant and Revoke table privileges to a principal.

      - **DatabaseName** *(string) --* **[REQUIRED]**

        The name of the database for the table. Unique to a Data Catalog. A database is a set of
        associated table definitions organized into a logical group. You can Grant and Revoke
        database privileges to a principal.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the table.

    - **TableWithColumns** *(dict) --*

      The table with columns for the resource. A principal with permissions to this resource can
      select metadata from the columns of a table in the Data Catalog and the underlying data in
      Amazon S3.

      - **DatabaseName** *(string) --*

        The name of the database for the table with columns resource. Unique to the Data Catalog.
        A database is a set of associated table definitions organized into a logical group. You
        can Grant and Revoke database privileges to a principal.

      - **Name** *(string) --*

        The name of the table resource. A table is a metadata definition that represents your
        data. You can Grant and Revoke table privileges to a principal.

      - **ColumnNames** *(list) --*

        The list of column names for the table. At least one of ``ColumnNames`` or
        ``ColumnWildcard`` is required.

        - *(string) --*

      - **ColumnWildcard** *(dict) --*

        A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
        ``ColumnWildcard`` is required.

        - **ExcludedColumnNames** *(list) --*

          Excludes column names. Any column with this name will be excluded.

          - *(string) --*

    - **DataLocation** *(dict) --*

      The location of an Amazon S3 path where permissions are granted or revoked.

      - **ResourceArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
    """


_RequiredClientBatchGrantPermissionsEntriesTypeDef = TypedDict(
    "_RequiredClientBatchGrantPermissionsEntriesTypeDef", {"Id": str}
)
_OptionalClientBatchGrantPermissionsEntriesTypeDef = TypedDict(
    "_OptionalClientBatchGrantPermissionsEntriesTypeDef",
    {
        "Principal": ClientBatchGrantPermissionsEntriesPrincipalTypeDef,
        "Resource": ClientBatchGrantPermissionsEntriesResourceTypeDef,
        "Permissions": List[str],
        "PermissionsWithGrantOption": List[str],
    },
    total=False,
)


class ClientBatchGrantPermissionsEntriesTypeDef(
    _RequiredClientBatchGrantPermissionsEntriesTypeDef,
    _OptionalClientBatchGrantPermissionsEntriesTypeDef,
):
    """
    Type definition for `ClientBatchGrantPermissions` `Entries`

    A permission to a resource granted by batch operation to the principal.

    - **Id** *(string) --* **[REQUIRED]**

      A unique identifier for the batch permissions request entry.

    - **Principal** *(dict) --*

      The principal to be granted a permission.

      - **DataLakePrincipalIdentifier** *(string) --*

        An identifier for the AWS Lake Formation principal.

    - **Resource** *(dict) --*

      The resource to which the principal is to be granted a permission.

      - **Catalog** *(dict) --*

        The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
        persistent metadata store. It contains database definitions, table definitions, and other
        control information to manage your AWS Lake Formation environment.

      - **Database** *(dict) --*

        The database for the resource. Unique to the Data Catalog. A database is a set of
        associated table definitions organized into a logical group. You can Grant and Revoke
        database permissions to a principal.

        - **Name** *(string) --* **[REQUIRED]**

          The name of the database resource. Unique to the Data Catalog.

      - **Table** *(dict) --*

        The table for the resource. A table is a metadata definition that represents your data. You
        can Grant and Revoke table privileges to a principal.

        - **DatabaseName** *(string) --* **[REQUIRED]**

          The name of the database for the table. Unique to a Data Catalog. A database is a set of
          associated table definitions organized into a logical group. You can Grant and Revoke
          database privileges to a principal.

        - **Name** *(string) --* **[REQUIRED]**

          The name of the table.

      - **TableWithColumns** *(dict) --*

        The table with columns for the resource. A principal with permissions to this resource can
        select metadata from the columns of a table in the Data Catalog and the underlying data in
        Amazon S3.

        - **DatabaseName** *(string) --*

          The name of the database for the table with columns resource. Unique to the Data Catalog.
          A database is a set of associated table definitions organized into a logical group. You
          can Grant and Revoke database privileges to a principal.

        - **Name** *(string) --*

          The name of the table resource. A table is a metadata definition that represents your
          data. You can Grant and Revoke table privileges to a principal.

        - **ColumnNames** *(list) --*

          The list of column names for the table. At least one of ``ColumnNames`` or
          ``ColumnWildcard`` is required.

          - *(string) --*

        - **ColumnWildcard** *(dict) --*

          A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
          ``ColumnWildcard`` is required.

          - **ExcludedColumnNames** *(list) --*

            Excludes column names. Any column with this name will be excluded.

            - *(string) --*

      - **DataLocation** *(dict) --*

        The location of an Amazon S3 path where permissions are granted or revoked.

        - **ResourceArn** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

    - **Permissions** *(list) --*

      The permissions to be granted.

      - *(string) --*

    - **PermissionsWithGrantOption** *(list) --*

      Indicates if the option to pass permissions is granted.

      - *(string) --*
    """


_ClientBatchGrantPermissionsResponseFailuresErrorTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresErrorTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresErrorTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresErrorTypeDef
):
    """
    Type definition for `ClientBatchGrantPermissionsResponseFailures` `Error`

    An error message that applies to the failure of the entry.

    - **ErrorCode** *(string) --*

      The code associated with this error.

    - **ErrorMessage** *(string) --*

      A message describing the error.
    """


_ClientBatchGrantPermissionsResponseFailuresRequestEntryPrincipalTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresRequestEntryPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresRequestEntryPrincipalTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresRequestEntryPrincipalTypeDef
):
    """
    Type definition for `ClientBatchGrantPermissionsResponseFailuresRequestEntry` `Principal`

    The principal to be granted a permission.

    - **DataLakePrincipalIdentifier** *(string) --*

      An identifier for the AWS Lake Formation principal.
    """


_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef",
    {"ResourceArn": str},
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef
):
    """
    Type definition for `ClientBatchGrantPermissionsResponseFailuresRequestEntryResource` `DataLocation`

    The location of an Amazon S3 path where permissions are granted or revoked.

    - **ResourceArn** *(string) --*

      The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
    """


_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef",
    {"Name": str},
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef
):
    """
    Type definition for `ClientBatchGrantPermissionsResponseFailuresRequestEntryResource` `Database`

    The database for the resource. Unique to the Data Catalog. A database is a set of
    associated table definitions organized into a logical group. You can Grant and Revoke
    database permissions to a principal.

    - **Name** *(string) --*

      The name of the database resource. Unique to the Data Catalog.
    """


_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableTypeDef",
    {"DatabaseName": str, "Name": str},
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableTypeDef
):
    """
    Type definition for `ClientBatchGrantPermissionsResponseFailuresRequestEntryResource` `Table`

    The table for the resource. A table is a metadata definition that represents your
    data. You can Grant and Revoke table privileges to a principal.

    - **DatabaseName** *(string) --*

      The name of the database for the table. Unique to a Data Catalog. A database is a
      set of associated table definitions organized into a logical group. You can Grant
      and Revoke database privileges to a principal.

    - **Name** *(string) --*

      The name of the table.
    """


_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef
):
    """
    Type definition for `ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumns` `ColumnWildcard`

    A wildcard specified by a ``ColumnWildcard`` object. At least one of
    ``ColumnNames`` or ``ColumnWildcard`` is required.

    - **ExcludedColumnNames** *(list) --*

      Excludes column names. Any column with this name will be excluded.

      - *(string) --*
    """


_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef
):
    """
    Type definition for `ClientBatchGrantPermissionsResponseFailuresRequestEntryResource` `TableWithColumns`

    The table with columns for the resource. A principal with permissions to this
    resource can select metadata from the columns of a table in the Data Catalog and the
    underlying data in Amazon S3.

    - **DatabaseName** *(string) --*

      The name of the database for the table with columns resource. Unique to the Data
      Catalog. A database is a set of associated table definitions organized into a
      logical group. You can Grant and Revoke database privileges to a principal.

    - **Name** *(string) --*

      The name of the table resource. A table is a metadata definition that represents
      your data. You can Grant and Revoke table privileges to a principal.

    - **ColumnNames** *(list) --*

      The list of column names for the table. At least one of ``ColumnNames`` or
      ``ColumnWildcard`` is required.

      - *(string) --*

    - **ColumnWildcard** *(dict) --*

      A wildcard specified by a ``ColumnWildcard`` object. At least one of
      ``ColumnNames`` or ``ColumnWildcard`` is required.

      - **ExcludedColumnNames** *(list) --*

        Excludes column names. Any column with this name will be excluded.

        - *(string) --*
    """


_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTypeDef",
    {
        "Catalog": Dict,
        "Database": ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef,
        "Table": ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableTypeDef,
        "TableWithColumns": ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef,
        "DataLocation": ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef,
    },
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTypeDef
):
    """
    Type definition for `ClientBatchGrantPermissionsResponseFailuresRequestEntry` `Resource`

    The resource to which the principal is to be granted a permission.

    - **Catalog** *(dict) --*

      The identifier for the Data Catalog. By default, the account ID. The Data Catalog is
      the persistent metadata store. It contains database definitions, table definitions,
      and other control information to manage your AWS Lake Formation environment.

    - **Database** *(dict) --*

      The database for the resource. Unique to the Data Catalog. A database is a set of
      associated table definitions organized into a logical group. You can Grant and Revoke
      database permissions to a principal.

      - **Name** *(string) --*

        The name of the database resource. Unique to the Data Catalog.

    - **Table** *(dict) --*

      The table for the resource. A table is a metadata definition that represents your
      data. You can Grant and Revoke table privileges to a principal.

      - **DatabaseName** *(string) --*

        The name of the database for the table. Unique to a Data Catalog. A database is a
        set of associated table definitions organized into a logical group. You can Grant
        and Revoke database privileges to a principal.

      - **Name** *(string) --*

        The name of the table.

    - **TableWithColumns** *(dict) --*

      The table with columns for the resource. A principal with permissions to this
      resource can select metadata from the columns of a table in the Data Catalog and the
      underlying data in Amazon S3.

      - **DatabaseName** *(string) --*

        The name of the database for the table with columns resource. Unique to the Data
        Catalog. A database is a set of associated table definitions organized into a
        logical group. You can Grant and Revoke database privileges to a principal.

      - **Name** *(string) --*

        The name of the table resource. A table is a metadata definition that represents
        your data. You can Grant and Revoke table privileges to a principal.

      - **ColumnNames** *(list) --*

        The list of column names for the table. At least one of ``ColumnNames`` or
        ``ColumnWildcard`` is required.

        - *(string) --*

      - **ColumnWildcard** *(dict) --*

        A wildcard specified by a ``ColumnWildcard`` object. At least one of
        ``ColumnNames`` or ``ColumnWildcard`` is required.

        - **ExcludedColumnNames** *(list) --*

          Excludes column names. Any column with this name will be excluded.

          - *(string) --*

    - **DataLocation** *(dict) --*

      The location of an Amazon S3 path where permissions are granted or revoked.

      - **ResourceArn** *(string) --*

        The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
    """


_ClientBatchGrantPermissionsResponseFailuresRequestEntryTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresRequestEntryTypeDef",
    {
        "Id": str,
        "Principal": ClientBatchGrantPermissionsResponseFailuresRequestEntryPrincipalTypeDef,
        "Resource": ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTypeDef,
        "Permissions": List[str],
        "PermissionsWithGrantOption": List[str],
    },
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresRequestEntryTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresRequestEntryTypeDef
):
    """
    Type definition for `ClientBatchGrantPermissionsResponseFailures` `RequestEntry`

    An identifier for an entry of the batch request.

    - **Id** *(string) --*

      A unique identifier for the batch permissions request entry.

    - **Principal** *(dict) --*

      The principal to be granted a permission.

      - **DataLakePrincipalIdentifier** *(string) --*

        An identifier for the AWS Lake Formation principal.

    - **Resource** *(dict) --*

      The resource to which the principal is to be granted a permission.

      - **Catalog** *(dict) --*

        The identifier for the Data Catalog. By default, the account ID. The Data Catalog is
        the persistent metadata store. It contains database definitions, table definitions,
        and other control information to manage your AWS Lake Formation environment.

      - **Database** *(dict) --*

        The database for the resource. Unique to the Data Catalog. A database is a set of
        associated table definitions organized into a logical group. You can Grant and Revoke
        database permissions to a principal.

        - **Name** *(string) --*

          The name of the database resource. Unique to the Data Catalog.

      - **Table** *(dict) --*

        The table for the resource. A table is a metadata definition that represents your
        data. You can Grant and Revoke table privileges to a principal.

        - **DatabaseName** *(string) --*

          The name of the database for the table. Unique to a Data Catalog. A database is a
          set of associated table definitions organized into a logical group. You can Grant
          and Revoke database privileges to a principal.

        - **Name** *(string) --*

          The name of the table.

      - **TableWithColumns** *(dict) --*

        The table with columns for the resource. A principal with permissions to this
        resource can select metadata from the columns of a table in the Data Catalog and the
        underlying data in Amazon S3.

        - **DatabaseName** *(string) --*

          The name of the database for the table with columns resource. Unique to the Data
          Catalog. A database is a set of associated table definitions organized into a
          logical group. You can Grant and Revoke database privileges to a principal.

        - **Name** *(string) --*

          The name of the table resource. A table is a metadata definition that represents
          your data. You can Grant and Revoke table privileges to a principal.

        - **ColumnNames** *(list) --*

          The list of column names for the table. At least one of ``ColumnNames`` or
          ``ColumnWildcard`` is required.

          - *(string) --*

        - **ColumnWildcard** *(dict) --*

          A wildcard specified by a ``ColumnWildcard`` object. At least one of
          ``ColumnNames`` or ``ColumnWildcard`` is required.

          - **ExcludedColumnNames** *(list) --*

            Excludes column names. Any column with this name will be excluded.

            - *(string) --*

      - **DataLocation** *(dict) --*

        The location of an Amazon S3 path where permissions are granted or revoked.

        - **ResourceArn** *(string) --*

          The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

    - **Permissions** *(list) --*

      The permissions to be granted.

      - *(string) --*

    - **PermissionsWithGrantOption** *(list) --*

      Indicates if the option to pass permissions is granted.

      - *(string) --*
    """


_ClientBatchGrantPermissionsResponseFailuresTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseFailuresTypeDef",
    {
        "RequestEntry": ClientBatchGrantPermissionsResponseFailuresRequestEntryTypeDef,
        "Error": ClientBatchGrantPermissionsResponseFailuresErrorTypeDef,
    },
    total=False,
)


class ClientBatchGrantPermissionsResponseFailuresTypeDef(
    _ClientBatchGrantPermissionsResponseFailuresTypeDef
):
    """
    Type definition for `ClientBatchGrantPermissionsResponse` `Failures`

    A list of failures when performing a batch grant or batch revoke operation.

    - **RequestEntry** *(dict) --*

      An identifier for an entry of the batch request.

      - **Id** *(string) --*

        A unique identifier for the batch permissions request entry.

      - **Principal** *(dict) --*

        The principal to be granted a permission.

        - **DataLakePrincipalIdentifier** *(string) --*

          An identifier for the AWS Lake Formation principal.

      - **Resource** *(dict) --*

        The resource to which the principal is to be granted a permission.

        - **Catalog** *(dict) --*

          The identifier for the Data Catalog. By default, the account ID. The Data Catalog is
          the persistent metadata store. It contains database definitions, table definitions,
          and other control information to manage your AWS Lake Formation environment.

        - **Database** *(dict) --*

          The database for the resource. Unique to the Data Catalog. A database is a set of
          associated table definitions organized into a logical group. You can Grant and Revoke
          database permissions to a principal.

          - **Name** *(string) --*

            The name of the database resource. Unique to the Data Catalog.

        - **Table** *(dict) --*

          The table for the resource. A table is a metadata definition that represents your
          data. You can Grant and Revoke table privileges to a principal.

          - **DatabaseName** *(string) --*

            The name of the database for the table. Unique to a Data Catalog. A database is a
            set of associated table definitions organized into a logical group. You can Grant
            and Revoke database privileges to a principal.

          - **Name** *(string) --*

            The name of the table.

        - **TableWithColumns** *(dict) --*

          The table with columns for the resource. A principal with permissions to this
          resource can select metadata from the columns of a table in the Data Catalog and the
          underlying data in Amazon S3.

          - **DatabaseName** *(string) --*

            The name of the database for the table with columns resource. Unique to the Data
            Catalog. A database is a set of associated table definitions organized into a
            logical group. You can Grant and Revoke database privileges to a principal.

          - **Name** *(string) --*

            The name of the table resource. A table is a metadata definition that represents
            your data. You can Grant and Revoke table privileges to a principal.

          - **ColumnNames** *(list) --*

            The list of column names for the table. At least one of ``ColumnNames`` or
            ``ColumnWildcard`` is required.

            - *(string) --*

          - **ColumnWildcard** *(dict) --*

            A wildcard specified by a ``ColumnWildcard`` object. At least one of
            ``ColumnNames`` or ``ColumnWildcard`` is required.

            - **ExcludedColumnNames** *(list) --*

              Excludes column names. Any column with this name will be excluded.

              - *(string) --*

        - **DataLocation** *(dict) --*

          The location of an Amazon S3 path where permissions are granted or revoked.

          - **ResourceArn** *(string) --*

            The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

      - **Permissions** *(list) --*

        The permissions to be granted.

        - *(string) --*

      - **PermissionsWithGrantOption** *(list) --*

        Indicates if the option to pass permissions is granted.

        - *(string) --*

    - **Error** *(dict) --*

      An error message that applies to the failure of the entry.

      - **ErrorCode** *(string) --*

        The code associated with this error.

      - **ErrorMessage** *(string) --*

        A message describing the error.
    """


_ClientBatchGrantPermissionsResponseTypeDef = TypedDict(
    "_ClientBatchGrantPermissionsResponseTypeDef",
    {"Failures": List[ClientBatchGrantPermissionsResponseFailuresTypeDef]},
    total=False,
)


class ClientBatchGrantPermissionsResponseTypeDef(
    _ClientBatchGrantPermissionsResponseTypeDef
):
    """
    Type definition for `ClientBatchGrantPermissions` `Response`

    - **Failures** *(list) --*

      A list of failures to grant permissions to the resources.

      - *(dict) --*

        A list of failures when performing a batch grant or batch revoke operation.

        - **RequestEntry** *(dict) --*

          An identifier for an entry of the batch request.

          - **Id** *(string) --*

            A unique identifier for the batch permissions request entry.

          - **Principal** *(dict) --*

            The principal to be granted a permission.

            - **DataLakePrincipalIdentifier** *(string) --*

              An identifier for the AWS Lake Formation principal.

          - **Resource** *(dict) --*

            The resource to which the principal is to be granted a permission.

            - **Catalog** *(dict) --*

              The identifier for the Data Catalog. By default, the account ID. The Data Catalog is
              the persistent metadata store. It contains database definitions, table definitions,
              and other control information to manage your AWS Lake Formation environment.

            - **Database** *(dict) --*

              The database for the resource. Unique to the Data Catalog. A database is a set of
              associated table definitions organized into a logical group. You can Grant and Revoke
              database permissions to a principal.

              - **Name** *(string) --*

                The name of the database resource. Unique to the Data Catalog.

            - **Table** *(dict) --*

              The table for the resource. A table is a metadata definition that represents your
              data. You can Grant and Revoke table privileges to a principal.

              - **DatabaseName** *(string) --*

                The name of the database for the table. Unique to a Data Catalog. A database is a
                set of associated table definitions organized into a logical group. You can Grant
                and Revoke database privileges to a principal.

              - **Name** *(string) --*

                The name of the table.

            - **TableWithColumns** *(dict) --*

              The table with columns for the resource. A principal with permissions to this
              resource can select metadata from the columns of a table in the Data Catalog and the
              underlying data in Amazon S3.

              - **DatabaseName** *(string) --*

                The name of the database for the table with columns resource. Unique to the Data
                Catalog. A database is a set of associated table definitions organized into a
                logical group. You can Grant and Revoke database privileges to a principal.

              - **Name** *(string) --*

                The name of the table resource. A table is a metadata definition that represents
                your data. You can Grant and Revoke table privileges to a principal.

              - **ColumnNames** *(list) --*

                The list of column names for the table. At least one of ``ColumnNames`` or
                ``ColumnWildcard`` is required.

                - *(string) --*

              - **ColumnWildcard** *(dict) --*

                A wildcard specified by a ``ColumnWildcard`` object. At least one of
                ``ColumnNames`` or ``ColumnWildcard`` is required.

                - **ExcludedColumnNames** *(list) --*

                  Excludes column names. Any column with this name will be excluded.

                  - *(string) --*

            - **DataLocation** *(dict) --*

              The location of an Amazon S3 path where permissions are granted or revoked.

              - **ResourceArn** *(string) --*

                The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

          - **Permissions** *(list) --*

            The permissions to be granted.

            - *(string) --*

          - **PermissionsWithGrantOption** *(list) --*

            Indicates if the option to pass permissions is granted.

            - *(string) --*

        - **Error** *(dict) --*

          An error message that applies to the failure of the entry.

          - **ErrorCode** *(string) --*

            The code associated with this error.

          - **ErrorMessage** *(string) --*

            A message describing the error.
    """


_ClientBatchRevokePermissionsEntriesPrincipalTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsEntriesPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientBatchRevokePermissionsEntriesPrincipalTypeDef(
    _ClientBatchRevokePermissionsEntriesPrincipalTypeDef
):
    """
    Type definition for `ClientBatchRevokePermissionsEntries` `Principal`

    The principal to be granted a permission.

    - **DataLakePrincipalIdentifier** *(string) --*

      An identifier for the AWS Lake Formation principal.
    """


_ClientBatchRevokePermissionsEntriesResourceDataLocationTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsEntriesResourceDataLocationTypeDef",
    {"ResourceArn": str},
)


class ClientBatchRevokePermissionsEntriesResourceDataLocationTypeDef(
    _ClientBatchRevokePermissionsEntriesResourceDataLocationTypeDef
):
    """
    Type definition for `ClientBatchRevokePermissionsEntriesResource` `DataLocation`

    The location of an Amazon S3 path where permissions are granted or revoked.

    - **ResourceArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
    """


_ClientBatchRevokePermissionsEntriesResourceDatabaseTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsEntriesResourceDatabaseTypeDef", {"Name": str}
)


class ClientBatchRevokePermissionsEntriesResourceDatabaseTypeDef(
    _ClientBatchRevokePermissionsEntriesResourceDatabaseTypeDef
):
    """
    Type definition for `ClientBatchRevokePermissionsEntriesResource` `Database`

    The database for the resource. Unique to the Data Catalog. A database is a set of
    associated table definitions organized into a logical group. You can Grant and Revoke
    database permissions to a principal.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the database resource. Unique to the Data Catalog.
    """


_ClientBatchRevokePermissionsEntriesResourceTableTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsEntriesResourceTableTypeDef",
    {"DatabaseName": str, "Name": str},
)


class ClientBatchRevokePermissionsEntriesResourceTableTypeDef(
    _ClientBatchRevokePermissionsEntriesResourceTableTypeDef
):
    """
    Type definition for `ClientBatchRevokePermissionsEntriesResource` `Table`

    The table for the resource. A table is a metadata definition that represents your data. You
    can Grant and Revoke table privileges to a principal.

    - **DatabaseName** *(string) --* **[REQUIRED]**

      The name of the database for the table. Unique to a Data Catalog. A database is a set of
      associated table definitions organized into a logical group. You can Grant and Revoke
      database privileges to a principal.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the table.
    """


_ClientBatchRevokePermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)


class ClientBatchRevokePermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef(
    _ClientBatchRevokePermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef
):
    """
    Type definition for `ClientBatchRevokePermissionsEntriesResourceTableWithColumns` `ColumnWildcard`

    A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
    ``ColumnWildcard`` is required.

    - **ExcludedColumnNames** *(list) --*

      Excludes column names. Any column with this name will be excluded.

      - *(string) --*
    """


_ClientBatchRevokePermissionsEntriesResourceTableWithColumnsTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsEntriesResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientBatchRevokePermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)


class ClientBatchRevokePermissionsEntriesResourceTableWithColumnsTypeDef(
    _ClientBatchRevokePermissionsEntriesResourceTableWithColumnsTypeDef
):
    """
    Type definition for `ClientBatchRevokePermissionsEntriesResource` `TableWithColumns`

    The table with columns for the resource. A principal with permissions to this resource can
    select metadata from the columns of a table in the Data Catalog and the underlying data in
    Amazon S3.

    - **DatabaseName** *(string) --*

      The name of the database for the table with columns resource. Unique to the Data Catalog.
      A database is a set of associated table definitions organized into a logical group. You
      can Grant and Revoke database privileges to a principal.

    - **Name** *(string) --*

      The name of the table resource. A table is a metadata definition that represents your
      data. You can Grant and Revoke table privileges to a principal.

    - **ColumnNames** *(list) --*

      The list of column names for the table. At least one of ``ColumnNames`` or
      ``ColumnWildcard`` is required.

      - *(string) --*

    - **ColumnWildcard** *(dict) --*

      A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
      ``ColumnWildcard`` is required.

      - **ExcludedColumnNames** *(list) --*

        Excludes column names. Any column with this name will be excluded.

        - *(string) --*
    """


_ClientBatchRevokePermissionsEntriesResourceTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsEntriesResourceTypeDef",
    {
        "Catalog": Dict,
        "Database": ClientBatchRevokePermissionsEntriesResourceDatabaseTypeDef,
        "Table": ClientBatchRevokePermissionsEntriesResourceTableTypeDef,
        "TableWithColumns": ClientBatchRevokePermissionsEntriesResourceTableWithColumnsTypeDef,
        "DataLocation": ClientBatchRevokePermissionsEntriesResourceDataLocationTypeDef,
    },
    total=False,
)


class ClientBatchRevokePermissionsEntriesResourceTypeDef(
    _ClientBatchRevokePermissionsEntriesResourceTypeDef
):
    """
    Type definition for `ClientBatchRevokePermissionsEntries` `Resource`

    The resource to which the principal is to be granted a permission.

    - **Catalog** *(dict) --*

      The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
      persistent metadata store. It contains database definitions, table definitions, and other
      control information to manage your AWS Lake Formation environment.

    - **Database** *(dict) --*

      The database for the resource. Unique to the Data Catalog. A database is a set of
      associated table definitions organized into a logical group. You can Grant and Revoke
      database permissions to a principal.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the database resource. Unique to the Data Catalog.

    - **Table** *(dict) --*

      The table for the resource. A table is a metadata definition that represents your data. You
      can Grant and Revoke table privileges to a principal.

      - **DatabaseName** *(string) --* **[REQUIRED]**

        The name of the database for the table. Unique to a Data Catalog. A database is a set of
        associated table definitions organized into a logical group. You can Grant and Revoke
        database privileges to a principal.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the table.

    - **TableWithColumns** *(dict) --*

      The table with columns for the resource. A principal with permissions to this resource can
      select metadata from the columns of a table in the Data Catalog and the underlying data in
      Amazon S3.

      - **DatabaseName** *(string) --*

        The name of the database for the table with columns resource. Unique to the Data Catalog.
        A database is a set of associated table definitions organized into a logical group. You
        can Grant and Revoke database privileges to a principal.

      - **Name** *(string) --*

        The name of the table resource. A table is a metadata definition that represents your
        data. You can Grant and Revoke table privileges to a principal.

      - **ColumnNames** *(list) --*

        The list of column names for the table. At least one of ``ColumnNames`` or
        ``ColumnWildcard`` is required.

        - *(string) --*

      - **ColumnWildcard** *(dict) --*

        A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
        ``ColumnWildcard`` is required.

        - **ExcludedColumnNames** *(list) --*

          Excludes column names. Any column with this name will be excluded.

          - *(string) --*

    - **DataLocation** *(dict) --*

      The location of an Amazon S3 path where permissions are granted or revoked.

      - **ResourceArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
    """


_RequiredClientBatchRevokePermissionsEntriesTypeDef = TypedDict(
    "_RequiredClientBatchRevokePermissionsEntriesTypeDef", {"Id": str}
)
_OptionalClientBatchRevokePermissionsEntriesTypeDef = TypedDict(
    "_OptionalClientBatchRevokePermissionsEntriesTypeDef",
    {
        "Principal": ClientBatchRevokePermissionsEntriesPrincipalTypeDef,
        "Resource": ClientBatchRevokePermissionsEntriesResourceTypeDef,
        "Permissions": List[str],
        "PermissionsWithGrantOption": List[str],
    },
    total=False,
)


class ClientBatchRevokePermissionsEntriesTypeDef(
    _RequiredClientBatchRevokePermissionsEntriesTypeDef,
    _OptionalClientBatchRevokePermissionsEntriesTypeDef,
):
    """
    Type definition for `ClientBatchRevokePermissions` `Entries`

    A permission to a resource granted by batch operation to the principal.

    - **Id** *(string) --* **[REQUIRED]**

      A unique identifier for the batch permissions request entry.

    - **Principal** *(dict) --*

      The principal to be granted a permission.

      - **DataLakePrincipalIdentifier** *(string) --*

        An identifier for the AWS Lake Formation principal.

    - **Resource** *(dict) --*

      The resource to which the principal is to be granted a permission.

      - **Catalog** *(dict) --*

        The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
        persistent metadata store. It contains database definitions, table definitions, and other
        control information to manage your AWS Lake Formation environment.

      - **Database** *(dict) --*

        The database for the resource. Unique to the Data Catalog. A database is a set of
        associated table definitions organized into a logical group. You can Grant and Revoke
        database permissions to a principal.

        - **Name** *(string) --* **[REQUIRED]**

          The name of the database resource. Unique to the Data Catalog.

      - **Table** *(dict) --*

        The table for the resource. A table is a metadata definition that represents your data. You
        can Grant and Revoke table privileges to a principal.

        - **DatabaseName** *(string) --* **[REQUIRED]**

          The name of the database for the table. Unique to a Data Catalog. A database is a set of
          associated table definitions organized into a logical group. You can Grant and Revoke
          database privileges to a principal.

        - **Name** *(string) --* **[REQUIRED]**

          The name of the table.

      - **TableWithColumns** *(dict) --*

        The table with columns for the resource. A principal with permissions to this resource can
        select metadata from the columns of a table in the Data Catalog and the underlying data in
        Amazon S3.

        - **DatabaseName** *(string) --*

          The name of the database for the table with columns resource. Unique to the Data Catalog.
          A database is a set of associated table definitions organized into a logical group. You
          can Grant and Revoke database privileges to a principal.

        - **Name** *(string) --*

          The name of the table resource. A table is a metadata definition that represents your
          data. You can Grant and Revoke table privileges to a principal.

        - **ColumnNames** *(list) --*

          The list of column names for the table. At least one of ``ColumnNames`` or
          ``ColumnWildcard`` is required.

          - *(string) --*

        - **ColumnWildcard** *(dict) --*

          A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
          ``ColumnWildcard`` is required.

          - **ExcludedColumnNames** *(list) --*

            Excludes column names. Any column with this name will be excluded.

            - *(string) --*

      - **DataLocation** *(dict) --*

        The location of an Amazon S3 path where permissions are granted or revoked.

        - **ResourceArn** *(string) --* **[REQUIRED]**

          The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

    - **Permissions** *(list) --*

      The permissions to be granted.

      - *(string) --*

    - **PermissionsWithGrantOption** *(list) --*

      Indicates if the option to pass permissions is granted.

      - *(string) --*
    """


_ClientBatchRevokePermissionsResponseFailuresErrorTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresErrorTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresErrorTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresErrorTypeDef
):
    """
    Type definition for `ClientBatchRevokePermissionsResponseFailures` `Error`

    An error message that applies to the failure of the entry.

    - **ErrorCode** *(string) --*

      The code associated with this error.

    - **ErrorMessage** *(string) --*

      A message describing the error.
    """


_ClientBatchRevokePermissionsResponseFailuresRequestEntryPrincipalTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresRequestEntryPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresRequestEntryPrincipalTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresRequestEntryPrincipalTypeDef
):
    """
    Type definition for `ClientBatchRevokePermissionsResponseFailuresRequestEntry` `Principal`

    The principal to be granted a permission.

    - **DataLakePrincipalIdentifier** *(string) --*

      An identifier for the AWS Lake Formation principal.
    """


_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef",
    {"ResourceArn": str},
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef
):
    """
    Type definition for `ClientBatchRevokePermissionsResponseFailuresRequestEntryResource` `DataLocation`

    The location of an Amazon S3 path where permissions are granted or revoked.

    - **ResourceArn** *(string) --*

      The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
    """


_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef",
    {"Name": str},
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef
):
    """
    Type definition for `ClientBatchRevokePermissionsResponseFailuresRequestEntryResource` `Database`

    The database for the resource. Unique to the Data Catalog. A database is a set of
    associated table definitions organized into a logical group. You can Grant and Revoke
    database permissions to a principal.

    - **Name** *(string) --*

      The name of the database resource. Unique to the Data Catalog.
    """


_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableTypeDef",
    {"DatabaseName": str, "Name": str},
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableTypeDef
):
    """
    Type definition for `ClientBatchRevokePermissionsResponseFailuresRequestEntryResource` `Table`

    The table for the resource. A table is a metadata definition that represents your
    data. You can Grant and Revoke table privileges to a principal.

    - **DatabaseName** *(string) --*

      The name of the database for the table. Unique to a Data Catalog. A database is a
      set of associated table definitions organized into a logical group. You can Grant
      and Revoke database privileges to a principal.

    - **Name** *(string) --*

      The name of the table.
    """


_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef
):
    """
    Type definition for `ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumns` `ColumnWildcard`

    A wildcard specified by a ``ColumnWildcard`` object. At least one of
    ``ColumnNames`` or ``ColumnWildcard`` is required.

    - **ExcludedColumnNames** *(list) --*

      Excludes column names. Any column with this name will be excluded.

      - *(string) --*
    """


_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef
):
    """
    Type definition for `ClientBatchRevokePermissionsResponseFailuresRequestEntryResource` `TableWithColumns`

    The table with columns for the resource. A principal with permissions to this
    resource can select metadata from the columns of a table in the Data Catalog and the
    underlying data in Amazon S3.

    - **DatabaseName** *(string) --*

      The name of the database for the table with columns resource. Unique to the Data
      Catalog. A database is a set of associated table definitions organized into a
      logical group. You can Grant and Revoke database privileges to a principal.

    - **Name** *(string) --*

      The name of the table resource. A table is a metadata definition that represents
      your data. You can Grant and Revoke table privileges to a principal.

    - **ColumnNames** *(list) --*

      The list of column names for the table. At least one of ``ColumnNames`` or
      ``ColumnWildcard`` is required.

      - *(string) --*

    - **ColumnWildcard** *(dict) --*

      A wildcard specified by a ``ColumnWildcard`` object. At least one of
      ``ColumnNames`` or ``ColumnWildcard`` is required.

      - **ExcludedColumnNames** *(list) --*

        Excludes column names. Any column with this name will be excluded.

        - *(string) --*
    """


_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTypeDef",
    {
        "Catalog": Dict,
        "Database": ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef,
        "Table": ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableTypeDef,
        "TableWithColumns": ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef,
        "DataLocation": ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef,
    },
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTypeDef
):
    """
    Type definition for `ClientBatchRevokePermissionsResponseFailuresRequestEntry` `Resource`

    The resource to which the principal is to be granted a permission.

    - **Catalog** *(dict) --*

      The identifier for the Data Catalog. By default, the account ID. The Data Catalog is
      the persistent metadata store. It contains database definitions, table definitions,
      and other control information to manage your AWS Lake Formation environment.

    - **Database** *(dict) --*

      The database for the resource. Unique to the Data Catalog. A database is a set of
      associated table definitions organized into a logical group. You can Grant and Revoke
      database permissions to a principal.

      - **Name** *(string) --*

        The name of the database resource. Unique to the Data Catalog.

    - **Table** *(dict) --*

      The table for the resource. A table is a metadata definition that represents your
      data. You can Grant and Revoke table privileges to a principal.

      - **DatabaseName** *(string) --*

        The name of the database for the table. Unique to a Data Catalog. A database is a
        set of associated table definitions organized into a logical group. You can Grant
        and Revoke database privileges to a principal.

      - **Name** *(string) --*

        The name of the table.

    - **TableWithColumns** *(dict) --*

      The table with columns for the resource. A principal with permissions to this
      resource can select metadata from the columns of a table in the Data Catalog and the
      underlying data in Amazon S3.

      - **DatabaseName** *(string) --*

        The name of the database for the table with columns resource. Unique to the Data
        Catalog. A database is a set of associated table definitions organized into a
        logical group. You can Grant and Revoke database privileges to a principal.

      - **Name** *(string) --*

        The name of the table resource. A table is a metadata definition that represents
        your data. You can Grant and Revoke table privileges to a principal.

      - **ColumnNames** *(list) --*

        The list of column names for the table. At least one of ``ColumnNames`` or
        ``ColumnWildcard`` is required.

        - *(string) --*

      - **ColumnWildcard** *(dict) --*

        A wildcard specified by a ``ColumnWildcard`` object. At least one of
        ``ColumnNames`` or ``ColumnWildcard`` is required.

        - **ExcludedColumnNames** *(list) --*

          Excludes column names. Any column with this name will be excluded.

          - *(string) --*

    - **DataLocation** *(dict) --*

      The location of an Amazon S3 path where permissions are granted or revoked.

      - **ResourceArn** *(string) --*

        The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
    """


_ClientBatchRevokePermissionsResponseFailuresRequestEntryTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresRequestEntryTypeDef",
    {
        "Id": str,
        "Principal": ClientBatchRevokePermissionsResponseFailuresRequestEntryPrincipalTypeDef,
        "Resource": ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTypeDef,
        "Permissions": List[str],
        "PermissionsWithGrantOption": List[str],
    },
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresRequestEntryTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresRequestEntryTypeDef
):
    """
    Type definition for `ClientBatchRevokePermissionsResponseFailures` `RequestEntry`

    An identifier for an entry of the batch request.

    - **Id** *(string) --*

      A unique identifier for the batch permissions request entry.

    - **Principal** *(dict) --*

      The principal to be granted a permission.

      - **DataLakePrincipalIdentifier** *(string) --*

        An identifier for the AWS Lake Formation principal.

    - **Resource** *(dict) --*

      The resource to which the principal is to be granted a permission.

      - **Catalog** *(dict) --*

        The identifier for the Data Catalog. By default, the account ID. The Data Catalog is
        the persistent metadata store. It contains database definitions, table definitions,
        and other control information to manage your AWS Lake Formation environment.

      - **Database** *(dict) --*

        The database for the resource. Unique to the Data Catalog. A database is a set of
        associated table definitions organized into a logical group. You can Grant and Revoke
        database permissions to a principal.

        - **Name** *(string) --*

          The name of the database resource. Unique to the Data Catalog.

      - **Table** *(dict) --*

        The table for the resource. A table is a metadata definition that represents your
        data. You can Grant and Revoke table privileges to a principal.

        - **DatabaseName** *(string) --*

          The name of the database for the table. Unique to a Data Catalog. A database is a
          set of associated table definitions organized into a logical group. You can Grant
          and Revoke database privileges to a principal.

        - **Name** *(string) --*

          The name of the table.

      - **TableWithColumns** *(dict) --*

        The table with columns for the resource. A principal with permissions to this
        resource can select metadata from the columns of a table in the Data Catalog and the
        underlying data in Amazon S3.

        - **DatabaseName** *(string) --*

          The name of the database for the table with columns resource. Unique to the Data
          Catalog. A database is a set of associated table definitions organized into a
          logical group. You can Grant and Revoke database privileges to a principal.

        - **Name** *(string) --*

          The name of the table resource. A table is a metadata definition that represents
          your data. You can Grant and Revoke table privileges to a principal.

        - **ColumnNames** *(list) --*

          The list of column names for the table. At least one of ``ColumnNames`` or
          ``ColumnWildcard`` is required.

          - *(string) --*

        - **ColumnWildcard** *(dict) --*

          A wildcard specified by a ``ColumnWildcard`` object. At least one of
          ``ColumnNames`` or ``ColumnWildcard`` is required.

          - **ExcludedColumnNames** *(list) --*

            Excludes column names. Any column with this name will be excluded.

            - *(string) --*

      - **DataLocation** *(dict) --*

        The location of an Amazon S3 path where permissions are granted or revoked.

        - **ResourceArn** *(string) --*

          The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

    - **Permissions** *(list) --*

      The permissions to be granted.

      - *(string) --*

    - **PermissionsWithGrantOption** *(list) --*

      Indicates if the option to pass permissions is granted.

      - *(string) --*
    """


_ClientBatchRevokePermissionsResponseFailuresTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseFailuresTypeDef",
    {
        "RequestEntry": ClientBatchRevokePermissionsResponseFailuresRequestEntryTypeDef,
        "Error": ClientBatchRevokePermissionsResponseFailuresErrorTypeDef,
    },
    total=False,
)


class ClientBatchRevokePermissionsResponseFailuresTypeDef(
    _ClientBatchRevokePermissionsResponseFailuresTypeDef
):
    """
    Type definition for `ClientBatchRevokePermissionsResponse` `Failures`

    A list of failures when performing a batch grant or batch revoke operation.

    - **RequestEntry** *(dict) --*

      An identifier for an entry of the batch request.

      - **Id** *(string) --*

        A unique identifier for the batch permissions request entry.

      - **Principal** *(dict) --*

        The principal to be granted a permission.

        - **DataLakePrincipalIdentifier** *(string) --*

          An identifier for the AWS Lake Formation principal.

      - **Resource** *(dict) --*

        The resource to which the principal is to be granted a permission.

        - **Catalog** *(dict) --*

          The identifier for the Data Catalog. By default, the account ID. The Data Catalog is
          the persistent metadata store. It contains database definitions, table definitions,
          and other control information to manage your AWS Lake Formation environment.

        - **Database** *(dict) --*

          The database for the resource. Unique to the Data Catalog. A database is a set of
          associated table definitions organized into a logical group. You can Grant and Revoke
          database permissions to a principal.

          - **Name** *(string) --*

            The name of the database resource. Unique to the Data Catalog.

        - **Table** *(dict) --*

          The table for the resource. A table is a metadata definition that represents your
          data. You can Grant and Revoke table privileges to a principal.

          - **DatabaseName** *(string) --*

            The name of the database for the table. Unique to a Data Catalog. A database is a
            set of associated table definitions organized into a logical group. You can Grant
            and Revoke database privileges to a principal.

          - **Name** *(string) --*

            The name of the table.

        - **TableWithColumns** *(dict) --*

          The table with columns for the resource. A principal with permissions to this
          resource can select metadata from the columns of a table in the Data Catalog and the
          underlying data in Amazon S3.

          - **DatabaseName** *(string) --*

            The name of the database for the table with columns resource. Unique to the Data
            Catalog. A database is a set of associated table definitions organized into a
            logical group. You can Grant and Revoke database privileges to a principal.

          - **Name** *(string) --*

            The name of the table resource. A table is a metadata definition that represents
            your data. You can Grant and Revoke table privileges to a principal.

          - **ColumnNames** *(list) --*

            The list of column names for the table. At least one of ``ColumnNames`` or
            ``ColumnWildcard`` is required.

            - *(string) --*

          - **ColumnWildcard** *(dict) --*

            A wildcard specified by a ``ColumnWildcard`` object. At least one of
            ``ColumnNames`` or ``ColumnWildcard`` is required.

            - **ExcludedColumnNames** *(list) --*

              Excludes column names. Any column with this name will be excluded.

              - *(string) --*

        - **DataLocation** *(dict) --*

          The location of an Amazon S3 path where permissions are granted or revoked.

          - **ResourceArn** *(string) --*

            The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

      - **Permissions** *(list) --*

        The permissions to be granted.

        - *(string) --*

      - **PermissionsWithGrantOption** *(list) --*

        Indicates if the option to pass permissions is granted.

        - *(string) --*

    - **Error** *(dict) --*

      An error message that applies to the failure of the entry.

      - **ErrorCode** *(string) --*

        The code associated with this error.

      - **ErrorMessage** *(string) --*

        A message describing the error.
    """


_ClientBatchRevokePermissionsResponseTypeDef = TypedDict(
    "_ClientBatchRevokePermissionsResponseTypeDef",
    {"Failures": List[ClientBatchRevokePermissionsResponseFailuresTypeDef]},
    total=False,
)


class ClientBatchRevokePermissionsResponseTypeDef(
    _ClientBatchRevokePermissionsResponseTypeDef
):
    """
    Type definition for `ClientBatchRevokePermissions` `Response`

    - **Failures** *(list) --*

      A list of failures to revoke permissions to the resources.

      - *(dict) --*

        A list of failures when performing a batch grant or batch revoke operation.

        - **RequestEntry** *(dict) --*

          An identifier for an entry of the batch request.

          - **Id** *(string) --*

            A unique identifier for the batch permissions request entry.

          - **Principal** *(dict) --*

            The principal to be granted a permission.

            - **DataLakePrincipalIdentifier** *(string) --*

              An identifier for the AWS Lake Formation principal.

          - **Resource** *(dict) --*

            The resource to which the principal is to be granted a permission.

            - **Catalog** *(dict) --*

              The identifier for the Data Catalog. By default, the account ID. The Data Catalog is
              the persistent metadata store. It contains database definitions, table definitions,
              and other control information to manage your AWS Lake Formation environment.

            - **Database** *(dict) --*

              The database for the resource. Unique to the Data Catalog. A database is a set of
              associated table definitions organized into a logical group. You can Grant and Revoke
              database permissions to a principal.

              - **Name** *(string) --*

                The name of the database resource. Unique to the Data Catalog.

            - **Table** *(dict) --*

              The table for the resource. A table is a metadata definition that represents your
              data. You can Grant and Revoke table privileges to a principal.

              - **DatabaseName** *(string) --*

                The name of the database for the table. Unique to a Data Catalog. A database is a
                set of associated table definitions organized into a logical group. You can Grant
                and Revoke database privileges to a principal.

              - **Name** *(string) --*

                The name of the table.

            - **TableWithColumns** *(dict) --*

              The table with columns for the resource. A principal with permissions to this
              resource can select metadata from the columns of a table in the Data Catalog and the
              underlying data in Amazon S3.

              - **DatabaseName** *(string) --*

                The name of the database for the table with columns resource. Unique to the Data
                Catalog. A database is a set of associated table definitions organized into a
                logical group. You can Grant and Revoke database privileges to a principal.

              - **Name** *(string) --*

                The name of the table resource. A table is a metadata definition that represents
                your data. You can Grant and Revoke table privileges to a principal.

              - **ColumnNames** *(list) --*

                The list of column names for the table. At least one of ``ColumnNames`` or
                ``ColumnWildcard`` is required.

                - *(string) --*

              - **ColumnWildcard** *(dict) --*

                A wildcard specified by a ``ColumnWildcard`` object. At least one of
                ``ColumnNames`` or ``ColumnWildcard`` is required.

                - **ExcludedColumnNames** *(list) --*

                  Excludes column names. Any column with this name will be excluded.

                  - *(string) --*

            - **DataLocation** *(dict) --*

              The location of an Amazon S3 path where permissions are granted or revoked.

              - **ResourceArn** *(string) --*

                The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

          - **Permissions** *(list) --*

            The permissions to be granted.

            - *(string) --*

          - **PermissionsWithGrantOption** *(list) --*

            Indicates if the option to pass permissions is granted.

            - *(string) --*

        - **Error** *(dict) --*

          An error message that applies to the failure of the entry.

          - **ErrorCode** *(string) --*

            The code associated with this error.

          - **ErrorMessage** *(string) --*

            A message describing the error.
    """


_ClientDescribeResourceResponseResourceInfoTypeDef = TypedDict(
    "_ClientDescribeResourceResponseResourceInfoTypeDef",
    {"ResourceArn": str, "RoleArn": str, "LastModified": datetime},
    total=False,
)


class ClientDescribeResourceResponseResourceInfoTypeDef(
    _ClientDescribeResourceResponseResourceInfoTypeDef
):
    """
    Type definition for `ClientDescribeResourceResponse` `ResourceInfo`

    A structure containing information about an AWS Lake Formation resource.

    - **ResourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource.

    - **RoleArn** *(string) --*

      The IAM role that registered a resource.

    - **LastModified** *(datetime) --*

      The date and time the resource was last modified.
    """


_ClientDescribeResourceResponseTypeDef = TypedDict(
    "_ClientDescribeResourceResponseTypeDef",
    {"ResourceInfo": ClientDescribeResourceResponseResourceInfoTypeDef},
    total=False,
)


class ClientDescribeResourceResponseTypeDef(_ClientDescribeResourceResponseTypeDef):
    """
    Type definition for `ClientDescribeResource` `Response`

    - **ResourceInfo** *(dict) --*

      A structure containing information about an AWS Lake Formation resource.

      - **ResourceArn** *(string) --*

        The Amazon Resource Name (ARN) of the resource.

      - **RoleArn** *(string) --*

        The IAM role that registered a resource.

      - **LastModified** *(datetime) --*

        The date and time the resource was last modified.
    """


_ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef = TypedDict(
    "_ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef(
    _ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef
):
    """
    Type definition for `ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissions` `Principal`

    The principal who is granted permissions.

    - **DataLakePrincipalIdentifier** *(string) --*

      An identifier for the AWS Lake Formation principal.
    """


_ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef = TypedDict(
    "_ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef",
    {
        "Principal": ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[str],
    },
    total=False,
)


class ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef(
    _ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef
):
    """
    Type definition for `ClientGetDataLakeSettingsResponseDataLakeSettings` `CreateDatabaseDefaultPermissions`

    Permissions granted to a principal.

    - **Principal** *(dict) --*

      The principal who is granted permissions.

      - **DataLakePrincipalIdentifier** *(string) --*

        An identifier for the AWS Lake Formation principal.

    - **Permissions** *(list) --*

      The permissions that are granted to the principal.

      - *(string) --*
    """


_ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef = TypedDict(
    "_ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef(
    _ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef
):
    """
    Type definition for `ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissions` `Principal`

    The principal who is granted permissions.

    - **DataLakePrincipalIdentifier** *(string) --*

      An identifier for the AWS Lake Formation principal.
    """


_ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsTypeDef = TypedDict(
    "_ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsTypeDef",
    {
        "Principal": ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[str],
    },
    total=False,
)


class ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsTypeDef(
    _ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsTypeDef
):
    """
    Type definition for `ClientGetDataLakeSettingsResponseDataLakeSettings` `CreateTableDefaultPermissions`

    Permissions granted to a principal.

    - **Principal** *(dict) --*

      The principal who is granted permissions.

      - **DataLakePrincipalIdentifier** *(string) --*

        An identifier for the AWS Lake Formation principal.

    - **Permissions** *(list) --*

      The permissions that are granted to the principal.

      - *(string) --*
    """


_ClientGetDataLakeSettingsResponseDataLakeSettingsDataLakeAdminsTypeDef = TypedDict(
    "_ClientGetDataLakeSettingsResponseDataLakeSettingsDataLakeAdminsTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientGetDataLakeSettingsResponseDataLakeSettingsDataLakeAdminsTypeDef(
    _ClientGetDataLakeSettingsResponseDataLakeSettingsDataLakeAdminsTypeDef
):
    """
    Type definition for `ClientGetDataLakeSettingsResponseDataLakeSettings` `DataLakeAdmins`

    The AWS Lake Formation principal.

    - **DataLakePrincipalIdentifier** *(string) --*

      An identifier for the AWS Lake Formation principal.
    """


_ClientGetDataLakeSettingsResponseDataLakeSettingsTypeDef = TypedDict(
    "_ClientGetDataLakeSettingsResponseDataLakeSettingsTypeDef",
    {
        "DataLakeAdmins": List[
            ClientGetDataLakeSettingsResponseDataLakeSettingsDataLakeAdminsTypeDef
        ],
        "CreateDatabaseDefaultPermissions": List[
            ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef
        ],
        "CreateTableDefaultPermissions": List[
            ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsTypeDef
        ],
    },
    total=False,
)


class ClientGetDataLakeSettingsResponseDataLakeSettingsTypeDef(
    _ClientGetDataLakeSettingsResponseDataLakeSettingsTypeDef
):
    """
    Type definition for `ClientGetDataLakeSettingsResponse` `DataLakeSettings`

    A list of AWS Lake Formation principals.

    - **DataLakeAdmins** *(list) --*

      A list of AWS Lake Formation principals.

      - *(dict) --*

        The AWS Lake Formation principal.

        - **DataLakePrincipalIdentifier** *(string) --*

          An identifier for the AWS Lake Formation principal.

    - **CreateDatabaseDefaultPermissions** *(list) --*

      A list of up to three principal permissions entries for default create database permissions.

      - *(dict) --*

        Permissions granted to a principal.

        - **Principal** *(dict) --*

          The principal who is granted permissions.

          - **DataLakePrincipalIdentifier** *(string) --*

            An identifier for the AWS Lake Formation principal.

        - **Permissions** *(list) --*

          The permissions that are granted to the principal.

          - *(string) --*

    - **CreateTableDefaultPermissions** *(list) --*

      A list of up to three principal permissions entries for default create table permissions.

      - *(dict) --*

        Permissions granted to a principal.

        - **Principal** *(dict) --*

          The principal who is granted permissions.

          - **DataLakePrincipalIdentifier** *(string) --*

            An identifier for the AWS Lake Formation principal.

        - **Permissions** *(list) --*

          The permissions that are granted to the principal.

          - *(string) --*
    """


_ClientGetDataLakeSettingsResponseTypeDef = TypedDict(
    "_ClientGetDataLakeSettingsResponseTypeDef",
    {"DataLakeSettings": ClientGetDataLakeSettingsResponseDataLakeSettingsTypeDef},
    total=False,
)


class ClientGetDataLakeSettingsResponseTypeDef(
    _ClientGetDataLakeSettingsResponseTypeDef
):
    """
    Type definition for `ClientGetDataLakeSettings` `Response`

    - **DataLakeSettings** *(dict) --*

      A list of AWS Lake Formation principals.

      - **DataLakeAdmins** *(list) --*

        A list of AWS Lake Formation principals.

        - *(dict) --*

          The AWS Lake Formation principal.

          - **DataLakePrincipalIdentifier** *(string) --*

            An identifier for the AWS Lake Formation principal.

      - **CreateDatabaseDefaultPermissions** *(list) --*

        A list of up to three principal permissions entries for default create database permissions.

        - *(dict) --*

          Permissions granted to a principal.

          - **Principal** *(dict) --*

            The principal who is granted permissions.

            - **DataLakePrincipalIdentifier** *(string) --*

              An identifier for the AWS Lake Formation principal.

          - **Permissions** *(list) --*

            The permissions that are granted to the principal.

            - *(string) --*

      - **CreateTableDefaultPermissions** *(list) --*

        A list of up to three principal permissions entries for default create table permissions.

        - *(dict) --*

          Permissions granted to a principal.

          - **Principal** *(dict) --*

            The principal who is granted permissions.

            - **DataLakePrincipalIdentifier** *(string) --*

              An identifier for the AWS Lake Formation principal.

          - **Permissions** *(list) --*

            The permissions that are granted to the principal.

            - *(string) --*
    """


_ClientGetEffectivePermissionsForPathResponsePermissionsPrincipalTypeDef = TypedDict(
    "_ClientGetEffectivePermissionsForPathResponsePermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientGetEffectivePermissionsForPathResponsePermissionsPrincipalTypeDef(
    _ClientGetEffectivePermissionsForPathResponsePermissionsPrincipalTypeDef
):
    """
    Type definition for `ClientGetEffectivePermissionsForPathResponsePermissions` `Principal`

    The Data Lake principal to be granted or revoked permissions.

    - **DataLakePrincipalIdentifier** *(string) --*

      An identifier for the AWS Lake Formation principal.
    """


_ClientGetEffectivePermissionsForPathResponsePermissionsResourceDataLocationTypeDef = TypedDict(
    "_ClientGetEffectivePermissionsForPathResponsePermissionsResourceDataLocationTypeDef",
    {"ResourceArn": str},
    total=False,
)


class ClientGetEffectivePermissionsForPathResponsePermissionsResourceDataLocationTypeDef(
    _ClientGetEffectivePermissionsForPathResponsePermissionsResourceDataLocationTypeDef
):
    """
    Type definition for `ClientGetEffectivePermissionsForPathResponsePermissionsResource` `DataLocation`

    The location of an Amazon S3 path where permissions are granted or revoked.

    - **ResourceArn** *(string) --*

      The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
    """


_ClientGetEffectivePermissionsForPathResponsePermissionsResourceDatabaseTypeDef = TypedDict(
    "_ClientGetEffectivePermissionsForPathResponsePermissionsResourceDatabaseTypeDef",
    {"Name": str},
    total=False,
)


class ClientGetEffectivePermissionsForPathResponsePermissionsResourceDatabaseTypeDef(
    _ClientGetEffectivePermissionsForPathResponsePermissionsResourceDatabaseTypeDef
):
    """
    Type definition for `ClientGetEffectivePermissionsForPathResponsePermissionsResource` `Database`

    The database for the resource. Unique to the Data Catalog. A database is a set of
    associated table definitions organized into a logical group. You can Grant and Revoke
    database permissions to a principal.

    - **Name** *(string) --*

      The name of the database resource. Unique to the Data Catalog.
    """


_ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableTypeDef = TypedDict(
    "_ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableTypeDef",
    {"DatabaseName": str, "Name": str},
    total=False,
)


class ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableTypeDef(
    _ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableTypeDef
):
    """
    Type definition for `ClientGetEffectivePermissionsForPathResponsePermissionsResource` `Table`

    The table for the resource. A table is a metadata definition that represents your data.
    You can Grant and Revoke table privileges to a principal.

    - **DatabaseName** *(string) --*

      The name of the database for the table. Unique to a Data Catalog. A database is a set
      of associated table definitions organized into a logical group. You can Grant and
      Revoke database privileges to a principal.

    - **Name** *(string) --*

      The name of the table.
    """


_ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "_ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)


class ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsColumnWildcardTypeDef(
    _ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsColumnWildcardTypeDef
):
    """
    Type definition for `ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumns` `ColumnWildcard`

    A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames``
    or ``ColumnWildcard`` is required.

    - **ExcludedColumnNames** *(list) --*

      Excludes column names. Any column with this name will be excluded.

      - *(string) --*
    """


_ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsTypeDef = TypedDict(
    "_ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)


class ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsTypeDef(
    _ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsTypeDef
):
    """
    Type definition for `ClientGetEffectivePermissionsForPathResponsePermissionsResource` `TableWithColumns`

    The table with columns for the resource. A principal with permissions to this resource
    can select metadata from the columns of a table in the Data Catalog and the underlying
    data in Amazon S3.

    - **DatabaseName** *(string) --*

      The name of the database for the table with columns resource. Unique to the Data
      Catalog. A database is a set of associated table definitions organized into a logical
      group. You can Grant and Revoke database privileges to a principal.

    - **Name** *(string) --*

      The name of the table resource. A table is a metadata definition that represents your
      data. You can Grant and Revoke table privileges to a principal.

    - **ColumnNames** *(list) --*

      The list of column names for the table. At least one of ``ColumnNames`` or
      ``ColumnWildcard`` is required.

      - *(string) --*

    - **ColumnWildcard** *(dict) --*

      A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames``
      or ``ColumnWildcard`` is required.

      - **ExcludedColumnNames** *(list) --*

        Excludes column names. Any column with this name will be excluded.

        - *(string) --*
    """


_ClientGetEffectivePermissionsForPathResponsePermissionsResourceTypeDef = TypedDict(
    "_ClientGetEffectivePermissionsForPathResponsePermissionsResourceTypeDef",
    {
        "Catalog": Dict,
        "Database": ClientGetEffectivePermissionsForPathResponsePermissionsResourceDatabaseTypeDef,
        "Table": ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableTypeDef,
        "TableWithColumns": ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsTypeDef,
        "DataLocation": ClientGetEffectivePermissionsForPathResponsePermissionsResourceDataLocationTypeDef,
    },
    total=False,
)


class ClientGetEffectivePermissionsForPathResponsePermissionsResourceTypeDef(
    _ClientGetEffectivePermissionsForPathResponsePermissionsResourceTypeDef
):
    """
    Type definition for `ClientGetEffectivePermissionsForPathResponsePermissions` `Resource`

    The resource where permissions are to be granted or revoked.

    - **Catalog** *(dict) --*

      The identifier for the Data Catalog. By default, the account ID. The Data Catalog is
      the persistent metadata store. It contains database definitions, table definitions, and
      other control information to manage your AWS Lake Formation environment.

    - **Database** *(dict) --*

      The database for the resource. Unique to the Data Catalog. A database is a set of
      associated table definitions organized into a logical group. You can Grant and Revoke
      database permissions to a principal.

      - **Name** *(string) --*

        The name of the database resource. Unique to the Data Catalog.

    - **Table** *(dict) --*

      The table for the resource. A table is a metadata definition that represents your data.
      You can Grant and Revoke table privileges to a principal.

      - **DatabaseName** *(string) --*

        The name of the database for the table. Unique to a Data Catalog. A database is a set
        of associated table definitions organized into a logical group. You can Grant and
        Revoke database privileges to a principal.

      - **Name** *(string) --*

        The name of the table.

    - **TableWithColumns** *(dict) --*

      The table with columns for the resource. A principal with permissions to this resource
      can select metadata from the columns of a table in the Data Catalog and the underlying
      data in Amazon S3.

      - **DatabaseName** *(string) --*

        The name of the database for the table with columns resource. Unique to the Data
        Catalog. A database is a set of associated table definitions organized into a logical
        group. You can Grant and Revoke database privileges to a principal.

      - **Name** *(string) --*

        The name of the table resource. A table is a metadata definition that represents your
        data. You can Grant and Revoke table privileges to a principal.

      - **ColumnNames** *(list) --*

        The list of column names for the table. At least one of ``ColumnNames`` or
        ``ColumnWildcard`` is required.

        - *(string) --*

      - **ColumnWildcard** *(dict) --*

        A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames``
        or ``ColumnWildcard`` is required.

        - **ExcludedColumnNames** *(list) --*

          Excludes column names. Any column with this name will be excluded.

          - *(string) --*

    - **DataLocation** *(dict) --*

      The location of an Amazon S3 path where permissions are granted or revoked.

      - **ResourceArn** *(string) --*

        The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
    """


_ClientGetEffectivePermissionsForPathResponsePermissionsTypeDef = TypedDict(
    "_ClientGetEffectivePermissionsForPathResponsePermissionsTypeDef",
    {
        "Principal": ClientGetEffectivePermissionsForPathResponsePermissionsPrincipalTypeDef,
        "Resource": ClientGetEffectivePermissionsForPathResponsePermissionsResourceTypeDef,
        "Permissions": List[str],
        "PermissionsWithGrantOption": List[str],
    },
    total=False,
)


class ClientGetEffectivePermissionsForPathResponsePermissionsTypeDef(
    _ClientGetEffectivePermissionsForPathResponsePermissionsTypeDef
):
    """
    Type definition for `ClientGetEffectivePermissionsForPathResponse` `Permissions`

    The permissions granted or revoked on a resource.

    - **Principal** *(dict) --*

      The Data Lake principal to be granted or revoked permissions.

      - **DataLakePrincipalIdentifier** *(string) --*

        An identifier for the AWS Lake Formation principal.

    - **Resource** *(dict) --*

      The resource where permissions are to be granted or revoked.

      - **Catalog** *(dict) --*

        The identifier for the Data Catalog. By default, the account ID. The Data Catalog is
        the persistent metadata store. It contains database definitions, table definitions, and
        other control information to manage your AWS Lake Formation environment.

      - **Database** *(dict) --*

        The database for the resource. Unique to the Data Catalog. A database is a set of
        associated table definitions organized into a logical group. You can Grant and Revoke
        database permissions to a principal.

        - **Name** *(string) --*

          The name of the database resource. Unique to the Data Catalog.

      - **Table** *(dict) --*

        The table for the resource. A table is a metadata definition that represents your data.
        You can Grant and Revoke table privileges to a principal.

        - **DatabaseName** *(string) --*

          The name of the database for the table. Unique to a Data Catalog. A database is a set
          of associated table definitions organized into a logical group. You can Grant and
          Revoke database privileges to a principal.

        - **Name** *(string) --*

          The name of the table.

      - **TableWithColumns** *(dict) --*

        The table with columns for the resource. A principal with permissions to this resource
        can select metadata from the columns of a table in the Data Catalog and the underlying
        data in Amazon S3.

        - **DatabaseName** *(string) --*

          The name of the database for the table with columns resource. Unique to the Data
          Catalog. A database is a set of associated table definitions organized into a logical
          group. You can Grant and Revoke database privileges to a principal.

        - **Name** *(string) --*

          The name of the table resource. A table is a metadata definition that represents your
          data. You can Grant and Revoke table privileges to a principal.

        - **ColumnNames** *(list) --*

          The list of column names for the table. At least one of ``ColumnNames`` or
          ``ColumnWildcard`` is required.

          - *(string) --*

        - **ColumnWildcard** *(dict) --*

          A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames``
          or ``ColumnWildcard`` is required.

          - **ExcludedColumnNames** *(list) --*

            Excludes column names. Any column with this name will be excluded.

            - *(string) --*

      - **DataLocation** *(dict) --*

        The location of an Amazon S3 path where permissions are granted or revoked.

        - **ResourceArn** *(string) --*

          The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

    - **Permissions** *(list) --*

      The permissions to be granted or revoked on the resource.

      - *(string) --*

    - **PermissionsWithGrantOption** *(list) --*

      Indicates whether to grant the ability to grant permissions (as a subset of permissions
      granted).

      - *(string) --*
    """


_ClientGetEffectivePermissionsForPathResponseTypeDef = TypedDict(
    "_ClientGetEffectivePermissionsForPathResponseTypeDef",
    {
        "Permissions": List[
            ClientGetEffectivePermissionsForPathResponsePermissionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientGetEffectivePermissionsForPathResponseTypeDef(
    _ClientGetEffectivePermissionsForPathResponseTypeDef
):
    """
    Type definition for `ClientGetEffectivePermissionsForPath` `Response`

    - **Permissions** *(list) --*

      A list of the permissions for the specified table or database resource located at the path in
      Amazon S3.

      - *(dict) --*

        The permissions granted or revoked on a resource.

        - **Principal** *(dict) --*

          The Data Lake principal to be granted or revoked permissions.

          - **DataLakePrincipalIdentifier** *(string) --*

            An identifier for the AWS Lake Formation principal.

        - **Resource** *(dict) --*

          The resource where permissions are to be granted or revoked.

          - **Catalog** *(dict) --*

            The identifier for the Data Catalog. By default, the account ID. The Data Catalog is
            the persistent metadata store. It contains database definitions, table definitions, and
            other control information to manage your AWS Lake Formation environment.

          - **Database** *(dict) --*

            The database for the resource. Unique to the Data Catalog. A database is a set of
            associated table definitions organized into a logical group. You can Grant and Revoke
            database permissions to a principal.

            - **Name** *(string) --*

              The name of the database resource. Unique to the Data Catalog.

          - **Table** *(dict) --*

            The table for the resource. A table is a metadata definition that represents your data.
            You can Grant and Revoke table privileges to a principal.

            - **DatabaseName** *(string) --*

              The name of the database for the table. Unique to a Data Catalog. A database is a set
              of associated table definitions organized into a logical group. You can Grant and
              Revoke database privileges to a principal.

            - **Name** *(string) --*

              The name of the table.

          - **TableWithColumns** *(dict) --*

            The table with columns for the resource. A principal with permissions to this resource
            can select metadata from the columns of a table in the Data Catalog and the underlying
            data in Amazon S3.

            - **DatabaseName** *(string) --*

              The name of the database for the table with columns resource. Unique to the Data
              Catalog. A database is a set of associated table definitions organized into a logical
              group. You can Grant and Revoke database privileges to a principal.

            - **Name** *(string) --*

              The name of the table resource. A table is a metadata definition that represents your
              data. You can Grant and Revoke table privileges to a principal.

            - **ColumnNames** *(list) --*

              The list of column names for the table. At least one of ``ColumnNames`` or
              ``ColumnWildcard`` is required.

              - *(string) --*

            - **ColumnWildcard** *(dict) --*

              A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames``
              or ``ColumnWildcard`` is required.

              - **ExcludedColumnNames** *(list) --*

                Excludes column names. Any column with this name will be excluded.

                - *(string) --*

          - **DataLocation** *(dict) --*

            The location of an Amazon S3 path where permissions are granted or revoked.

            - **ResourceArn** *(string) --*

              The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

        - **Permissions** *(list) --*

          The permissions to be granted or revoked on the resource.

          - *(string) --*

        - **PermissionsWithGrantOption** *(list) --*

          Indicates whether to grant the ability to grant permissions (as a subset of permissions
          granted).

          - *(string) --*

    - **NextToken** *(string) --*

      A continuation token, if this is not the first call to retrieve this list.
    """


_ClientGrantPermissionsPrincipalTypeDef = TypedDict(
    "_ClientGrantPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientGrantPermissionsPrincipalTypeDef(_ClientGrantPermissionsPrincipalTypeDef):
    """
    Type definition for `ClientGrantPermissions` `Principal`

    The principal to be granted the permissions on the resource. Supported principals are IAM users
    or IAM roles, and they are defined by their principal type and their ARN.

    Note that if you define a resource with a particular ARN, then later delete, and recreate a
    resource with that same ARN, the resource maintains the permissions already granted.

    - **DataLakePrincipalIdentifier** *(string) --*

      An identifier for the AWS Lake Formation principal.
    """


_ClientGrantPermissionsResourceDataLocationTypeDef = TypedDict(
    "_ClientGrantPermissionsResourceDataLocationTypeDef", {"ResourceArn": str}
)


class ClientGrantPermissionsResourceDataLocationTypeDef(
    _ClientGrantPermissionsResourceDataLocationTypeDef
):
    """
    Type definition for `ClientGrantPermissionsResource` `DataLocation`

    The location of an Amazon S3 path where permissions are granted or revoked.

    - **ResourceArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
    """


_ClientGrantPermissionsResourceDatabaseTypeDef = TypedDict(
    "_ClientGrantPermissionsResourceDatabaseTypeDef", {"Name": str}
)


class ClientGrantPermissionsResourceDatabaseTypeDef(
    _ClientGrantPermissionsResourceDatabaseTypeDef
):
    """
    Type definition for `ClientGrantPermissionsResource` `Database`

    The database for the resource. Unique to the Data Catalog. A database is a set of associated
    table definitions organized into a logical group. You can Grant and Revoke database permissions
    to a principal.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the database resource. Unique to the Data Catalog.
    """


_ClientGrantPermissionsResourceTableTypeDef = TypedDict(
    "_ClientGrantPermissionsResourceTableTypeDef", {"DatabaseName": str, "Name": str}
)


class ClientGrantPermissionsResourceTableTypeDef(
    _ClientGrantPermissionsResourceTableTypeDef
):
    """
    Type definition for `ClientGrantPermissionsResource` `Table`

    The table for the resource. A table is a metadata definition that represents your data. You can
    Grant and Revoke table privileges to a principal.

    - **DatabaseName** *(string) --* **[REQUIRED]**

      The name of the database for the table. Unique to a Data Catalog. A database is a set of
      associated table definitions organized into a logical group. You can Grant and Revoke
      database privileges to a principal.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the table.
    """


_ClientGrantPermissionsResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "_ClientGrantPermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)


class ClientGrantPermissionsResourceTableWithColumnsColumnWildcardTypeDef(
    _ClientGrantPermissionsResourceTableWithColumnsColumnWildcardTypeDef
):
    """
    Type definition for `ClientGrantPermissionsResourceTableWithColumns` `ColumnWildcard`

    A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
    ``ColumnWildcard`` is required.

    - **ExcludedColumnNames** *(list) --*

      Excludes column names. Any column with this name will be excluded.

      - *(string) --*
    """


_ClientGrantPermissionsResourceTableWithColumnsTypeDef = TypedDict(
    "_ClientGrantPermissionsResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientGrantPermissionsResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)


class ClientGrantPermissionsResourceTableWithColumnsTypeDef(
    _ClientGrantPermissionsResourceTableWithColumnsTypeDef
):
    """
    Type definition for `ClientGrantPermissionsResource` `TableWithColumns`

    The table with columns for the resource. A principal with permissions to this resource can
    select metadata from the columns of a table in the Data Catalog and the underlying data in
    Amazon S3.

    - **DatabaseName** *(string) --*

      The name of the database for the table with columns resource. Unique to the Data Catalog. A
      database is a set of associated table definitions organized into a logical group. You can
      Grant and Revoke database privileges to a principal.

    - **Name** *(string) --*

      The name of the table resource. A table is a metadata definition that represents your data.
      You can Grant and Revoke table privileges to a principal.

    - **ColumnNames** *(list) --*

      The list of column names for the table. At least one of ``ColumnNames`` or ``ColumnWildcard``
      is required.

      - *(string) --*

    - **ColumnWildcard** *(dict) --*

      A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
      ``ColumnWildcard`` is required.

      - **ExcludedColumnNames** *(list) --*

        Excludes column names. Any column with this name will be excluded.

        - *(string) --*
    """


_ClientGrantPermissionsResourceTypeDef = TypedDict(
    "_ClientGrantPermissionsResourceTypeDef",
    {
        "Catalog": Dict,
        "Database": ClientGrantPermissionsResourceDatabaseTypeDef,
        "Table": ClientGrantPermissionsResourceTableTypeDef,
        "TableWithColumns": ClientGrantPermissionsResourceTableWithColumnsTypeDef,
        "DataLocation": ClientGrantPermissionsResourceDataLocationTypeDef,
    },
    total=False,
)


class ClientGrantPermissionsResourceTypeDef(_ClientGrantPermissionsResourceTypeDef):
    """
    Type definition for `ClientGrantPermissions` `Resource`

    The resource to which permissions are to be granted. Resources in AWS Lake Formation are the Data
    Catalog, databases, and tables.

    - **Catalog** *(dict) --*

      The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
      persistent metadata store. It contains database definitions, table definitions, and other
      control information to manage your AWS Lake Formation environment.

    - **Database** *(dict) --*

      The database for the resource. Unique to the Data Catalog. A database is a set of associated
      table definitions organized into a logical group. You can Grant and Revoke database permissions
      to a principal.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the database resource. Unique to the Data Catalog.

    - **Table** *(dict) --*

      The table for the resource. A table is a metadata definition that represents your data. You can
      Grant and Revoke table privileges to a principal.

      - **DatabaseName** *(string) --* **[REQUIRED]**

        The name of the database for the table. Unique to a Data Catalog. A database is a set of
        associated table definitions organized into a logical group. You can Grant and Revoke
        database privileges to a principal.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the table.

    - **TableWithColumns** *(dict) --*

      The table with columns for the resource. A principal with permissions to this resource can
      select metadata from the columns of a table in the Data Catalog and the underlying data in
      Amazon S3.

      - **DatabaseName** *(string) --*

        The name of the database for the table with columns resource. Unique to the Data Catalog. A
        database is a set of associated table definitions organized into a logical group. You can
        Grant and Revoke database privileges to a principal.

      - **Name** *(string) --*

        The name of the table resource. A table is a metadata definition that represents your data.
        You can Grant and Revoke table privileges to a principal.

      - **ColumnNames** *(list) --*

        The list of column names for the table. At least one of ``ColumnNames`` or ``ColumnWildcard``
        is required.

        - *(string) --*

      - **ColumnWildcard** *(dict) --*

        A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
        ``ColumnWildcard`` is required.

        - **ExcludedColumnNames** *(list) --*

          Excludes column names. Any column with this name will be excluded.

          - *(string) --*

    - **DataLocation** *(dict) --*

      The location of an Amazon S3 path where permissions are granted or revoked.

      - **ResourceArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
    """


_ClientListPermissionsPrincipalTypeDef = TypedDict(
    "_ClientListPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientListPermissionsPrincipalTypeDef(_ClientListPermissionsPrincipalTypeDef):
    """
    Type definition for `ClientListPermissions` `Principal`

    Specifies a principal to filter the permissions returned.

    - **DataLakePrincipalIdentifier** *(string) --*

      An identifier for the AWS Lake Formation principal.
    """


_ClientListPermissionsResourceDataLocationTypeDef = TypedDict(
    "_ClientListPermissionsResourceDataLocationTypeDef", {"ResourceArn": str}
)


class ClientListPermissionsResourceDataLocationTypeDef(
    _ClientListPermissionsResourceDataLocationTypeDef
):
    """
    Type definition for `ClientListPermissionsResource` `DataLocation`

    The location of an Amazon S3 path where permissions are granted or revoked.

    - **ResourceArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
    """


_ClientListPermissionsResourceDatabaseTypeDef = TypedDict(
    "_ClientListPermissionsResourceDatabaseTypeDef", {"Name": str}
)


class ClientListPermissionsResourceDatabaseTypeDef(
    _ClientListPermissionsResourceDatabaseTypeDef
):
    """
    Type definition for `ClientListPermissionsResource` `Database`

    The database for the resource. Unique to the Data Catalog. A database is a set of associated
    table definitions organized into a logical group. You can Grant and Revoke database permissions
    to a principal.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the database resource. Unique to the Data Catalog.
    """


_ClientListPermissionsResourceTableTypeDef = TypedDict(
    "_ClientListPermissionsResourceTableTypeDef", {"DatabaseName": str, "Name": str}
)


class ClientListPermissionsResourceTableTypeDef(
    _ClientListPermissionsResourceTableTypeDef
):
    """
    Type definition for `ClientListPermissionsResource` `Table`

    The table for the resource. A table is a metadata definition that represents your data. You can
    Grant and Revoke table privileges to a principal.

    - **DatabaseName** *(string) --* **[REQUIRED]**

      The name of the database for the table. Unique to a Data Catalog. A database is a set of
      associated table definitions organized into a logical group. You can Grant and Revoke
      database privileges to a principal.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the table.
    """


_ClientListPermissionsResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "_ClientListPermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)


class ClientListPermissionsResourceTableWithColumnsColumnWildcardTypeDef(
    _ClientListPermissionsResourceTableWithColumnsColumnWildcardTypeDef
):
    """
    Type definition for `ClientListPermissionsResourceTableWithColumns` `ColumnWildcard`

    A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
    ``ColumnWildcard`` is required.

    - **ExcludedColumnNames** *(list) --*

      Excludes column names. Any column with this name will be excluded.

      - *(string) --*
    """


_ClientListPermissionsResourceTableWithColumnsTypeDef = TypedDict(
    "_ClientListPermissionsResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientListPermissionsResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)


class ClientListPermissionsResourceTableWithColumnsTypeDef(
    _ClientListPermissionsResourceTableWithColumnsTypeDef
):
    """
    Type definition for `ClientListPermissionsResource` `TableWithColumns`

    The table with columns for the resource. A principal with permissions to this resource can
    select metadata from the columns of a table in the Data Catalog and the underlying data in
    Amazon S3.

    - **DatabaseName** *(string) --*

      The name of the database for the table with columns resource. Unique to the Data Catalog. A
      database is a set of associated table definitions organized into a logical group. You can
      Grant and Revoke database privileges to a principal.

    - **Name** *(string) --*

      The name of the table resource. A table is a metadata definition that represents your data.
      You can Grant and Revoke table privileges to a principal.

    - **ColumnNames** *(list) --*

      The list of column names for the table. At least one of ``ColumnNames`` or ``ColumnWildcard``
      is required.

      - *(string) --*

    - **ColumnWildcard** *(dict) --*

      A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
      ``ColumnWildcard`` is required.

      - **ExcludedColumnNames** *(list) --*

        Excludes column names. Any column with this name will be excluded.

        - *(string) --*
    """


_ClientListPermissionsResourceTypeDef = TypedDict(
    "_ClientListPermissionsResourceTypeDef",
    {
        "Catalog": Dict,
        "Database": ClientListPermissionsResourceDatabaseTypeDef,
        "Table": ClientListPermissionsResourceTableTypeDef,
        "TableWithColumns": ClientListPermissionsResourceTableWithColumnsTypeDef,
        "DataLocation": ClientListPermissionsResourceDataLocationTypeDef,
    },
    total=False,
)


class ClientListPermissionsResourceTypeDef(_ClientListPermissionsResourceTypeDef):
    """
    Type definition for `ClientListPermissions` `Resource`

    A resource where you will get a list of the principal permissions.

    This operation does not support getting privileges on a table with columns. Instead, call this
    operation on the table, and the operation returns the table and the table w columns.

    - **Catalog** *(dict) --*

      The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
      persistent metadata store. It contains database definitions, table definitions, and other
      control information to manage your AWS Lake Formation environment.

    - **Database** *(dict) --*

      The database for the resource. Unique to the Data Catalog. A database is a set of associated
      table definitions organized into a logical group. You can Grant and Revoke database permissions
      to a principal.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the database resource. Unique to the Data Catalog.

    - **Table** *(dict) --*

      The table for the resource. A table is a metadata definition that represents your data. You can
      Grant and Revoke table privileges to a principal.

      - **DatabaseName** *(string) --* **[REQUIRED]**

        The name of the database for the table. Unique to a Data Catalog. A database is a set of
        associated table definitions organized into a logical group. You can Grant and Revoke
        database privileges to a principal.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the table.

    - **TableWithColumns** *(dict) --*

      The table with columns for the resource. A principal with permissions to this resource can
      select metadata from the columns of a table in the Data Catalog and the underlying data in
      Amazon S3.

      - **DatabaseName** *(string) --*

        The name of the database for the table with columns resource. Unique to the Data Catalog. A
        database is a set of associated table definitions organized into a logical group. You can
        Grant and Revoke database privileges to a principal.

      - **Name** *(string) --*

        The name of the table resource. A table is a metadata definition that represents your data.
        You can Grant and Revoke table privileges to a principal.

      - **ColumnNames** *(list) --*

        The list of column names for the table. At least one of ``ColumnNames`` or ``ColumnWildcard``
        is required.

        - *(string) --*

      - **ColumnWildcard** *(dict) --*

        A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
        ``ColumnWildcard`` is required.

        - **ExcludedColumnNames** *(list) --*

          Excludes column names. Any column with this name will be excluded.

          - *(string) --*

    - **DataLocation** *(dict) --*

      The location of an Amazon S3 path where permissions are granted or revoked.

      - **ResourceArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
    """


_ClientListPermissionsResponsePrincipalResourcePermissionsPrincipalTypeDef = TypedDict(
    "_ClientListPermissionsResponsePrincipalResourcePermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientListPermissionsResponsePrincipalResourcePermissionsPrincipalTypeDef(
    _ClientListPermissionsResponsePrincipalResourcePermissionsPrincipalTypeDef
):
    """
    Type definition for `ClientListPermissionsResponsePrincipalResourcePermissions` `Principal`

    The Data Lake principal to be granted or revoked permissions.

    - **DataLakePrincipalIdentifier** *(string) --*

      An identifier for the AWS Lake Formation principal.
    """


_ClientListPermissionsResponsePrincipalResourcePermissionsResourceDataLocationTypeDef = TypedDict(
    "_ClientListPermissionsResponsePrincipalResourcePermissionsResourceDataLocationTypeDef",
    {"ResourceArn": str},
    total=False,
)


class ClientListPermissionsResponsePrincipalResourcePermissionsResourceDataLocationTypeDef(
    _ClientListPermissionsResponsePrincipalResourcePermissionsResourceDataLocationTypeDef
):
    """
    Type definition for `ClientListPermissionsResponsePrincipalResourcePermissionsResource` `DataLocation`

    The location of an Amazon S3 path where permissions are granted or revoked.

    - **ResourceArn** *(string) --*

      The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
    """


_ClientListPermissionsResponsePrincipalResourcePermissionsResourceDatabaseTypeDef = TypedDict(
    "_ClientListPermissionsResponsePrincipalResourcePermissionsResourceDatabaseTypeDef",
    {"Name": str},
    total=False,
)


class ClientListPermissionsResponsePrincipalResourcePermissionsResourceDatabaseTypeDef(
    _ClientListPermissionsResponsePrincipalResourcePermissionsResourceDatabaseTypeDef
):
    """
    Type definition for `ClientListPermissionsResponsePrincipalResourcePermissionsResource` `Database`

    The database for the resource. Unique to the Data Catalog. A database is a set of
    associated table definitions organized into a logical group. You can Grant and Revoke
    database permissions to a principal.

    - **Name** *(string) --*

      The name of the database resource. Unique to the Data Catalog.
    """


_ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableTypeDef = TypedDict(
    "_ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableTypeDef",
    {"DatabaseName": str, "Name": str},
    total=False,
)


class ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableTypeDef(
    _ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableTypeDef
):
    """
    Type definition for `ClientListPermissionsResponsePrincipalResourcePermissionsResource` `Table`

    The table for the resource. A table is a metadata definition that represents your data.
    You can Grant and Revoke table privileges to a principal.

    - **DatabaseName** *(string) --*

      The name of the database for the table. Unique to a Data Catalog. A database is a set
      of associated table definitions organized into a logical group. You can Grant and
      Revoke database privileges to a principal.

    - **Name** *(string) --*

      The name of the table.
    """


_ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "_ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)


class ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsColumnWildcardTypeDef(
    _ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsColumnWildcardTypeDef
):
    """
    Type definition for `ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumns` `ColumnWildcard`

    A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames``
    or ``ColumnWildcard`` is required.

    - **ExcludedColumnNames** *(list) --*

      Excludes column names. Any column with this name will be excluded.

      - *(string) --*
    """


_ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsTypeDef = TypedDict(
    "_ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)


class ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsTypeDef(
    _ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsTypeDef
):
    """
    Type definition for `ClientListPermissionsResponsePrincipalResourcePermissionsResource` `TableWithColumns`

    The table with columns for the resource. A principal with permissions to this resource
    can select metadata from the columns of a table in the Data Catalog and the underlying
    data in Amazon S3.

    - **DatabaseName** *(string) --*

      The name of the database for the table with columns resource. Unique to the Data
      Catalog. A database is a set of associated table definitions organized into a logical
      group. You can Grant and Revoke database privileges to a principal.

    - **Name** *(string) --*

      The name of the table resource. A table is a metadata definition that represents your
      data. You can Grant and Revoke table privileges to a principal.

    - **ColumnNames** *(list) --*

      The list of column names for the table. At least one of ``ColumnNames`` or
      ``ColumnWildcard`` is required.

      - *(string) --*

    - **ColumnWildcard** *(dict) --*

      A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames``
      or ``ColumnWildcard`` is required.

      - **ExcludedColumnNames** *(list) --*

        Excludes column names. Any column with this name will be excluded.

        - *(string) --*
    """


_ClientListPermissionsResponsePrincipalResourcePermissionsResourceTypeDef = TypedDict(
    "_ClientListPermissionsResponsePrincipalResourcePermissionsResourceTypeDef",
    {
        "Catalog": Dict,
        "Database": ClientListPermissionsResponsePrincipalResourcePermissionsResourceDatabaseTypeDef,
        "Table": ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableTypeDef,
        "TableWithColumns": ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsTypeDef,
        "DataLocation": ClientListPermissionsResponsePrincipalResourcePermissionsResourceDataLocationTypeDef,
    },
    total=False,
)


class ClientListPermissionsResponsePrincipalResourcePermissionsResourceTypeDef(
    _ClientListPermissionsResponsePrincipalResourcePermissionsResourceTypeDef
):
    """
    Type definition for `ClientListPermissionsResponsePrincipalResourcePermissions` `Resource`

    The resource where permissions are to be granted or revoked.

    - **Catalog** *(dict) --*

      The identifier for the Data Catalog. By default, the account ID. The Data Catalog is
      the persistent metadata store. It contains database definitions, table definitions, and
      other control information to manage your AWS Lake Formation environment.

    - **Database** *(dict) --*

      The database for the resource. Unique to the Data Catalog. A database is a set of
      associated table definitions organized into a logical group. You can Grant and Revoke
      database permissions to a principal.

      - **Name** *(string) --*

        The name of the database resource. Unique to the Data Catalog.

    - **Table** *(dict) --*

      The table for the resource. A table is a metadata definition that represents your data.
      You can Grant and Revoke table privileges to a principal.

      - **DatabaseName** *(string) --*

        The name of the database for the table. Unique to a Data Catalog. A database is a set
        of associated table definitions organized into a logical group. You can Grant and
        Revoke database privileges to a principal.

      - **Name** *(string) --*

        The name of the table.

    - **TableWithColumns** *(dict) --*

      The table with columns for the resource. A principal with permissions to this resource
      can select metadata from the columns of a table in the Data Catalog and the underlying
      data in Amazon S3.

      - **DatabaseName** *(string) --*

        The name of the database for the table with columns resource. Unique to the Data
        Catalog. A database is a set of associated table definitions organized into a logical
        group. You can Grant and Revoke database privileges to a principal.

      - **Name** *(string) --*

        The name of the table resource. A table is a metadata definition that represents your
        data. You can Grant and Revoke table privileges to a principal.

      - **ColumnNames** *(list) --*

        The list of column names for the table. At least one of ``ColumnNames`` or
        ``ColumnWildcard`` is required.

        - *(string) --*

      - **ColumnWildcard** *(dict) --*

        A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames``
        or ``ColumnWildcard`` is required.

        - **ExcludedColumnNames** *(list) --*

          Excludes column names. Any column with this name will be excluded.

          - *(string) --*

    - **DataLocation** *(dict) --*

      The location of an Amazon S3 path where permissions are granted or revoked.

      - **ResourceArn** *(string) --*

        The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
    """


_ClientListPermissionsResponsePrincipalResourcePermissionsTypeDef = TypedDict(
    "_ClientListPermissionsResponsePrincipalResourcePermissionsTypeDef",
    {
        "Principal": ClientListPermissionsResponsePrincipalResourcePermissionsPrincipalTypeDef,
        "Resource": ClientListPermissionsResponsePrincipalResourcePermissionsResourceTypeDef,
        "Permissions": List[str],
        "PermissionsWithGrantOption": List[str],
    },
    total=False,
)


class ClientListPermissionsResponsePrincipalResourcePermissionsTypeDef(
    _ClientListPermissionsResponsePrincipalResourcePermissionsTypeDef
):
    """
    Type definition for `ClientListPermissionsResponse` `PrincipalResourcePermissions`

    The permissions granted or revoked on a resource.

    - **Principal** *(dict) --*

      The Data Lake principal to be granted or revoked permissions.

      - **DataLakePrincipalIdentifier** *(string) --*

        An identifier for the AWS Lake Formation principal.

    - **Resource** *(dict) --*

      The resource where permissions are to be granted or revoked.

      - **Catalog** *(dict) --*

        The identifier for the Data Catalog. By default, the account ID. The Data Catalog is
        the persistent metadata store. It contains database definitions, table definitions, and
        other control information to manage your AWS Lake Formation environment.

      - **Database** *(dict) --*

        The database for the resource. Unique to the Data Catalog. A database is a set of
        associated table definitions organized into a logical group. You can Grant and Revoke
        database permissions to a principal.

        - **Name** *(string) --*

          The name of the database resource. Unique to the Data Catalog.

      - **Table** *(dict) --*

        The table for the resource. A table is a metadata definition that represents your data.
        You can Grant and Revoke table privileges to a principal.

        - **DatabaseName** *(string) --*

          The name of the database for the table. Unique to a Data Catalog. A database is a set
          of associated table definitions organized into a logical group. You can Grant and
          Revoke database privileges to a principal.

        - **Name** *(string) --*

          The name of the table.

      - **TableWithColumns** *(dict) --*

        The table with columns for the resource. A principal with permissions to this resource
        can select metadata from the columns of a table in the Data Catalog and the underlying
        data in Amazon S3.

        - **DatabaseName** *(string) --*

          The name of the database for the table with columns resource. Unique to the Data
          Catalog. A database is a set of associated table definitions organized into a logical
          group. You can Grant and Revoke database privileges to a principal.

        - **Name** *(string) --*

          The name of the table resource. A table is a metadata definition that represents your
          data. You can Grant and Revoke table privileges to a principal.

        - **ColumnNames** *(list) --*

          The list of column names for the table. At least one of ``ColumnNames`` or
          ``ColumnWildcard`` is required.

          - *(string) --*

        - **ColumnWildcard** *(dict) --*

          A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames``
          or ``ColumnWildcard`` is required.

          - **ExcludedColumnNames** *(list) --*

            Excludes column names. Any column with this name will be excluded.

            - *(string) --*

      - **DataLocation** *(dict) --*

        The location of an Amazon S3 path where permissions are granted or revoked.

        - **ResourceArn** *(string) --*

          The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

    - **Permissions** *(list) --*

      The permissions to be granted or revoked on the resource.

      - *(string) --*

    - **PermissionsWithGrantOption** *(list) --*

      Indicates whether to grant the ability to grant permissions (as a subset of permissions
      granted).

      - *(string) --*
    """


_ClientListPermissionsResponseTypeDef = TypedDict(
    "_ClientListPermissionsResponseTypeDef",
    {
        "PrincipalResourcePermissions": List[
            ClientListPermissionsResponsePrincipalResourcePermissionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListPermissionsResponseTypeDef(_ClientListPermissionsResponseTypeDef):
    """
    Type definition for `ClientListPermissions` `Response`

    - **PrincipalResourcePermissions** *(list) --*

      A list of principals and their permissions on the resource for the specified principal and
      resource types.

      - *(dict) --*

        The permissions granted or revoked on a resource.

        - **Principal** *(dict) --*

          The Data Lake principal to be granted or revoked permissions.

          - **DataLakePrincipalIdentifier** *(string) --*

            An identifier for the AWS Lake Formation principal.

        - **Resource** *(dict) --*

          The resource where permissions are to be granted or revoked.

          - **Catalog** *(dict) --*

            The identifier for the Data Catalog. By default, the account ID. The Data Catalog is
            the persistent metadata store. It contains database definitions, table definitions, and
            other control information to manage your AWS Lake Formation environment.

          - **Database** *(dict) --*

            The database for the resource. Unique to the Data Catalog. A database is a set of
            associated table definitions organized into a logical group. You can Grant and Revoke
            database permissions to a principal.

            - **Name** *(string) --*

              The name of the database resource. Unique to the Data Catalog.

          - **Table** *(dict) --*

            The table for the resource. A table is a metadata definition that represents your data.
            You can Grant and Revoke table privileges to a principal.

            - **DatabaseName** *(string) --*

              The name of the database for the table. Unique to a Data Catalog. A database is a set
              of associated table definitions organized into a logical group. You can Grant and
              Revoke database privileges to a principal.

            - **Name** *(string) --*

              The name of the table.

          - **TableWithColumns** *(dict) --*

            The table with columns for the resource. A principal with permissions to this resource
            can select metadata from the columns of a table in the Data Catalog and the underlying
            data in Amazon S3.

            - **DatabaseName** *(string) --*

              The name of the database for the table with columns resource. Unique to the Data
              Catalog. A database is a set of associated table definitions organized into a logical
              group. You can Grant and Revoke database privileges to a principal.

            - **Name** *(string) --*

              The name of the table resource. A table is a metadata definition that represents your
              data. You can Grant and Revoke table privileges to a principal.

            - **ColumnNames** *(list) --*

              The list of column names for the table. At least one of ``ColumnNames`` or
              ``ColumnWildcard`` is required.

              - *(string) --*

            - **ColumnWildcard** *(dict) --*

              A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames``
              or ``ColumnWildcard`` is required.

              - **ExcludedColumnNames** *(list) --*

                Excludes column names. Any column with this name will be excluded.

                - *(string) --*

          - **DataLocation** *(dict) --*

            The location of an Amazon S3 path where permissions are granted or revoked.

            - **ResourceArn** *(string) --*

              The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

        - **Permissions** *(list) --*

          The permissions to be granted or revoked on the resource.

          - *(string) --*

        - **PermissionsWithGrantOption** *(list) --*

          Indicates whether to grant the ability to grant permissions (as a subset of permissions
          granted).

          - *(string) --*

    - **NextToken** *(string) --*

      A continuation token, if this is not the first call to retrieve this list.
    """


_ClientListResourcesFilterConditionListTypeDef = TypedDict(
    "_ClientListResourcesFilterConditionListTypeDef",
    {"Field": str, "ComparisonOperator": str, "StringValueList": List[str]},
    total=False,
)


class ClientListResourcesFilterConditionListTypeDef(
    _ClientListResourcesFilterConditionListTypeDef
):
    """
    Type definition for `ClientListResources` `FilterConditionList`

    This structure describes the filtering of columns in a table based on a filter condition.

    - **Field** *(string) --*

      The field to filter in the filter condition.

    - **ComparisonOperator** *(string) --*

      The comparison operator used in the filter condition.

    - **StringValueList** *(list) --*

      A string with values used in evaluating the filter condition.

      - *(string) --*
    """


_ClientListResourcesResponseResourceInfoListTypeDef = TypedDict(
    "_ClientListResourcesResponseResourceInfoListTypeDef",
    {"ResourceArn": str, "RoleArn": str, "LastModified": datetime},
    total=False,
)


class ClientListResourcesResponseResourceInfoListTypeDef(
    _ClientListResourcesResponseResourceInfoListTypeDef
):
    """
    Type definition for `ClientListResourcesResponse` `ResourceInfoList`

    A structure containing information about an AWS Lake Formation resource.

    - **ResourceArn** *(string) --*

      The Amazon Resource Name (ARN) of the resource.

    - **RoleArn** *(string) --*

      The IAM role that registered a resource.

    - **LastModified** *(datetime) --*

      The date and time the resource was last modified.
    """


_ClientListResourcesResponseTypeDef = TypedDict(
    "_ClientListResourcesResponseTypeDef",
    {
        "ResourceInfoList": List[ClientListResourcesResponseResourceInfoListTypeDef],
        "NextToken": str,
    },
    total=False,
)


class ClientListResourcesResponseTypeDef(_ClientListResourcesResponseTypeDef):
    """
    Type definition for `ClientListResources` `Response`

    - **ResourceInfoList** *(list) --*

      A summary of the data lake resources.

      - *(dict) --*

        A structure containing information about an AWS Lake Formation resource.

        - **ResourceArn** *(string) --*

          The Amazon Resource Name (ARN) of the resource.

        - **RoleArn** *(string) --*

          The IAM role that registered a resource.

        - **LastModified** *(datetime) --*

          The date and time the resource was last modified.

    - **NextToken** *(string) --*

      A continuation token, if this is not the first call to retrieve these resources.
    """


_ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef = TypedDict(
    "_ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef(
    _ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef
):
    """
    Type definition for `ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissions` `Principal`

    The principal who is granted permissions.

    - **DataLakePrincipalIdentifier** *(string) --*

      An identifier for the AWS Lake Formation principal.
    """


_ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef = TypedDict(
    "_ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef",
    {
        "Principal": ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[str],
    },
    total=False,
)


class ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef(
    _ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef
):
    """
    Type definition for `ClientPutDataLakeSettingsDataLakeSettings` `CreateDatabaseDefaultPermissions`

    Permissions granted to a principal.

    - **Principal** *(dict) --*

      The principal who is granted permissions.

      - **DataLakePrincipalIdentifier** *(string) --*

        An identifier for the AWS Lake Formation principal.

    - **Permissions** *(list) --*

      The permissions that are granted to the principal.

      - *(string) --*
    """


_ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef = TypedDict(
    "_ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef(
    _ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef
):
    """
    Type definition for `ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissions` `Principal`

    The principal who is granted permissions.

    - **DataLakePrincipalIdentifier** *(string) --*

      An identifier for the AWS Lake Formation principal.
    """


_ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsTypeDef = TypedDict(
    "_ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsTypeDef",
    {
        "Principal": ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[str],
    },
    total=False,
)


class ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsTypeDef(
    _ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsTypeDef
):
    """
    Type definition for `ClientPutDataLakeSettingsDataLakeSettings` `CreateTableDefaultPermissions`

    Permissions granted to a principal.

    - **Principal** *(dict) --*

      The principal who is granted permissions.

      - **DataLakePrincipalIdentifier** *(string) --*

        An identifier for the AWS Lake Formation principal.

    - **Permissions** *(list) --*

      The permissions that are granted to the principal.

      - *(string) --*
    """


_ClientPutDataLakeSettingsDataLakeSettingsDataLakeAdminsTypeDef = TypedDict(
    "_ClientPutDataLakeSettingsDataLakeSettingsDataLakeAdminsTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientPutDataLakeSettingsDataLakeSettingsDataLakeAdminsTypeDef(
    _ClientPutDataLakeSettingsDataLakeSettingsDataLakeAdminsTypeDef
):
    """
    Type definition for `ClientPutDataLakeSettingsDataLakeSettings` `DataLakeAdmins`

    The AWS Lake Formation principal.

    - **DataLakePrincipalIdentifier** *(string) --*

      An identifier for the AWS Lake Formation principal.
    """


_ClientPutDataLakeSettingsDataLakeSettingsTypeDef = TypedDict(
    "_ClientPutDataLakeSettingsDataLakeSettingsTypeDef",
    {
        "DataLakeAdmins": List[
            ClientPutDataLakeSettingsDataLakeSettingsDataLakeAdminsTypeDef
        ],
        "CreateDatabaseDefaultPermissions": List[
            ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef
        ],
        "CreateTableDefaultPermissions": List[
            ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsTypeDef
        ],
    },
    total=False,
)


class ClientPutDataLakeSettingsDataLakeSettingsTypeDef(
    _ClientPutDataLakeSettingsDataLakeSettingsTypeDef
):
    """
    Type definition for `ClientPutDataLakeSettings` `DataLakeSettings`

    A list of AWS Lake Formation principals.

    - **DataLakeAdmins** *(list) --*

      A list of AWS Lake Formation principals.

      - *(dict) --*

        The AWS Lake Formation principal.

        - **DataLakePrincipalIdentifier** *(string) --*

          An identifier for the AWS Lake Formation principal.

    - **CreateDatabaseDefaultPermissions** *(list) --*

      A list of up to three principal permissions entries for default create database permissions.

      - *(dict) --*

        Permissions granted to a principal.

        - **Principal** *(dict) --*

          The principal who is granted permissions.

          - **DataLakePrincipalIdentifier** *(string) --*

            An identifier for the AWS Lake Formation principal.

        - **Permissions** *(list) --*

          The permissions that are granted to the principal.

          - *(string) --*

    - **CreateTableDefaultPermissions** *(list) --*

      A list of up to three principal permissions entries for default create table permissions.

      - *(dict) --*

        Permissions granted to a principal.

        - **Principal** *(dict) --*

          The principal who is granted permissions.

          - **DataLakePrincipalIdentifier** *(string) --*

            An identifier for the AWS Lake Formation principal.

        - **Permissions** *(list) --*

          The permissions that are granted to the principal.

          - *(string) --*
    """


_ClientRevokePermissionsPrincipalTypeDef = TypedDict(
    "_ClientRevokePermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)


class ClientRevokePermissionsPrincipalTypeDef(_ClientRevokePermissionsPrincipalTypeDef):
    """
    Type definition for `ClientRevokePermissions` `Principal`

    The principal to be revoked permissions on the resource.

    - **DataLakePrincipalIdentifier** *(string) --*

      An identifier for the AWS Lake Formation principal.
    """


_ClientRevokePermissionsResourceDataLocationTypeDef = TypedDict(
    "_ClientRevokePermissionsResourceDataLocationTypeDef", {"ResourceArn": str}
)


class ClientRevokePermissionsResourceDataLocationTypeDef(
    _ClientRevokePermissionsResourceDataLocationTypeDef
):
    """
    Type definition for `ClientRevokePermissionsResource` `DataLocation`

    The location of an Amazon S3 path where permissions are granted or revoked.

    - **ResourceArn** *(string) --* **[REQUIRED]**

      The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
    """


_ClientRevokePermissionsResourceDatabaseTypeDef = TypedDict(
    "_ClientRevokePermissionsResourceDatabaseTypeDef", {"Name": str}
)


class ClientRevokePermissionsResourceDatabaseTypeDef(
    _ClientRevokePermissionsResourceDatabaseTypeDef
):
    """
    Type definition for `ClientRevokePermissionsResource` `Database`

    The database for the resource. Unique to the Data Catalog. A database is a set of associated
    table definitions organized into a logical group. You can Grant and Revoke database permissions
    to a principal.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the database resource. Unique to the Data Catalog.
    """


_ClientRevokePermissionsResourceTableTypeDef = TypedDict(
    "_ClientRevokePermissionsResourceTableTypeDef", {"DatabaseName": str, "Name": str}
)


class ClientRevokePermissionsResourceTableTypeDef(
    _ClientRevokePermissionsResourceTableTypeDef
):
    """
    Type definition for `ClientRevokePermissionsResource` `Table`

    The table for the resource. A table is a metadata definition that represents your data. You can
    Grant and Revoke table privileges to a principal.

    - **DatabaseName** *(string) --* **[REQUIRED]**

      The name of the database for the table. Unique to a Data Catalog. A database is a set of
      associated table definitions organized into a logical group. You can Grant and Revoke
      database privileges to a principal.

    - **Name** *(string) --* **[REQUIRED]**

      The name of the table.
    """


_ClientRevokePermissionsResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "_ClientRevokePermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)


class ClientRevokePermissionsResourceTableWithColumnsColumnWildcardTypeDef(
    _ClientRevokePermissionsResourceTableWithColumnsColumnWildcardTypeDef
):
    """
    Type definition for `ClientRevokePermissionsResourceTableWithColumns` `ColumnWildcard`

    A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
    ``ColumnWildcard`` is required.

    - **ExcludedColumnNames** *(list) --*

      Excludes column names. Any column with this name will be excluded.

      - *(string) --*
    """


_ClientRevokePermissionsResourceTableWithColumnsTypeDef = TypedDict(
    "_ClientRevokePermissionsResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientRevokePermissionsResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)


class ClientRevokePermissionsResourceTableWithColumnsTypeDef(
    _ClientRevokePermissionsResourceTableWithColumnsTypeDef
):
    """
    Type definition for `ClientRevokePermissionsResource` `TableWithColumns`

    The table with columns for the resource. A principal with permissions to this resource can
    select metadata from the columns of a table in the Data Catalog and the underlying data in
    Amazon S3.

    - **DatabaseName** *(string) --*

      The name of the database for the table with columns resource. Unique to the Data Catalog. A
      database is a set of associated table definitions organized into a logical group. You can
      Grant and Revoke database privileges to a principal.

    - **Name** *(string) --*

      The name of the table resource. A table is a metadata definition that represents your data.
      You can Grant and Revoke table privileges to a principal.

    - **ColumnNames** *(list) --*

      The list of column names for the table. At least one of ``ColumnNames`` or ``ColumnWildcard``
      is required.

      - *(string) --*

    - **ColumnWildcard** *(dict) --*

      A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
      ``ColumnWildcard`` is required.

      - **ExcludedColumnNames** *(list) --*

        Excludes column names. Any column with this name will be excluded.

        - *(string) --*
    """


_ClientRevokePermissionsResourceTypeDef = TypedDict(
    "_ClientRevokePermissionsResourceTypeDef",
    {
        "Catalog": Dict,
        "Database": ClientRevokePermissionsResourceDatabaseTypeDef,
        "Table": ClientRevokePermissionsResourceTableTypeDef,
        "TableWithColumns": ClientRevokePermissionsResourceTableWithColumnsTypeDef,
        "DataLocation": ClientRevokePermissionsResourceDataLocationTypeDef,
    },
    total=False,
)


class ClientRevokePermissionsResourceTypeDef(_ClientRevokePermissionsResourceTypeDef):
    """
    Type definition for `ClientRevokePermissions` `Resource`

    The resource to which permissions are to be revoked.

    - **Catalog** *(dict) --*

      The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the
      persistent metadata store. It contains database definitions, table definitions, and other
      control information to manage your AWS Lake Formation environment.

    - **Database** *(dict) --*

      The database for the resource. Unique to the Data Catalog. A database is a set of associated
      table definitions organized into a logical group. You can Grant and Revoke database permissions
      to a principal.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the database resource. Unique to the Data Catalog.

    - **Table** *(dict) --*

      The table for the resource. A table is a metadata definition that represents your data. You can
      Grant and Revoke table privileges to a principal.

      - **DatabaseName** *(string) --* **[REQUIRED]**

        The name of the database for the table. Unique to a Data Catalog. A database is a set of
        associated table definitions organized into a logical group. You can Grant and Revoke
        database privileges to a principal.

      - **Name** *(string) --* **[REQUIRED]**

        The name of the table.

    - **TableWithColumns** *(dict) --*

      The table with columns for the resource. A principal with permissions to this resource can
      select metadata from the columns of a table in the Data Catalog and the underlying data in
      Amazon S3.

      - **DatabaseName** *(string) --*

        The name of the database for the table with columns resource. Unique to the Data Catalog. A
        database is a set of associated table definitions organized into a logical group. You can
        Grant and Revoke database privileges to a principal.

      - **Name** *(string) --*

        The name of the table resource. A table is a metadata definition that represents your data.
        You can Grant and Revoke table privileges to a principal.

      - **ColumnNames** *(list) --*

        The list of column names for the table. At least one of ``ColumnNames`` or ``ColumnWildcard``
        is required.

        - *(string) --*

      - **ColumnWildcard** *(dict) --*

        A wildcard specified by a ``ColumnWildcard`` object. At least one of ``ColumnNames`` or
        ``ColumnWildcard`` is required.

        - **ExcludedColumnNames** *(list) --*

          Excludes column names. Any column with this name will be excluded.

          - *(string) --*

    - **DataLocation** *(dict) --*

      The location of an Amazon S3 path where permissions are granted or revoked.

      - **ResourceArn** *(string) --* **[REQUIRED]**

        The Amazon Resource Name (ARN) that uniquely identifies the data location resource.
    """

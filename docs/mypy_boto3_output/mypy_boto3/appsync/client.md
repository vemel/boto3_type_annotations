# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.appsync.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Appsync](index.md#appsync) / Client
    - [Client](#client)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_api_key](#clientcreate_api_key)
        - [Client().create_data_source](#clientcreate_data_source)
        - [Client().create_function](#clientcreate_function)
        - [Client().create_graphql_api](#clientcreate_graphql_api)
        - [Client().create_resolver](#clientcreate_resolver)
        - [Client().create_type](#clientcreate_type)
        - [Client().delete_api_key](#clientdelete_api_key)
        - [Client().delete_data_source](#clientdelete_data_source)
        - [Client().delete_function](#clientdelete_function)
        - [Client().delete_graphql_api](#clientdelete_graphql_api)
        - [Client().delete_resolver](#clientdelete_resolver)
        - [Client().delete_type](#clientdelete_type)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_data_source](#clientget_data_source)
        - [Client().get_function](#clientget_function)
        - [Client().get_graphql_api](#clientget_graphql_api)
        - [Client().get_introspection_schema](#clientget_introspection_schema)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_resolver](#clientget_resolver)
        - [Client().get_schema_creation_status](#clientget_schema_creation_status)
        - [Client().get_type](#clientget_type)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_api_keys](#clientlist_api_keys)
        - [Client().list_data_sources](#clientlist_data_sources)
        - [Client().list_functions](#clientlist_functions)
        - [Client().list_graphql_apis](#clientlist_graphql_apis)
        - [Client().list_resolvers](#clientlist_resolvers)
        - [Client().list_resolvers_by_function](#clientlist_resolvers_by_function)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().list_types](#clientlist_types)
        - [Client().start_schema_creation](#clientstart_schema_creation)
        - [Client().tag_resource](#clienttag_resource)
        - [Client().untag_resource](#clientuntag_resource)
        - [Client().update_api_key](#clientupdate_api_key)
        - [Client().update_data_source](#clientupdate_data_source)
        - [Client().update_function](#clientupdate_function)
        - [Client().update_graphql_api](#clientupdate_graphql_api)
        - [Client().update_resolver](#clientupdate_resolver)
        - [Client().update_type](#clientupdate_type)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L12)

```python
class Client(BaseClient):
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L15)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_api_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L19)

```python
def create_api_key(
    apiId: str,
    description: str = None,
    expires: int = None,
) -> Dict[str, Any]:
```

### Client().create_data_source

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L25)

```python
def create_data_source(
    apiId: str,
    name: str,
    type: str,
    description: str = None,
    serviceRoleArn: str = None,
    dynamodbConfig: Dict[str, Any] = None,
    lambdaConfig: Dict[str, Any] = None,
    elasticsearchConfig: Dict[str, Any] = None,
    httpConfig: Dict[str, Any] = None,
    relationalDatabaseConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_function

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L41)

```python
def create_function(
    apiId: str,
    name: str,
    dataSourceName: str,
    requestMappingTemplate: str,
    functionVersion: str,
    description: str = None,
    responseMappingTemplate: str = None,
) -> Dict[str, Any]:
```

### Client().create_graphql_api

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L54)

```python
def create_graphql_api(
    name: str,
    authenticationType: str,
    logConfig: Dict[str, Any] = None,
    userPoolConfig: Dict[str, Any] = None,
    openIDConnectConfig: Dict[str, Any] = None,
    tags: Dict[str, Any] = None,
    additionalAuthenticationProviders: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_resolver

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L67)

```python
def create_resolver(
    apiId: str,
    typeName: str,
    fieldName: str,
    requestMappingTemplate: str,
    dataSourceName: str = None,
    responseMappingTemplate: str = None,
    kind: str = None,
    pipelineConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().create_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L81)

```python
def create_type(apiId: str, definition: str, format: str) -> Dict[str, Any]:
```

### Client().delete_api_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L85)

```python
def delete_api_key(apiId: str, id: str) -> Dict[str, Any]:
```

### Client().delete_data_source

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L89)

```python
def delete_data_source(apiId: str, name: str) -> Dict[str, Any]:
```

### Client().delete_function

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L93)

```python
def delete_function(apiId: str, functionId: str) -> Dict[str, Any]:
```

### Client().delete_graphql_api

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L97)

```python
def delete_graphql_api(apiId: str) -> Dict[str, Any]:
```

### Client().delete_resolver

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L101)

```python
def delete_resolver(
    apiId: str,
    typeName: str,
    fieldName: str,
) -> Dict[str, Any]:
```

### Client().delete_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L107)

```python
def delete_type(apiId: str, typeName: str) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L111)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_data_source

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L121)

```python
def get_data_source(apiId: str, name: str) -> Dict[str, Any]:
```

### Client().get_function

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L125)

```python
def get_function(apiId: str, functionId: str) -> Dict[str, Any]:
```

### Client().get_graphql_api

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L129)

```python
def get_graphql_api(apiId: str) -> Dict[str, Any]:
```

### Client().get_introspection_schema

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L133)

```python
def get_introspection_schema(
    apiId: str,
    format: str,
    includeDirectives: bool = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L139)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_resolver

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L143)

```python
def get_resolver(apiId: str, typeName: str, fieldName: str) -> Dict[str, Any]:
```

### Client().get_schema_creation_status

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L147)

```python
def get_schema_creation_status(apiId: str) -> Dict[str, Any]:
```

### Client().get_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L151)

```python
def get_type(apiId: str, typeName: str, format: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L155)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_api_keys

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L159)

```python
def list_api_keys(
    apiId: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_data_sources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L165)

```python
def list_data_sources(
    apiId: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_functions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L171)

```python
def list_functions(
    apiId: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_graphql_apis

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L177)

```python
def list_graphql_apis(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_resolvers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L183)

```python
def list_resolvers(
    apiId: str,
    typeName: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_resolvers_by_function

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L189)

```python
def list_resolvers_by_function(
    apiId: str,
    functionId: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L195)

```python
def list_tags_for_resource(resourceArn: str) -> Dict[str, Any]:
```

### Client().list_types

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L199)

```python
def list_types(
    apiId: str,
    format: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().start_schema_creation

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L205)

```python
def start_schema_creation(apiId: str, definition: bytes) -> Dict[str, Any]:
```

### Client().tag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L209)

```python
def tag_resource(resourceArn: str, tags: Dict[str, Any]) -> Dict[str, Any]:
```

### Client().untag_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L213)

```python
def untag_resource(resourceArn: str, tagKeys: List[Any]) -> Dict[str, Any]:
```

### Client().update_api_key

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L217)

```python
def update_api_key(
    apiId: str,
    id: str,
    description: str = None,
    expires: int = None,
) -> Dict[str, Any]:
```

### Client().update_data_source

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L223)

```python
def update_data_source(
    apiId: str,
    name: str,
    type: str,
    description: str = None,
    serviceRoleArn: str = None,
    dynamodbConfig: Dict[str, Any] = None,
    lambdaConfig: Dict[str, Any] = None,
    elasticsearchConfig: Dict[str, Any] = None,
    httpConfig: Dict[str, Any] = None,
    relationalDatabaseConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_function

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L239)

```python
def update_function(
    apiId: str,
    name: str,
    functionId: str,
    dataSourceName: str,
    requestMappingTemplate: str,
    functionVersion: str,
    description: str = None,
    responseMappingTemplate: str = None,
) -> Dict[str, Any]:
```

### Client().update_graphql_api

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L253)

```python
def update_graphql_api(
    apiId: str,
    name: str,
    logConfig: Dict[str, Any] = None,
    authenticationType: str = None,
    userPoolConfig: Dict[str, Any] = None,
    openIDConnectConfig: Dict[str, Any] = None,
    additionalAuthenticationProviders: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().update_resolver

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L266)

```python
def update_resolver(
    apiId: str,
    typeName: str,
    fieldName: str,
    requestMappingTemplate: str,
    dataSourceName: str = None,
    responseMappingTemplate: str = None,
    kind: str = None,
    pipelineConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

### Client().update_type

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/appsync/client.py#L280)

```python
def update_type(
    apiId: str,
    typeName: str,
    format: str,
    definition: str = None,
) -> Dict[str, Any]:
```

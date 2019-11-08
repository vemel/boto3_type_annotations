# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.cloudsearch.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Cloudsearch](index.md#cloudsearch) / Client
    - [Client](#client)
        - [Client().build_suggesters](#clientbuild_suggesters)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_domain](#clientcreate_domain)
        - [Client().define_analysis_scheme](#clientdefine_analysis_scheme)
        - [Client().define_expression](#clientdefine_expression)
        - [Client().define_index_field](#clientdefine_index_field)
        - [Client().define_suggester](#clientdefine_suggester)
        - [Client().delete_analysis_scheme](#clientdelete_analysis_scheme)
        - [Client().delete_domain](#clientdelete_domain)
        - [Client().delete_expression](#clientdelete_expression)
        - [Client().delete_index_field](#clientdelete_index_field)
        - [Client().delete_suggester](#clientdelete_suggester)
        - [Client().describe_analysis_schemes](#clientdescribe_analysis_schemes)
        - [Client().describe_availability_options](#clientdescribe_availability_options)
        - [Client().describe_domains](#clientdescribe_domains)
        - [Client().describe_expressions](#clientdescribe_expressions)
        - [Client().describe_index_fields](#clientdescribe_index_fields)
        - [Client().describe_scaling_parameters](#clientdescribe_scaling_parameters)
        - [Client().describe_service_access_policies](#clientdescribe_service_access_policies)
        - [Client().describe_suggesters](#clientdescribe_suggesters)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().index_documents](#clientindex_documents)
        - [Client().list_domain_names](#clientlist_domain_names)
        - [Client().update_availability_options](#clientupdate_availability_options)
        - [Client().update_scaling_parameters](#clientupdate_scaling_parameters)
        - [Client().update_service_access_policies](#clientupdate_service_access_policies)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L12)

```python
class Client(BaseClient):
```

### Client().build_suggesters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L15)

```python
def build_suggesters(DomainName: str) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L19)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L23)

```python
def create_domain(DomainName: str) -> Dict[str, Any]:
```

### Client().define_analysis_scheme

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L27)

```python
def define_analysis_scheme(
    DomainName: str,
    AnalysisScheme: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().define_expression

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L33)

```python
def define_expression(
    DomainName: str,
    Expression: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().define_index_field

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L39)

```python
def define_index_field(
    DomainName: str,
    IndexField: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().define_suggester

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L45)

```python
def define_suggester(
    DomainName: str,
    Suggester: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().delete_analysis_scheme

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L51)

```python
def delete_analysis_scheme(
    DomainName: str,
    AnalysisSchemeName: str,
) -> Dict[str, Any]:
```

### Client().delete_domain

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L57)

```python
def delete_domain(DomainName: str) -> Dict[str, Any]:
```

### Client().delete_expression

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L61)

```python
def delete_expression(DomainName: str, ExpressionName: str) -> Dict[str, Any]:
```

### Client().delete_index_field

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L65)

```python
def delete_index_field(
    DomainName: str,
    IndexFieldName: str,
) -> Dict[str, Any]:
```

### Client().delete_suggester

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L71)

```python
def delete_suggester(DomainName: str, SuggesterName: str) -> Dict[str, Any]:
```

### Client().describe_analysis_schemes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L75)

```python
def describe_analysis_schemes(
    DomainName: str,
    AnalysisSchemeNames: List[Any] = None,
    Deployed: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_availability_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L84)

```python
def describe_availability_options(
    DomainName: str,
    Deployed: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_domains

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L90)

```python
def describe_domains(DomainNames: List[Any] = None) -> Dict[str, Any]:
```

### Client().describe_expressions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L94)

```python
def describe_expressions(
    DomainName: str,
    ExpressionNames: List[Any] = None,
    Deployed: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_index_fields

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L100)

```python
def describe_index_fields(
    DomainName: str,
    FieldNames: List[Any] = None,
    Deployed: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_scaling_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L106)

```python
def describe_scaling_parameters(DomainName: str) -> Dict[str, Any]:
```

### Client().describe_service_access_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L110)

```python
def describe_service_access_policies(
    DomainName: str,
    Deployed: bool = None,
) -> Dict[str, Any]:
```

### Client().describe_suggesters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L116)

```python
def describe_suggesters(
    DomainName: str,
    SuggesterNames: List[Any] = None,
    Deployed: bool = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L122)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L132)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L136)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().index_documents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L140)

```python
def index_documents(DomainName: str) -> Dict[str, Any]:
```

### Client().list_domain_names

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L144)

```python
def list_domain_names() -> Dict[str, Any]:
```

### Client().update_availability_options

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L148)

```python
def update_availability_options(
    DomainName: str,
    MultiAZ: bool,
) -> Dict[str, Any]:
```

### Client().update_scaling_parameters

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L154)

```python
def update_scaling_parameters(
    DomainName: str,
    ScalingParameters: Dict[str, Any],
) -> Dict[str, Any]:
```

### Client().update_service_access_policies

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/cloudsearch/client.py#L160)

```python
def update_service_access_policies(
    DomainName: str,
    AccessPolicies: str,
) -> Dict[str, Any]:
```

# Client

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.inspector.client](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Inspector](index.md#inspector) / Client
    - [Client](#client)
        - [Client().add_attributes_to_findings](#clientadd_attributes_to_findings)
        - [Client().can_paginate](#clientcan_paginate)
        - [Client().create_assessment_target](#clientcreate_assessment_target)
        - [Client().create_assessment_template](#clientcreate_assessment_template)
        - [Client().create_exclusions_preview](#clientcreate_exclusions_preview)
        - [Client().create_resource_group](#clientcreate_resource_group)
        - [Client().delete_assessment_run](#clientdelete_assessment_run)
        - [Client().delete_assessment_target](#clientdelete_assessment_target)
        - [Client().delete_assessment_template](#clientdelete_assessment_template)
        - [Client().describe_assessment_runs](#clientdescribe_assessment_runs)
        - [Client().describe_assessment_targets](#clientdescribe_assessment_targets)
        - [Client().describe_assessment_templates](#clientdescribe_assessment_templates)
        - [Client().describe_cross_account_access_role](#clientdescribe_cross_account_access_role)
        - [Client().describe_exclusions](#clientdescribe_exclusions)
        - [Client().describe_findings](#clientdescribe_findings)
        - [Client().describe_resource_groups](#clientdescribe_resource_groups)
        - [Client().describe_rules_packages](#clientdescribe_rules_packages)
        - [Client().generate_presigned_url](#clientgenerate_presigned_url)
        - [Client().get_assessment_report](#clientget_assessment_report)
        - [Client().get_exclusions_preview](#clientget_exclusions_preview)
        - [Client().get_paginator](#clientget_paginator)
        - [Client().get_telemetry_metadata](#clientget_telemetry_metadata)
        - [Client().get_waiter](#clientget_waiter)
        - [Client().list_assessment_run_agents](#clientlist_assessment_run_agents)
        - [Client().list_assessment_runs](#clientlist_assessment_runs)
        - [Client().list_assessment_targets](#clientlist_assessment_targets)
        - [Client().list_assessment_templates](#clientlist_assessment_templates)
        - [Client().list_event_subscriptions](#clientlist_event_subscriptions)
        - [Client().list_exclusions](#clientlist_exclusions)
        - [Client().list_findings](#clientlist_findings)
        - [Client().list_rules_packages](#clientlist_rules_packages)
        - [Client().list_tags_for_resource](#clientlist_tags_for_resource)
        - [Client().preview_agents](#clientpreview_agents)
        - [Client().register_cross_account_access_role](#clientregister_cross_account_access_role)
        - [Client().remove_attributes_from_findings](#clientremove_attributes_from_findings)
        - [Client().set_tags_for_resource](#clientset_tags_for_resource)
        - [Client().start_assessment_run](#clientstart_assessment_run)
        - [Client().stop_assessment_run](#clientstop_assessment_run)
        - [Client().subscribe_to_event](#clientsubscribe_to_event)
        - [Client().unsubscribe_from_event](#clientunsubscribe_from_event)
        - [Client().update_assessment_target](#clientupdate_assessment_target)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L12)

```python
class Client(BaseClient):
```

### Client().add_attributes_to_findings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L15)

```python
def add_attributes_to_findings(
    findingArns: List[Any],
    attributes: List[Any],
) -> Dict[str, Any]:
```

### Client().can_paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L21)

```python
def can_paginate(operation_name: str = None) -> None:
```

### Client().create_assessment_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L25)

```python
def create_assessment_target(
    assessmentTargetName: str,
    resourceGroupArn: str = None,
) -> Dict[str, Any]:
```

### Client().create_assessment_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L31)

```python
def create_assessment_template(
    assessmentTargetArn: str,
    assessmentTemplateName: str,
    durationInSeconds: int,
    rulesPackageArns: List[Any],
    userAttributesForFindings: List[Any] = None,
) -> Dict[str, Any]:
```

### Client().create_exclusions_preview

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L42)

```python
def create_exclusions_preview(assessmentTemplateArn: str) -> Dict[str, Any]:
```

### Client().create_resource_group

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L46)

```python
def create_resource_group(resourceGroupTags: List[Any]) -> Dict[str, Any]:
```

### Client().delete_assessment_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L50)

```python
def delete_assessment_run(assessmentRunArn: str) -> None:
```

### Client().delete_assessment_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L54)

```python
def delete_assessment_target(assessmentTargetArn: str) -> None:
```

### Client().delete_assessment_template

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L58)

```python
def delete_assessment_template(assessmentTemplateArn: str) -> None:
```

### Client().describe_assessment_runs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L62)

```python
def describe_assessment_runs(assessmentRunArns: List[Any]) -> Dict[str, Any]:
```

### Client().describe_assessment_targets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L66)

```python
def describe_assessment_targets(
    assessmentTargetArns: List[Any],
) -> Dict[str, Any]:
```

### Client().describe_assessment_templates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L72)

```python
def describe_assessment_templates(
    assessmentTemplateArns: List[Any],
) -> Dict[str, Any]:
```

### Client().describe_cross_account_access_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L78)

```python
def describe_cross_account_access_role() -> Dict[str, Any]:
```

### Client().describe_exclusions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L82)

```python
def describe_exclusions(
    exclusionArns: List[Any],
    locale: str = None,
) -> Dict[str, Any]:
```

### Client().describe_findings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L88)

```python
def describe_findings(
    findingArns: List[Any],
    locale: str = None,
) -> Dict[str, Any]:
```

### Client().describe_resource_groups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L94)

```python
def describe_resource_groups(resourceGroupArns: List[Any]) -> Dict[str, Any]:
```

### Client().describe_rules_packages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L98)

```python
def describe_rules_packages(
    rulesPackageArns: List[Any],
    locale: str = None,
) -> Dict[str, Any]:
```

### Client().generate_presigned_url

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L104)

```python
def generate_presigned_url(
    ClientMethod: str = None,
    Params: Dict[str, Any] = None,
    ExpiresIn: int = None,
    HttpMethod: str = None,
) -> None:
```

### Client().get_assessment_report

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L114)

```python
def get_assessment_report(
    assessmentRunArn: str,
    reportFileFormat: str,
    reportType: str,
) -> Dict[str, Any]:
```

### Client().get_exclusions_preview

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L120)

```python
def get_exclusions_preview(
    assessmentTemplateArn: str,
    previewToken: str,
    nextToken: str = None,
    maxResults: int = None,
    locale: str = None,
) -> Dict[str, Any]:
```

### Client().get_paginator

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L131)

```python
def get_paginator(operation_name: str = None) -> Paginator:
```

### Client().get_telemetry_metadata

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L135)

```python
def get_telemetry_metadata(assessmentRunArn: str) -> Dict[str, Any]:
```

### Client().get_waiter

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L139)

```python
def get_waiter(waiter_name: str = None) -> Waiter:
```

### Client().list_assessment_run_agents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L143)

```python
def list_assessment_run_agents(
    assessmentRunArn: str,
    filter: Dict[str, Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_assessment_runs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L153)

```python
def list_assessment_runs(
    assessmentTemplateArns: List[Any] = None,
    filter: Dict[str, Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_assessment_targets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L163)

```python
def list_assessment_targets(
    filter: Dict[str, Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_assessment_templates

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L172)

```python
def list_assessment_templates(
    assessmentTargetArns: List[Any] = None,
    filter: Dict[str, Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_event_subscriptions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L182)

```python
def list_event_subscriptions(
    resourceArn: str = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_exclusions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L188)

```python
def list_exclusions(
    assessmentRunArn: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_findings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L194)

```python
def list_findings(
    assessmentRunArns: List[Any] = None,
    filter: Dict[str, Any] = None,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_rules_packages

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L204)

```python
def list_rules_packages(
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().list_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L210)

```python
def list_tags_for_resource(resourceArn: str) -> Dict[str, Any]:
```

### Client().preview_agents

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L214)

```python
def preview_agents(
    previewAgentsArn: str,
    nextToken: str = None,
    maxResults: int = None,
) -> Dict[str, Any]:
```

### Client().register_cross_account_access_role

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L220)

```python
def register_cross_account_access_role(roleArn: str) -> None:
```

### Client().remove_attributes_from_findings

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L224)

```python
def remove_attributes_from_findings(
    findingArns: List[Any],
    attributeKeys: List[Any],
) -> Dict[str, Any]:
```

### Client().set_tags_for_resource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L230)

```python
def set_tags_for_resource(resourceArn: str, tags: List[Any] = None) -> None:
```

### Client().start_assessment_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L234)

```python
def start_assessment_run(
    assessmentTemplateArn: str,
    assessmentRunName: str = None,
) -> Dict[str, Any]:
```

### Client().stop_assessment_run

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L240)

```python
def stop_assessment_run(
    assessmentRunArn: str,
    stopAction: str = None,
) -> None:
```

### Client().subscribe_to_event

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L246)

```python
def subscribe_to_event(resourceArn: str, event: str, topicArn: str) -> None:
```

### Client().unsubscribe_from_event

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L250)

```python
def unsubscribe_from_event(
    resourceArn: str,
    event: str,
    topicArn: str,
) -> None:
```

### Client().update_assessment_target

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/inspector/client.py#L256)

```python
def update_assessment_target(
    assessmentTargetArn: str,
    assessmentTargetName: str,
    resourceGroupArn: str = None,
) -> None:
```

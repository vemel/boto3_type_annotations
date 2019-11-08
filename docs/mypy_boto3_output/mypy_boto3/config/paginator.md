# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.config.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Config](index.md#config) / Paginator
    - [DescribeAggregateComplianceByConfigRules](#describeaggregatecompliancebyconfigrules)
        - [DescribeAggregateComplianceByConfigRules().paginate](#describeaggregatecompliancebyconfigrulespaginate)
    - [DescribeAggregationAuthorizations](#describeaggregationauthorizations)
        - [DescribeAggregationAuthorizations().paginate](#describeaggregationauthorizationspaginate)
    - [DescribeComplianceByConfigRule](#describecompliancebyconfigrule)
        - [DescribeComplianceByConfigRule().paginate](#describecompliancebyconfigrulepaginate)
    - [DescribeComplianceByResource](#describecompliancebyresource)
        - [DescribeComplianceByResource().paginate](#describecompliancebyresourcepaginate)
    - [DescribeConfigRuleEvaluationStatus](#describeconfigruleevaluationstatus)
        - [DescribeConfigRuleEvaluationStatus().paginate](#describeconfigruleevaluationstatuspaginate)
    - [DescribeConfigRules](#describeconfigrules)
        - [DescribeConfigRules().paginate](#describeconfigrulespaginate)
    - [DescribeConfigurationAggregatorSourcesStatus](#describeconfigurationaggregatorsourcesstatus)
        - [DescribeConfigurationAggregatorSourcesStatus().paginate](#describeconfigurationaggregatorsourcesstatuspaginate)
    - [DescribeConfigurationAggregators](#describeconfigurationaggregators)
        - [DescribeConfigurationAggregators().paginate](#describeconfigurationaggregatorspaginate)
    - [DescribePendingAggregationRequests](#describependingaggregationrequests)
        - [DescribePendingAggregationRequests().paginate](#describependingaggregationrequestspaginate)
    - [DescribeRemediationExecutionStatus](#describeremediationexecutionstatus)
        - [DescribeRemediationExecutionStatus().paginate](#describeremediationexecutionstatuspaginate)
    - [DescribeRetentionConfigurations](#describeretentionconfigurations)
        - [DescribeRetentionConfigurations().paginate](#describeretentionconfigurationspaginate)
    - [GetAggregateComplianceDetailsByConfigRule](#getaggregatecompliancedetailsbyconfigrule)
        - [GetAggregateComplianceDetailsByConfigRule().paginate](#getaggregatecompliancedetailsbyconfigrulepaginate)
    - [GetComplianceDetailsByConfigRule](#getcompliancedetailsbyconfigrule)
        - [GetComplianceDetailsByConfigRule().paginate](#getcompliancedetailsbyconfigrulepaginate)
    - [GetComplianceDetailsByResource](#getcompliancedetailsbyresource)
        - [GetComplianceDetailsByResource().paginate](#getcompliancedetailsbyresourcepaginate)
    - [GetResourceConfigHistory](#getresourceconfighistory)
        - [GetResourceConfigHistory().paginate](#getresourceconfighistorypaginate)
    - [ListAggregateDiscoveredResources](#listaggregatediscoveredresources)
        - [ListAggregateDiscoveredResources().paginate](#listaggregatediscoveredresourcespaginate)
    - [ListDiscoveredResources](#listdiscoveredresources)
        - [ListDiscoveredResources().paginate](#listdiscoveredresourcespaginate)

## DescribeAggregateComplianceByConfigRules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L11)

```python
class DescribeAggregateComplianceByConfigRules(Paginator):
```

### DescribeAggregateComplianceByConfigRules().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L14)

```python
def paginate(
    ConfigurationAggregatorName: str,
    Filters: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeAggregationAuthorizations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L23)

```python
class DescribeAggregationAuthorizations(Paginator):
```

### DescribeAggregationAuthorizations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L26)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## DescribeComplianceByConfigRule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L30)

```python
class DescribeComplianceByConfigRule(Paginator):
```

### DescribeComplianceByConfigRule().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L33)

```python
def paginate(
    ConfigRuleNames: List[Any] = None,
    ComplianceTypes: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeComplianceByResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L42)

```python
class DescribeComplianceByResource(Paginator):
```

### DescribeComplianceByResource().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L45)

```python
def paginate(
    ResourceType: str = None,
    ResourceId: str = None,
    ComplianceTypes: List[Any] = None,
    Limit: int = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeConfigRuleEvaluationStatus

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L56)

```python
class DescribeConfigRuleEvaluationStatus(Paginator):
```

### DescribeConfigRuleEvaluationStatus().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L59)

```python
def paginate(
    ConfigRuleNames: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeConfigRules

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L65)

```python
class DescribeConfigRules(Paginator):
```

### DescribeConfigRules().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L68)

```python
def paginate(
    ConfigRuleNames: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeConfigurationAggregatorSourcesStatus

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L74)

```python
class DescribeConfigurationAggregatorSourcesStatus(Paginator):
```

### DescribeConfigurationAggregatorSourcesStatus().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L77)

```python
def paginate(
    ConfigurationAggregatorName: str,
    UpdateStatus: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeConfigurationAggregators

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L86)

```python
class DescribeConfigurationAggregators(Paginator):
```

### DescribeConfigurationAggregators().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L89)

```python
def paginate(
    ConfigurationAggregatorNames: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribePendingAggregationRequests

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L97)

```python
class DescribePendingAggregationRequests(Paginator):
```

### DescribePendingAggregationRequests().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L100)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## DescribeRemediationExecutionStatus

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L104)

```python
class DescribeRemediationExecutionStatus(Paginator):
```

### DescribeRemediationExecutionStatus().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L107)

```python
def paginate(
    ConfigRuleName: str,
    ResourceKeys: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## DescribeRetentionConfigurations

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L116)

```python
class DescribeRetentionConfigurations(Paginator):
```

### DescribeRetentionConfigurations().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L119)

```python
def paginate(
    RetentionConfigurationNames: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetAggregateComplianceDetailsByConfigRule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L127)

```python
class GetAggregateComplianceDetailsByConfigRule(Paginator):
```

### GetAggregateComplianceDetailsByConfigRule().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L130)

```python
def paginate(
    ConfigurationAggregatorName: str,
    ConfigRuleName: str,
    AccountId: str,
    AwsRegion: str,
    ComplianceType: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetComplianceDetailsByConfigRule

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L142)

```python
class GetComplianceDetailsByConfigRule(Paginator):
```

### GetComplianceDetailsByConfigRule().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L145)

```python
def paginate(
    ConfigRuleName: str,
    ComplianceTypes: List[Any] = None,
    Limit: int = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetComplianceDetailsByResource

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L155)

```python
class GetComplianceDetailsByResource(Paginator):
```

### GetComplianceDetailsByResource().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L158)

```python
def paginate(
    ResourceType: str,
    ResourceId: str,
    ComplianceTypes: List[Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## GetResourceConfigHistory

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L168)

```python
class GetResourceConfigHistory(Paginator):
```

### GetResourceConfigHistory().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L171)

```python
def paginate(
    resourceType: str,
    resourceId: str,
    laterTime: datetime = None,
    earlierTime: datetime = None,
    chronologicalOrder: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListAggregateDiscoveredResources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L183)

```python
class ListAggregateDiscoveredResources(Paginator):
```

### ListAggregateDiscoveredResources().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L186)

```python
def paginate(
    ConfigurationAggregatorName: str,
    ResourceType: str,
    Filters: Dict[str, Any] = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListDiscoveredResources

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L196)

```python
class ListDiscoveredResources(Paginator):
```

### ListDiscoveredResources().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/config/paginator.py#L199)

```python
def paginate(
    resourceType: str,
    resourceIds: List[Any] = None,
    resourceName: str = None,
    limit: int = None,
    includeDeletedResources: bool = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

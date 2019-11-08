# Paginator

> Auto-generated documentation for [mypy_boto3_output.mypy_boto3.personalize.paginator](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py) module.

- [mypy-boto3](../../../README.md#mypy_boto3) / [Modules](../../../MODULES.md#mypy-boto3-modules) / `Mypy Boto3 Output` / [Mypy Boto3](../index.md#mypy-boto3) / [Personalize](index.md#personalize) / Paginator
    - [ListCampaigns](#listcampaigns)
        - [ListCampaigns().paginate](#listcampaignspaginate)
    - [ListDatasetGroups](#listdatasetgroups)
        - [ListDatasetGroups().paginate](#listdatasetgroupspaginate)
    - [ListDatasetImportJobs](#listdatasetimportjobs)
        - [ListDatasetImportJobs().paginate](#listdatasetimportjobspaginate)
    - [ListDatasets](#listdatasets)
        - [ListDatasets().paginate](#listdatasetspaginate)
    - [ListEventTrackers](#listeventtrackers)
        - [ListEventTrackers().paginate](#listeventtrackerspaginate)
    - [ListRecipes](#listrecipes)
        - [ListRecipes().paginate](#listrecipespaginate)
    - [ListSchemas](#listschemas)
        - [ListSchemas().paginate](#listschemaspaginate)
    - [ListSolutionVersions](#listsolutionversions)
        - [ListSolutionVersions().paginate](#listsolutionversionspaginate)
    - [ListSolutions](#listsolutions)
        - [ListSolutions().paginate](#listsolutionspaginate)

## ListCampaigns

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py#L9)

```python
class ListCampaigns(Paginator):
```

### ListCampaigns().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py#L12)

```python
def paginate(
    solutionArn: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListDatasetGroups

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py#L18)

```python
class ListDatasetGroups(Paginator):
```

### ListDatasetGroups().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py#L21)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListDatasetImportJobs

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py#L25)

```python
class ListDatasetImportJobs(Paginator):
```

### ListDatasetImportJobs().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py#L28)

```python
def paginate(
    datasetArn: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListDatasets

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py#L34)

```python
class ListDatasets(Paginator):
```

### ListDatasets().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py#L37)

```python
def paginate(
    datasetGroupArn: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListEventTrackers

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py#L43)

```python
class ListEventTrackers(Paginator):
```

### ListEventTrackers().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py#L46)

```python
def paginate(
    datasetGroupArn: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListRecipes

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py#L52)

```python
class ListRecipes(Paginator):
```

### ListRecipes().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py#L55)

```python
def paginate(
    recipeProvider: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListSchemas

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py#L61)

```python
class ListSchemas(Paginator):
```

### ListSchemas().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py#L64)

```python
def paginate(PaginationConfig: Dict[str, Any] = None) -> Dict[str, Any]:
```

## ListSolutionVersions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py#L68)

```python
class ListSolutionVersions(Paginator):
```

### ListSolutionVersions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py#L71)

```python
def paginate(
    solutionArn: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

## ListSolutions

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py#L77)

```python
class ListSolutions(Paginator):
```

### ListSolutions().paginate

[[find in source code]](https://github.com/vemel/mypy_boto3/blob/master/mypy_boto3_output/mypy_boto3/personalize/paginator.py#L80)

```python
def paginate(
    datasetGroupArn: str = None,
    PaginationConfig: Dict[str, Any] = None,
) -> Dict[str, Any]:
```

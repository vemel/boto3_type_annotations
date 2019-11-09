# mypy_boto3

[![PyPI - Handsdown](https://img.shields.io/pypi/v/mypy-boto3.svg?color=blue&style=for-the-badge)](https://pypi.org/project/mypy-boto3)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mypy-boto3.svg?color=blue&style=for-the-badge)](https://pypi.org/project/mypy-boto3)
[![Docs](https://img.shields.io/readthedocs/mypy-boto3.svg?color=blue&style=for-the-badge)](https://mypy-boto3.readthedocs.io/)

Mypy-friendly type annotations for boto3.

- [mypy_boto3](#mypyboto3)
  - [Installation](#installation)
  - [Usage](#usage)
  - [How it works](#how-it-works)
  - [Differences from boto3-type-annotations](#differences-from-boto3-type-annotations)
  - [What's next](#whats-next)
  - [Thank you](#thank-you)
  - [Submodules](#submodules)
    - [Examples](#examples)
    - [List of all submodules](#list-of-all-submodules)

## Installation

```bash
# install only `mypy_boto3.s3` for S3 service annotations
pip install mypy-boto3[s3]

# or install multiple services
pip install mypy-boto3[s3,ec2]

# or install S3 service with docs
pip install mypy-boto3[s3-with-docs]

# or install all services
pip install mypy-boto3[all]

# or even install all boto3 services annotations
# WARNING: this will eat ~70 MB of space
pip install mypy-boto3[all-with-docs]
```

## Usage

- Install [mypy](https://github.com/python/mypy) and optionally enable it in your IDE
- Install [boto3](https://github.com/boto/boto3)
- Now imports from `boto3` and `boto3.session` are annotated automatically

```python
import boto3

client = boto3.client("s3")

# IDE autocomplete suggests function name and arguments here
client.create_bucket(Bucket="bucket")

# (mypy) error: Missing positional argument "Key" in call to "get_object" of "Client"
client.get_object(Bucket="bucket")

# (mypy) error: Argument "Key" to "get_object" of "Client" has incompatible type "None"; expected "str"
client.get_object(Bucket="bucket", Key=None)

resource = boto3.Session(region_name="us-west-1").resource("s3")

# IDE autocomplete suggests function name and arguments here
bucket = resource.Bucket("bucket")

# (mypy) error: Unexpected keyword argument "key" for "upload_file" of "Bucket"
bucket.upload_file(Filename="my.txt", key="my-txt")
```

## How it works

There is also a package `mypy-boto3-builder` that builds interface files from `boto3` documentation.

## Differences from boto3-type-annotations

- Fully type annotated
- `mypy` compatibility
- Generated types for return values and arguments
- Added ServiceResource sub-collections
- Support service-specific sub-modules
- Modules documentation
- Type annotations for return structures (in progress)

## What's next

- Add `TypedDict` types for arguments and return types to check keys and values
- Allow installation of sub-modules
- Always include docs and support them in generated documentation

## Thank you

- Guys behind [boto3-type-annotations](https://pypi.org/project/boto3-type-annotations/),
  this package is based on top of their work
- [black](https://github.com/psf/black) developers for awesome formatting tool
- [mypy](https://github.com/python/mypy) for doing all dirty work for us


## Submodules

### Examples

You can install any submodules using `pip`

```bash
# pip install mypy-boto3[<submodule_name>, ...]

# install ec2, s3 and sqs type annotations
pip install mypy-boto3[s3, ec2, sqs]

# install ec2, s3, rds, lambda, sqs and cloudformation type annotations
# with included documentation
pip install mypy-boto3[essential-with-docs]

# install type annotations for all boto3 services
pip install mypy-boto3[all]
```

### List of all submodules

- `all` - Type annotations for all `boto3` services.
- `all-with-docs` - Type annotations for all `boto3` services with included documentation.
- `essential` - Type annotations for `ec2`, `s3`, `rds`, `lambda`, `sqs` and `cloudformation` `boto3` services.
- `essential-with-docs` - Type annotations for `ec2`, `s3`, `rds`, `lambda`, `sqs` and `cloudformation` `boto3` services with included documentation.
- `acm` - Type annotations for `boto3` [acm](https://pypi.org/project/mypy-boto3-acm/) service.
- `acm-with-docs` - Type annotations for `boto3` [acm](https://pypi.org/project/mypy-boto3-acm-with-docs/) service with included documentation.
- `acm-pca` - Type annotations for `boto3` [acm-pca](https://pypi.org/project/mypy-boto3-acm-pca/) service.
- `acm-pca-with-docs` - Type annotations for `boto3` [acm-pca](https://pypi.org/project/mypy-boto3-acm-pca-with-docs/) service with included documentation.
- `alexaforbusiness` - Type annotations for `boto3` [alexaforbusiness](https://pypi.org/project/mypy-boto3-alexaforbusiness/) service.
- `alexaforbusiness-with-docs` - Type annotations for `boto3` [alexaforbusiness](https://pypi.org/project/mypy-boto3-alexaforbusiness-with-docs/) service with included documentation.
- `amplify` - Type annotations for `boto3` [amplify](https://pypi.org/project/mypy-boto3-amplify/) service.
- `amplify-with-docs` - Type annotations for `boto3` [amplify](https://pypi.org/project/mypy-boto3-amplify-with-docs/) service with included documentation.
- `apigateway` - Type annotations for `boto3` [apigateway](https://pypi.org/project/mypy-boto3-apigateway/) service.
- `apigateway-with-docs` - Type annotations for `boto3` [apigateway](https://pypi.org/project/mypy-boto3-apigateway-with-docs/) service with included documentation.
- `apigatewaymanagementapi` - Type annotations for `boto3` [apigatewaymanagementapi](https://pypi.org/project/mypy-boto3-apigatewaymanagementapi/) service.
- `apigatewaymanagementapi-with-docs` - Type annotations for `boto3` [apigatewaymanagementapi](https://pypi.org/project/mypy-boto3-apigatewaymanagementapi-with-docs/) service with included documentation.
- `apigatewayv2` - Type annotations for `boto3` [apigatewayv2](https://pypi.org/project/mypy-boto3-apigatewayv2/) service.
- `apigatewayv2-with-docs` - Type annotations for `boto3` [apigatewayv2](https://pypi.org/project/mypy-boto3-apigatewayv2-with-docs/) service with included documentation.
- `application-autoscaling` - Type annotations for `boto3` [application-autoscaling](https://pypi.org/project/mypy-boto3-application-autoscaling/) service.
- `application-autoscaling-with-docs` - Type annotations for `boto3` [application-autoscaling](https://pypi.org/project/mypy-boto3-application-autoscaling-with-docs/) service with included documentation.
- `application-insights` - Type annotations for `boto3` [application-insights](https://pypi.org/project/mypy-boto3-application-insights/) service.
- `application-insights-with-docs` - Type annotations for `boto3` [application-insights](https://pypi.org/project/mypy-boto3-application-insights-with-docs/) service with included documentation.
- `appmesh` - Type annotations for `boto3` [appmesh](https://pypi.org/project/mypy-boto3-appmesh/) service.
- `appmesh-with-docs` - Type annotations for `boto3` [appmesh](https://pypi.org/project/mypy-boto3-appmesh-with-docs/) service with included documentation.
- `appstream` - Type annotations for `boto3` [appstream](https://pypi.org/project/mypy-boto3-appstream/) service.
- `appstream-with-docs` - Type annotations for `boto3` [appstream](https://pypi.org/project/mypy-boto3-appstream-with-docs/) service with included documentation.
- `appsync` - Type annotations for `boto3` [appsync](https://pypi.org/project/mypy-boto3-appsync/) service.
- `appsync-with-docs` - Type annotations for `boto3` [appsync](https://pypi.org/project/mypy-boto3-appsync-with-docs/) service with included documentation.
- `athena` - Type annotations for `boto3` [athena](https://pypi.org/project/mypy-boto3-athena/) service.
- `athena-with-docs` - Type annotations for `boto3` [athena](https://pypi.org/project/mypy-boto3-athena-with-docs/) service with included documentation.
- `autoscaling` - Type annotations for `boto3` [autoscaling](https://pypi.org/project/mypy-boto3-autoscaling/) service.
- `autoscaling-with-docs` - Type annotations for `boto3` [autoscaling](https://pypi.org/project/mypy-boto3-autoscaling-with-docs/) service with included documentation.
- `autoscaling-plans` - Type annotations for `boto3` [autoscaling-plans](https://pypi.org/project/mypy-boto3-autoscaling-plans/) service.
- `autoscaling-plans-with-docs` - Type annotations for `boto3` [autoscaling-plans](https://pypi.org/project/mypy-boto3-autoscaling-plans-with-docs/) service with included documentation.
- `backup` - Type annotations for `boto3` [backup](https://pypi.org/project/mypy-boto3-backup/) service.
- `backup-with-docs` - Type annotations for `boto3` [backup](https://pypi.org/project/mypy-boto3-backup-with-docs/) service with included documentation.
- `batch` - Type annotations for `boto3` [batch](https://pypi.org/project/mypy-boto3-batch/) service.
- `batch-with-docs` - Type annotations for `boto3` [batch](https://pypi.org/project/mypy-boto3-batch-with-docs/) service with included documentation.
- `budgets` - Type annotations for `boto3` [budgets](https://pypi.org/project/mypy-boto3-budgets/) service.
- `budgets-with-docs` - Type annotations for `boto3` [budgets](https://pypi.org/project/mypy-boto3-budgets-with-docs/) service with included documentation.
- `ce` - Type annotations for `boto3` [ce](https://pypi.org/project/mypy-boto3-ce/) service.
- `ce-with-docs` - Type annotations for `boto3` [ce](https://pypi.org/project/mypy-boto3-ce-with-docs/) service with included documentation.
- `chime` - Type annotations for `boto3` [chime](https://pypi.org/project/mypy-boto3-chime/) service.
- `chime-with-docs` - Type annotations for `boto3` [chime](https://pypi.org/project/mypy-boto3-chime-with-docs/) service with included documentation.
- `cloud9` - Type annotations for `boto3` [cloud9](https://pypi.org/project/mypy-boto3-cloud9/) service.
- `cloud9-with-docs` - Type annotations for `boto3` [cloud9](https://pypi.org/project/mypy-boto3-cloud9-with-docs/) service with included documentation.
- `clouddirectory` - Type annotations for `boto3` [clouddirectory](https://pypi.org/project/mypy-boto3-clouddirectory/) service.
- `clouddirectory-with-docs` - Type annotations for `boto3` [clouddirectory](https://pypi.org/project/mypy-boto3-clouddirectory-with-docs/) service with included documentation.
- `cloudformation` - Type annotations for `boto3` [cloudformation](https://pypi.org/project/mypy-boto3-cloudformation/) service.
- `cloudformation-with-docs` - Type annotations for `boto3` [cloudformation](https://pypi.org/project/mypy-boto3-cloudformation-with-docs/) service with included documentation.
- `cloudfront` - Type annotations for `boto3` [cloudfront](https://pypi.org/project/mypy-boto3-cloudfront/) service.
- `cloudfront-with-docs` - Type annotations for `boto3` [cloudfront](https://pypi.org/project/mypy-boto3-cloudfront-with-docs/) service with included documentation.
- `cloudhsm` - Type annotations for `boto3` [cloudhsm](https://pypi.org/project/mypy-boto3-cloudhsm/) service.
- `cloudhsm-with-docs` - Type annotations for `boto3` [cloudhsm](https://pypi.org/project/mypy-boto3-cloudhsm-with-docs/) service with included documentation.
- `cloudhsmv2` - Type annotations for `boto3` [cloudhsmv2](https://pypi.org/project/mypy-boto3-cloudhsmv2/) service.
- `cloudhsmv2-with-docs` - Type annotations for `boto3` [cloudhsmv2](https://pypi.org/project/mypy-boto3-cloudhsmv2-with-docs/) service with included documentation.
- `cloudsearch` - Type annotations for `boto3` [cloudsearch](https://pypi.org/project/mypy-boto3-cloudsearch/) service.
- `cloudsearch-with-docs` - Type annotations for `boto3` [cloudsearch](https://pypi.org/project/mypy-boto3-cloudsearch-with-docs/) service with included documentation.
- `cloudsearchdomain` - Type annotations for `boto3` [cloudsearchdomain](https://pypi.org/project/mypy-boto3-cloudsearchdomain/) service.
- `cloudsearchdomain-with-docs` - Type annotations for `boto3` [cloudsearchdomain](https://pypi.org/project/mypy-boto3-cloudsearchdomain-with-docs/) service with included documentation.
- `cloudtrail` - Type annotations for `boto3` [cloudtrail](https://pypi.org/project/mypy-boto3-cloudtrail/) service.
- `cloudtrail-with-docs` - Type annotations for `boto3` [cloudtrail](https://pypi.org/project/mypy-boto3-cloudtrail-with-docs/) service with included documentation.
- `cloudwatch` - Type annotations for `boto3` [cloudwatch](https://pypi.org/project/mypy-boto3-cloudwatch/) service.
- `cloudwatch-with-docs` - Type annotations for `boto3` [cloudwatch](https://pypi.org/project/mypy-boto3-cloudwatch-with-docs/) service with included documentation.
- `codebuild` - Type annotations for `boto3` [codebuild](https://pypi.org/project/mypy-boto3-codebuild/) service.
- `codebuild-with-docs` - Type annotations for `boto3` [codebuild](https://pypi.org/project/mypy-boto3-codebuild-with-docs/) service with included documentation.
- `codecommit` - Type annotations for `boto3` [codecommit](https://pypi.org/project/mypy-boto3-codecommit/) service.
- `codecommit-with-docs` - Type annotations for `boto3` [codecommit](https://pypi.org/project/mypy-boto3-codecommit-with-docs/) service with included documentation.
- `codedeploy` - Type annotations for `boto3` [codedeploy](https://pypi.org/project/mypy-boto3-codedeploy/) service.
- `codedeploy-with-docs` - Type annotations for `boto3` [codedeploy](https://pypi.org/project/mypy-boto3-codedeploy-with-docs/) service with included documentation.
- `codepipeline` - Type annotations for `boto3` [codepipeline](https://pypi.org/project/mypy-boto3-codepipeline/) service.
- `codepipeline-with-docs` - Type annotations for `boto3` [codepipeline](https://pypi.org/project/mypy-boto3-codepipeline-with-docs/) service with included documentation.
- `codestar` - Type annotations for `boto3` [codestar](https://pypi.org/project/mypy-boto3-codestar/) service.
- `codestar-with-docs` - Type annotations for `boto3` [codestar](https://pypi.org/project/mypy-boto3-codestar-with-docs/) service with included documentation.
- `codestar-notifications` - Type annotations for `boto3` [codestar-notifications](https://pypi.org/project/mypy-boto3-codestar-notifications/) service.
- `codestar-notifications-with-docs` - Type annotations for `boto3` [codestar-notifications](https://pypi.org/project/mypy-boto3-codestar-notifications-with-docs/) service with included documentation.
- `cognito-identity` - Type annotations for `boto3` [cognito-identity](https://pypi.org/project/mypy-boto3-cognito-identity/) service.
- `cognito-identity-with-docs` - Type annotations for `boto3` [cognito-identity](https://pypi.org/project/mypy-boto3-cognito-identity-with-docs/) service with included documentation.
- `cognito-idp` - Type annotations for `boto3` [cognito-idp](https://pypi.org/project/mypy-boto3-cognito-idp/) service.
- `cognito-idp-with-docs` - Type annotations for `boto3` [cognito-idp](https://pypi.org/project/mypy-boto3-cognito-idp-with-docs/) service with included documentation.
- `cognito-sync` - Type annotations for `boto3` [cognito-sync](https://pypi.org/project/mypy-boto3-cognito-sync/) service.
- `cognito-sync-with-docs` - Type annotations for `boto3` [cognito-sync](https://pypi.org/project/mypy-boto3-cognito-sync-with-docs/) service with included documentation.
- `comprehend` - Type annotations for `boto3` [comprehend](https://pypi.org/project/mypy-boto3-comprehend/) service.
- `comprehend-with-docs` - Type annotations for `boto3` [comprehend](https://pypi.org/project/mypy-boto3-comprehend-with-docs/) service with included documentation.
- `comprehendmedical` - Type annotations for `boto3` [comprehendmedical](https://pypi.org/project/mypy-boto3-comprehendmedical/) service.
- `comprehendmedical-with-docs` - Type annotations for `boto3` [comprehendmedical](https://pypi.org/project/mypy-boto3-comprehendmedical-with-docs/) service with included documentation.
- `config` - Type annotations for `boto3` [config](https://pypi.org/project/mypy-boto3-config/) service.
- `config-with-docs` - Type annotations for `boto3` [config](https://pypi.org/project/mypy-boto3-config-with-docs/) service with included documentation.
- `connect` - Type annotations for `boto3` [connect](https://pypi.org/project/mypy-boto3-connect/) service.
- `connect-with-docs` - Type annotations for `boto3` [connect](https://pypi.org/project/mypy-boto3-connect-with-docs/) service with included documentation.
- `cur` - Type annotations for `boto3` [cur](https://pypi.org/project/mypy-boto3-cur/) service.
- `cur-with-docs` - Type annotations for `boto3` [cur](https://pypi.org/project/mypy-boto3-cur-with-docs/) service with included documentation.
- `datapipeline` - Type annotations for `boto3` [datapipeline](https://pypi.org/project/mypy-boto3-datapipeline/) service.
- `datapipeline-with-docs` - Type annotations for `boto3` [datapipeline](https://pypi.org/project/mypy-boto3-datapipeline-with-docs/) service with included documentation.
- `datasync` - Type annotations for `boto3` [datasync](https://pypi.org/project/mypy-boto3-datasync/) service.
- `datasync-with-docs` - Type annotations for `boto3` [datasync](https://pypi.org/project/mypy-boto3-datasync-with-docs/) service with included documentation.
- `dax` - Type annotations for `boto3` [dax](https://pypi.org/project/mypy-boto3-dax/) service.
- `dax-with-docs` - Type annotations for `boto3` [dax](https://pypi.org/project/mypy-boto3-dax-with-docs/) service with included documentation.
- `devicefarm` - Type annotations for `boto3` [devicefarm](https://pypi.org/project/mypy-boto3-devicefarm/) service.
- `devicefarm-with-docs` - Type annotations for `boto3` [devicefarm](https://pypi.org/project/mypy-boto3-devicefarm-with-docs/) service with included documentation.
- `directconnect` - Type annotations for `boto3` [directconnect](https://pypi.org/project/mypy-boto3-directconnect/) service.
- `directconnect-with-docs` - Type annotations for `boto3` [directconnect](https://pypi.org/project/mypy-boto3-directconnect-with-docs/) service with included documentation.
- `discovery` - Type annotations for `boto3` [discovery](https://pypi.org/project/mypy-boto3-discovery/) service.
- `discovery-with-docs` - Type annotations for `boto3` [discovery](https://pypi.org/project/mypy-boto3-discovery-with-docs/) service with included documentation.
- `dlm` - Type annotations for `boto3` [dlm](https://pypi.org/project/mypy-boto3-dlm/) service.
- `dlm-with-docs` - Type annotations for `boto3` [dlm](https://pypi.org/project/mypy-boto3-dlm-with-docs/) service with included documentation.
- `dms` - Type annotations for `boto3` [dms](https://pypi.org/project/mypy-boto3-dms/) service.
- `dms-with-docs` - Type annotations for `boto3` [dms](https://pypi.org/project/mypy-boto3-dms-with-docs/) service with included documentation.
- `docdb` - Type annotations for `boto3` [docdb](https://pypi.org/project/mypy-boto3-docdb/) service.
- `docdb-with-docs` - Type annotations for `boto3` [docdb](https://pypi.org/project/mypy-boto3-docdb-with-docs/) service with included documentation.
- `ds` - Type annotations for `boto3` [ds](https://pypi.org/project/mypy-boto3-ds/) service.
- `ds-with-docs` - Type annotations for `boto3` [ds](https://pypi.org/project/mypy-boto3-ds-with-docs/) service with included documentation.
- `dynamodb` - Type annotations for `boto3` [dynamodb](https://pypi.org/project/mypy-boto3-dynamodb/) service.
- `dynamodb-with-docs` - Type annotations for `boto3` [dynamodb](https://pypi.org/project/mypy-boto3-dynamodb-with-docs/) service with included documentation.
- `dynamodbstreams` - Type annotations for `boto3` [dynamodbstreams](https://pypi.org/project/mypy-boto3-dynamodbstreams/) service.
- `dynamodbstreams-with-docs` - Type annotations for `boto3` [dynamodbstreams](https://pypi.org/project/mypy-boto3-dynamodbstreams-with-docs/) service with included documentation.
- `ec2` - Type annotations for `boto3` [ec2](https://pypi.org/project/mypy-boto3-ec2/) service.
- `ec2-with-docs` - Type annotations for `boto3` [ec2](https://pypi.org/project/mypy-boto3-ec2-with-docs/) service with included documentation.
- `ec2-instance-connect` - Type annotations for `boto3` [ec2-instance-connect](https://pypi.org/project/mypy-boto3-ec2-instance-connect/) service.
- `ec2-instance-connect-with-docs` - Type annotations for `boto3` [ec2-instance-connect](https://pypi.org/project/mypy-boto3-ec2-instance-connect-with-docs/) service with included documentation.
- `ecr` - Type annotations for `boto3` [ecr](https://pypi.org/project/mypy-boto3-ecr/) service.
- `ecr-with-docs` - Type annotations for `boto3` [ecr](https://pypi.org/project/mypy-boto3-ecr-with-docs/) service with included documentation.
- `ecs` - Type annotations for `boto3` [ecs](https://pypi.org/project/mypy-boto3-ecs/) service.
- `ecs-with-docs` - Type annotations for `boto3` [ecs](https://pypi.org/project/mypy-boto3-ecs-with-docs/) service with included documentation.
- `efs` - Type annotations for `boto3` [efs](https://pypi.org/project/mypy-boto3-efs/) service.
- `efs-with-docs` - Type annotations for `boto3` [efs](https://pypi.org/project/mypy-boto3-efs-with-docs/) service with included documentation.
- `eks` - Type annotations for `boto3` [eks](https://pypi.org/project/mypy-boto3-eks/) service.
- `eks-with-docs` - Type annotations for `boto3` [eks](https://pypi.org/project/mypy-boto3-eks-with-docs/) service with included documentation.
- `elasticache` - Type annotations for `boto3` [elasticache](https://pypi.org/project/mypy-boto3-elasticache/) service.
- `elasticache-with-docs` - Type annotations for `boto3` [elasticache](https://pypi.org/project/mypy-boto3-elasticache-with-docs/) service with included documentation.
- `elasticbeanstalk` - Type annotations for `boto3` [elasticbeanstalk](https://pypi.org/project/mypy-boto3-elasticbeanstalk/) service.
- `elasticbeanstalk-with-docs` - Type annotations for `boto3` [elasticbeanstalk](https://pypi.org/project/mypy-boto3-elasticbeanstalk-with-docs/) service with included documentation.
- `elastictranscoder` - Type annotations for `boto3` [elastictranscoder](https://pypi.org/project/mypy-boto3-elastictranscoder/) service.
- `elastictranscoder-with-docs` - Type annotations for `boto3` [elastictranscoder](https://pypi.org/project/mypy-boto3-elastictranscoder-with-docs/) service with included documentation.
- `elb` - Type annotations for `boto3` [elb](https://pypi.org/project/mypy-boto3-elb/) service.
- `elb-with-docs` - Type annotations for `boto3` [elb](https://pypi.org/project/mypy-boto3-elb-with-docs/) service with included documentation.
- `elbv2` - Type annotations for `boto3` [elbv2](https://pypi.org/project/mypy-boto3-elbv2/) service.
- `elbv2-with-docs` - Type annotations for `boto3` [elbv2](https://pypi.org/project/mypy-boto3-elbv2-with-docs/) service with included documentation.
- `emr` - Type annotations for `boto3` [emr](https://pypi.org/project/mypy-boto3-emr/) service.
- `emr-with-docs` - Type annotations for `boto3` [emr](https://pypi.org/project/mypy-boto3-emr-with-docs/) service with included documentation.
- `es` - Type annotations for `boto3` [es](https://pypi.org/project/mypy-boto3-es/) service.
- `es-with-docs` - Type annotations for `boto3` [es](https://pypi.org/project/mypy-boto3-es-with-docs/) service with included documentation.
- `events` - Type annotations for `boto3` [events](https://pypi.org/project/mypy-boto3-events/) service.
- `events-with-docs` - Type annotations for `boto3` [events](https://pypi.org/project/mypy-boto3-events-with-docs/) service with included documentation.
- `firehose` - Type annotations for `boto3` [firehose](https://pypi.org/project/mypy-boto3-firehose/) service.
- `firehose-with-docs` - Type annotations for `boto3` [firehose](https://pypi.org/project/mypy-boto3-firehose-with-docs/) service with included documentation.
- `fms` - Type annotations for `boto3` [fms](https://pypi.org/project/mypy-boto3-fms/) service.
- `fms-with-docs` - Type annotations for `boto3` [fms](https://pypi.org/project/mypy-boto3-fms-with-docs/) service with included documentation.
- `forecast` - Type annotations for `boto3` [forecast](https://pypi.org/project/mypy-boto3-forecast/) service.
- `forecast-with-docs` - Type annotations for `boto3` [forecast](https://pypi.org/project/mypy-boto3-forecast-with-docs/) service with included documentation.
- `forecastquery` - Type annotations for `boto3` [forecastquery](https://pypi.org/project/mypy-boto3-forecastquery/) service.
- `forecastquery-with-docs` - Type annotations for `boto3` [forecastquery](https://pypi.org/project/mypy-boto3-forecastquery-with-docs/) service with included documentation.
- `fsx` - Type annotations for `boto3` [fsx](https://pypi.org/project/mypy-boto3-fsx/) service.
- `fsx-with-docs` - Type annotations for `boto3` [fsx](https://pypi.org/project/mypy-boto3-fsx-with-docs/) service with included documentation.
- `gamelift` - Type annotations for `boto3` [gamelift](https://pypi.org/project/mypy-boto3-gamelift/) service.
- `gamelift-with-docs` - Type annotations for `boto3` [gamelift](https://pypi.org/project/mypy-boto3-gamelift-with-docs/) service with included documentation.
- `glacier` - Type annotations for `boto3` [glacier](https://pypi.org/project/mypy-boto3-glacier/) service.
- `glacier-with-docs` - Type annotations for `boto3` [glacier](https://pypi.org/project/mypy-boto3-glacier-with-docs/) service with included documentation.
- `globalaccelerator` - Type annotations for `boto3` [globalaccelerator](https://pypi.org/project/mypy-boto3-globalaccelerator/) service.
- `globalaccelerator-with-docs` - Type annotations for `boto3` [globalaccelerator](https://pypi.org/project/mypy-boto3-globalaccelerator-with-docs/) service with included documentation.
- `glue` - Type annotations for `boto3` [glue](https://pypi.org/project/mypy-boto3-glue/) service.
- `glue-with-docs` - Type annotations for `boto3` [glue](https://pypi.org/project/mypy-boto3-glue-with-docs/) service with included documentation.
- `greengrass` - Type annotations for `boto3` [greengrass](https://pypi.org/project/mypy-boto3-greengrass/) service.
- `greengrass-with-docs` - Type annotations for `boto3` [greengrass](https://pypi.org/project/mypy-boto3-greengrass-with-docs/) service with included documentation.
- `groundstation` - Type annotations for `boto3` [groundstation](https://pypi.org/project/mypy-boto3-groundstation/) service.
- `groundstation-with-docs` - Type annotations for `boto3` [groundstation](https://pypi.org/project/mypy-boto3-groundstation-with-docs/) service with included documentation.
- `guardduty` - Type annotations for `boto3` [guardduty](https://pypi.org/project/mypy-boto3-guardduty/) service.
- `guardduty-with-docs` - Type annotations for `boto3` [guardduty](https://pypi.org/project/mypy-boto3-guardduty-with-docs/) service with included documentation.
- `health` - Type annotations for `boto3` [health](https://pypi.org/project/mypy-boto3-health/) service.
- `health-with-docs` - Type annotations for `boto3` [health](https://pypi.org/project/mypy-boto3-health-with-docs/) service with included documentation.
- `iam` - Type annotations for `boto3` [iam](https://pypi.org/project/mypy-boto3-iam/) service.
- `iam-with-docs` - Type annotations for `boto3` [iam](https://pypi.org/project/mypy-boto3-iam-with-docs/) service with included documentation.
- `importexport` - Type annotations for `boto3` [importexport](https://pypi.org/project/mypy-boto3-importexport/) service.
- `importexport-with-docs` - Type annotations for `boto3` [importexport](https://pypi.org/project/mypy-boto3-importexport-with-docs/) service with included documentation.
- `inspector` - Type annotations for `boto3` [inspector](https://pypi.org/project/mypy-boto3-inspector/) service.
- `inspector-with-docs` - Type annotations for `boto3` [inspector](https://pypi.org/project/mypy-boto3-inspector-with-docs/) service with included documentation.
- `iot` - Type annotations for `boto3` [iot](https://pypi.org/project/mypy-boto3-iot/) service.
- `iot-with-docs` - Type annotations for `boto3` [iot](https://pypi.org/project/mypy-boto3-iot-with-docs/) service with included documentation.
- `iot-data` - Type annotations for `boto3` [iot-data](https://pypi.org/project/mypy-boto3-iot-data/) service.
- `iot-data-with-docs` - Type annotations for `boto3` [iot-data](https://pypi.org/project/mypy-boto3-iot-data-with-docs/) service with included documentation.
- `iot-jobs-data` - Type annotations for `boto3` [iot-jobs-data](https://pypi.org/project/mypy-boto3-iot-jobs-data/) service.
- `iot-jobs-data-with-docs` - Type annotations for `boto3` [iot-jobs-data](https://pypi.org/project/mypy-boto3-iot-jobs-data-with-docs/) service with included documentation.
- `iot1click-devices` - Type annotations for `boto3` [iot1click-devices](https://pypi.org/project/mypy-boto3-iot1click-devices/) service.
- `iot1click-devices-with-docs` - Type annotations for `boto3` [iot1click-devices](https://pypi.org/project/mypy-boto3-iot1click-devices-with-docs/) service with included documentation.
- `iot1click-projects` - Type annotations for `boto3` [iot1click-projects](https://pypi.org/project/mypy-boto3-iot1click-projects/) service.
- `iot1click-projects-with-docs` - Type annotations for `boto3` [iot1click-projects](https://pypi.org/project/mypy-boto3-iot1click-projects-with-docs/) service with included documentation.
- `iotanalytics` - Type annotations for `boto3` [iotanalytics](https://pypi.org/project/mypy-boto3-iotanalytics/) service.
- `iotanalytics-with-docs` - Type annotations for `boto3` [iotanalytics](https://pypi.org/project/mypy-boto3-iotanalytics-with-docs/) service with included documentation.
- `iotevents` - Type annotations for `boto3` [iotevents](https://pypi.org/project/mypy-boto3-iotevents/) service.
- `iotevents-with-docs` - Type annotations for `boto3` [iotevents](https://pypi.org/project/mypy-boto3-iotevents-with-docs/) service with included documentation.
- `iotevents-data` - Type annotations for `boto3` [iotevents-data](https://pypi.org/project/mypy-boto3-iotevents-data/) service.
- `iotevents-data-with-docs` - Type annotations for `boto3` [iotevents-data](https://pypi.org/project/mypy-boto3-iotevents-data-with-docs/) service with included documentation.
- `iotthingsgraph` - Type annotations for `boto3` [iotthingsgraph](https://pypi.org/project/mypy-boto3-iotthingsgraph/) service.
- `iotthingsgraph-with-docs` - Type annotations for `boto3` [iotthingsgraph](https://pypi.org/project/mypy-boto3-iotthingsgraph-with-docs/) service with included documentation.
- `kafka` - Type annotations for `boto3` [kafka](https://pypi.org/project/mypy-boto3-kafka/) service.
- `kafka-with-docs` - Type annotations for `boto3` [kafka](https://pypi.org/project/mypy-boto3-kafka-with-docs/) service with included documentation.
- `kinesis` - Type annotations for `boto3` [kinesis](https://pypi.org/project/mypy-boto3-kinesis/) service.
- `kinesis-with-docs` - Type annotations for `boto3` [kinesis](https://pypi.org/project/mypy-boto3-kinesis-with-docs/) service with included documentation.
- `kinesis-video-archived-media` - Type annotations for `boto3` [kinesis-video-archived-media](https://pypi.org/project/mypy-boto3-kinesis-video-archived-media/) service.
- `kinesis-video-archived-media-with-docs` - Type annotations for `boto3` [kinesis-video-archived-media](https://pypi.org/project/mypy-boto3-kinesis-video-archived-media-with-docs/) service with included documentation.
- `kinesis-video-media` - Type annotations for `boto3` [kinesis-video-media](https://pypi.org/project/mypy-boto3-kinesis-video-media/) service.
- `kinesis-video-media-with-docs` - Type annotations for `boto3` [kinesis-video-media](https://pypi.org/project/mypy-boto3-kinesis-video-media-with-docs/) service with included documentation.
- `kinesisanalytics` - Type annotations for `boto3` [kinesisanalytics](https://pypi.org/project/mypy-boto3-kinesisanalytics/) service.
- `kinesisanalytics-with-docs` - Type annotations for `boto3` [kinesisanalytics](https://pypi.org/project/mypy-boto3-kinesisanalytics-with-docs/) service with included documentation.
- `kinesisanalyticsv2` - Type annotations for `boto3` [kinesisanalyticsv2](https://pypi.org/project/mypy-boto3-kinesisanalyticsv2/) service.
- `kinesisanalyticsv2-with-docs` - Type annotations for `boto3` [kinesisanalyticsv2](https://pypi.org/project/mypy-boto3-kinesisanalyticsv2-with-docs/) service with included documentation.
- `kinesisvideo` - Type annotations for `boto3` [kinesisvideo](https://pypi.org/project/mypy-boto3-kinesisvideo/) service.
- `kinesisvideo-with-docs` - Type annotations for `boto3` [kinesisvideo](https://pypi.org/project/mypy-boto3-kinesisvideo-with-docs/) service with included documentation.
- `kms` - Type annotations for `boto3` [kms](https://pypi.org/project/mypy-boto3-kms/) service.
- `kms-with-docs` - Type annotations for `boto3` [kms](https://pypi.org/project/mypy-boto3-kms-with-docs/) service with included documentation.
- `lakeformation` - Type annotations for `boto3` [lakeformation](https://pypi.org/project/mypy-boto3-lakeformation/) service.
- `lakeformation-with-docs` - Type annotations for `boto3` [lakeformation](https://pypi.org/project/mypy-boto3-lakeformation-with-docs/) service with included documentation.
- `lambda` - Type annotations for `boto3` [lambda](https://pypi.org/project/mypy-boto3-lambda/) service.
- `lambda-with-docs` - Type annotations for `boto3` [lambda](https://pypi.org/project/mypy-boto3-lambda-with-docs/) service with included documentation.
- `lex-models` - Type annotations for `boto3` [lex-models](https://pypi.org/project/mypy-boto3-lex-models/) service.
- `lex-models-with-docs` - Type annotations for `boto3` [lex-models](https://pypi.org/project/mypy-boto3-lex-models-with-docs/) service with included documentation.
- `lex-runtime` - Type annotations for `boto3` [lex-runtime](https://pypi.org/project/mypy-boto3-lex-runtime/) service.
- `lex-runtime-with-docs` - Type annotations for `boto3` [lex-runtime](https://pypi.org/project/mypy-boto3-lex-runtime-with-docs/) service with included documentation.
- `license-manager` - Type annotations for `boto3` [license-manager](https://pypi.org/project/mypy-boto3-license-manager/) service.
- `license-manager-with-docs` - Type annotations for `boto3` [license-manager](https://pypi.org/project/mypy-boto3-license-manager-with-docs/) service with included documentation.
- `lightsail` - Type annotations for `boto3` [lightsail](https://pypi.org/project/mypy-boto3-lightsail/) service.
- `lightsail-with-docs` - Type annotations for `boto3` [lightsail](https://pypi.org/project/mypy-boto3-lightsail-with-docs/) service with included documentation.
- `logs` - Type annotations for `boto3` [logs](https://pypi.org/project/mypy-boto3-logs/) service.
- `logs-with-docs` - Type annotations for `boto3` [logs](https://pypi.org/project/mypy-boto3-logs-with-docs/) service with included documentation.
- `machinelearning` - Type annotations for `boto3` [machinelearning](https://pypi.org/project/mypy-boto3-machinelearning/) service.
- `machinelearning-with-docs` - Type annotations for `boto3` [machinelearning](https://pypi.org/project/mypy-boto3-machinelearning-with-docs/) service with included documentation.
- `macie` - Type annotations for `boto3` [macie](https://pypi.org/project/mypy-boto3-macie/) service.
- `macie-with-docs` - Type annotations for `boto3` [macie](https://pypi.org/project/mypy-boto3-macie-with-docs/) service with included documentation.
- `managedblockchain` - Type annotations for `boto3` [managedblockchain](https://pypi.org/project/mypy-boto3-managedblockchain/) service.
- `managedblockchain-with-docs` - Type annotations for `boto3` [managedblockchain](https://pypi.org/project/mypy-boto3-managedblockchain-with-docs/) service with included documentation.
- `marketplace-entitlement` - Type annotations for `boto3` [marketplace-entitlement](https://pypi.org/project/mypy-boto3-marketplace-entitlement/) service.
- `marketplace-entitlement-with-docs` - Type annotations for `boto3` [marketplace-entitlement](https://pypi.org/project/mypy-boto3-marketplace-entitlement-with-docs/) service with included documentation.
- `marketplacecommerceanalytics` - Type annotations for `boto3` [marketplacecommerceanalytics](https://pypi.org/project/mypy-boto3-marketplacecommerceanalytics/) service.
- `marketplacecommerceanalytics-with-docs` - Type annotations for `boto3` [marketplacecommerceanalytics](https://pypi.org/project/mypy-boto3-marketplacecommerceanalytics-with-docs/) service with included documentation.
- `mediaconnect` - Type annotations for `boto3` [mediaconnect](https://pypi.org/project/mypy-boto3-mediaconnect/) service.
- `mediaconnect-with-docs` - Type annotations for `boto3` [mediaconnect](https://pypi.org/project/mypy-boto3-mediaconnect-with-docs/) service with included documentation.
- `mediaconvert` - Type annotations for `boto3` [mediaconvert](https://pypi.org/project/mypy-boto3-mediaconvert/) service.
- `mediaconvert-with-docs` - Type annotations for `boto3` [mediaconvert](https://pypi.org/project/mypy-boto3-mediaconvert-with-docs/) service with included documentation.
- `medialive` - Type annotations for `boto3` [medialive](https://pypi.org/project/mypy-boto3-medialive/) service.
- `medialive-with-docs` - Type annotations for `boto3` [medialive](https://pypi.org/project/mypy-boto3-medialive-with-docs/) service with included documentation.
- `mediapackage` - Type annotations for `boto3` [mediapackage](https://pypi.org/project/mypy-boto3-mediapackage/) service.
- `mediapackage-with-docs` - Type annotations for `boto3` [mediapackage](https://pypi.org/project/mypy-boto3-mediapackage-with-docs/) service with included documentation.
- `mediapackage-vod` - Type annotations for `boto3` [mediapackage-vod](https://pypi.org/project/mypy-boto3-mediapackage-vod/) service.
- `mediapackage-vod-with-docs` - Type annotations for `boto3` [mediapackage-vod](https://pypi.org/project/mypy-boto3-mediapackage-vod-with-docs/) service with included documentation.
- `mediastore` - Type annotations for `boto3` [mediastore](https://pypi.org/project/mypy-boto3-mediastore/) service.
- `mediastore-with-docs` - Type annotations for `boto3` [mediastore](https://pypi.org/project/mypy-boto3-mediastore-with-docs/) service with included documentation.
- `mediastore-data` - Type annotations for `boto3` [mediastore-data](https://pypi.org/project/mypy-boto3-mediastore-data/) service.
- `mediastore-data-with-docs` - Type annotations for `boto3` [mediastore-data](https://pypi.org/project/mypy-boto3-mediastore-data-with-docs/) service with included documentation.
- `mediatailor` - Type annotations for `boto3` [mediatailor](https://pypi.org/project/mypy-boto3-mediatailor/) service.
- `mediatailor-with-docs` - Type annotations for `boto3` [mediatailor](https://pypi.org/project/mypy-boto3-mediatailor-with-docs/) service with included documentation.
- `meteringmarketplace` - Type annotations for `boto3` [meteringmarketplace](https://pypi.org/project/mypy-boto3-meteringmarketplace/) service.
- `meteringmarketplace-with-docs` - Type annotations for `boto3` [meteringmarketplace](https://pypi.org/project/mypy-boto3-meteringmarketplace-with-docs/) service with included documentation.
- `mgh` - Type annotations for `boto3` [mgh](https://pypi.org/project/mypy-boto3-mgh/) service.
- `mgh-with-docs` - Type annotations for `boto3` [mgh](https://pypi.org/project/mypy-boto3-mgh-with-docs/) service with included documentation.
- `mobile` - Type annotations for `boto3` [mobile](https://pypi.org/project/mypy-boto3-mobile/) service.
- `mobile-with-docs` - Type annotations for `boto3` [mobile](https://pypi.org/project/mypy-boto3-mobile-with-docs/) service with included documentation.
- `mq` - Type annotations for `boto3` [mq](https://pypi.org/project/mypy-boto3-mq/) service.
- `mq-with-docs` - Type annotations for `boto3` [mq](https://pypi.org/project/mypy-boto3-mq-with-docs/) service with included documentation.
- `mturk` - Type annotations for `boto3` [mturk](https://pypi.org/project/mypy-boto3-mturk/) service.
- `mturk-with-docs` - Type annotations for `boto3` [mturk](https://pypi.org/project/mypy-boto3-mturk-with-docs/) service with included documentation.
- `neptune` - Type annotations for `boto3` [neptune](https://pypi.org/project/mypy-boto3-neptune/) service.
- `neptune-with-docs` - Type annotations for `boto3` [neptune](https://pypi.org/project/mypy-boto3-neptune-with-docs/) service with included documentation.
- `opsworks` - Type annotations for `boto3` [opsworks](https://pypi.org/project/mypy-boto3-opsworks/) service.
- `opsworks-with-docs` - Type annotations for `boto3` [opsworks](https://pypi.org/project/mypy-boto3-opsworks-with-docs/) service with included documentation.
- `opsworkscm` - Type annotations for `boto3` [opsworkscm](https://pypi.org/project/mypy-boto3-opsworkscm/) service.
- `opsworkscm-with-docs` - Type annotations for `boto3` [opsworkscm](https://pypi.org/project/mypy-boto3-opsworkscm-with-docs/) service with included documentation.
- `organizations` - Type annotations for `boto3` [organizations](https://pypi.org/project/mypy-boto3-organizations/) service.
- `organizations-with-docs` - Type annotations for `boto3` [organizations](https://pypi.org/project/mypy-boto3-organizations-with-docs/) service with included documentation.
- `personalize` - Type annotations for `boto3` [personalize](https://pypi.org/project/mypy-boto3-personalize/) service.
- `personalize-with-docs` - Type annotations for `boto3` [personalize](https://pypi.org/project/mypy-boto3-personalize-with-docs/) service with included documentation.
- `personalize-events` - Type annotations for `boto3` [personalize-events](https://pypi.org/project/mypy-boto3-personalize-events/) service.
- `personalize-events-with-docs` - Type annotations for `boto3` [personalize-events](https://pypi.org/project/mypy-boto3-personalize-events-with-docs/) service with included documentation.
- `personalize-runtime` - Type annotations for `boto3` [personalize-runtime](https://pypi.org/project/mypy-boto3-personalize-runtime/) service.
- `personalize-runtime-with-docs` - Type annotations for `boto3` [personalize-runtime](https://pypi.org/project/mypy-boto3-personalize-runtime-with-docs/) service with included documentation.
- `pi` - Type annotations for `boto3` [pi](https://pypi.org/project/mypy-boto3-pi/) service.
- `pi-with-docs` - Type annotations for `boto3` [pi](https://pypi.org/project/mypy-boto3-pi-with-docs/) service with included documentation.
- `pinpoint` - Type annotations for `boto3` [pinpoint](https://pypi.org/project/mypy-boto3-pinpoint/) service.
- `pinpoint-with-docs` - Type annotations for `boto3` [pinpoint](https://pypi.org/project/mypy-boto3-pinpoint-with-docs/) service with included documentation.
- `pinpoint-email` - Type annotations for `boto3` [pinpoint-email](https://pypi.org/project/mypy-boto3-pinpoint-email/) service.
- `pinpoint-email-with-docs` - Type annotations for `boto3` [pinpoint-email](https://pypi.org/project/mypy-boto3-pinpoint-email-with-docs/) service with included documentation.
- `pinpoint-sms-voice` - Type annotations for `boto3` [pinpoint-sms-voice](https://pypi.org/project/mypy-boto3-pinpoint-sms-voice/) service.
- `pinpoint-sms-voice-with-docs` - Type annotations for `boto3` [pinpoint-sms-voice](https://pypi.org/project/mypy-boto3-pinpoint-sms-voice-with-docs/) service with included documentation.
- `polly` - Type annotations for `boto3` [polly](https://pypi.org/project/mypy-boto3-polly/) service.
- `polly-with-docs` - Type annotations for `boto3` [polly](https://pypi.org/project/mypy-boto3-polly-with-docs/) service with included documentation.
- `pricing` - Type annotations for `boto3` [pricing](https://pypi.org/project/mypy-boto3-pricing/) service.
- `pricing-with-docs` - Type annotations for `boto3` [pricing](https://pypi.org/project/mypy-boto3-pricing-with-docs/) service with included documentation.
- `qldb` - Type annotations for `boto3` [qldb](https://pypi.org/project/mypy-boto3-qldb/) service.
- `qldb-with-docs` - Type annotations for `boto3` [qldb](https://pypi.org/project/mypy-boto3-qldb-with-docs/) service with included documentation.
- `qldb-session` - Type annotations for `boto3` [qldb-session](https://pypi.org/project/mypy-boto3-qldb-session/) service.
- `qldb-session-with-docs` - Type annotations for `boto3` [qldb-session](https://pypi.org/project/mypy-boto3-qldb-session-with-docs/) service with included documentation.
- `quicksight` - Type annotations for `boto3` [quicksight](https://pypi.org/project/mypy-boto3-quicksight/) service.
- `quicksight-with-docs` - Type annotations for `boto3` [quicksight](https://pypi.org/project/mypy-boto3-quicksight-with-docs/) service with included documentation.
- `ram` - Type annotations for `boto3` [ram](https://pypi.org/project/mypy-boto3-ram/) service.
- `ram-with-docs` - Type annotations for `boto3` [ram](https://pypi.org/project/mypy-boto3-ram-with-docs/) service with included documentation.
- `rds` - Type annotations for `boto3` [rds](https://pypi.org/project/mypy-boto3-rds/) service.
- `rds-with-docs` - Type annotations for `boto3` [rds](https://pypi.org/project/mypy-boto3-rds-with-docs/) service with included documentation.
- `rds-data` - Type annotations for `boto3` [rds-data](https://pypi.org/project/mypy-boto3-rds-data/) service.
- `rds-data-with-docs` - Type annotations for `boto3` [rds-data](https://pypi.org/project/mypy-boto3-rds-data-with-docs/) service with included documentation.
- `redshift` - Type annotations for `boto3` [redshift](https://pypi.org/project/mypy-boto3-redshift/) service.
- `redshift-with-docs` - Type annotations for `boto3` [redshift](https://pypi.org/project/mypy-boto3-redshift-with-docs/) service with included documentation.
- `rekognition` - Type annotations for `boto3` [rekognition](https://pypi.org/project/mypy-boto3-rekognition/) service.
- `rekognition-with-docs` - Type annotations for `boto3` [rekognition](https://pypi.org/project/mypy-boto3-rekognition-with-docs/) service with included documentation.
- `resource-groups` - Type annotations for `boto3` [resource-groups](https://pypi.org/project/mypy-boto3-resource-groups/) service.
- `resource-groups-with-docs` - Type annotations for `boto3` [resource-groups](https://pypi.org/project/mypy-boto3-resource-groups-with-docs/) service with included documentation.
- `resourcegroupstaggingapi` - Type annotations for `boto3` [resourcegroupstaggingapi](https://pypi.org/project/mypy-boto3-resourcegroupstaggingapi/) service.
- `resourcegroupstaggingapi-with-docs` - Type annotations for `boto3` [resourcegroupstaggingapi](https://pypi.org/project/mypy-boto3-resourcegroupstaggingapi-with-docs/) service with included documentation.
- `robomaker` - Type annotations for `boto3` [robomaker](https://pypi.org/project/mypy-boto3-robomaker/) service.
- `robomaker-with-docs` - Type annotations for `boto3` [robomaker](https://pypi.org/project/mypy-boto3-robomaker-with-docs/) service with included documentation.
- `route53` - Type annotations for `boto3` [route53](https://pypi.org/project/mypy-boto3-route53/) service.
- `route53-with-docs` - Type annotations for `boto3` [route53](https://pypi.org/project/mypy-boto3-route53-with-docs/) service with included documentation.
- `route53domains` - Type annotations for `boto3` [route53domains](https://pypi.org/project/mypy-boto3-route53domains/) service.
- `route53domains-with-docs` - Type annotations for `boto3` [route53domains](https://pypi.org/project/mypy-boto3-route53domains-with-docs/) service with included documentation.
- `route53resolver` - Type annotations for `boto3` [route53resolver](https://pypi.org/project/mypy-boto3-route53resolver/) service.
- `route53resolver-with-docs` - Type annotations for `boto3` [route53resolver](https://pypi.org/project/mypy-boto3-route53resolver-with-docs/) service with included documentation.
- `s3` - Type annotations for `boto3` [s3](https://pypi.org/project/mypy-boto3-s3/) service.
- `s3-with-docs` - Type annotations for `boto3` [s3](https://pypi.org/project/mypy-boto3-s3-with-docs/) service with included documentation.
- `s3control` - Type annotations for `boto3` [s3control](https://pypi.org/project/mypy-boto3-s3control/) service.
- `s3control-with-docs` - Type annotations for `boto3` [s3control](https://pypi.org/project/mypy-boto3-s3control-with-docs/) service with included documentation.
- `sagemaker` - Type annotations for `boto3` [sagemaker](https://pypi.org/project/mypy-boto3-sagemaker/) service.
- `sagemaker-with-docs` - Type annotations for `boto3` [sagemaker](https://pypi.org/project/mypy-boto3-sagemaker-with-docs/) service with included documentation.
- `sagemaker-runtime` - Type annotations for `boto3` [sagemaker-runtime](https://pypi.org/project/mypy-boto3-sagemaker-runtime/) service.
- `sagemaker-runtime-with-docs` - Type annotations for `boto3` [sagemaker-runtime](https://pypi.org/project/mypy-boto3-sagemaker-runtime-with-docs/) service with included documentation.
- `savingsplans` - Type annotations for `boto3` [savingsplans](https://pypi.org/project/mypy-boto3-savingsplans/) service.
- `savingsplans-with-docs` - Type annotations for `boto3` [savingsplans](https://pypi.org/project/mypy-boto3-savingsplans-with-docs/) service with included documentation.
- `sdb` - Type annotations for `boto3` [sdb](https://pypi.org/project/mypy-boto3-sdb/) service.
- `sdb-with-docs` - Type annotations for `boto3` [sdb](https://pypi.org/project/mypy-boto3-sdb-with-docs/) service with included documentation.
- `secretsmanager` - Type annotations for `boto3` [secretsmanager](https://pypi.org/project/mypy-boto3-secretsmanager/) service.
- `secretsmanager-with-docs` - Type annotations for `boto3` [secretsmanager](https://pypi.org/project/mypy-boto3-secretsmanager-with-docs/) service with included documentation.
- `securityhub` - Type annotations for `boto3` [securityhub](https://pypi.org/project/mypy-boto3-securityhub/) service.
- `securityhub-with-docs` - Type annotations for `boto3` [securityhub](https://pypi.org/project/mypy-boto3-securityhub-with-docs/) service with included documentation.
- `serverlessrepo` - Type annotations for `boto3` [serverlessrepo](https://pypi.org/project/mypy-boto3-serverlessrepo/) service.
- `serverlessrepo-with-docs` - Type annotations for `boto3` [serverlessrepo](https://pypi.org/project/mypy-boto3-serverlessrepo-with-docs/) service with included documentation.
- `service-quotas` - Type annotations for `boto3` [service-quotas](https://pypi.org/project/mypy-boto3-service-quotas/) service.
- `service-quotas-with-docs` - Type annotations for `boto3` [service-quotas](https://pypi.org/project/mypy-boto3-service-quotas-with-docs/) service with included documentation.
- `servicecatalog` - Type annotations for `boto3` [servicecatalog](https://pypi.org/project/mypy-boto3-servicecatalog/) service.
- `servicecatalog-with-docs` - Type annotations for `boto3` [servicecatalog](https://pypi.org/project/mypy-boto3-servicecatalog-with-docs/) service with included documentation.
- `servicediscovery` - Type annotations for `boto3` [servicediscovery](https://pypi.org/project/mypy-boto3-servicediscovery/) service.
- `servicediscovery-with-docs` - Type annotations for `boto3` [servicediscovery](https://pypi.org/project/mypy-boto3-servicediscovery-with-docs/) service with included documentation.
- `ses` - Type annotations for `boto3` [ses](https://pypi.org/project/mypy-boto3-ses/) service.
- `ses-with-docs` - Type annotations for `boto3` [ses](https://pypi.org/project/mypy-boto3-ses-with-docs/) service with included documentation.
- `shield` - Type annotations for `boto3` [shield](https://pypi.org/project/mypy-boto3-shield/) service.
- `shield-with-docs` - Type annotations for `boto3` [shield](https://pypi.org/project/mypy-boto3-shield-with-docs/) service with included documentation.
- `signer` - Type annotations for `boto3` [signer](https://pypi.org/project/mypy-boto3-signer/) service.
- `signer-with-docs` - Type annotations for `boto3` [signer](https://pypi.org/project/mypy-boto3-signer-with-docs/) service with included documentation.
- `sms` - Type annotations for `boto3` [sms](https://pypi.org/project/mypy-boto3-sms/) service.
- `sms-with-docs` - Type annotations for `boto3` [sms](https://pypi.org/project/mypy-boto3-sms-with-docs/) service with included documentation.
- `sms-voice` - Type annotations for `boto3` [sms-voice](https://pypi.org/project/mypy-boto3-sms-voice/) service.
- `sms-voice-with-docs` - Type annotations for `boto3` [sms-voice](https://pypi.org/project/mypy-boto3-sms-voice-with-docs/) service with included documentation.
- `snowball` - Type annotations for `boto3` [snowball](https://pypi.org/project/mypy-boto3-snowball/) service.
- `snowball-with-docs` - Type annotations for `boto3` [snowball](https://pypi.org/project/mypy-boto3-snowball-with-docs/) service with included documentation.
- `sns` - Type annotations for `boto3` [sns](https://pypi.org/project/mypy-boto3-sns/) service.
- `sns-with-docs` - Type annotations for `boto3` [sns](https://pypi.org/project/mypy-boto3-sns-with-docs/) service with included documentation.
- `sqs` - Type annotations for `boto3` [sqs](https://pypi.org/project/mypy-boto3-sqs/) service.
- `sqs-with-docs` - Type annotations for `boto3` [sqs](https://pypi.org/project/mypy-boto3-sqs-with-docs/) service with included documentation.
- `ssm` - Type annotations for `boto3` [ssm](https://pypi.org/project/mypy-boto3-ssm/) service.
- `ssm-with-docs` - Type annotations for `boto3` [ssm](https://pypi.org/project/mypy-boto3-ssm-with-docs/) service with included documentation.
- `stepfunctions` - Type annotations for `boto3` [stepfunctions](https://pypi.org/project/mypy-boto3-stepfunctions/) service.
- `stepfunctions-with-docs` - Type annotations for `boto3` [stepfunctions](https://pypi.org/project/mypy-boto3-stepfunctions-with-docs/) service with included documentation.
- `storagegateway` - Type annotations for `boto3` [storagegateway](https://pypi.org/project/mypy-boto3-storagegateway/) service.
- `storagegateway-with-docs` - Type annotations for `boto3` [storagegateway](https://pypi.org/project/mypy-boto3-storagegateway-with-docs/) service with included documentation.
- `sts` - Type annotations for `boto3` [sts](https://pypi.org/project/mypy-boto3-sts/) service.
- `sts-with-docs` - Type annotations for `boto3` [sts](https://pypi.org/project/mypy-boto3-sts-with-docs/) service with included documentation.
- `support` - Type annotations for `boto3` [support](https://pypi.org/project/mypy-boto3-support/) service.
- `support-with-docs` - Type annotations for `boto3` [support](https://pypi.org/project/mypy-boto3-support-with-docs/) service with included documentation.
- `swf` - Type annotations for `boto3` [swf](https://pypi.org/project/mypy-boto3-swf/) service.
- `swf-with-docs` - Type annotations for `boto3` [swf](https://pypi.org/project/mypy-boto3-swf-with-docs/) service with included documentation.
- `textract` - Type annotations for `boto3` [textract](https://pypi.org/project/mypy-boto3-textract/) service.
- `textract-with-docs` - Type annotations for `boto3` [textract](https://pypi.org/project/mypy-boto3-textract-with-docs/) service with included documentation.
- `transcribe` - Type annotations for `boto3` [transcribe](https://pypi.org/project/mypy-boto3-transcribe/) service.
- `transcribe-with-docs` - Type annotations for `boto3` [transcribe](https://pypi.org/project/mypy-boto3-transcribe-with-docs/) service with included documentation.
- `transfer` - Type annotations for `boto3` [transfer](https://pypi.org/project/mypy-boto3-transfer/) service.
- `transfer-with-docs` - Type annotations for `boto3` [transfer](https://pypi.org/project/mypy-boto3-transfer-with-docs/) service with included documentation.
- `translate` - Type annotations for `boto3` [translate](https://pypi.org/project/mypy-boto3-translate/) service.
- `translate-with-docs` - Type annotations for `boto3` [translate](https://pypi.org/project/mypy-boto3-translate-with-docs/) service with included documentation.
- `waf` - Type annotations for `boto3` [waf](https://pypi.org/project/mypy-boto3-waf/) service.
- `waf-with-docs` - Type annotations for `boto3` [waf](https://pypi.org/project/mypy-boto3-waf-with-docs/) service with included documentation.
- `waf-regional` - Type annotations for `boto3` [waf-regional](https://pypi.org/project/mypy-boto3-waf-regional/) service.
- `waf-regional-with-docs` - Type annotations for `boto3` [waf-regional](https://pypi.org/project/mypy-boto3-waf-regional-with-docs/) service with included documentation.
- `workdocs` - Type annotations for `boto3` [workdocs](https://pypi.org/project/mypy-boto3-workdocs/) service.
- `workdocs-with-docs` - Type annotations for `boto3` [workdocs](https://pypi.org/project/mypy-boto3-workdocs-with-docs/) service with included documentation.
- `worklink` - Type annotations for `boto3` [worklink](https://pypi.org/project/mypy-boto3-worklink/) service.
- `worklink-with-docs` - Type annotations for `boto3` [worklink](https://pypi.org/project/mypy-boto3-worklink-with-docs/) service with included documentation.
- `workmail` - Type annotations for `boto3` [workmail](https://pypi.org/project/mypy-boto3-workmail/) service.
- `workmail-with-docs` - Type annotations for `boto3` [workmail](https://pypi.org/project/mypy-boto3-workmail-with-docs/) service with included documentation.
- `workmailmessageflow` - Type annotations for `boto3` [workmailmessageflow](https://pypi.org/project/mypy-boto3-workmailmessageflow/) service.
- `workmailmessageflow-with-docs` - Type annotations for `boto3` [workmailmessageflow](https://pypi.org/project/mypy-boto3-workmailmessageflow-with-docs/) service with included documentation.
- `workspaces` - Type annotations for `boto3` [workspaces](https://pypi.org/project/mypy-boto3-workspaces/) service.
- `workspaces-with-docs` - Type annotations for `boto3` [workspaces](https://pypi.org/project/mypy-boto3-workspaces-with-docs/) service with included documentation.
- `xray` - Type annotations for `boto3` [xray](https://pypi.org/project/mypy-boto3-xray/) service.
- `xray-with-docs` - Type annotations for `boto3` [xray](https://pypi.org/project/mypy-boto3-xray-with-docs/) service with included documentation.

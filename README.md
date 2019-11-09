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
  - [List of supported boto3 services](#list-of-supported-boto3-services)

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
- Use `mypy-boto3` to annotate your code to discover errors

```python
import boto3

from mypy_boto3.s3 import Client, ServiceResource

client: Client = boto3.client("s3")

# IDE autocomplete suggests function name and arguments here
client.create_bucket(Bucket="bucket")

# (mypy) error: Missing positional argument "Key" in call to "get_object" of "Client"
client.get_object(Bucket="bucket")

# (mypy) error: Argument "Key" to "get_object" of "Client" has incompatible type "None"; expected "str"
client.get_object(Bucket="bucket", Key=None)

# explicitly set type to S3 ServiceResource
resource: ServiceResource = boto3.Session(region_name="us-west-1").resource("s3")

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


## List of supported boto3 services

- [acm](https://pypi.org/project/mypy-boto3-acm/): `pip install mypy-boto3[acm]`
- [acm-pca](https://pypi.org/project/mypy-boto3-acm-pca/): `pip install mypy-boto3[acm-pca]`
- [alexaforbusiness](https://pypi.org/project/mypy-boto3-alexaforbusiness/): `pip install mypy-boto3[alexaforbusiness]`
- [amplify](https://pypi.org/project/mypy-boto3-amplify/): `pip install mypy-boto3[amplify]`
- [apigateway](https://pypi.org/project/mypy-boto3-apigateway/): `pip install mypy-boto3[apigateway]`
- [apigatewaymanagementapi](https://pypi.org/project/mypy-boto3-apigatewaymanagementapi/): `pip install mypy-boto3[apigatewaymanagementapi]`
- [apigatewayv2](https://pypi.org/project/mypy-boto3-apigatewayv2/): `pip install mypy-boto3[apigatewayv2]`
- [application-autoscaling](https://pypi.org/project/mypy-boto3-application-autoscaling/): `pip install mypy-boto3[application-autoscaling]`
- [application-insights](https://pypi.org/project/mypy-boto3-application-insights/): `pip install mypy-boto3[application-insights]`
- [appmesh](https://pypi.org/project/mypy-boto3-appmesh/): `pip install mypy-boto3[appmesh]`
- [appstream](https://pypi.org/project/mypy-boto3-appstream/): `pip install mypy-boto3[appstream]`
- [appsync](https://pypi.org/project/mypy-boto3-appsync/): `pip install mypy-boto3[appsync]`
- [athena](https://pypi.org/project/mypy-boto3-athena/): `pip install mypy-boto3[athena]`
- [autoscaling](https://pypi.org/project/mypy-boto3-autoscaling/): `pip install mypy-boto3[autoscaling]`
- [autoscaling-plans](https://pypi.org/project/mypy-boto3-autoscaling-plans/): `pip install mypy-boto3[autoscaling-plans]`
- [backup](https://pypi.org/project/mypy-boto3-backup/): `pip install mypy-boto3[backup]`
- [batch](https://pypi.org/project/mypy-boto3-batch/): `pip install mypy-boto3[batch]`
- [budgets](https://pypi.org/project/mypy-boto3-budgets/): `pip install mypy-boto3[budgets]`
- [ce](https://pypi.org/project/mypy-boto3-ce/): `pip install mypy-boto3[ce]`
- [chime](https://pypi.org/project/mypy-boto3-chime/): `pip install mypy-boto3[chime]`
- [cloud9](https://pypi.org/project/mypy-boto3-cloud9/): `pip install mypy-boto3[cloud9]`
- [clouddirectory](https://pypi.org/project/mypy-boto3-clouddirectory/): `pip install mypy-boto3[clouddirectory]`
- [cloudformation](https://pypi.org/project/mypy-boto3-cloudformation/): `pip install mypy-boto3[cloudformation]`
- [cloudfront](https://pypi.org/project/mypy-boto3-cloudfront/): `pip install mypy-boto3[cloudfront]`
- [cloudhsm](https://pypi.org/project/mypy-boto3-cloudhsm/): `pip install mypy-boto3[cloudhsm]`
- [cloudhsmv2](https://pypi.org/project/mypy-boto3-cloudhsmv2/): `pip install mypy-boto3[cloudhsmv2]`
- [cloudsearch](https://pypi.org/project/mypy-boto3-cloudsearch/): `pip install mypy-boto3[cloudsearch]`
- [cloudsearchdomain](https://pypi.org/project/mypy-boto3-cloudsearchdomain/): `pip install mypy-boto3[cloudsearchdomain]`
- [cloudtrail](https://pypi.org/project/mypy-boto3-cloudtrail/): `pip install mypy-boto3[cloudtrail]`
- [cloudwatch](https://pypi.org/project/mypy-boto3-cloudwatch/): `pip install mypy-boto3[cloudwatch]`
- [codebuild](https://pypi.org/project/mypy-boto3-codebuild/): `pip install mypy-boto3[codebuild]`
- [codecommit](https://pypi.org/project/mypy-boto3-codecommit/): `pip install mypy-boto3[codecommit]`
- [codedeploy](https://pypi.org/project/mypy-boto3-codedeploy/): `pip install mypy-boto3[codedeploy]`
- [codepipeline](https://pypi.org/project/mypy-boto3-codepipeline/): `pip install mypy-boto3[codepipeline]`
- [codestar](https://pypi.org/project/mypy-boto3-codestar/): `pip install mypy-boto3[codestar]`
- [codestar-notifications](https://pypi.org/project/mypy-boto3-codestar-notifications/): `pip install mypy-boto3[codestar-notifications]`
- [cognito-identity](https://pypi.org/project/mypy-boto3-cognito-identity/): `pip install mypy-boto3[cognito-identity]`
- [cognito-idp](https://pypi.org/project/mypy-boto3-cognito-idp/): `pip install mypy-boto3[cognito-idp]`
- [cognito-sync](https://pypi.org/project/mypy-boto3-cognito-sync/): `pip install mypy-boto3[cognito-sync]`
- [comprehend](https://pypi.org/project/mypy-boto3-comprehend/): `pip install mypy-boto3[comprehend]`
- [comprehendmedical](https://pypi.org/project/mypy-boto3-comprehendmedical/): `pip install mypy-boto3[comprehendmedical]`
- [config](https://pypi.org/project/mypy-boto3-config/): `pip install mypy-boto3[config]`
- [connect](https://pypi.org/project/mypy-boto3-connect/): `pip install mypy-boto3[connect]`
- [cur](https://pypi.org/project/mypy-boto3-cur/): `pip install mypy-boto3[cur]`
- [datapipeline](https://pypi.org/project/mypy-boto3-datapipeline/): `pip install mypy-boto3[datapipeline]`
- [datasync](https://pypi.org/project/mypy-boto3-datasync/): `pip install mypy-boto3[datasync]`
- [dax](https://pypi.org/project/mypy-boto3-dax/): `pip install mypy-boto3[dax]`
- [devicefarm](https://pypi.org/project/mypy-boto3-devicefarm/): `pip install mypy-boto3[devicefarm]`
- [directconnect](https://pypi.org/project/mypy-boto3-directconnect/): `pip install mypy-boto3[directconnect]`
- [discovery](https://pypi.org/project/mypy-boto3-discovery/): `pip install mypy-boto3[discovery]`
- [dlm](https://pypi.org/project/mypy-boto3-dlm/): `pip install mypy-boto3[dlm]`
- [dms](https://pypi.org/project/mypy-boto3-dms/): `pip install mypy-boto3[dms]`
- [docdb](https://pypi.org/project/mypy-boto3-docdb/): `pip install mypy-boto3[docdb]`
- [ds](https://pypi.org/project/mypy-boto3-ds/): `pip install mypy-boto3[ds]`
- [dynamodb](https://pypi.org/project/mypy-boto3-dynamodb/): `pip install mypy-boto3[dynamodb]`
- [dynamodbstreams](https://pypi.org/project/mypy-boto3-dynamodbstreams/): `pip install mypy-boto3[dynamodbstreams]`
- [ec2](https://pypi.org/project/mypy-boto3-ec2/): `pip install mypy-boto3[ec2]`
- [ec2-instance-connect](https://pypi.org/project/mypy-boto3-ec2-instance-connect/): `pip install mypy-boto3[ec2-instance-connect]`
- [ecr](https://pypi.org/project/mypy-boto3-ecr/): `pip install mypy-boto3[ecr]`
- [ecs](https://pypi.org/project/mypy-boto3-ecs/): `pip install mypy-boto3[ecs]`
- [efs](https://pypi.org/project/mypy-boto3-efs/): `pip install mypy-boto3[efs]`
- [eks](https://pypi.org/project/mypy-boto3-eks/): `pip install mypy-boto3[eks]`
- [elasticache](https://pypi.org/project/mypy-boto3-elasticache/): `pip install mypy-boto3[elasticache]`
- [elasticbeanstalk](https://pypi.org/project/mypy-boto3-elasticbeanstalk/): `pip install mypy-boto3[elasticbeanstalk]`
- [elastictranscoder](https://pypi.org/project/mypy-boto3-elastictranscoder/): `pip install mypy-boto3[elastictranscoder]`
- [elb](https://pypi.org/project/mypy-boto3-elb/): `pip install mypy-boto3[elb]`
- [elbv2](https://pypi.org/project/mypy-boto3-elbv2/): `pip install mypy-boto3[elbv2]`
- [emr](https://pypi.org/project/mypy-boto3-emr/): `pip install mypy-boto3[emr]`
- [es](https://pypi.org/project/mypy-boto3-es/): `pip install mypy-boto3[es]`
- [events](https://pypi.org/project/mypy-boto3-events/): `pip install mypy-boto3[events]`
- [firehose](https://pypi.org/project/mypy-boto3-firehose/): `pip install mypy-boto3[firehose]`
- [fms](https://pypi.org/project/mypy-boto3-fms/): `pip install mypy-boto3[fms]`
- [forecast](https://pypi.org/project/mypy-boto3-forecast/): `pip install mypy-boto3[forecast]`
- [forecastquery](https://pypi.org/project/mypy-boto3-forecastquery/): `pip install mypy-boto3[forecastquery]`
- [fsx](https://pypi.org/project/mypy-boto3-fsx/): `pip install mypy-boto3[fsx]`
- [gamelift](https://pypi.org/project/mypy-boto3-gamelift/): `pip install mypy-boto3[gamelift]`
- [glacier](https://pypi.org/project/mypy-boto3-glacier/): `pip install mypy-boto3[glacier]`
- [globalaccelerator](https://pypi.org/project/mypy-boto3-globalaccelerator/): `pip install mypy-boto3[globalaccelerator]`
- [glue](https://pypi.org/project/mypy-boto3-glue/): `pip install mypy-boto3[glue]`
- [greengrass](https://pypi.org/project/mypy-boto3-greengrass/): `pip install mypy-boto3[greengrass]`
- [groundstation](https://pypi.org/project/mypy-boto3-groundstation/): `pip install mypy-boto3[groundstation]`
- [guardduty](https://pypi.org/project/mypy-boto3-guardduty/): `pip install mypy-boto3[guardduty]`
- [health](https://pypi.org/project/mypy-boto3-health/): `pip install mypy-boto3[health]`
- [iam](https://pypi.org/project/mypy-boto3-iam/): `pip install mypy-boto3[iam]`
- [importexport](https://pypi.org/project/mypy-boto3-importexport/): `pip install mypy-boto3[importexport]`
- [inspector](https://pypi.org/project/mypy-boto3-inspector/): `pip install mypy-boto3[inspector]`
- [iot](https://pypi.org/project/mypy-boto3-iot/): `pip install mypy-boto3[iot]`
- [iot-data](https://pypi.org/project/mypy-boto3-iot-data/): `pip install mypy-boto3[iot-data]`
- [iot-jobs-data](https://pypi.org/project/mypy-boto3-iot-jobs-data/): `pip install mypy-boto3[iot-jobs-data]`
- [iot1click-devices](https://pypi.org/project/mypy-boto3-iot1click-devices/): `pip install mypy-boto3[iot1click-devices]`
- [iot1click-projects](https://pypi.org/project/mypy-boto3-iot1click-projects/): `pip install mypy-boto3[iot1click-projects]`
- [iotanalytics](https://pypi.org/project/mypy-boto3-iotanalytics/): `pip install mypy-boto3[iotanalytics]`
- [iotevents](https://pypi.org/project/mypy-boto3-iotevents/): `pip install mypy-boto3[iotevents]`
- [iotevents-data](https://pypi.org/project/mypy-boto3-iotevents-data/): `pip install mypy-boto3[iotevents-data]`
- [iotthingsgraph](https://pypi.org/project/mypy-boto3-iotthingsgraph/): `pip install mypy-boto3[iotthingsgraph]`
- [kafka](https://pypi.org/project/mypy-boto3-kafka/): `pip install mypy-boto3[kafka]`
- [kinesis](https://pypi.org/project/mypy-boto3-kinesis/): `pip install mypy-boto3[kinesis]`
- [kinesis-video-archived-media](https://pypi.org/project/mypy-boto3-kinesis-video-archived-media/): `pip install mypy-boto3[kinesis-video-archived-media]`
- [kinesis-video-media](https://pypi.org/project/mypy-boto3-kinesis-video-media/): `pip install mypy-boto3[kinesis-video-media]`
- [kinesisanalytics](https://pypi.org/project/mypy-boto3-kinesisanalytics/): `pip install mypy-boto3[kinesisanalytics]`
- [kinesisanalyticsv2](https://pypi.org/project/mypy-boto3-kinesisanalyticsv2/): `pip install mypy-boto3[kinesisanalyticsv2]`
- [kinesisvideo](https://pypi.org/project/mypy-boto3-kinesisvideo/): `pip install mypy-boto3[kinesisvideo]`
- [kms](https://pypi.org/project/mypy-boto3-kms/): `pip install mypy-boto3[kms]`
- [lakeformation](https://pypi.org/project/mypy-boto3-lakeformation/): `pip install mypy-boto3[lakeformation]`
- [lambda](https://pypi.org/project/mypy-boto3-lambda/): `pip install mypy-boto3[lambda]`
- [lex-models](https://pypi.org/project/mypy-boto3-lex-models/): `pip install mypy-boto3[lex-models]`
- [lex-runtime](https://pypi.org/project/mypy-boto3-lex-runtime/): `pip install mypy-boto3[lex-runtime]`
- [license-manager](https://pypi.org/project/mypy-boto3-license-manager/): `pip install mypy-boto3[license-manager]`
- [lightsail](https://pypi.org/project/mypy-boto3-lightsail/): `pip install mypy-boto3[lightsail]`
- [logs](https://pypi.org/project/mypy-boto3-logs/): `pip install mypy-boto3[logs]`
- [machinelearning](https://pypi.org/project/mypy-boto3-machinelearning/): `pip install mypy-boto3[machinelearning]`
- [macie](https://pypi.org/project/mypy-boto3-macie/): `pip install mypy-boto3[macie]`
- [managedblockchain](https://pypi.org/project/mypy-boto3-managedblockchain/): `pip install mypy-boto3[managedblockchain]`
- [marketplace-entitlement](https://pypi.org/project/mypy-boto3-marketplace-entitlement/): `pip install mypy-boto3[marketplace-entitlement]`
- [marketplacecommerceanalytics](https://pypi.org/project/mypy-boto3-marketplacecommerceanalytics/): `pip install mypy-boto3[marketplacecommerceanalytics]`
- [mediaconnect](https://pypi.org/project/mypy-boto3-mediaconnect/): `pip install mypy-boto3[mediaconnect]`
- [mediaconvert](https://pypi.org/project/mypy-boto3-mediaconvert/): `pip install mypy-boto3[mediaconvert]`
- [medialive](https://pypi.org/project/mypy-boto3-medialive/): `pip install mypy-boto3[medialive]`
- [mediapackage](https://pypi.org/project/mypy-boto3-mediapackage/): `pip install mypy-boto3[mediapackage]`
- [mediapackage-vod](https://pypi.org/project/mypy-boto3-mediapackage-vod/): `pip install mypy-boto3[mediapackage-vod]`
- [mediastore](https://pypi.org/project/mypy-boto3-mediastore/): `pip install mypy-boto3[mediastore]`
- [mediastore-data](https://pypi.org/project/mypy-boto3-mediastore-data/): `pip install mypy-boto3[mediastore-data]`
- [mediatailor](https://pypi.org/project/mypy-boto3-mediatailor/): `pip install mypy-boto3[mediatailor]`
- [meteringmarketplace](https://pypi.org/project/mypy-boto3-meteringmarketplace/): `pip install mypy-boto3[meteringmarketplace]`
- [mgh](https://pypi.org/project/mypy-boto3-mgh/): `pip install mypy-boto3[mgh]`
- [mobile](https://pypi.org/project/mypy-boto3-mobile/): `pip install mypy-boto3[mobile]`
- [mq](https://pypi.org/project/mypy-boto3-mq/): `pip install mypy-boto3[mq]`
- [mturk](https://pypi.org/project/mypy-boto3-mturk/): `pip install mypy-boto3[mturk]`
- [neptune](https://pypi.org/project/mypy-boto3-neptune/): `pip install mypy-boto3[neptune]`
- [opsworks](https://pypi.org/project/mypy-boto3-opsworks/): `pip install mypy-boto3[opsworks]`
- [opsworkscm](https://pypi.org/project/mypy-boto3-opsworkscm/): `pip install mypy-boto3[opsworkscm]`
- [organizations](https://pypi.org/project/mypy-boto3-organizations/): `pip install mypy-boto3[organizations]`
- [personalize](https://pypi.org/project/mypy-boto3-personalize/): `pip install mypy-boto3[personalize]`
- [personalize-events](https://pypi.org/project/mypy-boto3-personalize-events/): `pip install mypy-boto3[personalize-events]`
- [personalize-runtime](https://pypi.org/project/mypy-boto3-personalize-runtime/): `pip install mypy-boto3[personalize-runtime]`
- [pi](https://pypi.org/project/mypy-boto3-pi/): `pip install mypy-boto3[pi]`
- [pinpoint](https://pypi.org/project/mypy-boto3-pinpoint/): `pip install mypy-boto3[pinpoint]`
- [pinpoint-email](https://pypi.org/project/mypy-boto3-pinpoint-email/): `pip install mypy-boto3[pinpoint-email]`
- [pinpoint-sms-voice](https://pypi.org/project/mypy-boto3-pinpoint-sms-voice/): `pip install mypy-boto3[pinpoint-sms-voice]`
- [polly](https://pypi.org/project/mypy-boto3-polly/): `pip install mypy-boto3[polly]`
- [pricing](https://pypi.org/project/mypy-boto3-pricing/): `pip install mypy-boto3[pricing]`
- [qldb](https://pypi.org/project/mypy-boto3-qldb/): `pip install mypy-boto3[qldb]`
- [qldb-session](https://pypi.org/project/mypy-boto3-qldb-session/): `pip install mypy-boto3[qldb-session]`
- [quicksight](https://pypi.org/project/mypy-boto3-quicksight/): `pip install mypy-boto3[quicksight]`
- [ram](https://pypi.org/project/mypy-boto3-ram/): `pip install mypy-boto3[ram]`
- [rds](https://pypi.org/project/mypy-boto3-rds/): `pip install mypy-boto3[rds]`
- [rds-data](https://pypi.org/project/mypy-boto3-rds-data/): `pip install mypy-boto3[rds-data]`
- [redshift](https://pypi.org/project/mypy-boto3-redshift/): `pip install mypy-boto3[redshift]`
- [rekognition](https://pypi.org/project/mypy-boto3-rekognition/): `pip install mypy-boto3[rekognition]`
- [resource-groups](https://pypi.org/project/mypy-boto3-resource-groups/): `pip install mypy-boto3[resource-groups]`
- [resourcegroupstaggingapi](https://pypi.org/project/mypy-boto3-resourcegroupstaggingapi/): `pip install mypy-boto3[resourcegroupstaggingapi]`
- [robomaker](https://pypi.org/project/mypy-boto3-robomaker/): `pip install mypy-boto3[robomaker]`
- [route53](https://pypi.org/project/mypy-boto3-route53/): `pip install mypy-boto3[route53]`
- [route53domains](https://pypi.org/project/mypy-boto3-route53domains/): `pip install mypy-boto3[route53domains]`
- [route53resolver](https://pypi.org/project/mypy-boto3-route53resolver/): `pip install mypy-boto3[route53resolver]`
- [s3](https://pypi.org/project/mypy-boto3-s3/): `pip install mypy-boto3[s3]`
- [s3control](https://pypi.org/project/mypy-boto3-s3control/): `pip install mypy-boto3[s3control]`
- [sagemaker](https://pypi.org/project/mypy-boto3-sagemaker/): `pip install mypy-boto3[sagemaker]`
- [sagemaker-runtime](https://pypi.org/project/mypy-boto3-sagemaker-runtime/): `pip install mypy-boto3[sagemaker-runtime]`
- [savingsplans](https://pypi.org/project/mypy-boto3-savingsplans/): `pip install mypy-boto3[savingsplans]`
- [sdb](https://pypi.org/project/mypy-boto3-sdb/): `pip install mypy-boto3[sdb]`
- [secretsmanager](https://pypi.org/project/mypy-boto3-secretsmanager/): `pip install mypy-boto3[secretsmanager]`
- [securityhub](https://pypi.org/project/mypy-boto3-securityhub/): `pip install mypy-boto3[securityhub]`
- [serverlessrepo](https://pypi.org/project/mypy-boto3-serverlessrepo/): `pip install mypy-boto3[serverlessrepo]`
- [service-quotas](https://pypi.org/project/mypy-boto3-service-quotas/): `pip install mypy-boto3[service-quotas]`
- [servicecatalog](https://pypi.org/project/mypy-boto3-servicecatalog/): `pip install mypy-boto3[servicecatalog]`
- [servicediscovery](https://pypi.org/project/mypy-boto3-servicediscovery/): `pip install mypy-boto3[servicediscovery]`
- [ses](https://pypi.org/project/mypy-boto3-ses/): `pip install mypy-boto3[ses]`
- [shield](https://pypi.org/project/mypy-boto3-shield/): `pip install mypy-boto3[shield]`
- [signer](https://pypi.org/project/mypy-boto3-signer/): `pip install mypy-boto3[signer]`
- [sms](https://pypi.org/project/mypy-boto3-sms/): `pip install mypy-boto3[sms]`
- [sms-voice](https://pypi.org/project/mypy-boto3-sms-voice/): `pip install mypy-boto3[sms-voice]`
- [snowball](https://pypi.org/project/mypy-boto3-snowball/): `pip install mypy-boto3[snowball]`
- [sns](https://pypi.org/project/mypy-boto3-sns/): `pip install mypy-boto3[sns]`
- [sqs](https://pypi.org/project/mypy-boto3-sqs/): `pip install mypy-boto3[sqs]`
- [ssm](https://pypi.org/project/mypy-boto3-ssm/): `pip install mypy-boto3[ssm]`
- [stepfunctions](https://pypi.org/project/mypy-boto3-stepfunctions/): `pip install mypy-boto3[stepfunctions]`
- [storagegateway](https://pypi.org/project/mypy-boto3-storagegateway/): `pip install mypy-boto3[storagegateway]`
- [sts](https://pypi.org/project/mypy-boto3-sts/): `pip install mypy-boto3[sts]`
- [support](https://pypi.org/project/mypy-boto3-support/): `pip install mypy-boto3[support]`
- [swf](https://pypi.org/project/mypy-boto3-swf/): `pip install mypy-boto3[swf]`
- [textract](https://pypi.org/project/mypy-boto3-textract/): `pip install mypy-boto3[textract]`
- [transcribe](https://pypi.org/project/mypy-boto3-transcribe/): `pip install mypy-boto3[transcribe]`
- [transfer](https://pypi.org/project/mypy-boto3-transfer/): `pip install mypy-boto3[transfer]`
- [translate](https://pypi.org/project/mypy-boto3-translate/): `pip install mypy-boto3[translate]`
- [waf](https://pypi.org/project/mypy-boto3-waf/): `pip install mypy-boto3[waf]`
- [waf-regional](https://pypi.org/project/mypy-boto3-waf-regional/): `pip install mypy-boto3[waf-regional]`
- [workdocs](https://pypi.org/project/mypy-boto3-workdocs/): `pip install mypy-boto3[workdocs]`
- [worklink](https://pypi.org/project/mypy-boto3-worklink/): `pip install mypy-boto3[worklink]`
- [workmail](https://pypi.org/project/mypy-boto3-workmail/): `pip install mypy-boto3[workmail]`
- [workmailmessageflow](https://pypi.org/project/mypy-boto3-workmailmessageflow/): `pip install mypy-boto3[workmailmessageflow]`
- [workspaces](https://pypi.org/project/mypy-boto3-workspaces/): `pip install mypy-boto3[workspaces]`
- [xray](https://pypi.org/project/mypy-boto3-xray/): `pip install mypy-boto3[xray]`

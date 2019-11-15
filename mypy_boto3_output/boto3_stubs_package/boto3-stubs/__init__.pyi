# pylint: disable=unused-argument,multiple-statements
import logging
from typing import Optional, Any, overload, Union
from typing_extensions import Literal

from boto3.session import Session
from botocore.client import Client
from botocore.service_resource import ServiceResource

try:
    from mypy_boto3.acm.client import Client as ACMClient
except ImportError:
    ACMClient = Any

try:
    from mypy_boto3.acm_pca.client import Client as AcmPcaClient
except ImportError:
    AcmPcaClient = Any

try:
    from mypy_boto3.alexaforbusiness.client import Client as AlexaforbusinessClient
except ImportError:
    AlexaforbusinessClient = Any

try:
    from mypy_boto3.amplify.client import Client as AmplifyClient
except ImportError:
    AmplifyClient = Any

try:
    from mypy_boto3.apigateway.client import Client as ApigatewayClient
except ImportError:
    ApigatewayClient = Any

try:
    from mypy_boto3.apigatewaymanagementapi.client import Client as ApigatewaymanagementapiClient
except ImportError:
    ApigatewaymanagementapiClient = Any

try:
    from mypy_boto3.apigatewayv2.client import Client as Apigatewayv2Client
except ImportError:
    Apigatewayv2Client = Any

try:
    from mypy_boto3.application_autoscaling.client import Client as ApplicationAutoscalingClient
except ImportError:
    ApplicationAutoscalingClient = Any

try:
    from mypy_boto3.application_insights.client import Client as ApplicationInsightsClient
except ImportError:
    ApplicationInsightsClient = Any

try:
    from mypy_boto3.appmesh.client import Client as AppmeshClient
except ImportError:
    AppmeshClient = Any

try:
    from mypy_boto3.appstream.client import Client as AppstreamClient
except ImportError:
    AppstreamClient = Any

try:
    from mypy_boto3.appsync.client import Client as AppsyncClient
except ImportError:
    AppsyncClient = Any

try:
    from mypy_boto3.athena.client import Client as AthenaClient
except ImportError:
    AthenaClient = Any

try:
    from mypy_boto3.autoscaling.client import Client as AutoscalingClient
except ImportError:
    AutoscalingClient = Any

try:
    from mypy_boto3.autoscaling_plans.client import Client as AutoscalingPlansClient
except ImportError:
    AutoscalingPlansClient = Any

try:
    from mypy_boto3.backup.client import Client as BackupClient
except ImportError:
    BackupClient = Any

try:
    from mypy_boto3.batch.client import Client as BatchClient
except ImportError:
    BatchClient = Any

try:
    from mypy_boto3.budgets.client import Client as BudgetsClient
except ImportError:
    BudgetsClient = Any

try:
    from mypy_boto3.ce.client import Client as CEClient
except ImportError:
    CEClient = Any

try:
    from mypy_boto3.chime.client import Client as ChimeClient
except ImportError:
    ChimeClient = Any

try:
    from mypy_boto3.cloud9.client import Client as Cloud9Client
except ImportError:
    Cloud9Client = Any

try:
    from mypy_boto3.clouddirectory.client import Client as ClouddirectoryClient
except ImportError:
    ClouddirectoryClient = Any

try:
    from mypy_boto3.cloudformation.client import Client as CloudformationClient
except ImportError:
    CloudformationClient = Any
try:
    from mypy_boto3.cloudformation.service_resource import ServiceResource as CloudformationServiceResource
except ImportError:
    CloudformationServiceResource = Any

try:
    from mypy_boto3.cloudfront.client import Client as CloudfrontClient
except ImportError:
    CloudfrontClient = Any

try:
    from mypy_boto3.cloudhsm.client import Client as CloudhsmClient
except ImportError:
    CloudhsmClient = Any

try:
    from mypy_boto3.cloudhsmv2.client import Client as Cloudhsmv2Client
except ImportError:
    Cloudhsmv2Client = Any

try:
    from mypy_boto3.cloudsearch.client import Client as CloudsearchClient
except ImportError:
    CloudsearchClient = Any

try:
    from mypy_boto3.cloudsearchdomain.client import Client as CloudsearchdomainClient
except ImportError:
    CloudsearchdomainClient = Any

try:
    from mypy_boto3.cloudtrail.client import Client as CloudtrailClient
except ImportError:
    CloudtrailClient = Any

try:
    from mypy_boto3.cloudwatch.client import Client as CloudwatchClient
except ImportError:
    CloudwatchClient = Any
try:
    from mypy_boto3.cloudwatch.service_resource import ServiceResource as CloudwatchServiceResource
except ImportError:
    CloudwatchServiceResource = Any

try:
    from mypy_boto3.codebuild.client import Client as CodebuildClient
except ImportError:
    CodebuildClient = Any

try:
    from mypy_boto3.codecommit.client import Client as CodecommitClient
except ImportError:
    CodecommitClient = Any

try:
    from mypy_boto3.codedeploy.client import Client as CodedeployClient
except ImportError:
    CodedeployClient = Any

try:
    from mypy_boto3.codepipeline.client import Client as CodepipelineClient
except ImportError:
    CodepipelineClient = Any

try:
    from mypy_boto3.codestar.client import Client as CodestarClient
except ImportError:
    CodestarClient = Any

try:
    from mypy_boto3.codestar_notifications.client import Client as CodestarNotificationsClient
except ImportError:
    CodestarNotificationsClient = Any

try:
    from mypy_boto3.cognito_identity.client import Client as CognitoIdentityClient
except ImportError:
    CognitoIdentityClient = Any

try:
    from mypy_boto3.cognito_idp.client import Client as CognitoIdpClient
except ImportError:
    CognitoIdpClient = Any

try:
    from mypy_boto3.cognito_sync.client import Client as CognitoSyncClient
except ImportError:
    CognitoSyncClient = Any

try:
    from mypy_boto3.comprehend.client import Client as ComprehendClient
except ImportError:
    ComprehendClient = Any

try:
    from mypy_boto3.comprehendmedical.client import Client as ComprehendmedicalClient
except ImportError:
    ComprehendmedicalClient = Any

try:
    from mypy_boto3.config.client import Client as ConfigClient
except ImportError:
    ConfigClient = Any

try:
    from mypy_boto3.connect.client import Client as ConnectClient
except ImportError:
    ConnectClient = Any

try:
    from mypy_boto3.cur.client import Client as CURClient
except ImportError:
    CURClient = Any

try:
    from mypy_boto3.datapipeline.client import Client as DatapipelineClient
except ImportError:
    DatapipelineClient = Any

try:
    from mypy_boto3.datasync.client import Client as DatasyncClient
except ImportError:
    DatasyncClient = Any

try:
    from mypy_boto3.dax.client import Client as DAXClient
except ImportError:
    DAXClient = Any

try:
    from mypy_boto3.devicefarm.client import Client as DevicefarmClient
except ImportError:
    DevicefarmClient = Any

try:
    from mypy_boto3.directconnect.client import Client as DirectconnectClient
except ImportError:
    DirectconnectClient = Any

try:
    from mypy_boto3.discovery.client import Client as DiscoveryClient
except ImportError:
    DiscoveryClient = Any

try:
    from mypy_boto3.dlm.client import Client as DLMClient
except ImportError:
    DLMClient = Any

try:
    from mypy_boto3.dms.client import Client as DMSClient
except ImportError:
    DMSClient = Any

try:
    from mypy_boto3.docdb.client import Client as DocdbClient
except ImportError:
    DocdbClient = Any

try:
    from mypy_boto3.ds.client import Client as DSClient
except ImportError:
    DSClient = Any

try:
    from mypy_boto3.dynamodb.client import Client as DynamodbClient
except ImportError:
    DynamodbClient = Any
try:
    from mypy_boto3.dynamodb.service_resource import ServiceResource as DynamodbServiceResource
except ImportError:
    DynamodbServiceResource = Any

try:
    from mypy_boto3.dynamodbstreams.client import Client as DynamodbstreamsClient
except ImportError:
    DynamodbstreamsClient = Any

try:
    from mypy_boto3.ec2.client import Client as EC2Client
except ImportError:
    EC2Client = Any
try:
    from mypy_boto3.ec2.service_resource import ServiceResource as EC2ServiceResource
except ImportError:
    EC2ServiceResource = Any

try:
    from mypy_boto3.ec2_instance_connect.client import Client as Ec2InstanceConnectClient
except ImportError:
    Ec2InstanceConnectClient = Any

try:
    from mypy_boto3.ecr.client import Client as ECRClient
except ImportError:
    ECRClient = Any

try:
    from mypy_boto3.ecs.client import Client as ECSClient
except ImportError:
    ECSClient = Any

try:
    from mypy_boto3.efs.client import Client as EFSClient
except ImportError:
    EFSClient = Any

try:
    from mypy_boto3.eks.client import Client as EKSClient
except ImportError:
    EKSClient = Any

try:
    from mypy_boto3.elasticache.client import Client as ElasticacheClient
except ImportError:
    ElasticacheClient = Any

try:
    from mypy_boto3.elasticbeanstalk.client import Client as ElasticbeanstalkClient
except ImportError:
    ElasticbeanstalkClient = Any

try:
    from mypy_boto3.elastictranscoder.client import Client as ElastictranscoderClient
except ImportError:
    ElastictranscoderClient = Any

try:
    from mypy_boto3.elb.client import Client as ELBClient
except ImportError:
    ELBClient = Any

try:
    from mypy_boto3.elbv2.client import Client as Elbv2Client
except ImportError:
    Elbv2Client = Any

try:
    from mypy_boto3.emr.client import Client as EMRClient
except ImportError:
    EMRClient = Any

try:
    from mypy_boto3.es.client import Client as ESClient
except ImportError:
    ESClient = Any

try:
    from mypy_boto3.events.client import Client as EventsClient
except ImportError:
    EventsClient = Any

try:
    from mypy_boto3.firehose.client import Client as FirehoseClient
except ImportError:
    FirehoseClient = Any

try:
    from mypy_boto3.fms.client import Client as FMSClient
except ImportError:
    FMSClient = Any

try:
    from mypy_boto3.forecast.client import Client as ForecastClient
except ImportError:
    ForecastClient = Any

try:
    from mypy_boto3.forecastquery.client import Client as ForecastqueryClient
except ImportError:
    ForecastqueryClient = Any

try:
    from mypy_boto3.fsx.client import Client as FSXClient
except ImportError:
    FSXClient = Any

try:
    from mypy_boto3.gamelift.client import Client as GameliftClient
except ImportError:
    GameliftClient = Any

try:
    from mypy_boto3.glacier.client import Client as GlacierClient
except ImportError:
    GlacierClient = Any
try:
    from mypy_boto3.glacier.service_resource import ServiceResource as GlacierServiceResource
except ImportError:
    GlacierServiceResource = Any

try:
    from mypy_boto3.globalaccelerator.client import Client as GlobalacceleratorClient
except ImportError:
    GlobalacceleratorClient = Any

try:
    from mypy_boto3.glue.client import Client as GlueClient
except ImportError:
    GlueClient = Any

try:
    from mypy_boto3.greengrass.client import Client as GreengrassClient
except ImportError:
    GreengrassClient = Any

try:
    from mypy_boto3.groundstation.client import Client as GroundstationClient
except ImportError:
    GroundstationClient = Any

try:
    from mypy_boto3.guardduty.client import Client as GuarddutyClient
except ImportError:
    GuarddutyClient = Any

try:
    from mypy_boto3.health.client import Client as HealthClient
except ImportError:
    HealthClient = Any

try:
    from mypy_boto3.iam.client import Client as IAMClient
except ImportError:
    IAMClient = Any
try:
    from mypy_boto3.iam.service_resource import ServiceResource as IAMServiceResource
except ImportError:
    IAMServiceResource = Any

try:
    from mypy_boto3.importexport.client import Client as ImportexportClient
except ImportError:
    ImportexportClient = Any

try:
    from mypy_boto3.inspector.client import Client as InspectorClient
except ImportError:
    InspectorClient = Any

try:
    from mypy_boto3.iot.client import Client as IOTClient
except ImportError:
    IOTClient = Any

try:
    from mypy_boto3.iot_data.client import Client as IotDataClient
except ImportError:
    IotDataClient = Any

try:
    from mypy_boto3.iot_jobs_data.client import Client as IotJobsDataClient
except ImportError:
    IotJobsDataClient = Any

try:
    from mypy_boto3.iot1click_devices.client import Client as Iot1clickDevicesClient
except ImportError:
    Iot1clickDevicesClient = Any

try:
    from mypy_boto3.iot1click_projects.client import Client as Iot1clickProjectsClient
except ImportError:
    Iot1clickProjectsClient = Any

try:
    from mypy_boto3.iotanalytics.client import Client as IotanalyticsClient
except ImportError:
    IotanalyticsClient = Any

try:
    from mypy_boto3.iotevents.client import Client as IoteventsClient
except ImportError:
    IoteventsClient = Any

try:
    from mypy_boto3.iotevents_data.client import Client as IoteventsDataClient
except ImportError:
    IoteventsDataClient = Any

try:
    from mypy_boto3.iotthingsgraph.client import Client as IotthingsgraphClient
except ImportError:
    IotthingsgraphClient = Any

try:
    from mypy_boto3.kafka.client import Client as KafkaClient
except ImportError:
    KafkaClient = Any

try:
    from mypy_boto3.kinesis.client import Client as KinesisClient
except ImportError:
    KinesisClient = Any

try:
    from mypy_boto3.kinesis_video_archived_media.client import Client as KinesisVideoArchivedMediaClient
except ImportError:
    KinesisVideoArchivedMediaClient = Any

try:
    from mypy_boto3.kinesis_video_media.client import Client as KinesisVideoMediaClient
except ImportError:
    KinesisVideoMediaClient = Any

try:
    from mypy_boto3.kinesisanalytics.client import Client as KinesisanalyticsClient
except ImportError:
    KinesisanalyticsClient = Any

try:
    from mypy_boto3.kinesisanalyticsv2.client import Client as Kinesisanalyticsv2Client
except ImportError:
    Kinesisanalyticsv2Client = Any

try:
    from mypy_boto3.kinesisvideo.client import Client as KinesisvideoClient
except ImportError:
    KinesisvideoClient = Any

try:
    from mypy_boto3.kms.client import Client as KMSClient
except ImportError:
    KMSClient = Any

try:
    from mypy_boto3.lakeformation.client import Client as LakeformationClient
except ImportError:
    LakeformationClient = Any

try:
    from mypy_boto3.lambda_.client import Client as LambdaClient
except ImportError:
    LambdaClient = Any

try:
    from mypy_boto3.lex_models.client import Client as LexModelsClient
except ImportError:
    LexModelsClient = Any

try:
    from mypy_boto3.lex_runtime.client import Client as LexRuntimeClient
except ImportError:
    LexRuntimeClient = Any

try:
    from mypy_boto3.license_manager.client import Client as LicenseManagerClient
except ImportError:
    LicenseManagerClient = Any

try:
    from mypy_boto3.lightsail.client import Client as LightsailClient
except ImportError:
    LightsailClient = Any

try:
    from mypy_boto3.logs.client import Client as LogsClient
except ImportError:
    LogsClient = Any

try:
    from mypy_boto3.machinelearning.client import Client as MachinelearningClient
except ImportError:
    MachinelearningClient = Any

try:
    from mypy_boto3.macie.client import Client as MacieClient
except ImportError:
    MacieClient = Any

try:
    from mypy_boto3.managedblockchain.client import Client as ManagedblockchainClient
except ImportError:
    ManagedblockchainClient = Any

try:
    from mypy_boto3.marketplace_entitlement.client import Client as MarketplaceEntitlementClient
except ImportError:
    MarketplaceEntitlementClient = Any

try:
    from mypy_boto3.marketplacecommerceanalytics.client import Client as MarketplacecommerceanalyticsClient
except ImportError:
    MarketplacecommerceanalyticsClient = Any

try:
    from mypy_boto3.mediaconnect.client import Client as MediaconnectClient
except ImportError:
    MediaconnectClient = Any

try:
    from mypy_boto3.mediaconvert.client import Client as MediaconvertClient
except ImportError:
    MediaconvertClient = Any

try:
    from mypy_boto3.medialive.client import Client as MedialiveClient
except ImportError:
    MedialiveClient = Any

try:
    from mypy_boto3.mediapackage.client import Client as MediapackageClient
except ImportError:
    MediapackageClient = Any

try:
    from mypy_boto3.mediapackage_vod.client import Client as MediapackageVodClient
except ImportError:
    MediapackageVodClient = Any

try:
    from mypy_boto3.mediastore.client import Client as MediastoreClient
except ImportError:
    MediastoreClient = Any

try:
    from mypy_boto3.mediastore_data.client import Client as MediastoreDataClient
except ImportError:
    MediastoreDataClient = Any

try:
    from mypy_boto3.mediatailor.client import Client as MediatailorClient
except ImportError:
    MediatailorClient = Any

try:
    from mypy_boto3.meteringmarketplace.client import Client as MeteringmarketplaceClient
except ImportError:
    MeteringmarketplaceClient = Any

try:
    from mypy_boto3.mgh.client import Client as MGHClient
except ImportError:
    MGHClient = Any

try:
    from mypy_boto3.mobile.client import Client as MobileClient
except ImportError:
    MobileClient = Any

try:
    from mypy_boto3.mq.client import Client as MQClient
except ImportError:
    MQClient = Any

try:
    from mypy_boto3.mturk.client import Client as MturkClient
except ImportError:
    MturkClient = Any

try:
    from mypy_boto3.neptune.client import Client as NeptuneClient
except ImportError:
    NeptuneClient = Any

try:
    from mypy_boto3.opsworks.client import Client as OpsworksClient
except ImportError:
    OpsworksClient = Any
try:
    from mypy_boto3.opsworks.service_resource import ServiceResource as OpsworksServiceResource
except ImportError:
    OpsworksServiceResource = Any

try:
    from mypy_boto3.opsworkscm.client import Client as OpsworkscmClient
except ImportError:
    OpsworkscmClient = Any

try:
    from mypy_boto3.organizations.client import Client as OrganizationsClient
except ImportError:
    OrganizationsClient = Any

try:
    from mypy_boto3.personalize.client import Client as PersonalizeClient
except ImportError:
    PersonalizeClient = Any

try:
    from mypy_boto3.personalize_events.client import Client as PersonalizeEventsClient
except ImportError:
    PersonalizeEventsClient = Any

try:
    from mypy_boto3.personalize_runtime.client import Client as PersonalizeRuntimeClient
except ImportError:
    PersonalizeRuntimeClient = Any

try:
    from mypy_boto3.pi.client import Client as PIClient
except ImportError:
    PIClient = Any

try:
    from mypy_boto3.pinpoint.client import Client as PinpointClient
except ImportError:
    PinpointClient = Any

try:
    from mypy_boto3.pinpoint_email.client import Client as PinpointEmailClient
except ImportError:
    PinpointEmailClient = Any

try:
    from mypy_boto3.pinpoint_sms_voice.client import Client as PinpointSmsVoiceClient
except ImportError:
    PinpointSmsVoiceClient = Any

try:
    from mypy_boto3.polly.client import Client as PollyClient
except ImportError:
    PollyClient = Any

try:
    from mypy_boto3.pricing.client import Client as PricingClient
except ImportError:
    PricingClient = Any

try:
    from mypy_boto3.qldb.client import Client as QldbClient
except ImportError:
    QldbClient = Any

try:
    from mypy_boto3.qldb_session.client import Client as QldbSessionClient
except ImportError:
    QldbSessionClient = Any

try:
    from mypy_boto3.quicksight.client import Client as QuicksightClient
except ImportError:
    QuicksightClient = Any

try:
    from mypy_boto3.ram.client import Client as RAMClient
except ImportError:
    RAMClient = Any

try:
    from mypy_boto3.rds.client import Client as RDSClient
except ImportError:
    RDSClient = Any

try:
    from mypy_boto3.rds_data.client import Client as RdsDataClient
except ImportError:
    RdsDataClient = Any

try:
    from mypy_boto3.redshift.client import Client as RedshiftClient
except ImportError:
    RedshiftClient = Any

try:
    from mypy_boto3.rekognition.client import Client as RekognitionClient
except ImportError:
    RekognitionClient = Any

try:
    from mypy_boto3.resource_groups.client import Client as ResourceGroupsClient
except ImportError:
    ResourceGroupsClient = Any

try:
    from mypy_boto3.resourcegroupstaggingapi.client import Client as ResourcegroupstaggingapiClient
except ImportError:
    ResourcegroupstaggingapiClient = Any

try:
    from mypy_boto3.robomaker.client import Client as RobomakerClient
except ImportError:
    RobomakerClient = Any

try:
    from mypy_boto3.route53.client import Client as Route53Client
except ImportError:
    Route53Client = Any

try:
    from mypy_boto3.route53domains.client import Client as Route53domainsClient
except ImportError:
    Route53domainsClient = Any

try:
    from mypy_boto3.route53resolver.client import Client as Route53resolverClient
except ImportError:
    Route53resolverClient = Any

try:
    from mypy_boto3.s3.client import Client as S3Client
except ImportError:
    S3Client = Any
try:
    from mypy_boto3.s3.service_resource import ServiceResource as S3ServiceResource
except ImportError:
    S3ServiceResource = Any

try:
    from mypy_boto3.s3control.client import Client as S3controlClient
except ImportError:
    S3controlClient = Any

try:
    from mypy_boto3.sagemaker.client import Client as SagemakerClient
except ImportError:
    SagemakerClient = Any

try:
    from mypy_boto3.sagemaker_runtime.client import Client as SagemakerRuntimeClient
except ImportError:
    SagemakerRuntimeClient = Any

try:
    from mypy_boto3.savingsplans.client import Client as SavingsplansClient
except ImportError:
    SavingsplansClient = Any

try:
    from mypy_boto3.sdb.client import Client as SDBClient
except ImportError:
    SDBClient = Any

try:
    from mypy_boto3.secretsmanager.client import Client as SecretsmanagerClient
except ImportError:
    SecretsmanagerClient = Any

try:
    from mypy_boto3.securityhub.client import Client as SecurityhubClient
except ImportError:
    SecurityhubClient = Any

try:
    from mypy_boto3.serverlessrepo.client import Client as ServerlessrepoClient
except ImportError:
    ServerlessrepoClient = Any

try:
    from mypy_boto3.service_quotas.client import Client as ServiceQuotasClient
except ImportError:
    ServiceQuotasClient = Any

try:
    from mypy_boto3.servicecatalog.client import Client as ServicecatalogClient
except ImportError:
    ServicecatalogClient = Any

try:
    from mypy_boto3.servicediscovery.client import Client as ServicediscoveryClient
except ImportError:
    ServicediscoveryClient = Any

try:
    from mypy_boto3.ses.client import Client as SESClient
except ImportError:
    SESClient = Any

try:
    from mypy_boto3.shield.client import Client as ShieldClient
except ImportError:
    ShieldClient = Any

try:
    from mypy_boto3.signer.client import Client as SignerClient
except ImportError:
    SignerClient = Any

try:
    from mypy_boto3.sms.client import Client as SMSClient
except ImportError:
    SMSClient = Any

try:
    from mypy_boto3.sms_voice.client import Client as SmsVoiceClient
except ImportError:
    SmsVoiceClient = Any

try:
    from mypy_boto3.snowball.client import Client as SnowballClient
except ImportError:
    SnowballClient = Any

try:
    from mypy_boto3.sns.client import Client as SNSClient
except ImportError:
    SNSClient = Any
try:
    from mypy_boto3.sns.service_resource import ServiceResource as SNSServiceResource
except ImportError:
    SNSServiceResource = Any

try:
    from mypy_boto3.sqs.client import Client as SQSClient
except ImportError:
    SQSClient = Any
try:
    from mypy_boto3.sqs.service_resource import ServiceResource as SQSServiceResource
except ImportError:
    SQSServiceResource = Any

try:
    from mypy_boto3.ssm.client import Client as SSMClient
except ImportError:
    SSMClient = Any

try:
    from mypy_boto3.stepfunctions.client import Client as StepfunctionsClient
except ImportError:
    StepfunctionsClient = Any

try:
    from mypy_boto3.storagegateway.client import Client as StoragegatewayClient
except ImportError:
    StoragegatewayClient = Any

try:
    from mypy_boto3.sts.client import Client as STSClient
except ImportError:
    STSClient = Any

try:
    from mypy_boto3.support.client import Client as SupportClient
except ImportError:
    SupportClient = Any

try:
    from mypy_boto3.swf.client import Client as SWFClient
except ImportError:
    SWFClient = Any

try:
    from mypy_boto3.textract.client import Client as TextractClient
except ImportError:
    TextractClient = Any

try:
    from mypy_boto3.transcribe.client import Client as TranscribeClient
except ImportError:
    TranscribeClient = Any

try:
    from mypy_boto3.transfer.client import Client as TransferClient
except ImportError:
    TransferClient = Any

try:
    from mypy_boto3.translate.client import Client as TranslateClient
except ImportError:
    TranslateClient = Any

try:
    from mypy_boto3.waf.client import Client as WAFClient
except ImportError:
    WAFClient = Any

try:
    from mypy_boto3.waf_regional.client import Client as WafRegionalClient
except ImportError:
    WafRegionalClient = Any

try:
    from mypy_boto3.workdocs.client import Client as WorkdocsClient
except ImportError:
    WorkdocsClient = Any

try:
    from mypy_boto3.worklink.client import Client as WorklinkClient
except ImportError:
    WorklinkClient = Any

try:
    from mypy_boto3.workmail.client import Client as WorkmailClient
except ImportError:
    WorkmailClient = Any

try:
    from mypy_boto3.workmailmessageflow.client import Client as WorkmailmessageflowClient
except ImportError:
    WorkmailmessageflowClient = Any

try:
    from mypy_boto3.workspaces.client import Client as WorkspacesClient
except ImportError:
    WorkspacesClient = Any

try:
    from mypy_boto3.xray.client import Client as XrayClient
except ImportError:
    XrayClient = Any

__author__: str
__version__: str

DEFAULT_SESSION: Optional[Session] = None

def setup_default_session(
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    region_name: str = None,
    botocore_session: str = None,
    profile_name: str = None,
) -> Session: ...
def set_stream_logger(
    name: str = "boto3", level: int = logging.DEBUG, format_string: Optional[str] = None
) -> None: ...
def _get_default_session() -> Session: ...

class NullHandler(logging.Handler):
    def emit(self, record: Any) -> Any:
        pass

@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['acm'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ACMClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['acm-pca'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> AcmPcaClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['alexaforbusiness'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> AlexaforbusinessClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['amplify'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> AmplifyClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['apigateway'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ApigatewayClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['apigatewaymanagementapi'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ApigatewaymanagementapiClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['apigatewayv2'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> Apigatewayv2Client: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['application-autoscaling'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ApplicationAutoscalingClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['application-insights'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ApplicationInsightsClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['appmesh'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> AppmeshClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['appstream'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> AppstreamClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['appsync'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> AppsyncClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['athena'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> AthenaClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['autoscaling'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> AutoscalingClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['autoscaling-plans'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> AutoscalingPlansClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['backup'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> BackupClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['batch'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> BatchClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['budgets'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> BudgetsClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['ce'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CEClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['chime'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ChimeClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['cloud9'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> Cloud9Client: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['clouddirectory'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ClouddirectoryClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['cloudformation'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CloudformationClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['cloudfront'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CloudfrontClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['cloudhsm'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CloudhsmClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['cloudhsmv2'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> Cloudhsmv2Client: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['cloudsearch'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CloudsearchClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['cloudsearchdomain'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CloudsearchdomainClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['cloudtrail'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CloudtrailClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['cloudwatch'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CloudwatchClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['codebuild'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CodebuildClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['codecommit'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CodecommitClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['codedeploy'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CodedeployClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['codepipeline'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CodepipelineClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['codestar'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CodestarClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['codestar-notifications'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CodestarNotificationsClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['cognito-identity'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CognitoIdentityClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['cognito-idp'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CognitoIdpClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['cognito-sync'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CognitoSyncClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['comprehend'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ComprehendClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['comprehendmedical'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ComprehendmedicalClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['config'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ConfigClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['connect'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ConnectClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['cur'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CURClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['datapipeline'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> DatapipelineClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['datasync'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> DatasyncClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['dax'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> DAXClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['devicefarm'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> DevicefarmClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['directconnect'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> DirectconnectClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['discovery'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> DiscoveryClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['dlm'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> DLMClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['dms'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> DMSClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['docdb'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> DocdbClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['ds'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> DSClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['dynamodb'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> DynamodbClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['dynamodbstreams'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> DynamodbstreamsClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['ec2'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> EC2Client: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['ec2-instance-connect'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> Ec2InstanceConnectClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['ecr'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ECRClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['ecs'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ECSClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['efs'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> EFSClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['eks'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> EKSClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['elasticache'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ElasticacheClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['elasticbeanstalk'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ElasticbeanstalkClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['elastictranscoder'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ElastictranscoderClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['elb'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ELBClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['elbv2'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> Elbv2Client: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['emr'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> EMRClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['es'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ESClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['events'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> EventsClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['firehose'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> FirehoseClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['fms'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> FMSClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['forecast'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ForecastClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['forecastquery'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ForecastqueryClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['fsx'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> FSXClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['gamelift'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> GameliftClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['glacier'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> GlacierClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['globalaccelerator'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> GlobalacceleratorClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['glue'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> GlueClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['greengrass'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> GreengrassClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['groundstation'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> GroundstationClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['guardduty'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> GuarddutyClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['health'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> HealthClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['iam'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> IAMClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['importexport'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ImportexportClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['inspector'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> InspectorClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['iot'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> IOTClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['iot-data'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> IotDataClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['iot-jobs-data'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> IotJobsDataClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['iot1click-devices'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> Iot1clickDevicesClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['iot1click-projects'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> Iot1clickProjectsClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['iotanalytics'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> IotanalyticsClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['iotevents'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> IoteventsClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['iotevents-data'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> IoteventsDataClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['iotthingsgraph'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> IotthingsgraphClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['kafka'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> KafkaClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['kinesis'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> KinesisClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['kinesis-video-archived-media'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> KinesisVideoArchivedMediaClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['kinesis-video-media'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> KinesisVideoMediaClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['kinesisanalytics'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> KinesisanalyticsClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['kinesisanalyticsv2'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> Kinesisanalyticsv2Client: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['kinesisvideo'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> KinesisvideoClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['kms'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> KMSClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['lakeformation'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> LakeformationClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['lambda'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> LambdaClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['lex-models'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> LexModelsClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['lex-runtime'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> LexRuntimeClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['license-manager'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> LicenseManagerClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['lightsail'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> LightsailClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['logs'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> LogsClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['machinelearning'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> MachinelearningClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['macie'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> MacieClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['managedblockchain'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ManagedblockchainClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['marketplace-entitlement'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> MarketplaceEntitlementClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['marketplacecommerceanalytics'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> MarketplacecommerceanalyticsClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['mediaconnect'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> MediaconnectClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['mediaconvert'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> MediaconvertClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['medialive'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> MedialiveClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['mediapackage'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> MediapackageClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['mediapackage-vod'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> MediapackageVodClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['mediastore'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> MediastoreClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['mediastore-data'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> MediastoreDataClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['mediatailor'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> MediatailorClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['meteringmarketplace'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> MeteringmarketplaceClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['mgh'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> MGHClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['mobile'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> MobileClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['mq'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> MQClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['mturk'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> MturkClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['neptune'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> NeptuneClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['opsworks'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> OpsworksClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['opsworkscm'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> OpsworkscmClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['organizations'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> OrganizationsClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['personalize'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> PersonalizeClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['personalize-events'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> PersonalizeEventsClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['personalize-runtime'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> PersonalizeRuntimeClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['pi'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> PIClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['pinpoint'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> PinpointClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['pinpoint-email'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> PinpointEmailClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['pinpoint-sms-voice'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> PinpointSmsVoiceClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['polly'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> PollyClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['pricing'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> PricingClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['qldb'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> QldbClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['qldb-session'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> QldbSessionClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['quicksight'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> QuicksightClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['ram'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> RAMClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['rds'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> RDSClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['rds-data'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> RdsDataClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['redshift'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> RedshiftClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['rekognition'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> RekognitionClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['resource-groups'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ResourceGroupsClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['resourcegroupstaggingapi'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ResourcegroupstaggingapiClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['robomaker'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> RobomakerClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['route53'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> Route53Client: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['route53domains'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> Route53domainsClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['route53resolver'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> Route53resolverClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['s3'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> S3Client: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['s3control'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> S3controlClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['sagemaker'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> SagemakerClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['sagemaker-runtime'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> SagemakerRuntimeClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['savingsplans'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> SavingsplansClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['sdb'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> SDBClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['secretsmanager'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> SecretsmanagerClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['securityhub'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> SecurityhubClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['serverlessrepo'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ServerlessrepoClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['service-quotas'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ServiceQuotasClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['servicecatalog'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ServicecatalogClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['servicediscovery'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ServicediscoveryClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['ses'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> SESClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['shield'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> ShieldClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['signer'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> SignerClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['sms'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> SMSClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['sms-voice'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> SmsVoiceClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['snowball'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> SnowballClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['sns'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> SNSClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['sqs'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> SQSClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['ssm'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> SSMClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['stepfunctions'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> StepfunctionsClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['storagegateway'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> StoragegatewayClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['sts'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> STSClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['support'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> SupportClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['swf'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> SWFClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['textract'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> TextractClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['transcribe'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> TranscribeClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['transfer'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> TransferClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['translate'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> TranslateClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['waf'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> WAFClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['waf-regional'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> WafRegionalClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['workdocs'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> WorkdocsClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['worklink'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> WorklinkClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['workmail'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> WorkmailClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['workmailmessageflow'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> WorkmailmessageflowClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['workspaces'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> WorkspacesClient: ...
@overload
# pylint: disable=arguments-differ
def client(
    service_name: Literal['xray'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> XrayClient: ...
@overload
# pylint: disable=arguments-differ
def resource(
    service_name: Literal['cloudformation'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CloudformationServiceResource: ...
@overload
# pylint: disable=arguments-differ
def resource(
    service_name: Literal['cloudwatch'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> CloudwatchServiceResource: ...
@overload
# pylint: disable=arguments-differ
def resource(
    service_name: Literal['dynamodb'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> DynamodbServiceResource: ...
@overload
# pylint: disable=arguments-differ
def resource(
    service_name: Literal['ec2'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> EC2ServiceResource: ...
@overload
# pylint: disable=arguments-differ
def resource(
    service_name: Literal['glacier'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> GlacierServiceResource: ...
@overload
# pylint: disable=arguments-differ
def resource(
    service_name: Literal['iam'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> IAMServiceResource: ...
@overload
# pylint: disable=arguments-differ
def resource(
    service_name: Literal['opsworks'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> OpsworksServiceResource: ...
@overload
# pylint: disable=arguments-differ
def resource(
    service_name: Literal['s3'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> S3ServiceResource: ...
@overload
# pylint: disable=arguments-differ
def resource(
    service_name: Literal['sns'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> SNSServiceResource: ...
@overload
# pylint: disable=arguments-differ
def resource(
    service_name: Literal['sqs'],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None
) -> SQSServiceResource: ...

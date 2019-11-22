"""
Enum with all AWS services.
"""
from __future__ import annotations

import enum
from typing import List

from mypy_boto3_builder.constants import PYPI_NAME, MODULE_NAME


class ServiceName(enum.Enum):
    """
    Enum with all AWS services.
    """

    acm = "acm"
    acm_pca = "acm-pca"
    alexaforbusiness = "alexaforbusiness"
    amplify = "amplify"
    apigateway = "apigateway"
    apigatewaymanagementapi = "apigatewaymanagementapi"
    apigatewayv2 = "apigatewayv2"
    application_autoscaling = "application-autoscaling"
    application_insights = "application-insights"
    appmesh = "appmesh"
    appstream = "appstream"
    appsync = "appsync"
    athena = "athena"
    autoscaling = "autoscaling"
    autoscaling_plans = "autoscaling-plans"
    backup = "backup"
    batch = "batch"
    budgets = "budgets"
    ce = "ce"
    chime = "chime"
    cloud9 = "cloud9"
    clouddirectory = "clouddirectory"
    cloudformation = "cloudformation"
    cloudfront = "cloudfront"
    cloudhsm = "cloudhsm"
    cloudhsmv2 = "cloudhsmv2"
    cloudsearch = "cloudsearch"
    cloudsearchdomain = "cloudsearchdomain"
    cloudtrail = "cloudtrail"
    cloudwatch = "cloudwatch"
    codebuild = "codebuild"
    codecommit = "codecommit"
    codedeploy = "codedeploy"
    codepipeline = "codepipeline"
    codestar = "codestar"
    codestar_notifications = "codestar-notifications"
    cognito_identity = "cognito-identity"
    cognito_idp = "cognito-idp"
    cognito_sync = "cognito-sync"
    comprehend = "comprehend"
    comprehendmedical = "comprehendmedical"
    config = "config"
    connect = "connect"
    cur = "cur"
    datapipeline = "datapipeline"
    datasync = "datasync"
    dax = "dax"
    devicefarm = "devicefarm"
    directconnect = "directconnect"
    discovery = "discovery"
    dlm = "dlm"
    dms = "dms"
    docdb = "docdb"
    ds = "ds"
    dynamodb = "dynamodb"
    dynamodbstreams = "dynamodbstreams"
    ec2 = "ec2"
    ec2_instance_connect = "ec2-instance-connect"
    ecr = "ecr"
    ecs = "ecs"
    efs = "efs"
    eks = "eks"
    elasticache = "elasticache"
    elasticbeanstalk = "elasticbeanstalk"
    elastictranscoder = "elastictranscoder"
    elb = "elb"
    elbv2 = "elbv2"
    emr = "emr"
    es = "es"
    events = "events"
    firehose = "firehose"
    fms = "fms"
    forecast = "forecast"
    forecastquery = "forecastquery"
    fsx = "fsx"
    gamelift = "gamelift"
    glacier = "glacier"
    globalaccelerator = "globalaccelerator"
    glue = "glue"
    greengrass = "greengrass"
    groundstation = "groundstation"
    guardduty = "guardduty"
    health = "health"
    iam = "iam"
    importexport = "importexport"
    inspector = "inspector"
    iot = "iot"
    iot_data = "iot-data"
    iot_jobs_data = "iot-jobs-data"
    iot1click_devices = "iot1click-devices"
    iot1click_projects = "iot1click-projects"
    iotanalytics = "iotanalytics"
    iotevents = "iotevents"
    iotevents_data = "iotevents-data"
    iotthingsgraph = "iotthingsgraph"
    kafka = "kafka"
    kinesis = "kinesis"
    kinesis_video_archived_media = "kinesis-video-archived-media"
    kinesis_video_media = "kinesis-video-media"
    kinesisanalytics = "kinesisanalytics"
    kinesisanalyticsv2 = "kinesisanalyticsv2"
    kinesisvideo = "kinesisvideo"
    kms = "kms"
    lakeformation = "lakeformation"
    lambda_ = "lambda"
    lex_models = "lex-models"
    lex_runtime = "lex-runtime"
    license_manager = "license-manager"
    lightsail = "lightsail"
    logs = "logs"
    machinelearning = "machinelearning"
    macie = "macie"
    managedblockchain = "managedblockchain"
    marketplace_entitlement = "marketplace-entitlement"
    marketplacecommerceanalytics = "marketplacecommerceanalytics"
    mediaconnect = "mediaconnect"
    mediaconvert = "mediaconvert"
    medialive = "medialive"
    mediapackage = "mediapackage"
    mediapackage_vod = "mediapackage-vod"
    mediastore = "mediastore"
    mediastore_data = "mediastore-data"
    mediatailor = "mediatailor"
    meteringmarketplace = "meteringmarketplace"
    mgh = "mgh"
    mobile = "mobile"
    mq = "mq"
    mturk = "mturk"
    neptune = "neptune"
    opsworks = "opsworks"
    opsworkscm = "opsworkscm"
    organizations = "organizations"
    personalize = "personalize"
    personalize_events = "personalize-events"
    personalize_runtime = "personalize-runtime"
    pi = "pi"
    pinpoint = "pinpoint"
    pinpoint_email = "pinpoint-email"
    pinpoint_sms_voice = "pinpoint-sms-voice"
    polly = "polly"
    pricing = "pricing"
    qldb = "qldb"
    qldb_session = "qldb-session"
    quicksight = "quicksight"
    ram = "ram"
    rds = "rds"
    rds_data = "rds-data"
    redshift = "redshift"
    rekognition = "rekognition"
    resource_groups = "resource-groups"
    resourcegroupstaggingapi = "resourcegroupstaggingapi"
    robomaker = "robomaker"
    route53 = "route53"
    route53domains = "route53domains"
    route53resolver = "route53resolver"
    s3 = "s3"
    s3control = "s3control"
    sagemaker = "sagemaker"
    sagemaker_runtime = "sagemaker-runtime"
    savingsplans = "savingsplans"
    sdb = "sdb"
    secretsmanager = "secretsmanager"
    securityhub = "securityhub"
    serverlessrepo = "serverlessrepo"
    service_quotas = "service-quotas"
    servicecatalog = "servicecatalog"
    servicediscovery = "servicediscovery"
    ses = "ses"
    shield = "shield"
    signer = "signer"
    sms = "sms"
    sms_voice = "sms-voice"
    snowball = "snowball"
    sns = "sns"
    sqs = "sqs"
    ssm = "ssm"
    stepfunctions = "stepfunctions"
    storagegateway = "storagegateway"
    sts = "sts"
    support = "support"
    swf = "swf"
    textract = "textract"
    transcribe = "transcribe"
    transfer = "transfer"
    translate = "translate"
    waf = "waf"
    waf_regional = "waf-regional"
    workdocs = "workdocs"
    worklink = "worklink"
    workmail = "workmail"
    workmailmessageflow = "workmailmessageflow"
    workspaces = "workspaces"
    xray = "xray"

    @classmethod
    def items(cls) -> List[ServiceName]:
        return list(cls)

    @classmethod
    def values(cls) -> List[str]:
        """
        Get all values - valid boto3 service names.

        Returns:
            A list of supported boto3 service names.
        """
        return [i.value for i in cls]

    @property
    def module_name(self) -> str:
        """
        Package name for given service.
        """
        return f"{MODULE_NAME}_{self.name}".rstrip("_")

    @property
    def extras_name(self) -> str:
        """
        Extras name for subpackage installation.
        """
        return str(self.value)

    @property
    def import_name(self) -> str:
        """
        Submodule name in main module.
        """
        return self.name

    @property
    def pypi_name(self) -> str:
        """
        Name of package on PyPI.
        """
        return f"{PYPI_NAME}-{self.value}"

    def is_essential(self) -> bool:
        """
        Whether service is essential and installed with main package by default.
        """
        return self in [
            ServiceName.ec2,
            ServiceName.rds,
            ServiceName.s3,
            ServiceName.lambda_,
            ServiceName.sqs,
            ServiceName.cloudformation,
            ServiceName.dynamodb,
        ]

    @property
    def boto3_name(self) -> str:
        """
        Boto3 service name.
        """
        return str(self.value)

    @property
    def class_prefix(self) -> str:
        """
        Class prefix for internal classes.
        """
        import_name = self.import_name
        if len(import_name) < 4:
            return import_name.upper().replace("_", "")

        name_parts = [i.capitalize() for i in import_name.split("_") if i]
        return "".join(name_parts)

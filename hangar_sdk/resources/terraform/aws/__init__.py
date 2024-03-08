from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformProvider


@define(kw_only=True, slots=False)
class AssumeRole(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="assume_role")
    duration: Optional[str] = None
    external_id: Optional[str] = None
    policy: Optional[str] = None
    policy_arns: Optional[Sequence[str]] = None
    role_arn: Optional[str] = None
    session_name: Optional[str] = None
    source_identity: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    transitive_tag_keys: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class AssumeRoleWithWebIdentity(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="assume_role_with_web_identity")
    duration: Optional[str] = None
    policy: Optional[str] = None
    policy_arns: Optional[Sequence[str]] = None
    role_arn: Optional[str] = None
    session_name: Optional[str] = None
    web_identity_token: Optional[str] = None
    web_identity_token_file: Optional[str] = None


@define(kw_only=True, slots=False)
class DefaultTags(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="default_tags")
    tags: Optional[Dict[str, str]] = None


@define(kw_only=True, slots=False)
class Endpoints(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="endpoints")
    accessanalyzer: Optional[str] = None
    account: Optional[str] = None
    acm: Optional[str] = None
    acmpca: Optional[str] = None
    amg: Optional[str] = None
    amp: Optional[str] = None
    amplify: Optional[str] = None
    apigateway: Optional[str] = None
    apigatewayv2: Optional[str] = None
    appautoscaling: Optional[str] = None
    appconfig: Optional[str] = None
    appfabric: Optional[str] = None
    appflow: Optional[str] = None
    appintegrations: Optional[str] = None
    appintegrationsservice: Optional[str] = None
    applicationautoscaling: Optional[str] = None
    applicationinsights: Optional[str] = None
    appmesh: Optional[str] = None
    appregistry: Optional[str] = None
    apprunner: Optional[str] = None
    appstream: Optional[str] = None
    appsync: Optional[str] = None
    athena: Optional[str] = None
    auditmanager: Optional[str] = None
    autoscaling: Optional[str] = None
    autoscalingplans: Optional[str] = None
    backup: Optional[str] = None
    batch: Optional[str] = None
    beanstalk: Optional[str] = None
    bedrock: Optional[str] = None
    bedrockagent: Optional[str] = None
    budgets: Optional[str] = None
    ce: Optional[str] = None
    chime: Optional[str] = None
    chimesdkmediapipelines: Optional[str] = None
    chimesdkvoice: Optional[str] = None
    cleanrooms: Optional[str] = None
    cloud9: Optional[str] = None
    cloudcontrol: Optional[str] = None
    cloudcontrolapi: Optional[str] = None
    cloudformation: Optional[str] = None
    cloudfront: Optional[str] = None
    cloudfrontkeyvaluestore: Optional[str] = None
    cloudhsm: Optional[str] = None
    cloudhsmv2: Optional[str] = None
    cloudsearch: Optional[str] = None
    cloudtrail: Optional[str] = None
    cloudwatch: Optional[str] = None
    cloudwatchevents: Optional[str] = None
    cloudwatchevidently: Optional[str] = None
    cloudwatchlog: Optional[str] = None
    cloudwatchlogs: Optional[str] = None
    cloudwatchobservabilityaccessmanager: Optional[str] = None
    cloudwatchrum: Optional[str] = None
    codeartifact: Optional[str] = None
    codebuild: Optional[str] = None
    codecatalyst: Optional[str] = None
    codecommit: Optional[str] = None
    codedeploy: Optional[str] = None
    codeguruprofiler: Optional[str] = None
    codegurureviewer: Optional[str] = None
    codepipeline: Optional[str] = None
    codestarconnections: Optional[str] = None
    codestarnotifications: Optional[str] = None
    cognitoidentity: Optional[str] = None
    cognitoidentityprovider: Optional[str] = None
    cognitoidp: Optional[str] = None
    comprehend: Optional[str] = None
    computeoptimizer: Optional[str] = None
    config: Optional[str] = None
    configservice: Optional[str] = None
    connect: Optional[str] = None
    connectcases: Optional[str] = None
    controltower: Optional[str] = None
    costandusagereportservice: Optional[str] = None
    costexplorer: Optional[str] = None
    costoptimizationhub: Optional[str] = None
    cur: Optional[str] = None
    customerprofiles: Optional[str] = None
    databasemigration: Optional[str] = None
    databasemigrationservice: Optional[str] = None
    dataexchange: Optional[str] = None
    datapipeline: Optional[str] = None
    datasync: Optional[str] = None
    dax: Optional[str] = None
    deploy: Optional[str] = None
    detective: Optional[str] = None
    devicefarm: Optional[str] = None
    directconnect: Optional[str] = None
    directoryservice: Optional[str] = None
    dlm: Optional[str] = None
    dms: Optional[str] = None
    docdb: Optional[str] = None
    docdbelastic: Optional[str] = None
    ds: Optional[str] = None
    dynamodb: Optional[str] = None
    ec2: Optional[str] = None
    ecr: Optional[str] = None
    ecrpublic: Optional[str] = None
    ecs: Optional[str] = None
    efs: Optional[str] = None
    eks: Optional[str] = None
    elasticache: Optional[str] = None
    elasticbeanstalk: Optional[str] = None
    elasticloadbalancing: Optional[str] = None
    elasticloadbalancingv2: Optional[str] = None
    elasticsearch: Optional[str] = None
    elasticsearchservice: Optional[str] = None
    elastictranscoder: Optional[str] = None
    elb: Optional[str] = None
    elbv2: Optional[str] = None
    emr: Optional[str] = None
    emrcontainers: Optional[str] = None
    emrserverless: Optional[str] = None
    es: Optional[str] = None
    eventbridge: Optional[str] = None
    events: Optional[str] = None
    evidently: Optional[str] = None
    finspace: Optional[str] = None
    firehose: Optional[str] = None
    fis: Optional[str] = None
    fms: Optional[str] = None
    fsx: Optional[str] = None
    gamelift: Optional[str] = None
    glacier: Optional[str] = None
    globalaccelerator: Optional[str] = None
    glue: Optional[str] = None
    grafana: Optional[str] = None
    greengrass: Optional[str] = None
    groundstation: Optional[str] = None
    guardduty: Optional[str] = None
    healthlake: Optional[str] = None
    iam: Optional[str] = None
    identitystore: Optional[str] = None
    imagebuilder: Optional[str] = None
    inspector: Optional[str] = None
    inspector2: Optional[str] = None
    inspectorv2: Optional[str] = None
    internetmonitor: Optional[str] = None
    iot: Optional[str] = None
    iotanalytics: Optional[str] = None
    iotevents: Optional[str] = None
    ivs: Optional[str] = None
    ivschat: Optional[str] = None
    kafka: Optional[str] = None
    kafkaconnect: Optional[str] = None
    kendra: Optional[str] = None
    keyspaces: Optional[str] = None
    kinesis: Optional[str] = None
    kinesisanalytics: Optional[str] = None
    kinesisanalyticsv2: Optional[str] = None
    kinesisvideo: Optional[str] = None
    kms: Optional[str] = None
    lakeformation: Optional[str] = None
    launchwizard: Optional[str] = None
    lex: Optional[str] = None
    lexmodelbuilding: Optional[str] = None
    lexmodelbuildingservice: Optional[str] = None
    lexmodels: Optional[str] = None
    lexmodelsv2: Optional[str] = None
    lexv2models: Optional[str] = None
    licensemanager: Optional[str] = None
    lightsail: Optional[str] = None
    location: Optional[str] = None
    locationservice: Optional[str] = None
    logs: Optional[str] = None
    lookoutmetrics: Optional[str] = None
    m2: Optional[str] = None
    macie2: Optional[str] = None
    managedgrafana: Optional[str] = None
    mediaconnect: Optional[str] = None
    mediaconvert: Optional[str] = None
    medialive: Optional[str] = None
    mediapackage: Optional[str] = None
    mediapackagev2: Optional[str] = None
    mediastore: Optional[str] = None
    memorydb: Optional[str] = None
    mq: Optional[str] = None
    msk: Optional[str] = None
    mwaa: Optional[str] = None
    neptune: Optional[str] = None
    networkfirewall: Optional[str] = None
    networkmanager: Optional[str] = None
    oam: Optional[str] = None
    opensearch: Optional[str] = None
    opensearchingestion: Optional[str] = None
    opensearchserverless: Optional[str] = None
    opensearchservice: Optional[str] = None
    opsworks: Optional[str] = None
    organizations: Optional[str] = None
    osis: Optional[str] = None
    outposts: Optional[str] = None
    pcaconnectorad: Optional[str] = None
    pinpoint: Optional[str] = None
    pipes: Optional[str] = None
    polly: Optional[str] = None
    pricing: Optional[str] = None
    prometheus: Optional[str] = None
    prometheusservice: Optional[str] = None
    qbusiness: Optional[str] = None
    qldb: Optional[str] = None
    quicksight: Optional[str] = None
    ram: Optional[str] = None
    rbin: Optional[str] = None
    rds: Optional[str] = None
    recyclebin: Optional[str] = None
    redshift: Optional[str] = None
    redshiftdata: Optional[str] = None
    redshiftdataapiservice: Optional[str] = None
    redshiftserverless: Optional[str] = None
    rekognition: Optional[str] = None
    resourceexplorer2: Optional[str] = None
    resourcegroups: Optional[str] = None
    resourcegroupstagging: Optional[str] = None
    resourcegroupstaggingapi: Optional[str] = None
    rolesanywhere: Optional[str] = None
    route53: Optional[str] = None
    route53domains: Optional[str] = None
    route53recoverycontrolconfig: Optional[str] = None
    route53recoveryreadiness: Optional[str] = None
    route53resolver: Optional[str] = None
    rum: Optional[str] = None
    s3: Optional[str] = None
    s3api: Optional[str] = None
    s3control: Optional[str] = None
    s3outposts: Optional[str] = None
    sagemaker: Optional[str] = None
    scheduler: Optional[str] = None
    schemas: Optional[str] = None
    sdb: Optional[str] = None
    secretsmanager: Optional[str] = None
    securityhub: Optional[str] = None
    securitylake: Optional[str] = None
    serverlessapplicationrepository: Optional[str] = None
    serverlessapprepo: Optional[str] = None
    serverlessrepo: Optional[str] = None
    servicecatalog: Optional[str] = None
    servicecatalogappregistry: Optional[str] = None
    servicediscovery: Optional[str] = None
    servicequotas: Optional[str] = None
    ses: Optional[str] = None
    sesv2: Optional[str] = None
    sfn: Optional[str] = None
    shield: Optional[str] = None
    signer: Optional[str] = None
    simpledb: Optional[str] = None
    sns: Optional[str] = None
    sqs: Optional[str] = None
    ssm: Optional[str] = None
    ssmcontacts: Optional[str] = None
    ssmincidents: Optional[str] = None
    ssmsap: Optional[str] = None
    sso: Optional[str] = None
    ssoadmin: Optional[str] = None
    stepfunctions: Optional[str] = None
    storagegateway: Optional[str] = None
    sts: Optional[str] = None
    swf: Optional[str] = None
    synthetics: Optional[str] = None
    terraform_lambda: Optional[str] = None
    timestreamwrite: Optional[str] = None
    transcribe: Optional[str] = None
    transcribeservice: Optional[str] = None
    transfer: Optional[str] = None
    verifiedpermissions: Optional[str] = None
    vpclattice: Optional[str] = None
    waf: Optional[str] = None
    wafregional: Optional[str] = None
    wafv2: Optional[str] = None
    wellarchitected: Optional[str] = None
    worklink: Optional[str] = None
    workspaces: Optional[str] = None
    xray: Optional[str] = None


@define(kw_only=True, slots=False)
class IgnoreTags(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="ignore_tags")
    key_prefixes: Optional[Sequence[str]] = None
    keys: Optional[Sequence[str]] = None


@define(kw_only=True, slots=False)
class Aws(AbstractTerraformProvider):
    _group: Any
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws")
    _top_name: str
    access_key: Optional[str] = None
    allowed_account_ids: Optional[Sequence[str]] = None
    assume_role: Optional[Sequence[AssumeRole]] = None
    assume_role_with_web_identity: Optional[Sequence[AssumeRoleWithWebIdentity]] = None
    custom_ca_bundle: Optional[str] = None
    default_tags: Optional[Sequence[DefaultTags]] = None
    ec2_metadata_service_endpoint: Optional[str] = None
    ec2_metadata_service_endpoint_mode: Optional[str] = None
    endpoints: Optional[Sequence[Endpoints]] = None
    forbidden_account_ids: Optional[Sequence[str]] = None
    http_proxy: Optional[str] = None
    https_proxy: Optional[str] = None
    ignore_tags: Optional[Sequence[IgnoreTags]] = None
    insecure: Optional[bool] = None
    max_retries: Optional[int] = None
    no_proxy: Optional[str] = None
    profile: Optional[str] = None
    region: Optional[str] = None
    retry_mode: Optional[str] = None
    s3_us_east_1_regional_endpoint: Optional[str] = None
    s3_use_path_style: Optional[bool] = None
    secret_key: Optional[str] = None
    shared_config_files: Optional[Sequence[str]] = None
    shared_credentials_files: Optional[Sequence[str]] = None
    skip_credentials_validation: Optional[bool] = None
    skip_metadata_api_check: Optional[str] = None
    skip_region_validation: Optional[bool] = None
    skip_requesting_account_id: Optional[bool] = None
    sts_region: Optional[str] = None
    token: Optional[str] = None
    token_bucket_rate_limiter_capacity: Optional[int] = None
    use_dualstack_endpoint: Optional[bool] = None
    use_fips_endpoint: Optional[bool] = None

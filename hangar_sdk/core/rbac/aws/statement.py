from hangar_sdk.core.rbac.aws.iam_types.aws_policy_sentry_schema_version import aws_policy_sentry_schema_versionStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_a4b import aws_a4bStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_execute_api import aws_execute_apiStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_apigateway import aws_apigatewayStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_appflow import aws_appflowStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_app_integrations import aws_app_integrationsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_appstream import aws_appstreamStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_athena import aws_athenaStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_bedrock import aws_bedrockStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_braket import aws_braketStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_chime import aws_chimeStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_clouddirectory import aws_clouddirectoryStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_cloudfront import aws_cloudfrontStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_cloudfront_keyvaluestore import aws_cloudfront_keyvaluestoreStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_cloudsearch import aws_cloudsearchStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_cloudwatch import aws_cloudwatchStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_applicationinsights import aws_applicationinsightsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_evidently import aws_evidentlyStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_internetmonitor import aws_internetmonitorStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_logs import aws_logsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_networkmonitor import aws_networkmonitorStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_oam import aws_oamStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_synthetics import aws_syntheticsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_codecatalyst import aws_codecatalystStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_codeguru import aws_codeguruStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_codeguru_profiler import aws_codeguru_profilerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_codeguru_reviewer import aws_codeguru_reviewerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_codeguru_security import aws_codeguru_securityStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_codewhisperer import aws_codewhispererStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_cognito_identity import aws_cognito_identityStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_cognito_sync import aws_cognito_syncStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_cognito_idp import aws_cognito_idpStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_comprehend import aws_comprehendStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_comprehendmedical import aws_comprehendmedicalStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_connect import aws_connectStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_cases import aws_casesStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_profile import aws_profileStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_voiceid import aws_voiceidStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_wisdom import aws_wisdomStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_dlm import aws_dlmStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_datazone import aws_datazoneStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_datazonecontrol import aws_datazonecontrolStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_detective import aws_detectiveStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_devops_guru import aws_devops_guruStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_docdb_elastic import aws_docdb_elasticStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_dynamodb import aws_dynamodbStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_dax import aws_daxStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ec2 import aws_ec2Statement
from hangar_sdk.core.rbac.aws.iam_types.aws_autoscaling import aws_autoscalingStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_imagebuilder import aws_imagebuilderStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ec2_instance_connect import aws_ec2_instance_connectStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_eks_auth import aws_eks_authStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_elasticache import aws_elasticacheStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ebs import aws_ebsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ecr import aws_ecrStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ecr_public import aws_ecr_publicStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ecs import aws_ecsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_elasticfilesystem import aws_elasticfilesystemStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_elastic_inference import aws_elastic_inferenceStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_eks import aws_eksStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_elasticmapreduce import aws_elasticmapreduceStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_elastictranscoder import aws_elastictranscoderStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_emr_containers import aws_emr_containersStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_emr_serverless import aws_emr_serverlessStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_events import aws_eventsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_pipes import aws_pipesStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_scheduler import aws_schedulerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_schemas import aws_schemasStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_finspace import aws_finspaceStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_finspace_api import aws_finspace_apiStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_forecast import aws_forecastStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_frauddetector import aws_frauddetectorStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_freertos import aws_freertosStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_fsx import aws_fsxStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_gamelift import aws_gameliftStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_gamesparks import aws_gamesparksStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_glacier import aws_glacierStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_groundtruthlabeling import aws_groundtruthlabelingStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_guardduty import aws_guarddutyStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_healthlake import aws_healthlakeStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_honeycode import aws_honeycodeStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_inspector import aws_inspectorStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_inspector2 import aws_inspector2Statement
from hangar_sdk.core.rbac.aws.iam_types.aws_inspector_scan import aws_inspector_scanStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ivs import aws_ivsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ivschat import aws_ivschatStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_kendra import aws_kendraStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_kendra_ranking import aws_kendra_rankingStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_cassandra import aws_cassandraStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_kinesis import aws_kinesisStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_kinesisanalytics import aws_kinesisanalyticsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_firehose import aws_firehoseStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_kinesisvideo import aws_kinesisvideoStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_lex import aws_lexStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_lightsail import aws_lightsailStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_geo import aws_geoStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_lookoutequipment import aws_lookoutequipmentStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_lookoutmetrics import aws_lookoutmetricsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_lookoutvision import aws_lookoutvisionStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_machinelearning import aws_machinelearningStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_macie2 import aws_macie2Statement
from hangar_sdk.core.rbac.aws.iam_types.aws_macie import aws_macieStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_managedblockchain import aws_managedblockchainStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_managedblockchain_query import aws_managedblockchain_queryStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_grafana import aws_grafanaStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_aps import aws_apsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_kafka import aws_kafkaStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_kafkaconnect import aws_kafkaconnectStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_airflow import aws_airflowStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_mechanicalturk import aws_mechanicalturkStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_mediaimport import aws_mediaimportStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_memorydb import aws_memorydbStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ec2messages import aws_ec2messagesStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_mobileanalytics import aws_mobileanalyticsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_monitron import aws_monitronStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_mq import aws_mqStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_neptune_db import aws_neptune_dbStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_neptune_graph import aws_neptune_graphStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_nimble import aws_nimbleStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_omics import aws_omicsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_one import aws_oneStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_osis import aws_osisStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_aoss import aws_aossStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_es import aws_esStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_personalize import aws_personalizeStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_mobiletargeting import aws_mobiletargetingStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ses import aws_sesStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_sms_voice import aws_sms_voiceStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_polly import aws_pollyStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_q import aws_qStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_qbusiness import aws_qbusinessStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_qldb import aws_qldbStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_quicksight import aws_quicksightStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_rds import aws_rdsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_rds_data import aws_rds_dataStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_rds_db import aws_rds_dbStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_redshift import aws_redshiftStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_redshift_data import aws_redshift_dataStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_redshift_serverless import aws_redshift_serverlessStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_rekognition import aws_rekognitionStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_tag import aws_tagStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_rhelkb import aws_rhelkbStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_route53 import aws_route53Statement
from hangar_sdk.core.rbac.aws.iam_types.aws_arc_zonal_shift import aws_arc_zonal_shiftStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_route53domains import aws_route53domainsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_route53_recovery_cluster import aws_route53_recovery_clusterStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_route53_recovery_control_config import aws_route53_recovery_control_configStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_route53_recovery_readiness import aws_route53_recovery_readinessStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_route53resolver import aws_route53resolverStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_s3 import aws_s3Statement
from hangar_sdk.core.rbac.aws.iam_types.aws_s3express import aws_s3expressStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_s3_object_lambda import aws_s3_object_lambdaStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_s3_outposts import aws_s3_outpostsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_sagemaker import aws_sagemakerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_sagemaker_geospatial import aws_sagemaker_geospatialStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_sagemaker_groundtruth_synthetic import aws_sagemaker_groundtruth_syntheticStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_securitylake import aws_securitylakeStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ssmmessages import aws_ssmmessagesStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_sdb import aws_sdbStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_swf import aws_swfStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_sns import aws_snsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_sqs import aws_sqsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_storagegateway import aws_storagegatewayStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_sumerian import aws_sumerianStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_textract import aws_textractStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_timestream import aws_timestreamStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_transcribe import aws_transcribeStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_translate import aws_translateStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_verifiedpermissions import aws_verifiedpermissionsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_vpc_lattice import aws_vpc_latticeStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_vpc_lattice_svcs import aws_vpc_lattice_svcsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_workdocs import aws_workdocsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_worklink import aws_worklinkStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_workmail import aws_workmailStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_workmailmessageflow import aws_workmailmessageflowStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_workspaces import aws_workspacesStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_wam import aws_wamStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_thinclient import aws_thinclientStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_workspaces_web import aws_workspaces_webStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_kafka_cluster import aws_kafka_clusterStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_discovery import aws_discoveryStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_arsenal import aws_arsenalStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_account import aws_accountStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_activate import aws_activateStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_amplify import aws_amplifyStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_amplifybackend import aws_amplifybackendStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_amplifyuibuilder import aws_amplifyuibuilderStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_a2c import aws_a2cStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_appconfig import aws_appconfigStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_appfabric import aws_appfabricStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_application_autoscaling import aws_application_autoscalingStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_application_cost_profiler import aws_application_cost_profilerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_mgn import aws_mgnStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_application_transformation import aws_application_transformationStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_appmesh import aws_appmeshStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_appmesh_preview import aws_appmesh_previewStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_apprunner import aws_apprunnerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_appsync import aws_appsyncStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_artifact import aws_artifactStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_auditmanager import aws_auditmanagerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_autoscaling_plans import aws_autoscaling_plansStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_b2bi import aws_b2biStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_backup import aws_backupStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_backup_gateway import aws_backup_gatewayStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_backup_storage import aws_backup_storageStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_batch import aws_batchStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_billing import aws_billingStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_bcm_data_exports import aws_bcm_data_exportsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_billingconductor import aws_billingconductorStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_aws_portal import aws_aws_portalStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_budgets import aws_budgetsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_bugbust import aws_bugbustStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_acm import aws_acmStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_acm_pca import aws_acm_pcaStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_chatbot import aws_chatbotStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_cleanrooms import aws_cleanroomsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_cleanrooms_ml import aws_cleanrooms_mlStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_cloud9 import aws_cloud9Statement
from hangar_sdk.core.rbac.aws.iam_types.aws_cloudformation import aws_cloudformationStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_cloudhsm import aws_cloudhsmStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_servicediscovery import aws_servicediscoveryStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_cloudshell import aws_cloudshellStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_cloudtrail import aws_cloudtrailStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_cloudtrail_data import aws_cloudtrail_dataStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_rum import aws_rumStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_codeartifact import aws_codeartifactStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_codebuild import aws_codebuildStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_codecommit import aws_codecommitStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_codedeploy import aws_codedeployStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_codedeploy_commands_secure import aws_codedeploy_commands_secureStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_codepipeline import aws_codepipelineStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_codestar import aws_codestarStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_codestar_connections import aws_codestar_connectionsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_codestar_notifications import aws_codestar_notificationsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_compute_optimizer import aws_compute_optimizerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_config import aws_configStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_awsconnector import aws_awsconnectorStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_consoleapp import aws_consoleappStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_consolidatedbilling import aws_consolidatedbillingStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_controltower import aws_controltowerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_cur import aws_curStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ce import aws_ceStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_cost_optimization_hub import aws_cost_optimization_hubStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_customer_verification import aws_customer_verificationStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_dms import aws_dmsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_dataexchange import aws_dataexchangeStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_datapipeline import aws_datapipelineStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_datasync import aws_datasyncStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_deepcomposer import aws_deepcomposerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_deeplens import aws_deeplensStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_deepracer import aws_deepracerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_devicefarm import aws_devicefarmStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ts import aws_tsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_directconnect import aws_directconnectStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ds import aws_dsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_elasticbeanstalk import aws_elasticbeanstalkStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_drs import aws_drsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_elasticloadbalancing import aws_elasticloadbalancingStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_elemental_appliances_software import aws_elemental_appliances_softwareStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_elemental_activations import aws_elemental_activationsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_mediaconnect import aws_mediaconnectStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_mediaconvert import aws_mediaconvertStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_medialive import aws_medialiveStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_mediapackage import aws_mediapackageStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_mediapackagev2 import aws_mediapackagev2Statement
from hangar_sdk.core.rbac.aws.iam_types.aws_mediapackage_vod import aws_mediapackage_vodStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_mediastore import aws_mediastoreStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_mediatailor import aws_mediatailorStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_elemental_support_cases import aws_elemental_support_casesStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_elemental_support_content import aws_elemental_support_contentStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_entityresolution import aws_entityresolutionStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_fis import aws_fisStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_fms import aws_fmsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_freetier import aws_freetierStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_globalaccelerator import aws_globalacceleratorStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_glue import aws_glueStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_databrew import aws_databrewStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_groundstation import aws_groundstationStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_health import aws_healthStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_medical_imaging import aws_medical_imagingStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_access_analyzer import aws_access_analyzerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_sso_oauth import aws_sso_oauthStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_sso import aws_ssoStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_sso_directory import aws_sso_directoryStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_iam import aws_iamStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_rolesanywhere import aws_rolesanywhereStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_identitystore import aws_identitystoreStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_identitystore_auth import aws_identitystore_authStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_identity_sync import aws_identity_syncStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_importexport import aws_importexportStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_invoicing import aws_invoicingStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_iot import aws_iotStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_iot1click import aws_iot1clickStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_iotanalytics import aws_iotanalyticsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_iotdeviceadvisor import aws_iotdeviceadvisorStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_iotwireless import aws_iotwirelessStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_iot_device_tester import aws_iot_device_testerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_iotevents import aws_ioteventsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_iotfleethub import aws_iotfleethubStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_iotfleetwise import aws_iotfleetwiseStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_greengrass import aws_greengrassStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_iotjobsdata import aws_iotjobsdataStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_iotroborunner import aws_iotroborunnerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_iotsitewise import aws_iotsitewiseStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_iotthingsgraph import aws_iotthingsgraphStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_iottwinmaker import aws_iottwinmakerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_iq import aws_iqStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_iq_permission import aws_iq_permissionStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_kms import aws_kmsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_lakeformation import aws_lakeformationStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_lambda import aws_lambdaStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_launchwizard import aws_launchwizardStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_license_manager import aws_license_managerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_license_manager_linux_subscriptions import aws_license_manager_linux_subscriptionsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_license_manager_user_subscriptions import aws_license_manager_user_subscriptionsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_m2 import aws_m2Statement
from hangar_sdk.core.rbac.aws.iam_types.aws_aws_marketplace import aws_aws_marketplaceStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_marketplacecommerceanalytics import aws_marketplacecommerceanalyticsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_aws_marketplace_management import aws_aws_marketplace_managementStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_vendor_insights import aws_vendor_insightsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_serviceextract import aws_serviceextractStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_mapcredits import aws_mapcreditsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_mgh import aws_mghStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_migrationhub_orchestrator import aws_migrationhub_orchestratorStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_refactor_spaces import aws_refactor_spacesStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_migrationhub_strategy import aws_migrationhub_strategyStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_mobilehub import aws_mobilehubStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_network_firewall import aws_network_firewallStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_networkmanager import aws_networkmanagerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_networkmanager_chat import aws_networkmanager_chatStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_opsworks import aws_opsworksStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_opsworks_cm import aws_opsworks_cmStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_organizations import aws_organizationsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_outposts import aws_outpostsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_panorama import aws_panoramaStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_partnercentral_account_management import aws_partnercentral_account_managementStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_payment_cryptography import aws_payment_cryptographyStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_payments import aws_paymentsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_pi import aws_piStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_pricing import aws_pricingStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_pca_connector_ad import aws_pca_connector_adStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_proton import aws_protonStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_purchase_orders import aws_purchase_ordersStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_repostspace import aws_repostspaceStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_rbin import aws_rbinStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_resiliencehub import aws_resiliencehubStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ram import aws_ramStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_resource_explorer_2 import aws_resource_explorer_2Statement
from hangar_sdk.core.rbac.aws.iam_types.aws_resource_groups import aws_resource_groupsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_robomaker import aws_robomakerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_savingsplans import aws_savingsplansStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_secretsmanager import aws_secretsmanagerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_securityhub import aws_securityhubStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_sts import aws_stsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_serverlessrepo import aws_serverlessrepoStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_sms import aws_smsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_servicecatalog import aws_servicecatalogStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_private_networks import aws_private_networksStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_shield import aws_shieldStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_signer import aws_signerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_simspaceweaver import aws_simspaceweaverStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_snowball import aws_snowballStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_snow_device_management import aws_snow_device_managementStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_sqlworkbench import aws_sqlworkbenchStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_states import aws_statesStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_scn import aws_scnStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_support import aws_supportStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_supportapp import aws_supportappStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_supportplans import aws_supportplansStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_sustainability import aws_sustainabilityStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ssm import aws_ssmStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ssm_sap import aws_ssm_sapStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ssm_guiconnect import aws_ssm_guiconnectStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ssm_incidents import aws_ssm_incidentsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_ssm_contacts import aws_ssm_contactsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_resource_explorer import aws_resource_explorerStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_tax import aws_taxStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_tnb import aws_tnbStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_tiros import aws_tirosStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_transfer import aws_transferStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_trustedadvisor import aws_trustedadvisorStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_notifications import aws_notificationsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_notifications_contacts import aws_notifications_contactsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_verified_access import aws_verified_accessStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_waf import aws_wafStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_waf_regional import aws_waf_regionalStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_wafv2 import aws_wafv2Statement
from hangar_sdk.core.rbac.aws.iam_types.aws_wellarchitected import aws_wellarchitectedStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_wickr import aws_wickrStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_xray import aws_xrayStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_dbqms import aws_dbqmsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_connect_campaigns import aws_connect_campaignsStatement
from hangar_sdk.core.rbac.aws.iam_types.aws_servicequotas import aws_servicequotasStatement
from typing import List
from hangar_sdk.core.rbac.aws.base_type import Policy
from hangar_sdk.resources.terraform import AbstractTerraformResource

class Statement():

    def __init__(self, policy: Policy):
        self.policy = policy
    
    
    def aws_policy_sentry_schema_version(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_policy_sentry_schema_versionStatement:
        return aws_policy_sentry_schema_versionStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_a4b(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_a4bStatement:
        return aws_a4bStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_execute_api(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_execute_apiStatement:
        return aws_execute_apiStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_apigateway(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_apigatewayStatement:
        return aws_apigatewayStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_appflow(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_appflowStatement:
        return aws_appflowStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_app_integrations(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_app_integrationsStatement:
        return aws_app_integrationsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_appstream(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_appstreamStatement:
        return aws_appstreamStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_athena(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_athenaStatement:
        return aws_athenaStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_bedrock(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_bedrockStatement:
        return aws_bedrockStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_braket(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_braketStatement:
        return aws_braketStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_chime(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_chimeStatement:
        return aws_chimeStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_clouddirectory(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_clouddirectoryStatement:
        return aws_clouddirectoryStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_cloudfront(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_cloudfrontStatement:
        return aws_cloudfrontStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_cloudfront_keyvaluestore(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_cloudfront_keyvaluestoreStatement:
        return aws_cloudfront_keyvaluestoreStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_cloudsearch(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_cloudsearchStatement:
        return aws_cloudsearchStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_cloudwatch(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_cloudwatchStatement:
        return aws_cloudwatchStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_applicationinsights(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_applicationinsightsStatement:
        return aws_applicationinsightsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_evidently(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_evidentlyStatement:
        return aws_evidentlyStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_internetmonitor(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_internetmonitorStatement:
        return aws_internetmonitorStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_logs(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_logsStatement:
        return aws_logsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_networkmonitor(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_networkmonitorStatement:
        return aws_networkmonitorStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_oam(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_oamStatement:
        return aws_oamStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_synthetics(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_syntheticsStatement:
        return aws_syntheticsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_codecatalyst(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_codecatalystStatement:
        return aws_codecatalystStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_codeguru(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_codeguruStatement:
        return aws_codeguruStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_codeguru_profiler(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_codeguru_profilerStatement:
        return aws_codeguru_profilerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_codeguru_reviewer(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_codeguru_reviewerStatement:
        return aws_codeguru_reviewerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_codeguru_security(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_codeguru_securityStatement:
        return aws_codeguru_securityStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_codewhisperer(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_codewhispererStatement:
        return aws_codewhispererStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_cognito_identity(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_cognito_identityStatement:
        return aws_cognito_identityStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_cognito_sync(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_cognito_syncStatement:
        return aws_cognito_syncStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_cognito_idp(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_cognito_idpStatement:
        return aws_cognito_idpStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_comprehend(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_comprehendStatement:
        return aws_comprehendStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_comprehendmedical(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_comprehendmedicalStatement:
        return aws_comprehendmedicalStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_connect(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_connectStatement:
        return aws_connectStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_cases(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_casesStatement:
        return aws_casesStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_profile(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_profileStatement:
        return aws_profileStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_voiceid(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_voiceidStatement:
        return aws_voiceidStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_wisdom(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_wisdomStatement:
        return aws_wisdomStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_dlm(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_dlmStatement:
        return aws_dlmStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_datazone(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_datazoneStatement:
        return aws_datazoneStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_datazonecontrol(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_datazonecontrolStatement:
        return aws_datazonecontrolStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_detective(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_detectiveStatement:
        return aws_detectiveStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_devops_guru(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_devops_guruStatement:
        return aws_devops_guruStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_docdb_elastic(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_docdb_elasticStatement:
        return aws_docdb_elasticStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_dynamodb(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_dynamodbStatement:
        return aws_dynamodbStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_dax(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_daxStatement:
        return aws_daxStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ec2(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ec2Statement:
        return aws_ec2Statement(policy=self.policy, arns=arns, resources=resources)


    def aws_autoscaling(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_autoscalingStatement:
        return aws_autoscalingStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_imagebuilder(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_imagebuilderStatement:
        return aws_imagebuilderStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ec2_instance_connect(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ec2_instance_connectStatement:
        return aws_ec2_instance_connectStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_eks_auth(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_eks_authStatement:
        return aws_eks_authStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_elasticache(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_elasticacheStatement:
        return aws_elasticacheStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ebs(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ebsStatement:
        return aws_ebsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ecr(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ecrStatement:
        return aws_ecrStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ecr_public(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ecr_publicStatement:
        return aws_ecr_publicStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ecs(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ecsStatement:
        return aws_ecsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_elasticfilesystem(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_elasticfilesystemStatement:
        return aws_elasticfilesystemStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_elastic_inference(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_elastic_inferenceStatement:
        return aws_elastic_inferenceStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_eks(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_eksStatement:
        return aws_eksStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_elasticmapreduce(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_elasticmapreduceStatement:
        return aws_elasticmapreduceStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_elastictranscoder(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_elastictranscoderStatement:
        return aws_elastictranscoderStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_emr_containers(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_emr_containersStatement:
        return aws_emr_containersStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_emr_serverless(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_emr_serverlessStatement:
        return aws_emr_serverlessStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_events(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_eventsStatement:
        return aws_eventsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_pipes(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_pipesStatement:
        return aws_pipesStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_scheduler(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_schedulerStatement:
        return aws_schedulerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_schemas(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_schemasStatement:
        return aws_schemasStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_finspace(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_finspaceStatement:
        return aws_finspaceStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_finspace_api(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_finspace_apiStatement:
        return aws_finspace_apiStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_forecast(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_forecastStatement:
        return aws_forecastStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_frauddetector(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_frauddetectorStatement:
        return aws_frauddetectorStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_freertos(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_freertosStatement:
        return aws_freertosStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_fsx(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_fsxStatement:
        return aws_fsxStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_gamelift(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_gameliftStatement:
        return aws_gameliftStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_gamesparks(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_gamesparksStatement:
        return aws_gamesparksStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_glacier(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_glacierStatement:
        return aws_glacierStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_groundtruthlabeling(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_groundtruthlabelingStatement:
        return aws_groundtruthlabelingStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_guardduty(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_guarddutyStatement:
        return aws_guarddutyStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_healthlake(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_healthlakeStatement:
        return aws_healthlakeStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_honeycode(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_honeycodeStatement:
        return aws_honeycodeStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_inspector(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_inspectorStatement:
        return aws_inspectorStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_inspector2(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_inspector2Statement:
        return aws_inspector2Statement(policy=self.policy, arns=arns, resources=resources)


    def aws_inspector_scan(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_inspector_scanStatement:
        return aws_inspector_scanStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ivs(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ivsStatement:
        return aws_ivsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ivschat(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ivschatStatement:
        return aws_ivschatStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_kendra(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_kendraStatement:
        return aws_kendraStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_kendra_ranking(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_kendra_rankingStatement:
        return aws_kendra_rankingStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_cassandra(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_cassandraStatement:
        return aws_cassandraStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_kinesis(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_kinesisStatement:
        return aws_kinesisStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_kinesisanalytics(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_kinesisanalyticsStatement:
        return aws_kinesisanalyticsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_firehose(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_firehoseStatement:
        return aws_firehoseStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_kinesisvideo(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_kinesisvideoStatement:
        return aws_kinesisvideoStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_lex(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_lexStatement:
        return aws_lexStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_lightsail(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_lightsailStatement:
        return aws_lightsailStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_geo(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_geoStatement:
        return aws_geoStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_lookoutequipment(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_lookoutequipmentStatement:
        return aws_lookoutequipmentStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_lookoutmetrics(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_lookoutmetricsStatement:
        return aws_lookoutmetricsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_lookoutvision(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_lookoutvisionStatement:
        return aws_lookoutvisionStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_machinelearning(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_machinelearningStatement:
        return aws_machinelearningStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_macie2(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_macie2Statement:
        return aws_macie2Statement(policy=self.policy, arns=arns, resources=resources)


    def aws_macie(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_macieStatement:
        return aws_macieStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_managedblockchain(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_managedblockchainStatement:
        return aws_managedblockchainStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_managedblockchain_query(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_managedblockchain_queryStatement:
        return aws_managedblockchain_queryStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_grafana(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_grafanaStatement:
        return aws_grafanaStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_aps(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_apsStatement:
        return aws_apsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_kafka(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_kafkaStatement:
        return aws_kafkaStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_kafkaconnect(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_kafkaconnectStatement:
        return aws_kafkaconnectStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_airflow(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_airflowStatement:
        return aws_airflowStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_mechanicalturk(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_mechanicalturkStatement:
        return aws_mechanicalturkStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_mediaimport(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_mediaimportStatement:
        return aws_mediaimportStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_memorydb(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_memorydbStatement:
        return aws_memorydbStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ec2messages(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ec2messagesStatement:
        return aws_ec2messagesStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_mobileanalytics(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_mobileanalyticsStatement:
        return aws_mobileanalyticsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_monitron(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_monitronStatement:
        return aws_monitronStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_mq(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_mqStatement:
        return aws_mqStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_neptune_db(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_neptune_dbStatement:
        return aws_neptune_dbStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_neptune_graph(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_neptune_graphStatement:
        return aws_neptune_graphStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_nimble(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_nimbleStatement:
        return aws_nimbleStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_omics(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_omicsStatement:
        return aws_omicsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_one(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_oneStatement:
        return aws_oneStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_osis(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_osisStatement:
        return aws_osisStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_aoss(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_aossStatement:
        return aws_aossStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_es(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_esStatement:
        return aws_esStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_personalize(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_personalizeStatement:
        return aws_personalizeStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_mobiletargeting(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_mobiletargetingStatement:
        return aws_mobiletargetingStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ses(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_sesStatement:
        return aws_sesStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_sms_voice(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_sms_voiceStatement:
        return aws_sms_voiceStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_polly(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_pollyStatement:
        return aws_pollyStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_q(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_qStatement:
        return aws_qStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_qbusiness(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_qbusinessStatement:
        return aws_qbusinessStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_qldb(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_qldbStatement:
        return aws_qldbStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_quicksight(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_quicksightStatement:
        return aws_quicksightStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_rds(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_rdsStatement:
        return aws_rdsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_rds_data(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_rds_dataStatement:
        return aws_rds_dataStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_rds_db(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_rds_dbStatement:
        return aws_rds_dbStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_redshift(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_redshiftStatement:
        return aws_redshiftStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_redshift_data(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_redshift_dataStatement:
        return aws_redshift_dataStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_redshift_serverless(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_redshift_serverlessStatement:
        return aws_redshift_serverlessStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_rekognition(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_rekognitionStatement:
        return aws_rekognitionStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_tag(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_tagStatement:
        return aws_tagStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_rhelkb(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_rhelkbStatement:
        return aws_rhelkbStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_route53(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_route53Statement:
        return aws_route53Statement(policy=self.policy, arns=arns, resources=resources)


    def aws_arc_zonal_shift(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_arc_zonal_shiftStatement:
        return aws_arc_zonal_shiftStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_route53domains(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_route53domainsStatement:
        return aws_route53domainsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_route53_recovery_cluster(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_route53_recovery_clusterStatement:
        return aws_route53_recovery_clusterStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_route53_recovery_control_config(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_route53_recovery_control_configStatement:
        return aws_route53_recovery_control_configStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_route53_recovery_readiness(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_route53_recovery_readinessStatement:
        return aws_route53_recovery_readinessStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_route53resolver(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_route53resolverStatement:
        return aws_route53resolverStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_s3(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_s3Statement:
        return aws_s3Statement(policy=self.policy, arns=arns, resources=resources)


    def aws_s3express(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_s3expressStatement:
        return aws_s3expressStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_s3_object_lambda(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_s3_object_lambdaStatement:
        return aws_s3_object_lambdaStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_s3_outposts(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_s3_outpostsStatement:
        return aws_s3_outpostsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_sagemaker(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_sagemakerStatement:
        return aws_sagemakerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_sagemaker_geospatial(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_sagemaker_geospatialStatement:
        return aws_sagemaker_geospatialStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_sagemaker_groundtruth_synthetic(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_sagemaker_groundtruth_syntheticStatement:
        return aws_sagemaker_groundtruth_syntheticStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_securitylake(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_securitylakeStatement:
        return aws_securitylakeStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ssmmessages(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ssmmessagesStatement:
        return aws_ssmmessagesStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_sdb(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_sdbStatement:
        return aws_sdbStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_swf(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_swfStatement:
        return aws_swfStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_sns(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_snsStatement:
        return aws_snsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_sqs(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_sqsStatement:
        return aws_sqsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_storagegateway(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_storagegatewayStatement:
        return aws_storagegatewayStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_sumerian(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_sumerianStatement:
        return aws_sumerianStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_textract(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_textractStatement:
        return aws_textractStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_timestream(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_timestreamStatement:
        return aws_timestreamStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_transcribe(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_transcribeStatement:
        return aws_transcribeStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_translate(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_translateStatement:
        return aws_translateStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_verifiedpermissions(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_verifiedpermissionsStatement:
        return aws_verifiedpermissionsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_vpc_lattice(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_vpc_latticeStatement:
        return aws_vpc_latticeStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_vpc_lattice_svcs(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_vpc_lattice_svcsStatement:
        return aws_vpc_lattice_svcsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_workdocs(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_workdocsStatement:
        return aws_workdocsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_worklink(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_worklinkStatement:
        return aws_worklinkStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_workmail(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_workmailStatement:
        return aws_workmailStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_workmailmessageflow(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_workmailmessageflowStatement:
        return aws_workmailmessageflowStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_workspaces(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_workspacesStatement:
        return aws_workspacesStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_wam(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_wamStatement:
        return aws_wamStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_thinclient(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_thinclientStatement:
        return aws_thinclientStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_workspaces_web(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_workspaces_webStatement:
        return aws_workspaces_webStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_kafka_cluster(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_kafka_clusterStatement:
        return aws_kafka_clusterStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_discovery(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_discoveryStatement:
        return aws_discoveryStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_arsenal(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_arsenalStatement:
        return aws_arsenalStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_account(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_accountStatement:
        return aws_accountStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_activate(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_activateStatement:
        return aws_activateStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_amplify(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_amplifyStatement:
        return aws_amplifyStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_amplifybackend(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_amplifybackendStatement:
        return aws_amplifybackendStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_amplifyuibuilder(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_amplifyuibuilderStatement:
        return aws_amplifyuibuilderStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_a2c(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_a2cStatement:
        return aws_a2cStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_appconfig(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_appconfigStatement:
        return aws_appconfigStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_appfabric(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_appfabricStatement:
        return aws_appfabricStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_application_autoscaling(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_application_autoscalingStatement:
        return aws_application_autoscalingStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_application_cost_profiler(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_application_cost_profilerStatement:
        return aws_application_cost_profilerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_mgn(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_mgnStatement:
        return aws_mgnStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_application_transformation(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_application_transformationStatement:
        return aws_application_transformationStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_appmesh(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_appmeshStatement:
        return aws_appmeshStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_appmesh_preview(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_appmesh_previewStatement:
        return aws_appmesh_previewStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_apprunner(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_apprunnerStatement:
        return aws_apprunnerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_appsync(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_appsyncStatement:
        return aws_appsyncStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_artifact(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_artifactStatement:
        return aws_artifactStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_auditmanager(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_auditmanagerStatement:
        return aws_auditmanagerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_autoscaling_plans(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_autoscaling_plansStatement:
        return aws_autoscaling_plansStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_b2bi(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_b2biStatement:
        return aws_b2biStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_backup(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_backupStatement:
        return aws_backupStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_backup_gateway(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_backup_gatewayStatement:
        return aws_backup_gatewayStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_backup_storage(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_backup_storageStatement:
        return aws_backup_storageStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_batch(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_batchStatement:
        return aws_batchStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_billing(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_billingStatement:
        return aws_billingStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_bcm_data_exports(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_bcm_data_exportsStatement:
        return aws_bcm_data_exportsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_billingconductor(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_billingconductorStatement:
        return aws_billingconductorStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_aws_portal(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_aws_portalStatement:
        return aws_aws_portalStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_budgets(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_budgetsStatement:
        return aws_budgetsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_bugbust(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_bugbustStatement:
        return aws_bugbustStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_acm(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_acmStatement:
        return aws_acmStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_acm_pca(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_acm_pcaStatement:
        return aws_acm_pcaStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_chatbot(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_chatbotStatement:
        return aws_chatbotStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_cleanrooms(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_cleanroomsStatement:
        return aws_cleanroomsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_cleanrooms_ml(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_cleanrooms_mlStatement:
        return aws_cleanrooms_mlStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_cloud9(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_cloud9Statement:
        return aws_cloud9Statement(policy=self.policy, arns=arns, resources=resources)


    def aws_cloudformation(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_cloudformationStatement:
        return aws_cloudformationStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_cloudhsm(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_cloudhsmStatement:
        return aws_cloudhsmStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_servicediscovery(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_servicediscoveryStatement:
        return aws_servicediscoveryStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_cloudshell(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_cloudshellStatement:
        return aws_cloudshellStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_cloudtrail(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_cloudtrailStatement:
        return aws_cloudtrailStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_cloudtrail_data(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_cloudtrail_dataStatement:
        return aws_cloudtrail_dataStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_rum(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_rumStatement:
        return aws_rumStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_codeartifact(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_codeartifactStatement:
        return aws_codeartifactStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_codebuild(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_codebuildStatement:
        return aws_codebuildStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_codecommit(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_codecommitStatement:
        return aws_codecommitStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_codedeploy(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_codedeployStatement:
        return aws_codedeployStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_codedeploy_commands_secure(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_codedeploy_commands_secureStatement:
        return aws_codedeploy_commands_secureStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_codepipeline(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_codepipelineStatement:
        return aws_codepipelineStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_codestar(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_codestarStatement:
        return aws_codestarStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_codestar_connections(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_codestar_connectionsStatement:
        return aws_codestar_connectionsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_codestar_notifications(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_codestar_notificationsStatement:
        return aws_codestar_notificationsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_compute_optimizer(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_compute_optimizerStatement:
        return aws_compute_optimizerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_config(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_configStatement:
        return aws_configStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_awsconnector(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_awsconnectorStatement:
        return aws_awsconnectorStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_consoleapp(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_consoleappStatement:
        return aws_consoleappStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_consolidatedbilling(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_consolidatedbillingStatement:
        return aws_consolidatedbillingStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_controltower(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_controltowerStatement:
        return aws_controltowerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_cur(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_curStatement:
        return aws_curStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ce(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ceStatement:
        return aws_ceStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_cost_optimization_hub(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_cost_optimization_hubStatement:
        return aws_cost_optimization_hubStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_customer_verification(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_customer_verificationStatement:
        return aws_customer_verificationStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_dms(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_dmsStatement:
        return aws_dmsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_dataexchange(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_dataexchangeStatement:
        return aws_dataexchangeStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_datapipeline(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_datapipelineStatement:
        return aws_datapipelineStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_datasync(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_datasyncStatement:
        return aws_datasyncStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_deepcomposer(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_deepcomposerStatement:
        return aws_deepcomposerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_deeplens(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_deeplensStatement:
        return aws_deeplensStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_deepracer(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_deepracerStatement:
        return aws_deepracerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_devicefarm(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_devicefarmStatement:
        return aws_devicefarmStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ts(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_tsStatement:
        return aws_tsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_directconnect(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_directconnectStatement:
        return aws_directconnectStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ds(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_dsStatement:
        return aws_dsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_elasticbeanstalk(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_elasticbeanstalkStatement:
        return aws_elasticbeanstalkStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_drs(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_drsStatement:
        return aws_drsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_elasticloadbalancing(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_elasticloadbalancingStatement:
        return aws_elasticloadbalancingStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_elemental_appliances_software(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_elemental_appliances_softwareStatement:
        return aws_elemental_appliances_softwareStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_elemental_activations(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_elemental_activationsStatement:
        return aws_elemental_activationsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_mediaconnect(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_mediaconnectStatement:
        return aws_mediaconnectStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_mediaconvert(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_mediaconvertStatement:
        return aws_mediaconvertStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_medialive(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_medialiveStatement:
        return aws_medialiveStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_mediapackage(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_mediapackageStatement:
        return aws_mediapackageStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_mediapackagev2(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_mediapackagev2Statement:
        return aws_mediapackagev2Statement(policy=self.policy, arns=arns, resources=resources)


    def aws_mediapackage_vod(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_mediapackage_vodStatement:
        return aws_mediapackage_vodStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_mediastore(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_mediastoreStatement:
        return aws_mediastoreStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_mediatailor(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_mediatailorStatement:
        return aws_mediatailorStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_elemental_support_cases(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_elemental_support_casesStatement:
        return aws_elemental_support_casesStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_elemental_support_content(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_elemental_support_contentStatement:
        return aws_elemental_support_contentStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_entityresolution(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_entityresolutionStatement:
        return aws_entityresolutionStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_fis(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_fisStatement:
        return aws_fisStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_fms(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_fmsStatement:
        return aws_fmsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_freetier(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_freetierStatement:
        return aws_freetierStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_globalaccelerator(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_globalacceleratorStatement:
        return aws_globalacceleratorStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_glue(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_glueStatement:
        return aws_glueStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_databrew(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_databrewStatement:
        return aws_databrewStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_groundstation(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_groundstationStatement:
        return aws_groundstationStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_health(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_healthStatement:
        return aws_healthStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_medical_imaging(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_medical_imagingStatement:
        return aws_medical_imagingStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_access_analyzer(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_access_analyzerStatement:
        return aws_access_analyzerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_sso_oauth(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_sso_oauthStatement:
        return aws_sso_oauthStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_sso(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ssoStatement:
        return aws_ssoStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_sso_directory(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_sso_directoryStatement:
        return aws_sso_directoryStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_iam(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_iamStatement:
        return aws_iamStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_rolesanywhere(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_rolesanywhereStatement:
        return aws_rolesanywhereStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_identitystore(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_identitystoreStatement:
        return aws_identitystoreStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_identitystore_auth(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_identitystore_authStatement:
        return aws_identitystore_authStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_identity_sync(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_identity_syncStatement:
        return aws_identity_syncStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_importexport(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_importexportStatement:
        return aws_importexportStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_invoicing(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_invoicingStatement:
        return aws_invoicingStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_iot(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_iotStatement:
        return aws_iotStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_iot1click(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_iot1clickStatement:
        return aws_iot1clickStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_iotanalytics(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_iotanalyticsStatement:
        return aws_iotanalyticsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_iotdeviceadvisor(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_iotdeviceadvisorStatement:
        return aws_iotdeviceadvisorStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_iotwireless(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_iotwirelessStatement:
        return aws_iotwirelessStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_iot_device_tester(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_iot_device_testerStatement:
        return aws_iot_device_testerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_iotevents(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ioteventsStatement:
        return aws_ioteventsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_iotfleethub(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_iotfleethubStatement:
        return aws_iotfleethubStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_iotfleetwise(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_iotfleetwiseStatement:
        return aws_iotfleetwiseStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_greengrass(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_greengrassStatement:
        return aws_greengrassStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_iotjobsdata(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_iotjobsdataStatement:
        return aws_iotjobsdataStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_iotroborunner(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_iotroborunnerStatement:
        return aws_iotroborunnerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_iotsitewise(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_iotsitewiseStatement:
        return aws_iotsitewiseStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_iotthingsgraph(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_iotthingsgraphStatement:
        return aws_iotthingsgraphStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_iottwinmaker(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_iottwinmakerStatement:
        return aws_iottwinmakerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_iq(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_iqStatement:
        return aws_iqStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_iq_permission(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_iq_permissionStatement:
        return aws_iq_permissionStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_kms(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_kmsStatement:
        return aws_kmsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_lakeformation(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_lakeformationStatement:
        return aws_lakeformationStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_lambda(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_lambdaStatement:
        return aws_lambdaStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_launchwizard(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_launchwizardStatement:
        return aws_launchwizardStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_license_manager(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_license_managerStatement:
        return aws_license_managerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_license_manager_linux_subscriptions(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_license_manager_linux_subscriptionsStatement:
        return aws_license_manager_linux_subscriptionsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_license_manager_user_subscriptions(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_license_manager_user_subscriptionsStatement:
        return aws_license_manager_user_subscriptionsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_m2(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_m2Statement:
        return aws_m2Statement(policy=self.policy, arns=arns, resources=resources)


    def aws_aws_marketplace(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_aws_marketplaceStatement:
        return aws_aws_marketplaceStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_marketplacecommerceanalytics(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_marketplacecommerceanalyticsStatement:
        return aws_marketplacecommerceanalyticsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_aws_marketplace_management(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_aws_marketplace_managementStatement:
        return aws_aws_marketplace_managementStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_vendor_insights(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_vendor_insightsStatement:
        return aws_vendor_insightsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_serviceextract(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_serviceextractStatement:
        return aws_serviceextractStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_mapcredits(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_mapcreditsStatement:
        return aws_mapcreditsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_mgh(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_mghStatement:
        return aws_mghStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_migrationhub_orchestrator(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_migrationhub_orchestratorStatement:
        return aws_migrationhub_orchestratorStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_refactor_spaces(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_refactor_spacesStatement:
        return aws_refactor_spacesStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_migrationhub_strategy(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_migrationhub_strategyStatement:
        return aws_migrationhub_strategyStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_mobilehub(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_mobilehubStatement:
        return aws_mobilehubStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_network_firewall(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_network_firewallStatement:
        return aws_network_firewallStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_networkmanager(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_networkmanagerStatement:
        return aws_networkmanagerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_networkmanager_chat(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_networkmanager_chatStatement:
        return aws_networkmanager_chatStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_opsworks(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_opsworksStatement:
        return aws_opsworksStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_opsworks_cm(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_opsworks_cmStatement:
        return aws_opsworks_cmStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_organizations(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_organizationsStatement:
        return aws_organizationsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_outposts(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_outpostsStatement:
        return aws_outpostsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_panorama(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_panoramaStatement:
        return aws_panoramaStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_partnercentral_account_management(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_partnercentral_account_managementStatement:
        return aws_partnercentral_account_managementStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_payment_cryptography(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_payment_cryptographyStatement:
        return aws_payment_cryptographyStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_payments(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_paymentsStatement:
        return aws_paymentsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_pi(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_piStatement:
        return aws_piStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_pricing(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_pricingStatement:
        return aws_pricingStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_pca_connector_ad(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_pca_connector_adStatement:
        return aws_pca_connector_adStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_proton(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_protonStatement:
        return aws_protonStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_purchase_orders(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_purchase_ordersStatement:
        return aws_purchase_ordersStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_repostspace(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_repostspaceStatement:
        return aws_repostspaceStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_rbin(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_rbinStatement:
        return aws_rbinStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_resiliencehub(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_resiliencehubStatement:
        return aws_resiliencehubStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ram(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ramStatement:
        return aws_ramStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_resource_explorer_2(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_resource_explorer_2Statement:
        return aws_resource_explorer_2Statement(policy=self.policy, arns=arns, resources=resources)


    def aws_resource_groups(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_resource_groupsStatement:
        return aws_resource_groupsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_robomaker(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_robomakerStatement:
        return aws_robomakerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_savingsplans(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_savingsplansStatement:
        return aws_savingsplansStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_secretsmanager(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_secretsmanagerStatement:
        return aws_secretsmanagerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_securityhub(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_securityhubStatement:
        return aws_securityhubStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_sts(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_stsStatement:
        return aws_stsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_serverlessrepo(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_serverlessrepoStatement:
        return aws_serverlessrepoStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_sms(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_smsStatement:
        return aws_smsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_servicecatalog(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_servicecatalogStatement:
        return aws_servicecatalogStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_private_networks(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_private_networksStatement:
        return aws_private_networksStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_shield(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_shieldStatement:
        return aws_shieldStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_signer(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_signerStatement:
        return aws_signerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_simspaceweaver(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_simspaceweaverStatement:
        return aws_simspaceweaverStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_snowball(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_snowballStatement:
        return aws_snowballStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_snow_device_management(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_snow_device_managementStatement:
        return aws_snow_device_managementStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_sqlworkbench(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_sqlworkbenchStatement:
        return aws_sqlworkbenchStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_states(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_statesStatement:
        return aws_statesStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_scn(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_scnStatement:
        return aws_scnStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_support(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_supportStatement:
        return aws_supportStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_supportapp(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_supportappStatement:
        return aws_supportappStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_supportplans(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_supportplansStatement:
        return aws_supportplansStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_sustainability(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_sustainabilityStatement:
        return aws_sustainabilityStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ssm(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ssmStatement:
        return aws_ssmStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ssm_sap(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ssm_sapStatement:
        return aws_ssm_sapStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ssm_guiconnect(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ssm_guiconnectStatement:
        return aws_ssm_guiconnectStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ssm_incidents(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ssm_incidentsStatement:
        return aws_ssm_incidentsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_ssm_contacts(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_ssm_contactsStatement:
        return aws_ssm_contactsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_resource_explorer(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_resource_explorerStatement:
        return aws_resource_explorerStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_tax(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_taxStatement:
        return aws_taxStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_tnb(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_tnbStatement:
        return aws_tnbStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_tiros(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_tirosStatement:
        return aws_tirosStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_transfer(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_transferStatement:
        return aws_transferStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_trustedadvisor(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_trustedadvisorStatement:
        return aws_trustedadvisorStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_notifications(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_notificationsStatement:
        return aws_notificationsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_notifications_contacts(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_notifications_contactsStatement:
        return aws_notifications_contactsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_verified_access(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_verified_accessStatement:
        return aws_verified_accessStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_waf(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_wafStatement:
        return aws_wafStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_waf_regional(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_waf_regionalStatement:
        return aws_waf_regionalStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_wafv2(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_wafv2Statement:
        return aws_wafv2Statement(policy=self.policy, arns=arns, resources=resources)


    def aws_wellarchitected(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_wellarchitectedStatement:
        return aws_wellarchitectedStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_wickr(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_wickrStatement:
        return aws_wickrStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_xray(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_xrayStatement:
        return aws_xrayStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_dbqms(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_dbqmsStatement:
        return aws_dbqmsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_connect_campaigns(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_connect_campaignsStatement:
        return aws_connect_campaignsStatement(policy=self.policy, arns=arns, resources=resources)


    def aws_servicequotas(self, arns: List = [],  resources: List[AbstractTerraformResource] = None) -> aws_servicequotasStatement:
        return aws_servicequotasStatement(policy=self.policy, arns=arns, resources=resources)


import aioboto3
import boto3

def get_credentials():
    session = boto3.Session()
    return {
        "AccessKeyId": session.get_credentials().access_key,
        "SecretAccessKey": session.get_credentials().secret_key,
        "SessionToken": session.get_credentials().token,
    }

def get_account_id():
    pass

def aaws_session(credentials):
    return aioboto3.Session(
        aws_access_key_id=credentials["AccessKeyId"],
        aws_secret_access_key=credentials["SecretAccessKey"],
        aws_session_token=credentials["SessionToken"],
    )

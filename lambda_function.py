import json
import boto3
import os

s3 = boto3.client('s3')
bucket_name = os.environ['LOGGING_BUCKET']

def lambda_handler(event, context):
    repo_name = event['repository']['name']
    pull_request = event['pull_request']
    changes = pull_request['changes']
    
    log_entry = {
        'repository': repo_name,
        'changes': changes
    }
    
    s3.put_object(
        Bucket=bucket_name,
        Key=f"{repo_name}/{context.aws_request_id}.json",
        Body=json.dumps(log_entry),
        ContentType='application/json'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Log entry created successfully!')
    }

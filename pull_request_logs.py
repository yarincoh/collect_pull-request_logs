<<<<<<< HEAD
import json  # Import the JSON module to handle JSON data
import logging  # Import the logging module to log information
import os  # Import the OS module to access environment variables
import requests  # Import the requests module to make HTTP requests

# Retrieve the GitHub token from the environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
# Retrieve the name of the S3 bucket for logging from the environment variables
LOGGING_BUCKET = os.getenv('LOGGING_BUCKET')

def lambda_handler(event, context):
    """
    AWS Lambda handler function to process the GitHub webhook event.
    This function is triggered by an HTTP request from the GitHub webhook.
    """
    # Parse the incoming event payload from GitHub (assumed to be JSON)
    body = json.loads(event['body'])
    
    # Check if the event is for a merged pull request
    if 'pull_request' in body and body['action'] == 'closed' and body['pull_request']['merged']:
        # Extract the repository name from the event payload
        repo_name = body['repository']['full_name']
        # Extract the pull request number from the event payload
        pr_number = body['pull_request']['number']
        # Log the processing of the merged pull request
        logging.info(f"Processing merged PR #{pr_number} in repository {repo_name}")
        
        # Get the list of changed files in the merged pull request
        changed_files = get_changed_files(repo_name, pr_number)
        
        # Log the repository name and changed files
        log_info(repo_name, changed_files)
        
    # Return a successful HTTP response
    return {
        'statusCode': 200,
        'body': json.dumps('Processed successfully!')
    }

def get_changed_files(repo_name, pr_number):
    """
    Get the list of files changed in the specified pull request.
    """
    # Construct the GitHub API URL to get the files changed in the pull request
    url = f"https://api.github.com/repos/{repo_name}/pulls/{pr_number}/files"
    # Set the authorization header with the GitHub token
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    # Make the HTTP GET request to the GitHub API
    response = requests.get(url, headers=headers)
    # Parse the JSON response to get the list of files
    files = response.json()
    
    # Initialize an empty list to store the changed file names
    changed_files = []
    for file in files:
        # Add the file name to the list
        changed_files.append(file['filename'])
        
    # Return the list of changed file names
    return changed_files

def log_info(repo_name, changed_files):
    """
    Log the repository name and changed files.
    """
    # Log the repository name
    logging.info(f"Repository: {repo_name}")
    # Log the list of changed files
    logging.info(f"Changed files: {', '.join(changed_files)}")

    # Optionally, save the log to an S3 bucket
    import boto3  # Import the Boto3 library to interact with AWS services
    # Create an S3 client
    s3 = boto3.client('s3')
    # Create the log content as a dictionary
    log_content = {
        'repository': repo_name,
        'changed_files': changed_files
    }
    # Save the log content as a JSON object in the specified S3 bucket
    s3.put_object(Bucket=LOGGING_BUCKET, Key=f'logs/{repo_name}/{context.aws_request_id}.json', Body=json.dumps(log_content))

=======
import json  # Import the JSON module to handle JSON data
import logging  # Import the logging module to log information
import os  # Import the OS module to access environment variables
import requests  # Import the requests module to make HTTP requests

# Retrieve the GitHub token from the environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
# Retrieve the name of the S3 bucket for logging from the environment variables
LOGGING_BUCKET = os.getenv('LOGGING_BUCKET')

def lambda_handler(event, context):
    """
    AWS Lambda handler function to process the GitHub webhook event.
    This function is triggered by an HTTP request from the GitHub webhook.
    """
    # Parse the incoming event payload from GitHub (assumed to be JSON)
    body = json.loads(event['body'])
    
    # Check if the event is for a merged pull request
    if 'pull_request' in body and body['action'] == 'closed' and body['pull_request']['merged']:
        # Extract the repository name from the event payload
        repo_name = body['repository']['full_name']
        # Extract the pull request number from the event payload
        pr_number = body['pull_request']['number']
        # Log the processing of the merged pull request
        logging.info(f"Processing merged PR #{pr_number} in repository {repo_name}")
        
        # Get the list of changed files in the merged pull request
        changed_files = get_changed_files(repo_name, pr_number)
        
        # Log the repository name and changed files
        log_info(repo_name, changed_files)
        
    # Return a successful HTTP response
    return {
        'statusCode': 200,
        'body': json.dumps('Processed successfully!')
    }

def get_changed_files(repo_name, pr_number):
    """
    Get the list of files changed in the specified pull request.
    """
    # Construct the GitHub API URL to get the files changed in the pull request
    url = f"https://api.github.com/repos/{repo_name}/pulls/{pr_number}/files"
    # Set the authorization header with the GitHub token
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    # Make the HTTP GET request to the GitHub API
    response = requests.get(url, headers=headers)
    # Parse the JSON response to get the list of files
    files = response.json()
    
    # Initialize an empty list to store the changed file names
    changed_files = []
    for file in files:
        # Add the file name to the list
        changed_files.append(file['filename'])
        
    # Return the list of changed file names
    return changed_files

def log_info(repo_name, changed_files):
    """
    Log the repository name and changed files.
    """
    # Log the repository name
    logging.info(f"Repository: {repo_name}")
    # Log the list of changed files
    logging.info(f"Changed files: {', '.join(changed_files)}")

    # Optionally, save the log to an S3 bucket
    import boto3  # Import the Boto3 library to interact with AWS services
    # Create an S3 client
    s3 = boto3.client('s3')
    # Create the log content as a dictionary
    log_content = {
        'repository': repo_name,
        'changed_files': changed_files
    }
    # Save the log content as a JSON object in the specified S3 bucket
    s3.put_object(Bucket=LOGGING_BUCKET, Key=f'logs/{repo_name}/{context.aws_request_id}.json', Body=json.dumps(log_content))

>>>>>>> 454933c40425826c19d7b7c777f7b471d4a53b4d

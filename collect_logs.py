import os 
from github import Github
import boto3
import logging

github_token = "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"
GITHUB_TOKEN = os.getenv('github_token')

user_id = GITHUB_TOKEN.get_user()
print(user_id.name)
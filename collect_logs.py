<<<<<<< HEAD
import os 
from github import Github
import boto3
import logging

github_token = "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"
GITHUB_TOKEN = os.getenv('github_token')

user_id = GITHUB_TOKEN.get_user()
=======
import os 
from github import Github
import boto3
import logging

github_token = "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"
GITHUB_TOKEN = os.getenv('github_token')

user_id = GITHUB_TOKEN.get_user()
>>>>>>> 454933c40425826c19d7b7c777f7b471d4a53b4d
print(user_id.name)
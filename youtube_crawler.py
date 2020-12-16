# -*- coding: utf-8 -*- 
import pickle
import csv
import os

import google.oauth2.credentials

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

CLIENT_SECRETS_FILE = "/Users/yeong-in/Desktop/pyi/코리/dev/client_secret_415059270452-s5jn59vb5v8cqb9go6juqspltbj41c0h.apps.googleusercontent.com.json" #delete file name, if you post this code later
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


#api를 사용할 수 있는 서비스를 빌드한다.
def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)


if __name__ == '__main__':
    # When running locally, disable OAuthlib's HTTPs verification. When
    # running in production *do not* leave this option enabled.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    service = get_authenticated_service()

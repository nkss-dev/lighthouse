import json
import os
from dotenv import load_dotenv

load_dotenv()

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ("https://www.googleapis.com/auth/drive",)

GOOGLE_CLIENT_ID = os.environ["GOOGLE_CLIENT_ID"]
GOOGLE_CLIENT_SECRET = os.environ["GOOGLE_CLIENT_SECRET"]
GOOGLE_REFRESH_TOKEN = os.environ.get("GOOGLE_REFRESH_TOKEN")

if GOOGLE_REFRESH_TOKEN:
    creds = Credentials.from_authorized_user_info(
        {
            "client_id": GOOGLE_CLIENT_ID,
            "client_secret": GOOGLE_CLIENT_SECRET,
            "refresh_token": GOOGLE_REFRESH_TOKEN,
        },
        SCOPES,
    )
    creds.refresh(Request())
else:
    flow = InstalledAppFlow.from_client_config(
        {
            "installed": {
                "client_id": GOOGLE_CLIENT_ID,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "client_secret": GOOGLE_CLIENT_SECRET,
            }
        },
        SCOPES,
    )
    creds = flow.run_local_server(port=0)

os.environ["GOOGLE_REFRESH_TOKEN"] = json.loads(creds.to_json())["refresh_token"]
print(json.loads(creds.to_json())["refresh_token"])

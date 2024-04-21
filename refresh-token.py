import json
import os

from dotenv import load_dotenv

load_dotenv()

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

creds = Credentials.from_authorized_user_info(
    {
        "client_id": os.getenv("GOOGLE_CLIENT_ID"),
        "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
        "refresh_token": os.getenv("GOOGLE_REFRESH_TOKEN"),
        "token": "",
    },
    ("https://www.googleapis.com/auth/drive",),
)
print(json.loads(creds.to_json())["refresh_token"])
creds.refresh(Request())
os.environ["GOOGLE_REFRESH_TOKEN"] = json.loads(creds.to_json())["refresh_token"]
print(json.loads(creds.to_json())["refresh_token"])

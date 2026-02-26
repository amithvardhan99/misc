from crewai_tools import BaseTool
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
import base64
import os
import markdown

SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]

class SendEmailTool(BaseTool):
    name: str = "Sent Gmail Email"
    description: str "Creates and sends Gmail draft with meeting minutes"

    def _run(self, recipient: str, subject: str, body: str):
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())
        
        service = build("gmail", "v1", credentials=creds)
        message = MIMEText(body)
        message["to"] = recipient
        message["subject"] = subject
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        draft = service.users().messages().create(userId="me", body={"raw": raw}).execute()
        #html_body = markdown.markdown(body)
        return f"Draft created: {draft['id']}"

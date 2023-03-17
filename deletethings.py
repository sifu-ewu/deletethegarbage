import os
import httplib2
import google.auth
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Path to your client_secret.json file
CLIENT_SECRET_FILE = 'E:\client_secret_1013428011465-sd7erugf193vun8r7th3jqe7l31u3jgr.apps.googleusercontent.com.json'

# Scopes required for the Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive']

def get_credentials():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    return flow.run_local_server(port=0)

def delete_all_files():
    try:
        credentials = get_credentials()
        service = build('drive', 'v3', credentials=credentials)
        
        # Retrieve all files
        files_to_delete = []
        page_token = None
        while True:
            response = service.files().list(q="mimeType != 'application/vnd.google-apps.folder'",
                                            spaces='drive',
                                            fields='nextPageToken, '
                                                   'files(id, name)',
                                            pageToken=page_token).execute()
            files_to_delete.extend(response.get('files', []))
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break

        # Permanently delete all files
        for file in files_to_delete:
            try:
                print(f'Deleting file: {file["name"]} ({file["id"]})')
                service.files().delete(fileId=file['id']).execute()
            except HttpError as error:
                print(f'An error occurred while deleting {file["name"]}: {error}')

    except HttpError as error:
        print(f'An error occurred: {error}')
        files_to_delete = None

    return files_to_delete

if __name__ == '__main__':
    delete_all_files()

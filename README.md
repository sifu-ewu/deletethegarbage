
# Delete all files permanently from your Google Drive using Python
you'll need to use the Google Drive API. First, you need to set up a project in Google Cloud Platform, enable the Drive API, and obtain the necessary credentials.

Set up a project in the Google Cloud Platform Console.
Enable the Google Drive API.
Create credentials for your project (OAuth 2.0 client ID), and download the JSON file.

After setting up the project, install the Google Client Library:





run this code on terminal

```bash
  pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

Replace 'path/to/your/client_secret.json' with the path to your client_secret.json file. This script will prompt you to authorize access to your Google Drive, and then it will permanently delete all non-Google Workspace files. If you want to delete Google Workspace files as well, you can remove the q parameter in the service.files().list() method.

now run the python file 

```bash
  python deletethings.py

```

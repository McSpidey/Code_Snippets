#PyDrive is too simple
# https://pythonhosted.org/PyDrive/oauth.html

#Google Drive native API should be used instead.
#Roles https://developers.google.com/drive/api/guides/ref-roles
#Service Account/Key Mode https://blog.benjames.io/2020/09/13/authorise-your-python-google-drive-api-the-easy-way/

#Standard quickstart, doesn't work for service account.
# from pydrive.auth import GoogleAuth

# gauth = GoogleAuth()
# gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

#Alt method
# https://stackoverflow.com/questions/60736955/how-to-connect-pydrive-with-an-service-account
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials

JSON_FILE = "client_secrets.json"
gauth = GoogleAuth()
scope = ["https://www.googleapis.com/auth/drive"]
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_FILE, scope)
drive = GoogleDrive(gauth)


#Upload file.
#https://stackoverflow.com/questions/46562255/python-upload-my-own-files-into-my-drive-using-pydrive-library

myfile = "SyamaFile.txt"
file1 = drive.CreateFile()
#Alt - Manually overwrite metadata
# file1 = drive.CreateFile(metadata={"title": "CustomFileName.txt"})

file1.SetContentFile(myfile)
file1.Upload()

#https://pythonhosted.org/PyDrive/filemanagement.html
# Insert the permission.
permission = file1.InsertPermission({
                        'type': 'anyone',
                        'value': 'anyone',
                        'role': 'reader'})

print(file1['permissions'])
print(file1['alternateLink'])  # Display the sharable link.

#List files, simple.
#https://pythonhosted.org/PyDrive/filelist.html
# query = "'root' in parents and trashed=false"
# file_list = drive.ListFile({'q': query}).GetList()
# for file1 in file_list:
#   print('title: %s, id: %s' % (file1['title'], file1['id']))


#ListFiles Paginated.
# Paginate file lists by specifying number of max results
# query = 'trashed=true'
# for file_list in drive.ListFile({'q': query, 'maxResults': 20}):
#   print('Received %s files from Files.list()' % len(file_list)) # <= 10
#   for file1 in file_list:
#       print('title: %s, id: %s' % (file1['title'], file1['id']))
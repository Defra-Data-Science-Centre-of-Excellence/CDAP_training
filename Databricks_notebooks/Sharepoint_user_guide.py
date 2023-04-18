# Databricks notebook source
pip install office365-rest-client --quiet

# COMMAND ----------

from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.files.file import File
import getpass
import pandas as pd
import os

# COMMAND ----------

# DBTITLE 1,Authenticate into SharePoint
shrpt_base = 'https://defra.sharepoint.com'    #DEFRA' ssharepoint site
shrpt_team = '/teams/<your-team-no>' # your team site e.g. '/teams/Team334'
siteurl = baseurl + basesite
ctx_auth = AuthenticationContext(shrpt_base)      #Authrenticate to SharePoint
ctx = ClientContext(siteurl, ctx_auth).with_credentials(UserCredential("your_sharepoint_login@defra.gov.uk", getpass.getpass()))   #Use getpass to hide password input
web = ctx.web
ctx.load(web)
ctx.execute_query()
print("Authenticated into: {0}".format(web.properties['Title']))

# COMMAND ----------

# DBTITLE 1,Get a list of files and folders inside your SharePoint folder
folder_url = 'https://defra.sharepoint.com/teams/Team552/Data%20Information/Data%20Strategy%20and%20Engagement/Current%20Projects/' #You will have to alter the link for the folder you want to access so it looks like this link here
folder = ctx.web.get_folder_by_server_relative_url(folder_url)
fold_names, file_names = [], []
sub_folders = folder.folders #Get subfolders in the folder
files = folder.files         #Get files in folder
ctx.load(sub_folders)
ctx.load(files)
ctx.execute_query()

for s_folder in sub_folders:
    fold_names.append(s_folder.properties["Name"])    #Append name of folders to our folder list
for i in files:
    file_names.append(i.properties['Name'])           #Append name of files to our folder list

print(fold_names)
print(file_names)

# COMMAND ----------

# DBTITLE 1,Access the file you want
remotepath = files[0].properties['ServerRelativeUrl']   # Url of path for the file in sharepoint that we want to open, replace the '0' in files[0] with the index of the file in the file_names list
response=File.open_binary(ctx, remotepath)
data = pd.read_excel(response.content)

# COMMAND ----------

# DBTITLE 1,Save SharePoint file to your lab zone
with open('/dbfs/mnt/lab/unrestricted/<your-labzonefolder>', 'wb') as output_file:
    output_file.write(response.content)       # Saves the file in sharepoint to the lab zone

# COMMAND ----------

# DBTITLE 1,Save file to your SharePoint site
with open('/dbfs/mnt/lab/unrestricted/<file-from-labzone>', 'rb') as content_file:
    file_content = content_file.read()      #Read file from the labzone

file_name = 'test.csv'         #The name of the file once saved in sharepoint
remotepath = folder_url + file_name    
dir, name = os.path.split(remotepath)
file = ctx.web.get_folder_by_server_relative_url(dir).upload_file(name, file_content).execute_query()   #Upload the file to SharePoint

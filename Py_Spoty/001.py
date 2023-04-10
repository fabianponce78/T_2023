'''
Created on Sep 15, 2022

@author: fponce
'''
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import base64
from requests.auth import HTTPBasicAuth
import datetime
#import json
import json, codecs
#from oauthlib.oauth1.rfc5849.endpoints import access_token
#from pandas._libs.tslibs.strptime import seconds


'''
Client ID d6338d1d10164334b76a70a2df5e495b
Client Secret d7c5fc75f56d4050aa6b25e78bce9b57
token_url = "https://accounts.spotify.com/api/token"
Authorization: Basic <base64 encoded client_id:client_secret>

See. https://www.youtube.com/watch?v=xdq6Gz33khQ
'''

client_id = "d6338d1d10164334b76a70a2df5e495b"
client_secret = "d7c5fc75f56d4050aa6b25e78bce9b57"


client_creds = f"{client_id}:{client_secret}"
print("client_creds Type = ", type(client_creds))

client_creds_b64 = base64.b64encode(client_creds.encode())
print("client_creds_b64 = ", client_creds_b64) 
#client_creds.encode().decode()

token_url = "https://accounts.spotify.com/api/token"

method = "POST"

token_data = {
    "grant_type": "client_credentials"
    }
token_headers = {    
    #"Authorization": f"Basic {client_creds}"    #"Authorization": "Basic <base64 encoded client_id:client_secret>"
    "Authorization": f"Basic {client_creds_b64.decode()}"    #"Authorization": "Basic <base64 encoded client_id:client_secret>"
    }

print("token_headers = ", token_headers)



######------------------------------------------------------------------------------
######------------------------------------------------------------------------------
print("-----------------------------------------------------------------------------")
r = requests.post(token_url, data=token_data, headers=token_headers)
print(r.json())

valid_request = r.status_code in range(200, 299)
print("valid_request = ", valid_request)

if valid_request:
    token_response_data = r.json()    
    now = datetime.datetime.now()
    access_token = token_response_data['access_token']
    expires_in = token_response_data['expires_in'] # Seconds
    expires = now + datetime.timedelta(seconds=expires_in)
    did_expire = expires < now

#print("expires = ", expires)

######------------------------------------------------------------------------------
######------------------------------------------------------------------------------
######------------------------------------------------------------------------------
######------------------------------------------------------------------------------

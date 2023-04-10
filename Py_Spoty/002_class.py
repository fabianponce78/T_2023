'''
Created on Sep 15, 2022

@author: fponce
'''
import requests
import datetime
import base64


'''
Client ID d6338d1d10164334b76a70a2df5e495b
Client Secret d7c5fc75f56d4050aa6b25e78bce9b57
token_url = "https://accounts.spotify.com/api/token"
Authorization: Basic <base64 encoded client_id:client_secret>

See. https://www.youtube.com/watch?v=xdq6Gz33khQ
'''

client_id = "d6338d1d10164334b76a70a2df5e495b"
client_secret = "d7c5fc75f56d4050aa6b25e78bce9b57"


class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True    
    client_id = None
    client_secret = None
    token_url = "https://accounts.spotify.com/api/token"
    
    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret
        
    def get_client_credentials(self):
        """
        Returns a base64 encoded string
        """
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret == None or client_id == None:
            raise Exception("You most set client_id and client_secret")
            
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()
        
    def get_token_headers(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            "Authorization": f"Basic {client_creds_b64}"    #"Authorization": "Basic <base64 encoded client_id:client_secret>"
        }
    
    def get_token_data(self):
        return {
            "grant_type": "client_credentials"
        }
        
    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        
        r = requests.post(token_url, data=token_data, headers=token_headers)

        if r.status_code not in range(200, 299):
            return False
        data = r.json()    
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in'] # Seconds
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True 


Spotify = SpotifyAPI(client_id, client_secret)    

print(Spotify.perform_auth())
print(Spotify.access_token)






 

'''
method = "POST"

token_data = {
    "grant_type": "client_credentials"
    }
token_headers = {    
    #"Authorization": f"Basic {client_creds}"    #"Authorization": "Basic <base64 encoded client_id:client_secret>"
    "Authorization": f"Basic {client_creds_b64.decode()}"    #"Authorization": "Basic <base64 encoded client_id:client_secret>"
    }

print("token_headers = ", token_headers)
'''


######------------------------------------------------------------------------------
######------------------------------------------------------------------------------
#print("-----------------------------------------------------------------------------")


#print("expires = ", expires)

######------------------------------------------------------------------------------
######------------------------------------------------------------------------------
######------------------------------------------------------------------------------
######------------------------------------------------------------------------------

import requests
import time
import json

from pprint import pprint


#===============================================================================
# Get Currently Playing Track with Spotify API (Python Tutorial)
# https://www.youtube.com/watch?v=yKz38ThJWqE
# https://github.com/imdadahad/spotify-get-current-playing-track/blob/master/main.py
#===============================================================================

#===============================================================================
# Get Playlist Items
# https://developer.spotify.com/console/get-playlist-tracks/?playlist_id=&market=&fields=&limit=&offset=&additional_types=
# 
#  GET https://api.spotify.com/v1/playlists/{playlist_id}/tracks
#  curl -X "GET" "https://api.spotify.com/v1/playlists//tracks" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQBodWQBKf3wdVg7j2aY20-UFL4hlkx5USfDEZwlFO6qz21ssu-xcDs73S8W-kinSSpjQhgxg65e5chrEf4ksRz_LJ0OE4nQQf181Bl-wiQ6rzOn82RHwrYq2ZiHyeIZR3djHBEDbHMIQCVsIeIoM3p0l2XUclrSBFUk3UCts06LJmebTw6tpi18N0S6vu73JBs"
#  
#    TOKEN   ==>  BQBodWQBKf3wdVg7j2aY20-UFL4hlkx5USfDEZwlFO6qz21ssu-xcDs73S8W-kinSSpjQhgxg65e5chrEf4ksRz_LJ0OE4nQQf181Bl-wiQ6rzOn82RHwrYq2ZiHyeIZR3djHBEDbHMIQCVsIeIoM3p0l2XUclrSBFUk3UCts06LJmebTw6tpi18N0S6vu73JBs
#===============================================================================


SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
ACCESS_TOKEN = 'BQBodWQBKf3wdVg7j2aY20-UFL4hlkx5USfDEZwlFO6qz21ssu-xcDs73S8W-kinSSpjQhgxg65e5chrEf4ksRz_LJ0OE4nQQf181Bl-wiQ6rzOn82RHwrYq2ZiHyeIZR3djHBEDbHMIQCVsIeIoM3p0l2XUclrSBFUk3UCts06LJmebTw6tpi18N0S6vu73JBs'


#"Authorization": f"Bearer {access_token}"
def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    json_resp = response.json()
    
    r = requests.post(token_url, data=token_data, headers=token_headers)
print(r.json())

#===============================================================================
#     track_id = json_resp['item']['id']
#     track_name = json_resp['item']['name']
#     artists = [artist for artist in json_resp['item']['artists']]
# 
#     link = json_resp['item']['external_urls']['spotify']
# 
#     artist_names = ', '.join([artist['name'] for artist in artists])
# 
#     current_track_info = {
#         "id": track_id,
#         "track_name": track_name,
#         "artists": artist_names,
#         "link": link
#     }
# 
#     return current_track_info
#===============================================================================


def main():
    current_track_id = None
    while True:
        current_track_info = get_current_track(ACCESS_TOKEN)

        if current_track_info['id'] != current_track_id:
            pprint(
                current_track_info,
                indent=4,
            )
            current_track_id = current_track_info['id']

        time.sleep(1)


if __name__ == '__main__':
    main()
# import requests
# import json

# import os
# from dotenv import load_dotenv

# load_dotenv(dotenv_path="./.env")


# API_KEY=os.getenv("API_KEY")
# CHANNEL_HANDLE="MrBeast"

# def get_playlist_id():
#     try:
#         url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

#         response = requests.get(url)

#         # print(response)

#         response.raise_for_status()

#         data = response.json()

#         # print(json.dumps(data,indent=4))

#         channel_items = data['items'][0]

#         channel_playlistId = channel_items['contentDetails']['relatedPlaylists']['uploads']

#         print(channel_playlistId)

#         return channel_playlistId

#     except requests.exceptions.RequestException as e:
#         raise e 
    
# if __name__=="__main__":
    
#     get_playlist_id()

   
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Config variables
API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = "MrBeast"

# Debug prints
print("Working directory:", os.getcwd())
print("API_KEY:", API_KEY)

def get_playlist_id():
    try:
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        channel_items = data['items'][0]

        channel_playlistId = channel_items['contentDetails']['relatedPlaylists']['uploads']

        print(channel_playlistId)

        return channel_playlistId

    except requests.exceptions.RequestException as e:
        raise e


if __name__ == "__main__":
    get_playlist_id()
















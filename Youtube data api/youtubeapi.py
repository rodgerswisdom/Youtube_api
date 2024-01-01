import pandas as pd
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os.path
import json

# Constants
API_KEYS = ['YOUR API KEY_1,...n']
API_KEY_INDEX = 0  # Index to keep track of the current API key
MAX_RESULTS = 100  # Maximum results per request

#num_api = len(API_KEYS)
#print("number of apis is:", num_api)

"""for index in API_KEYS:
    print(index)"""

# Function to read Excel sheet
def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df

# Function to display data
def display_data(data):
    print(data)

# Function to store data in a list
def store_data(data):
    # Implement storing logic here
    pass

# Function to search for a video using the name
def search_video(api_key, video_name):
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.search().list(
        q=video_name,
        type="video",
        part="id",
        maxResults=1
    )
    response = request.execute()
    """
    video_id = response["items"][0]["id"]["videoId"]
    video_link = f"https://www.youtube.com/watch?v={video_id}"
    return video_link"""

    if "items" in response and response["items"]:
        video_id = response["items"][0]["id"]["videoId"]
        video_link = f"https://www.youtube.com/watch?v={video_id}"
        return video_link
    else:
        # No items found for the search query
        return None

# Function to handle API key rotation
def get_next_api_key():
    global API_KEY_INDEX
    API_KEY_INDEX = (API_KEY_INDEX + 1) % len(API_KEYS)
    return API_KEYS[API_KEY_INDEX]

# Main function
def main():
    file_path = "nameoftool.xlsx"
    data = read_excel(file_path)
    display_data(data)

    # Assuming your Excel sheet has a column named "VideoName"
    video_names = data["Tool Name"].tolist()

    stored_data = []

    for video_name in video_names:
        api_key = get_next_api_key()
        print(f"Using API Key: {api_key} for video: {video_name}")
        video_link = search_video(api_key, video_name)
        
        # Store data
        stored_data.append({"Tool Name": video_name, "Video Link": video_link})
        

    display_data(stored_data)

    #periodically write data in excel
    if len(stored_data) % 10 == 0:
        partial_df = pd.DataFrame(stored_data)
        partial_df.to_excel("partial_result.xlsx", index=False)

    # Write to Excel
    result_df = pd.DataFrame(stored_data)
    result_df.to_excel("result.xlsx", index=False)

if __name__ == "__main__":
    main()

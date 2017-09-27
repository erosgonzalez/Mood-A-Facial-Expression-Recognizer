#Gets a Youtube ID
from ExpressionDetec import faceDetect
import random
from apiclient.discovery import build
from oauth2client.tools import argparser

API_Key = "AIzaSyBsXXhBHacMndY4niLEsIUfZQ3eRptjhUw"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

VideoIds = [ ] 

def yt_search(term):
    youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION, developerKey = API_Key)
    
    search_response = youtube.search().list(
        q =term,
        part="id,snippet",
        maxResults=50
        ).execute()
        
    videos = []
 
    for search_results in search_response.get("items", [ ]):
        if search_results["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_results["snippet"]["title"],search_results["id"]["videoId"]))
            Id = search_results["id"]["videoId"]
            VideoIds.append(Id)

def user():
	emotion = faceDetect()

	if emotion == "smile":
		yt_search("happy music")
	elif emotion == "neutral":
		yt_search("neutral music")
	elif emotion == "face":
		yt_search("alternative music")
	elif emotion == "no face":
		yt_search("nujabes")

	Random_Id = (random.choice(VideoIds))
	return Random_Id

    
        

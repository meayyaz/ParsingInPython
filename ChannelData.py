import json
import urllib.request

GOOGLE_API_KEY="<YOUR_GOOGLE_KEY>"
CHANNEL_ID="UCllefjGak7WtAV3sVcRy9xQ&"

urlData = "https://www.googleapis.com/youtube/v3/search?channelId="+CHANNEL_ID+"order=date&part=snippet&type=video&maxResults=500&key="+GOOGLE_API_KEY


videos = list()

webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
json_data = json.loads(data.decode(encoding))

nextPageToken = "start"

while nextPageToken != "":
    if(nextPageToken != "start"):
        webURL = urllib.request.urlopen(urlData+"&pageToken="+nextPageToken)
    else:
        webURL = urllib.request.urlopen(urlData)

    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    json_data = json.loads(data.decode(encoding))

    for item in json_data["items"]:
        data = list()
        data.append(item["id"]["videoId"] )
        data.append(item["snippet"]["title"])
        data.append(item["snippet"]["publishTime"])
        videos.append(data)
    
    if ("nextPageToken" in json_data):
        nextPageToken =  json_data["nextPageToken"]
    else:
        nextPageToken = "";

    print(nextPageToken)


urlData = "https://www.googleapis.com/youtube/v3/videos?key="+GOOGLE_API_KEY+"&part=snippet,contentDetails,statistics,status&id="
count = 0
for video in videos:
    webURL = urllib.request.urlopen(urlData+video[0])
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    json_data = json.loads(data.decode(encoding))

    for item in json_data["items"]:
        
        video.append(item["statistics"]["viewCount"] if "viewCount" in item["statistics"] else "0")
        video.append(item["statistics"]["likeCount"] if "likeCount" in item["statistics"] else "0")
        video.append(item["statistics"]["dislikeCount"] if "dislikeCount" in item["statistics"] else "0")
        video.append(item["statistics"]["favoriteCount"] if "favoriteCount" in item["statistics"] else "0")
        video.append(item["statistics"]["commentCount"] if "commentCount" in item["statistics"] else "0")
        
    count +=1
    print(str(count) + "\t" + video[0] + "\t" + video[5])

import csv

with open('/Users/ayyaz/DataScience/ZeeshanUsmaniChannelData.csv', mode='w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerow(['Video Id', 'Title', 'PublishTime','ViewCount','LikeCount','DislikeCount','favoriteCount','commentCount'])
    writer.writerows(videos)

import pandas as pd 
df = pd.DataFrame(videos) 
df 
df.columns = ['Video Id', 'Title', 'PublishTime','ViewCount','LikeCount','DislikeCount','favoriteCount','commentCount']

df["likePerView"] = round( pd.to_numeric(df["LikeCount"]) / pd.to_numeric(df["ViewCount"]), 2 ) *100

df['year'] = pd.DatetimeIndex(df['PublishTime']).year
df['month'] = pd.DatetimeIndex(df['PublishTime']).month
df['day'] = pd.DatetimeIndex(df['PublishTime']).day
df['time'] = pd.DatetimeIndex(df['PublishTime']).time

# Saving...
df.to_csv('/Users/ayyaz/DataScience/ZeeshanUsmaniChannelData.csv', index=False)

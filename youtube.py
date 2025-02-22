from pytubefix import YouTube, Search
import random
import time

def video_data(id):
  yt = YouTube(f"https://youtube.com/?v={id}")
  stream = yt.streams.filter(file_extension='mp4')[0]
  return stream.download(filename=f"{random.randint(1000,9999)}_temp.mp4")


def audio_data(id):
  yt = YouTube(f"https://youtube.com/?v={id}")
  stream = yt.streams.filter(only_audio=True)[0]
  return stream.download(filename=f"{random.randint(1000,9999)}_temp.mp3")

def video_metadata(id):
  yt = YouTube(f"https://youtube.com/?v={id}")
  return [yt.title, time.strftime("%H:%M:%S", yt.length), yt.thumbnail_url, str(yt.views), yt.author, yt.publish_date]


def search_query(query):
  results = []
  for result in Search(query).videos:
    results.append(result.video_id)
    results.extend(video_metadata(result.video_id))
  results.insert(0, f"There were {len(results)} results for {query}.")
  return results
  

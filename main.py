import scratchattach as sa
import youtube

cloud = sa.get_tw_cloud("1116186279")
client = cloud.requests(respond_order='finish')

@client.event
def on_ready():
	print("READY")

@client.request
def ping():
	print("ping")
	return "pong"

@client.request
def video_data(id):
	print("video_data for " + id)
	return ["frame-1-data", "frame-2-data", "frame-3-data", "etc."] # frame data for each frame

@client.request
def audio_data(id):
	print("audio_data for " + id)
	return ["idk", "what", "format", "this", "will", "be"] # idk what format this will be

@client.request
def video_metadata(id):
	print("metadata for " + id)
	return youtube.video_metadata(id)

@client.request
def search_query(query):
	print("searched")
	return youtube.search_query(query)

client.start()

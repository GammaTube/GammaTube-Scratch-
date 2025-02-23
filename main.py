import scratchattach as sa
import youtube
import converter

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
	return youtube.video_data(id)

@client.request
def audio_data(id):
	print("audio_data for " + id)
	return youtube.audio_data(id)

@client.request
def video_metadata(id):
	print("metadata for " + id)
	m = youtube.video_metadata(id)
	thumb = m[2]
	data = converter.img_from_url(thumb, 64)
	m[2] = data
	return m

@client.request
def search_query(query):
	print("searched")
	return youtube.search_query(query)

@client.request
def high_res_thumb(id):
	print("high res thumb for " + id)
	m = youtube.video_metadata(id)
	thumb = m[2]
	data = converter.img_from_url(thumb, 96)
	return str(data)

client.start()

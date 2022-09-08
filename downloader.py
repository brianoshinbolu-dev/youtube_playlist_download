from pytube import Playlist
p = input("Enter the url of the playlist")
purl = Playlist(p)


print(f"Downloading: {p.title}")

for video in purl.videos:
	print(video.title)
	st = video.streams.get_highest_resolution()
	st.download()
	#vido.streams.first().download()
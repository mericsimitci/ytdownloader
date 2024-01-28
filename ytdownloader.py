from pytube import YouTube

video_url = input("Enter video url: ")
video_quality = input("Enter video quality (örn: 720p): ")
yt = YouTube(video_url)
video = yt.streams.filter(res=video_quality).first()
print("Video downloading...")
video.download()

print("Video downloaded.")

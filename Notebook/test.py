from pytube import YouTube

# get url
url = "https://www.youtube.com/watch?v=JtPbk7WvHAQ"
# call youtube method and pass the url
myVideo = YouTube(url)

# set the stream resolution to download video
my_video = myVideo.streams.get_highest_resolution()

my_video = myVideo.streams.first()

print(my_video)
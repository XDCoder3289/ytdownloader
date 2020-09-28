from pytube import YouTube
import os

video = input("Please enter the YouTube video link you want to download: ")
ytdownloader = YouTube(video)

print("Is this the title of the video you want to download: ", ytdownloader.title)

check = input("enter \'y\' or \'n\': ")
if check == "y":
    print("Ok!")
    if os.path.isdir("videos") != True:
        os.mkdir('videos')
    print(f"Downloading a {ytdownloader.length} seconds video")
    vid = ytdownloader.streams.get_highest_resolution()
    vid.download('videos')
    print('Download completed! Please check a folder \'videos\' in script\'s directory')
else:
    print("Ok. Please be more particular!")


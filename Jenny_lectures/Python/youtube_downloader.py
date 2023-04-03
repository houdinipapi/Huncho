#!/usr/bin/python3

import pytube

# Save it in the current working directory
download_loc = './'

# User input
video_url = input("Enter url: ")

#Create an instance of YouTube video
video_instance = pytube.YouTube(video_url)

stream = video_instance.streams.get_highest_resolution()

# download
stream.download()

import os
from mutagen.mp4 import MP4

PATH = "C:/Users/Zanis/Desktop/Java Social Network/Videos"
videos = os.listdir(PATH)
sum = 0
for video in videos:
    audio = MP4(PATH + "/" + video)
    sum+=round(audio.info.length/60)
print(sum/60)
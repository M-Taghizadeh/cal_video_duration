import os
from mutagen.mp4 import MP4

PATH = "D:/My Courses/Java Social Network"
videos = os.listdir(PATH)
sum = 0
for video in videos:
    audio = MP4(PATH + "/" + video)
    sum+=round(audio.info.length/60)
print(sum/60)

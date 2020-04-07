# A script to find total duration of videos in a folder

import os
from moviepy.editor import VideoFileClip
directory = input("Enter video directory : ")
def main():
    tot = 0.0
    for filename in os.listdir(directory):
        if filename.endswith('.mkv' or '.mp4'):
            a = (directory+"/"+filename)
            clip = VideoFileClip(a)
            dur = int(clip.duration)
            clip.reader.close()
            tot += dur
    print("Total binge time is : "+str(tot/3600)+"  hours")
    input("Press enter to exit ;)")

main()
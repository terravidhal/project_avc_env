#!/usr/bin/env python3.10.11
import os
# os.environ["IMAGEIO_FFMPEG_EXE"] = "C:/ffmpeg/bin/ffmpeg.exe"
os.environ["IMAGEIO_FFMPEG_EXE"] = "./myenv/Lib/site-packages/imageio_ffmpeg/binaries/ffmpeg-win64-v4.2.2.exe"
# os.environ["IMAGEIO_FFMPEG_EXE"] = 'C:/Users/"terra vidhal"/AppData/Roaming/Python/Python37/site-packages/imageio_ffmpeg/binaries/ffmpeg-win64-v4.2.2.exe'
import moviepy.editor as mp 
import speech_recognition as sr 
  
# Load the video 
# video = mp.VideoFileClip("t.mp4") 
  
# Extract the audio from the video 
# audio_file = video.audio 
# audio_file.write_audiofile("t.wav") 
  
# Initialize recognizer 
r = sr.Recognizer() 
  
# Load the audio file 
with sr.AudioFile("t.wav") as source: 
    data = r.record(source) 
  
# Convert speech to text 
text = r.recognize_google(data, language="fr-FR") 
  
# Print the text 
print("\nThe resultant text from video is: \n") 
print(text) 

# Open a new text file in write mode
with open("t.txt", "w") as file:
    # Write the text to the file
    file.write(text)




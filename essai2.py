import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "./myenv/Lib/site-packages/imageio_ffmpeg/binaries/ffmpeg-win64-v4.2.2.exe"

import moviepy.editor as mp
import speech_recognition as sr
import docx 
from docx.shared  import Inches 
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Load the video
video = mp.VideoFileClip("TCF1.mp4")

# Extract the audio from the video
audio_file = video.audio
audio_file.write_audiofile("TCF1.wav")

# Initialize recognizer
r = sr.Recognizer()

# Load the audio file
with sr.AudioFile("TCF1.wav") as source:
    data = r.record(source)

# Convert speech to text
text = r.recognize_google(data, language="fr-FR")

# Print the text
print("\nThe resultant text from video is: \n")
print(text)

# Open a new Word document
doc = docx.Document()

# Add the text to the document
para = doc.add_paragraph(text)

# Apply formatting to the paragraph
# 1. Line spacing (relative value)
para.paragraph_format.line_spacing = 1.75

# 2. Spacing before and after the paragraph (0.5 inch each)
para.paragraph_format.space_before = Inches(0.5)
para.paragraph_format.space_after = Inches(0.5)

# 3. Text alignment (centered)
para.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Save the document
doc.save("TCF1.docx")
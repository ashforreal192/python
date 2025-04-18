import os
from moviepy.editor import VideoFileClip # type: ignore

video_path = input("Enter the path to the video file: ")

if os.path.exists(video_path):
    try:
        clip = VideoFileClip(video_path)
        audio = clip.audio
        audio.write_audiofile("Extracted_Audio.mp3")
        print("Audio extracted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("Video file not found.")

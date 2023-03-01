from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os


video_clip = VideoFileClip("./1677639152039.mp4")
audio_clip = AudioFileClip("./1677639152039.wav")
final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile("video.mp4")

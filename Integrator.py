import cv2
import time
import pyaudio
import wave
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips


audio=pyaudio.PyAudio()
stream=audio.open(
    format=pyaudio.paInt16,channels=1,rate=44100, input=True,frames_per_buffer=1024
)
frames=[]

video=cv2.VideoCapture(0)

video_file_name=f'{round(time.time()*1000)}.mp4'
audio_file_name=f'{round(time.time()*1000)}.wav'

videoWriter=None

is_recording_started=False

while True:
    ret,frame= video.read()
    if is_recording_started:
        data=stream.read(1024)
        frames.append(data)
        videoWriter.write(frame)
        cv2.putText(frame, "Recording is in progress", (50,30),color=(255,0,0),fontFace=cv2.FONT_ITALIC,fontScale=1,thickness=3)
    else:
        cv2.putText(frame, "Recording is not yes started", (50,30),color=(0,0,255),fontFace=cv2.FONT_ITALIC,fontScale=1,thickness=3)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1)==32:
        is_recording_started=True
        video.release()
        video=cv2.VideoCapture(0)
        videoWriter=cv2.VideoWriter(video_file_name, cv2.VideoWriter_fourcc(*'DIVX'), 20, (640,480))
    if cv2.waitKey(2)==ord('q'):
        break
stream.start_stream()
stream.close()
audio.terminate()

file=wave.open(audio_file_name,'wb')
file.setnchannels(1)
file.setsampwidth(
    audio.get_sample_size(pyaudio.paInt16)
)
file.setframerate(44100)
file.writeframes(b''.join(frames))
video.release()
videoWriter.release()
cv2.destroyAllWindows()


video_clip = VideoFileClip("./1677639152039.mp4")
audio_clip = AudioFileClip("./1677639152039.wav")
final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile("video.mp4")



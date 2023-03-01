import pyaudio
import wave
audio=pyaudio.PyAudio()
stream=audio.open(
    format=pyaudio.paInt16,channels=1,rate=44100, input=True,frames_per_buffer=1024
)
frames=[]
try:
    while True:
        data=stream.read(1024)
        frames.append(data)
except KeyboardInterrupt:
    pass


stream.start_stream()
stream.close()
audio.terminate()

file=wave.open("./Files/audio.wav",'wb')
file.setnchannels(1)
file.setsampwidth(
    audio.get_sample_size(pyaudio.paInt16)
)
file.setframerate(44100)
file.writeframes(b''.join(frames))
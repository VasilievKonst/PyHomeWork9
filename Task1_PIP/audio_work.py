import wave
import sys

import pyaudio

CHUNK = 1024

def music(data):

    with wave.open(data, 'rb') as m:
    
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(m.getsampwidth()),
                    channels=m.getnchannels(),
                    rate=m.getframerate(),
                    output=True)

        while len(data := m.readframes(CHUNK)):
            stream.write(data)

        stream.close()

        p.terminate()
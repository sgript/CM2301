import pyaudio
import wave
import sys


class Audio:
    def __init__(self):
        self.name = ""

    def aud(self, name):
        chunk = 1024

        wf = wave.open(name, 'rb')

        p = pyaudio.PyAudio()


        stream = p.open(format =
                        p.get_format_from_width(wf.getsampwidth()),
                        channels = wf.getnchannels(),
                        rate = wf.getframerate(),
                        output = True)

        data = wf.readframes(chunk)

        while data != '':
            stream.write(data)
            data = wf.readframes(chunk)

        stream.close()    
        p.terminate()


if __name__ == '__main__':
    try:
        audio = Audio()
        audio.aud(sys.argv[1])
    except (Exception) as err:
        print err

    

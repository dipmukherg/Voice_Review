import pyaudio
import wave
import requests
import os
import io
from google.cloud import speech_v1
from google.cloud import speech_v1
from google.cloud.speech_v1 import types
from array import array
import requests

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='my-new-project-265705-90a669a5d4c2.json'








def sample_recognize():
    # CHUNK = 1024
    # FORMAT = pyaudio.paInt16
    # CHANNELS = 2
    # RATE = 44100
    # RECORD_SECONDS = 5
    # WAVE_OUTPUT_FILENAME = "output.wav"

    # p = pyaudio.PyAudio()

    # stream = p.open(format=FORMAT,
    #                 channels=CHANNELS,
    #                 rate=RATE,
    #                 input=True,
    #                 frames_per_buffer=CHUNK)

    # print("* recording")

    # frames = []

    # # you'll probably want to experiment on threshold
    # # depends how noisy the signal
    # threshold = 10000 
    # max_value = 0

    # count=0
    # #for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    # while count<100:
    #     data = stream.read(CHUNK)
    #     as_ints = array('h', data)
    #     max_value = max(as_ints)
    #     #print(max_value)
    #     if max_value > threshold:
    #         print("More Than Threshold")
    #         count=0    
    #     else:
    #         print("Less Than Threshold")
    #         count+=1
    #     frames.append(data)
        

    # print("* done recording")

    # stream.stop_stream()
    # stream.close()
    # p.terminate()

    # wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    # wf.setnchannels(CHANNELS)
    # wf.setsampwidth(p.get_sample_size(FORMAT))
    # wf.setframerate(RATE)
    # wf.writeframes(b''.join(frames))
    # wf.close()

    client = speech_v1.SpeechClient()

    # storage_uri = 'gs://cloud-samples-data/speech/multi.wav'

    # The number of channels in the input audio file (optional)
    audio_channel_count = 1

    # When set to true, each audio channel will be recognized separately.
    # The recognition result will contain a channel_tag field to state which
    # channel that result belongs to
    enable_separate_recognition_per_channel = True

    # The language of the supplied audio
    language_code = "en-US"
    config = {
        "audio_channel_count": audio_channel_count,
        "enable_separate_recognition_per_channel": enable_separate_recognition_per_channel,
        "encoding": "LINEAR16",
        "language_code": language_code,
        # "sample_rate_hertz":44100
    }
    
    voice_file='tmp.wav'
    with io.open(voice_file,'rb') as f:
        audio_file = f.read()
    
    audio = types.RecognitionAudio(content=audio_file)
    response = client.recognize(config, audio)
    for result in response.results:
        # channel_tag to recognize which audio channel this result is for
        print(u"Channel tag: {}".format(result.channel_tag))
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))

    
if __name__=="__main__":
    sample_recognize()
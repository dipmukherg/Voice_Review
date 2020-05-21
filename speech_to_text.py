import requests
import os
import io
from google.cloud.speech_v1 import types
import json
import codecs
import base64



#os.environ['GOOGLE_APPLICATION_CREDENTIALS']='my-new-project-265705-90a669a5d4c2.json'
API_KEY="AIzaSyCCm76qtJakFpaI19D37LlBokhdoVdjKwM"

voice_file='output.wav'
with io.open(voice_file,'rb') as f:
    audio_file = f.read()


# Pass the audio data to an encoding function.
def encode_audio(audio):
  audio_content = audio.read()
  return base64.b64encode(audio_content)
#audio = types.RecognitionAudio(content=audio_file)
data = {
        "audio": {
            "content": None
        },
        "config": {
            "enableAutomaticPunctuation": True,
            "encoding": "LINEAR16",
            "languageCode": "en-US",
            "model": "default",
            "sampleRateHertz":44100,
            "audioChannelCount":2

        }
    }
#data_json = json.dumps(data)
r = requests.post('https://speech.googleapis.com/v1p1beta1/speech:recognize?key={}'.format(API_KEY),json=data)

print(r._content)
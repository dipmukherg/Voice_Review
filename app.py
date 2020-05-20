from flask import render_template,Flask,request
import requests
import record
import librosa
import soundfile as sf

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/messages', methods = ['POST'])
def api_message():
    f = open('./new.wav', 'wb')
    f.write(request.data)
    f.close()
    x,_ = librosa.load('./new.wav', sr=44100)
    sf.write('tmp.wav', x, 44100)
    record.sample_recognize()
    return "File Submitted"

if __name__=="__main__":
    app.run(debug=True)
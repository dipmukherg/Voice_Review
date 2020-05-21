from flask import render_template,Flask,request
import requests
import record
import librosa
import soundfile as sf

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/messages', methods = ['POST','GET'])
def api_message():
    f = open('./new.wav', 'wb')
    f.write(request.data)
    f.close()
    #print("Inside Main")
    x,_ = librosa.load('./new.wav', sr=44100)
    sf.write('tmp.wav', x, 44100)
    returned_text= record.sample_recognize()
    return returned_text


if __name__=="__main__":
    app.run(debug=True)
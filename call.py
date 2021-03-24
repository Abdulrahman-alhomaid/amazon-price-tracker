from flask import Flask
from flask_ngrok import run_with_ngrok
from twilio.twiml.voice_response import VoiceResponse


app = Flask(__name__)
run_with_ngrok(app)
@app.route("/voice" , methods=['POST' , 'GET'])

def voice():
    resp = VoiceResponse()

    resp.say('السلام عليكم عبدالرحمن, ألقي نطرة على بريدك الإلكتروني')

    return str(resp)

if __name__ == "__main__":
    app.run()
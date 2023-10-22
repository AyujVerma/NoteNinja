from flask import Flask
from flask import request
import delegate
from flask_cors import CORS
# from delegate import Delegate

api = Flask(__name__)
CORS(api)


@api.get('/output')
def my_profile():
    slides = request.args.get('slides')
    audio = request.args.get('audio')
    delegate.runner(audio=audio, ppt=slides)
    return audio


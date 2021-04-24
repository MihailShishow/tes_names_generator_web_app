from flask import Flask
from .views import *


def get_app(config=None):

    app = Flask(__name__)

    app.add_url_rule('/', 'index', index)

    app.add_url_rule('/dunmer', 'dunmer', dunmer)
    app.add_url_rule('/altmer', 'altmer', altmer)
    app.add_url_rule('/bosmer', 'bosmer', bosmer)
    app.add_url_rule('/orsimer', 'orsimer', orsimer)
    app.add_url_rule('/argonian', 'argonian', argonian)
    app.add_url_rule('/khajiit', 'khajiit', khajiit)
    app.add_url_rule('/breton', 'breton', breton)
    app.add_url_rule('/nord', 'nord', nord)
    app.add_url_rule('/redguard', 'redguard', redguard)
    app.add_url_rule('/imperial', 'imperial', imperial)

    return app

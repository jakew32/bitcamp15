from flask import Flask, jsonify
import logic, twitter

app = Flask(__name__)

import json

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/analyze/hashtag/<toparse>')
def parse_hashtag(toparse):
    song = logic.pick_song(twitter.hashtagSearch(toparse))
    return song.title + " - " + song.artist_name

@app.route('/analyze/username/<username>')
def parse_username(username):
    song = logic.pick_song(twitter.userSearch(username))
    return song.title + " - " + song.artist_name

if __name__ == '__main__':
    app.run(host='0.0.0.0')

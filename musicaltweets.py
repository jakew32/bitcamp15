from flask import Flask, jsonify
import logic, twitter

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/analyze/hashtag/<toparse>')
def parse_hashtag(toparse):
    song = logic.pick_song(twitter.hashtagSearch(toparse))
    return jsonify(song)

if __name__ == '__main__':
    app.run()

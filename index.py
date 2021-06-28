from flask import Flask, render_template, send_file
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<videoID>')
def downloadVideo(videoID):
    video = YouTube('https://www.youtube.com/watch?v=' + videoID)
    return send_file(video.streams.get_highest_resolution().download(), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
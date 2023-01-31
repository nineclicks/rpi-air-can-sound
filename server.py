from subprocess import check_output, Popen
from flask import Flask, send_from_directory
from time import time, sleep
from threading import Thread

app = Flask(__name__)

VIDEO_DIR = 'video/'

@app.route("/sound")
def hello_world():
    ts = str(int(time()))
    t = Thread(target = rec, args=(ts,))
    t.start()
    sleep(2)
    error = None
    try:
        check_output('amixer -Dhw:UACDemoV10 set PCM 85%'.split())
        check_output('aplay air_can.wav -Dhw:UACDemoV10'.split())
    except Exception:
        error = 'Error playing sound.'
    return {'video': f'{ts}.mp4', 'error': error}

@app.route("/<ts>.mp4")
def vid(ts):
    return send_from_directory(VIDEO_DIR, f'{ts}.mp4')

def rec(fn):
    cmds = [
        f'libcamera-vid -t 15000 --width 1280 --height 720 -o {VIDEO_DIR}{fn}.h264',
        f'ffmpeg -i {VIDEO_DIR}{fn}.h264 -c:v libx264 -preset ultrafast -crf 22  {VIDEO_DIR}{fn}.mp4',
        f'rm {VIDEO_DIR}{fn}.h264',
    ]

    for cmd in cmds:
        p = Popen(cmd.split())
        p.wait()

app.run(host='0.0.0.0', port=8080)

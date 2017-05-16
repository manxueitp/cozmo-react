from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='eventlet')

@app.route("/")
def index():
    return render_template(
        'home.html',async_mode=socketio.async_mode)

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
        'test.html',name=name)

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=5000)
     socketio.run(app)

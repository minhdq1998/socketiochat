from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit

import names

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abaskdjklfjaskldf'
socketio = SocketIO(app)

@app.route('/')
def index():
    if session.get('username') is None:
        random_name = names.get_full_name()
        session['username'] = random_name

    # for Debug purpose only 
    print(f"User {session['username']} connected")

    return render_template(
        'chatbox.html', 
        username  = session['username']
    )


@socketio.on('messaging event')
def handle_messaging_event(json):
    # Handling the messages
    print('received:' + str(json['message']))
    json['username'] = session['username']
    socketio.emit('message response', json)

if __name__ == '__main__':
    socketio.run(app, debug=True)
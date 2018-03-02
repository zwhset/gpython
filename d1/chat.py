# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect
from flask_socketio import SocketIO, rooms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sldjfalsfnwlemnw'

socketio = SocketIO(app)

# 添加url跳转，免得人直接访问 / 不知道怎么办
@app.route('/')
@app.route('/chats')
def index():
    return redirect('/chats/1')

@app.route('/chats/<int:room_id>')
def chats(room_id=1):
    return render_template('chat.html', room_id=room_id)

@socketio.on('chat_send')
def chat_send(json):
    room_id = None
    if json.get('room_id', None):
        room_id = json['room_id']

    socketio.emit('chat_recv_{room_id}'.format(room_id=room_id), json)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080, debug=True)
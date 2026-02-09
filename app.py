import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template
from flask_socketio import SocketIO, send
import mysql.connector

app = Flask(__name__)
socketio = SocketIO(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rahul@123",
    database="chatdb"
)

@app.route('/')
def index():
    return render_template("chat.html")

@socketio.on('message')
def handle_message(data):
    username = data['username']
    message = data['message']

    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO messages (username, message) VALUES (%s, %s)",
        (username, message)
    )
    db.commit()

    send(data, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)

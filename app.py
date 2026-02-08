from flask import Flask, render_template
from flask_socketio import SocketIO, send
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'
socketio = SocketIO(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rahul@123",
    database="chatapp"
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    username = data['username']
    message = data['message']

    cursor.execute(
        "INSERT INTO messages (username, message) VALUES (%s, %s)",
        (username, message)
    )
    db.commit()

    send(data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)

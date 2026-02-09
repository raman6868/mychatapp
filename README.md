
# 💬 Real-Time Chat Application  
A beautiful real-time chatting web application built using **Flask, Socket.IO, MySQL, HTML, and CSS**.  
This application allows multiple devices to connect and chat instantly over the same network.

---

## ✨ Features

- Real-time messaging using WebSockets
- Messages sent by you appear on the **right side**
- Messages from others appear on the **left side**
- Aesthetic UI with transitions and effects
- Custom logo and background
- Purple themed design
- Multiple devices can connect simultaneously
- Messages stored in MySQL database

---

## 🛠 Technologies Used

- Python
- Flask
- Flask-SocketIO
- MySQL
- HTML5
- CSS3

---

## 📁 Project Structure

```

chat_app/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── chat.html
│
├── static/
│   ├── style.css
│   ├── logo.png
│   └── background.png

```

---

## ⚙️ Installation Guide

### 1. Clone or Download the Project

Download or copy the project folder to your system.

---

### 2. Install Dependencies

Open terminal inside the project folder and run:

```

pip install flask flask-socketio mysql-connector-python eventlet

````

---

### 3. Setup MySQL Database

Open MySQL and run:

```sql
CREATE DATABASE chatdb;

USE chatdb;

CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    message TEXT
);
````

---

### 4. Configure Database

Open **app.py** and update:

```python
user="root",
password="YOUR_PASSWORD",
database="chatdb"
```

---

### 5. Run the Application

```
python app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

## 📱 Access from Another Device

1. Find your IP address:

```
ipconfig
```

Example:

```
192.168.1.5
```

2. Open on another laptop or phone:

```
http://192.168.1.5:5000
```

Make sure both devices are connected to the same Wi-Fi.


---


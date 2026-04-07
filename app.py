from flask import Flask, render_template
from flask_socketio import SocketIO
import random
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def telemetry_thread():
    while True:
        # Simulate telemetry data
        data = {
            "pitch": round(random.uniform(-30, 30), 2),
            "roll": round(random.uniform(-45, 45), 2),
            "yaw": round(random.uniform(0, 360), 2),
            
            "alt": round(random.uniform(0, 3600), 2),            
            "speed": round(random.uniform(0, 300), 2),
            "stateAntain": round(random.uniform(0, 13), 2),
            
            "battery": round(random.uniform(20, 100), 2),
            "batteryValt": round(random.uniform(0, 14), 2),
            "batteryHour": round(random.uniform(10, 300), 2),
            
            "lat": round(25.0 + random.uniform(-0.01, 0.01), 6),
            "lon": round(55.0 + random.uniform(-0.01, 0.01), 6)
        }
        
        


        socketio.emit('telemetry', data)
        socketio.sleep(1)  # 10 Hz update rate

if __name__ == '__main__':
    # Start telemetry thread
    socketio.start_background_task(target=telemetry_thread)
    socketio.run(app, host='0.0.0.0', port=5000)


from flask import Flask, Response
import serial
import cv2
import numpy as np

app = Flask(__name__)

# Update the serial port to match the one your Arduino is connected to
serial_port = "COM13"  # Update to the correct port (e.g., COMx on Windows or /dev/ttyUSB0 on Linux)
baud_rate = 9600  # Match the baud rate set in the Arduino code

# Open the serial port to communicate with the Arduino
ser = serial.Serial(serial_port, baud_rate)

# Initialize the camera frame size based on the Arduino camera resolution
width, height = 176, 144  # QCIF resolution used in your code

# Define the frame size (QCIF, RGB565, 2 bytes per pixel)
bytes_per_frame = width * height * 2

if not ser.isOpen():
    ser.open()

def gen_frames():
    while True:
        # Read data from the Arduino via serial (read one frame at a time)
        data = ser.read(bytes_per_frame)
        if len(data) == bytes_per_frame:
            # Convert the byte data into a NumPy array and decode it into an image
            frame = np.frombuffer(data, dtype=np.uint8).reshape((height, width, 2))
            frame = cv2.cvtColor(frame, cv2.COLOR_YUV2BGR_YV12)  # Convert to BGR format for Flask streaming

            # Encode the frame as JPEG for streaming
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue
            frame = buffer.tobytes()

            # Yield the frame to the browser
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def index():
    return "Live Camera Feed from Arduino! Access /video for live feed."

@app.route('/video')
def video():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

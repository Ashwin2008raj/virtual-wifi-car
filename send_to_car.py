# send_to_car.py

import socket
import time

ESP32_IP = "192.168.1.184"  # Match your ESP32 static IP
PORT = 80
RETRY_ATTEMPTS = 5          # Number of retries
RETRY_DELAY = 1             # Delay between retries in seconds

def send_command(command):
    for attempt in range(RETRY_ATTEMPTS):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2)  # Timeout for connection and send
                s.connect((ESP32_IP, PORT))
                s.sendall((command + "\n").encode())
                print(f"✅ Sent: {command}")
                return  # Exit after success
        except Exception as e:
            print(f⚠️ Attempt {attempt + 1}/{RETRY_ATTEMPTS} failed: {e}")
            time.sleep(RETRY_DELAY)

    print("❌ Failed to connect to the car after several attempts.")

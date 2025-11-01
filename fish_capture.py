import cv2
from ultralytics import YOLO
import serial
import time
from datetime import datetime

# Connect to Arduino
arduino = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)

# Load YOLO model (pretrained)
model = YOLO("yolov8n.pt")

def detect_objects():
    cap = cv2.VideoCapture(0)
    time.sleep(2)  # camera time to start

    print("\n[INFO] Starting object detection...")
    ret, frame = cap.read()
    if not ret:
        print("Camera not available.")
        return 0

    results = model(frame)
    detections = results[0].boxes
    count = len(detections)

    print(f"[INFO] Objects detected: {count}")
    cap.release()
    return count

def send_to_arduino(count):
    if count > 0:
        arduino.write(f"{count}\n".encode())  # send number as text
        print(f"[INFO] Sent {count} to Arduino.")
    else:
        print("[INFO] No objects detected, nothing sent.")

# Run forever every 2 hours
while True:
    print(f"\n====== Cycle started at {datetime.now().strftime('%H:%M:%S')} ======")
    
    obj_count = detect_objects()
    send_to_arduino(obj_count)
    
    print("[INFO] Waiting 2 hours before next detection...")
    time.sleep(2 * 60 * 60)  # 2 hours
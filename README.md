# 🐠 Smart Fish Feeder System — AI + IoT Based Automation

An ongoing project that automates fish feeding using **computer vision (OpenCV + YOLO)** and **microcontroller-based control (Arduino)**.  
The system aims to detect the number of fish in an aquarium using a trained **fish detection model** and rotate a **servo motor** that many times to dispense food — ensuring accurate, efficient, and adaptive feeding.

---

## 🚀 Project Overview

Traditional automatic feeders release food on fixed timers, leading to overfeeding or wastage.  
This project introduces an **intelligent feeding mechanism** that combines **AI-driven fish detection** with **hardware actuation** through Arduino.

- Detects fish in real-time using **YOLO (You Only Look Once)** object detection model.  
- Sends the detected count to **Arduino** via **serial communication**.  
- Arduino controls a **servo motor** that rotates that many times to release food.  
- Designed for **scalability**, with plans to integrate **ESP32** for IoT-based remote monitoring through **Blynk**.

---

## 🧠 Current Implementation (Phase 1)

- **Hardware Used**
  - Arduino UNO  
  - Servo Motor  
  - Jumper Wires  
  - USB connection to computer (for serial communication)  
  - Webcam (for live detection)

- **Software Tools**
  - Python  
  - OpenCV  
  - YOLOv8 (Ultralytics)  
  - Arduino IDE  
  - PySerial

- **How It Works**
  1. Webcam captures a live frame of the aquarium.  
  2. YOLO model detects objects (currently general detection).  
  3. The number of detected fish (objects) is counted in Python.  
  4. Count is sent to Arduino via serial port.  
  5. Arduino rotates the servo motor the same number of times → food is dispensed.

---

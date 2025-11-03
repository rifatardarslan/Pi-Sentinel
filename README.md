For Turkish documentation, see [README_TR.md](./README_TR.md).

# 🛰️ Pi Sentinel — Smart Home Security System (AI + IoT)

**Pi Sentinel** integrates Artificial Intelligence (AI) and Internet of Things (IoT) technologies to provide a low-cost, portable, and energy-efficient smart home security system on **Raspberry Pi Zero 2 W**.
When motion is detected by a PIR sensor, the camera activates; frames are analyzed by **YOLOv8** to detect humans, animals, or vehicles.
If a human is detected, a **face recognition** module (OpenCV + Dlib) distinguishes known individuals and triggers alerts only for unknown ones — minimizing false alarms.

The system runs locally without cloud dependency, managed securely via **SSH**, ensuring privacy and data integrity.

---

## ⚙️ Features
- Real-time object detection using YOLOv8
- Face recognition to minimize false alerts
- Optimized for Raspberry Pi Zero 2 W
- Remote control via SSH
- Offline, privacy-first design
- Low power consumption and compact size

---

## 🧠 Technologies Used
- Python 3.x
- OpenCV
- Dlib
- Ultralytics YOLOv8
- Raspberry Pi OS / Armbian
- SSH

---

## 🔧 Installation
```bash
pip install -r requirements.txt
python pi_sentinel.py
```

---

## 🧩 Model File (Important ⚠️)
The YOLOv8n model file is **not included** in this repository due to file size limitations.
Please **download it manually** from the official Ultralytics source:

👉 [Download yolov8n.pt](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt)

Place the file in the same folder as `pi_sentinel.py` before running the script.

```
Pi-Sentinel/
├── pi_sentinel.py
├── yolov8n.pt
├── requirements.txt
├── README.md
└── README_TR.md
```

---

## 🧪 Technology Readiness Level (TRL)
The project has reached **TRL 4**, validated through real-world prototype testing.

---

## 🏫 Academic and Industrial Contribution
**Pi Sentinel** was showcased at **Afyon Kocatepe University Project Fair** as an example of an AI-powered, energy-efficient, low-cost smart security solution.

It provides a robust foundation for **academic research**, **small businesses**, and **individual users** seeking a secure and privacy-focused alternative.

---

## 📄 License
This project is open source under the **MIT License**.  
See [LICENSE](./LICENSE) for details.


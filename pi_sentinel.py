import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera not found! Ensure the camera is connected and enabled.")
    raise SystemExit(1)

mirror_enabled = True
print("✅ Started. Press 'ESC' to quit, 'M' to toggle mirror mode.")

try:
    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            print("⚠️ Frame could not be read from camera.")
            break

        if mirror_enabled:
            frame = cv2.flip(frame, 1)

        results = model.predict(source=frame, conf=0.5, stream=True, verbose=False)

        for r in results:
            annotated = r.plot()
            cv2.imshow("Pi Sentinel - YOLOv8 Detection", annotated)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC
            print("🛑 Exit requested.")
            break
        elif key == ord('m'):
            mirror_enabled = not mirror_enabled
            print(f"🔁 Mirror: {'ON' if mirror_enabled else 'OFF'}")

except KeyboardInterrupt:
    print("
🧩 Interrupted by user.")
finally:
    cap.release()
    cv2.destroyAllWindows()
    print("🎬 Camera closed and resources released.")

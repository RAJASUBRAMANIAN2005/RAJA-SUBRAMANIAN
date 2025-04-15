import cv2
from ultralytics import YOLO
import pyttsx3
import time
import RPi.GPIO as GPIO

LEFT_MOTOR_FORWARD = 17
LEFT_MOTOR_BACKWARD = 18
RIGHT_MOTOR_FORWARD = 22
RIGHT_MOTOR_BACKWARD = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

motor_pins = [LEFT_MOTOR_FORWARD, LEFT_MOTOR_BACKWARD, RIGHT_MOTOR_FORWARD, RIGHT_MOTOR_BACKWARD]
for pin in motor_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def stop_motors():
    for pin in motor_pins:
        GPIO.output(pin, GPIO.LOW)

def move_left():
    GPIO.output(LEFT_MOTOR_FORWARD, GPIO.LOW)
    GPIO.output(LEFT_MOTOR_BACKWARD, GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_FORWARD, GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_BACKWARD, GPIO.LOW)

def move_right():
    GPIO.output(LEFT_MOTOR_FORWARD, GPIO.HIGH)
    GPIO.output(LEFT_MOTOR_BACKWARD, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_FORWARD, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_BACKWARD, GPIO.HIGH)

def move_forward():
    GPIO.output(LEFT_MOTOR_FORWARD, GPIO.HIGH)
    GPIO.output(LEFT_MOTOR_BACKWARD, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_FORWARD, GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_BACKWARD, GPIO.LOW)

model = YOLO("yolov8n.pt")  

engine = pyttsx3.init()
engine.setProperty('rate', 150)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

FRAME_WIDTH = 640
CENTER_TOLERANCE = 50
last_direction = ""
last_speak_time = 0
speak_delay = 2

follow_target = "person"

print("🤖 Smart Object-Following Robot is Running...")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(source=frame, conf=0.5, verbose=False)
        boxes = results[0].boxes
        annotated_frame = results[0].plot()

        direction = ""

        if boxes is not None and len(boxes) > 0:
            for box in boxes:
                cls_id = int(box.cls[0])
                label = results[0].names[cls_id]

                if label == follow_target:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    object_center_x = (x1 + x2) // 2
                    frame_center_x = FRAME_WIDTH // 2

                    if object_center_x < frame_center_x - CENTER_TOLERANCE:
                        direction = "left"
                    elif object_center_x > frame_center_x + CENTER_TOLERANCE:
                        direction = "right"
                    else:
                        direction = "center"
                    break  # Only follow first matching object

        current_time = time.time()
        if direction:
            if direction != last_direction or current_time - last_speak_time > speak_delay:
                print(f"🔊 Go {direction}")

                engine.say(f"Go {direction}")
                engine.runAndWait()

                if direction == "left":
                    move_left()
                elif direction == "right":
                    move_right()
                elif direction == "center":
                    move_forward()

                last_direction = direction
                last_speak_time = current_time
        else:
            stop_motors()

        cv2.imshow("Smart Object Follower", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("🛑 Interrupted by user")

finally:
    stop_motors()
    cap.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
    print("✅ Cleanup done. Exiting.")

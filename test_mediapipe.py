import mediapipe as mp, cv2, numpy as np
import time

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(model_complexity=2)

# Try different camera indices
cap = None
for i in range(3):
    temp_cap = cv2.VideoCapture(i)
    if temp_cap.isOpened():
        print(f"Camera {i} is available")
        cap = temp_cap
        break
    temp_cap.release()

if cap is None or not cap.isOpened():
    print("Error: Could not open any webcam")
    exit(1)

# Give camera time to initialize
time.sleep(1)

ret, frame = cap.read()
if not ret:
    print("Error: Could not read frame")
    cap.release()
    exit(1)

print(f"Frame shape: {frame.shape}")

rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
result = pose.process(rgb)
if result.pose_landmarks:
    print('Pose detected! Landmarks:', len(result.pose_landmarks.landmark))
else:
    print('No pose detected in frame (this is normal if no person is in front of camera)')
cap.release()


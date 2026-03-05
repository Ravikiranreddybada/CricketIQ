import mediapipe as mp, cv2, numpy as np

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(model_complexity=2)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit(1)

print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame")
        break
    
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb)
    
    if result.pose_landmarks:
        print('Pose detected! Landmarks:', len(result.pose_landmarks.landmark))
        break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
print("Done!")


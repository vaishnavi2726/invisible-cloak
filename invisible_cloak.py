import cv2
import numpy as np
import time

# Start webcam
cap = cv2.VideoCapture(0)
time.sleep(3)

# Capture background
background_frames = []
for i in range(30):
    ret, frame = cap.read()
    if ret:
        background_frames.append(np.flip(frame, axis=1))
background = np.median(background_frames, axis=0).astype(np.uint8)

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break
    
    img = np.flip(img, axis=1)
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Red cloak mask
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Refine mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask = cv2.dilate(mask, np.ones((3,3), np.uint8), iterations=1)

    # Invisibility effect
    res1 = cv2.bitwise_and(background, background, mask=mask)
    res2 = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Invisible Cloak", final_output)

    if cv2.waitKey(1) == 27:  # Esc to exit
        break

cap.release()
cv2.destroyAllWindows()

import cv2
import mediapipe as mp
import pyautogui
import math
import numpy as np

# Initialize webcam
cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()

print(screen_width, screen_height)


# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1)


# For smoothing mouse movement
prev_x, prev_y = 0, 0
smoothening = 5


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror image
    h, w, c = frame.shape

    # Convert to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            # Get fingertip coordinates
            lm_list = []
            for id, lm in enumerate(handLms.landmark):
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            if lm_list:
                # Index fingertip
                x1, y1 = lm_list[8]
                # Thumb tip
                x2, y2 = lm_list[4]

                # Map coordinates to screen
                screen_x = np.interp(x1, [0, w], [0, screen_width])
                screen_y = np.interp(y1, [0, h], [0, screen_height])

                # Smooth movement
                curr_x = prev_x + (screen_x - prev_x) / smoothening
                curr_y = prev_y + (screen_y - prev_y) / smoothening
                pyautogui.moveTo(curr_x, curr_y)
                prev_x, prev_y = curr_x, curr_y

                # Click detection: distance between index finger and thumb
                distance = math.hypot(x2 - x1, y2 - y1)
                if distance < 40:  # adjust threshold
                    pyautogui.click()
                    cv2.circle(frame, (x1, y1), 15, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Virtual Mouse", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

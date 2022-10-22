from turtle import right
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=2,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            left_most = right_most = top_most = bottom_most = -1
            # for y, top pixels are smaller numbers
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y*h)
                if left_most == -1 or cx < left_most:
                    left_most = cx
                if right_most == -1 or cx > right_most:
                    right_most = cx
                if bottom_most == -1 or cy > bottom_most:
                    bottom_most = cy
                if top_most == -1 or cy < top_most:
                    top_most = cy
                # if id ==0:
                cv2.circle(img, (cx, cy), 3, (255, 0, 255), cv2.FILLED)

            if not (left_most < 0 or right_most < 0 or top_most < 0 or bottom_most < 0):
                multiplier = 0.5
                dx = (right_most - left_most) * multiplier
                dy = (bottom_most - top_most) * multiplier

                cv2.rectangle(img, (left_most - dx, top_most - dy),
                              (right_most + dx, bottom_most + dy), (255, 0, 255), 3)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

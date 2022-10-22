from turtle import left, right
import cv2
from matplotlib import image
import mediapipe as mp
import time
import torch
from model import Net
import numpy as np
import torchvision.transforms as transforms
from LettersDataset import testset
import matplotlib.pyplot as plt
import keyboard
import torchvision.utils as tvu

classes = list(testset.dataset.class_to_idx.keys())
maxImages = 50
currImages = 0
test = True


def process_hand(img, left_most, right_most, bottom_most, top_most):
    multiplier = 1.7
    x_diff = (right_most - left_most)
    y_diff = (bottom_most - top_most)

    dx = int(x_diff * multiplier) + 50
    dy = int(y_diff * multiplier) + 50

    mid = ((left_most + right_most)//2, (bottom_most + top_most) // 2)
    if x_diff > y_diff:
        start = (mid[0] - dx//2, mid[1] - dx//2)
        end = (mid[0] + dx//2, mid[1] + dx//2)

    else:
        start = (mid[0] - dy//2, mid[1] - dy//2)
        end = (mid[0] + dy//2, mid[1] + dy//2)
    # end = (right_most + dx, bottom_most + dy)
    height, width, _ = img.shape
    if start[0] < 0 or end[0] > width or start[1] < 0 or end[1] > height:
        return

    color = (255, 0, 255)
    # cv2.rectangle(img, start, end, color, 3)
    if start[0] < 0:
        start = (0, start[1])
    if start[1] < 0:
        start = (start[0], 0)
    if end[0] < 0:
        end = (0, end[1])
    if end[1] < 0:
        end = (end[0], 0)

    cropped = img[start[1]: end[1], start[0]: end[0]]
    transform = transforms.Compose(
        [transforms.ToTensor(), transforms.Resize(200)])
    batch = transform(cropped).unsqueeze(0)

    if keyboard.read_key() == "n" and currImages < maxImages:
        tvu.save_image(batch, "test" + currImages + ".jpg")
        currImages += 1
    cv2.imshow("cropped", cropped)


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 10)

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
    img_copy = img.copy()
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
                process_hand(img_copy, left_most, right_most,
                             bottom_most, top_most)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

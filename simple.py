import cv2
import mediapipe as mp
import numpy as np
import pyautogui



mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

capture = cv2.VideoCapture(0)
with mp_hands.Hands(min_tracking_confidence=0.8, min_detection_confidence=0.5, max_num_hands=1) as hands:
    while capture.isOpened():
        # reading the frame
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)
        # converting image to rgb
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # process Images
        image.flags.writeable = False
        result = hands.process(image)
        # writing the images to the app
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # after the results of hands processed image  the hand landmarks if true
        lmlist=[]
        if result.multi_hand_landmarks:
            for  hand in result.multi_hand_landmarks:
                myhands=result.multi_hand_landmarks[0]
                for id,lm in enumerate(hand.landmark):
                     h, w, c = image.shape
                     cx,cy= int(lm.x*w),int(lm.y*h)
                     lmlist.append([id,cx,cy])
                     print(id,cx,cy)
            mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)
        if len(lmlist)!=0:

            if lmlist[8][2]<lmlist[7][2]:
                print("nothing")
            else:
                pyautogui.press('space')

        cv2.imshow("Faizer Hand Detection application", image)
        if cv2.waitKey(120) & 0xFF == ord('s'):
            break

capture.release()
cv2.destroyAllWindows()

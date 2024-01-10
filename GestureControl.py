import cv2
import keyboard
import HndTrck
import time
import HndTrck as Ht

Hands = HndTrck.DetectHand(Num_hands = 1)
Cpt = cv2.VideoCapture(0)
Xmid = 320
Ymid = 180
cooldown_duration = 0.7
last_press_time = {'left': 0, 'up': 0, 'right': 0, 'down': 0}

while True:
    success, Img = Cpt.read()
    Img = Hands.FindHand(Img)
    Lms = Hands.FindPos(Img, draw = False)
    if len(Lms) != 0:
        Idx1 = Lms[8]
        Idx2 = Lms[4]
        F1x, F1y = Idx1[1], Idx1[2]
        F2x, F2y = Idx2[1], Idx2[2]
        
        if Ymid > F1y & (Ymid - F1y) > 50:
            if Ymid > F2y & (Ymid - F2y) > 50:
                if time.time() - last_press_time['up'] > cooldown_duration:
                    print("Up")
                    keyboard.press_and_release('up_arrow')
                    last_press_time['up'] = time.time()
        elif F1y > Ymid & (F1y - Ymid) > 50:
            if F2y > Ymid & (F2y - Ymid) > 50:
                if time.time() - last_press_time['down'] > cooldown_duration:
                    print("down")
                    keyboard.press_and_release('down_arrow')
                    last_press_time['down'] = time.time()
        elif F1x > Xmid & (F1x - Xmid) > 50:
            if F2x > Xmid & (F2x - Xmid) > 50:
                if time.time() - last_press_time['left'] > cooldown_duration:
                    print("Left")
                    keyboard.press_and_release('left_arrow')
                    last_press_time['left'] = time.time()
        elif Xmid > F1x & (Xmid - F1x) > 50:
            if Xmid > F2x & (Xmid - F2x) > 50:
                if time.time() - last_press_time['right'] > cooldown_duration:
                    print("Right")
                    keyboard.press_and_release('right_arrow')
                    last_press_time['right'] = time.time()

    cv2.line(Img, (320, 0), (320, 360), (0, 100, 255), 1)
    cv2.line(Img, (0, 180), (640, 180), (0, 100, 255), 1)
    cv2.rectangle(Img, (310, 90), (330, 270), (0, 255, 0), 1)
    cv2.rectangle(Img, (230, 170), (410, 190), (0, 255, 0), 1)
    cv2.circle(Img, (320, 180), 5, (255, 255, 0), cv2.FILLED)
    Img = cv2.flip(Img, 1)
    cv2.imshow("Window", Img)
    if cv2.waitKey(1) & 0xFF == ord('p'):
        break

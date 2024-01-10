import cv2
import mediapipe as mp
import time

class DetectHand():
    def __init__(self, mode = False, Num_hands = 2, Cmplxt = 1, DtctConf_min = 0.5, TrckConf_min = 0.5):
        self.mode = mode
        self.max_num_hands = Num_hands
        self.model_complexity = Cmplxt
        self.min_detection_confidence = DtctConf_min
        self.min_tracking_confidence = TrckConf_min
        self.tipID = [4, 8, 12, 16, 20]

        self.MPhands = mp.solutions.hands
        self.hands = self.MPhands.Hands(
            self.mode,
            self.max_num_hands,
            self.model_complexity,
            self.min_detection_confidence,
            self.min_tracking_confidence
        )
        self.MPdraw = mp.solutions.drawing_utils

    def FindHand(self, Img, draw = True):
        ImgRGB = cv2.cvtColor(Img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(ImgRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                if draw:
                    self.MPdraw.draw_landmarks(Img, handlms, self.MPhands.HAND_CONNECTIONS)
        return Img

    def FindPos(self, Img, HandNo = 0, draw = True):
        self.lmlist = []
        if self.results.multi_hand_landmarks:
            TheHand = self.results.multi_hand_landmarks[HandNo]
            for Id, lm in enumerate(TheHand.landmark):
                ht, wd, ch = Img.shape
                cx, cy = int(lm.x * wd), int(lm.y * ht)
                # print(cx, cy)
                self.lmlist.append([Id, cx, cy])
                if draw:
                    cv2.circle(Img, (cx, cy), 7, (255, 0, 0), cv2.FILLED)
        return self.lmlist

    def FingerCount(self):
        fingers = []
        if self.lmlist[4][1] < self.lmlist[2][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        for Id in range(1, 5):
            if self.lmlist[self.tipID[Id]][2] < self.lmlist[self.tipID[Id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers


def main():
    Cpt = cv2.VideoCapture(0)
    detector = DetectHand()
    while True:
        success, Img = Cpt.read()
        Img = detector.FindHand(Img)
        lmlist = detector.FindPos(Img, draw = False)
        if len(lmlist) != 0:
            print(lmlist[8])

        cv2.imshow("Cam", Img)
        if cv2.waitKey(1) & 0xFF == ord('p'):
            break


if __name__ == "__main__":
    main()
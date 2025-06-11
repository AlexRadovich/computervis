import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, min_det=0.7, min_trk=0.5):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=min_det,
            min_tracking_confidence=min_trk
        )
        self.mp_draw = mp.solutions.drawing_utils

    def get_index_x(self, frame):
        """
        Returns the x-pixel of the first detected hand's index fingertip (landmark 8),
        or None if no hand detected.
        """
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)
        if results.multi_hand_landmarks:
            lm = results.multi_hand_landmarks[0].landmark[8]
            h, w, _ = frame.shape
            return int(lm.x * w)
        return None

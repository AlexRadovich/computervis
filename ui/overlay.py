import cv2
from config.settings import FRAME_WIDTH, FRAME_HEIGHT

class Overlay:
    def __init__(self, height=60):
        self.bar_height = height

    def draw(self, frame, fader, x_left, x_right):
        """
        Draws a crossfader bar at the bottom of the frame.
        fader: [0.0..1.0], x_left/right: pixel bounds.
        """
        h, w, _ = frame.shape
        y0 = h - self.bar_height
        # background
        cv2.rectangle(frame,
                      (x_left, y0),
                      (x_right, h),
                      (50, 50, 50),
                      thickness=-1)
        # fader indicator
        fx = int(x_left + fader * (x_right - x_left))
        cv2.line(frame,
                 (fx, y0),
                 (fx, h),
                 (0, 220, 0),
                 thickness=4)
        # labels
        cv2.putText(frame, 'Deck A', (x_left, y0 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200,200,200), 1)
        cv2.putText(frame, 'Deck B', (x_right - 60, y0 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200,200,200), 1)
        return frame

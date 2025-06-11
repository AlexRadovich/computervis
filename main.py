import cv2

from config.settings           import (CAMERA_INDEX,
                                       FRAME_WIDTH,
                                       FRAME_HEIGHT)
from vision.hand_tracker       import HandTracker
from vision.gesture_recognizer import GestureRecognizer
from audio.mixer               import Mixer
from ui.overlay                import Overlay

def main():
    # ——— Setup camera ———
    cap = cv2.VideoCapture(CAMERA_INDEX)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,  FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    # ——— Initialize modules ———
    tracker    = HandTracker()
    # For MVP we use the full frame width as fader range:
    x_left, x_right = 0, FRAME_WIDTH
    recognizer = GestureRecognizer(x_left, x_right)
    mixer      = Mixer()
    overlay    = Overlay()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # <-- FLIP the frame horizontally here -->
        frame = cv2.flip(frame, 1)

        # 1) Get fingertip X
        x_px = tracker.get_index_x(frame)

        # 2) Compute fader & smooth
        fader_raw = recognizer.compute_fader(x_px)
        fader      = recognizer.smooth(fader_raw)

        # 3) Apply crossfader
        mixer.set_crossfader(fader)

        # 4) Draw UI overlay
        out_frame = overlay.draw(frame, fader, x_left, x_right)

        cv2.imshow('Virtual DJ Mixer', out_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

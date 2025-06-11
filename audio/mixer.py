from audio.deck import Deck
from config.settings import LOOP_A_PATH, LOOP_B_PATH

class Mixer:
    def __init__(self):
        # Deck A on channel 0, Deck B on channel 1
        self.deckA = Deck(LOOP_A_PATH, channel_id=0)
        self.deckB = Deck(LOOP_B_PATH, channel_id=1)
        self.deckA.play()
        self.deckB.play()

    def set_crossfader(self, value):
        """
        value=0.0 → only Deck A,
        value=1.0 → only Deck B,
        linear crossfade in between.
        """
        self.deckA.set_volume(1 - value)
        self.deckB.set_volume(value)

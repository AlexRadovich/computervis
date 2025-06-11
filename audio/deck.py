import pygame

class Deck:
    def __init__(self, file_path, channel_id):
        # Initialize mixer once on first deck
        pygame.mixer.init()
        self.sound   = pygame.mixer.Sound(file_path)
        self.channel = pygame.mixer.Channel(channel_id)

    def play(self):
        # loops=-1 → infinite loop
        self.channel.play(self.sound, loops=-1)

    def set_volume(self, vol):
        """vol in [0.0 .. 1.0]"""
        self.channel.set_volume(vol)

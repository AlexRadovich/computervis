class GestureRecognizer:
    def __init__(self, x_left, x_right, alpha=0.2):
        self.x_left = x_left
        self.x_right = x_right
        self.alpha = alpha
        self.current = 0.5  # start fader centered

    def compute_fader(self, x_px):
        """Clamp x_px into [x_left, x_right] and normalize to [0.0, 1.0]."""
        if x_px is None:
            return self.current
        x = max(min(x_px, self.x_right), self.x_left)
        return (x - self.x_left) / (self.x_right - self.x_left)

    def smooth(self, new_val):
        """Exponential moving average to prevent jitter."""
        self.current = self.alpha * new_val + (1 - self.alpha) * self.current
        return self.current

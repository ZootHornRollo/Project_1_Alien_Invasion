class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialise game settings."""
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # Screen settings
        self.screen_width = 1440
        self.screen_height = 900
        self.bg_colour = (255, 255, 255)

        # Ship settings
        self.ship_speed = 1.5
class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        
        # Screen settings
        self.screen_width = 1200   # Screen width in pixels
        self.screen_height = 580  # Screen height in pixels
        self.bg_color = (230, 230, 230)  # Background color (RGB tuple)
        self.ship_speed = 0.75
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

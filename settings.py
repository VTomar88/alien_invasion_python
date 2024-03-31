class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.alien_speed_factor = None
        self.fleet_direction = None
        self.alien_points = None
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        self.fleet_drop_speed = 2
        # How quickly the game speed up
        self.speedup_scale = 0.2
        # How quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        # Alien settings
        self.alien_speed_factor = 0.2
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.alien_speed_factor += self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        

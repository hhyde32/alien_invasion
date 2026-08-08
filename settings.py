class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's static settings."""
        # Sreen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # Alien settings
        self.fleet_drop_speed = 30


        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """Initialise_dynamic_settings that change throughout the game."""
        self.ship_speed = 7.0
        self.bullet_speed = 15.0
        self.alien_speed = 2.0

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale







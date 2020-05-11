class Settings:
    """Store all Alien Invasion settings"""

    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # Alien settigns
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction 1 = right; -1 = left
        self.fleet_direction = 1
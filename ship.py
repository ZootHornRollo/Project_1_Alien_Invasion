import pygame


class Ship:
    """A class to manage the player's ship"""

    def __init__(self, ai_game):
        """Initialise the ship and set it's starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get it's rect
        self.image = pygame.image.load('images/player_ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom centre of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store the decimal value of the ships x position
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False
        
    def bliteme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag"""
        # update the ship's x value, not the rect and collision detect when the ship hits edge of screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x

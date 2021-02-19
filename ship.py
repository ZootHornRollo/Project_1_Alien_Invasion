import pygame


class Ship:
    """A class to manage the player's ship"""

    def __init__(self, ai_game):
        """Initialise the ship and set it's starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get it's rect
        self.image = pygame.image.load('images/player_ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom centre of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
    def bliteme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)

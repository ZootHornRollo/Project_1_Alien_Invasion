import sys

import pygame

from settings import Settings

from ship import Ship


class AlienInvasion:
    """Main game class to manage game assets and behaviour."""

    def __init__(self):
        """Initialise the game and create game resources."""
        pygame.init()
        # create a Settings object attribute
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        #  Set background colour
        self.bg_colour = self.settings.bg_colour

    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keyboard and mouse events"""
        # monitor keyboard and mouse input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # move the ship to the right as long as key is held down
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # move the ship left
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update images on screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_colour)
        self.ship.bliteme()
        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # make game instance and run the game
    ai = AlienInvasion()
    ai.run_game()

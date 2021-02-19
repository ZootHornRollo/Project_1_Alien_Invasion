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
            # monitor keyboard and mouse input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw the screen through each pass of the while loop
            self.screen.fill(self.settings.bg_colour)
            self.ship.bliteme()

            # Make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # make game instance and run the game
    ai = AlienInvasion()
    ai.run_game()

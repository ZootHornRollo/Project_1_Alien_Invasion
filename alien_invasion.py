import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Main game class to manage game assets and behaviour."""

    def __init__(self):
        """Initialise the game and create game resources."""
        pygame.init()
        # create a Settings object attribute
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        #  Set background colour
        self.bg_colour = self.settings.bg_colour

    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keyboard and mouse events"""
        # monitor keyboard and mouse input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_colour)
        self.ship.bliteme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # make game instance and run the game
    ai = AlienInvasion()
    ai.run_game()

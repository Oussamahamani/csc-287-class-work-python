import sys
import pygame
from settings import Settings
from ship import Ship
class Game:
    """Template class for PyGame."""

    def __init__(self):
        """Initialize the game, and the screen."""
        pygame.init()
        self.game_settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([self.game_settings.screen_width,self.game_settings.screen_height])
        pygame.display.set_caption("Arcade Game!")
        self.ship = Ship(self)
        self.ship2 = Ship(self,"./images/alien.png")
        self.ship3 = Ship(self,"./images/alien2.png")
    def run_game(self):
        """The main game loop."""
        while True:
            # Get latest events from the user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Update any game elements
            # Redraw the screen
            self.screen.fill(self.game_settings.bg_color)
            self.ship.blitme(None,None)
            self.ship2.blitme(100,100)
            self.ship3.blitme(500,500)
            
            
            # draws the screen
            pygame.display.flip()

            # Wait a bit;  this controls the frame rate
            # When set to, e.g. 60, PyGame does its best
            # to run the loop 60 times / second.
            self.clock.tick(60)

game = Game()
game.run_game()
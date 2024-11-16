import pygame
import sys
from bird import Bird
from settings import Settings
from plant import Plant

class Game:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.score = 0
        self.clock = pygame.time.Clock()
        background_image = pygame.image.load("assets/background/grid_bg.png")

        # Resize the background image to fit the screen
        self.background_image = pygame.transform.scale(background_image, (self.settings.screen_width, self.settings.screen_height))

        # Set the screen height and caption.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Bird/Plant Game!")
        self.bird = Bird(self)
        self.plant = Plant(self)
        
        pygame.mixer.music.load("assets/sounds/background.ogg")  # Replace with your music file path
        pygame.mixer.music.set_volume(0.5)               # Set volume (0.0 to 1.0)
        pygame.mixer.music.play(-1)                      # -1 loops the music indefinitely

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.bird.update(self)
            
            self._update_screen()
            self.clock.tick(60)
            

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""

        if event.key == pygame.K_RIGHT:
            self.bird.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.bird.moving_left = True
        elif event.key == pygame.K_UP:
            self.bird.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.bird.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()  
            pygame.k_          

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        keys = pygame.key.get_pressed()
        if event.key == pygame.K_RIGHT:
            self.bird.moving_right = False  
        elif event.key == pygame.K_LEFT:
            self.bird.moving_left = False
        elif event.key == pygame.K_UP:
            self.bird.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.bird.moving_down = False
    def update_score(self,score_to_be_added):
        # if self.score <=1: pass
        if  self.bird.explosion: return
        self.score +=score_to_be_added
        self.settings.bird_speed +=score_to_be_added
        self.plant.size+= score_to_be_added*5
        self.plant.y -=score_to_be_added*5
        self.plant.rect.y = self.plant.y 
        self.bird.explosion = True
        self.plant.explosion= True
    def draw_score(self):
        # Set up the font
        font = pygame.font.Font(None, 36)  # None uses the default font, 36 is the font size

        # Text to display
        text = f"score = {self.score}"
        text_color = (255, 255, 255)  # White color

        text_surface = font.render(text, True, text_color)

        # Blit the text to the screen at the top-left corner
        self.screen.blit(text_surface, (10, 10))  # Position (10, 10)

        
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.background_image, (0, 0))

        self.bird.blitme()
        self.plant.blitme()
        self.bird.check_collision(self.plant,self)
        self.draw_score()
        pygame.display.flip()

    
if __name__ == "__main__":
    # Make a game instance, and run the game.
    game = Game()
    game.run_game()

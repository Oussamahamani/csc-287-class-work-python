import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game,image='./images/ship.bmp'):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(35,35))

        self.rect = self.image.get_rect()
        print(self.screen_rect)
        
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self,x,y):
        """Draw the ship at its current location."""
        if x:
            self.rect.x= x
            self.rect.y= y
        
        self.screen.blit(self.image, self.rect)

import pygame
from pygame.sprite import Sprite


class Plant(Sprite):
    """A class to manage the plant."""

    def __init__(self, game):
        """Initialize the plant and set its starting position."""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        # Load the ship image and get its rect.
        self.image = pygame.image.load('assets/plant/plant_0.png')
        self.size = 60
        self.image = pygame.transform.scale(self.image,(self.size,self.size))

        self.frame_images  =[ ]
        for x in range(36):
            self.frame_images.append(pygame.image.load(f'assets/plant/plant_{x}.png'))
        self.current_frame = 0
        self.frame_rate = 5  # How fast the frames switch (lower is faster)
        self.frame_count = 0        
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        # self.rect.midbottom = self.screen_rect

        # Store a float for the ship's exact horizontal position.
        self.current_frame = 0
        self.frame_rate = 2 # How fast the frames switch (lower is faster)
        self.frame_count = 0

        # self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(game.settings.screen_width/2)
        self.y = float(game.settings.screen_height-100)
        self.rect.x = self.x
        self.rect.y = self.y 
        self.explosion = False
        

    def blitme(self):
        if self.explosion:
            self.frame_count += 1
            if self.frame_count >= self.frame_rate:
                self.frame_count = 0
                self.current_frame = (self.current_frame + 1) % len(self.frame_images)
            self.image = self.frame_images[self.current_frame]
            self.image = pygame.transform.scale(self.image,(self.size,self.size))

        # self.rect = image.get_rect()
        
       
        """Draw the plant at its current location."""
      

        self.screen.blit(self.image, self.rect)

import pygame
from pygame.sprite import Sprite
import random


class Bird(Sprite):
    """A class to manage the bird."""

    def __init__(self, game):
        """Initialize the bird and set its starting position."""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.frame_images  =[pygame.image.load('assets/bird/bird_0.png'),pygame.image.load('assets/bird/bird_1.png')]
        self.explosion_frame_images = []
        for x in range(16):
             self.explosion_frame_images.append(pygame.image.load(f'assets/explosion/explosion_{x}.gif'))

        self.current_frame = 0
        self.frame_rate = 5  # How fast the frames switch (lower is faster)
        self.frame_count = 0

        self.explosion_frame_count = 0
        self.explosion_current_frame=0
        # Load the ship image and get its rect.
        self.image = pygame.image.load('assets/bird/bird_0.png')
        self.image = pygame.transform.scale(self.image,(60,60))

        
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        # self.rect.midbottom = self.screen_rect

        # Store a float for the ship's exact horizontal position.
        self.x = float(200)
        self.y = float(100)

        # Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.direction = "right"
        self.explosion = False
        pass

    def update(self,game):
        """Update the bird's position based on movement flags."""

        if self.explosion_current_frame == len(self.explosion_frame_images) -1:
            self.x= float(200)
            self.y = float(100)  
            self.rect.x = self.x
            self.rect.y = self.y 
            self.explosion= False
            self.explosion_current_frame= 0
            game.plant.explosion = False
            game.plant.current_frame = 0
            return
        
        if self.explosion:
            self.explosion_frame_count += 1
            if self.explosion_frame_count >= 5:
                self.explosion_frame_count = 0
                self.explosion_current_frame = (self.explosion_current_frame + 1) % len(self.explosion_frame_images) 
            self.image = self.explosion_frame_images[self.explosion_current_frame]
            return

        
   

        
        # logic for hitting the wall:
        if self.rect.right >= self.screen_rect.right or self.rect.left < 0:
            self.x= float(random.uniform(1, game.settings.screen_width-100))
            self.y = float(100)  
            self.rect.x = self.x
            self.rect.y = self.y 
            game.update_score(-1)
            return
        
         
        # Update the ship's x value, not the rect.
        if self.moving_right and self.direction != "right" :
                self.direction = "right"

        if self.moving_left and self.direction != "left":
                self.direction = "left"

            
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.bird_speed
        if self.moving_down and self.rect.bottom< self.screen_rect.bottom:
            self.y += self.settings.bird_speed
        


        if(self.direction == "right"):
            self.x += self.settings.bird_speed/2
        else:
            self.x -= self.settings.bird_speed/2
        

        self.frame_count += 1
        if self.frame_count >= self.frame_rate:
            self.frame_count = 0
            self.current_frame = (self.current_frame + 1) % len(self.frame_images)
        self.image = self.frame_images[self.current_frame]
        self.image = pygame.transform.scale(self.image,(60,60))
        if self.direction == "left":
            flipped_image = pygame.transform.flip(self.image, True, False)
            self.image =flipped_image

       
        self.rect.x = self.x
        self.rect.y = self.y

    def check_collision(self,plant,game):
        collide = pygame.Rect.colliderect(self.rect, plant.rect)
        if collide:
            explosion_sound = pygame.mixer.Sound("assets/sounds/explosion.flac")  # Load an explosion sound effect
            explosion_sound.set_volume(0.7)
            explosion_sound.play()
            game.update_score(1)

    def blitme(self):
        """Draw the bird at its current location."""
        self.screen.blit(self.image, self.rect)

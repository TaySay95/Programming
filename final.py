# Taylor Sayson
# 13 May 2024

import random
import pygame as pg
import time

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
ORANGE = (255, 127, 80)

WIDTH = 1280
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)

RIMIMAGE = pg.image.load("./Images/rim.png")
RIM = pg.transform.scale(RIMIMAGE, (RIMIMAGE.get_width() // 8, RIMIMAGE.get_height() // 8))

class Rim(pg.sprite.Sprite):
    def __init__(self, x, rim:pg.sprite.Group = None):
        super().__init__()

        self.image = RIM
        self.rect = self.image.get_rect()
        self.rim_sprites = rim
        # Spawn in a random location
        self.rect.centerx = x
        self.rect.y = 190

class Ball(pg.sprite.Sprite):
    def __init__(self, players:pg.sprite.Group = None):
        super().__init__()

        self.image = pg.Surface((50,50))
        self.image.set_colorkey(BLACK)
        pg.draw.circle(self.image, ORANGE, (25,25), 25)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.vel_x = 8
        self.vel_y = 0


        self.player_sprites = players
        self.hold = None
        self.dribble = False
        self.vertical_direction = 1
        self.shotframes = 0
        self.startshot= None
        self.endshot = None

        self.shot_start = 0

        self.shot_cooldown = 1000

    def update(self):
        """ Move ball """
        collided = pg.sprite.spritecollide(self, self.player_sprites, False)

        if collided: # and pg.time.get_ticks() - self.shot_start > self.shot_cooldown:
            self.hold = collided[0]

        if self.hold:
            if self.hold.rect.bottom == HEIGHT:
                if self.hold.vel_x>0:
                    self.rect.left = self.hold.rect.right -15
                elif self.hold.vel_x < 0:
                    self.rect.right = self.hold.rect.left +15
                elif self.hold.vel_x ==0:
                    if self.hold.initial == 100:
                        self.rect.left = self.hold.rect.right -15
                    if self.hold.initial == 1180:
                        self.rect.right = self.hold.rect.left +15
                if self.rect.y <= 630:
                    self.vertical_direction = 1
                elif self.rect.y >= 670:
                    self.vertical_direction = -1
                self.rect.y += 4 * self.vertical_direction
               
            pressed = pg.key.get_pressed()
            if self.hold.rect.bottom < HEIGHT and pressed[self.hold.input["up"]]:
                
                if self.shotframes == 0:
                    self.shotframes = 30
                    self.endshot = self.hold.rect.top + 23
                    self.startshot = self.hold.rect.top +65

                if self.shotframes > 0:
                    changey = (self.endshot - self.startshot)/self.shotframes
                    self.rect.bottom += changey
                    self.shotframes -= 1
                
                self.rect.bottom = self.hold.rect.top + 23
                
                if self.hold.initial == 100:
                    self.rect.left = self.hold.rect.right -35
                if self.hold.initial == 1180:
                    self.rect.right = self.hold.rect.left +35
            else:
                self.shot_start = pg.time.get_ticks()

                self.shotframes =0
                if self.hold.initial == 100:
                    self.hold = None
                    self.vel_x = 10
                    self.vel_y =-15
                elif self.hold.initial == 1180:
                    self.hold = None
                    self.vel_x = -10
                    self.vel_y = -15
    
        else:
            if self.rect.top < 0:
                self.rect.top = 0 
                self.vel_y *= -1
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
                self.vel_y *= -1
            if self.rect.left < 0:
                self.rect.left = 0
                self.vel_x *= -1
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
                self.vel_x *= -1
                

            if self.vel_y >=0:
                self.vel_y = self.vel_y + .5
            if self.vel_y <0:
                self.vel_y = self.vel_y + .65
            if -0.5<self.vel_y<0.5 and self.rect.bottom == HEIGHT:
                self.vel_y *=0
 
            if self.vel_x >1:
                self.vel_x = max(self.vel_x - .017, 0)
            elif self.vel_x <1:
                self.vel_x = min(self.vel_x + .017, 0)
            elif self.vel_x > 0:
                self.vel_x = max(self.vel_x - .005, 0)
            elif self.vel_x < 0:
                self.vel_x = min(self.vel_x + .005, 0)

            self.rect.x += self.vel_x
            self.rect.y += self.vel_y



class Player(pg.sprite.Sprite):
    def __init__(self, color, input, x, y):
        super().__init__()


        self.image = pg.Surface((90, 90))
        self.image.set_colorkey(BLACK)
        pg.draw.circle(self.image, color, (45, 45), 45)

        self.rect = self.image.get_rect()
        self.initial = x
        self.rect.centerx = x
        self.rect.centery = y
        self.vel_x = 0
        self.vel_y = 10
        self.acceleration = 0.8
        self.deceleration = 0.9
        self.slowaccel = 4

        self.input = input

    def update(self):
        """ Move the player. """
        pressed = pg.key.get_pressed()
        
        # Handle horizontal movement
        if pressed[self.input["left"]] and self.vel_y==0:
            self.vel_x = max(self.vel_x - self.acceleration, -8)
        elif pressed[self.input["right"]]and self.vel_y==0:
            self.vel_x = min(self.vel_x + self.acceleration, 8)
        elif pressed[self.input["left"]]:
            self.vel_x = max(self.vel_x - self.slowaccel, -3)
        elif pressed[self.input["right"]]:
            self.vel_x = min(self.vel_x + self.slowaccel, 3)
        else:
            if self.vel_x >1:
                self.vel_x = max(self.vel_x - self.deceleration, 0)
            elif self.vel_x <1:
                self.vel_x = min(self.vel_x + self.deceleration, 0)

        # Handle vertical movement
        if pressed[self.input["up"]] and self.rect.bottom > 570 and self.vel_y<=0:
            self.vel_y = -16
        else:
            self.vel_y = self.vel_y + .7
             
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        # Keep player within screen bounds
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.vel_x = 0
        if self.rect.left < 0:
            self.rect.left = 0
            self.vel_x = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.vel_y = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.vel_y = 0

def start():
    """Environment Setup and Game Loop"""
    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group

    all_sprites = pg.sprite.Group()
    player_sprites = pg.sprite.Group()
    rim_sprites = pg.sprite.Group()
    # Create the Player sprite object

    player = Player(BLUE, {'left': pg.K_LEFT, 'right': pg.K_RIGHT, 'up': pg.K_UP, 'down': pg.K_DOWN}, 1180, 720,)
    player2 = Player(RED, {'left': pg.K_a, 'right': pg.K_d, 'up': pg.K_w, 'down': pg.K_s}, 100, 720,)
    player_sprites.add(player)
    player_sprites.add(player2)
    
    rim1 = Rim(80, rim_sprites)
    rim2 = Rim(1200, rim_sprites)
    ball = Ball(player_sprites)
    all_sprites.add(player)
    all_sprites.add(player2)
    all_sprites.add(ball)
    all_sprites.add(rim1)
    all_sprites.add(rim2)
    pg.display.set_caption("GAME")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        all_sprites.update()

        # --- Draw items
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps

    pg.quit()

def main():
    start()

if __name__ == "__main__":
    main()
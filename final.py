#Taylor Sayson
# 13 May 2024

# pygame-example-shmup.py
# Shoot 'em Up

import random
import pygame as pg

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

class Ball(pg.sprite.Sprite):
    def __init__(self, players:pg.sprite.Group = None):
        super().__init__()

        self.image = pg.Surface((50,50))
        self.image.set_colorkey(BLACK)
        pg.draw.circle(self.image, ORANGE, (25,25), 25)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.vel_x = 0
        self.vel_y = 10
        self.deceleration = 1
        self.slowdecel = .01

        self.player_sprites = players

    def update(self):
        """ Move puck based on contact """
        # collisions = pg.sprite.spritecollide(self, self.player_sprites, False)
        # for x in collisions:
        #     if isinstance(x, Player):
        #         # Increase puck velocity to 15
        #         self.vel_x = 15
        #         self.vel_y = 15

        # Decleration
        # if self.rect.right > WIDTH:
        #     self.rect.right = WIDTH
        #     self.vel_x = self.vel_x * -1
        # if self.rect.left < 0:
        #     self.rect.left = 0
        #     self.vel_x = self.vel_x * -1
        if self.rect.y< HEIGHT:
            self.vel_y = self.vel_y + 2
        
        if self.rect.bottom == 720:
            self.vel_y = self.vel_y * -1
        if self.rect.y < 720 and self.vel_y < 0:
            self.vel_y =self.vel_y *-1 


        self.rect.x += self.vel_x
        self.rect.y += self.vel_y



        # if self.vel_x >0:
        #     self.vel_x = self.vel_x - self.deceleration
        # elif self.vel_x <0:
        #     self.vel_x = self.vel_x + self.deceleration

        # if self.vel_y >= 0:
        #         self.vel_y = self.vel_y - self.deceleration
        # if self.vel_y < 0:
        #     self.vel_y = self.vel_y + .5


class Player(pg.sprite.Sprite):
    def __init__(self, color, input, x,y):
        super().__init__()


        self.image = pg.Surface((90, 90))
        self.image.set_colorkey(BLACK)
        pg.draw.circle(self.image, color, (45, 45), 45)

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        # Initialize velocity
        self.vel_x = 0
        self.vel_y = 10
        self.acceleration = 0.5
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
        # elif pressed[self.input["down"]]:
        #     self.vel_y = min(self.vel_y + self.acceleration, 6)
                
                
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
    # Create the Player sprite object

    player = Player(BLUE, {
        'left': pg.K_LEFT, 'right': pg.K_RIGHT, 'up': pg.K_UP, 'down': pg.K_DOWN}, 1180, 720)
    player2 = Player(RED, {
        'left': pg.K_a, 'right': pg.K_d, 'up': pg.K_w, 'down': pg.K_s}, 100, 720)

    player_sprites.add(player)
    player_sprites.add(player2)

    ball = Ball(player_sprites)


    all_sprites.add(player)
    all_sprites.add(player2)
    all_sprites.add(ball)

    pg.display.set_caption("GAME")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        all_sprites.update()

        # --- Draw items
        screen.fill(WHITE)

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
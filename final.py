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

WIDTH = 1000
HEIGHT = 1200
SCREEN_SIZE = (WIDTH, HEIGHT)



class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/galaga_ship.png")
        self.image = pg.transform.scale(
            self.image, (self.image.get_width() // 2, self.image.get_height() // 2)
        )

        self.rect = self.image.get_rect()
        # Initialize velocity
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        """ Move the player. """

        # Move left/right
        self.rect.x += self.vel_x

        # Move up/down
        self.rect.y += self.vel_y

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left designated button. """
        self.vel_x = -6

    def go_right(self):
        """ Called when the user hits the right designated button. """
        self.vel_x = 6

    def go_up(self):
        """ Called when the user hits the right designated button. """
        self.vel_y = -6

    def go_down(self):
        """ Called when the user hits the right designated button. """
        self.vel_y = 6

    def stop_leftright(self):
        """ Called when the user lets off the keyboard. """
        self.vel_x = 0
    def stop_updown(self):
        """ Called when the user lets off the keyboard. """
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
    # Create the Player sprite object
    player = Player()

    all_sprites.add(player)


    pg.display.set_caption("Shoot 'Em Up")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    player.go_right()
                if event.key == pg.K_LEFT:
                    player.go_left()
                if event.key == pg.K_UP:
                    player.go_up()
                if event.key == pg.K_DOWN:
                    player.go_down()
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT and player.vel_x < 0:
                    player.stop_leftright()
                if event.key == pg.K_RIGHT and player.vel_x > 0:
                    player.stop_leftright()
                if event.key == pg.K_UP and player.vel_y < 0:
                    player.stop_updown()
                if event.key == pg.K_DOWN and player.vel_y > 0:
                    player.stop_updown()
        # --- Update the world state
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
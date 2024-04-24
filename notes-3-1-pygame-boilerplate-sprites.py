# Intro to Pygame
# Taylor Sayson
# 23 April 2024

# Boilerplates
# Sprite Class


import pygame
import random


def update(self):
        #Update  position of Dvdlogo
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    # Keep the Dvdlogo in the screen
    # Right side of the screen
    #     - if the right edge of dvdlogo > WIDTH
    #          - switch the direction (+vel-x -> -vel-x)
        if self.rect.right >= 1280:
            self.vel_x = -self.vel_x
        if self.rect.left <= 0:
            self.vel_x = -self.vel_x
        if self.rect.top <=0:
            self.vel_y = -self.vel_y
        if self.rect.bottom >=720:
            self.vel_y = -self.vel_y

        print(self.rect.x, self.rect.y)




class Kanye(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Images/Kanye-West-PNG.png")
        self.rect = self.image.get_rect() 

        self.image = pygame.transform.scale(self.image, (self.rect.width // 2, self.rect.height // 2))

        self.rect.centerx = random.randrange(250,970)
        self.rect.centery = random.randrange(250,470)

        self.vel_x = random.randrange(-8, 8)
        self.vel_y = random.randrange(-8, 8)

    def update(self):
                self.rect.x += self.vel_x
                self.rect.y += self.vel_y

                if self.rect.right >= 1280:
                    self.vel_x = -self.vel_x
                if self.rect.left <= 0:
                    self.vel_x = -self.vel_x
                if self.rect.top <=0:
                    self.vel_y = -self.vel_y
                if self.rect.bottom >=720:
                    self.vel_y = -self.vel_y

                print(self.rect.x, self.rect.y)


class Rb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Images/rb.webp")
        self.rect = self.image.get_rect() 

        self.image = pygame.transform.scale(self.image, (self.rect.width // 2, self.rect.height // 2))

        self.rect.centerx = random.randrange(200,1020)
        self.rect.centery = random.randrange(200,520)

        self.vel_x = random.randrange(-8, 8)
        self.vel_y = random.randrange(-8, 8)

    def update(self):
                self.rect.x += self.vel_x
                self.rect.y += self.vel_y

                if self.rect.right >= 1280:
                    self.vel_x = -self.vel_x
                if self.rect.left <= 0:
                    self.vel_x = -self.vel_x
                if self.rect.top <=0:
                    self.vel_y = -self.vel_y
                if self.rect.bottom >=720:
                    self.vel_y = -self.vel_y

                print(self.rect.x, self.rect.y)

class Mercedes(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Images/mercedes.png")
        self.rect = self.image.get_rect() 

        self.image = pygame.transform.scale(self.image, (self.rect.width // 2, self.rect.height // 2))

        self.rect.centerx = random.randrange(200,1020)
        self.rect.centery = random.randrange(200,520)

        self.vel_x = 1
        self.vel_y = 1

    def update(self):
                self.rect.x += self.vel_x
                self.rect.y += self.vel_y

                if self.rect.right >= 1280:
                    self.vel_x = -self.vel_x
                if self.rect.left <= 0:
                    self.vel_x = -self.vel_x
                if self.rect.top <=0:
                    self.vel_y = -self.vel_y
                if self.rect.bottom >=720:
                    self.vel_y = -self.vel_y

                print(self.rect.x, self.rect.y)


class Dvdlogo(pygame.sprite.Sprite):
    """Represents the DVD Logo"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Images/dvd-logo.png")

        # Sets the x and y to 0
        #   First position of the image is in the top right
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randrange(150,1130)
        self.rect.centery = random.randrange(150,570)

        # How much position changes over time
        # - pixels per tick

        self.vel_x = random.randrange(-8, 8)
        self.vel_y = random.randrange(-8, 8)


    def update(self):
            #Update  position of Dvdlogo
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y

        # Keep the Dvdlogo in the screen
        # Right side of the screen
        #     - if the right edge of dvdlogo > WIDTH
        #          - switch the direction (+vel-x -> -vel-x)
            if self.rect.right >= 1280:
                self.vel_x = -self.vel_x
            if self.rect.left <= 0:
                self.vel_x = -self.vel_x
            if self.rect.top <=0:
                self.vel_y = -self.vel_y
            if self.rect.bottom >=720:
                self.vel_y = -self.vel_y

            print(self.rect.x, self.rect.y)
    
def start():
    """Environment Setup and Game Loop"""

    pygame.init()

    # --CONSTANTS--
    # COLOURS
    WHITE   = (255, 255, 255)
    BLACK   = (  0,   0,   0)
    EMERALD = ( 21, 219, 147)
    RED     = (255,   0,   0)
    GREEN   = (  0, 255,   0)
    BLUE    = (  0,   0, 255)
    GRAY    = (128, 128, 128)
    PURPLE  = (128,   0, 128)

    WIDTH   = 1280    # Pixels
    HEIGHT  =  720
    SCREEN_SIZE = (WIDTH, HEIGHT)

    # --VARIABLES--
    screen = pygame.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pygame.time.Clock()

    dvdlogo = Dvdlogo()
    kanye = Kanye()
    rb = Rb()
    mercedes = Mercedes()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(dvdlogo)
    all_sprites.add(kanye)
    all_sprites.add(rb)
    all_sprites.add(mercedes)
    pygame.display.set_caption("DVD Screen Saver")

    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

		# --- Update the world state
        all_sprites.update()

        # --- Draw items
        screen.fill(PURPLE)

        all_sprites.draw(screen)

        
      
        # Update the screen with anything new
        pygame.display.flip()

        # --- Tick the Clock
        clock.tick(60)    # 60 fps


def main():
    start()

if __name__ == "__main__":
    main()
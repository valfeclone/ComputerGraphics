import os
import pygame
from pygame.locals import *
import pyganim
import math as mt

# pygame.init()

width, height = 800, 600
# screen = pygame.display.set_mode((width, height))

current_path = os.path.dirname("C:\\Users\DREAMOCHEL\\Desktop\\Py\\") # Where your .py file is located
resource_path = os.path.join(current_path, 'resources') # The resource folder path
image_path = os.path.join(resource_path, 'images') # The image folder path

player_image = pygame.image.load(os.path.join(image_path, 'parkiran.jpg'))

class owlImgs(pygame.sprite.Sprite):
    def __init__(self):
        super(owlImgs, self).__init__()
        #memuat sprite
        self.images = []
        self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'set1.png')), (100, 100)))
        self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'set2.png')), (100, 100)))
        self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'set3.png')), (100, 100)))
        self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'set4.png')), (100, 100)))
        self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'set5.png')), (100, 100)))
        self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'set6.png')), (100, 100)))
        self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'set7.png')), (100, 100)))
        self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'set8.png')), (100, 100)))
        self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'set9.png')), (100, 100)))
        self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'set10.png')), (100, 100)))
        self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'set11.png')), (100, 100)))
        self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'set12.png')), (100, 100)))
        self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'set13.png')), (100, 100)))
        self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'set14.png')), (100, 100)))
        self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'set15.png')), (100, 100)))
        self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'set16.png')), (100, 100)))
        # self.images.append(pygame.transform.scale(pygame.image.load(os.path.join(image_path, 'tile008.png')), (100, 100)))
        #index menunjuk ke sprite yang sedang ditampilkan
        self.index = 0
        self.image = self.images[self.index]
        #membuat rect pada posisi (x, y) dengan ukuran (100, 100)
        self.x = 700
        self.y = 100
        self.rect = pygame.Rect(self.x, self.y, 100, 100)
        self.outBorder = 0
    
    def update(self):
        #berpindah ke sprite selanjutnya
        if(self.outBorder==0):
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            #membuat sprite bergerak mengikuti grafik sin
            # self.x += 10
            # self.y = 100 * mt.cos(self.x*5) + 200
            # self.rect = pygame.Rect(self.x, self.y, 100, 100)
            self.x -= 5
            self.y = 37 * mt.sin(self.x*5) + 250
            self.rect = pygame.Rect(self.x, self.y, 100, 100)
            if(self.x<0):
                self.outBorder = 1

        if(self.outBorder==1):
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            self.x += 5
            self.y = 37 * mt.sin(self.x*5) + 250
            self.rect = pygame.Rect(self.x, self.y, 100, 100)
            if(self.x > width):
                self.outBorder = 0

def main():
      #untuk menampilkan layar
    pygame.init()
    wndow = (width, height)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,20) #untuk menentukan posisi layar
    screen = pygame.display.set_mode(wndow)
    bird_sprite = owlImgs()
    sprite_group = pygame.sprite.Group(bird_sprite)
    pygame.display.set_caption('Fadhlan Pasyah A F - 18536')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        sprite_group.update()
        screen.blit(player_image, [0, 0])
        sprite_group.draw(screen)
        pygame.display.update()
        pygame.time.wait(65)

main()
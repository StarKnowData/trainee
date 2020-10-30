#-*- coding:utf-8 -*-
import pygame
from random import *

class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy0.png")
        self.destroy_images = []
        self.destroy_images.extend([pygame.image.load("images/enemy0_down1.png"), \
                                    pygame.image.load("images/enemy0_down2.png"), \
                                    pygame.image.load("images/enemy0_down3.png"), \
                                    pygame.image.load("images/enemy0_down4.png"), \
                                    ])
        self.rect = self.image.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        self.speed = 2
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left,self.rect.top = randint(0,self.width-self.rect.width),\
                                        randint(-5*self.height,0)
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(-5 * self.height, 0)

class MidEnemy(pygame.sprite.Sprite):
    energy = 8
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy1.png")
        self.image_hit = pygame.image.load("images/enemy1_hit.png")
        self.destroy_images = []
        self.destroy_images.extend([pygame.image.load("images/enemy1_down1.png"), \
                                    pygame.image.load("images/enemy1_down2.png"), \
                                    pygame.image.load("images/enemy1_down3.png"), \
                                    pygame.image.load("images/enemy1_down4.png"), \
                                    ])
        self.rect = self.image.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        self.rect.left,self.rect.top = randint(0,self.width-self.rect.width),\
                                        randint(-10*self.height,-self.height)
        self.speed = 1
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = MidEnemy.energy
        self.hit = False
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = MidEnemy.energy
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(-10 * self.height,-self.height)

class BigEnemy(pygame.sprite.Sprite):
    energy = 20
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("images/enemy2.png")
        self.image2 = pygame.image.load("images/enemy2_n2.png")
        self.image_hit = pygame.image.load("images/enemy2_hit.png")
        self.destroy_images = []
        self.destroy_images.extend([pygame.image.load("images/enemy2_down1.png"), \
                                    pygame.image.load("images/enemy2_down2.png"), \
                                    pygame.image.load("images/enemy2_down3.png"), \
                                    pygame.image.load("images/enemy2_down4.png"), \
                                    pygame.image.load("images/enemy2_down5.png"), \
                                    pygame.image.load("images/enemy2_down6.png"), \
                                    ])
        self.rect = self.image1.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        self.speed = 1
        self.active = True
        self.mask = pygame.mask.from_surface(self.image1)
        self.energy = BigEnemy.energy
        self.hit = False
        self.rect.left,self.rect.top = randint(0,self.width-self.rect.width),\
                                        randint(-15*self.height,-5*self.height)
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = BigEnemy.energy
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(-15 * self.height, -5*self.height)

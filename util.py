from pygame import *


class Ball(sprite.Sprite):
    def __init__(self,img="a.png",speed=0):
        super().__init__()
        self.image=image.load(img)
        self.rect=self.image.get_rect()
        self.speed=speed
        self.bullentlist=[]



    def move(self,speed):
        self.speed=speed
        self.rect=self.rect.move(self.speed)

    def shoot():
        pass

class Bullent(sprite.Sprite):
    def __init__(self,img="b.png",speed=(0,0)):
        super().__init__()
        self.image=image.load(img)
        self.rect=self.image.get_rect()
        self.speed=speed
    def move(self,speed):
        self.speed=speed
        self.rect=self.rect.move(self.speed)
    def go(self):
        self.rect=self.rect.move(self.speed)


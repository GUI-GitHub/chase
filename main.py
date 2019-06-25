from pygame import *
from util import *

init()
screen=display.set_mode([10*48+1,10*48+1],0,32)
display.set_caption("chase")
screen.fill((255,255,255))

ball=Ball()



if __name__=="__main__":
    ball.rect.move_ip(240,240)
    speed=[0,0]
    while 1:
        for i in event.get():
            if i.type==QUIT:
                exit()
            
            if i.type==MOUSEMOTION:
                print(ball.rect)
                speed=[(i.pos[0]-ball.rect.x)/10,(i.pos[1]-ball.rect.y)/10]
            if i.type==MOUSEBUTTONDOWN:
                pass
            ball.move(speed)

        
        screen.fill((255,255,255))
        sprite.Group(ball).draw(screen)

        display.update()






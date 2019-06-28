from pygame import *
from util import *

init()
screen=display.set_mode([10*48+1,10*48+1],0,32)
display.set_caption("chase")
screen.fill((255,255,255))

ball=Ball()


bu=Bullent()


if __name__=="__main__":
    ball.rect.move_ip(240,240)
    bu.rect.move_ip(240,240)
    speed=[0,0]
    spb=[0,0]
    bs=[]

    g=sprite.Group()

    while 1:
        for i in event.get():
            if i.type==QUIT:
                exit()
            if i.type==MOUSEMOTION:
                #print(ball.rect)
                speed=[(i.pos[0]-ball.rect.x)/10,(i.pos[1]-ball.rect.y)/10]
            if i.type==MOUSEBUTTONDOWN:
                spb=[(i.pos[0]-ball.rect.x)/10,(i.pos[1]-ball.rect.y)/10]
                bu.speed=spb
            ball.move(speed)
            
            bu.go()
            

        g.add(ball)
        g.add(bu)

        if not((0<bu.rect[0])and(bu.rect[0]<480)and(0<bu.rect[1])and(bu.rect[1]<480)):
            g.remove(bu)
            print("bu kill")
        screen.fill((255,255,255))
        
        g.draw(screen)

        display.update()






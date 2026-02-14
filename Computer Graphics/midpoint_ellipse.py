import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((800,800))
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

def midpoint_ellipse(xc,yc,rx,ry):
    x=0
    y=ry
    ry2=ry*ry
    rx2=rx*rx
    p1=ry2-rx2*y+0.25*rx2
    while(2*ry2*x<=2*rx2*y):
        screen.set_at((xc+x,yc+y),WHITE)
        screen.set_at((xc+x,yc-y),WHITE)
        screen.set_at((xc-x,yc+y),WHITE)
        screen.set_at((xc-x,yc-y),WHITE)
        if p1<0:
            x=x+1
            p1=p1+2*ry2*x+ry2
        else:
            x=x+1
            y=y-1
            p1=p1+2*ry2*x-2*rx2*y+ry2
    p2=ry2*(x+0.5)**2+rx2*(y-1)**2-rx2*ry2
    while(y>=0):
        screen.set_at((xc+x,yc+y),WHITE)
        screen.set_at((xc+x,yc-y),WHITE)
        screen.set_at((xc-x,yc+y),WHITE)
        screen.set_at((xc-x,yc-y),WHITE)
        if p2>0:
            y=y-1
            p2=p2-2*rx2*y+rx2
        else:
            x=x+1
            y=y-1
            p2=p2+2*ry2*x-2*rx2*y+rx2
    

            
def main():
     while True:
         for event in pygame.event.get():
             if event.type==pygame.QUIT:
                 pygame.quit()
                 sys.exit()
                 
         screen.fill(BLACK)
         midpoint_ellipse(400,400,150,100)
         pygame.display.flip()

if __name__=="__main__":
    main()
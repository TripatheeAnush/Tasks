import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((800,800))
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

def midpoint_circle(xc,yc,r):
    x=0
    y=r
    p=1-r
    while(x<=y):
        screen.set_at((xc+x,yc+y),WHITE)
        screen.set_at((xc+x,yc-y),WHITE)
        screen.set_at((xc-x,yc+y),WHITE)
        screen.set_at((xc-x,yc-y),WHITE)
        screen.set_at((xc+y,yc+x),WHITE)
        screen.set_at((xc-y,yc+x),WHITE)
        screen.set_at((xc+y,yc-x),WHITE)
        screen.set_at((xc-y,yc-x),WHITE)
        x=x+1
        if p<0:
            p=p+2*x+1
        else:
            y=y-1
            p=p+2*x-2*y+1
    

            
def main():
     while True:
         for event in pygame.event.get():
             if event.type==pygame.QUIT:
                 pygame.quit()
                 sys.exit()
                 
         screen.fill(BLACK)
         midpoint_circle(400,400,300)
         pygame.display.flip()

if __name__=="__main__":
    main()
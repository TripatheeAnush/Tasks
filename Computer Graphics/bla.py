import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((600,600))
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

def bla(x1,y1,x2,y2):
    dx=abs(x2-x1)
    dy=(y2-y1)
    lx=1 if x2>x1 else -1
    ly=1 if y2>y1 else -1
    x=x1
    y=y1
    screen.set_at((round(x),round(y)),RED)
    
    if dx>dy:
        p=2*dy-dx
        for _ in range(dx):
            if p<0:
                x=x+lx
                p=p+2*dy
            else:
                x=x+lx
                y=y+ly
                p=p+2*dy-2*dx
            screen.set_at((round(x),round(y)),RED)

    else:
        p=2*dx-dy
        for _ in range(dy):
            if p<0:
                y=y+ly
                p=p+2*dx
            else:
                x=x+lx
                y=y+ly
                p=p+2*dx-2*dy
            screen.set_at((round(x),round(y)),RED)


            
def main():
     while True:
         for event in pygame.event.get():
             if event.type==pygame.QUIT:
                 pygame.quit()
                 sys.exit()
                 
         screen.fill(BLACK)
         bla(100,100,300,300)
         pygame.display.flip()

if __name__=="__main__":
    main()
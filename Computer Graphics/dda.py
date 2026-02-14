import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((600,600))
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

def dda(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    if dx>dy:
        step=abs(dx)
    else:
        step=abs(dy)
    x_inc=dx/step
    y_inc=dy/step
    x=x1
    y=y1
    screen.set_at((round(x),round(y)),GREEN)
    for _ in range(step):
        x=x+x_inc
        y=y+y_inc
        screen.set_at((round(x),round(y)),GREEN)
def main():
     while True:
         for event in pygame.event.get():
             if event.type==pygame.QUIT:
                 pygame.quit()
                 sys.exit()
                 
         screen.fill(BLACK)
         dda(100,100,300,300)
         pygame.display.flip()

if __name__=="__main__":
    main()
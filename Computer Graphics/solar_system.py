import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0,0,0)
WHITE = (255,255,255)
SUN = (255,200,0)
MERCURY = (180,180,180)
VENUS = (220,180,120)
EARTH = (80,120,255)
MARS = (255,80,80)
JUPITER = (200,160,120)
SATURN = (210,190,140)
URANUS = (120,220,220)
NEPTUNE = (100,120,255)
def midpoint_ellipse(xc,yc,rx,ry):
    x=0
    y=ry
    rx2=rx*rx
    ry2=ry*ry
    p1=ry2-rx2*ry+0.25*rx2
    while 2*ry2*x<=2*rx2*y:
        screen.set_at((xc+x,yc+y),WHITE)
        screen.set_at((xc-x,yc+y),WHITE)
        screen.set_at((xc+x,yc-y),WHITE)
        screen.set_at((xc-x,yc-y),WHITE)
        if p1<0:
            x+=1
            p1+=2*ry2*x+ry2
        else:
            x+=1
            y-=1
            p1+=2*ry2*x-2*rx2*y+ry2
    p2=ry2*(x+0.5)**2+rx2*(y-1)**2-rx2*ry2
    while y>=0:
        screen.set_at((xc+x,yc+y),WHITE)
        screen.set_at((xc-x,yc+y),WHITE)
        screen.set_at((xc+x,yc-y),WHITE)
        screen.set_at((xc-x,yc-y),WHITE)
        if p2>0:
            y-=1
            p2+=rx2-2*rx2*y
        else:
            x+=1
            y-=1
            p2+=2*ry2*x-2*rx2*y+rx2
def midpoint_circle(xc,yc,r,color=WHITE):
    x=0
    y=r
    d=1-r
    while x<=y:
        for i in range(xc-x,xc+x+1):
            screen.set_at((i,yc+y),color)
            screen.set_at((i,yc-y),color)
        for i in range(xc-y,xc+y+1):
            screen.set_at((i,yc+x),color)
            screen.set_at((i,yc-x),color)
        if d<0:
            d+=2*x+1
        else:
            d+=2*(x-y)+1
            y-=1
        x+=1
def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        midpoint_circle(500,500,25,SUN)
        midpoint_ellipse(500,500,80,30)
        midpoint_ellipse(500,500,130,90)
        midpoint_ellipse(500,500,180,130)
        midpoint_ellipse(500,500,230,170)
        midpoint_ellipse(500,500,280,220)
        midpoint_ellipse(500,500,330,270)
        midpoint_ellipse(500,500,380,320)
        midpoint_ellipse(500,500,430,370)
        midpoint_circle(580,500,8,MERCURY)
        midpoint_circle(500,410,9,VENUS)
        midpoint_circle(315,500,10,EARTH)
        midpoint_circle(450,340,11,MARS)
        midpoint_circle(780,500,11,JUPITER)
        midpoint_circle(500,230,12,SATURN)
        midpoint_circle(580,810,12,URANUS)
        midpoint_circle(500,130,13,NEPTUNE)
        pygame.display.flip()
if __name__=="__main__":
    main()
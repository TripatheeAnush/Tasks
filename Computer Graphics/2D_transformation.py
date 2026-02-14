import pygame
import sys
import math

pygame.init()

W, H = 1000, 1000
screen = pygame.display.set_mode((W, H))

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
BLUE  = (0,0,255)
GREEN = (0,255,0)

def translate(x1,y1,x2,y2,tx,ty):
    pygame.draw.line(screen, WHITE, (x1,y1), (x2,y2), 4)
    X1 = x1 + tx
    Y1 = y1 + ty
    X2 = x2 + tx
    Y2 = y2 + ty
    pygame.draw.line(screen, RED, (X1,Y1), (X2,Y2), 4)

def scale_line(x1,y1,x2,y2,sx,sy):
    pygame.draw.line(screen, WHITE, (x1,y1), (x2,y2), 4)
    X1 = x1 * sx
    Y1 = y1 * sy
    X2 = x2 * sx
    Y2 = y2 * sy
    pygame.draw.line(screen, (0,0,255), (X1,Y1), (X2,Y2), 4)

def rotate(x1,y1,x2,y2,theta):
    angle = math.radians(theta)
    pygame.draw.line(screen, WHITE, (x1,y1), (x2,y2), 4)
    dx = x2 - x1
    dy = y2 - y1
    X2 = x1 + dx * math.cos(angle) - dy * math.sin(angle)
    Y2 = y1 + dx * math.sin(angle) + dy * math.cos(angle)
    pygame.draw.line(screen, GREEN, (x1,y1), (X2,Y2), 4)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        
        translate(100,100,250,200,50,50)
        scale_line(600,100,700,200,1.2,1.2)  
        rotate(100,600,250,700,45)

        pygame.display.flip()

if __name__=="__main__":
    main()

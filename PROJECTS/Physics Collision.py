import pygame
import math
import random
import sys

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Physics Game – Elastic Collision Demo")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 18)

#CONSTANTS
GRAVITY = 0.4
FRICTION = 0.995
BOUNCE_DAMPING = 0.9

BALL_RADIUS = 10
ORB_RADIUS = 15

PADDLE_WIDTH = 120
PADDLE_HEIGHT = 15
PADDLE_Y = HEIGHT - 40
PADDLE_SPEED = 8

MAX_LEVEL = 3
LEVEL_SCORE_THRESHOLD = 200

COL_BALL = (255, 100, 100)
COL_ORB = (0, 200, 255)
COL_ORB_HIT = (70, 70, 90)
COL_PADDLE = (220, 60, 60)
COL_UI = (240, 240, 240)
COL_PATH = (180, 180, 180)

x_position=140
y_position=120
x_hit=80
y_hit=70

#BACKGROUND THEMES
background_themes = [
    ((20, 20, 35), (40, 40, 70)),
    ((0, 50, 0), (100, 200, 100)),
    ((50, 0, 50), (200, 50, 200))
]
bg_index = 0

def draw_gradient_background(top_color, bottom_color):
    for y in range(HEIGHT):
        t = y / HEIGHT      #normalises top as 0 and bottom as 1
        #Linear Interpolation
        r = int(top_color[0] * (1 - t) + bottom_color[0] * t)
        g = int(top_color[1] * (1 - t) + bottom_color[1] * t)
        b = int(top_color[2] * (1 - t) + bottom_color[2] * t)
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

#GRAPHICS
def make_circle(radius, color):
    test = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    pygame.draw.circle(test, color, (radius, radius), radius)
    return test

ball_sprite = make_circle(BALL_RADIUS, COL_BALL)
orb_sprite = make_circle(ORB_RADIUS, COL_ORB)
orb_hit_sprite = make_circle(ORB_RADIUS, COL_ORB_HIT)

#LEVEL DATA
def create_orbs(level):
    orbs = []
    if level == 1:
        for r in range(4):
            for c in range(8):
                orbs.append([x_position + c * x_hit, y_position + r * y_hit, False])    #start_offset+index*spacing
    elif level == 2:
        for r in range(6):
            for c in range(r + 1):
                x = WIDTH // 2 - r * 35 + c * 70
                y = 100 + r * 60
                orbs.append([x, y, False])
    else:
        for _ in range(25):
            orbs.append([
                random.randint(100, WIDTH - 100),   #spawns random sprites
                random.randint(100, 400),
                False
            ])
    return orbs

#PARTICLES
particles = []

def spawn_particles(x, y):
    for _ in range(8):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 4)
        particles.append([x, y, math.cos(angle) * speed, math.sin(angle) * speed, 20])

def update_particles():
    for p in particles[:]:
        p[0] += p[2]
        p[1] += p[3]
        p[3] += 0.15
        p[4] -= 1
        pygame.draw.circle(screen, (255, 200, 80), (int(p[0]), int(p[1])), 2)
        if p[4] <= 0:
            particles.remove(p)

#TRAJECTORY 
def draw_dotted_path(x, y, vx, vy):
    tx, ty = x, y
    tvx, tvy = vx, vy
    for i in range(40):
        tvy += GRAVITY
        tvx *= FRICTION
        tx += tvx
        ty += tvy
        if i % 2 == 0:
            pygame.draw.circle(screen, COL_PATH, (int(tx), int(ty)), 2)

##COLLISION##
def handle_orb_collision(ball, orbs):
    gained = 0
    for orb in orbs:
        if orb[2]:
            continue
        dx = ball["x"] - orb[0]
        dy = ball["y"] - orb[1]
        dist = math.hypot(dx, dy)
        if dist < BALL_RADIUS + ORB_RADIUS:
            nx, ny = dx / dist, dy / dist
            dot = ball["vx"] * nx + ball["vy"] * ny
            ball["vx"] = (ball["vx"] - 2 * dot * nx) * BOUNCE_DAMPING
            ball["vy"] = (ball["vy"] - 2 * dot * ny) * BOUNCE_DAMPING
            orb[2] = True
            gained += 10
            spawn_particles(orb[0], orb[1])
    return gained


def main():
    global bg_index
    ball = {"x": WIDTH//2, "y": 60, "vx":0, "vy":0, "active":False, "shots":10}
    paddle_x = WIDTH//2 - PADDLE_WIDTH//2
    score = 0
    level = 1
    orbs = create_orbs(level)

    running = True
    while running:
        top_color, bottom_color = background_themes[bg_index]
        draw_gradient_background(top_color, bottom_color)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    bg_index = (bg_index + 1) % len(background_themes)
            if (event.type == pygame.MOUSEBUTTONDOWN and 
                not ball["active"] and ball["shots"]>0):
                angle = math.atan2(mouse_y - ball["y"], mouse_x - ball["x"])
                ball["vx"] = math.cos(angle) * 12
                ball["vy"] = math.sin(angle) * 12
                ball["active"] = True
                ball["shots"] -= 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            paddle_x -= PADDLE_SPEED
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            paddle_x += PADDLE_SPEED
        paddle_x = max(0, min(WIDTH - PADDLE_WIDTH, paddle_x))

        if ball["active"]:
            ball["vy"] += GRAVITY
            ball["vx"] *= FRICTION
            ball["x"] += ball["vx"]
            ball["y"] += ball["vy"]

            if ball["x"] < BALL_RADIUS or ball["x"] > WIDTH - BALL_RADIUS:
                ball["vx"] *= -BOUNCE_DAMPING
            if ball["y"] < BALL_RADIUS:
                ball["vy"] *= -BOUNCE_DAMPING

            if (ball["y"] + BALL_RADIUS >= PADDLE_Y and
                paddle_x < ball["x"] < paddle_x + PADDLE_WIDTH and
                ball["vy"] > 0):
                ball["vy"] *= -1.2
                offset = ball["x"] - (paddle_x + PADDLE_WIDTH/2)
                ball["vx"] += offset * 0.08

            if ball["y"] > HEIGHT + 50:
                ball["active"] = False
                ball["x"], ball["y"] = WIDTH//2, 60
                ball["vx"], ball["vy"] = 0, 0

        score += handle_orb_collision(ball, orbs)
        update_particles()

        if all(o[2] for o in orbs) or score >= level*LEVEL_SCORE_THRESHOLD:
            if level < MAX_LEVEL:
                level += 1
                orbs = create_orbs(level)
                ball["shots"] += 5
                ball["active"] = False
                ball["x"], ball["y"] = WIDTH//2, 60
            else:
                win_font = pygame.font.SysFont("consolas", 60, True)
                text = win_font.render("YOU WIN!", True, (255,215,0))
                screen.blit(text, text.get_rect(center=(WIDTH//2, HEIGHT//2)))
                pygame.display.flip()
                pygame.time.wait(3500)
                running = False

        if not ball["active"] and ball["shots"]>0:
            angle = math.atan2(mouse_y - ball["y"], mouse_x - ball["x"])
            draw_dotted_path(ball["x"], ball["y"], math.cos(angle)*12, math.sin(angle)*12)

        for orb in orbs:
            sprite = orb_hit_sprite if orb[2] else orb_sprite
            screen.blit(sprite, (orb[0]-ORB_RADIUS, orb[1]-ORB_RADIUS))

        if ball["active"] or ball["shots"]>0:
            screen.blit(ball_sprite, (ball["x"]-BALL_RADIUS, ball["y"]-BALL_RADIUS))

        pygame.draw.rect(screen, COL_PADDLE, (paddle_x, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT))

        ui = font.render(f"Score: {score}  Level: {level}  Shots: {ball['shots']}", True, COL_UI)
        screen.blit(ui, (20,20))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__=="__main__":
    main()

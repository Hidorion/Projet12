import pygame
import math
pygame.init()

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()

x, y, dx, dy = 360, 240, 0, 0
player = pygame.image.load("pygame_12_bow/miniarc.png")


bullet_x, bullet_y = 360, 240
speed = 20
bullet = pygame.image.load("pygame_12_bow/arrow.png")



def update(mouse_x, mouse_y):
    global x, y, dx, dy, bullet_x, bullet_y
    dx = mouse_x - x
    dy = mouse_y - y
    angle = math.atan2(dy, dx)
    bullet_x += speed * math.cos(angle)
    bullet_y += speed * math.sin(angle)

run_update = False
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                run_update = True
                mouse_x, mouse_y = pygame.mouse.get_pos()
    if run_update:
        update(mouse_x, mouse_y)
        if 0 > bullet_x or bullet_x > 800 or 0 > bullet_y or bullet_y > 800:
            bullet_x, bullet_y = 360, 240
            run_update = False
    screen.fill((0, 0, 0))
    screen.blit(player, (x, y))
    screen.blit(bullet, (bullet_x, bullet_y))
    pygame.display.update()
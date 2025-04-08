# moving circle on screen game
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

running = True
dt = 0
ds = 1280
ts = 0
jump = False

# circle at the center
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
# player_pos = pygame.Vector2(0,0)


def reset():
    running = True
    dt = 0
    ds = 1280
    ts = 0
    jump = False

while running:
    for event in pygame.event.get():
        # pygame.QUIT = X button on the window
        if event.type == pygame.QUIT:
            running = False

    # fill screen with color for new frame
    screen.fill('blue')

    if ds < 0:
        ds = 1280

    ds -= 10

    # circle plot according to new position
    pygame.draw.circle(screen, "red", player_pos, 40)

    # platform
    pygame.draw.rect(screen, "green", (0, screen.get_height() /
                     2, screen.get_width(), screen.get_height()))

    # obstacle
    pygame.draw.circle(screen, "black", (ds, screen.get_height()/2), 40)

    # if player hits obstacles
    if player_pos.y == screen.get_height()/2:
        if ds <= player_pos.x + 20 and ds > player_pos.x - 20:
            reset()

    # keys for navigation
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if not jump:
            jump = True

    if jump:
        ts += 1
        if ts < 15:
            player_pos.y -= 15
        elif ts >= 15 and ts < 29:
            player_pos.y += 15
        else:
            jump = False
            ts = 0

    # display everything on screen
    pygame.display.flip()

    # 60 fps
    # delta time
    dt = clock.tick(60)/1000

pygame.quit()

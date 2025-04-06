# moving circle on screen game
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


# circle at the center
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
# player_pos = pygame.Vector2(0,0)

while running:
    for event in pygame.event.get():
        # pygame.QUIT = X button on the window
        if event.type == pygame.QUIT:
            running = False

    # fill screen with color for new frame
    screen.fill('purple')

    print("check")

    # circle plot according to new position
    pygame.draw.circle(screen, "red", player_pos, 40)

    # keys for navigation
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300*dt

    if keys[pygame.K_s]:
        player_pos.y += 300*dt

    if keys[pygame.K_a]:
        player_pos.x -= 300*dt

    if keys[pygame.K_d]:
        player_pos.x += 300*dt

    print("test")

    # display everything on screen
    pygame.display.flip()

    # 60 fps
    # delta time
    dt = clock.tick(60)/1000

pygame.quit()

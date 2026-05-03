import pygame


ENDGAME = 0
RUN = 1
NEWGAME = 2


def defaultSetup():
    ds = 1280
    ts = 0
    jump = False
    return ds, ts, jump


def resetScreen(screen, text_renders):
    pygame.draw.rect(screen, "yellow", (0, 0, screen.get_width(), screen.get_height()))
    screen.blit(text_renders, (0, 0))


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    
    # font and text setup
    font = pygame.font.SysFont('Times New Roman', 50)
    texts = ['Press space to start', 'Game Over! Press space to restart']
    text_renders = [font.render(text, True, (0, 0, 255)) for text in texts]

    # player starts at the center
    player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

    ds, ts, jump = defaultSetup()

    gameState = NEWGAME
    resetScreen(screen, text_renders[0])

    while gameState != ENDGAME:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            # pygame.QUIT = X button on the window
            if event.type == pygame.QUIT:
                gameState = ENDGAME
            elif gameState == NEWGAME and keys[pygame.K_SPACE]:
                gameState = RUN
                ds = 0

        if gameState == RUN:
            # move obstacle according to delta time
            if ds < 0:
                ds = 1320
            ds -= 10
            
            # fill screen with color for new frame
            screen.fill('blue')

            # circle plot according to new position
            pygame.draw.circle(screen, "red", player_pos, 40)

            # platform
            pygame.draw.rect(screen, "green", (0, screen.get_height() /
                            2, screen.get_width(), screen.get_height()))

            # obstacle
            pygame.draw.circle(screen, "black", (ds, screen.get_height()/2), 40)

            # if player hits obstacles
            # check if player is on the platform and if the obstacle is within the player's x range
            if player_pos.y == screen.get_height()/2:
                if ds <= player_pos.x + 80 and ds > player_pos.x - 80:
                    ds, ts, jump = defaultSetup()
                    resetScreen(screen, text_renders[1])
                    gameState = NEWGAME

            # keys for navigation
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                if not jump:
                    # start jumping if space is pressed and player is not already jumping
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
        clock.tick(60)/1000

    pygame.quit()


if __name__ == "__main__":
    main()

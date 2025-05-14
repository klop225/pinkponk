import pygame

pygame.init()
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
x = WIDTH // 2
y = HEIGHT // 2

pole = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("pong")
clock = pygame.time.Clock()

raketkaL = pygame.Rect(30, HEIGHT // 2 - 50, 15,100)
raketkaR = pygame.Rect(770,HEIGHT // 2 - 50, 15,100)
shar = pygame.draw.circle(pole, WHITE, (x, y), 10)

raketka_speed = 7
shar_x_speed = 5
shar_y_speed = 5

chet1 = 0
chet2 = 0

font = pygame.font.Font(None, 36)

run = True
while run:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if raketkaL.top > 0:
            raketkaL.y -= raketka_speed
    if keys[pygame.K_s]:
        if raketkaL.bottom < HEIGHT:
            raketkaL.y += raketka_speed
    if keys[pygame.K_UP]:
        if raketkaR.top > 0:
            raketkaR.y -= raketka_speed
    if keys[pygame.K_DOWN]:
        if raketkaR.bottom < HEIGHT:
            raketkaR.y += raketka_speed

    shar.x += shar_x_speed
    shar.y += shar_y_speed

    if shar.topleft[0] <= 0 or shar.bottomright[0] >= WIDTH:
        shar_x_speed = -shar_x_speed
    if shar.topleft[1] <= 0 or shar.topleft[1] >= HEIGHT:
        shar_y_speed = -shar_y_speed

    if shar.colliderect(raketkaL) or shar.colliderect(raketkaR):
        shar_x_speed *= -1

    if shar.left <= 0:
        chet1 += 1
        shar.x = WIDTH // 2 - 10 // 2
        shar.y = HEIGHT // 2 - 10 // 2
    if shar.right >= WIDTH:
        chet2 += 1
        shar.x = WIDTH // 2 - 10 // 2
        shar.y = HEIGHT // 2 - 10 // 2

    pole.fill((0, 0, 0))
    pygame.draw.rect(pole,WHITE,raketkaR)
    pygame.draw.rect(pole,WHITE,raketkaL)
    pygame.draw.ellipse(pole,WHITE,shar)

    chet = font.render(f"{chet2} : {chet1}", True,WHITE)
    pole.blit(chet,(WIDTH // 2 - 20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
import pygame
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("shitty ass tutorial pygame game")

SKULL_HIT = pygame.USEREVENT + 1
MOAI_HIT = pygame.USEREVENT + 2
skull_bullets = [] 
moai_bullets = []
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
space1 = pygame.image.load('C:/Users/NOOBY124/code shit/pygamefirstgame asstests/image-removebg-preview.png')
space2 = pygame.image.load('C:/Users/NOOBY124/code shit/pygamefirstgame asstests/image-removebg-preview(1).png')
def draw_window(skull_bullets, moai_bullets, skull, moai):
    WIN.fill((48, 10, 36))
    pygame.draw.rect(WIN, black, BORDER)
    WIN.blit(space1, (skull.x, skull.y))
    WIN.blit(space2, (moai.x, moai.y))
    for bullet in moai_bullets:
        pygame.draw.rect(WIN, yellow, bullet)
    for bullet in skull_bullets:
        pygame.draw.rect(WIN, yellow, bullet)
    pygame.display.update()
def skull_handle_movement(keys_pressed, skull):
    if keys_pressed[pygame.K_a] and skull.x - VEL > 0: #!left
        skull.x -= VEL
    if keys_pressed[pygame.K_d] and skull.x + VEL + skull.width < BORDER.x - 25: #!right
        skull.x += VEL
    if keys_pressed[pygame.K_w] and skull.y - VEL > 0: #!up
        skull.y -= VEL
    if keys_pressed[pygame.K_s] and skull.y + VEL + skull.height < HEIGHT - 40: #!down
        skull.y += VEL

def moai_handle_movement(keys_pressed, moai):
    if keys_pressed[pygame.K_LEFT] and moai.x - VEL > BORDER.x + BORDER.width - 50: #!left
        moai.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and moai.x + VEL + moai.width < WIDTH + -55: #!right
        moai.x += VEL
    if keys_pressed[pygame.K_UP] and moai.y - VEL > 0: #!up
        moai.y -= VEL
    if keys_pressed[pygame.K_DOWN] and moai.y + VEL + moai.height < HEIGHT - 50: #!down
        moai.y += VEL

def handle_bullets(skull_bullets, moai_bullets, skull, moai):
    for bullet in skull_bullets:
        bullet.x += BULLET_VEL
        if moai.colliderect(bullet):
            pygame.event.post(pygame.event.Event(MOAI_HIT))
            skull_bullets.remove(bullet)
    for bullet in moai_bullets:
        bullet.x -= BULLET_VEL
        if skull.colliderect(bullet):
            pygame.event.post(pygame.event.Event(SKULL_HIT))
            moai_bullets.remove(bullet)
            

def main():
    global skull
    global moai
    skull = pygame.Rect(100, 300, 30, 20)
    moai = pygame.Rect(700, 300, 30, 20)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and len(skull_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        skull.x + skull.width, skull.y + skull.height//2 - 2, 10 - 3, 50)
                    skull_bullets.append(bullet)
                
                if event.key == pygame.K_RSHIFT and len(moai_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        moai.x - moai.width, moai.y - moai.height + 55//2 - 2, 10 - 3, 50)
                    moai_bullets.append(bullet)
                    



        
        global keys_pressed
        keys_pressed = pygame.key.get_pressed()
        skull_handle_movement(keys_pressed, skull)
        moai_handle_movement(keys_pressed, moai)

        handle_bullets(skull_bullets, moai_bullets, skull, moai)

        draw_window(skull_bullets, moai_bullets, skull, moai)
    pygame.quit()


if __name__ == "__main__":
    print("sup")
    main()
    print("bye")

import pygame
import time
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
pygame.mixer.init()
pygame.font.init()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("cursed ass pygame game")
HEALTH_FONT = pygame.font.SysFont("comicsans", 35)
hitsound = pygame.mixer.Sound("bonk.mp3")
shootsound = pygame.mixer.Sound("vineboom.mp3")
skullwonsound = pygame.mixer.Sound("skull won.mp3")
moaiwonsound = pygame.mixer.Sound("moai won.mp3")
global SKULL_HEALTH
global MOAI_HEALTH
SKULL_HEALTH = 3
MOAI_HEALTH = 3
SKULL_HIT = pygame.USEREVENT + 1
MOAI_HIT = pygame.USEREVENT + 2
skull_bullets = [] 
moai_bullets = []
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
space1 = pygame.image.load('image-removebg-preview.png')
space2 = pygame.image.load('image-removebg-preview(1).png')
bg = pygame.transform.scale(pygame.image.load('bg.png'), (WIDTH, HEIGHT))
def draw_window(skull_bullets, moai_bullets, skull, moai, SKULL_HEALTH, MOAI_HEALTH):
    WIN.blit(bg, (0, 0))
    pygame.draw.rect(WIN, (0, 0, 0), BORDER)
    WIN.blit(space1, (skull.x, skull.y - 13))
    WIN.blit(space2, (moai.x - 50, moai.y - 20))
    for bullet in moai_bullets:
        pygame.draw.rect(WIN, yellow, bullet)
    for bullet in skull_bullets:
        pygame.draw.rect(WIN, yellow, bullet)
    if MOAI_HEALTH == 3:
        moai_health_text = HEALTH_FONT.render(
            "Health: " + str(3), 1, (255, 255, 255))
    if MOAI_HEALTH == 3:
        skull_health_text = HEALTH_FONT.render(
            "Health: " + str(3), 1, (255, 255, 255))
    if MOAI_HEALTH == 2:
        moai_health_text = HEALTH_FONT.render(
            "Health: " + str(2), 1, (255, 255, 255))
    if SKULL_HEALTH == 2:
        skull_health_text = HEALTH_FONT.render(
            "Health: " + str(2), 1, (255, 255, 255))
    if MOAI_HEALTH == 1:
        moai_health_text = HEALTH_FONT.render(
            "Health: " + str(1), 1, (255, 255, 255))
    if SKULL_HEALTH == 1:
        skull_health_text = HEALTH_FONT.render(
            "Health: " + str(1), 1, (255, 255, 255))
    skull_health_text = HEALTH_FONT.render(
            "Health: " + str(SKULL_HEALTH), 1, (255, 255, 255))
    WIN.blit(skull_health_text, (730, 10))
    WIN.blit(moai_health_text, (10, 10))
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
    if keys_pressed[pygame.K_LEFT] and moai.x - VEL > BORDER.x + BORDER.width - 5: #!left
        moai.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and moai.x + VEL + moai.width < WIDTH: #!right
        moai.x += VEL
    if keys_pressed[pygame.K_UP] and moai.y - VEL > 0: #!up
        moai.y -= VEL
    if keys_pressed[pygame.K_DOWN] and moai.y + VEL + moai.height < HEIGHT - 50: #!down
        moai.y += VEL

def handle_bullets(skull_bullets, moai_bullets, skull, moai):
    for bullet in skull_bullets:
        bullet.x += BULLET_VEL
        if moai.colliderect(bullet):
            hitsound.play()
            MOAI_HEALTH = 3
            pygame.event.post(pygame.event.Event(MOAI_HIT))
            skull_bullets.remove(bullet)
            
        elif bullet.x > WIDTH:
            skull_bullets.remove(bullet)
    for bullet in moai_bullets:
        bullet.x -= BULLET_VEL
        if skull.colliderect(bullet):
            hitsound.play
            SKULL_HEALTH = 3
            pygame.event.post(pygame.event.Event(SKULL_HIT))
            moai_bullets.remove(bullet)
            SKULL_HEALTH -= 1
            
        elif bullet.x < 0:
            moai_bullets.remove(bullet)            

def main(MOAI_HEALTH, SKULL_HEALTH):
    global skull
    global moai
    skull = pygame.Rect(100, 300, 30, 20)
    moai = pygame.Rect(700, 300, 30, 20)
    clock = pygame.time.Clock()
    run = True
    pygame.mixer.music.load("Tobu_candyland_full_mp3.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and len(skull_bullets) < MAX_BULLETS:
                    shootsound.play()
                    bullet = pygame.Rect(
                        skull.x + skull.width, skull.y + skull.height//2 - 2, 10 - 3, 30)
                    skull_bullets.append(bullet)
                
                if event.key == pygame.K_RSHIFT and len(moai_bullets) < MAX_BULLETS:
                    shootsound.play()
                    bullet = pygame.Rect(
                        moai.x - moai.width, moai.y - moai.height + 55//2 - 2, 10 - 3, 30)
                    moai_bullets.append(bullet)
            if event.type == SKULL_HIT:
                SKULL_HEALTH -= 1
            if event.type == MOAI_HIT:
                MOAI_HEALTH -= 1
        
        winner_text = ""
        if MOAI_HEALTH <= 0:
            time.sleep(0.2)
            skullwonsound.play()
            time.sleep(1)
            pygame.quit()

        if SKULL_HEALTH <= 0:
            time.sleep(0.2)
            moaiwonsound.play()
            time.sleep(1)
            pygame.quit()
        if winner_text != "":
            break
        global keys_pressed
        keys_pressed = pygame.key.get_pressed()
        skull_handle_movement(keys_pressed, skull)
        moai_handle_movement(keys_pressed, moai)

        handle_bullets(skull_bullets, moai_bullets, skull, moai)
        draw_window(skull_bullets, moai_bullets, skull, moai, MOAI_HEALTH, SKULL_HEALTH)
    pygame.quit()


if __name__ == "__main__":
    print("sup")
    main(MOAI_HEALTH, SKULL_HEALTH)
    print("bye")
    
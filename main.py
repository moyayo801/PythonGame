import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 950, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FALLING STARS")

BG = pygame.transform.scale(pygame.image.load("bg.jfif"),(WIDTH, HEIGHT)) 

star_image = pygame.image.load("bbg.png").convert_alpha()
player_image = pygame.image.load("ppp.png").convert_alpha()
PLAYER_WIDTH = 45
PLAYER_HEIGHT = 125
PLAYER_VEL = 5
STAR_WIDTH = 35
STAR_HEIGHT = 30
STAR_VEL = 4
FONT =  pygame.font.SysFont("Tahoma", 22)
FONT2 =  pygame.font.SysFont("Tahoma", 40)

def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0,0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s",1, (222, 230, 234))

    WIN.blit(time_text,(10,10))

    #pygame.draw.rect(WIN, "red", player)
    
    WIN.blit(player_image,player)
    for star in stars:
        
       
        WIN.blit(star_image,star)

    pygame.display.update()

def main():
    run = True

    player = player_image.get_rect(left = 200 , top = HEIGHT - PLAYER_HEIGHT, width = PLAYER_WIDTH, height = PLAYER_HEIGHT) #pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0

    star_add_inc = 2000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_inc:
            for _ in range(3): #pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = star_image.get_rect(left = star_x, top = -STAR_HEIGHT, width = STAR_WIDTH, height = STAR_HEIGHT) 
                stars.append(star)
            star_add_inc = max(200, star_add_inc-50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x -PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x +PLAYER_VEL+ player.width <= WIDTH:
            player.x += PLAYER_VEL  

        for star in stars[:]:
            star.y += STAR_VEL  
            if star.y > HEIGHT:
                stars.remove(star) 
            elif star.y +star.height >= player.y  and star.colliderect(player):
                  stars.remove(star)
                  hit= True
                  break

        if hit:
            lost_text = FONT2.render("YOU LOST", 1, (222, 230, 234))
            WIN.blit(lost_text,(WIDTH/2 - lost_text.get_width()/2,HEIGHT/2 - lost_text.get_height()/2 ))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)

    pygame.quit()  

if __name__ == "__main__":
    main()      


















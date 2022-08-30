import pygame
from sys import exit

def display_score():
    current_time = (pygame.time.get_ticks() // 1000)-start_time
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)


pygame.init() # initialise all of pygame
screen = pygame.display.set_mode((800,400)) #(width, hight)
pygame.display.set_caption('Runner') # string of the window title
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50) # font type, font size
start_time = 0
game_active = True

# test_surface = pygame.Surface((100,200))
# test_surface.fill('Red')

sky_surf = pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surf = pygame.image.load("graphics/ground.png").convert_alpha()

score_surf = test_font.render('My Game',False,(64,64,64)) # content, anti aliasing, color
score_rect = score_surf.get_rect(center = (400,50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (700,300))

player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

player_gravity = 0 

while True:
    for event in pygame.event.get(): # gets all the events and loops through them
        if event.type == pygame.QUIT: # closing the window
            pygame.quit() # opposite to pygame.init()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -21

            if event.type == pygame.KEYDOWN and player_rect.bottom >= 300:
                if event.key == pygame.K_SPACE:
                    player_gravity = -21
        
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 600
                start_time = (pygame.time.get_ticks() // 1000)

    if game_active:
        screen.blit(ground_surf,(0,300))
        screen.blit(sky_surf,(0,0)) # put test_surface on display
        # pygame.draw.rect(screen,'#c0e8ec',score_rect)
        # pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
        # screen.blit(score_surf,score_rect)
        display_score()

        snail_rect.x -= 4
        if snail_rect.right < 0:  snail_rect.left = 800
        screen.blit(snail_surf,snail_rect)



        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        if snail_rect.colliderect(player_rect):
            game_active=False
            
    else:
        screen.fill('Yellow')


    pygame.display.update()
    clock.tick(60) # sets the frame limit to 60 FPS

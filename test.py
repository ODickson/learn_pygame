import pygame
from sys import exit


pygame.init() # initialise all of pygame
screen = pygame.display.set_mode((800,400)) #(width, hight)
pygame.display.set_caption('Runner') # string of the window title
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50) # font type, font size

# test_surface = pygame.Surface((100,200))
# test_surface.fill('Red')

sky_surf = pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surf = pygame.image.load("graphics/ground.png").convert_alpha()
text_surf = test_font.render('My Game',False,'Black') # content, anti alyasing, color

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (700,300))

player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get(): # gets all the events and loops through them
        if event.type == pygame.QUIT: # closing the window
            pygame.quit() # opposite to pygame.init()
            exit()
        if event.type == pygame.MOUSEMOTION:
            payler_rect.collidepoint(event.pos)

    screen.blit(ground_surf,(0,300))
    screen.blit(sky_surf,(0,0)) # put test_surface on display
    screen.blit(text_surf,(300,50))
    
    snail_rect.x -= 4
    if snail_rect.right < 0:  snail_rect.left = 800
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print("Collision")

    # mouse_pos - pygame.mouse.get_pos()
    # if payler_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60) # sets the frame limit to 60 FPS

import pygame
pygame.init()
surface=pygame.display.set_mode((500,500))
pygame.display.set_caption("Adding image and background image")
bgimage=pygame.transform.scale(pygame.image.load("bg.jpeg").convert(),(500,500))
cimage=pygame.transform.scale(pygame.image.load("character.jpeg").convert_alpha(),(200,200))
crect=cimage.get_rect(center=(500//2,500//2-30))

text=pygame.font.Font(None,36).render("It's a me Mario",True,pygame.Color("white"))
trect=text.get_rect(center=(500//2,500//2+110))
def game_loop():
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        surface.blit(bgimage,(0,0))
        surface.blit(cimage,crect)
        surface.blit(text,trect)
        pygame.display.flip()
    pygame.quit()
game_loop()
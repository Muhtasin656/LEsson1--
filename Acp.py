import pygame
pygame.init()
surface=pygame.display.set_mode((500,500))
backgimage=pygame.transform.scale(pygame.image.load("ACPim1.jpeg").convert(),(600,600))
characterimage=pygame.transform.scale(pygame.image.load("ACPim2.jpeg").convert_alpha(),(200,200))
crect=characterimage.get_rect(center=(600/3,600//3-40))

text=pygame.font.Font(None,36).render("It is me Edgar",True,pygame.Color("black"))
trect=text.get_rect(center=(500//2,500//2+110))
def game_loop():
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        surface.blit(backgimage,(0,0))
        surface.blit(characterimage,crect)
        surface.blit(text,trect)
        pygame.display.flip()
    pygame.quit()
game_loop()
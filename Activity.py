# import library
import pygame

#intial module
pygame.init()

# setup window geometry
screen=pygame.display.set_mode((500,500))


# create a loop to run till the game is quit by user
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    # make the changes visible
    pygame.display.flip()
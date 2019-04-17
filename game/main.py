import pygame

pygame.init()
disp=pygame.display.set_mode((800,600))
img=pygame.image.load("hqdefault.png")
finish=False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish=True
    disp.blit(img,(100,100))
    pygame.display.update()

pygame.quit()
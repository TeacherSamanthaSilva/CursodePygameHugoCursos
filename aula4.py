import pygame, sys
pygame.init()
screen = pygame.display.set_mode((640, 480))
font = pygame.font.Font(None, 36)

panel = pygame.Surface((300, 200), pygame.SRCALPHA)
panel.fill((0, 0, 0, 150))  # painel semi-transparente

# desenhar formas sobre a surface
pygame.draw.rect(panel, (255, 0, 0), (10, 10, 100, 50))
pygame.draw.circle(panel, (0, 0, 255), (200, 100), 40)

# texto
txt = font.render("Painel", True, (255,255,255))
panel.blit(txt, (10,70))

clock = pygame.time.Clock()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    screen.fill((50,50,50))
    screen.blit(panel, (170,140))
    pygame.display.flip()
    clock.tick(60)

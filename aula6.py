#importando a biblioteca pygame
import pygame

#iniciando o  pygame
pygame.init()

largura = 640
altura = 360
tela = pygame.display.set_mode((largura,altura))
clock = pygame.time.Clock()

# Superfície de fundo (pode ser uma imagem também)
background = pygame.Surface((largura, altura))
background.fill((30, 30, 60))

# Superfície overlay com alpha por pixel (transparente)
overlay = pygame.Surface((200, 120), pygame.SRCALPHA)
# desenha um retângulo semi-transparente e um círculo
overlay.fill((0, 0, 0, 0))               # totalmente transparente inicialmente
pygame.draw.rect(overlay, (255, 255, 255, 120), (0, 0, 200, 120), border_radius=12)
pygame.draw.circle(overlay, (255, 0, 0, 200), (50, 60), 30)

# Se quiser usar uma imagem: 
# overlay = pygame.image.load("overlay.png").convert_alpha()

# posição do overlay (por exemplo, centro da tela)
overlay_rect = overlay.get_rect(center=(largura // 2, altura // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # desenha fundo
    tela.blit(background, (0, 0))

    # desenha o overlay sobre o fundo
    tela.blit(overlay, overlay_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
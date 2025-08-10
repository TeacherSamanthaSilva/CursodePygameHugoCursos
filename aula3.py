#importar as bibliotecas que serão utilizadas
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))

#criando uma superficie
sup = pygame.Surface((200, 150)) #largura e altura da superficie

#preencher com cor
sup.fill((255,100,50))

# Opcional: permitir canal alfa por pixel (transparência)
surf_alpha = pygame.Surface((200, 150), pygame.SRCALPHA)
surf_alpha.fill((0, 255, 0, 128))  # RGBA, 128 = semi-transparente

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #comando para limpar a tela
    screen.fill((30,30,30))

# Blitar (copiar) surf para a tela em (50, 50)
    screen.blit(sup, (50, 50))
    # Blitar surf com alfa
    screen.blit(surf_alpha, (300, 50))

    pygame.display.flip()
    clock.tick(27)

    """ pygame.Surface((w, h)) — cria uma superfície simples.

pygame.Surface((w, h), pygame.SRCALPHA) — cria superfície com canal alfa por pixel (permite transparência parcial).

surf.fill((r,g,b)) ou surf.fill((r,g,b,a)) — preenche a superfície.

screen.blit(surf, (x,y)) — desenha (copia) surf na superfície alvo (por exemplo, a janela).

surf.set_colorkey((r,g,b)) — define uma cor que será transparente (útil sem alfa).

surf.set_alpha(value) — define alfa inteiro para toda a superficie (0-255).

surf.convert() e surf.convert_alpha() — converte formato para otimizar velocidade de blit; use convert_alpha() se a surface tiver transparência.

Desenhar na surface: pygame.draw.rect(surf, color, rect), pygame.draw.circle(...) etc.

Textos: font = pygame.font.Font(None, 30); text_surf = font.render("Olá", True, (255,255,255)); surf.blit(text_surf, (10,10)). """
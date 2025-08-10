import pygame

# Inicializa o pygame
pygame.init()

# Cria a janela
largura, altura = 400, 300
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Cores por Variáveis")

# Definindo cores com variáveis (RGB)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)

# Criando superfícies com cores
superficie_vermelha = pygame.Surface((100, 100))
superficie_vermelha.fill(VERMELHO)

superficie_verde = pygame.Surface((100, 100))
superficie_verde.fill(VERDE)

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Preenche a janela
    janela.fill(BRANCO)

    # Desenha as superfícies
    janela.blit(superficie_vermelha, (50, 50))
    janela.blit(superficie_verde, (200, 50))

    # Atualiza a tela
    pygame.display.flip()

pygame.quit()


import pygame

#inicializando o pygame
pygame.init()

#define as dimensões da janela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("meu primeiro jogo")

# Define a fonte (tamanho 36)
fonte = pygame.font.Font(None, 36)  # None = fonte padrão do pygame

# Renderiza o texto (texto, antialias, cor)
texto = fonte.render("Olá, mundo!", True, (255, 255, 255))  # Branco

# Posição do texto
pos_texto = (100, 100)

#loop principal
rodando = True
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

# Preenche a tela com preto
    tela.fill((0, 0, 0))

    # Desenha o texto
    tela.blit(texto, pos_texto)

    # Atualiza a tela
    pygame.display.flip()

pygame.quit()
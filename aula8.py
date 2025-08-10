import pygame

# Inicializa o pygame
pygame.init()

# Cria a janela
largura, altura = 500, 400
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Botão com Clique")

# Define cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERMELHO_ESCURO = (200, 0, 0)

# Define o botão
botao = pygame.Rect(150, 150, 200, 80)
cor_botao = VERMELHO

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # Quando o mouse é pressionado
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Botão esquerdo
                if botao.collidepoint(evento.pos):
                    cor_botao = VERMELHO_ESCURO
                    print("Botão pressionado!")

        # Quando o mouse é solto
        if evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                cor_botao = VERMELHO  # Volta à cor original
                if botao.collidepoint(evento.pos):
                    print("Botão clicado!")

    # Desenha a tela
    janela.fill(BRANCO)
    pygame.draw.rect(janela, cor_botao, botao, border_radius=10)  # Botão arredondado
    pygame.display.flip()

# Encerra o pygame
pygame.quit()

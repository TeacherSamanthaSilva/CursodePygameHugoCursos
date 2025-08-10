import pygame

# Inicializa o pygame
pygame.init()

# Cria uma janela
largura, altura = 500, 400
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Exemplo de Clique do Mouse")

# Define cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

# Define um retângulo (área clicável)
botao = pygame.Rect(150, 150, 200, 80)

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        # Evento de fechamento da janela
        if evento.type == pygame.QUIT:
            rodando = False

        # Evento de clique do mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Botão esquerdo do mouse
                pos_mouse = pygame.mouse.get_pos()
                print("Posição do clique:", pos_mouse)

                # Verifica se clicou no retângulo
                if botao.collidepoint(pos_mouse):
                    print("Botão clicado!")

    # Desenha a tela
    janela.fill(BRANCO)
    pygame.draw.rect(janela, VERMELHO, botao)  # Desenha o botão
    pygame.display.flip()

# Encerra o pygame
pygame.quit()

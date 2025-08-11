import pygame

# Inicializa o pygame
pygame.init()

# Cria a janela
largura, altura = 500, 400
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Botão com Texto")

# Define cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERMELHO_ESCURO = (200, 0, 0)
PRETO = (0, 0, 0)

# Define fonte
fonte = pygame.font.Font(None, 40)  # None usa fonte padrão do pygame, 40 é o tamanho

# Define o botão
botao = pygame.Rect(150, 150, 200, 80)
cor_botao = VERMELHO
texto_botao = "Clique aqui"

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
                cor_botao = VERMELHO
                if botao.collidepoint(evento.pos):
                    print("Botão clicado!")

    # Desenha a tela
    janela.fill(BRANCO)

    # Desenha o botão
    pygame.draw.rect(janela, cor_botao, botao, border_radius=10)

    # Renderiza o texto e centraliza no botão
    texto_render = fonte.render(texto_botao, True, PRETO)
    texto_rect = texto_render.get_rect(center=botao.center)
    janela.blit(texto_render, texto_rect)

    pygame.display.flip()

# Encerra o pygame
pygame.quit()

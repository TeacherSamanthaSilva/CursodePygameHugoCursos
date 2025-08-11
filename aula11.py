import pygame

# Inicializa o pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Movimento com Teclado")

# Configurações do personagem
x = 400
y = 300
velocidade = 5
largura_personagem = 50
altura_personagem = 50

# Cor do personagem
cor_personagem = (0, 255, 0)  # Verde

# Loop principal
rodando = True
while rodando:
    # Captura eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Captura teclas pressionadas
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:  # Esquerda
        x -= velocidade
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:  # Direita
        x += velocidade
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:  # Cima
        y -= velocidade
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:  # Baixo
        y += velocidade

    # Limita para não sair da tela
    x = max(0, min(x, largura - largura_personagem))
    y = max(0, min(y, altura - altura_personagem))

    # Desenha fundo e personagem
    tela.fill((0, 0, 0))  # Preto
    pygame.draw.rect(tela, cor_personagem, (x, y, largura_personagem, altura_personagem))

    # Atualiza tela
    pygame.display.update()

    # Controla FPS
    pygame.time.Clock().tick(60)

# Encerra pygame
pygame.quit()

import pygame

# Inicializa o Pygame
pygame.init()

# Configurações da janela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Movimento e Colisão")

# Cores
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

# Velocidade do personagem
velocidade = 5

# Criar o retângulo do personagem
personagem = pygame.Rect(100, 100, 50, 50)  # x, y, largura, altura

# Criar um obstáculo
obstaculo = pygame.Rect(400, 300, 100, 100)

# Loop principal
rodando = True
while rodando:
    # Limita o FPS
    pygame.time.Clock().tick(60)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento do personagem
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        personagem.x -= velocidade
    if teclas[pygame.K_RIGHT]:
        personagem.x += velocidade
    if teclas[pygame.K_UP]:
        personagem.y -= velocidade
    if teclas[pygame.K_DOWN]:
        personagem.y += velocidade

    # Verificação de colisão
    if personagem.colliderect(obstaculo):
        print("Colidiu com o obstáculo!")
        # Exemplo: empurrar o personagem para trás
        if teclas[pygame.K_LEFT]:
            personagem.x += velocidade
        if teclas[pygame.K_RIGHT]:
            personagem.x -= velocidade
        if teclas[pygame.K_UP]:
            personagem.y += velocidade
        if teclas[pygame.K_DOWN]:
            personagem.y -= velocidade

    # Desenho
    tela.fill(BRANCO)
    pygame.draw.rect(tela, AZUL, personagem)   # Personagem
    pygame.draw.rect(tela, VERMELHO, obstaculo) # Obstáculo
    pygame.display.flip()

pygame.quit()

import pygame
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colisão com Som")

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Sons
pygame.mixer.music.load("fundo.mp3")  # Som de fundo
pygame.mixer.music.play(-1)  # -1 = loop infinito

colisao_sound = pygame.mixer.Sound("colisao.mp3")  # Som de colisão

# Objetos
player = pygame.Rect(100, 100, 50, 50)
obstaculo = pygame.Rect(400, 300, 100, 100)

# Velocidade
vel = 5

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimento do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= vel
    if keys[pygame.K_RIGHT]: player.x += vel
    if keys[pygame.K_UP]: player.y -= vel
    if keys[pygame.K_DOWN]: player.y += vel

    # Verifica colisão
    if player.colliderect(obstaculo):
        colisao_sound.play()

    # Desenha na tela
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, BLUE, obstaculo)
    pygame.display.update()

import pygame 

#Inicializa o pygame
pygame.init()

#define o tamanho da tela
largura = 800
altura = 600

#cria a tela
tela = pygame.display.set_mode(largura,altura)
pygame.display.set_caption("Meu primeiro jogo")

#controle do loop principal
rodando = True

while rodando:
    #loop de eventos
    #criando o evento de sair
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

#cor da tela de fundo em RGB
tela.fill(50,100,200)

#atualiza a tela
pygame,display.flip()

#finaliza o jogo
pygame.quit()

""" pygame.event.get() → pega todos os eventos (como clicar no X da janela, pressionar teclas, mover o mouse, etc.).

if evento.type == pygame.QUIT: → verifica se o evento é o de fechar a janela.

rodando = False → encerra o loop principal e fecha o programa.

tela.fill() → preenche a tela com uma cor de fundo.

pygame.display.flip() → atualiza a tela com o que foi desenhado. """
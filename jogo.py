import pygame
from map import map
import sys

class Jogo:
    def __init__(self):
        pygame.init()
        self.janela = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Jogo 2D")

        # Carrega o mapa
        self.mapa = map(10, 10)

    def run(self):
        while True:
            # Lógica do jogo

            # Desenha o mapa na tela
            self.mapa.desenhar(self.janela)

            # Atualiza a tela
            pygame.display.update()

            # Verifica eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    jogo = Jogo()
    jogo.run()

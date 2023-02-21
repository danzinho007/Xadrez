# Gerando muitos objetos 

import random
import string

# Definindo as dimensões dos mapas
NUM_LINHAS = 10
NUM_COLUNAS = 10

# Lista de caracteres permitidos para os elementos do mapa
CARACTERES_VALIDOS = "#@. $*"

# Gerando os 100 mapas jogáveis com paredes ao redor
mapas = []
for i in range(100):
    # Gerando um novo mapa vazio com paredes ao redor
    novo_mapa = []
    for j in range(NUM_LINHAS+2):
        if j == 0 or j == NUM_LINHAS+1:
            nova_linha = "#" * (NUM_COLUNAS+2)
        else:
            nova_linha = "#" + "." * NUM_COLUNAS + "#"
        novo_mapa.append(nova_linha)
    # Colocando o jogador em um local vazio
    while True:
        posicao_jogador = (random.randint(1, NUM_LINHAS), random.randint(1, NUM_COLUNAS))
        if novo_mapa[posicao_jogador[0]][posicao_jogador[1]] == ".":
            novo_mapa[posicao_jogador[0]] = novo_mapa[posicao_jogador[0]][:posicao_jogador[1]] + "@" + novo_mapa[posicao_jogador[0]][posicao_jogador[1]+1:]
            break
    # Colocando as caixas em locais vazios, sem bloquear o caminho do jogador
    posicoes_caixas = []
    for j in range(3):
        while True:
            posicao_caixa = (random.randint(1, NUM_LINHAS), random.randint(1, NUM_COLUNAS))
            if novo_mapa[posicao_caixa[0]][posicao_caixa[1]] == "." and all(posicao_caixa != p for p in posicoes_caixas):
                novo_mapa[posicao_caixa[0]] = novo_mapa[posicao_caixa[0]][:posicao_caixa[1]] + "$" + novo_mapa[posicao_caixa[0]][posicao_caixa[1]+1:]
                posicoes_caixas.append(posicao_caixa)
                break
    # Nomeando o mapa com uma string aleatória de 6 letras
    nome_mapa = ''.join(random.choices(string.ascii_uppercase, k=6))
    mapas.append((nome_mapa, novo_mapa))

# Imprimindo os mapas gerados
for nome_mapa, mapa in mapas:
    print(f"Mapa {nome_mapa}:")
    for linha in mapa:
        print(linha)
    print()

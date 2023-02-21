# Definindo a função para verificar se os mapas são iguais (mesma função do exemplo anterior)
def sao_mapas_iguais(mapa1, mapa2):
    if len(mapa1) != len(mapa2) or len(mapa1[0]) != len(mapa2[0]):
        return False
    
    for i in range(len(mapa1)):
        for j in range(len(mapa1[0])):
            if mapa1[i][j] != mapa2[i][j]:
                return False
    
    return True


# Definindo a lista de mapas que queremos comparar
mapas = [
    [
        "#####",
        "#.@.#",
        "#$ $.#",
        "#   #",
        "#####",
    ],
    [
        "#####",
        "#.@.#",
        "# $.#",
        "#$  #",
        "#####",
    ],
    [
        "#####",
        "#.@.#",
        "#  $.#",
        "#$  #",
        "#####",
    ],
    [
        "#####",
        "#.@.#",
        "#  $.#",
        "#$  #",
        "#####",
    ],
]

# Criando uma lista vazia para armazenar as informações sobre mapas iguais
mapas_iguais = []

# Comparando cada par de mapas usando a função sao_mapas_iguais
for i in range(len(mapas)):
    for j in range(i+1, len(mapas)):
        if sao_mapas_iguais(mapas[i], mapas[j]):
            mapas_iguais.append((i+1, j+1))  # armazena o par de mapas iguais

# Imprimindo as informações sobre mapas iguais
if len(mapas_iguais) == 0:
    print("Não foram encontrados mapas iguais")
else:
    for mapa1, mapa2 in mapas_iguais:
        print(f"Mapa {mapa1} é igual ao mapa {mapa2}")

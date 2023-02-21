# Definindo a função para verificar se os mapas são iguais (mesma função do exemplo anterior)
def sao_mapas_iguais(mapa1, mapa2):
    if len(mapa1) != len(mapa2) or len(mapa1[0]) != len(mapa2[0]):
        return False
    
    for i in range(len(mapa1)):
        for j in range(len(mapa1[0])):
            if mapa1[i][j] != mapa2[i][j]:
                return False
    
    return True


# Definindo o dicionário de mapas que queremos comparar
mapas = {
    "mapa1": [
        "#####",
        "#.@.#",
        "#$ $.#",
        "#   #",
        "#####",
    ],
    "mapa2": [
        "#####",
        "#.@.#",
        "# $.#",
        "#$  #",
        "#####",
    ],
    "mapa3": [
        "#####",
        "#.@.#",
        "#  $.#",
        "#$  #",
        "#####",
    ],
    "mapa4": [
        "#####",
        "#.@.#",
        "#  $.#",
        "#$  #",
        "#####",
    ],
}

# Criando uma lista vazia para armazenar as informações sobre mapas iguais
mapas_iguais = []

# Comparando cada par de mapas usando a função sao_mapas_iguais
chaves_mapas = list(mapas.keys())
for i in range(len(chaves_mapas)):
    for j in range(i+1, len(chaves_mapas)):
        nome_mapa1 = chaves_mapas[i]
        nome_mapa2 = chaves_mapas[j]
        if sao_mapas_iguais(mapas[nome_mapa1], mapas[nome_mapa2]):
            mapas_iguais.append((nome_mapa1, nome_mapa2))  # armazena o par de mapas iguais

# Imprimindo as informações sobre mapas iguais
if len(mapas_iguais) == 0:
    print("Não foram encontrados mapas iguais")
else:
    for mapa1, mapa2 in mapas_iguais:
        print(f"{mapa1} é igual a {mapa2}")
        resposta = input(f"Deseja apagar o mapa {mapa1}? (S/N) ")
        if resposta.lower() == "s":
            del mapas[mapa1]

# Imprimindo o dicionário atualizado
print("Mapas restantes:")
for chave, mapa in mapas.items():
    print(chave)
    for linha in mapa:
        print(linha)

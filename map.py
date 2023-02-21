import numpy as np
import random

# Define as dimensões do mapa
map_width = 20
map_height = 10

# Cria um grid com todas as posições preenchidas com 1 (representando paredes)
map_grid = np.ones((map_height, map_width), dtype=int)

# Define as posições iniciais e finais do caminho
start_row = random.randint(0, map_height-1)
start_col = 0
end_row = random.randint(0, map_height-1)
end_col = map_width-1

# Cria um caminho aleatório do início ao fim
current_row = start_row
current_col = start_col
while current_col != end_col or current_row != end_row:
    map_grid[current_row, current_col] = 0
    direction = random.randint(1, 4)
    if direction == 1 and current_row > 0:
        current_row -= 1
    elif direction == 2 and current_row < map_height-1:
        current_row += 1
    elif direction == 3 and current_col > 0:
        current_col -= 1
    elif direction == 4 and current_col < map_width-1:
        current_col += 1

# Exibe o mapa
print(map_grid)

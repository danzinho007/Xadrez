import random
# Jogo da Velha Aleatório
# Define a função para imprimir o tabuleiro
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

# Define a função para verificar se alguém ganhou o jogo
def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

# Define a função para fazer a jogada do agente
def agent_play(board):
    valid_move = False
    while not valid_move:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if board[x][y] == " ":
            board[x][y] = "O"
            valid_move = True

# Define a função para fazer a jogada do jogador humano
def human_play(board):
    valid_move = False
    while not valid_move:
        x = int(input("Digite a linha que deseja jogar (0, 1 ou 2): "))
        y = int(input("Digite a coluna que deseja jogar (0, 1 ou 2): "))
        if board[x][y] == " ":
            board[x][y] = "X"
            valid_move = True

# Define a função principal do jogo
def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print("Bem-vindo ao Jogo da Velha!")
    print_board(board)
    winner = None
    while winner is None:
        # Jogada do agente
        agent_play(board)
        print("O agente jogou:")
        print_board(board)
        winner = check_win(board)
        if winner is not None:
            print(f"O {winner} ganhou o jogo!")
            break
        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print("O jogo terminou empatado!")
            break
        # Jogada do jogador humano
        human_play(board)
        print("Você jogou:")
        print_board(board)
        winner = check_win(board)
        if winner is not None:
            print(f"Parabéns! Você ganhou o jogo!")
            break
        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print("O jogo terminou empatado!")
            break
    
# Chama a função principal do jogo
play_game()

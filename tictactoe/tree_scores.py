class Node:
    def __init__(self, board, score):
        self.board = board
        self.score = score
        self.children = []  # Lista de nodos hijos

    def add_child(self, child_node):
        # Método para agregar un nodo hijo a la lista de nodos hijos
        self.children.append(child_node)

# Definir las puntuaciones
WIN_SCORE = 10
LOSS_SCORE = -10
NEUTRAL_SCORE = 0

# Función para generar el árbol de búsqueda
def generate_tree(node, depth, current_player):
    if depth == 0 or check_game_over(node.board):
        return

    valid_moves = find_valid_moves(node.board)

    for move in valid_moves:
        new_board = [row[:] for row in node.board]
        row, col = move
        new_board[row][col] = current_player

        child_node = Node(new_board, 0)
        node.add_child(child_node)

        next_player = 'X' if current_player == 'O' else 'O'

        # Recursión para explorar el árbol
        generate_tree(child_node, depth - 1, next_player)

# Función para asignar puntuaciones
def assign_scores(node, current_player):
    if check_game_over(node.board):
        if is_winner(node.board, current_player):
            node.score = WIN_SCORE
        elif is_winner(node.board, 'X' if current_player == 'O' else 'O'):
            node.score = LOSS_SCORE
        else:
            node.score = NEUTRAL_SCORE
    else:
        for child in node.children:
            assign_scores(child, current_player)
        
        # Calcular las puntuaciones basadas en las condiciones mencionadas
        for child in node.children:
            if current_player == 'X':
                if child.score == WIN_SCORE:
                    child.score = WIN_SCORE
                elif child.score > NEUTRAL_SCORE:
                    child.score = 5  # Situación favorable en futuros turnos
                elif child.score < NEUTRAL_SCORE:
                    child.score = -5  # Podría favorecer al oponente
                else:
                    child.score = 0
            else:
                if child.score == WIN_SCORE:
                    child.score = WIN_SCORE
                elif child.score > NEUTRAL_SCORE:
                    child.score = -5  # Situación favorable en futuros turnos
                elif child.score < NEUTRAL_SCORE:
                    child.score = 5  # Podría favorecer al oponente
                else:
                    child.score = 0

    # Restaurar el puntaje original si es necesario
    if node.score == NEUTRAL_SCORE:
        node.score = NEUTRAL_SCORE

      
def check_game_over(board):
    # Verificar filas, columnas y diagonales para una victoria
    for row in board:
        if all(cell == 'X' for cell in row) or all(cell == 'O' for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)) or all(board[row][col] == 'O' for row in range(3)):
            return True

    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][i] == 'O' for i in range(3)):
        return True

    if all(board[i][2 - i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return True

    # Verificar empate (tablero lleno sin victoria)
    if all(cell != ' ' for row in board for cell in row):
        return True

    return False

#  Devuelve la lista de casillas que aún no estan ocupadas
def find_valid_moves(board):
    valid_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                valid_moves.append((row, col))
    return valid_moves

# Encontrar la mejor jugada
def minimax(node, depth, maximizing_player):
    if depth == 0 or check_game_over(node.board):
        return node.score

    if maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(node, depth, maximizing_player):
    best_move = None
    best_eval = float('-inf')
    
    for child in node.children:
        eval = minimax(child, depth - 1, not maximizing_player)
        if (maximizing_player and eval > best_eval) or (not maximizing_player and eval < best_eval):
            best_eval = eval
            best_move = (child.board, child.score)  # Devuelve el tablero y la puntuación del nodo hijo

    return best_move

# Verificar si un jugador gano
def is_winner(board, player):
    # Verificar filas
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Verificar columnas
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Verificar diagonales
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False
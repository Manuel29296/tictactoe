import tree_scores as tp

class TicTacToe:
    def __init__(self):
        # Inicializa el tablero, el jugador actual, el ganador, las casillas disponibles y la profundidad del árbol.
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.available_moves = [str(i) for i in range(1, 10)]  # Lista de casillas disponibles
        self.tree_depth = 1000  # Profundidad del árbol de búsqueda

    def make_move(self, move):
        # Realiza un movimiento en el juego.
        if move not in self.available_moves or self.winner:
            print("Casilla inválida. Elige una casilla disponible.")
            return

        move = int(move)
        row, col = (move - 1) // 3, (move - 1) % 3

        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.available_moves.remove(str(move))

            if self.check_winner(self.current_player):
                self.winner = self.current_player
            elif not self.available_moves:
                self.winner = 'Tie'
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Esta casilla ya está ocupada. Elige una casilla disponible.")

    def check_winner(self, player):
        # Verifica si un jugador ha ganado.
        for row in range(3):
            if all(cell == player for cell in self.board[row]):
                return True

        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def print_board(self):
        # Imprime el tablero actual.
        print("Tablero:")
        move_number = 1
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    cell_value = str(move_number)
                else:
                    cell_value = self.board[row][col]
                print(cell_value, end=' ')
                if col < 2:
                    print('|', end=' ')
                move_number += 1
            print()
            if row < 2:
                print('-' * 5)

    def get_winner(self):
        # Obtiene el ganador del juego.
        return self.winner

    def play(self):
        # Inicia el juego.
        while not self.winner:
            self.print_board()
            print(f"Jugador actual: {self.current_player}")
            if self.current_player == 'X':
                move = input("Elige una casilla (1-9): ")
                self.make_move(move)
            else:
                print("Turno del oponente (O). Calculando mejor movimiento...")

                tree_root = tp.Node(self.board, 0)
                tp.generate_tree(tree_root, self.tree_depth, self.current_player)  # Agregamos el jugador actual
                tp.assign_scores(tree_root, self.current_player)  # Agregamos el jugador actual
                best_move = tp.find_best_move(tree_root, self.tree_depth, True)
                row, col = self.find_difference(self.board, best_move[0])
                move = row * 3 + col + 1
                self.make_move(str(move))

        self.print_board()
        winner = self.get_winner()
        if winner == 'Tie':
            print("¡Es un empate!")
        else:
            print(f"¡{winner} gana!")

    def find_difference(self, board1, board2):
        # Encuentra la diferencia entre dos tableros.
        for i in range(3):
            for j in range(3):
                if board1[i][j] != board2[i][j]:
                    return i, j
        return -1, -1

if __name__ == '__main__':
    game = TicTacToe()
    game.play()

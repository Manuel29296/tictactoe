class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.available_moves = [str(i) for i in range(1, 10)]  # Lista de casillas disponibles

    def make_move(self, move):
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
                self.winner = 'Empate'
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Esta casilla ya está ocupada. Elige una casilla disponible.")

    def check_winner(self, player):
        # Verificar si el jugador dado ha ganado
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
                print('-' * 9)

    def get_winner(self):
        return self.winner

    def play(self):
        while not self.winner:
            self.print_board()
            print(f"Jugador actual: {self.current_player}")
            move = input("Elige una casilla (1-9): ")
            self.make_move(move)

        self.print_board()
        winner = self.get_winner()
        if winner == 'Empate':
            print("¡Es un empate!")
        else:
            print(f"¡{winner} gana!")

if __name__ == '__main__':
    game = TicTacToe()
    game.play()

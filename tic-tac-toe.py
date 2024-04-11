class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def print_board(self):
        for row in [self.board[i:i + 3] for i in range(0, 9, 3)]:
            print(" | ".join(row))
            print("-" * 9)

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]

        if " " not in self.board:
            return "Tie"

        return None

    def minimax(self, board, depth, maximizing):
        if self.check_winner() == "X":
            return -1
        elif self.check_winner() == "O":
            return 1
        elif self.check_winner() == "Tie":
            return 0

        if maximizing:
            best_score = float("-inf")
            for i in range(9):
                if board[i] == " ":
                    board[i] = "O"
                    score = self.minimax(board, depth + 1, False)
                    board[i] = " "
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if board[i] == " ":
                    board[i] = "X"
                    score = self.minimax(board, depth + 1, True)
                    board[i] = " "
                    best_score = min(best_score, score)
            return best_score

    def get_best_move(self):
        best_score = float("-inf")
        best_move = None
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                score = self.minimax(self.board, 0, False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move


def main():
    game = TicTacToe()
    while True:
        game.print_board()
        if game.check_winner():
            print(f"Game over! {game.check_winner()} wins!")
            break
        if game.current_player == "X":
            position = int(input("Enter your move (0-8): "))
            game.make_move(position)
        else:
            ai_move = game.get_best_move()
            game.make_move(ai_move)


if __name__ == "__main__":
    main()

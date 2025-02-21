from classes import Node, State, GameTree

class TicTacToeState(State):
    def __init__(self, board=None, player='MAX', parent=None):
        """Initializes a Tic-Tac-Toe game state."""
        if board is None:
            board = [[' ' for _ in range(3)] for _ in range(3)]
        super().__init__(board, player, parent)

    def possible_actions(self):
        """Returns the empty cells where a move can be made."""
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']

    def apply_action(self, action):
        """Applies a move and returns a new state."""
        i, j = action
        new_board = [row[:] for row in self.board]  # Copy the board
        new_board[i][j] = 'X' if self.player == 'MAX' else 'O'
        next_player = 'MIN' if self.player == 'MAX' else 'MAX'
        return TicTacToeState(new_board, next_player, parent=self)

    def is_terminal(self):
        """Checks if the game is over (win or draw)."""
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return True
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] and self.board[0][j] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return True
        return all(cell != ' ' for row in self.board for cell in row)

    def evaluate(self):
        """Returns a heuristic evaluation score."""
        return 0  # To be improved for AI strategy

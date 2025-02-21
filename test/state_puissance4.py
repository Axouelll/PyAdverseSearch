from classes import Node, State, Tree

class Connect4State(State):
    def __init__(self, grid=None, player='MAX', parent=None):
        """Initializes a Connect 4 game state."""
        if grid is None:
            grid = [[' ' for _ in range(7)] for _ in range(6)]
        super().__init__(grid, player, parent)

    def possible_actions(self):
        """Returns the columns where a token can be placed."""
        return [col for col in range(7) if self.board[0][col] == ' ']

    def apply_action(self, column):
        """Drops a token in a column and returns a new state."""
        new_grid = [row[:] for row in self.board]  # Copy the grid
        for i in range(5, -1, -1):  # Find the lowest empty row
            if new_grid[i][column] == ' ':
                new_grid[i][column] = 'X' if self.player == 'MAX' else 'O'
                break
        next_player = 'MIN' if self.player == 'MAX' else 'MAX'
        return Connect4State(new_grid, next_player, parent=self)

    def is_terminal(self):
        """Checks if the game is over (win or full board)."""
        return all(self.board[0][col] != ' ' for col in range(7))

    def evaluate(self):
        """Returns a heuristic evaluation score."""
        return 0  # To be improved for AI strategy

# FILE: PyAdverseSearch/test/state_connect4.py

from ..classes.state import State
from ..classes.game import Game

ROWS = 6
COLS = 7

class Connect4State(State):
    def __init__(self, board=None, player='MAX', parent=None, game=None):
        if board is None:
            board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
        super().__init__(board, player, parent)
        self.board = board
        self.player = player
        self.parent = parent
        self.game = game

    def _apply_action(self, action):
        col = action
        new_board = [row[:] for row in self.board]
        
        # Find the lowest empty row in the selected column
        for row in reversed(range(ROWS)):
            if new_board[row][col] == ' ':
                new_board[row][col] = 'X' if self.player == 'MAX' else 'O'
                break

        next_player = 'MIN' if self.player == 'MAX' else 'MAX'
        return Connect4State(new_board, next_player, parent=self, game=self.game)

    def display(self):
        print("  " + "   ".join(str(i) for i in range(COLS)))
        print(" +" + "---+" * COLS)
        for row in self.board:
            print(" | " + " | ".join(row) + " |")
            print(" +" + "---+" * COLS)


def possible_actions(state):
    """
    Returns a list of column indices where a move can be played.
    """
    return [c for c in range(COLS) if state.board[0][c] == ' ']


def is_terminal(state):
    """
    Returns True if the game is over (win or full board).
    """
    return winner_function(state) is not None or all(state.board[0][c] != ' ' for c in range(COLS))


def utility(state):
    """
    Returns 1000 if MAX wins, -1000 if MIN wins, 0 otherwise.
    """
    winner = winner_function(state)
    if winner == 'MAX':
        return 1000
    elif winner == 'MIN':
        return -1000
    return 0


def heuristic(state):
    """
    Heuristic based on number of 3-in-a-rows for each player.
    """
    def count_patterns(symbol, count_required):
        count = 0
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for r in range(ROWS):
            for c in range(COLS):
                if state.board[r][c] != symbol:
                    continue
                for dr, dc in directions:
                    streak = 0
                    for i in range(count_required):
                        nr, nc = r + dr*i, c + dc*i
                        if 0 <= nr < ROWS and 0 <= nc < COLS and state.board[nr][nc] == symbol:
                            streak += 1
                        else:
                            break
                    if streak == count_required:
                        count += 1
        return count

    x_threes = count_patterns('X', 3)
    o_threes = count_patterns('O', 3)

    return 0.5 * x_threes - 0.5 * o_threes


def winner_function(state):
    """
    Returns 'MAX' or 'MIN' if someone won, otherwise None.
    """
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # down, right, diag-down-right, diag-down-left
    for r in range(ROWS):
        for c in range(COLS):
            symbol = state.board[r][c]
            if symbol == ' ':
                continue
            for dr, dc in directions:
                win = True
                for i in range(1, 4):
                    nr, nc = r + dr*i, c + dc*i
                    if not (0 <= nr < ROWS and 0 <= nc < COLS) or state.board[nr][nc] != symbol:
                        win = False
                        break
                if win:
                    return 'MAX' if symbol == 'X' else 'MIN'
    return None


def generate_connect4_game(isMaxStartingParameter=True):
    initial_state = Connect4State()
    game = Game(
        initial_state=initial_state,
        possible_actions=possible_actions,
        is_terminal=is_terminal,
        winner_function=winner_function,
        utility=utility,
        heuristic=heuristic,
        isMaxStarting=isMaxStartingParameter
    )
    initial_state.game = game
    return game

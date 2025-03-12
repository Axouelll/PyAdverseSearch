from PyAdverseSearch.classes import Node, State, GameTree

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

    
    def evaluate(state):
        """
        Évalue l'état du Tic Tac Toe en comptant les alignements potentiels.
        On considère 'X' pour MAX et 'O' pour MIN.
        """
        print("Évaluation de l'état reçu :")
        print("Plateau actuel :")
        for row in state.board:
            print(row)
        print("Joueur actuel :", state.player)
        
        board = state.board
        ROWS = len(board)
        COLS = len(board[0])
        score = 0

        def score_line(count, spaces):
            # Pour Tic Tac Toe, on peut fixer des valeurs par exemple :
            if count == 3:
                return 100  # victoire
            elif count == 2 and spaces == 1:
                return 10
            elif count == 1 and spaces == 2:
                return 1
            return 0

        # Lignes et colonnes
        for i in range(ROWS):
            # Ligne i
            line = board[i]
            if line.count('X') > 0 or line.count('O') > 0:
                if 'X' in line and 'O' not in line:
                    count = line.count('X')
                    spaces = line.count(' ')
                    score += score_line(count, spaces)
                elif 'O' in line and 'X' not in line:
                    count = line.count('O')
                    spaces = line.count(' ')
                    score -= score_line(count, spaces)
            # Colonne i
            col = [board[r][i] for r in range(ROWS)]
            if col.count('X') > 0 or col.count('O') > 0:
                if 'X' in col and 'O' not in col:
                    count = col.count('X')
                    spaces = col.count(' ')
                    score += score_line(count, spaces)
                elif 'O' in col and 'X' not in col:
                    count = col.count('O')
                    spaces = col.count(' ')
                    score -= score_line(count, spaces)

        # Diagonales
        diag1 = [board[i][i] for i in range(ROWS)]
        diag2 = [board[i][ROWS-1-i] for i in range(ROWS)]
        for diag in [diag1, diag2]:
            if diag.count('X') > 0 or diag.count('O') > 0:
                if 'X' in diag and 'O' not in diag:
                    count = diag.count('X')
                    spaces = diag.count(' ')
                    score += score_line(count, spaces)
                elif 'O' in diag and 'X' not in diag:
                    count = diag.count('O')
                    spaces = diag.count(' ')
                    score -= score_line(count, spaces)

        return score

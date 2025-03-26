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
        print("----------------------------------------------------")
        print("Évaluation de l'état reçu :")
        print("Plateau actuel :")
        for row in state.board:
            print(row)
        print("Joueur actuel :", state.player)
        print("-------------------------------------------------------")
        
        """
        Évalue l'état du Tic Tac Toe (morpion) en une seule fonction.

        On suppose que :
        - state.board est une liste de listes représentant le plateau (3×3)
        - Chaque case contient 'X' (pour MAX), 'O' (pour MIN) ou ' ' (case vide).

        Si l'état est terminal, la fonction renvoie :
        1  si MAX (X) a gagné,
        -1  si MIN (O) a gagné,
        0  en cas d'égalité.

        Sinon, l'évaluation heuristique se base sur le nombre de lignes (lignes, colonnes, diagonales)
        "ouvertes" (c'est-à-dire sans présence simultanée de X et O) et attribue un bonus
        plus important lorsque deux symboles sont déjà alignés.
        """
        board = state.board

        # Fonction interne pour vérifier si le plateau est plein
        def is_full(board):
            for row in board:
                if ' ' in row:
                    return False
            return True

        # Fonction interne pour déterminer le gagnant
        def get_winner_morpion(board):
            # Vérification des lignes
            for row in board:
                if row[0] == row[1] == row[2] and row[0] != ' ':
                    return row[0]
            # Vérification des colonnes
            for j in range(3):
                if board[0][j] == board[1][j] == board[2][j] and board[0][j] != ' ':
                    return board[0][j]
            # Vérification des diagonales
            if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
                return board[0][0]
            if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
                return board[0][2]
            return None

        # Vérifier si l'état est terminal
        winner = get_winner_morpion(board)
        if winner == 'X':
            return 1
        elif winner == 'O':
            return -1
        elif is_full(board):
            return 0

        # Si l'état n'est pas terminal, on calcule une évaluation heuristique
        score = 0
        lines = []

        # Rassembler toutes les lignes
        # Lignes
        for row in board:
            lines.append(row)
        # Colonnes
        for j in range(3):
            col = [board[i][j] for i in range(3)]
            lines.append(col)
        # Diagonales
        diag1 = [board[i][i] for i in range(3)]
        diag2 = [board[i][2 - i] for i in range(3)]
        lines.append(diag1)
        lines.append(diag2)

        # Évaluer chaque ligne non bloquée
        for line in lines:
            # Si la ligne contient à la fois 'X' et 'O', elle est bloquée
            if 'X' in line and 'O' in line:
                continue

            # Pour MAX ('X')
            if 'X' in line:
                count = line.count('X')
                if count == 1:
                    score += 1
                elif count == 2:
                    score += 10

            # Pour MIN ('O')
            if 'O' in line:
                count = line.count('O')
                if count == 1:
                    score -= 1
                elif count == 2:
                    score -= 10

        return score
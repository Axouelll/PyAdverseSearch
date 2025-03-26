from PyAdverseSearch.classes import Node, State, GameTree


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

    def evaluate(state):
            print("Évaluation de l'état reçu :")
            print("Plateau actuel :")
            for row in state.board:
                print(row)
            print("Joueur actuel :", state.player)
            
            """
            Évalue l'état du jeu en s'inspirant des méthodes d'évaluation aux échecs.
            
            Si l'état est terminal, on renvoie :
            1  si MAX a gagné,
            0  en cas d'égalité,
            -1  si MIN a gagné.
            
            Sinon, on calcule une évaluation heuristique en combinant :
            - Un score "matériel" basé sur la différence de jetons.
            - Un bonus positionnel (par exemple, contrôler le centre du plateau).
            """
            # Vérifier si l'état est terminal et renvoyer la valeur appropriée.
            if state.is_terminal():
                winner = state.game.get_winner()
                if winner == 'MAX':
                    return 1
                elif winner == 'MIN':
                    return -1
                else:
                    return 0

            # Évaluation non terminale (inspirée des échecs)
            board = state.board
            # "Matériel" : différence du nombre de jetons
            max_tokens = sum(row.count('X') for row in board)
            min_tokens = sum(row.count('O') for row in board)
            material_score = max_tokens - min_tokens  # avantage matériel pour MAX

            # Bonus positionnel : par exemple, occuper le centre du plateau
            positional_score = 0
            ROWS = len(board)
            COLS = len(board[0])
            center_row = ROWS // 2
            center_col = COLS // 2
            center_value = board[center_row][center_col]
            if center_value == 'X':
                positional_score += 1
            elif center_value == 'O':
                positional_score -= 1

            # Combiner les scores avec des coefficients (ces coefficients peuvent être ajustés)
            # Ici, on attribue 0.1 pour l'aspect matériel et 0.05 pour le bonus positionnel.
            score = material_score * 0.1 + positional_score * 0.05

            # Pour une perspective relative : si c'est le tour de MIN, on inverse le score.
            if state.player == 'MIN':
                score = -score

            return score

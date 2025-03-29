# FILE: test_tree.py
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from state_tictactoe import TicTacToeState
from classes.game import Game
from classes.minimax import Minimax
from test import generate_tictactoe_game


def test_best_move_tictactoe():
    print("\n🔵 TESTING BEST MOVE FOR TIC TAC TOE 🔵")
    
    # Supposez que votre Game est instancié avec toutes les fonctions nécessaires.
    # Par exemple, vous devez définir possible_actions, is_terminal, utility, et heuristic.
    # Ici, nous supposons que TicTacToeState a déjà une référence à l'instance Game dans self.game.
    initial_state = TicTacToeState()

    # Créez une instance de l'algorithme Minimax.
    # Ici, on définit par exemple une profondeur maximale de 4.
    algo = Minimax(game=initial_state.game, max_depth=4)

    # Obtenez le meilleur coup à partir de l'état initial
    best_move = algo.choose_best_move(initial_state)
    print("Le meilleur coup à jouer est :", best_move)

from test import generate_tictactoe_game

if __name__ == "__main__":
    game = generate_tictactoe_game()
    game.state.display()
# FILE: test_tree.py

from test.state_tictactoe import TicTacToeState
from classes import GameTree

def test_tic_tac_toe_tree():
    print("\n🔵 TESTING FULL TIC-TAC-TOE TREE WITH DEPTH INFO 🔵")
    initial_state = TicTacToeState()
    game_tree = GameTree(initial_state)  # Full game tree generation
    game_tree.display()

# Run test
test_tic_tac_toe_tree()

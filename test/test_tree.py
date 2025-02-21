# FILE: test_tree.py

from state_tictactoe import TicTacToeState
from tree import GameTree

def test_tic_tac_toe_tree():
    print("\n🔵 TESTING FULL TIC-TAC-TOE TREE 🔵")
    initial_state = TicTacToeState()
    game_tree = GameTree(initial_state)  # Full game tree (no depth limit)
    game_tree.display()

# Run test
test_tic_tac_toe_tree()

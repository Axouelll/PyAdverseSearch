# FILE: test_tree.py

# 1) Importer la classe TicTacToeState depuis le fichier state_tictactoe.py
from PyAdverseSearch.test.state_tictactoe import TicTacToeState

# 2) Importer GameTree (ou Node, State) depuis le dossier classes
from PyAdverseSearch.classes.tree import GameTree

def test_tic_tac_toe_tree():
    print("\n🔵 TESTING FULL TIC-TAC-TOE TREE 🔵")
    initial_state = TicTacToeState()  # On crée un état initial
    game_tree = GameTree(initial_state)  # On crée l'arbre de jeu
    game_tree.display()

if __name__ == "__main__":
    test_tic_tac_toe_tree()

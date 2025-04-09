# FILE: PyAdverseSearch/test/test_tree.py

from .state_tictactoe import generate_tictactoe_game
from ..classes.tree import GameTree

def test_tic_tac_toe_tree():
    print("\n🔵 TESTING FULL TIC-TAC-TOE TREE 🔵")
    # Par défaut, ne construit pas l'arbre dans Game
    game = generate_tictactoe_game()  
    game.state.display()

    # Si vous souhaitez construire l'arbre, vous pouvez soit :
    # a) Créer l'arbre directement
    tree = GameTree(game.state)
    tree.display()
    # b) Ou, lors de l'initialisation du Game, passer build_tree=True (si generate_tictactoe_game() est adapté)

if __name__ == "__main__":
    test_tic_tac_toe_tree() 
# FILE: PyAdverseSearch/test/test_tree.py

from .state_tictactoe import generate_tictactoe_game
from ..classes.tree import GameTree

def test_tic_tac_toe_tree():
    print("\n🔵 TESTING FULL TIC-TAC-TOE TREE 🔵")
    
    # Crée le jeu via la fonction qui configure tout
    game = generate_tictactoe_game()  
    # Affiche l'état initial et sa référence au game
    print("Etat initial du jeu (board):")
    game.state.display()
    if game.state.game is None:
        print("ERREUR : game.state.game est None")
    else:
        print("OK : game.state.game est bien initialisé.")
    
    # Construire l'arbre de jeu à partir de l'état initial
    game_tree = GameTree(game.state)
    print("\nAffichage de l'arbre de jeu :")
    game_tree.display()

if __name__ == "__main__":
    test_tic_tac_toe_tree()

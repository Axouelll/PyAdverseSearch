# FILE: PyAdverseSearch/test/test_full_game_next_move.py

from PyAdverseSearch.classes.node import Node
from PyAdverseSearch.classes.minimax import Minimax
from .state_tictactoe import generate_tictactoe_game


def test_full_game_next_move():
    """
    Simule une partie complète de Tic-Tac-Toe en utilisant next_move() de Minimax.
    Affiche chaque étape et annonce le gagnant ou match nul.
    """
    print("🔵 TESTING FULL GAME VIA next_move() 🔵")
    game = generate_tictactoe_game()
    state = game.state

    # 1. Construire le nœud racine et générer ses enfants
    root = Node(state, parent=None, depth=0)
    root._expand()

    # 2. Instancier Minimax
    minimax = Minimax(game=game, max_depth=6)

    current = root
    step = 1
    # 3. Boucle de jeu
    while True:
        print(f"\n--- Move {step} | Player: {current.state.player} ---")
        current.state.display()

        # Si terminal, fin
        if current.is_terminal():
            print("État terminal atteint.")
            break

        # Choisir le prochain nœud via next_move
        next_node = minimax.next_move(current)
        if next_node is None:
            print("Aucun coup possible.")
            break

        # Passer au nœud suivant et étendre
        current = next_node
        current._expand()
        step += 1

    # 4. Afficher résultat final
    print("\n--- Final Board ---")
    current.state.display()
    winner = game.get_winner()
    print(f"Winner: {winner if winner else 'Draw'}")


if __name__ == "__main__":
    test_full_game_next_move()

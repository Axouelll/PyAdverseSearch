# FILE: PyAdverseSearch/test/test_minimax.py

from .state_tictactoe import generate_tictactoe_game
from PyAdverseSearch.classes.algorithm import choose_best_move


def test_minimax_via_algorithm_selector():
    print("🔵 TESTING MINIMAX VIA ALGORITHM SELECTOR (DEBUG) 🔵")
    game = generate_tictactoe_game()
    state = game.state
    print("Plateau initial :")
    print(f"Player: {state.player}")
    state.display()

    move_count = 10  # Nombre de coups à jouer
    for i in range(move_count):
        print(f"\n--- Coup {i+1} | Player: {state.player} ---")


        # Choisir le meilleur coup via Minimax
        best_state = choose_best_move('minimax', game, state, max_depth=9)
        if best_state is None:
            print("Aucun coup trouvé (état terminal ou erreur).")
            break

        print("Coup choisi :")
        print(f"Player: {best_state.player}")
        best_state.display()
        state = best_state

        if state._is_terminal():
            print("État terminal atteint.")
            break

        input("Appuie sur Entrée pour continuer...")



if __name__ == "__main__":
    test_minimax_via_algorithm_selector()

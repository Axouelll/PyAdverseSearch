# FILE: PyAdverseSearch/test/test_minimax.py

from .state_tictactoe import generate_tictactoe_game
from PyAdverseSearch.classes.algorithm import choose_best_move

def test_minimax_via_algorithm_selector():
    print("\n🔵 TESTING MINIMAX VIA ALGORITHM SELECTOR 🔵")
    game = generate_tictactoe_game()
    state = game.state
    print("Plateau initial :")
    state.display()

    move_count = 10  # Nombre de coups à jouer
    for i in range(move_count):
        print(f"\n--- Coup {i+1} ---")
        # On utilise l'algorithme pour obtenir le meilleur état à partir de l'état courant.
        best_state = choose_best_move('minimax', game, state, max_depth=4)
        if best_state is None:
            print("Aucun coup trouvé (état terminal ou erreur).")
            break

        # Mettre à jour l'état courant
        state = best_state
        state.display()

        # Si l'état est terminal, on arrête la séquence
        if state._is_terminal():
            print("État terminal atteint.")
            break

if __name__ == "__main__":
    test_minimax_via_algorithm_selector()

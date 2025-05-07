# FILE: PyAdverseSearch/test/test_minimax.py
# python -m PyAdverseSearch.test.test_minimax


from .state_tictactoe import generate_tictactoe_game
from PyAdverseSearch.classes.algorithm import choose_best_move


def test_minimax_via_algorithm_selector():
    print("TESTING MINIMAX VIA ALGORITHM SELECTOR (DEBUG)")
    game = generate_tictactoe_game()
    state = game.state
    print("Initial Board :")
    state.display()

    move_count = 10
    for i in range(move_count):
        print(f"\n--- Coup {i+1} | Player: {state.player} ---")


        # chooses the best move using Minimax
        best_state = choose_best_move('minimax', game, state, max_depth=4)
        if best_state is None:
            print("No move found (final state or a mistake...).")
            break

        print("Picked move :")
        best_state.display()
        state = best_state

        if state._is_terminal():
            print("Final state reached.")
            break

        input("Press enter to continue...")



if __name__ == "__main__":
    test_minimax_via_algorithm_selector()














"""def test_minimax_via_algorithm_selector():
    print("TESTING MINIMAX VIA ALGORITHM SELECTOR (DEBUG)")
    game = generate_tictactoe_game()
    state = game.state
    print("Initial Board :")
    state.display()

    move_count = 10
    for i in range(move_count):
        print(f"\n--- Coup {i+1} | Player: {state.player} ---")


        # chooses the best move using Minimax
        best_state = choose_best_move('minimax', game, state, max_depth=4)
        if best_state is None:
            print("No move found (final state or a mistake...).")
            break

        print("Picked move :")
        best_state.display()
        state = best_state

        if state._is_terminal():
            print("Final state reached.")
            break

        input("Press enter to continue...")"""
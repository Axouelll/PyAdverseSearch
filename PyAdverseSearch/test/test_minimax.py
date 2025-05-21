# FILE: PyAdverseSearch/test/test_minimax.py
# commande a execute pour tester : python -m PyAdverseSearch.test.test_minimax


from .state_tictactoe import generate_tictactoe_game
from .state_connect4 import generate_connect4_game
from PyAdverseSearch.classes.algorithm import choose_best_move


"""

TIC TAC TOE

"""
def test_minimax_via_algorithm_selector_human_player_tictactoe():
    print("TESTING MINIMAX VIA ALGORITHM SELECTOR WITH A HUMAN PLAYER AS MIN (DEBUG)")
    maxStarting = input("Would you like to start  (y/n) ?")
    if maxStarting == 'y' : maxStarting = False
    elif maxStarting == 'n' : maxStarting = True
    else : 
        print("Answer didn't match 'y' or 'n', program ended...")
        return
    game = generate_tictactoe_game(maxStarting)
    state = game.state
    print("Initial Board :")
    state.display()

    move_count = 10
    for i in range(move_count):
        current_player_is_max = (i % 2 == 0) if maxStarting else (i % 2 != 0)
        print(f"\n--- Move {i+1} | {"Max's" if current_player_is_max else 'Your'} turn ---")

        #max is playing
        if current_player_is_max :
            # chooses the best move using Minimax
            best_state = choose_best_move('minimax', game, state, max_depth=9)
            if best_state is None:
                print("No move found (final state or a mistake...).")
                break

            print("Picked move :")
            best_state.display()
            state = best_state

        #min / the player is playing
        else :
            print("Here are all the possible moves you could do :")
            possible_moves = state._generate_successors()
            for j in range (len(possible_moves)):
                print("Option ", j+1, " :")
                possible_moves[j].display()
            while True:
                user_input = input(f"Which one do you wish to do? (number between 1 and {len(possible_moves)}): ")
                
                try:
                    choice = int(user_input)
                    if 1 <= choice <= len(possible_moves):
                        state = possible_moves[choice - 1]
                        state.display()
                        break
                    else:
                        print(f"Invalid input! Please enter a number between 1 and {len(possible_moves)}.")
                
                except ValueError:
                    print("Invalid input! Please enter a numeric value.")
            
        # printing who won
        if state._is_terminal():
            print("Final state reached.")
            winner = game.winner_function(state)
            if not winner : print("It's a draw")
            else : print("Winner is : " + winner)
            break

        input("Press enter to continue...")

def test_minimax_via_algorithm_selector_tictactoe():
    print("TESTING MINIMAX VIA ALGORITHM SELECTOR (DEBUG)")
    game = generate_tictactoe_game()
    state = game.state
    print("Initial Board :")
    state.display()

    move_count = 10
    for i in range(move_count):
        print(f"\n--- Coup {i+1} | Player: {state.player} ---")


        # chooses the best move using Minimax
        best_state = choose_best_move('minimax', game, state, max_depth=1)
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

"""

CONNECT 4

"""
def test_minimax_via_algorithm_selector_human_player_connect4():
    print("TESTING MINIMAX VIA ALGORITHM SELECTOR WITH A HUMAN PLAYER AS MIN (DEBUG)")
    maxStarting = input("Would you like to start  (y/n) ?")
    if maxStarting == 'y' : maxStarting = False
    elif maxStarting == 'n' : maxStarting = True
    else : 
        print("Answer didn't match 'y' or 'n', program ended...")
        return
    game = generate_connect4_game(maxStarting)
    state = game.state
    print("Initial Board :")
    state.display()

    move_count = 100
    for i in range(move_count):
        current_player_is_max = (i % 2 == 0) if maxStarting else (i % 2 != 0)
        print(f"\n--- Move {i+1} | {"Max's" if current_player_is_max else 'Your'} turn ---")

        #max is playing
        if current_player_is_max :
            # chooses the best move using Minimax
            best_state = choose_best_move('minimax', game, state, max_depth=7)
            if best_state is None:
                print("No move found (final state or a mistake...).")
                break

            print("Picked move :")
            best_state.display()
            state = best_state

        #min / the player is playing
        else :
            print("Here are all the possible moves you could do :")
            possible_moves = state._generate_successors()
            for j in range (len(possible_moves)):
                print("Option ", j+1, " :")
                possible_moves[j].display()
            while True:
                user_input = input(f"Which one do you wish to do? (number between 1 and {len(possible_moves)}): ")
                
                try:
                    choice = int(user_input)
                    if 1 <= choice <= len(possible_moves):
                        state = possible_moves[choice - 1]
                        state.display()
                        break
                    else:
                        print(f"Invalid input! Please enter a number between 1 and {len(possible_moves)}.")
                
                except ValueError:
                    print("Invalid input! Please enter a numeric value.")
            
        # printing who won
        if state._is_terminal():
            print("Final state reached.")
            winner = game.winner_function(state)
            if not winner : print("It's a draw")
            else : print("Winner is : " + winner)
            break

        input("Press enter to continue...")

if __name__ == "__main__":
    test_minimax_via_algorithm_selector_human_player_connect4()
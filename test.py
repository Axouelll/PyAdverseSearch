from state_tictactoe import TicTacToeState
from state_puissance4 import Connect4State

def test_tic_tac_toe():
    print("\n🔵 TEST TIC-TAC-TOE 🔵")
    ttt_state = TicTacToeState()
    ttt_state.display()
    print("Possible actions:", ttt_state.possible_actions())

    successors = ttt_state.generate_successors()
    print(f"\nNumber of successors generated: {len(successors)}")
    for i, succ in enumerate(successors):  # Show first 3 successors
        print(f"\nSuccessor {i+1}: Player {succ.player}")
        succ.display()

def test_connect4():
    print("\n🟡 TEST CONNECT 4 🟡")
    c4_state = Connect4State()
    c4_state.display()
    print("Possible actions:", c4_state.possible_actions())

    successors = c4_state.generate_successors()
    print(f"\nNumber of successors generated: {len(successors)}")
    for i, succ in enumerate(successors):  # Show first 3 successors
        print(f"\nSuccessor {i+1}: Player {succ.player}")
        succ.display()

# Run tests
test_tic_tac_toe()
test_connect4()

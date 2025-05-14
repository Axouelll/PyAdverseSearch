from PyAdverseSearch.test.state_tictactoe import generate_tictactoe_game
from PyAdverseSearch.classes.algorithm import choose_best_move

# Génère une partie de Tic-Tac-Toe
game = generate_tictactoe_game()
state = game.state

# On suppose que le joueur qui commence est le joueur MAX
max_player = state.player

# Boucle de jeu
while not game.is_terminal(state):
    print("\nÉtat actuel :")
    state.display()

    best = choose_best_move('montecarlo', game, state, max_iterations=2000)
    print("\nCoup joué :")
    best.display()

    state = best

# État final
print("\nPartie terminée. Résultat final :")
print("Valeur retournée par utility(state) :", game.utility(state))
state.display()

# Déterminer le résultat via game.utility (qui retourne 1, 0, ou -1)
result = game.utility(state)
if result == 1000:
    print("Joueur MAX (X) gagne.")
elif result == -1000:
    print("Joueur MIN (O) gagne.")
else:
    print("Match nul.")

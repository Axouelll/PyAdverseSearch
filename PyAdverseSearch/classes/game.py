# FILE: game.py
from PyAdverseSearch.classes.tree import GameTree


class Game:
    """
    The Game class is used by library users.
    It provides other classes with user-defined functions.
    They must initialize the game class with the initial state of the game,
    the rules of the game, the final state of the game and the function
    that defines who is the winner.
    """

    def __init__(self, initial_state=None, possible_actions=None, is_terminal=None, winner_function=None, utility=None, heuristic=None, isMaxStarting=True):
        # param initial_state: The initial state of the game.
        # param possible_actions: The function that defines possible actions from a given state.
        # param is_terminal: The function that checks if the game has reached a final state (ended).
        # param winner_function: The function that determines the winner once the game is finished.
        # param utility: evaluates a terminal state to determine the final outcome of the game.
        # param heuristic: function to evaluate non-terminal states (returns a numerical value)
       
        self.state = initial_state
        self.possible_actions = possible_actions
        self.is_terminal = is_terminal
        self.winner_function = winner_function
        self.utility = utility
        self.heuristic = heuristic
        self.isMaxStarting = isMaxStarting
        print("[DEBUG] Dans Game.__init__: Avant affectation, initial_state.game =", getattr(self.state, "game", None))
        if self.state is not None:
            self.state.game = self
        print("[DEBUG] Dans Game.__init__: Après affectation, initial_state.game =", self.state.game)

    # Rules
    def game_possible_actions(self, state):
        # Returns the possible actions from the state given through the parameter.
        return self.possible_actions(state)

    # End game
    def game_is_terminal(self, state):
        # Checks if the game is over using the is_terminal function on the state given through the parameter.
        return self.is_terminal(state)
    
    def game_utility(self, state):
        # returns a numerical value based on if the game has been lost or won (or if it's a draw) by the player 'Max'
        # only call this function if the state is terminal (see game_is_terminal)
        return self.utility(state)

    def game_heuristic(self, state):
        return self.heuristic(state)

    def get_winner(self):
        # Returns the winner of the game if it's finished, otherwise None.
        return self.winner_function(self.state)

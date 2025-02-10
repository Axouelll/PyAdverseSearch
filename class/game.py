class Game:

    """
    The Game class is used by library users.
    It provides other classes with user-defined functions.
    They must initialize the game class with the initial state of the game,
    the rules of the game, the final state of the game and the function
    that defines who is the winner.
    """

    """Constructor"""
    def __init__(self, initial_state = None, rules_function = None, final_state_function = None, winner_function = None):

        # param initial_state: The initial state of the game.
        # param rules_function: The function that defines possible actions from a given state.
        # param final_state_function: The function that checks if the game has reached a final state (ended).
        # param winner_function: The function that determines the winner once the game is finished.

        self.state = initial_state
        self.rules_function = rules_function
        self.final_state_function = final_state_function
        self.winner_function = winner_function

    """Rules"""
    def get_possible_actions(self):
        # Returns the possible actions from the current game state.
        return self.rules_function(self.state)

    """End game"""
    def is_game_over(self):
        # Checks if the game is over using the final_state_function.
        return self.final_state_function(self.state)

    def get_winner(self):
        # Returns the winner of the game if it's finished, otherwise None.
        return self.winner_function(self.state)


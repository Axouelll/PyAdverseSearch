# FILE: state.py

from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, board, player, parent=None, game=None):
        """
        Generic class for all discrete-state games.

        :param board: Representation of the game state.
        :param player: Current player ('MAX' or 'MIN').
        :param parent: Previous state (useful for the search tree).
        :param game: Reference to the instance of the Game class that's being used for this state,
                     used to get access to the is_terminal function given by the user
        """
        self.board = board
        self.player = player
        self.parent = parent
        self.value = None  # (optionnel) peut servir pour un stockage temporaire
        self.game = game  # référence au Game pour accéder aux fonctions définies par l'utilisateur


    def _possible_actions(self):
        """
        Returns a list of possible actions from this state.
        This list is returned by the function given by the user to the Game class.
        """
        return self.game.game_possible_actions(self)

    def _is_terminal(self):
        """
        Checks if the state is a terminal state (game over)
        thanks to the dedicated function defined by the user through the Game class.
        """
        return self.game.game_is_terminal(self)

    def _utility(self):
        """
        Calls the utility function given by the user to the Game class.
        """
        return self.game.game_utility(self)

    def _evaluate(self):
        """
        Returns a heuristic evaluation of the state.
        This implementation delegates the call to the Game's game_heuristic function,
        following the same pattern as for possible_actions and is_terminal.
        """
        return self.game.game_heuristic(self)

#?applyaction
    def _generate_successors(self):
        """Generates and returns all possible successor states."""
        return [self.apply_action(action) for action in self._possible_actions()]

    def display(self):
        """Displays the current game state."""
        for row in self.board:
            print('|'.join(row))
        print("\n")

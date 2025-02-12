from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, board, player, parent=None):
        """
        Generic class for all discrete-state games.

        :param board: Representation of the game state.
        :param player: Current player ('MAX' or 'MIN').
        :param parent: Previous state (useful for the search tree).
        """
        self.board = board
        self.player = player
        self.parent = parent
        self.value = None  # Heuristic score (to be calculated later)

    @abstractmethod
    def possible_actions(self):
        """Returns a list of possible actions from this state."""
        pass

    @abstractmethod
    def apply_action(self, action):
        """Applies an action and returns a new state."""
        pass

    @abstractmethod
    def is_terminal(self):
        """Checks if the state is a terminal state (game over)."""
        pass

    @abstractmethod
    def evaluate(self):
        """Calculates and returns the heuristic value of the state."""
        pass

    def generate_successors(self):
        """Generates and returns all possible successor states."""
        return [self.apply_action(action) for action in self.possible_actions()]

    def display(self):
        """Displays the current game state."""
        for row in self.board:
            print('|'.join(row))
        print("\n")

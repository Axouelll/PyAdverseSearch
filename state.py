from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, board, player, parent=None, game=None):
        """
        Generic class for all discrete-state games.

        :param board: Representation of the game state.
        :param player: Current player ('MAX' or 'MIN').
        :param parent: Previous state (useful for the search tree).
        :param game: Reference to the instance of the Game class that's begin used for this state
                        used to get access to the is_terminal function given by the user
        """
        self.board = board
        self.player = player
        self.parent = parent
        self.value = None  # Heuristic score (to be calculated later)
        self.game = game #reference to the Game that's being played, used to get the utility function

    
    def possible_actions(self):
        """
        Returns a list of possible actions from this state, 
        this list is returned by the function given by the user to the Game class
        """
        return self.game.game_possible_actions(self)

    
    def is_terminal(self):
        """
        Checks if the state is a terminal state (game over)
        thanks to the dedicated function defined by the user through the Game class
        """
        return self.game.game_is_terminal(self)

    @abstractmethod
    def utility(self):
        pass
    
    @abstractmethod
    def apply_action(self, action):
        """Applies an action and returns a new state."""
        pass

    def generate_successors(self):
        """Generates and returns all possible successor states."""
        return [self.apply_action(action) for action in self.possible_actions()]

    def display(self):
        """Displays the current game state."""
        for row in self.board:
            print('|'.join(row))
        print("\n")

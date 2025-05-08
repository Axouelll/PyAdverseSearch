# FILE: PyAdverseSearch/classes/minimax.py

import time
from PyAdverseSearch.classes.algorithm import SearchAlgorithm
from PyAdverseSearch.classes.node import Node

class Minimax(SearchAlgorithm):
    def __init__(self, game=None, max_depth=9, max_time_seconds=None):
        #verifying parameters
        if max_depth is not None and (max_depth <= 0 or not isinstance(max_depth, int)):
            print("Error: max_depth must be a positive integer")
            return
        if max_time_seconds is not None and (max_time_seconds <= 0 or not isinstance(max_time_seconds, (int, float))):
            print("Error: max_time_seconds must be a positive number")
            return

        self.game = game
        self.max_depth = max_depth
        self.max_time = max_time_seconds
        self.start_time = None


    def choose_best_move(self, state):
        """
        Selects the best move for the current player (MAX or MIN),
        prioritizing terminal states (utility × 1000), then calling
        min_value or max_value depending on the player, and comparing scores.

        """
        is_max = (state.player == "MAX")


        best_score = -float('inf') if is_max else float('inf')
        best_state = None

        for action in state._possible_actions():
            child = state._apply_action(action)

            # final state → strong score
            if self.game.game_is_terminal(child):
                util = self.game.game_utility(child)
                score = util * 1000
            else:
                # non-terminal → we call MAX or MIN accordingly
                if is_max:
                    score = self.min_value(child, self.max_depth - 1)
                else:
                    score = self.max_value(child, self.max_depth - 1)

            # choosing best child
            if (is_max and score > best_score) or (not is_max and score < best_score):
                best_score = score
                best_state = child

        return best_state

    def max_value(self, state, depth):
        """
        Returns the highest value (utility or heuristic) for MAX.
        """
        # final state
        if self.game.game_is_terminal(state):
            return self.game.game_utility(state)
        # Depth cutoff: return heuristic
        if depth == 0:
            return self.game.game_heuristic(state)

        v = -float('inf')
        for action in state._possible_actions():
            child = state._apply_action(action)
            v = max(v, self.min_value(child, depth - 1))
        return v

    def min_value(self, state, depth):
        """
        Returns the smallest value (utility or heuristic) for MIN.
        """
        # Terminal state
        if self.game.game_is_terminal(state):
            return self.game.game_utility(state)
        # Depth cutoff: return heuristic
        if depth == 0:
            return self.game.game_heuristic(state)

        v = float('inf')
        for action in state._possible_actions():
            child = state._apply_action(action)
            v = min(v, self.max_value(child, depth - 1))
        return v


    def time_limit_reached(self):
        if self.max_time is None:
            return False
        return (time.time() - self.start_time) >= self.max_time

    # If the node is terminal, it directly returns its utility value.
    # Otherwise, it recursively calculates utilities of all children.
    def default_utility(self, node):
        if node.is_terminal():
            return node.state._utility()

        # If there's no children, return the heuristic evaluation of the node.
        if not node.children:
            return node.valuation

        if node.state.player == "MAX":
            return max(self.default_utility(child) for child in node.children)
        else:  # MIN
            return min(self.default_utility(child) for child in node.children)


    def next_move(self, node):
        if not node.children:
            return None

        # evaluates each children
        child_utils = [(child, self.default_utility(child)) for child in node.children]
        if node.state.player == "MAX":
            best_child = max(child_utils, key=lambda x: x[1])[0]
        else:
            best_child = min(child_utils, key=lambda x: x[1])[0]
        return best_child

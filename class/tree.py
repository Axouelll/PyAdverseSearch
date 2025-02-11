"""Importing the necessary classes"""
from node import Node
from state import State

class Tree:
    """Constructor"""
    def __init__(self, initial_state, max_depth):
        # initial_state : the first state of the game
        # max_depth : the maximum depth we're allowing the tree to go to
        
        self.root = Node(state = initial_state)
        self.max_depth = max_depth

    """Fill the search tree with every state possible in the game"""
    def generate_tree(self):
        #todo
        return 0
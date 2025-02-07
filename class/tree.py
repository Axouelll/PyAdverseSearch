"""Importing the necessary classes"""
from node import Node
from state import State

class Tree:
    """Constructor"""
    def __init__(self, initial_state):
        # initial_state : the first state of the game
        self.root = Node(state = initial_state)

    """Fill the search tree with every state possible in the game"""
    # max_depth : the maximum depth we're allowing the tree to go to
    def generate_tree(self , max_depth):
        #todo
        return 0
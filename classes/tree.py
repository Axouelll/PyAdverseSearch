# FILE: tree.py

from classes import Node

class GameTree:

    def __init__(self, initial_state, max_depth=float('inf')):
        """
        Constructs a full game tree starting from an initial state.

        :param initial_state: The starting state of the game.
        """
        self.root = Node(initial_state, max_depth)
        self.node_count = 0
        self.leaf = 0
        self.max_depth = max_depth
        self.build_tree(self.root)

    def build_tree(self, node):
            """Recursively expands the tree until all terminal states are reached."""
            if node.is_terminal():
                self.leaf += 1
                return  # Stop expanding if this is a terminal state
        
            elif (node.depth < self.max_depth): 
                node.expand()  # Generate successor nodes
                self.node_count += 1
                for child in node.children:
                    self.build_tree(child)  # Recursively expand the tree

    def display(self):
        print (self.node_count)
        print (self.leaf)
                

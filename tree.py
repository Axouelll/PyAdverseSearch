# FILE: tree.py

class TreeNode:
    def __init__(self, state, parent=None):
        """
        Represents a node in the game tree.

        :param state: The game state at this node.
        :param parent: The parent node in the tree (None if root).
        """
        self.state = state
        self.parent = parent
        self.children = []  # List of successor nodes

    def expand(self):
        """Generates all possible successor states and adds them as children."""
        for action in self.state.possible_actions():
            new_state = self.state.apply_action(action)
            self.children.append(TreeNode(new_state, parent=self))

    def is_terminal(self):
        """Returns True if this node represents a terminal state."""
        return self.state.is_terminal()

    def display(self, depth=0):
        """Recursively displays the tree structure."""
        indent = "  " * depth
        print(f"{indent}Player: {self.state.player}")
        self.state.display()
        for child in self.children:
            child.display(depth + 1)


class GameTree:
    def __init__(self, initial_state):
        """
        Constructs a full game tree starting from an initial state.

        :param initial_state: The starting state of the game.
        """
        self.root = TreeNode(initial_state)
        self.build_tree(self.root)

    def build_tree(self, node):
        """Recursively expands the tree until all terminal states are reached."""
        if node.is_terminal():
            return
        node.expand()
        for child in node.children:
            self.build_tree(child)

    def display(self):
        """Displays the entire game tree."""
        self.root.display()

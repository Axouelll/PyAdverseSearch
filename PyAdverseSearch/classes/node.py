# FILE: node.py

class Node:
    next_id = 0
    def __init__(self, state, parent=None, depth=0):
        """
        Represents a node in the game tree.

        :param state: The game state at this node.
        :param parent: The parent node in the tree (None if root).
        :param depth: The depth of the node in the tree.
        """
        self.state = state
        self.parent = parent
        self.depth = depth
        self.valuation = None
        self.children = []  # List of successor nodes
        self.id = Node.next_id
        Node.next_id += 1

#?applyaction
    def _expand(self):
        """Generates all possible successor states and adds them as children."""
        for action in self.state._possible_actions():
            new_state = self.state._apply_action(action)
            child_node = Node(new_state, parent=self, depth=self.depth + 1)
            self.children.append(child_node)

    def is_terminal(self):
        """Returns True if this node represents a terminal state."""
        return self.state._is_terminal()


    def display(self, depth=0):
        """Recursively displays the tree structure."""
        space  = "  " * depth
        print(f"{space}Depth: {self.depth}, Player: {self.state.player}, Heuristic: {self.valuation}")
        self.state.display()
        for child in self.children:
            child.display(depth + 1)

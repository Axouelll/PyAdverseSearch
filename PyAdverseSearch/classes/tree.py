from .node import Node

class GameTree:
    def __init__(self, initial_state, max_depth=float('inf')):
        self.root = Node(initial_state, parent=None, depth=0)
        self.node_count = 0
        self.leaf = 0
        self.max_depth = max_depth
        self.__build_tree(self.root)

    def __build_tree(self, node):
        if node.utility is not None:
            self.leaf += 1
            return
        elif node.depth < self.max_depth:
            node._expand()
            self.node_count += 1
            for child in node.children:
                self.__build_tree(child)

    def display(self):
        print("Nombre de nœuds :", self.node_count)
        print("Nombre de feuilles :", self.leaf)
        self.root.display()

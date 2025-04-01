# FILE: tree.py

from .node import Node

class GameTree:
    def __init__(self, initial_state, max_depth=float('inf')):
        """
        Constructs a full game tree starting from an initial state.

        :param initial_state: The starting state of the game.
        :param max_depth: The maximum depth to explore in the tree.
        """
        self.root = Node(initial_state, parent=None, depth=0)
        self.node_count = 0
        self.leaf = 0
        self.max_depth = max_depth
        self.__build_tree(self.root)


    def __build_tree(self, node):
        # Affichage de la valeur heuristique de chaque nœud lors de sa création
        print(f"Création du nœud - Profondeur: {node.depth}, Joueur: {node.state.player}, Valeur heuristique: {node.valuation}")

        if node.is_terminal():
            self.leaf += 1
            return  # Arrête l'expansion si l'état est terminal
        elif node.depth < self.max_depth:
            node._expand()  # Génère les nœuds successeurs
            self.node_count += 1
            for child in node.children:
                self.__build_tree(child)

    def display(self):
        print("Nombre de nœuds :", self.node_count)
        print("Nombre de feuilles :", self.leaf)
        self.root.display()

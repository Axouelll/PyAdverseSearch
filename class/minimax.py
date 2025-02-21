import node as node

"""
Implémentation de l'algorithme Minimax.
:param Node : Le Node actuel
:return Node: Le meilleut prochain Node
"""
class Minimax :
    def __init__(self, game = None):
        self.game = game

    def minimax_decision(node = None):
        #initialise la meilleur value à - l'infini
        best_value = -1
        #initialise le meilleur Node à nul
        best_node = None

        #On itère sur les enfants du Node
        for n in node.children:
            value = min_value(n)

            # si l'enfant est un meilleur cout que le précédent il
            # devient best Node et best value
            if value > best_value:
                best_value = value
                best_node = n

        return best_node

    def max_value(node = None):
        if node.state.is_terminal():
            return node.state.evaluate()

        v = -1
        for n in node.children:
            v = max(v,min_value(n))
        return v

    def min_value(node = None):
        if node.state.is_terminal():
            return node.state.evaluate()

        v = 100
        for n in node.children:
            v = min(v,max_value(n))
        return v
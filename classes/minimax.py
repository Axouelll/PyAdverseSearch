from classes import node,state,game

"""
Implémentation de l'algorithme Minimax.
:param Node : Le Node actuel
:return Node: Le meilleut prochain Node
"""
class Minimax :
    def __init__(self, game = None):
        self.game = game

    def minimax_decision(self,node = None):
        #initialise la meilleur value à - l'infini
        best_value = game.heuristique(node.etat)
        #initialise le meilleur Node à nul
        best_node = None

        #On itère sur les enfants du Node
        for n in node.children:
            value = self.__min_value(n)

            # si l'enfant est un meilleur cout que le précédent il
            # devient best Node et best value
            if value > best_value:
                best_value = value
                best_node = n

        return best_node

    #private methode for max
    def __max_value(self, node = None):
        if node.state.is_terminal():
            return self.game.utility(node.state)

        v = -1
        for n in node.children:
            v = max(v,self.__min_value(n))
        return v

    #private methode for min
    def __min_value(self, node = None):
        if node.state.is_terminal():
            return self.game.utility(node.state)

        v = game.heuristique(node.etat)
        for n in node.children:
            v = min(v,self.__max_value(n))
        return v
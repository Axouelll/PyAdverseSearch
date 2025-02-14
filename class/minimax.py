
"""
Implémentation de l'algorithme Minimax.
:param Node : Le Node actuel
:return Node: Le meilleut prochain Node
"""
def minimax_decision(Node = None):
    #initialise la meilleur value à - l'infini
    best_value = -1
    #initialise le meilleur Node à nul
    best_Node = None

    #On itère sur les enfants du Node
    for n in Node.children:
        value = min_value(n)

        # si l'enfant est un meilleur cout que le précédent il
        # devient best Node et best value
        if value > best_value:
            best_value = value
            best_Node = n

    return best_Node

def max_value(Node = None):
    if Node.state.is_terminal():
        return Node.state.evaluate()

    v = -1
    for n in Node.children:
        v = max(v,min_value(n))
    return v

def min_value(Node = None):
    if Node.state.is_terminal():
        return Node.state.evaluate()

    v = 100
    for n in Node.children:
        v = min(v,max_value(n))
    return v


'''
def minimax(state, depth, maximizing):
    """
    Implémentation de l'algorithme Minimax.

    :param etat: L'état actuel du jeu.
    :param profondeur: La profondeur de recherche maximale.
    :param maximisant: Booléen indiquant si c'est le tour du joueur MAX.
    :return: La valeur minimax de l'état actuel.
    """

    # Si l'état est terminal ou la profondeur est atteinte, on évalue l'état
    if depth == 0 or state.is_terminal():
        return state.evaluate()

     # Cas du joueur MAX (veut maximiser son score)
    if maximizing:
        max_value = float('-inf')
        for successor in state.generate_successors():
            value = minimax(successor, depth - 1, False)
            max_value = max(max_value, value)
        return max_value

    # Cas du joueur MIN (veut minimiser le score de MAX)
    else:
        min_value = float('inf')
        for successor in state.generate_successors():
            value = minimax(successor, depth - 1, True)
            min_value = min(min_value, value)
        return min_value
'''

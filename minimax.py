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

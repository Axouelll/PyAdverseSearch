# FILE: PyAdverseSearch/classes/minimax.py

import time
from PyAdverseSearch.classes.algorithm import SearchAlgorithm
from PyAdverseSearch.classes.node import Node

class Minimax(SearchAlgorithm):
    def __init__(self, game=None, max_depth=4, max_time_seconds=None):
        # Vérification des paramètres
        if max_depth is not None and (max_depth <= 0 or not isinstance(max_depth, int)):
            print("Error: max_depth must be a positive integer")
            return
        if max_time_seconds is not None and (max_time_seconds <= 0 or not isinstance(max_time_seconds, (int, float))):
            print("Error: max_time_seconds must be a positive number")
            return

        self.game = game
        self.max_depth = max_depth
        self.max_time = max_time_seconds
        self.start_time = None

        if self.max_depth is not None and self.max_time is not None:
            print(f"[INFO] Combined mode: max_depth = {self.max_depth} and max_time = {self.max_time} seconds")
        elif self.max_depth is not None:
            print(f"[INFO] Maximum depth mode (max_depth = {self.max_depth})")
        elif self.max_time is not None:
            print(f"[INFO] Time limit mode (max_time = {self.max_time} seconds)")
        else:
            print("[INFO] Classic Minimax without constraints")

    def choose_best_move(self, state):
        """
        Sélectionne le meilleur coup pour le joueur courant (MAX ou MIN),
        en priorisant les états terminaux (utility × 1000), puis en appelant
        min_value ou max_value selon le joueur, et en comparant scores.
        """
        is_max = (state.player == "MAX")
        print(f"[DEBUG] choose_best_move for {'MAX' if is_max else 'MIN'}")
        state.display()
        print(f"Depth limit: {self.max_depth}\n")

        best_score = -float('inf') if is_max else float('inf')
        best_state = None

        for action in state._possible_actions():
            child = state._apply_action(action)

            # terminal → score fixe très fort
            if self.game.game_is_terminal(child):
                util = self.game.game_utility(child)
                score = util * 1000
                print(f"[DEBUG] Action {action}: terminal utility={util}, score={score}")
            else:
                # non-terminal → on intercale MAX et MIN
                if is_max:
                    score = self.min_value(child, self.max_depth - 1)
                    print(f"[DEBUG] Action {action}: min_value score={score}")
                else:
                    score = self.max_value(child, self.max_depth - 1)
                    print(f"[DEBUG] Action {action}: max_value score={score}")

            # sélection selon MAX ou MIN
            if (is_max and score > best_score) or (not is_max and score < best_score):
                best_score = score
                best_state = child
                print(f"[DEBUG] New best action: {action} with score {score}\n")

        print(f"[DEBUG] choose_best_move end: best_score={best_score}")
        return best_state



    def max_value(self, state, depth):
        """
        Renvoie la plus grande valeur (utility ou heuristic) pour MAX.
        """
        # Terminal state
        if self.game.game_is_terminal(state):
            return self.game.game_utility(state)
        # Depth cutoff: return heuristic
        if depth == 0:
            return self.game.game_heuristic(state)

        v = -float('inf')
        for action in state._possible_actions():
            child = state._apply_action(action)
            v = max(v, self.min_value(child, depth - 1))
        return v

    def min_value(self, state, depth):
        """
        Renvoie la plus petite valeur (utility ou heuristic) pour MIN.
        """
        # Terminal state
        if self.game.game_is_terminal(state):
            return self.game.game_utility(state)
        # Depth cutoff: return heuristic
        if depth == 0:
            return self.game.game_heuristic(state)

        v = float('inf')
        for action in state._possible_actions():
            child = state._apply_action(action)
            v = min(v, self.max_value(child, depth - 1))
        return v


    def time_limit_reached(self):
        if self.max_time is None:
            return False
        return (time.time() - self.start_time) >= self.max_time

    # If the node is terminal, it directly returns its utility value.
    # Otherwise, it recursively calculates utilities of all children.
    def default_utility(self, node):
        if node.is_terminal():
            return node.state._utility()

        # Si pas d'enfants, on retourne l'évaluation heuristique du nœud
        if not node.children:
            return node.valuation

        if node.state.player == "MAX":
            return max(self.default_utility(child) for child in node.children)
        else:  # MIN
            return min(self.default_utility(child) for child in node.children)

    def default_heuristic(self, node):
        if node.state._is_terminal():
            return self.game.game_utility(node.state)

        total = 0
        for child in node.children:
            total += self.default_heuristic(child)
        return total

    def next_move(self, node):
        if not node.children:
            return None

        # Évalue chaque enfant
        child_utils = [(child, self.default_utility(child)) for child in node.children]
        if node.state.player == "MAX":
            best_child = max(child_utils, key=lambda x: x[1])[0]
        else:
            best_child = min(child_utils, key=lambda x: x[1])[0]
        return best_child



"""
BACKUP DES CLASSES INDEPENDANTES
class Minimax :
    def __init__(self, game = None):
        self.game = game

    def minimax_decision(self,node = None):
        #initialise la meilleur value à la valeur heuristique du noeud actuel
        best_value = game.heuristique(node.etat)
        #initialise le meilleur Node à nul
        best_node = None

        #On itère sur les enfants du Node
        for n in node.children:
            value = self.min_value(n)

            # si l'enfant est un meilleur cout que le précédent il
            # devient best Node et best value
            if value > best_value:
                best_value = value
                best_node = n

        return best_node

    def max_value(self, node = None):
        if node.state.is_terminal():
            return self.game.utility(node.state)

        v = -1
        for n in node.children:
            v = max(v,self.min_value(n))
        return v

    def min_value(self, node = None):
        if node.state.is_terminal():
            return self.game.utility(node.state)

        v = game.heuristique(node.etat)
        for n in node.children:
            v = min(v,self.max_value(n))
        return v


'''

ALTERNATIVE MINIMAX CLASS WITH MAX DEPTH ATTRIBUTE

'''
class Minimax_Max_Depth:
    def __init__(self, game=None, max_depth=float('inf')):
        self.game = game
        self.max_depth = max_depth

    def minimax_decision(self, node=None):
        # initialise la meilleur value à - l'infini
        best_value = game.heuristique(node.etat)
        # initialise le meilleur Node à nul
        best_node = None

        # On itère sur les enfants du Node
        for n in node.children:
            #  on transmet l'information de la profondeur actuelle a la
            value = self.min_value(n, current_depth=1)

            # si l'enfant est un meilleur cout que le précédent il
            # devient best Node et best value
            if value > best_value:
                best_value = value
                best_node = n

        return best_node

    def max_value(self, node=None, current_depth=0):
        # Vérifie si la profondeur maximale est atteinte, si c'est le cas on renvoie l'heuristique du noeud courant
        if current_depth >= self.max_depth:
            return game.heuristique(node.etat)

        if node.state.is_terminal():
            return self.game.utility(node.state)

        v = -1
        for n in node.children:
            v = max(v, self.min_value(n, current_depth + 1))
        return v

    def min_value(self, node=None, current_depth=0):
        # Vérifie si la profondeur maximale est atteinte, si c'est le cas on renvoie l'heuristique du noeud courant
        if current_depth >= self.max_depth:
            return game.heuristique(node.etat)

        if node.state.is_terminal():
            return self.game.utility(node.state)

        v = game.heuristique(node.etat)
        for n in node.children:
            v = min(v, self.max_value(n, current_depth + 1))
        return v

'''

ALTERNATIVE MINIMAX CLASS WITH MAX TIME ATTRIBUTE

'''
import time

class Minimax:
    def __init__(self, game=None, max_time_seconds=None):
        self.game = game
        self.max_time = max_time_seconds
        self.start_time = None  # heure de début de l'execution de l'algo

    def minimax_decision(self, node=None):
        self.start_time = time.time()  # on sauvegarde l'heure de depart

        # initialise la meilleur value à - l'infini
        best_value = game.heuristique(node.etat)
        # initialise le meilleur Node à nul
        best_node = None

        # on itère sur les enfants du Node
        for n in node.children:
            value = self.min_value(n)

            # si l'enfant est un meilleur cout que le précédent il devient best Node et best value
            if value > best_value:
                best_value = value
                best_node = n

            # Vérifie si la limite de temps est dépassée, si c'est le cas on arrete l'execution de la boucle for
            if self.time_limit_reached():
                break

        return best_node

    def max_value(self, node=None):
        # Vérifie si la limite de temps est atteinte, si c'est le cas on renvoie l'heuristique du noeud courant
        if self.time_limit_reached():
            return game.heuristique(node.etat)

        if node.state.is_terminal():
            return self.game.utility(node.state)

        v = -1
        for n in node.children:
            v = max(v, self.min_value(n))

            if self.time_limit_reached():
                break
        return v

    def min_value(self, node=None):
        # Vérifie si la limite de temps est atteinte, si c'est le cas on renvoie l'heuristique du noeud courant
        if self.time_limit_reached():
            return game.heuristique(node.etat)

        if node.state.is_terminal():
            return self.game.utility(node.state)

        v = game.heuristique(node.etat)
        for n in node.children:
            v = min(v, self.max_value(n))

            if self.time_limit_reached():
                break
        return v

    # fonction permettant de verifier que la limite de temps n'est pas depasser
    # renvoie vrai si elle est depassee, faux sinon
    def time_limit_reached(self):
        if self.max_time is None:
            return False  # Pas de limite de temps définie
        elapsed_time = time.time() - self.start_time
        return elapsed_time >= self.max_time

"""
"""
def choose_best_move(self, state):
        is_max = (state.player == "MAX")
        best_score = -float('inf') if is_max else float('inf')
        best_state = None

        for action in state._possible_actions():
            child = state._apply_action(action)

            # Score terminal, on priorise utility × 1000
            if self.game.game_is_terminal(child):
                score = self.game.game_utility(child) * 1000
            else:
                # Après un coup de MAX, c’est MIN qui joue => min_value
                # Après un coup de MIN, c’est MAX qui joue => max_value
                if is_max:
                    score = self.min_value(child, self.max_depth - 1)
                else:
                    score = self.max_value(child, self.max_depth - 1)

            # Choix selon MAX ou MIN
            if (is_max and score > best_score) or (not is_max and score < best_score):
                best_score = score
                best_state = child

        return best_state
"""
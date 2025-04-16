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
        Implémente la méthode de l'interface SearchAlgorithm.
        À partir d'un état donné, génère les successeurs via _generate_successors()
        et renvoie le meilleur état enfant en utilisant la valeur heuristique.

        Logique :
        - Si un état enfant terminal a utility == 1, il est renvoyé immédiatement.
        - Sinon, parmi tous les états successeurs, on retourne celui avec la meilleure évaluation heuristique.
        """
        self.start_time = time.time()
        best_value = self.game.game_heuristic(state)
        best_state = None

        print(f"[DEBUG] Évaluation initiale de l'état courant: {best_value}")

        # On suppose que _generate_successors() retourne une liste d'états successeurs.
        successors = state._generate_successors()
        for idx, child_state in enumerate(successors):
            # Crée un nœud temporaire pour évaluer cet état successeur
            child_node = Node(child_state, parent=None, depth=1)
            print(f"[DEBUG] Successeur {idx}: Heuristic = {child_node.valuation}, utility = {child_node.utility}")

            # Si cet état est terminal et a utility == 1, c'est le meilleur cas possible pour MAX.
            if child_node.utility == 1:
                print(f"[DEBUG] Successeur {idx} est terminal avec utility == 1, retour immédiat de cet état.")
                return child_state

            # Met à jour le meilleur état selon la valeur heuristique (valuation)
            if child_node.valuation >= best_value:
                best_value = child_node.valuation
                best_state = child_state
                print(f"[DEBUG] Successeur {idx} devient le meilleur état avec une nouvelle évaluation: {best_value}")

            if self.time_limit_reached():
                print("[DEBUG] Limite de temps atteinte, arrêt de l'exploration.")
                break

        print(f"[DEBUG] Retour du meilleur état avec évaluation finale: {best_value}")
        return best_state


    def min_value(self, state, current_depth=0):
        if current_depth >= self.max_depth or state.is_terminal():
            return self.game.game_heuristic(state)
        min_eval = float('inf')
        for action, child_state in state._generate_successors():
            eval_value = self.max_value(child_state, current_depth + 1)
            if eval_value < min_eval:
                min_eval = eval_value
            if self.time_limit_reached():
                break
        return min_eval

    def max_value(self, state, current_depth=0):
        if current_depth >= self.max_depth or state.is_terminal():
            return self.game.game_heuristic(state)
        max_eval = -float('inf')
        for action, child_state in state._generate_successors():
            eval_value = self.min_value(child_state, current_depth + 1)
            if eval_value > max_eval:
                max_eval = eval_value
            if self.time_limit_reached():
                break
        return max_eval

    def time_limit_reached(self):
        if self.max_time is None:
            return False
        return (time.time() - self.start_time) >= self.max_time


    # If the node is terminal, it directly returns its utility value. Otherwise, it recursively calculates the total utility of all child nodes.
    def default_heuristic(self, node):
        if node.state.is_terminal():
            return self.game.utility(node.state)

        total = 0
        for node_child in node.children:
            total += self.default_heuristic(node_child)

        return total

    def default_utility(self, node):
        if node.is_terminal():
            return node.state._utility()

        if node.state.player == "MAX":
            return max(self.default_utility(child) for child in node.children)
        else:  # MIN
            return min(self.default_utility(child) for child in node.children)

    def next_move(self, node):
        if not node.children:
            return None  # Aucun coup possible

        # Calculer la valeur utilitaire de chaque enfant
        child_utilities = [(child, self.default_utility(child)) for child in node.children]

        if node.state.player == "MAX":
            # Retourner l'enfant avec la plus haute utilité
            best_child = max(child_utilities, key=lambda x: x[1])[0]
        else:  # player == "MIN"
            # Retourner l'enfant avec la plus basse utilité
            best_child = min(child_utilities, key=lambda x: x[1])[0]

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
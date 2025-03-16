from classes import game
import time

"""
Implémentation de l'algorithme Minimax.
:param game: la partie sur laquelle utilisee l'algorithme
:param max_depth: la profondeur maximum autorisee
:param max_time_seconds: le temps en secondes d'execution de l'algorithme autorise
:return Node: Le meilleur prochain Node

si ni max_depth ni max_time_seconds ne sont fournis au constructeur de la classe, c'est le fonction de l'algorithme classique qui s'effectura
si max_depth est donne, la verification de la profondeur se fera
si max_time_seconds est donne, la verification de la duree d'execution de l'algorithme se fera
si les deux sont donnes, la verification de la profondeur et de la duree d'execution se feront
"""

class Minimax:
    def __init__(self, game=None, max_depth=None, max_time_seconds=None):
        # on verifie que si il y a un max depth ou/et un max time, qu'ils soient bien des nombres positifs et que max depth soit bien un entier
        if max_depth is not None and ( max_depth <= 0 or not isinstance(max_depth, int) ) :
            print("Error during the creation of a Minimax instance, max depth attribute must be a positive integer")
            return
        # max time peut etre un entier ou un reel (toujours positif non nul)
        elif max_time_seconds is not None and ( max_time_seconds <= 0 or not isinstance(max_time_seconds, float) or not isinstance(max_time_seconds, int) ):
            print("Error during the creation of a Minimax instance, max time attribute must be a positive integer or a positive float")
            return

        self.game = game
        self.max_depth = max_depth
        self.max_time = max_time_seconds
        self.start_time = None

        if self.max_depth is not None and self.max_time is not None:
            print(f"[INFO] Mode combiné : profondeur maximale ({self.max_depth}) et limite de temps ({self.max_time} sec) activés")
        elif self.max_depth is not None:
            print(f"[INFO] Mode profondeur maximale activé (max_depth = {self.max_depth})")
        elif self.max_time is not None:
            print(f"[INFO] Limite de temps activée (max_time = {self.max_time} secondes)")
        else:
            print("[INFO] Minimax classique sans contrainte activé")


    def minimax_decision(self, node=None):
        self.start_time = time.time()

        best_value = game.heuristique(node.etat)
        best_node = None

        for n in node.children:
            value = self.min_value(n, current_depth=1)

            if value > best_value:
                best_value = value
                best_node = n

            if self.time_limit_reached():
                break

        return best_node

    def max_value(self, node=None, current_depth=0):
        if self.max_depth is not None and current_depth >= self.max_depth:
            return game.heuristique(node.etat)

        if self.time_limit_reached():
            return game.heuristique(node.etat)

        if node.state.is_terminal():
            return self.game.utility(node.state)

        v = -1
        for n in node.children:
            v = max(v, self.min_value(n, current_depth + 1))

            if self.time_limit_reached():
                break

        return v

    def min_value(self, node=None, current_depth=0):
        if self.max_depth is not None and current_depth >= self.max_depth:
            return game.heuristique(node.etat)

        if self.time_limit_reached():
            return game.heuristique(node.etat)

        if node.state.is_terminal():
            return self.game.utility(node.state)

        v = game.heuristique(node.etat)
        for n in node.children:
            v = min(v, self.max_value(n, current_depth + 1))

            if self.time_limit_reached():
                break

        return v

    # fonction permettant de verifier que la limite de temps n'est pas depasser
    # renvoie vrai si elle est depassee, faux sinon
    def time_limit_reached(self):
        if self.max_time is None:
            return False
        elapsed_time = time.time() - self.start_time
        return elapsed_time >= self.max_time





""""
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
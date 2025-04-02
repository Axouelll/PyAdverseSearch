# FILE: PyAdverseSearch/classes/algorithm.py

from abc import ABC, abstractmethod

class SearchAlgorithm(ABC):
    @abstractmethod
    def choose_best_move(self, state):
        """
        À partir d'un état donné, retourne le meilleur coup (ou action) à jouer,
        ou un état enfant (selon votre choix).
        """
        pass

# Dictionnaire d'algorithmes – initialement vide pour éviter l'import circulaire
ALGORITHMS = {}

def choose_best_move(algo_name, game, state, **kwargs):
    """
    Permet de sélectionner dynamiquement l'algorithme voulu (par son nom)
    et de retourner le meilleur coup/enfant à partir de l'état fourni.
    """
    # Import local pour éviter le cercle d'import
    if algo_name == 'minimax':
        from .minimax import Minimax
        AlgoClass = Minimax
    # ajout des futurs algorithmes ICI
    else:
        raise ValueError(f"Algorithme inconnu : {algo_name}")

    algo = AlgoClass(game=game, **kwargs)
    return algo.choose_best_move(state)

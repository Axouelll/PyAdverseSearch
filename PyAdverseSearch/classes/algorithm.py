# FILE: algorithm.py
from abc import ABC, abstractmethod

class SearchAlgorithm(ABC):
    @abstractmethod
    def choose_best_move(self, state):
        """
        À partir d'un état donné, retourne le meilleur coup (ou action) à jouer.
        """
        pass

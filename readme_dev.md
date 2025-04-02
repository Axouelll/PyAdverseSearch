## Guide de développement pour PyAdverseSearch

Ce fichier README s'adresse aux développeurs souhaitant reprendre, étendre ou améliorer la bibliothèque PyAdverseSearch. Contrairement au guide principal destiné aux utilisateurs, ce document fournit une vue détaillée de l'architecture interne, des conventions de conception, ainsi que des indications précises pour développer de nouveaux jeux, algorithmes ou fonctionnalités compatibles avec le framework.

## Présentation générale

PyAdverseSearch est structurée pour permettre une exploration adverse efficace dans des jeux à deux joueurs à somme nulle. Elle s’appuie sur des classes abstraites à spécialiser pour chaque jeu, ainsi qu’un arbre d’exploration et des algorithmes comme Minimax. La bibliothèque est conçue pour être facilement extensible, tout en respectant une architecture bien définie.

## Structure interne du projet

Le dossier principal contient un répertoire class/ qui regroupe les classes essentielles : State, Game, Node, Tree, Minimax, ainsi qu'une interface SearchAlgorithm. Le dossier test/ contient des implémentations concrètes de jeux comme le Tic Tac Toe ou le Puissance 4. Ces exemples servent à la fois de démonstration et de base pour les tests automatisés ou manuels.

## Conception orientée objet et hiérarchie

La classe State est abstraite et doit être étendue pour chaque jeu. Elle définit les éléments nécessaires à la modélisation d’un état de jeu : le plateau (board), le joueur actif (player), l’état parent, et une référence à l’instance de la classe Game pour appeler dynamiquement les fonctions du jeu. Chaque état doit donc implémenter les méthodes publiques possible_actions, apply_action, is_terminal, et evaluate, qui définissent respectivement les actions valides, la transition d’un état à un autre, la condition de fin de partie, et l’évaluation heuristique.

La classe Game est le point d’entrée utilisateur. Elle permet d’associer des fonctions spécifiques à un jeu donné à une instance globale, en centralisant les règles, la fonction de fin, l’utilité et l’heuristique. Elle construit automatiquement un arbre d’exploration à partir de l’état initial, via la classe GameTree.

La classe Node représente chaque nœud de l’arbre de jeu. Elle encapsule un état, ses enfants, son parent, un identifiant unique et sa profondeur. La construction de l’arbre est déléguée à GameTree, dont la méthode privée __build_tree() s’occupe de générer récursivement tous les nœuds à partir de la racine.

L’algorithme Minimax est implémenté dans sa propre classe. Il propose trois modes d'exécution : classique (sans limite), avec profondeur maximale, et avec limite de temps. La méthode principale choose_best_move permet de déterminer le meilleur coup à jouer à partir d’un état donné.

## Conventions de nommage et encapsulation

Dans l’architecture de PyAdverseSearch, des conventions sont utilisées pour marquer les fonctions internes ou critiques :

Les méthodes préfixées par un seul tiret bas (_) sont dites protégées. Elles sont destinées à être utilisées uniquement en interne, soit par la classe elle-même, soit par ses sous-classes. Par exemple, dans la classe State, les méthodes _possible_actions, _apply_action, _is_terminal, _evaluate ou _generate_successors sont appelées par l’arbre d’exploration et les algorithmes, mais ne doivent pas être invoquées directement par l’utilisateur final. Elles assurent une interface cohérente entre les classes internes tout en permettant la spécialisation via des méthodes publiques comme apply_action.

Une seule méthode privée est définie dans le projet : __build_tree, au sein de la classe GameTree. Le double underscore (__) déclenche un mécanisme de masquage de nom en Python (name mangling) afin de limiter strictement son accès à la classe elle-même. Cette méthode étant responsable de la construction complète et récursive de l’arbre, elle est rendue privée pour garantir l'intégrité de la structure et éviter toute manipulation externe non contrôlée.

Ces conventions d'encapsulation permettent de maintenir la séparation entre l'interface utilisateur (à modifier ou spécialiser) et l'infrastructure interne (à manipuler avec précaution), ce qui facilite la maintenance et la robustesse de la bibliothèque.

## Étendre la bibliothèque : ajout d’un nouveau jeu

Pour ajouter un jeu personnalisé, il faut :

Créer une nouvelle sous-classe de State et y implémenter toutes les méthodes obligatoires (possible_actions, apply_action, is_terminal, evaluate).

Définir les fonctions spécifiques au jeu : celles-ci seront passées à la classe Game lors de son instanciation (par exemple, winner_function, utility, heuristic).

Instancier un objet Game avec l’état initial et les fonctions définies.

Vérifier que state.game est bien initialisé (ce lien est crucial pour que les méthodes dynamiques comme _is_terminal ou _evaluate fonctionnent).

Tester le comportement à l’aide de l’algorithme Minimax, en modifiant éventuellement sa profondeur ou sa limite de temps.

## Ajouter un nouvel algorithme d’exploration

L’extension à d’autres algorithmes est également prévue. Il suffit de créer une nouvelle classe héritant de SearchAlgorithm et d’implémenter la méthode choose_best_move(state). L’algorithme peut exploiter l’arbre fourni ou utiliser une autre stratégie (ex. Monte Carlo, Alpha-Beta Pruning, etc.).

Il est conseillé de respecter la structure et les conventions existantes, notamment pour le nommage des paramètres, la gestion du temps et la compatibilité avec les objets State et Game.

## Tests, exemples et recommandations

Les fichiers de test sont situés dans le dossier test/. Ils contiennent des jeux complets comme TicTacToe (state_tictactoe.py) ou Connect 4, ainsi que des fonctions comme generate_tictactoe_game() qui facilitent l’automatisation des tests. Il est recommandé de créer une fonction équivalente pour tout nouveau jeu ajouté.

L’affichage des états est géré par la méthode display() dans chaque sous-classe de State, et peut être personnalisé pour chaque jeu. Des visualisations plus avancées peuvent être ajoutées sous forme de modules externes ou notebooks Jupyter.

## Collaboration et bonnes pratiques

Les contributions au projet peuvent se faire via GitHub. Chaque fonctionnalité doit être développée sur une branche dédiée. Toute nouvelle classe ou méthode importante doit être documentée. Il est également recommandé de conserver une certaine homogénéité dans les messages de commit, les noms de fichiers et les logs (print("[DEBUG] ...")).

Ce guide vise à fournir aux développeurs toutes les informations nécessaires pour comprendre, utiliser et faire évoluer PyAdverseSearch de manière structurée et efficace.



### Résolveur du problème des N reines

Ce script Python utilise le module `pysat` pour résoudre le problème des N reines en formulant le problème comme un ensemble de clauses SAT (satisfiabilité booléenne). Le but est de placer N reines sur un échiquier N x N de manière à ce qu'aucune reine ne puisse en attaquer une autre.

#### Fonctionnalités principales :
- Génération des variables pour représenter les positions des reines sur l'échiquier
- Ajout de contraintes pour s'assurer qu'il y a exactement une reine par ligne, une par colonne, et une par diagonale
- Utilisation d'un solveur SAT pour trouver des solutions
- Affichage des solutions trouvées sous forme d'échiquier
- Comptage et affichage du nombre total de solutions trouvées

#### Utilisation :
1. Exécutez le script.
2. Entrez la taille de l'échiquier (N).
3. Le script affichera toutes les solutions possibles et le nombre total de solutions.
4. Vous pouvez également choisir d'afficher les contraintes générées si besoin.


### Résolveur du problème des N reines

Ce script Python utilise le module `pysat` pour résoudre le problème des N reines en formulant le problème comme un ensemble de clauses SAT (satisfiabilité booléenne). Le but est de placer N reines sur un échiquier N x N de manière à ce qu'aucune reine ne puisse en attaquer une autre.

#### Fonctionnalités principales :
- Génération des variables pour représenter les positions des reines sur l'échiquier
- Ajout de contraintes pour s'assurer qu'il y a exactement une reine par ligne, une par colonne, et une par diagonale
- Utilisation d'un solveur SAT pour trouver des solutions
- Affichage des solutions trouvées sous forme d'échiquier
- Comptage et affichage du nombre total de solutions trouvées

#### Prérequis : 
- Python 3.X,
- Créer un environnement de dév,
- installer python-sat -> pip install python-sat

#### Utilisation :
1. Exécutez le script.
2. Entrez la taille de l'échiquier (N).
3. Le script affichera toutes les solutions possibles et le nombre total de solutions.
4. Vous pouvez également choisir d'afficher les contraintes générées si besoin.

Exemple : 
N = 4

<img width="367" height="298" alt="image" src="https://github.com/user-attachments/assets/226b8a09-18fb-448b-8cac-baae5b0a0e58" />

N = 8

<img width="382" height="409" alt="image" src="https://github.com/user-attachments/assets/7104cef5-aac6-4918-a5b5-92dd452ba272" />

Test sans solution : 
N = 2

<img width="369" height="229" alt="image" src="https://github.com/user-attachments/assets/3275f6ba-e5ce-449c-878d-55414d8d2ed7" />

N = 3

<img width="353" height="480" alt="image" src="https://github.com/user-attachments/assets/14d5bd98-a7a7-48d3-98e2-cf8245b97621" />



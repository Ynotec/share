# Implémentation de l'Algorithme de Bellman-Ford

Ce projet propose une implémentation native en Python de l'algorithme de Bellman-Ford. Il permet de calculer les plus courts chemins depuis un sommet source vers tous les autres sommets d'un graphe orienté pondéré, tout en détectant la présence éventuelle de cycles de poids négatif.

## Fonctionnalités

- **Calcul des plus courts chemins** : Détermine la distance minimale et le chemin complet depuis une source.
- **Détection de cycles négatifs** : Signale si le graphe contient des cycles de poids négatif rendant le calcul impossible pour certains nœuds.
- **Graphes pondérés** : Supporte des poids entiers ou décimaux, positifs ou négatifs.
- **Interface CLI** : Utilisation simple via la ligne de commande.

## Installation et Utilisation

### Prérequis
- Python 3.x installé sur la machine.
- Aucune bibliothèque externe n'est requise (utilisation des bibliothèques standard uniquement).

### Commande d'exécution
Le programme s'exécute via la ligne de commande en spécifiant le fichier du graphe et optionnellement le nœud source.

python bellman_ford.py fichier.txt

Démonstration 

Traitement normal 

Contenu du fichier : 
-------
```
A B 4
A C 2
B C 1
B D 5
C D 3
```
-------
Execution
-------
```
Traitement du graphe: fichierNormal.txt
Nombre de sommets: 4
Nombre d'arêtes: 5

Plus courts chemins depuis le nœud A:
Vers B: distance = 4, chemin A -> B
Vers C: distance = 2, chemin A -> C
Vers D: distance = 5, chemin A -> C -> D
```
------

Traitement négatif OK

Contenu du fichier :
--------
```
S A 6
S E 7
A B 5
A C -4
A D 8
B A -2
C D 7
D A 2
D C -3
D E 9
```
-------
Execution
--------
```
Traitement du graphe: fichierNegatifOk.txt
Nombre de sommets: 6
Nombre d'arêtes: 10

Plus courts chemins depuis le nœud A:
Vers B: distance = 5, chemin A -> B
Vers C: distance = -4, chemin A -> C
Vers D: distance = 3, chemin A -> C -> D
Vers E: distance = 12, chemin A -> C -> D -> E
Vers S: distance = Inaccessible, chemin -
```

Traitement de cycle négatif

Contenu du fichier :
--------
```
S A 5
A B 1
B C -4
C A 2
C D 3
```
------
Execution
------
```
Traitement du graphe: fichierTestCycleNeg.txt
Nombre de sommets: 5
Nombre d'arêtes: 5

Plus courts chemins depuis le nœud A:
ALERTE : Un cycle de poids négatif a été détecté accessible depuis la source !
```

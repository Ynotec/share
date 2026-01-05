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

```bash
python bellman_ford.py fichier.txt
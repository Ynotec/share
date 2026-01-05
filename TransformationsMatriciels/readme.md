# Visualiseur de Transformations Matricielles 2D
Ce projet est une application web interactive permettant de visualiser en temps réel l'impact des transformations matricielles (rotation, translation, mise à l'échelle) sur des formes géométriques en 2D.

## Fonctionnalités

### Création de formes :

- Utilisation de formes prédéfinies (Triangle, Quadrilatère, Carré).
- Définition personnalisée point par point (coordonnées X, Y).
- Ajustement dynamique du nombre de sommets (minimum 3).

### Transformations Matricielles :

- Rotation : Application de rotations prédéfinies (90°, 180°, 270°) autour de l'origine.
- Translation : Déplacement de la forme sur les axes X et Y via une matrice de translation.
- Mise à l'échelle (Scaling) : Redimensionnement global de la forme par un facteur k.

### Visualisation :

- Rendu sur un canvas HTML5.
- Affichage d'une grille repère avec axes X et Y centrés.
- Personnalisation de la couleur de la forme.

*Interface Réactive : Les coordonnées affichées dans l'interface se mettent à jour automatiquement après chaque transformation.*

## Installation et Lancement
Ce projet utilise des modules ES6. Vous ne pouvez pas simplement ouvrir le fichier index.html directement depuis votre explorateur de fichiers.

### Prérequis

- Un navigateur web (Chrome, Firefox, Edge, Safari).
- Un serveur local simple.

### Comment lancer le projet

- Cloner ou télécharger les fichiers du projet.
- Lancer un serveur local à la racine du dossier.

par exemple avec VS Code : Installez l'extension "Live Server", faites un clic droit sur index.html et choisissez "Open with Live Server".

Accédez à l'adresse locale (ex: http://127.0.0.1:5500 ou http://localhost:8000).

## Architecture du Code

Le projet suit une structure modulaire pour garantir la maintenabilité :

- **index.html** : Structure de la page et conteneur du Canvas.
- **style.css** : Mise en page (Flexbox) et design de l'interface.
- **main.js** : Point d'entrée de l'application. Il orchestre les interactions entre le rendu, la logique mathématique et l'interface utilisateur.
- **matrix.js** : Contient la logique mathématique pure.
  -> Classe utilitaire statique fournissant les matrices 3x3 pour la rotation, la translation et le scaling.
  -> Méthode transformPoint pour appliquer une matrice à un point (x,y).
- **renderer.js** : Gère le contexte graphique (Canvas 2D).
  -> Dessin de la grille et des axes.
  -> Conversion des coordonnées mathématiques (centrées) vers les coordonnées écran (Canvas).
  -> Tracé des polygones.
- **uimanager.js** : Gère le DOM.
  -> Récupération des entrées utilisateur (inputs, boutons).
  -> Génération dynamique des champs de coordonnées.
  -> Mise à jour des valeurs affichées après calcul.


Démonstration : 

Un triangle avec 3 transformations appliquées

1. Rotation 90
2. Translation
3. Mise à l'échelle

<img width="1307" height="648" alt="image" src="https://github.com/user-attachments/assets/0de9460f-4b06-4d81-8d4d-8b7134ab99fe" />

Un quadrilatère avec une composition d'au moins 2 transformation

Translation + rotation 90

<img width="995" height="495" alt="image" src="https://github.com/user-attachments/assets/6c359f5a-56e2-472a-9b69-8895b9c463fe" />


L'effet d'une translation combinée avec une rotation 

<img width="988" height="497" alt="image" src="https://github.com/user-attachments/assets/c6c41e6b-7346-4bd8-bfef-b1acf8bbe259" />



---
title: "4. Création des objets et mise en place du scrolling parallaxe"
weight: 4
prev_url: "/game-maker-studio/shoot-them-up/demarrer-projet-game-maker-studio-gestion-ressources/"
next_url: "/game-maker-studio/shoot-them-up/debuter-game-maker-integrer-deplacer-vaisseau/"
date: 2023-10-27
categories: ['Archive']
tags: ['GameMaker', 'Tutoriel', 'GameDev', 'LevelDesign']
images: ["https://img.youtube.com/vi/J8ScXyORCVI/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/J8ScXyORCVI/maxresdefault.jpg"]
---

Dans ce guide, nous allons transformer vos ressources graphiques en éléments interactifs et donner vie à votre premier niveau grâce à la technique du scrolling parallaxe.

{{< youtube-rgpd "J8ScXyORCVI" >}}

### Résumé des notions clés

*   **Gestion des Objets (Objects) :** Les sprites ne sont que des images statiques. Pour leur donner vie (vitesse, collisions, logique), il est indispensable de les convertir en "Objets".
*   **Configuration des Rooms :** La "Room" est votre espace de jeu. Il est crucial de définir ses dimensions (largeur/hauteur) et sa fréquence de rafraîchissement (FPS) pour garantir une expérience fluide.
*   **Superposition de Backgrounds :** Game Maker permet d'empiler plusieurs calques de fond pour enrichir visuellement votre scène.
*   **Effet de Parallaxe :** En attribuant des vitesses de défilement horizontales (Hspeed) différentes à chaque calque de fond, vous créez une illusion de profondeur et de distance, essentielle pour le dynamisme d'un jeu 2D.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions récentes de Game Maker (GMS2 et versions ultérieures) aient fait évoluer l'interface utilisateur, les concepts fondamentaux abordés ici restent le socle de tout développement 2D :

1.  **La séparation Sprite/Objet :** Cette architecture reste le cœur du moteur. Comprendre que l'objet est le conteneur logique de votre entité est une compétence indispensable.
2.  **La gestion des calques (Layers) :** La logique de superposition des backgrounds est devenue encore plus puissante avec le système de "Layer" moderne, permettant de gérer la profondeur (Z-index) de manière très intuitive.
3.  **Le Parallaxe :** Cette technique demeure le standard de l'industrie pour donner du relief aux jeux en 2D. La manipulation des vitesses de défilement est toujours la méthode la plus efficace et la moins coûteuse en ressources pour simuler un environnement vivant.

{{< footer >}}
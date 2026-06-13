---
title: "7. Maîtriser le tir automatique et la gestion des instances"
weight: 7
prev_url: "/game-maker-studio/shoot-them-up/limiter-deplacements-vaisseau-game-maker-studio/"
next_url: "/game-maker-studio/shoot-them-up/creer-ennemis-spawn-dynamique-gamemaker/"
date: 2023-10-27
categories: ['Archive']
tags: ['Game Maker', 'Tutoriel', 'Programmation', 'Gamedev']
---

Apprendre à créer un système de tir automatique est une étape fondamentale pour tout développeur débutant sur Game Maker Studio, car cela permet de comprendre la gestion du temps et des objets.

{{< youtube-rgpd "F9s0fEzwpNk" >}}

### Résumé des notions clés

Dans ce tutoriel, nous avons abordé les piliers de la création d'un système de tir fonctionnel :

*   **Utilisation des Alarmes :** Création d'un événement `Alarm 0` pour cadencer le tir et éviter une création d'objets infinie à chaque frame.
*   **Gestion des instances :** Utilisation de la fonction `instance_create(x, y, obj)` pour faire apparaître les lasers à la position du vaisseau.
*   **Variables intégrées :**
    *   `room_speed` : Pour rendre la cadence de tir indépendante de la vitesse de rafraîchissement du jeu.
    *   `hspeed` : Pour définir la vitesse horizontale de déplacement du projectile.
    *   `depth` : Pour gérer la superposition des calques (le laser doit apparaître au-dessus du vaisseau).
*   **Optimisation des ressources :** Utilisation de l'événement `Outside Room` couplé à `instance_destroy()` pour supprimer les objets qui ne sont plus visibles à l'écran, évitant ainsi les fuites de mémoire.

### Ce qui reste d'actualité aujourd'hui

Bien que Game Maker ait évolué (notamment avec l'introduction du GML moderne et des systèmes de couches/layers plus complexes), les concepts présentés ici restent le socle de tout projet 2D :

1.  **La logique de boucle :** Le concept d'alarme est toujours la méthode la plus propre pour gérer des actions répétitives sans surcharger le processeur.
2.  **L'optimisation est reine :** La destruction des instances hors champ (`instance_destroy`) est une règle d'or qui reste indispensable, quel que soit le moteur utilisé, pour maintenir un jeu fluide sur le long terme.
3.  **La manipulation des coordonnées :** Apprendre à décaler l'apparition d'un objet (`x + 16`) par rapport à son parent est une compétence essentielle pour le "game feel" et le rendu visuel de vos armes.

{{< footer >}}
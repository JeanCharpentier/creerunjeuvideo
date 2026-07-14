---
title: "13. Gérer les collisions et la défaite du joueur"
weight: 13
prev_url: "/game-maker-studio/shoot-them-up/gerer-collisions-destruction-ennemis-gamemaker/"
next_url: "/game-maker-studio/shoot-them-up/creer-menus-interactifs-gamemaker-studio/"
date: 2023-10-27
categories: ['Archive']
tags: ['GameMaker', 'Tutoriel', 'Developpement de jeux', 'Collision']
images: ["https://img.youtube.com/vi/Wigukk6hdqY/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/Wigukk6hdqY/maxresdefault.jpg"]
---

Apprenez à implémenter un système de défaite efficace en gérant les collisions entre votre vaisseau et les ennemis ou leurs projectiles dans GameMaker.

{{< youtube-rgpd "Wigukk6hdqY" >}}

### Résumé des notions clés

*   **Gestion des collisions :** Utilisation de l'événement `Collision` pour détecter les interactions entre le vaisseau du joueur et les objets ennemis (vaisseaux ou lasers).
*   **Destruction d'instances :** Utilisation de la fonction `instance_destroy()` pour supprimer les objets impliqués dans la collision.
*   **Ciblage dynamique :** Utilisation de `other` dans le code de collision pour identifier précisément l'objet qui entre en contact avec le joueur.
*   **Duplication d'événements :** Optimisation du workflow en dupliquant les événements de collision pour les différents types d'ennemis et de projectiles afin de gagner du temps.
*   **Tests de gameplay :** Importance de tester les différentes conditions de défaite (collision frontale vs projectile) pour valider la logique du jeu.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions récentes de GameMaker (GMS2/GMS2023+) aient évolué, les fondamentaux présentés ici restent le socle de tout jeu d'action :

1.  **La logique de collision :** Le concept d'utiliser `instance_destroy()` sur `other` reste la méthode standard pour gérer les interactions destructibles.
2.  **L'architecture événementielle :** Le système d'événements de GameMaker est toujours basé sur cette structure, rendant la gestion des collisions extrêmement intuitive et performante.
3.  **Bonnes pratiques de workflow :** La duplication d'événements et la réutilisation de code sont des réflexes essentiels pour maintenir un projet propre, surtout lorsque le nombre d'ennemis augmente.
4.  **Gestion des états :** Bien que ce tutoriel se concentre sur la destruction, il pose les bases pour introduire plus tard des systèmes de "Game Over" ou de réapparition (respawn), piliers de la boucle de jeu.

{{< footer >}}
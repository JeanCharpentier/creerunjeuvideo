---
title: "2. Créer des ennemis et un système de tir dans GDevelop 5"
weight: 2
date: 2024-05-22
categories: ['Tutoriels GDevelop']
tags: ['GDevelop', 'GameDev', 'Survivors-like', 'Tutoriel']
---

Bienvenue dans ce deuxième volet de notre série dédiée à la création d'un jeu de type "Survivors-like" avec GDevelop 5. Après avoir mis en place les déplacements de base de notre personnage, il est temps de donner un peu de vie (et de danger) à notre scène en ajoutant des ennemis qui nous traquent et un système de tir automatique pour se défendre.

{{< youtube-rgpd "XTURiRilc0k" >}}

### Ce que vous allez apprendre dans cet épisode :

*   **Gestion des objets et des groupes :** Organisation de vos ressources (armes et ennemis) pour faciliter la programmation.
*   **Comportement "Recherche de chemin" (Pathfinding) :** Comment faire en sorte que vos ennemis se dirigent intelligemment vers le joueur.
*   **Optimisation des collisions :** Utiliser l'action "Séparer deux objets" pour éviter que les ennemis ne se superposent et ne forment un bloc unique.
*   **Système de tir automatique :** Utilisation des points personnalisés sur le sprite du joueur pour créer des projectiles qui visent l'ennemi le plus proche.
*   **Optimisation des performances :** Utilisation du comportement "Détruire en dehors de l'écran" pour éviter de surcharger la mémoire avec des projectiles inutiles.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions de GDevelop évoluent, les concepts abordés ici restent les piliers fondamentaux pour tout jeu de type *bullet heaven* ou *survivors-like* :

1.  **L'utilisation des Groupes :** C'est la méthode la plus efficace pour gérer des dizaines d'ennemis sans dupliquer vos lignes d'événements.
2.  **Le Pathfinding :** Le comportement natif de GDevelop est toujours la solution recommandée pour des déplacements fluides, même si vous ajoutez des obstacles complexes par la suite.
3.  **Les points personnalisés :** Apprendre à manipuler les points d'origine et les points de "socket" (comme pour l'arme) est indispensable pour que vos projectiles partent exactement de l'endroit souhaité, peu importe l'animation du personnage.
4.  **La gestion du cycle de vie des objets :** Le comportement "Détruire en dehors de l'écran" est une règle d'or en GameDev pour maintenir un framerate stable, surtout dans un genre où le nombre d'objets à l'écran peut exploser très rapidement.

{{< footer >}}
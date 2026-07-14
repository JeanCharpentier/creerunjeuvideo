---
title: "15. Créer un système de vagues d''ennemis sur PICO-8"
weight: 15
date: 2023-10-27
categories: ['PICO-8']
tags: ['gamedev', 'tutoriel', 'lua', 'pixelart']
images: ["https://img.youtube.com/vi/L3Kf3dgaXEg/maxresdefault.jpg"]
---

Dans ce nouvel épisode de notre série dédiée à la création d'un *Space Invaders-like* sur PICO-8, nous allons structurer la progression de notre jeu. Après avoir défini nos différents types d'ennemis, il est temps de les organiser en vagues successives pour donner du rythme à l'expérience de jeu.

{{< youtube-rgpd "L3Kf3dgaXEg" >}}

### Au programme de cet atelier :
*   **Organisation des vagues :** Création d'un tableau global pour lister et séquencer l'apparition des ennemis.
*   **Gestion de l'index :** Utilisation d'une variable `ivague` pour suivre la progression du joueur.
*   **Nettoyage automatique :** Mise en place d'une routine pour vider les tableaux d'ennemis et de tirs entre chaque vague, évitant ainsi les bugs de collision résiduels.
*   **Transition d'état :** Passage automatique vers un écran de victoire (ou *Game Over*) une fois que toutes les vagues ont été terrassées.

### Ce qui reste d'actualité aujourd'hui
*   **Modularité :** La méthode utilisée ici permet d'ajouter autant de vagues que vous le souhaitez sans modifier le cœur du moteur de jeu.
*   **Gestion des états (Game State) :** L'utilisation de variables pour basculer entre les menus et le gameplay reste la norme pour garder un code propre sur PICO-8.
*   **Nettoyage mémoire :** Réinitialiser les tableaux (`tirs = {}`) est une bonne pratique indispensable pour éviter les comportements imprévisibles lors des transitions de niveaux.
*   **Évolutivité :** Ce système est une base solide ; il sera très simple, dans les prochains épisodes, d'ajouter des comportements complexes (mouvements, patterns de tir) à ces vagues.

{{< footer >}}
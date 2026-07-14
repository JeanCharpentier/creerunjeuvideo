---
title: "17. Création de mouvements pour vos ennemis"
weight: 17
date: 2023-10-27
categories: ['Pico-8']
tags: ['tutoriel', 'gamedev', 'space-invaders', 'programmation']
images: ["https://img.youtube.com/vi/QZVACYRSKt8/maxresdefault.jpg"]
---

Dans ce nouvel épisode de notre série dédiée à la création d'un *Space Invaders* sur Pico-8, nous nous attaquons à une mécanique fondamentale : le déplacement des ennemis. Pour rester fidèle au classique de l'arcade, nous allons implémenter un système où les ennemis se déplacent horizontalement, descendent d'un cran lorsqu'ils atteignent le bord de l'écran, puis changent de direction.

{{< youtube-rgpd "QZVACYRSKt8" >}}

### Résumé de l'implémentation
*   **Initialisation :** Création des variables `mv_time` (timer), `dir` (direction : 1 ou -1) et `bord` (indicateur de collision avec les bords).
*   **Logique de déplacement :** Utilisation d'un timer basé sur les FPS (30 par défaut) pour cadencer le mouvement.
*   **Gestion des bords :** Si un ennemi touche le bord, on active le flag `bord`, on inverse la direction (`dir *= -1`) et on déplace tout le groupe vers le bas.
*   **Condition de défaite :** Si un ennemi atteint la position Y de l'interface (108 pixels), le jeu se réinitialise et bascule sur l'écran "Game Over".
*   **Optimisation :** Utilisation de la multiplication par `dir` pour inverser le mouvement sans multiplier les conditions `if`.

### Ce qui reste d'actualité aujourd'hui
*   **La puissance des tableaux :** La manipulation des listes d'ennemis via `foreach` reste la méthode la plus efficace et la plus propre pour gérer des groupes d'objets dans Pico-8.
*   **La gestion des états (Game States) :** Séparer la logique de jeu (jeu en cours vs game over) est une bonne pratique indispensable pour tout projet, même simple.
*   **Le "Game Feel" :** Anticiper les prochaines étapes (animations de sprites, particules d'explosion, *camera shake*) est ce qui transforme un simple exercice de code en un véritable jeu vidéo gratifiant.

{{< footer >}}
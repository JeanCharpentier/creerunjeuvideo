---
title: "13. Création de l''écran Game Over"
weight: 13
date: 2024-05-22
categories: ['Pico-8']
tags: ['tutoriel', 'gamedev', 'pico8', 'game-over', 'state-machine']
images: ["https://img.youtube.com/vi/3YG6W5Yrgac/maxresdefault.jpg"]
---

Dans cet épisode, nous finalisons la boucle de gameplay en ajoutant l'écran de "Game Over". C'est une étape cruciale pour rendre votre jeu complet, permettant au joueur de comprendre qu'il a perdu et de relancer une partie proprement.

{{< youtube-rgpd "3YG6W5Yrgac" >}}

### Résumé de l'épisode
*   **Structure du Game Over :** Création d'un nouvel onglet dédié avec ses propres fonctions `init_go`, `update_go` et `draw_go`.
*   **Gestion des Game States :** Utilisation d'une variable `game_state` (0 pour le menu, 1 pour le jeu, 2 pour le Game Over) pour basculer entre les écrans.
*   **Réinitialisation complète :** Nettoyage des tableaux (`bullets`, `enemies`), remise à zéro du score et réinitialisation des points de vie du joueur.
*   **Refactorisation :** Création d'une fonction `create_enemies()` pour pouvoir générer une nouvelle vague d'ennemis à chaque nouvelle partie sans accumuler d'erreurs de positionnement.

### Ce qui reste d'actualité aujourd'hui
*   **La machine à états (State Machine) :** Utiliser une variable d'état reste la méthode la plus propre et la plus simple pour gérer les différents écrans dans PICO-8.
*   **Le nettoyage des données :** Il est fondamental de vider vos tableaux d'objets (`bullets = {}`) avant de relancer une partie pour éviter les comportements erratiques ou les fuites de mémoire.
*   **Modularité du code :** Déplacer la logique de création d'objets dans des fonctions dédiées (comme `create_enemies`) facilite grandement la maintenance et la réutilisation du code.
*   **Gestion des variables globales :** N'oubliez jamais de réinitialiser vos variables de position (comme `ex` et `ey` dans l'exemple) à chaque nouvelle initialisation, sinon vos objets apparaîtront à des endroits décalés à chaque nouvelle partie.

{{< footer >}}
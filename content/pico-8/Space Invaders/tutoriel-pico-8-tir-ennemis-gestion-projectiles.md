---
title: "10. Tirer avec les ennemis et gestion des projectiles"
weight: 10
date: 2023-10-27
categories: ['Pico-8']
tags: ['tutoriel', 'gamedev', 'pico-8', 'programmation']
images: ["https://img.youtube.com/vi/XpDhbc151tA/maxresdefault.jpg"]
---

Dans cet épisode, nous passons à une étape cruciale pour donner du dynamisme à notre jeu de type *space shooter* : permettre aux ennemis de riposter ! Nous allons aborder la centralisation du code de tir, la gestion des projectiles par "parentalité" et l'optimisation de nos boucles de mise à jour.

{{< youtube-rgpd "XpDhbc151tA" >}}

### Résumé de l'épisode
*   **Optimisation du flux :** Modification du `game_state` pour démarrer directement en jeu et gagner du temps lors des tests.
*   **Centralisation :** Déplacement de la logique de tir (`update_shoot`) dans un onglet dédié pour éviter la duplication de code entre le joueur et les ennemis.
*   **Système de "Parentalité" :** Ajout d'une propriété `parent` aux projectiles pour identifier leur origine (joueur ou ennemi) et gérer dynamiquement leur direction et leurs collisions.
*   **Gestion des ennemis :** Ajout d'une cadence de tir (`cd_ennemis`) et d'un timer individuel pour chaque ennemi afin qu'ils puissent tirer de manière autonome.
*   **Nettoyage mémoire :** Mise en place d'une condition pour supprimer les projectiles lorsqu'ils sortent de l'écran (vers le haut ou vers le bas) afin d'éviter les fuites de mémoire.

### Ce qui reste d'actualité aujourd'hui
*   **La modularité :** Utiliser des fonctions centralisées pour les mécaniques répétitives (comme le tir) est une règle d'or pour maintenir un projet propre sur Pico-8.
*   **La gestion des objets :** L'utilisation de tables pour stocker les entités (joueur, ennemis, tirs) et leurs propriétés (`x`, `y`, `w`, `h`) permet une évolutivité simple du code.
*   **Le débogage :** Apprendre à lire les messages d'erreur (ex: `attempt to perform arithmetic on field 'w' (a nil value)`) est indispensable pour identifier rapidement les variables non initialisées.
*   **Prochaines étapes :** Le système de "parentalité" est la base parfaite pour implémenter prochainement la gestion des points de vie (HP) et les écrans de Game Over.

{{< footer >}}
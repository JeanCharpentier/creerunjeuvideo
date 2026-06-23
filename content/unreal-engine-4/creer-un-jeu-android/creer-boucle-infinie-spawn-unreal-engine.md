---
title: "16. Créer une boucle infinie de spawn d''objets"
weight: 16
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprints', 'GameDev', 'Spawner', 'Logique']
---

Dans ce seizième épisode, nous allons aborder une problématique essentielle pour tout jeu de type "Runner" ou jeu d'arcade : comment faire en sorte que notre système de spawn ne s'arrête jamais ? Nous allons transformer notre séquence limitée en une boucle infinie grâce à la logique conditionnelle dans les Blueprints.

{{< youtube-rgpd "" >}}

### Résumé de la mise en place
Pour automatiser le cycle de spawn de nos troncs, nous avons suivi ces étapes clés :

*   **Création d'une variable de contrôle :** Ajout d'une variable `MaxSpawn` (Integer) pour définir le nombre d'éléments par cycle.
*   **Utilisation d'une condition (Branch) :** Insertion d'un nœud `Branch` après l'Event Tick pour vérifier si l'index actuel est inférieur au maximum autorisé.
*   **Logique de réinitialisation :** Si la condition est fausse (le cycle est terminé), nous réinitialisons `IndexSpawn` à 0 pour relancer la boucle.
*   **Configuration dans l'éditeur :** Ne pas oublier de définir la valeur par défaut de `MaxSpawn` dans les détails du Blueprint, sans quoi la condition sera toujours nulle.

### Ce qui reste d'actualité aujourd'hui
Bien que cet épisode utilise l'`Event Tick` pour gérer le spawn, les concepts fondamentaux restent parfaitement valides dans les versions récentes d'Unreal Engine (UE5 inclus) :

1.  **La logique de boucle :** Le principe de comparer un index à une valeur maximale est la base de tout système de gestion de vagues d'ennemis ou d'objets.
2.  **L'importance des variables éditables :** Exposer des variables comme `MaxSpawn` permet de modifier le gameplay (difficulté, fréquence) directement depuis l'éditeur sans toucher au code.
3.  **La gestion des états :** Comprendre quand "reset" une variable est crucial pour éviter les bugs de logique où le jeu semble "bloqué" (comme nous l'avons vu avec la valeur à 0).
4.  **Optimisation :** Si l'utilisation de l'`Event Tick` est idéale pour débuter, gardez à l'esprit qu'à mesure que votre jeu grandit, l'utilisation de **Timers** est souvent plus performante pour éviter de surcharger le processeur à chaque frame.

{{< footer >}}
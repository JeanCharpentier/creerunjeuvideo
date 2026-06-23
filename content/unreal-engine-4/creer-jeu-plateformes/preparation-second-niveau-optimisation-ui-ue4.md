---
title: "45. Préparation du second niveau et optimisation de l''UI"
weight: 45
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['GameDev', 'Blueprints', 'UI', 'LevelDesign', 'Optimisation']
---

Dans cet épisode, nous faisons une pause dans la complexité technique pour préparer la structure de notre second niveau. L'objectif est de valider que nos systèmes de gameplay (checkpoints, zones de mort, collecte de pièces) sont modulaires et réutilisables. Nous en profitons également pour refactoriser l'affichage de notre interface utilisateur (UI) afin de la rendre globale et automatique.

{{< youtube-rgpd "Dwvj7pZCShw" >}}

### Résumé de l'épisode
*   **Modularité des assets :** Création d'un second niveau en réutilisant les blueprints existants (pièces, checkpoints, zones de kill).
*   **Refactorisation de l'UI :** Déplacement de la logique d'affichage du widget (Create Widget / Add to Viewport) du *Level Blueprint* vers le *Character Blueprint*.
*   **Avantage de l'approche :** En plaçant l'UI dans le personnage, celle-ci s'initialise automatiquement à chaque chargement de niveau, évitant de dupliquer du code dans chaque *Level Blueprint*.
*   **Constat technique :** Le score actuel est local au niveau. Le passage d'un niveau à l'autre réinitialise les variables, ce qui introduit la nécessité d'un système de persistance de données (GameInstance).

### Ce qui reste d'actualité aujourd'hui
Bien que cet épisode se concentre sur Unreal Engine 4, les principes fondamentaux abordés restent des piliers du développement sous Unreal Engine 5 :

1.  **La centralisation de la logique :** Déplacer la logique d'UI du *Level Blueprint* vers le *Character* ou le *PlayerController* est une bonne pratique. Le *Level Blueprint* doit être réservé aux événements spécifiques à un niveau donné, et non à la gestion globale du joueur.
2.  **Réutilisabilité des Blueprints :** La création de classes parentes ou de composants réutilisables pour les checkpoints et les objets à collecter est la base d'un workflow efficace. Cela permet de modifier le comportement de tous les objets d'un type donné en une seule fois.
3.  **La gestion de l'état du jeu :** La problématique soulevée ici — le fait que les variables soient réinitialisées lors du changement de niveau — est un problème classique. La solution, que nous aborderons bientôt, réside dans l'utilisation de la `GameInstance`, qui est la seule classe capable de survivre au changement de niveau.

{{< footer >}}
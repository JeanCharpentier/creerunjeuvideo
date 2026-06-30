---
title: "10. Implémenter un Dash dynamique dans Unreal Engine 4"
weight: 10
date: 2026-06-17
categories: ['GameDev']
tags: ['Unreal Engine 4', 'FPS', 'Blueprints', 'Gameplay']
---

Dans cet épisode de notre série dédiée à la création d'un FPS sur Unreal Engine 4, nous allons ajouter une mécanique essentielle pour dynamiser vos déplacements : le **Dash**. Ce mouvement rapide permet d'esquiver les tirs ou de parcourir des distances en un clin d'œil, tout en intégrant un système de "cooldown" pour éviter les abus.

{{< youtube-rgpd "6LAiahvECdU" >}}

### Résumé du tutoriel
*   **Configuration des Inputs** : Ajout d'une action "Dash" dans les *Project Settings* (assignée par défaut à la touche Ctrl).
*   **Gestion des variables** : Création d'une variable booléenne `PeutDacher` pour contrôler l'état du joueur.
*   **Initialisation** : Sauvegarde des valeurs de vitesse et d'accélération de base au `BeginPlay` pour pouvoir les restaurer après le dash.
*   **Logique du Dash** : 
    *   Utilisation d'un `Character Movement` pour booster temporairement l'accélération et la vitesse maximale.
    *   Utilisation d'une `Timeline` pour gérer la durée de l'impulsion.
    *   Application d'une force directionnelle via `Add Movement Input` basé sur le vecteur avant (`Forward Vector`) du personnage.
*   **Cooldown** : Mise en place d'un délai de 5 secondes avant de réactiver la possibilité de dasher.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes d'Unreal Engine (UE5) proposent des outils comme le *Enhanced Input System* ou le *Motion Warping*, les principes fondamentaux expliqués ici restent parfaitement valides :
*   **La modularité des variables** : Stocker les valeurs de base (`Base Speed`, `Base Acceleration`) au démarrage est une bonne pratique pour éviter les bugs de valeurs "en dur" lors de modifications ultérieures.
*   **Le contrôle d'état** : L'utilisation de booléens pour verrouiller des capacités est la base du développement de systèmes de jeu robustes.
*   **L'utilisation des Timelines** : Elles restent un outil extrêmement puissant et visuel pour gérer des transitions de valeurs dans le temps sans alourdir le code avec des `Tick` complexes.

{{< footer >}}
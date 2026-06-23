---
title: "22. Création du menu principal et gestion de l''interface"
weight: 22
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['UI', 'Widget', 'Menu', 'Blueprint', 'GameDev']
---

Dans ce nouvel épisode de notre série sur Unreal Engine 4, nous allons mettre en place la porte d'entrée de votre jeu : le menu principal. L'objectif est de créer une interface utilisateur (UI) fonctionnelle permettant de lancer la partie et de préparer l'accès futur à un système de classement (leaderboard).

{{< youtube-rgpd "" >}}

### Résumé des étapes clés
*   **Organisation des niveaux :** Renommage de votre carte de jeu actuelle en `Main Map` et création d'un nouveau niveau dédié au `Menu Principal`.
*   **Configuration du projet :** Ajustement des *Project Settings* pour définir la carte de démarrage par défaut.
*   **Création du Widget :** Utilisation de l'éditeur de Widget pour concevoir le menu avec deux boutons : "Jouer" et "Classement".
*   **Design et ancres :** Importance de bien configurer les ancres (anchors) pour que votre interface reste cohérente sur différentes résolutions d'écran.
*   **Optimisation des assets :** Rappel crucial sur l'utilisation de textures dont les dimensions sont des puissances de 2 (ex: 256x256, 512x1024) pour éviter des problèmes de rendu, surtout sur mobile.
*   **Programmation du menu :** 
    *   Utilisation du *Level Blueprint* pour afficher le widget au lancement (`Create Widget` + `Add to Viewport`).
    *   Activation du curseur de la souris via `Set Show Mouse Cursor` (en décochant *Context Sensitive* pour trouver la fonction).
    *   Liaison du bouton "Jouer" à l'action `Open Level`.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Unreal Engine aient évolué, les fondamentaux abordés ici restent le socle de toute interface utilisateur dans le moteur :
1.  **Le système de Widgets (UMG) :** La méthode de création d'interfaces via UMG n'a pas changé. La gestion des ancres et des variables reste la norme pour créer des interfaces responsives.
2.  **La gestion des entrées :** L'activation du curseur de la souris via le *Player Controller* est toujours la méthode standard pour les menus sur PC.
3.  **Optimisation des textures :** La règle des puissances de 2 est toujours une bonne pratique pour l'optimisation mémoire, particulièrement sur les plateformes mobiles (Android/iOS).
4.  **Modularité :** Séparer le menu principal du niveau de jeu est une architecture indispensable pour éviter de charger inutilement des ressources lourdes dès le lancement de l'application.

{{< footer >}}
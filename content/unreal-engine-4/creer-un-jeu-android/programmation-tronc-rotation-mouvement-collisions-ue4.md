---
title: "14. Programmation du tronc : Rotation, Mouvement et Collisions"
weight: 14
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprints', 'GameDev', 'Tutoriel', 'Gameplay']
---

Dans cet épisode, nous passons à la phase de programmation de notre "BP_Tronc". L'objectif est de donner vie à cet obstacle en le faisant tourner sur lui-même tout en le faisant avancer vers le joueur. Nous aborderons également l'optimisation des références et la configuration précise des collisions pour garantir une expérience de jeu fluide.

{{< youtube-rgpd "" >}}

### Résumé des étapes clés
*   **Initialisation propre :** Utilisation du `Event Begin Play` pour caster le joueur et stocker sa référence dans une variable dédiée. Cela évite de répéter l'opération à chaque frame.
*   **Organisation :** Utilisation des "Comment Boxes" (touche C) pour documenter le code et faciliter la relecture future.
*   **Rotation dynamique :** Utilisation de `AddWorldRotation` couplé à un `MakeRotator` et au `Delta Seconds` pour assurer une rotation fluide, indépendante du framerate.
*   **Mouvement :** Création d'une variable de type `Vector` nommée "Vitesse" pour piloter le déplacement de l'acteur via `AddWorldOffset`.
*   **Configuration des collisions :** Réglage des `Collision Presets` sur "Pawn" et activation de `Generate Overlap Events` pour que les boîtes de détection interagissent uniquement avec le joueur.

### Ce qui reste d'actualité aujourd'hui
Bien que cet épisode traite d'Unreal Engine 4, les concepts fondamentaux restent parfaitement transposables à Unreal Engine 5 :

1.  **Le Casting et les Variables :** La méthode de mise en cache (caching) des références (comme le `PlayerPawn`) est une bonne pratique de performance qui reste indispensable pour éviter de surcharger le processeur avec des recherches inutiles.
2.  **Delta Time :** L'utilisation du `Delta Seconds` pour les calculs de mouvement et de rotation est la base du développement de jeux. Sans cela, votre jeu tournerait plus ou moins vite selon la puissance de la machine de l'utilisateur.
3.  **Gestion des Collisions :** Le système de `Collision Presets` et de `Overlap Events` n'a pas changé dans sa logique. Comprendre comment filtrer les interactions (ignorer les murs, détecter le joueur) est une compétence transversale essentielle.
4.  **Propreté du Blueprint :** L'utilisation de commentaires et l'organisation des nœuds restent la règle d'or pour maintenir des projets complexes sur le long terme.

{{< footer >}}
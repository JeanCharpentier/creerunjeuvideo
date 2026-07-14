---
title: "5. Implémenter les collisions AABB sur PICO-8"
weight: 5
date: 2023-10-27
categories: ['GameDev']
tags: ['pico-8', 'tutoriel', 'lua', 'gamedev', 'collisions']
images: ["https://img.youtube.com/vi/T2d0-XYF2bE/maxresdefault.jpg"]
---

Bienvenue dans ce cinquième volet de notre série dédiée à la création d'un *Space Invaders-like* sur PICO-8. Après avoir structuré notre moteur de jeu, géré les tirs et les déplacements, il est temps d'aborder un pilier fondamental du développement de jeux vidéo : **la détection de collisions**.

Dans cet épisode, nous allons mettre en place un système de collision "AABB" (Axis-Aligned Bounding Box). C'est la méthode la plus efficace et la plus simple pour gérer les interactions entre les entités de votre jeu sans surcharger le processeur de la console virtuelle.

{{< youtube-rgpd "T2d0-XYF2bE" >}}

### Ce que nous avons couvert dans cet épisode :

*   **Comprendre le concept AABB :** Pourquoi utiliser des boîtes de collision (bounding boxes) plutôt que des calculs complexes de pixels ou de cercles.
*   **La logique mathématique :** Analyse des 4 conditions nécessaires pour vérifier si deux rectangles se chevauchent (ou, plus simplement, vérifier quand ils ne se touchent pas).
*   **Création de l'onglet `util` :** Centralisation de notre logique de collision pour garder un code propre et réutilisable.
*   **Mise à jour des structures de données :** Ajout des propriétés `w` (largeur) et `h` (hauteur) à nos objets `ennemis` et `tirs` pour permettre les calculs de collision.
*   **Intégration dans la boucle `update` :** Mise en place de la vérification de collision entre les projectiles et les ennemis, avec suppression automatique des objets lors de l'impact.

### Ce qui reste d'actualité aujourd'hui

La détection de collision AABB reste le standard absolu pour les jeux 2D rétro. Même dans des moteurs modernes comme Godot ou Unity, cette logique est souvent utilisée en interne pour les tests de collision de base. 

*   **Optimisation :** N'oubliez pas que vous pouvez limiter vos boucles de collision en ne testant que les objets proches ou en utilisant des grilles spatiales si votre nombre d'ennemis augmente drastiquement.
*   **Évolutivité :** Ce système est une base. Vous pourrez facilement le faire évoluer plus tard pour ajouter des effets visuels (particules d'explosion) ou des boîtes de collision plus petites que le sprite lui-même pour rendre le jeu plus "juste" pour le joueur.
*   **Débogage :** Comme vu dans la vidéo, si vos collisions ne fonctionnent pas, affichez les valeurs de vos variables (`w`, `h`, `x`, `y`) à l'écran avec `print()` pour identifier rapidement les erreurs de frappe ou les valeurs `nil`.

{{< footer >}}
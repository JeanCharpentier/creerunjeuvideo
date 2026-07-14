---
title: "9. Créer des téléporteurs fonctionnels"
weight: 9
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['FPS', 'Blueprint', 'GameDev', 'Téléportation']
images: ["https://img.youtube.com/vi/Glgdmv0lbpA/maxresdefault.jpg"]
---

Dans cet épisode de notre série dédiée à la création d'un FPS solo, nous allons aborder un mécanisme essentiel pour le level design : le système de téléportation. Que ce soit pour faciliter les déplacements sur de grandes cartes ou pour créer des puzzles environnementaux, les téléporteurs sont un outil indispensable.

{{< youtube-rgpd "Glgdmv0lbpA" >}}

### Résumé de la mise en place
Pour créer ce système, nous avons décomposé le travail en deux Blueprints distincts :

*   **BP_TP_Dest :** Un acteur simple contenant un composant `Arrow` (flèche). Il sert de point d'arrivée. La flèche permet de visualiser facilement la direction de sortie dans l'éditeur.
*   **BP_Teleporteur :** L'acteur principal. Il utilise une `Sphere Collision` pour détecter le joueur.
*   **Logique de téléportation :**
    *   Utilisation de l'événement `OnComponentBeginOverlap` sur la sphère.
    *   `Cast` vers le personnage joueur pour s'assurer que seul le joueur déclenche l'effet.
    *   Utilisation de la fonction `Teleport` intégrée à Unreal Engine.
    *   Mise en place d'une variable `Destination` (de type `BP_TP_Dest`) rendue éditable (`Instance Editable`) pour permettre de lier chaque téléporteur à sa cible directement dans le viewport.

### Ce qui reste d'actualité aujourd'hui
Bien que cet épisode utilise Unreal Engine 4, les concepts fondamentaux restent parfaitement valides pour les versions plus récentes (UE5) :

1.  **Modularité :** Séparer l'objet de déclenchement (le portail) de l'objet de destination (le point de sortie) est une bonne pratique qui permet une grande flexibilité dans le level design.
2.  **Gestion des collisions :** Le problème de "l'apparition dans le sol" est un classique. L'utilisation d'une capsule de collision pour prévisualiser la taille du joueur au point d'arrivée reste la méthode la plus fiable pour éviter que le personnage ne reste bloqué.
3.  **Conservation de la vélocité :** La fonction `Teleport` d'Unreal conserve naturellement l'élan du joueur, ce qui est crucial pour garder une sensation de fluidité dans un FPS rapide.
4.  **Variables éditables :** L'utilisation de références d'objets dans les détails de l'acteur est la méthode standard pour créer des systèmes "plug-and-play" sans avoir à coder en dur chaque connexion.

{{< footer >}}
---
title: "Maîtriser la caméra dans Unreal Engine 3 : Passer du FPS à la vue à la troisième personne"
date: 2026-06-17
categories: ['GameDev']
tags: ['Unreal Engine 3', 'Kismet', 'Camera', 'Level Design']
images: ["https://img.youtube.com/vi/32yl1pbx-6I/maxresdefault.jpg"]
---

Dans cet article, nous revenons sur une problématique classique pour les développeurs utilisant l'Unreal Engine 3 (UE3) : comment modifier la perspective par défaut du joueur. Si le moteur est nativement configuré pour le FPS (First Person Shooter), il est tout à fait possible de basculer vers une vue à la troisième personne ou une vue de dessus grâce à l'outil **Kismet**.

{{< youtube-rgpd "32yl1pbx-6I" >}}

### Résumé de la méthode
Pour modifier la caméra sans toucher au code source (UnrealScript), voici les étapes clés :

*   **Placement de la caméra :** Utilisez le *Content Browser* pour ajouter un `CameraActor` dans votre niveau. Positionnez-le manuellement selon l'angle souhaité.
*   **Utilisation de Kismet :** Ouvrez l'éditeur de script visuel pour créer un flux logique :
    *   **Événement :** `Player Spawn` (déclenché à l'apparition du joueur).
    *   **Variables :** Créez une variable `Player` et une variable `CameraActor`.
    *   **Actions :** Utilisez `Attach to Actor` pour lier la caméra au joueur, puis `Set Camera Target` pour forcer le moteur à utiliser cette caméra.
*   **Configuration du monde :** Pour éviter les conflits avec l'interface de tir (crosshair), accédez aux `World Properties` > `World Info` et cochez `No Default Inventory For Player`. Cela supprime les armes par défaut, idéal pour un jeu de plateforme ou d'exploration.

### Ce qui reste d'actualité aujourd'hui

Bien que l'Unreal Engine 3 soit désormais une technologie héritée (*legacy*), les concepts abordés ici restent fondamentaux pour comprendre le fonctionnement des moteurs modernes (UE4/UE5) :

1.  **La séparation entre le Pawn et la Camera :** Même dans les versions récentes, la gestion de la caméra est un système distinct du personnage. Comprendre comment "attacher" une vue à un acteur est la base de tout système de caméra cinématique ou de jeu à la troisième personne.
2.  **Le Scripting Visuel :** Kismet est l'ancêtre direct des **Blueprints**. La logique de nœuds (Events, Actions, Variables) que vous apprenez ici est exactement la même que celle utilisée aujourd'hui dans l'UE5.
3.  **Le prototypage rapide :** La méthode présentée ici est parfaite pour le *blockout* ou le prototypage rapide. Avant de coder un système de caméra complexe en C++ ou en Blueprint, tester une vue fixe via un acteur de caméra permet de valider immédiatement le "game feel" d'un niveau.
4.  **La gestion des World Properties :** La notion de configuration globale de la scène (World Settings) reste le lieu privilégié pour définir les règles de base de votre gameplay (inventaire, mode de jeu, paramètres de rendu).

{{< footer >}}
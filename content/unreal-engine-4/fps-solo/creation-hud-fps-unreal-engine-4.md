---
title: "3. Création d''une interface HUD pour votre FPS"
weight: 3
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['GameDev', 'UE4', 'HUD', 'Widget', 'Blueprint']
images: ["https://img.youtube.com/vi/jhiP_tJ5xLE/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/jhiP_tJ5xLE/maxresdefault.jpg"]
---

Dans ce troisième volet de notre série dédiée à la création d'un FPS sur Unreal Engine 4, nous allons aborder une étape cruciale pour l'immersion du joueur : l'affichage des informations à l'écran. Nous allons mettre en place un système de barres de progression (vie, armure, endurance) en utilisant les Widgets Blueprints.

{{< youtube-rgpd "jhiP_tJ5xLE" >}}

### Résumé du tutoriel
*   **Gestion des variables :** Création des variables `Vie`, `Armure` et `Endurance` (type *Float*) dans le *FirstPersonCharacter* et organisation via des catégories pour plus de clarté.
*   **Interface utilisateur (HUD) :** Création d'un *Widget Blueprint* et utilisation d'une *Vertical Box* pour aligner proprement les éléments.
*   **Barres de progression :** Intégration de trois *Progress Bars* avec une gestion dynamique de la taille via l'option "Fill".
*   **Binding (Liaison) :** Utilisation du système de *Binding* pour lier les valeurs des barres de progression aux variables du personnage via un *Cast to FirstPersonCharacter*.
*   **Affichage :** Utilisation de l'événement *Begin Play* dans le *Level Blueprint* pour instancier le widget et l'ajouter au viewport du joueur.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Unreal Engine aient évolué (notamment avec l'arrivée d'UE5), les fondamentaux présentés ici restent parfaitement valides :
*   **Le système de Widgets :** Le fonctionnement des *User Widgets* et des *Progress Bars* est identique dans les versions récentes.
*   **Le Binding :** La technique du *Binding* est toujours utilisée pour des interfaces simples, bien qu'il soit recommandé, pour des projets complexes, d'utiliser des *Property Bindings* ou des *Delegates* pour optimiser les performances (éviter le *Cast* à chaque frame).
*   **L'organisation :** L'utilisation de conteneurs comme la *Vertical Box* reste la meilleure pratique pour créer des interfaces responsives qui s'adaptent à toutes les résolutions d'écran.
*   **Le Cast :** Le *Cast to Character* reste une méthode standard pour accéder aux données du joueur depuis l'interface, bien que l'utilisation d'interfaces (Blueprints Interfaces) soit une alternative plus propre pour découpler votre code.

{{< footer >}}
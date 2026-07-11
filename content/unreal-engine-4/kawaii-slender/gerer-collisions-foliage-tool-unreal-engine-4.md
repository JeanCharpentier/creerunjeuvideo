---
title: "9. Gérer les collisions du Foliage Tool"
weight: 9
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Foliage', 'Collision', 'GameDev', 'Tutoriel']
images: ["https://img.youtube.com/vi/JhKVxSunK2s/maxresdefault.jpg"]
---

Dans ce neuvième épisode de notre série dédiée à Unreal Engine 4, nous nous attaquons à un problème classique : la traversée des objets. Lorsque vous utilisez le *Foliage Tool* pour peupler votre environnement, les arbres et rochers ajoutés sont souvent dépourvus de collisions par défaut. Résultat ? Votre personnage passe à travers comme un fantôme. Voici comment corriger cela en quelques clics.

{{< youtube-rgpd "JhKVxSunK2s" >}}

### Résumé du tutoriel
*   **Le problème :** Les éléments générés par le *Foliage Tool* ne bloquent pas le joueur par défaut.
*   **La solution :**
    1. Ouvrez l'outil **Foliage** dans votre éditeur.
    2. Sélectionnez chaque type de mesh (arbre, bûche, etc.) ajouté à votre liste.
    3. Dans le panneau des propriétés (en bas), cherchez la section **Collision**.
    4. Modifiez le paramètre de collision pour le régler sur **BlockAll**.
    5. Répétez l'opération pour tous les objets solides de votre scène.
*   **Astuce :** Ne vous souciez pas de l'herbe ou des petits végétaux, laissez-les sans collision pour optimiser les performances.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes d'Unreal Engine aient évolué, la gestion des collisions via le *Foliage Tool* reste fondamentale. Voici pourquoi cette méthode est toujours pertinente :
*   **Performance :** Gérer les collisions directement sur le mesh dans le Foliage est bien plus léger que de placer des *Blocking Volumes* manuellement partout sur la carte.
*   **Workflow :** Comprendre comment modifier les propriétés d'un asset au sein du Foliage est une compétence indispensable pour tout environnement artist.
*   **Flexibilité :** Vous pouvez choisir précisément quels éléments bloquent le joueur et lesquels sont purement décoratifs, ce qui est crucial pour le gameplay (ex: cacher un ennemi derrière un arbre solide).

{{< footer >}}
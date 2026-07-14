---
title: "20. Création et animation d''objets à ramasser"
weight: 20
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprint', 'Actor', 'Matériaux', 'Collision', 'Rotation']
images: ["https://img.youtube.com/vi/dfPQ3dpQ_-8/maxresdefault.jpg"]
---

Dans cet épisode, nous passons à une étape cruciale du développement de votre jeu : la création d'objets interactifs. Nous allons apprendre à concevoir une pièce (ou "collectible") en utilisant les Blueprints, à lui donner un aspect visuel attrayant via l'éditeur de matériaux, et à la rendre dynamique en la faisant tourner sur elle-même. Enfin, nous aborderons la gestion des collisions pour que le joueur puisse traverser l'objet sans être bloqué.

{{< youtube-rgpd "dfPQ3dpQ_-8" >}}

### Résumé de l'épisode
*   **Création de l'Actor :** Utilisation d'une classe `Actor` nommée "Zone Pièce" pour définir notre objet.
*   **Modélisation simple :** Ajout d'une composante `Sphere` et ajustement de son échelle pour simuler une pièce.
*   **Design visuel :** Création d'un matériau simple avec une couleur dorée, une valeur métallique élevée et une rugosité ajustée.
*   **Animation procédurale :** Utilisation du node `Event Tick` couplé à `Add Actor Local Rotation` pour faire pivoter la pièce en continu.
*   **Gestion des collisions :** Modification des paramètres de collision de `Block All` vers `Overlap All Dynamic` pour permettre au joueur de traverser l'objet tout en déclenchant des événements.

### Ce qui reste d'actualité aujourd'hui
Bien que cet épisode utilise Unreal Engine 4, les concepts fondamentaux restent identiques dans Unreal Engine 5 :
*   **Le système d'Actors :** La structure de base des objets dans le monde reste inchangée.
*   **L'Event Tick :** Bien qu'il faille l'utiliser avec parcimonie pour optimiser les performances (préférez les `Timelines` pour des animations fluides), le principe de rotation par frame reste une base solide pour débuter.
*   **Les collisions :** La distinction entre "Block" (collision physique solide) et "Overlap" (détection de zone) est un pilier du gameplay dans tous les jeux Unreal.
*   **Matériaux :** L'éditeur de matériaux (Material Editor) fonctionne sur les mêmes principes de nœuds, vous permettant de créer des shaders complexes très rapidement.

{{< footer >}}
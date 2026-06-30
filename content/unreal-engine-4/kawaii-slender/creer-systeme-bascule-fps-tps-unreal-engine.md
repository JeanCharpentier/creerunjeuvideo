---
title: "34. Créer un système de bascule entre vue FPS et TPS"
weight: 34
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprint', 'Camera', 'Gameplay', 'Tutoriel']
---

Dans cet épisode, nous abordons une fonctionnalité très demandée : comment permettre au joueur de basculer dynamiquement entre une vue à la première personne (FPS) et une vue à la troisième personne (TPS) en appuyant sur une simple touche.

{{< youtube-rgpd "P43Pz7odhXs" >}}

### Résumé du tutoriel
*   **Configuration des entrées :** Ajout d'un *Action Mapping* dans les *Project Settings* pour définir la touche de bascule (ex: touche '0' ou bouton de manette).
*   **Stockage de la position initiale :** Utilisation d'une variable de type *Vector* nommée `BaseCamera` pour mémoriser la position relative de la caméra au démarrage du jeu via l'événement *BeginPlay*.
*   **Logique de bascule :** Utilisation du nœud *Flip Flop* pour alterner entre deux états à chaque pression de touche.
*   **Manipulation de la caméra :** Utilisation du nœud *Set Relative Location* pour déplacer la caméra vers une position décalée (TPS) ou pour la ramener à sa position d'origine (FPS) en utilisant la variable stockée.

### Ce qui reste d'actualité aujourd'hui
Bien que ce tutoriel ait été réalisé sur une version ancienne d'Unreal Engine 4, les concepts fondamentaux restent parfaitement valables dans les versions récentes (UE4.27 ou même UE5) :
*   **Le système de Input :** Bien que l'Enhanced Input System soit désormais la norme, la logique de bascule via un *Flip Flop* reste une méthode rapide et efficace pour des prototypes.
*   **Manipulation des composants :** La gestion des *Relative Locations* est toujours la manière standard de positionner des caméras attachées à un *Character Blueprint*.
*   **Modularité :** L'utilisation de variables pour stocker des états (comme la position de base) est une bonne pratique de développement qui évite de coder des valeurs en dur (*hardcoding*) dans vos Blueprints.

{{< footer >}}
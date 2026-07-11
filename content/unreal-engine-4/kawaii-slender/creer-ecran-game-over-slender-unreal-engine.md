---
title: "24. Créer un écran de Game Over pour votre Slender"
weight: 24
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprints', 'UI', 'Slender', 'GameDev']
images: ["https://img.youtube.com/vi/lwjaOFhjXP0/maxresdefault.jpg"]
---

Dans ce nouvel épisode de notre série dédiée à la création d'un jeu de type "Slender", nous allons nous concentrer sur la fin de partie. L'objectif est simple : lorsqu'il vous attrape, le jeu doit s'arrêter, afficher un écran de Game Over et vous permettre de reprendre le contrôle via une interface utilisateur.

{{< youtube-rgpd "lwjaOFhjXP0" >}}

### Résumé du tutoriel
Dans cette vidéo, nous avons modifié la logique de notre IA (Slender) pour déclencher un événement de défaite :

*   **Nettoyage de la logique :** Suppression des anciennes variables de vision et de délai pour simplifier la détection de collision.
*   **Création du Widget :** Utilisation de `Create Widget` pour instancier notre interface "Game Over".
*   **Affichage et Pause :** Utilisation de `Add to Viewport` pour afficher l'interface, suivie de `Set Game Paused` pour figer le jeu.
*   **Gestion de l'UI :** Récupération de l'image de Game Over via le widget pour définir sa visibilité (`Set Visibility`).
*   **Interaction souris :** Activation du curseur via `Set Show Mouse Cursor` pour permettre au joueur de cliquer sur les boutons du menu.

### Ce qui reste d'actualité aujourd'hui
Bien que ce tutoriel utilise des mécaniques de base d'Unreal Engine 4, les concepts abordés restent fondamentaux pour n'importe quel projet sous Unreal Engine 5 :

1.  **Le système de Widgets (UMG) :** La méthode de création et d'affichage des interfaces utilisateur n'a pas changé. C'est toujours la base pour créer des menus interactifs.
2.  **Le contrôle de l'état du jeu :** L'utilisation de `Set Game Paused` couplée à `Set Show Mouse Cursor` est la norme pour gérer les menus de pause ou d'écran de fin de partie.
3.  **La communication Blueprint :** La logique de déclenchement par collision (Overlap) reste le moyen le plus efficace pour lancer des événements de gameplay (comme une mort ou une victoire) dans vos prototypes.

{{< footer >}}
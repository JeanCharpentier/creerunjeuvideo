---
title: "11. Gestion des tirs ennemis et préparation du Game Over"
weight: 11
date: 2024-05-22
categories: ['PICO-8']
tags: ['tutoriel', 'gamedev', 'lua', 'shmup']
images: ["https://img.youtube.com/vi/9DPgyq75ufk/maxresdefault.jpg"]
---

Dans cet épisode, nous poursuivons le développement de notre *Space Invaders* sur PICO-8. Après avoir implémenté les tirs du joueur, il est temps d'équilibrer le jeu en permettant aux ennemis de riposter. Nous allons voir comment gérer l'apparition des projectiles ennemis, ajuster leur positionnement et préparer la logique pour la défaite du joueur.

{{< youtube-rgpd "9DPgyq75ufk" >}}

### Résumé des points abordés
*   **Création des assets :** Mise en place d'un nouveau sprite (n°4) pour représenter les projectiles ennemis.
*   **Système de spawn dynamique :** Utilisation d'un objet intermédiaire (`spawn`) pour calculer intelligemment la position d'apparition des tirs selon qu'ils proviennent du joueur ou d'un ennemi.
*   **Gestion des sprites par type de tir :** Modification de la fonction `add` pour assigner dynamiquement le numéro de sprite au projectile lors de sa création.
*   **Refactorisation de `draw` :** Mise à jour de la boucle d'affichage pour que chaque tir utilise son propre sprite défini lors de son instanciation.
*   **Préparation à la défaite :** Mise en place des bases structurelles pour gérer les points de vie du joueur et l'écran de Game Over.

### Ce qui reste d'actualité aujourd'hui
*   **La modularité :** L'utilisation d'objets intermédiaires pour gérer les propriétés d'apparition (spawn) est une excellente pratique pour garder un code propre et évolutif.
*   **La maintenance du code :** Centraliser la logique de création des tirs dans une seule fonction `add` permet d'éviter les bugs de duplication et facilite l'ajout futur de nouveaux types d'armes ou d'ennemis.
*   **La gestion des sprites :** Associer les données visuelles (numéro de sprite) directement à l'objet dans la table des tirs est la méthode standard pour gérer des entités variées dans PICO-8.
*   **L'importance de l'anticipation :** Prévoir des variables de décalage (offset) dès le début permet d'ajuster le "feeling" du jeu sans avoir à réécrire toute la logique de collision ou d'affichage.

{{< footer >}}
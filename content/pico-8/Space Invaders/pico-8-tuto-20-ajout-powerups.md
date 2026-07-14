---
title: "20. Ajout de Power-ups (Vie et Score)"
weight: 20
date: 2024-05-22
categories: ['Pico-8']
tags: ['pico-8', 'gamedev', 'tutoriel', 'space-invaders']
images: ["https://img.youtube.com/vi/drB-zs1BzMs/maxresdefault.jpg"]
---

Dans ce 20ème épisode de notre série dédiée à la création d'un *Space Invaders-like* sur PICO-8, nous allons ajouter une dimension stratégique à notre jeu : les **Power-ups**. Bien que ce ne soit pas présent dans l'original, ces bonus permettent de dynamiser le gameplay en offrant au joueur des opportunités de survie et de progression rapide.

{{< youtube-rgpd "drB-zs1BzMs" >}}

### Au programme de ce tutoriel :
*   **Gestion des données :** Création d'un tableau `PUS` pour stocker les instances de bonus.
*   **Logique de création :** Mise en place d'une fonction `add_up` pour générer des bonus à la position d'un ennemi détruit.
*   **Types de bonus :**
    *   **Type 1 (Vert) :** Restauration d'un point de vie.
    *   **Type 2 (Jaune) :** Bonus de 10 points de score.
*   **Système de probabilités :** Utilisation de `flr(rnd(n))` pour définir des taux d'apparition différents selon le type de bonus.
*   **Nettoyage :** Suppression automatique des bonus sortant de l'écran pour optimiser les performances.

### Ce qui reste d'actualité aujourd'hui
*   **La modularité :** Utiliser des fonctions dédiées (`add_up`, `update_pus`, `draw_pus`) permet de garder un code propre et facile à maintenir, même sur une console limitée comme la PICO-8.
*   **Le "Game Feel" :** L'ajout de bonus aléatoires est une technique fondamentale pour briser la répétitivité d'un jeu de tir et récompenser le joueur.
*   **Optimisation :** La gestion des tableaux (suppression des éléments hors écran) reste une règle d'or pour éviter de saturer la mémoire et le processeur de la machine virtuelle.

{{< footer >}}
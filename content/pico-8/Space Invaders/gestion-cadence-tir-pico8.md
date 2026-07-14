---
title: "6. Gérer la cadence de tir dans PICO-8"
weight: 6
date: 2023-10-27
categories: ['PICO-8']
tags: ['tutoriel', 'gamedev', 'lua', 'programmation']
images: ["https://img.youtube.com/vi/4Ef4Drbp6nk/maxresdefault.jpg"]
---

Dans ce sixième épisode de notre série dédiée à la création d'un *Space Invaders-like* sur PICO-8, nous allons nous attaquer à un aspect crucial du gameplay : la cadence de tir. Jusqu'à présent, notre vaisseau tirait à chaque frame, ce qui sature rapidement la mémoire et rend le jeu trop facile. Apprenons à réguler cela grâce à un système de timer simple.

{{< youtube-rgpd "4Ef4Drbp6nk" >}}

### Résumé de l'épisode
*   **Refactorisation :** Création d'une fonction dédiée `tirer()` pour isoler la logique de création des projectiles.
*   **Gestion du temps :** Introduction d'une variable `temps` qui s'incrémente à chaque frame dans la boucle `_update()`.
*   **Logique de cadence :** Utilisation d'un calcul basé sur le framerate (30 FPS) pour déclencher le tir uniquement lorsque le compteur atteint un seuil défini par une variable `cadence`.
*   **Flexibilité :** Mise en place d'une structure permettant de régler facilement la vitesse de tir entre 1 et 30 tirs par seconde.

### Ce qui reste d'actualité aujourd'hui
*   **La séparation des responsabilités :** Créer des fonctions spécifiques (comme `tirer()`) est une bonne pratique indispensable pour garder un code lisible, même dans un projet aussi restreint que PICO-8.
*   **Les timers basés sur les frames :** La méthode utilisée ici (incrémenter un compteur et le réinitialiser) est le standard pour gérer des événements temporels dans les jeux 2D rétro.
*   **Adaptabilité au framerate :** Bien que nous travaillions en 30 FPS, comprendre que la logique de tir dépend du nombre d'images par seconde est essentiel si vous décidez un jour de passer votre jeu en 60 FPS.
*   **Optimisation mémoire :** En limitant la cadence, on évite de créer trop d'objets simultanément, ce qui préserve les ressources limitées de la console virtuelle.

{{< footer >}}
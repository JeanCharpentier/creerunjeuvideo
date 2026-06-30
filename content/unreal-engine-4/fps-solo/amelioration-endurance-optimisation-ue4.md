---
title: "5. Amélioration de l''endurance et optimisation"
weight: 5
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['FPS', 'Blueprint', 'Optimisation', 'HUD', 'Tutoriel']
---

Dans ce cinquième épisode de notre série dédiée à la création d'un FPS sur Unreal Engine 4, nous nous concentrons sur le peaufinage de notre système d'endurance. Grâce aux retours précieux de la communauté, nous allons corriger des comportements illogiques, optimiser nos performances et ajouter un retour visuel plus professionnel.

{{< youtube-rgpd "Ir1HW7VUPEw" >}}

### Au programme de cet épisode :

*   **Correction de mouvement :** Empêcher la consommation d'endurance lorsque le joueur est à l'arrêt.
*   **Optimisation des Timers :** Apprendre à utiliser les *Timer Handles* pour arrêter proprement les boucles et économiser des ressources.
*   **Lissage visuel (Smoothing) :** Utiliser l'interpolation linéaire (Lerp) pour rendre la barre d'endurance plus fluide.
*   **Feedback visuel :** Changer dynamiquement la couleur de la barre lorsque le joueur est épuisé.
*   **Refactorisation du HUD :** Mise en cache de la référence du joueur dans le widget pour éviter les appels répétitifs de `Cast`.

### Ce qui reste d'actualité aujourd'hui

Bien que cet épisode traite d'Unreal Engine 4, les concepts abordés restent des piliers fondamentaux du développement de jeux vidéo, quel que soit le moteur :

1.  **Gestion des entrées :** Vérifier l'état du mouvement avant de déclencher une action est une pratique standard pour éviter les bugs de logique.
2.  **Gestion des ressources :** L'utilisation des *Timer Handles* est toujours la méthode recommandée pour gérer les cycles de vie des fonctions répétitives. Laisser des timers tourner en arrière-plan inutilement est une source classique de perte de performance.
3.  **Interpolation (Lerp) :** Le lissage des valeurs (UI, caméra, mouvements) est essentiel pour donner un aspect "AAA" à votre projet. C'est une technique universelle en GameDev.
4.  **Optimisation UI :** Éviter les `Cast` dans le `Tick` d'un widget est une règle d'or. Enregistrer la référence du joueur lors de l'événement `Construct` est la manière la plus efficace de procéder.

{{< footer >}}
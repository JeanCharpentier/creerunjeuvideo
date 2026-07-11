---
title: "7. Implémenter le Wall Jump dans votre FPS"
weight: 7
date: 2026-06-17
categories: ['GameDev']
tags: ['Unreal Engine 4', 'FPS', 'Blueprint', 'Gameplay']
images: ["https://img.youtube.com/vi/a8yne_WenSA/maxresdefault.jpg"]
---

Dans cet épisode de notre série dédiée à la création d'un FPS sur Unreal Engine 4, nous allons aborder une mécanique essentielle pour donner du dynamisme à vos déplacements : le **Wall Jump**. Ce mouvement permet au joueur de rebondir sur les parois pour atteindre des zones en hauteur ou prendre l'avantage lors d'un combat rapide.

{{< youtube-rgpd "a8yne_WenSA" >}}

### Résumé de l'implémentation
Pour réaliser ce système sans utiliser les fonctions de saut natives (souvent trop limitées pour un FPS nerveux), nous avons suivi ces étapes :

*   **Nettoyage du système de saut :** Suppression de la fonction `Jump` native au profit de `Launch Character` pour un contrôle total de la vélocité.
*   **Gestion de l'état au sol :** Utilisation de `IsMovingOnGround` pour différencier le saut classique du saut aérien.
*   **Détection des murs :** Utilisation de `Capsule Trace By Channel` plutôt qu'un simple `Line Trace` pour détecter les parois autour du personnage avec précision.
*   **Calcul de la trajectoire :** Utilisation du `Forward Vector` et de l' `Impact Point` pour éjecter le joueur dans la direction opposée au mur.
*   **Contrôle du flux :** Réintégration du nœud `DoN` pour limiter le nombre de sauts autorisés avant de toucher à nouveau le sol.

### Ce qui reste d'actualité aujourd'hui
Bien que cet article se base sur Unreal Engine 4, les principes fondamentaux restent parfaitement transposables à **Unreal Engine 5** :

1.  **La logique de "Launch Character" :** Cette fonction reste la méthode la plus fiable pour créer des mouvements de type "arcade" ou "fast-paced" car elle ignore les contraintes de friction et de gravité standard du Character Movement Component.
2.  **L'utilisation des Traces :** La `Capsule Trace` est toujours l'outil privilégié pour détecter des surfaces autour d'un personnage, car elle est plus robuste qu'un simple rayon (Line Trace) qui peut passer à travers des géométries fines.
3.  **Architecture Blueprint :** La séparation entre la logique d'entrée (Input Action) et la vérification d'état (Branch/Trace) est une bonne pratique de développement qui facilite le débogage et l'ajout de nouvelles mécaniques (comme le dash ou le double saut) sans casser le code existant.

{{< footer >}}
---
title: "12. Gestion des points de vie et interface utilisateur"
weight: 12
date: 2024-05-22
categories: ['Pico-8']
tags: ['tutoriel', 'gamedev', 'lua', 'pico-8']
images: ["https://img.youtube.com/vi/YVv5SAG7z_4/maxresdefault.jpg"]
---

Bienvenue dans ce douzième épisode de notre série dédiée à l'apprentissage de Pico-8 ! Après avoir corrigé nos exercices précédents, nous entrons dans le vif du sujet : la survie. Dans cet épisode, nous allons implémenter un système de points de vie pour notre joueur et apprendre à les afficher dynamiquement sur notre interface (HUD).

{{< youtube-rgpd "YVv5SAG7z_4" >}}

### Ce que nous avons appris dans cet épisode :

*   **Initialisation des PV :** Ajout d'une variable `vie` directement dans l'objet `player` (fixée à 3 par défaut).
*   **Logique de dégâts :** Modification de la fonction de collision pour décrémenter les points de vie lors d'un impact avec un tir ennemi.
*   **Sécurité du code :** Mise en place d'une condition pour éviter que les points de vie ne deviennent négatifs.
*   **Affichage HUD :** Création d'une interface simple utilisant des rectangles (`rectfill`) pour représenter visuellement les points de vie restants.
*   **Débogage :** Utilisation de la console pour vérifier en temps réel l'état de nos variables avant de passer à l'affichage graphique.

### Ce qui reste d'actualité aujourd'hui

*   **La simplicité avant tout :** Bien que l'utilisation de conditions `if` successives ne soit pas la méthode la plus "évolutive" (comparée à une boucle `for` ou à une gestion par tableau), elle reste une excellente approche pédagogique pour débuter sans complexifier inutilement le code.
*   **Modularité :** Séparer la gestion des points de vie de la logique du "Game Over" permet de garder un code propre et facile à maintenir.
*   **Flexibilité visuelle :** L'utilisation de `rectfill` peut être facilement remplacée par des `spr()` (sprites) pour donner un aspect plus rétro et soigné à votre interface sans changer la logique sous-jacente.
*   **Prochaine étape :** La gestion des états de jeu (`Game State`) pour déclencher un écran de "Game Over" propre lorsque les points de vie atteignent zéro.

{{< footer >}}
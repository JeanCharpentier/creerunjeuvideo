---
title: "8. Gestion avancée des ennemis et difficulté dynamique"
weight: 8
date: 2023-10-27
categories: ['Tutoriels GDevelop']
tags: ['GDevelop 5', 'GameDev', 'Survival', 'Tutoriel']
---

Bienvenue dans ce huitième volet de notre série dédiée à la création d'un jeu de type "Survival" sur GDevelop 5. Aujourd'hui, nous attaquons le cœur du système : la génération procédurale des ennemis, la montée en difficulté et l'utilisation de variables pour rendre votre jeu évolutif.

{{< youtube-rgpd "KYVF-NKtV_w" >}}

### Ce que vous allez apprendre dans cet épisode :
*   **Gestion des ennemis via des tableaux :** Stocker vos types d'ennemis dans une variable globale pour les appeler dynamiquement.
*   **Système de Spawner :** Créer un chronomètre de scène pour cadencer l'apparition des vagues.
*   **Difficulté progressive :** Augmenter le nombre d'ennemis et réduire le temps d'apparition à chaque montée de niveau.
*   **Trigonométrie simplifiée :** Utiliser les fonctions `Cos` et `Sin` pour faire apparaître vos ennemis en cercle autour du joueur, peu importe sa position.
*   **Optimisation :** Limiter le nombre d'ennemis actifs pour préserver les performances de votre jeu.

### Ce qui reste d'actualité aujourd'hui
Les concepts abordés ici sont fondamentaux pour n'importe quel jeu de survie ou de type "Bullet Heaven". La méthode consistant à utiliser des tableaux (`ListEnnemis`) et des index de difficulté (`indexDifficulté`) est une pratique propre qui permet de faire évoluer votre jeu sans avoir à réécrire tout votre code. Même si la trigonométrie peut sembler intimidante au premier abord, elle devient un outil puissant une fois que vous avez compris la logique du cercle trigonométrique : le `Cos` pour l'axe horizontal (X) et le `Sin` pour l'axe vertical (Y).

{{< footer >}}
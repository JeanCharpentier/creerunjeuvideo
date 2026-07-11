---
title: "10. Créer des ennemis avec un mouvement sinusoïdal"
weight: 10
prev_url: "/game-maker-studio/shoot-them-up/optimiser-vagues-ennemis-game-maker-escadrilles/"
next_url: "/game-maker-studio/shoot-them-up/creer-ennemi-tir-laser-gamemaker-studio/"
date: 2023-10-27
categories: ['Archive']
tags: ['GameMaker', 'Tutoriel', 'Game Development', 'GML']
images: ["https://img.youtube.com/vi/KMUlQOwbJkw/maxresdefault.jpg"]
---

Apprenez à dynamiser vos jeux en créant des ennemis aux trajectoires complexes grâce aux fonctions mathématiques intégrées de GameMaker.

{{< youtube-rgpd "KMUlQOwbJkw" >}}

### Résumé des notions clés

Dans ce tutoriel, nous explorons comment passer d'un mouvement linéaire simple à une trajectoire fluide et cyclique pour vos ennemis :

*   **Initialisation des variables :** Création de variables personnalisées (`frequence`, `amplitude`, `timer`) pour contrôler le comportement du mouvement.
*   **Utilisation de la fonction `sin()` :** Application de la trigonométrie pour calculer une position Y oscillante en fonction du temps.
*   **Gestion du temps :** Utilisation d'un `timer` incrémenté à chaque `step` pour animer le mouvement de manière fluide.
*   **Duplication de logique :** Optimisation du workflow en dupliquant des objets existants (`spawner`) pour créer de nouvelles vagues d'ennemis rapidement.
*   **Enchaînement de vagues :** Utilisation de l'événement `Destroy` pour déclencher l'apparition automatique d'un nouveau spawner une fois la vague précédente terminée.
*   **Positionnement hors-champ :** Technique pour faire apparaître des ennemis à des coordonnées spécifiques en dehors de la zone de jeu visible.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions de GameMaker aient évolué, les principes fondamentaux abordés ici restent des piliers du développement de jeux 2D :

1.  **La puissance des mathématiques :** La fonction `sin()` (sinus) est toujours l'outil standard pour créer des mouvements naturels, des effets de flottement ou des trajectoires de projectiles sans avoir recours à des animations complexes.
2.  **Modularité du code :** La séparation des responsabilités entre l'objet "ennemi" (qui gère son propre mouvement) et l'objet "spawner" (qui gère la logique de vague) est une excellente pratique d'architecture logicielle.
3.  **Gestion d'état :** L'utilisation d'événements comme `Destroy` pour déclencher des événements futurs est une méthode propre et efficace pour gérer le rythme de progression d'un niveau (game pacing).
4.  **Optimisation :** Apprendre à manipuler les coordonnées X et Y pour faire apparaître des objets hors écran est essentiel pour créer des jeux fluides sans temps de chargement visibles.

{{< footer >}}
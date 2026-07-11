---
title: "4. Créer le mouvement et l''IA des joueurs"
weight: 4
date: 2024-05-22
categories: ['Tutoriels']
tags: ['GDevelop', 'GameDev', 'Babyfoot', 'IA', 'Mouvement']
images: ["https://img.youtube.com/vi/QZrJDOstYNY/maxresdefault.jpg"]
---

Dans cet épisode de notre série "Babyfoot 2026", nous allons donner vie à notre terrain. Un baby-foot statique, c'est bien, mais un baby-foot dynamique, c'est mieux ! Nous allons apprendre à automatiser le mouvement de nos joueurs (PNG) et à programmer une intelligence artificielle basique pour notre gardien afin qu'il puisse intercepter la balle.

{{< youtube-rgpd "QZrJDOstYNY" >}}

### Au programme de cet épisode :
*   **Organisation des objets :** Création d'un groupe "PNG" pour gérer nos joueurs automatiquement.
*   **Positionnement initial :** Utilisation des variables `startX` et `Line` pour placer nos joueurs sur le terrain.
*   **Mouvement sinusoïdal :** Utilisation de la fonction mathématique `sin()` couplée à `TimeFromStart()` pour créer un mouvement de va-et-vient fluide.
*   **IA du gardien :** Utilisation de l'interpolation linéaire (`lerp`) pour permettre au gardien de suivre la position de la balle en temps réel.

### Ce qui reste d'actualité aujourd'hui
*   **La puissance des groupes :** Regrouper vos objets permet d'appliquer des actions à plusieurs entités simultanément, ce qui est indispensable pour optimiser vos événements.
*   **Les fonctions mathématiques :** Le sinus reste l'outil le plus simple et le plus efficace pour créer des mouvements répétitifs sans avoir recours à des chemins complexes.
*   **L'interpolation (Lerp) :** C'est la technique standard pour obtenir des mouvements fluides et naturels. Que ce soit pour une caméra, un menu ou une IA, le `lerp` est votre meilleur allié pour éviter les déplacements "robotiques".
*   **Gestion de la difficulté :** En jouant sur les paramètres de vitesse (le facteur dans le `lerp` ou l'amplitude du sinus), vous pouvez facilement créer différents niveaux de difficulté pour vos joueurs.

{{< footer >}}
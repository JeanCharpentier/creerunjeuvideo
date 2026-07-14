---
title: "8. Création sonore et musicale sur PICO-8"
weight: 8
date: 2024-05-22
categories: ['PICO-8']
tags: ['tutoriel', 'gamedev', 'audio', 'musique', 'sfx']
images: ["https://img.youtube.com/vi/ouRhGNG-TuE/maxresdefault.jpg"]
---

Bienvenue dans ce huitième épisode de notre série dédiée à l'apprentissage de PICO-8. Après avoir exploré le code et les sprites, il est temps de s'attaquer à un pilier fondamental de l'immersion : le son et la musique. Si, comme moi, vous n'êtes pas musicien, ne paniquez pas : PICO-8 propose des outils accessibles qui permettent de faire illusion rapidement.

{{< youtube-rgpd "ouRhGNG-TuE" >}}

### Résumé de l'épisode
*   **Mise à jour :** Pensez à vérifier votre version de PICO-8 (actuellement 0.2.7) pour profiter des dernières fonctionnalités, notamment sur la gestion des textes.
*   **L'éditeur SFX :** C'est ici que tout commence. On y définit les formes d'ondes, la vitesse et la hauteur des notes pour créer des effets sonores (tirs, collisions) ou des boucles mélodiques.
*   **L'éditeur de musique :** Il permet d'assembler vos différents SFX sur 4 canaux simultanés (batterie, basse, mélodie, etc.) pour composer vos morceaux.
*   **Gestion des boucles :** Apprenez à utiliser les icônes de contrôle (Stop, Boucle) pour gérer l'enchaînement et la répétition de vos pistes musicales.
*   **Intégration dans le code :** Utilisation des fonctions `sfx(n)` pour déclencher un effet sonore et `music(n)` pour lancer une composition.

### Ce qui reste d'actualité aujourd'hui
*   **L'importance de la communauté :** La musique reste le défi numéro 1 pour les développeurs solo. N'hésitez pas à consulter les ressources communautaires (tutoriels YouTube spécialisés) pour approfondir la théorie musicale appliquée au tracker de PICO-8.
*   **La logique des 64 slots :** PICO-8 offre 64 emplacements pour les SFX et 64 pour les patterns musicaux. Cette limite est une contrainte créative qui force à l'optimisation.
*   **Workflow :** La méthode consistant à créer des "ingrédients" (SFX) avant de les assembler (Musique) reste la manière la plus efficace de travailler sur la console virtuelle.

{{< footer >}}
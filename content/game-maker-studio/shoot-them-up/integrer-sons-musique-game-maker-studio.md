---
title: "18. Intégrer les sons et la musique"
weight: 18
prev_url: "/game-maker-studio/shoot-them-up/animer-effets-visuels-game-maker-explosions/"
next_url: "/game-maker-studio/shoot-them-up/guide-exporter-jeu-gamemaker-studio/"
date: 2023-10-27
categories: ['Archive']
tags: ['Game Maker', 'Tutoriel', 'Audio', 'Developpement de jeux']
images: ["https://img.youtube.com/vi/QaBsdnFBQYI/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/QaBsdnFBQYI/maxresdefault.jpg"]
---

Apprendre à gérer l'ambiance sonore est une étape cruciale pour donner vie à votre projet : découvrez comment implémenter les effets de tir, les explosions et la musique de fond dans Game Maker Studio.

{{< youtube-rgpd "QaBsdnFBQYI" >}}

### Résumé des notions clés

*   **Lecture audio de base** : Utilisation de la fonction `audio_play_sound(soundID, priority, loop)` pour déclencher vos fichiers audio.
*   **Gestion des variables audio** : Stocker le son dans une variable (ex: `var snd = audio_play_sound(...)`) permet de manipuler ses propriétés en temps réel.
*   **Ajustement du volume (Gain)** : Utilisation de `audio_sound_gain(soundID, volume, time)` pour régler l'intensité sonore (de 0 à 1) et le temps de transition.
*   **Bouclage de musique** : Activation du paramètre `loop` à `true` pour les musiques de fond afin qu'elles se répètent en continu.
*   **Bonnes pratiques** : L'importance de commenter son code pour faciliter la relecture et la maintenance du projet.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions de Game Maker aient évolué, les principes fondamentaux de la gestion audio restent identiques. La fonction `audio_play_sound` demeure le standard pour déclencher des effets sonores. La capacité à manipuler le gain dynamiquement est une compétence essentielle pour créer des environnements sonores immersifs, notamment pour gérer la distance entre la caméra et la source sonore ou pour créer des fondus (fades) lors des transitions de scènes. Maîtriser ces fonctions de base vous offre une base solide pour intégrer des systèmes audio plus complexes, comme les groupes audio ou les effets de filtres, disponibles dans les versions les plus récentes du moteur.

{{< footer >}}
---
title: "29. Intégration sonore et Sound Cues"
weight: 29
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['GameDev', 'Audio', 'Blueprint', 'SoundCue', 'KawaiiSlender']
images: ["https://img.youtube.com/vi/lVwGLSWO6A8/maxresdefault.jpg"]
---

Dans cet avant-dernier tutoriel de la série "Kawaii Slender", nous abordons une étape cruciale pour l'immersion : l'ambiance sonore. Un jeu sans son est une expérience incomplète ; c'est le design audio qui donne vie à votre environnement et renforce la tension face à votre antagoniste.

{{< youtube-rgpd "lVwGLSWO6A8" >}}

### Résumé des étapes clés
*   **Importation des assets :** Organisation des fichiers audio dans un dossier dédié et importation des sons (respiration, cri, ambiance).
*   **Play Sound 2D :** Utilisation du node `Play Sound 2D` pour déclencher le cri du Slender lors de l'attaque, indépendamment de la position spatiale.
*   **Spawn Sound Attached :** Utilisation de `Spawn Sound Attached` pour lier le son de respiration au Mesh du personnage, permettant au son de suivre le joueur.
*   **Création de Sound Cues :** Utilisation de l'éditeur de *Sound Cue* pour gérer des comportements complexes comme le bouclage (looping) d'une ambiance sonore ou la limitation de la polyphonie (éviter que le son de respiration ne se superpose à l'infini).
*   **Gestion de la concurrence :** Configuration des paramètres de *Max Concurrent Play Count* pour garantir une expérience propre et éviter les saturations sonores.

### Ce qui reste d'actualité aujourd'hui
Bien que cet article traite d'Unreal Engine 4, les concepts fondamentaux présentés ici restent parfaitement valables pour Unreal Engine 5 :
*   **La puissance des Sound Cues :** Bien qu'UE5 introduise le système *MetaSounds* (plus performant et flexible), les *Sound Cues* restent un outil rapide et efficace pour des besoins simples d'ambiance ou de déclencheurs ponctuels.
*   **La gestion des composants :** La logique de lier un son à un composant (Mesh) via `Spawn Sound Attached` est une pratique standard qui permet une gestion propre des sons 3D dans l'espace.
*   **L'importance de l'optimisation :** La gestion de la concurrence sonore (ne pas jouer 10 fois le même son en même temps) est une règle d'or du Game Design, quel que soit le moteur utilisé, pour éviter la fatigue auditive du joueur et les problèmes de mixage.

{{< footer >}}
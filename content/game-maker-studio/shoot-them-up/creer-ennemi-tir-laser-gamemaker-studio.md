---
title: "11. Créer un ennemi avec tir laser"
weight: 11
prev_url: "/game-maker-studio/shoot-them-up/creer-ennemis-mouvement-sinusoidal-gamemaker/"
next_url: "/game-maker-studio/shoot-them-up/gerer-collisions-destruction-ennemis-gamemaker/"
date: 2024-05-22
categories: ['Archive']
tags: ['GameMaker', 'Tutoriel', 'GameDev', 'Gamedev-debutant']
images: ["https://img.youtube.com/vi/QvGxIZWXvA0/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/QvGxIZWXvA0/maxresdefault.jpg"]
---

Dans ce tutoriel, nous allons enrichir votre jeu en ajoutant un troisième type d'ennemi capable de tirer des projectiles laser, tout en automatisant son apparition via un système de "spawner" dynamique.

{{< youtube-rgpd "QvGxIZWXvA0" >}}

### Résumé des notions clés

*   **Duplication et héritage :** Utiliser la fonction "Duplicate" sur des sprites et objets existants pour gagner du temps et conserver une structure cohérente.
*   **Manipulation de sprites :** Utilisation des outils *Mirror Flip* pour l'orientation et *Colorize* (swap color) pour créer des variantes visuelles rapidement.
*   **Logique de tir :** Création d'un objet laser dédié avec une vitesse négative (`hspeed = -2`) pour se déplacer vers la gauche, en direction du joueur.
*   **Gestion des alarmes :** Ajustement de la cadence de tir en modifiant le multiplicateur de la `room_speed` dans l'événement *Alarm*.
*   **Spawning dynamique :** Utilisation de la fonction `random()` pour varier la position verticale (`y`) des ennemis et rendre les vagues moins prévisibles.
*   **Chaînage de vagues :** Déclenchement de l'apparition d'un nouveau spawner juste avant la destruction du précédent pour créer une progression fluide.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions de GameMaker aient évolué, les principes fondamentaux abordés ici restent le cœur du développement 2D :

1.  **La réutilisation de code :** La duplication d'objets et la modification de paramètres spécifiques (vitesse, cadence) est une pratique standard pour maintenir un projet propre et éviter la redondance.
2.  **La gestion du temps :** Le système d'alarmes reste la méthode la plus simple et efficace pour gérer des événements répétitifs (tirs, apparitions) sans alourdir l'événement *Step*.
3.  **Le "Game Feel" par l'aléatoire :** L'utilisation de fonctions de hasard pour le placement des ennemis est une technique intemporelle pour éviter que le joueur ne mémorise par cœur les patterns et pour augmenter la rejouabilité.
4.  **Workflow efficace :** La manipulation directe des propriétés d'instance via le code (comme le `hspeed` ou le `y`) est toujours la base de la programmation dans GameMaker, que vous utilisiez le GML (GameMaker Language) ou le GML Visual.

{{< footer >}}
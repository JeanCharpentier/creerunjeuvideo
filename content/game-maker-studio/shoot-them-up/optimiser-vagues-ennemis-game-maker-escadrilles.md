---
title: "9. Créer des escadrilles et limiter le spawn"
weight: 9
prev_url: "/game-maker-studio/shoot-them-up/creer-ennemis-spawn-dynamique-gamemaker/"
next_url: "/game-maker-studio/shoot-them-up/creer-ennemis-mouvement-sinusoidal-gamemaker/"
date: 2023-10-27
categories: ['Archive']
tags: ['Game Maker Studio', 'Gamedev', 'Tutoriel', 'Programmation']
images: ["https://img.youtube.com/vi/AHREtn2lelI/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/AHREtn2lelI/maxresdefault.jpg"]
---

Dans ce tutoriel, nous allons apprendre à structurer l'apparition de vos ennemis pour rendre votre jeu plus dynamique en créant des escadrilles et en limitant le nombre de vagues.

{{< youtube-rgpd "AHREtn2lelI" >}}

### Résumé des notions clés

*   **Création d'escadrilles :** Au lieu de faire apparaître un seul objet, nous dupliquons la fonction `instance_create` dans l'alarme du spawner pour générer trois vaisseaux simultanément.
*   **Gestion des coordonnées (X, Y) :** En modifiant les offsets (décalages) des coordonnées X et Y, nous créons une formation en "V" pour un rendu visuel plus professionnel.
*   **Variables de comptage :** Utilisation d'une variable (`nbne1`) initialisée à 0 dans l'événement *Create* pour suivre le nombre de vagues générées.
*   **Incrémentation :** Utilisation de l'opérateur `++` (ex: `nbne1++`) pour ajouter 1 à la variable à chaque déclenchement de l'alarme.
*   **Logique de fin de vague :** Utilisation de l'événement *Step* pour vérifier en temps réel si le nombre de vagues souhaité est atteint, déclenchant ainsi la destruction du spawner via `instance_destroy()`.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions de Game Maker aient évolué, les concepts abordés ici restent les piliers du développement de jeux 2D :

1.  **La gestion des instances :** La manipulation des coordonnées relatives pour créer des formations reste la méthode la plus efficace pour gérer des groupes d'ennemis sans surcharger la room.
2.  **L'utilisation des alarmes :** C'est toujours le moyen le plus propre pour gérer le timing dans Game Maker, évitant ainsi de surcharger l'événement *Step* avec des compteurs complexes.
3.  **La logique conditionnelle :** L'utilisation de l'événement *Step* pour surveiller des variables globales ou locales est une pratique standard pour gérer les transitions de niveaux ou les changements d'état du jeu.
4.  **Optimisation du code :** L'usage de l'opérateur d'incrémentation (`++`) est une bonne habitude de syntaxe GML (GameMaker Language) qui rend votre code plus lisible et concis, une pratique toujours recommandée pour les projets de grande envergure.

{{< footer >}}
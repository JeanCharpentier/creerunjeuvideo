---
title: "17. Créer des explosions dynamiques"
weight: 17
prev_url: "/game-maker-studio/shoot-them-up/gerer-score-affichage-game-over-gamemaker/"
next_url: "/game-maker-studio/shoot-them-up/integrer-sons-musique-game-maker-studio/"
date: 2023-10-27
categories: ['Archive']
tags: ['Game Maker', 'Tutoriel', 'Animation', 'Game Design', 'Developpement de jeux']
---

Apprenez à donner vie à vos combats en ajoutant des effets d'explosion animés et en gérant leur cycle de vie pour un rendu professionnel.

{{< youtube-rgpd "NSc3FpzcLsw" >}}

### Résumé des notions clés

Pour transformer un simple sprite statique en un effet visuel dynamique, voici les étapes essentielles abordées dans ce tutoriel :

*   **Création d'animation par étapes :** Utilisation de la fonction *Set Length* pour définir le nombre de frames d'un sprite.
*   **Transformation progressive :** Utilisation de l'outil *Scale* pour modifier la taille des frames individuellement (en veillant à décocher "Apply to All Images").
*   **Gestion du cycle de vie :** Utilisation de l'événement *Animation End* pour déclencher une action une fois l'animation terminée.
*   **Nettoyage de la mémoire :** Emploi de la fonction `instance_destroy()` pour supprimer l'objet explosion après son affichage, évitant ainsi les fuites de mémoire.
*   **Instanciation dynamique :** Utilisation de `instance_create(x, y, obj)` pour faire apparaître l'effet visuel précisément à l'endroit de la collision.

### Ce qui reste d'actualité aujourd'hui

Bien que les interfaces de Game Maker aient évolué vers des versions plus modernes (GMS2/GMS 2023+), les concepts fondamentaux présentés ici restent le socle de tout développement 2D :

1.  **La gestion des ressources :** La logique de destruction d'instance (`instance_destroy`) est toujours la méthode standard pour gérer les effets éphémères (particules, explosions, impacts).
2.  **La séparation des responsabilités :** Le fait de créer un objet dédié à l'explosion plutôt que de gérer l'animation directement dans l'ennemi permet une meilleure modularité et facilite la réutilisation de l'effet sur différents types d'ennemis.
3.  **L'optimisation :** Comprendre comment ne pas laisser d'objets inutiles en mémoire est une compétence cruciale pour maintenir un framerate stable, quel que soit le moteur utilisé.

{{< footer >}}
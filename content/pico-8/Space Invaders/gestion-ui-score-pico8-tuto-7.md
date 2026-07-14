---
title: "7. Gestion de l''interface utilisateur (UI) et du score"
weight: 7
date: 2023-10-27
categories: ['Pico-8']
tags: ['tutoriel', 'gamedev', 'lua', 'ui', 'score']
images: ["https://img.youtube.com/vi/MFsvSsqe6Jc/maxresdefault.jpg"]
---

Dans ce septième épisode de notre série sur Pico-8, nous délaissons temporairement la musique pour nous concentrer sur un élément crucial de tout jeu : l'interface utilisateur (UI). Nous allons apprendre à afficher un score dynamique et à créer une barre d'interface simple pour rendre notre *Space Invaders-like* plus professionnel.

{{< youtube-rgpd "MFsvSsqe6Jc" >}}

### Résumé de la mise en place
*   **Structure du code :** Création d'un nouvel onglet `UI` avec ses propres fonctions `init_ui()`, `update_ui()` et `draw_ui()`.
*   **Logique de mise à jour :** Appel de `update_ui()` à la fin de la fonction `_update()` principale pour s'assurer que toutes les données (score, vie) sont bien à jour avant l'affichage.
*   **Affichage graphique :** Utilisation de `rectfill()` pour dessiner une barre de fond et de la fonction `print()` pour afficher le texte et la valeur du score.
*   **Gestion des variables :** Le score est stocké dans la table `player` pour une meilleure organisation.
*   **Astuce de debug :** Attention à l'utilisation de `print()` sans paramètres de position, qui peut hériter des couleurs et coordonnées des appels précédents.

### Ce qui reste d'actualité aujourd'hui
*   **Modularité :** Séparer son code par onglets (ou fichiers) reste la meilleure pratique pour ne pas se perdre dans un projet qui grandit.
*   **Ordre d'exécution :** L'ordre `init` -> `update` -> `draw` est le pilier fondamental de la boucle de jeu sur Pico-8.
*   **Conversion de type :** L'utilisation de `tostr()` est indispensable pour convertir des variables numériques en chaînes de caractères afin de les afficher à l'écran.
*   **Simplicité avant tout :** Comme le montre l'exemple, des formes géométriques simples (`rectfill`) suffisent souvent à créer une interface lisible et efficace avant de passer à des sprites complexes.

{{< footer >}}
---
title: "4. Nettoyer et structurer son code sur PICO-8"
weight: 4
date: 2024-05-22
categories: ['Développement']
tags: ['pico-8', 'tutoriel', 'lua', 'organisation']
images: ["https://img.youtube.com/vi/f1reGPqWtjU/maxresdefault.jpg"]
---

Dans ce quatrième épisode, nous faisons une pause dans le développement pur de notre *shoot 'em up* pour nous concentrer sur une étape cruciale : l'organisation. Au fur et à mesure que le projet grandit, le code devient plus complexe à lire. Apprendre à cloisonner ses fonctionnalités est essentiel pour maintenir un projet propre et évolutif.

{{< youtube-rgpd "f1reGPqWtjU" >}}

### Résumé de l'épisode
*   **Utilisation des onglets :** Découverte du système d'onglets de PICO-8 pour séparer le code par entités (Joueur, Ennemis, Tirs).
*   **Nommage des onglets :** Astuce pour renommer ses onglets en utilisant un commentaire (`-- nom`) sur la première ligne de chaque page.
*   **Modularisation :** Déplacement des fonctions `init`, `update` et `draw` spécifiques au joueur dans son propre onglet.
*   **Appel des fonctions :** Rappel indispensable : PICO-8 ne connaît que les fonctions `_init`, `_update` et `_draw` globales. Il faut donc appeler manuellement nos fonctions personnalisées (ex: `update_player()`) à l'intérieur de ces boucles principales.
*   **Bonnes pratiques :** Importance de commenter son code et de garder une structure cohérente pour éviter les bugs de logique (comme l'ordre d'exécution des tirs).

### Ce qui reste d'actualité aujourd'hui
*   **La lisibilité avant tout :** Même sur une console limitée comme la PICO-8, la séparation des préoccupations (*Separation of Concerns*) facilite grandement le débogage.
*   **La gestion des onglets :** C'est la méthode standard pour gérer la taille limitée de l'éditeur de code. Bien nommer ses onglets permet de naviguer instantanément dans un projet complexe.
*   **La boucle principale :** Comprendre que PICO-8 exécute uniquement les fonctions systèmes (`_update`, `_draw`) reste la base fondamentale pour tout développeur débutant sur cette plateforme.
*   **L'ordre d'exécution :** L'importance de l'ordre des appels dans `_update` et `_draw` (ex: effacer l'écran avant de redessiner, traiter les entrées avant les collisions) est une règle d'or immuable en GameDev.

{{< footer >}}
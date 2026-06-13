---
title: "16. Gérer le score et l'affichage Game Over"
weight: 16
prev_url: "/game-maker-studio/shoot-them-up/gerer-afficher-score-global-gamemaker-studio/"
next_url: "/game-maker-studio/shoot-them-up/animer-effets-visuels-game-maker-explosions/"
date: 2023-10-27
categories: ['Archive']
tags: ['GameMaker', 'Tutoriel', 'Gamedev', 'Programmation']
---

Apprenez à dynamiser votre système de score en récompensant le joueur pour chaque ennemi détruit et à afficher le résultat final sur votre écran de Game Over.

{{< youtube-rgpd "JP9EpNKrGW8" >}}

### Résumé des notions clés

Dans ce tutoriel, nous abordons deux aspects fondamentaux de la gestion de score dans GameMaker :

*   **Incrémentation dynamique :** Utilisation de l'opérateur `+=` pour ajouter des points à une variable globale (`global.score`) lors de la collision entre un laser et un ennemi.
*   **Différenciation des récompenses :** Attribution de valeurs de points variables (25, 50, 75) selon le type d'ennemi éliminé pour enrichir le gameplay.
*   **Gestion des variables globales :** Comprendre comment stocker une valeur persistante qui peut être récupérée même après un changement de room.
*   **Affichage sur l'écran de fin :** Création d'un objet dédié (`obj_score_go`) pour capturer le score final et l'afficher via l'événement `Draw` sur la room de Game Over.
*   **Positionnement UI :** Utilisation de la fonction `draw_text` pour placer précisément le score au-dessus des éléments d'interface comme les boutons "Rejouer" ou "Quitter".

### Ce qui reste d'actualité aujourd'hui

Bien que les versions de GameMaker aient évolué, les principes fondamentaux présentés ici restent le socle de tout jeu arcade :

1.  **L'opérateur `+=` :** C'est une convention de programmation universelle en GML (GameMaker Language). Elle reste la méthode la plus propre et la plus efficace pour modifier une valeur existante sans alourdir votre code.
2.  **La puissance des variables globales :** L'utilisation de `global.` est toujours la méthode recommandée pour gérer des données qui doivent survivre au passage d'une room à une autre (comme le score, les vies ou les paramètres du joueur).
3.  **La séparation des responsabilités :** Créer un objet spécifique pour l'affichage du score (`obj_score_go`) est une bonne pratique de conception. Cela permet de garder votre logique d'interface propre et isolée de la logique de jeu pure, facilitant ainsi la maintenance et les modifications futures de votre UI.
4.  **L'événement Draw :** La gestion de l'affichage via l'événement `Draw` reste le standard pour dessiner du texte, des sprites ou des formes primitives à l'écran en temps réel.

{{< footer >}}
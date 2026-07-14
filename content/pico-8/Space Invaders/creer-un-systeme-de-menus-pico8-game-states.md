---
title: "9. Créer un système de menus avec les Game States"
weight: 9
date: 2023-10-27
categories: ['Pico-8']
tags: ['tutoriel', 'gamedev', 'lua', 'menu', 'gamestate']
images: ["https://img.youtube.com/vi/aYTscEZzhwo/maxresdefault.jpg"]
---

Dans ce neuvième épisode de notre série dédiée à PICO-8, nous passons à une étape cruciale pour structurer votre jeu : la création d'un menu principal. Pour gérer la transition entre l'écran de titre et le gameplay, nous allons mettre en place un système de "Game States" (états de jeu).

{{< youtube-rgpd "aYTscEZzhwo" >}}

### Résumé de l'épisode
*   **Nettoyage :** Mise en commentaire des tests audio précédents pour libérer de l'espace.
*   **Architecture :** Création d'un nouvel onglet `menu` avec ses fonctions `init_menu`, `update_menu` et `draw_menu`.
*   **Game States :** Utilisation d'une variable globale (`game_state`) pour basculer entre l'état "Menu" (0) et l'état "Jeu" (1).
*   **Logique de contrôle :** Implémentation d'une condition dans les fonctions `_update()` et `_draw()` principales pour n'exécuter que le code correspondant à l'état actuel.
*   **Interaction :** Utilisation de la touche `btn(4)` (bouton Z/O) pour déclencher le passage du menu vers le jeu.

### Ce qui reste d'actualité aujourd'hui
*   **La gestion des états :** La méthode des `game_state` reste la manière la plus simple et efficace pour gérer des écrans (menu, pause, game over, jeu) sans alourdir votre code.
*   **Optimisation des tokens :** Garder vos conditions `if` sur une seule ligne quand c'est possible est une excellente habitude pour rester sous la limite des 8192 tokens de PICO-8.
*   **Modularité :** Séparer votre code dans des onglets distincts (menu, joueur, ennemis) est indispensable pour maintenir un projet propre à mesure qu'il grandit.
*   **Évolutivité :** Ce système de `game_state` est facilement extensible. Si vous souhaitez ajouter un écran de "Game Over" ou un menu "Options" plus tard, il suffira d'ajouter une nouvelle valeur à votre variable et une nouvelle condition `elseif`.

{{< footer >}}
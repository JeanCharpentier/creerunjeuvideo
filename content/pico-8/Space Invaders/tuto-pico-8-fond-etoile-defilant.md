---
title: "16. Ajouter un fond étoilé défilant"
weight: 16
date: 2024-05-22
categories: ['Pico-8']
tags: ['tutoriel', 'gamedev', 'pico-8', 'background', 'lua']
images: ["https://img.youtube.com/vi/LVHjNJesUmo/maxresdefault.jpg"]
---

Dans ce seizième épisode de notre série sur PICO-8, nous allons passer à la partie visuelle pour donner un peu plus de profondeur à notre *Space Invaders-like*. L'objectif est simple : créer un système de fond étoilé défilant (parallaxe) pour rendre notre jeu plus dynamique et "photo-réaliste" pour l'époque.

{{< youtube-rgpd "LVHjNJesUmo" >}}

### Résumé du tutoriel
*   **Structure des données :** Création d'un nouvel onglet `background` pour gérer un tableau (`table`) contenant toutes les étoiles.
*   **Initialisation :** Utilisation d'une boucle `for` pour générer 30 étoiles avec des positions (X, Y) et des vitesses aléatoires.
*   **Gestion du mouvement :** Mise à jour de la position Y des étoiles dans la fonction `update` et réinitialisation en haut de l'écran lorsqu'elles dépassent 128 pixels.
*   **Rendu graphique :** Utilisation de la fonction `rectfill` (ou `rect`) pour dessiner chaque étoile sous forme de pixel coloré.
*   **Débogage :** Apprentissage de la lecture des erreurs de syntaxe (parenthèses oubliées, fautes de frappe dans les noms de fonctions).

### Ce qui reste d'actualité aujourd'hui
*   **La gestion des listes d'objets :** Le pattern "créer, mettre à jour, supprimer et recycler" est la base de tout système de particules ou de gestion d'ennemis dans PICO-8.
*   **Le découpage en onglets :** Garder son code propre en séparant la logique du fond d'écran (Background) du reste du jeu est une excellente pratique pour la maintenabilité.
*   **L'optimisation visuelle :** Ajouter des détails simples comme un fond en mouvement transforme radicalement le ressenti du joueur (le fameux "juice") sans surcharger le processeur de la console virtuelle.
*   **L'aléatoire contrôlé :** Utiliser `rnd()` avec des offsets (ex: `rnd(1.5) + 1.5`) permet de créer un mouvement naturel et non répétitif, essentiel pour éviter l'effet "grille" dans les jeux 2D.

{{< footer >}}
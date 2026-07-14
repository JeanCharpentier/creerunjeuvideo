---
title: "1. Créer et déplacer son premier personnage sur PICO-8"
weight: 1
date: 2023-10-27
categories: ['GameDev']
tags: ['pico-8', 'tutoriel', 'lua', 'débutant']
images: ["https://img.youtube.com/vi/glutCcmZlcY/maxresdefault.jpg"]
---

Bienvenue dans cette série dédiée à l'apprentissage de **PICO-8**, la console virtuelle "fantasy" qui fait battre le cœur des développeurs indépendants. Dans ce premier épisode, nous posons les bases indispensables : la création de votre premier sprite et la mise en place du système de déplacement.

{{< youtube-rgpd "glutCcmZlcY" >}}

### Résumé de l'épisode
*   **Gestion du projet** : Importance de sauvegarder régulièrement ses fichiers (ex: `tuto_0`, `tuto_1`) pour garder un historique de progression.
*   **Éditeur de Sprite** : Création du visuel du vaisseau et compréhension de la transparence (couleur noire).
*   **Structure du code** : Utilisation des trois fonctions vitales :
    *   `_init()` : Initialisation des variables.
    *   `_update()` : Logique du jeu (déplacements, entrées clavier).
    *   `_draw()` : Rendu graphique à l'écran.
*   **Déplacement** : Utilisation de la fonction `btn()` pour détecter les touches et modifier les coordonnées `PX` (position X) du joueur.
*   **Nettoyage** : Utilisation de `cls()` dans la fonction `_draw()` pour éviter les traînées visuelles à chaque frame.

### Ce qui reste d'actualité aujourd'hui
Même si PICO-8 évolue, les fondamentaux abordés ici sont le socle de tout développement sur cette plateforme :
*   **La boucle de jeu** : La séparation stricte entre la logique (`update`) et l'affichage (`draw`) reste la règle d'or pour maintenir un jeu fluide à 30 ou 60 FPS.
*   **La gestion des entrées** : La fonction `btn()` est toujours le moyen le plus direct et efficace pour gérer les contrôles simples.
*   **L'optimisation manuelle** : Contrairement aux moteurs modernes (Unity/Godot), PICO-8 vous oblige à gérer vous-même l'effacement de l'écran et le positionnement des objets, ce qui est une excellente école pour comprendre le fonctionnement interne d'un moteur de jeu.
*   **L'importance de l'indentation** : Bien que l'éditeur soit minimaliste, structurer son code avec des tabulations reste indispensable pour la lisibilité, surtout quand le projet gagne en complexité.

{{< footer >}}
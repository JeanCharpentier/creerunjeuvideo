---
title: "3. Création des projectiles et gestion des objets dans PICO-8"
weight: 3
date: 2024-05-22
categories: ['Développement de jeux']
tags: ['pico-8', 'tutoriel', 'lua', 'gamedev', 'space-invaders']
images: ["https://img.youtube.com/vi/3mIlj0iII7U/maxresdefault.jpg"]
---

Dans ce troisième épisode de notre série dédiée à la création d'un *Space Invaders* sur PICO-8, nous passons à l'étape cruciale de l'armement : le tir. Apprendre à gérer des projectiles, c'est comprendre comment manipuler des tableaux (tables) et nettoyer la mémoire pour éviter que votre jeu ne ralentisse.

{{< youtube-rgpd "3mIlj0iII7U" >}}

### Au programme de cet épisode :
*   **Initialisation des tirs :** Création d'une structure d'objet pour nos lasers (position X, Y et vitesse).
*   **Gestion des entrées :** Utilisation de `btn()` pour déclencher la création d'un projectile lors de l'appui sur une touche.
*   **Manipulation de tables :** Ajout des projectiles dans une liste (`add`) et affichage via une boucle `for`.
*   **Optimisation mémoire :** Mise en place d'un système de suppression (`del`) pour les projectiles sortant de l'écran afin de ne pas saturer le processeur.
*   **Correction de bugs :** Ajustement de l'ordre d'exécution dans la fonction `update()` pour éviter que les tirs ne soient décalés dès leur apparition.

### Ce qui reste d'actualité aujourd'hui
*   **La gestion des tables :** Le principe de `add(table, objet)` et `del(table, objet)` reste la méthode standard et la plus efficace pour gérer des entités dynamiques (balles, ennemis, particules) dans PICO-8.
*   **Le nettoyage (Garbage Collection) :** Supprimer les objets qui sortent du champ de vision est une règle d'or en développement sur console virtuelle. Cela permet de maintenir un framerate stable à 30 ou 60 FPS.
*   **La structure `update/draw` :** Séparer la logique de mouvement (calculs) de l'affichage (rendu) est indispensable pour garder un code propre et maintenable, même sur un projet aussi simple qu'un *Space Invaders*.
*   **Le versioning manuel :** Bien que PICO-8 possède des outils, la méthode de l'auteur (sauvegarder des versions incrémentales `projet_01`, `projet_02`, etc.) reste une excellente pratique pour les débutants afin de pouvoir revenir en arrière en cas de corruption de fichier ou d'erreur critique.

{{< footer >}}
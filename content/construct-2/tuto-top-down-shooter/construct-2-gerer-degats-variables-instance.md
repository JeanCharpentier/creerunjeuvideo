---
title: "4. Gérer les Dégâts et Introduire les Variables d'Instance"
weight: 4
prev_url: "/construct-2/tuto-top-down-shooter/creer-monstres-ia-simple-construct-2/"
next_url: "/construct-2/tuto-top-down-shooter/construct-2-munitions-rechargement-hud-statique/"
date: 2023-10-27
categories: ['Archive']
tags: ['Construct 2', 'Game Development', 'Variables', 'Instance Variables', 'Damage System', 'Tutoriel', 'HTML5 Game']
images: ["https://img.youtube.com/vi/TV3utJo2og0/maxresdefault.jpg"]
---
---
Dans ce quatrième épisode de notre série sur Construct 2, nous plongeons au cœur de la gestion des dégâts et de l'introduction des variables d'instance pour rendre nos interactions de jeu plus dynamiques et réalistes.

{{< youtube-rgpd "TV3utJo2og0" >}}

### Résumé de l'épisode : Gérer les Dégâts et les Variables d'Instance

Cet épisode clé nous guide à travers l'implémentation d'un système de dégâts et l'utilisation des variables, des concepts fondamentaux en développement de jeux.

*   **Introduction aux Variables d'Instance**
    *   **Définition** : Les variables sont des valeurs qui peuvent être modifiées par le jeu et pendant le jeu, par opposition aux constantes qui restent fixes.
    *   **Utilité** : Elles sont essentielles pour gérer les états dynamiques des objets (points de vie, dégâts, scores, etc.).
*   **Configuration des Variables pour les Objets du Jeu**
    *   **Joueur (Marine)** : Ajout d'une variable d'instance `Vie_Joueur` (type: Nombre, valeur initiale: 100).
    *   **Ennemi (Mob)** : Ajout de deux variables d'instance :
        *   `Degats_Mob` (type: Nombre, valeur initiale: 5) pour les dégâts infligés au joueur.
        *   `Vie_Mob` (type: Nombre, valeur initiale: 10) pour les points de vie du mob.
    *   **Balle (Bullet)** : Ajout d'une variable d'instance `Degats_Balle` (type: Nombre, valeur initiale: 5) pour les dégâts infligés aux mobs.
    *   **Types de Variables** : Construct 2 propose des types "Nombre", "Booléen" (vrai/faux) et "Texte".
    *   **Modification** : Les variables d'instance sont ajoutées et modifiées via le panneau des propriétés de chaque objet.
*   **Logique des Événements pour les Dégâts et la Mort**
    *   **Joueur touché par un Mob** :
        *   **Mort du joueur** : Si `Marine` entre en collision avec `Mob` ET `Vie_Joueur` est inférieure ou égale à `Mob.Degats_Mob`, alors `Destroy Marine`.
        *   **Perte de vie** : Si `Marine` entre en collision avec `Mob`, alors `Marine: Soustraire de Vie_Joueur` la valeur de `Mob.Degats_Mob`.
    *   **Mob touché par une Balle** :
        *   **Mort du mob** : Si `Bullet` entre en collision avec `Mob` ET `Vie_Mob` est inférieure ou égale à `Bullet.Degats_Balle`, alors `Destroy Mob` et `Destroy Bullet`.
        *   **Perte de vie du mob** : Si `Bullet` entre en collision avec `Mob`, alors `Mob: Soustraire de Vie_Mob` la valeur de `Bullet.Degats_Balle`, puis `Destroy Bullet`.
*   **Affichage de la Vie du Joueur (HUD)**
    *   **Création** : Ajout d'un objet `Text` sur le layout (calque HUD).
    *   **Mise à jour** : Dans l'événement `System: Every Tick`, ajouter l'action `Text: Set text` à la valeur de `Marine.Vie_Joueur` pour un affichage en temps réel.
*   **Suivi de Caméra sur le Joueur**
    *   **Implémentation** : Dans l'événement `System: Every Tick`, ajouter l'action `System: Scroll to object (Marine)` pour que la caméra suive le joueur.
*   **Organisation des Événements**
    *   **Regroupement** : Brève introduction à l'organisation des événements en groupes pour une meilleure lisibilité et gestion du projet.

### Ce qui reste d'actualité aujourd'hui

Bien que ce tutoriel utilise Construct 2, les concepts abordés sont des piliers du développement de jeux et restent pleinement pertinents, quel que soit le moteur ou le langage utilisé :

*   **Variables d'Instance (ou Propriétés d'Objet)** : C'est un concept fondamental. Dans Unity, Godot, Unreal Engine ou même en programmation pure (C++, Python), chaque instance d'un objet peut avoir ses propres propriétés (variables) qui définissent son état unique (sa vie, sa position, sa couleur, etc.). Comprendre leur rôle est essentiel pour créer des jeux dynamiques.
*   **Systèmes de Dégâts et de Santé** : La logique de soustraction de points de vie, la vérification d'un seuil de mort (vie <= 0 ou vie <= dégâts entrants), et la destruction de l'objet sont des mécanismes universels. La manière de les implémenter peut varier (scripts, blueprints, événements visuels), mais le principe reste le même.
*   **Affichage Dynamique de l'Interface Utilisateur (HUD)** : Mettre à jour des éléments visuels (barres de vie, scores, compteurs) en temps réel en fonction des variables du jeu est une pratique courante pour informer le joueur. Cela se fait via des Canvas UI dans Unity, des Control Nodes dans Godot, ou des widgets dans Unreal.
*   **Logique Conditionnelle** : L'utilisation de conditions (`If`, `Else If`, `Else`, opérateurs de comparaison comme `<=`, `==`, `>`) est la base de toute programmation. Les événements de Construct 2 illustrent parfaitement comment ces conditions structurent le comportement du jeu.
*   **Gestion de Caméra** : Le suivi de caméra (`Scroll to object`) est un mécanisme essentiel pour de nombreux types de jeux. Des systèmes plus avancés incluent des zones mortes, des interpolations douces ou des caméras cinématiques, mais le principe de base est de maintenir le joueur à l'écran.
*   **Organisation du Code/des Événements** : Regrouper les événements ou le code par fonctionnalité (joueur, ennemis, UI) est une bonne pratique pour maintenir un projet propre, lisible et facile à déboguer, quel que soit l'outil.

Ces notions sont des fondations solides pour quiconque souhaite se lancer dans le développement de jeux, et les apprendre avec Construct 2 offre une excellente porte d'entrée visuelle et intuitive.

{{< footer >}}
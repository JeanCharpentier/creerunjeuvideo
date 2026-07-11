---
title: "1. Créer un jeu de Babyfoot 3D avec GDevelop 5"
weight: 1
date: 2023-10-27
categories: ['Tutoriels']
tags: ['GDevelop', '3D', 'Tutoriel', 'GameDev']
---

Bienvenue dans cette nouvelle série de tutoriels dédiée à la création d'un jeu de **Babyfoot en 3D** avec GDevelop 5. Dans ce premier épisode, nous posons les fondations du projet en configurant la scène, les caméras et le système de contrôle des joueurs.

{{< youtube-rgpd "eQAwY2zmyEo" >}}

### Ce que vous allez apprendre dans cet épisode :
*   **Utilisation d'un Starter Pack :** Comment importer un projet pré-configuré avec des objets 3D (terrain, joueurs, balle, cages).
*   **Gestion des caméras 3D :** Mise en place d'un système de caméra qui suit un objet cible ("Camera Center") pour une meilleure gestion de la profondeur.
*   **Architecture orientée multijoueur :** Structurer le code dès le début avec des variables d'instance pour faciliter une future transition vers le multijoueur en ligne.
*   **Contrôles tactiles/souris :** Création d'une zone de contrôle ("Player Controller") pour déplacer les joueurs de manière fluide sans décrochage.
*   **Contraintes physiques :** Utiliser l'action "Séparer deux objets" pour éviter que les joueurs ne traversent les bordures du terrain.

### Ce qui reste d'actualité aujourd'hui
Bien que GDevelop évolue rapidement, les concepts abordés ici restent des piliers fondamentaux pour tout projet 3D :
*   **L'organisation des scènes :** L'utilisation de dossiers et de variables globales/d'instance est toujours la meilleure pratique pour garder un projet propre.
*   **La gestion des caméras :** La technique de "regarder un objet" est la méthode la plus efficace pour créer des cinématiques ou des vues de jeu dynamiques en 3D.
*   **L'anticipation du multijoueur :** Réfléchir à l'architecture de vos variables dès le début du développement vous fera gagner des dizaines d'heures de refactorisation si vous décidez d'ajouter une dimension réseau plus tard.
*   **Le système de contrôle :** L'utilisation d'objets invisibles comme "zones de contrôle" est une astuce classique pour gérer les entrées tactiles sur mobile de manière précise.

{{< footer >}}
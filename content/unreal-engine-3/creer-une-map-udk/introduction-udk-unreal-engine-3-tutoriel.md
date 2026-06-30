---
title: "1. Introduction à l''Unreal Development Kit (UDK) et l''Unreal Engine 3"
weight: 1
date: 2026-06-17
categories: ['GameDev']
tags: ['Unreal Engine 3', 'UDK', 'Tutoriel', 'Level Design']
---

Bienvenue dans cette rétrospective technique dédiée à l'**Unreal Development Kit (UDK)**, la porte d'entrée historique vers l'Unreal Engine 3. Si vous avez toujours voulu comprendre comment les classiques comme *Gears of War* ou *Mirror's Edge* ont été bâtis, cet article vous plonge dans les fondamentaux du moteur qui a révolutionné l'industrie du jeu vidéo au début des années 2010.

{{< youtube-rgpd "fQYLSl3yjLs" >}}

### Résumé de l'épisode
Dans cette première leçon, nous abordons les bases de la création de niveaux sous UDK :
*   **Présentation de l'interface :** Gestion des quatre vues (Perspective, Top, Side, Front) pour une manipulation précise dans l'espace 3D.
*   **Configuration du projet :** Création d'une "Blank Map" et paramétrage des outils de travail.
*   **Le système de "Brushes" (Brosses) :** Utilisation des formes primitives (cubes, cylindres) pour sculpter l'architecture de base.
*   **Opérations CSG (Constructive Solid Geometry) :** Apprentissage des fonctions *Add* et *Subtract* pour ajouter de la matière ou creuser des espaces.
*   **Manipulation et alignement :** Utilisation du *Snap to Grid* pour garantir une géométrie propre et éviter les erreurs de texture ou les trous dans la map.

### Ce qui reste d'actualité aujourd'hui
Bien que l'Unreal Engine 5 soit désormais la norme, les concepts enseignés dans l'UDK restent les piliers du métier de Level Designer :
1.  **Le Blockout :** La méthode de création par "brosses" (ou *Geometry Scripting* dans UE5) est toujours la première étape pour valider le gameplay d'un niveau avant d'ajouter les assets finaux.
2.  **La rigueur de la grille :** Travailler avec un *Snap to Grid* est une règle d'or pour assurer la compatibilité des textures et la navigation fluide des bots (IA).
3.  **La logique des vues :** La maîtrise des vues orthogonales reste indispensable pour aligner les éléments complexes avec précision, une compétence que même les outils modernes ne remplacent pas totalement.
4.  **L'architecture modulaire :** Comprendre comment assembler des pièces pour former une structure cohérente est la base de tout environnement 3D professionnel.

{{< footer >}}
---
title: "0. Introduction à la création d''armes pour Unreal Engine 3 (UDK)"
weight: 0
date: 2026-06-17
categories: ['GameDev', 'Unreal Engine 3']
tags: ['UDK', 'Blender', 'Modélisation', 'Tutoriel']
images: ["https://img.youtube.com/vi/bOT3cdvahUQ/maxresdefault.jpg"]
---

Bienvenue dans cette série dédiée à l'Unreal Development Kit (UDK), la version emblématique de l'Unreal Engine 3 qui a marqué toute une génération de développeurs indépendants. Dans ce premier épisode, nous posons les bases de notre workflow : transformer un concept brut en une arme fonctionnelle intégrée directement dans le moteur.

{{< youtube-rgpd "bOT3cdvahUQ" >}}

### Résumé du projet
Dans cette série, nous allons couvrir l'intégralité du pipeline de production d'un asset d'arme :
*   **Modélisation 3D :** Utilisation de Blender pour sculpter et optimiser le mesh de l'arme.
*   **Texturing :** Création des textures via Paint.NET pour donner vie à notre modèle.
*   **Intégration :** Utilisation de l'Unreal Editor pour importer le mesh et configurer les shaders.
*   **Animation :** Mise en place des mécaniques de mouvement au sein de l'UDK.
*   **Scripting :** Configuration des propriétés de l'arme pour qu'elle soit jouable.

### Ce qui reste d'actualité aujourd'hui
Bien que l'Unreal Engine 3 soit considéré comme une technologie "legacy", les principes fondamentaux enseignés ici restent le socle de tout développement de jeu moderne :
1.  **Le Pipeline Asset :** Le processus de modélisation (High-poly vers Low-poly) et d'optimisation reste identique, peu importe le moteur (UE5, Unity, Godot).
2.  **La structure des données :** Comprendre comment un moteur lie un mesh, un squelette et une texture est une compétence transférable.
3.  **L'importance de l'optimisation :** Travailler sur UDK force à respecter des contraintes de budget de polygones et de textures, une excellente école pour apprendre à créer des jeux performants.
4.  **La logique de gameplay :** La manière dont les armes sont gérées via des classes et des états reste très proche de la logique actuelle des *Actor Components* dans les versions récentes d'Unreal.

{{< footer >}}
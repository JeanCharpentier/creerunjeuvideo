---
title: "3. Création d''un terrain Low-Poly avec Blender et Paint.net"
weight: 3
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blender', 'Terrain', 'Level Design', 'Tutoriel', 'Low-Poly']
---

Bienvenue dans ce troisième volet de notre série dédiée à la création de votre projet sur Unreal Engine 4. Aujourd'hui, nous faisons une petite entorse à nos habitudes : nous délaissons temporairement l'éditeur d'Unreal pour nous concentrer sur la modélisation externe.

Nous allons utiliser **Paint.net** pour générer une *heightmap* (carte de hauteur) et **Blender** pour sculpter notre terrain. Cette approche est idéale si vous recherchez un rendu "Low-Poly" brut et stylisé, difficile à obtenir avec les outils procéduraux classiques du moteur.

{{< youtube-rgpd "cuf28wQRYyc" >}}

### Résumé des étapes clés
*   **Génération de la Heightmap :** Utilisation de l'effet "Nuage" dans Paint.net (2048x2048) pour créer des variations de gris représentant les altitudes.
*   **Préparation dans Blender :** Importation du plan, subdivision (touche W) et triangulation (Ctrl+T) pour préparer la géométrie.
*   **Déformation :** Application du modificateur "Displace" en utilisant notre texture de hauteur pour donner du relief au terrain.
*   **Sculpting manuel :** Utilisation du "Proportional Editing" pour affiner les chemins et les vallées de manière douce et naturelle.
*   **Exportation :** Sauvegarde du fichier `.blend` dans votre dossier `Resource` du projet Unreal pour une intégration future.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions des logiciels aient évolué (Blender 2.76 est aujourd'hui largement dépassé par les versions 4.x), les concepts fondamentaux restent parfaitement valides pour le GameDev :

1.  **Le workflow Heightmap :** La technique consistant à utiliser une image en niveaux de gris pour définir un relief est un standard de l'industrie, même si Unreal Engine propose désormais des outils de *Landscape* très avancés.
2.  **L'importance de la topologie :** Comprendre comment subdiviser et trianguler un mesh reste crucial pour optimiser les performances, surtout dans un style Low-Poly où chaque polygone compte.
3.  **Le Proportional Editing :** C'est l'outil indispensable pour sculpter des terrains à la main sans avoir besoin d'outils de sculpting complexes.
4.  **Organisation des assets :** Créer un dossier `Resource` dédié dès le début du projet est une bonne pratique de gestion de fichiers qui vous évitera bien des maux de tête lors de l'importation dans l'Unreal Engine.

*Note : Si vous souhaitez créer des terrains vastes et complexes, n'oubliez pas que le "Landscape Editor" natif d'Unreal Engine reste la solution la plus optimisée pour gérer le LOD (Level of Detail) et les matériaux complexes.*

{{< footer >}}
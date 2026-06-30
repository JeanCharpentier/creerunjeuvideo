---
title: "5. Texturing et finitions intérieures sous Unreal Engine 3"
weight: 5
date: 2026-06-17
categories: ['GameDev']
tags: ['Unreal Engine 3', 'Tutoriel', 'Level Design', 'FPS']
---

Bienvenue dans ce cinquième épisode de notre série dédiée à la création d'un FPS avec l'Unreal Engine 3 (UE3). Après avoir posé les bases de notre structure, il est temps de passer à une étape cruciale pour l'immersion : le texturing complet de notre environnement intérieur.

{{< youtube-rgpd "MNo1WBSjMpg" >}}

Dans cet épisode, nous nous concentrons sur l'habillage de notre map. Le défi principal réside dans l'alignement des textures sur les différentes surfaces (murs, couloirs, escaliers) pour éviter les "coutures" visibles et les répétitions disgracieuses.

### Au programme de cet épisode :
*   **Gestion des matériaux :** Utilisation du *Content Browser* pour appliquer les textures (`MMDORSECOR`, `MLT Flores BSP`, etc.) sur les différentes brosses BSP.
*   **Alignement et Scaling :** Techniques pour ajuster les textures en U et en V afin d'assurer une continuité visuelle, notamment dans les zones complexes comme les couloirs et les escaliers.
*   **Gestion des surfaces :** Utilisation de la fonction "Select Surfaces -> Matching Brush" pour appliquer des modifications de manière efficace sur plusieurs faces à la fois.
*   **Optimisation visuelle :** Astuces pour tricher légèrement sur le scaling (ex: 2.1 au lieu de 2.0) afin de masquer les jointures entre deux textures.
*   **Build Lighting :** Lancement du calcul des lumières avec *Lightmass* en mode "High" pour valider le rendu final de notre travail de texturing.

### Ce qui reste d'actualité aujourd'hui

Bien que l'Unreal Engine 3 soit aujourd'hui remplacé par des versions plus modernes (UE4/UE5), les principes fondamentaux abordés ici restent des piliers du métier de Level Designer :

1.  **La rigueur de l'alignement :** Le "texel density" et l'alignement des textures restent une compétence clé pour éviter que les environnements ne paraissent "amateurs".
2.  **L'utilisation des brosses BSP :** Bien que le *Modeling Mode* ait évolué, la logique de création de volumes de base (Greyboxing) reste identique dans les workflows modernes.
3.  **La gestion des matériaux :** La compréhension des propriétés de surface et de leur répétition est universelle, quel que soit le moteur utilisé.
4.  **Le compromis performance/visuel :** Apprendre à "tricher" pour obtenir un résultat propre sans surcharger le moteur est une leçon de game design intemporelle.

{{< footer >}}
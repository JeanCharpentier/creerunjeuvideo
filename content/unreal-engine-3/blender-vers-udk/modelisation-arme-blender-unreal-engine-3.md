---
title: "2. Modélisation d''une arme pour Unreal Engine 3 avec Blender"
weight: 2
date: 2026-06-17
categories: ['Tutoriels GameDev']
tags: ['Unreal Engine 3', 'Blender', 'Modélisation', '3D', 'Game Design']
images: ["https://img.youtube.com/vi/oyysYuBDsSU/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/oyysYuBDsSU/maxresdefault.jpg"]
---

Dans ce deuxième volet de notre série dédiée au développement sur **Unreal Engine 3 (UDK)**, nous abordons une étape cruciale : la création de vos propres assets 3D. L'objectif est de modéliser une arme inspirée du lance-roquettes de *Rocket Arena*, en apprenant à configurer correctement Blender pour garantir une compatibilité parfaite avec l'Unreal Development Kit.

{{< youtube-rgpd "oyysYuBDsSU" >}}

### Résumé du tutoriel
*   **Configuration de l'environnement :** Réglage des subdivisions et de l'échelle dans Blender (32 subdivisions, 8 segments) pour éviter les problèmes de taille lors de l'importation dans UDK.
*   **Gestion des axes :** Importance de modéliser le canon dans l'axe des X pour faciliter l'intégration dans le moteur.
*   **Techniques de modélisation :** Utilisation des primitives (cylindres, cubes), extrusion (touche E), mise à l'échelle (S) et rotation (R).
*   **Optimisation :** Application des transformations (`Ctrl + A` > Scale) pour que le moteur reconnaisse les dimensions réelles de l'objet.
*   **Organisation :** Renommage des objets dans l'outliner (canon, chargeur, mécanisme, poignée) pour une meilleure gestion de la scène.
*   **Workflow :** Utilisation des vues orthographiques (1, 3, 7) pour vérifier le positionnement des éléments sous tous les angles.

### Ce qui reste d'actualité aujourd'hui
Bien que l'Unreal Engine 3 soit considéré comme une technologie "legacy", les principes fondamentaux enseignés dans ce tutoriel restent des piliers du GameDev moderne :
*   **Le respect de l'échelle :** Quel que soit le moteur (UE5, Unity, Godot), définir une échelle cohérente dès le logiciel de modélisation est indispensable pour éviter des problèmes de physique ou de collision.
*   **La propreté de la hiérarchie :** Nommer ses objets et organiser sa scène est une habitude de professionnel qui facilite le travail en équipe et le debug.
*   **L'application des transformations :** C'est une erreur classique des débutants. Appliquer le "Scale" et la "Rotation" avant l'exportation est une étape qui reste obligatoire dans 99% des pipelines de production 3D actuels.
*   **La modélisation par primitives :** La méthode consistant à assembler des formes simples pour créer un "blockout" ou un modèle final reste la base de tout workflow de modélisation efficace.

{{< footer >}}
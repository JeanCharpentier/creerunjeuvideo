---
title: "8. Création de décors et géométrie BSP"
weight: 8
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['GameDev', 'Level Design', 'BSP', 'Static Mesh', 'Tutoriel']
---

Dans cet épisode, nous abordons une étape fondamentale du level design : la création de formes géométriques directement au sein d'Unreal Engine 4. Bien que la majorité des assets complexes soient importés depuis des logiciels de modélisation 3D (Blender, Maya, 3ds Max), la maîtrise des outils intégrés est indispensable pour le prototypage rapide, les décors lointains ou l'architecture simple.

{{< youtube-rgpd "jc6G-Or2psU" >}}

### Résumé de l'épisode
*   **Utilisation des outils "Geometry" (BSP) :** Présentation des formes de base (boîtes, cylindres, cônes, escaliers) disponibles dans l'onglet *Modes*.
*   **Modification des paramètres :** Ajustement de la résolution (nombre de côtés) et des dimensions directement dans le panneau *Details*.
*   **Opérations booléennes :** Création d'un tuyau en utilisant une forme "Additive" (le cylindre plein) et une forme "Subtractive" (le cylindre creux) pour évider l'objet.
*   **Conversion en Static Mesh :** Transformation des brosses BSP en un objet 3D unique et réutilisable via le panneau *Brush Settings*.
*   **Gestion des collisions :** Configuration de la propriété *Collision Complexity* sur "Use Complex Collision as Simple" pour permettre au joueur d'interagir physiquement avec l'objet créé.

### Ce qui reste d'actualité aujourd'hui
Bien qu'Unreal Engine 5 ait introduit des outils de modélisation beaucoup plus avancés (le mode *Modeling*), les concepts abordés ici restent cruciaux pour plusieurs raisons :
1.  **Prototypage (Greyboxing) :** La méthode BSP reste la plus rapide pour définir les volumes d'un niveau avant de remplacer les éléments par des assets finaux.
2.  **Compréhension des collisions :** La gestion des collisions "Complex as Simple" est une notion technique qui s'applique toujours à de nombreux assets importés dans les versions récentes du moteur.
3.  **Workflow de travail :** La logique de soustraction de formes (booléens) est le socle de la modélisation constructive, un concept universel en GameDev.
4.  **Optimisation :** Savoir quand transformer une géométrie dynamique en *Static Mesh* est une compétence clé pour maintenir les performances de votre projet.

{{< footer >}}
---
title: "2. Créer les salles"
weight: 2
date: 2026-06-17
categories: ['GameDev']
tags: ['Unreal Engine 3', 'Level Design', 'Tutoriel', 'BSP']
images: ["https://img.youtube.com/vi/Fd_RjYxAEYY/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/Fd_RjYxAEYY/maxresdefault.jpg"]
---

Bienvenue dans ce deuxième volet de notre série consacrée à la création de niveaux sur **Unreal Engine 3**. Si vous avez suivi le premier épisode, vous avez déjà pris en main les bases de la manipulation des *Brushes* (brosses) et l'importance cruciale de la grille (*Grid*) pour structurer votre environnement.

Dans cet épisode, nous allons passer à la vitesse supérieure en construisant la structure de nos pièces, en intégrant des couloirs et en utilisant des techniques de soustraction géométrique pour ajouter du relief à notre map.

{{< youtube-rgpd "Fd_RjYxAEYY" >}}

### Résumé des étapes clés
*   **Gestion de la grille :** Alternance entre les grilles de 1, 8, 16 et 64 pour assurer une précision chirurgicale lors du placement des éléments.
*   **Construction modulaire :** Création de sols et de murs en utilisant les outils de base (Cube) pour définir deux pièces distinctes reliées par un couloir central.
*   **Alignement :** Utilisation systématique des vues orthogonales (dessus, face, côté) plutôt que la vue perspective pour garantir que les brosses sont parfaitement jointives.
*   **Optimisation :** Importance du "CSG Add" pour ajouter de la géométrie et du "CSG Subtract" pour creuser des formes (comme notre cylindre central).
*   **Éléments de gameplay :** Intégration d'escaliers via l'outil `LinearStaircase` avec ajustement du nombre de marches pour s'adapter à la hauteur de nos plateformes.

### Ce qui reste d'actualité aujourd'hui
Bien que l'Unreal Engine 3 soit aujourd'hui remplacé par les versions 4 et 5, les principes fondamentaux abordés ici restent le socle du *Level Design* moderne :

1.  **Le "Blockout" :** La méthode consistant à créer une carte avec des formes géométriques simples (BSP/ProBuilder) avant d'ajouter des assets finaux est toujours la norme dans l'industrie pour valider le *gameplay*.
2.  **La rigueur de la grille :** Travailler sur des multiples de puissances de 2 (8, 16, 64) est une règle d'or qui facilite l'alignement des textures et évite les problèmes de "z-fighting" ou de collisions.
3.  **La vision orthogonale :** Même dans les moteurs récents, maîtriser les vues de face et de dessus reste indispensable pour éviter les erreurs de placement dans l'espace 3D.
4.  **La gestion des ressources :** L'habitude de sauvegarder fréquemment et de garder une hiérarchie propre dans ses brosses est une discipline qui vous sauvera la mise, quel que soit le moteur utilisé.

{{< footer >}}
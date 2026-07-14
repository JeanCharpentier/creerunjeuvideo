---
title: "3. Création de niveaux : Structuration et éclairage dans Unreal Engine 3"
weight: 3
date: 2026-06-17
categories: ['GameDev']
tags: ['Unreal Engine 3', 'Level Design', 'Tutoriel', 'CSG']
images: ["https://img.youtube.com/vi/QAXiEZGE4bQ/maxresdefault.jpg"]
---

Dans ce troisième épisode de notre série dédiée à la création de jeux avec **Unreal Engine 3**, nous passons à la vitesse supérieure. Après avoir posé les bases de notre carte dans les épisodes précédents, il est temps de structurer l'intérieur de notre niveau : création des couloirs, intégration d'une salle principale, gestion des dénivelés avec des escaliers et mise en place d'un éclairage fonctionnel pour tester notre environnement.

{{< youtube-rgpd "QAXiEZGE4bQ" >}}

### Résumé de l'épisode
*   **Modélisation CSG (Constructive Solid Geometry) :** Utilisation intensive de l'outil "Cube" pour bâtir les couloirs et la salle principale.
*   **Gestion des alignements :** Importance du réglage de la grille (Grid) pour assurer une cohérence géométrique et éviter les erreurs de jonction.
*   **Création de dénivelés :** Mise en place d'escaliers pour connecter des zones à différentes hauteurs.
*   **Calculs géométriques :** Ajustement précis des dimensions des murs pour s'adapter aux changements de niveau.
*   **Éclairage et Player Start :** Ajout de lumières ponctuelles (Point Lights) et positionnement du point d'apparition du joueur.
*   **Compilation du niveau :** Utilisation des outils de "Build" (Geometry, Lighting, Paths) pour finaliser la scène et permettre le test en jeu.

### Ce qui reste d'actualité aujourd'hui

Bien que l'Unreal Engine 3 soit considéré comme une technologie "legacy" face à l'Unreal Engine 5, les principes fondamentaux abordés dans ce tutoriel restent le socle de tout level designer :

1.  **Le Workflow CSG (ou "Greyboxing") :** Même dans les moteurs modernes, le blocage de niveau (greyboxing) reste l'étape cruciale pour valider le *gameplay* et le *level design* avant de passer à l'habillage visuel (assets finaux).
2.  **La rigueur de la grille :** Travailler sur une grille est une règle d'or universelle. Elle garantit que les éléments s'emboîtent parfaitement, évitant les fuites de lumière (*light leaks*) et les problèmes de collision.
3.  **La hiérarchie du Build :** La distinction entre la géométrie, l'éclairage et les chemins d'IA (Navigation Mesh) est une logique qui persiste dans les versions actuelles d'Unreal Engine.
4.  **L'itération rapide :** La méthode consistant à construire, tester, puis corriger est le cœur même du développement de jeu. Apprendre à utiliser les outils de test intégrés (Play In Editor) est indispensable pour tout développeur.

{{< footer >}}
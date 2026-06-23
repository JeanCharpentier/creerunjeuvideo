---
title: "13. Création du Blueprint ''Tronc'' et gestion des collisions"
weight: 13
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprint', 'GameDev', 'Collision', 'Actor', 'Débutant']
---

Dans cet épisode, nous passons à la phase concrète du développement : la création des mécaniques de jeu. Après avoir importé nos assets, il est temps de donner vie à notre premier obstacle : le tronc. Nous allons apprendre à structurer un Blueprint, configurer un modèle 3D et définir des zones de collision précises pour gérer le "Game Over" et le score.

{{< youtube-rgpd "" >}}

### Résumé des étapes clés
*   **Organisation du projet :** Création d'un dossier dédié `Blueprints` pour séparer vos créations des assets du template.
*   **Création de l'Actor :** Utilisation d'une classe `Actor` simple, idéale pour les objets qui n'ont pas besoin d'être contrôlés par le joueur.
*   **Intégration du Mesh :** Ajout d'un composant `Static Mesh` et ajustement de son échelle (Scale) pour correspondre aux proportions du jeu.
*   **Gestion des collisions (Game Over) :** Ajout d'une `Capsule Collision` (renommée `Box_GameOver`) ajustée précisément au mesh pour éviter la frustration du joueur.
*   **Gestion des points :** Ajout d'une `Box Collision` indépendante (`Box_Point`) placée au-dessus du tronc pour détecter le passage réussi du joueur.
*   **Optimisation du workflow :** Configuration de l'option "Save on Compile" pour automatiser la sauvegarde et gagner en productivité.

### Ce qui reste d'actualité aujourd'hui
Bien que cet article se base sur Unreal Engine 4, les principes fondamentaux abordés ici restent parfaitement valables pour **Unreal Engine 5** :
1.  **La hiérarchie des composants :** La méthode consistant à attacher des collisions à un `DefaultSceneRoot` ou à un mesh spécifique est toujours la norme pour créer des acteurs interactifs.
2.  **Le "Game Feel" :** L'importance de ne pas faire dépasser les boîtes de collision pour éviter les collisions injustes est un pilier du game design, quel que soit le moteur utilisé.
3.  **Le workflow de compilation :** L'automatisation de la sauvegarde lors de la compilation est une bonne pratique qui permet de sécuriser votre travail contre les crashs imprévus.
4.  **La structure des dossiers :** Garder ses propres assets séparés des dossiers de base (Engine Content ou Templates) reste la meilleure façon de maintenir un projet propre et évolutif.

{{< footer >}}
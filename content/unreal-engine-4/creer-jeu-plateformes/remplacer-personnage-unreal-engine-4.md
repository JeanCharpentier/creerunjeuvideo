---
title: "6. Remplacer le personnage par défaut dans Unreal Engine 4"
weight: 6
date: 2026-06-17
categories: ['Développement de jeux']
tags: ['Unreal Engine 4', 'GameDev', 'Tutoriel', 'Skeletal Mesh', 'Animation']
---

Dans ce sixième chapitre de notre série dédiée à la création d'un jeu de plateforme, nous allons passer à l'étape cruciale de la personnalisation visuelle : remplacer le mannequin "crash test" par défaut par votre propre personnage.

{{< youtube-rgpd "hoyZCg9gZZo" >}}

### Résumé des étapes clés
*   **Organisation :** Création d'un dossier dédié (`/Perso`) pour importer proprement vos assets.
*   **Importation FBX :** Utilisation des options d'importation (`Import Mesh` et `Import Skeletal`) pour garantir que le modèle 3D possède un squelette fonctionnel.
*   **Configuration du Squelette :** Association du squelette au `UE4 Mannequin Skeleton` pour assurer la compatibilité avec les animations existantes.
*   **Gestion des Matériels :** Importation automatique des textures (Base Color, Normal Map, Specular) pour un rendu visuel complet.
*   **Intégration :** Remplacement du mesh dans le Blueprint `FirstPersonCharacter` via le `Viewport`.
*   **Retargeting d'animation :** Ajustement des paramètres de translation du squelette (`Skeleton` vs `Animation Relative`) pour corriger la posture du personnage et éviter les déformations lors des mouvements.

### Ce qui reste d'actualité aujourd'hui
Bien que cet article se concentre sur Unreal Engine 4, les principes fondamentaux abordés restent parfaitement valables pour **Unreal Engine 5** :

1.  **Le workflow d'importation :** La structure des fichiers FBX et la nécessité de lier un squelette restent identiques.
2.  **L'importance des Normal Maps :** L'optimisation par les textures de relief est toujours la norme pour maintenir un bon ratio performance/qualité visuelle.
3.  **Le système de collision :** L'utilisation de capsules de collision simplifiées pour les personnages est toujours la méthode privilégiée pour éviter les calculs physiques trop coûteux.
4.  **Le Retargeting :** Si l'interface a évolué avec l'IK Rig dans UE5, la logique de "remapage" des os pour adapter des animations à différents modèles reste le cœur du métier d'animateur sur le moteur.

{{< footer >}}
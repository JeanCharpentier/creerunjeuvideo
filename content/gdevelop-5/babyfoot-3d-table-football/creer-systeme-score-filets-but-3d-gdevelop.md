---
title: "3. Créer un système de score et des filets de but 3D"
weight: 3
date: 2023-10-27
categories: ['Tutoriels']
tags: ['GDevelop', '3D', 'Jeu Mobile', 'GameDev']
---

Dans ce troisième épisode de notre série dédiée à la création d'un baby-foot mobile avec GDevelop 5, nous allons passer aux choses sérieuses : la gestion du score et l'intégration visuelle des filets de but.

{{< youtube-rgpd "5f5_dowmP30" >}}

### Au programme de cet épisode :
*   **Interface utilisateur (UI) :** Création d'un calque dédié pour afficher le score en temps réel.
*   **Zones de détection :** Mise en place des "Scorebox" (objets 3D invisibles) derrière les buts pour détecter le passage de la balle.
*   **Logique de jeu :** Utilisation des variables d'instance pour inverser les scores selon le camp qui encaisse.
*   **Réinitialisation :** Automatisation du "kickoff" (remise en jeu) après chaque but marqué.
*   **Design 3D :** Création et application de textures de filets avec Piskel, en abordant les bonnes pratiques sur la transparence.

### Ce qui reste d'actualité aujourd'hui
*   **Gestion des calques :** Séparer l'interface (UI) du monde 3D reste la méthode la plus propre pour maintenir une lisibilité optimale sur mobile.
*   **Performance et Transparence :** Comme mentionné dans la vidéo, la transparence en 3D est coûteuse. Évitez de superposer trop d'objets transparents pour préserver le framerate sur les appareils mobiles.
*   **Le "Tuilage" (Tiling) :** L'utilisation du tuilage pour les textures répétitives (comme un filet) est une technique indispensable pour optimiser la mémoire tout en gardant un rendu visuel détaillé.
*   **Logique de collision :** N'oubliez jamais d'ajouter un comportement physique (même statique) aux objets 3D destinés à détecter des collisions, sans quoi GDevelop ne pourra pas déclencher vos événements.

{{< footer >}}
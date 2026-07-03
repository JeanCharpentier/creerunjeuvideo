---
title: "1. Créer un jeu de type Survival avec GDevelop 5"
weight: 1
date: 2023-10-27
categories: ['Tutoriels']
tags: ['GDevelop 5', 'Survival', 'Débutant', 'GameDev']
---

Bienvenue dans cette nouvelle série dédiée à la création d'un jeu de type "Survival" (à la *Vampire Survivors* ou *Deep Rock Galactic: Survivor*) avec GDevelop 5 ! Dans ce premier épisode, nous posons les bases techniques : mise en place du projet, gestion du personnage et création d'une caméra fluide.

{{< youtube-rgpd "g_nucz_EsCQ" >}}

### Au programme de cet épisode :
*   **Configuration du projet :** Création d'un projet vide optimisé pour le Pixel Art.
*   **Gestion des assets :** Utilisation du pack "Dungeon" (CC0) pour intégrer un personnage et un sol.
*   **Comportements (Behaviors) :** Mise en place du mouvement "8 directions" et remappage des touches (ZQSD).
*   **Logique de jeu :** Inversion horizontale du sprite en fonction de la direction.
*   **Caméra fluide :** Utilisation de l'interpolation linéaire (Lerp) pour un suivi de caméra professionnel.

### Ce qui reste d'actualité aujourd'hui

*   **L'importance de l'optimisation :** Même pour un petit projet, bien structurer ses variables et ses objets dès le début est crucial pour la suite.
*   **Le "Lerp" (Interpolation Linéaire) :** C'est une technique incontournable en GameDev. Elle permet de passer d'une valeur A à une valeur B de manière progressive, offrant un rendu beaucoup plus "smooth" et agréable qu'un simple centrage automatique.
*   **L'indépendance des contrôles :** En utilisant la vitesse de l'objet plutôt que les touches du clavier pour gérer l'orientation du sprite, vous rendez votre jeu compatible avec n'importe quelle configuration de clavier (AZERTY, QWERTY, etc.).
*   **L'organisation :** Utiliser des dossiers et renommer ses objets (ex: "Joueur", "Sol") est une habitude de travail qui vous fera gagner un temps précieux quand votre projet gagnera en complexité.

{{< footer >}}
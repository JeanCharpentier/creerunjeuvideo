---
title: "5. Munitions, Rechargement et HUD Statique"
weight: 5
prev_url: "/construct-2/tuto-top-down-shooter/construct-2-gerer-degats-variables-instance/"
next_url: "/construct-2/tuto-top-down-shooter/gerer-vie-creer-menu-optimiser-jeu-construct-2/"
date: 2023-10-27
categories: ['Archive']
tags: ['Construct 2', 'Tutoriel', 'Game Dev', 'HTML5', 'HUD', 'Parallax', 'Variables', 'Munitions', 'Rechargement', 'Pickups', 'UI']
images: ["https://img.youtube.com/vi/5Vs9f7pI2-s/maxresdefault.jpg"]
---
Dans ce cinquième épisode de notre série sur Construct 2, nous allons approfondir la gestion de l'interface utilisateur et des mécaniques de jeu essentielles, en nous concentrant sur les munitions et le rechargement.

{{< youtube-rgpd "5Vs9f7pI2-s" >}}

### Résumé des notions clés abordées :

*   **Gestion du HUD Statique avec Parallax (0,0)**
    *   Apprentissage de la propriété `Parallax` pour les calques (Layers) dans Construct 2.
    *   Configuration du calque HUD (Heads-Up Display) avec une valeur de parallax de `0,0` pour s'assurer que les éléments d'interface (vie, munitions) restent fixes à l'écran, indépendamment du défilement de la caméra.
*   **Affichage des Munitions**
    *   Création d'un objet `Text` sur le calque HUD pour afficher le nombre de munitions restantes.
    *   Personnalisation du texte (police, taille, couleur, position).
*   **Variables d'Instance pour les Munitions**
    *   **Pour le Joueur (`Marine`)** :
        *   `MaxMun` : Variable d'instance pour définir la capacité maximale de munitions que le joueur peut porter (ex: 6 pour un revolver).
        *   `Munition` : Variable d'instance pour suivre le nombre actuel de munitions du joueur.
    *   **Pour les Chargeurs (`Charger`)** :
        *   `Charge` : Variable d'instance pour définir la quantité de munitions qu'un chargeur (pickup) fournit.
*   **Initialisation des Munitions au Démarrage du Niveau**
    *   Utilisation de l'événement système `On Start Of Layout` pour initialiser la variable `Munition` du joueur à la valeur de `MaxMun`. Cela assure que le joueur commence chaque niveau avec un chargeur plein.
*   **Mise à Jour de l'Affichage des Munitions**
    *   Dans l'événement système `Every Tick` (à chaque image du jeu), mise à jour de l'objet `Text` des munitions pour qu'il affiche la valeur actuelle de la variable `Munition` du joueur.
*   **Mécanique de Tir et Consommation de Munitions**
    *   Modification de l'événement `Mouse - On Left Button Clicked` (lorsque le joueur tire).
    *   **Condition** : Ajout d'une condition `Marine.Munition > 0` pour s'assurer que le joueur ne peut tirer que s'il a des munitions.
    *   **Action** : Soustraire `1` à la variable `Munition` du joueur après chaque tir.
*   **Ramassage des Chargeurs (Pickups)**
    *   Création d'un objet `Sprite` pour représenter un chargeur de munitions sur le sol.
    *   **Événement** : `Marine - Is Overlapping another object (Charger)` (lorsque le joueur entre en collision avec un chargeur).
    *   **Condition Cruciale** : Ajout d'une condition pour éviter de recharger au-delà de la capacité maximale : `Marine.MaxMun >= Marine.Munition + Charger.Charge`. Cela vérifie si l'ajout des munitions du chargeur ne dépasse pas la capacité maximale du joueur.
    *   **Actions** :
        *   Ajouter la valeur de `Charger.Charge` à la variable `Munition` du joueur.
        *   Détruire l'objet `Charger` pour le faire disparaître du niveau.

### Ce qui reste d'actualité aujourd'hui

Bien que ce tutoriel utilise Construct 2, les concepts abordés sont des piliers fondamentaux du développement de jeux vidéo et restent entièrement pertinents, quel que soit le moteur ou le langage utilisé :

*   **Gestion de l'Interface Utilisateur (UI/HUD)** : La nécessité de calques dédiés pour l'interface utilisateur et la gestion de leur comportement (comme la fixité à l'écran via le parallax) est une pratique standard pour une bonne expérience joueur. Tous les moteurs modernes offrent des outils robustes pour cela.
*   **Variables d'Instance et Gestion des États** : L'utilisation de variables pour stocker des données spécifiques à chaque objet (vie, munitions, vitesse, etc.) est la base de la logique de jeu. Comprendre comment définir, modifier et comparer ces variables est essentiel pour créer des systèmes de jeu dynamiques.
*   **Logique Conditionnelle et Événementielle** : Le modèle "si [condition] alors [action]" est le cœur de la programmation. Savoir comment enchaîner des conditions complexes (comme empêcher le tir sans munitions ou le sur-rechargement) est une compétence précieuse pour tout développeur.
*   **Interactions Objets-Joueur (Pickups)** : La détection de collision et la gestion des interactions avec des objets ramassables (santé, munitions, bonus) sont des mécaniques de jeu universelles, présentes dans presque tous les types de jeux.
*   **Construct 2 comme Tremplin** : L'approche visuelle de Construct 2 est excellente pour apprendre ces concepts sans se noyer dans la syntaxe complexe. Les compétences acquises sont directement transférables à des moteurs plus complexes comme Unity (avec C#), Godot (avec GDScript) ou GameMaker Studio (avec GML), où les mêmes principes de variables, d'événements et de conditions s'appliquent.

{{< footer >}}
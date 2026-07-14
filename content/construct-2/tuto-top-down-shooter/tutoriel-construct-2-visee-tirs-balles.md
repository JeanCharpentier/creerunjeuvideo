---
title: "2. Visée à la Souris et Tirs de Balles"
weight: 2
prev_url: "/construct-2/tuto-top-down-shooter/creer-jeu-html5-construct-2-introduction-premiers-pas/"
next_url: "/construct-2/tuto-top-down-shooter/creer-monstres-ia-simple-construct-2/"
date: 2023-10-27
categories: ['Archive']
tags: ['Construct 2', 'Tutoriel', 'Game Dev', 'Top-Down Shooter', 'Evenements', 'Comportements', 'Visee Souris', 'Tir', 'Developpement de jeu']
images: ["https://img.youtube.com/vi/9VbNUC23V6k/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/9VbNUC23V6k/maxresdefault.jpg"]
---
Plongez dans la deuxième partie de notre série de tutoriels Construct 2, où nous allons donner à notre personnage la capacité de viser avec la souris et de tirer des projectiles !

{{< youtube-rgpd "9VbNUC23V6k" >}}

### Résumé des notions clés abordées :

*   **Ouverture de Projet et Prévisualisation**
    *   Comment ouvrir un projet récent dans Construct 2.
    *   Utilisation de la fonction "Preview" pour tester le jeu en cours de développement.
*   **Introduction aux Événements Construct 2**
    *   Explication du concept d'événement : "Si [condition], alors [action]".
    *   Utilisation de l'exemple de la cuisson des pâtes pour illustrer la logique événementielle.
    *   Comment ajouter un événement (`Add Event`) et une action (`Add Action`).
*   **L'événement Système "Every Tick"**
    *   Présentation de l'événement `System -> Every Tick`, qui s'exécute à chaque cycle de lecture du programme (la boucle de jeu).
    *   Son importance pour les actions continues.
*   **Intégration de la Souris**
    *   Ajout de l'objet `Mouse` au projet pour capter les entrées de la souris.
    *   Utilisation des expressions `Mouse.X` et `Mouse.Y` pour obtenir les coordonnées du curseur.
*   **Visée du Personnage avec la Souris**
    *   Action `Marines -> Set Angle Towards Position` pour orienter le personnage vers un point spécifique.
    *   Combinaison de cette action avec `Mouse.X` et `Mouse.Y` pour que le personnage suive le curseur de la souris.
*   **Création et Configuration d'un Projectile (Balle)**
    *   Ajout d'un nouveau `Sprite` pour représenter la balle.
    *   Application du comportement (`Behavior`) "Bullet" au sprite de la balle.
    *   Configuration des propriétés du comportement "Bullet" (vitesse, accélération, gravité, rebond).
    *   Astuce pour masquer le sprite initial de la balle en le plaçant hors de la zone de jeu.
*   **Système de Tir**
    *   Création d'un événement `Mouse -> On Click` (bouton gauche) pour déclencher le tir.
    *   Action `Marines -> Spawn another object` pour instancier une balle à partir du personnage.
    *   Spécification du calque (`Layer`) sur lequel la balle doit apparaître.

### Ce qui reste d'actualité aujourd'hui

Bien que ce tutoriel utilise Construct 2, les concepts fondamentaux abordés sont intemporels et s'appliquent à la plupart des moteurs de jeu modernes, y compris Construct 3 et d'autres plateformes de développement :

*   **La Logique Événementielle (Event-Driven Programming)** : Le principe "Si [condition], alors [action]" est le pilier de nombreux systèmes de jeu, en particulier dans les moteurs sans code ou low-code. Comprendre cette logique est essentiel pour créer des interactions dynamiques.
*   **La Boucle de Jeu (Game Loop)** : L'événement "Every Tick" illustre le concept universel de la boucle de jeu, où le programme met à jour l'état du jeu en continu. C'est le cœur de tout jeu en temps réel.
*   **Gestion des Inputs** : L'intégration des périphériques d'entrée (souris, clavier, manette) est une étape fondamentale. Les méthodes pour capter les clics ou les positions du curseur sont des compétences transférables.
*   **Comportements (Behaviors / Components)** : L'idée d'attacher des fonctionnalités pré-construites (comme le comportement "Bullet") à des objets est une abstraction puissante. Dans d'autres moteurs, cela se retrouve sous forme de composants ou de scripts réutilisables.
*   **Instanciation Dynamique d'Objets (Spawning)** : Créer des objets en cours de jeu (comme des projectiles, des ennemis ou des effets) à partir de "préfabriqués" ou de "modèles" est une technique courante et indispensable pour la plupart des jeux.
*   **Gestion des Calques (Layers)** : Organiser les éléments du jeu sur différents calques est une pratique standard pour gérer la profondeur de rendu, les interactions et la visibilité des objets.

{{< footer >}}
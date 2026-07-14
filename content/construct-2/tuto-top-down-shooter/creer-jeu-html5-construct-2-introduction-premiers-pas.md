---
title: "1. Introduction et premiers pas"
weight: 1
prev_url: "/construct-2/tuto-top-down-shooter/index/"
next_url: "/construct-2/tuto-top-down-shooter/tutoriel-construct-2-visee-tirs-balles/"
date: 2023-10-27
categories: ['Archive']
tags: ['Construct 2', 'HTML5', 'Game Development', 'Tutoriel', 'Debutant', 'Interface', 'Projet', 'Sprite', 'Comportements', 'Mouvement']
images: ["https://img.youtube.com/vi/z2rZLCJolRE/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/z2rZLCJolRE/maxresdefault.jpg"]
---
Plongez dans le monde de la création de jeux HTML5 avec Construct 2 ! Ce premier tutoriel vous guide à travers l'installation, la découverte de l'interface et la mise en place des bases de votre premier jeu, un Top-Down Shooter.

{{< youtube-rgpd "z2rZLCJolRE" >}}

### Résumé des notions clés

*   **Introduction à Construct 2 et HTML5**
    *   **Avantages du HTML5** : Compatibilité multiplateforme (PC, Mac, Linux, iOS, Android), permettant de créer un jeu jouable partout.
    *   **Construct 2** : Logiciel intuitif et accessible, idéal pour une première approche du développement de jeux.
    *   **Versions de Construct 2** : Gratuite (avec limitations), personnelle (environ 60€), et commerciale (plus de 200€ pour la revente de jeux).
    *   **Objectif de la série** : Apprendre à créer un jeu de tir vu de dessus (Top-Down Shooter - TDS).
*   **Prise en main de l'interface de Construct 2**
    *   **Panneau de propriétés** (à gauche) : Affiche les attributs de l'élément sélectionné.
    *   **Zone de travail centrale** :
        *   **Layout** : La partie graphique où vous placez vos éléments de jeu.
        *   **Event Sheet** : La partie logique où vous définissez les interactions et comportements.
    *   **Panneau de droite** :
        *   **Project Explorer** : Gère l'ensemble de votre projet (layouts, event sheets, etc.).
        *   **Layers** : Permet de superposer les éléments du jeu sur différents niveaux (calques).
        *   **Objects** : Liste tous les objets présents dans la scène actuelle.
*   **Configuration du projet**
    *   Création d'un nouveau projet (`.capx` pour un fichier unique).
    *   Nom du projet : `TDS`.
    *   **Taille de la fenêtre de jeu (`Window Size`)** : Définie à `640x480` pixels.
    *   **Navigateur de prévisualisation (`Preview Browser`)** : Permet de choisir le navigateur pour tester le jeu.
*   **Configuration du niveau (Layout)**
    *   Renommage du layout par défaut en `Level One`.
    *   **Taille du layout (`Layout Size`)** : Définie à `1280x1224` (deux fois la taille de la fenêtre) pour un niveau plus grand que l'écran.
*   **Gestion des Event Sheets**
    *   Renommage de l'Event Sheet par défaut en `ES_Level One` pour une meilleure organisation et la possibilité de réutiliser la même feuille d'événements pour plusieurs niveaux.
*   **Organisation des calques (Layers)**
    *   Renommage du calque par défaut en `Fond`.
    *   Ajout de nouveaux calques : `Joueur`, `Ennemis`, `HUD`.
    *   **Limitation de la version gratuite** : Seulement 4 calques disponibles.
    *   **Verrouillage du calque `Fond`** : Empêche toute modification accidentelle une fois le fond configuré.
*   **Ajout des premiers éléments graphiques**
    *   **Arrière-plan (`Tiled Background`)** :
        *   Ajout d'un objet `Tiled Background` sur le calque `Fond`.
        *   Chargement de l'image `BG.png`.
        *   Positionnement à `0,0` et redimensionnement à la taille du layout (`1280x1224`) pour couvrir tout le niveau.
    *   **Personnage joueur (`Sprite`)** :
        *   Ajout d'un objet `Sprite` sur le calque `Joueur`.
        *   Chargement de l'image `player.png`.
        *   Renommage du sprite en `Marine`.
*   **Introduction aux comportements (Behaviors)**
    *   Sélection du sprite `Marine`.
    *   Ajout du comportement `8 Direction` via le panneau des propriétés.
    *   Ce comportement permet un déplacement facile du personnage avec les touches directionnelles du clavier, sans écrire de code.
    *   Test du jeu pour visualiser le personnage se déplaçant.

### Ce qui reste d'actualité aujourd'hui

Bien que Construct 2 ait été remplacé par Construct 3, les concepts fondamentaux introduits dans ce tutoriel restent d'une pertinence capitale pour tout développeur de jeux, quel que soit le moteur utilisé :

*   **La philosophie "No-Code/Low-Code"** : Construct 2 a été un pionnier dans la démocratisation de la création de jeux sans code ou avec très peu de code. Cette approche est plus que jamais d'actualité, avec des outils comme Construct 3, Unity Bolt, Unreal Engine Blueprints ou Godot Visual Script, qui permettent de se concentrer sur le design et la logique du jeu plutôt que sur la syntaxe du code.
*   **Le développement HTML5 et multiplateforme** : La capacité de créer un jeu une seule fois et de le déployer sur une multitude de plateformes (web, mobile, desktop) est un avantage majeur. Le HTML5 reste une cible de choix pour les jeux casual, les prototypes et les applications interactives web.
*   **L'interface visuelle intuitive** : La structure de l'interface de Construct 2 (panneaux de propriétés, zone de travail, explorateur de projet, gestion des calques) est un modèle que l'on retrouve dans la plupart des moteurs de jeu modernes. Maîtriser cette organisation facilite grandement l'apprentissage de nouveaux outils.
*   **Le système de comportements (Behaviors)** : L'utilisation de comportements prédéfinis pour des actions courantes (mouvement, physique, détection de collisions) est une fonctionnalité puissante qui accélère considérablement le développement. Elle permet aux créateurs de se concentrer sur l'expérience de jeu plutôt que sur l'implémentation technique de base.
*   **La gestion des calques (Layers)** : L'organisation des éléments du jeu en calques est une pratique fondamentale en 2D pour gérer la profondeur, les interactions et l'ordre d'affichage. Ce concept est universel et essentiel pour des scènes complexes.
*   **L'importance de la préparation du projet** : Bien nommer ses éléments (layouts, event sheets, sprites) et organiser ses calques dès le début sont des bonnes pratiques qui évitent des problèmes futurs et facilitent la maintenance, quel que soit le moteur de jeu.
*   **Le concept de "Top-Down Shooter"** : Ce genre de jeu simple est un excellent point de départ pour apprendre les bases du mouvement, des collisions, du tir et de la gestion des ennemis, des compétences transférables à de nombreux autres types de jeux.

{{< footer >}}
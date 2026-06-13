---
title: "3. Créer des Monstres et une IA Simple dans Construct 2"
weight: 3
prev_url: "/construct-2/tuto-top-down-shooter/tutoriel-construct-2-visee-tirs-balles/"
next_url: "/construct-2/tuto-top-down-shooter/construct-2-gerer-degats-variables-instance/"
date: 2023-10-27
categories: ['Archive']
tags: ['Construct 2', 'Game Development', 'Tutoriel', 'Monstres', 'IA Simple', 'Comportements', 'Evenements', 'Collision', 'HTML5', 'WizWig']
---
Dans cette troisième partie de notre tutoriel sur Construct 2, nous allons donner vie à notre jeu en introduisant des ennemis et une intelligence artificielle rudimentaire.

{{< youtube-rgpd "8SKId4m6uu4" >}}

### Résumé des notions clés abordées :

*   **Préparation de l'environnement :**
    *   Verrouillage des calques existants (HUD, Joueur, Fond) pour s'assurer de travailler exclusivement sur le calque "Monstres".
    *   Création d'un nouveau Sprite nommé "Mubbe" (notre monstre) et importation de son image.
*   **Comportement des Monstres :**
    *   Ajout du comportement "Bullet" (Projectile) au monstre, le considérant comme un projectile qui se déplace.
    *   Réglage de la vitesse du monstre (ex: 50) pour un mouvement plus lent et contrôlé.
*   **Intelligence Artificielle Simple (Suivi de Joueur) :**
    *   Dans la feuille d'événements (Event Sheet), à chaque "tick" (chaque boucle de jeu) :
        *   Le monstre utilise l'action "Set Angle Towards Position" pour toujours regarder et se diriger vers la position (X, Y) du joueur.
*   **Gestion des Collisions :**
    *   **Balle vs. Monstre :**
        *   Événement : Quand la "Balle" entre en collision avec "Mubbe".
        *   Actions : "Mubbe: Destroy" (le monstre disparaît), "Balle: Destroy" (la balle disparaît après l'impact).
    *   **Joueur vs. Monstre :**
        *   Événement : Quand le "Marine" (le joueur) entre en collision avec "Mubbe".
        *   Action : "Marine: Destroy" (le joueur disparaît – cette action est temporaire pour les tests et sera remplacée par un système de points de vie/Game Over plus tard).
*   **Duplication des Monstres :**
    *   Démonstration de la facilité à dupliquer les monstres configurés (Ctrl+C, Ctrl+V) pour peupler rapidement le niveau avec plusieurs ennemis.

### Ce qui reste d'actualité aujourd'hui

Bien que ce tutoriel utilise Construct 2, les principes fondamentaux du développement de jeux qu'il aborde sont intemporels et s'appliquent à la plupart des moteurs de jeu modernes :

*   **Logique événementielle et Comportements :** Le concept de "feuille d'événements" et l'utilisation de "comportements" pré-faits pour gérer le mouvement, les projectiles ou l'IA sont des piliers du développement de jeux sans code ou à faible code (comme GDevelop, Scratch, ou même des systèmes de nœuds visuels dans Unity/Unreal).
*   **Gestion des entités et des collisions :** Créer des objets (Sprites), leur attribuer des propriétés et gérer leurs interactions (collisions) est la base de tout jeu. La détection de collision et les actions qui en découlent sont des mécaniques essentielles.
*   **IA simple (Suivi de joueur) :** La technique de faire "regarder" un ennemi vers le joueur est une forme d'IA très courante et efficace pour les jeux d'action top-down ou les tower defense. Elle est souvent le point de départ pour des IA plus complexes.
*   **Organisation du projet :** L'utilisation de calques (layers) pour structurer les éléments du jeu (joueur, HUD, ennemis, fond) reste une excellente pratique pour maintenir la clarté du projet et gérer l'ordre de rendu.
*   **Prototypage rapide :** Construct 2, comme d'autres outils similaires, excelle dans le prototypage rapide. Les méthodes présentées permettent de mettre en place des mécaniques de jeu de base en un temps record, ce qui est précieux pour tester des idées.
*   **Développement HTML5 :** Construct 2 génère des jeux HTML5, un format toujours très pertinent pour les jeux web, mobiles via des wrappers, et même pour des applications légères.

{{< footer >}}
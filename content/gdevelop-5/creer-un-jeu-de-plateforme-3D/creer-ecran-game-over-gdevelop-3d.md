---
title: "7. Créer un écran de Game Over et gérer la réinitialisation du score"
weight: 7
date: 2023-10-27
categories: ['Tutoriels GDevelop']
tags: ['GDevelop', '3D', 'Game Over', 'Variables', 'Développement de jeu']
---

Dans cet avant-dernier épisode de notre série dédiée à la découverte de la 3D sur GDevelop 5, nous allons finaliser le système de défaite de notre jeu. L'objectif est de créer un écran de "Game Over" propre, de mettre le jeu en pause lors de l'affichage, et de corriger le bug persistant du score qui ne se réinitialisait pas correctement lors du redémarrage.

{{< youtube-rgpd "VHE9VnW3ccw" >}}

### Ce que vous allez apprendre dans cet épisode :
*   **Intégration d'un écran de Game Over :** Utilisation des objets prédéfinis de GDevelop pour afficher rapidement une interface de défaite.
*   **Gestion des calques :** Création d'un calque dédié pour superposer l'interface au-dessus de votre scène 3D.
*   **Utilisation des ancres :** Assurer que votre menu reste parfaitement centré, quelle que soit la résolution de l'écran.
*   **Contrôle du temps :** Utilisation de l'échelle de temps (*Time Scale*) pour "figer" le jeu tout en gardant les menus interactifs.
*   **Gestion des variables globales :** Réinitialiser correctement le score à zéro lors du redémarrage de la scène pour éviter les cumuls indésirables.

### Ce qui reste d'actualité aujourd'hui
*   **La logique des calques :** La séparation entre le monde 3D et l'interface utilisateur (UI) reste la méthode standard et la plus efficace pour concevoir des jeux propres sur GDevelop.
*   **L'échelle de temps :** La manipulation de `TimeScale` est toujours la technique recommandée pour mettre un jeu en pause sans arrêter le moteur de rendu ou les événements de l'interface.
*   **La gestion des variables :** Bien comprendre la différence entre une variable de scène et une variable globale est crucial pour éviter les bugs de persistance de données entre les niveaux.
*   **Les ancres :** Le comportement "Ancre" est indispensable pour le responsive design, garantissant que vos menus ne flottent pas n'importe où sur les écrans des joueurs.

{{< footer >}}
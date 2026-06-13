---
title: "14. Créer des menus interactifs"
weight: 14
prev_url: "/game-maker-studio/shoot-them-up/gerer-collisions-defaite-joueur-gamemaker/"
next_url: "/game-maker-studio/shoot-them-up/gerer-afficher-score-global-gamemaker-studio/"
date: 2024-05-22
categories: ['Archive']
tags: ['GameMaker', 'Tutoriel', 'UI', 'Game Design']
---

Apprendre à concevoir des menus fonctionnels est une étape cruciale pour transformer votre prototype en un véritable jeu vidéo. Dans ce guide, nous explorons comment créer des boutons personnalisés et gérer la navigation entre les différentes salles (rooms) de votre projet.

{{< youtube-rgpd "YzaHUjgKxlE" >}}

### Résumé des notions clés

La création d'une interface utilisateur (UI) dans GameMaker Studio repose sur une méthodologie simple mais efficace :

*   **Conception graphique :** Utilisation d'outils externes (comme Paint.NET) pour créer des assets transparents au format PNG. Il est essentiel de travailler sur des calques séparés pour conserver la transparence lors de l'exportation.
*   **Importation et configuration :**
    *   Importation des images en tant que `Sprites`.
    *   Réglage du masque de collision sur "Full Image" pour assurer une détection précise des clics.
    *   Création d'objets dédiés pour chaque bouton.
*   **Logique de navigation :**
    *   Utilisation de l'événement `Mouse Left Button` pour déclencher des actions.
    *   Utilisation de la fonction `room_goto` (ou l'action "Go to room") pour changer de niveau.
    *   Utilisation de la commande `game_end()` pour fermer l'application.
*   **Gestion des flux :** Duplication de salles existantes pour créer rapidement des menus (Menu principal, Game Over) tout en conservant les éléments de décor.
*   **Transitions :** Appel des menus de défaite directement dans les événements de collision du vaisseau joueur.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions récentes de GameMaker (GMS2/GMS2023+) aient introduit des systèmes plus avancés comme les *Sequences* ou les *UI Layers*, les principes fondamentaux présentés ici restent la base de tout développement :

1.  **La séparation des responsabilités :** Créer un objet par bouton est toujours une excellente pratique pour maintenir un code propre et modulaire.
2.  **La gestion des ressources :** L'importance de l'exportation en PNG avec transparence est une règle d'or qui ne change pas, quel que soit le moteur utilisé.
3.  **La logique événementielle :** La structure "Événement souris -> Action de changement de salle" demeure le standard pour les menus simples. Même si vous passez au GML (GameMaker Language) pur, la logique de `room_goto()` reste la méthode privilégiée pour naviguer dans votre jeu.
4.  **L'optimisation du workflow :** La technique de duplication de salles pour créer des menus est une astuce de productivité qui permet de gagner un temps précieux lors du prototypage.

{{< footer >}}
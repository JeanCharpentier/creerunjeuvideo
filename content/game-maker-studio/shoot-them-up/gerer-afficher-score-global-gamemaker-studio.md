---
title: "15. Gérer et afficher un score global"
weight: 15
prev_url: "/game-maker-studio/shoot-them-up/creer-menus-interactifs-gamemaker-studio/"
next_url: "/game-maker-studio/shoot-them-up/gerer-score-affichage-game-over-gamemaker/"
date: 2023-10-27
categories: ['Archive']
tags: ['GameMaker', 'Tutoriel', 'Programmation', 'Gamedev']
images: ["https://img.youtube.com/vi/zTWULvHy9Ck/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/zTWULvHy9Ck/maxresdefault.jpg"]
---

Apprendre à intégrer un système de score dynamique est une étape fondamentale pour tout développeur débutant sur GameMaker Studio.

{{< youtube-rgpd "zTWULvHy9Ck" >}}

### Résumé des notions clés

Dans ce tutoriel, nous abordons la mise en place d'un système de score persistant à travers les différentes salles de votre jeu :

*   **Création d'un objet contrôleur :** Utilisation d'un objet invisible (sans sprite) dédié à la gestion du score, permettant de centraliser la logique sans encombrer vos autres objets.
*   **Variables globales (`global.variable`) :** Comprendre la différence entre une variable locale (propre à un objet) et une variable globale, accessible par n'importe quel élément du jeu.
*   **Initialisation dans l'événement `Create` :** Définition des valeurs de départ (ex: `global.points = 0`) dès le lancement de l'objet.
*   **Gestion des couleurs personnalisées :** Utilisation de la fonction `make_color_rgb` pour créer des teintes sur mesure au-delà des constantes par défaut.
*   **Affichage dynamique :** Utilisation de l'événement `Draw` combiné à la fonction `draw_text` pour projeter le score à l'écran à chaque frame.
*   **Configuration de la Room :** Ne pas oublier de placer l'objet "score" dans votre Room pour que le code soit exécuté.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions récentes de GameMaker (GMS2 et versions ultérieures) aient introduit des outils plus modernes comme les *Sequences* ou les *GUI Layers*, les concepts présentés ici restent le socle de la programmation de jeux 2D :

1.  **La puissance des variables globales :** Elles restent indispensables pour stocker des données persistantes comme le score, le niveau du joueur ou les paramètres de sauvegarde.
2.  **La séparation des responsabilités :** Créer un objet "Game Manager" ou "Score Manager" invisible est toujours la meilleure pratique pour garder un projet propre et maintenable.
3.  **Le pipeline de rendu :** Comprendre que l'événement `Draw` est une boucle constante qui s'exécute à chaque image est crucial pour optimiser les performances de votre jeu.
4.  **La manipulation des couleurs :** La gestion RGB reste la norme pour personnaliser l'interface utilisateur (UI) et créer une identité visuelle cohérente.

{{< footer >}}
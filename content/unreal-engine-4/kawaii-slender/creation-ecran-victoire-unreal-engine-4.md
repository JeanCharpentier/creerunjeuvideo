---
title: "23. Création de l''écran de victoire et gestion de fin de partie"
weight: 23
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprint', 'HUD', 'UI', 'Game Design']
images: ["https://img.youtube.com/vi/s8QJ4oo3CJI/maxresdefault.jpg"]
---

Dans ce tutoriel, nous allons finaliser la logique de fin de partie de votre jeu. Après avoir configuré les menus de pause, il est temps de créer un système dynamique pour afficher l'écran de victoire lorsque le joueur atteint son objectif (collecter tous les cookies). Nous aborderons également la mise en pause du jeu et l'activation du curseur de la souris pour permettre au joueur de naviguer dans le menu de fin.

{{< youtube-rgpd "s8QJ4oo3CJI" >}}

### Résumé des étapes clés
*   **Préparation des assets :** Importation des images "Victoire" et "Game Over" dans votre projet.
*   **Configuration du HUD :** Création d'un widget unique contenant les deux images, configurées par défaut en mode "Hidden" (cachées).
*   **Variable de contrôle :** Utilisation de l'option "Is Variable" sur les images pour pouvoir modifier leur visibilité via le Blueprint.
*   **Logique dans le Level Blueprint :**
    *   Utilisation de l'**Event Tick** pour vérifier en continu le nombre de cookies collectés.
    *   Mise en place d'une condition (`Branch`) avec un opérateur "supérieur ou égal" pour déclencher la victoire.
    *   Gestion de la visibilité des widgets via `Set Visibility`.
    *   Mise en pause du jeu (`Set Game Paused`) et activation du curseur (`Set Show Mouse Cursor`) pour une interface interactive.

### Ce qui reste d'actualité aujourd'hui
Bien que ce tutoriel utilise Unreal Engine 4, les concepts fondamentaux restent parfaitement transposables aux versions récentes (UE5) :
*   **Le système de Widgets (UMG) :** La gestion de la visibilité des éléments d'interface via les variables reste la méthode standard pour créer des menus dynamiques.
*   **Le Level Blueprint :** Bien que pour des projets complexes on préfère utiliser des `GameMode` ou des `PlayerController` dédiés, la logique de vérification via `Event Tick` reste un excellent point d'entrée pour comprendre les flux de données.
*   **La gestion de l'état du jeu :** Les fonctions `Set Game Paused` et `Set Show Mouse Cursor` sont toujours les piliers pour créer des menus de fin de partie fonctionnels et ergonomiques.

{{< footer >}}
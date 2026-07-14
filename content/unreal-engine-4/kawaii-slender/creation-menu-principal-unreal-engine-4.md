---
title: "21. Création et programmation d''un menu principal"
weight: 21
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['UI', 'Widget', 'Blueprints', 'Menu', 'GameDev']
images: ["https://img.youtube.com/vi/K5BmZzMh1kc/maxresdefault.jpg"]
---

Dans ce vingt-et-unième épisode de notre série dédiée au développement de jeux avec Unreal Engine 4, nous finalisons notre menu principal. Nous allons voir comment configurer la map dédiée au menu, afficher le curseur de la souris, et programmer les interactions de base pour naviguer entre les différentes options (Jouer, Quitter, Paramètres).

{{< youtube-rgpd "K5BmZzMh1kc" >}}

### Résumé des étapes clés
*   **Configuration de la Map :** Création d'un nouveau niveau dédié au menu et utilisation du *Level Blueprint* pour afficher le Widget au démarrage (*Event BeginPlay*).
*   **Affichage du curseur :** Utilisation du nœud `Set Show Mouse Cursor` pour permettre au joueur d'interagir avec les boutons du menu.
*   **Gestion de la visibilité :** Utilisation de `Set Visibility` pour basculer entre le menu principal et le sous-menu des options.
*   **Commandes console :** Programmation des boutons pour lancer le jeu (`Open Level`), quitter l'application (`Quit`) et ajuster la résolution (`r.SetRes`).
*   **Débogage :** Astuce sur l'utilisation de la touche "P" pour vérifier le *NavMesh* si votre personnage ne se déplace plus correctement.

### Ce qui reste d'actualité aujourd'hui
Bien que cet article traite d'Unreal Engine 4, les concepts fondamentaux abordés restent parfaitement transposables à **Unreal Engine 5** :
*   **Le système de Widgets (UMG) :** La logique de création et d'affichage via `Create Widget` et `Add to Viewport` est identique.
*   **Gestion des entrées :** La nécessité de configurer le *Player Controller* pour afficher le curseur est une étape incontournable dans toutes les versions du moteur.
*   **Modularité :** L'approche consistant à séparer les menus par des boîtes de visibilité (`Visibility Box`) reste une excellente pratique pour garder une interface propre et organisée.
*   **Commandes Console :** Les commandes de base comme `r.SetRes` fonctionnent toujours, bien que dans un projet moderne, on privilégiera souvent l'utilisation des *Game User Settings* via C++ ou Blueprints pour une gestion plus robuste des paramètres graphiques.

{{< footer >}}
---
title: "20. Création et intégration de l''interface utilisateur (HUD)"
weight: 20
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['UI', 'HUD', 'Widget Blueprint', 'GameDev']
images: ["https://img.youtube.com/vi/ti85sY0rvXs/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/ti85sY0rvXs/maxresdefault.jpg"]
---

Dans ce vingtième épisode, nous abordons une étape cruciale pour tout projet de jeu vidéo : la mise en place de l'interface utilisateur (HUD). Après avoir préparé vos assets graphiques, il est temps de les intégrer dans Unreal Engine 4 pour construire un menu fonctionnel, interactif et esthétique.

{{< youtube-rgpd "ti85sY0rvXs" >}}

### Résumé du tutoriel
*   **Importation des assets :** Création d'un dossier dédié et importation des textures (fond, boutons) en veillant à bien gérer les paramètres d'importation.
*   **Création du Widget Blueprint :** Mise en place du `MenuHUD` via l'interface utilisateur d'Unreal.
*   **Configuration du fond :** Utilisation d'un composant *Image* avec un ancrage complet pour garantir une adaptation à toutes les résolutions.
*   **Structure du menu :** Utilisation de *Vertical Box* pour organiser les boutons de manière propre et réactive.
*   **Gestion des états des boutons :** Configuration des styles (Normal, Hovered, Pressed) pour offrir un retour visuel au joueur lors de l'interaction.
*   **Superposition des menus :** Stratégie consistant à créer deux boîtes (Menu principal et Options) dans le même HUD pour basculer facilement entre les deux en masquant/affichant les éléments.
*   **Variable d'accès :** Activation de l'option "Is Variable" sur les conteneurs pour permettre une manipulation dynamique via le Blueprint par la suite.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes d'Unreal Engine (UE5) aient introduit des outils plus avancés comme *Common UI*, les principes fondamentaux présentés ici restent parfaitement valables :
1.  **L'importance de l'ancrage (Anchors) :** C'est la base pour créer des interfaces "Responsive" qui ne se déforment pas selon le ratio d'écran.
2.  **La hiérarchie des Widgets :** L'utilisation de conteneurs comme les *Vertical Box* ou *Overlay* est toujours la méthode standard pour structurer une interface.
3.  **Le workflow de design :** Séparer les états des boutons (Normal/Hover/Pressed) reste la norme pour garantir une expérience utilisateur (UX) intuitive.
4.  **La logique de visibilité :** La technique de superposer des menus et de gérer leur visibilité (`Set Visibility`) est une méthode légère et efficace, toujours très utilisée pour les menus simples.

{{< footer >}}
---
title: "6. Personnalisation des assets et intégration graphique"
weight: 6
date: 2026-06-17
categories: ['Raycasting GameMaker']
tags: ['GameDev', 'Raycasting', 'GameMaker', 'Assets', 'FPS']
---

Dans cet épisode hors-série de notre série sur la création d'un FPS avec Raycasting GameMaker, nous mettons de côté le code pur pour nous concentrer sur l'identité visuelle de votre projet. L'objectif est de vous donner les clés pour intégrer vos propres armes, menus et éléments d'interface (HUD) afin de rendre votre jeu unique.

{{< youtube-rgpd "EWQ4u8Mwhuc" >}}

### Résumé de l'épisode
*   **Liberté créative :** Vous êtes libres d'utiliser vos outils préférés (Photoshop, GIMP, Paint.NET) pour créer vos assets.
*   **Localisation des fichiers :** Rappel sur l'accès au dossier des ressources via le menu `Game Beat Maps` > `Open Game Beat Maps folder`.
*   **Contraintes techniques :** Les images d'animation des armes doivent impérativement respecter les dimensions de 64x64 pixels.
*   **Workflow :** Démonstration de l'intégration d'un AK-47 et d'un USP (style Counter-Strike) avec leurs sprites de tir et leurs "pickups" (objets au sol).
*   **Interface :** Conseils sur la modification des menus et du viseur (crosshair) pour personnaliser l'expérience utilisateur.

### Ce qui reste d'actualité aujourd'hui
Bien que les outils de création d'images évoluent, les principes fondamentaux de l'intégration dans Raycasting GameMaker restent inchangés :
1.  **Le respect des dimensions :** Le moteur de raycasting repose sur des grilles de sprites fixes. Le format 64x64 reste la norme pour garantir que vos animations d'armes s'affichent correctement sans déformation.
2.  **La structure des dossiers :** Comprendre comment le logiciel lit les fichiers dans le dossier `Game Beat Maps` est essentiel pour tout développeur souhaitant créer des mods ou des jeux complets.
3.  **L'importance du "Pickup" :** Créer un sprite dédié pour l'objet posé au sol (le pickup) est une étape souvent oubliée, mais cruciale pour l'immersion et le gameplay.
4.  **Flexibilité logicielle :** Le moteur est agnostique quant à l'outil de création. Que vous soyez sur un logiciel professionnel ou gratuit, tant que vous exportez en PNG avec les bonnes dimensions, le moteur acceptera vos créations.

{{< footer >}}
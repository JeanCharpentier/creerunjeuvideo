---
title: "7. Placer les objets, armes et points de spawn dans Unreal Engine 3"
weight: 7
date: 2026-06-17
categories: ['GameDev']
tags: ['Unreal Engine 3', 'UDK', 'FPS', 'Level Design']
---

Dans ce septième épisode de notre série dédiée au développement d'un FPS avec l'Unreal Development Kit (UDK), nous passons à une étape cruciale : le "peuplage" de votre carte. Un niveau vide est une chose, mais un niveau jouable en nécessite une autre : des armes, des munitions, de la santé et des points de réapparition stratégiques.

{{< youtube-rgpd "QC-NRMFqkVI" >}}

### Ce que vous allez apprendre dans cet épisode :
*   **Utilisation du Content Browser :** Navigation dans l'onglet *Actor Classes* pour trouver les objets interactifs.
*   **Configuration des Pickups :** Placement et paramétrage des `UTWeaponPickupFactory` pour intégrer le lance-roquettes, le Shock Rifle et le Link Gun.
*   **Gestion des ressources :** Ajout de packs de santé, d'armures et de munitions pour dynamiser le gameplay.
*   **Configuration du GameType :** Réglage des *World Properties* pour définir le mode de jeu (Deathmatch) afin que les armes et les bots fonctionnent correctement.
*   **Système de Spawn :** Placement et orientation des `PlayerStart` pour garantir une expérience multijoueur équilibrée.
*   **Astuces de gameplay :** Utilisation du tir secondaire du Shock Rifle pour créer des explosions combinées.

### Ce qui reste d'actualité aujourd'hui
Bien que l'Unreal Engine 3 (UDK) soit aujourd'hui considéré comme un moteur "legacy", les principes fondamentaux abordés ici restent le socle de tout développement de FPS moderne :
*   **La logique des Factories :** Le concept d'objets "Factory" qui génèrent des items (respawn) est toujours présent sous d'autres formes dans l'UE4 et l'UE5 (via les *Actor Blueprints*).
*   **L'importance du Level Design :** Le placement stratégique des armes et des points de vie reste le cœur de l'équilibrage d'une carte multijoueur.
*   **Navigation et Bots :** La nécessité de reconstruire les chemins de navigation (*Build Paths*) après avoir ajouté des objets interactifs est une étape indispensable dans n'importe quel moteur pour que l'IA puisse interagir avec l'environnement.
*   **Workflow de test :** L'itération rapide (placer, compiler, tester) est la méthode de travail standard de tout développeur de jeu, quel que soit l'outil utilisé.

{{< footer >}}
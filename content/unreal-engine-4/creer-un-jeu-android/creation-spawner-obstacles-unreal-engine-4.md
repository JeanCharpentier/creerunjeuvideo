---
title: "15. Création d''un Spawner pour vos obstacles"
weight: 15
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprint', 'GameDev', 'Spawner', 'Tutoriel']
---

Dans cet épisode, nous allons automatiser l'apparition de nos obstacles. Plutôt que de placer manuellement chaque tronc dans le niveau, nous allons créer un "Spawner" (générateur) dédié. Ce système nous permettra de contrôler précisément le rythme et la position des objets, garantissant ainsi une expérience de jeu équitable pour tous les joueurs, essentielle pour un système de classement (leaderboard).

{{< youtube-rgpd "XS97TG91xvQ" >}}

### Résumé de la mise en place
*   **Création du Blueprint Spawner :** Création d'un nouvel acteur nommé `BP_Spawner`. Cet objet sera invisible en jeu, mais servira de point d'ancrage logique.
*   **Initialisation :** Utilisation de l'événement `BeginPlay` pour récupérer la référence du joueur (via `GetPlayerPawn`), identique à la configuration du tronc.
*   **Automatisation avec l'Event Tick :** Utilisation du node `Event Tick` couplé à un `Delay` (réglé sur 1 seconde) pour cadencer l'apparition des objets.
*   **Spawn Actor :** Utilisation du node `SpawnActorFromClass` pour instancier le `BP_Tron`.
*   **Gestion des Transforms :** Utilisation du node `MakeTransform` pour définir la position, la rotation et l'échelle d'apparition.
*   **Variante aléatoire :** Possibilité d'utiliser `Random Float in Range` pour varier la position Y des troncs, bien que nous privilégierons une approche par tableau de vecteurs pour un contrôle total.

### Ce qui reste d'actualité aujourd'hui
Bien que cet épisode utilise Unreal Engine 4, les concepts fondamentaux restent identiques dans les versions plus récentes (UE5) :
1.  **La logique de Spawn :** Le node `SpawnActorFromClass` est toujours la méthode standard pour faire apparaître des objets dynamiquement.
2.  **L'importance du Transform :** La manipulation des structures `Transform` (Location, Rotation, Scale) est le cœur du placement d'objets dans l'espace 3D.
3.  **Architecture de code :** Séparer la logique de génération (Spawner) de la logique de l'objet (Tronc) est une bonne pratique de programmation orientée objet qui facilite la maintenance et l'évolutivité de votre projet.
4.  **Déterminisme :** Le choix de préférer des positions pré-programmées à l'aléatoire pur est une excellente stratégie pour le "Game Design" compétitif, permettant de créer des niveaux "parfaits" ou des défis identiques pour tous les joueurs.

{{< footer >}}
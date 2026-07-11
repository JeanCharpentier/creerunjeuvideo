---
title: "44. Créer un système de Checkpoint"
weight: 44
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprints', 'GameDev', 'Checkpoint', 'Gameplay']
images: ["https://img.youtube.com/vi/vxiQ9odjUJo/maxresdefault.jpg"]
---

Dans cet épisode, nous allons apprendre à implémenter un système de checkpoint efficace. L'objectif est simple : éviter que le joueur ne doive recommencer tout le niveau après une chute ou une erreur, en le téléportant à sa dernière position validée.

{{< youtube-rgpd "vxiQ9odjUJo" >}}

### Résumé de la mise en place
*   **Variable de suivi :** Création d'une variable `DernierCheckpoint` de type *Vector* dans le `FirstPersonCharacter`.
*   **Initialisation :** Utilisation de l'événement `BeginPlay` pour définir la position de départ du joueur comme premier checkpoint.
*   **Zone de défaite :** Modification du Blueprint `ZoneDeDefaite` pour utiliser `SetActorLocation` vers la valeur de `DernierCheckpoint` au lieu de recharger le niveau.
*   **Création du Checkpoint :** Création d'un acteur `ZoneCheckpoint` avec une `BoxCollision`.
*   **Logique de collision :** Utilisation du `CastToFirstPersonCharacter` pour mettre à jour la variable `DernierCheckpoint` du joueur lors du passage dans la zone.
*   **Optionnel :** Ajout d'un nœud `DestroyActor` après la mise à jour du checkpoint pour empêcher le joueur de revenir sur un ancien point de sauvegarde.

### Ce qui reste d'actualité aujourd'hui
Bien que cet article traite d'Unreal Engine 4, les concepts fondamentaux restent parfaitement transposables à **Unreal Engine 5** :
*   **Gestion des variables :** Le système de variables (Vector) et le `Cast` restent les piliers de la communication entre les Blueprints.
*   **Transform vs Location :** La distinction entre `SetActorLocation` (position seule) et `SetActorTransform` (position, rotation et échelle) est toujours une notion clé pour gérer le réapparition du joueur avec son orientation initiale.
*   **Modularité :** L'utilisation d'acteurs dédiés pour les zones (trigger volumes) est une pratique standard qui permet de garder un projet propre et facilement éditable dans le viewport.
*   **Persistence :** La logique de destruction de l'acteur (`DestroyActor`) après activation est une technique classique pour gérer la progression linéaire dans les jeux de plateforme ou d'aventure.

{{< footer >}}
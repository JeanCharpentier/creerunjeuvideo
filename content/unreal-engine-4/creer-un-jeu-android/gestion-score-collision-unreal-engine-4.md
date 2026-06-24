---
title: "18. Gestion du score et logique de collision"
weight: 18
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprints', 'Game Logic', 'Collision', 'Gameplay']
---

Dans cet épisode, nous allons structurer la logique de score de notre jeu. Jusqu'ici, nous savions détecter une collision pour le "Game Over", mais il est temps d'ajouter une mécanique de points gratifiante sans pour autant permettre au joueur de "tricher" en accumulant des points à l'infini lors d'un seul passage.

{{< youtube-rgpd "yZbrNqECy9U" >}}

### Résumé de la mise en place
*   **Extension de la logique de collision :** Utilisation de branches (`Branch`) successives pour tester quel composant est touché (Box Game Over vs Box Points).
*   **Gestion des variables :** Création d'une variable `Points` (Integer), rendue éditable pour un accès facilité.
*   **Le problème du "Multi-trigger" :** Constat que le chevauchement (overlap) déclenche l'incrémentation plusieurs fois par seconde.
*   **Utilisation du node `DoOnce` :** Mise en place d'une exécution unique pour éviter le spam de points.
*   **Réinitialisation via `Event Tick` :** Utilisation du `Character Movement Component` et de la fonction `IsFalling` pour détecter quand le joueur touche le sol, permettant ainsi de réinitialiser le `DoOnce` via un `Custom Event`.

### Ce qui reste d'actualité aujourd'hui
Bien que cet épisode traite d'Unreal Engine 4, les concepts fondamentaux restent parfaitement valables dans Unreal Engine 5 :

1.  **La hiérarchie des composants :** L'utilisation de `GetChildComponent` reste une méthode efficace pour identifier des éléments spécifiques dans un Blueprint, bien que l'utilisation de *Tags* ou de *Casting* soit souvent recommandée pour plus de robustesse.
2.  **Le `DoOnce` :** C'est un outil indispensable en Blueprint pour verrouiller une logique. Il est très utile pour les systèmes de ramassage d'objets ou les déclencheurs de cinématiques.
3.  **L'Event Tick et la performance :** L'utilisation de l'Event Tick pour vérifier l'état du personnage (`IsFalling`) est une approche classique. Attention toutefois : dans des projets complexes, il est préférable d'utiliser des `Delegates` (ou *Event Dispatchers*) pour éviter de surcharger le Tick.
4.  **Custom Events :** La création d'événements personnalisés est la base de la modularité en Blueprint. Cela permet de garder un graphe propre et réutilisable.

{{< footer >}}
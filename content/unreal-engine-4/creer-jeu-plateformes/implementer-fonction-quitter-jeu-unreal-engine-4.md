---
title: "32. Implémenter une fonction Quitter le jeu dans Unreal Engine 4"
weight: 32
date: 2026-06-17
categories: ['Développement Unreal Engine']
tags: ['Unreal Engine 4', 'Blueprints', 'Level Blueprint', 'Console Command']
images: ["https://img.youtube.com/vi/d5FKwLmvvIQ/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/d5FKwLmvvIQ/maxresdefault.jpg"]
---

Dans cet épisode, nous abordons une fonctionnalité essentielle pour tout projet : la gestion de la sortie du jeu. Que ce soit pour revenir au menu principal, quitter l'application ou fermer une session après une victoire ou une défaite, il est crucial de savoir comment fermer proprement votre build. Nous allons utiliser le *Level Blueprint* pour déclencher une commande système simple mais efficace.

{{< youtube-rgpd "d5FKwLmvvIQ" >}}

### Résumé de la procédure
*   **Accès au Level Blueprint :** Ouvrez votre carte, allez dans le menu *Blueprints* et sélectionnez *Open Level Blueprint*.
*   **Gestion de l'input :** Utilisez l'événement `Escape` (ou une touche de test comme `P`) pour déclencher l'action.
*   **Commande système :** Utilisez le nœud *Execute Console Command* avec la commande `quit`.
*   **Test et nettoyage :** Testez votre commande avec une touche temporaire avant de supprimer le nœud de test pour la version finale.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Unreal Engine aient évolué, les principes fondamentaux restent identiques :
1.  **La commande `quit` :** Elle demeure la méthode standard pour fermer une application packagée via les Blueprints.
2.  **Le Level Blueprint :** Il reste l'endroit idéal pour gérer des entrées clavier globales qui ne dépendent pas d'un personnage spécifique.
3.  **Bonnes pratiques :** Il est toujours recommandé de tester vos commandes de sortie avec des touches alternatives pendant le développement, car la touche `Escape` est souvent réservée par l'éditeur pour arrêter la simulation (PIE - Play In Editor).
4.  **Modularité :** Pour des projets plus complexes, il est préférable de centraliser cette logique dans un *GameInstance* ou un *PlayerController* plutôt que dans le *Level Blueprint* afin de rendre la fonction disponible sur toutes les cartes du jeu.

{{< footer >}}
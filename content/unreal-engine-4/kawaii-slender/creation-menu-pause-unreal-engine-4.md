---
title: "22. Création d''un menu de pause fonctionnel"
weight: 22
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Tutoriel', 'UI', 'Widget', 'Blueprint', 'GameDev']
images: ["https://img.youtube.com/vi/-PCEYxS58k8/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/-PCEYxS58k8/maxresdefault.jpg"]
---

Dans ce vingt-deuxième épisode de notre série dédiée à la création d'un jeu de type "Kawaii Slender", nous nous attaquons à une fonctionnalité indispensable pour tout projet : le menu de pause. Ce menu permettra aux joueurs de reprendre leur partie, de réapparaître aléatoirement sur la carte en cas de blocage, ou de quitter le jeu.

{{< youtube-rgpd "-PCEYxS58k8" >}}

### Résumé des étapes clés
*   **Création du Widget :** Mise en place d'un `Pause HUD` avec une `Vertical Box` contenant trois boutons : "Reprendre", "Réapparaître" et "Quitter".
*   **Logique des boutons :**
    *   *Quitter :* Utilisation de la commande `Execute Console Command` avec l'argument `quit`.
    *   *Reprendre :* Suppression du widget (`Remove from Parent`).
    *   *Réapparaître :* Utilisation de la fonction `Teleport` couplée à `Get Random Point in Navigable Radius` pour repositionner le joueur sur le NavMesh.
*   **Gestion du Level Blueprint :** Configuration de la touche "P" pour basculer l'état du jeu (`Set Game Paused`) et afficher le curseur de la souris (`Set Show Mouse Cursor`).
*   **Gestion de l'état :** Utilisation d'une variable booléenne `EnPause` pour alterner entre l'affichage et la fermeture du menu.

### Ce qui reste d'actualité aujourd'hui
Bien que cet épisode traite d'Unreal Engine 4, les concepts fondamentaux restent parfaitement transposables aux versions plus récentes (UE5) :
*   **L'UI Widget :** La hiérarchie des composants (Vertical Box, Buttons) et le système de `Designer` restent identiques.
*   **Le Game State :** La gestion de la pause via `Set Game Paused` est une méthode standard qui ne change pas.
*   **Le NavMesh :** La logique de téléportation aléatoire sur une zone navigable (`Get Random Point in Navigable Radius`) est toujours la méthode privilégiée pour éviter que le joueur ne se retrouve "hors map" ou coincé dans la géométrie.
*   **Input Handling :** Bien que l'Enhanced Input System soit désormais la norme dans les nouveaux projets, la logique de déclenchement via une touche clavier reste le point de départ de toute interaction utilisateur.

{{< footer >}}
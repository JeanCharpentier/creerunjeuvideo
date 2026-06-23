---
title: "30. Créer un menu de victoire dans Unreal Engine 4"
weight: 30
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['UI', 'Widget Blueprint', 'GameDev', 'Tutoriel']
---

Dans cet épisode, nous allons finaliser l'expérience utilisateur en ajoutant un écran de victoire. Lorsqu'un joueur atteint la zone de fin de niveau, il est crucial de lui offrir un retour visuel clair avec des options pour continuer à jouer ou quitter l'application. Nous allons voir comment créer ce Widget, le lier à notre zone de victoire et gérer les interactions à la souris.

{{< youtube-rgpd "FbGUbXvjG50" >}}

### Résumé de l'implémentation
*   **Création du Widget :** Création d'un nouveau *Widget Blueprint* nommé `HUD_Victoire` dans le dossier UI.
*   **Design :** Mise en place d'une image de fond et de deux boutons (Rejouer et Quitter).
*   **Logique des boutons :**
    *   *Quitter :* Utilisation de la commande `Execute Console Command` avec la commande `quit`.
    *   *Rejouer :* Utilisation de `Open Level` pour charger la scène du menu principal.
*   **Déclenchement :** Modification du Blueprint `Zone_Victoire` pour remplacer la fermeture du jeu par l'affichage du widget.
*   **Interaction :** Utilisation de `Set Show Mouse Cursor` via le *Player Controller* pour permettre au joueur de cliquer sur les boutons.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Unreal Engine aient évolué (notamment avec l'arrivée d'UE5), les principes fondamentaux abordés ici restent le standard de l'industrie :
1.  **Le système UMG (Unreal Motion Graphics) :** La création de menus via des *Widget Blueprints* est toujours la méthode privilégiée pour les interfaces 2D.
2.  **La gestion du Player Controller :** La nécessité d'activer le curseur de la souris et de changer le mode d'entrée (*Input Mode UI Only*) reste une étape indispensable pour tout menu interactif.
3.  **Modularité :** La logique présentée ici est facilement réutilisable. Comme mentionné dans la vidéo, le processus pour un écran de "Défaite" est identique, ce qui permet de créer des systèmes de gestion d'état de jeu très rapidement.
4.  **Commandes Console :** L'utilisation de `Execute Console Command` pour quitter le jeu reste une méthode rapide et efficace pour les prototypes et les builds de développement.

{{< footer >}}
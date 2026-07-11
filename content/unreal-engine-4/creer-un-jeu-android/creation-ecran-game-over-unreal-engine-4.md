---
title: "23. Création de l''écran de Game Over et gestion du score"
weight: 23
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['GameDev', 'UE4', 'Blueprints', 'UI', 'Widget']
images: ["https://img.youtube.com/vi/zC8pPbEwh2s/maxresdefault.jpg"]
---

Dans cet épisode, nous allons finaliser l'expérience utilisateur en créant un écran de "Game Over" fonctionnel. Lorsqu'un joueur perd, il est crucial de lui offrir un retour visuel clair, d'afficher son score final et de lui proposer une option pour retourner au menu principal ou attendre une redirection automatique.

{{< youtube-rgpd "zC8pPbEwh2s" >}}

### Résumé de la mise en place
*   **Création du Widget :** Conception d'un nouveau `User Widget` (WBP_GameOver) avec un texte de défaite, l'affichage dynamique du score et un bouton de retour.
*   **Gestion des ancres :** Rappel sur l'importance de bien ancrer vos éléments UI pour garantir une compatibilité avec toutes les résolutions d'écran.
*   **Logique de redirection :** Utilisation de l'événement `Event Construct` couplé à un `Delay` pour automatiser le retour au menu principal après 15 secondes.
*   **Affichage dynamique du score :** Utilisation du `Cast To` vers votre Character pour récupérer la variable de score et l'injecter dans le widget via un `Set Text`.
*   **Nettoyage de l'interface :** Utilisation de la fonction `Remove from Parent` pour supprimer l'affichage du score en cours de jeu avant d'afficher l'écran de Game Over, évitant ainsi les superpositions visuelles.

### Ce qui reste d'actualité aujourd'hui
*   **La modularité des Widgets :** La méthode consistant à créer des widgets séparés pour chaque état du jeu (Menu, HUD, Game Over) reste la norme pour garder un projet propre et maintenable.
*   **Le Cast To :** Bien que dans des projets complexes on privilégie souvent les *Interfaces* ou l'*Event Dispatching* pour éviter les dépendances directes, le `Cast To` reste l'outil le plus rapide et le plus pédagogique pour débuter sur UE4.
*   **Gestion du cycle de vie :** L'utilisation de `Remove from Parent` est toujours la méthode standard pour gérer la destruction des éléments d'interface utilisateur en Blueprint.
*   **UX et monétisation :** L'idée d'ajouter un délai sur l'écran de fin de partie est une pratique courante dans le jeu mobile pour laisser le temps à une publicité interstitielle de se charger ou d'être visionnée.

{{< footer >}}
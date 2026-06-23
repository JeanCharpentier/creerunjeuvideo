---
title: "21. Créer une interface utilisateur (UI) pour afficher votre score"
weight: 21
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['UI', 'Widget', 'Blueprint', 'HUD', 'GameDev']
---

Dans cet épisode, nous quittons la console de débogage pour offrir à nos joueurs une interface visuelle propre. Nous allons apprendre à créer un **Widget Blueprint** pour afficher le score en temps réel à l'écran, une étape essentielle pour transformer votre prototype en un véritable jeu.

{{< youtube-rgpd "" >}}

### Résumé de la mise en place
*   **Création du Widget :** Utilisation du menu *User Interface > Widget Blueprint* (nommé `WD_Score` par convention).
*   **Configuration visuelle :** Ajout d'un élément *Text* dans le designer, avec un réglage précis des ancres (Anchors) pour garantir la compatibilité avec toutes les résolutions d'écran.
*   **Binding de données :** Création d'une fonction de liaison (*Binding*) pour mettre à jour dynamiquement le texte en fonction de la variable `Points` stockée dans le personnage.
*   **Manipulation de chaînes :** Utilisation du node `Build String (Int)` pour concaténer le label "Score : " avec la valeur numérique de notre variable.
*   **Affichage à l'écran :** Utilisation de l'événement `Event Begin Play` dans le Character Blueprint pour instancier le widget via `Create Widget` et l'ajouter au viewport avec `Add to Viewport`.
*   **Nettoyage :** Suppression des anciens `Print String` dans le Character pour une interface épurée.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Unreal Engine aient évolué (UE5), les principes fondamentaux de l'UI restent identiques :
1.  **Le système UMG (Unreal Motion Graphics) :** Le workflow de création de widgets via le designer et les bindings est toujours la méthode standard pour les interfaces simples.
2.  **Les Ancres :** La gestion des ancres est cruciale dans n'importe quelle version d'Unreal pour éviter que les éléments d'interface ne se décalent sur des écrans ultra-wide ou des résolutions mobiles.
3.  **Le Binding vs Event-Driven :** Si le *Binding* est simple à mettre en place, gardez à l'esprit que pour des projets plus complexes, il est préférable d'utiliser des **Events (Dispatcher)** pour mettre à jour l'UI uniquement quand le score change, plutôt que de recalculer la valeur à chaque frame (ce qui est le comportement par défaut du binding).
4.  **Modularité :** La séparation entre la logique (Character) et la vue (Widget) reste une bonne pratique de programmation pour maintenir un code propre et évolutif.

{{< footer >}}
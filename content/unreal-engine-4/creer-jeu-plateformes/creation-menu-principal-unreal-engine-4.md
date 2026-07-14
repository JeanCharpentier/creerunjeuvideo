---
title: "28. Création du Menu Principal et gestion de l''interface"
weight: 28
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['UI', 'UMG', 'Blueprint', 'Menu', 'GameDev']
images: ["https://img.youtube.com/vi/-d5nDYQ7UGY/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/-d5nDYQ7UGY/maxresdefault.jpg"]
---

Dans cet épisode, nous abordons une étape cruciale pour tout projet de jeu vidéo : la création du menu principal. Nous allons voir comment configurer une scène dédiée, concevoir une interface utilisateur (UI) avec le système UMG (Unreal Motion Graphics) et rendre les boutons interactifs pour naviguer dans votre jeu.

{{< youtube-rgpd "-d5nDYQ7UGY" >}}

### Résumé des étapes clés
*   **Création de la Map Menu :** Mise en place d'une nouvelle carte vide dédiée exclusivement à l'affichage du menu.
*   **Conception du Widget Blueprint :** Utilisation de l'outil UMG pour ajouter une image de fond et des boutons (Jouer, Quitter, Plein écran).
*   **Gestion des ancres (Anchors) :** Configuration des ancres pour assurer une mise en page responsive, quel que soit le format d'écran.
*   **Programmation du Level Blueprint :** Affichage du widget au lancement de la scène via `Create Widget` et `Add to Viewport`.
*   **Activation du curseur :** Utilisation du node `Set Show Mouse Cursor` pour permettre au joueur d'interagir avec les éléments de l'interface.
*   **Logique des boutons :** Implémentation des événements `OnClicked` pour charger les niveaux (`Open Level`) ou quitter l'application (`Execute Console Command`).

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes d'Unreal Engine (UE5) aient introduit des améliorations dans l'éditeur UMG, les fondamentaux présentés ici restent parfaitement valides :
*   **Le workflow UMG :** La création de widgets via le Content Browser et leur ajout au Viewport via le Level Blueprint est toujours la méthode standard pour les menus simples.
*   **Le Player Controller :** La gestion du curseur de la souris via le `Player Controller` est une notion immuable dans l'architecture d'Unreal Engine.
*   **La modularité :** L'utilisation de `Execute Console Command` pour des fonctions système comme "Quit" reste une solution rapide et efficace pour le prototypage.
*   **Bonnes pratiques :** L'importance de bien nommer ses composants (ex: `BTN_Jouer`) et d'utiliser les ancres pour éviter les problèmes d'affichage sur différentes résolutions est une règle d'or qui ne change pas avec les versions du moteur.

{{< footer >}}
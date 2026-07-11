---
title: "47. Création d''un menu de sauvegarde et gestion de l''interface"
weight: 47
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['UI', 'Widget', 'Blueprints', 'Sauvegarde', 'GameDev']
images: ["https://img.youtube.com/vi/TxtT7ZKBxqY/maxresdefault.jpg"]
---

Dans cet épisode, nous posons les bases techniques nécessaires à la mise en place d'un système de sauvegarde persistante. Avant de manipuler les données, il est indispensable de créer une interface utilisateur (UI) permettant au joueur d'interagir avec le système de sauvegarde. Nous allons voir comment créer un menu simple et gérer son affichage via le Blueprint de votre personnage.

{{< youtube-rgpd "TxtT7ZKBxqY" >}}

### Résumé de la mise en place
*   **Création du Widget :** Conception d'un menu basique contenant deux boutons (sans logique pour le moment).
*   **Logique d'affichage (Flip Flop) :** Utilisation du node `Flip Flop` pour alterner entre l'ouverture et la fermeture du menu à chaque pression de la touche 'P'.
*   **Gestion des variables :** Stockage du widget dans une variable (`W_Menu`) pour pouvoir le manipuler (l'ajouter au viewport ou le supprimer) sans avoir à le recréer.
*   **Interaction souris :** Utilisation du node `Set Show Mouse Cursor` pour permettre au joueur de cliquer sur les boutons, en ciblant correctement le `Player Controller`.
*   **Nettoyage :** Utilisation de `Remove from Parent` pour libérer l'interface de l'écran.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Unreal Engine aient évolué, les principes fondamentaux abordés ici restent des piliers du développement :
1.  **Le pattern Flip Flop :** C'est toujours la méthode la plus rapide et efficace pour créer des bascules (toggle) simples dans vos Blueprints.
2.  **Gestion des Widgets :** La promotion en variable (`Promote to Variable`) est une bonne pratique indispensable pour éviter les fuites de mémoire ou les erreurs de référence lors de la manipulation d'UI.
3.  **Le Player Controller :** La distinction entre le *Character* (le corps) et le *Player Controller* (l'input/la souris) est une règle d'or dans UE4 et UE5. Comprendre que le curseur appartient au contrôleur est essentiel pour éviter les bugs d'input.
4.  **Débogage :** Comme montré dans la vidéo, savoir lire les messages d'erreur du compilateur (notamment sur les cibles invalides) est la compétence la plus précieuse pour un développeur.

{{< footer >}}
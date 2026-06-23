---
title: "31. Création d''un menu de défaite (Game Over) dans Unreal Engine 4"
weight: 31
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['UI', 'Widget Blueprint', 'Game Design', 'Tutoriel']
---

Dans cet épisode, nous allons finaliser l'expérience utilisateur en cas d'échec dans votre jeu. Plutôt que de laisser le joueur face à un écran figé, nous allons implémenter un menu de "Game Over" fonctionnel. L'approche choisie ici est l'optimisation : au lieu de repartir de zéro, nous allons dupliquer notre interface de victoire pour y intégrer un message d'alerte tout en conservant les options de navigation essentielles (rejouer ou quitter).

{{< youtube-rgpd "veUnQ82xKkE" >}}

### Résumé des étapes clés
*   **Duplication de l'UI :** Utilisation du widget de victoire existant comme base pour créer le `WBP_Defaite`.
*   **Personnalisation visuelle :** Ajout d'un élément `Text` centré affichant "Game Over" en rouge, avec une police agrandie pour un impact immédiat.
*   **Logique de déclenchement :** Configuration du Blueprint pour instancier le widget lors de la collision avec une zone de défaite.
*   **Gestion du curseur :** Utilisation de la fonction `Set Show Mouse Cursor` pour permettre au joueur d'interagir avec les boutons du menu.
*   **Correction de bug :** Importance de cocher la case "Show Mouse Cursor" dans le nœud `Set Show Mouse Cursor` pour garantir l'affichage du pointeur à l'écran.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes d'Unreal Engine (UE5) aient introduit des outils comme *Common UI*, les principes fondamentaux abordés ici restent le socle du développement d'interfaces :
1.  **Réutilisation des assets :** La duplication et la modification de widgets existants restent une méthode efficace pour maintenir une cohérence visuelle tout en gagnant du temps.
2.  **Gestion du Player Controller :** La nécessité de basculer l'input du jeu vers l'UI (via `Set Show Mouse Cursor` et `Set Input Mode UI Only`) est une étape incontournable dans n'importe quelle version du moteur.
3.  **Modularité :** Séparer la logique de défaite dans un widget dédié permet de garder un code propre et facilement modifiable si vous décidez plus tard d'ajouter des animations ou des effets sonores spécifiques au Game Over.

{{< footer >}}
---
title: "29. Créer un bouton de bascule Plein Écran / Fenêtré"
weight: 29
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprints', 'UI', 'GameDev', 'Tutoriel']
---

Dans cet épisode, nous allons apprendre à gérer l'affichage de notre jeu en permettant aux joueurs de basculer dynamiquement entre le mode "Plein écran" et le mode "Fenêtré". Pour ce faire, nous utiliserons les Blueprints pour manipuler les variables d'état et les commandes de console intégrées à Unreal Engine 4.

{{< youtube-rgpd "kbHNt4dFauY" >}}

### Résumé de la mise en place
*   **Gestion d'état :** Création d'une variable booléenne `PleinEcran` (par défaut à `true`) pour suivre le mode d'affichage actuel.
*   **Logique de bascule :** Utilisation d'un nœud `Branch` pour tester la valeur de la variable à chaque clic sur le bouton.
*   **Mode Fenêtré :** Utilisation de la commande `r.SetRes 1280x720w` pour forcer une résolution spécifique en mode fenêtré.
*   **Mode Plein Écran dynamique :**
    *   Récupération des résolutions supportées via `Get Supported Fullscreen Resolutions`.
    *   Extraction de la résolution maximale via le dernier index du tableau (`Last Index`).
    *   Utilisation du nœud `Append` pour construire dynamiquement la commande `r.SetRes` avec les valeurs X et Y récupérées, suivie du paramètre `f` pour le plein écran.
*   **Mise à jour de l'état :** Utilisation du nœud `Set` pour inverser la valeur de la variable `PleinEcran` après chaque changement.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes d'Unreal Engine (UE5) proposent des nœuds plus modernes comme `Set Game User Settings`, la logique présentée ici reste fondamentale pour comprendre :
1.  **La gestion des états :** L'utilisation de variables booléennes pour piloter l'interface utilisateur (UI).
2.  **La manipulation de tableaux :** Savoir récupérer la valeur maximale d'une liste (ici les résolutions) est une compétence clé en développement.
3.  **La construction de chaînes de caractères :** Le nœud `Append` est un outil indispensable pour formater des commandes ou des messages dynamiques.
4.  **La console Unreal :** La commande `r.SetRes` reste un outil de débogage et de configuration très puissant pour tester rapidement des résolutions sans passer par les menus de paramètres complexes.

{{< footer >}}
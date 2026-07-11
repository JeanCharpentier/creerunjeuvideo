---
title: "20. Gestion de la mémoire : Détruire les acteurs hors écran"
weight: 20
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprint', 'Optimisation', 'Performance', 'GameDev']
images: ["https://img.youtube.com/vi/lfoHehq7aEA/maxresdefault.jpg"]
---

Dans cet épisode, nous abordons une étape cruciale pour la survie de votre projet : l'optimisation de la mémoire. Lorsqu'on génère des objets en continu (comme des ennemis ou des obstacles), il est impératif de nettoyer ceux qui ne sont plus visibles par le joueur. Si vous ne le faites pas, ces acteurs continueront de consommer des ressources processeur et mémoire, menant inévitablement à une chute de framerate, particulièrement sur mobile.

{{< youtube-rgpd "lfoHehq7aEA" >}}

### Résumé de la mise en place
Pour gérer proprement la disparition de nos "Tromps" (obstacles), nous avons mis en place une zone de nettoyage invisible :

*   **Création d'un acteur dédié :** Nous avons créé un `BP_DestroyTromps` basé sur un `Actor` simple.
*   **Zone de collision :** Ajout d'un composant `Box Collision` à cet acteur pour définir la zone de "suppression".
*   **Logique de détection :** Dans le `BP_Tromps`, nous utilisons l'événement `Event Actor Begin Overlap`.
*   **Vérification de classe :** Grâce au nœud `Get Class` comparé à notre `BP_DestroyTromps`, nous vérifions si l'objet qui entre dans la zone est bien celui que nous voulons détruire.
*   **Destruction :** Utilisation du nœud `Destroy Actor` (avec la cible réglée sur `Self`) pour supprimer l'instance spécifique du tromp qui franchit la limite.
*   **Placement :** Positionnement de la zone de collision derrière la caméra du joueur pour qu'elle soit invisible tout en remplissant son rôle de "poubelle" à objets.

### Ce qui reste d'actualité aujourd'hui

Bien que cet article traite d'Unreal Engine 4, les principes fondamentaux restent identiques dans les versions plus récentes (UE5) :

1.  **Gestion des ressources :** Le "Pooling" ou la destruction systématique des acteurs hors écran est une règle d'or en développement de jeux vidéo.
2.  **Collision vs Trigger :** L'utilisation d'une `Box Collision` configurée en mode "Overlap" est toujours la méthode la plus légère pour déclencher des événements de gameplay sans impacter les calculs physiques complexes.
3.  **Optimisation mobile :** Sur les plateformes mobiles, la gestion de la mémoire vive (RAM) est encore plus stricte. Détruire les acteurs inutiles est la meilleure façon d'éviter les crashs liés à une surcharge mémoire.
4.  **Modularité :** Créer un acteur dédié à la destruction permet de réutiliser ce système partout dans votre niveau sans avoir à réécrire la logique pour chaque type d'ennemi.

{{< footer >}}
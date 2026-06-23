---
title: "13. Maîtriser le Foliage Editor dans Unreal Engine 4"
weight: 13
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Foliage', 'Level Design', 'Optimisation', 'Tutoriel']
---

Dans cet épisode, nous abordons une étape cruciale pour donner vie à vos environnements : l'utilisation du **Foliage Editor** (Éditeur de feuillage). Plutôt que de placer vos arbres et éléments de végétation un par un manuellement — une tâche fastidieuse et chronophage — nous allons apprendre à utiliser les outils de peinture procédurale d'Unreal Engine 4 pour peupler rapidement vos niveaux.

{{< youtube-rgpd "cJfM2Ty2YDU" >}}

### Résumé des points clés
*   **Importation des assets :** Utilisation du *Content Browser* pour filtrer et sélectionner vos modèles 3D (arbres, troncs, etc.).
*   **Configuration du Foliage Editor :** Glisser-déposer les assets dans la zone dédiée pour créer une palette de végétation.
*   **Gestion de la densité :** Ajustement des paramètres de *Paint Density* pour contrôler la fréquence d'apparition de chaque type d'arbre.
*   **Optimisation :** Désactivation des collisions si le gameplay ne nécessite pas d'interaction physique avec la végétation.
*   **Édition fine :** Utilisation de l'outil *Select* pour supprimer ou déplacer manuellement des instances afin de créer des clairières ou des chemins spécifiques.
*   **Workflow de placement :** Peindre directement sur le terrain pour créer des forêts denses tout en gardant la main sur la composition visuelle.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes d'Unreal Engine (UE5) aient introduit le système *PCG (Procedural Content Generation)* et les *Packed Level Actors*, les fondamentaux du **Foliage Editor** restent identiques et essentiels pour :
1.  **Le prototypage rapide :** C'est toujours la méthode la plus efficace pour habiller un niveau en quelques minutes.
2.  **La performance :** Le système de foliage d'Unreal utilise l'instanciation (HISM - Hierarchical Instanced Static Meshes), ce qui est indispensable pour maintenir un framerate élevé avec des milliers d'objets.
3.  **Le contrôle artistique :** La possibilité de peindre manuellement reste irremplaçable pour diriger le regard du joueur ou créer des zones de gameplay spécifiques (clairières, sentiers) sans avoir à générer des règles procédurales complexes.

{{< footer >}}
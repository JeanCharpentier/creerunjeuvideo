---
title: "11. Système de ramassage d''objets par interaction"
weight: 11
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprints', 'Interaction', 'Gameplay', 'Tutoriel']
---

Dans ce nouvel épisode de notre série sur Unreal Engine 4, nous allons passer à l'étape suivante de notre système d'interaction. Après avoir appris à détecter et mettre en surbrillance (Highlight) nos objets, il est temps de leur donner une utilité : le ramassage. Nous allons voir comment déclencher la destruction d'un acteur via une touche clavier tout en conservant une structure de code propre et organisée.

{{< youtube-rgpd "zCFxSKBxUts" >}}

### Résumé de l'implémentation
*   **Organisation du Blueprint :** Utilisation des "Comment Boxes" pour regrouper logiquement les nœuds et améliorer la lisibilité du graphe.
*   **Duplication de logique :** Réutilisation du système de *Line Trace* existant pour détecter l'objet visé lors de l'appui sur une touche.
*   **Input Action :** Configuration de la touche 'E' pour déclencher l'interaction.
*   **Communication entre Blueprints :** Création d'un *Custom Event* dans le Blueprint du cookie pour gérer sa propre destruction (`Destroy Actor`).
*   **Validation :** Utilisation du *Cast* pour s'assurer que l'objet visé est bien un cookie avant d'exécuter la commande de ramassage.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Unreal Engine aient évolué (notamment avec l'arrivée d'UE5), les concepts fondamentaux abordés ici restent des piliers du développement :
1.  **Le Line Trace (Raycasting) :** C'est toujours la méthode standard pour détecter des objets dans le champ de vision du joueur.
2.  **La communication inter-Blueprints :** Le principe de "caster" un objet pour appeler un événement spécifique est une pratique courante et efficace pour des systèmes simples.
3.  **L'organisation du code :** L'utilisation des commentaires et des boîtes de regroupement est une règle d'or pour ne pas se perdre dans des projets complexes.
4.  **Gestion des Inputs :** Bien que l'Enhanced Input System soit désormais la norme, la logique de déclenchement d'un événement via une touche reste identique dans sa structure fonctionnelle.

{{< footer >}}
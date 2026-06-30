---
title: "16. Implémenter un système de sprint dans Unreal Engine 4"
weight: 16
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprints', 'Character Movement', 'Gameplay', 'Tutoriel']
---

Dans ce seizième épisode de notre série dédiée au développement du jeu *Kawaai Slender*, nous allons aborder une mécanique fondamentale pour tout jeu à la première personne : le système de sprint. Apprendre à modifier dynamiquement la vitesse de déplacement de votre personnage est essentiel pour dynamiser votre gameplay.

{{< youtube-rgpd "4HHJm5P_Af0" >}}

### Ce que vous allez apprendre :
*   **Configuration des entrées (Input) :** Comment déclarer une nouvelle action dans les *Project Settings* pour associer la touche "Shift" (Maj) à une commande de sprint.
*   **Accès au Character Movement :** Utiliser le composant *Character Movement* pour manipuler les propriétés physiques de votre personnage via les Blueprints.
*   **Logique de vitesse :** Utiliser le nœud `Set Max Walk Speed` pour alterner entre la vitesse de marche normale et la vitesse de course.
*   **Organisation :** L'importance de commenter et de structurer vos graphes de Blueprints pour maintenir un projet propre.

### Ce qui reste d'actualité aujourd'hui
Bien que cet article se base sur Unreal Engine 4, les principes fondamentaux restent identiques dans les versions plus récentes (UE5) :
*   **Input Mapping :** La gestion des entrées via les *Project Settings* est toujours la base, bien que l'UE5 privilégie désormais le système *Enhanced Input* (plus flexible).
*   **Character Movement Component :** Ce composant reste le cœur de la gestion des déplacements dans Unreal. La fonction `Set Max Walk Speed` est toujours la méthode standard et la plus optimisée pour modifier la vitesse de marche en temps réel.
*   **Modularité :** La logique de "Press" (appuyer) et "Release" (relâcher) pour basculer entre deux états de vitesse est une pratique toujours très utilisée pour les mécaniques de stamina ou de sprint simple.

{{< footer >}}
---
title: "1. Afficher un compteur de FPS dans Unreal Engine 4"
weight: 1
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Unreal Engine 4', 'Optimisation', 'Blueprints', 'Quick Tips', 'Performance']
---

Bienvenue dans ce premier épisode de notre série "Quick Tips" dédiée à Unreal Engine 4. L'objectif de ces tutoriels est de vous fournir des astuces concises et immédiatement applicables pour améliorer votre workflow, le débogage et l'optimisation de vos projets.

Pour commencer, nous allons voir comment afficher un compteur de FPS (images par seconde) directement dans votre jeu. C'est une étape indispensable pour surveiller les performances de votre application en temps réel.

{{< youtube-rgpd "dcQee57BVjw" >}}

### Résumé de la procédure
*   **Configuration de l'Input :** Allez dans `Edit > Project Settings > Input` et ajoutez un nouvel *Action Mapping* nommé "FPSCounter" assigné à la touche de votre choix (ex: Tabulation).
*   **Accès au Blueprint :** Ouvrez le Blueprint de votre personnage (ou tout autre Blueprint gérant vos entrées).
*   **Implémentation :** Appelez l'événement "FPSCounter" créé précédemment.
*   **Commande Console :** Reliez-le au node `Execute Console Command` et saisissez la commande : `stat fps`.
*   **Comportement :** La commande `stat fps` fonctionne nativement comme un interrupteur (toggle), il n'est donc pas nécessaire d'ajouter un node *Flip Flop*.

### Ce qui reste d'actualité aujourd'hui
Bien que cet article traite d'Unreal Engine 4, cette méthode reste parfaitement valide et pertinente pour les versions plus récentes du moteur (UE5) :
*   **Commandes Console :** Le système de commandes console (`stat fps`, `stat unit`, `stat game`) est un standard immuable dans l'écosystème Unreal.
*   **Débogage rapide :** L'utilisation de touches de raccourci pour le profiling reste la méthode la plus efficace pour tester les performances sans avoir à ouvrir des outils de diagnostic complexes.
*   **Indépendance du matériel :** Comme mentionné dans la vidéo, gardez toujours à l'esprit que les FPS dépendent de votre machine. Testez systématiquement sur des configurations cibles variées pour obtenir des données représentatives.

{{< footer >}}
---
title: "4. Création d''un système de Sprint et d''Endurance"
weight: 4
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['FPS', 'Blueprint', 'Gameplay', 'Tutoriel']
images: ["https://img.youtube.com/vi/MfM02swJz8U/maxresdefault.jpg"]
---

Dans ce quatrième épisode de notre série dédiée à la création d'un FPS sous Unreal Engine 4, nous allons implémenter une mécanique essentielle : le **Sprint**. Contrairement à des approches basiques, nous allons ici intégrer une gestion dynamique de l'endurance (stamina) avec une interface utilisateur (HUD) intelligente qui ne s'affiche que lorsque le joueur est en effort.

{{< youtube-rgpd "MfM02swJz8U" >}}

### Résumé des étapes clés
*   **Configuration des Inputs :** Création d'un *Action Mapping* "Course" lié à la touche *Left Shift* dans les *Project Settings*.
*   **Variables d'état :** Mise en place de variables booléennes (`PeutCourir`, `Court`) organisées par catégories pour gérer la logique de déplacement.
*   **Logique de mouvement :** Utilisation du composant *Character Movement* pour basculer entre une vitesse de marche et une vitesse de sprint via des variables éditables.
*   **Gestion de l'endurance :** Création de deux fonctions (`BaisserEndurance` et `MonterEndurance`) appelées via des *Timers* pour une gestion fluide de la jauge.
*   **Interface dynamique (HUD) :** Mise en place d'un *Binding* sur la visibilité de la barre d'endurance pour qu'elle disparaisse automatiquement lorsque le joueur est au repos complet.

### Ce qui reste d'actualité aujourd'hui
Bien que cet article traite d'Unreal Engine 4, les concepts fondamentaux abordés restent parfaitement transposables sur **Unreal Engine 5** :
*   **L'utilisation des Timers :** La méthode `Set Timer by Function Name` reste une excellente pratique pour éviter de surcharger l'Event Tick.
*   **La modularité des Blueprints :** L'usage de variables pour définir les vitesses (`VitesseMax`, `VitesseMin`) est toujours la norme pour faciliter l'équilibrage du gameplay.
*   **L'optimisation du HUD :** La gestion de la visibilité des éléments d'interface via des *Bindings* ou des *Property Bindings* est une technique toujours très utilisée pour épurer l'écran de jeu.
*   **La structure de données :** L'organisation des variables dans des catégories (ici "État") est une habitude de travail indispensable pour maintenir des projets complexes, peu importe la version du moteur.

{{< footer >}}
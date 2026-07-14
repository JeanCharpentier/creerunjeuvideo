---
title: "Créer un effet de Bullet Time (Slow Motion) dans Unreal Engine 4"
date: 2026-06-17
categories: ['Développement']
tags: ['Unreal Engine 4', 'Blueprint', 'Gameplay', 'Tutoriel']
images: ["https://img.youtube.com/vi/-3oHJbaHazY/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/-3oHJbaHazY/maxresdefault.jpg"]
---

Le "Bullet Time", popularisé par des titres cultes comme *Max Payne* ou la saga *Matrix*, est un outil puissant pour dynamiser vos séquences d'action. En ralentissant le temps, vous offrez au joueur une sensation de contrôle accrue et une mise en scène cinématographique immédiate. Dans ce tutoriel, nous allons voir comment implémenter cet effet simplement dans Unreal Engine 4 en utilisant les Blueprints et la commande console `slomo`.

{{< youtube-rgpd "-3oHJbaHazY" >}}

### Résumé de la mise en place
Pour réaliser cet effet, nous suivons une logique simple basée sur les événements d'entrée :

*   **Configuration de l'Input :** Création d'un *Action Mapping* dans les *Project Settings* pour assigner une touche (ex: 'F') à l'action "BulletTime".
*   **Variable de contrôle :** Création d'une variable de type `Float` nommée `GameSpeed` dans votre *Character Blueprint*.
*   **Logique de Blueprint :**
    *   À l'appui sur la touche : On définit `GameSpeed` sur une valeur faible (ex: 0.2 pour un ralentissement, 0 pour un arrêt total).
    *   Au relâchement : On réinitialise `GameSpeed` à 1.0 (vitesse normale).
*   **Exécution :** Utilisation du node `Execute Console Command` avec la commande `slomo` concaténée à la valeur de `GameSpeed`.

### Ce qui reste d'actualité aujourd'hui
Bien que ce tutoriel utilise Unreal Engine 4, les principes fondamentaux restent parfaitement valables pour les versions actuelles (UE5) :

1.  **La commande `slomo` :** Elle reste la méthode la plus rapide et efficace pour manipuler l'échelle de temps globale du moteur (`GlobalTimeDilation`).
2.  **Modularité :** L'utilisation d'une variable `GameSpeed` permet d'évoluer facilement vers des systèmes plus complexes, comme une jauge d'endurance qui se vide pendant l'utilisation du ralenti.
3.  **Flexibilité :** Cette méthode permet non seulement de ralentir le temps, mais aussi de l'accélérer (en mettant une valeur supérieure à 1) ou de le figer totalement, offrant une grande liberté créative pour vos mécaniques de jeu.
4.  **Performance :** Cette approche est extrêmement légère en termes de ressources, car elle s'appuie sur une fonctionnalité native du moteur plutôt que sur des calculs complexes par objet.

{{< footer >}}
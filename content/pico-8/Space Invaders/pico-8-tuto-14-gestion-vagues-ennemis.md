---
title: "14. Gestion des vagues et types d''ennemis"
weight: 14
date: 2023-10-27
categories: ['Pico-8']
tags: ['tutoriel', 'gamedev', 'space-invaders', 'lua']
images: ["https://img.youtube.com/vi/xPdKfs4jkSw/maxresdefault.jpg"]
---

Dans ce nouvel épisode de notre série dédiée à la création d'un *Space Invader* sur Pico-8, nous allons passer à la vitesse supérieure. Fini le placement statique des ennemis : nous allons mettre en place un système de **vagues** modulable. L'objectif est de pouvoir définir des patterns d'ennemis variés, mélanger les types de vaisseaux (bleus, rouges, etc.) et gérer leurs comportements spécifiques, comme la capacité de tir.

{{< youtube-rgpd "xPdKfs4jkSw" >}}

### Résumé de l'épisode
*   **Édition des sprites :** Création d'un second type d'ennemi (vaisseau rouge) via un simple *color swap* pour diversifier le visuel.
*   **Structure de données :** Utilisation de tableaux (matrices) pour définir les vagues. Chaque chiffre dans le tableau correspond à un type d'ennemi (0 pour vide, 1 pour bleu, 2 pour rouge).
*   **Logique de boucle :** Remplacement de la création manuelle par une boucle `for` qui parcourt le tableau de la vague et positionne les ennemis dynamiquement en fonction de leur index (modulo 6 pour le retour à la ligne).
*   **Comportement différencié :** Ajout d'une propriété `s` (shoot) dans les objets ennemis pour déterminer si un vaisseau est autorisé à tirer ou non.
*   **Optimisation du code :** Mise à jour du gestionnaire de tir pour vérifier cette propriété avant de déclencher une attaque.

### Ce qui reste d'actualité aujourd'hui
*   **L'approche modulaire :** Utiliser des tableaux de données pour définir des niveaux ou des vagues est une pratique standard en GameDev. Cela permet de modifier le gameplay sans toucher au moteur de rendu.
*   **Le "Data-Driven Design" :** En séparant la logique (le code de déplacement) des données (la configuration de la vague), vous rendez votre jeu beaucoup plus facile à maintenir et à étendre.
*   **Gestion des états :** L'utilisation de propriétés booléennes (comme `s` pour le tir) est la base pour créer des ennemis avec des comportements variés (ennemis qui foncent, ennemis qui tirent, ennemis qui restent immobiles).
*   **Pico-8 et Lua :** La manipulation des tableaux et des boucles `for` reste le cœur battant de tout projet sur cette console virtuelle. Maîtriser ces structures est indispensable pour progresser.

{{< footer >}}
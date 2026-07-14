---
title: "23. Maîtriser le système de Crafting"
weight: 23
prev_url: "/intersect-engine/creer-un-mmorpg/guide-migration-intersect-engine-beta-1/"
next_url: "/intersect-engine/creer-un-mmorpg/maitriser-systeme-quetes-intersect-engine/"
date: 2023-10-27
categories: ['Archive']
tags: ['Intersect Engine', 'Game Development', 'MMO', 'Tutoriel']
images: ["https://img.youtube.com/vi/z45ZPNIw-F0/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/z45ZPNIw-F0/maxresdefault.jpg"]
---

Le système de craft est un pilier fondamental pour l'immersion et l'économie de tout MMO. Avec Intersect Engine, les développeurs disposent d'un outil puissant pour créer des ateliers spécialisés et structurer la progression de leurs joueurs.

{{< youtube-rgpd "z45ZPNIw-F0" >}}

### Résumé des notions clés

Le système de craft d'Intersect Engine repose sur une logique d'ateliers (ou *Crafting Benches*) plutôt que sur un craft portable universel. Voici les étapes essentielles pour le mettre en place :

*   **Le Crafting Bench Editor :** C'est ici que vous définissez vos ateliers. Chaque atelier peut être spécialisé (ex: forge pour le métal, établi d'ébéniste pour le bois) afin de segmenter les recettes par zone ou par type de métier.
*   **Configuration des recettes :**
    *   **Sélection de l'item :** Choisissez l'objet final à produire parmi votre base de données d'items.
    *   **Temps de fabrication :** Définissez une durée réaliste pour le craft (en millisecondes).
    *   **Ingrédients :** Ajoutez les ressources nécessaires. Vous pouvez exiger plusieurs types d'objets et des quantités variables pour complexifier la création.
*   **Intégration dans le monde :**
    *   Utilisez l'éditeur de carte pour placer un événement (PNJ ou objet décoratif comme un coffre/enclume).
    *   Assignez la commande `OpenCrafting Station` à cet événement en sélectionnant l'atelier correspondant.
*   **Expérience joueur :** Une fois en jeu, le joueur interagit avec l'objet, ce qui ouvre une interface dédiée listant les recettes disponibles et permettant de lancer la production instantanément si les ingrédients sont présents dans l'inventaire.

### Ce qui reste d'actualité aujourd'hui

Bien que l'interface d'Intersect Engine ait pu évoluer au fil des mises à jour, la logique fondamentale décrite ici reste le standard pour ce moteur :

1.  **La spécialisation géographique :** Le fait de forcer les joueurs à se déplacer vers des lieux spécifiques (forges, scieries) reste une excellente pratique de *game design* pour encourager l'exploration et créer des points de rencontre sociaux.
2.  **L'économie de jeu :** Le système de craft est le moteur principal de l'économie. En contrôlant les ingrédients nécessaires, vous pouvez réguler la rareté des objets et favoriser le commerce entre joueurs (les "artisans" vs les "récolteurs").
3.  **Modularité :** La possibilité d'ajouter autant d'ingrédients que souhaité permet de créer des systèmes de craft complexes, incluant des objets de haut niveau nécessitant des matériaux rares, ce qui prolonge considérablement la durée de vie de votre MMO.

{{< footer >}}
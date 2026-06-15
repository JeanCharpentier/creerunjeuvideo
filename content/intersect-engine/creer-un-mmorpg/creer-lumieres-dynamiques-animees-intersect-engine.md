---
title: "17. Créer des lumières dynamiques et animées"
weight: 17
prev_url: "/intersect-engine/creer-un-mmorpg/mise-en-place-cycle-jour-nuit-intersect-engine/"
next_url: "/intersect-engine/creer-un-mmorpg/creer-sort-soin-intersect-engine/"
date: 2023-10-27
categories: ['Archive']
tags: ['Intersect Engine', 'Game Development', 'Tutoriel', 'MMORPG', 'Level Design']
---

Donner vie à votre monde est essentiel pour l'immersion, surtout lors de la mise en place d'un cycle jour/nuit. Dans ce tutoriel, nous allons apprendre à intégrer des torches animées et des sources de lumière dynamiques pour illuminer vos villages.

{{< youtube-rgpd "-bQqu1j0Zhg" >}}

### Résumé des notions clés

Pour réussir l'intégration de vos effets de lumière, voici les étapes à suivre dans l'éditeur :

*   **Création de l'animation :**
    *   Rendez-vous dans le *Content Editor* pour créer une nouvelle animation.
    *   **Gestion des calques :** Choisissez entre *Upper* (au-dessus du joueur) ou *Lower* (en dessous) selon le placement de votre objet.
    *   **Configuration des frames :** Vérifiez le nombre d'images dans votre fichier source (dossier `resources/animations`). Ajustez les valeurs *Horizontal/Vertical Frames* pour que l'animation soit fluide.
    *   **Réglages temporels :** Utilisez le *Frame Duration* pour définir la vitesse de l'animation (100ms est une bonne base).
*   **Intégration des lumières sur la carte :**
    *   Utilisez l'onglet *Lights* dans l'éditeur de carte.
    *   **Paramétrage :** Définissez la couleur, l'intensité (0 à 255) et la taille (rayon) de la lumière.
    *   **Ajustements :** Utilisez les *Offsets* (X et Y) pour aligner précisément la source lumineuse avec l'objet graphique de la torche.
*   **Placement :**
    *   Utilisez l'onglet *Attributes* pour poser l'animation créée précédemment sur les cases de votre carte.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions d'Intersect Engine évoluent, les principes fondamentaux de ce tutoriel demeurent des piliers du level design sur ce moteur :

1.  **Le découpage des animations :** La logique de lecture des spritesheets (horizontal/vertical frames) est une constante dans le développement 2D. Comprendre comment Intersect découpe une image pour créer un mouvement est une compétence transférable à tous vos futurs assets.
2.  **L'optimisation des lumières :** La gestion des lumières via l'onglet *Lights* reste la méthode la plus performante pour créer des ambiances sans surcharger le moteur. La distinction entre les lumières statiques (map) et dynamiques (objets/projectiles) est toujours d'actualité pour maintenir un bon framerate.
3.  **L'importance du "Layering" :** La gestion des calques (*Upper/Lower*) est cruciale pour éviter les problèmes de profondeur visuelle, un point qui reste central pour assurer la lisibilité de votre MMORPG.

{{< footer >}}
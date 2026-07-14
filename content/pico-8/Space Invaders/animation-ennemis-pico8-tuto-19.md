---
title: "19. Animation des ennemis sur PICO-8"
weight: 19
date: 2024-05-22
categories: ['PICO-8']
tags: ['gamedev', 'tutoriel', 'animation', 'lua']
images: ["https://img.youtube.com/vi/_a-vMfM3B44/maxresdefault.jpg"]
---

Dans ce 19ème épisode de notre série dédiée à la création d'un *Space Invaders-like* sur PICO-8, nous abordons une étape cruciale pour donner vie à vos ennemis : l'animation. Bien que nous nous concentrions sur une boucle simple de deux frames, les concepts abordés ici sont transposables à n'importe quel système d'animation plus complexe.

{{< youtube-rgpd "_a-vMfM3B44" >}}

### Résumé de l'épisode
*   **Préparation des sprites :** Organisation des feuilles de sprites pour regrouper les états d'animation (ex: 16-17 pour le vaisseau bleu, 18-19 pour le rouge).
*   **Structure de données :** Ajout d'une table `anim` dans la définition de chaque type d'ennemi pour stocker les IDs des sprites correspondants.
*   **Gestion du temps :** Utilisation d'un `anim_time` et d'un `anim_rate` pour cadencer le changement d'image indépendamment de la vitesse de la boucle principale.
*   **Fonction utilitaire `flipflop` :** Création d'une fonction réutilisable permettant de basculer facilement entre deux valeurs (A et B), idéale pour alterner entre deux frames d'animation.
*   **Intégration :** Mise à jour de la fonction `create_enemy` pour initialiser correctement la propriété d'animation lors de l'instanciation.

### Ce qui reste d'actualité aujourd'hui
*   **Modularité :** La création de fonctions utilitaires comme `flipflop` est une excellente pratique. Elle permet d'alléger le code principal et de rendre vos outils réutilisables pour d'autres éléments du jeu (clignotement d'un menu, changement d'état d'un objet, etc.).
*   **Organisation des assets :** Anticiper l'espace dans votre *Sprite Editor* est essentiel. Laisser des cases vides permet d'ajouter des frames d'animation ou de nouveaux ennemis sans avoir à réorganiser toute votre feuille de sprites et à corriger les IDs dans le code.
*   **Découplage :** Gérer la vitesse d'animation via un `rate` plutôt que de se baser sur le `frame rate` brut du jeu garantit une animation fluide et cohérente, quel que soit le matériel ou les ralentissements potentiels.

{{< footer >}}
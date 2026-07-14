---
title: "Créer un mini-jeu de type ''Doodle Jump'' avec GDevelop 5"
date: 2026-06-17
categories: ['Tutoriels']
tags: ['GDevelop', 'Jeu Vidéo', 'Plateforme', 'Développement']
images: ["https://img.youtube.com/vi/4NYoKyn1R6g/maxresdefault.jpg"]
---

Dans cet article, nous allons explorer les bases pour créer un jeu de type "Doodle Jump" (saut infini vertical) en utilisant GDevelop 5. Ce projet est idéal pour comprendre la gestion des caméras, les collisions dynamiques et la génération procédurale d'objets.

{{< youtube-rgpd "4NYoKyn1R6g" >}}

### Résumé des étapes clés
*   **Configuration de la scène :** Utilisation d'une vue verticale (format mobile) et renommage de la scène principale.
*   **Comportements (Behaviors) :** 
    *   *Platformer Character* pour le joueur avec une vitesse de saut ajustée.
    *   *Screen Wrap* pour permettre au joueur de passer d'un côté à l'autre de l'écran.
    *   *Jump-thru platform* pour permettre au joueur de traverser les plateformes par le bas.
*   **Gestion de la caméra :** Utilisation d'une interpolation linéaire (LERP) pour que la caméra suive le joueur vers le haut de manière fluide.
*   **Génération procédurale :** Création d'une "Dead Zone" invisible qui suit le joueur et déclenche la suppression/création de nouvelles plateformes au fur et à mesure de l'ascension.
*   **Système de bonus :** Ajout de "boosts" (champignons) qui modifient temporairement la vitesse de saut du joueur via des variables de scène.

### Ce qui reste d'actualité aujourd'hui
Bien que GDevelop ait évolué depuis la réalisation de cette vidéo, les concepts fondamentaux présentés restent parfaitement valides :
1.  **La logique de la "Dead Zone" :** C'est toujours la méthode la plus efficace pour gérer le nettoyage de mémoire (suppression des objets hors champ) et la génération infinie.
2.  **L'interpolation (LERP) :** La fonction `lerp()` reste l'outil standard pour créer des mouvements de caméra "smooth" (fluides) sans saccades.
3.  **Les variables de scène :** L'utilisation de variables pour stocker les positions de génération est une bonne pratique pour garder un code propre et éviter les conflits entre instances d'objets.
4.  **La modularité :** La séparation entre la logique de saut, la gestion de la caméra et le système de score (à ajouter séparément) permet de construire un projet robuste et facile à maintenir.

{{< footer >}}
---
title: "3. Gérer le score et l''interface utilisateur dans GDevelop 5"
weight: 3
date: 2023-10-27
categories: ['Tutoriels GDevelop']
tags: ['GDevelop', '3D', 'Développement de jeu', 'Interface', 'Variables']
images: ["https://img.youtube.com/vi/FAWah1ve3rA/maxresdefault.jpg"]
---

Bienvenue dans ce troisième volet de notre série dédiée à la création d'un jeu 3D avec GDevelop 5. Après avoir mis en place les déplacements et la collecte d'objets, il est temps de donner un but à votre joueur en implémentant un système de score. Nous aborderons la gestion des variables, la création d'une interface utilisateur (UI) et l'utilisation des calques pour afficher vos informations par-dessus votre monde 3D.

{{< youtube-rgpd "FAWah1ve3rA" >}}

### Au programme de cet épisode :
*   **Comprendre les variables :** Différence entre variables globales, de scène et d'objet.
*   **Création de variables globales :** Stocker le score pour qu'il soit accessible partout dans le jeu.
*   **Système de calques :** Créer un calque dédié à l'interface (2D) pour qu'il reste fixe au-dessus de la scène 3D.
*   **Affichage du texte :** Utiliser un objet Texte pour visualiser le score.
*   **Ancrage (Anchors) :** Assurer que votre interface reste bien positionnée, peu importe la résolution de l'écran.
*   **Programmation événementielle :** Utiliser la fonction `ToString()` pour convertir vos nombres en texte et mettre à jour l'affichage dynamiquement.
*   **Le Debugger :** Apprendre à inspecter l'état de vos variables en temps réel pour corriger vos bugs.

### Ce qui reste d'actualité aujourd'hui

*   **Optimisation des événements :** Ne mettez pas à jour votre texte à chaque "frame" (image par seconde). Appelez l'action de mise à jour uniquement au moment où la variable change (lorsque vous ramassez une pièce). Cela économise les ressources de calcul.
*   **Le comportement "Ancre" :** C'est devenu l'outil standard pour gérer le responsive design. Il est indispensable pour que vos éléments d'interface (barres de vie, scores) ne se retrouvent pas décalés sur des écrans aux ratios différents.
*   **La conversion de type :** N'oubliez jamais que GDevelop distingue les nombres des chaînes de caractères. La fonction `ToString()` reste la méthode incontournable pour afficher une valeur numérique dans un objet texte.
*   **Organisation des calques :** Garder vos éléments d'interface sur un calque séparé du monde 3D est une bonne pratique de Game Design qui facilite grandement la gestion de la caméra et du rendu.

{{< footer >}}
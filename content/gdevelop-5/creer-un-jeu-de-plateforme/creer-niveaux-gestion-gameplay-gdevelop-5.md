---
title: "4. Créer des niveaux et gérer le gameplay global dans GDevelop 5"
weight: 4
date: 2024-05-23
categories: ['Tutoriels GDevelop']
tags: ['GDevelop 5', 'GameDev', 'Débutant', 'Niveaux', 'External Events']
images: ["https://img.youtube.com/vi/lE0Z5ih3_ik/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/lE0Z5ih3_ik/maxresdefault.jpg"]
---

Bienvenue dans ce quatrième épisode de notre série dédiée à la création d'un jeu de plateforme 2D sur GDevelop 5 ! Aujourd'hui, nous allons franchir une étape cruciale pour la structure de votre projet : comment passer d'un niveau à un autre et, surtout, comment organiser votre code pour ne pas avoir à réécrire les mêmes règles de gameplay à chaque nouvelle scène.

{{< youtube-rgpd "lE0Z5ih3_ik" >}}

### Résumé du tutoriel
Dans cette vidéo, nous abordons deux points fondamentaux pour la scalabilité de votre jeu :

*   **La modularité avec les "External Events" (Feuilles d'événements externes) :** Au lieu de copier-coller vos événements de gameplay dans chaque scène, nous créons une feuille unique. Cela permet de modifier une règle (comme le score ou les collisions) une seule fois pour que l'ensemble du jeu soit mis à jour instantanément.
*   **La gestion des niveaux :** Nous apprenons à renommer nos scènes selon une convention logique (ex: `Niveau_1`, `Niveau_2`) et à utiliser l'action "Changer de scène" pour créer une progression fluide.
*   **Les objets globaux :** Nous découvrons comment transformer un objet (comme notre drapeau de fin de niveau) en "Objet Global" pour qu'il soit accessible et fonctionnel dans tous les niveaux sans avoir à le recréer.

### Ce qui reste d'actualité aujourd'hui
Bien que GDevelop évolue régulièrement, les concepts présentés ici restent les piliers d'un développement propre :

1.  **La séparation des préoccupations :** Utiliser des feuilles d'événements externes est toujours la meilleure pratique pour éviter la dette technique. Cela rend votre projet beaucoup plus facile à maintenir sur le long terme.
2.  **La convention de nommage :** Garder une structure cohérente pour vos scènes (Niveau_1, Niveau_2...) est indispensable si vous souhaitez automatiser plus tard le chargement des niveaux via des variables.
3.  **La réflexion sur les objets globaux :** Il est toujours crucial de ne transformer en "Global" que ce qui est strictement nécessaire. Garder vos objets locaux quand c'est possible permet d'optimiser la gestion de la mémoire et de garder votre liste d'objets propre.
4.  **La gestion des collisions :** La méthode de détection de collision avec un objet de fin de niveau reste la base absolue pour déclencher des transitions de scène.

{{< footer >}}
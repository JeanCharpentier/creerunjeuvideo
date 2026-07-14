---
title: "5. Créer un système d''expérience et de montée de niveau"
weight: 5
date: 2023-10-27
categories: ['Tutoriels GDevelop']
tags: ['GDevelop 5', 'Survival', 'GameDev', 'Variables', 'UI']
images: ["https://img.youtube.com/vi/DtqWmMlafnM/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/DtqWmMlafnM/maxresdefault.jpg"]
---

Dans ce cinquième épisode de notre série dédiée à la création d'un jeu de type *Survivor* sur GDevelop 5, nous allons nous concentrer sur la progression du joueur. Vous apprendrez à mettre en place un système d'expérience, à créer une barre de progression dynamique et à automatiser l'attraction des objets vers le personnage.

{{< youtube-rgpd "DtqWmMlafnM" >}}

### Ce que vous allez apprendre dans ce tutoriel :
*   **Gestion des variables :** Créer et manipuler les variables d'objet pour suivre l'expérience actuelle et le seuil du prochain niveau.
*   **Interface utilisateur (UI) :** Utiliser l'objet "Barre de ressources" pour afficher visuellement la progression du joueur.
*   **Attraction d'objets :** Programmer un système où les flasques d'expérience sont attirées automatiquement vers le joueur lorsqu'il s'en approche.
*   **Logique de montée de niveau :** Créer un système de calcul automatique pour augmenter la difficulté (le seuil d'XP nécessaire) à chaque niveau franchi.
*   **Optimisation :** Utiliser les groupes d'objets pour simplifier la gestion des collisions et des apparitions d'objets.

### Ce qui reste d'actualité aujourd'hui
*   **La gestion des variables :** La manipulation des variables d'objet reste le cœur du système de progression dans GDevelop.
*   **L'utilisation des groupes :** Regrouper vos objets (ennemis, flasques) est toujours la meilleure pratique pour garder un code propre et évolutif.
*   **La soustraction de l'XP :** La technique consistant à soustraire l'XP du niveau précédent lors du passage au niveau supérieur est indispensable pour ne pas "voler" de points au joueur.
*   **Les barres de ressources :** L'objet natif "Barre de ressources" est toujours l'outil le plus simple et efficace pour afficher des jauges de vie ou d'expérience.

{{< footer >}}
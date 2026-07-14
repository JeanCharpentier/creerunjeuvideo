---
title: "6. Créer un système d'upgrades (Level Up) - Partie 1"
weight: 6
date: 2024-05-22
categories: ['Tutoriels']
tags: ['GDevelop 5', 'Survival-like', 'Game Design', 'Variables']
images: ["https://img.youtube.com/vi/AL5Qg1EyutU/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/AL5Qg1EyutU/maxresdefault.jpg"]
---

Dans cet épisode de notre série dédiée à la création d'un *Survival-like* avec GDevelop 5, nous attaquons une étape cruciale : le système de montée de niveau. Comme le sujet est dense, nous allons le diviser en deux parties. Aujourd'hui, nous nous concentrons sur l'affichage dynamique des choix d'améliorations.

{{< youtube-rgpd "AL5Qg1EyutU" >}}

### Ce que nous allons mettre en place :
*   **Gestion des scènes :** Renommage et organisation de la scène principale.
*   **Interface de menu :** Création d'un calque dédié au menu "Level Up" pour le masquer/afficher à la volée.
*   **Data-driven design :** Utilisation d'une variable globale de type "Tableau" pour stocker toutes les statistiques modifiables (vitesse, dégâts, vie, etc.).
*   **Logique de tirage au sort :** Utilisation de `RandomInRange` pour proposer deux améliorations aléatoires parmi la liste, tout en évitant les doublons grâce à une boucle `Tant que`.
*   **Mise à jour dynamique :** Programmation des boutons pour qu'ils affichent le nom de l'amélioration piochée dans le tableau.

### Ce qui reste d'actualité aujourd'hui
*   **Structure des données :** L'utilisation de structures dans les variables (Tableaux de structures) reste la meilleure pratique pour gérer des objets complexes comme des compétences ou des items.
*   **Modularité :** Le système de "Data-driven" présenté ici permet d'ajouter de nouvelles compétences en modifiant simplement la variable globale, sans avoir à toucher au code des événements.
*   **Bonnes pratiques :** L'utilisation de calques séparés pour l'interface (UI) est indispensable pour garder un projet propre et performant.
*   **Exercice pratique :** N'oubliez pas que l'affichage de la description (le texte explicatif sous le nom de la compétence) est un excellent exercice pour consolider vos acquis sur la manipulation des variables de structure.

{{< footer >}}
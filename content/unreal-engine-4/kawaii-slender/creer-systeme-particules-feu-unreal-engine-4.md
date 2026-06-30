---
title: "25. Créer un système de particules simple pour un feu"
weight: 25
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Tutoriel', 'Particules', 'Niagara', 'Cascade', 'GameDev']
---

Dans cet épisode, nous abordons les bases du système de particules dans Unreal Engine 4. Bien que les outils aient évolué avec l'arrivée de Niagara, comprendre la logique derrière le système classique (Cascade) reste une excellente porte d'entrée pour maîtriser les effets visuels dans vos projets. Nous allons créer un effet de feu stylisé, idéal pour un rendu "low-poly".

{{< youtube-rgpd "ZK9ZNjDOZwU" >}}

### Résumé du tutoriel
*   **Création du matériel :** Configuration d'un matériel en mode *Translucent* et *Unlit* pour gérer la transparence et l'absence de calcul d'éclairage complexe.
*   **Utilisation du Radial Gradient Exponential :** Création d'une forme circulaire dégradée pour simuler la base de la flamme.
*   **Node Particle Color :** Intégration de ce node pour permettre au système de particules de piloter dynamiquement la couleur et l'opacité.
*   **Configuration du Particle System (Cascade) :**
    *   **Required :** Assignation du matériel créé.
    *   **Initial Size :** Réglage de la taille aléatoire des particules.
    *   **Initial Location :** Définition d'une zone d'apparition pour éviter que toutes les particules ne naissent au même point.
    *   **Color Over Life :** Utilisation d'une courbe pour faire varier la couleur de la flamme (du jaune au rouge/rose) au cours de sa durée de vie.

### Ce qui reste d'actualité aujourd'hui
Bien que le système **Cascade** (utilisé dans ce tutoriel) soit progressivement remplacé par **Niagara** dans les versions récentes d'Unreal Engine, les principes fondamentaux restent identiques :
1.  **La logique des matériaux :** La gestion des modes *Translucent* et *Unlit* est toujours la norme pour les effets de particules performants.
2.  **Le workflow de données :** La séparation entre le matériel (l'apparence) et le système de particules (le comportement) est une règle d'or en GameDev.
3.  **L'optimisation :** L'utilisation de formes simples et de dégradés mathématiques (comme le *Radial Gradient*) est toujours la méthode la plus efficace pour garder un jeu fluide, surtout sur des styles graphiques low-poly.
4.  **La courbe de vie :** Le concept de "Color Over Life" ou "Size Over Life" est le cœur battant de tout système de particules, qu'il soit ancien ou moderne.

{{< footer >}}
---
title: "9. Création d''un système d''armes rotatives (Orbitales)"
weight: 9
date: 2024-05-22
categories: ['Tutoriels GDevelop']
tags: ['GDevelop 5', 'GameDev', 'Survival-like', 'Tutoriel']
images: ["https://img.youtube.com/vi/JxOhXjIb7UU/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/JxOhXjIb7UU/maxresdefault.jpg"]
---

Dans cet épisode de notre série dédiée à la création d'un *survival-like* avec GDevelop 5, nous allons ajouter une mécanique très populaire dans ce genre de jeu : les armes orbitales. Ces armes tournent autour du joueur et infligent des dégâts continus aux ennemis sans disparaître au contact.

{{< youtube-rgpd "JxOhXjIb7UU" >}}

### Ce que nous avons appris dans cet épisode :

*   **Gestion des données :** Utilisation des variables globales et des tableaux pour structurer les améliorations (upgrades) de manière flexible.
*   **Extension "Orbital" :** Installation et utilisation de l'extension communautaire pour faire orbiter des objets autour d'un point central sans calculs trigonométriques complexes.
*   **Système de projectiles :** Distinction entre les projectiles "destructibles" (comme les couteaux) et les armes orbitales (qui restent actives après un impact) via une variable booléenne.
*   **Logique d'amélioration :** Mise en place d'un système où, une fois le nombre maximal d'armes atteint, les améliorations suivantes augmentent automatiquement les dégâts des armes existantes.
*   **Optimisation du code :** Utilisation de la condition "Sinon" pour gérer efficacement les deux états de l'arme (ajout d'une nouvelle masse ou amélioration des dégâts).

### Ce qui reste d'actualité aujourd'hui

*   **La modularité des variables :** La méthode consistant à utiliser des variables pour définir le comportement des objets (dégâts, destructibilité) reste la meilleure pratique pour garder un projet propre et évolutif.
*   **L'utilisation des extensions :** GDevelop propose de nombreuses extensions communautaires qui simplifient grandement des tâches mathématiques lourdes. N'hésitez pas à explorer le catalogue pour vos futurs projets.
*   **La structure des groupes :** Regrouper vos objets (comme le groupe "Projectiles") permet d'appliquer des changements globaux en une seule action, ce qui est indispensable pour la maintenance d'un jeu qui s'agrandit.
*   **Le système d'upgrades :** La logique de "plafond" (ex: 3 masses max, puis augmentation des dégâts) est un excellent moyen de gérer la progression du joueur sans avoir à créer une infinité d'objets différents.

{{< footer >}}
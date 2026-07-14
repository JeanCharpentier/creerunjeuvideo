---
title: "2. Créer des objets interactifs et animés en 3D"
weight: 2
date: 2023-10-27
categories: ['GDevelop 5']
tags: ['3D', 'Tutoriel', 'Débutant', 'GameDev']
images: ["https://img.youtube.com/vi/n2k2yuj_l-g/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/n2k2yuj_l-g/maxresdefault.jpg"]
---

Bienvenue dans ce deuxième volet de notre série dédiée à la création d'un jeu de plateforme 3D sur GDevelop 5. Après avoir mis en place les bases de notre environnement, il est temps de donner vie à notre niveau en ajoutant des éléments interactifs : les pièces à ramasser.

{{< youtube-rgpd "n2k2yuj_l-g" >}}

Dans cet épisode, nous allons apprendre à manipuler les instances d'objets, à créer des animations simples par le code et à gérer les collisions pour supprimer des objets de la scène.

### Ce que nous avons appris dans cet épisode :

*   **Organisation du projet :** Renommer ses scènes pour une meilleure gestion (via le menu burger ou F2).
*   **Animation procédurale :** Utiliser l'action "Tourner autour de l'axe Z" pour donner du dynamisme à vos objets sans passer par des animations complexes.
*   **Gestion des instances :** Comprendre que modifier un objet dans la liste de scène impacte toutes ses occurrences dans le niveau.
*   **Système de collision simple :** Utiliser la détection de collision standard de GDevelop pour déclencher des événements (ici, la suppression de l'objet) sans avoir recours au moteur physique 3D, ce qui optimise les performances.

### Ce qui reste d'actualité aujourd'hui

*   **L'optimisation avant tout :** Comme souligné dans la vidéo, ne pas activer le moteur physique 3D si ce n'est pas nécessaire est une règle d'or pour garder un jeu fluide, surtout sur mobile ou navigateur.
*   **La puissance de GDevelop :** Le moteur gère nativement l'identification des instances. Lorsque vous demandez de supprimer une pièce lors d'une collision, GDevelop sait exactement laquelle supprimer sans que vous ayez besoin de créer des variables complexes pour chaque pièce.
*   **Le "Game Feel" :** Ajouter de simples rotations ou des mouvements flottants à vos objets de collection transforme radicalement le ressenti du joueur. Un jeu statique paraît toujours moins professionnel qu'un jeu où les éléments "vivent".

{{< footer >}}
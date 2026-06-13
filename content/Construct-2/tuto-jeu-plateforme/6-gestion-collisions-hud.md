---
title: "6. Gestion des collisions, HUD et interface"
date: 2026-06-13
weight: 7
categories: ["Archive"]
tags: ["Construct 2", "Game Dev", "Tutoriel", "HUD", "Collisions"]
prev_url: "/construct-2/tuto-jeu-plateforme/5-creation-ennemi-dynamique"
next_url: "/construct-2/tuto-jeu-plateforme/correctif-animation-atterrissage"
---

> **Note :** Cet article est une archive pédagogique du sixième épisode de ma série sur la création d'un jeu de plateforme avec Construct 2.

{{< youtube-rgpd "rpz05UibsW4" >}}

### Programme de l'épisode

* **Gestion avancée des collisions :** Distinguer l'interaction "saut sur l'ennemi" (destruction) de l'interaction "contact latéral" (perte de vie/redémarrage).
* **Interface (HUD) :** Création d'une interface fixe pour afficher la vie (cœurs) et le score.
* **Optimisation UI :** Utilisation du comportement *Anchor* pour maintenir l'interface à l'écran pendant le défilement.
* **Ajout d'objets :** Intégration de pièces à collecter.

### Logique des collisions (Feuille d'événement)

Pour gérer la différence entre écraser un ennemi et se faire toucher, on utilise des **sous-événements** basés sur l'état vertical du joueur :

1. **Événement principal :** `Player` -> `On collision with another object` -> `Ennemi`.
2. **Sous-événement 1 (Destruction) :** `Player` -> `Platform Is Falling`.
    * Action : `Ennemi` -> `Destroy`.
3. **Sous-événement 2 (Mort/Reset) :** `Player` -> `Platform Is Falling` (Inversé).
    * Action : `System` -> `Restart layout`.

### Configuration de l'interface (HUD)

* **Calque dédié :** Création d'un calque nommé `HUD` pour séparer l'interface des éléments de jeu.
* **Comportement Anchor :** Pour éviter que les éléments de l'interface ne disparaissent lors du déplacement de la caméra, ajoutez le comportement **Anchor** à chaque objet (barre de vie, texte de score). Cela verrouille les éléments par rapport aux bords de la fenêtre de jeu.
* **Taille :** Ajustement manuel des *Tiled Backgrounds* et des objets texte pour assurer une présentation cohérente et alignée.

### Exercice pour la suite
* Préparez vos éléments de score et vos icônes de pièces.
* Assurez-vous que votre calque HUD est bien isolé et que les ancrages sont correctement configurés sur les quatre coins ou bords de l'écran.

{{< footer >}}
---
title: "Correctif: Résoudre les problèmes de collision de plateformes"
date: 2026-06-13
weight: 5
categories: ["Archive"]
tags: ["Construct 2", "Game Dev", "Tutoriel", "Debug", "Collision"]
prev_url: "/construct-2/tuto-jeu-plateforme/4-gestion-niveaux-variables-pieges"
next_url: "/construct-2/tuto-jeu-plateforme/5-creation-ennemi-dynamique"
images: ["https://img.youtube.com/vi/oTqFDMUasfY/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/oTqFDMUasfY/maxresdefault.jpg"]
---

> **Note :** Cet article est une archive technique traitant d'une solution spécifique aux problèmes de collision irrégulière dans Construct 2.

{{< youtube-rgpd "oTqFDMUasfY" >}}

### Le problème : Plateformes et formes complexes
Dans Construct 2, la gestion des collisions sur des plateformes possédant des trous, des pentes ou des arrondis peut provoquer des erreurs de calcul. Le moteur a parfois du mal à gérer physiquement le personnage sur ces surfaces, entraînant des traversées accidentelles ou des bugs de positionnement.

### La solution : Utiliser un contrôleur de collision transparent

Au lieu de compter sur la forme visuelle complexe de vos plateformes, la technique consiste à créer une couche invisible dédiée à la physique.

* **Étape 1 : Visualisation**
  Allez dans l'onglet *View* en haut à gauche et cochez *Show collision polygons*. Cela vous permet de voir les zones réelles où le moteur calcule la collision.

* **Étape 2 : Nettoyage des objets**
  Supprimez le comportement *Jump-through* de vos objets de décor visuel (plateformes, coins, etc.). Ces objets ne doivent plus gérer la collision eux-mêmes.

* **Étape 3 : Création du contrôleur**
  * Créez un nouveau Sprite transparent nommé `call platform`.
  * Définissez son point d'origine à 0,0.
  * Appliquez le comportement *Jump-through* à cet objet.

* **Étape 4 : Implémentation**
  Placez cet objet `call platform` par-dessus vos plateformes visuelles. Dupliquez-le pour couvrir toute la surface de jeu où le personnage doit pouvoir marcher.

### Conclusion sur les concessions techniques
Cette méthode supprime radicalement les bugs de traversée. Il est important de noter qu'il s'agit d'une concession : le personnage peut sembler flotter de quelques pixels sur les bords arrondis. C'est toutefois une solution très robuste pour garantir un gameplay fluide, indépendamment de la puissance de calcul du navigateur du joueur.

N'oubliez pas de décocher *Show collision polygons* une fois le travail terminé pour retrouver un affichage propre.

{{< footer >}}
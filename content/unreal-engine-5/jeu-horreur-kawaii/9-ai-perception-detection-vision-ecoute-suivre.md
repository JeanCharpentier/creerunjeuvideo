---
title: "9. Perception sensorielle de l'IA (AI Perception) et activation du Slender"
date: 2026-06-12
category: Archive
weight: 9
tags: [Unreal Engine 5, Kawaii Slender, Blueprint, Input System, Audio, Game Design]
prev_url: "/unreal-engine-5/jeu-horreur-kawaii/8-ia-behavior-tree-blackboard-ennemi"
next_url: "/unreal-engine-5/jeu-horreur-kawaii/10-slender-animations-3d-spacialisation-sonore-blendspace"
images: ["https://img.youtube.com/vi/mpM0HlCrteU/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/mpM0HlCrteU/maxresdefault.jpg"]
---

{{< youtube-rgpd "mpM0HlCrteU" >}}

Dans ce neuvième volet de la série *Kawaii Slender*, nous concrétisons le travail architectural débuté dans l'épisode précédent. Nous allons connecter la structure logique de notre arbre de comportement (Behavior Tree) à la vue 3D de notre ennemi (la créature gallinacée maléfique). Pour cela, nous configurons le système de perception natif d'Unreal Engine afin que l'IA puisse repérer visuellement le joueur et basculer en mode chasse.

### Concepts clés abordés dans ce tutoriel

* **Mise en place d'un AI Controller dédié :**
    * Création d'une classe de Blueprint héritant d'**AI Controller** (`AIC_Slender`). Ce script fait office de pilote invisible pour notre créature.
    * Liaison de l'IA au personnage : configuration du paramètre *AI Controller Class* dans le Blueprint du monstre (`BP_Slender`) pour s'assurer qu'il s'exécute automatiquement dès l'apparition du personnage sur la carte.
* **Intégration du composant AI Perception :**
    * Ajout du composant **AIPerception** au sein de l'AI Controller pour lui donner des capacités sensorielles.
    * Configuration du sens de la vue (**AI Sight Config**) : définition de l'angle de vision périphérique (*Lose Sight Radius* et *Sight Radius* à 3000 unités) et filtrage des cibles par affiliation (détection des entités neutres, amies ou ennemies).
* **Création de la logique de détection (Perception Updates) :**
    * Exploitation de l'événement **On Target Perception Updated** qui se déclenche dès qu'un élément entre ou sort du champ de vision de l'IA.
    * Utilisation du node **Break AIStimulus** pour interroger la structure des données sensorielles et récupérer la valeur booléenne `Successfully Sensed` (vrai si l'IA voit la cible, faux si elle la perd de vue).
* **Alimentation dynamique du Blackboard :**
    * Initialisation et lancement de l'arbre de comportement via le node **Run Behavior Tree** lors du *Begin Play* de l'AI Controller.
    * Utilisation du node **Set Value as Boolean** pour injecter l'état de détection de la cible directement dans la clé `VoitJoueur` de notre Blackboard. Ce changement de valeur force instantanément l'aiguillage du Behavior Tree entre la patrouille aléatoire et la poursuite.
* **Résolution des collisions et navigation (NavMesh) :**
    * Rappel de l'importance du volume **NavMeshBoundsVolume** pour générer les zones de déplacement de l'IA.
    * Ajustement des paramètres du composant *Capsule Component* du monstre et de ses composants physiques pour éviter que l'IA ne se bloque ou ne repousse brutalement les burgers interactifs présents au sol.

### Ce qui reste d'actualité aujourd'hui

Les paradigmes de détection et de contrôle des IA présentés dans cette archive s'appliquent fidèlement sur les versions modernes d'Unreal Engine 5 :

1. **La supériorité de l'AI Perception face aux Traces :** Utiliser le composant *AIPerception* reste la méthode standard et optimisée de l'industrie pour gérer la détection sensorielle (vue, ouïe, toucher). C'est un système asynchrone natif bien plus léger pour le CPU que d'exécuter des boucles de tir de rayons (*Line Traces*) à chaque frame dans le script du monstre.
2. **Le découplage par AI Controller :** Séparer l'enveloppe corporelle (le *Character Mesh* et ses animations) de sa logique décisionnelle (l'*AI Controller*) est une règle architecturale d'or sur Unreal Engine. Cela permet de modifier le comportement ou de réutiliser le même esprit d'IA sur des monstres visuellement différents sans réécrire le code.
3. **Le pilotage par événement du Blackboard :** Modifier les clés du Blackboard uniquement lorsqu'un événement sensoriel se produit (*On Target Perception Updated*) plutôt que d'interroger la distance du joueur en continu garantit un code propre, performant et parfaitement adapté au débogage visuel via l'outil de diagnostic de l'IA d'Unreal.

---
{{< footer >}}
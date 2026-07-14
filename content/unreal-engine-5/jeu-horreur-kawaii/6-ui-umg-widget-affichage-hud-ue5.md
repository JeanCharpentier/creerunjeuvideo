---
title: "6. Création de l'interface HUD (Viseur, Batterie et Endurance)"
date: 2026-06-12
category: Archive
weight: 6
tags: [Unreal Engine 5, Kawaii Slender, Blueprint, Input System, Audio, Game Design]
prev_url: "/unreal-engine-5/jeu-horreur-kawaii/5-variable-sprint-course-stamina"
next_url: "/unreal-engine-5/jeu-horreur-kawaii/7-ramassage-objet-score-points-compteur"
images: ["https://img.youtube.com/vi/azXsAPmcO5k/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/azXsAPmcO5k/maxresdefault.jpg"]
---

{{< youtube-rgpd "azXsAPmcO5k" >}}

Après avoir mis en place les mécaniques de fond pour la lampe-torche et la gestion de la course, il est indispensable de donner des retours visuels clairs au joueur. Cet épisode se concentre sur l'habillage de notre prototype avec la création complète d'un HUD (Heads-Up Display) dynamique sous Unreal Engine 5.

### Concepts clés abordés dans ce tutoriel

* **Préparation d'un asset graphique transparent :**
    * Conception d'une texture de réticule de visée carrée ($64 \times 64$ pixels) exportée au format PNG avec un canal Alpha pour gérer la transparence.
    * Importation de la ressource dans le dossier des textures du projet.
* **Architecture et mise en page sous UMG (Unreal Motion Graphics) :**
    * Création d'un **Widget Blueprint** (`WBP_MainUI`) structuré autour d'un *Canvas Panel* global.
    * Utilisation du système d'ancres (**Anchors**) et ajustement chirurgical de l'alignement (`0.5` en X et Y) pour fixer le viseur parfaitement au centre de l'écran, indépendamment du ratio ou de la résolution d'affichage.
    * Emploi d'une **Vertical Box** en bas à gauche de l'écran pour empiler et organiser automatiquement des barres de progression (*Progress Bars*) sans positionnement manuel fastidieux.
* **Liaison de données (Data Binding) et optimisation CPU :**
    * Utilisation de la propriété *Percent* des barres de progression (valeurs normalisées de `0.0` à `1.0`) pour refléter les états de la batterie et de la stamina.
    * **Bonne pratique d'optimisation :** Utilisation de l'événement **Event Construct** du Widget pour effectuer un unique moulage (**Cast to BP_FirstPersonCharacter**) et stocker la référence du joueur dans une variable locale (`Joueur`). Cela évite de répéter un node *Cast* très gourmand à chaque image.
* **Instanciation de l'interface via le Game Mode :**
    * Initialisation du Widget lors de l'événement général **Event Begin Play** dans le Blueprint du mode de jeu (*Game Mode*).
    * Enchaînement des nodes indispensables **Create Widget** (sélection de la classe) puis **Add to Viewport** pour injecter visuellement l'UI sur l'écran de jeu.

### Ce qui reste d'actualité aujourd'hui

Les principes de conception d'interface utilisateur présentés dans cette archive posent des bases techniques qui n'ont pas bougé sur Unreal Engine 5 :

1. **La mise en cache des références au Construct :** Réaliser des calculs lourds ou des vérifications d'identité (*Casting*) dans des fonctions de liaison ou directement sur un *Tick* est l'une des erreurs de performance majeures commises par les débutants. Extraire le profil du joueur une seule fois à l'initialisation reste la règle absolue.
2. **La flexibilité d'UMG face aux résolutions modernes :** L'usage conjoint des ancres et de conteneurs composites (*Vertical/Horizontal Boxes*) demeure indispensable pour concevoir des jeux PC et consoles capables de s'adapter proprement aux écrans ultra-larges (*Ultrawide*) et aux affichages mobiles.
3. **Le découplage de l'interface :** Instancier le HUD principal via le *Game Mode* ou le *Player Controller* au lancement du niveau assure une architecture modulaire et saine, idéale pour charger et décharger les interfaces proprement lors des transitions de gameplay.

---
{{< footer >}}
---
title: "1. Les Fondations et le Ghost"
date: 2026-06-12
category: Archive
weight: 1
tags: [Unreal Engine 5, Build, Blueprint, Input System, Audio, Game Design]

# Navigation de la série (remplir avec les URLs relatives)
prev_url: "/unreal-engine-5/enhanced-input-mapping/index.html"
next_url: "/unreal-engine-5/systeme-construction/2-raytracing-raycasting-blocs-poser"
images: ["https://img.youtube.com/vi/8IkLkMXLXj4/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/8IkLkMXLXj4/maxresdefault.jpg"]
---

Ce tutoriel est issu de mes archives et est partagé pour son intérêt conceptuel.

{{< youtube-rgpd "8IkLkMXLXj4">}}

Dans cette première partie d'une mini-série consacrée aux systèmes de construction (similaires à ceux des jeux de survie ou de Fortnite), nous posons les bases techniques indispensables pour permettre au joueur de prévisualiser et de poser des structures dans le monde.

### Concepts clés abordés dans ce tutoriel

* **Mise en place de l'environnement :** Utilisation du modèle First Person Template nettoyé et import de meshes spécifiques conçus pour s'empiler parfaitement (murs, sols, fenêtres, toits).
* **Création du Master Material "Ghost" :** * Configuration d'un matériau translucide vert servant de guide visuel avant le placement de l'objet.
    * Utilisation de paramètres de type Vector (Color) et Scalar (Opacity) modifiables par la suite via des instances.
    * Activation de l'option Two-Sided pour donner du relief et de la visibilité aux faces internes de la prévisualisation.
* **Architecture Blueprint Parent-Enfant (POO) :**
    * Création d'un Blueprint Maître (MBP_BuildBlock) englobant la logique commune à toutes les structures.
    * Génération d'un Blueprint Enfant (BP_BuildWall) qui hérite automatiquement des propriétés et des événements du parent.
* **Logique de l'Event Graph pour le placement :**
    * **Phase de prévisualisation :** Sauvegarde du matériau d'origine dans une variable au chargement de l'acteur, application du matériau Ghost et désactivation complète des collisions pour éviter les conflits avec le décor.
    * **Phase de validation (Custom Event Placed) :** Bascule d'une variable booléenne IsPlaced à True, réapplication du matériau d'origine et réactivation de collisions optimisées (Query Only) pour économiser les ressources.
* **Configuration des Inputs :** Création d'un nouveau mapping d'action (Build Mode) assigné par défaut à la touche B pour entrer ou sortir du mode construction.

### Ce qui reste d'actualité aujourd'hui

Bien que ce tutoriel utilise une logique initialement pensée pour Unreal Engine 4, les mécaniques présentées forment les piliers immuables du gamedev moderne :

1. **La programmation orientée objet (Parents/Enfants) :** Structurer ses architectures avec un Blueprint maître reste la meilleure méthode sur Unreal Engine 5 pour concevoir un système de build évolutif sans jamais dupliquer son code.
2. **L'optimisation des matériaux :** L'usage de Master Materials paramétriques destinés à être déclinés en Material Instances est toujours la norme absolue pour préserver les performances graphiques et la mémoire vidéo.
3. **La gestion fine des collisions :** Passer par un état "No Collision" durant la prévisualisation, puis réactiver des profils légers comme le Query Only, reste la technique standard pour éviter les bugs physiques et les chutes de framerate lors de l'empilement d'objets.
{{< footer >}}
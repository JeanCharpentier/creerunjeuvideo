---
title: "0. Introduction à la création de jeux"
weight: 0
date: 2026-06-17
categories: ['GameDev']
tags: ['Unreal Engine 4', 'Blender', 'Tutoriel', 'Débutant', 'Game Design']
---

Bienvenue dans cette série de tutoriels dédiée à la création de jeux vidéo. L'objectif est de vous accompagner pas à pas dans la réalisation d'un projet complet, en utilisant l'Unreal Engine 4 comme moteur principal. Nous allons concevoir un jeu de type "Slender" (collecte d'objets avec une menace poursuivante), mais avec une direction artistique originale : un style "low-poly" coloré et kawaii, à l'opposé des ambiances sombres habituelles.

{{< youtube-rgpd "fCCWc2H_7xk" >}}

### Ce que nous allons aborder dans cette série :
*   **Modélisation 3D :** Création des assets avec Blender.
*   **Texturing et UI :** Utilisation de Paint.net pour les textures et l'interface utilisateur (HUD).
*   **Personnages :** Utilisation de MakeHuman pour générer et riguer nos personnages rapidement.
*   **Intégration :** Importation et configuration dans Unreal Engine 4.
*   **Logique de jeu :** Mise en place des mécaniques de ramassage d'objets et des comportements de l'IA.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions logicielles mentionnées (UE 4.10, Blender 2.76) soient aujourd'hui obsolètes, les principes fondamentaux enseignés restent le socle de tout développeur :

1.  **Le pipeline de production :** La méthodologie consistant à créer ses modèles dans un logiciel tiers (Blender) pour les importer dans un moteur de jeu est toujours le standard de l'industrie.
2.  **L'importance du prototypage :** Apprendre à créer un jeu simple (type "collecte") est la meilleure façon de comprendre les interactions, les triggers et la gestion des états dans un moteur comme Unreal.
3.  **La modularité :** L'utilisation de logiciels spécialisés (MakeHuman pour le rigging, outils de retouche pour les textures) reste une pratique courante pour gagner en productivité.
4.  **La philosophie "Engine Agnostic" :** Même si vous utilisez Unreal Engine 5 aujourd'hui, la logique de création de "Blueprints" ou de gestion d'armatures est directement héritée de ces bases. Les concepts de "Game Loop" ne changent pas, seule la puissance des outils évolue.

{{< footer >}}
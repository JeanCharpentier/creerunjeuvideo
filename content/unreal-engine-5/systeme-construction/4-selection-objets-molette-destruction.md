---
title: "4. Sélection des Blocs à la Molette et Système de Destruction"
date: 2026-06-12
category: Archive
weight: 4
tags: [Unreal Engine 5, Build, Blueprint, Input System, Audio, Game Design]

prev_url: "/unreal-engine-5/systeme-construction/3-overlaps-erreurs-construction"
next_url: ""
images: ["https://img.youtube.com/vi/mUvL7on9Gds/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/mUvL7on9Gds/maxresdefault.jpg"]
---

Ce tutoriel est issu de mes archives et est partagé pour son intérêt conceptuel.

{{< youtube-rgpd "mUvL7on9Gds" >}}

Dans ce quatrième épisode, nous enrichissons l'expérience utilisateur en permettant au joueur de naviguer de manière fluide entre plusieurs types de structures (murs, sols, toits) à l'aide de la molette de la souris, tout en implémentant les bases d'un mode de destruction pour nettoyer ses chantiers.

### Concepts clés abordés dans ce tutoriel

* **Gestion d'un inventaire de structures via Array :**
    * Création d'une variable de type Tableau (*Array*) contenant les classes de nos Blueprints enfants (`BP_BuildWall`, `BP_BuildFloor`, etc.).
    * Utilisation d'une variable d'index entier (`CurrentIndex`) pour suivre le bloc actuellement sélectionné par le joueur.
* **Logique de défilement cyclique (Scroll) :**
    * Interception des inputs de la molette de la souris (`Mouse Scroll Up` et `Mouse Scroll Down`).
    * Implémentation d'un système de boucle mathématique : incrémentation ou décrémentation de l'index, avec réinitialisation automatique à 0 si l'on dépasse la taille maximale du tableau, ou bascule sur le dernier élément si l'on descend en dessous de zéro.
* **Changement dynamique d'acteur en temps réel :**
    * Destruction instantanée du Ghost actuel dès qu'un changement de sélection est détecté.
    * Réinitialisation de la fonction de *Spawn* pour faire apparaître immédiatement le nouveau modèle sélectionné, garantissant une transition visuelle transparente pour le joueur.
* **Introduction du mode destruction (Demolish) :**
    * Configuration d'une touche dédiée (ex: **X**) pour basculer entre le mode "Pose" et le mode "Destruction".
    * Utilisation du tracé de ligne (*Line Trace*) existant : si le rayon touche un bloc de construction déjà posé dans le monde, l'appui sur le clic gauche déclenche la fonction `Destroy Actor` pour supprimer instantanément la structure visée.

### Ce qui reste d'actualité aujourd'hui

Bien que l'architecture des entrées utilisateur ait évolué avec le système *Enhanced Input* d'Unreal Engine 5, la logique algorithmique demeure identique :

1. **La puissance des tableaux (Arrays) de classes :** Utiliser un tableau pour stocker des classes d'acteurs afin de les instancier dynamiquement est la méthode universelle pour créer des barres d'action, des inventaires ou des menus de sélection dans n'importe quel moteur de jeu.
2. **Le nettoyage des acteurs en mémoire :** Penser à détruire proprement l'ancien Ghost (`Destroy Actor`) avant d'en recréer un nouveau à chaque coup de molette est un réflexe de programmation essentiel pour éviter les fuites de mémoire (Memory Leaks) et la multiplication d'objets invisibles.
3. **Le recyclage des tracés de rayons (Line Trace) :** Utiliser la même logique de détection de visée (le *Line Trace* de la caméra) à la fois pour poser un bloc et pour le cibler en mode destruction est un excellent exemple de réutilisation de code propre (*DRY - Don't Repeat Yourself*), optimisant ainsi les performances de scripts.


{{< footer >}}
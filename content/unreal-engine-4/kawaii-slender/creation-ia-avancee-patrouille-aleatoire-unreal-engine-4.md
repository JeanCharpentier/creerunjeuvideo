---
title: "14. Création d''une IA avancée : Patrouille aléatoire"
weight: 14
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Unreal Engine 4', 'Blueprints', 'IA', 'GameDev', 'Tutoriel']
images: ["https://img.youtube.com/vi/-H34L60gGmM/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/-H34L60gGmM/maxresdefault.jpg"]
---

Dans ce tutoriel, nous allons donner un peu plus de vie à notre intelligence artificielle. Jusqu'à présent, notre "Slender" se contentait de nous foncer dessus dès qu'il nous voyait. Nous allons maintenant lui apprendre à patrouiller de manière aléatoire sur la carte lorsqu'il ne détecte pas le joueur, rendant son comportement beaucoup plus imprévisible et réaliste.

{{< youtube-rgpd "-H34L60gGmM" >}}

### Résumé du tutoriel
*   **Gestion des états avec les variables booléennes :** Création de deux variables (`VisionCheck` et `Mouvement`) pour suivre l'état actuel de l'IA.
*   **Logique de détection :** Mise à jour du script pour basculer `VisionCheck` à *True* lors de la détection du joueur et à *False* après un court délai suite au contact.
*   **Utilisation de l'Event Tick :** Mise en place d'une structure de conditions (Branches) pour vérifier en continu si l'IA doit poursuivre le joueur ou se déplacer aléatoirement.
*   **Déplacement aléatoire :** Utilisation de la fonction `Get Random Reachable Point in Radius` pour générer une destination valide autour de l'IA.
*   **Gestion du mouvement :** Activation et désactivation de la variable `Mouvement` pour éviter que l'IA ne tente de recalculer un chemin à chaque frame.

### Ce qui reste d'actualité aujourd'hui
Bien que ce tutoriel utilise les bases des Blueprints d'Unreal Engine 4, les concepts fondamentaux restent parfaitement applicables dans les versions récentes (UE5) :
*   **Le système de NavMesh :** Le `NavMeshBoundsVolume` est toujours la méthode standard pour définir les zones de déplacement des IA.
*   **La logique d'état :** L'utilisation de variables booléennes pour gérer des états simples est une excellente base avant de passer à des systèmes plus complexes comme les *Behavior Trees* (Arbres de comportement).
*   **Event Tick :** Bien que l'utilisation de l'Event Tick doive être limitée pour des raisons de performance, la logique de branchement conditionnel présentée ici est le socle de toute programmation événementielle dans Unreal Engine.

{{< footer >}}
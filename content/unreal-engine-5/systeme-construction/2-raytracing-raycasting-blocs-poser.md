---
title: "2. Rotation, Tracé de Ligne et Pose des Blocs"
date: 2026-06-12
category: Archive
weight: 2
tags: [Unreal Engine 5, Build, Blueprint, Input System, Audio, Game Design]
prev_url: "/unreal-engine-5/systeme-construction/1-introduction-ghost-object-blueprint"
next_url: "/unreal-engine-5/systeme-construction/3-overlaps-erreurs-construction"
images: ["https://img.youtube.com/vi/ZnRD83zyQvs/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/ZnRD83zyQvs/maxresdefault.jpg"]
---

Ce tutoriel est issu de mes archives et est partagé pour son intérêt conceptuel.

{{< youtube-rgpd "ZnRD83zyQvs" >}}

Dans cette deuxième partie, nous passons à la vitesse supérieure en connectant le personnage à notre système de construction. L'objectif est de projeter la prévisualisation dans le monde via un tracé de ligne, d'autoriser la rotation du bloc et de valider sa pose finale.

### Concepts clés abordés dans ce tutoriel

* **Gestion de la rotation du Ghost :**
    * Configuration de l'input de rotation (touche **R**) dans les paramètres du projet.
    * Utilisation de l'événement `Mouse Wheel` combiné à une logique d'incrémentation d'angle (+90° ou -90°) pour faire pivoter le Blueprint de prévisualisation de manière fluide et précise avant la pose.
* **Le Tracé de Ligne (Line Trace by Channel) :**
    * Récupération de la position et du vecteur de direction de la caméra du joueur (`Get World Location` et `Get Forward Vector`).
    * Calcul de la portée maximale de construction en multipliant le vecteur de direction par une constante (ex: 1500 unités) pour obtenir le point d'arrivée du tracé dans l'espace 3D.
* **Logique de Tick et Spawn Dynamique :**
    * À chaque frame (`Event Tick`), si le mode construction est actif, le système effectue le *Line Trace*.
    * Si le tracé ne touche rien, le Ghost se positionne par défaut au bout de la ligne de portée. S'il y a un impact (*Hit Result*), l'emplacement du Ghost est immédiatement mis à jour sur le point d'impact.
* **Instanciation et Transition (Spawn & Place) :**
    * Création d'une fonction pour faire apparaître proprement l'acteur de prévisualisation (`Spawn Actor from Class`) dès l'activation du mode build.
    * Gestion de la validation avec le clic gauche de la souris : appel du *Custom Event* `Placed` (développé en partie 1) qui fige le bloc dans le monde, réactive ses collisions, puis instancie immédiatement un nouveau Ghost pour permettre au joueur de continuer à construire en continu.

### Ce qui reste d'actualité aujourd'hui

Bien que les menus ou certains noms de nœuds aient légèrement évolué avec Unreal Engine 5, les concepts de Game Design Engineer présentés ici restent indispensables :

1. **Le Line Tracing pour l'interaction :** Que ce soit sur UE4 ou UE5, l'utilisation d'un *Line Trace* (ou *Raycast*) basé sur la caméra reste la méthode standard et la plus optimisée pour savoir exactement ce que le joueur regarde et où il souhaite interagir avec le décor.
2. **Le découplage de la prévisualisation (Ghost vs Objet Physique) :** Séparer la logique du "fantôme" temporaire et de l'objet solidifié dans le monde est le seul moyen propre de gérer les performances, évitant ainsi de charger des calculs physiques ou des scripts complexes tant que l'objet n'est pas officiellement posé.
3. **Le flux séquentiel des fonctions :** Organiser ses scripts en vérifiant systématiquement la validité des pointeurs (les nœuds `Is Valid`) avant de manipuler un acteur en mémoire reste la règle d'or pour s'assurer qu'un jeu ne plante pas (Crash / Access Violation) en cours de partie.


{{< footer >}}
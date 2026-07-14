---
title: "Gérer le multijoueur local (4 joueurs) avec des manettes dans GDevelop 5"
date: 2026-06-17
categories: ['Tutoriels']
tags: ['GDevelop 5', 'Multijoueur', 'Gamepad', 'Tutoriel', 'GameDev']
images: ["https://img.youtube.com/vi/h9GRHb22ybA/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/h9GRHb22ybA/maxresdefault.jpg"]
---

Le multijoueur local est un excellent moyen de rendre vos jeux plus conviviaux. Dans ce tutoriel, nous allons voir comment configurer un système permettant de contrôler jusqu'à 4 joueurs simultanément avec des manettes dans GDevelop 5, en utilisant une approche propre et optimisée basée sur un "Player Controller".

{{< youtube-rgpd "h9GRHb22ybA" >}}

### Résumé de la méthode
*   **Utilisation d'un "Player Controller" :** Au lieu de créer 4 objets différents, nous utilisons un seul objet "joueur" que nous instancions 4 fois. Chaque instance possède une variable `PlayerID` unique pour identifier sa manette associée.
*   **Extension Gamepad :** Installation de l'extension officielle "Gamepad" pour détecter les entrées des manettes.
*   **Variables de scène :** Utilisation d'un tableau de variables booléennes (`ActivatedGamepads`) pour suivre quelles manettes sont connectées et actives.
*   **Logique centralisée :** Les événements de mouvement et d'action sont écrits une seule fois pour tous les joueurs, en utilisant le `PlayerID` de l'instance pour filtrer les entrées.
*   **Gestion des sticks :** Utilisation des expressions `StickForce` et `StickAngle` pour un contrôle fluide du mouvement et de la visée.

### Ce qui reste d'actualité aujourd'hui
*   **L'architecture "Controller" :** Cette méthode reste la plus efficace pour éviter la duplication d'événements. Si vous devez modifier la vitesse de déplacement ou ajouter une nouvelle capacité (comme un dash), vous ne le faites qu'une seule fois dans votre feuille d'événements.
*   **L'extension Gamepad :** Elle demeure l'outil standard et indispensable pour gérer les manettes dans GDevelop.
*   **La contrainte de l'ordre :** Comme mentionné dans la vidéo, cette technique nécessite que les manettes soient activées dans l'ordre (1, 2, 3, 4). C'est un point technique important à anticiper dans votre interface utilisateur (UI) pour guider les joueurs lors de la sélection des personnages.
*   **Gestion de la caméra :** Le défi du multijoueur local reste la caméra. La solution la plus simple reste de limiter les joueurs dans une zone fixe, mais les techniques de zoom dynamique ou de "split-screen" restent des pistes d'évolution pertinentes pour des projets plus ambitieux.

{{< footer >}}
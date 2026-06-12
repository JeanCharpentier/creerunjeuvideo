---
title: "Partie 3 : Gestion des Overlaps et Interdiction de Placement"
date: 2026-06-12
category: Archive
tags:
  - Unreal Engine
  - Blueprints
  - Game Design
  - Tutoriel

prev_url: "/unreal-engine-5/systeme-construction/cours-2/"
next_url: "/unreal-engine-5/systeme-construction/cours-4/"
---

Ce tutoriel est issu de mes archives et est partagé pour son intérêt conceptuel.

{{< youtube-rgpd "thJWz64OKCQ" >}}

Dans cette troisième partie, nous abordons un aspect crucial du confort de jeu et de la robustesse technique : la gestion des collisions aberrantes. L'objectif est d'empêcher le joueur de tricher ou de casser l'immersion en superposant des structures les unes sur les autres, en mettant en place un retour visuel dynamique (vert/rouge).

### Concepts clés abordés dans ce tutoriel

* **Détection des volumes superposés (Overlap) :**
    * Utilisation des événements `On Component Begin Overlap` et `On Component End Overlap` sur la boîte de collision (*Box Collision*) de notre Blueprint Maître.
    * Filtrage des détections pour ignorer le joueur lui-même et s'assurer que le Ghost ne réagit qu'aux autres blocs de construction déjà solidifiés dans le monde.
* **Gestion d'un compteur d'interférences :**
    * Création d'une variable entière `Overlap Count` pour suivre le nombre d'objets en collision avec le Ghost.
    * Incrémentation (+1) lorsqu'un objet entre dans la zone et décrémentation (-1) lorsqu'il en sort, évitant ainsi les faux négatifs si le Ghost touche plusieurs structures simultanément.
* **Changement dynamique de couleur du Ghost :**
    * Exploitation des *Material Instances* pour modifier à la volée les paramètres vectoriels du matériau translucide.
    * Création d'une fonction de mise à jour visuelle : application d'une couleur verte si `Overlap Count` est égal à 0 (placement valide) et bascule sur une couleur rouge d'alerte dès que le compteur est supérieur à 0 (placement invalide).
* **Conditionnalité de la validation (Le Booléen de contrôle) :**
    * Introduction d'une variable booléenne `CanBuild` mise à jour en temps réel selon l'état du compteur d'overlaps.
    * Branchement d'un nœud de condition (*Branch*) sur l'action de clic gauche du joueur pour bloquer l'appel de l'événement `Placed` tant que la zone n'est pas totalement dégagée.

### Ce qui reste d'actualité aujourd'hui

Les outils visuels d'Unreal Engine 5 ont été modernisés, mais la logique systémique sous-jacente reste inchangée pour tout développeur de jeux de survie ou de gestion :

1. **La technique du compteur d'overlaps (Counter vs Boolean) :** Utiliser un compteur d'objets plutôt qu'un simple booléen *True/False* lors des intersections reste la méthode standard en gamedev. Cela empêche le système de croire à tort que la voie est libre lorsqu'un premier objet quitte la zone alors qu'un deuxième s'y trouve encore.
2. **Le feedback visuel immédiat (Juiciness) :** Changer la couleur d'un hologramme (vert/rouge) est une règle d'or d'UX (User Experience). Donner une réponse instantanée aux actions du joueur avant même qu'il ne clique est indispensable pour éviter la frustration.
3. **L'optimisation par événements plutôt qu'en Tick :** Bien que la position du Ghost soit rafraîchie à chaque frame, la vérification de la validité du placement est entièrement gérée par des événements de collision (`Begin/End Overlap`). Cette approche événementielle est toujours indispensable aujourd'hui pour économiser du temps CPU.

{{< footer >}}
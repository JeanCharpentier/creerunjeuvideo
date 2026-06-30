---
title: "2. Passer de la vue TPS à la vue FPS dans Unreal Engine 4"
weight: 2
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['FPS', 'Blueprint', 'Camera', 'GameDev', 'Tutoriel']
---

Dans ce nouvel épisode de notre série dédiée au développement FPS sur Unreal Engine 4, nous allons aborder une étape fondamentale : la transition de votre personnage de la vue à la troisième personne (TPS) vers une vue à la première personne (FPS). Que vous soyez un nouvel arrivant ou que vous souhaitiez mettre à jour vos connaissances, ce guide vous permettra de configurer votre caméra pour une immersion totale.

{{< youtube-rgpd "VFF4YOzY4s8" >}}

### Résumé des étapes clés
*   **Modification de la hiérarchie :** Déplacer la `FollowCamera` pour qu'elle devienne enfant du `Mesh` (et non plus du `CameraBoom`).
*   **Attachement au Skeleton :** Utiliser les sockets (ou les bones) pour fixer la caméra directement sur la tête du personnage (`head`).
*   **Paramétrage de la caméra :** Désactiver le `CameraBoom` et ajuster manuellement la position et la rotation de la caméra pour l'aligner avec le regard du personnage.
*   **Contrôle de rotation :** Activer l'option `Use Pawn Control Rotation` sur la caméra et sur l'acteur pour synchroniser les mouvements de la souris avec la vue.
*   **Astuce Workflow :** Utiliser l'option "Save on Compile" pour automatiser la sauvegarde de vos Blueprints.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Unreal Engine aient évolué, les concepts fondamentaux présentés ici restent des piliers du développement :
1.  **La gestion des hiérarchies :** Comprendre comment les composants héritent de leurs parents est crucial pour tout système de caméra ou d'attachement d'objets.
2.  **L'utilisation des Sockets :** L'attachement aux bones du squelette est toujours la méthode standard pour gérer les caméras FPS, les armes ou les accessoires.
3.  **Le contrôle de rotation :** La gestion du `Pawn Control Rotation` est le mécanisme de base pour la caméra FPS dans le moteur, garantissant une fluidité de mouvement cohérente avec les inputs du joueur.
4.  **Optimisation du workflow :** L'organisation de vos Blueprints et l'utilisation des outils de compilation automatique restent des bonnes pratiques pour gagner en productivité et éviter les erreurs de manipulation.

{{< footer >}}
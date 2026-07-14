---
title: "35. Créer une cinématique d''introduction avec le Sequencer"
weight: 35
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Unreal Engine 4', 'Sequencer', 'Cinématique', 'Level Design', 'Blueprint']
images: ["https://img.youtube.com/vi/5Ps4s3EZZDQ/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/5Ps4s3EZZDQ/maxresdefault.jpg"]
---

Dans cet épisode, nous abordons la création d'une séquence d'introduction pour votre jeu. L'objectif est de réaliser un mouvement de caméra fluide qui se termine par une transition en fondu au noir, tout en redonnant le contrôle au joueur une fois la séquence terminée.

{{< youtube-rgpd "5Ps4s3EZZDQ" >}}

### Résumé du tutoriel
*   **Organisation :** Création d'un dossier dédié aux cinématiques pour maintenir une structure de projet propre.
*   **Level Sequence :** Utilisation de l'outil *Sequencer* pour créer une séquence de niveau, ajout d'une caméra et configuration du *Camera Cut*.
*   **Animation :** Utilisation des *keyframes* (images clés) pour définir les positions et rotations de la caméra sur la timeline.
*   **Gestion des inputs :** Utilisation du *Level Blueprint* pour désactiver les entrées du joueur au début de la séquence (`Disable Input`) et les réactiver après un délai (`Enable Input`).
*   **Transitions :** Ajout d'une *Fade Track* dans le Sequencer pour créer des fondus au noir fluides au début et à la fin de l'intro.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes d'Unreal Engine (UE5) aient apporté des améliorations majeures à l'interface du Sequencer, les fondamentaux présentés ici restent parfaitement valides :
*   **Le workflow du Sequencer :** La logique de création de pistes, l'ajout de caméras et la gestion des images clés sont identiques.
*   **Le contrôle du joueur :** La méthode consistant à désactiver/réactiver les entrées via le Blueprint reste la technique standard pour empêcher le joueur de bouger pendant une cinématique.
*   **La gestion des fondus :** L'utilisation des *Fade Tracks* est toujours le moyen le plus rapide et efficace pour gérer les transitions de caméra sans passer par des widgets complexes.
*   **Temps réel :** La puissance du rendu en temps réel dans le viewport reste l'atout majeur de l'outil, permettant d'itérer très rapidement sur le rythme de votre mise en scène.

{{< footer >}}
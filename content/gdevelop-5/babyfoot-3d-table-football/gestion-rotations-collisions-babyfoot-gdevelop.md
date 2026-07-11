---
title: "5. Gestion des rotations et collisions pour votre Baby-foot"
weight: 5
date: 2023-10-27
categories: ['Tutoriels GDevelop']
tags: ['GDevelop 5', 'Physique 3D', 'GameDev', 'Baby-foot']
---

Dans cet épisode de notre série sur la création d'un baby-foot avec GDevelop 5, nous allons nous concentrer sur le "game feel". Un bon jeu ne repose pas seulement sur des mécaniques fonctionnelles, mais sur des retours visuels gratifiants. Aujourd'hui, nous allons affiner les collisions et ajouter une animation de rotation dynamique à nos joueurs lorsqu'ils frappent la balle.

{{< youtube-rgpd "Iv1vdjxD42A" >}}

### Au programme de cet épisode :

*   **Optimisation des collisions :** Remplacement des formes de collision (boîtes) par des capsules pour un comportement plus fluide et moins anguleux.
*   **Gestion de la restitution :** Réglage de la restitution à 0 pour reprendre le contrôle total des rebonds via le code plutôt que par le moteur physique.
*   **Animation de rotation :** Création d'un système de rotation angulaire déclenché lors du contact avec la balle.
*   **Gestion du timing :** Utilisation des chronomètres d'objets pour arrêter la rotation après une durée précise (0,2 seconde), assurant un effet visuel propre et répétable.
*   **Différenciation des équipes :** Application de rotations opposées pour les joueurs rouges et bleus afin de dynamiser le terrain.

### Ce qui reste d'actualité aujourd'hui

Même si GDevelop évolue, les principes abordés ici restent fondamentaux pour tout projet 3D :

1.  **Le contrôle manuel vs physique :** Il est souvent préférable de gérer les rebonds par le code (changement de vélocité) plutôt que de laisser le moteur physique gérer seul les collisions, ce qui permet une meilleure prédictibilité du gameplay.
2.  **L'importance du "Game Feel" :** Ajouter une petite rotation ou une animation simple lors d'une interaction (le contact balle/joueur) transforme un jeu statique en une expérience vivante.
3.  **La modularité :** Utiliser des groupes d'événements pour séparer les logiques d'équipe (Rouge vs Bleu) facilite grandement la maintenance et le débogage de votre projet.
4.  **Gestion des chronomètres :** L'utilisation des chronomètres d'objets est une technique robuste pour créer des actions temporaires sans alourdir le moteur avec des variables globales complexes.

{{< footer >}}
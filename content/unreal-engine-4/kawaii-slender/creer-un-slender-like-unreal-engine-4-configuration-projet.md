---
title: "1. Créer un Slender-like : Configurer son projet Unreal Engine 4"
weight: 1
date: 2026-06-17
categories: ['Tutoriels']
tags: ['Unreal Engine 4', 'GameDev', 'Blueprint', 'FPS', 'Débutant']
images: ["https://img.youtube.com/vi/cZSkaLaZsRc/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/cZSkaLaZsRc/maxresdefault.jpg"]
---

Bienvenue dans cette série dédiée à la création d'un jeu de type "Slender-like". Pour ce premier épisode, nous allons poser les bases de notre projet. Plutôt que d'utiliser le template FPS classique (qui ne propose que des bras et une arme), nous allons détourner le template **Third Person** pour obtenir une vue à la première personne tout en conservant le corps complet du personnage.

{{< youtube-rgpd "cZSkaLaZsRc" >}}

### Résumé des étapes de configuration
*   **Création du projet :** Lancement via l'Epic Games Launcher (version 4.10.2), sélection du template *Third Person* (pour bénéficier des animations de base) et désactivation du *Starter Content* pour un projet propre.
*   **Accès au Blueprint :** Ouverture du `ThirdPersonCharacter` pour modifier la hiérarchie des composants.
*   **Configuration de la caméra :** 
    *   Attachement de la `FollowCamera` au `Mesh` du personnage.
    *   Positionnement manuel de la caméra au niveau de la tête dans le Viewport.
*   **Paramétrage du Pawn :**
    *   Activation de l'option *Use Pawn Control Rotation* sur la caméra.
    *   Activation de *Use Control Rotation Yaw* dans les paramètres du personnage pour permettre la rotation du corps en fonction du regard.

### Ce qui reste d'actualité aujourd'hui
Bien que cet article se base sur une version ancienne d'Unreal Engine (4.10), les principes fondamentaux restent parfaitement valables pour les versions actuelles (UE5) :
*   **La logique des templates :** Le choix du template n'est qu'un point de départ. La manipulation des composants (Camera, Mesh, SpringArm) reste la méthode standard pour définir la perspective du joueur.
*   **L'utilisation des Blueprints :** La programmation visuelle par "briques" est toujours le cœur du développement sur Unreal Engine.
*   **La hiérarchie des composants :** Comprendre comment attacher une caméra à un socket ou à un mesh pour créer une vue "True FPS" (où l'on voit son corps) est une compétence indispensable pour l'immersion dans les jeux d'horreur.
*   **Le workflow de test :** L'utilisation du bouton "Play" pour itérer rapidement sur le positionnement de la caméra reste la base du travail de level design et de gameplay.

{{< footer >}}
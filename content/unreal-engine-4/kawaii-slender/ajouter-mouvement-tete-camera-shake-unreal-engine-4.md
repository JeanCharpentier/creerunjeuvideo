---
title: "2. Ajouter un mouvement de tête réaliste (Camera Shake)"
weight: 2
date: 2026-06-17
categories: ['Développement de jeux']
tags: ['Unreal Engine 4', 'Blueprints', 'Camera Shake', 'GameDev']
images: ["https://img.youtube.com/vi/zZbtywQzpiE/maxresdefault.jpg"]
---

Dans ce deuxième tutoriel dédié à Unreal Engine 4, nous allons donner un peu plus de vie à notre personnage. Après avoir configuré le corps et le mode de vue à la troisième personne, nous allons implémenter un effet de "Camera Shake" (vibration de caméra) pour simuler le mouvement naturel de la tête lors de la marche.

{{< youtube-rgpd "zZbtywQzpiE" >}}

### Résumé des étapes clés
*   **Création de la classe :** Création d'un Blueprint basé sur la classe `CameraShake` nommé `HeadShake`.
*   **Configuration des oscillations :** Réglage des paramètres de Pitch, Yaw et Roll pour simuler le mouvement naturel (montée/descente, rotation latérale, inclinaison).
*   **Intégration dans le Character Blueprint :** Utilisation du nœud `Client Play Camera Shake` lié aux entrées de mouvement (Move Forward / Move Right).
*   **Ajustement dynamique :** Utilisation du paramètre `Scale` pour lier l'intensité de la vibration à la vitesse de déplacement du joueur.
*   **Optimisation :** Utilisation du copier-coller dans l'éditeur de Blueprint pour gagner du temps sur les entrées redondantes.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes d'Unreal Engine (UE5+) aient introduit le système *Enhanced Input* et le *Camera Shake Source*, les principes fondamentaux abordés ici restent essentiels :
1.  **La modularité :** Séparer les effets de caméra dans des classes dédiées permet de garder votre `Character Blueprint` propre et maintenable.
2.  **La compréhension des axes :** Maîtriser le Pitch, le Yaw et le Roll est indispensable pour tout développeur souhaitant manipuler des objets ou des caméras dans un environnement 3D.
3.  **Le feedback visuel :** Ajouter des micro-mouvements (même légers) est une technique de "Game Feel" incontournable pour éviter l'aspect rigide et artificiel des déplacements de base.
4.  **Le workflow de test :** La méthode consistant à compiler, sauvegarder et tester immédiatement en jeu reste le cycle de développement standard pour itérer rapidement sur les sensations de gameplay.

{{< footer >}}
---
title: "4. Création et déploiement de votre premier projet Android"
weight: 4
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Android', 'Mobile', 'Déploiement', 'Tutoriel']
---

Dans cet épisode, nous passons à la pratique. Une fois votre environnement de développement et le SDK Android correctement configurés, il est temps de créer votre premier projet Unreal Engine 4 et de le déployer sur votre appareil mobile.

{{< youtube-rgpd "6kp9TRyOZpk" >}}

### Résumé des étapes clés
*   **Lancement du projet :** Utilisation du Epic Games Launcher pour ouvrir la version 4.17.2 (ou ultérieure).
*   **Choix du Template :** Sélection du modèle "Side Scroller" (version 3D) pour bénéficier de la profondeur de champ.
*   **Configuration cible :** Réglage sur "Mobile/Tablet" avec une qualité "Scalable 3D or 2D" pour optimiser les performances sur mobile.
*   **Optimisation :** Désactivation du "Starter Content" pour alléger le poids final de l'application.
*   **Déploiement :** Connexion de l'appareil via USB, activation du mode débogage USB, et utilisation du bouton "Launch" pour compiler et installer le jeu sur le terminal.
*   **Suivi :** Utilisation de l'Output Log pour surveiller la compilation des shaders (étape longue lors du premier lancement).

### Ce qui reste d'actualité aujourd'hui

Bien que cet épisode se base sur la version 4.17, les fondamentaux du déploiement mobile dans Unreal Engine restent très proches, même avec l'arrivée de l'Unreal Engine 5 :

1.  **La gestion des SDK :** Le principe de configurer le SDK Android via le *Project Settings* reste une étape indispensable pour que l'éditeur puisse communiquer avec votre appareil.
2.  **Le mode Débogage USB :** Cette étape est toujours le prérequis numéro un pour que votre PC reconnaisse votre smartphone ou tablette comme une cible de déploiement.
3.  **La compilation des Shaders :** C'est un processus inévitable. Lors du premier déploiement, Unreal doit convertir les matériaux pour qu'ils soient compatibles avec l'API graphique mobile (OpenGL ES ou Vulkan), ce qui explique toujours la durée importante de la première installation.
4.  **L'importance du "Scalable" :** Choisir le mode "Scalable" au lieu de "Maximum Quality" est toujours une bonne pratique pour garantir un framerate stable sur une large gamme d'appareils Android.

{{< footer >}}
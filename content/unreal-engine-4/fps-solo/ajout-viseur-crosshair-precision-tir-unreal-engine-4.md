---
title: "15. Ajout d''un viseur (Crosshair) et correction de la précision de tir"
weight: 15
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['FPS', 'HUD', 'Blueprints', 'GameDev']
images: ["https://img.youtube.com/vi/BnkE2jYFUog/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/BnkE2jYFUog/maxresdefault.jpg"]
---

Dans cet épisode, nous allons améliorer deux aspects cruciaux de notre FPS : l'interface utilisateur et la précision balistique. Jusqu'à présent, nos tirs dépendaient de la rotation du canon de l'arme, ce qui créait un décalage frustrant. Nous allons corriger cela pour que les projectiles suivent la direction réelle de la caméra, tout en ajoutant un viseur (crosshair) pour guider le joueur.

{{< youtube-rgpd "BnkE2jYFUog" >}}

### Résumé du tutoriel
*   **Importation du Crosshair** : Utilisation de ressources (comme Kenney.nl) pour obtenir un viseur propre, importé dans un dossier dédié (`Texture/HUD`).
*   **Configuration du Widget** : Ajout d'une image dans le Widget HUD, centrée via les paramètres d'alignement (0.5, 0.5) pour garantir une position fixe au centre de l'écran.
*   **Correction de la précision** : Modification du système de tir dans le `BP_Arme_Base`. Au lieu d'utiliser la rotation du socket de l'arme (qui bouge avec les animations), nous passons la rotation de la caméra du joueur (`Follow Camera`) comme paramètre au moment du tir.
*   **Mise à jour du Blueprint** : Utilisation d'un `Custom Event` avec un paramètre de type `Rotator` pour transmettre l'orientation de la caméra au projectile lors de son apparition (`SpawnActor`).

### Ce qui reste d'actualité aujourd'hui
Bien que cet épisode traite d'Unreal Engine 4, les concepts fondamentaux restent parfaitement applicables sur **Unreal Engine 5** :
*   **Le système de HUD (UMG)** : La méthode de création de widgets et l'utilisation des ancres (anchors) et de l'alignement restent la norme pour les interfaces 2D.
*   **La logique de tir** : Dans un FPS, il est toujours préférable de baser la direction du projectile sur la caméra (ou un *Line Trace* partant de la caméra) plutôt que sur le mesh de l'arme, afin d'éviter les imprécisions liées aux animations de "recul" ou de "sway".
*   **Modularité** : L'utilisation de `Custom Events` avec des paramètres d'entrée est une pratique propre et recommandée pour garder des Blueprints maintenables et réutilisables entre différentes armes.

{{< footer >}}
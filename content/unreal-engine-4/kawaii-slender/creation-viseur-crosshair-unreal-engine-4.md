---
title: "26. Création et intégration d''un viseur (Crosshair)"
weight: 26
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['HUD', 'UI', 'GameDev', 'Tutoriel', 'Crosshair']
images: ["https://img.youtube.com/vi/z_j4rfJs9Vs/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/z_j4rfJs9Vs/maxresdefault.jpg"]
---

Dans cet épisode de notre série "Kawaii Slender", nous allons améliorer l'aspect visuel et fonctionnel de notre jeu en ajoutant un élément indispensable pour tout jeu de tir ou d'interaction à la première personne : le viseur (ou *crosshair*). Fini le gros carré rouge de debug, place à un point de précision propre et discret.

{{< youtube-rgpd "z_j4rfJs9Vs" >}}

### Au programme de ce tutoriel :
*   **Création graphique :** Utilisation de Paint.net pour concevoir un viseur simple (33x33 pixels).
*   **Gestion des calques :** Astuces pour dessiner avec précision et centrer son élément.
*   **Importation :** Intégration du fichier PNG dans le dossier `HUD` de votre projet Unreal Engine 4.
*   **Configuration du HUD :** Ajout de l'image dans le widget, centrage mathématique selon la résolution (1080p) et ancrage.
*   **Nettoyage :** Suppression du *Debug Line Trace* dans le Blueprint du personnage pour une immersion totale.

### Ce qui reste d'actualité aujourd'hui
Bien que ce tutoriel utilise une version plus ancienne d'Unreal Engine, les principes fondamentaux restent parfaitement valides pour les versions actuelles (UE4 et UE5) :
*   **La logique du HUD :** La création de widgets via l'UMG (*Unreal Motion Graphics*) est toujours la méthode standard pour afficher des éléments 2D à l'écran.
*   **Le centrage des éléments :** La méthode de calcul (Résolution / 2 - Taille de l'image / 2) est une base mathématique incontournable en UI, même si les outils d'ancrage (*Anchors*) et d'alignement dans les versions récentes facilitent grandement cette tâche.
*   **Workflow de création :** L'utilisation d'outils externes (Paint.net, Photoshop, GIMP) pour créer des assets UI simples reste une pratique courante pour les développeurs indépendants.
*   **Debug vs Release :** La transition entre le *Debug Draw* (utilisé pour tester la logique de sélection) et l'affichage d'un élément UI propre est une étape clé du polissage d'un jeu.

{{< footer >}}
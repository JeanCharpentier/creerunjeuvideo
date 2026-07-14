---
title: "6. Créer un matériau d'eau dynamique"
weight: 6
prev_url: "/unreal-engine-4/creer-ses-matériaux/maitriser-les-textures-dans-unreal-engine-4/"
next_url: "/unreal-engine-4/creer-ses-matériaux/maitriser-le-tiling-des-textures-unreal-engine/"
date: 2024-05-22
categories: ['Archive']
tags: ['Unreal Engine 4', 'Material Editor', 'Game Design', 'Tutoriel']
images: ["https://img.youtube.com/vi/2wFRp6BMZ2A/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/2wFRp6BMZ2A/maxresdefault.jpg"]
---

Apprenez à concevoir un matériau d'eau réaliste et dynamique dans Unreal Engine 4 en utilisant les fonctions de profondeur, les normales animées et les effets de réfraction.

{{< youtube-rgpd "2wFRp6BMZ2A" >}}

### Résumé des notions clés

Ce tutoriel vous guide à travers les étapes essentielles pour créer une surface d'eau crédible :

*   **Gestion de la profondeur (Depth Fade) :** Utilisation du nœud `DepthFade` pour créer un dégradé de couleur naturel en fonction de la profondeur de l'eau.
*   **Mélange linéaire (Lerp) :** Technique permettant d'interpoler entre deux couleurs (ou textures) pour un rendu visuel fluide.
*   **Normal Maps et animation :** 
    *   Inversion des normales via un nœud `Multiply` et un `Constant3Vector` pour corriger le relief.
    *   Utilisation de `Panner` pour le mouvement simple ou de `Motion_FarWave_Chaos` pour un rendu plus organique et chaotique.
*   **Réfraction et physique :** Application du nœud `Fresnel` pour simuler le comportement de la lumière sur une surface liquide (indice de réfraction de l'eau à 1.33).
*   **Paramétrage du matériau :** Ajustement des propriétés `Roughness`, `Specular` et `Opacity` pour obtenir l'aspect translucide caractéristique de l'eau.

### Ce qui reste d'actualité aujourd'hui

Bien que ce tutoriel soit basé sur Unreal Engine 4, les fondamentaux du **Material Editor** restent inchangés dans Unreal Engine 5. La logique de création de matériaux "Master" reste la pierre angulaire du développement visuel :
*   **La modularité :** L'utilisation des *Material Functions* pour organiser vos graphes est une pratique indispensable pour maintenir des projets complexes.
*   **Le calcul procédural :** Les techniques de `DepthFade` et de `Fresnel` sont toujours les méthodes standards pour donner du volume et de la profondeur aux surfaces transparentes sans alourdir les performances.
*   **Le workflow de shading :** La compréhension des modes de mélange (`Translucent`, `Surface Forward Shading`) est toujours cruciale pour gérer correctement la lumière à travers des surfaces semi-transparentes.

{{< footer >}}
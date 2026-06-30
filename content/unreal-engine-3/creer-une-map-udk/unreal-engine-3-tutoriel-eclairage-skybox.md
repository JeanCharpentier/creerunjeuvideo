---
title: "6. Éclairage et Skybox dans Unreal Engine 3"
weight: 6
date: 2026-06-17
categories: ['Tutoriels GameDev']
tags: ['Unreal Engine 3', 'UDK', 'Level Design', 'Lighting']
---

Dans ce sixième épisode de notre série dédiée à la création d'un FPS multijoueur sous UDK (Unreal Development Kit), nous allons donner vie à notre environnement. Une carte vide ne prend réellement forme qu'une fois que l'ambiance lumineuse et le ciel sont correctement configurés. Nous allons voir comment intégrer un *Skydome* et paramétrer un éclairage dynamique pour structurer nos volumes.

{{< youtube-rgpd "OMUzEsQY5AM" >}}

### Résumé de l'épisode
*   **Intégration du Skydome :** Utilisation du *Content Browser* pour ajouter un ciel pré-configuré (Skydome) afin d'envelopper la carte dans une sphère visuelle.
*   **Directional Light :** Mise en place d'une lumière directionnelle dominante pour simuler le soleil, avec un focus sur la rotation pour gérer les ombres portées.
*   **Propriétés lumineuses :** Ajustement de la couleur (teintes orangées pour un coucher de soleil) et de la puissance (*Brightness*).
*   **Light Shafts :** Activation des rayons divins (volumétriques) pour ajouter du réalisme autour des objets.
*   **Point Lights :** Ajout de lumières ponctuelles pour éclairer les zones d'items et les recoins sombres, en jouant sur les couleurs pour créer des contrastes.
*   **Build Lighting :** Processus de calcul de la lumière (*Lightmass*) pour finaliser le rendu visuel de la scène.

### Ce qui reste d'actualité aujourd'hui

Bien que l'Unreal Engine 3 (UDK) soit une technologie ancienne, les principes fondamentaux abordés ici restent le socle du level design moderne :

1.  **La hiérarchie de la lumière :** La distinction entre la lumière directionnelle (lumière globale/soleil) et les lumières ponctuelles (sources locales) est toujours la base du travail dans Unreal Engine 5.
2.  **L'importance des ombres :** Le travail sur la rotation de la source lumineuse pour créer des contrastes et guider le regard du joueur est une technique intemporelle.
3.  **Le "Light Baking" :** Bien que nous utilisions aujourd'hui le *Lumen* (éclairage dynamique en temps réel), comprendre le processus de *Build Lighting* reste crucial pour optimiser les performances sur des projets plus légers ou mobiles.
4.  **L'ambiance par la couleur :** L'utilisation de teintes complémentaires (le bleu pour les items, le rouge pour les zones de danger) est une règle d'or du game design pour la lisibilité de l'interface environnementale.

{{< footer >}}
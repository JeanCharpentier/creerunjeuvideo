---
title: "12 et 13. Créer un matériau de lave dynamique"
weight: 13
prev_url: "/unreal-engine-4/creer-ses-matériaux/creer-materiau-lave-dynamique-unreal-engine/"
next_url: "/unreal-engine-4/creer-ses-matériaux/creer-effet-neige-dynamique-unreal-engine-4/"
date: 2023-10-27
categories: ['Archive']
tags: ['Unreal Engine 4', 'Materiaux', 'Tessellation', 'Shaders']
---

Apprenez à concevoir un matériau de lave réaliste et dynamique en utilisant les systèmes de textures, de masques et de tessellation dans Unreal Engine 4.

{{< youtube-rgpd "rCl-wIc9d48" >}}

{{< youtube-rgpd "_C-WsUo3eTw" >}}

### Résumé des notions clés

Ce tutoriel détaille la création d'un shader complexe pour simuler de la lave. Voici les points techniques abordés :

*   **Gestion des textures PBR :** Utilisation combinée des maps de couleur (Base Color), normale (Normal), rugosité (Roughness) et émissivité (Emissive).
*   **Animation de surface :** Utilisation du nœud `Panner` couplé à des `Texture Coordinates` pour créer un mouvement fluide de la lave.
*   **Masquage dynamique :** Utilisation d'une texture de masque (via le canal Alpha) pour contrôler précisément les zones lumineuses de l'émissivité.
*   **Tessellation et déplacement :** Application d'une texture de bruit (`Tiling Noise`) reliée au `World Displacement` pour déformer dynamiquement la géométrie du mesh.
*   **Optimisation :** Utilisation de `Scalar Parameters` pour permettre un contrôle en temps réel des valeurs (vitesse, intensité lumineuse, force de déformation) via les Blueprints.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions récentes d'Unreal Engine (UE5) aient introduit le système *Nanite* et le *Virtual Shadow Mapping*, les fondamentaux présentés ici restent piliers pour tout développeur :

1.  **La logique des masques :** La technique consistant à multiplier une texture émissive par un masque Alpha est toujours la méthode standard pour créer des effets de lumière localisés sur des matériaux.
2.  **Le workflow PBR :** La structure des entrées (Base Color, Roughness, Normal) demeure le standard industriel pour la création de shaders, quelle que soit la version du moteur.
3.  **Paramétrisation :** L'utilisation de `Scalar Parameters` est une bonne pratique indispensable pour créer des matériaux "Master" flexibles, permettant de modifier l'apparence d'un objet sans avoir à dupliquer le shader.
4.  **Déformation procédurale :** La manipulation des vertex via le `World Displacement` reste une technique efficace pour ajouter du relief organique à des surfaces planes, même si les méthodes de rendu ont évolué vers des solutions plus performantes pour les scènes à très haute densité géométrique.

{{< footer >}}
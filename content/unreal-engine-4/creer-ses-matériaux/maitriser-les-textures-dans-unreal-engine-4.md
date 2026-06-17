---
title: "5. Ajouter des textures"
weight: 5
prev_url: "/unreal-engine-4/creer-ses-matériaux/creer-materiaux-emissifs-unreal-engine/"
next_url: "/unreal-engine-4/creer-ses-matériaux/creer-materiau-eau-dynamique-unreal-engine/"
date: 2023-10-27
categories: ['Archive']
tags: ['Unreal Engine 4', 'Materiaux', 'Texturing', 'Game Dev']
---

Découvrez comment passer de simples aplats de couleurs à des matériaux réalistes en intégrant des textures complexes dans Unreal Engine 4.

{{< youtube-rgpd "lvTc4i7PA3M" >}}

### Résumé des notions clés

Dans ce tutoriel, nous explorons l'utilisation des textures pour enrichir le rendu visuel de vos objets 3D. Voici les points essentiels abordés :

*   **Base Color (Albedo) :** La texture qui définit la couleur réelle et les motifs visuels de votre matériau.
*   **Normal Map (NRM) :** Une carte indispensable pour simuler du relief et des détails géométriques complexes sans augmenter le nombre de polygones, en manipulant la manière dont la lumière rebondit sur la surface.
*   **Roughness (RGH) :** Une carte en niveaux de gris qui définit la rugosité de la surface. Elle permet de varier la brillance et la réflexion de la lumière sur différentes zones de l'objet.
*   **Workflow dans l'éditeur :**
    *   Utilisation du nœud `Texture Sample` pour importer vos fichiers.
    *   Importance de bien configurer le `Sampler Type` (notamment en mode "Normal" pour les Normal Maps).
    *   Utilisation du raccourci `Ctrl + W` pour dupliquer rapidement vos nœuds.
    *   Application des textures aux entrées correspondantes du nœud principal du matériau.

### Ce qui reste d'actualité aujourd'hui

Bien que ce tutoriel utilise Unreal Engine 4, les principes fondamentaux du "PBR" (Physically Based Rendering) restent identiques dans Unreal Engine 5. La gestion des textures, la compréhension des cartes de normales et la manipulation des paramètres de rugosité sont des compétences universelles. Que vous travailliez sur UE4 ou UE5, la logique de connexion des nœuds dans l'éditeur de matériaux (Material Editor) demeure le standard de l'industrie pour créer des surfaces crédibles. Maîtriser ces bases est une étape incontournable pour tout développeur souhaitant passer à des systèmes plus avancés comme les *Material Instances* ou les *Layered Materials*.

{{< footer >}}
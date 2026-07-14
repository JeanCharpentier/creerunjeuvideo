---
title: "7. Maîtriser le tiling des textures"
weight: 7
prev_url: "/unreal-engine-4/creer-ses-matériaux/creer-materiau-eau-dynamique-unreal-engine/"
next_url: "/unreal-engine-4/creer-ses-matériaux/creer-materiau-terrain-adaptatif-unreal-engine-4/"
date: 2023-10-27
categories: ['Archive']
tags: ['Unreal Engine 4', 'Material Editor', 'Texturing', 'Game Dev']
images: ["https://img.youtube.com/vi/4_1kVUWbLfo/maxresdefault.jpg"]
---

Apprenez à contrôler dynamiquement la répétition de vos textures sur vos modèles 3D grâce au Material Editor d'Unreal Engine 4.

{{< youtube-rgpd "4_1kVUWbLfo" >}}

### Résumé des notions clés

Dans ce tutoriel, nous explorons comment manipuler les coordonnées UV pour ajuster le "tiling" (la répétition) de vos textures :

*   **Texture Coordinate (TexCoord) :** Le nœud de base qui définit comment la texture est plaquée sur la géométrie.
*   **Multiplication des coordonnées :** Utiliser un nœud `Multiply` pour multiplier les coordonnées UV par une valeur scalaire afin de répéter la texture.
*   **Scalar Parameter :** Remplacer les valeurs fixes par des paramètres pour modifier la taille de la texture à la volée, idéal pour les Material Instances.
*   **Append Vector :** Une technique avancée pour séparer le contrôle des répétitions sur l'axe X et l'axe Y, permettant d'étirer ou d'ajuster la texture indépendamment sur chaque dimension.
*   **Application pratique :** L'importance de cette technique pour les grands objets ou les terrains, où une texture unique peut paraître trop étirée ou peu détaillée.

### Ce qui reste d'actualité aujourd'hui

Bien que ce tutoriel soit basé sur Unreal Engine 4, les principes fondamentaux du Material Editor restent identiques dans Unreal Engine 5. La manipulation des coordonnées UV via des paramètres scalaires est une compétence indispensable pour tout artiste technique. Que vous travailliez sur des matériaux complexes ou des systèmes de shaders procéduraux, la capacité à contrôler le tiling de manière dynamique permet d'optimiser le rendu visuel sans avoir à modifier les UV dans un logiciel de modélisation externe (comme Blender ou Maya). C'est une méthode efficace pour garantir une densité de texels cohérente sur l'ensemble de vos environnements.

{{< footer >}}
---
title: "30. Création d''ambiance : Éclairage et Post-Process"
weight: 30
date: 2026-06-17
categories: ['Tutoriels Unreal Engine 4']
tags: ['Unreal Engine 4', 'Lighting', 'Post-Process', 'Game Design', 'Ambiance']
images: ["https://img.youtube.com/vi/zgIIyTFOatM/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/zgIIyTFOatM/maxresdefault.jpg"]
---

Dans cet avant-dernier épisode de notre série dédiée au développement d'un jeu de type "Slender", nous allons transformer l'aspect visuel de notre niveau. Passer d'une scène éclairée par le soleil à une ambiance nocturne immersive demande de maîtriser deux outils fondamentaux : le **Lightmass Importance Volume** pour le calcul des lumières et le **Post-Process Volume** pour la colorimétrie et les effets de rendu.

{{< youtube-rgpd "zgIIyTFOatM" >}}

### Résumé des étapes clés
*   **Configuration des volumes :** Ajustement du *Lightmass Importance Volume* et du *Post-Process Volume* pour couvrir l'intégralité de la zone de jeu.
*   **Ajout de sources lumineuses :** Placement de *Point Lights* sur les éléments du décor (feux de camp, torches) avec réglage de l'intensité, de la portée (attenuation radius) et de la couleur.
*   **Passage en mode nuit :** Modification du *SkySphere Blueprint* (désactivation de la lumière directionnelle, ajustement de la hauteur du soleil et des étoiles) et de la *Directional Light* pour simuler une lumière lunaire.
*   **Post-Processing :** Application d'une teinte bleue nuit, ajustement du contraste, ajout d'un effet de vignetage et de *Fringe Intensity* pour renforcer l'immersion.
*   **Calcul des lumières :** Lancement du *Build Lighting* pour finaliser le rendu statique de la scène.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes d'Unreal Engine (UE5) aient introduit le système *Lumen* pour l'éclairage dynamique global, les principes abordés ici restent essentiels pour plusieurs raisons :
*   **Optimisation :** Le *Lightmass* (et le *Baking* de lumière) reste une technique incontournable pour les projets ciblant les plateformes mobiles ou les configurations matérielles modestes.
*   **Direction Artistique :** Le *Post-Process Volume* demeure l'outil principal pour définir "l'identité visuelle" d'un jeu, quel que soit le moteur utilisé.
*   **Organisation :** La gestion des dossiers dans le *World Outliner* et le regroupement des acteurs (feux, lumières, objets) sont des bonnes pratiques de GameDev qui facilitent grandement la maintenance de projets complexes.
*   **Workflow :** La logique de "découpage" d'un environnement en zones d'influence lumineuse est une compétence fondamentale pour tout environnement artist.

{{< footer >}}
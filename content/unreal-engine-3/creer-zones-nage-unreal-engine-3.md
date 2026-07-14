---
title: "Créer des zones de nage et des effets de profondeur dans Unreal Engine 3"
date: 2026-06-17
categories: ['GameDev']
tags: ['Unreal Engine 3', 'Level Design', 'Tutoriel', 'Water Volume']
images: ["https://img.youtube.com/vi/7rAZQXiKKCw/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/7rAZQXiKKCw/maxresdefault.jpg"]
---

Dans cet article, nous revenons sur les fondamentaux du level design sous **Unreal Engine 3 (UDK)**. Créer une surface liquide interactive ne se limite pas à poser une texture animée ; il s'agit de combiner des volumes physiques et des effets de post-traitement pour simuler l'immersion.

{{< youtube-rgpd "7rAZQXiKKCw" >}}

### Résumé de la procédure
Pour mettre en place une zone de nage fonctionnelle, voici les étapes clés à suivre dans l'éditeur :

*   **Création du bassin :** Utilisez une brosse additive pour le volume principal, puis une brosse soustractive pour creuser l'emplacement de la piscine.
*   **Surface liquide :** Ajoutez un `FluidSurfaceActor` depuis le Content Browser, ajustez ses dimensions pour qu'il s'insère parfaitement dans le bassin et appliquez un matériau de type "Water".
*   **Physique de nage :** Placez un `UTWaterVolume` au niveau de la surface pour définir la zone où le joueur peut nager.
*   **Immersion visuelle :** Ajoutez un `PostProcessVolume` pour simuler le flou (Depth of Field) et réduire la visibilité sous l'eau, rendant l'expérience plus réaliste.
*   **Gestion des calques :** Utilisez l'onglet "Scene" du Content Browser pour sélectionner facilement les volumes superposés (WaterVolume et PostProcess) afin de modifier leurs propriétés respectives.

### Ce qui reste d'actualité aujourd'hui

Bien que l'Unreal Engine 3 soit désormais un moteur "legacy", les concepts abordés ici restent des piliers du développement de jeux vidéo modernes :

1.  **La séparation entre visuel et logique :** Comme dans UE5, le rendu (le matériau d'eau) est distinct de la logique physique (le volume de collision). Comprendre cette séparation est essentiel pour tout développeur.
2.  **Le Post-Processing :** L'utilisation de volumes de post-traitement pour simuler des environnements (sous l'eau, brouillard, vision thermique) est toujours la méthode standard dans les moteurs actuels.
3.  **L'importance du "Build" :** La nécessité de reconstruire la géométrie et l'éclairage après des modifications structurelles reste une étape incontournable pour assurer la cohérence du rendu final, même si les technologies de *Lumen* ou *Nanite* ont grandement automatisé ces processus.

{{< footer >}}
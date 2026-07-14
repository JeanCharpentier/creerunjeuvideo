---
title: "2. Création de textures rétro pour votre FPS"
weight: 2
date: 2026-06-17
categories: ['Raycasting GameMaker']
tags: ['GameMaker', 'Raycasting', 'Pixel Art', 'Texturing', 'FPS']
images: ["https://img.youtube.com/vi/mOPD0_ErDdc/maxresdefault.jpg"]
---

Bienvenue dans ce deuxième épisode de notre série dédiée à la création d'un FPS de type "Doom-like" avec le moteur de Raycasting GameMaker. Aujourd'hui, nous délaissons temporairement le code pour nous concentrer sur l'aspect visuel : la création de vos propres textures.

{{< youtube-rgpd "mOPD0_ErDdc" >}}

### Au programme de cet épisode :
*   **Configuration technique :** Pourquoi privilégier des textures en 32x32 pixels plutôt que de la haute résolution.
*   **Workflow Paint.net :** Utilisation des outils de base pour créer des briques, gérer les décalages (offset) et créer des variations.
*   **Gestion des couleurs :** Utilisation des réglages de luminosité, contraste et saturation pour donner du relief à vos surfaces.
*   **Exportation :** Le format BMP 24 bits, standard indispensable pour la compatibilité avec le moteur.
*   **Variations :** Création rapide du sol et du plafond à partir de vos textures de murs existantes.

### Ce qui reste d'actualité aujourd'hui

Bien que les outils de création graphique aient évolué, les principes fondamentaux abordés ici restent cruciaux pour le développement de jeux "rétro" :

1.  **L'optimisation est reine :** Dans un moteur de raycasting, la mémoire vidéo est limitée. Utiliser des textures de petite taille (32x32 ou 64x64) permet non seulement de garder un look authentique, mais garantit surtout une fluidité parfaite, même sur des configurations modestes.
2.  **La répétabilité (Tiling) :** La technique du décalage des briques (une ligne sur deux) est la base pour éviter l'effet "grille" trop visible et rendre vos murs plus naturels.
3.  **La cohérence visuelle :** Utiliser les outils de réglage (Teinte/Saturation/Luminosité) pour décliner vos textures (sol, plafond, murs) permet de garder une unité graphique sans avoir à redessiner chaque élément de zéro.
4.  **Le format BMP :** Bien que le PNG soit devenu la norme, le format BMP reste souvent le plus simple à manipuler pour les moteurs de rendu bas niveau, car il ne nécessite pas de décompression complexe.

{{< footer >}}
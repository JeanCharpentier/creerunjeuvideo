---
title: "11. Préparation des animations et des sockets pour les armes"
weight: 11
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['FPS', 'Animation', 'Socket', 'GameDev']
images: ["https://img.youtube.com/vi/NFijPoJ9S3k/maxresdefault.jpg"]
---

Dans cet épisode, nous préparons les fondations nécessaires à l'intégration des armes dans notre FPS. Avant de pouvoir ramasser et équiper des objets, il est crucial de configurer correctement le squelette de notre personnage et d'ajouter des points d'ancrage précis.

{{< youtube-rgpd "NFijPoJ9S3k" >}}

### Résumé de la vidéo
*   **Mise à jour de l'Animation Blueprint :** Remplacement de l'animation par défaut par le pack "UE4 Animation Starter Pack" pour bénéficier d'animations de tir réalistes.
*   **Configuration du squelette :** Sélection du bon squelette (celui du starter pack) dans les paramètres du mesh pour assurer la compatibilité des animations.
*   **Création de Sockets :** Ajout d'un socket sur l'os de la main droite pour servir de point d'ancrage aux armes.
*   **Ajustement visuel :** Utilisation de l'outil "Preview Asset" pour positionner précisément l'arme (fusil d'assaut, pistolet) dans la main du personnage et vérifier la cohérence avec différentes animations (Idle, Fire, Iron Sight).

### Ce qui reste d'actualité aujourd'hui
Bien que cet article traite d'Unreal Engine 4, les concepts fondamentaux abordés restent parfaitement transposables aux versions plus récentes (UE5) :
*   **La hiérarchie des Sockets :** La méthode consistant à créer des points d'ancrage sur les os pour attacher des objets (armes, accessoires) est toujours la norme dans le développement de jeux 3D.
*   **Animation Blueprints :** La logique de gestion des états d'animation via le graphe reste le cœur du système d'animation d'Unreal.
*   **Le workflow de Preview :** Utiliser des assets de prévisualisation pour ajuster les transformations (rotation/translation) avant d'implémenter la logique de ramassage est une pratique indispensable pour gagner du temps et éviter les bugs visuels.
*   **Modularité :** La séparation entre le squelette, le mesh et les animations permet de changer facilement de style de personnage tout en conservant les mêmes mécaniques de jeu.

{{< footer >}}
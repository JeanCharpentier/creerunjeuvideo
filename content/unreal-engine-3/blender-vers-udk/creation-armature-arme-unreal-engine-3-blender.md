---
title: "4. Création et configuration de l''armature pour Unreal Engine 3"
weight: 4
date: 2026-06-17
categories: ['Tutoriels GameDev']
tags: ['Unreal Engine 3', 'Blender', 'Modélisation', 'Rigging', 'UDK']
images: ["https://img.youtube.com/vi/acoBgupzn2U/maxresdefault.jpg"]
---

Dans ce quatrième volet de notre série dédiée à l'intégration d'assets dans l'Unreal Engine 3 (UDK), nous allons aborder une étape cruciale : le **rigging** de votre arme. L'ajout d'une armature n'est pas seulement utile pour l'animation, c'est un prérequis indispensable pour que le moteur puisse manipuler votre modèle, notamment pour gérer des points d'attache spécifiques comme le *Muzzle Flash*.

{{< youtube-rgpd "acoBgupzn2U" >}}

### Résumé de l'épisode
*   **Préparation du pivot :** Ajustement du point d'origine de l'objet sur la poignée pour faciliter la manipulation dans l'UDK.
*   **Création de l'armature :** Ajout d'un os de base (*RL_Base*) et d'un os dédié aux effets visuels (*RL_Muzzle*).
*   **Hiérarchie :** Parentage des os avec l'option "Keep Offset" pour conserver la structure.
*   **Skinning manuel :** Utilisation de l'option "With Empty Groups" pour assigner les sommets (vertices) au groupe de vertex correspondant à l'os principal.
*   **Exportation FBX :** Configuration des paramètres d'export (échelle, orientation X-Forward, suppression des éléments inutiles) pour une compatibilité optimale avec l'UDK.

### Ce qui reste d'actualité aujourd'hui

Bien que l'Unreal Engine 3 (UDK) soit aujourd'hui considéré comme une technologie "legacy", les principes fondamentaux abordés dans ce tutoriel restent le socle de tout workflow moderne :

1.  **La structure Squeletal Mesh :** Même dans Unreal Engine 5, le concept de *Skeletal Mesh* avec des *Sockets* (l'équivalent moderne de nos os de Muzzle Flash) est la norme pour attacher des effets de particules ou des accessoires aux armes.
2.  **L'importance du point de pivot :** Une bonne pratique de modélisation consiste toujours à placer l'origine de l'objet à un point logique (poignée, centre de masse) pour simplifier le placement des objets dans le monde.
3.  **Gestion des unités et échelles :** Le problème de l'échelle lors de l'exportation est un classique. Comprendre comment appliquer un facteur d'échelle lors de l'exportation FBX permet d'éviter des heures de débogage dans le moteur de jeu.
4.  **Workflow non-destructif :** L'utilisation des *Vertex Groups* reste la méthode la plus propre pour contrôler précisément quelle partie de votre mesh doit suivre quel os, évitant ainsi les déformations automatiques parfois imprévisibles.

{{< footer >}}
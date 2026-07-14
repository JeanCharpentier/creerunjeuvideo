---
title: "6. Gestion des Lightmaps et correction d''éclairage"
weight: 6
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blender', 'Lightmap', 'UV Mapping', 'Lighting', 'Tutoriel']
images: ["https://img.youtube.com/vi/vi7d5aZh-7Y/maxresdefault.jpg"]
---

Dans cet épisode, nous abordons une étape cruciale pour la qualité visuelle de vos projets sous Unreal Engine 4 : la gestion des **Lightmaps**. Si vous avez importé vos modèles depuis Blender sans configuration spécifique, vous avez probablement remarqué des ombres étranges ou des artefacts lors du calcul de la lumière (le "Build").

{{< youtube-rgpd "vi7d5aZh-7Y" >}}

### Résumé de l'épisode
*   **Pourquoi les Lightmaps ?** Unreal Engine a besoin d'un canal UV dédié pour calculer correctement les ombres portées et les reflets sur vos objets statiques.
*   **La méthode Blender :** Utilisation de l'outil "Smart UV Project" pour générer automatiquement un dépliage UV propre.
*   **Double canal UV :** Création d'un premier canal pour les textures (à venir) et d'un second canal spécifiquement pour la Lightmap.
*   **Réimportation :** Mise à jour des assets via le clic droit "Reimport" dans l'éditeur Unreal.
*   **Optimisation :** Ajustement des paramètres "Lightmass" (Shadow indirect only) pour corriger les problèmes d'ombrage sur le terrain.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes d'Unreal Engine (UE5) aient introduit le système *Lumen* qui permet de se passer de Lightmaps dans de nombreux cas, la compréhension de ce workflow reste fondamentale pour :
1.  **L'optimisation mobile :** Les projets destinés aux plateformes mobiles utilisent toujours majoritairement le "Baked Lighting" (lumières précalculées).
2.  **La performance sur PC :** Pour les scènes très complexes, le précalcul des lumières reste une solution très efficace pour maintenir un framerate élevé.
3.  **La maîtrise technique :** Comprendre comment Unreal traite les UV et les canaux de lumière vous rendra bien plus autonome pour résoudre des problèmes de rendu, quel que soit le moteur utilisé.
4.  **Le workflow Blender/UE :** La technique du "Smart UV Project" demeure la méthode la plus rapide pour préparer des objets simples (props, environnement) avant leur intégration.

{{< footer >}}
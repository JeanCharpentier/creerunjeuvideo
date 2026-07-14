---
title: "10. Créer un matériau de verre translucide avancé"
weight: 10
prev_url: "/unreal-engine-4/creer-ses-matériaux/creer-materiau-glace-tessellation-unreal-engine/"
next_url: "/unreal-engine-4/creer-ses-matériaux/creer-effet-dissolution-dynamique-unreal-engine/"
date: 2023-10-27
categories: ['Archive']
tags: ['Unreal Engine 4', 'Material Editor', 'Game Dev', 'Shader']
images: ["https://img.youtube.com/vi/0xIro9WnwgM/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/0xIro9WnwgM/maxresdefault.jpg"]
---

Dans ce tutoriel, nous allons explorer la création d'un matériau de type "verre" (VR) évolué sous Unreal Engine 4, en intégrant des effets de réfraction, de flou et de transparence dynamique.

{{< youtube-rgpd "0xIro9WnwgM" >}}

### Résumé des notions clés

Pour obtenir un rendu de verre réaliste et personnalisable, nous avons structuré le Material Editor autour des points suivants :

*   **Mode de fusion (Blend Mode) :** Utilisation du mode *Translucent* pour permettre la transparence.
*   **Effet de flou (Blur) :** Utilisation du node `SpiralBlurSceneTexture` pour simuler un verre dépoli ou granuleux (type paroi de douche).
*   **Gestion de la couleur :** Utilisation d'un `Vector Parameter` relié à l'entrée *Emissive Color* pour une gestion flexible via les instances.
*   **Réalisme avec le Fresnel :** Utilisation du node *Fresnel* pour varier l'opacité et la réfraction selon l'angle de vue de la caméra.
*   **Interpolation linéaire (Lerp) :** Mise en place de `Linear Interpolate` pour piloter les transitions entre deux états de réfraction et d'opacité.
*   **Material Instances :** Création d'une instance de matériau pour modifier en temps réel les paramètres (couleur, intensité du flou, indices de réfraction) sans recompiler le shader.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions récentes d'Unreal Engine (UE5) aient introduit des systèmes comme *Lumen* ou le *Substrate Material Framework*, les concepts abordés ici restent fondamentaux pour tout développeur :

1.  **La puissance des Material Instances :** C'est toujours la méthode standard pour optimiser le workflow et permettre aux artistes de varier les propriétés d'un matériau sans multiplier les assets.
2.  **L'utilisation du Fresnel :** Ce node est indispensable pour simuler le comportement physique des surfaces transparentes ou réfléchissantes, un principe qui ne change pas avec les versions du moteur.
3.  **La logique de Shader :** Comprendre comment manipuler les entrées *Opacity*, *Refraction* et *Emissive* est la base pour créer n'importe quel matériau complexe, qu'il s'agisse de verre, d'eau ou de surfaces holographiques.
4.  **Optimisation :** La technique du `SpiralBlurSceneTexture` reste une astuce efficace pour créer des effets visuels coûteux en apparence, tout en gardant un contrôle total sur les performances via des paramètres scalaires.

{{< footer >}}
---
title: "9. Créer un matériau de glace réaliste avec la tessellation"
weight: 9
prev_url: "/unreal-engine-4/creer-ses-matériaux/creer-materiau-terrain-adaptatif-unreal-engine-4/"
next_url: "/unreal-engine-4/creer-ses-matériaux/creer-materiau-verre-translucide-unreal-engine/"
date: 2023-10-27
categories: ['Archive']
tags: ['Unreal Engine 4', 'Material Editor', 'Tessellation', 'Game Dev']
images: ["https://img.youtube.com/vi/tnTxZ8C4zHY/maxresdefault.jpg"]
---

Apprenez à concevoir un matériau de glace dynamique et visuellement riche en utilisant les outils avancés de l'éditeur de matériaux d'Unreal Engine 4, incluant la tessellation pour une déformation géométrique réelle.

{{< youtube-rgpd "tnTxZ8C4zHY" >}}

### Résumé des notions clés

Ce tutoriel explore les techniques fondamentales pour créer un shader de glace complexe :

*   **Gestion des couleurs (Lerp & Fresnel) :** Utilisation du nœud *Linear Interpolate* (Lerp) combiné à un effet *Fresnel* pour simuler les variations de teintes naturelles de la glace.
*   **Rugosité et Bruit :** Intégration d'un nœud *Noise* pour générer des variations aléatoires de brillance sur la surface.
*   **Normal Maps superposées :** Mélange de plusieurs textures de normales via une addition pour obtenir un relief plus profond et moins répétitif.
*   **Shading Model Subsurface :** Passage au modèle *Subsurface* pour simuler la pénétration de la lumière sous la surface de la glace.
*   **Tessellation (World Displacement) :** Introduction à la déformation géométrique du mesh. Utilisation du *Vertex Normal World Space* masqué pour cibler uniquement certaines zones (le bas du mesh) et créer des effets de coulées gelées.
*   **Optimisation :** Importance du découpage en groupes (touche 'C') et de l'utilisation de paramètres (Scalar/Vector Parameters) pour créer des instances de matériaux flexibles.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions récentes d'Unreal Engine (UE5) aient introduit le système **Nanite** et le **Virtual Shadow Mapping**, les concepts abordés ici restent des piliers du développement :

1.  **Logique de Shader :** La compréhension des nœuds *Lerp*, *Fresnel* et *Noise* est universelle. Ces outils sont toujours la base pour créer des matériaux procéduraux performants.
2.  **Workflow des Material Instances :** La pratique consistant à exposer des paramètres (couleurs, puissances, tailles) reste la méthode standard pour travailler efficacement en équipe et itérer rapidement sur le rendu visuel.
3.  **Compréhension des normales et du Subsurface :** Ces techniques de simulation de lumière sont toujours essentielles pour le rendu de matériaux organiques ou translucides, même avec les nouvelles technologies de rendu.
4.  **Limites géométriques :** Le rappel sur la densité des sommets (vertex count) pour la tessellation est une leçon cruciale : un effet de déformation ne sera jamais visible si le mesh de base est trop simple (ex: un cube de base). Cela reste vrai pour toute manipulation de vertex, qu'il s'agisse de tessellation classique ou de *World Position Offset*.

{{< footer >}}
---
title: "12. Création et sculpture de terrain avec Landscape"
weight: 12
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Landscape', 'Level Design', 'Sculpting', 'Tutoriel']
images: ["https://img.youtube.com/vi/Lhuy1UoudXI/maxresdefault.jpg"]
---

Dans cet épisode, nous passons à une étape cruciale pour donner vie à votre environnement : le remplacement du sol basique par un véritable terrain sculpté. L'outil **Landscape** d'Unreal Engine 4 est un système puissant qui permet de créer des reliefs complexes, des montagnes et des vallons, tout en gérant nativement les textures de sol.

{{< youtube-rgpd "Lhuy1UoudXI" >}}

### Résumé de la leçon
*   **Nettoyage de la scène :** Suppression de l'objet "Floor" par défaut pour laisser place au système Landscape.
*   **Configuration du Landscape :** Utilisation de l'éditeur dédié avec un réglage de *Section Size* (7x7 quads) pour une gestion optimisée des performances.
*   **Application des matériaux :** Assignation d'un matériau de type "Ground Gravel" pour habiller le terrain.
*   **Maîtrise des outils de sculpture :**
    *   **Sculpt :** Pour créer le relief (montagnes, collines).
    *   **Smooth :** Pour adoucir les polygones trop saillants.
    *   **Flatten :** Idéal pour créer des plateaux ou des chemins plats.
    *   **Erosion :** Pour simuler l'usure naturelle du sol.
    *   **Noise :** Pour ajouter un aspect chaotique et organique.
*   **Réglages de brosse :** Compréhension du *Brush Size* (taille) et du *Brush Falloff* (atténuation) pour sculpter avec précision.
*   **Gestion du LOD (Level of Detail) :** Observation du changement de résolution du terrain en fonction de la distance de la caméra.

### Ce qui reste d'actualité aujourd'hui
Bien que cet épisode se concentre sur Unreal Engine 4, les fondamentaux du **Landscape Editor** sont restés quasi identiques dans Unreal Engine 5. La logique de sculpture, l'utilisation des brosses et la gestion des matériaux de terrain (Landscape Layers) sont des compétences transversales. 

Le point de vigilance reste le **LOD (Level of Detail)** : si vous constatez des changements de résolution visibles lors de vos déplacements, sachez que dans les versions récentes, le système *Nanite pour Landscape* (introduit dans UE 5.1+) permet désormais de gérer des terrains d'une complexité géométrique extrême sans avoir à se soucier autant des transitions de LOD classiques. Cependant, pour un projet léger ou mobile, les techniques de sculpture manuelle abordées ici restent la méthode la plus performante.

{{< footer >}}
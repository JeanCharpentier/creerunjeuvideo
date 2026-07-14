---
title: "4. Créer des matériaux émissifs"
weight: 4
prev_url: "/unreal-engine-4/creer-ses-matériaux/maitriser-materiaux-dynamiques-instances-unreal-engine/"
next_url: "/unreal-engine-4/creer-ses-matériaux/maitriser-les-textures-dans-unreal-engine-4/"
date: 2023-10-27
categories: ['Archive']
tags: ['Unreal Engine 4', 'Materiaux', 'Shaders', 'Game Dev']
images: ["https://img.youtube.com/vi/4jYSXcoYZoM/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/4jYSXcoYZoM/maxresdefault.jpg"]
---

Découvrez comment donner vie à vos environnements en créant des matériaux capables d'émettre leur propre lumière, une technique essentielle pour simuler la lave, les néons ou les écrans.

{{< youtube-rgpd "4jYSXcoYZoM" >}}

### Résumé des notions clés

*   **Le canal Emissive Color :** Contrairement à la Base Color qui définit l'aspect visuel, le canal *Emissive* permet à une surface de briller par elle-même, sans nécessiter de source lumineuse externe.
*   **Vector Parameter :** Utilisé pour définir la couleur de base, il permet de créer des instances de matériaux facilement modifiables.
*   **Scalar Parameter :** Indispensable pour contrôler l'intensité de l'émission. En multipliant la couleur par une valeur scalaire, vous pouvez augmenter la puissance lumineuse au-delà de 1.
*   **Le nœud Multiply :** L'opération mathématique de base pour combiner votre couleur et votre valeur d'intensité (puissance) avant de les injecter dans le canal *Emissive Color*.
*   **Workflow efficace :** Utilisation des raccourcis clavier (touche 'V' pour Vector, touche 'S' pour Scalar) pour accélérer la création de vos graphiques de matériaux.

### Ce qui reste d'actualité aujourd'hui

Bien que ce tutoriel utilise Unreal Engine 4, les principes fondamentaux des matériaux émissifs restent identiques dans Unreal Engine 5. La logique de multiplication d'un paramètre scalaire avec une couleur pour piloter l'intensité lumineuse est une pratique standard dans l'industrie. Que vous travailliez sur du rendu temps réel ou sur des effets visuels (VFX), la maîtrise de ces nœuds est le socle indispensable pour créer des shaders complexes, comme des matériaux réactifs au *Bloom* ou des surfaces luminescentes dynamiques. Ces techniques sont toujours le moyen le plus performant pour ajouter du "punch" visuel à vos scènes sans alourdir le calcul des lumières dynamiques.

{{< footer >}}
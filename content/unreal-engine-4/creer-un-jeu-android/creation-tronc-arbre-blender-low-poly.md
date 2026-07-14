---
title: "7. Création et modélisation d''un tronc d''arbre dans Blender"
weight: 7
date: 2026-06-17
categories: ['GameDev']
tags: ['Blender', 'Modélisation', 'Low Poly', 'Tutoriel']
images: ["https://img.youtube.com/vi/vKQ96bAisPk/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/vKQ96bAisPk/maxresdefault.jpg"]
---

Dans cet épisode, nous abordons une étape cruciale de la création d'assets pour vos jeux vidéo : la modélisation d'un objet simple, ici un tronc d'arbre, en utilisant les outils de base de Blender. L'objectif est de comprendre le workflow "Low Poly" pour optimiser les performances de votre moteur de jeu.

{{< youtube-rgpd "vKQ96bAisPk" >}}

### Résumé de la manipulation
*   **Ajout d'objet :** Utilisation du raccourci `Shift + A` pour ajouter un cylindre.
*   **Optimisation :** Réduction du nombre de sommets (vertices) à 8 pour conserver un style Low Poly efficace.
*   **Transformations :** Utilisation des touches `R` (rotation), `S` (scale) et des contraintes d'axes (`X`, `Y`, `Z`) pour orienter et dimensionner le tronc.
*   **Mode Édition :** Passage en `Edit Mode` (`Tab`) pour ajouter des subdivisions (`Ctrl + R`) afin de permettre une déformation organique.
*   **Modificateurs :** Utilisation du modificateur `Displace` couplé à une texture `Wood` pour donner du relief au tronc.
*   **Nettoyage :** Utilisation de la sélection par boîte (`B`) et de la mise à l'échelle à zéro (`S + X + 0`) pour aplatir les extrémités du tronc.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions de Blender évoluent, les fondamentaux présentés ici restent le socle de toute modélisation 3D pour le jeu vidéo :
1.  **L'importance du Low Poly :** Dans le développement de jeux (notamment sur mobile ou VR), la gestion du nombre de polygones est toujours la priorité pour maintenir un framerate stable.
2.  **La maîtrise des raccourcis :** Apprendre les raccourcis clavier (`Shift+A`, `Tab`, `R`, `S`, `G`) est toujours le moyen le plus rapide pour travailler efficacement dans n'importe quelle version de Blender.
3.  **Le workflow non-destructif :** L'utilisation des modificateurs (comme `Displace`) permet de modifier la forme de base sans altérer définitivement la géométrie, une pratique indispensable pour itérer rapidement sur vos assets.
4.  **La rigueur des axes :** Travailler avec des contraintes d'axes (`X`, `Y`, `Z`) est une compétence universelle qui vous servira autant dans Blender que dans l'interface d'Unreal Engine 4 ou 5.

{{< footer >}}
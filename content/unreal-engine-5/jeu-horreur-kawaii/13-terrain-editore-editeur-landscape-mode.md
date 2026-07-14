---
title: "13. Création de paysages et peinture de textures (Landscape Mode)"
date: 2026-06-12
category: Archive
weight: 13
tags: [Unreal Engine 5, Kawaii Slender, Blueprint, Input System, Audio, Game Design]
prev_url: "/unreal-engine-5/jeu-horreur-kawaii/12-win-loose-gameover-ecran-fin-menu-widget"
next_url: "/unreal-engine-5/jeu-horreur-kawaii/14-foliage-editor-feuillage-arbres-nature-paysage"
images: ["https://img.youtube.com/vi/V34gCSVsgEk/maxresdefault.jpg"]
---

{{< youtube-rgpd "V34gCSVsgEk" >}}

Après avoir bouclé notre boucle de gameplay avec les conditions de victoire et de défaite, nous attaquons enfin la phase de **mapping**. Dans cet épisode, nous quittons la carte de test par défaut pour sculpter notre tout premier terrain 3D et apprendre à y peindre différentes textures (herbe, terre, roche) pour poser l'ambiance de notre Slender-like.

### Concepts clés abordés dans ce tutoriel

* **Initiation à l'éditeur de paysages (Landscape Mode) :**
    * Passage du mode *Select* au mode **Landscape** (`Shift + 2`) pour activer les outils de génération de terrain d'Unreal Engine 5.
    * Configuration et dimensionnement de la grille du terrain : gestion des sections, des composants et de la résolution globale avant la création.
* **Sculpture et modelage du relief :**
    * Utilisation de l'outil **Sculpt** pour surélever le terrain et dessiner des collines ou des barrières naturelles (montagnes) afin de délimiter la zone de jeu.
    * Utilisation de l'outil **Smooth** (Adoucissement) pour lisser les imperfections et les étirements trop abruptes des polygones, garantissant des pentes naturelles pour le joueur et l'IA.
* **Configuration d'un Matériau de Terrain (Landscape Material) :**
    * Importation et organisation des textures de sol (Albedo/Color, Normal Map).
    * Utilisation du nœud **Landscape Layer Blend** au sein de l'éditeur de matériau pour définir et nommer les différentes couches de peinture disponibles (ex: `Herbe`, `Terre`, `Roche`).
    * Application du matériau global sur l'acteur Landscape.
* **Peinture et gestion des couches (Layer Info) :**
    * Création indispensable des fichiers de données de couche (**Weight-Blended Layer Info**) pour chaque texture dans l'onglet *Paint*. Sans ces fichiers, le moteur ne peut pas enregistrer où les textures sont appliquées.
    * Utilisation des brosses de peinture pour appliquer dynamiquement la roche sur les falaises escarpées et la terre sur les chemins de randonnée.
* **Précautions techniques et flux de travail (Workflow) :**
    * Sensibilisation à la stabilité de l'éditeur lors de la manipulation des outils de Landscape (risques de crashs liés à la mémoire vidéo ou aux shaders).
    * Recommandation de sécurité : réaliser ses expérimentations graphiques et ses tests d'outils sur des cartes de brouillon dédiées afin de préserver la intégrité de la map principale du jeu.

### Ce qui reste d'actualité aujourd'hui

L'essentiel de la gestion des paysages dans cette archive pose des bases solides qui restent valables sur les versions récentes d'Unreal Engine 5 :

1. **L'architecture du Landscape Layer Blend :** Bien que les technologies de terrain se modernisent (comme l'usage des *Runtime Virtual Textures* ou de *PCG* pour le peuplement automatique), la logique de fusion par nœud *Layer Blend* et la création des *Layer Infos* restent la méthode universelle pour peindre manuellement un sol dans l'éditeur.
2. **Le besoin crucial de sauvegardes régulières :** La sculpture et la compilation des shaders de terrain à la volée restent des opérations lourdes pour le moteur. L'importance de sauvegarder fréquemment et de compartimenter ses tests sur des maps secondaires demeure une règle d'or pour tout Level Designer.
3. **Le blocage du joueur par le relief :** Utiliser la topologie du terrain (des montagnes escarpées) plutôt que des murs invisibles pour ceindre la zone de jeu reste une technique d'habillage et de Level Design classique, immersive et performante pour optimiser l'affichage de l'environnement.

---
{{< footer >}}
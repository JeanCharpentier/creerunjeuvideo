---
title: "14. Système de végétation (Foliage Mode) et optimisation des collisions"
date: 2026-06-12
category: Archive
weight: 14
tags: [Unreal Engine 5, Kawaii Slender, Blueprint, Input System, Audio, Game Design]
prev_url: "/unreal-engine-5/jeu-horreur-kawaii/13-terrain-editore-editeur-landscape-mode"
next_url: "/unreal-engine-5/jeu-horreur-kawaii/15-props-decor-lumiere-clignotte-lanterne-village"
images: ["https://img.youtube.com/vi/-I9-Q0RDq-0/maxresdefault.jpg"]
---

{{< youtube-rgpd "-I9-Q0RDq-0" >}}

Notre terrain 3D est désormais sculpté et peint, mais il manque cruellement de vie. Dans ce quatorzième épisode, nous transformons notre carte en une véritable forêt dense en utilisant les outils de peuplement de masse d'Unreal Engine 5. Nous verrons comment peindre de la végétation (arbres, buissons, cailloux) en quelques clics tout en appliquant des règles d'optimisation strictes pour préserver les performances du jeu.

### Concepts clés abordés dans ce tutoriel

* **Découverte du mode Végétation (Foliage Mode) :**
    * Passage en mode **Foliage** (`Shift + 3`) pour accéder aux outils de peinture d'instances de meshs 3D.
    * Importation des modèles Low-Poly (arbres, sapins, rochers) dans la palette de composants de végétation (*Foliage Types*).
* **Paramétrage et dispersion réaliste (Brush Settings) :**
    * Ajustement de la densité (*Density*) et du rayon de la brosse pour contrôler la concentration des éléments au mètre carré.
    * Configuration des variations d'échelle (*Scale X/Y/Z*) et de rotation aléatoire pour casser l'effet de répétition et donner un aspect organique et unique à chaque arbre ou rocher cloné.
* **Gestion et optimisation des collisions de masse :**
    * Analyse de l'impact des collisions complexes sur les performances du processeur (CPU) lorsque des milliers d'arbres sont présents sur la carte.
    * **Bonne pratique d'optimisation :** Duplication des *Foliage Types* pour séparer les éléments de décor en deux catégories :
        1. Les arbres accessibles, dotés de collisions simplifiées (*Block All*), avec lesquels le joueur et l'IA peuvent interagir physiquement.
        2. Les arbres de l'arrière-plan, situés derrière des volumes bloquants ou des barrières naturelles, configurés sur *No Collision* pour délester le moteur physique.
* **Intégration d'éléments aquatiques et résolution de bugs :**
    * Ajout de plans d'eau basiques pour habiller les zones basses du relief.
    * Identification et correction des bugs fréquents de superposition ou d'étirage de textures (gaps physiques) aux intersections entre les acteurs de feuillage et le maillage du terrain.

### Ce qui reste d'actualité aujourd'hui

L'usage du Foliage Mode reste une compétence technique fondamentale pour tout constructeur de monde sur Unreal Engine 5 :

1. **La puissance des instances (Instanced Static Meshes) :** Le mode Foliage repose sur l'instanciation de maillages. Contrairement à un simple copier-coller d'acteurs dans la scène, l'instanciation permet d'afficher des milliers de buissons et d'arbres en envoyant une seule commande de rendu (*Draw Call*) à la carte graphique. C'est le pilier de l'optimisation d'environnements ouverts.
2. **Le tri des collisions par zone :** Désactiver les collisions sur les éléments de décor inaccessibles ou lointains reste l'une des astuces de performance les plus efficaces et indispensables de l'industrie pour maintenir un taux de rafraîchissement (FPS) stable, particulièrement sur les configurations modestes ou les consoles portables.
3. **Le flux de travail hybride (Peinture vs Procédural) :** Si UE5 met en avant des outils de génération procédurale avancés (PCG - *Procedural Content Generation*), la maîtrise de la peinture manuelle via le Foliage Mode reste indispensable pour apporter des ajustements esthétiques précis, créer des sentiers propres ou peaufiner des zones de gameplay spécifiques.

---
{{< footer >}}
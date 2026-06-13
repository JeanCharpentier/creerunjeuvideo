---
title: "10. Animations et spatialisation sonore de l'IA (Blend Space 1D & Animation Blueprint)"
date: 2026-06-12
category: Archive
weight: 10
tags: [Unreal Engine 5, Kawaii Slender, Blueprint, Input System, Audio, Game Design]
prev_url: "/unreal-engine-5/jeu-horreur-kawaii/9-ai-perception-detection-vision-ecoute-suivre"
next_url: "/unreal-engine-5/jeu-horreur-kawaii/11-attaque-ennemie-ragdoll-physique-unreal"
---

{{< youtube-rgpd "7q4_2XAiKOo" >}}

Dans ce dixième volet de la série *Kawaii Slender*, nous passons à la phase de polissage visuel et sonore de notre antagoniste. Maintenant que notre poulet géant est capable de nous traquer logiquement grâce à son arbre de comportement, nous allons lui donner corps en synchronisant ses postures physiques (marche, course, repos) à sa vitesse réelle et en intégrant des bruitages spatialisés pour accentuer la tension dramatique.

### Concepts clés abordés dans ce tutoriel

* **Création et logique d'un Blend Space 1D :**
    * Utilisation de l'outil de fusion d'animations **Blend Space 1D** (`BS_Slender`) pour interpoler automatiquement les mouvements selon un seul axe de données.
    * Configuration de l'axe horizontal : paramétrage de la variable `Vitesse` sur une plage allant de `0.0` (immobile) à la vitesse maximale de course définie dans le composant *Character Movement* (ex: `600.0`).
    * Échantillonnage graphique : placement des poses d'animation (*Idle*, *Walk*, *Run*) aux points clés de l'axe pour assurer une transition visuelle fluide et sans coupure lorsque l'IA accélère ou décélère.
* **Architecture de l'Animation Blueprint (AnimBP) :**
    * Création d'un script d'animation dédié (`ABP_Slender`) combinant un graphique d'événements (*Event Graph*) et un graphique d'animation (*Anim Graph*).
    * **Calcul de la vitesse dans l'Event Graph :** Utilisation du node **Try Get Pawn Owner** pour valider l'existence de l'IA, extraction de son vecteur physique via **Get Velocity**, puis calcul de la longueur du vecteur à l'aide du node **Vector Length** (pour convertir la vélocité 3D en une valeur scalaire absolue).
    * Mise en cache de la donnée dans une variable float `Vitesse` locale.
    * **Alimentation de la pose dans l'Anim Graph :** Connexion du Blend Space 1D à la pose de sortie finale (*Output Pose*) en lui injectant en continu la variable `Vitesse` calculée.
* **Spatialisation Audio 3D (Sound Cue) :**
    * Création d'un conteneur sonore **Sound Cue** (`SC_Slender_Glousse`) regroupant plusieurs fichiers audio de gloussements pour éviter la répétition mécanique.
    * Utilisation des nodes internes **Random** (pour alterner aléatoirement les pistes) et **Modulator** (pour faire varier subtilement la hauteur du ton et le volume à chaque déclenchement).
    * Configuration de l'**Attenuation (Audio Spatiale)** : paramétrage des rayons de portée (*Inner Radius* pour la zone d'écoute à $100\%$ et *Falloff Distance* pour l'atténuation progressive) pour permettre au joueur de situer la créature à l'oreille dans l'espace 3D.
* **Déclenchement des sons via les composants :**
    * Ajout d'un composant **Audio** directement attaché au Mesh de l'IA pour diffuser les sons de fond en continu.
    * Utilisation alternative des fonctions de Blueprint comme **Play Sound 2D** ou **Play Sound at Location** selon que l'événement audio doit être global ou géolocalisé.

### Ce qui reste d'actualité aujourd'hui

Les principes fondamentaux de l'animation et de la gestion sonore traités dans cette vidéo restent la norme sur Unreal Engine 5 :

1. **La fusion d'animations par Blend Space :** Bien que l'outil de gestion des graphes d'animation ait évolué visuellement, le concept de calcul de la vitesse (*Vector Length* de la *Velocity*) pour piloter un *Blend Space* reste la méthode standard pour animer n'importe quel personnage ou créature qui se déplace.
2. **Le découplage de la logique d'animation :** L'utilisation de l'Animation Blueprint pour lire, stocker et appliquer les poses en fonction des données physiques du personnage (*Try Get Pawn Owner*) demeure le pilier central du système de character animation d'Unreal Engine.
3. **Le Sound Cue face à MetaSounds :** Bien qu'Unreal Engine 5 mette désormais en avant le système *MetaSounds* pour la génération audio procédurale, l'architecture classique des *Sound Cues* associés aux profils d'atténuation 3D reste une méthode extrêmement légère, robuste et rapide pour spatialiser des sons d'ambiance et des bruitages de monstres.

---
{{< footer >}}
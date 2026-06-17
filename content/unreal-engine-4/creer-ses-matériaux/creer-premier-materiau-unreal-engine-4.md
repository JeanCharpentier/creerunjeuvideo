---
title: "2. Les bases"
weight: 2
prev_url: "/unreal-engine-4/creer-ses-matériaux/demarrer-creation-materiaux-unreal-engine-4/"
next_url: "/unreal-engine-4/creer-ses-matériaux/maitriser-materiaux-dynamiques-instances-unreal-engine/"
date: 2023-10-27
categories: ['Archive']
tags: ['Unreal Engine 4', 'Game Development', 'Materiaux', 'Tutoriel']
---

Apprendre à manipuler l'éditeur de matériaux d'Unreal Engine 4 est une étape fondamentale pour tout développeur souhaitant donner vie à ses environnements 3D. Dans ce guide, nous explorons les bases de la création de matériaux, de la gestion des couleurs aux propriétés physiques de surface.

{{< youtube-rgpd "QxSCXKtpvY4" >}}

### Résumé des notions clés

La création de matériaux dans Unreal Engine 4 repose sur l'utilisation de l'éditeur de matériaux (Material Editor). Voici les points essentiels à retenir :

*   **Organisation et nommage :** Adoptez une nomenclature rigoureuse (ex: `Mat_NomDuMateriau`) pour maintenir votre projet propre et structuré.
*   **Interface de l'éditeur :**
    *   **Palette :** Contient toutes les fonctions et nodes disponibles.
    *   **Fenêtre centrale :** Espace de travail pour connecter vos nodes.
    *   **Aperçu (Viewport) :** Permet de visualiser le rendu sur différentes formes (sphère, cube, plan).
    *   **Détails :** Permet de configurer le *Blend Mode* (Opaque, Translucent, etc.) et les options d'illumination.
*   **Propriétés fondamentales :**
    *   **Base Color :** Définit la couleur diffuse de l'objet.
    *   **Metallic :** Détermine si la surface se comporte comme un métal (1) ou un diélectrique (0).
    *   **Roughness :** Gère la "rugosité" ou la dureté de la réflexion (0 = miroir parfait, 1 = surface mate).
*   **Nodes essentiels :**
    *   **Vector Parameter :** Utilisé pour définir une couleur (et idéal pour les instances de matériaux).
    *   **Constant :** Valeur numérique fixe (0 à 1) pour contrôler les propriétés physiques comme le métallique ou la rugosité.
*   **Two-Sided :** Une option cruciale dans les détails si vous souhaitez que votre matériau soit visible des deux côtés d'un plan.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions récentes d'Unreal Engine (UE5) aient introduit des fonctionnalités avancées comme le *Lumen* ou le *Nanite*, les principes fondamentaux abordés ici restent le socle du développement :

1.  **Le workflow PBR (Physically Based Rendering) :** Le système de *Base Color*, *Metallic* et *Roughness* est toujours le standard industriel pour créer des matériaux réalistes.
2.  **L'importance des paramètres :** L'utilisation de *Vector Parameters* au lieu de constantes simples est une pratique toujours recommandée pour créer des "Material Instances", permettant de varier l'apparence de vos objets sans multiplier les fichiers de matériaux.
3.  **La structure de l'éditeur :** L'interface de l'éditeur de matériaux n'a que très peu changé. Maîtriser ces bases dans UE4 vous permet d'être immédiatement opérationnel dans les versions les plus récentes du moteur.

{{< footer >}}
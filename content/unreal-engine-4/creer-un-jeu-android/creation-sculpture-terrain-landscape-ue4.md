---
title: "25. Création et sculpture de terrain avec l''outil Landscape"
weight: 25
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Landscape', 'Level Design', 'Sculpting', 'UE4']
images: ["https://img.youtube.com/vi/3mW86Soez9g/maxresdefault.jpg"]
---

Dans cet épisode, nous abordons une étape cruciale pour donner vie à vos environnements : l'utilisation de l'outil **Landscape** dans Unreal Engine 4. Fini les plateaux vides, nous allons apprendre à générer un terrain, le dimensionner correctement et utiliser les outils de sculpture pour créer du relief.

{{< youtube-rgpd "3mW86Soez9g" >}}

### Résumé de la manipulation
*   **Initialisation :** Accès à l'outil *Landscape* et configuration de la taille (sections et composants) pour éviter de générer un terrain trop lourd inutilement.
*   **Positionnement :** Ajustement de la hauteur du terrain par rapport au sol existant (utilisation de la vue latérale recommandée).
*   **Sculpture (Sculpt Mode) :** Utilisation des outils de base pour modifier la topographie :
    *   **Sculpt :** Pour monter (clic gauche) ou creuser (Shift + clic gauche).
    *   **Smooth :** Pour adoucir les angles et rendre le relief plus naturel.
    *   **Flatten :** Pour créer des zones planes.
    *   **Ramp :** Pour créer des chemins d'accès fluides.
*   **Gestion des ressources :** Importance de sauvegarder régulièrement (*Save All*) avant de sculpter, car ces opérations sont gourmandes en ressources.
*   **LOD (Level of Detail) :** Explication sur la gestion automatique de la géométrie en fonction de la distance pour optimiser les performances.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes d'Unreal Engine (UE5) aient introduit des outils comme le *Landscape Edit Layers* ou le *Nanite pour Landscape*, les fondamentaux présentés ici restent le socle de tout level design :
1.  **La gestion de la résolution :** Comprendre le ratio sections/composants est toujours indispensable pour maintenir un projet performant.
2.  **L'ergonomie de travail :** L'utilisation des brosses, de la force (*Tool Strength*) et du *Falloff* est identique dans toutes les versions du moteur.
3.  **Le workflow de sculpture :** La logique de "sculpter puis lisser" demeure la méthode la plus efficace pour obtenir des paysages crédibles sans avoir recours à des outils externes complexes.
4.  **L'optimisation :** La règle d'or de sauvegarder avant de manipuler des outils de terrain complexes est une habitude de développeur qui ne se démodera jamais.

{{< footer >}}
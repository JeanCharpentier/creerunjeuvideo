---
title: "43. Créer une lumière scintillante dynamique"
weight: 43
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprint', 'Lumières', 'GameDev', 'Tutoriel']
images: ["https://img.youtube.com/vi/sGnHP5k2RbU/maxresdefault.jpg"]
---

Dans cet épisode, nous terminons notre chapitre bonus consacré aux lumières en apprenant à créer un effet de "lumière scintillante". Grâce aux Blueprints, nous allons automatiser le changement d'intensité et de couleur d'une source lumineuse pour donner vie à nos environnements.

{{< youtube-rgpd "sGnHP5k2RbU" >}}

### Résumé de la manipulation
Pour réaliser cet effet, nous suivons ces étapes clés dans l'éditeur :
*   **Création de l'acteur :** Création d'un nouveau Blueprint de type `Actor` nommé `BP_Lumiere`.
*   **Ajout du composant :** Insertion d'un composant `Point Light` dans le Blueprint.
*   **Logique dans l'Event Graph :**
    *   Utilisation de l'événement `Event Tick` couplé à un `Delay` (0.2s) pour définir la fréquence de rafraîchissement.
    *   Utilisation du node `Set Intensity` pour varier la puissance lumineuse avec un `Random Float in Range` (0 à 8000).
    *   Ajout du node `Set Light Color` couplé à un `Make Linear Color` pour randomiser les composantes RVB (Rouge, Vert, Bleu) et créer un effet de changement de couleur dynamique.
*   **Flexibilité :** Possibilité d'attacher ce système à d'autres objets ou même au personnage (pour simuler une lampe torche).

### Ce qui reste d'actualité aujourd'hui
Bien que cet épisode utilise Unreal Engine 4, les principes fondamentaux restent parfaitement valables dans les versions récentes (UE5) :
*   **La puissance des Blueprints :** La logique de modification des propriétés des composants via les nodes `Set` reste la méthode standard pour créer des interactions dynamiques simples.
*   **L'Event Tick :** Bien que l'utilisation du `Tick` soit à surveiller pour les performances sur des systèmes complexes, il demeure l'outil idéal pour des effets visuels rapides et légers comme celui-ci.
*   **Modularité :** La capacité d'exposer des variables (comme l'intensité min/max) dans le Blueprint permet de réutiliser cet acteur dans n'importe quel niveau sans avoir à modifier le code à chaque fois.
*   **Propriétés des composants :** La méthode consistant à inspecter le panneau "Details" d'un composant pour identifier les nodes `Set` correspondants est une compétence essentielle pour tout développeur Unreal.

{{< footer >}}
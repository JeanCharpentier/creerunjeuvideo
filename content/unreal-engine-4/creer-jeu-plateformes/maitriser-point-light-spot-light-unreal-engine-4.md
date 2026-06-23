---
title: "41. Maîtriser les sources lumineuses : Point Light et Spot Light"
weight: 41
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Lumière', 'Lighting', 'GameDev', 'Tutoriel']
---

Dans cet épisode, nous explorons les outils fondamentaux de l'éclairage dans Unreal Engine 4. Après avoir appréhendé la *Directional Light* (simulant le soleil), il est temps de passer aux sources de lumière localisées : la *Point Light* et la *Spot Light*. Comprendre comment ces sources interagissent avec votre environnement est crucial pour donner du volume, de la profondeur et une ambiance unique à vos scènes.

{{< youtube-rgpd "tLiIPC17bN0" >}}

### Résumé des points clés
*   **Point Light :** Une source de lumière omnidirectionnelle qui diffuse dans toutes les directions à partir d'un point central. Idéale pour simuler des ampoules, des bougies ou des feux.
*   **Réglages de la Point Light :** Vous pouvez ajuster l'intensité, la couleur et surtout l' *Attenuation Radius* pour contrôler la portée et la concentration de la lumière.
*   **Spot Light :** Une source de lumière directionnelle limitée par un cône. Elle permet de cibler précisément des zones ou des objets spécifiques sans éclairer le reste de la scène.
*   **Réglages de la Spot Light :** En plus des paramètres classiques, vous pouvez modifier l' *Outer Cone Angle* pour élargir ou resserrer le faisceau lumineux.
*   **Expérimentation :** N'hésitez pas à créer un projet de test pour manipuler ces paramètres et observer les changements en temps réel.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions récentes d'Unreal Engine (UE5+) aient introduit le système *Lumen* pour une gestion dynamique de la lumière globale, les bases de l'éclairage restent identiques. La gestion des *Point Lights* et *Spot Lights* demeure le socle indispensable pour :
*   **Le "Level Design" narratif :** Guider le regard du joueur vers des points d'intérêt grâce à des spots.
*   **L'optimisation :** Savoir utiliser des lumières statiques ou mobiles reste essentiel pour maintenir un framerate stable, même avec les nouvelles technologies.
*   **La création de Blueprints :** La logique de placer une source lumineuse dans un composant (comme un gyrophare ou une lampe torche) est une compétence fondamentale qui n'a pas changé depuis l'UE4.

{{< footer >}}
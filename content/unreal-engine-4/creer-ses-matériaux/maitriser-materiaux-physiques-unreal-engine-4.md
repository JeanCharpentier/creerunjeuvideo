---
title: "18. Maîtriser les matériaux physiques"
weight: 18
prev_url: "/unreal-engine-4/creer-ses-matériaux/integrer-video-objet-unreal-engine-4/"
next_url: "/unreal-engine-4/creer-ses-matériaux/maitriser-les-masques-et-linear-interpolate-unreal-engine/"
date: 2023-10-27
categories: ['Archive']
tags: ['Unreal Engine 4', 'Game Development', 'Physics', 'Tutoriel']
images: ["https://img.youtube.com/vi/cJ9ijl3BhKc/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/cJ9ijl3BhKc/maxresdefault.jpg"]
---

Les matériaux physiques sont des outils indispensables pour donner du caractère à vos objets : découvrez comment simuler des comportements réalistes comme le rebond ou la glisse dans Unreal Engine 4.

{{< youtube-rgpd "cJ9ijl3BhKc" >}}

### Résumé des notions clés

Pour manipuler la physique de vos objets, voici les concepts essentiels à retenir :

*   **Rôle des Physical Materials :** Contrairement aux matériaux visuels, ils ne modifient pas l'apparence (couleur, texture) mais uniquement les propriétés physiques (friction, rebond, densité).
*   **Paramètres fondamentaux :**
    *   **Friction :** Définit l'accroche de l'objet. Proche de 0, l'objet glisse ; plus la valeur est élevée, plus il est "freiné".
    *   **Restitution :** Gère le facteur de rebondissement (bounciness). Une valeur de 1 signifie un rebond parfait sans perte d'énergie.
    *   **Density :** Influence la masse de l'objet en fonction de son volume.
*   **Combine Modes :** Permet de définir comment deux objets interagissent lors d'une collision (Average, Min, Max, Multiply). L'option "Override" est cruciale pour forcer un comportement spécifique.
*   **Surface Types :** Utilisables via les *Project Settings*, ils permettent de catégoriser vos matériaux (ex: glace, caoutchouc) pour déclencher des effets logiques (sons, particules) via les Blueprints.
*   **Application :** Vous pouvez assigner un matériau physique directement dans l'éditeur de matériau (Material Editor) ou via l'onglet "Collision" dans les détails d'un acteur spécifique.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions récentes d'Unreal Engine (UE5) aient introduit le système *Chaos Physics*, les principes fondamentaux expliqués ici restent parfaitement valides. La gestion des matériaux physiques demeure la méthode standard pour définir le comportement dynamique des objets. La compréhension des modes de combinaison (Min/Max/Average) et de la restitution est toujours le socle nécessaire pour créer des interactions cohérentes, que vous travailliez sur un jeu de plateforme, un simulateur de conduite ou un jeu de tir. Maîtriser ces réglages vous évitera bien des comportements erratiques dans vos simulations physiques.

{{< footer >}}
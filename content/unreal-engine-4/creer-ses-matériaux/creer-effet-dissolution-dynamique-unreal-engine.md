---
title: "11. Créer un effet de dissolution dynamique"
weight: 11
prev_url: "/unreal-engine-4/creer-ses-matériaux/creer-materiau-verre-translucide-unreal-engine/"
next_url: "/unreal-engine-4/creer-ses-matériaux/creer-materiau-lave-dynamique-unreal-engine/"
date: 2024-05-22
categories: ['Archive']
tags: ['Unreal Engine 4', 'Game Development', 'Materials', 'Blueprints', 'Tutoriel']
images: ["https://img.youtube.com/vi/y8L14ztyLw8/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/y8L14ztyLw8/maxresdefault.jpg"]
---

Apprenez à manipuler les propriétés de vos matériaux en temps réel pour créer des effets visuels saisissants, comme la disparition progressive d'un objet, grâce aux instances de matériaux dynamiques et aux Blueprints.

{{< youtube-rgpd "y8L14ztyLw8" >}}

### Résumé des notions clés

Ce tutoriel vous guide à travers la création d'un système de "dissolve" (dissolution) complet :

*   **Création du Matériau :** Utilisation de *Scalar Parameters* pour contrôler la quantité de dissolution et la répartition de l'effet néon.
*   **Logique Mathématique :** Emploi des nœuds `IF` pour comparer les valeurs de texture et créer un masque d'opacité dynamique.
*   **Configuration du Blend Mode :** Passage du mode *Opaque* au mode *Masked* pour permettre la transparence.
*   **Instances Dynamiques :** Utilisation du nœud `Create Dynamic Material Instance` dans le Blueprint pour modifier les propriétés du matériau au *runtime*.
*   **Animation via Timeline :** Mise en place d'une `Timeline` pour interpoler les valeurs de dissolution de 0 à 1 sur une durée définie.
*   **Interactivité :** Gestion des entrées clavier pour déclencher l'apparition et la disparition des objets, avec l'option `Auto Receive Input` activée.

### Ce qui reste d'actualité aujourd'hui

Bien que ce tutoriel utilise Unreal Engine 4, les concepts fondamentaux restent le pilier du développement visuel dans les versions plus récentes (UE5) :

1.  **Material Instances :** La séparation entre le matériau maître et ses instances reste la méthode la plus optimisée pour gérer les variations visuelles sans multiplier les ressources.
2.  **Dynamic Material Instances :** La capacité de modifier les paramètres d'un matériau via Blueprint au cours d'une partie est toujours indispensable pour le gameplay (effets de dégâts, changements d'état, transitions).
3.  **Le système de masquage :** La logique de `Opacity Mask` est toujours la norme pour gérer les objets qui doivent disparaître ou être découpés dynamiquement.
4.  **Timelines :** Elles demeurent l'outil privilégié pour créer des animations simples et fluides directement dans les Blueprints sans avoir recours à des séquences complexes.

{{< footer >}}
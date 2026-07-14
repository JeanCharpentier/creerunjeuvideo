---
title: "15. Habillage du décor (Props) et création d'une lumière de lanterne vacillante"
date: 2026-06-12
category: Archive
weight: 15
tags: [Unreal Engine 5, Kawaii Slender, Blueprint, Input System, Audio, Game Design]
prev_url: "/unreal-engine-5/jeu-horreur-kawaii/14-foliage-editor-feuillage-arbres-nature-paysage"
next_url: "/unreal-engine-5/jeu-horreur-kawaii/16-menu-principal-optimisations-export-packaging-build"
images: ["https://img.youtube.com/vi/eEt9MyDXO30/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/eEt9MyDXO30/maxresdefault.jpg"]
---

{{< youtube-rgpd "eEt9MyDXO30" >}}

Notre forêt est désormais dense et bien plantée, mais pour renforcer l'ambiance de notre Slender-like nocturne, il est temps d'y ajouter des points d'intérêt narratifs. Dans cet avant-dernier épisode de la série, nous allons habiller notre niveau avec des structures en bois (cabanes, ponts, barrières) et concevoir de A à Z une lanterne atmosphérique dotée d'une flamme vacillante et entourée de petits insectes nocturnes.

### Concepts clés abordés dans ce tutoriel

* **Habillage du décor et Level Design (Props placement) :**
    * Importation et disposition d'éléments modulaires en Low-Poly (cabanes, barrières, puits) pour rompre la monotonie de la forêt et créer des repères visuels pour le joueur.
    * Structuration de la carte en plaçant des obstacles logiques pour guider subtilement l'exploration et la traque du monstre.
* **Création d'une lumière vacillante réaliste (Flickering Light) :**
    * Intégration d'une source lumineuse de type **Point Light** de couleur chaude (orangée) au centre d'un mesh de lanterne.
    * Implémentation du vacillement dans le Blueprint via l'événement **Event Tick** ou l'utilisation d'une **Timeline** : application d'une fonction mathématique (génération de valeurs aléatoires fluctuantes) pour faire varier dynamiquement l'intensité lumineuse et simuler l'effet d'une vraie flamme de bougie.
* **Effets de particules d'ambiance (Niagara / Cascade) :**
    * Intégration d'un système de micro-particules pour simuler des lucioles ou des moucherons attirés par la chaleur et la lumière de la lanterne.
    * Configuration du comportement des particules : vélocité aléatoire et déplacements orbitaux erratiques autour du point chaud de la lumière.
* **Matériaux émissifs pour les sources de lumière :**
    * Création d'un matériau personnalisé appliqué sur le mesh de la vitre ou de la flamme de la lanterne.
    * Utilisation du paramètre **Emissive Color** multiplicateur pour donner l'illusion physique que l'objet produit lui-même de la lumière à l'écran, indépendamment de l'éclairage global de la scène.
* **Gestion de l'ambiance nocturne et précautions techniques :**
    * Bascule et ajustement du cycle de lumière vers une nuit profonde pour valider le contraste et la portée de nos nouvelles sources d'éclairage localisées.
    * Recommandation de sécurité : rappel de l'importance cruciale de sauvegarder régulièrement son travail et de réaliser des copies de sauvegarde (*backups*) du projet avant d'attaquer les dernières phases d'optimisation.

### Ce qui reste d'actualité aujourd'hui

Les mécaniques d'habillage et d'éclairage dynamique présentées dans cette archive demeurent d'excellents standards de production sur Unreal Engine 5 :

1. **La puissance de l'émissif couplée à Lumen :** Sous Unreal Engine 5, l'utilisation de matériaux émissifs combinée au système d'illumination globale en temps réel **Lumen** prend une toute autre dimension. Un objet émissif projette désormais naturellement de la vraie lumière sur le décor environnant sans nécessiter obligatoirement l'ajout d'une *Point Light* pour les petits objets.
2. **L'importance des variations de fréquences (Flicker) :** Utiliser des variations d'intensité lumineuse mathématiques pour briser la perfection du numérique reste la méthode n°1 pour donner de la vie et du cachet à une scène d'horreur ou d'exploration.
3. **L'habillage par la narration environnementale :** Placer des structures à des endroits clés de la carte pour attirer l'œil du joueur (comme des cabanes ou des lanternes) reste la règle d'or du Level Design pour structurer le rythme d'un jeu sans recourir à une mini-map ou à des flèches de guidage intrusives.

---
{{< footer >}}
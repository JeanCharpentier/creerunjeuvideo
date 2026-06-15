---
title: "15. Créer un système de récolte de ressources"
weight: 15
prev_url: "/intersect-engine/creer-un-mmorpg/creer-banque-fonctionnelle-intersect-engine/"
next_url: "/intersect-engine/creer-un-mmorpg/mise-en-place-cycle-jour-nuit-intersect-engine/"
date: 2023-10-27
categories: ['Archive']
tags: ['Intersect Engine', 'MMO', 'Game Dev', 'Tutoriel']
---

Apprendre à intégrer des ressources récoltables est une étape fondamentale pour donner vie à l'économie de votre MMORPG. Dans ce guide, nous explorons comment transformer des éléments visuels en objets interactifs que vos joueurs pourront farmer.

{{< youtube-rgpd "xVwCR--qQlY" >}}

### Résumé des notions clés

La mise en place d'un système de récolte dans Intersect Engine repose sur une chaîne de production logique :

*   **Préparation graphique :** Utilisation d'un logiciel d'édition d'image (type Paint.net) pour isoler les tuiles (32x32 ou 64x64) depuis vos *tilesets* existants. Il est crucial de créer deux états : l'objet intact et l'objet épuisé.
*   **Configuration dans le Resource Editor :**
    *   **Tool Type :** Définir l'outil requis (ex: Hache pour le bois).
    *   **Respawn Time :** Paramétrer le temps de réapparition pour équilibrer l'économie.
    *   **HP de la ressource :** Définir une plage de points de vie pour varier la difficulté de récolte.
    *   **Graphismes :** Associer les sprites créés aux états "Initial" et "Removed".
*   **Gestion des objets (Items) :**
    *   Créer l'objet récolté (ex: Rondin de bois) dans l'Item Editor.
    *   Créer l'outil de récolte (ex: Hache) en veillant à bien spécifier le `Tool Type` correspondant dans ses propriétés.
*   **Déploiement sur la carte :** Utiliser l'onglet "Attribute" de l'éditeur de map pour placer les ressources manuellement sur le terrain.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions d'Intersect Engine évoluent, la logique de ce système reste un pilier central du moteur. La séparation entre l'objet "outil" (qui possède un `Tool Type`) et l'objet "ressource" (qui possède des points de vie et des probabilités de drop) est une mécanique robuste qui n'a pas changé. Cette approche modulaire permet aux développeurs de créer des systèmes complexes — comme de la minage, de la cueillette ou de la pêche — simplement en modifiant les paramètres de l'éditeur sans avoir à toucher au code source. Maîtriser ce flux de travail est essentiel pour tout créateur souhaitant implémenter une boucle de gameplay "récolte-artisanat-vente" cohérente.

{{< footer >}}
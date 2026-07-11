---
title: "13. Créer une boutique (Shop)"
weight: 13
prev_url: "/intersect-engine/creer-un-mmorpg/creer-mobs-monstres-intersect-engine-tutoriel/"
next_url: "/intersect-engine/creer-un-mmorpg/creer-banque-fonctionnelle-intersect-engine/"
date: 2023-10-27
categories: ['Archive']
tags: ['Intersect Engine', 'Game Development', 'MMORPG', 'Tutoriel']
images: ["https://img.youtube.com/vi/I5S2GWSrcGI/maxresdefault.jpg"]
---

Dans ce tutoriel, nous allons apprendre à dynamiser l'économie de votre MMORPG en créant un système de marchands fonctionnel avec Intersect Engine.

{{< youtube-rgpd "I5S2GWSrcGI" >}}

### Résumé des notions clés

La mise en place d'un système de commerce dans Intersect Engine repose sur deux piliers : la configuration des données dans l'éditeur et l'implémentation via les événements sur la carte.

*   **Shop Editor (Gestion des stocks) :**
    *   **Création :** Définissez un nom et la monnaie utilisée par défaut pour les transactions.
    *   **Gestion des listes :** Séparez clairement les objets destinés à la vente (ce que le joueur achète) et ceux destinés au rachat (ce que le marchand accepte d'acheter au joueur).
    *   **Équilibrage :** Pensez à appliquer une marge bénéficiaire en fixant un prix de rachat inférieur au prix de vente.
    *   **Conversion de devises :** Vous pouvez ajouter des objets de type "monnaie" dans la liste de vente pour permettre aux joueurs d'échanger leurs petites coupures contre des plus grosses.

*   **Event Editor (Mise en scène) :**
    *   **Graphisme :** Choisissez un sprite de PNJ et configurez son apparence (face, animation).
    *   **Trigger (Déclencheur) :** Utilisez le "Action Button" pour que le joueur doive interagir avec le PNJ pour ouvrir la boutique.
    *   **Commandes :** Utilisez la commande `Open Shop` dans la liste des actions de l'événement pour lier votre boutique créée précédemment au PNJ.
    *   **Conditions :** Vous pouvez restreindre l'accès à la boutique selon le niveau, la classe ou les quêtes du joueur.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions d'Intersect Engine évoluent, la logique de création de boutiques reste un pilier fondamental du moteur. La séparation entre la **base de données des objets** (Shop Editor) et **l'instance physique** (Event Editor) est une structure immuable qui permet une grande flexibilité. 

Aujourd'hui, il est toujours crucial de bien tester vos restrictions de classes (comme vu dans la vidéo avec les dagues) pour éviter la frustration des joueurs. De plus, la recommandation de sauvegarder régulièrement votre projet reste le conseil le plus précieux : en développement de jeu, la stabilité de l'éditeur dépend de la rigueur de vos sauvegardes manuelles.

{{< footer >}}
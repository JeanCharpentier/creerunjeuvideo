---
title: "11. Créer et équiper les objets de départ dans Intersect Engine"
weight: 11
prev_url: "/intersect-engine/creer-un-mmorpg/guide-import-assets-systeme-monnaie-intersect-engine/"
next_url: "/intersect-engine/creer-un-mmorpg/creer-mobs-monstres-intersect-engine-tutoriel/"
date: 2024-05-22
categories: ['Archive']
tags: ['Intersect Engine', 'Game Dev', 'MMORPG', 'Tutoriel']
---

Dans ce guide, nous allons configurer l'équipement de départ pour vos classes de personnages dans Intersect Engine, afin de donner à vos joueurs un coup de pouce bien mérité dès leur arrivée en jeu.

{{< youtube-rgpd "" >}}

### Notions clés abordées
*   **Item Editor :** Création des objets (hache, bâton, dagues) avec définition des statistiques (attaque, défense, bonus).
*   **Gestion des restrictions :** Limitation du port d'armes par classe et par sexe.
*   **Slots d'équipement :** Configuration des emplacements (Weapon, Shield, Two-Handed) pour structurer l'inventaire.
*   **Class Editor :** Attribution des objets de départ et de la monnaie initiale via les index d'inventaire.
*   **Test en jeu :** Importance de créer un compte joueur standard (non-admin) pour vérifier l'attribution correcte des items au démarrage.

### Ce qui reste d'actualité aujourd'hui
Bien que l'interface d'Intersect Engine puisse évoluer au fil des mises à jour, la logique fondamentale présentée ici demeure le standard pour tout développeur de MMORPG sur ce moteur :

1.  **La hiérarchie des données :** La séparation entre la création de l'objet (Item Editor) et son attribution (Class Editor) est une structure immuable qui garantit la propreté de votre base de données.
2.  **L'équilibrage par les prérequis :** L'utilisation des niveaux minimums ou des statistiques requises pour équiper des objets puissants reste la méthode la plus efficace pour éviter le "power creep" (la montée en puissance trop rapide) dès le début de l'aventure.
3.  **L'importance du test utilisateur :** Tester avec un compte "joueur" plutôt qu'un compte "admin" est une règle d'or. Les droits d'administration peuvent masquer des erreurs de configuration sur les permissions d'objets ou les inventaires de départ.
4.  **Modularité :** La possibilité d'ajouter plusieurs index d'objets (monnaie + arme + armure) permet de créer des packs de départ personnalisés pour chaque classe, offrant une expérience de jeu unique dès la première seconde.

{{< footer >}}
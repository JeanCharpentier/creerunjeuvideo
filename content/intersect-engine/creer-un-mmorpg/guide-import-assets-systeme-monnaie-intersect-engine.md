---
title: "10. Importer vos assets et créer votre système de monnaie"
weight: 10
prev_url: "/intersect-engine/creer-un-mmorpg/optimiser-ressources-graphiques-decouper-sprites-intersect-engine/"
next_url: "/intersect-engine/creer-un-mmorpg/creer-equiper-objets-depart-intersect-engine/"
date: 2023-10-27
categories: ['Archive']
tags: ['Intersect Engine', 'Game Development', 'MMORPG', 'Tutoriel', 'Asset Management']
---

Dans ce nouvel épisode de notre série dédiée à la création d'un MMORPG avec Intersect Engine, nous abordons une étape cruciale : l'intégration de vos assets graphiques et la mise en place structurée de votre économie en jeu.

{{< youtube-rgpd "N3r_706d6ts" >}}

### Résumé des notions clés

L'organisation est la clé pour éviter de perdre du temps lors du développement de votre monde persistant. Voici les points essentiels abordés :

*   **Préparation des assets :** Avant de lancer l'éditeur, placez vos images dans le dossier `resources/items` de votre projet. Une bonne convention de nommage (ex: "Hache_Guerrier_01", "Hache_Guerrier_02") facilite grandement la recherche dans l'éditeur.
*   **Gestion des ressources :** L'utilisation de banques d'images (spritesheets) permet de gagner un temps précieux. N'hésitez pas à renommer vos fichiers par lots pour garder une structure propre.
*   **L'importance de la monnaie :** Il est fortement conseillé de créer vos types de monnaie avant vos objets équipables. Cela vous permet d'assigner immédiatement une valeur marchande à vos items lors de leur création, évitant ainsi de devoir éditer chaque objet une seconde fois plus tard.
*   **Hiérarchie monétaire :** Pour une économie équilibrée, implémentez un système de paliers (ex: 100 unités de base = 1 unité supérieure). Cela rend la gestion des prix dans les boutiques beaucoup plus flexible.
*   **Utilisation de l'Item Editor :** Apprenez à définir le type d'objet (`Currency`, `Equipment`, `Consumable`) et à remplir les champs descriptifs pour chaque item créé.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions d'Intersect Engine évoluent, la logique de gestion des assets et de la base de données reste un pilier fondamental du moteur :

1.  **Workflow de fichiers :** Le moteur scanne toujours le dossier `resources` au démarrage. La méthode consistant à préparer ses assets en amont reste la norme pour éviter les conflits de chargement.
2.  **Architecture de données :** La structure de l'Item Editor est conçue pour être modulaire. La hiérarchie des types (Currency, Equipment, etc.) est le cœur du système de jeu d'Intersect. Comprendre cette hiérarchie dès le début est toujours le meilleur moyen de concevoir un MMORPG scalable.
3.  **Bonnes pratiques :** L'anticipation des valeurs (prix, prérequis de classe) lors de la création initiale d'un objet est une règle d'or en Game Design. Cela réduit drastiquement la dette technique et le temps passé à l'équilibrage global de votre jeu.

{{< footer >}}
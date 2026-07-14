---
title: "21. Comment gérer les droits d'administration et de modération"
weight: 21
prev_url: "/intersect-engine/creer-un-mmorpg/creer-quete-fedex-intersect-engine/"
next_url: "/intersect-engine/creer-un-mmorpg/guide-migration-intersect-engine-beta-1/"
date: 2024-05-22
categories: ['Archive']
tags: ['Intersect Engine', 'MMORPG', 'Tutoriel', 'SQLite', 'Administration']
images: ["https://img.youtube.com/vi/l2UfLUE79iQ/maxresdefault.jpg"]
---

Dans ce guide, nous allons explorer comment élever les privilèges de vos joueurs au sein de votre projet MMORPG développé avec Intersect Engine, en passant par une manipulation directe de la base de données.

{{< youtube-rgpd "l2UfLUE79iQ" >}}

### Résumé des notions clés

Pour transformer un simple joueur en modérateur ou administrateur, il est nécessaire d'intervenir directement sur les fichiers du serveur. Voici les étapes essentielles à retenir :

*   **Sauvegarde indispensable :** Avant toute manipulation, copiez votre fichier `Intersect.db` situé dans `serveur/ressource`. Une erreur de manipulation peut corrompre votre base de données.
*   **Outil nécessaire :** Utilisez le logiciel **DB Browser for SQLite** pour ouvrir et modifier votre base de données sans risque.
*   **Localisation des données :** Les droits des joueurs sont gérés dans la table `users`, au sein de la colonne `Power`.
*   **Niveaux de privilèges :**
    *   `0` : Joueur standard.
    *   `1` : Modérateur (accès aux outils de modération via la touche `Inser`).
    *   `2` : Administrateur (accès complet).
*   **Procédure de sécurité :** Coupez toujours votre serveur avant d'ouvrir la base de données dans le logiciel, puis enregistrez vos modifications avant de relancer le serveur.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions d'Intersect Engine aient évolué depuis la sortie de ce tutoriel, les principes fondamentaux de gestion des données restent très pertinents :

1.  **La structure SQLite :** Intersect Engine continue d'utiliser SQLite pour la gestion des données locales. La maîtrise de *DB Browser for SQLite* reste une compétence indispensable pour tout développeur souhaitant effectuer des corrections rapides ou des modifications de masse sur ses comptes utilisateurs.
2.  **La gestion des accès :** Le système de "Power" (niveaux de privilèges) est un standard dans le développement de jeux multijoueurs. Comprendre comment le moteur hiérarchise les droits permet de mieux structurer la modération de votre communauté dès le lancement de votre serveur.
3.  **Bonnes pratiques de développement :** La règle d'or consistant à toujours sauvegarder sa base de données avant toute modification manuelle reste le meilleur conseil pour éviter de perdre des semaines de travail sur le développement de vos quêtes, objets ou cartes.

{{< footer >}}
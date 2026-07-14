---
title: "22. Guide de migration et nouveautés Beta 1"
weight: 22
prev_url: "/intersect-engine/creer-un-mmorpg/gestion-droits-administration-moderation-intersect-engine/"
next_url: "/intersect-engine/creer-un-mmorpg/maitriser-systeme-crafting-intersect-engine/"
date: 2023-10-27
categories: ['Archive']
tags: ['Intersect Engine', 'MMORPG', 'Tutoriel', 'Game Development']
images: ["https://img.youtube.com/vi/dHjTyPN0mmI/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/dHjTyPN0mmI/maxresdefault.jpg"]
---

Le passage à la version Beta 1 d'Intersect Engine marque un tournant majeur dans le développement de votre MMORPG 2D, introduisant des fonctionnalités essentielles pour enrichir l'expérience de jeu.

{{< youtube-rgpd "dHjTyPN0mmI" >}}

### Résumé des nouveautés de la Beta 1
Cette mise à jour majeure apporte des outils indispensables qui transforment la structure même de votre projet :

*   **Éditeur de quêtes dédié :** Fini le recours complexe aux événements, vous disposez désormais d'un éditeur complet pour concevoir des quêtes complexes.
*   **Systèmes sociaux et économiques :** Introduction du trading (échange entre joueurs), des groupes (parties) pour affronter des boss, et du système de craft basé sur la récolte de ressources.
*   **Interface utilisateur (UI) :** Passage à une interface "Dark Mode" pour un meilleur confort visuel et une meilleure lisibilité des couleurs lors de la création.
*   **Outil de migration :** Un utilitaire dédié permet de mettre à jour votre base de données existante vers la nouvelle version sans perdre votre progression.

### Guide de migration rapide
Pour mettre à jour votre projet en toute sécurité, suivez ces étapes clés :
1.  **Sauvegarde :** Copiez l'intégralité de votre dossier de projet actuel vers un dossier "Backup".
2.  **Nettoyage :** Supprimez tous les fichiers des dossiers `Server` et `Client/Editor`, à l'exception du dossier `Resources`.
3.  **Installation :** Téléchargez la version Beta 1 et extrayez les nouveaux fichiers dans vos dossiers respectifs.
4.  **Mise à jour des ressources :** Appliquez le patch "Beta 1 upgrade resources" en écrasant les fichiers existants.
5.  **Migration DB :** Lancez le `Intersect Migration Tool` pour mettre à jour votre base de données vers la version 6.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Intersect Engine aient évolué, les principes fondamentaux présentés ici restent le socle de tout projet sur ce moteur :
*   **La gestion des backups :** La règle d'or reste de toujours sauvegarder ses ressources avant toute manipulation de version.
*   **L'importance des outils natifs :** L'utilisation des éditeurs intégrés (Quêtes, Craft) est toujours préférable à la création de systèmes personnalisés via des événements, car ils sont optimisés pour la stabilité du serveur.
*   **La structure de projet :** La séparation claire entre le client, l'éditeur et le serveur, ainsi que l'importance du dossier `Resources`, demeure la norme pour organiser correctement vos assets et bases de données.

{{< footer >}}
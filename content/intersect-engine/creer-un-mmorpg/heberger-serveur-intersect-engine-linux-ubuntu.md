---
title: "2. Héberger son serveur Intersect Engine sur Linux (Ubuntu)"
weight: 2
prev_url: "/intersect-engine/creer-un-mmorpg/debuter-avec-intersect-engine-installation-serveur-mmo/"
next_url: "/intersect-engine/creer-un-mmorpg/decouverte-editeur-cartes-base-donnees-intersect-engine/"
date: 2023-10-27
categories: ['Archive']
tags: ['Intersect Engine', 'Linux', 'Ubuntu', 'Serveur', 'MMORPG']
---

Déployer son MMORPG sur un serveur dédié ou un VPS Linux est une étape cruciale pour garantir une disponibilité 24h/24 et une meilleure stabilité. Voici comment configurer votre environnement sous Ubuntu pour faire tourner le moteur Intersect Engine.

{{< youtube-rgpd "" >}}

### Résumé des étapes clés

Pour transformer votre machine Linux en serveur de jeu, voici la procédure à suivre via votre terminal SSH :

*   **Installation de Mono :** Le moteur Intersect étant basé sur .NET, l'installation de `mono-complete` est indispensable pour exécuter les fichiers `.exe` sur un environnement Linux.
    *   Commande : `sudo apt-get install mono-complete`
*   **Récupération des fichiers :** Téléchargez l'archive du moteur (client + serveur) directement sur votre serveur via `wget`.
*   **Décompression :** Utilisez la commande `unzip` pour extraire les fichiers de l'archive.
*   **Lancement du serveur :** Naviguez dans le dossier `/server` et exécutez le serveur avec la commande `mono Intersect.Server.exe`.
*   **Configuration réseau :** Identifiez l'adresse IP de votre machine (via `ifconfig`) et mettez à jour le fichier `config.xml` de votre client/éditeur local pour pointer vers cette IP au lieu de `localhost`.

### Ce qui reste d'actualité aujourd'hui

Bien que les versions d'Intersect Engine aient évolué, les fondamentaux présentés dans ce tutoriel restent des piliers pour tout développeur de MMORPG :

1.  **L'importance de l'hébergement distant :** Le passage de l'hébergement local (votre PC) vers un VPS (Virtual Private Server) est toujours la norme pour passer d'un projet de test à un jeu jouable par une communauté.
2.  **La gestion via SSH :** La maîtrise de la ligne de commande reste l'outil de prédilection pour administrer des serveurs de jeu, offrant une gestion légère et efficace sans interface graphique gourmande en ressources.
3.  **La portabilité :** La capacité d'Intersect à fonctionner sur Linux via Mono (ou les versions plus récentes basées sur .NET Core/.NET 5+) prouve la flexibilité du moteur, permettant d'optimiser les coûts d'hébergement en évitant les licences Windows Server.
4.  **La structure des fichiers :** La séparation entre le dossier `Client & Editor` et le dossier `Server` reste la structure logique standard pour maintenir une architecture client-serveur propre et sécurisée.

{{< footer >}}
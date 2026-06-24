---
title: "39. Intégrer les classements (Leaderboards) Google Play"
weight: 39
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Android', 'Google Play Services', 'Leaderboard', 'Mobile', 'Blueprints']
---

Dans cet épisode, nous allons franchir une étape cruciale pour la rétention de vos joueurs : l'intégration des classements (Leaderboards) via les services Google Play. Apprendre à configurer ces outils permet non seulement de créer une compétition saine entre vos joueurs, mais aussi d'ajouter une rejouabilité infinie à vos projets.

{{< youtube-rgpd "gaL-CpfAp_Q" >}}

### Résumé de la mise en place
*   **Configuration Console Google Play :** Création du classement, définition du format (chiffres), choix de l'ordre (score le plus élevé) et activation de la protection contre la falsification.
*   **Identifiants :** Récupération de l'ID du classement généré par Google pour le lier à votre projet Unreal Engine.
*   **Paramétrage du projet :** Ajout du classement dans les *Project Settings > Android > Google Play Services* (Leaderboard Map).
*   **Gestion de la connexion :** Création d'un `BP_Game` (Actor) pour centraliser l'état de connexion (`isLoggedIn`) et éviter les reconnexions inutiles.
*   **Interface utilisateur :** Utilisation du node `Show Platform Specific Leaderboard Screen` dans votre Widget de menu pour afficher l'interface native de Google Play.

### Ce qui reste d'actualité aujourd'hui
Bien que l'écosystème Android évolue, les fondamentaux présentés ici restent la norme pour les développeurs Unreal Engine :
*   **La structure des IDs :** Le couplage entre la console Google Play et les *Project Settings* d'Unreal Engine est toujours la méthode privilégiée pour éviter de coder en dur des identifiants complexes.
*   **La gestion des états :** Utiliser un Actor dédié (comme `BP_Game`) pour gérer la persistance de la connexion utilisateur est une bonne pratique d'architecture qui facilite la maintenance.
*   **L'interface native :** Le node `Show Platform Specific Leaderboard Screen` est toujours le moyen le plus simple et le plus robuste pour afficher les classements sans avoir à créer une interface personnalisée complexe, garantissant ainsi une expérience utilisateur familière aux joueurs Android.
*   **Sécurité :** L'activation de la protection contre la falsification reste indispensable pour maintenir l'intégrité de vos classements face aux scores aberrants.

{{< footer >}}
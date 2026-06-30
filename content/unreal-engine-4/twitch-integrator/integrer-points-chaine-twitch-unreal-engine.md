---
title: "3. Intégrer les Points de Chaîne Twitch dans Unreal Engine"
weight: 3
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Twitch', 'Blueprint', 'GameDev', 'Tutoriel', 'Interactivité']
---

Dans ce troisième volet de notre série dédiée aux "Twitch Plays", nous allons franchir une étape cruciale pour la monétisation et l'engagement de votre stream : **l'intégration des points de chaîne Twitch dans Unreal Engine**. Cette fonctionnalité permet à vos spectateurs de déclencher des événements spécifiques en jeu en échange de leurs points accumulés.

{{< youtube-rgpd "t-oeC4T0xt4" >}}

### Résumé de l'épisode
*   **Prérequis :** Vous devez être affilié ou partenaire Twitch pour accéder aux points de chaîne.
*   **Configuration Twitch :** Création de la récompense dans le Dashboard des créateurs (nom, prix, icône, et option de saisie de texte).
*   **Récupération de l'ID :** Identification du `custom_reward_id` unique pour chaque récompense créée.
*   **Logique Blueprint :** Utilisation du tableau `Tags Data` pour filtrer les messages entrants.
*   **Débogage :** Mise en place d'une boucle `For Each Loop` pour identifier les champs envoyés par Twitch et isoler l'identifiant de la récompense.
*   **Implémentation :** Création d'une condition (`Branch`) pour vérifier si un message est lié à une récompense et déclencher une action spécifique en jeu.

### Ce qui reste d'actualité aujourd'hui
Bien que les interfaces de Twitch puissent légèrement évoluer, les fondamentaux techniques présentés ici restent parfaitement valables pour Unreal Engine 4 (et transposables en UE5) :

1.  **La structure des données :** Le système de `Tags Data` reste la méthode standard pour parser les informations provenant de l'API Twitch.
2.  **L'importance de l'ID unique :** Le `custom_reward_id` est toujours la clé maîtresse pour différencier une interaction classique (chat) d'une interaction payante (points de chaîne).
3.  **La modularité :** La méthode consistant à séparer le traitement des messages du chat de l'exécution des récompenses permet de garder un Blueprint propre et évolutif.
4.  **Le débogage via le Log :** L'utilisation de l'Output Log pour inspecter les données en temps réel reste la meilleure pratique pour diagnostiquer des problèmes de communication entre votre serveur Twitch et votre jeu.

{{< footer >}}
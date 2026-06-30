---
title: "1. Créer une passerelle entre Twitch et Unreal Engine 4"
weight: 1
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Twitch', 'Plugin', 'Blueprints', 'GameDev', 'Tutoriel']
---

L'interactivité est devenue un pilier du streaming moderne. Permettre à votre communauté d'influencer directement le gameplay de votre jeu via le chat Twitch est un excellent moyen d'augmenter l'engagement. Dans ce premier volet, nous allons configurer l'environnement nécessaire pour connecter votre projet Unreal Engine 4 à l'API de Twitch.

{{< youtube-rgpd "sNsU4wOdbBk" >}}

### Résumé des étapes clés
*   **Configuration Développeur :** Création d'un compte sur la console développeur Twitch et enregistrement d'une application.
*   **Gestion des Redirections :** Configuration de l'URL de redirection (OAuth) pour récupérer votre jeton d'accès.
*   **Scopes (Droits) :** Attribution des permissions nécessaires (`chat:read` et `chat:edit`) pour permettre au plugin de lire et d'écrire dans votre chat.
*   **Installation du Plugin :** Intégration du *Twitch Integrator* depuis le Marketplace Epic Games.
*   **Mise en place dans l'Editor :** Placement de l'acteur `Twitch Chat` dans votre niveau et configuration des identifiants (Token, Channel, Username).
*   **Premier test :** Utilisation de l'événement `On Chat Message` pour vérifier la réception des données via un `Print String`.

### Ce qui reste d'actualité aujourd'hui
Bien que les interfaces de la console développeur Twitch puissent évoluer légèrement au fil du temps, les fondamentaux techniques restent inchangés :
1.  **La sécurité des jetons (Tokens) :** La règle d'or est toujours de ne jamais exposer votre *Access Token* ou votre *Client Secret* dans une vidéo ou un dépôt public.
2.  **Le principe des Scopes :** Le concept de "moindre privilège" est crucial. Ne demandez que les droits strictement nécessaires au fonctionnement de votre jeu pour protéger votre compte.
3.  **L'architecture par événements :** Le fonctionnement du plugin basé sur des *Events* (On Chat Message, On Cheers, etc.) est une pratique standard dans le développement Unreal Engine pour garder un code propre et réactif.
4.  **La structure des données :** La manière dont Twitch envoie les informations (JSON/Strings) nécessite toujours une étape de parsing (décomposition) pour extraire le nom de l'utilisateur, le message et les badges, ce qui sera le sujet de notre prochaine étape.

{{< footer >}}
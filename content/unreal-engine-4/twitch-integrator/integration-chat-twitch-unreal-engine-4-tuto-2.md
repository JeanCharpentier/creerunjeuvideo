---
title: "2. Intégrer le chat Twitch dans Unreal Engine 4 : Gestion des messages et statuts"
weight: 2
date: 2026-06-17
categories: ['GameDev']
tags: ['Unreal Engine 4', 'Twitch API', 'Blueprints', 'UMG']
images: ["https://img.youtube.com/vi/rv3-yRX0S6Y/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/rv3-yRX0S6Y/maxresdefault.jpg"]
---

Dans ce deuxième épisode de notre série dédiée à l'intégration de Twitch dans Unreal Engine 4, nous allons passer à l'étape supérieure : ne plus simplement afficher un message brut, mais décortiquer les données envoyées par vos viewers. Vous apprendrez à identifier qui écrit, quel est son statut (Sub, Modérateur, VIP) et comment transmettre ces informations proprement vers une interface utilisateur (HUD) via une *Game Instance*.

{{< youtube-rgpd "rv3-yRX0S6Y" >}}

{{< youtube-rgpd "P71kGXqOeKo" >}}

### Résumé des étapes clés
*   **Décomposition des données :** Utilisation du node `Break Chat Message Data` pour extraire le nom d'utilisateur, le message, et les booléens de statut.
*   **Logique de filtrage :** Mise en place de branches (`Branch`) pour vérifier les permissions (Modérateur, Sub, VIP) et formater le texte en conséquence.
*   **Architecture propre :** Utilisation d'une `Game Instance` pour stocker les variables de chat, garantissant que les données persistent entre les niveaux et les menus.
*   **Liaison UMG :** Création de *Bindings* dans vos widgets pour afficher dynamiquement le pseudo, le statut et le message du viewer en temps réel.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Unreal Engine aient évolué, les fondamentaux abordés ici restent des piliers du développement :
1.  **La Game Instance :** C'est toujours la méthode recommandée pour faire transiter des données globales qui ne doivent pas être détruites lors d'un changement de niveau.
2.  **Le Binding UMG :** La technique de création de fonctions de liaison pour mettre à jour l'interface reste une pratique standard, bien que l'utilisation de *Property Bindings* ou de *Delegates* soit parfois préférée pour optimiser les performances sur des projets complexes.
3.  **La structure des données Twitch :** La logique de récupération des informations via des plugins tiers (ou via l'API Twitch directement) suit toujours le même schéma : réception d'un événement, parsing du JSON/Data, et mise à jour de l'état du jeu.

{{< footer >}}
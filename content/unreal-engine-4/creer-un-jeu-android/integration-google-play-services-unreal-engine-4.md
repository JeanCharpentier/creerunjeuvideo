---
title: "36. Intégration des services Google Play : Association et Authentification"
weight: 36
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Android', 'Google Play Services', 'Mobile', 'Tutoriel', 'Déploiement']
---

Dans cet épisode, nous abordons une étape cruciale pour tout développeur mobile sur Unreal Engine 4 : la liaison entre votre projet et les services de jeu Google Play (Google Play Games Services). Cette configuration est indispensable pour activer des fonctionnalités comme les succès, les classements ou la sauvegarde dans le cloud.

{{< youtube-rgpd "" >}}

### Résumé de la procédure
*   **Association de l'application :** Liaison du package Android dans la console Google Play pour générer la clé d'authentification OAuth.
*   **Configuration des options :** Choix des fonctionnalités multijoueurs et activation de l'anti-piratage pour restreindre l'accès aux services aux seules versions téléchargées via le Play Store.
*   **Récupération de l'empreinte SHA1 :** Utilisation de l'outil `keytool` via l'invite de commande (CMD) pour extraire l'empreinte numérique de votre keystore.
*   **Validation :** Saisie de l'empreinte dans la console Google Play pour finaliser l'association sécurisée entre votre jeu et les services Google.

### Ce qui reste d'actualité aujourd'hui
Bien que l'interface de la Google Play Console évolue régulièrement, les fondamentaux techniques restent identiques :
1.  **La nécessité du Keystore :** La signature de votre application est toujours le socle de la sécurité Android. Sans une correspondance exacte entre l'empreinte SHA1 de votre keystore et celle déclarée dans la console, les services Google Play renverront systématiquement une erreur d'authentification.
2.  **L'outil Keytool :** L'utilisation de la ligne de commande `keytool` reste la méthode la plus fiable pour extraire les informations de signature, peu importe la version d'Unreal Engine utilisée.
3.  **Le rôle de l'anti-piratage :** L'option de restriction d'accès aux utilisateurs du Play Store demeure une bonne pratique pour protéger vos services de backend contre les appels non autorisés provenant de versions "sideloadées" ou modifiées de votre APK.

*Note : Assurez-vous toujours de conserver une copie de sauvegarde de votre fichier `.keystore` et de votre mot de passe, car sans eux, toute mise à jour de votre jeu sur le store deviendra impossible.*

{{< footer >}}
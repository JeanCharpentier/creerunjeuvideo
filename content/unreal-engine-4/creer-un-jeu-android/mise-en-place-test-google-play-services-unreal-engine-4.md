---
title: "38. Mise en place et test de la connexion Google Play Services"
weight: 38
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Android', 'Google Play Services', 'Blueprint', 'Mobile Development']
images: ["https://img.youtube.com/vi/yXUE5p4Y8z4/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/yXUE5p4Y8z4/maxresdefault.jpg"]
---

Dans cet épisode, nous abordons une étape cruciale du développement mobile sous Unreal Engine 4 : la vérification de l'intégration des Google Play Services. Après avoir configuré les paramètres complexes, il est temps de tester si votre application communique correctement avec les serveurs de Google.

{{< youtube-rgpd "yXUE5p4Y8z4" >}}

### Résumé de l'épisode
*   **Workflow de test :** Explication sur la nécessité de recompiler l'APK pour tester les services, tout en précisant qu'il n'est pas nécessaire de réuploader sur la console Google Play à chaque modification interne.
*   **Implémentation Blueprint :** Utilisation du node `Show External Login UI` dans le Level Blueprint pour déclencher la fenêtre de connexion.
*   **Gestion des retours :** Mise en place de `Print String` sur les sorties "On Success" et "On Failure" pour déboguer visuellement la connexion sur l'appareil.
*   **Processus de build :** Rappel sur l'utilisation du dossier "Export" et du script d'installation (`install.bat`) pour déployer rapidement le projet sur votre périphérique Android.
*   **Validation :** Vérification des autorisations demandées par Google Play au lancement du jeu.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Unreal Engine aient évolué, les fondamentaux abordés ici restent des piliers du développement mobile :
1.  **Le cycle de itération :** Le processus de packaging et d'installation via le script `install.bat` reste la méthode standard pour tester les fonctionnalités natives (Google Play, Firebase, etc.) sur un appareil physique.
2.  **L'utilisation des nodes de Login :** Le node `Show External Login UI` est toujours la porte d'entrée universelle pour l'authentification sur les plateformes mobiles (Android/iOS).
3.  **Le débogage par Print String :** Même dans les versions récentes d'UE5, le `Print String` reste l'outil de diagnostic le plus rapide pour confirmer qu'un flux d'exécution Blueprint est bien déclenché sur mobile.
4.  **Gestion des autorisations :** La nécessité de valider les autorisations (permissions) au runtime est une exigence de sécurité Android qui n'a fait que se renforcer avec les mises à jour de l'OS.

{{< footer >}}
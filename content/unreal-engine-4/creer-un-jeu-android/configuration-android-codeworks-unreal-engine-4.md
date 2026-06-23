---
title: "3. Configuration de l''environnement Android avec CodeWorks"
weight: 3
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Android', 'SDK', 'CodeWorks', 'Développement Mobile']
---

Dans cet épisode, nous abordons une étape cruciale pour tout développeur souhaitant porter ses projets sur mobile : la configuration de l'environnement Android. Pour qu'Unreal Engine puisse compiler vos jeux vers des appareils Android, il ne suffit pas d'avoir le moteur ; il faut installer le kit de développement logiciel (SDK) et les outils associés.

{{< youtube-rgpd "" >}}

### Résumé de la procédure d'installation
*   **Localisation des outils :** Accédez au répertoire d'installation d'Unreal Engine (généralement dans `C:\Program Files\Epic Games\UE_4.xx\Engine\Extras\AndroidWorks`).
*   **Lancement de l'installeur :** Exécutez `CodeWorks for Android` en tant qu'administrateur.
*   **Configuration des répertoires :** Il est fortement recommandé de conserver les chemins d'installation par défaut pour éviter les conflits de configuration avec Unreal Engine.
*   **Sélection des composants :**
    *   Assurez-vous que le SDK Android est bien réglé sur "Install".
    *   Sélectionnez les versions d'API nécessaires (API 19, 21, 23, etc.) selon les cibles de compatibilité souhaitées.
*   **Validation :** Acceptez les licences Nvidia/Android pour lancer le téléchargement et l'installation des packages.

### Ce qui reste d'actualité aujourd'hui
Bien que cet article se base sur une version ancienne (4.17), les principes fondamentaux restent valides pour le développement mobile :
1.  **La dépendance au SDK :** Unreal Engine nécessite toujours des outils externes (SDK, NDK, JDK) pour transformer votre code C++ ou vos Blueprints en un fichier `.apk` ou `.aab` exécutable sur Android.
2.  **L'importance des API :** La gestion des versions d'API (Target SDK) reste le cœur du développement Android. Même dans les versions récentes d'UE5, vous devez toujours configurer ces versions dans les paramètres du projet.
3.  **Chemins d'installation :** La règle d'or reste la même : évitez les chemins d'installation complexes ou contenant des espaces/caractères spéciaux, car cela peut causer des erreurs de compilation obscures lors de l'appel aux outils de build (Gradle).

*Note : Dans les versions récentes d'Unreal Engine (4.25+ et UE5), Nvidia CodeWorks a été remplacé par le "Android Setup" (SetupAndroid.bat) situé dans le dossier `Engine/Extras/Android`. La logique reste identique, mais le processus est désormais plus automatisé.*

{{< footer >}}
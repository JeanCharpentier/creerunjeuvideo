---
title: "48. Mise en place d''un système de sauvegarde persistant"
weight: 48
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprints', 'SaveGame', 'GameDev', 'Tutoriel']
images: ["https://img.youtube.com/vi/1bCEcHDZgtQ/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/1bCEcHDZgtQ/maxresdefault.jpg"]
---

Dans cet épisode, nous abordons une étape cruciale pour tout jeu : la persistance des données. Contrairement à la `GameInstance` qui est réinitialisée à chaque fermeture du jeu, l'objet `SaveGame` permet d'écrire des informations directement sur le disque dur de l'utilisateur.

{{< youtube-rgpd "1bCEcHDZgtQ" >}}

### Résumé des étapes clés
*   **Création de la classe SaveGame** : Création d'un Blueprint de type `SaveGame` (nommé `MySaveGame`) pour stocker les variables persistantes.
*   **Définition des variables** : Ajout de `S_score` (Integer) et `S_niveau` (Name) avec une nomenclature spécifique pour les distinguer des variables temporaires.
*   **Logique de sauvegarde** :
    *   Utilisation du node `Create Save Game Object` pour instancier la classe.
    *   Récupération des données actuelles depuis le `ThirdPersonCharacter` (pour éviter les décalages de la `GameInstance`).
    *   Utilisation du node `Save Game to Slot` pour écrire les données sur le disque dans un emplacement nommé ("save").
*   **Organisation** : Utilisation des *Reroute Nodes* pour maintenir la lisibilité du graphe Blueprint.

### Ce qui reste d'actualité aujourd'hui
Bien que cet épisode se concentre sur Unreal Engine 4, les principes fondamentaux de la persistance des données restent identiques dans Unreal Engine 5 :
1.  **La distinction entre mémoire vive et disque** : La `GameInstance` reste l'outil idéal pour le transfert de données entre niveaux, tandis que le `SaveGame` est indispensable pour la pérennité après fermeture de l'application.
2.  **Le système de Slots** : Le concept de "Slot" (nom de fichier de sauvegarde) est toujours la méthode standard pour gérer plusieurs profils de sauvegarde.
3.  **La structure des données** : La pratique consistant à préfixer ses variables de sauvegarde (ex: `S_`) est une excellente habitude de développement pour éviter les erreurs de logique dans des projets complexes.
4.  **Conversion de types** : La conversion automatique entre `String` et `Name` lors de la récupération du nom du niveau est une fonctionnalité native qui facilite grandement le workflow.

{{< footer >}}
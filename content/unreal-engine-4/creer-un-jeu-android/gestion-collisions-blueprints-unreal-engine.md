---
title: "17. Gestion des collisions et détection d''objets dans Unreal Engine 4"
weight: 17
date: 2026-06-17
categories: ['Développement de jeux']
tags: ['Unreal Engine 4', 'Blueprints', 'Collision', 'GameDev']
---

Dans cet épisode, nous abordons une étape cruciale pour l'interactivité de votre jeu : la gestion des collisions. Nous allons apprendre à faire en sorte que votre personnage puisse "ressentir" les objets qu'il touche, qu'il s'agisse de collecter des points ou de déclencher un Game Over.

{{< youtube-rgpd "a9iGvXzS9FQ" >}}

### Au programme de cet épisode :
*   **Utilisation de l'Event Hit** : Apprendre à capturer l'événement de collision dans le `SideScrollerCharacter`.
*   **Stockage d'informations** : Utiliser des variables pour garder une trace de l'objet touché (`ObjectTouché`).
*   **Filtrage par classe** : Utiliser le node `Get Class` et `Equal (Class)` pour vérifier si l'objet touché est bien un "Tron".
*   **Analyse des composants** : Utiliser `Break Hit Result` pour identifier précisément quelle partie de l'objet (la "Loose Box" ou la "Point Box") a été percutée.
*   **Hiérarchie des composants** : Comprendre comment naviguer dans les enfants d'un Blueprint via `Get Child Component` pour isoler des zones de collision spécifiques.
*   **Débogage visuel** : Utilisation du `Print String` pour valider le fonctionnement de la logique en temps réel.

### Ce qui reste d'actualité aujourd'hui
Bien que cet épisode se concentre sur Unreal Engine 4, les concepts fondamentaux restent parfaitement valables pour Unreal Engine 5 :
*   **Le système d'événements** : L'utilisation de l'`Event Hit` est toujours la méthode standard pour gérer les collisions physiques directes.
*   **La structure des Blueprints** : La logique de "Break" d'une structure de collision et la vérification des classes restent identiques.
*   **La hiérarchie des composants** : La gestion des composants parents/enfants dans le viewport est un pilier de l'organisation des Actors dans l'écosystème Unreal.
*   **Bonnes pratiques** : L'importance de commenter ses nœuds Blueprints pour maintenir un projet lisible est un conseil qui ne vieillira jamais, quel que soit le moteur utilisé.

{{< footer >}}
---
title: "Créer et intégrer un menu Flash dans Unreal Engine 3 (UDK)"
date: 2026-06-17
categories: ["GameDev"]
tags: ["Unreal Engine 3", "UDK", "Flash", "UI", "Tutoriel"]
images: ["https://img.youtube.com/vi/XhYARTXctIg/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/XhYARTXctIg/maxresdefault.jpg"]
---

Dans cet article, nous revenons sur une technique classique mais fondamentale de l'ère **Unreal Engine 3 (UDK)** : l'intégration d'interfaces utilisateur (UI) via Adobe Flash. Bien que les workflows modernes aient évolué vers UMG (Unreal Motion Graphics), comprendre comment l'UDK communiquait avec le moteur Scaleform est essentiel pour maintenir ou étudier des projets legacy.

{{< youtube-rgpd "XhYARTXctIg" >}}

### Résumé du processus d'intégration
La création d'un menu fonctionnel pour l'UDK se décompose en trois phases majeures :

*   **Conception dans Adobe Flash (CS3 recommandé) :**
    *   Configuration du projet en ActionScript 2.0 (seule version supportée par l'UDK).
    *   Organisation rigoureuse des calques (Fond, Logo, Boutons).
    *   Exportation des assets en format `.swf` avec des textures en puissances de deux.
    *   Utilisation des `FSCommand` pour envoyer des signaux au moteur de jeu.
*   **Importation dans l'UDK :**
    *   Import du fichier `.swf` via le *Content Browser*.
    *   Configuration du package et des textures associées.
*   **Logique dans Kismet :**
    *   Utilisation de l'action `Open GFX Movie` pour afficher l'interface.
    *   Gestion du `Cinematic Mode` pour masquer le HUD par défaut.
    *   Liaison des `FSCommand` à des `Console Command` (ex: `Open DM-Deck`) pour déclencher les actions de jeu (Lancer la partie, Quitter).

### Ce qui reste d'actualité aujourd'hui

Bien que l'utilisation de Flash/Scaleform soit aujourd'hui obsolète au profit de solutions natives comme UMG ou Slate dans Unreal Engine 5, certains concepts restent des piliers du développement UI :

1.  **La séparation des responsabilités :** Comme dans le tutoriel, la distinction entre le design visuel (l'interface) et la logique de contrôle (le moteur de jeu) est toujours la base de toute architecture UI propre.
2.  **La gestion des événements :** Le principe de "déclencher une action via un signal" (ici les `FSCommand`) est l'ancêtre direct des *Event Dispatchers* et des *Delegates* que nous utilisons quotidiennement dans les Blueprints modernes.
3.  **L'optimisation des assets :** La contrainte des textures en puissances de deux et l'organisation des dossiers restent des bonnes pratiques pour la gestion de la mémoire vidéo et l'organisation des projets, quel que soit le moteur utilisé.
4.  **L'importance du "Game Mode" :** La gestion des transitions entre les menus et les modes de jeu (via les commandes console) rappelle que le chargement de niveaux et la gestion des états de jeu sont des problématiques immuables du GameDev.

{{< footer >}}
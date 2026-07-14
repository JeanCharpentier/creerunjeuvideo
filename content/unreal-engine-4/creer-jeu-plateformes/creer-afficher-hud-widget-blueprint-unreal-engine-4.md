---
title: "19. Créer et afficher un HUD avec les Widget Blueprints"
weight: 19
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['HUD', 'Widget Blueprint', 'UI', 'GameDev', 'Tutoriel']
images: ["https://img.youtube.com/vi/jvwX6Jhlzyw/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/jvwX6Jhlzyw/maxresdefault.jpg"]
---

Dans cet épisode, nous abordons une étape cruciale pour l'expérience utilisateur : l'affichage d'informations en temps réel. Que ce soit pour un score, une barre de vie ou un compteur de munitions, le système de **HUD (Heads-Up Display)** est indispensable. Nous allons voir comment créer une interface utilisateur simple à l'aide des **Widget Blueprints** dans Unreal Engine 4 et comment l'injecter dans votre viewport dès le lancement de la partie.

{{< youtube-rgpd "jvwX6Jhlzyw" >}}

### Résumé des étapes clés
*   **Organisation :** Création d'un dossier dédié `HUD` dans votre Content Browser pour garder le projet propre.
*   **Création du Widget :** Utilisation de l'outil *User Interface > Widget Blueprint* pour concevoir l'affichage.
*   **Design :** Ajout de composants `Text` pour le libellé "Score" et la valeur numérique.
*   **Ancrage (Anchors) :** Utilisation des ancres pour garantir que l'interface reste bien positionnée, quelle que soit la résolution d'écran du joueur.
*   **Programmation (Level Blueprint) :**
    *   Utilisation de l'événement `Event BeginPlay` pour initialiser l'UI.
    *   Utilisation de la node `Create Widget` pour instancier votre classe HUD.
    *   Utilisation de la node `Add to Viewport` pour rendre le widget visible à l'écran.

### Ce qui reste d'actualité aujourd'hui
Bien que les versions d'Unreal Engine aient évolué (notamment avec l'arrivée de *Common UI* ou *UMG* amélioré), les fondamentaux présentés ici restent la base absolue du développement UI :
*   **Le concept de Widget Blueprint :** C'est toujours la méthode standard pour créer des interfaces 2D dans le moteur.
*   **L'importance des Ancres :** La gestion du responsive design via les ancres est une compétence indispensable pour éviter que votre interface ne soit coupée ou mal placée sur différents formats d'écran (16:9, 21:9, etc.).
*   **Le cycle de vie :** La logique `Create Widget` -> `Add to Viewport` est toujours la procédure standard pour afficher une interface utilisateur au démarrage d'un niveau ou d'une partie.

{{< footer >}}
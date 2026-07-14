---
title: "3. Création de projet et gestion des ressources"
weight: 3
prev_url: "/game-maker-studio/shoot-them-up/installation-configuration-gamemaker-studio-debutants/"
next_url: "/game-maker-studio/shoot-them-up/creation-objets-scrolling-parallaxe-gamemaker/"
date: 2023-10-27
categories: ['Archive']
tags: ['Game Maker Studio', 'Tutoriel', 'Developpement de jeux', 'Debutant']
images: ["https://img.youtube.com/vi/b3xJZ1A7FSM/maxresdefault.jpg"]
---

Dans ce guide, nous explorons les étapes fondamentales pour bien débuter sur Game Maker Studio : de la configuration de votre premier projet à l'importation structurée de vos assets graphiques et sonores.

{{< youtube-rgpd "b3xJZ1A7FSM" >}}

### Résumé des notions clés

Pour bien structurer votre projet dès le lancement, voici les étapes essentielles abordées :

*   **Initialisation du projet :** Création via l'onglet "New", choix du répertoire et importance du nommage pour une meilleure organisation.
*   **Interface utilisateur :** Compréhension de la hiérarchie de l'interface, notamment la colonne de gauche dédiée aux ressources (Sprites, Sounds, Backgrounds).
*   **Gestion des Sprites :** 
    *   Renommage systématique (ex: `s_vaisseau`) pour éviter les conflits.
    *   Utilisation de l'outil "Center" pour définir le point d'origine de l'objet.
    *   Activation du "Precise collision checking" pour une détection de collision pixel-par-pixel, idéale pour les jeux d'action.
*   **Gestion des Sons :** Importation via "Load Sound", avec une préférence pour le mode "Uncompressed" pour les musiques afin de limiter la charge CPU.
*   **Gestion des Backgrounds :** Importation des fonds (ex: étoiles pour un effet de parallaxe) via la section dédiée.
*   **Bonnes pratiques :** Sauvegarde régulière du projet pour éviter toute perte de données en cas de plantage.

### Ce qui reste d'actualité aujourd'hui

Bien que Game Maker ait évolué vers des versions plus récentes (comme GMS2 ou GMS3), les fondamentaux présentés ici restent le socle de tout développement réussi :

1.  **La rigueur du nommage :** Adopter une convention (préfixes comme `s_`, `snd_`, `bg_`) est une règle d'or qui vous sauvera des heures de débogage lorsque votre projet comptera des centaines d'assets.
2.  **La gestion des collisions :** La distinction entre les masques de collision simples (rectangulaires) et précis reste cruciale pour équilibrer performance et précision dans vos jeux.
3.  **L'optimisation sonore :** Le choix entre "Uncompressed" (pour la rapidité d'exécution) et "Compressed" (pour économiser la mémoire vive) est toujours une question pertinente pour le développement sur mobile ou plateformes limitées.
4.  **L'organisation de l'espace de travail :** La structure par dossiers (Sprites, Sounds, Rooms) est le cœur même du workflow de Game Maker, garantissant une navigation fluide dans vos projets les plus complexes.

{{< footer >}}
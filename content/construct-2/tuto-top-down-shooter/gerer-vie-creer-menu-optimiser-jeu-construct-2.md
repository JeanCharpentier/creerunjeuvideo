---
title: "6. Gérer la Vie, Créer un Menu et Optimiser son Jeu"
weight: 6
prev_url: "/construct-2/tuto-top-down-shooter/construct-2-munitions-rechargement-hud-statique/"
date: 2023-10-27
categories: ['Archive']
tags: ['Construct 2', 'Game Dev', 'Tutoriel', 'HTML5', 'Variables', 'Evenements', 'Optimisation', 'Menu', 'Export']
images: ["https://img.youtube.com/vi/tlPL1TQw7kU/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/tlPL1TQw7kU/maxresdefault.jpg"]
---
Dans ce sixième épisode de notre série dédiée à Construct 2, nous allons approfondir la gestion des packs de vie, structurer notre jeu avec un menu d'accueil et peaufiner les performances et l'organisation de notre projet.

{{< youtube-rgpd "tlPL1TQw7kU" >}}

### Résumé des notions clés

*   **Gestion des Packs de Vie (Health Packs)**
    *   Création du sprite "Elpack" (Health Pack) et ajout d'une variable d'instance `pv` (points de vie) pour définir la quantité de soin.
    *   Ajout d'une variable d'instance `MaxV` (vie maximale) au joueur pour définir sa capacité de vie maximale.
    *   Initialisation de la vie du joueur à `MaxV` au démarrage du layout pour garantir une vie pleine au début.
    *   Implémentation de deux logiques de ramassage pour les packs de vie :
        *   Ajout des `pv` du pack à la vie du joueur si cela ne dépasse pas `MaxV`.
        *   Réinitialisation de la vie du joueur à `MaxV` si le ramassage du pack le ferait dépasser, évitant ainsi de soigner au-delà du maximum.
*   **Création d'un Menu Principal**
    *   Ajout d'un nouveau layout "Menu" et d'une feuille d'événements dédiée "ES_Menu" pour gérer la logique du menu.
    *   Intégration d'un bouton "Jouer" sur le menu qui, une fois cliqué, redirige le joueur vers le "Level 1" (le jeu).
    *   Modification de l'événement de mort du joueur pour qu'il revienne au menu principal plutôt que de simplement disparaître.
*   **Optimisation et Améliorations du Jeu**
    *   **Nettoyage des balles**: Ajout d'un événement pour détruire automatiquement les balles qui sortent du layout, économisant ainsi des ressources.
    *   **Point de sortie du tir**: Création d'un "Image Point" nommé "gun" sur le sprite du joueur, permettant aux balles de partir de l'extrémité de l'arme pour un rendu plus réaliste.
    *   **Organisation du code**: Utilisation de groupes d'événements ("System", "Marine", "Balles") pour structurer et rendre plus lisible la feuille d'événements.
    *   **Exportation du jeu**: Explication du processus d'exportation du projet en "HTML5 Website" et des étapes pour le déployer sur un hébergement web.
*   **Devoir Maison**
    *   Appliquer la logique de "vie maximale" aux munitions : faire en sorte que ramasser un chargeur ne permette pas de dépasser la capacité maximale du chargeur du joueur.

### Ce qui reste d'actualité aujourd'hui

Bien que Construct 2 ait évolué vers Construct 3, les principes fondamentaux abordés dans ce tutoriel restent des piliers du développement de jeux vidéo et sont applicables à la plupart des moteurs de jeu modernes :

*   **Logique de jeu fondamentale**: La gestion des attributs du joueur (vie, munitions) via des variables d'instance et l'implémentation de conditions pour interagir avec des objets (packs de vie, chargeurs) sont des concepts universels.
*   **Structuration de l'expérience utilisateur**: La création d'un menu principal, la gestion des transitions entre les écrans (jeu, menu, fin de partie) sont essentielles pour une expérience utilisateur cohérente et professionnelle.
*   **Optimisation des ressources**: La pratique de détruire les objets hors écran (comme les balles) est une technique d'optimisation courante pour maintenir les performances du jeu, même avec des moteurs plus puissants.
*   **Précision visuelle et gameplay**: L'utilisation de "points d'image" ou de "sockets" pour définir des points d'attache précis sur les sprites (comme la sortie d'une arme) est une méthode standard pour améliorer le réalisme et la précision du gameplay.
*   **Organisation du projet**: L'importance de regrouper les événements ou le code par catégorie (système, joueur, projectiles) est cruciale pour la maintenabilité, la lisibilité et la collaboration sur des projets de toute taille.
*   **Déploiement Web**: La capacité d'exporter des jeux pour le web (HTML5) reste une voie d'accès majeure pour la distribution et la jouabilité instantanée, très pertinente à l'ère du cloud gaming et des plateformes de jeux en ligne.
*   **Apprentissage par la pratique**: Le conseil d'expérimenter, de tester et de ne pas hésiter à créer des copies de son projet pour des tests est une approche intemporelle et efficace pour l'apprentissage et la résolution de problèmes en développement de jeux.

{{< footer >}}
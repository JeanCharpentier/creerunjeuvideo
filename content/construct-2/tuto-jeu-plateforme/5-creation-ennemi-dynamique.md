---
title: "5. Création d'un ennemi dynamique et aménagement de niveau"
date: 2026-06-13
weight: 6
categories: ["Archive"]
tags: ["Construct 2", "Game Dev", "Tutoriel", "Ennemi", "Level Design"]
prev_url: "/construct-2/tuto-jeu-plateforme/debug-collisions-plateformes"
next_url: "/construct-2/tuto-jeu-plateforme/6-gestion-collisions-hud"
images: ["https://img.youtube.com/vi/iJu76SZhhOI/maxresdefault.jpg"]
---

> **Note :** Cet article est une archive pédagogique du cinquième épisode de ma série sur la création d'un jeu de plateforme avec Construct 2.

{{< youtube-rgpd "iJu76SZhhOI" >}}

### Points clés abordés

* **Amélioration du Level Design :** Conseils pour rendre vos niveaux plus visuels et attrayants en modifiant la disposition des éléments de décor.
* **IA d'ennemi basique :** * Mise en place d'un ennemi qui se déplace automatiquement de gauche à droite.
    * Utilisation de la logique de retournement automatique pour simuler une patrouille.
* **Organisation du code :** * Introduction aux **Groupes d'événements** : création d'un groupe dédié (`AnimJackEnemy`) pour isoler la logique de l'ennemi.
    * Activation/Désactivation des groupes au démarrage pour optimiser la lisibilité et la maintenance du projet.
* **Gestion des bugs de collision :** Identification et résolution de problèmes liés aux chutes non désirées à travers les plateformes (complémentaire au tutoriel de debug).

### Conseils d'organisation pour vos feuilles d'événements

À mesure que votre projet gagne en complexité, la structure de votre feuille d'événements devient cruciale :
* **Regroupement logique :** Ne laissez pas vos événements "flotter" sur la page. Créez des groupes par fonctionnalité (ex: `Mouvement Joueur`, `IA Ennemis`, `Animations`).
* **Gestion d'état :** L'activation de groupes au démarrage permet de garder une interface de travail propre et de structurer le comportement de chaque entité de manière indépendante.

### Exercice pratique
Pour cet épisode, l'objectif est de rendre votre niveau moins statique. Essayez d'intégrer au moins deux ennemis ayant des zones de patrouille distinctes et assurez-vous que leurs animations de retournement sont fluides en utilisant les groupes pour organiser vos événements.

{{< footer >}}
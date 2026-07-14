---
title: "2. Créer le coup d''envoi et le tir automatique dans GDevelop 5"
weight: 2
date: 2023-10-27
categories: ['Tutoriels GDevelop']
tags: ['GDevelop 5', 'Jeu 3D', 'Babby Foot', 'Développement de jeu']
images: ["https://img.youtube.com/vi/1XYaTK3cvBw/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/1XYaTK3cvBw/maxresdefault.jpg"]
---

Dans ce deuxième épisode de notre série dédiée à la création d'un baby-foot 3D sous GDevelop 5, nous passons aux choses sérieuses : la mise en jeu et l'interaction entre les joueurs et la balle. Sans coup d'envoi, pas de match, et sans tir automatique, pas de plaisir !

{{< youtube-rgpd "1XYaTK3cvBw" >}}

### Au programme de cet épisode :
*   **Structuration du code :** Utilisation des groupes d'événements pour garder un projet propre et lisible.
*   **Le Kickoff (Engagement) :** Mise en place d'un chronomètre de scène pour déclencher le mouvement de la balle après un court délai.
*   **Gestion des impulsions :** Utilisation de la force instantanée pour propulser le ballon au démarrage.
*   **Tir automatique :** Création de groupes d'objets (Red/Blue) pour gérer les collisions et renvoyer la balle avec une trajectoire aléatoire.
*   **Game Feel :** Ajout d'une légère impulsion sur l'axe Z pour donner du relief aux tirs et éviter que la balle ne reste collée au sol.

### Ce qui reste d'actualité aujourd'hui
*   **Les groupes d'objets :** Cette fonctionnalité reste indispensable pour gérer des équipes entières sans dupliquer les lignes d'événements.
*   **La gestion des forces :** Comprendre la différence entre une "impulsion" (instantanée) et une "force" (continue) est toujours la base de la physique dans GDevelop.
*   **L'aléatoire (Random) :** L'utilisation de `RandomInRange` est la méthode la plus simple et efficace pour rendre les comportements de l'IA ou des rebonds moins prévisibles et plus naturels.
*   **Le nettoyage :** Supprimer un chronomètre une fois son rôle rempli est une bonne pratique pour optimiser les performances de votre scène.

{{< footer >}}
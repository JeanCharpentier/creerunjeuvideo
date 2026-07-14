---
title: "4. Gestion des niveaux, variables et pièges"
date: 2026-06-13
weight: 4
categories: ["Archive"]
tags: ["Construct 2", "Game Dev", "Tutoriel", "Niveaux", "Variables Globales"]
prev_url: "/construct-2/tuto-jeu-plateforme/3-animations-gestion-etats-personnage"
next_url: "/construct-2/tuto-jeu-plateforme/debug-collisions-plateformes"
images: ["https://img.youtube.com/vi/fL_1EOZ0WAw/maxresdefault.jpg"]
---

> **Note :** Cet article est une archive du quatrième tutoriel de la série sur la création d'un jeu de plateforme avec Construct 2.

{{< youtube-rgpd "fL_1EOZ0WAw" >}}

### Points clés abordés

* **Architecture des niveaux :** Utilisation d'une feuille d'événement unique (`ESJOUEUR`) pour tous les niveaux afin d'éviter la duplication de code.
* **Transition de niveau dynamique :** 
    * Création d'une variable globale `Niveau Actuel` (valeur initiale : 1) pour suivre la progression.
    * Utilisation de l'action système `Go to layout by name` combinée avec une concaténation (`"niveau" & Niveau Actuel`) pour charger automatiquement le layout suivant.
* **Gestion des interactions (Panneaux) :**
    * Affichage contextuel d'une infobulle via le changement d'opacité (`Set Opacity`) lorsque le joueur chevauche le panneau.
    * Utilisation de la touche Espace pour valider le passage au niveau supérieur.
* **Implémentation de pièges :** Ajout d'objets `Spikes` provoquant le redémarrage du niveau ou le retour au menu via une collision.

### Organisation du projet

Pour maintenir une feuille d'événements lisible malgré l'ajout de fonctionnalités, il est fortement conseillé de :
* **Utiliser les commentaires :** Organisez votre feuille par sections (Fin de niveau, Pièges, etc.) pour une maintenance facilitée.
* **Regrouper les événements :** Utilisez la fonction `Add Group` pour condenser des ensembles d'actions (ex: groupe "Animations") et gagner de l'espace visuel.

### Résumé technique pour Hugo

* **Variable Globale :** `Nive Actuel` (Nombre, Initial 1).
* **Logique de chargement :** `System: Go to layout by name` -> `"niveau" & Nive Actuel`.
* **Optimisation visuelle :** Utilisation de `Set Opacity` (0 à 100) pour des effets de fondu plus élégants que la simple visibilité binaire.

{{< footer >}}
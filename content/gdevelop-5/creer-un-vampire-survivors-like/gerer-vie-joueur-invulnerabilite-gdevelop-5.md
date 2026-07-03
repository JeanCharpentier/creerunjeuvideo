---
title: "4. Gérer la vie du joueur et les frames d''invulnérabilité"
weight: 4
date: 2023-10-27
categories: ['Tutoriels']
tags: ['GDevelop 5', 'GameDev', 'Débutant', 'Survival']
---

Dans ce quatrième épisode de notre série dédiée à la création d'un jeu de type "Survival", nous allons nous attaquer à un pilier fondamental : la gestion de la santé du joueur. Il ne suffit pas d'avoir une barre de vie, il faut aussi que le joueur ressente les impacts et qu'il ne meure pas instantanément au moindre contact.

{{< youtube-rgpd "pTorx3bI3t8" >}}

### Au programme de cet épisode :
*   **Variables d'objet :** Création des variables `HP`, `HP_max` et `invulnerabilite` pour gérer l'état de santé.
*   **Feedback visuel :** Utilisation du comportement "Clignotement" (Flash) pour signaler les dégâts.
*   **Mécanique d'invulnérabilité :** Mise en place d'un système de "frames d'invulnérabilité" via un chronomètre pour éviter les dégâts en chaîne.
*   **Interface utilisateur (UI) :** Ajout d'une barre de ressources pour afficher visuellement les points de vie.
*   **Organisation :** Utilisation de groupes d'événements pour garder votre feuille d'événements propre et lisible.

### Ce qui reste d'actualité aujourd'hui
*   **La structure des variables :** Utiliser des variables numériques pour la santé et des booléens pour les états (invulnérabilité) reste la méthode standard dans GDevelop.
*   **Le comportement "Clignotement" :** C'est toujours l'outil le plus simple et efficace pour donner un retour visuel immédiat au joueur sans avoir à créer des animations complexes.
*   **L'importance de l'UI :** La séparation des calques (un calque "UI" pour l'interface et un calque "Base" pour le jeu) est une bonne pratique indispensable pour que vos éléments d'interface restent fixes à l'écran.
*   **Gestion du Debug :** Créer un groupe d'événements dédié au "Debug" dès le début du projet est un conseil précieux qui vous fera gagner un temps fou lors de la phase de test.

{{< footer >}}
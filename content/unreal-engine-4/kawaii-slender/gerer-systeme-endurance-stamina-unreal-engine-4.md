---
title: "17. Gérer un système d''endurance (Stamina)"
weight: 17
date: 2026-06-17
categories: ['Unreal Engine 4']
tags: ['Blueprint', 'GameDev', 'Stamina', 'Tutoriel']
---

Dans ce tutoriel, nous abordons une mécanique essentielle pour tout jeu d'action ou d'aventure : la gestion de l'endurance (stamina). L'objectif est de permettre à votre personnage de sprinter, tout en limitant cette capacité par une jauge qui se vide à l'effort et se régénère au repos.

{{< youtube-rgpd "M1fcGV2maUI" >}}

{{< youtube-rgpd "bmbhq_GOZKk" >}}

### Résumé du tutoriel
*   **Organisation du Blueprint :** Nettoyage de l'Event Graph avec des commentaires colorés pour une meilleure lisibilité.
*   **Utilisation de la Séquence :** Introduction du node `Sequence` pour gérer plusieurs actions sur l'`Event Tick` sans conflit.
*   **Variables nécessaires :** Création de 5 variables (2 booléens pour l'état de course, 3 floats pour la vitesse de marche, de course et la valeur d'endurance).
*   **Configuration des valeurs :** Mise en place des valeurs par défaut (vitesse de marche à 500, vitesse de course à 900, endurance max à 100).
*   **Logique de sprint :** Mise en place d'une branche conditionnelle pour vérifier si le joueur a assez d'endurance avant d'autoriser le sprint.

### Ce qui reste d'actualité aujourd'hui
Bien que ce tutoriel utilise une version plus ancienne d'Unreal Engine, les concepts fondamentaux restent parfaitement valides dans les versions récentes (UE5 inclus) :
1.  **La gestion des états via les variables :** L'utilisation de booléens pour suivre l'état du personnage (est-il en train de courir ?) est toujours la méthode standard.
2.  **L'Event Tick et la Séquence :** Le node `Sequence` reste l'outil indispensable pour organiser des logiques complexes qui doivent s'exécuter à chaque frame.
3.  **Modularité :** Remplacer des valeurs "en dur" (hardcoded) par des variables permet de créer des systèmes évolutifs (ex: buffs de vitesse, objets augmentant l'endurance).
4.  **Bonnes pratiques :** Le commentaire et l'organisation visuelle des Blueprints sont des habitudes de développement cruciales pour maintenir des projets de grande envergure.

{{< footer >}}
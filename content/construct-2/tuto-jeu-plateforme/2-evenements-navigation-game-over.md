---
title: "2. Événements et navigation : Créer un Game Over"
date: 2026-06-13
weight: 2
categories: ["Archive"]
tags: ["Construct 2", "Game Dev", "Tutoriel", "Événements", "Navigation"]
prev_url: "/construct-2/tuto-jeu-plateforme/1-creation-personnage-plateforme-c2"
next_url: "/construct-2/tuto-jeu-plateforme/3-animations-gestion-etats-personnage"
images: ["https://img.youtube.com/vi/maWbN37ey5o/maxresdefault.jpg"]
---

> **Note :** Cet article est une archive pédagogique du deuxième épisode de ma série sur la création d'un jeu de plateforme avec Construct 2.

{{< youtube-rgpd "maWbN37ey5o" >}}

### Points clés abordés

* **Logique Événement/Action :** Comprendre le principe fondamental de Construct 2 : lorsqu'une condition est remplie dans le jeu (événement), alors le moteur exécute une réaction spécifique (action).
* **Liaison des feuilles d'événements :** Apprendre à lier une feuille d'événements (Event Sheet) à un Layout spécifique via les propriétés du niveau.
* **Gestion des sorties de zone :** Utilisation de l'événement *Is Outside Layout* sur le personnage pour déclencher une réaction lorsqu'il tombe hors de l'écran.
* **Navigation entre niveaux :** Mise en place d'une interaction utilisateur (clic sur un bouton) pour changer de Layout via l'action *Go To Layout*.
* **Gestion du Game Over :** Modification dynamique d'une action existante pour créer une boucle de gameplay (retour au menu principal au lieu de simplement redémarrer le niveau).

### Ce qui reste d'actualité aujourd'hui

La logique des événements de Construct 2 reste le cœur battant du développement sur Construct 3. Bien que l'interface ait évolué, le concept de **"Condition -> Action"** et la gestion des feuilles d'événements sont des acquis universels pour tout développeur de jeux 2D. Comprendre comment lier un bouton à un changement de niveau ou gérer la sortie d'un personnage de l'aire de jeu sont des techniques que vous utiliserez dans chacun de vos projets.

### Exercice pratique (Devoirs)

Pour préparer le prochain épisode, l'objectif est de créer votre propre écran de "Game Over" :
* Intégrer un bouton pour retourner au menu principal.
* Intégrer un bouton pour redémarrer le niveau 1.

{{< footer >}}
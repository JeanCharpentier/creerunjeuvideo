---
title: "9. Système de codes de niveau"
date: 2026-06-13
weight: 12
categories: ["Archive"]
tags: ["Construct 2", "Game Dev", "Tutoriel", "Navigation", "Dictionary"]
prev_url: "/construct-2/tuto-jeu-plateforme/patch-mise-a-jour-webstorage"
next_url: "/construct-2/tuto-jeu-plateforme/10-integration-son-effets-audio"
images: ["https://img.youtube.com/vi/FabTCjh4Hjg/maxresdefault.jpg"]]
images: ["https://img.youtube.com/vi/FabTCjh4Hjg/maxresdefault.jpg"]
---

> **Note :** Cet article est une archive pédagogique du neuvième épisode de ma série sur la création d'un jeu de plateforme avec Construct 2.

{{< youtube-rgpd "FabTCjh4Hjg" >}}

### Points clés abordés

* **Saisie utilisateur :** Insertion d'un objet `TextBox` sur le calque HUD du menu pour permettre au joueur de taper un code.
* **Gestion des données avec le Dictionary :** Utilisation de l'objet `Dictionary` pour associer une clé (le code saisi) à une valeur (le nom du Layout/niveau correspondant).
* **Navigation dynamique :** Mise en place d'une logique conditionnelle pour le bouton "Jouer" :
    * Si le champ est vide : Chargement du niveau par défaut.
    * Si un code est saisi : Chargement du niveau associé via l'action `Go to layout by name`.
* **Récupération de valeur :** Utilisation de l'expression `Dictionary.Get(tbcode.Text)` pour automatiser le basculement vers le bon niveau.

### Configuration technique du Dictionary

Pour que le système fonctionne, la déclaration des codes doit se faire dès le lancement du menu :

* **Événement :** `System > On start of layout`.
* **Action :** `Dictionary > AddKey` (ou `SetKey`).
    * **Key :** "CODE_NIVEAU_2" (par exemple).
    * **Value :** "Niveau 2" (le nom exact de votre layout dans l'arborescence du projet).

### Conseils d'implémentation
* **Expérience utilisateur :** Pensez à activer l'option *Case insensitive* sur vos comparaisons de texte pour que le joueur ne soit pas bloqué par une erreur de casse.
* **Erreur de saisie :** Le système de `Go to layout by name` est sécurisé : si le dictionnaire ne trouve pas de correspondance pour le code tapé, le changement de niveau ne se déclenche pas, évitant ainsi les plantages.
* **Communication :** N'oubliez pas d'afficher les codes de niveau dans vos décors (panneaux, messages) pour que les joueurs puissent les mémoriser.

{{< footer >}}